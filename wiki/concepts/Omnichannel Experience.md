---
type: concept
name: Omnichannel Experience
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Cross-Channel Design"
  - "Cross-Channel Experience"
  - "Omnichannel"
  - "Omnichannel Design"
---

# Omnichannel Experience

## Definition

Omnichannel experience is the design of an entire customer journey as one
experience rather than as a collection of independently optimised channel
interactions. The founding distinction in these sources is between multichannel
and omnichannel: simply existing on every channel is not omnichannel, because
omnichannel means designing both an appropriate experience on each channel *and*
the transitions between them. Users never think in channels and devices; to them
a journey is one holistic interaction with the organisation, and they will
neither understand nor tolerate an experience fragmented across channels
([[2016-07-24_customer-journeys-omnichannel]]).

The corpus, largely a single NN/g series, defines the concept through five
components — consistency, optimisation for context, seamlessness, orchestration
and collaboration — each of which received its own article
([[2016-07-24_customer-journeys-omnichannel]], [[2016-10-16_omnichannel-consistency]],
[[2017-02-26_context-specific-cross-channel]], [[2017-03-19_seamless-cross-channel]],
[[2020-08-16_omnichannel-orchestration]], [[2021-04-25_omnichannel-collaboration]]).
Four are treated as requirements; collaboration is explicitly optional, valuable
when present but not detrimental when absent
([[2021-04-25_omnichannel-collaboration]]). The vocabulary is precise: a
*channel* is the medium of interaction (website, app, phone, in-person, mail,
packaging); *devices* are not channels but the means of accessing them; a
*touchpoint* is a specific interaction combining a device, a channel and a task
([[2016-12-04_channels-devices-touchpoints]]). Crucially, the later sources treat
omnichannel failure as an organisational symptom rather than a design one:
fragmented experiences surface internal fragmentation, and fixing them demands
structural change ([[2019-09-15_cx-organizational-fluidity]],
[[2024-10-18_journey-centric-design]]).

## Practice

### Map the ecosystem before designing

- Identify your own channel ecosystem: which channels are bidirectional
  (websites, apps, live chat, phone, in-person) versus unidirectional (mail,
  advertising, packaging); which are device-specific (a smartwatch app) versus
  cross-device (email, live chat). Every organisation's mix differs — banks lean
  on physical locations, internet companies on digital channels
  ([[2016-12-04_channels-devices-touchpoints]]).
- Map common journeys and examine touchpoints — device, channel, task — to
  understand how customers actually use what you offer, and where the gaps are
  ([[2016-12-04_channels-devices-touchpoints]]).
- Journeys do not follow a single-channel happy path: users start, stop and
  switch. Design horizontally around journeys rather than vertically around
  channel solutions ([[2019-09-15_cx-organizational-fluidity]]).
- Use an asset map for a bounded workflow: a chronological catalogue of every
  screen, email and notification a user meets across channels, used to audit
  consistency of functionality, workflow, data, tone of voice and visual design.
  It complements a journey map — assets cover what users see, journeys cover what
  they think and feel — and works best on defined tasks (buying a product,
  checking in for a flight) rather than sprawling journeys
  ([[2021-03-14_asset-mapping]]).
- Social media is one channel inside these journeys, and often an entry point to
  others rather than the primary channel. Users discover, research, engage,
  purchase, get support and promote there, moving fluidly between those six
  modes ([[2021-01-31_companies-social-media]]).

### Consistency

- Consistency operates on three dimensions: core functionality (primary tasks
  supported on every channel with similar workflows), customer data (real-time
  and synchronised through integrated backend systems), and visual design
  (shared palette, imagery and typography telling one brand story)
  ([[2016-10-16_omnichannel-consistency]]).
- The payoff is familiarity, learnability, efficiency and trust; the cost of
  inconsistency is that users question the organisation's credibility and
  wonder whether offerings or values differ between channels
  ([[2016-10-16_omnichannel-consistency]]).
- Audit functional consistency before look and feel: if core functionality
  differs, users cannot reach their goal no matter how coherent the visuals
  ([[2021-03-14_asset-mapping]]).
- Where functionality must differ for business or strategic reasons, do not
  mislead — say so in the content and help users recover
  ([[2021-03-14_asset-mapping]]).
