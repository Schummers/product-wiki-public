---
type: concept
name: Prioritization
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Analytics and Prioritization"
  - "Feature Prioritization"
  - "Prioritization Matrices"
  - "Prioritization Methods"
---

# Prioritization

## Definition

Prioritization is the act of ranking candidate work — research questions, user
segments, features, ideas, tasks, roadmap themes — against defined criteria
rather than against opinion [[2021-11-14_prioritization-methods]]. The sources
treat it as a decision method with two simultaneous jobs: producing a defensible
ordering, and producing agreement about it. Prioritization charts are described
as a simple way to assess what is most impactful to the user and to the business,
in a collaborative and disciplined way [[2018-05-27_prioritization-matrices]],
and structured scoring is preferred to unstructured debate precisely because it
yields objectivity and buy-in [[2021-05-23_roadmapping-workshop]].

The inputs to that ranking come from elsewhere in the design system of record:
quantitative data filtered for its uneven distribution
[[2021-10-17_pareto-principle]], user types and goals represented by personas
[[2022-10-09_personas-study-guide]], and research and existing artifacts gathered
before themes are formed [[2020-11-29_roadmapping-steps]]. Its most consequential
output is often a negative one — deciding what not to build
[[2023-12-01_smartwatch-app]].

*Solving Product Design Exercises* decomposes the ranking criterion itself:
impact is reach (how many customers), value for the customer and potential
revenue, weighed against implementation effort, on the premise that there will
always be upsides and downsides for each solution
[[2018-02-12_solving-design-exercises_13-step-5-prioritise-and-choose-an-idea]].

*Continuous Discovery Habits* narrows what gets ranked and loosens how.
Prioritization, in its account, is strategy: it happens in the opportunity
space, by comparing customer opportunities against each other, not in the
solution space by ranking features, and it is a skillfully subjective,
reversible decision made by relative judgement between sibling opportunities
rather than by absolute scoring
[[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]].
The move it asks for is from "whether or not" decisions about one item to
"which is most important" comparisons across a set
[[2021-05-18_continuous-discovery-habits_05-chapter-two-a-common-framework-for-continuous-discovery]].

## Practice

### Choose a method that fits the team, not the "best" method

[[2021-11-14_prioritization-methods]] presents five frameworks and states plainly
that no method is better than another; choose according to project context, team
culture and success criteria, and note that the best methods are the ones the
whole team, stakeholders included, buys into.
[[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]]
would add a prior question: all five frameworks rank items, and it argues that
what a product team should be ranking is opportunities, not features (see
"Prioritizing opportunities, not solutions" below).

- **Impact-effort matrix** — plots relative user value against implementation
  complexity, sorting items into quick wins, big bets, money pits and fill-ins;
  good for quick, democratic, team-wide prioritization.
- **Feasibility-desirability-viability scorecard** — scores each item on three
  criteria and sums for a ranking; highly customizable, criteria can be added or
  swapped for organizational priorities.
- **RICE** — reach × impact × confidence, divided by effort; quantitative and
  formula-based, suited to data-comfortable technical teams with many items.
- **MoSCoW** — clusters items into Must / Should / Could / Will Not Have through
  weighted voting and discussion; works best with clearly defined time horizons.
- **Kano model** — plots functionality against customer satisfaction to classify
  items as Attractive, Performance, Indifferent or Must-be; useful when a team
  struggles to hold user needs against business pressure.

### Frameworks as communication, not decision

Christian Crumlish's chapter on roadmaps surveys the same territory (impact
versus effort, the Eisenhower matrix, RICE, T-shirt sizing) and declines to
endorse any of them: they help articulate reasoning and communicate a decision,
but they do not remove the subjectivity in it, and they are tools for
discussion rather than decision-makers
[[2022-01-19_product-management-for-ux-people_13-chapter-10-roadmaps-and-how-to-say-no]]. He gives the sharpest
formulation to Matt LeMay, product consultant and co-founder of Sudden Compass,
quoted in the chapter:

> Matt LeMay said, "I like to think of all of these as communication
> frameworks. The framework won't help you make a perfect decision, but it will
> help you communicate how you made a necessarily imperfect decision."

For the comparative overview of the methods themselves, the chapter routes the
reader out to Andrea Saez of ProdPad, whose "What is the best framework to
prioritize what to work on next?", published at Product Manager HQ, it presents
as a good survey of the methods and of knowing which to use when
[[2022-01-19_product-management-for-ux-people_13-chapter-10-roadmaps-and-how-to-say-no]]. The chapter also insists that
prioritization is not a linear process and happens at different stages of
development: start with objectives, find problems to solve, and run discovery
to understand which items may produce the desired outcome
[[2022-01-19_product-management-for-ux-people_13-chapter-10-roadmaps-and-how-to-say-no]].

### Running a prioritization matrix

[[2018-05-27_prioritization-matrices]] defines the matrix as a 2D visual showing
the relative importance of a set of items on two weighted criteria, descended
from the Eisenhower Method originally used for time management. Its procedural
advice:

- **Vote first.** Voting speeds the process, structures the plotting, and above
  all prevents the loudest person in the room from dominating the outcome.
- **Encode expertise in the vote.** Coloured dots per area of expertise —
  developers on feasibility, designers on user impact — so that judgement comes
  from the people qualified to give it.
- **Vote privately or digitally** when the team is prone to groupthink or to the
  HIPPO effect, to keep the exercise democratic.
- **Discuss and negotiate placement** after the initial plot; consensus comes
  from the conversation, not from the dots.
- **Split criteria across several matrices** when more than two matter, keeping
  the best outcome consistently in the same corner of every matrix so they can be
  compared at a glance.

### Prioritizing solution ideas in a design exercise

[[2018-02-12_solving-design-exercises_13-step-5-prioritise-and-choose-an-idea]]
makes prioritization step 5 of a seven-step framework for solving a design
exercise, between listing ideas and designing the chosen one. Ideas are weighed
on four dimensions: reach (how many customers), value for the customer (how
satisfied the solution leaves them), potential revenue (alignment with the
business), and implementation effort (development complexity). Impact is the
first three taken together, plotted against effort on a two-axis matrix, and the
target zone is quick wins — with a caveat specific to the interview: ideas
placed there must still be sophisticated enough to demonstrate design talent, a
criterion that comes from the exercise context rather than from the product one.
Whichever idea is chosen, the candidate is expected to explain why each solution
scores high or low on both axes, and especially why the chosen one does.

The source's warning concerns constraints that do not show on the surface of an
idea: a solution can meet the user need well and still score low on impact
because its reach is minimal (a smartwatch app only reaches smartwatch owners),
and a strong solution can be blocked by expertise the team does not have (a
physical product requiring industrial design).

Two worked examples show the matrix doing the deciding. In
[[2018-02-12_solving-design-exercises_22-3-5-improving-the-atm-experience]] it
selects converting ATMs into fulfillment-only points, with the requests
themselves moved to a mobile app. In
[[2018-02-12_solving-design-exercises_21-3-4-improving-primary-health-care]] it
weighs novelty and market potential against feasibility across four ideas: a
family-doctor marketplace and on-demand chat score low on impact because they
already exist, appointment-scheduling improvements touch only administrative
efficiency, and group appointments win as the novel, high-impact option because
one GP can educate several patients at once — a choice that also carries a
first-mover bet, that a white-label platform can capture the market before
competitors.

### Prioritizing inside the interface

[[2018-02-12_solving-design-exercises_19-3-2-a-self-publishing-platform-for-amazon]]
uses the word in a second sense: not ranking what the team builds, but ranking
what the user is shown. Its self-publishing product prioritizes anxiety
reduction for first-time authors and efficiency for recurring ones, and encodes
that ranking in the layout — the sidebar is split explicitly into "Essentials"
and "Tools" so that the required steps come first, cognitive load drops, and the
same sidebar doubles as a progress indicator answering "What's my progress?"
and "What's next?" at a glance.

### Prioritizing inside roadmapping

