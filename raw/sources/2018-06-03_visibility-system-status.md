---
title: "Visibility of System Status (Usability Heuristic #1)"
date: "2018-06-03"
url: "https://www.nngroup.com/articles/visibility-system-status/"
author: "Aurora Harley"
topics: [heuristic-evaluation, human-computer-interaction, web-usability]
type: article
---

*Download a free poster of Jakob’s Usability Heuristic #1 at the bottom of this article.*

The first of Jakob Nielsen’s [ten heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) — visibility of system status — relates to so much more than user-interface design. At its essence, it is about communication and transparency, which are critical to many aspects of life. People strive for predictability and control, and, in most cases, **more information translates to better decision making**.

Wherever you are, whatever you are doing, take a few moments to look around and note the various types of systems around you, and how they communicate their current status. Your phone or laptop display how much battery life remains; your email application tells you how many unread emails you have; a sign in the subway indicates the next stop (or, if you’ve missed the last one, how many minutes until the next train arrives at the station). All these nuggets of information allow you to accurately assess the current state of the systems you interact with.

> **Visibility of system status:** How well the state of the system is conveyed to its users. Ideally, systems should always keep users informed about what is going on, through appropriate feedback within reasonable time.

## In This Article:

- [Knowledge Is Power](#toc-knowledge-is-power-1)
- [Appropriate Feedback](#toc-appropriate-feedback-2)
- [Compel Users to Action](#toc-compel-users-to-action-3)
- [Communication Creates Trust](#toc-communication-creates-trust-4)
- [Conclusion](#toc-conclusion-5)

## Knowledge Is Power

Only by knowing what the current system status is can you change it — that is, you can overcome the [gulf of evaluation](https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/) and figure out what you need to do next in order to reach your goal.

For instance, when you drive a car, you need to continuously see its speed to decide if you need to go faster or slow down. Those who have ever driven a car where the speedometer was broken can attest to the fact that it’s quite difficult. When this happened to me, I felt at the mercy of the cars around me, as I attempted to keep pace and blindly trust that they were going at a reasonable speed. **A lack of information often equates to a lack of control**.

## Appropriate Feedback

Whenever users interact with a system, they need to know whether the interaction was successful. Did the system actually catch that button press or was it busy with something else and it ignored it? Did the item get added to cart? Did the request go through? (One reason users have these questions is that they have been [burned before by technology that didn’t work properly](https://www.nngroup.com/articles/time-to-make-tech-work/). However, even when the happy day of bug-free technology arrives, people will still wonder if they really clicked or tapped correctly.)

Appropriate feedback for a user action is perhaps the most basic guideline of user-interface design. It serves to keep users informed of the current status and to allow them to steer the interaction in the right direction, without wasting effort.

Such feedback can be as simple as a change of color once the user has clicked on a button, or a [progress indicator](https://www.nngroup.com/articles/progress-indicators/) when a process needs a little longer to finish. These indicators communicate that the system is working, and reduce uncertainty — preventing users from, say, tapping the same button multiple times because they weren’t sure if the first time worked.

![2 screenshot examples of communicating system status through feedback](https://media.nngroup.com/media/editor/2018/05/22/systemstatus-ui_feedback.png)

*Changing the color and adding a checkmark to buttons on a selection screen communicates that the system has registered the user’s choices (left). Progress indicators reassure the user that a longer wait is normal, and that the system is still working (right).* Your browser does not support the video tag.

*In this video clip from our mobile eyetracking study, the user has clicked on a button and is unsure whether a new page is actually loading because there is no feedback. The hollow red circle shows where the user is fixating on the screen. We can see that she looks back and forth between the button and the top of the screen, where a progress indicator for the page load typically appears, to assess whether anything is happening. (In most browsers, hover over the video to display the controls if they're not already visible.)*

Providing immediate feedback for interactive events allows users to quickly identify the source of [errors](https://www.nngroup.com/articles/user-mistakes/) and fix them as soon as they were made. In fact, [immediate feedback](https://www.nngroup.com/articles/response-times-3-important-limits/) is one of the main benefits of [direct manipulation](https://www.nngroup.com/articles/direct-manipulation/), an interaction style in which users can act directly upon different UI objects. In contrast to direct-manipulation UIs, command-line interfaces do not display the current state of the system, nor do they give immediate feedback. Programmers know how difficult it can be to locate the source of an error in an interface which lacks immediate feedback; they often have to resort to tools such as breakpoints and stepping to understand how the state of the system changes with each action specified in their code.

Do you want your users to feel like they’re using DOS or Unix? The real difference between these ancient command-line UIs and modern GUI designs is not the presence of colorful icons. It’s visibility of system status.

![Screenshot of songs getting reordered using drag and drop for a playlist on the Amazon Prime Music mobile app](https://media.nngroup.com/media/editor/2018/05/22/amazonmusicapp_playlist_directmanipulationstatus.png)

*The Amazon Music app on iOS allows users to directly manipulate the order of items within a playlist. Users are aware of the system status at all times, and thus can easily identify and correct an error.*

Even when users cannot see the effect of an action because the system does not have a screen (like is the case for [voice-only devices](https://www.nngroup.com/articles/voice-interaction-ux/) such as Amazon Echo and Google Home), a minimum feedback that the command was heard is essential. Amazon’s Echo displays a ring of light on the device to indicate that it is currently listening or working on the command. This on–off type of indicator isn’t as good as a running timer, for example, but at least the user can be assured that the system heard the command and the timer was set in the first place.

## Compel Users to Action

Modern systems are often complex, and it is unreasonable to assume that all the variables that describe the state of a system can be communicated to the user. Many [backstage components](https://www.nngroup.com/articles/service-design-101/), such as what JavaScript files are downloading and executing to make a site work, are of little interest to users. Yet, occasionally backstage aspects can actually play an important role frontstage.

Take, for instance, the case of inventory size. How much stock is available for a product is usually not relevant to users and should not be displayed. Yet, there are two exceptions:

1. When the stock is low: If people know that there are just a few items left, they are more likely to act immediately — following biases such as [scarcity](https://www.nngroup.com/articles/scarcity-principle-ux/) and [social proof](https://www.nngroup.com/articles/social-proof-ux/).
2. When there are no items in stock: This information can save the users the effort of trying to add to cart products that are no longer available. (Losing the immediate order is preferable to [losing credibility](https://www.nngroup.com/articles/trustworthy-design/) for future orders, which will never be placed if users feel that they cannot trust you.)

![Screenshot of product quick view on J.Crew site](https://media.nngroup.com/media/editor/2018/05/22/visibilityofsystemstatus-onlyafewleft_inquicklook-jcrew_dress.jpg)

*The J.Crew site displays a notification that there are “Only a Few Left!” when the user moves the mouse over low-stock sizes of a product. Some sizes are already sold out, and thus shown crossed out in light gray.*

Communicating how far away a user currently is from qualifying for free shipping or another type of deal can also encourage additional purchases.

![Screenshot of NatureBox website with 1 item added into the cart](https://media.nngroup.com/media/editor/2018/05/22/almosttofreeshippingstatus_naturebox.png)

*NatureBox.com: A banner across the top of the page communicates how much more money the user needs to spend to qualify for free shipping.*

To communicate backstage events that may impact users, you can use either [notifications or indicators](https://www.nngroup.com/articles/indicators-validations-notifications/). [Modal dialogs](https://www.nngroup.com/articles/modal-nonmodal-dialog/) are also used to inform people of state changes that can significantly affect them.

## Communication Creates Trust

When, in a real-life relationship with a person, that person withholds information from us or makes decisions unilaterally, we start losing trust and feel that the relationship is no longer on equal footing. The same thing happens when we interact with a system.

When we understand the system’s state, [we feel in control](https://www.nngroup.com/articles/ideologies-of-web-design/) — we can rely on the system to act as expected in all circumstances. The predictability of the interaction creates trust not only in the mechanics of the site or the app, but also in the [brand](https://www.nngroup.com/articles/interaction-branding/) itself.

Sites and apps should **clearly communicate to users what the system’s state is** — no action with consequences to users should be taken without informing them. When an external event or the passage of time caused a change in the state of the system, explain it in brief but understandable terms.

For example, what should happen when a user revisits a previously created wish list that now contains items that are out of stock or no longer sold? The worst user experience would be if those items simply disappeared from the list, with no explanation why. How about a notification at the top of the screen? This would be only slightly better because it would not help the user remember what items had previously been on the list to find suitable replacements. Both of these methods take control away from the user and degrade trust — users may stop relying on the wish list if the items in it sometimes disappear on their own.

A better **way to build trust is to explicitly communicate the current system’s status** — which items are no longer available — and then allow the user to either remove them from the list or keep them visible for future reference.

![Screenshot of out of stock items on wish list at Loft website](https://media.nngroup.com/media/editor/2018/05/22/systemstatus_wishlist_itemoutofstock.png)

*Loft.com continues to display out-of-stock items in wish lists, with appropriate messaging to communicate the status of the item to the user.*

## Conclusion

The visibility of system status is a basic tenet of a great user experience. At its core, this heuristic encourages open and continuous communication, which is fundamental to all relationships — whether with people or devices. Users who are uninformed about the system’s current status cannot decide what to do next in order to accomplish their goals, nor can they figure out if their actions were effective or if they made a mistake. **Don’t blindfold your users!**
