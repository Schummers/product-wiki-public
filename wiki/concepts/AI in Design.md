---
type: concept
name: AI in Design
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "AI Design Tools"
  - "AI Tools"
  - "AI and Design"
  - "AI in Design Tools"
  - "AI in UX"
  - "Intelligence Artificielle en Design"
  - "UX Design for AI"
---

# AI in Design

## Definition

AI in design covers two intertwined questions the sources keep returning to:
what generative AI can actually do *for* design work, and how design work must
change to make AI-powered products usable. On the first question, the sources
converge on a deflationary answer. Between April 2024 and May 2025 NN/g ran the
same assessment twice and found design-specific AI tools improved only
marginally: designers use text-based AI heavily for brainstorming and copy, but
adopt almost none of the design-specific tools in serious professional work
([[2024-04-12_ai-design-tools-not-ready]], [[2025-05-09_ai-design-tools-update-2]]).
A practitioner review of tools in daily use reaches the same conclusion from the
other direction: AI accelerates particular phases, while research, conception
and thinking remain untouched ([[2025-09-09_394_Top_5_outils_IA_Product_Design_&_UXUI_-_Septembre_2025]]).
What AI does displace is technical execution, and the sources treat that as a
shift in what a designer is paid for rather than a threat to the job:
discernment, taste and problem framing become the differentiator once anyone can
produce an artefact ([[2024-05-10_taste-vs-technical-skills-ai]],
[[2025-05-09_ux-job-with-ai]], [[2025-03-28_return-ux-generalist]]).

On the second question, AI is a design material with its own failure modes.
Because LLMs generate text word by word from learned probabilities rather than
retrieving indexed content, they hallucinate confidently, and their behaviour
carries bias from every training stage ([[2025-05-02_ai-model-training]]). Users
nonetheless trust their output largely without checking it
([[2023-09-24_generative-ai-diary]]). The quality difference between AI products
therefore comes less from the model than from the interface and the aggregation
around it: three bots sharing comparable underlying models scored very
differently on helpfulness and trustworthiness
([[2023-10-01_ai-bot-comparison]]). The most recent sources push this further
still — designing for AI increasingly means designing the *context* the model
sees, and evaluating agentic systems on whether they actually complete tasks
([[2026-07-24_ux-context-design]], [[2026-04-03_definition-ai-agent]]).

## Practice

### Where AI currently earns its place in design work

- Narrow, repetitive tasks are the reliable win: renaming layers, rewriting
  copy, finding assets, generating colour palettes, producing placeholder
  imagery. These are genuinely adopted and save time without extensive guidance
  ([[2025-05-09_ai-design-tools-update-2]]).
- Text-based general-purpose AI is used for brainstorming, ideation and copy —
  including filling a skill gap, such as a designer producing copy without a
  copywriter — which the sources distinguish sharply from automating design
  itself ([[2024-04-12_ai-design-tools-not-ready]]).
- Generation tools are strongest for breadth, not precision: users generate 20
  to 80 images to find a promising direction, and report that discovering
  alternatives better than their original vision is the main benefit
  ([[2024-06-14_ai-imagegen-stages]]).
- Practitioner tool picks follow the same logic — similarity search inside
  Figma, AI prototyping with real data, AI search for benchmarking, semantic
  search over screenshot libraries by user story or job to be done, and custom
  agent platforms — chosen because they answer a need, not because they contain
  AI ([[2025-09-09_394_Top_5_outils_IA_Product_Design_&_UXUI_-_Septembre_2025]]).
- AI also compresses learning: multiple variations to study, contextual
  explanations of principles and immediate feedback let a generalist pick up
  visual design, research methods or IA faster than before
  ([[2025-03-28_return-ux-generalist]]).

### Where it still fails

- Non-determinism cuts both ways: identical prompts produce drastically
  different designs, which is useful for ideation and disqualifying for
  production ([[2024-04-12_ai-design-tools-not-ready]]).
- Broad wireframe and prototype generation produces generic layouts with poor
  information hierarchy, and minor variations rather than meaningful
  alternatives ([[2025-05-09_ai-design-tools-update-2]]).
- Design-system integration is the critical missing piece: prototypes assembled
  from random elements are worthless to teams working from an established system
  ([[2025-05-09_ai-design-tools-update-2]]).
- Prompt-length limits (around 500 characters in the tools reviewed) cannot
  carry enough context for contextual design decisions, and some interfaces
  actively discourage longer prompts through a small text box
  ([[2025-05-09_ai-design-tools-update-2]]).
- Refinement is where users get stuck. Making a small targeted adjustment means
  fighting the tool's randomness, and many users abandon and finish in external
  software instead ([[2024-06-14_ai-imagegen-stages]]).
- The effort to extract a high-quality result can exceed the time saved, which
  is why NN/g called these tools a solution in search of a problem
  ([[2024-04-12_ai-design-tools-not-ready]]).
- Never use AI to generate artificial user research data
  ([[2024-04-12_ai-design-tools-not-ready]]). Related distinctions matter here:
  synthetic users simulate a segment from group-level descriptors, digital twins
  simulate a specific individual from person-specific data
  ([[2026-01-02_ux-quiz]]).

