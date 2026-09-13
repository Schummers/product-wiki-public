---
type: concept
name: Animation
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Animation Design"
  - "Animation Timing"
  - "Animation Usability"
  - "Animation in UX"
---

# Animation

## Definition

Animation is motion in an interface. The sources treat it above all as a
communication device rather than an ornament: motion attracts attention because
peripheral vision is evolutionarily attuned to detect movement, and that single
property is what makes animation both useful and dangerous
[[2020-01-12_animation-purpose-ux]]. Used deliberately, it provides feedback
that an action was registered, communicates a state change, supports spatial
navigation, and acts as a signifier for what an element can do. Used for
delight or entertainment, the same sensitivity to motion turns into
distraction, perceived slowness, and in some cases physical discomfort.

The recurring position across the corpus is restraint. Scroll-triggered text
animations delay access to information [[2017-04-16_scroll-animations]],
parallax is admired by designers but ignored or disliked by ordinary users
[[2019-01-20_parallax-usability]], animated GIFs in marketing email test worse
than static versions [[2020-03-15_gif-emails]], and scroll fading introduces
discoverability problems of its own [[2023-12-08_scroll-fading-101]]. Quality
in animation is a matter of execution detail — duration, easing, entrance
versus exit — where tens of milliseconds change how the interface feels
[[2020-02-09_animation-duration]].

## Practice

### Use animation for a purpose, not for delight

Animation should primarily provide noticeable, smooth feedback that the system
has recognised an action, help users notice state changes they would otherwise
miss through change blindness, communicate direction and position inside a
hierarchy (zoom-in/zoom-out metaphors, slide-over transitions), and signal what
actions an element affords, such as the direction it can be swiped
[[2020-01-12_animation-purpose-ux]]. Gratuitous animation overwhelms and
distracts; motion should stay subtle, unobtrusive and brief. The email study
reaches the same conclusion empirically: animation is acceptable when it serves
a clear purpose such as demonstrating a product feature, while excessive and
meaningless movement is read by recipients as a gimmick or a cheap
attention-seeking tactic [[2020-03-15_gif-emails]]. Compelling content and
clear messaging matter more than animated flash — animating a boring email does
not make recipients appreciate it.

### Timing and motion characteristics

Most animations belong in the 100–500 ms range [[2020-02-09_animation-duration]]:

- Simple feedback such as a toggle: about 100 ms, so it feels immediate.
- Substantial screen changes: 200–300 ms.
- At 500 ms or more, animation reads as a delay and becomes cumbersome.
- Entrance and exit are asymmetric: objects entering the screen typically need
  longer (around 300 ms) than objects leaving (200–250 ms).

Easing is what makes motion feel natural, since linear motion appears
unnatural: ease-out (fast start, slow end) works best for elements entering,
ease-in for elements exiting, and ease-in-out feels less responsive on
entrance. Small details matter disproportionately — the difference between
250 ms and 300 ms is perceptible. For scroll fading specifically, fade-in
should be fast, in the 100–400 ms band, because text fading in slower than
500 ms risks users scrolling past before they have comprehended it
[[2023-12-08_scroll-fading-101]]. The perceived-delay threshold is low in
general: users notice even one extra second, and multiple animations compound
the impression of slowness [[2017-04-16_scroll-animations]].

Specify animations to developers as timelines carrying every detail — elements,
triggers, transition types, durations in milliseconds, easing curves — rather
than handing over a video file, and expect platform-specific easing notation
(cubic-Bezier for CSS, named curves for iOS and Android)
[[2020-02-09_animation-duration]].

### Scroll-triggered animation

Scroll-triggered effects are the corpus's main cautionary case.

- Main body text should load immediately, without artificial delay; reserve
  scroll-triggered effects for secondary, supporting elements such as images or
  graphic elements [[2017-04-16_scroll-animations]].
- Animate once. Effects should fire on the first scroll to a position and leave
  the content permanently available afterwards; replaying them — including
  re-animating objects when the user scrolls back up — frustrates task-oriented
  users [[2017-04-16_scroll-animations]], [[2019-01-20_parallax-usability]],
  [[2023-12-08_scroll-fading-101]].
- Repetition destroys whatever delight exists: seeing the same effect across
  multiple pages wears patience down and the novelty effect disappears
  [[2017-04-16_scroll-animations]].
