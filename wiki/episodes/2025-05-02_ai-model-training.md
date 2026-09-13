---
type: source
name: "How AI Models Are Trained"
created: 2026-07-30
published: 2025-05-02
source_type: article
status: processed
url: https://www.nngroup.com/articles/ai-model-training/
author: Tanner Kohler
raw: raw/sources/2025-05-02_ai-model-training.md
concepts:
  - "Generative AI"
  - "Large Language Model"
  - "AI Limitations"
  - "Artificial Intelligence"
  - "AI in Design"
---

# How AI Models Are Trained

## Summary

Understanding how AI models are trained is crucial for forming accurate mental models of LLM capabilities and limitations. The article describes four types of training: pretraining (unsupervised learning on massive internet datasets to learn statistical patterns), finetuning (supervised learning using carefully crafted examples to teach specific tasks), RLHF (reinforcement learning with human feedback using real-world preferences), and specialized training. Each phase contributes different capabilities and introduces different types of bias. LLMs differ fundamentally from search engines: search engines retrieve existing indexed content, while LLMs generate new text word-by-word based on learned patterns, which is why they can hallucinate.

## Key Takeaways

- **Pretraining uses unsupervised learning on vast datasets** — models process terabytes of internet text, code, books to learn statistical patterns (which words follow other words); learn grammar, facts, reasoning abilities, and biases present in data; not learning specific tasks or human-like meaning, just statistical relationships.
- **Finetuning uses supervised learning with curated examples** — researchers create smaller datasets with carefully crafted prompt-response pairs rated on helpfulness, clarity, safety; teaches model to use pretraining patterns in useful, truthful ways aligned to human expectations; bias can enter through raters' perspectives and values.
- **RLHF (Reinforcement Learning with Human Feedback) optimizes for human preferences** — humans rank or choose between multiple model outputs; a separate reward model learns to predict which responses humans prefer; main LLM uses reward model as guide to improve outputs; bias enters if feedback providers aren't representative of user base.
- **LLMs generate text probabilistically, not retrieve it** — fundamental difference from search engines which retrieve indexed content; LLMs construct answers word-by-word based on learned probabilities; explains why LLMs hallucinate confidently stating incorrect information despite training data accuracy.
- **Training has significant environmental and labor costs** — unsupervised learning requires enormous computational power for weeks or months; RLHF and some supervised learning depend on thousands of human labelers worldwide often working low-wage positions with exposure to sensitive content.

## Quotes

> During the pretraining phase, the AI model is *not* learning specific tasks or 'meaning' in the human sense. It's pretty much all statistical relationships: which words are most likely to follow other words in different contexts.

> Think of unsupervised learning like a toddler immersed in language for the first two years of life.

> This generative nature is why LLMs can hallucinate — confidently state incorrect information.

## Concepts

- [[Generative AI]] — describes training approaches specific to generative AI systems and how each training phase contributes to generative capabilities.
- [[Large Language Model]] — details training stages for LLMs, bias sources at each stage, and capability limitations resulting from training approach.
- [[AI Limitations]] — explains hallucination, bias amplification, and capability constraints as direct consequences of training data and methodologies, with bias arising from pretraining (data representation), finetuning (rater perspectives), RLHF (feedback provider demographics), and cumulative amplification across stages.
- [[Artificial Intelligence]] — documents supervised and unsupervised learning approaches and how they contribute different types of knowledge to models.
- [[AI in Design]] — addresses how design-specific training approaches (finetuning on design files, RLHF for design feedback) affect design AI system capabilities and limitations.
