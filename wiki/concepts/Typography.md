---
type: concept
name: Typography
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Color and Typography"
  - "Legibility"
  - "Readability"
  - "Typography Terminology"
---

# Typography

## Definition

Typography is a key component of almost every digital experience, and its
complexity and jargon make it a common source of misunderstanding
[[2024-05-10_typography-terms-ux]]. It covers the design of text through font
choice, size, weight and spacing, and it is what builds the hierarchy that
guides users to the important information
[[2017-12-17_visual-newsletters]]. The corpus consistently separates two
properties that typographic decisions affect: legibility, the ability to
perceive and distinguish individual characters and symbols — seeing letterforms
clearly — and readability, how complex and easy to understand the words
themselves are [[2016-01-10_ux-quiz-15]], [[2017-11-26_glanceable-fonts]].

Typography is treated as one of the foundational visual-design decisions
alongside grids, colour and imagery [[2025-11-14_good-visual-design]], and as
one of the signalling systems that tells users what things are and how they
relate: link colour signals clickability, button shapes signal actionability,
size signals importance [[2020-09-06_gestalt-similarity]]. A typeface sets the
overall tone and personality of a site or application while increasing or
decreasing readability [[2022-06-19_pairing-typefaces]].

## Practice

### Shared vocabulary

- A typeface (or font family) is the group to which fonts belong; a font is the
  specific combination of typeface, size, style and weight
  [[2024-05-10_typography-terms-ux]].
- Kerning adjusts space between specific character pairs; letter spacing adjusts
  space between all characters uniformly. Leading is measured baseline to
  baseline and should account for the specific typeface and size
  [[2024-05-10_typography-terms-ux]].
- Baseline and x-height determine how a typeface's proportions appear relative
  to others at the same nominal size [[2024-05-10_typography-terms-ux]].
- Serif carries traditional, warm connotations; sans-serif reads as modern and
  impersonal — the choice influences brand perception
  [[2024-05-10_typography-terms-ux]].
- Orphans cause uncomfortable reading and visual imbalance
  [[2024-05-10_typography-terms-ux]].

### Choosing and pairing typefaces

- Six classifications narrow the field: serif, sans-serif, slab-serif, script,
  display and monospaced [[2022-06-19_pairing-typefaces]].
- Choose typefaces that support multiple languages even for a single-language
  site, since users may translate the content, and check the appearance in other
  languages before committing [[2022-06-19_pairing-typefaces]].
- Test character distinctness, especially 1, I and l — critical for alphanumeric
  data and for financial or healthcare contexts
  [[2022-06-19_pairing-typefaces]].
- Reserve decorative typefaces with strong personality for headers and
  illustrations; they are hard to read at small sizes and should never be used
  for body copy, which needs a neutral serif or sans-serif
  [[2022-06-19_pairing-typefaces]].
- Give each typeface a distinct role; using two typefaces for body copy makes a
  design look inconsistent and diminishes trust
  [[2022-06-19_pairing-typefaces]].
- A single family with several weights (light, regular, bold, italic) can carry
  the hierarchy without introducing a second typeface
  [[2022-06-19_pairing-typefaces]].
- Record typeface patterns and roles in a design system or style guide to keep
  products consistent [[2022-06-19_pairing-typefaces]].
- Prefer web-safe fonts: non-web-safe fonts may not render correctly and cannot
  be read by screen readers, which affects accessibility, SEO and usability
  [[2024-05-10_typography-terms-ux]].

### Building hierarchy

- Limit designs to three type sizes (large primary, medium secondary, small
  captions) to establish a strong hierarchy without overwhelming the design or
  the user [[2025-11-14_good-visual-design]].
- Use size, colour and placement intentionally so the important element is seen
  first, and cap headline treatments at two different styles
  [[2021-03-07_why-does-design-look-good]].
- Use different styles from the same family (bold, italic, small caps)
  consistently for the same purpose across pages, so variety differentiates
  content types without breaking cohesion
  [[2021-03-07_why-does-design-look-good]].
- Objects at similar sizes are perceived as sharing the same level of
  importance, so size must be applied consistently to create hierarchy — the
  pitfall being content and advertisements displayed at equal prominence, which
  feeds banner blindness [[2020-09-06_gestalt-similarity]].
- Flattened hierarchy is a real failure mode: emails where everything is bold
  overwhelm users; information must be prioritised through varied weight, size
  and emphasis [[2017-12-17_visual-newsletters]].

### Spacing and proportion

- Increase leading beyond the default — roughly 4 to 6 extra pixels on paragraph
  text — to make text feel more open and less dense
  [[2021-03-07_why-does-design-look-good]].
- Alongside three type sizes, appropriate leading and line length are what
  prioritise reading [[2025-11-14_good-visual-design]].