- Fading content in below the fold can trigger an illusion of completeness — a
  page that already looks finished, thanks to whitespace, leads users to assume
  nothing else exists [[2023-12-08_scroll-fading-101]].
- Fade one element type at a time, and combine scroll fading with concise,
  punchy writing and adequate data loading, since the pattern often accompanies
  lazy loading and breaks visibly when images fail to load
  [[2023-12-08_scroll-fading-101]].
- Tying animation to scroll speed removes user control: scroll too fast and the
  content is missed, scroll slowly and you are made to wait
  [[2019-01-20_parallax-usability]].
- Avoid scroll fading on mobile altogether: smaller screens increase scroll
  fatigue and worsen the illusion of completeness, so desktop issues are
  amplified [[2023-12-08_scroll-fading-101]]. Parallax has a parallel mobile
  problem — the user's hands can block the animation
  [[2019-01-20_parallax-usability]].

### Context decides

Appropriateness depends on the site and the user's mindset. Task-focused
contexts (medical, financial, B2B) with goal-oriented users should avoid
scroll-triggered animation entirely; leisure contexts (entertainment, casual
browsing) have more room for visual effects [[2017-04-16_scroll-animations]].
Parallax is judged the same way: most defensible in leisure browsing without a
specific goal, least defensible on task-focused or information-heavy pages
[[2019-01-20_parallax-usability]]. Goal-oriented users scroll quickly, scanning
for keywords, and simply miss animated content; content presented solely
through animation may never be seen at all. Users have also learned to ignore
motion because they associate it with advertising, and may deliberately
disregard it.

### Accessibility and motion sensitivity

Excessive animation, flashing, parallax, scroll-jacking and carousel animation
can cause vestibular reactions — dizziness, nausea, migraines — and trigger
seizures in users with epilepsy; browser and OS "reduce motion" settings must
be respected [[2020-02-09_animation-duration]]. Motion overload from parallax
animating many text elements makes reading harder and can produce vertigo,
nausea and dizziness, which is what prompted Apple's iOS 7 "Reduce Motion"
option [[2019-01-20_parallax-usability]].

### Evidence against the assumed benefit

The email study is the corpus's hardest evidence that animation does not
automatically pay off. Across 121 respondents and 14 marketing emails, animated
versions drew 40% more negative word selections and 30% fewer positive ones
than static versions, with the biggest gaps on *annoying* (31% vs 14%),
*distracting* (20% vs 11%) and *dull* (20% vs 13%). Positive sentiment fell by
165%, from slightly positive (0.55) for static emails to negative (-0.36) for
animated ones, and static emails were rated more valuable (3.69 vs 3.24) and
more trustworthy (4.34 vs 3.90), the trust difference reaching statistical
significance [[2020-03-15_gif-emails]]. Parallax points the same way from
qualitative testing: it wins design awards yet draws indifferent reactions from
average users, who focus on content rather than animation
[[2019-01-20_parallax-usability]].

The sources are not uniformly negative, and the nuance is worth keeping: subtle
animation often goes unnoticed and can strengthen brand perception
[[2017-04-16_scroll-animations]], scroll fading is credited with guiding users
through long pages, lazy loading data, surfacing timely supporting information
and boosting brand credibility [[2023-12-08_scroll-fading-101]], and meaningful
subtle animation may still work even in email [[2020-03-15_gif-emails]]. The
disagreement is one of degree — how much benefit remains once the cost of
delay, distraction and motion sensitivity is subtracted.

## Sources (6)

- [[2017-04-16_scroll-animations]] — Explores when scroll-triggered animations enhance vs. harm UX, emphasizing balancing aesthetic appeal with content accessibility and task completion.
- [[2019-01-20_parallax-usability]] — Animations can support understanding or create distraction/harm; parallax represents a cautionary case where visual appeal to designers doesn't translate to user value.
- [[2020-01-12_animation-purpose-ux]] — Establishes that animation serves specific UX purposes and should be used sparingly as feedback and communication tools rather than for delight or entertainment.
- [[2020-02-09_animation-duration]] — Provides specific guidance on animation durations appropriate for different scenarios, from simple feedback to complex screen transitions.
- [[2020-03-15_gif-emails]] — provides empirical evidence that animations in email marketing violate UX principles about purposeful animation and distraction avoidance.
- [[2023-12-08_scroll-fading-101]] — scroll fading is a specific animation pattern triggered by user scrolling; understanding animation principles (duration, preattentive processing) is essential.
