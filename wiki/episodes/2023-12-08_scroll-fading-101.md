---
type: source
name: "Scroll Fading 101"
created: 2026-07-30
published: 2023-12-08
source_type: article
status: processed
url: https://www.nngroup.com/articles/scroll-fading-101/
author: Sara Paul
raw: raw/sources/2023-12-08_scroll-fading-101.md
concepts:
  - "Animation"
  - "Design Patterns"
  - "Interaction Design"
  - "Performance Optimization"
  - "Visual Hierarchy"
---

# Scroll Fading 101

## Summary

Scroll fading is an animation triggered by scrolling where elements fade in or out as users scroll down the page. While animation is processed preattentively and draws eye attention automatically, scroll fading can create usability problems including illusion of completeness reducing content discoverability, users skipping slowly-fading text, and images failing to load. Best practices include fast fade-in rates (100-400ms), element persistence, fading one element type at a time, and avoiding scroll fading on mobile. Scroll fading works best when combined with effective writing and adequate data loading to provide supplementary visual information at the right moment.

## Key Takeaways

- **Scroll fading triggers animations when users reach specific scroll positions** — designers use it to guide users through long pages, lazy load data, display timely supporting information, or boost brand credibility.
- **Element persistence is critical** — animations that occur only once as users first reach a position work better than repeated animations that frustrate task-oriented users.
- **Scroll fading can trigger illusion of completeness** — when information below the fold slowly fades in on pages that already appear complete (due to whitespace), users may assume nothing else exists.
- **Text comprehension depends on fast fade-in rates and effective writing** — text fading in slower than 500ms risks users scrolling past before comprehending; concise, punchy text works better than lengthy passages.
- **Avoid scroll fading on mobile** — smaller screens increase scroll fatigue and worsen illusion of completeness; usability issues observed on desktop are exacerbated on mobile.

## Quotes

> Scroll fade is a new design pattern. It refers to an animation that is triggered by scrolling: new elements or content fade in or out once the user scrolls down to a certain point on the page.

> Movement (and thus animation) is processed preattentively: the eyes are automatically drawn to it. As a result, incorrectly deployed animations can be highly distracting.

> Users are likely to skip over text if it fades in too slowly. As a result, they may not comprehend what the website offers and whether it addresses their needs. However, too fast fade-in rates can also cause them to not notice the animation.

## Concepts

- [[Animation]] — scroll fading is a specific animation pattern triggered by user scrolling; understanding animation principles (duration, preattentive processing) is essential.
- [[Design Patterns]] — scroll fading is a distinct design pattern that differs from scrolljacking and should be applied selectively with clear design purposes.
- [[Interaction Design]] — scroll fading affects how users interact with page content; proper implementation considers user scanning patterns and content discovery.
- [[Performance Optimization]] — scroll fading often supports lazy loading of images and data; optimizing data loading is critical to avoid broken user experience.
- [[Visual Hierarchy]] — scroll fading can establish visual hierarchy by fading in important information; however, it can also contribute to illusion of completeness if misused.
