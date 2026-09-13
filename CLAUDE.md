# Product & Design Domain

A reference corpus on product and design: external material only, ingested from
public sources, distilled into per-source records and cross-source concept
pages. This is **not** the owner's personal thinking — that lives in the second
brain (`../second-brain/knowledge/notes/`). Here, everything is attributable to
a source.

Not design alone: product management, careers, research and tooling all belong
here.

## Plan and repo

GitHub plan, own remote, nested repo (gitignored from `ai-os`). The whole domain
is text, so `raw/` is versioned like the rest; only `.venv/` and Obsidian's
per-machine UI state are ignored.

**Public snapshot.** `Schummers/product-wiki` (this repo) is private and the
only place anyone commits. `Schummers/product-wiki-public` is a snapshot: one
commit, no history, overwritten on every sync, without the raw text of the
books (`type: book` in `raw/sources/`); their records and concept pages stay.
Syncing is manual and deliberate, never automatic:

```bash
./sync_public.sh
```

The script refuses an uncommitted tree, a remaining book file or a `$HOME`
path, then force-pushes. Before running it, re-read what changed since the
last sync as a stranger would. Decided 2026-09-05, same pattern as `ai-os`.

The folder is an Obsidian vault, separate from the second brain and not linked
to it. Wikilinks resolve inside this vault only. If the two are ever merged, the
schema is already compatible — see `docs/adr/0001-normalisation-par-extension.md`.

## Structure

- `raw/sources/` — verbatim ingested material (YouTube transcripts, scraped
  articles). Written by scripts, read-only for humans and agents. One file per
  source, never edited after ingestion.
- `wiki/episodes/` — one record per source: frontmatter, summary, key
  takeaways, quotes, concepts. Distilled from `raw/`.
- `wiki/concepts/` — cross-source pages. A concept compiles what several
  sources say about one topic. First-class objects here, with their own
  frontmatter and lifecycle status.
- `wiki/themes/` — the routing layer: 22 theme pages plus `_router.md`, the
  entry point an agent reads first. Generated; the curation lives in
  `stage3/theme_map.py` and the judgement in `stage3/theme_prose.py`.
- `wiki/playbooks/` — a theme distilled into checkable rules for a design
  review. Only the themes a review runs against (`docs/adr/0004`).
- `wiki/orphans.md` — generated index of the 860 single-source concepts that
  have no page, so their wikilinks stop being dead ends.
- `wiki/index.md` — generated catalogue (reverse-chronological sources +
  alphabetical concepts). Never hand-edited, and never the routing surface:
  220 Ko flat. Agents start from `wiki/themes/_router.md`.
- `wiki/log.md` — ingestion journal.
- `check_records.py`, `check_claims.py`, `check_names.py` — the three stage 1
  gates, run per book (`--book <slug>`): schema and verbatim quotes; numbers the
  record states that its raw does not carry; named attributions (a person, a
  company, a work credited in the raw) that no line of the record mentions.
  The last two report and never fail — every hit is read by hand against the
  raw, because a chapter names people a record has no room for.
- `stage3/` — the theme stage: `theme_map.py` (curation, theme -> concepts),
  `theme_prose.py` (judgement, written by a strong model), `generate_themes.py`,
  `orphan_index.py`, and `check_playbooks.py` which flags a playbook whose
  concepts have moved past its `sources_as_of`.
- `stage2/` — the concept stage's working artefacts: `merge_map.py` and
  `singleton_map.py` (candidate name -> canonical name, hand-curated),
  `apply_merge.py` (rewrites records), `generate_stubs.py` (builds the concept
  pages and their `## Sources`), plus the counts the decisions were made from.
  Kept because the merge is the one judgement call the corpus cannot re-derive.
- `SCHEMA.md` — the contract every agent working in this vault follows:
  templates, frontmatter, anti-duplicate rules, language. Read it before
  writing anything into `wiki/`.
- `CONTEXT.md` — operational glossary of this domain.
- `docs/adr/` — why the hard-to-reverse choices were made.

## Corpora

