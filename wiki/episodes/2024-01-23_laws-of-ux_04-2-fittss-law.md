---
type: source
name: "Laws of UX: 2. Fitts's Law"
created: 2026-09-10
published: 2024-01-23
source_type: book
status: processed
url: "https://www.oreilly.com/library/view/laws-of-ux/9781098146962/"
author: Jon Yablonski
raw: raw/sources/2024-01-23_laws-of-ux_04-2-fittss-law.md
book: "Laws of UX"
chapter: "2. Fitts's Law"
concepts:
  - "Fitts's Law"
  - "Tap Area"
  - "Human Factors Engineering"
---

# Laws of UX: 2. Fitts's Law

## Summary

Fitts's Law establishes that the time to select an interactive target is determined by its distance and size. Originally developed by psychologist Paul Fitts in 1954 to understand human motor control in physical tasks, this principle applies directly to digital interface design. A separate sidebar recounts the World War II aviation crashes caused by pilots under duress confusing identical-looking flap and landing gear controls, and how Fitts and Chapanis's response — shape coding, then a new paradigm they called human factors — laid the foundation for what we now call human-centered design: adapting technology to human limitations rather than forcing humans to adapt to rigid systems.

## Key Takeaways

- **Size and Distance Trade-off** — Time to select a target decreases as the target becomes larger and as the distance to it decreases. Fitts quantified this with an index of difficulty formula: ID = log₂(2D/W), where D is distance and W is target width.

- **Minimum Touch Target Sizes** — Industry guidelines recommend minimum touch target sizes ranging from 44 × 44 CSS pixels (WCAG) to 60 × 60 points (Apple spatial interfaces), though designers should exceed these minimums when possible to reduce precision requirements.

- **Spacing Prevents Errors** — The MIT Touch Lab found average adult fingertips are 16–20 mm in diameter. Google Material Design recommends at least 8dp of space between targets to prevent accidental activation of adjacent elements.

- **Positioning and Reachability** — Targets should be placed in easily accessible areas. On smartphones, users achieve highest accuracy when touching the center of the screen. Apple's Reachability feature enables one-handed use by moving top-screen items to the lower half via gesture.

- **Infinite Targets Exploit Edges** — Screen edges act as natural walls, making targets along edges (menu bars, app docks) infinitely selectable without precision penalties. This is why macOS places the app bar at the screen edge.

- **Contextual Inquiry Method** — The chapter presents Fitts and Chapanis's approach — noticing the crash data was not random, then interviewing the pilots — as an early form of contextual inquiry, the ethnographic field study that observes and interviews a small sample of users in their natural environments instead of relying on recall alone.

## Quotes

> The time to acquire a target is a function of the distance to and size of the target.

> It's important to keep in mind that these recommendations are minimums. Designers should aim to exceed these target touch sizes whenever possible to decrease the need for precision.

> To design better technology means to design for humans, and to design for humans means to anticipate our emotions, limitations, and preconceptions.

## Concepts

- [[Fitts's Law]] — foundational principle quantifying the relationship between target size, distance, and selection time in user interfaces; strategic placement of controls in areas where users can reach them accurately, optimized for device form factor and use context.
- [[Tap Area]] — practical application of sizing and spacing interactive elements to match human precision and minimize errors; the interactive surface area of an element, expandable through label association and adequate spacing from adjacent targets; minimum distance between targets to prevent accidental selection, informed by human fingertip dimensions.
- [[Human Factors Engineering]] — design discipline founded on adapting technology to human limitations and behavior rather than expecting human adaptation to machines.
