---
type: source
name: "Breakpoints in Responsive Design"
created: 2026-07-30
published: 2024-04-05
source_type: article
status: processed
url: https://www.nngroup.com/articles/breakpoints-in-responsive-design/
author: Kelley Gordon
raw: raw/sources/2024-04-05_breakpoints-in-responsive-design.md
concepts:
  - "Responsive Design"
  - "Web Layout"
  - "Breakpoints"
  - "Mobile Design"
  - "Grid Systems"
---

# Breakpoints in Responsive Design

## Summary

Breakpoints are foundational to responsive design, defining specific screen sizes where layouts must adjust to fit device characteristics and screen dimensions. The article explains the concept, rationale, and implementation of breakpoints using a T-shirt sizing convention (extra-small, small, medium, large) corresponding to different device types and screen ranges. Practical guidance addresses common layout changes (navigation collapsing, column reflowing, visible content adjustment) and emphasizes defining breakpoints based on the actual device-usage distribution of a site's audience rather than arbitrary standards.

## Key Takeaways

- **Definition and function** — a breakpoint is a specific screen size where design adjusts to a different layout; in practice, designers work with screen-size ranges (minimum and maximum width) for which a specific layout applies.
- **Common breakpoints** — typical designs accommodate four basic breakpoints: extra-small (mobile, up to 500px), small (tablet, 500-1200px), medium (laptop, 1200-1400px), and large (monitors, 1400px+).
- **Layout changes** — common adjustments at breakpoints include different navigation (hamburger menus at smaller sizes), collapsing columns, and changing numbers of visible content elements.
- **Design considerations** — designers must think through how content flows at different sizes, decide what information is crucial at each breakpoint, and communicate layout changes to developers through specifications and testing.
- **Naming conventions** — using clear, sensible naming (like T-shirt sizing) allows teams to adjust specific breakpoint values as audience device usage evolves.

## Quotes

> A breakpoint defines a screen size where the design should adjust to a different layout.

> Involve your development team in defining your breakpoints, because that team will set up the website's breakpoints.

> Creating an exception from regular column stacking to make the call to action more discoverable (for example by making some preceding content collapsible under accordions) may be needed.

## Concepts

- [[Responsive Design]] — demonstrates how breakpoints are fundamental to creating adaptive layouts for varying device sizes.
- [[Web Layout]] — addresses how breakpoints enable strategic layout reorganization to maintain usability across screen sizes.
- [[Breakpoints]] — defines the concept and practical implementation of screen-size-specific layout adjustments.
- [[Mobile Design]] — explores how smallest breakpoints require special consideration for space-constrained mobile interfaces.
- [[Grid Systems]] — shows how grid column counts (4-column, 8-column, 12-column) vary across breakpoints to organize layout structure.
