---
type: concept
name: User Retention
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Churn"
  - "Churn Rate"
  - "Customer Loyalty"
  - "Taux de churn"
---

# User Retention

## Definition

User retention is whether people keep using a product over time, and churn is
its inverse — the loss of users or subscribers after they have converted. In
this corpus retention appears mostly as a **control metric**: something you
watch alongside conversion to check that a short-term gain has not been bought
at the cost of the relationship. When designing a paywall, conversion rate is
the primary metric but churn must be monitored in parallel to confirm the
converted customers are viable in the long run
[[2024-06-11_332_Designer_et_AB_tester_un_paywall]]. The same logic closes the
funnel guide: after optimising a funnel, retention is what verifies that forced
engagement has not damaged durable use of the product
[[2026-05-19_414_L_anatomie_d_un_funnel_-_Guide_Growth_&_UX]].

Christian Crumlish adds the measurement definition and reverses the emphasis:
retention is the percentage of users who return after initial use, measured by
cohorts over time, and it is the foundation on which growth compounds rather
than a guardrail on it
[[2022-01-19_product-management-for-ux-people_09-chapter-6-product-analytics-growth-engagement-retention]].

The corpus also treats retention as loyalty in the wider sense — the outcome of
a consistent brand experience [[2016-07-03_brand-experience-ux]], something
measurable (imperfectly) through NPS [[2024-06-21_nps-ux]], addressable in the
moment of departure [[2019-10-13_exit-intent-good-ux]], and explicable through
qualitative research with the people who left
[[2024-11-12_351_Les_cold_calls,_méthode_d_UX_Research_-_Guide_pratique]].

## Practice

### Retention as the counterweight to conversion

Two Parlons Design sources put retention in the same structural position: the
guardrail behind a conversion number.

On paywalls, [[2024-06-11_332_Designer_et_AB_tester_un_paywall]] describes the
screen as the boundary between the free and paid worlds, which must state the
offer, the benefits and the price. Conversion rate is what you optimise, churn
is what you check so the conversions hold. The rest of the guidance in that
source: adapt to context (monthly vs. lifetime offers, promotions, the user's
entry point each demand a different ordering of arguments); strip distractions
such as navigation menus, since a clear space lowers mental stress and helps
the user focus on the purchase; and settle length by experiment rather than by
principle — an A/B test on the Habitude app found a long paywall increased
conversion by 50%, with the source stating there is no universal answer about
ideal length.

On funnels, [[2026-05-19_414_L_anatomie_d_un_funnel_-_Guide_Growth_&_UX]] splits
the funnel into three phases:

1. **The bounce** (first page) — losing 10–30% here is normal, and the cause is
   usually the quality of the entry point (marketing campaign, SEO) rather than
   a UX problem. Fix it upstream by attracting a qualified audience instead of
   over-investing in that first step.
2. **The descent** (intermediate steps) — target 95% conversion at each step.
   Heavy loss here signals a real UX problem: locate the blockers with data
   tracking, then iterate through A/B testing or user tests.
3. **The completion** (the final, most committing step) — the user decides based
   on the overall perceived experience. Test deep conceptual changes and new
   engagement approaches, while taking care not to force the user's hand at the
   expense of long-term retention.

### Retention as the pivot of the growth funnel (book)

[[2022-01-19_product-management-for-ux-people_09-chapter-6-product-analytics-growth-engagement-retention]]
places retention inside Dave McClure's AARRR sequence (Acquisition, Activation,
Retention, Referral, Revenue, sometimes with Awareness on top), where each stage
can be instrumented as its own funnel. Its practical instruments overlap with the
Parlons Design sources but the framing differs: cohorts compare drop-off across
time periods and user segments, and the DAU/MAU ratio says how many days of the
month a typical user drops by, with 40% generally considered good and above 50%
excellent — a rule of thumb the chapter immediately qualifies, since "this will
actually vary depending on industry norms". Crumlish also warns that counting
anyone who shows up as active overstates the case and produces a vanity metric:
a useful definition of active requires a basket of qualifying events. His link
from engagement to retention is explicit: comparing the ratio of engaged users to
active users shows "where more lookie-loos can be converted to participants", and
"the more engaged a person is with your product, the more likely you are to
retain them in your user base". See [[Sustainable Growth]] and [[Funnel]].

Where the Parlons Design funnel guide warns against forcing engagement at the
expense of long-term retention
[[2026-05-19_414_L_anatomie_d_un_funnel_-_Guide_Growth_&_UX]], Crumlish makes the
same point as an ethical caution about metrics: avoid "dark metrics" powered by
manipulation or deception, such as making a subscription hard to cancel, which
harm people in service of short-term business goals.

### Measuring loyalty: NPS and its limits

