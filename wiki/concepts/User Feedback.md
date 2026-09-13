---
type: concept
name: User Feedback
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Feedback in-app"
  - "In-App Feedback"
---

# User Feedback

## Definition

The sources gathered here use "feedback" in two directions, and the page keeps
both. In one direction it is feedback the product gives the user: system status,
progress indicators, confirmations, and error messages that let people
understand what happened and fix it
[[2019-02-03_errors-forms-design-guidelines]],
[[2021-07-11_usability-heuristics-virtual-reality]]. In the other it is feedback
the user gives the product: voice-of-customer programmes, in-app micro-surveys
and feedback requests that inform design decisions
[[2023-03-26_user-feedback]], [[2024-11-26_353_3_outils_pour_accélérer_son_Product_Market_Fit]],
[[2026-04-07_408_Les_3_façons_de_mesurer_l_impact_du_design_-_Guide_complet]].

What the two senses share is a concern with timing and context. Error feedback
should appear as soon as the field is filled and next to the field concerned
[[2019-02-03_errors-forms-design-guidelines]]; feedback requests should come
after a real task, in the channel where the interaction happened
[[2023-03-26_user-feedback]]. In both cases the alternative — delayed, generic,
displaced feedback — costs the user effort and costs the team reliable
information.

## Practice

### Feedback the system gives: errors in forms

- Use inline validation so errors surface as soon as a field is completed,
  letting users fix mistakes immediately instead of hunting for the offending
  field [[2019-02-03_errors-forms-design-guidelines]].
- For fields with specific requirements such as passwords, show real-time
  success indicators as users type so they can meet the rules without trial and
  error [[2019-02-03_errors-forms-design-guidelines]].
- Keep the message adjacent to the field in error: this minimises working-memory
  load, since users can read the message while fixing the problem instead of
  memorising it [[2019-02-03_errors-forms-design-guidelines]].
- Combine red colouring, background highlights and icons so errors are scannable,
  which matters particularly for users with colour blindness
  [[2019-02-03_errors-forms-design-guidelines]].
- Do not report errors in tooltips: hiding the message behind hover or focus
  makes it hard to notice and costs extra effort to retrieve
  [[2019-02-03_errors-forms-design-guidelines]].
- Treat repetition as a signal: the same error three or more times in one
  form-filling attempt indicates a deeper interface problem — unclear messaging,
  a mismatch with user needs, or over-complex requirements — and calls for design
  review, not just better wording
  [[2019-02-03_errors-forms-design-guidelines]].
- The overall goal is that an error flow lets users fix their mistakes and
  continue with their task [[2019-02-03_errors-forms-design-guidelines]].

### Feedback the system gives: visibility of status

- Visibility of system status through appropriate feedback — battery life,
  progress, confirmations — builds trust and lets users make informed decisions
  about their interaction [[2021-07-11_usability-heuristics-virtual-reality]].
- The need intensifies in VR because a headset reduces environmental awareness,
  so the system must supply what the user can no longer perceive directly
  [[2021-07-11_usability-heuristics-virtual-reality]].
- In the same setting, prevention beats recovery: warnings and confirmations,
  such as alerting users when their physical play space is smaller than
  recommended, are more effective than error messages after the fact
  [[2021-07-11_usability-heuristics-virtual-reality]].

### Feedback the user gives: when to ask

- Task, then ask. Requesting feedback before users have interacted skews results;
  asking after a completed task, while the experience is fresh, produces
  meaningful feedback [[2023-03-26_user-feedback]].
- Keep the request subtle and non-obstructive, and pair it with an always-present
  on-demand route such as a small feedback tab, so users can respond when ready
  or after dismissing the first prompt [[2023-03-26_user-feedback]].
- Avoid intrusive popups on page arrival and mid-workflow interruptions: they
  reduce honest feedback [[2023-03-26_user-feedback]].
- Placement inside the product matters as much as timing: micro-surveys embedded
  at strategic moments, for example when a user abandons a payment step, reveal
  the real reasons behind a choice rather than a bare satisfaction score
  [[2024-11-26_353_3_outils_pour_accélérer_son_Product_Market_Fit]].

### Feedback the user gives: how to ask

- Ask in the channel where the interaction happened — push notification, in-app
  message, SMS — rather than defaulting to email, because users are already
  flooded with feedback-request emails [[2023-03-26_user-feedback]].
- Better still, let people choose the format: some find push less intrusive than
  a cluttered inbox, others the reverse. Offering a choice across email, push,
  SMS, call or social media raises participation compared with a single channel
  [[2023-03-26_user-feedback]].
- Keep surveys short, and make the question specific to the task just completed —
  "Tell us about your cancellation experience" beats a generic satisfaction
  question [[2023-03-26_user-feedback]].
- Match the tone to the user's emotional state: a cheerful request during
  something like tax filing reads as tone-deaf and erodes trust
  [[2023-03-26_user-feedback]].
- Appreciate participants for their time [[2023-03-26_user-feedback]].
- A workable in-app form combines a numeric score (CSAT or NPS) with a free-text
  comment, kept tightly targeted and contextualised
  [[2026-04-07_408_Les_3_façons_de_mesurer_l_impact_du_design_-_Guide_complet]].

### What qualitative feedback is good for, and its limits

- Direct qualitative feedback is the most intuitive way to measure customer
  experience and yields striking verbatims, but it is presented as only the first
  of three levels: it must be complemented by product analytics across the whole
  user base, and ultimately connected to business metrics such as revenue,
  margin and churn
  [[2026-04-07_408_Les_3_façons_de_mesurer_l_impact_du_design_-_Guide_complet]].
- The same reasoning appears in the product-market-fit context: contextual
  qualitative feedback sits alongside search-volume validation before building
  and behavioural analysis afterwards (funnels, heatmaps, session recording),
  which need a minimum of traffic to be representative
  [[2024-11-26_353_3_outils_pour_accélérer_son_Product_Market_Fit]].
- That source also warns against over-reading feedback too early: the biggest
  risk is scattering, trying to answer everything too generally and optimising
  flows in detail while the open question is still whether the product answers a
  real need at all
  [[2024-11-26_353_3_outils_pour_accélérer_son_Product_Market_Fit]].

## Sources (5)

- [[2019-02-03_errors-forms-design-guidelines]] — Strategies for communicating system status to users through error messages that are explicit, human-readable, polite, precise, and constructive.
- [[2021-07-11_usability-heuristics-virtual-reality]] — Clear system feedback (battery status, progress indicators, confirmations) is essential in VR to compensate for the reduced environmental awareness users have while wearing a headset.
- [[2023-03-26_user-feedback]] — effective user feedback collection requires timing requests after task completion, using contextually relevant channels, and offering flexible feedback formats.
- [[2024-11-26_353_3_outils_pour_accélérer_son_Product_Market_Fit]]
- [[2026-04-07_408_Les_3_façons_de_mesurer_l_impact_du_design_-_Guide_complet]]
