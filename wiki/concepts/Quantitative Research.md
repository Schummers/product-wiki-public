---
type: concept
name: Quantitative Research
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Quantitative UX Research"
---

# Quantitative Research

## Definition

Quantitative UX research collects numerical metrics that represent aspects of the
user experience — success rates, task completion times, satisfaction scores — in
order to measure the scale or priority of design problems, benchmark an
experience, track it over time, and compare design alternatives experimentally
[[2021-08-29_quantitative-research-study-guide]]
[[2021-07-25_summary-quant-sample-sizes]]. It answers "how many" and "how much";
qualitative research answers "why" and "how to fix it", and the two are
complementary rather than competing
[[2021-08-29_quantitative-research-study-guide]]
[[2022-08-21_guide-ux-research-methods]]. NN/g's method framework places all
research on two axes — attitudinal vs. behavioral (what people say vs. what they
do) and qualitative vs. quantitative — which puts analytics, A/B testing and
quantitative usability testing in the behavioral-quantitative quadrant and
surveys, uniquely, in the attitudinal-quantitative one
[[2022-08-21_guide-ux-research-methods]] [[2024-02-23_should-you-run-a-survey]].

The methods in scope include quantitative usability testing, analytics, A/B and
multivariate testing, surveys, and card sorting and tree testing for information
architecture [[2021-08-29_quantitative-research-study-guide]]
[[2018-09-02_quant-research-practice]] [[2024-01-19_interpreting-tree-test-results]].
*UX Research* draws the same boundary in stronger terms: a quantitative result
should be "consistent and generally agreed on by all parties involved," unlike
a subjective measure such as personality, and while informative, quantitative
research doesn't tell a team how to fix a problem, doesn't explain why it
happens, and doesn't share information nobody asked for or measured. The same
source adds tree jacking (iterative testing of proposed navigation and
terminology solutions) and eye tracking (camera-based tracking of eye movement
on screen-based products) to the method inventory
([[2016-11-04_ux-research_04-chapter-3-quantitative-research-methods]]).
The practice is widespread but uncomfortable: in a survey of 429 UX
professionals, 71% did quantitative research at least occasionally, yet only 2
respondents reported doing at least one quantitative study per project with no
significant concerns — "almost everyone struggles with quantitative research in
some way" [[2018-09-02_quant-research-practice]].

*UX Research* also frames the discipline around three research focuses:
insight-driven research seeks to understand the problem space and identify
opportunities through benchmarks and KPIs; evaluative research measures how a
design stands up against those KPIs; and generative research balances
subjective design recommendations against quantifiable, measurable gains
([[2016-11-04_ux-research_04-chapter-3-quantitative-research-methods]]).

## Practice

### Choosing quantitative — and choosing the method

Quantitative work is the right call when the question is about magnitude,
frequency or comparison; qualitative work when the question is about causes and
mechanisms [[2021-08-29_quantitative-research-study-guide]]
[[2022-08-21_guide-ux-research-methods]]. The attitudinal/behavioral axis narrows
the choice further: interviews and focus groups for what people think, surveys
for attitudes at scale (with social-desirability bias as the known cost), field
studies and observation for real practices, analytics and usability testing for
performance [[2022-08-21_guide-ux-research-methods]]. Most substantial questions
warrant methods from more than one quadrant
[[2022-08-21_guide-ux-research-methods]]. *UX Research* narrows it further still:
quantitative methods work best when a large number of participants is
reachable for statistically significant outcomes and the research question has
a tangible, measurable outcome, and should be avoided when the goal is
understanding user motivation or comprehension (qualitative territory instead),
when the user population is too small for analytics to be statistically
significant, or in an entirely new market where analytics may not yet exist
([[2016-11-04_ux-research_04-chapter-3-quantitative-research-methods]]).

*UX Research* devotes a full chapter to this choice. It notes quantitative work
suits a "set-and-forget" measurement mode such as ongoing analytics and is
rooted in statistics, typically favouring large data sets — though it adds
that quantitative studies can also be performed with small data sets, so the
split is a general guideline rather than a strict rule. Selection should start
from the questions being asked and the stakeholders' goals (validating an
assumption, defining a new market, proving organisational value each favour a
different mix), then check available sample size, participant location,
budget, and timeline, framed as a "project triangle" where time, budget, and
scope compete and practitioners choose which two matter most. Its rule for
mixing methods is to identify a qualitative and a quantitative measure for the
same root question, rather than combining disparate methods or expecting one
method to serve unrelated goals
([[2016-11-04_ux-research_06-chapter-5-choosing-your-methods]]).

