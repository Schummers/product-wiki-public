---
type: concept
name: Task Design
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Task Complexity"
---

# Task Design

## Definition

The sources use "task" in two connected senses. The first is the research sense:
a task is the instruction given to a participant about what to do in a study, and
its craft is writing instructions that reflect the research goal without biasing
the participant [[2018-01-21_test-tasks-quant-qualitative]]
[[2017-04-09_better-usability-tasks]]. The second is the analytical sense: a task
is any observable activity with a start and an end point, performed by a user to
reach a goal, and distinct from the goal itself
[[2020-09-20_task-analysis]] — a design that solves the wrong problem, meaning
one that does not support users' actual tasks, fails whatever the quality of its
UI.

The two senses meet at complexity. How many steps and decision points a task
requires predicts where it succeeds: intelligent assistants handle simple
single-step tasks and fail on multistep, multitask or research-oriented ones
[[2018-09-16_intelligent-assistants-poor-usability-high-adoption]], and users
themselves route tasks by complexity, deferring difficult or high-stakes ones to
larger devices [[2019-08-25_large-devices-important-tasks]].

## Practice

### Match the task to the method

[[2018-01-21_test-tasks-quant-qualitative]] is explicit that a task perfect for a
qualitative study would not work at all for a quantitative one. Quantitative
tasks must be narrow, focused and specific enough that every participant
interprets them identically, with a single success criterion — multiple criteria
make partial success ambiguous and contaminate the metrics — because ambiguity
produces variability and therefore meaningless data. Quantitative studies should
also supply dummy data such as fake login credentials, so every participant
enters the same thing and nobody hesitates over sharing personal information.
Qualitative tasks, by contrast, may be open-ended, and changing them mid-study is
acceptable when a better understanding emerges: flexibility is a feature, not a
failure.

### Start from the user's goal, not from the feature

[[2017-04-09_better-usability-tasks]] frames the underlying principle as writing
tasks that reflect real-world user goals rather than internal system thinking:
consider the user's end goal rather than the task's end goal, and ask why someone
would use the section or feature at all instead of pointing at it.
[[2018-01-21_test-tasks-quant-qualitative]] adds that realism should be sourced,
not invented — from user interviews, search logs, analytics and customer-service
calls rather than designer assumptions — because forcing participants to do
something they would not do in real life measures something irrelevant to the
project.

### Do not prime, do not pre-position

Removing the interface's own vocabulary from the task is the most repeated rule
in this corpus. [[2017-04-09_better-usability-tasks]] warns that using exact UI
words tests reading comprehension rather than navigation and labelling;
[[2018-01-21_test-tasks-quant-qualitative]] gives the same rule for both
methodologies; [[2020-02-09_user-testing-stepped-tasks]] adds that matching
terminology artificially inflates success and masks real discoverability
problems.

The same logic extends to the starting point.
[[2016-03-06_feature-user-test]] argues against sending participants straight to
the page under test: getting to a feature is a major part of using it, and
navigation is often the biggest hindrance to its use. A study of embedded
calculators found 36% of task failures occurred during navigation rather than
interaction — a finding that would have been missed with a narrow scope. Being
pre-positioned also removes the skeptical judgement real users apply on arrival,
since in real life no bell rings when users reach the right page. When
pre-positioning is unavoidable, the article recommends bookmarks renamed to
neutral labels, as long URLs invite typing errors and search shortcuts introduce
result-selection bias.

### Ten wording mistakes to avoid

From [[2017-04-09_better-usability-tasks]], whose central claim is that bad
instructions bias participants and change the outcome of the study:

- Never reuse interface language.
- Do not tell users what to do — let steps such as registration or downloading be
  discovered, so their surprise or annoyance is observable.
- Keep tasks timely; outdated dates and events make the task feel unrealistic.
- Make tasks require effort: users should process information, not merely locate
  it.
- Avoid elaborate scenarios; brief context can clarify, but a backstory long
  enough to justify the task is a signal the task is unrealistic.
- Use user-centric language, not marketing phrases, business jargon, corporate
  acronyms or internal terminology.
- Avoid emotional or offensive content: specific relationships, jokes, famous
  names, politics, health, religion, money.
- Phrase as imperatives, not questions — "Find X" rather than "How would you find
  X" — because the goal is to observe behaviour, not collect a hypothetical.

### Stepped tasks for discoverability

