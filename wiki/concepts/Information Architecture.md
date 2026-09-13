---
type: concept
name: Information Architecture
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Content Organization"
  - "Customer Service Information Architecture"
  - "Findability"
  - "Information Architecture for AI"
  - "Metadata"
  - "Website Information Architecture"
---

# Information Architecture

## Definition

Information architecture is the underlying organizational structure of a content
or information system, as distinct from navigation, which is the visible
interface that exposes that structure to users ([[2022-04-10_ia-study-guide]]).
[[2022-07-03_taxonomy-101]] separates four organization models that are often
conflated: navigation (user-visible), IA structure (the full backstage map),
taxonomies (controlled vocabularies describing concepts for retrieval), and
content models (content types and their relationships). Work in this space is
about how content is grouped, labeled, hierarchically arranged, tagged, and
cross-linked so that people can find and understand it.

The sources treat IA as fundamentally a question of alignment with users' mental
models rather than with internal logic. Content that is organized according to
company thinking rather than user expectations produces the recurring failure of
users not finding what exists ([[2016-10-30_top-10-enduring]]);
[[2024-01-26_mental-models]] states that when users hold an erroneous model of
where things live, the preferred fix is usually to move the content or reorganize
navigation to match, not to argue with the model. IA is also a baseline that
other techniques cannot substitute for: neither customization nor personalization
rescues a weak structure ([[2016-07-10_customization-personalization]]), and
offering search does not remove the need for good navigation
([[2022-04-10_ia-study-guide]]). The scope has widened over time in the corpus:
the same principles of structure, hierarchy, taxonomy, labeling and findability
are applied to the context window of AI systems in
[[2026-06-12_context-architecture]].

## Practice

### Choosing a structure

- Hierarchy depth and breadth should be driven by usability rather than by
  click-count heuristics. [[2019-08-11_3-click-rule]] reports no evidence that
  dropoff or dissatisfaction rise past three clicks; what matters is information
  scent, wayfinding clarity, cognitive load and page-load time — three slow
  clicks are worse than five fast ones. Navigation hubs or landing pages with
  grouped links, descriptions and images at key decision points give users
  stopping points along the journey.
- A polyhierarchy places a child node under several parents so that items are
  findable through more than one reasonable path ([[2018-05-13_polyhierarchy]]).
  Because digital items have no physical location constraint, this is practical
  online, and [[2018-08-12_ecommerce-homepages-listing-pages]] recommends it for
  product findability. But [[2018-05-13_polyhierarchy]] insists on restraint —
  two or three natural parents based on research, not every possible location —
  and notes a direct trade-off with breadcrumbs, which need a single canonical
  path.
- Items that do not fit planned categories should not be forced.
  [[2021-10-17_ia-category-outliers]] draws on family-resemblance categorization
  to argue that atypical members still belong, and offers three options: a
  dedicated subcategory (risking deep, sparsely populated structures), leaving
  outliers in the broader category with search, facets and metadata carrying
  findability, or strategic polyhierarchy.
- Related information split across the site with no links between the pieces
  leaves users unable to discover it; consolidate and cross-link
  ([[2016-10-30_top-10-enduring]]). The intranet version of this failure is
  content silos in team spaces or subsites, usually created by organizational
  politics rather than design intent ([[2016-11-27_top-intranet-design-mistakes]]).
- Merging organizations must be integrated into one coherent structure rather
  than left as parallel intranets, which produces duplication and signals
  disorganization; a two-stage day-one/long-term strategy relieves the pressure
  ([[2018-11-04_intranet-merger-or-acquisition]]).
- In a crisis, [[2020-05-31_covid19-intranet-ia]] presents two strategies —
  consolidating all crisis content in one dedicated section, fastest to build and
  maintain, versus integrating it into the existing IA, better long-term but more
  upfront work. It warns that the severe mistake is leaving now-permanent
  information in temporary locations forever, and recommends crosslinking plus
  improved metadata when content lives in several places.

### Labels and vocabulary

- Category and link labels must make sense both alone and against the other
  options ([[2018-08-12_ecommerce-homepages-listing-pages]]); similar names force
  users to guess which path to take ([[2016-10-30_top-10-enduring]]).
