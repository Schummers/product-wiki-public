---
type: concept
name: Research Validity
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Fiabilité et Répétabilité"
  - "Measurement Error"
  - "Reliability and Repeatability"
  - "Research Rigor"
  - "Statistical Validity"
---

# Research Validity

## Definition

Research validity is whether a study actually measures the thing it claims to
measure, and whether what it finds holds outside the room where it was found. The
sources split it into two dimensions that must be held separately: a study has
**internal validity** if it does not favour or encourage any particular
participant response or behaviour, and **external validity** if the participants
and the setup are representative of the real-world situation in which the design
is used [[2021-02-14_internal-vs-external-validity]]. Validity is also distinct
from reliability, the reproducibility of results: a study with high reliability
and low validity is one where you get a really good measurement of the wrong
thing [[2021-02-14_internal-vs-external-validity]].

Underneath both dimensions sits measurement error. True-score theory holds that
any observed score from a sample differs from the true population score by an
error term, and that the observed score only predicts the true score when that
error is small — which it is not when the sample is 5 or 10 people, or when the
protocol varies between sessions [[2021-05-23_true-score]]. Confidence intervals
are the way that error is made visible, and their width is driven by sample size,
by variability between participants, and by the confidence level chosen
[[2021-06-27_confidence-interval]]. Crucially, the sources insist that validity is
not a single scale on which qualitative research scores badly: quantitative
studies require statistical validity through narrow confidence intervals, while
qualitative studies require a different kind of validity in the logic of issue
identification [[2021-07-11_5-test-users-qual-quant]], and qualitative rigor has
its own established criteria — credibility, transferability, dependability,
confirmability — that emerge from systematic methodology rather than from sample
size [[2021-08-01_qualitative-rigor]]. One source in this corpus uses the same
vocabulary for interfaces rather than studies, calling repeatability the property
that a given input produces the same output every time — an area where
conventional clicks often beat natural-language input, since the same sentence
does not guarantee the same response on each iteration
[[2024-05-21_329_Interface_IA_langage_naturel,_la_solution_idéale]].

## Practice

### Internal validity: design the study so it cannot bias the answer

A study loses internal validity when its own design favours certain responses.
The named threats are confounding variables (time of day, differences between
facilitators, protocol changes mid-study) that produce results not reflecting
reality; task order effects; and facilitator style. The remedies are
randomization and counterbalancing: random task order, warmup tasks, and
randomized condition order such as which site participants see first
[[2021-02-14_internal-vs-external-validity]].

The same threats reappear at analysis time under different names. Comments and
actions introduced without facilitator cueing are more genuine than those elicited
by priming or leading questions — revealing the study's purpose or naming a UI
element in a question contaminates what follows. Order effects, overly complex
task instructions and fatigue are confounds that shape validity and must be
factored into interpretation, not discovered afterwards
[[2025-04-11_usability-data-in-analysis]].

### External validity: representative people, representative setup

External validity requires participants who match the target audience in
demographics, goals and motivation. Proxy users — people pretending to be in a
situation they are not in — lack authenticity. The setup matters as much as the
people: testing mobile designs on desktop, or in a lab rather than the field,
moves the study away from natural use conditions
[[2021-02-14_internal-vs-external-validity]].

Screening is the operational lever. A screener is a set of questions establishing
that a prospective participant is a good fit, and its purpose is precisely to
ensure findings are valid and relevant to the product rather than invalidated by
unsuitable participants [[2024-11-01_screening-participants]]. Practical rules:
define inclusion and exclusion criteria around the behavioural and demographic
characteristics most critical to the research questions instead of chasing a
perfect participant; ask about relevant past behaviours rather than hypothetical
future ones, because users are unreliable at predicting future behaviour; avoid
yes/no questions, which are easy to game; and pilot the screener before launch
[[2024-11-01_screening-participants]].

Recruitment sources carry their own bias. Volunteer research panels skew toward
IT professionals and other web-savvy individuals, which screeners help counteract
[[2024-11-01_screening-participants]]. Internal panels degrade in three
predictable ways — static participant data, panel-sampling bias where loyal
customers create a positive echo chamber that excludes new users and edge cases,
and business misalignment as the company enters new markets — so panels stay valid
only through audits, rotation practices and periodic strategic review
[[2026-04-24_user-panels-fail]]. Misrecruitment of professional participants or
coworkers is one of the six dimensions to weigh when judging whether a data point
is appropriate [[2025-04-11_usability-data-in-analysis]].

