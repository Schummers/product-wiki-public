---
type: concept
name: Research Planning
created: 2026-07-31
updated: 2026-09-10
status: developed
---

# Research Planning

## Definition

Research planning is the work done before data collection: defining goals,
choosing a method, deciding who participates, and preparing the materials the
study will run on. Its artifact is the research plan — a document outlining the
goals, methods and logistical details of a study, called a test plan when the
study is a usability test [[2024-11-01_pm-research-plan]]. The same source argues
it is not bureaucratic overhead: the act of planning structures thinking and
stops important considerations from being missed, it creates transparency with
stakeholders, and it makes the study reproducible later.

Across the sources, planning is where the method-specific constraints get
resolved: session structure and technical setup for remote work
[[2022-11-13_remote-contextual-inquiry]], protocol flexibility and location for
field studies [[2023-02-19_tips-user-research-field]], cadence, incentives and
attrition for longitudinal studies [[2024-03-29_diary-studies]], and how
participants are selected at all [[2025-04-18_convenience-vs-probability-sampling]].
Two recent additions cover the use of generative AI as a planning assistant
[[2024-04-05_plan-research-ai]] [[2024-09-27_research-with-ai]].

The foreword to *UX Research* frames the same starting point from research
philosophy rather than process: modern product research begins with the
questions a team needs answered, not with data collection for its own sake,
and doing it well takes practice, reflection and mentorship rather than being
a low-barrier skill [[2016-11-04_ux-research_01-foreword]].

## Practice

### What a research plan contains

[[2024-11-01_pm-research-plan]] lists four components: purpose and goals,
participants, method and procedure, and links to relevant documents such as
consent forms and interview guides. Two of them carry specific requirements.
Participants need explicit inclusion and exclusion criteria — which
characteristics are required, and which would invalidate the study — so
recruitment targets the right people. The method section should be detailed
enough for replication: session length, tools, tasks and procedure described so
another researcher could run a comparable study.

Its practical tips: share the plan with stakeholders to build buy-in and to let
them know when they can observe sessions or expect deliverables, provide observer
guidelines, keep personally identifiable information out by using codes (P1, P2),
and update the plan after the study to record what actually changed during
sessions.

### Planning the questions themselves

[[2016-11-04_ux-research_03-chapter-2-good-research-starts-with-good-questions]]
treats question-writing as a planning discipline in its own right: every
question should tie back to the research objectives, and one that doesn't
should be cut from the guide. It gives a question anatomy — a setup (what,
why, how, when, where), an area of inquiry, laddering (follow-up probes for
deeper detail), and a segue into the next question — and lists four pitfalls
to plan against: leading questions, shallow yes/no questions, personal bias,
and unconscious bias. Once a guide has been practiced, the authors note the
same pitfalls can be broken deliberately: a leading question to build trust,
a shallow question to ease a participant into comfort, or a personal-bias
question to spark discussion through devil's advocacy.

### Choosing a method as a planning decision

[[2016-11-04_ux-research_06-chapter-5-choosing-your-methods]] frames method
choice itself as a planning question, resolved by working through what the
design team and stakeholders need to know, what sample size and participant
locations are realistic, and what budget and timeline are available. It
structures the trade-off as a project triangle of time, budget and scope:
identify which two constraints matter most for this study and let the third
vary. On combining methods, its planning guidance is to pair a qualitative
and a quantitative measure aimed at the same root question rather than
forcing one method to serve unrelated goals, and to run separate research
tracks when the questions being asked are genuinely distinct.

### Deciding how participants are selected

[[2025-04-18_convenience-vs-probability-sampling]] frames sampling as a planning
decision driven by stakes rather than by rigour for its own sake. Convenience
sampling — nonrandom recruitment of readily available participants — is the UX
default and is defensible: it is fast and cheap, and sufficient for qualitative
usability testing, exploratory research and iterative feedback, because most
studies aim to find usability problems rather than to generalize statistically.
Probability sampling requires a well-defined population, a complete contact list,
a random selection method, and larger samples (40+ for quantitative usability
testing, 100+ for surveys).

The article's planning heuristic: reach for probability sampling when inferring
how prevalent a behaviour is in a broader population, when the user base is
diverse enough that recruitment bias would skew results, when decisions carry
high stakes (healthcare, finance, automotive), or when statistical comparisons
between groups are involved. It also warns that quotas are not randomness — a
convenience sample stratified by age still carries hidden biases such as
emotional state, cultural influence, or willingness to participate.

