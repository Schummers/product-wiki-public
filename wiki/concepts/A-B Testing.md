---
type: concept
name: A-B Testing
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "A/B Testing"
  - "AB Testing"
  - "Split Testing"
---

# A-B Testing

## Definition

A/B testing is the method of running two versions of an interface element
simultaneously to determine, with real numbers, which one converts better
[[2024-06-11_332_Designer_et_AB_tester_un_paywall]]. Across the sources it is
treated less as a research technique in its own right than as the arbitrator of
last resort: the thing you do when reasoning, expertise, and intuition cannot
settle a question. On paywall length there is no universal answer, so "the best
method for iterating on a paywall is the A/B test"
[[2024-06-11_332_Designer_et_AB_tester_un_paywall]]. In a funnel, it is the way
to compare a proposed fix against the existing version
[[2026-05-19_414_L_anatomie_d_un_funnel_-_Guide_Growth_&_UX]]. For entry
points, it is how you find which variant performs best on click-through and
bounce [[2026-06-09_417_Les_3_clés_de_l_adoption_produit_-_Hacks_Growth_Design]].

Its authority comes from context-dependence. What works depends intrinsically on
the specific company, its users, and its offer, which is precisely the data no
amount of external judgement — including an AI's — possesses without a real
test [[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]].

## Practice

### Where A/B testing is applied

The recurring application in this corpus is monetisation and conversion.
Paywalls: testing short versus long formats, since there is no absolute answer
and the right one depends on context — on the Habitude app a long paywall raised
conversion by 50% [[2024-06-11_332_Designer_et_AB_tester_un_paywall]]. The
conversion funnel more broadly: testing different prices, wordings, and offers
to continuously optimise the sales tunnel's conversion rate
[[2025-05-06_376_Designer_un_funnel_de_conversion_paywall_-_Gold_standard_2025]].
Feature adoption: comparing entry points to find the most effective on
conversion and bounce
[[2026-06-09_417_Les_3_clés_de_l_adoption_produit_-_Hacks_Growth_Design]]. And
wording or sales arguments, validated in production to obtain tangible data
[[2025-09-23_396_UX_Research_en_StartUp,_guide_et_astuces]].

### Where in a funnel to test

The funnel anatomy places A/B testing precisely. The first step (the bounce)
normally loses 10–30% of users, and that loss usually reflects the quality of
the entry point — marketing campaign, SEO — rather than a UX problem, so the
optimisation belongs upstream in attracting a qualified audience rather than in
over-investing in that first screen
[[2026-05-19_414_L_anatomie_d_un_funnel_-_Guide_Growth_&_UX]]. The middle steps
(the descent) should target 95% conversion per step; a significant loss here
signals a genuine UX problem, located through data tracking and then iterated on
via A/B testing or user testing
[[2026-05-19_414_L_anatomie_d_un_funnel_-_Guide_Growth_&_UX]]. The final step
(completion) calls for testing deeper conceptual changes and new engagement
approaches rather than surface variants
[[2026-05-19_414_L_anatomie_d_un_funnel_-_Guide_Growth_&_UX]].

### Instrumentation: analytics as a prerequisite

Event-based analytics makes A/B test analysis easier by letting you define
precise entry and exit events to measure and compare conversion between variants
[[2024-07-02_335_L’event_based_analytics_pour_les_designers_-_Data-driven_culture]].
The same source's warnings apply directly to test validity: define a tracking
plan at design time listing the events and properties to follow, and test it
after implementation, because "nothing is worse than a badly implemented
tracking plan" — it returns bad data and leads to wrong conclusions
[[2024-07-02_335_L’event_based_analytics_pour_les_designers_-_Data-driven_culture]].
It also recommends crossing volume metrics with conversion metrics in dashboards
to avoid bias
[[2024-07-02_335_L’event_based_analytics_pour_les_designers_-_Data-driven_culture]].

### Guardrail metrics

Conversion alone is not a sufficient verdict. On paywalls, churn must be
monitored alongside conversion to confirm that converted customers are viable in
the long run [[2024-06-11_332_Designer_et_AB_tester_un_paywall]]. On funnels,
the question posed is direct: what is the point of optimising a funnel if you
lose on user retention over the longer term? Completion should be optimised
without forcing the user's hand at the expense of durable use
[[2026-05-19_414_L_anatomie_d_un_funnel_-_Guide_Growth_&_UX]].

### A/B testing in a startup context

In startups, the academic research process should be abandoned in favour of
targeting the riskiest hypotheses; quick concept tests, A/B testing, and fake
doors are named as the methods that de-risk the essentials with excellent return
on investment [[2025-09-23_396_UX_Research_en_StartUp,_guide_et_astuces]]. The
framing is that startups accept a higher level of risk and therefore need
somewhat less upfront research, with quantitative metrics serving as tangible
evidence when arguing against founder intuition
[[2025-09-23_396_UX_Research_en_StartUp,_guide_et_astuces]].

