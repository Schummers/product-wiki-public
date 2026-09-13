"""Stage 0 for books: one EPUB becomes one raw file per chapter.

Pure script, no LLM (CLAUDE.md, "Pipeline"; docs/adr/0005). The EPUB stays in
the library outside AI OS; only the extracted text enters `raw/sources/`, one
file per chapter, named `<published>_<book-slug>_<NN>-<chapter-slug>.md`.

How a chapter is found: the NCX table of contents, never the HTML headings.
An EPUB born from a PDF (Calibre "PDF Reflow") has no `<h1>` at all, only
`page_N` anchors targeted by the NCX. Each NCX entry is a cut point; a chapter
is the text between two cut points, in document order (spine order, then
anchor position; `playOrder` is not trusted, it is wrong in such EPUBs).

Conversion: the spine's HTML files go through pandoc
(`-f html -t gfm-raw_html --wrap=none`), which drops the Calibre spans and
raw HTML. Images are removed.

`--rejoin-lines`, for PDF-born EPUBs: Calibre emits one `<p>` per PDF line,
plus page numbers and running headers. This pass drops those, merges the
lines of a paragraph back together and repairs hyphenation ("mythi-" +
"cal"). Heuristic, documented in `rejoin_paragraphs()`: the most common `<p>`
class is the continuation line; a blank paragraph, a paragraph in another
class (unless it starts in lower case), or a paragraph whose text is entirely
wrapped in a `<span>`/`<b>` (a heading) starts a new block. Bare page numbers
are dropped, as are running headers (the span class that wraps page numbers).
Verify with `--dry-run` and read a sample: tables and figures come out as
loose lines, that is the residual defect.

Idempotent: a chapter whose output file exists is skipped, like
fetch_nngroup.py.

Usage:
    .venv/bin/python fetch_epub.py BOOK.epub --url URL --topics a,b \
        [--title T] [--author A] [--published YYYY-MM-DD] [--slug S] \
        [--rejoin-lines] [--strip-page-numbers] [--min-chars 1500] \
        [--exclude REGEX ...] [--absorb REGEX ...] [--relabel 'RE=REPL' ...] \
        [--dry-run]

    --exclude   drop the segment entirely (editorial apparatus). Adds to the
                default list (title page, copyright, contents, acknowledgements,
                about the author, references, glossary, further readings...).
    --absorb    merge the segment's text into the preceding chapter, drop its
                label (a tear sheet or sidebar the NCX lists as a chapter).
    --relabel   regex substitution applied to NCX labels before anything
                else, e.g. '^art (\\d)=Part \\1' to repair a truncated label.
"""

import argparse
import os
import posixpath
import re
import subprocess
import sys
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter

from bs4 import BeautifulSoup, NavigableString, Tag

OUTPUT_DIR = "raw/sources"
PANDOC = ["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"]
MARK = "@@CUT{}@@"
MARK_RE = re.compile(r"@@CUT(\d+)@@")

DEFAULT_EXCLUDE = [
    r"^(title ?page|cover|copyright|contents|table of contents|dedication)\b",
    r"^(acknowledg(e)?ments?|about the authors?|about the author|references|"
    r"bibliography|notes|glossary|further readings?|index|endnotes)\b",
]
PART_RE = re.compile(r"^part\b", re.IGNORECASE)
# A label that names a chapter. Used only to warn: a segment that calls
# itself a chapter and is nonetheless merged forward into another one is
# almost always --min-chars swallowing a short chapter opener.
CHAPTER_RE = re.compile(r"^(chapter|chapitre)\b", re.IGNORECASE)
# An NCX entry shorter than this is reported in the dry run's SHORT SEGMENTS
# block. Not a threshold the script acts on: a decision it refuses to make
# silently.
SHORT_SEGMENT_CHARS = 2000
# A planned chapter bigger than this AND four times the median is the symptom
# of an NCX that lists parts instead of chapters (see the warning below).
OUTSIZED_CHAPTER_CHARS = 60000


# --------------------------------------------------------------------------
# EPUB reading
# --------------------------------------------------------------------------

def _local(tag):
    return tag.rsplit("}", 1)[-1]


def _find_all(root, name):
    return [el for el in root.iter() if _local(el.tag) == name]


def _text(root, name):
    els = _find_all(root, name)
    return " ".join((els[0].text or "").split()) if els else ""


