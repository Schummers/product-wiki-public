---
type: concept
name: Statistical Significance
created: 2026-07-31
updated: 2026-09-11
status: stub
---

# Statistical Significance

## Definition

Statistical significance is what separates a real difference from random
chance. In measurement terms it tells you whether an observed difference
reflects a genuine true-score difference or is just measurement noise, with
p < 0.05 taken as the significance threshold [[2021-05-23_true-score]].
Interpreting a quantitative finding therefore means reading the study design
alongside the number: the confidence level (95% or 90%) and the margin of error
(15% or 20%) [[2021-07-25_summary-quant-sample-sizes]].

Christian Crumlish approaches it from the practitioner's side, as the threshold
of sample size and consistency at which an [[A-B Testing]] result can be
trusted. As a very broad rule of thumb he says you tend to need at
least 2,000 people in each bucket before you can trust a result, and separately,
of an A/A test, that you should not be surprised if the two groups' results
stabilise at parity when there are about 2,000 people in each. Two disciplines
protect the reading: decide the end condition before running the test, so a
favourable moment cannot be cherry-picked, and run an A/A test — identical
control and variant — to see when results stabilise at parity
[[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]].

## Sources (3)

- [[2021-05-23_true-score]] — P-values indicate whether observed differences reflect real true-score differences or are just measurement noise; p < 0.05 indicates statistical significance.
- [[2021-07-25_summary-quant-sample-sizes]] — Statistical significance indicates whether observed differences are real or due to random chance; understanding confidence levels (95% or 90%), margins of error (15% or 20%), and study design is essential for interpreting quantitative findings.
- [[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]] — the threshold of sample size and consistency at which you can trust A/B test results; as a very broad rule of thumb you tend to need at least 2,000 people per bucket, and an A/A test (identical control and variant) shows when results stabilize at parity, which Crumlish says may also happen around 2,000 per group.