### Sampling: convenience versus probability

Convenience sampling — nonrandom selection of participants who are readily
available — is the UX default, and legitimately so: it is fast, cost-effective and
sufficient for qualitative usability testing, exploratory research and iterative
feedback, because most studies aim to find usability problems rather than make
statistically rigorous generalizations. Probability sampling, based on random
selection so that everyone in the population has a known chance of inclusion,
reduces bias and increases external validity, but demands a well-defined
population, a complete contact list, a random selection method and larger samples
(40+ for quantitative usability testing, 100+ for surveys)
[[2025-04-18_convenience-vs-probability-sampling]].

Two warnings follow. Quotas are not randomness: restricting a convenience sample
to, say, five users per age group still leaves hidden biases (emotional state,
cultural influences, interest in participating) that skew results. And probability
sampling should be reserved for cases that justify it — inferring prevalence in a
broader population, highly diverse user bases where recruitment bias would skew
results, high-stakes domains such as healthcare, finance and automotive, or
statistical comparisons between groups
[[2025-04-18_convenience-vs-probability-sampling]].

### Numbers: measurement error, confidence intervals, significance

Never report numbers from a sample-based study without doing the math. Calculate
confidence intervals and statistical significance to see how well observed scores
predict true scores, and state explicitly whether results generalize to the
population or are specific to the study
[[2021-05-23_true-score]]. The magnitudes are the argument: 50% of 10 participants
means 50% ± 26%, a range of 24–76%, while 50% of 100 participants means 50% ± 10%,
a range of 40–60% [[2021-05-23_true-score]]. P-values below 0.05 indicate a
difference is real rather than measurement noise [[2021-05-23_true-score]].

Three factors set the width of a confidence interval: sample size (larger samples
narrow it), variability between participants on continuous metrics such as task
time (higher variability widens it, independently of sample size), and the
confidence level chosen (95% is wider than 80%). The confidence level is a
deliberate, cost-bearing choice: matching an 80% interval's width at 95%
confidence requires substantially more participants — a 40%+ increase — so pick it
from the stakes. Critical interfaces such as a plane dashboard warrant 95% or
above; a low-consequence task such as resetting a video system can accept 80% and
its 20% risk of being wrong [[2021-06-27_confidence-interval]].

Qualitative studies add a second source of noise on top of sample size: they
deliberately allow facilitator flexibility, different interventions and protocol
adjustments between sessions, so their observed numbers are noisier still
[[2021-05-23_true-score]]. Note that the sources do not treat this as a reason to
distrust qualitative research as such — only as a reason not to report metrics
from it (see below).

### Qualitative validity is a different construct, not a weaker one

The 5-user guideline and the 40+ rule are not in contradiction, because you do not
collect metrics in a qualitative study. Qualitative studies identify usability
problems, and an issue is valid regardless of how many participants hit it;
quantitative studies predict population behaviour and need large samples for
narrow confidence intervals [[2021-07-11_5-test-users-qual-quant]]. The 5-user
figure rests on three assumptions — that the goal is issue identification, that
any issue someone encounters is worth fixing, and that the probability of
encountering an issue is 31% — and the third is contestable: 31% is a 1990s
average, and better interfaces have lower encounter probability, so a 10–20%
probability implies 9–18 users under the Nielsen–Landauer formula. What survives
the challenge is the ROI argument: peak gain-to-cost ratio still typically lands
around five participants in iterative cycles
[[2021-07-11_5-test-users-qual-quant]].

Qualitative rigor has explicit criteria: credibility (accurate observation),
transferability (applicability in other contexts), dependability (consistent
findings) and confirmability (reduced bias). They are produced by systematic
process — evidence-based theoretical frameworks, specific research questions,
careful participant sampling, open-ended facilitation, systematic coding using
inductive reasoning, and triangulation — not by sample size
[[2021-08-01_qualitative-rigor]]. Theoretical grounding is itself a validity
argument: a finding that exemplifies a known principle (Nielsen's heuristics,
cognitive psychology, HCI principles) is trustworthy regardless of how many people
exhibited it [[2021-08-01_qualitative-rigor]].

### Assess each data point in context