- [[2019-03-24_better-link-labels]] gives four qualities: specific (what will be
  found), sincere (expectations met immediately), substantial (meaningful out of
  context, since users read links rather than surrounding text), and succinct —
  with information-carrying words frontloaded, because users read only the first
  few words when scanning. [[2020-02-02_information-scent]] adds that scent comes
  from the label plus surrounding context and prior knowledge of the source, that
  context is often cut off on mobile so the label itself carries more weight, and
  that clickbait erodes future click-through.
- Branded, invented, or internal terminology blocks discovery.
  [[2021-03-28_keyword-foraging]] warns that inventing a term instead of using
  the established one means users never search for it, and recommends pairing
  plain language with any necessary branded term. [[2018-12-23_branding-intranet]]
  applies the same rule inside organizations: label features descriptively
  ("Upload a Document", "Job Postings") rather than with catchy names or
  third-party product names. [[2024-06-07_menu-design]] and
  [[2019-02-24_footers]] both call for clear conventional labels over vague ones
  like "Resources" or "Help".
- [[2018-07-29_customer-service-model]] found "Customer Service" and "Customer
  Assistance" tested well while "Help" or "Help Center" misled users into
  expecting website navigation help.
- Faceted navigation can teach domain vocabulary: seeing a filter labeled
  "dual-fuel range" hands the user the term they lacked
  ([[2021-03-28_keyword-foraging]]).

### Navigation and wayfinding

- [[2022-04-10_ia-study-guide]] and [[2024-06-07_menu-design]] converge on
  placing navigation where users already look, keeping it visible on large
  screens rather than behind a hamburger, indicating current location, using
  familiar patterns over novel ones, and avoiding multi-level cascading dropdowns
  in favour of mega menus or landing pages. [[2019-08-11_3-click-rule]] likewise
  finds mega menus superior to cascading dropdowns because they show several
  hierarchy levels at once and reduce precision demands.
- Global and local navigation divide the work: global shows the top tier and
  stays constant, local shows the current branch and varies
  ([[2021-07-04_local-navigation]]). Local navigation provides orientation,
  wayfinding and cheap access to deep content; it suits large sites with
  exploratory browsing, supports roughly two to three tiers horizontally, and
  must be visible but less salient than global navigation or users mistake it for
  the main menu.
- Vertical left-side navigation scales to broad hierarchies without forcing
  generic groupings or truncated labels, exploits the fact that users look left
  most of the time, and adapts to mobile with minimal change; the cost is a lower
  content-to-chrome ratio ([[2021-05-16_vertical-nav]]).
  [[2016-06-05_top-intranet-trends]] observes the same move to left-side global
  navigation on award-winning intranets, precisely because megamenus travel badly
  to mobile.
- Breadcrumbs supplement rather than replace primary navigation, should show
  hierarchical position and not session history, should end with a non-linked
  current page, and are unnecessary for shallow or linear structures; on mobile
  they may need truncating or dropping ([[2018-12-23_breadcrumbs]]).
- Global navigation disappearing on subsites or deep pages strands employees, and
  progressive disclosure is not an excuse — navigation is rarely unnecessary
  ([[2016-11-27_top-intranet-design-mistakes]]). Where an organization runs
  subsites, [[2016-09-11_universal-navigation]] prescribes universal navigation on
  every subsite as an "exit sign": visually subordinate to the subsite's own
  navigation, with the universal-home link top-left near the logo, collapsible
  when users rarely switch subsites, and deprioritized on mobile. Both articles
  and [[2016-10-30_top-10-enduring]] describe the same failure mode of users
  stranded on microsites.
- Footers are a deliberate destination, used as a second chance or a last resort
  ([[2019-02-24_footers]]): always carry utility links (contact, customer
  service, privacy, terms), use doormat navigation on long pages, restrict to
  first- and second-level categories rather than a full site map, and keep them
  visible and legible. [[2016-06-05_top-intranet-trends]] records fat footers as
  a winning intranet pattern for the same reason.
