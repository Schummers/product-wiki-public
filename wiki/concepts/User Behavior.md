---
type: concept
name: User Behavior
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "AI User Behavior"
  - "Behavior Patterns"
  - "Mobile User Behavior"
  - "User Behavior Change"
  - "User Behavior Patterns"
  - "User Motivation"
---

# User Behavior

## Definition

User behavior is what people actually do with interfaces, as opposed to what
they say they do or what designers assume they will do. Across these sources it
is treated as observable and largely predictable: people allocate attention in
recurring ways, they carry expectations learned on other sites, and they make
decisions through psychological shortcuts rather than through full rational
evaluation. [[2024-01-10_psychology-study-guide]] frames the whole territory as
psychology applied to technology, and states the working premise the rest of the
corpus shares: the best designs are built for people as they really are, not who
designers wish they were.

Two forces run through the material and pull in opposite directions. On one
side, behavior is remarkably stable: [[2020-05-24_25-years-ux-wins-fails]] finds
that predictions grounded in user conservatism and preference for simplicity
held for twenty-five years, while optimistic predictions about systemic change
failed, and [[2018-04-22_banner-blindness-old-and-new-findings]] documents the
same avoidance behavior across three decades. On the other side, behavior is
shaped by what the environment teaches: attention patterns are adaptations to
convention ([[2017-10-22_horizontal-attention-leans-left]]), information-seeking
purposes have shifted measurably over twenty-two years
([[2020-01-26_information-seeking-behavior-changes]]), an external shock
rewrites routines wholesale ([[2020-08-30_covid-changed-users]]), and new
technology generates behaviors that did not previously exist
([[2023-09-24_accordion-editing-apple-picking]]). The practical consequence
these sources draw is the same in both cases: behavior must be observed rather
than assumed.

## Practice

### Attention is scarce and unevenly distributed

Users direct attention to a subset of what is on screen, and the distribution is
consistent enough to design against. Horizontally, attention leans left: 80% of
fixations fall on the left half of a maximized page, and on search results pages
94% fall on the left with 60% in the leftmost 400 pixels
([[2017-10-22_horizontal-attention-leans-left]]). Vertically, attention
concentrates at the top: over 40% of viewing time falls in the top 20% of
content, 57% above the fold, and 81% within the first three screenfuls, with
users rarely scrolling past the third
([[2018-04-15_scrolling-and-attention]]). [[2024-01-10_psychology-study-guide]]
generalises the mechanism: attention is limited, selective, and subject to
change blindness.

Note the movement between two of these sources: the fold has weakened but not
disappeared. [[2018-04-15_scrolling-and-attention]] reports 57% of viewing time
above the fold against 80% in 2010, so the barrier has moved down roughly to the
third screenful rather than vanished.

Practical guidance the sources converge on: place critical content top and left,
give the right rail only secondary content and raise its visual prominence if it
must carry something important
([[2017-10-22_horizontal-attention-leans-left]]); keep high-priority content and
major calls to action above the fold, and add scrolling signifiers such as text
cut off at the edge to counter false floors created by minimalist layout and
excess white space ([[2018-04-15_scrolling-and-attention]]).

### Scanning patterns and reading behavior

The F-shaped pattern (horizontal sweep at the top, shorter horizontal sweep
lower, then a vertical scan down the left) persists on desktop and mobile, but
[[2017-11-12_f-shaped-pattern-reading-web-content]] insists it is one pattern
among several: layer-cake (heading to heading), spotted (searching for a
specific item), marking (fixed gaze during scroll), bypassing (skipping repeated
opening words), and commitment (full reading). It appears when text is
unformatted, engagement is low, and users are optimising for efficiency, and it
is the default when nothing pulls the eye toward meaningful content. The same
source calls the pattern bad for users and businesses, since it makes people
miss content merely for sitting on the right or lower down.
[[2019-01-06_ux-quiz-2018]] states the more neutral version: the pattern is
neither inherently good nor bad, design either supports or interferes with it.
These two framings sit side by side in the corpus and are not reconciled.

The antidotes are formatting rather than exhortation: important points in the
first two paragraphs, headings and subheadings, bolded key words, visually
grouped related content, bullets and numbers, headings starting with
information-bearing words, and cutting unnecessary content
([[2017-11-12_f-shaped-pattern-reading-web-content]]).

On search results, scanning is no longer linear at all.
[[2020-04-26_key-serp-features]] describes a pinball pattern: users bounce
between SERP features and organic results according to visual emphasis and
expected benefit, sometimes keep reading a knowledge panel after clicking
through, and often end the task on the results page itself because a feature
answered the question at near-zero interaction cost.

