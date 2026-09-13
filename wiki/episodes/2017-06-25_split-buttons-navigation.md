---
type: source
name: "Don't Use Split Buttons for Navigation Menus"
created: 2026-07-30
published: 2017-06-25
source_type: article
status: processed
url: https://www.nngroup.com/articles/split-buttons-navigation/
author: Raluca Budiu
raw: raw/sources/2017-06-25_split-buttons-navigation.md
concepts:
  - "Menu Design"
  - "Navigation Design"
  - "Touch Target"
---

# Don't Use Split Buttons for Navigation Menus

## Summary

Split buttons, common in desktop applications, are poorly suited for mobile navigation. A split button contains two functions within one control: clicking the label performs one action while clicking the arrow displays a dropdown menu. On desktop sites, this pattern allows hovering to reveal submenus while clicking the label navigates to a category page. On mobile, where hover is unavailable, designers attempted to use split buttons for the same functionality. However, users are unfamiliar with split buttons on the web, the two touch targets are too close together, and the unpredictable interface behavior frustrates users. Better alternatives include providing category landing pages through links within the menu, or using a two-tap interaction.

## Key Takeaways

- **Users don't expect split behavior on the web** — The split button pattern is familiar in desktop applications but rare on websites. Users lack mental models for this interaction and won't discover the dual functionality without extensive testing.

- **Touch targets must be farther apart** — The fat-finger problem on touchscreens means users cannot reliably tap between closely positioned targets like a split button's label and arrow; the two functions require separation.

- **Unpredictability damages perceived reliability** — When the same apparent gesture (tapping the label) sometimes navigates and sometimes expands the menu, users perceive the interface as buggy and unreliable, even if the behavior is technically consistent.

- **Provide category links inside the menu** — A better solution allows menus to expand on tap while including a link to the category landing page within the expanded menu (e.g., labeled All Sports or View All).

- **Two-tap interactions have discoverability issues** — Tapping once to expand the menu, then again to navigate to the category page is sometimes used but has weak discoverability; users may not realize they can tap again.

## Quotes

> Users are rarely precise or consistent: sometimes they will tap the arrow and sometimes tap the label, looking for the same result. If the interface does different things after two instances of (seemingly) the same user action, it will seem buggy and erratic.

> While the solution may seem elegant, it doesn't work well on touchscreens.

> When it comes to touch gestures, users are rarely precise or consistent: sometimes they will tap the arrow and sometimes tap the label, looking for the same result. If the interface does different things after two instances of (seemingly) the same user action, it will seem buggy and erratic.

## Concepts

- [[Menu Design]] — guidance on multi-device navigation patterns, showing why split buttons fail on mobile and what patterns work better.
- [[Navigation Design]] — adaptation of desktop mega-menu patterns to touchscreens, addressing hover unavailability and interaction model mismatch.
- [[Touch Target]] — physical constraints of finger-based input, including spacing requirements and discoverability challenges for non-standard interaction patterns.
