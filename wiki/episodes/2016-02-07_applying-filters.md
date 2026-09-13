---
type: source
name: "User Intent Affects Filter Design"
created: 2026-07-30
published: 2016-02-07
source_type: article
status: processed
url: https://www.nngroup.com/articles/applying-filters/
author: Katie Sherwin
raw: raw/sources/2016-02-07_applying-filters.md
concepts:
  - "Faceted Navigation"
  - "E-Commerce"
  - "User Intent"
---

# User Intent Affects Filter Design

## Summary

Filter and facet design requires understanding whether users are in exploratory or goal-directed search modes. Exploratory users benefit from interactive filters that update results after each selection, allowing them to discover available options. Goal-directed users benefit from batch filters that let them specify all criteria before results refresh. Site speed and user behavior detection also influence implementation. The key design principle is not fragmenting the user experience and maintaining UI stability as users progress toward their goals.

## Key Takeaways

- **User intent drives implementation choice** — exploratory users (learning about the search space) benefit from interactive filters; goal-directed users (with multiple criteria in mind) benefit from batch filters with an Apply button.
- **Detect activity to infer intent** — systems can watch for mouse hover, keyboard focus, or inactivity timeouts to determine if users are still making selections or are ready to see results.
- **Site speed is a secondary factor** — if results load in under one second, interactive filtering is acceptable even for goal-directed users; slower sites should default to batch filtering.
- **Avoid visual distraction during updates** — dim the results area and show a progress indicator when filtering to prevent users from being distracted by flickering content changes.
- **Handle scrolling carefully** — when results update, avoid jumping to the top of the page if users are still interacting with filters; this can cause disorientation and accidental clicks.
- **Continuous feedback prevents zero-result surprises** — interactive filtering with facet counts helps users avoid dead-end filter combinations.

## Quotes

> The overarching theme in selecting an implementation should be to not fragment the user experience, and let users smoothly progress towards their goals while maintaining a sense of UI stability and user mastery.

> For users who intend to select more than one facet, it's disruptive and tiresome to refresh the page every single time they make a selection, especially if the site is slow.

> Intelligent filtering mechanisms recognize when users are still thinking and do not refresh the page until the user is done making selections.

## Concepts

- [[Faceted Navigation]] — the article discusses batch vs. interactive filter implementations and facet-driven exploration.
- [[E-Commerce]] — filter design is central to product discovery and conversion on ecommerce sites.
- [[User Intent]] — detecting whether users are exploratory or goal-directed is key to choosing the right filter strategy.