| Corpus | Source | Language of records |
|---|---|---|
| Parlons Design (Romain Penchenat) | YouTube `@ParlonsDesign`, Substack `parlonsdesign` | French (legacy, kept as-is) |
| Nielsen Norman Group | `nngroup.com/articles`, post-2016, topic-filtered | English |
| *Startup Studio Playbook* (Attila Szigeti, 2019) | EPUB, `fetch_epub.py`, 21 chapter records | English |
| *Venture Studios Demystified* (Kannan and Peterman, 2022) | EPUB born from a PDF, `fetch_epub.py --rejoin-lines`, 25 chapter records | English |
| *Continuous Discovery Habits* (Teresa Torres, 2021) | native EPUB, `fetch_epub.py`, 18 chapter records | English |
| *The 10x Method* (Hexa: Thibaud Elziere, Quentin Nickmans, 2026) | seven public chapters of `media.hexa.com`, manual extraction, no EPUB, 7 chapter records | English |
| *Articulating Design Decisions* (Tom Greever, 2nd ed., 2020) | O'Reilly EPUB, `fetch_epub.py --absorb --min-chars 1`, 12 chapter records | English |
| *Solving Product Design Exercises* (Artiom Dashinsky, 2018) | native EPUB, `fetch_epub.py --relabel`, 30 chapter records | English |
| *User Story Mapping* (Jeff Patton with Peter Economy, 2014) | O'Reilly EPUB, `fetch_epub.py --min-chars 1` with a negative-lookahead `--absorb` over a nested NCX, 23 chapter records | English |
| *Just Enough Research* (Erika Hall, A Book Apart, 2013) | native EPUB, `fetch_epub.py` with no repair option, 11 chapter records | English |
| *Laws of UX* (Jon Yablonski, 2nd ed., 2024) | O'Reilly EPUB, `fetch_epub.py --min-chars 1 --absorb`, 14 chapter records | English |
| *UX Research* (Nunnally and Farkas, O'Reilly 2016) | Calibre EPUB born from a PDF, NCX rebuilt by hand, `fetch_epub.py --rejoin-lines`, 16 chapter records | English |
| *The Path to Senior Product Designer* (Artiom Dashinsky, 2023) | native EPUB (Pages), `fetch_epub.py --exclude '^Footnotes'`, 25 chapter records | English |
| *Product Management for UX People* (Christian Crumlish, Rosenfeld Media, 2022) | native EPUB, `fetch_epub.py --min-chars 1 --exclude --absorb` (negative-lookahead absorb: every sub-section had its own NCX entry), 14 chapter records | English |
| *Storytelling in Design* (Anna Dahlström, O'Reilly 2019) | native EPUB, `fetch_epub.py --min-chars 1 --exclude '^\[ Index \]$' --absorb '^(?!chapter \d+\.|\[)'` over a nested NCX (118 entries for 15 chapters), 15 chapter records | English |

A book enters as one record per chapter (`docs/adr/0005`); see "Ingesting a
book" below for the exact sequence.

English is the language of the corpus going forward, including all concept
pages — see `docs/adr/0002-anglais-langue-du-corpus.md`.

## Pipeline

Four stages, deliberately split by cost and by who does the judging:

0. **Scrape** — `fetch_*.py`. Pure scripts, no LLM. Writes `raw/sources/`.
1. **Records** — one raw file → one record in `wiki/episodes/`. Mechanical and
   parallelisable, runs on a cheap model. Proposes **candidate** concepts in
   frontmatter; never creates a concept page.
2. **Concepts** — merges the candidates, creates or enriches `wiki/concepts/`,
   cross-links, regenerates the index. Needs judgement, runs on the strong
   model. This is the only stage allowed to create a concept page, precisely so
   the anti-duplicate rule has a single enforcement point. Incremental since
   2026-09-03: `stage2/fold_records.py` folds new records without touching a
   written page. `stage2/generate_stubs.py` is the initial build and **must
   not be re-run**: it rewrites every page and would erase the developed ones.
3. **Themes** — groups the `developed` concepts into 22 themes and regenerates
   the router. Strong model for the judgement layer, script for everything else,
   so an ingestion refreshes it without losing a written line
   (`docs/adr/0003`).
4. **Playbooks** — distils a theme into checkable rules for a design review.
   Only the six themes a review uses, on demand (`docs/adr/0004`).

A cross-source **synthesis** inside a concept page (`status: synthesized`)
remains available and unused: on demand only, never automatic.

## Ingesting a book

The one route that is not an article feed: a book enters as one record per
chapter (`docs/adr/0005`). The runbook is the **`product-wiki-ingest`
skill** — seven steps from EPUB to theme, which model runs which stage, and
the guardrails. One book per session.

Tables are flattened to inline text before pandoc sees them, because the gfm
writer drops any table it cannot render and `-raw_html` leaves no fallback
(`docs/adr/0006`). If the dry run still reports a `[TABLE]`, that chapter's
raw is missing content: read the table in the book, and never let a record
assert what it held or count the items of a list it belonged to.

## Querying the corpus

Three skills, in `skills/`, symlinked into `.claude/skills/` (gitignored, a
committed symlink breaks at clone):

- `product-wiki-consult` — answers a design question from the corpus.
- `product-wiki-review` — reviews an artifact against it, then re-reviews.
- `product-wiki-ingest` — the book runbook, EPUB to records to concepts to
  themes.

Both route `_router.md` → theme → concept, and both are bound by the same rule:
when the corpus does not cover the question, say so rather than answering from
general knowledge. That rule is the whole value of the corpus.

Scripts run in the local venv: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`.

## Rules

- `raw/` is append-only. Never rewrite ingested material to fit a record.
- Never present an external claim as the owner's own. Every claim in `wiki/`
  traces back to a source.
- No fabrication: a record says only what its source says (`SCHEMA.md`).
- Before creating a concept, search existing names **and** aliases; enrich
  rather than create.
- `wiki/index.md` is generated — change the generator, not the file.
- Finished deliverables (if this domain ever produces one) move to
  `../deliverables/product-wiki/`.
