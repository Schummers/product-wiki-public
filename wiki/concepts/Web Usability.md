---
type: concept
name: Web Usability
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Link Design"
  - "Web Design"
---

# Web Usability

## Definition

Web usability is the body of evidence-based guidance on making websites work for
the people using them: how pages are laid out, how links and labels announce
where they lead, how content is written and formatted, how fast the site
responds, and how much of all this matches what users already expect from every
other site they use. The corpus treats it as a compiled research discipline
rather than a set of opinions — decades of findings on scanning versus reading,
viewing patterns from eyetracking, navigation mental models, form completion and
search behaviour, turned into design guidelines
([[2025-12-18_web-ux-study-guide]]).

Its defining property in these sources is stability. Design patterns and trends
change, human behaviour does not: the four credibility factors identified in
1999 still hold ([[2016-05-08_trustworthy-design]]), most of the 113 homepage
guidelines written in 2001 remain valid ([[2024-03-15_homepage-design-principles]]),
and a 25-year review of UX predictions found that the ones that survived were
precisely the conservative ones, grounded in users resisting change and
preferring simplicity ([[2020-05-24_25-years-ux-wins-fails]]). The practical
corollary runs through nearly every source: users spend most of their time on
other websites, so a site that behaves like the others is easier to use than one
that innovates on layout ([[2017-10-22_horizontal-attention-leans-left]],
[[2024-03-15_homepage-design-principles]]).

## Practice

### Convention is the default, deviation is a cost

- Users learn where things go from years of exposure elsewhere, and the further
  a design strays from that norm, the worse the experience
  ([[2016-07-10_centered-logos]], [[2017-10-22_horizontal-attention-leans-left]]).
- The measured case: centred logos, popularised by mobile-first design, made
  users six times more likely to fail to reach the homepage in a single click
  than left-aligned ones. Curiously, centred placement did not significantly hurt
  aided brand recall — the damage was navigational, not mnemonic
  ([[2016-07-10_centered-logos]]). A separate quiz item makes the same point
  about recall: logo *presence* matters more than logo *position*
  ([[2017-01-01_ux-quiz-16]]).
- The lesson generalises: mobile-first patterns should not be ported to desktop
  uncritically ([[2016-07-10_centered-logos]]), and mobile-first is not dogma —
  users do important or complex tasks on larger screens, and dispersing content
  across many pages for mobile's sake hurts desktop
  ([[2025-12-18_web-ux-study-guide]]).
- Homepages in particular should use standard, predictable designs rather than
  creative layouts, because people prefer a site that works like the ones they
  already know ([[2024-03-15_homepage-design-principles]]).
- Standardisation is also what makes patterns discoverable and trustworthy in
  the first place ([[2025-12-18_web-ux-study-guide]]).

### Layout and where attention goes

- Attention leans left: 80% of fixations fall on the left half of the page even
  on wide screens, and 94% on search-results pages. Put critical content top and
  left, secondary content in the right rail, and raise visual prominence if
  something important must live on the right
  ([[2017-10-22_horizontal-attention-leans-left]]).
- The fold still matters, though less than in 2010: 57% of viewing time above
  the fold, 74% within two screenfuls, 81% within three, and users rarely go
  further. High-priority content and primary calls to action go above the fold;
  counter false floors created by minimalism and excess white space with
  scrolling signifiers such as cut-off text; test page length with real users
  ([[2018-04-15_scrolling-and-attention]]). The study guide restates the same:
  do not hide critical information below the fold or behind secondary content
  ([[2025-12-18_web-ux-study-guide]]).
- The illusion of completeness is the underlying failure mode — content looks
  complete within the viewport while more exists outside it
  ([[2017-01-01_ux-quiz-16]]).
