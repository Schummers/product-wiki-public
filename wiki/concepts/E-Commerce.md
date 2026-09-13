---
type: concept
name: E-Commerce
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Ecommerce"
  - "Comparison Tables"
  - "E-Commerce Design"
  - "E-Commerce UX"
  - "E-commerce"
  - "E-commerce Design"
  - "E-commerce UX"
  - "Payment Systems"
---

# E-Commerce

## Definition

E-commerce is the design discipline of online retail: the pages, components and
flows through which people find products, evaluate them, decide, pay, and are
kept informed afterwards. The sources treat it as a specialised practice with
its own recurring surfaces — homepages, category and product-listing pages,
filters and search, product detail pages, comparison tables, carts and
wishlists, payment screens, transactional messages and customer-service pages —
each with documented failure modes drawn from usability testing rather than
from theory [[2018-08-12_ecommerce-homepages-listing-pages]]
[[2018-06-17_cart-feedback]] [[2024-02-09_comparison-tables]].

Two shifts run through the corpus. First, online shopping is no longer a
separate channel: customers move between digital and physical retail during a
single journey, showrooming and webrooming as convenience dictates, so the
design problem includes the transitions between channels
[[2018-10-28_changing-shopper-behaviors]] [[2018-10-07_store-finders-and-locators]].
Second, the discipline's assumptions are not universal: payment methods,
device constraints, sizing conventions, notification channels and even the
format of the sales pitch differ by market, and several sources are explicitly
case studies of what works outside the Western desktop default
[[2016-09-04_mobile-behavior-india]] [[2021-02-28_livestream-ecommerce-china]]
[[2022-04-24_sizes-measurements-ecommerce]] [[2022-11-06_transactional-notifications]].
Across all of them the recurring currency is confidence: users buy when the
interface has answered their questions and confirmed what just happened, and
hesitate when it has not [[2017-06-18_ux-design-ecommerce]]
[[2022-03-20_facial-recognition-payment]].

## Practice

### Homepages, categories and listing pages

The homepage should state plainly what the site sells and how it differs from
competitors; the comparison drawn is a shop window, where cramming in more
items lowers perceived quality [[2018-08-12_ecommerce-homepages-listing-pages]].
Category labels must make sense both on their own and against their siblings,
and polyhierarchy (letting an item sit under several parents) improves
findability. Category and listing pages can be merged, with subcategories
highlighted above the product grid to encourage browsing without choice
overload. Listings themselves should carry enough differentiating information —
concise name, large identifying photo, available colours and styles, price, and
optionally ratings, availability and quick view — that a decision is possible
without opening every product page; this matters most on mobile, where every
click costs [[2018-08-12_ecommerce-homepages-listing-pages]].

For long result sets, traditional numbered pagination fits mega-retailers with
huge inventories, while small and medium catalogues do better with infinite
loading or a Show More button, both of which lower interaction cost
[[2022-03-06_alternatives-pagination-listing-pages]]. Infinite loading works
under roughly 40 products per page, with good filters and fast loading, but it
pushes the footer out of reach, so return policies and shipping information
become unreachable; Show More restores footer access between batches and gives
users on limited data plans a choice about loading more. Either way, show the
total item count and how much has been loaded, and save scroll position so that
pogo-sticking back from a product page does not lose the user's place
[[2022-03-06_alternatives-pagination-listing-pages]].

Products that differ only by an attribute belong under one listing with
selectable colour, size or pattern; fundamentally different products deserve
separate listings [[2022-05-08_products-with-multiple-variants]]. Getting this
wrong hurts in both directions: representing distinct products as variants
forces complex comparison inside a single page, while splitting variants across
pages makes users scroll past every version of everything and miss variations
entirely. When variants are split, the listing page must signal them with
salient swatches or thumbnails rather than a small "+MORE" link
[[2022-05-08_products-with-multiple-variants]].

### Filtering and search

