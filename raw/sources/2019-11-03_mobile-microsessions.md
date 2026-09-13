---
title: "Mobile Microsessions"
date: "2019-11-03"
url: "https://www.nngroup.com/articles/mobile-microsessions/"
author: "Raluca Budiu"
topics: [mobile-and-tablet-design]
type: article
---

Have you ever briefly turned on your phone, glanced at it, found whatever needed to find, and then turned it back off? That’s an example of a microsession — a quick session with minimal interaction that completes a user goal.

Definition: **Mobile microsessions** are mobile sessions shorter than 15 seconds.

The word “microsession **”** follows the terminology introduced by an article by Ferreira and his colleagues, who coined the term “microusage” to refer to mobile usage that is shorter than 15 seconds. They found that a little more than 40% of the mobile usage was microusage.

While the exact time threshold may be arguable (and may vary depending on the population — for example, another study, coauthored by researchers from Stanford University and Apple, found that for elderly adults, the microsession threshold moves up to 22 seconds), it does not really matter. What matters is how to design your apps so that you can allow users to complete certain tasks quickly.

**Microsessions are good for the user experience**. Generally, time on task is inversely proportional with usability. Time translates in [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/), and low interaction cost leads to good user experience. A microsession means that users were able to reach their goal very quickly — likely, because the mobile design supported them.

## In This Article:

- [Supporting Microsessions Benefits Even Apps with Complex Tasks](#toc-supporting-microsessions-benefits-even-apps-with-complex-tasks-1)
- [Designing for Microsessions](#toc-designing-for-microsessions-2)
- [Familiarity](#toc-familiarity-3)
- [Conclusion](#toc-conclusion-4)
- [References](#toc-references-5)

## Supporting Microsessions Benefits Even Apps with Complex Tasks

There are many mobile tasks that we do every day and that are so simple that they can be easily completed in a few seconds. Setting an alarm, checking whether you have any new emails, looking up the calendar for the day usually involve just a quick glance at one screen and maybe 1–2 button presses. These are most likely to result in microsessions.

However, not all tasks can be completed in 15 seconds, even with the best possible design. Researching and buying an air purifier, watching a video, reading and following instructions, composing an email to your boss are all fairly complex activities and most users will take more than 15 seconds to complete them.

But even if your app involves several convoluted steps, **reducing the time to complete the task will improve the user experience.** A good design will often translate into a reduced interaction cost and thus low task time. Yet, it is not enough. You can do more.

To understand why, let’s think of a user who is trying to check in for a United Airlines flight on the phone. First, the user must find the app on her phone, launch it, wait for the splash screen to load, bypass a [login wall](https://www.nngroup.com/articles/login-walls/) or sign in if she does not notice the *Continue as guest* button, then find the *Check in* button on the United homepage, tap it, and eventually start the login process. In other words, she has to spend a lot of time to locate **an entry point** into the task.

*United for Android: When checking in by launching the app, the user has to wait for the splash screen to load (top left), then skip the login wall (top right), then find the Check in button on the homepage (bottom left) and finally get to the* Flight Check-in *page (bottom right).*

Designers can provide users with quick, outside-the-app access to the tasks that they perform the most. Doing so can save users the need to locate the entry point by themselves, and if the task is significant enough, can substantially improve the overall user experience.

## Designing for Microsessions

Of course, the first worry that you should have is to design your app so that the entry points to these tasks are easily discoverable within the app and the flows are simple and easy to understand. However, you can go one step further and allow people to start these tasks (and sometimes even complete them) without launching the app. Here are 4 common ways to design for microsessions and thus accommodate **external task entry points**:

### 1. Notifications

Notifications are the main way in which apps today support microsessions. About 60% of the microsessions in the Ferreira study involved reading or interacting with a notification.

Although notifications do provide at least one entry point to the app (tapping on the notification opens the app), in many cases their function is to update the user on a state of affairs. When a notification is well-designed, users can often get all the information they need from the text of the notification and may not need to launch the full app.

In order to design a successful, notification-based microsession, **create notifications that are self-sufficient**: that convey a fully formed idea and do not require the user to go elsewhere to understand what the notification is about. Text that is truncated or that does not include enough information forces people to gather additional context for the notification, and that action not only lengthens the session, but also degrades the user experience

*A Lyft notification provides all the info that the user needs in order to act upon the notification, without having to launch the app.*

If it’s not possible to create a notification that is entirely self-sufficient, **at least give users enough context to decide if they are interested in the notification.**

*This YouTube notification is not self-sufficient: The title of the video is truncated requiring the user to tap on it to see what it’s about. However, the keyword* Everleigh *present in the notification at least allows users to decide if it’s worth getting additional information. (If they never heard of Everleigh, then the notification is probably irrelevant; if they are enthusiastic fans, then they will probably attend to it.)**Amazon’s notification is not self-sufficient — it does not tell the user what item was delivered, but only that it was delivered. (The photo shows the package, but not the item.)**The default view of a notification on Android truncates the notification to 2 lines. If users expand the notification by tapping the down arrow in the top-right corner, they can see an additional line of text However, even though this notification from Settings on Android is truncated (left), there is enough information scent to understand its content (right).*

Make sure that tapping on the notification not only launches the corresponding app, but it takes users to the corresponding page in the app (for example, for a news story, that may be the article page). And, because most users are familiar with this functionality, it’s unnecessary to have an additional *Open up in app* action present in the notification.

*MyShake for iPhone notifies the user that an earthquake has occurred (left), but tapping on the notification does not offer any supplemental information. At the very least, the app should take the user to the location of the earthquake. Instead it simply shows the homepage of the app, which contains a map centered at the user’s current location (right).**ESPN for Android: The option* Open in App *is not necessary, since the same result can be obtained by simply tapping the notification text (a behavior that is highly familiar to mobile users).*

**Consider supporting the main actions that apply to the notification item within the notification itself.** Doing so presents the user with the opportunity to complete the task without launching the app. For example, for a news article, an appropriate action may be to save it for further reading, whereas for an email notification, deleting the message may be a good one to support.

*The notifications from Calendar for iPhone (left) and NYTimes for iPhone (middle) allow users to directly act upon the content they present. The notification from Linkedin (right) is self-sufficient, but would have benefited from a* Congratulate *button that would take the user directly to the message page.*

In some cases **, consider providing entry points into typical flows that the user may take from that notification**. For example, the Weather Channel’s Android app notification allows people to access weather info in different formats (*Hourly*, *Daily*, *Radar*).

*Weather Channel’s Android notification provided entry points into the* Hourly, Daily,*and* Radar *views of the local weather.*

### 2. Widgets

Widgets are compressed views of the app that usually present a single piece of data that represents the state of the app. They are ideal for tracking frequently changing information (such as weather) and are typically accessed from the phone’s homescreen (on iOS, from the *Search* screen), if the user chooses to add the respective widget to the screen.

In iOS, widgets can also be accessed through a long press or 3D touch gesture on the app icon, even if the user has not decided to install the widget.

*iOS widgets: (Left) The* Search *screen contains several widgets from multiple apps. (Right) Some apps also display a widget when the user long presses the app icon on the phone’s homescreen. The Maps app shows a widget offering directions to a frequent destination.**Android widgets: Widgets can have different shapes and display different types of content. The Gmail widget is a collection widget, that shows several emails and the CNN widget is an information widget. Note that the user can resize the widgets, as noticed by the two sizes of the CNN widget in the two screenshots. (However, even when the CNN widget is enlarged, right, the text displayed is still truncated — forcing the user to launch the app in order to get the full title and gist of the story.)*

Widgets are helpful because they allow users to quickly inspect data from the app and track if something has changed. **Like notifications, widgets should be self-contained and preferably not truncated**. For example, the CNN widget should not display a truncated title; instead, a full sentence should describe the story even at the smallest widget size.

Widgets are, however, more powerful than notifications. They allow simple interactions within the widget itself. For example, the user can scroll vertically within the Gmail widgets or can tap the lateral arrows to move through news stories in the CNN widget. And sometimes widgets simply offer a list of entry points to tasks in the app (similar to quick actions below).

The key issue for widget usability is **whether you can indeed identify the one thing people will want to track, and if so, whether you can compress that information into a concise unit for display in the widget**. If there are several items of potential interest, s, then a collection widget that shows them may be a solution, although the same general problems arise: can you reasonably focus on those few items that your users will want to see, and will they remain useful even after being seriously compressed to fit within the widget space?

*Unlike notifications, widgets allow some limited interactions. In iOS, it’s possible to expand a widget(left) and see additional content (right).*

*In Android, it’s possible to tap the arrows in the CNN widget in order to see more stories (top) or you can scroll vertically in the Gmail widget to expose more emails (bottom).**The Yelp widget for iOS provides entry points to various content-categories available within the app.*

### 3. Quick Actions

Recent versions of iOS and Android support accessing actions within an app directly from the homescreen, through a long press or a [3D Touch](https://www.nngroup.com/articles/3d-touch/) gesture — essentially an implementation of a [contextual menu](https://www.nngroup.com/articles/contextual-menus/). (Note: the 3D Touch is no longer supported on iPhones XI and it was replaced by the long press.) In iOS, the gesture can also display a widget alongside the quick actions.

*A long press on Amazon for iPhone (left) and United for Android (right) displays a list of actions that users can take directly, without having to open the app. Thus, using United’s* Check *-*in* quick action leads directly to the *Flight Check*-*in* page.*

The quick actions save users from having to launch the app and find the within-app entry point for the task they want to accomplish. The quick actions don’t need to include only tasks that can be microsessioned — instead, **they should link to tasks that are important to your users**.

There is only a limited number of quick actions that can be displayed in the quick-action contextual menu, so **don’t waste the space with actions that are likely irrelevant to your users**. Instead, **focus on the top tasks** — the tasks that are performed often by many users. For example, inviting friends to Airbnb is likely a rarely performed action, as is contributing to Google Maps — none of these actions need to be included on a quick-action list.

*Quick-action list should include actions that are important to your users and that they perform frequently. Neither* Invite friends *(Airbnb, left), nor* Your contributions *(Google Maps, right) qualify.*

### 4 . Through an Intelligent Assistant (Siri or Google Assistant)

Both iOS and Android apps can take advantage of [intelligent assistants](https://www.nngroup.com/articles/intelligent-assistant-usability/)— Siri and, respectively, Google Assistant — to allow users to quickly interact with the app using voice.

In iOS, applications can provide shortcuts to Siri that enable users to perform certain frequent tasks or tasks that are appropriate at certain moments of time and in certain locations. For example, upon noticing frequent payments to a certain person, the PayPal app can suggest a shortcut that enables the user to do that action directly through Siri. While the user has to accept these shortcuts **, it’s still important for the application to identify them and suggest them to the user** (ideally, even within the app).

*Application-suggested shortcuts enable the users to perform a specific action quickly. In this example, the PayPal app suggested a shortcut for a frequent payment, which is available both from the iPhone’s Shortcuts app (left) and, in this case, from the PayPal app itself (middle). After the user defines the shortcut (right), she can use the word* Cheese *to perform the action.*

In the Android ecosystem, it’s also possible to define shortcuts, or, in Android parlance, **routines.** For example, one such routine can ask Google Assistant to report the Weather Channel forecast for San Francisco whenever it hears the word *Weather*.

*A Google Assistant custom routine allows the user to get the weather in San Francisco whenever she says* weather *to Google Assistant.*

## Familiarity

Most users are not familiar with the tools available for microsession support — widgets, quick actions, Siri shortcuts, and Google Assistant routines don’t yet get widespread usage (the only notable exception is notifications). Yet, these actions can offer significant speedups for those users who know about them, and are thus an example of usability heuristic # 7: [flexibility and efficiency of use](https://www.nngroup.com/videos/flexibility-efficiency-use/). And more and more users will discover them accidentally — for example, long pressing an app has long been the gesture for rearranging apps on the screen in both iOS and Android. Because now long press also shows quick actions, people will uncover them while trying to clean up their screens, and thus they will eventually get used to them. Or, if apps advertise their Siri suggestions inside the app, users will notice them sooner or later and may take advantage of them.

Normally, if a design change or innovation will take a lot of money to implement but will only benefit a few of your users, we don’t recommend it. Its [ROI](https://www.nngroup.com/articles/usability-roi-declining-but-still-strong/) is likely too low. But unlike other fringe design innovations, **support for microsessions is easy to implement**. Take advantage of these features in order to improve the overall user experience.

## Conclusion

If your mobile users can quickly finish what they want to do in your app, it means that you’ve done a good job of designing it. You can save users even more time and effort by allowing them to circumvent the launching of the app through self-sufficient notifications and widgets or by providing them with external task entry points through quick actions and voice-assistant shortcuts or routines.

## References

D. Ferreira, J. Goncalves, V. Kostakos, L. Barkhuus, and A. K. Dey. 2014. Contextual experience sampling of mobile application micro-usage. *MobileHCI '14*. DOI: [https://doi.org/10.1145/2628363.2628367](https://doi.org/10.1145/2628363.2628367)

M. L. Gordon, L. Gatys, C. Guestrin, J. P. Bigham, A. Trister, and K. Patel. 2019. App Usage Predicts Cognitive Ability in Older Adults. *CHI '19*. DOI: [https://doi.org/10.1145/3290605.3300398](https://doi.org/10.1145/3290605.3300398)

iOS Human Interface Guidelines. [https://developer.apple.com/design/human-interface-guidelines/ios](https://developer.apple.com/design/human-interface-guidelines/ios)

Android Developers Guide. [https://developer.android.com/guide](https://developer.android.com/guide)