- Grids give the structure users scan against. Column grids for general layouts,
  modular grids for e-commerce and listing pages, hierarchical grids where
  importance must be ranked; all built from columns, gutters and margins.
  Columns in percentages (often 12 on desktop, fewer on smaller devices),
  gutters at fixed values that change per breakpoint, and an 8px system since
  most screen sizes are multiples of 8. Breaking the grid deliberately can
  highlight an item; breaking it inconsistently produces chaos and destroys
  scannability ([[2022-07-17_using-grids-in-interface-designs]]).
- Image–text layouts: informational value matters more than alignment. Where
  images carry information, zigzag and aligned layouts perform alike; where they
  are decorative, zigzag causes stumbling and redirects. Align decorative
  images, put informational content on the left, top-align text with decorative
  images, avoid complex early images, and give every image a purpose
  ([[2017-11-26_zigzag-page-layout]]).
- Navigation should be visible: hidden hamburger navigation is used less than a
  visible bar, even on mobile ([[2017-01-01_ux-quiz-16]]).

### Links, labels, and information scent

- Information scent is the user's imperfect estimate of how relevant a
  destination will be, built from the link label, the accompanying text or
  image, the surrounding context, and prior knowledge of the source
  ([[2020-02-02_information-scent]]).
- Labels should be succinct but accurate, self-explanatory, in the user's
  language, not vague or jargon-laden. Context (summaries, images, surrounding
  content) augments scent but is often cut off on mobile, so the label itself
  must carry the load ([[2020-02-02_information-scent]]).
- Reviews, recommendations and word of mouth act as social foraging, adding
  scent from other users; a strong brand buys a little tolerance for the
  occasional misstep, but not much
  ([[2020-02-02_information-scent]]).
- Clickbait wins clicks and loses trust: overpromising erodes future
  click-through ([[2020-02-02_information-scent]]).
- The `title` attribute can preview a destination in a tooltip, but only as a
  supplement. Keep titles under 60–80 characters, naming the destination site or
  subsite, the kind of information there, or an access warning. Do not add them
  to every link — where the label and context already make the destination
  obvious, the tooltip is clutter. Browsers render them inconsistently and most
  touchscreen browsers not at all, so nothing essential may depend on them
  ([[2016-06-19_title-attribute]]). The two link sources agree on the hierarchy:
  the title attribute never substitutes for good scent in the link text itself
  ([[2016-06-19_title-attribute]], [[2020-02-02_information-scent]]).
- On the homepage, the same rule drives action prompts: descriptive labels with
  high information scent, primary navigation prominently placed with clear
  visual hierarchy ([[2024-03-15_homepage-design-principles]]).

### Content, reading and formatting

- Users read roughly 20% of page text and scan selectively by task, so
  front-load: keywords at the start of headings, links and bullets
  ([[2025-12-18_web-ux-study-guide]]). How users read on the web is listed among
  the findings that have held for 25 years ([[2020-05-24_25-years-ux-wins-fails]]).
- Format for scanning rather than for the printer: bold important phrases,
  sentence case rather than ALL CAPS, minimum 14pt body text, no long unbroken
  paragraphs, and pages that render properly on mobile
  ([[2020-07-26_privacy-policies-terms-use-pages]]).
- Show, don't categorise: specific examples of what the site offers beat generic
  category labels at getting people to explore
  ([[2024-03-15_homepage-design-principles]]).

### Trust and transparency

- Four credibility factors, unchanged since 1999 and identical across Western
  and Asian cultures: design quality, upfront disclosure, comprehensive and
  current content, and connection to the rest of the web
  ([[2016-05-08_trustworthy-design]]).
- Design quality is read as competence — organised navigation, meaningful
  unambiguous labels, appropriate colour, quality imagery, adequate white space,
  no typos or broken links. Colour schemes signal positioning (corporate,
  budget, luxury), and young adults perceived flat design as more professional
  ([[2016-05-08_trustworthy-design]]).