Filter implementation should follow user intent: exploratory users, still
learning the search space, benefit from interactive filters that refresh after
each selection, while goal-directed users with several criteria in mind prefer
batch filters behind an Apply button [[2016-02-07_applying-filters]]. Systems
can infer which mode a user is in from hover, keyboard focus or inactivity
timeouts. Speed is a secondary factor: under one second, interactive filtering
is acceptable even for goal-directed users; slower sites should default to
batch. While results update, dim the results area and show progress rather than
letting content flicker, and avoid jumping back to the top of the page while
the user is still working the filters. Facet counts with continuous feedback
keep users out of dead-end zero-result combinations
[[2016-02-07_applying-filters]].

Site search rewards simplicity. Plain text autocomplete suggestions are heavily
used and should be kept and optimised; enriched suggestions (featured items,
trending products, recently viewed, category links with imagery) were used only
7 times out of 60 encounters in testing
[[2022-08-21_enriched-site-search-suggestions]]. The reasons are that searchers
are goal-focused and using search precisely to bypass browsing, that image-based
enrichment loads too slowly to be read before the query is submitted, that
banner blindness makes users fixate on the search box and miss graphical
results even when they match exactly, and that unlabelled suggestions read as
ads or upsell. If enriched content is kept, give each content type a dedicated,
stable place rather than shifting categories around
[[2022-08-21_enriched-site-search-suggestions]]. There is a tension worth
noting here: the same enrichment that backfires for quick-purchase shoppers is,
in livestream commerce, exactly the sort of engagement mechanic that drives
sales — the difference the sources point to is the user's mindset, not the
feature [[2022-08-21_enriched-site-search-suggestions]]
[[2021-02-28_livestream-ecommerce-china]].

### Product information and buying confidence

For high-involvement purchases, decompose the decision: sequential steps each
focused on a single attribute (style, then fabric, then colour) beat presenting
every option at once [[2017-06-18_ux-design-ecommerce]]. Explain
domain-specific vocabulary with illustrations rather than jargon, caption every
image with the exact configuration it shows, list all measurable dimensions
with labels and explanations, show the product in real customers' rooms so
scale and context are legible, and offer free physical samples so tactile
qualities can be judged without committing. The underlying method is to find
out which questions people need answered before they are comfortable buying,
and answer them in advance [[2017-06-18_ux-design-ecommerce]]. Comprehensive
online product information — high-quality and close-up photography, detailed
descriptions, robust reviews — also reduces the need to visit a store at all
[[2018-10-28_changing-shopper-behaviors]].

Sizing is a distinct pain point, especially for international shoppers who may
not be able to return an item; good size guides cut both return rates and
support tickets [[2022-04-24_sizes-measurements-ecommerce]]. Localised sites
should show local sizes prominently next to original sizes; international sites
need comprehensive conversion charts, optionally filterable by country. Because
brands vary, a single chart is insufficient: provide brand-specific guides,
body dimensions (bust, waist, hip) so users can match their actual body rather
than an abstract label, and product measurements for every size — with an
explanation of how those measurements were taken. On mobile, place the original
size and the local equivalent in adjacent columns to avoid endless scrolling
[[2022-04-24_sizes-measurements-ecommerce]].

Luxury e-commerce concentrates its difficulty in the Consider phase, the
longest of the four phases (Discover, Consider, Purchase, Use) and the one
where digital experiences most often fail through poor organisation, too few
photos, missing details and bad recommendations — which damages brand
perception [[2022-06-12_luxury-user-groups-journeys]]. Luxury shoppers segment
into professional stylists buying for clients, window shoppers who aspire
without buying, occasional splurgers treating purchases as investments, and
habitual big spenders who research brand history and leadership as a hobby and
value a personal relationship with a sales representative. Return anxiety is
acute given the sums involved, and preferences diverge within the audience:
occasional splurgers want visible logos, big spenders prefer discreet branding
[[2022-06-12_luxury-user-groups-journeys]].

### Comparison and deferred decisions

Comparison tables support compensatory decisions — weighing several criteria
across a small set of alternatives, typically 3 to 7, and best kept to 5 or
fewer [[2024-02-09_comparison-tables]]. Static tables suit small selections and
give tight control; dynamic tables, where users pick what to compare, scale to
larger catalogues. The most common failure is not visual but editorial:
incomplete or inconsistent metadata across rows makes a table useless however
well it is designed. Keep cell text short and scannable, use symbols and
colour-coding, include only attributes users actually care about, and define
unfamiliar terms in context or via tooltips [[2024-02-09_comparison-tables]].

