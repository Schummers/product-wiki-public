---
type: concept
name: Persona
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Personas"
  - "User Segmentation"
---

# Persona

## Definition

A persona is a fictional yet realistic description of a typical or target user
of a product ([[2025-10-03_persona]], [[2022-10-09_personas-study-guide]]) — more
precisely, a fictional representation and generalisation of a cluster of target
users who share attitudes, goals, and behaviours in relation to the product
([[2018-01-28_why-personas-fail]]). Personas are built by clustering research
data and then adding the human detail — a name, a photo, a short biography — that
makes the cluster memorable ([[2025-10-03_persona]],
[[2022-05-15_personas-archetypes]]). They are snapshots in time of user
behaviours, goals, and needs ([[2016-02-14_revising-personas]]), an
empathy-inducing shorthand for users' context, motivations, needs, and approaches
to using a product ([[2020-06-21_persona-types]]).

Their function is to make users memorable and to give a team one shared
reference instead of many private mental models of "the user": the persona's name
becomes shorthand for the full set of attributes, desires, and behaviours a
decision has to account for ([[2025-10-03_persona]]). They promote empathy,
raise awareness of target users, help prioritise features, and inform design
decisions ([[2022-10-09_personas-study-guide]]). Their value depends far less on
the artefact's polish than on how rigorously they were made, how well they match
their intended scope, whether the organisation actually uses them, and whether
they are kept current ([[2018-01-28_why-personas-fail]],
[[2020-01-12_persona-scope]], [[2016-02-14_revising-personas]],
[[2023-01-08_personas-are-living-documents]]).

One source works from a narrower angle. In
[[2018-02-12_solving-design-exercises_10-step-2-define-the-audience-who]] the
persona step is an audience-definition step inside a design exercise: list the
high-level categories of people whose motivations for using the product differ
significantly, pick one of the two biggest as the primary audience so there is
enough scope to generate ideas about serving it, then characterise it. The
artefact's job there is to narrow the problem enough that solutions can be
proposed at all, rather than to carry research findings across an organisation.

## Practice

### Ground them in research, not in narrative

- Personas must reflect the what and the why of user needs, which means they have
  to be rooted in qualitative understanding; even statistical personas begin with
  qualitative research to inform the survey ([[2020-06-21_persona-types]]).
- Field studies, surveys, interviews, and longitudinal studies form the
  foundation; personas must be based on actual user data, not assumptions
  ([[2025-10-03_persona]]).
- Narrative bias is the specific risk: humans construct explanatory stories on
  the flimsiest foundations, and personas and user stories built from narrative
  assumptions rather than research reinforce stereotypes
  ([[2017-02-19_narrative-biases]]). Specific details override base rates, causal
  explanations feel more plausible than randomness, and knowing the bias exists
  does not neutralise it — the remedy is to derive memorable details from real
  research, preferably several data sources, and to state and challenge implicit
  assumptions explicitly.
- Sparse empathy maps expose where the team's understanding of users is thin,
  which is a signal to do more research before designing
  ([[2018-01-14_empathy-mapping]]).

### Segment by behaviour, and be wary of demographics

- Designing for "everyone" produces a less usable experience because it prevents
  a clear understanding of who users are and what they need; even mass-market
  products need personas representing distinct segments
  ([[2019-05-12_everyone-as-users]]).
- Group by actual behaviour patterns, frequency of use, goals, and domain
  knowledge rather than age or income. Frequency of use is a useful starting
  point: frequent users need efficient workflows, infrequent users need clear
  guidance and memory aids, and one interface cannot serve both equally without
  segmentation ([[2019-05-12_everyone-as-users]]).
- Personas rooted only in demographic or analytics data lack context about
  motivation and behaviour; even high-level behavioural data cannot answer the
  "why", which makes assumption-driven design inevitable
  ([[2020-06-21_persona-types]]). Personas and archetypes both cluster on
  behaviours and attitudes, not demographics or personality traits
  ([[2022-05-15_personas-archetypes]]).
