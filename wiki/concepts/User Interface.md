---
type: concept
name: User Interface
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "AI User Interface Design"
  - "Interface Design"
  - "UI"
  - "UI Design"
  - "User Interface (UI)"
  - "User Interface Design"
  - "User Interface Quality"
---

# User Interface

## Definition

The user interface is the craft of creating effective human–computer
interactions [[2018-09-23_change-blindness-definition]]. In the sources, an
interface is judged less by how it looks than by what it makes visible and
achievable: modern graphical interfaces rest on direct manipulation, where
users act on displayed objects through physical, incremental, reversible
actions whose effects are immediately visible, so that available actions can be
recognised rather than remembered [[2016-08-21_direct-manipulation]]. The same
logic runs through the sources' treatment of menus, buttons, labels and
controls, which support recognition where hidden commands force recall
[[2024-01-15_recognition-and-recall]], and through the argument that the
interface should be built around human limitations rather than asking users to
compensate for poor design [[2022-04-01_recall-beats-recognition]]. Interface
quality is therefore treated as a proxy for product quality: even a detail like
an error message reads as an indicator of how much a product respects users'
time [[2023-06-18_error-messages-scoring-rubric]].

The concept is not confined to screens or to the desktop GUI. It extends to
touch and gesture on mobile devices with their sensors, cameras and varied
contexts of use [[2017-10-15_better-mobile]], to combined voice-and-screen
systems where the sources debate which modality should be primary
[[2017-11-12_voice-first]], and to a bodily gesture like raising a phone to the
ear as the entry point to an AI assistant
[[2024-05-28_330_Call_Arc,_l_interface_ChatGPT_parfaite_-_Analyse_Product_Design]].
It is also historically unstable: Nielsen frames generative AI as the third
interface paradigm after batch processing and command-based interaction, in
which users specify a desired outcome rather than the steps to reach it, while
predicting that hybrid interfaces retaining GUI elements will prevail
[[2023-06-18_ai-paradigm]]. And the population of users is itself changing —
AI agents now navigate interfaces built for humans, so "user" is no longer
synonymous with "human" [[2026-04-10_ai-agents-as-users]].

## Practice

### Make objects and actions visible

- Build on direct manipulation: continuous representation of the objects of
  interest, physical actions instead of complex syntax, continuous feedback,
  and reversibility. This yields rapid learning because users recognise what
  they can do instead of recalling command syntax
  [[2016-08-21_direct-manipulation]].
- Expose functions in visible elements — buttons, menus, labels. Menus are the
  archetypal recognition-based interface because they display the available
  commands; passwords are the archetypal recall-based one. Support recognition
  further with history, favourites, wishlists and recently-viewed items
  [[2024-01-15_recognition-and-recall]]. Games make the same point with
  on-screen contextual controls, maps and waypoints
  [[2019-05-19_usability-heuristics-applied-video-games]].
- Beware the costs of hiding. Hiding UI chrome to create a "zen" writing
  surface backfires: users must divert attention from the task to find and
  remember where the tools went, and mode switching adds its own overhead. True
  zen is a state of productivity, produced by immersive, forgettable design,
  not a visual style [[2016-12-18_zen-mode]]. Hamburger menus similarly reduce
  discoverability: hidden navigation is used less than a visible bar, even on
  mobile [[2017-01-01_ux-quiz-16]].
- Visibility has limits worth designing around: direct manipulation only works
  on objects that are visible, its physical actions cost effort and can cause
  repetitive strain injury, some actions fail silently with no feedback,
  experts prefer keyboard shortcuts for repetitive work, and
  direct-manipulation UIs can fail visually or motor-impaired users
  [[2016-08-21_direct-manipulation]]. Hotkeys and customisable controls serve
  expert users alongside novices
  [[2019-05-19_usability-heuristics-applied-video-games]].
- One source presents the opposite advice — deliberately designing for recall
  with numeric command codes, inscrutable icons and cue cards shown for three
  seconds — but it is an explicit April Fools' hoax and states that recognition
  over recall remains correct [[2022-04-01_recall-beats-recognition]].

### Choose the right control

- Listboxes vs. dropdowns: listboxes keep options visible, lowering interaction
  cost and supporting multiselection and reordering, but consume space and are
  less familiar; dropdowns are compact, familiar and allow a good default, but
  hide options behind a click, are prone to overstuffing, and slow users down
  for values they already know (dates, card expiry). Use a listbox for 5–15
  options when space allows, a dropdown for 5–15 when it does not, listboxes
  for multiselection, and radio buttons or checkboxes for five or fewer.
  Display options in a logical order [[2020-04-12_listbox-dropdown]].
