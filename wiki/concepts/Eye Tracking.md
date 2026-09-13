---
type: concept
name: Eye Tracking
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Eye-Tracking Studies"
  - "Eyetracking"
  - "Eyetracking Research"
---

# Eye Tracking

## Definition

Eye tracking is a research method that uses specialised equipment to record
where users look and for how long, producing data about fixations and saccades
on digital and physical interfaces ([[2019-08-18_eyetracking-setup]]). Its
outputs come in three forms: gazeplots of an individual's fixations, gaze
replays as video, and heatmaps aggregating fixations across participants
([[2019-08-18_eyetracking-setup]]). In this corpus it is above all the
instrument that turned "how people read online" from opinion into evidence:
five studies over 13 years, 500+ participants and 750 hours of tracking
([[2020-04-05_how-people-read-online]]), out of which come the named scanning
patterns — F-shaped, layer-cake, spotted, commitment, pinball, lawn mower,
love-at-first-sight, exhaustive review — that the rest of this vault refers to.

The method's value lies less in the pictures than in the interpretation. Raw
fixation counts do not distinguish confusion from engagement
([[2017-10-29_exhaustive-review-eyetracking]]), and heatmaps generated from
unrealistic tasks actively mislead
([[2017-03-19_eyetracking-tasks-efficient-scanning]]). The corpus also uses eye
tracking as a longitudinal instrument, revisiting the same measures across
years to separate what changes with technology from what does not: the F-pattern
after 11+ years ([[2017-11-12_f-shaped-pattern-reading-web-content]]), the
left-leaning bias since 2010 ([[2017-10-22_horizontal-attention-leans-left]]),
banner blindness across three decades
([[2018-04-22_banner-blindness-old-and-new-findings]]). Separately, the term
also names an *input* modality rather than a research method: on the Apple
Vision Pro, gaze is the pointer and a finger pinch is the click
([[2024-07-23_338_Test_de_l_Apple_Vision_Pro_-_Design_review_&_avenir_de_l_ordinateur_spatial]]).

## Practice

### Running a study

- Sample size depends on the output you want: gazeplots and gaze replays give
  qualitative insight with 8–12 participants, while heatmaps need roughly 39
  participants before aggregate patterns mean anything
  ([[2019-08-18_eyetracking-setup]]).
- Calibrate every participant individually — eye shape, face shape and height
  differ — and monitor calibration in real time, because losing it mid-session
  ruins the data ([[2019-08-18_eyetracking-setup]]).
- Set the lab up deliberately: separate monitors for participant and
  facilitator so gaze data (red dots and lines) can be watched live; the tracker
  positioned away from direct overhead lighting; a fixed chair for the
  participant to prevent calibration drift and a rolling chair for the
  facilitator ([[2019-08-18_eyetracking-setup]]).
- Deliver tasks verbally or through the eyetracking software rather than on
  printed sheets, which make participants look away from the tracker
  ([[2019-08-18_eyetracking-setup]]).
- Budget for failure: one to two full days of setup and equipment testing, then
  one to two pilot days before real data collection
  ([[2019-08-18_eyetracking-setup]]).
- Build realistic, task-based studies. Non-realistic tasks produce misleading
  heatmaps that can drive harmful design decisions
  ([[2017-03-19_eyetracking-tasks-efficient-scanning]]).
- Triangulate. The flat-design findings rest on two years of research using
  multiple methods, not eyetracking alone, across 9 sites and 6 domains, with
  results reported at p<0.05; the article also notes the limits openly — 70
  users, small tasks, fine-grained metrics that coarse measures like task time
  would not surface ([[2017-10-15_response-criticisms-flat-design]]).

### Interpreting the data

- Watching the full session beats studying gaze plots alone
  ([[2017-03-19_eyetracking-tasks-efficient-scanning]]).
- Repeated looking has at least three different meanings, and a fixation count
  cannot tell them apart: exhaustive review signals confusion and wasted effort,
  desired exploration signals engaged interest, necessary review signals
  deliberate understanding ([[2017-10-29_exhaustive-review-eyetracking]]).
- Exhaustive review — the "I can't believe it's not there" phenomenon — happens
  when users return to an area convinced the content they expect must be there.
  Two expectations drive it: like information should sit together, and UI
  elements should follow web convention (a logo in the upper left). When a
  convention is violated, users keep checking the familiar location even after
  finding the content elsewhere ([[2017-10-29_exhaustive-review-eyetracking]],
  [[2018-01-07_ux-quiz-2017]]).
