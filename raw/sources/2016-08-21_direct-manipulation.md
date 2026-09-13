---
title: "Direct Manipulation: Definition"
date: "2016-08-21"
url: "https://www.nngroup.com/articles/direct-manipulation/"
author: "Raluca Budiu, Samyukta Sherugar"
topics: [applications, human-computer-interaction]
type: article
---

## In This Article:

- [Introduction](#toc-introduction-1)
- [The Characteristics of Direct Manipulation](#toc-the-characteristics-of-direct-manipulation-2)
- [Direct Manipulation vs. Skeuomorphism](#toc-direct-manipulation-vs-skeuomorphism-3)
- [Disadvantages of Direct Manipulation](#toc-disadvantages-of-direct-manipulation-4)
- [Conclusion](#toc-conclusion-5)
- [References](#toc-references-6)

## Introduction

Let’s say that you’re looking at an image of a concert you went to and want to see the performer on stage more clearly. What do you do? Something like this?

![A photo of the zooming gesture over a mobile screen that is displaying an image of a concert](https://media.nngroup.com/media/editor/2024/10/12/zoom.jpg)

*On a mobile phone, you can pinch out to zoom into an image and pinch in to zoom out.*

The action of using your fingertips to zoom in and out of the image is an example of a **direct-manipulation****interaction**. Another classic example is dragging a file from one folder to another in order to move it.

![A screenshot of moving a document from one folder to another.](https://media.nngroup.com/media/editor/2016/08/19/2016-08-18_dm-move3.png)

*Moving a file on MacOS using direct manipulation involves dragging that file from the source folder and moving it into the destination folder.*

> **Direct manipulation (DM)** is an interaction style in which users act on displayed objects of interest using physical, incremental, and reversible actions whose effects are immediately visible on the screen.

Ben Shneiderman first coined the term “direct manipulation” in the early 1980s, at a time when the dominant interaction style was the command line. In **command-line interfaces,** the user must remember the system label for a desired action and type it in together with the names of the objects of the action.

![A screenshot of the the Mac terminal displaying command lines to move a file to a different folder.](https://media.nngroup.com/media/editor/2016/08/19/2016-08-18_dm-correct-command-2.png)

*Moving a file in a command-line interface involves remembering the name of the command (“mv” in this case), the names of the source and destination folders, as well as the name of the file to be moved.*

Direct manipulation is one of the central concepts of graphical user interfaces (GUIs) and is sometimes equated with “what you see is what you get” (WYSIWYG). These interfaces **combine menu-based interaction with physical actions** such as [dragging and dropping](https://www.nngroup.com/articles/drag-drop/) in order to help the user use the interface with [minimal learning](https://www.nngroup.com/articles/power-law-learning/).

## The Characteristics of Direct Manipulation

In his analysis of direct manipulation, Shneiderman identified several attributes of this interaction style that make it superior to command-line interfaces:

### Continuous Representation of the Object of Interest

In direct-manipulation interactions, users can see visual representations of the objects that they can interact with. As soon as they perform an action, they can see its effects on the state of the system.

For example, when moving a file using drag-and-drop, users can see the initial file displayed in the source folder, select it, and, as soon as the action is completed, they can see it disappear from the source and appear in the destination — an immediate confirmation that their action had the intended result.

Thus, direct-manipulation UIs satisfy, by definition, the first [usability heuristic](https://www.nngroup.com/articles/ten-usability-heuristics/): the [visibility of the system status](https://www.nngroup.com/articles/visibility-system-status/). In contrast, in a command-line interface, users usually must explicitly check that their actions had the intended result (for example, by listing the content of the destination directory).

### Physical Actions Instead of Complex Syntax

Actions are invoked physically via clicks, button presses, menu selections, and touch gestures. In the move-file example, drag-and-drop has a direct analog in the real world, so this implementation for the move action has the right signifiers and can be easily learned and remembered.

In contrast, the command-line interface requires users to recall not only the command name (“mv”) but also the names of the objects involved (files and paths to the source and destination folders). Thus, unlike DM interfaces, command-line interfaces are based on [recall instead of recognition](https://www.nngroup.com/articles/recognition-and-recall/) and violate an important usability heuristic.

### Continuous Feedback and Reversible, Incremental Actions

Because of the visibility of the system state, it’s easy to check whether each action produced the right result. Thus, when users [make mistakes](https://www.nngroup.com/articles/slips/), they can see right away the cause of the mistake and they should be able to easily undo it.

In contrast, with command-line interfaces, one single user command may have multiple components that can cause the error. For instance, in the example below, the name of the destination folder contains a typo *Measuring Usablty* instead of *Measuring Usability*. The system simply assumed that the file name should be changed to *Measuring Usablty*. If users check the destination folder, they will discover that there was a problem but will have no way of knowing what caused it: did they use the wrong command, the wrong source filename, or the wrong destination?

![A typo is shown in the command line: the word "Usability" is missing an i.](https://media.nngroup.com/media/editor/2016/08/19/2016-08-18_wrong-command.png)

*The command contains a typo in the destination name. Users have no way of identifying this error and must do detective work to understand what went wrong.*

This type of problem is familiar to everyone who has written a computer program. Finding a bug when there are a variety of potential causes often takes more time than actually producing the code.

### Rapid Learning

Because the objects of interest and the potential actions in the system are visually represented, users can use recognition instead of recall to see what they could do and select an operation most likely to fulfill their goal. They don’t have to learn and remember complex syntax. Thus, although direct-manipulation interfaces may require some initial adjustment, the learning required is likely to be less substantial.

## Direct Manipulation vs. Skeuomorphism

When direct manipulation first appeared, it was based on the office-desk metaphor — the computer screen was an office desk, and different documents (or files) were placed in folders, moved around, or thrown in the trash. This underlying metaphor indicates the skeuomorphic origin of the concept. The DM systems described originally by Shneiderman are also **skeuomorphic — that is, they are based on resemblance with a physical object in the real world**. Thus, he talks about software interfaces that copy Rolodexes and physical checkbooks to support tasks done (at the time) with these tools.

As we all know, skeuomorphism saw a huge revival in the early iPhone days and has now come out of fashion.

![A screenshot of the piano interface that mimics the look of real piano keyboards](https://media.nngroup.com/media/editor/2024/10/12/img_6e344302760a-1.jpg)

*GarageBand: A skeuomorphic direct-manipulation interface for “playing” the piano on a phone.t-manipulation interface for “playing” the piano on a phone*

While skeuomorphic interfaces are indeed based on direct manipulation, not all direct-manipulation interfaces need to be skeuomorphic. In fact, [flat interfaces](https://www.nngroup.com/articles/flat-design/) are a reaction to skeuomorphism and depart from real-world metaphors, yet they still rely on direct manipulation.

## Disadvantages of Direct Manipulation

Almost each DM characteristic has a directly corresponding disadvantage:

- *Continuous representation of the objects?* It means that you can **act only on the small number of objects that can be seen at any given time**. Objects that are out of sight but not out of mind can be dealt with only after the user has laboriously navigated to the place that holds those objects so that they can be made visible.
- *Physical actions?* They can lead to **RSI (repetitive strain injury)**. It’s a [lot of work](https://www.nngroup.com/articles/interaction-cost-definition/) to move all those icons and [sliders](https://www.nngroup.com/articles/gui-slider-controls/) around the screen. Another potential issue is, **accidental activation**(hitting the wrong target), which is particularly common on touchscreens but can also happen on mouse-driven systems.
- *Continuous feedback?***Only if you attempt an operation that the system feels like letting you do.** If you want to do something that’s not available, you can push and drag buttons and icons as much as you want with no effect whatsoever. No feedback, only frustration. (A good UI will show [in-context help](https://www.nngroup.com/articles/onboarding-tutorials/) to explain why the desired action isn’t available and how to enable it. Sadly, UIs this good are not very common.)
- *Rapid learning?* Yes, if the design is good, but in practice, **learnability depends on how well-designed the interface is**. We’ve all seen [menus with poorly chosen labels](https://www.nngroup.com/articles/category-names-suck/), buttons that did not look clickable, or [dropdown boxes](https://www.nngroup.com/articles/drop-down-menus/) with more options than the length of the screen.

And there are even more disadvantages:

### DM Is Slow

If the user needs to perform many actions on many objects, using direct manipulation takes a lot longer than a command-line UI. Have you encountered any software engineers who use DM to write their code? Sure, they might use DM elements in their software-development interfaces, but most of the code will be typed in.

### Repetitive Tasks Are Not Well Supported

DM interfaces are great for novices because they are easy to learn, but because they are slow, experts who perform the same set of tasks with high-frequency usually rely on keyboard shortcuts, macros, and other command-language interactions to speed up the process. For example, when you need to send an email attachment to one recipient, it is easy to drag the desired file and drop it into the attachment section. However, if you need to do this for 50 different recipients with customized subject lines, a macro or script will be faster and less tedious.

![A screenshot of Figma keyboard shortcuts.](https://media.nngroup.com/media/editor/2024/10/12/screenshot-2024-09-14-at-35435-pm.jpg)

*Figma: Keyboard shortcuts allowed users to speed up their workflow by quickly accessing frequently used tools.*

### Some Gestures Can Be More Error-Prone or Take More Effort than Typing

In theory, because of the continuous feedback, [DM minimizes the chance of certain errors](https://www.nngroup.com/articles/direct-manipulation-analysis/); in practice, there are situations when a gesture is harder to perform than typing equivalent information. For example, good luck trying to move the 50th column of a spreadsheet into the 2nd position using drag and drop.

For this exact reason, YouTube offered two interaction techniques for reordering videos in a playlist: dragging the video to the desired position (easy for short moves), and a one-button shortcut for moving into the first or last position. However, with 113 videos in this playlist, the design would have been more efficient if it had included a *Move to...* option, allowing users to specify the exact position number.

![A screenshot of a YouTube Playlist with a selection menu that allows users to move each video to the top or bottom of the list](https://media.nngroup.com/media/editor/2024/10/12/screenshot-2024-09-14-at-44258-pm.jpg)

*YouTube: Users could rearrange the playlist by dragging a video to the desired position or clicking a button to move a video to the top or bottom of the list.*

![A screenshot of Bumble's Edit Profile page with a modal dialog for adjusting height using a slider control](https://media.nngroup.com/media/editor/2024/10/12/bumble-web-166.jpg)

*Bumble: Users had to use a slider to input their precise height, which required high interaction cost. This interaction would have been better if users could simply type in their height.*

### Accessibility May Suffer

DM UIs may fail visually impaired users or users with motor skill impairments, especially if they are heavily based on physical actions, as opposed to button presses and menu selections. (Workarounds exist, but it can be difficult to implement them.)

## Conclusion

It’s hard to imagine modern interfaces without direct manipulation. Almost any interface that is aimed at a broad audience and has a graphical component is based on DM. With the explosion of touchscreen devices, we’ve seen DM UIs depart from the original office metaphors and innovate in a variety of domains. And [augmented-reality](https://www.nngroup.com/articles/augmented-reality-ux/) and virtual-reality systems will push DM to even newer limits.

Despite the many downsides, we still recommend a heavy dose of direct manipulation for most UIs. Direct manipulation often enhances users’ sense of empowerment over the computer by [letting them feel that they are in control](https://www.nngroup.com/articles/user-control-and-freedom/) and are the ones making things happen. The upsides of DM usually enhance usability more than the downsides degrade it. Any interaction style has its minuses and can be ruined by a lack of attention to the details: there is no magic bullet for UX, but there are definitely design ideas that can advance usability if employed correctly, and direct manipulation has proven to be one of these good ideas for more than 30 years.

## References

Shneiderman, B. 1983. *Direct Manipulation: A Step Beyond Programming Languages*. Computer 16 ****(8), pp. 57–69. ([Access-controlled archival copy](http://dl.acm.org/citation.cfm?id=1320072) available in ACM Digital Library.)
