---
type: concept
name: Analytics
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Analytics Framework"
  - "Analytics Strategy"
  - "Analytics and Metrics"
  - "Analytics and Strategy"
  - "Behavioral Analytics"
  - "Data Analytics"
  - "Metrics and Analytics"
  - "Search Analytics"
---

# Analytics

## Definition

Analytics is the collection and interpretation of numerical data about what
users actually do in a live product: where they go, what they click, which
features they use, where they churn. It sits inside the wider family of
quantitative UX research alongside quantitative usability testing, A/B and
multivariate testing, surveys, card sorting and tree testing, and its
characteristic role is monitoring live behaviour at scale and generating
hypotheses that qualitative research then explains
[[2021-08-29_quantitative-research-study-guide]]. Quantitative work measures how
many users hit a problem and how severe or widespread it is; qualitative work
explains why the problem exists — the two are complementary, not substitutes
[[2021-08-29_quantitative-research-study-guide]], [[2022-10-16_analytics-pathways]].

The recurring theme across the sources is that analytics is an interpretation
problem more than a collection problem. Numbers without context mislead
[[2019-10-13_vanity-metrics]], the easily measurable is not the meaningful
[[2017-05-14_ux-goals-analytics]], and behavioural data can never reveal intent:
two users on an identical path may have opposite motivations, and one
abandonment may be satisfaction while another is frustration
[[2022-10-16_analytics-pathways]]. One source situates analytics as the third of
three complementary ways to measure design impact, between direct qualitative
customer feedback and company financial metrics
[[2026-04-07_408_Les_3_façons_de_mesurer_l_impact_du_design_-_Guide_complet]].

Christian Crumlish describes it less as a method than as a daily habit, and one
that feels alien to most designers: successful product managers may spend a
large share of their time "living in the data", immersing themselves in
dashboards and exploratory analysis until they have an intuitive feel for
patterns and anomalies. His framing of the tool is the same as the sources
above — data is neither good nor evil, and works alongside qualitative research
rather than replacing it
[[2022-01-19_product-management-for-ux-people_09-chapter-6-product-analytics-growth-engagement-retention]].

## Practice

### Start from goals, not from what is easy to count

Work goal-down, not metric-up: define the high-level user-experience goal, ask
"why?" repeatedly until you reach the root goal, identify the observable
behaviours that signal it is being met (scroll depth, widget interaction, photo
zooming, return patterns), then design the measurement — rather than starting
from available metrics and inferring insight backwards. Real goals are never
"reduce bounce rate" or "increase page views"; they describe experiences.
Narrow to the strongest signals rather than tracking every possible proxy, and
measure the actual benefit — for a time-saving feature, measure time on task, not
adoption [[2017-05-14_ux-goals-analytics]]. Before collecting anything, ask what
action you would take with the answer [[2017-05-14_ux-goals-analytics]].

Frameworks help structure that translation. CASTLE (Cognitive Load, Advanced
Feature Usage, Satisfaction, Task Efficiency, Learnability, Errors) is built for
workplace and productivity software where users cannot choose whether to use the
product, and where HEART's engagement/adoption/retention dimensions apply poorly.
Like HEART it decomposes each dimension into goals, signals and measures — and it
is explicit that not every dimension is best served by analytics: cognitive load
needs surveys such as NASA-TLX or inspection methods, satisfaction needs surveys
and post-task questionnaires, task efficiency is better captured by controlled
usability testing because live analytics are skewed by external interruptions,
while errors are a good fit for analytics instrumentation
[[2023-01-29_castle-framework]].

### Vanity metrics and the context that fixes them

Ever-growing totals — cumulative users, downloads, page views, shares — always go
up with time, so they cannot tell you whether a design change helped. The fix is
context: express metrics as rates or ratios normalized by time or population
(downloads per store-page visit, page views per session, conversion per visit,
DAU/MAU stickiness), so the metric is relatively stable and a change means
something real. Choose a time frame that balances stability and responsiveness —
per-minute is noise, yearly is too slow, weekly or monthly is usually the sweet
spot. Cohort analysis (comparing users who joined the same week) shows whether an
improvement sticks. An actionable metric is one that moves when the design moves
[[2019-10-13_vanity-metrics]].