Note a difference of emphasis rather than a contradiction: the 2024 assessment
concluded AI was not shortcutting any step of the design process, while the 2025
follow-up found narrow-scope features that genuinely do
([[2024-04-12_ai-design-tools-not-ready]], [[2025-05-09_ai-design-tools-update-2]]).
Both maintain that no current tool replaces the designer.

### Getting better output: prompting and context

- Structure prompts with CARE — Context (user profiles, mission, project goals,
  tone of voice), Ask (role, output format, number of options, steps), Rules
  (constraints such as length or plain language), Examples of what you do and
  do not want ([[2024-05-24_careful-prompts]], echoed in
  [[2025-12-19_top-videos-2025]]).
- Expect to iterate. Even careful prompts require refining outputs, asking for
  variations, or combining several ([[2024-05-24_careful-prompts]]).
- Treat AI as a first-pass contributor — an "intern" whose output you
  double-check and fact-verify, and to whom you give specific instructions
  ([[2025-12-19_top-videos-2025]]).
- Beyond the individual prompt, curate organisational context. AI produces
  output from what it can see; without your users, domain, standards and
  research findings, it designs the average product
  ([[2026-07-24_ux-context-design]]).
- This reframes the deliverable itself: personas and journey maps were built for
  human empathy, whereas AI needs the underlying reasoning in machine-readable
  form. Google Labs' DESIGN.md is the concrete precedent — exact values for
  colour, type and spacing alongside human-readable guidelines, living next to
  the code and read on every generation. A broader UX.md could add research
  synthesis, interaction standards, a domain glossary, and user and world models
  ([[2026-07-24_ux-context-design]]).
- Context is curated continuously, never handed off: it changes with the product,
  and watching what AI gets wrong is itself an input
  ([[2026-07-24_ux-context-design]]).
- Since product managers and engineers now generate designs before a designer
  sees them, the practical goal is to make sure everything AI generates is
  informed by research and standards, rather than to gatekeep
  ([[2026-07-24_ux-context-design]]).
- Understanding the training stages — pretraining, finetuning, RLHF — helps form
  an accurate mental model of what a design AI can and cannot do, and where its
  bias comes from ([[2025-05-02_ai-model-training]]).

### Designing AI-powered products

- Start from the problem, not the technology. Establish a research-backed
  understanding of the user problem and the desired outcome first, then ask
  whether generative AI is the right solution
  ([[2025-03-28_ai-superpowers]]).
- The four areas where AI reliably adds value are content creation,
  summarisation, basic data analysis and perspective taking — illustrated by
  Bumble's Icebreaker, Gmail summaries, Mixpanel's natural-language queries and
  interview practice tools ([[2025-03-28_ai-superpowers]]).
- Interface and aggregation matter more than the model. Bing Chat scored
  significantly lower than ChatGPT and Bard on helpfulness and trustworthiness
  despite a shared underlying model, because it gave shallow answers and pushed
  users to links instead of synthesising ([[2023-10-01_ai-bot-comparison]]).
- Design for verification. Chatbots collapse the find–evaluate–aggregate loop
  into a single answer, but only 22% of logged conversations included any
  verification; provide sources and citations that make checking cheap
  ([[2023-09-24_generative-ai-diary]]).
- Handle references carefully: poorly curated, broken or irrelevant links damage
  credibility rather than supporting it ([[2023-10-01_ai-bot-comparison]]).
- Preserve conversational context. Bots that forget earlier turns return
  irrelevant answers where users expected continuity
  ([[2023-09-24_generative-ai-diary]]).
- Avoid vague, generic answers. Expectations of AI exceed those of search
  engines precisely because writing a prompt costs more effort
  ([[2023-09-24_generative-ai-diary]]).
- Use prompt suggestions to solve the blank-page problem, in three types:
  use-case suggestions that showcase capability, prompt autocomplete for
  efficiency, and followup questions — the most useful type, because they are
  tailored to what the conversation has already established
  ([[2025-04-25_prompt-suggestions]]). Badly executed followups (too basic, too
  close to the original query, or disappearing after the next response) frustrate
  users instead ([[2023-10-01_ai-bot-comparison]]).
- Multimedia and ads are trade-offs: images and video can break scanning and
  scale poorly on mobile, and ads accepted in product-recommendation queries
  become offensive in research conversations ([[2023-10-01_ai-bot-comparison]]).
- Apply web-writing fundamentals to generated content. Product-embedded AI is
  measurably worse than general-purpose tools at concision, scannable
  formatting, and the inverted pyramid, and it defaults to jargon regardless of
  how basic the question was; finetuning and enforced writing standards are the
  proposed fix ([[2025-04-04_genai-write-for-the-web]]).
- Match response depth to the user's evident expertise, inferring context from
  prompt signals and follow-up questions
  ([[2025-04-04_genai-write-for-the-web]]).
- Build trust by emphasising analytical capability and showing clear,
  task-focused reasoning and limits; entertainment personas and false confidence
  undermine it ([[2026-01-02_ux-quiz]]).
