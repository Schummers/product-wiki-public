---
title: "Evaluating AI-Simulated Behavior: Insights from Three Studies on Digital Twins and Synthetic Users"
date: "2025-08-15"
url: "https://www.nngroup.com/articles/ai-simulations-studies/"
author: "Raluca Budiu"
topics: [ai, research-methods]
type: article
---

Can AI-powered models replace real people in user research? A growing body of research is exploring whether [digital twins](https://www.nngroup.com/articles/digital-twins/) (generative AI models designed to simulate individual users) and [synthetic users](https://www.nngroup.com/articles/synthetic-users/) (models that mimic broader user groups) can replicate real human responses. In UX, these technologies raise exciting possibilities for scaling research, filling in gaps, and running studies that might otherwise be too slow or expensive.

In this article, I examine three recent studies that put digital twins and synthetic users to the test. I review at how they were built, what kinds of tasks they performed, and how closely their results matched real human data.

## In This Article:

- [TL;DR](#toc-tldr-1)
- [Study 1: Survey-Based, Finetuned Digital Twins](#toc-study-1-survey-based-finetuned-digital-twins-2)
- [Study 2: Interview-Based Digital Twins](#toc-study-2-interview-based-digital-twins-3)
- [Study 3: Synthetic Users](#toc-study-3-synthetic-users-4)
- [Summary of Findings](#toc-summary-of-findings-5)
- [Limitations and Ethical Problems](#toc-limitations-and-ethical-problems-6)

## TL;DR

Don’t care about the full details of each study? Here are the key findings.

- **Digital twins work fairly well to replicate both individual-level and group-level human responses**.**** They can fill in missing answers from incomplete surveys and even backfill data from previous versions of surveys with relatively high accuracy, and, thus, prove promising for reducing survey attrition. When based on extensive interview data, they can also correctly predict human responses and behaviors in a variety of classic-survey questions and economic-behavior games.
- **Interview-based simulated users** seem to produce more accurate models of humans than synthetic users based only on demographic information or on a persona-like description of the user, perhaps because they provide richer, more nuanced data.
- **Digital twins have bias.** Depending on a person’s socioeconomic class, race, or political views, digital twins may perform less accurately. For example, one study found that digital twins were better at predicting white people’s responses compared to other racial groups *.* However, bias may be reduced when the twins are built on extensive interview data.
- **Synthetic users are less impressive:** they may capture trends in human behavior but not the magnitude of the effects or the variability in the human data.
- **The method used for building the AI-based model** may highly impact its performance. Promisingly, the simplest method (augmenting the LLM prompt with rich interview data) seems to yield the best results.

## Study 1: Survey-Based, Finetuned Digital Twins

A 2024 study by Junsol Kim and Byungkyu Lee explored how digital twins can be used to address some common issues in survey-based research. The researchers drew on the [General Social Survey (GSS)](https://en.wikipedia.org/wiki/General_Social_Survey), a long‑running U.S. survey program that has collected responses from about 69,000 adults to more than 3,100 questions since 1972. They [finetuned](https://www.nngroup.com/articles/ai-model-training/) a large language model (LLM) with this rich corpus. Through this process, they retrained the model to consider not just general-purpose, linguistic similarity between words but also domain-specific similarities between questions, individuals, and time periods.

To evaluate the model, Kim and Lee split their survey data into a training and a testing set. They removed 10% of the survey data and directly compared the individual human data with the data predicted by the corresponding digital twin. They tested their twins on **two types of tasks: predicting missing data and predicting answers to new questions.**

#### Missing Data

Survey responses are often incomplete: respondents skip questions or abandon the survey before completing it, especially when it’s long. This missing data makes it harder to run accurate statistical analyses.

A related challenge in longitudinal surveys (run multiple times over years) is backfilling — inferring how someone would have answered a question that wasn’t asked in a past version of the survey. For example, a researcher may be interested in knowing when a user started completing a task on their phone, but that question may have been asked only in recent versions of a survey.

#### New Questions

Sometimes, after running a survey, researchers may realize that they failed to include a relevant question and wonder how survey respondents would have answered those questions.

### Predicting Individual-Level Responses

Kim and Lee found that digital twins were able to achieve a **fairly high 78% accuracy for missing data and backfilling,** meaning the model could successfully infer how a specific person would have answered a question they skipped or were never asked in past surveys. This level of accuracy suggests that digital twins could be particularly valuable for mitigating survey attrition or for completing longitudinal datasets.

However **, the twins were less accurate (67%) when asked to predict how someone would answer a completely new question**— that is, a question not included in the training data. This drop in performance reveals a key limitation, at least for digital twins built with the finetuning method used by Kim and Lee: while they can interpolate within known question sets based on a respondents’ other answers, **they might struggle to extrapolate beyond their learned context**.

### Predicting Population-Level Trends

To obtain general-population trends, Kim and Lee aggregated the individual data obtained from digital twins (while taking into account the overall sampling frames in the demographics of their survey respondents). They looked at how well the resulting population-level measure (such as the proportion of respondents selecting a particular response) obtained from twin data correlated with the corresponding measure from human data. They found **high correlations when digital twins were used for both replacing missing data and backfilling (r=0.98)**, but **lower correlations when digital twins were used to predict responses to new questions (r=0.68).**

### Subgroup Variations

The digital twins were better at predicting the responses of individuals with higher socio-economic status (both in terms of income and education) and of white individuals (when compared with other racial groups). This disparity raises questions about fairness and representation: If digital twins perform less accurately for marginalized groups, **their use could unintentionally reinforce existing biases.**

### Effect of Context Size

Kim and Lee also looked at how much contextual data needs to be included in the model during the finetuning phase to get reasonable accuracy. They found that, especially for the task of predicting missing data, **even eliminating 40% of the available training corpus kept the performance of the digital twins quite high**. This finding has a significant impact on survey attrition: participants could be asked to respond to a subset of questions out of a larger survey, and **digital twins could be used for inferring the responses to the rest.**

## Study 2: Interview-Based Digital Twins

A Stanford‑Google team tried a different recipe: they conducted two‑hour AI‑led interviews with 1,052 U.S. adults and used the resulted transcripts to build digital twins for these individuals. Both the human participants and the twins had to take an extensive battery of tests, that were then used to evaluate the twins’ performance:

- a subset of the GSS survey questions
- [Big-Five Personality Inventory](https://openpsychometrics.org/tests/IPIP-BFFM/) (a 50-question survey which measures 5 broad personality dimensions)
- 5 well-known economic behavior games (such as the [dictator game](https://en.wikipedia.org/wiki/Dictator_game) and the [prisoner’s dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma))
- 5 social-science experiments

(To account for human gaps in self-consistency, participants had to retake the same surveys and experiments two weeks later.)

The responses from the AI-based digital twins were compared to real human data, while controlling for each participant’s self-consistency across the two instances of the experiment.

Unlike the elaborate finetuning method used by Kim and Lee, the Stanford researchers used prompt augmentation to essentially create a single “model” for each individual participant. To mimic an individual’s response, their interview was added to the prompt; if the task that the participant was supposed to complete was multistep, then the previous responses provided by the agent were also included in the prompt. (This would be akin to the concept of having a conversation with a model like ChatGPT).

Additionally, to understand how much of the prediction quality was due to the interviews, the research team also created two simpler types of models for comparison:

- a demographic model, based on participants’ responses to questions about age, gender, race, and political ideology (This model is the equivalent of a typical synthetic user.)

- a persona-based model, based on a brief paragraph that participants wrote about themselves after the interview (This model is somewhere in between a synthetic user and a digital twin.)

### Predicting Individual-Level Data

The table below summarizes how each type of model performed across three types of tasks.

Accuracy | Task | Interview-based twins | Persona-based models | Demographic-based models | GSS survey questions | 0.85 | 0.70 | 0.71 | Big Five Personality Inventory | 0.80 | 0.75 | 0.55 | Economic games | 0.66 | 0.66 | 0.66

**Interview-based twins achieved an impressive accuracy of over 80% for the survey tasks and consistently outperformed both persona-based and demographic-based models,** especially for the GSS and Big Five surveys. Interestingly, for economic games involving decision making, all models performed similarly, suggesting that **interview context might matter less for at least certain types of behavior simulations**.

Even trimmed transcripts (80% shorter) or AI-generated summaries retained high accuracy (0.79–0.83). This suggests that much of the predictive power of these interview-based digital twins comes from the core themes and patterns present in a participant's responses, rather than the full verbatim detail. This finding is especially encouraging: it implies that **even short or summarized interview content may be sufficient for building reasonably accurate models.**

### Predicting Population-Level Effects

Humans and digital twins also participated in 5 classic published social-science experiments that were part of a large-scale replication study. The researchers evaluated whether the data from AI-generated digital twins would point to the same conclusions as the real data from human participants, when analyzed using the original statistical methods described in each study.

**The twins’ and the humans’ data were remarkably similar**: the same 4 out of 5 experiments were successfully replicated with both types of data; neither the twins nor the humans were able to replicate the fifth experiment. Furthermore, **the effect sizes reported from the digital-twin data showed a near-perfect correlation (r = 0.98) with those from the human data**. This suggests that digital twins, when prompted with rich individual context, can accurately reflect not just individual behaviors but also population-level patterns and scientific findings. Thus, digital twins might have promise not only for simulating individual-user responses but also for exploring broader patterns in attitudes, preferences, and behaviors across a user base.

### Interviews Reduce Bias

Bias was measured using a metric known as **demographic parity difference**, which quantifies how much the model's performance varies between the best and worst performing groups. A higher difference indicates greater bias, while a lower number suggests more equitable outcomes.

Researchers applied this metric across tasks such as survey questions, personality predictions, and economic games to assess fairness in political and racial dimensions.

**Interview-based twins showed significantly lower bias than demographic models for groups based on political ideology and race**. For example, political bias was reduced by 36–62% depending on the task, and racial bias saw reductions ranging from 7% to 38% in twins versus demographic models.

Bias | (Min=0, Max=1) | Interview-based twins | Demographic-based models | %Change | Political ideology | GSS | 0.079 | 0.124 | 36% | Big Five (correlation coefficients) | 0.063 | 0.175 | 62% | Economic games | 0.190 | 0.500 | 62% | Racial bias | GSS | 0.020 | 0.033 | 38% | Big Five (correlation coefficients) | 0.110 | 0.170 | 35% | Economic games | 0.040 | 0.043 | 7%

These improvements demonstrate that **richer, more personal context — like a detailed interview — can help digital twins generate responses that better reflect the diversity of the user population**. This means interview-based models may offer a more inclusive and trustworthy alternative to demographic-only modeling approaches.

## Study 3: Synthetic Users

A study by Neeraj Arora and colleagues at the University of Wisconsin-Madison explored several ways in which LLMs could support marketing research. One specific use case they investigated was the use of synthetic users to make population-level predictions. Rather than modeling individuals, this approach involves generating a large group of AI-based synthetic users with demographic profiles that mirror a target population. The researchers then looked at population-level predictions: they analyzed how well the aggregate responses of these synthetic users matched those of real human participants.

(Arora’s paper looked at both qualitative and quantitative synthetic data, and at the use of thematic analysis and AI moderation in marketing, but for the purposes of this article, we will focus only on their synthetic quantitative-data results.)

The researchers used data from a 605-respondent marketing survey about the attractiveness of refrigerated dog food. The respondents rated how unique and likable the product was to them and how likely they were to buy it on a 5-point scale. They also rated specific attributes of the product (e.g., convenience, health, quality) on a 5-point scale and indicated the frequency of purchase.

605 synthetic users were generated to match the respondent distribution in terms of gender, age, income, urbanicity, education, and ethnicity. Then the aggregated data from both humans and synthetic users were compared.

### Predicting Product-Related Attitudinal Data

#### Synthetic Data Followed Human-Data Trends, but Differed Significantly in Magnitude

Overall, both the synthetic users and the humans were fairly unlikely to purchase the product and had relatively negative attitudes towards it, but humans were generally more positive than synthetic users. For example, humans were significantly more likely to purchase (1.66 for humans vs. 1.58 for synthetic users, on a 5-point scale with 1=low) and liked the product significantly more. However, the synthetic users considered the product more unique than the humans did.

Product Rating (1–5, 1=low) | Human Users | Synthetic Users | How likely are you to purchase | 1.66 | 1.58* | How much do you like the product | 1.43 | 1.4* | How unique do you think the product is | 2.12 | 2.48* | *Statistically significant difference

Note, however, that **even though****all these differences are statistically significant, they are fairly small** for many of the metrics. Thus, while synthetic users did not perfectly replicate human responses, **the gaps were narrow enough that their directional accuracy might still be useful in exploratory research or early-stage testing**. However, researchers should remain cautious about relying on synthetic data, especially for making high-stakes decisions.

#### Synthetic Data Had Lower Variability

Another notable difference was that **the standard deviation in the synthetic data was consistently lower than the standard deviation in the human data**. This means that synthetic users tended to cluster more closely around the average response, showing less diversity in their opinions than real users. This lack of variability can be problematic in contexts where capturing the full range of user behavior or attitude is essential — such as identifying edge cases or detecting polarized opinions. For UX research, variability isn't just noise; it might reveal meaningful subgroups that could influence design choices.

Researchers were able to somewhat **increase the variability of responses by enriching the context provided to the model**. They used two strategies: enhancing the model’s memory of past conversations and expanding its access to domain-specific knowledge.

To simulate a more realistic conversation flow, they included prior questions and the model’s earlier responses in the prompt. This approach allowed the model to "remember" its previous answers when acting as a particular respondent, making its behavior more consistent and individualized across tasks.

To supplement domain expertise, the team applied retrieval-augmented generation (RAG) techniques. They gave the model access to an external dataset — interview transcripts from 16 real pet owners discussing their attitudes toward pet products. This additional context helped the synthetic users generate more nuanced and varied responses,

## Summary of Findings

Digital twins and synthetic users are a promising new tool in behavioral science and in UX. As shown in the three studies reviewed:

- When trained on large, domain-specific datasets, **digital twins can accurately fill in individual missing data and historical responses in surveys.** This may enable survey researchers to finally have a reasonable solution to the problem of survey attrition — the high chance that respondents will abandon a long survey.
- When built by augmenting the LLM prompt with extensive interview data, they can achieve remarkable individual-level and population-level predictions of human data. It’s impressive that the **simplest technique for building digital twins seems to produce the best results.**
- Synthetic users’ performance tends to **capture general trends in human behavior but fails at capturing the magnitude of the effects or the variability** in the human data. Their performance can somewhat improve, however, when more contextual information is added to the model.
- **Digital twins** built on specific individual data (as in studies 1 and 2) seem to be able to **capture population-level behaviors****better** than synthetic users built on only generic attributes of a specific user group (as in study 3).
- Both digital twins and synthetic users are **susceptible to biases;** these biases may, however, be overcome in twins based on ample interview data.

These findings reinforce the idea that **digital twins and synthetic users exist on a continuum**. Models based solely on generic demographic or persona-like inputs — such as those used for synthetic users — tend to underperform compared to those enriched with deeper context. That context may be tailored to the individual, as with digital twins, or rooted in detailed domain knowledge, as with synthetic users enhanced through RAG-based techniques.

## Limitations and Ethical Problems

However, AI-generated human models are not a panacea. **Accuracy depends on demographic group, task, and contextual information, as well as on the specific technique used to build the models**. As a practical next step, UX teams interested in exploring this approach should start by identifying data-rich touchpoints they already collect — such as survey histories or user interviews — and experiment with prompt-augmented or [RAG](https://www.nngroup.com/articles/artificial-intelligence-glossary/#retrieval-augmented_generation)-based digital twins before investing in more resource-intensive [finetuning](https://www.nngroup.com/articles/artificial-intelligence-glossary/#fine_tuning).

That said, **the increasing realism and predictive power of digital twins raise ethical questions that researchers and designers must not overlook.** As these AI-generated proxies become more accurate and realistic, it becomes increasingly important to ask how they are built, what data is used, and whether participants have given informed consent for their data to be repurposed in this way. There are also risks of digital twins being used beyond their intended context, potentially leading to misrepresentation, bias, or loss of agency for the individuals they simulate. These issues demand proactive attention from UX teams, not just in how digital twins are designed, but in how they are communicated, deployed, and governed.

**Equally important is the recognition that digital twins should complement, not replace, human-centered research.**(In fact, as emphasized above, successful digital twins are built on extensive *human data*.) While they can extend the reach of UX methods and fill gaps in data, they cannot fully capture the nuance, lived experience, and unpredictability of real users. Continued engagement with human participants remains essential for validating models, uncovering new behaviors, and ensuring the ethical and contextual integrity of the research.

### References

Neeraj Arora , Ishita Chakraborty , and Yohei Nishimura (2025). AI–Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators. *Journal of Marketing,* 2025, Vol. 89(2) 43-70.

Junsol Kim and Byungkyu Lee (2024). AI-Augmented Surveys: Leveraging Large Language Models and Surveys for Opinion Prediction *. arxiv.org,*[https://arxiv.org/abs/2305.09620](https://arxiv.org/abs/2305.09620).

Joon Sung Park, Carolyn Q. Zou, Aaron Shaw, Benjamin Mako Hill, Carrie Cai, Meredith Ringel Morris, Robb Willer, Percy Liang, Michael S. Bernstein. Generative Agent Simulations of 1,000 People.***arxiv.org,*[https://arxiv.org/ abs/2411.10109](http://https://arxiv.org/ abs/2411.10109).
