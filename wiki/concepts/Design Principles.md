---
type: concept
name: Design Principles
created: 2026-07-31
updated: 2026-09-10
status: developed
---

# Design Principles

## Definition

The sources use "design principles" in two related but distinct senses, and [[2020-08-02_design-principles]]
is explicit that they are not the same thing. In the first sense, a design
principle is a **value statement** describing the most important goals a product
or service should deliver for users, used to frame design decisions and resolve
tradeoffs [[2020-08-02_design-principles]] [[2025-04-18_design-guidance]]. These are product-specific: unlike general usability
guidelines or visual-design principles, they belong to the product being
designed, and their job is to reduce subjective debate by anchoring choices to
shared values [[2020-08-02_design-principles]]. In the second sense, design principles are the **foundational
concepts of visual design** — alignment and grids, hierarchy, contrast, balance,
scale, colour harmony, consistency — that make an interface look good and, with
it, work well [[2021-03-07_why-does-design-look-good]] [[2023-03-05_why-does-a-design-look-good-part2]] [[2024-05-17_visual-design-cheat-sheet]].

[[2025-04-18_design-guidance]] places the first sense in a hierarchy of design guidance: principles sit on
top as the guiding philosophy, usability heuristics provide research-backed
assessment applicable to any interface regardless of organisation, design
patterns supply concrete tactical solutions to recurring problems, and team
charters govern team dynamics; the four function together rather than replacing
one another. The common thread across both senses is intention: each decision in
a design should be made deliberately, ideally backed by a visual-design system
[[2021-03-07_why-does-design-look-good]].

[[2024-01-23_laws-of-ux_01-preface]] adds a third sense, close to the first but sourced
differently: a design principle can be a **psychological guideline**, a
principle drawn from cognitive and behavioural psychology that describes how
people actually perceive and process the world, and that a designer can use to
justify a decision when quantitative or qualitative research data is not
available [[2024-01-23_laws-of-ux_01-preface]]. That source is explicit that these are
guidelines informed by observed patterns of human behaviour rather than absolute
laws to be followed rigidly, and that they complement user research rather than
replacing it [[2024-01-23_laws-of-ux_01-preface]].

## Practice

### Writing product-specific principles

[[2020-08-02_design-principles]] gives a four-step process: identify core values, consider user impact,
identify common tradeoffs, then write, compare and iterate. It sets out what
separates an effective principle from a decorative one:

- **Take a stand on conflicting values.** Principles exist to resolve tradeoffs
  (minimalism vs. discoverability, power users vs. casual users), not to
  prescribe UI elements. Where two values regularly collide, state explicitly
  which should win, or name the contexts in which one matters more; ambiguous
  principles create interpretation problems and reintroduce the lengthy debates
  they were meant to end [[2020-08-02_design-principles]].
- **Inspire empathy.** Include why the value matters to users, not only what it
  is; this keeps users at the heart of decisions and lifts the principle above a
  generic statement [[2020-08-02_design-principles]].
- **Stay concise and memorable.** Principles are not essays. Limit them to five
  to eight; ten or more are largely forgotten. Involving content specialists
  helps make them stick [[2020-08-02_design-principles]].
- **Avoid internal conflict** between principles [[2020-08-02_design-principles]].

[[2025-04-18_design-guidance]] adds that principles are most effective when memorable, distinctive,
reflective of brand values, and both general and actionable.

[[2024-01-23_laws-of-ux_13-11-applying-psychological-principles-in-design]] describes a workshop
process for arriving at them: identify the team, align on what success looks
like, diverge into ideas, converge on themes, refine, then circulate, a sequence
whose purpose is widespread adoption and team buy-in. Its criteria for a good
principle overlap with the above and sharpen the point about taking a stand:
principles should be direct, clear and actionable rather than bland truisms,
they should answer real design questions, they should be opinionated with a
clear prioritisation, and they should be memorable enough to be used regularly
[[2024-01-23_laws-of-ux_13-11-applying-psychological-principles-in-design]].

### From principle to law to rule

