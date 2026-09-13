---
type: concept
name: Customization
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Interface Customization"
  - "User Preferences and Customization"
---

# Customization

## Definition

Customization is tailoring done **by the user**: the user actively makes
selections and sets preferences to shape the content, layout, functionality or
design of a system to their own needs
[[2016-07-10_customization-personalization]]. The sources define it in
opposition to personalization, which is tailoring done **by the system** — the
system identifies the user and adjusts what it shows, either by predefined role
or by an individual model. The trade-off between the two is control versus
effort: customization lets users get exactly what they want because they are in
control, while personalization improves the experience without demanding
anything of them but depends on the system guessing correctly
[[2016-07-10_customization-personalization]], [[2016-10-02_personalization]].

Its value is framed in terms of autonomy — the ability to use an interface in
ways that align with personal preferences and priorities, treated as a
fundamental human need [[2022-04-17_increase-user-autonomy]] — and in terms of
efficiency, since letting people adapt an interface to their own work habits is
one of the levers of the flexibility-and-efficiency-of-use heuristic
[[2020-11-22_flexibility-efficiency-heuristic]]. The recurring caveat across
the corpus is that customization costs the user work, so many customization
features simply go unused [[2016-08-14_customization]].

## Practice

### Customization vs. personalization: choose deliberately, or offer both

Personalization is system-driven and effortless for the user but is only ever a
best guess; customization is user-driven, accurate by construction, but
requires initiative that not all users will supply
[[2016-07-10_customization-personalization]]. One source argues explicitly for
providing both, so that the convenience of system-driven adaptation is balanced
by user-held control [[2016-10-02_personalization]] — which in practice means
explicit controls such as view-as features, universal access options, and the
ability to override personalized settings, all treated as essential to
preventing frustration and maintaining trust.

A rule both sources state flatly: **neither is a fix for a broken experience**.
Customization and personalization should enhance an already-good baseline, not
rescue poor structure or unclear content, and neither can compensate for weak
information architecture [[2016-07-10_customization-personalization]],
[[2016-08-14_customization]].

### Making customization actually get used

Because customization requires work and input from users, it has to be designed
to entice usage and to pay off the effort invested. Features go unused when
users do not know they exist, find them too complex, or judge the baseline good
enough that customizing is not worth it [[2016-08-14_customization]]. Practical
guidance from that source:

- **Show that it exists** — place customization links near the related content
  and name them clearly so their function is obvious.
- **Make it easy** — one-click or minimal-step configuration is adopted far more
  than multi-step processes.
- **Layer it with progressive disclosure** — surface only the most useful or
  common options, defer the rest to an "advanced" area.
- **Provide a clear benefit** — customization must solve a real problem;
  customization for its own sake does not drive adoption.
- **Encourage gently over time** — nudge users toward it as they gain
  familiarity, and let them change earlier selections later, which increases
  long-term adoption and satisfaction.

The same low-uptake observation recurs elsewhere: most users will not customize
without strong motivation [[2020-11-22_flexibility-efficiency-heuristic]], and
surface-level customizations in particular are rarely used
[[2022-04-17_increase-user-autonomy]]. The consequence both draw is the same —
defaults must work well for most people on their own, and customization is
offered on top rather than relied upon
[[2020-11-22_flexibility-efficiency-heuristic]],
[[2022-04-17_increase-user-autonomy]].

### Types of customization

- **Surface-level** (themes, colours): provides delight and a sense of
  ownership without altering the workflow, though it is rarely used
  [[2022-04-17_increase-user-autonomy]].
- **Task-related** (view options, zoom controls): helps users adapt the
  interface to shifting needs [[2022-04-17_increase-user-autonomy]].
- **Workspace and workflow** (screen arrangements, workspace configuration,
  settings): aimed at expert users matching the system to their own work habits
  [[2020-11-22_flexibility-efficiency-heuristic]].

Customization is one of three autonomy methods in
[[2022-04-17_increase-user-autonomy]], alongside scannable content (so users
choose what to read in detail rather than reading everything or leaving) and
flexible timing and sequencing (some users want onboarding, others want to jump
straight in).

### Customization for expert users

In the flexibility-and-efficiency heuristic, customization sits next to
accelerators as a way of resolving the novice–expert tension: rather than
optimising for one group, provide multiple methods of doing a task and
unobtrusive shortcuts that novices need not see but experts can discover — for
example showing keyboard shortcuts next to menu items
[[2020-11-22_flexibility-efficiency-heuristic]]. The same source adds a limit:
avoid duplicating functionality in several places, because users then have to
learn differences that may not exist.

Personalizing **functionality** rather than only content is the system-side
counterpart: autofill known information (with the ability to edit it), remember
frequent selections and searches, save progress in long workflows, and let
sessions continue seamlessly across devices [[2016-10-02_personalization]].

### Granular control as a defence against fatigue

The smart-home case makes customization a condition of the system surviving at
all: users need granular control over notification types, thresholds, channels
and timing, and without it they abandon the entire notification system
[[2026-02-20_smart-home-notifications]]. Concretely, that source's frequency
principle recommends letting users set event thresholds (notify at 20% battery
rather than 50%), filter by event type (people, not insects), and set repeat
intervals, while separating discrete events from ongoing conditions. Its
relevance principle sets the default: alert only for the core purpose by
default, allow customization on top, and auto-expire notifications when the
issue resolves itself.

### Balancing choice against usability

Autonomy has to be balanced against usability: offer a few meaningful options
with strong defaults rather than forcing customization or drowning users in
choice overload [[2022-04-17_increase-user-autonomy]]. On the personalization
side, the equivalent restraint is to assign roles conservatively — past
behaviour does not reliably predict future needs, and tagging too narrowly
produces inaccurate, restrictive experiences — to add or reshuffle content
rather than remove access, and to create only as many roles as the team can
actually maintain [[2016-10-02_personalization]]. Both sides also require
thoughtful design so the tailoring machinery does not add complexity to the
baseline experience [[2016-07-10_customization-personalization]].

## Sources (6)

- [[2016-07-10_customization-personalization]] — Customization empowers users to control their experience but requires user effort and initiative; not all users will engage with customization options.
- [[2016-08-14_customization]] — Successful customization requires strategic implementation, clear benefits, ease of use, and strong baseline experiences.
- [[2016-10-02_personalization]] — Emphasizes the difference between system-driven personalization and user-controlled customization, and the importance of providing both to balance convenience with control.
- [[2020-11-22_flexibility-efficiency-heuristic]] — allowing expert users to customize interface arrangements, settings, and workflows to match their unique needs and work habits, though designing defaults that work well for most users.
- [[2022-04-17_increase-user-autonomy]] — allowing users to adapt interfaces to personal preferences and needs.
- [[2026-02-20_smart-home-notifications]] — Users need granular control over notification types, thresholds, channels, and timing; allowing customization prevents abandonment of entire notification systems.