Eyetracking shows users scan such tables in a lawn mower pattern — left to
right, drop down, right to left, row by row — after an initial appraisal of the
column and row labels [[2020-12-13_lawn-mower-pattern]]. Design should protect
that pattern: sticky or fixed headers so column identity is never lost (a point
both comparison-table sources make [[2024-02-09_comparison-tables]]), narrower
navigation, self-explanatory cells, grouped yes/no features, minimal
repetition, plain terminology, and no placeholder content. Very long tables
break the pattern by forcing users back to the top to recheck which product is
in which column, and unexplained jargon produces dense fixation clusters where
scanning stalls [[2020-12-13_lawn-mower-pattern]].

Saving for later is a parallel decision surface. Carts are used as external
memory: a comparison table, a reference, a scrapbook, held across sessions
rather than a pure purchase vehicle [[2018-11-04_wishlist-or-cart]]. Users
treat a cart addition as "might want" and a list addition as "definitely want",
so they add to the cart even when the intent is long-term saving. The label
"wishlist" carries gift-sharing and greedy connotations that discourage
personal use; "Favorites" or "My List" carry fewer. Save-for-later must be
visible and clearly labelled rather than hidden behind swipes or dropdowns, and
must never require registration, which derails checkout. Preserving items this
way converts what would be abandonment into a later purchase, because the work
of finding the products is not lost [[2018-11-04_wishlist-or-cart]]. Note that
users frequently fail to notice they have saved duplicate variants of the same
product, which complicates the later comparison
[[2022-05-08_products-with-multiple-variants]].

### Cart feedback, payment and trust

Adding to cart is a fundamental interaction that many sites confirm poorly,
leaving users unsure whether the action registered and whether the right
configuration was added [[2018-06-17_cart-feedback]]. Use a noticeable cart
badge with item count and running subtotal; include product image, name, price,
quantity and chosen options in the confirmation so the user can verify; and
change the button state when an item is already in the cart, offering "Add
Another" rather than silently duplicating. Avoid transient popovers that fade
before they can be read — reviewing them becomes a race against time — and
prefer persistent overlays, banners or interstitial pages. Interstitials suit
sites where sessions contain few purchases; persistent overlays or banners suit
sites where users add many items while browsing [[2018-06-17_cart-feedback]].

Payment is not a solved commodity. Alternatives to card payment — mobile
wallets, SMS money transfer, QR-code payment — enable transactions for the
unbanked and matter in markets with low card penetration; one-time passwords
sent by SMS reduce both memory load and mobile typing effort compared with
passwords, and auto-filling the code from the message improves the experience
further [[2016-09-04_mobile-behavior-india]]. Facial-recognition payment in
China is the corpus's worked example of speed failing to buy adoption: 4 of 5
participants preferred QR-code scanning after trying it, because consent had
been buried in a user agreement they never saw, the mechanism was never
explained (users assumed registration happened at first use and feared anyone
with their phone number could register and take their money), the payment
account was forced rather than chosen, and no confirmation password was
required [[2020-05-10_face-recognition-pay]]. A follow-up study three years
later found the same problems persisting despite technical progress and mass
adoption: users still held an incorrect model of how recognition works,
secondary authentication appeared inconsistently so users could not tell
whether payment had gone through, and confirmation screens omitted the amount,
the account charged and the maximum payment limit
[[2022-03-20_facial-recognition-payment]]. The shared lesson is that a false
mental model survives technical improvement unless the design actively corrects
it: explain the technology briefly at the point of use, ask for consent
explicitly, allow account choice, keep interaction behaviour consistent or
explain the variance, and show the transaction's details on confirmation
[[2020-05-10_face-recognition-pay]] [[2022-03-20_facial-recognition-payment]].

### After the order: notifications, service and disruption