Surveys get the sharpest warning in the corpus. They are "the hardest research
method to do well (yet the easiest to launch in the next 10 minutes)", small
wording changes move results significantly, and large samples cannot rescue
flawed methodology; nor are they a gentler alternative to interviews. Their
legitimate use is narrow: quantitative, attitudinal questions such as what
percentage of users believe or feel something
[[2024-02-23_should-you-run-a-survey]]. Where in the design cycle you are
determines which survey to run: discovery and diary surveys in Discover;
competitor and statistical-persona surveys in Explore; post-task and post-test
instruments (SEQ, SUS) in Test; NPS, CSAT and CES in Listen — with the caveat
that NPS should never be the only usability metric
[[2023-11-24_surveys-design-cycle]].

A/B testing is defined as comparing two or more design variations with a live
audience against predetermined business-success metrics, in four steps:
hypothesis, defined change, outcome metrics, timeframe. It tells you which
variation wins, never why. Only about one in seven A/B tests is a winner, and the
rate improves markedly when the hypothesis comes from qualitative findings rather
than assumption. Use a calculator to size the test from the baseline metric,
minimum detectable effect and significance threshold, run it at least one to two
weeks to absorb behavioral fluctuation, and track guardrail metrics alongside the
primary one — otherwise a change can lift one metric while damaging another, as
deceptive patterns lift conversion while hurting retention. It is unsuited to
low-traffic products and to testing several elements at once
[[2024-08-30_ab-testing]].

### Sample size

The headline guideline is 40 participants for quantitative studies, derived from
a calculation assuming a population above 500, a 15% margin of error and 95%
confidence [[2021-07-25_summary-quant-sample-sizes]]. The assumptions are
adjustable: relaxing to a 20% margin and 90% confidence drops the requirement to
28. Continuous metrics such as task time or satisfaction depend on population
variability — with Nielsen's estimate of a standard deviation at 52% of the mean,
roughly 47 users are needed for 95% confidence and a 15% margin. Teams on tight
budgets can start at 20–25, compute the resulting margins of error, and add
participants if precision is insufficient, provided analysis is fast enough to
keep the study valid [[2021-07-25_summary-quant-sample-sizes]]. Method-specific
figures exist too: comparing two information architectures in a tree test needs
50+ participants per tree, and three or more trees requires ANOVA
[[2024-01-19_interpreting-tree-test-results]].

The apparent conflict with Nielsen's "5 users" rule is not a conflict at all: the
5-user guideline applies to *qualitative* studies whose goal is identifying
issues, and you do not collect metrics in a qualitative study
[[2021-07-11_5-test-users-qual-quant]]. That guideline rests on three
assumptions — the goal is issue identification, any issue a user hits is worth
fixing, and the probability of any one user encountering a given issue is 31% (a
1990s average). Better interfaces have lower encounter probabilities: at 10–20%,
the Nielsen–Landauer formula calls for 9–18 users. What makes 5 robust is not
coverage but ROI, whose gain-to-cost peak sits around 5 in an iterative
test-fix-retest cycle. Quantitative studies have the opposite goal — predicting
population behavior — so small samples yield confidence intervals too wide to be
useful, hence 40+ [[2021-07-11_5-test-users-qual-quant]].

### Designing a valid study

Task writing differs fundamentally by method. A quantitative task must admit a
single interpretation and a single success criterion, and be specific enough that
every participant does essentially the same thing; ambiguity and open-endedness
are outright failures because they inject variability into the data. Multiple
success criteria contaminate metrics by making partial success ambiguous. Dummy
login credentials keep inputs identical and avoid hesitation over personal data.
Qualitative tasks may be open-ended and may even change mid-study when a better
understanding emerges — there, flexibility is a feature. Both kinds must be
realistic and derived from user research, search logs, analytics or
customer-service calls rather than designer assumption; both must avoid priming
language and exact UI labels; and both should be pilot-tested with one or two
representative users [[2018-01-21_test-tasks-quant-qualitative]].

