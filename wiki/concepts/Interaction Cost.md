---
type: concept
name: Interaction Cost
created: 2026-07-31
updated: 2026-07-31
status: developed
---

# Interaction Cost

## Definition

Interaction cost is the sum of effort — physical and mental — a user must invest
to complete a task [[2017-12-03_iphone-x]]. It is not the same thing as the
number of clicks: it accumulates from extra steps, from cognitive load (deciding,
remembering, recovering context), from precision demands, and from technical
factors such as page load time [[2019-08-11_3-click-rule]]. Anything that hides,
duplicates, interrupts or delays raises it; anything that removes a step, keeps
information in place or resumes the user's context lowers it.

The cost matters because it is weighed against perceived value. When the effort
required to complete a task exceeds what the activity is worth to the user, they
abandon the task, or the brand [[2017-03-19_seamless-cross-channel]]. This is
also how the concept links to pain points, which are defined partly by the extra
steps, help-seeking and complicated workflows they force on users
[[2021-05-16_pain-points]]. Cost is not always fatal: users will absorb an
initially high cost when the perceived value is high enough, as with the
iPhone X's invisible gestures, and repetition erodes the cost over time
[[2017-12-03_iphone-x]].

## Practice

### Do not measure it by counting clicks

The 3-click rule has no empirical support: research found no evidence that
dropoff rises or satisfaction falls past three clicks. Click count depends on
task complexity and design rather than an absolute threshold, and clicks are not
equivalent to each other — three clicks with long load times are worse than five
fast ones. What actually drives navigation experience is information scent,
strong menu labels and wayfinding (breadcrumbs, local navigation, a sense of
where you are). Mega menus beat cascading dropdowns even when they need as many
or more clicks, because they show several hierarchy levels at once, allow error
correction and demand less pointer precision; navigation hubs at key decision
points give users grouped links, descriptions and vocabulary help
[[2019-08-11_3-click-rule]].

### Hiding raises the cost

Hiding is the most consistent cost-adding pattern across the sources.

- **Chrome-hiding modes.** Zen mode looks like it reduces clutter but forces
  users to divert attention from the task to find and recall where tools went;
  mode switching adds its own overhead (track which mode you are in, which
  features exist in it, how to switch). Learning does not rescue it — even
  frequent users struggle with hidden interfaces lacking visible signifiers, as
  Windows 8 showed — and aesthetic appeal does not offset the usability cost
  [[2016-12-18_zen-mode]].
- **Dropdown lists.** Interacting takes three steps (open, scroll, select), the
  collapsed state gives almost no information scent, and scroll precision is
  demanding, especially on mobile. Avoid them for fewer than 5–7 options (radio
  buttons expose everything in one click), for more than about 15 (use a
  filterable combobox, or skip selection entirely with address lookup), for
  familiar data like ages, birthdates and heights where typing is faster and less
  error-prone, and wherever users need visual comparison — product variants
  should be buttons that surface availability and out-of-stock states upfront.
  They remain justified for roughly 5–10 options, for secondary fields, or when
  fields must stay visually compact [[2026-07-17_dropdown-list]].
- **Info tips.** Every activation costs something, so it is only justified when
  the tip delivers genuine value rather than repeating the obvious or carrying
  marketing fluff. Essential instructions, constraints, form limits and legal
  disclaimers must never live inside them. Keep them inline or adjacent rather
  than in modals or overlays that hijack focus, distinguish the "i" icon
  (optional information) from "?" (help and support), and assume most users never
  open them. They are not a decluttering tool: dense layouts and poor labels need
  redesign, not a hidden layer [[2026-01-23_info-tips-bad]].
- **Point-of-need information.** Basic information essential to a primary task
  should be visible, not behind a click; interrupt-heavy designs that make users
  hunt for the next function disrupt progress instead of supporting it, and
  warnings should be actionable where they appear rather than on a separate
  screen. Task analysis or jobs-to-be-done analysis, done before screens are
  structured, is what prevents these workflow problems from becoming chronic
  [[2021-07-04_feature-checklists-are-not-enough]].
- **Save-for-later features.** These go unused when hidden behind swipes,
  dropdowns or placement low on the page: they must be visible, clearly labelled
  with strong information scent and low-effort. Requiring registration or login
  to save an item derails checkout and deters use outright
  [[2018-11-04_wishlist-or-cart]].
- **Notification settings.** Turning notifications off must be easy and obvious
  inside the app; burying settings behind multiple navigation steps or pushing
  users to global device settings raises effort and erodes trust
  [[2018-11-18_push-notification]].

### Redundancy and noise cost too

