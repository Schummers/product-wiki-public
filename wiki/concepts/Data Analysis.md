---
type: concept
name: Data Analysis
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Data Collection"
  - "Data Interpretation"
  - "Data Synthesis"
  - "Research Synthesis"
  - "Data Tracking"
---

# Data Analysis

## Definition

Data analysis is the work of examining collected observations and measurements
to identify patterns, and then interpreting those patterns so they can inform
decisions [[2023-04-23_data-findings-insights-differences]]. The sources
describe it as a ladder with three rungs: raw data points, which have no
significance on their own; findings, which name the patterns present in the
data without explaining them; and insights, which interpret findings in context
of past research, business objectives and user needs, and are the only level a
team can confidently act on [[2023-04-23_data-findings-insights-differences]].
*UX Research* supplies a working definition of the base unit beneath that
ladder: a data point is a single thought, concept, or idea. It distinguishes
discrete quantitative data points (a cell in a spreadsheet) from qualitative
ones (a conversational observation), and insists a qualitative data point that
bundles several observations — for example, "participant found the checkout
flow complex and wished guest checkout was available" — should be split apart,
so the team can see where different observations overlap and organise them
later ([[2016-11-04_ux-research_14-chapter-13-making-sense-of-the-mess]]).
Analysis and synthesis alternate throughout: analysis breaks the material down
into manageable units, synthesis recombines it into explanations
[[2025-05-02_analyze-usability-data]].

The techniques differ by data type — thematic analysis and coding for
qualitative material, statistics for quantitative
[[2023-04-23_data-findings-insights-differences]] — but the failure modes are
shared: skimming instead of reading, latching onto memorable moments, producing
description rather than interpretation, and ignoring contradictions
[[2022-08-17_thematic-analysis]], [[2025-05-02_analyze-usability-data]]. The
sources treat judgement as the irreducible part: assessing reliability, asking
sharp questions, deciding which patterns actually matter for a decision
[[2025-06-06_future-proof-designer]], [[2026-03-06_practical-significance]].

## Practice

### Budgeting time for analysis

*UX Research* argues analysis is worth planning for rather than skipping
straight to design: formal analysis creates shared understanding and a common
language across the team, while skipping it creates more problems than it
solves. Its rule of thumb is roughly three hours of analysis for every hour of
research — 8–12 hours reviewing recordings and coding notes, 8–12 hours
organising and reorganising the data, and 8–12 hours analysing for
opportunities — an accounting meant to stop teams from underestimating the
work required ([[2016-11-04_ux-research_14-chapter-13-making-sense-of-the-mess]]).

### Assess the data before you interpret it

Individual data points cannot be taken at face value. Positive feedback may
come from a leading question, participants contradict themselves, and behaviour
diverges from stated preference; each point must be read against the other
points and against what is known about recruitment, study design and
facilitation events [[2025-04-11_usability-data-in-analysis]]. Six dimensions
structure that assessment: **authenticity** (was the comment natural, or shaped
by a wish to please the facilitator or by professional-participant status),
**consistency** (when a participant calls a task easy but struggled, errored or
restarted, prioritise the behavioural data), **repetition** (recurring comments
or behaviours across sessions signal genuine sentiment or a real usability
problem), **spontaneity** (unprompted actions and remarks beat those elicited by
priming or by revealing the study's purpose), **appropriateness** (participant
representativeness and task realism) and **confounds** (order effects, complex
task instructions, fatigue) [[2025-04-11_usability-data-in-analysis]]. The
framework applies independently of sample size, to qualitative and quantitative
research alike [[2025-04-11_usability-data-in-analysis]].

*UX Research* treats the same signal — repetition — primarily as a discovery
tool rather than a filter: redundancy across participants is a good sign, and
the chapter recommends writing down every data point even when it feels
repetitive, using tools such as Tomer Sharon's Rainbow Spreadsheets to
visualise trends by colour-coding participants and highlighting the cells
where they contributed a given data point
([[2016-11-04_ux-research_14-chapter-13-making-sense-of-the-mess]]).

### A four-step loop for qualitative test data

1. **Collect the relevant data points** — observations and quotes from session
   notes and recordings that bear on the research questions
   [[2025-05-02_analyze-usability-data]].
