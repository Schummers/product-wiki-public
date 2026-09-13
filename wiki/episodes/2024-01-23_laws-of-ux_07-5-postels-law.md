---
type: source
name: "Laws of UX: 5. Postel's Law"
created: 2026-09-10
published: 2024-01-23
source_type: book
status: processed
url: "https://www.oreilly.com/library/view/laws-of-ux/9781098146962/"
author: Jon Yablonski
raw: raw/sources/2024-01-23_laws-of-ux_07-5-postels-law.md
book: "Laws of UX"
chapter: "5. Postel's Law"
concepts:
  - "Postel's Law"
  - "Progressive Enhancement"
  - "Responsive Design"
---

# Laws of UX: 5. Postel's Law

## Summary

Postel's Law, the robustness principle, states: "Be conservative in what you do, be liberal in what you accept from others." Originally formulated by computer scientist Jon Postel for TCP network protocols in 1981, the principle applies directly to user experience design. It advocates for systems that accept variable, flexible user input while providing reliable, accessible output. The chapter demonstrates how this principle enables designers to create human-centric experiences that account for diverse devices, capabilities, languages, and input methods.

## Key Takeaways

- **Conservative Output, Liberal Input** — Design systems should output reliable, accessible interfaces while accepting input in multiple formats, languages, dialects, and from various devices (smartwatches to televisions).

- **Form Field Flexibility** — Minimize required fields to reduce decision fatigue. Support variable name orderings across cultures, flexible address formats, hyphenated names, and single-letter names. Error messages should be empathetic rather than dismissive.

- **Responsive Design** — Ethan Marcotte's 2010 approach uses fluid grids, flexible images, and media queries to adapt content to any screen size, from smartwatches to TVs. Now the de facto web standard.

- **Progressive Enhancement** — Layer styling and interaction on top of core content. Everyone gets basic functionality (e.g., a search box); devices supporting voice recognition get an enhanced microphone icon layer without obscuring core search functionality.

- **Internationalization Resiliency** — English is a very compact language, and its words can expand up to 300% when translated into a less compact language such as Italian. Design must account for text expansion, right-to-left orientation, and vertical text layouts.

- **User Font Size Customization** — Users customize default font sizes for accessibility. Designs must gracefully adapt by reorganizing layouts and prioritizing content visibility, as Amazon does by removing lower-importance navigation links when font size increases.

## Quotes

> Be conservative in what you do, be liberal in what you accept from others.

> Designing good user experiences means designing good human experiences. People don't behave like machines: we are sometimes inconsistent, frequently distracted, occasionally error-prone, and usually driven by emotion.

> By designing systems that liberally accept variable human input and translate it into a structured, machine-friendly output, we transfer this burden away from users and therefore ensure a more human user experience.

## Concepts

- [[Postel's Law]] — guiding principle for human-centric design: conservative in output (reliable, accessible), liberal in input (flexible, forgiving, adaptable); systems should be resilient enough to accept nonconformant input as long as meaning is clear; foundation of fault-tolerant design; accepting variable forms of human input (keyboard, touch, voice, assistive technology) and translating them into machine-readable formats; anticipating and planning for variations (language, text expansion, font size, device features) to ensure robust designs that adapt gracefully to user and context changes.
- [[Progressive Enhancement]] — layering strategy that ensures core content and functionality work for all users, with styling and interaction enhancements added for supported browsers and devices.
- [[Responsive Design]] — design approach using fluid grids, flexible images, and media queries to adapt content across any screen size and context.