Extra content is not free. Duplicate links on a page make users process each one
and decide whether the destinations differ, deplete the finite attention
available to other links, and cause wasted repeat visits to a page already seen —
and analytics showing more traffic to the duplicated destination are misleading,
since that traffic may simply be drawn from clicks elsewhere. If a link matters,
give it visual prominence rather than repeating it; if duplication is genuinely
justified, place the copies far enough apart that they are never visible on the
same screen. The one exception is a graphic plus its label, which users perceive
as a single link [[2016-03-13_duplicate-links]].

The same logic applies to alt text, where cost is measured in listening time:
adding alt text to images whose information already appears in the page copy
makes screen-reader users sit through repetition for no gain. Alt text should
communicate an image's purpose in completing the task, not its appearance, and
the decision runs through three questions — is the information repetitive, is the
image referenced by page copy, and would alt text help users complete tasks more
efficiently. Good page copy does more accessibility work than alt text, and
tools that auto-generate alt text for every image add cost rather than removing
it [[2024-11-15_alt-text-usability]].

Enriched site-search suggestions are a documented case of added content failing
on cost grounds: they were used only 7 times out of 60 encounters in a usability
study. Users in search mode are goal-focused rather than exploratory, image-based
enriched results often load too slowly to be seen before the query is submitted,
banner blindness makes users overlook even exact matches shown graphically, and
unlabelled suggestions read as ads. Plain text autocomplete, by contrast, is
heavily used and should be kept fast and simple; shifting content types and
inconsistent placement in the enriched container only add perceived noise
[[2022-08-21_enriched-site-search-suggestions]]. This sits in tension with the
earlier account of search suggestions, which credits rich suggestions — links to
category pages, product pages and articles — as a way to reduce cost for sites
with visually diverse products, while still requiring that every suggestion
return relevant results, that typed and suggested characters be visually
distinguished, and that mobile fall back to text only
[[2018-05-20_site-search-suggestions]]. Both agree that a suggestion returning
zero or irrelevant results is worse than no suggestion at all.

### Removing steps

- **Search suggestions** let users pick a query instead of typing it in full, and
  spare them typos and the mental effort of formulating a query
  [[2018-05-20_site-search-suggestions]].
- **Saved scroll position** removes the repetitive scrolling and scanning needed
  to get back where you were, which matters most during pogo-sticking between a
  listing and its detail pages. Reset it when content updates in real time or
  when significant time has passed (roughly beyond a 30–60 minute session), since
  landing deep in a stale page is disorienting; when intent is unclear, preserve
  position as the least disruptive default but offer a jump to the latest
  content, and signal a reset with a visible scroll animation
  [[2025-07-11_saving-scroll-position]], [[2022-03-06_alternatives-pagination-listing-pages]].
- **Pagination alternatives.** Show More buttons and infinite loading carry lower
  interaction cost than numbered pagination for small and medium catalogues,
  while mega-retailers with huge inventories still need pagination for precise
  navigation. Infinite loading works under roughly 40 items per page with good
  filters and fast loading, but pushes the footer out of reach; Show More keeps
  the user in control, which matters on limited mobile data plans, and leaves the
  footer accessible between batches. Either way, display the total count, how
  many are loaded and how many remain
  [[2022-03-06_alternatives-pagination-listing-pages]].
- **External entry points on mobile.** Over 40% of mobile usage happens in
  microsessions shorter than 15 seconds, and time on task correlates inversely
  with usability, so letting users finish without launching the app is a direct
  cost reduction: notifications that convey a fully formed idea without needing
  the app opened, self-contained untruncated widgets for quick data checks, quick
  actions on the home screen for genuinely frequent tasks, and voice-assistant
  integration. Adoption rates are low but implementation effort is minimal, so
  ROI stays high [[2019-11-03_mobile-microsessions]].
- **Noncommand interfaces.** Augmented reality lowers cost by displaying
  information in context without the user issuing any command — an aircraft
  mechanic sees a part's service record in place instead of memorising a part
  number and navigating a separate system — and cuts attention-switching by
  merging several information sources into one overlay. Context and timing let the
  same gesture mean different things without explicit commands. Badly designed AR
  can still overwhelm users with clutter and irrelevant information
  [[2016-09-18_augmented-reality-ux]].
- **Interaction style.** Contrary to the assumption that conversation is the
  low-effort interface, WeChat research in China found most users prefer
  menu-based and GUI interaction to typed text commands on mobile, and that
  standardized interaction patterns across official accounts reduce cognitive
  load compared with the diversity of traditional websites — convenience, not
  conversation, drove adoption [[2016-08-21_wechat-integrated-ux]].

### Cost across a whole journey

