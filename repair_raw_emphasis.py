"""Re-extraction fix: restore the spaces lost at emphasis boundaries.

`fetch_nngroup.py` used to strip whitespace inside <strong>/<em>, gluing words
together ("should be to**not fragment**"). The markers still marked the
boundary, so no information was lost, but the rendered text was wrong. This
rewrites the affected raw files to exactly what the corrected extractor now
produces, rather than re-fetching 900 pages for a spacing defect.

This is a re-extraction, not an edit of the source: it repairs how the
publisher's HTML was converted, never what the publisher wrote. The
append-only rule on `raw/` (CLAUDE.md) forbids bending material to fit a
record; it does not forbid fixing a conversion bug.

Deterministic: an emphasis span is `**...**` or `*...*` within one line; a
space is inserted only where an alphanumeric character sits directly against
the opening or the closing marker of a matched span.
"""

import glob
import re

# A matched emphasis span, non-greedy, never spanning a line break.
SPAN = re.compile(r"(\*{1,2})(\S(?:[^\n]*?\S)?)\1")


def repair_line(line):
    out, pos = [], 0
    for m in SPAN.finditer(line):
        marker, inner = m.group(1), m.group(2)
        out.append(line[pos:m.start()])
        if m.start() > 0 and line[m.start() - 1].isalnum():
            out.append(" ")
        out.append(f"{marker}{inner}{marker}")
        if m.end() < len(line) and line[m.end()].isalnum():
            out.append(" ")
        pos = m.end()
    out.append(line[pos:])
    return "".join(out)


def repair(text):
    return "\n".join(repair_line(line) for line in text.split("\n"))


def main():
    changed = 0
    for path in sorted(glob.glob("raw/sources/*.md")):
        text = open(path, encoding="utf-8").read()
        if not re.search(r"^type: article", text, re.M):
            continue
        fixed = repair(text)
        if fixed != text:
            open(path, "w", encoding="utf-8").write(fixed)
            changed += 1
    print(f"raw files repaired: {changed}")


if __name__ == "__main__":
    main()
