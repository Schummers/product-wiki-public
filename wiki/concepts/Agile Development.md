---
type: concept
name: Agile Development
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Agile Methodology"
  - "Definition of Done"
  - "Effort Estimation"
  - "Estimation"
  - "Product Owner"
  - "Story Points"
---

# Agile Development

## Definition

Agile, in the sources here, is not treated as a speed doctrine: it is about
prioritising and delivering small, high-value increments to users, early and
often [[2023-02-05_discovery-in-agile]]. It shows up in this corpus mainly
through its artefacts and rituals — sprints, backlogs, story points, spikes, and
retrospectives — and through the recurring question of how UX work fits inside
them. Its defining property, repeatedly exploited by the sources, is
flexibility: there is no definitive rulebook for Agile backlogs, and every team
may structure its own differently [[2019-10-06_ux-agile-backlog]].

Jeff Patton, in *User Story Mapping*, ties the practice to Agile's own origin
story: user stories emerged from Kent Beck's insight that document-driven
requirements fail because different readers imagine different solutions from
the same document, and Beck replaced specification with conversation — teams
talk together to build shared understanding instead of one person writing a
spec another must interpret. Stories are a reaction against document-driven
development inside Extreme Programming and Agile practice, prioritising
conversation, collaboration and flexibility over upfront specification
[[2014-09-05_user-story-mapping_11-6-the-real-story-about-stories]].

In the book's foreword, Marty Cagan draws the line between strong and weak
Agile teams sharper than the corpus does elsewhere: what separates them is not
process compliance but vision, discovery habits, and how outcome is defined
[[2014-09-05_user-story-mapping_03-foreword-by-marty-cagan]].

The corpus reads Agile as a set of pressures as much as a method. The cadence
that produces frequent releases also produces pressure to ship that turns into
quality compromises if nothing counterbalances it [[2018-11-11_ux-debt]], and
sprint-length timeboxes tempt teams into rushing or skipping the learning that
should precede a solution [[2023-02-05_discovery-in-agile]]. Several of the
practices documented here — front-end style guides
[[2016-03-27_front-end-style-guides]], UX-debt tracking [[2018-11-11_ux-debt]],
scaled discovery [[2023-02-05_discovery-in-agile]] — exist precisely as
responses to those pressures.

Christian Crumlish adds the role vocabulary the framework carries with it. In
his definition the **product owner** is an Agile scrum role: engineer-centric
and tactical, focused on shaping and guiding the engineering team and tracking
tasks, originating from the engineering pool and, in his words, "invented in the
absence of true product managers," sometimes paired with a certified scrum
master; some businesses treat it as an entry-level product management title,
and he notes the title is used many other ways in practice
[[2022-01-19_product-management-for-ux-people_04-chapter-1-what-exactly-does-a-product-manager-do]].

## Practice

### What separates strong Agile teams from weak ones (Cagan)

Cagan's foreword contrasts good and bad teams across the dimensions that,
in his framing, actually determine whether Agile delivers
[[2014-09-05_user-story-mapping_03-foreword-by-marty-cagan]]:

- **Vision versus mercenary execution** — good teams pursue a compelling
  product vision "with a missionary-like passion"; bad teams are mercenaries
  executing orders without genuine commitment.
- **Customer-driven discovery versus passive requirements-gathering** — good
  teams draw ideas from KPIs, customer observation and data; bad teams gather
  requirements passively from sales and stakeholders.
- **Rapid validation versus roadmap meetings** — good teams test ideas quickly
  to see which are worth building; bad teams hold meetings to produce a
  prioritised roadmap instead of validating anything.
- **Side-by-side collaboration versus silos** — good teams have product,
  design and engineering working with mutual influence; bad teams communicate
  through formal requests across silos.
- **Engineers in discovery versus engineers at sprint planning** — good teams
  let engineers review discovery prototypes daily so they can contribute; bad
  teams only show prototypes at sprint planning, for estimation.
- **Outcome versus output** — good teams know many favourite ideas will fail
  and expect several iterations before an idea delivers the outcome it was
  meant to; bad teams build what is on the roadmap and stop once it ships, as
  long as dates and quality are met.

Cagan situates story mapping itself inside this contrast: it is not a
technique that fixes a weak team by itself, but a gateway that either enables
or is undermined by which of these two patterns a team actually practises
[[2014-09-05_user-story-mapping_03-foreword-by-marty-cagan]].

