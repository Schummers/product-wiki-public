---
type: playbook
name: Interaction and Interface Patterns
theme: Interaction and Interface Patterns
created: 2026-08-21
updated: 2026-08-21
status: active
sources_as_of: 2026-07-31
concepts:
  - Interaction Design
  - Design Patterns
  - User Interface
  - Form Design
  - Modal Window
  - Feedback Design
  - Error Prevention
  - Error Messages
  - Notification Design
  - Affordance
  - Animation
  - Progressive Disclosure
---

# Playbook — Interaction and Interface Patterns

Checkable rules distilled from this theme's concept pages, for
`product-wiki-review`. Give each one a verdict: `holds`, `breached`, or `n/a`
with a reason.

A **cache** of [[Interaction and Interface Patterns]] (`docs/adr/0004`), not a
replacement. Open the concept page when a rule needs its nuance.

## Choosing a pattern

**I1. A pattern from a large company is tested on your own users before you
build on it.** Giants run continuous experiments and discard most of what they
try; an outside observer cannot tell a validated design from a guess. Google
reverted minimalist input fields after testing, Amazon dropped decorative menu
backgrounds. [[2020-01-19_risks-imitating-designs]]

**I2. A mobile pattern moving to desktop is questioned, not ported.**
Hidden navigation imported from mobile measurably degrades discoverability,
task time and perceived difficulty on desktop too.
[[2016-06-26_hamburger-menus]]

**I3. Deviating from a familiar pattern is done completely, or not at all.**
A near-miss makes users apply the learned pattern anyway and miss the
difference, producing errors they never notice.
[[2017-12-10_practiced-patterns-mistakes]]

## Selection controls

**I4. The control matches the option count and the data, not visual
compactness.** Radio buttons under ~5-7 options, a filterable combobox above
~15, plain text for data users already know (dates, ages), visible buttons
when users must compare variants. Dropdowns are justified for a moderate 5-10
options or a field that must stay compact. [[2026-07-17_dropdown-list]]

**I5. Checkboxes are zero-or-more, radio buttons are exactly one.**
Square with a checkmark for checkboxes, never circles. The label itself is
clickable, options list vertically, and selection limits are stated with
real-time feedback. [[2024-06-28_checkboxes-design-guidelines]]

**I6. An icon and its adjacent label always do the same thing.**
Tested directly: users tap the icon and the label at near-equal rates, so a
split control that assigns different functions to each is unsafe.
[[2020-08-23_accordion-icons]]

**I7. A button's style communicates hierarchy, its state communicates
availability, and the two are independent.** Five core states: enabled,
disabled, hover, focus, pressed, plus loading and selected. Hover carries
150-200ms delay against accidental triggers, focus appears within 100-150ms of
Tab, pressed within 100-150ms or users click again.
[[2025-04-25_button-states-communicate-interaction]]

## Signifiers

**I8. A signifier is perceivable before it is clever.**
Hidden interaction is forgotten interaction. Apps built almost entirely on
undiscoverable gestures (Clear, Mailbox) were praised by designers and failed
with general users. [[2017-12-03_iphone-x]]

**I9. A signifier is accurate, not merely familiar.**
The floppy-disk save icon is recognised by 96% of users, yet "save" today
covers sync, autosave, export and versioning — familiarity does not guarantee
the icon still describes what happens. Match the metaphor to the actual
action. [[2025-07-04_floppy-disk-icon-understandability]]

**I10. A toggle communicates current state and next action as two separate
facts.** The safest pattern is two controls: one shows the state, a separate
one triggers the change. A single control needs an unambiguous label or icon
change, and colour alone is never sufficient signal.
[[2020-10-18_state-switch-buttons]]

## Modals and overlays

**I11. A modal is used only after asking whether another pattern fits
better.** Nonmodal windows, accordions, tooltips, a plain sub-page: all named
as usually less intrusive. The corpus is consistently sceptical of the
pattern; modal ads rank among the most-hated ad formats.
[[2024-09-24_347_Fenêtre_modale,_le_Guide_UX_Design]]
[[2017-06-04_most-hated-advertising-techniques]]

**I12. When a modal is used, it opens only on a deliberate user action, for
one of three things: confirming an irreversible action, previewing an item, or
capturing a short form.** [[2024-09-24_347_Fenêtre_modale,_le_Guide_UX_Design]]

**I13. Modals never stack, and never carry marketing.**
Multiple consecutive modals overwhelm and signal poor design; unrelated
content in a modal erodes trust and dulls attention to future ones.
[[2019-06-30_popups]] [[2024-09-24_347_Fenêtre_modale,_le_Guide_UX_Design]]

**I14. Closing a modal is never ambiguous about what it does to the user's
work.** An X read as cancel destroys work the user thought was dismissed, not
abandoned. Confirm before a destructive dismissal, replace X with explicit
labels (Cancel, Done, Apply), or default to save-and-close with a separate
discard control. [[2019-09-01_cancel-vs-close]]

