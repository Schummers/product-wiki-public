---
type: concept
name: Design Process
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Agile Design Process"
  - "UX Design Process"
  - "UX Process"
  - "UX Workflow"
  - "Ux Design Process"
---

# Design Process

## Definition

The design process is the structured approach a team follows to move from an
imperfectly understood problem to a solution that has been built and shipped.
Across the sources it is described through a small number of overlapping
frameworks: the six phases of design thinking — empathize, define, ideate,
prototype, test, implement — grouped into understanding, exploring and
materializing ([[2016-07-31_design-thinking]]); the double diamond, whose first
half is the discovery phase where the problem space is researched and framed
([[2020-03-15_discovery-phase]]); and a four-phase research cycle of Discover,
Explore, Test and Listen used to decide which research method fits where
([[2017-02-12_ux-research-cheat-sheet]], [[2023-11-24_surveys-design-cycle]]).
None of these are presented as linear pipelines. Phases are repeated, teams
return to empathy and definition after a prototype teaches them something new,
and the framework is explicitly meant to be scaffolding rather than a recipe
([[2016-07-31_design-thinking]]).

What the sources treat as the substance of the process is less the sequence of
phases than a set of commitments: define the outcome before the output
([[2016-08-14_outcomes-vs-features]]), ground decisions in research rather than
assumption ([[2016-10-16_journey-mapping-ux-practitioners]]), iterate at low
fidelity before investing ([[2016-08-28_ux-success-agile]]), and actually
implement, since the implement phase is the most often forgotten and the most
important ([[2016-07-31_design-thinking]]). The process is also organisational:
UX maturity is assessed partly on process as one of four factors alongside
strategy, culture and outcomes ([[2025-08-29_informal-ux-maturity]]), and a
large share of the sources describe process work as the work of building
alignment, buy-in and shared vision across departments rather than of producing
artifacts. A recurring counterpoint is that process can be performed rather
than practised: experienced designers compress and internalise it until it looks
like intuition, which is not the same as abandoning it
([[2026-03-13_design-process-isnt-dead]]), while less experienced practitioners
can substitute template-following for the contextual thinking the process exists
to do ([[2025-05-30_template-trap]]). One source sharpens who does which part:
in real product development most steps of the process are worked with other team
members such as product managers and data analysts, and it is the UI/UX
execution step that is typically the designer's own responsibility and the core
skill expected at any level of seniority ([[2018-02-12_solving-design-exercises_08-the-framework]]).

## Practice

### Start with the problem, not the solution

- Define the outcome (the problem solved) before the output (the thing built);
  an excellent interface for the wrong features still fails
  ([[2016-08-14_outcomes-vs-features]]). The recommended sequence is: state the
  problem and who it is for, gather data proving the problem exists, define the
  core competencies that create advantage, set concrete success criteria, then
  test multiple ideas with users.
- Write user need statements during the define stage: a specific user, a
  research-grounded need, and an insight about the goal sought. Phrase needs as
  verbs (outcomes) rather than nouns (UI components) so the solution space is
  not prematurely constrained; the statement then acts as a north star for the
  project ([[2019-03-24_user-need-statements]]).
- Run a discovery phase when there are too many unknowns, when the team is not
  aligned on goals, or when the context shifts (new market, acquisition, policy
  change, chronic problem). Successful discovery yields understanding of users
  and needs, of problems and opportunities, an inventory of constraints, and a
  shared vision of success; its typical outputs are problem statements, maps,
  need statements, personas and early concepts
  ([[2020-03-15_discovery-phase]]).

### Research woven through the phases, not bolted on

- Choose methods by phase: Discover (field studies, interviews, diary studies,
  competitive analysis) to validate or discard assumptions; Explore (personas,
  journey mapping, card sorting, prototype feedback) to define the problem
  space; Test (qualitative usability testing, benchmarking, accessibility
  evaluation); Listen (surveys, analytics, search logs, FAQ review). If only one
  method is affordable, qualitative usability testing has the highest impact
  ([[2017-02-12_ux-research-cheat-sheet]]). The same four-phase frame governs
  survey selection — discovery and diary surveys, competitor and
  statistical-persona surveys, post-task/post-test instruments such as SEQ and
  SUS, then NPS/CSAT/CES and custom listening surveys
  ([[2023-11-24_surveys-design-cycle]]).
