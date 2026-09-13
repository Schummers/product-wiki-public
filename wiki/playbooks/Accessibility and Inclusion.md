---
type: playbook
name: Accessibility and Inclusion
theme: Accessibility and Inclusion
created: 2026-08-21
updated: 2026-08-21
status: active
sources_as_of: 2026-07-31
concepts:
  - Accessibility
  - Localization
  - Young Users
  - User Expectations
---

# Playbook — Accessibility and Inclusion

Checkable rules distilled from this theme's concept pages, for
`product-wiki-review`. Give each one a verdict: `holds`, `breached`, or `n/a`
with a reason.

A **cache** of [[Accessibility and Inclusion]] (`docs/adr/0004`), not a
replacement. Open [[Accessibility]] whenever a rule needs its nuance.

The corpus treats accessibility as **structural**: a property of how an
interface is coded, labelled and sequenced, not a layer added afterwards.
Third-party accessibility plugins are largely ignored by screen-reader users,
who already run more powerful built-in OS screen readers
[[2023-04-30_screen-reader-users-on-mobile]]. A customised native component that
breaks takes every form built on it down with it
[[2025-08-12_390_Designer_une_checkbox_-_Guide_UX_avancé]].

## Redundancy

**A1. Every capability reachable through a second channel.**
Enhanced or accelerated interactions may exist, and the UI never relies on them
for any task. [[2016-05-01_enhancement]] Cursor changes are a cheap
discoverability signal, and the keyboard and touch paths stay open
[[2025-03-18_369_Guide_UX_Curseur_de_souris_natif_et_custom]]. Date fields
accept typed input in several formats alongside pickers and lists
[[2017-01-22_date-input]]. Tooltips carry no information the link text and
context do not already give: most touchscreen browsers never display them
[[2016-06-19_title-attribute]].

**A2. Colour is never the only signal.**
Combine it with pattern, icon, stroke or text. Quantitative testing found
colour-plus-icon best across every UX metric, the icon carrying the fallback
[[2016-08-07_visual-indicators-differentiators]]. Avoid red/green pairings and
use colour-blind-safe palettes in charts, with text labels or hover detail as
the secondary signal [[2019-09-29_treemaps]]. A selected tab carries at least
two cumulative indicators, for example underline plus colour
[[2025-01-07_359_In-page_tabs_-_Guide_UX_design]]. Palettes are usability-tested
for legibility, contrast and colour-blindness rather than assumed
[[2021-06-06_color-enhance-design]].

## Perception

**A3. Contrast reaches 4.5:1 for normal text and 3:1 for large text**, verified
with a contrast checker. [[2022-10-30_visual-treatments-accessibility]]
*It does not bend for aesthetics:* bold palettes still meet the ratios, and
pairings such as yellow on cyan fail readability [[2025-04-11_neobrutalism]].
*Translucency is the hard case:* text crossing several background colours makes
the ratio unpredictable, so verify across the range and expose a contrast or
reduced-transparency control where feasible [[2024-06-07_glassmorphism]].

**A4. Dark mode is offered as a pervasive option, not imposed as the default.**
Light mode with positive polarity generally performs better for normal or
corrected vision, and dark mode helps at night, at very small font sizes, and
specifically for users with cloudy ocular media such as cataracts, where less
emitted light reduces scattering. [[2020-02-02_dark-mode]]

**A5. Motion respects the reduce-motion setting.**
Excessive animation, flashing, parallax, scroll-jacking and carousel motion
cause vestibular symptoms and can trigger seizures.
[[2020-02-09_animation-duration]]

## Operation

**A6. Focus is visually obvious and arrives within 100 to 150 ms of Tab.**
A clear stroke or border, the default browser outline being what users expect.
[[2022-10-30_visual-treatments-accessibility]]
[[2025-04-25_button-states-communicate-interaction]]

**A7. Every interactive element has a keyboard path.**
Tooltips reachable by focus as well as hover [[2019-01-27_tooltip-guidelines]].
Modals closable from the keyboard, Escape included
[[2024-09-24_347_Fenêtre_modale,_le_Guide_UX_Design]]. Drag-and-drop gets grab
handles reachable with Tab, spacebar to grab, and screen-reader messaging that
announces available actions, the grabbed state, and current position
[[2020-02-23_drag-drop]].

