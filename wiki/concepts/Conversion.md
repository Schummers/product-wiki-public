---
type: concept
name: Conversion
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Conversion Optimization"
  - "Conversion Rate"
  - "Taux de conversion"
---

# Conversion

## Definition

Conversion is the share of visitors who complete a desired action, typically a
purchase [[2017-12-03_m-commerce-terrible-ux]]. Framed from the user's side, it
is the transformation of a user need into a validated action, and it improves as
the friction standing between the two is reduced
[[2025-05-27_379_EAS_Optimiser_l_UX_des_forms_pour_augmenter_la_conversion_-_Guide]].
The sources treat it as a design outcome rather than a marketing lever: form
length, page speed, mobile design quality and onboarding friction all move the
number, and the same design decisions determine both conversion and the
experience that produced it.

The sources also caution against reading conversion too narrowly. Meaningful
conversions happen deeper in the journey — purchases, registrations, repeat
visits — and optimising a shallow proxy such as bounce rate can degrade the
experience that would have produced the real conversion later
[[2016-11-13_return-visits-not-bounce]]. In a product-led growth model,
conversion is one link in a chain running from acquisition through activation,
retention and monetisation, alongside time to value and churn
[[2023-05-21_product-led-growth-ux]]; the paywall case makes the same point by
pairing conversion rate with churn as a control metric
[[2024-06-11_332_Designer_et_AB_tester_un_paywall]].

## Practice

### Forms: remove, automate, simplify

Forms are where the sources are most concrete. Forms that follow basic usability
guidelines are submitted correctly on the first try 78% of the time, against 42%
for forms that violate them [[2016-05-01_web-form-design]].

- **Cut fields.** Every field removed increases the conversion rate — the
  business case is that simple [[2016-05-01_web-form-design]]. The EAS framework
  (Éliminer, Automatiser, Simplifier) makes the same first step a test: is this
  information worth the conversion it may cost, do we already have it, could we
  ask for it later
  [[2025-05-27_379_EAS_Optimiser_l_UX_des_forms_pour_augmenter_la_conversion_-_Guide]].
- **Pre-fill what you cannot cut.** Sensible defaults, contextual inference and
  third-party APIs remove the typing rather than the field
  [[2025-05-27_379_EAS_Optimiser_l_UX_des_forms_pour_augmenter_la_conversion_-_Guide]].
- **Smooth the remaining interaction.** Correct mobile keyboard types, input
  suggestions, and tolerance for natural-language entry
  [[2025-05-27_379_EAS_Optimiser_l_UX_des_forms_pour_augmenter_la_conversion_-_Guide]].
- **Structural guidelines.** Single-column layout to keep vertical momentum;
  labels above or beside fields with related fields grouped; logical field
  sequencing tested with the Tab key; field width matching the expected input;
  persistent labels instead of placeholder text; optional fields clearly marked;
  formatting requirements stated upfront rather than revealed in errors; no Reset
  or Clear buttons; visible, specific error messages that preserve what the user
  already typed [[2016-05-01_web-form-design]].
- **Friction is a cost the user pays.** The more information you request, the more
  time and energy the user spends reaching their own goal, and the worse the
  experience becomes
  [[2025-05-27_379_EAS_Optimiser_l_UX_des_forms_pour_augmenter_la_conversion_-_Guide]].

### Speed

- Decades of data link load time to conversion: half-second delays reduced
  conversions (Google and Bing, 2009), cutting two seconds raised conversions 15%
  (Mozilla, 2010), and a three-second mobile load produced 53% abandonment
  (Google, 2016) [[2020-05-17_the-need-for-speed]].
- A single second of delay is enough to interrupt conscious thought and turn
  direct control into waiting [[2020-05-17_the-need-for-speed]].
- Being faster than average is not a goal when the average site is frustratingly
  slow; sub-second load times are the target, and every incremental second gained
  pays off — the slower the site, the more there is to gain
  [[2020-05-17_the-need-for-speed]].
- The gap persists structurally: desktop load times have been flat around six
  seconds for a decade while mobile has doubled to twenty, because faster networks
  are consumed by heavier pages [[2020-05-17_the-need-for-speed]].

### Mobile

- Desktop visitors generated 111% more revenue per visit than mobile visitors in
  2017, down from 288% in 2014, but still a large gap while mobile carried 40% of
  traffic [[2017-12-03_m-commerce-terrible-ux]].
- The gap is a design problem, not a demographic one: it reflects mobile
  experiences that ignore mobile-specific guidelines or merely scale a desktop
  design down [[2017-12-03_m-commerce-terrible-ux]].
- Mobile is inherently a weaker UI platform for screen size and text input, which
  raises rather than lowers the cost of ignoring the guidelines
  [[2017-12-03_m-commerce-terrible-ux]].
