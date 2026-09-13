---
title: "Contextual Menus: Delivering Relevant Tools for Tasks"
date: "2019-03-17"
url: "https://www.nngroup.com/articles/contextual-menus/"
author: "Anna Kaley"
topics: [applications]
type: article
---

In any given application, there’s an abundance of tools to use, tasks to complete, menu options to explore, and commands to execute. As such, an important user-interface element that **narrows** the set of available commands and **associates** them to relevant tasks is the contextual menu.

## In This Article:

- [What Is a Contextual Menu?](#toc-what-is-a-contextual-menu-1)
- [Triggers for Revealing Contextual Menus](#toc-triggers-for-revealing-contextual-menus-2)
- [Tips for Effective Contextual Menus](#toc-tips-for-effective-contextual-menus-3)
- [Conclusion](#toc-conclusion-4)

## What Is a Contextual Menu?

Definition: A **contextual menu** is a type of menu that appears on demand and contains a small set of relevant actions related to a control, an area of the interface, a piece of data in the application, or a view of the application. Usually, this context is given by the current selection or has otherwise been specified by the user before invoking the contextual menu.

![Context Menu for Text in Word](https://media.nngroup.com/media/editor/2019/02/14/contextmenu_word_text.jpg)

*In Microsoft Word, highlighting a passage of text, holding down the* Control *key, and clicking the mouse revealed a contextual menu that contained only commands related to the selected piece of data.*

![Contextual Menu in Word from lower status bar](https://media.nngroup.com/media/editor/2019/02/14/contextmenu_word_statusbar.jpg)

*Right-clicking the status bar in Microsoft Word revealed a contextual menu with commands that pertained to the entire document. The contextual menu also contained commands to toggle the view of specific elements to show or hide in the status bar.*

Offering a small subset of relevant actions in contextual menus helps users **find exactly what they need for the task at hand.** This menu type also reduces [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/)and [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/) as users don’t have to parse through long lists of main-menu items to find what they need, nor do they have to continually return to the toolbar every time they wish to use certain commands.

Contextual menus exist across all operating systems, in both desktop and [mobile applications](https://www.nngroup.com/articles/mobile-native-apps/). However, there are important usability considerations to keep in mind for each device type and system. In this article, we’ll introduce several examples of contextual menus and discuss the interaction and visual factors to keep in mind when designing them.

## Triggers for Revealing Contextual Menus

Contextual menus usually aren’t triggered by a consistent UI element, gesture, or interaction. They appear next to where the user clicks, taps, presses, or swipes, and the resulting actions vary based on the tap target. **Options presented to users in contextual menus should be the same, regardless of how users interact with the system to reveal these menus.**

On **desktop**, the main interactions that reveal contextual menus include:

- Right-clicking on a two-button mouse
- Pressing the *Control**(Ctrl)* button and then clicking
- Two-finger click on a trackpad

On **mobile**, the main interactions that reveal contextual menus include:

- Tapping an icon or visual element
- [Horizontal swipe](https://www.nngroup.com/articles/contextual-swipe/)
- Long press (tap and hold)
- [3D Touch](https://www.nngroup.com/articles/3d-touch/) (iOS)

## Tips for Effective Contextual Menus

To determine if you need a contextual menu in your application, **ask yourself if you can identify a small set of options or tools that are related to a particular task, selected element, or app screen**. In addition to answering that basic question, here are a few more tips for designing effective contextual menus:

- **Only include a focused set of actions and common options related to the task at hand.** Items inside of contextual menus should directly relate to the tasks the user needs to complete or the element in the interface that’s selected or clicked.

![Contextual Menu in One Note](https://media.nngroup.com/media/editor/2019/02/14/contextual-menu-in-one-note.jpg)

*A contextual menu for a selected note in OneNote included commands that were relevant to editing the contents of the note. Actions such as* Paste *and* Insert Link *made sense to include here, but global actions such as* Save *or* Print *did not make sense to include as those commands are related to the entire Notebook, rather than the selected note.*

- **Make sure the commands in contextual menus are also available from the application’s main menu.** Like [keyboard shortcuts](https://www.nngroup.com/articles/ui-copy), contextual menus give users another way to execute actions and select options. Because the default view of a contextual menu is usually hidden, users may not know it is available, or how to access it. There should always be an additional way to find and use the actions found in contextual menus in main navigation menus.

![Photoshop Contextual Menu in Layers](https://media.nngroup.com/media/editor/2019/02/14/photoshop-layers-contextual-menu.png)

*In Photoshop, consistent contextual actions for manipulating layers were available by either right-clicking on the layer in the* Layers *panel (top) or by selecting the layer, and clicking on the* Layer *label in the main navigation (bottom). This design gave users convenient options for accessing the commands.*

- **Include visual elements in the UI to indicate that a contextual menu is available.** Advanced users may understand that right-clicking, control-clicking, swiping, or long-pressing will reveal a contextual menu, but not all users will know this. Common visual signifiers for contextual menus include vertical or horizontal ellipsis and down-pointing arrows.

![Google Photos contextual menu](https://media.nngroup.com/media/editor/2019/02/14/google-photos-contextual-menu.png)

*A horizontal-ellipsis button in Google Photos helped users access relevant commands related to their photo album.*

![Windows Contextual Menu](https://media.nngroup.com/media/editor/2019/02/14/windows-contextual-menu.jpg)

*Down-pointing arrow buttons on Windows helped users access a contextual menu of commands related to their profile and profile picture.*

- **For hidden contextual menus, (1) include tips to create awareness and (2) allow users to perform the same actions another way.** For example, on mobile, often contextual menus will be accessed through special gestures such as 3D touch or swipe. Though [mobile gestures](https://www.nngroup.com/articles/iphone-x/) are becoming more and more familiar to users, these gestures are not discoverable and have still not become standard. Make sure to include other ways to perform the actions, that don’t rely on gestures. For example, swipe is not always discoverable for contextual actions, so provide assistive clues to help users find your menus. Even if your app uses an initial tip to disclose gestures such as swipe-triggered actions, it is unlikely that people will naturally remember to use it later on in the app. Thus, the contextual actions may be never discovered.

![Gmail contextual menu](https://media.nngroup.com/media/editor/2019/02/14/gmailcontextualmenu.png)

*Swipe gestures are not deployed consistently in all lists, so people don’t always think to use them and as a result, the gestures become less discoverable. Swipe actions are accelerators intended to speed up interactions for power users, but the actions available through the gesture should also be present in the visible UI. For example, the iOS Mail app offered redundant commands in a contextual menu bar at the bottom an email message; these commands were also available by swiping an email in the list view and clicking the* More *option.*

- **Contextual menus should not be triggered by icons that could be mistaken for main navigation or app Settings .** Avoid using gear icons or [hamburger-menu](https://www.nngroup.com/articles/hamburger-menus/) icons to represent contextual menus. Users have come to recognize these as elements that trigger global menus and settings, rather than narrower, task-focused [commands](https://www.nngroup.com/articles/overloaded-vs-generic-commands/).

![Quip contextual menu using a settings icon.](https://media.nngroup.com/media/editor/2019/02/14/quip-contextual-menu.png)

*Quip used a gear icon to trigger a contextual menu; this gear icon could have been mistaken for a global* Settings *menu for the broader app, rather than a contextual menu related to the document.*

- **Limit the use of submenus within contextual menus.** Submenus triggered from contextual menus can easily disappear if the cursor moves away from the primary list item or if the user accidentally clicks outside of the contextual menu. If a submenu is needed, make sure that none of its options open yet another level of submenus and don’t overload it with obscure commands to the point that it becomes cluttered, confusing, and difficult to use.

![Google Sheets contextual menu with many duplicate commands.](https://media.nngroup.com/media/editor/2019/02/14/google-sheets-contextual-menu.jpg)

*In Google Sheets, a submenu appeared when users hovered over the* Paste Special *command in a contextual menu. Though the submenu contained only one additional layer of options, it displayed many similarly worded commands that were hard to decipher or scan.*

![Apple's 3D touch revealed a contextual menu from the Safari application.](https://media.nngroup.com/media/editor/2019/02/14/3d-touch-iphone.png)

*Apple’s 3D Touch feature allowed users to press and hold an application’s icon, revealing a single-level contextual menu with the most common actions associated with the app. This menu helped users quickly access simple tools and commands without having to launch the app and then subsequently, find those commands.*

- **List commands in in frequency-of-use order.** Don’t make users scan through a long list of disorganized commands. To help users focus on the most relevant options, place the ones used most often at the top. Because people scan lists from top to bottom, place seldomly used commands low down in the menu. Let users decide which option best meets their needs and, if none of the available options fits, no resulting action should take place when the menu is closed.

![YouTube contextual menu with commands in frequency of use order.](https://media.nngroup.com/media/editor/2019/02/14/youtube-contextual-menu.png)

*YouTube’s contextual menu for a recommended video appeared after a long press; the same menu also appeared if the user clicked the action-overflow icons. The menu options were presented in order of importance and, if users decided to take no action, they were able to easily* Cancel *the task, thus hiding the contextual menu without any change to their view.*

- **Show keyboard shortcuts in contextual menus.** To help users save time and learn keyboard shortcuts, include them in contextual menus. Seeing these shortcuts repeatedly will help users memorize task-specific commands and become efficient.

![PowerPoint menu for text](https://media.nngroup.com/media/editor/2019/02/14/powerpoint-contextual-menu.png)

*PowerPoint included keyboard shortcuts in its contextual menus; these shortcuts helped users to learn time-saving alternatives for navigating and accomplishing tasks.*

- **Limit the number of items within a contextual menu.** Don’t overwhelm users with expansive lists of options in contextual menus. Keep the list length manageable by including fewer than 10–12 items, to avoid [choice overload](https://www.nngroup.com/articles/simplicity-vs-choice/) and ensure that all of the contextual options are visible, without having to scroll.

![Zillow contextual menu with an appropriate amount of list items.](https://media.nngroup.com/media/editor/2019/02/14/zillow-owner-view.png)

*Zillow’s mobile app offered a contextual menu on the screen that showed statistics about a real estate listing. The menu had 9 items that all were related to the screen’s context. The length of the menu made it easy to understand the available options and select one without having to scroll.*

- **Disable items that aren’t relevant to the user’s context.** Rather than hiding irrelevant actions, disable them so that users won’t have to try to find where menu items disappeared, nor will they have to determine how to get the system back in the proper context to reveal a specific command. Also, make sure that you include all options (instead of just one) in a family of related commands. For example, if there is a *Back*, there should also be a *Forward*. If there's a *Cut*, there should also be *Copy* and *Paste*.

![Evernote contextual menu](https://media.nngroup.com/media/editor/2019/02/14/evernote-context-menu.png)

*A contextual menu in Evernote allowed users to customize the elements that showed up in the sidebar of the application. Because* All Notes *couldn’t be removed from the sidebar, this option was displayed as disabled. Had it been removed from the menu, users may have wondered why or where to find it in order to hide or show it.*

## Conclusion

Though there are many ways to trigger and present contextual menus, at their core, these UI elements aim to provide users with the most important commands and relevant tools they need to complete tasks easily within their given context. For more on designing effective contextual menus, take our full-day courses, [Application Design for Web and Desktop](https://www.nngroup.com/courses/application-ux/) and [Mobile User Experience](https://www.nngroup.com/courses/usability-mobile-websites-apps/).
