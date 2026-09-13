---
type: concept
name: Decision Making
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Choice Overload"
  - "Compensatory Decision Making"
  - "Decision-Making"
  - "Democratic Decision-Making"
  - "Team Decision-Making"
---

# Decision Making

## Definition

Decision making is the process of choosing among alternatives, and the sources
treat it on two fronts that turn out to obey the same laws. On one side there
is the **user** deciding — which product to buy, which show to watch, which
option to trust — a process that is not purely logical but shaped by cognitive
biases, by how the choice is framed, and by how many alternatives are on the
table [[2016-06-19_prospect-theory]],
[[2020-10-25_compensatory-noncompensatory-decisions]]. On the other side there
is the **practitioner and the team** deciding — whether to redesign, what to
prioritize, which trade-off to accept — a process just as vulnerable to
framing, narrative and conformity, and one that consequently needs deliberate
structure to stay honest [[2017-12-19_decision-framing-cognitive-bias-ux-pros]],
[[2017-02-19_narrative-biases]], [[2023-01-15_groupthink-in-ux]].

The practical consequence running through the corpus is that decisions can be
designed for. On the product side, interfaces should support the strategy the
user is actually running at that moment rather than dumping every option at
once [[2020-10-25_compensatory-noncompensatory-decisions]]. On the team side,
mechanisms — explicit design principles, structured voting, named deciders,
reflective journaling — substitute for the assumption that people will reason
well unaided [[2020-08-02_design-principles]], [[2019-07-07_dot-voting]],
[[2022-08-14_workshop-participant-lists]], [[2022-05-01_ink-thinking]].
*Continuous Discovery Habits* adds a third kind of structure: a visual one. The
opportunity solution tree lays out the outcome, the opportunities, the
solutions and the assumption tests so that a team stops making "whether or not"
decisions about a single idea and starts comparing and contrasting options,
which it presents as the way past false certainty
[[2021-05-18_continuous-discovery-habits_05-chapter-two-a-common-framework-for-continuous-discovery]].
In that framing, structured discovery habits ground choices in regular customer
research rather than intuition, and that grounding is what gives a team
confidence in its own decisions
[[2021-05-18_continuous-discovery-habits_01-foreword-chris-mercuri]]. One source
applies the same instinct to a third kind of decision, the practitioner choosing
their own career path, and reaches for structure there too rather than trusting
the gut [[2023-09-05_path-to-senior-product-designer_04-2-setting-career-goals]].

## Practice

### How users choose among alternatives

The dominant variable is the **number of options**
[[2020-10-25_compensatory-noncompensatory-decisions]]:

- **Noncompensatory strategy** — with many alternatives, people quickly
  eliminate anything failing a nonnegotiable criterion instead of comparing
  everything. Support it with relevant filters and faceted navigation on
  listing pages.
- **Compensatory strategy** — with roughly 5–7 remaining alternatives, people
  compare attributes in depth, letting positives outweigh negatives. Support it
  with side-by-side comparison.
- **The two run in sequence**: filter down from many, then compare the few. An
  interface should support both stages of the same decision.

[[2024-02-09_comparison-tables]] details the compensatory half: use comparison
tables when users weigh multiple criteria across a small set (typically 3–7),
limit comparisons to five items or fewer for cognitive load, use static tables
for five items or fewer and dynamic ones for larger catalogues. Its strongest
warning is that consistency beats design — incomplete or missing metadata
across rows makes a table useless however good it looks. Beyond that: keep text
short and scannable rather than in full sentences, use symbols and
color-coding, add sticky column headers when scrolling is required, include
only attributes users care about, and define unfamiliar terms in context or via
tooltips.

Recommendations are the third mechanism, acting as curation against the
too-many-options problem on sites like YouTube, Netflix and e-commerce
platforms [[2018-09-30_recommendation-expectations]]. Users appreciate them for
narrowing large inventories, accept behavioural tracking as the price, and
expect explicit actions (purchases, saved items) to weigh more than passive
browsing, since a click does not necessarily signal genuine interest. They read
perceived popularity as a cue for whether something is really personalised, and
they simply ignore bad recommendations rather than investing effort in
correcting them.

[[2025-09-12_physical-discs-streaming-experience]] supplies the counterweight:
a curated collection of 200 personal favourites gave more satisfaction and
discoverability than algorithmic suggestions drawn from 100,000+ titles. It
argues quality of choice over quantity of choice — and, more broadly, that
convenience that isn't reliable isn't convenient.

### The biases that shape user choices

[[2016-06-19_prospect-theory]] summarises Kahneman and Tversky's account of how
people choose between prospects and misestimate their likelihood:

- **Loss aversion** — losses loom larger than gains; people overweight small
  probabilities to guard against loss and often prefer a small certain loss to
  a possible large one.
- **Certainty bias** — certain options are overweighted; people are risk averse
  for gains and will take a small sure reward over a chance at more.
- **Isolation effect** — when comparing, people discard what the options share
  and focus only on differentiators, which makes choices inconsistent depending
  on presentation.
- **Framing** — presenting information as a gain or a loss shifts the decision;
  negative framing primes people to think about what they might lose.

The same article extends this to experience itself: users react far more
strongly to moments of loss (frustration, confusion) than to things working,
and remember small stumbling blocks much longer than positive moments.

### Where the decision-relevant information comes from

[[2020-04-05_passive-information-acquisition]] complicates the picture of the
deliberate seeker: passive acquisition — accidental discovery while browsing,
or information pushed by email, text or notification — grew from 4% to 14% of
the critical information leading to significant decisions over 22 years. The
design implications it draws: passively acquired information arrives without
context, so users want links to related content, comparison tables and expanded
information to act on it; credibility is hard to assess in that mode, so
transparent sourcing and clear citations matter and sensationalism hurts;
notification volume is overwhelming, so customization is needed; and paid
content accounts for 37% of critical passive acquisitions versus 1% of active
ones, since browsing users are less goal-driven.

### Anchoring team decisions: principles

[[2020-08-02_design-principles]] proposes product-specific design principles as
the device for resolving recurring trade-offs (minimalism vs discoverability,
power users vs casual users) rather than re-debating them:

- They are value statements about what the product should deliver, not
  directions for UI elements.
- A good principle **takes a stand** on which value wins when two conflict, or
  names the contexts where one dominates; ambiguity re-opens the debate.
- It must inspire empathy by saying why the value matters to users, not just
  what it is.
- Keep them concise and memorable, 5–8 maximum — ten or more get forgotten.
- Use them to justify: not "because I say so" but "because principle #3 tips
  the balance". They guide justification without eliminating judgment.

### Structuring group decisions

Groups default badly. [[2023-01-15_groupthink-in-ux]] describes groupthink as
cohesive teams prioritising consensus over consideration of alternatives, with
symptoms including collective rationalization of warnings, illusion of
unanimity produced by silence, self-censorship, and direct pressure on
dissenters. Its countermeasures are concrete: communicate group norms that
value all ideas and explicitly encourage disagreement; have people ideate solo
before sharing; use diverge-converge and dot voting so the facilitator does not
decide; recruit diverse focus-group participants and warm them up; test design
trends with your own users instead of assuming a competitor's adoption
validates them; and in virtual settings rotate hosts and use anonymous
follow-ups, because remote work exacerbates the effect.