2. **Assess them for accuracy** — not all data points carry equal weight
   [[2025-05-02_analyze-usability-data]].
3. **Explain the data** through synthesis
   [[2025-05-02_analyze-usability-data]].
4. **Check the explanation for fit** against the whole dataset
   [[2025-05-02_analyze-usability-data]].

Steps 3 and 4 cycle. Initial explanations are usually built from the data points
that were easiest to recall, and testing them against the full set surfaces
inconsistencies and overlooked patterns [[2025-05-02_analyze-usability-data]].
Treating an explanation as a hypothesis — making a prediction, then rejecting or
refining it when the data does not support it — is what stops a single striking
observation from becoming a conclusion [[2025-05-02_analyze-usability-data]].
Complex questions about discoverability, comprehension or mental models require
triangulating data from different moments in the sessions with study-design,
recruitment and facilitation details [[2025-05-02_analyze-usability-data]].
Triangulation is also the standard defence against researcher bias: multiple
data sources, multiple analysis approaches, multiple researchers
[[2023-04-23_data-findings-insights-differences]].

### Thematic analysis and coding

Thematic analysis breaks down and organises rich qualitative data by tagging
observations and quotations with codes, so significant themes can be discovered
[[2022-08-17_thematic-analysis]]. A code is a shorthand label for a text
segment; codes need descriptions and examples, especially when several people
code, so segments about the same topic stay comparable
[[2022-08-17_thematic-analysis]]. **Descriptive** codes capture what the data is
about; **interpretive** codes add the researcher's analytical reading; both are
useful and can be assigned during or after grouping
[[2022-08-17_thematic-analysis]]. A theme emerges when related findings appear
repeatedly across participants or data sources
[[2022-08-17_thematic-analysis]].

The six steps: gather all the data, read everything end to end, code by asking
"what is this about?", create codes that encapsulate potential themes, take a
break for fresh perspective, then evaluate each theme for support and
saturation — returning to the board rather than forcing a conclusion when a
theme does not hold [[2022-08-17_thematic-analysis]]. Three practical routes
exist: analysis software such as Dovetail or Dedoose, manual journaling with
memos, and affinity diagramming [[2022-08-17_thematic-analysis]]. Involving the
team — workshops where members read transcripts and highlight important sections
— builds empathy and shared understanding, and having others evaluate themes
reduces personal bias [[2022-08-17_thematic-analysis]].

### Affinity diagramming

Affinity diagramming (affinity mapping, the KJ method) organises related
observations, ideas, concepts or findings into clusters
[[2023-03-19_affinity-diagramming-pitfalls]], [[2024-04-26_affinity-diagram]].
The three steps are: generate ideas independently on sticky notes (5-10
minutes, individually, to avoid bias from dominant participants), organise them
collaboratively into thematic clusters, then prioritise the clusters through
dot voting or discussion, documenting action items, next steps and a point
person [[2024-04-26_affinity-diagram]]. Do not force notes together; small
clusters can still hold value [[2024-04-26_affinity-diagram]]. The discussions
that happen while building the diagram matter more than the finished artefact
[[2024-04-26_affinity-diagram]].

Three pitfalls compromise the result [[2023-03-19_affinity-diagramming-pitfalls]]:

- **No focus question.** "What usability issues exist?" and "Where did users
  encounter issues?" sort the same data very differently; without a visible
  focus question the groupings are ambiguous and serve no strategic purpose.
  Large datasets can justify multiple rounds with different focus questions.
- **Keyword matching.** Clustering on shared words rather than shared meaning
  (Apple, Applesauce, Pineapple) produces useless categories. Enforcing a label
  rule — for instance, labels must be verbs describing the problem — forces
  meaningful categorisation.
- **Groupthink.** Dominant personalities (high-authority HIPPOs, eager
  enthusiasts, self-declared experts) make others conform, destroying the
  diversity of perspective that makes the method work. The early period of
  "organised chaos", where people sort with different strategies, produces
  better results than premature alignment behind one framework.

*UX Research* describes a specific three-colour execution of the same method:
write each data point on a sticky note in one colour, group notes together as
they are read aloud, add group titles in a second colour, and use a third
colour for section labels, reorganising as you go
([[2016-11-04_ux-research_14-chapter-13-making-sense-of-the-mess]]).

