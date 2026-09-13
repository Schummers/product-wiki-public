"""Stage 1 gate, third half: named attributions the record dropped.

check_records.py verifies the schema and the verbatim quotes; check_claims.py
verifies the numbers. Neither sees the dominant defect of the book corpus: the
raw credits an idea to a named person, company or work, and the record presents
it as the book author's own voice. Six books in, that is by far the most
frequent correction — on *User Story Mapping* alone, 39 fixes, nine of them
contributed sidebars signed by a practitioner and absent from the record from
end to end. Nothing breaks when a name disappears, so nothing catches it.

The heuristic, deliberately crude and dependency-free, in the regime of
check_claims.py:

- candidates are capitalized word sequences in the raw's prose (headings
  excluded: title case capitalizes everything), plus all-caps acronyms;
- a token is treated as an ordinary word, not a name, when the same book uses
  it in lowercase often enough — self-calibrating, no hand-kept stoplist of
  English vocabulary. A candidate made only of such tokens is dropped, as are
  the book's own author and title, and any candidate that occurs across a
  large share of the book's chapters (that is the book's vocabulary, not an
  attribution);
- what survives is split in two. **attributed** — the raw names the source
  next to an attribution marker (`according to`, `says`, `coined`, `'s work`,
  a byline under a sidebar title, a `—` signature). **also unmentioned** —
  bare proper nouns, printed only under `--all`, because that half is noise
  by construction.

A hit is a name to look up in the raw, never a defect by itself: a chapter
mentions people the record has no room for. Reports, never fixes; exits 0 with
hits, non-zero only on a real error.

Calibrated against the *User Story Mapping* re-read of 2026-09-11, which
restored 39 attributions across 23 records: 35 of them are flagged on the
records as they stood before it (`git show 03fbf7d`), 14 hits remain on the
corrected ones. The four it misses say where the wall is: a name the raw
writes in lowercase (`d.school`), and one buried in a paragraph with no marker
at all.

Usage:
    python3 check_names.py [basename ...]
    python3 check_names.py --book user-story-mapping [--all]
"""

import glob
import os
import re
import sys
import unicodedata
from collections import Counter

import yaml

EPISODES_DIR = "wiki/episodes"
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)

# A capitalized run: "Kent Beck", "Jeff Patton", "Osterwalder and Pigneur" is
# caught as two candidates, which is what we want. Internal lowercase joiners
# ("de", "van", "von") stay inside the name.
WORD = r"[A-Z][\w’'’-]*"
JOIN = r"(?:de|del|van|von|der|di|da|la|le)"
NAME_RE = re.compile(rf"\b({WORD}(?:\s+(?:{JOIN}\s+)?{WORD}){{0,3}})")
ACRO_RE = re.compile(r"\b([A-Z]{2,6})\b")

# Function words and corpus furniture that survive the lowercase test because
# the book almost never writes them in lowercase (sentence starts, headings
# inside prose, list labels).
FURNITURE = {
    "a", "an", "the", "and", "but", "or", "if", "so", "then", "when", "while",
    "this", "that", "these", "those", "there", "here", "it", "its", "i", "we",
    "you", "he", "she", "they", "my", "our", "your", "his", "her", "their",
    "in", "on", "at", "to", "for", "of", "by", "with", "from", "as", "is",
    "was", "are", "were", "be", "been", "do", "does", "did", "not", "no",
    "yes", "now", "just", "how", "what", "why", "who", "which", "all", "any",
    "each", "every", "some", "one", "two", "three", "first", "second", "next",
    "last", "figure", "chapter", "part", "page", "note", "table", "step",
    "let", "let's", "don't", "it's", "i'm", "i've", "you'll", "we'll",
    "however", "because", "after", "before", "during", "since", "until",
    "yeah", "ok", "okay", "well", "sure", "maybe", "many", "most", "more",
    "less", "much", "very", "really", "think", "know", "see", "look", "make",
    "post-it", "post-its", "internet", "web", "email",
    # Job titles read as names once capitalized: "Vice President", "Emeritus
    # Professor", "Product Manager".
    "vice", "president", "professor", "emeritus", "director", "chief",
    "officer", "senior", "junior", "principal", "head", "founder", "cofounder",
    "co-founder", "manager", "designer", "engineer", "researcher", "author",
    "coach", "consultant", "student", "professor's",
}
BAD_ACRONYMS = {"UI", "UX", "IT", "OK", "PM", "PO", "QA", "API", "MVP", "CEO",
                "CTO", "COO", "CFO", "VP", "ROI", "KPI", "NPS", "SaaS", "B2B",
                "B2C", "US", "USA", "UK", "EU", "AI", "ML", "TV", "PDF", "HTML",
                "CSS", "SQL", "PC", "FAQ", "TL", "DR", "AB", "URL", "OKR",
                "SEO", "CRM", "MVPS", "NDA", "HR", "RD", "NCX", "EPUB"}

