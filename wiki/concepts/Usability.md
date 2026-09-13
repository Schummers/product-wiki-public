---
type: concept
name: Usability
created: 2026-07-31
updated: 2026-07-31
status: developed
---

# Usability

## Definition

Across these sources, usability is the property of an interface that lets people
complete their tasks with little effort, few errors and an accurate
understanding of what the system is doing. It is treated less as a single
attribute than as the aggregate of a series of concrete choices — which control
to use for a numeric field, whether the active mode is visible, whether an icon
can be read in one fixation, whether feedback reaches the user through the right
channel — each of which is judged by its effect on effort, speed and error rate.
Two sources anchor it to Nielsen's heuristics in particular: visibility of system
status is the heuristic invoked both by [[2019-04-14_modes]] (mode errors violate
the first heuristic) and by [[2024-01-17_indicators-validations-notifications]]
(keeping the state of the system visible is one of the ten usability heuristics).

The delight literature in this corpus positions usability structurally.
[[2017-03-05_theory-user-delight]] places it in Aarron Walter's hierarchy of user
needs — functionality, reliability, usability, then delight — and states flatly
that a product can be delightful only if it is usable; delight cannot be skipped
ahead to. [[2022-11-27_pillars-user-delight]] refines rather than contradicts
this: usability is the *behavioral* pillar of delight, necessary but not
sufficient, standing alongside the visceral (aesthetic) and reflective
(value-aligned) pillars, and a design strong on only one leg is unstable.
[[2021-05-16_pain-points]] draws the boundary from the other side: usability
issues are the interaction level of a three-level model, with journey-level and
relationship-level pain points sitting above them — pain points encompass
usability issues but extend beyond them.

## Practice

### Treat usability as a precondition, not a finishing layer

- [[2017-03-05_theory-user-delight]] argues that beautiful but non-functional
  products fail: aesthetic qualities go unappreciated without function, and
  surface delight (animations, transitions, snarky microcopy, high-resolution
  imagery, sound) applied to an unusable interface reads as non-genuine, can
  damage brand trust and wastes the investment. Negativity bias compounds this,
  since users remember bad experiences more than good ones. Its notion of deep
  delight — the interface behaving like a surgeon's knowledgeable assistant,
  handing over the right instrument at the right moment without getting in the
  way — is described as requiring streamlined workflows and reduced pain points,
  that is, as an outcome of usability work rather than an alternative to it.
- [[2022-11-27_pillars-user-delight]] cautions against reading that hierarchy as
  a licence to stop at usability: interaction design, service design and journey
  management contribute to delight as much as visual design, function should be
  defined around long-term user needs rather than short-term task completion,
  and qualitative research (contextual inquiry, interviews, diary studies) is
  needed to see the emotional side that metrics miss.

### Make system state and available actions visible

- **Feedback channels.** [[2024-01-17_indicators-validations-notifications]]
  separates three mechanisms and warns that mismatching them harms usability:
  *indicators* are passive, contextual, conditional visual cues (icon,
  typography, size, animation) that flag something worth attention; *validations*
  are error messages tied to a specific input that require correction;
  *notifications* alert to system events and split into action-required
  (interrupting, modal) and passive (toast, badge). Passive notifications used for
  critical errors get missed; modal notifications used for passive information
  frustrate; indicators should not carry critical feedback. The choice is driven
  by information type, urgency, and whether user action is required.
- **Modes.** [[2019-04-14_modes]] defines a mode as a state in which the same
  input produces different results, useful when many commands must be reached
  through few input methods, but a source of mode slips when users cannot tell
  which mode is active — the article cites a 1991 crash where the same control
  set either the degree or the speed of descent depending on an insufficiently
  clear mode. Its guidance: use at least two independent, redundant visual
  signals (for instance highlighting plus a cursor change) so the active mode is
  obvious to an inattentive user; expect reduced discoverability, since
  mode-specific features are hard to find and re-find, especially for occasional
  users; treat modal windows as a mode, justified only when the user must
  interact before continuing; and where mixing modes up can cause real harm, use
  separate controls instead.
- **Recognition over recall.** [[2016-08-21_direct-manipulation]] presents direct
  manipulation — acting on displayed objects through physical, incremental,
  reversible actions with immediately visible effects — as supporting usability
  precisely by making objects and available actions visible, so users recognize
  what they can do instead of recalling syntax, and learn faster than with a
  command line. It also names the limits: only visible objects can be acted on,
  physical actions cost effort and can cause repetitive strain injury, some
  actions fail silently with no feedback, experts doing repetitive work prefer
  keyboard shortcuts, and direct-manipulation interfaces can fail visually or
  motor-impaired users in ways that are hard to work around.

