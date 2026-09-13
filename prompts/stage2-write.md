# Stage 2 prompt — write a concept page from its sources

You are running **stage 2 (writing)** in the vault
`~/AI OS/compound-learning/product-wiki`.

FIRST: read `~/AI OS/compound-learning/product-wiki/SCHEMA.md` in full.

You are assigned a list of concept pages in `wiki/concepts/`. For each one:

1. Read the page: its `## Sources` list names the records that feed it.
2. Open every listed record in `wiki/episodes/` and read its Summary, Key
   Takeaways, and the `## Concepts` bullet for this concept. NEVER open `raw/`.
3. Rewrite ONLY these parts of the concept page:
   - `## Definition` — 1-2 paragraphs: a general synthesis of the concept as
     the sources describe it. Replace the stub placeholder line.
   - Add `## Practice` between Definition and Sources — a structured
     compilation of the guidance the sources give. Use `###` sub-headings when
     it helps. Attributed: cite records inline as `[[basename]]` where a claim
     comes from a specific source; when two sources disagree, say so rather
     than picking one.
   - Frontmatter: set `status: developed` and `updated: <today, YYYY-MM-DD>`.
4. Do NOT touch: the `## Sources` section, `aliases`, `created`, `name`, the
   page filename, or any other file.

ABSOLUTE RULES (SCHEMA.md):
- English.
- Zero fabrication: nothing the sources don't say. No outside knowledge, even
  if you know the topic well.
- Wikilinks (`[[...]]`) only to records or concepts inside this vault.
- Quotes are not needed; if you use one it must come verbatim from a record.

When done, reply with only: the concept names you wrote, and any concept you
could not complete and why.
