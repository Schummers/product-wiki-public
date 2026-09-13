---
type: source
name: "AI Chatbots Discourage Error Checking"
created: 2026-07-30
published: 2025-05-16
source_type: article
status: processed
url: https://www.nngroup.com/articles/ai-chatbots-discourage-error-checking/
author: Pavel Samsonov
raw: raw/sources/2025-05-16_ai-chatbots-discourage-error-checking.md
concepts:
  - "AI Limitations"
  - "Error Checking in AI"
  - "AI Verification Design"
  - "AI Output Quality"
---

# AI Chatbots Discourage Error Checking

## Summary

Large language models (LLMs) generate content prone to hallucinations—outputs that are grammatically correct but factually incorrect. While genAI tools increase productivity through text generation, designers bear responsibility for helping users identify and correct these errors. Currently, most genAI products fail in this responsibility, with design patterns that signal false confidence and discourage verification behavior.

The usability problem stems from both interface design and user behavior. Designers must understand that verifying AI outputs is difficult and time-consuming work that requires users to possess subject-matter expertise, follow multiple verification steps, and build mental models from scratch. Interface design patterns often undermine this effort by treating AI outputs as finished products rather than early drafts.

## Key Takeaways

- **Hallucinations are inevitable** — LLMs extrapolate outside training data to produce truth-like but incorrect outputs, making error-checking a necessary responsibility for product designers.
- **Verification requires substantial effort** — users must review entire outputs, identify items needing verification, validate claims against sources, verify argument logic, articulate corrections, and re-verify responses.
- **AI outputs signal false authority** — confident tone, grammatical correctness, and polished formatting trigger halo effects that cause users to treat early drafts as finished work without adequate review.
- **Users lack expertise** — when AI assists outside their field of expertise, users cannot meaningfully evaluate outputs, leading to trusted hallucinations in domains like law, medicine, and code.
- **Finished products hide problems** — requesting entire documents at once prevents users from building the mental models necessary to identify and troubleshoot errors.
- **Design solutions exist** — prompt questions for critical thinking, highlight referenced source text, and enable inline clarification questions to make error-checking more salient and less costly.

## Quotes

> "People are efficient (not lazy). Users adopt genAI tools precisely because they come with the promise of greater efficiency."

> "Outputs of genAI tools mimic certain attributes that we associate with authoritative sources. Their tone is unerringly confident, regardless of the accuracy of the response."

> "Due to the limited context window and nondeterministic output of LLMs, there is no guarantee that any given error was fixed or new errors were not introduced."

## Concepts

- [[AI Limitations]] — the phenomenon of LLMs producing grammatically correct but factually incorrect outputs that users struggle to identify.
- [[Error Checking in AI]] — the challenging, multistep process users must undertake to verify accuracy of AI-generated content.
- [[AI Verification Design]] — interface design patterns that can reduce interaction cost and encourage users to engage more critically with AI outputs.
- [[AI Output Quality]] — users' tendency to treat unverified AI outputs as finished work due to confident tone and polished formatting.
