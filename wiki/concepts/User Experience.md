---
type: concept
name: User Experience
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Integrated User Experience"
  - "UX"
  - "UX Design"
  - "User Experience (UX)"
  - "User Experience Analysis"
  - "User Experience Definition"
  - "User Experience Degradation"
  - "User Experience Design"
---

# User Experience

## Definition

User experience is the holistic relationship — perceptions, emotions and
interactions — between a person and a product, service or company. The term was
coined by Don Norman in the 1990s, and the field that grew from it is a
professional practice focused on designing and enhancing that overall experience
for all users of a product, service or brand [[2024-11-15_what-is-user-experience]].
It is deliberately broader than the concepts it is often confused with: usability
is a critical component of UX but is scoped to task efficiency, while user
interface names the components and design elements that enable interaction; UX
covers all touchpoints, entire ecosystems and journeys, and is not limited to
websites or applications [[2024-11-15_what-is-user-experience]]. Read as a
touchpoint set, UX is what users actually encounter — the app, the website, the
kiosk, the mailer — and is the external manifestation of the service design
that organises the people, processes and technology behind it
[[2021-08-08_ux-vs-service-design]].

Because customers now interact with companies mostly through interfaces, the
experience and the brand have become hard to separate: brand is the sum of a
person's experiences with a product or company, expressed through visuals, tone
and behaviour, which makes UX the differentiator when people cannot distinguish
how they feel about a brand from how they feel about using it
[[2016-07-03_brand-experience-ux]]. The sources also treat good UX as a business
imperative rather than a nice-to-have, tied to reduced support costs and
increased conversions, and note that many organisations still sit in the bottom
half of the UX-maturity scale and cut UX first when budgets tighten
[[2024-11-15_what-is-user-experience]].

## Practice

### Usability first, delight after

Delight is one layer of a hierarchy, not a substitute for the layers under it:
functionality is essential, reliability keeps usability meaningful, and only then
can pleasure be appreciated; surface delight (animations, microcopy, imagery)
layered onto an unusable interface reads as non-genuine and can harm brand trust
[[2017-03-05_theory-user-delight]]. Deep delight — the interface handing users
what they need without getting in the way — requires streamlined workflows and
reduced pain points, and is much rarer [[2017-03-05_theory-user-delight]].
Negativity bias compounds this: users remember bad experiences more than good
ones [[2017-03-05_theory-user-delight]].

The same fundamentals hold outside productivity software. Nielsen's usability
heuristics apply to video games as well as to websites and apps: entertainment
products benefit from visibility of system status, user control, consistency,
error prevention and recognition over recall just as work tools do
[[2019-05-19_usability-heuristics-applied-video-games]]. Error handling is part
of the experience rather than an edge case — errors displayed near their source,
written in plain language, offering a constructive remedy and avoiding blame
make mistakes feel manageable [[2023-05-15_error-message-guidelines]].
Perceptual and cognitive principles feed the same goal: containers create
groupings that let users read interface structure at a glance, though overusing
them adds clutter and false floors [[2020-07-12_common-region]]; and visuals are
remembered better than words, so placement, literal imagery and distinctiveness
improve overall impression and decision-making [[2024-04-26_picture-superiority-effect]].

### Reliability and accumulated friction

Convenience that is not reliable is not convenience. Streaming went from a
revolutionary improvement to a frustrating experience through accumulated
friction — password resets, forced ads, app updates, premium-tier bloat,
deceptive consent flows on smart TVs — to the point that physical discs feel
pleasant by comparison [[2025-09-12_physical-discs-streaming-experience]].
Cross-device complexity is a specific source of that decay: separate sign-ins,
updates and subscription management per device turn a seamless multi-device
promise into work [[2025-09-12_physical-discs-streaming-experience]]. Navigation
choices erode the experience in a measurable way too: hidden navigation such as
hamburger menus produced longer task times, higher perceived difficulty and a
drop in content discoverability, especially on desktop, and it mostly affects
content not reachable through in-page links [[2016-06-26_hamburger-menus]].

### Respecting user intent and control

