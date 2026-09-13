---
type: source
name: "Context Architecture"
created: 2026-07-30
published: 2026-06-12
source_type: article
status: processed
url: https://www.nngroup.com/articles/context-architecture/
author: Paz Perez
raw: raw/sources/2026-06-12_context-architecture.md
concepts:
  - "Information Architecture"
  - "Context Engineering"
  - "Prompt Engineering"
---

# Context Architecture

## Summary

Context architecture applies information-architecture principles to the entire context window of AI systems. As AI systems shifted from prompt engineering (single instructions) to context engineering (orchestrating multiple signals), the need emerged for a design discipline around how that context is structured. Context includes system instructions, retrieved knowledge, skills, tools, and memory. Information architects structure this context so AI systems can reason more effectively. Context architecture asks: what concepts belong, how are they labeled, how do they relate, what should be remembered, what should never be done? Good context architecture reduces ambiguity and cognitive load on the model, enabling more accurate and efficient responses.

## Key Takeaways

- **From Prompt to Context Engineering** — Early success relied on well-written prompts; context engineering realized that prompts alone are insufficient; context includes instructions, knowledge, tools, memory, and state all working together.
- **Context Ecosystem Is Complex** — Context includes system instructions, retrieved knowledge via RAG, skills, tools, long-term and short-term memory, and user prompts; every element competes for the model's attention.
- **Information Architecture Principles Apply** — Structure context so AI systems can navigate reliably; establish hierarchies to prioritize information; use categorization and labeling that align with user language, not engineering terminology.
- **Improve Findability Through IA** — Skills and tools must be discoverable; clear taxonomy, controlled vocabulary, and unambiguous naming help agents select the right tool; poor labeling leads to wrong tool selection and unnecessary steps.
- **Align System Model to User Mental Model** — Users navigate systems based on mental models; misalignment between internal terminology and user language causes agents to perform wrong actions; context architecture bridges this gap.

## Quotes

> Context is not just a list of system prompts; it is an ecosystem of information that needs to be discovered and selected.

> The challenge is not only the access to information. It is making that information meaningful, structured, and usable for both humans and machines.

> These are not neutral decisions. They determine how meaning is constructed and how outcomes are produced. This is design work, and it needs to be treated as such.

## Concepts

- [[Information Architecture]] — IA principles—structure, hierarchy, taxonomy, labeling, findability—apply to designing context for AI systems; good IA reduces ambiguity and cognitive load on the model.
- [[Context Engineering]] — Context orchestration involves coordinating multiple information sources and signals; engineers build the infrastructure; architects design the structure.
- [[Prompt Engineering]] — Prompt design is evolving into context design; clear structure, labeling aligned with user language, and strategic prioritization matter as much as content.
