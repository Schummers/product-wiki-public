---
type: concept
name: Mental Model
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Mental Models"
  - "User Mental Models"
---

# Mental Model

## Definition

A mental model is a user's belief about how a system works, formed from
background knowledge and past experience rather than from facts about the
system's actual construction [[2024-01-26_mental-models]]. It is an internal
representation, built through repetition and observation, that users apply to
predict what an interface will do, decide where to look, and choose what to
click [[2017-12-10_practiced-patterns-mistakes]]. The model does not have to be
correct to be operative: what users believe about a system, accurate or not,
determines what they actually do with it [[2024-10-25_technology-myths]]. When
users cannot understand how something works, they invent explanations that feel
logical from what they already know, and those inaccurate theories, called
technology myths, spread and drive behaviour just as strongly as accurate ones
[[2024-10-25_technology-myths]].

Mental models are assembled from prior exposure: real-world objects and
activities [[2018-07-01_match-system-real-world]], physical systems and their
spatial or cultural conventions [[2018-10-14_natural-mappings]], and the
accumulated practice of using dozens of other websites and apps
[[2016-10-30_power-law-learning]]. Because users borrow rather than build from
scratch, an interface that mirrors a model they already hold is learned quickly,
while one that contradicts it produces confusion, misdirected attention, and
undetected errors [[2017-12-10_practiced-patterns-mistakes]]. Models are also
sticky: once formed they persist even when unhelpful
[[2024-01-26_mental-models]], survive technological improvement if the design
does not actively correct them [[2022-03-20_facial-recognition-payment]], and a
single failure can convince a user a system cannot do something, after which
they will not come back to retry it even once it works
[[2019-02-03_mental-model-ai-assistants]]. A recurring design problem is the
distance between the designer's detailed model of their own product and the
user's much thinner one [[2024-01-26_mental-models]].

## Practice

### The two moves: conform to the model, or change it

When users hold an erroneous model, the sources describe two options. The first
is to make the system conform: move content or reorganise navigation so it sits
where users already expect to find it, guided by research such as card sorting
[[2024-01-26_mental-models]]. The second is to improve the model itself, through
clearer labels, explanations and documentation
[[2024-01-26_mental-models]]. The same pair recurs for AI agents, which must
either align with the models users arrive with or explicitly teach the new
paradigm [[2026-05-08_designing-ai-agents]]. A third, intermediate position
appears in the AI literature: design for the mental models users currently hold
while gradually priming the expectations they will need later, since models
evolve slowly across a population [[2025-02-28_scope-ai-features]].

### Borrowing from the real world

Matching the real world is Nielsen's second usability heuristic: use familiar
words rather than system-oriented jargon, make UI elements that look like
physical objects behave like them, and present information in the order users
expect [[2018-07-01_match-system-real-world]]. Natural mappings extend this to
the arrangement of controls: spatial similarity (a monitor-arrangement control
laid out like the actual desk), metaphorical and cultural associations ("up is
more", "green is go"), and behavioural similarity (raise-to-wake mimicking how
people tilt a watch) all speed learning and cut errors, while complex
multi-finger gestures violate the principle because nothing relates the action
to the outcome [[2018-10-14_natural-mappings]]. Skeuomorphism is the same
leverage applied to visual design: trash bins, folders and floppy-disk icons
work as functional learning aids by connecting to existing models of physical
objects [[2024-03-15_skeuomorphism]], [[2024-01-26_mental-models]]. The sources
qualify this rather than disagree: skeuomorphism as a 2010s visual trend became
excessive, cluttering interfaces and occasionally producing unintuitive
interactions, so the recommendation is balance between familiarity and
innovation rather than maximal realism [[2024-03-15_skeuomorphism]]. For
children, the borrowing is especially strong: skeuomorphic design and real-world
metaphors such as a coloring book or a real kitchen let them apply what they
already know and reduce cognitive load [[2018-12-16_kids-cognition]].

Bridging the gulfs of evaluation and execution rests on the same mechanism:
designs with clear visual similarity to familiar models — a checkbox that
matches paper-form convention — let users correctly interpret system state and
predict what an action will do [[2018-03-11_two-ux-gulfs-evaluation-execution]],
and good mappings reduce the gap between intention and execution
[[2018-10-14_natural-mappings]].

### Consistency, practice, and the cost of deviating

Consistency is not aesthetic preference but a consequence of how learning works:
using a standard pattern gives the user one more repetition of something they
have already practised across dozens of other sites, so they reach proficiency
faster [[2016-10-30_power-law-learning]]. Deviating restarts the learning curve,
which is only worth it if the new design performs substantially better once
learned, if users will encounter it often enough to practise it, or if the brand
value justifies the cost [[2016-10-30_power-law-learning]].

