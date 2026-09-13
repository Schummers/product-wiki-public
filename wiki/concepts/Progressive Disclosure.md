---
type: concept
name: Progressive Disclosure
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Accès progressif à l'information"
---

# Progressive Disclosure

## Definition

Progressive disclosure is showing only what a user needs at a given moment and
revealing the rest on demand or at a later step. The sources apply it along two
axes: **sequentially**, splitting a long task into steps so that less information
is presented at a time ([[2017-06-25_wizards]],
[[2025-07-18_4-principles-reduce-cognitive-load]],
[[2025-09-12_smart-device-onboarding]]); and **in depth**, keeping the common
case in the primary view and pushing secondary options or supplemental
explanation into an "advanced" area or an on-demand tip
([[2016-08-14_customization]], [[2026-01-23_info-tips-bad]]). In both cases the
stated payoff is the same: less cognitive load, fewer errors, more confidence.

What makes it a design problem rather than a simple rule is the second half of
the bargain. Hidden content still has to be *findable*, and several sources are
about what happens when it is not: the illusion of completeness, where a screen
looks finished and users never scroll or swipe to what lies beyond
([[2016-01-17_illusion-of-completeness]], [[2021-07-18_principle-closure]]).
Deferring content therefore obliges the designer to leave a visible signal that
more exists, and to be honest about what is optional. Where a source draws that
line varies: [[2026-01-23_info-tips-bad]] is emphatic that essential content
must never be deferred at all, while [[2016-08-14_customization]] treats
layering as a way to keep depth available without overwhelming anyone.

## Practice

### Break a long task into steps

- **Wizards.** [[2017-06-25_wizards]] defines a wizard as a step-by-step process
  in a prescribed order where later steps may depend on earlier answers, and
  names showing less information at a time as its core benefit over a
  comprehensive single-page form: lower cognitive load and fewer errors. It
  recommends wizards for novice users and infrequent tasks and warns against them
  for frequent, expert work, where step-by-step becomes tedious. Its design rules
  are practical: show the full list of steps and highlight the current one;
  enforce sequential completion rather than letting users skip ahead; label
  buttons with the actual next step ("Choose Fabric") instead of a generic
  "Next"; make each step self-sufficient so users never have to look back at
  earlier data; put help beside the wizard, never over it; allow saving and
  resuming; and reuse prior values as defaults for repeat users. The same source
  is candid about the costs — more clicks, blocked access to information,
  reduced user control, poor interruptibility, and difficulty comparing data
  across steps — and suggests offering a faster alternative to people who run
  the process repeatedly.
- **Forms.** [[2025-07-18_4-principles-reduce-cognitive-load]] lists progressive
  disclosure under its Structure principle: break a long form into multiple pages
  or manageable sections, and show only the fields made relevant by previous
  answers. It pairs this with transparency — communicate estimated time, required
  materials and deadlines upfront, and show progress indicators — so that
  splitting the task does not leave users unable to see what they are getting
  into.
- **Setup flows.** [[2025-09-12_smart-device-onboarding]] applies the same
  pattern to smart-device connection: one task at a time in a visual wizard,
  supported by images, animations and clear text, builds confidence better than
  text-only instructions or several simultaneous tasks. Because these tasks are
  infrequent, users rarely remember the steps, so reconnection after a power or
  WiFi outage deserves the same visual guidance as first-time setup. Two caveats
  from that source bear on staged reveals generally: progress indicators must be
  honest, since a bar that fills without reflecting real progress destroys trust;
  and each step should tell users what to expect physically (beeps, blinking
  lights) so they can tell whether the device is responding.

### Layer optional depth

- [[2016-08-14_customization]] recommends showing only the most useful or common
  customization options first and deferring secondary ones to an "advanced"
  section, so the feature offers depth without overwhelming the majority. It also
  bounds the technique: customization tools cost the user effort, so the payoff
  must be clear, and a layered options panel cannot rescue a weak baseline
  experience — a good default is still the primary obligation.
- [[2026-01-23_info-tips-bad]] treats info tips as progressive disclosure done
  well *when* they surface the essential upfront and reveal only supplemental
  detail on demand: clarifying jargon, explaining why a piece of data is
  requested, or pointing to further information. Its distinction between icons is
  part of the signal — the encircled "i" means optional helpful information,
  the "?" means help and support.
- [[2025-07-11_saving-scroll-position]] touches the same idea from the
  navigation side, showing basic content first and revealing details through
  interaction; its main concern is that this pattern produces pogo sticking
  between a list and detail pages, and that failing to restore the user's scroll
  position on return raises interaction cost. It advises preserving the position
  within a session (roughly 30–60 minutes), resetting when content updates in
  real time or much time has passed, choosing the least disruptive default when
  intent is ambiguous (preserve, plus an easy "jump to latest"), and animating
  the change when the position is reset.

