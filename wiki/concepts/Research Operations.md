---
type: concept
name: Research Operations
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "AI and Research Operations"
  - "ResearchOps"
---

# Research Operations

## Definition

Research Operations (ResearchOps, ReOps) is the orchestration and optimization
of people, processes, and craft in order to amplify the value and impact of
research at scale [[2020-08-16_research-ops-101]]. It is described as a
specialized subcomponent of Design Operations, applying the same orchestration
logic to the operational challenges specific to user research: participant
logistics, insight sharing, research memory, and methodology consistency
[[2019-11-10_design-ops-faq]]. Kate Towsey frames it more broadly still, as
"the systems that enable people to do research, […] consume research, and act on
research" [[2025-02-14_researchops-kate-towsey]].

The discipline emerged from the growth of the UX profession and the practical
problem of meeting rising research demand without a proportional rise in cost:
when an organization runs ten times more research, ResearchOps practices should
let cost scale to eight or nine times the original budget rather than eleven,
through economies of scale and reuse [[2020-08-16_research-ops-101]]. It is
consistently described as far broader than participant recruitment alone,
covering standardization of methods, participant management, ethics, partner
education, insight management, and the socialization of research impact
[[2020-08-16_research-ops-101]]. Its concrete expressions in the corpus include
participant panels and databases [[2023-05-07_research-participant-database]]
[[2026-01-23_user-panels-101]], research repositories
[[2024-07-26_why-repositories-fail]], workflow automation
[[2022-12-11_automating-research-workflows]], and adoption metrics
[[2026-02-20_recommendation-adoption-score]].

## Practice

### The component model

Two overlapping decompositions appear in the sources. NN/g's ResearchOps 101
names six focus areas: participants (recruiting, screening, scheduling,
compensating), governance (consent, privacy, information storage), knowledge
(collecting, synthesizing, sharing insights), tools (consistent toolsets),
competency (enabling others to perform research), and advocacy (defining and
sharing research value) [[2020-08-16_research-ops-101]]. Towsey names eight
interconnected functions: participant recruitment, knowledge management,
onboarding, tools, ethics, metrics, program management, and people development,
all operating inside an organization's culture and practice
[[2025-02-14_researchops-kate-towsey]]. Both stress the same structural point:
the areas are interwoven, every component affects and is affected by the others,
and touching one means ending up working on all of them
[[2020-08-16_research-ops-101]] [[2025-02-14_researchops-kate-towsey]].

### Getting started

Begin by identifying the current pain points of researchers and of the research
team's partners through internal research, then concentrate initial effort on
the most pressing area while keeping the components in balance
[[2020-08-16_research-ops-101]]. Towsey adds a sequencing constraint: strategy
precedes operations. Business goals inform research strategy, which in turn
determines what operational support is needed; without that clarification you
get reactive "knee-jerk operations" rather than systems
[[2025-02-14_researchops-kate-towsey]]. Even when the ambition is large-scale,
start with scoped pilot efforts and expand gradually
[[2025-02-14_researchops-kate-towsey]].

### Ownership, governance, and roles

Dedicated roles such as design producers, program managers, and ResearchOps
specialists help a practice mature, but design managers and senior designers
often handle these tasks successfully without a formal role
[[2019-11-10_design-ops-faq]]. Where ownership is absent, systems decay: 29% of
research repositories surveyed had no owner, and without dedicated governance
and advocacy they quickly become disorganized and forgotten
[[2024-07-26_why-repositories-fail]]. The same requirement recurs for adoption
tracking, which needs clear ownership, governance, and regular review to sustain
[[2026-02-20_recommendation-adoption-score]], and for panels, where governance
is the sixth and final step that makes privacy, consistency, and sustainability
possible [[2026-01-23_user-panels-101]].

On governance proper: consent templates must comply with data-privacy
regulations such as GDPR and use plain language, and organizations need
processes for the proper maintenance and disposal of personally identifiable
information and study artifacts [[2020-08-16_research-ops-101]]. Panel work
should be done with legal and compliance teams on security policies, storage
methods, and GDPR compliance, with the resulting policies communicated clearly
to opt-in participants [[2023-05-07_research-participant-database]].

### Participants: panels and databases

An internal participant panel is a curated group of opted-in customers or target
users who agree to future research contact — research infrastructure rather than
a list [[2026-01-23_user-panels-101]]. Reported benefits are speed (no-show
rates drop around 20%), cost (external recruiting is expensive), and lasting
customer relationships [[2026-01-23_user-panels-101]]; panels also let
researchers spin up small studies for quick insights
[[2023-05-07_research-participant-database]].