### Organising data from multiple viewpoints, and three more analysis grids

*UX Research* makes reorganising the same data from different points of view
(by frequency, by task, by demographic) a deliberate step: a single
organisation tells one story, and switching lenses surfaces richer
interpretations; where data points contradict each other, the contradiction is
read as a cue to find what distinguishes the participants involved, rather
than as noise to discard. Three further methods complement affinity
diagramming. SWOT analysis sorts sticky notes into a
strengths/weaknesses/opportunities/threats grid, useful for meetings with
business leaders shaping strategic roadmaps. Frequency mapping and word
clouds visualise how often something recurs, and suit quantitative data or
open survey questions rather than rich qualitative observation. Spectrum
analysis maps data points back to context — a customer journey, a persona, a
workflow — rather than grouping them in isolation, which can be done digitally
through annotated PDFs
([[2016-11-04_ux-research_14-chapter-13-making-sense-of-the-mess]]).

### Debriefing during research

*UX Research* treats debriefing as continuous communication that begins in the
field, not a formal presentation held once research concludes. It
distinguishes planned debriefs — scheduled five-minute stand-ups or
end-of-day discussions with stakeholders — from ad hoc debriefs held after a
particularly successful or problematic session. The stated reason to debrief
is that different observers, carrying different skill sets and biases,
interpret the same session through different lenses (the chapter's eyewitness
metaphor: no single perspective is perfect or right), so debriefing calibrates
the team onto shared findings and a common language. It also functions as a
real-time check on the research questions and hypotheses themselves: if
answers are already clear after four of ten scheduled participants,
debriefing can surface that and save time and money, and the chapter argues it
is better to realign a leading or too-narrow question than to keep gathering
less-than-ideal feedback. For distributed teams, regular email, phone or video
recaps keep the home office and clients aware of progress, and sharing raw,
unfiltered content early builds transparency and client relationships even
when it raises new questions. The chapter is explicit that its suggested
tracking tools — spreadsheets, affinity diagrams, digital collaboration
platforms such as Trello, Mural.ly or Google Drawing, and highlight reels —
are representative rather than prescriptive; the point is to track data early
and often so the team is not overwhelmed by thousands of data points later
([[2016-11-04_ux-research_13-chapter-12-debrief-sessions]]).

### Capture built for analysis

Analysis quality is decided partly at capture time. In group research, each
observer should take separate notes and combine them afterwards; seeing others'
notes during a session invites groupthink and diffuses responsibility
[[2017-04-30_group-notetaking]]. Two capture formats trade off against each
other: **chronological logs** when sequence matters, observers are remote,
time-on-task is measured or detailed technical observation is needed;
**topical notes** — one incident per sticky note, colour-coded by participant —
when the goal is fast post-session sorting into emergent categories, which feeds
affinity diagramming directly [[2017-04-30_group-notetaking]]. A short
whiteboard top-findings debrief after each session keeps findings visible, lets
stakeholders catch up, and allows recurring issues to be tallied quickly, which
suits fast-paced Agile environments [[2017-04-30_group-notetaking]]. Four to ten
observers is practical, rotated so everyone sees at least two sessions, which
also prevents judgements formed from a single observation
[[2017-04-30_group-notetaking]].

For surveys, analysability is a design constraint: test the survey on paper
first and then in the platform, checking the output format for analysability;
randomise question and answer order so that partial completions and
first-position bias do not skew the data; use conditional logic so respondents
never face unanswerable questions that would bias results; and keep the survey
short, since every extra question lowers the response rate and the validity
[[2016-09-25_qualitative-surveys]]. When reporting, be explicit that qualitative
survey metrics represent the opinions of the respondents rather than the whole
target audience, and code the open responses to find trends, using visualisation
to make them actionable [[2016-09-25_qualitative-surveys]].

For diary studies, revisit the original research questions, evaluate how
behaviour evolved over time, look at the customer journey holistically, and
synthesise themes into actionable insights; sample size is driven by saturation,
the point at which the data becomes repetitive, typically 5-50 participants
depending on scope and variance in the user group [[2024-03-29_diary-studies]].

### Analysing behavioural and analytics data

