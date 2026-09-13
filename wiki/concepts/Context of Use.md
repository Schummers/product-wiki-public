---
type: concept
name: Context of Use
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Context in Design"
---

# Context of Use

## Definition

Context of use is the set of circumstances surrounding a task: who the user is,
when and where they act, what device or channel they reach for, and what state
they are in while doing it. [[2017-02-26_context-specific-cross-channel]] breaks
it into four elements — the user's most important tasks, when and where those
tasks are completed, which devices are used at each stage of the journey, and
what each channel is good at. [[2018-02-12_solving-design-exercises_11-step-3-understand-the-customer-s-context-and-needs-when-and]]
frames it as a set of variables to interrogate: physical location, the trigger
event that creates the need, the time available, the platform at hand, and the
customer's emotional state.

The sources treat context as an input to design decisions rather than
background colour. Conditions such as being on the move or in a hurry lead to
concrete choices like hands-free navigation or a dark interface
([[2018-02-12_solving-design-exercises_11-step-3-understand-the-customer-s-context-and-needs-when-and]]),
and context also determines what behaviour is socially acceptable: the same
system needs to behave differently at dinner, in an office, at a church service
or at a sporting event, and a system with no contextual awareness produces
social awkwardness through mismatched behaviour
([[2016-06-12_embarrassment]]).

## Practice

### Map the variables before designing

[[2018-02-12_solving-design-exercises_11-step-3-understand-the-customer-s-context-and-needs-when-and]]
makes "understand when and where they experience this problem" a distinct step,
taken after the audience is defined and before ideation. The questions to
answer are where the user physically is, what triggers the need, how much time
they have, which platform they are on, and how they feel. The chapter pairs
this with two techniques for turning context into needs: user stories
("As a [role], I want [goal/desire] so that [benefit]") to expose the real
motivation behind a desired behaviour, and journey mapping to locate pain
points that become product opportunities later.

[[2017-02-26_context-specific-cross-channel]] gives the cross-channel version of
the same exercise: identify the most important tasks, when and where they are
completed, which device serves each stage of the journey, and what each
channel's strengths are.

### Context decides the device, and the device decides the design

The two NN/g sources agree that context shapes device choice, and that device
choice should feed back into scope.

- [[2017-02-26_context-specific-cross-channel]] maps strengths to channels:
  desktop for complex tasks and detailed, scannable content thanks to large
  screens, keyboards and multitasking; mobile for microtasks, quick access,
  geolocation and urgent action, with layered content because sessions are
  interrupted; tablets for reading, video and immersive activities with little
  text input, including wet or messy hands. It recommends leveraging
  device-specific capabilities — geolocation for a store finder, camera for
  photo input, SMS for urgent alerts, Touch ID for authentication.
- [[2019-08-25_large-devices-important-tasks]] supplies the behavioural evidence:
  in a diary study of 50 participants and 492 activities, desktop activities
  were rated more important (4.03 vs 3.61 out of 5) and mobile activities
  easier (4.52 vs 3.96). The authors read this as self-selection — users solve
  easy problems on the phone and defer hard ones to the computer. Away from
  home, the phone is primary; at home or work with uninterrupted time, users
  take on longer, more important tasks on larger devices.

The practical consequence in [[2019-08-25_large-devices-important-tasks]] is that
mobile-first is not automatic: for products supporting high-importance
activities such as finance or healthcare, actual mobile usage rates should
decide the priority, and if mobile volume is low, desktop stays first.

[[2017-02-26_context-specific-cross-channel]] frames the trade-off as a balance
rather than a choice: keep core functionality consistent across channels so the
experience stays learnable, but optimise presentation and available features
for each device and its context.

### Social context is part of the context

[[2016-06-12_embarrassment]] extends context beyond the individual to the people
around them. Systems are used in front of others, and failures there embarrass
the user rather than merely inconveniencing them: messages sent to unintended
recipients, private information exposed by defaults, alarms defaulting to 2am
instead of 2pm, personal notifications popping up during a formal presentation.
The article's methodological point follows directly: lab testing one user at a
time misses these defects, so field studies, diary studies over time, and
testing with groups and in realistic contexts are what surface them.

