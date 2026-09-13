---
type: concept
name: Assumption Testing
created: 2026-09-03
updated: 2026-09-11
status: developed
---

# Assumption Testing

## Definition

Assumption testing is the practice of breaking an idea into the beliefs it
depends on and testing those beliefs, rather than building the idea and seeing
what happens. Teresa Torres frames it as the counter to testing one idea at a
time: doing that invites confirmation bias and escalation of commitment,
because a team notices the confirming evidence and misses the disconfirming
[[2021-05-18_continuous-discovery-habits_13-chapter-ten-testing-assumptions-not-ideas]].
Testing assumptions shared across several ideas instead lets a team compare
ideas and pick clear front-runners. The tests are quick and small by design:
teams competent in modern discovery techniques run on the order of 10-20
iterations a week, validating or refuting the beliefs embedded in each idea
rather than building full prototypes
[[2021-05-18_continuous-discovery-habits_12-chapter-nine-identifying-hidden-assumptions]].

The standard of proof is deliberately low. Torres is explicit that "our goal as
a product team is not to seek truth but to mitigate risk" — the burden of truth
is too much
[[2021-05-18_continuous-discovery-habits_13-chapter-ten-testing-assumptions-not-ideas]].

Christian Crumlish arrives at the same practice from the product manager's side
and calls it experimentation as a way of life rather than a specialised
activity: product work is a series of testable bets, and the core discipline is
developing crisp, testable hypotheses about why data is behaving a certain way,
then designing experiments to validate or disprove them
[[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]].
A hypothesis, in his definition, explains why something is the way it is, is
grounded in observation (often of anomalous data), and can be validated or
disproven. He is deliberately reassuring about the vocabulary: generating
hypotheses is "just a fancy way of coming up with theories and ideas you can
test out," and any design exploration or research script already was one
[[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]].

## Practice

### Surface the assumptions first, then prioritise them

Before anything can be tested it has to be named. Torres lists five categories
of assumption — desirability, viability, feasibility, usability, ethical — and
warns that teams have blind spots in some of them, particularly the ethical
ones, so several surfacing methods should be used together: story mapping each
step a user must take, pre-mortems, walking the opportunity solution tree
backward, and asking directly what harm the solution could cause
[[2021-05-18_continuous-discovery-habits_12-chapter-nine-identifying-hidden-assumptions]].
[[Assumption Mapping]] then sorts them by importance and evidence strength, and
the "leap of faith" assumptions (high importance, weak evidence) are tested
first.

Do not test everything. Most assumptions will be harmless if the discovery work
was solid; the target is the two or three riskiest assumptions per idea, not
every one of dozens
[[2021-05-18_continuous-discovery-habits_12-chapter-nine-identifying-hidden-assumptions]].

Crumlish prioritises experiments on a rubric weighing potential reach,
potential impact, engineering effort, and confidence in the hypothesis, with
highest priority going to the riskiest bets rather than the easiest or most
visible ones, and he recommends keeping a backlog of hypotheses and proposed
experiments in a shared tracking tool such as Airtable
[[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]].
Both authors therefore prioritise by risk, and Crumlish's practical example is
Heather Cornell at 7 Cups, who hypothesised that "new visitors don't know what
a Listener is" and ran a button-label test that improved performance.

### Designing a test that actually tests behaviour

A strong assumption test simulates the specific moment when a customer would
behave according to the assumption, and success is evaluated on how people
actually behave in the simulation, not on what they say they would do
[[2021-05-18_continuous-discovery-habits_13-chapter-ten-testing-assumptions-not-ideas]].
Success criteria are defined upfront — how many participants, and how many must
exhibit the desired behaviour ("at least 3 out of 10") — which aligns the team
on what the result means before the result exists, and guards against
confirmation bias.

Start small: fast tests with 5-10 participants completed in a day or two give
early signals, and only signals that warrant it justify a larger experiment.
Small samples produce false positives (test passes, assumption faulty) and false
negatives (test fails, assumption valid); Torres treats both as acceptable
because teams run many tests and can triangulate several research methods on
one assumption
[[2021-05-18_continuous-discovery-habits_13-chapter-ten-testing-assumptions-not-ideas]].
The methods she names as fast and reliable enough are unmoderated user testing,
one-question surveys, and data-mining.

### Twelve named alternatives when an A/B test is not the tool

Crumlish covers [[A-B Testing]] in detail but insists its blind spots make it
one instrument among many: it shows what happened, not why; externalities such
as seasonal changes, marketing campaigns or industry events can skew results
unnoticed; and overreliance leads to "polishing a local maximum," optimising a
small area while missing much larger opportunities
[[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]].
There is also a context where it is simply unavailable: according to Clement
Kao, enterprise and B2B customers cannot be shown different workflows, because
the user base is small, named customers in high-touch relationships, and
training separate cohorts on different interfaces is disruptive.

The twelve methods the chapter catalogues beyond A/B tests
[[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]]:

- **Concierge** — a human behind the scenes doing what the product would do.
- **Wizard of Oz** — a human disguised as automation.
- **Pretotypes** — a low-fidelity proof of concept (see
  [[Minimum Viable Product]]).