### Never hide what users actually need

[[2026-01-23_info-tips-bad]] is the corpus's strongest statement of the limit:
info tips are not a catch-all for decluttering an interface by sweeping essential
content into a hidden layer. Essential instructions, constraints, form limits and
legal disclaimers must stay visible; hiding them turns guidance into
hide-and-seek. Redundant, obvious or promotional tips waste the interaction cost
of opening them. Modals, overlays and full-page takeovers hijack focus, so tips
belong inline or adjacent where users can read them while keeping context. And
the working assumption should be that most users never open a tip — design for
the motivated minority who are confused or stuck, and fix poor labelling or dense
layouts by redesigning rather than by adding tips.

[[2016-08-14_customization]] makes the parallel point for deferred options:
users often will not bother to customize even when the interface is clear and
simple, so a good experience cannot depend on their having gone looking.

### Signal that more exists

Deferred content is only disclosed if something invites the next action.

- [[2016-01-17_illusion-of-completeness]] documents the failure: when the visible
  screen looks complete, users stop. Full-screen hero videos or graphics with
  strong calls-to-action are a common cause — in one usability study, six of
  eight users did not scroll past a hero video because nothing indicated content
  below. Distinct full-width horizontal lines, expansive white space between
  sections and large advertisements act as false floors. Horizontally, carousels
  give too little signal: small dot indicators do not communicate more content,
  and users do not expect horizontal scrolling on desktop or reliably guess at
  swiping on mobile. Its remedies are content peeking off the screen edge,
  headlines that name the carousel's frames, salient arrow controls, slide counts,
  explicit continuation copy when an ad interrupts the flow ("Read past this ad"),
  and testing across device sizes.
- [[2021-07-18_principle-closure]] supplies the perceptual mechanism: because
  people automatically fill in partially visible objects, showing only part of a
  carousel item or deliberately segmenting elements above the fold makes the page
  read as incomplete and invites scrolling or swiping. The same source sets the
  constraint — enough of the cut-off element must remain on screen to communicate
  its value and function, otherwise there is nothing for the viewer to complete.

### Keep the ordinary path available when the interface adapts

[[2025-02-11_364_Intent_Driven_Design,_la_méthode_pour_une_UX_moderne_à_l_heure_de_l_IA]]
positions progressive access to information as a safeguard for interfaces that
adapt themselves to inferred user intent: because the system's reading of intent
can be wrong, the personalized action is suggested while the classic path stays
available, which limits the frustration a misinterpretation would otherwise
cause. The same source ties this to a modular, block-based information
architecture, so elements can be shown or hidden by context without building new
pages.

## Sources (11)

- [[2016-01-17_illusion-of-completeness]] — relates to revealing information gradually; hero content and interruptions disrupt progressive disclosure by hiding or obscuring continuation signals, preventing users from discovering deeper page content.
- [[2016-08-14_customization]] — Layering customization features prevents overwhelming users while still offering depth for those who want it.
- [[2017-06-25_wizards]] — showing less information at a time to prevent overwhelm, a core benefit of wizards over comprehensive single-page forms.
- [[2021-07-18_principle-closure]] — The principle of closure supports progressive disclosure by allowing designers to hint at additional content through partial display, encouraging users to interact and discover more information.
- [[2025-02-11_364_Intent_Driven_Design,_la_méthode_pour_une_UX_moderne_à_l_heure_de_l_IA]]
- [[2025-07-11_saving-scroll-position]] — The article mentions showing basic content first and revealing details through interaction, applicable to how scroll position relates to information architecture.
- [[2025-07-18_4-principles-reduce-cognitive-load]] — Breaking long forms into multiple pages or showing only relevant fields based on previous answers reduces overwhelm by presenting only necessary information.
- [[2025-09-12_smart-device-onboarding]] — Shows how revealing information one step at a time, with feedback cues about device responses, reduces cognitive load and builds user confidence during complex connection processes.
- [[2026-01-23_info-tips-bad]] — Info tips exemplify progressive disclosure when done well: surfacing essential info upfront, revealing supplemental details on demand.
- [[2024-01-23_laws-of-ux_06-4-hicks-law]] — revealing choices, information, and features gradually over time rather than presenting all options simultaneously.
- [[2024-01-23_laws-of-ux_11-9-teslers-law]] — An interaction design technique revealing only essential actions by default, with additional features accessible through dropdowns, accordions, or toggles. Reduces cognitive load and interface clutter while deferring advanced functionality.