# The raw names the source. Anything matching just before the candidate...
BEFORE_RE = re.compile(
    r"(according to|thanks to|borrowed from|adapted from|taken from|"
    r"credited to|attributed to|coined by|invented by|created by|"
    r"popularized by|described by|introduced by|written by|told by|"
    r"cites?|citing|quotes?|quoting|interview(?:ed)? with|courtesy of|"
    r"(?:my|our|a) (?:former |old )?(?:friend|colleague|coworker|co-worker|"
    r"co-author|client|student|teammate|mentor|boss)|"
    r"(?:company|firm|agency|consultancy|team|book|tool|technique|method|"
    r"term|approach|framework|model|product|startup|game)s? (?:called|named)|"
    r"(?:advisor|author|founder|professor|coach|consultant|researcher|"
    r"designer|colleague|coworker|co-worker|friend|client|student|manager|"
    r"owner|lead|partner)s?[^,.]{0,25}(?:,|\bwas\b|\bis\b|\bnamed\b)|"
    r"photos?[^.]{0,20} from|the late)\s*$",
    re.IGNORECASE | re.MULTILINE)
# A signature line: the dash has to open the line, "Art—Creativity" is not one.
SIGNATURE_RE = re.compile(r"\A\s*(?:—|--|by)\s*\Z", re.IGNORECASE)
# ...or just after it.
AFTER_RE = re.compile(
    r"^\s*(?:’s|'s|s’)?\s*(says?|said|writes?|wrote|argues?|argued|claims?|"
    r"calls?|called|coined|describes?|described|explains?|explained|notes?|"
    r"noted|observes?|observed|points out|pointed out|tells?|told|teaches?|"
    r"taught|suggests?|suggested|recommends?|reminds?|introduced|invented|"
    r"created|popularized|defines?|defined|shares?|shared|showed|shows?|"
    r"asked|asks?|adds?|added|put it|puts it|and (?:his|her|their) team|"
    r"et al|and colleagues|would say|likes? to say|refers? to|"
    r"(?:is|was|are|were) credited|(?:of|at|from) (?:the )?[A-Z])",
    re.IGNORECASE)
# "…’s idea", "…’s work", "…’s book": possession is attribution too.
POSSESSIVE_RE = re.compile(r"\A\s*(?:’s|'s)\s+\S", re.IGNORECASE)
# "Rick Cusick, Reading Plus, Winooski, Vermont" — the byline of a contributed
# sidebar, the exact shape of the nine that vanished from User Story Mapping.
BYLINE_RE = re.compile(r"\A[A-Z][^.!?]{0,150}(?:,[^.!?]{2,60}){1,4}\Z")
# "Andrea Schmieden", "Erin Beierwaltes and Aaron White": a standalone line of
# names alone, the other shape a contributed sidebar signs itself with.
NAMES_ONLY_RE = re.compile(
    r"\A[A-Z][\w’'-]*(?:[ ,]+(?:and|&|of|the|at|for|with|[A-Z][\w’'-]*))*\Z")


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"[’’]", "'", s)


def prose_lines(text):
    """Body lines only: headings are title-cased, every word looks like a name."""
    out = []
    for line in norm(text).split("\n"):
        if line.startswith("#") or not line.strip():
            continue
        out.append(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line))
    return out


def lowercase_vocabulary(texts):
    """Words the book itself writes in lowercase are words, not names."""
    lower, upper = Counter(), Counter()
    for t in texts:
        for w in re.findall(r"\b[\w']+\b", norm(t)):
            (lower if w[0].islower() else upper)[w.lower()] += 1
    return {w for w, n in lower.items() if n >= 4 and n > upper[w]}


def is_word(token, vocab):
    t = token.lower().strip("'").removesuffix("'s")
    if t in FURNITURE or t in vocab:
        return True
    # "Post-it": both halves are ordinary words of the book.
    parts = [x for x in t.split("-") if x]
    return len(parts) > 1 and all(x in FURNITURE or x in vocab for x in parts)


def names_only(stripped, vocab):
    """A standalone line made of nothing but names: a sidebar signature."""
    if not NAMES_ONLY_RE.match(stripped):
        return False
    tokens = [t.strip(",") for t in stripped.split()
              if t[:1].isupper() and t.strip(",")]
    return len(tokens) >= 2 and not any(is_word(t, vocab) for t in tokens)


