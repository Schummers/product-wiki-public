---
type: concept
name: Interaction Design
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "AI Interaction Design"
  - "Human-Computer Interaction"
  - "Interaction Design Fundamentals"
  - "Interaction Design Optimization"
---

# Interaction Design

## Definition

Interaction design is the design of the exchange between a person and a system:
what the user can do, how the system responds, and how the two stay in sync. The
sources frame it around two recurring gaps described in
[[2018-03-11_two-ux-gulfs-evaluation-execution]] — the gulf of execution (the
user must work out what action will achieve their goal and how to perform it)
and the gulf of evaluation (the user must perceive and correctly interpret the
system's state). Everything else in this concept is machinery for narrowing
those gaps: controls whose arrangement matches their effect
([[2018-10-14_natural-mappings]]), feedback small enough to be constant
([[2018-10-21_microinteractions]], [[2025-04-25_button-states-communicate-interaction]]),
interfaces that let users recognise rather than recall
([[2024-01-15_recognition-and-recall]]), and targets that human hands can
actually hit ([[2019-05-05_touch-target-size]], [[2019-06-23_steering-law]]).
[[2024-01-10_psychology-study-guide]] states the underlying commitment plainly:
the best designs are built for people as they really are, not as designers wish
they were.

Interaction design is distinct from visual design and, according to
[[2016-07-17_interaction-branding]], receives less attention despite carrying
comparable weight — responsiveness, precision, consistency and expectedness were
found to map onto perceived brand attributes such as sincerity and competence,
so behaviour communicates as much as appearance ([[2016-07-03_brand-experience-ux]]).
Its scope in this corpus runs from the individual control (toggles, checkboxes,
steppers, split buttons) to the flow across screens and states
([[2016-12-04_wireflows]]), to the whole ecosystem of channels, devices and
touchpoints a customer moves through ([[2016-12-04_channels-devices-touchpoints]]).
It is also technology-agnostic: [[2024-03-29_new-ai-users-onboarding]] argues
that the fundamental principles hold regardless of how novel the technology is,
and [[2023-09-24_accordion-editing-apple-picking]] shows a conversational
interface failing on ordinary interaction-design grounds rather than on anything
specific to AI.

## Practice

### Feedback and visibility of system state

- Poor feedback is one of the longest-standing application design mistakes:
  applications must show current state, how a command was interpreted, and what
  is happening now, with explicit feedback for edit modes
  ([[2019-02-17_top-10-application-design-mistakes]]).
- Microinteractions are trigger-feedback pairs; they confirm the system
  registered an action, communicate state, and indicate whether more input is
  needed. Only elements triggered by user action or system change count —
  always-present elements are not microinteractions
  ([[2018-10-21_microinteractions]]).
- Button states carry that feedback at the component level: enabled, disabled,
  hover, focus, pressed, plus loading and selected. Timing is part of the
  specification — roughly 150–200 ms delay on hover to avoid accidental
  triggers, focus visible within 100–150 ms of a Tab press, pressed state within
  100–150 ms or users click again
  ([[2025-04-25_button-states-communicate-interaction]]).
- Sliders and other continuous controls need response within 0.1 second, and a
  linked slider/text-field pair must stay in sync within the same budget
  ([[2017-05-14_sliders-knobs]]).
- Empty states are a feedback surface, not a void: say whether content is
  loading, processing, or genuinely absent, and never show a "No records"
  message that disappears once loading finishes
  ([[2021-09-19_empty-state-interface-design]]).
- Drag-and-drop needs feedback at every phase — a distinct appearance once an
  object is grabbed (outline, drop shadow, offset, ghost image), and a ~100 ms
  reshuffle animation previewing where it will land
  ([[2020-02-23_drag-drop]]).

### Mental models, mappings, and expected behaviour

- Stimulus-response compatibility: when the spatial or conceptual relationship
  between a control and its outcome is aligned, users respond faster and err
  less. Spatial similarity (controls laid out like the thing they control),
  metaphorical and cultural associations ("up is more", green/red), and
  behavioural similarity (raise-to-wake mimicking how people tilt a watch) all
  produce good mappings; complex multi-finger gestures violate them because they
  have no clear relationship to the outcome ([[2018-10-14_natural-mappings]]).
- Parameter controls should represent what they adjust — a knob for an angle, a
  horizontal slider for panning left/right ([[2017-05-14_sliders-knobs]]).
- Toggle switches work because they match a real-world expectation: they take
  effect immediately, without Save or Submit, and are only appropriate for
  binary states ([[2018-07-29_toggle-switch-guidelines]]).
- Designers can borrow familiar mental models deliberately — checkbox controls
  that echo paper-form conventions let users interpret state correctly
  ([[2018-03-11_two-ux-gulfs-evaluation-execution]]). Breaking the analogy is
  costly: checkboxes where checked means "do not subscribe" produce errors,
  because users assume a checked box records a current subscription
  ([[2018-04-29_unsubscribe-mistakes]]), and negatively worded checkbox labels
  create double negatives ([[2024-06-28_checkboxes-design-guidelines]]).

### Motor constraints: targets, distance, and paths

- Touch targets should be at least 1 cm × 1 cm as physically rendered; pixel
  dimensions are meaningless across densities. Blame small targets, not "fat
  fingers". Size and spacing must both be right — either alone fails — and
  primary actions, in-motion use, children and seniors warrant more than the
  minimum ([[2019-05-05_touch-target-size]]).
- View-tap asymmetry: an element can be large enough to read yet too small or
  too crowded to tap, a common failure when desktop designs are adapted to
  mobile ([[2019-05-05_touch-target-size]]).
- Fitts's law applies beyond screens. On the Tesla dashboard, controls at the
  bottom of a 17-inch screen sit far from the steering wheel, targets shrank
  between versions, and crowding caused accidental activation — all with a
  distraction cost, since time looking at the UI is time not watching the road
  ([[2019-05-19_tesla-big-touchscreen]]).
- Small, closely spaced stepper buttons violate Fitts's law; horizontal steppers
  generally beat vertical ones, especially on mobile
  ([[2018-11-11_input-steppers]]).
- The Accot-Zhai steering law governs any control the pointer must travel
  through a bounded path to use: dropdown and hierarchical menus, sliders,
  scrollbars, scrubbers. Long narrow tunnels are slower than short wide ones
  because elbow and wrist describe an arc. Remedies: keep menus short, prefer
  mega menus over hierarchical ones (free 2D movement), add secondary controls
  such as a numeric field for precision, and pad tunnel boundaries for wiggle
  room ([[2019-06-23_steering-law]]).
- Magnetic snapping that activates drop zones slightly beyond their visible
  border expands the effective target in drag-and-drop
  ([[2020-02-23_drag-drop]]).

### Choosing the right control

- [[2025-02-28_ui-elements-glossary]] catalogues the vocabulary — buttons,
  accordions, dropdowns, dialogs, tooltips and popup tips, tab bars — with the
  conditions under which each is appropriate.
- Listbox vs dropdown: the listbox has lower interaction cost (options visible
  without a click) and supports multiselect, but costs space and is less
  familiar; the dropdown is compact and familiar but hides options, is easy to
  overstuff, and slows users who already know the value. Both fit roughly 5–15
  options — listbox when space allows, dropdown when it does not; below 5
  options use radio buttons or checkboxes ([[2020-04-12_listbox-dropdown]]).
- Toggles suit two opposing states with immediate effect; radio buttons or
  checkboxes suit multiple options or anything needing a Submit
  ([[2018-07-29_toggle-switch-guidelines]]). Checkboxes mean zero-or-more,
  radio buttons exactly one; keep boxes square, make labels clickable, list
  vertically, and state minimum/maximum selection rules explicitly
  ([[2024-06-28_checkboxes-design-guidelines]]).
- Input steppers fit fields with a clear, frequently chosen default and small
  relative adjustments (passenger count, cart quantity); they fail for wide
  ranges and continuous quantities. Pairing a stepper with a text field covers
  both ([[2018-11-11_input-steppers]]).
- Parameter controls trade exploration against precision. Sliders support
  exploration; text inputs support precision; range sliders with a histogram
  help users avoid empty result sets; 2D matrices handle related parameters
  simultaneously; virtual knobs read naturally for rotation but the mouse
  affords no rotation, and hidden vertical-drag behaviour hurts discoverability.
  Linked controls plus a neutral default and a visible Reset are the
  recommended combination ([[2017-05-14_sliders-knobs]]).
- Split buttons give one-click access to the dominant action while grouping the
  rest, but the arrow must be visually separated and always visible, labels beat
  icons, and they are unsuitable for touch and for navigation. The source names
  its own tension: persistent split buttons (last choice becomes the new
  default) help power users and confuse newcomers by breaking spatial
  consistency ([[2019-05-12_split-buttons]]).
- Contextual menus should hold only task-relevant actions, ordered by frequency,
  under about ten to twelve items, with irrelevant options disabled rather than
  hidden, and every command also reachable from main navigation
  ([[2019-03-17_contextual-menus]]).
  [[2025-11-28_contextual-menus-guidelines]] adds that they are for secondary,
  low-priority actions only — burying essential functions behind extra clicks
  violates expectations — and names the tradeoff explicitly: they reduce visual
  noise at the cost of findability, information scent (users cannot predict what
  is inside) and misinterpretation risk. Kebab (⋮) and meatball (⋯) icons are
  recognised as "more options", but repurposing them for other interactions
  erodes mental models and trust; they must be large, high-contrast, visible
  without hover, placed near the content they affect, and labelled ("Post
  Actions") or tooltipped, since overflow icons carry no inherent meaning.
  Reserve them for actions, not for expanding text or images, and keep the
  hamburger for global navigation.
- Tooltips carry supplementary information only — never instructions or
  actionable content — must work on keyboard focus as well as mouse hover, and
  should be applied consistently across similar elements
  ([[2019-01-27_tooltip-guidelines]]). Unlabelled icons are ambiguous; visible
  text labels also enlarge the target
  ([[2019-02-17_top-10-application-design-mistakes]]).

### Direct manipulation, gestures, and drag-and-drop

- Direct manipulation means acting on displayed objects with physical,
  incremental, reversible actions whose effects are immediately visible. It
  favours recognition over recall and is learned quickly, but only works on
  visible objects, can cause repetitive strain, sometimes gives no feedback when
  an action is unavailable, is slower than keyboard shortcuts for expert
  repetition, and raises accessibility difficulties
  ([[2016-08-21_direct-manipulation]]).
- Drag-and-drop is familiar yet inherently inefficient and error-prone: it
  demands precise positioning over distance. Use it only where users expect it
  and no better alternative exists. Grab handles are not universally recognised,
  so cursor change is the more reliable signifier; keyboard access (Tab, space
  to grab, arrow keys) and screen-reader messaging are required; on touch,
  menu-based alternatives may be more usable despite taking more steps
  ([[2020-02-23_drag-drop]]).
- Contextual swipe is widely adopted but weakly signified: users forget it
  exists, the swipe hides the very item being acted on, non-standard meanings
  (saving rather than deleting) go undiscovered, direction-dependent meanings
  raise cognitive load, and horizontal swipe collides with back/split-screen
  navigation. The guidance is to keep affected content visible, confirm or offer
  easy undo before destruction, and restrict swipe to delete/remove so the
  meaning stays consistent ([[2017-02-12_contextual-swipe]]).
- Gestures can nonetheless become mainstream: WeChat's QR scanning and shake
  gesture met usefulness, ease of use, and discoverability, helped by embedding
  the scanner in the app itself and by a Spring Festival campaign that gave
  hundreds of millions a reason to learn the gesture. The same source notes the
  implementation's own discoverability faults — long-press extraction from chat
  is unintuitive and QR codes carry no information scent
  ([[2016-10-16_wechat-qr-shake]]).
- Complex multi-finger gestures are hard to discover and remember
  ([[2018-10-14_natural-mappings]]), and gesture-based interfaces push users
  toward recall rather than recognition ([[2024-01-15_recognition-and-recall]]).

### Cognitive load, memory, and external scaffolding

- Working memory holds roughly seven chunks briefly and varies by individual,
  education and age. Programmers self-select for larger capacity, so what feels
  easy to a developer may overload most users
  ([[2018-04-29_working-memory-external-memory]]).
- Offload rather than demand: comparison tables, shopping carts, open tabs and
  note-taking act as virtual scratchpads. Mobile screens show less external
  memory at once, so demand rises ([[2018-04-29_working-memory-external-memory]]).
  [[2022-09-11_context-cues-framework-field-studies]] grounds the same point in
  distributed cognition — thinking is spread across people, artefacts and
  environments, and field observation reveals where that scaffolding is missing.
- Design for recognition: menus show available commands where a command line
  requires recall; history, favourites, wishlists and recently-viewed items make
  past context visible again ([[2024-01-15_recognition-and-recall]]).
- Interaction cost — the total mental and physical resource an action demands —
  predicts whether users will attempt it at all
  ([[2024-01-10_psychology-study-guide]]). Attention is selective and change
  blindness is real, so changes outside the focus area are missed
  ([[2024-01-10_psychology-study-guide]]).
- Modals cover context users may still need and force them to hold instructions
  in memory ([[2019-02-17_top-10-application-design-mistakes]]).
- Meaningful defaults speed interaction, teach appropriate responses, and guide
  novices toward safe outcomes
  ([[2019-02-17_top-10-application-design-mistakes]],
  [[2017-05-14_sliders-knobs]]).

### Errors, modes, and consequential actions

- Modes make the same input produce different results. They fail through mode
  slips when the active mode is not obvious; discoverability suffers because
  features live inside modes; the remedy is at least two independent visual
  indicators (for example highlight plus cursor change) so the mode is evident
  to an inattentive user. Modal windows are a special case of the same problem
  ([[2019-04-14_modes]]).
- Confirmation dialogs only work if users still read them. Restate the request
  with identifying detail (filename, quantity) rather than "Are you sure?",
  reserve them for serious consequences so habituation does not set in, label
  buttons with the action ("Delete file" / "Keep file") instead of Yes/No, avoid
  defaulting to yes, and reserve nonstandard confirmations such as typing a word
  for genuinely rare, extreme cases ([[2018-02-18_confirmation-dialog]]). For
  swipe-to-delete, [[2017-02-12_contextual-swipe]] treats confirmation *or* easy
  undo as the minimum bar.
- Do not place consequential options next to benign ones. Users on repetitive
  work run on System 1 automaticity and respond to preattentive cues, so
  differentiate redundantly by colour, icon, size and alignment, and separate
  spatially — using Fitts's law in reverse, so a destructive action costs more
  motor time to reach. The precedent given is Chapanis's WWII shape-coding of
  B-17 levers ([[2021-02-14_proximity-consequential-options]]). Proximity of
  destructive actions also appears among the newer application design mistakes
  ([[2019-02-17_top-10-application-design-mistakes]]).
- Error messages must say why the error happened and how to fix it; "something
  went wrong" strands the user
  ([[2019-02-17_top-10-application-design-mistakes]]). Microinteractions can
  prevent errors before submission through password-requirement indicators,
  validation feedback and undo affordances ([[2018-10-21_microinteractions]]).
- Video games follow the same heuristics: undo/redo and save points for user
  control, confirmation before quitting, disabling impossible actions, and
  on-screen contextual controls instead of memorised combinations
  ([[2019-05-19_usability-heuristics-applied-video-games]]).

### Consistency, conventions, and learnability

- Users expect consistent terminology, control placement, rules and feature
  availability; inconsistency confuses even experienced users
  ([[2019-02-17_top-10-application-design-mistakes]]). Toggles
  ([[2018-07-29_toggle-switch-guidelines]]), tooltips
  ([[2019-01-27_tooltip-guidelines]]), swipe
  ([[2017-02-12_contextual-swipe]]) and overflow icons
  ([[2025-11-28_contextual-menus-guidelines]]) each repeat the point for their
  own component; games that break platform control conventions raise learning
  cost ([[2019-05-19_usability-heuristics-applied-video-games]]).
- The rule of enhancement: an enhanced interaction may be offered, but the UI
  must never depend on it for any task, whether the constraint is technological
  (camera search exists only on some devices) or user ability (not everyone
  knows the gesture). Redundancy is welcome here. Enhancements become standards
  when there are no competing alternatives for the same function and when
  consistent use across many sites lets people practise — as happened with
  scroll-wheel scrolling — and older methods should still be retained
  ([[2016-05-01_enhancement]]).
- The sources disagree about surprise. [[2016-07-17_interaction-branding]]
  reports that carefully designed unexpected interactions can trigger pleasant
  surprise, while also warning they can make users feel powerless and that
  testing is essential; [[2017-02-12_contextual-swipe]] and
  [[2025-10-10_liquid-glass]] treat unexpected behaviour as straightforwardly
  harmful.
- [[2025-10-10_liquid-glass]] is the corpus's case study in accumulated
  interaction damage: translucency obscuring content, motion that delights on
  first use and fatigues on the hundredth, tap targets below the 1 cm²
  guideline, controls that appear and vanish by context so users must rescan
  every time, abandoned conventions (search moved to the bottom, changed
  back-button behaviour) whose relearning costs productivity even if the new
  pattern is eventually better, and hidden controls that reduce discoverability.
- Animation is disruptive by default: use it only where necessary, keep it fast
  and smooth, and avoid the "stalker menu" pattern
  ([[2021-04-04_sticky-headers]]). Scroll fading has its own failure modes —
  the illusion of completeness that stops users discovering content below the
  fold, and text fading in slower than 500 ms that users scroll past before
  comprehending; fade in fast (100–400 ms), let elements persist rather than
  re-animate, animate one element type at a time, and avoid it on mobile
  ([[2023-12-08_scroll-fading-101]]).
- Sticky headers should be as short as possible, high-contrast rather than
  translucent, and justified by an actual cost-benefit analysis; partially
  persistent headers that reappear on upward scroll (300–400 ms animation) are
  the middle ground ([[2021-04-04_sticky-headers]]).

### Reducing interaction cost and friction

- The EAS framework applies effort reduction to forms: eliminate nonessential
  questions (every question is a trust withdrawal), defer what can wait, branch
  early with conditional logic, automate by reusing prior data and inferring
  values (city/state from ZIP, age from birthdate, card type from number), then
  simplify what remains with helpful defaults, mobile affordances (camera
  scanning, GPS, voice), flexible formatting and input masks
  ([[2025-03-07_eas-framework-simplify-forms]]).
- Exit flows deserve the same care as entry flows: an unsubscribe should be one
  click, with a visually weighted, conventionally styled link labelled
  "Unsubscribe", confirmed on the website rather than by a follow-up email, and
  free of login walls, preference matrices or feedback requests
  ([[2018-04-29_unsubscribe-mistakes]]).
- Contextual menus reduce interaction cost by presenting only relevant actions
  without parsing a full menu system ([[2019-03-17_contextual-menus]]);
  steppers reduce it for small numeric adjustments
  ([[2018-11-11_input-steppers]]); QR and shake replace arduous mobile typing
  and bridge offline to online ([[2016-10-16_wechat-qr-shake]]).
- [[2016-11-20_ux-thanks]] catalogues friction removed in practice: biometric
  authentication replacing passwords, adding a stop mid-route without leaving
  the flow, voice input when hands are occupied, offline downloads, and device
  handoff that preserves login and playback position.
- Virtual tours are the counter-example: movement is slow and effortful (turning
  around can take eight or more swipes on mobile), wayfinding is poor, and the
  initial delight fades. The successful ones curate and guide rather than
  offering freeform exploration, and supply expert information (room dimensions,
  appliance condition) by default instead of making users discover it
  ([[2020-08-30_virtual-tours]]).
- Calculators and quizzes are used casually and exploratively: allow anonymous
  use with no registration, embed the tool rather than hiding it in a popup,
  require only essential inputs, return results immediately, let a single input
  be changed without re-entering the rest, offer an easy restart, explain why
  each input is needed, contextualise the output, and avoid misleading defaults
  ([[2024-04-19_recommendations-calculator]]). Users arrive with low commitment,
  enter rough estimates first, expect more detail to yield more accurate
  results, and work the tool in both directions — entering a desired output to
  reverse-engineer the inputs ([[2024-03-22_calculator-expectations]]).
  Conversion and prediction calculators can lead into recommendation, guiding
  users from understanding their situation to an actionable next step
  ([[2024-04-12_3-types-calculator]]).

### Modality, device, and channel

- A channel is the medium of interaction, a device is what gives access to a
  channel, and a touchpoint is a specific combination of device, channel and
  task. Organisations should map their whole ecosystem rather than optimising
  one device at the expense of the omnichannel journey
  ([[2016-12-04_channels-devices-touchpoints]]).
- Mobile interaction design is its own body of constraints — touch targets,
  gestures, input methods, accordions, sliders, carousels, input fields — with
  navigation patterns that have standardised and are widely understood
  ([[2023-01-12_mobile-ux-study-guide]]). [[2025-12-18_web-ux-study-guide]]
  plays the equivalent role for web interaction design, organising 150+ NN/g
  resources across 13 areas and putting foundational theory first: information
  foraging and information scent explain navigation choices, scanning patterns
  (F-shaped, layer-cake, lawn-mower) explain how people read, and convention
  and standardisation matter because users arrive with mental models built on
  other sites. Its recurring interaction-design point is that every pattern
  buys something and costs something — accordions and carousels hide content
  and lower discoverability, modals interrupt, infinite scrolling removes
  pagination cues — so each use needs a contextual justification rather than an
  appeal to minimalism or trend. It also rejects mobile-first as dogma: users
  do important or complex tasks on larger screens, and breakpoints should
  follow content hierarchy and task rather than screen size alone.
- Voice and screen are complementary: voice is efficient input and works
  hands-free, screens display large information sets and reduce memory burden.
  Screen-first agents fragment the task (voice does step one, touch does the
  rest) and waste screen space; voice-only devices force users to remember
  commands. [[2017-11-12_voice-first]] argues explicitly against voice-first
  purity — prohibiting a visual list across 15,000+ skills creates a memory
  burden — and concludes that combining both modalities without handicapping
  either is more effective.
- Cross-device continuity is itself a feature: maintaining login state and
  resuming playback on another device ([[2016-11-20_ux-thanks]]).
- Customization is user-driven, personalization system-driven; neither should be
  used to rescue a weak baseline experience
  ([[2016-07-10_customization-personalization]]). Customization interfaces
  should be discoverable and placed near the related content, simple (one click
  beats many steps), layered by progressive disclosure, and clearly worth the
  effort ([[2016-08-14_customization]]).

### Discoverability, help, and onboarding

- Push revelations — unprompted tutorials at launch — interrupt users, present
  information out of context, and exceed working memory. Pull revelations,
  triggered by a signal that the user needs help now, work better; progressive
  disclosure keeps help visible without overwhelming, and multi-step workflows
  should show help alongside each step rather than requiring memorisation
  ([[2023-02-12_onboarding-tutorials]]).
- The same conclusion holds for users new to AI: short tutorials answering "what
  does this do?" and "how does it work?" beat long ones, help placed too early
  is skipped, contextual guidance should arrive at the moment of use, tool names
  should communicate function, and general examples invite exploration better
  than niche ones ([[2024-03-29_new-ai-users-onboarding]]).
- Empty states are a learning surface: explain what could appear there and how
  to populate it, and provide a direct path to the action rather than only
  describing it ([[2021-09-19_empty-state-interface-design]]).
- Hidden interactions need signifiers — an ellipsis or arrow for contextual
  menus ([[2019-03-17_contextual-menus]]), a visible separated arrow on a split
  button ([[2019-05-12_split-buttons]]), a cursor change or grab handle for
  drag-and-drop ([[2020-02-23_drag-drop]]) — because gestures and right-click
  are not universally known.

### Conversational and AI interfaces

- Conversational UIs are not automatically easier. Users perform *accordion
  editing* (repeatedly asking for longer or shorter output, using word counts
  and forced rankings) and *apple picking* (referencing a specific fragment of a
  previous answer), and the endlessly scrolling chat window supports neither:
  users scroll through walls of text and get lost comparing iterations. The
  fixes proposed are compartmentalisation, point-to-select referencing, and
  direct editing of a portion of a response without regenerating it
  ([[2023-09-24_accordion-editing-apple-picking]]).
- Site chatbots: consolidate multiple chats into one entry point, persist across
  pages, state capabilities in the opening message instead of "ask me anything",
  make suggested questions clickable buttons and tailor them to the current
  page, include images in recommendations, use progressive disclosure rather
  than appending, do not autoscroll away from the start of a message, allow
  resizing, and support saving or sharing
  ([[2026-04-24_ai-chatbots-design-guidelines]]).
- Prompt suggestions address the blank-page problem in three forms: use-case
  suggestions (learnability), prompt autocomplete (efficiency), and follow-up
  questions (engagement). Follow-ups are judged the most useful because they are
  tailored to what the user has already established
  ([[2025-04-25_prompt-suggestions]]).
- Humanization is a deliberate choice with measurable cost: warmth is associated
  with 10–30% higher error rates and 12–14% reliability drops, filler
  pleasantries waste time, users who attribute emotional traits to a system are
  less likely to accept its advice, and human-like conversation invites a
  confidentiality expectation the system cannot meet. The recommendation is to
  design AI as a tool — accurate, transparent about limits, low on sycophancy
  ([[2026-01-09_humanizing-ai]]).
- Explanations of how an AI reached an output help users build accurate mental
  models and calibrate trust, but the explanations LLMs currently offer are
  often inaccurate, and three common patterns each fail in their own way.
  Source citations are frequently hallucinated — nonexistent URLs, or real
  articles that do not support the claim — and users rarely click them, so the
  mere presence of citations manufactures confidence. Step-by-step reasoning
  looks transparent but is often an after-the-fact rationalisation rather than
  a faithful trace of the computation, omitting real influences and shifting
  when the user pushes back. Disclaimers fail because they are skimmed. UX
  cannot fix the model, but it controls presentation: style citations
  prominently and place them adjacent to the claim they support, put the
  disclaimer near the input box in clear action-oriented wording ("Please
  double-check responses") and repeat it in onboarding, and avoid first-person
  anthropomorphic phrasing such as "I thought about your problem", which
  inflates trust ([[2025-12-12_explainable-ai]]).

### Specifying and prototyping interaction

- Wireflows combine wireframe layout with flowchart sequence, documenting the
  state changes and feedback (confirmations, colour changes, error messages)
  that static wireframes miss. Arrows must mark the hotspot that triggers each
  step. They suit apps with few screens but heavy dynamic change, and become
  unwieldy for sites with many static pages; they work at any fidelity,
  including rough collaborative sketching
  ([[2016-12-04_wireflows]]).
- Prototype specifications (redlines) cover element, functionality and content
  details. Functionality specs matter most precisely where behaviour cannot be
  read off a wireframe or visual comp; they act as external memory for the team,
  work only alongside the prototype rather than replacing it, and can feed back
  into the design system ([[2022-06-05_prototype-specifications]]).
- AI prototyping tools follow instructions but do not weigh design tradeoffs.
  Output quality tracks prompt specificity, and design artefacts (Figma links,
  high-fidelity mockups) outperform text alone because the model can read
  existing patterns and spatial relationships; outputs still miss visual
  hierarchy, grouping of related elements, spacing and colour contrast, and skew
  toward mainstream conventions — generic sans-serif, minimal styling — inherited
  from training data. Because UX language is ambiguous ("profile page" means
  several things), designers must disambiguate it, and the tools work best in
  the hands of people who already know layout, typography and component naming
  well enough to direct them ([[2025-10-24_ai-prototyping]]). Vague prompts
  produce what [[2025-12-05_vague-prototyping]] calls *Frankenstein layouts*:
  information repeated several times, visually prominent containers holding
  almost nothing, elements placed illogically, and a hierarchy that contradicts
  task priority — which raises cognitive load and interaction cost and buries
  the content that matters. Precision beats verbosity: an established style term
  ("neobrutalism") directs the model better than "modern" or "clean", and
  lightweight references (moodboards, design-system screenshots, mock data,
  code snippets from the existing system) sharpen output without any polished
  mockup.

### Ethics and the cases outside the happy path

- Interaction cost, visibility of options and clarity of choice can all be
  weaponised. Deceptive patterns work through obstruction, visual tricks,
  nagging, emotional manipulation and sneaking; mild ones escape notice in
  testing while obvious ones provoke anger, and they hit users with lower
  literacy hardest. The line from persuasive design is whether information is
  accurate, accessible, and the exchange fair; cognitive walkthroughs asking
  whether users might overspend, misread a choice, miss an option or feel
  rushed help surface them ([[2023-12-01_deceptive-patterns]]).
- Designing only the happy path leaves out scenarios that are common rather than
  exceptional: account lockouts and recovery after a stolen phone, name changes,
  multiple or shared accounts, simultaneous editors on poor connections, bad
  actors (so blocking, reporting and account-creation friction belong in the
  design from the start), and death (memorial modes, legacy contacts, stopping
  automated retrospectives). Account switching must not force repeated logouts
  or data loss when circumstances change, and safety needs friction built in
  from the start rather than bolted on after abuse appears. Accessibility is a
  constraint from day one, not a later feature — over 1 in 4 adults have a
  disability — as is offline behaviour: design offline-first, cache
  intelligently, and show a clear sync status ([[2025-10-24_edge-cases]]).
- Direct manipulation and drag-and-drop both carry accessibility debt that must
  be paid deliberately — keyboard access and screen-reader messaging
  ([[2016-08-21_direct-manipulation]], [[2020-02-23_drag-drop]]) — as do
  tooltips, which must respond to keyboard focus
  ([[2019-01-27_tooltip-guidelines]]).

## Sources (64)

- [[2016-05-01_enhancement]] — The article explores how interaction patterns can evolve from enhancements to standards through consistent, widespread adoption and user learning.
- [[2016-07-03_brand-experience-ux]] — Interaction design details—from transitions to animations to overall system behavior—communicate brand attributes and influence customer perceptions of professionalism and competence.
- [[2016-07-10_customization-personalization]] — Both customization and personalization require thoughtful design to avoid adding complexity to the baseline experience.
- [[2016-07-17_interaction-branding]] — Interaction design is a primary vehicle for communicating brand attributes; responsiveness, consistency, and clear feedback signal competence and sincerity.
- [[2016-08-14_customization]] — Customization interfaces should be minimal, progressive, and integrated naturally near relevant content.
- [[2016-08-21_direct-manipulation]] — Direct manipulation is a core interaction paradigm that supports user empowerment and control through physical, visible actions, reducing the gulf between user intentions and system actions.
- [[2016-10-16_wechat-qr-shake]] — Shows how gesture-based and QR-code interaction exemplify low-cost alternatives to typing, and how repeated exposure and association with valued outcomes build adoption and mastery.
- [[2016-11-20_ux-thanks]] — Removing friction and enabling seamless flows across device ecosystems and contexts improves perceived value and user satisfaction.
- [[2016-12-04_channels-devices-touchpoints]] — Designing for multiple interaction channels requires understanding how devices enable access to channels, and how touchpoints define specific customer-organization interactions across the full ecosystem.
- [[2016-12-04_wireflows]] — Wireflows document how interactions change page state and provide feedback, capturing the dynamic behavior that traditional wireframes miss.
- [[2017-02-12_contextual-swipe]] — contextual swipe design must maximize content visibility, prevent accidental actions, maintain consistency, limit swipe to destructive actions, and avoid gesture ambiguity with navigation.
- [[2017-05-14_sliders-knobs]] — Emphasizes immediate feedback, natural mappings, affordance clarity, and keyboard efficiency in parameter control design.
- [[2017-11-12_voice-first]] — considers tradeoffs between voice-first purity and practical functionality when combining interaction modes.
- [[2018-02-18_confirmation-dialog]] — balancing the need to prevent errors against user annoyance by applying confirmation selectively and providing undo alternatives.
- [[2018-03-11_two-ux-gulfs-evaluation-execution]] — Interaction design requires both understanding the fundamental challenges users face in perceiving system state and planning effective actions, and designing controls and feedback that bridge these gulfs through clear mental models.
- [[2018-04-29_unsubscribe-mistakes]] — designing clear, minimal flows that prioritize user goals over organizational interests or data collection.
- [[2018-04-29_working-memory-external-memory]] — providing UI features like comparison tools and persistent storage that help users manage complex tasks within cognitive constraints.
- [[2018-07-29_toggle-switch-guidelines]] — toggle switches exemplify proper interaction design by matching system behavior to user expectations from the real world.
- [[2018-10-14_natural-mappings]] — how the relationship between user actions and system responses must be intuitive and aligned with user expectations to create usable interfaces.
- [[2018-10-21_microinteractions]] — how small, incremental feedback elements combine to create a coherent and engaging experience throughout the user journey.
- [[2018-11-11_input-steppers]] — designing numeric input controls that balance usability, precision requirements, and the context of use.
- [[2019-01-27_tooltip-guidelines]] — The article addresses interaction patterns for desktop systems, distinguishing between mouse hover and keyboard hover interactions.
- [[2019-02-17_top-10-application-design-mistakes]] — Design patterns for interactions including edit modes, validation, progress indication, and modal dialogs that support user understanding and prevent errors.
- [[2019-03-17_contextual-menus]] — Platform-specific interaction patterns for triggering contextual menus (right-click, long-press, swipe) and managing submenu complexity.
- [[2019-04-14_modes]] — Mode design requires careful consideration of user awareness and feedback; redundant visual indicators prevent mode slips.
- [[2019-05-05_touch-target-size]] — Fitts's law applies to touch: acquisition time depends on target size and distance; larger targets and better spacing improve usability.
- [[2019-05-12_split-buttons]] — Split buttons reduce cognitive load by grouping commands but require careful design to ensure the secondary menu is discoverable.
- [[2019-05-19_tesla-big-touchscreen]] — Car dashboards require special consideration of distraction cost and safety implications; touchscreen design must minimize attention demands.
- [[2019-05-19_usability-heuristics-applied-video-games]] — Game controls and interfaces must follow platform conventions and provide clear feedback; violations increase cognitive load and learning time.
- [[2019-06-23_steering-law]] — the steering law informs design choices for controls that require path-following; understanding motor constraints helps create faster, more usable interfaces.
- [[2020-02-23_drag-drop]] — Details how to design drag-and-drop interactions including signifiers, feedback, and trigger mechanics for smooth, understandable interactions.
- [[2020-04-12_listbox-dropdown]] — examines interaction cost, visibility, and cognitive load differences between always-visible listboxes and hidden-until-clicked dropdowns.
- [[2020-08-30_virtual-tours]] — Successful virtual tours minimize interaction cost through guided, curated experiences rather than freeform exploration, and incorporate contextual expert information rather than requiring users to explore and discover details independently.
- [[2021-02-14_proximity-consequential-options]] — demonstrates how to differentiate controls through visual and spatial properties that work even when users are inattentive.
- [[2021-04-04_sticky-headers]] — the article provides guidance on animation, motion, and interaction patterns for sticky header implementations.
- [[2021-09-19_empty-state-interface-design]] — The article emphasizes providing clear calls to action within empty states to encourage users to engage with features and workflows.
- [[2022-06-05_prototype-specifications]] — Specifications are especially important for complex interactions where behavior details cannot be expressed through wireframes or visual design alone.
- [[2022-09-11_context-cues-framework-field-studies]] — Products that minimize cognitive load by providing scaffolding and external memory support better usability; context observations reveal where these supports are missing.
- [[2023-01-12_mobile-ux-study-guide]] — Mobile interaction design encompasses touch targets, gestures, input methods, and component design adapted to mobile constraints and touchscreen affordances.
- [[2023-02-12_onboarding-tutorials]] — designing help systems requires understanding user workflows and signals indicating when help is needed to create effective, non-intrusive support.
- [[2023-09-24_accordion-editing-apple-picking]] — Conversational interfaces require specific design features like compartmentalization and point-to-select to support iterative work patterns.
- [[2023-12-01_deceptive-patterns]] — interaction cost, visibility of options, and clarity of choices are design elements that can be misused deceptively or applied ethically.
- [[2023-12-08_scroll-fading-101]] — scroll fading affects how users interact with page content; proper implementation considers user scanning patterns and content discovery.
- [[2024-01-10_psychology-study-guide]] — the intersection of psychology and technology; HCI design succeeds by respecting human limitations and capabilities.
- [[2024-01-15_recognition-and-recall]] — designing for recognition through visibility and accessibility leads to more usable interactions than forcing users to memorize commands.
- [[2024-03-22_calculator-expectations]] — addresses how interaction patterns affect user trust and willingness to explore calculator outputs.
- [[2024-03-29_new-ai-users-onboarding]] — demonstrates that fundamental interaction-design principles remain applicable regardless of technology novelty.
- [[2024-04-12_3-types-calculator]] — discusses designing calculator workflows that guide users through calculation toward recommendations.
- [[2024-04-19_recommendations-calculator]] — covers interaction patterns that support casual, exploratory tool use.
- [[2024-06-28_checkboxes-design-guidelines]] — checkbox interaction must be intuitive and predictable; users must understand both selected and unselected states, and feedback must be clear.
- [[2025-02-28_ui-elements-glossary]] — Explains foundational patterns (buttons, inputs, menus, dialogs) and when each is appropriate, helping designers select components matching user needs and task types.
- [[2025-03-07_eas-framework-simplify-forms]] — Applies effort-reduction principles to form interactions, showing how automation and smart input handling (input masks, format flexibility, mobile features) reduce cognitive and physical burden.
- [[2025-04-25_button-states-communicate-interaction]] — focuses on how state changes communicate interaction possibilities and feedback to users through visual design.
- [[2025-04-25_prompt-suggestions]] — focuses on how suggestion placement, content, and types influence user behavior and engagement with AI systems.
- [[2025-10-10_liquid-glass]] — Shows how motion and changing interfaces, even when individually justified, accumulate to create a restless, unpredictable interface that disrupts learning and established mental models.
- [[2025-10-24_ai-prototyping]] — what this article contributes to this concept
- [[2025-10-24_edge-cases]] — what this article contributes to this concept
- [[2025-11-28_contextual-menus-guidelines]] — what this article contributes to this concept
- [[2025-12-05_vague-prototyping]] — what this article contributes to this concept
- [[2025-12-12_explainable-ai]] — what this article contributes to this concept
- [[2025-12-18_web-ux-study-guide]] — what this article contributes to this concept
- [[2026-01-09_humanizing-ai]] — Humanization represents a deliberate design choice with measurable costs; effective AI design instead emphasizes clarity, efficiency, and realistic boundaries.
- [[2026-04-24_ai-chatbots-design-guidelines]] — Focuses on interaction patterns that reduce friction, support user scanning, and make chatbots feel responsive and efficient.
- [[2024-01-23_laws-of-ux_02-a-brief-history-of-psychology-and-design]] — The interdisciplinary field combining psychology, systems analysis, and computer science that emerged during the Cold War, fundamentally shaped by psychological research into how humans think and learn.
