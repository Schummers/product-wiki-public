---
type: concept
name: Hick's Law
created: 2026-09-10
updated: 2026-09-10
status: stub
aliases:
  - "Paradox of Choice"
---

# Hick's Law

## Definition

Hick's Law states that the time it takes to make a decision increases with the
number and complexity of the choices available. Formulated in 1952 by the
psychologists William Edmund Hick and Ray Hyman, it is expressed as
RT = a + b log₂(n), where n is the number of stimuli and a and b are
task-dependent constants: decision time grows logarithmically with the number
of options, not linearly
([[2024-01-23_laws-of-ux_06-4-hicks-law]]). Applied to interfaces, an
abundance of options lengthens decisions and raises [[Cognitive Load]].

The law is closely tied to the paradox of choice: Sheena Iyengar and Mark
Lepper's jam study (2000) found shoppers were ten times more likely to buy when
shown 6 varieties rather than 24, so more choice leads to choice overload
rather than to greater satisfaction
([[2024-01-23_laws-of-ux_06-4-hicks-law]]). In *Laws of UX*, Hick's Law is also
used as the worked example of how a psychological law sits underneath a team's
[[Design Principles]]: it is the observation behind the principle "clarity over
abundance of choice"
([[2024-01-23_laws-of-ux_13-11-applying-psychological-principles-in-design]]).

## Practice

### Reduce the choices presented at any one moment

- Minimize the number of choices offered at critical moments, so that decision
  time and mental effort stay low
  ([[2024-01-23_laws-of-ux_06-4-hicks-law]]).
- Use [[Progressive Disclosure]]: reveal choices at the right time rather than
  all at once. Google Search keeps the initial interface focused on the search
  box and surfaces filters (images, videos, news) only once results appear
  ([[2024-01-23_laws-of-ux_06-4-hicks-law]]).
- Decompose complex processes into smaller steps. Notion's onboarding uses a
  progressive checklist to teach new users instead of exposing every feature at
  once ([[2024-01-23_laws-of-ux_06-4-hicks-law]]).

### Give some options more weight than others

- Highlighting recommended options reduces the burden of choosing. Netflix
  answered an 18-minute decision paralysis with "Trending Now" and "Popular on
  Netflix", which give specific options weight through social proof
  ([[2024-01-23_laws-of-ux_06-4-hicks-law]]).

### Do not simplify past the point of clarity

- Removing unnecessary complexity improves usability, but simplifying to the
  point of abstraction makes it unclear what actions are available, what the
  next step is, or where to find information. Icon-only navigation confuses
  users; pairing icons with text labels restores clarity and aids recognition
  ([[2024-01-23_laws-of-ux_06-4-hicks-law]]).

### Turn the law into rules a team can apply

- In the principle-to-law-to-rule framework, a design principle is anchored to
  the psychological law that justifies it and then translated into specific
  rules. "Clarity over abundance of choice" is connected to Hick's Law and
  produces rules such as limiting choices to three items and keeping
  explanations under 80 characters
  ([[2024-01-23_laws-of-ux_13-11-applying-psychological-principles-in-design]]).

## Sources (2)

- [[2024-01-23_laws-of-ux_06-4-hicks-law]] — principle that decision time increases logarithmically with the number of choices; fundamental to interface complexity and user decision-making; the psychological phenomenon where abundance of options reduces satisfaction and increases decision paralysis rather than improving outcomes.
- [[2024-01-23_laws-of-ux_13-11-applying-psychological-principles-in-design]] — demonstrated as an example law connected to the design principle "clarity over abundance of choice," showing how psychology principles guide specific rules like limiting choices.
