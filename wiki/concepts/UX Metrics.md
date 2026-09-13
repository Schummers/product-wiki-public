---
type: concept
name: UX Metrics
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Measurement"
  - "Measurement Strategy"
  - "UX Measurement"
  - "Usability Metrics"
  - "User Experience Metrics"
---

# UX Metrics

## Definition

UX metrics are numerical representations of aspects of the user experience:
behavioural measures such as task success, time on task and errors, perceptual
measures such as satisfaction and perceived usability, and business measures
such as conversion, revenue and retention [[2021-08-29_quantitative-research-study-guide]].
They exist to answer "how much" questions — how many users hit a problem, how
widespread or severe it is, whether a design change moved anything — where
qualitative research answers why the problem exists
[[2021-08-29_quantitative-research-study-guide]], [[2018-09-02_quant-research-practice]].
Metrics tell you what changed, never how to improve it, which is why the
sources treat them as one half of a pair rather than a substitute for
qualitative work [[2023-01-29_castle-framework]]. They are also something a designer
proposes alongside a solution, not only something collected afterwards: the
final step of Dashinsky's design-exercise framework is to answer how you would
know the solution succeeded
[[2018-02-12_solving-design-exercises_15-step-7-measure-success-how]].

A single number carries no meaning on its own. It becomes a metric only against
a reference point — an earlier version, a competitor, an industry standard, or
a goal set by stakeholders [[2020-05-03_benchmarking-ux]] — and only when it is
tied to a goal someone would act on
[[2017-05-14_ux-goals-analytics]], [[2019-10-13_vanity-metrics]]. The recurring
failure mode across the corpus is measuring what is easy rather than what
matters: ever-growing counts, inherited defaults, dozens of collected data
points nobody uses [[2019-10-13_vanity-metrics]], [[2025-10-03_ux-metrics-goals]],
[[2026-06-26_establishing-baselines]].

## Practice

### Start from goals, not from what the tool reports

Tracking metrics for their own sake wastes time: decide first what you want to
know and what you would do with the answer [[2017-05-14_ux-goals-analytics]].
The goal-down approach works from a high-level goal, down to the user
behaviours that signal the goal is being met, and only then to measurements of
those behaviours — asking "why?" repeatedly until you reach the root goal (video
plays matter only if they lead to form submissions, which matter only if they
drive sales) [[2017-05-14_ux-goals-analytics]]. Real goals are never "reduce
bounce rate" or "increase page views"; they describe experiences, and good
design is not about getting more clicks [[2017-05-14_ux-goals-analytics]].

The organisational version of the same move is a collaborative workshop (3-4
hours) that starts by naming where UX actually influences business outcomes —
revenue, retention, adoption, support costs — before any metric is selected,
with UX, product, analytics, support and leadership in the room
[[2025-10-03_ux-metrics-goals]]. Three traps recur: vanity metrics that look
good but yield no insight, silos where UX defines metrics without stakeholder
buy-in, and noise metrics nobody uses [[2025-10-03_ux-metrics-goals]].

### Selecting metrics

- **Test each candidate against the experience.** Ask: if this number improves,
  does that mean users have a better experience with the thing we changed? If
  answering needs several inferential steps, the metric is too indirect
  [[2026-06-26_establishing-baselines]].
- **Cover several dimensions, but few metrics.** Benchmarking guidance
  recommends defining the context (product, user group, tasks), identifying the
  5-10 top tasks, then picking 2-4 metrics spread across different aspects of
  the experience using Google's HEART framework — happiness, engagement,
  adoption, retention, task effectiveness [[2020-09-13_product-ux-benchmarks]].
  Pick metrics that will still matter years from now, since you will collect
  them repeatedly [[2020-09-13_product-ux-benchmarks]].
- **One source argues for a single metric.** For baselines, picking one
  well-chosen metric is more convincing than assembling a collection after the
  results are in, which invites cherry-picking and undermines trust
  [[2026-06-26_establishing-baselines]]. This sits in tension with the 2-4
  metric recommendation for benchmarking programmes
  [[2020-09-13_product-ux-benchmarks]] and with the multi-metric argument made
  about NPS [[2024-06-21_nps-ux]]; the sources differ on how many metrics a
  measurement effort should carry. The worked design exercises sit at the
  multi-metric end, carrying four to five per solution
  [[2018-02-12_solving-design-exercises_18-3-1-designing-a-kiosk-interface]],
  [[2018-02-12_solving-design-exercises_22-3-5-improving-the-atm-experience]].
