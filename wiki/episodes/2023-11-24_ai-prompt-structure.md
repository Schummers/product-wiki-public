---
type: source
name: "Prompt Structure in Conversations with Generative AI"
created: 2026-07-30
published: 2023-11-24
source_type: article
status: processed
url: https://www.nngroup.com/articles/ai-prompt-structure/
author: Amy Zhang, Emma Cionca, Feifei Liu, Raluca Budiu
raw: raw/sources/2023-11-24_ai-prompt-structure.md
concepts:
  - Prompt Engineering
  - Information Architecture
  - Query Design
  - User Research
  - AI Interface Design
---

# Prompt Structure in Conversations with Generative AI

## Summary

Analysis of 425 AI chatbot interactions identified four key components often present in effective prompts: request, references, format, and framing. Not all prompts include all components, and their importance varies by conversation type. Request-only prompts resembling search queries are inefficient and lead to funneling conversations. Framing requires significant user effort but is essential for well-defined information needs. Users struggle with internal references to previous bot answers, especially on mobile. Designers can support users by providing UI elements that make including these prompt components easier.

## Key Takeaways

- **Request is the core component** — the basic information need (question, command, or incomplete sentence) that is present in most prompts but often lacks sufficient detail for effective responses.
- **References can be internal or external** — internal references quote previous bot answers (difficult on mobile), while external references include pasted text from documents; both benefit from direct-manipulation UI support.
- **Format specifications describe desired output attributes** — length, language, presentation style (list/table/visual), and tone are more common in task-based conversations but often omitted in exploratory ones.
- **Framing provides necessary context** — problem description, goals, user background, and roleplaying prompts reduce ambiguity and query reformulations, though framing requires significant user effort.
- **Special prompt types signal different intents** — "Can you" prompts about bot capability need brief answers, "Give me more" prompts need framing questions, and filler prompts need to be distinguished from actual requests.

## Quotes

> A prompt is a discrete input from the user that initiates or guides the chatbot's response. A conversation with an AI chatbot can have one or more prompts.

> Framing a prompt is a time-consuming task for users. It requires them to think of all the information that the bot might need and then type it out. Some users may find it difficult to explicitly state all the constraints of their query. As a result, many conversations with well-defined information goals start without proper framing.

> The user's information need is like an iceberg. The visible tip of this iceberg is the direct prompt, while the submerged layers are the critical mass that gives the prompt its true shape and direction. The more of these submerged layers is revealed in the prompt, the more effective the AI can be in meeting the user's information need.

## Concepts

- [[Prompt Engineering]] — understanding prompt structure helps users and designers create more effective prompts that include request, references, format, and framing components.
- [[Information Architecture]] — prompts themselves have a structure with distinct components that parallel information architecture principles for organizing complex information.
- [[Query Design]] — effective query design for AI requires more than just stating a request; format and framing specifications dramatically improve response quality.
- [[User Research]] — diary study methodology systematically analyzed actual AI usage patterns to identify prompt structures and their effectiveness across conversation types.
- [[AI Interface Design]] — UI elements can support prompt component entry through suggestion menus, document upload, format selectors, and example prompts.
