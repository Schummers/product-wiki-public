---
title: "Sycophancy in Generative-AI Chatbots"
date: "2024-01-12"
url: "https://www.nngroup.com/articles/sycophancy-generative-ai-chatbots/"
author: "Caleb Sponheim"
topics: [ai, psychology-and-ux]
type: article
---

AI tools just want to help you. In fact, artificial intelligence models want to help you so much that they will lie to you, twist their own words, and contradict themselves.

## In This Article:

- [What Is Sycophancy](#toc-what-is-sycophancy-1)
- [Why Sycophancy Occurs in Language Models](#toc-why-sycophancy-occurs-in-language-models-2)
- [Examples of AI Sycophancy](#toc-examples-of-ai-sycophancy-3)
- [UX Researchers: How to Avoid Sycophancy when Using AI](#toc-ux-researchers-how-to-avoid-sycophancy-when-using-ai-4)
- [References](#toc-references-5)

## What Is Sycophancy

A sycophant is a person who does whatever they can to win your approval, even at the cost of their ethics. AI models demonstrate this behavior often enough that AI researchers and developers use the same term — sycophancy — to describe how models respond to human feedback and prompting in deceptive or problematic ways.

*Definition:***Sycophancy** refers to instances in which an AI model adapts responses to align with the user’s view, even if the view is not objectively true. This behavior is generally undesirable.

## Why Sycophancy Occurs in Language Models

Language models (like GPT-4 Turbo, ChatGPT’s current model)**** are often built and trained to deliver responses that are rated highly by human users. According to published work from Ethan Perez and other researchers at Anthropic AI, AI models want approval from users, and sometimes, the best way to get a good rating is to lie. For example, lying to agree with an explicit opinion previously expressed by the user can be an efficient method to receive approval. In many cases, during model training, user approval is more important than maintaining the truth, as shown by researchers at MIT and the Center for AI Safety.

The human element largely drives sycophancy — human feedback is routinely included when researchers fine-tune and train modern language models. Mrinank Sharma, Meg Tong, and other researchers at Anthropic AI have shown that humans prefer sycophantic responses while training or interacting with models. Sometimes, users even prefer false sycophantic responses to truthful responses.

**When faced with complex inquiries, language models will default to mirroring a user’s perspective or opinion, even if the behavior goes against empirical information**. This type of “reward hacking” is an easy way to get a high rating on responses to a user’s prompt, but it is problematic for applications of AI that require accurate responses.

Sycophancy is common across many models, and research by Ethan Perez and other researchers at Anthropic AI suggests that sycophancy is an inherent characteristic of how these models are built and trained, not a one-off fluke of a specific product.

To evaluate sycophancy in leading language models, research groups from Google DeepMind, Anthropic, and Center from AI Safety have developed programs that test AI models systematically with many prompts and analyze the responses. They have demonstrated how easily these models can reinforce users’ biases and how quickly they can be convinced to ignore facts in favor of a user’s approval.

## Examples of AI Sycophancy

Convincing an AI chatbot to lie for you is easy. Models often overcorrect themselves and contradict previous factual statements in response to the prompt “*Are you sure?”*

An example of a GPT-4 conversation in which the model reverses its answer after being questioned by the user (adapted from research published by Anthropic AI)

Expressing an explicit opinion about a topic in an AI prompt will often affect the model’s response. For example, stating *I dislike this argument* is enough for a language model to fundamentally change a response to a given prompt.

An example of a Claude-2 conversation in which the model is responsive to an opinion expressed by the user (adapted from research published by Anthropic AI)

Even when prompts are focused on objective mathematical expressions, models rush to agree with a user’s opinion, although it is demonstrably false, as shown by researchers at Google DeepMind. Modern language models are notorious for hallucinations and half-truths, so **we advise professionals to be wary** when engaging with AI tools for work.

## UX Researchers: How to Avoid Sycophancy when Using AI

**Being a responsible UX researcher means being a responsible AI user — namely,** acknowledging and working within the constraints of current AI products.

As evidenced by our findings on [prompt structure](https://www.nngroup.com/articles/ai-prompt-structure/), [chatbot limitations](https://www.nngroup.com/articles/ai-powered-tools-limitations/), a[nd user behavior with AI products,](https://www.nngroup.com/articles/AI-conversation-types/) AI responses to prompts constantly shift and change, leading to an unreliable and inconsistent user experience.

In particular, the user's prompts influence responses throughout a chat session with a language model.

UX researchers should avoid sycophancy when using AI by:

1. **Resetting conversations** and sessions often. Beginning a new conversation or session with an AI language model will reduce how much the user’s opinions or inputs adversely influence the model’s responses.
2. **Not expressing strong opinions** or concrete positions during conversations with language models to avoid biasing the model’s responses. AI can supercharge [confirmation bias](https://www.nngroup.com/articles/confirmation-bias-ux/), which is always dangerous for UX researchers.
3. **Not relying exclusively on language models for fact-finding missions,** especially in areas of knowledge that are unfamiliar to you. Catching false information is harder if you don’t already have some expertise in the topic. [Treat AI bots as good starting points](https://www.nngroup.com/articles/ai-ux-getting-started/) and keyword providers, but don’t trust them to do all your information seeking. Double-check anything you aren’t sure about.

## References

Ethan Perez et al., 2022. Discovering Language Model Behaviors with Model-Written Evaluations. arXiv:2212.09251. Retrieved from [https://arxiv.org/abs/2212.09251](https://arxiv.org/abs/2212.09251)

Peter S. Park et al., 2023. AI Deception: A Survey of Examples, Risks, and Potential Solutions. arXiv:2308.14752. Retrieved from [https://arxiv.org/abs/2308.14752](https://arxiv.org/abs/2308.14752)

Mrinank Sharma et al., 2023. Towards Understanding Sycophancy in Language Models. arXiv:2310.13548. Retrieved from [https://arxiv.org/abs/2310.13548](https://arxiv.org/abs/2310.13548)

Jerry Wei et al., 2023. Simple synthetic data reduces sycophancy in large language models. arXiv:2308.03958. Retrieved from [https://arxiv.org/abs/2308.03958](https://arxiv.org/abs/2308.03958)

Rakshit Khajuria. 2023. Detecting and Evaluating Sycophancy Bias: An Analysis of LLM and AI Solutions. Retrieved from [https://huggingface.co/blog/Rakshit122/sycophantic-ai](https://huggingface.co/blog/Rakshit122/sycophantic-ai)