- Distinguish button styles from button states: styles carry visual emphasis
  (primary vs. secondary), states carry interaction status (enabled, hover,
  pressed, disabled). Put secondary actions in contextual menus rather than
  among primary actions, and keep icons consistent across screens instead of
  tailoring them per layout [[2026-01-02_ux-quiz]].
- Icons must earn their place: their benefit should exceed the cost of design,
  research, coding, screen real estate and added visual noise. Good icons map a
  concept that naturally becomes an image, are simple, need no decoding, and
  are understood in a single fixation. Bad ones reuse an established meaning
  incorrectly, rely on esoteric references, are blurry, repeat needlessly down
  a list, or only make sense as a set. Icons are often added merely to break up
  text or follow a trend [[2017-11-19_bad-icons]].

### Dialogs, modals and modes

- A mode is a state in which the same input produces a different result. Modes
  help when there are many commands and few input methods, but they cause mode
  slips when the active mode is unclear, and they hurt discoverability because
  features that live in one mode are hard to find and remember, especially for
  occasional users. Signal the active mode with at least two independent visual
  indicators, and where a mix-up could cause real harm use separate controls
  instead. Modal windows are a special case of the same problem
  [[2019-04-14_modes]]. Modals restrict interaction with background content and
  should be used only when the user must interact before continuing
  [[2019-04-14_modes]].
- Confirmation dialogs give a genuine second chance only if users still read
  them. Restate the request with identifying details rather than asking "Are
  you sure?"; reserve them for serious consequences such as destroying work or
  large financial transactions, since over-warning produces habituation; label
  buttons with the action ("Delete file" / "Keep file") instead of Yes/No;
  avoid a dangerous default; and offer undo. Nonstandard confirmations such as
  typing a word should stay rare [[2018-02-18_confirmation-dialog]]. Games use
  the same devices — confirmation before quitting, clear mode indicators,
  disabling unavailable options
  [[2019-05-19_usability-heuristics-applied-video-games]].

### Feedback, status and noticing change

- Pick the right communication mechanism for the information: indicators are
  passive, conditional visual cues (icon, typography, size, animation) marking
  something worth attention; validations are error messages tied to user input
  and require correction; notifications announce system events and may be
  action-required (modal) or passive (toast, badge). Mismatches hurt — passive
  notifications for critical errors get missed, modal notifications for passive
  information frustrate, and indicators should not carry critical feedback
  [[2024-01-17_indicators-validations-notifications]].
- Design against change blindness: users miss changes outside their focus of
  attention, especially when the movement cue is weak or masked by a page load
  or a competing animation. Make one change at a time, group simultaneous
  changes in the same screen region, animate to signal change, dim unchanged
  areas, and place floating elements near where attention already is
  [[2018-09-23_change-blindness-definition]].
- Treat error messages as measurable interface output. A rubric scores them on
  visibility, communication and efficiency, four guidelines each, 1–4, averaged
  into a letter grade; independent scoring by several evaluators before
  averaging reduces bias and groupthink, and the grade helps prioritise UX debt
  [[2023-06-18_error-messages-scoring-rubric]].
- Keep system status visible, as with health meters and score displays in games
  [[2019-05-19_usability-heuristics-applied-video-games]].

### The visual layer

- Good-looking interfaces come from consistent application of fundamentals, not
  decoration: alignment to a grid, hierarchy carried by type size, weight and
  colour within a limited set of families, generous spacing and white space for
  scannability, a harmonious palette (monochromatic 3–4 colours being easiest
  to execute), asymmetrical balance for energy or symmetry for calm, and
  imagery that adds information rather than ornament. Whitespace, consistent
  iconography and subtle signals such as shadows and gradients guide users
  without distracting them [[2023-03-05_why-does-a-design-look-good-part2]].
- The vocabulary behind those choices — Gestalt grouping, visual hierarchy,
  contrast and brightness for legibility, internal and external consistency,
  whitespace as a design element, responsive adaptation across screens — is
  what connects visual design principles to design systems, component
  libraries and layouts [[2024-05-17_visual-design-cheat-sheet]].
- Glassmorphism uses translucency and background blur to build depth and
  separate foreground from background, with low-opacity strokes and gradients
  adding sophistication. Because translucent elements let text fall across
  several colours, contrast ratios become unpredictable and must be checked
  across the possible backgrounds; more blur is better over intricate
  backgrounds; offer user controls such as reduced transparency where feasible
  [[2024-06-07_glassmorphism]].