- Mobile subnavigation depends on subcategory count in
  [[2017-07-16_mobile-subnavigation]]: accordions inside the main menu under six,
  section menus for six to fifteen, category landing pages above fifteen.
  Sequential menus, though space-efficient, disorient users with low spatial
  ability, who mistake the phone's Back button for the menu's.
- The homepage carries a specific structural load in
  [[2024-03-15_homepage-design-principles]]: it must be reachable through both
  implicit (logo) and explicit ("Home") links with a guessable URL, state who the
  organization is and what it does, show specific examples of offerings rather
  than generic category labels, place primary navigation prominently with clear
  visual hierarchy, and stay predictable rather than inventive.
- Policy content should sit where users expect it — footer links on every page,
  plus contextual links from Settings and near the relevant feature; redundant
  links help here ([[2020-07-26_privacy-policies-terms-use-pages]]).
- [[2018-07-29_customer-service-model]] proposes a hub-and-spoke structure for
  customer service: a Customer Service hub as catch-all, optionally FAQ and
  Contact Us as secondary hubs, all three crosslinked, with granular pages
  (Returns, Shipping) linking back to hubs from body content; more than three hub
  types increases confusion.

### Search as part of the architecture

- Search quality depends on the underlying structure. [[2022-05-22_intranet-search]]
  makes metadata foundational — coherent page titles, meta descriptions and tags,
  backed by naming conventions and process — and recommends a persistent search
  box upper-right, a single unified index across content, people and tools rather
  than separate boxes, results separated into sections with dates and metadata
  labels, and retirement of outdated content.
  [[2016-11-27_top-intranet-design-mistakes]] and [[2016-10-30_top-10-enduring]]
  both trace poor results back to uncrawled, untagged or miscategorized content.
- Taxonomies are the backstage layer that powers faceted navigation, search
  suggestions and related-content recommendations ([[2022-07-03_taxonomy-101]]).
  The article's build sequence is: inventory content, check existing standards,
  identify concepts from research and analytics, evaluate terms, pick preferred
  variants, build relationships, review, apply, maintain. Most so-called
  taxonomies are in practice thesauri, since they add synonymy and associative
  relationships; ontologies support many relationship types and are rarer in UX
  work. Governance is continuous — without it, taxonomies rot.
- Filtering deserves the same care as categorization: a one-size-fits-all facet
  set fails different needs, so support both include and exclude and tailor
  facets to content type ([[2016-10-30_top-10-enduring]]).
- Search-engine results pages have themselves become an information architecture:
  snippets, knowledge panels and People Also Ask answer needs without a click, in
  about 35% of desktop and 62% of mobile searches, with the risk that context is
  lost and source credibility cannot be assessed ([[2020-03-29_good-abandonment]]).

### Research and evaluation methods

- Card sorting is the discovery method: participants group labeled cards by their
  own logic, revealing mental models ([[2024-02-02_card-sorting-definition]],
  [[2024-01-26_mental-models]]). Practical parameters given are 30–50 cards, 15+
  participants for qualitative and 30–50 for quantitative, groups labeled after
  sorting rather than before, and open sorting as the default. Results are ideas,
  not prescriptions — they show only one categorization level, lack context, and
  need designer judgement ([[2024-02-23_card-sorting-tree-testing-differences]]).
  [[2024-06-14_card-sorting-terminology-matches]] identifies keyword matching as
  a specific validity threat, where participants group by shared words rather
  than meaning, and counters it with synonyms, non-parallel grammatical
  structures, in-depth card descriptions, and facilitation that explains
  objectives and encourages thinking aloud.
- Tree testing is the evaluative counterpart, validating whether users can locate
  content in a proposed hierarchy stripped of visual design — which is also its
  limitation, since real sites carry visual cues that aid findability
  ([[2024-02-23_card-sorting-tree-testing-differences]]).
  [[2024-01-19_interpreting-tree-test-results]] gives the metrics: success rate,
  directness, and time; a median success rate of 62% with bands of poor (<40),
  fair (41–60), good (61–80), very good (80–90) and excellent (>90), read against
  task importance rather than absolutes; first clicks as strong predictors of
  success; high success with low directness as a sign of struggle; and 50+
  participants per tree when comparing structures.