Several sources converge on the same failure mode: optimising a local metric at
the expense of the relationship. Needy patterns — please-don't-go popups,
attention-seeking tab titles — chase signups and page views while slowing users
down, signalling organisational desperation and damaging credibility
[[2016-05-15_needy-design-patterns]]. Aggressive advertising works the same way:
ads that force interaction, delay the primary content, appear unpredictably or
target too precisely damage trust even when the surrounding content is good
[[2017-07-16_user-requirements-online-ads]]. Exits deserve as much care as
entries — an unsubscribe should be a one-click, clearly labelled, friction-free
process, since blocking it pushes users to report the mail as spam and costs
long-term brand perception [[2018-04-29_unsubscribe-mistakes]]. In conversational
products, the experience hinges on whether the bot respects user choice (handing
off to a human on request), adapts to the user's direction, acknowledges their
situation without pretending to feel, and is honest about its limitations and
data practices [[2026-07-10_dimensions-of-ai-chatbots]].

### Designing for the medium and the context

Mobile is a medium of its own, not a smaller desktop: designs should prioritise
location-based, time-sensitive and emergency information, integrate device
capabilities such as camera, GPS and biometrics, and pursue experiences that are
only possible because the device is portable and contextual
[[2017-10-15_better-mobile]]. This is the same argument that warns against
carrying a mobile navigation pattern onto desktop without questioning it
[[2016-06-26_hamburger-menus]]. In augmented reality, the experience depends on
balancing UI controls against immersion: overlays should be minimisable,
interactions should be self-sufficient inside the AR scene, and audio narration
and gesture controls help — but AR should never be added for its own sake
[[2022-11-20_ar-ux-guidelines]]. Reusing a gesture already anchored in habit can
do the same work: Arc's Call Arc launches an AI conversation by raising the phone
to the ear, which makes a new technology immediately legible to a non-technical
audience [[2024-05-28_330_Call_Arc,_l_interface_ChatGPT_parfaite_-_Analyse_Product_Design]].

Integration is its own experience quality. WeChat's advantage comes from
payments, ecommerce, social and official accounts reinforcing each other in one
place, with a standardised interaction style across accounts; users named
convenience, not conversation, as the reason they use it, and they still fall
back to traditional websites for complex tasks
[[2016-08-21_wechat-integrated-ux]]. That source also notes that new platforms
inherit old usability problems, because usability is determined by the human mind
and people's needs rather than by the technology
[[2016-08-21_wechat-integrated-ux]].

### The experience extends past the interface

UX cannot be delivered by the interface layer alone. Poor internal processes,
understaffing and unintegrated systems degrade the customer experience directly —
long waits, re-explaining an issue to successive agents — which is why service
design (the "how") and UX (the "what") are described as two sides of the same
coin, with service blueprints revealing where internal weaknesses surface as
customer pain [[2021-08-08_ux-vs-service-design]]. Automation does not escape
this: an unmanned restaurant that automates the surface without redesigning the
operation underneath produces new problems (out-of-stock ordering, no
customisation, group ordering, single payment method), and accessibility,
personalisation and human warmth remain irreplaceable — less human help does not
by itself mean a better experience [[2022-06-19_unmanned-restaurant-case-study]].
On the brand side, consistency of visuals, tone and behaviour across every
channel is what makes the experience coherent, and interaction details down to
transitions communicate professionalism and competence
[[2016-07-03_brand-experience-ux]].

### Diagnosing and improving an existing experience

A customer-journey map becomes useful when it is analysed rather than merely
drawn. Seven lenses are offered: expectation mismatches, unnecessary touchpoints
to remove interaction cost, low-point friction (weighted by the peak-end rule,
since the lowest point disproportionately damages the branding effect of the
experience), high-friction channel or device transitions, time spent per stage,
moments of truth where the whole experience can hinge on one interaction, and
high points worth amplifying elsewhere [[2020-03-22_analyze-customer-journey-map]].

### The discipline under business and AI pressure

Two Parlons Design episodes describe a shift in how the work is practised. UX is
presented as the strongest source of a product designer's value — user contact,
surfacing problems before they appear, reducing risk before development — but it
has to become less procedural and closer to the ground: calibrate the level of
certainty to the risk, prototype fast, gather client feedback often, and accept
that defending the end user exclusively is no longer tenable when buyers and the
company's own business constraints are in play
[[2025-09-16_395_L_UX_Design_est_mort_L_impact_de_l_IA_&_du_business_sur_le_métier_de_designer]].
The same source argues designers must get their hands into the technology,
including AI APIs and LLMs, to turn a commoditised technology into differentiated
value [[2025-09-16_395_L_UX_Design_est_mort_L_impact_de_l_IA_&_du_business_sur_le_métier_de_designer]].
A related episode makes the technical-culture point directly: understanding
application logic, databases and how code works lets designers anticipate edge
cases and build more robust user journeys, and the market is moving from a
purely theoretical or mockup-bound UX practice toward hybrid "product builder"
profiles [[2024-10-08_349_L_IA_dans_le_design_usages_concrets_et_avenir_avec_Romain_Dao]].
These two sit in tension with the strand of the corpus that treats UX as a
holistic, user-first practice that should exist in every department
[[2024-11-15_what-is-user-experience]]: they do not deny it, but they push the
balance toward business viability and delivery rather than toward orthodoxy.

