---
type: concept
name: Augmented Reality
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Augmented Reality Calibration"
  - "Augmented Reality Design"
  - "Augmented Reality Onboarding"
---

# Augmented Reality

## Definition

Augmented reality is technology that responds contextually to real-world inputs
and combines real-world data with programmed interactive elements without
restricting the user's movement [[2016-09-18_augmented-reality-ux]]. It differs
from virtual reality, which isolates users in a fabricated environment, while
sharing its real-time contextual response; a static hologram is not AR, whereas
a working parking-assistance system is
[[2016-09-18_augmented-reality-ux]]. Put more simply in the later usability
work, AR enhances the real world with an additional layer of information, with
applications across fitness, entertainment, ecommerce, tourism, and education
[[2022-11-20_ar-ux-guidelines]], superimposing digital items over a real-world
camera view [[2020-11-08_augmented-reality-useful]].

The corpus holds two positions in tension. The 2016 article frames AR as a
noncommand interface with three UX benefits: it decreases interaction cost
because information appears in context without an explicit command, reduces
cognitive load because users need not memorise details or switch to a lookup
system, and minimises attention-splitting by combining several information
sources into one overlay [[2016-09-18_augmented-reality-ux]]. The usability
studies that follow, from 2020 onward, find that real implementations fall well
short of that promise: significant usability challenges currently limit AR's
utility [[2020-11-08_augmented-reality-useful]], most users are unfamiliar with
AR and confuse it with virtual reality
[[2022-09-25_ar-walkthroughs]] [[2022-11-20_ar-ux-guidelines]], and the 2016
article itself predicted that many lousy AR systems would ship.

## Practice

### Deciding whether AR adds value

Do not implement AR for the sake of AR: users delight in it but question
features that add no functional value, and the appreciation concentrates on
immersive, interactive, educational experiences
[[2022-11-20_ar-ux-guidelines]]. In ecommerce, AR is most useful for items where
aesthetics and size matter — home décor, furniture, wearables, makeup — and
provides less value for functional items such as appliances, where specifications
dominate [[2020-11-08_augmented-reality-useful]]. Its stated strength is
bridging the gap of not seeing an item in real life before buying
[[2020-11-08_augmented-reality-useful]]. As of that study, users treated AR as
supplementary to product photos rather than a primary decision tool, using it to
gain confidence without weighting it heavily
[[2020-11-08_augmented-reality-useful]].

### Realism, accuracy, and trust

How realistic an item appears and how accurately it is placed in the environment
has a large impact on perceived helpfulness; users forgive minor imperfections
but reject cartoony or misaligned renderings
[[2020-11-08_augmented-reality-useful]]. Technical limitations that prevent
realistic product visualisation undermine trust
[[2022-11-20_ar-ux-guidelines]]. Trust is also path-dependent: negative prior
experiences damage it, users often avoid trying AR again after a poor
experience, and brands perceived as high-end are expected to have better AR
tools [[2020-11-08_augmented-reality-useful]].

### Discoverability

AR is not discoverable by default, because the technology is new and most users
do not think to look for it while browsing products online
[[2020-12-06_augmented-reality-ecommerce-guidelines]]. Many users do not know AR
exists in apps they use frequently (Amazon, Ulta, Best Buy, Target)
[[2022-11-20_ar-ux-guidelines]]. Remedies: promote AR clearly with descriptive
labels and prominent placement near the product image or a prominent
call-to-action; use text labels such as "See it in AR" or "Try It On", since the
AR cube icon is not universally recognised and any icon should be paired with
meaningful text; use hints and animations on first visit, which are well
received, but do not rely solely on hints users may dismiss without reading
[[2020-12-06_augmented-reality-ecommerce-guidelines]]. At the catalogue level,
add visual indicators on product listings or filtering options to highlight
AR-compatible items [[2022-11-20_ar-ux-guidelines]].

If AR requires a separate app, navigate users seamlessly from the product page
on the website to the same product in the app; generic links that only open the
app store force users to find the product again
[[2020-12-06_augmented-reality-ecommerce-guidelines]].

### Onboarding walkthroughs

Because AR presents novel interaction patterns, onboarding is critical
[[2022-09-25_ar-walkthroughs]]. The study of 11 participants found interactive
walkthroughs clearly more effective than static ones: static presentations such
as deck-of-cards layouts caused cognitive overload and strained working memory,
leaving users unable to remember the information and forcing them to replay the
tutorial, while walkthroughs that let users practise the interaction built
comprehension and confidence [[2022-09-25_ar-walkthroughs]].

Content guidance: start with the high-level purpose of the AR experience (for
instance, visualising furniture in your room) before descending into specific
controls; explain device handling, since users are often unaware that AR relies
on the device camera, covering how to hold the phone, angle, height, and
orientation; provide step-by-step environmental guidance on lighting, surface
quality, space size, and safety before launching; and combine text, visuals, and
audio, especially when users must hold the device away from their body
[[2022-09-25_ar-walkthroughs]].

### Calibration

Calibration aligns virtual elements with the real environment, and unlike
onboarding it recurs every session
[[2022-10-09_ar-calibration]]. Calibration patterns vary — scanning surfaces,
absolute positioning, relative positioning, or none — and each needs clear
communication [[2022-10-09_ar-calibration]]. The documented failure modes are
instructions that are too complex, presented all at once, or visually unclear;
vague feedback signals users cannot interpret; and misalignment between the
visual demonstration and the actual requirement
[[2022-10-09_ar-calibration]].

