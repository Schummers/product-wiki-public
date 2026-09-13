---
type: concept
name: Prototyping
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Low-Fidelity Prototypes"
  - "Paper Prototyping"
  - "Prototypage"
  - "Prototype"
---

# Prototyping

## Definition

A prototype is a hypothesis: a candidate design solution that must be tested
with real users [[2016-12-18_ux-prototype-hi-lo-fidelity]]. Its economic
argument is blunt — ripping up code is very expensive, ripping up a prototype is
not, especially when it is a piece of paper — which is why testing final
products is described as uninformed and risky
[[2016-12-18_ux-prototype-hi-lo-fidelity]]. Prototypes vary independently along
several dimensions (single-page or multipage, hand-sketched or realistic,
interactive or static), so fidelity is not one slider but several
[[2016-12-18_ux-prototype-hi-lo-fidelity]].

The French corpus frames the same idea as de-risking a precise hypothesis: a
good prototype answers your doubts and questions, it is not a beautiful Figma
file made to close a design phase [[2026-02-17_401_Prototypage_Le_guide_design_complet_-_Figma,_Lovable,_Google_Sheets_et_+]]. Three current purposes are named —
testing with users, anticipating edge cases inside the product team, and, more
recently, assessing technical feasibility, especially for AI-based features
[[2025-02-18_365_Replit,_l’outil_de_prototypage_design_ultime]]. In practice, prototyping spans paper cutouts
[[2021-12-19_paper-prototyping-cutout-kit]], human-operated Wizard of Oz setups
[[2024-04-19_wizard-of-oz]], AI-populated content
[[2024-05-17_promptframes]], and AI-generated code
[[2025-10-24_ai-prototyping]].

## Practice

### Start from the hypothesis, not the tool

- Define the hypothesis to challenge before creating anything; the prototype
  exists to de-risk one specific element — a problem, a solution, or interaction
  details [[2026-02-17_401_Prototypage_Le_guide_design_complet_-_Figma,_Lovable,_Google_Sheets_et_+]].
- Match the artefact to the question. Figma suits high-fidelity prototypes
  validating usability and detailed flows; for data-heavy interfaces
  (dashboards, analysis tools) content matters more than visuals, so real data
  in a Google Sheet or an AI tool like Lovable checks whether the information
  presented is actually relevant; and in exploratory phases, static screens or a
  slide deck with deliberately opposed concepts provoke reaction and debate
  without any interactivity [[2026-02-17_401_Prototypage_Le_guide_design_complet_-_Figma,_Lovable,_Google_Sheets_et_+]].
- Classic tools have known ceilings: Figma works for simple flows but not for
  real data or AI, Protopie excels at micro-interactions but not real data, and
  hand-written code costs too much time and skill [[2025-02-18_365_Replit,_l’outil_de_prototypage_design_ultime]].
- When testing usability in Figma, turn off click hints and test on the right
  device (mobile where relevant) so results are not biased [[2026-02-17_401_Prototypage_Le_guide_design_complet_-_Figma,_Lovable,_Google_Sheets_et_+]].

### Prototyping to learn before building software

[[2014-09-05_user-story-mapping_08-3-plan-to-learn-faster]] follows a product
owner, Eric, using prototypes as the step between validating that a problem
exists and committing to production software: high-fidelity prototypes in
tools such as Axure or PowerPoint let the team envision a solution and test it
with users while surprises are still cheap, before any code is written. Patton
treats this explicitly as a stage of validated learning rather than a step
toward a finished spec — each release afterward is run as an experiment, and
the prototype's job is only to filter out ideas that would not work.
[[2014-09-05_user-story-mapping_20-15-using-discovery-for-validated-learning]]
narrows the fidelity choice further inside that same discovery discipline:
simple, low-fidelity prototypes — paper, comics, minimal code — are what teams
use to think through solutions and reject bad ones before building anything
scalable, because in Patton's design-thinking and lean-startup synthesis a
prototype is one step in the empathize–define–ideate–prototype–test cycle, and
its purpose is speed of learning, not fidelity for its own sake. This lines up
with [[2016-12-18_ux-prototype-hi-lo-fidelity]]'s point that low-fidelity work
is faster to prepare and easier to discard, though Patton's framing goes
further: for him, a minimum viable product is itself "the smallest possible
experiment" needed to validate a risky assumption, which can be a prototype
rather than working code at all.

### Choosing fidelity

- High-fidelity prototypes give realistic system response, remove delays, cut
  human error, and let the facilitator observe rather than operate the
  prototype; they support testing specific UI components, graphical affordances,
  page hierarchy and engagement, and look real enough to elicit realistic
  behaviour [[2016-12-18_ux-prototype-hi-lo-fidelity]]. They are also what
  effectively tests visual design and aesthetic appeal before development
  [[2018-08-26_case-study-iterative-design-prototyping]].
- Low-fidelity prototypes need less preparation, allow changes between sessions,
  and reduce the pressure on participants who feel less obliged to succeed with
  an obviously unfinished interface [[2016-12-18_ux-prototype-hi-lo-fidelity]].
  They also reduce designer attachment: sketchy work is easier to throw away
  than polished work [[2016-12-18_ux-prototype-hi-lo-fidelity]].
