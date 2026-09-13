---
title: "How to Conduct a Cognitive Walkthrough Workshop"
date: "2022-04-10"
url: "https://www.nngroup.com/articles/cognitive-walkthrough-workshop/"
author: "Kim Flaherty"
topics: [heuristic-evaluation]
type: article
---

A [cognitive walkthrough](https://www.nngroup.com/articles/cognitive-walkthroughs/) is a technique used to evaluate the [learnability](https://www.nngroup.com/articles/measure-learnability/) of a system. Unlike user testing, it does not involve users (and, thus, it can be relatively cheap to implement). Like [heuristic evaluations](https://www.nngroup.com/topic/heuristic-evaluation/), [expert reviews](https://www.nngroup.com/articles/ux-expert-reviews/), and [PURE evaluations](https://www.nngroup.com/articles/pure-method/), it relies on the expertise of a set of reviewers to assess the interface.

Although cognitive walkthroughs can be conducted by an individual, they are designed to be done as part of a group in a **workshop setting** where evaluators walk through a task in a highly structured manner from a new user’s point of view.

## In This Article:

- [Preparing for a Cognitive Walkthrough Workshop](#toc-preparing-for-a-cognitive-walkthrough-workshop-1)
- [How Long Does a Cognitive-Walkthrough Session Last?](#toc-how-long-does-a-cognitive-walkthrough-session-last-2)
- [Output and Next Steps](#toc-output-and-next-steps-3)
- [Resources](#toc-resources-4)
- [References](#toc-references-5)

## Preparing for a Cognitive Walkthrough Workshop

Before you start the evaluation, there are a number of decisions to be made up front.

### Determine Who Will Participate

In a group evaluation, you should seek to include 2–6 evaluators of varying roles. Each role brings a different perspective to the walkthrough and, thus, ensures that the evaluation is comprehensive.

Below is a (nonexhaustive) list of individuals you might consider including as evaluators in a cognitive-walkthrough workshop.

- **Product experts** with intimate knowledge of the product being tested — for example, a UX designer or product owner that has been working on the system
- **One or more UX practitioners****who have a strong body of knowledge in human-computer interaction or cognitive science**. Because the evaluation aims to assess how people will think and behave when faced with an interface, this knowledge is useful in making those determinations. These experts can, but do not need to be working directly with the system being evaluated.
- **Engineers.** Including those who are building the system in the cognitive walkthrough brings another perspective to the table and builds ownership of the user experience among engineers. These analysis sessions will also help engineers learn the importance of UX and pick up key considerations for future implementation work.
- **Domain experts** who bring expert knowledge of the realm in which the product operates. For example, if the system serves a complex field of business such as finance or insurance, consider including someone with strong knowledge of that area.

### Define the Inputs

When preparing for a cognitive-walkthrough session, you must first define the conditions for the evaluation. There are four questions to answer before you begin:

1. **From which users’ perspective(s) will we evaluate?**

Even if the user audience for your system may be general, the technique is most effective if you have some high-level context for the users of the interface. For this reason, you should use your user [personas](http://nngroup.com/articles/persona/) as the basis for the walkthroughs. If you do not have personas, it’s strongly recommended that you develop personas for use in the walkthrough (and, more generally, for the development of the system).

Personas give you basic information about a type of user’s attitudes, beliefs, prior knowledge, and common behaviors. This information helps you determine whether users will understand the interface and how they will behave, and thus reduce the risk that the evaluators will base their comments on fantasy users. You will conduct one walkthrough per persona.

1. **What task(s) will we analyze?**

Websites and applications typically support many user tasks. You will walk through one supported task at a time, so you must decide which tasks are the most important. Consider which tasks are core activities in the system — tasks that many users will engage in or that are so critical that user errors would result in catastrophic or life-threatening consequences.

1. **What is the correct sequence of actions to complete the task?**

Define a list of underlying steps that must be taken in the interface to accomplish a task.

We’ll use a sample task from a web-based expense-reporting application, Certify, as an example. Let’s say the cognitive walkthrough we intend to conduct has the following inputs and action sequence:

- **Persona:** Pamela, a new employee at the company.
- **Task:** Pamela needs to resolve a duplicate-expense error in her expense report.
- **Action sequence:** We’ll assume Pamela already has already created her first expense report.

Below is the sequence of correct actions for her task. Several actions require the user to complete a form or review a page and click Next, in order to streamline the evaluation, we will combine these into a single action.

![step 1 select duplicate expense error](https://media.nngroup.com/media/editor/2022/02/09/step-1-duplicate-expense-errors.jpg)

*Step 1. Select the* Play *icon next to the exclamation-point icon on one of the expenses in error.*

![step 2 - merge expenses](https://media.nngroup.com/media/editor/2022/02/09/step-2-merge-expenses.png)

*Step 2. Select the* Merge *Expenses link.*

![step 3 - confirm merge](https://media.nngroup.com/media/editor/2022/02/09/step-3-confirm-merge.png)

*Step 3.  Approve the merge in the* Confirmation *modal.*

Be sure to write these action sequences down explicitly for use in the walkthrough.

Because some activities may have various pathways to completion, you may need to start with a primary path and subsequently define alternative paths. It’s best to formally define these steps and variations in advance, to ensure the group is not derailed by debate during the walkthrough.

1. **What version of the interface (prototype, live site, etc.) will we evaluate?**

Cognitive walkthroughs are often done during the development of a new system, so they can be conducted on [prototypes of varying levels of fidelity](https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/) — ranging from [paper prototypes](https://www.nngroup.com/articles/paper-prototyping/) to clickable functional prototypes. They can also be conducted on existing systems to elicit ideas and identify opportunities for improvement. The fidelity of the interface will clearly set limits on the scope of your evaluation. For example, a paper prototype will not allow you to assess the influence of color or realistic imagery on the activity.

### Establish Roles and Rules

Cognitive walkthroughs, like most well-run workshops, rely on clear rules and assignment of participant roles. It’s possible to wait until the beginning of the evaluation session to discuss roles and rules, but doing so in advance of the meeting can maximize the time for evaluation.

#### Key Roles

1. **Facilitator:** The [facilitator is typically the organizer of the session](https://www.nngroup.com/articles/workshop-facilitation-101/). This person is responsible for making sure that participants are prepared for the session and ensures that the discussion is in line with the purpose and rules of the meeting, so the session runs as smoothly as possible.
2. **Presenter:** The presenter’s job is to make the prototype viewable to the entire group and serve as a proxy for the user, interacting with the interface as the group determines the users would. The facilitator may double as the presenter if necessary.
3. **Recorder:** The recorder captures the output of the cognitive-walkthrough discussions and the determinations made by the larger group. This person will also summarize the findings of the group after the session is finished.
4. **Evaluators:** Most meeting participants serve as evaluators. The facilitator, presenter, and recorder can also serve as evaluators. Evaluators follow along with the presenter or facilitator and assess the interface by responding to the prompts defined by the cognitive-walkthrough methodology, which is discussed later in this article.

#### Ground Rules

To ensure that the meeting is efficient and stays focused on task, communicate basic ground rules for evaluators. With practice, you will learn what ground rules make sense for your team; below we list a few key rules you might start with:

1. **The conversation should remain focused on user reactions to the existing experience.** The walkthrough session is not the time for brainstorming or recommending design changes.
2. **Participants should not justify or discuss reasoning** behind the current design of the interface.
3. **Participants should keep their laptops closed and avoid** multitasking during the session.

The facilitator will remind everyone of the ground rules during the walkthrough.

### Gather Materials and Plan Logistics

The facilitator should ensure that the following materials are ready for use in the session:

1. **The prototype** to be evaluated and a plan for how it will be presented to the group
2. **The formal action sequences** for the tasks being analyzed. These should be written down and distributed or presented by the presenter for each task evaluated.
3. **The personas that will be used for the evaluation.** Consider also distributing these as documents to each participant; alternatively, the facilitator may also briefly review the personas at the beginning of the session.
4. **Materials for recording the outcomes** of the walkthrough (as discussed later in this article)

### Conducting the Cognitive Walkthrough

1. **Brief the participants** at the beginning of the session. Describe the purpose of the meeting, which task(s) will be evaluated, and on behalf of which personas. Review the basic ground rules and discuss or assign roles for the analysis.
2. **Review the customer segment or persona** before starting the walkthrough. Discuss prior relevant knowledge that users would have as they approach the activity.
3. **Introduce a task and brief participants** on the predefined action sequence for its successful completion.
4. **Walks through that task**. Led by the facilitator and the presenter, the group goes through each individual action of the predefined action sequence one by one, determining success or failure, as discussed below.

#### Determine Success or Failure for Each Action

**The evaluators’ goal is to determine whether the user is likely to succeed at each step in the predefined action sequence; they should also document why that determination was made.**

In order to determine whether the user is likely to succeed, evaluators should discuss 4 key questions (analysis criteria) at each step:

1. **Will users try to achieve the right result?**
2. **Will users notice that the correct action is available?**
3. **Will users associate the correct action with the result they’re trying to achieve?**
4. **After the action is performed, will users see that progress is made toward the goal?**

To streamline the recording process during the walkthrough, it is helpful to utilize a recording tool or template for each predefined step in the action sequence of the task. Below is a printable template we recommend for recording the group’s decisions manually. This template and digital-form option are included for download at the end of the article.

![blank cognitive walkthrough template](https://media.nngroup.com/media/editor/2022/02/09/blank-cog-walkthrough-template2.jpeg)

*Example template for recording success or failure at each step of the cognitive walkthrough.*

The recorder fills in the overarching task and the specific step. For each of the four analysis questions, the recorder marks the appropriate answer — *yes* or *no*. For each question, the group should be able to explain why this is the correct answer.

- **If the answer is yes ,** there are some common reasons for success for each question. To streamline the recording process, we’ve included these common reasons in the *Yes* column of the template (*from experience, the system tells them so,* etc.). If one of these reasons applies, the recorder can simply circle the appropriate reason. If the reason is not given, the recorder should write the reason for the *Yes* determination in the cell below.
- **If the answer is no ,** the recorder should also write why exactly this determination was made by the group.

Below we’ll show how the evaluation template might be filled out for 2 of the 3 actions in the action sequence for our expense report example.

![step 1 screenshot](https://media.nngroup.com/media/editor/2022/02/09/step-1-duplicate-expense-errors.jpg)

*The presenter would show this interface so the group can evaluate it and complete the evaluation template for step 1 of the action sequence (below).*

![Step 1 evaluation form - fails third question. The user will not associate the correct action with the effect they're trying to achieve.](https://media.nngroup.com/media/editor/2022/04/22/cog-walkthrough-template-fail2.jpeg)

*The first action in the sequence failed the third analysis question; as a result, the action was recorded as a failure in the tip right corner.*

![step 2 - merge expenses](https://media.nngroup.com/media/editor/2022/02/09/step-2-merge-expenses.png)

*The presenter would show this interface (the next in the sequence) so the group can evaluate it and complete the evaluation template for step 2 of the action sequence (below).*

![Step 2 evaluation form succeeds against all four analysis questions.](https://media.nngroup.com/media/editor/2022/02/09/step-2-eval-select-merge-expenses-link.jpeg)

*The second action in the sequence passed all analysis questions and was recorded as a success in the top right corner.*

Lastly, the recorder circles the overall success/failure determination for the step in the top right corner. The overall success for the step requires a checkmark in the *yes* column for each of the four criteria for analysis. However, for the step to be marked as a failure, it needs a *no* for only one of the four criteria.

If your team determines that the user would fail at any step of the action sequence, note the problem and proceed to analyze the next step as if the current one had been successful. That is, assume that the system gave feedback for the correct action and is now in the state corresponding to the successful action. (This approach guarantees that, even if the walkthrough identified a problem with one step, subsequent steps can still be analyzed.)

Action | Determination | Select the | Play | icon next to the exclamation | - | point | icon on one of the expenses in error. | Fail | Select the | Merge Expenses | link. | Success | Approve the merge in the | Confirmation | modal. | Success

## How Long Does a Cognitive-Walkthrough Session Last?

The length of a cognitive-walkthrough session is up to the facilitator, the participants involved, and the complexity of the tasks that are analyzed. It’s generally possible to evaluate two full tasks in a 90-minute session.

## Output and Next Steps

After the group has finished evaluating each step for the defined tasks, the workshop concludes. The recorder should package up the completed templates for each tasks into a shareable format. The session facilitator should then summarize the overall findings of the session and track the identified areas for improvement in the project-management tool used to track work.

## Resources

- [Printable step template](https://media.nngroup.com/media/editor/2022/02/09/blank-cognitive-walkthrough-template.pdf)
- [Google Forms version](https://docs.google.com/forms/d/11iY0gmA-QyJBWpdNGAPQHiCOYVQY4Yi4UGjGCG24Ujw/copy)

## References

Clayton Lewis, Peter Polson, Cathleen Wharton, John Reiman. 1990. Testing a Walkthrough Methodology for Theory-Based Design of Walk-Up-and-Use Interfaces. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’90)*, April 1-5 1990, Seattle Washington USA, Association for Computing Machinery, New York, NY, 235-242, https://dl.acm.org/doi/10.1145/97243.97279

Cathleen Wharton, John Reiman, Clayton Lewis, Peter Polson. 1994. The cognitive walkthrough: A practitioner’s guide. In Jakob Nielsen, Robert L. Mack (ed.) *Usability Inspection Methods*, John Wiley & Sons Inc, New York, New NY. DOI: https://dl.acm.org/doi/book/10.5555/189200