- Analytics surface IA problems if interpreted in context.
  [[2016-09-25_ia-warning-signs-analytics]] lists five warning signs — low
  category traffic, low conversion, high bounce on category pages, low entrance
  rates, high search-query volume — and insists each be weighed against strategic
  importance, visual prominence, layout and multi-stage journeys before acting,
  with A/B tests or surveys for ambiguous cases.
- Site-search logs are described by [[2017-07-30_search-log-analysis]] as an
  underused research source that shows what users want and whether the IA serves
  them: analyze query sequences per user, cluster queries by intent to find
  content groupings and cross-link opportunities, compare user vocabulary against
  site language, and watch long queries as distress signals — while protecting
  personally identifiable information. [[2021-03-28_keyword-foraging]] uses the
  same logs to detect users hunting for the right term.
- Eyetracking shows how structure meets scanning. [[2017-03-19_eyetracking-tasks-efficient-scanning]]
  finds gaze patterns are task-driven and ruthlessly efficient, that consistent
  positioning and predictable layouts let users build a scanning algorithm, and
  that the layer-cake pattern means headings must carry the information.
  [[2017-10-29_exhaustive-review-eyetracking]] identifies exhaustive review —
  repeated returns to an area — as evidence of confusion caused by splitting
  related information across page regions or violating placement conventions.
- Other inputs named: interviews with sales and support teams, who see the real
  pain points ([[2021-01-31_quantifying-case-study]]); task analysis or
  jobs-to-be-done to establish the actual sequence of user steps before
  structuring screens ([[2021-07-04_feature-checklists-are-not-enough]]); and
  tracing the full user journey to find where users must leave the site or bounce
  between departments ([[2016-04-24_university-sites]]).
- Business impact is quantified in [[2021-01-31_quantifying-case-study]]: a tree
  test baseline of 4/10 rising to 7.4/10 after redesign, an 85% findability
  improvement against a typical 75% average, reduced support burden through
  self-service, and increased revenue and qualified leads.

### Organizing information on the page

- Chunking related items into meaningful groups is described as fundamental
  ([[2016-03-20_chunking]]): use headings, white space, highlighting and
  background colour to mark boundaries, keep lines around 50–75 characters, and
  format data strings conventionally. The article corrects Miller's "magical
  number seven" — people remember about seven chunks, which is not a limit on
  interface options, and well-structured menus with more than seven items work
  fine. [[2022-08-14_phone-tree-guidelines]] nonetheless caps audio menus at four
  or five distinct options, on the grounds that phone trees remove visual
  landmarks and force sequential memorization; the two are reconcilable as a
  visual-versus-auditory distinction, but the numeric guidance differs.
- Visual hierarchy is the mechanism by which structure becomes perceptible:
  colour and contrast, scale (limited to three sizes), and grouping by proximity
  or common region, validated with the squint test
  ([[2021-01-17_visual-hierarchy-ux-definition]]). Poor layout, unclear hierarchy
  and illegible text are named as core intranet failures
  ([[2016-11-27_top-intranet-design-mistakes]]), and dense walls of text defeat
  scanning ([[2016-10-30_top-10-enduring]]).
- List and listing pages act as a miniature architecture.
  [[2016-04-10_list-entries]] argues for balancing density so users need not pogo
  stick to detail pages, prioritizing attributes from analytics and research,
  mapping priority onto placement and typography, and keeping entries consistent
  so they can be compared by scanning — with exceptions (sale, sold out) limited
  to two or three. [[2018-08-12_ecommerce-homepages-listing-pages]] merges
  subcategories above product listings to encourage browsing without choice
  overload, and notes that on mobile listings must carry enough differentiating
  information to avoid detail-page visits.
- Tabs chunk related content and work best with few options and related content
  inside each; in-page and navigation tabs must not be mixed, selected state
  needs at least two visual cues, and labels need information scent because
  unselected tabs hide their content ([[2024-08-02_tabs-used-right]]). On desktop
  tabs suit long content and complex layouts while accordions suit mobile and
  short content like FAQs.
