---
type: concept
name: Qualitative Research
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Qualitative Research Analysis"
  - "Qualitative Research Methods"
  - "Quantitative and Qualitative Research"
---

# Qualitative Research

## Definition

Qualitative research is the family of methods that explores how and why things
happen, valuing depth of understanding over breadth
([[2018-01-21_test-tasks-quant-qualitative]]). It gathers insights about user
experience, expectations, mental models, and behavior through observation and
conversation, and its output is an explanation of why a problem occurs and how
to fix it, not a measurement of how many people it affects
([[2021-08-01_qualitative-rigor]]). In the two-dimensional map of
[[2022-08-21_guide-ux-research-methods]], it sits opposite quantitative research
on the why/how versus how-many axis, and spans both attitudinal methods
(interviews, focus groups: what people say) and behavioral ones (observation,
contextual inquiry, field studies: what people do).

The corpus is unanimous that qualitative is not a lesser or looser form of
quantitative work. [[2021-08-01_qualitative-rigor]] argues it is rigorous
data-driven inquiry rather than anecdote collection, with its own criteria of
credibility, transferability, dependability, and confirmability, and locates
rigor in systematic methodology rather than in sample size. The recurring
consequence across sources is that qualitative and quantitative answer different
questions and must not be blended or ranked: neither should automatically
override the other ([[2019-01-27_interpreting-research-findings]]).

## Practice

### Phases: planning, discovery, and validation

*UX Research* structures qualitative work into three phases. Initial planning
uses landscape analysis, surveying existing products that serve similar
functions or customer segments to reveal market gaps, and heuristic reviews,
evaluating designs against established best practices such as Jakob Nielsen's
10 usability heuristics. Discovery and exploration relies on contextual
inquiry: following participants and prompting them to "think aloud" about what
they are doing, run with as few as 5 or as many as 50 participants depending
on scope. Product testing and validation offers three variants: moderated
validation in a lab or workplace, where the researcher adjusts criteria and
asks probing questions on the fly; unmoderated remote validation through tools
such as UserTesting, where participants complete predefined tasks under audio
and screen recording; and remote moderated testing, combining real-time
interaction with digital communication tools. Participatory design — workshop
brainstorming, sketching exercises, and collaborative visual adaptation of
mental models with stakeholders and customers — can occur at any of these
phases ([[2016-11-04_ux-research_05-chapter-4-qualitative-research-methods]]).

The same source frames qualitative and quantitative research as equals rather
than opposites: the most successful projects combine both, since qualitative
supplies context and motivation while quantitative supplies scale, together
producing data-driven personas and customer journeys that account for task
time as well as human needs
([[2016-11-04_ux-research_05-chapter-4-qualitative-research-methods]]).

### Choosing qualitative, and choosing a method

[[2022-08-21_guide-ux-research-methods]] offers the selection framework: place
the question on two axes, attitudinal versus behavioral and qualitative versus
quantitative, and pick accordingly, since no single method answers every
question and attitudinal data is subject to social desirability bias. It
recommends combining methods across quadrants for most real questions.

*UX Research* devotes a full chapter to this choice and frames it as answering
a fixed set of questions rather than applying a formula: what questions need
answering, what stakeholders' goals are (validating an assumption, defining a
new market, proving organisational value each point toward a different
approach), what sample size and participant locations are realistically
available, and what budget and timeline apply. It generalises the sample-size
split into a "project triangle" of time, budget, and scope: identify which two
matter most and let the third vary. Location favours qualitative work
specifically, since it benefits when researchers can travel to participants in
their own environment — though the chapter notes global products can make
travel cost-prohibitive, and large-scale qualitative studies are common for
international products regardless; contextual inquiries specifically demand
90–120 minutes each, against quantitative measures that can run in a
"set-and-forget" mode such as ongoing analytics. Its rule for combining
methods is to identify a qualitative and a quantitative measure for the same
root question, rather than combining disparate methods or expecting one method
to serve unrelated goals — and, facing several distinct questions, to run
separate research tracks instead of forcing them into one method or session
([[2016-11-04_ux-research_06-chapter-5-choosing-your-methods]]).

The qualitative methods described across the corpus:

- **Interviews** — one-on-one conversations that surface first-hand experience,
  frustrations, and needs; in-person interviews with visual mapping help
  participants recall steps accurately ([[2019-02-10_research-journey-mapping]]).
  *UX Research* frames the strongest setup as a two-person team, a moderator
  conducting the conversation and a note taker capturing observations, since
  listening, formulating a response, and writing at the same time is very
  difficult for one person alone, and recommends framing the exchange as the
  participant teaching the researcher so the participant leads and chooses
  what to share ([[2016-11-04_ux-research_09-chapter-8-making-research-happen]]).
- **Field studies** — context research in the user's natural environment rather
  than a lab, revealing what happens amid distractions, noise, and concurrent
  activity. [[2024-01-12_field-studies]] distinguishes four types by researcher
  involvement: direct observation (fly on the wall), contextual inquiry
  (observation plus interview), customer-site visits (guided tour), and
  ethnography (full immersion). Most valuable in discovery, before design
  begins, though usable evaluatively as field testing. Remote moderated and lab
  research are the fallbacks when travel is costly, participants are dispersed,
  or the scenario cannot be observed ethically.
- **Diary studies** — self-reported interactions over days to months, collected
  remotely and asynchronously, for long-term experiences, habits, attitudes,
  behavioral change, customer journeys, and channel usage
  ([[2024-03-29_diary-studies]]). Three collection modes: event-based,
  interval-based, and signal-based. That source also covers the operational side:
  tool choice between all-in-one apps, survey tools, and messaging apps;
  incentives scaled to the time commitment (roughly $40/hour for US
  participants) and paid in installments at milestones to keep long studies
  alive; and recruiting with dropouts expected.
- **Cognitive mapping** — participants build a visual artifact from sticky notes
  and drawings to externalise a mental model that would be hard to say out loud
  ([[2019-08-11_cognitive-mapping-user-research]]). Suited to exploratory,
  complex, and participatory research. That source warns the method demands
  improvisation traditional interviews do not, and advises 2-3 practice sessions
  before a real one, plus a dedicated note-taker, video recording, and prepared
  materials.
- **Critical Incident Technique** — participants recall specific occasions when
  a behavior or event notably affected an outcome, positive and negative asked
  separately, usually starting with the positive
  ([[2020-01-26_critical-incident-technique]]). Formalised by Flanagan in 1954,
  usable through interviews, focus groups, or surveys. It beats generic
  "give me an example" questions because it anchors on consequential events, and
  it captures rare incidents across years that observation would never catch.
  Its stated limits are memory (fallible, sometimes stressful to search) and
  bias toward the extreme: everyday usage and small usability issues rarely
  surface. The same source concedes that observational research such as
  contextual inquiry or usability testing always teaches more about actual pain
  points.
- **Qualitative surveys** — open-ended questions used to generate rich feedback
  and, notably, to discover what the answer categories should be before a
  quantitative survey is written, avoiding closed questions invented in a
  conference room ([[2016-09-25_qualitative-surveys]]).
- **Qualitative usability testing** — running users through tasks to find
  problems rather than to measure performance
  ([[2021-07-11_5-test-users-qual-quant]], [[2021-06-13_metrics-qualitative]]).

For journey mapping specifically, [[2019-02-10_research-journey-mapping]]
prescribes a sequence: audit existing internal data first (past focus groups,
support logs, analytics, satisfaction scores), then run a multipronged
qualitative study combining interviews, field studies, diary studies, and
competitive analysis, then supplement with quantitative data for credibility and
magnitude. Its reason for not stopping at interviews is that what people say
they do is not always what they do, which is why interviews should be coupled
with field studies. It also rejects assumption-based maps: stakeholders lack
both the breadth and the depth to reconstruct the journey.

### Sample size: issue-finding versus saturation

Two distinct sizing logics run through the corpus, and the sources are careful
to keep them apart.

For usability testing, [[2021-07-11_5-test-users-qual-quant]] defends five
participants and explains why it is not in contradiction with the 40+ figure
quoted for quantitative work: you do not collect metrics in a qualitative study.
It exposes the three assumptions under the number (the goal is identifying
issues, any issue a user hits is worth fixing, and the probability of hitting a
given issue is 31%) and immediately questions the third: the 31% is a 1990s
average, and on a more mature interface where probability is 10-20%, the
Nielsen-Landauer formula calls for 9-18 users. Its defence of five is
economic rather than statistical: the gain-to-cost ratio peaks around five and
stays robust across reasonable parameter variation, inside an iterative
test-fix-retest cycle.

