---
type: concept
name: Design Trends
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Glassmorphism"
  - "Neobrutalism"
  - "Skeuomorphism"
  - "Visual Design Trends"
  - "Web Design Trends"
---

# Design Trends

## Definition

A design trend is a dominant visual style with a lifespan. The sources describe
trends as fundamentally reactive: each one responds to the limitations of what
came before, and the movement is cyclical rather than progressive. Excessive
skeuomorphism gave way to flat design; flat design's weak signifiers produced
neumorphism, which reintroduced subtle 3D effects with limited success
[[2024-03-15_skeuomorphism]]. Brutalism arose as a reaction against
cookie-cutter template design [[2017-11-05_brutalism-antidesign]], neobrutalism
as a rebellion against sleek minimalism [[2025-04-11_neobrutalism]], and
handmade aesthetics as an answer to years of AI-generated-looking polish
[[2026-04-10_handmade-designs]], which describes the movement explicitly as a
pendulum swinging in response to whatever dominates.

The corpus treats each trend the same way: describe what it is made of, then
test it against usability and accessibility. The recurring verdict is that a
trend is legitimate as a **visual** layer over a sound interface and
illegitimate when it starts costing readability, discoverability, predictability
or task completion — the criticism levelled at antidesign
[[2017-11-05_brutalism-antidesign]], at the visual-excess phase of
skeuomorphism [[2024-03-15_skeuomorphism]], and at iOS 26's Liquid Glass
[[2025-10-10_liquid-glass]].

## Practice

### Trends are cyclical and reactive

Trends respond to their predecessor's limitations, and elements periodically
resurface: skeuomorphic details reappear inside later trends, including
neobrutalism's nostalgic 90s and early-web references
[[2024-03-15_skeuomorphism]], [[2025-04-11_neobrutalism]]. The practical
implication drawn in [[2024-03-15_skeuomorphism]] is a balance principle:
effective design balances innovation against familiarity, applying a trend's
principles without the ornamental excess. [[2026-04-10_handmade-designs]] adds
that trends carry emotional signals — audiences are responding to cultural
fatigue, not only to aesthetics.

### Skeuomorphism: metaphor as learning aid, texture as excess

The corpus separates two things that share a name
[[2024-03-15_skeuomorphism]]. As a **functional** device, skeuomorphism borrows
familiar real-world objects to make digital interfaces easier to learn,
leveraging existing mental models; the trash bin, the folder and the floppy-disk
save icon are still in use. As an early-2010s **visual trend**, it became
excessive realistic textures, shadows and gradients that prioritised aesthetics
over digital efficiency, producing cluttered interfaces, slower load times from
processing demands, and occasionally unintuitive interactions that
paradoxically disconnected users from digital functionality.

### Brutalism and antidesign are not the same thing

[[2017-11-05_brutalism-antidesign]] insists on the distinction. Brutalism, in
the architectural lineage, values honesty, rawness and function over form, and
digital brutalism echoes early-1990s websites with minimal styling. Antidesign
deliberately manufactures visual chaos — harsh colours, distracting animations,
poor hierarchy — motivated by humour, attention-seeking or boredom rather than
function.

The verdicts differ accordingly. Brutalism can work when it is confined to
visual design while navigation, hierarchy and interaction patterns stay strong.
Antidesign backfires for anything requiring task completion or content
discovery: users want to accomplish goals, not solve puzzles, and the majority
prefer clarity over novelty. Both are most defensible for entertainment
products and designer audiences who get the irony. The source rejects the
framing of a tension between boring clarity and interesting difficulty:
interfaces simplify because that is what users need, and designers should not
impose complexity out of personal interest.

### Neobrutalism: bold, but bounded by usability

Neobrutalism evolves from brutalism while being more colourful and more orderly,
and is exemplified by brands such as Figma and Gumroad
[[2025-04-11_neobrutalism]]. Its five characteristics: high contrast and bright
primary colours to emphasise key functions; thick lines and geometric shapes
building structure without gradients; stark single-colour drop shadows for
depth; bold, "unpolished" typefaces carrying personality; and skeuomorphic
elements evoking 90s and early-web nostalgia. Implementation constraints from
the same source:

- Limit the palette to 2–3 bold, high-contrast colours.
- Pair bold headlines with clean, neutral body fonts.
- Use generous whitespace (24–32px margins) to offset the geometric elements.
- Maintain hierarchy through size variation and colour intensity.
- Meet WCAG contrast ratios; avoid vibrant pairings such as yellow on cyan that
  fail readability tests, and check combinations with a contrast checker such
  as Coolors'.

Without that balance, the style overwhelms users and hinders accessibility;
clear buttons, readable type, ample whitespace and intuitive interaction
patterns stay in the foreground even within a raw aesthetic.

### Glassmorphism: usable in principle, fragile in execution

[[2024-06-07_glassmorphism]] is the constructive treatment: translucency
mimicking frosted glass, prominent in Apple's and Microsoft's design systems,
creating layered depth that helps users separate foreground from background.
Opacity controls how much background shows through, blur distorts it to reduce
distraction, and low-opacity strokes plus gradient fills add sophistication,
especially over simple or single-colour backgrounds. The heavier the background
(photos, video, animation), the more blur is needed. Its central risk is
contrast: translucent elements let text fall across several colours, making
contrast ratios unpredictable, so accessibility must be verified across
background conditions, and user controls such as contrast adjustment or reduced
transparency (as in Apple's accessibility settings) should be offered where
feasible.

[[2025-10-10_liquid-glass]] is the critical counterpart, and the two sources sit
in tension: the first treats glassmorphism as workable when opacity, blur and
contrast are handled deliberately; the second argues that Apple's Liquid Glass
in iOS 26 shows the trend delivering visual complexity without functional
benefit. Its findings:

- Transparency obscures content: text on images, icons blending into
  backgrounds, translucent controls hiding what is underneath — invoking the
  long-standing usability finding that anything layered on top of something
  else becomes harder to see.
- Motion without purpose becomes distraction: animated buttons, morphing
  controls and shimmering elements delight on first use and turn into noise and
  fatigue by the hundredth.
- Tap targets shrink below the 1cm² guideline, and a floating search button
  fragments what used to feel like a unified control area.
- Interfaces that appear, vanish, collapse and expand by context force
  rescanning and destroy predictability and learnability — the forward button
  showing only when needed disrupts the learned location of the target.
- Abandoned conventions cost long-time users: search moved from top to bottom,
  changed back-button behaviour, Android-style patterns. Even if the new
  patterns eventually prove better, relearning costs productivity.
- Hidden controls reduce discoverability: breadcrumbs dropped from back
  buttons, tabs pushed into overflow menus, truncated URLs.

### Handmade aesthetics as a trust signal

The most recent trend in the corpus moves away from polish toward visible human
authorship: linocut illustration, watercolour, hand-lettered type, wabi-sabi
appreciation of imperfection, variable line weights, incomplete paths, visible
brushstrokes, organic shapes, misalignment and imperfect colour fills
[[2026-04-10_handmade-designs]]. Brands such as Hermès, the Paris Olympics and
Acne Studios pair these visuals with emphasis on the human artist behind the
work, where the human story is what gives it value and irreplaceability, and
authenticity is the answer to AI fatigue.

Two caveats from the same source. First, handmade warmth is a signal, not a
guarantee: warm design concealing poor functionality undermines trust rather
than building it. Second, adoption can be gradual — no full rebrand is needed;
try it in one campaign, one feature or on social media, and expand if it
resonates.

## Sources (6)

- [[2017-11-05_brutalism-antidesign]] — examines brutalism and antidesign as reactions to previous design trends and their sustainability.
- [[2024-03-15_skeuomorphism]] — explores both the functional use of real-world metaphors to aid learning and the visual excess phase that later fell out of favor, illustrating the cyclical nature of design trends and how each responds to limitations of its predecessor.
- [[2024-06-07_glassmorphism]] — glassmorphism is a specific translucent design approach that mimics frosted glass, creating layered depth and visual sophistication, representing a contemporary design trend particularly popular in Apple and Microsoft systems and reflecting evolving aesthetic and technical possibilities.
- [[2025-04-11_neobrutalism]] — documents neobrutalism as an emerging trend that reacts against minimalism by emphasizing bold aesthetics, high contrast, and raw, unpolished elements.
- [[2025-10-10_liquid-glass]] — Examines the glassmorphic trend in iOS 26 as problematic: translucent, layered elements reduce contrast, obscure content, and create visual complexity without functional benefit.
- [[2026-04-10_handmade-designs]] — Shows how trends respond to cultural fatigue and what signals audiences are responding to emotionally.
