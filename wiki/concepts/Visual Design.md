---
type: concept
name: Visual Design
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Color and Contrast"
  - "Design Aesthetics"
  - "Visual Design Glossary"
  - "Visual Design Impact"
  - "Visual Design Systems"
---

# Visual Design

## Definition

Visual design is the deliberate arrangement of visual elements — scale, color,
contrast, typography, spacing, imagery, layout — to make an interface
understandable, usable and emotionally appropriate. The sources are consistent
on one framing above all: it is not decoration but a functional component of UX
[[2022-11-06_visual-design-in-ux-study-guide]] [[2020-03-01_principles-visual-design]].
Its work is to establish hierarchy so users consume elements in the intended
order of importance [[2021-01-17_visual-hierarchy-ux-definition]], to group and
separate content so relationships are legible [[2020-07-12_common-region]]
[[2020-09-06_gestalt-similarity]], and to make the relevant look relevant so
that a reader scanning quickly lands where the task is
[[2017-10-01_first-impressions-human-automaticity]]. Good design in this account
is not accidental: it is the consistent application of a small set of principles
rather than complexity or ornament [[2021-03-07_why-does-design-look-good]]
[[2023-03-05_why-does-a-design-look-good-part2]] [[2025-11-14_good-visual-design]].

The sources also treat visual design as a perceptual and social signal, not only
a functional one. Aesthetic judgments are made in about 50 milliseconds and
rarely revised [[2017-10-01_first-impressions-human-automaticity]]; attractive
design makes people perceive a product as more usable and tolerate minor flaws
[[2024-02-03_aesthetic-usability-effect]]; the visual treatment of a page primes
unconscious inferences about the business behind it [[2016-01-24_priming]] and
feeds credibility judgments through which elements are prominent and how they
are interpreted [[2018-08-19_prominence-interpretation-theory]]. That leverage
cuts both ways, and the recurring tension in the corpus is between visual appeal
and functional clarity: several sources document styles and effects that look
striking while degrading readability, discoverability or accessibility
[[2025-10-10_liquid-glass]] [[2019-01-20_parallax-usability]]
[[2017-12-17_visual-newsletters]] [[2017-11-05_brutalism-antidesign]]. The
consensus position is that form and function must support rather than compete
with each other, and that aesthetics cannot rescue a product from serious
usability failures [[2024-02-03_aesthetic-usability-effect]].

## Practice

### The core principles

Five principles are presented as the foundation: scale (relative size signals
importance and rank), visual hierarchy (variations in scale, value, color,
spacing and placement lead the eye), balance (visual weight distributed around
an axis, symmetrically or not), contrast (dissimilar elements read as different
categories or functions), and the Gestalt principles that explain how people
organise elements into wholes [[2020-03-01_principles-visual-design]]. A
glossary source organises the same field as principles (Gestalt, hierarchy)
plus practical techniques (color, typography, spacing), adding that consistency
— internal to the product and external to conventions — reduces cognitive load,
and that whitespace is a design element rather than leftover space
[[2024-05-17_visual-design-cheat-sheet]]. A third source reduces the field to
four working principles — grids, typography, colour and imagery — and argues
that what separates good visual design from bad is not the principles
themselves but their intentional and consistent application across every page;
its closing claim is that how an interface looks changes how well users think
it functions, which is what makes those principles a usability matter and not a
matter of taste [[2025-11-14_good-visual-design]].

Hierarchy is built primarily through color and contrast, scale, and grouping
[[2021-01-17_visual-hierarchy-ux-definition]]. Limiting the design to about
three sizes is repeated across sources: three sizes create variety while keeping
rank legible [[2020-03-01_principles-visual-design]]
[[2021-01-17_visual-hierarchy-ux-definition]] [[2025-11-14_good-visual-design]].
Content itself can disrupt an otherwise sound hierarchy — a strongly colored
photo can dominate a well-built template — which is why hierarchy should be
validated rather than assumed [[2021-01-17_visual-hierarchy-ux-definition]].

