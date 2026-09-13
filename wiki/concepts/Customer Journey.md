---
type: concept
name: Customer Journey
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Customer Journey Management"
  - "Customer Journey Visualization"
  - "Customer Journeys"
  - "Journey-Centric Design"
  - "User Journeys"
  - "Experience Life Cycle"
  - "Product Life Cycle"
---

# Customer Journey

## Definition

A customer journey is the end-to-end process a person goes through to complete a
goal with an organization, spanning multiple touchpoints, channels, devices and
organizational departments, and often stretching over days, weeks or months
[[2021-07-18_customer-journey-management]]. Its building blocks are precise: a
*channel* is the medium of interaction (website, app, phone, in-person, mail),
a *device* is the means of accessing a channel, and a *touchpoint* is a specific
instance of interaction combining a device, a channel and a task
[[2016-12-04_channels-devices-touchpoints]]. Users do not think in channels: they
experience their whole interaction with an organization as one holistic journey,
and do not tolerate fragmentation between its parts
[[2016-07-24_customer-journeys-omnichannel]].

The journey is one of three levels at which experience can be designed —
interaction level (a single interface), journey level (multiple products or
channels over time), and relationship level (the lifetime connection to the
company) [[2024-11-29_ux-and-cx-merge]], [[2019-09-15_cx-organizational-fluidity]],
[[2023-02-05_omnichannel-journeys-cx-study-guide]]. Several sources argue the
journey level is where the remaining value sits: performance across a whole
journey affects satisfaction and business outcomes more than optimizing
individual touchpoints in isolation [[2020-10-11_refine-remodel]], and
micro-level interface optimization has matured to the point of diminishing
returns [[2025-02-21_long-live-ux]]. The journey is distinct from a user flow,
which zooms into a discrete interaction inside a single product; journeys are
macro, scenario-based, emotional and cross-channel, flows are micro and
transactional, and the two are complementary rather than competing
[[2023-04-16_user-journeys-vs-user-flows]].

## Practice

### Design the journey, not the touchpoint

Simply being present on every channel is multichannel, not omnichannel: the work
is both creating an appropriate experience on each channel *and* designing the
transitions between them [[2016-07-24_customer-journeys-omnichannel]]. Five
components recur as the definition of a good journey — consistency, optimization
per channel and context, seamlessness across transitions, orchestration
(proactive personalized interactions), and collaboration (channels working
together) [[2016-07-24_customer-journeys-omnichannel]],
[[2019-09-15_cx-organizational-fluidity]],
[[2023-02-05_omnichannel-journeys-cx-study-guide]]. Improvement at journey level
comes in three strategies of increasing investment: **refine** (smooth the rough
edges of existing journeys iteratively), **remodel** (moderate changes requiring
operational and foundational change), **rebuild** (entirely new experiences
built on new technology and business models); the choice should match the
organization's investment capacity, risk tolerance and competitive landscape
[[2020-10-11_refine-remodel]].

### Know the ecosystem the journey runs on

Every organization supports a different set of relevant channels — banks lean on
physical locations, internet companies on digital channels, some build
proprietary devices — so the first task is mapping that ecosystem, identifying
gaps, and examining each touchpoint's device/channel/task context
[[2016-12-04_channels-devices-touchpoints]]. Channel and device choice is driven
by task fit, not loyalty: in a healthcare diary study, 78 of 93 interactions
happened on smartphones for simple scheduling and messaging, while patients
switched to computers for intake forms and detail-heavy tasks, and the patient
portal was the most-used digital channel precisely because it consolidated
functions asynchronously in one place [[2023-03-12_healthcare-customer-journeys]].
Retail journeys show the same blending: showrooming and webrooming are
established behaviors, customers move between online and store by convenience,
and each transition is a risk of abandonment
[[2018-10-28_changing-shopper-behaviors]]. Social media is usually an entry point
into other channels rather than the primary one, supporting six distinct
interaction types: discover, research, engage, purchase, support and promote
[[2021-01-31_companies-social-media]].

Journeys also have phases with unequal design leverage. In luxury shopping the
four phases are discover, consider, purchase and use, and the *consider* phase is
the longest and the critical opportunity — where poor organization, few photos
and missing details damage the brand [[2022-06-12_luxury-user-groups-journeys]].
Journeys are rarely completed in one sitting: frequency and recency analysis
shows conversions typically follow several visits over weeks, so content, email
and design strategies must support returning and context recovery, not just
first-visit conversion [[2016-10-09_frequency-recency]].

