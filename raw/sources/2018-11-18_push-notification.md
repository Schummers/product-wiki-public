---
title: "Five Mistakes in Designing Mobile Push Notifications"
date: "2018-11-18"
url: "https://www.nngroup.com/articles/push-notification/"
author: "Alita Kendrick"
topics: [mobile-and-tablet-design]
type: article
---

When properly executed, mobile push notifications can provide users with relevant information to encourage them to engage with an app. However, when poorly implemented, notifications can deter users from interacting and, in severe circumstances, can prompt them to delete an app altogether.

In 2016, the average mobile phone user received **56 notifications per day** according to a study from Telefonica Research in Spain [Pielot 2018]. Today, maybe more? For sure, notifications need to be designed properly, or they can be highly detrimental to the user experience, given this barrage of notifications.

[Notifications](https://www.nngroup.com/articles/indicators-validations-notifications/) are generally not triggered by the user’s immediate actions. Nonetheless, they announce an event that (supposedly) has some significance to the user. There are two main types of notifications: action-required and passive. Action-required notifications, as the label suggests, require the user to act upon the information received in the notification. Passive notifications are purely informational. Most push notifications are passive.

Do you ever feel the need to read an email as soon as you get it? When the message is important or time-sensitive, this behavior is beneficial. However, if the message is unimportant, you may feel bad because you became distracted and wasted time reading it. Push notifications can be disruptive for the same reason.

Notifications can happen in almost any type of user interface. For example, in Windows 10, they usually appear either as a “toast” that slides up from the taskbar for a short time or as a small icon in the dedicated notification area of the taskbar. In auditory interfaces, notifications can be especially disruptive, if the system started speaking when you least expect it. In this article, we’ll focus on notifications on mobile devices. Mobile notifications have the potential to be particularly useful (when used right) since many people carry their mobile device most of the time and thus will be informed about an important event no matter when it occurs.

In this article, we discuss 5 push-notification mistakes that mobile apps make frequently:

1. Asking users to enable notifications in the initial launch
2. Neglecting to tell users what information notifications will contain
3. Sending burst notifications
4. Sharing irrelevant content
5. Making it difficult to turn off notifications

## In This Article:

- [Mistake #1: Asking Users to Enable Notifications Immediately After Launching an App for the First Time](#toc-mistake-1-asking-users-to-enable-notifications-immediately-after-launching-an-app-for-the-first-time-1)
- [Mistake #2: Neglecting to Tell Users What Information Notifications Will Contain](#toc-mistake-2-neglecting-to-tell-users-what-information-notifications-will-contain-2)
- [Mistake #3: Sending Notifications in Bursts](#toc-mistake-3-sending-notifications-in-bursts-3)
- [Mistake #4: Sharing Irrelevant Content](#toc-mistake-4-sharing-irrelevant-content-4)
- [Mistake #5: Making it Difficult to Turn Off Notifications](#toc-mistake-5-making-it-difficult-to-turn-off-notifications-5)
- [Conclusion](#toc-conclusion-6)

## Mistake #1: Asking Users to Enable Notifications Immediately After Launching an App for the First Time

Users who have just downloaded your app do not necessarily have a clear understanding of the value the app will bring to them. At that point, the app has not yet gained their [trust](https://www.nngroup.com/articles/commitment-levels/), but it asks for permission to invade their screens. What will users get from the app’s notification?

This offense is so frequent that users barely read the message anymore. In many of our studies, the immediate response is to click *Don’t Allow*. Instead, apps should take advantage of the [reciprocity principle](https://www.nngroup.com/articles/reciprocity-principle/) and offer users some value first. **Allow them to experience the app** and only in a later session ask them to accept notifications.

**DON'T**

*FreePrints, an app for ordering photos, greets first-time users with a simple splash screen which transitions into a Getting Started page. Before users get a chance to read the copy on this page, they’re interrupted with a message asking them to allow notifications. FreePrints has neglected to inform users of what type of notifications they will receive and why they will find the content valuable.*

**DO**

The Conquest mobile game lets users experience the app before asking them to enable notifications. Game players complete multiple tasks to increase their stats and level up. Only after a player has leveled up for the first time does the game ask users to enable notifications.

## Mistake #2: Neglecting to Tell Users What Information Notifications Will Contain

Consider the generic messaging that iOS sends users: *X company would like to send you notifications*. This message focuses on what the company wants from users, but not on what the user will gain from the company. For some apps (such as social-media or news apps) users can make reasonable guesses on the sort of information they will see in notifications. On the other hand, it’s harder to guess the content of the notifications sent by a retail or an entertainment app. Details about the nature of your notifications can make users understand whether they need them and can increase the perceived credibility and trustworthiness of your app (after all, you’re being honest and transparent about your notifications, rather than trying to fool your users into accepting them).

**Tell people****what notifications will be about** to increase the chance that they will accept your request.

**DON'T**

*The Tasty app, which houses food videos and recipes, doesn’t provide users with an explanation of the information that will be in notifications. Users are stuck pondering why Tasty wants to send them notifications and whether it will be content that they want to see or not.*

**DO**

*Night Sky, an AR planetarium app explains what notifications will be about (stargazing conditions, object rise times, etc.). By providing this information before asking users to enable notifications, the app allows users to make an informed decision.*

## Mistake #3: Sending Notifications in Bursts

Has someone ever rung your doorbell repeatedly? This is the effect that burst notifications can have within an interface. Receiving many notifications in a short interval can overwhelm and irritate users, causing them to turn off notifications (or worse, delete your app). Not to mention, repeated notifications may appear sloppy and unprofessional, perhaps even [needy](https://www.nngroup.com/articles/needy-design-patterns/), leaving a lasting negative impression on your users.

Instead of filling your user’s screen with several notifications, **send fewer notifications in a meaningful way**. If you have more than five notifications that you need to send at once, combine them into a single message. Shift the focus to quality over quantity and you will be sure to see increased user satisfaction.

**DON'T**

*Wunderlist, a to-do–list app, sends notifications for every task that is due. Receiving reminders via notifications is helpful until it becomes overwhelming. If multiple items have the same due date, they will result in burst notifications.*

**DO**

*Instagram bundles notifications when several users like a photo that you’ve posted. In this case, rather than sending 11 separate notifications, Instagram sent one with the names of two users and a numeric count of the others. (Ideally, the two users named would be the ones of most salience to the user and not just the two most recent likes.)*

Note: iOS 12 makes it easier to deal with burst notifications by grouping all notifications from one app into a single stack. However, combing through 10 similar notifications is overwhelming at worst and boring at best. Don’t rely on the operating system to deal with burst notifications for you.

*iOS 12 groups all the notifications from a single app under the same alert (left); tapping a stack shows the list of all notifications from that app (right).*

## Mistake #4: Sharing Irrelevant Content

Any notification amounts to an interruption: it is meant to grab our attention and direct it to the notification. When the message is irrelevant to us, the interruption is irritating. Some people like to keep their inbox at zero unread messages, others like their phone’s lock screen clear of notifications. If you’re in the latter group, swiping away irrelevant notifications feels particularly time-consuming and bothersome.

Sending users notifications for every little thing that happens in your app is a big mistake. You don’t want to be the app that causes your users to roll their eyes any time a notification pops up on their screen. Nor should you justify this behavior by saying ‘Well, they can turn them off in settings.’ Instead, **provide relevant content** aimed to inform and engage.

**DON'T**

*Venmo, an app that allows you to send money to people you know, sends users notifications when any transaction (even ones that do not involve the primary user) occurs. The app has a feed which shows when your friends send others money. When using the app, this feature isn’t bothersome (may be a little strange, but it’s not disruptive). But notifications with this type of content are irrelevant because they do not pertain to the main user.*

**DO**

*Reddit sends users notifications when there is a trending post in a subreddit they follow. Notifications for popular posts within subreddits that users subscribed to are relevant and prompt users to open the app and explore further content.*

Ideally, apps should allow users more control over both the frequency and relevancy of notifications. Maybe people could specify the maximum number of notifications they would want in any given time period, or maybe they could require some minimum importance for events that triggered a notification. The latter feature is difficult to make usable, but it would be very useful in domains where it’s easy for users to specify importance. However, research shows that [most users don’t bother customizing their systems](https://www.nngroup.com/articles/customization-of-uis-and-products/), even when customization would help them substantially in the long run. Thus, allowing users to modify their preference settings are no excuse for pushing too many (or too unimportant) notifications to the many users who stick with the default settings.

## Mistake #5: Making it Difficult to Turn Off Notifications

There are many reasons why users decide to turn off notifications:

- They get too many notifications overall.
- Your content is less relevant or important to them than it once was.
- They find them distracting.

No matter the reason, you should never try to hide this functionality from your users. This practice is deceptive, decreases trust in the company and application, and provides users with all the more reason to delete your app.

Turning off app notifications should be straightforward and quick. **Allow users to edit their notification preferences within the app**, so they are not forced to go to their phone’s native settings. Additionally, place this functionality in the *Settings* section of your app to meet users’ expectations and ensure [findability](https://www.nngroup.com/articles/navigation-ia-tests/).

**DON'T**

*The Economic Times, an app focused on providing news related to the economy, does not allow users to change notification settings within the app despite some deceiving language. Within the hamburger menu, there are two places where users may reasonably expect to change their notification settings: Notifications Hub (left) and Settings (right). The Notifications Hub contains no information about changing notifications. The Settings page does not allow users to edit notification preferences either. To change notifications, users are forced to go to their phone’s global-notification settings.*

**DO**

*The brain training app, Elevate, allows users to edit their notification preferences within the app. Users can navigate to the Settings page (left), then select Push Notifications and navigate to a page where they can change the toggle state for any type of push notification (right).*

## Conclusion

Notifications are disruptive and [annoy](https://www.nngroup.com/articles/does-user-annoyance-matter/) users when they are irrelevant. Don’t risk inciting negative sentiment. Allow users to experience your app and understand its value proposition before asking permission to send push notifications. Tell them what type of notifications you will send. Ensure that users can easily find and edit your app’s notification settings. Avoid burst notifications and share content that is relevant to the user at hand.

For more on mobile notifications and related topics, read our report [UX for Mobile Applications and Websites](https://www.nngroup.com/reports/mobile-website-and-application-usability/).

### Reference

Martin Pielot, Amalia Vradi, and Souneil Park (2018): [Dismissed!: a detailed exploration of how mobile phone users handle push notifications](https://dl.acm.org/citation.cfm?doid=3229434.3229445), *Proceedings MobileHCI '18 Conference.*