- Tablets convert nearly as well as desktop (ratio 1.18 against desktop's 1.27),
  so optimisation attention belongs on phones
  [[2017-12-03_m-commerce-terrible-ux]].
- With only three products visible on a phone screen against six on desktop,
  product prioritisation and thumbnail-optimised photos matter far more
  [[2017-12-03_m-commerce-terrible-ux]].

### Paywalls and the moment of payment

- A paywall is the screen separating the free and paid worlds, stating the offer,
  the benefits and the price [[2024-06-11_332_Designer_et_AB_tester_un_paywall]].
- Conversion rate is the primary metric, but churn must be watched alongside it to
  confirm the converted customers are viable in the long run
  [[2024-06-11_332_Designer_et_AB_tester_un_paywall]].
- The design must fit the context: type of offer (monthly, lifetime), any
  promotion, and the entry point the user arrived from — each situation
  prioritises different arguments
  [[2024-06-11_332_Designer_et_AB_tester_un_paywall]].
- Strip distractions such as navigation menus; a clear space lowers mental stress
  and lets the user focus on the purchase
  [[2024-06-11_332_Designer_et_AB_tester_un_paywall]].
- There is no universal answer on length. A/B testing is the way to find the right
  form: on the Habitude app, a long paywall raised conversion by 50%
  [[2024-06-11_332_Designer_et_AB_tester_un_paywall]].

### Exit moments

- Exit-intent popups fire as the cursor approaches the page boundary, so unlike
  ordinary popups they do not interrupt a task in progress — which makes them
  lower-risk [[2019-10-13_exit-intent-good-ux]].
- They convert when they carry genuine user value: an instant discount code
  (people abandon carts to hunt for codes anyway), confirming intent before an
  accidental exit from checkout, offering to email a cart or save progress on a
  long task, support contact, or surfacing price-match and money-back guarantees
  users never discovered [[2019-10-13_exit-intent-good-ux]].
- The source is explicit that most exit-intent popups do the opposite — asking for
  an email and using manipulative wording to shame people into acting — and that
  the aim should be raising the popup's perceived value to the user rather than
  extracting something [[2019-10-13_exit-intent-good-ux]].

### Funnel design in product-led growth

- In product-led growth, customers discover value by using the product rather than
  through a sales representative, so the first experience decides whether they
  convert before moving to a competitor [[2023-05-21_product-led-growth-ux]].
- Reduce friction at acquisition: minimise onboarding tutorials and login barriers
  so the benefit is grasped before payment is asked for
  [[2023-05-21_product-led-growth-ux]].
- Value delivered is not value perceived: research should test both whether the
  product delivers value and whether the design communicates it
  [[2023-05-21_product-led-growth-ux]].
- Connect UX work to the product-led metric set — time to value, conversion rate,
  retention, churn, customer-acquisition cost — and monitor usage patterns to spot
  at-risk segments and promote the features engaged users adopt early
  [[2023-05-21_product-led-growth-ux]].
- Apply the Pareto principle to converted customers: invest in the top 20% who
  generate 80% of revenue [[2023-05-21_product-led-growth-ux]].

### Do not optimise the wrong metric

- Bounce rate does not separate a successful single-page visit from a failure: a
  user who found the exact answer they needed on one page had a good experience
  [[2016-11-13_return-visits-not-bounce]].
- Chasing the second click produces artificial friction — splitting articles
  across pages, hiding essential details behind "learn more", withholding prices —
  which degrades the experience and can cost the return visit that would have
  converted [[2016-11-13_return-visits-not-bounce]].
- Track return frequency and recency instead, and use bounce rate selectively:
  comparing similar page types to find outliers is legitimate, optimising it
  site-wide is not [[2016-11-13_return-visits-not-bounce]].
- Revenue per visit is a more meaningful measure than conversion rate alone,
  because it accounts for both how often people buy and how much they spend
  [[2017-12-03_m-commerce-terrible-ux]].

## Sources (9)

- [[2016-05-01_web-form-design]] — Form design directly impacts conversion rates; compliant forms achieve significantly higher completion and one-try success rates.
- [[2016-11-13_return-visits-not-bounce]] — Meaningful conversions occur deeper in the user journey (purchases, registrations, repeat visits) and are more directly linked to business goals than shallow metrics like bounce rate; design decisions should optimize for these end-goals rather than single-visit metrics.
- [[2017-12-03_m-commerce-terrible-ux]] — The percentage of visitors who complete a desired action (purchase); mobile conversion rates are substantially lower than desktop, indicating poor mobile user experience rather than user demographics.
- [[2019-10-13_exit-intent-good-ux]] — Exit-intent popups can drive conversions through discounts, support offers, or progress-saving; the key is providing user value rather than pure persuasion.
- [[2020-05-17_the-need-for-speed]] — details documented correlation between page load time and conversion, with data from multiple companies showing 50% drops in conversion for longer load times.
- [[2023-05-21_product-led-growth-ux]] — Designing experiences that move users through the funnel from acquisition through activation, retention, and monetization.
- [[2024-06-11_332_Designer_et_AB_tester_un_paywall]]
- [[2025-05-27_379_EAS_Optimiser_l_UX_des_forms_pour_augmenter_la_conversion_-_Guide]]
- [[2013-08-01_just-enough-research_10-chapter-9-quantitative-research]] — any measurable user action aligned with site goals; conversion rate is the percentage of users taking that action; different types of conversion (newsletter sign-up, purchase, membership) may have different importance to business success; is the primary metric optimized in split testing.
