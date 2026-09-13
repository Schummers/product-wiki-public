"""Integrity check for the wiki (SCHEMA.md rules 3, 4 and the theme layer).

- Every wikilink in wiki/ resolves to a record, a concept or a theme, an alias
  counting as a valid target.
- Every record's `raw:` path exists.
- Every concept name a record uses has a concept page, and that page's Sources
  section links back to the record (bidirectionality).
- No two concepts collide on a name or alias (case-insensitive), and no theme
  name collides with a concept name.
- Every `developed` concept belongs to at least one theme (stage3/theme_map.py).

Single-source concepts are EXPECTED to have no page: stage 2 only creates a
page from two sources up (docs/adr/0003). A name cited by exactly one record
with no page is therefore normal and stays silent; the same name cited by two
or more records is a real gap and is reported. That distinction is what keeps
this gate green enough to catch an actual regression.
"""

import collections
import glob
import os
import re
import sys

import yaml

EPISODES_DIR = "wiki/episodes"
CONCEPTS_DIR = "wiki/concepts"
THEMES_DIR = "wiki/themes"
PLAYBOOKS_DIR = "wiki/playbooks"

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def parse(path):
    content = open(path, encoding="utf-8").read()
    m = FM_RE.match(content)
    if not m:
        return None, content
    return yaml.safe_load(m.group(1)), content[m.end():]


def load(directory, expected_type, problems):
    out = {}
    for path in glob.glob(f"{directory}/*.md"):
        basename = os.path.splitext(os.path.basename(path))[0]
        meta, body = parse(path)
        if not meta:
            problems.append(f"{expected_type} without frontmatter: {basename}")
            continue
        out[basename] = (meta, body)
    return out


def main():
    problems = []

    records = load(EPISODES_DIR, "record", problems)
    for basename, (meta, _) in records.items():
        raw = meta.get("raw")
        if not raw or not os.path.exists(raw):
            problems.append(f"missing raw file: {basename} -> {raw}")

    concepts = load(CONCEPTS_DIR, "concept", problems)
    name_owners = {}
    for basename, (meta, _) in concepts.items():
        for name in [meta.get("name", basename)] + (meta.get("aliases") or []):
            key = str(name).lower()
            if key in name_owners and name_owners[key] != basename:
                problems.append(
                    f"name collision: '{name}' claimed by both "
                    f"{name_owners[key]} and {basename}"
                )
            name_owners[key] = basename

    themes = {}
    for path in glob.glob(f"{THEMES_DIR}/*.md"):
        basename = os.path.splitext(os.path.basename(path))[0]
        meta, body = parse(path)
        if not meta:
            problems.append(f"theme without frontmatter: {basename}")
            continue
        if meta.get("type") == "theme-router":
            themes[basename] = (meta, body)
            continue
        if meta.get("type") != "theme":
            problems.append(f"theme with wrong type: {basename} -> {meta.get('type')}")
        if basename.lower() in name_owners:
            problems.append(f"theme name collides with a concept: {basename}")
        themes[basename] = (meta, body)

    # A single-source concept legitimately has no page; two or more is a gap.
    citations = collections.Counter()
    for _, (meta, _) in records.items():
        for name in meta.get("concepts") or []:
            citations[str(name)] += 1
    expected_missing = {
        name.lower() for name, n in citations.items()
        if n == 1 and name.lower() not in name_owners
    }

    playbooks = {}
    for path in glob.glob(f"{PLAYBOOKS_DIR}/*.md"):
        basename = os.path.splitext(os.path.basename(path))[0]
        meta, body = parse(path)
        if not meta:
            problems.append(f"playbook without frontmatter: {basename}")
            continue
        if meta.get("theme") not in themes:
            problems.append(f"playbook points at no theme page: {basename}")
        playbooks[basename] = (meta, body)

    valid_targets = set(records) | set(concepts) | set(themes)

    for basename, (_, body) in (
        list(records.items()) + list(concepts.items())
        + list(themes.items()) + list(playbooks.items())
    ):
        for link in re.findall(r"\[\[(.*?)\]\]", body):
            target = link.split("|")[0].split("#")[0].strip()
            if target in valid_targets or target.lower() in name_owners:
                continue
            if target.lower() in expected_missing:
                continue
            problems.append(f"broken link: {basename} -> [[{link}]]")

    for basename, (meta, _) in records.items():
        for concept_name in meta.get("concepts") or []:
            owner = name_owners.get(str(concept_name).lower())
            if not owner:
                if str(concept_name).lower() not in expected_missing:
                    problems.append(
                        f"concept cited by {citations[str(concept_name)]} records "
                        f"but has no page: {concept_name} (first seen in {basename})"
                    )
                continue
            _, cbody = concepts[owner]
            if f"[[{basename}]]" not in cbody:
                problems.append(
                    f"missing backlink: concept '{owner}' does not list [[{basename}]]"
                )

    # Every developed concept belongs to at least one theme.
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "stage3"))
    try:
        from theme_map import THEMES
    except ImportError:
        THEMES = {}
        problems.append("stage3/theme_map.py not importable")
    placed = {n for names in THEMES.values() for n in names}
    for basename, (meta, _) in concepts.items():
        if meta.get("status") != "developed":
            continue
        if str(meta.get("name", basename)) not in placed:
            problems.append(f"developed concept in no theme: {basename}")

    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    print(
        f"OK — {len(records)} records, {len(concepts)} concepts, "
        f"{len(themes)} theme files, {len(playbooks)} playbook(s), "
        f"{len(expected_missing)} single-source concepts without a page "
        f"(expected), links intact."
    )


if __name__ == "__main__":
    main()
