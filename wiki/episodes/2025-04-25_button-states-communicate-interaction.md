---
type: source
name: "Button States: Communicate Interaction"
created: 2026-07-30
published: 2025-04-25
source_type: article
status: processed
url: https://www.nngroup.com/articles/button-states-communicate-interaction/
author: Kelley Gordon
raw: raw/sources/2025-04-25_button-states-communicate-interaction.md
concepts:
  - "Design Patterns"
  - "Interaction Design"
  - "Feedback Design"
  - "Accessibility"
  - "Button Design"
  - "UI Elements"
---

# Button States: Communicate Interaction

## Summary

Buttons are core interface elements that execute actions when clicked or tapped. Clear signaling of button states is critical for good design and user understanding. The article defines five core states (enabled, disabled, hover, focus, pressed) plus additional states (loading, selected), explaining what each communicates and typical visual characteristics. It distinguishes button states (which change based on user interaction or system status) from button styles (visual hierarchy classification: primary, secondary, tertiary), emphasizing that effective button design requires both clear state signals and descriptive labels.

## Key Takeaways

- **Five core button states communicate interaction availability** — enabled (ready to be clicked), disabled (unavailable, appears desaturated), hover (mouse over, indicates clickability), focus (keyboard focus, indicated by outline), pressed (action registered, brief feedback); each must be visually distinct and clearly communicated.
- **Button states serve specific UX functions** — disabled prevents invalid actions; hover and focus indicate interaction possibility; pressed provides immediate feedback that action was registered; all states help users understand when and how to interact.
- **Loading and selected states extend core state vocabulary** — loading indicates longer-duration actions with spinners or indicators; selected applies to checkboxes and radio buttons rather than buttons, though often confused with pressed state.
- **Timing matters for state feedback** — hover state should have 150-200ms delay to prevent accidental triggers; focus state should appear within 100-150ms of tab press so users don't miss it; pressed state must appear within 100-150ms or users will click multiple times.
- **Button style versus state is critical distinction** — style (primary, secondary, tertiary) provides visual hierarchy and emphasis independent of state; one button has one style but changes states; states communicate interaction status; styles communicate importance level.

## Quotes

> Buttons are core user-interface elements that, when clicked or tapped, execute an action. When designed correctly, buttons set accurate user expectations and help them understand how to interact with the interface.

> The focus state should appear pretty quickly (around 100-150ms) after the user uses the keyboard. Otherwise, the user may end up tabbing on the keyboard again and may miss the desired button.

> Button styles help provide the intended visual emphasis to actions, while button states inform users of the interaction status of the button.

## Concepts

- [[Design Patterns]] — documents button state patterns as standardized solutions for communicating interaction availability and feedback.
- [[Interaction Design]] — focuses on how state changes communicate interaction possibilities and feedback to users through visual design.
- [[Feedback Design]] — emphasizes the importance of immediate, clear state signals for communicating to users that their actions were registered.
- [[Accessibility]] — highlights focus state, ARIA attributes, and contrast standards as essential for keyboard navigation and screen reader compatibility.
- [[Button Design]] — systematizes button design through states, styles, labels, and visual characteristics to create usable, understandable interface controls.
- [[UI Elements]] — covers button as a core UI element and how state design influences the broader user experience of interface interactions.
