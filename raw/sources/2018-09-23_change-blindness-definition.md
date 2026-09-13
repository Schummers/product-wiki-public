---
title: "Change Blindness in UX: Definition"
date: "2018-09-23"
url: "https://www.nngroup.com/articles/change-blindness-definition/"
author: "Raluca Budiu"
topics: [psychology-and-ux]
type: article
---

In usability testing, we often observe users who overlook a change on the screen that the designers thought would be obvious and highly noticeable. As always in usability, if you worked on a design, then you know *what* to look for, *where* to look for it, *when* it will appear, and what it *means*. So yes, it’s *obvious to you* and you wouldn’t miss the appearance of an important message or data object when you review your own design. But users often do. Why? Because of change blindness, which is a million-year old fact of human (and protohuman) perception, and not likely to go away any time soon.

So what is change blindness? In Alfred Hitchcock’s *Psycho*, one of the most famous movies of all time, detective Arbogast looks at Norman Bates’ house projected on a dark cloudless sky. The camera moves back to the detective’s face, and follows him as he starts walking toward the house. The scene is still dark, but the sky has suddenly become full of clouds.

Whether the change in the sky’s texture was intentional (perhaps Hitchock’s subtle warning for what was to come) or a continuity error, chances are that most viewers won’t notice it. Motion pictures often have small inconsistencies like this from one scene to the next — changes in the background, in the actors clothing, makeup, or positions, but these get ignored when they are made during cuts between scenes.

This phenomenon is called change blindness and goes beyond movies — it applies to how people perceive scenes in general, whether projected on a screen or in real life. Change blindness is very robust: even when people are warned that a change may happen, changes in a scene can go undetected.

**Definition**: **Change blindness** refers to people’s tendency to ignore changes in a scene when they occur in a region that is far away from their focus of attention.

In psychology, change blindness is perhaps best illustrated by a series of experiments performed in mid 1990s. In these experiments, participants were shown a picture of a complex scene for about half a second; then the display went blank for a fraction of a second, and finally the same picture was shown again. However, the second time the scene was shown, some detail was modified — for example, an object changed size, color, or an element was added or removed. Participants in the experiment were supposed to identify the changes in the two images. In some of these studies, people cycled through the two versions many times, until they were able to detect the change. For many it took 20 or 40 alternations to be able to find it.

The flickering quality of the display (one scene, followed by a blank screen, followed by what seems to be the same scene) is an essential component of change blindness. In movies, the scene cut plays the role of a flicker; and, in interacting with a computer, the flicker is caused by the loading of a new page (or UI element) once the user has pressed a button. But it turns out that the flicker doesn’t have to be literal — scene modifications that happen when the user is blinking or during a saccade (when she’s moving her eyes to another region of the screen) are also highly susceptible to change blindness.

Magicians take advantage of humans’ propensity to change blindness as their eyes move: they use an attention-attracting device to cause eye movements to that spot, and, at the same time, engage in unobserved actions that are essential to their tricks.

## In This Article:

- [Why Does Change Blindness Happen?](#toc-why-does-change-blindness-happen-1)
- [Change Blindness in Interface Design](#toc-change-blindness-in-interface-design-2)
- [How to Prevent Change Blindness in Interface Design](#toc-how-to-prevent-change-blindness-in-interface-design-3)
- [References](#toc-references-4)

## Why Does Change Blindness Happen?

The fundamental reason for which change blindness occurs is a limitation in our attention capacities. Any complex scene has a multitude of details, and it’s hard and inefficient for people to attend to all of them. What we normally do is take shortcuts.

Change is and has always been important for humans — it can convey essential information about our environment. Most changes in nature are mediated by movement (with few exceptions such as chameleons, a physical object can’t change instantly with no movement being involved), and movement is easily detected by human peripheral vision. Once the human eyes detect movement in the periphery, they look at the source of movement — central vision kicks in and provides supplemental, detailed information. This behavior is a remnant of our life in the wild, where any move could signal a predator waiting to hunt us.

**Change blindness occurs when movement as a cue for change is weak or completely absent**. When the screen flickers, the movement is shunted out — we see two static versions of the scene. The only way to find out what changed is by inspecting all the corresponding elements in the before and after versions and comparing them. This task is very difficult — not only is it tedious to inspect the myriad of little details in the scene, but our [memory](https://www.nngroup.com/articles/short-term-memory-and-web-usability/) of the prior version of the scene is likely to be quite poor. In fact, chances are that we paid no attention to many of the elements of that scene anyhow.

But change blindness also happens during an eye movement. In other words, if two (possibly movement-cued changes) compete with each other — like in the magic show, one change usually wins and attracts the eye, but that eye movement blocks the detection of the second change. This cause is particularly important in interface design.

## Change Blindness in Interface Design

In normal interactions with a UI, change blindness often occurs when a new element (such as a different image in a product-image [carousel](https://www.nngroup.com/articles/designing-effective-carousels/), or the contents of a [dropdown](https://www.nngroup.com/articles/drop-down-menus/) menu) appears on the screen as a result of user action and other areas of the screen also change. The locus of the change is expected to be the visible design element that responds directly to the user action and the user moves the eyes in that direction — yet in fact, the change is spread across multiple regions of the screen.

For example, when users tap on the [hamburger menu](https://www.nngroup.com/articles/hamburger-menus/) in Aldiko’s Android app, they expect that the changes on the screen be related to that action — namely, that the new elements will be localized in the area enclosing the menu contents. Their eyes will stay around that area and they will be unlikely to notice that the action-overflow button in the top right corner of the screen has been replaced with a search icon.

*Aldiko for Android: When the menu is opened, the controls in the right top corner of the screen get replaced by a magnifier glass. The search tool will remain unnoticed because (1) people will look at the expanded menu, which will be a direct result of their action; (2) they will expect the other elements of the screen to remain unchanged (as they normally do in interactions with most UIs).*

Elsewhere, we discussed how the search box should not be replaced by a search icon on the desktop; on a mobile screen, however, the pattern is more usable than on the desktop, as our research shows that the magnifier tool is fairly discoverable even when the search box is absent. However, if the search box is not visible by default, when users click on the search icon, the text field should appear next to it (rather than farther apart on the screen) to ensure that people will not miss it.

*Not only did Texas A & M University replace the search field with a search icon, but it also displayed the search text box far away from the search icon. The animation of the hero image was competing with the display of the search box.**John Hopkins University also used an animated hero and hid search under an icon. But at least it displayed the search box close to the search icon and dimmed the moving background, to reduce some of the competing animation.*

Semipersistent navigation bars or floating buttons that appear towards the top of the page are also in danger of staying undetected, because often the scrolling of the page masks them. For example, semipersistent navigation bars appear at the top of the screen when the user stars scrolling up. The hope is that people will notice these bars and select one of the options inside them instead of swiping their way up to the very top of the page. Unfortunately, the movement of the page can easily block the movement caused by the apparition of the bar, especially when the color of the bar blends in with the color of the page, like in the New York Times example below.

*NYTimes for iPhone: As they start scrolling up, people may miss the semipersistent navigation bar that appears at the top of the screen because they are focused on the scrolling of the page. An aggravating factor is the fact that the visuals of the navigation bar are not distinctive enough from the page content.**Chicago Tribune’s mobile site also uses a semipersistent navigation bar that appears at the top of the page when people start scrolling up. However, in this case, the visual design of the bar makes it more salient.*

(Our peripheral vision is responsible for picking out movement and also shadows. When the “shadow” profile of a page changes, for example because a big block of contrasting color has appeared in one corner, it is easier for us to detect its appearance than when the same block subtly blends in with the rest of the page and does not significantly alter the shadow profile of the page.)

There are many other design aspects that can be affected by change blindness — error messages or other notifications, results that [appear too quickly](https://www.nngroup.com/articles/too-fast-ux/), or changing navigation bars may also remain ignored due to this phenomenon, as discussed on our [companion article on the same topic](https://www.nngroup.com/articles/change-blindness/).

## How to Prevent Change Blindness in Interface Design

To avoid change blindness, analyze your design for any competing changes that may happen at the same time and that may divert attention from each other. Here are some techniques for doing it:

- **Make****one change at a time**. In the Aldiko example above, search could be placed in the top right corner and be visible always.
- **Group all elements that will change** simultaneously in the same region of the screen, to make sure that the motion will draw attention to all of them. For example, another easy fix for the Aldiko design is to move search inside the menu. (Note however that hiding search under a menu will seriously impact its discoverability and may only be acceptable on browse-heavy sites.)
- **Use animation to signal change**, but avoid having too many competing animations on the screen to prevent a dilution of attention.
- **Dim the areas of the screen** that do not change, in order to attract attention to changes.
- **If you are adding floating elements** to the page as the user scrolls, [display them next to the user’s focus of attention](https://www.nngroup.com/articles/closeness-of-actions-and-objects-gui/) (for instance, towards the bottom of the page for *Back to Top buttons*) and use colors that contrast with the rest of the page.

## References

Ronald Resnick. 2002. Change Detection. *Annual Review of Psychology*, 53, p/245-277.

Ronald Rensnick. 2005. Change Blindness. In In *McGraw-Hill Yearbook of Science & Technology*. pp. 44-46.
