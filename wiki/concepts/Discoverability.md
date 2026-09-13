---
type: concept
name: Discoverability
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Découvrabilité"
  - "Feature Discoverability"
---

# Discoverability

## Definition

Discoverability is whether users realise a feature exists at all. The corpus's
cleanest formulation separates it from two neighbours it is often confused
with: discoverability is knowing the feature exists, **findability** is being
able to locate it once you know it exists, and **usability** is being able to
operate it once found [[2020-02-09_user-testing-stepped-tasks]]. A feature can
be perfectly usable and still fail, because nobody ever learns it is there —
which is the recurring failure mode documented across hidden navigation,
gestures, modes, AR tools and AI features.

The sources converge on the causes. Things go undiscovered when they are
visually hidden or low-salience [[2016-06-26_hamburger-menus]], when there is
no signifier that an interaction is even possible
[[2017-02-12_contextual-swipe]],
[[2025-03-18_369_Guide_UX_Curseur_de_souris_natif_et_custom]], when they are
reachable only from a particular mode or behind a secondary control
[[2019-04-14_modes]], [[2019-05-12_split-buttons]], when the technology is new
enough that users do not think to look for it
[[2020-12-06_augmented-reality-ecommerce-guidelines]],
[[2022-11-20_ar-ux-guidelines]], or when the capability itself is opaque and
users cannot know what to ask for
[[2025-08-22_ai-information-seeking-keyword-foraging]],
[[2025-04-25_prompt-suggestions]]. Familiarity with an interface is itself a
cause: habitual, task-focused users skip past new additions entirely
[[2025-10-17_google-ai-mode]].

## Practice

### Visibility beats hiding

The quantitative case against hidden navigation is the strongest data point in
the corpus [[2016-06-26_hamburger-menus]]. Comparing hidden, visible and combo
navigation:

- On desktop, hidden navigation was used in 27% of cases versus 48% (visible)
  and 50% (combo); on mobile, 57% versus 86% for combo.
- Content discoverability dropped 20% on sites with hidden navigation.
- Users rated tasks 21% more difficult than with visible navigation, and took
  at least 39% longer to complete them on desktop (15% slower on mobile).
- Accessing hidden navigation itself cost 5–7 extra seconds on desktop, 2 on
  mobile.

Its diagnosis of why hidden menus fail — low salience, low information scent,
extra work to access, low familiarity — generalises beyond menus. Its
prescription is that mobile-first must not become mobile-only: hamburger menus
may be a necessary compromise on a small screen, but porting them to desktop
where space exists degrades the experience more, not less.

### Signifiers for invisible interactions

Where an interaction leaves no visible trace, the interaction has to be
announced.

- **Gestures.** Contextual swipe suffers precisely from the absence of
  signifiers: not every app supports it, so even familiar users forget to try
  it, especially returning to an app used infrequently
  [[2017-02-12_contextual-swipe]]. Nonstandard swipe behaviour compounds this —
  users expect swipe to delete or remove, and an app that uses it to save
  produces an action nobody will discover. The same article recommends keeping
  swipe consistent within an app, limiting it to destructive actions, keeping
  affected content visible, and providing confirmation or easy undo.
- **The cursor.**
  [[2025-03-18_369_Guide_UX_Curseur_de_souris_natif_et_custom]] treats the
  mouse cursor as an under-used discoverability lever: native browser cursors
  (pointer, text, grab, not-allowed, busy) are universally understood web
  standards, set with a single line of CSS, and can signal an invisible status
  or an available interaction instantly. It argues that when a feature has a
  discoverability problem, changing the cursor is often an excellent fix, with
  essentially no downside. Custom cursors are justified for visual editing
  tools, real-time collaboration and advanced data visualization, but demand
  care over contrast, click precision and multiple states — and the interface
  must never depend on the mouse alone, for accessibility.

### Modes and secondary controls

[[2019-04-14_modes]] identifies modes as a structural discoverability tax:
features that exist only in a specific mode are hard to find and hard to
remember, and the problem is worst for occasional users who must rediscover
them each time. Its remedy for the related mode-slip risk is at least two
independent visual indicators (for instance highlighting plus a cursor change)
so the active mode is obvious to an inattentive user; where mixing modes up
could cause real harm, use separate controls instead.

[[2019-05-12_split-buttons]] describes the same trade-off in a single
component: a split button lowers interaction cost for the dominant action while
consolidating related commands, but users — especially those still learning the
app — may never notice the arrow or the menu behind it, which defeats the
purpose. Its mitigations: separate the arrow from the label with a dividing
line or contrast and keep it always visible rather than on hover; use text
labels rather than icons alone, which improves learnability and enlarges the
target; avoid split buttons on touch (small arrow targets) and for navigation
(use a standard dropdown); and note that persistent split buttons, where the
last choice becomes the default, help power users but confuse new ones by
breaking spatial consistency.

### Promoting genuinely unfamiliar capabilities

When the technology itself is new, users are not looking for it at all.

