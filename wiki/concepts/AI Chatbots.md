---
type: concept
name: AI Chatbots
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Agent Conversationnel"
  - "Chatbot"
  - "Conversational Agent"
  - "Conversational Interface"
  - "Conversational Interfaces"
  - "Conversational UI"
  - "Interface Conversationnelle - Chatbot"
  - "Interface Conversationnelle / Chatbot"
---

# AI Chatbots

## Definition

A chatbot is defined in this corpus as a domain-specific, text-based
conversational interface that supports users with a limited set of tasks; it
requires natural-language processing and intelligent interpretation but not
necessarily voice output or agency, and it is described as "the poor relative of
the intelligent assistant" [[2018-11-25_chatbots]]. The category has since
widened to cover universal generative-AI chatbots trained on broad knowledge
(ChatGPT and its peers) and product- or site-specific chatbots embedded in an
app or website with narrower scope [[2024-03-01_ai-chat-not-the-answer]], with
voice assistants forming an adjacent branch that shares the natural-language
interface but adds the constraints of an audio-only channel
[[2017-11-12_voice-first]] [[2018-08-05_voice-assistant-attitudes]].

The dominant argument across the corpus is that conversation is one interface
option among many, not an intrinsically superior one. Chat looks simple on the
surface while creating a new set of usability problems
[[2023-09-24_accordion-editing-apple-picking]], and AI does not have to be
anthropomorphized, conversational, or even visible to add value
[[2024-03-01_ai-chat-not-the-answer]]. The Parlons Design sources make the same
point in stronger terms: AI is a technology, not a use case, and replacing an
interface with a chatbot in order to say the product "has AI" is the wrong
starting move [[2025-09-30_397_Pourquoi_l_IA_n_a_pas_(encore)_révolutionné_l_UX]]
[[2024-08-13_341_Dust_🇫🇷,_mieux_que_ChatGPT_Analyse_design_de_l_outil_IA_des_product_people...]].
Site-specific chatbots in particular are described as still earning users'
trust, with every interaction either building or eroding it
[[2026-07-10_dimensions-of-ai-chatbots]].

## Practice

### Decide whether chat is the right interface at all

Before building one, validate three criteria: does it solve a real, widespread
user need; does it align with product strategy; and does it scale with advancing
technology. Customer support, where speed matters, is offered as a good use
case; LinkedIn's AI-generated follow-up suggestions are offered as an example of
adding chat without a real problem to solve. Alternatives — personalization,
predictive analytics, strategic automation, email automation — often address the
need better [[2024-03-01_ai-chat-not-the-answer]].

The French-language sources reach the same conclusion from a designer's
practice angle. Open conversation is called a trap: without framing, a
discussion goes in every direction at once. The better pattern illustrated by
Dust is a pre-configured, specialized assistant connected to internal knowledge
bases (Notion, Slack), where several specialized agents can be invoked in one
conversation, and where an expert configures an agent once and shares it with
the team so that uneven prompting skill stops determining output quality. The
upfront configuration is deliberate friction that pays back daily by removing
the need to rewrite long prompts
[[2024-08-13_341_Dust_🇫🇷,_mieux_que_ChatGPT_Analyse_design_de_l_outil_IA_des_product_people...]].
The complementary episode argues designers must experiment with the models
themselves — otherwise they will reproduce existing patterns rather than
innovate — and cites Jira explaining acronyms proactively, Granola mixing
written and audio notes, and Airtable generating formulas from a prompt as
integrations that target a specific friction without imposing a full chat
interface. Using a chat to draft an email, it notes, can be more laborious than
writing it yourself
[[2025-09-30_397_Pourquoi_l_IA_n_a_pas_(encore)_révolutionné_l_UX]].

### Getting a site chatbot noticed and understood

A study of 9 users across 8 site chatbots found most participants did not
notice the feature, rarely used it, or could not say what it offered beyond
tools they already had. Failure modes: icons that are small, unlabelled, or lost
in a busy background; skepticism carried over from bad chatbots of years past;
vague messaging about capabilities, which matters because users will not
experiment to discover value; capabilities misaligned with why people visit the
site (recipes and DIY help on a site people come to in order to buy); and
chatbots that are simply slower than the search, filters and navigation users
have already mastered. Where they do add value is context-specific: answering
product-page questions, clarifying complex information, and handling
personalized, multivariate questions [[2026-03-20_site-ai-chatbot]].

