---
title: "Why You Cannot Trust Numbers from Qualitative Usability Studies"
date: "2021-05-23"
url: "https://www.nngroup.com/articles/true-score/"
author: "Raluca Budiu"
topics: [analytics-and-metrics]
type: article
---

Perhaps one of the most common methods of collecting user data is [qualitative usability testing](https://www.nngroup.com/articles/quant-vs-qual/). This method usually involves [observing a few users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) and noticing those elements of the design that are easy or hard to use.

Some researchers also like to collect numerical data in qualitative studies — measures like success (whether the participant was able to complete the task or not), task time, or self-reported metrics such as satisfaction, task difficulty, [NPS](https://www.nngroup.com/articles/nps-ux/), and [SUS](https://www.nngroup.com/articles/measuring-perceived-usability/). As a result, in reports or presentations, we often see formulations such as:

- *70% of the users are able to complete the task*.
- *The ease-of-use rating for the new version of the design is much better than that for the old design (6.2 vs. 5.1).*
- *The average satisfaction rating is 6.7 on a scale from 1 to 7.*

**These statements are misleading.** To understand why, let’s take a detour into the **true-score theory**, which is central to any measurement.

## In This Article:

- [True-Score Theory](#toc-true-score-theory-1)
- [Small Sample Size, Large Measurement Error](#toc-small-sample-size-large-measurement-error-2)
- [Statistics Tells Us if We Can Trust the Numbers](#toc-statistics-tells-us-if-we-can-trust-the-numbers-3)
- [Protocol Variability in Qualitative Studies](#toc-protocol-variability-in-qualitative-studies-4)
- [Do Not Report Numbers Without Statistics](#toc-do-not-report-numbers-without-statistics-5)
- [Conclusion](#toc-conclusion-6)

## True-Score Theory

To assess the usability of a design, you are often interested in the value of a metric over your whole user population. For example, you may want to know the percentage of users, out of your whole target population, who are able to successfully place an order on an ecommerce website. Unless your audience is tiny (because, perhaps, you are [designing an intranet](https://www.nngroup.com/articles/intranet-design/) for a small company), you will have thousands of users and it will be unfeasible to determine that number precisely — after all, to compute it, you would need to ask every single member of your audience to place an order on your site and record whether they were successful.

This value of the metric based on the entire population is called the **true score** — it is something that cannot be determined exactly. However, it is possible to estimate it. This is precisely what you do when you run a study with a sample of your user population and ask participants to place an order. Based on that study, you obtain an **observed score** — how many users in your sample were able to complete the task. **The observed score is often used to predict the true score**.

However, the observed score is not the same with the true score. The true-score theory says that they differ by a **measurement error**:

**Observed score = True score + Measurement error**

If the measurement error is small, then the observed score will be a good prediction of the true score. If, however, the error is big, the observed score will not tell us much about the true score.

## Small Sample Size, Large Measurement Error

**As a rule of thumb, when the sample size in a study is small, the measurement error will be big.** To understand why, remember that each participant in the study brings to the study their own personal context — some may be more versed in online ecommerce and therefore have little difficulty shopping, others may be a little under the weather and may need to work hard to focus on the task, yet others may like the study facilitator and do their best to please them. This personal context is noise because it has nothing to do with the quality of your design, but it will contribute to the observed score. It can skew your study results in one direction or the other — for example, a person who is distracted may have a poorer performance on the site and may produce longer task times, more errors, and lower satisfaction ratings. (Or, a happy, highly motivated participant may generate scores that are better than the reality.)

If your study involves only a few participants (say, 5 or 10), it is very likely that their personal context will skew the study results. However, when the study involves a lot of participants, the personal context will cancel out — for every person that is unhappy and that may give you a poor rating, there will usually be a person who’s happy and who will give you a better one.

Thus, when the number of people included in the study is small, that estimate obtained from the study will not be a good predictor of what will happen in the population at large. That is because there is a large chance that the noise will overcome the signal in your data.

## Statistics Tells Us if We Can Trust the Numbers

Even though sample size gives us a good heuristic for knowing whether we can trust a number, we can do better than that. In fact,**statistics helps us precisely estimate the measurement error** from a study.

There are two statistical instruments that tell us whether one or more numbers obtained from a study are good predictors of the true score: **confidence intervals** and **statistical****significance**.

### Confidence Intervals

The confidence interval is a statistical instrument that allows us to quantify how well a number observed in a study predicts the true score. **A confidence interval indicates the likely range for the true score** — how different we expect the true score to be from an observed score. For example, based on a study in which 50 out of 100 participants were successful on a task, the confidence interval for the success rate among the whole population can be computed to be between 40% and 60%. In other words, the true score for success is somewhere between 40% and 60% — it could be 42% or it could be 59%. We could also say that the true score is 50% ± 10% — that is, our measurement error for this study is ± 10%. (All the confidence intervals calculated in this article are real 95% confidence intervals; however, for the purposes of this article, the confidence level is a technicality that we will not insist on.)

Confidence intervals are strongly influenced by sample size. For instance, if you run a study with 10 people and 5 of them complete a task, your confidence interval will be 50% ± 26% — between 24% and 76%. That means that your success rate may be decent at 75% or very poor at 32%. With that few users, your measurement error is high and your estimate range is very wide.

If, however, you were to include 100 users in your study and 50 of them completed the task, the observed score will still be 50%, but your confidence interval will be 50% ± 10% (or, from 40% to 60%) — a much lower measurement error.

### Statistical Significance

While confidence intervals are used to describe the range of a true score based on an observed score, **statistical significance allows us to compare two observed scores**. It tells us whether the difference between two observed scores is likely to reflect a real difference between the corresponding true scores or is just due to chance.

If you run a study on two different designs A and B, you may obtain that the success rates are 60% and 70%, respectively, suggesting that design B is better than A. These numbers are, however, observed scores and therefore include some noise. So, it is possible that this observed difference of 10% between the 2 designs does not reflect a real difference — in other words, it could be the case that the true scores for success are 65% for design A and 60% for design B and, in reality, design A is better than design B.

**Statistical significance allows us to tell whether an observed difference is real or just the effect of measurement noise**. There are many tests for statistical significance that are appropriate in different circumstances, but they all return a **p-value** — the probability that a difference is due to chance or noise in the data **. If the p-value is small (less than 0.05), we say that the difference is statistically significant** — in other words, that it reflects a real difference in the true scores.

Coming back to our example, without running a statistical significance test, we cannot say whether design B is better than A based on just the observed scores. We would need to look into whether that difference is statistically significant. Only if it was, could we say that design B is better than design A.

## Protocol Variability in Qualitative Studies

So, by now, I hope I convinced you that small studies generally lead to large measurement errors. That is the primary reason for which it is irrelevant whether your success rate was 70% or 20% in a qualitative study and it will be hard to make inferences that apply to the whole population.

However, there is another reason for which numbers from qualitative studies are unreliable — and that is **variability in study protocol**.

In quantitative usability testing, because we want to make sure we’re not adding any confounding variables that can impact the measurement error, the researcher works hard at establishing both [internal and external validity](internal%20and%20external%20validity). Study conditions are usually strictly documented and the specifications are followed to the letter from one participant to the next. Even for in-person quantitative studies, there is usually little if any intervention from the moderator.

In contrast, qualitative studies often are [formative](https://www.nngroup.com/articles/formative-vs-summative-evaluations/) in nature — they aim to identify issues in the design and fix them as soon as possible. Unlike quantitative studies, they give the facilitator [some freedom to steer the participants in the direction of interest](https://www.nngroup.com/articles/user-testing-stepped-tasks/) (hopefully without [priming](https://www.nngroup.com/articles/priming/) them) or ask clarifying questions. Sometimes, different sessions may involve different tasks or even different designs — for example, if you are doing [parallel and iterative testing](https://www.nngroup.com/articles/parallel-and-iterative-design/).

As a result, very often, a qualitative session will be different than the next — with different amounts of intervention from the facilitator, different levels of think-aloud verbalization from the participant, and sometimes even different tasks and interfaces. This variability in the protocol ultimately leads to more noise in the data. On participant may have completed a task with no help on the site and another one may have needed repeated guidance from the facilitator. Their success rates and even satisfaction ratings may eventually be the same, but only because of external factors.

This fluidity is part of the strength of qualitative testing and is what makes it such a great tool for quickly identifying issues in the design. But it’s also partly why you’re more likely to get a noisy number in a qualitative test than in a quantitative one.

## Do Not Report Numbers Without Statistics

In general, whenever you report numbers based on a sample of your population, do the math — **calculate confidence intervals and statistical significance to see how well your observed scores** (the numbers from your study) predict the corresponding true scores and the behavior of your whole population.

There is a single exception to this rule — if your sample includes the whole population. In that case, we are not making any prediction: we are simply reporting the true score. For example, if I wanted to know the percentage of blue-eyed people n my high-school class of 100, I would simply count them and report the percentage. I would not need a confidence interval. But if I wanted to know the proportion of blue-eyed people among the readers of NNgroup.com articles , I would not possibly count them. I would have to take a sample, see how many people in the sample have blue eyes, then based on that sample calculate a confidence interval and report it as the likely range for the percentage of blue-eyed readers.

If your stakeholders insist on seeing numbers from small studies, present the numbers in the right light and make it clear that they cannot be trusted. Make sure that you mention whether your results generalize to the whole population or not. Even though you may carefully craft your formulation to apply it only to your study, people will tend to generalize. For example, you might say *The average satisfaction rating in our study was 6.7 on a scale from 1 to 7,* but your stakeholders will likely hear *The average satisfaction rating for all our users is 6.7.* So, always, explicitly include whether anything can be inferred about the population at large.**

BAD | GOOD | 70% of the users are able to complete the task. | 70% (7 out of 10) of the participants in this study completed the task. Based on this result, we estimate that the success rate in the whole population is between 39% and 90% (95% confidence interval). | The ease-of-use rating for the new version of the design is much better than that for the old design (6.2 vs. 5.1). | Even though in our study the ease-of-use rating for the new version of the design was higher than for the old design, this difference was not statistically significant at p > 0.05 and is unlikely to be replicated in the general population. | OR, if p < 0.05: | The ease-of-use rating for the new version of the design was higher than for the old version, and this difference was statistically significant at p <0.05. | The average satisfaction rating is 6.7 on a scale from 1=low to 7=high. | The average satisfaction rating in our study was 6.7 on a scale from 1=low to 7=high; we expect that in our whole population the average satisfaction will be between 5.2 and 7 (95% confidence interval).

## Conclusion

Any study that includes only a sample of your users will have a measurement error. Numbers from studies with only a few participants usually lead to large measurement errors and make for poor predictors. In order to understand how big the measurement error is and how well the numbers that you obtained in the study predict the behavior of the population at large, you need to use statistical instruments such as confidence intervals and statistical significance.
