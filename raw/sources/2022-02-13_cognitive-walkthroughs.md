---
title: "Evaluate Interface Learnability with Cognitive Walkthroughs"
date: "2022-02-13"
url: "https://www.nngroup.com/articles/cognitive-walkthroughs/"
author: "Kim Flaherty"
topics: [heuristic-evaluation, human-computer-interaction, web-usability]
type: article
---

## In This Article:

- [Defining Cognitive Walkthroughs](#toc-defining-cognitive-walkthroughs-1)
- [A Cognitive-Walkthrough Example](#toc-a-cognitive-walkthrough-example-2)
- [History of the Methodology](#toc-history-of-the-methodology-3)
- [Are Cognitive Walkthroughs Appropriate for All Types of Interfaces?](#toc-are-cognitive-walkthroughs-appropriate-for-all-types-of-interfaces-4)
- [When Should a Cognitive Walkthrough Be Conducted?](#toc-when-should-a-cognitive-walkthrough-be-conducted-5)
- [Cognitive Walkthroughs Compared to Heuristic Evaluations](#toc-cognitive-walkthroughs-compared-to-heuristic-evaluations-6)

## Defining Cognitive Walkthroughs

A **cognitive walkthrough** is a technique used to evaluate the [learnability](https://www.nngroup.com/articles/measure-learnability/) of a system from the perspective of a new user. Unlike user testing, it does not involve users (and, thus, it can be relatively cheap to implement). Like [heuristic evaluations](https://www.nngroup.com/topic/heuristic-evaluation/), [expert reviews](https://www.nngroup.com/articles/ux-expert-reviews/), and [PURE evaluations](https://www.nngroup.com/articles/pure-method/), it relies on the expertise of a set of reviewers who, in a highly structured manner, walk through a task and assess the interface from a new user’s point of view.

> A **cognitive walkthrough** is a task-based [usability-inspection method](https://www.nngroup.com/articles/summary-of-usability-inspection-methods/) that involves a crossfunctional team of reviewers walking through each step of a task flow and answering a set of prescribed questions, with the goal of identifying those aspects of the interface that could be challenging to new users.

A cognitive walkthrough takes place in a **workshop setting**. The user tasks to be evaluated within the session are defined in advance. (If you have a list of [top tasks](https://www.nngroup.com/videos/top-tasks-ux-design/), that’s a good source for evaluation tasks.) The workshop participants may include UX specialists, product owners, engineers, and domain experts.

One participant acts as a **facilitator**. All participants serve as **evaluators**, offering their interpretation of how a particular type of user (which could be defined by a [user persona](https://www.nngroup.com/articles/persona/)) would perceive the interface and behave in the given situation. Another participant serves as the **recorder**, documenting the answers found for each question and the probable success or failure of the overarching task (as determined by the group).

During the evaluation of a given task, the facilitator performs the task and stops at each new screen or other discrete step in the interaction. To establish whether the user is likely to succeed at this step of the flow, evaluators discuss 4 key questions (analysis criteria) meant to uncover potential causes for failure:

1. **Will users try to achieve the right result?** In other words, do users understand that the action (step) at hand is needed to reach their larger goal?
2. **Will users notice that the correct action is available?** In other words, is the interactive element that achieves the step visible or easily findable?
3. **Will users associate the correct action with the result they’re trying to achieve?** Perhaps the right button is visible, but will users understand the label and will they know to engage with it?
4. **After the action is performed, will users see that progress is made toward the goal?** Based on what occurs after the action is taken, will users know that this action was correct and helped them make progress toward their larger goal?

We discuss in detail [how to run a cognitive-walkthrough workshop in another article](https://www.nngroup.com/articles/cognitive-walkthroughs/).

## A Cognitive-Walkthrough Example

Let’s look at an example. Imagine a tablet interface used by health-clinic patients to check in for a visit and update their patient information. To assess the user experience using a cognitive walkthrough, the reviewers would focus on evaluating the steps that patients go through within the interface to complete these activities in preparation for their visit.

The key user tasks that should be evaluated using this methodology would include:

- **Checkin:** A patient new to the clinic (of a predefined persona) arrives for an appointment and is asked by the receptionist to check in using the provided tablet application.
- **Record update:**­ A returning patient (of a predefined persona) arrives for an appointment and is asked by the receptionist to review and update patient information and health history using the provided tablet application.

Let’s dive deeper into the first user task, patient checkin. During the cognitive-walkthrough session, the group begins by looking at the first screen that the user would encounter when trying to complete the checkin. In the example screenshot below, the correct action for the new patient would be to tap the square in the bottom right corner.

![Health Clinic Application](https://media.nngroup.com/media/editor/2022/01/04/health-clinic-application.png)

*Walkthrough evaluators would assess the first step in the patient-checkin flow for learnability. The correct action at this point is to tap the* New Patient *square.*

At this step in the walkthrough, the team would address the four analysis questions mentioned above:

Analysis Question | Group Determination | 1. | Will users try to achieve the right result? | Yes | : patients will be directed by a receptionist upon entry to check in for their appointment, and the application includes the phrase | Patient Check in | in the header. | Note: | Group discusses that there may be instances where the receptionist is away from the desk. Although the phrase | Patient Check in, | is shown in the app, its placement in the top right corner could be perceived as branding, causing it to be overlooked. They agree to further look for  design solutions for this situation. | 2. | Will users notice that the correct action is available? | Yes | : all action buttons are positioned within the body of the page using a highly salient visual styling that effectively communicates tapability. | 3. | Will users associate the correct action with the result they’re trying to achieve? | No: | the group discusses that selecting from the four options provided on the screen requires a lot of cognitive effort for new patients, because they must assess and eliminate the incorrect options before determining the correct one, | New Patient | . | Some patients may assume they have a patient record because they have an appointment. Others may simply see the | Patient Search | option first and take action before assessing the | New Patient | option. | The group agrees to further seek ways to simplify the design by first asking whether the patient is a new or existing patient and then providing returning visitors various record-lookup options. | 4. | After the action is performed, will users see that progress is made toward the goal? | Yes: | the page changes and a form with the heading | Enter your personal information | is displayed | .

After the team discusses the first action, it proceeds to the next step in the flow, addressing the same analysis questions until the task is complete. It is up to the team to decide how granular a step should be. For example, a form with 5 fields could be divided into 5 steps or kept as a single step. For efficiency purposes, we suggest keeping together smaller actions that are commonly executed as part of a group, such as a filling out a section of a form and hitting the *Next* button. The facilitator should determine in advance of the workshop what constitutes a step in the context of that task and system.

For each step that makes up the larger task flow, the group makes an overall determination as to whether the user will pass or fail at that step. If any of the questions results in a determination of *No*, the entire step would be marked as *Fail* by the recorder.

After all steps have been evaluated, the group summarizes fail points and discusses next steps.

## History of the Methodology

The cognitive walkthrough was first presented by Clayton Lewis and his colleagues in 1990. It was developed for evaluating walk-up-and-use interfaces such as kiosks and ATM machines, where the users’ ability to understand and use the interface with no prior knowledge or formal training is critical. The technique is rooted in cognitive science, specifically around the CE+ theoretical model that describes how people learn interfaces through exploration and problem solving. The cognitive-walkthrough methodology was developed based on this theory as a means to evaluate interface learnability.

The original methodology was time-consuming and laborious; over the years, it’s had multiple iterations and adaptations to make it feasible for product teams. A more straightforward and streamlined process developed by Cathleen Wharton and colleagues and based on the original technique was widely adopted for all types of interfaces, including applications and websites. This approach became the modern version of cognitive walkthroughs that is used today in UX.

## Are Cognitive Walkthroughs Appropriate for All Types of Interfaces?

Since cognitive walkthroughs are meant to evaluate learnability, they’re most effective for systems with complex, new, or unfamiliar workflows and functionalities.

The example we referenced earlier, a tablet application used at health clinics for patients to check in and update their information, is a good candidate for the cognitive-walkthrough methodology, because most users do not have a lot of previous experience with such applications, so they would not be able to refer to and employ existing [mental models](https://www.nngroup.com/articles/mental-models/) for how such applications work.

A website intended for the general public and that correctly employs standard design patterns would not be well suited for a cognitive walkthrough, because these patterns are so ubiquitous across the web that most users will bring enough knowledge from previous experience to be able to use the interface right away with no issues. Assessing the website learnability with such a fine-tooth comb as the cognitive-walkthrough method would be overkill. For example, conducting a walkthrough of a basic ecommerce checkout flow would not be necessary because nearly all users are very familiar with such flows.

For this reason, cognitive walkthroughs are best used to evaluate complex applications and systems that require new design patterns or interactions.

## When Should a Cognitive Walkthrough Be Conducted?

This evaluative methodology is best used during the development of a new system to uncover design problems that could hinder its learnability for new users. By walking through early conceptual prototypes and focusing on the cognitive processes that users go through as they explore the interface, product teams can identify opportunities for improvement.

Of course, a cognitive walkthrough should not be the only evaluative technique applied to a new interface. Usability testing would still be necessary during development, but walkthroughs allow teams to find problems without planning and conducting a formal usability study, which can be a costly effort.

## Cognitive Walkthroughs Compared to Heuristic Evaluations

With cognitive walkthroughs, the analysis is done by addressing a predefined set of exploratory questions from the user’s point of view at each step along the way until the goal is complete. This step-by-step process helps reviewers identify potential weaknesses and opportunities in the system.

This question-based evaluation approach applied to common tasks sets cognitive walkthroughs apart from [heuristic evaluations](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/), which are more general in nature. Heuristic evaluations help identify weaknesses and potential improvements by evaluating the entire product against a set of usability guidelines and best practices. They do not seek to explore users’ perspectives and reactions to the system. A comparison of these two approaches is outlined in the table below.

Heuristic Evaluation | Cognitive Walkthrough | Perspective | Analyst | New User | Target | General usability | Learnability | Scope | Comprehensive | Targeted activities | Method | Evaluation of interface against guidelines | Exploring potential user reactions and behaviors to the system

Both types of evaluations are useful for evaluating the usability of a product or experience. In fact, both methods could be applied together as part of a general evaluation effort, resulting in a comprehensive understanding of the system from both perspectives. However, it’s likely there will be some degree of overlap in the insights garnered from the two approaches.

### Conclusion

Cognitive walkthroughs are a proven way to evaluate the learnability of a system using a framework based on what is known about how humans assess and interact with new interfaces. This methodology is great for identifying improvements in instances when access to users or resources for usability testing may be limited. However, it is just one way to evaluate design and should ideally be coupled with other methods to ensure a comprehensive understanding of the effectiveness of a product’s design.

### References

Clayton Lewis, Peter Polson, Cathleen Wharton, John Reiman. 1990. Testing a Walkthrough Methodology for Theory-Based Design of Walk-Up-and-Use Interfaces. In *Proceedings of* the SIGCHI Conference on Human Factors in Computing Systems (CHI ’90), April 1-5 1990, Seattle Washington USA, Association for Computing Machinery, New York, NY, 235-242, [https://dl.acm.org/doi/10.1145/97243.97279](https://dl.acm.org/doi/10.1145/97243.97279)

Cathleen Wharton, John Reiman, Clayton Lewis, Peter Polson. 1994. The cognitive walkthrough: A practitioner’s guide. In Jakob Nielsen, Robert L. Mack (ed.) *Usability Inspection Methods*, John Wiley & Sons Inc, New York, New NY. DOI: [https://dl.acm.org/doi/book/10.5555/189200](https://dl.acm.org/doi/book/10.5555/189200)
