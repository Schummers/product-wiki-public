---
type: concept
name: Documentation
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "Design Artifacts"
  - "Design Deliverables"
  - "Design Documentation"
  - "Documentation Produit"
  - "Product Documentation"
  - "Research Documentation"
  - "UX Documentation"
---

# Documentation

## Definition

The sources use "documentation" in three connected senses. The first is
internal: a deliverable is a document that serves as a record of work that has
occurred, produced to communicate design ideas, research findings, and project
context to various audiences — over seventy such artifacts exist across research, strategy,
design, and operations [[2024-08-09_ux-deliverables-glossary]]. Research plans,
design specs, personas, journey maps, promptframes, design-system references and
portfolio material all belong to this family
[[2024-11-01_pm-research-plan]], [[2025-06-20_creating-design-specs-for-development]],
[[2024-05-17_promptframes]]. The second sense is user-facing: help and
documentation is the tenth usability heuristic, the reactive layer of FAQs,
technical manuals, training modules and video tutorials users consult once they
hit a problem or want to become expert [[2020-12-13_help-and-documentation]].
The third cuts across both: a document as the paper trail of a decision. Meeting
notes exist to record not only what was decided but why, because opinions about
the right decision shift over time and without notes there is no way to recover
the logic that produced the original one
[[2020-08-03_articulating-design-decisions_05-chapter-4-listen-to-understand]].

What unites all three is that a document is judged by whether its audience acts
on it. Internally, this means treating colleagues with the same user-centredness
normally reserved for end users — an irony the sketch-test article names
explicitly [[2017-01-22_sketch-test]]. Externally, one source goes further and
treats documentation as a product in its own right, serving the main product
[[2025-06-24_383_Guide_Rédiger_la_documentation_produit]]. Format is never neutral: a polished, uneditable artifact
signals finality and quietly discourages the updates that keep it true
[[2023-01-08_personas-are-living-documents]].

## Practice

### Know which document you are writing, and for whom

Deliverables span the whole project lifecycle — affinity diagrams and personas
in discovery, wireframes and prototypes in design, design systems and roadmaps
in operations — and different audiences need different ones: researchers want
research plans and screeners, designers want wireframes and mockups, executives
want roadmaps and business cases. The deliverable produced also follows from the
method: interviews yield interview guides and empathy maps, surveys yield
demographic data and insights [[2024-08-09_ux-deliverables-glossary]]. For
user-facing documentation, the same targeting question comes first: define who
it is for and why before writing anything [[2025-06-24_383_Guide_Rédiger_la_documentation_produit]].

### Structure before prose

Rather than drafting paragraphs directly, define the target and the objective,
then build a structured bullet-point outline; and work directly inside the final
documentation tool so the format stays realistic instead of designing a layout
the tool cannot produce [[2025-06-24_383_Guide_Rédiger_la_documentation_produit]]. Design specs follow a
parallel logic: a complete spec has two parts, a design file carrying visual and
interaction detail (flows, colour and typography, layout and breakpoints,
component states, real content, accessibility needs) and a development issue
carrying strategic context (goals, use cases, functional and nonfunctional
requirements, scope boundaries, assumptions, success metrics, risks). The design
file says what to build; the issue says why
[[2025-06-20_creating-design-specs-for-development]]. Research plans have their
own required contents: purpose and goals, participants with inclusion and
exclusion criteria, method and procedure, and links to supporting documents such
as consent forms and interview guides [[2024-11-01_pm-research-plan]].

### Keep documents small and maintainable

Small specs are easier to create and implement than one large one; a spec
growing hard to organise is a signal to break it into digestible pieces, defined
together with developers [[2025-06-20_creating-design-specs-for-development]].
The same rationalising instinct governs a design system: only what is actually
and frequently used should remain, since sheer volume of components harms
maintenance [[2024-05-14_328_Gouverner_un_Design_System_@KristinaGudim]].

### Design for updating, not for finality

