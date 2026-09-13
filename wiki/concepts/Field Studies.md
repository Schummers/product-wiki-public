---
type: concept
name: Field Studies
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Contextual Inquiry"
  - "Ethnographic Research"
  - "Observation Methods"
---

# Field Studies

## Definition

A field study is context research carried out in the user's natural environment
— in situ — rather than in a lab or an orchestrated setting
[[2024-01-12_field-studies]]. It belongs to the family of context methods, which
also includes diary studies and contextual inquiry, and whose common purpose is
to learn about users' environments, workflows, tools, pain points and habits by
observing behaviour instead of asking about hypothetical scenarios (usability
tests) or self-reported past behaviour (interviews)
[[2021-12-05_context-methods-field-diary-studies]]. The justification is
ecological validity: an accurate picture of how users behave in their real lives
[[2021-12-05_context-methods-field-diary-studies]].

What field work buys is what other methods structurally cannot see: real data,
physical and organisational constraints, interruptions, the workarounds people
have built around system limits, and the low-level habits that have become
invisible to the people performing them and so never surface in an interview
[[2018-07-08_field-studies-intranet-redesign]], [[2020-12-06_contextual-inquiry]].
It also corrects the team's theory of the problem, which is a large part of its
value — solving the wrong problem well still leaves you with the wrong thing
[[2018-07-08_field-studies-intranet-redesign]].

## Practice

### Variants and when each applies

- [[2024-01-12_field-studies]] distinguishes four types by how much the
  researcher intervenes: direct observation (fly on the wall), contextual
  inquiry (observation plus interview), customer-site visits (a guided tour or
  walk), and ethnography (complete immersion to understand the cultural and
  social context around product use).
- [[2021-12-05_context-methods-field-diary-studies]] draws the same line
  between field studies, which observe without interrupting, and contextual
  inquiry, which adds clarifying questions to augment and validate the
  researcher's understanding. Choose by research question: diary studies to
  understand experience over time, field studies or contextual inquiry to see
  tasks completed in the real environment with real tools, people and
  constraints.
- Field studies are most valuable in discovery, before design begins, but can
  also evaluate prototypes in their intended context (field testing)
  [[2024-01-12_field-studies]].
- Contextual inquiry is not worth it for simple interfaces such as an ecommerce
  page or a newsletter signup; plain direct observation suits those
  [[2020-12-06_contextual-inquiry]].
- Remote moderated research and lab research are the fallbacks when travel is
  expensive, participants are dispersed, or the scenario cannot be observed
  ethically [[2024-01-12_field-studies]].

### Running a contextual inquiry

- The governing metaphor is apprenticeship: the researcher is the apprentice
  learning the craftsman's task by watching and asking
  [[2020-12-06_contextual-inquiry]].