Among the Gestalt principles, two are treated in depth. **Common region**: items
inside a boundary are perceived as grouped, and a boundary overpowers proximity
or similarity, which makes containers useful when whitespace alone cannot
resolve grouping — for separating chrome from content, and in cards and
accordions [[2020-07-12_common-region]] [[2016-11-06_cards-component]]. The same
source warns against overuse: unnecessary borders and colored boxes create
visual clutter and false floors that stop scrolling
[[2020-07-12_common-region]]. **Similarity**: shared color, shape or size makes
elements read as related and as functioning alike, which is how users build
accurate mental models; the pitfall is that unrelated content displayed at
similar size reads as equivalent, as when ads in a right rail look as important
as content [[2020-09-06_gestalt-similarity]].

One source offers a mathematical alternative route to balance and proportion:
the golden ratio, applied to header sizes (body size × φ), line heights, image
cropping via a golden spiral, and two-column layouts. It presents this as useful
for designers who want a concrete starting point, while noting it is one method
among many and that responsive design makes strict application difficult
[[2021-10-31_golden-ratio-ui-design]].

### Grids, layout and spacing

Grids are described as foundational: they create order and coherence through
consistent alignment, help designers align quickly, and help users scan a
predictable layout [[2022-07-17_using-grids-in-interface-designs]]
[[2025-11-14_good-visual-design]]. Every grid is columns, gutters and margins;
column widths should be percentages so they adapt (often 12 columns on desktop,
fewer on smaller devices) while gutter widths are fixed values that vary by
breakpoint — wider on large screens, narrower on mobile
[[2022-07-17_using-grids-in-interface-designs]]. Gutter width also carries
meaning: thin gutters for airy content, wide gutters to separate callouts
[[2025-11-14_good-visual-design]]. Three grid types serve different needs:
column grids for general layouts, modular grids for ecommerce and listing pages,
hierarchical grids for importance-driven layouts such as news
[[2022-07-17_using-grids-in-interface-designs]]. An 8px system is recommended
because most screen dimensions are multiples of 8. Breaking the grid
deliberately can emphasise an item, but doing so inconsistently produces chaos
and hurts scannability [[2022-07-17_using-grids-in-interface-designs]].
Analyses of real sites confirm that alignment to a grid — three-column or
modular — is what makes a design look crisp and intentional rather than
arbitrary [[2021-03-07_why-does-design-look-good]]
[[2023-03-05_why-does-a-design-look-good-part2]].

Spacing does comparable work. Generous leading beyond the default (4–6px extra
on paragraph text is suggested) makes text feel open rather than dense
[[2021-03-07_why-does-design-look-good]]; appropriate line length and white
space between elements are what make a design comfortable to read
[[2023-03-05_why-does-a-design-look-good-part2]]. In intranets, the opposite is
one of the enduring failures: no layout strategy, no clear hierarchy, and
whitespace and graphic positioning left unmanaged, producing cluttered pages
where employees miss critical information
[[2016-11-27_top-intranet-design-mistakes]].

Layout choices interact with images. Eyetracking of zigzag (alternating
image–text) versus aligned layouts found that when images are informative both
layouts perform equally, because users attend to both; when images are
decorative, zigzag causes users to stumble onto them and redirect, while aligned
layouts let text scanning proceed smoothly. The recommendations are aligned
layouts for decorative images, informational content on the left, text
top-aligned with decorative images, and no early complex imagery
[[2017-11-26_zigzag-page-layout]].

### Typography

Typography is treated as a core component of visual design with measurable
impact on legibility and perceived polish [[2024-05-10_typography-terms-ux]],
working alongside color, spacing and layout to build hierarchy
[[2022-06-19_pairing-typefaces]]. Hierarchy comes from size, weight and color
within a limited number of type families — one source quantifies important text
as 30–50% larger [[2023-03-05_why-does-a-design-look-good-part2]] — and from
using multiple weights of a single typeface rather than reaching for more
typefaces [[2022-06-19_pairing-typefaces]]. The three sizes are conventionally
a large primary, a medium secondary and a small caption size, and hierarchy
alone is not enough: leading and line length have to be set for reading, not
just for rank [[2025-11-14_good-visual-design]]. Headlines should carry at most two
different treatments, and a given type style (bold, italic, small caps) should
mean the same thing on every page [[2021-03-07_why-does-design-look-good]].

