---
type: concept
name: Localization
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Cultural Design"
  - "International UX"
  - "Internationalization"
---

# Localization

## Definition

Localization is the adaptation of a product to the mental models, conventions
and context of use of an audience other than the one it was designed for. It is
not a synonym for translation: [[2021-03-21_crosscultural-design]] places the
two on a spectrum, with pure translation (same design, different language) at
one end and full localization (different visual presentation, content strategy
and interaction patterns per culture) at the other, and most products sitting
somewhere in between, adapting only specific elements. A design built for a
domestic audience often fails abroad not because the words are wrong but because
the underlying assumptions — about formats, units, trust signals, device
ownership, how people get online — do not hold.

The sources treat localization as an empirical question rather than a stylistic
one. [[2016-11-06_china-website-complexity]] is explicit that impressions formed
by looking at a foreign site, without being able to use it, are not a valid user
experience assessment; [[2021-03-21_crosscultural-design]] insists that
localization decisions be grounded in research with the target audience and
validated by testing with them. At the same time, the corpus is clear that
localization does not suspend general usability principles:
[[2016-11-06_china-website-complexity]] finds the same well-documented problems
(poor search, carousels, inconsistent navigation, intrusive advertising) hurting
Chinese users as Western ones, and concludes that clarity, visual hierarchy,
legible text and standard interface elements improve usability regardless of
regional design tradition.

## Practice

### Decide how far to localize

[[2021-03-21_crosscultural-design]] gives the criteria for placing a product on
the translation-to-localization spectrum: the cultural heterogeneity of the
audience within each language (localize specifically for a large, culturally
distinct subgroup; fall back to a culturally neutral international version for
smaller ones), how far cultural factors affect actual product usage, brand image
considerations, and the potential value of the market. The more a product is
involved in daily life, touches organizational hierarchies, or requires several
people to collaborate, the more localized it should be. The same source suggests
Hofstede's cultural dimensions and high-context versus low-context culture theory
as frameworks for identifying where the target audience differs from the domestic
one and where localization will pay off most.

