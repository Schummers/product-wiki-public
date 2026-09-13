"""Generate wiki/themes/ from the curated map plus the corpus.

Deterministic and idempotent. Curation lives in theme_map.py, judgement in
theme_prose.py; this script only assembles. Re-running after an ingestion
refreshes counts, rank-2 attachments and the router without touching a single
line a model wrote.

Rank 1 = `developed` concepts, curated in theme_map.THEMES.
Rank 2 = stubs and single-source concepts, DERIVED: a rank-2 concept lands in
the themes of the rank-1 concepts it shares records with. No hand-curation, so
an ingestion re-files them automatically.
"""

import collections
import glob
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from theme_map import THEMES  # noqa: E402

try:
    from theme_prose import CONCEPT_GLOSS, THEME_WHEN
except ImportError:  # first run, before the judgement layer is written
    CONCEPT_GLOSS, THEME_WHEN = {}, {}

EPISODES_DIR = "wiki/episodes"
CONCEPTS_DIR = "wiki/concepts"
THEMES_DIR = "wiki/themes"
ROUTER = f"{THEMES_DIR}/_router.md"
TODAY = os.environ.get("WIKI_DATE") or __import__("datetime").date.today().isoformat()

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
MAX_RANK2 = 30


def parse(path):
    content = open(path, encoding="utf-8").read()
    m = FM_RE.match(content)
    if not m:
        return None, content
    return yaml.safe_load(m.group(1)), content[m.end():]


def load_corpus():
    concepts = {}
    for path in glob.glob(f"{CONCEPTS_DIR}/*.md"):
        meta, body = parse(path)
        if not meta or meta.get("type") != "concept":
            continue
        base = os.path.splitext(os.path.basename(path))[0]
        concepts[str(meta.get("name", base)).strip()] = {
            "basename": base,
            "status": meta.get("status", "stub"),
            # Only the bullets under ## Sources are sources. Counting them
            # over the whole body inflated 16 pages whose Practice opens a
            # bullet with the record it attributes it to (found 2026-09-10 on
            # Human Factors Engineering, printed as 4 sources for 2).
            "sources": len(re.findall(r"^- \[\[", body[body.find("\n## Sources"):],
                                      re.MULTILINE)) if "\n## Sources" in body else 0,
        }

    records = {}
    for path in glob.glob(f"{EPISODES_DIR}/*.md"):
        meta, _ = parse(path)
        if not meta or meta.get("type") != "source":
            continue
        base = os.path.splitext(os.path.basename(path))[0]
        records[base] = [str(c).strip() for c in (meta.get("concepts") or [])]
    return concepts, records


def derive_rank2(concepts, records):
    """Attach every non-rank-1 concept name to themes, via shared records."""
    rank1_theme = collections.defaultdict(set)
    for theme, names in THEMES.items():
        for n in names:
            rank1_theme[n].add(theme)

    scores = collections.defaultdict(collections.Counter)
    where = collections.defaultdict(list)
    for base, names in records.items():
        themes_here = set()
        for n in names:
            themes_here |= rank1_theme.get(n, set())
        for n in names:
            if n in rank1_theme:
                continue
            where[n].append(base)
            for t in themes_here:
                scores[n][t] += 1

    rank2 = collections.defaultdict(list)
    for name, counter in scores.items():
        if not counter:
            continue
        # `counter.most_common(2)` breaks a tie by insertion order, which comes
        # from glob() over wiki/episodes and is filesystem order, not sorted.
        # A concept tied between two themes therefore landed in a different one
        # on every run: two consecutive runs of this script rewrote 22 theme
        # files with a different Sharp-edges list, pure churn in every
        # ingestion commit (found 2026-09-10 on UX Research). Sort the tie.
        for theme, _ in sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:2]:
            page = concepts.get(name)
            rank2[theme].append({
                "name": name,
                "linkable": bool(page),
                "sources": sorted(set(where[name])),
            })
    for theme in rank2:
        rank2[theme].sort(key=lambda d: (-len(d["sources"]), d["name"].lower()))
    return rank2


def theme_page(theme, concepts, rank2):
    members = [n for n in THEMES[theme] if n in concepts]
    members.sort(key=lambda n: -concepts[n]["sources"])

    fm = {
        "type": "theme",
        "name": theme,
        "created": TODAY,
        "updated": TODAY,
        "status": "active",
        "concepts": members,
    }
    out = ["---", yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip(),
           "---", "", f"# {theme}", "", "## When to open this theme", ""]
    out.append(THEME_WHEN.get(theme, "_Judgement layer not written yet._"))
    out += ["", f"## Concepts ({len(members)})", ""]
    for n in members:
        c = concepts[n]
        gloss = CONCEPT_GLOSS.get(n, "")
        line = f"- [[{c['basename']}]] ({c['sources']} sources)"
        out.append(f"{line} : {gloss}" if gloss else line)

    pointes = rank2.get(theme, [])[:MAX_RANK2]
    if pointes:
        out += ["", f"## Sharp edges ({len(pointes)})", "",
                "Single-source and stub concepts. Narrow, often the most",
                "actionable. Open the record, not the concept page.", ""]
        for p in pointes:
            label = f"[[{p['name']}]]" if p["linkable"] else f"**{p['name']}**"
            srcs = ", ".join(f"[[{s}]]" for s in p["sources"][:3])
            out.append(f"- {label} : {srcs}")
    out.append("")
    return "\n".join(out)


def router(concepts):
    lines = [
        "---", "type: theme-router", f"updated: {TODAY}", "---", "",
        "# Router", "",
        "Generated file. Entry point for any question asked of this corpus.",
        "Read this, pick one to three themes, open those, then open the",
        "concept pages the theme points at. Never read `index.md`: it is a",
        "220 KB flat catalogue with no routing value.", "",
        f"## Themes ({len(THEMES)})", "",
        "| Theme | Concepts | Open it when |", "|---|---|---|",
    ]
    for theme in sorted(THEMES):
        members = [n for n in THEMES[theme] if n in concepts]
        when = THEME_WHEN.get(theme, "").split("\n")[0].strip()
        when = re.sub(r"\s+", " ", when)
        if len(when) > 160:
            when = when[:157] + "..."
        lines.append(f"| [[{theme}]] | {len(members)} | {when} |")
    lines.append("")
    return "\n".join(lines)


def main():
    os.makedirs(THEMES_DIR, exist_ok=True)
    concepts, records = load_corpus()
    rank2 = derive_rank2(concepts, records)

    missing = [n for names in THEMES.values() for n in names if n not in concepts]
    if missing:
        print(f"WARNING unknown concept names in theme_map: {sorted(set(missing))}")

    for theme in THEMES:
        path = f"{THEMES_DIR}/{theme}.md"
        with open(path, "w", encoding="utf-8") as f:
            f.write(theme_page(theme, concepts, rank2))
    with open(ROUTER, "w", encoding="utf-8") as f:
        f.write(router(concepts))

    placed = {n for names in THEMES.values() for n in names}
    dev = {n for n, c in concepts.items() if c["status"] == "developed"}
    print(f"themes: {len(THEMES)} | rank-1 concepts: {len(placed)} | "
          f"developed unplaced: {sorted(dev - placed) or 'none'}")
    print(f"rank-2 attachments: {sum(len(v) for v in rank2.values())}")
    print(f"judgement written: {len(THEME_WHEN)}/{len(THEMES)} themes, "
          f"{len(CONCEPT_GLOSS)} concept glosses")


if __name__ == "__main__":
    main()