- Establish a regular testing cadence rather than testing late; testing too late
  leaves no time to act on findings ([[2017-10-08_ux-lessons]]).
- Never let assumptions stand in for evidence: journey maps built on
  preconceptions fail to gain traction (25% of failures)
  ([[2016-10-16_journey-mapping-ux-practitioners]]), and roadmaps built from
  feature wishlists rather than researched user problems are release plans in
  disguise ([[2020-07-05_ux-roadmaps]]).
- Distinguish empathy from sympathy. Empathic design needs qualitative methods
  with open-ended questions, diverse team composition, direct exposure of team
  members to users, and protocols that counter unconscious bias and false
  consensus ([[2019-04-21_sympathy-vs-empathy-ux]]).

### Ideation and exploration

- Ideate after research and before prototyping: 71% of teams rating their
  ideation very effective work in that window, against 48% of merely
  somewhat-effective teams. Effectiveness comes from structure, not duration —
  the most effective teams spend under three hours, use written techniques such
  as brainwriting to reduce groupthink and hierarchy bias, and prefer group to
  individual ideation; 95% of ineffective teams rely on unstructured discussion
  ([[2017-10-29_ideation-in-practice]]).
- Keep early artifacts cheap and disposable. Distinguish disposables (made to
  help you think, allowed to be wrong) from deliverables (made to communicate,
  deserving care); polish before testing an idea raises sunk-cost attachment and
  slows iteration. Ask, before making anything: is this for me or for someone
  else? ([[2026-05-22_design-disposables]])
- Wireframe early and roughly. Work from device aspect ratio, to navigation and
  search, to the largest elements, to details; thick pens, time limits and
  limited space prevent obsessing over aesthetics, and knowing the component
  conventions matters more than drawing skill
  ([[2021-06-20_draw-wireframe-even-if-you-cant-draw]]).
- Post-its remain useful in ideation, affinity diagramming and synthesis: equal
  size makes contributions visually equal, limited space forces concision, and
  physical arrangement forces a group to commit to a structure. They support a
  process, they are not the design, and they are poor for remote teams and
  colour-blind participants ([[2018-03-25_post-it-in-ux]]).
- Use mood boards in the define or ideate phases to align a team on visual and
  emotional direction before prototyping, reducing later revisions; keep all
  visuals under one coherent theme, and avoid filling the board with competitor
  screenshots, which turns it into a feature comparison
  ([[2023-02-26_mood-boards]]).

### Mapping and alignment artifacts

- Journey mapping recurs across the sources as the process activity that
  identifies gaps and opportunities and forces cross-functional alignment. The
  map has three zones — lens (persona, scenario), the mapped experience (phases,
  actions, thoughts, emotions), and insights (opportunities, ownership,
  metrics); practitioners routinely omit the third zone, which is the one that
  turns a narrative into an action plan
  ([[2016-07-31_customer-journey-mapping]],
  [[2016-10-16_journey-mapping-ux-practitioners]]).
- Scope tightly (one persona, one scenario), start with a small journey with
  known pain points your team has authority to fix, keep the first version
  low-fidelity, involve stakeholders early and often, and judge the map by the
  decisions it changes rather than by how it looks
  ([[2019-04-07_journey-mapping-faq]], [[2021-03-07_journey-mapping-tips]]).
- Two decisions come before any mapping work: current-state (to surface pain
  points and build a persuasive case) versus future-state (to set a North Star),
  and assumption-first versus research-first
  ([[2020-06-14_journey-mapping-approaches]]).
- A worked workshop sequence: build a crossfunctional team, pick actor and
  scenario, consolidate existing research, set homework; then map current-state
  assumptions, bring customers in to react to and correct the map, generate need
  statements from pain points and dot-vote them, brainstorm future-state ideas
  with customers, and have the internal team sketch flows in timed design-studio
  rounds; then capture artifacts and prototype
  ([[2020-07-05_journey-mapping-workshop]]).