The most dangerous deviation is the small one. When a design mimics a familiar
pattern but differs slightly — a Filter button styled like a Search Submit
button — users apply the learned pattern automatically, do not notice the
difference, and make errors they never become aware of, because well-practised
tasks consume so little attention that mistakes go uncorrected
[[2017-12-10_practiced-patterns-mistakes]]. Violated expectations also
misdirect attention: users skip screen regions their model says content
"shouldn't be" in [[2017-12-10_practiced-patterns-mistakes]]. The prescription
is to either comply fully with the established pattern or depart completely and
obviously, so conscious processing kicks in
[[2017-12-10_practiced-patterns-mistakes]]. Consistency of behaviour matters as
much as consistency of appearance: when facial-recognition payment sometimes
asked for secondary authentication and sometimes did not, users lost confidence
about whether the payment had gone through, and any such variance needs an
explanation attached [[2022-03-20_facial-recognition-payment]].

Familiarity has a cost as well as a benefit. The hamburger icon is recognised by
83% of participants, chiefly because of its top-left position, but that same
learned association creates interference: three-line icons in that position get
read as menus even when they mean list view or filters, and recognisability does
not make hidden navigation as usable as visible navigation
[[2025-06-13_hamburger-menu-icon-recognizability]].

### Surfacing mental models in research

Several methods exist specifically to externalise models. Cognitive mapping asks
participants to draw and arrange materials, producing artefacts that reveal
hierarchies and relationships people cannot easily articulate; it suits
exploratory, complex and participatory work, needs 2-3 practice sessions before
real research, and is analysed with qualitative coding across maps, transcripts
and facilitator notes. Comparing maps across participants shows whether a group
shares one model, splits into distinct clusters, or varies widely
[[2019-08-11_cognitive-mapping-user-research]]. Card sorting targets how users
relate items, but is easily corrupted by keyword matching, where participants
group cards on shared words rather than meaning and produce groupings that do
not reflect their real models; the countermeasures are synonyms instead of
parallel labels, non-parallel grammatical structures, in-depth descriptions, and
facilitation that explains the objective and asks participants to think aloud
[[2024-06-14_card-sorting-terminology-matches]]. Contextual inquiry gets at the
reasoning behind actions by observing work in its natural setting and probing
with follow-up questions, surfacing habitual workarounds and superstitious
behaviours that have become invisible to the user
[[2020-12-06_contextual-inquiry]]. Usability tests and attitudinal studies are
also myth detectors: listen for gaps between what users believe and what the
system does, since each gap marks a place where design clarity is failing and
signals an opportunity for explicit communication or progressive disclosure
[[2024-10-25_technology-myths]].

Models also need to be aligned inside the team, not only observed outside it.
Common ground — the shared knowledge that lets colleagues use shortcuts instead
of explaining everything — is built through shared vocabulary and artefacts such
as personas and journey maps, and one-to-one conversation is where individual
mental-model misalignments get clarified [[2021-05-09_common-ground]].
Practitioners' own models diverge too: research on design thinking found
definitions ranging from a problem-solving process to a mindset shift to a
flexible toolkit, apparently tracking expertise, and the recommendation is that
each organisation write an explicit working definition rather than assume an
industry norm [[2018-12-02_design-thinking-practitioners-say]].

### When the system is opaque: algorithms, AI, and new technology

Opacity is the main obstacle to accurate models. Users treat machine-learning
systems as black boxes and try to infer input-output relationships by
experimentation; when the inputs are unclear or the effects delayed, accurate
models become nearly impossible and users conclude they are being tracked far
more invasively than they are — one participant believed Facebook listened to
conversations [[2018-12-16_machine-learning-ux]]. Netflix's "Because you
watched X" labels are cited as best practice for revealing inputs, though even
there the model broke when the outputs contradicted what users expected
[[2018-12-16_machine-learning-ux]]. Transparency is the general antidote: explain
briefly how complex features work, add explainability to recommendations, and
communicate about data use, or users will fill the gap with myths that cost them
real time and effort — clearing form fields to "protect privacy", switching
devices to dodge price tracking [[2024-10-25_technology-myths]].

The facial-recognition payment studies are the fullest case. Four onboarding
mistakes (no explicit consent request, no explanation of how recognition works,
no choice of payment account, no confirmation password) produced false models
about security, and 4 of 5 participants preferred QR-code scanning despite FRP
being faster — convenience did not outweigh distrust
[[2020-05-10_face-recognition-pay]]. Three years later the same misconceptions
persisted: users still believed the system compared their face to a stored
photo rather than recognising features, showing that inaccurate models survive
technical improvement unless the design actively corrects them
[[2022-03-20_facial-recognition-payment]]. Both sources recommend handholding
and brief explanations at the point of use, including alongside advertising
[[2020-05-10_face-recognition-pay]], [[2022-03-20_facial-recognition-payment]].