Prioritization is step 4 of the six-step roadmapping process: establish 4-8
prioritization factors mixing user-oriented and business-oriented criteria,
create a scoring scale, score each theme, then force rank to assign priorities
across time horizons [[2020-11-29_roadmapping-steps]]. The themes being ranked
come from step 3, clustering candidate problems by affinity diagramming, which
itself rests on inputs gathered in step 2 from prior artifacts and research.

[[2021-05-23_roadmapping-workshop]] runs the same two steps as a workshop and
adds the mechanics: the same 4-8 standardized, agreed-upon criteria, individual
rating, averaged scores, then group discussion of the results for alignment.
Duration is 2 to 4 hours depending on scope; where roadmapping is new or the
burden is high, split into a 1.5-hour preliminary workshop for goals and inputs
and a 2.5-hour primary workshop for themes and prioritization. The article's
governing claim is that a roadmap built alone will likely stay unused, which is
also the argument for prioritizing collectively rather than privately.
[[2020-11-29_roadmapping-steps]] then asks for a routine revisit cadence, monthly
at minimum, so priorities stay current.

### Using quantitative data to find the vital few

[[2021-10-17_pareto-principle]] applies the 80/20 rule as a prioritization
filter: inputs and outputs are rarely evenly distributed, so a small share of
categories usually carries most of the effect (20% of sites capturing 80% of
traffic, 20% of bugs causing 80% of crashes). Build a Pareto chart — bars for the
metric by category, a line for the cumulative percentage — to make the imbalance
immediately visible, and use it to cut through analytics overload and analysis
paralysis. The recommended sequence is: confirm organizational goals, the metrics
that measure them, and the user data aligned to those goals, then focus research
and design on the areas contributing significantly to those metrics. The article
adds an explicit counterweight: do not ignore the remaining 80%, since exclusive
focus on the top 20% risks stagnation and overoptimization of narrow metrics.

### Keeping users in the ranking

[[2022-10-09_personas-study-guide]] positions personas as one of the tools that
make prioritization user-centric: they let teams evaluate features systematically
by asking how each serves different user types and aligns with user goals, and
feature prioritization is listed among personas' main applications alongside
scenario mapping, participant recruitment and analytics segmentation. The
caveat is that personas only work when built with sufficient rigour, refreshed
periodically, and actively used — a persona created and then left unused does not
influence decisions.

### Deciding not to build

[[2023-12-01_smartwatch-app]] is the applied case for prioritization as
subtraction. Smartwatch apps are described as a dangerous opportunity for feature
creep, because a companion app is easier to justify than a new app, yet over 80%
of the 200 submitted interactions studied were with native apps such as messages
and timers. Value comes from context and from wearable-specific advantages
(proximity to the body, hands-free use, quick access), not from replicating
phone functionality; a smart-home unlock has durable value, a hotel app has none
after checkout. The prioritization conclusion is to favour high-value
microinteractions and effective notifications — the most common interaction type
— over a standalone app, and to do adequate discovery before committing
resources rather than building because it is technically possible.

### Prioritizing opportunities, not solutions

[[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]]
relocates prioritization one level up from everything above. Teams that
obsess over roadmaps and feature releases are, in its words, stuck in the
build trap; product strategy is made by deciding which outcomes to pursue,
which customers to serve and which opportunities to address, and most teams
skip those decisions and jump straight to solutions and roadmaps.
[[2021-05-18_continuous-discovery-habits_05-chapter-two-a-common-framework-for-continuous-discovery]]
names mapping the opportunity space and selecting which opportunities to
pursue as the two most critical steps of discovery for the same reason.

The procedure works down a well-structured opportunity solution tree. Compare
the top-level parent opportunities against each other first; once a priority
branch is identified, ignore the other branches and focus assessment on its
children. Each comparison uses four lenses, and the record insists on all four
to avoid blind spots:

- **Opportunity sizing** — which opportunity affects the most customers, most
  often (reach and frequency).
- **Market factors** — competitive position and external trends.
- **Company factors** — vision, mission, strategic fit, organizational
  strengths.
