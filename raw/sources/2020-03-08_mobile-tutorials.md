---
title: "Mobile Tutorials: Wasted Effort or Efficiency Boost?"
date: "2020-03-08"
url: "https://www.nngroup.com/articles/mobile-tutorials/"
author: "Alita Kendrick"
topics: [applications, design-patterns, mobile-and-tablet-design]
type: article
---

There are several different methods that mobile apps use to onboard new users: tutorials, interface tours, gamified onboarding, contextual help, and so on. But, do these methods work? In other words, do they have an impact on users’ performance and their success using the interface? And subsequently, is it worth the design and development effort to create these onboarding tools?

We conducted a [quantitative usability test](https://www.nngroup.com/articles/quant-vs-qual/)**with 70 users and 4 mobile apps** that used [deck-of-cards](https://www.nngroup.com/articles/two-basic-hypertext-presentation-models/) tutorials as a means to onboard users. This particular type of onboarding was selected as the focus of this study due to its popularity in mobile apps.

**Deck-of-cards tutorials contain help or tip screens that provide instructions for how to use an interface and are usually presented when a mobile app is first launched.**

*A deck-of-cards tutorial in the Movesum App: Notice instructional content like Swipe left to right to browse through different foods and Swipe up to set a daily goal found on the cards.*

## In This Article:

- [Methodology](#toc-methodology-1)
- [Procedure](#toc-procedure-2)
- [Key Findings](#toc-key-findings-3)
- [Study Limitations](#toc-study-limitations-4)
- [Conclusion](#toc-conclusion-5)

## Methodology

The **study was conducted as a**[between-subject](https://www.nngroup.com/articles/between-within-subjects/)**,**[remote unmoderated](https://www.nngroup.com/articles/unmoderated-usability-testing/)[quantitative usability test](https://www.nngroup.com/articles/quant-vs-qual/). We used [Userlytics](https://www.userlytics.com/) as our testing platform and for participant recruitment.

### Applications

We selected the following apps to test: Movesum, Brainsparker, LaunchCenter Pro, and Sketch.Book. All apps were iPhone apps. These apps are not highly complex applications and did not require specialized expertise or advanced training to use.

These mobile apps were chosen because 1) at the time of the study, they had tutorials, 2) they allowed users to skip or close the tutorial, and 3) the apps were not widely known (which made recruiting easier and prevented prior exposure to the app).

### Participants

Participants were diverse in age, location, and ethnicities. Besides participant diversity, the most significant factor for our participant recruitment was that they had not previously used or downloaded any of the four apps being tested. All participants were prior iOS users. Thus, these users could be expected to know general basics of mobile-app use, but not the specifics of using the apps in the study. (Note: participants signed up for a “Mobile App Study” and were not made aware of the purpose of the study at the time of recruitment.)

Participants were assigned to one of 2 groups:

- Group A always engaged with the tutorial.
- Group B always skipped the tutorial.

In total, we had 70 participants, 35 in each group.

### Tasks

For each app, users were asked to do the following actions (in this order):

1. Download the app from the app store and either complete or skip the tutorial (based on their group).
2. If participants were successful in completing the first action (namely downloading the app), they would then be presented with an in-app task, which was the primary task we measured. This task was always something that the tutorial “taught” users.

For example, here are the instructions for the Movesum app:

Group A: Deck-of-cards tutorial

1. Initial instruction: Download Movesum app from the app store. Launch the app and read through the overview.
2. Task: Set a target of 6500 steps.

Group B: Skipped tutorial

1. Initial instruction: Download Movesum app from the App Store. Launch the app and skip the overview (by clicking the X in the top right corner).
2. Task: Set a target of 6500 steps.

At the time of this study, Userlytics did not provide randomization, so we manually randomized the order of the apps being tested, in order to avoid order effects. This was done manually by splitting group A and group B into 6 separate subgroups for which we created separate tests and manually reordered the apps being tested. (If all users tested the apps in the same order, we may have seen better performance in apps tested later in the session, due to participants’ learning.)

## Procedure

Participants were asked to think aloud and mention anything they encountered that made them feel stuck or unsure about how to proceed. However, users were asked to complete the 4 tasks as quickly and accurately as possible.

## Key Findings

We collected [task success](https://www.nngroup.com/articles/success-rate-the-simplest-usability-metric/), [single-ease questionnaire (SEQ)](https://www.nngroup.com/articles/measuring-perceived-usability/), and [task-completion time](https://www.nngroup.com/articles/usability-metrics/) for each primary task — these were the [dependent variables](https://www.nngroup.com/articles/between-within-subjects/) in our experiment, with the independent variable being the act of engaging or not in the tutorial. We excluded those trials when participants were not able to download the app or complete the initial instructions. In total, we removed 13 trials (5% of total trials).

### Comparable Success Rates

We observed **comparable task success rates for the two conditions**. Task success across the four apps tested was **91%** for the those who read the tutorial (n=35) and **94%** for those who skipped the tutorial (n=35). This difference was not statistically significant (p=0.443): **basically, whether people viewed the tutorial or not, they were still very successful at completing the primary task.**

Part of the reason for the high success rates may be that the tasks in the mobile apps tended to be fairly simple. One participant in group A said, “to me, I didn’t even have to watch the tutorial, but I guess it’s there if you need it.”

*Group A, which read through tutorials, had an average task success of 91% while group B, which skipped tutorials, had an average task success of 94%.*

### Easier Tasks When Participants Skipped Tutorials

After completing the second task for each app, we asked participants *“Overall, how difficult or easy was the task to complete? 1 (very difficult) to 7 (very easy).”* Across all the apps, group A, who read the tutorials (n=35), had an average SEQ of **4.92** while group B, who skipped tutorials (n=35), had an average SEQ of **5.49**. This difference was statistically significant (p=0.047). In other words, **participants who read tutorials perceived tasks (which were explained in the tutorials) as more difficult than those who skipped tutorials.** Half a point is a fairly substantial difference on a 1–7 rating scale.

**Group A, who read the tutorials, may have reported these tasks as more difficult because tutorials can make apps seem overly complicated.** We also observed this effect with [coach marks and instructional overlays](https://www.nngroup.com/articles/mobile-instructional-overlay/) in mobile apps. Users may expect a tutorial for complex applications, but for mobile apps, particularly those labeled as ‘easy’ or ‘intuitive’, a tutorial may shift users’ perception and make them think the app is more complicated than it really is.

*Group A, which read through tutorials, gave an average ease-of-use rating of 4.92 while group B, which skipped tutorials, gave an average rating of 5.49.*

### No Difference in Task-Completion Times

In what follows, we report task-completion times — that is times for those trials when users were able to complete the task successfully. (We carried out an analysis including all trials and the results were the same.)

Across all the apps, group A, who read the tutorials had a mean task-completion time of **93.49** seconds, while group B, who skipped tutorials had a mean task-completion time of **85.17** seconds. **This difference was not statistically significant** (p > 0.1): in other words, **reading the tutorials did not make users faster at completing the tasks described in the tutorial.**

(Because task times tend to be skewed to the right, instead of using the arithmetic mean — the traditional “average” — to describe the set of data, we used the [geometric mean](https://en.wikipedia.org/wiki/Geometric_mean). Confidence intervals reported below are also based on the geometric mean. To understand what the geometric mean is, when it should be used, and how to compute confidence intervals centered around it, see our class on [statistics for UX](https://www.nngroup.com/courses/ux-statistics/).)

Note that the task-completion times reported here did not include the upfront time to read the tutorial before using the app. (For example, for the MoveSum app, they reflect the time to use the app to set a target of 6500 steps.) If this reading time had been added, then obviously the total time would have been much higher for users who read the tutorial compared to those who did not. Since tutorial-reading time is a one-time expense, it’s not reasonable to include it in a per-task time metric, but seen from the perspective of total user burden, it’s still a downside for tutorials.

*For the in-app tasks, group A, which read tutorials, had a mean task-completion time of 93.49 seconds while group B, which skipped tutorials, had a mean task-completion time of 85.17 seconds.*

## Study Limitations

This study focused on 4 iOS applications. Thus, it is technically possible that:

1. It may not generalize to Android applications.
2. It may not generalize to other iOS applications (with perhaps slightly different characteristics), due to the low number of apps included. (In other words, it’s possible that, by chance, these 4 chosen tutorials were not particularly effective.)

These objections are valid. However, in recent years, we’ve observed that the UIs for Android and iOS devices tend to converge, so there’s little reason to believe that tutorials on Android apps will have a different effect.

## Conclusion

Think twice about creating a tutorial for simple applications. **Tutorials take time and effort to design and develop, and those would be better spent on making the UI easy****to use** and thus alleviating the need for a tutorial in the first place. We already know that many participants skip tutorials when they first download an app. But now we’ve found that participants who read tutorials perceive tasks as more difficult and they don’t show any advantage in terms of success rates or task-completion times compared with people who skip the tutorials. **If, even when people read these tutorials, they don’t make a positive impact, are these tutorials worth building**?

Instead of a tutorial acting like a polished manual, consider whether you need formal onboarding and if you do, consider interactive methods of doing so, like [contextual help](https://www.nngroup.com/videos/just-in-time-help/).
