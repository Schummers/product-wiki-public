---
type: concept
name: Problem Framing
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Problem Definition"
  - "Problem-First Design"
---

# Problem Framing

## Definition

Problem framing is the work of defining and articulating what needs to be solved,
for whom, and why it matters, before any solution is proposed
([[2021-08-22_problem-statements]], [[2024-09-27_7-tips-discovery]]). The sources
treat it as the foundation the rest of the process rests on: a great solution to
the wrong problem will fail ([[2019-03-24_user-need-statements]]), and the
commonest trap in product planning is discussing what to build before defining
its purpose ([[2016-08-14_outcomes-vs-features]]). Framing therefore has both a
cognitive function — resisting the pull toward a preferred solution
([[2024-10-11_discovery-mindset]]) — and an organisational one, since a written
frame is what gives a team shared scope and stakeholders a reason to fund the
work ([[2021-08-22_problem-statements]]).

The corpus offers three related artefacts rather than one: the problem statement,
which describes the problem, the people affected and the organisational impact
([[2021-08-22_problem-statements]]); the user need statement, which names a
specific user, a research-grounded need and an insight about the outcome sought
([[2019-03-24_user-need-statements]]); and the How Might We question, which turns
a research finding into a design challenge open enough to ideate against
([[2021-01-17_how-might-we-questions]]). Two later sources extend the same
principle to technology choices: whether AI belongs in a product is answered by
the framed problem, not the reverse ([[2025-03-28_ai-superpowers]]), and framing
the problem is named as the part of the job AI cannot yet do
([[2025-05-09_ux-job-with-ai]]).

An earlier source adds a fourth structure and a different starting condition.
[[2018-02-12_solving-design-exercises_07-answer-structure]] frames a problem
through 5W1H — Why (the goal), Who (the audience), When and Where (the context),
What (the product) and How (the measurement) — a technique it traces to
journalism, research and police investigations and reports as already in use in
product building. And where the sources above assume access to research,
[[2018-02-12_solving-design-exercises_06-chapter-2-how-to-solve-a-product-design-exercise]]
works from the case where the brief is deliberately incomplete: framing there
consists of clarifying questions plus assumptions stated openly and backed by
reasoning, an assumption being defined as a claim backed by little or no data
that is nonetheless needed to build a successful product.

## Practice

### Outcomes before outputs

[[2016-08-14_outcomes-vs-features]] draws the distinction plainly: an output is
the product or service created, an outcome is the problem solved, and products
fail when they solve problems nobody cares about. It compares this to the
marketing distinction between features and benefits — a feature is what a product
offers, a benefit is what customers actually want. Its five steps: state the
problem clearly and say who it is for; gather user data proving the problem
exists rather than deciding on gut feel; define the core competencies that give
sustainable advantage instead of chasing trendy peripheral features; set concrete
goals with clear success criteria; and test multiple ideas with users. Time spent
on discovery, it argues, prevents resources spent building the wrong thing.

### Writing the problem statement

[[2021-08-22_problem-statements]] treats the statement as the thing that keeps a
discovery from meandering, and specifies its content through the five Ws: who is
affected, what the problem is, where and when it occurs, and why it matters. It
requires three elements — background and origin of the problem, the people
affected (internal and external, several groups if relevant), and the
organisational impact, whether reputational, financial or operational. It is
explicit on scope: one discovery effort, one problem statement, focused on one
problem, and kept concise. Teams need not have every answer up front, particularly
root causes, since discovery is what fills those gaps. The statement doubles as a
communication tool that wins stakeholder buy-in for the exploration. The same
structure can be written as an opportunity statement, framing the same situation
as potential ("there's potential to make X faster and easier") rather than
deficit ("users struggle to do X").

[[2024-09-27_7-tips-discovery]] repeats the recommendation within a broader
discovery checklist: frame the problem with a clear statement so everyone
understands the scope and the team avoids researching the wrong things. Its
adjacent tactics are securing stakeholder buy-in early, agreeing roles and norms
collaboratively at kick-off, clustering and voting on which unknowns are most
important and risky, timeboxing discovery against the planning fallacy, involving
the whole team in research, and analysing and synthesising together — a session
that it says should produce How Might We questions.

### Writing the user need statement

