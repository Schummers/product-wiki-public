---
type: concept
name: Accessibility
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Accessibility Research"
  - "Accessibility in Design"
  - "Accessibility in Testing"
  - "Accessibilité"
  - "Accessibilité Web"
  - "Assistive Technology"
  - "Image Accessibility"
  - "Mobile Accessibility"
  - "Web Accessibility"
---

# Accessibility

## Definition

Accessibility is the practice of designing digital products so that people with
disabilities — auditory, cognitive, physical, visual — can perceive, navigate
and interact with content effectively [[2023-04-30_screen-reader-users-on-mobile]].
It is measured against standards, chiefly the Web Content Accessibility
Guidelines, alongside platform-specific guidance such as Apple's
Human-Interface Guidelines and Google's Material Design
[[2022-10-30_visual-treatments-accessibility]]. With 61 million adults in the
United States living with disabilities, the sources treat it as essential
rather than optional [[2022-10-30_visual-treatments-accessibility]]. It is
deliberately narrower than inclusive design, which also addresses age, culture,
economic situation, education, gender, geography, language and race, and
narrower than universal design, which enforces a single solution for everyone
[[2022-01-30_inclusive-design]].

Across the corpus, accessibility is repeatedly described as structural rather
than additive. It is a property of how an interface is coded, labelled and
sequenced, not a layer bolted on afterwards: third-party accessibility plugins
are largely ignored by screen-reader users, who already have more powerful
built-in operating-system screen readers
[[2023-04-30_screen-reader-users-on-mobile]], and native components broken by
excessive technical customisation take every form built on them down with them
[[2025-08-12_390_Designer_une_checkbox_-_Guide_UX_avancé]]. The sources also
insist the benefit is not confined to disabled users: the same visual-treatment
guidelines that make information perceivable and operable for people with
vision, motor or cognitive disabilities improve the experience for everyone
[[2022-10-30_visual-treatments-accessibility]], and design barriers such as
small text, poor contrast and complex interactions that disproportionately hurt
older users hurt all ages [[2019-09-08_usability-for-senior-citizens]]. Barriers
also extend beyond disability into skill: a quarter of adults across OECD
countries cannot use a computer at all, which makes many interfaces inherently
inaccessible to people without advanced technical skills
[[2016-11-13_computer-skill-levels]].

## Practice

### Never make one channel the only channel

The most widely shared rule in the corpus is redundancy: any capability offered
through a single modality must also exist through another. Enhanced or
accelerated interactions may be implemented, but the UI must never rely on them
for any task, whether the constraint is the device or the user's familiarity
with the interaction [[2016-05-01_enhancement]]. Title-attribute tooltips
illustrate the failure mode: they can help mouse users preview a link, but link
text and surrounding context must be understandable without them, since most
touchscreen browsers do not display them at all [[2016-06-19_title-attribute]].
The same reasoning applies to the mouse cursor — cursor changes are a cheap,
high-value discoverability signal, but an interface must never depend
exclusively on the mouse, and keyboard and touchscreen paths must remain
[[2025-03-18_369_Guide_UX_Curseur_de_souris_natif_et_custom]]. Date fields
should accept typed input in multiple formats as well as pickers and lists, so
that users with different abilities and preferences all have a workable route
[[2017-01-22_date-input]].

Colour is the canonical single channel to avoid. Colour-blind users cannot
distinguish elements by colour alone, so colour changes must be combined with
patterns, icons, strokes or other non-colour signals
[[2022-10-30_visual-treatments-accessibility]]. Quantitative testing of visual
indicators found combined colour-and-icon differentiation best across all UX
metrics, with icons providing the fallback when colour fails
[[2016-08-07_visual-indicators-differentiators]]. In data visualisation, the
guidance is to avoid red/green pairings, use colour-blind-safe palettes, and
provide text labels or hover details as secondary signals for anything encoded
in colour [[2019-09-29_treemaps]]. Colour palettes should be usability-tested
for legibility, contrast and colour-blindness compatibility rather than assumed
to work [[2021-06-06_color-enhance-design]]. In-page tabs follow the same
pattern: the selected tab should be marked by at least two cumulative visual
indicators, for example an underline plus a colour change
[[2025-01-07_359_In-page_tabs_-_Guide_UX_design]].

### Contrast and visual treatment

