---
title: "Internal vs. External Validity of UX Studies"
date: "2021-02-14"
url: "https://www.nngroup.com/articles/internal-vs-external-validity/"
author: "Raluca Budiu"
topics: [research-methods, user-testing]
type: article
---

Any UX-research study aims to answer general questions about our design or about our users. What percentage of our user population will be able to subscribe to our newsletter? What major usability issues will people encounter on our site? Is design A more usable than design B for our target audience? But any time we set up a UX-research study, whether [quantitative or qualitative](https://www.nngroup.com/articles/quant-vs-qual/), there is danger that it will not reflect the reality we want to capture because the study is poorly designed.

There are two big types of study-design errors:

1. **Internal-validity** errors that bias participants towards a certain response or behavior
2. **External-validity** errors that capture behaviors or situations which are not characteristic for our target audience

We’ll talk about each of these separately. But before we do, let’s note that **validity is separate from****reliability**. Reliability of a study simply means that you will get the same result if you repeat the study. In other words, findings are not random. There are plenty of statistical methods to calculate the degree of study reliability, and the main way to increase reliability is to test more participants. But **reliability is no good without validity**: a study with high reliability and low validity is one where you get a really good measurement of the wrong thing.

## In This Article:

- [Internal Validity for UX Studies](#toc-internal-validity-for-ux-studies-1)
- [External Validity](#toc-external-validity-2)
- [Recommendations for Study Design](#toc-recommendations-for-study-design-3)
- [External validity](#toc-external-validity-4)
- [Conclusion](#toc-conclusion-5)

## Internal Validity for UX Studies

Think of a study that compares two sites — site A and site B. You are trying to decide which of the two is better and you always show the participants in your study design A first, ask them to complete some tasks on it, then move to design B and show them the same tasks. Is this study design likely to produce accurate results, that reflect the reality? In other words, will this study identify the better design?

Not necessarily. This study setup favors design B because, when they get to it, participants will be already used to the testing situation and with the task domain — if they’re testing car-rental sites, they will already know what a LDW (loss-damage waver) is when they get to site B and they may have certain expectations regarding the steps of the rental process. They will also know what you expect them to do and how they’re supposed to perform the task. Therefore, this study is missing internal validity. (The usual fix to this problem is to alternate which site goes first, and have half of the users try site B first.)

Definition: A study has **internal validity** if it does not favor or encourage any particular participant response or behavior.

Internal validity is an issue in both qualitative and quantitative studies. With moderated qualitative studies, the facilitator may inadvertently [bias or eliciting a certain response](https://www.nngroup.com/articles/leading-questions/) from the participants. For example, even a simple questions such as “Have you found the checkout difficult?” may invalidate the study results because the participants are [primed](https://www.nngroup.com/articles/priming/) to think of difficulties, so they may identify more than normal (like with Richard Nixon’s “I am not a crook” statement).

With quantitative studies, lack of internal validity may produce results that skew in one direction, but do not reflect the reality. You may, for instance, in a [benchmarking](https://www.nngroup.com/articles/benchmarking-ux/) study, discover that your time on task is better on a redesigned version of the site than on the original and you may infer that you did a good job with the redesign, when in fact, the difference was due to different study protocols — the original test used the [think-aloud protocol](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/), but the test of the redesign didn’t. (And thinking aloud does take some extra time, so it can cause longer task times.)

In this example, the protocol is an example of a **confounding variable**— a hidden variable that can affect the results of your study, but that you didn’t take into account when you designed the study.

## External Validity

External validity is about how naturalistic your study is.

If you’re designing a site for seniors and recruit study participants from the general population, will that study be valid? Will it tell you something relevant about your real audience? Possibly not, because younger participants are likely to behave differently than older ones. Or, if you’re testing a mobile design on a desktop, will your findings generalize to the use of the design in the wild? Maybe yes, maybe no — it’s impossible to know for sure (unless you do another study). In both these situations, the studies are missing external validity.

Definition: A study has **external validity** if the participants and the study setup are representative for the real-world situation in which the design is used.

The concept of external validity also applies to both qualitative and quantitative studies — for obvious reasons.

## Recommendations for Study Design

Here are some recommendations to help you set up studies that are both internally and externally valid.

### Internal validity

Randomization is essential for ensuring internal validity.

1. **Use random ordering of tasks.**

Task order can bias task responses. At the beginning of a study, people are usually new to both the study environment and to the system that they’re testing. It’s normal for them to take longer to perform the first tasks in a session and perhaps make more errors than normal. On the other hand, tasks that are shown at the end of the session might see the effect of participant fatigue.

That is why we strongly recommend that in any test, whether qualitative or quantitative, you randomize the order of the tasks as much as possible. (Sometimes, however, following this recommendation may not be entirely feasible — for example, if the tasks are *Log in* and *Deposit check*, it may not be possible for *Deposit check* to follow *Log in*).

Additionally, to mitigate the learning phase at the beginning of every session, we recommend that you prepare 1–2 **warmup tasks** (psychologists call them **practice trials**) that are irrelevant for your study and that are meant to get participants familiar and comfortable with the study environment and the study procedure. I like to pick easy tasks that bolster participants’ confidence and make them feel relaxed. But, if you do use warmup tasks, make sure that you do not include them in your analysis.

1. If your study contrasts two or more conditions (e.g., you want to compare your site with a competitor site) and each participant will be exposed to all conditions (i.e., [within-subject design](https://www.nngroup.com/articles/between-within-subjects/)), **you should counterbalance or randomize the order in which each participant is exposed to those conditions** (for instance, the order in which they see your site and your competitor’s).

This recommendation is related to the previous one — randomizing the task order. However, if you’re testing, say, 2 ecommerce sites, sometimes it may be unrealistic or unfeasible to ask the participant to shop on site one, then add an item to a wishlist on site 2, then go back to site 1 and subscribe to the newsletter, then shop on site 2 — this would be a detrimental and possibly confusing setup, if you want, for instance, to collect post-test questionnaires such as [SUS](https://www.nngroup.com/articles/measuring-perceived-usability/) and [NPS](https://www.nngroup.com/articles/nps-ux/) for the two designs at the end of the session.

In that situation, we recommend that you group all the tasks for design 1 together and all the tasks for design 2 together. You should, however, randomize the order in which participants see the two designs — with some participants seeing design 1 first and others seeing design 2 first. And, within each design itself, the order of tasks should be randomized.

1. **Control study setup from one session to the next and look for confounding variables —** hidden factors that could affect your results.

For example, assume a researcher is interested in comparing two sites and uses a between-subject design. She decides to study site A with the participants in the morning sessions and site B with those participants coming for afternoon sessions. If she ends up finding that participants perform better on, say, site A, it could be because site A is better, or it could be because people are less tired in the morning.

Similarly, if a colleague helps you facilitate a study and you divide the sites — you take the sessions with site A and she takes site B, the facilitator is a hidden variable. It could be that one facilitator’s style is more biasing than the other or that one facilitator is a naturally a more pleasant person and participants feel more talkative and relaxed with her.

Thus, if you know that there will be any factors that will need to vary from one session to the next, ensure that they vary for all the conditions in your study.

When you put together a benchmarking program for your organization, planning carefully for internal validity is essential. You have to document very carefully your study conditions (task wording, study protocol, whether think-aloud was used, and so on) so that they could be replicated in further studies that you will run in order to determine design improvements over time. Otherwise, a difference between a current version of a system and a prior installment may simply be due to study setup rather than to usability improvements.

## External validity

1. **Recruit participants who are representative of your target audience**— both in terms of demographics and user goals.

In general, researchers are very careful with creating [screeners](https://www.nngroup.com/articles/screening-questions-select-research-participants/) that match the exact demographics of their population, yet that may not be enough to ensure external validity. It could be that your participants are in the right demographics but have very different goals than your users (or they’re simply not motivated enough). Always strive to find participants who are likely to have the same goals as your users.

1. **Replicate, to the best of your abilities, the natural situation** in which participants will use the UI that they test.

Are your participants supposed to use your car-repair mobile application in their garage? Then don’t have them test it in a conference room. The environment — light, dirty hands, place where the phone is positioned, time available, tools available — are all likely to play a role in how usable this app is.

However, sometimes it may be impossible for a study to be externally valid.

### Is External Validity Always Possible?

In some sense, any study will lack external validity — we rarely use interfaces with a stranger watching over our shoulder, sitting at a desk or in a lab. (To some extent, one could even argue that some [remote studies](https://www.nngroup.com/articles/remote-usability-tests/) are more externally valid than in-person ones because at least the participants may be in their natural environments.) We also know that participants tend to behave slightly differently — more compliant and more persistent — in a usability-testing situation than by themselves.

Also, sometimes, it may be too cost-prohibitive to test a design in the natural environment. For example, we are great advocates of [paper prototyping](https://www.nngroup.com/articles/paper-prototyping/), but these types of tests will always lack external validity. So, what should we do?

In these situations, some testing is better than no testing. With paper prototyping, it may be that your results are not externally valid and you will have to retest later on in naturalistic conditions. But the goal of paper prototyping is to identify any big hurdles so that you won’t spend money implementing something that is completely off. So, run a paper-prototyping study, identify the big issues, fix them, then move forward to a [high-fidelity prototype](https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/) that you could test in naturalistic conditions, on the device that participants will use to complete the task.

Another common situation that lacks external validity is [mobile testing](https://www.nngroup.com/articles/mobile-usability-testing/) — most participants will not use mobile designs uninterrupted, sitting at a desk, and connected to wifi. It can, however, be acceptable to test in that setup to identify those issues that will be encountered even in the best-case scenario of a great connection and no interruptions. Those are likely the first issues many mobile sites will need to address — if the site has problems even under ideal conditions, then the design needs to be fixed. Once you’ve ironed out those issues, you still will need to retest under more realistic conditions.

Similarly, some quantitative-study professionals recommend to include only expert participants in certain quantitative studies in order to reduce variability (lack of variability translates into a lower margin of error for the study results and may allow the researchers to reduce the number of participants). The expert users will give you a best-case scenario and you should be fine as long as you don’t assume that the results will generalize to all your users.

In general, if you find yourself forced to sacrifice some external validity, it’s crucial that you always interpret your findings in context and realize that they may not stand true if the study were to be replicated in realistic conditions.

## Conclusion

Poorly planned research will translate in results that are invalid. You may have potentially wasted time and money on running a study which doesn’t tell you anything about your product or your audience. Pay attention to your study’s internal and external validity — strive to recruit participants that are representative of your target audience and make sure that the study setup replicates how your users will use the system in real life and that it does not encourage any one behavior or response.
