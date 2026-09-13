---
title: "Accelerators Maximize Efficiency in User Interfaces"
date: "2024-10-18"
url: "https://www.nngroup.com/articles/ui-accelerators/"
author: "Aurora Harley, Rachel Krause"
topics: [design-patterns]
type: article
---

Designing for expert users requires **balancing**[learnability](https://www.nngroup.com/articles/measure-learnability/)**with efficiency**. While new users need an intuitive interface to start quickly, expert users demand features that improve speed and productivity over time. Any system that will be repeatedly used should cater to both new users and expert users by including **accelerators** to allow people to complete certain routine tasks quickly and easily.

## In This Article:

- [What Are Accelerators?](#toc-what-are-accelerators-1)
- [Examples of Accelerators](#toc-examples-of-accelerators-2)
- [Discoverability of Accelerators](#toc-discoverability-of-accelerators-3)
- [Accelerator-Design Best Practices](#toc-accelerator-design-best-practices-4)
- [Conclusion](#toc-conclusion-5)

## What Are Accelerators?

> An **accelerator** is a UI feature that speeds up an interaction or process.

Also referred to as **shortcuts**, accelerators [enhance user interfaces](https://www.nngroup.com/articles/enhancement/) by providing an alternate method for accomplishing a specific action and thus allowing expert users to **complete a common task more quickly** and efficiently. Accelerators should be **additional, alternate ways to accomplish a task** — something that expert users can take advantage of, but that others can ignore completely.

Accelerators make the system more **flexible and efficient** — one of the [ten usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/). A [highly flexible system](https://www.nngroup.com/videos/flexibility-efficiency-use/) satisfies both experienced and inexperienced users by allowing each to complete an action through whatever method works best for them.

Typically, all users hit an [efficiency plateau](https://www.nngroup.com/articles/measure-learnability/) once they have fully learned an interface, where further repetitions of a task do not significantly reduce the task time. Using an accelerator **helps expert users push past that plateau:** they can become even more efficient by adopting the faster method of completing that same task (once they have learned it, of course).

## Examples of Accelerators

Common accelerators include:

- [Keyboard shortcuts](https://www.nngroup.com/articles/ui-copy/)**:** Ctrl+C for copy, Ctrl+V for paste
- [Gestures](https://www.nngroup.com/articles/contextual-swipe/)**:** Swipe-to-delete, double-tap to react, right click on a mouse, two-finger scroll on a trackpad
- [Voice commands](https://www.nngroup.com/articles/audio-signifiers-voice-interaction/)**:**“Start bedtime” to a voice assistant

## Discoverability of Accelerators

Because accelerators are enhancements to the interface, **discovering them should not be critical****to learning and using the interface**. In fact, you shouldn’t aim to expose new users to every accelerator, as that would be overwhelming and not helpful. [New users just want to get started](https://www.nngroup.com/articles/paradox-of-the-active-user/) and complete their tasks — not read user manuals — and they should be allowed to do so. Only those users who have learned the basics and continue using the system should be exposed to the related shortcuts.

That said, we can’t know precisely when a user is “ready” to learn an accelerator. Some users may never look for these shortcuts, while others may do so immediately. For that reason, accelerators should be readily **available, yet easy to ignore**.

Incorporate the following strategies when considering the discoverability of accelerators.

### Gradually Reveal Accelerators as Users Become Accustomed to the System

Novice users are focused on completing their primary tasks and will become overwhelmed if accelerators are introduced too early. Let users explore core functionality and reveal accelerators as they become more familiar with the interface.

### Provide Contextual Hints

For less-obvious shortcuts, it’s best to introduce accelerators after a user performs the action in the standard way. Just-in-time help (also called [push revelations](https://www.nngroup.com/articles/onboarding-tutorials/)) makes it more likely that users will attend to the tip since it relates to their current task. Focus on a single action at a time using short, scannable messages.

![A messaging app with a purple banner that reads "Add a quick reaction. Tap and hold on a message to add an emoji reaction."](https://media.nngroup.com/media/editor/2024/10/07/slack.png)

Slack’s mobile app displays this tip after reacting to a message.

### Display Keyboard Shortcuts Inline

Common shortcuts should be visible and easily accessible in the interface. Style them in a way that differentiates them from the corresponding GUI-command label. For example, you might right-align shortcuts next to the corresponding action in a dropdown menu or show them in parentheses. Different styling allows expert users to quickly spot them while novice users can ignore them.

![A "Search actions" menu with various shortcut options. The first option, "Compose note," is highlighted, showing the shortcut key "N." Other options include "Use macro," "Insert gif," "Close," "Snooze," "Upload attachment," and "Insert emoji," each with corresponding keyboard shortcuts.](https://media.nngroup.com/media/editor/2024/10/07/intercom.png)

Intercom’s web app displays associated keyboard shortcuts right-aligned next to each action.

### Show Accelerators Within a Tooltip or Hover

You can also provide the accelerator in a tooltip or hover. While this approach will help users discover the accelerators without disrupting their workflow, hover actions won’t work for users who do not use a mouse (e.g., because of physical limitations or because they use a touchscreen).

![The highlighted icon displays "Add a group" with the shortcut key "G" shown.](https://media.nngroup.com/media/editor/2024/10/07/dovetail.png)

Dovetail provides a keyboard shortcut, G, next to the icon label when a user hovers over the button.

### Place Complex Accelerators in Multiple Locations

Macros and automation tools will be more discoverable if found in multiple places, such as menus, toolbars, or setup screens.

### Create Cheat Sheets for Expert Users

A last resort is to create a list of all shortcuts, accessible within the *Help* or *Support* documentation. Such a list is not very discoverable, as most users don’t seek this type of information out but can be helpful for expert users who want to see everything available to them quickly.

![A large list of keyboard shortcuts, divided into three sections: "General shortcuts," "Navigating your admin panel," and "Navigating settings." Each section has various shortcut key combinations for specific actions.](https://media.nngroup.com/media/editor/2024/10/07/shopify.png)

Shopify provides a cheat sheet of all keyboard shortcuts organized by workflow.

## Accelerator-Design Best Practices

Not all actions within a system need an accelerator. Focus on those **features** that many people tend to **use repeatedly**. Ask yourself: What are the [core actions](https://www.nngroup.com/videos/top-tasks-ux-design/) within the system? Increasing efficiency and productivity really matters only for repeat tasks; thus, these routine actions are good candidates for adding an accelerator. [Learning requires repetition](https://www.nngroup.com/articles/power-law-learning/), so people will learn a shortcut better if it is an action they repeat often.

Keep in mind that an accelerator is *not* a new feature — it is merely an additional way of completing an existing action. Those users who never discover the accelerator should be able to complete the same task in another way.

### Prioritize Efficiency Without Overwhelming Users

Accelerators should be designed for tasks that users perform frequently. For example, keyboard shortcuts for common actions — such as copy, paste, and save — improve efficiency and reduce repetition.

However, too many accelerators in an interface can overwhelm users, especially those new to an application. Start with the most used actions and introduce additional accelerators gradually as users become more familiar with the interface. Expert users may even benefit from customized accelerators to fit their specific workflows.

![GPT  A dialog box titled "Keyboard Shortcuts" with multiple options.](https://media.nngroup.com/media/editor/2024/10/07/indesign.png)

Adobe InDesign allows expert users to add and modify keyboard shortcuts based on desired workflows. This dialog is nested in the Edit menu (and thus not easily discoverable); however, that is okay since such shortcuts are likely used only by a fraction of users.

### Maintain Consistency Across Platforms

When designing cross-platform applications (web, mobile, desktop), make sure that common shortcuts and gestures are consistent across platforms. For example, a double-tap-to-react feature should work the same in a mobile app as it does on a responsive website to avoid confusing users who switch interaction channels.

![A side-by-side comparison of an Instagram post, each with a heart icon indicating the user has "liked" the post.](https://media.nngroup.com/media/editor/2024/10/07/instagram-comparison.png)

Instagram uses the same double-tap gesture both on its web app (when displayed on a touch device — left) and in its mobile app (right). Both actions animate in the same way.

Do not override commonly known shortcuts, such as those for copy, paste, select all, and print, to prevent errors and accelerate learning of the interface. You can also take advantage of platform-specific gestures, such as long press, swipe, or double tap on mobile devices.

### Provide Visual Cues and Feedback

Tooltips, hover states, or contextual hints are great ways to teach users about accelerators without overwhelming them. For example, hovering over a button can reveal its corresponding keyboard shortcut, while a tooltip can introduce touch gestures or complex commands.

Regardless of how you introduce an accelerator, always [provide feedback](https://www.nngroup.com/articles/indicators-validations-notifications/) to users that the action has been successfully completed. You can do this with an animation, highlight, or confirmation message.

![Two screenshots of an email interface. On the left, a message is highlighted in green with an archive icon. On the right, the message is archived with an "Undo" option displayed in a white bar at the bottom.](https://media.nngroup.com/media/editor/2024/10/07/gmail.png)

Gmail’s mobile app: Swiping on a message is an accelerator for archiving the message (left). After the message is archived, a snackbar confirms that the message was successfully archived and also displays an option to undo the action if it was done in error.

### Design for Error Prevention and Recovery

Provide a safety net for users to undo actions performed via accelerators on the off chance that they triggered them accidentally. A confirmation dialog not only reassures the user that their action was correct (as shown above) but also serves to prevent unintended actions that could lead to data loss or significant changes.

## Conclusion

Repeat users who are already familiar with an interface want to be efficient, whereas novice users need the interface to be as explicit as possible so they can find their way around. Accelerators help balance the needs of both types of users and enhance an interface by giving them control over completing an action. This is what makes a system highly flexible — and ultimately widely usable.