Conversions should be tracked at two grains. Macro conversions are the actions
directly tied to business objectives (a completed purchase, an account created);
micro conversions are the smaller steps along the way (adding to cart, reaching
the checkout page) and give far more frequent feedback on a design change than
waiting for macro conversions. Process milestones (linear progress toward the
macro conversion) differ from secondary actions (trust- and loyalty-building, not
required steps). For mandatory actions such as an intranet workflow, conversion
metrics are the wrong instrument — measure ease of use and error counts instead;
and products with no sales goal can still track registrations, downloads or other
meaningful optional actions [[2024-07-19_micro-conversions]].

### Reading the standard metrics carefully

**Bounce rate.** Popular and readily available, but optimizing for it produces
bad design. Not all bounces are failures: a user who found the exact answer on
one page had a successful visit. Sites chasing the metric split articles across
pages, hide details behind "learn more" and withhold prices, adding artificial
friction that costs the return visit. Use bounce rate selectively — a high rate
for one page type compared with similar pages is a red flag — but track return
rate and frequency instead of optimizing site-wide bounce
[[2016-11-13_return-visits-not-bounce]].

**Frequency and recency.** Counting visits per user (not merely new vs.
returning) shows what share of the audience is highly familiar and whether the
design should serve novices or experts; recency (days since last visit) shows
whether return rhythm matches content update rhythm — a spike at six days often
tracks a weekly newsletter. Frequency histograms in isolation reveal little; the
insight comes from segmenting, especially by conversion event. Knowing
conversions typically land after five or six visits enables targeted action:
reminders to users at three or four visits, features that ease context recovery,
or research into the barrier [[2016-10-09_frequency-recency]].

**Information-architecture signals.** Five analytics patterns flag IA problems —
low traffic to a category, low conversion, high bounce on category pages, low
entrance rates, and high search-query volume for terms that match no category.
Each needs contextual interpretation before acting: compare against the average,
check for visual-prominence bias, weigh strategic importance and SEO value,
consider whether the category feeds longer multi-visit journeys, and supplement
with A/B testing or surveys when ambiguous [[2016-09-25_ia-warning-signs-analytics]].

**Pathways.** Sankey diagrams of common page sequences show where traffic flows,
but they aggregate users with different goals, so identical paths can represent
opposite experiences. Filter into meaningful chunks (a single node, mobile vs.
desktop, one key goal), review entry pages, look for anomalies in second-step
patterns, investigate hub pages users keep returning to (engagement or
frustration), and start from the desired outcome and work backwards. Then
supplement with qualitative research for intent
[[2022-10-16_analytics-pathways]].

**Long-tail distributions.** The tail is where UX work compounds: search,
information architecture and filtering are what make niche inventory findable and
revenue-generating; long-tail keywords are cheaper to advertise on and can be
identified from search logs and user research; the long tail of slow requests
costs retention even when most requests are fast; and machine-learning accuracy
depends on rare training examples [[2021-12-12_long-tail]].

### Site-search logs as a research source

Internal site-search logs, distinct from external search analytics, show what
users want from your site and whether the IA serves them. Top queries reveal
demand; zero-result queries reveal content or navigation gaps. Sort by user
identifier and timestamp to reconstruct sessions — repeated searches for related
terms mean the earlier query failed. Cluster queries by meaning and intent to
surface content groupings, cross-link opportunities, best bets and FAQs. Compare
user vocabulary against site labels to catch mismatches from branded terms,
acronyms or cute labels. Long full-sentence queries or non-ASCII input signal
either distress or attempted attacks and deserve investigation. Findings feed
content strategy, IA, search tuning through synonyms and best bets, and new
features — and personally identifiable information in logs must be protected
[[2017-07-30_search-log-analysis]].

### Choosing among quantitative methods

