---
title: "How to Measure Learnability of a User Interface"
date: "2019-10-20"
url: "https://www.nngroup.com/articles/measure-learnability/"
author: "Alita Kendrick"
topics: [human-computer-interaction, psychology-and-ux]
type: article
---

## In This Article:

- [What Is Learnability?](#toc-what-is-learnability-1)
- [Learnability vs Efficiency](#toc-learnability-vs-efficiency-2)
- [Why Measure Learnability?](#toc-why-measure-learnability-3)
- [Running a Learnability Study](#toc-running-a-learnability-study-4)
- [Conclusion](#toc-conclusion-5)

## What Is Learnability?

Learnability is one of the [five quality components of usability](https://www.nngroup.com/articles/usability-101-introduction-to-usability/) (the others being efficiency, memorability, errors, and satisfaction). Testing learnability is especially valuable for complex applications and systems that users access frequently, though knowing how quickly users can acclimate to your interface is valuable for even objectively simple systems.

**Learnability considers how easy it is for users to accomplish a task the first time they encounter the interface and how many repetitions it takes for them to become efficient at that task.**

In a learnability study, we want to produce a [learning curve](https://www.nngroup.com/articles/power-law-learning/), which reveals longitudinal changes of a quantified aspect of human behavior. With the data from the learning curve, we can identify how long it takes users to reach saturation — a plateau in our charted data which tells us that users have learned the interface as much as possible.

For example, let’s say we are redesigning an enterprise file-backup application intended to be run by IT administrators on a regular basis. We assume users will use the application frequently enough that they will progress up that learning curve. For such an application, it is crucial that users be able to complete their work as fast as possible. In this scenario, a learnability study will determine how fast administrators learn to run a backup efficiently. We recruit several representative users and invite them to the lab. Then we ask them to perform the backup and measure how long they take to do so for the first time. Next, we ask them to come back into the lab and do the task for a second time — again, measuring their task-completion time. This process repeats for several more times. The result of our study will be a learning curve which plots the task time over a set number of trials.

![Learning curve with average time on task decreasing across six trials and a saturation point reached at the fourth trial.](https://media.nngroup.com/media/editor/2019/09/18/filebackup.png)

*This learning curve shows the hypothetical completion time for a backup as a function of the number of task repetitions (or trials). Notice that the time for the first repetition is longest, and then the completion time decreases — by trial 4, it levels off, reaching the saturation plateau. Although details such as how many repetitions are needed to reach saturation will vary from case to case, this learning curve is representative of all human learning.*

## Learnability vs Efficiency

There are 3 different aspects of learnability, each of which is important to different kinds of users:

- **First-use learnability**: How easy is it to use the design the first time you try? This aspect of learnability is of interest to those users who will only perform the task once. These users won’t progress up the learning curve, so they don’t care how it looks.
- **Steepness of the learning curve:** How quickly do people get better with repeated use of the design? This facet of learnability is particularly important for users who will use the design multiple times, even though they won’t use it excessively. If people feel that they are progressing and getting better and better at using your system, they’ll be motivated to stick with it. (And conversely, if people feel that it’s hardly getting better, no matter how hard they try, they’ll start looking for a better solution.)
- **Efficiency of the ultimate plateau:** How high is the productivity that users can reach with this interface, once they have fully learned how to use it? This aspect is particularly important for people with a frequent and long-lasting need to use the system — for example, when it’s the main tool for important everyday tasks.

Ideally, of course, your system should fare well on all 3 aspects. But, in the real world, design tradeoffs are often necessary, and you should shape the learning curve to cater mostly to those users who have the highest business value.

The relative importance of these dimensions also depends on the stages in the users’ lives. New users want to be able to learn the system quickly and get to the point of optimal (plateau) performance as soon as possible, but expert users want the plateau to be as low (i.e., the optimal task time as short) as possible.

Sometimes these different attributes of learnability may pull the design in different directions. For instance,**a learnable system is not always efficient**. Coming back to our example, let’s assume that the backup was performed through a step-by-step [wizard](https://www.nngroup.com/articles/wizards/) workflow with a lot of instructions and explanations. This system may be highly learnable: users may be able to perform the task as fast as possible even as they complete it for the first time. But the curve would be pretty much flat: they would not be able to perform it much faster the second time, as they would need to go through the same screens and answer the same questions. As users become well-versed in the interface, this design will feel like hand-holding and will be inefficient for repeated use. (It is for this reason that we recommend implementing [accelerators](https://www.nngroup.com/videos/flexibility-efficiency-use/), or process shortcuts, for expert users.) Designers must carefully balance learnability and efficiency.

![Learning curve with average time on task consistent across all six trials.](https://media.nngroup.com/media/editor/2019/09/18/backupwizard.png)

*This learning curve shows the hypothetical completion time for a backup application with a wizard flow as a function of the number of task repetitions (or trials). Notice that, despite the increase in trials, the task time stays steady around 16 minutes. This system is learnable but not efficient.*

## Why Measure Learnability?

High learnability contributes to usability. It results in quick system onboarding which translates to low training costs. Additionally, good learnability can result in high satisfaction because users will feel confident in their abilities.

**If your system and corresponding tasks are complex and ones that users access frequently, your product may be a good case for a learnability study**. Learnability studies are time and budget consuming, so don’t pitch them haphazardly to stakeholders. It wouldn’t make sense to measure learnability for tasks which users complete infrequently or one time (for example, signing up for a service or filing annual taxes) because users will most likely behave like new users each time they encounter the task. In these cases, a standard [usability test](https://www.nngroup.com/articles/quant-vs-qual/) would be better suited and more cost-effective than a learnability study.

## Running a Learnability Study

In learnability studies, we’re focused on gathering metrics, which is why we turn to [quantitative research](https://www.nngroup.com/articles/quant-vs-qual/) methods. This sort of study requires focused tasks and controlled experiments, and therefore **quantitative usability testing is best suited for studying system learnability**.

### Participants

In running this type of study, we’re trying to determine how easily people learn our interfaces. Therefore, it is important to **gather participants with little to no experience** using the system that they’ll be testing.

One consideration when it comes to testing learnability is prior experience with similar systems. Prior experience may help users (for example, because they may be already familiar with domain conventions) or may slow them down (for example, because they may suffer from [change aversion](https://www.nngroup.com/videos/users-hate-change/)). However, this data is still valuable, especially when launching a new product with the goal to steal customers away from existing products. When applicable, recruit participants with no similar system experience *and* participants with some similar-system experience, and plan to compare corresponding data from both groups.

As for any [quantitative study](https://www.nngroup.com/articles/quantitative-user-research-methods/), we recommend that you [recruit a fairly large number of participants](https://www.nngroup.com/articles/quantitative-studies-how-many-users/) (usually at least 30–40). The exact number will depend on the complexity of your task, with highly complex tasks requiring more participants to account for the inherently higher data variability, and simpler tasks requiring fewer participants.

### Step 1: Determine the Metric

**Time on task is the most commonly collected metric for learnability studies**. The reason is the [power law of learning](https://www.nngroup.com/articles/power-law-learning/), which says that the time it takes to complete a task decreases with the number of repetitions of that task. The rest of this article will assume you’re collecting time on task as the primary metric.

Depending on your system, time on task might not be relevant and therefore you need a different metric. In these situations, consider collecting the **number of errors** users make for a given task.

### Step 2: Determine the Number of Trials

The next step consists of deciding how often to collect these metrics — each instance of data collection is known as a trial.

Remember, we’re trying to plot this metric over time, so we need to have the **same participants complete the same task multiple times**. We recommend you **repeat the trials until a plateau is****reached.** A flattened curve indicates our participants have learned the system (specific to this task) as much as possible.

When considering trials, there are two questions you may be asking: how many trials should I run? And how far apart should the trials be? The answer to both of these questions depend on your circumstances.

To predict the number of trials needed for a user to reach a point of saturated learning, consider your system complexity. As a starting point, consider 5–10 trials but when in doubt, **plan for more trials than you think you need**, for two reasons: (1) you want to be sure that you’ve reached stable performance and (2) once you’ve reached a point of stable performance, it’s generally easier to cancel usability sessions than to schedule more.

If you’re wondering how much time is necessary between trials, consider how often you anticipate your customers to use the product and match that interval as closely as possible. For a task that users perform daily or a few times a week, you can have trials on consecutive days. But for tasks done once a month you may want to leave 4 weeks between trials.

### Step 3: Gather and Plot the Data

Remember to [recruit](https://www.nngroup.com/articles/recruiting-test-participants-for-usability-studies/) the same participants for each trial and have them complete the same task(s) in each trial. (This is different than the normal case, where you want [different test users to study different iterations](https://www.nngroup.com/videos/using-usability-test-participants-multiple-times/) of a design.) You may want to run a learnability study and test with multiple tasks. If this is the case, be sure to randomize your tasks to avoid biasing your results. In research studies, users take what they know from one task and apply it to future tasks; task randomization helps to mitigate this effect.

For each task, **calculate the metric averages for each trial** and plot them on a line graph with labeled axes. By plotting the data for each trial, you will obtain the learning curve for that task.

### Step 4: Analyze the curve

As with any quantitative study, you will want to analyze the data for statistical significance. In other words, you will have to investigate whether the trial effect was indeed significant — namely, whether the drop that you see in your learning curve is real or is just the result of noise in the data. Usually, the statistical method involved will be fairly simple — a [one-way repeated-measures ANOVA](https://en.wikipedia.org/wiki/One-way_analysis_of_variance) with trial as the factor.

Once you’ve done your analysis (and presumably found that the trial effect was significant), consider the big picture: What is the slope of your learning curve? Less-learnable interfaces have relatively small drops in the curve and take many trials to reach a point of saturation. Alternatively, highly learnable systems have curves that are steep and drop quickly and reach the saturation point after fewer repetitions.

For example, in our original file-backup example, it took users 4 trials to reach the saturation plateau and become efficient. That may seem acceptable. On the other hand, if it took them 30 trials to reach that same point, the learnability will likely be too low.

Also, consider the final efficiency: is it acceptable that, once users have learned how to perform the task, it will take them 10 minutes? The answer may depend on what that number is for competitor products. If a competitive analysis isn’t viable, you can also compare the findings to costs and [ROI](https://www.nngroup.com/articles/usability-roi-declining-but-still-strong/). If an administrator spends 10 minutes a day to complete a backup task in an optimal way and performs the task daily for a year, this amounts to 3650 minutes or approximately 60 hours. At a cost of $100 per hour, it means that the company will spend $6000 for completing the backups. Whether that amount is acceptable or may need to be lowered (by improving the design) will depend on the specifics of each product.

## Conclusion

The learnability of a product tells us how fast users reach optimal behavior with that product. It is important to measure learnability for UIs that get used relatively frequently. A learnability study involves repeated measurements of the same participants completing the same task. The result of a learnability study is a learning curve that will uncover how many repetitions are needed in order for users to complete the task efficiently.

Even if you don’t conduct a complete learnability research project to plot the full learning curve, thinking about these concepts will help you make the trade-off decisions to design products that target your most important customers.

For more on design tradeoffs, like learnability versus efficiency, check out our course, [Design Tradeoffs and UX Decision Frameworks](https://www.nngroup.com/courses/design-tradeoffs/).

### References

Tom Tullis, Bill Albert (2013) *Measuring the User Experience: Collecting, Analyzing, and Presenting Usability Metrics*. Morgan Kaufmann.

Allen Newell, Paul Rosenbloom (1980). [Mechanisms of skill acquisition and the law of practice](http://repository.cmu.edu/cgi/viewcontent.cgi?article=3420&context=compsci)*.* Technical Report. School of Computer Science, Carnegie Mellon University.
