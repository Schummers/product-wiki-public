---
type: concept
name: Responsive Design
created: 2026-07-31
updated: 2026-09-10
status: developed
---

# Responsive Design

## Definition

Responsive design serves the same content from a single codebase and dynamically adjusts the layout to the screen it is displayed on, so that one site works across smartphones, tablets, and desktops [[2016-02-14_mobile-vs-responsive]]. It is one of four possible approaches to serving mobile users, alongside mobile-dedicated sites on a separate URL, adaptive design where the server detects device capabilities and sends only what the device can handle, and simply serving the desktop site, which is not recommended [[2016-02-14_mobile-vs-responsive]]. Its mechanism is the breakpoint: a specific screen size at which the design switches to a different layout, in practice a range of minimum and maximum widths for which one layout applies [[2024-04-05_breakpoints-in-responsive-design]]. By 2023 the approach had become the norm — the separate "full site" is largely obsolete, and most sites now offer all features and content on both mobile and desktop [[2023-01-01_state-mobile-ux]].

The consistent warning across these sources is that responsive is a delivery technique, not a design decision. Content reflow across screen sizes does not mean the same interactions and layouts work equally well everywhere [[2016-07-24_mobile-first-not-mobile-only]]; simply rewrapping desktop content on small screens does not produce a usable mobile interface [[2016-02-14_mobile-vs-responsive]]; and naively scaling content is itself a cause of poor mobile ecommerce performance [[2017-12-03_m-commerce-terrible-ux]]. What responsive design demands is deliberate adaptation at each size, not uniform scaling.

## Practice

### Choosing responsive over the alternatives

The trade-offs between the four approaches [[2016-02-14_mobile-vs-responsive]]:

- **Responsive** — content parity, the same content and mostly the same functionality on every screen size, from a single codebase, which lowers maintenance burden. The cost is speed and price: because the same content is delivered to every device, responsive pages often load more slowly than an optimized mobile-dedicated version, and responsive sites tend to be more expensive to develop.
- **Mobile-dedicated** — often faster and simpler, but requires separate maintenance. It trades breadth for depth by omitting complex features and content, and that simplification can actually improve usability for mobile tasks.
- **Adaptive** — solves the performance problem through server-side content negotiation, sending lightweight versions to less capable devices while keeping some content parity.
- **Desktop site on mobile** — not recommended.

On user preference, the source is explicit that stated preference and behaviour diverge: despite saying they prefer the full desktop site, people are more efficient and more successful on mobile-optimized experiences, so watch what users do rather than what they say [[2016-02-14_mobile-vs-responsive]].

### Breakpoints

A common set is four sizes, named by T-shirt convention: extra-small for mobile up to about 500px, small for tablet from 500 to 1200px, medium for laptop from 1200 to 1400px, and large for monitors above 1400px [[2024-04-05_breakpoints-in-responsive-design]]. Clear naming of this kind lets a team adjust the actual pixel values later as the audience's device usage evolves, and breakpoints should be defined from that real device-usage distribution rather than from arbitrary standards [[2024-04-05_breakpoints-in-responsive-design]].

The typical adjustments at a breakpoint are a change of navigation (hamburger menus at smaller sizes), collapsing columns, and a change in the number of visible content elements; grid column counts (4, 8, 12) vary accordingly [[2024-04-05_breakpoints-in-responsive-design]]. Designers have to think through how content flows at each size and decide what information is crucial there, then communicate those layout changes to developers through specifications and testing — and involve the development team in defining the breakpoints, since that team sets them up. Regular column stacking sometimes needs an exception, for instance collapsing preceding content under accordions to keep a call to action discoverable [[2024-04-05_breakpoints-in-responsive-design]].

Foldable devices stretch this model. They have unconventional screen sizes, so apps should be tested on popular foldable models and breakpoints adjusted if the app struggles; designing for them means thinking beyond traditional breakpoints, considering new interaction patterns, screen-switching behaviour, and multitasking [[2025-01-10_foldable-smartphones]]. Because a user may open the same app at several screen sizes on one device, consistency between folded and unfolded states matters: inconsistency forces relearning [[2025-01-10_foldable-smartphones]].