- Demographics still have a legitimate research role, and this is where the
  sources sit at slightly different angles: demographic data lets you compare
  across groups and check whether findings generalise to the whole population
  ([[2022-11-27_demographics-in-ux]]). That article's guidance is about
  collection discipline — justify every variable, use broad response ranges,
  always offer "Prefer not to say", use inclusive gender language, rethink
  "Other", allow "select all that apply" for sensitive categories, and put
  non-screening demographics at the end of the survey.
- The book sits on the other side of that line.
  [[2018-02-12_solving-design-exercises_10-step-2-define-the-audience-who]] has
  you characterise the chosen audience along age, gender, location, occupation,
  and mobility patterns, on the grounds that these dimensions significantly
  influence product design, where [[2020-06-21_persona-types]] and
  [[2022-05-15_personas-archetypes]] hold that clustering happens on behaviours
  and attitudes and that demographic data cannot answer the "why". The same
  chapter does make a second cut on need rather than on demographics, dividing
  the primary audience into subgroups (Spotify listeners by age or by activity),
  and presents that second cut as what surfaces targeted feature opportunities.
- A worked segmentation: luxury shoppers split into professional stylists buying
  for clients, window shoppers who aspire but cannot yet afford, occasional
  splurgers treating purchases as investments, and big spenders who buy
  habitually — each with distinct behaviours, from logo preferences to
  relationships with a dedicated sales representative
  ([[2022-06-12_luxury-user-groups-journeys]]).

### Choose the scope before creating anything

- Ask first what the personas are for; only then can the scope be set
  ([[2020-01-12_persona-scope]]). The broader the scope, the shallower the
  supporting data, because shared motivations and behaviours are hard to find
  across a wide array of situations.
- Segments are determined by context and goal: the same person can be a different
  persona depending on the scenario or product, and different research questions
  yield different segments ([[2020-01-12_persona-scope]]).
- Personas do not cascade. One universal set applied across every organisational
  level is unrealistic, because the research questions differ at each level
  ([[2020-01-12_persona-scope]]). Using broad marketing personas for granular UX
  design work, or the reverse, is one of the standard causes of failure
  ([[2018-01-28_why-personas-fail]]).
- Practitioners have an educational responsibility here: explain the tradeoffs to
  stakeholders, deliver contextual information alongside the personas, and help
  teams identify tangible applications ([[2020-01-12_persona-scope]]).

### Defining the audience inside a design exercise

One source treats the audience step as a move inside a time-boxed design
exercise rather than as a research programme, and its guidance is
correspondingly procedural
([[2018-02-12_solving-design-exercises_10-step-2-define-the-audience-who]]).

- Start from the high-level audience categories whose motivations for using the
  product differ significantly — Spotify has listeners, artists, and business
  owners — and pick one of the two biggest, so there is enough scope to come up
  with ideas for serving it. The justification for the step matches the rest of
  this page: building without truly understanding the audience risks building
  something users do not want, which is a primary reason products fail.
- Characterise the chosen audience along age, gender, location, occupation, and
  mobility patterns, then divide it into subgroups with different needs, since
  that division is what reveals specific feature opportunities per segment.
- Distinguish the user from the customer. In a B2B2C solution the people using
  the product and the party buying it differ (patients versus clinics), and the
  distinction should be stated when presenting the work.

Three worked exercises in the same book make the cut mostly on lifecycle stage
and experience level, which converges with the frequency-of-use rule in
[[2019-05-12_everyone-as-users]]:

- **Self-publishing on Amazon** — two personas inside a 30-80 age range,
  first-time and recurring authors, separated by emotional state and
  information need: newcomers are anxious about an unfamiliar process and need
  guidance and reassurance, recurring authors want efficiency. One product
  serves both, with contextual help for the first and streamlined workflows for
  the second
  ([[2018-02-12_solving-design-exercises_19-3-2-a-self-publishing-platform-for-amazon]]).