For voice assistants, users hold models of the system as unintelligent —
comparable to a young child or someone with poor hearing — and consequently
restrict themselves to simple, predictable requests and sometimes compress their
speech into keywords [[2018-08-05_voice-assistant-attitudes]]. A diary study
found three dominant models: the assistant as an interface to the web and smart
home, as a handy helper, or as a repository of all knowledge, and these shape
usage far more than advertised skills do; models form from what users actually
try and what succeeds, not from marketing
[[2019-02-03_mental-model-ai-assistants]].

Generative AI repeats the pattern. New users cannot tell an image generator from
a conversational chatbot and ask the tool about its own capabilities rather than
reading documentation, so tool names should signal function, tutorials should be
brief and answer "What does this do?" and "How does it work?", help should
arrive contextually at the moment of need, and examples should be general enough
to invite exploration [[2024-03-29_new-ai-users-onboarding]]. Users also conflate
generative AI with search engines and expect the wrong interaction paradigm, so
both education and interface behaviour have to work on the expectation
[[2026-02-06_ai-literacy]]. Entrenched search-bar expectations are given as a
concrete reason AI feature adoption is slow [[2025-02-28_scope-ai-features]].
For agents, users' models favour answering questions over completing
transactions, which is why discoverability needs redundant entry points; mirroring
established conventions such as delivery-app patterns builds confidence, but the
borrowed pattern must still fit the context — a carousel showing one option at a
time made users underestimate how much choice they had
[[2026-05-08_designing-ai-agents]]. Perceptions of data handling follow the same
logic: showing a full address before item selection creates a false impression of
data leakage, so surface only the minimum at each step and explain its use
[[2026-05-08_designing-ai-agents]].

On AI features generally, respecting existing models is the dividing line
between the examples given: Adobe Lightroom's AI object removal works with what
users already do, while Instagram's AI chat placed in search violates it, and
generative AI does not remove the need for research and a deep understanding of
users' mental models [[2024-11-08_ai-user-value]]. Scope is a lever here: narrow
features like a playlist generator are easier for new users to understand and
prompt than broad systems such as ChatGPT, whose flexibility forces users to
imagine the capabilities for themselves [[2025-02-28_scope-ai-features]]. AI
literacy itself splits into two independently developing capabilities, prompt
fluency and output literacy, and design must support both — prompt suggestions
and lightweight constraint controls on one side, visible verify actions on the
other — because frequent use does not imply critical evaluation
[[2026-02-06_ai-literacy]].

### Models attached to specific interface objects

Users also hold models of individual features, and those models can be finer
than the designer's labels. Shopping carts are used as external memory and as
comparison tables, not only as purchase vehicles; users read a cart addition as
"might want" and a list addition as "definitely want", so they add to the cart
even when they mean to save long-term, and the word "wishlist" carries
gift-sharing connotations that put them off. Save-for-later must therefore be
discoverable, clearly labelled, low-effort, and never gated behind registration
[[2018-11-04_wishlist-or-cart]]. With calculators and quizzes, users treat the
tool as an exploration device: they enter rough estimates first to build a model
of what it is worth, work it both forwards and backwards to understand the
input-output relationship, and expect that supplying more detail yields more
accurate results, mirroring their model of consulting a specialist
[[2024-03-22_calculator-expectations]]. Cloud storage shows the cost of a
mismatched borrowed model: users apply single-agent models from traditional file
systems and email to multi-agent cloud systems, attach cloud documents to email
expecting recipients to gain access, misjudge access rights, and invent their own
collaboration policies to work around what they do not understand
[[2019-11-24_cloud-storage]].

## Sources (31)