### Learned conventions and expectation

Several sources treat behavior as literacy acquired elsewhere.
[[2017-10-22_horizontal-attention-leans-left]] states it plainly: users spend
most of their time on other websites, so viewing patterns follow what other
sites taught them, and design and behavior reinforce each other. Deviating
individually forces users to search; if every site moved navigation to the
right, users would adapt.

[[2017-10-29_exhaustive-review-eyetracking]] names the failure mode this
produces. Exhaustive review is repeated returning to the same area because the
user believes the expected content must be there. It has two drivers: the
expectation that like information appears together, and web conventions about
where elements live (logo upper left, and so on). It looks like engagement in
raw fixation counts but signals confusion, which is why that source distinguishes
it from desired exploration and from necessary review. The remedies are to place
related content together, use clear labels, follow convention, and test any
non-standard design heavily.

The same conditioning applies to search: because users' mental models of search
are formed by the dominant search engine, internal site search should adopt
SERP-feature conventions rather than invent its own
([[2020-04-26_key-serp-features]]).
[[2016-01-10_ux-quiz-15]] adds the localisation cues users read to know where
they are: logo, breadcrumbs, and window title, but not the footer.

### Filtering and avoidance

Banner blindness is presented as selective attention rather than annoyance:
users learn which elements are typically irrelevant and stop looking at them
([[2018-04-22_banner-blindness-old-and-new-findings]]). Three triggers are
described: location (top banners, right rails), visual treatment (animation,
fancy formatting, coloured backgrounds, embedded text), and proximity, via the
hot-potato phenomenon where one ad in a region leads users to write off the
whole region. Mobile makes this harder to manage, since screen size both makes
ads harder to distinguish from content and makes large ads impossible to avoid.
The design implication is symmetrical: legitimate content must not look like an
ad, and ads must not poison the content next to them.
[[2020-05-24_25-years-ux-wins-fails]] confirms banner and format blindness as
one of the durable findings across decades.

### Decision-making, motivation, and friction

Users do not evaluate options rationally.
[[2016-06-19_prospect-theory]] describes loss aversion (losses loom larger than
gains, small probabilities are overweighted), certainty bias (a small certain
reward preferred over a chance at a larger one), the isolation effect (elements
common to both options are ignored, so only differentiators drive the choice),
and framing effects. It draws an experiential corollary: users react far more
strongly to moments of loss, that is frustration or confusion, than to things
working, and remember the bad far longer than the good.
[[2024-01-10_psychology-study-guide]] catalogues the same family more broadly:
satisficing, choice overload, anchoring, availability heuristic, confirmation
bias, negativity bias, false-consensus effect, plus Gestalt grouping, the
recognition-over-recall rule, and Fitts's Law.

Commitment is the lever [[2018-03-04_commitment-consistency-ux]] develops:
people feel personal and social pressure to act consistently with what they have
already committed to, public commitments bind harder than private ones, and the
effective sequence is a small low-stakes first step followed by gradually larger
ones. It attaches two constraints: the request must match the trust the
relationship has earned (early on, even asking for an email address reads as
high stakes), and any commitment requiring real work will be refused regardless
of stakes. Its formulation of the failure case is that an all-or-nothing design
delivers nothing from most users.

[[2026-06-05_behavioral-economics-for-ux]] turns this into a procedure for the
intention-action gap. Its 3B framework separates Behavior, Barriers, and
Benefits: define the target behavior unusually specifically (what the user does,
when, and what completion looks like, so "select a plan in one session" rather
than "increase memberships"), map every step users actually take, name the
psychological barrier at each moment (attention, cognitive load, status quo
bias, mental models), then pick a single barrier to remove or benefit to
strengthen, write a hypothesis, and test it against a baseline. It notes that
this friction is often invisible to usability testing alone, and lists COM-B,
the Fogg Behavior Model, and EAST as alternative structures for the same work.

Motivation is treated as a need to be met, not a resource to be extracted.
[[2022-01-09_autonomy-relatedness-competence]] applies self-determination theory:
autonomy (control over configuration, customisation, pacing, which also makes
users value the product more through invested effort), relatedness (built slowly
through many small interactions, by messaging users find relevant and by
enabling communication between people), and competence (best supported by
just-in-time pull help rather than upfront tutorials). It flags that the three
can conflict, with wizards as the example: they raise competence while cutting
autonomy, and only user testing settles which trade-off a given audience wants.
It also claims the payoff extends to obligatory tasks, not just voluntary ones.

