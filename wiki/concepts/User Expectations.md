---
type: concept
name: User Expectations
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "User Perception"
  - "User Preferences"
---

# User Expectations

## Definition

User expectations are what people anticipate a product will do, how fast, and in
what form — formed before and during use, and largely outside conscious control.
These sources show them forming from three inputs: the design itself, which
primes anticipations through imagery, layout and aesthetic treatment
([[2016-01-24_priming]]); direct experience, which is the dominant force for
intelligent assistants, where mental models are built from what users actually
tried and what succeeded or failed rather than from advertised capabilities
([[2019-02-03_mental-model-ai-assistants]]); and external messaging, which can
run ahead of what the technology delivers and open an expectation-reality rift
([[2025-09-05_vr-hype-cycle-lessons-for-ai]]).

The practical consequence running through the corpus is that expectations, not
objective performance, are the yardstick users apply. [[2016-01-24_priming]]
states it most directly: when primed expectations are confirmed the experience
feels smooth and intuitive, and when they are violated users perceive poor
usability even though the interface itself has not changed. Expectations are also
not uniform — they vary by task ([[2020-05-24_information-seeking-expectations]]),
by channel ([[2022-11-06_transactional-notifications]]), and by personal
preference ([[2020-02-02_dark-mode]]) — and they are not fixed:
[[2019-01-27_interpreting-research-findings]] describes perception becoming
actual experience over time as users adapt to something new.

## Practice

### Design primes expectations, whether or not you intend it

[[2016-01-24_priming]] treats priming — exposure to one stimulus influencing the
response to another — as an active force in interfaces. Its examples run both
ways. A prominent coupon-code field primes users to leave checkout and hunt for a
promotional code they never intended to use, costing sales. Aesthetic treatment
drives unconscious inferences about the business itself: a less polished design
primes a perception of local authenticity, a polished one primes corporate
establishment. Images and page content set expectations about what the site
offers, and misalignment between the priming and the reality produces frustration
and a judgement of poor usability. The source's recommendation is not to avoid
priming but to steer it — bias people toward behaviors and expectations that
match both the site's goals and their needs.

The same article extends the warning to research: task wording that reuses terms
present in the interface primes participants to hunt for those exact words, which
can make findability look better than it is, and facilitator behaviour
(friendliness, verbosity, terminology, demonstrations, physical redirects) primes
participants and degrades test reliability.

### Expect perception to lag, or diverge from, measured performance

[[2019-01-27_interpreting-research-findings]] is the corpus's treatment of the
gap between what metrics say and what users say. Efficiency gains measured in
seconds rather than minutes may go unnoticed; users may notice an improvement yet
judge it insufficient to justify learning a new workflow; and people resist change
regardless of benefits, because they have already invested in learning the
current system and take an initial productivity hit on any new one. So even an
objectively better system draws negative qualitative feedback during transition.
The source's method is to check the study design first (were the participants the
same? which tasks, with how much exposure? realistic conditions? proper analysis?),
then triangulate rather than let quantitative data automatically override
qualitative feedback, and, when contradictions persist, run learnability studies
across multiple rounds to see whether the negative reaction is temporary
change-aversion or a real usability problem.

### Baseline expectations that do not move

- **Speed.** [[2020-05-17_the-need-for-speed]] argues that users' sense of an
  acceptable wait rests on response-time thresholds that have not changed in 23
  years, while actual pages have not got faster: desktop load times sat flat
  around 6 seconds over a decade and mobile more than doubled to 20 seconds
  despite roughly tenfold faster connections, because extra bandwidth was spent
  on heavier pages. A one-second delay is enough to interrupt conscious thought
  and turn the experience from direct control into waiting. The conversion
  evidence it assembles is consistent — half-second delays cut conversions
  (Google and Bing, 2009), two seconds faster raised conversions 15% (Mozilla,
  2010), a three-second mobile load produced 53% abandonment (Google, 2016).
  Being merely faster than an already-frustrating average is not enough; the
  target is subsecond, and each incremental second gained pays off, with the
  slowest sites gaining most.
- **Scanning behaviour.** [[2016-08-07_visual-indicators-differentiators]] shows
  how people expect to find a distinctive item in a list: by secondary visual
  cues. Quantitative testing of four indicator families found unique icon plus
  unique colour best on every UX metric, icon alone slightly ahead of colour
  alone (particularly where arrows carry semantic meaning, as in stock
  performance), and text-only indicators worst — 57% slower to complete the task
  and 56% slower to first correct click. It also warns against colour alone,
  which fails colourblind users and is open to interpretation, and against
  stripping such "clutter" in the name of mobile decluttering.

### Expectations differ by task and by channel

- **By information-seeking task.**
  [[2020-05-24_information-seeking-expectations]], drawing on 498 critical
  incidents and 471 search instances, separates three behaviours with different
  expectations. *Acquire* (finding a fact): users want speed, few clicks, a
  direct answer in plain language, which makes featured snippets and knowledge
  panels valuable; they do not expect to invest effort, and these incidents are
  less memorable (57% reported within a week, versus 33% for the other types).
  *Compare/Choose*: users want comprehensive information from multiple
  perspectives, key information upfront, and comparison tables. *Understand*:
  users want clear organization (bullet points, subheadings), centralized content
  in one place, and ads confined to expected locations. Research tasks draw
  significantly more time on the results page before clicking (p<0.01), and the
  source argues that supporting them well matters disproportionately because
  users form stronger impressions from research-intensive experiences.