- [[2016-10-30_power-law-learning]] — Users develop mental models based on patterns they practice across multiple websites; familiar patterns activate more readily in memory and users expect interfaces to follow patterns they've previously learned.
- [[2017-12-10_practiced-patterns-mistakes]] — Users' internal representation of how an interface works; built through repeated experience, mental models guide attention and behavior; interface changes that violate mental models cause confusion and errors.
- [[2018-03-11_two-ux-gulfs-evaluation-execution]] — using familiar design patterns to help users build accurate mental models of system behavior.
- [[2018-07-01_match-system-real-world]] — The article explains how users build mental models based on past experiences with real-world objects and activities, and how good design leverages these existing models to make interfaces intuitive and easy to learn.
- [[2018-08-05_voice-assistant-attitudes]] — users' beliefs about what assistants can do shape their interactions significantly; they view these systems as far less intelligent than true AI, limiting ambitions for complex tasks.
- [[2018-10-14_natural-mappings]] — how users' existing understanding of how physical systems work informs their expectations for how digital systems should behave.
- [[2018-11-04_wishlist-or-cart]] — understanding how users conceptualize the difference between carts and wishlists, and how to design features that align with their natural assumptions.
- [[2018-12-02_design-thinking-practitioners-say]] — The research reveals how different expertise levels produce different mental models of design thinking, with novices viewing it as a process while experts treat it as a dynamic toolkit.
- [[2018-12-16_kids-cognition]] — Children apply existing knowledge of the real world to interfaces, meaning skeuomorphic designs and familiar metaphors help them learn quickly.
- [[2018-12-16_machine-learning-ux]] — Users' theories about how algorithms work, formed through observation and experimentation; lack of transparency prevents accurate mental model formation.
- [[2019-02-03_mental-model-ai-assistants]] — Analysis of how users conceptualize intelligent assistants as interfaces, helpers, or knowledge repositories, and how these models drive usage patterns and expectations.
- [[2019-08-11_cognitive-mapping-user-research]] — The method is specifically designed to surface how users organize and relate concepts, making it valuable for understanding complex domains and system design.
- [[2019-11-24_cloud-storage]] — documents the gap between users' simplified mental models of cloud systems and actual system complexity.
- [[2020-05-10_face-recognition-pay]] — describes how users develop false mental models when technology is not properly explained, leading to security concerns that override perceived benefits.
- [[2020-12-06_contextual-inquiry]] — understanding the underlying reasoning and thought processes users employ when completing work, uncovered through observation combined with probing questions about their actions.
- [[2021-05-09_common-ground]] — One-to-one communication can clarify mental model misalignments and unique individual understandings when building common ground with specific stakeholders.
- [[2022-03-20_facial-recognition-payment]] — how users' understanding of how technology works shapes their trust and willingness to use it, even when their models are inaccurate.
- [[2024-01-26_mental-models]] — a foundational concept for understanding how users predict system behavior and make decisions about interface interactions.
- [[2024-03-15_skeuomorphism]] — emphasizes how skeuomorphic design leverages existing user mental models of physical objects to ease digital interface adoption.
- [[2024-03-22_calculator-expectations]] — explains how users form mental models around calculator tool capabilities and input-output relationships.
- [[2024-03-29_new-ai-users-onboarding]] — explores how users form mental models about AI tools based on onboarding experiences and initial interactions.
- [[2024-06-14_card-sorting-terminology-matches]] — card sorting aims to understand users' mental models of relationships between items; keyword matching produces superficial groupings that do not reflect actual mental models.
- [[2024-10-25_technology-myths]] — internal, often inaccurate representations of how systems work that users develop based on their experiences, beliefs, and existing knowledge; mental models drive user behavior.
- [[2024-11-08_ai-user-value]] — Explains how well-designed AI features like Adobe Lightroom respect users' existing mental models, while poorly designed features like Instagram's AI chat violate them.
- [[2025-02-28_scope-ai-features]] — Discusses how users' ingrained mental models (e.g., search-bar expectations) slow AI feature adoption; design must work with current models while gradually priming future expectations.
- [[2025-06-13_hamburger-menu-icon-recognizability]] — users' internal understanding of how a system works, built through learned associations and repeated exposure to consistent patterns.
- [[2026-02-06_ai-literacy]] — Users conflate genAI with search engines, expecting different interaction paradigms; education and design must align interface behavior with user expectations.
- [[2026-05-08_designing-ai-agents]] — Users approach agents with mental models shaped by prior experience; agents must either align with existing models or explicitly teach new paradigms; mental-model mismatches cause confusion and abandonment.
- [[2024-01-23_laws-of-ux_03-1-jakobs-law]] — A user's internal representation of how a system works, built through experience with similar systems; designers can improve user experience by aligning their designs with these mental models so users can apply previous knowledge without needing to learn new interaction patterns.
- [[2013-08-01_just-enough-research_06-chapter-5-user-research]] — the chapter defines mental models as an individual's pre-existing internal concepts and associations with systems and situations; understanding mental models helps design interfaces that hook into existing maps rather than requiring users to learn from scratch.
- [[2013-08-01_just-enough-research_09-chapter-8-analysis-and-models]] — explains mental models as internal cognitive representations; describes how to diagram them from affinity clusters, and how they guide information architecture and reveal gaps between user expectations and product design. Hall notes that the diagram sense of the term follows Indi Young's work, *Mental Models: Aligning Design Strategy with Human Behavior*.
