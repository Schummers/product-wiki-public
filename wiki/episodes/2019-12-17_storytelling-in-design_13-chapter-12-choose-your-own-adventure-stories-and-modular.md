---
type: source
name: "Storytelling in Design: Chapter 12. Choose-Your-Own-Adventure Stories and Modular Design"
created: 2026-09-11
published: 2019-12-17
source_type: book
status: processed
url: https://www.oreilly.com/library/view/storytelling-in-design/9781491959428/
author: Anna Dahlström
raw: raw/sources/2019-12-17_storytelling-in-design_13-chapter-12-choose-your-own-adventure-stories-and-modular.md
book: "Storytelling in Design"
chapter: "Chapter 12. Choose-Your-Own-Adventure Stories and Modular Design"
concepts:
  - "Nonlinear Storytelling"
  - "Modular Architecture"
  - "Narrative Structure"
  - "Subplot"
  - "Red Thread"
  - "Content Strategy"
---

# Storytelling in Design: Chapter 12. Choose-Your-Own-Adventure Stories and Modular Design

## Summary

This chapter applies the framework of Choose-Your-Own-Adventure (CYOA) stories to product design, arguing that user journeys increasingly resemble branching narratives rather than linear experiences. Dahlström draws parallels between the modular structure required in CYOA books—where different paths must cohere into a coherent story—and the modular design approach needed in products across multiple devices and entry points. The eight patterns of CYOA structures (Time Cave, Gauntlet, Branch and Bottleneck, Quest, Open Map, Sorting Hat, Floating Modules, and Loop and Grow) offer a vocabulary for understanding and designing complex product experiences where users control their own navigation.

## Key Takeaways

- **CYOA as a design metaphor** — Users navigate products through branching storylines with multiple entry and exit points, similar to CYOA books where readers make choices that determine the narrative path. Unlike traditional stories with one reading order, products must work coherently regardless of where users enter.

- **Modular design enables content fluidity** — Standardized modules and conditional rules allow the same content to adapt across devices and user contexts. Trent Walton calls this "content choreography": designers must orchestrate how content reflows while maintaining narrative clarity and the "intended messages...at any device and at any width."

- **State tracking drives personalization** — Many CYOA patterns rely on tracking state (past choices and actions) to determine what content to show next. In product design, state tracking enables dynamic publishing of tailored experiences based on user data and behavior, moving beyond one-size-fits-all templates.

- **CYOA patterns as design structures** — Sam Kabo Ashwell identifies eight patterns that provide templates for thinking through product complexity: Time Cave (extensive branching), Gauntlet (central thread with side branches), Branch and Bottleneck (rejoin around common events), Quest (modular clusters reconnecting to winning endings), Open Map (reversible travel and exploration), Sorting Hat (heavy early branching, linear later), Floating Modules (no trees and no central plot; modular encounters become available randomly or based on state), and Loop and Grow (central thread looping with unlocking choices over time).

- **Build from story nodes and interconnectedness** — Some key modules are reused again and again, make up larger parts of pages and views, and push the user's experience forward (related posts is Dahlström's example); they are the product's equivalent of a CYOA story's nodes. Changing one shared module may involuntarily change another page where it is used, so designers must track interconnectedness and reuse the same module pattern wherever it makes sense from a content, user and business point of view.

- **Visualize branching to identify all eventualities** — Chooseco's republished *Choose Your Own Adventure* books include maps of each story's hidden narrative structure (an arrow per page, a circle per decision point, a square per ending), and computer scientist Christian Swinehart has visualized CYOA books by the type of ending each branch leads to; Kabo Ashwell and other bloggers have been making such visualizations for years. Dahlström draws the parallel to flow charts, which anyone who has worked on a complex website knows are beneficial for defining and designing for each eventuality.

## Quotes

> Users will increasingly land in the middle of the experiences that we create rather than right at the beginning. Any given page generally has more than one CTA (whether a primary or secondary one), that when clicked or tapped takes the user to a different page or view in the experience.

> The main thing about all of these slight variations or CYOA―is that they allow the user to participate in the story. Unlike novels, where the reader is passive and the author has decided in which order the narrative will be told, CYOA stories (like games) enable the reader to be active, making choices about characters and which way the story will unfold.

Brad Frost, quoted by Dahlström

> Get your content to go anywhere because it's going to go everywhere.

## Concepts

- [[Nonlinear Storytelling]] — CYOA stories and gamebooks exemplify user-driven, choice-based narratives with multiple endpoints. Product experiences increasingly resemble this model as users control their entry points, progression, and exits through branching CTAs and personalized content.

- [[Modular Architecture]] — Modular design and pattern libraries ensure content can adapt across devices and display contexts. Dahlström emphasizes that modules must be purpose-built and interconnected; changing one shared module (e.g., a related-posts component) affects all pages where it appears, so the system must maintain coherence.

- [[Narrative Structure]] — CYOA patterns (Time Cave, Gauntlet, Branch and Bottleneck, Quest, Open Map, Sorting Hat, Floating Modules, Loop and Grow) serve as templates for understanding how branching narratives work. Each pattern describes rules for how branches rejoin, how state affects progression, and what structure suits different story types.

- [[Subplot]] — Product experiences contain a main plot (the primary user goal) and alternative or secondary branches (error states, alternate journeys, related content). CYOA thinking clarifies which subplots rejoin the main thread and which lead to dead ends.

- [[Red Thread]] — The through-line that connects all branches must remain clear. Even as users take different paths, the core promise and theme of the product experience should persist, just as in Gauntlet-structure CYOA stories where one central narrative thread holds the branching together.

- [[Content Strategy]] — State tracking and conditional rules govern which content appears for which users at which moments. On the BBC Olympics project Dahlström's team was not directly involved in defining those rules; her point is that product design should be a cross-discipline collaboration and that someone on the team must own the job of ensuring the right rules are set for what to show when, where and for whom, so a single template works for every athlete, from those with frequent news coverage to those from countries with almost none.