- **AR.** Most users do not think to look for AR while browsing products, so it
  must be actively promoted [[2020-12-06_augmented-reality-ecommerce-guidelines]]:
  prominent placement near the product image or a strong call to action on the
  product-detail page, and descriptive text labels ("See it in AR", "Try It
  On") rather than the AR cube icon, which is not universally recognised. Hints
  and animations on a first visit are well received, but should not be the only
  mechanism since users dismiss them unread.
  [[2022-11-20_ar-ux-guidelines]] confirms the finding two years later — users
  did not know AR existed in apps they used regularly (Amazon, Ulta, Best Buy,
  Target) — and adds catalogue-level fixes: visual indicators on product
  listings and filtering options for AR-compatible items. It also notes that
  prior gaming experience is what makes AR signifiers legible; non-gamers
  struggle, so icons need descriptive labels and instructions need high
  contrast against unpredictable real-world backgrounds.
- **AI.** [[2025-08-22_ai-information-seeking-keyword-foraging]] frames the AI
  version as a discoverability barrier of a deeper kind: the technology is
  opaque, so users do not know what to ask or how far its capabilities go — "you
  don't know what you don't know". It rejects putting the burden on the user
  (expecting people to write detailed prompts is a high interaction cost, and
  users are not prompt engineers) in favour of systems that ask clarifying
  questions.
  [[2025-04-25_prompt-suggestions]] supplies the corresponding pattern:
  system-generated prompt hints that solve the blank-page problem. It
  distinguishes use-case suggestions (demonstrate capabilities, support
  learnability and creativity), prompt autocomplete (efficiency), and followup
  questions (engagement) — and finds followups currently the most useful,
  because they are tailored to needs the conversation has already established
  rather than generic demonstrations. Good suggestions lead users to explore
  topics they would have missed or assumed impossible.

### When visual cues are not enough

[[2025-10-17_google-ai-mode]] is the strongest counter to the reflex of "just
make it more visible". Four of seven participants had never noticed Google AI
Mode despite multiple access points and a rainbow animation intended to draw
attention: interface familiarity and task-focused habits make users skip new
elements, and vague naming plus poor differentiation from Gemini and AI
Overviews left participants unable to tell the products apart. Its conclusion
is that structural changes are needed beyond visual cues. It also documents the
onboarding trap: AI Mode's welcome page with guidance and prompt suggestions
exists, but users bypass it through default browser search — help text is
useless if people never encounter it.

[[2026-03-20_site-ai-chatbot]] finds the same pattern on site chatbots. The
visibility failures are basic (small icons, no labels, blending into busy
backgrounds — one participant took the launcher for a graphic, and regular
customers skipped it), but visibility alone would not fix it: users carry
skepticism from years of unhelpful bots, the messaging does not communicate
what the bot can do, and people will not experiment to find value that is not
immediately obvious. Where the chatbot duplicates search, filters or navigation
that users have already mastered, discovering it does not help; the value
appears on context-specific product questions and personalised, multivariate
queries.

### Designing for the moment of discovery

[[2025-06-27_complex-apps-users]] situates discoverability in the user journey
rather than in a component. Its three complex-app profiles — the Legacy user
(long tenure, rigid workarounds, protecting fragile productivity rather than
resisting change), the Legend (power user who will leave for a faster tool), and
the Learner (domain expert new to the software) — progress or stagnate
depending on whether capabilities and their benefits are made visible at the
point where learning or an efficiency gain is possible. It rejects treating
Learner struggles as a training problem: even great training and documentation
cannot compensate for poor usability, and deliberate support for
discoverability, learnability, safe exploration and progressive feature
introduction is what turns a Learner into a Legend rather than into a Legacy
user.

### Testing for it

Discoverability is only measurable if the test does not give it away
[[2020-02-09_user-testing-stepped-tasks]]. Stepped tasks present related tasks
with progressively more specific instructions: the first is deliberately broad
and vague, so completing it unaided proves the feature is discoverable, and
subsequent steps deliver micro-hints that separate a findability problem from a
usability one. Two rules make this work: never reuse the UI's own terminology
in the task wording, since it primes users to hunt for that term and inflates
success artificially; and write the steps in advance, because tasks improvised
under time pressure are badly designed. Handing participants written tasks also
preserves the rhythm of observation over conversation and keeps the facilitator
from helping too early.

## Sources (13)

- [[2016-06-26_hamburger-menus]] — Visual prominence is key to navigation discoverability; hidden menus suffer from low salience, low information scent, extra work to access, and low familiarity.
- [[2017-02-12_contextual-swipe]] — lack of signifiers and nonstandard behavior reduce the discoverability of swipe actions.
- [[2019-04-14_modes]] — Mode-specific features have lower discoverability because users may not know the feature exists or how to access it from the current mode.
- [[2019-05-12_split-buttons]] — Small arrow targets and hidden menus have low discoverability, especially for new users who may not recognize the split button pattern.
- [[2020-02-09_user-testing-stepped-tasks]] — Shows how stepped tasks specifically reveal whether users can discover that features exist without being told about them.
- [[2020-12-06_augmented-reality-ecommerce-guidelines]] — making AR features visible and understandable to users who don't expect to find them, through prominent placement, clear labels, and contextual promotions on product pages.
- [[2022-11-20_ar-ux-guidelines]] — AR features hidden in apps lack discoverability; visual indicators on product listings, filtering options, and clear labels help users find and recognize AR-compatible items.
- [[2025-03-18_369_Guide_UX_Curseur_de_souris_natif_et_custom]]
- [[2025-04-25_prompt-suggestions]] — highlights how prompt suggestions reduce barriers to discovering what the AI system can do by presenting examples and possibilities proactively.
- [[2025-06-27_complex-apps-users]] — making system capabilities and their benefits visible and recognizable to users at the point when learning or efficiency improvements are possible.
- [[2025-08-22_ai-information-seeking-keyword-foraging]] — The opaque nature of AI and users' limited understanding of its capabilities creates a discoverability barrier to accessing AI's full potential.
- [[2025-10-17_google-ai-mode]] — Analyzes poor discoverability caused by interface familiarity, task-focus, vague naming, animation ineffectiveness, and lack of differentiation from other Google AI features; structural changes needed beyond visual cues.
- [[2026-03-20_site-ai-chatbot]] — Shows how poorly designed chatbot visibility undermines adoption even when the feature itself could be useful.
