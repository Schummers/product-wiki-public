---
type: source
name: "Explainable AI in Chat Interfaces"
created: 2026-07-30
published: 2025-12-12
source_type: article
status: processed
url: https://www.nngroup.com/articles/explainable-ai/
author: Megan Chan
raw: raw/sources/2025-12-12_explainable-ai.md
concepts:
  - Artificial Intelligence
  - Interaction Design
  - Design
---

# Explainable AI in Chat Interfaces

## Summary

As users increasingly rely on AI chat outputs for decisions, explanations become critical for forming accurate mental models, preventing misinformation, and enabling trust calibration. However, current LLM explanations are often inaccurate, hidden, or confusing. Three common explanation patterns introduce specific risks: source citations are frequently hallucinated (pointing to nonexistent URLs or unrelated articles) and appear trustworthy despite being invalid; step-by-step reasoning appears transparent but often represents unfaithful rationalizations generated after the fact rather than faithful traces of the model's actual computation; and disclaimers rarely work because users skim text and overlook fine print.

UX teams cannot fix technical limitations of AI models, but they can influence how explanations are presented and interpreted. Design strategies include styling citations prominently and placing them adjacent to claims, using clear action-oriented language in disclaimers (not vague text), avoiding anthropomorphic language that inflates trust, and being honest about model limitations rather than creating false impressions of certainty or transparency.

## Key Takeaways

- **Explanations are critical but LLMs cannot truly explain themselves** — Modern AI models are so complex that even engineers cannot always trace how they arrived at outputs; explanations users see are often inaccurate or hallucinated, yet users place undeserved trust because the outputs appear confident and plausible.
- **Source citations are frequently hallucinated** — Citations often point to nonexistent URLs or unrelated articles that don't support the claim; even when links are real, users rarely click them to verify, so the appearance of citations alone creates false confidence in outputs.
- **Step-by-step reasoning is often unfaithful rationalizations** — These explanations appear transparent but are frequently generated after the fact to justify outputs rather than faithfully representing how the model actually computed the answer; they may omit influencing factors or adjust explanations when users push back.
- **Disclaimers fail because users don't read them** — Fine print and vague language (e.g., "AI-generated, for reference only") are skimmed or skipped; disclaimers only work if placed prominently near the input box, written in clear action-oriented language (e.g., "Please double-check responses"), and included in onboarding to set expectations early.
- **Avoid anthropomorphic language and false transparency** — First-person language (e.g., "I thought about your problem") inflates trust and unrealistic expectations about AI capabilities; use factual, neutral language and be honest about limitations rather than creating impressions of human-like thinking or certainty.

## Quotes

> “I trust [the chatbot] a lot, to be honest… if I want to learn more and see where it got the information from, I could just click the source and keep reading.”

## Concepts

- [[Artificial Intelligence]] — addresses limitations of LLM explainability and the technical reality that modern AI models cannot fully trace their reasoning; distinguishes between faithful model behavior and unfaithful post-hoc rationalizations that can mislead users.
- [[Interaction Design]] — provides UX design strategies for presenting AI explanations (source citations, disclaimers, reasoning walkthroughs) including placement, styling, language, and interaction patterns that increase discoverability and reduce misinterpretation.
- [[Design]] — emphasizes the UX team's role in shaping mental models and building trust in AI tools through transparent communication of limitations, avoiding anthropomorphic language, and guiding users toward critical evaluation rather than blind trust.
