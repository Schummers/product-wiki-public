---
type: concept
name: User Research
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Pain Points"
  - "UX Research"
  - "UX Research Practices"
  - "User Goals"
  - "User Needs"
  - "User Research Infrastructure"
  - "User Research Platforms"
  - "Design Research"
  - "Research Benefits"
---

# User Research

## Definition

User research is the systematic investigation of users' needs, behaviors, goals
and reactions, conducted to ground design and product decisions in evidence
rather than assumption. It is not a single method but a family of them,
qualitative and quantitative, behavioral and attitudinal, spread across every
phase of a project: discovering whether a problem is worth solving, exploring
the problem space, testing designs, and listening to what happens after launch
([[2017-02-12_ux-research-cheat-sheet]]). Its object is broader than an
interface: it covers what users are trying to accomplish, what stands in their
way, the vocabulary and mental models they bring, and the context in which they
work ([[2017-09-17_ux-research-goals-to-scenarios]],
[[2025-07-25_strategies-complex-application-design]]).

The sources converge on why it is necessary: designers are systematically
unrepresentative of, and wrong about, their users. The false-consensus effect
makes people assume others share their choices and reasoning
([[2017-10-22_false-consensus]]); narrative bias makes compelling but unfounded
stories feel like knowledge ([[2017-02-19_narrative-biases]]); and large-scale
skill measurement shows design teams sit in the top few percent of computer
ability while a quarter of the adult population cannot use a computer at all
([[2016-11-13_computer-skill-levels]]). Research is presented as the antidote,
and repeatedly distinguished from validation: studies run to confirm a decision
already made are less useful than no study at all, because they prime both
participants and teams to overlook problems ([[2017-09-10_no-validate-in-ux]],
[[2025-08-08_research-yes-or-no]]). Its outputs are also double: findings, and
the shared learning a team acquires by witnessing users directly — a distinction
that matters when deciding what can be delegated to AI
([[2026-07-17_human-led-research-still-matters]]).

The philosophical framing runs deeper than method choice. In the foreword to
*UX Research*, Steve Portigal contrasts research as practiced in product
design, which starts from specific questions a team needs answered in order to
build or improve something, with earlier academic research such as Roger
Barker's decades-long study of a Kansas town, which privileged data collection
over questions. He treats the most valuable outcome as often what a team
didn't know it didn't know, not merely the answer to the initial question, and
frames research as fundamentally an act of human connection that requires
practice, reflection, mentorship and training despite its apparently low
barrier to entry ([[2016-11-04_ux-research_01-foreword]]).

## Practice

### Start from goals, not methods

Research goals should be derived from the top user tasks and the organization's
own concerns, grouped and prioritized with stakeholders, condensed into problem
statements, and only then translated into observable activities and scenarios
([[2017-09-17_ux-research-goals-to-scenarios]]). The same discipline governs
method choice: pick the method from the research question, then check budget and
minimum sample size ([[2017-10-01_quant-vs-qual]]). Overcommitting to too many
goals in one study degrades the answers to the primary ones
([[2017-09-17_ux-research-goals-to-scenarios]]). Framing matters even at the
level of vocabulary: replacing "validate" with "test", "examine" or "see where
the design is successful and unsuccessful" changes what participants report and
what teams do with it ([[2017-09-10_no-validate-in-ux]]).

### Match the method to the phase

The cheat sheet organizes methods into four phases: Discover (field studies,
user interviews, diary studies, competitive analysis), Explore (personas,
journey mapping, card sorting, prototype feedback), Test (qualitative usability
testing, benchmarking, accessibility evaluation) and Listen (surveys, analytics,
search-log analysis, FAQ review); if only one activity is affordable, it
recommends qualitative usability testing of an existing system
([[2017-02-12_ux-research-cheat-sheet]]). Discovery specifically combines
exploratory research with stakeholder interviews and workshops, and aims at four
outcomes: understanding users and needs, understanding problems and
opportunities, identifying constraints, and a shared team vision
([[2020-03-15_discovery-phase]]). In Agile settings, discovery should be scaled
rather than skipped, and user research is only one of its ingredients:
secondary research, stakeholder interviews, analytics, past research and
heuristic evaluation can carry part of the load within a sprint, with spikes
used to time-box one or two key questions ([[2023-02-05_discovery-in-agile]]).
Design thinking places the same requirement at the front of its own cycle: the
empathize phase, made of research and observation of real users, grounds
everything that follows ([[2016-07-31_design-thinking]]).

### Qualitative, quantitative, behavioral, attitudinal

Qualitative work gives direct observation and the freedom to probe, identifying
which elements are problematic; quantitative work gives indirect but statistically
defensible measures suited to benchmarking and comparison
([[2017-10-01_quant-vs-qual]]). The related split is between what people do and
what they say: behavioral methods (usability testing, analytics) versus
attitudinal ones (surveys, card sorting, desirability studies). Attitudinal data
alone cannot be trusted to predict behavior — participants often answer to
please, or lack the context to predict themselves — so stated preference should
be checked against observed behavior ([[2025-08-08_research-yes-or-no]]).
Sample sizes follow from this: qualitative studies work with small numbers,
while quantitative usability testing needs roughly 40+ participants and surveys
100+ under probability sampling ([[2025-04-18_convenience-vs-probability-sampling]]).

### The method inventory

The sources describe, among others:

- **Interviews and field studies**, the qualitative base for uncovering genuine
  needs, mental models and motivations ([[2019-03-24_user-need-statements]],
  [[2019-04-21_sympathy-vs-empathy-ux]]).