def read_epub(path):
    z = zipfile.ZipFile(path)
    container = ET.fromstring(z.read("META-INF/container.xml"))
    opf_path = _find_all(container, "rootfile")[0].attrib["full-path"]
    opf_dir = posixpath.dirname(opf_path)
    opf = ET.fromstring(z.read(opf_path))

    def rel(href):
        return posixpath.normpath(posixpath.join(opf_dir, href)) if opf_dir else href

    manifest = {item.attrib["id"]: rel(item.attrib["href"]) for item in _find_all(opf, "item")}
    spine_el = _find_all(opf, "spine")[0]
    spine = [manifest[ref.attrib["idref"]] for ref in _find_all(spine_el, "itemref")]

    meta = {
        "title": _text(opf, "title"),
        "author": ", ".join(" ".join((c.text or "").split()) for c in _find_all(opf, "creator")),
        "published": _text(opf, "date")[:10],
    }

    ncx_path = manifest.get(spine_el.attrib.get("toc", ""))
    if not ncx_path:
        ncx_path = next((h for h in manifest.values() if h.endswith(".ncx")), None)
    if not ncx_path:
        sys.exit("No NCX found: this script cuts on the NCX, nothing else.")
    ncx = ET.fromstring(z.read(ncx_path))

    entries = []
    for nav in _find_all(ncx, "navPoint"):
        label = _text(nav, "text")
        contents = _find_all(nav, "content")
        if not label or not contents:
            continue
        file_, _, anchor = contents[0].attrib["src"].partition("#")
        # `_find_all` flattens the tree, so nesting has to be recorded here:
        # a navPoint holding navPoints of its own is a chapter whose
        # sub-sections each became a cut point. That, not a count, is what
        # tells a nested NCX from a flat one.
        has_children = any(el is not nav and _local(el.tag) == "navPoint"
                           for el in nav.iter())
        entries.append({"label": label, "file": rel(file_), "anchor": anchor,
                        "has_children": has_children})
    return z, spine, entries, meta


# --------------------------------------------------------------------------
# Labels
# --------------------------------------------------------------------------

def clean_label(label, relabels, strip_page_numbers):
    for pattern, repl in relabels:
        label = re.sub(pattern, repl, label)
    if strip_page_numbers:
        label = re.sub(r"\s+\d{1,4}$", "", label)
    return label.strip()


def slugify(text, max_len=60):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rsplit("-", 1)[0]
    return text or "chapter"


def norm_text(s):
    return " ".join(s.split()).lower()


# --------------------------------------------------------------------------
# HTML preparation: cut markers, line rejoining, image removal
# --------------------------------------------------------------------------

def body_paragraphs(body):
    return [c for c in body.children if isinstance(c, Tag) and c.name == "p"]


def insert_markers(soup, targets, snap):
    """Put a MARK text node at each cut point. `targets` = [(index, anchor,
    label)]. With `snap`, a page anchor moves forward to the paragraph whose
    text equals the label, when one exists before the next page anchor:
    a page-based NCX points at the top of the page, not at the title."""
    body = soup.body or soup
    for index, anchor, label in targets:
        if not anchor:
            body.insert(0, NavigableString(MARK.format(index)))
            continue
        el = soup.find(id=anchor)
        if el is None:
            print(f"  WARNING anchor #{anchor} not found for '{label}'", file=sys.stderr)
            continue
        if snap:
            want = norm_text(label)
            for sib in [el] + list(el.find_next_siblings()):
                if sib is not el and sib.get("id", "").startswith("page_"):
                    break
                text = norm_text(sib.get_text())
                if text == want or (len(text) >= 4 and want.startswith(text)):
                    el = sib
                    break
        el.insert(0, NavigableString(MARK.format(index)))


def is_block(p):
    """A paragraph whose text lives entirely inside span/b/i is a heading or
    a set-off line, never a continuation line."""
    text = p.get_text().strip()
    if not text:
        return False
    for child in p.children:
        if isinstance(child, NavigableString):
            if child.strip() and not MARK_RE.fullmatch(child.strip()):
                return False
        elif child.name not in ("span", "b", "i", "strong", "em"):
            return False
    return True


def page_furniture_classes(paragraphs):
    """Span classes that wrap page numbers wrap running headers too."""
    digits, total = Counter(), Counter()
    for p in paragraphs:
        spans = p.find_all("span")
        if len(spans) == 1 and norm_text(spans[0].get_text()) == norm_text(p.get_text()):
            cls = " ".join(spans[0].get("class", []))
            total[cls] += 1
            if p.get_text().strip().isdigit():
                digits[cls] += 1
    return {c for c in total if digits[c] >= 5 and digits[c] / total[c] >= 0.5}


