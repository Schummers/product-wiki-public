---
type: concept
name: Error Prevention
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Slip (Error)"
---

# Error Prevention

## Definition

Error prevention is the design principle that a system should be built so errors
are unlikely in the first place, rather than merely recoverable after the fact. It
is one of Nielsen's ten usability heuristics, and it is achieved through clear
labeling, differentiation of options, visual signifiers and structural safeguards
[[2018-01-16_error-prevention]]. Its starting premise is that the design, not the
operator, is accountable: a good UI makes it hard for people to err, and easier to
recover from any errors that remain [[2018-01-16_error-prevention]]. The
principle is not tied to a modality; most usability principles have more to do
with human capabilities and limitations than with technology, and error prevention
applies just as much to voice-only systems as to screens
[[2016-01-31_voice-interaction-ux]].

The central object is the slip: an unintended action, where a user wants one thing
but takes another, usually similar, action on autopilot. Slips are distinct from
mistakes, which are conscious but wrong choices, and they require design-level
prevention rather than user blame [[2018-01-16_error-prevention]]. Slips are made
possible by how expertise works: a well-practiced task requires fewer cognitive
resources, so users apply automatic processing, and when an interface mimics a
familiar pattern but deviates slightly, they apply the learned pattern and never
notice the difference [[2017-12-10_practiced-patterns-mistakes]]. Because attention
is minimal on practiced tasks, these errors often go unnoticed and therefore
uncorrected [[2017-12-10_practiced-patterns-mistakes]].

## Practice

### Design for the inattentive user

Designers often overlook that the user may not be paying full attention to their
design [[2021-02-14_proximity-consequential-options]]. Users doing repetitive work
rely on automatic System 1 thinking and respond to preattentive visual and spatial
cues before conscious System 2 thinking engages, which is precisely why
consequential options placed next to benign ones invite accidental clicks
[[2021-02-14_proximity-consequential-options]]. Divided attention has the same
effect from a different cause: serial task switching fragments cognitive resources
across activities and increases mistakes in both
[[2025-05-23_serial-task-switching]].

### Differentiate consequential from benign options

The Hawaiian false missile alert is analysed as a design failure, not operator
negligence: PACOM and DRILL-PACOM were cryptic, similar labels sitting side by
side, requiring excessive mental effort to tell apart; clearer labels such as
"Test Alert" and "Live Alert", or grouping, would have prevented the confusion
[[2018-01-16_error-prevention]]. Live and test workflows on the same screen create
dangerous proximity; the recommendation is structural separation with different
modes, visual distinctions and an explicit action required to enter live mode
[[2018-01-16_error-prevention]].

The same problem recurs across contextual menus, dropdowns, dialogs, error
messages and wizards, where delete, block or mute sit beside benign options, and a
suggested spelling correction sits next to "Add to Dictionary"
[[2021-02-14_proximity-consequential-options]]. Two remedies are proposed:
visual redundancy, using color, icons, text size and alignment to signal which
option is destructive; and spatial separation, placing consequential actions
farther away so that, by Fitts's Law, the extra motor movement time acts as a
safety buffer [[2021-02-14_proximity-consequential-options]]. The precedent cited
is industrial: Alphonse Chapanis solved B-17 pilots confusing the landing-gear and
wing-flap levers by changing one lever's shape, so pilots could tell by touch which
one they held, signalling intent without conscious attention
[[2021-02-14_proximity-consequential-options]].

### Respect or fully break established patterns

Users' mental models, built through repetition, guide where they look; when a
design deviates from the model, they focus on the wrong screen areas and miss
important information [[2017-12-10_practiced-patterns-mistakes]]. The hazard is
selective: hot-potato scanning and banner blindness make users systematically
ignore relevant content their model says should not be there
[[2017-12-10_practiced-patterns-mistakes]]. Subtle variation is the dangerous case,
for instance a Filter button styled like a Search Submit button. The prescription
is binary: either comply fully with the established pattern, so users can transfer
their existing mental model, or depart completely and obviously, forcing conscious
processing and new learning [[2017-12-10_practiced-patterns-mistakes]].

### Confirmation dialogs, used sparingly

Confirmation dialogs give users a genuine second chance before a dangerous or
irreversible operation, but only if users actually read them
[[2018-02-18_confirmation-dialog]]. Overuse defeats the purpose: frequent dialogs
train users to dismiss them habitually, and a bare "Are you sure you want to do
this?" invites an automatic yes, since the only sensible reaction is that of
course they want to do what they just asked for
[[2018-02-18_confirmation-dialog]]. The same warning appears in the missile-alert
analysis, where confirmation screens that become habitual roadblocks may simply not
be noticed [[2018-01-16_error-prevention]].