Text-to-background contrast should reach at least 4.5:1 for normal text and 3:1
for large text, verified with contrast-checking tools; low-contrast text harms
readability for users with low vision and reduces comfort for everyone
[[2022-10-30_visual-treatments-accessibility]]. Contrast requirements do not
bend for aesthetics: neobrutalism's bold palettes still have to meet WCAG
ratios, and vibrant pairings such as yellow and cyan that fail readability tests
should be avoided [[2025-04-11_neobrutalism]]. Glassmorphism creates a harder
case, because translucent surfaces let text fall across several background
colours and make contrast ratios unpredictable; designers must verify contrast
across the range of backgrounds and, where feasible, expose user controls such
as contrast adjustment or reduced transparency
[[2024-06-07_glassmorphism]]. Older users affected by presbyopia and cataracts
need large font sizes, high contrast, clean typefaces and font-size controls
[[2022-01-30_inclusive-design]].

Contrast polarity is one place the sources are more nuanced than a single rule.
Light mode with positive contrast polarity generally performs better for users
with normal or corrected vision, yet dark mode helps at night, at very small
font sizes, and specifically for users with cloudy ocular media such as
cataracts, where less emitted light reduces scattering distortion; the
recommendation is to offer dark mode as a pervasive option without necessarily
making it the default [[2020-02-02_dark-mode]].

### Keyboard operation and focus

Keyboard focus states must be visually obvious — a clear stroke or border around
the focused element, with the default browser outline being what users expect
[[2022-10-30_visual-treatments-accessibility]]. Focus is listed among the five
core button states, alongside ARIA attributes and contrast standards, as
essential for keyboard navigation and screen-reader compatibility; the focus
state should appear within 100–150ms of the Tab press so users do not miss it
[[2025-04-25_button-states-communicate-interaction]]. Tooltips must be
reachable by keyboard focus as well as mouse hover, so keyboard users get the
same information [[2019-01-27_tooltip-guidelines]]. Modals must be closable from
the keyboard, Escape included, as well as compatible with screen readers
[[2024-09-24_347_Fenêtre_modale,_le_Guide_UX_Design]], and tabs must be readable,
visually identifiable and keyboard-navigable
[[2025-01-07_359_In-page_tabs_-_Guide_UX_design]]. Drag-and-drop needs an
explicit keyboard path: grab handles reachable with Tab, spacebar to grab, and
screen-reader messaging announcing available actions, the grabbed state, and
current position or size [[2020-02-23_drag-drop]].

### Screen readers and semantic structure

Screen readers present information one element at a time, which forces users to
swipe through everything and hold it in memory to build a mental model
[[2023-04-30_screen-reader-users-on-mobile]]. Consequences for design: scanning
by jumping between headings and links only works if those elements are coded
semantically, since visual styling alone is insufficient; labels must be
frontloaded with keywords because users do not listen to entire labels; and when
an overlay or menu opens, screen-reader focus must move to the new content
[[2023-04-30_screen-reader-users-on-mobile]]. Mega menus raise parallel
problems, with screen-magnifier users seeing only part of the menu, and the
recommended answer is a simple fallback (clickable top-level items leading to
full pages) alongside the advanced screen-reader-accessible implementation
[[2017-03-26_mega-menus-work-well]]. Heavily customised checkboxes risk breaking
screen-reader compatibility, and an inaccessible base component makes every form
that uses it inaccessible [[2025-08-12_390_Designer_une_checkbox_-_Guide_UX_avancé]].
Audio-only phone trees create comparable barriers, where the ARIA feed role and
explicit support for the phone's back button are the improvements named
[[2022-08-14_phone-tree-guidelines]].

Input is a distinct problem from output. Touchscreen keys feel identical, so
screen-reader users must rely entirely on audio feedback to know what they
typed, and most prefer dictation despite its transcription errors and homophone
confusions; voice assistants cut navigation steps, and Braille displays give
tactile precision and silence at the cost of price and portability
[[2023-05-28_screen-reader-type-control]]. Gestural control allows navigation
but offers far fewer direct actions than desktop keyboard shortcuts, so complex
typing requirements should be avoided and screen-reader users treated as a
default audience rather than an afterthought
[[2023-05-28_screen-reader-type-control]].

### Images and alt text

