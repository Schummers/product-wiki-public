---
type: concept
name: Navigation Design
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Mobile Navigation"
  - "Navigation"
  - "Navigation Patterns"
  - "Wayfinding"
---

# Navigation Design

## Definition

Navigation design is the visible interface layer that lets people move through
and access the information a product holds. It is distinct from information
architecture: IA is the underlying organizational structure, navigation is the
set of controls and cues that expose it [[2022-04-10_ia-study-guide]]. Its job
is threefold — orientation (showing users where they currently are), wayfinding
(showing what lies adjacent and how to get there), and access to deep content at
low interaction cost [[2021-07-04_local-navigation]]. A navigation system
therefore combines menus, links, labels, and location indicators
[[2024-06-07_menu-design]], and it fails not when it has too many levels but
when users cannot predict where a path leads.

The sources converge on one explanatory mechanism: users behave as information
foragers, choosing what to click by estimating the ratio of expected information
value to the cost of getting it, using imperfect heuristics rather than optimal
calculation [[2019-11-10_information-foraging]]. The cue driving that estimate is
information scent — what the link label, surrounding text, images, and prior
knowledge of the source promise about the destination
[[2020-02-02_information-scent]]. This reframes what "good navigation" means:
minimizing clicks is not the objective. The 3-click rule has no empirical
support, and click counts are a poor usability metric because clicks differ in
cost and in how much progress they buy; clear labels, visible hierarchy, and
wayfinding indicators matter more [[2019-08-11_3-click-rule]]. Repeated
hub-and-spoke returns (pogosticking) signal that users cannot find content
[[2016-01-10_ux-quiz-15]], and the quality of each click — does the user get
closer to the goal — matters far more than the quantity
[[2016-10-30_top-10-enduring]].

## Practice

### Information scent and link labels

- Link labels should be specific (say what the user will find), sincere
  (expectations met immediately on arrival), substantial (meaningful standing
  alone, since users scan and often read only the links), and succinct without
  sacrificing the other three [[2019-03-24_better-link-labels]].
- Frontload information-carrying words: users scan the first few words of a link
  [[2019-03-24_better-link-labels]], and the same rule applies to group labels
  inside mega menus [[2017-03-26_mega-menus-work-well]].
- Avoid jargon, internal terminology, and creative labels
  [[2024-06-07_menu-design]]; obscure or vague labels produce poor scent and
  valuable content gets missed [[2020-02-02_information-scent]].
- Context (summary text, images, surrounding content) augments scent, but it is
  frequently cut off on mobile, which makes the label itself carry more weight
  [[2020-02-02_information-scent]].
- Prior knowledge and social signals (reviews, recommendations, word of mouth)
  also feed scent; clickbait raises short-term clicks but erodes trust and
  future click-through [[2020-02-02_information-scent]].
- Well-formatted pages (scannable structure, bolded keywords, descriptive
  headlines) reduce the need for users to compensate with learned enrichment
  behaviours [[2019-11-10_information-foraging]].
- The HTML `title` attribute can preview a destination before the click, but
  keep titles under 60–80 characters, use them only where label and context are
  not already obvious, and never let basic comprehension depend on them —
  browsers render them inconsistently and most touchscreen browsers not at all
  [[2016-06-19_title-attribute]].

### Visible versus hidden navigation

- Hidden navigation measurably degrades performance. On desktop, users employed
  hidden navigation in 27% of cases against 48% for visible and 50% for combo;
  on mobile, 57% against 86% for combo. Content discoverability dropped 20%,
  perceived task difficulty rose 21% versus visible navigation, and desktop task
  times were at least 39% longer [[2016-06-26_hamburger-menus]].
- Recognizability is not usability: 83% of participants associate the hamburger
  icon with main navigation, and top-left placement is the dominant factor
  enabling that recognition — yet hidden navigation still raises interaction
  cost and task time relative to visible navigation
  [[2025-06-13_hamburger-menu-icon-recognizability]]. Embellishments (borders,
  arrowheads) introduce some doubt, and any three-line icon in the top-left is
  often read as a hamburger even when it means list view or filters.
- Do not hide navigation behind a hamburger on desktop
  [[2024-06-07_menu-design]], [[2021-05-16_vertical-nav]].
- Note a tension across the corpus: the mobile study guide reports that mobile
  navigation patterns, hamburger menus included, have standardized and are
  widely understood [[2023-01-12_mobile-ux-study-guide]], while the empirical
  hamburger studies show the pattern still costs discoverability and time even
  where it is recognized [[2016-06-26_hamburger-menus]],
  [[2025-06-13_hamburger-menu-icon-recognizability]].