The guidance that follows: restate the user's request with identifying details
(filenames, quantities) so a mistake is recognisable; trigger dialogs only for
serious consequences such as destroying work or large financial transactions, not
routine actions; use action-specific button labels ("Delete file" / "Keep file")
rather than Yes and No, and avoid a default yes on dangerous operations; and for
extremely dangerous operations require a nonstandard action, such as typing a
confirmation word as MailChimp does, reserved for rare situations
[[2018-02-18_confirmation-dialog]]. For critical actions specifically, one source
argues confirmation should be more intrusive, for instance re-entering a password,
to force conscious attention [[2018-01-16_error-prevention]].

### Prevention through in-flight feedback

Microinteractions are trigger-feedback pairs that can catch problems before
submission: password-requirement indicators, validation feedback and undo
affordances guide users to correct input up front, preventing the frustration of
repeated failed submissions [[2018-10-21_microinteractions]]. They also carry
system status, so users know whether an action was recognised and whether further
input is needed [[2018-10-21_microinteractions]]. In voice interfaces, prevention
moves partly into hardware and scope: the Echo's seven microphones and
background-noise filtering make recognition more reliable in real conditions such
as a noisy kitchen, and its deliberately narrower functionality reduces error rates
and semantic misinterpretation compared with an assistant biased toward general web
search [[2016-01-31_voice-interaction-ux]].

### Recovery is part of prevention

Undo capability is treated as a companion requirement rather than a separate topic:
authorization to take an action should include authorization to undo it, and where
undo is not technically possible a recovery workflow should exist. The missile
alert had no way to rescind a sent message [[2018-01-16_error-prevention]]. Offering
undo is also recommended as a way to reduce anxiety and let users recover from
major problems, under the user control and freedom heuristic
[[2018-02-18_confirmation-dialog]]. For attention-fragmented contexts, the named
safety net is confirmation dialogs, undo options and autosaving, which help users
recover from mistakes induced by divided attention
[[2025-05-23_serial-task-switching]].

### Multi-step, real-world processes

Prevention also applies off-screen, to service design. The Massachusetts
vote-by-mail packet asked voters to place one envelope inside another without
explaining it clearly, buried key information in places suggesting it was not
critical (a footer), gave instructions as dense text without images, and referred
to envelopes by colour rather than clear labels or numbers matched to each step
[[2020-10-25_mail-ballot-usability]]. Nearly 18,000 votes were rejected in
Massachusetts in October as a result, with the further consequence of voters
feeling compelled to vote in person during a pandemic
[[2020-10-25_mail-ballot-usability]]. The method the source implies is
anticipatory: work out where in a complex multi-step process users are likely to
err, then design instructions, labels and visual cues to stop it happening
[[2020-10-25_mail-ballot-usability]].

### A defense-in-depth stance

Critical systems call for layered protection: prevention, then confirmation, then
recovery, because no single layer is sufficient
[[2018-01-16_error-prevention]]. The layers also constrain each other, and the
sources are consistent about the trade-off: warn too much and people stop paying
attention [[2018-02-18_confirmation-dialog]], which is why the heavier safeguards
are reserved for the genuinely consequential actions and the lighter differentiation
work (labels, color, spacing, defaults) carries the everyday load
[[2021-02-14_proximity-consequential-options]], [[2018-01-16_error-prevention]].

## Sources (8)

- [[2016-01-31_voice-interaction-ux]] — background noise rejection, command recognition reliability, and semantic disambiguation are all error-prevention mechanisms.
- [[2017-12-10_practiced-patterns-mistakes]] — An unintended action that occurs when users intend one action but inadvertently take another, often because automatic processing is applied to a changed interface or slightly varied pattern.
- [[2018-01-16_error-prevention]] — A design principle emphasizing that systems should make errors unlikely by guiding users when they intend one action but might take another (on autopilot); distinct from mistakes (conscious but wrong choices); achieved through clear labeling, differentiation of options, visual signifiers, and structural safeguards.
- [[2018-02-18_confirmation-dialog]] — using confirmation dialogs strategically to catch serious user errors before they cause irreversible harm.
- [[2018-10-21_microinteractions]] — using microinteractions like validation feedback and confirmation prompts to help users avoid mistakes and reduce the need for error recovery.
- [[2020-10-25_mail-ballot-usability]] — anticipating where voters might make mistakes in a complex multi-step process and designing clear instructions, labels, and visual cues to prevent them from occurring.
- [[2021-02-14_proximity-consequential-options]] — applies industrial design principles to prevent unintentional destructive actions through shape, color, and spatial design.
- [[2025-05-23_serial-task-switching]] — features like confirmation dialogs, undo options, and autosaving that help users recover from mistakes induced by divided attention.