For interviews, [[2021-10-31_interview-sample-size]] states plainly that five is
often too few, because interviews explore experiences and needs, which vary more
than interface issues do. The governing concept there is saturation, the point
at which new interviews stop producing new themes. It reports academic sample
sizes ranging from 5 to 95 with 20-30 typical, and lists the factors that move
the point: scope breadth, population diversity, interviewer experience,
participant domain expertise, and structure (semi-structured reaches saturation
faster than unstructured). Its procedure is to start at 5-6, analyse as you go,
and recruit until themes stabilise, while giving stakeholders a range for
budgeting. [[2024-03-29_diary-studies]] applies the same saturation logic to
diary studies, quoting 5-50 depending on scope and user-group variance, and
defines saturation as the moment data becomes repetitive.

*UX Research* gives a similar generalist bracket, outside interviews
specifically: qualitative studies typically rely on 5–10 participants for
narrow projects and 20–40 for broader scope, smaller than the pools
quantitative research needs, though it notes smaller data sets can still
surface valuable insights
([[2016-11-04_ux-research_05-chapter-4-qualitative-research-methods]]).

### Rigor, and defending small samples

[[2021-08-01_qualitative-rigor]] locates rigor in the process: evidence-based
theoretical frameworks, specific research questions, careful sampling,
open-ended facilitation, systematic inductive coding, and triangulation. Its
argument for small samples is that a single observation exemplifying a known
usability principle is already credible data, and that quantifying how many
users hit a known hazard is wasted effort when the point is to fix it early. It
also treats empathy as a first-class output: engaging with real people builds
understanding of users as humans, which it ties to ethical design.

[[2019-02-24_responding-skepticism-small-usability-tests]] is the practical
companion, aimed at stakeholders who object to five users. Its tactics: explain
the methodology before testing rather than defending it afterwards, since
prevention beats rebuttal; get the team to observe sessions directly, because
watching a real user struggle carries more than a written report; recruit
genuinely representative participants and share the screening criteria in
advance; refuse to discount single-user findings, weighing fix cost, severity,
competitive comparison and usability theory instead of frequency; corroborate
with independent sources such as analytics, support requests, and event tracking
to estimate impact; and tie observations to published guidelines and heuristics.
Its framing of the stakes is that discovering problems is pointless if the team
does not believe the findings.

### Designing the instrument

Study materials are themselves designs and need iteration.

**Tasks.** [[2018-01-21_test-tasks-quant-qualitative]] states that a task
perfect for a qualitative study would not work at all in a quantitative one.
Qualitative tasks may be open-ended, and changing them mid-study when a better
understanding emerges is a feature rather than a failure, whereas quantitative
tasks need a single interpretation and a single success criterion. Shared
requirements across both: realism grounded in actual user behavior drawn from
interviews, search logs, analytics, and support calls rather than designer
assumption; no priming language, in particular no exact UI labels, which would
turn discovery into word-matching; emotional neutrality; and pilot testing with
1-2 representative users, which routinely exposes ambiguity the formal study
would have carried. On data, that source recommends dummy credentials for
quantitative studies to remove variability.

[[2016-01-24_users-real-data]] takes the qualitative side of the same question
and reaches the opposite recommendation for qualitative work: fake but realistic
data usually suffices in quantitative testing, while in qualitative testing real
user data should be assessed case by case and often helps, because variation in
names, passwords, and entry habits exposes problems that identical dummy data
hides. It attaches privacy obligations: confirm willingness at recruiting with a
clear explanation of use and protection, especially for financial or health
data; offer workarounds such as gift cards instead of personal credit cards or
budget-based scenarios; blur personal data in highlight videos and reports;
clear browser data in front of the participant; and let participants take or
shred printed materials.

**Questions.** [[2016-09-25_qualitative-surveys]] gives the structural rules:
test iteratively with at least four think-aloud rounds using real
target-audience members rather than colleagues, on paper first and then in the
platform, checking that the output is actually analysable; keep the survey short
because every added question lowers response rate and validity, with twenty
already too many for unmotivated respondents; split into several short surveys
across subsamples instead of one long one; mark "(Required)" or "(Optional)"
after each question rather than relying on asterisks; use conditional logic so
nobody meets an unanswerable question; randomise section, question, and answer
order against position and drop-out bias; and front-load what matters most.

