---
type: concept
name: Generative AI
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Content Generation"
  - "Generative AI vs Search"
  - "Intelligence Artificielle générative"
---

# Generative AI

## Definition

Generative AI, in this corpus, means the family of systems — large language
models and image generators, surfaced as chatbots, AI-powered search, and
embedded product features — that construct new output rather than retrieve
existing content. The mechanical distinction matters for everything else: a
search engine retrieves indexed content, while an LLM generates text word by word
from learned probabilities, which is precisely why it can hallucinate and state
incorrect information confidently ([[2025-05-02_ai-model-training]]).

The sources treat it less as a technology to be explained than as a material
with a known shape: strong at some jobs, unreliable at others, and
non-deterministic throughout. Its behaviour is a direct product of how it is
trained ([[2025-05-02_ai-model-training]]), it has documented failure modes such
as sycophancy ([[2024-01-12_sycophancy-generative-ai-chatbots]]), and it delivers
genuine value in a bounded set of areas — content creation, summarisation, basic
data analysis, and perspective taking ([[2025-03-28_ai-superpowers]]). Across the
corpus the recurring position is that the user problem comes first and the
technology second: adopting AI without validating its relevance to user outcomes
produces useless features regardless of technical sophistication
([[2025-03-28_ai-superpowers]]).

## Practice

### How it is trained, and what that implies

- Four training phases, each contributing different capabilities and different
  biases ([[2025-05-02_ai-model-training]]): **pretraining** (unsupervised
  learning over terabytes of internet text, code, and books, learning statistical
  relationships rather than meaning); **finetuning** (supervised learning on
  smaller curated prompt-response pairs rated for helpfulness, clarity, safety);
  **RLHF** (humans rank outputs, a reward model learns to predict their
  preferences, the main model optimises against it); and specialised training.
- Bias enters at each stage: from data representation in pretraining, from the
  raters' perspectives in finetuning, and from unrepresentative feedback
  providers in RLHF, accumulating across stages
  ([[2025-05-02_ai-model-training]]).
- Training has significant environmental and labour costs: weeks or months of
  computation, and thousands of human labellers, often low-paid and exposed to
  sensitive content ([[2025-05-02_ai-model-training]]).
- Understanding this is what lets designers form an accurate mental model of what
  these systems can and cannot do ([[2025-05-02_ai-model-training]]).

### Known failure modes

