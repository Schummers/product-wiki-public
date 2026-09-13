---
type: source
name: "The Core Skill of Design in the AI Era: Critique"
created: 2026-07-30
published: 2026-06-12
source_type: article
status: processed
url: https://www.nngroup.com/articles/ai-era-critique/
author: Adam Elman
raw: raw/sources/2026-06-12_ai-era-critique.md
concepts:
  - AI Quality Standards
  - Design Critique
  - LLM Evaluation
---

# The Core Skill of Design in the AI Era: Critique

## Summary

Generative AI systems are probabilistic, not deterministic; the same input can produce different outputs. This fundamental difference requires designers to shift from specifying exact behaviors to defining what "good" looks like. The judge-evaluate-iterate loop enables this: designers define judge criteria for what acceptable output is, evaluate actual outputs against those criteria, and iterate implementations. Criteria must be as objective as possible to enable consistent evaluation by humans and AI judges. An F1 score of 0.8 or higher indicates reliable automated evaluation. As AI systems become more prevalent, the ability to set standards for quality—rooted in research and design expertise—becomes a core design skill.

## Key Takeaways

- **Shift from Specification to Definition** — Designers cannot specify exact AI outputs; instead, they must define what "good" looks and doesn't look like through measurable criteria.
- **Judge-Evaluate-Iterate Loop** — Define judge criteria for acceptable output, evaluate actual system output against those criteria, identify failures, and iterate on prompts or training data to improve performance.
- **Make Criteria Objective but Not Arbitrary** — Criteria should be specific enough for consistent judgment across evaluators but grounded in user research and context; vague criteria force evaluators to exercise subjective design judgment.
- **Use LLM as Judge Cautiously** — LLM-based judges enable scalability but must be calibrated against human annotations; an F1 score of 0.8+ indicates reliable performance; always verify with human review.
- **Opacity Persists at Scale** — Even with hundreds of iterations, designers don't fully understand AI systems; critique and iteration become the method for shaping behavior, not comprehensive specification.

## Quotes

> Without being able to specify every possible design decision the model might make, how do we **influence these design decisions to be the "right" ones** — the ones that serve users' needs best, as grounded in research and our understanding of our target users?

> If we reframe our task as designers from specifying exact behaviors to **defining what "good" looks (and doesn't look) like,** we can create mechanisms by which our engineering and data-science partners can evaluate how closely the model's behavior adheres to our intentions.

> the **shift from static, predefined experiences to AI-powered dynamic ones will soon impact every user experience.**

## Concepts

- [[AI Quality Standards]] — Defining quality for AI systems requires objective judge criteria grounded in user research; criteria must be specific enough for consistent evaluation by humans and AI models.
- [[Design Critique]] — In AI systems, critique shifts from reviewing static work to defining and refining quality standards; critique becomes an iterative practice rather than a gate-stage review.
- [[LLM Evaluation]] — LLMs can serve as automated judges if carefully calibrated; F1 scores of 0.8+ indicate reliability; human verification remains necessary to prevent low-quality automated evaluations from degrading performance.
