---
title: "Expandable Menus: Pull-Down, Square, or Pie?"
date: "2016-05-08"
url: "https://www.nngroup.com/articles/expandable-menus/"
author: "Raluca Budiu"
topics: [human-computer-interaction, interaction-design]
type: article
---

Originally developed at PARC back in the 1970s, **menus** are lists of options in a graphical user interface (GUI). They can be either **visible** (sometimes called “menu bars”) or **expandable.** In expandable menus, the list of options is exposed when a **menu****handle** is clicked or tapped; the menu handle can be a label, an icon, or both. In this article we focus on expandable menus.

## In This Article:

- [Two Design Problems for Expandable Menus](#toc-two-design-problems-for-expandable-menus-1)
- [Fitts’ Law and Movement Time](#toc-fitts-law-and-movement-time-2)
- [Linear (or Pull-Down Menus)](#toc-linear-or-pull-down-menus-3)
- [Rectangular (or Square) Menus](#toc-rectangular-or-square-menus-4)
- [Pie (or Radial) Menus](#toc-pie-or-radial-menus-5)
- [Marking Menus](#toc-marking-menus-6)
- [Other Types of Menus](#toc-other-types-of-menus-7)
- [How About Touch?](#toc-how-about-touch-8)
- [Conclusion](#toc-conclusion-9)

## Two Design Problems for Expandable Menus

*Internet Explorer menu bar (left) and* File *menu (right). The* File *menu is an expandable menu hidden under the handle “File.” The menu option* Send *is further expandable to display a submenu.*

The two big design problems concerning expandable menus are:

- **How make menus discoverable**, or in other words, how to make the handle look clickable (so people click on it) and have good [information scent](https://www.nngroup.com/articles/information-scent/)
- **How to minimize selection time** inside a menu, that is, how to reduce the time to *find* and *click* on the right option

The selection time itself has two components:

1. **The visual-search time:** the time to locate the item of interest among the set of options inside the menu
2. **The movement time**: the time needed to move the cursor (or finger) to the item of interest located by visual search

**Familiarity** with the type of menu modulates both these components. If users have to first learn how to operate a menu, then this learning time can easily dwarf any savings in selection time unless they will use that same menu many, many times. Also, the initial use of a new interaction method is more error prone, and the time wasted recovering form errors is hugely larger than the time savings from optimizing selection time.

Over the last 35 years, HCI researchers have explored various types of menus and of menu organizations, in the attempt to minimize either the visual-search time or the movement time. This article surveys several menu types and discusses how well they fare with respect to average movement time. But before discussing the different types of menus, let’s see how we can quantify the movement time.

## Fitts’ Law and Movement Time

[Fitts’ law](http://www.asktog.com/columns/022DesignedToGiveFitts.html) calculates the time it takes people to reach any target, whether using a mouse, a finger, or even their hands to grab an object. What it says is simple and makes intuitive sense: the time it takes people to reach a target depends on:

- The size of the target (the smaller the target, the longer the time)
- The distance to the target (the farther away the target, the longer the time)

*Fitts’ law says that the time to reach Target A is shorter than the time to reach any of the other targets. Although Targets A and B have the same size, the distance from cursor to A (d1) is shorter than the distance to B (d2), so movement to A will be faster. Target C is placed at the same distance (d1) from the cursor as Target A, but it’s smaller, so it will take longer to move the cursor to it than to A.*

While the [target size](https://www.nngroup.com/articles/touch-target-size/) usually informs our design for buttons and other active elements, the distance to target is the component that is usually optimized for menu design.

## Linear (or Pull-Down Menus)

To understand the time it takes to reach a target in a menu, let’s first focus on a mouse-based interaction in a traditional pull-down or drop-down menu. (This type of menu is also called a linear menu because all the menu options are displayed in a list.) We will assume that the menu has been just triggered by clicking on the menu handle. As a result, the menu options are now visible on the screen and the cursor is placed on the menu handle.

*In a linear menu, the time to reach the first item in the menu is shortest and the time to reach the last element is longest because the distance from the cursor (that is, menu handle) to the first element is the shortest and the distance to the last element is the longest.*

Note that the time it takes to reach the first element in the menu is shorter than the time it takes to reach any other element in the menu — simply because the distance to that first element is shorter than the distance to the second element, which is shorter than the distance to the third element and so on. In fact, the last element in the menu takes the longest time to reach because it’s the farthest away from the handle. This is one of the reasons for which we recommend against overly long menus — it takes a long time for people to select one item from such a menu (plus, sometimes, it is even more challenging if the menu is longer than the window size and users must scroll down the page).

Can we improve the average movement time in a linear menu? One simple improvement is to actually change the position of the list so that the middle element is aligned with the handle instead of the first element. By doing that, you’ve decreased the average distance to a menu element.

*By aligning the menu handle with the middle element, you reduce the average movement time to click options inside the menu.*

(Unfortunately it is not always possible to use a menu like this one simply because there may be not enough space above the handle to display half of the options.)

## Rectangular (or Square) Menus

Another way to reduce the distance to the menu options is to place them in a rectangle. Hence the **rectangular** (sometimes called square) **menu**, better known as the [megamenu](https://www.nngroup.com/articles/mega-menus-work-well/).

*The average distance to an item inside a megamenu is smaller than if all the items were placed in a long list one under the other (that is, in a linear menu).*

It’s easy to show (using a little bit of geometry) that the rectangular menu has better average distance to any random element than the linear menu. Rectangular menus work quite well in terms of optimizing the movement time, and nowadays they are hugely popular on the web.

## Pie (or Radial) Menus

What if the time to all elements of the menu was the same? That is possible if all the elements are at equal distance from the handle — that is, they are placed on a circle centered in the menu handle. That’s how the **pie (or radial) menu** was born. Believe it or not, the pie menus are quite old: they date from the late 1980s.

*One Note pie menu: the handle is in the middle of the circle, and all the menu options are displayed around it. The distance to any of the options is the same.*

Pie menus have never been really popular. Although HCI researchers love them, it turns out that users are not quite familiar with them. A 2010 study showed that in practice they are harder to learn than the more standard linear and rectangular menus, so the movement-time gain is lost due to lack of familiarity with this interface. However, as users become more familiar with the pie menus, these menus do start to show the advantage that researchers have predicted.

*Yelp for iPhone uses a “half-pie” menu to display options related to reviewing a service.*

(We wrote an April Fool’s article suggesting that [pizza menus are even better than pie menus](https://www.nngroup.com/articles/hamburger-menu-vs-pizza/). However, that was a joke, and pizza menus aren’t a real design concept.)

## Marking Menus

Marking menus are a version of the pie menus that takes advantage of the fact that menu items are uniquely defined by their direction. In other words, when the user starts moving towards a target, you can tell what the target is going to be before the target is hit, just by looking at the direction of the movement.

Marking menus have two “modes”: in *normal mode*, the menu gets expanded when the handle is clicked, and then you can select an option either by clicking an item (like in a regular pie menu) or by moving the cursor (or the finger) towards the desired item. In the *expert mode*, however, the menu does not get displayed: the user simply starts moving the cursor in the direction of the target (this action is called “making a mark”, hence the name “marking menu”) and the system interprets that gesture as the selection of the corresponding target. The expert mode makes sense for applications that receive heavy use, where users learn the arrangement of the menu options in the menu and don’t need to see them displayed (for instance, Kurtenbach and Buxton showed in 1994 that the expert mode is preferred by users in the context of a task that required more than 9 hours of audio editing per user).

*Pinterest for iPad uses a marking menu that has only the normal mode. Once the user presses the menu handle, the menu gets expanded and the user can select an option by moving the finger in the direction of that option. As soon as the user lifts the finger, the highlighted option is selected and the menu disappears.*

Marking menus are well suited for contextual use, being more efficient because users do not need to travel the whole route to the target, but they can just start moving towards the target. In expert mode, the menu also saves users an extra step (that of expanding the menu and inspecting the items inside). Of course, the expert mode is too error-prone for less skilled users, since they don’t get visual confirmation of their choices.

## Other Types of Menus

HCI researchers have experimented with many variations on these menus in their attempt to minimize movement time inside the menu (an example included a linear menu in which elements farther away from the handle got larger target areas to compensate for the increase in distance). Most of these never found their way in real-world interfaces because, in spite of their nice theoretical properties, they were unfamiliar and hard to get used to, so they never became popular on the web.

## How About Touch?

Although Fitts’ law does apply to touch interfaces, one assumption that does not transfer easily when it comes to menu design is that of the initial cursor position. With the mouse, one can assume that immediately after opening a menu, the cursor is still on the handle. But with a touchscreen it’s very possible that after a menu has been opened, the finger position is no longer on the handle or even above it. (This is true in particular for mobile handheld devices —phones and tablets; for [very large touchscreens](https://www.nngroup.com/articles/very-large-touchscreen-ux-design/) (e.g., tabletops), where often the entire body needs to be moved to get to an area, it is possible that the user and the hands are still in closer proximity of the handle.) Keeping the finger above the menu handle is usually unproductive because it obscures part of the screen. Plus, many times the handle actually disappears or is moved to a different area of the screen.

*Gmail for iPad: The hamburger icon (top screenshot) expands a sliding menu that pushes the menu handle (the hamburger) towards the middle of the page (bottom screenshot). Even if the finger position were to stay unchanged after the menu got expanded, the user would have to move it out of the way to see the elements inside the menu. (The blue area approximately represents the finger.)*

Thus, many of the considerations we discuss in this article do not necessarily apply. The interesting question for touch handhelds is where the menu is displayed in relation to the most likely position of the hands and fingers, and how to optimize menu reach time relative to that positon.

That being said, there is one exception: marking menus in the normal mode (like the one in the Pinterest app displayed above). Marking menus are well suited for touch interfaces, because they don’t require a precise reach of the target (which tends to be problematic with touchscreen interfaces due to our [fat fingers](https://www.nngroup.com/articles/mouse-vs-fingers-input-device/)). To preserve the movement-time advantage, they do require that the finger stay put on the handle and then move in the direction of the desired option. The disadvantages of this constraint are two: (1) there is a certain physical strain associated with keeping the finger in the same spot for a given amount of time to inspect the menu elements; (2) the finger does block part of the screen, so often these menus work best as circle fragments.

Pie and marking menus have encountered their moment of glory in the era of touchscreen devices. We see more and more versions of these menus in touch apps. Finally, these menus are in a good position to overcome the unfamiliarity obstacle and translate their theoretical advantages to the real world. However, many of these menus are not optimally designed. Remember, a normal pie menu (like in the Yelp app above), where the menu stays on the screen when the finger is lifted from the handle and the user can select an option by tapping on the desired item, does not gain you the movement-time benefits.

## Conclusion

Movement time in an expandable menu is governed by Fitts’ law. Linear menus are best when the number of menu options is small; as the number increases, rectangular menus (or megamenus) are more appropriate. Marking menus are well suited for touchscreens, and, like pie menus, optimize the reach time to individual options, but are only now starting to become more familiar due to their popularity on touchscreen devices. If you’re considering a new, less familiar menu because it has good movement time (or any other desirable quality), reserve it for cases with high-frequency use or wait until the design has become more familiar.

### References

D. Ahlström, A. Cockburn, C. Gutwin, and P. Irani. 2010. Why it's quick to be square: modelling new and existing hierarchical menu designs. ACM CHI’10, 1371-1380. DOI=[http://dx.doi.org/10.1145/1753326.1753534](http://dx.doi.org/10.1145/1753326.1753534)

G. Kurtenbach, and W. Buxton, W. 1994. User learning and performance with marking menus. ACM CHI '94, 258-264. DOI=[http://dx.doi.org/10.1145/191666.191759](http://dx.doi.org/10.1145/191666.191759)