The corresponding guidelines are concrete [[2026-04-24_ai-chatbots-design-guidelines]]:

- Consolidate AI and human chat into a single entry point; multiple chatbots
  confuse users about which to use.
- Keep the chatbot persistent across pages; one that disappears is abandoned.
- Say what it can do in the opening message, not "ask me anything".
- Tailor suggested prompts to the current page so it is visibly aware of what
  the user is looking at.
- Present suggested questions as clickable buttons rather than text.
- Include product images, diagrams and visuals in recommendations.
- Use progressive disclosure (expand/collapse) instead of appending to the chat.
- Do not autoscroll; keep the scroll position at the start of the message.
- Allow window resizing for rich content such as maps and comparisons.
- Enable saving and sharing of recipes, guides and comparisons.
- Consider voice input.

### Write like a search result, not like a conversation

Users treat site chatbots as search bars: they type minimal, often incomplete
queries with typos, skip greetings and politeness, and get terser as trust
builds. They want answers, not a relationship. The guidance is to cut
pleasantries and sycophancy ("great question"), keep sentences short and
paragraphs to two or three sentences, use lists, bold, headers and white space,
and follow a truncated-pyramid rule: essential answer first, follow-up prompts
so detail can be pulled on demand. Specific beats generic — give a range or
estimate rather than a long answer covering every scenario — and when the bot
cannot help it should say so plainly, without padding or irrelevant advice
[[2026-04-17_less-chat-more-answer]]. This is consistent with the finding that
LLM filler such as "Alright, let's break it down" adds noise without value
[[2026-01-09_humanizing-ai]].

### Five qualities to design for

A framework for site-specific chatbots names five qualities
[[2026-07-10_dimensions-of-ai-chatbots]]:

1. **Handoff willingness** — never gatekeep. Users do not consider bots
   equivalent to human agents, so honour a request for a human immediately, and
   escalate proactively on failure or visible frustration.
2. **Flexibility** — handle questions adjacent to the core domain (dietary
   substitutions for a meal-kit service) rather than acting as an expanded FAQ;
   when a question is genuinely out of scope, acknowledge the limit and redirect
   to what is possible.
3. **Proactivity** — clarification proactivity asks for more information on an
   ambiguous query; directional proactivity surfaces follow-ups and related
   information once the main goal is met, with direct links rather than names.
