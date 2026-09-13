---
type: concept
name: Usability Testing
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Design Testing"
  - "Moderation"
  - "Moderation Techniques"
  - "Quantitative Usability Testing"
  - "Remote Usability Testing"
  - "Test d'usabilité"
  - "Usability Evaluation"
  - "Usability Testing Bias"
  - "Usability Testing Methods"
  - "Usability Testing Tools"
  - "User Testing"
  - "User Testing Methods"
  - "Visual Design Testing"
---

# Usability Testing

## Definition

Usability testing is a research methodology in which a facilitator observes
participants attempting realistic tasks with a user interface, in order to
identify design problems, discover improvement opportunities, and learn how
users actually behave ([[2019-12-01_usability-testing-101]]). Its three core
elements are the facilitator, who guides the session and observes without
influencing behaviour; the tasks, which are realistic activities matching the
research questions; and the participants, who should be real or realistic users
of the product. The think-aloud protocol, where participants narrate their
actions and reasoning, is the method most commonly layered on top. It is a
behavioural, scripted, and typically formative method — it tells you *why* users
struggle rather than *how many* of them do ([[2022-07-17_which-ux-research-methods]]),
and [[2017-02-12_ux-research-cheat-sheet]] names qualitative usability testing
the single highest-impact research activity when a team can afford only one.

The method has a wide variation space rather than one canonical form: it can be
qualitative (finding problems with roughly five participants) or quantitative
(estimating metrics for a population with 20–40+ participants), moderated or
unmoderated, remote or in person, run on a live product, a high-fidelity
prototype, a paper sketch, or even a static deliverable
([[2021-06-13_metrics-qualitative]], [[2019-12-01_usability-testing-101]],
[[2017-01-22_sketch-test]]). Costs scale accordingly, from discount studies
costing a few hundred dollars and three days to elaborate international or
eyetracking studies costing hundreds of thousands. Several sources stress that
its value is not limited to bug-finding: shared observation of real users builds
team empathy, consensus, and persuasive power that written reports do not
([[2018-01-28_test-when-you-know-answer]], [[2019-04-21_sympathy-vs-empathy-ux]],
[[2016-08-28_ux-success-agile]]). [[2017-09-10_no-validate-in-ux]] argues the
framing matters: calling a study "validation" primes both participants and teams
to look for confirmation rather than problems, and a study that finds nothing
wrong signals a methodology failure, not a perfect design.

## Practice

### Planning a study