Transactional messages — order confirmations, delivery notices, status changes,
service-term updates — are distinct from marketing messages and are judged by
whether they carry the details the customer needs
[[2022-11-06_transactional-notifications]]. They need clear subject lines and
concise content; push notifications, constrained to roughly 50–240 characters
with little formatting, demand frontloading key information because users scan
only the first few words. Reserve notification channels for genuinely
time-sensitive content, since excess pushes users to disable communication
altogether. SMS is the durable channel, right for pickup codes, delivery
details, order changes and confirmations the user may need to retrieve later;
push suits nonurgent reminders such as an abandoned cart. Channel preference is
cultural — SMS historically favoured in China, email in the West — and users
should be able to opt out of specific channels rather than all of them
[[2022-11-06_transactional-notifications]].

Customer-service content should follow a hub-and-spoke structure: one main
Customer Service hub as a catch-all, with FAQ and Contact Us as the only two
additional hubs, since further hubs increase confusion about which to visit
[[2018-07-29_customer-service-model]]. The labels "Customer Service" or
"Customer Assistance" tested well, while "Help" or "Help Center" led users to
expect assistance with the website itself rather than service policies. All
hubs should crosslink, and granular pages such as Returns and Shipping should
link back to the hubs from body content, not only through global navigation.
The model came out of e-commerce research but applies to any site offering
service information, and standardising it builds trust in the company
[[2018-07-29_customer-service-model]].

When operations change — the corpus's case is the COVID-19 pandemic's shipping
delays, stock shortages and purchase limits — communicate early and repeatedly
along the whole journey [[2020-06-14_emergency-covid]]. Announce delays on the
homepage and product pages before users invest time, using high-contrast
banners with bold headlines and iconography so they are not lost to banner
blindness or mistaken for ads, then repeat the message at cart and checkout as
a safety net for task-focused users who missed it. When only some categories
are affected, layer sitewide messaging with targeted banners on the affected
categories and products. Unfamiliar new services such as curbside pickup need
explanation on the homepage and at checkout plus step-by-step instructions by
email and in-app before the physical interaction. Automated transactional
emails must be updated to reflect the new reality, since they are often the
reference customers keep [[2020-06-14_emergency-covid]].

### Crossing into physical retail

Customers do not distinguish online from in-store shopping; they move between
channels by convenience, showrooming to touch products before buying online and
webrooming to research before visiting a store
[[2018-10-28_changing-shopper-behaviors]]. Every transition is an opportunity
for a lost sale, so the design goal is to remove unnecessary transitions and
smooth the unavoidable ones — confirmation emails with directions, parking
information and what to bring. Physical stores keep their value as places to
try and touch, but should be integrated with digital comparison and extended
selection [[2018-10-28_changing-shopper-behaviors]].

Store locators are the connective tissue. Across four rounds of testing over 18
years, success rates rose from 63% to 97%, yet 40% of users still met
difficulty, so functional is not the same as easy
[[2018-10-07_store-finders-and-locators]]. Three steps must all work: finding
the locator link, using it to find the right location, and getting directions
from there. Around 80% of users go straight to a search engine or mapping app
rather than the company site, so linking out to familiar platforms such as
Google Maps for turn-by-turn directions beats building a proprietary map.
Geolocation should be offered through a discoverable button or link rather than
hidden behind a permission dialog. The remaining problem is calibration:
locators are either overloaded with features or too simple to filter results by
what the user actually needs [[2018-10-07_store-finders-and-locators]].

### Formats and constraints beyond the Western default

Livestream ecommerce — retailers, influencers or celebrities selling through
live video with real-time audience interaction — has surged in China to an
estimated 60 billion dollars annually and is spreading through TikTok and
Amazon [[2021-02-28_livestream-ecommerce-china]]. It runs on existing social
and commerce platforms rather than proprietary ones, is mobile-first, and
mimics in-store shopping by letting a host demonstrate products from multiple
angles or show an item on a specific model on request. It is social (live
questions, visible comments), gamified (loyalty levels, tiered coupons rewarding
participation, time-limited deals), and partly asynchronous through replay of
earlier product showcases [[2021-02-28_livestream-ecommerce-china]].

