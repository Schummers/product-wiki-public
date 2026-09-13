---
type: concept
name: Mobile Design
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Gesture-Based Interaction"
  - "Mobile App Design"
  - "Mobile Applications"
  - "Mobile Design Patterns"
  - "Mobile UX"
  - "Mobile Usability"
  - "Touchscreen Design"
---

# Mobile Design

## Definition

Mobile design is the design of interfaces for phones and other small,
touch-operated, portable devices. Across the corpus it is treated not as a
smaller version of desktop design but as its own medium, with its own input
model (fingers and gestures rather than a cursor), its own constraints (little
screen space, variable network and data cost, shared and interrupted contexts of
use) and its own capabilities (camera, GPS, biometrics, sensors, notifications)
that desktop does not have ([[2017-10-15_better-mobile]],
[[2017-02-26_context-specific-cross-channel]]). Because mobile devices are
carried everywhere, mobile users care disproportionately about location-based,
time-sensitive and urgent information, and they work in short bursts rather than
long sessions ([[2019-11-03_mobile-microsessions]]).

The recurring failure mode named by the sources is porting: taking a design made
for one platform and moving it unchanged to another. Desktop layouts converted
to mobile produce unreadable images and untappable targets
([[2017-05-21_big-pictures-small-screens]], [[2019-05-05_touch-target-size]]),
while mobile patterns pushed back onto desktop produce hidden navigation and
wasted space ([[2016-07-24_mobile-first-not-mobile-only]],
[[2016-06-26_hamburger-menus]]). Mobile-first is endorsed as a prioritisation
discipline, not as a licence to design once and ship everywhere. The field is
also described as mature: after roughly fifteen years, patterns have converged,
content parity between mobile and desktop is the norm, and iOS and Android have
grown closer, so the remaining problems are less about basic layout and more
about overlays, in-app browsers and interaction subtleties
([[2023-01-01_state-mobile-ux]]). A curated survey of the whole area — general
principles, interaction design, navigation, content, onboarding, gestures,
device features, responsive design, cultural difference, devices beyond the
phone, ecommerce and testing — is collected in
[[2023-01-12_mobile-ux-study-guide]].

## Practice

### Treat mobile as its own medium

- Prioritise mobile-relevant information first: location, time-sensitive
  content, emergencies, phone numbers ([[2017-10-15_better-mobile]]).
- Integrate device capabilities rather than reproducing web forms: camera and
  barcode scanning instead of long number entry, GPS for store finders, SMS for
  urgent alerts, biometrics for authentication
  ([[2017-10-15_better-mobile]], [[2017-02-26_context-specific-cross-channel]]).
- Innovate on what only mobile can do — location-based rather than time-based
  reminders, and in the deepest cases whole business processes rethought around
  portability and real-time location ([[2017-10-15_better-mobile]]).
- Map the context of use: which tasks matter, when and where they happen, which
  device is used at each stage of the journey, and what each channel is good at.
  Desktop suits complex tasks and rich content; mobile suits microtasks and
  location; tablets suit media consumption
  ([[2017-02-26_context-specific-cross-channel]]).
- Keep core functionality consistent across channels while letting presentation
  and secondary features optimise per device
  ([[2017-02-26_context-specific-cross-channel]]).
- Do not port patterns between platforms. Hamburger menus, bottom-repeated
  navigation, sticky navigation, search icons instead of search boxes and
  top-right navigation placement all hurt desktop usability when carried over
  from mobile ([[2016-07-24_mobile-first-not-mobile-only]],
  [[2016-06-26_hamburger-menus]]).

Note a tension across dates: [[2016-06-26_hamburger-menus]] measures hidden
navigation as worse than visible navigation even on phones (used in 57% of cases
versus 86% for combo navigation, 2 seconds slower, 20% drop in content
discoverability), and treats hamburgers on mobile as a space-constrained
necessity rather than a good pattern. Seven years later
[[2023-01-01_state-mobile-ux]] reports hamburger menus and navigation bars as
converged, standard patterns users expect, and
[[2024-04-05_breakpoints-in-responsive-design]] treats collapsing navigation
into a hamburger at the smallest breakpoint as routine practice.

### Screen space, layout and responsive behaviour

