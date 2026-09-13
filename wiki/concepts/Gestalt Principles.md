---
type: concept
name: Gestalt Principles
created: 2026-07-31
updated: 2026-09-10
status: developed
---

# Gestalt Principles

## Definition

Gestalt principles are principles of visual perception describing how people
organise complex images into coherent wholes rather than seeing separate pieces
[[2020-03-01_principles-visual-design]]. They come from early-20th-century
Gestalt psychology [[2020-09-06_gestalt-similarity]] and describe how people
perceive and organise the visual world; designers apply them to build usable,
intuitive interfaces [[2021-07-18_principle-closure]]. The set named in the
corpus is proximity, similarity, continuation, closure, common region,
figure/ground and symmetry, presented as one of the five principles of visual
design alongside scale, visual hierarchy, balance and contrast
[[2020-03-01_principles-visual-design]].

Their practical role is grouping: they determine which elements users read as
related, as sharing functionality, or as belonging to the same level of
importance. Because grouping happens automatically, the principles work whether
or not the designer intended them — accidental groupings mislead just as
reliably as deliberate ones [[2020-08-02_gestalt-proximity]],
[[2020-09-06_gestalt-similarity]]. The same perceptual mechanics also underlie
UX issues such as the illusion of completeness
[[2017-01-01_ux-quiz-16]], [[2021-07-18_principle-closure]].

## Practice

### Proximity

Items placed close together are perceived as belonging to the same group and
sharing functionality or traits, and proximity can overpower other cues such as
colour or shape [[2020-08-02_gestalt-proximity]]. The working tool is
whitespace: varying the amount of space unites or separates elements, and extra
whitespace signals that elements belong to different groups with different
functions. The source calls the practice of placing related elements together
and separating unrelated ones with whitespace nearly universal in interface
design.

Applications and pitfalls from the same source:

- **Forms** — grouping related fields makes forms easier to scan and less
  daunting: one form of 12 fields feels more taxing than the same fields split
  into three meaningful groups.
- **Responsive layouts** — proximity relationships break when layouts adapt.
  Columns side by side on desktop may stack vertically on mobile, destroying
  the grouping and causing users to miss related information.
- **Accidental grouping** — putting unrelated elements together camouflages
  them, especially when users are pursuing a task; people may look at a single
  item in a perceived group and judge all the others by it.
- **Tunnel vision** — users selectively attend to certain screen areas while
  completing a task and miss things "in plain sight" outside the focal area.

### Similarity

Items sharing visual characteristics — colour, shape, size — are assumed to be
related and to function alike; they need not be identical, only to share
visible traits [[2020-09-06_gestalt-similarity]]. Every interaction with a
similar element builds expectations about how the next one will behave, which
is why consistent visual rules per element type matter. Similarity can unite
elements despite distributed placement and is more resilient than
proximity-based grouping, though it is often overpowered by proximity or common
region.

Guidance from that source:

- **Colour** is the strongest unifier and can tie together elements of
  different types. Link colour consistently signals clickability — and must not
  be used for non-clickable content.
- **Primary actions** deserve a separate colour so they stand out among
  secondary buttons; when every button shares a colour, users must work out
  which one is primary.
- **Shape** signals function: rectangles read as buttons, rounded pill shapes as
  navigation links, consistent icon shapes as consistent functionality across
  categories.
- **Size** communicates rank: similarly sized objects are read as equally
  important, and consistent sizing produces a scannable hierarchy.
- **Size pitfall** — different content types displayed at similar sizes are
  perceived as related even when they are not. This is what makes right rails
  fail, with content and advertisements equally prominent, feeding banner
  blindness.

The quiz source frames the same lever from the opposite direction: different
shapes and colours are what distinguish items from one another
[[2017-01-01_ux-quiz-16]].

### Common region

Items inside a boundary are perceived as a group and assumed to share
characteristics or functionality; borders, background colours and card layouts
therefore let users grasp interface structure quickly
[[2020-07-12_common-region]]. Common region is the strongest of the grouping
cues — a boundary overpowers proximity and similarity, so elements enclosed
together read as grouped even when spaced far apart, which makes it the tool for
resolving ambiguity when whitespace alone is not enough.