4. **Emotional responsiveness** — acknowledge the situation ("Two weeks is a
   long time to wait") without professing feelings ("I'm sincerely sorry") or
   asserting what the user feels; it never substitutes for resolving the problem
   quickly.
5. **Transparency** — disclose upfront that it is AI, surface capabilities
   contextually rather than as an exhaustive list, explain why it cannot help
   and what it can do instead, and explain data practices inside the
   conversation rather than only in a privacy policy.

The transparency point echoes an earlier finding: when users know they are
talking to a bot they adapt their language to be more direct and
keyword-focused, dropping the politeness markers bots handle badly
[[2018-11-25_chatbots]]. On personality more broadly, the corpus leans one way:
deliberately humanizing an LLM backfires, because users anthropomorphize anyway,
warm systems show measurably higher error rates, and people who attribute
emotional traits to an AI are less likely to accept its advice
[[2026-01-09_humanizing-ai]]. Emotional responsiveness as defined above is
compatible with this — acknowledging circumstances is not the same as simulating
feeling — but the two sources set the dial at different points.

### Supporting iterative work, not just single answers

Qualitative studies of generative-AI use surfaced behaviours the chat window
handles badly:

- **Accordion editing** — users repeatedly ask the AI to expand or shrink an
  output to reach the length and level of detail they want, using word-count
  limits and forced rankings ("top 5") to compress
  [[2023-09-24_accordion-editing-apple-picking]].
- **Apple picking** — users reference specific elements of an earlier response
  in a new prompt, but a linear chat forces extensive scrolling to find and
  describe the part they mean, and they get lost comparing iterations
  [[2023-09-24_accordion-editing-apple-picking]].
- **Response outlining** — users add format and structure specifications to
  prompts (headings, numbering, "include a SWOT analysis"), usually only after
  an unsatisfactory first answer. It works, but carries high cognitive and
  interaction cost because it forces users to anticipate every component of the
  output, and an articulation barrier blocks those who lack the jargon
  [[2024-02-02_response-outlining]].

Both sources propose the same direction: hybrid interfaces. Add GUI elements
that suggest structural options or ask for specifications upfront instead of
letting users learn by failure [[2024-02-02_response-outlining]]; and add
compartmentalization — direct editing of a portion of a response,
point-to-select for referencing earlier content, and text editing that does not
regenerate everything [[2023-09-24_accordion-editing-apple-picking]]. Most users
still finish their editing in external tools anyway
[[2023-09-24_accordion-editing-apple-picking]].

### Known limits of conversational understanding

The 2018 study of chatbots found bots work smoothly on expected paths and fail
on deviation, losing context and forcing users to start over or escalate without
the history carrying across. They behave as decision trees with linear flows and
limited branching, closer to wizards than to intelligent systems. Carousels are
a poor way to present long result lists, because users doubt they are seeing
everything and worry about missing better options. Offering both predetermined
buttons and free text gives flexibility; forcing a single input method
frustrates [[2018-11-25_chatbots]].

Voice assistants show the same expectation gap from the user's side: people
described Alexa, Siri and Google Assistant as being like young children or
someone with poor hearing, restricted use to simple predictable tasks, and
either spoke naturally or artificially compressed queries into keywords —
dropping articles, changing word order — to maximise comprehension. They
projected gender and used politeness markers while laughing at themselves for
doing so, and raised trust and privacy concerns about always-on recording and
cloud transmission [[2018-08-05_voice-assistant-attitudes]].

### Voice and screen as complementary channels

Voice is an efficient input modality (quick commands on the user's own terms);
a screen is an efficient output modality (large amounts of information at once,
lower memory burden). Screen-first voice agents fragment functionality, execute
only the first step, and waste screen space with designs that drop the
affordances of the GUI. Voice-first devices with screens err the other way, and
arbitrarily prohibiting visual menus — for instance no browsable list across
15,000+ skills — imposes a memory burden the source compares to fighting with
one hand tied behind your back. The recommended direction is both modalities
fully integrated, with neither handicapped [[2017-11-12_voice-first]].

## Sources (13)

- [[2017-11-12_voice-first]] — examines voice input modality, natural language processing, and voice-driven interaction patterns.
- [[2018-08-05_voice-assistant-attitudes]] — text-based or voice-based interfaces that leverage natural language; users adapt their speech patterns based on perceived assistant capabilities, sometimes speaking unnaturally to improve success rates.
- [[2018-11-25_chatbots]] — how text-based conversation differs from graphical interfaces, including challenges of natural language understanding and maintaining conversation context.
- [[2023-09-24_accordion-editing-apple-picking]] — While simple on the surface, conversational interfaces create new usability problems that poorly designed chat histories do not adequately address.
- [[2024-02-02_response-outlining]] — conversational interfaces where prompt quality directly affects output quality.
- [[2024-03-01_ai-chat-not-the-answer]] — conversational interfaces powered by AI; one implementation pattern among many, appropriate for specific use cases but not universally applicable or always the optimal solution to user problems.
- [[2024-08-13_341_Dust_🇫🇷,_mieux_que_ChatGPT_Analyse_design_de_l_outil_IA_des_product_people...]]
- [[2025-09-30_397_Pourquoi_l_IA_n_a_pas_(encore)_révolutionné_l_UX]]
- [[2026-01-09_humanizing-ai]] — Conversational paradigms invite anthropomorphization; designers must offset that tendency through system prompts and interface decisions that foreground utility.
- [[2026-03-20_site-ai-chatbot]] — Documents real user behavior with site chatbots, identifying common design failures and patterns of successful use.
- [[2026-04-17_less-chat-more-answer]] — Details how users interact with site chatbots and what communication strategies work and fail.
- [[2026-04-24_ai-chatbots-design-guidelines]] — Comprehensive design guidelines for site chatbots covering discovery, communication, interaction, and content structure.
- [[2026-07-10_dimensions-of-ai-chatbots]] — require five key qualities—handoff willingness, flexibility, proactivity, emotional responsiveness, and transparency—to earn and maintain user trust.