For pairing: six classifications (serif, sans-serif, slab-serif, script, display,
monospaced) narrow the field; decorative typefaces belong in headers and
illustrations only, paired with a neutral serif or sans-serif for body copy;
each typeface needs a distinct role, and using two typefaces for body copy looks
inconsistent and diminishes trust [[2022-06-19_pairing-typefaces]]. Practical
selection checks include support for multiple languages (users translate pages)
and character distinctness, especially 1, I and l, which matters in
alphanumeric, financial and healthcare contexts
[[2022-06-19_pairing-typefaces]]. The typography glossary adds the underlying
vocabulary — typeface versus font, kerning versus letter spacing, leading
measured baseline to baseline, baseline and x-height as proportion measures —
and notes that serif carries traditional, warm connotations while sans-serif
reads modern and impersonal, and that non-web-safe fonts may not render or be
read by screen readers [[2024-05-10_typography-terms-ux]].

### Color and contrast

Restraint is the dominant recommendation. Refined palettes of two to three
carefully chosen colors give focus and stronger brand representation, and
primary CMYK colors are called out as looking unsophisticated
[[2021-03-07_why-does-design-look-good]]. Monochromatic (three to four colors)
or dual-color palettes are described as the easiest to execute well and as
enforcing hierarchy, with imagery given center stage and neon avoided
[[2023-03-05_why-does-a-design-look-good-part2]] [[2025-11-14_good-visual-design]].
For UX maps, palettes of three to six colors either follow company branding or
encode map attributes, applied consistently across related maps
[[2022-12-04_ux-mapping-methods-visual-design-guide]]. Even the boldest style in
the corpus prescribes limiting to two or three high-contrast colors
[[2025-04-11_neobrutalism]].

Color is also a functional signal: shared color unites elements and communicates
that they work alike, link color must be reserved for clickable things, and a
separate color should be reserved for the primary call to action so users do not
have to work out which button is primary [[2020-09-06_gestalt-similarity]].
High-contrast color can mark a distinct category or consequence, such as red for
delete [[2020-03-01_principles-visual-design]].

Contrast is where visual design and accessibility meet. Text and graphical
elements must hold sufficient contrast against their background
[[2024-05-17_visual-design-cheat-sheet]]; reducing text contrast to de-emphasise
content is explicitly rejected because it compromises accessibility
[[2020-03-01_principles-visual-design]]; small light-gray text on white is named
as a recurring intranet failure, made worse by glare on portable devices
[[2016-11-27_top-intranet-design-mistakes]]. Bold aesthetics do not exempt a
design from WCAG contrast ratios, and specific vibrant pairings such as yellow
and cyan are called out as failing readability
[[2025-04-11_neobrutalism]]. Accessibility and visual design are described as
inseparable — contrast, focus states, alt text and semantic meaning
[[2022-11-06_visual-design-in-ux-study-guide]]. Relatedly, color alone is an
unsafe differentiator: it fails colorblind users and is open to interpretation,
so it should be combined with another cue
[[2016-08-07_visual-indicators-differentiators]].

On contrast polarity, the evidence favors light mode for users with normal or
corrected vision — the pupil contracts, reducing spherical aberration and
increasing depth of field — but dark mode outperforms at night, at very small
font sizes, and for users with cloudy ocular media such as cataracts. The
recommendation is to offer dark mode pervasively as an option without making it
the default, especially for long-form reading
[[2020-02-02_dark-mode]].

### Imagery and icons

