---
type: concept
name: UX Writing
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Microcontent"
  - "UI Copy"
  - "Web Writing"
---

# UX Writing

## Definition

UX writing is the craft of choosing and optimising the words inside an
interface so they guide users, a skill the sources present as still requiring
expert human intervention [[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]]. It covers microcontent — small, discrete
elements such as page titles, headlines and taglines, excluding body text —
which play an outsized role in helping users grasp content quickly and decide
whether to engage [[2018-01-07_ux-quiz-2017]]. It also covers UI copy proper:
the labels of commands in buttons and menus, which differ from microcopy or link
text in that they represent actions that change system state
[[2019-03-03_ui-copy]], as well as supporting fragments like tooltips
[[2019-01-27_tooltip-guidelines]] and tab labels
[[2025-01-07_359_In-page_tabs_-_Guide_UX_design]].

Across the corpus, UX writing is inseparable from how people actually consume
text on screens. Users do not read, they scan
[[2019-08-25_text-scanning-patterns-eyetracking]],
[[2025-04-04_genai-write-for-the-web]], so writing decisions — structure,
heading clarity, chunking, emphasis — determine which scanning pattern users
fall into and how much information they extract
[[2019-08-25_text-scanning-patterns-eyetracking]]. The same decisions carry an
ethical weight: because no neutral presentation of options exists, interface
language can support good decision-making or push users toward choices they
later regret [[2019-02-10_interface-copy-decision-making]].

## Practice

### Write for scanning

- Users scan to minimise effort and maximise benefit; the F-pattern (horizontal
  sweep at the top, shorter sweep in the middle, vertical scan down the left
  edge) is the default when nothing on the page attracts the eye toward
  meaningful information [[2017-11-12_f-shaped-pattern-reading-web-content]].
  It is described as bad for users and businesses because content on the right
  or lower in a paragraph is simply skipped
  [[2017-11-12_f-shaped-pattern-reading-web-content]].
- Four patterns are ranked by effectiveness: F-pattern (least effective, on
  unstructured prose), spotted, layer-cake, and commitment (reading nearly
  everything, which requires high motivation, trust, or consequences for missing
  information) [[2019-08-25_text-scanning-patterns-eyetracking]]. Layer-cake is
  described as by far the most effective way to scan, nearly as good as reading
  everything [[2019-08-04_layer-cake-pattern-scanning]],
  [[2019-08-25_text-scanning-patterns-eyetracking]].
- Antidotes to F-pattern scanning: put important points in the first two
  paragraphs, use headings and subheadings, bold key words, group related
  content visually, use bullets and numbered lists, start headings with
  information-bearing words, and cut unnecessary content
  [[2017-11-12_f-shaped-pattern-reading-web-content]].
- Lead with the need-to-know information (inverted pyramid) instead of burying
  the summary in the conclusion [[2025-04-04_genai-write-for-the-web]].

### Subheadings and chunking

- Content rule for subheadings: describe all and only the topics of their
  section, stay concise, lead with the important words, and use clear language
  so users can skip what is irrelevant [[2019-08-04_layer-cake-pattern-scanning]].
- Visual rule: subheadings must stand out consistently through size, colour,
  typeface, or bolding — but not so much that they read as ads or promotions
  rather than content [[2019-08-04_layer-cake-pattern-scanning]].
- On pages with cards or irregular layouts, extend the same principles: group
  related content, visually distinguish the chunks, use spacing to signal
  relationships, and label each chunk with a clear subheading
  [[2019-08-04_layer-cake-pattern-scanning]].
- Bolding, bullet points, differently coloured text and meaningful headings are
  what move users from F-pattern toward the spotted and layer-cake patterns
  [[2019-08-25_text-scanning-patterns-eyetracking]].

### Labels, commands and short fragments

- Command labels: one to four words maximum, dropping articles like "a" and
  "the" to improve scannability, while keeping enough text to describe the
  command accurately [[2019-03-03_ui-copy]].
- Describe the consequent state, not the current one, so users understand where
  the system will go [[2019-03-03_ui-copy]].
