---
type: concept
name: Information Design
created: 2026-07-31
updated: 2026-07-31
status: developed
---

# Information Design

## Definition

Information design, as these sources use the term, is the discipline of
organising and presenting complex information so that it can be understood
without additional explanation ([[2018-08-12_designing-effective-infographics]],
[[2018-09-09_signal-noise-ratio]], [[2022-12-04_ux-mapping-methods-visual-design-guide]]).
It is concerned with what is shown, how much of it, in what order of prominence,
and through which encoding — text, colour, icon, image, container, layout. Its
central measure is the ratio of relevant to irrelevant content: signal is
whatever serves the user's current task, noise is everything else, and the goal
is to raise that ratio ([[2018-09-09_signal-noise-ratio]]).

Two consequences recur across the corpus. First, encoding is not neutral:
identical information delivered as plain text, as colour, as an icon, or as
several of these at once produces measurably different task performance
([[2016-08-07_visual-indicators-differentiators]]) and different memorability
([[2024-04-26_picture-superiority-effect]]). Second, missing or ambiguous
information is a cost paid elsewhere in the system — in the case of
[[2016-09-11_customer-service-omnichannel-ux]], as support calls that would not
have been needed had the content been clear enough for the user to decide alone.
The same responsibility applies where an interface produces information rather
than merely displaying it, as with calculator and quiz outputs users may base
important decisions on ([[2024-04-12_3-types-calculator]]).

## Practice

### Raise the signal-to-noise ratio, but know it is contextual

[[2018-09-09_signal-noise-ratio]] defines signal as information relevant to the
user's current task and noise as the rest, and warns that the same element can be
signal for one person and noise for another: navigation is noise while reading
content and signal when looking for the next page. It therefore rejects
minimalism as an absolute philosophy, since practical design must balance user
efficiency against visual appeal, branding and business goals. Its concrete
advice: establish content hierarchy before writing or revising, prioritise by
user need, front-load with the inverted pyramid, and use formatting aids (bold,
bullets) to help users separate signal from noise. Consistency mitigates the
tension created by noise that shifts moment to moment.

[[2016-08-07_visual-indicators-differentiators]] sounds a caution in the opposite
direction: on mobile, decluttering can remove cues that were doing real work.
Visual indicators are "clutter" that should stay.

### Choose the encoding deliberately, and prefer redundant cues

[[2016-08-07_visual-indicators-differentiators]] tested four families of list
indicator (text only, colour only, icon only, colour and icon) and found the
combination of unique colour and unique icon best on every UX metric; text-only
indicators were 57% slower for task completion and 56% slower to first correct
click. Icon alone slightly outperformed colour alone, particularly where the icon
carried strong semantics such as up and down arrows for stock performance.
Secondary cues raise the chance a difference is noticed at all. Relying on colour
alone risks failing colourblind users and is open to interpretation —
[[2018-08-12_designing-effective-infographics]] repeats this rule verbatim in its
own domain: colour must never be the only visual distinction.

[[2024-04-26_picture-superiority-effect]] extends the argument to images. Under
dual-coding theory, an image is stored both as image and as a word description
while a word is stored only once, which makes images more memorable. Its
guidance: place information-carrying visuals above the fold and where users spend
time, keep them from auto-rotating, prefer literal and realistic images over
abstract ones that cost effort to interpret, and pick imagery distinct from
surrounding elements and from competitors. It is explicit that text remains
essential for usability, and that text labels add redundancy which strengthens
comprehension and memorability — the same redundancy principle the list-indicator
study demonstrates.

### Group and chunk with containers

[[2016-11-06_cards-component]] describes the card as a container that chunks a
few related pieces of information into one self-contained, clickable unit,
typically mixing media types and linking to fuller detail elsewhere. Its grouping
works through the common-regions principle: items inside a boundary read as
grouped even where proximity alone would not suggest it, which is why borders,
background colour and subtle shadows carry the effect. The source is equally
clear on limits: multiple cards are less scannable than a vertical list because
positions are not predictable, so cards suit browsing more than searching, and
their irregular treatment makes side-by-side comparison hard. They earn their
place with heterogeneous content, where items legitimately differ in structure,
and less so for homogeneous lists.

