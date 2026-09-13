---
type: concept
name: Study Design
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Diary Study Design"
  - "Research Design"
---

# Study Design

## Definition

Study design is the set of decisions made before data collection that determine
what a study can legitimately conclude: which method to use, who participates,
what tasks or questions they are given, and how the session is structured and
run [[2024-11-01_pm-research-plan]]. The sources treat these decisions as
inseparable from validity. A study has internal validity when its design does
not favour any particular participant response, and external validity when the
participants and the setup represent the real-world situation the design is used
in [[2021-02-14_internal-vs-external-validity]]. Design choices as ordinary as
task order, facilitator style, testing environment, or the wording of a
demographic question are what create or destroy those two properties.

Design is also what makes a study's data interpretable afterwards. Analysis
cannot take a single comment or behaviour at face value: each data point has to
be read against the recruitment strategy, the study design, and what happened
during facilitation [[2025-04-11_usability-data-in-analysis]]. The methods
themselves are described as easy; the return on a research investment comes from
the preparation around them [[2016-04-17_usability-test-checklist]].

## Practice

### Start from goals, then choose a format

Meet stakeholders first to identify the specific questions and concerns the
study must answer, and resist overcommitting: additional goals degrade the
quality of insight on the primary ones. Only then choose the format — in-lab vs.
field, moderated vs. unmoderated, in-person vs. remote — based on constraints and
on how critical it is to observe the real context of use
[[2016-04-17_usability-test-checklist]]. A research plan documents all of this
(purpose and goals, participants, method and procedure, supporting documents);
the planning act itself is what surfaces details that would otherwise be missed
[[2024-11-01_pm-research-plan]].

### Do not blend qualitative and quantitative structures

Qualitative and quantitative studies differ in sample size, task
standardisation, and facilitator latitude, and blending them produces
meaningless data: qualitative work identifies problems with roughly five
participants and flexible tasks, quantitative work estimates population metrics
with 40+ participants and standardised tasks
[[2021-06-13_metrics-qualitative]]. The planning checklist gives the same split
with a different quantitative floor — 5 participants for qualitative studies,
20-30+ for quantitative ones [[2016-04-17_usability-test-checklist]]. Metrics
collected inside a qualitative study may be reported anecdotally as individual
values, never as averages or success percentages
[[2021-06-13_metrics-qualitative]].

Combining the two is legitimate when it is designed as such from the start.
Mixed-methods research aligns both strands under one overarching question, in
one of three patterns: explanatory sequential (quantitative first, qualitative
to explain), exploratory sequential (qualitative first, quantitative to test),
or convergent parallel (both at once, independent but complementary). The value
lies in integration rather than addition, and it costs more time, more
protocols, and closer coordination [[2025-07-25_mixed-methods-research]]. Where
confounds are too hard to control quantitatively, one source recommends
switching to qualitative exploratory work instead
[[2023-09-24_confounding-variables-quantitative-ux]].

### Protect internal validity: order, facilitator, environment

Randomise or counterbalance the order in which participants meet conditions, use
warm-up tasks, and control facilitator style and protocol so nothing in the
setup pushes participants toward a response
[[2021-02-14_internal-vs-external-validity]]. Confounding variables — unmeasured
factors affecting both conditions and outcomes — are the mechanism behind this:
time of day, fatigue and learning effects, age, seasonality, market shifts,
prior product experience, or preexisting opinions. Either structure the study to
avoid them, or measure them so they can be controlled for in analysis; a
within-subjects design in particular needs randomised or counterbalanced order
[[2023-09-24_confounding-variables-quantitative-ux]]. Order effects, overly
complex task instructions, and fatigue also resurface at analysis time as
"confounds" to weigh against each data point
[[2025-04-11_usability-data-in-analysis]].

### Protect external validity: real users, real conditions

Participants must match the target audience in demographics, goals, and
motivation; proxy users who have to imagine themselves in a situation lack
authenticity and invalidate results, especially on specialised or content-rich
sites [[2021-02-14_internal-vs-external-validity]],
[[2016-04-17_usability-test-checklist]]. The setup must replicate real
conditions too — testing a mobile design on desktop, or in a lab rather than the
field, reduces external validity. When validity has to be sacrificed for cost
(paper prototyping, for instance), the results should be read as best-case or
laboratory findings needing field retesting
[[2021-02-14_internal-vs-external-validity]]. Misrecruitment such as
professional participants or coworkers undermines the appropriateness of the
data and limits how far insights generalise
[[2025-04-11_usability-data-in-analysis]].

### Write tasks that do not lead

Tasks should be concrete, matched to the study goals, and free of clues that
prime behaviour; exploratory (open-ended) tasks and specific (defined endpoint)
tasks serve different purposes [[2016-04-17_usability-test-checklist]].
Scenarios that feel familiar rather than novel reduce the pressure participants
feel to perform for the researcher
[[2023-05-21_hawthorne-effect-observer-bias-user-research]]. At analysis time,
spontaneity is a dimension of data quality: actions and comments produced
without facilitator cueing — no revealing of the study purpose, no naming of UI
elements in questions — are more genuine than primed ones
[[2025-04-11_usability-data-in-analysis]]. Run a pilot with one or two
participants to test task wording, timing, recruitment criteria, and setup
before formal sessions [[2016-04-17_usability-test-checklist]].

