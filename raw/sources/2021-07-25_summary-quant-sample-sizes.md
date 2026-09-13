---
title: "How Many Participants for Quantitative Usability Studies: A Summary of Sample-Size Recommendations"
date: "2021-07-25"
url: "https://www.nngroup.com/articles/summary-quant-sample-sizes/"
author: "Kate Moran, Raluca Budiu"
topics: [research-methods]
type: article
---

## In This Article:

- [Introduction](#toc-introduction-1)
- [The Intuition Behind the 40-Participants Guideline: Why You Need 40 Participants](#toc-the-intuition-behind-the-40-participants-guideline-why-you-need-40-participants-2)
- [The Assumptions Behind the 40-Participant Guideline](#toc-the-assumptions-behind-the-40-participant-guideline-3)
- [When You May Get Away with Fewer Participants](#toc-when-you-may-get-away-with-fewer-participants-4)
- [What if Your Metric Is Continuous?](#toc-what-if-your-metric-is-continuous-5)
- [Conclusion](#toc-conclusion-6)
- [Reference](#toc-reference-7)

## Introduction

The exact number of participants required for [quantitative usability testing](https://www.nngroup.com/articles/quant-vs-qual/) can vary. Apparently contradictory recommendations (ranging from [20](https://www.nngroup.com/articles/quantitative-studies-how-many-users/) to 30 to 40 or more) often confuse new quantitative UX researchers. (In fact, we’ve recommended different numbers over the years.)

Where do these recommendations come from and **how many participants do you really need?** This is an important question. If you test with [too few](https://www.nngroup.com/articles/metrics-qualitative/), your results may not be [statistically reliable](https://www.nngroup.com/videos/statistical-significance-ux/). If you test with too many, you’re essentially throwing your money away. We want to strike the perfect balance — collecting enough data points to be confident in our results, but not so many that we’re wasting precious research funding.

In most cases, we recommend **40 participants** for quantitative studies. If you don’t really care about the reasoning behind that number, you can stop reading here. Read on if you do want to know where that number comes from, when to use a different number, and why you may have seen different recommendations.

Since this is a common confusion, let’s clarify: there are two kinds of studies, qualitative and quantitative. [Qual aims at insights, not numbers](https://www.nngroup.com/articles/5-test-users-qual-quant/), so statistical significance doesn’t come into play. In contrast, quant does focus on collecting [UX metrics](https://www.nngroup.com/reports/ux-metrics-roi/), so we need to ensure that these numbers are correct. And the key point: **this article is about quant, not qual**. ([Qualitative studies only need a small number of users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/), but that’s not what we’re discussing here.)

## The Intuition Behind the 40-Participants Guideline: Why You Need 40 Participants

When we conduct quantitative usability studies, we’re collecting [UX metrics](https://www.nngroup.com/reports/ux-metrics-roi/) — numbers that represent some aspect of the user experience.

For example, we might want to know what percentage of our users are able to book a hotel room on Expedia, a travel-booking site. We won’t be able to ask every Expedia user to try to book a hotel room. Instead, we will run a study in which will ask a subset of our target population of Expedia users to make a reservation.

*As an example, imagine we want to know the percentage of users who can successfully book a hotel room on Expedia.com.*

Then, we’ll count how many participants in that study are able to complete the task and we’ll use that percentage to estimate the percentage of our population. Of course, what we get from the study is not going to be exactly the same as our population success rate (there is always going to be some amount of measurement error), but we hope that it will be close enough.

When the number of people we include in the study is small, the percentage from the study will be unlikely to predict the success rate of the whole population — that number will simply be too noisy.

As another example, image you want to figure out the average daily temperature in Berlin, Germany during the summer. You decide to estimate that average by looking only at three random daily temperatures. Those three days probably will not give you a very accurate number, will they? This is the problem with small samples for quantitative studies.

In a quantitative usability study, to get a reasonably trustworthy prediction for the behavior of your overall population, you need around 40 data points. There are nuances depending on how much risk you are willing to take and what exactly you are trying to measure.

The **40-participant recommendation comes from a calculation**. That calculation estimates the minimum number of users needed to produce a reasonable prediction of your population behavior based on one study. It has specific assumptions, but it **will work for many quantitative usability studies**.

If you don’t care about statistics, you can stop reading at this point (or jump directly to the [conclusion](#conclusion)). Otherwise, if you’re curious about the nuances behind this recommendation, keep reading.

## The Assumptions Behind the 40-Participant Guideline

In statistical terms, the 40-participant guideline comes from a very specific situation, which may or may not apply to your particular scenario. It assumes that you have a considerable user population (over 500 people) and that the following are true:

- You want to estimate a binary metric such as success rate or conversion rate based on a study with a sample of your user population.
- You aim for a 15% margin of error — namely, you want your [true score](https://www.nngroup.com/articles/true-score/) (e.g., the success rate or conversion rate for your whole population) to be within 15% of the observed score (the percentage you obtained from your study).
- You want to take very little risk of being wrong in this prediction (that is, you will use a [confidence level](https://www.nngroup.com/articles/confidence-interval/) of 95% for computing your margin of error).

If all the above are true, it turns out that [you can calculate the number of participants you need for your study,](https://measuringu.com/sample-size-designs/) and it is 39. We round it up to 40 — hence the above recommendation. (These estimates are often rounded up by a few participants. First, rounding up makes the numbers more memorable. Second, slight overrecruiting helps if something goes wrong with one or two participants and their data has to be removed. For example, you may discover during the study that you accidentally recruited an [unrepresentative user or a cheater.)](https://www.nngroup.com/articles/problem-participants-remote-unmoderated/)

## When You May Get Away with Fewer Participants

It is possible to need fewer participants if the last two of the assumptions above are not true. Specifically, if you are:

- Willing to have a margin of error that is bigger than 15%
- Willing to take a larger risk

### Willing to Have a Margin of Error Bigger than 15%

The margin of error tells you how much you can expect your overall population rate to vary as a function of the observed score. Any time you collect a metric you should compute a margin of error (or, equivalently, a confidence interval). In other words, if in your Expedia study, 70% of your study participants were able to book a room and your margin of error was 15%, it means that your whole-population completion rate (the true score) is 70% ± 15% — that is, it could be anywhere from 55% to 85%.

*If the success rate in the study was 70% and the margin of error was 15%, the whole population’s success rate could range between 55% (70%-15%) and 85% (70%+ 15%); that range represents the 95% confidence interval.*

That range is 30% wide and it represents the **precision of your estimate;** it could, however, be the case that in some situations you don’t care if it’s a little wider and your margin of error is bigger (for example, if you want to be able to say that most people can use a certain feature of your UI). We don’t recommend going for margins of error bigger than 20% because your confidence interval for the true score will be quite wide and unlikely to be useful.

### Willing to Take a Larger Risk

A 95% confidence level means that your margin of error computations will be wrong only 5% of the time. It is the gold standard for published academic research. However, most UX researchers work in applied research, not academic research. For practical purposes, you may be willing to take a little bit more risk.

(Taking more risk is cheaper and is a good idea if the risks of a somewhat unreliable result won’t be catastrophic. However, bear in mind that UX teams often use quantitative usability testing to inform prioritization and resource allocation, so unreliable data may be quite problematic.)

If you are willing to drop the confidence level to 90%, then a **margin of error of 15% will require 28 users** and a **margin of error of 20% will require 15 users**. Again, you may consider rounding these up for many good reasons (for example, you may end up having to remove some of your trials when you clean up the data). This is the origin of the 30-user guideline that you may have encountered elsewhere — **that recommendation accepts more risk.**

The Number of Participants for Studies Involving a Binary Metric (Success, Conversion) | Confidence level | Desired margin of error | Required number of participants | Low risk,good precision | 95% | 15% | 39 | Low risk, fair precision | 95% | 20% | 21 | Medium risk,good precision | 90% | 15% | 28 | Medium risk, fair precision | 90% | 20% | 15

*This table shows the number of participants needed for different confidence levels and desired margins of error for binary metrics. The lower the confidence level, the riskier the study. The bigger the margin of error, the lower your precision and the less useful the numbers will be.*

## What if Your Metric Is Continuous?

If your metric is continuous or can be treated as continuous (e.g., task time, satisfaction or other types of rating, [SUS score](https://www.nngroup.com/articles/measuring-perceived-usability/)), the formula for the number of participants will depend on an additional factor: the variability of your target population. (It will also depend, like for binary metrics, on the desired margin of error and the confidence level used). That is something that you could estimate separately for your population by running a pilot study.

Of course, a pilot study to estimate the standard deviation is quite expensive and it will itself involve a fairly large number of participants. On the other hand, in most quantitative usability studies, there are several metrics involved and usually at least one of them is binary. Therefore, we recommend using that binary metric as a constraint in deciding the number of users. In other words, if you are collecting success, task time, and satisfaction, then you can **simply say I want a 15% margin of error for success at a 90% or 95% confidence level** (and recruit 30 or 40 users respectively). That will usually result in good margins of error for the other metrics involved.

If, however, you collect only continuous metrics (this is unusual) and you cannot afford to estimate the standard deviation of your population, you must first settle on a desired value for your margin of error. Of course, your desired value will depend on what you are measuring and the range for a task. We usually recommend using as a desired value 15% or 20% of the mean — in other words, if your task time is around 1 minute, you would like a margin of error no bigger than 0.15–0.20 minutes (9 to 12 seconds); if your task time is around 10 minutes, your margin of error should be no bigger than 1.5–2 minutes.

Next, you can use [Jakob Nielsen’s estimate of variability for website- and intranet-related continuous metrics](https://www.nngroup.com/articles/quantitative-studies-how-many-users/). That estimate is **52% of the mean**. In other words, if the mean task time is 1 min, your estimated standard deviation is 0.52 x 1 min = 0.52 minutes. If the mean task time is 10 minutes, then your estimated standard deviation will be 0.52 x 10 min = 5.2 minutes. With that supplementary assumption, you would need 47 users for a 15% margin of error at 95% confidence level, 33 users for a 15% margin of error at 90% confidence level, 26 users for a 20% margin of error at 95% confidence level and 19 users for a 20% margin of error at 90% confidence level. (Note that a 15% margin of error of 1 minute translates into 0.15 minutes — that is, 9 seconds.)

The Number of Participants for Studies Involving Only Continuous Metrics (Satisfaction, Task Time) | Confidence level | Desired margin of error (as a percentage of the mean) | Required number of participants | Low risk, good precision | 95% | 15% | 47 | Low risk, fair precision | 95% | 20% | 26 | Medium risk, good precision | 90% | 15% | 33 | Medium risk, fair precision | 90% | 20% | 19

*This table shows the required number of participants needed for a study involving continuous metrics such as time on task or satisfaction. Different numbers of participants are appropriate for different confidence levels and desired margins of error.*

In general, the number of users can be determined using the following formula:

![N is k squared times s squared divided by m squared.](https://media.nngroup.com/media/editor/2021/07/19/formula1-tight.JPG)

The variables in that formula are:

- *K* is a constant (1.96 for 95% confidence level or 1.645 for 90% confidence level)
- *s* is your standard deviation as a proportion of the mean
- *m* is your desired margin of error, also expressed as a proportion of the mean (0.15 corresponding to 15% or 0.20 corresponding to 20%)

If you estimate your standard deviation as a 52% (or 0.52) of the mean, then you can use the formula below:

![N is k squared times 0.27 divided by m squared](https://media.nngroup.com/media/editor/2021/07/19/formula2-tight.JPG)

## Conclusion

Even though there are many different recommendations for sample sizes in quantitative usability testing, they are all consistent with each other — they simply make slightly different assumptions. We think the **40-user guideline is the simplest and the most likely to lead to good results** — namely, a relatively small margin of error with a high confidence level.

However, you may settle for a lower number of users (around 30) if you want to take slightly more risk that your findings will not represent the behavior of your user population and thus decrease your confidence level to 90%. Moreover, if you also have tolerance for a larger margin of error, you can drop the number of users to **20 or even fewer, but that is generally a lot riskier.**

An acceptable strategy (especially if you are on a tight budget and mostly interested in continuous metrics such as task time and satisfaction) is to start with as many users as you can comfortably afford — say, 20–25 users. Once you’ve collected your data from these users, calculate your margins of error and determine if they are tight enough for your purposes. If they are too wide, then consider adding more users. This approach, however, requires that you work fast: you’ll need to do your analysis in a matter of a few days in order to be able to run the extra participants very soon after the first batch. Otherwise, you risk compromising the validity of your study.

Choose the right sample size for your situation to ensure you’ll optimize your quantitative study: collecting just enough data, but not too much.

## Reference

Jeff Sauro, James Lewis. 2016. *Quantifying the User Experience: Practical Statistics for User Research*. Elsevier.
