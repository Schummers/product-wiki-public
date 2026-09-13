---
type: concept
name: Design
created: 2026-07-31
updated: 2026-07-31
status: developed
---

# Design

## Definition

Across these sources, design is treated less as the production of screens than
as the deliberate shaping of what a product does for people who live
complicated lives. It covers the structure of an interaction (which flows exist,
which scenarios are anticipated), the framing of information (what a
notification says, what a citation looks like, what an automation groups
together), and the process by which evidence about users turns into decisions.
The recurring claim is that quality comes from what teams choose to account for:
the messy reality of actual usage rather than a "happy path" ([[2025-10-24_edge-cases]]),
the goal a person is pursuing rather than the device-level action available
([[2025-12-05_smart-homes-user-value]]), the human intent behind an output rather
than the technology producing it ([[2025-12-19_ai-ad]]).

Design is also described as an organisational activity, not a solitary one. Its
outcomes depend on whether research recommendations survive the trip to
implementation ([[2025-11-07_research-recommendation-breakage]]), whether
stakeholders have actually internalised the findings that should be driving the
work ([[2025-11-21_ux-research-workshops]]), and whether the team shares coherent
practices and tooling rather than each person improvising their own
([[2025-10-31_ai-research-ops]]). Even research instruments are objects to be
designed: the structure of a diary-entry template determines both the quality of
the data and the experience of the participant filling it in
([[2025-11-28_diary-study-entries]]).

## Practice

### Design for the messy reality, not the happy path

[[2025-10-24_edge-cases]] argues that scenarios usually filed as edge cases —
account lockouts, name changes, multiple or shared accounts, stolen phones, slow
connections, several people editing at once, harassment, bereavement — are common
enough that they happen to somebody every day, and should be treated as ordinary
design work. Concretely: build safety features (blocking, reporting, friction in
account creation) from the ground up rather than adding them after abuse occurs;
support account switching, shared accounts and data export without forcing users
to lose data when their circumstances change; plan for death with memorial modes,
legacy contacts, suppression of collaboration invites to inactive accounts, and
no automated emotional triggers such as photo retrospectives; design offline-first,
cache intelligently, and show clear sync status. The same source insists
accessibility is a constraint present from day one, not a feature added later,
noting that over one in four adults have disabilities.

### Design around goals, not around the mechanism

[[2025-12-05_smart-homes-user-value]] found that people think in experiences
("relax after work", "bedtime"), not in device-specific actions, and recommends
supporting scenes (preset multi-device configurations) and automations
(conditional workflows) so several devices can be driven together. Its second
recommendation concerns data: raw numbers do not change behaviour. Information
must arrive with context, comparison and a recommended action — an energy meter
showing kilowatt figures prompts nothing, while a device flagging a weight
deviation with a visual alert and an explanation prompted immediate action.
Schedules and suggestions should be flexible, realistic about comfort,
context-aware from actual usage, and easy to adjust without starting over. The
source also advises tailoring information complexity to the role of the device
and to the user's mental model.

Convenience, in the same study, is not only time saved: reducing cognitive load
matters as much, with automations and reminders acting as "scaffolding" for
people with ADHD or crowded lives, which moves such devices from nice-to-have to
essential.

### Designing AI-facing experiences

Three sources converge on the same posture: the honest presentation of what the
technology actually is.

- [[2025-12-12_explainable-ai]] holds that UX teams cannot repair the technical
  limits of models but can control how explanations are presented. Style
  citations prominently and place them adjacent to the claim they support; write
  disclaimers in clear, action-oriented language ("Please double-check
  responses") rather than vague fine print, place them near the input box, and
  set expectations during onboarding; avoid anthropomorphic first-person language
  ("I thought about your problem"), which inflates trust; be honest about limits
  instead of manufacturing an impression of certainty or transparency. The
  underlying warning is that citations are frequently hallucinated and that
  step-by-step reasoning is often an after-the-fact rationalisation rather than a
  faithful trace.
- [[2025-12-19_ai-ad]] draws principles from publicly rejected AI-generated
  campaigns: start from purpose and a real user problem rather than from the
  technology ("AI-powered" means nothing to users); use AI to assist internal
  process — early ideation, copy refinement, microcopy testing — rather than to
  replace human creative work; keep human intent, vision and storytelling in the
  foreground of the output; prioritise long-term trust over short-term virality;
  and stay sceptical while running low-risk experiments to build firsthand
  judgement. It notes audiences can tell when a narrative has been bent to
  accommodate the technology, and that the choice to use AI is read as a signal
  about a team's priorities.
- [[2025-10-31_ai-research-ops]] adds the team dimension: when everyone picks
  their own tools and methods, work cannot be shared, built upon or peer-reviewed,
  and expertise ends up trapped in individual prompt "grimoires". Shared processes
  and systems are needed so AI practice is coherent instead of individually
  improvised.

### Turning research into design decisions

[[2025-11-07_research-recommendation-breakage]] names the failure mode:
"breakage", where value leaks between the readout and the release. Design teams
reinterpret recommendations into familiar patterns, deprioritise high-value fixes
during crunch, or cherry-pick convenient findings, so problems that have evidence
behind them persist. Its remedy is to measure adoption explicitly rather than
delivering findings and hoping — tracking where in the chain (prioritisation,
design, development) the value is lost, and treating the chain from data →
findings → insights → recommendations → adoption as complete only when every link
holds.

[[2025-11-21_ux-research-workshops]] tackles the same gap upstream, through
workshop design. It distinguishes three types — research-alignment workshops
(gallery walks, affinity diagramming, assumption comparison) to build shared
understanding; empathy workshops (persona walkthroughs, journey mapping, empathy
mapping) to create emotional connection; research-application workshops
(opportunity mapping, ideation) to translate insight into design direction and
priorities. The choice depends on audience readiness: understanding activities
for groups new to the research, empathy activities for groups who know the
findings but have not internalised them, application activities for teams ready
to act, and most effective sessions blend the three. Structure matters —
timeboxed activities, clear prompts, facilitated discussion, visual outputs.

### Designing the research instrument itself

[[2025-11-28_diary-study-entries]] treats an entry template as a designed
artefact whose structure determines both data quality and participant experience.
Closed entries (rating scales, checkboxes) are cheap for participants and yield
quantitative tracking but do not surface the why; open-ended entries give depth
at a higher cost to both participant and analyst; multimedia captures visual
context but adds technical complexity. Combine types deliberately, pair
structured questions with short open follow-ups, and make high-effort questions
optional. Keep entries to 5–10 minutes — beyond 15, the risk of skipped questions
and dropout rises sharply. When participant effort, analysis effort and research
goals conflict, participant effort wins, because burdensome entries produce poor
insight regardless of how convenient the analysis would have been.

## Sources (8)

- [[2025-10-24_edge-cases]] — what this article contributes to this concept
- [[2025-10-31_ai-research-ops]] — what this article contributes to this concept
- [[2025-11-07_research-recommendation-breakage]] — what this article contributes to this concept
- [[2025-11-21_ux-research-workshops]] — describes workshop design methodologies and activities for presenting research findings.
- [[2025-11-28_diary-study-entries]] — what this article contributes to this concept
- [[2025-12-05_smart-homes-user-value]] — what this article contributes to this concept
- [[2025-12-12_explainable-ai]] — what this article contributes to this concept
- [[2025-12-19_ai-ad]] — what this article contributes to this concept
