---
title: "Context Architecture"
date: "2026-06-12"
url: "https://www.nngroup.com/articles/context-architecture/"
author: "Paz Perez"
topics: [ai, information-architecture]
type: article
---

## In This Article:

- [From Prompts to Context](#toc-from-prompts-to-context-1)
- [Why Context Matters](#toc-why-context-matters-2)
- [The Context Ecosystem](#toc-the-context-ecosystem-3)
- [From Context Engineering to Context Architecture](#toc-from-context-engineering-to-context-architecture-4)
- [IA Principles for AI Systems](#toc-ia-principles-for-ai-systems-5)
- [Context Is Never Neutral](#toc-context-is-never-neutral-6)

## From Prompts to Context

The way we shape AI products has evolved quickly.

It started with prompt engineering. Early on, success depended on crafting the right instruction. A well-written prompt could unlock surprisingly strong results, and teams began collecting and reusing prompts as assets.

Then came context engineering, a concept coined by [Tobi Lutke](https://x.com/tobi/status/1935533422589399127). Teams realized that prompts alone were not enough; what matters is a concise collection of context-specific guidance, targeted to the task at hand: instructions, retrieved knowledge, narrow tools, selected memory, and state all working together. The task shifted from writing prompts to orchestrating context.

Now we are entering the era of agentic systems. Agents do not just respond, they perform tasks on behalf of the user. They retrieve information, call tools, maintain state, and act across multiple steps. They operate with increasing autonomy, often coordinating with other agents.

This shift unlocks a new design problem. We are no longer defining only what to say to a model, we are designing the environment in which it thinks and acts.

To address this challenge a familiar discipline, information architecture, becomes critical in a new form: **context architecture**.

For millennia, humans have organized information so people can understand it, navigate through it, and use it effectively. We developed structures, taxonomies, labeling systems, and navigation patterns to reduce ambiguity and improve findability. LLMs need the same foundations.

The challenge is not only the access to information. It is making that information meaningful, structured, and usable for both humans and machines.

This is the role of information architecture, now applied to context itself.

And in the age of AI, it becomes central.

## Why Context Matters

Traditional digital products are deterministic. We design flows step by step, define our product's behavior across those flows, and hard-code them. This way allows us to have a consistent output every single time. The system behaves as intended, and we have to worry only about how the user would react to it.

AI products change this dynamic. LLMs are probabilistic, so the same input can lead to different outputs. That variability is part of their power, but it also means we no longer have full control over what the system produces. The challenge shifts from defining exact outcomes to shaping the behavior of the system, while still accounting for how users will interpret and respond.

For many teams, training data is not something they can directly control. They rely on third party models and foundation models trained elsewhere. That makes context one of the primary ways to shape system behavior. Instructions, retrieved knowledge, tools, memory, and state all influence how the model interprets a task and generates a response. Teams can then measure whether changes to the context actually improve system behavior.

## The Context Ecosystem

Context is not just a list of system prompts; it is an ecosystem of information that needs to be discovered and selected. It is everything inside the context window of an AI system. It can either live there or be retrieved from stored information, to shape the model's output.

In modern AI systems, context is assembled dynamically from multiple sources:

- **System instructions and guardrails** are directions designers and engineers give the system about what it should and should not do. These are not visible to the end user, and companies use them to steer results toward the desired outcome.
- **Retrieved information from knowledge bases** is information pulled from databases or other knowledge sources, often through RAG (retrieval-augmented generation). When prompted, AI systems search for and retrieve relevant information, then use it to generate a response grounded in that content.
- **Skills** are reusable packages of instructions, scripts, and resources that agents load only when needed. By default, only the skill's name and description are loaded, and the full skill is disclosed when invoked.
- **Tools** are external capabilities that an AI system can call to take action or access information beyond its context window. They can include web search, calendars, databases, APIs, and more. Increasingly, these capabilities are exposed through MCP (Model Context Protocol), which standardizes how models discover and interact with tools and external resources. Their effectiveness depends not only on the capability itself, but also on how tools are described, labeled, categorized, and incorporated back into the context. Poorly structured tool definitions can lead agents to select the wrong tool, retrieve irrelevant information, or take unnecessary actions.
- **Long-term memory** includes information the system retains across conversations or is explicitly instructed to remember over time.
- **Conversation (short-term) memory** is the immediate history of the interaction within a session.
- **The user's prompt** is the immediate input provided by the user at a given moment.

![Diagram of AI-Context Ecosystem: a system-internal group (knowledge base/RAG, tools/MCP, skills, system prompts, guard rails, memory) alongside user-visible context (conversation and user prompt).](https://media.nngroup.com/media/editor/2026/06/11/the-ai-context-ecosystem.png)

The AI-Context Ecosystem 

All these elements blend natural language, structured markup, and code. Some may be long and layered.

However, more context does not lead to better results, because every element competes for the model's "attention." Just like humans, models are affected by information overload.

Poorly structured context can slow systems down, increase costs, and lead to inconsistent or error-prone outputs. Clear context structure and prioritization matter as much as the content itself.

## From Context Engineering to Context Architecture

Context engineering is how engineering teams now shape AI behavior. It recognizes that these systems are not driven by a single input, but by a collection of interacting signals that need to be curated and maintained.

This is where UX professionals are needed.

We have seen this dynamic before in physical systems. Before moving to UX, I worked as an architect designing public schools in New York City. Engineers ensured the plumbing worked, the electricity flowed, and the structure held together. Architects focused on a different set of questions: What was the building for? How should people move through it? How should the spaces be organized so they make sense to the people using them?

What makes a house feel like a home is not just structural integrity. It is the natural light, the proportions of a room, and the spaces where people gather and create memories.

The same nuances apply here. Context engineering builds the infrastructure. Context architecture defines the structure of the information that lives on top of it. While context engineering focuses on pipelines and components, **context architecture,** led by information architects, focuses on structure, meaning, and behavior.

It asks things like:

- What concepts belong in the context?
- How are they labeled and how do these labels map onto user language?
- How do they relate to each other?
- What should the system remember or forget? Which sources should be trusted more?
- What should it never do?

Information architects define what metadata exists, how entities relate to each other, and how the structure reflects the user's mental model, ultimately making the model more efficient and accurate. For example, a well-designed taxonomy allows engineers to retrieve only the policies related to billing disputes instead of searching across all customer-support documentation, thus reducing retrieval noise and improving response accuracy. Similarly, labels aligned with the users' mental models help engineers invoke the right skill for each task. For example, labeling a skill *reset password* instead of *credential-recovery workflow* makes it easier for the system to match the skill to a user saying, "I can't log in."

As AI systems become embedded in everyday products, the collaboration between information architects and context engineers becomes critical. Context architecture is more than writing clear prompts or formatting instructions with headings and bullets. It is the design of the entire information environment surrounding an AI system. It includes how knowledge is structured, how tools are labeled, how retrieval works, how memory is organized, and how concepts relate to one another. Good writing improves readability. Context architecture shapes how the system interprets information, makes decisions, and behaves.

## IA Principles for AI Systems

Context architecture is rooted in IA principles and requires a structured approach to designing how context is organized, connected, and delivered. We developed a framework grounded in **core information-architecture principles**, adapted for AI systems. It is still evolving, shaped by the rapid pace of AI and the need to continuously refine how we build.

The framework applies across the entire context ecosystem. A well-written prompt cannot compensate for poorly structured retrieval, inconsistent labels, overlapping tools, or noisy memory systems.

### Structuring Context

Information architects structure context so AI systems can reason more effectively. When information is organized clearly, ambiguity and cognitive load are reduced for both users and models. Systems spend less effort interpreting inputs and can generate more accurate responses.

Let's take the example of a customer-support AI agent. Without clear structure, the support agent might retrieve large amounts of loosely related information from across the company's knowledge base.

Example: A customer-support agent without structured context | User prompt: | "I am locked out of my account" | System retrieves | Agent's output | Old troubleshooting notes | Deprecated password-reset procedures | Security-escalation policies | Internal employee conversations | Outdated instructions | Misleading steps to recovery | Unnecessary escalation | Hallucinated procedural steps

The problem is not the model itself. The problem is that the system must interpret noisy and unstructured context. Information architects reduce this ambiguity by organizing context into clear structures the system can navigate more reliably.

A structured context helps the system understand which information matters most, which sources are authoritative, and how concepts relate to one another.

Example: A customer-support agent with structured context | User prompt | : "I'm locked out of my account" | IA tool | What it does | Examples | Why it helps | Hierarchy | Establishes information priority and depth | Rules for information priority: | Approved company policies appear above team notes. | Current workflows appear above deprecated procedures. | Core account-recovery instructions are surfaced before edge cases. | The system can identify which information should carry the most authority during reasoning and retrieval. | Categorization | Groups related concepts into clear domains | Content categories: | Account access | Billing | Technical troubleshooting | Security | Enterprise administration | Instead of searching across all support documentation, retrieval can target a smaller and more relevant subset of information. Retrieval noise is reduced and response accuracy improves. | Labeling | Ensures the language inside the system aligns with how users naturally describe problems. | Labels inside the system: | Locked out | Cannot log in | Reset password | Instead of: | Credential invalidation | Authentication failure | Identity-recovery workflow | Aligned labeling improves retrieval and workflow selection because the system can better map user language to internal concepts.

### Improving Findability

LLMs often struggle with findability much like users navigating a confusing website. We want to prevent AI agents from retrieving the wrong information or taking unnecessary steps. When agents can find the information right away, they are more accurate and more efficient. Better findability also reduces the system's load by limiting the amount of irrelevant information that it must process before retrieving the correct context.

Let's look at skills, one layer of the context ecosystem. In the example of the customer-support AI agent, findability helps the system quickly identify which skill matches the user's request. If the skills have vague or overlapping names or descriptions, the agent may choose the wrong one, ask unnecessary questions, or search broad support documentation instead of addressing the specific user problem.

Example: A customer-support agent with no IA support for finding skills | User prompt | : "I'm locked out of my account" | Skills | Agent's Behavior | Name: | account-support | Description: | Use this skill for account issues. | Name: | customer-help | Description: | Use this skill when customers need help. | Name: | access-workflow | Description: | Use this skill for access related workflows. | Because the skills are difficult to distinguish, the agent may choose the wrong one, ask unnecessary questions, or search broad support documentation instead of using the correct login workflow.

Information architects improve findability by making context easier to discover, distinguish, and retrieve.

Example: Customer-support agent with IA support around skills | User prompt | : "I can't log in" | IA tool | What it does | Example | Why it helps | Taxonomy | Groups related skills into clear categories. | Account access | reset-password | unlock-account | verify-identity | Billing | update-payment-method | refund-request | subscription-change | The agent can narrow its search before selecting a specific skill. | Controlled vocabulary | Ensures the system uses the same terms as the users for the same concepts. | Name: | account-access-support | Description: | Use this skill when the user cannot log in, is locked out, needs a password reset, or has trouble accessing their account. | User language, such as "I can't log in," is connected to the correct internal concept. | Unambiguous naming | Makes each skill easier to compare and invoke. | Name: | reset-password | Description: | Use this skill only when the user needs to reset, recover, or change a password. | Name: | unlock-account | Description: | Use this skill only when the user is locked out after failed login attempts. | Clear names reduce overlap and help the agent select the right skill faster.

### Aligning to Users' Mental Models

A conceptual model for context is the system's internal representation of what information matters, how different pieces of information relate to each other, and when a particular one should be used during an interaction.

An important part of context architecture is aligning the system's internal model with the user's mental model. In practice, that means structuring context around how users naturally describe problems, form expectations, and move through tasks.

In our example of a customer-support AI agent, this alignment is essential. The system must correctly map the user's language and intent to the appropriate tool. The system has access to tools and connected services, each with descriptions and metadata that help the model decide when to use them, but the tools' descriptions are inconsistent and overly technical. Because the system's conceptual model reflects internal engineering terminology instead of user language, the agent may end up performing the wrong action. The issue is not the lack of tools or MCP ([model-context protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol)) integrations. It is that the descriptions, labels, and relationships in the context layer do not match the user's mental model.

Example: Customer-support agent's internal model does not match user's mental model | User prompt: | "I can't log in and I need help fast." | Tool Descriptions | AI Agent's Output | Credential-recovery workflow | Handles authentication state transitions | Identity-validation sequence | Triggers identity-escalation protocol | Select the wrong tool | Trigger expensive workflows | Ask confusing clarification questions | Fail to recognize that "can't log in" maps to account access recovery

Information architects align tool structures and terminology with how users naturally think and communicate. They may organize tools into categories that map onto how users think and make sure that the internal description language matches the users' language.

Example: Customer-support agent's internal model matches user's mental model | User prompt: | "I can't log in and I need help fast." | IA tool | What it does | Examples | Why it helps | Taxonomy | Organizes tools into categories users intuitively recognize. | Account Access | reset-password | unlock-account | verify-identity | Billing | request-refund | update-payment-method | The system can narrow down the set of relevant tools before selecting one. | Ontology | Defines how concepts relate to one another. | 'Can't log in' relates to account access | Locked account may result from multiple failed logins. | Urgent access issue may require priority escalation. | The system can reason about intent and select tools accurately. | Labeling | Aligns tool names and descriptions with user language. | Instead of | credential-recovery workflow | use | reset-password | Instead of | authentication-state_manager | use | unlock-account | Aligned terminology improves tool selection, reduces ambiguity, and makes interactions feel more natural to users.

### Designing Memory

Memory determines continuity and relevance over time. Without a clear structure, systems either forget critical information or become overloaded with irrelevant details. Use system instructions to define:

- What to remember
- How to index it
- When to retrieve it

Structuring memory becomes increasingly important as conversations grow longer and users continue working within the same chat over time. Teams must decide what the AI system [needs to know and what it needs to forget.](https://youtu.be/esY99nYXxR4?si=INaCD2b6Ya3P1o5E)

In our customer-support-agent example, the lack of clear memory-related instructions may cause the agent to retrieve everything from previous conversations at the expense of critical long-term information. As the conversation grows, the memory retrievals become noisy and inconsistent. The problem is not memory itself. The problem is the lack of structure governing what should persist over time.

Example: Customer-support agent with noisy and inconsistent memory layer | Returning user's prompt: | "I'm still having trouble accessing my account." | Related Information from Memory | AI Agent's Behavior | Irrelevant information: | Old troubleshooting attempts | Expired billing disputes | Unrelated technical issues | Relevant information: | Accessibility preferences | Preferred communication method | Enterprise-account status | Surfaces irrelevant information | Misses important customer preferences | Increases token usage and latency

Information architects design memory systems with clear rules for retention, retrieval, and relevance so the system retrieves only the information needed for the task at hand.

Example: Customer-support agent with structured memory | Returning user's prompt: | "I'm still having trouble accessing my account." | IA tool | What it does | Example | Why it helps | Faceted classification | Organizes memory into distinct types | Accessibility preferences | Billing history | Security verification | Active support cases | Temporary troubleshooting steps | The system can retrieve only the memory relevant to the current task. | Scoping rules | Define when memory should be available | Temporary troubleshooting details should be accessed only during the current session. | Accessibility preferences persist across conversations. | Irrelevant information won't contaminate future interactions. | Retention policies | Define how long different types of information should persist | Password-reset tokens expire quickly. | Active billing disputes remain accessible until resolution. | Resolved support tickets are archived. | The rules balance continuity with relevance and privacy.

Both the system and the user should have transparency into how these practices are applied. Clear and visible memory rules help users understand what information is retained, why it matters, and how it is used over time, which ultimately helps build trust in the product.

## Context Is Never Neutral

The decisions we make when designing context shape how a system interprets tasks and directly influences its output. Context design includes:

- The naming we choose
- The relationships we define
- The constraints we encode

These are not neutral decisions. They determine how meaning is constructed and how outcomes are produced. This is design work, and it needs to be treated as such.

**AI introduces new tools, but the underlying challenge remains the same.** We are still organizing information in service of human goals. The difference now is that the AI system is also an active participant, interpreting that structure and acting on it.

Context architecture sits at the intersection of technology, business, and human intent. It is how meaningful AI products take shape.

Information architects are needed now more than ever.
