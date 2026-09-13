---
title: "AI Agents as Users"
date: "2026-04-10"
url: "https://www.nngroup.com/articles/ai-agents-as-users/"
author: "Kate Moran, Sarah Gibbons"
topics: [ai]
type: article
---

The design community has spent decades refining what it means to design for users. We study their behaviors, map their journeys, test our assumptions against their needs. Our discipline is, and should be, oriented around understanding who is using the product or service, and designing accordingly.

[AI agents](https://www.nngroup.com/articles/definition-ai-agent/) (systems that pursue a goal by iteratively taking actions, evaluating progress, and deciding its own next steps) are now interacting with the same digital interfaces we design for people.

They navigate websites, fill out forms, compare options, and execute transactions. [They do this crudely, often unreliably, and with significant limitations.](https://www.nngroup.com/articles/impressions-chatgpt-agent/) In functional terms, they are users of our interfaces, even if we haven't recognized them as such. There’s a conceptual shift required to account for this reality. **A core assumption needs updating: "user" is no longer synonymous with "human."**

## In This Article:

- [The Expanding Definition of "User"](#toc-the-expanding-definition-of-user-1)
- [How Agents Interact with Interfaces Today](#toc-how-agents-interact-with-interfaces-today-2)
- [What Breaks When Agents Are Users](#toc-what-breaks-when-agents-are-users-3)
- [Near Term: Designing for Both](#toc-near-term-designing-for-both-4)
- [Longer Term: When the Interface Layer Diverges](#toc-longer-term-when-the-interface-layer-diverges-5)

## The Expanding Definition of "User"

For most of the history of digital design, the word "user" has implicitly meant a human being sitting in front of a screen. Most design heuristics, usability principles, and research methods assume a human on the other end.

People are having agents attempt a nearly infinite variety of tasks: combining calendars and adding new events, booking flights, checking if a prescription has been refilled, finding the best-reviewed product under a certain price. The agent interacts with digital interfaces to find information, understand available actions, and execute them, just as a human user would.

While it may feel antithetical to the philosophy of user experience, **this reality means the agent is a user in every functional sense:**

- It has a goal.
- It encounters an interface.
- It attempts to accomplish the goal through that interface.
- The interface either supports that attempt or it doesn't.

The distinction matters because the interfaces we design today are already failing this new type of user. And those agents are, in turn, failing the human being on the other side of the screen.

## How Agents Interact with Interfaces Today

There are three primary approaches agents use to interact with digital interfaces, and each one reveals a different set of design assumptions that break down.

### Vision-Based Interaction

The most rudimentary approach mirrors what humans do: the agent takes a screenshot of the interface and uses a vision model to interpret what it sees. The agent looks at the page, identifies elements (buttons, text fields, navigation items), decides what to click, and repeats.

This approach is expensive — it’s slow, computationally wasteful, error-prone, and token-intensive. A single screenshot requires tens of thousands of tokens for the model to process and doesn’t account for dynamic content or multi-step workflows.

### Accessibility-Tree Parsing

Rather than screenshotting the page, agents can also read the browser's accessibility tree (the structured representation of the page that browsers generate from HTML). This is the same data structure that screen readers use to make interfaces navigable for people with visual impairments.

The accessibility tree provides a clean, hierarchical representation of page elements: their roles, labels, states, and relationships. It costs a few thousand tokens to process (a fraction of what a screenshot requires) and provides more reliable information.

Interfaces that are well-built for accessibility are already more legible to agents: semantic HTML, properly labeled elements, clear roles, and logical page hierarchy also serve agent users.

### Direct API Access

The third approach bypasses the interface entirely with [agent-to-agent interactions](https://www.nngroup.com/articles/service-design-evolve-ai-agents/) and agent-to-API interactions. When structured APIs are available, agents can query data and execute actions directly, without having to interact with any visual or structural representation of a page.

Emerging standards like the Model Context Protocol (MCP) are making this approach more standardized, but not necessarily more widespread.

## What Breaks When Agents Are Users

Consider a mundane example. A parent asks their agent to check the school website for upcoming events, cross-reference those dates against the family's shared calendar, and flag any conflicts. A human would scan the events page, note the dates, and check the calendar.

The agent's experience is different. The school website was designed for a parent to scan visually. Events are listed with dates, times, and descriptions arranged through spatial grouping. A human may not struggle to read this, but for an agent parsing a screenshot, every piece of information must be inferred from pixel clusters: which text is a date, which is a title, and how they relate. The events page may load dynamically, capturing an incomplete page. Some events live on the website, others in a downloadable PDF, others behind a parent-portal login.

Each step increases likelihood of error, as well as token-use. Completing something this ordinary and mundane becomes a large task, let alone agents completing more complex tasks: making changes to a profile, ordering an item, or checking availability and booking.

## Near Term: Designing for Both

In the immediate term, the design question is "how do we build interfaces that serve both human users and agent users simultaneously?” (This is context-dependent and assumes the delegation of tasks by your user aligns with your product or service’s ethos.)

Accessibility guidelines achieve this design goal: clear, descriptive element names, predictable interaction patterns, logical page hierarchy, semantic HTML, ARIA standards. These are accessibility fundamentals that the design community has understood, albeit often deprioritized, for years.

**Investing in accessibility has been the right thing to do, but now there’s a clear business case for it** as it's how agents will use products and services in the near term. Organizations that have been rigorous about accessibility have, perhaps without realizing it, been building interfaces that agents can already navigate more effectively:

- **Clear, descriptive labeling.** Avoid icon-only buttons, ambiguous link text ("click here"), and labels that depend on visual context.
- **Predictable, consistent patterns.** Consistent navigation structures, standard form patterns, and predictable state changes reduce the likelihood of agent errors compounding across multi-step workflows.
- **Minimal reliance on visual-only information architecture.** Structural markup must reflect the visual grouping in order for agents to understand relationships.

None of these recommendations are new. They are the same principles that make interfaces more usable for humans with disabilities, more robust across devices and contexts, and more maintainable over time.

### What If You Don’t Want Agents in Your Product?

There are certainly business models and product categories where having an agent in your product may be undesirable. The argument for designing with agents in mind assumes that your users' goals and your business goals stay aligned when a machine acts on the user's behalf. That's not always true.

#### When the Visit Is the Product

Some businesses depend on humans actually visiting the product. For these companies, an agent that extracts the value without the visit is an existential problem. Ad-supported content and content marketing sites have already begun to see the impacts of this shift in their metrics.

Streaming services have a version of this problem, too. Netflix wants you to *browse* — browse time surfaces original content and deepens the engagement loop that drives retention. An agent that answers "what should I watch tonight?" without the user ever opening the app undermines the discovery experience Netflix has been optimizing for years.

#### When Friction Is Intentional

Not all friction in an interface is a design failure. In some domains, the friction exists for regulatory, legal, or safety reasons — and removing it creates liability.

Financial services are full of examples. A brokerage that makes it easy for an agent to execute trades without safety checkpoints and legal disclosures opens itself to regulatory risk. The friction is necessary.

Healthcare products will face similar challenges. HIPAA restricts how patient data can be accessed and by whom, and the question of whether an AI agent acting on a patient's behalf qualifies as an authorized accessor is unresolved. Until it is, healthcare organizations have legitimate reasons to resist agent access.

#### When You're Protecting Competitive Intelligence

Some interfaces are deliberately opaque to machines because the data behind them is competitively sensitive.

Airlines, hotels, and rental car companies have spent years fighting screen-scraping bots. Their pricing is dynamic, proprietary, and strategically managed — real-time access to that data is exactly what competitors and price-comparison aggregators want. Making interfaces agent-friendly would undo all that.

#### When You Want Your Product to Be the Agent

There are plenty of platforms that want to *be* the agent layer themselves. Some products are actively restricting third-party agent access — blocking external MCP calls, limiting API surface area — because they see their own AI capabilities as a differentiator. If your product's value proposition is becoming "the intelligent layer" on top of your users' data, letting an external agent treat your platform as a dumb data store commoditizes the thing you're building toward.

### The Competitive Risk of Opting Out

None of this means the decision to block agents is risk-free. The harder question is what happens when a competitor *doesn't* block them.

If you work for a bank, you might make the reasonable choice to prevent agents from executing transactions on behalf of your customers for security reasons. But what happens when a competitor offering similar financial products starts advertising that they support agentic wealth managers?

This is a strategic calculus, not a universal imperative. Designing for agents isn't always the right call, but opting out entirely carries its own risk. Whether you optimize for agents or not, we all need to (at minimum) recognize that agents will attempt to use our products.

## Longer Term: When the Interface Layer Diverges

When agents can query structured data and execute actions the visual interface will become irrelevant to them. As more organizations expose their services through agent-compatible APIs, the design problem for human users and agent users will increasingly separate.

Despite this, **humans will still need interfaces**— visual, interactive, designed for comprehension and decision-making.

**Agents will interact with the underlying data** and logic directly. The experience a human has will depend on their agent’s ability to complete a task.

### Conclusion

The word "user" was always a shorthand. It described the entity trying to accomplish a goal through the thing we designed. For decades, that entity was exclusively human, which is no longer the case.

Recognizing agents as users requires expanding an assumption that has been implicit in our work since the field began. What changes with this shift is the scope of who we're designing for, and the urgency of practices we already know matter: semantic structure, accessibility, clear labeling, and predictable interaction patterns.