No single comment or behaviour tells the full story. Six dimensions govern whether
a data point can be trusted: authenticity (was the response natural, or motivated
by a desire to please the facilitator, by framing, or by professional-participant
status), consistency (verbal against behavioural data, and repetition across
sessions), repetition, spontaneity (unprompted versus primed), appropriateness
(was this participant and this task representative and realistic), and confounds.
When what participants say contradicts what they do — claiming a task was easy
after struggling, erring and restarting — prioritize the behavioural data. Each
data point must be assessed against other data points and paired with information
about recruitment strategy, study design and facilitation events
[[2025-04-11_usability-data-in-analysis]].

### Triangulate, in proportion to the stakes

Every method is limited: qualitative studies lack statistical proof and have small
samples, quantitative methods lack context and meaning. Triangulation — examining
the same question through multiple sources or methods — mitigates one method's
limitations with another's data and enhances credibility
[[2021-02-21_triangulation-better-research-results-using-multiple-ux-methods]].
The investment should scale with the decision: small, reversible decisions need
only a few hours checking existing data, while expensive and hard-to-reverse
decisions warrant robust triangulation mixing qualitative, quantitative and
external analysis. Everyday forms include checking survey data against analytics,
running qualitative research after a quantitative finding, and consulting support
records when analytics show high error rates. Teams whose members are experienced
in several methods can triangulate without slowing the development pace
[[2021-02-21_triangulation-better-research-results-using-multiple-ux-methods]].

This sits alongside the same risk-proportionality logic found in the confidence
level [[2021-06-27_confidence-interval]] and the sampling decision
[[2025-04-18_convenience-vs-probability-sampling]]: how much validity to buy is a
function of what the decision costs to get wrong.

### When validity must be sacrificed, say so

Perfect validity is sometimes unaffordable. Neither internal nor external validity
errors are unavoidable, but when one must be sacrificed — paper prototyping
instead of a working build, for cost reasons — the results must be interpreted
accordingly: as a best-case scenario, or as a laboratory finding that needs
retesting in the field [[2021-02-14_internal-vs-external-validity]].

Transparency about confidence and limitations is presented as a professional
differentiator, not merely a methodological nicety. Where AI accelerates
transcription and tagging, what clients value is careful research design,
thoughtful interpretation, transparency about confidence, and human validation —
rigor is what distinguishes trustworthy work from corner-cutting
[[2026-02-13_ux-consulting-ai]]. Consistently, one source argues that AI cannot yet
reliably analyse usability test data because it misses the recordings, the context
and the study-design factors that determine whether a data point is valid at all
[[2025-04-11_usability-data-in-analysis]].

## Sources (12)

- [[2021-02-14_internal-vs-external-validity]] — defines internal and external validity as separate but complementary dimensions of study quality.
- [[2021-02-21_triangulation-better-research-results-using-multiple-ux-methods]] — shows how triangulation increases validity by examining questions from multiple perspectives and verifying findings across sources.
- [[2021-05-23_true-score]] — The difference between observed scores and true population scores, larger in small-sample studies and qualitative studies with protocol variability.
- [[2021-06-27_confidence-interval]] — Difference between observed and true scores; larger in small samples and studies with high variability.
- [[2021-07-11_5-test-users-qual-quant]] — Quantitative studies require statistical validity through narrow confidence intervals; qualitative studies require logical validity in issue identification.
- [[2021-08-01_qualitative-rigor]] — Qualitative rigor is established through credibility (accurate observation), transferability (applicable in other contexts), dependability (consistent findings), and confirmability (reduced bias); rigor emerges from systematic methodology, not sample size.
- [[2024-05-21_329_Interface_IA_langage_naturel,_la_solution_idéale]]
- [[2024-11-01_screening-participants]] — Emphasizes that screeners are essential for ensuring research findings are valid and relevant to the product, preventing data from being invalidated by unsuitable participants.
- [[2025-04-11_usability-data-in-analysis]] — articulates how methodological factors (priming, leading questions, order effects) compromise data quality and must be considered during analysis.
- [[2025-04-18_convenience-vs-probability-sampling]] — describes how probability sampling reduces bias and increases external validity through random selection and stratification techniques.
- [[2026-02-13_ux-consulting-ai]] — Rigor—thoughtful study design, careful interpretation, transparency about confidence—distinguishes trustworthy consultants from those cutting corners with AI acceleration.
- [[2026-04-24_user-panels-fail]] — Panels maintain research validity only when they remain representative of the target population; misaligned or biased panels produce unreliable findings that undermine research integrity.