- Prioritise fixes by value against effort; functional inconsistencies take
  longest to fix and matter most ([[2021-03-14_asset-mapping]]).

### Optimisation for context

- Consistency and optimisation are in tension by design, and the sources resolve
  it the same way each time: keep core functionality and brand presentation
  consistent, and compromise on presentation and available features where the
  channel warrants it ([[2016-10-16_omnichannel-consistency]],
  [[2017-02-26_context-specific-cross-channel]]).
- Context has four elements to establish: the user's most important tasks, when
  and where they are done, which devices are used at which journey stage, and
  each channel's strengths ([[2017-02-26_context-specific-cross-channel]]).
- Device roles as described: desktop for complex tasks, multitasking and rich
  scannable content; mobile for microtasks, quick access and location-aware or
  urgent actions, with layered content that gives the gist first and collapses
  secondary detail; tablet for media consumption and immersive reading with
  minimal text input ([[2017-02-26_context-specific-cross-channel]]).
- Use native capabilities rather than generic screens: geolocation for store
  finders, camera for photo input, SMS for urgent alerts, biometric
  authentication ([[2017-02-26_context-specific-cross-channel]]).

### Seamlessness

- Seamlessness means zero or minimal overhead when moving between channels:
  users resume where they left off without re-establishing context or redoing
  work ([[2017-03-19_seamless-cross-channel]]).
- Users switch channels for three reasons: an external interruption, a task
  better suited to another channel, or a task that inherently requires several
  channels ([[2017-03-19_seamless-cross-channel]]).
- The failure mechanism is interaction cost: once the effort of completing a
  task exceeds its perceived value, users abandon the task or the brand, now or
  later ([[2017-03-19_seamless-cross-channel]]).
- Concrete tactics: make resumption easy (authentication, email links,
  passcodes, OS handoff), give users a sandbox that stores progress (wishlists,
  save-for-later, recently viewed), and proactively surface the next step
  ([[2017-03-19_seamless-cross-channel]]).
- Typical roadblocks to hunt for: scanning failures, incompatible systems,
  missing next-step instructions, and no fallback when the primary workflow
  breaks ([[2017-03-19_seamless-cross-channel]]).
- Seamless frontends usually require backend integration; silos between online
  and offline systems are the root of most cross-channel roadblocks
  ([[2017-03-19_seamless-cross-channel]], [[2016-09-11_customer-service-omnichannel-ux]]).

### Orchestration

- Orchestration is the discreet planning and coordination of a journey to
  minimise the user's effort on future actions — predicting the next need and
  meeting it before the user has formulated it
  ([[2020-08-16_omnichannel-orchestration]]).
- Three levels, in increasing sophistication: level one automates a common
  linear journey with no customer data at all, needing only thoughtful service
  design; level two personalises for segments using customer data; level three
  uses journey-orchestration engines and AI for real-time personalisation of
  granular segments. You do not need advanced data infrastructure to start
  ([[2020-08-16_omnichannel-orchestration]]).
- Monitor the analytics and conversion of speculative nudges, and discontinue
  the ones few customers accept ([[2020-08-16_omnichannel-orchestration]]).
- Journey-centric operations are what make AI-driven personalisation at scale
  feasible, because they establish the data foundation and analytics
  infrastructure ([[2024-10-18_journey-centric-design]]).

### Collaboration

- Collaboration is two or more normally separate devices or channels used
  together for one goal, with a *target* channel where the task happens and a
  *helper* channel supplying a resource
  ([[2021-04-25_omnichannel-collaboration]]).
- It works in two ways: reducing interaction cost by borrowing a resource (a
  phone scanning a QR code to log into a desktop client), or adding capability
  outright (using a phone camera to insert a photo into a laptop presentation)
  ([[2021-04-25_omnichannel-collaboration]]).
- Paired or physically nearby devices — smart appliances, streaming services,
  productivity suites — are the natural openings
  ([[2021-04-25_omnichannel-collaboration]]).
- Cross-ecosystem collaboration remains rare and inconsistent, since the pattern
  only pays off once most apps support it
  ([[2021-04-25_omnichannel-collaboration]]).

### Bridging digital and physical

