---
title: "Split Buttons: Definition"
date: "2019-05-12"
url: "https://www.nngroup.com/articles/split-buttons/"
author: "Page Laubheimer"
topics: [interaction-design]
type: article
---

In complex applications, it is easy to overwhelm users with a tremendous number of options, commands, tools, and controls. Showing a large number of tools all at once is visually overwhelming, and evaluating all the available actions places far too much [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/) on users. Split buttons reduce visual complexity by grouping similar commands together — much like how navigation menus chunk together related options to enable conceptual understanding of the site information structure.

**Definition**: A split button is a button with two components: a label and an arrow; clicking on the label selects a default action, and clicking on the arrow opens up a list of other possible actions.

A split button is a hybrid between a button and a menu: it groups related commands together into a [dropdown](https://www.nngroup.com/articles/drop-down-menus/), but also offers one-click access to a default choice that doesn’t require opening the menu.

![A menu button on the left with the word Paragraph that has no default choice.  A split button with the word Insert on the right that has a default choice.  Both menus are open.](https://media.nngroup.com/media/editor/2019/04/25/menu-and-split-buttons.png)

*Left : The* Paragraph *button is a regular menu button. Clicking anywhere on the button opens the menu, and there is no default choice made by clicking* Paragraph *. Right : The* Insert *button is a split button. Clicking* Insert *itself performs the default action of inserting text but does not open the menu, whereas clicking the arrow part of the button opens a menu, providing several related commands.*

Split buttons are for presenting several related tools if one option is used most frequently. Making the most commonly accessed option a [default](https://www.nngroup.com/articles/the-power-of-defaults/) lowers the [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) to use that option since it removes the need to open the menu before selecting the item. The obvious penalty is that accessing the menu becomes harder because it requires hitting a small target (which takes [more time according to Fitts’s Law](https://www.nngroup.com/videos/fittss-law/)) and also involves an extra mental operation to decide which part of the button to activate.

Unlike [contextual menus](https://www.nngroup.com/articles/contextual-menus/), split buttons are typically placed in a main toolbar, and the commands found within their associated menu are not limited to options related to items the user has already selected before triggering the menu.

While a split button may seem like an obvious design pattern, options within the menu can have low [discoverability](https://www.nngroup.com/articles/navigation-ia-tests/). Users (especially those learning an application) don’t always recognize this pattern, so they may not notice the secondary menu button and, consequently, the options located within the menu. Therefore, the first thing to consider when deciding whether to use split buttons is whether there is a strong choice for the default option; if users only notice the default option, will that serve the majority of situations? If not, a traditional menu button (without a default option) may assist users better by promoting discovery, especially in an application that doesn’t see a lot of repeat usage.

In desktop applications, menu buttons are used for commands and tools rather than for navigation. Thus, the second aspect to consider when using a split button is whether that button will be hosting commands versus navigation categories (in fact, we recommend that you [don’t use split buttons for website navigation](https://www.nngroup.com/articles/split-buttons-navigation/)): if the result of clicking the button is an *action* or *selecting a tool* then a split button is appropriate, whereas if the button takes a user to *another page**or screen*, a [standard dropdown menu](https://www.nngroup.com/articles/drop-down-menus/) is a better choice than a split button.

## In This Article:

- [Visually Separate Arrow Button](#toc-visually-separate-arrow-button-1)
- [Use Text Labels for Split Buttons](#toc-use-text-labels-for-split-buttons-2)
- [Other Tips for Effective Split Buttons](#toc-other-tips-for-effective-split-buttons-3)
- [Persistent Split Buttons](#toc-persistent-split-buttons-4)
- [Summary](#toc-summary-5)

## Visually Separate Arrow Button

Good visual design is essential for a split button to be recognized: **the arrow that signals the menu aspect of the button must be clearly separated from the label of the button**.

A poorly designed split-button can look like a standard menu button (which always opens the menu). Strong visual [signifiers](https://jnd.org/signifiers_not_affordances/)for split buttons include a dividing line within the button or a slightly different color for the region around the arrow. The visual separation between the default action and the arrow should be always visible, and not simply a hover effect — when the visual separation between is hidden until hover, users will not properly recognize a split button.

![A split button that has no clear visual separation between the arrow and the default button parts.](https://media.nngroup.com/media/editor/2019/04/25/hidden-signifier.png)

*Menu button or split button? The arrow button is not visually separated from the default* Paste *action (left) until the user hovers over that region of the button (right). This hidden signifier is not as effective as one that is always shown.*

The target size of the arrow component of the split button is a major limiting factor on its usability. If the size of the arrow button is very small (as it often happens), that button will be harder to acquire (according to Fitts’s Law). As a result, we do not recommend split buttons for touchscreen applications (because of the [fat-finger problem](https://www.nngroup.com/articles/mouse-vs-fingers-input-device/)), unless it is possible to make tap target sizes for *both* parts of the button at least [1cm × 1cm](https://www.nngroup.com/touch-targets).

Adobe Photoshop, for example, attempts to circumvent this sizing issue and places the arrow ambiguously within the bottom right corner of each split button, allowing (and requiring) a click-and-hold gesture *anywhere* on the button to open the menu. This solution is not recommended, as there is no visual signifier for that unique affordance; we have observed that even veteran users of Photoshop do not realize that they can click and hold anywhere on the button to access its menu component; instead, they would attempt to position their mouse cursor over the tiny arrow icon. And some of those who painstakingly succeed are disappointed to discover that the menu does not open on click (requiring instead a click and hold).

![Photoshop's use of split buttons that has a very small arrow in the bottom right corner of the button](https://media.nngroup.com/media/editor/2019/04/25/photoshop-ambiguous-split-button.png)

*Photoshop uses split buttons for the main toolbar, but does not clearly signify that the menu should be opened by clicking and holding anywhere on the visible target area. This design causes learnability problems for new Photoshop users, who often attempt to hone their mouse cursor over the tiny arrow icon and click to open the menu.*

## Use Text Labels for Split Buttons

Some split buttons have both an icon and text in the label component. While icons are optional, [a text label is always necessary](https://www.nngroup.com/videos/icon-text-labels/). Text improves learnability, discoverability, and findability, and increases the target size of the button, thus providing a Fitts’s Law benefit. The default choice in a split button should always include a text label, and so should the alternate options inside the menu.

Unlike regular menu buttons, in which the text label should clearly describe a generic *category* comprising all that is contained in the menu, a split button’s visible text label should be a [descriptive name of the default tool or command](https://www.nngroup.com/articles/ui-copy/).

![Row height button with a categorical label, because it is a menu button.  The reply button, on the right, is a split button, and the text label is a verb.](https://media.nngroup.com/media/editor/2019/04/25/splitbuttoncategory.png)

*Left : The* Row Height *button is a regular menu button, and the text label is a category description for the options in the menu. Right : The* Reply *button is a split button, and the text label is the name of the default action, rather than a description of the entire category.*

## Other Tips for Effective Split Buttons

While many of these recommendations carry over from other types of menus such as [contextual menus](https://www.nngroup.com/articles/contextual-menus/) and [menu bars](https://www.nngroup.com/articles/menu-design/), abiding by these rules ensures that split buttons work well:

- **Limit the overall number of choices** within the menu to less than 10–12, to avoid [choice paralysis](https://www.nngroup.com/articles/simplicity-vs-choice/)and the tedious need to review a long list of items to find the desired one.
- **Avoid submenus within split buttons**, as it is difficult to move the cursor to the submenu without accidentally closing the main menu.
- **Disable items that are not relevant** or unavailable for the current task.
- **Order the items within the menu****by popularity** (for a small number of items), **or alphabetically** (for a larger number of items with names that will be known to users). Ordering helps users find the command they need without having to exhaustively review all options. For a small number of items (fewer than 5 or so), ordering them by popularity makes the most important items quickly available. For more than 5 menu options, alphabetical order makes it easier for users to predict where to find a known item in the menu order (according to [Hick-Hyman law](https://www.nngroup.com/videos/hicks-law-long-menus/)).
- **If keyboard shortcuts are available for any options within the menu, make those visible next to the command** to promote learnability.

## Persistent Split Buttons

A useful variation of split buttons is called a **persistent split button** (sometimes known as a **modal split button**). In this type of button, the default changes to the last action selected by the user (from the list of actions in the split-button menu). Thus, the user’s menu choice persists as the default (until, of course, the user makes a different selection from the menu). Thus, persistent split buttons allow a degree of [customization](https://www.nngroup.com/videos/personalization-customization/)for each user without the necessity of going through preferences and advanced application settings ([which many users will not engage with](https://www.nngroup.com/articles/customization-of-uis-and-products/)). They also speed up repetitive work or work in batches, where a user might utilize one option from a split button repeatedly for a short while, then switch to a related tool for a while, and so on.

![A persistent split button, where the user's selection becomes the new default.](https://media.nngroup.com/media/editor/2019/04/25/persistent-split-button.png)

*In the Windows Snipping Tool application, choosing an option from the split button’s menu (such as* Window Snip *) becomes the new default option, and clicking* New *would thereafter trigger a* Window Snip *(until the user chooses a different option from the menu). It is worth noting that in this example, the default label button remains,* New *, rather than* Window Snip *, which is very likely to cause confusion if the user is not aware of the current default state.*

However, the benefit that persistent split buttons have for power users has a [similarly strong detriment to new users](https://www.nngroup.com/articles/novice-vs-expert-users/). As users learn an interface, they rely on familiar cues, such as the position of a command within the interface, in order to recall where that command is. This spatial consistency helps to build a mental model of the UI. As the interface changes (for example because labels for buttons change), even subtly, with each use, the context clues to build that mental model become weaker, and the UI is less easy to learn. Users might be forced to ask themselves “where was that button again?” while trying to find a useful tool.

That is why persistent buttons are best avoided when you have a mix of power users and occasional users.

## Summary

Split buttons are most useful in repeat-use desktop applications with a large number of commands that need to be consolidated. While split buttons are efficient for accessing the most-commonly used tools, they can have a learnability and discoverability deficit for users. Ensure that the arrow section of the button is visually signified, provide clear descriptive text labels, and do not use split buttons for navigation menus on websites.
