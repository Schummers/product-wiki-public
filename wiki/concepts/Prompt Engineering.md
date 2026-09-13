---
type: concept
name: Prompt Engineering
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "AI Prompt Engineering"
  - "Prompt Design"
  - "Prompt Iteration"
  - "Prompt Structure"
  - "Prompt Suggestions"
---

# Prompt Engineering

## Definition

A prompt is a discrete input from the user that initiates or guides a chatbot's
response, and a conversation may contain one or many
[[2023-11-24_ai-prompt-structure]]. Prompt engineering is the practice of
crafting those inputs to elicit the desired output
[[2024-02-02_response-outlining]], [[2024-03-08_chatgpt-and-tone]]. Analysis of
425 real chatbot interactions found four recurring components: the **request**
(the core information need), **references** (internal, quoting a previous bot
answer, or external, such as pasted document text), **format** (length, language,
presentation style, tone) and **framing** (problem description, goals, user
background, roleplaying). Not every prompt carries all four, and their relative
importance varies by conversation type; the source describes the user's
information need as an iceberg whose visible tip is the prompt, with the AI
becoming more effective the more of the submerged mass is surfaced
[[2023-11-24_ai-prompt-structure]].

The corpus treats prompt engineering as a moving target rather than a settled
skill. One source calls prompt writing a currently broken user experience and
argues design should let people reuse familiar patterns — Perplexity made its
input resemble a search box so non-technical users could succeed with simple
keywords instead of mastering prompts [[2024-02-16_perplexity-henry-modisett]].
Another describes the field moving beyond single instructions into context
engineering, where system instructions, retrieved knowledge, skills, tools,
memory and state all compete for the model's attention, and where prompt design
becomes context design [[2026-06-12_context-architecture]].

## Practice

### Structure the prompt

The CARE mnemonic organises what to include: **Context** (background such as user
profiles, organisation mission, project goals, tone of voice), **Ask** (the
specific request, stating the desired role, output format, number of options,
steps to follow, and how to iterate), **Rules** (constraints such as avoiding
passive voice, staying under 100 characters, using plain language, plus product
and brand rules) and **Examples** (good and bad, so the model grasps not only
what is wanted but why). The same source names chain-of-thought prompting —
breaking a task into discrete ordered steps so the model proceeds
systematically — and few-shot prompting, and it is explicit that iteration
remains necessary even with careful prompts: designers typically refine outputs,
ask for variations, and combine options [[2024-05-24_careful-prompts]].

Response outlining is the narrower technique of putting format or structure
specifications into the prompt — numbering, bullet points, section headings,
required elements such as a SWOT analysis. Users typically discover the needed
specification only after an unsatisfactory answer and add it in a follow-up.
Combining several structural and format requirements works better than a single
isolated constraint. The cost is high: users must anticipate the shape of an
answer they have not seen yet, which carries real cognitive load and typing
effort [[2024-02-02_response-outlining]]. Framing carries a similar cost — it
demands that users think of everything the bot might need and type it out, which
is why many conversations with well-defined goals begin without it
[[2023-11-24_ai-prompt-structure]].

For generating interfaces, one source recommends writing prompts as
specifications: detail the user journey step by step and make the wanted features
explicit exactly as one would in technical specs for a developer — bad specs
given to a very good developer still produce a bad result
[[2025-08-26_392_Artifact_le_meilleur_outil_de_micro-prototypage_IA_pour_designers_&_PMs]].

### Prompt shape determines conversation shape

The six observed conversation types map onto how well the opening prompt is
specified. Search-query conversations are single, simple prompts where users
transfer a search-engine mental model and supply too little context. Funnelling
conversations start vague and need several exchanges to narrow down, even though
the underlying need is specific but poorly articulated. Pinpointing
conversations invest heavy effort upfront — full context and format
specification — and stay short. Exploring and chiselling conversations are long
by nature, serving less well-defined needs through depth or breadth, and
expanding conversations start too narrow and get widened by removing criteria.
The source is explicit that length is not a success measure: both short and long
conversations can be helpful [[2023-11-10_ai-conversation-types]]. Request-only
prompts that resemble search queries are inefficient and lead to funnelling
[[2023-11-24_ai-prompt-structure]].

### Specifying tone

Tests of common tone strategies found that a single tone adjective makes the
model latch onto that word and exaggerate it unnaturally, whereas several
nuanced descriptors together ("happy, professional, business-casual") prevent
over-indexing and balance the output. The most effective approach is not
abstract description at all but supplying existing copy as a stylistic model to
mirror. Requesting several alternatives raises the odds of a usable result and
lets elements be combined. Outputs still tend toward the forced or cartoony, so
human editing remains essential; an organisation without tone-of-voice
guidelines can have the model analyse its existing copy and draft them
[[2024-03-08_chatgpt-and-tone]]. For visual output, another source suggests
asking the model to take inspiration from the design of well-known companies
(Apple, Notion, Uber) to avoid a crude default rendering, favouring English in
prompts and avoiding long iteration chains inside a single conversation
[[2025-08-26_392_Artifact_le_meilleur_outil_de_micro-prototypage_IA_pour_designers_&_PMs]].

### Prompts shape model failure modes