Building one is a six-step process: recruit, organize and segment, contact and
schedule, incentivize and engage, re-engage and manage, and establish governance
[[2026-01-23_user-panels-101]]. Practical rules from the participant-database
guidance: choose tools by team maturity (spreadsheets are simple but manual, CRM
software adds structure, specialized tools streamline the full workflow at
higher cost); collect only the demographic and qualification data you actually
need, since excess data creates maintenance and storage obligations; track
engagement history (last contact, participation dates, articulation level, study
count) to avoid over-recruiting the same people; populate the panel from
existing customer touchpoints such as support interactions, surveys, events, and
social media; and audit regularly, removing stale contacts and making opt-out
easy at every contact [[2023-05-07_research-participant-database]]. The tool
spectrum is described the same way for panels: purpose-built research platforms
offer study management, CRMs structure profiles, general tools like spreadsheets
are inexpensive but risky at scale [[2026-01-23_user-panels-101]].

Both sources flag the same bias risk: a panel may skew toward loyal customers
and fans [[2023-05-07_research-participant-database]], and existing customers
will not reflect new-user perspectives, which is why hybrid approaches combining
an internal panel with external recruiting for reach and diversity are standard
[[2026-01-23_user-panels-101]]. Panel maturity itself is treated as a maturity
signal, ranging from informal spreadsheets to structured systems with automation
and governance [[2026-01-23_user-panels-101]].

### Knowledge, repositories, and research memory

Compiled research insights help teams avoid repeating studies and educate people
outside the research team; a shared insight database across the organization
creates a comprehensive source of knowledge [[2020-08-16_research-ops-101]].
The repository research qualifies this heavily. Tool choice affects adoption:
collaboration software shows the lowest satisfaction and adoption, while
user-research platforms and database tools report higher adoption despite higher
cost, thanks to better usability and search
[[2024-07-26_why-repositories-fail]]. Contribution must be effortless: if adding
research requires excessive tagging or duplicated work, researchers deprioritize
it, so the repository has to be integrated into existing workflows
[[2024-07-26_why-repositories-fail]]. The recommendation is to treat building a
repository like building a product, applying a user-centered approach to it, and
to sustain post-launch advocacy through newsletters, team meetings, Slack
sharing, and reminders [[2024-07-26_why-repositories-fail]].

The strongest caution is structural: low organizational UX maturity prevents
success, and a repository "will not address the root cause problem your company
likely has, which is a broken decision-making process based on political power
and gut feelings" [[2024-07-26_why-repositories-fail]].

### Standardization and automation

Standardizing research methods and the supporting documentation (scripts,
templates, consent forms) lets teams apply them consistently and saves planning
time [[2020-08-16_research-ops-101]]. Automation attacks the administrative
overhead directly. The recommended way in is to look for manual, repetitive
activities, especially moving data between tools and manually tracking study
progress [[2022-12-11_automating-research-workflows]]. Documented targets:
webhook-based scripts for recruitment emails, screening, and cross-platform
scheduling (worked in batches to preserve quality control); automated
confirmations, internal announcements, reminders, and consent forms; scripts
that watch email or survey submissions to track diary-study progress and prompt
lagging participants; automatic incentive distribution on study completion via
platforms like BHN Rewards; and automated upload of survey responses into
analysis tools like Dovetail for real-time coding and progress tracking
[[2022-12-11_automating-research-workflows]]. Beyond commercial tools such as
Zapier, custom webhooks, Google Apps scripts, and desktop tools like Apple
Automator can handle file preparation, participant folder setup, and environment
configuration [[2022-12-11_automating-research-workflows]].

On AI specifically, the guidance is deliberately measured: AI is one tool among
many, and teams must evaluate where it genuinely smooths processes or takes over
a task versus where human judgment and context remain essential. Budget cuts,
layoffs, and pressure to reduce headcount often arrive before AI effectiveness
has been proven, so a balanced perspective is needed
[[2025-02-14_researchops-kate-towsey]].

### Advocacy and measuring the impact of operations

Advocacy — defining and sharing the value of research — is one of the six focus
areas [[2020-08-16_research-ops-101]]. To secure buy-in, track and communicate
metrics such as participants recruited, reports produced, and people impacted by
ResearchOps improvements, and make sure that visibility reaches the right
organizational level [[2025-02-14_researchops-kate-towsey]]. Panels similarly
require organizational buy-in, with the advocacy message tailored to what each
stakeholder cares about [[2026-01-23_user-panels-101]].

The Recommendation-Adoption Score offers one concrete operational metric for the
downstream half of ResearchOps: it treats recommendations as inventory, each
with a description, an owner, a definition of done, and evidence tied back to
it, and assigns each a status (Adopted, Committed, Communicated, Canceled) and a
user-value rating. RAS = (actual user value ÷ total possible user value) × 100,
read against ranges from Poor (0–29, research ignored) to Great (80–100)
[[2026-02-20_recommendation-adoption-score]]. Trends over a rolling 12-month
window matter more than any single score, and the act of tracking adoption
itself starts conversations that had not been happening
[[2026-02-20_recommendation-adoption-score]].

