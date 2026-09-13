---
title: "Digital Twins: Simulating Humans with Generative AI"
date: "2025-08-01"
url: "https://www.nngroup.com/articles/digital-twins/"
author: "Raluca Budiu"
topics: [ai]
type: article
---

Let’s face it: research with real users takes time. Recruiting participants, collecting data, and waiting for results are often the most time-consuming stages of the research process. One of the most exciting and promising avenues for improving efficiency across domains —including user research — is the use of **generative AI**.

Can research be made faster or more scalable with AI? Elsewhere, I’ve outlined the types of [studies our field must undertake](https://www.nngroup.com/articles/genai-ux-research-agenda/) to understand how generative AI can support UX and behavioral research. Today, I focus on one particularly promising — and sensitive —direction: **simulating human behavior using AI models.**

## In This Article:

- [What Is a Digital Twin?](#toc-what-is-a-digital-twin-1)
- [Synthetic Users vs Digital Twins: A Continuum](#toc-synthetic-users-vs-digital-twins-a-continuum-2)
- [Use Cases for Digital Twins](#toc-use-cases-for-digital-twins-3)
- [How Are Digital Twins Built?](#toc-how-are-digital-twins-built-4)
- [But Do Digital Twins Work?](#toc-but-do-digital-twins-work-5)
- [Are Digital Twins Ethical?](#toc-are-digital-twins-ethical-6)

## What Is a Digital Twin?

A **digital twin** is a generative model — typically based on a [large language model (LLM)](https://www.nngroup.com/articles/artificial-intelligence-glossary/#LLM) — that attempts to act as a proxy for a particular person. This model can respond to new questions or situations in roughly the same way the individual would.

Think of it as an **artificial cognitive clone:** a system that can complete surveys, predict choices, or interact in real time on behalf of a real individual. The twin is trained or primed with personal information — such as demographics, past survey responses, interviews, behavioral logs — and can be used for predicting **individual-level** behavior (what that particular individual will do) and **population-level****behaviors**(what a user group would do)**.**

## Synthetic Users vs Digital Twins: A Continuum

When simulating humans with AI, we can distinguish between two broad approaches:

- **Synthetic users** represent population segments or archetypes (e.g., “medical professionals in Latin America”). They’re generated from group-level descriptors and are used to make population-level predictions.
- **Digital twins** represent *specific individuals*, modeling their likely thoughts and actions. These representations of individuals can be used to predict either individual-level or population-level behaviors.

In practice, however, the distinction between digital twins and synthetic users is blurred. Imagine a continuum:

- At one end, a synthetic user is built from attributes that many real people share
- At the other end, a digital twin is based on information gathered about very few people — often, just one.

![A chart. On the left end (labeled "less information"), three icons of people with the label: "Synthetic user: Generic, based on a group." The right side (labeled "More information"), has one icon of a person. It is labeled "Digital twin: Specific, based on one person."](https://media.nngroup.com/media/editor/2025/07/29/digital-twinv-synthetic-user_final.png)

*Synthetic users and digital twins are both ways of modeling human behavior with AI. Synthetic users represent population segments and are based on generic information about that segment, whereas digital twins represent particular individuals and are built on lots of data specific to that individual.*

Sometimes, synthetic users may be generated based on a little more than demographic information — for example, a generic persona-like description. And the less specific information is used to create digital twins, the less likely they are to match a specific individual and to act as synthetic users corresponding to a larger group.

## Use Cases for Digital Twins

### Predicting Individual Preferences and Behaviors

Being able to forecast how a particular person will respond to a stimulus has clear value in UX, marketing, and social sciences. Examples include:

- **Missing-data imputation:** Fill in skipped survey items using the twin’s predictions.
- **Shorter surveys:** Ask respondents only a subset of questions, then infer the rest via the twin.
- **Hard-to-reach participants:** Use data from one-time interviews to build twins that stand in for groups that are expensive or impractical to recruit repeatedly and follow over time.
- **Journey orchestration:** Anticipate user reactions to different touchpoints and tailor experiences accordingly.
- **Usability issues:** Preemptively identify usability hurdles or emotional reactions to interface changes.

### Predicting Population-Level Trends

Although twins are constructed at the individual level, their outputs could be aggregated to reveal broader population-level trends. They would enable researchers to simulate how entire audiences might respond to a new feature, design, or message — without needing to recruit hundreds or thousands of people in advance.

By applying sampling weights that reflect a target population's structure, digital twins can approximate survey representativeness and support large-scale behavioral testing before any real-world rollout.

## How Are Digital Twins Built?

The construction of a digital twin depends on how much contextual information is available about the individual and how that information is integrated into the model.

The individual-specific contextual information could include:

- Demographic attributes
- Stated preferences and beliefs, often in the form of a persona-like summary
- Prior survey responses
- Interviews
- Behavioral data — such as previous websites that a person has visited or products they purchased

Once gathered, this contextual information needs to be fed into the model. That can be done in several ways. The chosen route depends on budget, data availability, the level of technical expertise available, and how narrowly the digital twins will be used.

### Prompt Augmentation

This approach builds the twin by adding the corresponding personal context to the LLM prompt. While this is easy to implement, it can run into prompt-length limitations when the individual context is too large.

### Retrieval-Augmented Generation (RAG)

With this method, all the relevant information (such as the individual’s history along with other domain-specific information) is encoded in an external data source. For each prompt, the most relevant documents in the external data sources are retrieved and appended to the prompt, then passed to the LLM.

This allows models to dynamically access rich data — like interview transcripts or response histories — without overloading the prompt.

### Finetuning

This approach is the most costly — it involves retraining the model using a smaller domain-specific dataset (e.g., responses from thousands of users of the same product), to adapt it to a particular set of tasks. This process can result in internal model weights that are optimized for this particular domain.

As a result, an individual’s responses may be predicted not only based on their own past actions but also on the past actions of individuals with similar behavior patterns or opinions within the same domain. For example, the model may predict that a particular dog lover would like a fenced yard based on the fact that many dog lovers in the training set had fenced yards.

## But Do Digital Twins Work?

In our evaluations of synthetic users, we haven’t been very impressed with the performance of currently available simulated humans. They tend to fail to capture the messy, nuanced nature of real human behavior. We find them useful when treated as a desk research tool, rather than considering them as a substitute for talking to your actual customers.

Hypothetically, it’s possible that digital twins may produce more realistic results because they’re based on the nuanced complexity of a single real individual, instead of the aggregated, averaged data representing a group.

In my next article in this series, I’ll review some recent academic studies looking at the predictive power of digital twins and synthetic users; broadly speaking, these studies show a lot of promise for digital twins, especially for practical applications such as filling in missing data in surveys and predicting survey answers based on extensive interviews.

## Are Digital Twins Ethical?

**Digital twins raise serious ethical questions that researchers and designers must not overlook.** How should consent be managed when reusing a participant’s data to create a long-lasting proxy? Would users agree to having a digital version of themselves created to fill out surveys or predict further behavior?

What are the risks of misrepresentation, especially if a twin is used in contexts beyond its original intent? And how do we ensure that models don’t perpetuate or amplify existing biases in data collection?

These questions are not merely academic. As digital twins move from experimental tools to operational ones, the UX community has a responsibility to address issues of transparency, privacy, and fairness. Used thoughtfully, digital twins could complement traditional methods and extend the reach of UX research into new, faster, and more adaptive territory — but only if we proceed with care and clarity about their limitations.
