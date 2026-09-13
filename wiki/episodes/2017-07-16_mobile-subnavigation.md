---
type: source
name: "Mobile Subnavigation"
created: 2026-07-30
published: 2017-07-16
source_type: article
status: processed
url: https://www.nngroup.com/articles/mobile-subnavigation/
author: Raluca Budiu
raw: raw/sources/2017-07-16_mobile-subnavigation.md
concepts:
  - "Navigation Design"
  - "Information Architecture"
  - "Menu Design"
---

# Mobile Subnavigation

## Summary

Complex information architectures with many category levels present challenges when translated to mobile. Desktop sites often use mega menus showing 30+ subcategories clearly; mobile screens cannot display them easily. Subnavigation refers to UI helping users access lower-level categories. The article defines four common mobile subnavigation patterns: accordions within main menus, sequential menus, section menus, and category landing pages. Each has different interaction costs, typical-path support, and discoverability characteristics. A simple decision algorithm helps select the pattern based on subcategory count: under 6 use accordions, 6-15 use section menus, over 15 use category landing pages.

## Key Takeaways

- **Define subnavigation design goals** — Minimize interaction cost (few taps, no page loads), support typical paths through the site, and ensure discoverability of the navigation UI itself.

- **Sequential menus disorient users** — Sequential menus show only current-level subcategories; selecting a category replaces the view. While space-efficient, users with low spatial ability become confused about their location and often accidentally tap the phone's Back button instead of the menu's Back link.

- **Accordions inside main menus work for few subcategories** — When primary categories have fewer than 6 subcategories, accordions embedded in the main navigation menu provide low interaction cost and support all navigation paths without page loads.

- **Section menus specialize support** — Section menus appear on category landing pages and work best when users spend most of their session in a single site section. They don't support efficient jumping between different sections.

- **Category landing pages cost more interaction** — Category landing pages force users to load a page and navigate through it each time they switch branches. Reserve this pattern for over 15 subcategories when no other option fits.

## Quotes

> The small screen size cannot easily accommodate many subcategories. While Cisco's desktop site can display 30 or more subcategories in its mega menus fairly comfortably, without forcing users to scroll, those categories will not easily fit on a single mobile screen.

> Sequential menus cause users to accidentally make mistakes, especially on Android phones (or in a browser) — often people are tempted to use the phone's physical Back button or the browser's Back button, and accidentally end up closing the menu and navigating to a different page instead of moving back to the higher-level menu.

> Definition: Subnavigation refers to the navigation UI that helps users access lower-level categories in the site's information architecture (IA).

## Concepts

- [[Navigation Design]] — patterns for displaying hierarchical navigation on small screens, with decision criteria based on number of subcategories.
- [[Information Architecture]] — how site structure is reflected in navigation patterns, and how mobile constraints require different presentation strategies than desktop.
- [[Menu Design]] — implementation patterns for subnavigation including accordions, sequential menus, section menus, and landing pages, with interaction cost analysis.
