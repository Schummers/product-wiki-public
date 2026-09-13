---
type: concept
name: User Flow
created: 2026-07-31
updated: 2026-09-11
status: developed
---

# User Flow

## Definition

A user flow describes the set of specific, discrete interactions that make up a
common user pathway through a single product: the steps and screens needed to
accomplish a task. [[2023-04-16_user-journeys-vs-user-flows]] defines it against
its sibling artefact, the user journey: journeys are macro-level and holistic,
spanning channels and time, while flows zoom in on the micro level inside one
product. Both are structured around user goals and examined from the user's
perspective; what separates them is scope and level of detail.

The flow is not only a navigation diagram. Romain Penchenat's "advanced user
flow charts" add, at each step, the hierarchy of content the user needs there,
so the artefact anticipates user needs rather than merely sequencing screens
([[2025-01-21_361_Top_3_outils_lo-fi_pour_remplacer_les_wireframes]]). Nor is a
flow limited to the ideal path: Anna Dahlström treats the alternative and
non-happy routes as subplots that branch off the main journey and must be
designed alongside it
([[2019-12-17_storytelling-in-design_11-chapter-10-applying-main-plots-and-subplots-to-user]]).

## Practice

### Pair flows with journeys rather than choosing between them

[[2023-04-16_user-journeys-vs-user-flows]] (Kate Kaplan, Nielsen Norman Group)
argues the two artefacts are complementary: using both gives teams the macro and
micro views at once, with flows serving as deep dives into specific areas of the
overall journey. The same record notes an organisational gap — most teams lack a
systematic process to connect the journey view and the flow view, which it
frames as an opportunity for teams that manage to integrate both.

### Research methods differ by artefact

Kaplan ties each artefact to its research method: field studies and diary
studies are best for uncovering the longer-term goals and behaviours a journey
needs, while user flows are best documented through usability testing, where
researchers watch users interact directly with the product under guided
scenarios ([[2023-04-16_user-journeys-vs-user-flows]]).

### Situate the flow among the other mapping methods

[[2017-11-05_ux-mapping-cheat-sheet]] (Sarah Gibbons, Nielsen Norman Group)
places the visualisation of user paths and touchpoints inside a wider toolkit:
empathy mapping for the user mindset, customer journey mapping for a specific
person's chronological interaction with a product, experience mapping for
generic human behaviour independent of a business, and service blueprinting for
the organisational frontstage/backstage view. Any of these maps requires three
decisions before it is built: current versus future state, hypothesis versus
research-based, and low versus high fidelity. See [[Customer Journey]].

### Design the branches, not only the happy path

Dahlström
([[2019-12-17_storytelling-in-design_11-chapter-10-applying-main-plots-and-subplots-to-user]])
warns that abstracting to the ideal path can miss critical design requirements,
because real use is messy and non-linear — users search wide, shift focus, and
move between online and offline contexts. She proposes three kinds of branch:

- **Alternative journeys** — different routes to the same destination, such as
  entering through search versus through social.
- **Unhappy journeys** — experiences that do not go as the user intended, from
  minor frustrations to outright failure; forgotten-password flows and cart
  abandonment are the standard examples.
- **Branched journeys** — decision-tree structures in interactive experiences
  such as chatbots, voice interfaces and booking apps.

Her constraint on all of them: a subplot must connect to and impact the main
plot, otherwise it does not belong in the design. Storymaps are the
visualisation she recommends to show the overview of these branches, where they
intersect the main path, and which user types are involved. See [[Subplot]].

### Enrich the flow with the content each step requires

In [[2025-01-21_361_Top_3_outils_lo-fi_pour_remplacer_les_wireframes]],
Penchenat presents the advanced user flow chart as one of three replacements for
wireframing: mapping the path and, at each step, the key content it needs. He
also frames it as a good objective communication support with developers and
product managers. In the same episode he pairs it with
[[Object-Oriented UX]] — structuring the application around its main objects,
their relationships and their possible actions — as a way to consolidate the
project's structure before drawing any interface.

### Study competitors' flows, in context

[[2025-04-15_373_Top_5_outils_de_benchmark_UXUI_gratuits]] treats user flows as
one of the things worth examining in a full UX/UI benchmark, and names
Pablo.club as a free library dedicated to them. The record's main warning
applies here: the most critical benchmarking error is forgetting your own
context and the context of the actor you are looking at, so an observed flow
should be adapted to your own objectives, never copied because a recognised
player uses it. See [[Benchmarking]].

## Sources (5)

- [[2017-11-05_ux-mapping-cheat-sheet]] — relates to customer journey and experience mapping as methods for visualizing user paths and touchpoints.
- [[2023-04-16_user-journeys-vs-user-flows]] — Details the specific, discrete interactions and steps within a single product needed to accomplish common tasks, focusing on the ideal pathway through screens.
- [[2025-01-21_361_Top_3_outils_lo-fi_pour_remplacer_les_wireframes]]
- [[2025-04-15_373_Top_5_outils_de_benchmark_UXUI_gratuits]]
- [[2019-12-17_storytelling-in-design_11-chapter-10-applying-main-plots-and-subplots-to-user]] — subplots map the alternative and edge case flows users take when things don't go as planned, such as forgotten passwords and error recovery paths.