Personas fail as often from going stale as from being badly made. Overly
polished artifacts — Photoshop files, printed posters — signal immutability and
make updates feel like major undertakings, so teams skip them; an editable
format (a simple slide deck, for instance) invites iteration. The recommendation
is the "prettiest easily editable format" the team can sustain, chosen against
the team's actual design resources, and frequent updates correlate with higher
stakeholder ratings of impact — though updates should follow real business or
user change, not an arbitrary cycle
[[2023-01-08_personas-are-living-documents]]. Research plans should likewise be
updated after the study to reflect what actually changed during sessions
[[2024-11-01_pm-research-plan]].

There is a genuine tension in the corpus here. The mapping guide argues for
investing in polish when a map has a large audience, is public-facing, or is
high-stakes and needs stakeholder buy-in and perceived legitimacy
[[2022-12-04_ux-mapping-methods-visual-design-guide]], while the persona article
warns that overinvestment in visual design is tempting but risky
[[2023-01-08_personas-are-living-documents]]. Both qualify the position rather
than assert it absolutely: polish for reach and stakes, editability for
longevity.

### Visual craft, when it is warranted

For UX maps, establish the visual system before populating content — header and
body text styles, arrows and lines, labels — to cut later decisions and keep
related maps cohesive. Use a palette of three to six colours, either aligned
with company branding or encoding map attributes, applied consistently across
related maps. Lay a foundation of title, owner and date plus structural lines
(thicker, grey or black), then refine alignment, distribution, spacing and
sizing once content is in. Use a coherent icon set and always include a legend
[[2022-12-04_ux-mapping-methods-visual-design-guide]].

### Test the deliverable like an interface

The sketch test applies telephone-game logic to a document: hand it to a
colleague who matches its real audience (developers for wireframes, project
managers for reports) and ask for a short sketch or summary. Watch what they
circle, underline, redraw, or stumble on — these behaviours reveal pain points
better than verbal suggestions — give them scratch paper and permission to
annotate, and do not correct their misunderstandings mid-session, since that
biases the rest of the data. Discrepancies surface both perceptual problems
(content that is visually obscured) and comprehension problems (content that is
misread); different visual metaphors, intermediate inferences and unfamiliar
terminology in their sketch point at content gaps
[[2017-01-22_sketch-test]]. The mapping guide gives the same instruction for
maps: test it like you would test an interface, get feedback, iterate
[[2022-12-04_ux-mapping-methods-visual-design-guide]].

### Documentation as a design activity

Writing product documentation is described as the last brick of the Double
Diamond: the act of explaining the product forces a review of what was designed,
exposes inconsistencies in the interface, and settles the terminology and
wording once and for all. It is also where new improvement opportunities get
spotted [[2025-06-24_383_Guide_Rédiger_la_documentation_produit]]. A related argument holds that documentation is
the designer's business because it is part of the user experience and carries
the product's tone of voice toward the customer, and that it is preferable to
write the simplest possible documentation for the most specific edge cases
rather than believe the interface is perfect [[2025-01-28_362_Générer_de_la_doc_avec_ChatGPT_-_Product_Support_Tech_documentation]]. In a design
system, documentation is the onboarding and training tool rather than a
technical appendix; writing it means gathering the needs of several disciplines
and making it digestible through UX writing [[2024-05-14_328_Gouverner_un_Design_System_@KristinaGudim]].

### User-facing help

Distinguish proactive help (tutorials, instructional overlays, contextual tips
that keep new users or users of a redesigned interface from getting stuck) from
reactive help (documentation, FAQs, training). Within proactive help, prefer
pull revelations — contextual tips tied to the user's current task — over push
revelations, which are unsolicited, given to everyone, and often ignored; reserve
push for essential information and always allow easy dismissal. Reactive help
must be detailed and specific rather than a high-level overview, because the
person reading it already has a concrete problem; a high-level summary belongs
at the top of the page. Optimise for scanning: clear hierarchy, chunked content,
highlighted keywords and lists, both text and video, working search, grouped
categories, and surfaced top content [[2020-12-13_help-and-documentation]].

