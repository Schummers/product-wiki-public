---
type: concept
name: Design System
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Component Libraries"
  - "Design System Operations"
  - "Design Systems"
  - "UI Components"
---

# Design System

## Definition

A design system is a complete, living set of standards intended to manage design
at scale using reusable components and patterns [[2021-04-11_design-systems-101]]
[[2024-05-24_design-systems-vs-style-guides]]. It has two halves that the sources
insist on keeping together: the **repository** — style guides, component
libraries, pattern libraries, usually published as a website or shared platform —
and the **team** that maintains it [[2021-04-11_design-systems-101]]
[[2024-05-24_design-systems-vs-style-guides]]. Design systems are the parent
object; style guides, component libraries and pattern libraries are the children
[[2024-05-24_design-systems-vs-style-guides]]. Their earliest widely documented
form was the front-end style guide: a modular collection of every UI element in a
product, paired with the code snippets developers copy to implement it, born in
Agile and Lean environments and kept as a living digital asset rather than a
static PDF [[2016-03-27_front-end-style-guides]].

The sources are consistent that a design system is not primarily a visual
artefact. It is an efficiency and alignment mechanism: it gives teams a shared
language for UI elements so nobody argues about what a "dropdown" is
[[2021-04-11_design-systems-101]], it frees designers from re-tweaking basic
components so they can work on information architecture, workflows and journeys
[[2021-04-11_design-systems-101]], and it is the practical instrument through
which internal consistency — the fourth usability heuristic — is actually
maintained [[2021-01-10_consistency-and-standards]]. One source pushes the point
furthest, arguing the name "Design System" is reductive and that "Alignment
System" would better describe a product whose job is to unify design, tech,
product and marketing [[2024-05-14_328_Gouverner_un_Design_System_@KristinaGudim]];
another frames the goal the same way from the other end: "on ne fait pas un design
system, on répond à une problématique d'efficience et de qualité de vie"
[[2024-12-10_355_Les_5_astuces_Design_System_de_l_équipe_Figma]].

## Practice

### What the system contains

- **Style guides** document branding, typography, colour, tone of voice and
  design principles; a content style guide covers tone and grammar, a brand style
  guide covers logos and palettes, and a front-end style guide covers UI
  components and interaction patterns
  [[2021-04-11_design-systems-101]] [[2024-05-24_design-systems-vs-style-guides]].
- **Component libraries** catalogue individual UI elements with names,
  descriptions, attributes, states, code snippets and usage guidelines
  [[2021-04-11_design-systems-101]] [[2024-05-24_design-systems-vs-style-guides]].
  A front-end style guide should cover 25+ common elements — buttons, form
  fields, navigation, modals, icons, animations, chips — each with dos and don'ts
  [[2016-03-27_front-end-style-guides]], plus layout grids, spacing rules and
  component behaviour across screen sizes [[2016-03-27_front-end-style-guides]].
- **Pattern libraries** hold combinations of elements and layouts that address
  common workflows or page templates, which matters most where the information
  architecture is complex [[2021-04-11_design-systems-101]].
- **Design guidance sits in a hierarchy**: principles (value statements) on top,
  usability heuristics as research-backed assessment, design patterns as the
  concrete tactical solutions, team charters governing how the team works
  [[2025-04-18_design-guidance]].
- For an intranet redesign, the system to plan for includes brand, content, UI
  guidelines and a pattern library [[2020-05-30_user-centered-intranet-redesign-steps]].

### Component conventions the system encodes

Individual component records show what "standards" concretely means:

- **Cards** — group related information into a self-contained unit with a visual
  boundary (border, background, subtle shadow) that signals clickability; making
  the whole card clickable enlarges the touch target
  [[2016-11-06_cards-component]].
- **Checkboxes** — square (optionally rounded), never circular, with a checkmark
  for the selected state; clickable labels; vertical lists; positively worded
  labels. Deviating from the convention users already expect causes confusion
  [[2024-06-28_checkboxes-design-guidelines]].
- **Tabs** — in-page and navigation tabs must not be mixed; the selected tab needs
  at least two visual indicators; labels need information scent
  [[2024-08-02_tabs-used-right]].
- **Typography** — assign each typeface a distinct role, use weights rather than
  extra families for hierarchy, and record those patterns in the system so teams
  choose confidently [[2022-06-19_pairing-typefaces]].