[[2019-03-24_user-need-statements]] describes the artefact of design thinking's
define stage — also called a problem statement or point-of-view statement — that
summarises who the user is, what they need, and why the need matters to them. Its
core rule is to express needs as verbs (goals and end states) rather than nouns
(solutions): a user needs to accomplish an outcome, not a dropdown or a
dashboard, and naming components early constrains the solution space. Effective
statements come from qualitative research — interviews, field studies, diary
studies — not team assumptions, with the caveat that users do not always know
what they need even when they say they do. Beyond alignment, the statement
supplies success metrics and acts as a north star across the project. It should
not be confused with a development statement, which comes later and describes
implementation tasks.

### Turning the frame into a design challenge

[[2021-01-17_how-might-we-questions]] covers the technique introduced by Procter
& Gamble and adopted by IDEO, used at the end of discovery to frame the design
challenge and stop teams defaulting to pet solutions. Its criteria for a good
HMW question: ground it in actual research findings rather than generic
challenges; keep it solution-agnostic, since a question that embeds a solution
("tell users…") generates only ideas of that kind; keep it broad enough to admit
several approaches without losing the core problem; target the root problem
rather than the symptom — user confidence rather than stopping users from
calling; and use positive verbs (increase, create, enhance) rather than negative
ones (reduce, remove, prevent), which the source says produces more creative
ideas. Teams should write and select questions together, against a checklist.

### Framing a brief that arrives incomplete

[[2018-02-12_solving-design-exercises_06-chapter-2-how-to-solve-a-product-design-exercise]]
names the same pull as the sources above, in its own terms: designers think
visually and are tempted to jump straight to sketching, which it says leads to
building the wrong product for the audience. Its remedy is procedural. Clarify
expectations first — what the deliverable is, at what fidelity, in what format,
and whether it must be presented. Then ask clarifying questions about goal,
audience and needs rather than silently implementing what was handed over. Where
information is genuinely missing, state assumptions explicitly and back them with
reasoning instead of guessing; the source treats operating well with incomplete
information as a core skill in its own right. It also asks that the "why" behind
each decision stay available on demand, with both pros and cons ready — its
example being a chatbot that reduces friction but demands significant NLP
engineering and human support for edge cases.

The structure that carries this is 5W1H
[[2018-02-12_solving-design-exercises_07-answer-structure]]: Why (goal), Who
(audience), When and Where (context), What (product), How (measurement). Its use
is diagnostic — a brief typically answers Who, What and Why in part and usually
omits How, so the first move is to work out which of the six questions the brief
has already answered and which are still open. The same source notes that the
more a brief specifies, the more time is left for developing the solution.

Starting with Why is treated as more than sequencing.
[[2018-02-12_solving-design-exercises_09-step-1-understand-your-goal-why]] asks
for an opening that states why the product or feature matters: what problem it
solves, what impact it has, how it benefits customers and what business
opportunity it creates. For an improvement to an existing product it starts from
the company's vision and mission and explains how the improvement supports them.
It asks for both value propositions at once, customer and business — its NYC
MetroCard example pairing societal impact (less pollution, better access to
employment) with the business opportunity — and, when time allows, for the status
quo and its existing problems to be described before anything is proposed, on the
grounds that this makes the opportunity more compelling.

