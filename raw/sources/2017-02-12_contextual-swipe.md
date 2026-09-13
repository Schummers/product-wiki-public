---
title: "Using Swipe to Trigger Contextual Actions"
date: "2017-02-12"
url: "https://www.nngroup.com/articles/contextual-swipe/"
author: "Angie Li"
topics: [interaction-design, mobile-and-tablet-design]
type: article
---

While many touch gestures still get limited use in most mobile apps, one that has become fairly widely adopted is the swipe-to-delete, which simply involves dragging the finger across an item, in a gesture that resembles the physical action of crossing off a list item with a pen.

Initially introduced by Apple in the iOS Mail app, today many apps use it not only to remove an item from a list, but also to expose an entire set of contextual actions[.]()

While in the early iPhone years, this gesture was unfamiliar to the users, nowadays it’s so widely spread that many iOS and even Android users have learned it and use it frequently. Applications have embraced it as a convenient way to prioritize content and eliminate some [visible chrome](https://www.nngroup.com/articles/browser-and-gui-chrome/) from the small mobile screen, and also to keep actions in line with the content that they affect. Yet, **contextual swipe** (the name we will use in this article for swipe-to-delete and its many relatives that trigger contextual actions) has questionable usability in many of its implementations.

*In the iOS Reminders app, swiping towards the left on an item revealed the* More *and* Delete *buttons. Swiping right without choosing an action kept the item in the list.*

**Disadvantages of Contextual Swipe**

Despite the growing number of applications that use this gesture, there are several reasons to take caution with contextual-swipe designs:

1. **Lack of signifiers** makes it unclear where the contextual swipe can be used. (This is a general problem for gesture-based interactions.) Although many users have become familiar with the gesture, some are still not used to it. And even those who have learned it may occasionally forget to perform it in the absence of any visible cues. A complicating factor is that not all applications support this gesture, which [slows down users’ learning](https://www.nngroup.com/articles/power-law-learning/). When encountering new apps or revisiting infrequently used apps, users will have difficulty to predict if they can use contextual swipe. For example, the Key Ring app for iPhone (an app for storing digitized loyalty cards) did nothing when an item was swiped, although widespread use of this technique may suggest otherwise.

*Swipe-to-delete was not available in the Key Ring app. In order to delete a card, the item had to be opened to reveal a detailed view.*

1. **Content is obscured** when the user swipes to reveal actions. Although swiping is useful for keeping the actions close to the content they affect, swiping to reveal the menu often obscures the content beyond recognition. In the YouTube app, users had to swipe left to unsubscribe from a channel. However, swiping obscured the name of the channel and made it difficult to confirm that the right channel had been selected before taking action. Users wanting to avoid mistakes would need swipe right to reveal the full name of the channel before continuing.

*In the iOS YouTube app swiping left on a channel revealed an* Unsubscribe *button, but also obscured the name of the channel that the user could unsubscribe from.*

1. **Some of the actions associated with contextual swipe are nonstandard.** Because swipe was originally used to delete an item from a list, most users who have learned the gesture expect it to reveal some destructive actions. While many implementations do associate such actions with swipe (e.g., unsubscribe in the YouTube app), others reveal completely unexpected options. For instance, in the Spotify app, swiping left on a song that was not part of the user’s library revealed an option to save the song. (Pretty much the opposite action of deleting it.) This nonstandard behavior is problematic because users would not think to attempt swipe if they wanted to add a song to their library, since saving is not a destructive action. 

Some applications associate a plethora of actions with the swipe, delete included. Remember, most users won’t discover these actions (or they will discover them only accidentally when they attempt to delete the item).

 In the example below, B&H Photo app used swipe gestures to reveal multiple actions associated with the items in the shopping cart — not only *Remove* from cart, but also *Save for Later, Savings,* and *Accessories*.

*In the B&H Photo app several actions were nested behind a swiping gesture. Keeping too many actions from view not only made it more difficult to see the affected content, but also made these features less discoverable.*

1. **Contextual swipe is sometimes used inconsistently within the same app.** Some apps expose different types of actions depending on either:

- the direction of the swipe (e.g., swipe left means something else than swipe right)
- the state of the item being swiped

For example, in Spotify, swiping could have 3 meanings:

- Swiping left on a song that was not part of the user’s library revealed a *Save* option (as discussed before).
- Swiping left on a song in the user’s library revealed a *Remove* option.
- Swiping right on a song revealed an option to add the song to a queue of music that was being played.

When multiple actions are associated with the same gesture, it becomes harder for people to learn and remember them. (This is an instance of what psychologists call *the fan effect —* when a cue is associated with many items, it’s harder to retrieve any of those items.)

*Spotify app for iPhone: the contextual swipe revealed multiple actions: swiping left on a song revealed a button to save the song to your personal music library. If the song was already in the library, then the identical gesture would cause a button for removing the song to be shown instead.*

1. **Poorly implemented swipe-to-delete can lead to loss of data**. Swipe is a fairly easy-to-perform gesture, and every now and then people will accidentally [remove an item unintendedly](https://www.nngroup.com/articles/slips/). To prevent such accidents, it’s important to always ask for confirmation or provide an easy way to undo the swipe.

*Overcast app for iPhone: swiping alone would not delete a podcast. In order to remove a podcast, the* Delete *button needed to be selected, which prevented users from accidentally deleting items*

1. **Swipe ambiguity can affect how effective contextual swipe is.** To make matters worse, some apps use horizontal swipe gestures not only for destructive actions, but also to navigate across different sections of the app. In many iOS apps, the horizontal swipe is used to go back to a previous page, and in Android it is sometimes used to reveal a hidden menu. Plus, on the iPad, horizontal swipe can be used to split the screen into multiple windows. 

All these gestures can affect the usability of contextual swipe. Imagine that you were trying to open up another application and accidentally deleted an important work email. Or, vice versa, imagine that you wanted to remove an item from a list and unintendedly triggered a split view.

*iPad Pro: The Mail and Photos apps appeared in split-view mode on the screen at the same time. Swiping right on an email message in could mark the message as read or could close the panel containing the Mail app, depending on how close to the edge of this panel the swipe was executed.*

Even if users can easily recover from such incidents, the overall user experience degrades as the user feels less in control over the interface.

## In This Article:

- [Recommendations for Using Contextual Swipe](#toc-recommendations-for-using-contextual-swipe-1)
- [Conclusion](#toc-conclusion-2)

## Recommendations for Using Contextual Swipe

- **Maximize content visibility** and make sure that users know the item that they are deleting or acting upon. Contextual actions should be in view of the content it affects. Keep content in view anytime the contextual swipe is used in order to minimize uncertainty.

*Notability for iPhone (left): a contextual swipe kept the name of each ‘note’ aligned with the app border, allowing users to see what they were deleting. Wunderlist (right): The list title shifted off screen when users performed a contextual swipe, preventing them from checking the name of the list before acting on it.*

- **Ask for confirmation** before completing a destructive action. Using contextual swipe to remove an item without confirmation can be problematic. Prevent mistakes and avoid errors by asking for confirmation with something as simple as a delete button.
- Alternatively, if the action is highly repetitive and asking for confirmations would be tedious, **support easy undo.** Make sure that the undo option is highly salient on the screen, so people won’t have to look for it. In the YouTube app, after unsubscribing from a channel, users were provided the chance to undo or re-subscribe right away.

*After unsubscribing from a channel in the YouTube app there were multiple options to undo the action and re-subscribe.*

- **Limit contextual swipe to destructive actions.** Burying key actions behind a contextual swipe prevents users from discovering them. Most users expect to use contextual swipe to find destructive actions, such as *Delete* and *Remove*: not only was this the original use of the gesture (and thus the best known), there’s also a bit of a metaphorical relation between the gesture to swipe something off the screen and the command to delete that object.
- **Keep the behavior of contextual swipe consistent** within an application. People have difficulty learning multiple meanings for the same gesture and they will not expect swipe to do different things on different pages of your app. Avoid using actions that are dependent on the state of an item or of the location within the app; instead, keep the meaning of contextual swipe consistent because [overloaded commands](https://www.nngroup.com/articles/overloaded-vs-generic-commands/) tend to be confusing.
- **Do not overuse swipe gestures in your app.** If your app uses contextual swipe, make sure it won’t interfere with other uses of swipe in your app (such as swipe to navigate from one page to another).

## Conclusion

Contextual swipe is popular in app development, but when used incorrectly it can cause confusion. Take caution when using it as a primary method of providing actions for content. Although more and more users have learned to associate swipe with delete, some apps still do not use it, while others use inconsistently or in nonstandard ways. Moreover, the swipe gesture can obscure the item, and thus either increase [user mistakes](https://www.nngroup.com/articles/user-mistakes/), or force people to work harder to reassure themselves that they selected the right item.