- Define breakpoints from the actual device distribution of your audience, not
  from arbitrary standards; a common set is extra-small (mobile, up to 500px),
  small (tablet, 500–1200px), medium (laptop, 1200–1400px) and large (1400px+).
  Typical adjustments are collapsing navigation, reflowing columns and changing
  how many content elements are visible ([[2024-04-05_breakpoints-in-responsive-design]]).
- Images do not survive simple resizing. Remove images that add little, crop or
  reorient the ones that carry meaning, and move overlay text below or beside
  the image where small screens make it illegible. Watch for landscape shots
  cropped into portrait, and for desktop grids that stack into long single
  columns and separate images from their captions
  ([[2017-05-21_big-pictures-small-screens]]).
- Protect the content-to-chrome ratio. Keep sticky headers as small as
  possible while preserving readable text and adequate tap targets, give them
  high contrast with the content (avoid translucency), limit animation, consider
  partially persistent headers that hide on scroll down and return on scroll up
  with a 300–400ms animation, and question whether the header needs to be sticky
  at all ([[2021-04-04_sticky-headers]]). Decorative images and graphics still
  needlessly lengthen mobile pages, and users only keep scrolling if the content
  looks promising ([[2023-01-01_state-mobile-ux]]).
- Long responsive pages have made in-page links more valuable than they once
  were; label them explicitly ("On this page"), match link text to the target
  heading, scroll the target near the top of the screen with a little
  whitespace above so headings are not hidden behind sticky elements, and
  indicate the current section if the list stays sticky
  ([[2017-05-07_in-page-links]]).
- Tables: make the desktop table good first, keep columns legible without
  zooming, stick column headers and row labels, signal horizontal scrolling with
  cut-off elements or arrows (dots draw attention poorly), and let users filter,
  toggle columns or expand accordions to control what they see
  ([[2017-09-17_mobile-tables]]).
- Carousels: users should reach the last item in three or four steps, otherwise
  use a list; put the most interesting items first; use strong signifiers such
  as the illusion of continuity (half-images, truncated text) or arrows rather
  than dots; support horizontal swipe and add page gutters to reduce swipe
  ambiguity; keep items related and make hero content reachable another way
  ([[2018-08-19_mobile-carousels]]).
- Do not declutter away useful cues. Testing four families of visual indicators
  on mobile pages found colour plus icon best on every metric, while text-only
  indicators were 57% slower to task completion; relying on colour alone risks
  failing colourblind users ([[2016-08-07_visual-indicators-differentiators]]).
- Inline advertising is harder to distinguish from content on a small screen,
  and large ads relative to the viewport catch the eye even when the user
  intends to ignore them ([[2018-04-22_banner-blindness-old-and-new-findings]]).
- Responsive email has largely caught up: single-column layouts with full-width
  imagery now outperform multicolumn desktop-era designs, and file sizes should
  respect data-conscious mobile users ([[2017-08-13_newsletters]]).

### Touch and gesture

- Touch targets must be at least 1cm × 1cm as physically rendered — pixel
  dimensions are meaningless across densities — because fingertips are 1.6–2cm
  wide and the thumb contact area is around 2.5cm. Size and spacing must both be
  right: large targets packed together and well-spaced tiny targets each fail.
  Blame the target, not the finger. Primary calls to action, apps used while
  moving, and interfaces for children or seniors need more than the minimum.
  "View-tap asymmetry" — an element big enough to see but too small to tap —
  is the classic symptom of a desktop design converted to mobile
  ([[2019-05-05_touch-target-size]]). Touch-target sizing and microsessions were
  considered core enough knowledge to appear in the year's UX quiz
  ([[2020-01-05_ux-quiz-2019]]).
- Gestures are invisible: they have no visual representation, so they are hard
  to discover and remember, and gesture-heavy apps have failed commercially
  despite design-community enthusiasm. They pay off when a visual signifier
  reminds the user (the iPhone X home line) and when repetition is frequent
  enough to build habit; the compensation is screen real estate reclaimed from
  physical buttons ([[2017-12-03_iphone-x]]). Swipe ambiguity — the same swipe
  meaning different things depending on location, length and direction —
  increases the cognitive cost ([[2017-12-03_iphone-x]],
  [[2018-08-19_mobile-carousels]]).