- **Diary studies**, used to log needs over time — for example 12 participants
  logging 428 ideal needs for an intelligent assistant
  ([[2018-10-21_intelligent-assistant-user-needs]]) — and to characterize
  behavior at scale, such as the finding that 21% of online activities are
  research-based ([[2019-03-03_unbridged-knowledge-gaps]]) or the analysis of
  425 AI chatbot interactions ([[2023-11-24_ai-prompt-structure]]) or of 10
  smart-home users' motivations ([[2025-12-05_smart-homes-user-value]]). The
  entry template itself shapes both data quality and participant effort: closed
  entries track behaviour and trends cheaply but not the reasons behind them,
  open-ended entries buy depth at a cost to participant and analyst, multimedia
  entries buy visual context at a cost in technical complexity. Participant
  effort takes priority over analysis effort, entries should stay within 5–10
  minutes, and most studies mix the three types rather than picking one
  ([[2025-11-28_diary-study-entries]]).
- **Contextual inquiry and observation of real work**, which reveal
  environmental constraints, interruptions and coordination that isolated
  testing misses ([[2020-09-20_task-analysis]],
  [[2025-07-25_strategies-complex-application-design]],
  [[2024-06-14_ai-imagegen-stages]]). *UX Research* frames it as an
  ethnographic method: follow participants in their environment and prompt
  them to "think aloud" as they work, which supplies both context for their
  actions and immediate, observable feedback alongside probing questions about
  motivations and barriers; scope can run from as few as 5 to as many as 50
  participants ([[2016-11-04_ux-research_05-chapter-4-qualitative-research-methods]]).
- **Task analysis**, a two-stage method (gather via contextual inquiry, critical
  incident interviews, diary studies, activity sampling, simulation; then
  structure into a hierarchical task analysis) that separates goals from the
  tasks performed to reach them ([[2020-09-20_task-analysis]]).
- **Card sorting**, qualitative or quantitative, to surface how users expect
  content to be structured ([[2024-02-02_card-sorting-definition]]).
- **Search-log analysis**, behavioral data revealing intent, vocabulary
  mismatches, missing content and user distress
  ([[2017-07-30_search-log-analysis]], and used to inform navigation labels in
  [[2022-07-10_university-ux-professionals]]).
- **Usability testing**, the primary means of observing designs in use
  ([[2019-12-01_usability-testing-101]]), including multi-country moderated plus
  unmoderated combinations ([[2022-12-11_time-zone-selectors]]).
- **Surveys with structured sentiment instruments**, such as word-selection
  studies of animated versus static marketing emails
  ([[2020-03-15_gif-emails]]) and of emoji subject lines
  ([[2020-06-28_emojis-email]]).
- **Multi-method, multi-country programs**, combining usability testing,
  naturalistic recording, diary studies and surveys across 7 countries and 91
  participants ([[2016-04-10_young-adults-ux]]).
- **Long discovery interviews**, which come in three forms — purely exploratory
  interviews, probe testing that puts a long-term vision or futuristic concept in
  front of participants to capture immediate reactions and emotions, and
  co-construction with expert users — each matched to a different objective and
  a different audience. They require the purpose to be set before the session
  (adjusting a roadmap, finding opportunities), since an unprepared long
  interview returns superficial data and invites confirmation bias
  ([[2025-04-01_371_L_interview_longue_en_phase_de_Discovery_-_Guide_UXR]]).
- **The "Excel test"**, a B2B technique for separating wants from needs by
  hunting for the homemade tools users build around the product — spreadsheets,
  scripts, summary documents, manual processes. A want is a hypothetical
  request; a need is something the user has already paid for or already worked
  around, and the effort spent building that workaround is itself the evidence
  that the underlying problem was worth solving and that an integrated solution
  would be wanted. Surface these artifacts with written questionnaires whose
  questions target tooling, or with long interviews using screen sharing to
  observe the habit in detail ([[2024-12-17_356_Excel_test_la_méthode_d_UX_Research_B2B_idéale]]).
- **Formative evaluation**, qualitative usability testing on prototypes to
  determine which design changes are needed, distinct from summative comparative
  or baseline testing; and **thematic analysis**, a method for analysing
  qualitative interview data rather than quantitative, analytics or biometric
  data ([[2020-01-05_ux-quiz-2019]]).

Specialized domains adapt the toolkit rather than abandon it: games user
research adds multiuser playtesting, biometric sensors and telemetry at the
scale of hundreds of millions of sessions ([[2016-03-20_game-user-research]]);
complex applications require studying the domain itself and triangulating across
frontline users, supervisors and adjacent teams, and evaluating expert reasoning
rather than task completion ([[2025-07-25_strategies-complex-application-design]]).

### Testing concepts before committing

The largest risk is heading for the wrong destination, so concepts are
deliberately challenged before a direction is locked in. Internally that means
co-constructing the problem definition with stakeholders from the start —
post-it trashing, where existing interfaces are put up and everything that works
or fails is criticised, or simple needs forms — then live concept voting, where
two or three deliberately opposed, extreme concepts are presented to
decision-makers in one-to-one meetings so the business reasoning and user
knowledge behind their reactions come out, the debate being the point rather
than the vote. The same exercise runs asynchronously for a wider internal
audience to collect volume, with answers split by profile (customer support,
sales) to expose profile-specific behaviours and needs. Internal challenge is
necessary but not sufficient: testing with end users, through user tests,
interviews or asynchronous studies, remains the reliable way to confirm the
solution holds, and the designer's job is then to extract the core information
and filter the noise ([[2026-03-03_403_Guide_Tester_un_concept_design_produit_en_interneexterne_-_Podcast_Product_Design]]).