- **Customer factors** — how important the opportunity is to customers and how
  satisfied they are with current alternatives.

Choosing a target opportunity is framed as a reversible, two-way-door
decision: it commits the team only to exploring that opportunity over the
next few days or weeks, not to building it, which keeps the team willing to
course-correct when new information emerges.

### Patton: prioritize goals and users, then features

[[2014-09-05_user-story-mapping_19-14-using-discovery-to-build-shared-understanding]]
gives the same ordering as the "opportunities, not solutions" argument above,
from inside a different book and a different vocabulary. Patton's version of
the secret to prioritization is that it must start with specific business
goals — he deliberately avoids the term "business value" — flow from there to
specific users and their goals, and only then flow to specific features;
reversing that order, starting from a feature list, is what produces
over-scoped products. This is close to, but not identical to,
[[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]]'s
claim that teams should compare opportunities rather than rank features: both
books push prioritization up a level, away from the feature list, but Patton's
version keeps the sequence linear (goals, then users, then features) where
*Continuous Discovery Habits* frames it as relative comparison across sibling
opportunities in a tree.

Story-level prioritization has a mechanical precondition, in Patton's account:
it only works on a backlog small enough to reason about.
[[2014-09-05_user-story-mapping_22-17-stories-are-actually-like-asteroids]]
argues that a backlog filled with hundreds of small stories — the product of
breaking every story down too early, an anti-pattern Patton names after the
old Atari video game Asteroids — makes meaningful prioritization impossible, because
the connection between a small work item and the larger goal it serves gets
lost. His fix is to bundle related small stories back under a distilled header
card and prioritize the header, treating the original stories as supporting
detail; that is what turns the prioritization conversation back into something
a team can actually have.

### Scoring versus subjective comparison: a disagreement in the corpus

The sources split on whether prioritization should be mathematized, and the
page keeps both positions. [[2021-05-23_roadmapping-workshop]] argues that
standardized criteria and scoring scales yield objectivity and buy-in that
unstructured debate cannot, [[2020-11-29_roadmapping-steps]] scores each theme
and force-ranks, and [[2021-11-14_prioritization-methods]] offers RICE as a
formula for data-comfortable teams.
[[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]]
says the opposite for opportunities: do not score or stack-rank; compare and
contrast siblings, have healthy debate across the four dimensions, make the
best decision for this moment and leave room for doubt, embracing the
messiness and subjectivity of the comparison rather than reducing it to a
formula. The two camps agree on the collective part, that a ranking made alone
is not one the team owns, and differ on whether a number is what produces the
agreement.

[[2022-01-19_product-management-for-ux-people_13-chapter-10-roadmaps-and-how-to-say-no]] sits closer to the
second camp without abandoning the first: it keeps the scoring instruments on
the table (RICE, impact versus effort, T-shirt sizing) while denying that any
of them decides anything, which makes the frameworks a way of showing your
reasoning rather than a way of replacing it.

[[2018-02-12_solving-design-exercises_13-step-5-prioritise-and-choose-an-idea]]
sits on the scoring side, and in the space
[[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]]
rules out: it ranks solution ideas rather than opportunities, by composing
impact out of reach, customer value and revenue and plotting it against effort.
On the latter's account that is prioritizing in the solution space, which is the
wrong level to prioritize at. The setting differs as well: the design exercise
has one candidate producing the ranking and explaining it to one interviewer,
whereas [[2018-05-27_prioritization-matrices]] and
[[2021-05-23_roadmapping-workshop]] build the same instrument around group
voting and shared buy-in.

### Prioritizing among ideas: look for clear front-runners

Once a target opportunity is chosen, prioritization reappears among solution
ideas, and there the book's instrument is evidence rather than judgement.
[[2021-05-18_continuous-discovery-habits_13-chapter-ten-testing-assumptions-not-ideas]]
has teams test the assumptions shared across a set of ideas instead of testing
one idea at a time, because sequential single-idea testing invites
confirmation bias and escalation of commitment, then compare and contrast the
results to identify which ideas are most promising, looking for clear
front-runners rather than pursuing all ideas equally. The comparison is fair
only if success criteria are fixed upfront, with the number of participants
and the number who must exhibit the expected behaviour stated before the test
runs.

