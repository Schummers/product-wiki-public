---
type: concept
name: Productivity
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Interface Patterns for Productivity"
  - "Productivité"
---

# Productivity

## Definition

Productivity appears in these sources in two distinct senses that should not be
collapsed. The first is the productivity of the person doing the work: how much
of value a designer or a team ships, and what shifts it.
[[2023-09-05_path-to-senior-product-designer_11-9-growing-your-impact]] (Artiom
Dashinsky) treats it as a function of leverage rather than hours, while
[[2025-02-04_363_Top_4_des_outils_de_productivité_pour_designers]] (Romain
Penchenat) frames it as removing friction and mental load rather than as an end
in itself: "Être productif, c'est effacer la friction pour se concentrer sur la
création de valeurs concrètes."

The second sense is productivity as something an interface either protects or
destroys for its users. [[2025-05-23_serial-task-switching]] (Megan Chan,
Nielsen Norman Group) reports that true multitasking is cognitively impossible
when tasks draw on similar cognitive resources; what users actually do is switch
serially between tasks, and despite feeling productive they complete fewer tasks
and produce lower-quality work than those keeping focus. Here productivity is a
design outcome, and the interface is one of the variables.

## Practice

### Leverage over hours

[[2023-09-05_path-to-senior-product-designer_11-9-growing-your-impact]] argues
that improving productivity is not about working longer but about shifting
toward higher-return activities. Dashinsky cites Dropbox for the components of
seniority: consistency (how often you make an impact), velocity (how large it
is) and accountability. His three-step method is to define what an activity
impacts (product, work or people), identify its current level of impact, then
upgrade it to a higher level. The chapter also borrows kaizen: improving by one
percent per week compounds, in his figures, to a 170% improvement over two
years, so the gain comes from consistency rather than dramatic change. On
learning, it recommends reading selectively by topic rather than cover to cover,
preferring multi-idea books over single-idea ones, using podcasts for niche
knowledge and to research companies, and applying what is learned immediately.

### Protecting the conditions to ship

[[2023-09-05_path-to-senior-product-designer_17-15-shipping-ownership]] is the
tactical counterpart. Dashinsky recommends a time audit: map how your time is
actually allocated across designing, meetings, learning and mentoring, compare
it to your ideal allocation, and treat recurring meetings as the high-leverage
target for reclaiming time without reducing output. Makers, he writes, need
half-day blocks to make significant progress, unlike managers who work in
one-hour slots, so scheduling meetings at the beginning or the end of a work
sprint preserves unbroken time. He advises finding when you are personally most
productive, protecting those hours for challenging work, leaving routine tasks
for low-productivity hours, and experimenting with intervals such as
ninety-minute sprints followed by rest. The chapter cites a study by John
Pencavel of Stanford University reporting that productivity falls sharply above
50 work hours and that any hour worked above 55 does not contribute at all.
Shipping also depends on stopping: a design is often good enough to ship before
its designer is satisfied. Tracking time on projects, including revisions,
meetings and feedback cycles, is presented as the most accurate basis for
estimating future work.

### Fixing the process, not just your own habits

[[2023-09-05_path-to-senior-product-designer_12-10-tools-and-processes-craft]]
moves the question from the individual to the team. Its four-step framework:
check whether the process is already documented and volunteer to create or
update it if not, map it by listing steps, collaborators and tools, find
inefficiencies through your own observation and through team feedback, then
solve them with tools, documentation, design systems or policy. For feedback,
the chapter suggests asking colleagues specifically about frustrations, tool
pain points, repetitive tasks, bottlenecks, and what they would change with a
magic wand, then using an impact/effort matrix to decide which inefficiencies to
tackle first. Its worked example is automating a repetitive asset export in
Photoshop, which took the task from up to one minute per asset down to a few
seconds, a gain that multiplies across a team.

Note the tension with the previous section: the same book argues both for
optimising your personal rhythms and for the claim that identifying process
problems has more leverage than executing well within them.

### Tooling

[[2025-02-04_363_Top_4_des_outils_de_productivité_pour_designers]] is the one
source here that names concrete tools, and it deliberately excludes AI. Romain
Penchenat presents Alfred as an omnipresent command bar on Mac for launching
applications, running web searches and reaching clipboard history or text
snippets; Shortcutter as a mobile app teaching one new keyboard shortcut a day
for tools such as Figma or Notion; Feedly as an RSS aggregator that centralises
quality sources and bounds the time spent on design watching, as an alternative
to scrolling social networks; and Rectangle as an open-source Mac tool for
arranging and resizing windows by keyboard shortcut, including moving them
between screens. His framing is that the point is not productivity for its own
sake but removing what costs time unnecessarily.

### Designing for users who switch tasks

[[2025-05-23_serial-task-switching]] treats productivity as an interface
problem. Because switching fragments the cognitive resources available to each
task, it increases errors in both activities and accumulates stress on working
memory. The article's recommendation is to accommodate the behaviour rather than
ignore it: multi-view interfaces (split screens, picture-in-picture, resizable
panels) keep several tasks visible and lower the cost of switching; parallel
task execution lets background work continue without blocking focus; focus
features such as Do Not Disturb modes support users who choose to give one task
their full attention; and orientation cues plus robust error recovery help
people re-enter an interrupted task. Chan suggests evaluating your own product
with task switching in mind to find where that friction sits.

## Sources (5)

- [[2025-02-04_363_Top_4_des_outils_de_productivité_pour_designers]]
- [[2025-05-23_serial-task-switching]] — design solutions like multi-view layouts, focus modes, and parallel execution that reduce the costs of serial task switching.
- [[2023-09-05_path-to-senior-product-designer_11-9-growing-your-impact]] — Improving productivity (and thus consistency and velocity) is not about working longer hours but about shifting toward higher-leverage activities through the three-step redesign framework.
- [[2023-09-05_path-to-senior-product-designer_12-10-tools-and-processes-craft]] — Optimizing processes and workflows directly improves team productivity; the chapter demonstrates how small improvements (like automating exports) can multiply efficiency across a team.
- [[2023-09-05_path-to-senior-product-designer_17-15-shipping-ownership]] — deliberately optimizing when and how you work by protecting peak hours, removing distractions, using work intervals that match your biology, and declining interruptions.
