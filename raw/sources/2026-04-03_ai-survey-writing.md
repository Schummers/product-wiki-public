---
title: "AI Can Help with Survey Writing, But It Still Requires Human Expertise"
date: "2026-04-03"
url: "https://www.nngroup.com/articles/ai-survey-writing/"
author: "Rachel Banawa"
topics: [ai]
type: article
---

Generative AI chatbots are an appealing tool for UX researchers who are under pressure to quickly deploy surveys. When given a clear research objective and prompted to use survey-design best practices, genAI tools like ChatGPT and Claude can generate a solid first draft in a matter of seconds.

That said, a solid first draft is still only a starting point. Although these tools can handle some aspects of survey design surprisingly well, they also show weaknesses in other important areas. Understanding where AI performs well — and where it falls short — is essential. Without that judgment, AI can speed up the writing process while introducing problems that weaken the quality of your survey and, ultimately, your research insights.

## In This Article:

- [Where GenAI Can Assist in Survey Creation](#toc-where-genai-can-assist-in-survey-creation-1)
- [Current Limitations of GenAI for Survey Development](#toc-current-limitations-of-genai-for-survey-development-2)
- [Tips for GenAI-Assisted Survey Writing](#toc-tips-for-genai-assisted-survey-writing-3)

## Where GenAI Can Assist in Survey Creation

When guided with clear instructions, generative AI tools can perform reasonably well on several foundational aspects of survey writing. In many cases, they can:

- Generate relevant questions that cover multiple dimensions of the research topic
- Write questions in clear, neutral, and straightforward language
- Avoid certain common issues such as double-barreled wording
- Group questions together based on related topics
- Suggest a mix of both [closed-ended and open-ended questions](https://www.nngroup.com/articles/open-ended-questions/)
- Suggest multiple ways to phrase questions and construct response options

These are meaningful strengths. For researchers who need a starting point, especially when time is limited, **AI-generated drafts can meaningfully**[accelerate survey development](https://www.nngroup.com/articles/research-with-ai)**** by providing a strong initial structure.

## Current Limitations of GenAI for Survey Development

Despite these strengths, AI-generated surveys often miss important aspects of good survey design. These shortcomings are not always dramatic. In fact, that is what makes them risky: **a survey can look polished at first glance while still containing subtle issues that weaken data quality or the respondent experience**.

To examine how these issues may show up in practice, I tested ChatGPT 5.4 (*Thinking* mode), Claude Sonnet 4.6 (*Extended Thinking* mode), and Claude Opus 4.6 (*Extended Thinking* mode) using the same survey-writing prompt. I ran the prompt at least twice in each tool to see how the outputs varied across attempts. (Because these tools are evolving quickly, future models may resolve some of the issues described in this article, while possibly introducing new ones of their own.)

Here’s the prompt I used.

> **Prompt:***I'm creating a survey for the discovery stage of developing a new telehealth platform, so my goal is to learn what barriers people face when trying to access care online and what would make the experience feel more useful, trustworthy, and convenient. Results from this survey will be used to inform how to create a telehealth platform that is easy and intuitive for users to use.*
> 
> 
> 
> *Draft survey questions for this survey. Incorporate survey design best practices. Make the survey take no longer than 10 minutes to complete. Give suggestions for page order and question order in a way that will reduce priming. Export the survey draft into a Microsoft Word document.*

Across the survey drafts that were created, several issues emerged.

### GenAI May Underestimate Respondent Burden

A major limitation is that **genAI tends to underestimate how effortful the survey will feel to respondents**. Because genAI does not experience the survey as a respondent would, it can miss forms of friction that make a survey feel tiring or frustrating in practice.

For example, genAI tools may:

- **Underestimate survey length:** A genAI tool may confidently suggest that a survey will fit within a 10-minute completion time despite containing far too many questions. In other cases, it may generate an overly long draft and give suggestions on which questions to trim. In either case, human review is needed to assess actual burden and cut unnecessary content.
- **Recommend grid questions:** GenAI may suggest using grid questions to present rating-scale items, but this approach is generally best avoided. Grid questions can increase respondent burden and encourage straightlining, which refers to when participants repeatedly select the same answer across multiple items without fully evaluating each one.
- **Generate too many options for multiselect questions:** GenAI may produce long lists of answer options — such as more than 10 choices — for multiselect items. Even when the options are plausible, too many choices can make questions harder to scan and evaluate, especially if there are several multiselect questions with long lists used consecutively.
- **Place demographic questions too early**: GenAI tools may recommend asking demographics questions at the beginning of the survey. However, demographic questions are often better placed at the end (if they’re not being used as screener questions), where they feel less intrusive and are less likely to discourage participation early on.
- **Use inconsistent instructions for multiselect questions:** A survey draft may require respondents to *Select exactly 3* for one multiselect question and *Select up to 2* for another, without a clear reason for the difference. These shifts can make the survey feel less predictable, increase cognitive effort, and lead to selection errors.

### GenAI May Generate Flawed Response Options

Another issue is that **genAI can produce response options that seem reasonable at first glance but do not support high-quality measurement.** Writing good response options requires more than coming up with plausible answers. The options need to be complete, mutually exclusive when appropriate, balanced, easy to interpret, and aligned with how respondents naturally think about the topic. These are the kinds of issues an experienced survey designer is more likely to catch, even when the draft sounds polished.

For example, genAI may:

- **Omit an “Other” option when one is needed:** GenAI may generate a list of plausible answer choices without including *Other* when the list is not exhaustive. This can make it harder for respondents to answer accurately if none of the listed options fully fits their situation.
- **Generate semantically unbalanced rating scales**: In a rating-scale question, genAI recommended the endpoints *Very poor* and *Excellent*. These labels are not parallel, which can make the scale feel uneven and negatively affect how respondents interpret the response options.
- **Create its own rating scale options:** GenAI may invent custom rating-scale options instead of using well-established formats such as Likert-type or semantic differential scales. While these custom labels may sound polished, they can be harder for respondents to interpret and make the results less reliable.
- **Use incorrect categories for Likert-type formats:** GenAI may produce response options that look like a standard [Likert-type format](https://www.nngroup.com/articles/rating-scales/) but omit expected categories. For example, one tool generated *Strongly disagree, Somewhat disagree, Neither agree nor disagree, Somewhat agree, and Strongly agree* — leaving out *Disagree* and *Agree*. This misalignment with standard practice makes the scale harder to interpret.

![Survey question Q7 asks respondents to rate importance of 6 online healthcare features (like provider continuity, 24-hour appointments, messaging, pricing) on a 5-point scale from Not important to Essential.](https://media.nngroup.com/media/editor/2026/03/23/q7-image-compressed.png)

*In this example, Claude Opus 4.6 (Extended Thinking) recommended a grid question with semantically unbalanced response options – two issues that reduce survey quality.*

![Survey question Q16 asks agreement with "A virtual visit can be just as effective as an in-person visit for certain health concerns" using a 5-point Likert scale from Strongly disagree to Strongly agree.](https://media.nngroup.com/media/editor/2026/03/23/q16-image-compressed.png)

*This example from Claude Opus 4.6 (Extended Thinking) includes a Likert-type response format that omits two standard categories: Agree and Disagree.*

### GenAI May Overlook Response Formats Worth Considering

GenAI may not always consider the full range of response formats that could work well for a survey. As a result, it can overlook methodologically strong formats that may be well-suited for the research goal.

For example, genAI may overlook:

- [Semantic differential scales](https://www.nngroup.com/articles/rating-scales/)**:** None of the genAI tools I tested considered the use of a semantic differential scale, even in scenarios where they would be a strong fit. Semantic differential scales are an important format to consider given their strengths in reducing acquiescence bias and social desirability bias.
- **Simple rank order:** GenAI tools may not always consider the use of simple rank order questions (e.g., *Rank the following items from ‘Most Important’ to ‘Least Important’*). However, this response format is useful when the goal is to understand participants’ relative priorities.

## Tips for GenAI-Assisted Survey Writing

Here are 7 tips for using genAI chatbots in survey design. **The key principle is to use genAI as a drafting tool, but always rely on human expertise for oversight**.

### 1. Start with a Clear Research Objective

GenAI performs best when you give it a specific goal, clear context, and enough background on what you are trying to learn. [The more precise you are about the context,](https://www.nngroup.com/articles/careful-prompts/)**the more likely the tool will generate survey questions that are relevant and actionable.**

Your prompt can include aspects such as:

- Your research questions
- The business or product decisions it will inform
- Your target audience
- Any parts of the research goal that should not be made too obvious to participants
- Your analysis plan (for instance, mentioning that you do not intend to gather any qualitative data to prevent it from suggesting open-ended questions)
- The ideal survey length

### 2. Prompt the Tool to Follow Survey-Design Best Practices

Do not assume the model will naturally produce good survey questions on its own. Tell it to **incorporate**[survey-design best practices](https://www.nngroup.com/articles/survey-best-practices/).

You can even explicitly tell it to avoid specific common problems such as double-barreled questions, leading wording, vague terms, overly long answer lists, and unnecessarily burdensome question formats. If you have access to a paid subscription to Claude, you could consider creating a Claude Skill that documents these best practices.

### 3. Use AI to Generate Alternatives, Not Final Questions

One of the most useful applications of genAI is producing multiple alternatives of a question or response set. You can do this using a simple prompt such as, “Provide 5 alternatives for this survey question”. This approach makes it easier to compare wordings, identify subtle issues, and refine the draft more efficiently.

In many cases, the best final question may come from combining the strongest parts of several alternatives.

### 4. Scrutinize Question Wording and Response Options Carefully

Even when a survey item sounds strong initially, both the question wording and the answer choices may still be flawed. Doublecheck whether the question is clear, specific, and neutral, and whether the response options are exhaustive, mutually exclusive when appropriate, balanced, semantically parallel, and aligned with how respondents naturally think about the topic.

### 5. Review the Survey for Respondent Burden

Check whether the survey truly fits your ideal length and is as easy to complete as the tool claims.

Look for signs of unnecessary burden, such as too many questions, long multiselect lists, inconsistent instructions, intrusive questions placed too early, or formats like grids, that are likely to frustrate respondents.

### 6. Consider Different Response Formats

Do not limit yourself to the formats genAI happens to suggest. In some cases, another format such as a semantic differential scale or a simple rank-order question may better match the research goal than the default structure produced by the tool.

### 7. Pilot with Real People

No matter how polished the draft looks, you still need to see how actual participants respond to it. Running a [pilot test](https://www.nngroup.com/videos/3-ways-to-test-surveys/)**with real people can reveal confusion or friction that AI simply cannot detect**. In fact, pilot testing is essential to the survey-design process regardless of whether AI was involved, because teams simply cannot know in advance how real participants will interpret questions.

### Conclusion

Generative AI can produce genuinely strong survey drafts and, with the right prompting, can be a valuable accelerator in the survey-design process. It can help researchers generate useful questions quickly, explore alternative phrasings, and build an initial structure that might otherwise take much longer to create.

But those strong outputs are reliable only when an experienced human is actively reviewing and refining them. AI can support the work, but it still takes an experienced survey designer to tell the difference between a draft that is seemingly good and one that will actually yield useful, trustworthy data. The most effective way to use genAI is not as a replacement for survey expertise, but as a powerful drafting partner that performs best under skilled human supervision.