Start from the research question, then filter by budget and minimum sample size.
General questions about usability trends suit quantitative usability testing,
analytics or surveys; specific questions about a design choice suit A/B testing,
card sorting, tree testing or desirability studies. Behavioural methods (testing,
analytics, A/B) measure what people do; attitudinal methods (surveys, card
sorting, desirability) measure what they say. Web analytics and surveys are cheap
and easy; eyetracking and in-person testing are expensive and hard
[[2018-04-22_quantitative-user-research-methods]].

Perceived usability has standard instruments, preferable to custom ones because
their validity, reliability and sensitivity are established: SUS (10 questions,
post-test, 0–100, average 68 across 500 studies, 80+ places a site in the top
10%), SEQ (a 7-point post-task question that pinpoints which sections are hardest),
and NASA-TLX (6 questions, for workload in high-consequence environments like
healthcare and aerospace, not typical consumer UX). Post-task instruments are less
distorted by the peak-end effect than post-test ones, and subjective scores should
be paired with objective performance data
[[2018-02-11_measuring-perceived-usability]].

Experiments: A/B testing compares genuinely different designs; multivariate
testing tests several elements at once and, unlike sequential A/B tests, reveals
interactions between them, so the best combination may not be the one individual
tests would suggest. Because variations multiply (two variables with two variants
each gives four variations), MVT needs much more traffic and longer runs — use A/B
for radical redesigns and MVT afterwards to refine the winner
[[2018-04-08_multivariate-testing]].

### Statistical rigor and bias

Quantitative methods need larger samples than qualitative testing — typically
20–30 users minimum — and results from five users must not drive design decisions
[[2018-04-22_quantitative-user-research-methods]],
[[2018-02-11_measuring-perceived-usability]]. Interpretation requires confidence
intervals, margins of error, statistical significance and deliberate study design
(within- vs. between-subjects); without that rigor the conclusions are unreliable
[[2021-08-29_quantitative-research-study-guide]]. NPS makes the failure modes
concrete: it measures loyalty and brand perception rather than usability,
excludes Passives (7–8) from the score while counting them in the base, varies
strongly by country and culture (high in India and Mexico, negative in Japan and
South Korea even for liked companies), demands large samples, and is frequently
gamed by surveying only satisfied customers or incentivizing high ratings. It
should be one metric among several, backed by behavioural data such as task
success and task time [[2024-06-21_nps-ux]].

Time frame is itself a rigor question. The Pandora study of 35 million users over
18 months found that users exposed to 38% more ads listened 2.8% fewer hours per
week, with the effect growing from 0.4% at one month to 2.8% at one year — 41% of
the loss from users leaving and 59% from remaining users engaging less. A decision
taken on one month of data would have reached the wrong conclusion
[[2018-05-06_annoying-ads-cost-business]].

### Living in the data, and instrumenting for it (book)

[[2022-01-19_product-management-for-ux-people_09-chapter-6-product-analytics-growth-engagement-retention]] treats analytics as an owned daily practice rather than a study you commission:

- **Immersion, not consumption.** Set up alerts for anomalies and actively interrogate the data to find patterns and meaning, instead of passively reading dashboards. Matt LeMay, co-founder of Sudden Compass, gives the counterweight in the same chapter, calling his own version "living in your user's reality": data is a proxy for people and their experiences, not an end in itself, and he has seen product managers "spend forever on dashboards but never actually learn directly from their customers".
- **Technical self-sufficiency.** Learn SQL, or use a no-code tool such as Airtable, so you can query and manipulate data yourself; you cannot always wait for an engineer or analyst to answer your question.
- **Instrumentation belongs in the feature spec.** Adding analytics hooks that capture user and system events must be part of every spec and launch plan, never an afterthought. Once it is a convention, everything you ship is measurable from day one.
- **Reality-check the numbers.** Lukas Bergstrom, an ex-Google product consultant quoted in the chapter, argues that at least some quantitative data needs to be regularly checked against qualitative research. Crumlish adds that he finds it helpful to treat product metrics and qualitative deep dives as opposite poles to move between constantly.