Sycophancy — a model adapting its answer to match the user's stated view even
when that view is false — is an inherent consequence of training on human
approval. Asking "Are you sure?" can make a model reverse a factually correct
answer, and stating an opinion such as "I dislike this argument" changes the
response to match, including on demonstrably false mathematical statements. The
practical countermeasures given for researchers are behavioural: reset
conversations often, avoid expressing strong opinions while working with the
tool, and never rely on a language model alone for fact-finding without
double-checking [[2024-01-12_sycophancy-generative-ai-chatbots]].

### Design the interface so users need less prompting skill

Prompt controls — buttons, toggles and menus around the input field — expedite
and supplement text input. Four uses emerge: raising discoverability of
capabilities so users need not ask "can you" questions; conversation starters
that teach new users what the bot can do; scope constraints (Perplexity's Focus,
for instance) that narrow the domain before asking and thereby improve relevance
and reduce hallucinations; and follow-up controls for editing, regeneration and
suggested next questions. The best practices are conventional ones: standard
icons with labels or tooltips, clear feature names, grouping by function, and
following existing design conventions. Their purpose is to overcome the
articulation barrier [[2024-08-02_prompt-controls-genai]] — the same barrier
that response outlining exposes, where users lack the jargon or clarity to state
requirements even when they know what they want, and where a UI could suggest
structural elements or ask for preferences upfront instead of letting users learn
through failure [[2024-02-02_response-outlining]].

Use-case prompt suggestions are the content side of this. Their complexity should
match the context: simple clickable pills for broad systems and low-complexity
tasks, richer examples such as conversation replays or video demonstrations for
specialised systems and complex tasks. Curated suggestions in pre-authentication
views act as lightweight onboarding for new users; for active users,
context-aware suggestions surfacing when they face ambiguity or lack domain
knowledge give just-in-time guidance. Specificity wins ("Easy family dinners"
over "Recipe ideas"), individualisation by skill level or prior behaviour
increases relevance, and placement near the input field maximises engagement.
Analytics can identify which suggestions drive engagement, provided placement and
order biases are controlled for [[2025-06-27_designing-use-case-prompt-suggestions]].

The corpus is consistent that the fix is design rather than user training: prompt
engineering is named as the current friction point, and external consistency
with familiar patterns such as a search box lets people apply existing knowledge
instead of learning prompt craft [[2024-02-16_perplexity-henry-modisett]].

### Prompting as a group activity

In AI-enhanced workshops, prompts are worth writing collaboratively: the
discussion small groups have while drafting a prompt together is often as
valuable as the output they get. Budget more time than expected, roughly 8-10
minutes per prompt against 5 without AI, so participants can write thoughtfully,
read the response and iterate. Because AI can generate hundreds of ideas in
minutes, the standard diverge-converge structure needs an intermediate step where
AI ranks ideas against criteria the group has agreed (feasibility, desirability,
viability, or custom) before human discussion; limiting how many ideas the AI
produces would undercut its strength. Digital documentation suits AI's long
outputs better than physical sticky notes
[[2025-06-06_facilitating-ai-workshops]].

### From prompt design to context design

Context is described as an ecosystem to be discovered and selected, not a list of
system prompts: instructions, RAG-retrieved knowledge, skills, tools, long- and
short-term memory, and the user prompt all compete for the model's attention.
Information-architecture principles apply directly — establish hierarchies that
prioritise information, use categorisation and labelling that align with user
language rather than engineering terminology, and give skills and tools a clear
taxonomy, controlled vocabulary and unambiguous naming, since poor labelling
leads agents to pick the wrong tool and take unnecessary steps. Misalignment
between internal terminology and users' mental models makes agents perform the
wrong actions. These are framed as design decisions that determine how meaning is
constructed [[2026-06-12_context-architecture]].

## Sources (12)

- [[2023-11-10_ai-conversation-types]] — the article identifies how the structure and completeness of initial prompts (pinpointing vs. search queries) affects conversation length and efficiency.
- [[2023-11-24_ai-prompt-structure]] — understanding prompt structure helps users and designers create more effective prompts that include request, references, format, and framing components.
- [[2024-01-12_sycophancy-generative-ai-chatbots]] — the way users formulate prompts (including expressing opinions) directly influences whether models exhibit sycophantic behavior.
- [[2024-02-02_response-outlining]] — the practice of crafting prompts to elicit desired AI outputs, including response-outlining techniques.
- [[2024-02-16_perplexity-henry-modisett]] — the current friction point in AI tools; better design can reduce reliance on complex prompting skills.
- [[2024-03-08_chatgpt-and-tone]] — the practice of crafting prompts to elicit desired AI outputs; tone specification is a key technique.
- [[2024-05-24_careful-prompts]] — Establishes systematic approaches to prompt writing including the CARE framework, few-shot prompting, and chain-of-thought techniques; effective prompts include context, specific asks, constraints, and examples, with the order and completeness of information affecting output quality.
- [[2024-08-02_prompt-controls-genai]] — explores how UI design and user guidance can help users formulate better prompts and overcome articulation barriers.
- [[2025-06-06_facilitating-ai-workshops]] — the collaborative refinement of AI prompts to improve outputs, a process requiring adequate time and group discussion.
- [[2025-06-27_designing-use-case-prompt-suggestions]] — creating effective examples and suggestions that guide users toward productive AI interactions.
- [[2025-08-26_392_Artifact_le_meilleur_outil_de_micro-prototypage_IA_pour_designers_&_PMs]]
- [[2026-06-12_context-architecture]] — Prompt design is evolving into context design; clear structure, labeling aligned with user language, and strategic prioritization matter as much as content.