### Fitting UX work into the backlog

Agile teams face a standing dilemma: how to get UX work into the backlog without
it being deprioritised in favour of features. Three models are described, each
with its own trade-off [[2019-10-06_ux-agile-backlog]]:

- **Unified backlog with explicit UX items** — UX work is tagged and prioritised
  alongside features, which makes it visible to stakeholders, but leaves
  research and design vulnerable to consistent deprioritisation where
  stakeholders undervalue UX.
- **Task-based unified backlog** — one backlog item is broken into role-specific
  subtasks. Works best in a well-understood domain where design and development
  both fit in a single sprint, but demands strong estimation: multiple roles
  estimate differently (story points for development, t-shirt sizes for UX), so
  coordination and dependency tracking get complex.
- **Separate backlogs** — UX work is kept apart from development. Suits large
  teams, multiple UX specialties, several engineering teams (iOS, Android, web),
  or work that must run ahead of development; it buys autonomy at the price of
  velocity visibility, and requires discipline and communication to keep timing
  aligned.

Two rules cut across all three: UX work that blocks development must be
explicitly visible and prioritised, since weak dependency tracking risks
stalling development sprints; and the structure should match team context and
change as team dynamics, product maturity, and stakeholder understanding evolve
[[2019-10-06_ux-agile-backlog]]. The stated key is understanding how the team
works together and how much influence stakeholders have over the backlog.

### Scaling discovery instead of skipping it

Discovery — learning about problems before building solutions — is presented as
essential to Agile yet routinely rushed or dropped under sprint timelines. The
recommended mindset is to scale it, not skip it: discovery timing should not be
arbitrarily constrained to sprint length, and scaled discovery concentrates on
specific, valuable activities and assumptions rather than every possible
question [[2023-02-05_discovery-in-agile]].

The SCALE mnemonic structures this [[2023-02-05_discovery-in-agile]]:

- **Speak and spike** — communicate the need for discovery and use spikes for
  research.
- **Capture** — identify where the team is aligned and where it conflicts.
- **Assign** — distribute the discovery activities.
- **Learn and share** — communicate findings continuously.
- **Evaluate and decide** — assess readiness to move forward.

Practical details attached to it: spikes add dedicated sprint time for research
and should be constrained to one or two key questions and completed early in the
sprint so they can inform the delivery work that follows; having team members
individually draft problem or opportunity statements and then converge surfaces
diverse perspectives and knowledge gaps; and discovery is broader than user
research, also covering business documents, stakeholder interviews, analytics,
past research, and heuristic evaluation, so the most valuable activities for the
available time should be prioritised. UX, product, and engineering should all
take part, since shared understanding from collaborative discovery speeds
delivery and reduces rework. Sustaining the practice is helped by UX
representation in leadership, tracking discovery velocity, and avoiding
premature assignment of delivery tasks [[2023-02-05_discovery-in-agile]].

### The cadence as the product manager's main channel

Crumlish describes the Agile rhythm from the product manager's seat rather than
the designer's. The tooling and cadence are scrum: Jira with Confluence, epics
decomposed into user stories, backlog grooming, biweekly planning, daily
stand-ups, answering developer questions on tickets, reviewing demos and
automated test data, reading burn-down charts, running retrospectives, and
reporting the roadmap to leadership quarterly if not monthly — with the PM
functioning as a de facto product owner at stand-up
[[2022-01-19_product-management-for-ux-people_05-chapter-2-do-you-want-to-be-a-product-manager]].

These check-ins form a fractal: daily stand-ups, sprints of two to four weeks,
monthly roadmap reviews, quarterly planning, annual goal-setting, each
reinforcing the same "iterate, review, recalibrate, repeat" cycle, and together
they are the PM's primary channel for collaborating with engineers
[[2022-01-19_product-management-for-ux-people_07-chapter-4-wrangling-engineers]].
The reason to route communication through them is that engineers are makers who
need uninterrupted time for deep work, so Crumlish routes communication into
two channels instead of micro-interruptions: asynchronous written formats
developers can review when it suits them, and these regular cadences. The PM's role inside them is facilitation, not
command — engineers do not report to the PM 99% of the time, nor should they.

Two practices attach to the sprint itself
[[2022-01-19_product-management-for-ux-people_07-chapter-4-wrangling-engineers]]:

- **Definition of done needs team buy-in** — a shared definition tied to the
  requirements documents that defined the original problem space, and meaning
  coded, tested and accepted, which is what stops constant
  slippage and lets the team escape the paralysis of perfectionism.
- **Estimation is a negotiation, not a demand** — different engineers pad or
  underestimate differently, so the PM facilitates a balanced discussion and
  treats estimates as best-effort assessments of where to invest time and
  resources. John Cutler, quoted in the same book, lists being pressured for
  estimates you know are worthless among his "44 signs you are becoming a
  product manager"
  [[2022-01-19_product-management-for-ux-people_05-chapter-2-do-you-want-to-be-a-product-manager]].

Patton reaches a compatible but differently grounded conclusion in *User Story
Mapping*, through Aaron and Mike's delivery at Workiva
[[2014-09-05_user-story-mapping_09-4-plan-to-finish-on-time]]. Where Crumlish's
point is procedural — negotiate the estimate, don't demand it — Patton's is
about what makes an estimate accurate in the first place: "the best estimates
come from developers who really understand what they're estimating," so
shared understanding built through mapping conversations, not the estimation
method applied to unclear requirements, is what improves accuracy. He then
treats the estimate itself as **a budget to manage actively** rather than a
one-time commitment: teams track actual velocity against it as work proceeds,
and if they are halfway through the schedule but only a third through the
scope, that is the signal to replan or escalate, not to keep going and hope.
A sidebar from Chris Shinkle of SEP gives a concrete failure mode this catches:
a team building a wireless access-control system kept missing milestones from
unplanned work, until they added "Risk Stories" alongside ordinary activities,
tasks and details, so the map showed the unknown work as well as the known
[[2014-09-05_user-story-mapping_09-4-plan-to-finish-on-time]].

Patton also gives release planning a specific shape at Workiva: slice delivery
into an **opening game** (core functionality end-to-end, a "functional walking
skeleton" that surfaces technical risk early), a **midgame** (filling in
features and edge cases), and an **endgame** (refinement and polish), rather
than building layer by layer and assembling at the end. He frames this as
artistic rather than mechanical, citing Leonardo da Vinci's "great art is
never finished, only abandoned" for the idea that a team iterates and refines
continuously within a time constraint instead of hoping separately-built
pieces fit together later [[2014-09-05_user-story-mapping_09-4-plan-to-finish-on-time]].

### Managing the quality debt the cadence creates

UX debt is the accumulation of ongoing experience problems caused by shipping
expedient solutions rather than ideal ones — the direct analogue of technical
debt, whose costs compound over time [[2018-11-11_ux-debt]]. In Agile teams the
pressure to ship new features regularly is what generates it, alongside skipped
testing, inconsistent design, poor communication, and integration difficulty.
The compounding is not only financial: users who hit a poor experience abandon
the product and post negative reviews, and they do not come back to retry once
it is fixed. Worse, behaviour adapts to bad design, so improving it later can
itself drive users away, and repeatedly changing inconsistent components damages
perceived coherence [[2018-11-11_ux-debt]].

The management routine offered fits Agile rituals directly
[[2018-11-11_ux-debt]]: surface debt through monthly usability testing, customer
service reports, surveys, and team retrospectives; prioritise it on a matrix
plotting user value (frequency, severity, impact) against effort to fix; and
allocate recurring capacity — story points reserved each sprint, or quarterly
cleanup sprints — so debt is reduced gradually instead of deferred forever. The
framing argument for that budget is that a feature people cannot use might as
well not exist, so fixing it delivers the same customer value as adding one.

### Retrospectives as the improvement loop

Retrospectives are the regular meeting where a team reflects on how its members
work together and considers process improvements based on recently completed
work; they are typically practised inside Agile and Scrum at sprint end, though
the source is explicit that any team benefits regardless of methodology
[[2019-02-17_ux-retrospectives]]. Guidance:

- **Set ground rules first** — no blame, focus on the team rather than
  individual shortcomings, stay open to different perspectives. The meeting must
  be a safe space to raise issues without fear of retaliation, and raising an
  issue must not read as negative.
- **Open with what went well** — acknowledge accomplishments and what propelled
  the team forward, crediting the team as a whole rather than individuals.