- Shoppers do not distinguish online from in-store; showrooming (inspect in
  store, buy online) and webrooming (research online, buy in store) are
  established behaviours ([[2018-10-28_changing-shopper-behaviors]]).
- Every transition between online and offline is a chance to lose the sale, so
  either remove the transition or make it easy. Comprehensive product
  information — high-quality photography, close-ups, detailed descriptions,
  robust reviews — removes the need for a store visit; confirmation emails with
  directions, parking information and what to bring support the transition when
  it is unavoidable ([[2018-10-28_changing-shopper-behaviors]]).
- Physical stores remain valuable as discovery and testing spaces, integrated
  with digital options for comparison and wider selection
  ([[2018-10-28_changing-shopper-behaviors]]).
- Store locators must be easy at all three steps: finding the locator link,
  finding the location, and getting directions. Success rates rose from 63% to
  97% over 18 years, yet 40% of users still hit difficulty. Offer current
  location through a discoverable button rather than hiding it behind a
  permission dialog, and link out to familiar mapping platforms instead of
  building a proprietary map — 80% of users go straight to a search engine or
  maps app anyway ([[2018-10-07_store-finders-and-locators]]).
- QR codes are an omnichannel primitive: an offline index into online content
  that avoids mobile typing, a way of attaching information to physical objects,
  and a validation mechanism. Their adoption in China rested on usefulness, ease
  of use and discoverability together — scanning embedded in an app people
  already used, tied to valued features and reinforced by a mass campaign with
  financial reward. Their weakness is information scent: a QR code looks
  meaningless without explanation ([[2016-10-16_wechat-qr-shake]]).
- An integrated platform can make the bridge itself the product. WeChat's draw
  was convenience, not conversation — payments made up 32% of logged activity,
  official accounts shared a standardised interaction style that reduced
  cognitive load, and users still went to traditional websites for complex tasks
  ([[2016-08-21_wechat-integrated-ux]]).
- Cross-device and cross-channel consistency is part of why disruptive services
  spread: it lets people complete the task from wherever they are, backed by
  backend operations that improve the visible experience
  ([[2017-02-19_3-user-experiences-reshaping-industries]]).

### Support channels as part of the journey

- Contacting customer service is itself a UX failure. Of 45 journeys studied,
  64% required at least one contact, meaning only about a third could be
  completed online unaided ([[2016-09-11_customer-service-omnichannel-ux]]).
- The four triggers are service problems, roadblocks, missing or confusing
  information, and perceived complexity — with missing or ambiguous information
  the largest at 38% of contacts
  ([[2016-09-11_customer-service-omnichannel-ux]]).
- The prescription is to eliminate the *need* for customer service, never the
  service itself: do not hide contact details, offer several channels for
  different urgencies, and make them easy to reach
  ([[2016-09-11_customer-service-omnichannel-ux]]).
- Never create circular routing — a website that sends people to a phone tree
  and a phone tree that sends them back to the website. Callers reach the phone
  as a last resort and value autonomy, so feeling trapped compounds an already
  failed self-service attempt ([[2022-08-14_phone-tree-guidelines]]).
- Interruptions and channel switching, digital to human or otherwise, degrade
  the experience and over time damage satisfaction, loyalty and the bottom line
  ([[2016-09-11_customer-service-omnichannel-ux]]).

### The organisational condition

- Omnichannel maturity is a ladder, and each rung — consistent branding,
  optimised channels, seamless transitions, personalised orchestration,
  collaborative use — demands deeper organisational change
  ([[2019-09-15_cx-organizational-fluidity]]).
- Interaction-level fixes need little coordination; journey-level ones require
  cross-department alignment of process, technology and people that are usually
  siloed. When marketing, product and support each work their own channel, users
  feel the disconnect ([[2019-09-15_cx-organizational-fluidity]]).
- Treating individual pain points without restructuring produces the same
  problems again; the root causes are structural
  ([[2019-09-15_cx-organizational-fluidity]]).
- Digitally native companies have this maturity by construction; established
  companies must deliberately redesign legacy structures and technology
  ([[2019-09-15_cx-organizational-fluidity]]).