### Choose controls by task, range and input modality

- **Input steppers.** [[2018-11-11_input-steppers]] fits them to fields with one
  commonly entered default that users adjust only slightly — passenger count,
  cart quantity — where a change from 1 to 2 costs a single tap instead of
  focusing a field, typing and dismissing a keyboard. They are wrong for wide
  ranges (1 to 50 means excessive clicking) and for continuous quantities like
  prices or distances, which need typed input. Buttons must be large and
  well-spaced, since tiny or crowded targets violate Fitts's Law and produce
  misclicks; horizontal steppers generally beat vertical ones, especially on
  mobile; and pairing a stepper with a text field covers both small adjustments
  and precise entry.
- **Split buttons.** [[2019-05-12_split-buttons]] describes the same trade-off in
  reverse: a default action plus a menu of alternatives lowers interaction cost
  for the frequent case and reduces visual complexity, but the hidden menu costs
  discoverability, especially for people still learning the application. The
  arrow must be visually separated from the label by a dividing line or contrast
  and always visible, never revealed on hover; text labels (not icons alone)
  improve learnability and enlarge the target. The source rules split buttons out
  for touchscreens, because Fitts's Law makes the small arrow target slow and
  error-prone, and out for navigation, where a standard dropdown is the right
  pattern. Persistent variants, where the last selection becomes the new default,
  help power users but break spatial consistency for new ones.

The two sources agree on the underlying method: match the control to the
expected range of values and to the input modality, and combine controls rather
than forcing one to cover every case.

### Do not let decoration add cognitive load

[[2017-11-19_bad-icons]] applies a cost-benefit test to a single interface
element: an icon costs design, research and iteration time, coding and QA, screen
real estate, and potential clutter, so its benefit must exceed all of that. Bad
icons reuse an established meaning for something else (a star for templates
rather than ratings), rely on esoteric references that demand inference, are
blurry or under-detailed, repeat needlessly on every item in a list, or only make
sense as a set. Good ones map a concept naturally onto a picture, stay simple,
require no decoding, are understood in a single fixation, and survive at small
sizes; used well they are faster than text for familiar, repeated tasks and,
combined with a word, enlarge the click target. The source also names why bad
icons proliferate — breaking up text-heavy pages, adding interest to link
clusters, following a trend — which are designer motives, not user benefits.

### Find and prioritize usability problems

[[2021-05-16_pain-points]] gives the research counterpart: interaction-level pain
points, that is usability issues, are identified through usability testing and
prioritized by impact, frequency and likelihood of recurrence, while journey-level
problems need interviews, diary studies and journey mapping, and
relationship-level problems need benchmarking surveys, analytics and behavioral
tracking. Every pain point has a cost — interaction cost and cognitive load for
usability problems, time, money, and eroded trust further up — and the source
argues that pain points, rather than arbitrary feature requests, should drive
design change, while conceding that it is not cost-efficient to solve all of them.

Several other sources describe defects that only such testing surfaces, because
they are invisible from the design file: an action that fails with no feedback at
all ([[2016-08-21_direct-manipulation]]), a menu users never notice behind a
split-button arrow ([[2019-05-12_split-buttons]]), a mode slip by an inattentive
user ([[2019-04-14_modes]]), or an icon whose reference the designer finds
obvious and the user has to decode ([[2017-11-19_bad-icons]]).

## Sources (9)

- [[2016-08-21_direct-manipulation]] — Direct manipulation supports usability through immediate feedback, reduced learning requirements, and recognition-based action selection.
- [[2017-03-05_theory-user-delight]] — presented as the foundation upon which delight must be built; cannot be skipped or assumed.
- [[2017-11-19_bad-icons]] — examines how poor icon design increases cognitive load and reduces task efficiency.
- [[2018-11-11_input-steppers]] — how control design affects the ease and speed of completing input tasks, particularly for users on mobile devices or systems without keyboards.
- [[2019-04-14_modes]] — Mode errors violate Nielsen's first heuristic and are especially problematic in safety-critical systems or when consequences are severe.
- [[2019-05-12_split-buttons]] — Fitts's Law applies to split-button arrows; small targets require more precision and time, making split buttons unsuitable for touchscreen interfaces.
- [[2021-05-16_pain-points]] — Interaction-level pain points are usability issues identifiable through testing and prioritized by severity, frequency, and impact.
- [[2022-11-27_pillars-user-delight]] — usability is the behavioral pillar of delight; while necessary, it is not sufficient alone; interaction design, service design, and journey management contribute equally to delight as visual design.
- [[2024-01-17_indicators-validations-notifications]] — one of Nielsen's heuristics is system visibility; choosing appropriate feedback mechanisms is essential for usability.