### Mapping: scope, grounding, and the insights zone

Journey maps typically contain three zones — the lens (personas, scenarios), the
experience (actions, thoughts, emotions), and the insights (opportunities,
ownership, metrics). Most practitioners omit the third, which is the one that
turns a narrative into an action plan: without ownership there is no
accountability, without metrics no improvement can be measured
[[2016-10-16_journey-mapping-ux-practitioners]]. In a survey of 48 practitioners,
maps failed for lack of clear focus (36%), lack of research grounding (25%), not
being shared or used (21%), and lack of organizational buy-in (11%); they
succeeded when collaborative, tightly focused, action-producing and measurable
[[2016-10-16_journey-mapping-ux-practitioners]]. Consolidated advice from 300+
practitioners agrees: start small with a journey that has known pain points and
that your team has the authority to fix, mix qualitative interviews with
analytics for scale, stay low-fidelity until content and structure are validated,
involve stakeholders early, and remember the artifact is not the goal — the
decisions it drives are [[2021-03-07_journey-mapping-tips]].

Two decisions frame any mapping initiative: **current-state vs. future-state**
and **assumption-first vs. research-first**. Current-state maps expose pain
points, gaps and emotional dips and build a persuasive case for investment;
future-state maps act as a North Star for a reimagined experience.
Assumption-first workshops are fast and build buy-in but risk baking in wrong
beliefs; research-first is rigorous but slower and costlier. The recommended
hybrid: start current-state and assumption-based, validate and evolve with
research, then build the future-state vision once pain points are understood
[[2020-06-14_journey-mapping-approaches]].

### Story mapping's narrative-flow lens on the journey

Jeff Patton describes a related but simpler mechanic for laying out a journey:
arrange the tasks a person does, in the order they happen, left to right, so
reading across the map tells the story of the journey; the technique works
identically whether it maps a morning routine or product usage, because both
follow the same pattern of tasks, alternatives and goals
[[2014-09-05_user-story-mapping_10-5-you-already-know-how]]. Once the main
flow is laid out, Patton adds depth below it for alternatives and variations —
what happens when things go wrong, what a hurried version looks like, what an
ideal version looks like — which shows the many ways the same journey can play
out [[2014-09-05_user-story-mapping_10-5-you-already-know-how]]. This is a
narrower artefact than the journey maps described above (no touchpoints,
channels or emotional layer), but it is grounded the same way: Patton insists
the map be built by talking directly with people about their work and
capturing how they actually do things, not how designers imagine they should
[[2014-09-05_user-story-mapping_10-5-you-already-know-how]].

### Running the mapping workshop

Preparation, execution, follow-up. Beforehand: build a cross-functional team of
allies, pick one actor and one scenario, consolidate existing research into a
shared repository, and send participants background reading and thought-starter
questions [[2020-07-05_journey-mapping-workshop]]. During: refresh knowledge,
review research, build a current-state assumption map, then bring real customers
in to react to it with tangible tools (stickers, sticky notes) so the map is
validated and evolved rather than defended. Turn pain points into needs
statements ("I need ___ so that ___") and dot-vote them *before* ideating, so the
group does not jump to solutions; then brainstorm big ideas with customers and
have internal teams sketch flows using design-studio rounds
[[2020-07-05_journey-mapping-workshop]]. Afterwards: capture artifacts, prototype,
keep momentum.

Low-fidelity materials do real work here. Post-its make group effort visible,
equalize contributions regardless of tool proficiency or volume of voice, force
concise expression, and push a group to physically organize ideas instead of
talking in circles — while being poor for remote teams and colour-blind
participants, and never a substitute for design thinking itself
[[2018-03-25_post-it-in-ux]]. Storyboards complement journey maps: they favour
imagery over text and usually depict a *fragment* of a journey rather than the
whole, which makes them good for enriching a map with context and emotional
state, communicating research findings, and ideation — one path per storyboard
[[2018-07-15_storyboards-visualize-ideas]].

### Extending the map backstage: service blueprints