- Disclose upfront: prominent contact information, base costs, additional fees,
  links to policies. Omission reads as concealment. Avoid login walls and gated
  content that demand personal information before delivering value
  ([[2016-05-08_trustworthy-design]]). Users share personal data only once a
  site has cleared basic relevance and trust thresholds, and outperformed
  competitors ([[2017-01-01_ux-quiz-16]]).
- Link out. Users trust third-party review sites, social media and news outlets
  more than in-house testimonials ([[2016-05-08_trustworthy-design]]).
- Gaps in coverage damage credibility: missing content about a product line or
  customer segment suggests the company does not value it
  ([[2016-05-08_trustworthy-design]]).
- Negativity bias means bad experiences weigh more than good ones, so preventing
  the bad interaction beats compensating for it later
  ([[2017-01-01_ux-quiz-16]]).

### Speed and simplicity

- Response time was the 1997 finding that aged best: fast sites convert better,
  with 1 second the target for great usability and 10 seconds the maximum
  tolerable wait ([[2020-05-24_25-years-ux-wins-fails]]).
- Homepage simplicity means standard predictable design, minimal motion and
  animation, fast loading, no popups unless legally required
  ([[2024-03-15_homepage-design-principles]]).
- Users are conservative and prefer simplicity, which makes staying a few years
  behind the technology curve the usable choice; animation criticism and search
  as a global, always-available, user-controlled interface are on the same list
  of durable findings ([[2020-05-24_25-years-ux-wins-fails]]).
- Every UI pattern buys a benefit with a cost: accordions and carousels hide
  content, modals interrupt, infinite scroll removes pagination cues. Justify
  each by context, not by minimalism or trend. Same for visual trends —
  minimalism, flat design, dark mode, glassmorphism, neobrutalism — judged
  through usability, noting that flat design lacks clickability cues and high
  contrast improves scannability ([[2025-12-18_web-ux-study-guide]]).

### Documents and policy pages

- Avoid PDFs for on-screen reading. Twenty years of testing show they degrade
  the experience: optimised for paper rather than viewports, lacking scanning
  and scrolling affordances, splitting content across sheets, slow to download,
  and hard to search through. Organisations keep using them believing they are
  quicker to publish, when version control and updates are in fact faster in
  HTML, where links survive automatically
  ([[2020-06-28_avoid-pdf-for-on-screen-reading]]).
- The preferred pattern is an accessible HTML gateway page summarising the core
  message with enough detail to read online, plus an optional PDF download. If a
  PDF is unavoidable: verify users actually need to print it, make it accessible
  (searchable text, labelled form fields, adequate contrast), minimise file
  size, label the download with size and page count, and remove old versions.
  Offer HTML, e-reader and audio alternatives
  ([[2020-06-28_avoid-pdf-for-on-screen-reading]]).
- Policy pages (privacy, terms, EULAs) fail on five recurring counts:
  unreadable legalese, no high-level summary, poor formatting, no functional
  navigation, and placement where users do not look. Fixes: plain-language
  translations of legal sections with concrete examples of impact; an overview
  at the top stating scope, audience, key points, update and effective dates,
  and a summary of what recently changed; web-readable formatting; a clickable
  table of contents or left-rail navigation, which makes the policy feel
  transparent even unread; and links in the footer of every page plus in
  Settings and next to the relevant feature, redundancy being welcome here
  ([[2020-07-26_privacy-policies-terms-use-pages]]).
- Well-designed policies reassure; badly designed ones suggest the company cares
  more about liability than about customers
  ([[2020-07-26_privacy-policies-terms-use-pages]]).

### Forms as a usability surface

Forms compliant with basic usability guidelines produce 78% one-try submissions
with no errors, against 42% for those violating them, and every field cut raises
conversion. Keep forms short, group related fields, use a single column, follow
logical sequences, avoid placeholder text, mark optional versus required, state
formatting requirements upfront, drop Reset and Clear buttons, and make error
messages visible and specific ([[2016-05-01_web-form-design]]). Form design is
one of the thirteen topic areas the web-UX corpus is organised around
([[2025-12-18_web-ux-study-guide]]).

