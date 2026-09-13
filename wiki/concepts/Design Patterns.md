---
type: concept
name: Design Patterns
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Design Patterns for AI"
  - "Interaction Patterns"
  - "Web Design Patterns"
---

# Design Patterns

## Definition

A design pattern is a standardized, reusable solution to a design problem that
recurs across interfaces: pagination, breadcrumbs, form validation, accordions,
progress indicators, and the like. Patterns sit at the tactical end of a
hierarchy of design guidance, below design principles (high-level value
statements that align a team) and usability heuristics (research-backed rules
of thumb for evaluating any interface), and alongside team charters that govern
how the team works; their function is to create consistency across the parts of
a product and to cut design and development time [[2025-04-18_design-guidance]].
Patterns are not free-standing inventions but reusable answers governed by
usability principles, spanning the full UI spectrum — input controls, forms,
navigation, search, error handling, privacy [[2024-02-09_design-pattern-guidelines]].
Some are revivals rather than novelties: the card component is the 1990s
hypertext deck-of-cards model adapted to responsive multi-card layouts
[[2016-11-06_cards-component]].

What gives a pattern its power is repetition on the user's side, not the
designer's. Well-practiced interactions consume fewer cognitive resources, so
users rely on learned patterns instead of conscious deliberation, and they carry
those mental models into every new interface they meet
[[2017-12-10_practiced-patterns-mistakes]]. The same logic explains why some
arrangements feel self-explanatory: natural mappings and cultural metaphors
("up is more", "green is go", spatial layouts that mirror the thing they
control) let people bridge the gulf of execution with almost no learning
[[2018-10-14_natural-mappings]]. That dependence on prior learning is also the
liability. A design that mimics a familiar pattern but deviates slightly makes
users apply the learned pattern anyway and miss the difference, producing errors
they never notice; the safe options are to comply fully with the convention or
to depart from it completely and obviously
[[2017-12-10_practiced-patterns-mistakes]]. Because guidelines are grounded in
human behaviour rather than technology, they age slowly, and a pattern should be
judged on its underlying principle rather than dismissed as dated
[[2024-02-09_design-pattern-guidelines]]; foundational patterns such as
hamburger menus, button states and carousels stay relevant but need their best
practices refreshed [[2025-12-19_top-videos-2025]], and new visual styles like
Neobrutalism have to be validated for usability rather than adopted as trends
[[2025-12-12_top-articles-2025]].

## Practice

### Deciding whether a pattern applies to you

Patterns observed at large companies are not portable by default. Giants operate
in different brand contexts, run continuous experiments, and discard many
released designs after monitoring them, so an outside observer cannot tell a
tested design from a guess: Google reverted minimalist single-line input fields
to enclosed boxes after testing, Amazon replaced decorative menu backgrounds
with high-contrast text, and Apple's low-contrast pricing text falls short of
accessibility minimums. Test the solution with your own users before building on
it [[2020-01-19_risks-imitating-designs]]. The same caution applies across
platforms: mobile-first must not become mobile-only, and hidden navigation
imported to desktop measurably degrades discoverability, task time and perceived
difficulty [[2016-06-26_hamburger-menus]]. Familiarity also moderates the choice
of an unusual pattern — the initial learning cost can outweigh the theoretical
efficiency gain unless users will use the control many times
[[2016-05-08_expandable-menus]].

### Selection and input controls

Match the control to the number of options and the nature of the data. Dropdown
lists hide options behind a click, cost three steps to operate and offer almost
no information scent; prefer radio buttons below roughly 5–7 options, a
filterable combobox above 15, plain text input for data users already know
(ages, birthdates, heights), and visible button layouts when users must compare
variants or see what is out of stock. Dropdowns remain justified for a moderate
5–10 options, secondary fields, or fields that must stay visually compact
[[2026-07-17_dropdown-list]]. Input steppers are the relative counterpart: they
fit fields with a clear default that users adjust only slightly, and they fail
for wide ranges or continuous quantities, where text input is needed; combining
a stepper with a text field gives both small adjustments and precise entry, and
buttons must be large and well spaced to respect Fitts' Law
[[2018-11-11_input-steppers]]. Cards group heterogeneous content into
self-contained, clickable units and enlarge the touch target, but they are
weaker than vertical lists for scanning and searching, and poor for
side-by-side comparison [[2016-11-06_cards-component]].