### Porting is not adapting

Mobile-first is not mobile-only. Starting from a mobile-optimized design is a sound strategy, but the design should not be ported unchanged to desktop, where larger screens and different capabilities allow better solutions [[2016-07-24_mobile-first-not-mobile-only]]. Quantitative testing of navigation on six sites found lower navigation use on desktop than on mobile — not because desktop users needed navigation less, but because the desktop interfaces were mobile designs on a bigger screen [[2016-07-24_mobile-first-not-mobile-only]]. Patterns that fail when ported to desktop include hamburger menus, navigation repeated at the bottom, sticky navigation, search icons instead of search boxes, and navigation in the top-right or other nonstandard positions [[2016-07-24_mobile-first-not-mobile-only]]. The article frames this as a recurring historical failure — DOS to Windows to Mac, website to mobile, and now mobile to desktop — and concludes that designing once to use twice risks a subpar experience on one platform and possibly both [[2016-07-24_mobile-first-not-mobile-only]].

The commercial consequence appears in ecommerce data: in 2017 each desktop visitor was worth 111% more than a mobile visitor, down from 288% in 2014 but still a large gap, and the gap is attributed to design rather than to who mobile users are [[2017-12-03_m-commerce-terrible-ux]]. Mobile is inherently a weaker UI platform in screen size and text input, which makes following mobile-specific guidelines more critical, not less; some sites merely scale desktop designs down [[2017-12-03_m-commerce-terrible-ux]]. Tablets, by contrast, convert almost as well as desktop (1.18 against 1.27), so tablet usability needs less attention than phone optimization [[2017-12-03_m-commerce-terrible-ux]]. With a mobile listing showing three products where desktop shows six, getting product prioritization right and optimizing photos for small thumbnails matters far more on the small screen [[2017-12-03_m-commerce-terrible-ux]].

### Images across screen sizes

Images designed for mobile often fail when scaled up. Three failure modes [[2017-07-23_small-pictures-big-screens]]: disproportionate scaling, where the image becomes too large relative to surrounding content, creating low information density and forcing users to scroll past it; cropping, where vertical constraints cut off skylines, faces, or the relationship between subjects and make the photo ambiguous or change its message; and repositioning, where a scaled image's relationship to nearby text shifts so it overlaps copy, obscures its subject, or communicates something unintended. Low-resolution images become pixelated at larger sizes, and in general any weakness in an image becomes more apparent the larger it gets.

Four remedies [[2017-07-23_small-pictures-big-screens]]: combine scaling and cropping rather than doing either alone — scale up to a point, then crop carefully to preserve meaning; choose images that tolerate multiple aspect ratios, typically ones with a central subject that survives edge cropping; set a maximum dimension beyond which the image would lose meaning and fill the rest of the screen with white space or complementary content; or swap in a different image at a different screen size. The source also notes the process cause: these problems get overlooked when designers and developers only ever view their work on a single monitor or only at their target breakpoints.

### Tables

Adapting a data table for small screens takes different techniques than scaling. Start by making the table usable on a large screen, keeping only meaningful attributes and consistent content — the mobile constraint often reveals improvements that help everyone [[2017-09-17_mobile-tables]]. Then, on mobile [[2017-09-17_mobile-tables]]:

- Columns must be legible without zooming; how many fit depends on content, with wordy comparison tables sometimes managing only two columns while numeric data fits more.
- Stick column headers and row labels in place, since a table taller than one screen otherwise leaves users without context for what each column is.
- Signal that horizontal scrolling is available, using cut-off elements or arrows at the edge; dots draw attention less effectively than a visual cut or arrow.
- Give users control over what they see: filters to narrow the data before display, toggles for relevant columns, accordions to expand categories on demand.

Legibility without zooming and clear context are treated as non-negotiable [[2017-09-17_mobile-tables]].