- **Narrow to the strongest signals** rather than tracking every possible proxy
  [[2017-05-14_ux-goals-analytics]].
- **Skip what you cannot do well.** Bad numbers are worse than no numbers
  [[2020-09-13_product-ux-benchmarks]].

### Naming success metrics when proposing a solution

Measuring success is the seventh and last step of the design-exercise
framework: having presented the solution, say how you would know it worked
[[2018-02-12_solving-design-exercises_15-step-7-measure-success-how]]. In an
exercise the candidate proposes which KPIs matter without naming the threshold
numbers, since in real product work a product manager or data analyst makes the
final call on those; the book presents this as a deliberately narrower scope
than real-world product work
[[2018-02-12_solving-design-exercises_15-step-7-measure-success-how]]. That
narrowing is worth keeping in view, because the rest of the corpus holds that a
number means nothing without a reference point [[2020-05-03_benchmarking-ux]]
and that a post-launch figure without a documented baseline proves nothing
[[2026-06-26_establishing-baselines]]. Proposing an MVP or an experiment to
validate the solution before full investment is treated as part of the same step
[[2018-02-12_solving-design-exercises_15-step-7-measure-success-how]], and the
earlier technique of listing the tasks a customer must complete already frames
the flow as completion that can be measured
[[2018-02-12_solving-design-exercises_14-step-6-solve]].

Metric choice follows the problem statement rather than a standard list: a
doctor-facing dashboard meant to increase patients seen per day is measured by
task completion time and patient satisfaction (NPS), and the eight indicators
offered as examples are task success rate, completion time, engagement,
retention, revenue, conversion, user acquisition and NPS
[[2018-02-12_solving-design-exercises_15-step-7-measure-success-how]]. The
worked exercises show what that produces in practice:

- **Kiosk interface** — first interaction count, checkout completion time,
  checkout success rate and NPS
  [[2018-02-12_solving-design-exercises_18-3-1-designing-a-kiosk-interface]].
- **ATM redesign** — churn rate, queue reduction, decrease in PIN reset
  requests, card fraud reduction and adoption rate among people with
  disabilities
  [[2018-02-12_solving-design-exercises_22-3-5-improving-the-atm-experience]].
- **Freelancer dashboard** — the completion rate of "Up next" actions as the
  direct test that the dashboard unblocks projects, survey statements on
  perceived help with financial understanding, future planning and forward
  momentum, and product-level project completion and retention
  [[2018-02-12_solving-design-exercises_20-3-3-a-dashboard-for-freelancers]].

Each set runs past the interface into consequences the business tracks, which is
the upstream/downstream distinction
[[2026-07-03_reporting-ux-business-outcomes]] draws, applied at design time
rather than at reporting time.

### Behavioural, perceptual and business metrics

Behavioural metrics (completion rates, error rates, dropoff) are more
defensible than attitudinal ones (perceived ease, satisfaction) because they
show what actually happened rather than how users felt
[[2026-06-26_establishing-baselines]]. The benchmarking sources prefer to pair
the two: self-reported survey data alongside behavioural observation from
quantitative testing or analytics gives a more holistic reading
[[2020-09-13_product-ux-benchmarks]], and evaluating success with both
quantitative and qualitative data is described as the ideal, practised by only
24% of surveyed teams [[2018-09-02_quant-research-practice]].

Which measure fits which construct varies. Cognitive load is measured by survey
(NASA-TLX) or usability inspection rather than analytics; task efficiency by
controlled quantitative usability testing, because analytics are skewed by
external interruptions; satisfaction by surveys, post-task questionnaires and
indirect signals such as rage clicks; learnability by longitudinal testing or
log analysis of performance improvement; errors by analytics instrumentation
and analysis of repetitive error loops [[2023-01-29_castle-framework]].

### Common metric families in the corpus

- **Task metrics** — time to completion, click counts, success rates,
  satisfaction ratings, retention, tracked across redesign cycles
  [[2020-05-03_benchmarking-ux]]; time on task, completion rates and error
  reduction as the actual benefit of a time-saving feature, rather than its
  adoption rate [[2017-05-14_ux-goals-analytics]].
