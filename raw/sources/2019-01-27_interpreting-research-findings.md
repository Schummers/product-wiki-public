---
title: "Interpreting Contradictory UX Research Findings"
date: "2019-01-27"
url: "https://www.nngroup.com/articles/interpreting-research-findings/"
author: "Kate Moran"
topics: [research-methods]
type: article
---

While presenting a recent training [seminar on quantitative research for UX](https://www.nngroup.com/courses/measuring-ux/), I was asked an interesting question:

> *“I’m leading a team tasked with overhauling a complex enterprise product . We have a high-fidelity prototype, and we’ve been conducting extensive research to get it ready for launch. The stakes are high — even minor improvements could lead to big productivity gains, but conversely, minor issues in the design could cause big problems for our users.*
> 
> 
> 
> *In our quantitative usability testing, we’ve seen substantial reductions in the amount of time it takes people to do important tasks in the prototype as compared to the old product. But here’s the problem — in qualitative interviews, our users hate the prototype . The feedback is so negative. How do we reconcile this contradiction? What should we do?”*

The situation that this UX lead described is a common one for many research-focused digital product teams.

The ideal way to conduct UX research is to use [multiple methodologies](https://www.nngroup.com/videos/when-use-which-ux-research-method/), mixing both [quantitative](https://www.nngroup.com/articles/quant-vs-qual/) and qualitative research. Using multiple approaches to answer our research questions and to see our product’s performance in different ways is a sophisticated **triangulation** strategy,. **But what happens when those different research methods tell different — even contradictory — stories?**

In this article, I’ll consider some possible problems, explanations, and solutions for this UX lead’s situation. Unfortunately, I have very few details about her product and her research, but I’ll generate some theories based on other questions I’ve been asked and teams I’ve worked with.

## In This Article:

- [Check the Methodology](#toc-check-the-methodology-1)
- [Interpreting the Findings: Not Only What Users Say, But Why?](#toc-interpreting-the-findings-not-only-what-users-say-but-why-2)
- [Next Steps](#toc-next-steps-3)
- [The Challenge of UX Research](#toc-the-challenge-of-ux-research-4)

## Check the Methodology

In situations like the one described above, the first step is to examine how each study was conducted. Since UX research involves studying human beings, there are a huge number of potential **mistakes that could’ve resulted in an incorrect or misleading finding.**

Before we consider what these contradictory findings might mean, we need to check some critical components in each study. We should look for potential problems in four areas:

- Participants
- Tasks
- Logistics
- Analysis

### Participants

#### Who was involved in each study? How many people participated in each of the studies? Were there any outliers — people who behaved very differently than the rest of the group?

Was the same user group involved in both the quantitative and the qualitative research? How were the participants in the two studies recruited? Answering these questions may point to the reason behind the contradictory findings.

For example, maybe the researchers decided to recruit users with different levels of expertise in using the product. If novices participated in the quantitative research, but experienced users provided the qualitative feedback, then the differences between the participant groups could influence the results.

### Tasks

#### Which tasks did the quantitative study include?

It’s possible that users may be more efficient when performing a handful of tasks that the company cares about. However, if users regularly engage in a broad set of tasks, that increased efficiency in one area of the product may not exist throughout the system.

*How much exposure preceded the qualitative interviews?* If the researchers just pulled up the new version on a laptop, pointed to it, and asked participants what they thought without giving them the chance to actually complete any tasks, that could explain some negative responses. Users could’ve just been reacting to the fact that the UI looked new and different, if they didn’t have adequate time to explore its features.

*How much exposure preceded the quantitative study?* Were users given any practice tasks before they tested the system? Did they receive any type of training from the researchers? If the quantitative participants had more exposure to the new system than the qualitative participants, they have had time to get over their initial negative reactions and learn to be efficient with the new product.

### Logistics

*How were the studies run?* We’ll need to verify that the studies were conducted in a reasonably realistic manner — that the studies have **external validity**.

For example, imagine that this product is always used on a factory floor, where users are exposed to a lot of environmental noise and distractions. If the study was conducted in a quiet conference room, the users may have performed better with the new version. But there could be some aspect of the design that would make it perform worse in realistic conditions.

Additionally, we’ll also need to check that there wasn’t some accidental problem with how the quantitative study was run that could have biased the result — that the study has **internal validity**. We can ask: who was moderating those tests? How much experience did the moderators have?

Even small confounding variables could produce an invalid result. For example, imagine if all of the participants who tested the new version of the product did so in the morning on a Monday, and all of the participants who tested the old version did so in the evening on a Friday. There could easily be something about the timing of the tests that influenced the participants to perform better or worse.

### Analysis

*Do we have statistical significance?* For the quantitative research, was the difference between the two designs [statistically significant](https://www.nngroup.com/articles/understanding-statistical-significance/)? In order words, were the faster task times in the new version reliable and not likely due to random change?

*How was time on task analyzed?* In many studies, the time on task includes only *successful* attempts. The new design was faster than the old one, but were the success rates comparable? If the average time on task increased by 2 minutes, but the proportion of users who could successfully complete the task *decreased* by 40%, that would still be bad for the company and the users!

*What the types of errors did people run into?* We should look not just at time on task, but other metrics that were collected during the quantitative study, to see if they all suggest that the new product is better. Even if there were fewer errors with the new design, it’s possible that they were more severe than the errors made with the old system and that they influenced users’ attitude in the qualitative study.

## Interpreting the Findings: Not Only What Users Say, But Why?

If we find no substantial faults or explanations in the methodologies, it’s time to consider what the conflict between these two standards of quality (quantitative efficiency and qualitative satisfaction) might mean.

As UX professionals, **it’s our job to listen to users.** But as any experienced UX professional will tell you, that **sounds easier to do than it really is**. That’s because we can’t just listen to users and follow their verbatim requests. People usually [don’t know what they really want](https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/) — your users aren’t the designers of the system, they can’t see the big picture the way you can. What’s worse, their feedback is often influenced by other factors (faulty memories, social pressure, psychological biases, etc.)

This is part of the reason why a triangulation strategy is so necessary. We can’t just ask people what they want and do what they tell us. We have to collect a mix of data (quantitative, qualitative, self-reported, and observed) to really see what’s going on. Then we can use that information to interpret what our users say.

So, in this UX team lead’s example, how should we make sense of the user feedback, which seems to contradict the quantitative performance data? We need to look at **why** these people might be responding so negatively to an objectively better product, while the task times in the quantitative study seem to be better.

### Perceived Usability Can Differ from Objective Usability

Unfortunately, we don’t know exactly how much this particular team reduced time on task in the quant studies. The UX lead said that the reduction was “substantial,” but that could mean a matter of seconds or minutes. From the company’s perspective, even a reduction of seconds could be hugely beneficial. Imagine that thousands of employees perform this task thousands of times per year — at the company level, those efficiency gains add up quickly, and could result in cost savings.

However, from an individual user’s perspective, those gains might not matter so much. If it’s an improvement of seconds, an individual user may not even realize that the new system is actually faster, as she doesn’t see her own time on task or that of other participants. Or maybe they *do* realize the new system is faster, but those small gains may not seem worth the difficulty of a new workflow.

### People Don’t Like Change

The users of this complex enterprise product have been using it almost every day for work. Some of them have been using essentially the same version of the application for many years. Even if it isn’t the most efficient it could possibly be, they’re used to it. They know how it works. By changing things, the design team is asking the end users to invest effort to become proficient with the new version. (It’s a common finding that [users hate change](https://www.nngroup.com/articles/fresh-vs-familiar-aggressive-redesign/) — which is a reason to do research before release so that subsequent changes can be minimized.)

If users in the quantitative study received training or practice with the new system before the test (as described above in “Check the Methodology”), there may have been an initial lag in performance that was not captured by the measured task time. When a new interface is introduced, there will sometimes be an **initial loss of productivity**. Learning a new interface for a complex task takes time and is less efficient than simply doing the task with the old, familiar interface. Even though in the end the new interface may prove better, (1) people have no way of knowing that when they first start using it; (2) in the beginning, the experience can be worse.

It’s also possible that there was one negative reaction to some (presumably minor) feature of the new system — for example, a change in color that people did not like, a change in the visibility of the teams’ contributions in an Intranet — that did not necessarily affect UI performance, but dominated their reaction and created [a peak-end effect](https://www.nngroup.com/articles/peak-end-rule).

## Next Steps

My advice to this team lead was to first consider these reasons behind the user feedback, and then step back and look at the larger picture. Of course, in UX, quantitative data should never automatically overrule qualitative information or designers’ instincts (taking that approach leads to [comical design mistakes](https://www.nngroup.com/articles/shaming-users/).)

When weighing conflicting findings, we have to consider the tradeoffs. We always want users to be effective, efficiency, and happy with the products they use. However, in this context, the potential efficiency gains are probably much more attractive to stakeholders than the employees’ happiness. This new version of the product is very likely to be implemented, regardless of how users feel about it. That could be a potential problem, though — if users hate this new version enough, it could lead to decreased job satisfaction or employee turnover. It’s worth this company’s time to try to make its users both efficient *and* happy.

As we’ve discussed, this negative feedback may be a temporary negative reaction to change. Since the stakes are high, and so is this team’s research budget, my recommendation would be more investigation to see if that hypothesis is correct. The team could try **qualitative beta testing with new hires,** who had minimal exposure to the previous system, and see if their feedback differs. New hires will not have the same attachment to the old system as more experienced employees and may be less susceptible to affective reactions to change. (On the other hand, new hires are also less likely to have as much domain knowledge as people who have been using the system for a while, so they may ignore some important aspect.) Positive feedback from new hires might indicate that the experienced employees’ responses were caused by an initial aversion to change.

Or, the team could conduct a systematic **learnability study,** with multiple rounds of quantitative usability testing that track task time, task completion, and satisfaction over time. This study will give an accurate and complete picture of how user performance *and* satisfaction changes as people gain experience with the new product. If the new design is truly better than the old one, the team should expect both the satisfaction and the performance measures (task time and task completion) increase over time and eventually reach comparable or better numbers than the current design. The study will give a good idea of how much exposure to the new design people need in order to overcome their initial negative reaction.

*(We did one such study for a consulting client. While the details have to remain confidential, I can say that it took a full year before users performed better with the new design than with the old, which they had used daily for a decade. In the long run, the new design was indeed much better, but the decision to change over required long-term commitment from management.)*

If those studies show that the initial negative reactions will be replaced by long-term satisfaction and productivity gains, then the team can be confident that it is moving in the right direction. From there, they can plan an **incremental rollout** of the new system. Allowing current users to opt in to the new product when they’re ready (and not under pressing deadlines) can reduce the short-term frustration.

Alternatively, another possible outcome of research could be that the new design is mostly good, but that there’s some good aspect in the old design that should be retained in the new version.

## The Challenge of UX Research

Making sense of contradictory findings is part of **the challenge (and the fun) of conducting UX research.** Each methodology is just one piece of information, a way of looking at our users or our products from a different perspective. The data should always inform our decisions, but at the end of the day, it’s up to us to make sense of that information and make the best choice.

For more strategies to help you incorporate quantitative data into your decision-making process, check out our full-day course, [Measuring UX and ROI](https://www.nngroup.com/courses/measuring-ux/).

For more on how to correctly analyze quantitative data, check out our full-day course, [How to Interpret UX Numbers](https://www.nngroup.com/courses/UX-statistics/).