**Funnels and the AARRR frame.** Funnels show how many users complete each step of a multi-step process; the chapter offers a rough rule of thumb that you lose 10% off the top each time you add a step, while stressing that drop-off varies greatly and that some steps are trivial enough that everyone who clears the previous one clears the next. The work is spotting anomalous drop-offs against normal attrition, monitoring funnels over time to see whether experiments improve conversion, and comparing cohorts across periods and segments. Growth levers are organised by AARRR, which Crumlish credits to Dave McClure, an entrepreneur and investor "from the eBay mob", and flags as a start-up-oriented framing: Acquisition, Activation, Retention, Referral, Revenue, sometimes written AAARRR with Awareness on top. Each stage can be instrumented as its own funnel. On DAU/WAU/MAU the chapter is explicitly offering rules of thumb: DAU/MAU says how many days a month a typical user drops by, 40% is generally considered good and above 50% excellent, "but this will actually vary depending on industry norms". Counting anyone who shows up as active overstates the case and produces a vanity metric, so a useful definition of active requires a basket of qualifying events. See [[Funnel]] and [[Sustainable Growth]].

**Two cautions.** Avoid "dark metrics" powered by manipulation or deception, such as making a subscription hard to cancel: they harm people in service of short-term business goals. And guard against a proxy metric becoming an end in itself, since it can improve while the underlying goal does not — which is why it needs ongoing validation against qualitative research and other signals.

### Connecting analytics to business impact

ROI calculation is a four-step unit conversion: benchmark a UX metric before and
after the change (from surveys, analytics, quantitative usability testing or
support data), pick a KPI the organization actually cares about, find the
conversion ratio and multiply (support tickets at $6 each, reduced by 21,900,
gives $131,400 saved a year), and report transparently about sources and
assumptions. These are strategic estimates, not financial forecasts; include
project costs and project two to five years, since design improvements persist
[[2020-02-23_calculating-roi-design-projects]]. Benchmarking over time,
competitor comparison and ROI are the standard uses of quantitative data for
demonstrating UX value [[2021-08-29_quantitative-research-study-guide]].

For product-led growth, where users discover value by using the product rather
than through a salesperson, UX work must connect to time to value, conversion
rate, retention, churn and customer-acquisition cost; usage patterns identify
at-risk segments and reveal what engaged users do early, so retention-driving
features can be promoted, and the Pareto principle argues for investing in
understanding the top 20% of customers who generate 80% of revenue
[[2023-05-21_product-led-growth-ux]]. In the same spirit, a designer should become
owner of the analytics rather than a consumer of it: define the tracking plan, run
tools such as Amplitude or Mixpanel, and build dashboards tied to feature
releases; the highest maturity level is expressing an initiative's value in euros
against revenue, margin and churn, where approximate ranges are enough to start
[[2026-04-07_408_Les_3_façons_de_mesurer_l_impact_du_design_-_Guide_complet]].

Research impact itself can be metered. The Recommendation-Adoption Score treats
recommendations as inventory — each with an owner, a clear definition of done and
tied-back evidence — assigns a status (Adopted, Committed, Communicated,
Canceled) and a user-value rating, and computes actual user value over total
possible value as a 0–100 score: Poor (0–29) means research is ignored, Fair
(30–54) some movement, Good (55–79) majority adoption, Great (80–100) rare. As
with every other metric here, the trend over a rolling 12-month window matters
more than any single score, because new research entering as Communicated
mechanically lowers it [[2026-02-20_recommendation-adoption-score]].

### Presenting the numbers

Communicating quantitative results is part of the method: charts need attention
to context, contrast and clutter, and should carry the key takeaway rather than
overwhelm the viewer with data
[[2021-08-29_quantitative-research-study-guide]].

## Sources (24)

