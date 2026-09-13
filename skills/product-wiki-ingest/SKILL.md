---
name: product-wiki-ingest
description: |
  Ingest one book into the product-wiki corpus, from EPUB to chapter records to concepts to themes. Use when adding a book from the library to the corpus, resuming a half-finished ingestion, or when an EPUB's chapters, metadata or line breaks come out wrong.
---

# Ingest a book

Runs the book route of the pipeline in
`~/AI OS/compound-learning/product-wiki`. Every other stage-0 script takes an
article feed, one source to one record. A book takes this one: **one work, N
chapter records** (`docs/adr/0005`).

**One book per session, never two.** The judgement calls (which candidate
names merge, which concepts earn a page, which theme receives them) get
shallow when a session carries two books, and the session budget runs out
mid-fold with a red gate.

Read `SCHEMA.md` before writing anything into `wiki/`. It is the contract:
templates, frontmatter, the anti-duplicate rule, the language.

## Which model runs what

The split is deliberate, by cost and by who is judging. Ignoring it is how a
corpus fills with duplicate concepts.

| Stage | Model | Why |
|---|---|---|
| 0 Scrape | none, pure script | `fetch_epub.py` reads the NCX, no judgement in it |
| 1 Records | Haiku 4.5, 3 to 5 agents per wave | mechanical and parallel; 46 records passed the gate first try |
| 2 Concepts | the session model | merging candidates and writing Definition/Practice **is** the judgement |
| 3 Themes | the session model | trigger lines and glosses are written prose |

**Waves of 3 to 5 agents, never more.** Bigger bursts kill the session before
the wave lands. Verify and commit between two waves.

## Guardrails

- `stage2/generate_stubs.py` **never runs again**. It rewrites every concept
  page from scratch and would erase the 163 written ones. The incremental
  counterpart is `stage2/fold_records.py`.
- The EPUB stays in `~/Documents/livres/product/`. Only extracted text enters
  the repo, and `raw/` is append-only.
- A concept name never contains a slash: it is a filename. Write `Stage Gate`,
  not `Go/No-Go Decision`.

## The seven steps

Each ends on a gate or a commit. The run is resumable at any step, so a
session that stops cleanly mid-book loses nothing.

### 1. Cut the book into chapters

```bash
.venv/bin/python fetch_epub.py ~/Documents/livres/product/BOOK.epub \
  --title "Short Title" --url https://www.amazon.com/dp/ASIN --slug short-title \
  --topics topic-a,topic-b --dry-run
```

A native EPUB (one HTML file per chapter, clean OPF) needs nothing more. An
EPUB born from a PDF (Calibre: title is a hash, author `Unknown`, no HTML
headings, `page_N` anchors) needs `--author`, `--published`, `--rejoin-lines`,
`--strip-page-numbers`, plus repairs: `--relabel '^art (\d)=Part \1'` for a
truncated label, `--exclude REGEX` for a bogus NCX entry, `--absorb REGEX` to
merge a tear sheet or a three-piece introduction into its neighbour.

The dry-run prints a **SHORT SEGMENTS** block. Every entry in it is a
decision you make now, from the plan: absorb it, exclude it, or accept the
merge. Deciding after the raw files exist means deleting them and starting
over.

**Done when** every NCX entry is accounted for as a chapter, an exclusion or
an absorb, and the short-segments block holds nothing you have not ruled on.
Then drop `--dry-run`. The script skips chapters already written.

### 2. Read three raw files

Start, middle, end. Continuous prose, no Calibre spans, hyphens rejoined, no
images. Tables come out as loose lines in a PDF-born book: accepted residue.

Commit `feat(stage0): raw <book-slug>`.

### 3. Write the chapter records

First, draft the candidate list. Skim the table of contents and two or three
chapters, write 8 to 15 concept names this book needs, checking
`ls wiki/concepts/` for ones that already exist and fit. Substitute it into
`{{CANDIDATE_CONCEPTS}}` in `prompts/stage1-record-book.md`, along with
`{{FILES}}` and `{{DATE}}`.

That list is what makes step 4 nearly empty. Agents handed the same names
converge on them; agents left to coin their own produce a merge pass measured
in hours.

Pilot 3 chapters on one Haiku agent and read the records. Then the rest, 5
chapters per agent, 3 to 5 agents per wave.

```bash
.venv/bin/python check_records.py --book <book-slug>   # schema, links, quotes verbatim
.venv/bin/python check_claims.py --book <book-slug>    # numbers absent from the raw
.venv/bin/python check_names.py --book <book-slug>     # named attributions the record dropped
```

`check_records.py` verifies the quotes character by character and says
nothing about the Summary and the Takeaways, which are free paraphrase.
`check_claims.py` covers the gap on the one thing a script can judge: a
figure in the record that the chapter does not carry. Every hit is read by
hand against the raw — a derived figure ("7 of 19" told as "37%") is
legitimate, a drifted one is not. The rate is book-dependent: 0 of 18
chapters on a prose book, 7 of 25 on a statistics-dense one converted from
PDF, where the tables reach the agent as loose lines.

