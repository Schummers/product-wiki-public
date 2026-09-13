---
type: source
name: "Solving Product Design Exercises: 3.2. A self-publishing platform for Amazon"
created: 2026-09-10
published: 2018-02-12
source_type: book
status: processed
url: "https://productdesigninterview.com"
author: Artiom Dashinsky
raw: raw/sources/2018-02-12_solving-design-exercises_19-3-2-a-self-publishing-platform-for-amazon.md
book: "Solving Product Design Exercises"
chapter: "3.2. A self-publishing platform for Amazon"
concepts:
  - "Design Exercise"
  - "Persona"
  - "Problem Framing"
  - "Context of Use"
  - "Prioritization"
  - "Business Impact"
---

# Solving Product Design Exercises: 3.2. A self-publishing platform for Amazon

## Summary

This chapter presents a worked example of applying a seven-step design framework to a self-publishing platform for Amazon. The exercise demonstrates how to approach a large, multi-step product problem by systematically understanding business goals, audience segments, customer context, and constraints before proposing a solution. Dashinsky designs a dedicated web application that simplifies the publishing process by guiding authors through essential and optional steps via a sidebar-driven interface, while addressing the anxieties of first-time authors and the efficiency needs of experienced publishers.

## Key Takeaways

- **Audience segmentation by lifecycle** — First-time authors require more guidance and reassurance due to anxiety about the unfamiliar publishing process, while recurring authors prioritize efficiency. The same product must serve both by offering contextual help for newcomers and streamlined workflows for experienced users.
- **Sidebar navigation with progress feedback** — A sidebar organized into "Essentials" and "Tools" sections provides both navigation and a visual progress indicator, answering "What's my progress?" and "What's next?" at a glance to motivate authors through a potentially overwhelming multi-step journey.
- **Master-detail layout with reusable components** — Many of the ten publishing steps need the same kinds of interaction, so the candidate proposes building a design system of five reusable blocks (forms, file upload, marketplace, calculator, preview) and adjusting them per use case, which makes the product easier to develop. The brief itself is framed as a test of working inside Amazon's existing design system.
- **Marketplace model for specialist services** — Instead of building in-house editorial and design capabilities, the platform connects freelance designers, editors, and reviewers, reducing Amazon's operational burden while giving authors vetted options for critical tasks.
- **Data-driven success guidance** — Leverage Amazon's sales data to develop best-practice guidelines for each aspect of publishing, suggesting which features correlate with successful books and proactively recommending actions like adding illustrations if the data supports it.
- **Auto-save and completion flow** — Auto-saving all changes removes pressure on authors and creates a low-friction experience; a prominent call-to-action appears after all essential steps are complete, leading to a celebratory success screen that acknowledges the milestone.

## Quotes

> Book publishing involves a lot of aspects — working with manuscripts, graphics, communicating with vendors and more. I think building a web app allowing authors to work on these tasks from their laptop/desktop, as they are already used to, would provide them with the best experience.

> For example, Amazon could determine, from their sales data and reviews, if using illustrations makes non-fiction books more successful. If there appears to be a correlation, they could suggest authors include illustrations.

> To reduce the pressure on the customer of constantly having to save their progress, we should auto-save all the data changed unless the user chooses "Cancel changes".

## Concepts

- [[Design Exercise]] — A worked example of the framework on a large-scope brief, running goal, audience, context and needs, ideas, solve and measure; Step 5 is skipped outright, the chapter stating that the web app was already settled in Step 4 so there is nothing left to prioritise.
- [[Persona]] — The chapter identifies two distinct personas (first-time vs. recurring authors) within the 30-80 age range, noting their different emotional states and information needs, and designs the product to serve both simultaneously with different levels of guidance.
- [[Problem Framing]] — The author frames the problem not as "how to build a self-publishing tool" but as "how to minimize entry barriers for authors while increasing Amazon's marketplace supply," starting from business goal and working toward customer needs.
- [[Context of Use]] — Dashinsky maps when and where authors work (laptops and desktops from home, coffee shops, airports, co-working spaces) and their emotional state (excited and anxious), using this to justify a web app for desktop publishing and mobile for post-launch tracking.
- [[Prioritization]] — The product prioritizes author anxiety reduction for new users and efficiency for experienced ones, with sidebar sections explicitly split into "Essentials" and "Tools" to reduce cognitive load and focus authors on required steps first.
- [[Business Impact]] — The chapter closes by proposing metrics (completion rate, step-wise completion, feature retention) that directly measure whether the design reduces barriers and increases Amazon's revenue through higher marketplace supply.
