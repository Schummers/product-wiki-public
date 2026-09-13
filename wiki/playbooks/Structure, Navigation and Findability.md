---
type: playbook
name: Structure, Navigation and Findability
theme: Structure, Navigation and Findability
created: 2026-08-21
updated: 2026-08-21
status: active
sources_as_of: 2026-07-31
concepts:
  - Information Architecture
  - Navigation Design
  - Content Strategy
  - Web Usability
  - Information Seeking
  - Discoverability
  - Information Scent
  - Search
  - Menu Design
  - Intranet Design
  - Card Sorting
  - Complex Applications
---

# Playbook — Structure, Navigation and Findability

Checkable rules distilled from this theme's concept pages, for
`product-wiki-review`. Give each one a verdict: `holds`, `breached`, or `n/a`
with a reason.

A **cache** of [[Structure, Navigation and Findability]] (`docs/adr/0004`),
not a replacement. Open the concept page when a rule needs its nuance.

Information architecture is the backstage structure; navigation is the
visible interface exposing it. The recurring failure across the corpus is
structure built on internal, organisational logic instead of users' mental
models. [[Information Architecture]]

## Structure

**N1. Depth and breadth are decided by usability, not a click-count rule.**
No evidence that dropoff rises past three clicks; what predicts success is
information scent, wayfinding clarity, cognitive load and page-load time.
Three slow clicks are worse than five fast ones.
[[2019-08-11_3-click-rule]]

**N2. A findable item lives under every path a user would reasonably expect,
within reason.** A polyhierarchy is legitimate practice online, restrained to
two or three research-backed parents, not every conceivable location — it
trades directly against breadcrumbs, which need one canonical path.
[[2018-05-13_polyhierarchy]]

**N3. Related content that lives in two places is cross-linked, never left
to be discovered separately.** Splitting information with no links between
the pieces is a named, recurring failure. [[2016-10-30_top-10-enduring]]

**N4. A structural decision is checked against users' actual mental model,
not fixed by argument.** When users hold an erroneous model of where
something lives, the fix is normally to move the content or the navigation to
match the model, not to correct the user. [[2024-01-26_mental-models]]

**N5. Search and customisation are not substitutes for a weak structure.**
Neither personalisation nor a search box rescues bad information
architecture underneath. [[2016-07-10_customization-personalization]]

## Labels

**N6. A link label is specific, sincere, substantial and succinct, keywords
frontloaded.** Users scan and read only the first few words; a label must
also work standing alone, since surrounding context is often absent on
mobile. [[2019-03-24_better-link-labels]]

**N7. Category labels use the term users already search for, not an invented
or branded one.** A coined term never gets searched for at all; pair any
necessary branded term with the plain-language equivalent.
[[2021-03-28_keyword-foraging]]

**N8. Vague labels ("Resources", "Help") are replaced by what the section
actually contains.** Tested directly: "Customer Service" and "Customer
Assistance" outperformed "Help" and "Help Center", which misled users into
expecting site-navigation help. [[2018-07-29_customer-service-model]]

## Navigation and wayfinding

**N9. Primary navigation stays visible on large screens, not behind a
hamburger.** Navigation is placed where users already look, indicates current
location, and favours familiar patterns over novel ones.
[[2022-04-10_ia-study-guide]]

**N10. A menu with several hierarchy levels uses a mega menu over cascading
dropdowns.** A mega menu exposes several levels at once and reduces the
precision demanded of the user; cascading submenus cost more errors.
[[2019-08-11_3-click-rule]]

**N11. Local navigation is visible but stays subordinate to global
navigation.** If local navigation is more salient, users mistake it for the
main menu. It suits large sites with exploratory browsing, at roughly two to
three tiers. [[2021-07-04_local-navigation]]

**N12. Breadcrumbs show hierarchical position, not click history, and the
current page is not a link.** Unnecessary for shallow or linear structures;
consider truncating or dropping on mobile.
[[2018-12-23_breadcrumbs]]

**N13. Global navigation stays present on subsites and deep pages.**
Its disappearance strands users; progressive disclosure is not a valid excuse
to remove it. Where an organisation runs subsites, a universal-navigation
"exit sign" stays visually subordinate to the subsite's own navigation.
[[2016-11-27_top-intranet-design-mistakes]] [[2016-09-11_universal-navigation]]