### Menu patterns

- **Mega menus** beat regular dropdowns: they show all options at a glance
  rather than taxing short-term memory, support visual grouping, and accommodate
  images and richer typography [[2017-03-26_mega-menus-work-well]]. They also
  outperform cascading hierarchical dropdowns by displaying multiple hierarchy
  levels at once, allowing error correction and requiring less pointer
  precision, even when the click count is equal or higher
  [[2019-08-11_3-click-rule]].
- Mega-menu timing: require the pointer to rest 0.5s before opening (avoiding
  flicker on pass-through), display within 0.1s, and keep the menu up until the
  pointer has exited for 0.5s; handle the diagonal problem by detecting the
  trajectory toward a target item rather than closing the instant the pointer
  leaves the active area [[2017-03-26_mega-menus-work-well]].
- Chunk mega-menu options at medium granularity, order groups by workflow or
  importance, never duplicate options, and keep the menu free of complex widgets,
  text fields, or search boxes [[2017-03-26_mega-menus-work-well]].
- Avoid multi-level cascading dropdowns entirely; use mega menus or landing
  pages instead [[2024-06-07_menu-design]].
- **Vertical navigation** scales to broad architectures without forcing generic
  top-level groupings, scans efficiently (users look at the left side 80% of the
  time, and vertical lists yield more information per fixation), and ports to
  mobile with fewer design changes than horizontal navigation. Its cost is a
  lower content-to-chrome ratio [[2021-05-16_vertical-nav]].
- **Tabs** work best with few options and related content within each tab; never
  mix in-page tabs (which keep users in place, similar content) with navigation
  tabs (which navigate, dissimilar content). Use at least two selection
  indicators, and give tab labels information scent since unselected tabs hide
  their content. On desktop, prefer tabs for lengthy content; accordions work
  better on mobile and for short content like FAQs [[2024-08-02_tabs-used-right]].
- **Contextual menus** should hold only task-relevant actions, expose every one
  of those commands somewhere in the main navigation as well, carry a visible
  affordance (ellipsis or caret) since gestures and right-click are not
  universally known, list commands by frequency of use, stay under roughly ten
  to twelve items, and disable rather than hide irrelevant options
  [[2019-03-17_contextual-menus]].
- **Navigation hubs** — landing pages with grouped links, descriptions, and
  images — help at key decision points by explaining terminology and giving
  users a stopping point [[2019-08-11_3-click-rule]]. The navigation-hub
  architecture (all options on the homepage, every page linking back) suits
  task-based sites where users rarely explore multiple branches in one session
  [[2016-01-10_ux-quiz-15]].
- Avoid gimmicky or novel menu designs that impress stakeholders and confuse
  users; familiar patterns are almost always better [[2024-06-07_menu-design]].
- Make links large enough to hit — roughly 1cm x 1cm [[2024-06-07_menu-design]].

### Global, local, and secondary navigation

- Global navigation shows the top tier and stays constant; local navigation
  shows the current branch and varies by location. Together they expose the full
  hierarchy [[2021-07-04_local-navigation]].
- Local navigation pays off on deep sites with many pages per category and for
  exploratory browsing (comparing options within a section); it is wasted on
  small sites, and very deep hierarchies exceed what the UI can hold. Horizontal
  local navigation below the global bar is compact but supports only 2–3 tiers;
  a left-side vertical version supports more depth at a space cost; breadcrumbs
  are more compact for deep pages [[2021-07-04_local-navigation]].
- Keep local navigation visible but less salient than global navigation — if it
  looks more prominent, users mistake it for the main menu
  [[2021-07-04_local-navigation]].
- **Universal navigation** (the link back from a subsite to the parent site)
  must appear on every subsite page, like an exit sign; without it users get
  stranded [[2016-09-11_universal-navigation]], a failure the enduring-problems
  list also flags as trapping users on microsites
  [[2016-10-30_top-10-enduring]]. Keep it subordinate to the subsite's own
  navigation, place the universal home link top-left near the logo, collapse the
  universal category list when users rarely switch subsites, and on mobile push
  it to the bottom of the menu [[2016-09-11_universal-navigation]].