### Design against observer effects

People change behaviour when they know they are watched, across field studies,
usability tests, surveys, and diary studies. Mitigations are method-specific:
build rapport and a judgement-free environment in field studies (participants
return to default behaviour once comfortable); state explicitly that the design
is being tested and not the participant, and that honest feedback is wanted;
use indirect questioning in surveys on sensitive topics; explain in diary
studies why responses matter and show what changed as a result
[[2023-05-21_hawthorne-effect-observer-bias-user-research]]. Elimination is
impossible; awareness and intentional design reduce the impact. Analysis should
then flag responses that look motivated by a wish to please the facilitator, and
prioritise behavioural data when what participants say contradicts what they do
[[2025-04-11_usability-data-in-analysis]].

### Plan for no-shows and attrition

Roughly one in nine recruited users fails to show up
[[2019-04-28_usability-testing-minors]]. Overrecruiting is framed explicitly as
buying insurance, with three models: one floater per participant (most
expensive, lowest risk), one floater per two participants (moderate on both),
and extra sessions (cheapest but slowest — 1.5 days instead of 1 for five
users). Time-constrained projects favour floaters; flexible schedules favour
extra sessions; remote unmoderated research needs only about one extra per three
sessions. Floaters are screened with the same criteria, told honestly what their
role is, paid, and dismissed without implying they did anything wrong
[[2020-10-04_recruit-backup-users-in-research]]. Sessions with minors warrant
extra participants as well, since both parent and child affect attendance
[[2019-04-28_usability-testing-minors]].

### Longitudinal designs: diary studies

Diary studies fail through forgetfulness, waning interest, fatigue, and dropout,
so the design variables are engagement variables. Screen for commitment by
stating the time cost in recruitment materials and asking open-ended questions
about willingness and writing comfort; choose a tool matching the participant's
primary device and pilot it; run a pre-study brief covering the tool, the
procedure, what a helpful entry looks like, the incentives, and withdrawal
conditions; keep entries under 15 minutes; maintain regular contact and
reminders without flooding participants
[[2023-01-29_better-diary-studies]].

Incentives are a design decision of their own, because diary studies compensate
effort rather than time. Three structures: paying for a minimum number of
entries (simplest, but participants submit exactly the minimum and may cluster
entries at the start or end), pay-per-entry (motivates more submissions, suits
effortful entries like video or photo, risks low-effort or fabricated
submissions), and tiered pay-per-entry (different rates for different entry
types, encourages targeted behaviour, needs more explanation and tracking).
Bonuses can reward consistency, completeness, or responsiveness. Cadence
matters as much as amount: lump-sum end-of-study payment suits shorter studies,
regular weekly or biweekly payments combat attrition in longer ones at the cost
of administrative work. There is no single best structure — the right one is the
one that fits the study's priorities and the data needed
[[2026-06-19_diary-study-incentives]]. The engagement-focused source agrees on
the direction, recommending interval payments over a single end-of-study payment
and warning that a reward perceived as too much work for its value causes
dropout [[2023-01-29_better-diary-studies]].

### Designing what you ask about participants

Collect only demographics whose use you can justify — unnecessary questions
lengthen surveys, raise sensitivity, and lower response rates. Use broad
response ranges (10-15 year bands rather than 45-50) unless developmental
differences justify narrower ones, always offer "Prefer not to say", use
inclusive and current language around gender, rethink the "Other" option, allow
"Select all that apply" for race and gender, and place demographic questions at
the end of a survey — unless they are screening criteria, which must come early
[[2022-11-27_demographics-in-ux]]. A research plan should state inclusion and
exclusion criteria explicitly, and should avoid personally identifiable
information by using participant codes (P1, P2)
[[2024-11-01_pm-research-plan]].

### Designing the session's questions and flow

[[2016-11-04_ux-research_03-chapter-2-good-research-starts-with-good-questions]]
treats the shape of a session as a set of deliberate design choices: the flow
of questions, the balance between openness and guidance, how far to follow a
rabbit hole versus staying on topic, and the progression of a conversation
from comfort to depth. Each question is built from a setup (what, why, how,
when, where), an area of inquiry, laddering (follow-up probes for deeper
detail) and a segue to the next question, and every question should tie back
to the research objectives or be cut. Four pitfalls to design against: leading
questions, shallow yes/no questions, personal bias, and unconscious bias —
though once a guide is practiced, the chapter notes these can be broken
deliberately, for instance a leading question used to build trust.

### Choosing a method as a design constraint

[[2016-11-04_ux-research_06-chapter-5-choosing-your-methods]] treats method
choice as upstream of study design: once a method is selected on the
strength of the questions, stakeholder needs, sample size, location, and the
time/budget/scope trade-off (the project triangle), the chapter's design
advice is to keep each session focused on a specific goal and, when multiple
distinct questions are in play, to run them as separate research tracks
rather than force one session or one method to answer all of them.