def candidates(text, vocab, keep_singles=False):
    """{candidate: (attributed?, context line)} for one raw file."""
    found = {}
    for line in prose_lines(text):
        stripped = line.strip("*_> ").strip()
        # A bold standalone line is a heading pandoc did not mark as one.
        heading_like = "**" in line
        byline = not heading_like and len(stripped) < 180 and bool(
            BYLINE_RE.match(stripped)
            or (len(stripped) < 70 and names_only(stripped, vocab)))
        for m in NAME_RE.finditer(line):
            name = m.group(1).strip()
            tokens = [t.removesuffix("’s").removesuffix("'s")
                      for t in name.split()]
            # "I'll", "It's", "We'd": a contraction is not a surname.
            if any(re.match(r"\A[A-Z]'[a-z]{1,2}\Z", t) for t in tokens):
                continue
            tokens = [t for t in tokens if t.lower() not in
                      {"de", "del", "van", "von", "der", "di", "da", "la", "le"}]
            # An adverb opening a sentence ("Optionally", "Finally").
            if any(re.fullmatch(r"[A-Z][a-z]+ly", t) for t in tokens):
                continue
            tokens = [t for t in tokens if len(t.strip("'’-")) > 1]
            if not tokens or all(is_word(t, vocab) for t in tokens):
                continue
            # Trailing ordinary words are sentence, not name: "Kent was" ->
            # "Kent". Leading ones too: "The Learning Connexion" -> keep tail.
            while tokens and is_word(tokens[-1], vocab):
                tokens.pop()
            while tokens and is_word(tokens[0], vocab):
                tokens.pop(0)
            if not tokens:
                continue
            name = " ".join(tokens)
            before = line[:m.start()]
            # The candidate lost its trailing "'s"; the line still has it,
            # and POSSESSIVE_RE reads it as an attribution.
            after = line[m.start() + len(name):]
            single = len(tokens) == 1 and not name.isupper()
            sentence_start = not before.strip() or bool(
                re.search(r"[.!?:;]\s+$|^\s*[-*]\s*$", before))
            # In a byline, only the opening field carries the name; the rest
            # is employer, city and country.
            strong = bool((byline and "," not in before)
                          or SIGNATURE_RE.match(before)
                          or BEFORE_RE.search(before[-40:]))
            # A lone first name is the book's own cast ("Gary", "Mary") far
            # more often than a credit, so a verb or a possessive is not
            # enough: it takes an explicit source marker.
            attributed = strong or (not single and bool(
                AFTER_RE.match(after) or POSSESSIVE_RE.match(after)))
            if not keep_singles and single and (sentence_start or not attributed):
                continue
            prev = found.get(name)
            if prev is None or (attributed and not prev[0]):
                found[name] = (attributed, stripped[:160])
    return found


def mentioned(name, record):
    """A record saying "Beck" covers "Kent Beck"; surname is enough."""
    tokens = name.split()
    for probe in {name, tokens[-1]}:
        if re.search(rf"\b{re.escape(probe)}\b", record, re.IGNORECASE):
            return True
    return False


_BOOK_CACHE = {}


def book_context(meta, raw_path):
    """Lowercase vocabulary and per-chapter counts, computed once per book."""
    slug = meta.get("book_slug") or meta.get("book") or raw_path
    if slug in _BOOK_CACHE:
        return _BOOK_CACHE[slug]
    stem = re.sub(r"_\d+[^_]*\.md$", "_*.md", raw_path)
    paths = sorted(glob.glob(stem)) or [raw_path]
    texts = [open(p, encoding="utf-8").read() for p in paths]
    vocab = lowercase_vocabulary(texts)
    spread = Counter()
    for t in texts:
        spread.update(set(candidates(t, vocab, keep_singles=True)))
    _BOOK_CACHE[slug] = (vocab, spread, len(paths))
    return _BOOK_CACHE[slug]


def check(basename, show_all=False):
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

    raw = open(raw_path, encoding="utf-8").read()
    vocab, spread, chapters = book_context(meta, raw_path)
    # The book's own voice: its authors and its title are not attributions.
    own = norm(f"{meta.get('author', '')} {meta.get('book', '')} "
               f"{meta.get('name', '')}").lower()
    # A name carried by half the book is its vocabulary, not a credit.
    ubiquitous = max(3, chapters // 2)

    found = candidates(raw, vocab)
    # "Jen" and "Jen Yates" are one hit, not two.
    found = {n: v for n, v in found.items()
             if not any(o != n and re.search(rf"\b{re.escape(n)}\b", o)
                        for o in found)}
    problems, weak = [], []
    for name, (attributed, ctx) in sorted(found.items()):
        if name.upper() in BAD_ACRONYMS or name.lower() in own:
            continue
        if any(tok.lower() in own.split() for tok in name.split()):
            continue
        if spread[name] >= ubiquitous:
            continue
        if mentioned(name, norm(content)):
            continue
        (problems if attributed else weak).append(
            f"{'attributed' if attributed else 'unmentioned'}: {name} "
            f"— “{ctx}”")
    return problems + (weak if show_all else [])


def main():
    args = sys.argv[1:]
    show_all = "--all" in args
    args = [a for a in args if a != "--all"]
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

    clean = dirty = hits = 0
    for name in names:
        problems = check(name, show_all)
        if problems:
            dirty += 1
            hits += len(problems)
            print(f"\n{name}")
            for p in problems:
                print(f"  - {p}")
        else:
            clean += 1
    print(f"\nclean: {clean}, to check by hand: {dirty} ({hits} names)")


if __name__ == "__main__":
    main()