- The absence of fixations is data too: it is how banner blindness and the
  hot-potato effect are detected
  ([[2018-04-22_banner-blindness-old-and-new-findings]],
  [[2018-01-07_ux-quiz-2017]]).

### Task drives the pattern

- Gaze is optimised for the current goal. The same page scanned by someone
  looking for prices and someone looking for ratings produces dramatically
  different patterns; users fixate on what serves the task and barely touch the
  rest, an efficient-scanning strategy that follows the principle of least
  effort ([[2017-03-19_eyetracking-tasks-efficient-scanning]]).
- Predictable, consistent layouts let users converge on an optimal scanning
  algorithm quickly: consistent positioning of key information, large bold
  typography for primary elements, adequate white space, short recognisable
  text, comparison tables, consistent photo types, and clear visual
  differentiation of ratings
  ([[2017-03-19_eyetracking-tasks-efficient-scanning]]).
- Task type also changes search behaviour: simple fact-finding concentrates gaze
  on top results, while complex research tasks push users further down, with 20%
  of selections below the fold ([[2019-11-17_pinball-pattern-search-behavior]]).

### Text scanning patterns

- Users scan rather than read, and have for 23 years
  ([[2020-04-05_how-people-read-online]],
  [[2019-08-25_text-scanning-patterns-eyetracking]]).
- Four text patterns, ranked from least to most effective: **F-pattern**
  (inefficient, appears with unstructured prose), **spotted** (fixating on
  styled words), **layer-cake** (heading, then its body section, repeated), and
  **commitment** (reading nearly every word)
  ([[2019-08-25_text-scanning-patterns-eyetracking]]). The layer-cake pattern is
  by far the most effective short of reading everything; commitment requires
  trust in the source, high interest, or real consequences for missing something
  ([[2019-08-25_text-scanning-patterns-eyetracking]]).
- The F-pattern — a horizontal sweep across the top, a shorter horizontal sweep
  in the middle, then a vertical scan down the left — still occurs on desktop
  and mobile 11+ years after its 2006 identification. It is the default when
  text has no formatting, users prioritise efficiency, and engagement is low; it
  is mirrored in right-to-left languages. It is bad for users and businesses
  because content on the right or later in a paragraph simply gets skipped, and
  responsive reflow makes it worse
  ([[2017-11-12_f-shaped-pattern-reading-web-content]],
  [[2019-08-25_text-scanning-patterns-eyetracking]]).
- Other named variants: **marking** (gaze held in place while the page scrolls),
  **bypassing** (skipping repeated leading words), and **commitment**
  ([[2017-11-12_f-shaped-pattern-reading-web-content]]).
- Antidotes are the same across sources: put the important points in the first
  two paragraphs, use headings and subheadings that start with
  information-bearing words, bold key words, group related content visually, use
  bullets and numbers, cut the rest
  ([[2017-11-12_f-shaped-pattern-reading-web-content]],
  [[2019-08-25_text-scanning-patterns-eyetracking]],
  [[2020-04-05_how-people-read-online]]).
- Pull quotes and inline elements disrupt linear reading: users start reading
  carefully, hit one, and drop into light scanning
  ([[2020-04-05_how-people-read-online]]). Reading depth otherwise depends on
  motivation, task type, focus, and the individual reader
  ([[2020-04-05_how-people-read-online]]).

### Where attention lands on the page

- Horizontally, attention leans left: 80% of fixations fall on the left half
  even on 1920×1080 screens, and a 900-pixel width increase moved peak attention
  only 200 pixels right. On SERPs the bias is stronger — 94% left, 60% in the
  leftmost 400 pixels ([[2017-10-22_horizontal-attention-leans-left]]).
- Vertically, the fold has softened but not disappeared: 57% of viewing time
  above the fold (down from 80% in 2010), 74% in the first two screenfuls, 81%
  in the first three; over 40% of viewing time on general websites falls in the
  top 20% of content, and users rarely go past the third screenful
  ([[2018-04-15_scrolling-and-attention]]).
- Practical consequence: critical content and major calls to action belong top
  and left, secondary content in the right rail — and if something must sit on
  the right, raise its visual prominence
  ([[2017-10-22_horizontal-attention-leans-left]],
  [[2018-04-15_scrolling-and-attention]]). Counter false floors created by
  minimalist design and excess white space with scrolling signifiers such as cut
  off text, and test page length with real users
  ([[2018-04-15_scrolling-and-attention]]).
