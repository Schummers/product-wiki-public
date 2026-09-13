---
type: source
name: "Common-Sense AI Integration: Lessons from the Cofounder of Condens"
created: 2026-07-30
published: 2025-02-21
source_type: article
status: processed
url: https://www.nngroup.com/articles/ai-integration-condens/
author: Alexander Knoll
raw: raw/sources/2025-02-21_ai-integration-condens.md
concepts:
  - "AI Product Design"
  - "AI Limitations"
  - "Practical AI Implementation"
---

# Common-Sense AI Integration: Lessons from the Cofounder of Condens

## Summary

As hype around generative AI has settled, Condens learned to resist overconfident marketing claims and adopt an evidence-backed, cautious-yet-optimistic strategy toward AI integration. Rather than pursuing ambitious claims like "high-quality insights in seconds" or "eliminate bias," the company established design guidelines: scope tasks narrowly and specifically, make AI output easy to verify, enable easy modifications, and ensure core workflows function without AI. Using three key evaluation questions—Does AI have necessary context? Does the task work within AI's technical constraints? Can output be verified and modified?—designers can assess realistic AI applicability across research and other domains.

## Key Takeaways

- **Resist exaggerated AI marketing and establish evidence-backed guidelines** — Ambitious claims about AI capabilities often conflict with reality; define company-wide AI-design guidelines focused on scoped, specific tasks with verifiable output that users can modify.
- **AI requires deeper context than prompts typically provide** — AI often needs industry, company, or research-specific knowledge beyond what a prompt can convey; tasks requiring minimal context (like transcription and translation) excel, while contextual work like UX analysis struggles.
- **LLMs have technical input constraints that degrade quality with large datasets** — GPT-4o accepts up to 128k tokens (roughly 10 hours of transcribed interviews); exceeding limits forces AI to preselect data, potentially introducing bias and reducing result quality.
- **Prioritize AI for small-chunk summarization, semantic search, and quote clustering** — AI succeeds at extracting and organizing small, verifiable units; fails at complex semantic search, ranking, and full-project analysis that require interpretation and deep context.
- **Break complex tasks into smaller verifiable steps with human validation** — Rather than automating full analysis end-to-end, decompose tasks to keep humans in the loop, catch errors incrementally, and avoid accumulating AI mistakes.
- **Maintain core workflows without AI dependency** — Ensure your product functions fully without AI; treat AI as an enhancement that speeds up or simplifies specific steps, not as the foundation of critical functionality.

## Quotes

> While generative AI could meaningfully improve research productivity, many of the claims, especially in marketing messaging, were overstated.

> We lost a customer for our decision to take a more measured approach. The team decided to move to a competitor that was more aggressively integrating new AI features.

> Research findings and recommendations must be backed by evidence, so AI's output in UXR is useless if you can't verify the source.

## Concepts

- [[AI Product Design]] — Outlines a cautious-yet-optimistic approach to AI integration that resists hype, establishes clear design guidelines, and prioritizes evidence over ambitious marketing claims.
- [[AI Limitations]] — Details technical and practical limitations: context requirements, input constraints, verification challenges, and tasks where AI realistically fails, preventing false expectations.
- [[Practical AI Implementation]] — Provides a framework for evaluating task suitability and implementing AI incrementally, keeping humans in the loop, maintaining non-AI fallbacks, and building user trust through verifiable outputs.