### Designing for teenagers

- Fifteen years of testing with 100 teenagers aged 13–17, across 210 websites
  and 30 apps, yielding 130 guidelines — and refuting the stereotype of the
  tech-wizard teen who wants multimedia
  ([[2019-03-17_usability-of-websites-for-teenagers]]).
- Teens are goal-oriented like adults, but less patient and quicker to give up,
  and they blame the site rather than themselves
  ([[2019-03-17_usability-of-websites-for-teenagers]]).
- Practical consequences: avoid dense text (they read enough at school) and use
  white space and bullet points; present content professionally, since they
  dislike clutter and pointless multimedia; load fast, because slow sites are a
  deal-breaker and heavy widgets fail on older devices; avoid a condescending
  tone, the word "kids", childish animation and garish colours; and design for
  mobile as the primary device, avoiding complex mouse gestures, small buttons
  and rollovers ([[2019-03-17_usability-of-websites-for-teenagers]]).

### What has stayed true

Response time, how people read on the web, search as primary navigation, banner
blindness and format blindness, mobile device design, animation criticism and
PDF usability problems all survived 25 years of review; the predictions that
failed were the optimistic ones about systemic and business-model change. Small-N
qualitative testing with 5 users also held up
([[2020-05-24_25-years-ux-wins-fails]]). The same durability argument appears in
the trust research ([[2016-05-08_trustworthy-design]]) and the homepage
principles ([[2024-03-15_homepage-design-principles]]): the guidelines last
because they rest on human behaviour, not on technology.

## Sources (16)

- [[2016-05-01_web-form-design]] — Form usability is a core web usability concern affecting task completion, errors, and user satisfaction.
- [[2016-05-08_trustworthy-design]] — Design decisions (organization, color, typography, imagery, white space) directly influence perceived trustworthiness of the organization.
- [[2016-06-19_title-attribute]] — The title attribute is one tool for communicating link destinations, but should only be used when the link text itself is insufficient.
- [[2016-07-10_centered-logos]] — Usability suffers when websites fail to meet user expectations; the degree of deviation from expected design patterns correlates with experience degradation.
- [[2017-01-01_ux-quiz-16]] — covers topics directly related to usable web design including trust, brand recall, and navigation.
- [[2017-10-22_horizontal-attention-leans-left]] — establishes conventions for navigation placement and content layout based on where users naturally look.
- [[2017-11-26_zigzag-page-layout]] — establishes best practices for image-text layouts based on content value and user efficiency.
- [[2018-04-15_scrolling-and-attention]] — designing page layout and content hierarchy to align with natural user scanning patterns and attention allocation.
- [[2019-03-17_usability-of-websites-for-teenagers]] — Best practices for mainstream websites serving teen audiences including professional presentation, fast loading, clear navigation, and age-appropriate social features.
- [[2020-02-02_information-scent]] — Details what makes links and labels effective, emphasizing clarity over cleverness and the importance of matching link promises to actual content.
- [[2020-05-24_25-years-ux-wins-fails]] — documents principles that have remained true for 25 years including response time, search design, readability, and banner blindness.
- [[2020-06-28_avoid-pdf-for-on-screen-reading]] — specific problems PDFs cause for online reading and research evidence accumulated over 20 years of testing.
- [[2020-07-26_privacy-policies-terms-use-pages]] — how policy pages violate web usability principles and best practices for readability and scannability.
- [[2022-07-17_using-grids-in-interface-designs]] — Grid systems enable designers to create scannable, accessible interfaces and empower developers to implement responsive designs that work across breakpoints.
- [[2024-03-15_homepage-design-principles]] — emphasizes how standard, predictable design patterns aligned with user expectations improve homepage usability and effectiveness.
- [[2025-12-18_web-ux-study-guide]] — what this article contributes to this concept