- These positions are learned, not innate. Users spend most of their time on
  other websites, so their expectations come from convention; if every site
  moved navigation right, users would adapt, but an individual deviation just
  forces them to search ([[2017-10-22_horizontal-attention-leans-left]]).

### What attention avoids

- Banner blindness is selective attention: with limited capacity, users learn
  which elements are usually irrelevant and skip them. It has been documented
  across three decades ([[2018-04-22_banner-blindness-old-and-new-findings]]).
- Three triggers: location (top banners, right rails), visual treatment
  (animation, fancy formatting, coloured backgrounds, embedded text), and
  proximity to real ads. Legitimate content carrying any of these signals gets
  ignored too ([[2018-04-22_banner-blindness-old-and-new-findings]]).
- The hot-potato effect: after meeting an ad in a page section, users write off
  the whole section and avoid it, poisoning the legitimate content beside it
  ([[2018-04-22_banner-blindness-old-and-new-findings]],
  [[2018-01-07_ux-quiz-2017]]). On mobile the problem sharpens — inline ads are
  harder to tell from content, and large ads relative to screen size catch the
  eye against the user's intent
  ([[2018-04-22_banner-blindness-old-and-new-findings]]).
- Weak or absent visual signifiers produce a comparable effect: they attract
  less attention than strong traditional cues, which is the real finding behind
  the flat-design study — flat design is not the enemy, weak signifiers are
  ([[2017-10-15_response-criticisms-flat-design]]).
- Recovering a blind area is slow: relevance, not prominence, wins attention
  back, and once users have been trained by a bad design to ignore a region,
  they will not see the better content placed there
  ([[2020-05-31_google-baidu-serp-comparison]]).

### Search-results pages

- The **pinball pattern**: on modern, feature-rich SERPs users scan nonlinearly,
  bouncing between results and features rather than moving down the list. A
  meta-analysis of 471 queries from 2017–2019 studies shows first-position
  clicks falling from 51% in 2006 to 28%, with the 6th position now receiving
  looks in 36% of cases; SERP features drew looks in 74% of cases. Positions 1–5
  have a 10–20% click chance but a 40–80% chance of a look, and users clicked
  past page one in only 2% of queries. Users spent on average 5.7 seconds
  considering results before their first selection (95% CI 4.9–6.5)
  ([[2019-11-17_pinball-pattern-search-behavior]]).
- The pattern is a product of design, not of search itself: it was extremely
  rare on Baidu (1 of 60+ searches), where scanning stayed sequential, because
  Baidu's right rail carries ads and unrelated searches while Google's knowledge
  panels answer the question. Promoted content is fine as long as it is relevant
  to the task ([[2020-05-31_google-baidu-serp-comparison]]).
- The **love-at-first-sight pattern**: in 20% of 377 search instances users
  looked at a single result and nothing else, up from 17% in 2006. It is
  satisficing rather than maximising, enabled by trust in the search engine
  ("Google gullibility", observed cross-culturally), by distinctive SERP
  features that answer the question outright (good abandonment), and by low
  motivation or time pressure or a purely navigational query. The implication
  for content owners is to understand the question precisely and structure the
  answer — lists, tables, definitions — so it can be featured
  ([[2020-07-12_love-at-first-sight-pattern]]).
- Even unclicked, a glance builds awareness and familiarity that helps on later
  searches ([[2019-11-17_pinball-pattern-search-behavior]]).

### Structured content: tables and image–text layouts

- The **lawn-mower pattern**: comparing products in a table, users sweep
  left-to-right, drop a row, then sweep right-to-left, and so on. It follows an
  initial appraisal phase where users read column and row labels to grasp the
  structure ([[2020-12-13_lawn-mower-pattern]],
  [[2020-04-05_how-people-read-online]]).
- Two things break it: excessive length, which makes users lose track of which
  column holds which product and forces repeated returns to the top; and
  unexplained jargon, which produces dense hesitation fixations. Support the
  pattern with fixed headers, narrower navigation, self-explanatory cells,
  grouped yes/no features, minimal repetition, clear terminology, and no
  placeholder content ([[2020-12-13_lawn-mower-pattern]]).
- Zigzag image–text layouts: informational value matters more than alignment.
  When images carry information, zigzag and aligned layouts perform equally
  because users attend to both. When images are decorative, zigzag layouts
  produce stumbling and redirects — including residual fixations, where the gaze
  stays put as the page scrolls — while aligned layouts let users glide past.
  Complex imagery (photos with text, screenshots, heavy detail) compounds it.
  Hence: align decorative images, put informational content on the left,
  top-align text with decorative images, avoid complex early images, and give
  every image a purpose ([[2017-11-26_zigzag-page-layout]]).