**N14. Footers carry the utility links every page needs.**
Contact, customer service, privacy, terms; doormat navigation on long pages;
depth limited to first- and second-level categories; kept visible and
legible rather than hidden behind an accordion or animation.
[[2019-02-24_footers]]

## Search

**N15. Search quality is treated as a structure problem, not a search-box
problem.** Poor results trace back to uncrawled, untagged or miscategorised
content, and a persistent, unified index across content types beats separate
search boxes per section. [[2022-05-22_intranet-search]]

**N16. Filtering supports both include and exclude, tailored per content
type.** A single one-size-fits-all facet set fails different user needs.
[[2016-10-30_top-10-enduring]]

## Chunking and page structure

**N17. Related items are chunked into meaningful groups**, marked by
headings, whitespace and visual grouping. Miller's "magical seven" is not a
hard limit on interface options; well-structured menus with more items still
work. In audio-only interfaces the limit is real: cap a phone menu at four or
five options, since it removes the visual landmarks that make more options
tractable. [[2016-03-20_chunking]]

**N18. Tabs and accordions are matched to content length and device**, not
used interchangeably. On-page and navigation tabs are never mixed; the
selected state carries at least two visual cues, because unselected tabs hide
their own content and need scent. Desktop favours tabs for long, complex
content; mobile favours accordions for short content like FAQs.
[[2024-08-02_tabs-used-right]]

**N19. A listing page balances information density.**
Too little detail and users pogo-stick to detail pages; too much and they
cannot compare choices at a glance. Prioritise attributes from analytics and
research, and keep entries visually consistent for scanning.
[[2016-04-10_list-entries]]

## Placement relative to the task

**N20. Information and controls appear at the point of need, in the order
users actually follow.** Feature completeness is not enough on its own;
misplaced controls make a design interrupt-heavy, and the problem is chronic
because fixing it later means refactoring the flow.
[[2021-07-04_feature-checklists-are-not-enough]]

**N21. A rarely used but critical feature stays reachable.**
A utility's outage map, buried below routine metrics, failed users during a
hurricane: a dormant task can become the only one that matters.
[[2024-07-19_top-tasks]]

## Research and evaluation methods

**N22. Card sorting is run before a structure exists, to discover a
grouping; tree testing is run after, to validate one.**
Card sorting: 30-50 cards, 15+ participants for a qualitative read, groups
labelled after sorting rather than before. Its results are ideas, not
prescriptions — one categorisation level, no context, still needing
designer judgement. [[Card Sorting]] [[2024-02-23_card-sorting-tree-testing-differences]]

**N23. A card-sort result is checked for keyword matching before it is
trusted.** Participants sometimes group by shared words rather than shared
meaning; counter it with synonyms, non-parallel phrasing and think-aloud
facilitation. [[2024-06-14_card-sorting-terminology-matches]]

**N24. A tree-test success rate is read against task importance, not an
absolute bar.** Median success sits around 62%; bands run poor (<40) to
excellent (>90). High success paired with low directness is a sign users
struggled before finding the right path anyway.
[[2024-01-19_interpreting-tree-test-results]]

**N25. An analytics warning sign (low category traffic, high bounce, high
search-query volume) is weighed against strategic importance and layout
before it is treated as an IA problem.** Acting on the number alone risks
cutting a page that is strategically important but low-traffic on purpose.
[[2016-09-25_ia-warning-signs-analytics]]

## Extending structure to AI systems

**N26. A context window is treated as an information architecture problem.**
System instructions, retrieved knowledge, skills, tools and memory compete
for the model's attention the same way page elements compete for a user's;
labels for tools and skills must match user language, not engineering
naming, or the model selects the wrong one. [[2026-06-12_context-architecture]]

**N27. A chatbot answer leads with the essential answer, detail pulled on
demand.** Users treat a site chatbot as a search bar and apply the same
scanning habits: short paragraphs, lists, headers, and a plain refusal when
the system cannot help. [[2026-04-17_less-chat-more-answer]]

## Where this theme stops

Component-level menu and control choices live in
[[Interaction and Interface Patterns]]. Page-level layout and visual
hierarchy live in [[Page Composition and Hierarchy]]. Content voice and
microcopy live in [[Content and Interface Writing]].