[[2019-10-06_survey-questions-iterative-design]] shows the same discipline
applied to one question across four rounds, and its finding is
counterintuitive: edits made to clarify introduced bias. Adding a sentence
defining "significant action or decision" narrowed respondents toward
change-related answers; a preceding multiselect question primed research-related
answers through recency and anchoring; and adding reassurance that a single
recalled instance was enough reduced overthinking. It notes that meaning drifts
with context (finding information online was unusual in 1998 and mundane by
2019), that participants read subtle cues and try to answer as they assume the
researcher wants, and that pilots must run with the target demographic, 5-10
participants per iteration with think-aloud, not with coworkers.

### Analysis

[[2022-08-17_thematic-analysis]] supplies the core analytic method: tag
observations and quotations with codes, then find themes through iterative
comparison. Six steps: gather all the data, read everything end to end, code by
asking what each segment is about, create codes that encapsulate potential
themes, take a break for fresh perspective, and evaluate themes for fit and
saturation, returning to the board rather than forcing a conclusion. It
distinguishes descriptive codes (what the data is about) from interpretive ones
(the researcher's analytical reading), insists codes carry descriptions and
examples so multiple coders stay consistent, defines a theme as related findings
recurring across participants or data sources, and recommends three possible
setups: analysis software such as Dovetail or Dedoose, manual journaling with
memos following grounded theory, or affinity diagramming. Its stated purpose is
defensive: without a systematic process, analysis degenerates into skimming,
fixation on memorable moments, description without interpretation, and silent
dropping of contradictions. It also recommends team workshops where colleagues
read transcripts and highlight passages, both for shared understanding and to
check personal bias.

[[2025-05-02_analyze-usability-data]] gives a four-step frame: collect the
relevant data points, assess them for accuracy, explain the data through
synthesis, and check the explanation against the data for fit, with steps three
and four cycling repeatedly. Its central warning matches the previous source:
first explanations tend to be built from whatever was most memorable, and break
when tested against the full dataset. It borrows a hypothesis-testing posture,
making predictions from an explanation and rejecting or refining it when the
data does not support them, and requires triangulation across session moments,
study design, recruitment details, and facilitation events for complex questions
about discoverability, comprehension, and mental models.

[[2025-04-11_usability-data-in-analysis]] supplies the per-data-point filter,
six dimensions: authenticity (was the response natural, or shaped by wanting to
please the facilitator, by framing, or by professional-participant habits),
consistency (between what a participant says and does, and across sessions),
repetition, spontaneity (unprompted comments beat those elicited by leading
questions or by revealing the study's purpose), appropriateness (participant
representativeness and task realism), and confounds (order effects, convoluted
instructions, fatigue). Its rule when speech and behavior disagree is to
prioritise the behavioral data. It also states that AI cannot yet reliably
analyse usability test data, because it misses recordings, context, and study
design factors.

### Metrics, contradictions, and mixing methods

[[2021-06-13_metrics-qualitative]] permits collecting numbers during qualitative
studies under two conditions: report them anecdotally rather than statistically,
and state explicitly that they may not reflect the whole user population. Report
individual values ("one participant spent 8 minutes"), never averages, and say
"only 1 out of 6 participants" rather than "16.7%", since a percentage implies a
sample that can generalise. Its explanation for the ban is structural: the
facilitator flexibility and per-participant task modification that make
qualitative studies good at finding problems also inject the noise that makes
statistics meaningless. If metrics genuinely matter, it says, run a dedicated
quantitative study, which remote unmoderated methods have made practical.

When quantitative and qualitative results conflict,
[[2019-01-27_interpreting-research-findings]] treats the contradiction as
missing context rather than as bad data. It prescribes checking methodology
across four areas (participant selection, tasks and exposure, logistics and
realism, analysis) before interpreting, and offers substantive explanations for
the classic case where metrics improve but users complain: perceived usability
differs from objective usability, a gain of seconds may be invisible, users may
judge an improvement not worth relearning, and change aversion produces negative
feedback even about objectively better systems during the transition. Its
resolution is learnability studies, multi-round testing that tracks satisfaction
and performance as experience accumulates, which separates temporary change
aversion from a real usability problem.

[[2025-07-25_mixed-methods-research]] describes doing this deliberately rather
than reactively: mixed-methods research integrates both within one project
against one overarching research question, planned jointly from the start rather
than bolted together afterwards. It names three designs, explanatory sequential
(quantitative first to find the pattern, qualitative after to explain it),
exploratory sequential (qualitative first to generate hypotheses, quantitative
after to test them), and convergent parallel (both at once, as independent but
complementary evidence). Its core claim is that value comes from integration
rather than addition, from how the two datasets explain, inform, or triangulate
each other, and it warns that the approach costs more time, more coordination,
and more protocols than a single-method study.

## Sources (23)

- [[2016-01-24_users-real-data]] — the article distinguishes qualitative from quantitative testing approaches and emphasizes when real data benefits qualitative findings.
- [[2016-09-25_qualitative-surveys]] — Emphasizes open-ended questions as the foundation of qualitative research, requiring iterative testing and realistic interpretation as respondent opinions rather than population statistics.
- [[2018-01-21_test-tasks-quant-qualitative]] — Research that explores how and why things happen; values depth of understanding over breadth; flexible enough to pursue unexpected insights mid-study.
- [[2019-01-27_interpreting-research-findings]] — Quantitative studies measure efficiency and task success; qualitative studies capture user sentiment and satisfaction. Both are necessary for complete understanding; neither should automatically override the other.
- [[2019-02-10_research-journey-mapping]] — Emphasis on unstructured observation and conversation to understand user emotions, motivations, and actual behaviors rather than just reported preferences.
- [[2019-02-24_responding-skepticism-small-usability-tests]] — Approaches to interpreting findings from small participant groups using theory, comparative data, and representative participant selection.
- [[2019-08-11_cognitive-mapping-user-research]] — Cognitive mapping is an exploratory qualitative technique that produces rich multimedia data (maps, transcripts, video) requiring grounded theory analysis.
- [[2019-10-06_survey-questions-iterative-design]] — Open-ended survey questions require careful framing to avoid biasing respondents; small linguistic choices (definitions, preceding questions, reassurance) shape what participants report.
- [[2020-01-26_critical-incident-technique]] — Shows how CIT gathers rich qualitative information about critical system requirements and processes through structured participant recall.
- [[2021-06-13_metrics-qualitative]] — Methodology focused on identifying problems and opportunities through insights and anecdotes from representative users; flexible by nature.
- [[2021-07-11_5-test-users-qual-quant]] — Studies identifying usability issues through iterative testing; 5 users sufficient because any issue found is valid, not dependent on frequency.
- [[2021-08-01_qualitative-rigor]] — Qualitative research systematically gathers insights about user experience, expectations, mental models, and behavior through observation and conversation; it complements quantitative measurement by explaining why problems occur and how to solve them.
- [[2021-10-31_interview-sample-size]] — The article situates interviews within qualitative research and contrasts saturation-driven sizing with quantitative statistical approaches.
- [[2022-08-17_thematic-analysis]] — Thematic analysis is a systematic method for making sense of large volumes of qualitative data through iterative coding and theme identification across participants.
- [[2022-08-21_guide-ux-research-methods]] — Methods like interviews, observations, and field studies provide deep understanding of how and why people behave, revealing rich context and unexpected patterns.
- [[2024-01-12_field-studies]] — field studies are qualitative research methods generating rich descriptive data about user behavior, mental models, and workarounds.
- [[2024-03-29_diary-studies]] — provides detailed guidance on conducting high-quality qualitative research with long-term participant engagement.
- [[2025-04-11_usability-data-in-analysis]] — stresses that qualitative data analysis requires understanding whether data is authentic, consistent, spontaneous, and representative rather than statistically generalizable.
- [[2025-05-02_analyze-usability-data]] — emphasizes iterative cycles between analysis and synthesis, hypothesis testing, and triangulation of multiple data sources.
- [[2025-07-25_mixed-methods-research]] — The article describes how qualitative methods provide context, reveal motivations, and explain the "why" behind user behaviors.
- [[2016-11-04_ux-research_05-chapter-4-qualitative-research-methods]] — the chapter's primary topic, defining qualitative research as the complement to quantitative methods, rooted in ethnography and psychology, suited to understanding motivations, desires, and subjective experience
- [[2016-11-04_ux-research_06-chapter-5-choosing-your-methods]] — addressed as the complementary category in the selection equation: better suited to limited participant pools and exploring a specific workflow, especially when researchers can travel to participants in their environment, though the chapter notes large-scale qualitative studies are common for international products
- [[2016-11-04_ux-research_09-chapter-8-making-research-happen]] — the intensive process of directly observing and discussing user behavior, requiring multiple roles and interpersonal skill.