Buttons carry their own state vocabulary: enabled, disabled, hover, focus and
pressed, extended by loading and selected. Each state must be visually distinct,
and the feedback timing matters — roughly 150–200 ms of hover delay to avoid
accidental triggers, focus visible within 100–150 ms of a tab press, pressed
feedback within 100–150 ms or users click again. Style (primary, secondary,
tertiary) communicates hierarchy and is independent of state
[[2025-04-25_button-states-communicate-interaction]]. Disabled buttons in
particular confuse users by looking clickable while doing nothing; use them
sparingly and explain why they are disabled
[[2025-12-19_top-videos-2025]].

### Menus and navigation

Expandable menus pose two problems: making the handle discoverable with good
information scent, and minimising selection time (visual search plus movement).
Linear menus are fastest to their first item and slowest to their last;
rectangular megamenus cut average distance; pie/radial menus equalise distance
but lose their advantage to unfamiliarity; marking menus add an expert shortcut
and suit touch and contextual use. On touch, the finger is no longer where the
handle was once the menu opens, so placement must account for hand reach
[[2016-05-08_expandable-menus]]. Hidden navigation such as the hamburger is
measurably worse than visible or combo navigation on both phone and desktop, and
worse on desktop [[2016-06-26_hamburger-menus]]. Contextual menus should hold
secondary, low-priority actions only; kebab (⋮) and meatball (⋯) icons read as
"more options" and must be used consistently, kept large, high-contrast and
visible without hover, placed near the content they affect, and labelled or
tooltipped — hamburger icons stay reserved for global navigation, and these
overflow icons should trigger actions, never expand text or images
[[2025-11-28_contextual-menus-guidelines]]. Footers are a genuine navigation
surface, not leftovers: users scroll to them deliberately, as a second chance or
a last resort. Always include utility links (contact, customer service, privacy,
terms), repeat global navigation as doormat navigation on long pages, limit
depth to first- and second-level categories, use conventional link names
("Contact Us" rather than "Resources"), and keep footers legible rather than
hidden behind animation or accordions [[2019-02-24_footers]]. Utility controls
belong where users look for them: language switchers in the top corners on
desktop, above the fold or in the navigation on mobile where the top-right is
taken by account or cart [[2022-03-27_language-switching-ecommerce]].

### Interruption, disclosure and instruction

Modal dialogs are a system mode change: they block background content, impose
cognitive load, and add the extra goal of dismissal. They are warranted for
irreversible errors, for critical information required to continue a
user-initiated process, and for fragmenting a complex workflow — though a
dedicated page often beats a multi-step modal. They must never carry marketing,
upsells or unrelated content, which erodes trust and dulls attention to future
modals, and never interrupt high-stakes flows such as checkout
[[2017-04-23_modal-nonmodal-dialog]]. Info tips follow the same discipline: the
encircled "i" signals optional information and "?" signals help and support;
tips should clarify jargon or explain why data is requested, never hide
essential instructions, constraints, form limits or legal disclaimers, never
hijack focus with modals or full-page takeovers, and never serve as a
decluttering device for a layout that needs redesigning
[[2026-01-23_info-tips-bad]]. Onboarding deserves the same scepticism: avoid it
where possible and invest in a more learnable interface instead, test a
no-onboarding version first, move feature promotion to the app store, gather
only content-level setup data rather than visual customisation, avoid
deck-of-cards tutorials that make a simple app look complex, and prefer
contextual overlays and interactive walkthroughs when instruction is genuinely
needed [[2020-06-21_mobile-app-onboarding]]. Scroll fading is a distinct pattern
(not scrolljacking) with narrow good uses: fade in fast (100–400 ms, and text
slower than 500 ms risks being scrolled past uncomprehended), let elements
persist rather than re-animate, fade one element type at a time, watch for the
illusion of completeness it creates, and avoid it on mobile
[[2023-12-08_scroll-fading-101]].

### Icons, labels and ambiguity

Icons should not be assumed self-evident: recognition (identifying the shape)
and interpretation (deciding what it means) both vary widely across
populations, few icons are genuinely universal, and icon sets should be built
and validated from research rather than intuition [[2024-09-06_digital-icons-ux-quiz]].
The X icon is the standing example of a convention that never resolved its own
meaning — users read it as either close (non-destructive) or cancel
(destructive), and the ambiguity costs them work. The three remedies are a
confirmation before a destructive dismissal, explicit text labels (Cancel, Done,
Apply, Clear) in place of the icon, or defaulting to save-and-close with a
separate cancel button; long-running processes should auto-save on dismissal,
and there should always be a distinct emergency exit
[[2019-09-01_cancel-vs-close]]. Complex multi-finger gestures fail for the same
reason as opaque icons: they have no visible relationship to their outcome, so
they are hard to discover and to remember [[2018-10-14_natural-mappings]].

