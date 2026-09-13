---
type: concept
name: Wireframing
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Idéation sur papier"
  - "Wireframing - Idéation sur papier"
  - "Wireframing / Idéation sur papier"
---

# Wireframing

## Definition

Wireframing is the practice of visualising a user path or flow, page layout,
information hierarchy and even interactions, at fidelity levels ranging from a
quick sketch to a detailed design
([[2021-06-20_draw-wireframe-even-if-you-cant-draw]]). Its output is a
structural artefact, not a finished screen: Anna Dahlström calls wireframes
screenplays rather than products, whose job is to say what content goes where,
in what order and why, without dictating colours or styling
([[2019-12-17_storytelling-in-design_14-chapter-13-applying-scene-structure-to-wireframes-designs]]).

The sources do not agree on whether the artefact is still worth producing.
Nielsen Norman Group treats it as a normal early-design step that anyone can
perform ([[2021-06-20_draw-wireframe-even-if-you-cant-draw]]) and as a base that
newer deliverables extend ([[2024-05-17_promptframes]]). Romain Penchenat argues
the opposite in [[2025-01-21_361_Top_3_outils_lo-fi_pour_remplacer_les_wireframes]]:
"L'ère des wireframes est terminée." His objection is not to low fidelity but to
the uncomfortable middle ground of grey-box mockups built in a design tool,
which in his view constrains creativity while making a poor communication
support.

## Practice

### Drawing one does not require drawing skill

Kelley Gordon ([[2021-06-20_draw-wireframe-even-if-you-cant-draw]]) gives a
four-step sequence: identify the browser or device aspect ratio (1024x768 for
web, device-specific for mobile), draw the navigation and search, draw the
largest elements (headers, images, body text), then fill in the remaining
details (buttons, dropdowns, checkboxes). Working from the largest elements
down prevents getting lost in detail. What replaces artistic ability is a
vocabulary of conventions:

- Headers as thick lines, body text as thin lines.
- Images and icons as a rectangle with an X; icons may also be coarse line art.
- Navigation as horizontal or vertical rectangles; hidden navigation shown
  expanded or closed; active links underlined or boxed.
- Search as an icon with a field and an optional suggestion box.
- Dropdowns as a rectangle plus a caret, open or closed; checkboxes as squares
  with check marks; radio buttons as circles, filled when selected — selection
  state should be unambiguous.
- Text labels on calls to action, so reviewers get the key detail; less
  critical for secondary buttons.

### Messy is the point

The same record insists that low-fidelity wireframes should be rough and quick,
and that perfection is counterproductive. It recommends deliberate physical
constraints — thick pens, time-boxing, limited space — to make overpolishing
impossible. Messy wireframes also steer reviewers towards feedback on the
concept rather than on aesthetics
([[2021-06-20_draw-wireframe-even-if-you-cant-draw]]). See [[Sketching]].

### Start on paper, away from the tool

Penchenat makes the same move for a different reason. In
[[2024-09-17_346_Le_meilleur_hack_productivité_pour_les_designers]] he
recommends starting a project on paper or a whiteboard to stay focused on the
experience and how it works before touching the interface software. In
[[2025-01-21_361_Top_3_outils_lo-fi_pour_remplacer_les_wireframes]] he sharpens
it: thinking inside [[Figma]] pushes you to design according to the software's
limits rather than the real user experience, and complex shapes that are painful
to build in a tool are trivial on paper.

### Penchenat's three replacements

Rather than wireframes, [[2025-01-21_361_Top_3_outils_lo-fi_pour_remplacer_les_wireframes]]
prescribes very low fidelity for personal thinking and very high fidelity for
internal sharing and client feedback, with design systems making the jump to
high-fidelity prototypes fast. The three lo-fi tools he names are paper
[[Sketching]] (including [[Crazy Eights]], eight ideas or screens in eight
minutes), advanced [[User Flow]] charts enriched with the content hierarchy each
step requires, and [[Object-Oriented UX]], which structures the application
around its objects, their relationships and their actions before any interface
is drawn.

### Wireframes as the story of a page

Dahlström
([[2019-12-17_storytelling-in-design_14-chapter-13-applying-scene-structure-to-wireframes-designs]])
treats each page as a scene with three acts: an opening above the fold, a middle
carrying the content and its conflict, and a closing below the fold that ends
strongly and links to the next scene. Before sketching or wireframing, define in
one or two sentences why the page exists — the practice she takes from Jerry
Jenkins's blog on writing scenes — and if you cannot articulate that purpose,
either clarify it or scrap the page. She adds several checks a wireframe should
answer: what a first-time user versus a returning user must be able to do, a
desired time-on-page as a coherence checkpoint, and how modules reflow across
breakpoints (content that does not need to be on mobile probably does not belong
on desktop either). A related test she proposes: if the wireframe still tells a
story once styling is stripped away, the hierarchy is sound; if not, visual
design is compensating for unclear structure ([[Visual Hierarchy]],
[[Scene Structure]]).

### Add content fidelity before high-fidelity design

[[2024-05-17_promptframes]] (Evan Sunwall, Nielsen Norman Group) proposes an
extra stage between wireframes and prototypes: a promptframe, "a design
deliverable that documents content goals and requirements for generative-AI
prompts based on a wireframe's layout and functionality." The problem it
targets is placeholder content such as lorem ipsum, which prevents meaningful
user feedback — "The content inspires feedback, not the container." Different
content types (copy, images, data visualisations) each need their own prompt
parameters for tone, style, dimensions and constraints, and the AI tool should
be given personas, brand voice, organisation mission and visual principles.
The record is explicit that this accelerates feedback cycles without replacing
the human craft needed for production-ready content. See [[Prototyping]].

## Sources (5)

- [[2021-06-20_draw-wireframe-even-if-you-cant-draw]] — Visualization technique for exploring design solutions through user paths, layouts, hierarchy, and interactions at varying fidelities.
- [[2024-05-17_promptframes]] — promptframes extend traditional wireframing by adding a new stage that bridges wireframes and prototypes, focusing on content fidelity before detailed design.
- [[2024-09-17_346_Le_meilleur_hack_productivité_pour_les_designers]]
- [[2025-01-21_361_Top_3_outils_lo-fi_pour_remplacer_les_wireframes]]
- [[2019-12-17_storytelling-in-design_14-chapter-13-applying-scene-structure-to-wireframes-designs]] — Wireframes are screenplays, not finished products. They communicate hierarchy, content placement, and intended length to designers, developers, and stakeholders—not prescriptive visual layouts. A good wireframe answers: what content goes where, in what order, and why, without dictating colors or styling.
