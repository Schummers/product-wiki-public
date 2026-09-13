---
type: concept
name: AI Product Design
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "AI Feature Design"
  - "AI Product Design Considerations"
  - "AI Product Design Patterns"
  - "AI Product Strategy"
---

# AI Product Design

## Definition

AI product design is the work of building interfaces and experiences that
deliver AI capabilities to users. [[2026-06-05_design-jobs-ai-created]] isolates
it as one of four distinct orientations that have emerged around AI — designing
*with* AI as a tool, designing AI products, designing *for* AI agents, and
designing the AI itself — and splits it further into AI-native products, which
must teach an entirely new paradigm, and AI features added to existing products,
which must integrate into established patterns. Both, it notes, challenge users'
mental models and require research.

The corpus is strikingly consistent about the discipline's founding claim: AI
does not suspend user-centered design. [[2024-11-08_ai-user-value]] states that
whether or not they are AI-driven, products, features and services must solve
users' problems, and that generative AI is not magic — it does not remove the
need for research or a deep understanding of users' needs and mental models.
[[2025-10-21_designing-ai-study-guide]] puts the same point bluntly: adding AI
does not magically create value. What the technology adds is a specific set of
new design problems — probabilistic output that can be confidently wrong,
users who do not know what to ask, features that are invisible or
incomprehensible, and organizational pressure to ship AI regardless of fit — and
this concept is the accumulated guidance on those problems.

## Practice

### Start from the user problem, not from the technology

- [[2025-07-04_powered-by-ai-is-not-a-value-proposition]] argues that "powered by
  AI" cannot function as a value proposition because it names a technology rather
  than a user benefit, and leaves users wholly responsible for working out how the
  tool fits their workflow. Strong propositions state what the user achieves
  ("accelerate your research", "never miss a bill"); the technology is chosen
  afterwards, once the value is established. Its warning about the failure mode is
  concrete: when "it has AI" becomes the guiding principle, the only remaining
  design direction is to make the experience as AI as possible, which tends to
  produce broad-scope chatbots with high adoption barriers. The source also notes
  that AI presence can itself trigger fear — users are aware of LLM drawbacks, so
  the label can lower conversion unless the specific anxieties are addressed.
- [[2024-11-08_ai-user-value]] makes the historical case, drawing a line from
  Flash plugins to LinkedIn's AI-generated questions and Instagram's AI chat
  placed in front of search — its verdict being that the only thing worse than an
  unnecessary AI chat is one that blocks a useful feature. Against these it sets
  Adobe Lightroom's AI object removal, a case where AI makes a previously
  difficult, time-consuming task accessible. When communicating such features, it
  advises leading with the benefit to the user's life and following with the
  technical specifics, not the reverse.
- [[2025-10-21_designing-ai-study-guide]] organizes its first section around the
  same question — does AI add value here? — and asks teams to name the concrete
  gain (better accuracy, faster synthesis, a genuinely new capability). It offers
  a shorthand for where AI tends to earn its place: content creation,
  summarization, data analysis and perspective-taking, which it calls AI's four
  superpowers, and observes that successful integrations usually lean on one of
  them rather than trying to replace a whole workflow. It also insists on the
  willingness to say the emperor has no clothes when a feature is not making a
  valuable difference.
- [[2025-02-28_scope-ai-features]] supplies the question list before any scope
  decision: what specific problem are we solving, how does it serve business
  goals, is AI genuinely the best means, and how clean is our data.

### Scope narrowly

[[2025-02-28_scope-ai-features]] treats scope — how broad or narrow the
capabilities are — as the decision that most shapes usability and adoption.
Broad-scope systems such as ChatGPT and Perplexity accept anything and produce
anything, which forces new users to imagine what is possible and to articulate it
unaided, so they spend their time exploring rather than accomplishing. Narrow
features such as Spotify's playlist generator or Photoshop's generative fill
constrain inputs and outputs, and tested better with new users, who understood
them, wrote appropriate prompts, iterated more successfully and reported more
positively. The source frames this as the flexibility-usability tradeoff applied
to AI, with a paradox worth noting: a narrow scope actually permits *richer* UI
controls — prompt wizards, helpful defaults, structured outputs, as in
TripAdvisor's trip planner — because the design knows what the user is trying to
do. [[2025-10-21_designing-ai-study-guide]] repeats the finding independently:
narrowly scoped AI features are easier to understand and see better adoption.