### Patterns for specific domains

Calculator and quiz tools form a pattern family of their own, split into
conversion, prediction and recommendation calculators, which can be chained to
carry users from understanding a situation to a suggested next step; trust
varies by type, and users trust complex prediction tools more precisely because
they cannot question the algorithm [[2024-04-12_3-types-calculator]]. Users
approach them with low initial commitment, entering rough estimates to test the
tool's worth, resist registration during exploration, expect more detail to
yield more accurate results, and work the tool both forward and backward
[[2024-03-22_calculator-expectations]]. The corresponding recommendations:
include calculator keywords in page titles, embed the tool in the page rather
than a popup, require only essential inputs, allow anonymous use with immediate
on-page results, let users change one input without re-entering the rest,
explain why each input is needed, contextualise the output, avoid misleading
defaults, and consider exposing how the result is calculated — trust comes from
perceived reliability and usefulness, not from using AI
[[2024-04-19_recommendations-calculator]]. Livestream ecommerce has its own
interface vocabulary — product lists, chat areas, reaction buttons,
picture-in-picture, on-demand product replay, tiered coupons and loyalty levels
— built on existing platforms and designed mobile-first
[[2021-02-28_livestream-ecommerce-china]]. Cross-device collaboration pairs a
helper channel with a target channel (QR-code login, phone camera inserting a
photo into a laptop presentation) to cut interaction cost or add capability;
it is optional rather than required for a good omnichannel experience, and
cross-ecosystem versions such as drag-and-drop between Microsoft and Google
apps remain inconsistent because the pattern needs broad adoption to work
[[2021-04-25_omnichannel-collaboration]]. For AI products, the recommended
pattern runs against the anthropomorphic default: position the AI truthfully as
a competent tool rather than a friend, narrow the feature scope, ground answers
in retrieval, stay transparent about limitations, and favour professional
interactions in finetuning — perceived intelligence raised users' willingness
to accept AI advice while perceived emotion lowered it, and warmth-tuned models
showed 10–30% higher error rates
[[2025-09-19_smarts-emotion-trust-ai]]. Generative UI, which builds personalised
interfaces in real time, pushes the field from static design toward dynamic,
user-specific interaction [[2025-12-19_top-videos-2025]].

### Inclusion, autonomy and the health of the pattern set

