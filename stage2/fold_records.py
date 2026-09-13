"""Stage 2, incremental: fold new records into the concept layer.

The first stage 2 run used generate_stubs.py, which (re)writes EVERY concept
page from scratch. That was right when all pages were empty stubs; today 147
pages carry a written Definition and Practice, so re-running it would erase
them. This script is the incremental counterpart (docs/adr/0005): it touches
only what a new record changes, and nothing a model wrote.

For each record whose status is `summarized` (the ones stage 2 has not folded
yet), for each candidate concept in its frontmatter:

- a page exists (name or alias, case-insensitive): append
  `- [[record]] — contribution` to its `## Sources`, refresh the count in the
  section title, bump `updated`. Nothing else on the page is touched.
- no page, but the name is cited by 2+ records across the whole corpus:
  create a stub page (same shape as generate_stubs.py) listing every citing
  record.
- no page, 1 citation: leave the wikilink dangling, as docs/adr/0003 expects.

Idempotent: a source line already present is never duplicated. Records keep
`status: summarized`; the writing pass flips them to `processed` once the
concept pages they feed are finalised (see prompts/finish-stage2.md).

Also prints the `developed` candidates under the two-works rule (ADR 0005):
5+ records AND 2+ distinct works, where a work is the record's `book` when
it has one and the record itself otherwise.

Usage: python3 stage2/fold_records.py [--write] [--book SLUG]
       [--accept-alias-capture]
"""

import argparse
import collections
import datetime
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from merge_map import MERGES, BOOK_MERGES  # noqa: E402
from singleton_map import SINGLETON_MERGES  # noqa: E402

# Aliases come from the merge maps. A BOOK_MERGES key that is already a
# global alias elsewhere ("Team Dynamics" -> Team Collaboration) is NOT
# re-registered: two pages claiming one alias is a collision verify_wiki.py
# refuses. apply_merge.py --only has already retargeted the book records.
_GLOBAL = {**MERGES, **SINGLETON_MERGES}
ALIASES = collections.defaultdict(set)
for _k, _v in _GLOBAL.items():
    ALIASES[_v].add(_k)
for _k, _v in BOOK_MERGES.items():
    if _k not in _GLOBAL:
        ALIASES[_v].add(_k)

try:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "stage3"))
    from theme_map import THEMES  # noqa: E402
    PLACED_IN_THEMES = {n for names in THEMES.values() for n in names}
except ImportError:  # theme layer absent, the warning simply goes quiet
    PLACED_IN_THEMES = set()

EP, CO = "wiki/episodes", "wiki/concepts"
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
TODAY = os.environ.get("WIKI_DATE") or datetime.date.today().isoformat()
DEVELOPED_MIN_RECORDS = 5


def parse(path):
    t = open(path, encoding="utf-8").read()
    m = FM_RE.match(t)
    if not m:
        return None, t, t
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None, t, t
    return meta, t[m.end():], t