- In-page links give an overview of a page and let users skip irrelevant
  sections; they require clear labels such as "On This Page", link styling, long
  enough content, and genuinely divisible sections
  ([[2023-10-01_in-page-links-content-navigation]]).
- Policy pages need a plain-language high-level summary at the top, web-readable
  formatting, and a clickable table of contents or left rail; functional
  navigation makes a policy feel transparent even unread
  ([[2020-07-26_privacy-policies-terms-use-pages]]).
- What to hide is itself an IA decision. [[2026-01-23_info-tips-bad]] holds that
  essential instructions, constraints, form limits and legal disclaimers must
  never live inside info tips, that tips should be inline rather than modal, and
  that they are not a decluttering tool — dense layouts and poor labels need
  redesign. [[2017-04-23_modal-nonmodal-dialog]] applies the same priority
  reasoning to dialogs: modals for critical errors, irreversible actions and
  genuinely required information, never for marketing or upsells, and never
  during high-stakes flows such as checkout.
- Recognition beats recall, so options should be visible and discoverable rather
  than remembered; history, favorites and recently-viewed items make past context
  available ([[2024-01-15_recognition-and-recall]]).
- Status information should lead with the latest update, use plain language
  instead of backend codes, and be structured for scanning
  ([[2019-02-03_status-tracker-progress-update]]). Notifications should be
  organized by type and urgency — reactive, proactive, optimization — each with
  its own timing, intensity and channel, with thresholds and grouping to prevent
  fatigue ([[2026-02-20_smart-home-notifications]]).

### Placement relative to the task

- Feature completeness is not enough: information and controls must appear at the
  point of need in the sequence users actually follow, or the design becomes
  interrupt-heavy; embedded workflow problems are chronic because fixing them
  means refactoring ([[2021-07-04_feature-checklists-are-not-enough]]).
- Complex applications should reduce clutter with staged disclosure while
  preserving capability, ease transitions between primary and secondary
  information levels via hover and contextual displays, and make critical
  information salient ([[2020-11-08_complex-application-design]]).
- Top tasks must be reachable even when rare. [[2024-07-19_top-tasks]] shows a
  utility's outage map buried below metrics and explanatory text during a
  hurricane, compounded by multiple outdated maps and jargon-filled status
  labels; dormant tasks can become critical in a crisis.
- Sites should anticipate knowledge gaps and structure information for synthesis
  and side-by-side comparison with consistent attributes, rather than leaving
  users to assemble it themselves across tabs
  ([[2019-03-03_unbridged-knowledge-gaps]]).
- Recommendations should be split into specific genre- or behavior-based
  categories rather than pooled, and placed high on the page
  ([[2018-11-04_recommendation-guidelines]]).
- Media formats have a place in the hierarchy: [[2020-08-30_virtual-tours]] finds
  photos serve as the primary touchpoint, narrated or expert-led video as
  secondary, and interactive tours as a tertiary option consulted late for
  spatial verification — with wayfinding inside tours a recurring weak point.
- Locators must make three steps easy — finding the locator link, finding the
  location, and getting directions — with geolocation offered explicitly and
  external mapping tools preferred over proprietary maps
  ([[2018-10-07_store-finders-and-locators]]).

### Findability failures in specific contexts

- University sites: 48% of tested users did not realize a university offered
  their target program because they could not find it; the recommendations
  include a discoverable complete list of majors grouped by field or school,
  prominent deadlines, scannable facts, and robust internal search, since users
  otherwise turn to aggregators and review sites
  ([[2016-04-24_university-sites]]).
- WeChat: findability breaks when many accounts share similar names, verification
  marks do not clarify legitimacy, and account types (service versus
  subscription) silently change what works; standardized interaction patterns
  across official accounts reduce learning cost
  ([[2016-08-21_wechat-integrated-ux]]).
- Information-seeking behaviour itself has shifted: understand-oriented activity
  grew to 40% of critical internet use while compare/choose fell to 36%, passive
  acquisition through exploration and notifications rose from 4% to 14%, and 42%
  of critical incidents now happen on smartphones — so structures must support
  learning, browsing-based discovery and device switching
  ([[2020-01-26_information-seeking-behavior-changes]]).