- **Visual style** can itself be systematised: neobrutalism becomes workable when
  it is expressed as rules — a 2-3 colour high-contrast palette, generous 24-32px
  spacing, bold headline type paired with neutral body type, WCAG contrast
  minimums [[2025-04-11_neobrutalism]].
- A study guide organises the same material for visual design as a whole:
  principles, elements, accessibility, testing, and design systems as the layer
  that scales all of it across products and teams
  [[2022-11-06_visual-design-in-ux-study-guide]].

### Semantics and naming

Several sources converge on naming components and tokens by **function rather
than appearance**:

- Name tokens for their role ("background accent", "headline") instead of their
  look ("light blue", "bold XL"), and extend the same semantics to components and
  variants ("primary" button, "success message" rather than "pop-up"). This
  prevents "Frankenstein" components that try to answer too many discordant needs
  [[2024-11-19_352_Design_system_sémantique_Scaler_un_DS_efficacement]]. The stated
  aim is deliberate constraint: "On vient créer de la contrainte dans le design
  system pour créer de la consistance."
- Semantic naming is also used defensively: calling a component "confirmation
  dialog" rather than "modal" signals the narrow context it was designed for and
  discourages overuse [[2024-09-24_347_Fenêtre_modale,_le_Guide_UX_Design]].
- Figma's own system is named a *Pattern Library* rather than a component library,
  precisely to frame each entry as a semantic answer to a usage problem instead of
  a visual brick [[2024-12-10_355_Les_5_astuces_Design_System_de_l_équipe_Figma]].
- Agreeing on component definitions, nomenclature and architecture with every
  stakeholder should happen **before** production starts
  [[2024-05-14_328_Gouverner_un_Design_System_@KristinaGudim]].

### Structuring components in the tool

- Separate **state properties** (focus, dictated by the end user) from **context
  properties** (with icon, dictated by the designer), so designers are not
  manipulating irrelevant controls
  [[2024-12-10_355_Les_5_astuces_Design_System_de_l_équipe_Figma]].
- Do not chase a perfect one-to-one mapping between Figma properties and code
  properties: the constraints and the users differ, and forcing alignment is often
  counterproductive [[2024-12-10_355_Les_5_astuces_Design_System_de_l_équipe_Figma]].
  A later source pulls the other way on the same question, recommending alignment
  with the engineering team so components stay identical between design and code,
  since a Figma slot maps closely onto the `children` notion in React or Vue
  [[2026-03-24_406_Figma_Slots_-_Le_guide_Design_System]] — the two sources
  disagree on how tightly design and code structures should mirror each other.
- Use **modes** to let a single component adapt automatically to the right visual
  identity across sibling products (Figma, FigJam, Slides)
  [[2024-12-10_355_Les_5_astuces_Design_System_de_l_équipe_Figma]].
- **Slots** replace the old placeholder-component workaround, which produced
  unmaintainable technical debt; they suit structural components (modals,
  sidebars) and listing components (tables, lists). Their dimensions and
  auto-layout rule are fixed at creation, so configure rigorously, name slots
  clearly, recommend components, and pre-fill default content. Multiplying slots
  in one component erodes the constraint the system exists to provide
  [[2026-03-24_406_Figma_Slots_-_Le_guide_Design_System]].

### Governance, enforcement and adoption

- Governance, organisation and collaborative workshops are the first pillar of
  success — before operational production
  [[2024-05-14_328_Gouverner_un_Design_System_@KristinaGudim]].
- Design systems fail without active enforcement. Small deviations compound: one
  team customises a carousel, another adjusts a button, and dozens of variations
  emerge that confuse customers and break maintainability
  [[2026-02-06_design-system-enforcer]]. The enforcer role is stewardship, not
  refusal — ensuring adoption, rolling innovations back into the system, and
  facilitating compromises — and it depends on executive backing and engineering
  support to be more than a suggestion [[2026-02-06_design-system-enforcer]].
- A working decision rule: if three or more teams need a change, it belongs in the
  system; if one team needs it, it is an exception; prototype first when uncertain
  [[2026-02-06_design-system-enforcer]].
- Flexibility beats purity: "A perfect system that nobody uses is worthless. A
  slightly messier system that solves real problems is valuable"
  [[2026-02-06_design-system-enforcer]].
- Measure adoption through the satisfaction of internal users — KPIs, monthly
  surveys, Figma usage statistics
  [[2024-05-14_328_Gouverner_un_Design_System_@KristinaGudim]].