- **By notification channel.** [[2022-11-06_transactional-notifications]], based
  on two longitudinal diary studies across four countries, reports that users
  expect notifications to be more urgent and more concise than emails, with push
  notifications constrained to 50–240 characters and minimal formatting, so key
  information must be frontloaded because users scan only the first few words.
  SMS is stable and durable, fitting information users need to retain or act on
  quickly — pickup codes, delivery details, order changes, confirmation requests
  — while push suits nonurgent app-specific content such as abandoned-cart
  reminders and suggestions to return. Reserve both for genuinely time-sensitive
  content, since extraneous notifications frustrate users who may then disable all
  communication, and make per-channel opt-out easy. The source also notes cultural
  variation in channel preference, with Chinese users historically favouring SMS
  and Western users email.

### When preference and performance disagree, give the choice

[[2020-02-02_dark-mode]] is an explicit case of subjective expectation
outweighing measured performance. The evidence it reviews favours light mode for
users with normal or corrected vision — a brighter display contracts the pupil,
reducing spherical aberrations and increasing depth of field, which improves
acuity, proofreading and glanceable reading — with dark mode winning at night, at
very small font sizes, and for users with cloudy ocular media such as cataracts.
Yet the recommendation is to offer dark mode pervasively across all screens
(without necessarily defaulting to it, and especially in long-form reading
applications) for three reasons, one of which is simply that some users like it
better. Preference is treated as a legitimate reason to provide the option rather
than as an error to be corrected.

### Failed expectations are sticky, and messaging sets them

- [[2019-02-03_mental-model-ai-assistants]], a two-week diary study, found users
  settling into one of three mental models of an intelligent assistant —
  interface to the web or smart home, handy helper, repository of all knowledge —
  and into a narrow, stable set of activities (weather, music, reminders) that
  barely expanded over time. Mental models formed from experience rather than
  advertised skills, and once users concluded the assistant could not do
  something, they did not try again soon; new and frequent users hit the same
  limitations (varied phrasings not understood, wrong answers, no multistep
  commands). The source draws two design consequences: new users are the most
  fragile, since early failures freeze their model, and the open challenge is
  teaching users that a system has improved after they have already written a
  capability off.
- [[2025-09-05_vr-hype-cycle-lessons-for-ai]] describes the same dynamic at
  market scale: hype cycles occur when expectations, narratives and messaging
  outpace technological capability, and VR's promises (metaverse collaboration,
  a seamless merging of digital and physical) did not match the delivered
  experience, so billions in investment from Apple and Meta produced no mainstream
  adoption against limits of cost, ergonomics and performance — while niche uses
  (entertainment, medical visualization, hazard training, flight simulation)
  succeeded where the benefit clearly outweighed the drawbacks. Its advice for
  practitioners facing the equivalent moment in AI: avoid platform lock-in and
  invest in transferable, platform-agnostic skills; build a personal judgement
  from direct experience rather than marketing narratives; and identify the
  specific user pain points that define when the technology is actually worth
  adopting.

## Sources (10)

- [[2016-01-24_priming]] — design elements (aesthetic treatment, imagery, layout) prime specific user expectations about what a website or product offers; misalignment between priming and reality causes negative perception and frustration.
- [[2016-08-07_visual-indicators-differentiators]] — Humans rely on secondary visual cues like shape and color for quick item location; combining both cues significantly improves scanning performance.
- [[2019-01-27_interpreting-research-findings]] — Subjective user experience may diverge from objective performance metrics due to familiarity, change-aversion, or insufficient exposure; perception becomes actual experience over time as users adapt.
- [[2019-02-03_mental-model-ai-assistants]] — Examination of how users' expectations form through direct experience and how failures shape future behavior and adoption of features.
- [[2020-02-02_dark-mode]] — Acknowledges that users have subjective preferences for dark mode despite performance advantages of light mode, justifying the need to provide choice.
- [[2020-05-17_the-need-for-speed]] — explains how users' perception of acceptable wait times is based on response-time thresholds unchanged over 23 years.
- [[2020-05-24_information-seeking-expectations]] — documents distinct expectations for each task type, from speed preferences in Acquire to organization preferences in Understand tasks.
- [[2022-11-06_transactional-notifications]] — users expect SMS for urgent, time-sensitive, detailed information; push notifications for nonurgent suggestions and reminders; both channels need easy unsubscribe options.
- [[2025-09-05_vr-hype-cycle-lessons-for-ai]] — Demonstrates how messaging creates expectations (metaverse collaboration, seamless merging of digital/physical) that don't match actual capability or user experience.
- [[2024-01-23_laws-of-ux_03-1-jakobs-law]] — The anticipated behaviors and layouts users develop from cumulative experience with other products; when designs violate these expectations through unfamiliar conventions, users become confused and frustrated, as demonstrated by Snapchat's 2018 redesign failure.
