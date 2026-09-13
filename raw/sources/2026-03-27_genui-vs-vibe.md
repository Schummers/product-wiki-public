---
title: "GenUI vs. Vibe Coding: Who’s Designing?"
date: "2026-03-27"
url: "https://www.nngroup.com/articles/genui-vs-vibe/"
author: "Kate Moran"
topics: [ai]
type: article
---

Since [Andrej Karpathy coined the term “vibe coding”](https://x.com/karpathy/status/1886192184808149383) in early 2025, the concept has taken over the conversation about AI and interfaces. Describe what you want; the AI builds it. There are many variations of that concept, and all of them are relevant to the design community right now, as they impact both how our teams work, and the users they design for.

But vibe coding is not [generative UI (genUI).](https://www.nngroup.com/articles/generative-ui/) The difference is about who makes the decision to build an interactive system or component. This distinction gets blurry in practice, and that’s exactly why it’s worth defining carefully. The line between them determines what we hold the AI accountable for: execution fidelity or design judgment.

## In This Article:

- [Different Flavors of AI-Generated Interfaces](#toc-different-flavors-of-ai-generated-interfaces-1)
- [Who Asks for the Design?](#toc-who-asks-for-the-design-2)
- [The Problem with the “Build-Your-Own-Everything” Argument](#toc-the-problem-with-the-build-your-own-everything-argument-3)
- [GenUI in the Future](#toc-genui-in-the-future-4)
- [Design Implications](#toc-design-implications-5)

## Different Flavors of AI-Generated Interfaces

First, some definitions. The landscape of AI-generated and AI-assisted interfaces includes several overlapping concepts.

> **Generative UI (genUI)** refers to interfaces where the AI system decides to produce a visual or interactive element — the system initiates the design.

We’ve been [thinking](https://www.nngroup.com/articles/generative-ui/) and [talking](https://www.youtube.com/watch?v=4pbYHXAe7Tg) about genUI’s future potential since early 2024, but only recently have examples of true genUI been appearing in real life. Most of those examples [are currently happening within AI chats](https://www.nngroup.com/articles/genui-buttons-and-checkboxes/) (other than highly experimental ones).

> **Vibe coding** means that the user describes what they want and the AI builds it.

The user asks the system to create a particular software product (an application, a website, etc.), often without specifying any implementation details (e.g., specific languages or design patterns to be used). Karpathy described it as fully surrendering control (“forget that the code even exists.”) In practice, many people use the term more loosely to describe any AI-driven development, though purists argue that's a misuse.

> **AI-assisted design** means using AI-based tools within a professional design workflow — generating wireframes, prototyping variations, or exploring layout options as part of building a product for an end-user audience.

In this article, I focus on comparing genUI and vibe coding specifically.

![Flowchart for classifying AI-generated interfaces. First decision: was AI used within a traditional design process? If yes, it's AI-assisted design. If no, the next question is who decided to create the UI. If the AI system decided, it's generative UI (genUI). If the user requested it, it's vibe coding — which falls on a spectrum from vague to detailed specification, where vague prompts give the AI more design decisions and detailed prompts put the AI in an execution role](https://media.nngroup.com/media/editor/2026/03/25/genui.png)

*If an AI system produced an interface for a designer or design team as part of a traditional design process (ideating, testing, evaluating, before launching to customers), that’s AI-assisted design. If not, then consider who decided to create the UI. If the AI system did, it’s an instance of genUI. If the user specifically requested it, then it’s vibe coding. Within vibe coding, there’s a spectrum of specificity that users could employ, from vague to detailed specification.*

## Who Asks for the Design?

Either the AI decides a UI element would serve the user better than text, or the user explicitly asks the system to build something.

In genUI, the user asks a question or states a goal (either explicitly in chat or implicitly by their behavior in a product) and the system decides that the response should include one or more interactive elements (such as checkboxes, interactive data visualization, clarification widgets, or full-blown complex interfaces). The user didn’t request a checkbox. The AI made a judgment call that the experience would benefit from one.

**That judgment call is the defining act of genUI.** The system assessed the situation and determined that the best response would include one or more visual, interactive UI elements. This is a design decision, made in real time, by the AI.

**Vibe coding works differently.** The user initiates and directs the construction. For example:

> “Build me a London trip planner app.”
> 
> 
> 
> “Create a dashboard for my expenses.”
> 
> 
> 
> “Make a quiz about European capitals.”

The user knows they want an interface and asks for one. The AI’s role is execution — translating the user’s intent into a working artifact. That’s valuable, but it’s a different kind of work.

### The Specification Spectrum Within Vibe Coding

Even within vibe coding, there’s a further dimension: **how much does the user specify, and how much do they delegate?**

For example, consider the prompt:

> “Build me a trip planner.”

This leaves the AI significant room to make structural and strategic choices — layout, interaction patterns, information hierarchy.

![A trip planner app generated from a vague vibe-coding prompt. The result is a simple list-based interface showing trip cards (Tokyo Adventure, Italy Road Trip, Costa Rica) and a chronological activity list with names, ratings, times, and category tags. The layout is functional but generic, reflecting the AI's default design choices when given minimal specification.](https://media.nngroup.com/media/editor/2026/03/18/vague-vibe-coding-trip-planner.jpg)

*A vague vibe-coding prompt leaves all the detailed design decisions up to the AI system and can lead to some unpredictable results. (Example built with Claude.)*

But compare that to this prompt:

> “Build me a trip planner with a three-column layout. Left column is a fixed-position interactive map using Mapbox, with custom pins color-coded by activity type — blue for transit, green for outdoors, orange for food, purple for cultural. Clicking a pin opens a compact card overlay on the map showing the place name, a 5-star rating, hours, and a one-line summary. Middle column is the itinerary organized as a vertical timeline grouped by day, with drag-and-drop reordering within and across days. Each item on the timeline shows a thumbnail, the place name, time slot, and estimated travel time from the previous item. Right column is a collapsible details panel that expands when a timeline item is selected — full description, photos in a carousel, address with a copy button, average cost, and a notes field I can type in. Top bar has a date range picker, a trip title I can rename inline, and a share button that generates a read-only link. Filter chips below the top bar for activity type, budget range, and time of day. Everything should persist to local storage so I don't lose work on refresh.”

This version leaves little up to the AI system — it’s executing a designer’s vision. (Most people cannot, and would not try to, imagine or specify this level of detail to reach such an outcome.)

![A trip planner app generated from a highly detailed vibe-coding prompt. The result is a three-column layout: an interactive map with color-coded pins on the left, a day-by-day itinerary timeline in the center, and a detail panel for the selected location on the right. The specificity of the output reflects the user's detailed design specification, putting the AI in an execution role rather than a design role.](https://media.nngroup.com/media/editor/2026/03/18/specific-vibe-coding-trip-planner.jpg)

*A specific vibe-coding prompt can still leave many small details up to the AI system, but puts the AI into the role of executing the user’s design vision. (Example built with Claude.)*

In both cases, the user initiated the construction. But the degree of design judgment the AI exercises varies enormously. This range of specification on the vibe-coding side of the line is why some people get confused by the distinction between vibe coding and genUI.

## The Problem with the “Build-Your-Own-Everything” Argument

Vibe-coding enthusiasts believe that **AI will let everyone build their own custom software for everything they need**(this narrative was [blamed for a big drop in software stocks in February](https://www.cnbc.com/2026/02/04/software-stocks-plunge-us-ai-disruption.html))**.** Why pay for Slack when your company can just generate its own version? Why subscribe to project-management tools when you can vibe code one that fits your exact workflow?

I think back to the hundreds of [user-research](https://www.nngroup.com/videos/what-is-user-research/) sessions I’ve conducted and observed where I’ve seen firsthand how bad most people are at identifying and articulating what they want from a digital product or service. Experienced designers might find it easy to describe the interface they want to build. Most people do not.

**Vibe coding assumes a user who can think in terms of apps, dashboards, and interaction patterns.** That’s a meaningful prerequisite, and not one most people meet.

**GenUI serves the rest.** “Help me plan my trip” is a prompt anyone might type. If the system responds by generating a custom itinerary tool rather than a paragraph of text, someone who would never think to vibe code a trip planner still gets the benefit of an interface designed for their situation. That’s the promise of genUI — not that AI becomes a better code generator, but that it becomes a designer. One that makes the interface decision so the user doesn’t have to know they needed one, let alone try to [envision and articulate what it should be](https://www.nngroup.com/articles/ai-articulation-barrier/) (which is extremely hard for most people).

There’s also an argument for specialized software that the **“build your own everything”** narrative overlooks. Part of the value of a dedicated company building communication or project-management software is the institutional knowledge they accumulate — from years of user research, iterative refinement, and observing how the tool performs across thousands of different organizational contexts. LLMs don’t inherently have that depth baked in. The idea that every team will vibe code its own Slack replacement feels wasteful when the real value of those tools comes from design maturity that no ad hoc prompt can replicate.

This is where genUI carries a higher design burden than vibe coding. **When the user specifies what they want, the AI is accountable for execution quality**— does the thing work as described?

**When the AI decides what to generate, it’s accountable for the design decision.** Right now, if you leave design decisions up to an AI system, you tend to get generic-looking outputs — random layout choices that don’t quite make sense, content errors, visual complexity without clear purpose. GenUI’s success will be measured not by how impressive the generated elements look, but by how well the AI reads the moment.

## GenUI in the Future

In the near future, we’ll start to see the AI customizations moving behind the UI to accelerate and customize interfaces without the visual sparkle icons or beta feature callouts. This is closer to the how [Sarah Gibbons and I originally imagined genUI](https://www.nngroup.com/articles/generative-ui/). Essentially, this is what’s now being called “invisible AI”.

Invisible AI is when AI-driven customization happens behind the scenes of an existing product. The system adjusts the interface based on user behavior, context, and goals without the user explicitly asking for anything.

Think of a productivity tool that surfaces a relevant template before you knew to search for it. The AI is doing design work, but it’s woven into the product so seamlessly that the user just experiences a faster, more relevant interface.

Invisible AI is where genUI’s original vision starts to feel most tangible — and where the evaluation challenges get sharpest. If the user never asked for an interface change and might not even notice one happened, how do we know whether it was the right call?

## Design Implications

Vibe coding and genUI fail in different ways. Vibe coding fails when execution is poor — the thing doesn’t match intent. Broken features, misinterpreted layouts, a trip planner that ignores half your specifications. The user knew what they wanted; the AI just didn’t deliver it.

GenUI fails when judgment is poor — the wrong element was generated, or it shouldn’t have been generated at all. An unsolicited interactive dashboard nobody needed is a design failure even if it’s technically flawless. These are fundamentally different failure modes, and they demand different evaluation approaches.

What is quality in this context? For both vibe coding and genUI, quality is measured in how well the system addressed the user need.

For a **vibe-coded artifact**, high quality means **matching user intent while being usable.** A vibe coder asked for a quiz app and can tell whether the result is what they had in mind.

For **genUI,** quality is whether the response gets the user closer to solving their problem in a way that is as frictionless as possible. It’s harder to assess because the user had no prior expectation and may have nothing to compare against. They asked a question; the system decided an interactive chart was the right response.

But was it the right response? The user might not have the context to know. This means **genUI needs to be evaluated more like traditional UIs:** through user research, task-completion metrics, and satisfaction signals — not just “did it render correctly.”

Finally, and crucially, the audience for genUI is broader than that for vibe coding. Vibe coding empowers people who can articulate what they want built. **GenUI benefits everyone — including users who wouldn’t think to ask for an interface element.** That broader reach comes with a higher design burden: the system must make good decisions on behalf of people who can’t tell it what they want, which is most people.