- Contextual menus and legacy workflows are cited as everyday cases where
  structure and navigation patterns decide usability, with secondary actions
  belonging in contextual menus and icons kept consistent across screens
  ([[2026-01-02_ux-quiz]]).

### Extending IA to AI systems

- [[2026-06-12_context-architecture]] applies IA directly to the context window:
  system instructions, retrieved knowledge, skills, tools and memory all compete
  for the model's attention, so hierarchies must prioritize, taxonomy and
  controlled vocabulary must make skills and tools discoverable, and labels must
  align with user language rather than engineering terminology — poor labeling
  produces wrong tool selection.
- [[2026-04-17_less-chat-more-answer]] finds users treat site chatbots as search
  bars and applies familiar structural rules: essential answer first with detail
  pulled on demand (a truncated pyramid), short paragraphs, lists, headers and
  white space, and plain refusals.
- [[2025-04-25_prompt-suggestions]] organizes prompt suggestions into use-case
  suggestions, prompt autocomplete and followup questions, each serving
  discoverability, efficiency or engagement, addressing the blank-page problem
  when users do not know what a system can do.
- [[2023-11-24_ai-prompt-structure]] identifies request, references, format and
  framing as recurring components of effective prompts, and notes that
  request-only prompts behave like bare search queries and produce funneling
  conversations.

## Sources (67)

