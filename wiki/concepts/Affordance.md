---
type: concept
name: Affordance
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Affordance in Design"
  - "Signifiers"
  - "Visual Affordance"
---

# Affordance

## Definition

An affordance, as the sources use the term, is the perceivable cue — the
signifier — that tells a user what actions are possible and what will happen
when they take one [[2025-07-04_floppy-disk-icon-understandability]]. Its job is
to bridge the Gulf of Execution, the gap between what a user intends and what
the system will actually accept: in a graphical interface, visible signifiers
such as distinctive colours for clickable text let people understand at a glance
what is possible, and research shows that diminishing those signifiers produces
slower task times and click uncertainty
[[2017-09-10_audio-signifiers-voice-interaction]].

Two properties recur across the sources. First, a signifier has to be
perceivable at all: hidden interaction is forgotten interaction, and "out of
sight is out of mind" applies as fully to gestures as to any other hidden UI
element [[2017-12-03_iphone-x]]. Second, a signifier has to be *accurate* — it
must reflect the actual system behaviour, not merely be recognisable. Familiarity
does not guarantee appropriateness; the best icon is the one that accurately
reflects what is going to happen
[[2025-07-04_floppy-disk-icon-understandability]]. Where the visual channel is
unavailable, as in voice, the same function has to be carried by audio
signifiers instead [[2017-09-10_audio-signifiers-voice-interaction]].

## Practice

### Invisible interactions carry a learning cost

Gestures have no visual representation, which makes them hard to remember and
hard to discover; apps that implemented nearly all their functionality through
gestures with almost no graphical UI, such as Clear Todos and Mailbox, were
praised by the design community and failed with general users
[[2017-12-03_iphone-x]]. The iPhone X compounds this with swipe ambiguity: the
same swipe produces different outcomes depending on its location, length, and
direction, forcing users to spend cognitive resources on remembering
gesture-specific contexts [[2017-12-03_iphone-x]].

The source identifies two mitigations rather than a fix. One is a residual
visual signifier: the home line at the bottom of the screen acts as a reminder
for the swipe-up gesture, and is credited with preventing the kind of complete
usability failure that followed Windows 8's reliance on invisible gestures. The
other is forced repetition — unlike a website gesture a user meets once, the
home swipe is practised constantly, so the initial friction is eventually
absorbed. The trade-off is judged worthwhile only because the screen real estate
gained is genuinely valuable and because a strong brand can carry users through
the learning cost [[2017-12-03_iphone-x]].

### Icons as signifiers: pick the standard one, and test it

A quantitative test of accordion signifiers on mobile compared a caret, a plus,
a right-facing arrow, no icon, and a foil control
[[2020-08-23_accordion-icons]]. Findings:

- The downward caret was the safest choice, significantly outperforming the
  alternatives at conveying that content would expand in place rather than
  navigate away.
- The right-facing arrow was not statistically different from no icon or from
  the foil at signalling accordion behaviour — users neither expected to stay on
  the page nor to leave it, contrary to designer assumptions.
- The plus icon performed adequately but was not significantly better than no
  icon at conveying that the page would stay put.
- Inventing new icons, or using none, violates user expectations; standard
  signifiers convey intent better than foils or absence.

The same study delivers a structural rule: users tap fairly equally on the icon
and on the text label for every condition except the caret, so split-button
designs that assign different functions to icon and label are unsafe — users
expect both to do the same thing [[2020-08-23_accordion-icons]]. And when no
icon was present at all, users gravitated to the text label rather than empty
space, showing a preference for whatever obvious signifier exists
[[2020-08-23_accordion-icons]].

### Recognisability is not appropriateness

The floppy disk icon is recognised by 83% of participants as meaning "save", 96%
if storage answers are included, yet that recognition rests on interface
familiarity — consistent repeated exposure — and not on familiarity with the
physical object [[2025-07-04_floppy-disk-icon-understandability]]. The icon has
shifted from a resemblance icon to a reference icon, sustained by consistency.
The problem is on the behaviour side: saving now covers syncing, auto-saving,
exporting, versioning, and downloading, so the metaphor of writing to a
removable medium diverges from what the system actually does. The source's
position is that the icon still works in enterprise and complex-application
contexts where stability is valued, but may send the wrong signal in cloud-based
interfaces, and that context-appropriate selection means matching the visual
metaphor to the actual user action
[[2025-07-04_floppy-disk-icon-understandability]].

Read together with the accordion study, the two sources pull in slightly
different directions: one shows that adopting the standard, widely recognised
signifier is the safest bet [[2020-08-23_accordion-icons]], the other that wide
recognition alone is not sufficient grounds to keep a signifier whose meaning
has drifted from system behaviour
[[2025-07-04_floppy-disk-icon-understandability]].

### Signal the current state, not just the action

A control that toggles between two states has to communicate two things at once:
what state the system is in now, and what pressing it will do
[[2020-10-18_state-switch-buttons]]. A mute button that fails at this leaves
users unable to tell whether they are muted or about to be. The recommended
solutions, in order of safety:

- **Two controls** — one element indicating the current state, a separate button
  showing what will happen (the Tesla app unlock example).
- **One control, carefully labelled** — the label states what will happen next,
  the icon changes with the next state, or the active state is marked by a
  visual signifier such as a shadow. This works only if the shadow is
  recognisable as a signifier for "active".
- **Never colour alone** — colour carries multiple meanings across interfaces
  and users do not reliably remember the association; the source's own account
  describes missing a red icon entirely while panicking about being muted.

Context can substitute in part: external cues such as sound or visual feedback
may let a single control suffice, but determining state quickly under time
pressure requires an explicit indicator
[[2020-10-18_state-switch-buttons]].

### Affordances without a screen

In voice interfaces the signifier has to be audible, and the sources describe
three forms with different trade-offs
[[2017-09-10_audio-signifiers-voice-interaction]]: nonverbal earcons
(distinctive beeps), which are ambiguous, need context or repeated exposure, and
work best for confirmations in narrow repetitive tasks; explicit verbal cues
that state the available options, the most understandable but ineffective in
long lists because people forget the early options by the time they hear the
later ones; and implicit verbal cues such as appending "ok?" or "sound good?",
which hint that a correction is possible without enumerating everything. Because
listening to a signifier takes longer than scanning a menu, audio affordances
must be rationed — via guessing intent when the system has enough information,
progressive disclosure, and sequential cues — especially for secondary or easily
reversible commands [[2017-09-10_audio-signifiers-voice-interaction]].

## Sources (5)

- [[2017-09-10_audio-signifiers-voice-interaction]] — in voice contexts, sound-based cues (earcons), explicit verbal suggestions, and implicit verbal hints guide users to available commands.
- [[2017-12-03_iphone-x]] — Visible design cues (like the home line) signal to users how to interact; absence of affordances for gesture-based actions creates discoverability and learning problems.
- [[2020-08-23_accordion-icons]] — Clear, recognizable signifiers are critical for helping users understand what will happen when they interact with UI elements. Users expect icon and label to work together rather than having separate functions.
- [[2020-10-18_state-switch-buttons]] — making the current state and available actions visually obvious through consistent design patterns and clear signifiers so users understand what they can do and what will happen.
- [[2025-07-04_floppy-disk-icon-understandability]] — visual cues that suggest what actions are possible and what will happen when actions are taken, challenged when icon meaning diverges from system behavior.