[[2024-01-23_laws-of-ux_13-11-applying-psychological-principles-in-design]] adds a layer the other
sources do not: a three-tier framework that connects each design principle to
the psychological law supporting it (the observation) and then to specific rules
a team can follow. Its worked examples are "clarity over abundance of choice",
connected to [[Hick's Law]] and translated into rules such as limiting a set of
choices to three items and keeping explanations under 80 characters, and
"familiarity over novelty", connected to [[Jakob's Law]] and translated into
rules about using common design patterns and avoiding flashy animations
[[2024-01-23_laws-of-ux_13-11-applying-psychological-principles-in-design]].

The same source treats team awareness as a precondition rather than an
afterthought: psychological-principle posters displayed in the workspace keep
the principles constantly visible during the design process, and regular
show-and-tell sessions build the shared vocabulary the framework depends on
[[2024-01-23_laws-of-ux_13-11-applying-psychological-principles-in-design]].

### Using them

Publish the principles, reference them regularly, and use them to justify design
decisions [[2020-08-02_design-principles]]. The shift [[2020-08-02_design-principles]] asks for is from "we're doing it this way because
I say so" to "we're doing it this way because principle #3 tips the balance" —
principles guide justification rather than eliminating judgment, and they build
team confidence in the choice. Used well, they ensure consistency in decision
making across designers and teams, removing the need to debate simple tradeoffs
so designers can spend their attention on complex problems [[2020-08-02_design-principles]]. [[2025-04-18_design-guidance]] makes the
same point at team scale: principles help resolve design debates and keep
decisions aligned to a shared vision across products and organisations.
[[2024-01-23_laws-of-ux_13-11-applying-psychological-principles-in-design]] frames a shared set of
principles as a North Star, guiding values embodying what good design looks like
for the team, and credits them with removing the bottleneck created by design
gatekeepers and holding consistency as team size and the volume of decisions
grow [[2024-01-23_laws-of-ux_13-11-applying-psychological-principles-in-design]].

### Visual-design principles: structure

Align to a consistent grid — a column grid in [[2021-03-07_why-does-design-look-good]], three-column or modular in
[[2023-03-05_why-does-a-design-look-good-part2]] — since consistent alignment makes a design look crisp, easier to scan, and
intentionally organised rather than arbitrary [[2021-03-07_why-does-design-look-good]] [[2023-03-05_why-does-a-design-look-good-part2]]. Whitespace is a design
element in its own right, a tool for balance, emphasis and scannability rather
than wasted space [[2024-05-17_visual-design-cheat-sheet]]. Balance can be symmetrical, which feels calm and static,
or asymmetrical, which weights opposite sides differently and creates energy and
engagement [[2023-03-05_why-does-a-design-look-good-part2]].

### Visual-design principles: hierarchy and type

Use size, colour and placement intentionally so the important elements are seen
first [[2021-03-07_why-does-design-look-good]]; [[2023-03-05_why-does-a-design-look-good-part2]] quantifies it, making important elements 30–50% larger, and
varying weight and colour within a limited set of type families. Keep type
variance purposeful: use different styles from the same family (bold, italic,
small caps) consistently for the same purpose across pages, and cap headline
treatments at two different styles [[2021-03-07_why-does-design-look-good]]; too many different type styles overwhelm
users [[2023-03-05_why-does-a-design-look-good-part2]]. Increase leading beyond the default — [[2021-03-07_why-does-design-look-good]] suggests 4–6px extra on
paragraph text — and watch line length and white space between elements so the
design reads open rather than dense [[2021-03-07_why-does-design-look-good]] [[2023-03-05_why-does-a-design-look-good-part2]]. [[2024-05-17_visual-design-cheat-sheet]] frames the same territory
through the Gestalt principles (proximity, similarity, closure, continuation),
which describe how people group visual elements, and notes that continuation
guides users along desired paths in an interface.

### Visual-design principles: colour, contrast and imagery

Limit the palette: two or three carefully chosen colours in [[2021-03-07_why-does-design-look-good]], three or four
in [[2023-03-05_why-does-a-design-look-good-part2]], on the grounds that fewer elements make hierarchy and contrast easier to
convey and monochromatic palettes are the easiest to execute successfully. [[2021-03-07_why-does-design-look-good]]
also advises avoiding primary CMYK colours, which can look unsophisticated. Text
and graphical elements need sufficient contrast against their background for
legibility and accessibility [[2024-05-17_visual-design-cheat-sheet]]. Imagery should add information or context
rather than decorate, and cropping matters, particularly across screen sizes
[[2023-03-05_why-does-a-design-look-good-part2]].

### Consistency as a principle

[[2024-05-17_visual-design-cheat-sheet]] distinguishes internal consistency, within a product, from external
consistency with design conventions, and credits both with reducing cognitive
load and improving usability. [[2021-03-07_why-does-design-look-good]] makes it operational: define clear visual
rules for spacing, typography and padding, then apply them throughout, using
spacing and colour to differentiate groupings and establish relationships. The
tension [[2021-03-07_why-does-design-look-good]] names is that too much variety disrupts consistency and makes a
design look haphazard, so variants must be applied consistently and with
purpose.

### Why it matters beyond aesthetics

Visual details such as fonts, colours and alignment both create a usable
experience and express brand traits like friendliness or reliability [[2021-03-07_why-does-design-look-good]]. [[2023-03-05_why-does-a-design-look-good-part2]]
notes that how something looks affects the perception of how well it functions,
and [[2024-05-17_visual-design-cheat-sheet]] names the underlying effect: users tend to perceive attractive products
as more usable, believing things that look better will work better even when
they are not more effective or efficient. [[2023-03-05_why-does-a-design-look-good-part2]] concludes that good design does
not require complexity or decoration — simplicity plus thoughtful application of
fundamental principles is most effective.

## Sources (7)

- [[2020-08-02_design-principles]] — how to create product-specific design principles that guide decision-making and resolve tradeoffs.
- [[2021-03-07_why-does-design-look-good]] — the article illustrates alignment, hierarchy, consistency, and other core design principles through real-world examples.
- [[2023-03-05_why-does-a-design-look-good-part2]] — understanding grid alignment, type hierarchy, color theory, symmetry, and scale helps designers create aesthetically pleasing interfaces that support usability.
- [[2024-05-17_visual-design-cheat-sheet]] — foundational concepts like balance, hierarchy, contrast, and consistency that guide visual design decisions.
- [[2025-04-18_design-guidance]] — describes value statements that guide team decision-making and ensure alignment across products and organizations.
- [[2024-01-23_laws-of-ux_01-preface]] — The psychological guidelines presented in this book that help designers make decisions aligned with human behavior patterns and cognitive capabilities.
- [[2024-01-23_laws-of-ux_13-11-applying-psychological-principles-in-design]] — provides the framework teams use to ensure consistent decision-making by articulating shared priorities, values, and what good design means within their specific context.