Narrowing is its own step when the brief is broad.
[[2018-02-12_solving-design-exercises_22-3-5-improving-the-atm-experience]] shows
a wide prompt ("improving the ATM experience") narrowed by two clarifying
questions, one on scope (rethink how people bank, or fix the machine as it is
today) and one on the specific type of machine (bank-owned, street or branch,
rather than third-party). Read the other way round,
[[2018-02-12_solving-design-exercises_24-chapter-5-tasks-list]] shows what a
well-specified brief carries: market size, user demographics, behavioural trends
and explicit technology constraints ("Every suggested technology has to be
available on the market today").

The frame reappears at the end.
[[2018-02-12_solving-design-exercises_16-how-to-present-your-solution]] asks a
presentation to open on the problem, the audience and the context so the solution
reads as a response to a specific, bounded challenge, and to state scope
explicitly: what the solution addresses, what it does not, and what would come
next given more time. For assumptions that are critical, it asks that the
validation route be proposed alongside them — quick user research, surveys or
testing services.

Where this sits against the research-grounded sources is worth naming.
[[2016-08-14_outcomes-vs-features]] asks for user data proving the problem exists
rather than a decision made on gut feel, and [[2019-03-24_user-need-statements]]
insists effective statements come from qualitative research rather than team
assumptions. Dashinsky's chapters work in a setting he describes as designing a
product in extremely limited time, and accept reasoned assumptions in place of
that research, with a validation plan attached
([[2018-02-12_solving-design-exercises_06-chapter-2-how-to-solve-a-product-design-exercise]],
[[2018-02-12_solving-design-exercises_16-how-to-present-your-solution]]). The two
are addressed to different situations, but they set a different bar for what a
frame must rest on.

### Framing at the level of the goal, not the feature

Three worked examples in the same book demonstrate the reframing move itself.
[[2018-02-12_solving-design-exercises_19-3-2-a-self-publishing-platform-for-amazon]]
asks not how to build a self-publishing tool but how to minimise entry barriers
for authors while increasing Amazon's marketplace supply, starting from the
business goal and working toward customer needs.
[[2018-02-12_solving-design-exercises_20-3-3-a-dashboard-for-freelancers]] asks
not what features a freelancer tool should have but how to help freelancers
understand their business health and know what action to take next, a frame
derived from the observation that administration diverts time from billable work;
it is then stated as three questions the product must answer — how the business
is doing financially, how to plan future work, and what can be done now to move
the business forward.
[[2018-02-12_solving-design-exercises_21-3-4-improving-primary-health-care]] asks
not what features a clinic needs but how one GP can serve more patients
effectively on preventable conditions, a reframing that produced group
appointments as a multiplier on the doctor's time rather than an incremental
improvement.

[[2018-02-12_solving-design-exercises_17-chapter-3-questions-and-answers]] gathers
five such tasks across consumer hardware, digital publishing, freelancer tools,
healthcare and infrastructure, and makes the point that there is no single right
solution: different people frame and solve the same brief differently and can all
do well, provided the process is structured and the reasoning is visible.

### The mindset that makes framing possible

[[2024-10-11_discovery-mindset]] identifies what defeats framing in practice:
starting with a solution in mind. Two biases follow — anchoring, where research is
interpreted through the lens of the preferred solution and the team tests it
rather than exploring the problem, and confirmation bias, where contradicting
evidence is ignored. Its three countermeasures: reframe the goal around a problem
rather than a solution (aim at "provide users with data to make good decisions"
rather than "identify how an AI chatbot can help"); surface assumptions and
unknowns explicitly at the start and prioritise them by importance and risk; and
"icebox" solution ideas by documenting them up front, then freezing them until
research is complete, which removes the anchor without losing the ideas. It
values openness to unknown unknowns, the unexpected findings that can change a
discovery's trajectory.

[[2018-02-12_solving-design-exercises_27-helen-tran-the-skill-most-designers-overlook]]
locates the same failure one step upstream, in the frame the designer is handed
rather than the one they invent. Tran's claim is that when designers are given a
target market they typically trust the people who gave them the directive, and
that those assumptions are usually wrong and steeped in someone else's biases;
a large part of the designer's job is therefore making sure the team is building
the right thing, which means double-checking the assumptions through thorough
research before anyone invests in a product nobody needs. Her named instruments
are user experience mapping, design sprints and in-depth market interviews, and
her test for whether the work has been done is whether the designer can explain
the bridge between business needs and user needs.

### Framing as the test for new technology

[[2025-03-28_ai-superpowers]] applies the principle to AI adoption: establish a
research-backed understanding of the user problem and the desired outcome first,
and only then ask whether generative AI is the right solution for that specific
problem. Its test question is behavioural — whether the technology makes the user
more likely to perform the behaviour that produces the desired outcome and
business impact. It names four areas where generative AI currently delivers
genuine value (content creation, summarisation, basic data analysis, perspective
taking) and warns that adopting AI without validating its relevance to user
outcomes yields useless features however sophisticated.

[[2025-05-09_ux-job-with-ai]] arrives at framing from the career angle, treating
UX methods as tools for building better products rather than ends in themselves,
and AI as the latest in twenty years of tool changes. Its claim about framing:
someone must define the problem clearly enough for AI to address it, ask the
right questions, judge whether the outputs are good, and decide which issues are
most critical. Specific method skills such as running a usability test may be
automated; understanding people, asking the right questions and analytical
judgement are what carry through.

## Sources (22)

- [[2016-08-14_outcomes-vs-features]] — Clear problem definition is the foundation of successful design; problems must be stated before solutions are proposed.
- [[2019-03-24_user-need-statements]] — The statement forces teams to articulate what they're solving before generating solutions, reducing wasted effort.
- [[2021-01-17_how-might-we-questions]] — explains how to frame design challenges based on research findings rather than assumptions, using How Might We questions.
- [[2021-08-22_problem-statements]] — Defining the problem is a critical first step before design work; problem statements articulate what needs to be solved, who is affected, and why it matters, creating focus for downstream research and design.
- [[2024-09-27_7-tips-discovery]] — the articulation of what needs to be solved, who is affected, and why it matters, forming the foundation for focused discovery research.
- [[2024-10-11_discovery-mindset]] — the process of defining and articulating the problem space before proposing solutions, ensuring research focuses on understanding the real problem rather than validating assumptions.
- [[2025-03-28_ai-superpowers]] — articulates the principle that design decisions should start with well-researched user problems and desired behaviors, using this to evaluate whether any technology (including AI) is appropriate.
- [[2025-05-09_ux-job-with-ai]] — highlights that identifying and framing problems remains human work that AI cannot yet do; AI execution still requires human problem definition.
- [[2018-02-12_solving-design-exercises_06-chapter-2-how-to-solve-a-product-design-exercise]] — Emphasizes that clarifying the task, asking questions, and making explicit assumptions are how designers properly frame problems before attempting solutions.
- [[2018-02-12_solving-design-exercises_07-answer-structure]] — the 5W1H technique helps frame the problem by answering structured questions about why, who, when/where, and what, with measurement as the final component.
- [[2018-02-12_solving-design-exercises_09-step-1-understand-your-goal-why]] — the chapter emphasizes articulating the problem clearly and the impact the solution creates, which is foundational to problem framing
- [[2018-02-12_solving-design-exercises_16-how-to-present-your-solution]] — Clearly stating the problem, target audience, and context at the start of a presentation ensures the solution is understood as a response to a specific, bounded challenge.
- [[2018-02-12_solving-design-exercises_17-chapter-3-questions-and-answers]] — Each of the five example tasks represents a distinct problem domain; the framework's applicability across these contexts shows the importance of problem framing as a universal skill.
- [[2018-02-12_solving-design-exercises_19-3-2-a-self-publishing-platform-for-amazon]] — The author frames the problem not as "how to build a self-publishing tool" but as "how to minimize entry barriers for authors while increasing Amazon's marketplace supply," starting from business goal and working toward customer needs.
- [[2018-02-12_solving-design-exercises_20-3-3-a-dashboard-for-freelancers]] — Rather than asking "What features should a freelancer tool have?", the author frames the core problem as helping freelancers understand their business health and know what action to take next, derived from observing that administration is a burden that diverts time from billable work.
- [[2018-02-12_solving-design-exercises_21-3-4-improving-primary-health-care]] — Rather than asking "What features does a clinic need?", Dashinsky reframes the core problem as "How can we let one GP serve more patients effectively on preventable conditions?", leading to group appointments as a novel multiplier rather than incremental feature improvements.
- [[2018-02-12_solving-design-exercises_22-3-5-improving-the-atm-experience]] — Techniques for narrowing a broad problem statement (improve ATM experience) with two clarifying questions: rethink how people bank or fix the machine as it exists today, and which type of machine (bank-owned street or branch ATMs rather than third-party ones).
- [[2018-02-12_solving-design-exercises_24-chapter-5-tasks-list]] — Tasks demonstrate how to frame problems across diverse domains (fintech, healthcare, transportation, social, real estate) with contextual details like market size, user demographics, behavioral trends, and technology constraints.
- [[2018-02-12_solving-design-exercises_27-helen-tran-the-skill-most-designers-overlook]] — A designer's role includes ensuring the team is solving the right problem; this requires validating that assumptions about the target market and user needs are correct before building.
- [[2013-08-01_just-enough-research_02-chapter-1-enough-is-enough]] — The chapter uses the Segway example to argue that understanding context—how the system fits into existing conventions, infrastructure, and real needs—is essential before designing solutions.
- [[2013-08-01_just-enough-research_05-chapter-4-organizational-research]] — understanding organizational goals, incentives, and constraints shapes how the problem is framed; this chapter emphasizes surfacing the real goals versus stated goals and documenting success metrics.
- [[2013-08-01_just-enough-research_11-conclusion]] — framed as the foundational work of asking hard questions before design work begins; checking assumptions early prevents wasted time and resources; competitive advantage comes from asking the right questions about why products should exist and who they serve.