### Stability of the findings

- Technology changes quickly, humans do not: fundamental reading behaviours from
  2006 persist even as new patterns appear in response to new design trends
  ([[2020-04-05_how-people-read-online]]).
- Gaze patterns held nearly identical between American and Beijing users despite
  differences in culture, character set and site complexity, suggesting
  universal rather than cultural behaviour
  ([[2020-04-05_how-people-read-online]]).
- But behaviour does shift with design: new frequently-encountered designs
  trigger new patterns, as Google's and Baidu's SERPs show
  ([[2020-05-31_google-baidu-serp-comparison]]), and the design/behaviour
  relationship is codependent — layouts and viewing habits reinforce each other
  ([[2017-10-22_horizontal-attention-leans-left]]).

### Gaze as an input modality

Distinct from the research method, gaze can be the interface itself. On the
Apple Vision Pro the user's gaze acts as the primary pointer and a finger pinch
as the click, a combination described as extremely natural and adopted within a
minute, working even with the hands outside the field of view. Shadows and a
light audio cue on contact with nearby virtual interfaces complete the illusion
of manipulating physical objects
([[2024-07-23_338_Test_de_l_Apple_Vision_Pro_-_Design_review_&_avenir_de_l_ordinateur_spatial]]).

## Sources (18)

- [[2017-03-19_eyetracking-tasks-efficient-scanning]] — Discusses gaze plots, fixations, saccades, and the eye-mind hypothesis as tools for understanding how users process web pages in relation to their tasks.
- [[2017-10-15_response-criticisms-flat-design]] — describes triangulation of eyetracking with other methods over two years to validate findings about visual attention and design.
- [[2017-10-22_horizontal-attention-leans-left]] — demonstrates consistent viewing patterns despite technological changes and larger screens over seven years.
- [[2017-10-29_exhaustive-review-eyetracking]] — demonstrates how eyetracking metrics must be interpreted through behavioral context, not raw fixation counts.
- [[2017-11-12_f-shaped-pattern-reading-web-content]] — establishes persistence of the F-pattern across 11+ years and multiple scanning pattern variants.
- [[2017-11-26_zigzag-page-layout]] — demonstrates residual fixations and redirect behavior revealing how layout predictability affects scanning.
- [[2018-01-07_ux-quiz-2017]] — Research method measuring where users look on a page; reveals patterns like exhaustive review (repeated fixation on expected areas) and hot-potato scanning (avoidance of certain areas).
- [[2018-04-15_scrolling-and-attention]] — using eyetracking data to reveal attention distribution and identify which interface elements capture user focus.
- [[2018-04-22_banner-blindness-old-and-new-findings]] — using eyetracking data to reveal which page sections receive no attention due to ad-like characteristics.
- [[2019-08-18_eyetracking-setup]] — A method using specialized equipment to measure eye fixations and saccades, producing data about visual attention patterns on digital and physical interfaces.
- [[2019-08-25_text-scanning-patterns-eyetracking]] — Fixation patterns revealed through eyetracking show how users navigate text in predictable ways based on visual structure and styling cues.
- [[2019-11-17_pinball-pattern-search-behavior]] — uses eyetracking research findings to demonstrate the pinball pattern and distribution of attention across SERP elements.
- [[2020-04-05_how-people-read-online]] — demonstrates the methodology of tracking user gaze across studies spanning 13 years to identify patterns and measure content element attention.
- [[2020-05-31_google-baidu-serp-comparison]] — methodology for studying gaze patterns on SERPs, revealing pinball patterns on Google and sequential patterns on Baidu.
- [[2020-07-12_love-at-first-sight-pattern]] — eye-tracking research methods used to document the love-at-first-sight pattern over time.
- [[2020-12-13_lawn-mower-pattern]] — demonstrates how eyetracking research reveals predictable scanning patterns users adopt when processing structured data.
- [[2024-07-23_338_Test_de_l_Apple_Vision_Pro_-_Design_review_&_avenir_de_l_ordinateur_spatial]]
- [[2024-01-23_laws-of-ux_10-8-von-restorff-effect]] — A research technique measuring where users look and how they interact with interfaces, providing objective data about where users look, how they navigate, what they ignore, and their emotional responses; the chapter recommends pairing it with other research methods because of its limitations.
