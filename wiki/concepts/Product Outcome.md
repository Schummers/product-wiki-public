---
type: concept
name: Product Outcome
created: 2026-09-03
updated: 2026-09-11
status: developed
aliases:
  - "Desired Outcome"
  - "Leading Indicators"
  - "Measuring Impact"
---

# Product Outcome

## Definition

An outcome is the change the product produces, as opposed to the product itself.
Jeff Patton, in *User Story Mapping*, sets out a three-term vocabulary: **output**
is what we build, **outcome** is how people's lives change when they use it to
reach their goals, and **impact** is the long-term business benefit that follows
([[2014-09-05_user-story-mapping_05-read-this-first]]). Teresa Torres, in
*Continuous Discovery Habits*, uses a partly different split: a **business
outcome** measures company progress and is usually a lagging indicator, a
**product outcome** measures how well the product drives that business result and
behaves as a leading indicator, and a **traction metric** merely tracks usage of a
specific feature ([[2021-05-18_continuous-discovery-habits_06-chapter-three-focusing-on-outcomes-over-outputs]]).
The two works therefore cut the same territory differently: what Patton calls
impact sits close to what Torres calls a business outcome, and both reserve
"outcome" for a change in behaviour rather than a shipped feature. Torres quotes
Josh Seiden's formulation, "An outcome is a change in human behavior that drives
business results."

Both books treat the outcome, not the feature list, as the thing a team should be
held to. Patton frames the job as minimising output while maximising outcome and
impact ([[2014-09-05_user-story-mapping_05-read-this-first]]); Torres defines
success as the value the code creates for customers and for the business rather
than the code shipped, and calls the opposite the build trap: measuring success by
outputs, by shipping and developing features rather than by the value those
things produce ([[2021-05-18_continuous-discovery-habits_04-chapter-one-the-what-and-why-of-continuous-discovery]],
[[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]]).
Marty Cagan makes the same contrast in the forewords to both books: strong teams
work from KPIs, customer response and business impact and expect several
iterations before an idea reaches the desired outcome, while weak teams build the
roadmap as written and are satisfied with hitting dates
([[2014-09-05_user-story-mapping_03-foreword-by-marty-cagan]],
[[2021-05-18_continuous-discovery-habits_02-foreword-marty-cagan]]).

## Practice

### Which outcome a team should be given

- Torres argues product trios should be assigned **product outcomes**, not
  business outcomes and not traction metrics: teams make more progress on a
  leading indicator that predicts the direction of a lagging business metric,
  because the feedback cycle is shorter
  ([[2021-05-18_continuous-discovery-habits_06-chapter-three-focusing-on-outcomes-over-outputs]]).
- The outcome should be assigned to the trio as a unit rather than to individual
  members, so that product manager, designer and engineer pursue a shared goal
  (same chapter). See [[Product Trio]].
- Setting the outcome is a **two-way negotiation**: leaders bring business context
  and strategic priorities, the trio brings customer knowledge and a realistic
  estimate of achievable impact; Torres treats both inputs as necessary
  ([[2021-05-18_continuous-discovery-habits_06-chapter-three-focusing-on-outcomes-over-outputs]]).
- On goal-setting, Torres cites research showing that when a team faces a complex,
  unfamiliar outcome, a **learning goal** (discover which strategies work) beats a
  specific, challenging performance goal; commit to a performance target only once
  the strategies are known (same chapter).

### Torres's anti-patterns

From [[2021-05-18_continuous-discovery-habits_06-chapter-three-focusing-on-outcomes-over-outputs]]:
pursuing too many outcomes at once, ping-ponging between outcomes from quarter to
quarter, assigning an outcome to an individual instead of a team, dressing an
output up as an outcome, and pushing one outcome to the detriment of health
metrics.

### The outcome as the root of discovery

- In the [[Opportunity Solution Tree]], the desired outcome is the root: it frames
  the scope of discovery and gives the team the latitude to look for
  customer-centric solutions
  ([[2021-05-18_continuous-discovery-habits_05-chapter-two-a-common-framework-for-continuous-discovery]]).
- Opportunities are then prioritised by which of them will drive the product
  outcome, which is how customer needs stay central to strategy rather than being
  displaced by a feature roadmap
  ([[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]]).
- Torres also uses the outcome to set the scope of an [[Experience Map]]: narrow
  scope for an optimisation outcome, broader scope for an open-ended one
  ([[2021-05-18_continuous-discovery-habits_07-chapter-four-visualizing-what-you-know]]).
- Patton's equivalent move is **slicing the map**: draw a line across the story map
  and push below it every task that is not needed to reach the chosen outcome.
  This exposes what is essential and, in Patton's words on prioritisation, prevents
  gold-plating ([[2014-09-05_user-story-mapping_10-5-you-already-know-how]]).

### Measuring the outcome

- Torres advises against measuring everything up front. Rather than a waterfall
  instrumentation project, start by measuring what the current assumption tests
  need and iterate towards outcome measurement
  ([[2021-05-18_continuous-discovery-habits_14-chapter-eleven-measuring-impact]]).
