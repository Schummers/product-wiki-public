---
type: source
name: "Confidence Intervals, Margins of Error, and Confidence Levels in UX"
created: 2026-07-30
published: 2021-06-27
source_type: article
status: processed
url: https://www.nngroup.com/articles/confidence-interval/
author: Raluca Budiu
raw: raw/sources/2021-06-27_confidence-interval.md
concepts:
  - "Confidence Intervals"
  - "Statistical Analysis"
  - "Research Validity"
  - "Sample Size"
  - "Confidence Level"
---

# Confidence Intervals, Margins of Error, and Confidence Levels in UX

## Summary

A confidence interval is the likely range for the true population score based on an observed score from a study sample. The margin of error describes the width of that range (e.g., 79% ± 2.1% means 77-81% true score range). Three factors influence confidence interval width: sample size (larger samples produce narrower intervals), variability in the sample (higher variability produces wider intervals), and confidence level (higher confidence levels like 95% produce wider intervals than lower levels like 80%). The confidence level indicates how often the calculated range will contain the true score; a 95% confidence level means 95% of studies will produce correct ranges, with 5% being wrong. Researchers choose confidence levels based on what's at stake: higher stakes (critical functions) justify higher confidence levels and larger studies, while lower stakes allow acceptable risk.

## Key Takeaways

- **Confidence Interval Definition** — The likely range for the true population score; a 50% ± 10% confidence interval means the true score is likely between 40-60%.
- **Margin of Error** — The range width around the observed score; confidence interval width equals twice the margin of error (observed ± margin of error).
- **Sample Size Impact** — Larger sample sizes produce narrower confidence intervals; small studies (5-10 people) produce large measurement errors and wide, uninformative confidence intervals.
- **Variability Affects Width** — For continuous metrics like task time, high variability between participants produces wider confidence intervals than low variability, independent of sample size.
- **Confidence Level Tradeoff** — 95% confidence level is standard in science; UX can use lower levels (80%) for less critical decisions, producing narrower intervals but with 20% risk of being wrong.
- **Cost of High Confidence** — Achieving a 95% confidence interval with the same width as an 80% interval requires substantially more participants (40%+ increase), representing significant resource cost.
- **Risk-Based Selection** — Choose confidence level based on stakes: critical interfaces (plane dashboards) need 95%+; less critical tasks (video system reset) can use 80%; decision magnitude determines justifiable cost.

## Quotes

> Definition: A confidence interval is the likely range for the true score of your entire population.

> In general, narrower confidence intervals carry more information. And when we are running quantitative studies, we're always striving for narrow confidence intervals.

> The confidence level tells you how confident you can be that your calculation of a confidence interval will include the true score.

## Concepts

- [[Confidence Intervals]] — Statistical range quantifying uncertainty around observed metrics from studies; essential for any metric reporting.
- [[Statistical Analysis]] — Framework for determining reliability of study findings and whether they represent true population behavior.
- [[Research Validity]] — Difference between observed and true scores; larger in small samples and studies with high variability.
- [[Sample Size]] — Primary driver of confidence interval width; larger samples produce narrower, more informative intervals.
- [[Confidence Level]] — Probability that calculated confidence interval contains true score; higher levels cost more resources but provide more certainty.