- Minimalism is worth pursuing only when it does not hide what users need:
  games keep interfaces powerful by pushing information to screen corners and
  using progressive disclosure
  [[2019-05-19_usability-heuristics-applied-video-games]], whereas hiding tools
  outright raises cognitive load [[2016-12-18_zen-mode]], and aesthetic appeal
  does not offset usability costs because negative experiences are weighted
  more heavily than positive ones [[2016-12-18_zen-mode]],
  [[2017-01-01_ux-quiz-16]].

### Beyond the desktop screen: mobile, gesture and voice

- Mobile is its own medium, not a shrunken desktop. Prioritise location-based,
  time-sensitive, emergency and phone-number information; integrate camera,
  GPS, biometrics and touch to remove friction (scanning a barcode instead of
  typing a long number); and look for interactions only possible on a mobile
  device, such as location-based rather than time-based reminders
  [[2017-10-15_better-mobile]].
- Voice and screen are complements: voice is an efficient input modality,
  screens an efficient output modality that reduces memory burden. Screen-first
  voice agents fragment tasks and drop visual affordances; voice-first devices
  that forbid visual menus create memory burden for no good reason. The source
  argues for integrating both without handicapping either
  [[2017-11-12_voice-first]].
- Gesture can be the interface. Arc's Call Arc launches an AI conversation by
  raising the phone to the ear, borrowing iOS call-interface conventions plus
  an animated smiley, which makes the feature immediately understandable to
  non-technical users while still offering advanced hooks (iOS shortcuts,
  the action button) for experts
  [[2024-05-28_330_Call_Arc,_l_interface_ChatGPT_parfaite_-_Analyse_Product_Design]].

### Interfaces in the AI era

- Intent-based outcome specification inverts the locus of control: the user
  states a desired result and the system decides how, which creates risk when
  users cannot verify that their intent was understood. Chat prose is not
  efficient for everything (form filling, for example), so hybrid interfaces
  keeping GUI elements are the likely outcome; iterative refinement is
  currently poorly supported [[2023-06-18_ai-paradigm]].
- Interface beats model. Bing Chat scored lower on helpfulness and
  trustworthiness than ChatGPT and Bard despite the same underlying model,
  because of weak information aggregation and UI problems: poorly curated
  references, broken or irrelevant in-answer links, weak or vanishing suggested
  follow-ups, multimedia that blocks scanning and scales badly on mobile, and
  ads placed in research-oriented conversations. More UI features can make a
  product worse when poorly executed [[2023-10-01_ai-bot-comparison]].
- For site chatbots, the guidance is conventional UI practice applied to a new
  container: one consolidated entry point, persistence across pages, an opening
  message that states capabilities instead of "ask me anything",
  context-aware suggestions presented as clickable buttons, images in
  recommendations, progressive disclosure instead of an ever-growing thread, no
  autoscrolling away from the start of a message, resizable windows for rich
  content, save/share, and voice input where relevant
  [[2026-04-24_ai-chatbots-design-guidelines]]. On trust, users respond to
  clear, task-focused reasoning and stated limits; entertainment personas and
  false confidence undermine it [[2026-01-02_ux-quiz]].
- Design for agent users as well as human ones. Agents read interfaces by
  vision (expensive, error-prone), by parsing the accessibility tree (cheaper,
  more reliable), or by direct API. Semantic HTML, clear labelling, predictable
  patterns and proper ARIA therefore serve agents as well as accessibility.
  Not every product wants agent traffic — ad-supported models, regulatory
  friction, competitive intelligence — but opting out carries competitive risk
  [[2026-04-10_ai-agents-as-users]].

### Evaluating an interface

- Nielsen's ten heuristics apply beyond conventional applications: visibility
  of status, match with the real world, user control and freedom, consistency
  with established conventions, error prevention, recognition over recall,
  flexibility and efficiency for both novices and experts, and aesthetic
  minimalism all transfer to video games
  [[2019-05-19_usability-heuristics-applied-video-games]]. Roughly 90% of the
  heuristics have held over 28 years, though specific guidelines can evolve
  [[2022-04-01_recall-beats-recognition]].
- Cognitive walkthroughs evaluate learnability without users: a cross-functional
  group steps through a task flow asking, at each step, whether users will try
  to achieve the right result, notice the correct action is available,
  associate it with the desired result, and see progress afterwards. They suit
  complex or unfamiliar workflows and early conceptual prototypes, and are
  overkill for standard, ubiquitous patterns
  [[2022-02-13_cognitive-walkthroughs]].