### Worked examples: context as the source of constraints

Three chapters of *Solving Product Design Exercises* show the analysis producing
design decisions.

- **Kiosk** ([[2018-02-12_solving-design-exercises_18-3-1-designing-a-kiosk-interface]]):
  the retail environment sets the requirements — queues form, customers are
  carrying shopping bags so operation must be single-handed, lighting is
  adequate, and the hygiene motivation is unsophisticated. Because the setting
  produces queues, interface efficiency is not a nicety: less time per
  operation means fewer queues and more sales, and queue perception alone can
  drive customers away.
- **Self-publishing platform** ([[2018-02-12_solving-design-exercises_19-3-2-a-self-publishing-platform-for-amazon]]):
  authors work on laptops and desktops from home, coffee shops, airports and
  co-working spaces, and are both excited and anxious. That mapping is what
  justifies a web app for the publishing work itself and mobile for tracking
  after launch.
- **Primary health care** ([[2018-02-12_solving-design-exercises_21-3-4-improving-primary-health-care]]):
  patients initiate care from home, work or on the go, usually when they feel
  unwell and are anxious or uncertain, and then have to travel to the clinic,
  which costs time and carries the risk of catching something else. Remote
  group appointments are chosen partly because joining by smartphone removes
  the travel burden and lowers the commitment barrier for preventive care that
  would otherwise be skipped.

### Context understanding as a hiring signal

[[2018-02-12_solving-design-exercises_23-chapter-4-how-to-use-a-design-exercise-when-interviewing]]
lists it among the criteria for evaluating a design candidate: whether they
think about audience and context, and articulate customer needs, before
proposing a solution. Candidates who skip that step are distinguished from
those who do not.

## Sources (10)

- [[2016-06-12_embarrassment]] — Understanding context (different social norms and expectations in different settings) is essential to preventing embarrassing system behaviors.
- [[2017-02-26_context-specific-cross-channel]] — understanding when, where, and how users complete tasks on different devices drives design decisions.
- [[2019-08-25_large-devices-important-tasks]] — Location, time availability, and task urgency shape which device users select; on-the-go contexts favor mobile for simpler tasks.
- [[2018-02-12_solving-design-exercises_11-step-3-understand-the-customer-s-context-and-needs-when-and]] — this chapter details how to understand when and where users experience problems, including physical location, trigger events, time constraints, platforms, and emotional state.
- [[2018-02-12_solving-design-exercises_18-3-1-designing-a-kiosk-interface]] — the chapter demonstrates careful analysis of when and where the kiosk operates (retail, busy, queues), what customers are doing (shopping, holding bags), and how these factors drive design decisions
- [[2018-02-12_solving-design-exercises_19-3-2-a-self-publishing-platform-for-amazon]] — Dashinsky maps when and where authors work (laptops and desktops from home, coffee shops, airports, co-working spaces) and their emotional state (excited and anxious), using this to justify a web app for desktop publishing and mobile for post-launch tracking.
- [[2018-02-12_solving-design-exercises_21-3-4-improving-primary-health-care]] — Patients initiate care from home, work, or on-the-go, often when they feel unwell and are anxious or uncertain, and must travel to clinic (adding time and risk of catching other illnesses). Remote group appointments address this by reducing travel burden and anxiety through peer learning.
- [[2018-02-12_solving-design-exercises_23-chapter-4-how-to-use-a-design-exercise-when-interviewing]] — A core evaluation criterion is whether candidates understand and articulate the target audience, user context, and customer needs before proposing solutions, distinguishing strong candidates from those who skip this step.
- [[2013-08-01_just-enough-research_02-chapter-1-enough-is-enough]] — Hall emphasizes that design success depends on understanding the environment, conventions, and constraints within which the product must operate, not on engineering alone.
- [[2019-12-17_storytelling-in-design_08-chapter-7-defining-the-setting-and-context-of-your-product]] — Dahlström demonstrates how Foursquare's failure to account for context (a one-time share vs. a pattern of sharing) breaks user expectations; context determines whether sharing should default on or off. Julien Samson explains that context is a tool that helps authors build trust and interest with their readers, a principle that applies equally to product design.
