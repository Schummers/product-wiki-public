---
title: "Accot-Zhai Steering Law: Implications for UI Design"
date: "2019-06-23"
url: "https://www.nngroup.com/articles/steering-law/"
author: "Page Laubheimer"
topics: [human-computer-interaction, interaction-design]
type: article
---

## In This Article:

- [The Steering Law](#toc-the-steering-law-1)
- [Making Menus Steer-Friendly](#toc-making-menus-steer-friendly-2)
- [Sliders, Scrollbars, and Scrubbers Need Additional Controls for Precision](#toc-sliders-scrollbars-and-scrubbers-need-additional-controls-for-precision-3)
- [Be Generous](#toc-be-generous-4)
- [Summary](#toc-summary-5)
- [References](#toc-references-6)

## The Steering Law

The Accot-Zhai steering law (discovered by HCI researchers Johnny Accot and Shumin Zhai, but also known simply as the steering law) is a corollary of [Fitts’s Law](https://www.nngroup.com/videos/fittss-law/). The steering law is an equation that predicts the efficiency of very common interactions; it describes the particular case of path-steering tasks — that is, when a user must move a pointer through a path with boundaries or a “tunnel.” The equation is:

![Accot-Zhai Steering Law equation, T = a+b(A/W)](https://media.nngroup.com/media/editor/2019/05/31/steeringlawequation.png)

T *is the overall movement time,* a *and* b *are constants, A**is the length of the tunnel, and* W *is the width of the tunnel.*

Don’t worry, most UX professionals will never need to use this equation: the main actionable insight is that long, narrow tunnels take more time to navigate than short, wide tunnels.

> The steering law predicts the time necessary to steer a pointer (such as a mouse cursor) through a bounded tunnel (such as a menu, a scroll bar, or slider). The steering time depends on the length and the width of the tunnel: the longer and the narrower the tunnel, the more time will be required to successfully steer through it.

According to the steering law, a **tunnel** is any user-interface control that requires the user to move the cursor (or drag a finger on a touchscreen) along a **path that has borders**. Overstepping the border will have some consequence, though since this is a common user error, the consequences will hopefully be mild, such as having the computer stop paying attention while the pointer is outside the tunnel. Some of the most common UI elements that involve this type of interaction include [dropdown menus](https://www.nngroup.com/articles/drop-down-menus/) (particularly hierarchical menus with hover-revealed submenus), [parameter-control sliders](https://www.nngroup.com/articles/gui-slider-controls/), scroll bars, video-playback scrubber bars, and video-game elements that require drag and drop in a straight line.

![YouTube's video scrubber playback control](https://media.nngroup.com/media/editor/2019/05/31/video-scrubber.png)

*On YouTube, the playback scrubber at the bottom of the video is an example of a tunnel that obeys the Steering Law.*

In most cases, moving outside the tunnel boundaries interrupts the user action: for example, in a hierarchical dropdown menu, if the user moves the cursor outside the menu area, the menu disappears (which is a somewhat harsh penalty, if the tunnel breakage was unintentional). That is why the width of the tunnel is important for how easily the user can steer through — a narrow tunnel makes it easy to accidentally exit the tunnel area.

![macOS hierarchical menu showing a path steering task with 90-degree turns](https://media.nngroup.com/media/editor/2019/05/31/macos-lshape-menu.png)

*On MacOS, moving the mouse cursor through a hierarchical menu involves a series of linear path-steering tasks separated by 90-degree turns. Within the main menu, submenus open on hover. Note that the second step in this L-shaped sequence (moving from* Find *to its child menu) involves the narrowest tunnel, which is slow and difficult for users to move through without errors.*

![macOS hierarchical menu showing typical user diagonal mouse movement patterns](https://media.nngroup.com/media/editor/2019/05/31/macos-diagonal-menu.png)

*Many users will attempt to move diagonally from* Find *to an item in the child menu, but, because in doing so their mouse will cross the area for* Spelling and Grammar *, the target submenu will be lost and instead the* Spelling and Grammar *one will be opened. (Note that older versions of MacOS featured a menu designed by NN/g principal Bruce Tognazzini; that menu did not exhibit this behavior, but instead, used a vector-based triangular buffer to allow users to move diagonally. Unfortunately, in the years since, Apple has reverted this excellent bit of interaction design.)*

Why people have trouble maintaining the cursor on a straight path has to do with human physiology: the elbow and wrist, which enable the movement of the hand, describe an arc, not a line. Try it yourself: hold your arm out directly in front of you and move your hand from left to right. You’ll notice that, even if you attempt to keep it moving in a straight line, your arm will always have a subtle arc in the movement. As a result, using one’s hand to move in a long, straight line is physically difficult; the longer the motion, the greater the chance of error. Furthermore, many users (especially older adults and those with disabilities) have unsteady hands, and all mobile users are subject to the bumps and jitters of using a device out in the world.

## Making Menus Steer-Friendly

Menus are one of the UI elements most affected by the steering law. Here are a few design choices to make them easy to use.

**Keep dropdown menus as short as possible .** Menus with few choices minimize the time and difficulty of steering through the narrow tunnel, and also reduces the time to [visually search](https://www.nngroup.com/videos/hicks-law-long-menus/) through a large number of choices.

**Avoid hierarchical menus**, particularly hierarchical menus that are more than two-levels deep. Hierarchical menus are inherently a difficult UI to design well due to Steering Law constraints. There will always be a tradeoff between designing the two tunnels associated with a hierarchical menu: the vertical tunnel that corresponds to the main-menu area and the horizontal tunnel, that corresponds to subcategory name that the user has to traverse to open the submenu:

- The vertical tunnel needs to be short, but that means that each of the items in the menu may have to be given smaller height — which leads to narrow horizontal tunnels.
- The vertical tunnel must also be wide, but that leads to longer horizontal tunnels from main-menu option to the corresponding submenu.

![Two views of Costco.com hierarchical menus, showing the tradeoff in width vs height of menus](https://media.nngroup.com/media/editor/2019/05/31/menu-width-optimization-zoom.png)

*This hierarchical menu on Costco.com shows the inherent tradeoff of optimizing a hierarchical menu for steering-law effects and compromising between the sizes of the vertical tunnel (left) and the horizontal tunnel (right). A wide menu optimizes the vertical tunnel for ease of steering down the menu, especially for menus with many choices. However, by making the menu wide, the length of the horizontal tunnel is increased, and moving across the menu to access the corresponding submenu is more fraught with errors. Note that most menus have not been optimized at all for the Steering Law, as they are simply made as wide as the longest text label.*

When a hierarchical menu is absolutely necessary, use a short time delay between mouse hover and when reveal of the child menu (or use a vector-based triangular system to allow for some diagonal movement error). Also include as much padding as reasonably possible above and below each menu item, to increase the width of the tunnel for horizontal movement.

For navigation menus, consider[mega menus](https://www.nngroup.com/articles/mega-menus-work-well/) (or square menus) as an alternative to [pull-down](https://www.nngroup.com/articles/expandable-menus/) menus. As mega menus allow for free movement within a wide 2D space, the steering law does not apply (though Fitts’s Law still does, so make sure targets are still large).

## Sliders, Scrollbars, and Scrubbers Need Additional Controls for Precision

When designing other UI elements that involve path-steering tasks, such as sliders, scrollbars, and video playback heads, remember that users will have a hard time achieving precision with such controls. Therefore, for precise tasks, [supplement these UI elements with other secondary controls that support precision.](https://www.nngroup.com/articles/gui-slider-controls/) When using a slider to select a parameter value, use the slider as a coarse control (for reaching the general desired region), and provide a secondary fine control (such as numeric input box with [stepper](https://www.nngroup.com/articles/input-steppers/) buttons) to choose a specific value. Also, allow users to click anywhere on the slider to jump to the desired position, rather than requiring them to click and drag; this approach enables a user to move freely in 2D space without needing to steer through the tunnel. On touchscreens, think about the overall target size of the slider knob (it should be at least [1cm x 1cm](https://www.nngroup.com/articles/touch-target-size/)) and ensure that the user’s finger won’t obscure the slider (or any labels around it).

## Be Generous

Finally, you can add padding to a tunnel, making its effective width bigger than its visual representation on the screen. The padding will allow some wiggle room for the user to move along the tunnel without dropping out because of a small deviation outside the tunnel’s visual area.

## Summary

The steering law states that narrow, long tunnels are more difficult to navigate than short, wide ones. Dropdown menus, hierarchical menus, sliders, and other path-following UI elements should be designed so that the corresponding tunnel is as wide and as short as possible. Remember that such controls are hard to use for precise tasks and consider alternatives (such as mega menus instead of dropdowns or secondary controls for sliders) to prevent errors due to linear path-steering interactions.

## References

Johnny Accot and Shumin Zhai. 1997. “Beyond Fitts' law: models for trajectory-based HCI tasks,” *Proceedings of CHI '97.*

Sergey Kulikov, I. Scott MacKenzie, Wolfgang Stuerzlinger. 2005. “Measuring the Effective Parameters of Steering Motions,” *CHI '05 Extended Abstracts on Human Factors in Computing Systems*.