- **Rationalise rather than accumulate**: a large component count harms
  maintainability; keep only what is genuinely and frequently used, and prune
  obsolete or draft elements — "Dans un design system, la seule chose qui doit
  exister, c'est ce qui est réellement utilisé"
  [[2024-05-14_328_Gouverner_un_Design_System_@KristinaGudim]].
- Match the system's complexity to the size of the company: a young startup should
  not copy the extremely complex systems of large tech organisations
  [[2024-11-19_352_Design_system_sémantique_Scaler_un_DS_efficacement]].
- Documentation is an onboarding and training tool, not a technical dump; it
  should gather the needs of several disciplines and be made digestible with UX
  writing [[2024-05-14_328_Gouverner_un_Design_System_@KristinaGudim]].

### The team behind it

- Design-system teams are typically 2-5 people even at organisations with
  thousands of employees, and this is a deliberate operating model rather than
  pure under-resourcing: shared context removes handoff delays, blurred roles let
  designers contribute to API design and developers critique designs, and
  constrained capacity forces explicit prioritisation
  [[2026-05-15_lean-design-system-teams]].
- Small is only an advantage when paired with executive buy-in, defined scope and
  realistic expectations; otherwise it is "small by default" — underinvestment
  disguised as scrappiness, producing burnout and maintenance debt
  [[2026-05-15_lean-design-system-teams]].
- Scale the system without scaling the team by shifting from producer to enabler:
  champion programmes and contributor models distribute the work
  [[2026-05-15_lean-design-system-teams]].
- Systems are built by interaction designers, visual designers and developers, and
  ideally researchers and architects [[2021-04-11_design-systems-101]]. At the top
  of the UX-maturity model, the system is owned by a specialised team that
  continuously iterates [[2022-01-02_ux-maturity-stage-6]].

### Maturity and organisational context

- Design systems start taking shape and gaining traction with development and
  business partners at UX-maturity stage 4, while inconsistencies still exist
  [[2021-11-21_ux-maturity-stage-4]]; at stage 6 a well-vetted, continuously
  iterated system ensures consistent, high-quality output at scale
  [[2022-01-02_ux-maturity-stage-6]].
- Maturity is better read as six independent dimensions — organisational
  alignment, team effectiveness, infrastructure robustness, governance, support
  and adoption — than as a linear climb. Systems regress when organisations
  restructure or budgets are cut, and a 10-person startup and a 10,000-person
  enterprise can both be mature under different conditions
  [[2026-07-10_design-system-maturity]]. This directly contradicts the sequential
  framing implied by placing design systems at particular UX-maturity stages
  [[2021-11-21_ux-maturity-stage-4]] [[2022-01-02_ux-maturity-stage-6]].
- Plot the six scores on a hexagonal radar chart: symmetry means even development,
  valleys mean structural constraints, spikes may mean uneven investment; a small
  balanced shape is often more stable than a large uneven one. Assess as a team,
  quarterly or after organisational shifts, and compare against a kept baseline
  [[2026-07-10_design-system-maturity]].
- One source frames the system as a mirror of the organisation itself — "le
  miroir d'une organisation. C'est la voix des équipes" — with the ideal system
  being one that liberates teams and gives them autonomy
  [[2024-05-14_328_Gouverner_un_Design_System_@KristinaGudim]].

### Consistency, and its limits as an advantage

- Design systems, design reviews and consistency audits are what make internal
  consistency survive contact with designers who interpret standards differently:
  "Consistency doesn't happen by itself, but requires an active process"
  [[2021-01-10_consistency-and-standards]].
- Consistency pays for customers (transferable learning, lower cognitive load) and
  for engineers (maintainability) [[2026-02-06_design-system-enforcer]]
  [[2021-01-10_consistency-and-standards]].
- But standardisation has made UI itself less of a differentiator: as design
  systems mature, competitive advantage moves to research-informed understanding,
  judgment and strategic problem-solving, while enforcement and governance remain
  critical [[2026-01-16_state-of-ux-2026]]. The same shift is described from the
  practitioner's side: component assembly removed much of the pure UI role and
  pushed designers toward product design, delivery and business concerns
  [[2025-09-16_395_L_UX_Design_est_mort_L_impact_de_l_IA_&_du_business_sur_le_métier_de_designer]]
  [[2025-04-22_374_La_fin_du_Product_Design_Se_réinventer_pour_2026]].