- **A dashboard for freelancers** — segmented on three axes at once: profession
  (designers, developers, writers, photographers, videographers, marketers),
  work arrangement (full-time, part-time, retainer), and experience level. New
  freelancers need onboarding on business setup and first invoicing, existing
  ones need import tools for their prior data
  ([[2018-02-12_solving-design-exercises_20-3-3-a-dashboard-for-freelancers]]).
  That chapter also shows what to do with a segment the design does not fit:
  retainer contractors, a small minority with flat revenue, may not benefit from
  the dashboard at all and are set aside for specialised treatment later rather
  than accommodated.
- **Primary health care** — both sides of the encounter are segmented: patients
  by reason for visit and by risk profile, giving new, preventive, and
  chronic-condition archetypes that each warrant a different engagement
  approach, and GPs, whose time is named as the clinic's most expensive
  resource
  ([[2018-02-12_solving-design-exercises_21-3-4-improving-primary-health-care]]).
  Which appointments a patient is shown is driven by three signals: the GP's
  advice during a face-to-face visit, the conditions already recorded for that
  patient, and calculated risk factors, so each patient sees only what is
  relevant to them.

### Three ways to build them

([[2020-06-21_persona-types]], summarised also in
[[2022-10-09_personas-study-guide]])

- **Proto (lightweight) personas** — no new research, drawn from existing team
  knowledge. Fast, and useful for surfacing the team's implicit assumptions and
  creating shared direction, but they often misrepresent real users and can
  damage the team's confidence in personas if the assumptions turn out wrong.
- **Qualitative personas** — built from 5 to 30 interviews or usability tests.
  The sweet spot for most teams: modest time investment, real motivations, pain
  points and expectations, enough accuracy for design decisions. Their limit is
  that they cannot say what share of the user base each persona represents.
- **Statistical personas** — qualitative research plus a large-scale survey (100+
  respondents) and statistical clustering. They give population-level
  distributions and support recruitment for later studies, but need statistical
  expertise and often duplicate effort without producing substantially different
  results from qualitative personas.

Jeff Patton describes a proto-persona practice from product discovery workshops
that lands on the same side as the proto (lightweight) approach above. In
*User Story Mapping*, Patton advocates building simple personas collaboratively
with the whole team, on flipchart paper, grounded in what the team already
knows and has observed, rather than commissioning a detailed document —
he cautions that a detailed persona document risks becoming one that "no one
reads" [[2014-09-05_user-story-mapping_19-14-using-discovery-to-build-shared-understanding]].
For Patton the point of the exercise is to focus discussion and build empathy
during discovery, not to produce a polished artefact, which converges with this
page's later point that "having personas and believing in them provides 90% of
their value" ([[2018-01-28_why-personas-fail]]).

### Presentation: persona, archetype, empathy map

- Personas and archetypes visualise the same insights; the only difference is
  presentation. A persona gets a plausible name, bio, and photo, an archetype
  only an abstract label ([[2022-05-15_personas-archetypes]]). The human face
  invites empathy and is more memorable, since people latch onto characters and
  stories, but too many personas overwhelm a team. Archetypes are the usable
  fallback when there is organisational resistance to personas or when
  stakeholders have been burned by badly made ones.
- Include names and photos for memorability but leave out irrelevant details that
  obscure the information needed to make design decisions
  ([[2025-10-03_persona]]).
- Empathy maps (Says, Thinks, Does, Feels) capture a non-chronological snapshot
  of a user type; aggregating individual maps of users who behave similarly
  produces a map for a segment, which is a first step toward a persona — or an
  alternative representation, depending on the project
  ([[2018-01-14_empathy-mapping]]).
- Both personas and archetypes are inherently reductive: one face or label stands
  for many diverse people, and can exclude those not represented
  ([[2022-05-15_personas-archetypes]]).

### Design them to be updated