[[2020-02-09_user-testing-stepped-tasks]] proposes related tasks with
progressively more specific instructions: a broad, deliberately vague first step,
then micro hints if the participant struggles. Completing step one unaided shows
the feature is discoverable; needing the later steps localises the problem. The
article separates three things the sequence reveals in order — discoverability
(does the user realise the feature exists), findability (can they locate it when
they know it exists), and usability (can they use it effectively). It also
defends the practical rhythm: handing over a written task reinforces that the
session is observation rather than conversation, keeps the facilitator from
helping too early, and pre-writing the steps avoids the poor task design that
comes from improvising under time pressure. Given how expensive each participant
is, stepped tasks extract insight that a single focused task would never surface.
The general framing is walking the thin line between telling users too much and
too little.

### Pilot the wording

[[2018-01-21_test-tasks-quant-qualitative]] calls pilot testing critical: run the
wording past 1-2 representative users before the main study, which routinely
exposes ambiguities, missing details and unrealistic scenarios that the formal
study would otherwise have inherited.

### Analysing the tasks users actually perform

[[2020-09-20_task-analysis]] describes task analysis as learning how users work
in order to achieve their goals, a practice inherited from instructional design
and human factors, and distinguishes it from job analysis (roles over time) and
workflow analysis (work spread across several people). Goals are what users want
to accomplish (set up a retirement fund); tasks are the activities that serve
them (search for deals, consult an advisor, fill in an application), and several
tasks usually serve one goal.

It runs in two stages. Stage one gathers information through contextual inquiry,
critical-incident interviews, record keeping or diary studies, activity sampling,
and simulations where the analyst walks through the user's steps. Stage two
structures those observations by order, hierarchy, frequency and cognitive
demand, and produces a diagram — most commonly a hierarchical task analysis
starting from the goal and scenario, breaking major operations into subtasks and
capturing plans (which steps happen in which order, which are optional). Depth
depends on complexity and the granularity wanted. Tasks are then analysed for
number, frequency, cognitive complexity, physical requirements and time taken,
with areas for design improvement noted. The article also observes that users do
not all reach a goal the same way: a novice may perform more tasks than an expert
who skips steps.

### Complexity determines where a task can live

[[2018-09-16_intelligent-assistants-poor-usability-high-adoption]] shows users
resolving a usability problem by restricting the tasks they attempt: 86% reported
single-action tasks against 26% for multistep ones, with virtually no multitask or
research activities. They stay with information retrieval, weather, music and
hands-free communication, where success rates are high, and hands-free value —
cited as the primary benefit by 35% of daily users, most often while driving —
outweighs the poor usability at that level of complexity. The article notes these
formative experiences teach users the assistants are not truly intelligent, which
may depress adoption of later improvements.

[[2019-08-25_large-devices-important-tasks]] finds the same routing behaviour
across devices, from a diary study of 50 participants covering 492 activities.
Desktop activities were rated more important than mobile ones (4.03 vs 3.61 out
of 5) while mobile activities were rated easier (4.52 vs 3.96) — and the article
interprets the second figure as a consequence of the first, not as evidence of
better mobile usability: users solve their easier problems on phones and defer
the harder ones to a full-size computer. Screen real estate, text input and
one-window-at-a-time workflows are the named constraints, and perceived error
risk is why high-stakes tasks (taxes, healthcare, financial decisions) go to
larger screens. The design implication drawn is that mobile-first is not
universal: where an application supports high-importance activities, actual
mobile usage volume should decide the priority. Its closing condition is that
unless important tasks can be made easy and fail-proof, people will avoid doing
them on mobile.

## Sources (7)

- [[2016-03-06_feature-user-test]] — how to frame and stage tasks to elicit realistic user behavior.
- [[2017-04-09_better-usability-tasks]] — Core topic covering ten specific mistakes and how to avoid them, with emphasis on realistic wording, appropriate complexity, and participant well-being.
- [[2018-01-21_test-tasks-quant-qualitative]] — The craft of creating instructions for what users should do in research; requires understanding research goals and methodologies; mistakes in task design undermine research validity.
- [[2018-09-16_intelligent-assistants-poor-usability-high-adoption]] — the number of steps and decision points required; assistants handle simple single-step tasks well but fail on multistep, multitask, or research-oriented activities.
- [[2019-08-25_large-devices-important-tasks]] — Task complexity drives device choice more than device capabilities; users strategically defer complex or important tasks to appropriate devices.
- [[2020-02-09_user-testing-stepped-tasks]] — Details how to craft tasks that avoid priming users with UI terminology and provide progressive hints without giving away answers.
- [[2020-09-20_task-analysis]] — Understanding task sequences, subtasks, cognitive demands, and physical requirements helps designers create workflows and interfaces that support efficient and effective user performance.