Imagery serves four functions — engagement, brand identity, communicating
complex concepts, emotional connection — across four types: photographs,
illustrations, iconography and data visualization
[[2023-07-23_imagery-in-visual-design]]. The recurring test is informational
value: information-carrying images (product photos, infographics, software
screenshots) over decorative stock imagery, which adds little and is quickly
overlooked [[2023-07-23_imagery-in-visual-design]]
[[2024-05-03_7-tips-memorable-imagery]]. An image earns its place by carrying
product information or by expressing the brand; balanced, centred photographs
free of clutter serve both, while anything that competes with the content
around it fails the test [[2025-11-14_good-visual-design]].
Practical guidance: match exposure, brightness, contrast and style across images
so no single one draws undue attention; balance density (text-heavy layouts
tolerate detailed, textured imagery, minimalist layouts call for simpler
images); keep total page weight around 1–2MB using formats such as WEBP or PNG;
and keep a high data-ink ratio in infographics, avoiding shadows, grid lines and
3D effects [[2023-07-23_imagery-in-visual-design]]. Seven further rules: make
images reinforce the text, avoid generic stock, show products in realistic
context, place visuals near their related text and keep that proximity across
breakpoints, use few strong visuals rather than many similar ones (excess
weakens hierarchy), use high resolution, and account for cross-cultural
interpretation [[2024-05-03_7-tips-memorable-imagery]].

The cognitive case for images is the picture-superiority effect: dual-coding
theory holds that images are stored both as image and as a word description,
making them more memorable than words. Its strength depends on discoverability,
clarity, familiarity and uniqueness — hence placing important visuals where
users spend time and above the fold, keeping them from auto-rotating, choosing
literal over abstract images, and making imagery distinct from both competitors
and surrounding elements. Text nonetheless remains essential to usability
[[2024-04-26_picture-superiority-effect]].

Responsive behavior is treated as a design decision, not a scaling operation.
Scaling large-screen images down produces illegible overlay text, cropping that
changes meaning, portrait/landscape mismatches, and grids that stack into
excessive scrolling; the remedies are to remove images with little value, resize
and crop to preserve meaning, and edit text placement — shortening it, moving it
from overlay to below or beside the image, increasing contrast
[[2017-05-21_big-pictures-small-screens]]. Scaling up has mirror problems:
disproportionate enlargement wastes space and lowers information density,
vertical cropping removes meaning, and repositioning breaks the relationship
between image and text; the answers are combining scaling with careful cropping,
choosing images that tolerate several aspect ratios, setting maximum dimensions
and filling the rest with white space or complementary content, or swapping
images per breakpoint [[2017-07-23_small-pictures-big-screens]].

Icons get a cost-benefit framing. Their true cost includes design and research,
coding and QA, screen real estate, and added visual noise; each icon must earn
more than that. Bad icons reuse an established meaning for something else, rely
on esoteric references, are blurry, repeat pointlessly on every list item, or
only make sense as a set. Good icons map naturally to their concept, are simple,
need no decoding, are understood in a single fixation, and survive small sizes.
They are often added for the wrong reasons — to break up text, add visual
interest, or follow a trend [[2017-11-19_bad-icons]]. Where icons do work, they
work best combined with other cues: testing four indicator families in mobile
lists, color-plus-icon performed best across all metrics, icon-only slightly
beat color-only, and text-only was 57% slower to task completion and 56% slower
to first correct click [[2016-08-07_visual-indicators-differentiators]]. Icon
stroke weight should be consistent within a set and aligned with the weight of
the accompanying typeface [[2023-07-23_imagery-in-visual-design]]; consistent
icon sets plus a legend are recommended for maps
[[2022-12-04_ux-mapping-methods-visual-design-guide]]. Illustrations that read
fine in isolation can confuse readers without context, and misassociation
between an illustration and its text can be fixed by color-coding them together
[[2021-03-21_visual-design-heuristics-posters]].

Emoji are a special case: in email subject lines they attract attention through
visual salience (considered in 33% of selections versus 9%) but increase
negative sentiment by 26%, reduce perceived value, and do not raise intent to
open that email. They shift attention to visual characteristics and away from
meaning, so they should be reserved for cases where they genuinely add context
[[2020-06-28_emojis-email]].

### Consistency, systems and brand

Consistency is what turns individual choices into polish: define explicit rules
for spacing, typography and padding, then apply them everywhere
[[2021-03-07_why-does-design-look-good]] [[2025-11-14_good-visual-design]].
Design systems and style guides are the mechanism for holding typeface roles and
patterns steady across products [[2022-06-19_pairing-typefaces]], and design
systems are one of the six areas the study guide treats as core to visual design
[[2022-11-06_visual-design-in-ux-study-guide]]. Across channels — web, mobile,
email, kiosk, packaging — consistent color palettes, imagery and typography tell
a unified brand story and signal an integrated organisation; extreme visual
inconsistency suggests fragmentation and raises doubts about whether offerings
or values differ. That source also concedes that channels have different
affordances, so some divergence is legitimate provided core workflows and brand
presentation stay consistent [[2016-10-16_omnichannel-consistency]].