- Contextual swipe (swipe to reveal actions) is widely adopted but weakly
  signified: users forget to try it, the revealed actions obscure the item being
  acted on, nonstandard meanings (saving rather than deleting) go undiscovered,
  and inconsistent behaviour inside one app multiplies what must be remembered.
  Keep the affected content visible, confirm destructive actions or provide easy
  undo, and reserve swipe for deletion and removal so the meaning stays stable
  ([[2017-02-12_contextual-swipe]]).
- A gesture can also be a deliberate space-saving device when it is culturally
  familiar: WeChat's shake gesture provides functionality that is invisible yet
  accessible to repeat users and reduces visual clutter, but it became familiar
  only through a mass campaign with a tangible reward
  ([[2016-10-16_wechat-qr-shake]]).
- Drag-and-drop is weak on touch: there are no hover states to carry signifiers,
  fingers are imprecise, and the system must distinguish taps from swipes.
  Menu-based alternatives take more steps but produce fewer errors
  ([[2020-02-23_drag-drop]]).
- Overlay dismissal is a live problem. Close buttons, tapping outside, swiping
  down, the phone's back button and horizontal swipes coexist without signalling
  which applies; stacked overlays get closed wholesale; full-page overlays look
  like pages and invite the back button; nested close buttons get confused. Lost
  selections and lost progress are the cost. Prefer separate pages or accordions,
  avoid stacking, keep a visible close button and support the device back button
  ([[2022-09-18_accidental-overlay-dismissal]], [[2023-01-01_state-mobile-ux]]).
- A visual language can undo these gains: iOS 26's Liquid Glass is documented as
  shrinking tap targets below the 1cm² guideline, crowding navigation, layering
  translucent controls over content so text becomes unreadable, animating without
  purpose, hiding controls in overflow menus, and moving long-established
  controls (search from top to bottom, changed back-button behaviour) so learned
  habits break ([[2025-10-10_liquid-glass]]).

### Input, forms and authentication

- Date input: calendar pickers work for dates near the present, but scrolling
  pickers in a small mobile space are tedious for distant dates such as
  birthdates — typing is faster. Parse multiple typed formats without demanding
  leading zeros, report errors with suggested fixes, disable impossible
  combinations, and disambiguate international formats by spelling out months
  ([[2017-01-22_date-input]]).