- **Tree-test metrics** — success rate (findability), directness (effort and
  struggle), and time spent (mental load); a median success rate of 62% across
  studies, with suggested bands of poor (<40), fair (41-60), good (61-80), very
  good (80-90) and excellent (>90), though mission-critical tasks should exceed
  90% and task importance matters more than the absolute number
  [[2024-01-19_interpreting-tree-test-results]]. High success with low
  directness means users succeeded despite difficulty
  [[2024-01-19_interpreting-tree-test-results]]. In one case study, a tree-test
  score moved from 4/10 to 7.4/10, an 85% findability improvement above the
  typical 75% average [[2021-01-31_quantifying-case-study]].
- **Expert-rated ease of use** — PURE (Pragmatic Usability Rating by Experts)
  fills the gap between expensive benchmarking studies and indirect behavioural
  metrics: three experts rate the steps of 3-20 fundamental tasks on a 1-3
  friction scale, silently then by discussion, aggregated per task and product
  and shown as green/yellow/red, with a target interrater reliability of 0.667+
  [[2017-04-16_pure-method]]. It measures friction on the happy path only, and
  makes frequent, comparable tracking affordable [[2017-04-16_pure-method]].
- **Loyalty metrics** — NPS asks likelihood to recommend on a 0-10 scale and
  subtracts the share of detractors (0-6) from promoters (9-10), discarding the
  passives (7-8); it measures loyalty rather than usability, varies by country
  and culture, needs large samples, and is easily gamed, so it should be one of
  several metrics supplemented by behavioural data
  [[2024-06-21_nps-ux]].
- **Analytics metrics** — pageviews, unique visitors, bounce rates, entrance
  rates, conversions, and search-query volume, each of which signals an
  information-architecture problem only when read in context of strategic
  importance, visual prominence, layout, and multi-stage journeys
  [[2016-09-25_ia-warning-signs-analytics]].
- **Commercial metrics** — revenue per visit is more meaningful than conversion
  rate alone, since it accounts for both how often people buy and how much they
  spend [[2017-12-03_m-commerce-terrible-ux]].
- **Domain-specific metrics** — games research uses measures uncommon in
  mainstream UX, such as kill/death ratios, skin-conductance sensors for
  frustration and arousal, and telemetry at the scale of hundreds of millions of
  sessions [[2016-03-20_game-user-research]].

### Frameworks for choosing dimensions

HEART (happiness, engagement, adoption, retention, task effectiveness) is the
starting framework for benchmarking selection
[[2020-09-13_product-ux-benchmarks]]. CASTLE — cognitive load, advanced feature
usage, satisfaction, task efficiency, learnability, errors — was designed for
productivity and workplace applications where users cannot choose whether to use
the product, so HEART's engagement, adoption and retention dimensions apply
poorly [[2023-01-29_castle-framework]]. Both work the same way: each dimension
is broken down into goals, behavioural signals and quantifiable measures, and
the framework guides the choice rather than prescribing specific measurements
[[2023-01-29_castle-framework]].

### Give raw numbers context

Vanity metrics — total users, downloads, page views, shares — always grow with
time and so cannot indicate whether anything improved
[[2019-10-13_vanity-metrics]]. Convert them with rates and ratios normalised by
time or population: downloads per store-page visit, page views per session,
DAU/MAU stickiness, unique-to-total page views as a pogosticking signal
[[2019-10-13_vanity-metrics]]. Pick a time frame that balances stability and
responsiveness — per-minute is noise, yearly delays discovery, weekly or monthly
is usually the sweet spot — and use cohort analysis to see whether improvements
stick [[2019-10-13_vanity-metrics]]. A metric worth keeping is one that changes
when the design changes [[2019-10-13_vanity-metrics]].

Context also governs interpretation. Low traffic, low conversion, high bounce,
low entrance rates and high search-query volume each have benign explanations —
a category may drive traffic elsewhere, support a long multi-visit journey, or
carry strategic or SEO value — so analytics should be read against content
strategy and business needs, and supplemented with A/B testing or surveys when
ambiguous [[2016-09-25_ia-warning-signs-analytics]].

### Baselines and tracking over time

Measure before the work starts. The most common way UX teams undermine their own
value is measuring too late: a 67% task-completion rate after a redesign only
proves anything if you know it was 48% before
[[2026-06-26_establishing-baselines]]. Document the method alongside the number
— how, who, when, what was measured — so that the post-launch comparison is
made the same way; a baseline without documentation is not a baseline
[[2026-06-26_establishing-baselines]]. Share the baseline with stakeholders
before building, so post-launch conversations complete a story instead of
arguing for UX's impact [[2026-06-26_establishing-baselines]].

