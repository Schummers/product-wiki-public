---
title: "Confounding Variables in Quantitative Studies"
date: "2023-09-24"
url: "https://www.nngroup.com/articles/confounding-variables-quantitative-ux/"
author: "Caleb Sponheim"
topics: [analytics-and-metrics, research-methods]
type: article
---

[Quantitative studies](https://www.nngroup.com/articles/quantitative-research-study-guide/) (such as [surveys](https://www.nngroup.com/courses/surveys/), [quantitative usability testing](https://www.nngroup.com/articles/quantitative-user-research-methods/), and [analytics](https://www.nngroup.com/topic/analytics-and-metrics/) experiments) can offer valuable insights for product development. However, it is **crucial to carefully design quantitative studies to ensure accuracy and reliability.**

UX teams often rely on [quantitative research](https://www.nngroup.com/articles/quantitative-research-study-guide/) to help them make important decisions. Basing those decisions on faulty data can lead to serious design mistakes and misallocated resources.

(Quantitative UX research involves lots of terminology and jargon, so consider referring to this [quantitative-research glossary](https://www.nngroup.com/articles/quant-ux-glossary/) for quick definitions.)

## In This Article:

- [Confounding Variable: Definition](#toc-confounding-variable-definition-1)
- [An Example of a Confounding Variable](#toc-an-example-of-a-confounding-variable-2)
- [More Examples of Confounding Variables](#toc-more-examples-of-confounding-variables-3)
- [Why Are Confounding Variables Important?](#toc-why-are-confounding-variables-important-4)
- [Best Practices for Avoid Confounding Variables](#toc-best-practices-for-avoid-confounding-variables-5)

## Confounding Variable: Definition

> Definition: A **confounding variable** is an unmeasured variable that may unintentionally affect the outcome of a research study.

Typically, UX researchers designate an independent variable and one or more dependent variables for their quantitative studies.

> **Independent variables** are study conditions that are manipulated by researchers. For example, a team might run a quantitative study comparing two different versions of a design. In this case, the design change is the independent variable.
> 
> 
> 
> **Dependent variables** are outcomes that are measured from a quantitative study. Researchers typically expect the values of dependent variables to change based on their independent variables. For example, researchers might measure user satisfaction to see which version of a design leads to higher satisfaction ratings. Put another way, UX researchers typically expect changes to an independent variable to influence dependent variables.

A confounding variable can affect both the independent variable (the conditions you change) and the dependent variable (the outcomes you measure), causing unexpected results in the study.

*Independent variables can directly influence dependent variables, but confounding variables can interfere, causing unpredictable and unreliable results.*

For example, a confounding variable could:

- Reduce the expected influence of a design change
- Reverse the outcome of a task-success metric
- Eliminate and change an effect of an independent variable

## An Example of a Confounding Variable

A research team ran a [within-subjects](https://www.nngroup.com/articles/between-within-subjects/)**quantitative usability study** to test a design change, which means that each participant would test both designs. (If the study were a between-subjects design, each participant would be asked to interact with only one design.)

**Design A was tested in the morning** with a group of participants, followed by a lunch break. The participants **returned to test****design B in the afternoon.**

After analyzing the data, the team found that design B had a higher [task-completion time](https://www.nngroup.com/articles/ux-benchmarking-repository/) than design A — in other words, participants completed tasks more slowly with design B in the afternoon than with design A in the morning.

*Example of addressing a confounding variable. In this example, design A was tested in the morning, and design B was tested in the afternoon; the test results were influenced by the time of day.*

Lower task-completion times are usually associated with better usability, but is that the case in this situation? **Does design A realistically have better usability than design B?**

**Several confounding variables** were present in this study; these variables could muddy the reliability of the results:

- Participants who tested design B had previous experience with the product, from the morning session.
- Lunch may have made participants less energized.
- Participants may be tired late in the day.

Some of these confounding variables may add contradictory and conflicting effects: In the afternoon, participants might do better due to experience but could also perform worse due to a post-lunch slump. **Confounding variables can make it difficult to predict the result of a study**.

To avoid the time-of-day and learning effects introduced in this study, **participants should be randomly assigned to either design A or design B** in the morning, with the other design in the afternoon. Randomizing the order in which participants are exposed to the study conditions will reduce the influence of time of day, depleted energy, experience, or hunger.

*The best approach to account for the effect of time of day would be to randomize the conditions of the study so that some participants see design B in the morning and design A in the afternoon.*

## More Examples of Confounding Variables

*The age of a participant could correlate with the experience they have with mobile interfaces and therefore affect their task success rate. If unmeasured or uncontrolled, participant age becomes a confounding variable.*

Confounding Variable | Description | Solution | Age effects | The age of participants can affect many UX-related variables | , including satisfaction, time on task, task success rate, and reading ability. | Recruit a representative sample of participant ages for your study. Randomize your participants across the conditions of your study, so that ages of participants are equally distributed across conditions. Record the ages of your participants for later analysis, if needed. | Seasonal effects | Participants may behave differently depending on the current season. | Consumers’ habits drastically shift around holidays | (Chinese New Year, American Winter Holidays, etc.). Comparing a Q4 usability study to a Q1 study may be affected by confounding variables. | If you are conducting a study over long periods of time or comparing results from different studies, consider the time of year at which the studies were completed. Ideally, compare data collected over similar time periods. | COVID-19 pandemic | The coronavirus pandemic has changed how people interact with products | ; data collected before and after the pandemic may be affected by the pandemic. | Exclude date ranges during the most acute period of the pandemic by identifying outlier data. | Competitive market shifts | If a competitor has a large sale or introduces an entirely new product right before a design change, | user behavior may be affected by the competitor’s actions | , preventing you from assessing the effect of your design change. | Structure your studies to avoid major market disruptions. | Existing product experience | When comparing metrics like task-completion time for two different products, participants’ prior experience with the products can skew the results into one direction or another.. | Recruit a representative sample of participant experience levels or exclude participants with extensive experience with your products (if applicable). | Existing product opinions | Users may have preexisting viewpoints about the products being tested, influencing usability or survey outcomes. When comparing user satisfaction with two products, prior opinions about the two products could bias the results. | During recruitment, screen for extreme positive or negative product sentiments and either control for or exclude those participants.

## Why Are Confounding Variables Important?

A quantitative study can be an investment of [significant time and money](https://www.nngroup.com/courses/measuring-ux/). You must have confidence that your study will be [reliable](https://www.nngroup.com/articles/qualitative-rigor/), and its results will be valid. Studies should be constructed such that they could be repeated, with an expectation of the same result.

**When a research study has low bias and a high level of repeatability and control, it has high**[internal validity](https://www.nngroup.com/articles/internal-vs-external-validity/)****— in other words, a study is internally valid if it does not bias a participant towards any specific answer or action.

If your research study has significant confounding variables, then the conclusions from that study may be wrong. Making decisions based on these misguided conclusions can result in significant loss of time and money for organizations.

## Best Practices for Avoid Confounding Variables

- **Use**[within-subject](https://www.nngroup.com/articles/between-within-subjects/)**study designs when possible**. Counterbalance or randomize the order in which participants are exposed to the different conditions in your study. For example, if they are testing two designs, randomly decide the first one tested by each participant. Within-subjects designs reduce sources of error and naturally counterbalance experimental conditions.
- **Randomly assign condition groups** for between-subjects study designs. For example, randomly decide which design should be seen by a participant.
- **Carefully consider possible confounding variables** of an upcoming study; structure the study to avoid them or measure them to control for them later. For example, if you know that age may be a factor for task completion, carefully collect all your participants' ages and control for the effect of that variable when performing [statistical analyses](https://www.nngroup.com/courses/ux-statistics/) such as regression in your study.
- **Keep your testing environments, personnel, and protocols consistent** throughout a study. Changing a study’s testing conditions between experiments or conditions (such as testing a different design in a different room) can unintentionally influence the outcomes of a study.
- **If it proves too difficult to estimate confounding variables or effectively control the potential variables in a quantitative study,**[consider conducting a qualitative study instead](https://www.nngroup.com/videos/qualitative-vs-quantitative-research/). In UX research, quantitative studies are not typically meant for exploratory research.
- Focus, clarify, and justify your research hypotheses before conducting your study.
