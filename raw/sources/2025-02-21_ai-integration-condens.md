---
title: "Common-Sense AI Integration: Lessons from the Cofounder of Condens"
date: "2025-02-21"
url: "https://www.nngroup.com/articles/ai-integration-condens/"
author: "Alexander Knoll"
topics: [ai]
type: article
---

Now that [generative AI (genAI)](https://www.nngroup.com/articles/how-ai-works/) has been around for a couple of years, the extreme hype is starting to simmer down. As the dust settles, we have a clearer picture of AI's potential and limitations.

In this article, I share some of the lessons learned through our genAI journey at Condens, our research-analysis platform. These lessons will be useful to anyone trying to determine how to integrate AI into their product strategy or research workflow.

## In This Article:

- [Resisting AI Pressure](#toc-resisting-ai-pressure-1)
- [Our AI-Product-Integration Strategy](#toc-our-ai-product-integration-strategy-2)
- [3 Key Questions for AI Integration](#toc-3-key-questions-for-ai-integration-3)
- [Where GenAI Succeeds and Fails](#toc-where-genai-succeeds-and-fails-4)

## Resisting AI Pressure

When ChatGPT was released in 2022, I felt like a little kid with a new Game Boy, exploring prompts and imagining all the new possibilities. And like many companies, [Condens](https://condens.io/) began testing genAI's potential for speeding up and improving UX research.

Unfortunately, we also started seeing very ambitious and exaggerated claims being made about AI’s capabilities and how it could be used — **claims which conflicted with what we observed in our evaluations and testing.**

*Examples:*

- “High-quality insights in seconds”
- “Automatically analyze your projects”
- “Eliminate bias from your research”
- “User research without the users.”

We found that, while generative AI could meaningfully improve research productivity, many of the claims, especially in marketing messaging, were overstated. Although many AI features looked impressive in demos, [they often didn’t perform well in real research situations.](https://www.nngroup.com/articles/ai-powered-tools-limitations/)

This hype environment has placed considerable pressure on researchers and research vendors alike. At Condens, we had to define our **evidence-backed strategy towards common-sense AI integration** and stick to it.

It wasn’t easy. **We lost a customer** for our decision to take a more measured approach. The team decided to move to a competitor that was more aggressively integrating new AI features. Sadly, that move was not the choice of the research team — it was motivated by pressure from stakeholders who had seen unrealistic marketing about efficiency gains with AI. Four months later, the disappointed research team reported having to "drastically adjust their expectations" when the AI features underperformed and “reality hit” them.

We concluded that significant work is still needed to [develop truly useful AI applications,](https://www.nngroup.com/articles/ai-user-value/)and we have a responsibility to both drive innovation and maintain the hard-earned [trust](https://www.nngroup.com/videos/building-trust-ux/) of our researchers.

## Our AI-Product-Integration Strategy

I’d describe our approach to genAI in UX research (UXR) as cautiously optimistic. We’re eager to explore where AI can genuinely enhance UXR workflows, but we’re also mindful of its limitations. We won’t build AI features that don’t have value or reliability.

To resist the hype and stay on the right track, we **established some of our own AI-design guidelines**:

1. Give AI tasks that are **scoped****and specific.**
2. Make it easy to **verify****AI output** and always connect it back to evidence.
3. Make it easy to make **changes****to AI output.**
4. Ensure core tasks (in our case, data analysis) **can also be done without AI.**

## 3 Key Questions for AI Integration

Here are 3 questions you should ask to decide whether a particular AI tool can reasonably support your task.

(When you ask these questions, consider the specific API or LLM version that you have access to. Though the latest and greatest systems may be powerful, these may not be available or cost-effective.)

While we developed these questions in our research context at Condens, they're valuable for any AI implementation.

### Does the AI Have the Necessary Context and Data?

**AI often requires deeper context** about industries, companies, or research studies than can be provided in a prompt. Without sufficient context, results are rarely high-quality. That’s particularly true for UX work, which is extremely contextual.

Automatic transcription and translation are excellent examples where AI excels because all necessary data is present in the input, requiring minimal additional context or interpretation.

### Does the Task Work Within the AI’s Technical Input Constraints?

Research shows that **LLMs have technical limitations regarding the size of the input data.** For example, GPT-4o currently takes a maximum of 128k tokens, which corresponds to roughly 10 hours of interviews transcribed. When provided with too much input, these models reduce the data they consider down to what they think is relevant, likely introducing bias into the results.

Additionally, studies done at the Chinese Academy of Sciences and at University of Waterloo, respectively, suggest that result quality may deteriorate as input size increases. (AI researchers are actively working to develop solutions to this problem. At the time of writing, those solutions have not been conclusively proven.)

### Can the Output Be Verified and Modified?

AI-generated content inherently requires fact checking, which is exponentially more challenging with larger datasets. In some cases, it may be faster and better for a human to do the task instead of verifying the AI-produced work.

**Research findings and recommendations must be backed by evidence,** so AI’s output in UXR is useless if you can’t verify the source.

The results should also be easy for humans to edit when needed, because it’s unlikely that they’ll take the AI output exactly as is. Especially if the output contains an error, people will need to be able to adjust it, even if just a bit.

## Where GenAI Succeeds and Fails

These questions have been extremely useful for our team as we evaluate different research-related tasks that are candidates for genAI. Based on its current capabilities, here are our conclusions.

### Summarizing Small Chunks of Content

> *Example research task:*
> 
> 
> 
> Asking AI to summarize a long quote from a participant to make it easy and quick to understand for yourself or stakeholders

Key Question | Evaluation | Note | Necessary Context and Data? | ✅ Yes | The only input required is the quote. | Works with Input Constraints? | ✅ Yes | Even if it’s a long quote, you won’t exceed the technical limits. | Can Output Be Verified and Modified? | ✅ Yes | The summary is usually 1–2 sentences so it can be quickly reviewed and verified.

Even if the summary occasionally fails to capture the core of the message, it can still be useful.

### Summarizing Large Amounts of Content

> *Example research task:*
> 
> 
> 
> Asking AI to summarize an entire research project

Key Question | Evaluation | Note | Necessary Context and Data? | ⚠️Partially | AI's literal summarization approach becomes problematic with complex data that requires meaningful selection and interpretation. | Works with Input Constraints? | ⚠️Partially | Project data often exceeds input limits, forcing AI to make potentially biased preselections. | Can Output Be Verified and Modified? | ⚠️Partially | While reading a summary is quick, verifying accuracy requires deep familiarity with the source material.

### Simple Semantic Search

> *Example research task:*
> 
> 
> 
> Finding explicit user complaints or pain points mentioned in current project interviews

Key Question | Evaluation | Note | Necessary Context and Data? | ✅ Yes | Identifying explicit mentions requires minimal context. | Works with Input Constraints? | ✅ Yes | Most projects stay within the 10-hour transcript limit. | Can Output Be Verified and Modified? | ⚠️Partially | Users can quickly verify if the returned quotes mention pain points, but it is harder to check whether the output includes all mentions of pain points.

### Complex Semantic Search

> *Example research task:*
> 
> 
> 
> Identifying and ranking the most important pain points across all historical research data

Key Question | Evaluation | Note | Necessary Context and Data? | ❌ No | Ranking pain points requires significant interpretation and industry/company context that AI lacks. | Works with Input Constraints? | ❌ No | Historical data exceeds AI limits, forcing potentially biased data selection. | Can Output Be Verified and Modified? | ❌ No | Verification would require manual review of all source data.

This task requires (1) identifying the pain points and (2) ranking them by importance. It involves interpretation and judgment and should not be left to AI. The AI output will likely miss subtle behavioral cues (e.g., facial expressions) that point to challenges encountered by users. An experienced researcher with context about the company and industry will definitely be better here.

A version of this task that would likely be more realistic and feasible with AI would involve ranking pain points across all *research insights* generated from previous studies. That task would require substantially less data to be input into the AI and would make the output easier to verify.

### Quote Clustering

> *Example research task:*
> 
> 
> 
> Grouping preselected quotes and observations into initial themes

Key Question | Evaluation | Note | Necessary Context and Data? | ✅ Yes | The AI can work with quote text, although it might miss subtle connections. | Works with Input Constraints? | ✅ Yes | A single-project quote set should be fairly small. | Can Output Be Verified and Modified? | ⚠️Partially | Effectiveness depends on how results are presented and how closely evidence links to themes

AI can provide initial quote clusters based on text similarities, but it might miss connections that require reading between the lines or having a deep understanding of the topic. So, it can provide a starting point but its output will be limited in depth and uniqueness of insights.​

### Automated Analysis

> *Example research task:*
> 
> 
> 
> Generating a complete research report from raw project data

Key Question | Evaluation | Note | Necessary Context and Data? | ❌ No | The task requires complex reasoning and judgment that may be beyond AI's capabilities. | Works with Input Constraints? | ⚠️Partially | For some projects, large datasets might exceed limits, leading to biased data selection. | Can Output Be Verified and Modified? | ❌ No | Verification requires a full manual review, negating any time savings.

For this task, you’re asking the AI to make judgment calls with limited context. It’s likely that biases will be introduced and relevant data will be left out of your results. Moreover, even though current models advertise being capable of “reasoning,” it is unclear whether their level of reasoning is available within your tool or would produce the same results as a human.

For better results, break complex-analysis tasks into smaller, verifiable steps rather than attempting full automation. One benefit of working with subtasks is that you can have checks along the way to fix the AI’s errors (and thus “keep the human in the loop”). You thereby avoid an accumulation of AI errors and the risk of ending up in a totally wrong place.

### Conclusion

While the limitations of AI systems are much clearer now than they were two years ago, how they will develop is still an open question. So, for the time being, it’s reasonable to limit our expectations of AI’s capabilities to scoped, well-defined tasks that can be verified easily.

### References

- Li, T., Zhang, G., Do, Q. D., Yue, X., and Chen, W. 2024. Long-context LLMs struggle with long in-context learning. *arXiv preprint arXiv:2404.02060*.
- Wang, M., Chen, L., Fu, C., Liao, S., Zhang, X., Wu, B., Yu, H., Xu, N., Zhang, L., Luo, R., Li, Y., Yang, M., Huang, F., and Li, Y. 2024. Leave no document behind: Benchmarking long-context LLMs with extended multi-doc QA. *arXiv preprint arXiv:2406.17419*.
