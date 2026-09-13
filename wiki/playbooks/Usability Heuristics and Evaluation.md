---
type: playbook
name: Usability Heuristics and Evaluation
theme: Usability Heuristics and Evaluation
created: 2026-08-21
updated: 2026-08-21
status: active
sources_as_of: 2026-07-31
concepts:
  - Usability Heuristics
  - Heuristic Evaluation
  - Usability
  - User Experience
  - Learnability
  - Design Principles
  - Error Prevention
  - Aesthetic-Usability Effect
  - Benchmarking
---

# Playbook — Usability Heuristics and Evaluation

Checkable rules distilled from this theme's concept pages, for
`product-wiki-review`. Every rule carries its source. Give each one a verdict:
`holds`, `breached`, or `n/a` with a reason.

This is a **cache** of [[Usability Heuristics and Evaluation]], not a
replacement for it. `sources_as_of` records the concept pages' `updated` date;
when they move past it, re-distil. Open the concept page whenever a rule needs
its nuance or its exceptions.

Attribution runs to the record where the corpus gives it, and to the concept
page otherwise.

## The ten heuristics

**H1. Every interaction produces visible feedback, immediately.**
A lack of information reads to users as a lack of control. A button colour
change is enough for a small action; state changes are announced rather than
applied silently, and an item going out of stock is communicated, not quietly
removed. [[2018-06-03_visibility-system-status]]
*Long operations:* "please wait" is insufficient. Show percentage complete and
steps remaining so the user can decide whether to wait or switch tasks; a
success dialog reports what happened and links onward.
[[2021-08-15_usability-heuristics-complex-applications]]

**H2. The interface speaks the user's words, in the user's order.**
Specific familiar terms over system vocabulary, no unexplained jargon or
acronyms, and flows sequenced the way users expect. Never assume your reading
of a word matches theirs. [[2018-07-01_match-system-real-world]]
*Mechanism:* natural mapping. Controls correspond to their outcome, spatially
(layout mirrors the thing controlled), metaphorically ("up is more", and
culture governs whether it lands), or behaviourally. Multi-finger gestures
violate this: no discoverable relationship to their outcome.
[[2018-10-14_natural-mappings]]

**H3. There is always a way out.**
Undo, redo, save points, exit states, so people can experiment without
permanent consequence. [[2019-05-19_usability-heuristics-applied-video-games]]
Back and Cancel are critical wherever being trapped is costly.
[[2021-07-11_usability-heuristics-virtual-reality]] Defaults the user cannot
change are a breach. [[2019-05-19_tesla-big-touchscreen]]
*Weight it up* where users have invested cognitive effort: undo and version
history reduce the fear of exploring.
[[2021-08-15_usability-heuristics-complex-applications]]

**H4. Conventions are followed, internally and externally.**
Jakob's Law: users spend most of their time elsewhere and arrive with
expectations from there. Blue underlined text is clickable, logo top left,
magnifier means search. Consistency is required across visual treatment, page
and button layout, data formatting, and tone at once.
[[2021-01-10_consistency-and-standards]]
*Breaking a convention costs cognition,* so it is done only when the task
genuinely requires it or the efficiency gain is significant. One icon carrying
two meanings (a plus for both "add" and "expand") confuses daily users, not
only newcomers. [[2021-08-15_usability-heuristics-complex-applications]]

**H5/H9. Errors are prevented first, and recovery explains the fix.**
Proactive warning beats after-the-fact messaging. Confirmation before
destructive actions, clear mode indicators, unavailable options disabled,
real-time previews of what a change will do.
[[2021-07-11_usability-heuristics-virtual-reality]]
[[2021-08-15_usability-heuristics-complex-applications]]
When an error does occur, say what went wrong and how to fix it, without
blaming the user. [[2022-10-30_hostile-error-messages]]

**H5b. Validation waits for the user to finish.**
Premature validation scolds: an error on the first digit of a phone number,
"Invalid email address" after one letter, required-field errors before any
interaction. Validate format on blur or on submit. Reserve error styling (red,
caution symbols) for real errors. Mark a required field with **one** indicator,
an asterisk or the word "required", never asterisk plus icon plus red outline
plus inline message. Over-applying H5 and H9 this way breaches H8.
[[2022-10-30_hostile-error-messages]]