- Journey-centric design is the operational answer proposed later: rather than
  dismantling silos, which is near-impossible, build connectivity across them
  with cross-functional structures organised around specific journeys. It adds a
  layer of journey strategy over product teams rather than replacing product
  design, and it unlocks end-to-end journey analytics that measure design's
  actual business impact better than product-level metrics
  ([[2024-10-18_journey-centric-design]]).
- Involve channel-dedicated teams and other departments early when you surface
  inconsistencies, before proposing solutions — it builds buy-in and breaks down
  silos ([[2021-03-14_asset-mapping]]).

## Sources (19)

- [[2016-07-24_customer-journeys-omnichannel]] — Omnichannel design integrates experiences across channels, ensuring consistency, seamlessness, and personalization throughout the customer journey, while optimizing for each channel's specific context and constraints.
- [[2016-08-21_wechat-integrated-ux]] — Illustrates integration across physical and digital channels through QR codes and seamless payment, creating a consistent experience that bridges online and offline.
- [[2016-09-11_customer-service-omnichannel-ux]] — Defines consistency, information continuity, and seamless channel transitions as essential to reducing service contact and improving self-service completion rates.
- [[2016-10-16_omnichannel-consistency]] — Defines consistency alongside context optimization, seamlessness, orchestration, and collaboration as critical components for successful multichannel customer experience, while emphasizing the need to balance consistency in primary workflows and brand presentation against optimization for each channel's unique affordances and user context.
- [[2016-10-16_wechat-qr-shake]] — Illustrates how QR and shake bridge online-offline worlds, enabling context-aware interactions, offline-to-online transitions, and seamless cross-device handoff (omnichannel UX).
- [[2016-12-04_channels-devices-touchpoints]] — Organizations must design across their full channel ecosystem rather than optimizing individual devices; consistency and continuity across channels improve customer experience.
- [[2017-02-19_3-user-experiences-reshaping-industries]] — cross-device and cross-channel consistency enable users to complete tasks from any location.
- [[2017-02-26_context-specific-cross-channel]] — consistency in core functionality and look/feel across channels enables learnable, efficient experiences as part of broader cross-channel design principles and components.
- [[2017-03-19_seamless-cross-channel]] — Defines seamlessness as one of five key elements (alongside consistency, context optimization, orchestration, and collaboration) necessary for a usable omnichannel strategy.
- [[2018-10-07_store-finders-and-locators]] — users' expectation that they can research products online and purchase in-store, or vice versa, requiring seamless experience across digital and physical touchpoints.
- [[2018-10-28_changing-shopper-behaviors]] — the integration of online and offline channels to create a seamless customer experience across touchpoints and reducing friction in channel transitions.
- [[2019-09-15_cx-organizational-fluidity]] — Omnichannel maturity requires consistent branding, optimized channel experiences, seamless transitions, personalized orchestration, and collaborative channel use; each level demands deeper organizational change.
- [[2020-08-16_omnichannel-orchestration]] — Orchestration is one of five key attributes of high-quality omnichannel experiences, alongside consistency, context optimization, seamlessness, and collaboration across touchpoints.
- [[2021-01-31_companies-social-media]] — demonstrates how social media functions as one channel within broader customer journeys that span multiple touchpoints.
- [[2021-03-14_asset-mapping]] — the article addresses consistency across multiple channels and touchpoints in omnichannel experiences.
- [[2021-04-25_omnichannel-collaboration]] — Collaboration is one of five key elements of high-quality omnichannel customer experiences, enabled through design patterns and interactions that span multiple channels and devices.
- [[2022-08-14_phone-tree-guidelines]] — Phone systems are part of broader customer journeys; avoid sending website visitors to phone trees and vice versa, creating circular frustration instead of seamless support.
- [[2024-10-18_journey-centric-design]] — the design of consistent, integrated experiences across multiple channels and touchpoints (web, mobile, in-person, etc.) that customers use to interact with a brand.
- [[2019-12-17_storytelling-in-design_04-chapter-3-storytelling-for-product-design]] — Dahlström opens the section on the analogy that "in a well-told story, everything from big to small details comes together," then defines omnichannel experiences as cross-channel experiences spanning social media, physical locations, ecommerce, mobile apps and desktops. Online and offline increasingly merge; companies that optimize so users move seamlessly across channels gain a competitive advantage, in higher conversion and increased brand loyalty.