[[2025-02-21_ai-integration-condens]] arrives at the same rule from
implementation experience, listing "scope tasks narrowly and specifically" among
the company-wide guidelines it settled on.

### Design for probabilistic, sometimes wrong output

[[2025-02-07_ai-hallucinations]] is the corpus's dedicated treatment.
Hallucinations are not bugs but artifacts of how LLMs work: output is generated
by predicting statistically likely continuations rather than retrieving facts, so
the system cannot distinguish a correct answer from an incorrect one and
eliminating hallucinations may be infeasible with current technology. Training
data compounds the risk, since models absorb falsehoods, opinions, sarcasm and
satire and can treat them as authoritative. Engineering measures (lower
temperature, retrieval augmentation) are partial, which leaves design with real
work to do:

- Drop generic, always-on disclaimers — the article compares them to ubiquitous
  California Proposition 65 labels, which desensitize rather than warn — and show
  contextually relevant warnings only when uncertainty is actually high.
- Express uncertainty in the first person: research showed users respond better
  to "I'm not completely sure, but…" than to an impersonal "It's not clear",
  with first-person phrasing raising appropriate skepticism.
- Display confidence scores where available, especially in high-stakes domains
  such as healthcare; surface inconsistencies between multiple generated
  responses, or present multiple AI perspectives in a debate format, so users can
  spot likely hallucinations.
- Present sources as drillable links or reference lists to encourage
  fact-checking — while noting that reference links can create a false-halo
  effect.

Its summary principle is that establishing trust requires acknowledging AI's
limits and fallibility. [[2025-10-21_designing-ai-study-guide]] converges on the
same design responses — source citation for trust, transparency about limitations
— and adds formatting long responses for web readability.

### Keep humans in the loop and AI out of the critical path

[[2025-02-21_ai-integration-condens]] reports the operating guidelines a research
tool company settled on after the hype receded, having judged marketing claims
like "high-quality insights in seconds" or "eliminate bias" overstated:

- Three evaluation questions before applying AI to a task — does the AI have the
  necessary context, does the task fit within the model's technical constraints,
  and can the output be verified and modified?
- Context is the usual binding constraint: tasks needing little of it, such as
  transcription and translation, do well, while contextual work like UX analysis
  needs industry, company or study-specific knowledge that a prompt cannot carry.
- Technical limits matter concretely: GPT-4o's 128k-token window corresponds to
  roughly ten hours of transcribed interviews, and exceeding it forces the model
  to preselect data, which can introduce bias and degrade results.
- Prefer small-chunk summarization, semantic search and quote clustering — AI
  extracting and organizing small verifiable units — over complex ranking or
  whole-project analysis that requires interpretation.
- Decompose complex tasks into smaller verifiable steps with human validation, so
  errors are caught incrementally instead of accumulating through an end-to-end
  automation.
- Make the core workflow work without AI, treating AI as an enhancement to
  specific steps rather than the foundation of critical functionality.

The source is honest about the price of this stance: it lost a customer to a
competitor that was integrating AI more aggressively.

### Respect existing mental models, and expect them to move slowly

- [[2024-11-08_ai-user-value]] frames the choice as maintaining existing
  interaction patterns and mental models rather than forcing users into a new
  paradigm, contrasting Lightroom (which fits the model users already have)
  with Instagram's AI chat (which violates it).
- [[2025-02-28_scope-ai-features]] observes that ingrained models — search-bar
  expectations, for instance — slow adoption, that younger users are adapting to
  AI-in-search faster but broad change takes time, and that the practical stance
  is to design for the mental models users hold today while priming the ones they
  will hold later.
- [[2026-06-05_design-jobs-ai-created]] separates the two cases explicitly:
  AI-native products have to teach a new paradigm, while AI features inside
  existing products have to integrate into established patterns. Both challenge
  mental models and both require research.

### Do not assume your users know what you know