Study design choices carry statistical consequences. Between-subjects (different
participants per condition) and within-subjects (same participants across all
conditions) designs change recruitment needs, session length and which tests
apply [[2023-07-02_quant-ux-glossary]]. **Confounding variables** — unmeasured
variables that affect both conditions and outcomes — are the main threat to
internal validity; the worked example is a within-subjects study where design A
was tested in the morning and design B after lunch. Common sources are age
effects, seasonal effects, market shifts, prior product experience and
preexisting opinions. Controls: randomise or counterbalance the order of
conditions, keep the testing environment consistent, and measure suspected
confounds so they can be controlled statistically. If they cannot be controlled,
the recommendation is to run qualitative exploratory research instead
[[2023-09-24_confounding-variables-quantitative-ux]]. Internal validity means the
setup is fair to all conditions and does not bias participants; external validity
means the setup and participants reflect the real world
[[2023-07-02_quant-ux-glossary]]
[[2023-09-24_confounding-variables-quantitative-ux]].

### Metrics and vocabulary

Metrics divide into performance metrics (behavior) and self-reported metrics
(perception), and into categorical, continuous, discrete or binary — each
demanding a different analysis [[2023-07-02_quant-ux-glossary]]. The study guide
adds business metrics (conversion, revenue, retention) to behavioral and
perceptual ones [[2021-08-29_quantitative-research-study-guide]]. Standardised
instruments — SUS, NPS, NASA-TLX — exist precisely so results can be compared
across studies and organizations, and a benchmark may be a target value or one
taken from a third-party study [[2023-07-02_quant-ux-glossary]]
[[2023-11-24_surveys-design-cycle]]. Confidence intervals and margins of error
express precision and depend on sample size and confidence level; a p-value below
0.05 is the conventional threshold for statistical significance
[[2023-07-02_quant-ux-glossary]].

Tree testing illustrates how metrics need a frame of reference. It produces
success rate (findability), directness (percentage reaching the destination
without backtracking, a proxy for struggle) and time spent (mental load); the
median success rate across studies is 62%, with suggested bands of poor (<40),
fair (41–60), good (61–80), very good (80–90) and excellent (>90). But absolute
numbers matter less than task importance — mission-critical tasks should exceed
90% — and a high success rate with low directness still means a poor experience.
First-click data is highly predictive: once users reach the right top-level
category, context cues usually carry them home, and a wrong first click is often
fatal [[2024-01-19_interpreting-tree-test-results]].

### Interpreting: significance is not importance

Statistical significance says a result is unlikely to be random; practical
significance says it is big enough to matter. The two come apart in both
directions. With very large datasets, differences as small as a 0.2% completion
gap or a 0.03% reduction reach significance while being invisible to users; with
small samples, a consistent pattern — 10 of 12 participants failing a task versus
1 of 12 — can be plainly meaningful without a p-value. Practical significance is
context- and scale-dependent: a $2 improvement per conversion is worth $150,000 a
year at two million conversions. The three lenses offered are: would users notice,
does it support a business outcome, and what does the effect size say. The
article also notes that many impactful insights come from qualitative work that
needs neither large samples nor statistical tests
[[2026-03-06_practical-significance]].

### Presenting the results

Charts should be designed the way an interface is designed, starting from the
question "what is your goal — what point are you trying to make?"
[[2022-01-30_choosing-chart-types]]. NN/g's "3 Cs for better charts" are context,
clutter-free and contrast [[2022-01-30_choosing-chart-types]]; the study guide
frames the same requirement as context, contrast and minimal clutter, with charts
communicating a takeaway rather than dumping data
[[2021-08-29_quantitative-research-study-guide]]. Context means comparison: a
lone number such as a 24% completion rate is meaningless until set against a
previous year, a competitor, another user group or another task. Bar charts are
the most comprehensible for comparisons; paired bars should be grouped so the
intended comparison sits adjacent; horizontal bars suit long labels; line charts
suit trends over time, with markers for collection points. Stacked bars, pie
charts, bubble charts and anything requiring judgment of angle, area or volume
should be avoided unless they add unique value
[[2022-01-30_choosing-chart-types]].

### Combining with qualitative work

The corpus's stated ideal is judging success on both measured results and
observations — practised by only 24% of the 429 surveyed professionals, while
others rely on one alone or on stakeholder satisfaction
[[2018-09-02_quant-research-practice]]. **Mixed-methods research** is the
disciplined version: qualitative and quantitative methods planned together from
the start, under one overarching research question, with three design patterns —
explanatory sequential (quant first to find patterns, qual to explain them),
exploratory sequential (qual first to generate hypotheses, quant to test them)
and convergent parallel (both at once, as independent but complementary
evidence). The value lies in integration rather than addition: how the two data
sets connect, explain each other, or triangulate. The cost is real — more time,
more protocols, more participant groups, closer coordination
[[2025-07-25_mixed-methods-research]]. The same pairing logic appears in
individual methods: A/B tests need qualitative research to explain the *why* and
to source hypotheses [[2024-08-30_ab-testing]], and surveys pair well with
qualitative findings to give stakeholders multifaceted evidence
[[2024-02-23_should-you-run-a-survey]].