Constraint-driven behaviour also reshapes commerce design. Mobile-only users in
India, facing limited storage and expensive data, adopt lightweight browsers,
store apps on SD cards, share files peer-to-peer and prefer a good mobile web
experience over installing an app at all; device sharing makes app-level locks
and login walls desirable rather than friction to be removed
[[2016-09-04_mobile-behavior-india]]. Designing for these users means treating
data cost, storage, authentication method and payment method as variables, not
constants.

## Sources (21)

- [[2016-02-07_applying-filters]] — filter design is central to product discovery and conversion on ecommerce sites.
- [[2016-09-04_mobile-behavior-india]] — Documents alternatives to credit cards (mobile wallets, SMS money transfer, QR-code payments) that enable transactions for the unbanked and serve environments with low credit-card penetration.
- [[2017-06-18_ux-design-ecommerce]] — strategies for high-involvement purchases online, including progressive disclosure, guided workflows, and confidence-building through detailed information.
- [[2018-06-17_cart-feedback]] — The article addresses one of the fundamental e-commerce interactions, showing how poor feedback on cart additions damages user confidence and prevents repeat purchases.
- [[2018-07-29_customer-service-model]] — The hub-and-spoke model was developed from e-commerce research but applies to all websites providing customer service, helping build trust and reduce support burden.
- [[2018-08-12_ecommerce-homepages-listing-pages]] — specialized product design discipline addressing unique challenges of online retail, including homepage clarity, category organization, and shopping workflow efficiency.
- [[2018-10-07_store-finders-and-locators]] — how online shopping increasingly requires integration with physical retail locations and how companies must facilitate transitions between digital and physical channels.
- [[2018-10-28_changing-shopper-behaviors]] — how online shopping has evolved from a separate channel to one component of a larger shopping ecosystem requiring integration with physical retail.
- [[2018-11-04_wishlist-or-cart]] — how shopping workflows must support both immediate and deferred purchasing decisions with appropriate tools and features.
- [[2020-05-10_face-recognition-pay]] — case study of FRP as an alternative payment method and lessons for designing payment interfaces that balance speed with user confidence.
- [[2020-06-14_emergency-covid]] — principles for communicating operational changes across e-commerce touchpoints during supply-chain disruptions.
- [[2020-11-08_augmented-reality-useful]] — online shopping contexts where AR features help users preview items in their spaces or on themselves to reduce purchase uncertainty and return rates.
- [[2020-12-13_lawn-mower-pattern]] — establishes best practices for designing comparison tables that support the lawn mower pattern and reduce cognitive load.
- [[2021-02-28_livestream-ecommerce-china]] — the article analyzes how livestream ecommerce is reshaping online retail and what traditional ecommerce sites can learn from it.
- [[2022-03-06_alternatives-pagination-listing-pages]] — Ecommerce listing-page design should balance user goals (browsing products) with footer access, mobility considerations, and clear navigation; different approaches suit different inventory sizes.
- [[2022-03-20_facial-recognition-payment]] — design considerations for fast payment methods that require users to feel secure and informed about the transaction.
- [[2022-04-24_sizes-measurements-ecommerce]] — addressing specific pain points for online shoppers in selecting correct product sizes.
- [[2022-05-08_products-with-multiple-variants]] — best practices for product presentation that reduce friction in shopping decisions.
- [[2022-06-12_luxury-user-groups-journeys]] — Luxury e-commerce requires special attention to the consideration phase, product information, and brand storytelling to meet shopper expectations shaped by offline luxury retail experiences.
- [[2022-08-21_enriched-site-search-suggestions]] — Shopping search requires fast text suggestions; enriched results intended to increase browsing or upsell often backfire when users are in quick-purchase mode.
- [[2022-11-06_transactional-notifications]] — ecommerce notifications benefit users most when they contain order details, delivery information, and status changes; users appreciate options to opt out from specific channels.
- [[2024-02-09_comparison-tables]] — A specialized component for supporting side-by-side evaluation of multiple products or services, with a primary use case in helping users choose among product variants.
