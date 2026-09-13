---
type: concept
name: Card Sorting
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Card Sorting (Tri de cartes)"
  - "Tri de cartes"
---

# Card Sorting

## Definition

Card sorting is a UX research method in which participants organise labelled
cards into groups according to their own logic, revealing how they naturally
categorise content and what they assume about the relationships between items
[[2024-02-02_card-sorting-definition]]. Its purpose is to surface users' mental
models so that navigation and information architecture can be built to match
them rather than to match an internal org chart
[[2022-04-10_ia-study-guide]].

It sits at the discovery end of the research toolkit: it is run early, before a
structure exists, to generate ideas about how content could be organised
[[2024-02-23_card-sorting-tree-testing-differences]]. Beyond information
architecture, the method is also used on feature concepts, with minimal cards
pairing a visual and a short description, so that users can sort candidate
features by interest or by type of use
[[2024-06-04_331_Tester_un_concept_de_fonctionnalité,_3_méthodes_d_UX_&_Market_research]].

## Practice

### Variations and study design

Card sorting comes in several forms — open, closed, hybrid; moderated or
unmoderated; in person or remote — each suited to a different research goal
[[2024-02-02_card-sorting-definition]]. Open card sorting, where the researcher
supplies no predefined categories, is the most common approach and the one that
allows unbiased discovery of how users organise content on their own terms.
Studies can be run remotely with tooling such as OptimalSort
[[2024-02-02_card-sorting-definition]],
[[2024-02-23_card-sorting-tree-testing-differences]].

Practical parameters [[2024-02-02_card-sorting-definition]]:

- Prepare 30–50 cards. Fewer keeps participants from fatiguing; beyond 50 they
  start dumping items into oversized "Miscellaneous" categories.
- Recruit 15 or more participants for a qualitative study, 30–50 for a
  quantitative one. Qualitative studies lean on think-aloud to understand
  reasoning; quantitative studies track how frequently groupings recur across a
  larger sample.
- Ask participants to label their groups *after* sorting, not before: labelling
  afterwards stops them from confining themselves to predefined categories and
  exposes their categorisation logic.

### Avoiding keyword matching

The main threat to validity is keyword matching: participants group cards by
word similarity (every card containing "Employee") instead of thinking about
what the items actually mean and how they relate
[[2024-06-14_card-sorting-terminology-matches]]. The resulting groups produce
vague labels that do not represent users' real mental models. Countermeasures
fall into two families.

Card wording:

- Use synonyms to break parallel language, for example "Staff Directory"
  instead of "Employee Directory", so participants must consider meaning.
- Deliberately vary grammatical structure ("Benefits for Employees" vs.
  "Employee Benefits") so cards cannot be scanned and matched at a glance.
- Replace short labels with in-depth descriptions explaining purpose and
  medium, which pushes participants to reflect on content meaning.

Facilitation:

- Explain the study objective so participants know conceptual grouping is what
  is wanted.
- Ask them to think aloud, request subcategories, and let them revise their
  groupings iteratively.

### Reading the results

Results are ideas, not prescriptions. Participants routinely group the same
content differently, so the output needs designer judgement, critical thinking
and often further research before it becomes an IA
[[2024-02-02_card-sorting-definition]],
[[2024-02-23_card-sorting-tree-testing-differences]]. Known limitations: the
method strips away broader context, and it exposes only one level of
categorisation.

Card sorts are also the place where **outliers** appear — items participants
associate only weakly with a category, or that cluster in unexpected ways
[[2021-10-17_ia-category-outliers]]. Rather than forcing them into strictly
logical categories, that source draws on categorisation theory: human
categories rest on family resemblance, members share overlapping rather than
identical traits, boundaries shift as new items arrive, and a noncentral member
still belongs (an unusual car is still recognisably a car). Three ways to
handle the outliers a sort reveals:

1. Create a dedicated subcategory — appropriate when family resemblance to the
   main group is low, but it risks deep structures with sparsely populated
   categories.
2. Leave them in the broader category and support findability with robust
   search, facets and metadata — this respects users' mental models.
3. Use polyhierarchy, listing the item both in its subcategory and in the main
   category, while watching out for overlap so heavy that users cannot tell the
   two apart.

### Pairing with tree testing

Card sorting and tree testing are complementary rather than competing
[[2024-02-23_card-sorting-tree-testing-differences]],
[[2022-04-10_ia-study-guide]]. Card sorting discovers, using individual labelled
cards to explore possible groupings before a structure exists. Tree testing
evaluates, using a text-based hierarchy — with tools such as Treejack — to check
whether users can locate content inside a proposed or existing IA, deliberately
without the distraction of visual design. Its own limitation mirrors that
strength: the isolated hierarchy lacks the colour, imagery and placement cues
that help findability on a fully designed site. Using both gives discovery
insight and evaluative validation across the IA process.

### Beyond information architecture: testing feature concepts

Card sorting also appears as one of three methods for testing appetite for a
feature before building it, alongside fake doors and fake landing pages
[[2024-06-04_331_Tester_un_concept_de_fonctionnalité,_3_méthodes_d_UX_&_Market_research]].
Here the cards are "feature cards": minimal cards combining a visual and a short
description of a candidate feature, which participants sort by interest or type
of use in a qualitative session. The source is explicit about the trade-off —
feature cards are simple to set up but carry higher bias than in-product
methods, because they are far removed from a real usage context, and the
overriding risk in this kind of testing is confirmation bias.

## Sources (8)

- [[2021-10-17_ia-category-outliers]] — Card sorts reveal outliers and unexpected groupings from users, providing data to inform IA decisions about category boundaries.
- [[2022-04-10_ia-study-guide]] — a research method for discovering how users naturally categorize content and information.
- [[2024-02-02_card-sorting-definition]] — a specialized research method for discovering users' mental models and natural content-organization patterns.
- [[2024-02-23_card-sorting-tree-testing-differences]] — a discovery research method for understanding user mental models of content organization.
- [[2024-06-04_331_Tester_un_concept_de_fonctionnalité,_3_méthodes_d_UX_&_Market_research]]
- [[2024-06-14_card-sorting-terminology-matches]] — card sorting is a UX research method for understanding mental models, but must be carefully designed to measure conceptual relationships rather than word similarities.
- [[2024-01-23_laws-of-ux_06-4-hicks-law]] — user research method where participants organize topics into groups reflecting their mental models; identifies information architecture expectations.
- [[2016-11-04_ux-research_04-chapter-3-quantitative-research-methods]] — card sorting is explored as a generative method where participants arrange topics in logical chunks based on their understanding, with variations between open and closed approaches and moderated and unmoderated formats