- [[2016-03-20_chunking]] — organizing related items into coherent groups is fundamental to IA.
- [[2016-04-10_list-entries]] — The article describes how list entries serve as a mini-IA, organizing attributes hierarchically to help users navigate choices.
- [[2016-04-24_university-sites]] — Design guidelines focus on navigation clarity, content organization, and information hierarchy to help users find critical decisions.
- [[2016-06-05_top-intranet-trends]] — Navigation patterns (left-side, fat footers), search evolution, and content organization are central to intranet usability improvement.
- [[2016-07-10_customization-personalization]] — Neither customization nor personalization can rescue poor information architecture; strong baseline structure must come first.
- [[2016-08-21_wechat-integrated-ux]] — Reveals challenges in findability when many accounts share similar names, verification checkmarks don't clarify legitimacy, and account types (service vs. subscription) break expected functionality patterns.
- [[2016-09-11_universal-navigation]] — Shows how organizational structure (multiple sites, subsites) requires clear hierarchical navigation design to prevent users from getting lost or forming false conclusions about site scope.
- [[2016-09-25_ia-warning-signs-analytics]] — Analytics metrics reveal IA problems by exposing discrepancies between user vocabulary and category names through low search traffic and high search-query volume; however, contextual interpretation is essential for distinguishing true issues from strategic categories that serve niche needs.
- [[2016-10-30_top-10-enduring]] — Aligning site structure with user mental models is critical; surprises in content location stem from organization based on company thinking rather than user expectations.
- [[2016-11-27_top-intranet-design-mistakes]] — Preventing content silos requires integrated information architecture and proper linking; search and navigation integration across potential subsites is critical.
- [[2017-03-19_eyetracking-tasks-efficient-scanning]] — Shows that information hierarchy, positioning, and layout structure directly support or hinder efficient task completion based on how well design aligns with user scanning patterns.
- [[2017-04-23_modal-nonmodal-dialog]] — Shows how information priority and task criticality should determine whether dialogs are modal or nonmodal, and whether dialogs are appropriate at all.
- [[2017-07-16_mobile-subnavigation]] — how site structure is reflected in navigation patterns, and how mobile constraints require different presentation strategies than desktop.
- [[2017-07-30_search-log-analysis]] — using search log insights to improve site organization, navigation labels, content grouping, and cross-linking based on actual user behavior.
- [[2017-10-29_exhaustive-review-eyetracking]] — addresses organization of content and placement of UI elements to match user expectations and reduce search behavior.
- [[2018-05-13_polyhierarchy]] — Polyhierarchical organization accommodates multiple user mental models by enabling users to locate content through any reasonable categorization path they might expect without duplicating every possible link.
- [[2018-07-29_customer-service-model]] — This article proposes the hub-and-spoke model as a standardized framework for organizing customer-service information on websites, addressing inconsistencies that force users into trial-and-error searching.
- [[2018-08-12_ecommerce-homepages-listing-pages]] — the structural design of ecommerce sites; proper IA helps users navigate product hierarchies, understand category relationships, and locate items efficiently through clear labeling and logical organization.
- [[2018-10-07_store-finders-and-locators]] — the structural design of locator tools, including navigation, labeling, and how to organize location results when stores meet certain criteria like amenities or hours.
- [[2018-11-04_intranet-merger-or-acquisition]] — organizing and integrating information from multiple organizations into a coherent structure that employees can navigate and understand.
- [[2018-11-04_recommendation-guidelines]] — how to structure recommendation sections into logical categories that improve discoverability and usability for users with diverse interests.
- [[2018-12-23_branding-intranet]] — Clear labeling and organization of intranet features using descriptive language rather than branded terms ensures discoverability and reduces cognitive load for employees seeking information.
- [[2018-12-23_breadcrumbs]] — Hierarchical site structure that breadcrumbs represent and help users navigate, showing the relationship between pages and helping users understand overall site organization.
- [[2019-02-03_status-tracker-progress-update]] — Organization of tracking information with clear visual hierarchy, scannable layouts, and strategic use of progress bars and dated entries.
- [[2019-02-24_footers]] — Organizing footer content with appropriate hierarchy, visual grouping, and labeling to support scanning and findability.
- [[2019-03-03_unbridged-knowledge-gaps]] — Organizing and presenting information to support complex synthesis tasks and comparisons across multiple attributes or alternatives.
- [[2019-03-24_better-link-labels]] — Specific, substantial links help users locate the information they need without wasted clicks.
- [[2019-08-11_3-click-rule]] — The article argues that hierarchical IA breadth/depth choices should be driven by usability principles rather than arbitrary click-count rules.
- [[2020-01-26_information-seeking-behavior-changes]] — Demonstrates that information architecture must accommodate understand-oriented information seeking, passive discovery through browsing, and seamless cross-device experiences.
- [[2020-02-02_information-scent]] — Shows how context and page organization influence how link scent is perceived, and how structure affects user navigation confidence.
- [[2020-03-29_good-abandonment]] — examines how search engine results pages organize information through features like snippets and knowledge panels, fundamentally changing user behavior.
- [[2020-05-31_covid19-intranet-ia]] — addresses IA strategy for organizing crisis-related content with guidance on temporary consolidation versus permanent integration approaches.
- [[2020-07-26_privacy-policies-terms-use-pages]] — organizing policy information for findability and user control through navigation and structure.
- [[2020-08-30_virtual-tours]] — Virtual tours work best when integrated into information hierarchies with photos as primary touchpoint, narrated videos as secondary, and interactive tours as tertiary options for detailed spatial verification.
- [[2020-11-08_complex-application-design]] — organizing interface structure and information access in complex applications to reduce clutter, support learning, and enable quick access to critical data without overwhelming users.
- [[2021-01-17_visual-hierarchy-ux-definition]] — shows how visual hierarchy works in concert with content and layout to help users understand and navigate information.
- [[2021-01-31_quantifying-case-study]] — shows how poor IA creates support burden and how improved IA can increase self-service and business outcomes.
- [[2021-03-28_keyword-foraging]] — the article addresses how information architecture and navigation help users discover correct terminology.
- [[2021-05-16_vertical-nav]] — Vertical navigation enables IA that naturally fits broad information spaces without forcing generic groupings or abbreviated labels.
- [[2021-07-04_feature-checklists-are-not-enough]] — How information is organized affects whether users can find what they need at the point when they need it.
- [[2021-07-04_local-navigation]] — Hierarchical IA structure determines whether local navigation is appropriate and how many tiers can be shown effectively.
- [[2021-10-17_ia-category-outliers]] — The article addresses a core IA challenge: how to structure content when items don't fit neatly into planned categories.
- [[2022-04-10_ia-study-guide]] — the underlying structural organization of content and information systems.
- [[2022-05-22_intranet-search]] — The underlying structure that supports effective search through clear naming conventions, consistent metadata, and organized content; essential elements include page titles, meta descriptions, and tags that enable search to deliver relevant results.
- [[2022-07-03_taxonomy-101]] — Taxonomies are backstage IA structures and formal metadata systems that organize concepts to support content discovery and retrieval through faceted navigation, search suggestions, and related-content recommendations, ensuring consistent logical classification by controlling which terms content creators can use and separating logical precision from user mental models.
- [[2022-08-14_phone-tree-guidelines]] — Phone menus must balance depth with breadth; linear menus are less efficient than rectangular layouts, and all levels must support undoing selections.
- [[2023-10-01_in-page-links-content-navigation]] — In-page links provide an overview of page content that helps users form mental models and assess whether a page meets their information needs.
- [[2023-11-24_ai-prompt-structure]] — prompts themselves have a structure with distinct components that parallel information architecture principles for organizing complex information.
- [[2024-01-15_recognition-and-recall]] — menu structures and information organization should support recognition by making options visible and discoverable.
- [[2024-01-19_interpreting-tree-test-results]] — tree testing assesses whether category labels and hierarchy enable users to find information; results guide IA improvements.
- [[2024-01-26_mental-models]] — card sorting research helps align navigation structures with users' mental models of how content should be organized.
- [[2024-02-02_card-sorting-definition]] — the core design challenge that card sorting helps address by aligning navigation with user expectations.
- [[2024-02-23_card-sorting-tree-testing-differences]] — the design domain where both methods contribute distinct but complementary insights.
- [[2024-03-15_homepage-design-principles]] — addresses structuring homepage navigation and content organization to help users understand and access site offerings.
- [[2024-06-07_menu-design]] — navigation menus should communicate site structure and content organization; visible menus help users understand scope and available options.
- [[2024-06-14_card-sorting-terminology-matches]] — card-sorting research reveals how users expect information to be organized; keyword-matching bias undermines the validity of IA insights.
- [[2024-07-19_top-tasks]] — demonstrates how poor content organization, cognitive load, and language complexity can prevent users from completing essential tasks.
- [[2024-08-02_tabs-used-right]] — addresses how tabs serve to structure and present related content in scannable chunks.
- [[2025-04-25_prompt-suggestions]] — organizes prompt suggestions by type and purpose to support discovery of system capabilities and guide user navigation through possibility space.
- [[2026-01-02_ux-quiz]] — Contextual menus and legacy user workflows demonstrate how information structure and navigation patterns affect usability.
- [[2026-01-23_info-tips-bad]] — Info tips reflect broader IA decisions; deciding what to hide and what to surface is fundamental to information structure.
- [[2026-02-20_smart-home-notifications]] — Organizing notifications by type, urgency, and impact helps users understand what requires immediate action and what can wait.
- [[2026-04-17_less-chat-more-answer]] — Shows how structuring information in chatbots mirrors principles of good web IA: clear hierarchy, scannable organization, progressive disclosure.
- [[2026-06-12_context-architecture]] — IA principles—structure, hierarchy, taxonomy, labeling, findability—apply to designing context for AI systems; good IA reduces ambiguity and cognitive load on the model.
- [[2024-01-23_laws-of-ux_05-3-millers-law]] — the organization and structure of content, including hierarchy and relationships between information groups; using spacing, color, scale, headings, and dividers to visually separate and organize information into distinct, scannable sections.
- [[2022-01-19_product-management-for-ux-people_06-chapter-3-ux-skills-that-carry-over]] — IA is identified as perhaps the single most directly applicable UX skill to product management; it provides tools for consensus-building and mapping meaning relationships that serve all disciplines, and IA artifacts make product direction visible to entire teams.
- [[2019-12-17_storytelling-in-design_12-chapter-11-theme-and-story-development-in-product-design]] — shaped by the product's theme and red thread; organizes content to reflect user mental models and expectations, ensuring the structure tells the story users expect regardless of their entry point.
