---
type: source
name: "What the Erroneous Hawaiian Missile Alert Can Teach Us About Error Prevention"
created: 2026-07-30
published: 2018-01-16
source_type: article
status: processed
url: https://www.nngroup.com/articles/error-prevention/
author: Kim Flaherty
raw: raw/sources/2018-01-16_error-prevention.md
concepts:
  - "Error Prevention"
  - "System Design"
  - "Confirmation Dialogue"
  - "Mode Error"
---

# What the Erroneous Hawaiian Missile Alert Can Teach Us About Error Prevention

## Summary

This article examines the January 2018 false missile alert sent to Hawaii residents and argues that responsibility lies with poor interface design, not operator error. While headlines blamed the employee for selecting the wrong option and confirming it, the article identifies underlying UI design problems that set up the slip: poorly differentiated options (PACOM vs. DRILL-PACOM are cryptic and similar), problematic presentation (live and test options on the same screen, inviting confusion), inadequate confirmation (confirmation screens that are habitual roadblocks may not be noticed), and lack of undo capability (no way to rescind a sent message). The article presents Nielsen's 10 usability heuristics, specifically emphasizing error prevention and error recovery. Good UX design makes errors unlikely through safeguards, clear labeling, and structural separation of critical functions (e.g., test and live environments should be visually and functionally distinct).

## Key Takeaways

- **Design Enables Errors** — The interface design, not operator negligence, is responsible for slips; when two options are similar and side-by-side, users are set up to select incorrectly.
- **Poorly Differentiated Options** — Cryptic, similar labels (PACOM vs. DRILL-PACOM) require excessive mental effort to differentiate; clearer labels (Test Alert vs. Live Alert) or grouping would prevent confusion.
- **Separation of Live and Test** — Mixing live and test workflows on the same screen creates dangerous proximity; best practice is structural separation with different modes, visual distinctions, and explicit actions required to enter live mode.
- **Confirmation Screens as Roadblocks** — Frequent confirmation dialogs train users to dismiss them habitually without reading; for critical actions, confirmation should be more intrusive (e.g., password re-entry) to force conscious attention.
- **Slips Happen Automatically** — Slips occur when users want one action but unintentionally take another, often on autopilot; they differ from mistakes (conscious but wrong choices) and require design-level prevention rather than user blame.
- **Undo Capability Critical** — Systems should be designed to allow recovery from errors; authorization to take an action should include authorization to undo it; if undoing is not technically possible, recovery workflows should exist.

## Quotes

> "When I heard about this mishap, my immediate question was, "What is wrong with the interface that caused the operator to inadvertently make the incorrect selection?""

> "Slips occur when a user wants to do one action but unintentionally takes another (usually similar) action."

> "a poorly designed system is to blame. A good UI makes it hard for people to err, and easier to recover from any remaining errors."

## Concepts

- [[Error Prevention]] — A design principle emphasizing that systems should make errors unlikely by guiding users when they intend one action but might take another (on autopilot); distinct from mistakes (conscious but wrong choices); achieved through clear labeling, differentiation of options, visual signifiers, and structural safeguards.
- [[System Design]] — The overall architecture and interaction design of a system; affects not only usability but safety; critical systems require defense-in-depth approaches including prevention, confirmation, and recovery.
- [[Confirmation Dialogue]] — A dialog asking users to confirm a critical action; effective when truly intrusive and requiring conscious attention; ineffective when habitual and easily dismissed.
- [[Mode Error]] — An error that occurs when users have different mental models of the system state (believing they are in test mode when actually in live mode); prevented through clear, visible, distinct mode indicators.
