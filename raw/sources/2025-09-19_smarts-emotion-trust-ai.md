---
title: "Prioritize Smarts over Sentience to Increase Trust with AI"
date: "2025-09-19"
url: "https://www.nngroup.com/articles/smarts-emotion-trust-ai/"
author: "Evan Sunwall"
topics: [ai]
type: article
---

A common concern from attendees of our [Designing AI Experiences](https://www.nngroup.com/courses/designing-ai-experiences/) course is how to help users develop trust with artificial intelligence (AI). One technique that designers are frequently tempted to use is [anthropomorphism](https://www.nngroup.com/articles/eliza-effect-ai/). The rationale is that the more the user sees the AI as a conscious, human-like entity, the more likely they’ll trust it.

But is anthropomorphism an effective tactic? A recent study offers intriguing data about how our beliefs about an AI’s “mind” predict our willingness to trust and rely on its advice.

## In This Article:

- [About the Study](#toc-about-the-study-1)
- [Smarts Builds Trust, Simulated Emotions Erode It](#toc-smarts-builds-trust-simulated-emotions-erode-it-2)
- [Emerging Research on the Implications of Emotional AI](#toc-emerging-research-on-the-implications-of-emotional-ai-3)
- [Competent Doesn’t Mean Impersonal](#toc-competent-doesnt-mean-impersonal-4)
- [Practical Advice for UX Professionals](#toc-practical-advice-for-ux-professionals-5)

## About the Study

Psychology researchers Clara Colombatto, Jonathan Birch, and Stephen Fleming wanted to unravel the broad concept of anthropomorphism and explore its effect on trust. They recruited 410 US participants for an experiment with two counterbalanced parts in a [within-subjects](https://www.nngroup.com/articles/between-within-subjects/) format.

### Part A: Preconceived Perceptions of AI (Self-Reported Data)

The researchers asked about their beliefs regarding ChatGPT’s mental abilities. Specifically, the researchers asked questions around:

- **How intelligent is ChatGPT?** Can it plan, reason, decide, or remember?
- **Does ChatGPT experience emotions?** Does it have the capacity for emotions, feelings, or consciousness?

### Part B: AI-Informed Decisions (Behavioral Data)

In addition to these perception questions, the researchers gave participants a simple quiz with 40 general-knowledge questions on population estimates for countries, like: "Does Colombia or Germany have more people?"

Participants were then presented with information that represented “ChatGPT’s choice” on the quiz and were given the opportunity to change their answers. The researchers **measured how often people “took ChatGPT’s advice”**(i.e., changed their answers based on the AI’s choice). Participants were not told if their quiz answer was correct, but 10% of the time, they were asked to recall ChatGPT’s advice for the previous quiz question as a quality-control measure, and a participant’s data was excluded if they failed to answer 70% of these recall questions correctly.

Unbeknownst to the participants, **ChatGPT’s choice was not actually AI-generated.** It was scripted by the researchers. (This scripting was to control for the [confounding variable](https://www.nngroup.com/articles/confounding-variables-quantitative-ux/) of unpredictable accuracy from live ChatGPT responses and ensure that any differences in trust were due to the participant’s beliefs about ChatGPT, rather than the quality of a particular response.)

### Final Trust and Usage Ratings (Self-Reported Data)

At the end of the experiment, participants reported their trust in ChatGPT on this population-estimation task and their overall trust in it. They also reported on the frequency of usage of digital assistants (Alexa, Siri), AI companionship apps (Character AI, Replika), and general-purpose AI chatbots (ChatGPT, Gemini, Claude).

## Smarts Builds Trust, Simulated Emotions Erode It

A regression analysis of the data revealed two key findings about the link between what people believe about AI, and how much they’ll take its advice.

- **Final trust ratings were correlated with advice taking** (r=0.58, p < 0.001), meaning that participants who reported trusting ChatGPT were more likely to change their answers to match the AI’s. Perceptions of intelligence were positively related to taking ChatGPT’s advice (B = 0.31, p < .001). **As participants’ perception of ChatGPT’s intelligence increased, their willingness to accept its advice increased significantly.**
- Perceptions of emotion were negatively related to taking ChatGPT’s advice (B = –1.04, p = .042). **As participants' perception of the AI's capacity for emotion increased, their willingness to accept its advice decreased slightly.**

The researchers speculate that people may be more willing to trust an AI's factual advice when they associate traits like memory and reasoning with it, viewing it as more reliable. In contrast, users may trust AI less when they perceive it as having more emotional traits, and thus more unstable, subjective, or less analytical.

The bottom line is: When it comes to taking AI’s advice, trust is essential. **Users are more likely to follow the AI’s advice if they perceive AI as smart, rather than emotional.** Thus, if you want to build trust, you should work on creating the impression of intelligence (by providing accurate, relevant answers) instead of just creating the illusion of emotional rapport.

## Emerging Research on the Implications of Emotional AI

More emerging research suggests that making AI emotional has serious risks beyond user trust and in other contexts.

### Training for Warmth and Empathy Makes AI Less Reliable

In the Colombatto et al. study, ChatGPT’s advice was scripted to be about 62% accurate to simulate average human performance. But what if the AI's personality itself affects its reliability?

A recent preprint study by Lujain Ibrahim, Franziska Sofia Hafner, and Luc Rocher found exactly that. The researchers finetuned several LLMs to make them produce warmer and more empathetic responses, which revealed a significant [tradeoff](https://www.nngroup.com/courses/design-tradeoffs/). **These 'warm' models were far less reliable in their responses and had****error rates 10%–30% higher** than the originals. While finetuning represents a deeper level of model customization than most product teams undertake, the researchers also tested adjusting the LLM’s behavior through a system prompt, which is a far more likely customization approach. The results were similar: **instructing the base models to be warmer also produced a 12%–14% drop in reliability**.

These warmer models were more likely to promote conspiracy theories, provide incorrect facts, and offer problematic medical advice. **Making the AI more caring made it less competent**!

### AI Is Untrustworthy in Sensitive Contexts

The Colombatto study acknowledged that it explored trust during low-stakes factual tasks, leaving the possibility of different results in emotionally sensitive contexts, like companionship or mental health. But there is research to suggest it is unwise there, too. A preprint by Jared Moore, Declan Grabb, and colleagues investigated the high-stakes scenario of using LLMs as replacements for mental-health providers. They found that LLMs' tendency to [sycophancy](https://www.nngroup.com/articles/sycophancy-generative-ai-chatbots/) led them to encourage delusional thinking and mishandle severe mental-health crises.

The Ibrahim study found that **warm, empathetic models were significantly more likely to be sycophantic,** which is precisely the quality that makes them untrustworthy and potentially harmful for mental-health needs. **An empathetic and emotional AI performs poorly even in contexts where it may seem beneficial.**

## Competent Doesn’t Mean Impersonal

The insights from this research may raise a few misconceptions about anthropomorphizing AI that are worth clarifying:

- **Should AI never discuss emotions?** No, it can acknowledge a user’s feelings (if the user shares them, such as a disappointed customer whose purchase was misdelivered) or discuss emotions as a concept. AI should never claim to experience these emotions and should always acknowledge these limitations to users.
- **Should AI never use pronouns or have an identity?** Sure, it can have an identity or use pronouns like “I” or possessive adjectives like ”my”****because****the AI system exists, and people need to refer to it by some short-hand descriptor. It's just an entity that is neither conscious nor human; forcing alternative phrasing to depersonalize it further results in awkward grammar and unintuitive communication.
- **Should AI communicate robotically?** No, it doesn’t have to communicate with a cold, unfriendly voice and tone. System instructions can adjust an AI’s word choice and sentence structure to make it helpful without indulging in false emotional expressions.

## Practical Advice for UX Professionals

When designing AI features or systems to perform work, UX professionals should heed this advice.

- **Position AI truthfully**: Avoid using customary human names or fake human avatars. Marketing, onboarding, and interface copy should always position it as a helpful work tool and never as a person or friend.
- **Tightly focus the scope of AI features**: The more focused the feature, the more likely the AI is to demonstrate competence. Be clear about what the AI cannot reliably perform.
- **Align finetuning towards professionalism**: Ask the team about steps to ensure that emotionally charged interactions are penalized or excluded from the AI’s fine tuning. Prefer and reward professional interactions that remain neutral.
- **Check and refine system prompts**: Ensure guardrails are in place at a system level to align the AI towards transparency and competence over sycophantic warmth.
- **Incorporate robust sourcing into the interface**: A competent AI model justifies its output with data to reduce the chances of hallucination. Use techniques like retrieval-augmented generation (RAG) to enrich the AI’s output from data sources and enable users to confirm those sources with minimal [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/).
- **Probe for AI usage in recruitment**: Use screener questions in user research to understand participants' prior experiences and [mental models](https://www.nngroup.com/articles/mental-models/) of AI. Are you recruiting participants who view AI primarily through a social lens when you’re designing a productivity-focused AI tool? These prior experiences might bias participant expectations and their qualitative feedback.

![Infographic titled 'How to Develop User Trust in GenAI Chatbots for Work Tasks.' Left panel with a green check shows 'AI Project Advisor' focusing on competence, giving data-based advice about delaying a product launch. Right panel with a red X shows 'Sam, Project Manager' focusing on emotions, offering vague feelings and personal thoughts instead of concrete evidence.](https://media.nngroup.com/media/editor/2025/09/24/genai2.jpg)

*If you want users to trust an AI while doing work-like tasks, develop its ability to complete tasks competently. Simulating an emotional, human-like persona is counterproductive.*

### Conclusion

Promoting anthropomorphic qualities in a task-oriented AI is a counterproductive strategy. This approach seems like an easy path towards making approachable AI, but it can undermine user trust. Instead, **teams working in productivity contexts should develop the AI's analytical, planning, and reasoning capabilities**. This path is more challenging, but there are no shortcuts to creating AI experiences that users will actually trust and use.

### References

Clara Colombatto, Jonathan Birch, and Stephen M. Fleming. 2025. The influence of mental state attributions on trust in large language models. *Communications Psychology* 3, 84. [https://doi.org/10.1038/s44271-025-00262-1](https://doi.org/10.1038/s44271-025-00262-1)

Jared Moore, Declan Grabb, Kevin Klyman, William Agnew, Stevie Chancellor, Desmond C. Ong, and Nick Haber. 2025. Expressing Stigma and Inappropriate Responses Prevents LLMs from Safely Replacing Mental Health Providers. arXiv preprint [https://arxiv.org/abs/2504.18412](https://arxiv.org/abs/2504.18412)

Lujain Ibrahim, Franziska Sofia Hafner, and Luc Rocher. 2025. Training Language Models to Be Warm and Empathetic Makes Them Less Reliable and More Sycophantic. arXiv preprint [https://arxiv.org/abs/2507.21919v2](https://arxiv.org/abs/2507.21919v2)