- Distributed teams face the same failure modes amplified — weaker buy-in,
  scepticism about outcomes, harder iteration on static documents. Tools help at
  three levels: visualization only, real-time collaboration, and data
  integration; team size and data needs determine the level
  ([[2017-02-05_remote-customer-journey-mapping]]).
- Service blueprints extend a journey into frontstage, backstage, support
  processes and evidence. Derive customer actions from qualitative research or
  an existing journey map, document how employees actually work rather than how
  they are supposed to, keep redundant steps because they expose inefficiency,
  and use dot voting and colour-coding to mark pain points and opportunities. A
  spreadsheet is the recommended first draft, polished later for presentation
  ([[2020-07-19_service-blueprinting-template]]).
- Empathy maps are usable at three different moments, not only as a
  post-research deliverable: before research to expose knowledge gaps and shape
  research questions, during research to capture observations, and after to
  communicate and build buy-in. Their four-quadrant format is simple enough for
  non-researchers to contribute ([[2023-02-12_using-empathy-maps]]).
- Personas fail on execution and adoption rather than on concept: created and
  never used, unfunded for lack of leadership buy-in, imposed without
  involvement, unusable because no one was taught how to apply them, or scoped
  wrongly (marketing personas used for granular UX work). They only hold value
  if referenced continuously in standups, design reviews and planning
  ([[2018-01-28_why-personas-fail]]).
- A UX roadmap communicates vision, not implementation: themes organised by Now,
  Next and Future horizons, each naming a beneficiary and need, a business
  outcome, and ownership and work type. It is not a release plan, Kanban board,
  backlog or journey map ([[2020-07-05_ux-roadmaps]]).

### Prototyping, evaluation and iteration

- A modelled lean cycle: qualitative survey to understand audience expectations,
  outcome-focused design goals, low-fidelity wireframes, then high-fidelity
  prototypes, three rounds of testing on desktop and mobile, a content hierarchy
  that drives layout and specification, and a modular component stylesheet for
  handoff. Iterative testing does not require a large budget; planning multiple
  rounds with discount methods produces steady improvement without unreasonable
  delay ([[2018-08-26_case-study-iterative-design-prototyping]]).
- The same user-centred cycle transfers to non-interactive artifacts: define
  goals up front, explore in low fidelity with real content, iterate visual
  hierarchy in high fidelity (squint test), test with target users, and prototype
  physically when the artifact is physical
  ([[2021-03-21_visual-design-heuristics-posters]]).
- Expert reviews can run at any stage where a prototype exists, but belong
  iteratively during the creative phase and before major redesigns, while
  changes are still cheap. The reviewer should be external to the team, and each
  issue needs a severity rating and an explanation grounded in usability
  principles or research rather than opinion
  ([[2018-02-25_ux-expert-reviews]]).
- Design critiques are a distinct, frequent, crossdisciplinary stage — not an
  approval gate. They need a facilitator, an agreed scope, agreed design
  objectives, and conversation rather than command-and-control feedback;
  round-robin or quota methods balance contributions. Common failure modes:
  no agreement on personas or objectives beforehand, over-long sessions, rushing
  to solve during the session, and focusing only on negatives
  ([[2016-10-23_design-critiques]]).
- Accept incremental improvement over perfection: there is no perfect interface,
  and recommendations must balance user needs against business viability
  ([[2017-10-08_ux-lessons]]).

### Prioritisation, risk and quality debt

- Prioritisation matrices plot items on two weighted criteria. Vote with colours
  representing areas of expertise (developers on feasibility, designers on user
  impact), vote privately or digitally where groupthink or the HIPPO effect is a
  risk, then discuss and renegotiate placement to reach consensus; split more
  than two criteria into paired matrices ([[2018-05-27_prioritization-matrices]]).
- Treat risk as likelihood times impact across six steps: set objectives,
  identify hazards from behavioural research, analytics, support tickets and
  competitive analysis, plot them on a severity/probability matrix, develop
  controls, weigh mitigation cost against benefit, and monitor continuously
  since risk profiles shift as the design evolves
  ([[2023-05-28_design-risk-management]]).