NPS asks a single question about likelihood to recommend on a 0–10 scale,
classifies respondents as Promoters (9–10), Passives (7–8) and Detractors (0–6),
and reports the percentage of Promoters minus the percentage of Detractors
[[2024-06-21_nps-ux]]. It is designed to measure loyalty and correlates with
company growth, which is why management buys into it. The same source lists the
reasons not to use it alone:

- It measures loyalty and overall brand perception, not usability, so it
  identifies no specific usability problem.
- Passives are counted in the denominator but contribute nothing to the score,
  discarding useful middle-range information.
- Scores vary strongly by country and culture: India and Mexico rate higher,
  while Japan and South Korea can produce negative scores even for companies
  people like.
- It needs large samples; scoring five participants in a qualitative study is
  meaningless.
- It is easy to game — surveying only satisfied customers, incentivising good
  ratings — which inflates the number without improving the experience.

The recommendation is to treat NPS as one metric among several, supplemented by
behavioural data such as task success rates and task times, and by lower-level
satisfaction measures.

### Understanding why users leave

Cold calls are proposed as a qualitative method for exactly this
[[2024-11-12_351_Les_cold_calls,_méthode_d_UX_Research_-_Guide_pratique]]:
calling customers unannounced to collect fast, emotional, authentic feedback,
including from people who have stopped using the product, to understand the
motivations behind a purchase or a churn. Practical constraints from that
source:

- Calls are very short (under three minutes) and the customer does not have the
  product in front of them, so the method suits reasons and feelings, not
  interface detail.
- Response rates run only 20–30%, so build a list of several hundred customers
  and expect to chain many calls, with only a fraction of those reached
  agreeing to answer.
- Structure: a sharp introduction, transparent about the goal of improving the
  product and clearly distinct from a sales call; then only three short
  questions about a recent experience (less than a week old), ideally asking the
  customer to tell a story.
- Legal: use customer data in strict compliance with GDPR and the user's
  communication preferences; if the call is recorded, collect explicit consent
  within the first thirty seconds.

The same source notes product–market fit can be estimated during the call by
asking whether the user would be disappointed if the product disappeared.

### Intervening at the moment of departure

Exit-intent popups track cursor movement toward the page boundary and fire when
the user signals intent to leave [[2019-10-13_exit-intent-good-ux]]. Their
timing is what makes them lower-risk than conventional popups: they arrive when
the user is already leaving rather than interrupting a task. The source's
retention-relevant argument is that these moments should ease the user's goals
rather than merely capture contact details — saving progress, reminders and
support offers address the actual barriers to returning. Among its ten
applications:

- Instant discount codes, since users abandon carts to hunt for coupons anyway.
- Mistake prevention when someone is about to leave checkout or an unfinished
  multi-step process, preventing data loss.
- Saving progress — emailing the cart or storing the state of a long task so the
  user can return without starting over.
- Genuine value with nothing asked in return (a content download, a
  consultation, a support contact) rather than a self-serving, pushy ask.
- Feedback requests framed in customer-centric language ("sharing your
  experience will help us serve you better").
- Surfacing user-friendly policies users rarely discover on their own —
  price-match and money-back guarantees, free samples, free trials.

### Brand consistency as a retention driver

[[2016-07-03_brand-experience-ux]] argues brand is now the sum of a person's
experiences with a product or company, expressed equally through visuals
(graphic elements), tone (communication style) and behaviour (how the company
acts). Because customers cannot separate how they feel about a brand from how
they feel about their experiences with it, exceptional UX becomes the
competitive differentiator, and consistent delivery of visuals, tone and
behaviour across every channel is what produces the strong brand experiences
that drive customer loyalty in competitive markets. Interaction details —
transitions, animations, overall system behaviour — carry brand attributes and
shape perceptions of professionalism and competence.

## Sources (7)

- [[2016-07-03_brand-experience-ux]] — Strong, consistent brand experiences drive customer loyalty and differentiation in competitive markets.
- [[2019-10-13_exit-intent-good-ux]] — Offering progress-saving, reminders, or support addresses barriers to return; retention strategies should ease user goals, not just capture contact information.
- [[2024-06-11_332_Designer_et_AB_tester_un_paywall]]
- [[2024-06-21_nps-ux]] — NPS is specifically designed to measure loyalty and its correlation with business growth, though loyalty is not identical to usability.
- [[2024-11-12_351_Les_cold_calls,_méthode_d_UX_Research_-_Guide_pratique]]
- [[2026-05-19_414_L_anatomie_d_un_funnel_-_Guide_Growth_&_UX]]
- [[2022-01-19_product-management-for-ux-people_09-chapter-6-product-analytics-growth-engagement-retention]] — the percentage of users who return after initial use, measured by cohorts over time; retention is the foundation of compounding growth.
