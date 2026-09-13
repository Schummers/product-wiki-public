---
type: source
name: "Infinite Scrolling: When to Use It, When to Avoid It"
created: 2026-07-30
published: 2022-09-04
source_type: article
status: processed
url: https://www.nngroup.com/articles/infinite-scrolling-tips/
author: Tim Neusesser
raw: raw/sources/2022-09-04_infinite-scrolling-tips.md
concepts:
  - "Infinite Scrolling"
  - "Pagination"
  - "Content Discovery"
  - "Mobile Design"
  - "Search and Navigation"
---

# Infinite Scrolling: When to Use It, When to Avoid It

## Summary

Infinite scrolling continuously loads content as users scroll, eliminating pagination but creating distinct usability tradeoffs. It reduces interruptions and interaction cost for users browsing homogeneous streams (social media, news, entertainment) but causes problems for users searching for specific items or comparing options. Key issues include difficulty refinding content without page landmarks, illusion of completeness when content loads slowly below the fold, inability to reach footers, accessibility barriers for keyboard and screen-reader users, increased page load times, and poor SEO performance. Variants like Load More buttons and integrated pagination address some issues. Designers must consider whether their users are in a browse mindset (infinite scroll works well) or search mindset (pagination or Load More is better), along with factors like device types, bandwidth limitations, and accessibility needs.

## Key Takeaways

- **Browse mindset requires uninterrupted flow** — Infinite scrolling works best for entertainment, news, and social media where users scroll through homogeneous items with no specific goal; interruptions for pagination can shift tasks and reduce engagement.
- **Search mindset needs landmarks** — When users search for specific items or compare options, pagination provides page landmarks that help refinding; infinite scrolling makes it nearly impossible to remember item locations and return to them.
- **Illusion of completeness** — Without indication that content is loading, users assume the end has been reached and stop scrolling; slow-loading enriched results contribute to this problem.
- **Footer inaccessibility is real** — Infinite scrolling (without Load More button) can make it impossible to access footer information like contact details, policies, or legal text; this blocks important user needs.
- **Accessibility creates barriers** — Keyboard-only users must tab through vast content to reach the end, and screen-reader users only see the initial chunk without ability to load more; ARIA feed role helps but doesn't solve all issues.
- **Load More button is a compromise** — This variant reduces interaction cost for mobile users with limited data, enables footer access, eliminates illusion of completeness, but still requires clicking and maintains some interaction cost.

## Quotes

> There is no solution (infinite scroll, pagination, Load More , or integrated pagination) that is overall superior and the perfect fit for every website.

> Infinite scrolling is also not a good fit if you have a large user group from areas with low bandwidth or if your website is visited frequently by users with accessibility needs.

> Infinite scrolling typically works best for situations where users will want to scroll through homogeneous items with no particular task or goal in mind— for example, entertainment, news, or social media.

## Concepts

- [[Infinite Scrolling]] — A listing-page pattern that continuously loads content as users scroll, creating seamless browsing but causing refinding and footer-access problems.
- [[Pagination]] — Traditional pagination breaks content into numbered pages, providing clear landmarks and footer access but interrupting browsing and requiring clicks.
- [[Content Discovery]] — Different listing patterns serve different discovery modes; pagination suits specific-item search while infinite scrolling suits open-ended browsing and exploration.
- [[Mobile Design]] — Infinite scrolling rose in popularity with mobile devices due to scroll-friendly touchscreens; Load More buttons help address data-usage concerns for mobile users.
- [[Search and Navigation]] — Infinite scrolling damages search usability by eliminating landmarks; users searching for specific items or comparing options need pagination or Load More to succeed.