A journey map takes the customer's perspective; a service blueprint is its part
two, adding frontstage employee actions, backstage actions, support processes and
physical evidence, organized by the lines of interaction, visibility and internal
interaction [[2017-08-27_service-blueprints-definition]],
[[2022-01-23_service-design-study-guide]]. This is what exposes root causes that
single-touchpoint design cannot see, and forces departments to see how their work
affects downstream touchpoints [[2017-08-27_service-blueprints-definition]].
Service design more broadly organizes people, props and processes so that
backstage operations support frontstage touchpoints — asking a customer to repeat
information to three agents is a data-sharing process flaw, not an interface flaw
[[2017-07-09_service-design-101]]. Practically: derive customer actions from
qualitative research or an existing journey map, document how employee work
actually happens rather than how it is supposed to, keep redundant steps because
they reveal inefficiency, layer in support processes and evidence, and use dot
voting and colour-coding to mark pain points, moments of truth and opportunities
to remove steps [[2020-07-19_service-blueprinting-template]]. A spreadsheet is a
better first draft than a specialized design tool; polish for presentation only
after validation [[2020-07-19_service-blueprinting-template]]. Run it as a
workshop with 4–6 stakeholders who have power to act, one facilitator per twelve
attendees, diverge-and-converge mapping, a parking lot for open questions, and
dot voting on fail points; then layer quantitative data on the qualitative
findings and test the cleaned-up blueprint on someone who was not in the room
[[2020-09-20_service-blueprinting-workshops]].

### Finding what breaks

Pain points exist at all three levels; journey-level pain points are obstacles
along a goal-completion path and are found through user interviews, diary studies
and journey mapping, prioritized by impact across phases and by organizational
feasibility — as opposed to interaction-level pain points found via usability
testing [[2021-05-16_pain-points]]. Customer-service contacts are a direct
symptom: in a diary study of 45 journeys, 64% required at least one contact with
the organization, with missing or confusing information the single largest driver
at 38%. The recommendation is not to hide contact options but to eliminate the
*need* for them while keeping them easy to reach
[[2016-09-11_customer-service-omnichannel-ux]].

Analytics contribute pathways data (Sankey diagrams of common page sequences),
useful for spotting entry pages, anomalous second steps and hub pages users keep
returning to; but pathways aggregate many users with different intentions, so an
identical path can represent opposite experiences and abandonment may be success
or failure. Filter into meaningful segments, work backward from desired outcomes,
and supplement with qualitative research for intent and emotion
[[2022-10-16_analytics-pathways]]. This is the explicit boundary between
aggregated pathways and individual journeys.

### Transitions and orchestration

Where a journey crosses channels, either remove the transition or support it.
Rich product information online (high-quality photography, detailed descriptions,
robust reviews, close-ups) removes the need to visit a store; when a transition
is unavoidable, prepare the customer with confirmation emails carrying
directions, parking details and what to bring
[[2018-10-28_changing-shopper-behaviors]]. Communicate operational changes at
every stage of the journey rather than at the end: the COVID e-commerce study
found delays should be surfaced on homepage and product pages before checkout,
repeated at cart as a safety net for task-focused users who missed the banner,
targeted per category when only some products are affected, and reflected in
automated transactional emails, which are the message customers actually keep
[[2020-06-14_emergency-covid]].

Orchestration is the deliberate planning of a journey to minimize the user's
effort for the next action, in three levels of maturity: level one automates a
common linear journey and needs no customer data, only thoughtful service design;
level two uses customer data to personalize by segment; level three uses
journey-orchestration engines with customer-data platforms and AI for real-time
personalization [[2020-08-16_omnichannel-orchestration]]. Organizations do not
need advanced data infrastructure to start, and speculative nudges should be
monitored through analytics and conversion rates and discontinued when few
customers accept them [[2020-08-16_omnichannel-orchestration]].

### Organizing for journeys

Journey-level experience is limited by organizational structure more than by
craft. Siloed teams working independently on their own channels produce the
disconnects users experience, and fixing individual pain points without
restructuring the underlying teams, processes and technology produces the same
problems again; digitally native companies have omnichannel maturity by design,
while legacy organizations must redesign deliberately
[[2019-09-15_cx-organizational-fluidity]]. Journey management is the ongoing
practice of researching, measuring, optimizing and orchestrating a journey, built
on three competencies — insights, design and orchestration — and requiring
dedicated practitioners who own one journey and sit high enough to influence
siloed teams [[2021-07-18_customer-journey-management]]. Journeys can be managed
as if they were products, through continuous research, measurement and design
iteration [[2024-11-29_ux-and-cx-merge]].

