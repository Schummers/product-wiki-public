---
type: source
name: "AI Hallucinations: What Designers Need to Know"
created: 2026-07-30
published: 2025-02-07
source_type: article
status: processed
url: https://www.nngroup.com/articles/ai-hallucinations/
author: Page Laubheimer
raw: raw/sources/2025-02-07_ai-hallucinations.md
concepts:
  - "AI Behavior and Limitations"
  - "Trust and Transparency in AI"
  - "AI Product Design"
---

# AI Hallucinations: What Designers Need to Know

## Summary

AI hallucinations—confident but false or nonsensical outputs—are not bugs but inherent artifacts of how generative AI systems work. Because LLMs generate output statistically rather than retrieving facts, they cannot distinguish between correct and incorrect answers. Hallucinations stem from the stochastic nature of language models and from falsehoods in training data. While engineering approaches like lower temperature settings or retrieval-augmented generation offer partial solutions, designers can meaningfully mitigate hallucination impact through interface design that communicates uncertainty, encourages verification, and builds appropriate user trust.

## Key Takeaways

- **Hallucinations are fundamental to how LLMs work, not bugs to be eliminated** — LLMs generate output by predicting statistically likely next words, not by accessing stored facts; they make up answers whether correct or incorrect, so eliminating hallucinations may be infeasible with current technology.
- **Training data quality compounds hallucination risk** — LLMs absorb falsehoods, opinions, sarcasm, and jokes from training data; when training data includes satire (like The Onion), AI systems may treat it as authoritative, leading to confident false recommendations.
- **Generic disclaimers fade into background clutter** — Constantly showing small-font warnings desensitizes users, similar to ubiquitous California Proposition 65 labels; better approach is to show contextually relevant warnings only when uncertainty is high.
- **Communicate uncertainty through first-person language** — Research shows users respond better to "I'm not completely sure, but..." than generalized "It's not clear"; first-person expressions of uncertainty increase appropriate user skepticism.
- **Display confidence scores and multiple perspectives when available** — Show confidence ratings (especially in high-stakes fields like healthcare), highlight inconsistencies when the AI generates multiple responses, or present multiple AI perspectives (debate format) to help users identify potential hallucinations.
- **Present sources and encourage verification** — Displaying sources as drillable links or reference lists encourages fact-checking and primes users to treat AI output as requiring validation, though reference links may create false-halo effects.

## Quotes

> A hallucination occurs when a generative AI system generates output data that seems plausible but is incorrect or nonsensical.

> AI is simply not concerned with truthfulness in the way that humans are. An AI's goal is to output strings (of words, pixels, etc.) that are statistically likely for a given input (such as your prompt).

> Establishing trust with users requires acknowledging AI's limits and fallibility.

## Concepts

- [[AI Behavior and Limitations]] — Explains the stochastic nature of LLMs, how hallucinations arise from statistical prediction rather than fact retrieval, and why current engineering approaches offer partial rather than complete solutions.
- [[Trust and Transparency in AI]] — Emphasizes that users need clear communication of AI uncertainty and limitations; generic disclaimers fail, but contextually relevant uncertainty signals, first-person expressions, and source attribution build appropriate skepticism.
- [[AI Product Design]] — Provides evidence-based design patterns for mitigating hallucination impact: uncertainty language, confidence indicators, multi-response consistency checks, source displays, and verification-encouraging layouts.
