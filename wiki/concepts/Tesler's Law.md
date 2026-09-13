---
type: concept
name: Tesler's Law
created: 2026-09-10
updated: 2026-09-10
status: stub
---

# Tesler's Law

## Definition

Tesler's law, also known as the law of conservation of complexity, states that
for any system there is a certain amount of complexity that cannot be reduced.
It was formulated by Larry Tesler at Xerox PARC and later refined at Apple
([[2024-01-23_laws-of-ux_11-9-teslers-law]]). Every process carries a core of
complexity that cannot be designed away and must therefore be assumed by either
the system or the user. Design does not remove that core; it decides who
carries it.

The record treats the choice as a responsibility rather than a preference:
designers should absorb as much of the complexity as possible in the product
itself. Tesler's own reasoning is the argument for it, that if a million users
each waste a minute a day dealing with complexity an engineer could have
eliminated in a week by making the software a little more complex, the user is
being penalised to make the engineer's job easier.

## Practice

### Move the complexity into the system

[[2024-01-23_laws-of-ux_11-9-teslers-law]] works through four illustrations,
each one a transfer rather than a disappearance:

- **Email.** Modern clients pre-populate the sender and suggest recipients from
  the user's contacts; Gmail's Smart Compose goes further and suggests sentence
  completions. The complexity has not vanished, it has shifted from user to
  system.
- **Checkout.** Ecommerce sites let the shipping address inherit from billing
  details so nothing is entered twice. Apple Pay and comparable services push
  the complexity out to payment service providers, so the user verifies and
  buys without entering anything more.
- **Amazon Go.** Machine learning, computer vision and AI are integrated deeply
  enough that customers enter, take items and leave. [[User Friction]] drops
  drastically for the user precisely because the designers absorbed a dizzying
  amount of system complexity.
- **Intent-based interaction.** Natural language interfaces such as Mixpanel's
  Spark let users ask a question and get an analysis without knowing the
  system's commands. The complexity shifts from users learning commands to the
  system understanding intent, which democratises access to powerful features.

### Do not mistake complexity for competence

Complexity bias works against this law: humans favour complex solutions over
simple ones because complexity is associated with intelligence and expertise
([[Cognitive Bias]]). The record cites a 1989 study by Farris and Revlin in
which participants preferred complicated hypotheses over the simple rule "list
three numbers that go up", and reads the preference for overengineered
solutions as a symptom of incomplete understanding of the problem.

### Manage the complexity that must stay visible

Not all of the irreducible core can be hidden, so the [[User Interface]]
question becomes which aspects to abstract away and how to guide people through
the rest without overwhelming them.

- [[Progressive Disclosure]] reveals only the essential actions by default and
  defers the rest to dropdowns, accordions or toggles, cutting cognitive load
  and clutter without removing the functionality.
- The paradox of the active user sets where guidance belongs: users never read
  software manuals but start using the software immediately. Help therefore has
  to be available throughout the experience, in tooltips and contextual help,
  rather than front-loaded as documentation.

## Sources (1)

- [[2024-01-23_laws-of-ux_11-9-teslers-law]] — The principle that every system has irreducible complexity that must be transferred either to the user or to the designers and developers; the chapter places the responsibility for absorbing it on designers and developers.
