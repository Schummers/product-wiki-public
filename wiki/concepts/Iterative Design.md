---
type: concept
name: Iterative Design
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Iteration"
  - "Itération"
  - "Parallel Design"
  - "Iterative Process"
---

# Iterative Design

## Definition

Iterative design is the intentional repetition of a step in the design process
with the goal of improving the design at that stage
([[2024-12-03_parallel-and-iterative-design]]). Its premise is that there is no
one perfect interface and that usability cannot be obtained by shipping a single
best idea: a candidate design is a hypothesis, and it must be put in front of
users, found wanting, and revised
([[2016-12-18_ux-prototype-hi-lo-fidelity]]). The cycle — create, test, identify
issues, improve, repeat — runs until the design is good enough to release or to
face a summative evaluation ([[2019-07-28_formative-vs-summative-evaluations]]).

The sources pair it with a sibling process, parallel design, which explores
several alternatives at once instead of refining a single one; ideation feeds
that exploration by generating many candidates before any of them is prototyped
([[2017-01-15_ux-ideation]], [[2024-12-03_parallel-and-iterative-design]]). What
makes the loop affordable is fidelity: it is cheap to discard a sketch and
expensive to discard production code, so iteration is concentrated as early as
possible ([[2016-12-18_ux-prototype-hi-lo-fidelity]],
[[2021-12-19_paper-prototyping-cutout-kit]]). Iteration is also something a
designer is expected to be able to narrate afterwards — showing the successive
versions is how the reasoning behind a final solution becomes legible
([[2024-12-03_354_Les_6_tips_de_présentation_d_un_case_study_design_-_Guide_Product_Design]]).

*User Story Mapping* extends the same logic to delivery rather than to a
single screen: Patton treats a slice of working, end-to-end software as the
unit that gets iterated, refined in workshops, shipped, and learned from,
rather than a component built once to a finished specification
[[2014-09-05_user-story-mapping_15-10-bake-stories-like-cake]].

## Practice

### The loop, and how many turns it takes

[[2024-12-03_parallel-and-iterative-design]] calls iterative design the simplest
and cheapest of the three usability processes it describes, and the oldest
foundation of user-centred design; an iteration can often be completed in a few
hours. It recommends at least two to ten iterations, citing research showing 38%
usability improvement per iteration in traditional development, with measurable
gains continuing indefinitely, and warns that a first redesign typically still
carries many usability problems. [[2018-08-26_case-study-iterative-design-prototyping]]
confirms the point from practice, running three rounds of testing on the NN/g
homepage across desktop and mobile, and stresses that this does not require a
large budget: planning several rounds and using discount methods produces steady
improvement without unreasonable delay.

[[2019-07-28_formative-vs-summative-evaluations]] supplies the evaluation
vocabulary. Formative evaluations ask what works and what breaks, run repeatedly
through a redesign with a few users per study, and feed the loop; summative
evaluations ask how the finished thing performs against a benchmark — prior
version, competitor, industry standard — and happen rarely, just before or after
a redesign. It corrects a common misconception: formative work is often
qualitative for speed and cost but can be quantitative in mature organisations,
and summative work is often quantitative but can be qualitative, as in an expert
review. The final summative evaluation it describes is a go/no-go decision before
launch.

### Iterate in parallel, not only in series

[[2024-12-03_parallel-and-iterative-design]] argues that iteration alone leaves a
team stuck refining its own best idea. Parallel design creates three to five
alternatives simultaneously, tests them, and merges the best ideas into one
design before iterative refinement continues. Its reported figures: merging gave
70% usability improvement versus 56% for simply picking a winner, and further
iteration added 48% more. Competitive testing against three or four competitors'
designs is offered as a third, complementary source of insight. The stated
purpose of design diversity is to avoid design fixation.

[[2017-01-15_ux-ideation]] supplies the upstream half of that argument. Ideation
generates a broad set of ideas with no attempt to judge them, favouring quantity
over quality, because breadth raises the odds that one idea seeds a great
solution; evaluation must be postponed so judgement does not stifle contribution,
ideas must be recorded as tangible artefacts, and groups produce more variety
than individuals. It places ideation after research and before prototyping, and
insists ideas be grounded in a problem statement built on user research rather
than on technology or trends — without that grounding, the ideas are worthless
and the team lacks criteria to choose between them. A break between generation
and evaluation improves the decision.