## Feedback

**I15. Every interaction confirms it registered, inside 100-150ms.**
Even a button colour shift prevents users wondering whether the action took.
Missing feedback produces repeated actions: users double-check by clicking
again. [[2018-06-03_visibility-system-status]]
[[2025-04-25_button-states-communicate-interaction]]

**I16. The feedback mechanism matches the message's urgency.**
Indicators (passive, contextual) for low-stakes cues, validations for input
errors, notifications for system events, action-required ones interrupting
only when urgency justifies it. A critical error in a passive channel gets
missed; a passive update in a modal frustrates.
[[2024-01-17_indicators-validations-notifications]]

**I17. A long wait shows its shape.**
Percentage complete, steps remaining, or a status animation, not a generic
"please wait" — so users can decide whether to wait or switch tasks.
[[2021-08-15_usability-heuristics-complex-applications]]

**I18. State changes are announced, never applied silently.**
An item going out of stock is communicated, not quietly removed.
[[2018-06-03_visibility-system-status]]

## Errors

**I19. Validation waits for the user to finish, not to start.**
An error on the first digit, or on form load before any interaction, reads as
scolding. Validate on field exit or submission.
[[2022-10-30_hostile-error-messages]]

**I20. An error message says what went wrong, why, and how to fix it, without
blaming the user.** Vague "something went wrong" strands people; blame-oriented
wording ("invalid", "incorrect") reframes the system's job as the user's
fault. [[2023-05-15_error-message-guidelines]]

**I21. Error styling is reserved for real errors.**
Red text, caution icons and warning symbols used for routine status
desensitise users and generate false alarms; one required-field indicator is
enough, never asterisk plus icon plus outline plus message.
[[2022-10-30_hostile-error-messages]]

**I22. The same error hit three times in one attempt is a design defect, not
a user error.** Treat it as a signal to fix the interface, not to add another
message. [[2019-02-03_errors-forms-design-guidelines]]

## Forms

**I23. Every field justifies its presence, or it is cut, deferred, or
inferred.** Each field removed raises conversion. Prefill from prior data or
SSO and let users verify rather than retype; infer city/state from ZIP, age
from birthdate. [[2016-05-01_web-form-design]]
[[2025-03-07_eas-framework-simplify-forms]]

**I24. Labels are persistent, never placeholder-only.**
Placeholder text disappears on typing and drops contrast.
[[2016-05-01_web-form-design]]

**I25. Required-field marking sits on the field, not only at the top of the
form.** A single top-of-form note is unreliable; users do not read it.
[[2019-06-16_required-fields]]

**I26. Reset and Clear buttons are dropped.**
The risk of accidental data loss outweighs their value. Cancel, where offered,
sits at much lower visual weight than Submit. [[2016-05-01_web-form-design]]

## Progressive disclosure

**I27. A long task is split into steps only for infrequent tasks or novice
users**, with a faster path offered to people who repeat it.
[[2017-06-25_wizards]]

**I28. Deferred content signals that it exists.**
A carousel needs more than dot indicators: edge-peeking content, a named
headline, visible controls. [[2016-01-17_illusion-of-completeness]]

## Notifications

**I29. A notification is classified by urgency before it is designed.**
Reactive (act now), proactive (prepare), optimisation (suggestion) each need
different timing, intensity and channel. [[2026-02-20_smart-home-notifications]]

**I30. Notification permission is asked for after the user has seen value,
never on first launch, and the ask names what it is for.**
A generic system prompt on first open gets declined by users who do not yet
trust the app. [[2018-11-18_push-notification]]

**I31. Disabling notifications is easy, inside the app, and granular by
type.** Hiding the control decreases trust; forcing all-or-nothing pushes users
to disable everything. [[2018-11-18_push-notification]]
[[2026-02-20_smart-home-notifications]]

## Animation

**I32. Animation is feedback first, delight second.**
Its productive uses: confirming an action registered, communicating a state
change, showing spatial position, signalling what an element affords.
[[2020-01-12_animation-purpose-ux]]

**I33. Most interface animation runs 100-500ms.**
Simple feedback around 100ms, substantial screen changes 200-300ms; past
500ms it reads as delay. Entrances take longer than exits (~300ms vs
~200-250ms). [[2020-02-09_animation-duration]]

**I34. Scroll-triggered animation runs once, never on scroll-back.**
Re-animating on re-encounter frustrates task-oriented users, and body text
never waits on an animation to appear. [[2017-04-16_scroll-animations]]

**I35. Motion respects the reduce-motion setting.**
Excessive animation, parallax and carousel motion can trigger vestibular
symptoms and seizures. [[2020-02-09_animation-duration]]

## Where this theme stops

Layout-level hierarchy and grouping live in
[[Page Composition and Hierarchy]]. Contrast, focus order and screen-reader
structure live in [[Accessibility and Inclusion]]. The ten Nielsen heuristics
that these patterns instantiate live in
[[Usability Heuristics and Evaluation]].