- Choose the level per dimension based on project goals, timeline, and what
  specifically needs testing — a prototype can be high-fidelity in interactivity
  and low in visuals, or the reverse [[2016-12-18_ux-prototype-hi-lo-fidelity]].
- Keep fidelity consistent across screens: mixing high- and low-fidelity screens
  makes participants over-focus on the detailed ones and give poor feedback on
  the rest [[2021-12-19_paper-prototyping-cutout-kit]].
- For technical prototypes, deliberately drop visual style and brand guidelines:
  a fully functional flow with the right components and behaviours but no brand
  styling is better than the opposite [[2025-02-18_365_Replit,_l’outil_de_prototypage_design_ultime]].
- The case study runs the sequence in order — low-fidelity wireframes first,
  then high-fidelity visual prototypes, then three rounds of testing across
  desktop and mobile, narrowing the set successively and watching what users do
  rather than what they say [[2018-08-26_case-study-iterative-design-prototyping]].

### Paper prototyping

- Paper prototyping is a fast, cheap way to test early, when changes are still
  easy: sketch concepts, flows or ideas on paper and test the sketches with
  users [[2021-12-19_paper-prototyping-cutout-kit]].
- A session has a facilitator, a participant, and optionally a "computer helper"
  who manipulates the screens; that dedicated person, familiar with the screens
  and their order, prevents waiting and keeps momentum
  [[2021-12-19_paper-prototyping-cutout-kit]].
- Simulate interactions physically: long sheets pulled through a frame cutout
  for scrolling, separate paper layers laid on top for dropdowns and overlays
  [[2021-12-19_paper-prototyping-cutout-kit]].
- Keep blank paper at hand to create new screens between sessions when a problem
  recurs, and apply standard usability-testing practice (recruitment, clear task
  articulation) as usual [[2021-12-19_paper-prototyping-cutout-kit]].

### Wizard of Oz

- In a Wizard of Oz study, the user interacts with an interface that appears
  autonomous but is fully or partially controlled by a hidden human, which lets
  teams test complex technologies before building them
  [[2024-04-19_wizard-of-oz]].
- It fits conversational UIs, recommendation algorithms, and interfaces that look
  up real-time information, and it lowers the investment risk in costly
  technologies such as generative AI by giving early signal on desirability,
  utility and usability [[2024-04-19_wizard-of-oz]].
- Figma prototypes, coded prototypes and physical mockups can all serve as the
  visible surface [[2024-04-19_wizard-of-oz]].
- The wizard can answer with a closed method (preset responses), an open method
  (composed in session), or a hybrid; document roles, opening questions, which
  elements the wizard controls, the response options, and the rules for
  improvisation, then pilot the study [[2024-04-19_wizard-of-oz]].

### Content inside the prototype

- Poor placeholder content such as lorem ipsum prevents meaningful feedback,
  because it is the content that inspires feedback, not the container
  [[2024-05-17_promptframes]].
- A promptframe is a deliverable sitting between wireframe and prototype that
  documents what content should be generated, why, and under what constraints;
  different content types (copy, images, data visualisations) each need their
  own prompt parameters for tone, style, dimensions
  [[2024-05-17_promptframes]].
- Share context with the AI tool — personas, brand voice, mission, visual
  principles — to raise output quality; iterate by revising prompts and
  regenerating; and remember that final production content still requires human
  craft [[2024-05-17_promptframes]].

### Specifying and handing off

- Prototype specifications (redlines, annotations) are short text descriptions
  placed next to a prototype to explain ambiguous details; they come in three
  types — element (font, colour), functionality (behaviours and states), and
  content (placeholder text, messages) [[2022-06-05_prototype-specifications]].
- Good specifications are clear and brief, describe the prototype rather than
  replace it, use consistent project vocabulary, and follow design standards;
  they only work combined with the visual prototype, since text alone is harder
  to understand than a wireframe [[2022-06-05_prototype-specifications]].
- They act as external memory of design intent, help onboard new team members,
  and can be folded into a design system for reuse
  [[2022-06-05_prototype-specifications]]. They are not always needed: simple
  interfaces, small scopes, or work on a well-established design system may skip
  functionality and content specs, though element specs remain essential
  [[2022-06-05_prototype-specifications]].
- Designing components once and adding them to a master stylesheet lets
  developers reference detailed specs without redundancy when a component
  changes [[2018-08-26_case-study-iterative-design-prototyping]].
- Early interactive mockups also work as a collaboration device with
  developers: have the tech team test the first prototypes as users first, then
  discuss technical constraints, which gathers fast feedback and involves them
  early [[2024-09-03_344_Créer_du_lien_dev_tech_X_design_-_3_méthodes_efficaces]].

### AI-generated prototypes