`check_names.py` covers the defect that costs the most corrections, book after
book: the raw credits an idea to a named person, company or work — a signed
sidebar, the genealogy of a term, an epigraph — and the record hands it to the
book's author. It lists the names the raw attributes and the record never
mentions, ranked by the attribution marker that carried them (`according to`,
`says`, `coined`, a byline). Same regime as `check_claims.py`: it reports, it
never fails, and each name is looked up in the raw before anything is changed —
a chapter names people a record legitimately has no room for. Calibrated on
*User Story Mapping*: 35 of the 39 attributions its re-read restored were
flagged on the records as they stood, against 14 hits on the corrected ones.
Add `--all` for the bare proper nouns, noisy by construction.

Check `author:` matches the raw file: agents put the guest author of a
chapter there instead of the book's.

Run both gates **after** the wave's agents have all reported, not while they
are still working: they verify and repair their own records, so a run started
mid-wave reports problems that fix themselves under you.

**Done when** `check_records.py` reports 0 problems and every `check_claims.py`
and `check_names.py` hit has been read against its raw. Commit per wave, then
`feat(stage1): records de <book>`.

### 4. Merge the candidates

```bash
grep -h '^  - ' wiki/episodes/*<book-slug>*.md | sort | uniq -c | sort -rn
```

Map each candidate to an existing page, an existing alias, or a new name.
Put the decisions in `stage2/merge_map.BOOK_MERGES`, then apply to this book
only:

```bash
.venv/bin/python stage2/apply_merge.py --only <book-slug>          # dry run
.venv/bin/python stage2/apply_merge.py --only <book-slug> --write
```

Watch for a candidate that is already an alias carrying another meaning:
`Portfolio Management` meant a UX portfolio before a studio book wanted it
for a venture portfolio. `BOOK_MERGES` overrides for this book's records.

If a candidate you want to merge is also cited by an older record, check what
that record means by it before mapping. `fold_records.py --write` now refuses
when a `BOOK_MERGES` alias it is about to stamp onto a page is cited outside
the book: one name, two senses, and `verify_wiki.py` goes red on a backlink the
older record cannot earn. Drop the alias, or promote it to `MERGES` and re-run
`apply_merge.py` with no `--only` so those records fold in too.

**Done when** the candidate tally holds no two names for one idea.

### 5. Fold and write the concepts

```bash
.venv/bin/python stage2/fold_records.py            # dry run
.venv/bin/python stage2/fold_records.py --write
```

The dry run lists the **developed candidates**: 5+ records **and** 2+ works.
A work is the book when the record has one, the record itself otherwise, so
eight chapters of one book are eight records but one work and stay `stub`
(`docs/adr/0005`).

Write `## Definition` and `## Practice` for each of them with
`prompts/stage2-write.md`, 1 to 3 concepts per agent. Where two works
disagree on a number or a recommendation, both stay, named.

`fold_records.py` ends by naming the `developed` concepts sitting in no
theme. **Place them in `stage3/theme_map.py` before the next
`verify_wiki.py`**: a `developed` concept in no theme is a gate failure, not
a warning.

Flip the book's records to `status: processed`, run
`generate_index_and_concepts.py`, and gate:

```bash
.venv/bin/python verify_wiki.py
```

**Done when** the gate is green. Commit `feat(stage2)`.

### 6. Route the new concepts

Write the trigger line and one gloss per new concept in
`stage3/theme_prose.py`, grounded in each page's own `###` sub-headings. A
trigger line prints in the router: keep it under 160 characters and make it
stand alone.

```bash
WIKI_DATE=$(date +%F) .venv/bin/python stage3/generate_themes.py
WIKI_DATE=$(date +%F) .venv/bin/python stage3/orphan_index.py
.venv/bin/python verify_wiki.py
```

A book on a subject the existing themes already cover needs no new theme. One
on a new subject gets its own, outside `PLAYBOOK_THEMES` unless a design
review will actually run against it (`docs/adr/0004`).

**Done when** `generate_themes.py` reports `developed unplaced: none` and the
gate is green. Commit `feat(stage3)`.

### 7. Close the book

- A dated entry in `wiki/log.md` with the counts: raw, records, concepts
  created and enriched, theme.
- A line in the corpora table of `CLAUDE.md`.
- `stage3/check_playbooks.py` if the book touched a playbook theme.

Commit `docs(pipeline)`.

## Leaving the route better than you found it

Close with at most three things the next book should do differently. For each
one, ask whether a script could check it instead of a reader remembering it.
Two of the first run's three lessons became warnings in `fetch_epub.py` and
`fold_records.py`; a check in a script does not go stale and costs no
context, while a paragraph in this file does both.
