---
title: "UX-Context Design: Using UX Knowledge to Inform AI-Generated Design"
date: "2026-07-24"
url: "https://www.nngroup.com/articles/ux-context-design/"
author: "Tony Alicea"
topics: [ai]
type: article
---

## In This Article:

- [Context Is the New UX Deliverable](#toc-context-is-the-new-ux-deliverable-1)
- [Everyone Is Designing](#toc-everyone-is-designing-2)
- [AI-Ready Deliverables](#toc-ai-ready-deliverables-3)
- [DESIGN.md](#toc-designmd-4)
- [A Hypothesis: UX.md](#toc-a-hypothesis-uxmd-5)
- [Curation, Not Handoff](#toc-curation-not-handoff-6)
- [Open Research](#toc-open-research-7)

## Context Is the New UX Deliverable

AI models produce output based on context. Context is everything the model can see when it does the work: your request, plus whatever instructions, standards, examples, and background information come along with it.

Context enables you to avoid middle-of-the-road output. For example, an AI model has been trained on a huge number of search screens, so when you ask for one, it produces an *average* search screen. It knows what software *generally* looks like. It doesn't know your users, your domain, your design standards, nor anything your team has learned from research. Unless that knowledge is in the context, the model designs without it.

Context *leans* a model’s output in a particular direction.

Think of a skilled builder designing your house without ever meeting your family. They design the average house. Two stories, because most houses have two stories. And if you use a wheelchair, or you have a baby who needs to sleep near you, or you have no kids and you and your partner both work from home, the design will be wrong in ways that impact day-to-day quality of life. That’s not the builder’s fault; the problem is the builder didn’t have context.

Similarly, the difference between generic AI output and AI output that fits your users and matches your organization’s standards is mostly a difference in context. So, what should we put in it?

## Everyone Is Designing

Before answering, it helps to look at who is prompting these tools.

In many organizations, designers are no longer the only people producing designs. A product manager asks an AI tool for a quick mockup to make an idea concrete before a meeting. An engineer asks a coding assistant to add an export feature, and the assistant decides the button placement, the wording, the error states. These are all design decisions made by the AI.

The instinct might be to gatekeep who does design work, but that’s counterproductive. These tools are too available, too fast, and too useful for turning ideas into concrete forms. The more practical goal is to **ensure that everything AI generates, no matter who prompts it, is informed by an organization's knowledge of its users and design standards**.

That goal changes the output of research and design work. Historically, UX work produced deliverables for humans: personas, journey maps, research reports, annotated wireframes. A human read them, interpreted them, and made decisions. If AI is doing more of the building, then AI becomes the consumer of research and design deliverables.

And what an AI consumes is **context**.

Thus, the output of research and design work is, primarily, context that anyone in the organization can include when using AI to generate anything from slides to prototypes to working software. We call the creation of this output *UX-context design*.

> **UX-context design** is the practice of discovering and curating what an organization knows and wants into the context that guides everything its AI tools generate: from who its users are and the world they live in, to how a product should look and behave.

UX-context design also involves testing the efficacy of that context with the models your team is using and refining the context to improve the output quality for everyone.

## AI-Ready Deliverables

A first attempt at UX context might include what we already have: the personas, the journey maps, the findings reports. Some of those will help. But these artifacts were designed for human attention. A persona has a stock photo and a first name with the intention of helping a human to empathize and remember. However, a model does not need persuading, it needs the underlying reasoning.

That reasoning can be distilled with AI help. It can be useful, for example, to simply give raw research transcripts to a model and let it extract insights. Without human guidance, however, it’s possible that important takeaways may be lost in all the noise, or the AI may over-focus on the wrong takeaway.

To serve as maximally effective context, research and design output needs to be made “AI-ready” (or “machine-readable”), be curated by a skilled human, and made readily available to anyone that designs, no matter their role.

## DESIGN.md

Let's look at a concrete example. In April 2026, Google Labs open-sourced [DESIGN.md](https://github.com/google-labs-code/design.md), a file format for describing a product's visual identity to AI coding tools. The format grew out of Stitch, Google's AI design tool, and is now a draft specification that anybody can use.

A DESIGN.md file lives alongside a product's code and holds two kinds of content. One part is “machine-readable” exact values: the colors, type sizes, spacing, and corner radii of the design system, written so tools can read them precisely. The other part is plain, human-readable prose explaining what those values are for and how to apply them, including do's and don'ts, providing guidelines for both humans and AI. [Google's announcement](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/) says that, instead of guessing intent, AI tools can "know exactly what a color is for," and can check their color choices against accessibility contrast standards.

This serves as a good example of a successful format for UX context, and provides some lessons. It's a text file, kept next to the code, that AI tools read every time they generate something. Unlike traditional deliverables, there is no handoff: UX context feeds directly into product creation.

But visual identity is only one part of user experience and product design. What about everything else from research and design that informs the building of a product?

## A Hypothesis: UX.md

Let's imagine another text file, with a broader intent than DESIGN.md. We'll call it UX.md. It would reference DESIGN.md for visual standards and point to where the product's actual components live in the code. However, it could also include things like:

- **Research synthesis.** The major findings, stated as straightforward insights that the AI can reason upon. "Users abandon setup when asked for information they don't have on hand" is a finding that becomes a constraint on what is generated, not just an insight in a report.
- **Interaction standards.** How the product behaves. When to confirm versus allow undo. How errors are worded. Whether UI is optimized for expert users or novices.
- **A glossary.** The words the product and its domain experts use, with definitions. If your users say "case" and are confused by "ticket," the AI should know that.
- **User models.** User modeling states what research has established about the users themselves: their expertise, their concerns, what they are trying to accomplish, what doesn't work for them.
- **World models.** World modeling includes the conditions the user is in while using the software. (The term is borrowed from AI research, where a world model is a system's understanding of real physical environments.) For UX purposes, we model the circumstances of the world the users live in (i.e., “context of use”) and how they can change: users are interrupted mid-task (a nurse on a hospital floor), are under stress (filing a claim after a car accident), or operate under compliance rules (every action must leave an audit trail).

DESIGN.md shows how visual-design standards can be made available to AI tools. UX.md is a broader hypothetical version of the same idea: a structured source of UX research, interaction standards, terminology, and context-of-use knowledge that AI tools can use when generating product work.

Suppose your research synthesis says that users work in the product for hours at a time, making complex decisions with many variables. That finding should lean generation towards denser screens that keep more information in view, the kind expert users prefer. A finding that the product is used a few minutes a month should lean AI towards fewer choices per screen. An AI without that context will default to whatever is most common in its training data.

Of course, for large projects a single file might not be enough. Instead, UX.md could serve as an index to a folder of context files, each used for a specific purpose. Or you might instead make the context available via MCP servers and agent skills, or some other method.

Since context steers AI generation, this approach has an interesting side-effect: research insights and design standards find their way into unexpected places. For example, users’ glossary terms may show up in the behind-the-scenes code, rather than terms the engineers might have chosen on their own. Research and design output becomes embedded wherever AI is used.

## Curation, Not Handoff

Taking a cue from what we learned from DESIGN.md, we see two important properties of an artifact like UX.md that differentiate it from traditional research and design artifacts.

First, it is not written for humans. People *can* read it, but its success is measured by whether AI output improves, not by whether stakeholders are convinced by it. This could become a measurable standard, a metric you can track over time.

Second, it is not separate from the product. It lives with the product's code, changes when the product changes, and is read by every AI tool in the organization each time something gets generated. The research and standards are in the room every time anyone generates anything, whether that person is a designer, a product manager, or an engineer.

This is not an artifact that is left behind over time, or handed off to other humans, but a continuously curated source of truth. UX.md (or its equivalent) is never finished. New research updates it, and so does watching what the AI gets wrong. It is continuous research and continuous design, accumulating in one place for the entire organization to benefit from.

## Open Research

Our experiments suggest that curated UX context improves AI-generated UI, and [many teams are already practicing UX-context design in some form](https://www.nngroup.com/articles/context-architecture/). Still, important questions remain, and the answers will shift as models become more capable:

- Which, if any, traditional artifacts improve AI output the most?
- When is raw research data helpful? In what amounts?
- What are the concrete metrics to measure the efficacy of UX context?
- How do the answers change as models improve? A curation decision made for today's models may be wrong for next year's.
- Is there such a thing as too much context?
- How should context be scaled and maintained over time?

You don’t need to wait for the answers to all these questions to engage in UX-context design. Take a sample of insights your research has established about your users. Write them down in a plain text file (likely a markdown file), where your team's AI tools can see them. Work on making your design system machine-readable. Then watch what happens.

UX-context design may become the future of research and design work. If so, the impact of quality research and expert design will be broader than ever, shaping AI-generated work across the entire organization.
