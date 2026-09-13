---
title: "AI-Powered Tools for UX Research in 2023: Issues and Limitations"
date: "2023-07-02"
url: "https://www.nngroup.com/articles/ai-powered-tools-limitations/"
author: "Feifei Liu, Kate Moran"
topics: [ai, design-patterns]
type: article
---

**Updated guidance is available in a newer article:****Accelerating Research with AI .** This article captures our early assessment of AI research tools and their marketing claims. Some of these limitations still exist, but many of the tools have improved.

## In This Article:

- [Introduction](#toc-introduction-1)
- [The AI-Powered UX-Research Tools](#toc-the-ai-powered-ux-research-tools-2)
- [How We Evaluated the AI-Powered Tools](#toc-how-we-evaluated-the-ai-powered-tools-3)
- [Issues and Limitations](#toc-issues-and-limitations-4)
- [Future Iterations of AI-Powered Research Tools](#toc-future-iterations-of-ai-powered-research-tools-5)
- [Reference](#toc-reference-6)

## Introduction

New AI tools of all kinds are entering the marketplace, eager to capitalize on the interest sparked by ChatGPT. The UX field is no exception.

The marketing descriptions of AI-powered tools for UX research make big claims, like:

- “We’ll do your research analysis for you! No need to analyze or tag your data.”
- “AI has no bias! Reduce bias in your research!”
- “Our tool can analyze data from any kind of user-research method, including usability testing!”

**If these claims sound too good to be true, it’s because they are.** It’s likely that, in the future, AI-powered user-research tools will become much better at delivering on these kinds of promises. Right now, however, you should be careful **** when considering a subscription to one of them.

**We evaluated four new AI-powered UX-research tools**. In this article, we present the results of our evaluation. Note that we won’t mention any of the tools by name, because we hope that they will learn from their mistakes and improve in the near future.

## The AI-Powered UX-Research Tools

There are two types of AI-powered tools we currently see on the market:

- Insight generators
- Collaborators

They both can be used to summarize transcripts of qualitative-research sessions.

### AI Insight Generators

**AI insight generators summarize user-research sessions** based solely on the transcripts of those sessions.

These tools don’t accept other types of information from the researcher. This ends up being a big problem because, unlike human researchers,**these tools can’t factor in context.** You can’t give them background information about the product or about the users. They also cannot take advantage of findings from previous studies.

(Researchers may work around these limitations by uploading background information and their own session notes as separate assets to add to analysis, but these might be treated as different sources instead of session-specific information, whereas human researchers could easily combine the two.)

### AI Collaborators

**AI collaborators are like insight generators,** except that they **can accept some contextual information** from the researcher. Like insight generators, collaborators can absorb your text data and produce insights.

For instance, researchers can show the AI some human-generated codes to “train” it. The tool can then recommend tags for the [thematic analysis](https://www.nngroup.com/articles/thematic-analysis/) of the data. In addition to session transcripts, they can also analyze researchers’ notes. As a result, collaborators (unlike basic insight generators) can create themes and insights based on input from multiple sources.

AI collaborators are more sophisticated than AI insight generators but still suffer from similar limitations (discussed below).

## How We Evaluated the AI-Powered Tools

We looked at three insight generators and one collaborator. Out of the three insight generators, **two were deemed too premature in terms of handling user-research data** when the article was written. (One generated only a list of top 5 insights for a given project with no capability of modifying the prompt or asking followup questions; the other allowed researchers to upload only text files — a feature that seemed too restricting for most user-research projects, but possibly suitable for analysis of large sets of text, like app-store reviews.)

To evaluate the other two tools, **we uploaded recordings from a usability-testing study of NNgroup.com. We compared the tools’ analyses against analysis produced by human researchers**. The study aimed to understand how our mobile customers choose from NN/g’s training courses. The data from the study had been already analyzed by NN/g researchers. None of the researchers who originally analyzed the user-testing sessions contributed to this AI evaluation.

Additionally, **we supplied the collaborator**(which could accept such input)**with the tags from the original thematic analysis** of the sessions.

The output of the tools included:

- A list of insights, either based on a single document (session video, notes, and so on) or, in the case of the collaborator, on several pieces of text tagged
- Followup answers to questions submitted through an AI-chat tool (e.g., *What were the users’ frustrations? Visualize with a bar chart.)*
- Tag recommendations (for the collaborator only)

*The AI collaborator produced a list of insights based on notes tagged with one of 4 tags.**The AI insight generator allowed the researcher to ask specific questions regarding the project.**When researchers manually coded transcripts with an AI collaborator tool, AI-suggested tags would show up at the top of the tag list.*

## Issues and Limitations

### Most AI Tools Can’t Process Visual Input

None of the AI research tools we tested had the ability to process video or visual input. They were fully text-based, so they could only analyze transcript data. That isn’t a big problem for analyzing [user interviews](https://www.nngroup.com/articles/user-interviews/). However — contrary to the ludicrous claims made by the creators of these tools — **no human or AI tool can analyze**[usability-testing](https://www.nngroup.com/articles/usability-testing-101/)**sessions by the transcript alone**.

Usability testing is a method that inherently relies on observing how the user is interacting with the product. Participants often [think aloud](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/), describing what they’re doing and thinking. Their words do provide valuable information. However, you should never analyze usability tests based only on what participants say!

Transcript-only analysis misses important context in user tests, because participants:

- **Don’t verbalize all their actions,** particularly small [microinteractions](https://www.nngroup.com/articles/microinteractions/), which are sometimes the most interesting. They also don’t verbally announce every single page or screen they visit or every click they make, so the AI tool will often lose track of the current page or screen.
- **Don’t describe every element in the product.** There are many reasons why a design element may not be mentioned in a user-test transcript. For example, it could be that the element is common and works as expected. Or it could be that the element is not present in the interface. The AI cannot know the actual reason without being able to “see” the design.
- **Don’t always have a clear understanding,** or [mental model](https://www.nngroup.com/articles/mental-models/), of the product. Participants may misinterpret certain aspects of the design. If the AI tool accepts the participant’s misunderstanding as fact, it will not understand the product.

In the AI-generated high-level summary of a session, one AI tool gave us the recommendation of adding filters to the site we tested. That website *did* have a filter tool on some pages, and that specific participant did use it during the study without mentioning the feature out loud. However, she expressed the need for filters on a different type of page.

As a result, the AI tool’s recommendation to add filters was confusing: did the site need more filters on the page? Or did it need to include a filter tool on every single page? (This type of recommendation also exemplifies another common problem with AI-generated insights: their vagueness — see the next section below.)

**Do not trust AI tools that claim to be able to analyze usability-testing sessions by transcripts alone.** Future tools able to process video visuals will be much more useful for this method.

### Vague Summaries and Recommendations

The AI tools often gave **extremely vague** summaries and recommendations.

For example, one tool made the following recommendations about a description page:

> *Make sure that all relevant information is easily accessible and clearly presented*.
> 
> 
> 
> *Provide more detailed descriptions*[about the page]*.*

This sounds good, but it didn’t explain what *relevant information* or *detailed descriptions* meant, nor did it say how the existing content should be modified to be *clearly presented.*

We’ve included two analysis excerpts below — one generated by an AI tool and one written by a human researcher.

*One AI tool provided vague recommendations on adding filtering options and improving navigation, without actionable to-dos.**An NN/g researcher (who was not involved in the AI evaluation and is not an author of this article) started by providing an overall assessment and then described key issues in the user flow by giving specific examples to help readers visualize the situation. Her recommendations (e.g.,* Expose the number of search results *, Change “* Interaction *” to “* Interaction Design *”) were also more concrete than the ones provided by the AI tool.*

### Limited Understanding of the Context

AI insight generators severely lack context. They don’t ask for, and can’t accept:

- The **study goals** or research questions
- Insights or tags from **previous rounds of research**
- **Background information** about the product or the user groups
- **Contextual information** about each participant (e.g., new user vs. existing user)
- The list of **tasks** or interview **questions**

Note that, even though some tools allow people to upload information to a given project, they don’t allow researchers to differentiate between how these resources should be used. For instance, the study goals should be carried over in all sessions, but session-specific participant information should be applied only to certain videos.

That lack of context caused problems in the analysis generated by these tools. For example, the insights were presented without any priority. With no understanding of the study goals, **the system can’t know what’s most important or relevant to the researcher.**

In fact, some of the themes generated by the tools were extremely uninformative and uninteresting. Here’s **a finding** provided by one of the AI insight generators:

> *The participant was happy that they could share both positive and negative feedback.*

This finding appeared at the top of the findings list. Imagine putting such an inane observation in a presentation or a report!

When helpful insights are buried in an ocean of irrelevant ones, identifying and prioritizing them can be time-consuming –- even more so than analyzing the session manually.

### Lack of Citation and Validation

When generating quotes and recommendations, some tools don’t reference where they found that information (for example, they fail to attribute a quote to a specific session, timestamp it, or link it to the clip they’re referencing.)

Ironically, this lack of referencing causes lots of problems for the AI collaborators, which can accept content from the researcher. The tool we tested was **not able to distinguish between the researcher’s notes and the session transcript.** That’s a huge ethical issue in reporting research — we always must differentiate between our interpretations or assumptions and what the participants said or did.

Most important, this lack of citation **prevents researchers from verifying** whether the tool’s summary or recommendations came from the research. AI systems have a dangerous [tendency to provide incorrect information](https://hbr.org/2022/09/ai-isnt-ready-to-make-unsupervised-decisions) that sounds plausible. Imagine if an AI tool recommended that you add a specific new feature to a product, but that recommendation was not grounded in the user-research data. Such a mistake could be costly in time and resources.

Some of the tools we evaluated had **information-accuracy disclaimers**. Interestingly, those disclaimers were often nowhere to be seen in their promotional claims.

### Unstable Performance and Usability Issues

Unfortunately, none of the tools we tested had solid usability or performance. We encountered **outages, errors, and unstable performance.** We had to reach out to some tools’ customer-support departments several times, just to use the basic features of the tools. These issues have the capacity to slow your analysis down, rather than speed it up.

### Bias

Another **questionable claim** made by some AI-powered research tools is:

> *Our tool will give you an unbiased perspective of your users, because AI systems do not have bias.*

Perhaps they may reduce bias in some ways. For example, if you [test your own designs](https://www.nngroup.com/articles/designers-developers-doing-usability/), it’s easy to be subconsciously influenced by [confirmation bias.](https://www.nngroup.com/articles/confirmation-bias-ux/) The AI tool doesn’t care whether your design works as you hoped it would.

However, **the claim that AI tools are bias-free is blatantly false** and shows a misunderstanding of how the technology works. According to NIST’s Reva Schwartz and her colleagues, AI systems and applications can involve biases at 3 levels: systematic, statistical and computational, and human biases. AI must be trained on data, which can introduce systematic (such as historical and institutional) and statistical biases (e.g., dataset sampling isn’t representative enough). When people are using AI-powered results in decision making, they can bring in human biases like [anchoring bias](https://www.nngroup.com/articles/anchoring-principle/).

AI product companies like OpenAI have worked hard to reduce the potential biases as much as possible, which we truly appreciate. Still, users of AI-powered tools should be aware of these biases.

## Future Iterations of AI-Powered Research Tools

We do believe that user researchers will have good, reliable, useful AI-driven tools in the near future. They will make our work much faster and of higher quality. However, the currently available tools cannot provide those benefits yet.

We hope and expect that future iterations of these types of tools will have:

- **The ability to accept many different types of background and contextual information,** including study goals, research questions, participant information, prior research findings
- **A way to accept edits and corrections from researchers.** These tools should have more flexibility and collaborate with the human researchers (especially given their current reliance on transcripts). Eventually, AI systems will need less direction from humans, but for now, it’s essential to make these tools useful in any way.
- **Accurate, specific, linked referencing.** Researchers need quick, easy ways to doublecheck the AI system’s work. That means they need to be able to see where the tool got its findings from –- whether from a specific session or one observer’s note.
- **Better UX and reliability.** Advanced technology does not invalidate the need for usability — if anything, it’s [even more important with novel tech](https://www.nngroup.com/articles/face-recognition-pay/).
- **The capability to process video, screen, and webcam footage.** Any tool that cannot process these visual inputs cannot analyze usability tests. Don’t trust tools that claim they can do test analysis based on transcripts alone.
- **Accurate and trustworthy promotional claims.** We were disappointed to see just how inaccurate and misleading were many of the claimed benefits of these AI research tools.

**AI tools definitely have a large role to play in the near future of UX research.** But for now, be wary of grandiose claims. Definitely request and **test out a demo** before committing to pay for any AI-powered research tool. Be cautious about the tool’s findings and recommendations, and doublecheck its work. If doublechecking isn’t possible, don’t use it.

## Reference

Schwartz, R. , Vassilev, A. , Greene, K. , Perine, L. , Burt, A. and Hall, P. (2022), Towards a Standard for Identifying and Managing Bias in Artificial Intelligence, Special Publication (NIST SP), National Institute of Standards and Technology, Gaithersburg, MD, [online], https://doi.org/10.6028/NIST.SP.1270