Pathways data in analytics, visualised as Sankey diagrams, shows aggregated
trends rather than individual journeys: two users on an identical path may have
had wildly different experiences, and one abandonment may be satisfaction while
another is frustration [[2022-10-16_analytics-pathways]]. To extract something
actionable, filter the data into meaningful chunks (a single node, a segment
such as mobile versus desktop, one key goal); review entry pages and second-step
patterns for anomalies; examine hub pages where users repeatedly return, which
may signal either engagement or frustration; start from the desired outcome and
work backwards through the pathways; and compare the links present on a page
against the paths actually taken [[2022-10-16_analytics-pathways]]. Analytics
cannot supply intent, so it must be supplemented with qualitative research
[[2022-10-16_analytics-pathways]].

Raw counts need transformation before they mean anything. Time-based
normalisation, cohort analysis (comparing users who joined the same week) and
ratio-based comparisons turn aggregates into actionable indicators; the analysis
methodology is what determines insight quality
[[2019-10-13_vanity-metrics]]. The choice of time frame matters too: too short
produces random noise, too long delays discovery of problems
[[2019-10-13_vanity-metrics]].

### Statistical significance is not practical significance

Statistical significance asks whether a result is unlikely to be random;
practical significance asks whether it is large enough to matter
[[2026-03-06_practical-significance]]. The two come apart in both directions:
with a massive dataset a 0.03% reduction can reach statistical significance
without any user ever noticing, while a small study with no p-value can be
convincing when the pattern is large and consistent — 10 of 12 participants
failing a task versus 1 of 12 [[2026-03-06_practical-significance]]. Three
lenses for judging practical significance: would users notice; does it support
business outcomes; what does the effect size say
[[2026-03-06_practical-significance]]. Context and scale carry the answer — a
$2 gain per conversion is $150,000 a year at two million conversions
[[2026-03-06_practical-significance]]. Many impactful insights come from
qualitative work that needs no statistical test to be compelling
[[2026-03-06_practical-significance]].

### Choosing what data to collect in the first place

Method selection determines what analysis is possible. A three-dimensional
framework organises the options: attitudinal versus behavioural (what people say
versus what they do), qualitative versus quantitative (direct observation versus
measurement), and context of use — natural (external validity), scripted
(focuses insight on a specific area), limited (isolates one aspect) or
decontextualised (examines issues beyond usage)
[[2022-07-17_which-ux-research-methods]]. Qualitative answers why and how to
fix; quantitative answers how much and at what scale
[[2022-07-17_which-ux-research-methods]]. Behavioural methods usually give more
reliable insight about actual use than attitudinal ones, and nearly every
project benefits from combining methods
[[2022-07-17_which-ux-research-methods]].

Journey-mapping research applies the same logic: audit existing organisational
data first (past focus groups, support call logs, analytics, satisfaction
scores), then combine interviews, field studies, diary studies and competitive
analysis, since what people say they do is not always what they do, and add
quantitative data (surveys, analytics, satisfaction metrics, social sentiment)
to establish frequency and magnitude [[2019-02-10_research-journey-mapping]].
Bringing users into the workshop to help interpret findings, and building
multipronged studies that view the journey from several perspectives, is part of
the analysis rather than of the collection
[[2019-02-10_research-journey-mapping]]. Open-ended qualitative surveys serve
the same preparatory role for quantitative ones: they reveal the answer
categories to offer later, instead of designing closed questions from
conference-room assumptions [[2016-09-25_qualitative-surveys]].

### Where AI helps and where it does not

AI can accelerate the early mechanical steps: transcription, summarisation,
preliminary coding, initial clustering of qualitative data, and quantitative
analysis [[2024-09-27_research-with-ai]]. It cannot observe behaviour — it
analyses transcripts and what users say, not what they do — and it is
stochastic, so it may attend to the wrong aspects of the data
[[2024-09-27_research-with-ai]]. The guidance is to treat it like an intern
needing instructions, context, constraints and correction, and never to hand it
the whole analysis; its output is a starting point that a human expert reviews
and refines [[2024-09-27_research-with-ai]]. One source states plainly that AI
cannot yet reliably analyse usability test data because it misses the
recordings, the context and the study-design factors
[[2025-04-11_usability-data-in-analysis]]. Contextual understanding, cultural
awareness and connecting dots across data are described as human capabilities
[[2024-09-27_research-with-ai]] — assessing reliability, asking the sharp
questions and identifying which insights matter for a decision is the judgement
that keeps designers strategic rather than tactical as AI surfaces patterns at
scale [[2025-06-06_future-proof-designer]].

