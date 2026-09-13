---
type: source
name: "Designing for Long Waits and Interruptions: Mitigating Breaks in Workflow in Complex Application Design"
created: 2026-07-30
published: 2021-09-05
source_type: article
status: processed
url: https://www.nngroup.com/articles/designing-for-waits-and-interruptions/
author: Kate Kaplan
raw: raw/sources/2021-09-05_designing-for-waits-and-interruptions.md
concepts:
  - "Progress Indication"
  - "Cognitive Load"
  - "Task Resumption"
---

# Designing for Long Waits and Interruptions: Mitigating Breaks in Workflow in Complex Application Design

## Summary

Users of complex applications frequently encounter long waits (processing data, running models, querying databases) and interruptions that break their workflow. Five guidelines mitigate the frustration of these unavoidable waits: clearly indicating progress completed and time remaining, contextualizing success messages with details about what occurred, enabling user-generated notes within the system, providing quick access to historical content, and allowing processes to run in the background. These strategies acknowledge that complex-app users must step away during long processes, incurring cognitive load upon return; they support task reentrance and reduce uncertainty about system status.

## Key Takeaways

- **Detailed Progress Indicators** — For waits exceeding 10 seconds, provide percentage completion or steps remaining rather than generic loops; users need information to decide whether to wait or begin other tasks.
- **Contextualized Success Messages** — Success dialogs should include processing time (start time, end time, duration), what occurred during processing (records created, validations passed, errors), and links to relevant content; this helps users recover context after stepping away.
- **External Memory Support** — Allow users to create notes and comments within workflows to track their thought processes; without this, users resort to maintaining external spreadsheets, creating additional burden.
- **Recent Content Access** — Provide quick access to recently viewed files or pages with clear labels; previews help users quickly identify the correct file, especially when files take time to load or have system-generated names.
- **Background Processing** — Allow lengthy processes to run in the background so users can continue other work; modal success dialogs are appropriate for background processes because users are not actively monitoring them.

## Quotes

> Regardless of circumstance, adhering to the following 5 guidelines can mitigate the frustration that complex-app users experience during long waits or interruptions in their workflows:

> Long waits are often inevitable during complex workflows, but there are several strategies for helping users cope with the duration of these waits and supporting task reentrance at the end of them:

> Users of complex applications often analyze large data sets, run complex models, or query robust information sources — all processes that take a substantial amount of system-processing time.

## Concepts

- [[Progress Indication]] — Progress indicators communicate system status during long waits; effective indicators show percentage complete, time remaining, or steps completed rather than generic loading animations, helping users make informed decisions.
- [[Cognitive Load]] — Complex-app users experience increased cognitive load when interrupted by long waits; supporting context recovery through notes, success dialogs, and recent content access reduces the mental burden of task resumption.
- [[Task Resumption]] — Task resumption is returning to work after an interruption; complex applications should minimize resumption costs through historical content access, contextual information, and support for recording thoughts and decisions.