Alt text should be provided for images that support screen-reader users
[[2023-07-23_imagery-in-visual-design]], written succinctly, describing the
image's role rather than replicating captions, and omitted on purely decorative
images to reduce cognitive load [[2022-10-30_visual-treatments-accessibility]].
Practically: keep it to roughly 150 characters or less, frontload the most
important information, and let context and the author's intent decide what it
says, since the same image needs different alt text in different places
[[2024-11-22_write-alt-text]]. Decorative images take an empty alt attribute,
functional images describe the action they afford, and informative images
highlight their unique value without restating page copy; complex images such as
charts may be better served by restructuring the page copy into a table or list,
or by a long description [[2024-11-22_write-alt-text]].

The corpus pushes back on the reflex of alt text everywhere. Adding alt text to
redundant images — those whose information already appears in the page copy —
raises interaction cost and wastes screen-reader users' time, so the test is a
three-question decision tree: is the information repetitive, is the image
referenced by the page copy, and would alt text help users complete tasks more
efficiently [[2024-11-15_alt-text-usability]]. On this reading, well-written page
copy is the primary accessibility mechanism and alt text supplements it
[[2024-11-15_alt-text-usability]]. Both sources agree that automatically
generated alt text is not a solution: AI tools struggle with context and intent,
and their output is at best a first draft requiring human verification
[[2024-11-22_write-alt-text]], if it does not simply add interaction cost
[[2024-11-15_alt-text-usability]].

### Targets, dexterity and physical interaction

Touch targets should be at least 1cm × 1cm as physically rendered, since pixel
dimensions are meaningless across device densities; the constraint is target
size, not "fat fingers" [[2019-05-05_touch-target-size]]. Users with limited
dexterity — young children, seniors, people with disabilities — and users in
challenging conditions such as movement or one-handed use need targets above
that minimum, and adequate spacing matters as much as size because crowded
targets cause slips [[2019-05-05_touch-target-size]]. View-tap asymmetry, where
elements are large enough to see but too small or dense to tap, is a common
artefact of desktop-to-mobile conversions [[2019-05-05_touch-target-size]].
Checkboxes should carry a fully clickable label and a tap area of at least
40×40 pixels including surrounding space
[[2025-08-12_390_Designer_une_checkbox_-_Guide_UX_avancé]]. Tiny options in mega
menus produce selection errors on touchscreens and pose motor-skill problems
[[2017-03-26_mega-menus-work-well]]. On mobile, drag-and-drop is weak — no hover
states for signifiers, fat-finger issues, taps hard to distinguish from swipes —
so menu-based alternatives, though longer, reduce errors
[[2020-02-23_drag-drop]]. Larger foldable screens are noted as an accessibility
gain for users with visual impairments and older adults
[[2025-01-10_foldable-smartphones]].

### Motion and animation

Excessive animation, flashing, parallax, scroll-jacking and carousel animation
can cause vestibular symptoms (dizziness, nausea, migraine) and trigger seizures
in epileptic users; browser "reduce motion" settings must be respected
[[2020-02-09_animation-duration]].

### Skill, age and the wider gap

Design teams sit in the top 5–8% of computer skills worldwide while 26% of
adults across OECD countries cannot use a computer at all; targeting a broad
consumer audience means assuming level-1 skills, since anything more complex
serves roughly a third of the population or less
[[2016-11-13_computer-skill-levels]]. Level-1 capability defines the floor:
little navigation, few steps, explicit criteria, simple reasoning, minimal
information integration — exceeding it raises accessibility barriers
[[2016-11-13_computer-skill-levels]]. Eighteen years of research with users aged
65+ shows small fonts and small targets as the most persistent barrier, along
with rigid input formats, an inability to correct typos, and confusing error
messages that punish users who make more mistakes
[[2019-09-08_usability-for-senior-citizens]]. Form fields with character limits
or bans on hyphens, apostrophes and accented characters exclude users with
non-English naming conventions [[2022-01-30_inclusive-design]].

### Research and testing

