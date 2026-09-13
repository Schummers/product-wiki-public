---
type: concept
name: Menu Design
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Navigation Menu"
---

# Menu Design

## Definition

A menu is a list of options in a graphical user interface, either permanently
visible (menu bars) or expandable behind a handle
[[2016-05-08_expandable-menus]]. Menus carry two jobs at once: wayfinding, helping
users locate content, and orientation, helping them understand where they are and
what else is available [[2024-06-07_menu-design]]. Sub-navigation is the specific
UI that gives access to lower levels of the information architecture
[[2017-07-16_mobile-subnavigation]].

Two design problems recur across every menu type: making the handle discoverable,
looking clickable and carrying good information scent, and minimising selection
time, which is visual search time plus movement time
[[2016-05-08_expandable-menus]]. The movement half is governed by motor laws
rather than taste: Fitts's Law for point-and-click targets
[[2022-07-31_fitts-law]] and the Accot-Zhai steering law for anything requiring a
pointer to travel down a bounded tunnel, such as a dropdown or a hierarchical
menu [[2019-06-23_steering-law]]. The recurring observation from testing is
practical: users are too often seen struggling with menus that are confusing,
hard to manipulate, or hard to find [[2024-06-07_menu-design]].

## Practice

### Visibility and placement

Keep navigation visible on desktop; a hamburger that hides navigation on a large
screen removes users' sense of the site's scope and available options, out of
sight meaning out of mind. The hamburger is described as a necessary evil on
small screens only [[2024-06-07_menu-design]]. Put menus where they are expected:
primary navigation in the header on desktop or on the left in applications,
utility navigation at the top, local navigation on the left, footer navigation at
the bottom [[2024-06-07_menu-design]]. Indicate the current location clearly, via
breadcrumbs or a highlighted current page [[2024-06-07_menu-design]]. Screen
edges are a free efficiency gain: an edge target behaves as an infinite target
because the boundary prevents overshooting, which is why operating systems place
menu bars and taskbars there (macOS at the top edge, the Windows start button in
the bottom-left corner) [[2022-07-31_fitts-law]].

### Choosing a menu shape

Menu geometry changes the average distance to an option. Linear pull-down menus
have the shortest movement time to the first item and the longest to the last, so
very long ones should be avoided, and aligning the handle with the middle item
reduces the average distance. Rectangular menus and mega menus reduce average
distance compared with a linear arrangement. Pie or radial menus put every option
at equal distance, which is optimal in theory, but users' lack of familiarity
cancels the advantage; marking menus, a pie variant, add an expert mode where a
user moves toward the target without displaying the menu, and suit touch and
contextual use [[2016-05-08_expandable-menus]]. Fitts's Law analysis reaches the
same ranking: rectangular menus beat linear ones on average distance, and pie
menus offer equal distance but remain unfamiliar [[2022-07-31_fitts-law]].

Familiarity is the moderating variable: initial learning time can easily outweigh
the movement-time savings unless users will use the menu many times, so novel menu
types belong in high-frequency contexts, or should wait until familiarity rises
[[2016-05-08_expandable-menus]]. The checklist source states the same conclusion
more bluntly: avoid gimmicky navigation patterns, since stakeholders may be
impressed by novel menu designs but users are far more impressed by great content
easily accessed with familiar menus [[2024-06-07_menu-design]].

### Mega menus

Mega menus are two-dimensional dropdown panels showing many grouped choices at
once without scrolling, and they work well for large information architectures
[[2017-03-26_mega-menus-work-well]]. They beat regular dropdowns because all
options are visible at a glance instead of demanding scrolling and short-term
memory, because they support visual grouping that clarifies relationships, and
because they accommodate illustrations and richer typography; regular dropdowns
support grouping only through kludges such as indenting with space characters
[[2017-03-26_mega-menus-work-well]]. They also sidestep the steering law by
allowing free two-dimensional movement instead of forcing a pointer down a narrow
tunnel [[2019-06-23_steering-law]].

Implementation details from that source: for hover-based mega menus, require the
mouse to remain stationary for 0.5 seconds before appearing (to avoid flicker on
pass-through), display within 0.1 seconds after that, and keep the menu visible
until the pointer has been outside for 0.5 seconds; handle the diagonal problem by
detecting the pointer's trajectory toward a dropdown item so the menu does not
disappear erratically when the path briefly exits the active area; chunk related
options at medium granularity, neither too coarse nor too fragmented; start labels
with information-carrying words; order groups by workflow or importance; and never
duplicate an option [[2017-03-26_mega-menus-work-well]]. Keep them simple: avoid
complex interactions, GUI widgets, text inputs or search boxes inside the menu,
since fewer options mean less to scan, less to understand and less to get wrong
[[2017-03-26_mega-menus-work-well]]. Accessibility needs explicit handling, as
screen-magnifier users may see only part of the menu and tiny options cause
selection errors on touchscreens; the recommendation is both a simple solution
(clickable top-level items leading to full pages) and an advanced one (jQuery
screen-reader accessibility) [[2017-03-26_mega-menus-work-well]].

### Dropdowns and hierarchy

