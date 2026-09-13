---
type: source
name: "It's Time We Addressed Time-Zone Selectors"
created: 2026-07-30
published: 2022-12-11
source_type: article
status: processed
url: https://www.nngroup.com/articles/time-zone-selectors/
author: Kelley Gordon, Maria Rosala
raw: raw/sources/2022-12-11_time-zone-selectors.md
concepts:
  - "Form Design"
  - "Dropdown Menus"
  - "Localization"
  - "Search Interfaces"
  - "User Research"
---

# It's Time We Addressed Time-Zone Selectors

## Summary

Time-zone selectors are UI components that allow users to set or change local time, commonly found in scheduling features, user settings, and virtual event websites. Designing effective time-zone selectors is challenging due to dynamic offsets (daylight savings), large lists, varied user mental models, and different organizational approaches. This article presents findings from 2 rounds of moderated usability tests with 13 participants and 1 unmoderated study with 83 participants across 4 countries (US, Australia, UK, Germany), offering evidence-based recommendations for designing time-zone selectors.

## Key Takeaways

- **Most users know their time zone but not their offset** — 73% of participants correctly identified their time zone (e.g., Pacific Time), while only 34% knew their UTC offset; GMT was marginally more familiar than UTC but only significantly benefited UK-based users.
- **Avoid organizing by offset** — Participants expected alphabetical ordering; when time zones were organized by offset, users struggled to understand the ordering and often assumed it was broken, expecting to find zones under alphabetical letters.
- **Search is essential** — Nearly all participants attempted to search when the search field was deactivated; providing a visible, easily discoverable search field is critical for user success with long time-zone lists.
- **City is the most common search strategy** — 44% of participants' first search attempts used a city name, followed by time zones (24%); however, not all cities appear in lists, requiring users to broaden their search to country or state.
- **Grouping by continent aids offset-based lists** — When time zones are ordered by offset, grouping by continent reduced relative completion time significantly; however, continents should be ordered to prioritize the user's primary audience.
- **Pre-select or highlight the user's time zone** — Many participants wished their location was automatically detected or highlighted; displaying the user's time zone at the top or auto-scrolling to it reduces cognitive load.

## Quotes

> This is something that I hate doing in [sic] most websites.

> I hate time zones. I hate having to select the time zone. I don't know why they always go wrong, especially when it comes to scheduling for me.

> I would have thought it would have been in alphabetical order as opposed to it didn't seem to be in any order.

## Concepts

- [[Form Design]] — Time-zone selectors are form controls requiring careful design choices about organization, search, and presentation to support user mental models.
- [[Dropdown Menus]] — Dropdown lists for time zones can quickly become unwieldy; design considerations include search, grouping, ordering, and pre-selection to reduce user effort.
- [[Localization]] — Time-zone selectors are inherently localization features; design decisions must account for regional differences in familiarity with GMT versus UTC and user geographic distribution.
- [[Search Interfaces]] — Search is a critical affordance for time-zone selection; visible, discoverable search fields with typeahead suggestions significantly improve user success rates.
- [[User Research]] — Quantitative and qualitative testing across multiple countries revealed that designers' assumptions about optimal time-zone organization often conflict with actual user expectations and mental models.