[[2016-04-17_usability-test-checklist]] gives a nine-point planning checklist:
define focused goals with stakeholders (extra goals degrade the quality of
insight on the primary ones), choose a format, recruit representative
participants, write tasks that match the goals, run a pilot, decide metrics,
document a test plan, and coordinate the team.
[[2017-09-17_ux-research-goals-to-scenarios]] details a seven-step path from
broad concerns to concrete sessions: list top user tasks, surface organisational
concerns, group and prioritise the issues collaboratively with stakeholders,
condense them into problem statements, derive research goals, break those goals
into observable activities and behaviours facilitators can watch for, and only
then write scenarios. Scenarios should describe an outcome the user wants ("show
me how you'd set up this device"), not interface operations.
[[2021-11-28_facilitate-ux-workshop-user-test]] frames the same principle for
facilitation generally: begin with goals, not activities, and prepare a detailed
guide covering agenda, timing, research questions, happy paths, and post-task
questions.

Piloting is treated as non-negotiable by several sources.
[[2016-04-17_usability-test-checklist]] and
[[2018-01-21_test-tasks-quant-qualitative]] both recommend running 1–2
representative participants first to catch ambiguous wording, missing details,
timing problems, and unrealistic scenarios. [[2019-10-27_unmoderated-usability-testing]]
makes piloting even more critical for unmoderated studies, since no moderator can
repair a broken instruction mid-session, and recommends piloting with real
participants on their own equipment. [[2024-04-19_wizard-of-oz]] likewise makes
piloting one of its five implementation steps.

### Qualitative and quantitative studies are different studies

[[2017-10-01_quant-vs-qual]] separates the two by what they assess: qualitative
work is a direct assessment through observation, letting the researcher see
which UI elements are problematic and probe with follow-ups; quantitative work is
an indirect assessment through metrics such as task time and success rate, better
suited to evaluation and comparison against a baseline or competitor than to
identifying specific problems. Quantitative studies carry formal statistical
confidence; qualitative studies do not, but work at small sample sizes — one quick
qualitative study with five users can uncover 85% of problems.
[[2018-04-22_quantitative-user-research-methods]] puts the quantitative minimum
at roughly 20–30 users and warns that metrics must not be collected and acted on
without statistical analysis; results from five users should not drive
quantitative claims. [[2019-10-20_measure-learnability]] illustrates a full
quantitative design: 30–40 participants with little prior exposure,
time-on-task measured across repeated trials until the learning curve plateaus,
tasks randomised to avoid order bias, and significance testing at the end.
[[2020-03-08_mobile-tutorials]] is a worked example with 70 participants across
matched groups, used to test whether onboarding tutorials actually help.

[[2021-06-13_metrics-qualitative]] addresses the tempting middle ground:
collecting metrics inside a qualitative study is acceptable only if the numbers
are reported anecdotally and the report explicitly states that findings may not
generalise. Individual values ("one participant spent 8 minutes") are fine;
averages ("average time was 4 minutes 23 seconds") and percentages ("16.7%
succeeded" for 1 of 6) falsely imply a population estimate — report "1 out of 6"
instead. If metrics genuinely matter, run a separate quantitative study.
[[2020-05-03_benchmarking-ux]] names quantitative usability testing as one of
three practical ways to collect benchmarking data alongside analytics and
surveys, notes that a single metric is meaningless without a reference point
(prior version, competitor, industry standard, or internal goal), and classes
benchmarking as summative — done between design cycles, not to guide them.

### Writing tasks

Task wording is where several sources concentrate the most warnings.
[[2017-04-09_better-usability-tasks]] lists ten mistakes: using the interface's
exact words (which tests reading comprehension instead of navigation and
labelling), telling users what steps to take, referencing stale dates or events,
writing tasks that only require locating rather than processing information,
padding with elaborate backstories, using marketing or internal jargon, touching
emotionally sensitive ground (politics, health, religion, money, real
relationships, famous names), and phrasing as a question rather than an
imperative — "Find X", not "How would you find X", because you want to observe
behaviour, not collect hypotheses. [[2021-11-28_facilitate-ux-workshop-user-test]]
repeats the imperative rule.

[[2018-01-21_test-tasks-quant-qualitative]] splits task design by methodology:
quantitative tasks must be narrow enough that every participant interprets them
identically and must have exactly one success criterion, since ambiguity and
multiple endpoints contaminate the metrics; qualitative tasks may be open-ended,
and changing them mid-study when understanding improves is a feature, not a
failure. Both should be grounded in what real users do, drawn from interviews,
search logs, analytics, and support calls rather than designer assumptions.
[[2020-02-09_user-testing-stepped-tasks]] offers stepped tasks — a deliberately
vague first task, followed by progressively more specific micro-hints only if the
participant struggles — to separate discoverability (does the user realise the
feature exists), findability (can they locate it knowing it exists), and
usability (can they use it). Pre-writing these beats improvising under time
pressure, and handing them over in writing preserves the rhythm of testing as
observation rather than conversation.
[[2022-07-24_the-funnel-technique-in-qualitative-user-research]] generalises the
same shape into the funnel technique: broad exploratory tasks before directed
ones, broad follow-up questions before specific ones, so that participants
volunteer information before any cue narrows them.

[[2016-03-06_feature-user-test]] argues against a common shortcut: sending users
straight to the page hosting the feature under test. Navigation to a feature is
part of its usability — in one study of embedded calculators, 36% of task
failures happened during navigation, not interaction — and pre-positioned users
skip the skeptical "is this page worth my time" judgement real users make. When
pre-positioning is unavoidable, use a bookmark with a neutral label rather than a
long URL or a search query.

On data inside tasks, [[2016-01-24_users-real-data]] and
[[2018-01-21_test-tasks-quant-qualitative]] agree on the split by methodology and
differ in emphasis: quantitative studies should use identical dummy credentials to
minimise variability, while qualitative studies often benefit from participants'
real data, because variation in names, passwords, and entry habits surfaces
problems that uniform fake data hides. [[2016-01-24_users-real-data]] adds the
privacy obligations that follow: confirm willingness during recruiting, offer
workarounds (a gift card instead of a personal credit card), blur personal
information in highlight reels and reports, and clear browser data in front of
the participant.

### Participants and recruitment

[[2016-04-17_usability-test-checklist]] insists on real users matching target
demographics and behaviours; proxy users forced to imagine a scenario produce
invalid results, especially on specialised or content-heavy sites.
[[2016-09-04_employees-user-test]] makes the strongest version of that argument
against internal recruitment: employees carry prior knowledge of jargon, business
goals, and the project; they feel obliged to complete tasks and fear disappointing
designers; Yahoo! research found employees rated their own company's site 2%
higher than external users did while external users rated it 15% lower than
competitors. Employees are legitimate only for intranets (where they *are* the
audience), pilot tests, or as a skunkworks demonstration in a low-UX-maturity
organisation. [[2024-09-03_344_Créer_du_lien_dev_tech_X_design_-_3_méthodes_efficaces]]
takes a different angle on the same practice for a different purpose: it
recommends having developers test early prototypes as users, not to gather valid
usability data but to involve the tech team early, generate fast feedback, and
defuse technical objections.

[[2019-05-12_everyone-as-users]] warns that an unfiltered recruit tends to
converge — a study might end up with nine commuters and one tourist when both are
target users — and recommends segmenting by behaviour, frequency of use, goals,
and domain knowledge rather than demographics, then recruiting proportionally
from each segment. [[2021-02-07_testing-content-websites]] adds that proxy
participants cannot acquire domain knowledge or replicate the emotional state of
a real user (a patient versus an interested observer).
[[2023-05-07_research-participant-database]] covers building an internal panel:
choose tools by team maturity, collect only necessary data, track engagement
history to avoid over-using the same people, work with legal on storage and GDPR,
populate from support interactions, surveys, events, and social media, audit
regularly, and always allow opt-out — while acknowledging the sampling bias
toward loyal customers that panels introduce.

### Choosing a format

[[2019-12-01_usability-testing-101]] lays out the axes: moderated or unmoderated,
remote or in person. [[2020-04-12_moderated-remote-usability-test-why]] compares
three formats across eight dimensions and positions remote moderated as the
middle ground — findings comparable to in-person, cost and convenience closer to
unmoderated. Facilitators can reorder or skip tasks, ask follow-ups, coach
think-aloud, and run roughly one-hour sessions, while teams observe together and
debrief immediately; unmoderated sessions typically cap around 20 minutes, allow
no clarification, and carry risks of unrepresentative or unmotivated testers.
[[2020-04-26_moderated-remote-usability-test]] gives the seven-step operational
version: evaluate screen-sharing tools carefully (installation, OS and browser
compatibility, and mobile support, which is often unstable); offer three ways to
deliver tasks (PDF, chat, or read aloud) while having participants read each task
aloud themselves to confirm comprehension and stop them looking ahead; schedule a
15-minute technology practice session the day before without showing the
prototype; enable webcam video if the connection allows; build in buffer time for
technical failures; and set explicit observer rules for muting, chat privacy, and
join timing.

[[2019-10-27_unmoderated-usability-testing]] describes the unmoderated case
directly: it scales to dozens or hundreds of simultaneous participants and can
return results within hours, but is poorly suited to early-stage prototypes
(nobody can explain or recover from errors) and to tasks demanding imagination or
emotional investment. Instructions must be exceptionally clear, hint-free, and
must state explicitly when to stop.
[[2020-07-26_remote-usability-testing-costs]] complicates the usual assumption
that unmoderated is dramatically cheaper: for a five-participant US study it puts
moderated at $415–$1,680 and 32–48 researcher hours against unmoderated at
$250–$1,250 and 11–27 hours — a 20–40% saving, not an order of magnitude — and
notes hidden costs in over-recruiting to compensate for cheaters and professional
participants, and in analysis time that simply migrates from the session to the
recording review. [[2021-02-07_testing-content-websites]] goes further for one
specific case: content testing should be moderated, because unmoderated
participants rush and skip the reading.
[[2024-12-06_unmoderated-user-testing-tools]] compares 11 platforms as of
September 2024; all record screen and voice, timestamp notes, auto-transcribe,
and export clips, most support live sites, prototypes, and mobile (Maze being the
exception noted for live sites), most bundle or integrate participant panels, and
they differ mainly in pricing model and extras such as webcam recording, AI
transcription, highlight reels, randomisation, skip logic, and statistical
analysis.

### Facilitation and moderation

[[2022-05-29_usability-checklist]] provides a ten-step moderation framework
supported by a facilitator's guide used only by the researcher: avoid the word
"test" (say "research" or "study", since the design is being tested, not the
person), check name pronunciation and build rapport, obtain informed consent with
time to read and ask questions, run a short background interview only if it does
not prime later behaviour, set expectations (tasks one at a time, the facilitator
takes notes rather than helping, both positive and negative feedback wanted),
start each follow-up broad before narrowing, reserve the last five minutes for
observer questions, and thank and compensate participants before the session
ends. [[2023-07-23_usability-testing-older-adults]] echoes the "the design, not
you, is being evaluated" framing as an anxiety reducer.

[[2019-05-05_intentional-silence-ux]] treats silence as a technique rather than
an accident: English speakers become uncomfortable after about four seconds, but
counting to seven before speaking gives participants time to organise their
thoughts and often lets them resolve the situation themselves; the first response
is frequently just thinking aloud. During task completion, facilitators should not
fill silence with commentary or a barrage of questions.
[[2021-11-28_facilitate-ux-workshop-user-test]] repeats the count-to-seven rule
and adds that great facilitators improvise when a plan stops working — encouraging
exploration when a participant wanders somewhere revealing.
[[2021-02-07_testing-content-websites]] applies silence specifically to long
stretches of quiet reading, and adds that the facilitator must first spend hours
with the content and subject-matter experts, and should tailor tasks to each
participant's circumstances based on a pre-study interview.

### Bias: the recurring failure mode

Priming is the thread running through the largest cluster of sources.
[[2016-01-24_priming]] describes both mechanisms: task wording that reuses
interface terminology primes participants to hunt for those exact words, and
facilitator behaviour — excessive friendliness, verbosity, terminology choices,
demonstrations, physical redirects — primes them to act in particular ways.
[[2016-02-07_icon-testing]], [[2020-02-09_user-testing-stepped-tasks]],
[[2018-01-21_test-tasks-quant-qualitative]], and
[[2017-04-09_better-usability-tasks]] all restate the terminology rule
independently. [[2024-12-13_testing-visual-design]] adds order effects, and
recommends counterbalancing or randomising the sequence in which design variants
are shown; [[2019-10-20_measure-learnability]] randomises tasks for the same
reason.

[[2017-12-17_leading-questions]] handles the questioning side. A leading question
implies its own answer and makes disagreement socially awkward, which matters more
than usual in usability testing because participants perceive the interviewer as
an authority. Its worked example ranks three phrasings: "I saw you were having
difficulty" assumes the observation, "Why did you have difficulty" still presumes
difficulty occurred, and "What was easy or difficult" lets the participant define
their own experience. The named traps are rephrasing observations in the
interviewer's words, suggesting answers, naming UI elements, and assuming
emotions; the cost is not only bias but the loss of unanticipated insight.
[[2022-05-29_usability-checklist]] and
[[2022-07-24_the-funnel-technique-in-qualitative-user-research]] converge on the
same remedy: broad open-ended follow-ups before any specific one.

[[2024-02-03_aesthetic-usability-effect]] identifies a bias in the other
direction: attractive design makes participants perceive products as more usable
and forgive minor problems, so they often praise visuals right after struggling
with the core task. The article offers three explanations for positive feedback
despite poor performance — pressure to say something, pressure to be nice to the
designer, and the effect itself — and recommends low-stress sessions, distancing
the facilitator from ownership of the design, and probing with vague questions
about functionality and difficulty.

### Observers and the team

[[2016-10-30_observer-guidelines]] gives observers explicit rules: remember audio
is recording and do not discuss participants in hallways or bathrooms where the
next participant might hear; avoid laughing or talking, pass notes instead of
speaking, silence notifications; take structured notes with one observation per
note, tagged with the scenario letter and the observer's initials; record
strategies, click-paths, and search terms rather than only mistakes; write
questions down for the facilitator instead of interrupting; and never answer,
advise, or correct a participant.
[[2016-05-29_team-members-user-test]] covers the ethical failures teams
introduce: participants must always be free to pause or leave; do not lie about
observers, mirrors, or recording; pay the full incentive even when recruitment
screening failed; never let a manager observe a direct report; cap in-room
observers at three and broadcast to a second room beyond that; and reframe failure
as an interface problem rather than user incompetence to stop name-calling.

[[2017-04-30_group-notetaking]] treats collective observation as a method in its
own right. Observers should capture notes individually and combine them
afterwards rather than sharing a live document, which invites groupthink and
distraction. Chronological logs suit remote observers, measured time-on-task, and
sequence-sensitive detail; topical one-incident-per-sticky notes colour-coded by
participant suit fast sorting and Agile rhythms. A short whiteboard top-findings
debrief after each session keeps findings visible; 4–10 observers is practical,
and stakeholders should be rotated so each sees at least two sessions and does not
form judgements from a single one.
[[2016-08-28_ux-success-agile]] reports the same practice from the Agile side —
making user research a team event with developers, product owners, and
stakeholders shifts decisions from opinion to data.
[[2019-04-21_sympathy-vs-empathy-ux]] adds that direct observation and research
videos build empathy far better than summary reports.
[[2019-02-24_responding-skepticism-small-usability-tests]] gives the persuasion
toolkit for small samples: explain the methodology *before* testing rather than
defending findings afterwards, get skeptics to observe sessions, share recruitment
criteria in advance, refuse to discount single-user findings (weigh fix cost,
severity, competitive analysis, and theory instead), corroborate with analytics
and support tickets, and connect observations to published usability guidelines.
[[2018-01-28_test-when-you-know-answer]] argues testing is worth running even
when the outcome is predictable — for team education, for letting users settle
design debates, for handling executive requests diplomatically by researching them
instead of refusing, and as insurance against the designer being wrong.

### What gets tested

Prototypes. [[2016-12-18_ux-prototype-hi-lo-fidelity]] frames a prototype as a
hypothesis that must be tested, and notes the asymmetry that motivates early
testing: tearing up a prototype is cheap, tearing up production code is not.
High-fidelity prototypes give realistic system response, reduce facilitator error,
and support evaluation of specific components and hierarchy; low-fidelity
prototypes are faster to prepare, changeable between sessions, less intimidating
for participants, and easier for teams to discard. Fidelity varies independently
across interactivity and visuals.
[[2021-12-19_paper-prototyping-cutout-kit]] describes the paper variant: a
facilitator, a participant, and optionally a "computer" helper who manipulates
screens to simulate responses and keep momentum, with scrolling simulated by long
sheets pulled through a frame cutout and dropdowns layered on top. It insists on
consistent fidelity across screens — mixing polished and rough screens skews
attention toward the polished ones — and on applying standard testing practice
regardless. [[2018-08-26_case-study-iterative-design-prototyping]] documents
three rounds of desktop and mobile testing across low- and high-fidelity
prototypes, narrowing the set each round and watching behaviour rather than
trusting stated preferences.
[[2024-12-03_parallel-and-iterative-design]] situates testing at the centre of
iterative design (38% usability improvement per iteration, 2–10 iterations
recommended), parallel design (3–5 alternatives tested and merged, yielding 70%
improvement versus 56% for simply picking a winner, with iteration adding 48%
more), and competitive testing.
[[2026-02-17_401_Prototypage_Le_guide_design_complet_-_Figma,_Lovable,_Google_Sheets_et_+]]
adds that the prototype's fidelity should follow the hypothesis being tested:
Figma high-fidelity prototypes for usability and detailed journeys (with click
hints disabled and testing done on the right device so as not to bias results),
real data in a Google Sheet or a Lovable-generated interface when the question is
whether the information itself is relevant, and static screens or a slide deck
with deliberately opposed concepts when the question is whether a concept is
interesting at all. [[2025-06-03_380_Figma_est_mort_les_nouveaux_outils_de_mon_process_de_design]]
argues AI code generators (Lovable, Bolt, Firebase Studio, Replit) now produce
functional prototypes wired to real data, which yields more qualitative test
feedback than fictional data and exposes real use cases and edge cases; the
author expects them to replace "90% des prototypes de tests utilisateurs" without
replacing pixel-perfect Figma work.

Content. [[2021-02-07_testing-content-websites]] argues content testing needs
genuinely different handling: moderated only, deeply prepared facilitators,
tolerance for silence, participants with authentic domain knowledge and
motivation, tasks tailored per participant, and open-ended information-seeking
tasks rather than pointers to specific pages.

Visual design and icons. [[2024-12-13_testing-visual-design]] splits methods into
attitudinal (5-second tests, preference testing) for brand alignment and first
impressions, and behavioural (eyetracking, A/B testing) for task success, and
warns that preference testing only works when the variants differ enough for
non-designers to notice, and that open-ended feedback is unreliable in
unmoderated settings — structured word choice or numerical ratings work better
there. [[2016-02-07_icon-testing]] maps four icon quality criteria to methods:
out-of-context presentation early on for recognition and information scent,
in-context time-to-locate and first-click measurement for findability, A/B tests
on live sites for information scent, and 1–7 rating scales plus comparative
selection for attractiveness. [[2016-02-28_microsoft-desirability-toolkit]]
describes the Microsoft Desirability Toolkit (reaction cards, 2002): a controlled
vocabulary of product-reaction words reduces the variability of open-ended
comments, the list should be tailored to study goals, at least 40% of the words
should be negative or neutral to counter flattery, online lists should stay at 25
words or fewer, word order should be randomised, and screenshots rather than live
interfaces reduce distraction from functionality.
[[2024-05-03_7-tips-memorable-imagery]] names three methods for testing visual
memorability: the 5-second test, an open word-choice test, and A/B testing.
[[2022-11-06_visual-design-in-ux-study-guide]] collects these together and notes
that subtle changes in colour, alignment, and font have measurable effects.
[[2021-03-21_visual-design-heuristics-posters]] applies the same practice to a
static print artifact, testing illustrations with general users and overall design
and content with UX professionals; testing revealed readers associating
illustrations with the wrong text through proximity, fixed by colour-coding.

Deliverables. [[2017-01-22_sketch-test]] extends the method to UX artifacts:
a colleague from the deliverable's actual audience reads it and sketches or
summarises it back, and the discrepancies reveal perceptual problems (content
hard to see) and comprehension problems (content misread). Standard protocol
still applies — watch what they circle, underline, and redraw rather than
soliciting suggestions, and do not correct misunderstandings mid-session.

Competitors. [[2024-01-05_competitive-usability-evaluations]] describes both
expert review and user testing against 2–4 selected competitors, with participants
typically testing 2–3 sites, order and pairings alternated to prevent learnability
effects, and explicit comparison questions as a bonus source of insight; the goal
is improving your own design, not declaring a winner.
[[2020-01-19_risks-imitating-designs]] gives the corollary: what a large company
ships is not evidence it works — Google reverted minimalist input fields to boxes
after testing hundreds of users, Amazon dropped decorative menu backgrounds that
hurt legibility — so test the borrowed solution with your own users and context.

### Adapting to specific populations and technologies

Minors. [[2019-04-28_usability-testing-minors]] recommends over-recruiting
(both parent and child affect attendance), segmenting by maturity and interest
rather than age alone, age-appropriate incentives such as small toys or stickers
rather than cash the parents will control, shorter sessions with breaks (up to 60
minutes for ages 3–12, 90 for teenagers), an abundance of varied tasks because
children disengage quickly, and a warm, casually dressed facilitator using
generic praise — a poker face makes young children quieter and think-aloud harder
to elicit. This directly contradicts the neutrality expected with adult
participants, and the article treats it as a deliberate adaptation.

Older adults. [[2023-07-23_usability-testing-older-adults]] warns against
assuming homogeneity, and recommends testing in participants' homes or nearby
residences to remove mobility barriers and reveal real device use, equipment
compatible with screen readers, magnifiers, keyguards, head wands and
voice recognition, reminders to bring glasses, realistic and memorable tasks with
printed references, shorter sessions to limit cognitive fatigue, explicit framing
that the design is under evaluation, and reserved time before and after for setup
and conversation. [[2019-09-08_usability-for-senior-citizens]] supplies the
longitudinal backdrop: 18 years and 123 participants aged 65+, showing rising
digital skill and multi-device use alongside persistent barriers in font size,
target size, contrast, inflexible input formats, and error messages.

International audiences. [[2021-04-18_why-international-usability-testing]]
argues domestic-only testing cannot surface two categories of problem: features
international users lean on disproportionately (language switchers, size guides,
currency converters) and culturally specific issues in context of use, product
perception, content tone, and trust signals; it also notes measured differences in
visual-complexity preference (Russians lower, Mexicans and Chileans higher) and
recommends remote testing in users' own environments to capture context. Both
[[2021-04-18_why-international-usability-testing]] and
[[2016-11-06_china-website-complexity]] conclude that testing with the actual
target population beats outsider intuition — the China study found that foreign
observers' assumption about Chinese users' comfort with density was partly right
but that those users still struggled with carousels, disappearing navigation, and
non-standard elements, complaining less while performing no better.

AR. [[2022-08-28_testing-ar-apps]] adds AR-specific planning: unambiguous task
wording for participants unfamiliar with the technology, ample hazard-free space
because participants focused on virtual objects ignore their surroundings, longer
sessions to absorb app downloads and the AR learning curve, dual recording of
both phone screen and room movement plus a wearable microphone, screening for age,
health and physical ability, and advance communication about physical activity,
recording of surroundings, and the right to withdraw.

High-stakes and civic contexts. [[2020-10-25_mail-ballot-usability]] evaluates
real vote-by-mail materials and connects design failures to roughly 18,000
rejected Massachusetts ballots, using the case to argue that testing matters most
where the transaction is unforgiving.

### Analysis and interpretation

[[2025-05-02_analyze-usability-data]] gives a four-step framework: collect
relevant data points from notes and recordings, assess each for accuracy, explain
the data through synthesis, and check the explanation against the data for fit,
cycling between the last two steps. It warns that initial explanations are
typically built from the most memorable data points and tend to break when tested
against the full dataset, and recommends treating explanations as hypotheses that
make predictions the data can reject.
[[2025-04-11_usability-data-in-analysis]] supplies six dimensions for weighing an
individual data point: authenticity (was the participant trying to please the
facilitator, or acting as a professional participant), consistency (when someone
says a task was easy but struggled, errored, or restarted, prioritise the
behaviour), repetition across sessions, spontaneity versus prompting,
appropriateness of participant and task, and confounds such as order effects,
fatigue, or over-complex instructions; it also states that AI cannot yet reliably
analyse usability test data because it lacks the recordings, context, and study
design information.
[[2023-11-24_surveys-design-cycle]] covers the instrumented side: post-task and
post-test surveys (SEQ, SUS) measure perceived usability during the Test phase and
come with industry benchmarks that make the numbers interpretable.
[[2023-06-18_error-messages-scoring-rubric]] shows how to operationalise abstract
guidelines into scored criteria — visibility, communication, efficiency, each
with four guidelines scored 1–4 and averaged into a letter grade — with multiple
independent evaluators averaged to reduce individual bias and groupthink.

### Methods that sit alongside it

[[2023-06-25_how-to-conduct-a-heuristic-evaluation]] positions heuristic
evaluation as a usability-inspection method that finds problems without users,
best run by three to five evaluators working independently before consolidating,
and explicitly states it cannot replace user research: a heuristic violation may
be justified by context, and only user research can confirm whether it actually
harms usability. [[2022-04-10_cognitive-walkthrough-workshop]] describes the
cognitive walkthrough as a group technique for assessing learnability without
users, with 2–6 evaluators from diverse roles, an explicitly defined action
sequence, and four questions asked at each step (will users try to achieve the
right result, notice the correct action, associate it with the result, and see
progress afterwards); it is recommended for early designs or when user testing is
cost-prohibitive.
[[2024-04-19_wizard-of-oz]] covers testing systems that do not exist yet: a
hidden human operator supplies system responses while the participant believes the
interface is autonomous, useful for conversational UIs, recommendation engines,
and real-time lookup, with the wizard working from a closed set of preset
responses, generating them live, or a hybrid, under a protocol documenting roles,
controlled elements, and improvisation rules.
[[2018-04-22_quantitative-user-research-methods]] situates quantitative usability
testing among analytics, A/B testing, card sorting, tree testing, surveys,
desirability studies, and eyetracking, distinguishing behavioural methods (what
people do) from attitudinal ones (what people say).
[[2022-07-17_which-ux-research-methods]] adds the three-dimensional map
(attitudinal/behavioural, qualitative/quantitative, context of use) and notes that
behavioural methods such as usability testing generally give more reliable
insight than attitudinal ones, while recommending method combination.
[[2016-01-10_ux-quiz-15]] touches the same territory obliquely, through questions
on testing bias and on distinguishing slips (execution errors) from mistakes
(planning errors).

### Testing throughout delivery, not only before release

[[2014-09-05_user-story-mapping_14-9-the-card-is-just-the-beginning]] frames
usability testing as a cadence rather than a gate: Patton recommends testing
with real users at least biweekly through a build, because the team's shared
mental picture of the solution routinely diverges from actual user behaviour,
and only observation exposes the gap. [[2014-09-05_user-story-mapping_23-18-learn-from-everything-you-build]]
extends the same discipline to the point of release, arguing that teams should
test working software with users doing real work rather than demo it and ask
for feedback — show-and-tell generates far less learning than watching someone
actually try to reach their goal. Both chapters tie this back to the empathy
argument already made by [[2019-04-21_sympathy-vs-empathy-ux]] and
[[2016-08-28_ux-success-agile]]: for Patton, watching users struggle is itself
what keeps a team's shared understanding honest, not just a bug-finding step.

## Sources (77)

- [[2016-01-10_ux-quiz-15]] — referenced through questions about avoiding bias in testing, differentiating slips from mistakes, and designing interfaces that support user goals; testing concepts underpin best-practice validation.
- [[2016-01-24_priming]] — task wording and facilitator behavior (friendliness, verbosity, demonstrations, physical actions) can unintentionally prime participants, influencing how they interact with interfaces and compromising test result reliability.
- [[2016-01-24_users-real-data]] — the article addresses how to design testing procedures that respect user privacy while gathering realistic behavioral data.
- [[2016-02-07_icon-testing]] — the article addresses how to test visual properties separate from functionality and content.
- [[2016-02-28_microsoft-desirability-toolkit]] — the Desirability Toolkit is one structured approach to aesthetic evaluation.
- [[2016-03-06_feature-user-test]] — methodology for designing test tasks and scenarios.
- [[2016-04-17_usability-test-checklist]] — The article provides practical guidance on planning and executing usability studies as a core UX research method.
- [[2016-05-29_team-members-user-test]] — The article addresses challenges that arise when teams observe testing sessions and strategies for maintaining research integrity.
- [[2016-08-28_ux-success-agile]] — Shows testing as a team-building and decision-influencing activity, not just a UX specialty, when multiple roles observe sessions and participate in debriefs.
- [[2016-09-04_employees-user-test]] — Clarifies the risks of participant bias and establishes external recruitment as methodological best practice for obtaining valid, generalizable usability data.
- [[2016-10-30_observer-guidelines]] — Observer guidelines ensure data integrity by preventing unintended influence on participant behavior during sessions.
- [[2016-11-06_china-website-complexity]] — Empirical testing with native speakers and target users reveals design problems that casual observation misses; the same methods work across cultures.
- [[2016-12-18_ux-prototype-hi-lo-fidelity]] — testing prototypes reveals design flaws, user interactions, and necessary iterations; this is presented as essential to quality outcomes.
- [[2017-01-22_sketch-test]] — sketch testing applies usability testing principles to deliverables rather than products.
- [[2017-02-12_ux-research-cheat-sheet]] — qualitative usability testing is highlighted as the single most impactful research activity.
- [[2017-04-09_better-usability-tasks]] — Discusses task design as a critical component of qualitative usability studies, with direct impact on study validity and actionable findings.
- [[2017-04-30_group-notetaking]] — Discusses group participation in observation and notetaking as a way to democratize research and build team confidence in findings.
- [[2017-09-10_no-validate-in-ux]] — empirical evaluation of designs with real users; framing and language significantly affect what problems are discovered and how teams respond to findings.
- [[2017-09-17_ux-research-goals-to-scenarios]] — empirical evaluation of designs through observed user interactions; test success depends on clear scenarios and well-defined success criteria.
- [[2017-10-01_quant-vs-qual]] — distinguishes two complementary data types, qualitative for identifying problems and quantitative for evaluation and comparison.
- [[2017-12-17_leading-questions]] — Research method where users attempt tasks on an interface; relies on follow-up questions to understand what users experienced; leading questions compromise the validity of findings.
- [[2018-01-21_test-tasks-quant-qualitative]] — Research method where users attempt tasks on an interface; requires different task design depending on whether the goal is to collect metrics (quant) or understand user thinking (qual).
- [[2018-01-28_test-when-you-know-answer]] — Research method for evaluating design with actual users; serves multiple purposes including identifying problems, building team consensus, and persuading stakeholders to support design recommendations.
- [[2018-04-22_quantitative-user-research-methods]] — combining quantitative metrics with traditional testing to measure both whether users succeed and how they perceive the experience.
- [[2018-08-26_case-study-iterative-design-prototyping]] — validation of designs with real users to identify problems and validate solutions; multiple rounds of testing with different prototypes generates more feedback in shorter timeframes.
- [[2019-02-24_responding-skepticism-small-usability-tests]] — Methods and interpretation of small-sample qualitative usability studies, emphasizing efficiency for discovering common issues rather than proving frequency.
- [[2019-04-21_sympathy-vs-empathy-ux]] — Observing users directly and sharing research videos with teams builds empathy more effectively than summary reports.
- [[2019-04-28_usability-testing-minors]] — Testing with minors requires adaptations to all phases: recruitment, task writing, environment, and facilitation to get valid insights.
- [[2019-05-05_intentional-silence-ux]] — Skilled facilitators use silence strategically to invite response, signal interest, and create psychological safety during testing, allowing natural task progression while resisting biased commentary or nervous questioning that distracts participants.
- [[2019-05-12_everyone-as-users]] — Research must include appropriate numbers of participants from each important user segment to capture diverse perspectives and needs.
- [[2019-09-08_usability-for-senior-citizens]] — Testing with older adults reveals barriers that younger users might overlook; longitudinal research (18+ years) shows how user populations and technologies evolve.
- [[2019-10-20_measure-learnability]] — quantitative learnability studies exemplify usability testing methodology with sample sizes, statistical analysis, and repeated-measures designs.
- [[2019-10-27_unmoderated-usability-testing]] — provides methodology for conducting effective unmoderated usability studies with detailed guidance on each phase.
- [[2019-12-01_usability-testing-101]] — provides comprehensive overview of usability testing as a research methodology with core elements and variations.
- [[2020-01-19_risks-imitating-designs]] — Emphasizes the necessity of validating design solutions with your own users and context before implementation.
- [[2020-02-09_user-testing-stepped-tasks]] — Demonstrates how to structure user testing to discover not just usability issues but also discoverability and findability problems.
- [[2020-03-08_mobile-tutorials]] — demonstrates the value of quantitative usability testing with matched groups to validate assumptions about design patterns.
- [[2020-04-12_moderated-remote-usability-test-why]] — compares three testing formats across eight dimensions including facilitator role, questioning ability, cost, scheduling, session length, and participant motivation risk.
- [[2020-04-26_moderated-remote-usability-test]] — A practical alternative to in-person studies with distinct advantages and preparation requirements; outlined through a seven-step process for conducting remote moderated usability tests with clear guidance on tool setup, task delivery, session management, proper scripting, consent procedures, recording, and ending procedures that encourage team debriefs.
- [[2020-05-03_benchmarking-ux]] — identified as one of three primary methodologies for collecting benchmarking data alongside analytics and surveys.
- [[2020-07-26_remote-usability-testing-costs]] — how session length, facilitator presence, and participant quality affect test outcomes and research insights.
- [[2020-10-25_mail-ballot-usability]] — evaluating real voting materials to uncover design problems that could lead to user errors and invalid ballots, showing how critical testing is for high-stakes transactions.
- [[2021-02-07_testing-content-websites]] — demonstrates how traditional usability testing methods require adaptation when the focus is evaluating written content rather than UI.
- [[2021-03-21_visual-design-heuristics-posters]] — the article describes testing illustrations with general users and testing overall design and content with UX professionals to validate effectiveness.
- [[2021-04-18_why-international-usability-testing]] — the article argues for the necessity and value of conducting international usability testing as a research method.
- [[2021-06-13_metrics-qualitative]] — Can be conducted qualitatively (finding problems) or quantitatively (measuring population performance); each requires different study structure.
- [[2021-11-28_facilitate-ux-workshop-user-test]] — User test facilitation benefits from goal-driven planning and specific strategies including intentional silence (counting to 7 before speaking), visual cues, encouragement to act, and providing backup activities.
- [[2021-12-19_paper-prototyping-cutout-kit]] — Paper prototyping leverages standard usability testing practices with a facilitator, participant, and optional "computer" helper to evaluate interface learnability.
- [[2022-04-10_cognitive-walkthrough-workshop]] — structured approaches to evaluating interface design at different project stages.
- [[2022-05-29_usability-checklist]] — A research method requiring the facilitator's careful moderation to capture authentic user behavior and feedback without bias or intimidation, achieved through creating a comfortable environment, following a structured process, and gathering meaningful data through carefully timed questions.
- [[2022-07-17_which-ux-research-methods]] — Behavioral, qualitative, and scripted; usability testing is formative and useful for understanding why users struggle with designs.
- [[2022-07-24_the-funnel-technique-in-qualitative-user-research]] — Funnel technique applies to task ordering (broad exploratory before directed) and followup questioning (general before specific) to gather unbiased behavioral data.
- [[2022-08-28_testing-ar-apps]] — AR testing adds complexity to standard mobile usability testing through spatial interaction, movement, and AR-specific learning curves.
- [[2022-11-06_visual-design-in-ux-study-guide]] — testing visual design with users, desirability toolkits, and icon usability studies reveals whether visual choices improve or hinder experience; subtle changes have significant effects.
- [[2023-05-07_research-participant-database]] — Conducting research with actual users to understand how they interact with products, requiring reliable access to representative participants through panels.
- [[2023-06-18_error-messages-scoring-rubric]] — the rubric demonstrates how abstract guidelines can be operationalized into measurable criteria for consistent assessment across teams.
- [[2023-06-25_how-to-conduct-a-heuristic-evaluation]] — heuristic evaluation is one of several systematic approaches to identifying design problems without conducting user testing.
- [[2023-07-23_usability-testing-older-adults]] — Covers specialized techniques for recruiting, conducting, and supporting usability studies with older adult participants.
- [[2023-11-24_surveys-design-cycle]] — post-task and post-test surveys measure usability of designs through established instruments (SEQ, SUS) with industry benchmarks.
- [[2024-01-05_competitive-usability-evaluations]] — both expert review and usability testing methods can be applied to evaluate competitors' designs using established UX evaluation approaches.
- [[2024-02-03_aesthetic-usability-effect]] — practitioners must account for the aesthetic-usability effect when interpreting participant feedback.
- [[2024-04-19_wizard-of-oz]] — demonstrates a specialized usability-testing approach for technologies with complex, dynamic responses.
- [[2024-05-03_7-tips-memorable-imagery]] — describes three methods for testing visual memorability (5-second test, open word-choice test, A/B testing).
- [[2024-09-03_344_Créer_du_lien_dev_tech_X_design_-_3_méthodes_efficaces]]
- [[2024-12-03_parallel-and-iterative-design]] — Discusses how user testing is central to all three methods, enabling judgment of designs based on empirical observations of user behavior rather than designer preferences.
- [[2024-12-06_unmoderated-user-testing-tools]] — Compares features, pricing, and capabilities of 11 popular platforms used for unmoderated usability testing.
- [[2024-12-13_testing-visual-design]] — Introduces a structured approach to testing visual design using both attitudinal and behavioral methods rather than relying on designer preferences.
- [[2025-04-11_usability-data-in-analysis]] — emphasizes the need for rigorous, contextual analysis of test data across behavioral and verbal dimensions rather than accepting surface-level signals.
- [[2025-05-02_analyze-usability-data]] — applies systematic analysis framework to qualitative usability test data to generate trustworthy insights.
- [[2025-06-03_380_Figma_est_mort_les_nouveaux_outils_de_mon_process_de_design]]
- [[2026-02-17_401_Prototypage_Le_guide_design_complet_-_Figma,_Lovable,_Google_Sheets_et_+]]
- [[2024-01-23_laws-of-ux_09-7-aestheticusability-effect]] — Observational methods to uncover design problems and learn user behavior; however, the aesthetic-usability effect can mask genuine issues when beautiful interfaces lead users to underreport problems.
- [[2013-08-01_just-enough-research_04-chapter-3-the-process]] — the chapter describes usability testing as observing representative users attempting tasks to determine whether a product is usable and identify resolvable issues; it uncovers structural and flow problems but is not sufficient for successful product design.
- [[2013-08-01_just-enough-research_08-chapter-7-evaluative-research]] — Hall presents usability testing as a core practice, not a late-stage gate: test competitor products, sketches, and prototypes at every decision point. Tests revolve around task-based scenarios with four to eight participants per user type. Success is measured by completion rate and error-free rate. Results are rated by severity (does it prevent task completion?) and frequency (what percentage of users hit it?), then triaged into three tiers of priority.
- [[2016-11-04_ux-research_05-chapter-4-qualitative-research-methods]] — product validation is presented in three forms: moderated testing where researchers adjust criteria and ask probing questions, unmoderated remote testing using audio and screen recording, and remote moderated testing combining real-time interaction with digital tools
- [[2014-09-05_user-story-mapping_14-9-the-card-is-just-the-beginning]] — The chapter stresses regular testing with real users (at least biweekly) to see how actual behavior diverges from the team's expectations, and to build empathy across the team by witnessing user struggles.
- [[2014-09-05_user-story-mapping_23-18-learn-from-everything-you-build]] — Teams should test working software with real users doing real work, not demo it and ask for feedback. Observation of actual use generates insights that show-and-tell cannot provide.
