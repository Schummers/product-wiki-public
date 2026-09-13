---
title: "Documenting a UX-Benchmarking Study"
date: "2023-05-07"
url: "https://www.nngroup.com/articles/ux-benchmarking-repository/"
author: "Raluca Budiu"
topics: [research-methods]
type: article
---

As an organization refines the user experience of a product, a common question is whether the newer version of its product is better than what it had before. The answer to that question is usually provided by [UX benchmarking](https://www.nngroup.com/articles/benchmarking-ux/), a practice that aims to measure and compare the UX of different versions of the product.

## In This Article:

- [Need for Consistency in UX Benchmarking](#toc-need-for-consistency-in-ux-benchmarking-1)
- [Benchmark-Study Information](#toc-benchmark-study-information-2)
- [The Metrics Collected](#toc-the-metrics-collected-3)
- [The Raw Data](#toc-the-raw-data-4)
- [When Is It Okay to Make Changes to Your Study?](#toc-when-is-it-okay-to-make-changes-to-your-study-5)
- [Conclusion](#toc-conclusion-6)

## Need for Consistency in UX Benchmarking

UX benchmarking involves **running a set of iterations of the same summative study** (called a **benchmark study**) on various product versions, with each iteration aiming to capture the UX of the current version of the product. To gauge UX improvements from one version to the next, researchers would have to compare metrics such as [success rate](https://www.nngroup.com/articles/success-rate-the-simplest-usability-metric/), task time, and [user satisfaction](https://www.nngroup.com/articles/satisfaction-vs-performance-metrics/) for some important tasks. They will also have to go beyond the observed values of the metrics obtained in the two studies and run a statistical analysis to judge whether the observed differences are [statistically significant](https://www.nngroup.com/articles/understanding-statistical-significance/) or due to chance.

Imagine that the first iteration of the benchmark study, which evaluated the original version of the design, was conducted in person, whereas the second iteration was [remote unmoderated](https://www.nngroup.com/articles/remote-usability-tests/). Often, people tend to stay more on task in in-person studies than in remote unmoderated ones, and, as a result, times from remote unmoderated studies tend to be longer. Thus, if we notice a difference in task time or success rates between the two design versions, it could be due not to a better design, but to the way in which the study was conducted.

To soundly compare the results from the two studies, the company needs to compare apples to apples. In other words, the studies need to have **the same methodology and collect the same metrics**.

*In this example, the time on task (as obtained in two iterations of a benchmark study) was higher for the original version of the design than for the redesign. The difference between these numbers, however, should not be taken at face value. First, for the comparison to be fair, the two iterations of the benchmark study must have used the exact same protocol and definition of the metrics collected*. *Second, a statistical analysis should be run to determine if the difference is statistically significant or due to noise.*

Any company that considers a benchmarking practice should first **define the benchmark study** in minute detail and document it so that subsequent versions of the same design could be evaluated using the exact same methodology and metrics.

Usually, the study details and the raw data collected in the study are stored in a **benchmark research repository.** This repository could be part of the **research****repository** maintained by the company or could be separate. However, it should be easily findable and accessible. People who are involved in the UX evaluation of subsequent product versions should be able to refer to both the study information and the raw data from the study when they need them.

## Benchmark-Study Information

There are several aspects of the study that need to be well documented so that anybody will be able to replicate the study in the future. They include:

- The study methodology
- The study tasks
- The screener used for recruiting participants
- The dependent variables (or metrics) of interest and their exact definitions
- The raw data obtained in the study

### The Benchmark-Study Methodology

Differences in study methodology impact the results of the study and ultimately bias our comparison in one direction or the other. All the methodology details— ranging from the type of study to task phrasing — need to be well documented so that researchers who will run the subsequent iterations of your benchmark study will be able to replicate it.

These details include:

- The **type****of****study** (moderated or not, in-person vs. remote)
- The **tool** used to conduct the test. This is particularly important in unmoderated tests. In such tests, the study is usually run within an [unmoderated platform](https://www.nngroup.com/articles/unmoderated-user-testing-tools/) (e.g., UserZoom, UserTesting.com). Sticking to the same platform ensures a sound base for comparing results of different studies.
- The **use****of****think**-**aloud****protocol**. Even though it is not necessary to use [think aloud](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/) in quantitative studies, do not assume that everybody will know that. Instead, clearly specify whether participants were asked to think out loud.
- The **instructions****given****to****participants****at****the****beginning****of****the****study.** For example, if you ask participants in one study to be as quick and accurate as possible as they complete the different tasks, these instructions should be present in all the other studies.

### The Study Tasks

Generally, a benchmark study should collect measures regarding the [top tasks](https://www.nngroup.com/videos/top-tasks-ux-design/) that your users run on your site. These tasks usually remain the same across the product’s lifetime. (If they change, then it makes less sense to compare various versions of your product.) Thus, these **top tasks should be included in all the iterations of your benchmark study**.

There are several aspects of the tasks that need to stay the same across all iterations:

- The **task wording,** including any **fake credentials** or **information** given to participants
- The **task order** (whether random or not)
- Any **practice tasks** given to participants at the beginning of the study

#### Task Wording

If you change how the task is phrased, it is possible that users may understand it differently and that can ultimately invalidate any comparison with prior versions.

Additionally, in many quantitative studies, when we want participants to place an order or log into an existing account, we may give them a name, an address, or other information that they can in order to perform the task. This information needs to be well documented. (For instance, if you use different names or addresses, these may require different typing times and they may affect your overall task time.)

#### Task Order

We normally advocate task randomization in quantitative tests, to avoid introducing any biases in the study. Sometimes, however, it is not possible to randomize all tasks. (For example, if one of the tasks involves logging in, it will probably have to precede the task of accessing specific information in one’s account.) Thus, the order in which the tasks are presented (whether random or not) needs to be documented so it can be replicated in further iterations of the study.

#### Practice Tasks

Practice tasks are generally used to get participants comfortable with the study setup and the task domain, and thus mitigate the learning phase inherent to any experiment. (Some people are slower to warm up, others are faster. These individual differences add variability to the data collected in the study; to reduce that variability, quantitative researchers often use 1–2 practice tasks at the beginning of each study.) If you used practice tasks in one study, these should be present in all the iterations.

### Participant Screener

Another essential component of any study is the participants. It is unrealistic and, for most studies, also undesirable to set the goal of recruiting the same participants for different iterations of your benchmark study. However, even though the participants will differ across study iterations, they should be recruited using the same [screener](https://www.nngroup.com/articles/recruiting-screening-research-candidates/). Otherwise, it is possible that any differences that you might observe are not due to the design, but rather to participants’ individual characteristics.

Thus, the screener used for the benchmark study should be included with all the other study documents in your research repository.

## The Metrics Collected

There are many types of metrics that one can collect in a quantitative study. Some are relatively standard and likely to be used in most quantitative studies — for example, task success, usually defined as a binary metric (0 means success and 1 means failure). Others can be defined by the particular study. For instance, if your study includes a [survey](https://www.nngroup.com/articles/10-survey-challenges/) that is specific to your product, the answer to that survey will be a metric specific to your study.

For any kind of metric that you collect, **clearly document how that metric is defined.**

Even for metrics that feel obvious, like **success**, you need to specify what counts as success. For example, for the task of subscribing to a monthly newsletter, was success defined as clicking the *Subscribe* button or as reaching the page where that button was found?

If you are collecting **task****times**, are you recording only the task-completion times (that is, the times of those participants who successfully completed the task) or are you recording all the task times, whether participants were correct or not? Both these types of time measures are common in quantitative studies, so make sure that all the iterations of the benchmark study use the same.

If you included **rating****questions** or other multiple-choice questions in your study, record the wording for those questions and the possible responses. If you created a multiple-question survey instrument and defined a score for that, explain how the score was calculated. Any changes in the question or the responses could invalidate cross-study comparisons.

## The Raw Data

Once the first round of the benchmarking study is complete, the researcher will usually analyze the data and present a summary of the findings. It’s not enough to save a copy of the findings in your research repository. Equally important is to **save the raw data** — the spreadsheet (or spreadsheets) containing the data points generated by each participant.

(Of course, you should not include in such spreadsheets the [participants’ identifying information](https://www.nngroup.com/articles/privacy-and-security/); it’s enough to include a code that corresponds to each participant and the metrics that you collected from them.)

There are several reasons why this data needs to be included in your research repository:

- **Performing statistical analysis:** To determine whether the next version of the design is better than the current one, you will need to perform statistical analyses and establish statistical significance. These analyses require access to the raw data.
- **Revising analyses:** It is possible that in the future you will devise new ways to analyze the data — for example, you may decide to exclude all trials where participants took longer than a certain threshold time (e.g., 10 minutes). If you had access to the original raw data, you would be able to redo all the analyses with this new constraint.
- **Investigating errors:** You may want to investigate any errors present in the coding or the analysis. For example, it’s possible that the [SUS score](https://www.nngroup.com/videos/system-usability-scale/) was miscalculated. Or that the wrong method was used to calculate [confidence intervals](https://www.nngroup.com/articles/confidence-interval/).

## When Is It Okay to Make Changes to Your Study?

At this point, you may ask: what if you run your benchmark study over many years and your company needs, goals, or offerings shift?

It’s okay to change your benchmark study partially or even completely. In fact, it’s a good idea to periodically evaluate your benchmark study to make sure it answers the right questions. However, if you make changes to the study, you might diminish or completely lose the ability to compare with older versions of the product. In many cases that will not be a substantial problem. The new benchmark study can serve you well to evaluate the usability of subsequent versions of your product even if it doesn’t allow you to compare with what you had before.

Sometimes, you may still be able to use the results from the old study. For example, if you decide to add or remove a task to your list of tasks, it’s unlikely that the change will impact your comparisons. (There are some exceptions — for instance, if that removed task must precede another task that was based on it.)

But if you tweak the wording of a task or change the definition of a metric, any comparison involving that task or metric will not be sound (if the comparison involves prior versions of the design).

## Conclusion

A UX-benchmarking practice is based on a benchmark study that is repeated periodically, to evaluate new versions of your design. For this evaluation to be sound, the study setup needs to be always the same. The benchmark-study protocol, participant-recruitment screener, and the raw data should be stored in your research repository, so that researchers will be able to precisely replicate the benchmark study and compare the results obtained from its different iterations.
