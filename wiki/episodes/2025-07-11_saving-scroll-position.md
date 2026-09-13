---
type: source
name: "Designing Scroll Behavior: When to Save a User's Place"
created: 2026-07-30
published: 2025-07-11
source_type: article
status: processed
url: "https://www.nngroup.com/articles/saving-scroll-position/"
author: "Megan Chan"
raw: raw/sources/2025-07-11_saving-scroll-position.md
concepts:
  - Interaction Cost
  - Progressive Disclosure
  - Pogo Sticking
---

# Designing Scroll Behavior: When to Save a User's Place

## Summary

This article examines when and why designers should save a user's scroll position when they navigate back to a previously visited page. Saving scroll position reduces interaction cost and user effort in most scenarios, particularly during the same session when content has not changed. However, there are important exceptions where resetting the scroll position is more appropriate, such as when content updates frequently or after significant time has passed. The article emphasizes considering user intent and choosing the least disruptive default when intent varies.

## Key Takeaways

- **Reduce Interaction Cost** — Saving scroll position minimizes the effort users must expend to return to their previous location on a page, particularly during pogo sticking (navigating back and forth between a list and detail pages).
- **Context Matters for Freshness** — Reset scroll position when content is frequently updated in real-time, as users may miss important new information at their old scroll position or become confused about timing.
- **Session Duration is Key** — Save scroll position only within a session (roughly 30-60 minutes); resetting after extended time helps users reestablish context and reduces confusion about why they landed at a deep position.
- **Least Disruptive Default** — When user intent is unclear, preserve scroll position by default but offer an easy way to jump to the latest content, balancing competing user needs.
- **Visual Feedback Matters** — When resetting scroll position, use a clear visual indicator such as scroll animations to communicate to users that content or their position has changed.

## Quotes

> One of the fastest ways to frustrate a user is by losing their progress.

> It's a small moment, but failing to save scroll position increases the interaction cost of using sites with long pages.

> In such situations, the solution is to choose the least disruptive design. In the case of ChatGPT, this design would preserve the last scroll position and would offer users a persistent chat box or a Jump to Latest Message button that would allow them to quickly navigate to the end of the conversation.

## Concepts

- [[Interaction Cost]] — Saving scroll position directly addresses interaction cost by eliminating repetitive scrolling and scanning needed to return to a user's previous location.
- [[Progressive Disclosure]] — The article mentions showing basic content first and revealing details through interaction, applicable to how scroll position relates to information architecture.
- [[Pogo Sticking]] — This pattern of navigating between a routing page and detail pages is a primary use case where saving scroll position becomes critical for reducing user friction.
