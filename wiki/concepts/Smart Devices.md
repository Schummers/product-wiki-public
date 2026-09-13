---
type: concept
name: Smart Devices
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "IoT and Smart Devices"
  - "Smartwatch Design"
---

# Smart Devices

## Definition

Smart devices, in this corpus, cover two families that share a design problem:
wearables such as smartwatches, and connected home devices controlled through a
companion app. What unites them is that the interface is never the whole
experience. On a smartwatch, the screen is tiny and input methods are limited,
so users prefer brief and simple interactions and whole categories of behaviour
common elsewhere — consuming, browsing — are rarely useful
[[2023-11-17_smartwatch-interactions]]. In the smart home, the device being
controlled is physical and often out of sight, so status changes may be
invisible and feedback delayed, which is what shapes every recommendation
[[2025-09-05_smart-device-best-practices]].

The companion app is therefore framed not as a remote control but as a control
hub: it is what unlocks the device's full potential through advanced settings,
automations, multi-device coordination and information-rich dashboards
[[2025-09-05_smart-device-best-practices]]. Because these devices are personal
and physically present, trust is a recurring theme — well-designed alerts and
honest feedback foster confidence in the device and demonstrate respect for the
user's attention [[2026-02-20_smart-home-notifications]].

## Practice

### Decide whether to build at all

- Smartwatches present a dangerous opportunity for feature creep: it is much
  easier to justify a companion app for an existing mobile app than a new app
  from scratch, but a watch app only gets used if it offers value beyond what is
  convenient and possible on other devices
  [[2023-12-01_smartwatch-app]].
- The evidence for restraint: of 200 interactions submitted over five days, over
  80% were with native watch apps such as messages and timers; third-party apps
  struggle to gain traction, partly because users buy watches for specific
  purposes already covered by native apps, and partly because automatic
  downloading creates installations users are unaware of
  [[2023-12-01_smartwatch-app]].
- Value comes from context and from the wearable's own advantages — proximity to
  the body, hands-free use, quick access — not from replicating phone
  functionality. A smart-home door unlock has lasting value for a frequent task
  when the phone is out of reach; a hotel app has none after checkout
  [[2023-12-01_smartwatch-app]].
- For many companies the right answer is to invest in effective notifications
  rather than a standalone app, since notifications are the most common
  interaction type anyway [[2023-12-01_smartwatch-app]],
  [[2023-11-17_smartwatch-interactions]]. Do discovery work first rather than
  building because you can [[2023-12-01_smartwatch-app]].

### Interaction types worth supporting on a watch

Six types emerged from over 200 interactions across 11 participants, each with
its own design conditions [[2023-11-17_smartwatch-interactions]]:

- **Receiving** (notifications, reminders, feedback, suggestions) — the most
  common and most valuable, when informative, glanceable, personalised and
  timely; irrelevant ones are highly intrusive on so personal a device.
- **Referencing** — best when the information is simple, visual, personally
  meaningful and reachable in a flat hierarchy, so status can be checked without
  deep navigation.
- **Recording** — most helpful when the watch itself detects the activity and
  prompts, when it is perceived as accurate, when it shows real-time data, and
  when it is easy to start and to retrieve.
- **Controlling** — valued for operating other devices without fetching the
  phone; functions must be prioritised, synchronised across devices, and usable
  when hands are busy.
- **Communicating** — the watch's promise is comprehensive awareness of incoming
  messages; typing is tedious and dictation error-prone, so enough message
  content must be shown.
- **Guiding** — must work without the phone, use haptics to alert, and stay
  focused on the next step rather than dumping everything at once.

### Onboarding and reconnection

- Use visual step-by-step wizards: one task at a time with images, animations and
  clear text, which builds confidence better than text-only instructions or
  parallel tasks [[2025-09-12_smart-device-onboarding]].
- Reconnection after a power or WiFi outage deserves first-time-setup treatment.
  These tasks are infrequent, so users do not remember the steps and need the
  same visual guidance, feedback cues and progress reassurance as initial
  onboarding [[2025-09-12_smart-device-onboarding]].
- Tell users what to expect physically — beeps, blinking lights — so they can
  tell whether the device is responding
  [[2025-09-12_smart-device-onboarding]].
- Keep progress indicators honest: bars that fill without reflecting real
  progress destroy confidence; be transparent about what is happening and give
  realistic timeframes [[2025-09-12_smart-device-onboarding]].
- Make error messages specific and actionable — what went wrong, why, and the
  concrete next step — with built-in support access, rather than generic
  failures that push users into trial-and-error and abandonment
  [[2025-09-12_smart-device-onboarding]].

### Status, feedback and control in the companion app

- Show the status of every connected device on an overview screen, without
  navigation, so essential information (on/off, locked/unlocked) is immediately
  visible and commands can be confirmed
  [[2025-09-05_smart-device-best-practices]].
- Combine colour, iconography and text so status is unambiguous; this also
  supports accessibility [[2025-09-05_smart-device-best-practices]].
- For long-running tasks, show time remaining, completion percentage or status
  animations, which helps users plan and reassures them their settings were
  applied [[2025-09-05_smart-device-best-practices]].
- Give immediate feedback that a command was received and executed. Without it
  people wonder whether anything happened and repeat the action
  [[2025-09-05_smart-device-best-practices]].
- Cut repetition with reusable configurations, bulk editing across devices and
  quick-action shortcuts [[2025-09-05_smart-device-best-practices]].
- Act as the hub for other control channels — voice assistants, on-device
  buttons — and keep behaviour consistent across all of them so unified control
  is trustworthy [[2025-09-05_smart-device-best-practices]].

### Organisation over the device's life

- Let users categorise and name devices; custom names improve organisation and
  access speed while adding playfulness and anthropomorphism, which increases
  delight [[2025-09-05_smart-device-best-practices]].
- Allow renaming, removing and reassigning devices as homes evolve, so the app
  stays aligned with the user's actual environment
  [[2025-09-12_smart-device-onboarding]].
- Organise alerts by type, urgency and impact so users can tell what needs
  action now from what can wait [[2026-02-20_smart-home-notifications]].

### Notifications as the core of the experience

Alerts are how smart-home systems report status and invite interaction, and
well-designed ones build trust and keep users in control
[[2026-02-20_smart-home-notifications]]. As devices from several manufacturers
integrate into one ecosystem, consistent notification patterns across that
ecosystem become essential to usability and trust
[[2026-02-20_smart-home-notifications]]. The detailed guidance — three
notification types, seven principles of timing, relevance, specificity,
intensity, frequency, channel and adaptability — belongs to
[[Notification Design]].

## Sources (5)

- [[2023-11-17_smartwatch-interactions]] — the article identifies interaction types best suited to smartwatch constraints and advocates for designing interfaces that respect the device's limitations.
- [[2023-12-01_smartwatch-app]] — the article argues smartwatch apps require special consideration; not all phone features translate to valuable watch experiences.
- [[2025-09-05_smart-device-best-practices]] — The article specifically addresses design for smart-device companion apps across multiple device types.
- [[2025-09-12_smart-device-onboarding]] — Addresses specific smart-device app challenges: reconnection after power/WiFi outages, managing multiple devices across rooms, and handling device lifecycle changes that require interface flexibility.
- [[2026-02-20_smart-home-notifications]] — As multiple manufacturers' devices integrate, consistent notification patterns across ecosystems become essential to usability and trust.