### Keep fidelity low while the loop is fast

[[2016-12-18_ux-prototype-hi-lo-fidelity]] frames a prototype as a hypothesis to
be tested, and sets out the trade-off. Low-fidelity prototypes need less
preparation, allow design changes between sessions, put less pressure on
participants who feel less obliged to succeed with an unfinished-looking
interface, and reduce designer attachment, so teams discard them more readily
when testing goes badly. High-fidelity prototypes give realistic system response,
remove facilitator delay and human error, let the facilitator observe instead of
operating the prototype, and support testing of specific components, graphical
affordances and page hierarchy — at the cost of build time, since every click
target must be correct. Fidelity varies independently across dimensions
(interactivity versus visuals), so the level should be chosen from what actually
needs testing.

[[2021-12-19_paper-prototyping-cutout-kit]] pushes fidelity to its floor: sketch
concepts and flows on paper and test them with a facilitator, a participant and
optionally a "computer" who manipulates the screens — a role that keeps momentum
by avoiding wait times. Scrolling is simulated with long sheets pulled through a
frame cutout, dropdowns and overlays with separate paper layers. When a problem
recurs across sessions, blank paper lets the team build new screens between
sessions, which is where the fast cycle actually happens. Two constraints: keep
fidelity consistent across all screens, because mixing detailed and rough screens
skews participants' attention and feedback toward the detailed ones; and apply
standard usability-testing practice regardless — proper recruitment, clear tasks.

[[2016-08-28_ux-success-agile]] reaches the same conclusion from the Agile side:
treat design as iterative rather than perfect, use low-fidelity sketches and
wireframes to fail fast and catch flaws before coding. It adds process conditions
— invest in discovery and release planning before sprints, keep research and
design one to two sprints ahead of development so there is time to iterate, run
usability sessions as team events so decisions rest on data, and treat the
methodology itself as something to iterate on.

### Steering the iterations

[[2018-08-26_case-study-iterative-design-prototyping]] documents a full sequence:
qualitative surveys of audience expectations, design goals stated as outcomes
rather than features, low-fidelity wireframes, then high-fidelity visual
prototypes, then three rounds of testing, narrowing the set of versions at each
round. It uses a ranked content hierarchy as the through-line that keeps
successive iterations consistent and drives layout for both desktop and mobile,
and a modular component system with a master stylesheet so specification does not
have to be redone each time a component changes. Its rule for reading test
results: pay attention to what people do, which is often different from what they
say.

### Slicing as the unit of iteration (Patton)

*User Story Mapping* arrives at iteration from a different angle than the
usability-testing sources above: not repeated rounds on one screen, but
successive end-to-end slices of a product. Patton's baking metaphor makes the
rule explicit — when a story describes more work than is affordable, resist
the instinct to split it by technical layer (weeks of frontend, weeks of
backend); split it into small, complete, end-to-end slices ("cupcakes") that
users can evaluate, so the team learns sooner and can adjust course. "Half a
baked cake may not be enough to feed a wedding party, but it's enough to taste
and leave everyone looking forward to the rest of the cake"
[[2014-09-05_user-story-mapping_15-10-bake-stories-like-cake]]. At Workiva this
becomes a three-phase release plan — an opening game, midgame and endgame,
each slice building on the last as the team learns and adjusts, rather than
building sequentially and assembling at the end
[[2014-09-05_user-story-mapping_09-4-plan-to-finish-on-time]].

The **story workshop** is where this loop runs at the level of a single
story: rough stories from the backlog are polished through collaborative
discussion — by a small group of three to five, product-minded person,
developers and a tester — until they are small enough to build in a couple of
days or less and clear enough for shared understanding and predictable build
time. Patton calls it the "magic machine" that turns raw opportunities into
confirmed work: stories start rough, are refined in workshops, built and
tested in cycles, reviewed as a team, and improved based on what is learned,
a spiral toward a releasable product rather than a single pass
[[2014-09-05_user-story-mapping_21-16-refine-define-and-build]]. When a story
is still too large after a workshop, the Good-Better-Best game splits it into
a minimal viable version, enhancements, and delightful extras, and the team
builds that progression to gain confidence and maintain momentum
[[2014-09-05_user-story-mapping_21-16-refine-define-and-build]].