Prototypes serve this as instruments rather than deliverables: decide first
which hypothesis is being challenged, then match the artifact to it. A good
prototype answers a doubt, it is not a polished Figma file marking the end of a
design phase. High-fidelity Figma prototypes suit usability and detailed flows,
with click hints turned off and testing done on the appropriate device so
results are not biased; data-heavy interfaces such as dashboards or analysis
tools are better checked with real data in a plain Google Sheet or an
AI-generated interface from a tool like Lovable, since the relevance of the
information matters more than the visuals; and in the exploratory phase static
screens or a slide deck of deliberately opposed concepts are enough to provoke
reactions and steer the product vision
([[2026-02-17_401_Prototypage_Le_guide_design_complet_-_Figma,_Lovable,_Google_Sheets_et_+]]).

### Recruiting, sampling and panels

Convenience sampling is the acknowledged default because it is fast and
sufficient to find usability problems; probability sampling is reserved for
high-stakes, population-level inferences, and quotas do not make a convenience
sample random ([[2025-04-18_convenience-vs-probability-sampling]]).
Hard-to-reach groups need dedicated tactics: for high-income participants,
word-of-mouth introductions outperform recruitment services, income should not
be asked directly, sessions should be remote and flexibly scheduled, and
incentives raised or converted into charitable donations
([[2022-05-01_high-income-participants]]). Remote research widens the
participant pool but requires practising the technology, recruiting spare
participants and adapting consent forms ([[2020-03-29_remote-ux]]). At
organizational scale, a user panel is described as research infrastructure
rather than a list: it cuts no-show rates by around 20%, reduces recruiting
cost and builds customer relationships, while customer panels risk
overfamiliarity and target-user panels are harder to build — hence the common
hybrid of internal panel plus external recruiting
([[2026-01-23_user-panels-101]]). Personas can themselves serve as screening
criteria for recruitment ([[2025-10-03_persona]]). An existing audience can
itself be the pool: a podcast host framed a future design tool by putting a
short five-question research form to his listeners, in order to build against
real usage rather than assumption
([[2024-10-22_Bonus_Nouvel_outil_design_en_approche]]).