Distinguish dropdown menus (commands and navigation) from dropdown boxes (form
selection): each has its own visual treatment and interaction pattern, and using
the wrong one creates confusion [[2017-06-11_drop-down-menus]]. Resist very long
dropdowns, which violate the steering law because users cannot see all options at
once and must carefully hold the pointer's position; for large option sets, use
mega menus, HTML lists, or an input field with validation
[[2017-06-11_drop-down-menus]]. Avoid interacting menus, where the options in one
change based on a selection in another, since options appearing and disappearing
confuses users; gray out unavailable options rather than removing them, because
removal breaks spatial consistency and makes the interface unpredictable; allow
typing for well-known data such as states, countries or birthdates; and keep the
menu label visible when the menu is open, so users retain the scope of what they
are choosing among [[2017-06-11_drop-down-menus]]. Burying top-level categories is
called out as detrimental to user success on any site
[[2017-06-11_drop-down-menus]].

On depth, the sources converge. Avoid multi-level cascading menus, which are hard
to manipulate; use mega menus or landing pages instead
[[2024-06-07_menu-design]]. Hierarchical menus create competing tunnel-width
constraints, and mega menus or flatter structures avoid the narrow tunnels
altogether [[2019-06-23_steering-law]]. Where a tunnel is unavoidable, keep it as
short and as wide as possible and add generous padding so minor deviations do not
drop the user out of it [[2019-06-23_steering-law]].

### Labels and targets

Use clear, familiar link labels; avoid jargon, internal terminology and overly
creative wording, so users immediately understand where a link leads
[[2024-06-07_menu-design]]. Make links big enough to click, at least 1cm by 1cm,
because small or tightly spaced links frustrate users and raise error rates
[[2024-06-07_menu-design]]. Fitts's Law explains why: increasing target size
reduces interaction time more effectively than reducing distance, labels should
accompany icons because the combined area is larger and faster to acquire, and
crowding targets increases accidental overshoot errors, so adequate spacing is
needed beyond the active click area alone [[2022-07-31_fitts-law]].

### Mobile and touch

Touch changes the mechanics. After a menu opens, the finger may no longer be at
the handle, unlike a mouse pointer, so menu placement must be optimised for hand
reach; marking menus' normal mode is described as working well for touch
[[2016-05-08_expandable-menus]]. Split buttons, which put two functions in one
control (label navigates, arrow opens a submenu), work on desktop with hover but
fail on mobile: the pattern is rare on the web so users have no mental model for
it, the two touch targets sit too close together for the fat-finger problem, and
because users are imprecise, the same apparent tap sometimes navigates and
sometimes expands, which reads as buggy and erratic
[[2017-06-25_split-buttons-navigation]]. The recommended replacement is to let the
menu expand on tap and include a link to the category landing page inside the
expanded menu, labelled something like "All Sports" or "View All"; the alternative
two-tap interaction is noted as having weak discoverability
[[2017-06-25_split-buttons-navigation]].

For sub-navigation, four patterns are compared against three goals, minimising
interaction cost (few taps, no page loads), supporting typical paths, and making
the navigation UI itself discoverable [[2017-07-16_mobile-subnavigation]].
Accordions inside the main menu give low interaction cost and support all paths
without page loads. Sequential menus, which replace the view at each level, are
space-efficient but disorient users with low spatial ability and lead them to hit
the phone's or browser's Back button instead of the menu's Back link, closing the
menu and navigating away. Section menus, shown on category landing pages, suit
users who stay within one section but do not support jumping between sections.
Category landing pages force a page load on every branch switch. The decision rule
given is by subcategory count: under 6, accordions; 6 to 15, section menus; over
15, category landing pages [[2017-07-16_mobile-subnavigation]]. The underlying
constraint is that a desktop mega menu comfortably showing 30 or more
subcategories will not fit on one mobile screen
[[2017-07-16_mobile-subnavigation]].

## Sources (8)

- [[2016-05-08_expandable-menus]] — The article surveys expandable menu types and their design tradeoffs in terms of movement time, discoverability, and user familiarity.
- [[2017-03-26_mega-menus-work-well]] — Details specific implementation considerations including hover timing, grouping strategy, label clarity, and interaction simplicity specific to mega menu components.
- [[2017-06-11_drop-down-menus]] — guidance on when to use dropdowns for navigation, how to label them, and how to balance desktop hover behavior with mobile needs.
- [[2017-06-25_split-buttons-navigation]] — guidance on multi-device navigation patterns, showing why split buttons fail on mobile and what patterns work better.
- [[2017-07-16_mobile-subnavigation]] — implementation patterns for subnavigation including accordions, sequential menus, section menus, and landing pages, with interaction cost analysis.
- [[2019-06-23_steering-law]] — hierarchical menus create steering-law challenges; modern alternatives like mega menus or flat structures reduce navigation time and errors by avoiding narrow tunnels.
- [[2022-07-31_fitts-law]] — Fitts's Law informs menu structure decisions, with rectangular menus superior to linear ones in average distance to items, and edge placement optimizing reach.
- [[2024-06-07_menu-design]] — specific implementation guidance for navigation menus including visibility, placement, labeling, and interaction patterns.