Mood boards are the upstream tool for setting visual direction: collages of
images, colors, patterns and type that convey the intended feeling before
detailed design starts, built during the define or ideate phase and used to
align the team. All the collected material should fall under one theme —
contradicting aesthetics mean you need separate boards — and the board itself
benefits from hierarchy (size and central placement for key references, similar
items grouped). Too many competitor screenshots turn a mood board into a feature
comparison [[2023-02-26_mood-boards]].

### Perception, first impressions and credibility

Visual design operates largely on automatic cognition. System 1 makes snap
judgments using color, size and position, and information that does not look
relevant is ignored even when it is useful; beauty is judged within 50ms and
that judgment rarely changes. The design response is to identify what each
persona needs at each stage and make that information look important through
hierarchy, contrast and positioning, and to state clearly who you are and what
you do [[2017-10-01_first-impressions-human-automaticity]].
Prominence-interpretation theory formalises the credibility side: users judge a site by
which elements are prominent and how they interpret them; prominence depends on
involvement, topic, task and expertise, interpretation on culture, experience
and expectations. Visual tone of voice can be right for one industry and wrong
for another, and both halves can be tested — five-second tests for prominence,
usability testing with follow-up questions for interpretation
[[2018-08-19_prominence-interpretation-theory]].

Priming works in the same register: aesthetic treatment produces unconscious
inferences about the business — a less polished design can prime perceptions of
local authenticity, a polished one of corporate establishment — and images and
page content set expectations whose confirmation or violation is experienced as
good or bad usability [[2016-01-24_priming]]. The aesthetic-usability effect
completes the picture: attractive design makes users more forgiving of minor
problems and more patient, which is a genuine UX benefit, but it does not
survive serious usability flaws, and during research it masks real problems
because participants comment on looks after struggling with tasks. Countermeasures
include low-stress sessions, distancing the facilitator from ownership of the
design, and vague probing questions about functionality and difficulty
[[2024-02-03_aesthetic-usability-effect]].

Learned visual associations can work against legitimate content. Users skip top
banners and right rails, ignore anything using animation, fancy formatting,
colored backgrounds or embedded text because it reads as an ad, and a single ad
can poison an entire adjacent section ("hot potato"). Real content therefore
must not be styled like advertising [[2018-04-22_banner-blindness-old-and-new-findings]],
a failure mode also seen on intranets, where internal announcements styled like
external ads — bright colors, animation, stock-photo people — trigger the same
avoidance [[2016-11-27_top-intranet-design-mistakes]]. Similarity of size
between content and ads produces the same effect
[[2020-09-06_gestalt-similarity]].

### Styles, trends and their trade-offs

The corpus repeatedly evaluates style movements against usability rather than
taste. **Flat design**: a survey of 457 users found young adults (18–25) rated
flat screenshots 0.53 points higher on a 7-point scale than adults 35+
(p<0.00001), with the largest gap on the most minimal design; the skeuomorphic
control drew nearly identical ratings from both groups, making flat design
uniquely polarising. The article questions whether a modest gain in
attractiveness justifies reduced efficiency, click uncertainty and alienating
older users, and notes that content in the screenshots influenced ratings as
much as style [[2016-02-28_young-adults-flat-design]]. A companion piece
clarifies that flatness itself is not the problem — weak or absent visual
signifiers are, and flat design with strong signifiers works fine
[[2017-10-15_response-criticisms-flat-design]].

**Skeuomorphism** began as a functional learning aid borrowing users' mental
models of physical objects (trash bins, folders, floppy disks) before becoming
an excess of textures, shadows and gradients that cluttered interfaces and
slowed load times; flat design was the reaction, and neumorphism a partial
return. The lesson drawn is cyclical: trends answer their predecessor's
limitations, and balance between innovation and familiarity is what works
[[2024-03-15_skeuomorphism]].

