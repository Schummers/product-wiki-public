---
type: concept
name: Von Restorff Effect
created: 2026-09-10
updated: 2026-09-10
status: stub
---

# Von Restorff Effect

## Definition

The von Restorff effect, also called the isolation effect, holds that when
multiple similar objects are present, the one that differs from the rest is the
most likely to be remembered. It is named after the German psychiatrist Hedwig
von Restorff, whose 1933 study found that participants best remembered the
categorically similar items that had been made distinctly different
([[2024-01-23_laws-of-ux_10-8-von-restorff-effect]]). Applied to digital
interfaces, it is the case for visual contrast: an element isolated from its
neighbours is the one users notice, act on, and recall.

The effect rests on selective attention. Human attention is limited in both
capacity and duration, so people focus on what they judge relevant to the
detriment of everything else; contrast is what decides which elements land in
that category. The same filtering mechanism produces its two failure modes.
Banner blindness: users ignore anything they perceive as advertising, and
legitimate content is ignored too when it resembles an ad or sits next to one.
Change blindness: users fail to notice significant changes when the visual cues
are weak or their attention is focused elsewhere.

## Practice

### Contrast has more than one lever

Visual contrast can be created through color, shape, size, position, and
motion. [[2024-01-23_laws-of-ux_10-8-von-restorff-effect]] gives Material
Design's floating action button, Notion's pricing table emphasising the "Plus"
plan through color and shape, and notification badges as examples of the
principle in production interfaces. This is the mechanism behind
[[Visual Hierarchy]]: differentiation across several properties at once is what
makes one element read as primary.

### Draw attention to changes on purpose

Because of change blindness, a change the user genuinely needs to notice will
not be noticed on its own. If awareness is required, the designer has to draw
attention to it deliberately with appropriate contrast rather than assume the
change speaks for itself.

### Restraint is part of the technique

Contrast only works while it stays scarce. The record is explicit about
overuse:

> The only thing worse than no contrast is way too much of it, which not only
> can dilute the power of the elements or content that you intended to stand
> out but can also visually overwhelm people.

Too many emphasised elements produce visual noise, dilute the emphasis, and
push users to tune out the information that mattered.

### Contrast that excludes is not contrast

[[Accessibility]] constrains how the effect may be produced
([[2024-01-23_laws-of-ux_10-8-von-restorff-effect]]):

- WCAG requires a color contrast ratio of at least 4.5:1 between text and
  background for standard text, and 3:1 for larger text (18pt and above) or
  bold text (14pt and above).
- Color must never be the only differentiator. Patterns, strokes and shape
  carry the distinction for people with color vision deficiency.
- Motion-based contrast has to account for vestibular disorders.

### Check whether the contrast actually worked

[[Eye Tracking]] measures where users look and how they move through an
interface, giving objective data on attention patterns and on whether the
contrast a designer introduced is directing focus as intended.

## Sources (1)

- [[2024-01-23_laws-of-ux_10-8-von-restorff-effect]] — The principle that distinctly different items from a similar set are more memorable, applied in digital design through visual contrast to guide attention to key information and actions.