Automated tools and expert review are not sufficient: testing with five users
with varied accessibility needs, such as low vision or motor difficulties,
reveals issues they cannot catch, and designers should also use assistive tools
directly and try keyboard navigation themselves
[[2022-10-30_visual-treatments-accessibility]]. Testing with actual
screen-reader users shows that accessibility is structural rather than a plugin
problem [[2023-04-30_screen-reader-users-on-mobile]]. Recruiting through local
chapters of blind advocacy organisations costs less than half what specialised
agencies charge, and building an ongoing relationship with those communities
creates a sustainable panel [[2023-05-14_mobile-accessibility-research]].
Sessions should run in participants' homes, use participants' own heavily
customised devices, allow at least 30 extra minutes for setup and
troubleshooting, and be facilitated by someone who understands how screen
readers work [[2023-05-14_mobile-accessibility-research]]. Testing with older
adults calls for the same logic: recruit for varied ability rather than
assuming homogeneity, meet participants in familiar locations, make equipment
compatible with screen readers, magnifiers, keyguards, head wands and
voice-recognition software, keep sessions short enough to avoid cognitive
fatigue, and state explicitly that the design is under test, not the person
[[2023-07-23_usability-testing-older-adults]]. AR studies add a health and
safety dimension: screen participants for age, health conditions, physical
ability and whether they can wear glasses during physical activity, and tell
them in advance how much movement is involved and that they may withdraw
[[2022-08-28_testing-ar-apps]]. Underlying all of it, understanding users with
disabilities is presented as requiring direct exposure — observing real sessions
rather than reading reports — because that is what separates empathy from
sympathy [[2019-04-21_sympathy-vs-empathy-ux]].

### Accessibility as infrastructure

Two sources extend the argument beyond human users and standards compliance. AI
agents interact with interfaces by vision, by parsing the accessibility tree, or
by direct API, and accessibility-tree parsing is the cheaper and more reliable
route — so semantic HTML, clear labelling, predictable patterns and proper ARIA
are simultaneously an ethical and a pragmatic investment, making
accessibility-first interfaces already agent-friendly
[[2026-04-10_ai-agents-as-users]]. Generative UI is presented as a potential
accessibility gain, with interfaces tailored in real time to individual needs
[[2024-03-22_generative-ui]]. Heuristic evaluation and cognitive-load reduction
are noted as addressing usability and accessibility concerns together
[[2025-12-19_top-videos-2025]].

## Sources (38)