- **Footers** are deliberately used, either as a second chance to convince or as
  a last resort for hard-to-find content, and as a way to navigate without
  scrolling back up. Always include utility links (contact, customer service,
  privacy, terms); use doormat navigation (repeating global navigation) on long
  pages; limit to first- and second-level categories rather than a full sitemap;
  use conventional link names ("Contact Us", not "Resources"); and keep footers
  legible and unhidden [[2019-02-24_footers]]. Note that the footer is not a
  typical you-are-here indicator, unlike the logo, breadcrumbs, and window title
  [[2016-01-10_ux-quiz-15]].

### Orientation and wayfinding

- Indicate the current location explicitly — breadcrumbs and highlighted current
  pages both serve this [[2024-06-07_menu-design]].
- **Breadcrumbs** supplement global and local navigation rather than replacing
  them, and are especially valuable for users arriving from external links. They
  should reflect the site's hierarchy, not session history; the last item is the
  current page and should not be a link, but should be visually differentiated.
  They add little on flat or 1–2 level sites and on linear experiences, and on
  mobile they wrap or become untappable — truncate to the last level(s) or drop
  them [[2018-12-23_breadcrumbs]].
- Include Home as the first breadcrumb level rather than duplicating a home link
  elsewhere [[2017-07-23_homepage-links]].
- **Spatial memory** is built relative to boundaries and landmarks, not absolute
  positions, and is fuzzy — users recall neighbourhoods of items, and only the
  most frequently used items become precise. Support it with stable layouts
  (avoid adaptive interfaces that rearrange elements; scale rather than reflow),
  broad shallow hierarchies, visual labels and thumbnails, overviews such as
  minimaps, and deliberately created landmarks [[2020-10-11_spatial-memory]].
- Put navigation where users already look: headers on desktop, left side in
  applications, utility navigation at the top, footer navigation at the bottom
  [[2024-06-07_menu-design]]; users expect it in the top-left or top-right
  corners on desktop [[2022-04-10_ia-study-guide]].
- **Logo and Home link**: left-aligned logos act as reliable navigation anchors.
  Users were six times more likely to fail to reach the homepage in a single
  click with a centered logo than a left-aligned one
  [[2016-07-10_centered-logos]], [[2017-07-23_homepage-links]]. Provide both the
  implicit path (clickable logo) and the explicit one (a "Home" label), style
  the logo so it does not blend into navigation text, and do not render Home as
  an active link while on the homepage [[2017-07-23_homepage-links]]. The
  centered-logo trend comes from mobile-first layouts where the top-left holds
  the menu icon, and should not be ported uncritically to desktop
  [[2016-07-10_centered-logos]].

### Back navigation, windows, and overlays

- Always let users go back: never disable the browser Back button or trap users
  on the site. Back should move exactly one step, overlays should not cause Back
  to exit the site entirely, and exits (close, cancel) belong where users expect
  them — top right for overlays — with text labels or universal icons. Support
  undo at multiple levels and do not leave it keyboard-only
  [[2020-11-29_user-control-and-freedom]].
- Default to opening links in the same tab or window. New tabs are appreciated
  for comparing content, combining information from several sources, page
  parking, and using an original tab as a launch point; they are resented for
  quick inspection followed by a return, for multistep workflows where users
  would rather press Back, and when many tabs are already open. Decide on task
  type and context, not on link type or file format, and signal the new window
  before the click. For PDFs, prefer an HTML gateway page; if opening in the
  browser, use a new tab on desktop and the same tab on mobile so Back keeps
  working [[2020-09-27_new-browser-windows-and-tabs]].
- Overlay dismissal is a navigation problem: users guess among close buttons,
  outside taps, swipes, and the back button; stacked overlays make them lose
  track of layers and close the whole stack; full-page overlays look like pages
  and invite the back button; nested close buttons get confused; and accidental
  dismissal costs real work. Prefer separate pages or accordions unless keeping
  background context visible is genuinely necessary
  [[2022-09-18_accidental-overlay-dismissal]].

### Long pages: in-page links, sticky headers, back-to-top

- In-page links violate the mental model that a link leads to another page, which
  is the core usability concern [[2017-05-07_in-page-links]]. Later testing found
  most participants familiar with the pattern regardless of age (only 2 of 11
  showed no engagement), so the concern has softened, but clear styling and
  labeling remain necessary [[2023-10-01_in-page-links-content-navigation]].
- Use them only for long, genuinely sectioned content — first ask whether the
  content could be shortened, reorganized, or split across pages
  [[2017-05-07_in-page-links]]; content must chunk naturally, and on short pages
  a table of contents only adds length [[2023-10-01_in-page-links-content-navigation]].
