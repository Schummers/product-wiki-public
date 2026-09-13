# Stage 1 prompt — raw article to record

The prompt given to the cheap model, one batch of raw files per agent. Part of
the pipeline, versioned so a run is reproducible and a defect is fixable at the
source. Substitute `{{FILES}}` with the numbered list of raw basenames.

Validated on a 5-article pilot (2026-07-30): schema conformance 5/5, quotes
verbatim 14/14, one formatting defect found and folded back into the rules
below (the bold must cover the label only, not the whole bullet).

---

You are running **stage 1** of the ingestion pipeline in the vault
`~/AI OS/compound-learning/product-wiki`.

FIRST: read `~/AI OS/compound-learning/product-wiki/SCHEMA.md` in full. It
is the contract you must follow. Everything below assumes it.

Your job: turn each of these raw articles into exactly one **record**.

Raw files (in `raw/sources/`, all Nielsen Norman Group articles):

{{FILES}}

For each one:

1. Read the raw file completely. Its frontmatter carries `title`, `date`,
   `url`, `author`, `topics`.
2. Write the record to `wiki/episodes/<same basename as the raw file>.md`.
3. Frontmatter, exactly per SCHEMA.md:
   - `type: source`
   - `name:` the article title, double-quoted, inner quotes escaped
   - `created: 2026-07-30`
   - `published:` the raw file's `date`
   - `source_type: article`
   - `status: summarized`
   - `url:` the raw file's `url`
   - `author:` the raw file's `author`
   - `raw: raw/sources/<basename>.md`
   - `concepts:` a list of 3 to 6 **plain double-quoted strings** (NOT wikilinks)
4. Body sections, in this order: `# <title>`, `## Summary`, `## Key Takeaways`,
   `## Quotes`, `## Concepts`.
   - `## Summary`: one or two paragraphs, what the article is about and its
     context.
   - `## Key Takeaways`: 3 to 6 bullets, each written exactly as
     `- **Label** — what the article actually says`. The `**` bold markers wrap
     the short label ONLY; the explanation after the em dash is plain text.
     Never bold the whole bullet. Detailed enough to be useful without
     reopening the raw file.
   - `## Quotes`: 1 to 3 verbatim quotes from the article, as `> ` blockquotes.
     **Verbatim means you copy the characters from the raw file.** Never retype
     a sentence from memory, never tighten it, never drop a parenthetical, never
     swap a word for a shorter one. "People were significantly more likely to
     remember" must not become "More users remembered". If a sentence is too
     long, quote a shorter span of it that is still contiguous and exact, rather
     than compressing it. The only edit allowed is removing markdown emphasis
     markers (`**`, `*`) and link syntax that fall inside the quoted span.
   - `## Concepts`: **one bullet per concept in the frontmatter, all of them.**
     If the frontmatter lists five concepts, this section has five bullets.
     Format: `- [[Concept Name]] — what this specific article contributes to
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
- **No fabrication.** The record contains only what the article says. No
  advice, example, statistic or nuance the article does not provide. If you are
  unsure whether the article says something, leave it out.
- **Never create or edit any file in `wiki/concepts/`.** You propose concept
  names only. Broken `[[links]]` are expected and correct at this stage; a
  later stage resolves them.
- **Concept naming**: established English terms in Title Case, singular rather
  than plural ("Card Sorting", "Cognitive Load", "Progressive Disclosure").
  Before inventing a name, check whether a concept page already exists that
  means the same thing:
  `ls "~/AI OS/compound-learning/product-wiki/wiki/concepts/"` and reuse
  the exact existing filename when it matches. Prefer reusing an existing name
  over coining a new one.
- Do not touch any other file. Do not run the index or verification scripts.

When done, reply with only: the record paths you wrote, and any raw file you
could not process and why.