[[2025-03-07_ai-adoption-pew]] supplies the baseline. Pew survey data two years
after ChatGPT's release found 81% of US workers reporting little or no AI use at
work, 55% rarely or never using AI chatbots and 29% never having heard of the
popular products; adoption concentrated in data processing, IT, finance and
insurance, with only 9% of non-users citing an employer restriction, which the
article reads as adoption being driven by perceived value rather than by
barriers. Usage skews young (73% of adopters under 50, 18–29-year-olds the most
frequent chatbot users) and simple — 57% information seeking, 52% editing, 47%
drafting, against 35% ideation, 27% analysis or coding, 21% media creation. Rated
helpfulness rises with frequency, from 25% among infrequent users to 54% among at
least monthly users, which the source attributes to mental-model shifts and
competence taking time. Its design consequences: expect low baseline familiarity,
provide onboarding that explains what the AI can do for the user's actual
workflow, guard against false-consensus bias (designers work in tech and
socialize with tech people, so "you are not the user" applies with extra force
here), and test inclusively across ages and levels of technical expertise.

### Make features discoverable and help users articulate what they want

[[2025-10-21_designing-ai-study-guide]] names discoverability as a major
remaining barrier: a valuable feature has no impact if users never notice it, so
both discovery and understanding must be designed. It pairs this with prompt
assistance, since users often do not know what the AI can do or what to ask;
prompt suggestions contextualized to the task help them explore and set realistic
expectations. It also gives per-feature guidance — summaries should be specific
and transparent, prompt suggestions contextual and personalized, chat interfaces
formatted and concise, controls educational and exploratory. This complements
[[2025-02-28_scope-ai-features]]'s point that a broad system's vast capabilities
do not matter if users do not know they exist.

### One bad experience is expensive

[[2024-11-08_ai-user-value]] warns that a single negative encounter with an AI
feature can stop a user trying them again, so features must be genuinely ready
before launch. [[2025-10-21_designing-ai-study-guide]] makes the mirror-image
demand of teams: give AI a real chance, but be willing to call out a feature that
is not making a valuable difference.

### Where the design work is going

[[2026-06-05_design-jobs-ai-created]] situates AI product design among the other
three orientations and observes that most designers today work either on
designing with AI or on designing AI products, while very few design for AI
agents (structuring data, content and interactions so agents can parse and act on
them — infrastructure that is largely ignored yet shapes the end-user experience)
or design the AI itself (shaping model behavior, evaluation criteria and
principles, including what the model should do, what it should refuse, and how it
weighs competing instructions). Demand for the two underserved orientations is
growing faster than supply, and the source argues for depth in one direction over
staying broadly AI-adjacent, while warning the window will not stay open long.

## Sources (8)

- [[2024-11-08_ai-user-value]] — The article provides guidance on designing AI features thoughtfully, emphasizing that designers should maintain existing interaction patterns and mental models rather than forcing users to adopt new paradigms.
- [[2025-02-07_ai-hallucinations]] — Provides evidence-based design patterns for mitigating hallucination impact: uncertainty language, confidence indicators, multi-response consistency checks, source displays, and verification-encouraging layouts.
- [[2025-02-21_ai-integration-condens]] — Outlines a cautious-yet-optimistic approach to AI integration that resists hype, establishes clear design guidelines, and prioritizes evidence over ambitious marketing claims.
- [[2025-02-28_scope-ai-features]] — Examines how scope decisions—from broad (ChatGPT) to narrow (Spotify playlists)—fundamentally shape interface design, user guidance, and input/output structures.
- [[2025-03-07_ai-adoption-pew]] — Emphasizes that most users lack AI familiarity, use simple AI features, and need onboarding; warns designers against false-consensus bias and recommends inclusive testing across age and technical-expertise levels.
- [[2025-07-04_powered-by-ai-is-not-a-value-proposition]] — approaching AI integration by starting with user needs and selecting AI as a tool when appropriate, not beginning with AI as a given.
- [[2025-10-21_designing-ai-study-guide]] — Provides strategic framework for deciding whether AI adds value; emphasizes solving real user problems rather than chasing technology; documents design considerations for particular feature types.
- [[2026-06-05_design-jobs-ai-created]] — Designing AI products requires different approaches for AI-native products (teaching new paradigms) versus AI features in existing products (integrating into existing patterns); both challenge mental models and require research.
