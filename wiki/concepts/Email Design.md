---
type: concept
name: Email Design
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Email Communication"
---

# Email Design

## Definition

Email design is the craft of making marketing and transactional messages
readable, scannable and actionable across email clients and devices whose
rendering the designer does not control; it differs significantly from web
design because of those client limitations
[[2017-12-17_visual-newsletters]]. The sources cover both families of message —
newsletters and campaigns on one side, order confirmations, shipping
notifications and other automated mail on the other
[[2018-07-01_state-transactional-email]] — plus the exit path, the unsubscribe
flow, which they treat as part of the same design surface
[[2018-04-29_unsubscribe-mistakes]].

Two long-run shifts frame the current practice. First, the constraints loosened:
spam fear has receded thanks to spam-blocking tools, HTML, images and emojis are
now ordinary, and email clients handle responsive layouts well, so many old
formatting and broken-link problems are gone
[[2017-08-13_newsletters]], [[2018-07-01_state-transactional-email]]. Second,
the bar moved from deliverability to relevance and restraint: spam is now
defined by the recipient as anything irrelevant, whatever the opt-in status
[[2017-08-13_newsletters]], and several decorative techniques that marketers
assume help — full-graphic layouts, animated GIFs, emojis in subject lines —
measurably hurt perception [[2017-12-17_visual-newsletters]],
[[2020-03-15_gif-emails]], [[2020-06-28_emojis-email]].

## Practice

### Layout and structure

- Single-column layouts with full-width imagery outperform the dense
  multicolumn designs previously common on desktop; users described those as
  cluttered and outdated [[2017-08-13_newsletters]],
  [[2017-12-17_visual-newsletters]].
- Keep subscription friction low: users prefer short, simple signup forms
  embedded in footers to lengthy explanations [[2017-08-13_newsletters]].
- Design for mobile reading as the default; mobile impatience means users want
  quick answers, and the message must work on both small and large screens
  [[2018-07-01_state-transactional-email]], [[2017-08-13_newsletters]].
- Use preheader text as real inbox information rather than filler or an
  overflow of the subject line [[2018-07-01_state-transactional-email]].

### Imagery, without the flyer trap

- Users expect the same high-quality, large-scale imagery they meet on the web,
  and relevant large images improve reception; generic stock photography and
  small thumbnails feel outdated and add clutter
  [[2017-12-17_visual-newsletters]].
- The failure mode is the flyer-style email, where the whole message is one
  embedded graphic. [[2017-12-17_visual-newsletters]] lists its costs: poor
  legibility from low contrast and decorative fonts, no typographic hierarchy
  when all text is equally emphasised, content pushed below excessive negative
  space on mobile, preheader text the client cannot generate, and disappearing
  clickability signifiers.
- The corrective: keep real text, restore hierarchy through varied weight and
  size, put important information where it is immediately visible rather than
  under a large hero, and make interactivity obvious with prominent buttons,
  coloured or underlined links and clear labels
  [[2017-12-17_visual-newsletters]].

### Animation and emoji: what the tests found

- Animated GIFs tested worse than static versions. Across 121 respondents and 14
  marketing emails, animated versions drew 40% more negative word selections and
  30% fewer positive ones (annoying 31% vs 14%, distracting 20% vs 11%, dull 20%
  vs 13%), positive sentiment dropped by 165%, and static emails were rated more
  valuable (3.69 vs 3.24) and more trustworthy (4.34 vs 3.90, the statistically
  significant difference) [[2020-03-15_gif-emails]].
- Animation is not banned but must be purposeful and subtle, for instance
  demonstrating a product feature; meaningless movement reads as a gimmick, and
  animating a boring email does not make it appreciated
  [[2020-03-15_gif-emails]].
- Emojis in subject lines attract the eye without earning the open. In mixed
  inboxes, emoji emails were considered more often (33% vs 9% of selections),
  but users attributed that to the visual character rather than the message; all
  else equal, the emoji did not raise intent to open that email
  [[2020-06-28_emojis-email]].