- [[2016-09-25_ia-warning-signs-analytics]] — Shows how to translate raw metrics (traffic, conversions, bounce rates, entrances, search queries) into actionable insights about content organization and user behavior.
- [[2016-10-09_frequency-recency]] — Demonstrates how frequency and recency metrics quantify user engagement and reveal loyalty patterns, while behavioral patterns (visit timing, frequency, duration) reveal user intent, preferences, and barriers—together informing strategy and guiding design and content decisions based on actual behavior rather than assumptions.
- [[2016-11-13_return-visits-not-bounce]] — Bounce rate is a popular but potentially misleading metric; understanding what bounces actually represent is crucial for interpreting analytics correctly.
- [[2017-05-14_ux-goals-analytics]] — Emphasizes the gap between what's measurable and what's meaningful; advocates metric selection based on goals rather than convenience.
- [[2017-07-30_search-log-analysis]] — analysis methods for site-search logs including extraction, clustering, sequence analysis, and acting on findings through search tuning and content strategy.
- [[2018-02-11_measuring-perceived-usability]] — using established questionnaires like SUS and SEQ to quantify and benchmark usability metrics over time.
- [[2018-04-08_multivariate-testing]] — using MVT to quantify the performance impact of different design element combinations on conversion goals.
- [[2018-04-22_quantitative-user-research-methods]] — using quantitative data collection to benchmark and compare designs objectively against business metrics.
- [[2018-05-06_annoying-ads-cost-business]] — using longitudinal quantitative studies to measure cumulative business impacts of UX decisions over time.
- [[2019-10-13_vanity-metrics]] — Metrics require careful selection; raw counts without context mislead; meaningful metrics include rate, time frame, and relationship to design goals.
- [[2020-02-23_calculating-roi-design-projects]] — Shows how to select appropriate UX metrics and collect them through benchmarking studies to quantify design impact.
- [[2021-08-29_quantitative-research-study-guide]] — Analytics data describe live user behavior (where users go, what they click, features used, churn points); analytics inform UX by revealing what users actually do, supporting monitoring and hypothesis generation for qualitative research.
- [[2021-12-12_long-tail]] — The article shows how understanding long-tail patterns in user behavior and data informs strategic business and UX decisions.
- [[2022-10-16_analytics-pathways]] — pathways data reveals common user flows and bottlenecks but must be supplemented by qualitative research to understand intent; analytics alone cannot explain why users behave as they do.
- [[2023-01-29_castle-framework]] — The framework emphasizes choosing measurement approaches (analytics, surveys, testing, inspection) appropriate to each dimension; not all dimensions are best measured through analytics.
- [[2023-05-21_product-led-growth-ux]] — Tracking key performance indicators specific to product-led growth including time to value, conversion, retention, and churn.
- [[2024-06-21_nps-ux]] — implementing NPS measurement requires attention to statistical significance, sample size, and potential bias sources like sampling bias and rating racketeering.
- [[2024-07-19_micro-conversions]] — addresses how to select appropriate metrics for different product contexts including nonmonetary and enterprise applications.
- [[2026-02-20_recommendation-adoption-score]] — RAS provides a quantifiable, interpretable metric for research impact; trending RAS separates temporary setbacks from systemic problems.
- [[2026-04-07_408_Les_3_façons_de_mesurer_l_impact_du_design_-_Guide_complet]]
- [[2013-08-01_just-enough-research_08-chapter-7-evaluative-research]] — Once a product is live, analytics provide quantitative data on how users actually interact with the system. Combined with qualitative usability testing observations, analytics reveal both what users do and why. The chapter emphasizes that understanding actual behavior through data is essential to effective evaluation alongside user observation.
- [[2013-08-01_just-enough-research_10-chapter-9-quantitative-research]] — the collection and analysis of user interaction data on live sites; basic metrics include visits, pageviews, bounce rate, time on site, and traffic sources; tools like Google Analytics enable quick identification of pages and behaviors underperforming against goals.
- [[2016-11-04_ux-research_04-chapter-3-quantitative-research-methods]] — system analytics are presented as a major quantitative method for passive data collection on user flows, demographics, and geography, providing low-cost insight into how customers access and use products
- [[2022-01-19_product-management-for-ux-people_09-chapter-6-product-analytics-growth-engagement-retention]] — systematic immersion in data and interactive interrogation of metrics to find patterns and drive product decisions.
