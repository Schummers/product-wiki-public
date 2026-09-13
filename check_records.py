"""Stage 1 quality gate: schema conformance and quote fidelity.

Checks every record that has a raw counterpart, or only those named on the
command line. Reports, never fixes: a defect here means the stage 1 prompt
needs correcting, not the output patching.

Usage:
    python3 check_records.py [basename ...]
"""

import glob
import os
import re
import sys
import unicodedata

import yaml

EPISODES_DIR = "wiki/episodes"
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
REQUIRED = ["type", "name", "created", "published", "source_type", "status",
            "url", "author", "raw", "concepts"]
SECTIONS = ["Summary", "Key Takeaways", "Quotes", "Concepts"]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    for a, b in [("“", '"'), ("”", '"'), ("’", "'"),
                 ("‘", "'"), ("–", "-"), ("—", "-")]:
        s = s.replace(a, b)
    # A quote lifted from a link keeps the link text, not the URL, so the
    # raw side must be collapsed the same way before comparing.
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    # pandoc escapes punctuation in raw ("\$10M", "\[...\]"); the record
    # quotes it unescaped.
    s = re.sub(r"[*_`\[\]()#>\\]", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def check(basename):
    path = f"{EPISODES_DIR}/{basename}.md"
    problems = []
    content = open(path, encoding="utf-8").read()

    m = FM_RE.match(content)
    if not m:
        return ["no frontmatter"]
    try:
        meta = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return [f"invalid YAML: {str(e)[:80]}"]
    body = content[m.end():]

    for field in REQUIRED:
        if not meta.get(field):
            problems.append(f"missing field: {field}")
    if meta.get("type") != "source":
        problems.append(f"type is {meta.get('type')!r}, expected 'source'")

    raw_path = meta.get("raw", "")
    if not os.path.exists(raw_path):
        problems.append(f"raw not found: {raw_path}")
        raw_norm = ""
    else:
        raw_norm = norm(open(raw_path, encoding="utf-8").read())

    concepts = meta.get("concepts") or []
    # Stage 1 asks for 3-6 *candidate* names. Stage 2 merges candidates onto
    # canonical names, so a record legitimately ends up with fewer once two of
    # its candidates turn out to be the same concept. The floor therefore only
    # applies before the merge; the ceiling still catches a record that lists
    # more concepts than it can meaningfully cover.
    if not 1 <= len(concepts) <= 6:
        problems.append(f"{len(concepts)} concepts, expected 1-6 (3-6 before stage 2)")
    for c in concepts:
        if "[[" in str(c):
            problems.append(f"concept is a wikilink: {c}")

    found = re.findall(r"^## (.+)$", body, re.MULTILINE)
    if found != SECTIONS:
        problems.append(f"sections {found}, expected {SECTIONS}")

    # Bold must wrap the label only, never the whole bullet.
    for bad in re.findall(r"^- \*\*[^*]*—[^*]*\*\*\s*$", body, re.MULTILINE):
        problems.append(f"bullet fully bolded: {bad[:60]}")

    quotes = re.findall(r"^> (.+)$", body, re.MULTILINE)
    if not 1 <= len(quotes) <= 3:
        problems.append(f"{len(quotes)} quotes, expected 1-3")
    if raw_norm:
        for q in quotes:
            if norm(q).strip('"') not in raw_norm:
                problems.append(f"quote not verbatim: {q[:70]}")

    # Every frontmatter concept must appear as a wikilink in ## Concepts.
    linked = {l.strip() for l in re.findall(r"\[\[(.*?)\]\]", body)}
    for c in concepts:
        if str(c).strip() not in linked:
            problems.append(f"concept not linked in body: {c}")

    # apply_merge.py dedupes the frontmatter list but retargets body wikilinks
    # one by one, so two candidates merged onto the same name leave two bullets
    # pointing at it. fold_records.py then copies both into the concept page's
    # ## Sources. Caught by hand on The 10x Method (2026-09-08); a merged bullet
    # has to be folded into its twin, not left doubled.
    concepts_section = body.split("## Concepts", 1)[-1]
    bullets = re.findall(r"^- \[\[(.*?)\]\]", concepts_section, re.MULTILINE)
    for name in sorted({b for b in bullets if bullets.count(b) > 1}):
        problems.append(f"concept linked twice in ## Concepts: {name}")

    return problems


def main():
    args = sys.argv[1:]
    # --book SLUG: the runbook told the reader to build the basename list in a
    # shell variable and splat it. zsh does not word-split an unquoted
    # variable, so that command passed all 30 names as one filename and died
    # on "File name too long" (2026-09-10). Naming the book is one argument
    # and cannot be quoted wrong.
    if "--book" in args:
        i = args.index("--book")
        slug = args[i + 1]
        names = sorted(os.path.splitext(os.path.basename(p))[0]
                       for p in glob.glob(f"{EPISODES_DIR}/*{slug}*.md"))
        if not names:
            sys.exit(f"no record in {EPISODES_DIR} matches --book {slug}")
        args = args[:i] + args[i + 2:]
    elif args:
        names = [a.removesuffix(".md") for a in args]
    else:
        names = sorted(
            os.path.splitext(os.path.basename(p))[0]
            for p in glob.glob(f"{EPISODES_DIR}/*.md")
        )

    clean, dirty = 0, 0
    for name in names:
        problems = check(name)
        if problems:
            dirty += 1
            print(f"\n{name}")
            for p in problems:
                print(f"  - {p}")
        else:
            clean += 1
    print(f"\nclean: {clean}, with problems: {dirty}")


if __name__ == "__main__":
    main()