Crossing channels is where cost concentrates. Seamlessness means zero or minimal
overhead moving between channels: picking up where you left off without redoing
work or reestablishing context. Users switch channels because of external
interruptions, because another channel suits the task better, or because the
activity inherently needs several. Roadblocks — scanning failures, incompatible
systems, missing next-step instructions, no fallback when the primary workflow
fails — push the cost above the perceived value and users leave. The remedies are
easy resumption (authentication, email links, passcodes, OS handoff), sandboxes
that hold progress (wishlists, save-for-later, recently viewed) and proactively
facilitated next steps; and because these roadblocks are often rooted in separate
fulfilment or processing systems, backend integration is usually part of the fix
[[2017-03-19_seamless-cross-channel]]. Pain points at interaction level are
identified by usability testing and prioritized by impact, frequency and
likelihood of recurrence, with interaction cost and cognitive load as their
characteristic cost to users [[2021-05-16_pain-points]].

### When users refuse to pay

Users are strikingly unwilling to spend effort on anything that does not serve
their immediate goal. In recommendation systems, participants found inaccurate
suggestions easy to ignore and simply kept browsing rather than rating or
dismissing them to improve future results — so systems should not count on
explicit feedback, and users expect explicit actions like purchases and saves to
weigh more than passive browsing anyway
[[2018-09-30_recommendation-expectations]]. In search, the interaction is brief
and transactional enough that a small loading delay or a distraction from the
goal is sufficient to lose the user
[[2022-08-21_enriched-site-search-suggestions]]. Conversely, high perceived value
buys tolerance: only a brand strong enough to make the product worth the trouble
can introduce invisible gestures, and even then the design needs a visual
signifier such as the iPhone X's home line to avoid the Windows 8 failure, plus
enough daily repetition for the cost to fall over time
[[2017-12-03_iphone-x]].

## Sources (20)

- [[2016-03-13_duplicate-links]] — the article discusses why extra choices increase the cost of using an interface.
- [[2016-08-21_wechat-integrated-ux]] — Shows that menu-based and GUI interaction have lower interaction cost than text-based commands on mobile, driving user preference despite WeChat's conversational interface origins.
- [[2016-09-18_augmented-reality-ux]] — Shows how AR eliminates steps required in traditional screen-based UIs (remembering part numbers, navigating separate systems), allowing users to stay in their environment and accomplish tasks with minimal effort.
- [[2016-12-18_zen-mode]] — hiding tools increases the steps and mental effort required to access them, directly raising interaction cost during tasks.
- [[2017-03-19_seamless-cross-channel]] — Central concept showing that when friction in cross-channel transitions exceeds the perceived value of the activity, users exit the experience entirely.
- [[2017-12-03_iphone-x]] — The effort users must invest to complete a task; invisible gestures increase cognitive load compared to visible buttons, though frequent repetition eventually reduces this cost.
- [[2018-05-20_site-search-suggestions]] — Search suggestions reduce interaction cost by letting users select from suggestions rather than typing complete queries, and by helping them avoid typos and mental effort in formulating searches.
- [[2018-09-30_recommendation-expectations]] — how users avoid investing effort to provide feedback on recommendations, preferring to simply ignore irrelevant suggestions rather than actively rating or dismissing them.
- [[2018-11-04_wishlist-or-cart]] — the effort required to save items for later must be minimal; requiring registration or complex processes prevents usage and increases abandonment.
- [[2018-11-18_push-notification]] — the effort required to disable notifications must be low; hiding settings behind multiple navigation steps or global settings increases effort and user frustration.
- [[2019-08-11_3-click-rule]] — Click counting is a crude proxy for interaction cost; actual cost depends on cognitive load, clarity, and technical factors like page load time.
- [[2019-11-03_mobile-microsessions]] — demonstrates how reducing interaction cost through notifications, widgets, and quick actions enables faster task completion and better UX.
- [[2021-05-16_pain-points]] — Pain points increase interaction cost when users must take additional steps, seek help, or navigate complicated workflows to achieve their goals.
- [[2021-07-04_feature-checklists-are-not-enough]] — Hidden information behind clicks increases interaction cost; essential information for primary tasks should be visible.
- [[2022-03-06_alternatives-pagination-listing-pages]] — Show More buttons and infinite loading reduce interaction cost compared to pagination but require careful implementation (displaying counts, supporting pogo-sticking, considering mobile data concerns).
- [[2022-08-21_enriched-site-search-suggestions]] — Search is brief and transactional; even small delays in content loading or distractions from the search goal can cause users to lose interest or abandon suggestions.
- [[2024-11-15_alt-text-usability]] — Demonstrates how redundant alt text increases the interaction cost for screen-reader users by requiring them to listen to information they already have access to elsewhere on the page.
- [[2025-07-11_saving-scroll-position]] — Saving scroll position directly addresses interaction cost by eliminating repetitive scrolling and scanning needed to return to a user's previous location.
- [[2026-01-23_info-tips-bad]] — Every info-tip activation incurs a small cost; that cost is only justified when the tip delivers genuine value, not repetition or obvious information.
- [[2026-07-17_dropdown-list]] — increases when dropdowns hide options, requiring multiple steps and scroll precision, especially problematic for long lists and mobile users.