*UX Research* treats recruiting itself as a risk-management problem: start
from existing sources — past qualitative research, current analytics,
marketing's customer segments, or a written baseline profile — so screening
criteria track research goals, then build a screener as a 10–15 minute
multiple-choice survey that both confirms desirable behaviours and
disqualifies mismatches, since skipping screening to test with a friend,
relative or someone off the street exposes the study to risk and gaps.
Assuming participant availability is not an issue, it sets a quota of three
to five participants per user profile, adjusted by how important that
profile is and how hard it is to fill, and treats a small user pool as a
focused audience rather than an obstacle. Because no-shows are common,
scheduling backup participants, compensated the same way, is standard
practice, and when a screener fails and a mismatched participant (a "dud")
shows up anyway, the session still yields data and may call for adjusting
tactics mid-session. Recruitment methods range from slow, DIY self-recruiting
(a minimum two weeks' lead time) through in-person and online intercepts and
cold calling to outsourced third-party or client recruiters
([[2016-11-04_ux-research_08-chapter-7-recruiting]]).

### Research under startup constraints

Startups compress the practice rather than drop it. With little time, awkward
access to users and decisions concentrated in the founders, the advice is to
abandon long academic processes and aim research at the riskiest hypotheses
only, using fast concept tests, A/B testing and fake doors for the best return
on effort — a higher accepted level of risk means proportionally less upfront
research. Access to users is usually a matter of nerve rather than possibility:
cold calls, hand-written personalised emails and in-app messages beat elaborate
recruiting processes, and twenty manually sent emails outperform five hours
negotiating a campaign with marketing. In a founder-led culture, credibility is
won by demonstrating value quickly on a high-stakes project, with customer
recordings and quantitative metrics as the tangible evidence behind
recommendations ([[2025-09-23_396_UX_Research_en_StartUp,_guide_et_astuces]]).

### Ethics and participant care

Informed consent has two halves — the researcher informs, the participant
understands and freely agrees — and written forms guarantee every participant
gets the same information; vulnerable populations (children, prisoners,
cognitively impaired adults, low-literacy participants) cannot self-consent, and
modular consent with separate checkboxes for recording and publication raises
participation ([[2022-07-03_informed-consent]]).

*UX Research* adds the operational layer, arguing qualitative research demands
more preparation than quantitative precisely because so much of it is field
research conducted directly with people: session checklists covering tech
checks, paperwork, participant and observer briefing, and supplies prevent
disruptions and signal professionalism before, between and after sessions. It
distinguishes three consent documents by purpose — nondisclosure agreements to
prevent leaks, recording waivers to document permission to record, and
permission-to-quote forms to clarify how statements will be used — and treats
a participant declining to be recorded as normal, to be handled by visibly
putting devices away rather than as a problem. For sensitive topics, welcome
kits sent three to four days ahead (project information, team biographies with
photos, points of contact to verify legitimacy, logistics) build trust before
the session happens. Honorariums, whether cash split into individual
envelopes, gift cards or free product, are documented with receipts so
compensation is not later disputed
([[2016-11-04_ux-research_07-chapter-6-logistics]]).

### Facilitating the session: roles and flow

*UX Research* argues the best research initiatives run with a two-person
minimum: a moderator guiding the conversation and a note taker capturing
observations, since actively listening, formulating a response and taking
notes all at once is very difficult for one person alone; the two roles can
rotate between sessions. It recommends framing the relationship as the
participant teaching the researcher rather than as interviewer and
interviewee, so the participant leads and chooses what to share. Observers,
dialed in remotely or watching behind one-way glass, are asked to hold their
questions and not interrupt the session's flow. Dry runs with colleagues,
never real participants, are where technology, flow and timing get tested and
discussion guides get revised, before anything reaches an actual participant.
Within a session, formalities (consent forms, honorarium) come first, then an
opening script read aloud for consistency across sessions, then tasks
sequenced from simple and established toward more challenging. The chapter
states plainly that participants will not complete every task and that this
is fine — the introduction should tell participants that the product is being
evaluated, not them — and that moderators can choose in the moment whether to
support a struggling participant or let a task fail. A closing post-task
discussion invites observers and participants to raise anything unaddressed,
sometimes surfacing opportunities the study did not set out to find
([[2016-11-04_ux-research_09-chapter-8-making-research-happen]]).

### Asking without leading

Question design is treated as a first-order validity issue. Open-ended questions
starting with "how" or "what" let participants define their own experience;
closed questions beginning with "did", "was" or "is" suggest the expected
answer; the funnel technique moves from broad to specific, and probes like "tell
me more about that" extend the inquiry ([[2024-01-26_open-ended-questions]]).
Study materials must avoid priming: AI-drafted screeners, tasks and interview
questions need explicit guidance to prevent priming, vague instructions and weak
screener distractors ([[2024-04-05_plan-research-ai]]). Method-specific
artifacts carry their own bias risks — in card sorting, parallel keyword
labelling makes participants match words instead of meaning, which synonyms,
non-parallel phrasing, richer descriptions and think-aloud facilitation are used
to counter ([[2024-06-14_card-sorting-terminology-matches]]).

Beyond wording, the moderator's own conduct is part of the instrument. Leaving
silences unfilled lets participants keep digging instead of stopping at their
first answer, and reformulating what they just said prompts them to correct
imprecisions and name the real irritants. The most reliable questions are about
behaviour rather than desire: ask what people actually do today to solve the
problem, never what they would want, because current behaviour expresses needs
more faithfully than projection — what users do matters more than what they say
([[2025-04-01_371_L_interview_longue_en_phase_de_Discovery_-_Guide_UXR]], [[2024-12-17_356_Excel_test_la_méthode_d_UX_Research_B2B_idéale]]).

### From data to artifacts

Research feeds a set of shared representations, each of which the sources insist
must rest on data rather than assumption:

- **User need statements**, framed as verbs (outcomes) rather than nouns
  (solutions), and derived from interviews, field studies and diary studies
  ([[2019-03-24_user-need-statements]]).
- **Personas and archetypes**, clusters of behaviors, attitudes, motivations,
  pain points and goals built from field studies, surveys, interviews and
  longitudinal studies ([[2022-05-15_personas-archetypes]],
  [[2025-10-03_persona]]). Persona type follows research investment —
  lightweight, qualitative or statistical ([[2022-10-09_personas-study-guide]])
  — and scope determines segmentation: broad personas yield shallow data,
  narrow ones rich data, and the same segments do not cascade across
  organizational levels ([[2020-01-12_persona-scope]]). Personas decay:
  analytics, usability testing and support data signal when to revise, and teams
  updating quarterly reported higher impact (5.5/7) than those updating every
  1–4 years (4.5) or rarely (3.9) ([[2016-02-14_revising-personas]]).
  Antipersonas require the mirror-image research — direct study of threat actors
  where possible, or interviews with experts such as security staff, lawyers or
  social workers ([[2022-09-11_antipersonas-what-how]]).
- **Empathy maps**, which synthesize research into says/thinks/does/feels; their
  sparse regions are read as knowledge gaps requiring more research
  ([[2018-01-14_empathy-mapping]]), and they can be used before research to
  plan, during to capture observations, or after to communicate
  ([[2023-02-12_using-empathy-maps]]).
- **Journey, experience and service maps**, each requiring an explicit choice
  between hypothesis-based and research-based construction
  ([[2017-11-05_ux-mapping-cheat-sheet]]). Grounding is the recurring failure
  point: in a survey of 48 practitioners, 25% of journey-map failures came from
  maps based on assumptions rather than data
  ([[2016-10-16_journey-mapping-ux-practitioners]]), and phases should come from
  research, not guessed structure ([[2018-12-09_journey-mapping-101]],
  [[2019-04-07_journey-mapping-faq]]). Analysis of a finished map looks for
  expectation mismatches, unnecessary touchpoints, emotional low points,
  high-friction channel transitions, moments of truth and successes worth
  amplifying ([[2020-03-22_analyze-customer-journey-map]]).
- **UX stories**, which must stay tied to real research or risk satisfying
  imaginary needs ([[2017-01-15_ux-stories]]), and which persuade best when
  backed by real quotes and data ([[2019-04-28_persuasive-storytelling]]).
- **User stories**, written to the template "As a [role], I want [goal/desire]
  so that [benefit]", where the goal is what the user wants to achieve with the
  product and the benefit is the reason they want it — the real motivation for
  performing it. That source presents the template as a way to explore the
  connection between a customer's context and their needs, and to uncover the
  motivation behind a desired behaviour rather than stopping at the behaviour
  ([[2018-02-12_solving-design-exercises_11-step-3-understand-the-customer-s-context-and-needs-when-and]]).

### Pain points and user needs

[[2018-02-12_solving-design-exercises_11-step-3-understand-the-customer-s-context-and-needs-when-and]]
gives a compact route from context to needs. Start with where the customer
physically is, what event triggers the need, how much time they have, which
platform they are on and what emotional state they are in, since those
conditions drive design decisions such as hands-free navigation or a dark
interface. Then identify the high-level motivation for solving the problem
(freelancers wanting to be in control of their business is that source's
example) and break it into specific sub-needs — financial monitoring, work
planning, business growth — each of which opens a different solution angle.
Mapping the current customer journey then surfaces the problems and suboptimal
moments that can be turned into opportunities in later ideation.

Pain points are described at three levels, each with its own detection method:
interaction-level (usability testing, prioritized by impact, frequency and
recurrence), journey-level (interviews, diary studies, journey mapping) and
relationship-level (benchmarking surveys, analytics, behavior tracking,
prioritized by churn and brand-loyalty erosion) ([[2021-05-16_pain-points]]).
Research also surfaces needs that products systematically fail to meet:
knowledge gaps in complex decision-making tasks
([[2019-03-03_unbridged-knowledge-gaps]]), the distance between what users want
an intelligent assistant to do and what they actually attempt (62% of ideal
needs theoretically addressable, 7% actually attempted)
([[2018-10-21_intelligent-assistant-user-needs]]), employees' information needs
and anxieties during a merger ([[2018-11-04_intranet-merger-or-acquisition]]),
prospective students' four dominant questions
([[2022-07-10_university-ux-professionals]]), how experience level changes what
users want from a calculator ([[2024-03-22_calculator-expectations]]), and what
people value in smart-home devices — a diary study of 10 users that found five
motivations (convenience, understood as cognitive-load relief and not only time
saved; safety and peace of mind; saving resources; tracking home data; mood and
ambiance), that users think in experiences such as "relax after work" rather
than in device-specific actions, and that raw data without context, comparison
or a recommended action does not change behaviour
([[2025-12-05_smart-homes-user-value]]). Research also has to reach past the
happy path: account lockouts, name changes, shared and multiple accounts,
harassment, bereavement and poor connections are not rare exceptions but
"Tuesday afternoon" for a good share of users, so studies must explicitly
explore failure modes and exceptional circumstances rather than assume them away
([[2025-10-24_edge-cases]]). Research routinely
contradicts designer intuition: users know their time zone but not its offset,
and expect alphabetical rather than offset ordering
([[2022-12-11_time-zone-selectors]]).

### Making research land in the organization

Several sources treat adoption as part of the practice, not an afterthought.
Involving stakeholders in research builds empathy and organizational commitment,
and works better when the researcher aligns research goals with stakeholder
goals, starts with small pilots, makes participation logistically easy and
produces lightweight deliverables instead of dense reports
([[2017-02-26_collaborating-stakeholders]]). Research that is merely described
in a document is rarely internalised, so workshops bring stakeholders into it
through participation, in three types matched to audience readiness:
research-alignment workshops that build shared understanding through gallery
walks, affinity diagramming and assumption comparison; empathy workshops that
create emotional connection through persona walkthroughs, journey mapping and
empathy mapping; and research-application workshops that turn insight into
design directions and priorities through opportunity mapping and ideation.
Timeboxed activities with clear prompts and visual outputs are what produce
shared ownership ([[2025-11-21_ux-research-workshops]]); shared artifacts such
as personas and journey maps double as records of common ground that avoid re-explaining
everything ([[2021-05-09_common-ground]]). Ownership is genuinely contested: in
a survey of 372 professionals, 73% of UXers but only 19% of PMs saw discoveries
as a UX responsibility, and only 46% of PMs considered user testing a UX
activity ([[2021-05-02_pm-ux-different-views-of-responsibilities]]) — while
another source positions research as precisely what gives the designer authority
on user needs within the product triad
([[2025-07-18_the-product-triad-designs-role]]). Organizational refusal has its
own catalogue of excuses (no time, too expensive, users don't know what they
want, fear of negative feedback, A/B testing suffices), each rebutted, with the
real obstacle identified as incentives that reward shipping over user value
([[2025-08-22_why-organizations-dont-do-user-research]]). Even when research is
done and understood, recommendations break down between delivery and
implementation through cherry-picking, reinterpretation into familiar design
patterns, deprioritization during crunch, and fuzzy ownership of follow-up. The
chain runs data → findings → insights → recommendations → adoption, and a broken
link anywhere wastes the whole study; researchers typically measure whether they
learned something, never whether anything reached users, which is hope rather
than accountability and is a documented source of burnout as the same study gets
run again. The proposed remedy is to measure adoption explicitly, which also
shows where the value leaks — prioritisation, design or development — and which
teams follow through ([[2025-11-07_research-recommendation-breakage]]).
Communicating research outside a report obeys the same logic of selection: in a
design case study, what lands is the research learning that actually shaped the
thinking and the solution, not the full set of deliverables produced along the
way — the final value counts, not the document presenting it — together with
the real-world impact, measured through data, NPS or qualitative feedback
([[2024-12-03_354_Les_6_tips_de_présentation_d_un_case_study_design_-_Guide_Product_Design]]).
Existing research is also the lever for getting extra effort approved: sharing
interview extracts and success stories internally is what convinces product and
tech teams to invest in the small, unrequested improvements that exceed user
expectations ([[2026-05-12_413_Guide_design_Un_waouh_moment_a_impact_-_Malija_Saifullah]]).

### Tools, AI and the future of the practice

Unmoderated testing tools now sit inside larger research platforms covering
multiple methods, with built-in or integrated participant panels and pricing
models that vary widely ([[2024-12-06_unmoderated-user-testing-tools]]). The
sources are divided in emphasis on AI rather than in substance. AI is credited
with accelerating research planning when the plan is decomposed into components
and the model given organizational context ([[2024-04-05_plan-research-ai]]),
and treated as the latest in a long succession of tool changes that UX has
absorbed, with new technologies historically prompting new methods that must be
validated against established ones ([[2025-05-09_ux-job-with-ai]]). Against
that, an evaluation of four AI analysis tools found they could not process
video, lacked study context, produced vague and uncited recommendations, and
that claims of bias-free analysis are false ([[2023-07-02_ai-powered-tools-limitations]]).
Digital twins and synthetic users are presented as a promising but unresolved
way to scale research, with synthetic users failing to capture messy human
behavior and unresolved questions about consent, misrepresentation and bias
([[2025-08-01_digital-twins]]). And one source draws the line explicitly: hand
recruitment, transcription, data cleaning and draft discussion guides to AI, but
protect moderating, live observation, debriefing and interpretation, because
that is where team learning happens
([[2026-07-17_human-led-research-still-matters]]). A forward-looking piece
argues the same trend from the market side: as design systems commoditize UI,
research-informed understanding becomes the differentiator
([[2026-01-16_state-of-ux-2026]]).
On the tooling side, an AI meeting recorder such as Gong is reported, after six
months of use in research, to remove the friction of asking permission — the bot
joins from the calendar and announces the recording itself — and to produce
high-quality transcripts plus a searchable video-and-text archive useful for
sharing extracts internally, though its keyword search would gain from becoming
semantic. Its most valuable feature for a researcher is the analysis of the
interviewer's own behaviour (talk time, monologues, a patience score), since one
never sees oneself interviewing, nor the biases one induces or the room one
leaves the participant; the value lies in the team ingesting what was said and
working it into the product, not in producing a written summary
([[2025-04-08_372_Gong_l’allié_IA_parfait_pour_vos_user_interviews]]). The object of research shifts as well: designing an AI
agent moves the research questions toward the agent's personality and the
management of its autonomy, and above all toward when and in what form feedback
must be given so the user stays reassured about the actions the agent takes on
its own ([[2025-07-08_385_Designer_un_agent_IA,_ça_veut_dire_quoi_!]]).

### Recurring cautions

- Do not use research to confirm decisions already taken
  ([[2017-09-10_no-validate-in-ux]], [[2025-08-08_research-yes-or-no]],
  [[2017-10-22_false-consensus]]).
- A study that finds nothing wrong indicates a methodology problem, not a
  perfect design ([[2017-09-10_no-validate-in-ux]]).
- Ground stories and assumptions in data; small samples generate extreme,
  misleading numbers and invite false causal explanations
  ([[2017-02-19_narrative-biases]]).
- Users know their problems, not necessarily the solutions; ask about problems,
  behaviors and workflows rather than desired features
  ([[2025-08-22_why-organizations-dont-do-user-research]],
  [[2016-08-14_outcomes-vs-features]]).
- A/B testing shows which variant wins but not why; it does not replace
  qualitative research ([[2025-08-22_why-organizations-dont-do-user-research]]).
- Because a single flaw outweighs many successes in user perception, testing
  should hunt for every defect rather than count wins
  ([[2016-10-23_negativity-bias-ux]]).
- Empathy is not sympathy: it requires qualitative immersion and direct
  exposure, not reports read second-hand
  ([[2019-04-21_sympathy-vs-empathy-ux]]).

## Sources (94)

- [[2016-02-14_revising-personas]] — analytics, usability testing, and support data all inform persona updates.
- [[2016-03-20_game-user-research]] — games user research is a specialized application of UX research methods.
- [[2016-04-10_young-adults-ux]] — This article presents results from a multi-country, multi-method research study establishing evidence-based design guidelines for young adults.
- [[2016-07-31_design-thinking]] — Design thinking begins with empathy and understanding; research and observation of real users ground all subsequent decisions.
- [[2016-08-14_outcomes-vs-features]] — Understanding real user needs requires research and empathy; assumed user needs often lead to solutions nobody wants.
- [[2016-10-16_journey-mapping-ux-practitioners]] — Emphasizes that journey maps require research-grounded narratives to gain credibility and traction, not stakeholder assumptions or preconceptions.
- [[2016-10-23_negativity-bias-ux]] — Understanding that usability failures count more than successes should guide testing focus toward identifying and eliminating every design flaw.
- [[2016-11-13_computer-skill-levels]] — Large-scale research studies reveal actual skill distributions across populations, correcting designers' assumptions about user capabilities.
- [[2017-01-15_ux-stories]] — UX stories must be grounded in real user research rather than imagined scenarios; fabricated stories risk satisfying imaginary needs and missing actual pain points.
- [[2017-02-12_ux-research-cheat-sheet]] — Provides a comprehensive framework for when and how to conduct research across design phases through discovering user needs and validating assumptions via field studies, interviews, and testing, foundational to all phases.
- [[2017-02-19_narrative-biases]] — grounding stories and assumptions in research, not imagination, prevents bias-driven mistakes.
- [[2017-02-26_collaborating-stakeholders]] — involving stakeholders in research activities builds empathy, demonstrates user needs, and creates organizational commitment to UX.
- [[2017-07-30_search-log-analysis]] — search logs as a research method revealing user intent, vocabulary, and unmet needs; supplementing usability testing and interviews with behavioral data.
- [[2017-09-10_no-validate-in-ux]] — the practice of studying user needs, behaviors, and reactions; effective research requires genuine curiosity and openness to finding problems, not proof-seeking.
- [[2017-09-17_ux-research-goals-to-scenarios]] — systematic investigation of user needs, behaviors, and reactions; effective research starts with clear research goals rooted in user tasks and organizational concerns.
- [[2017-10-01_quant-vs-qual]] — defines methodological approaches based on research goals, timing in the design process, and type of evidence needed.
- [[2017-10-22_false-consensus]] — establishes that user research is the antidote to false-consensus bias and required to make valid design decisions.
- [[2017-11-05_ux-mapping-cheat-sheet]] — addresses data gathering approaches underlying mapping methods and research-based vs. hypothesis-driven mapping.
- [[2018-01-14_empathy-mapping]] — Methods for gathering information about user needs, behaviors, and emotions; provides the raw data that empathy maps synthesize and externalize for team alignment.
- [[2018-10-21_intelligent-assistant-user-needs]] — the diverse range of tasks users want assistance with, from simple one-step actions to complex multitask activities requiring information synthesis.
- [[2018-11-04_intranet-merger-or-acquisition]] — the critical importance of understanding employee mental models, concerns, and information needs during organizational upheaval to design effective intranets.
- [[2018-12-09_journey-mapping-101]] — Journey mapping applies user research findings to create shared organizational understanding of customer experience and pain points.
- [[2019-03-03_unbridged-knowledge-gaps]] — Observational research revealing gaps between what users need to know and what sites actually provide to support complex decision-making.
- [[2019-03-24_user-need-statements]] — Qualitative methods like interviews and field studies uncover genuine user needs; need statements that capture goals rather than solutions keep focus on what users are trying to accomplish in their lives.
- [[2019-04-07_journey-mapping-faq]] — Successful maps require qualitative research to understand real customer behavior, not just internal assumptions.
- [[2019-04-21_sympathy-vs-empathy-ux]] — Qualitative methods with open-ended questions reveal the mental models, motivations, and aspirations behind user behavior.
- [[2019-04-28_persuasive-storytelling]] — Stories grounded in real research findings, quotes, and observations are more compelling and credible than generic recommendations.
- [[2019-12-01_usability-testing-101]] — establishes usability testing as a primary means of validating design through direct user observation and feedback.
- [[2020-01-05_ux-quiz-2019]] — addresses research methods, analysis techniques, and evaluation approaches covered in 2019 articles.
- [[2020-01-12_persona-scope]] — Explains that the research approach and questions asked determine what segments emerge, and that research must be narrowly focused to discover meaningful user clusters.
- [[2020-03-15_discovery-phase]] — demonstrates how exploratory research methods (user interviews, field studies, diary studies) and stakeholder interviews form the evidence foundation of discovery.
- [[2020-03-15_gif-emails]] — demonstrates survey research with word-based sentiment analysis as a method to evaluate emotional responses to design choices.
- [[2020-03-22_analyze-customer-journey-map]] — shows how to locate, prioritize, and contextualize user friction within the broader journey narrative using emotional dips and effort assessment.
- [[2020-03-29_remote-ux]] — addresses both moderated and unmoderated remote research methods, technology considerations, and recruiting strategies for distributed participant pools.
- [[2020-06-28_emojis-email]] — two complementary studies on attitudes toward and engagement with emoji-containing emails.
- [[2020-09-20_task-analysis]] — Task analysis is a systematic research method that connects user goals to the tasks performed to achieve them, revealing optimal process flow and opportunities to streamline, simplify, or improve task completion, providing the foundation for design decisions that actually support user work.
- [[2021-05-02_pm-ux-different-views-of-responsibilities]] — Documents significant disagreement on who should own user research activities, with PMs and UXers having conflicting expectations.
- [[2021-05-09_common-ground]] — User testing and research methods serve to build common ground by helping organizations understand their communication partners at large.
- [[2021-05-16_pain-points]] — Frameworks identify customer problems across three levels (interaction, journey, and relationship) using distinct research methods: usability testing for interaction, interviews and studies for journey, and benchmarking for relationship.
- [[2022-05-01_high-income-participants]] — specialized recruitment approaches for accessing specific hard-to-reach demographics.
- [[2022-05-15_personas-archetypes]] — The foundation of both personas and archetypes, capturing user behaviors, attitudes, motivations, pain points, and goals through research data.
- [[2022-07-03_informed-consent]] — Proper consent processes protect participants and improve data quality by ensuring voluntary, understood participation rather than coerced or misled involvement.
- [[2022-07-10_university-ux-professionals]] — Understanding prospective students' information needs, search behaviors, and decision factors through qualitative testing and diary studies informs effective website design.
- [[2022-09-11_antipersonas-what-how]] — Understanding antipersonas requires research similar to persona research; direct studies with threat actors or expert interviews provide evidence for designing effective safeguards.
- [[2022-10-09_personas-study-guide]] — personas require sufficient research foundation; lightweight personas work for simple projects, while qualitative and statistical personas demand more research investment.
- [[2022-12-11_time-zone-selectors]] — Quantitative and qualitative testing across multiple countries revealed that designers' assumptions about optimal time-zone organization often conflict with actual user expectations and mental models.
- [[2023-02-05_discovery-in-agile]] — User research is one component of Agile discovery, but not the only one; secondary research, stakeholder interviews, and analytics often provide sufficient insight within sprint timeframes.
- [[2023-02-12_using-empathy-maps]] — empathy maps provide an accessible way for non-researchers to contribute observations and help teams collectively analyze and share research insights.
- [[2023-07-02_ai-powered-tools-limitations]] — researchers must adopt careful verification practices when using AI tools and maintain skepticism toward marketing claims about automation.
- [[2023-11-24_ai-prompt-structure]] — diary study methodology systematically analyzed actual AI usage patterns to identify prompt structures and their effectiveness across conversation types.
- [[2024-01-26_open-ended-questions]] — foundational to user-centered design practice, employing both open and closed questioning strategies.
- [[2024-02-02_card-sorting-definition]] — employing both qualitative and quantitative approaches to understand how users expect content to be structured.
- [[2024-03-22_calculator-expectations]] — documents how user behavior with calculators differs based on experience level and problem-space familiarity.
- [[2024-04-05_plan-research-ai]] — demonstrates how AI tools can accelerate research planning for UX professionals.
- [[2024-06-14_ai-imagegen-stages]] — contextual inquiry revealed user needs and pain points in AI image generation, highlighting opportunities for tool improvement (especially in refinement).
- [[2024-06-14_card-sorting-terminology-matches]] — effective UX research requires attention to research design; careful card labeling and facilitation prevent biases that would otherwise invalidate findings.
- [[2024-10-22_Bonus_Nouvel_outil_design_en_approche]]
- [[2024-12-03_354_Les_6_tips_de_présentation_d_un_case_study_design_-_Guide_Product_Design]]
- [[2024-12-06_unmoderated-user-testing-tools]] — Explains that modern unmoderated tools are typically part of larger research platforms supporting multiple research methods beyond just unmoderated testing.
- [[2024-12-17_356_Excel_test_la_méthode_d_UX_Research_B2B_idéale]]
- [[2025-04-01_371_L_interview_longue_en_phase_de_Discovery_-_Guide_UXR]]
- [[2025-04-08_372_Gong_l’allié_IA_parfait_pour_vos_user_interviews]]
- [[2025-04-18_convenience-vs-probability-sampling]] — distinguishes sampling approach appropriateness based on research goals and stakes, from exploratory studies to population-level inferences.
- [[2025-05-09_ux-job-with-ai]] — documents how new technologies prompt creation of new research methods requiring validation against established approaches.
- [[2025-07-08_385_Designer_un_agent_IA,_ça_veut_dire_quoi_!]]
- [[2025-07-18_the-product-triad-designs-role]] — User research is emphasized as the foundation for the designer's authority on user needs and ability to influence the team's direction.
- [[2025-07-25_strategies-complex-application-design]] — Multiple research methods and stakeholder involvement are emphasized as critical for understanding complex systems beyond conventional user-centered approaches.
- [[2025-08-01_digital-twins]] — Digital twins represent a new methodological approach to scaling and accelerating user research.
- [[2025-08-08_research-yes-or-no]] — The article critiques how research is misused for validation and advocates for more nuanced research approaches.
- [[2025-08-22_why-organizations-dont-do-user-research]] — The article comprehensively addresses why organizations avoid research and how to counter objections.
- [[2025-09-23_396_UX_Research_en_StartUp,_guide_et_astuces]]
- [[2025-10-03_persona]] — Shows how field studies, surveys, interviews, and longitudinal studies form the foundation for persona creation; personas must be based on actual user data, not assumptions.
- [[2025-10-24_edge-cases]] — what this article contributes to this concept
- [[2025-11-07_research-recommendation-breakage]] — what this article contributes to this concept
- [[2025-11-21_ux-research-workshops]] — demonstrates how to make research accessible through interactive workshops that help stakeholders internalize research insights.
- [[2025-11-28_diary-study-entries]] — what this article contributes to this concept
- [[2025-12-05_smart-homes-user-value]] — what this article contributes to this concept
- [[2026-01-16_state-of-ux-2026]] — Research becomes more essential as AI and automation reduce friction in other areas; deep understanding of users drives competitive advantage.
- [[2026-01-23_user-panels-101]] — Panels represent foundational infrastructure for scaling research across organizations; they support continuous, systematic user engagement.
- [[2026-02-17_401_Prototypage_Le_guide_design_complet_-_Figma,_Lovable,_Google_Sheets_et_+]]
- [[2026-03-03_403_Guide_Tester_un_concept_design_produit_en_interneexterne_-_Podcast_Product_Design]]
- [[2026-05-12_413_Guide_design_Un_waouh_moment_a_impact_-_Malija_Saifullah]]
- [[2026-07-17_human-led-research-still-matters]] — produces both findings and shared team learning; outsourcing the entire process to AI removes the learning value even if findings quality remains high.
- [[2018-02-12_solving-design-exercises_11-step-3-understand-the-customer-s-context-and-needs-when-and]] — the chapter introduces user stories and customer journey mapping as research techniques to understand customer needs and pain points.
- [[2013-08-01_just-enough-research_01-foreword]] — The foreword argues research helps teams avoid wrong problems, manage internal politics, and win strategic debates within organizations.
- [[2013-08-01_just-enough-research_02-chapter-1-enough-is-enough]] — Hall defines design research as inquiry integral to the design work itself, focusing on understanding the people for whom designers build, distinct from academic design research about design theory; The chapter argues research saves time and effort by validating assumptions, reducing risk of solving the wrong problem, and providing stronger arguments for design decisions.
- [[2013-08-01_just-enough-research_06-chapter-5-user-research]] — this chapter presents ethnographic research as the method for understanding users in context; it allows teams to replace assumptions with insight, understand true needs and priorities, learn how users see the world and use language, and develop personas.
- [[2016-11-04_ux-research_01-foreword]] — The philosophical foundations of user research as a question-driven, human-centered practice distinct from purely academic data collection.
- [[2016-11-04_ux-research_05-chapter-4-qualitative-research-methods]] — covered extensively through contextual inquiry (think-aloud and ride-along studies), where researchers observe customers performing tasks in context and ask probing questions to gain deeper understanding of motivations and barriers
- [[2016-11-04_ux-research_07-chapter-6-logistics]] — field methods and participant management as core components of systematic user research.
- [[2016-11-04_ux-research_08-chapter-7-recruiting]] — participant selection as a foundational step to any user research effort, whether qualitative or quantitative.
- [[2016-11-04_ux-research_09-chapter-8-making-research-happen]] — participant-centered research as a team effort balancing consistency with flexibility.
- [[2022-01-19_product-management-for-ux-people_06-chapter-3-ux-skills-that-carry-over]] — UX research experience is a natural strength for PM; the chapter emphasizes collaboration with researchers rather than running PM research in parallel, and learning to accept research methods different from UX ideals, while maintaining the commitment to frequent customer contact.
- [[2022-01-19_product-management-for-ux-people_08-chapter-5-the-business-of-product-is-business]] — Gauging market interest is user research by another name (identifying customers, pain points, needs, mental models); customer obsession means ravenous consumption of survey data, app reviews, social-media feedback, and qualitative insights from support, success, and community teams.