**Brutalism and antidesign** are distinguished: brutalism is stripped-down,
raw, honest and can work when confined to visual design while navigation,
hierarchy and interaction stay usable; antidesign deliberately creates visual
chaos, harsh colors and poor hierarchy for humor or attention and backfires for
anyone trying to complete a task, working only in entertainment or
designer-audience contexts [[2017-11-05_brutalism-antidesign]].
**Neobrutalism** is its more colorful, orderly descendant — bold primary colors,
thick borders, geometric shapes, stark single-color drop shadows, chunky
unpolished type, nostalgic 90s skeuomorphic touches — and comes with explicit
constraints: two or three high-contrast colors, bold headlines paired with clean
neutral body fonts, 24–32px whitespace margins, hierarchy through size variation
and color intensity, and WCAG-compliant contrast [[2025-04-11_neobrutalism]].

**Glassmorphism** is the clearest cautionary case: iOS 26's Liquid Glass is
criticised for translucency that obscures content, motion without purpose that
becomes fatigue by the hundredth use, tap targets shrinking below the 1cm²
guideline, controls that appear and vanish and so destroy learnability, and
abandoned conventions that cost long-time users productivity
[[2025-10-10_liquid-glass]]. **Parallax** fares similarly: goal-oriented users
scroll past the effects, slow loading leaves blank screens, excessive motion
causes dizziness and vestibular problems, users have learned to ignore motion as
advertising, and scroll-tied timing cannot be controlled deliberately — so
restraint and never placing content only in parallax
[[2019-01-20_parallax-usability]]. **Handmade aesthetics** are read as the
current pendulum swing: after years of polished AI-generated-looking visuals,
variable line weights, visible brushstrokes, hand-lettering, organic shapes and
deliberate misalignment now signal authenticity, paired with storytelling about
the human artist. It is framed as a trust signal that only holds if the product
backs it up, and adoptable gradually — one campaign or feature at a time
[[2026-04-10_handmade-designs]].

Across these, the sources converge on a single test: user needs dominate, and
designers should not impose complexity or spectacle for their own interest
[[2017-11-05_brutalism-antidesign]] [[2019-01-20_parallax-usability]]
[[2025-10-10_liquid-glass]].

### Beyond the screen: emails, charts, posters, maps

Newsletters show the aesthetics-versus-function tension in miniature. Large,
relevant imagery improves reception, but flyer-style emails that embed the whole
message in one graphic destroy legibility (poor contrast, decorative fonts),
lose typographic hierarchy, bury content below a large hero on mobile, make
preheader text useless, and remove clickability signifiers. Prominent buttons,
colored or underlined links, clear labels and real text are required
[[2017-12-17_visual-newsletters]].

Charts are governed by minimalism focused on the data: context first (a lone
number means nothing without a comparison), bar charts for comparisons with
thoughtful grouping of paired bars, horizontal bars for long labels, line charts
for trends over time, and avoidance of stacked bars, pie and bubble charts and
any form requiring judgment of angle, area or volume
[[2022-01-30_choosing-chart-types]] — consistent with the high data-ink ratio
recommended for infographics [[2023-07-23_imagery-in-visual-design]].

Static artifacts benefit from the same process as products: the heuristics
posters were built by defining design goals up front, exploring layout in
low-fidelity wireframes with real content, iterating in high fidelity on
typeface sizes, color, scale and hierarchy, testing with users, and printing
physically to catch dynamics invisible on screen
[[2021-03-21_visual-design-heuristics-posters]]. UX maps follow a similar
discipline: decide whether polish is warranted by audience and stakes, establish
the visual system (header and body text styles, arrows and lines, labels) before
adding content, build the foundation with title, owner and date plus structural
lines, then refine alignment, distribution and sizing
[[2022-12-04_ux-mapping-methods-visual-design-guide]].

### Validating visual design