Benchmarking is summative rather than formative: it happens between design
cycles, capturing a snapshot of one version, not guiding decisions inside a
cycle [[2020-05-03_benchmarking-ux]]. Run a pilot to validate the methodology
before collecting the baseline, and allow users time to adapt before measuring
again — 2-3 weeks for a daily product, 4-5 weeks for a weekly one — while
documenting external influences on both measurements
[[2020-09-13_product-ux-benchmarks]]. Frequency follows the method: quantitative
usability testing may only be affordable annually, while analytics permit
measurement after every redesign [[2020-05-03_benchmarking-ux]]. Metrics should
also evolve as goals and product strategy evolve [[2025-10-03_ux-metrics-goals]].

### Statistical rigour

Interpreting quantitative data requires confidence intervals, margins of error,
statistical significance and an understanding of study design (within-subjects
versus between-subjects); without it, conclusions are unreliable
[[2021-08-29_quantitative-research-study-guide]]. Use statistical methods to
decide whether an observed difference is real or noise
[[2020-09-13_product-ux-benchmarks]]. Comparing two information-architecture
trees needs 50+ participants per tree and manual significance testing; three or
more require ANOVA [[2024-01-19_interpreting-tree-test-results]]. NPS likewise
demands sample sizes that qualitative studies cannot supply — scoring five users
is meaningless [[2024-06-21_nps-ux]]. Where expert ratings are the instrument,
the equivalent of rigour is interrater reliability, targeted at 0.667+ and
typically 0.8-0.9 after training, with disagreement treated as a signal that
assumptions differ and must be resolved [[2017-04-16_pure-method]].

### Reporting metrics to the organisation

Report outcomes, not effort: "we conducted 24 interviews and 3 usability
studies" describes resources spent, not what changed
[[2026-07-03_reporting-ux-business-outcomes]]. UX-native metrics do not travel —
a CFO has no frame of reference for a SUS score, and a VP of operations cannot
connect a task-completion rate to quarterly targets — so they belong in research
reports rather than budget conversations
[[2026-07-03_reporting-ux-business-outcomes]]. Leaders assess investments
through five questions: does it impact revenue, reduce cost, mitigate risk,
improve speed to market, improve retention or satisfaction
[[2026-07-03_reporting-ux-business-outcomes]]. The fix is to chain upstream
metrics (task success, error rates, SUS) to downstream ones (support contact
volume, conversion, churn), partnering with finance, product analytics, support
or marketing to translate before-and-after data; even directional data persuades
if it is honest [[2026-07-03_reporting-ux-business-outcomes]].

This is the same argument benchmarking makes about ROI: connect UX metrics to
organisational KPIs — profit, cost, productivity, satisfaction — to demonstrate
the value of the work [[2020-09-13_product-ux-benchmarks]], and show concretely
how much faster, easier or more enjoyable the experience became
[[2020-05-03_benchmarking-ux]]. A quantitative case-study number serves the same
purpose in communicating impact to stakeholders
[[2021-01-31_quantifying-case-study]], and a simple numeric representation of
something they care about, like ease of use, tends to motivate stakeholders to
set goals against it [[2017-04-16_pure-method]]. In m-commerce, the metric
itself made the case: desktop visitors were worth 111% more per visit than
mobile ones in 2017, down from 288% in 2014, which framed mobile UX as an
investment priority [[2017-12-03_m-commerce-terrible-ux]].

Finally, metrics must be embedded where decisions happen — sprint reviews,
roadmap planning, OKRs, prioritisation — or they are tracked and never reviewed
[[2025-10-03_ux-metrics-goals]]. When stakeholders push for an easy but
misaligned metric, ask probing questions, propose an alternative capturing the
same intent, or run a test-drive of both [[2025-10-03_ux-metrics-goals]].

### Known obstacles

A survey of 429 UX professionals found that 71% do quantitative research at
least occasionally, but almost everyone struggles with it: 37% cited difficulty
recruiting large samples as the main obstacle, often because gatekeepers block
access to users in enterprise settings, and gaps in knowledge of quantitative
methods, data analysis and their value ranked high among the remaining barriers
[[2018-09-02_quant-research-practice]]. Analytics is among the most commonly
used methods, but is often collected without being applied to design decisions
[[2018-09-02_quant-research-practice]].

## Sources (22)