### What A/B testing cannot be replaced by

Asking an AI to guess which of two wordings will perform better is described as
illusory: the effectiveness of words depends on the company's and users'
context, data the model does not hold without a real test
[[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]]. AI can
still be used upstream of the test, to check that a wording is comprehensible
outside internal jargon and to generate 10–30 suggestions to remix manually, but
the choice between finalists belongs to expertise and to live testing
[[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]].

### Running the test with discipline

Christian Crumlish describes A/B testing as a form of bucket testing: users are
split into two equal cohorts, one on the control experience and one on the
variant, to measure the impact on a goal metric
[[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]].
His operating rules concern scheduling and honesty about the end point:

- **Decide the end condition before running the test**, precisely to avoid
  cherry-picking a moment when the numbers look good.
- **Give the test enough people.** As a very broad rule of thumb Crumlish says
  you tend to need at least 2,000 people in each bucket before you can trust a
  result, and that in an A/A test you should not be surprised if the two groups
  stabilise at parity around that same 2,000 each. This is looser than the
  quantitative-research sources on this page, which set a threshold rather than
  an observation: ninety-five percent statistical confidence, large samples for
  small changes, and enough duration to absorb external variables
  [[2013-08-01_just-enough-research_10-chapter-9-quantitative-research]]. Both
  are on the page; neither cancels the other.
- **Run an A/A test** — identical control and variant — to see when results
  stabilise at parity.
- **Record the qualitative insight, not only the number**: what the result means
  for the next hypothesis.
- **Stack wins and learn from losses equally.** Once a test succeeds, lock it in
  and attempt follow-up tests to compound the improvement; a loss teaches
  something about the hypothesis or about the test itself.

### Blind spots and contexts where it does not apply

Crumlish's caution is that A/B tests reveal what happened but not why, so
further validation through qualitative research is essential; that externalities
such as seasonal changes, marketing campaigns or industry events can skew a
result without the team knowing; and that overreliance leads to "polishing a
local maximum," optimising one small area while missing much larger
opportunities
[[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]].
The same limitation is stated elsewhere on this page as a retroactive look at
behaviour rather than the "why" behind it
[[2016-11-04_ux-research_04-chapter-3-quantitative-research-methods]], and as
usefulness for incremental optimisation rather than strategic direction
[[2013-08-01_just-enough-research_10-chapter-9-quantitative-research]].

The sharper caveat is a whole context where the method is unavailable. Clement
Kao, quoted in Crumlish's chapter, argues that in B2B you cannot A/B test at
all, because someone is using your product to run their business: training one
cohort of users on one workflow and another cohort on a different one is not
something you can do, and recruiting a random "enterprise user" is unhelpful
when you are going after a specific set of named accounts in high-touch
relationships
[[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]].
For those contexts the chapter routes to the other twelve experiment types it
catalogues (see [[Assumption Testing]]).

### Expectations about effort

Designing an excellent paywall takes time and many iterations
[[2024-06-11_332_Designer_et_AB_tester_un_paywall]], and one source adds a
limit on what optimisation can buy: a good monetisation strategy will never
compensate for not having a good product
[[2025-05-06_376_Designer_un_funnel_de_conversion_paywall_-_Gold_standard_2025]].

## Sources (10)

- [[2024-06-11_332_Designer_et_AB_tester_un_paywall]]
- [[2024-07-02_335_L’event_based_analytics_pour_les_designers_-_Data-driven_culture]]
- [[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]]
- [[2025-05-06_376_Designer_un_funnel_de_conversion_paywall_-_Gold_standard_2025]]
- [[2025-09-23_396_UX_Research_en_StartUp,_guide_et_astuces]]
- [[2026-05-19_414_L_anatomie_d_un_funnel_-_Guide_Growth_&_UX]]
- [[2026-06-09_417_Les_3_clés_de_l_adoption_produit_-_Hacks_Growth_Design]]
- [[2013-08-01_just-enough-research_10-chapter-9-quantitative-research]] — a controlled experiment where different page variations are shown randomly to visitors to determine which performs better; also called A/B testing or multivariate testing; requires ninety-five percent statistical confidence, large sample sizes for small changes, and sufficient duration to account for external variables; useful only for incremental optimization, not strategic direction.
- [[2016-11-04_ux-research_04-chapter-3-quantitative-research-methods]] — a version of site analytics where two different versions of a page are presented to customers so researchers can identify a leading option, focused on a specific question with established KPIs, though limited to a retroactive look at behavior rather than the "why" behind it
- [[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]] — a form of bucket testing in which users are split into two equal cohorts, one receiving a control experience and the other a variant, to measure statistical impact on a goal metric. Requires discipline around scheduling, statistical significance thresholds, and learning beyond the numerical result.