- Lead action commands with a verb or verb phrase ("Print", "Accept and Sign
  In"); use adjectives ("Bold", "Italic") when the command changes an element's
  appearance [[2019-03-03_ui-copy]].
- Avoid vague, cute, trendy or branded terms in command text; branded vocabulary
  confuses users unfamiliar with the application's conventions
  [[2019-03-03_ui-copy]].
- Tab labels should be very short, ideally two words, simple, descriptive, and
  not set in all caps, so the interface stays scannable
  [[2025-01-07_359_In-page_tabs_-_Guide_UX_design]]. In-page tabs are the wrong
  component when labels cannot be kept concise
  [[2025-01-07_359_In-page_tabs_-_Guide_UX_design]].
- Tooltips should carry brief, self-sufficient microcontent that adds value;
  avoid redundant or obvious text, and never hide instructions or directly
  actionable information in them — that content belongs on screen
  [[2019-01-27_tooltip-guidelines]]. Because most icons are ambiguous, unlabelled
  icons should at minimum get a descriptive tooltip
  [[2019-01-27_tooltip-guidelines]].

### Plain language for dense and legal content

- Policy pages fail when written in vague, complex legalese that makes users
  feel the text is "for lawyers"; provide plain-language translations of legal
  sections and specific examples of how the policy affects the user rather than
  broad statements [[2020-07-26_privacy-policies-terms-use-pages]].
- Open with a high-level plain-language summary covering what the policy is
  about, who it is for, and its key points, plus update and effective dates and
  a summary of what recently changed
  [[2020-07-26_privacy-policies-terms-use-pages]].
- Format for the web: minimum 14pt text, bold important phrases, sentence case
  rather than ALL CAPS, no long unbroken paragraphs, and a clickable table of
  contents or left-rail navigation. Poor formatting reads as carelessness or as
  the company hiding something [[2020-07-26_privacy-policies-terms-use-pages]].
- Do not deliver web content as PDF: PDFs are converted from print-focused
  documents, rarely follow web-writing or accessibility guidelines, and lack the
  chunking, bullets, subheadlines and accordions that make content skimmable
  [[2020-08-09_pdf-unfit-for-human-consumption]].

### Framing and ethics

- How options are worded, laid out and visually designed significantly
  influences which one users pick; a neutral presentation of options does not
  exist [[2019-02-10_interface-copy-decision-making]].
- Named manipulative techniques to avoid: scare tactics exploiting loss
  aversion, artificial scarcity and time pressure, emotionally charged framing
  of mundane transactions, and describing choices differently from what is
  actually selectable [[2019-02-10_interface-copy-decision-making]].
- Describe choices truthfully; manipulative copy can produce short-term
  conversions but damages long-term loyalty and reputation
  [[2019-02-10_interface-copy-decision-making]].

### Working with AI on interface copy

- Two concrete methods: give the AI your interface context plus a specific
  wording and ask it to explain what that wording means — a coherent answer
  suggests the wording is clear; and, when stuck, ask for 10 to 30 suggestions
  with maximum context, then keep the best, remix and rework them manually
  rather than taking the first output [[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]].
- The value of the model here is that it acts as a detached, impartial external
  tester, useful for checking that internal jargon has not deformed the chosen
  terms [[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]].
- Its limit: asking an AI to predict which of two wordings will perform better
  is illusory, since effectiveness depends on company and user context that only
  real testing reveals [[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]]. Because AI now easily produces average copy,
  the expected level rises and the UX writer's expertise becomes more important,
  not less [[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]].
- On the product side, product-specific AI features are reported to violate
  web-writing fundamentals — verbose "fluff", missing formatting and emphasis,
  inconsistent inverted pyramid, and jargon that assumes domain familiarity —
  while broad-scope tools like ChatGPT produce more scannable content
  [[2025-04-04_genai-write-for-the-web]].
- AI outputs should adapt to user context read from prompt signals and follow-up
  questions: simple prompts deserve simple responses, technical prompts detailed
  ones [[2025-04-04_genai-write-for-the-web]].

## Sources (12)

- [[2017-11-12_f-shaped-pattern-reading-web-content]] — addresses content structure, formatting, and prioritization as methods to prevent F-pattern scanning.
- [[2018-01-07_ux-quiz-2017]] — Small, discrete content elements like page titles, headlines, and taglines that guide user understanding; disproportionately important for usability despite their size.
- [[2019-01-27_tooltip-guidelines]] — Discusses how tooltips should contain brief, self-sufficient text fragments that stand alone without requiring additional context.
- [[2019-02-10_interface-copy-decision-making]] — The strategic use of language in interface elements to support ethical decision-making or, when misused, to manipulate user choices against their interests.
- [[2019-03-03_ui-copy]] — Guidelines for writing clear, concise, consistent command labels and short, action-oriented text fragments that support both novices and power users through precision in word choice for efficient user interaction in applications.
- [[2019-08-04_layer-cake-pattern-scanning]] — effective web writing uses descriptive, concise subheadings leading with important words to support scanning; subheadings must be visually distinct and accurately describe their sections' content.
- [[2019-08-25_text-scanning-patterns-eyetracking]] — Content organization, heading clarity, visual styling, and chunking directly influence which scanning pattern users employ and ultimately how much information they extract.
- [[2020-07-26_privacy-policies-terms-use-pages]] — how to write policy content in accessible, user-centered language for web audiences.
- [[2020-08-09_pdf-unfit-for-human-consumption]] — Web content should be structured with web-specific techniques like chunking, bullets, and accessible formatting, not converted from print-focused documents into PDF format.
- [[2025-01-07_359_In-page_tabs_-_Guide_UX_design]]
- [[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]]
- [[2025-04-04_genai-write-for-the-web]] — highlights the need for AI systems to understand user context and adjust writing style and detail level accordingly rather than defaulting to verbose, jargon-heavy responses.
