---
type: concept
name: Fitts's Law
created: 2026-09-10
updated: 2026-09-10
status: stub
aliases:
  - "User Interface Positioning"
---

# Fitts's Law

## Definition

Fitts's Law states that the time to acquire a target is a function of the
distance to it and its size: movement time grows with distance and shrinks as
the target gets bigger ([[2022-07-31_fitts-law]],
[[2024-01-23_laws-of-ux_04-2-fittss-law]]). The relationship is logarithmic
rather than linear, so time increases at a slower rate than distance does
([[2022-07-31_fitts-law]]); Yablonski gives Fitts's index of difficulty as
ID = log₂(2D/W), with D the distance and W the target width
([[2024-01-23_laws-of-ux_04-2-fittss-law]]).

The law was formulated by psychologist Paul Fitts in the 1950s (1954, per
[[2024-01-23_laws-of-ux_04-2-fittss-law]]) to describe human motor control in
physical tasks, and transfers directly to pointing and tapping in digital
interfaces. Its mechanism is a two-phase movement: a fast initial phase that
covers the distance, then a slower phase in which the pointer decelerates so as
not to overshoot. The second phase is driven mostly by target size, which is
why small targets cost proportionally more time
([[2022-07-31_fitts-law]]). Yablonski situates the law's origin in wartime
aviation crashes caused by pilots confusing identical controls, and treats it
as a founding result of [[Human Factors Engineering]]: adapt the technology to
human limits rather than the reverse ([[2024-01-23_laws-of-ux_04-2-fittss-law]]).

## Practice

### Make targets bigger before making them closer

Increasing target size reduces interaction time more effectively than bringing
the target nearer ([[2022-07-31_fitts-law]]). A practical consequence is to
pair icons with labels: the icon-plus-label area is larger than the icon alone,
so it is faster to acquire.

On minimum sizes, [[2024-01-23_laws-of-ux_04-2-fittss-law]] cites industry
guidelines from 44 × 44 CSS pixels (WCAG) up to 60 × 60 points (Apple spatial
interfaces), and insists these are floors: exceed them wherever possible to
reduce the precision the interface demands. See [[Tap Area]].

### Space targets apart

Crowded targets increase accidental overshooting and mis-clicks, especially
when the targets are small; spacing is needed beyond the active click area
itself ([[2022-07-31_fitts-law]]). The book gives the anthropometric basis and
a number: the MIT Touch Lab measured average adult fingertips at 16–20 mm in
diameter, and Google Material Design recommends at least 8dp between targets to
prevent activation of a neighbour ([[2024-01-23_laws-of-ux_04-2-fittss-law]]).

### Exploit screen edges

A target on a screen edge behaves as an infinite target: the boundary stops the
pointer from overshooting, so it can be acquired quickly without a precision
penalty. Both sources use the same illustration — operating systems park menus,
menu bars, taskbars and docks at the edges, macOS placing the application menu
along the top edge and Windows (through Windows 8) the Start button in the
bottom-left corner ([[2022-07-31_fitts-law]],
[[2024-01-23_laws-of-ux_04-2-fittss-law]]).

### Position for the device and the hand

Place controls where the user can actually reach them accurately, tuned to the
form factor and the context of use. On smartphones, accuracy is highest at the
centre of the screen; Apple's Reachability gesture exists to pull items from
the top of the screen into the lower half for one-handed use
([[2024-01-23_laws-of-ux_04-2-fittss-law]]).

### Menu shape changes the average distance

Menu structure is a Fitts's Law problem, because the layout sets the mean
distance to an item: rectangular menus are more efficient than linear ones, and
pie menus put every option at an equal distance, though users find them
unfamiliar ([[2022-07-31_fitts-law]]). See [[Menu Design]] and
[[Direct Manipulation]].

### Method note

The same research programme produced more than the law. The source describes
Fitts and Chapanis's approach — reading the crash data, then interviewing the
pilots — as an early form of contextual inquiry, and it is what revealed that
the crashes were systematic rather than individual pilot error
([[2024-01-23_laws-of-ux_04-2-fittss-law]]).

## Sources (2)

- [[2022-07-31_fitts-law]] — A quantitative law explaining how movement time depends on distance and target size, foundational for optimizing UI interaction speed.
- [[2024-01-23_laws-of-ux_04-2-fittss-law]] — foundational principle quantifying the relationship between target size, distance, and selection time in user interfaces; strategic placement of controls in areas where users can reach them accurately, optimized for device form factor and use context.