### Analysis quality does not guarantee use

Rigorous synthesis is necessary but not sufficient. Personas are the worked
example: a persona set can be well analysed and still fail, because it was
created in isolation and imposed on the team, because leadership never bought
in, because nobody was taught how to apply it, or because its scope (broad
marketing versus granular UX) did not match its use
[[2018-01-28_why-personas-fail]]. Involving stakeholders in the sessions, the
daily recaps and the synthesis itself is what builds investment in the validity
of the output and the desire to use it [[2018-01-28_why-personas-fail]]. The
same argument runs through the collaborative analysis methods: group observation
and shared sorting create alignment, ownership and faster decisions than
researcher-only analysis [[2017-04-30_group-notetaking]],
[[2024-04-26_affinity-diagram]].

## Sources (19)

- [[2016-09-25_qualitative-surveys]] — Shows how survey length, clarity, and user guidance directly impact response rates and data validity, and how to design for maximum thoughtful participation.
- [[2017-04-30_group-notetaking]] — Explains how individual capture followed by group sorting supports affinity diagramming and rapid consensus-building on actionable findings.
- [[2018-01-28_why-personas-fail]] — The process of analyzing research data and creating actionable representations (like personas); quality synthesis requires rigor, but quality alone does not ensure personas will be used.
- [[2019-02-10_research-journey-mapping]] — Process of bringing users into the workshop to interpret findings and creating multipronged research studies to view the journey from multiple perspectives.
- [[2019-10-13_vanity-metrics]] — Time-based normalization, cohort analysis, and ratio-based comparisons transform raw data into actionable insights; analysis methodology determines insight quality.
- [[2022-07-17_which-ux-research-methods]] — Different collection contexts (natural, scripted, limited, decontextualized) and data types (behavioral vs. attitudinal, qualitative vs. quantitative) serve different research objectives.
- [[2022-08-17_thematic-analysis]] — Thematic analysis transforms raw observations into organized themes by grouping coded segments and identifying relationships, similarities, differences, and causal patterns.
- [[2022-10-16_analytics-pathways]] — effective pathways analysis requires filtering to key pages and user segments, investigating anomalies, and comparing related links to actual traffic patterns.
- [[2023-03-19_affinity-diagramming-pitfalls]] — synthesizing qualitative research data requires facilitation skills to maintain focus on research questions and prevent superficial keyword-based groupings or groupthink.
- [[2023-04-23_data-findings-insights-differences]] — The process of examining collected observations and measurements to identify patterns, requiring different techniques for qualitative versus quantitative data.
- [[2024-03-29_diary-studies]] — discusses analysis approaches for large qualitative datasets collected over time.
- [[2024-04-26_affinity-diagram]] — presents affinity diagramming as a method for synthesizing and organizing large amounts of research data.
- [[2024-09-27_research-with-ai]] — approaches to extracting insights from qualitative and quantitative research data, including transcription, coding, thematic analysis, and interpretation.
- [[2025-04-11_usability-data-in-analysis]] — introduces a six-dimensional framework for evaluating data point reliability independent of sample size, applicable to both qualitative and quantitative research.
- [[2025-05-02_analyze-usability-data]] — describes breaking down complex data into manageable units for assessment and inspection.
- [[2025-06-06_future-proof-designer]] — the human capacity to assess data reliability, ask critical questions, identify meaningful patterns, and connect insights to decisions.
- [[2026-03-06_practical-significance]] — Emphasizes that interpreting research requires judgment about context, scale, and whether the effect sizes matter in practice.
- [[2016-11-04_ux-research_13-chapter-12-debrief-sessions]] — the chapter outlines methods for tracking highlights in real time using spreadsheets, affinity diagrams, digital collaboration tools, and highlight reels, enabling teams to start analysis early and avoid being overwhelmed by data later.
- [[2016-11-04_ux-research_14-chapter-13-making-sense-of-the-mess]] — the chapter frames analysis as the process of converting raw research observations into organized data points, coding and cataloging them, organizing them from multiple perspectives, and identifying trends and opportunities. This is the foundation for insights that inform design and strategy.