- [[2016-05-01_enhancement]] — Enhanced features must never be the only way to accomplish tasks, ensuring accessibility for users with different devices, abilities, or familiarity with new interactions.
- [[2016-06-19_title-attribute]] — While title attributes can enhance usability for mouse users, they must not be required for understanding or accessing content, as screen readers and touchscreen users may not have access to them.
- [[2016-08-07_visual-indicators-differentiators]] — Combined icon and color differentiation is more accessible than color alone, which fails colorblind users; icons provide fallback differentiation.
- [[2016-11-13_computer-skill-levels]] — Computer skill gaps are part of the broader digital divide; many designs are inherently inaccessible to people without advanced technical skills.
- [[2017-01-22_date-input]] — allowing multiple input methods (typing different date formats, calendar pickers, lists) makes date fields accessible to users with different abilities and preferences.
- [[2017-03-26_mega-menus-work-well]] — Addresses screen reader compatibility, screen magnifier issues, touchscreen target size, and motor skills impairment considerations for mega menus.
- [[2019-01-27_tooltip-guidelines]] — Emphasizes the need to support keyboard-triggered tooltips alongside mouse-triggered ones for inclusive design.
- [[2019-04-21_sympathy-vs-empathy-ux]] — Empathy for users with disabilities requires direct experience, not just theoretical understanding of challenges.
- [[2019-05-05_touch-target-size]] — Large touch targets benefit users with limited dexterity (young children, seniors, people with disabilities) and users in challenging conditions (moving, one-handed use).
- [[2019-09-08_usability-for-senior-citizens]] — Digital accessibility barriers (small text, poor contrast, complex interactions) disproportionately affect older users; accessible design benefits all ages.
- [[2019-09-29_treemaps]] — Data visualizations using color require accommodations for color-blind users; treemaps should employ redundant signals (text labels, patterns, hover details) alongside color encoding.
- [[2020-02-02_dark-mode]] — Shows that dark mode is beneficial for users with specific visual impairments, particularly those with cloudy ocular media, making it an important accessibility feature.
- [[2020-02-09_animation-duration]] — Highlights serious accessibility concerns with certain animation types and the importance of respecting user motion preferences.
- [[2020-02-23_drag-drop]] — Emphasizes necessity of keyboard support, screen reader messaging, and alternative interactions for users who cannot use mouse-based drag-and-drop.
- [[2021-06-06_color-enhance-design]] — Color use must be tested for legibility, contrast ratios, and color-blindness compatibility to ensure design works for all users.
- [[2022-01-30_inclusive-design]] — A narrower focus than inclusive design; accessibility specifically ensures interfaces work for people with disabilities (auditory, cognitive, physical, visual) and is measured against standards like WCAG.
- [[2022-08-14_phone-tree-guidelines]] — Audio-only interfaces create barriers for screen-reader users and keyboard-only users; the ARIA feed role and support for back buttons improve accessibility.
- [[2022-08-28_testing-ar-apps]] — AR health requirements should be screened in advance; participants should know whether they'll need glasses, how much movement is involved, and whether they can withdraw.
- [[2022-10-30_visual-treatments-accessibility]] — accessible design benefits all users; the five visual-treatment guidelines ensure information is perceivable and operable for users with vision, motor, or cognitive disabilities, and designers should understand how assistive tools such as screen readers, magnifiers, and speech-input interact with focus states, alt text, and semantic HTML.
- [[2023-04-30_screen-reader-users-on-mobile]] — Accessible design requires digital products that enable users with disabilities, including those using screen readers, to perceive, navigate, and interact with content effectively; developers must code with assistive tools like screen readers in mind to support users with visual impairments accessing content through audio.
- [[2023-05-14_mobile-accessibility-research]] — User research specifically focused on how people with disabilities interact with digital products, and understanding of tools like screen readers that enable this access, requires specialized recruiting, methodology, and developer knowledge of how these tools work.
- [[2023-05-28_screen-reader-type-control]] — Designing interactions so users with visual impairments can effectively input information and control devices through tools including dictation, voice assistants, and Braille displays, enabling screen-reader users to interact with mobile devices despite the medium's visual focus.
- [[2023-07-23_imagery-in-visual-design]] — Recommends providing alternative text for images to support screen reader users.
- [[2023-07-23_usability-testing-older-adults]] — Addresses how to design and test digital products to accommodate older adults' visual, hearing, motor, and cognitive needs through supporting assistive technologies such as screen readers and magnifiers that older adults rely on.
- [[2024-03-22_generative-ui]] — highlights genUI's potential to improve accessibility and inclusivity through interfaces tailored to individual needs.
- [[2024-06-07_glassmorphism]] — the article emphasizes that translucent designs must maintain contrast, provide user controls, and consider WCAG compliance to remain accessible.
- [[2024-09-24_347_Fenêtre_modale,_le_Guide_UX_Design]]
- [[2024-11-15_alt-text-usability]] — Focusing purely on accessibility (alt text for every image) without considering usability (whether screen-reader users actually need that information) fails to achieve the real goal of making the web usable for all; screen-reader users navigate and process web pages sequentially, fundamentally different from sighted users' visual scanning patterns.
- [[2024-11-22_write-alt-text]] — Covers the accessibility implications of different image types and how proper alt text contributes to making web content accessible and usable for people using assistive technology.
- [[2025-01-07_359_In-page_tabs_-_Guide_UX_design]]
- [[2025-01-10_foldable-smartphones]] — Explains how larger screens on foldable devices provide accessibility benefits for users with visual impairments and older adults.
- [[2025-03-18_369_Guide_UX_Curseur_de_souris_natif_et_custom]]
- [[2025-04-11_neobrutalism]] — emphasizes that accessibility standards (contrast ratios, readability) remain non-negotiable even in bold, unconventional aesthetics; tools and standards ensure functionality alongside striking design.
- [[2025-04-25_button-states-communicate-interaction]] — highlights focus state, ARIA attributes, and contrast standards as essential for keyboard navigation and screen reader compatibility.
- [[2025-08-12_390_Designer_une_checkbox_-_Guide_UX_avancé]]
- [[2025-12-19_top-videos-2025]] — Heuristic evaluation and cognitive load reduction address both usability and accessibility concerns central to the year's most-watched content.
- [[2026-04-10_ai-agents-as-users]] — Shows accessibility best practices as foundational to agent-friendly design, not separate concern.
- [[2024-01-23_laws-of-ux_10-8-von-restorff-effect]] — Inclusive design requires contrast beyond color alone (patterns, strokes, shape), sufficient color contrast ratios (4.5:1 for text), and careful motion use to avoid excluding users with visual impairments or vestibular disorders.