Patton closes the loop past release, which the usability-testing sources above
frame mainly as pre-launch. Building software is only part of the work; the
real work is learning whether it achieves the outcome, through team product
reviews, stakeholder reviews connecting the work to business value, and
testing with real users doing real work rather than watching a demo. "Software
is never done; outcomes are never insured" — teams should measure or observe
real outcomes after every release, not wait for complaints, and plan the next
cycle's improvements from what they learn
[[2014-09-05_user-story-mapping_23-18-learn-from-everything-you-build]].

### Making iteration visible afterwards

[[2024-12-03_354_Les_6_tips_de_présentation_d_un_case_study_design_-_Guide_Product_Design]]
addresses the same process from the presentation side, in a design-interview
context. It advises briefly showing the successive stages and versions of a
design, because the iterations are what explain the reasoning and show how
testing led to the final solution. Consistent with this, it warns against
presenting a standardised, by-the-book process: what should be foregrounded is
how methods were adapted to the specific project, the unexpected turns and
failures included, and the real-world impact measured afterwards through data,
NPS or qualitative feedback — not the deliverables themselves.

## Sources (14)

- [[2016-08-28_ux-success-agile]] — Reinforces the value of low-fidelity prototypes and rapid iteration to discover design flaws early, before development investment.
- [[2016-12-18_ux-prototype-hi-lo-fidelity]] — prototypes enable fast iteration, design changes between sessions, and continuous refinement based on user feedback before implementation.
- [[2017-01-15_ux-ideation]] — ideation supports parallel design by generating multiple solutions before narrowing to prototypes for testing.
- [[2018-08-26_case-study-iterative-design-prototyping]] — a design process of successive refinement through cycles of creation, testing, and improvement; especially effective for homepage and complex interface design.
- [[2019-07-28_formative-vs-summative-evaluations]] — formative evaluations support iterative design cycles: prototype, test, identify issues, improve, and repeat; this cycle continues until the design is ready for release or summative evaluation.
- [[2021-12-19_paper-prototyping-cutout-kit]] — Testing sessions reveal problems that can be fixed between sessions using blank paper, enabling rapid cycles of design discovery and refinement.
- [[2024-12-03_354_Les_6_tips_de_présentation_d_un_case_study_design_-_Guide_Product_Design]]
- [[2024-12-03_parallel-and-iterative-design]] — Iterative design involves repeated cycles of testing, identifying issues, and revising designs with incremental improvements that continue indefinitely; parallel design complements this by creating multiple alternative solutions simultaneously, testing them, and merging the best ideas before iterating further.
- [[2021-05-18_continuous-discovery-habits_15-chapter-twelve-managing-the-cycles]] — breaking large opportunities into sub-opportunities and addressing them incrementally allows teams to deliver value while laying groundwork for bigger solutions.
- [[2022-01-19_product-management-for-ux-people_06-chapter-3-ux-skills-that-carry-over]] — The UX practice of solving problems through iterative cycles and hypothesis testing carries directly to product; PM iteration emphasizes data-informed experiments over design-studio critique, combining scientific hypothesis-testing with creative problem-solving.
- [[2014-09-05_user-story-mapping_09-4-plan-to-finish-on-time]] — Applied through the three-phase approach where each slice builds on the previous, with the team learning and adjusting course as they go, rather than building sequentially and assembling at the end.
- [[2014-09-05_user-story-mapping_15-10-bake-stories-like-cake]] — By delivering small, evaluable pieces and gathering feedback from use, the team designs not in isolation but through repeated cycles of building, learning, and refining, reducing the risk of building something no one wants.
- [[2014-09-05_user-story-mapping_21-16-refine-define-and-build]] — The workshop approach supports iterative refinement: stories start rough, are polished in workshops, built and tested in cycles, reviewed as a team, and improved based on what is learned, creating a spiral toward a releasable product.
- [[2014-09-05_user-story-mapping_23-18-learn-from-everything-you-build]] — Post-release learning and iteration are as critical as pre-release planning. Teams should measure outcomes, observe user behavior, identify improvements, and write new stories to address them, creating continuous cycles of refinement.
