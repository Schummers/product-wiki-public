"""Stage 1 gate, second half: numeric claims that the raw file does not carry.

check_records.py verifies the 1-3 `> ` quotes of a record, character for
character. It says nothing about the Summary, the Key Takeaways or the
Concepts bullets, which are free paraphrase — and that is where a number
drifts. Three defects found by hand on the first two books, all in unquoted
prose, all past a green check_records.py:

- a fabricated figure: "72% vs 42%" (Seed to Series A conversion, credited by
  the book to a third-party study) became "60% of studio-founded companies
  reaching Series A", wrong number and wrong denominator;
- a misattribution: an equity range stated in chapter 17 landed in the record
  of chapter 14, which never mentions equity. The claim is true, the
  wikilink under it points at a chapter that does not support it;
- an epistemic upgrade: "7 of 19 studios interviewed" became "37% of
  studios", which reads like an industry statistic rather than a small
  sample.

Only the first two are catchable here: a number in the record that is not in
the raw. Notation is normalised, so `$250K-700K` in the raw covers `$700k` in
the record, and a bare one- or two-digit integer is ignored as noise. A hit is
a claim to check by hand, not proof of a defect: a derived figure (7 of 19 ->
37%) is legitimate arithmetic the raw never spells out. Reports, never fixes.

Usage:
    python3 check_claims.py [basename ...]
"""

import glob
import os
import re
import sys
import unicodedata

import yaml

EPISODES_DIR = "wiki/episodes"
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
NUM_RE = re.compile(r"(\d[\d,.]*)\s?(%|percent|[KMB]\b|million|billion)?", re.IGNORECASE)
MULTIPLIER = {"k": 1e3, "m": 1e6, "b": 1e9, "million": 1e6, "billion": 1e9}


def canon(digits, unit):
    """One spelling per value, so 0.5M, 500K and 500,000 compare equal."""
    n = digits.replace(",", "").rstrip(".")
    if not n or n.count(".") > 1:
        return None
    try:
        value = float(n)
    except ValueError:
        return None
    unit = (unit or "").lower()
    if unit in ("%", "percent"):
        return f"{value:g}%"
    return f"{value * MULTIPLIER.get(unit, 1):g}"


def numbers(text):
    found = set()
    for m in NUM_RE.finditer(unicodedata.normalize("NFKD", text)):
        c = canon(m.group(1), m.group(2))
        # A bare 1-2 digit integer is a list count or a year fragment, not a
        # claim: too noisy to be worth a reader's attention.
        if c and not re.fullmatch(r"\d{1,2}", c):
            found.add(c)
    return found


def check(basename):
    path = f"{EPISODES_DIR}/{basename}.md"
    content = open(path, encoding="utf-8").read()
    m = FM_RE.match(content)
    if not m:
        return ["no frontmatter"]
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return [f"invalid YAML: {str(e)[:80]}"]

    raw_path = meta.get("raw", "")
    if not raw_path or not os.path.exists(raw_path):
        return [f"raw not found: {raw_path}"]

    # Blockquotes are check_records.py's job and already verified verbatim.
    body = re.sub(r"^> .*$", "", content[m.end():], flags=re.MULTILINE)
    missing = sorted(numbers(body) - numbers(open(raw_path, encoding="utf-8").read()))
    return [f"number not in raw: {n}" for n in missing]


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
        names = sorted(os.path.splitext(os.path.basename(p))[0]
                       for p in glob.glob(f"{EPISODES_DIR}/*.md"))

    clean = dirty = 0
    for name in names:
        problems = check(name)
        if problems:
            dirty += 1
            print(f"\n{name}")
            for p in problems:
                print(f"  - {p}")
        else:
            clean += 1
    print(f"\nclean: {clean}, to check by hand: {dirty}")


if __name__ == "__main__":
    main()