Interaction cost is the recurring throttle.
[[2024-01-10_psychology-study-guide]] states it directly as the determinant of
whether users will attempt an action; [[2018-04-15_scrolling-and-attention]]
attributes the drop-off down long pages to the cost of scrolling;
[[2020-04-26_key-serp-features]] attributes the pull of SERP features to their
near-zero cost; [[2019-11-03_mobile-microsessions]] treats time on task as
inversely proportional to usability.

### Named behavior patterns

The corpus accumulates a vocabulary of specific observed behaviors:

- **Page parking** — opening many pages in rapid succession in browser tabs to
  keep them for later, distinct from bookmarking or memorising
  ([[2016-01-10_ux-quiz-15]]).
- **The Vortex** — rapid, frequent switching among windows or tabs, unplanned
  and distinct both from deliberate tab-hoarding for later reference and from
  ordinary window switching ([[2019-01-06_ux-quiz-2018]]).
- **Filling silence** — playing television, music, or podcasts as background
  while doing something else, and reaching for a phone at every waiting moment.
  [[2018-11-18_filling-silence-digital-noise]] reports the content often matters
  less than the act, finds the pattern across the US, China, and other field
  sites, and links it to the Vortex sense of being out of control. Attitudes
  differ: some participants felt trapped by the compulsion, others felt in
  control and untroubled. The same source states that products are deliberately
  designed to sustain the behavior.
- **Microsessions** — sessions under fifteen seconds in which a user completes a
  task; over 40% of mobile usage
  ([[2019-11-03_mobile-microsessions]]). Supporting them means external entry
  points that bypass launching the app: self-sufficient notifications that carry
  a fully formed idea and their own actions, self-contained untruncated widgets,
  quick actions covering genuinely frequent tasks rather than rare features, and
  voice assistant integration. That source argues the ROI is high even at low
  adoption because implementation effort is minimal.
- **Accordion editing and apple picking** — with generative AI, users repeatedly
  ask for expansion and contraction until the output is the right length (using
  word-count limits and forced ranking such as "top 5"), and reference specific
  pieces of earlier responses in new prompts
  ([[2023-09-24_accordion-editing-apple-picking]]). Both are made painful by the
  endlessly scrolling chat window, which forces long scrolling and loses users
  during comparison. That source reads these as friction that shouldn't exist
  rather than as natural behavior, and calls for compartmentalised responses,
  point-to-select referencing, and direct editing without regeneration. Most
  participants still finished their work in external tools.

### Behavior changes, and what it means for research

[[2023-09-24_accordion-editing-apple-picking]] argues AI is actively creating
new behaviors, comparing it to how the growth of online information made search
the dominant information-seeking behavior.
[[2020-01-26_information-seeking-behavior-changes]] measures a twenty-two-year
shift: Understand activities rose from 24% to 40% of critical internet use while
Compare/Choose fell from 51% to 36%, passive acquisition through exploration and
notifications rose from 4% to 14%, smartphones now account for 42% of critical
incidents, 28% of cases involve social interaction, and the content categories
have widened to entertainment, hobbies, home and family, and pets. Its design
conclusion is that comprehensive educational content, not appealing design, is
why users come.

[[2019-06-02_creepiness]] describes adoption of privacy-invasive technology as a
trajectory rather than a verdict: an explicit cost-benefit calculation whose
threshold moves as familiarity and observed benefit grow. It insists the benefit
must be concrete, since vague promises of a better experience do not convince,
that users are spread across a spectrum (digital voyagers comfortable trading
data, digital pragmatists wary of fraud, and outright refusers), that
collectivist cultures show lower creepiness thresholds than individualist ones,
and that transparency about what is collected helps users cross the threshold.

[[2020-08-30_covid-changed-users]] catalogues five kinds of pandemic-driven
change: behavioral (remote work, homeschooling, home exercise, online shopping,
telehealth), psychological (anxiety, depression, shifted priorities, requiring a
softer brand voice and no high-pressure selling), segmentation (risk tolerance
and living situation creating new user groups and requiring persona updates),
regional (different infection rates, policies, and restrictions per market), and
temporal (no way to know which changes are permanent). Its position is that
research is risk reduction, so faster change calls for more research, not less,
and that each organisation must study its own users rather than borrow
conclusions.

Set against this, [[2020-05-24_25-years-ux-wins-fails]] argues the opposite half
of the truth: behaviors rooted in fundamental human perception are stable over
decades, users are conservative and prefer simplicity, and staying a few years
behind the technology curve is optimal for usability. It also notes that small-N
qualitative testing with five users produced most of the durable insights.
The two positions are compatible in the corpus rather than contradictory: what
people fundamentally are changes slowly, what they are currently doing changes
fast.