def rejoin_paragraphs(soup):
    """Merge PDF lines back into paragraphs. See module docstring."""
    body = soup.body or soup
    paragraphs = body_paragraphs(body)
    furniture = page_furniture_classes(paragraphs)
    classes = Counter(" ".join(p.get("class", [])) for p in paragraphs
                      if p.get_text().strip() and not is_block(p))
    dominant = classes.most_common(1)[0][0] if classes else ""

    # 1. drop page numbers and running headers, plus the blank lines glued to
    #    them (a page break must not read as a paragraph break)
    for i, p in enumerate(paragraphs):
        spans = p.find_all("span")
        bare_number = p.get_text().strip().isdigit()
        if ((bare_number or (len(spans) == 1 and " ".join(spans[0].get("class", [])) in furniture))
                and not MARK_RE.search(p.get_text())):
            for j in (i - 1, i + 1):
                if 0 <= j < len(paragraphs) and not paragraphs[j].get_text().strip() \
                        and paragraphs[j].parent is not None:
                    paragraphs[j].decompose()
            p.decompose()
    paragraphs = body_paragraphs(body)

    # 2. merge continuation lines
    prev, prev_class, prev_block = None, None, False
    for p in paragraphs:
        text = p.get_text()
        cls = " ".join(p.get("class", []))
        if not text.strip():
            prev = None
            continue
        # A line starting in lower case can only be a continuation, whatever
        # its class or wrapping (the last line of a paragraph often carries
        # its own class; summary lines sit in spans).
        starts_lower = text.lstrip()[:1].islower()
        if starts_lower and prev is not None:
            pass
        elif is_block(p) or MARK_RE.match(text.lstrip()) or prev is None \
                or prev_block or (cls != prev_class and cls != dominant):
            prev, prev_class, prev_block = p, cls, is_block(p)
            continue
        # join p into prev
        last = None
        for node in prev.descendants:
            if isinstance(node, NavigableString) and node.strip():
                last = node
        first_text = p.get_text().lstrip()
        if last is not None and last.rstrip().endswith("-") and first_text[:1].islower():
            last.replace_with(NavigableString(last.rstrip()[:-1]))
        elif last is not None:
            last.replace_with(NavigableString(last.rstrip() + " "))
        for child in list(p.children):
            prev.append(child.extract() if isinstance(child, Tag) else NavigableString(str(child)))
        p.decompose()
        prev_class, prev_block = cls, False


def flatten_table_cells(soup):
    """Make every table renderable as a GFM pipe table.

    pandoc's gfm writer can only express a table whose cells hold inline
    content. A cell containing a list or several paragraphs is not
    representable, and with `-raw_html` there is no HTML fallback either, so
    pandoc emits a bare `[TABLE]` and the content is gone. Eight tables of
    *Articulating Design Decisions* vanished this way before anyone noticed
    (2026-09-10), including the five stakeholder-value tables its chapter 2 is
    built around. See `docs/adr/0006`.

    Flattening the block content down to inline text loses the layout, which is
    not what a record cites, and keeps the words, which is.
    """
    flattened = 0
    for cell in soup.find_all(["td", "th"]):
        blocks = cell.find_all(["ul", "ol", "p", "div", "blockquote",
                                "h1", "h2", "h3", "h4", "h5", "h6"])
        if not blocks:
            continue
        # Outermost first: replacing a parent takes its descendants with it,
        # and `find_all` returns document order, so a block already detached
        # by an earlier replacement is skipped rather than re-processed.
        for blk in blocks:
            if blk.find_parent() is None:
                continue
            # Direct children only: a nested list is already inside its
            # parent `li`'s text, and recursing would emit it twice.
            items = blk.find_all("li", recursive=False)
            text = (" ; ".join(li.get_text(" ", strip=True) for li in items)
                    if items else blk.get_text(" ", strip=True))
            blk.replace_with(NavigableString(text + " " if text else ""))
        flattened += 1
    return flattened


def prepare_html(html, targets, rejoin, snap):
    soup = BeautifulSoup(html, "html.parser")
    for img in soup.find_all(["img", "svg"]):
        img.decompose()
    flatten_table_cells(soup)
    insert_markers(soup, targets, snap)
    if rejoin:
        rejoin_paragraphs(soup)
    return str(soup)


def to_markdown(html):
    out = subprocess.run(PANDOC, input=html.encode("utf-8"), capture_output=True, check=True)
    return out.stdout.decode("utf-8")