- Label them explicitly ("On this page", "In this article", "Table of Contents")
  so users can tell them apart from cross-page links — critical for screen-reader
  and screen-magnifier users [[2017-05-07_in-page-links]],
  [[2023-10-01_in-page-links-content-navigation]] — and style them as links
  (color, underline), since links without visual signifiers get overlooked
  [[2023-10-01_in-page-links-content-navigation]].
- Match link text to the target heading, scroll the target near the top with a
  little whitespace above so the heading is not hidden by sticky elements,
  consider a sticky sidebar table of contents on larger screens, and mark the
  current section when the in-page navigation stays visible
  [[2017-05-07_in-page-links]]. In-page links gain value as screens shrink and
  content stretches vertically [[2017-05-07_in-page-links]]; users value them for
  skipping irrelevant sections [[2023-10-01_in-page-links-content-navigation]].
- Sticky headers: keep them as short as possible while preserving readable text
  and tap targets, ensure strong contrast (avoid translucency), limit animation
  and avoid the "stalker menu", consider partially persistent headers that hide
  on scroll-down and return on scroll-up with 300–400ms animation, and run a
  cost-benefit check on whether the header's contents are needed often enough to
  occupy space on every page [[2021-04-04_sticky-headers]].
- Back-to-top buttons: only for pages longer than about four screens, placed
  lower right, labeled "Back to Top" rather than an unlabeled arrow, one sticky
  button rather than repeated links, appearing only after the user has scrolled
  down and shown scroll-up intent. Often sticky navigation, bottom-of-page
  navigation, or search addresses the underlying need better
  [[2017-08-27_back-to-top]].

### Structure, filters, and redundancy

- **Polyhierarchy** — placing an item under several parent categories —
  accommodates the fact that users categorize differently, and is practical
  digitally where physical constraints do not apply. Exercise restraint: two or
  three natural parents based on research, not every plausible location, or menus
  bloat and cognitive load rises. It also conflicts with breadcrumbs, since only
  one canonical path can be shown [[2018-05-13_polyhierarchy]].
- **Duplicate links** raise cognitive load (users must decide whether two links
  are the same), compete for a zero-sum pool of attention, and cause wasted
  repeat visits. Traffic gains on a duplicated destination are misleading, since
  clicks may simply have been drained from elsewhere. Give an important link more
  prominence rather than repeating it; if duplication is justified, place the
  copies far enough apart that they are never visible together
  [[2016-03-13_duplicate-links]]. Mega menus should likewise never duplicate
  options [[2017-03-26_mega-menus-work-well]], and vertical navigation should not
  be mirrored horizontally [[2021-05-16_vertical-nav]]. The enduring-problems
  list also counts repetitive links — forcing users to select the same
  information repeatedly — among the recurring failures
  [[2016-10-30_top-10-enduring]].
- **Filters** are a navigation tool for large option sets: tailor them to the
  content type rather than reusing one generic set, use concrete predictable
  category labels ("Product Categories", "Genres") over vague ones ("Item Type",
  "Format"), strip internal jargon and codes from values, order general filters
  above specific ones unless a specific attribute dominates choice in the domain,
  and ground both labels and priorities in interviews, surveys, search logs, and
  analytics [[2018-07-15_filter-categories-values]]. Offer both include and
  exclude options and tailor facets to content types
  [[2016-10-30_top-10-enduring]].
- Recurring structural failures worth auditing: content in unexpected locations,
  competing category or link names that force guessing, islands of related
  content with no links between them, poor search results, and links styled to
  look like ads and therefore ignored [[2016-10-30_top-10-enduring]].
- Search does not remove the need for a good navigation structure
  [[2022-04-10_ia-study-guide]].
- Perceived interaction cost includes latency: three clicks with slow loads is
  worse than five fast ones [[2019-08-11_3-click-rule]].

### Mobile and touch

- Do not port a mobile design unchanged to desktop. Hamburger menus, navigation
  repeated at the bottom, sticky navigation, search icons, and top-right
  navigation placement are common on mobile and hurt desktop usability; observed
  low desktop navigation use reflected poor desktop implementations, not lower
  need [[2016-07-24_mobile-first-not-mobile-only]].
- Mobile subnavigation should minimize interaction cost (few taps, no page
  loads), support typical paths, and keep the navigation UI itself discoverable.
  Sequential menus are space-efficient but disorient users with low spatial
  ability, who often hit the phone's Back button instead of the menu's Back link.
  Accordions inside the main menu suit primary categories with fewer than six
  subcategories. Section menus on category landing pages suit sessions spent
  inside one section but not jumping between sections. Category landing pages
  cost a page load per branch switch — reserve them for more than 15
  subcategories when nothing else fits [[2017-07-16_mobile-subnavigation]].
