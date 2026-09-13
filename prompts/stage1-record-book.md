# Stage 1 prompt — book chapter to record

The variant of `stage1-record.md` for a chapter of a book (docs/adr/0005: a
book enters as one raw per chapter). Same rules, book fields added, and one
extra constraint: a chapter record does not summarise the book. Substitute
`{{FILES}}` with the numbered list of raw basenames, `{{DATE}}` with today,
and `{{CANDIDATE_CONCEPTS}}` with a book-specific list — see below.

Validated on a 3-chapter pilot (2026-09-03) before the rest of the two
studio books. Lesson from that run (`CLAUDE.md`, "Ingesting a book" step 3):
records converge on the same candidate names, with nothing left to merge,
when the prompt hands agents a short list of names to reuse instead of
letting each agent coin its own. `{{CANDIDATE_CONCEPTS}}` is that list — draft
it fresh for each book (8-15 names: skim the table of contents and 2-3
chapters, check `ls wiki/concepts/` for names already in the corpus that
fit), never carry a previous book's list forward. The two studio books used
`Venture Studio`, `Studio Funnel`, `Entrepreneur in Residence`, `Stage Gate`,
`Studio Economics`, `Equity Ownership`... — kept here only as a worked
example of the shape, not as defaults for the next book.

---

You are running **stage 1** of the ingestion pipeline in the vault
`~/AI OS/compound-learning/product-wiki`.

FIRST: read `~/AI OS/compound-learning/product-wiki/SCHEMA.md`
in full. It is the contract you must follow. Everything below assumes it.

Your job: turn each of these raw files, **one chapter of a book each**, into
exactly one **record**.

Raw files (in `raw/sources/`):

{{FILES}}

For each one:

1. Read the raw file completely. Its frontmatter carries `title`, `date`,
   `url`, `author`, `topics`, plus the book fields `book`, `part`, `chapter`,
   `chapter_number`.
2. Write the record to `wiki/episodes/<same basename as the raw file>.md`.
3. Frontmatter, exactly per SCHEMA.md:
   - `type: source`
   - `name:` the raw file's `title` (it already reads `<Book>: <Chapter>`),
     double-quoted, inner quotes escaped
   - `created: {{DATE}}`
   - `published:` the raw file's `date` (the book's publication date)
   - `source_type: book`
   - `status: summarized`
   - `url:` the raw file's `url` (the book's reference page)
   - `author:` the raw file's `author`, exactly as written there (the book's
     authors, even when the chapter is a guest contribution)
   - `raw: raw/sources/<basename>.md`
   - `book:` the raw file's `book`, double-quoted
   - `chapter:` the raw file's `chapter`, double-quoted
   - `concepts:` a list of 3 to 6 **plain double-quoted strings** (NOT wikilinks)
4. Body sections, in this order: `# <name>`, `## Summary`, `## Key Takeaways`,
   `## Quotes`, `## Concepts`.
   - `## Summary`: one or two paragraphs. First sentence situates the chapter
     in the book (which part, what it covers); the rest says what **this
     chapter** argues. Do not summarise the whole book, do not repeat what
     other chapters say.
   - `## Key Takeaways`: 3 to 6 bullets, each written exactly as
     `- **Label** — what the chapter actually says`. The `**` bold markers wrap
     the short label ONLY; the explanation after the em dash is plain text.
     Never bold the whole bullet. Detailed enough to be useful without
     reopening the raw file. Numbers, ranges and named examples from the
     chapter are welcome; nothing from outside it.
   - `## Quotes`: 1 to 3 verbatim quotes from the chapter, as `> ` blockquotes.
     **Verbatim means you copy the characters from the raw file.** Never retype
     a sentence from memory, never tighten it, never drop a parenthetical, never
     swap a word for a shorter one. If a sentence is too long, quote a shorter
     span of it that is still contiguous and exact, rather than compressing it.
     The only edit allowed is removing markdown emphasis markers (`**`, `*`),
     backslash escapes and link syntax that fall inside the quoted span.
     Quote running prose, never a line from a table or a figure caption.
   - `## Concepts`: **one bullet per concept in the frontmatter, all of them.**
     Format: `- [[Concept Name]] — what this specific chapter contributes to
     that concept.` The names must match the frontmatter strings exactly,
     character for character.

5. **Verify before you finish.** Once the batch is written, run:

   ```
   cd "~/AI OS/compound-learning/product-wiki" && python3 check_records.py <basename> <basename> ...
   ```

   passing every basename you wrote. It checks schema conformance, that each
   frontmatter concept is linked in the body, and that each quote really is
   verbatim in the raw file. Fix every problem it reports and run it again.
   Do not finish while it still reports a problem on one of your records. If a
   quote is flagged, open the raw file, find the real sentence, and replace your
   quote with the exact span.

CRITICAL RULES:

- **Write in English.** This corpus is English.
- **No fabrication.** The record contains only what the chapter says. No
  advice, example, statistic or nuance the chapter does not provide. If you are
  unsure whether the chapter says something, leave it out.
- **Never create or edit any file in `wiki/concepts/`.** You propose concept
  names only. Broken `[[links]]` are expected and correct at this stage; a
  later stage resolves them.
- **Concept naming**: established English terms in Title Case, singular rather
  than plural, never a name with a slash (it cannot be a filename — write
  "Stage Gate", not "Go/No-Go Decision"). Before inventing a name, check
  whether a concept page already exists that means the same thing:
  `ls "~/AI OS/compound-learning/product-wiki/wiki/concepts/"`
  and reuse the exact existing filename when it matches. For this book's own
  vocabulary, use these exact names when they fit, so the chapters converge
  on the same candidates instead of each agent coining its own:
  {{CANDIDATE_CONCEPTS}}
  Coin a new name only when none of the above covers what the chapter says.
- Do not touch any other file. Do not run the index or verification scripts.

When done, reply with only: the record paths you wrote, and any raw file you
could not process and why.