### Working with AI

Promptframes are a new deliverable sitting between the wireframe and the
high-fidelity prototype: they document what content generative AI should
produce, why, and under what constraints, so that placeholder text stops
sabotaging feedback. Different content types (copy, images, data
visualisations) need their own prompt parameters for tone, style, dimensions and
constraints; personas, brand voice, organisational mission and visual principles
should be given to the AI as context; and iteration happens by revising prompts
and regenerating. Final production content still requires human craft
[[2024-05-17_promptframes]].

For written documentation, the corpus is more cautious and the two French
sources split the task. One recommends defining the rules of a good deliverable
first (the exact structure of a variable name, what a good definition contains),
then few-shot prompting: give the model the rules plus a handful of
hand-written examples so it can see the expected format and quality, and treat
every generated result as requiring manual review to fix missing context and
product-specific vocabulary — a review that sometimes reveals a bad description
is really a badly chosen variable name. The guiding principle is delegating
long, low-value tasks and keeping expertise for where it counts [[2025-01-28_362_Générer_de_la_doc_avec_ChatGPT_-_Product_Support_Tech_documentation]].
The other advises against using AI to build the outline at all, since it will
drop context and edge cases, while endorsing it for turning bullet points into
paragraphs, simplifying text, and challenging finished documentation
[[2025-06-24_383_Guide_Rédiger_la_documentation_produit]].

### Keep a record of decisions, not just of designs

Notes taken during a design meeting are themselves a deliverable, and
[[2020-08-03_articulating-design-decisions_05-chapter-4-listen-to-understand]]
specifies what makes them usable: accessible to everyone who needs them,
organised by agenda item, specific about who said what, definitive in
separating decisions from open items, actionable with an owner assigned to each
task, referenced with links to the material discussed, and forward-looking
enough to serve the next meeting. The point of the discipline is not minutes
for their own sake but a record of design decisions *and their reasoning*, which
is what lets a team manage the conversations that reopen those decisions later.

The same source pairs note-taking with a listening practice: repeating
stakeholder feedback back in design vocabulary establishes the shared language
the notes are then written in
[[2020-08-03_articulating-design-decisions_05-chapter-4-listen-to-understand]].
A companion habit is a standing evidence file — research references, quotes and
data kept where they can be retrieved — which lets a designer back a claim up
the moment it is questioned and demonstrates that decisions were intentional
rather than arbitrary
[[2020-08-03_articulating-design-decisions_08-chapter-7-choose-a-message]].

### Timing and capture

Design specs come after discovery, ideation, prototyping and testing, once the
design is validated and worth the implementation investment; involving
developers early, before designs are final, improves spec quality and reduces
surprises [[2025-06-20_creating-design-specs-for-development]]. Method sections
of a research plan should be detailed enough for another researcher to replicate
the study, and should avoid personally identifiable information by using
participant codes [[2024-11-01_pm-research-plan]].

For a portfolio, the recommendation is continuous capture rather than
retrospective reconstruction: collect sketches, whiteboards, research notes,
prototypes, presentations, feedback, performance metrics and photos of physical
work throughout the year, take an expansive view of what counts as a deliverable
(wireframes, journey maps, personas, research plans, specifications), and
curate them into a roughly thirty-slide deck with three-to-four-sentence speaker
notes giving process, collaborators and goals. Capture before-state material and
quantifiable outcomes, and handle NDA, contract and privacy obligations by
anonymising, redacting or omitting rather than skipping the problem
[[2023-01-15_maintain-ux-portfolio]].

### Conversation over documents: the story-mapping counterpoint

