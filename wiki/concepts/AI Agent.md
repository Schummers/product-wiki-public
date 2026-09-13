---
type: concept
name: AI Agent
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "AI Agent Design"
  - "AI Agents"
  - "Agent IA"
  - "Intelligent Assistants"
---

# AI Agent

## Definition

"An AI agent is a system that pursues a goal by iteratively taking actions,
evaluating progress, and deciding its own next steps"
[[2026-04-03_definition-ai-agent]]. Five components make it up: pursuing a goal,
iteratively acting, evaluating progress, deciding next steps, and carrying
context forward across steps [[2026-04-03_definition-ai-agent]]. The LLM is only
the reasoning engine; the agent is the system built around it with tools,
external actions, and an iterative loop, and self-direction is what separates it
both from an LLM that responds once and from automated systems following
predetermined rules [[2026-04-03_definition-ai-agent]]. The distinction from a
chatbot is drawn concretely: the chatbot understood the request and described
the steps, handing them back to the user, while the agent attempted the work
itself [[2026-04-03_definition-ai-agent]].

The corpus reaches this definition after a long earlier phase of writing about
intelligent assistants and chatbots. A chatbot is "a domain-specific text-based
conversational interface that supports users with a limited set of tasks",
requiring natural-language processing and intelligent interpretation but not
necessarily voice output or agency — "the poor relative of the intelligent
assistant" [[2018-11-25_chatbots]]. The voice assistants of that era (Siri,
Alexa, Google Assistant) were studied for the gap between advertised and actual
performance [[2019-02-03_mental-model-ai-assistants]]
[[2018-10-21_intelligent-assistant-user-needs]]. The 2026 articles add two newer
framings: agents as a class of users of human interfaces
[[2026-04-10_ai-agents-as-users]], and agents embedded in tools, as with
Replit's coding agent, which develops an interface step by step from user
stories and handles databases and API calls natively
[[2025-02-18_365_Replit,_l’outil_de_prototypage_design_ultime]].

## Practice

### Judging whether an agent is useful

A useful agent reliably understands goals, adapts when things fail, and
minimises the human review needed; usefulness is context- and task-dependent
[[2026-04-03_definition-ai-agent]]. Agents can fail in two distinct ways — bad
execution (doing things poorly) and bad judgement (poor decisions about what to
attempt) [[2026-04-03_definition-ai-agent]] — and usefulness must be evaluated
through user research and task-completion metrics rather than technical
capability alone [[2026-04-03_definition-ai-agent]]. The Qwen study makes the
same point from the other direction: the underlying capability was strong, yet
usability issues produced confusion, uncertainty, and friction, so capability
alone is insufficient for adoption; users must understand, guide, and trust the
system [[2026-05-08_designing-ai-agents]].

### The gap between what users want and what they attempt

The diary study of 12 participants logging 428 unique "ideal" needs found that
existing assistants could fully address 41% and partially address another 21% —
yet participants actually tried an assistant for only 7% of those needs,
suggesting low expectations and prior frustration
[[2018-10-21_intelligent-assistant-user-needs]]. Both gaps, the capability gap
and the usage gap, must be closed for assistants to be truly useful
[[2018-10-21_intelligent-assistant-user-needs]].

Demand characteristics from that study: 84% of ideal needs involved spoken
commands as the trigger, with free-form voice input expected as a core
capability; 58% were one-step tasks, while with current assistants only 26% of
users engage with anything more complex than one step; 12% involved the
assistant acting without an explicit command based on context, a capability
users expect but rarely get; 65% required access to personal information and 44%
required web-based information, both areas where assistants integrate poorly
[[2018-10-21_intelligent-assistant-user-needs]].

### Mental models and the fragility of first impressions

Frequent users of intelligent assistants settle into one of three mental models
— the assistant as an interface to the web or smart home, as a handy helper, or
as a repository of all knowledge — and these models drive usage
[[2019-02-03_mental-model-ai-assistants]]. Usage stays limited and stable
(weather, music, reminders) despite long lists of advertised skills, and mental
models form through experience rather than marketing
[[2019-02-03_mental-model-ai-assistants]]. The consequential finding: "once
users decide that the assistant cannot do something, they are unlikely to try it
again very soon", so poor initial performance blocks the later adoption of
improved features, and new users are the most fragile group
[[2019-02-03_mental-model-ai-assistants]].

The Qwen research shows the same mechanism in an agentic context: mental models
of chatbots favour answering questions over completing transactions, and one
participant said outright that ordering deliveries through a genAI chatbot was
not their habit [[2026-05-08_designing-ai-agents]]. Agents must therefore either
align with existing mental models or explicitly teach a new paradigm, since
mismatches cause confusion and abandonment [[2026-05-08_designing-ai-agents]].

### Design guidance for agent interfaces

From the Qwen study, four lessons [[2026-05-08_designing-ai-agents]]:

- **Support discoverability through redundancy** — provide redundant entry
  points, both text prompts and visual menus, so users can find what the agent
  can do; note that prefilled prompts for broad categories can backfire when
  they default to the wrong choice.