Visual design is testable, and several sources insist it be tested. The squint
test — blurring the design — reveals whether groupings and hierarchy actually
work and exposes unintended emphasis [[2021-01-17_visual-hierarchy-ux-definition]]
[[2021-03-21_visual-design-heuristics-posters]]. Subjective appeal can be
measured with instruments such as a modified Microsoft Desirability Toolkit
[[2016-02-28_young-adults-flat-design]]. Prominence can be assessed with
five-second tests and interpretation through post-task questions
[[2018-08-19_prominence-interpretation-theory]]. The study guide places user
testing, desirability toolkits and icon usability studies alongside
accessibility as integral parts of visual design work, since subtle changes in
color, alignment and fonts change the experience
[[2022-11-06_visual-design-in-ux-study-guide]]. Testing also catches
misassociations that reasoning alone misses, such as readers linking an
illustration to the wrong text because of proximity
[[2021-03-21_visual-design-heuristics-posters]]. Two cautions apply to the
research itself: the aesthetic-usability effect biases what participants report
[[2024-02-03_aesthetic-usability-effect]], and task wording or facilitator
behavior can prime participants toward particular terms and behaviors
[[2016-01-24_priming]].

## Sources (45)

- [[2016-01-24_priming]] — aesthetics and visual treatment of pages prime unconscious inferences about business quality, authenticity, and offerings; visual design directly influences user perception, behavior, and satisfaction with the experience.
- [[2016-02-28_young-adults-flat-design]] — measuring subjective visual appeal and emotional responses to interface styles.
- [[2016-08-07_visual-indicators-differentiators]] — Visual differentiation through icons, colors, and combinations significantly impacts how quickly users locate items in lists.
- [[2016-10-16_omnichannel-consistency]] — Shows how consistent visual design (color, imagery, typography) across channels creates unified brand perception and signals organizational integration and trustworthiness.
- [[2016-11-06_cards-component]] — The principle of common regions allows cards to establish visual grouping more effectively than negative space alone, improving content organization.
- [[2016-11-27_top-intranet-design-mistakes]] — Poor visual layout with unclear hierarchy, illegible text, and cluttered pages cause employees to miss critical information; text styling, graphics positioning, and whitespace directly impact scannability.
- [[2017-05-21_big-pictures-small-screens]] — Explores how image cropping, overlay text, spacing, and color contrast interact differently on small screens.
- [[2017-07-23_small-pictures-big-screens]] — visual composition principles applied to responsive contexts, including managing focal points, subject positioning, and aspect ratios.
- [[2017-10-01_first-impressions-human-automaticity]] — effective visual design uses hierarchy, contrast, and positioning to support System 1's automatic pattern recognition and guide users toward task-relevant information.
- [[2017-10-15_response-criticisms-flat-design]] — addresses the relationship between visual style and usability, particularly concerning recognizability of interactive elements.
- [[2017-11-05_brutalism-antidesign]] — addresses design style choices, their motivations, and tradeoffs between aesthetics and usability.
- [[2017-11-19_bad-icons]] — addresses when and how to use icons effectively, balancing aesthetics against usability and cost.
- [[2017-11-26_zigzag-page-layout]] — addresses layout choices and image integration based on informativeness and scanning patterns.
- [[2017-12-17_visual-newsletters]] — The aesthetic use of images, color, typography, and layout; in emails, visual appeal must be balanced against legibility and functional requirements like email client compatibility.
- [[2018-04-22_banner-blindness-old-and-new-findings]] — carefully choosing colors, formatting, and styling to differentiate legitimate content from ads while maintaining visual hierarchy.
- [[2018-08-19_prominence-interpretation-theory]] — the aesthetic and functional arrangement of visual elements; visual design significantly influences credibility assessment through prominence and interpretation of design choices.
- [[2019-01-20_parallax-usability]] — Aesthetic choices like parallax must be evaluated against user goals; beautiful effects that interfere with task completion or create accessibility issues are poor UX choices.
- [[2020-02-02_dark-mode]] — Examines how contrast polarity affects visual hierarchy, readability, and user experience, with evidence for the superiority of light mode in most conditions.
- [[2020-03-01_principles-visual-design]] — Five core principles (scale, hierarchy, balance, contrast, and Gestalt) guide effective visual design and impact usability, emotional response, and accessibility; contrast through color choices (like red for delete) and between text and background is particularly influential.
- [[2020-06-28_emojis-email]] — how emojis shift user attention to visual characteristics and away from message meaning.
- [[2020-07-12_common-region]] — how the principle of common region applies to interface hierarchy, grouping, and visual perception.
- [[2020-09-06_gestalt-similarity]] — Applying consistent visual characteristics (color, shape, size, typography) across UI elements creates clear communication about relationships and functionality, helping users develop accurate mental models.
- [[2021-01-17_visual-hierarchy-ux-definition]] — demonstrates how visual principles like color, scale, and grouping work together to guide user attention and create clarity.
- [[2021-03-07_why-does-design-look-good]] — the article analyzes visual-design principles and how specific design choices affect aesthetics and usability.
- [[2021-03-21_visual-design-heuristics-posters]] — the article addresses visual hierarchy, color, typography, illustrations, and consistency in designing static visual artifacts.
- [[2021-10-31_golden-ratio-ui-design]] — The article explores mathematical approaches to creating visually balanced and aesthetically pleasing interfaces.
- [[2022-01-30_choosing-chart-types]] — Chart design should follow minimalist principles focused on data, not decoration; avoid Excel's default styles and complex visual effects that obscure meaning.
- [[2022-06-19_pairing-typefaces]] — Typography works alongside color, spacing, and layout to create hierarchy and guide user attention through interfaces and sites.
- [[2022-07-17_using-grids-in-interface-designs]] — Grids are foundational visual design tools that create order, hierarchy, and visual coherence through consistent alignment and spacing.
- [[2022-11-06_visual-design-in-ux-study-guide]] — strategic visual design improves usability and brand perception; design principles and elements guide attention, organize information, and support user goals.
- [[2022-12-04_ux-mapping-methods-visual-design-guide]] — Establishing consistent styles for text, color, arrows, and labels early reduces decision-making friction and ensures maps remain cohesive and professional throughout their creation.
- [[2023-02-26_mood-boards]] — mood boards establish visual direction through collected images, color palettes, typography, and patterns that convey the product's intended aesthetic.
- [[2023-03-05_why-does-a-design-look-good-part2]] — visual design excellence comes from consistent application of principles like grids, typography, color harmony, and balance rather than decoration or complexity.
- [[2023-07-23_imagery-in-visual-design]] — Outlines best practices for choosing, styling, and organizing imagery to support usability and brand identity.
- [[2024-02-03_aesthetic-usability-effect]] — fundamental to the aesthetic-usability effect, influencing user emotions and perceptions of product quality.
- [[2024-03-15_skeuomorphism]] — demonstrates how design aesthetics and realistic elements affected both user comprehension and system performance.
- [[2024-04-26_picture-superiority-effect]] — applies cognitive psychology research to guide strategic visual design decisions.
- [[2024-05-03_7-tips-memorable-imagery]] — provides seven specific guidelines for effective visual design implementation.
- [[2024-05-10_typography-terms-ux]] — typography is situated as a core component of visual design with measurable impact on legibility, visual polish, and professional appearance.
- [[2024-05-17_visual-design-cheat-sheet]] — Systematically defines visual design concepts as a combination of principles (Gestalt, hierarchy) and practical techniques (color, typography, spacing), providing a comprehensive reference tool that enables designers to communicate precisely with teammates and understand the conceptual foundations of interface design.
- [[2025-04-11_neobrutalism]] — Explores neobrutalism's visual identity, its evolution from brutalism, and its nostalgic 90s elements like skeuomorphism and chunky typography, while focusing on practical implementation through high-contrast color systems, contrast ratio standards, palette limitation to avoid overwhelming users, and balancing boldness with clarity.
- [[2025-10-10_liquid-glass]] — Criticizes iOS 26 for prioritizing spectacle and visual novelty over functional clarity; glassmorphic effects create aesthetic appeal while degrading readability and accessibility.
- [[2025-11-14_good-visual-design]] — what this article contributes to this concept
- [[2026-04-10_handmade-designs]] — Documents a shift in design aesthetics away from AI-generated-looking polish toward handmade imperfection.
- [[2024-01-23_laws-of-ux_10-8-von-restorff-effect]] — Strategic use of contrast through color, shape, size, position, and motion to create visual hierarchy and direct user focus toward important elements and actions.