- One mathematical option is the golden ratio (φ ≈ 1.618): derive header size
  from body size (16px × 1.618 ≈ 26px) and set line heights on the same
  proportion [[2021-10-31_golden-ratio-ui-design]]. That source is explicit that
  this is one method among many — some designers use it everywhere, others hold
  it no more valid than any other way of deriving sizes
  [[2021-10-31_golden-ratio-ui-design]].

### Matching type to the reading context

- Glancing (reading one or two words in isolation) is not the same task as
  scanning or reading. For glancing, bigger is better on every dimension:
  larger sizes, regular rather than condensed width, and uppercase all improved
  recognition speed significantly [[2017-11-26_glanceable-fonts]]. Lowercase
  cost 26% more time, condensed 11.2% more, and the lowercase penalty worsens at
  small sizes [[2017-11-26_glanceable-fonts]].
- Those findings apply to isolated words only. All-caps remains problematic for
  longer passages, where lowercase ascenders and descenders aid legibility
  [[2017-11-26_glanceable-fonts]].
- Apply the glanceable rules where the context demands them — GPS directions,
  notifications, smartwatch displays, AR/VR text — rather than following trends
  toward slim, small, light fonts [[2017-11-26_glanceable-fonts]].
- In email, legibility is critical because resolution and rendering vary widely;
  it depends on sufficient contrast, readable font sizes, and text that is not
  visually obstructed [[2017-12-17_visual-newsletters]]. Embedding an entire
  message in a single graphic destroys legibility through poor contrast and
  decorative fonts, especially for users with vision impairments or small
  screens [[2017-12-17_visual-newsletters]].

### Formatting text for comprehension

- Formatting choices that break up text, bold and italic emphasis on key points,
  and strategic headings are named as technical requirements for comprehension —
  and as what AI-generated product content most often gets wrong, producing
  wall-of-text output where bullet points exist without proper indentation or
  visual emphasis [[2025-04-04_genai-write-for-the-web]].

### Bold aesthetics without losing legibility

- Neobrutalism uses bold, unconventional, "unpolished" typefaces to reinforce
  personality, but its success depends on balancing boldness with usability
  [[2025-04-11_neobrutalism]].
- The stated resolution of that tension: pair bold headlines with clean, neutral
  body fonts, use generous whitespace (24–32px margins) to offset the geometric
  elements, limit the palette to two or three high-contrast colours, and keep
  hierarchy through size variation and colour intensity
  [[2025-04-11_neobrutalism]].
- Accessibility standards do not bend for a trend: contrast ratios must meet
  WCAG, and vibrant pairings that fail readability tests (yellow on cyan) should
  be avoided and checked with a contrast tool [[2025-04-11_neobrutalism]].

## Sources (11)

- [[2016-01-10_ux-quiz-15]] — the ability to perceive and distinguish individual characters and symbols in text (legibility, a visual/perceptual property distinct from semantic complexity) versus the ease with which people can understand the meaning of words and text (readability, concerning text complexity and word choice); legibility is about seeing letterforms clearly while readability concerns comprehension rather than visual clarity.
- [[2017-11-26_glanceable-fonts]] — Establishes size, case, and width tradeoffs for different reading contexts (glancing vs. skimming vs. reading), while distinguishing between legibility (recognizing characters quickly) and readability (comprehending longer passages).
- [[2017-12-17_visual-newsletters]] — Typography combines readability (achieved through sufficient contrast, readable font sizes, and lack of visual obstruction) with hierarchical design through font choice, size, weight, and spacing to guide users to important information; in email where resolution and rendering vary widely, hierarchy is often flattened by making all text equally prominent.
- [[2020-09-06_gestalt-similarity]] — Color and typography are powerful tools for signaling relationships. Link color signals clickability; button shapes signal actionability; and size signals importance. Consistent application prevents misunderstanding.
- [[2021-03-07_why-does-design-look-good]] — the article provides detailed guidance on typographic decisions including font families, leading, kerning, and size variance.
- [[2021-10-31_golden-ratio-ui-design]] — Designers can derive harmonious font size and line-height relationships from golden-ratio mathematics.
- [[2022-06-19_pairing-typefaces]] — Typeface selection and pairing are foundational visual design decisions that affect both aesthetic tone and functional readability.
- [[2024-05-10_typography-terms-ux]] — Typography terminology provides shared vocabulary for designers to communicate about typeface choices and their effects on legibility and brand, including technical terms like ascenders, descenders, leading, kerning, and orphans; typography choices directly affect readability and scannability, with guidance on how decisions like line spacing, font weight, and serif choice influence user comprehension.
- [[2025-04-04_genai-write-for-the-web]] — focuses on technical requirements: formatting choices that break up text, bold and italic emphasis on key points, and strategic headings that aid comprehension.
- [[2025-04-11_neobrutalism]] — highlights the tension between expressive, unconventional headline fonts and clean, neutral body fonts; bold type must be balanced with whitespace to maintain legibility.
- [[2025-11-14_good-visual-design]] — what this article contributes to this concept