### Trust in system output

[[2024-04-12_3-types-calculator]] observes that behavior around decision-support
tools varies by tool type. With conversion calculators, users trust the output
if they trust the provider and do not question the arithmetic. With prediction
calculators, they trust complex tools more than simple ones, precisely because
complexity leaves them no way to interrogate the algorithm. With recommendation
calculators, they take the advice seriously, sometimes above their own judgment,
while remaining aware the recommendation is not disinterested. The source draws
a responsibility from this: since users may base important decisions on these
outputs, accuracy is on the designer, and experienced users will not need the
tool at all.

## Sources (23)

- [[2016-01-10_ux-quiz-15]] — addresses specific behaviors like page parking (using tabs to save items for later), navigation patterns that reveal user intent, and how users interact with different control types in various contexts.
- [[2016-06-19_prospect-theory]] — Prospect theory explains why users often make seemingly illogical choices and how context, framing, and perception of risk shape their behavior in digital interfaces.
- [[2017-10-22_horizontal-attention-leans-left]] — shows that attention patterns are learned through exposure to other websites and represent adaptation to convention.
- [[2017-10-29_exhaustive-review-eyetracking]] — explains how web-literacy and learned conventions shape where users look and what they expect.
- [[2017-11-12_f-shaped-pattern-reading-web-content]] — explains that F-pattern reflects user efficiency-seeking behavior, not preference for that content arrangement.
- [[2018-03-04_commitment-consistency-ux]] — understanding how users remain consistent with their past decisions and commitments to themselves and others.
- [[2018-04-15_scrolling-and-attention]] — understanding how users predictably allocate visual attention when scanning pages, prioritizing top content over lower sections.
- [[2018-04-22_banner-blindness-old-and-new-findings]] — understanding how users selectively filter stimuli based on learned associations with irrelevant elements.
- [[2018-11-18_filling-silence-digital-noise]] — recurring user behaviors around device engagement and how they reflect deeper psychological needs and design-induced habits.
- [[2019-01-06_ux-quiz-2018]] — Observable patterns in how users interact with digital systems, including the Vortex (rapid tab-switching), tab-hoarding (opening multiple tabs for later), and others.
- [[2019-06-02_creepiness]] — Adoption of privacy-invasive technologies follows predictable patterns: initial wariness, increasing familiarity, growing perception of benefits, eventual acceptance.
- [[2019-11-03_mobile-microsessions]] — characterizes microsession behavior and patterns of mobile usage, showing how users complete frequent, time-critical tasks.
- [[2020-01-26_information-seeking-behavior-changes]] — Documents major shifts in how users seek and interact with information online, showing increased emphasis on learning and understanding rather than purchase decisions.
- [[2020-04-26_key-serp-features]] — details the shift from linear scanning to pinball patterns and post-click viewing behaviors that SERP features trigger.
- [[2020-05-24_25-years-ux-wins-fails]] — identification of stable user behaviors (conservatism, preference for simplicity, resistance to change) that have proven predictive over decades.
- [[2020-08-30_covid-changed-users]] — Pandemic-driven changes include behavioral shifts (what activities people do), psychological shifts (anxiety and priorities), changes in user grouping (risk tolerance), regional variations, and temporal uncertainty about duration.
- [[2022-01-09_autonomy-relatedness-competence]] — Meeting users' needs for autonomy, relatedness, and competence increases their motivation to use products and provides deep delight, even when performing tasks they have to do rather than want to do.
- [[2023-09-24_accordion-editing-apple-picking]] — Accordion editing and apple picking are new behaviors driven by limitations in current AI tools; the interface creates friction that shouldn't exist.
- [[2024-01-10_psychology-study-guide]] — psychological principles explain why users behave as they do, including common patterns, biases, and response to design elements.
- [[2024-04-12_3-types-calculator]] — examines how users interact differently with conversion, prediction, and recommendation calculators based on complexity and trust factors.
- [[2026-06-05_behavioral-economics-for-ux]] — Barriers make behavior harder; benefits make it feel worthwhile; understanding both at each step of a journey enables targeted interventions that increase follow-through on intentions.
- [[2024-01-23_laws-of-ux_01-preface]] — The observable patterns of how people interact with products and systems, which psychology helps explain and which designers can use to inform design decisions.
- [[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]] — explained through operant conditioning: behavior shaped by variable reinforcement schedules, defaults, friction removal, and algorithmic personalization that keeps users on platforms.
