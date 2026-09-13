"""Regenerate wiki/index.md from the records and concept pages (SCHEMA.md).

The index is fully generated — never hand-edited. Records are listed in
reverse-chronological `published` order with a one-line summary; concepts
alphabetically with their status and source count. This script only writes
the index: creating or enriching concept pages is stage 2's job (an agent,
not a script — see SCHEMA.md, "The four stages").
"""

import glob
import os
import re

import yaml

EPISODES_DIR = "wiki/episodes"
CONCEPTS_DIR = "wiki/concepts"
INDEX_FILE = "wiki/index.md"

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def parse(path):
    content = open(path, encoding="utf-8").read()
    m = FM_RE.match(content)
    if not m:
        return None, content
    return yaml.safe_load(m.group(1)), content[m.end():]


def one_liner(body, heading):
    m = re.search(rf"## .*(?:{heading}).*\n+(.+?)(?:\n\n|\n##|\Z)", body, re.DOTALL)
    if not m:
        return ""
    text = " ".join(m.group(1).split())
    return text[:150] + "…" if len(text) > 150 else text


def main():
    records = []
    for path in glob.glob(f"{EPISODES_DIR}/*.md"):
        meta, body = parse(path)
        if not meta or meta.get("type") != "source":
            print(f"skipping (no source frontmatter): {path}")
            continue
        records.append({
            "basename": os.path.splitext(os.path.basename(path))[0],
            "published": str(meta.get("published", "")),
            "summary": one_liner(body, "Summary|Résumé"),
        })
    records.sort(key=lambda r: r["published"], reverse=True)

    concepts = []
    for path in glob.glob(f"{CONCEPTS_DIR}/*.md"):
        meta, body = parse(path)
        if not meta or meta.get("type") != "concept":
            print(f"skipping (no concept frontmatter): {path}")
            continue
        concepts.append({
            "basename": os.path.splitext(os.path.basename(path))[0],
            "status": meta.get("status", "stub"),
            "sources": len(re.findall(r"^- \[\[", body, re.MULTILINE)),
        })
    concepts.sort(key=lambda c: c["basename"].lower())

    lines = [
        "# Index — Product & Design",
        "",
        "Generated file — run `generate_index_and_concepts.py` to refresh.",
        "",
        f"## Sources ({len(records)})",
        "",
    ]
    for r in records:
        lines.append(f"- **{r['published']}** — [[{r['basename']}]]"
                     + (f" : {r['summary']}" if r["summary"] else ""))
    lines += ["", f"## Concepts ({len(concepts)})", ""]
    for c in concepts:
        lines.append(
            f"- [[{c['basename']}]] — {c['status']}, {c['sources']} source(s)"
        )
    lines.append("")

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"index: {len(records)} records, {len(concepts)} concepts")


if __name__ == "__main__":
    main()