**A8. Touch targets are at least 1 cm × 1 cm as physically rendered.**
Pixel dimensions are meaningless across device densities. Spacing matters as
much as size: crowded targets cause slips. Watch for view-tap asymmetry, large
enough to see and too dense to tap, the classic artefact of a desktop-to-mobile
port. [[2019-05-05_touch-target-size]] A checkbox carries a fully clickable
label and a tap area of at least 40×40 px including surrounding space
[[2025-08-12_390_Designer_une_checkbox_-_Guide_UX_avancé]].

## Structure and screen readers

**A9. Headings and links are semantic, not just styled.**
Screen readers present one element at a time, so scanning by jumping between
headings and links works only when those elements are coded as such.
[[2023-04-30_screen-reader-users-on-mobile]]

**A10. Labels are frontloaded with their keywords.**
Users do not listen to an entire label.
[[2023-04-30_screen-reader-users-on-mobile]]

**A11. Opening an overlay or menu moves screen-reader focus to it.**
[[2023-04-30_screen-reader-users-on-mobile]]

**A12. A complex menu has a simple fallback.**
Screen-magnifier users see only part of a mega menu; clickable top-level items
leading to full pages sit alongside the advanced implementation.
[[2017-03-26_mega-menus-work-well]]

## Alt text

**A13. Alt text describes the image's role, in about 150 characters, keywords
first.** Context and intent decide what it says: the same image needs different
alt text in different places. Decorative images take an empty alt attribute,
functional images describe the action they afford, informative images give
their unique value without restating page copy. A complex chart may be better
served by restructuring the copy into a table or list.
[[2024-11-22_write-alt-text]] [[2022-10-30_visual-treatments-accessibility]]

**A14. Redundant images get no alt text.**
Where the information is already in the page copy, alt text raises interaction
cost and wastes screen-reader users' time. The test is three questions: is the
information repetitive, is the image referenced by the copy, would alt text help
complete the task faster. On this reading well-written page copy is the primary
mechanism and alt text supplements it. [[2024-11-15_alt-text-usability]]
*Both sources agree* generated alt text is a first draft at best: AI struggles
with context and intent. [[2024-11-22_write-alt-text]]
[[2024-11-15_alt-text-usability]]

## The wider floor

**A15. Assume level-1 computer skills for a broad consumer audience.**
Design teams sit in the top 5 to 8 % of computer skills worldwide while 26 % of
adults across OECD countries cannot use a computer at all. Level 1 means little
navigation, few steps, explicit criteria, simple reasoning, minimal information
integration. Exceeding it serves roughly a third of the population or less.
[[2016-11-13_computer-skill-levels]]

**A16. Input fields accept the names people actually have.**
Character limits and bans on hyphens, apostrophes and accented characters
exclude non-English naming conventions. [[2022-01-30_inclusive-design]]
Regional formats, units and currency conventions follow the same logic and are
grounded in research rather than appearance. [[Localization]]

**A17. Older users need size, contrast and forgiving correction.**
Eighteen years of research with users aged 65+ names small fonts and small
targets as the most persistent barrier, alongside rigid input formats, inability
to correct typos, and error messages that punish people who make more mistakes.
[[2019-09-08_usability-for-senior-citizens]] Younger users have their own
developmental constraints on interaction and reading. [[Young Users]]

**A18. Expectations set by the design are part of accessibility.**
A failed expectation is sticky, and messaging sets it. [[User Expectations]]

## Testing

**A19. Automated tools and expert review do not suffice.**
Test with five users with varied accessibility needs, and use the assistive
tools and keyboard navigation yourself.
[[2022-10-30_visual-treatments-accessibility]]

**A20. Real sessions run on the participants' own devices.**
Their devices are heavily customised. Allow at least 30 extra minutes for setup
and troubleshooting, run in their homes, and facilitate with someone who
understands how screen readers work. Recruiting through local chapters of blind
advocacy organisations costs under half what specialised agencies charge and
builds a sustainable panel. [[2023-05-14_mobile-accessibility-research]]
For older adults: recruit for varied ability rather than assuming homogeneity,
meet in familiar locations, keep sessions short against cognitive fatigue, and
state explicitly that the design is under test, not the person.
[[2023-07-23_usability-testing-older-adults]]

## Why it pays twice

AI agents read interfaces by vision, by parsing the accessibility tree, or by
API, and tree parsing is the cheaper and more reliable route. Semantic HTML,
clear labelling, predictable patterns and proper ARIA make an interface
agent-friendly for the same reason they make it accessible.
[[2026-04-10_ai-agents-as-users]]