- [[2016-03-20_game-user-research]] — games introduce metrics like kill/death ratios and engagement biometrics not common in mainstream UX.
- [[2016-09-25_ia-warning-signs-analytics]] — Explains how to interpret analytics metrics (pageviews, unique visitors, bounce rates, entrance rates, conversions) within context to identify IA problems and validate improvements.
- [[2017-04-16_pure-method]] — PURE provides an alternative metrics approach filling the gap between expensive benchmarking studies and indirect behavioral metrics, enabling frequent tracking.
- [[2017-05-14_ux-goals-analytics]] — Shows how goal-down thinking reveals actionable metrics that behavioral analytics or A/B testing alone would miss.
- [[2017-12-03_m-commerce-terrible-ux]] — Quantitative measures of user experience quality; revenue per visit is a more meaningful metric than conversion rate alone, accounting for both transaction frequency and purchase amount.
- [[2018-09-02_quant-research-practice]] — measurable indicators of system performance and user satisfaction; effective metrics programs connect quantitative findings to actionable design improvements.
- [[2019-10-13_vanity-metrics]] — Choosing what to measure requires understanding user tasks, business goals, and what changes in the metric actually mean; aggregates without context waste analysis effort.
- [[2020-05-03_benchmarking-ux]] — describes various quantifiable measurements (time to completion, click counts, success rates, satisfaction ratings, retention) that can be tracked over redesign cycles.
- [[2020-09-13_product-ux-benchmarks]] — Effective benchmarking selects 2-4 metrics across different aspects of user experience (happiness, engagement, adoption, retention, task effectiveness) that align with organizational goals and can be tracked repeatedly.
- [[2021-01-31_quantifying-case-study]] — demonstrates how quantitative metrics (tree test scores) can measure the impact of UX improvements and communicate results to stakeholders.
- [[2021-08-29_quantitative-research-study-guide]] — UX metrics are numerical representations of user experience aspects; they include behavioral metrics (success, time, errors), perceptual metrics (satisfaction, perceived usability), and business metrics (conversion, revenue, retention).
- [[2023-01-29_castle-framework]] — CASTLE provides a measurement framework for workplace applications where each dimension breaks into goals, signals, and measures to guide metric selection and tracking; effective measurement requires combining quantitative metrics (for tracking progress) with qualitative research (for understanding why), since metrics alone tell what changed, not how to improve.
- [[2024-01-19_interpreting-tree-test-results]] — success rate, directness, and time spent are standard usability metrics; understanding how to interpret each in context of task importance is essential.
- [[2024-06-21_nps-ux]] — measuring user experience requires multiple metrics; NPS reflects loyalty but not usability, requiring supplementary behavioral measurements.
- [[2025-10-03_ux-metrics-goals]] — Proposes connecting metrics directly to organizational goals through collaborative workshop methodology—pre-survey to uncover disconnects, cluster goals and KPIs, identify UX contributions, define and prioritize metrics, and embed in workflows where they'll be used—ensuring metrics reflect real UX influence on outcomes, are measurable and tracked, and inform actual decisions.
- [[2026-06-26_establishing-baselines]] — requires choosing relevant, behavior-linked metrics that directly reflect the user experience being changed and tracking them consistently from baseline through post-launch to prove whether UX work created meaningful change.
- [[2026-07-03_reporting-ux-business-outcomes]] — must connect to downstream business outcomes that leadership tracks, such as revenue impact, cost reduction, and retention.
- [[2018-02-12_solving-design-exercises_14-step-6-solve]] — While not the focus of this chapter, the author frames task lists in terms of task completion as a measurable outcome, which ties to later evaluation of solution success.
- [[2018-02-12_solving-design-exercises_15-step-7-measure-success-how]] — Quantifiable indicators such as task success rate, task completion time, engagement, retention, revenue, conversion, user acquisition, and NPS that demonstrate whether a designed solution achieves its intended outcomes.
- [[2018-02-12_solving-design-exercises_18-3-1-designing-a-kiosk-interface]] — the candidate proposes measuring success with first interaction count, checkout completion time, checkout success rate, and NPS, showing how to define measurable outcomes for the design
- [[2018-02-12_solving-design-exercises_20-3-3-a-dashboard-for-freelancers]] — The chapter proposes "Up next" actions completion rate to validate that the dashboard successfully unblocks projects, and survey statements measuring perceived help with financial understanding, future planning, and forward momentum, tied to product-level metrics like project completion and retention.
- [[2018-02-12_solving-design-exercises_22-3-5-improving-the-atm-experience]] — Five specific metrics to validate the design solution: churn rate, queue reduction, PIN reset decrease, card fraud reduction, and disability adoption rate.