### Effects on the design process

- Ready-made component libraries make it fast enough to go straight to
  high-fidelity, which is part of the argument that wireframing in Figma is now an
  uncomfortable in-between: use very low fidelity (paper sketching) for personal
  thinking and very high fidelity for sharing and testing
  [[2025-01-21_361_Top_3_outils_lo-fi_pour_remplacer_les_wireframes]].
- A design system is the enabling tool for intent-driven, dynamically assembled
  layouts: interfaces have to be conceived as modular blocks rather than fixed
  pages, and the system is what makes those variations coherent and cheap to
  implement [[2025-02-11_364_Intent_Driven_Design,_la_méthode_pour_une_UX_moderne_à_l_heure_de_l_IA]].
- Reuse compounds at product level: the Figma Pattern Library let the team build
  Figma Slides quickly while staying visually coherent with the rest of the suite
  [[2024-12-24_357_Figma_Slides,_une_leçon_de_Product_Market_Fit_-_Podcast_Product_Design]].
- Front-end style guides cut design-specification time and enforce consistency by
  making it less work to do the right thing than to invent something inconsistent
  [[2016-03-27_front-end-style-guides]].

### Design systems and AI tooling

- The missing integration with design systems is named as a critical gap in
  AI design tools: designers work with established systems, and prototypes built
  from random design elements provide no value; prompt-length limits compound the
  problem by making it impossible to convey enough context
  [[2025-05-09_ai-design-tools-update-2]]. AI code generators are described as
  still struggling to exploit an existing system's components
  [[2025-06-03_380_Figma_est_mort_les_nouveaux_outils_de_mon_process_de_design]],
  where the recommendation is to accept that and treat generated prototypes as
  disposable UX artefacts rather than pixel-perfect, system-compliant output.
- The counter-direction is to make the system machine-readable. Google Labs'
  DESIGN.md holds exact values (colours, type sizes, spacing) alongside
  human-readable guidelines, lives next to the code, and is read by AI tools every
  time they generate something [[2026-07-24_ux-context-design]]. Since product
  managers and engineers now generate designs before a designer sees them, the
  practical goal is that everything AI generates is informed by research and
  design standards, with context continuously curated rather than handed off
  [[2026-07-24_ux-context-design]].
- Bridge, an open-source knowledge base, lets Claude Code understand a Figma
  design system and generate conforming UI from a text specification; its "Learn"
  workflow feeds the designer's manual corrections back so the same mistakes are
  not repeated. Non-designers can then produce system-compliant screens, with the
  designer acting as reviewer rather than executor
  [[2026-04-21_410_Figma_x_Claude_Code_Les_outils_design_de_Noé_Chagué]].
- Claude Design is credited with integrating or creating a genuine code-based
  design system — structural, reusable components rather than a graphic palette —
  though it is reported as slow, credit-hungry, and prone to cluttered output with
  alignment and hierarchy defects
  [[2026-06-02_416_J_ai_testé_Claude_Design_-_Avis_&_impact_sur_le_métier_de_Designer]].

### Cautions

- Design systems are not one-and-done; they demand sustained investment in
  creation and maintenance, ongoing user education, and organisational commitment
  [[2021-04-11_design-systems-101]] [[2024-05-24_design-systems-vs-style-guides]].
- Do not build for the beauty of the structure or the code: the point is to
  accelerate value creation and improve quality of life for end users and creators
  [[2024-12-10_355_Les_5_astuces_Design_System_de_l_équipe_Figma]].
- Too much freedom is as dangerous as too little: over-permissive slots can make a
  system "perdre un petit peu son intérêt"
  [[2026-03-24_406_Figma_Slots_-_Le_guide_Design_System]], and a system without
  enforcement becomes "a Frankenstein's monster of competing patterns"
  [[2026-02-06_design-system-enforcer]].

## Sources (33)