### Obstacles in practice

Beyond method, the reported barriers are organizational and personal:
recruiting large samples is the single most common obstacle (37%), often because
gatekeepers block access to users in enterprise settings; knowledge gaps about
quantitative methods, analysis, and even the value of the work rank high; and
analytics is the most-used method partly because it is collected by default,
frequently without being applied to design decisions
[[2018-09-02_quant-research-practice]]. The same article notes the underlying
motivation for doing this work at all: UX is often perceived as a "soft" science
because of its reliance on qualitative observation
[[2018-09-02_quant-research-practice]].

## Sources (18)

- [[2018-01-21_test-tasks-quant-qualitative]] — Research that measures and compares variables to establish statistical patterns; requires controlled conditions, large samples, and specificity to ensure data reliability.
- [[2018-09-02_quant-research-practice]] — numerical methods for gathering data at scale; includes analytics, A/B testing, surveys, and quantitative usability testing that produce statistical insights about user behavior.
- [[2021-07-11_5-test-users-qual-quant]] — Studies measuring population metrics; 40+ users necessary to produce narrow confidence intervals and reliable generalization.
- [[2021-07-25_summary-quant-sample-sizes]] — Quantitative research in UX collects numerical metrics (success rates, task time, satisfaction) to measure the scale or priority of design problems, benchmark experiences, and compare design alternatives experimentally.
- [[2021-08-29_quantitative-research-study-guide]] — Quantitative research in UX collects numerical metrics (success rates, task times, satisfaction) to measure problem scale, prioritize issues, benchmark performance, and compare design alternatives; it complements qualitative research by answering "how much" questions.
- [[2022-01-30_choosing-chart-types]] — When presenting quantitative UX findings, apply user-centered design principles: define your goal first, provide context through comparison, and select chart types based on what enables viewers to understand your main point.
- [[2022-08-21_guide-ux-research-methods]] — Methods like surveys and analytics measure how many and how much, providing scale and statistical confidence but losing contextual depth.
- [[2023-07-02_quant-ux-glossary]] — the glossary provides foundational terminology for conducting and interpreting quantitative UX research.
- [[2023-09-24_confounding-variables-quantitative-ux]] — Confounding variables can systematically bias quantitative study results and invalidate the internal validity of findings.
- [[2023-11-24_surveys-design-cycle]] — surveys generate quantitative data; understanding appropriate metrics (SUS scores, NPS ranges, success rates) enables meaningful interpretation.
- [[2024-01-19_interpreting-tree-test-results]] — tree testing generates quantitative metrics; interpreting them requires statistical thinking, baselines, and within-study comparisons.
- [[2024-02-23_should-you-run-a-survey]] — research measuring magnitude and frequency; surveys are the attitudinal variant.
- [[2024-08-30_ab-testing]] — covers statistical concepts like sample size, significance, and measurement error relevant to A/B testing.
- [[2025-07-25_mixed-methods-research]] — The article explains how quantitative methods reveal patterns, trends, and effects at scale across large user groups.
- [[2026-03-06_practical-significance]] — Addresses the pitfalls of large-sample quantitative research and how to avoid over-interpreting statistical significance as meaningful change.
- [[2013-08-01_just-enough-research_10-chapter-9-quantitative-research]] — the chapter frames it as measurement and analysis of actual website or application usage to understand effectiveness; conducted after launch when real user data is available; enables identification of performance gaps and validation of design changes.
- [[2016-11-04_ux-research_04-chapter-3-quantitative-research-methods]] — the chapter's primary topic, defining and situating quantitative research as one side of a complementary pair with qualitative methods, covering its definition, applications, and limitations
- [[2016-11-04_ux-research_06-chapter-5-choosing-your-methods]] — addressed as one category in the selection equation: rooted in statistics, it often requires large data sets and suits a "set-and-forget" measurement mode like ongoing analytics, though the chapter notes quantitative studies can also be performed with small data sets