- Personas often fail simply by going out of date, and that failure mode is
  preventable at creation time ([[2023-01-08_personas-are-living-documents]]).
  They must stay stable enough to be internalised by the organisation yet
  flexible enough to follow real changes in the business or the user base.
- Overinvesting in visual design is tempting but risky: Photoshop files and
  printed posters signal finality and make updating feel like a major
  undertaking, whereas editable formats such as Google Slides invite iteration.
  Aim for the prettiest easily editable format the team can maintain, and match
  the format to the team's design resources
  ([[2023-01-08_personas-are-living-documents]]).
- Two signals that revision is due: shifts in business, product offering, or
  competitors' capabilities; and shifts in user demographics or behaviour, which
  analytics segmentation, usability testing, and support data can reveal
  ([[2016-02-14_revising-personas]]).
- Update frequency correlates with perceived impact: teams updating quarterly
  rated persona impact at 5.5 on a 1-7 scale, versus 4.5 for teams updating every
  one to four years and 3.9 for teams that rarely update
  ([[2016-02-14_revising-personas]]). Personas untouched for five or more years
  are likely performing "about as well as a dull butter knife cutting steak".
- Update in response to actual change, not on arbitrary cycles
  ([[2016-02-14_revising-personas]], [[2023-01-08_personas-are-living-documents]]).
  When you do update, explain what changed and why, make sure everyone has the
  current version, and discard old copies ([[2016-02-14_revising-personas]]).

### Getting the organisation to use them

- Five recurring failure modes: personas created but never used, no leadership
  buy-in, personas created in isolation and imposed on the team, failure to
  communicate how to apply them, and fundamental flaws such as misaligned scope
  ([[2018-01-28_why-personas-fail]]).
- A single bad first experience creates lasting sceptics, since people generalise
  freely from one observation; recovering requires understanding what went wrong
  ([[2018-01-28_why-personas-fail]]).
- Frame personas to executives as an alignment tool that settles disagreement
  about who "the user" is, rather than as pure research, to get past the "we
  already know our users" objection ([[2018-01-28_why-personas-fail]]).
- Create them collaboratively. Involving stakeholders in research sessions, daily
  recaps, and synthesis builds investment in their validity
  ([[2018-01-28_why-personas-fail]]); teams that took part in creation believe in
  the personas, use them, and promote them to others ([[2025-10-03_persona]]).
- Adoption needs continuous education and continuous reference: integrate
  personas into standups, design reviews, and planning, and keep a champion
  advocating for them ([[2018-01-28_why-personas-fail]]). "Having personas and
  believing in them provides 90% of their value."

### Putting them to work

- **Scenario mapping** — a scenario is a brief story about a persona completing
  one key task, with five elements: actor (the persona), motivator, intention,
  action, resolution ([[2021-03-28_scenario-mapping-personas]]). Grounding
  scenarios in a specific persona gives ideation the context that abstract
  requirements lack. Keep them high-level and free of UI specifics, include only
  a few high-priority needs, run the workshop with 4-6 crossfunctional
  participants, colour-code sticky notes by idea / question / consideration, and
  discuss collectively afterwards to set priorities.
- **Journey mapping** — 49% of surveyed practitioners use existing personas for
  their maps, 27% develop personas during the research, and 14% during the
  workshop itself ([[2023-01-08_journey-mapping-how]]).
- **Prioritisation and evaluation** — personas let teams assess features
  systematically against how they serve different user types and goals
  ([[2022-10-09_personas-study-guide]]); passive personas, created but unused,
  influence nothing.
- **Research and analytics** — use personas as screening criteria for usability
  study recruitment, to segment analytics data by user group, and as a guide for
  expert reviews ([[2025-10-03_persona]]). Recruit participants proportionally
  from each segment and watch how the groups behave differently with the same
  design ([[2019-05-12_everyone-as-users]]); an unfiltered study can end up with
  nine commuters and one tourist when both are target users.

### Complements, alternatives, and criticism

