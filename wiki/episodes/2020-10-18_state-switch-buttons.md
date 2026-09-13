---
type: source
name: "State-Switch Controls: The Infamous Case of the \"Mute\" Button"
created: 2026-07-30
published: 2020-10-18
source_type: article
status: processed
url: https://www.nngroup.com/articles/state-switch-buttons/
author: Raluca Budiu
raw: raw/sources/2020-10-18_state-switch-buttons.md
concepts:
  - State Switching
  - Button Design
  - Affordance
---

# State-Switch Controls: The Infamous Case of the "Mute" Button

## Summary

This article examines the usability challenges of state-switch controls that toggle between two states, using the microphone mute button as a case study. State-switch buttons must communicate two pieces of information: the current system state and what will happen if the user presses the button. The article identifies problems when these controls fail to clearly communicate both pieces of information and recommends design solutions.

## Key Takeaways

- **Two pieces of information required** — State-switch buttons must communicate both the current state (muted/unmuted) and the next state that will occur when pressed (what the button will do).
- **Two control approach** — The safest design uses separate UI elements: one indicator showing current state and one button showing what will happen, as seen in the Tesla app unlock example.
- **Single control label strategies** — If combining information into one control, the label should indicate what will happen next, and icons should change based on next state, or active state should be clearly indicated through visual signifiers like shadows.
- **Avoid relying on color alone** — Using color as the only signifier for active state is problematic because color has multiple meanings in interfaces and users may not remember color associations.
- **Context matters** — Some interfaces can use single controls if external cues (sound, visual feedback) help users determine current state, but quick state determination under time pressure requires explicit indicators.

## Quotes

> In my panic, I was completely oblivious at the change in the icon color! Eventually, I discovered that, even though the microphone was crossed in both states, the red color of the icon was meant to signal that the button was active and I was muted.

> The *Mute* button is used to switch between two system states (*Muted* and *Unmuted*), but the problem is that users cannot easily tell what the current state is and what they are switching to.

> Understanding this design clearly depends on the shadow being recognizable as a signifier for active state.

## Concepts

- [[State Switching]] — controls that toggle between two system states, requiring clear communication of both current state and next state to prevent user confusion.
- [[Button Design]] — visual and textual design decisions for buttons that must convey both their current state and their action, with special considerations for state-switch buttons.
- [[Affordance]] — making the current state and available actions visually obvious through consistent design patterns and clear signifiers so users understand what they can do and what will happen.
