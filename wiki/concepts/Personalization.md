---
type: concept
name: Personalization
created: 2026-07-31
updated: 2026-09-11
status: developed
---

# Personalization

## Definition

Personalization is done by the system: developers set it up to identify users
and deliver the content, experience or functionality that matches their role,
either at group level (intranet content filtered by job function) or at
individual level (purchase-based suggestions)
[[2016-07-10_customization-personalization]]. Its defining contrast is
customization, which is done by the user, who actively configures layout,
content or functionality. Personalization improves the experience without asking
users for effort, but it depends entirely on the system guessing correctly;
customization gives control but demands participation.

Because it is a guess, personalization is best read as an assumption about user
needs, derived from data, that has to be maintained and can be wrong
[[2016-10-02_personalization]]. The sources trace its spread from filtered
content and recommendation modules [[2018-11-04_recommendation-guidelines]] to
email [[2017-08-13_newsletters]], to orchestrated cross-channel journeys
[[2020-08-16_omnichannel-orchestration]], and finally to interfaces generated in
real time for each user [[2024-03-22_generative-ui]]. Expectations have moved
with it: relevance is no longer a bonus but the baseline against which generic
content is judged as spam [[2017-08-13_newsletters]].

## Practice

### Decide whether to personalize at all

Neither personalization nor customization should be used to fix a poor site
structure or unclear content; they should enhance an experience that is already
good, and be used thoughtfully with a clear purpose
[[2016-07-10_customization-personalization]]. Both add complexity to the baseline
experience, so the trade-off is deliberate: personalization buys convenience at
the cost of user control, customization the reverse.

### Build the user model conservatively

[[2016-10-02_personalization]] gives six operating rules, all pulling toward
restraint:

- **Assign roles conservatively.** Past behaviour does not always predict future
  action — someone who bought a responsive-design book may have bought it for a
  course, a colleague or as a gift. Tagging too narrowly produces an inaccurate,
  restrictive experience that annoys at every visit.
- **Restrict access sparingly.** Successful personalization mostly adds or
  reshuffles content rather than removing it; Amazon promotes matching products
  without blocking the rest. Remove access only where genuinely required
  (mature content and minors, role-based security, regional compliance).
- **Create only as many roles as you can maintain.** Intranet teams report
  segmenting so finely that maintenance became impossible. Personalize by broad
  characteristics — location, department, level — rather than nuanced profiles.
- **Personalize functionality, not just content.** Autofill known information
  (editable), remember frequent selections and searches, save progress in long
  workflows, continue seamlessly across devices.
- **Provide an out.** A "view as" or "swap role" feature lets support staff and
  managers see what a user sees; universal-access options let users override
  settings that go against their needs.
- **Review regularly.** Monitor traffic to personalized content, track
  personalization-related complaints, verify data-source accuracy, adjust roles
  against actual usage.

### What users expect from recommendations

The study behind [[2018-09-30_recommendation-expectations]] (8 participants,
remote moderated) found users value recommendations as curation: a way to narrow
a large inventory without sifting through everything. Participants knew sites
track them and largely accepted it as a normal cost of the internet, willing to
trade some privacy for relevance. They expected explicit actions — purchases,
saved items — to weigh more than passive browsing, since clicking something does
not prove interest. They read perceived popularity as a signal: trendy items felt
shown to everyone, niche items felt personal. New or infrequent users accepted
that the system needs time to become accurate.

One point where the sources pull in different directions: this study found bad
recommendations easy to ignore and users unwilling to invest effort in feedback,
whereas [[2018-11-04_recommendation-guidelines]] recommends building rating,
history-editing and fine-tuning mechanisms, and [[2016-10-02_personalization]]
treats a mis-tagged user as a recurring frustration serious enough to drive
people away. Tolerance appears to depend on the stakes of the mistake rather than
on a single rule.

### Presenting recommendations

[[2018-11-04_recommendation-guidelines]] turns the research into placement rules:

- Prioritize personalized recommendations above generic content — individualized
  suggestions are valued far more, and higher placement raises discoverability.
- State the data sources behind each suggestion specifically; vague wording such
  as "and more" confuses. Source clarity builds credibility and helps users judge
  whether to explore.
- Split recommendations into genre- or behaviour-based categories instead of one
  undifferentiated block, especially for users with diverse interests.
- Let users rate suggestions and edit their browsing history, which raises
  engagement where accuracy matters.
- Update recommendations quickly: users expect feedback to be reflected
  immediately, and fast updates visibly demonstrate that the system is learning.

### Personalization in email

[[2017-08-13_newsletters]] tracks 15 years of newsletter research and reports the
threshold shifting: spam is now defined by irrelevance rather than by lack of
consent, so a personalized-but-mismatched message is dismissed as spam even when
the user opted in. Newsletters using known user data for relevant, targeted
content get strong positive responses; generic broadcasts do not. The article
positions relevance as the next competitive requirement for UX and customer
experience.

### Orchestration across the journey

[[2020-08-16_omnichannel-orchestration]] extends personalization from a page to a
journey: orchestration is the surreptitious planning and coordination of a
journey to minimize user effort for future actions, predicting the next need
before the customer formulates it. It describes three maturity levels:

1. **Automation of common paths** — no customer data required, only service
   design; e.g. contextual notifications as customers move through steps.
2. **Segment-level personalization** — specific customer data used to inject
   personalized interactions at identified journey moments; e.g. comparison
   emails or test-drive maps built from browsing history.
3. **Real-time engines** — journey-orchestration engines with customer-data
   platforms and AI predicting future interactions; e.g. a food-delivery email
   after a late-night ride.

Organizations do not need advanced data infrastructure to start; they progress
from service design toward data-driven approaches. Speculative nudges should be
monitored through analytics and conversion, and discontinued when few customers
accept them.

### The generative frontier, and its friction

[[2024-03-22_generative-ui]] describes generative UI as an interface dynamically
generated in real time by AI to fit each user's needs and context — personalization
at the level of the interface itself rather than the content within it. It shifts
the designer's job from designing discrete elements to defining outcomes, user
goals and guard rails, and makes user research more critical, not less, since
dynamically generated interfaces still have to be tested against diverse needs.
The article is explicit about the costs: generative AI's hallucinations and
biases become genUI's, processing demands may delay adoption, the personalization
requires substantial privacy-sensitive data, and constantly changing interfaces
risk frustrating users through constant relearning — the loss of exactly the
predictability that standard interfaces provide.

## Sources (8)

- [[2016-07-10_customization-personalization]] — Personalization uses system-driven intelligence to deliver tailored experiences automatically; successful personalization requires the system's model to match actual user needs.
- [[2016-10-02_personalization]] — Defines personalization principles including conservative role assignment, broad characteristics over fine-grained profiles, and user control to prevent mis-targeting and frustration.
- [[2017-08-13_newsletters]] — users increasingly expect marketing emails to be tailored to their interests and behaviors; irrelevant, generic messages are perceived as spam regardless of opt-in status.
- [[2018-09-30_recommendation-expectations]] — what users expect from individualized content and how they perceive sites learning their preferences through data collection.
- [[2018-11-04_recommendation-guidelines]] — how to present individualized recommendations effectively by prioritizing them, providing source clarity, and enabling user control.
- [[2020-08-16_omnichannel-orchestration]] — Three levels of orchestration provide pathways from simple automation to sophisticated AI-powered personalization that delivers unique pathways for each customer.
- [[2024-03-22_generative-ui]] — explores how genUI enables unprecedented personalization for individual users at scale.
- [[2019-12-17_storytelling-in-design_08-chapter-7-defining-the-setting-and-context-of-your-product]] — The chapter explores how context enables one-to-one experiences tailored to the individual user; through intelligent use of data (Dahlström cites Ami Ben David's definition), products can seem to know and anticipate users before they realize they need something.