Localization also carries a brand signal in both directions: a foreign design
aesthetic can build a luxury image, while visibly localized components (the
source's example is WeChat integration) signal that the company understands local
users and invested in them ([[2021-03-21_crosscultural-design]]).

### Ground it in research, not appearance

- Do not judge a foreign market's conventions by looking at its sites; test with
  native users. [[2016-11-06_china-website-complexity]] found that expatriates
  and foreigners read Chinese sites as overly complex, while native participants
  saw the same density as normal and traditional and appreciated it more than
  foreign participants did — yet both groups struggled with the same underlying
  usability defects.
- Test after localizing, not only before. [[2021-03-21_crosscultural-design]]
  argues that usability testing with international users surfaces mental models,
  preferences and context-of-use factors that upstream research alone misses.
- Recruit across the regions you serve. [[2022-12-11_time-zone-selectors]] ran
  moderated and unmoderated studies across the US, Australia, the UK and Germany,
  and found regional splits that a single-country study would have hidden — GMT
  was only significantly more familiar than UTC for UK-based users.
- Designers' assumptions about the "logical" organization frequently conflict
  with what users expect ([[2022-12-11_time-zone-selectors]]).

### Formats, units and other regional conventions

Several sources converge on the same failure mode: a data format that is
unambiguous to the designer is ambiguous or unreadable to a user elsewhere.

- **Dates.** [[2017-01-22_date-input]] notes that "10/11/2016" reads as October
  11 or November 10 depending on where the user learned to write dates, and that
  date-entry fields are culture dependent. Its remedies are to spell out month
  names, separate the components, or use a calendar picker with spelled-out
  months — and, when typing is allowed, to parse whatever separators the user
  chose (dashes, slashes, spaces, dots) instead of imposing one format.
- **Sizes and measurements.** [[2022-04-24_sizes-measurements-ecommerce]]
  separates two cases: a localized site should list local sizes prominently
  alongside the original ones so users never look up a conversion, while an
  international site needs a comprehensive chart covering several regional
  systems, optionally filterable by country. Because brands vary, a single chart
  is not enough — brand-specific guides, body dimensions (bust, waist, hip) and
  per-size product measurements let users match a real body rather than an
  abstract label, provided the measurement method is documented. On mobile, put
  the original size and the user's local size in adjacent columns to avoid
  scrolling across a wide table.
- **Time zones.** [[2022-12-11_time-zone-selectors]] reports that 73% of
  participants could name their time zone but only 34% knew their UTC offset, so
  offset-based organization defeats them; they expect alphabetical order and
  assume a list is broken when it is not. Search is essential (nearly all
  participants tried to search when the field was disabled), city is the most
  common first search term (44%, ahead of time-zone names at 24%), grouping by
  continent measurably helps offset-ordered lists, and pre-selecting or
  highlighting the user's own zone reduces effort.

### Language, country and currency controls

[[2022-03-27_language-switching-ecommerce]] addresses the switcher itself, noting
that international customers often hesitate to shop in a foreign language even
when they can read it:

- Default to the browser's language setting rather than adding a step; if
  detection is unreliable, ask rather than guess wrong.
- Place the switcher in a top corner on desktop, where users look for utility
  features; on mobile, put it above the fold or in the navigation, because the
  top-right corner is taken by account or cart links.
- Write each language's name in that language ("Español", not "Spanish"), and
  combine several cues — flag, currency symbol, language name — to make the
  control discoverable.
- Let language, country and currency change independently, so a user can read in
  one language while shopping from another country.

[[2022-04-24_sizes-measurements-ecommerce]] adds the business case for this kind
of adaptation: a useful size guide lowers the return rate and the volume of
support tickets, both expensive.

### Trust and credibility conventions

[[2017-09-03_credibility-china]] shows that what makes a site believable is
itself local. Chinese shoppers, concerned about counterfeits, look for evidence
of local presence (a physical store or distributor makes an organization feel
tangible and accountable), actively search for the "official website" and read
search-engine results as legitimacy signals, weigh detailed before-and-after
photos and testimonials carrying direct contact information, and prefer online
chat over the phone so they can prepare questions and keep a record. The same
source warns of a halo effect in the other direction: one poorly produced element,
such as a low-quality video, can undermine an otherwise well-designed site. It
frames all of this as localization going beyond translation, into region-specific
conventions, pricing presentation and search-engine tactics.

### Context of use: devices, infrastructure, habits

- **How people got online shapes what works.**
  [[2018-09-02_mobile-login-china]] found Chinese users had far fewer
  password problems than North American ones, because mobile-first adoption made
  QR-code login and SMS one-time passwords viable and made the phone number, not
  the email address, the primary identifier. Desktop-first societies inherited
  email-based identification, and the same patterns face adoption barriers there:
  QR scanners are less ubiquitous and there is social resistance to sharing a
  mobile number. Both mechanisms shift authentication from what the user knows to
  what the user has.
- **Device ownership is not universal.** [[2016-11-27_app-lockers]] describes
  phone sharing among Indian families and friends as culturally normal — pooling
  resources, convenience, and children and teenagers rarely owning a handset —
  which produced app lockers as a local privacy solution: per-app PIN or pattern
  locks, sometimes with a stealth mode that hides the locker itself to avoid
  looking distrustful, sometimes replacing the device-level lock entirely to keep
  sharing frictionless. The source notes that American users had the same worries
  about accidental disclosure and the same pressure not to seem secretive, and
  frames these locally grown solutions as able to inspire designs elsewhere,
  while acknowledging their friction and generally poor execution.

### Aesthetic density, and what does not change

[[2016-11-06_china-website-complexity]] is the corpus's most direct
counterweight to over-adapting on style alone. Chinese participants rejected
overly sparse designs as lacking useful content, so an imported minimalist layout
can fail; but their tolerance for density does not make them, in the source's
words, superhumans who escape the laws of user interface psychology — they still
took longer to find information on complex sites and hit the same problems with
carousels, disappearing navigation, non-standard controls and ad-laden editorial
pages. The recommendation is a simpler design than the prevailing local tradition,
but not oversimplified or minimalist. [[2021-03-21_crosscultural-design]] points
the same way from the user's mouth: ease of use matters more than visual style.

## Sources (9)

- [[2016-11-06_china-website-complexity]] — Design preferences and usability issues differ across cultures; assumptions based on visual inspection without user testing are invalid, and excessive complexity causes usability problems and user frustration while users accustomed to higher information density may reject overly simple designs.
- [[2016-11-27_app-lockers]] — Device sharing practices and privacy needs vary globally; solutions developed in one context can inspire designs elsewhere.
- [[2017-01-22_date-input]] — date formats vary globally; the article stresses clear labeling and format support for international audiences.
- [[2017-09-03_credibility-china]] — effective localization for China requires understanding region-specific conventions beyond translation, including pricing presentation and search-engine optimization tactics.
- [[2018-09-02_mobile-login-china]] — regional differences in technology adoption, conventions, and user expectations require localized design solutions; mobile login methods demonstrate importance of context.
- [[2021-03-21_crosscultural-design]] — addresses designing products for multiple languages and cultural contexts at scale, providing detailed guidance on localizing visual design, content, interaction patterns, and features, and adapting design decisions based on cultural values, mental models, and preferences for specific target audiences.
- [[2022-03-27_language-switching-ecommerce]] — providing translated and region-adapted versions of sites to serve international customers effectively.
- [[2022-04-24_sizes-measurements-ecommerce]] — Adapting size information and measurement units through designing global sites and size charts that serve customers from diverse markets and regional audiences with different measurement systems.
- [[2022-12-11_time-zone-selectors]] — Time-zone selectors are inherently localization features; design decisions must account for regional differences in familiarity with GMT versus UTC and user geographic distribution.
