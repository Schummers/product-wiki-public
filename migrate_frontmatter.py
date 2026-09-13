"""One-shot migration of the legacy Parlons Design records to the schema in
SCHEMA.md (frontmatter only — bodies are left untouched, in French).

Legacy frontmatter:  title / date / youtube_url / substack_url / concepts[[wikilinks]]
Target frontmatter:  type / name / created / published / source_type / status /
                     url / author / raw / concepts[plain strings]

Idempotent: a record already carrying `type: source` is skipped.
"""

import os
import re
import sys
from datetime import date

EPISODES_DIR = "wiki/episodes"
RAW_DIR = "raw/sources"
AUTHOR = "Romain Penchenat"

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def scalar(block, key):
    m = re.search(rf"^{key}:\s*(.*)$", block, re.MULTILINE)
    if not m:
        return ""
    value = m.group(1).strip().strip('"').strip("'")
    # Legacy titles were double-quoted, so an inner quote arrives escaped.
    return value.replace('\\"', '"')


def legacy_concepts(block):
    """Legacy stored concepts as `- [[Name]]` list items."""
    names = []
    in_list = False
    for line in block.splitlines():
        if re.match(r"^concepts:\s*$", line):
            in_list = True
            continue
        if in_list:
            m = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if not m:
                break
            name = m.group(1).strip()
            name = re.sub(r"^\[\[|\]\]$", "", name).strip()
            if name:
                names.append(name)
    return names


def yaml_quote(value):
    return '"' + value.replace('"', '\\"') + '"'


def migrate(filename, today):
    path = os.path.join(EPISODES_DIR, filename)
    with open(path, encoding="utf-8") as f:
        content = f.read()

    m = FM_RE.match(content)
    if not m:
        return "no-frontmatter"
    block, body = m.group(1), content[m.end():]

    if re.search(r"^type:\s*source\s*$", block, re.MULTILINE):
        return "already-migrated"

    raw_path = os.path.join(RAW_DIR, filename)
    if not os.path.exists(raw_path):
        return "missing-raw"

    url = scalar(block, "substack_url") or scalar(block, "youtube_url")
    source_type = "video" if "youtube" in url else "transcript"

    lines = [
        "---",
        "type: source",
        f"name: {yaml_quote(scalar(block, 'title'))}",
        f"created: {today}",
        f"published: {scalar(block, 'date')}",
        f"source_type: {source_type}",
        "status: summarized",
        f"url: {url}",
        f"author: {AUTHOR}",
        f"raw: {raw_path}",
        "concepts:",
    ]
    for name in legacy_concepts(block):
        lines.append(f"  - {yaml_quote(name)}")
    lines.append("---")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n" + body)
    return "migrated"


def main():
    if not os.path.isdir(EPISODES_DIR):
        sys.exit(f"Run me from the vault root: {EPISODES_DIR} not found.")
    today = date.today().isoformat()

    tally = {}
    for filename in sorted(os.listdir(EPISODES_DIR)):
        if not filename.endswith(".md"):
            continue
        outcome = migrate(filename, today)
        tally[outcome] = tally.get(outcome, 0) + 1
        if outcome not in ("migrated", "already-migrated"):
            print(f"  {outcome}: {filename}")

    for outcome, count in sorted(tally.items()):
        print(f"{outcome}: {count}")


if __name__ == "__main__":
    main()