# --------------------------------------------------------------------------
# Segment post-processing
# --------------------------------------------------------------------------

def tidy(text, label):
    lines = []
    for line in text.split("\n"):
        s = line.strip()
        if s == "\\" or re.fullmatch(r"!\[[^\]]*\]\([^)]*\)", s):
            continue
        line = re.sub(r"^>\s*[●•]\s+", "- ", line)
        line = line.rstrip()
        lines.append(line)
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    # Promote the title line when it opens the segment.
    first, _, rest = text.partition("\n")
    bare = re.sub(r"^[>#*\s]+|[*\s]+$", "", first)
    if bare and norm_text(bare) == norm_text(label):
        text = f"# {bare}" + ("\n" + rest if rest else "")
    return text + "\n"


def yaml_str(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("epub")
    ap.add_argument("--title")
    ap.add_argument("--author")
    ap.add_argument("--published", help="YYYY-MM-DD, overrides the OPF date")
    ap.add_argument("--url", default="")
    ap.add_argument("--slug")
    ap.add_argument("--topics", default="")
    ap.add_argument("--rejoin-lines", action="store_true")
    ap.add_argument("--strip-page-numbers", action="store_true",
                    help="drop a trailing page number from NCX labels ('Strategy 26')")
    ap.add_argument("--min-chars", type=int, default=1500)
    ap.add_argument("--exclude", action="append", default=[])
    ap.add_argument("--absorb", action="append", default=[])
    ap.add_argument("--relabel", action="append", default=[], metavar="RE=REPL")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(OUTPUT_DIR):
        sys.exit(f"Run me from the vault root: {OUTPUT_DIR} not found.")

    z, spine, entries, meta = read_epub(args.epub)
    title = args.title or meta.get("title") or ""
    author = args.author or meta.get("author") or ""
    published = args.published or meta.get("published") or ""
    slug = args.slug or slugify(title, 40)
    topics = [t.strip() for t in args.topics.split(",") if t.strip()]
    if not (title and author and published):
        sys.exit("title, author and published are required (OPF or --title/--author/--published).")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", published):
        sys.exit(f"published must be YYYY-MM-DD, got {published!r}")

    relabels = []
    for r in args.relabel:
        pat, _, repl = r.partition("=")
        relabels.append((pat, repl))
    excludes = [re.compile(p, re.IGNORECASE) for p in DEFAULT_EXCLUDE + args.exclude]
    absorbs = [re.compile(p, re.IGNORECASE) for p in args.absorb]

    # Order the cut points by document position, not by playOrder.
    spine_pos = {f: i for i, f in enumerate(spine)}
    anchors_order = {}
    for e in entries:
        e["label"] = clean_label(e["label"], relabels, args.strip_page_numbers)
        if e["file"] not in spine_pos:
            print(f"  WARNING NCX target not in spine: {e['file']}", file=sys.stderr)
            e["pos"] = (10**6, 0)
            continue
        if e["file"] not in anchors_order:
            html = z.read(e["file"]).decode("utf-8", errors="replace")
            anchors_order[e["file"]] = {m.group(1): i for i, m in
                                        enumerate(re.finditer(r'\bid="([^"]+)"', html))}
        e["pos"] = (spine_pos[e["file"]],
                    -1 if not e["anchor"] else anchors_order[e["file"]].get(e["anchor"], 10**6))
    entries = [e for e in entries if e["pos"][0] < 10**6]
    entries.sort(key=lambda e: e["pos"])
    for i, e in enumerate(entries):
        e["index"] = i

    # Convert the whole spine with markers, then split on the markers.
    by_file = {}
    for e in entries:
        by_file.setdefault(e["file"], []).append((e["index"], e["anchor"], e["label"]))
    chunks = []
    for f in spine:
        if not f.endswith((".html", ".xhtml", ".htm")):
            continue
        html = z.read(f).decode("utf-8", errors="replace")
        prepared = prepare_html(html, by_file.get(f, []), args.rejoin_lines, args.rejoin_lines)
        chunks.append(to_markdown(prepared))
    full = "\n\n".join(chunks)

    pieces = MARK_RE.split(full)
    # pieces = [before first mark, idx, text, idx, text, ...]
    seg_text = {}
    for k in range(1, len(pieces), 2):
        seg_text[int(pieces[k])] = pieces[k + 1]
    for e in entries:
        e["text"] = tidy(seg_text.get(e["index"], ""), e["label"])
        e["chars"] = len(e["text"].strip())

    # Plan: exclude, absorb, merge short segments forward, track parts.
    chapters = []
    part = ""
    pending = []  # short segments waiting to merge into the next chapter
    for e in entries:
        lab = e["label"]
        if any(x.search(lab) for x in excludes):
            e["action"] = "excluded"
            continue
        if any(x.search(lab) for x in absorbs):
            if chapters:
                chapters[-1]["text"] += "\n" + e["text"]
                chapters[-1]["chars"] += e["chars"]
                e["action"] = f"absorbed into '{chapters[-1]['label']}'"
            else:
                e["action"] = "absorbed into nothing (dropped)"
            continue
        if PART_RE.match(lab):
            part = lab
        if e["chars"] < args.min_chars:
            pending.append(e)
            e["action"] = "merged forward"
            continue
        text = "".join(p["text"] + "\n" for p in pending) + e["text"]
        chapters.append({"label": lab, "part": part, "text": text,
                         "chars": e["chars"] + sum(p["chars"] for p in pending),
                         "merged": [p["label"] for p in pending]})
        pending = []
        e["action"] = "chapter"
    if pending and chapters:
        chapters[-1]["text"] += "\n" + "".join(p["text"] + "\n" for p in pending)
        chapters[-1]["chars"] += sum(p["chars"] for p in pending)
        for p in pending:
            p["action"] = f"merged back into '{chapters[-1]['label']}'"

    for n, ch in enumerate(chapters, 1):
        ch["number"] = n
        ch["path"] = os.path.join(OUTPUT_DIR, f"{published}_{slug}_{n:02d}-{slugify(ch['label'])}.md")

    # Report
    print(f"{title} — {author} — {published} — slug {slug}")
    print(f"NCX entries: {len(entries)}, chapters: {len(chapters)}, "
          f"total chars kept: {sum(c['chars'] for c in chapters)}")
    for e in entries:
        print(f"  [{e['chars']:6d}] {e['label'][:60]:60s} {e['action']}")
    # Short segments are where a cut plan goes wrong: a tear sheet the NCX
    # lists as a chapter, an introduction split in three, a chapter whose
    # title got its own NCX entry. Each one is an --absorb/--exclude decision
    # that costs nothing now and costs deleting raw files later.
    short = [e for e in entries
             if e["chars"] < SHORT_SEGMENT_CHARS and e["action"] != "excluded"]
    if short:
        print(f"  SHORT SEGMENTS ({len(short)} under {SHORT_SEGMENT_CHARS} chars) "
              "— rule on each one before writing:")
        for e in short:
            print(f"    [{e['chars']:6d}] {e['label'][:55]:55s} currently: {e['action']}")
        print("    absorb it (--absorb REGEX), drop it (--exclude REGEX), "
              "or accept the merge shown above.")
    # A nested NCX (depth > 1) lists every sub-section as an entry, so the cut
    # plan explodes into dozens of fragments unless an --absorb folds them back
    # into their chapter. Learned on Articulating Design Decisions (2026-09-10):
    # 66 NCX entries for 12 chapters.
    #
    # This used to be a ratio, `len(entries) >= 3 * spine files`, which asked
    # the wrong question: an EPUB that puts many flat chapters in one spine
    # file tripped it every time and was told to absorb sections it does not
    # have, while a nested NCX with one sub-section per chapter slipped past.
    # Nesting is observable, so observe it.
    parents = [e for e in entries if e["has_children"]]
    if not absorbs and parents:
        print(f"  WARNING: the NCX is nested. {len(parents)} of {len(entries)} entries "
              "have sub-entries of their own, and every sub-section becomes its own "
              f"segment, so this cuts into {len(entries)} fragments rather than "
              f"{len(parents)} chapters. Fold them back with an --absorb, "
              "e.g. --absorb '^(?!chapter \\d+\\.)'.")
    # --min-chars merges a short segment into the NEXT chapter. When that
    # segment is itself a chapter opener (the intro before its first
    # sub-section), it collapses two chapters into one and sends every
    # following --absorb into the wrong chapter. Same run, same book.
    swallowed = [e for e in entries
                 if e["action"] == "merged forward" and CHAPTER_RE.match(e["label"])]
    if swallowed:
        print(f"  WARNING: {len(swallowed)} segment(s) labelled as a chapter are "
              f"merged forward by --min-chars {args.min_chars}, which fuses them "
              "into the next chapter and misroutes any --absorb that follows:")
        for e in swallowed:
            print(f"    [{e['chars']:6d}] {e['label'][:55]}")
        print("    lower --min-chars (1 keeps every chapter opener) or exclude them.")
    # The opposite failure of a nested NCX: an NCX that lists almost nothing.
    # UX Research (Calibre, PDF-born, 2026-09-10) shipped 4 navPoints for a
    # 15-chapter book, none of them a chapter, and the naive plan produced
    # three files, one of 360 000 characters. Nothing warned: every entry was
    # accounted for, and no segment was short. An outsized chapter is the
    # observable symptom, so observe it.
    if chapters:
        median = sorted(c["chars"] for c in chapters)[len(chapters) // 2]
        huge = [ch for ch in chapters
                if ch["chars"] > OUTSIZED_CHAPTER_CHARS and ch["chars"] > 4 * median]
        if huge:
            print(f"  WARNING: {len(huge)} planned chapter(s) are far larger than the "
                  f"median ({median} chars). An NCX that does not actually list the "
                  "book's chapters cuts a whole part into one file:")
            for ch in huge:
                print(f"    [{ch['chars']:7d}] {ch['label'][:55]}")
            print("    check the NCX against the book's table of contents. If it lists "
                  "parts rather than chapters, rebuild it: this script cuts on the NCX "
                  "and on nothing else.")
    # pandoc's gfm writer replaces any table it cannot express as a pipe table
    # (block content in a cell, a grid table) with a bare "[TABLE]" marker,
    # and `-raw_html` removes the HTML fallback that would otherwise carry it.
    # The content is simply gone. Learned on Articulating Design Decisions
    # (2026-09-10): the five stakeholder-value tables of chapter 2 and one of
    # the chapter 8 case studies vanished this way, and nothing said so.
    lost = [(ch["label"], ch["text"].count("\n[TABLE]\n")) for ch in chapters]
    lost = [(lab, n) for lab, n in lost if n]
    if lost:
        print(f"  WARNING: pandoc could not express {sum(n for _, n in lost)} table(s) as "
              "GFM pipe tables and left a bare [TABLE] marker instead; their content is "
              "absent from the raw file:")
        for lab, n in lost:
            print(f"    {n:3d} in {lab[:60]}")
        print("    read those tables in the book before writing the records: a record must "
              "not assert what they held, nor count the items of a list they belonged to.")
    print()
    extraction = ("fetch_epub.py: NCX cut, pandoc html->gfm-raw_html, images removed"
                  + ("; --rejoin-lines" if args.rejoin_lines else "")
                  + (f"; --min-chars {args.min_chars}")
                  + ("; --strip-page-numbers" if args.strip_page_numbers else "")
                  # The cut plan is part of the provenance: without the absorb
                  # and exclude patterns, replaying the recorded command does
                  # not reproduce the file. Articulating Design Decisions cuts
                  # into 66 fragments without its --absorb, and the field used
                  # to claim an extraction that produced 12.
                  + "".join(f"; --exclude '{p}'" for p in args.exclude)
                  + "".join(f"; --absorb '{p}'" for p in args.absorb)
                  + "".join(f"; --relabel '{p}'" for p in args.relabel))
    written = skipped = 0
    for ch in chapters:
        merged = f" (+ {', '.join(ch['merged'])})" if ch["merged"] else ""
        state = "exists" if os.path.exists(ch["path"]) else ("would write" if args.dry_run else "write")
        print(f"  {ch['number']:02d} [{ch['chars']:6d}] {state:11s} {ch['label']}{merged}"
              + (f"  [part: {ch['part']}]" if ch["part"] else ""))
        if args.dry_run or state == "exists":
            skipped += state == "exists"
            continue
        fm = [
            "---",
            f"title: {yaml_str(title + ': ' + ch['label'])}",
            f"date: {yaml_str(published)}",
            f"url: {yaml_str(args.url)}",
            f"author: {yaml_str(author)}",
            f"topics: [{', '.join(topics)}]",
            "type: book",
            f"book: {yaml_str(title)}",
            f"book_slug: {slug}",
            f"part: {yaml_str(ch['part'])}",
            f"chapter: {yaml_str(ch['label'])}",
            f"chapter_number: {ch['number']}",
            f"extraction: {yaml_str(extraction)}",
            "---",
            "",
        ]
        with open(ch["path"], "w", encoding="utf-8") as f:
            f.write("\n".join(fm) + ch["text"])
        written += 1
    if not args.dry_run:
        print(f"\nwritten: {written}, already present: {skipped}")


if __name__ == "__main__":
    main()