- Split buttons (label navigates, arrow expands) do not transfer from desktop
  applications to touch: users have no mental model for the dual behaviour, the
  fat-finger problem makes two adjacent targets unreliable, and the ambiguity
  makes the interface feel buggy. A better solution expands the menu on tap and
  puts a link to the category landing page inside it ("All Sports", "View All");
  tap-to-expand-then-tap-again has weak discoverability
  [[2017-06-25_split-buttons-navigation]].
- Mobile requires different navigation patterns than desktop, including
  alternative placement for language and country switchers
  [[2022-04-10_ia-study-guide]], and navigation (hamburger, bottom navigation,
  subnavigation) is core to mobile design [[2023-01-12_mobile-ux-study-guide]].

### Accessibility

- Mega menus create specific problems: screen-magnifier users may see only part
  of the menu and tiny options cause selection errors on touch. Implement a
  simple fallback (clickable top-level items leading to full category pages)
  alongside advanced screen-reader support
  [[2017-03-26_mega-menus-work-well]].
- Contextual menus are invisible to users who do not know the gesture, so
  duplicate their commands in the main navigation and add a visible trigger
  [[2019-03-17_contextual-menus]].
- Keep visible text labels in navigation rather than icon-only designs
  [[2021-05-16_vertical-nav]], and label in-page links so assistive-technology
  users can distinguish them [[2017-05-07_in-page-links]].
- Mobile design must account for accessibility needs including screen readers and
  motor impairments [[2023-01-12_mobile-ux-study-guide]].

### Research and evaluation

- Card sorting surfaces users' mental models of how content should be grouped;
  tree testing checks whether they can find things in a proposed structure
  without visual design in the way [[2022-04-10_ia-study-guide]]. Both should
  ground polyhierarchy decisions rather than adding paths speculatively
  [[2018-05-13_polyhierarchy]], and both reveal competing category names and
  structures that do not match mental models [[2016-10-30_top-10-enduring]].
- Read tree tests on three metrics together: success rate (findability),
  directness (effort and struggle), and time (mental load). Median success is
  62%, good is 61–80%, and mission-critical tasks should clear 90% — but task
  importance matters more than the absolute number. First-click data is
  predictive: once users reach the right top-level category, context cues usually
  carry them home, while a wrong first click is often disastrous. High success
  with low directness means users struggled through, pointing at label or
  structure problems. Comparing two trees needs 50+ participants per tree and
  explicit significance testing, ANOVA for three or more
  [[2024-01-19_interpreting-tree-test-results]].
- Many of these navigation failures are cheap to detect: basic usability testing
  identifies competing categories, repetitive links, and disappearing navigation
  [[2016-10-30_top-10-enduring]].
- Research user vocabulary and priorities directly through interviews, surveys,
  search logs, and analytics [[2018-07-15_filter-categories-values]]; review
  search logs regularly [[2016-10-30_top-10-enduring]].

## Sources (37)

