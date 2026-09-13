# Product & Design — Operational Glossary

The working vocabulary of this domain. Terms only, no implementation detail.

## Corpus

The whole set of external material this domain covers. Made of several
**corpora**, one per publisher (Parlons Design, Nielsen Norman Group). A corpus
has one language and one ingestion route.

## Raw

Ingested material, verbatim, as the publisher wrote or said it. Lives in
`raw/sources/`, append-only. Raw is not a record: it carries no summary, no
judgement, no links. Deliberately kept in its own file rather than inside the
record, because a transcript runs 30–50K characters and would drown the record
it feeds.

## Work

The bibliographic unit: one book, one article, one episode. Counted when a
concept's status is decided, because a concept sourced by eight chapters of
one book knows one author's view, not eight. `developed` needs two works.

## Chapter record

The pipeline unit for a book: one raw file and one record per chapter, named
`<published>_<book-slug>_<NN>-<chapter-slug>`. A chapter record summarises its
chapter only, never the book. A book is therefore one work and N records;
the two never coincide, which is why both words exist (`docs/adr/0005`).

## Record

One file per source in `wiki/episodes/`, distilled from one raw file: summary,
key takeaways, quotes, concepts. Called *episode* in the folder name for
historical reasons (the first corpus was a podcast); the concept covers articles
too. A record is faithful, never additive — nothing in it that isn't in the raw.

Deliberately named *record*, not *note*: a note in this system's vocabulary
(`second-brain/knowledge/notes/`) is his own thinking. Nothing in this domain is.

## Concept

A page in `wiki/concepts/` that compiles what **several** sources say about one
topic. Sits between the second brain's two objects and matches neither: a MOC
only links, a note is personal thinking, a concept is attributed external
knowledge assembled across sources. That gap is why this domain exists
separately.

A concept has a **status**:

- `stub` — one or two sources, not yet enough to say anything general.
- `developed` — enough sources to be genuinely cross-source; eligible for
  synthesis.
- `synthesized` — a cross-source synthesis has been written.

A concept has **aliases**: alternative names it must not be duplicated under
(French legacy name, English variant, plural, acronym).

## Candidate concept

A concept name proposed by the record-writing stage, in the record's frontmatter.
A candidate is not a concept: it becomes one only when the concept stage accepts
it, possibly by folding it into an existing concept instead. The distinction is
what keeps the cheap parallel stage from re-creating duplicates.

## Synthesis

A cross-source distillation of a `developed` concept: what the sources agree on,
where they disagree, what follows. Produced on demand, never automatically. Still
external knowledge, still attributed — a synthesis is not a personal note either.

## Theme

The routing layer above the concepts: a group of `developed` concepts, with a
trigger line saying when to open it and a one-line gloss per concept saying what
opening it buys you. Twenty-two of them, in `wiki/themes/`. A theme adds no
knowledge — it exists so that a question reaches the right two or three pages
without loading the catalogue (`docs/adr/0003`).

Curation lives in `stage3/theme_map.py`, judgement in `stage3/theme_prose.py`,
assembly in `generate_themes.py`. Editing a generated page loses the edit.

## Rank 1 and rank 2

Inside a theme. **Rank 1** is its curated `developed` concepts, the substance.
**Rank 2**, printed as *sharp edges*, is the stubs and single-source names
attached to that theme, derived from shared records rather than curated. Rank 2
is often the most actionable material in the corpus (`Toggle Switch`,
`Alt Text`) and is reached through the record, not a concept page.

## Router

`wiki/themes/_router.md`, 594 words: the entry point an agent reads first, and
the only file it needs in context to decide where to go next. Distinct from
`wiki/index.md`, which is a 220 KB flat catalogue with no routing value.

## Playbook

A theme distilled into assertive, checkable rules for a design review, in
`wiki/playbooks/`. A **cache** of the concept pages, written only for the themes
a review actually runs against, and dated by `sources_as_of` so
`stage3/check_playbooks.py` can flag it when its concepts move (`docs/adr/0004`).

Distinct from a synthesis: a synthesis deepens a concept for a reader, a
playbook flattens a theme into rules for a reviewer.

## Topic filter

The rule deciding which articles of a large catalogue enter the corpus at all.
For Nielsen Norman Group: published 2016 or later, and tagged with one of the
retained topics. Applied at scrape time, so unwanted material never reaches
`raw/`.