Patton takes a more skeptical position on written documentation than the rest
of this page. He traces the argument to Kent Beck: traditional requirements
documents fail because they cannot capture all the context and nuance a
solution needs, and because different readers interpret the same document
differently, so Beck replaced document-driven specification with conversation
and storytelling [[2014-09-05_user-story-mapping_11-6-the-real-story-about-stories]].
In Patton's own workshops, the practical substitute for a formal document is
what he calls a "vacation photo": a photograph of the whiteboard sketches,
workflow diagrams and marked-up models a team produces while talking through a
story, taken to remember what was decided rather than to specify it
[[2014-09-05_user-story-mapping_11-6-the-real-story-about-stories]]
[[2014-09-05_user-story-mapping_12-7-telling-better-stories]].

This sits in real tension with the note-taking discipline argued for
elsewhere on this page:
[[2020-08-03_articulating-design-decisions_05-chapter-4-listen-to-understand]]
asks for organised, textual meeting notes that separate decisions from open
items and specify who said what, while Patton argues that the visual,
contextual record of a conversation is what actually helps a team recall what
was decided and why, and that a formal story card written up afterward is a
worse record than the vacation photo taken during the conversation itself
[[2014-09-05_user-story-mapping_12-7-telling-better-stories]]. Both positions
agree that the point of any record is the reasoning behind a decision, not
the decision in isolation; they disagree on whether that reasoning is best
captured in writing or in a photographed sketch.

## Sources (16)

- [[2017-01-22_sketch-test]] — A method that tests the effectiveness and understandability of UX documents and visualizations—specifically wireframes, personas, journey maps, and other artifacts—where sketching and annotation by test participants reveal what's perceptually obscured or comprehension-impaired.
- [[2020-12-13_help-and-documentation]] — reactive help including FAQs, technical manuals, training modules, and video tutorials that users consult when they encounter problems or want to become expert users.
- [[2022-12-04_ux-mapping-methods-visual-design-guide]] — Polished UX maps function as high-stakes communication and decision-making artifacts; visual refinement increases their perceived legitimacy and effectiveness with stakeholders.
- [[2023-01-08_personas-are-living-documents]] — Design artifacts communicate intent through their format; editable formats signal openness to change while finished, polished formats signal finality and can discourage updates.
- [[2023-01-15_maintain-ux-portfolio]] — Effective portfolio documentation includes not just final artifacts but process documentation (sketches, notes, photos) that tell the story of how work was created.
- [[2024-05-14_328_Gouverner_un_Design_System_@KristinaGudim]]
- [[2024-05-17_promptframes]] — promptframes represent a new category of deliverable that designers can use to collaborate with AI tools and document their content strategy.
- [[2024-08-09_ux-deliverables-glossary]] — Addresses the purpose, format, and audience for documents that record UX work, focusing on visual and interactive artifacts like wireframes, prototypes, and design systems.
- [[2024-11-01_pm-research-plan]] — the creation of records and supporting materials for research studies that enable effective communication with stakeholders, ensure research replication, and preserve organizational knowledge.
- [[2025-01-28_362_Générer_de_la_doc_avec_ChatGPT_-_Product_Support_Tech_documentation]]
- [[2025-06-20_creating-design-specs-for-development]] — comprehensive written and visual communication of design decisions to guide implementation and support team alignment.
- [[2025-06-24_383_Guide_Rédiger_la_documentation_produit]]
- [[2020-08-03_articulating-design-decisions_05-chapter-4-listen-to-understand]] — Meeting notes are a critical artifact that capture decisions, reasoning, and follow-ups; they must be accessible, organized, specific, and forward-looking.
- [[2020-08-03_articulating-design-decisions_08-chapter-7-choose-a-message]] — maintaining a file of research references, quotes, and data enables designers to back up claims when asked and shows stakeholders that decisions are intentional, not arbitrary.
- [[2014-09-05_user-story-mapping_11-6-the-real-story-about-stories]] — Traditional requirements documents fail because they cannot capture all the context and nuance, and different readers interpret them differently; vacation photos (photos of whiteboards and sketches from conversations) are better than formal specifications.
- [[2014-09-05_user-story-mapping_12-7-telling-better-stories]] — Vacation photos (photographs of whiteboards and sketches made during conversations) capture decisions better than formal story cards; the visual, contextual record helps teams recall what was decided and why.
