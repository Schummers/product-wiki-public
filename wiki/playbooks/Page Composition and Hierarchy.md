---
type: playbook
name: Page Composition and Hierarchy
theme: Page Composition and Hierarchy
created: 2026-08-21
updated: 2026-08-21
status: active
sources_as_of: 2026-07-31
concepts:
  - Eye Tracking
  - Web Usability
  - Visual Hierarchy
  - Progressive Disclosure
  - Data Visualization
  - Information Design
  - Aesthetic-Usability Effect
  - Gestalt Principles
---

# Playbook — Page Composition and Hierarchy

Checkable rules distilled from this theme's concept pages, for
`product-wiki-review`. Give each one a verdict: `holds`, `breached`, or `n/a`
with a reason.

A **cache** of [[Page Composition and Hierarchy]] (`docs/adr/0004`), not a
replacement. Open the concept pages when a rule needs its nuance.

## Establish hierarchy before styling

**P1. The content hierarchy and key takeaway are decided before the visual
design starts.** Not after. [[2021-01-17_visual-hierarchy-ux-definition]]

**P2. Three levers build prominence: contrast, scale, grouping.**
Contrast between an element and its background is the primary determinant.
Larger elements are reserved for what matters most, capped at three sizes for
clarity. Grouping is implicit (whitespace, proximity) or explicit (borders,
common regions). [[2021-01-17_visual-hierarchy-ux-definition]]

**P3. The squint test validates the hierarchy after the fact.**
Blur the design: the intended groupings and emphasis either read or they do
not, and unintended emphasis becomes visible.
[[2021-01-17_visual-hierarchy-ux-definition]]

**P4. Highlight only what is essential.**
Signal is what serves the user's current task, noise is everything else, and
the same element can be either depending on the moment (navigation is noise
while reading, signal when leaving). Highlighting everything overwhelms.
[[2018-09-09_signal-noise-ratio]]

## Grouping (Gestalt)

**P5. Related elements sit close together, unrelated elements do not.**
Proximity can overpower colour or shape as a grouping cue. Check this survives
responsive reflow: proximity relationships built on a side-by-side desktop
layout break when columns stack on mobile. [[Gestalt Principles]]

**P6. A boundary is used only when whitespace cannot carry the grouping.**
Common region (border, background, card) is the strongest grouping cue,
overpowering proximity and similarity, so it resolves ambiguity whitespace
alone cannot. Overuse creates clutter and **false floors**, apparent stopping
points that read as the end of the page. [[Gestalt Principles]]

**P7. Similar elements share visual treatment consistently.**
Colour, shape and size each signal something and each pitfall is real: a
primary action needs its own colour or every button looks equally important;
different content types shown at the same size read as equally important even
when they are not, which is what makes ad-like right rails fail through banner
blindness. [[Gestalt Principles]]

**P8. Colour is never the only distinction.**
Repeated across every source in this theme: colourblind and visually impaired
users lose a colour-only signal entirely. Pair it with icon, shape or text.
[[2016-08-07_visual-indicators-differentiators]]
[[2018-08-12_designing-effective-infographics]]

## Progressive disclosure

**P9. A long task is broken into steps only when the task is infrequent or the
user is a novice.** Step-by-step becomes tedious for frequent, expert work; a
faster path should exist for repeat users. [[2017-06-25_wizards]]

**P10. Deferred content stays honest and inline.**
Modals, overlays and full-page takeovers hijack focus; supplemental detail
belongs adjacent to what it explains. Essential instructions, constraints,
form limits and legal disclaimers are never deferred: hiding them turns
guidance into hide-and-seek. [[2026-01-23_info-tips-bad]]

**P11. Hidden content leaves a visible signal that it exists.**
Six of eight users in one study never scrolled past a hero video because
nothing indicated content below. Full-width horizontal lines, wide whitespace
between sections and large ads act as false floors the same way.
[[2016-01-17_illusion-of-completeness]]
*The mechanism is closure:* enough of a cut-off element must stay visible for
users to recognise it and infer more exists; too little and there is nothing
to complete. [[2021-07-18_principle-closure]]

**P12. A carousel signals its own existence beyond a dot indicator.**
Small dots do not communicate more content. Use edge-peeking content, a
headline naming the carousel, salient arrow controls, and a slide count.
[[2016-01-17_illusion-of-completeness]]

## Encoding information

**P13. An encoding choice is deliberate, and redundant where it matters.**
Tested across four indicator types, colour-plus-icon beat every alternative on
every UX metric; text-only was 57 % slower to complete and 56 % slower to first
correct click. [[2016-08-07_visual-indicators-differentiators]]

**P14. An image used to carry information sits above the fold, does not
auto-rotate, and favours literal over abstract.**
Dual-coding theory: an image is stored as image and as description, a word only
once, which is why images are more memorable. Text remains essential
regardless: a text label alongside an image adds redundancy that strengthens
both comprehension and recall. [[2024-04-26_picture-superiority-effect]]

**P15. A chart maximises its data-ink ratio and never distorts scale.**
State the source and the baseline so the reading is not misleading. Choose
static for making a point, interactive for enabling exploration.
[[2018-08-12_designing-effective-infographics]]

**P16. Missing or ambiguous information is a cost paid elsewhere.**
In one measured case, 38 % of customer-service contacts across 45 journeys
traced to information gaps, mostly ambiguous policy or thin comparison detail.
The fix is removing the roadblock, never hiding the contact option.
[[2016-09-11_customer-service-omnichannel-ux]]

## Instant judgement

**P17. The first aesthetic judgement happens in 50 ms and rarely reverses.**
It is System 1, automatic and pattern-based, and it sets the perceived value
and perceived cost of the whole page before any real interaction.
[[2017-10-01_first-impressions-human-automaticity]]
[[2016-04-17_perceived-value]]

**P18. Visual tone matches the positioning.**
A budget product looks budget-friendly, a premium one sophisticated.
Misalignment confuses and damages credibility.
[[2016-04-17_perceived-value]]

**P19. Beauty does not excuse a real usability flaw for long.**
Attractive design earns tolerance for minor friction, not for broken function;
patience runs out when functionality is sacrificed for looks.
[[2024-02-03_aesthetic-usability-effect]]

**P20. A polished artifact is probed harder for usability, not less.**
The aesthetic-usability effect biases evaluation itself: users comment on
visual appeal while struggling with the actual task, which masks real
problems. In research, sequence behavioural tasks before aesthetic questions,
and keep the facilitator visibly distant from ownership of the design.
[[2024-02-03_aesthetic-usability-effect]] [[2024-12-13_testing-visual-design]]

## Where this theme stops

Component-level layout choices (forms, modals, controls) live in
[[Interaction and Interface Patterns]]. Typography, colour and grid craft live
in [[Visual Design Craft]]. Contrast thresholds and screen-reader structure
live in [[Accessibility and Inclusion]].