- UX debt accumulates from expedient launches, skipped testing and poor
  communication, and its cost compounds — users abandon and do not return.
  Surface it through monthly usability testing, support reports, surveys and
  retrospectives; prioritise it on a user-value/effort matrix; and allocate
  recurring story points or quarterly cleanup sprints so it is reduced rather
  than deferred indefinitely ([[2018-11-11_ux-debt]]).
- Postmortems close the loop at project level, distinct from sprint retros:
  examine successes as well as failures, time them once outcome data exists but
  while memory is fresh, use five-whys to reach systemic causes, require
  concrete process changes, assign an owner and deadline to each action, and
  frame everything around system failure rather than personal blame
  ([[2026-02-27_ux-postmortems]]).

### Workshops and facilitation as process infrastructure

- Five workshop types map onto the lifecycle: discovery (consensus on current
  state and milestones), empathy (shift the team from features-first to
  users-first), design (rapid generation of solution ideas through sketching),
  prioritisation (consensus on what matters, countering scope creep), and
  critique (evaluate designs against user needs and principles). Workshops
  differ from meetings by solving problems actively; they cost more preparation
  and buy more shared ownership ([[2019-12-08_5-ux-workshops]]).
- Use a parking lot to capture off-topic questions and assumptions without
  derailing the session — these often become the next research questions.
  Introduce it and its ground rules up front, cluster items by affinity as they
  arrive, assign who does what by when, and document everything in the written
  follow-up; an unmanaged parking lot becomes a graveyard and insults the people
  who contributed ([[2019-09-08_parking-lots]]).
- Collaborative creation is repeatedly cited as the mechanism that makes process
  outputs stick: 37% of journey-mapping success factors involve creating maps as
  a team and sharing broadly ([[2016-10-16_journey-mapping-ux-practitioners]]),
  personas need stakeholder participation in research and synthesis
  ([[2018-01-28_why-personas-fail]]), and empathy maps and mood boards are
  valued partly because non-specialists can contribute
  ([[2023-02-12_using-empathy-maps]], [[2023-02-26_mood-boards]]).

### Fitting the process to an Agile and organisational reality

- Ten practices from 125 Agile practitioners: invest in release planning and
  discovery before sprints; run design one to two sprints ahead of development;
  build a collaborative, trust-based culture using design-thinking techniques;
  treat design as iterative with low-fidelity prototypes rather than perfect;
  keep UX visible in daily standups; make user research a team event so
  decisions follow data rather than opinion; and treat the methodology itself as
  iterative ([[2016-08-28_ux-success-agile]]).
- Change happens incrementally. Depending on organisational maturity, systemic
  change takes years; demonstrate value with small visible wins, let teams
  experience new approaches firsthand, and move from reactive request-taking to
  shaping product vision ([[2017-10-08_ux-lessons]]).
- Use the UX-maturity model's four factors — strategy, culture, process,
  outcomes — as a reflective lens even without a formal assessment. Ask "what
  signals are we seeing?" rather than "what stage are we?", track quarterly with
  lightweight methods, watch for regression, stagnation and performative
  practice, and avoid reassessing so often that it produces superficial fixes
  ([[2025-08-29_informal-ux-maturity]]).
- Build an information pipeline to gain autonomy over product direction: gather
  from analytics, support tickets, past research, roadmaps and communication
  archives; build relationships with domain experts and map upstream/downstream
  dependencies; create crossfunctional spaces; and synthesise into credible
  recommendations, showing tradeoff tables rather than telling. Central tracking
  of projects, owners, files, status and notes preserves rationale and avoids
  duplicate work ([[2026-04-17_information-pipeline]]).
- Journey mapping specifically is resource-intensive: a survey of 343
  practitioners found a mean of 73.8 hours across buy-in, internal data, external
  research, synthesis and artifact creation, with external research (20.6h) and
  synthesis (16.4h) dominating; in-house teams and large organisations invest
  more ([[2022-12-18_journey-map-how-much-time]]).

### How much process, and how rigidly