- **Use familiar patterns** — confidence rises when the agent interface mirrors
  established conventions such as delivery apps ("Okay, now I know where I am.
  This looks familiar"), but familiarity must still fit context: carousels
  showing one option at a time make users underestimate the choices available.
- **Handle personal data carefully** — users do not always understand how agents
  access or use their data; showing a full address before item selection created
  a false impression of leakage ("I feel like my address was leaked"), so
  surface only the minimum data per step and explain its use.
- **Prioritise transparency to protect autonomy** — users want efficiency
  without losing control; missing information about pricing, fees, minimum
  orders, or baggage allowances caused abandonment, while agents that inform
  users retain long-term trust.

The carousel problem is not new: the chatbot research had already found that
showing long lists through carousels works badly, since users doubt they are
seeing all options and worry about missing better ones
[[2018-11-25_chatbots]].

### Lessons carried over from chatbots

Chatbots come in two types: customer-service bots handling support queries, and
interaction bots enabling transactions; the former are faster than human agents
but perceived as less helpful [[2018-11-25_chatbots]]. Practical findings that
still read as design constraints: bots work when users follow the expected path
and fail when users deviate, forcing a restart or an escalation without
preserved context; transparency about bot identity improves interaction, because
users then adjust their language to be direct and keyword-focused; bots function
as decision trees with linear flows and limited branching, feeling like wizards
rather than intelligent systems; and offering both predetermined buttons and
free-text input gives users flexibility, while forcing a single input method
frustrates them [[2018-11-25_chatbots]]. The importance of escape hatches to
human agents and of clear indications of bot capability, to set expectations,
belongs to the same set [[2018-11-25_chatbots]].

### Agents as users of your interface

Agents now navigate websites, fill forms, and execute transactions, which makes
them functional users: "user is no longer synonymous with human"
[[2026-04-10_ai-agents-as-users]]. When an interface fails an agent, it fails
the human who delegated to it [[2026-04-10_ai-agents-as-users]]. Three
interaction approaches exist: vision-based (screenshot plus vision model),
expensive and error-prone; accessibility-tree parsing, cheaper and more
reliable; and direct API access, which bypasses the interface entirely
[[2026-04-10_ai-agents-as-users]]. The practical consequence is that
accessibility work — semantic HTML, clear labelling, predictable patterns,
proper ARIA — is now both an ethical and a pragmatic investment, since
accessible interfaces are already agent-friendly
[[2026-04-10_ai-agents-as-users]].

Opting out is treated as a strategic decision rather than a default: some
business models depend on human visits (ad-supported sites), some need friction
for regulatory reasons, some guard competitive intelligence, and some want to be
the intelligent layer themselves — but blocking agents carries risk if
competitors enable them [[2026-04-10_ai-agents-as-users]]. In the near term the
question is serving both human and agent users; longer term, the interface
layers may diverge into dedicated APIs for agents and visual interfaces for
humans [[2026-04-10_ai-agents-as-users]].

### Structural advantages between platforms

Platforms that already own delivery, payments, and behavioural data — Alibaba is
the example — hold a competitive advantage in building agents, because the agent
can anticipate requests and default to known user preferences, keeping users
inside the ecosystem [[2026-05-08_designing-ai-agents]].

### Agents as a design tool

Agents also appear on the designer's side of the desk. Replit's built-in AI
agent generates functional code from natural-language specifications, developing
the interface step by step from user stories and handling databases and API
calls natively, which makes it suited to prototyping complex flows or
AI-dependent features that Figma cannot cover and that Protopie cannot back with
real data [[2025-02-18_365_Replit,_l’outil_de_prototypage_design_ultime]]. Two
caveats accompany it: basic coding skills remain indispensable to identify and
fix bugs when the agent loops, and function should be prioritised over form,
since a fully functional flow without brand styling teaches more than the
reverse [[2025-02-18_365_Replit,_l’outil_de_prototypage_design_ultime]].

## Sources (7)

- [[2018-10-21_intelligent-assistant-user-needs]] — what users expect from intelligent assistants and the gap between ideal capabilities and current limitations in voice-activated systems.
- [[2018-11-25_chatbots]] — chatbots as limited implementations of broader intelligent assistant concepts, with constrained capabilities compared to ideal conversational systems.
- [[2019-02-03_mental-model-ai-assistants]] — Study of voice interface systems (Siri, Alexa, Google Assistant) examining their actual capabilities, user perceptions, and the gap between advertised and real-world performance.
- [[2025-02-18_365_Replit,_l’outil_de_prototypage_design_ultime]]
- [[2026-04-03_definition-ai-agent]] — Provides a durable definition that helps practitioners distinguish agents from chatbots and evaluate agent capabilities.
- [[2026-04-10_ai-agents-as-users]] — Examines agents as a new class of users and what that means for interface design.
- [[2026-05-08_designing-ai-agents]] — Successful agent design requires supporting discoverability through redundant entry points, using familiar interaction patterns, and maintaining user control through transparency about data, pricing, and limitations.