- Four grounding principles: Context (the natural environment), Partnership
  (user and researcher collaborate), Interpretation (a shared understanding of
  the work), Focus (the researcher knows the project's purpose)
  [[2020-12-06_contextual-inquiry]].
- Four-part session: Primer (rapport, explain goals), Transition (shift into
  observation mode), Contextual Interview (watch and discuss), Wrapup (clarify
  and summarise the understanding reached) [[2020-12-06_contextual-inquiry]].
- Six risks to guard against: the participant defaulting to interview mode, the
  session turning into a complaint session, researcher bias, user bias, missing
  important detail, and arriving with preconceived notions
  [[2020-12-06_contextual-inquiry]].

### Structuring what you observe

- Rich field data becomes overwhelming without structure. The context CUEs
  framework sorts observations into Culture (shared behaviours, beliefs, rules),
  the Unspoken (tacit knowledge and assumptions) and Environment (material,
  social and online surroundings)
  [[2022-09-11_context-cues-framework-field-studies]].
- Concretely: for Culture, what people do and how, when they turn to others, why,
  and how they explain it; for the Unspoken, group conflicts and their
  resolution, language norms, the questions newcomers ask, the effect of someone
  leaving, and access to needed information; for Environment, where the activity
  happens, how the space looks and feels, whether it is the only place the
  activity occurs, and how accessible it is
  [[2022-09-11_context-cues-framework-field-studies]].
- The framework rests on distributed cognition: thinking is not confined to one
  person's head but happens across people and material artifacts, so the design
  implication is to scaffold external thinking and reduce cognitive load
  [[2022-09-11_context-cues-framework-field-studies]].
- Cues translate into opportunities. People always consulting an address book to
  enter information suggests an online directory; exchanging business cards
  suggests a QR-code connection tool of the kind LinkedIn uses
  [[2022-09-11_context-cues-framework-field-studies]].

### Common failure modes in sessions

- [[2022-10-09_why-field-study-sessions-go-wrong]] lists five: sessions too
  long, sessions drifting into complaints, individual sessions turning into
  group observations, skewed host-guest relationship dynamics, and reliance on
  abstract description rather than observed behaviour.
- State the purpose upfront — understanding tasks and practices, not cataloguing
  every problem — then acknowledge complaints and steer back to habitual
  behaviour [[2022-10-09_why-field-study-sessions-go-wrong]].
- Keep it one-on-one; group sessions lack the depth needed to understand daily
  work [[2022-10-09_why-field-study-sessions-go-wrong]].
- In homes, accept small hospitality offers to reduce the participant's social
  stress but redirect to the task, and stay alert to hospitality altering
  behaviour [[2022-10-09_why-field-study-sessions-go-wrong]].
- Probe for concrete instances. Catch "in general…" and "we usually…" and ask
  "How did you do this today?" or "Tell me about this morning" instead
  [[2022-10-09_why-field-study-sessions-go-wrong]].
- Natural behaviour emerges as participants acclimatise to the researcher's
  presence [[2022-10-09_why-field-study-sessions-go-wrong]].

### Session length: the sources differ

- [[2021-12-05_context-methods-field-diary-studies]] describes typical field
  observation as lasting one to two hours.
- [[2022-10-09_why-field-study-sessions-go-wrong]] recommends not exceeding two
  hours, remote sessions especially, because of attention fatigue, and argues
  the quality of observation matters more than the number of tasks covered.
- [[2022-11-13_remote-contextual-inquiry]] instead sets two to three hours for
  remote sessions, split into observation and discussion, with multiple sessions
  when a workflow does not fit. Both remote-focused sources agree that virtual
  attention is the binding constraint and that several shorter sessions beat one
  long one, but they draw the ceiling in different places.

### Remote contextual inquiry

- It works: with the user still in their typical context, remote observation via
  video call and screen share preserves the core in-situ benefits — natural
  distractions, workarounds, interruptions — while removing access, travel-cost
  and safety barriers [[2022-11-13_remote-contextual-inquiry]].
- The fit is computer-based, desk-bound knowledge work visible on a single
  shareable display with little physical movement
  [[2022-11-13_remote-contextual-inquiry]].
- Setup discipline: communicate screen-sharing needs, firewall restrictions and
  recording permissions upfront, and rehearse the technical setup in a
  ten-minute call beforehand [[2022-11-13_remote-contextual-inquiry]].
- Say explicitly that you want to see the typical environment, or well-meaning
  participants will move somewhere tidier and quieter to be helpful
  [[2022-11-13_remote-contextual-inquiry]].
- Turning the researcher's camera off during observation helps the participant
  reach flow instead of watching for facial feedback
  [[2022-11-13_remote-contextual-inquiry]].
- Record for later analysis, use active inquiry to probe in real time since
  recall is harder remotely, watch for environmental cues and off-screen
  attention, encourage thinking aloud without forcing it, improvise guided tasks
  if flow does not come, and invite follow-up sessions for longer workflows
  [[2022-11-13_remote-contextual-inquiry]].

### Why teams commission field work

- Lab studies isolate participants in artificial settings that cannot always be
  made realistic; field studies build a more accurate representation of how work
  actually happens [[2018-07-08_field-studies-intranet-redesign]].
- They show the real journey — which information sources employees rely on, how
  they move between channels, where they struggle and why — and how workflow
  problems ripple across roles beyond the primary user group
  [[2018-07-08_field-studies-intranet-redesign]].
- They build empathy, moving teams from blaming users to blaming system design
  [[2018-07-08_field-studies-intranet-redesign]].
- They surface the discrepancy between what users believe they do and what they
  actually do, plus edge cases
  [[2021-12-05_context-methods-field-diary-studies]], and problems that appear
  when new tools are introduced into existing work practices
  [[2024-01-12_field-studies]].

### Planning

- Plan research questions, participants, setting, timing, method and
  permissions; side-by-side chatter can bias results, extra observers must be
  managed, and facility permissions are required
  [[2024-01-12_field-studies]].

## Sources (8)

- [[2018-07-08_field-studies-intranet-redesign]] — This article explains field study methodology for intranet research, describing how observational research in actual work environments reveals realistic context and workflow patterns that other methods miss.
- [[2020-12-06_contextual-inquiry]] — conducting research in users' natural environments where they perform actual tasks, revealing details and behaviors that interviews and labs cannot capture.
- [[2021-12-05_context-methods-field-diary-studies]] — Field studies and contextual inquiry are ethnographic methods involving direct observation in the user's natural environment, capturing real tools, interruptions, and interpersonal dynamics while emphasizing understanding of culture and context.
- [[2022-09-11_context-cues-framework-field-studies]] — A research method combining observation and interview in natural environments, revealing how users actually work; the context CUEs framework provides structure for consistent observation across complex settings, organizing observations into three categories that capture culture, unspoken norms, environmental cues, and relevant context while preventing data from becoming overwhelming.
- [[2022-10-09_why-field-study-sessions-go-wrong]] — conducted in natural environments, field studies reveal distractions, workarounds, and interruptions that lab settings cannot; effectiveness depends on proper session length, one-on-one observation, and managing relationship dynamics.
- [[2022-11-13_remote-contextual-inquiry]] — Remote contextual inquiry maintains the core benefits of in-situ research while overcoming access, cost, and safety barriers through screenshare observation of users in natural contexts; effective remote observation includes active inquiry, watching for environmental cues like facial expressions and off-screen attention, encouraging thinking aloud, and recording for deeper analysis.
- [[2024-01-12_field-studies]] — ethnography is one type of field study requiring complete immersion to understand cultural and social contexts affecting product use.
- [[2013-08-01_just-enough-research_06-chapter-5-user-research]] — the chapter describes contextual inquiry as conducting observations and interviews in the participant's actual environment, where habits and work-arounds are visible and can inform design of scenarios and features.