- **Then handle improvement areas constructively** — inclusive language ("we
  fell short" rather than "you failed") preserves psychological safety.
- **Produce realistic action items** — grounded in the discussion, large items
  broken down, each with an owner and a due date.
- **Close the loop** — review the previous retrospective's action items before
  starting a new one and check progress, which demonstrates commitment.
- **Keep it fresh** — rotate facilitators, vary formats and icebreakers to
  prevent retrospective fatigue.

Crumlish is blunter about whether the ritual is optional: end-of-sprint retros
where the team reflects on what went well and what can improve are "not
optional," and practised openly and supportively they drive team cohesion and
effectiveness
[[2022-01-19_product-management-for-ux-people_07-chapter-4-wrangling-engineers]].

Retrospectives also serve as one of the detection mechanisms for UX debt
[[2018-11-11_ux-debt]], which links the two practices: the ritual that reviews
the process is also where accumulated quality problems get named.

### Tooling that keeps design fast and consistent

Front-end style guides — modular collections of a product's UI elements together
with the code snippets developers copy to implement them — originated in Agile
and Lean environments as a response to the need for faster, more modular design
workflows [[2016-03-27_front-end-style-guides]]. They are simultaneously a UX
deliverable and a tool used by the whole team to keep product design consistent
and nimble across iterations. Their value in this context is throughput plus
consistency: they cut design-specification time, allow fast high-fidelity
prototyping, and enforce visual consistency by making it less work to do the
right thing than to invent a new inconsistent design. Unlike a static PDF they
are living digital assets that update as components change, and modern ones
cover layout grids, spacing rules, and responsive component behaviour, with 25+
documented UI elements and dos and don'ts for each
[[2016-03-27_front-end-style-guides]].

## Sources (11)

- [[2016-03-27_front-end-style-guides]] — Front-end style guides originated in Agile and Lean environments as a response to the need for faster, more modular design workflows.
- [[2018-11-11_ux-debt]] — managing UX debt within agile teams where pressure to ship new features regularly can lead to quality compromises if not actively managed.
- [[2019-02-17_ux-retrospectives]] — Retrospectives as practiced within Agile and Scrum frameworks, typically held at sprint end to review sprint work and plan improvements.
- [[2019-10-06_ux-agile-backlog]] — Agile flexibility enables different backlog structures; UX integration requires intentional choices about visibility, prioritization, and team structure.
- [[2023-02-05_discovery-in-agile]] — Discovery aligns with Agile values; scaling discovery rather than skipping or rushing it enables teams to deliver value efficiently while managing risk.
- [[2022-01-19_product-management-for-ux-people_04-chapter-1-what-exactly-does-a-product-manager-do]] — The product owner is presented as an Agile scrum role, engineer-centric and tactical, "invented in the absence of true product managers," sometimes paired with a certified scrum master; some businesses treat it as an entry-level product management title.
- [[2022-01-19_product-management-for-ux-people_05-chapter-2-do-you-want-to-be-a-product-manager]] — The PM's tooling and cadence are Agile scrum: Jira with Confluence, epics decomposed into user stories, biweekly planning, daily stand-ups, demos, retrospectives, burn-down charts, and functioning as a de facto product owner at stand-up.
- [[2022-01-19_product-management-for-ux-people_07-chapter-4-wrangling-engineers]] — The chapter details the fractal of cadences (daily stand-ups, sprints of 2–4 weeks, monthly roadmap reviews, quarterly planning, annual goal-setting) and how each reinforces the "iterate, review, recalibrate" cycle; Estimating sprint capacity is a negotiation, not a demand; different engineers pad or underestimate differently, and the PM's job is to facilitate balanced discussion and recognize that estimates are best-effort assessments of where to invest time and resources.
- [[2014-09-05_user-story-mapping_03-foreword-by-marty-cagan]] — While the book is about a technique used in Agile, Cagan situates story mapping within the broader context of how Agile principles can either enable or be undermined by team practices.
- [[2014-09-05_user-story-mapping_09-4-plan-to-finish-on-time]] — Improved by involving developers in mapping conversations, treating estimates as budgets to manage actively, and measuring actual work against estimates to improve future predictions.
- [[2014-09-05_user-story-mapping_11-6-the-real-story-about-stories]] — The story-based approach originated in Extreme Programming and Agile practices as a reaction against document-driven development; it prioritizes conversation, collaboration, and flexibility over upfront specification.