Uses and limits [[2020-07-12_common-region]]:

- Useful in complex interfaces with many options: print dialogs, navigation
  menus, filter panels.
- Background colours or borders around headers, footers, sidebars and
  navigation separate chrome from content, so users distinguish interface
  structure at a glance.
- Cards and accordions rely on it: keeping a label inside the same boundary as
  its content visually connects the two and establishes hierarchy; tabs and
  accordions group related options.
- Overuse creates visual clutter and **false floors** — apparent stopping points
  that make users think the page has ended. Before adding a border, ask whether
  it is needed to understand the grouping or whether whitespace would do.

### Closure

The brain automatically fills in missing information so that incomplete objects
are perceived as complete, which lets designers suggest complex shapes or
information with minimal visual elements [[2021-07-18_principle-closure]].
Applications range from logos (PBS, MLB) to interface icons — which still need
user testing to confirm they communicate their function — to partially
displayed carousel items that signal more content and invite swiping or
scrolling.

The constraint is sufficient context: enough of the cut-off element must be
visible for users to recognise it and understand that more exists; with too
little information they cannot fill in the blanks. Closure also has a
double-edged relationship with the **illusion of completeness**: when elements
above the fold look complete, users may never scroll, so deliberately
segmenting elements so they appear incomplete is what encourages scrolling
[[2021-07-18_principle-closure]]. The same phenomenon appears in
[[2017-01-01_ux-quiz-16]]: content looks complete within the viewport while more
information sits outside it, and the gap between perceived and actual
availability shapes user expectations.

### Gestalt within visual design as a whole

[[2020-03-01_principles-visual-design]] places Gestalt alongside four other
principles that shape perception together:

- **Scale** — relative size signals importance and rank; bigger elements are
  noticed first, and no more than three sizes keeps hierarchy clear.
- **Visual hierarchy** — built from variations in scale, value, colour, spacing
  and placement, so users immediately know what to focus on and in what order.
- **Balance** — visual weight distributed across an imaginary axis, not
  necessarily symmetrically: symmetry is static and quiet, asymmetry dynamic
  and engaging; balance may be symmetrical, asymmetrical or radial.
- **Contrast** — juxtaposing dissimilar elements to mark different categories or
  functions, such as high-contrast red for a delete action; but reducing text
  contrast to de-emphasise content compromises accessibility.

The same source argues visual design is not decoration: it increases usability
by making layouts easy to understand, provokes positive emotion (the
aesthetic-usability effect), and strengthens brand perception and trust,
directly affecting task success and engagement.

## Sources (7)

- [[2017-01-01_ux-quiz-16]] — the quiz addresses visual design principles that govern how users perceive and group elements, such as using different shapes and colors to distinguish items.
- [[2020-03-01_principles-visual-design]] — Explains how proximity, similarity, continuation, closure, common region, figure/ground, and symmetry help users organize and understand complex visual compositions.
- [[2020-07-12_common-region]] — common region as one of several Gestalt principles of visual perception relevant to UX.
- [[2020-08-02_gestalt-proximity]] — Proximity is one of the original Gestalt grouping principles (along with similarity and closure) and remains essential for creating usable interfaces that help users understand relationships between elements.
- [[2020-09-06_gestalt-similarity]] — Similarity is one of the original Gestalt grouping principles, discovered in the early 20th century, and remains essential for creating interfaces where relationships between elements are clear and predictable.
- [[2021-07-18_principle-closure]] — Gestalt psychology principles including closure, proximity, and similarity describe how people visually perceive and organize the world; designers apply these principles to create usable, intuitive interfaces.
- [[2024-01-23_laws-of-ux_02-a-brief-history-of-psychology-and-design]] — Visual perception principles from Gestalt psychology (figure-ground, similarity, proximity, closure) that continue to influence design by recognizing how humans organize sensory information into meaningful wholes.