- Interface knowledge is treated as testable common ground: NN/g's year-in-review
  quizzes probe hamburger menus, visual indicators and menu types
  [[2017-01-01_ux-quiz-16]] and, later, button states and styles and contextual
  menus [[2026-01-02_ux-quiz]].

## Sources (26)

- [[2016-08-21_direct-manipulation]] — Modern UIs are built on direct-manipulation principles; interfaces succeed by making objects and available actions visible.
- [[2016-12-18_zen-mode]] — true zen in UI design comes from immersive, forgettable design that lets users focus on the task itself, not the interface; UI feel is more important than UI look.
- [[2017-01-01_ux-quiz-16]] — the quiz tests knowledge of UI patterns including hamburger menus, visual indicators, and menu types.
- [[2017-10-15_better-mobile]] — addresses how touch and gesture interaction, combined with mobile device features, enable new interface patterns.
- [[2017-11-12_voice-first]] — addresses design of integrated voice and screen interfaces and questions about which modality should be primary.
- [[2017-11-19_bad-icons]] — discusses icon design and usage patterns in web and intranet interfaces.
- [[2018-02-18_confirmation-dialog]] — designing dialogs with specificity, appropriate severity thresholds, and action-specific language to support user intent.
- [[2018-09-23_change-blindness-definition]] — the craft of creating effective human-computer interactions; awareness of change blindness enables better design choices around notifications, menu animations, and dynamic content.
- [[2019-04-14_modes]] — Modals, dropdowns, and other UI patterns can create modes that restrict or redirect user actions in ways that need clear signaling.
- [[2019-05-19_usability-heuristics-applied-video-games]] — Games demonstrate that minimalist design, progressive disclosure, and contextual information reduce overwhelm while keeping interfaces powerful.
- [[2020-04-12_listbox-dropdown]] — provides specific guidance on matching UI controls to design contexts considering option count, selection type, space constraints, and user motivation.
- [[2022-02-13_cognitive-walkthroughs]] — The methodology identifies design problems hindering learnability; best applied to complex systems with unfamiliar workflows; less effective for standard, ubiquitous design patterns.
- [[2022-04-01_recall-beats-recognition]] — building systems that respect human limitations rather than asking users to compensate for poor design.
- [[2023-03-05_why-does-a-design-look-good-part2]] — good interface design leverages whitespace, consistent iconography, meaningful imagery, and subtle visual signals (shadows, gradients) to guide users without distraction.
- [[2023-06-18_ai-paradigm]] — the article analyzes how AI systems present a fundamentally different interaction model requiring new approaches to usability and user interface design.
- [[2023-06-18_error-messages-scoring-rubric]] — error messages are treated as a key indicator of overall product quality and organizational commitment to user respect and efficiency.
- [[2023-10-01_ai-bot-comparison]] — Complex interfaces with many features can perform worse than simpler designs if features are poorly executed or create additional friction.
- [[2024-01-15_recognition-and-recall]] — visible UI elements (buttons, menus, labels) that support recognition work better than hidden commands requiring recall.
- [[2024-01-17_indicators-validations-notifications]] — the strategic placement, prominence, and design of feedback elements determines whether users notice and act on system information.
- [[2024-05-17_visual-design-cheat-sheet]] — Specific UI applications of visual design principles including design systems, consistency, responsive layouts, and component libraries, whose choices directly impact how users perceive and interact with interfaces, affecting both usability and aesthetic appeal.
- [[2024-05-28_330_Call_Arc,_l_interface_ChatGPT_parfaite_-_Analyse_Product_Design]]
- [[2024-06-07_glassmorphism]] — glassmorphism represents one approach to establishing visual hierarchy and content focus within UI, with both benefits and accessibility considerations.
- [[2026-01-02_ux-quiz]] — Understanding button states, styles, and contextual menus reflects core UI knowledge tested across fundamental design decisions.
- [[2026-04-10_ai-agents-as-users]] — Addresses design choices that either support or hinder agent interaction with digital systems.
- [[2026-04-24_ai-chatbots-design-guidelines]] — Applies established UI patterns and principles to chatbot design, showing how familiar best practices enhance chatbot usability.
- [[2024-01-23_laws-of-ux_11-9-teslers-law]] — The challenge of managing complexity while maintaining usability requires deliberate choices about which aspects of a system to abstract away and how to guide users without overwhelming them.
