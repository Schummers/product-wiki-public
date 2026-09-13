---
title: "Flexibility and Efficiency of Use (Usability Heuristic #7)"
date: "2020-11-22"
url: "https://www.nngroup.com/articles/flexibility-efficiency-heuristic/"
author: "Page Laubheimer"
topics: [heuristic-evaluation]
type: article
---

I am not an accomplished cook. I can follow a recipe and get reasonably edible results, but it takes me a long time and a lot of concentration. If I don’t prepare for cooking by reading through a full, detailed recipe, laying out all of the ingredients beforehand in groups that will be used together, and googling a few advanced techniques, I’ll be left with a burned dinner. I have a few friends that know what they’re doing in the kitchen and I’m always amazed at all the little shortcuts they take when cooking. The first time I cooked with my friend Nick many years ago, I was laboriously cutting up basil leaves, putting a ton of concentration into trying to keep the slices of similar size and not chop off my fingers in the process. Nick walked over, grabbed a handful of basil leaves, tucked them one inside another and gently rolled it like a tiny cigar. He then quickly sliced his bundle of basil a few times, getting perfect consistency in the cuts and taking almost no time at all. He then gave me a wink and moved on to another part of the recipe while I stood there, gobsmacked at how efficient and precise he was.

Like in the kitchen, in UX we must accommodate people with a variety of competencies. Our systems should be flexible enough to allow users to complete a given task using a variety of methods. Flexible systems are efficient because people can choose the method that works best for them. The 7th of the [10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) says that we should prioritize flexibility and efficiency of use through the use of shortcuts and accelerators — unseen by the novice user — which speed up the interaction for expert users. This approach allows a system to cater to both inexperienced and experienced users.

## In This Article:

- [Novice and Expert Users Have Different Needs](#toc-novice-and-expert-users-have-different-needs-1)
- [Multiple Methods to Accomplish the Same Task](#toc-multiple-methods-to-accomplish-the-same-task-2)
- [Accelerators Improve Repetitious Usage](#toc-accelerators-improve-repetitious-usage-3)
- [Summary](#toc-summary-4)

## Novice and Expert Users Have Different Needs

New users often require guidance when using a system and need clear and obvious options because they have not yet developed a [mental model](https://www.nngroup.com/articles/mental-models/)of how the system works. Novice users rely heavily on [step-by-step wizards](https://www.nngroup.com/articles/wizards/) or [clearly labeled menus](https://www.nngroup.com/articles/category-names-suck/), for example, while [more-experienced users](https://www.nngroup.com/articles/novice-vs-expert-users/) learn [keyboard shortcuts](https://www.nngroup.com/articles/ui-copy/) or [touchscreen gestures](https://www.nngroup.com/articles/iphone-x/) to complete the same task. The expert users could still use the slower, more deliberate methods, of course, but get no benefit in doing so. Instead, they use a faster (but less guided) approach to the task. These faster, alternate methods of completing a frequent action are referred to as [accelerators](https://www.nngroup.com/articles/ui-accelerators/).

If a system caters primarily to new users by focusing on being very [learnable](https://www.nngroup.com/articles/measure-learnability/), repeat users will be slowed down because the system likely includes a lot more step-by-step handholding than a repeat user would need. So, the extra clicks to guide users through a wizard might be necessary to lead someone through a task the first time but extraneous for future repetitions.

On the other hand, if a system focused only on [efficiency for expert users](https://www.nngroup.com/videos/learnability-efficiency-ui-design/), it would probably be very difficult to learn. Keyboard combinations or performing a touch gesture are faster to execute than navigating through a sequence of menus to activate the same action, but place a higher burden on the user’s [memory](https://www.nngroup.com/articles/working-memory-external-memory/). Relying only on them would be like ditching a graphical user interface (GUI) altogether for a command-line one.

So, there are two different aspects to making a flexible and efficient system:

- Multiple methods to accomplish the same task according to one’s preferences
- Accelerators that don’t slow down inexperienced users, but speed up advanced users

## Multiple Methods to Accomplish the Same Task

A flexible and efficient system isn’t just about helping users transition from novice to expert use, it’s also about allowing users to approach tasks in multiple ways to suit their working style. This can be as simple as structuring functionality in an open-ended rather than a prescriptive way. For example, if you’re writing a bulk email that you’ll send to a large group with only small changes, you could:

- Type the same basic email over and over
- Copy and paste the email text and edit the parts that you want to differ for each recipient (such as their name)
- Send a single email to a large group (using bcc)
- Use a mail merge feature to separately address and send each email
- Integrate your email with a more advanced tool that allows for programmatic variables that pull information from a database into the email body

Each of these approaches will have (nearly) the same effect (sending the same email with a few small changes to a large group), but different levels of efficiency and control for the person sending the email. The effort to set up a full marketing automation system to send one email blast is probably not worth it due to high [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/), but having to do the task repeatedly might make the [tradeoff](https://www.nngroup.com/courses/design-tradeoffs/)worthwhile for experts.

(That said, the solution is not to simply [duplicate](https://www.nngroup.com/articles/reduce-redundancydecrease-duplicated-design-decisions/)functionality in multiple places, as [excessive duplication](https://www.nngroup.com/articles/duplicate-links/) makes systems harder to learn. Duplication can manifest either as functionality overlap or as positioning the same feature in several places in the UI. In both situations, users need to learn what the difference between the duplicated commands is, if any.)

There is a bit of natural tension between helpful flexibility and detrimental duplication; making the right decision involves systematically assessing appropriate tradeoffs, based on evidence of what is helpful for *your* users.)

Beyond simply structuring functionality to allow for open-ended approaches, another way that we can allow users flexibility in how they perform tasks is to enable expert users to **customize** the interface to suit their unique (and often dynamically changing) needs. For example, a user may set up and toggle through multiple window arrangements (known as *workspaces* or *screensets*) in an application.

![Logic Pro X two screensets (arrangements of windows) that are saved and easily recallable.](https://media.nngroup.com/media/editor/2020/11/04/logic-pro-screensets-sm.jpg)

*Logic Pro X features* Screensets *, a type of customization where users can set up their windows into arrangements that can be recreated with a single keystroke or through the menu. This capability allows power users to flexibly (and efficiently) customize their display throughout the various subtasks involved in recording or mixing music. Changes to an individual screenset (by adjusting window sizes as part of normal workflows) persist when the user recreates that screenset later.*

However, even though customization can provide flexibility to a UI and support special needs or work habits for some users, don’t rely on it, because most users [won’t bother to customize](https://www.nngroup.com/articles/customization-of-uis-and-products/) the system.

Some systems use personalization instead of customization — by automatically customizing the UI to the individual user. [Personalization](https://www.nngroup.com/articles/personalization/) can be expensive to get right and annoying if done poorly. But role-based personalization works well for enterprise tools. It’s also worth considering a simplistic approach to personalization that saves settings across one user’s different sessions — for example, by remembering the parameters used for a command the last time it was used, like Excel remembers the previous sort order for a column (e.g., descending) when you re-sort it.

## Accelerators Improve Repetitious Usage

Accelerators are *secondary* ways of accomplishing the *same* task that function as faster (but typically less obvious) methods. An example of an accelerator is how modern mobile keyboards allow users to perform a swipe gesture over the letters to input text, rather than tapping each individual letter. This gesture is an [enhancement](https://www.nngroup.com/articles/enhancement/): it doesn’t get in the way of a new user (who very likely is not aware of it at all), but can save a lot of time to a seasoned user.

![iOS swipe keyboard gesture interactions for typing](https://media.nngroup.com/media/editor/2020/11/04/swipe-keyboard-accelerator-sm.gif)

*The iOS keyboard allows swiping through the letters of a word instead of tapping them individually. This gesture is an accelerator: it helps experienced users but does not make typing harder to learn for novices.*

The trick for designing a usable accelerator is making it [discoverable](https://www.nngroup.com/videos/findability-vs-discoverability/)(which mobile keyboard gestures lack) but unobtrusive. The classic solution for keyboard-shortcut accelerators is to show them next to the associated commands in a menu or toolbar. A novice user doesn’t have to pay attention to the keyboard shortcut at all, but repeated exposure to it supports learning for experienced users.

![Photoshop showing keyboard commands when hovering over a toolbar icon](https://media.nngroup.com/media/editor/2020/11/04/photshop-accelerator-key-sm.jpg)

*Adobe Photoshop shows unobtrusive messages to indicate how to access the keyboard-shortcut accelerator (W in this case) for toolbar items in a small overlay that appears on hover.*

Macros are another way to increase flexibility and efficiency; they’re somewhat of a middle ground between user-defined customization and system-created accelerators. Macros allow users to run a series of commands with a single trigger, allowing expert users to automate repetitious or tedious tasks that have predictable steps. (Excel users may be familiar with macros created either by recording a series of mouse clicks and keystrokes or by writing a script.) Macros are not the only way to efficiently process batch actions, however; simple features allowing users to select multiple items in a table (e.g., by checking corresponding checkboxes) and run a command on all of them are also accelerators.

![Airtable screenshot showing the macros functionality](https://media.nngroup.com/media/editor/2020/11/04/airtable-macros-sm.jpg)

*Airtable offers* Automations *, a macro functionality that allows power users to chain together multiple actions that can be automatically triggered. Airtable also offers more-traditional checkboxes for each row in the table to allow users to take bulk actions (such as coloring or filtering) on multiple rows simultaneously. Both of these features are types of accelerators, but they have different levels of required user effort.*

## Summary

The 7th usability heuristic (flexibility and efficiency of use) is about allowing users to approach tasks in a variety of ways. New users may require guidance in performing their tasks, whereas experienced users can take advantage of accelerators and other secondary features designed to speed up commonly performed actions. Embracing this heuristic means allowing user customization, not being prescriptive about core task steps, and adding unobtrusive accelerators that power users can discover and employ efficiently.