### Designing the participant pool: profiles, screeners, quotas

[[2016-11-04_ux-research_08-chapter-7-recruiting]] treats participant
selection as a study-design decision with its own quotas and criteria:
baseline user profiles and behavioral demographics (not just age and income)
define who counts as in-scope, a screener survey of 10-15 minutes confirms or
disqualifies candidates, and — assuming participant availability is not an
issue — qualitative studies are designed around three to five participants
per user profile, adjusted by how important that profile is and how hard it
is to reach. The chapter frames avoiding bias in recruitment (screening
properly rather than assuming "everyone is a user" or recruiting convenient
contacts) as part of the same design decision as the quota itself.

### Adapting the protocol to the population

Testing minors (ages 3-17) changes nearly every design parameter. Segment by
maturity and interest rather than age alone, since the gap between a 7- and a
17-year-old dwarfs the gap between a 37- and a 47-year-old. Keep sessions short
with breaks (60 minutes for ages 3-12, up to 90 for teenagers), prepare more
tasks than needed and vary their type to counter boredom, use age-appropriate
incentives such as gift cards, small toys, or stickers alongside cash that
parents may control, and design an environment that is child-friendly yet free
of distractions. Facilitators should dress casually, be warm, and use generic
praise — a poker face makes young children quieter and think-aloud harder to
elicit [[2019-04-28_usability-testing-minors]].

### Write it down, and update it afterwards

Document the design in a test plan or research plan covering the product, goals,
logistics, participant profiles, tasks, metrics, and a description of the system
[[2016-04-17_usability-test-checklist]]. The method section should be detailed
enough for another researcher to replicate the study — session length, tools,
tasks, procedure — and the plan should be shared with stakeholders for buy-in,
paired with observer guidelines, and updated after the study to reflect what
actually changed during sessions [[2024-11-01_pm-research-plan]].

## Sources (16)

- [[2016-04-17_usability-test-checklist]] — Proper study design requires careful consideration of format, participant selection, task construction, and measurement approaches.
- [[2019-04-28_usability-testing-minors]] — Testing protocols for minors demand careful attention to environment (child-friendly but distraction-free), task realism, and facilitator demeanor.
- [[2020-10-04_recruit-backup-users-in-research]] — Different overrecruiting models suit different research scenarios. Time-constrained projects favor one-to-one floaters; flexible schedules favor extra sessions. Remote unmoderated studies can use lower overrecruit ratios than moderated studies.
- [[2021-02-14_internal-vs-external-validity]] — explains how design choices (task order, facilitator, participant recruitment, environment) affect study validity.
- [[2021-06-13_metrics-qualitative]] — Fundamental differences in sample size, task standardization, and facilitator flexibility distinguish qualitative from quantitative studies; blending creates invalid data.
- [[2022-11-27_demographics-in-ux]] — thoughtful demographic-question design respects participant privacy, uses inclusive and evolving language, and collects only information that directly shapes interpretation of results.
- [[2023-01-29_better-diary-studies]] — Diary study design significantly impacts completion rates; entry length, contact frequency, and incentive timing are critical design variables affecting participant engagement.
- [[2023-05-21_hawthorne-effect-observer-bias-user-research]] — The intentional structuring of research to minimize participant awareness, build comfort, use natural scenarios, and encourage authentic responses.
- [[2023-09-24_confounding-variables-quantitative-ux]] — Randomization, counterbalancing, and consistent testing environments are essential techniques to mitigate confounding variable effects.
- [[2024-11-01_pm-research-plan]] — the decisions about which research methods to use, who to recruit as participants, what tasks or questions to ask, and how to organize the research session for maximum learning.
- [[2025-04-11_usability-data-in-analysis]] — focuses on how task wording, session structure, facilitation approach, and confounding variables influence participant behavior and must be factored into analysis.
- [[2025-07-25_mixed-methods-research]] — The three research design patterns (explanatory sequential, exploratory sequential, convergent parallel) provide distinct frameworks for structuring mixed-methods projects.
- [[2026-06-19_diary-study-incentives]] — Diary studies require attention to attrition risk; incentive structure, payment timing, and clear participant communication are critical design elements.
- [[2016-11-04_ux-research_03-chapter-2-good-research-starts-with-good-questions]] — The structure of a research session—the flow of questions, the balance between openness and guidance, the management of rabbit holes versus staying on topic, and the progression of a conversation from comfort to depth—are deliberate design choices.
- [[2016-11-04_ux-research_06-chapter-5-choosing-your-methods]] — emphasized as an important consideration in research planning, recognizing that once methods are understood, practitioners should feel comfortable adapting approaches to their specific project needs while keeping sessions focused on specific goals
- [[2016-11-04_ux-research_08-chapter-7-recruiting]] — defining participant quotas, behavioral demographics, and screening criteria to ensure the participant pool matches research goals.