- [[2016-03-27_front-end-style-guides]] — The article establishes front-end style guides as practical implementations of design systems in product development, enabling modular consistency.
- [[2016-11-06_cards-component]] — Cards combine visual design elements (borders, background color, shadows) with interaction affordances (clickability) to create usable, grouped content containers.
- [[2020-05-30_user-centered-intranet-redesign-steps]] — recommends planning design systems that include brand, content, UI guidelines, and pattern libraries to promote consistency and efficiency.
- [[2021-01-10_consistency-and-standards]] — discusses how design systems help teams maintain internal consistency across products and families of applications.
- [[2021-04-11_design-systems-101]] — Design systems provide comprehensive frameworks encompassing component libraries, documentation, and ongoing maintenance practices that establish their value and structure.
- [[2021-11-21_ux-maturity-stage-4]] — Design systems begin to take shape and gain organizational adoption, supporting consistency and efficiency.
- [[2022-01-02_ux-maturity-stage-6]] — Well-vetted, continuously iterated design systems owned by specialized teams ensure high-quality, consistent output at scale across stage-6 organizations.
- [[2022-06-19_pairing-typefaces]] — Establishing typeface patterns and roles as part of design systems ensures consistency and helps teams make confident typographic choices.
- [[2022-11-06_visual-design-in-ux-study-guide]] — design systems scale visual consistency across products and teams; they codify principles, elements, and standards to maintain coherence and efficiency.
- [[2024-05-14_328_Gouverner_un_Design_System_@KristinaGudim]]
- [[2024-05-24_design-systems-vs-style-guides]] — A comprehensive approach to managing design at scale through collections of reusable components and patterns (buttons, inputs, cards) with standardized guidelines, design specifications, and implementation code that enable consistent and efficient design and development across products and teams.
- [[2024-06-28_checkboxes-design-guidelines]] — checkboxes are standard UI components with established conventions (squares with checkmarks) that users expect; deviating from these conventions causes confusion.
- [[2024-08-02_tabs-used-right]] — covers the anatomy, best practices, and accessibility requirements for tab controls.
- [[2024-09-24_347_Fenêtre_modale,_le_Guide_UX_Design]]
- [[2024-11-19_352_Design_system_sémantique_Scaler_un_DS_efficacement]]
- [[2024-12-10_355_Les_5_astuces_Design_System_de_l_équipe_Figma]]
- [[2024-12-24_357_Figma_Slides,_une_leçon_de_Product_Market_Fit_-_Podcast_Product_Design]]
- [[2025-01-21_361_Top_3_outils_lo-fi_pour_remplacer_les_wireframes]]
- [[2025-02-11_364_Intent_Driven_Design,_la_méthode_pour_une_UX_moderne_à_l_heure_de_l_IA]]
- [[2025-04-11_neobrutalism]] — describes how neobrutalist principles can be systematized through consistent color palette limits (2-3 colors), spacing conventions (generous padding), and hierarchy rules.
- [[2025-04-18_design-guidance]] — framework for organizing and applying design guidance including principles, patterns, and documentation to maintain consistency.
- [[2025-04-22_374_La_fin_du_Product_Design_Se_réinventer_pour_2026]]
- [[2025-05-09_ai-design-tools-update-2]] — highlights absence of design-system integration as critical gap preventing AI tools from supporting real design workflows.
- [[2025-06-03_380_Figma_est_mort_les_nouveaux_outils_de_mon_process_de_design]]
- [[2025-09-16_395_L_UX_Design_est_mort_L_impact_de_l_IA_&_du_business_sur_le_métier_de_designer]]
- [[2026-01-16_state-of-ux-2026]] — Standardization and design systems have made UI consistent and efficient but less of a differentiator; enforcement and governance remain critical.
- [[2026-02-06_design-system-enforcer]] — Effective design systems require active enforcement, not just documentation; enforcement ensures consistency and prevents a "Frankenstein's monster of competing patterns."
- [[2026-03-24_406_Figma_Slots_-_Le_guide_Design_System]]
- [[2026-04-21_410_Figma_x_Claude_Code_Les_outils_design_de_Noé_Chagué]]
- [[2026-05-15_lean-design-system-teams]] — Lean design-system teams operate effectively when they have clear scope, executive sponsorship, and realistic expectations; small size enables speed and cohesion but requires organizational support to be sustainable.
- [[2026-06-02_416_J_ai_testé_Claude_Design_-_Avis_&_impact_sur_le_métier_de_Designer]]
- [[2026-07-10_design-system-maturity]] — mature across multiple dimensions that work independently, requiring regular assessment and balanced development to remain coherent and useful.
- [[2026-07-24_ux-context-design]] — can include machine-readable standards (like DESIGN.md) that AI tools read every time they generate output, ensuring consistency and standards compliance.
