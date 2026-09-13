---
type: source
name: "Challenges for Screen-Reader Users on Mobile"
created: 2026-07-30
published: 2023-04-30
source_type: article
status: processed
url: https://www.nngroup.com/articles/screen-reader-users-on-mobile/
author: Tanner Kohler
raw: raw/sources/2023-04-30_screen-reader-users-on-mobile.md
concepts:
  - "Accessibility"
  - "Mobile Design"
---

# Challenges for Screen-Reader Users on Mobile

## Summary

Screen-reader users on mobile devices face significant challenges due to the mismatch between how technology was designed (assuming visual access) and how assistive technology must present information sequentially through audio. Screen readers present information one element at a time, making it difficult for users to scan content or understand page structure. Proper semantic HTML coding, informative labels frontloaded with keywords, and careful sequencing of page elements are essential for making mobile apps accessible. Third-party accessibility plugins provide limited value compared to fundamental design changes that consider screen-reader usage from the start.

## Key Takeaways

- **Sequential access creates cognitive burden** — Screen readers present all information one piece at a time, requiring users to swipe through every element and remember everything they’ve heard to build a mental model.
- **Scanning requires proper coding** — Screen-reader users scan by jumping between headings and links, but only if those elements are properly coded semantically in HTML; visual styling alone is insufficient.
- **Labels must be frontloaded with keywords** — Screen-reader users swipe quickly and don’t listen to entire labels; keywords must appear at the beginning so users can quickly decide relevance.
- **Focus management matters greatly** — When overlays or menus open, screen-reader focus must jump to the new content; leaving focus in place confuses users who expect to interact with what they just triggered.
- **Accessibility plugins are ineffective** — Third-party accessibility menus are largely ignored by screen-reader users who already have built-in operating system screen readers that are more powerful and familiar.
- **Real users, real testing needed** — Testing with actual screen-reader users reveals design problems that built-in screen readers miss and shows that accessibility is structural, not a plugin solution.

## Quotes

> His response was instructive and set the theme for the entire study:

“That’s a hard statement because I don’t love any app .

> Everything for me with [the screen reader] is very linear.

> Accessibility Menus: Not Considered Helpful

Some websites rely on accessibility menus provided by third-party companies to improve the accessibility of their designs — particularly to meet ADA requirements and WCAG accessibility standards. like they don’t need to actually work on making something accessible.

## Concepts

- [[Accessibility]] — Accessible design requires digital products that enable users with disabilities, including those using screen readers, to perceive, navigate, and interact with content effectively; developers must code with assistive tools like screen readers in mind to support users with visual impairments accessing content through audio.
- [[Mobile Design]] — Creating interfaces for small screens that must account for how users interact when they cannot see, requiring sequential code order and semantic HTML.