On silos, the sources are close but not identical: one frames the answer as
merging the CX and UX functions and building cross-functional journey teams,
noting that success comes from enabling connectivity across silos rather than
destroying them [[2024-11-29_ux-and-cx-merge]]; another frames it as structural
change to teams, processes, technology platforms and culture
[[2019-09-15_cx-organizational-fluidity]]. From four organizations that made the
shift: mindset change must precede operational change, a top-down mandate alone
is not enough; codify the methodology in a playbook with a dedicated owner;
create journey-operations teams to handle onboarding and process flexibility;
prioritize by shared business objectives rather than departmental budgets to
replace competition with cooperation; hold the ideal-state map as a reference but
commit firm plans only one quarter out; and accept the work is never finished
[[2025-01-24_journey-centric-design-lessons]]. One source additionally argues
that journey-centric design is what makes design ROI attributable, and that AI
applied to an un-upgraded organizational operating system delivers only shallow
returns [[2025-02-21_long-live-ux]].

### Research methods that fit journeys

Journeys unfold over time and across channels, so context methods — field
studies and diary studies — capture them better than session-based methods, with
journey maps and service blueprints as the visualizations and strategic ideation
tools [[2023-02-05_omnichannel-journeys-cx-study-guide]],
[[2023-04-16_user-journeys-vs-user-flows]]. Usability testing belongs to the
flow level [[2023-04-16_user-journeys-vs-user-flows]]. Recommended learning order
runs from customer journey and CX fundamentals, through research and mapping
methods, to omnichannel design and journey management as an organizational
practice [[2023-02-05_omnichannel-journeys-cx-study-guide]], with service design
fundamentals preceding service blueprinting
[[2022-01-23_service-design-study-guide]].

## Sources (37)