The guidelines: break instructions into low-granularity steps presented one at a
time; make them descriptive and unambiguous, since vague phrasing like "scan a
textured surface" confuses users, and add concrete examples and visual guidance;
make instructions visually salient by enclosing text in solid, high-contrast
boxes that stay readable against variable backgrounds and lighting; use clear,
standard signifiers instead of scattered dots and vague cues; give feedback on
system status so users know whether the system is processing, stuck, or ready;
and provide guidance, such as arrows, when an AR object leaves the field of view
[[2022-10-09_ar-calibration]]. The ecommerce guidelines say the same thing in
task terms: specify exactly what to show the camera, for instance "scan the
entire wall including where it meets floor and ceiling", which users found
immensely helpful because they would otherwise not know what to show
[[2020-12-06_augmented-reality-ecommerce-guidelines]]. Face-based AR (virtual
try-on) calibrates more easily than room-based AR, because facial detection is
more reliable [[2020-11-08_augmented-reality-useful]].

### Interface layout and attention

AR interaction demands intense focus on the main view and the bottom controls,
so functions placed at the top are often overlooked; put critical features in
the bottom chrome or make visual feedback obvious in the main view
[[2020-12-06_augmented-reality-ecommerce-guidelines]]. AR should also be
self-sufficient: users should be able to adjust an object's colour, details, or
dimensions inside the AR scene without exiting to product information, and UI
overlays should be minimised so they do not crowd the screen or interfere with
the experience [[2022-11-20_ar-ux-guidelines]]. Icons should be labelled and
instructions placed on solid backgrounds for visibility across variable
real-world environments [[2022-11-20_ar-ux-guidelines]].

One useful audience variable: participants with gaming backgrounds interpreted
AR icons and interactions quickly, while non-gamers struggled with unfamiliar
signifiers, so instructions should be tailored to users without gaming
experience [[2022-11-20_ar-ux-guidelines]].

### Testing AR apps

AR testing builds on mobile usability testing but adds spatial interaction,
physical movement, participant safety, and unfamiliarity with the technology
[[2022-08-28_testing-ar-apps]]. Seven areas need adaptation: task design, study
setting, session duration, recording equipment, participant selection, informed
consent, and session conduct [[2022-08-28_testing-ar-apps]].

Concretely: word tasks straightforwardly and unambiguously, since participants
new to AR misread them (asking to "take a photo of animals" can be understood as
real pets rather than virtual ones); allocate ample space and remove hazards
such as furniture, sharp objects, or slippery surfaces, because participants
focused on AR objects disregard their surroundings, and outdoor activities may
need an outdoor setting; allow longer sessions for app downloads and for
learning the technology, for example having participants download 15–20 minutes
beforehand or starting the download at the session opening; record both the
phone screen and the participant's movement in the room with a tripod-mounted
camera, using wearable microphones when participants are far from the equipment;
screen for age, health conditions, physical ability, and glasses, since some AR
apps are fitness games demanding real exertion; and communicate in advance about
physical activity, recording of surroundings, space requirements, the right to
withdraw, and charging the phone to avoid trailing cables
[[2022-08-28_testing-ar-apps]]. Above all, be calm and patient: participants are
often new to AR and will find tasks confusing for that reason alone
[[2022-08-28_testing-ar-apps]].

### Context awareness as the underlying promise

The original framing remains the benchmark: context and timing determine the
interaction, so the same gesture can mean different things depending on
proximity to a store, participation in an event, or proximity to a song, giving
rich contextual interaction without explicit commands
[[2016-09-18_augmented-reality-ux]]. That same source warns that poorly designed
AR overwhelms users with irrelevant information, confusing displays, and clutter
[[2016-09-18_augmented-reality-ux]] — the failure mode the later studies
document in detail.

## Sources (7)

- [[2016-09-18_augmented-reality-ux]] — Defines AR as real-time, contextually-responsive technology that overlays digital information on the physical world, creating opportunities to reduce interaction cost and cognitive load.
- [[2020-11-08_augmented-reality-useful]] — emerging technology that superimposes digital items over real-world camera views, with growing ecommerce use but significant usability challenges that currently limit utility.
- [[2020-12-06_augmented-reality-ecommerce-guidelines]] — specific UX guidelines for AR shopping tools including discoverability, labels, calibration instructions, and attention management for virtual try-on and view-in-room features.
- [[2022-08-28_testing-ar-apps]] — Users are often unfamiliar with AR technology and patterns; tasks must be clear, sessions require extra time for learning, and testing environment must be safe for movement.
- [[2022-09-25_ar-walkthroughs]] — AR users need clear walkthroughs that combine purpose, device handling, and environmental guidance; interactive walkthroughs are more effective than static presentations.
- [[2022-10-09_ar-calibration]] — calibration instructions must be broken into small, sequential steps; users need clear examples, visuals, and explicit feedback about system status and recovery actions.
- [[2022-11-20_ar-ux-guidelines]] — effective AR design prioritizes immersive, interactive, educational experiences over gratuitous use; technical quality, realism, and interaction smoothness significantly impact user perception.