Inclusive-design patterns come out of empathy with diverse needs and accept
multiple variations rather than one universal solution: name fields without
character restrictions, demographic questions allowing multiple selections,
large type with high contrast and user-controlled font size, filters that
reflect real user diversity (hair pattern, age range), and illustrations that
depict varied skin tones and features [[2022-01-30_inclusive-design]]. Autonomy
patterns give people room to work their own way through surface-level
customisation (themes), task-related customisation (view options, zoom),
scannable content that lets them choose what to read, and flexible timing and
sequencing — balanced by a few meaningful options and strong defaults rather
than forced customisation [[2022-04-17_increase-user-autonomy]]. Left
unattended, inconsistent or expedient patterns become UX debt whose cost
compounds: users abandon the product and do not return, negative accounts
persist online, behaviour adapts to the bad design so that fixing it later
provokes resistance, and repeatedly changing components damages perceived
coherence. Surface debt through monthly usability testing, support reports,
surveys and retrospectives; prioritise it on a user-value-versus-effort matrix;
and allocate recurring story points or cleanup sprints so it is reduced rather
than deferred [[2018-11-11_ux-debt]]. Guidance itself should be organised by use
case ("checkboxes vs. radio buttons", "tooltips, dialogs and instructional
overlays") and issued in several formats — articles, videos, checklists — so
teams can find the relevant pattern quickly; it increasingly has to cover
privacy and ethics, including cookie permissions, passwordless authentication
and deceptive or dark patterns [[2024-02-09_design-pattern-guidelines]].

## Sources (31)

- [[2016-05-08_expandable-menus]] — The article examines menu patterns (linear, rectangular, pie, marking) and how they support different interaction contexts and user expertise levels.
- [[2016-06-26_hamburger-menus]] — Designers should not uncritically adopt mobile patterns on desktop; instead, each platform should leverage its unique capabilities to create optimized user experiences.
- [[2016-11-06_cards-component]] — Cards represent a modern revival of the classic deck-of-cards hypertext model, adapted for multi-card responsive layouts.
- [[2017-04-23_modal-nonmodal-dialog]] — Discusses how modals function as system mode changes, affecting what commands work and what users can do; related to affordances and user mental models.
- [[2017-12-10_practiced-patterns-mistakes]] — Recurring, established solutions to common design problems; users learn patterns through repetition and transfer this knowledge to new interfaces; deviating from established patterns creates friction and errors.
- [[2018-10-14_natural-mappings]] — recurring solutions like the use of cultural metaphors and spatial arrangement to create interfaces that are self-explanatory and require minimal learning.
- [[2018-11-11_input-steppers]] — when to use relative controls like steppers versus absolute controls like text input, and how to combine them for optimal flexibility.
- [[2018-11-11_ux-debt]] — recurring UX problems that accumulate across products and how to prevent and remediate inconsistent or poor patterns that degrade user experience.
- [[2019-02-24_footers]] — Common footer variations including infinite scroll mini footers and contextual footers that adapt to user roles and page context.
- [[2019-09-01_cancel-vs-close]] — The X-as-close/cancel pattern is a widespread convention that creates usability problems; designers must actively disambiguate through confirmation, labeling, or saving strategies.
- [[2020-01-19_risks-imitating-designs]] — Shows that design patterns from successful companies must be evaluated for applicability to your context rather than adopted wholesale.
- [[2020-06-21_mobile-app-onboarding]] — deck-of-cards tutorials, instructional overlays, and interactive walkthroughs as onboarding patterns with guidance on appropriate use cases.
- [[2021-02-28_livestream-ecommerce-china]] — the article documents design patterns specific to livestream ecommerce interfaces including product lists, chat areas, and reaction buttons.
- [[2021-04-25_omnichannel-collaboration]] — the article documents specific interaction patterns that enable collaboration across devices.
- [[2022-01-30_inclusive-design]] — Inclusive-design patterns emerge from deep user empathy; examples include flexible name inputs, demographic options allowing multiple selections, readable fonts with size controls, and filters reflecting user diversity.
- [[2022-03-27_language-switching-ecommerce]] — best practices for positioning and designing controls that users expect to find in specific locations.
- [[2022-04-17_increase-user-autonomy]] — repeatable solutions for providing choices and flexibility while maintaining usability and consistency.
- [[2023-12-08_scroll-fading-101]] — scroll fading is a distinct design pattern that differs from scrolljacking and should be applied selectively with clear design purposes.
- [[2024-02-09_design-pattern-guidelines]] — reusable solutions to common interaction problems, governed by usability principles.
- [[2024-03-22_calculator-expectations]] — establishes patterns for calculator and quiz design that align with user expectations and usage behaviors.
- [[2024-04-12_3-types-calculator]] — categorizes calculator types as distinct design patterns serving different user needs.
- [[2024-04-19_recommendations-calculator]] — establishes 12 specific design patterns and best practices for calculator tool implementation.
- [[2024-09-06_digital-icons-ux-quiz]] — the application of established iconographic conventions and visual communication standards across interfaces.
- [[2025-04-18_design-guidance]] — identifies standardized solutions for recurring design problems, reducing design time and maintaining consistency.
- [[2025-04-25_button-states-communicate-interaction]] — documents button state patterns as standardized solutions for communicating interaction availability and feedback.
- [[2025-09-19_smarts-emotion-trust-ai]] — Recommends positioning AI truthfully as a tool, narrowing feature scope, prioritizing sourcing (RAG), maintaining transparency about limitations, and selecting professional interactions during finetuning.
- [[2025-11-28_contextual-menus-guidelines]] — what this article contributes to this concept
- [[2025-12-12_top-articles-2025]] — what this article contributes to this concept
- [[2025-12-19_top-videos-2025]] — Core patterns like hamburger menus, disabled buttons, and carousels remain relevant but require ongoing best-practice updates.
- [[2026-01-23_info-tips-bad]] — Info tips are a specific UI pattern with established best practices; misuse undermines both their effectiveness and user trust.
- [[2026-07-17_dropdown-list]] — for selection include radio buttons (few options), comboboxes (long lists), text input (familiar data), and buttons (visual comparison), each suited to different contexts than dropdowns.
