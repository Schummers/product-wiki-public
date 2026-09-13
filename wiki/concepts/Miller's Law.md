---
type: concept
name: Miller's Law
created: 2026-09-10
updated: 2026-09-10
status: stub
aliases:
  - "Chunking"
  - "Working Memory"
---

# Miller's Law

## Definition

Miller's Law states that the average person can hold roughly seven items, plus
or minus two, in working memory
([[2024-01-23_laws-of-ux_05-3-millers-law]]). Working memory is the temporary
buffer that holds the information relevant to the task at hand, and its
capacity is not a fixed constant: it varies by individual and depends on
familiarity with the content, on context, and on complexity. Yablonski notes
that there is research putting the average limit closer to four items, and other
theories arguing against measuring capacity as a fixed number of elements at
all.

The law is widely misread in design practice as a cap on the number of
interface elements. George Miller's 1956 research was not about that: his
actual contribution was **chunking** — showing that grouping bits of
information into meaningful units helps memorisation more than the raw count of
items does ([[2024-01-23_laws-of-ux_05-3-millers-law]]). The design payload of
the law is therefore [[Cognitive Load]] theory: organise content to match how
the brain processes information, rather than counting to seven.

## Practice

### Chunk, do not count

Formatting information into chunks is what aids memory. The example the source
uses is a phone number: the same digits are easier to process and memorise when
broken into groups than as an unbroken string
([[2024-01-23_laws-of-ux_05-3-millers-law]]).

### The seven-item navigation rule is a myth

A navigation menu does not need to be memorised, because the choices stay
visible. Yablonski's counter-example is Nike.com, whose navigation exceeds
seven items and remains scannable through clear categorisation, whitespace and
visual grouping — evidence that the "magical number seven" is not a design rule
([[2024-01-23_laws-of-ux_05-3-millers-law]]).

### How to chunk visually

Create distinct groups with visual hierarchy, colour, scale, dividers and
spacing. The source applies this to dense information layouts, ecommerce
product groupings, and toolbars in editing applications
([[2024-01-23_laws-of-ux_05-3-millers-law]]). See
[[Information Architecture]].

### What chunking buys

When incoming information exceeds working-memory capacity, users struggle, miss
details, and may abandon the task; chunking reduces cognitive load by
organising content into digestible groups. Effective chunking helps people
scan, identify what is relevant to their goal, and process content faster. A
wall of text with no hierarchy is harder to parse than the same content broken
up with headings, sections and whitespace
([[2024-01-23_laws-of-ux_05-3-millers-law]]).

## Sources (1)

- [[2024-01-23_laws-of-ux_05-3-millers-law]] — principle that working memory capacity is limited and optimized through chunking information into meaningful units; grouping related information, objects, and actions together using visual design to make content easier to comprehend and process; the temporary buffer space in human cognition for storing information relevant to the current task.