**Dot voting** is the recurring instrument [[2019-07-07_dot-voting]]:
participants get a fixed number of tokens, vote quietly without lobbying, and
the distribution becomes a visible heat map. It gives everyone equal voice,
prevents the HIPPO (highest-paid person's opinion) effect, converges quickly,
and leaves a shared artefact. Its documented adaptations counter its own
weaknesses: give voters research time beforehand, vote digitally or anonymously
to hide influence, dictate voting order (junior first), rank dots for weighted
votes, and color-code dots by criterion. Ties are broken by re-voting on the
tied candidates only. [[2016-09-18_design-thinking-team-building]] frames the
same practice culturally: anonymous idea cards and dot-voting keep hierarchy
from dominating, weight ideas equally, and build the psychological safety that
makes people participate at all.
[[2021-05-18_continuous-discovery-habits_11-chapter-eight-supercharged-ideation]]
uses the same instrument at a precise point in discovery: after individuals
have ideated alone and the team has filtered out ideas that do not address the
target opportunity, each person gets three votes to select three finalists for
testing, so that three diverse ideas compete rather than one champion emerging,
and every team member is excited about at least one of them. The record's
reasoning is that individuals generate ideas better than groups, but groups
evaluate better.

There is a real tension in the corpus here.
[[2016-09-18_design-thinking-team-building]] describes decisions made by
majority vote rather than hierarchy as a trust-building good in itself, while
[[2022-08-14_workshop-participant-lists]] insists a workshop include a
**designated decider** with veto power, on the grounds that one person often
does hold overwhelming authority over the outcome and excluding them to avoid
conflict only gets the work vetoed later. The same source adds the composition
rules that make a group decision durable: 6–12 participants, diversity across
departments, domain knowledge (experts plus novices who ask the naive question)
and seniority, a facilitator who facilitates rather than participates, and
always a user perspective — real users, or proxies such as customer-support
reps who have more direct user contact than managers.

### Deciding with stakeholders: show the reasoning, not the conclusion

[[2021-05-18_continuous-discovery-habits_16-chapter-thirteen-show-your-work]]
takes the HiPPO problem out of the workshop room and into stakeholder
management. Its Airship case has a team prototype a better journey builder
only to meet sales resistance, and its diagnosis is that presenting
conclusions, roadmaps and backlogs, invites stakeholders to reply with their
own opinions, an opinion battle a team cannot win. Showing the decision tree
instead (the outcome, how the opportunity space was mapped, which opportunities
were prioritized and why, which solutions were considered) invites them to
evaluate the thinking and turns the exchange into co-creation. The record's
mechanics: start at the top of the tree by confirming the desired outcome and
only mention solutions last; tailor the depth to the person, week-over-week
detail for a boss, the outcome, two or three opportunities, the chosen one and
one or two tests for a CEO; treat a stakeholder's suggestion as one more idea
to evaluate through story mapping and assumption listing rather than shooting
it down; and when asked to deviate from the process, argue the decision at
hand rather than the philosophy. Sharing along the way, week to week or month
to month, is what prevents surprises at the end.

### Deciding in the opportunity space: compare-and-contrast, two-way doors

Where the sources above structure a single decision, *Continuous Discovery
Habits* structures the sequence of decisions a product trio makes on the way
to an outcome. [[2021-05-18_continuous-discovery-habits_05-chapter-two-a-common-framework-for-continuous-discovery]]
describes reaching a desired outcome as an ill-structured problem with many
possible solutions, so how the team frames the problem determines the quality
of the solutions it considers; the two most critical steps are mapping the
opportunity space and selecting which opportunities to pursue, and many teams
skip both and jump to solutions. The opportunity solution tree is its device
for keeping those choices visible, so the team compares options rather than
deciding "whether or not" on one, and it credits the tree with helping teams
overcome narrow framing, confirmation bias, emotional attachment to ideas and
overconfidence, the same villains
[[2017-12-19_decision-framing-cognitive-bias-ux-pros]] and
[[2017-02-19_narrative-biases]] describe from the research side.

The first decision in that sequence is the outcome itself.
[[2021-05-18_continuous-discovery-habits_06-chapter-three-focusing-on-outcomes-over-outputs]]
frames it as a strategic choice about which customer needs matter most to the
business, negotiated two ways: product leaders bring business context and
strategic priorities, the trio brings customer knowledge and realistic impact
estimates, and both inputs are needed. It adds that when the outcome is new
and complex, teams should start with learning goals (discover which strategies
work) before committing to performance targets, and it lists the anti-patterns
of pursuing too many outcomes at once, ping-ponging between outcomes quarter
to quarter, assigning outcomes to individuals rather than teams, and confusing
outputs with outcomes.

The tree then changes the shape of each subsequent decision.
[[2021-05-18_continuous-discovery-habits_09-chapter-six-mapping-the-opportunity-space]]
argues that a flat backlog of opportunities hides dependencies and overlaps,
whereas parent-child and sibling relationships let a team compare sibling
opportunities at one level of the tree instead of comparing everything at
once, which it presents as the way to avoid analysis paralysis and to solve
smaller problems in sequence.
[[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]]
adds the mindset: choosing a target opportunity is a reversible, two-way-door
decision that commits the team only to exploring it for the next days or
weeks, not to building anything, so the team stays willing to course-correct
as new evidence emerges. It explicitly prefers subjective, data-informed
comparison with healthy debate across dimensions, leaving room for doubt, over
scoring and stack-ranking; the detail lives on [[Prioritization]].

### Go/no-go decisions from assumption tests

[[2021-05-18_continuous-discovery-habits_13-chapter-ten-testing-assumptions-not-ideas]]
supplies the evidence side of the same loop. Testing one idea at a time invites
confirmation bias and escalation of commitment, so the record has teams test
assumptions shared across several ideas and use the results to compare them
and select clear front-runners. The decision rule is set before the data
arrives: specify how many participants will be tested and how many must show
the expected behaviour (its example is at least 3 out of 10), so the team
agrees in advance on what the result means and no individual interprets it
after the fact. Tests start small, 5 to 10 participants in a day or two, and
only grow if the early signal warrants it; small samples produce false
positives and false negatives, which the record calls acceptable because teams
run multiple tests and can triangulate methods on one assumption, and because
the goal is to mitigate risk, not to establish scientific truth. This
pre-registration of the expected result is the same discipline
[[2022-05-01_ink-thinking]] and [[2026-07-24_product-sense-definition]]
recommend for the individual practitioner, applied to a team's go/no-go call.

### Auditing your own reasoning

Individual practitioners are biased in ways they can check for.

- **Framing.** [[2017-12-19_decision-framing-cognitive-bias-ux-pros]] showed
  that practitioners reading "4 out of 20 users could not find the search
  function" were 31% more likely to support a redesign than those reading the
  identical data as "16 out of 20 users found" it. Its remedies: resist snap
  judgments, gather context before deciding, and deliberately restate the
  decision from reversed perspectives (failure vs success, percentages vs
  actual numbers). It also warns about the shape of the frame itself —
  incomplete frames that consider only existing users miss expansion
  opportunities, and overly specific frames ("should we implement feature X")
  hide alternatives that a broader framing would surface.
- **Narrative.** [[2017-02-19_narrative-biases]] shows teams preferring causal
  stories to randomness: a high exit rate on a low-traffic page reads as a
  design flaw when small samples routinely produce extreme numbers, and 41% of
  surveyed UX practitioners fell for base-rate neglect. Its fixes: ground
  explicit stories in actual research from multiple data sources (even a quick
  survey checks a basic assumption), and make implicit stories explicit through
  formal problem definition so the assumption can be challenged.
- **Hindsight.** [[2022-05-01_ink-thinking]] proposes reflective journaling
  against the tendency to overestimate one's own predictive accuracy after the
  fact: a small thin ruled journal, 5–10 minutes scheduled weekly, two steps —
  record the decision and what you expect in 2–3 sentences, then, once the
  outcome is known, record what actually happened and write advice to yourself.
  It cites research where journaling participants answered 23% more math
  puzzles correctly than participants who simply practised more.

[[2026-07-24_product-sense-definition]] generalises this into a definition of
product sense: recognising when a current problem matches past successes or
failures and reliably estimating how similar solutions will perform. That
depends on closing the full experimentation loop — face the problem, choose a
solution, implement, measure, reflect — and it warns that too many builders
never close it, taking requests and moving on. Its prescriptions overlap ink
thinking: document hypotheses before looking at results, be specific about the
outcomes expected, measure real outcomes rather than output quality, and stay
long enough on a project to see the results. It adds a calibration rule: strong
product sense includes knowing when a pattern does *not* apply — high-validity
situations allow accurate pattern matching, low-validity ones demand more
evidence, and wicked situations that feel familiar but whose solutions do not
fit are the most dangerous.

### Deciding about your own career

[[2023-09-05_path-to-senior-product-designer_04-2-setting-career-goals]] applies
the same "structure beats intuition" instinct to a decision the rest of the corpus
does not cover: which career path to take. It opens on a principle it takes from
Stephen Covey, "begin with the end in mind", and on his warning that
"effectiveness does not depend solely on how much effort we expend, but on
whether or not the effort we expend is in the right jungle". Its instruments:

- **Score the options against your own values**, weighted by how much each value
  matters to you, rather than ranking the options directly. A related exercise
  writes personal values on one sheet and the outcomes of a potential change on
  another, then compares them. The chapter reports that the record of that
  exercise kept its use after the decision, when a later disruption made the
  author question the choice and revisiting the results showed the outcomes still
  aligned.
- **Visualise the outcome and then test it.** Imagine yourself a few years into
  the chosen path and picture the day: who you interact with, what work you do,
  where you are, how you feel. The chapter's instruction is to validate those
  assumptions against reality rather than stopping at the image.
- **Score competing job offers on stated criteria** such as getting things done,
  quality of life, growth, compensation, satisfying work and future success, with
  sub-criteria beneath them.
- **Use a coin flip as a catalyst, not a decider.** The chapter's use of it is
  psychological: the emotional response when the coin lands, relief or doubt, is
  what reveals the true preference.
- **The ABZ framework.** Know where you are (A) and where you want to be (Z), then
  work only on the immediate next step: "You don't have to know every single step
  between A and Z; you only need to focus on B, the next step." Its purpose is to
  keep a long-horizon decision from becoming paralysing (see
  [[Career Growth Plan]]).

## Sources (26)

- [[2016-06-19_prospect-theory]] — Understanding prospect theory helps designers anticipate how users will choose between options and frame choices to align with user goals.
- [[2016-09-18_design-thinking-team-building]] — Emphasizes anonymous voting, equal weighting of ideas, and transparent decision-making as building blocks for trust-based culture and equitable participation.
- [[2017-02-19_narrative-biases]] — the article addresses how narrative bias affects team choices about design and resource allocation.
- [[2017-12-19_decision-framing-cognitive-bias-ux-pros]] — The process of choosing among alternatives; vulnerable to context and framing effects; requires explicit consideration of multiple perspectives to avoid bias.
- [[2018-09-30_recommendation-expectations]] — how recommendations serve as a curation mechanism to help users navigate the problem of too many options available on sites like YouTube, Netflix, and e-commerce platforms.
- [[2019-07-07_dot-voting]] — dot voting supports group consensus by making voting visible and equal; adaptations like digital voting, research time, and voting order further improve decision quality and reduce groupthink.
- [[2020-04-05_passive-information-acquisition]] — shows that important decisions increasingly rely on accidentally discovered information acquired through browsing or notifications rather than deliberate search.
- [[2020-08-02_design-principles]] — using principles to anchor and justify design decisions across teams and over time.
- [[2020-10-25_compensatory-noncompensatory-decisions]] — how users choose among alternatives using different strategies based on the number of options available and the complexity of the decision.
- [[2022-05-01_ink-thinking]] — improving judgment and intuition through deliberate reflection on past decisions and outcomes.
- [[2022-08-14_workshop-participant-lists]] — Workshops should include a designated decider to provide clear authority for decisions; this role acknowledges the reality that one person often has overwhelming power over project outcomes.
- [[2023-01-15_groupthink-in-ux]] — Groupthink leads to suboptimal decisions; structured approaches (dot voting, diverge-converge) and explicit invitation for dissent improve decision quality.
- [[2024-02-09_comparison-tables]] — a cognitive process where users weigh multiple criteria; comparison tables directly support this decision strategy.
- [[2025-09-12_physical-discs-streaming-experience]] — Contrasts the paralysis of too many algorithmic suggestions with the satisfaction of intentionally curated collections, showing quality over quantity in media consumption.
- [[2026-07-24_product-sense-definition]] — improves when builders document hypotheses before seeing results and reflect on how their past experiences apply to current situations.
- [[2021-05-18_continuous-discovery-habits_01-foreword-chris-mercuri]] — Structured discovery habits gave the team confidence in their decision-making by grounding choices in customer research rather than intuition.
- [[2021-05-18_continuous-discovery-habits_05-chapter-two-a-common-framework-for-continuous-discovery]] — The OST helps teams overcome decision-making villains like narrow framing, confirmation bias, emotional attachment to ideas, and overconfidence.
- [[2021-05-18_continuous-discovery-habits_06-chapter-three-focusing-on-outcomes-over-outputs]] — Setting outcomes requires making strategic decisions about which customer needs matter most to the business, and these decisions should reflect both business context and team capacity.
- [[2021-05-18_continuous-discovery-habits_09-chapter-six-mapping-the-opportunity-space]] — The tree structure fundamentally changes how teams make strategic decisions; instead of comparing many opportunities at once, teams now compare sibling opportunities at each level, using the tree to optimize decisions and avoid analysis paralysis.
- [[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]] — Teams make strategic decisions in the opportunity space by comparing sets of opportunities at each level of the tree, using a two-way-door mindset that allows course-correction as new evidence emerges during discovery.
- [[2021-05-18_continuous-discovery-habits_11-chapter-eight-supercharged-ideation]] — Dot-voting is the evaluation method: a lightweight group decision that uses experience to assess ideas against the target opportunity, setting up a compare-and-contrast mindset where three diverse ideas compete, not one champion emerges.
- [[2021-05-18_continuous-discovery-habits_13-chapter-ten-testing-assumptions-not-ideas]] — The chapter emphasizes how assumption tests provide data that teams use to make go/no-go decisions about ideas and opportunities; success criteria defined upfront ensure the team agrees on what the results mean and avoids individual bias in interpretation.
- [[2021-05-18_continuous-discovery-habits_16-chapter-thirteen-show-your-work]] — showing the decision tree (outcome, opportunities, prioritization, solutions considered) rather than the final decision creates a collaborative evaluation process.
- [[2024-01-23_laws-of-ux_06-4-hicks-law]] — the cognitive process users undertake when selecting from available options; more options increase time and mental strain.
- [[2023-09-05_path-to-senior-product-designer_04-2-setting-career-goals]] — Techniques the chapter borrows and presents as aids, none to be relied on alone: scoring values against options, comparing life outcomes, a coin flip used as a catalyst rather than a decider, and the ABZ framework for progressive goal-setting.
- [[2022-01-19_product-management-for-ux-people_06-chapter-3-ux-skills-that-carry-over]] — The chapter centers on PM as a role of constant decision-making at high velocity, with the understanding that no PM gets all decisions right and that not deciding is itself a decision with consequences.