- Intermediate metrics are useful but not sufficient. In her AfterCollege example,
  search starts, job views and applications served [[Assumption Testing]], but the
  team still had to track actual hires, because the business outcome was job
  placements and not applications; driving the product outcome does not by itself
  prove the business outcome follows, so that connection must be tested too (same
  chapter).
- Do not stop at what is easy to instrument: when the final outcome happens off
  the platform, find a way to collect it anyway. AfterCollege sent a follow-up
  email 21 days after an application to learn what had happened (same chapter).
- Decide deliberately whether a metric counts people or actions, depending on
  whether the value comes from many people doing one thing or one person doing it
  many times (same chapter).
- Torres also suggests documenting the expected impact of a release, measuring the
  actual impact afterwards, and using the gap to show stakeholders what discovery
  is worth ([[2021-05-18_continuous-discovery-habits_17-chapter-fourteen-start-small-and-iterate]]).

### Evaluating after release

- Patton treats evaluation as multi-level: with the team on quality, with users on
  whether the problem is solved, with stakeholders on release readiness, and then
  post-release through metrics and observation of real use, which feeds new
  opportunities back into the cycle
  ([[2014-09-05_user-story-mapping_16-11-rock-breaking]]).
- Before releasing, Patton asks teams to define what counts as **enough software**
  for each audience: stakeholders need what is critical to acquire customers or
  learn against competitors, customers need value they can use, users need enough
  to complete a goal. The measure of done is whether users reach their goals and
  the business meets its objectives, not whether the stories are marked done
  ([[2014-09-05_user-story-mapping_23-18-learn-from-everything-you-build]]).
- Patton's own caution: outcomes are never insured. Users behave unpredictably
  despite validation, so plan to learn from every release, measure or observe real
  outcomes rather than waiting for complaints, and improve in the next cycle
  (same chapter).

## Sources (12)


- [[2021-05-18_continuous-discovery-habits_02-foreword-marty-cagan]] — The book teaches teams how to connect customer problem-solving to achieving business outcomes rather than building predetermined features.
- [[2021-05-18_continuous-discovery-habits_03-introduction]] — The coaching curriculum teaches teams how to measure and drive outcomes that matter to both customers and businesses.
- [[2021-05-18_continuous-discovery-habits_04-chapter-one-the-what-and-why-of-continuous-discovery]] — The chapter emphasizes outcomes over outputs, defining success by customer value and business sustainability rather than features shipped or code delivered.
- [[2021-05-18_continuous-discovery-habits_05-chapter-two-a-common-framework-for-continuous-discovery]] — The root of the tree is a clear business outcome that frames the scope of discovery and gives the team latitude to find customer-centric solutions.
- [[2021-05-18_continuous-discovery-habits_06-chapter-three-focusing-on-outcomes-over-outputs]] — Torres distinguishes product outcomes from business outcomes and traction metrics, explaining when each is appropriate and how they should be chosen through negotiation between leaders and teams.
- [[2021-05-18_continuous-discovery-habits_10-chapter-seven-prioritizing-opportunities-not-solutions]] — A product outcome (distinct from a business outcome) focuses on customer value; prioritization of opportunities is guided by which opportunities will drive the product outcome, ensuring customer needs remain central to strategy.
- [[2021-05-18_continuous-discovery-habits_14-chapter-eleven-measuring-impact]] — Distinguishes between product outcomes and business outcomes, showing that intermediate metrics (like search starts, job views, applications) are valuable only when they drive the ultimate goal; effective measurement requires instrumenting products to evaluate both assumption tests and progress toward desired outcomes, emphasizing what matters rather than everything, and maintaining focus on the end goal (like increasing job placements) rather than becoming distracted by successful intermediate metrics.
- [[2014-09-05_user-story-mapping_03-foreword-by-marty-cagan]] — Cagan contrasts teams that focus on outcomes (KPIs, customer response, business impact) with teams that focus only on output (shipping on schedule).
- [[2014-09-05_user-story-mapping_05-read-this-first]] — Patton introduces outcome as the central strategic concept: how people's lives change as a result of using what we build, distinct from output (what we build) and impact (business benefit), and positions outcome as the measure that matters most.
- [[2014-09-05_user-story-mapping_10-5-you-already-know-how]] — Slicing the map to a specific outcome shows which tasks and details are essential to reach that goal; prioritizing based on outcomes prevents gold-plating.
- [[2014-09-05_user-story-mapping_16-11-rock-breaking]] — Stories serve outcomes that users seek and businesses pursue. Evaluation asks whether the outcomes are actually being met, using metrics and conversations post-release. Learning from actual use feeds new opportunities back into the cycle.
- [[2014-09-05_user-story-mapping_23-18-learn-from-everything-you-build]] — The ultimate measure is whether users achieve their goals and whether the business achieves its objectives, not whether stories are "done." Patton emphasizes defining "enough software" for each audience (stakeholders, customers, users) before release.