- [[2016-07-24_customer-journeys-omnichannel]] — Modern customer journeys span multiple channels and devices; designing for the complete journey requires understanding all touchpoints and their relationships.
- [[2016-09-11_customer-service-omnichannel-ux]] — Emphasizes mapping full journeys including all stages, channel transitions, and information needs, not just individual touchpoints, to identify and eliminate roadblocks.
- [[2016-10-09_frequency-recency]] — Emphasizes that most conversions require multiple visits over weeks or months, requiring design and content strategies that support long-term engagement, not just first-visit conversion.
- [[2016-10-16_journey-mapping-ux-practitioners]] — Shows the necessity of understanding full journeys including all touchpoints, stages, and information needs, and how insights zones make journeys actionable rather than merely descriptive.
- [[2016-12-04_channels-devices-touchpoints]] — Journeys are composed of touchpoints across multiple channels and devices; understanding each touchpoint's context is essential for omnichannel design.
- [[2017-07-09_service-design-101]] — the complete customer experience including frontstage touchpoints and backstage support systems that enable seamless interactions.
- [[2017-08-27_service-blueprints-definition]] — the full sequence of touchpoints a customer experiences when interacting with a service, from initial awareness through support and beyond.
- [[2018-03-25_post-it-in-ux]] — using Post-its to map and visualize user journeys and customer touchpoints across the service experience.
- [[2018-07-15_storyboards-visualize-ideas]] — The article shows how storyboards can visualize user journeys or journey fragments, illustrating user context, emotional states, and interactions through sequential imagery.
- [[2018-10-28_changing-shopper-behaviors]] — mapping the paths customers take across channels and identifying where transitions occur and where friction can be reduced.
- [[2019-09-15_cx-organizational-fluidity]] — Customer journeys span multiple channels and touchpoints over time; delivering seamless, consistent experiences requires organizational alignment around journey-level goals.
- [[2020-06-14_emergency-covid]] — how to identify and communicate at key moments throughout the full journey from discovery to delivery.
- [[2020-06-14_journey-mapping-approaches]] — two dimensions of journey mapping (current vs. future state) and how they serve different strategic needs.
- [[2020-07-05_journey-mapping-workshop]] — practical methods for workshop-based journey mapping with customer input and cross-team participation.
- [[2020-07-19_service-blueprinting-template]] — how service blueprints extend journey maps to reveal employee and support processes.
- [[2020-08-16_omnichannel-orchestration]] — Understanding common customer journeys and identifying moments to inject orchestrated interactions at the right time in the relevant context is central to effective journey design.
- [[2020-09-20_service-blueprinting-workshops]] — Service blueprints map customer actions and emotions alongside organizational actions and support processes, revealing fail points and opportunities across entire customer journeys.
- [[2020-10-11_refine-remodel]] — viewing experience improvement at the journey level across multiple touchpoints and channels rather than optimizing individual touchpoints in isolation.
- [[2021-01-31_companies-social-media]] — maps six distinct interaction types users engage in when interacting with companies on social media platforms.
- [[2021-03-07_journey-mapping-tips]] — the article provides comprehensive guidance on creating customer journey maps to visualize end-to-end user experiences.
- [[2021-05-16_pain-points]] — Journey-level pain points require mapping entire goal-completion paths and considering cumulative impacts on the user experience.
- [[2021-07-18_customer-journey-management]] — A customer journey is the end-to-end process a customer goes through to complete a task, spanning multiple touchpoints, channels, and organizational departments; journey management treats the full journey as a strategic entity requiring coordinated research, design, and optimization.
- [[2022-01-23_service-design-study-guide]] — Service design focuses on understanding and supporting the customer journey through internal business processes; service blueprinting follows customer-journey mapping to reveal backstage operations.
- [[2022-06-12_luxury-user-groups-journeys]] — Understanding luxury shopper journeys across discover, consider, purchase, and use phases reveals where digital experiences succeed or fail to meet expectations.
- [[2022-10-16_analytics-pathways]] — individual journeys differ from aggregated pathways; qualitative research, interviews, and observation provide the rich context analytics cannot, including user goals and emotional states.
- [[2023-02-05_omnichannel-journeys-cx-study-guide]] — Customer journeys span time and channels, requiring longitudinal research and cross-functional design; journey-level thinking complements and extends interaction-level UX.
- [[2023-03-12_healthcare-customer-journeys]] — healthcare customer journeys typically include multiple touchpoints across devices and channels, with patients switching between channels based on task complexity and device capabilities.
- [[2023-04-16_user-journeys-vs-user-flows]] — Describes the high-level, scenario-based sequences users take across multiple channels and over time to accomplish goals, requiring emotional and contextual understanding.
- [[2024-11-29_ux-and-cx-merge]] — journey-centric design is an operational approach that facilitates cross-functional research and design of end-to-end customer journeys, managing and optimizing them as if they were products through ongoing research, measurement, and design iteration.
- [[2025-01-24_journey-centric-design-lessons]] — The article illustrates how mature organizations operationalize journey-centric thinking by designing experiences that transcend individual products, using journey maps, cross-functional teams, and measurement systems aligned to customer outcomes.
- [[2025-02-21_long-live-ux]] — Describes shifting from product-centric to journey-centric approaches, designing experiences across channels and time, requiring organizational operating-system upgrades.
- [[2014-09-05_user-story-mapping_10-5-you-already-know-how]] — The left-to-right narrative flow of a story map documents the customer's or user's journey; alternatives and variations captured in depth show the many ways the journey can play out.
- [[2019-12-17_storytelling-in-design_06-chapter-5-defining-and-structuring-experiences-with]] — Maps awareness, consideration, purchase, and post-purchase stages to the three-act structure and demonstrates how to break these into sequences, scenes, and steps; includes an example from Dahlström's work on Sony Ericsson (now Sony Mobile) at the agency Dare, and typical patterns across ecommerce, SaaS, travel, and other categories.
- [[2019-12-17_storytelling-in-design_08-chapter-7-defining-the-setting-and-context-of-your-product]] — Dahlström references Google's finding that user journeys are non-linear and vary even within the same task; she argues that designers must understand the full end-to-end journey as well as small contextual details that differ per user.
- [[2019-12-17_storytelling-in-design_09-chapter-8-storyboarding-for-product-design]] — Dahlström argues that storyboarding is equally valuable for customer journey mapping as it is for experience mapping; storyboards within a journey map add visual narrative and emotional flow, helping teams see the experience through the user's eyes.
- [[2019-12-17_storytelling-in-design_10-chapter-9-visualizing-the-shape-of-your-product-experience]] — The chapter applies experience goals across the stages of the product life cycle; each stage receives its own experience statements mapped to hygiene, feel good and delight levels, so that at any given point in a website or app you can say how that moment translates as an emotive feeling.
- [[2019-12-17_storytelling-in-design_11-chapter-10-applying-main-plots-and-subplots-to-user]] — the chapter reframes user journeys as layered narratives, requiring design for ideal, alternative, and unhappy paths in parallel, not just the main happy path.
