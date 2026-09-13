---
type: concept
name: Postel's Law
created: 2026-09-10
updated: 2026-09-10
status: stub
aliases:
  - "Design Resiliency"
  - "Robustness Principle"
  - "User Input Flexibility"
---

# Postel's Law

## Definition

Postel's Law, also known as the robustness principle, states: "Be conservative
in what you do, be liberal in what you accept from others." It was formulated
in 1981 by the computer scientist Jon Postel for TCP network protocols, and
transfers directly to user experience design: a system should produce reliable,
accessible output while accepting input in whatever form it arrives
([[2024-01-23_laws-of-ux_07-5-postels-law]]).

Applied to interfaces, the principle is a human-centric one. People are
sometimes inconsistent, frequently distracted, occasionally error-prone and
usually driven by emotion, so a design that liberally accepts variable human
input and translates it into structured, machine-friendly output moves the
burden of conformity away from the user
([[2024-01-23_laws-of-ux_07-5-postels-law]]). The same posture extends to
context: the design should be resilient to differences in device, language,
capability and user settings.

## Practice

### Accept input in the forms people actually give it

- Minimize the number of required form fields, which reduces decision fatigue
  ([[2024-01-23_laws-of-ux_07-5-postels-law]]).
- Support variable name orderings across cultures, flexible address formats,
  hyphenated names and single-letter names, rather than rejecting what does not
  match one assumed pattern
  ([[2024-01-23_laws-of-ux_07-5-postels-law]]).
- Write error messages that are empathetic rather than dismissive
  ([[2024-01-23_laws-of-ux_07-5-postels-law]]).

### Adapt to the device and its capabilities

- [[Responsive Design]], Ethan Marcotte's 2010 approach, uses fluid grids,
  flexible images and media queries to adapt content to any screen size, from
  smartwatches to televisions; it is now the de facto web standard
  ([[2024-01-23_laws-of-ux_07-5-postels-law]]).
- [[Progressive Enhancement]] layers styling and interaction on top of core
  content: everyone gets the basic functionality, such as a search box, and
  devices that support voice recognition get an added microphone layer without
  the core search being obscured
  ([[2024-01-23_laws-of-ux_07-5-postels-law]]).

### Plan for language and typography variation

- English text can expand by up to 300% when translated, so layouts must
  tolerate text expansion, right-to-left orientation and vertical text layouts
  ([[2024-01-23_laws-of-ux_07-5-postels-law]]).
- Users change their default font size for accessibility reasons, and a design
  should adapt gracefully by reorganizing the layout and prioritizing content
  visibility. Amazon removes lower-importance navigation links as font size
  increases ([[2024-01-23_laws-of-ux_07-5-postels-law]]).

## Sources (1)

- [[2024-01-23_laws-of-ux_07-5-postels-law]] — guiding principle for human-centric design: conservative in output (reliable, accessible), liberal in input (flexible, forgiving, adaptable); systems should be resilient enough to accept nonconformant input as long as meaning is clear; foundation of fault-tolerant design; accepting variable forms of human input (keyboard, touch, voice, assistive technology) and translating them into machine-readable formats; anticipating and planning for variations (language, text expansion, font size, device features) to ensure robust designs that adapt gracefully to user and context changes.
