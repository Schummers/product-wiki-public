---
name: product-wiki-consult
description: |
  Answer a product or design question from the product-wiki corpus (1000+ sourced records and 160+ developed concepts), citing what the sources actually say. Use when deciding how to structure a page or navigation, choosing a control or pattern, picking a research method, designing for mobile or accessibility, setting metrics, designing an AI feature, or asking "what are the best practices for X" and wanting evidence rather than opinion. Also use when a claim needs checking against real sources.
---

# Consult the product wiki

Answers a design question from `~/AI OS/compound-learning/product-wiki`, a corpus of external
material: 864 Nielsen Norman Group articles, 90 Parlons Design transcripts and the chapters of three books,
distilled into records and cross-source concept pages.

**The corpus is the authority here, not your priors.** The value of this skill
is that every claim traces to a source the owner chose. An answer assembled from
general knowledge and dressed in citations destroys that value. When the corpus
does not cover the question, say so in one line and stop.

## Route

Three rungs, each pointing at the next. Take them in order.

1. **`wiki/themes/_router.md`** — one trigger line per theme. Pick one to
   three. This is the only file you read in full.
2. **The theme pages you picked** — each concept carries a gloss saying what
   opening it buys you. Pick two to four concepts from those glosses.
3. **The concept pages** — open them and read the `###` sub-sections that bear
   on the question. A page runs 3000 to 6000 words; read the relevant sections,
   not the whole file.

Two side doors:

- A theme's **Sharp edges** section lists narrow single-source ideas (`Toggle
  Switch`, `Alt Text`, `Button Design`). When the question is that specific,
  open the record it names instead of a concept page.
- **`wiki/orphans.md`** indexes every single-source name when a theme's
  sharp edges do not carry the one you want.

Read `wiki/episodes/<record>.md` when a concept page's claim needs its original
context. Leave `wiki/index.md` closed: 220 KB of flat catalogue with no routing
value.

`raw/` follows the source. For an **article or a transcript**, leave it closed:
the record covers a short source closely, and the raw is an unprocessed dump.
For a **book**, open it. A chapter record distils 10 to 17 thousand characters
of argued prose into 3 to 6 takeaways, and only its `> ` quotes are verified
character by character (`check_records.py`); the Summary and Key Takeaways are
unverified paraphrase, which has drifted in practice — a fabricated conversion
rate, a figure attributed to a chapter that never states it (`check_claims.py`,
`docs/adr/0005`). So when a book-sourced claim will drive a decision, or
carries a number, open `raw/sources/<same basename as the record>.md` and read
the passage. A record with `source_type: book` names its `raw:` path in
frontmatter.

## Weigh the sources

The corpus is not uniform, and an answer that flattens it misleads.

- **Nielsen Norman Group** (`source_type: article`, named researcher) reports
  study-backed findings. Durable.
- **Parlons Design** (`source_type: transcript`, Romain Penchenat) is
  practitioner opinion and tool review. Useful, and dated faster.
- **Books** (`source_type: book`) argue a position across a whole work. One
  book is one *work*, however many chapters cite it: eight chapters agreeing
  is one author agreeing with themselves, not eight sources. Say which book a
  claim comes from, never "the sources say".
- Check `published` when the claim is about a tool, a trend or a platform
  convention. A 2016 finding about attention still holds; a 2024 claim about a
  Figma feature may not.

When two sources disagree, report both positions and name them. The concept
pages already flag their disagreements: carry that through rather than
resolving it.

## Answer

- Every claim carries its source as `[[record]]`, or names the concept page it
  came from.
- Lead with what the sources establish, then the caveats and the disagreements.
- Say plainly which part of the question the corpus does not answer.
- Attribute, never appropriate: this material is external, and none of it is
  the owner's own thinking.

**Done when** every claim in the answer is attributed, the disagreements the
sources hold are visible as disagreements, and any uncovered part of the
question is named.