### Navigation and long pages

Left-side vertical navigation is presented as a pattern that adapts well: it translates to mobile with minimal change, whereas horizontal navigation typically collapses into a hamburger menu, and the shared visual design across devices increases consistency [[2021-05-16_vertical-nav]]. It also scales to broad information architectures without forcing short labels or generic groupings, and benefits from attention leaning left — users look at the left half of the screen 80% of the time — with vertical lists giving more information per eye fixation than horizontal menus [[2021-05-16_vertical-nav]]. Its trade-off is directly a responsive concern: vertical navigation consumes screen space and lowers the content-to-chrome ratio, which needs care on smaller displays [[2021-05-16_vertical-nav]]. Its guidelines: place it on the left with high visual contrast, do not duplicate the same menu horizontally and vertically, keep visible text labels rather than icon-only designs, and put important items above the fold [[2021-05-16_vertical-nav]].

Responsive layouts and infinite scrolling have made pages long, which is why back-to-top buttons became common — but they are only justified when a page exceeds four screen heights; on shorter pages they add clutter [[2017-08-27_back-to-top]]. When used: place the button in the lower right, label it "Back to Top" rather than relying on an arrow icon whose meaning is too obscure, use one sticky button instead of repeated links throughout the page, and delay its appearance until the user has scrolled a certain distance and shown scroll-up behaviour [[2017-08-27_back-to-top]]. Better still, address the underlying need — sticky navigation menus, navigation at the bottom of the page, and search often solve the real problem, since returning to the top is a means to an end [[2017-08-27_back-to-top]].

### Where the practice stands

Usability testing with 19 US participants across 60 sites and applications found mobile design mature and converged: hamburger menus and navigation bars are standard, iOS and Android have grown more similar, and content parity through responsive design or a dedicated mobile site is the norm [[2023-01-01_state-mobile-ux]]. Remaining problems are not layout reflow but decorative images and graphics that still lengthen pages when mobile users only scroll if the content looks promising, and overlays and in-app browsers that cause accidental dismissal, duplicate hamburger menus, and buttons hidden behind browser controls [[2023-01-01_state-mobile-ux]].

## Sources (11)

- [[2016-02-14_mobile-vs-responsive]] — the core topic; responsive techniques and their trade-offs.
- [[2016-07-24_mobile-first-not-mobile-only]] — Responsive design enables content reflow across screen sizes, but does not mean identical interactions and layouts should work equally well everywhere.
- [[2017-07-23_small-pictures-big-screens]] — design practices for content and images that work across multiple screen sizes and orientations, with deliberate adaptation rather than uniform scaling.
- [[2017-08-27_back-to-top]] — long single-column layouts common in responsive design necessitate navigation shortcuts like back-to-top buttons for usability.
- [[2017-09-17_mobile-tables]] — adapting tables from desktop to mobile requires different techniques than simple scaling; sticky elements, user controls, and content prioritization are essential.
- [[2017-12-03_m-commerce-terrible-ux]] — Adapting a design across different screen sizes; naive responsive design (simply scaling content) does not adequately address mobile usability needs and contributes to poor mobile ecommerce performance.
- [[2021-05-16_vertical-nav]] — Vertical navigation adapts naturally to mobile without major redesign, unlike horizontal navigation which typically becomes hamburger menus.
- [[2023-01-01_state-mobile-ux]] — Responsive web design has become standard, eliminating the need for separate mobile and desktop sites; most users no longer need to access full desktop sites on mobile.
- [[2024-04-05_breakpoints-in-responsive-design]] — demonstrates how breakpoints are fundamental to creating adaptive layouts for varying device sizes.
- [[2025-01-10_foldable-smartphones]] — Discusses extending responsive design principles to accommodate the unconventional screen sizes and configurations of foldable devices.
- [[2024-01-23_laws-of-ux_07-5-postels-law]] — design approach using fluid grids, flexible images, and media queries to adapt content across any screen size and context.