**H6. Options are visible rather than remembered.**
Recognition supplies retrieval cues that recall does not. Menus display
available commands where a command line demands recall; history, favourites,
wishlists and recently-viewed convert recall into recognition.
[[2024-01-15_recognition-and-recall]] Label every element rather than leaving
unlabelled icons behind tooltips.
[[2021-07-11_usability-heuristics-virtual-reality]]

**H7. Novices and experts are both served.**
Hotkeys and customisable controls let frequent users build a faster path
without penalising first-timers.
[[2019-05-19_usability-heuristics-applied-video-games]]
*Efficiency is task-dependent:* a modality can suit a short task and fail a
repetitive multi-step one. [[2016-01-31_voice-interaction-ux]]

**H8. Minimalism maximises utility, it does not strip elements.**
Remove noise, retain everything necessary: too few elements inhibits utility,
too many obscures what matters. Maximise signal, minimise decorative clutter
and unexplained jargon, and use progressive disclosure so uncommon features
appear when needed. [[2021-01-24_aesthetic-minimalist-design]]
*Aesthetics are functional here:* users judge design quality in about 50
milliseconds, faster than they can read.
[[2021-01-24_aesthetic-minimalist-design]]

**H10. Help exists and is organised.**
Documentation is not skippable even when tedious; clear organisation and
supporting video lower the barrier to first use.
[[2024-02-16_usability-heuristics-board-games]]

## Applying and evaluating

**E1. Learn the heuristics before the pattern guidance.**
They are the foundational layer beneath every specific rule for checkboxes,
forms, menus, search and error handling. [[2024-02-09_design-pattern-guidelines]]

**E2. The heuristics hold across modality and platform.**
They describe human capability and limitation rather than technology, and the
corpus tests this against voice, VR, video games, board games, car dashboards
and enterprise software, reporting each time that they transfer.
[[2016-01-31_voice-interaction-ux]] [[2024-02-09_design-pattern-guidelines]]
[[2021-07-11_usability-heuristics-virtual-reality]]
[[2021-08-15_usability-heuristics-complex-applications]]

**E3. A breach is a finding only when it was unintentional.**
Breaking a heuristic can improve the experience where the goal is recreation
rather than productivity: hidden information creates tension, high cognitive
load can be the challenge itself. The condition is that the violation is
deliberate. Unintentional failures harm both.
[[2024-02-16_usability-heuristics-board-games]]

**E4. Popularity is not evidence.**
The 3-click rule persisted with no support from any published study, and pushes
poor tradeoffs: three slow clicks are worse than five fast ones. What actually
drives navigation usability is information scent, wayfinding, mega menus that
expose several levels at once, and hubs at decision points, even when those
cost more clicks. [[2019-08-11_3-click-rule]]
*Distinguish this from age:* guidance rooted in human behaviour is not
discarded for being old. [[2024-02-09_design-pattern-guidelines]]

**E5. Attractiveness hides usability problems during evaluation.**
The aesthetic-usability effect means attractive designs are recalled as easier
to use even where real problems exist, so a polished artifact needs its
usability probed harder, not less. [[Aesthetic-Usability Effect]]

**E6. Inspection and user testing are complementary, not substitutes.**
Heuristic evaluation, expert review and cognitive walkthrough find different
problems from a usability test; neither replaces the other.
[[Heuristic Evaluation]]

**E7. Usability is a precondition, not a finishing layer.**
It is established before delight is added, and problems found are prioritised
rather than listed flat. [[Usability]] [[User Experience]]

**E8. Score against a baseline when the claim is improvement.**
An improvement claim needs a number from before the work. PURE is the cheaper
instrument when a full benchmark is out of reach. [[Benchmarking]]

## Where this theme stops

Component-level rules (which control, which menu shape, form layout) live in
[[Interaction and Interface Patterns]]. Layout and scanning live in
[[Page Composition and Hierarchy]]. Contrast, focus order and screen readers
live in [[Accessibility and Inclusion]].