### Data graphics and infographics

[[2018-08-12_designing-effective-infographics]] treats infographics as
stand-alone content combining data visualisation with illustration, facts, quotes
and captions, and applies a set of rules: maximise the data-ink ratio (the share
of the graphic that carries meaning), present data truthfully with appropriate
scaling, and state sources and baselines so readings are not misleading. On
craft: readable rather than decorative fonts that scale, a limited palette with
enough contrast for colourblind users, simple illustrations that support rather
than distract. Common failures it names are distracting elements, distorted
scales, poorly optimised copy and unclear visual hierarchy. It advises choosing
between static and interactive formats according to intent — making a point
versus enabling exploration — and iterating on audience feedback rather than
pursuing perfection.

### Documents and maps as designed artefacts

[[2022-12-04_ux-mapping-methods-visual-design-guide]] applies information design
to UX maps (empathy maps, journey maps, service blueprints, roadmaps), which
often start as sticky notes or spreadsheets and end up circulated in polished
form. Its sequence: decide first whether polish is warranted (large audience,
public-facing, or high stakes requiring buy-in and perceived legitimacy);
establish a visual system before adding content — header and body text styles,
arrows and lines, labels — so later decisions are fewer and the result coheres;
build a palette of three to six colours, either brand-aligned or used as a
coding system, applied consistently across related maps; lay the foundation with
title, owner and date plus structural lines (thicker, grey or black); then refine
by aligning, distributing and sizing elements evenly. Use a coherent icon set and
supply a legend. The source warns against polish for its own sake and recommends
testing a map as you would test an interface, iterating on feedback.

### Content that lets people decide for themselves

[[2016-09-11_customer-service-omnichannel-ux]] quantifies the cost of poor
information: across 45 customer journeys, 64% required at least one contact with
the organisation, and missing or confusing information was the largest single
driver at 38% of contacts, typically ambiguous policies or insufficient
comparison detail. Its prescription is to eliminate the need for support rather
than the support itself — never hide contact details, but remove the roadblocks,
errors and content gaps that force people to ask, and design for the whole
journey including the points where users switch channel.

[[2024-04-12_3-types-calculator]] looks at outputs generated for the user:
conversion calculators restate inputs in comparable terms, prediction calculators
estimate future outcomes, recommendation calculators give personalised advice,
and the three can be chained so a user moves from understanding a situation to
predicting an outcome to acting. Trust behaviour differs by type — users trust
predictions from complex tools more than simple ones because they do not know how
to interrogate the algorithm, and they often weigh a recommendation as heavily as
their own judgement — which the source turns into a designer's responsibility for
accuracy, since real decisions rest on how outputs are framed and presented.

## Sources (8)

- [[2016-08-07_visual-indicators-differentiators]] — Using multiple redundant visual cues (icon + color) communicates information more effectively than single-method differentiation.
- [[2016-09-11_customer-service-omnichannel-ux]] — Shows the critical role of clear, detailed, and accessible content in enabling users to make decisions without support, particularly around policies and product comparisons.
- [[2016-11-06_cards-component]] — Cards chunk related information into self-contained units and use visual boundaries to indicate grouping, enabling efficient communication of complex content through distinct, digestible pieces.
- [[2018-08-12_designing-effective-infographics]] — the discipline of presenting complex information accessibly; infographic design applies principles like data-ink ratio, visual hierarchy, and minimal clutter to communicate effectively.
- [[2018-09-09_signal-noise-ratio]] — the discipline of organizing and presenting information accessibly; high signal-to-noise ratio is central to effective information design.
- [[2022-12-04_ux-mapping-methods-visual-design-guide]] — Thoughtful layout, spacing, and visual hierarchy help audiences understand and process map content without needing additional explanation.
- [[2024-04-12_3-types-calculator]] — addresses how calculator outputs should be framed and presented for user comprehension and decision-making.
- [[2024-04-26_picture-superiority-effect]] — discusses how images complement text to improve comprehension and message retention.
