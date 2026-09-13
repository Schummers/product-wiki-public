---
type: concept
name: Design Strategy
created: 2026-07-31
updated: 2026-09-11
status: developed
---

# Design Strategy

## Definition

Design strategy is the practice of connecting design decisions to where the
organisation is trying to go, rather than to the artefact in front of the
designer. Across the sources it appears at two altitudes. At the organisational
level, [[2023-03-12_strategy-study-guide]] (Nielsen Norman Group) frames UX
strategy as a plan of actions meant to reach an improved future state of an
organisation's user experience over an established period, built from three
components: a research-based vision of the intended future state, goals and
metrics that tie UX work to business outcomes, and a plan with roadmaps and
prioritisation. At the individual level, [[2023-09-05_path-to-senior-product-designer_19-17-strategy]]
(Artiom Dashinsky) defines strategy as a competency: understanding the internal
factors that drive business decisions (objectives and metrics, mission and
vision, roadmap, organisational structure and team incentives) and the external
ones (competitors, industry context), so design decisions can be made with that
picture in view.

Both readings share the same claim: strategy is what separates a designer who
executes a brief from one who decides what is worth building and why.
[[2025-06-06_future-proof-designer]] (Nielsen Norman Group) puts it as the
distinction between strategic and tactical work, and argues that in an
AI-driven product landscape a narrow definition of design as UI polish is what
makes a designer replaceable; the panel it reports quotes the position bluntly,
"Design is either becoming more strategic or completely irrelevant." Strategy in
these sources is therefore not a separate deliverable but a lens applied to
ordinary decisions: which platform gets its own solution, which problem gets
solved first, and when a design is done.

## Practice

### Vision, goals and plan

[[2023-03-12_strategy-study-guide]] organises strategy work into vision, goals
and measurement, and plan. The vision is an aspirational statement of the
product's ideal form and the value it gives users, and the guide insists it must
be grounded in research and viable in the market rather than merely aspirational.
Goals connect UX improvements to business KPIs so that progress is trackable.
The plan turns this into roadmaps that show how problems will be solved
immediately, in the near future and further out; the guide reports that
theme-based roadmaps, centred on high-level opportunities, communicate
experience strategy more effectively than feature-focused ones. On
prioritisation it declines to name a single best method: the right one varies
with project context, team culture and success criteria.

### Learning the business

[[2023-09-05_path-to-senior-product-designer_19-17-strategy]] gives the
individual counterpart. Dashinsky recommends asking your manager for the
documentation of the company's KPIs and OKRs (his examples include revenue per
customer, conversion rate and host churn) and contributing to the team's
progress on them, on the grounds that the CEO's primary question about any
design is how it increases revenue or reduces costs. He also recommends
familiarising yourself with the vision statement, the planned features and
timelines, and an organisational chart, which helps identify which design
conflicts to avoid, which feature ideas are already planned, and who to partner
with to influence decisions. Different roles carry different incentives, so
mapping stakeholder objectives reveals who holds authority over which topic.
Externally, he suggests identifying direct competitors and tracking their
product updates and launches using tools such as G2, Product Hunt or Google
auto-complete, learning from negative reviews to fix your own problems and from
positive ones to understand what users value, and following industry-leading
companies and their leadership. The first such analysis is effortful; the point
of doing it is that it leaves a reusable mental framework for the next business.

The same chapter frames the payoff as being more like a product manager without
taking on the full role: the designer who suggests how to simplify a task so it
costs less development effort while keeping the business impact provides more
value than the one who executes the brief as written.

### Choosing what to work on

[[2023-09-05_path-to-senior-product-designer_18-16-independence-ownership]]
treats prioritisation as strategy exercised on your own queue. Dashinsky rates
tasks one to ten on importance and urgency and places them on a matrix he
adapts from the Eisenhower matrix, which yields a priority from one to four, and
recommends identifying a Most Important Task each morning and doing it when you
are most productive. When proposing a new initiative he advises framing it as a
business problem, presenting alternatives with their trade-offs, supporting them
with data and business context, explaining how success will be measured,
justifying the timing against available resources, and proposing next steps that
do not add work to your manager.