- **Smokescreen** — an ad for a product that does not exist.
- **[[Fake Door]]** — a phantom feature in the interface.
- **Broken Glass** — a deliberately difficult feature.
- **Dogfooding** — internal testing.
- **Partial Rollouts** — staged release.
- **Beta Programs**.
- **Holdover** — keeping the old version for a cohort. One practitioner quoted
  in the chapter values it for looking at performance over time: many teams
  assume an initial test result equals the same result later, whereas features
  used initially because they were new dropped back after 90 days.
- **Sales Experiments** — testing pitch language.
- **Process Experiments** — varying team workflows.

### Measuring what the test claims to measure

Instrumentation should follow the tests, not precede them: Torres warns against
waterfall instrumentation projects and recommends measuring what the current
assumption tests need, then iterating toward outcome measurement
[[2021-05-18_continuous-discovery-habits_14-chapter-eleven-measuring-impact]].
Success criteria for an assumption are usually about whether customers take a
specific action (viewing or applying for jobs, in the AfterCollege case), and
those leading indicators are useful for testing — but a team must also track the
metric tied to the business outcome, or it will celebrate a successful
intermediate step that never produced hires. Testing with live prototypes in
production is a natural progression of this work: discovery feeds delivery and
delivery feeds discovery.

Crumlish's equivalent discipline is to record both the numerical impact and the
qualitative insight about what the result means for the next hypothesis, and to
treat a loss as informative: it teaches something about the hypothesis or about
the test itself, and both build the team's product intelligence over time. A
win should be locked in and followed up with further tests to compound it
[[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]].

### The payoff is what you decide not to build

Quick tests are what let a team pivot without overinvesting. Torres's case
studies make the point concretely: Simply Business found that customers
complained about late payments but did not want third-party help, and killing
that opportunity quickly after testing saved weeks of development; the team
killed it on Tuesday, chose a new opportunity on Wednesday, and used
already-scheduled Thursday interviews to learn about it
[[2021-05-18_continuous-discovery-habits_15-chapter-twelve-managing-the-cycles]].
Her summary of the value is direct: "the fruit of discovery work is often the
time we save when we decide not to build something." Discovery in this account
is non-linear — surprises send teams back to reprioritise opportunities, refocus
on other segments, or break an opportunity into sub-opportunities — and
assumption tests are what produce those surprises early enough to be cheap.

### Test through incremental release, not only through simulation

Patton illustrates the same discipline from the product owner's side,
narrating Eric, a product owner at Liquidnet, working through a real launch.
Before writing a backlog, Eric frames the opportunity with leadership and
then validates directly with customers that the problem he intends to solve
actually exists, rather than assuming his initial idea is correct
[[2014-09-05_user-story-mapping_08-3-plan-to-learn-faster]]. He sketches and
prototypes solutions without building production software, because surprises
are cheap to have at this stage, and releases what Patton calls a "minimum
viable product experiment" (MVPe), deliberately less than viable, to a small
group of development partners who care enough to tolerate the roughness,
growing and improving it with their feedback until they start recommending
it to others [[2014-09-05_user-story-mapping_08-3-plan-to-learn-faster]].
Patton's stated principle is to measure what people actually do with the
release rather than what they say they would do, since people may claim to
like something they never use
[[2014-09-05_user-story-mapping_08-3-plan-to-learn-faster]] — the same
behavioural standard Torres sets for a fast test.

Patton also locates assumption testing earlier, at the discovery stage that
precedes any of this: teams dig into assumptions about who the customers
are, how they meet their needs today, how a proposed solution would change
their world, and what the solution should look like, and test those
assumptions with prototypes, customer interviews and technical spikes
[[2014-09-05_user-story-mapping_16-11-rock-breaking]]. This maps onto the
same categories Torres names — who has the problem, whether a solution would
change things for the better, what shape it should take — without
formalising them into the desirability/viability/feasibility/usability/ethical
checklist that [[Assumption Mapping]] uses to sort them.

## Sources (7)

- [[2021-05-18_continuous-discovery-habits_12-chapter-nine-identifying-hidden-assumptions]] — The practice of quickly testing critical assumptions through iterations rather than building full prototypes; teams test dozens of assumptions per week by systematically validating or refuting the beliefs embedded in each idea.
- [[2021-05-18_continuous-discovery-habits_13-chapter-ten-testing-assumptions-not-ideas]] — The chapter teaches teams to break ideas into testable assumptions and design small, fast experiments to collect evidence about each assumption; this approach enables rapid iteration and reduces the risk of investing time in flawed ideas.
- [[2021-05-18_continuous-discovery-habits_14-chapter-eleven-measuring-impact]] — measuring success criteria for assumptions about whether customers will take specific actions (e.g., view or apply for jobs).
- [[2021-05-18_continuous-discovery-habits_15-chapter-twelve-managing-the-cycles]] — the quick tests that validate (or invalidate) which opportunities customers actually need solved, enabling teams to pivot rapidly without overinvesting.
- [[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]] — formulating testable hypotheses about product decisions (what to build, how to prioritize fixes, how to optimize features) and designing experiments to validate or disprove them.
- [[2014-09-05_user-story-mapping_08-3-plan-to-learn-faster]] — The strategy validates assumptions about customer problems, solution ideas, and what makes a product viable by releasing incrementally to development partners and measuring results.
- [[2014-09-05_user-story-mapping_16-11-rock-breaking]] — During discovery, teams dig into assumptions about who the customers are, how they meet needs today, how a solution would change their world, and what the solution should look like. Prototypes, customer interviews, and technical spikes all serve to test and validate these assumptions.