- The Replit approach: an integrated AI agent builds the interface step by step
  from your specifications written as user stories, handling databases and API
  calls natively — the episode reports a fully functional, shareable flow in
  about 30 minutes [[2025-02-18_365_Replit,_l’outil_de_prototypage_design_ultime]]. Basic coding skills remain necessary to spot and
  fix bugs when the agent loops [[2025-02-18_365_Replit,_l’outil_de_prototypage_design_ultime]].
- NN/g's evaluations are more reserved. AI prototyping tools can follow
  instructions toward a general goal but lack the sophistication to weigh design
  tradeoffs without extensive human guidance [[2025-10-24_ai-prototyping]], and
  broad wireframe- and prototype-generation tools produce generic layouts with
  poor information hierarchy and only minor variations rather than meaningful
  alternatives [[2025-05-09_ai-design-tools-update-2]].
- What improves output: longer, more specific prompts, and above all design
  artefacts — Figma links or high-fidelity mockups as references beat text
  alone, because the tool can examine existing patterns and spatial
  relationships [[2025-10-24_ai-prototyping]]. Prompt-length limits (around 500
  characters in the tools reviewed) are named as a hard restriction on conveying
  context [[2025-05-09_ai-design-tools-update-2]].
- Persistent gaps: missing design-system integration, so AI prototypes built
  from random elements provide no value to teams working in an established
  system [[2025-05-09_ai-design-tools-update-2]]; outputs biased toward
  mainstream conventions, sans-serif typefaces and minimalist styling because
  they mirror training data; and missed details of visual hierarchy, grouping,
  spacing and colour contrast — "good from afar, but far from good"
  [[2025-10-24_ai-prototyping]].
- Where they do fit: rapid exploration and early-stage ideation in the hands of
  experienced designers who already understand layout, typography and component
  naming well enough to direct the tool, and who disambiguate vague UX language
  (what exactly is a "profile page") [[2025-10-24_ai-prototyping]],
  [[2025-05-09_ai-design-tools-update-2]].
- Note the disagreement in emphasis: the Parlons Design episode presents an AI
  agent as a practical way to reach a testable functional prototype quickly
  [[2025-02-18_365_Replit,_l’outil_de_prototypage_design_ultime]], while the NN/g evaluations conclude that no current tool replaces
  human design judgement [[2025-05-09_ai-design-tools-update-2]],
  [[2025-10-24_ai-prototyping]]. The two are testing different things —
  functional feasibility of a flow versus craft quality of a finished design.

## Sources (14)

- [[2016-12-18_ux-prototype-hi-lo-fidelity]] — High and low-fidelity prototypes serve as testing mechanisms before production with different trade-offs in time, realism, and error reduction; sketchy, static prototypes particularly accelerate design exploration, reduce designer attachment, allow design changes between sessions, and encourage teams to discard them if testing reveals issues since they feel less finished.
- [[2018-08-26_case-study-iterative-design-prototyping]] — creating representations of designs at varying fidelity levels for testing and validation; high-fidelity prototypes effectively test visual design and aesthetic appeal before development.
- [[2021-12-19_paper-prototyping-cutout-kit]] — A low-fidelity testing method where sketched concepts are tested with users using simple materials like paper, frames, and sticky elements to simulate interaction; maintaining consistent visual fidelity and avoiding high-fidelity elements ensures participants give balanced feedback across all screens.
- [[2022-06-05_prototype-specifications]] — Creating prototype specifications alongside prototypes improves design clarity and team understanding of design intent.
- [[2024-04-19_wizard-of-oz]] — explores how prototyping tools (Figma, coded prototypes, physical mockups) support Wizard of Oz studies.
- [[2024-05-17_promptframes]] — promptframes enable faster prototyping with more realistic content, improving the quality of feedback from colleagues and users in testing sessions.
- [[2024-09-03_344_Créer_du_lien_dev_tech_X_design_-_3_méthodes_efficaces]]
- [[2025-02-18_365_Replit,_l’outil_de_prototypage_design_ultime]]
- [[2025-05-09_ai-design-tools-update-2]] — documents that AI-generated wireframes and prototypes work best only for early ideation with experienced designers and cannot replace human design judgment.
- [[2025-10-24_ai-prototyping]] — what this article contributes to this concept
- [[2026-02-17_401_Prototypage_Le_guide_design_complet_-_Figma,_Lovable,_Google_Sheets_et_+]]
- [[2014-09-05_user-story-mapping_08-3-plan-to-learn-faster]] — High-fidelity prototypes in tools like Axure or PowerPoint are used to envision solutions before committing to building software.
- [[2014-09-05_user-story-mapping_20-15-using-discovery-for-validated-learning]] — Simple, low-fidelity prototypes (paper, comics, minimal code) help teams think through solutions and filter out ideas that won't work before building scalable software. The goal is learning, not perfection.
- [[2019-12-17_storytelling-in-design_14-chapter-13-applying-scene-structure-to-wireframes-designs]] — Prototypes test interactions and flows, revealing whether the narrative structure works. They serve both as tools for team iteration and as deliverables for stakeholders to experience the intended story before development. Clickable prototypes can visualize journeys and test whether all branches of the narrative remain coherent.
