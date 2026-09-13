---
type: concept
name: Notification Design
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Notifications"
---

# Notification Design

## Definition

Notification design covers the choices behind any alert a product sends to
interrupt someone: what it says, when it arrives, on which channel, how loudly,
how often, and how easily it can be turned off. The sources treat notifications
as the sharpest point of contact between a product's interests and a user's
attention. Done well, they inform, build trust and demonstrate respect for the
user's time [[2026-02-20_smart-home-notifications]]; done badly they annoy,
cause fatigue, and drive users to disable all communication or delete the app
outright [[2018-11-18_push-notification]],
[[2022-11-06_transactional-notifications]].

The corpus also frames notifications as an ethics problem, not only a craft
problem. They are identified as the primary trigger of "the Vortex" — a chain of
unplanned interactions that starts with one intentional one — because they
interrupt focus and create an obligation to check and respond
[[2018-10-28_device-vortex]]. The volume is part of the problem: an average
mobile user received 56 notifications per day in 2016
[[2018-11-18_push-notification]]. Across sources the governing idea is the same:
the goal is not to communicate more but to communicate better
[[2026-02-20_smart-home-notifications]].

## Practice

### Classify before designing

Notifications are not one category. Transactional notifications convey
information about an existing order or the customer-company relationship, as
opposed to marketing notifications meant to persuade
[[2022-11-06_transactional-notifications]]. In the smart-home context three
types are distinguished — reactive (immediate action needed), proactive
(upcoming event, prepare) and optimization (efficiency suggestion) — each
demanding different timing, intensity and channel
[[2026-02-20_smart-home-notifications]]. Organising notifications by type,
urgency and impact is what lets users tell apart what needs acting on now from
what can wait [[2026-02-20_smart-home-notifications]].

### Timing and relevance

- Match the delay to the type: instantly and in real time for reactive alerts,
  in advance but not so early that users forget for proactive ones, and at a
  moment of relevant use for optimization suggestions
  [[2026-02-20_smart-home-notifications]].
- Reserve notifications for genuinely urgent, time-sensitive content
  (deliveries, payment alerts); extraneous ones cause frustration
  [[2022-11-06_transactional-notifications]].
- Send alerts for the product's core purpose only by default, let alerts expire
  automatically when the issue is resolved, and flag when a problem resolved
  itself [[2026-02-20_smart-home-notifications]].
- Send only content relevant to the individual. Irrelevant interruptions are
  especially frustrating when users feel obliged to clear them, and
  personalisation matters all the more because most users never change default
  settings [[2018-11-18_push-notification]].
- Relevance intolerance rises with the intimacy of the device: on a smartwatch
  users act as a filter and tolerate irrelevant information far less than
  anywhere else, so notifications there must be informative, glanceable,
  personalised and timely [[2023-11-17_smartwatch-interactions]].

### Content and length

- Give the headline a clear purpose summary and keep the body concise;
  conciseness itself signals that the company respects the user's time
  [[2022-11-06_transactional-notifications]].
- Constraints are tighter than email: push notifications run to roughly 50–240
  characters with minimal formatting, so key information must be frontloaded
  because users scan only the first few words
  [[2022-11-06_transactional-notifications]].
- Be specific rather than vague: answer what, why and when without forcing the
  user to open the app — "Person detected at front door" beats "Motion
  detected" [[2026-02-20_smart-home-notifications]].
- On a smartwatch, message content is critical because typing is tedious and
  dictation error-prone; users rely on the watch for comprehensive awareness of
  incoming communications, so enough content must be displayed
  [[2023-11-17_smartwatch-interactions]].

### Intensity, frequency and fatigue

- Match visual and audio cues to urgency — red and strong alerts for critical,
  yellow for moderate, subtle for low priority — and keep that mapping
  consistent across devices [[2026-02-20_smart-home-notifications]].
- Avoid bursts of notifications in a short timeframe: sequences overwhelm users,
  look sloppy and prompt app deletion. Combine related notifications into a
  single message, quality over quantity [[2018-11-18_push-notification]].
- Offer event thresholds (notify at 20% battery, not 50%), event-type filtering
  (people only, not insects) and repeat intervals, and separate discrete events
  from ongoing conditions [[2026-02-20_smart-home-notifications]].
- Too many notifications push users to disable all communication with the
  organisation [[2022-11-06_transactional-notifications]].

### Channel choice

- Push suits nonurgent, app-specific content: reminders to return to an app
  (abandoned cart), suggestions, nonurgent status updates
  [[2022-11-06_transactional-notifications]]. Smart-home guidance agrees on the
  split by urgency but assigns push to the urgent end and in-app to the
  nonurgent one [[2026-02-20_smart-home-notifications]] — the two sources are
  describing different channel sets (SMS vs push on one side, push vs in-app on
  the other), so read the principle as "match channel to urgency" rather than as
  a fixed ranking of push.
- SMS is stable and durable, so it fits information users must retain or act on
  quickly: pickup codes, delivery details, order changes, confirmation requests
  [[2022-11-06_transactional-notifications]].
- Channel preference is cultural: Chinese users have historically favoured SMS
  where Western users prefer email [[2022-11-06_transactional-notifications]].
- Smart-home apps span push, in-app, email, SMS and on-device channels, and the
  choice among them should follow urgency [[2026-02-20_smart-home-notifications]].

### Permission, control and opt-out

- Do not request notification permission on first launch: users don't trust a
  new app and decline without understanding the value. Let them experience the
  app first and ask in a later session, using the reciprocity principle
  [[2018-11-18_push-notification]].
- Say what the notifications will be about. Generic system prompts carry no
  information; naming the content types lets users decide and raises perceived
  credibility and transparency [[2018-11-18_push-notification]].
- Make disabling easy and obvious, inside the app's own settings rather than
  buried in global device settings; hiding them decreases trust
  [[2018-11-18_push-notification]]. Users should be able to opt out from
  specific channels rather than all at once
  [[2022-11-06_transactional-notifications]].
- Give granular control over types, thresholds, channels and timing, plus snooze
  options and adaptability to changing contexts; without it users abandon the
  whole notification system [[2026-02-20_smart-home-notifications]].

### The ethical line

Notifications interrupt focus and prime further engagement; even ignored, they
are often checked later and lead to unplanned extended usage
[[2018-10-28_device-vortex]]. That source frames this as a design
responsibility: persuasive technique is not wrong in itself, but it must not
cross into manipulation that leaves users feeling out of control or acting
against their own interests. The push-notification guidance reaches the same
conclusion from the business side — retention matters, but making users feel
manipulated backfires, and respecting autonomy is what builds long-term trust
and loyalty [[2018-11-18_push-notification]].

## Sources (5)

- [[2018-10-28_device-vortex]] — how alert mechanisms serve as triggers for the Vortex by interrupting focus and creating obligation to check and respond to messages.
- [[2018-11-18_push-notification]] — how alert design choices impact user engagement and whether users feel informed or manipulated by app communications.
- [[2022-11-06_transactional-notifications]] — transactional notifications must be concise, timely, and carry essential information only; both SMS and push notifications have specific use cases and require different strategies.
- [[2023-11-17_smartwatch-interactions]] — notifications are the most common smartwatch interaction and must be informative, timely, and personalized to avoid being intrusive.
- [[2026-02-20_smart-home-notifications]] — Seven principles ensure notifications remain useful: timing, relevance, specificity, intensity, frequency, channel, and adaptability prevent fatigue while keeping users informed.