[[2023-09-05_path-to-senior-product-designer_12-10-tools-and-processes-craft]]
extends the same logic to processes: identifying which processes are worth
improving, and how, sits above executing within them, and the chapter argues
that someone who initiates and defines processes has more leverage than someone
who follows them.

### Knowing when to stop

[[2023-09-05_path-to-senior-product-designer_17-15-shipping-ownership]] applies
strategy to the end of a project. The point at which a design achieves its goal
often arrives before the designer is satisfied with it, and Dashinsky argues
everything after that point is low-ROI work. Deciding what counts as "good
enough to ship" therefore depends on knowing which business goal the design has
to hit; a designer who understands that case can stop iterating with more
confidence.

### Strategy applied to platform decisions

[[2016-07-24_mobile-first-not-mobile-only]] (Kara Pernice and Raluca Budiu,
Nielsen Norman Group) is a worked case of a strategic call going wrong in
execution. Mobile-first is a sound prioritisation strategy, they write, but it
is not mobile-only: their quantitative testing of navigation across six websites
on desktop and mobile found lower navigation use on desktop, which they
attribute not to desktop users needing navigation less but to desktop interfaces
that were mobile designs ported unchanged. Patterns that work on mobile,
including hamburger menus and search icons in place of search boxes, hurt
desktop usability. Their conclusion is that each platform should be optimised
for its own strengths and constraints: "Tempting as it may be to design once and
use twice, it can result in a subpar user experience for one of the platforms,
and maybe for both of them."

### Deliverables that carry strategy

[[2025-10-03_persona]] (Taylor Dykes, Nielsen Norman Group) positions personas
as a strategic deliverable rather than a research artefact: the persona's name
becomes shorthand for the full set of attributes, goals and behaviours a team
must consider, giving a shared and precise reference instead of each member
holding a different mental model of "the user", and helping the team resist
designing for everyone. The article notes that personas built collaboratively
are more likely to be believed and used, and that they remain useful beyond
design for recruiting test participants, segmenting analytics and guiding expert
reviews.

### The strategic skills themselves

[[2025-06-06_future-proof-designer]] reports four practices identified by a
panel of product and design strategists: extending scope beyond UI work,
strengthening storytelling and emotional intelligence, framing conversations
around outcomes rather than feature novelty, and developing judgment about data.
The article's argument is that AI surfaces patterns at scale but humans must
assess reliability, ask sharp questions and decide which insights matter, and
that understanding stakeholder motivations and speaking their language is what
lets a designer influence decisions. Dashinsky reaches a converging conclusion
from a different angle in [[2023-09-05_path-to-senior-product-designer_19-17-strategy]]:
he credits his own trajectory to getting his craft to a good-enough level and
then redirecting his learning toward non-design skills.

## Sources (8)

- [[2016-07-24_mobile-first-not-mobile-only]] — Mobile-first design thinking is valuable for prioritization, but execution must adapt solutions to each platform rather than forcing ports.
- [[2023-03-12_strategy-study-guide]] — design strategy operationalizes vision through goals, roadmaps, and prioritization methods that help teams maintain strategic direction while solving user problems.
- [[2025-06-06_future-proof-designer]] — the practice of aligning design decisions with business objectives and user needs, distinguishing strategic designers from tactical executors.
- [[2025-10-03_persona]] — Personas are foundational deliverables that inform design strategy through shared vocabulary, common reference for decisions, and ongoing validation/refinement as living documents aligned with user behavior.
- [[2023-09-05_path-to-senior-product-designer_12-10-tools-and-processes-craft]] — Strategic thinking about process design and improvement sits at a higher level than execution; identifying which processes to optimize and how creates organizational-level impact.
- [[2023-09-05_path-to-senior-product-designer_17-15-shipping-ownership]] — making deliberate decisions about what qualifies as "good enough to ship" and understanding the business goal that the design needs to achieve so you can stop iterating at the right point.
- [[2023-09-05_path-to-senior-product-designer_18-16-independence-ownership]] — prioritizing what to work on independently using importance and urgency, timing new initiatives to align with business context and available resources, and understanding business problems well enough to position design solutions as business solutions.
- [[2023-09-05_path-to-senior-product-designer_19-17-strategy]] — This chapter defines strategy as understanding internal business factors (objectives, vision, roadmap, people) and external factors (competition) to make informed design decisions and increase career impact.