- **Jobs-to-be-Done** is presented as complementary rather than a replacement
  ([[2017-08-06_personas-jobs-be-done]]). JTBD captures the outcome a user wants,
  summarised in one sentence with its relevant context; personas capture
  behavioural and attitudinal richness — mental models, pain points, goals,
  emotional considerations — and help teams balance competing needs when one job
  has different requirements for different groups. JTBD does not build empathy
  the same way, because personas use narrative and personal detail to create
  emotional connection. Teams can fold JTBD data into personas, use both side by
  side, or pick one according to organisational context.
- **Antipersonas** represent groups who could misuse the product in ways that
  harm target users or the business ([[2022-09-11_antipersonas-what-how]]). They
  are warranted when a product handles sensitive data, poses physical or
  emotional threats, or when misuse would have severe consequences — weigh
  likelihood against severity. An antipersona carries a name and face for
  memorability plus goal, motivations, actions, tools, contextual needs, and
  consequences; four common threat types are thieves, creators of illegal
  content, spreaders of disinformation, and children. Validate through research
  with people similar to the antipersona or with experts such as security guards,
  lawyers, or social workers. The point is realistic risk assessment and
  safeguards that do not punish target users.
- **User-ecosystem thinking** is the most direct critique in the corpus
  ([[2025-08-29_user-ecosystem-thinking-anthropologic]]). It argues that personas
  and user journeys imagine users as isolated, intentional actors with a 1-to-1
  relationship to the product, and so miss how design decisions ripple through a
  system of interconnected people, relationships, and processes — a surgical tool
  affects nurses, technicians, and maintenance staff, not only the surgeon. It
  proposes user archetypes defined by role and relationship within a system, with
  context treated as foundational rather than supplementary. Note that this use of
  "archetype" is not the same as the one in
  [[2022-05-15_personas-archetypes]], where archetypes are simply personas
  without a name and face.

## Sources (27)

