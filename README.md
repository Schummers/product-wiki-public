# Product wiki

A reference corpus on product and design, built for coding agents to consult:
external material only, ingested from public sources, distilled into one record
per source and cross-source concept pages, then routed by theme. Nothing here is
the maintainer's own thinking; every claim is attributable to a source.

## Layout

| Folder | Role |
|---|---|
| `raw/sources/` | verbatim ingested material: NN/g articles, podcast transcripts. Written by scripts, never edited |
| `wiki/episodes/` | one record per source: summary, key takeaways, quotes, concepts |
| `wiki/concepts/` | cross-source pages, one per concept, with their own lifecycle status |
| `wiki/themes/` | the routing layer an agent reads first (`_router.md`, then 22 theme pages) |
| `wiki/playbooks/` | themes distilled into checkable rules for a design review |
| `skills/` | three agent skills: `product-wiki-consult`, `product-wiki-review`, `product-wiki-ingest` |
| `stage2/`, `stage3/`, `*.py` | the four-stage pipeline: fetch, record, concept pages, themes |
| `SCHEMA.md`, `CLAUDE.md`, `docs/adr/` | the record schema, the operating manual, the decisions |

## What is not published

This is a public snapshot of a private working repo, published without history
and refreshed by overwriting (`sync_public.sh`). The raw text of the three books
ingested by chapter is **excluded** from the snapshot. Their per-chapter records,
quotes and concept pages are kept. As a consequence, `verify_wiki.py`,
`check_claims.py` and `check_records.py` report those 64 records as having a
missing source when run from this snapshot; that is expected here.

Not a project accepting contributions; shared as a reference.