- [[2016-01-10_ux-quiz-15]] — covers specific navigation architectures like the navigation-hub pattern (suitable for task-focused sites with limited branch exploration) and user navigation behaviors like pogosticking (repeating hub-and-spoke navigation, indicating difficulty finding content).
- [[2016-03-13_duplicate-links]] — redundant links are a navigation pattern that affects usability.
- [[2016-06-19_title-attribute]] — Title attributes support navigation by helping users understand where links lead and reducing disorientation.
- [[2016-06-26_hamburger-menus]] — Hidden navigation patterns like hamburger menus significantly impair navigation performance; visible navigation is substantially more discoverable and leads to better task completion.
- [[2016-07-10_centered-logos]] — Logo placement affects navigation success; left-aligned logos function as reliable navigation anchors that users expect.
- [[2016-07-24_mobile-first-not-mobile-only]] — Navigation patterns successful on mobile often fail on desktop; different platforms require different navigation strategies.
- [[2016-09-11_universal-navigation]] — Provides principles for designing secondary navigation schemes (universal navigation) that guide users without distracting from primary navigation, with space constraints and context-of-use on mobile requiring different prioritization of navigation elements compared to desktop. Emphasizes users' need to understand where they are, why they are there, and how to return to familiar territory when navigating sites with multiple sections and levels.
- [[2016-10-30_top-10-enduring]] — Competing categories, repetitive links, and disappearing navigation are persistent problems that basic usability testing can identify and fix.
- [[2017-03-26_mega-menus-work-well]] — Mega menus represent an effective navigation pattern for large sites with complex information architectures, supporting visual comparison and reducing cognitive load.
- [[2017-05-07_in-page-links]] — Examines when in-page links are appropriate for navigation, balancing their usefulness for scrolling pages with the mental-model violation they represent.
- [[2017-06-25_split-buttons-navigation]] — adaptation of desktop mega-menu patterns to touchscreens, addressing hover unavailability and interaction model mismatch.
- [[2017-07-16_mobile-subnavigation]] — patterns for displaying hierarchical navigation on small screens, with decision criteria based on number of subcategories.
- [[2017-07-23_homepage-links]] — guidance on primary navigation elements including logos and Home links, with conventions and design patterns that users expect.
- [[2017-08-27_back-to-top]] — back-to-top buttons are one navigation solution among many; their appropriateness depends on page length, content structure, and user tasks.
- [[2018-05-13_polyhierarchy]] — balancing findability through multiple pathways against cognitive load and navigation complexity in menu systems.
- [[2018-07-15_filter-categories-values]] — The article addresses how filters serve as navigation tools that help users manage large sets of options through clear criteria and logical organization.
- [[2018-12-23_breadcrumbs]] — Helping users understand where they are within a larger space and how to navigate; breadcrumbs support wayfinding by displaying hierarchical location without requiring navigation controls.
- [[2019-02-24_footers]] — Use of footers as navigation elements through doormat patterns and secondary navigation for reaching pages not prominent in main navigation.
- [[2019-03-17_contextual-menus]] — Strategies for organizing and presenting commands through multiple access paths including main menus and contextual menus.
- [[2019-03-24_better-link-labels]] — Clear link labels are fundamental to helping users understand site structure and move through content.
- [[2019-08-11_3-click-rule]] — Effective navigation requires clear labels, visible hierarchy, wayfinding indicators, and optimized menu patterns rather than click minimization.
- [[2019-11-10_information-foraging]] — applies information foraging theory to explain how users choose between multiple information sources and scanning patterns.
- [[2020-02-02_information-scent]] — Demonstrates how understanding information scent improves navigation systems by making destinations clearly predictable from labels and context.
- [[2020-09-27_new-browser-windows-and-tabs]] — Opening new windows or tabs disrupts navigation patterns, particularly the Back button affordance. Navigation decisions must be based on task type and context, not link type alone.
- [[2020-10-11_spatial-memory]] — organizing interface structure to support users' spatial memory through consistent layouts, clear boundaries, and hierarchical organization.
- [[2020-11-29_user-control-and-freedom]] — designing back links, overlays, and multi-step processes so that back navigation works predictably and meets users' mental models of how navigation should function.
- [[2021-04-04_sticky-headers]] — the article addresses how sticky headers support navigation and discusses considerations for header content and structure.
- [[2021-05-16_vertical-nav]] — Vertical navigation is a pattern choice for organizing navigation UI with distinct advantages for broad hierarchies and scalability.
- [[2021-07-04_local-navigation]] — Global and local navigation must work together, with local navigation design decisions depending on site hierarchy and user browsing behaviors; local navigation enables efficient wayfinding by showing adjacent content users can reach from their current location.
- [[2022-04-10_ia-study-guide]] — visible interface patterns and controls that help users access information organized by IA.
- [[2022-09-18_accidental-overlay-dismissal]] — Navigation patterns including overlay dismissal must be consistent and unambiguous; conflicting patterns for back navigation and overlay dismissal cause errors and lost work.
- [[2023-01-12_mobile-ux-study-guide]] — Mobile navigation patterns have standardized; effective navigation is essential to mobile UX and understanding these patterns is foundational to mobile design.
- [[2023-10-01_in-page-links-content-navigation]] — In-page links are an effective navigation pattern that users have become familiar with, but they require clear styling and labeling to be effective.
- [[2024-01-19_interpreting-tree-test-results]] — first-click and destination data reveal expected navigation paths and category overlaps needing resolution.
- [[2024-06-07_menu-design]] — principles for creating effective navigation systems that help users wayfind and understand information architecture.
- [[2024-08-02_tabs-used-right]] — examines tab patterns as a navigation approach and their relationship to information architecture.
- [[2025-06-13_hamburger-menu-icon-recognizability]] — recurring solutions for helping users move through and access information in digital products.