- Emojis also cost sentiment: 26% more negative sentiment, "dull" and "boring"
  chosen twice as often, "straightforward" chosen more for the plain versions,
  and lower perceived value, with no difference in trustworthiness
  [[2020-06-28_emojis-email]]. Reserve them for cases where they add genuine
  context or emotional value, and use them sparingly to preserve the salience
  effect [[2020-06-28_emojis-email]].
- The sources are not fully aligned in tone here: [[2017-08-13_newsletters]]
  records emojis and animated GIFs as having taken a major role in email design
  alongside full-width imagery, describing the trend, while the later
  experimental work [[2020-03-15_gif-emails]] and [[2020-06-28_emojis-email]]
  finds those two specific devices reduce perceived value. The image findings,
  by contrast, agree across all three.

### Relevance and personalization

- Users now call a message spam when it does not match their interests, not when
  it is unsolicited; personalization built on known user data draws strong
  positive responses while generic broadcasts are dismissed
  [[2017-08-13_newsletters]].
- The emotional attachment users once had to newsletters has faded as inbox
  volume grew; timely, tailored content is what still builds loyalty, and the
  challenge is standing out without sacrificing usability
  [[2017-08-13_newsletters]].

### Transactional email

- Transactional mail has improved on average — a diary study rated it 5.9 out of
  7 on desirable characteristics — but some companies still deprioritise it and
  miss the relationship it could build [[2018-07-01_state-transactional-email]].
- Put core utility first: communicate the information quickly, easily and
  completely, answering every question so the user need not contact the company
  or click through unless necessary [[2018-07-01_state-transactional-email]].
- Keep marketing restrained. Emails cramped with ads or sent too often annoy
  users, and an aggressive sales approach wastes the relationship-building
  opportunity. Cleverness and entertainment are allowed only where they do not
  interfere with the core message [[2018-07-01_state-transactional-email]].
- Keep automated messages current with operations. During COVID-19, order
  confirmations, shipment notifications and pickup emails had to reflect new
  delays and procedures, since these are often the primary reference customers
  keep; email was also the channel for step-by-step instructions on unfamiliar
  services such as curbside pickup [[2020-06-14_emergency-covid]].

### The unsubscribe experience

- Treat it as designed, not tolerated: failing users at this point damages brand
  loyalty and pushes them to report the mail as spam, which harms deliverability
  [[2018-04-29_unsubscribe-mistakes]].
- Footer fine print that is small on desktop becomes untappable on mobile; give
  the unsubscribe link visual weight through contrast or font treatment,
  conventional clickable styling, and the literal label "Unsubscribe" rather
  than "Manage subscriptions" [[2018-04-29_unsubscribe-mistakes]].
- Make it one click. Preference pages full of checkboxes frustrate people who
  have already decided, and non-standard checkbox logic (checked meaning "do not
  subscribe") produces errors because users read a checked box as a current
  subscription [[2018-04-29_unsubscribe-mistakes]].
- Remove added friction — required login, personal information, feedback before
  confirmation — confirm on the website rather than by follow-up email, and use
  a tone that respects the decision [[2018-04-29_unsubscribe-mistakes]].

## Sources (7)

- [[2017-08-13_newsletters]] — newsletter design practices have evolved from text-heavy multicolumn layouts to single-column, image-rich designs optimized for mobile rendering.
- [[2017-12-17_visual-newsletters]] — Creating marketing and transactional messages that are readable, scannable, and support interaction across diverse email clients and devices; differs significantly from web design due to client limitations.
- [[2018-04-29_unsubscribe-mistakes]] — optimizing email layouts for unsubscribe discoverability and mobile usability in footer areas.
- [[2018-07-01_state-transactional-email]] — The article addresses HTML/image usage, preheader text optimization, mobile responsiveness, and structure considerations for effective transactional email design.
- [[2020-03-15_gif-emails]] — shows that animated GIFs in marketing emails reduce user perception of value and trustworthiness compared to static alternatives.
- [[2020-06-14_emergency-covid]] — best practices for including critical operational information in automated transactional emails.
- [[2020-06-28_emojis-email]] — empirical findings on how visual elements in subject lines affect user perception and engagement.
