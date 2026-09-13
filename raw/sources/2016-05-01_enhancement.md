---
title: "The Role of Enhancement in Web Design"
date: "2016-05-01"
url: "https://www.nngroup.com/articles/enhancement/"
author: "Raluca Budiu"
topics: [human-computer-interaction, interaction-design, web-usability]
type: article
---

A recent question that we got on Twitter asked whether it’s ok to use the right click in web apps. While we do have [guidelines that address this specific issue](https://www.nngroup.com/articles/feature-richness-and-user-engagement/), the question brought to mind an important concept in usability and design — the concept of enhancement.

Definition: An **enhancement** is a feature that speeds up or enriches the interaction for some of the users, but is not essential for accomplishing a task. In other words, it’s something that some users can take advantage of, but they don’t have to and they can easily live without it. Some forms of enhancements are also known as **accelerators** or **shortcuts**. In many user interfaces, they are a key way to support one of the [classic usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/): **flexibility and efficiency of use**.

If you are a coder, you’ve likely heard of “progressive enhancement.” Although it’s been introduced way back in 2003, the concept’s popularity surged with the advent of [responsive](https://www.nngroup.com/articles/responsive-web-design-definition/) and [adaptive](https://www.nngroup.com/articles/mobile-vs-responsive/) web design. Progressive enhancement refers to a strategy of web design that offers basic functionality and content to all users, while enhancing the experience with specific additional features on those platforms (e.g., browsers) that support them. For example, all users on all platforms will be able to type in a search box, but if the device supports voice recognition, users will also be able to dictate their queries. A multidevice interface that supported only voice queries and no typing would not be usable because it would prevent a segment of its users from using that features.

(Progressive enhancement is not the same as [progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/), which always starts out presenting the user with a limited set of core features and then may display advanced or rare features when they’re needed. The distinction is that in progressive enhancement, the computer or the server decides which features should be available on which device, whereas in progressive disclosure, all the features are present at all times, but the user may see some of them only after they spent some time interacting with the system.)

But the concept of enhancement goes beyond coding and can be applied more generally to usability, when we design any experiences that involve different types of users, be they users on different platforms or devices, or users with different expertise and knowledge of the web.

## In This Article:

- [When Should a Feature Be an Enhancement?](#toc-when-should-a-feature-be-an-enhancement-1)
- [From Enhancement to Standard](#toc-from-enhancement-to-standard-2)
- [The Rule of Enhancement](#toc-the-rule-of-enhancement-3)

## When Should a Feature Be an Enhancement?

The answer depends on two factors: (1) the technology and its available features, and (2) the users’ abilities.

1. **Technology**.

If your software will run on several devices with different capabilities, then on some of these devices enhancements can be used to speed up the interaction. For example, if the device has a camera, it can quickly scan bar codes. But for those devices with no cameras, it should still be possible to input bar codes through some other method. (This is the original, web-development view of enhancement.) Similarly, the [3D Touch](https://www.nngroup.com/articles/3d-touch/) is only available on iPhone 6S, so that gesture should only be used to access enhancement to the interface.

*Amazon for iPhone: You can take a picture of an object and search for it on Amazon. This feature takes advantage of the smartphone’s camera and is an enhancement only available in the mobile app. On desktop, users can search only by typing in their query.*

1. **Users’ knowledge and abilities**. If the users are not familiar with a certain type of interaction (e.g., a gesture), then the function supported by that interaction should also be accessible through some other path in the interface. For example, in Safari for iOS, the *Back* functionality is achieved by either a horizontal swipe on the left edge (enhancement) or by tapping the visible arrow at the bottom of the screen. The swipe is an enhancement because not all users are familiar with it as this point

*The swipe gesture in the Mail app (iPhone) is an enhancement: it can be used to quickly delete a message (top). However, users who are not familiar with that gesture can still achieve the same action (delete) by using the* Edit *button in the interface.*

Occasionally, users can be familiar with a gesture but may have trouble performing it accurately. For example, scrolling down using a vertical scrollbar is a feature most adults are familiar with; however, keeping the mouse within that narrow bar is not an easy motor feat. As a result, most modern interfaces support other ways of scrolling down besides moving the mouse within a small tunnel. In most interfaces, the scroll bar acts an enhancement: its value is usually not for supporting scrolling, but rather its visual presence (a) reminds users to scroll and (b) informs them how far down the page they’ve scrolled.

## From Enhancement to Standard

Sometimes an enhancement proves so useful that it morphs from being something extra to being the main way of accomplishing an interaction. The scroll wheel is a good example of this evolution: early commercial mice didn’t include a scroll wheel (though a few research-lab prototypes did). The Microsoft IntelliMouse introduced the scroll wheel to mainstream use in 1996, but for the next several years, using a mouse wheel to scroll would have been an enhancement. Twenty years later wheel-based scrolling has become the main way to scroll on desktops, and we would now consider other ways of scrolling to be the enhancements. (Note however that we cannot rely exclusively on the scroll wheel to implement scrolling because there are devices on which this gesture is not available: touchscreen tablets, and laptops are only two examples.)

Now that most desktop users have a scroll wheel, this hardware facility has taken on enhancements of its own. For example, many web browsers allow users to change the font size by holding down the control key while scrolling the wheel. While this is a nice feature, it’s definitely still only an enhancement and software needs to support other, more visible, means of adjusting font sizes.

Some gestures or actions may start as enhancements and later become so standard that they no longer need extra support in the interface and can become the only way through which an action is performed. However, we advise a high degree of conservatism in disabling older interaction mechanisms, since some users may be so ingrained in their behaviors that they keep doing things the old way, even after a newer (and better) way has become mainstream. Usually, the preferred choice is to downplay the older mechanism and make it less visible in the user interface, but retain it as an enhancement for those users who prefer it.

Enhancements that become standards are an ideal, gentle route for innovations in user-interface design. If you are thinking to introduce a new feature, start by providing it as an enhancement. But beware, the road from enhancement to standard is full of temptations, and it’s easy for a smart UI innovation to be ignored or quickly forgotten. There are two crucial aspects to making an enhancement catch on and advance all the way to standard:

1. Don’t add other enhancements that provide the same functionality. (In psychology, this is called **the fan effect**: the more facts associated to one concept, the harder it is to remember these facts. Thus, if you can do the same action in many different ways, it’s going to be more difficult to recall any one of them.) You want to give people the chance to practice and strengthen the enhancement; if you add other enhancements for the same interface functionality, it will be less likely that any one of them will get enough use.
2. Be consistent. Use the same enhancement everywhere you can. That is, try to give users many opportunities to practice and thus strengthen the association between the enhancement and its effect in the interface. (Remember, [repetition is the mother of retention](https://www.nngroup.com/articles/recognition-and-recall/).) Ideally, designers should use the same enhancements across many different sites, to allow people to learn them.

## The Rule of Enhancement

The concept of enhancement allows us to quickly answer questions such as:

- Should I hide important functionality in contextual menus triggered on a right click?
- How should I use hover states in a responsive site?
- Should I use [horizontal scrolling to mimic touchscreen swipe](https://www.nngroup.com/articles/horizontal-scrolling/) in a responsive site when it’s displayed on a touchscreen?
- Should I use a gesture such as shake to implement “undo” in my iPhone app? More generally, should I create a new [gesture](http://www.jnd.org/dn.mss/gestural_interfaces_a_step_backwards_in_usability_6.html) to give users access to certain functionality?

*On Cartoon Network’s responsive site, hovering on the* Video *option in the navigation bar exposes shortcuts to specific-characters’ video pages. This feature is an enhancement: it does add to the experience, but is not essential for accessing the corresponding content. The inability to access these shortcuts will not significantly affect users on tablets and other touchscreen devices.*

The answer to all of these is pretty much the same: these features can be implemented as enhancements in your interface, but the UI should not rely on them for accomplishing any one task — either because some users will not know about them or not think to use them (in the case of right click, shake or other new gestures, and even horizontal scrolling) or because some users will not have access to them on certain platforms (in the case of hover). In other words, although we don’t normally advocate [redundancy](https://www.nngroup.com/articles/duplicate-links/) in user interfaces, enhancements like these are the one spot where redundancy is welcome: you can provide them as UI shortcuts, but people should be able to perform a similar task using other interface functionality.

The enhancement concept leads us to a unified, multidevice and cross-user guideline for user experience — the rule of enhancement: **Enhanced interactions that take advantage of specific user or device capabilities can be provided, but they should not be the primary way of accessing interface features.**

Our course [Scaling User Interfaces](https://www.nngroup.com/courses/scaling-responsive-design/) contains more unified guidelines for designing for multiple devices.