### The operational work inside a single study

Alongside the organization-wide framing above, *UX Research* documents
ResearchOps at the scale of one session: the preparation, supplies, session
flow and cleanup that make a study run [[2016-11-04_ux-research_07-chapter-6-logistics]],
and the roles, timing and execution details needed to run sessions safely and
professionally [[2016-11-04_ux-research_09-chapter-8-making-research-happen]].
A consistent pre-, between- and after-session checklist — tech checks,
paperwork, participant familiarization, observer orientation, supplies —
prevents disruption and signals professionalism; qualitative field research
in particular needs more of this preparation than quantitative work
[[2016-11-04_ux-research_07-chapter-6-logistics]]. Operational governance
shows up here too, in the form of paperwork: nondisclosure agreements,
recording waivers and permission-to-quote forms, plus a documented
honorarium (cash split into individual envelopes, gift cards, or free
product, with receipts) [[2016-11-04_ux-research_07-chapter-6-logistics]].

Running a session is presented as a minimum two-person operation — a
moderator to guide the conversation and a note taker to capture
observations, since listening, formulating a response and taking notes at
once is very difficult for one person — with roles that can rotate between
sessions, and dry runs with colleagues used to test technology, flow and
timing before real participants arrive
[[2016-11-04_ux-research_09-chapter-8-making-research-happen]]. Observers are
folded into the same operational discipline: they dial in remotely or watch
behind one-way glass, are expected to write down questions rather than
interrupt, and are debriefed after the session
[[2016-11-04_ux-research_09-chapter-8-making-research-happen]].

### Research as a continuous, not discrete, operation

[[2016-11-04_ux-research_16-chapter-15-getting-the-most-out-of-research]]
extends ResearchOps thinking to the cadence of research itself: the chapter
frames research as an ongoing operational practice integrated throughout
product development rather than a discrete phase, with teams planning their
next research efforts out of internal workshop discussions and maintaining
continuous inquiry as market conditions and user behavior change. This
reframes advocacy and knowledge management, above, as a standing operational
loop rather than a one-time setup: as questions get answered, new ones
surface, and the operational job is to keep the loop running rather than to
close it out after a single study.

### Why the work is underestimated

Two sources converge on the organizational cause. Decentralized and embedded
design teams lack regular communication channels, producing redundant effort and
outdated processes, and designers pulled into strategic work have less time for
core craft — the conditions that make operational support necessary in the first
place [[2019-11-10_design-ops-faq]]. Towsey attributes the chronic
underestimation of ResearchOps effort to the interconnection itself: the Venn
diagram of functions is not understood, so the time required is wildly
underestimated [[2025-02-14_researchops-kate-towsey]].

## Sources (11)

- [[2019-11-10_design-ops-faq]] — introduces ResearchOps as specialized operational support for user research teams facing their own set of scaling challenges.
- [[2020-08-16_research-ops-101]] — ResearchOps is a specialized operational discipline focused on scaling research practices by optimizing people, processes, and craft across multiple interconnected focus areas.
- [[2022-12-11_automating-research-workflows]] — ResearchOps focuses on streamlining research processes; automation of administrative tasks increases researcher productivity and reduces resource requirements.
- [[2023-05-07_research-participant-database]] — The systems and processes that enable UX teams to conduct research at scale, including participant recruitment, scheduling, and data management infrastructure.
- [[2024-07-26_why-repositories-fail]] — covers the operations, tools, and processes required to scale user research across teams.
- [[2025-02-14_researchops-kate-towsey]] — ResearchOps is an interconnected ecosystem of functions enabling research delivery, consumption, and action with strategic alignment to business goals and holistic systems thinking; AI's role requires balanced evaluation of where it genuinely improves efficiency versus where human judgment and context remain essential.
- [[2026-01-23_user-panels-101]] — Panels require operational systems: segmentation, contact management, participation tracking, incentive distribution, and governance to sustain over time.
- [[2026-02-20_recommendation-adoption-score]] — RAS is an operational system for tracking and improving research adoption; it requires clear ownership, governance, and regular review to sustain.
- [[2016-11-04_ux-research_07-chapter-6-logistics]] — preparation, supplies, session flow, and cleanup required to run user research sessions.
- [[2016-11-04_ux-research_09-chapter-8-making-research-happen]] — roles, timing, logistics, and execution details required to run sessions safely and professionally.
- [[2016-11-04_ux-research_16-chapter-15-getting-the-most-out-of-research]] — the chapter frames research as an ongoing operational practice integrated throughout product development, not a discrete phase. Teams should plan their next research efforts based on internal workshop discussions and maintain continuous inquiry as market conditions and user behavior change.