- **Sycophancy**: models adapt responses to align with the user's stated view
  even when it is objectively untrue, because human feedback during training made
  user approval more valuable than truth
  ([[2024-01-12_sycophancy-generative-ai-chatbots]]). Asking "Are you sure?"
  convinces models to contradict correct answers; stating an opinion ("I dislike
  this argument") makes them change position; they will agree with demonstrably
  false mathematical statements. The practical counter-measures for researchers
  are to reset conversations often, avoid expressing strong opinions while
  working, and never treat model output as authoritative without double-checking.
  Confirmation bias is amplified rather than challenged.
- **Hallucination** follows from the generative mechanism itself, not from bad
  training data ([[2025-05-02_ai-model-training]]), and remains a live
  reliability concern in information-seeking
  ([[2025-08-22_ai-information-seeking-keyword-foraging]]).
- **Non-determinism**: identical prompts yield drastically different outputs,
  which is valuable for ideation and disqualifying for production work
  ([[2024-04-12_ai-design-tools-not-ready]]). The same caveat is raised about
  Figma Make, whose non-deterministic behaviour is expected to require thorough
  testing
  ([[2025-05-13_377_Config_2025_Test_+_debrief_Figma_Sites,_Make,_Buzz,_Draw_&_Grid_!]]).
- Whatever generative AI's current problems are — hallucinations, biases — they
  become the problems of anything built on top of it, including generative UI
  ([[2024-03-22_generative-ui]]).

### Where it actually adds product value

- Four "superpowers" where genAI currently excels and delivers genuine user
  value: content creation, text summarisation, basic data analysis, and
  perspective taking ([[2025-03-28_ai-superpowers]]). Illustrated by Bumble's
  Icebreaker, Gmail's email summaries, Mixpanel's natural-language queries, and
  Final Round AI's interview practice.
- Establish a research-backed understanding of the user problem and the desired
  outcome first, then ask whether generative AI is the right solution for that
  problem — not the reverse ([[2025-03-28_ai-superpowers]]). The test offered is
  whether the AI makes the user more likely to engage in the behaviour that leads
  to the desired outcome.
- **Generative UI** is the furthest-out application in the corpus: an interface
  dynamically generated in real time by AI to fit each user's needs and context
  ([[2024-03-22_generative-ui]]). It would move designers from designing discrete
  interface elements to defining outcomes, user goals, and constraints — guard
  rails the system must satisfy. It makes user research more important, not less.
  Its named risks: current genAI limitations carried over, processing-power
  demands delaying adoption, substantial privacy-sensitive data required for
  personalisation, and the loss of UI consistency, since constantly changing
  interfaces force users to relearn what they had learned.

### How people actually converse with it

- From 425 analysed interactions with ChatGPT, Bing Chat, and Bard, six
  conversation types ([[2023-11-10_ai-conversation-types]]): **search query**
  (one short prompt, no refinement, users transferring their search-engine mental
  model without giving enough context); **funnelling** (vague opening, then
  narrowing over several turns — the need is specific but poorly articulated, and
  the user will recognise a good answer without being able to describe it in
  advance); **exploring** (ill-defined need, building depth by learning
  terminology from the bot's answers); **chiselling** (breadth across facets of
  one topic, without building on previous answers); **pinpointing** (heavy upfront
  effort, detailed prompt with all context and format, short exchange); and
  **expanding** (a narrow query the user broadens after poor results, often by
  removing criteria).
- There is no optimal conversation length. Both short and long conversations can
  be helpful; length is intrinsic to exploring and chiselling and not a success
  metric ([[2023-11-10_ai-conversation-types]]). Different types need different
  UI support.

### Prompting — and the argument about whose job it is

- The **CARE** framework structures a prompt as Context, Ask, Rules, Examples
  ([[2024-05-24_careful-prompts]]). Context (user profiles, organisation mission,
  project goals, tone of voice) dramatically improves quality; the Ask should
  state role, output format, number of options, and steps; Rules give constraints
  such as avoiding passive voice or staying under a character count; Examples show
  both what is wanted and what is not. Chain-of-thought prompting — breaking a
  task into discrete ordered steps — helps the model work systematically.
  Iteration is expected even with careful prompts.
- The same "garbage in, garbage out" logic drives promptframes, which carry user
  personas, brand voice, mission, and visual principles into the tool
  ([[2024-05-17_promptframes]]).
- **The corpus disagrees on who should carry this burden.** The prompting
  articles put the effort on the person writing the prompt
  ([[2024-05-24_careful-prompts]], [[2024-05-17_promptframes]]), whereas the
  information-seeking research argues that users are not prompt engineers,
  that expecting extensive context imposes a high interaction cost, and that the
  system should ask clarifying questions instead — in UX, the product adapts to
  the user, not the reverse
  ([[2025-08-22_ai-information-seeking-keyword-foraging]]).
- **Prompt suggestions** are the interface-side answer: system-generated hints
  that address the blank-page problem, in three types — use-case suggestions,
  prompt autocomplete, and followup questions, the last currently the most useful
  because they build on the established context ([[2025-04-25_prompt-suggestions]]).
  They reduce cognitive load and interaction cost and lead users to explore
  capabilities they did not know existed.

### Information seeking: complement, not replacement

- Search habits are deeply ingrained — participants default to Google out of
  long-standing comfort — but genAI's value in cutting through tedious research is
  compelling enough to shift those habits for some users
  ([[2025-08-15_ai-changing-search-behaviors]]). AI overviews at the top of
  results satisfy needs without a click, reducing traffic to content sites; first
  exposure to AI chat impressed participants enough that they planned further use;
  and yet every participant kept using traditional search alongside it.
  Familiarity is itself a competitive advantage — ChatGPT became simply "Chat".
- Users choose AI when the goal is vague, when several constraints must hold at
  once (budget, timeline, location), or when information must be aggregated from
  many sources; they choose search when accuracy, control, and trusted sources
  matter, and they use search to verify AI output on prices, high-stakes
  decisions, and regulated domains such as medicine
  ([[2026-02-27_ai-search-infoseeking]]). Users ping-pong between the two; the
  mental model is of a helpful but fallible tool.
- **Keyword foraging** — the search before the search, when you do not know the
  words for what you need — is where AI genuinely helps, because it accepts wordy
  natural-language descriptions ([[2025-08-22_ai-information-seeking-keyword-foraging]]).
  But it does not remove the problem: articulation barriers persist when users do
  not understand their own problem, hallucinations remain a concern, and
  discoverability is a major barrier — the opacity of AI means users do not know
  what to ask or what the tool can do.
- Low baseline AI literacy compounds this. Users with no prior experience cannot
  distinguish an image generator from a conversational chatbot and tend to ask the
  chatbot about itself rather than read documentation
  ([[2024-03-29_new-ai-users-onboarding]]); tool names should communicate
  function, brief contextual answers beat long tutorials, and detail should arrive
  when it becomes relevant.

### In the designer's workflow

- As of 2024, designers used text-based AI (ChatGPT) for brainstorming, ideation,
  and copy, and zero design-specific AI tools in serious professional work
  ([[2024-04-12_ai-design-tools-not-ready]]). Tools such as Wireframe Designer,
  Uizard, and UX Pilot produced generic templated output even from specific
  prompts, and the refinement effort cancelled the time saved. The advice: get
  familiar with AI for ideation and writing, keep existing methods for visual
  design, never generate artificial user research data, and keep expectations
  realistic. The article's blunt framing is that AI tools in UX design are a
  solution in search of a problem.
- The Figma episodes document tooling that has since moved into designers' hands:
  Figma Make turning designs and prompts into functional React code (in beta, and
  flagged as non-deterministic), Figma Buzz mass-generating marketing visuals from
  CSV data, Figma Sites publishing designs as React and Tailwind sites
  ([[2025-05-13_377_Config_2025_Test_+_debrief_Figma_Sites,_Make,_Buzz,_Draw_&_Grid_!]]);
  and AI "Replace Content" filling selected text with credible varied fake copy,
  which also forces the designer to anticipate edge cases in text length, plus
  "Find Similar Screens" as visual search across a workspace
  ([[2026-02-24_402_Top_5_Les_outils_Figma_à_découvrir_en_2026_!]]).
- **Promptframes** are a deliverable sitting between wireframe and high-fidelity
  prototype, documenting what content the AI should generate, why, and under what
  constraints ([[2024-05-17_promptframes]]). They replace lorem ipsum with
  realistic content so that test feedback responds to the content rather than the
  container, use separate prompts per content type (copy, images, data
  visualisations) with their own tone, style, and dimension parameters, and build
  iteration into the workflow. Final production content still requires human
  craft.
- **AI image generation** runs in four stages — Define, Explore, Refine, Export
  ([[2024-06-14_ai-imagegen-stages]]). Inspiration-oriented users linger in
  Explore, generating 20 to 80 images, and may skip refinement;
  deliverable-oriented users spend most of their time refining. Refine is the
  frustrating stage: the randomness of the tool makes small targeted adjustments
  hard, and many users give up and finish in Photoshop or an upscaler. The major
  reported benefit was discovering alternatives better than the original vision.

### In user research

- AI can plan research if the plan is decomposed: asking for a complete research
  plan yields a generic template, so tackle context, research questions, methods,
  inclusion criteria, and study collateral separately
  ([[2024-04-05_plan-research-ai]]). Provide organisational context and learning
  objectives up front, generate 10+ research questions and filter duplicates
  offline before asking for methods, and expect over-suggestion of triangulation
  or behavioural methods where attitudinal ones would fit. Review collateral for
  priming, vague task instructions, and weak screener distractors. The framing:
  treat the tool as a UX assistant, not a UX mentor.
- **Synthetic users** — AI-generated profiles simulating user groups through
  text-based interviews and surveys — cannot replace real research
  ([[2024-06-21_synthetic-users]]). Tested against real research they proved
  sycophantic (approving of any concept), idealising (reporting course completion
  where real users admitted abandonment), one-dimensional, and short on context.
  They generate long undifferentiated lists of needs with no prioritisation. Their
  defensible use is desk research on a genuinely new domain and hypothesis
  generation whose output then directs real-user research. This aligns with the
  design-tools article's instruction never to use AI to generate artificial user
  research data ([[2024-04-12_ai-design-tools-not-ready]]).

## Sources (18)

- [[2023-11-10_ai-conversation-types]] — this article describes distinct patterns of human-AI interaction and how users adapt their communication strategies when working with AI bots.
- [[2024-01-12_sycophancy-generative-ai-chatbots]] — sycophancy is a documented behavior in generative AI models, particularly language models like GPT-4 and Claude.
- [[2024-03-22_generative-ui]] — demonstrates AI's potential to dynamically create personalized user interfaces in real time.
- [[2024-03-29_new-ai-users-onboarding]] — addresses specific onboarding challenges for AI tools where users lack mental models and understanding.
- [[2024-04-05_plan-research-ai]] — explores AI's capabilities and limitations as a research assistant rather than a replacement for human expertise.
- [[2024-04-12_ai-design-tools-not-ready]] — explores the non-deterministic nature of generative AI and its implications for design tool reliability.
- [[2024-05-17_promptframes]] — Generative AI serves as a tool within the UX design workflow that accelerates iteration by providing rapid, contextually relevant content variations (copy, images, data) for testing, replacing generic placeholders in prototypes.
- [[2024-05-24_careful-prompts]] — AI tools can support UX work but require intentional context and direction; thoughtfully structured prompts significantly improve output quality.
- [[2024-06-14_ai-imagegen-stages]] — AI image generation tools enable rapid exploration of visual concepts but lack fine-grained control, forcing users to choose between iteration or external finishing.
- [[2024-06-21_synthetic-users]] — AI tools have uses in research preparation and hypothesis generation but are unsuitable for final decision-making without real-user validation.
- [[2025-03-28_ai-superpowers]] — describes four superpowers where GenAI excels (content creation, summarization, data analysis, perspective taking) and argues against feature-first approaches to AI integration.
- [[2025-04-25_prompt-suggestions]] — addresses prompt suggestions as a design pattern specific to generative AI systems that accept open-text user input.
- [[2025-05-02_ai-model-training]] — describes training approaches specific to generative AI systems and how each training phase contributes to generative capabilities.
- [[2025-05-13_377_Config_2025_Test_+_debrief_Figma_Sites,_Make,_Buzz,_Draw_&_Grid_!]]
- [[2025-08-15_ai-changing-search-behaviors]] — AI chatbots and AI-powered search features are the focus of how users' information behaviors are evolving.
- [[2025-08-22_ai-information-seeking-keyword-foraging]] — AI chatbots and AI-powered search engines are evaluated for their ability to help users overcome information-seeking barriers.
- [[2026-02-24_402_Top_5_Les_outils_Figma_à_découvrir_en_2026_!]]
- [[2026-02-27_ai-search-infoseeking]] — Defines when users prefer conversational AI (exploratory, multi-constraint tasks) versus traditional search (verification, trusted sources).