- [[2016-02-14_revising-personas]] — core methodology for user-centered design; the article addresses when and how to revise them.
- [[2017-02-19_narrative-biases]] — the article cautions that personas and user stories must derive from research, not narrative assumptions, to avoid reinforcing stereotypes.
- [[2017-08-06_personas-jobs-be-done]] — personas provide rich behavioral and attitudinal representations of users that help teams build empathy and balance design decisions across different user groups, complementing job-to-be-done analysis.
- [[2018-01-14_empathy-mapping]] — A fictional but research-based representation of a user type; empathy maps can be an intermediate step toward personas or an alternative representation depending on project needs.
- [[2018-01-28_why-personas-fail]] — A fictional but research-based representation of a user type; creates a shared, specific user archetype that teams reference in design decisions; effectiveness depends on creation quality and organizational adoption.
- [[2019-05-12_everyone-as-users]] — Even mass-market products need personas representing distinct user segments based on behavior and frequency of use (not demographics) to guide research and design decisions, since different user types have different expertise, motivation, and needs.
- [[2020-01-12_persona-scope]] — Details how persona scope impacts their utility, showing that personas must be tailored to specific contexts and purposes rather than treated as one-size-fits-all artifacts.
- [[2020-06-21_persona-types]] — Three research-grounded approaches to identifying patterns and grouping users into actionable personas based on shared attitudes, goals, and pain points, with different tradeoffs between speed, accuracy, and resource investment.
- [[2021-03-28_scenario-mapping-personas]] — the article emphasizes the importance of grounding scenarios in specific personas to provide rich context for ideation.
- [[2022-05-15_personas-archetypes]] — The article clarifies that personas are representations of user clusters based on research, differentiated from archetypes only by their human presentation with names and biographical details.
- [[2022-06-12_luxury-user-groups-journeys]] — Luxury shoppers segment into professional buyers, aspirational followers, occasional investors, and habitual collectors, each with distinct behaviors and needs.
- [[2022-09-11_antipersonas-what-how]] — While regular personas build empathy with target users, antipersonas identify threats from misuse; both types inform comprehensive design that serves target users safely.
- [[2022-10-09_personas-study-guide]] — realistic fictional user profiles that synthesize research data to promote team empathy and guide design decisions; effectiveness depends on rigorous creation, active use, and periodic updates.
- [[2022-11-27_demographics-in-ux]] — demographic data enables comparison across groups (age, location, income) to discover whether patterns differ by segment and whether findings generalize to whole populations.
- [[2023-01-08_journey-mapping-how]] — Most journey maps reference existing personas; some develop personas specifically for the mapping project while others identify personas during the mapping process itself.
- [[2023-01-08_personas-are-living-documents]] — Personas are most valuable when designed as living documents that evolve with user base and business changes; format and editability are critical to long-term organizational adoption.
- [[2025-08-29_user-ecosystem-thinking-anthropologic]] — The article critiques persona-based design and proposes user archetypes as a more systems-aware alternative.
- [[2025-10-03_persona]] — Documents the definition, creation (research phase followed by clustering and detail addition), and purpose of personas as memorable, research-based representations that foster empathy and guide decisions.
- [[2018-02-12_solving-design-exercises_10-step-2-define-the-audience-who]] — this chapter details how to define personas by identifying audience categories with different motivations, then characterizing them using demographic and contextual dimensions like age, gender, location, and occupation; the chapter demonstrates how to divide a primary audience into subgroups with distinct needs, enabling discovery of specific feature opportunities for each segment.
- [[2018-02-12_solving-design-exercises_19-3-2-a-self-publishing-platform-for-amazon]] — The chapter identifies two distinct personas (first-time vs. recurring authors) within the 30-80 age range, noting their different emotional states and information needs, and designs the product to serve both simultaneously with different levels of guidance.
- [[2018-02-12_solving-design-exercises_20-3-3-a-dashboard-for-freelancers]] — Dashinsky segments freelancers by profession (designers, developers, writers, photographers, videographers, marketers), work arrangement (full-time, part-time, retainer), and experience level (new vs. existing), recognizing that new freelancers need guidance while experienced ones need efficiency.
- [[2018-02-12_solving-design-exercises_21-3-4-improving-primary-health-care]] — The author segments both patients (by reason for visit and risk profile) and GPs, recognizing that time is the most expensive clinic resource and that different patient archetypes (new, preventive, chronic condition) benefit from different engagement approaches.
- [[2013-08-01_just-enough-research_09-chapter-8-analysis-and-models]] — comprehensively covers creation from research data, including name, demographics, quote, goals, behaviors, skills, environment, relationships, and scenarios; emphasizes that personas are tools for empathy and reference across teams, not marketing segments.
- [[2016-11-04_ux-research_14-chapter-13-making-sense-of-the-mess]] — the chapter mentions personas as one of the reference points, alongside customer journeys and workflows, that spectrum analysis maps data points back to, so that opportunities and challenges surface at the specific point in the process being studied.
- [[2016-11-04_ux-research_15-chapter-14-communicating-insights]] — personas are presented as a tool for making user behavior and qualities digestible for teams and stakeholders, helping them recall and discuss different user segments and their needs.
- [[2014-09-05_user-story-mapping_19-14-using-discovery-to-build-shared-understanding]] — Patton advocates lightweight persona creation done collaboratively with the team during discovery, grounded in what the team knows and has observed, to focus discussion and build empathy; he cautions against producing detailed documents that no one reads.
- [[2019-12-17_storytelling-in-design_07-chapter-6-using-character-development-in-product-design]] — Foundational throughout the chapter; emphasizes data-driven personas as characters rather than demographic stereotypes; cites Alan Cooper, inventor of design personas, on looking at personas as individual users and digging deep into what matters to them; advocates detailed, research-backed personas with backstory, beliefs, motivations, weaknesses, and relationships to ensure users become the heroes of experiences.