- For agents, hold to a concrete definition — a system that pursues a goal by
  iteratively taking actions, evaluating progress and deciding its own next
  steps — and evaluate usefulness through user research and task-completion
  metrics rather than technical capability. A useful agent understands goals
  reliably, adapts when things fail, and minimises the human review required
  ([[2026-04-03_definition-ai-agent]]).
- Generative UI, which builds personalised interfaces in real time, moves UX
  from static design to dynamic, user-specific interaction and is treated as a
  live topic rather than a settled practice ([[2025-12-19_top-videos-2025]]).

### What this changes for the designer

- AI removes the technical barrier to production, so taste — intentional choices
  orchestrated around a single organising vision, serving both user needs and
  business goals — becomes the differentiator. Technical capability does not
  equal creative ability ([[2024-05-10_taste-vs-technical-skills-ai]]).
- Treat AI as the latest in a long line of tool changes (stopwatch to remote
  testing to AI transcription) and judge it against the mission of building
  better products, not as a job-replacement threat
  ([[2025-05-09_ux-job-with-ai]]).
- The durable human work is framing the problem clearly enough for AI to act on,
  asking the right questions, and judging whether the output is any good
  ([[2025-05-09_ux-job-with-ai]]).
- New technologies create new research methods — mobile produced journey
  mapping; generative UIs and AI interactions will need their own methods,
  validated against established approaches ([[2025-05-09_ux-job-with-ai]]).
- As AI absorbs specialised execution, value shifts back toward generalists who
  orchestrate tools, facilitate, navigate organisations and connect insight to
  strategy. The recommended preparation is a learning mindset, fluency in AI
  collaboration, transferable skills, and expansion into adjacent fields
  ([[2025-03-28_return-ux-generalist]], [[2025-12-19_top-videos-2025]]).
- Keep expectations realistic: rely on existing methods for visual design tasks
  and familiarise yourself with AI for ideation and writing
  ([[2024-04-12_ai-design-tools-not-ready]]). A tool must answer a need — the
  presence of AI is not itself a reason to adopt it
  ([[2025-09-09_394_Top_5_outils_IA_Product_Design_&_UXUI_-_Septembre_2025]],
  [[2025-03-28_ai-superpowers]]).

## Sources (18)

- [[2023-09-24_generative-ai-diary]] — Chatbots provide efficiency gains for information seeking but require verification mechanisms and better handling of context to become fully trustworthy.
- [[2023-10-01_ai-bot-comparison]] — Chatbot quality depends heavily on information aggregation capability and interface design, not just the underlying language model.
- [[2024-04-12_ai-design-tools-not-ready]] — evaluates current state of AI-based tools for UX design and identifies significant gaps between marketing promises and real capabilities.
- [[2024-05-10_taste-vs-technical-skills-ai]] — AI tools democratize technical production but do not replace the strategic and aesthetic decision-making that distinguishes professional design work.
- [[2024-05-24_careful-prompts]] — generative AI can accelerate UX work but is most effective when integrated into structured workflows with clear requirements and iterative refinement.
- [[2024-06-14_ai-imagegen-stages]] — AI generation tools are most powerful for exploring many directions quickly; they are less effective for precise control and fine adjustments.
- [[2025-03-28_ai-superpowers]] — provides concrete examples of how AI features enhance product value when embedded in workflows addressing real user friction (Bumble, Gmail, Mixpanel).
- [[2025-03-28_return-ux-generalist]] — explains how AI compresses skill-development timelines by generating multiple design variations, providing contextual explanations of principles, and offering immediate feedback on design choices.
- [[2025-04-04_genai-write-for-the-web]] — identifies how product-specific AI currently violates web-writing fundamentals compared to general-purpose AI and how finetuning can address this gap.
- [[2025-04-25_prompt-suggestions]] — describes prompt suggestions as a UX pattern for guiding user interaction with generative AI systems and supporting effective system use.
- [[2025-05-02_ai-model-training]] — addresses how design-specific training approaches (finetuning on design files, RLHF for design feedback) affect design AI system capabilities and limitations.
- [[2025-05-09_ai-design-tools-update-2]] — evaluates current capabilities and limitations of AI-powered design tools based on real-world practitioner adoption and use cases.
- [[2025-05-09_ux-job-with-ai]] — describes AI as a tool to be evaluated against building-better-products mission rather than as a job-replacement threat.
- [[2025-09-09_394_Top_5_outils_IA_Product_Design_&_UXUI_-_Septembre_2025]]
- [[2025-12-19_top-videos-2025]] — AI appears across multiple key 2025 videos, from synthetic users to prompt design to generated interfaces, showing pervasive adoption in practice.
- [[2026-01-02_ux-quiz]] — AI interviewers, synthetic users, and AI trust all emerge as critical concerns for UX professionals working with AI-powered systems.
- [[2026-04-03_definition-ai-agent]] — Emphasizes that usefulness must be evaluated through user research and task-completion metrics, not just technical capability.
- [[2026-07-24_ux-context-design]] — requires moving from creating human-readable deliverables to creating machine-readable context that guides AI generation across the organization.
