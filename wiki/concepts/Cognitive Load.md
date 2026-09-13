---
type: concept
name: Cognitive Load
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Charge cognitive"
---

# Cognitive Load

## Definition

Cognitive load is the mental effort a person must spend to process information
and complete a task [[2025-05-23_serial-task-switching]]
[[2017-12-10_practiced-patterns-mistakes]]. Its physical substrate is working
memory, described as a limited-capacity buffer or scratchpad where the mind
deposits the information relevant to the current task, holding roughly seven
chunks for a brief period, with the exact capacity varying by individual,
education and age [[2018-04-29_working-memory-external-memory]]. When an
interface asks users to keep more in mind than the buffer can hold, they dump
information to make room, which produces errors and longer task times
[[2018-04-29_working-memory-external-memory]]. *Laws of UX* gives the same
capacity as Miller's 7 ± 2 but qualifies it twice: the figure varies with how
familiar, contextual and complex the content is, and it cites research putting
the average limit closer to four items [[2024-01-23_laws-of-ux_05-3-millers-law]]
[[Miller's Law]]. Its account of the failure mode adds abandonment to the list —
when incoming information exceeds working memory capacity, users struggle, miss
details, and may give up on the task altogether
[[2024-01-23_laws-of-ux_05-3-millers-law]]. Designers systematically
underestimate this: programmers self-select for larger working-memory capacity,
so a feature that feels easy to the people building it may overload most of the
people using it [[2018-04-29_working-memory-external-memory]].

Load is not a property of the interface alone but of the interface in its
context. The same design costs little at a desk and a great deal at 55 miles per
hour, where five extra seconds spent deciphering a screen is a football field
travelled with eyes off the road [[2018-06-24_distracted-driving-ux]]. It also
depends on how practiced the user is: a well-rehearsed task runs on automatic
processing and consumes few cognitive resources, while any change to the
practiced pattern forces conscious attention back into the loop
[[2017-12-10_practiced-patterns-mistakes]]. It scales with the number of options
on offer as well: the time taken to decide rises logarithmically with the number
and complexity of the choices available, so a fuller interface costs more to
decide in before anything has even been read
[[2024-01-23_laws-of-ux_06-4-hicks-law]] [[Hick's Law]]. The design goal is usually to
minimise this burden, by getting to the point and controlling information
density [[2026-04-14_409_Les_8_heuristiques_de_Bastien_&_Scapin_-_Guide_UX_Design]],
though the sources are clear that reduction is not an absolute good: in games,
memory demands and challenge are part of what makes play engaging
[[2024-02-16_usability-heuristics-board-games]].

The concept is not confined to the artifact being designed. One source applies
it to the meeting where the design is reviewed, treating a stakeholder meeting
as itself an interface: clutter, options and roadblocks should be removed so
that the stakeholders' brains are free for the primary task, which is supporting
a design decision
[[2020-08-03_articulating-design-decisions_04-chapter-3-design-the-meeting]].

## Practice

### Do not make users remember what the system can show them

The core guideline is to make everything a task requires accessible without the
user committing it to working memory
[[2018-04-29_working-memory-external-memory]]. Concretely: mark required fields
on each field rather than in a top-of-form instruction users will not read and
will forget, and mark optional fields too so optionality never has to be
inferred from an unmarked neighbour [[2019-06-16_required-fields]]. In voice
interfaces, avoid long spoken option lists — people forget the early choices by
the time they hear the later ones [[2017-09-10_audio-signifiers-voice-interaction]].
Duplicate links create the same problem in a subtler form: users must hold both
in mind and decide whether they lead to the same place, pausing to wonder what
difference they missed [[2016-03-13_duplicate-links]].

Augmented reality is the strongest case of removing the memory step entirely:
information appears in context, so a mechanic never memorises a part number or
switches to a lookup system, and multiple sources are merged into one overlay
that minimises attention-switching [[2016-09-18_augmented-reality-ux]].

### Provide external memory

Where information cannot be displayed in place, give users a scratchpad outside
their head. Comparison tables, shopping carts, open tabs and note-taking
features all act as virtual scratchpads that let users externalise information
[[2018-04-29_working-memory-external-memory]]. Complex applications should let
users write notes and comments inside the workflow; without that, they build
external spreadsheets, which is its own burden
[[2021-09-05_designing-for-waits-and-interruptions]]. Smaller screens shrink the
external memory available at a glance: mobile users must scroll to see content
that stayed visible on a larger screen, raising working-memory demands
[[2018-04-29_working-memory-external-memory]].

### Chunk rather than count

Miller's actual contribution is read here as chunking rather than the number
seven: grouping related information into meaningful units helps memorisation
more than limiting how many items are shown, and a formatted phone number is
easier to process and memorise than the same digits in an unbroken string
[[2024-01-23_laws-of-ux_05-3-millers-law]] [[Miller's Law]]. The seven-item
navigation rule is named as a myth on the grounds that a menu requires no
memorisation at all, since the choices stay visible: Nike.com's navigation
exceeds seven items and remains scannable through clear categorisation,
whitespace and visual grouping [[2024-01-23_laws-of-ux_05-3-millers-law]]. What
does the work is visual grouping — hierarchy, colour, scale, dividers and
spacing — applied to dense information layouts, ecommerce product groupings and
editing toolbars alike, so users can scan, identify what matches their goal and
process it faster; a wall of text with no hierarchy is the counter-example
[[2024-01-23_laws-of-ux_05-3-millers-law]] [[Information Architecture]].

### Interruptions, waits and task switching

True simultaneous multitasking is not possible when tasks draw on similar
cognitive resources; what actually happens is serial task switching, a rapid
alternation of attention that fragments cognitive resources, increases errors,
lowers output quality and accumulates stress
[[2025-05-23_serial-task-switching]]. The same finding underpins the debunking of
the digital-native myth: heavier multitaskers are not better at it, and
refocusing attention carries a measurable delay
[[2016-01-03_millennials-digital-natives]].

Design for the switch rather than against it:

- Multi-view layouts (split screens, picture-in-picture, resizable panels) keep
  several tasks visible and lower the cost of switching
  [[2025-05-23_serial-task-switching]].
- Let long processes run in the background so users can work elsewhere
  [[2021-09-05_designing-for-waits-and-interruptions]]
  [[2025-05-23_serial-task-switching]].
- Support re-entry after an absence: detailed progress indicators for waits over
  ten seconds, success messages contextualised with what happened and when, and
  quick access to recently viewed content with previews and clear labels
  [[2021-09-05_designing-for-waits-and-interruptions]].
- Add focus modes, orientation cues and error recovery (undo, autosave,
  confirmations) for the mistakes divided attention induces
  [[2025-05-23_serial-task-switching]].

### Consistency and practiced patterns

Predictable, unambiguous layouts let users converge fast on an optimal scanning
algorithm and skip what is irrelevant to their goal, without leaning on
short-term memory: consistent positioning of key information, short recognisable
text, large bold typography for primary elements, and enough white space
[[2017-03-19_eyetracking-tasks-efficient-scanning]]. Familiar patterns work
because they run automatically; a design that mimics a convention but deviates
slightly is the worst case, since users apply the learned pattern, miss the
difference, and never notice the resulting error
[[2017-12-10_practiced-patterns-mistakes]]. The recommendation is to either
comply fully with the established pattern or depart from it completely and
obviously, so conscious processing is triggered on purpose
[[2017-12-10_practiced-patterns-mistakes]]. Homepages follow the same logic:
standard, predictable designs aligned with what users already know elsewhere,
minimal motion, no popups [[2024-03-15_homepage-design-principles]]. Consistent
vocabulary, respected standards for icons and behaviours, logical grouping and
immediate feedback are named as the guidance criterion that keeps load down
[[2026-04-14_409_Les_8_heuristiques_de_Bastien_&_Scapin_-_Guide_UX_Design]].

### Simplicity and what to remove

Reduce complexity through simple designs, clear language and focused content so
users are not overwhelmed [[2024-03-15_homepage-design-principles]], and cut
visual noise rather than adding [[2026-04-14_409_Les_8_heuristiques_de_Bastien_&_Scapin_-_Guide_UX_Design]].
Attention is treated as zero-sum: every extra link competes with the others, so
if something matters, give it more visual prominence instead of repeating it
[[2016-03-13_duplicate-links]]. Where duplication is genuinely justified, place
the copies far enough apart that they can never be seen on the same screen —
seeing them together is itself the signal that the page is redundant
[[2016-03-13_duplicate-links]].

Weak signifiers, unclear labels and wordiness cut the other way, raising load and
time on task; strong visual signals for interactive elements and glanceable
typography (larger, wider, capitalised) are the counter-measures
[[2018-06-24_distracted-driving-ux]].

### Choice and decision time

Hick's Law, formulated in 1952 by the psychologists William Edmund Hick and Ray
Hyman, states that the time to make a decision increases logarithmically with the
number and complexity of the choices available, formalised as RT = a + b log₂(n)
with task-dependent constants [[2024-01-23_laws-of-ux_06-4-hicks-law]]
[[Hick's Law]]. The behavioural counterpart is choice overload: Sheena Iyengar
and Mark Lepper's 2000 jam study found shoppers ten times more likely to buy when
shown six varieties rather than twenty-four, against the assumption that more
choice improves satisfaction [[2024-01-23_laws-of-ux_06-4-hicks-law]]. The
strategies that source gives:

- **Minimise the choices at critical moments**, and reveal the rest at the right
  time rather than all at once — Google Search keeps the initial interface on the
  search box and surfaces the image, video and news filters only once results
  appear [[2024-01-23_laws-of-ux_06-4-hicks-law]] [[Progressive Disclosure]].
- **Decompose the task.** Notion's onboarding uses a progressive checklist to
  teach new users instead of exposing every available feature simultaneously
  [[2024-01-23_laws-of-ux_06-4-hicks-law]].
- **Give some options more weight.** Netflix answered eighteen minutes of
  decision paralysis by highlighting "Trending Now" and "Popular on Netflix",
  which carries part of the choosing burden for the user
  [[2024-01-23_laws-of-ux_06-4-hicks-law]].

The counterweight that source attaches is that simplification has a floor: an
interface simplified to the point of abstraction no longer makes clear what
actions are available, what the next steps are, or where to find specific
information, and icon-only navigation is the named failure — text labels
alongside icons provide clarity and aid recognition
[[2024-01-23_laws-of-ux_06-4-hicks-law]].

### Hiding interface: reduction or displacement?

The sources disagree on whether hiding elements lowers load, and the disagreement
is worth keeping. [[2016-12-18_zen-mode]] argues that hiding UI chrome to help
users focus does the opposite: like a painter whose palette has been moved, users
must search for and recall where tools are, track which mode they are in, and
remember what exists in which mode — so a pattern sold as reducing cognitive load
increases it. [[2019-05-12_split-buttons]] takes a mixed position: grouping
related commands behind a default action does reduce visual complexity and
interaction cost, but hidden menu options raise load for anyone who does not
discover them, and persistent variants (where the last choice becomes the new
default) break spatial consistency for new users.

Against this, progressive disclosure is recommended in three places, on the
grounds that it reveals options only when they are needed rather than removing
access to what is already in use: in voice interfaces, to keep attention on the
current step instead of front-loading every possibility
[[2017-09-10_audio-signifiers-voice-interaction]], in long forms, split into
manageable sections or showing fields conditionally
[[2025-07-18_4-principles-reduce-cognitive-load]], and in any interface carrying
many options, where choices should be revealed at the right time rather than
presented all at once [[2024-01-23_laws-of-ux_06-4-hicks-law]]. [[2016-12-18_zen-mode]] also
warns that proactively surfacing tools when the software guesses they are needed
is unreliable, since intent cannot be inferred from a mouse movement; the voice
article makes the parallel point that a system should only guess when it has
enough information, because a wrong guess forces the user to work out how to
correct it [[2017-09-10_audio-signifiers-voice-interaction]].

### Forms

Forms are treated as the canonical high-load task, and
[[2025-07-18_4-principles-reduce-cognitive-load]] organises the guidance into
four principles:

- **Structure** — group related fields, create hierarchy with spacing and
  containers, order questions to minimise the effort of filling them in, prefer
  single-column layouts, break long forms up.
- **Transparency** — state requirements upfront (estimated time, materials
  needed, deadlines), distinguish required from optional fields, show progress.
- **Clarity** — plain language at a 6th-to-8th-grade reading level, positive
  wording rather than negatives that must be mentally reversed, one thing per
  question, formatting examples, familiar conventions.
- **Support** — no disappearing placeholders, constraints that prevent errors,
  timely error messages next to the field concerned, guidance that does not
  blame the user.

[[2019-06-16_required-fields]] adds the marking detail: an asterisk or the word
"required" in a contrasting colour with sufficient contrast, placed at the start
of the label to help scanning. Login forms are an exception where marking is
optional, since users already expect both fields to be mandatory, but
registration forms should always mark them because conventions vary between
sites [[2019-06-16_required-fields]]. Error management more broadly — preventing
errors, giving clear contextual messages, making correction easy — is presented
as the criterion that separates mediocre design from good design
[[2026-04-14_409_Les_8_heuristiques_de_Bastien_&_Scapin_-_Guide_UX_Design]].

### Attention-limited and safety-critical contexts

When users have little mental capacity to spare, ordinary usability flaws become
dangerous. [[2018-06-24_distracted-driving-ux]] argues from harm reduction:
people will use products while driving whether or not that is the intended use,
so reduce load with strong signifiers, context-aware defaults that cut the number
of interactions for top tasks, and glanceable typography — while questioning
gamification and notification patterns engineered for habitual use.
[[2019-05-19_tesla-big-touchscreen]] shows the failure mode: soft buttons offer
no haptic feedback, so drivers must look to hit them, and shrinking targets to
fit more options slowed acquisition and caused accidental touches, with an
always-present map background interfering visually. Its conclusion is that
touchscreen soft buttons should control only non-critical features, physical
buttons being preferable for critical ones.

### Modality-specific findings

- **Mobile reading** — comprehension of easy, linear content is equivalent to
  desktop, but difficult material triggers a speed–accuracy tradeoff: users slow
  down and re-read to hold comprehension, which is the visible cost of the extra
  load. Brevity and clear organisation matter more here, and some users value
  mobile's reduced distraction [[2016-12-11_mobile-content]].
- **AR onboarding** — static walkthroughs that front-load information (a
  deck-of-cards presentation) cause cognitive overload and force users to replay
  the tutorial; interactive walkthroughs that let users practise are markedly
  more effective, and instructions work best combining text, visuals and audio
  [[2022-09-25_ar-walkthroughs]].
- **Generative-AI chat** — response outlining (specifying structure in the
  prompt) works, but carries high cognitive and interaction cost because users
  must anticipate every relevant part of the output and articulate it, often
  discovering the gap only after a bad answer. GUI elements that suggest
  structural options or collect preferences upfront are proposed to shift that
  burden off the user [[2024-02-02_response-outlining]].

### The meeting as an interface

[[2020-08-03_articulating-design-decisions_04-chapter-3-design-the-meeting]]
transfers the guidance above onto a design review, on the argument that a
stakeholder has a finite budget of attention just as a user does, and that
whatever the meeting spends on clutter is not available for the decision. Its
prescriptions:

- **Set the context first.** State the goal, summarise the decisions already
  made, show where the work sits on the timeline of the design process, specify
  what kind of feedback is needed at this stage, then restate the goal. The
  refresh exists to absorb the switching cost stakeholders pay when they arrive
  from other work and other meetings. The source notes this need not be
  expensive: a few sentences, one slide, or a handful of bullets for an informal
  review.
- **Structure for memory.** Primacy and recency, repetition, surprise and mixed
  media are used deliberately to decide what stakeholders will retain, and
  content broken into distinct chunks with visual transitions is described as
  stickier than one long uninterrupted presentation.
- **Remove distractions.** Placeholder content — stock images, lorem ipsum — and
  visual clutter can derail an entire conversation onto trivia, so real copy,
  aligned layouts and appropriate imagery are worth the extra time. The source's
  rule is that a distraction should only happen once: the same one recurring
  across two meetings means it was not fixed.
- **Lower your own load too.** A printed agenda, speaking the presentation out
  loud beforehand and a short team huddle are recommended so the designer has
  capacity left to be present and articulate in the moment.

### When load is not the enemy

Board games show that heuristics can be broken on purpose: hidden information
creates tension, and high cognitive load can be the challenge that makes play
engaging, because recreation is not productivity
[[2024-02-16_usability-heuristics-board-games]]. Even there, load that is
accidental rather than designed still hurts — visible scoring tracks and pieces
free players to think about strategy, consistent icons and symbols reduce memory
demands and avoid excluding colourblind players, and clearly organised rules
lower the barrier to starting
[[2024-02-16_usability-heuristics-board-games]]. The same adaptability logic
appears in the ergonomic criteria: an interface should adjust to context,
preference and level of expertise, offering different paths to novices and
experts [[2026-04-14_409_Les_8_heuristiques_de_Bastien_&_Scapin_-_Guide_UX_Design]].

## Sources (24)

- [[2016-01-03_millennials-digital-natives]] — examines how multitasking increases cognitive load through frequent context-switching, with research showing heavy multitaskers take 0.5 seconds longer to refocus attention and experience higher stress levels.
- [[2016-03-13_duplicate-links]] — duplicate links increase the mental processing burden on users.
- [[2016-09-18_augmented-reality-ux]] — Demonstrates how AR reduces working-memory load by displaying relevant information automatically, eliminating the need to memorize details or use external memory aids.
- [[2016-12-11_mobile-content]] — Mobile reading increases working-memory load; users compensate through speed-accuracy tradeoffs on difficult material and benefit from clear organization and focused presentation.
- [[2016-12-18_zen-mode]] — the article argues that zen mode increases cognitive load by requiring users to remember and retrieve hidden tools instead of reducing it.
- [[2017-03-19_eyetracking-tasks-efficient-scanning]] — Illustrates how consistent design and predictable patterns reduce cognitive burden by helping users develop efficient scanning strategies without relying on short-term memory.
- [[2017-09-10_audio-signifiers-voice-interaction]] — voice systems must manage cognitive demands by using sequential rather than combined questions, progressive disclosure, and implicit cues that don't require users to remember long option lists.
- [[2017-12-10_practiced-patterns-mistakes]] — The mental effort required to complete a task; familiar patterns reduce cognitive load by allowing automatic processing; changed patterns require conscious attention and increase cognitive load.
- [[2018-04-29_working-memory-external-memory]] — understanding how interface design increases or decreases the burden on working memory and overall cognitive effort.
- [[2018-06-24_distracted-driving-ux]] — Weak signifiers, confusing interfaces, and wordiness all increase cognitive load, which is particularly dangerous when users are distracted by driving and have limited mental resources to decipher unclear designs.
- [[2019-05-12_split-buttons]] — Grouping related commands reduces complexity, but hidden menu options may increase cognitive load if users don't discover them.
- [[2019-05-19_tesla-big-touchscreen]] — Touchscreen interfaces in cars increase cognitive load by requiring visual confirmation and attention; soft buttons should only control non-critical features.
- [[2019-06-16_required-fields]] — reducing the need for users to remember whether fields are required or scan for optional-field markers minimizes working-memory burden during form completion.
- [[2021-09-05_designing-for-waits-and-interruptions]] — Complex-app users experience increased cognitive load when interrupted by long waits; supporting context recovery through notes, success dialogs, and recent content access reduces the mental burden of task resumption.
- [[2022-09-25_ar-walkthroughs]] — static walkthroughs with extensive information cause cognitive overload and strain working memory, forcing users to replay instructions to retain details.
- [[2024-02-02_response-outlining]] — response outlining increases cognitive load by requiring users to anticipate and articulate output structures.
- [[2024-02-16_usability-heuristics-board-games]] — a key design consideration in games, where challenge and memory demands contribute to engagement.
- [[2024-03-15_homepage-design-principles]] — emphasizes minimizing complexity through simple designs, clear language, and focused content to prevent user overwhelm.
- [[2025-05-23_serial-task-switching]] — the amount of mental effort required to process information; task switching fragments cognitive resources across multiple activities.
- [[2025-07-18_4-principles-reduce-cognitive-load]] — The article explicitly focuses on reducing mental effort required to complete forms through structural, transparent, and supportive design decisions.
- [[2026-04-14_409_Les_8_heuristiques_de_Bastien_&_Scapin_-_Guide_UX_Design]]
- [[2020-08-03_articulating-design-decisions_04-chapter-3-design-the-meeting]] — Reducing stakeholder cognitive load is the central framework; the chapter applies this UX principle directly to meeting structure.
- [[2024-01-23_laws-of-ux_05-3-millers-law]] — the mental effort required to understand and interact with an interface; design should minimize unnecessary cognitive load.
- [[2024-01-23_laws-of-ux_06-4-hicks-law]] — the mental effort required to process choices and make decisions; higher choice counts increase cognitive load.
