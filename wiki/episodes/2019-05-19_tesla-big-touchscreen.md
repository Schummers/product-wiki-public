---
type: source
name: "Tesla's Touchscreen UI: A Case Study of Car-Dashboard User Interface"
created: 2026-07-30
published: 2019-05-19
source_type: article
status: processed
url: https://www.nngroup.com/articles/tesla-big-touchscreen/
author: Raluca Budiu
raw: raw/sources/2019-05-19_tesla-big-touchscreen.md
concepts:
  - "Interaction Design"
  - "Usability Heuristics"
  - "Safety-Critical Design"
  - "Cognitive Load"
  - "Mobile Design"
---

# Tesla's Touchscreen UI: A Case Study of Car-Dashboard User Interface

## Summary

Tesla's Model S uses a 17-inch touchscreen for most secondary controls (climate, media, rear-view camera), replacing dedicated physical buttons. While the large screen allows multiple applications to be visible simultaneously, the design creates significant usability problems: soft buttons require visual attention unlike physical buttons with haptic feedback, controls are positioned far from the driver's hands, target sizes are too small, targets are crowded together causing accidental touches, and the always-present map background creates visual interference. The article identifies both problems and positive design decisions, highlighting the tension between new convenience features and safe driving.

## Key Takeaways

- **Soft buttons demand attention but lack haptic feedback** — Unlike physical buttons learned through muscle memory, touchscreen buttons require the driver to look and confirm position before tapping; time spent looking at the UI is time not watching the road.

- **Target placement causes longer acquisition times** — Fitts's Law applies to dashboards; controls placed at the bottom of the screen are far from the steering wheel position and require significant eye movement, increasing distraction time.

- **Smaller targets in Version 9 worsen accuracy** — Reducing target size to fit more options decreased acquisition speed and increased accidental touches; making targets smaller violates fundamental usability principles for interfaces in safety-critical contexts.

- **Crowding causes accidental interaction** — Closely spaced targets increase slip errors; the user accidentally triggered the seat warmer when trying to adjust temperature due to insufficient spacing.

- **Map background creates visual interference** — The always-present navigation map behind other apps makes status text hard to read, blocks important screen area, and interferes with app window management.

- **Multiple information sources create ambiguity** — For lane changes, drivers have mirror view, rear-view camera, and lane-assist display; users may misinterpret lane-assist information if not aware which lanes it refers to, creating safety risks.

## Quotes

> "For those of us who learned how to drive a few decades ago, driving a modern car is a completely different experience."

> "the most basic fact about human attention: it's limited. And if they design these sophisticated car features so that they don't take away cognitive resources from the basic task, which is driving."

> "no haptic feedback. In order to reliably touch these buttons, people must look at them."

## Concepts

- [[Interaction Design]] — Car dashboards require special consideration of distraction cost and safety implications; touchscreen design must minimize attention demands.

- [[Usability Heuristics]] — Nielsen's heuristics apply to cars; Tesla's design violates visibility of system status, control and freedom (users can't change defaults), and consistency (window close methods vary).

- [[Safety-Critical Design]] — In safety contexts, reducing mode errors and interaction cost is more important than fitting more features on screen; physical buttons for critical functions are preferable.

- [[Cognitive Load]] — Touchscreen interfaces in cars increase cognitive load by requiring visual confirmation and attention; soft buttons should only control non-critical features.

- [[Mobile Design]] — Touchscreens work well for multiple simultaneous windows (a benefit), but target sizing, spacing, and feedback are problematic for safety-critical driving tasks.