- Frameworks are scaffolding, not recipes; adapt them to team, expertise and
  problem ([[2016-07-31_design-thinking]]). [[2018-02-12_solving-design-exercises_08-the-framework]]
  says the same of its own seven-step framework for working a design exercise:
  do not follow it blindly, since no framework fits every task, and use
  judgement about when to apply it. It also reports the compression effect from
  the inside — the framework feels like a lot of work at first, but with
  practice most steps take a couple of minutes and the transitions between them
  feel natural — which is the same phenomenon
  [[2026-03-13_design-process-isnt-dead]] describes when it argues that senior
  practitioners are compressing the process rather than skipping it. The skill is process literacy —
  matching the right process to the problem — rather than either dogmatic
  application or abandonment. What looks like skipping steps in senior
  practitioners is compression: discovery, ideation and evaluation run
  nonlinearly and faster because they have been internalised. Solution-first
  work succeeds only where the problem space is mature, users sophisticated and
  organisational maturity high, and in regulated domains (healthcare, finance,
  government) process is a safeguard against harm
  ([[2026-03-13_design-process-isnt-dead]]).
- On templates the sources pull in opposite directions.
  [[2024-09-13_free-ux-templates]] offers pre-built templates across the whole
  workflow — research plans, consent forms, interview guides, journey maps,
  service blueprints, empathy maps, storyboards, content audits, critiques, RACI
  matrices — as a way to overcome blocks and save documentation time.
  [[2025-05-30_template-trap]] argues that template culture, amplified by social
  media stripping frameworks of their original context, substitutes
  plug-and-play application for the contextual thinking UX requires, and hits
  newer practitioners hardest. Its remedy is not to reject templates but to
  start from goals rather than from the template, check alignment with those
  goals, look for real case studies of use, and modify deliberately.
- The two journey-mapping sources also disagree on shortcuts.
  [[2020-06-14_journey-mapping-approaches]] recommends assumption-first mapping
  when time or budget is short, as a fast route to alignment and buy-in (with a
  hybrid — assumption map, then research validation, then future state — as the
  best default). The later time survey [[2022-12-18_journey-map-how-much-time]]
  found that hypothesis-first teams reported spending as much time or more
  overall than research-first teams, suggesting the upfront research investment
  pays for itself.

### AI in the process

- Where AI helps and where it does not has been tracked over time. In 2024,
  designers used text-based AI for brainstorming, ideation and copy but used
  essentially no design-specific AI tools in serious professional work;
  non-determinism made outputs useful for ideation and unusable for production
  ([[2024-04-12_ai-design-tools-not-ready]]). By 2025 narrow-scope features
  (renaming layers, rewriting content, finding assets, palette generation,
  placeholder imagery) had become genuinely useful, while broad
  wireframe/prototype generation still produced generic layouts with poor
  hierarchy, could not pull from a design system, and was throttled by short
  prompt limits ([[2025-05-09_ai-design-tools-update-2]]).
- Output quality tracks the quality of the input. Longer, more specific prompts
  and, better still, design artifacts such as Figma links or high-fidelity
  mockups as references, produce markedly better results, because the model can
  read existing patterns and spatial relationships instead of guessing; even
  then AI misses visual hierarchy, grouping of related elements, spacing and
  colour contrast, and skews toward the mainstream conventions present in its
  training data — good from afar, far from good. Designers must disambiguate
  their own vocabulary, since a term like "profile page" carries several
  meanings, and the tools work best for people who already know layout,
  typography and component naming well enough to direct them: strong design
  knowledge is a prerequisite for AI prototyping, not a substitute for it
  ([[2025-10-24_ai-prototyping]]). [[2025-12-05_vague-prototyping]] gives the
  failure mode a name — the *Frankenstein layout*, randomly assembled, with
  content repeated, prominent containers holding little, and hierarchy running
  against task priority — and five fixes that need no polished design work:
  precise visual keywords drawn from established style vocabulary rather than
  "modern" or "clean", lightweight visual references such as moodboards or
  design-system screenshots, using a chatbot to extract design characteristics
  from those references, generating mock data so layout follows real content,
  and attaching code snippets from the existing system. Its limit is the same
  one: AI speeds execution, but weighing requirements and tradeoffs stays
  designer work.
