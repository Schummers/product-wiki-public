"""Detect playbooks that have drifted from the concept pages they distil.

A playbook is a cache (docs/adr/0004): assertive rules extracted from concept
pages so a design review has something checkable to apply. A cache goes stale
silently, which is its whole risk. This script makes the staleness loud.

A playbook declares `sources_as_of`. When any concept it lists has an `updated`
date past that, the playbook is reported as stale and needs re-distilling.
Also reports themes marked for a playbook that do not have one yet.

Exit 1 on drift, so it can gate a commit.
"""

import glob
import os
import re
import sys

import yaml

CONCEPTS_DIR = "wiki/concepts"
PLAYBOOKS_DIR = "wiki/playbooks"

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from theme_map import PLAYBOOK_THEMES, THEMES  # noqa: E402


def parse(path):
    content = open(path, encoding="utf-8").read()
    m = FM_RE.match(content)
    return (yaml.safe_load(m.group(1)), content[m.end():]) if m else (None, content)


def main():
    updated = {}
    for path in glob.glob(f"{CONCEPTS_DIR}/*.md"):
        meta, _ = parse(path)
        if meta and meta.get("name"):
            updated[str(meta["name"])] = str(meta.get("updated", ""))

    problems = []
    found = set()
    for path in sorted(glob.glob(f"{PLAYBOOKS_DIR}/*.md")):
        base = os.path.splitext(os.path.basename(path))[0]
        meta, body = parse(path)
        if not meta or meta.get("type") != "playbook":
            problems.append(f"not a playbook: {base}")
            continue
        theme = meta.get("theme")
        found.add(theme)
        if theme not in THEMES:
            problems.append(f"playbook points at an unknown theme: {base} -> {theme}")
            continue

        as_of = str(meta.get("sources_as_of", ""))
        if not as_of:
            problems.append(f"playbook without sources_as_of: {base}")
            continue
        for name in meta.get("concepts") or []:
            when = updated.get(str(name))
            if when is None:
                problems.append(f"{base}: lists an unknown concept '{name}'")
            elif when > as_of:
                problems.append(
                    f"STALE {base}: [[{name}]] updated {when}, "
                    f"playbook distilled from {as_of}"
                )

        covered = set(meta.get("concepts") or [])
        missing = [c for c in THEMES[theme] if c not in covered]
        if missing:
            problems.append(f"{base}: theme concepts not covered: {sorted(missing)}")

    for theme in PLAYBOOK_THEMES:
        if theme not in found:
            problems.append(f"planned playbook not written yet: {theme}")

    if problems:
        print(f"{len(problems)} item(s):")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    print(f"OK — {len(found)} playbook(s), all fresh against their concepts.")


if __name__ == "__main__":
    main()