## Sources (24)

- [[2016-05-15_needy-design-patterns]] — Needy patterns prioritize short-term metrics (signups, page views) at the expense of overall user experience and relationship quality.
- [[2016-06-26_hamburger-menus]] — Users take longer and encounter higher difficulty with hidden navigation, and hidden navigation mostly affects content not directly accessible through in-page links.
- [[2016-07-03_brand-experience-ux]] — User experience is now inseparable from brand perception; customers judge brands largely by their interactive experiences.
- [[2016-08-21_wechat-integrated-ux]] — Demonstrates how multiple services (payments, ecommerce, social, accounts) working together create convenience and competitive advantage over individual point solutions.
- [[2017-03-05_theory-user-delight]] — delight is just one layer of the overall experience pyramid; functionality, reliability, and usability must precede emotional design.
- [[2017-07-16_user-requirements-online-ads]] — how ad design choices impact brand perception and customer relationships; overly aggressive ads damage trust even when content is high-quality.
- [[2017-10-15_better-mobile]] — emphasizes designing for mobile-specific user contexts and needs rather than porting desktop experiences.
- [[2018-04-29_unsubscribe-mistakes]] — respecting user intent at critical moments and removing friction from exits to maintain long-term brand perception.
- [[2019-05-19_usability-heuristics-applied-video-games]] — Entertainment products and productivity applications both benefit from clarity, control, consistency, and error prevention; usability improves experience in both domains.
- [[2020-03-22_analyze-customer-journey-map]] — demonstrates seven distinct analytical approaches to move beyond descriptive mapping toward problem identification and opportunity assessment.
- [[2020-07-12_common-region]] — practical applications of common region in cards, accordions, navigation, and content organization.
- [[2021-08-08_ux-vs-service-design]] — User experience encompasses all aspects of user interaction with a company, including the app, website, kiosk, or mailer—the tangible touchpoints users encounter; it is the external manifestation of service design.
- [[2022-06-19_unmanned-restaurant-case-study]] — Efficiency alone does not define good UX; accessibility, personalization, and human connection remain valuable and irreplaceable in service contexts.
- [[2022-11-20_ar-ux-guidelines]] — balancing UI controls with immersive experience is critical; overlays should be minimizable; users benefit from audio narration, gesture-based controls, and self-sufficient interactions within the AR scene.
- [[2023-05-15_error-message-guidelines]] — Creating experiences where even mistakes feel manageable, using visibility, communication, and efficiency principles to reduce frustration.
- [[2024-04-26_picture-superiority-effect]] — demonstrates how leverage of cognitive effects improves overall user impression and decision-making.
- [[2024-05-28_330_Call_Arc,_l_interface_ChatGPT_parfaite_-_Analyse_Product_Design]]
- [[2024-10-08_349_L_IA_dans_le_design_usages_concrets_et_avenir_avec_Romain_Dao]]
- [[2024-11-15_what-is-user-experience]] — Provides a comprehensive definition of UX as coined by Don Norman, covering the holistic relationship and interactions between people and products/services over time.
- [[2025-09-12_physical-discs-streaming-experience]] — Documents how streaming went from revolutionary improvement to frustrating experience through accumulated friction: password resets, forced ads, app updates, premium tier bloat, and deceptive patterns.
- [[2025-09-16_395_L_UX_Design_est_mort_L_impact_de_l_IA_&_du_business_sur_le_métier_de_designer]]
- [[2026-07-10_dimensions-of-ai-chatbots]] — is shaped by whether the chatbot respects user choice, adapts to their needs, acknowledges their situation, and communicates honestly about its limitations.
- [[2024-01-23_laws-of-ux_02-a-brief-history-of-psychology-and-design]] — A discipline that emerged from HCI alongside the web, emphasizing design that encompasses all aspects of the user's interaction with a system; pioneered by Donald Norman and Jane Fulton Suri to center on human needs and psychological insights.
- [[2024-01-23_laws-of-ux_08-6-peakend-rule]] — The holistic evaluation of experiences depends on emotional memory rather than chronological sum, reshaping how product success is measured.