- Structure the prompting itself: CARE — Context (background, users, mission,
  goals, tone), Ask (role, format, number of options, steps), Rules
  (constraints, brand and product guidelines), Examples (what you do and do not
  want). Prompting well takes real upfront effort and still requires iteration
  on the output ([[2024-05-24_careful-prompts]]).
- Two cautions about what speed costs. AI removes the friction of making, and
  that friction is where some of the thinking happened — generating a task flow
  gives you the output without the learning ([[2026-05-22_design-disposables]]);
  and faster cycles do not remove the uncertainty that process frameworks exist
  to manage ([[2026-03-13_design-process-isnt-dead]]). Research data must never
  be generated artificially ([[2024-04-12_ai-design-tools-not-ready]]).
- Looking further out, generative UI would shift the designer's work from
  designing discrete interface elements to defining outcomes, user goals and
  constraints for the AI to satisfy, making user research and testing more
  important rather than less, while raising risks around hallucination, bias,
  privacy-sensitive data and the loss of interface consistency
  ([[2024-03-22_generative-ui]]).

## Sources (48)

- [[2016-07-31_customer-journey-mapping]] — Journey mapping is a key UX research and strategy activity that identifies gaps and opportunities in customer experiences.
- [[2016-07-31_design-thinking]] — The six-phase design thinking process (empathize, define, ideate, prototype, test, implement) provides structure while remaining iterative and flexible.
- [[2016-08-14_outcomes-vs-features]] — User-centered design begins with problem discovery; research methods identify real needs before ideation and prototyping.
- [[2016-08-28_ux-success-agile]] — Provides ten concrete practices for integrating UX work into Agile, including discovery before sprints, working ahead, collaboration, and treating methodology itself as iterative.
- [[2016-10-16_journey-mapping-ux-practitioners]] — Shows journey mapping as a team activity requiring clear scope, research grounding, collaborative creation, and implementation planning to drive organizational change and improved customer experiences.
- [[2016-10-23_design-critiques]] — Critiques are positioned as a key iterative stage where feedback can be incorporated before a design is final, reducing project costs and timelines.
- [[2017-02-05_remote-customer-journey-mapping]] — journey mapping requires cross-functional teams, diverse perspectives, and ongoing iteration; distributed teams face amplified challenges around buy-in, outcome skepticism, and iteration difficulty.
- [[2017-02-12_ux-research-cheat-sheet]] — research methods are organized by four design phases: Discover, Explore, Test, and Listen.
- [[2017-10-08_ux-lessons]] — emphasizes integration of research into regular project cadence rather than ad-hoc application.
- [[2017-10-29_ideation-in-practice]] — establishes timing of ideation within the design cycle and relationship to research and prototyping phases.
- [[2018-01-28_why-personas-fail]] — The systematic approach to creating products; personas serve as reference points throughout the process; their value depends on being integrated into discussions and decisions.
- [[2018-02-25_ux-expert-reviews]] — using expert reviews iteratively throughout design creation to catch and fix issues before development.
- [[2018-03-25_post-it-in-ux]] — employing Post-its as collaborative ideation and synthesis tools during design discovery and research phases.
- [[2018-05-27_prioritization-matrices]] — Prioritization matrices are presented as a structured decision-making tool within the UX design process that enables teams to make informed decisions about which problems to solve and features to implement.
- [[2018-08-26_case-study-iterative-design-prototyping]] — the structured approach to creating user experiences, including goal setting, research, prototyping, testing, and specification; this article models a practical, lean process.
- [[2018-11-11_ux-debt]] — how to systematically identify and address quality issues in user experiences, and balance competing priorities between new features and existing quality.
- [[2019-03-24_user-need-statements]] — Need statements serve as a north star for alignment across team members and stakeholders throughout the project.
- [[2019-04-07_journey-mapping-faq]] — Journey mapping helps teams prioritize problems and iterate designs based on validated customer experiences.
- [[2019-04-21_sympathy-vs-empathy-ux]] — Empathic design requires diverse teams, direct user contact, and protocols that counter unconscious bias and false consensus.
- [[2019-09-08_parking-lots]] — Parking lots help design teams capture research questions and assumptions that emerge during workshops, informing future research plans and preventing rabbit-hole discussions.
- [[2019-12-08_5-ux-workshops]] — places workshops strategically throughout design lifecycle from discovery through critique phases.
- [[2020-03-15_discovery-phase]] — positions discovery as the first critical stage in the double-diamond model that frames problems before ideation and testing.
- [[2020-06-14_journey-mapping-approaches]] — methodological decisions about how to conduct journey mapping and when to involve research.
- [[2020-07-05_journey-mapping-workshop]] — how journey mapping fits into the larger design process and connects current-state understanding to future-state visioning.
- [[2020-07-05_ux-roadmaps]] — how roadmaps guide and align design activity and decision-making.
- [[2020-07-19_service-blueprinting-template]] — service blueprinting as a collaborative workshop activity and living document for organization-wide alignment.
- [[2021-03-07_journey-mapping-tips]] — the article situates journey mapping within the broader UX design and research process as a foundational tool.
- [[2021-03-21_visual-design-heuristics-posters]] — the article illustrates a complete user-centered design and iteration process applied to non-interactive artifacts.
- [[2021-06-20_draw-wireframe-even-if-you-cant-draw]] — Wireframing is an early design process step for exploring solutions; step-by-step progression from overall layout to detail prevents getting stuck on aesthetics.
- [[2022-12-18_journey-map-how-much-time]] — Whether following research-first or hypothesis-first approaches, journey-mapping projects require substantial time allocation for stakeholder buy-in and resource securing across all organizational types.
- [[2023-02-12_using-empathy-maps]] — empathy maps support different phases of the design process by clarifying research questions early on and ensuring findings reach and engage the entire team.
- [[2023-02-26_mood-boards]] — mood boards facilitate early-stage design alignment and reduce revisions by establishing shared visual direction before prototyping begins.
- [[2023-05-28_design-risk-management]] — The structured approach to creating solutions that incorporates risk identification, assessment, and control as integral stages.
- [[2023-11-24_surveys-design-cycle]] — the four-phase design cycle (Discover, Explore, Test, Listen) provides a framework for selecting appropriate research methods including surveys.
- [[2024-03-22_generative-ui]] — shows how generative UI fundamentally transforms designer work from component design to outcome and constraint definition.
- [[2024-04-12_ai-design-tools-not-ready]] — discusses where AI could potentially support designers (ideation, brainstorming, copy) versus where it currently cannot (visual design, wireframing, component generation).
- [[2024-05-24_careful-prompts]] — prompt engineering can support various UX tasks (copy writing, concept generation, persona creation) when designers provide sufficient context and constraints.
- [[2024-09-13_free-ux-templates]] — the structured processes and phases that UX practitioners follow to research, design, and validate user experiences.
- [[2025-05-09_ai-design-tools-update-2]] — describes how narrow-scope AI augments specific design tasks while broad AI fails to support end-to-end design process.
- [[2025-05-30_template-trap]] — the iterative, contextual work of understanding problems and developing solutions, degraded when compressed into template-following workflows.
- [[2025-08-29_informal-ux-maturity]] — The four maturity factors (strategy, culture, process, outcomes) provide a framework for assessing how UX work is structured.
- [[2025-10-24_ai-prototyping]] — what this article contributes to this concept
- [[2025-12-05_vague-prototyping]] — what this article contributes to this concept
- [[2026-02-27_ux-postmortems]] — Postmortems are an essential governance practice that helps teams systematize their approach to projects and reduce repeated mistakes.
- [[2026-03-13_design-process-isnt-dead]] — The article defends structured design frameworks as essential scaffolding that, once internalized, become implicit in experienced practitioners' work.
- [[2026-04-17_information-pipeline]] — Shows how information gathering becomes a repeatable process that supports long-term career development in complex organizations.
- [[2026-05-22_design-disposables]] — Successful design processes distinguish between exploration and delivery phases; exploration benefits from low-cost iteration and low attachment; delivery requires care and polish.
- [[2018-02-12_solving-design-exercises_08-the-framework]] — describes how the framework reflects real-world product development, where most steps involve cross-functional collaboration except for the UI/UX execution phase.
