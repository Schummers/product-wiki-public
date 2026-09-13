---
type: source
name: "Evaluating AI-Simulated Behavior: Insights from Three Studies on Digital Twins and Synthetic Users"
created: 2026-07-30
published: 2025-08-15
source_type: article
status: processed
url: "https://www.nngroup.com/articles/ai-simulations-studies/"
author: "Raluca Budiu"
raw: raw/sources/2025-08-15_ai-simulations-studies.md
concepts:
  - "Digital Twins"
  - "Synthetic Users"
  - "Research Methods"
  - "AI Limitations"
---

# Evaluating AI-Simulated Behavior: Insights from Three Studies on Digital Twins and Synthetic Users

## Summary

Three recent academic studies examined whether AI-powered digital twins and synthetic users can replicate real human responses in research contexts. Study 1 (Kim and Lee, 2024) used finetuned LLMs on survey data, achieving 78% accuracy for missing-data prediction but only 67% for new questions; digital twins showed demographic bias favoring higher-SES and white respondents. Study 2 (Stanford-Google team) used prompt augmentation with interview data, achieving over 80% accuracy for survey tasks and remarkably high effect-size correlations (r=0.98) for replicating population-level social science experiments; interview-based twins showed significantly lower bias than demographic-based models. Study 3 (Arora et al., Wisconsin) found synthetic users captured directional trends but underestimated effect magnitudes and showed lower variability than human data. Overall, interview-based digital twins show promise, simpler construction methods yield best results, and digital twins outperform synthetic users, but bias and ethical concerns remain.

## Key Takeaways

- **Interview-Based Twins Excel** — Digital twins built from extensive interview transcripts achieve impressive accuracy (80%+ for survey tasks) and can successfully replicate population-level effects and scientific findings; even shortened transcripts retain high accuracy.
- **Simpler is Better** — Prompt augmentation (the simplest method) yields the best results compared to finetuning; this suggests that rich, personal context is more valuable than algorithmic optimization for capturing individual behavior.
- **Synthetic Users Underperform** — Synthetic users based only on demographic information capture general trends but fail to capture effect magnitude and behavioral variability, limiting their utility for precise predictions.
- **Missing Data Imputation Works** — Digital twins can fill in skipped survey responses and backfill historical data with 78% accuracy, offering a potential solution to the persistent problem of survey attrition.
- **Bias Persists But Can Reduce** — Digital twins show demographic bias favoring certain groups, but interview-based twins demonstrate significantly lower bias (36-62% reduction for political ideology, 7-38% for race) compared to demographic-only models.
- **Context Matters for Bias** — Richer, more personal context helps digital twins generate responses reflecting population diversity; this suggests inclusion requires investment in capturing individual nuance, not just demographic diversity.

## Quotes

> Digital twins work fairly well to replicate both individual-level and group-level human responses.

> The simplest technique for building digital twins seems to produce the best results.

## Concepts

- [[Digital Twins]] — The article reviews empirical evidence on how well digital twins perform at replicating human responses in research.
- [[Synthetic Users]] — Synthetic users are evaluated as less effective than digital twins, particularly at capturing variability and effect magnitudes.
- [[Research Methods]] — The article synthesizes findings from three distinct methodological approaches to building and evaluating AI-simulated users.
- [[AI Limitations]] — Demographic bias in AI models is documented and analyzed as a critical concern, with evidence that richer context can reduce bias.