### Planning recruitment: profiles, screeners, quotas

[[2016-11-04_ux-research_08-chapter-7-recruiting]] treats recruiting as a
risk-management item that has to be planned before sessions are scheduled:
start from existing sources (past qualitative research, analytics reports,
marketing's customer segments) or write baseline user profiles, so
recruitment criteria stay aligned with the research goals. Screeners should
be surveys of 10-15 minutes using multiple-choice questions that confirm or
disqualify candidates on behavioral demographics, not just age and income.
Assuming participant availability is not an issue, the plan should set a
quota of three to five participants per user profile, adjusted for how
important that profile is and how hard it is to reach. Recruitment method
and lead time are planning variables too: self-recruiting is slow and needs
a minimum of two weeks, while in-person and online intercepts, cold calling,
and third-party or client-based recruiters trade speed against cost and
control. The plan should also schedule backup participants in advance, since
no-shows are common, and anticipate that some screened participants will
still turn out to be a mismatch ("duds") once they arrive.

### Piloting and rehearsing before the real sessions

Pilots recur across methods. [[2023-02-19_tips-user-research-field]] lists
pre-research pilots as a condition of successful field studies;
[[2024-03-29_diary-studies]] includes pilot testing in the planning requirements
for diary studies; [[2022-11-13_remote-contextual-inquiry]] recommends practising
the technical setup with each participant in a 10-minute video call before the
session, and communicating screensharing needs, firewall restrictions and
recording permissions upfront.
[[2016-11-04_ux-research_03-chapter-2-good-research-starts-with-good-questions]]
frames the same practice as validating the interview guide: dry runs with
coworkers, done before real sessions, are the place to revise question order
and wording without affecting real participant data.

### Planning session logistics

[[2016-11-04_ux-research_07-chapter-6-logistics]] adds a layer of planning
most other sources leave implicit: qualitative field research needs more
preparation than quantitative work, and a consistent pre-, between- and
after-session checklist (tech checks, paperwork, participant familiarization,
observer orientation, supplies) prevents disruption and signals
professionalism. For sensitive topics, welcome kits go out three to four days
ahead with project information, team bios and photos, and a point of contact
participants can use to verify the study is legitimate. The plan should also
specify the paperwork (nondisclosure agreements, recording waivers,
permission-to-quote forms) and the honorarium format (cash split into
individual envelopes, gift cards, or free product, with receipts to document
payment). Remote sessions need 5-10 minutes of tool training built into the
plan, since many participants do not use conferencing software daily, plus
technical contingencies such as a backup conference bridge and an analog
fallback for the prototype. The chapter's closing point is to plan for
flexibility as well as detail: unexpected issues are normal, and usually
invisible to everyone but the researcher.

### Planning session length and how many sessions

[[2022-11-13_remote-contextual-inquiry]] plans duration around virtual attention
spans: 2-3 hours maximum, split between observation and discussion, with
additional sessions scheduled when the workflow is too long to cover in one
sitting. [[2024-03-29_diary-studies]] plans on a different axis entirely — days
to months — and asks the plan to define the data-collection cadence upfront:
event-based (log when a specific interaction occurs), interval-based (report at
regular intervals) or signal-based (respond to a prompt). Its other planning
variables are sample size targeted at saturation (typically 5-50 depending on
scope and variance across user groups), incentives reflecting the time commitment
(roughly $40/hour for US participants), recruitment that anticipates dropouts,
and a tool choice among all-in-one apps (streamlined but expensive), survey tools
(free but manually coordinated) and messaging apps (informal but easy for
participants). For studies longer than a week it recommends splitting the
incentive into milestone installments to sustain engagement.

### Planning for a protocol that will change

[[2023-02-19_tips-user-research-field]] makes adaptability an explicit planning
item rather than an accident: prepare stakeholders for the fact that research
questions may evolve across sessions as insights emerge, unlike surveys where
consistency is mandatory. Its other pre- and post-session planning points:
monitor recruiting closely to avoid professional volunteers and superusers and to
get diversity of ethnicity, role, gender and task experience; decide deliberately
whether sessions happen in the natural setting (realistic context and
distractions) or in a controlled space (privacy and focus); plan for observers,
who bring context and become advocates for change but can overwhelm participants
if unmanaged; at a business location, reserve a private room for the team;
document immediately, taking notes even when recording, numbering participants
and documents for privacy and dating everything; and debrief right after each
session while observations are fresh.

### Using generative AI to build the plan

[[2024-04-05_plan-research-ai]] is against asking an AI for a whole research plan
at once, which produces a generic template. The recommended approach is
componentized: decompose the plan and handle context, research questions,
methods, criteria and screeners separately. Start by giving organizational
context, a product or service description and the learning objectives. Generate
10+ research questions, filter duplicates offline, refine them, and only then ask
which methods suit which questions and why — noting that generative AI tends to
over-suggest triangulation or behavioural methods where attitudinal ones would
fit. Study collateral (screeners, interview questions, tasks) can be drafted by
AI but needs specific guidance to avoid priming, vague task instructions and poor
screener distractors, and its first attempts are often poor, which the article
flags as a major risk area for new researchers. The framing rule: treat the tool
as a UX assistant, not a UX mentor.

[[2024-09-27_research-with-ai]] maps the same capability across the whole
research lifecycle and agrees on planning: AI helps generate research questions,
create study templates and draft consent forms and recruitment materials,
removing tedious administrative work. Its limits are stated just as firmly — AI
cannot observe behaviour or watch a usability test, only analyse what users say;
it is stochastic and may attend to the wrong aspects of the data; and contextual
understanding, cultural awareness and connecting evidence across a study remain
human. Both articles land on the same posture: AI works like an intern, needing
ample instructions, context, constraints and correction, and its output is a
starting point subject to expert review.

## Sources (15)

- [[2022-11-13_remote-contextual-inquiry]] — successful remote contextual inquiry requires testing technical setup beforehand, planning session duration for virtual settings, and planning multiple sessions for complex workflows.
- [[2023-02-19_tips-user-research-field]] — successful field studies require pre-research pilots, stakeholder preparation for adaptive protocols, consideration of location trade-offs, and post-session debriefing to capture insights while fresh.
- [[2024-03-29_diary-studies]] — covers comprehensive planning requirements including timelines, participant profiles, tools, communication, pilot testing, and protocols.
- [[2024-04-05_plan-research-ai]] — provides systematic approaches to using generative AI for methodical research-plan development.
- [[2024-09-27_research-with-ai]] — the process of designing research studies, defining goals and methods, preparing documentation, and setting up for effective data collection.
- [[2024-11-01_pm-research-plan]] — the process of structuring and documenting research studies before they are conducted, including defining goals, selecting methods, and preparing all necessary materials.
- [[2025-04-18_convenience-vs-probability-sampling]] — guides teams in assessing research stakes, participant diversity, and decision impact to determine appropriate sampling method and resource allocation.
- [[2013-08-01_just-enough-research_03-chapter-2-the-basics]] — Hall argues research activities must be chosen to support specific project decisions and situated in the researcher's professional context (freelance, agency, in-house, startup, agile), with explicit purpose statements and expected outcomes.
- [[2013-08-01_just-enough-research_04-chapter-3-the-process]] — this chapter defines the planning phase as identifying the point person, deciding time and budget, determining participants and roles, and preparing for change when new facts emerge.
- [[2013-08-01_just-enough-research_11-conclusion]] — stressed as a matter of determining which approaches fit your context, available resources, and goals; the process is "Form questions. Gather data. Analyze," with many possible approaches depending on constraints.
- [[2016-11-04_ux-research_01-foreword]] — The importance of starting with good questions and planning research around specific information needs rather than the collection of data for its own sake.
- [[2016-11-04_ux-research_03-chapter-2-good-research-starts-with-good-questions]] — Research begins with planning questions around your goals; every question should tie back to research objectives, and questions should progress naturally through a conversation rather than read like a verbal questionnaire.
- [[2016-11-04_ux-research_06-chapter-5-choosing-your-methods]] — planning is central to method selection, requiring practitioners to clarify their questions, understand stakeholder needs and goals, assess available sample size and location, evaluate budget and timeline constraints, and balance competing priorities using the project triangle
- [[2016-11-04_ux-research_07-chapter-6-logistics]] — documenting research goals and hypotheses, designing discussion guides, and preparing logistics before sessions begin.
- [[2016-11-04_ux-research_08-chapter-7-recruiting]] — documenting target profiles and recruitment screeners before recruiting begins, informed by existing data and stakeholder input.