def record_contributions(body):
    out = {}
    sec = re.search(r"## Concepts\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    if sec:
        for line in sec.group(1).splitlines():
            lm = re.match(r"- \[\[(.*?)\]\]\s*[—–-]*\s*(.*)", line.strip())
            if lm:
                out.setdefault(lm.group(1).strip(), lm.group(2).strip())
    return out


def load_records():
    recs = {}
    for f in sorted(os.listdir(EP)):
        if not f.endswith(".md"):
            continue
        meta, body, _ = parse(f"{EP}/{f}")
        if not meta:
            continue
        base = f[:-3]
        recs[base] = {
            "meta": meta,
            "concepts": [str(c).strip() for c in (meta.get("concepts") or [])],
            "contrib": record_contributions(body),
            "published": str(meta.get("published", "")),
            "work": str(meta.get("book") or base),
        }
    return recs


def load_pages():
    pages, owners = {}, {}
    for f in sorted(os.listdir(CO)):
        if not f.endswith(".md"):
            continue
        meta, body, full = parse(f"{CO}/{f}")
        if not meta:
            continue
        name = f[:-3]
        pages[name] = {"meta": meta, "body": body, "full": full, "path": f"{CO}/{f}"}
        for n in [str(meta.get("name", name))] + [str(a) for a in (meta.get("aliases") or [])]:
            owners.setdefault(n.lower(), name)
    return pages, owners


def yaml_name(c):
    return f'name: "{c}"' if ":" in c or c.startswith(("'", '"')) else f"name: {c}"


def stub_page(name, sources):
    fm = ["---", "type: concept", yaml_name(name), f"created: {TODAY}",
          f"updated: {TODAY}", "status: stub"]
    aliases = sorted(ALIASES.get(name, set()) - {name})
    if aliases:
        fm.append("aliases:")
        fm += [f'  - "{a}"' for a in aliases]
    fm.append("---")
    src = [f"- [[{b}]]" + (f" — {t}" if t else "") for _, b, t in sorted(sources)]
    body = [f"# {name}", "", "## Definition", "",
            "_Stub — to be written by the concept stage._", "",
            f"## Sources ({len(src)})", ""] + src + [""]
    return "\n".join(fm) + "\n\n" + "\n".join(body)


def add_aliases(page, name):
    """Add the merge-map aliases a page is missing. Returns new full text or None."""
    have = {str(a).lower() for a in (page["meta"].get("aliases") or [])} | {name.lower()}
    missing = sorted(a for a in ALIASES.get(name, set()) if a.lower() not in have)
    if not missing:
        return None
    full = page["full"]
    lines = "".join(f'  - "{a}"\n' for a in missing)
    if re.search(r"^aliases:\n", full, re.MULTILINE):
        full = re.sub(r"^(aliases:\n(?:  - .*\n)*)", lambda m: m.group(1) + lines, full, count=1, flags=re.MULTILINE)
    else:
        full = re.sub(r"^(status: .*\n)", lambda m: m.group(1) + "aliases:\n" + lines, full, count=1, flags=re.MULTILINE)
    return full


def add_source(page, base, contrib):
    """Append one source line and refresh the section count. Returns the new
    full text, or None when the line is already there."""
    full = page["full"]
    if f"[[{base}]]" in page["body"]:
        return None
    m = re.search(r"^## Sources(?: \((\d+)\))?\n", full, re.MULTILINE)
    if not m:
        raise RuntimeError(f"no ## Sources section in {page['path']}")
    # section spans from the heading to the next heading or end of file
    rest = full[m.end():]
    nm = re.search(r"^## ", rest, re.MULTILINE)
    section = rest[: nm.start()] if nm else rest
    tail = rest[nm.start():] if nm else ""
    lines = section.rstrip("\n").split("\n")
    count = sum(1 for l in lines if l.startswith("- [["))
    line = f"- [[{base}]]" + (f" — {contrib}" if contrib else "")
    new_section = "\n".join(lines + [line]) + "\n" + ("\n" if tail else "")
    head = full[: m.start()] + f"## Sources ({count + 1})\n"
    full = head + new_section + tail
    full = re.sub(r"^updated: .*$", f"updated: {TODAY}", full, count=1, flags=re.MULTILINE)
    return full


def stale_prose_pages(enriched, pages):
    """Developed pages that gained a source their prose never mentions.

    A `developed` page keeps the Definition and Practice it already had, so a
    fold leaves it citing a work its own text ignores. The fold cannot write
    that prose, but it can refuse to let it pass silently: these pages need a
    stage 2 refresh (prompts/stage2-write.md, integrating rather than
    rewriting) before the book is called done. Found by hand on The 10x Method
    (2026-09-08), where 7 developed pages were in that state.

    Returns [(concept name, [record basenames not cited in the prose])].
    """
    out = []
    for name, bases in sorted(enriched.items()):
        page = pages.get(name)
        if not page or page["meta"].get("status", "stub") == "stub":
            continue
        prose = page["body"].split("## Sources", 1)[0]
        uncited = [b for b in bases if f"[[{b}]]" not in prose]
        if uncited:
            out.append((name, uncited))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--accept-alias-capture", action="store_true",
                    help="write even though a BOOK_MERGES alias is cited by an "
                         "older record, after checking both senses match")
    ap.add_argument("--book", help="only fold records of this book_slug (basename contains it)")
    args = ap.parse_args()

    recs = load_records()
    pages, owners = load_pages()

    todo = {b: r for b, r in recs.items() if r["meta"].get("status") == "summarized"
            and (not args.book or args.book in b)}
    citations = collections.defaultdict(list)  # name(lower) -> [(pub, base, contrib)]
    display = {}
    for b, r in recs.items():
        for c in r["concepts"]:
            citations[c.lower()].append((r["published"], b, r["contrib"].get(c, "")))
            display.setdefault(c.lower(), c)

    enriched, created, dangling = {}, {}, collections.Counter()
    for b, r in sorted(todo.items()):
        for c in r["concepts"]:
            key = c.lower()
            owner = owners.get(key)
            if owner:
                page = pages[owner]
                new = add_source(page, b, r["contrib"].get(c, ""))
                if new is not None:
                    page["full"], page["body"] = new, new[FM_RE.match(new).end():]
                    enriched.setdefault(owner, []).append(b)
                if owner not in created:
                    new = add_aliases(page, owner)
                    if new is not None:
                        page["full"] = new
                        # record the names actually added, so the next record of
                        # this run sees them and does not add them again
                        have = {str(a).lower() for a in (page["meta"].get("aliases") or [])}
                        page["meta"]["aliases"] = list(page["meta"].get("aliases") or []) + [
                            a for a in ALIASES.get(owner, set()) if a.lower() not in have]
                        enriched.setdefault(owner, [])
            elif len(citations[key]) >= 2:
                name = display[key]
                if name not in created:
                    created[name] = stub_page(name, citations[key])
                    # register so later records in this run enrich it, not recreate it
                    pages[name] = {"meta": {"name": name}, "body": created[name],
                                   "full": created[name], "path": f"{CO}/{name}.md"}
                    owners[key] = name
            else:
                dangling[c] += 1

    print(f"records to fold: {len(todo)}")
    print(f"pages enriched: {len(enriched)}")
    for name, bs in sorted(enriched.items()):
        print(f"  {name}  +{len(bs)}")
    print(f"pages created: {len(created)}")
    for name in sorted(created):
        print(f"  {name}  ({len(citations[name.lower()])} sources)")
    print(f"dangling single-source names: {len(dangling)}")

    stale_prose = stale_prose_pages(enriched, pages)
    if stale_prose:
        print(f"\nWARNING — {len(stale_prose)} developed page(s) gain a source "
              "their prose does not mention.")
        print("Refresh Definition/Practice with prompts/stage2-write.md before closing the book:")
        for name, uncited in stale_prose:
            print(f"  {name}: {', '.join(uncited)}")

    # A BOOK_MERGES alias can capture an older, already-processed record that
    # used the same words for another idea ("Agency" of an AI assistant is
    # not "Agency" over one's own practice). verify_wiki.py then fails on a
    # missing backlink. Surface it here, before the write, so the reader rules
    # on it: same meaning, add the backlink; different meaning, drop the alias.
    #
    # An alias that already exists globally used to be skipped outright, which
    # silenced the check on the one case that most deserves it: an override,
    # where the book claims a name another page already owns (Articulating
    # Design Decisions took "Trust Building" from User Trust, 2026-09-10).
    # The override is legitimate but scoped, `apply_merge.py` only layers
    # BOOK_MERGES under --only, so it is reported rather than skipped.
    captured, overrides = [], []
    for alias, target in BOOK_MERGES.items():
        older = [b for b, r in recs.items() if b not in todo
                 and alias.lower() in {c.lower() for c in r["concepts"]}]
        if alias in _GLOBAL:
            if _GLOBAL[alias] != target:
                overrides.append((alias, _GLOBAL[alias], target, older))
            continue
        if older:
            # Already an alias of its target: the stamp happened in an earlier
            # book and the gate has lived with it. Report it, but do not refuse
            # this write over history that is not being changed here.
            tp = pages.get(target)
            fresh = alias.lower() not in {str(a).lower()
                                          for a in ((tp or {}).get("meta", {}).get("aliases") or [])}
            captured.append((alias, target, older, fresh))
    if captured:
        print(f"\nWARNING: {len(captured)} book alias(es) also cited by older records, "
              "same meaning? (backlink them or drop the alias)")
        for alias, target, older, fresh in captured:
            mark = "" if fresh else "  (already an alias of the target, pre-existing)"
            print(f"  {alias} -> {target}: {', '.join(older)}{mark}")
    if overrides:
        print(f"\nWARNING: {len(overrides)} book alias(es) override a global one. The "
              "override lives only in a --only pass, so a later source proposing the "
              "same name goes back to the global target: say on the page which sense "
              "it now covers, or the decision is lost.")
        for alias, was, now, older in overrides:
            print(f"  {alias}: globally -> {was}, this book -> {now}")
            if older:
                print(f"    also cited by {len(older)} older record(s) in the other "
                      f"sense: {', '.join(older[:5])}")

    # developed candidates under the two-works rule
    candidates = []
    print("\ndeveloped candidates (5+ records, 2+ works), currently stub:")
    for name, page in sorted(pages.items()):
        if page["meta"].get("status", "stub") != "stub":
            continue
        # Under ## Sources only: a Practice bullet that opens with the record
        # it cites is not an extra source (same defect as generate_themes.py,
        # 2026-09-10), and here it would inflate the developed count.
        _b = page["body"]
        _i = _b.find("\n## Sources")
        srcs = re.findall(r"^- \[\[(.*?)\]\]", _b[_i:] if _i >= 0 else "",
                          re.MULTILINE)
        works = {recs[s]["work"] for s in srcs if s in recs}
        if len(srcs) >= DEVELOPED_MIN_RECORDS and len(works) >= 2:
            candidates.append(name)
            print(f"  {name}: {len(srcs)} records, {len(works)} works")

    # verify_wiki.py fails on a `developed` concept that belongs to no theme.
    # Writing a page flips its status, so the theme placement has to land in
    # the same pass, not after the gate has already gone red.
    already_developed = [n for n, p_ in pages.items()
                         if p_["meta"].get("status") == "developed"]
    unplaced = sorted(n for n in candidates + already_developed
                      if n not in PLACED_IN_THEMES)
    if unplaced:
        print(f"\nWARNING — {len(unplaced)} concept(s) will fail verify_wiki.py "
              "once written: developed and in no theme.")
        print("Add them to stage3/theme_map.py THEMES before the next gate:")
        for name in unplaced:
            print(f"  {name}")

    if not args.write:
        print("\n(dry run; pass --write to apply)")
        return
    # A captured alias is not advisory. --write stamps it onto the concept page,
    # and verify_wiki.py then demands a backlink the older record cannot earn:
    # it links the alias, but its content belongs to the other sense. That is
    # how "Problem Solving" (chapter 12 = exploring solutions,
    # 2016-07-31_design-thinking = defining the problem) turned the gate red
    # after the fold had already run (2026-09-10). Rule on it before writing.
    fresh_captures = [c for c in captured if c[3]]
    if fresh_captures:
        print("\nREFUSED — the book alias(es) above are cited by older records. "
              "Either drop the alias from BOOK_MERGES (the older record keeps "
              "its own sense), or promote it to MERGES and re-run "
              "apply_merge.py with no --only so those records fold in too.\n"
              "Pass --accept-alias-capture only once you have checked that "
              "both senses really are the same idea.")
        if not args.accept_alias_capture:
            raise SystemExit(1)
        print("(--accept-alias-capture: writing anyway)")
    for name in enriched:
        open(pages[name]["path"], "w", encoding="utf-8").write(pages[name]["full"])
    for name, text in created.items():
        open(f"{CO}/{name}.md", "w", encoding="utf-8").write(text)
    print("\nwritten.")


if __name__ == "__main__":
    main()
