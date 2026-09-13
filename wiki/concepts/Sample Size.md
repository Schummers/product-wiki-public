---
type: concept
name: Sample Size
created: 2026-07-31
updated: 2026-07-31
status: developed
---

# Sample Size

## Definition

Sample size is how many participants a study includes, and across these sources
the central message is that there is no single right answer: the number follows
from the study's goal, not from a general rule of thumb. Qualitative studies
that identify usability issues need few participants; quantitative studies that
measure metrics and generalise them to a population need many; interview studies
follow a third logic entirely, driven by saturation rather than by any formula
[[2021-07-11_5-test-users-qual-quant]], [[2021-07-25_summary-quant-sample-sizes]],
[[2021-10-31_interview-sample-size]].

Where numbers are being reported, sample size is the main determinant of how
much they can be trusted. True-score theory frames every observed score as the
true population score plus measurement error, and as a rule of thumb, the
smaller the sample the bigger the error [[2021-05-23_true-score]]. That error
becomes visible in the confidence interval, whose width is driven primarily by
sample size: 50% of 10 participants means 50% ± 26%, whereas 50% of 100 means
50% ± 10% [[2021-05-23_true-score]], [[2021-06-27_confidence-interval]].

## Practice

### Match the number to the study type

- The 5-user guideline applies to qualitative issue identification only; 40+ is
  the quantitative figure. There is no contradiction between them, because a
  qualitative study does not collect metrics
  [[2021-07-11_5-test-users-qual-quant]].
- Qualitative studies aim to find problems, and any issue a participant hits is
  valid to fix regardless of how often it occurs — as the article puts it, one
  person falling into a pothole is enough to know it needs fixing. What the
  study produces is a list of problems; prioritising among them is the
  researcher's judgement call, not a frequency count
  [[2021-07-11_5-test-users-qual-quant]].
- Quantitative studies aim to predict population behaviour — success rates, task
  times, satisfaction — and small samples there produce wide, useless confidence
  intervals [[2021-07-11_5-test-users-qual-quant]].

### Where "5 users" comes from, and when it breaks

The guideline rests on three assumptions: the goal is identifying issues, any
issue encountered is worth fixing, and the probability of a given user
encountering a given issue is 31%. That 31% is a 1990s average; more mature
interfaces have lower encounter probabilities, and applying the
Nielsen–Landauer formula at 10–20% probability calls for 9–18 users rather than
5. The deeper justification is economic: the peak gain-to-cost ratio still tends
to fall around 5 participants in iterative testing cycles, and that ROI is
robust to reasonable variation in assumptions. Practically, test with 5, fix what
you find, then repeat; if the first test yields few insights, add users; if it
yields plenty, fix before testing again [[2021-07-11_5-test-users-qual-quant]].

### Quantitative sizing

- 40 participants is the default recommendation for quantitative studies
  estimating binary metrics such as success or conversion rates
  [[2021-07-25_summary-quant-sample-sizes]].
- That number is a calculation, not a law. It assumes a population above 500, a
  15% margin of error and a 95% confidence level; change the assumptions and the
  number changes [[2021-07-25_summary-quant-sample-sizes]].
- Accepting more risk is cheaper: moving to a 20% margin of error and a 90%
  confidence level drops the requirement from 40 to 28
  [[2021-07-25_summary-quant-sample-sizes]].
- Continuous metrics (task time, satisfaction) depend on population variability;
  with Nielsen's estimate of a standard deviation at 52% of the mean, 47 users
  are typically needed for 95% confidence and a 15% margin of error
  [[2021-07-25_summary-quant-sample-sizes]].
- On a tight budget, start with 20–25 participants, compute the resulting margins
  of error, and add participants if precision is insufficient — which requires
  analysing fast enough not to compromise study validity
  [[2021-07-25_summary-quant-sample-sizes]].
- Both under- and over-sampling are failures: too few and the results are not
  statistically reliable, too many and the money is wasted
  [[2021-07-25_summary-quant-sample-sizes]].

### Sample size, confidence intervals and confidence level

- Sample size is the primary driver of confidence-interval width, but not the
  only one: variability in the sample widens intervals independently of size for
  continuous metrics, and a higher confidence level widens them too
  [[2021-06-27_confidence-interval]].
- Choose the confidence level by what is at stake. 95% is the scientific
  standard; UX can drop to 80% for less critical decisions, buying narrower
  intervals at a 20% risk of being wrong. Critical interfaces such as a plane
  dashboard justify 95% or more; low-stakes tasks do not
  [[2021-06-27_confidence-interval]].
- Certainty is expensive in participants: reaching a 95% interval as narrow as an
  80% one requires substantially more people, upwards of a 40% increase
  [[2021-06-27_confidence-interval]].

### Interviews: saturation instead of formulas

- Interview sample size cannot be set statistically. The target is saturation —
  the point where emerging themes are fleshed out enough that more interviews
  would not change them [[2021-10-31_interview-sample-size]].
- Five is often too few for interviews. Interviews explore experiences and needs
  rather than interface issues, so the information collected varies more and
  saturation sits higher than for user tests. Academic sample sizes range from 5
  to 95, with 20–30 a common estimate
  [[2021-10-31_interview-sample-size]].
- Scope and population diversity drive it most: broad exploratory research on a
  diverse population needs more interviews than narrow research on a homogeneous
  one. Interviews on general healthcare access might need 20–30; interviews on
  one specific disease treatment might need only 5
  [[2021-10-31_interview-sample-size]].
- Secondary factors: experienced interviewers extract more, participants with
  domain expertise share more, and semi-structured interviews with consistent
  questions saturate faster than unstructured conversations
  [[2021-10-31_interview-sample-size]].
- The operating procedure is the same as elsewhere: recruit 5–6, analyse as you
  go, keep recruiting until themes stabilise, and give stakeholders a range for
  budgeting [[2021-10-31_interview-sample-size]].

### Reporting honestly at any sample size

- Never report numbers from a sample-based study without confidence intervals and
  statistical significance, and state explicitly whether the result generalises
  to the population or is specific to the study
  [[2021-05-23_true-score]].
- Statements like "70% of users completed the task" from a qualitative study are
  misleading because they present an observed score as if it carried no
  measurement error [[2021-05-23_true-score]].
- Sample size is not the only source of noise in qualitative work: deliberate
  protocol variability — facilitator flexibility, differing interventions,
  adjusted tasks — adds error on top of it [[2021-05-23_true-score]].
- Narrower confidence intervals carry more information, and quantitative studies
  should always be striving for them [[2021-06-27_confidence-interval]].

## Sources (5)

- [[2021-05-23_true-score]] — Small samples (5-10 people) produce large measurement errors where personal context and noise overwhelm signal; larger samples allow noise to cancel out.
- [[2021-06-27_confidence-interval]] — Primary driver of confidence interval width; larger samples produce narrower, more informative intervals.
- [[2021-07-11_5-test-users-qual-quant]] — Different studies require different sizes based on goals; issue identification needs fewer users than metric prediction.
- [[2021-07-25_summary-quant-sample-sizes]] — Sample size in quantitative studies is determined by acceptable margin of error, confidence level, and the metric type (binary or continuous); the appropriate size balances statistical reliability against research budget.
- [[2021-10-31_interview-sample-size]] — Unlike quantitative studies, interview sample size cannot be determined by statistical formulas but must be driven by saturation.