- Input steppers suit fields with a clear default that users nudge slightly
  (passengers, cart quantity), where one tap replaces focusing a field, typing
  and dismissing the keyboard. They fail for wide ranges and continuous
  quantities. Buttons must be large and well spaced (Fitts's Law), horizontal
  steppers generally beat vertical ones on mobile, and pairing the stepper with
  a text field covers both small adjustments and precise entry
  ([[2018-11-11_input-steppers]]).
- Authentication on mobile has improved markedly through biometrics, built-in
  password managers, one-time passwords, magic links and passkeys
  ([[2023-01-01_state-mobile-ux]], [[2016-11-20_ux-thanks]]).
- Two mobile-first login methods studied in China: scanning a QR code with a
  logged-in app to authenticate on another device, and SMS one-time passwords
  tied to a phone number. QR login needs a camera and an already-installed
  scanner but crosses channels; OTP works on any device but costs more
  interaction and raises concerns tied to phone ownership. Both shift
  authentication from what users know to what they have. Adoption in the US
  lags because scanners are less ubiquitous, phone numbers are less accepted as
  identifiers, and email remains the primary account identifier
  ([[2018-09-02_mobile-login-china]]). OTP also removes memory load and
  difficult mobile typing for Indian users, and auto-filling the code from SMS
  improves the cross-device experience ([[2016-09-04_mobile-behavior-india]]).

### Microsessions, interruption and notifications

- More than 40% of mobile usage consists of microsessions shorter than fifteen
  seconds. Even apps with complex tasks benefit from lowering time on task, and
  four external entry points let users bypass launching the app entirely:
  notifications, widgets, quick actions (long press) and voice assistants.
  Notifications and widgets must be self-sufficient and untruncated; quick
  actions should expose top tasks, not rare ones. Adoption of widgets and quick
  actions is low but implementation cost is low too, so the return stays high
  ([[2019-11-03_mobile-microsessions]]).
- Design for interruption. WeChat mini programs sit inside a messaging app, so
  progress must be saved and notifications used to bring users back to abandoned
  tasks. Constrained app variants should also keep the core functionality of the
  full app (or hand off to it), lean on the host platform's strengths such as
  sharing and QR scanning, and optimise for infrequent users who chose the
  lightweight version to save storage ([[2018-09-09_wechat-mini-programs]]).
- Push notifications: users receive around 56 a day. Do not request permission
  on first launch — let users experience value first; say what the notifications
  will contain rather than relying on the generic system prompt; never send
  bursts, combine related messages instead; personalise, because most users never
  change defaults; and keep the off switch inside the app's own settings rather
  than hiding it in device settings ([[2018-11-18_push-notification]]).
- Layer information on small screens: gist first, secondary detail collapsed,
  accordions where useful, because sessions are short and interrupted
  ([[2017-02-26_context-specific-cross-channel]]).
- Glanceable text (one or two words read in isolation — notifications, GPS
  directions, watch faces) benefits from larger, regular-width, uppercase type:
  lowercase cost 26% more time and condensed faces 11.2% more in a lexical
  decision study. The finding applies to isolated words only; all-caps remains
  bad for passages ([[2017-11-26_glanceable-fonts]]).

### Content and reading

- Comprehension on mobile is not the deficit it was once thought to be. A study
  of 276 participants found no practical difference for easy linear articles
  (mobile was 3 points higher, significant but not meaningful), attributed partly
  to screens with 6.5× the pixels of the phones in the original study, and some
  readers prefer mobile's reduced distraction. Difficult material is different:
  readers slow down and re-read to hold comprehension, a speed-accuracy
  trade-off. Most web tasks involve navigation and interaction as well as
  reading, and those remain harder on mobile; sites with complex financial,
  medical, scientific or B2B content should run their own mobile studies
  ([[2016-12-11_mobile-content]]).
- Content parity is now the norm — the separate "full site" is largely obsolete
  ([[2023-01-01_state-mobile-ux]]) — but content strategy still differs:
  prioritise, defer secondary material, use space efficiently
  ([[2023-01-12_mobile-ux-study-guide]]).
- Infinite scrolling grew with touchscreens because they make scrolling cheap.
  It suits a browse mindset on homogeneous streams and hurts a search mindset,
  where pagination provides landmarks for refinding. It also creates an illusion
  of completeness, blocks the footer and raises accessibility barriers. A Load
  More button is the compromise, and it specifically helps mobile users with
  limited data ([[2022-09-04_infinite-scrolling-tips]]).
- Teenagers, often mobile-primary without a laptop, are goal-oriented rather
  than entertainment-seeking, impatient with slow pages, put off by dense text
  and by childish design — and complex mouse gestures, small buttons and
  rollover effects do not survive the move to touch
  ([[2019-03-17_usability-of-websites-for-teenagers]]).

### Onboarding, tutorials and permissions

- Deck-of-cards tutorials on first launch do not help. In a study of 70 users
  across four apps, task success was 91% for those who read the tutorial versus
  94% for those who skipped it, completion times were comparable, and the
  tutorial group rated tasks as *more* difficult — tutorials can make a simple
  app look complicated ([[2020-03-08_mobile-tutorials]]).
- Avoid onboarding where possible and spend the effort on a more learnable
  interface. Test a version without onboarding first. Put feature promotion on
  the app-store page, not the launch sequence. Gather content-level setup data
  (language, fitness level) but not visual customisation before users understand
  the interface. If instruction is unavoidable, keep it minimal, optional and
  contextual ([[2020-06-21_mobile-app-onboarding]]).
- These two sit in tension with the AR findings below, where onboarding is
  judged necessary precisely because the interaction pattern is unfamiliar. The
  reconciling variable across the sources is novelty: instruction is wasted on
  conventional interfaces and needed for genuinely new ones
  ([[2022-09-25_ar-walkthroughs]], [[2020-06-21_mobile-app-onboarding]]).
- Permission requests: users run a cost-benefit analysis. Giving a reason made
  users 12% more likely to grant, and framing that reason around user benefit
  rather than system need produced an 81% increase. Ask in context (when the
  user taps the camera icon) rather than at launch; on Android, add an
  explanation screen because purpose strings are not supported in the dialog;
  and make it easy to reverse a refusal later
  ([[2019-04-28_permission-requests]]). Mobile deserves particular care here
  because apps are downloaded and installed quickly, before users grasp what
  data access they are granting.

### Bridging physical and digital

- QR codes lower interaction cost compared with typing a URL and serve
  progressive disclosure, cross-channel transitions and cross-device
  authentication — but they carry no information scent, so a label explaining
  what scanning yields is mandatory. Minimum 2cm × 2cm, adding 1cm for every
  10cm of viewing distance; deep-link to the relevant content rather than a
  homepage; assume every scan happens on a phone, so the destination must be
  mobile-optimised. Avoid them when the user has under fifteen seconds to scan
  or for frequently revisited sites, and account for phishing and overlaid fake
  codes ([[2024-02-09_qr-code-guidelines]]). The same lack of information scent,
  plus awkward long-press extraction from chat and wasted screen space when a QR
  replaces a link, is documented inside WeChat ([[2016-10-16_wechat-qr-shake]]).
- Adoption of such techniques needs usefulness, ease of use and discoverability
  together; QR and shake met all three in China and only the first in the US
  ([[2016-10-16_wechat-qr-shake]]).
- QR-code ordering can automate a restaurant, but the interface has to handle
  parties (a single table code forces phone-passing), customisation requests,
  and more than one payment method, or the automation simply generates waiter
  calls ([[2022-06-19_unmanned-restaurant-case-study]]).
- Store locators: 80% of users now go straight to a search engine or mapping app
  rather than the company site, success rates rose from 63% to 97% over eighteen
  years yet 40% still hit difficulty. Offer geolocation through a visible button
  rather than hiding it behind a permission dialog, and link out to familiar
  mapping platforms instead of building a proprietary map
  ([[2018-10-07_store-finders-and-locators]]).
- Smartphones also removed the need for printed directions, one of several
  mobile pain points resolved by design rather than by new technology, alongside
  biometric login, voice input when hands are occupied, offline downloads and
  device handoff ([[2016-11-20_ux-thanks]], [[2018-10-07_store-finders-and-locators]]).

### Augmented reality on phones

- AR is not discoverable by default: most users do not look for it, and many do
  not know it exists in apps they already use. Promote it near the product image
  with a descriptive text label ("See it in AR", "Try It On") — the AR cube icon
  is not universally recognised — and flag AR-compatible items in listings
  ([[2020-12-06_augmented-reality-ecommerce-guidelines]],
  [[2022-11-20_ar-ux-guidelines]]).
- Most users confuse AR with VR and lack the gaming background that would help
  them read AR signifiers, so instructions must be simple, unambiguous and set on
  high-contrast solid backgrounds that survive variable real-world environments
  ([[2022-11-20_ar-ux-guidelines]], [[2022-09-25_ar-walkthroughs]]).
- Interactive walkthroughs beat static deck-of-cards presentations, which
  overload working memory and send users back to replay them. Explain the
  high-level purpose before the controls, tell users how to hold the device
  (angle, height, orientation) since many do not realise the camera is involved,
  and give step-by-step guidance on lighting, surfaces, space and safety.
  Combine text, visuals and audio, especially when the device is held away from
  the body ([[2022-09-25_ar-walkthroughs]]).
- Calibration needs contextual step-by-step instructions naming exactly what to
  show the camera. Attention concentrates on the main view and the bottom
  chrome, so controls placed at the top get missed; keep critical functions at
  the bottom ([[2020-12-06_augmented-reality-ecommerce-guidelines]]). Make AR
  self-sufficient — colour, dimensions and details adjustable without exiting the
  scene — while minimising overlays that crowd it
  ([[2022-11-20_ar-ux-guidelines]]). If AR lives in a separate app, deep-link to
  the same product rather than dropping users at the app store
  ([[2020-12-06_augmented-reality-ecommerce-guidelines]]). Users are enthusiastic
  about immersive educational AR but sceptical of gratuitous AR that adds no
  value ([[2022-11-20_ar-ux-guidelines]]).

### Beyond the phone: watches and vehicle screens

- Smartwatches share mobile principles under tighter constraints. Six valuable
  interaction types were identified — receiving, referencing, recording,
  controlling, communicating, guiding — while consuming and browsing are rarely
  useful. Notifications must be glanceable, personalised and timely; reference
  information must be simple, visual and in a flat hierarchy; recording works
  best when the watch detects the activity; controlling is valued when hands are
  busy; typing is tedious and dictation error-prone; guidance must work without
  the phone and use haptics, showing only the next step
  ([[2023-11-17_smartwatch-interactions]]).
- Do not assume phone features transfer. Over 80% of logged smartwatch
  interactions were with native apps such as messages and timers; third-party
  apps struggle to gain traction, partly because users buy watches for
  notifications and activity tracking and partly because companion apps install
  automatically without the user noticing. Value comes from context (a door
  unlock used daily) rather than replicated functionality (a hotel app that dies
  at checkout), and most companies are better served by getting notifications
  right than by shipping a standalone watch app ([[2023-12-01_smartwatch-app]]).
- Large in-car touchscreens show the limits of soft controls in a
  safety-critical setting: physical buttons are operated by muscle memory while
  soft buttons demand a look; Fitts's Law makes controls at the bottom of the
  screen slow to acquire from the steering wheel; shrinking targets to fit more
  options reduced accuracy and increased accidental touches; crowding produced
  slips; and an always-present map background interfered with reading status
  text. Showing several applications at once was the genuine benefit
  ([[2019-05-19_tesla-big-touchscreen]]).

### Accessibility and inclusion

- Screen-reader users on mobile receive information sequentially, one element at
  a time, which forces them to remember everything heard to build a mental
  model. They scan by jumping between headings and links, which only works when
  the HTML is semantically coded — visual styling alone is not enough. Frontload
  labels with keywords, because users swipe fast and do not hear labels out.
  Manage focus so it moves to newly opened overlays and menus. Third-party
  accessibility plugins are largely ignored by users who already have a more
  powerful built-in screen reader; accessibility is structural, and testing with
  real screen-reader users is what surfaces the problems
  ([[2023-04-30_screen-reader-users-on-mobile]]).
- Related accessibility costs appear elsewhere: infinite scroll forces
  keyboard-only users to tab through vast content and leaves screen-reader users
  with only the first chunk ([[2022-09-04_infinite-scrolling-tips]]);
  drag-and-drop needs keyboard grab handles and screen-reader messaging
  ([[2020-02-23_drag-drop]]); colour-only indicators fail colourblind users
  ([[2016-08-07_visual-indicators-differentiators]]); and automated,
  screen-mediated service cannot substitute for human help for wheelchair users,
  elderly customers and others with specific needs
  ([[2022-06-19_unmanned-restaurant-case-study]]).

### Cultural and economic context

- Mobile behaviour is not universal. In India, constrained storage and RAM plus
  expensive data produce lightweight browsers, SD-card app storage,
  peer-to-peer file transfer and a preference for offline-capable web
  experiences; mobile-only users weigh whether the mobile web is good enough
  before installing an app, whereas desktop-heritage users install for frequent
  tasks. Mobile wallets and SMS transfers serve users without cards or bank
  accounts ([[2016-09-04_mobile-behavior-india]]).
- Where phone sharing is a norm, privacy design inverts the usual assumptions:
  app lockers are widely installed to protect messages, photos and financial
  apps and to give parents control, some can hide their own icon to avoid
  signalling distrust, and some users drop the device-level lock entirely so
  sharing stays easy. Users voluntarily add login walls — the opposite of the
  usual complaint about login friction — though lockers bring their own friction
  and generally poor UX ([[2016-11-27_app-lockers]],
  [[2016-09-04_mobile-behavior-india]]).
- Societies that came online via mobile developed different conventions —
  phone numbers as identifiers, QR and OTP login — that desktop-first societies
  did not inherit ([[2018-09-02_mobile-login-china]],
  [[2016-10-16_wechat-qr-shake]]). Cultural difference and accessibility
  diversity are treated as first-class dimensions of mobile design, not
  footnotes ([[2023-01-12_mobile-ux-study-guide]]).

## Sources (49)

- [[2016-06-26_hamburger-menus]] — While hamburger menus may be necessary on mobile due to space constraints, they should not be ported to desktop designs where screen space allows for visible navigation.
- [[2016-07-24_mobile-first-not-mobile-only]] — Mobile design has unique constraints and solutions; successful mobile patterns should not be uncritically applied to platforms with different capabilities.
- [[2016-08-07_visual-indicators-differentiators]] — While mobile screen space is limited, removing helpful visual indicators in the name of decluttering actually harms usability.
- [[2016-09-04_mobile-behavior-india]] — Illustrates how hardware constraints (storage, RAM, data costs) and cultural norms (device sharing) create mobile behaviors that differ fundamentally from Western patterns and require design adaptation.
- [[2016-10-16_wechat-qr-shake]] — Demonstrates how gesture-based UI (shake) reduces screen real estate when familiar, provides invisible yet accessible functionality for repeat users, and improves mobile UX through reduced visual clutter.
- [[2016-11-20_ux-thanks]] — Mobile-specific pain points like biometric authentication, hands-occupied scenarios with voice input, and offline access require design solutions tailored to mobile contexts and capabilities.
- [[2016-11-27_app-lockers]] — Shared device usage requires design solutions that balance privacy protection with usability and social acceptance in household contexts.
- [[2016-12-11_mobile-content]] — Mobile reading comprehension for easy content is equivalent to desktop, but difficult content requires more effort; interaction and navigation remain more challenging on mobile.
- [[2017-01-22_date-input]] — scrolling date pickers on small mobile screens are tedious; typing is faster for distant dates; mobile considerations must be taken into account for date input usability.
- [[2017-02-12_contextual-swipe]] — Analyzes swipe as the central gesture pattern for usability and discoverability, focusing on its implementation in iOS and Android mobile apps.
- [[2017-02-26_context-specific-cross-channel]] — mobile-specific optimization strategies for context and device capabilities.
- [[2017-05-07_in-page-links]] — Shows how responsive design and small screens have increased the value of in-page links by extending page length and making scrolling more burdensome.
- [[2017-05-21_big-pictures-small-screens]] — Addresses responsive image strategy as distinct from desktop design, accounting for small viewports and portrait orientation.
- [[2017-08-13_newsletters]] — responsive email design now accommodates various screen sizes and connection speeds, with single-column layouts and appropriate file sizes for data-conscious mobile users.
- [[2017-09-17_mobile-tables]] — mobile tables must accommodate smaller viewports, varied network speeds, and touch interaction; legibility and context are paramount.
- [[2017-10-15_better-mobile]] — defines mobile as a distinct medium with unique interaction patterns, context, and integrated capabilities that should drive design innovation.
- [[2017-11-26_glanceable-fonts]] — addresses font choices for micro-sessions and glanceable content on phones, smartwatches, and AR/VR devices.
- [[2017-12-03_iphone-x]] — Design for mobile devices faces unique constraints including small screens and touch input; gestures can help maximize content space but introduce learning costs that desktop interfaces do not face.
- [[2018-04-22_banner-blindness-old-and-new-findings]] — addressing the unique challenge of inline ads on mobile where screen size magnifies ad prominence and makes them harder to distinguish.
- [[2018-08-19_mobile-carousels]] — design discipline for small touchscreens with constrained space; carousel design on mobile requires special attention to gesture support, discoverability, and sequential access efficiency.
- [[2018-09-02_mobile-login-china]] — design for mobile-first societies differs from desktop-first approaches; understanding regional differences in mobile adoption and infrastructure informs appropriate solutions.
- [[2018-09-09_wechat-mini-programs]] — design principles for applications on mobile devices; mini programs represent a constrained variant requiring thoughtful feature prioritization and streamlined workflows.
- [[2018-10-07_store-finders-and-locators]] — the evolution from printed directions to mobile mapping integration, and how smartphone availability changed the role of store-locator features on company websites.
- [[2018-11-11_input-steppers]] — considerations specific to touch-based input on small screens, where the precision demands of traditional controls may not apply.
- [[2018-11-18_push-notification]] — designing notification systems that work effectively on mobile devices where attention is limited and interruptions are more disruptive than on desktop.
- [[2019-03-17_usability-of-websites-for-teenagers]] — Mobile-first considerations for teen audiences, including touch interface requirements, responsive design, and avoidance of complex mouse-dependent interactions.
- [[2019-04-28_permission-requests]] — Mobile apps require special consideration for permission timing and copy since users download and install apps quickly without full understanding of their data access.
- [[2019-05-05_touch-target-size]] — Mobile apps must account for physical reality of finger size and context of use; desktop designs often create unusable touch targets when converted to mobile.
- [[2019-05-19_tesla-big-touchscreen]] — Touchscreens work well for multiple simultaneous windows (a benefit), but target sizing, spacing, and feedback are problematic for safety-critical driving tasks.
- [[2019-11-03_mobile-microsessions]] — identifies specific design patterns and strategies for optimizing mobile experiences around microsessions and quick task completion.
- [[2020-01-05_ux-quiz-2019]] — includes questions on touch targets and microsessions specific to mobile experiences.
- [[2020-02-23_drag-drop]] — Explores challenges of implementing drag-and-drop on touchscreens and when menu-based alternatives are more usable despite additional steps.
- [[2020-03-08_mobile-tutorials]] — identifies specific challenges in mobile app design where tutorials may paradoxically make apps seem more complicated than they are.
- [[2020-06-21_mobile-app-onboarding]] — how onboarding patterns specifically apply to mobile applications versus desktop contexts.
- [[2020-12-06_augmented-reality-ecommerce-guidelines]] — designing AR experiences for mobile devices where screen real estate is limited, attention is focused on primary content, and calibration must be simple enough for touch interaction.
- [[2021-04-04_sticky-headers]] — the article emphasizes mobile considerations including tap target sizes, content-to-chrome ratios, and small screen constraints.
- [[2022-06-19_unmanned-restaurant-case-study]] — QR code ordering via mobile apps enables automation but requires careful interface design to handle parties, customization, and payment flexibility.
- [[2022-09-04_infinite-scrolling-tips]] — Infinite scrolling rose in popularity with mobile devices due to scroll-friendly touchscreens; Load More buttons help address data-usage concerns for mobile users.
- [[2022-09-18_accidental-overlay-dismissal]] — Common patterns like overlays provide functionality but create distinct usability challenges; mobile patterns require clear interaction affordances and recovery mechanisms.
- [[2022-09-25_ar-walkthroughs]] — AR apps must provide multi-modal instructions (text, visual, audio) tailored to unfamiliar user populations; clarity about device orientation and environmental requirements prevents failure.
- [[2022-11-20_ar-ux-guidelines]] — AR apps must account for users' limited familiarity with AR; instructions need to be high-contrast, unambiguous, and tailored to users without gaming experience.
- [[2023-01-01_state-mobile-ux]] — Mobile design has matured significantly, with convergence on standard patterns, content parity, and improved authentication, though challenges with overlays and in-app browsers persist.
- [[2023-01-12_mobile-ux-study-guide]] — Comprehensive study guide covering all aspects of mobile user experience from general principles to specialized topics, interaction design, and cultural considerations.
- [[2023-04-30_screen-reader-users-on-mobile]] — Creating interfaces for small screens that must account for how users interact when they cannot see, requiring sequential code order and semantic HTML.
- [[2023-11-17_smartwatch-interactions]] — smartwatch design shares many principles with mobile design but with tighter constraints around screen size and input methods.
- [[2023-12-01_smartwatch-app]] — while smartwatches are small mobile devices, their design is distinct from phones; phone app features should not be assumed to work on watches.
- [[2024-02-09_qr-code-guidelines]] — QR codes primarily serve mobile experiences and must link to mobile-optimized content.
- [[2024-04-05_breakpoints-in-responsive-design]] — explores how smallest breakpoints require special consideration for space-constrained mobile interfaces.
- [[2025-10-10_liquid-glass]] — Documents specific failures: contrast problems with text on images, animation distraction, crowded tap targets below guideline sizes, discoverability loss from hidden controls, and reduced predictability.