## Sources (17)

- [[2018-05-27_prioritization-matrices]] — The article provides a complete framework for using prioritization matrices including setup, voting, plotting, discussion, and documentation phases with guidance on adapting the approach to different team needs.
- [[2020-11-29_roadmapping-steps]] — using established criteria and scoring frameworks to rank roadmap themes from high to low priority, balancing user needs and business objectives.
- [[2021-05-23_roadmapping-workshop]] — Structured prioritization using standardized criteria and scoring scales ensures objectivity and buy-in compared to unstructured debate.
- [[2021-10-17_pareto-principle]] — Pareto charts and the principle help UX teams cut through analytics data and prioritize improvements where they'll have the most impact.
- [[2021-11-14_prioritization-methods]] — The article presents five distinct frameworks for making prioritization decisions based on defined criteria.
- [[2022-10-09_personas-study-guide]] — personas enable teams to evaluate features systematically by considering how they serve different user types and align with user goals and needs.
- [[2023-12-01_smartwatch-app]] — companies must prioritize high-value microinteractions over attempting to replicate the full functionality of phone apps.
- [[2021-05-18_continuous-discovery-habits_05-chapter-two-a-common-framework-for-continuous-discovery]] — Teams use the opportunity space to decide which customer needs to address, moving from "whether or not" decisions to "which is most important" comparisons.
- [[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]] — The chapter defines prioritization as strategic comparison of opportunities (not features) across four dimensions, using relative judgments between siblings rather than absolute scoring; it is a skillfully subjective, reversible decision.
- [[2021-05-18_continuous-discovery-habits_13-chapter-ten-testing-assumptions-not-ideas]] — Testing assumptions across sets of ideas requires comparing and contrasting results to identify which ideas are most promising; the chapter advocates for looking for "clear front runners" rather than pursuing all ideas equally.
- [[2018-02-12_solving-design-exercises_13-step-5-prioritise-and-choose-an-idea]] — Using a structured matrix with effort and impact dimensions to evaluate and rank solution concepts against business and user constraints.
- [[2018-02-12_solving-design-exercises_19-3-2-a-self-publishing-platform-for-amazon]] — The product prioritizes author anxiety reduction for new users and efficiency for experienced ones, with sidebar sections explicitly split into "Essentials" and "Tools" to reduce cognitive load and focus authors on required steps first.
- [[2018-02-12_solving-design-exercises_21-3-4-improving-primary-health-care]] — Using an impact/effort matrix, Dashinsky weighs novelty and market potential against feasibility, choosing group appointments over existing solutions with moderate impact or incremental improvements, and betting that a first-mover white-label platform can capture the market before competitors.
- [[2018-02-12_solving-design-exercises_22-3-5-improving-the-atm-experience]] — Using an impact/effort matrix to evaluate multiple design ideas and select the one with greatest potential benefit (in this case, converting ATMs to fulfillment-only points).
- [[2022-01-19_product-management-for-ux-people_13-chapter-10-roadmaps-and-how-to-say-no]] — Methods for weighing ideas against effort and impact, including impact-vs.-effort matrices, Eisenhower matrix, and RICE framework; frameworks help communicate decisions but cannot eliminate the need for human judgment.
- [[2014-09-05_user-story-mapping_19-14-using-discovery-to-build-shared-understanding]] — Patton articulates the principle that prioritization starts with specific business goals (not the term "business value"), flows to specific users and their goals, and only then flows to specific features; reversing this order leads to over-scoped products.
- [[2014-09-05_user-story-mapping_22-17-stories-are-actually-like-asteroids]] — When a backlog is filled with hundreds of small stories, meaningful prioritization is impossible. Bundling stories and reassembling broken rocks makes prioritization conversations feasible and preserves the connection between small work items and larger goals.
