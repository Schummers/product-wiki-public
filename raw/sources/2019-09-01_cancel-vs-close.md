---
title: "Cancel vs Close: Design to Distinguish the Difference"
date: "2019-09-01"
url: "https://www.nngroup.com/articles/cancel-vs-close/"
author: "Aurora Harley"
topics: [design-patterns, web-usability]
type: article
---

Long ago, the symbol *X*meant “this is where the treasure is buried.” In today’s digital interfaces, *X* no longer marks the spot, but rather functions as a way for users to cancel a process or to dismiss an interim screen. How can one tell for sure whether the *X*means *cancel* or *close*? Sometimes, unfortunately, you can’t.

The main issue lies with the common [lack of a text label](https://www.nngroup.com/videos/icon-text-labels/) for the *X* icon. When an icon represents multiple meanings in similar contexts across different interfaces, [icon usability](https://www.nngroup.com/articles/icon-usability/) suffers because users cannot rely on any single interpretation.

## In This Article:

- [Avoid Losing Users’ Work](#toc-avoid-losing-users-work-1)
- [1. Ask for Confirmation](#toc-1-ask-for-confirmation-2)
- [2. Use Explicit Labels](#toc-2-use-explicit-labels-3)
- [3. Favor Close & Save](#toc-3-favor-close-save-4)
- [Conclusion](#toc-conclusion-5)

## Avoid Losing Users’ Work

When users intend to dismiss a modal or view by clicking the *X* button, but the system instead completely cancels the process and clears all their work, it is disheartening at best, and maddening at worst. Yes, the *X* icon is commonly recognized by users to mean either to *cancel* or to *close*, but **distinguishing between the two possibilities is critical for the success of the interaction**.

In some cases, the distinction between cancel and close doesn’t matter. When a popup takes over the majority of your screen, hitting the *X* button (as quickly as humanly possible) serves to both close that [modal](https://www.nngroup.com/articles/modal-nonmodal-dialog/) and perhaps cancel any process it might have triggered. However, if a screen contains a running timer, is playing audio, holds several selected filter options, or contains some other type of unsaved work, it becomes much more important to correctly interpret what that *X* icon represents — you may intend to leave that timer or audio running, apply those selected filters, or save your in-progress work, while wanting to close that view to continue some other related activity.

For example, the Sephora checkout process used a modal window to present free samples that users could add to their cart. In the following example, an item had just been selected by clicking the *Add* button below it; that action caused the *Add* button to be replaced by a *Remove* link, which made it look as if the sample had already been added to the cart. However, when the user closed the modal by clicking the *X* icon rather than *Done* link, she discovered that the item was not in the cart and that she needed to add it again.

![Sephora website: Screenshot of Choose a trial product modal window](https://media.nngroup.com/media/editor/2019/08/28/sephora-actionsnotsubmitted_xascancel.jpg)

*Sephora: Even though it looked as if the sample had already been added to the cart because it could now be removed, closing the modal (by clicking the* X *in the top right corner) canceled the process of choosing a trial item. To add the item to their carts, users had to first click* Add *and then apply that action by clicking the* Done *link.*

**To avoid losing users’ work, systems need to determine the user’s intent — cancel or close — and provide clear options.**

This goal can be accomplished by one or more of the following:

1. Asking the user to confirm their intention
2. Using explicit text labels rather than ambiguous icons
3. Presenting two distinct buttons: *X* for closing the view (with the side effect of saving intermediate work) and *Cancel* for abandoning the process

## 1. Ask for Confirmation

If a user pressed the *X* icon on a modal or intermediate view where she had already performed an action, the UI could confirm her intention by directly asking whether to apply that action before closing the view. ** This solution is ideal for destructive cancel actions** that would lose the user’s work. Here, the old adage that it’s better to beg forgiveness than ask for permission is absolutely not true — always ask for [confirmation before committing destructive actions](https://www.nngroup.com/articles/confirmation-dialog/).

For example, filter views are often accidentally closed, and that action causes users to lose their work. This problem is particularly rampant on mobile interfaces, as filter screens often consume the majority — if not all — of the available screen space, making it difficult or impossible to tell whether selections have already been applied.

To [guard against potential mistakes](https://www.nngroup.com/articles/user-mistakes/), ask users who close a filter view whether they intend to apply the filters and close the view or clear their selections. For instance, the Lowes mobile app showed a confirmation dialog when the user attempted to close the filter screen before applying her selections.

![Lowes mobile app: 2 screenshots of filter screen and confirmation dialog](https://media.nngroup.com/media/editor/2019/08/28/lowes_mobileapp-filter-confirmationdialog.png)

*Lowes mobile app: Tapping either the* X *button or the* Back *arrow could reset any selections and take the user back to the previous result set. Right: After tapping* X *, a confirmation dialog appeared to check whether the user meant to apply or cancel the filter refinements before returning to the results list.*

Similarly, the language-learning app Duolingo showed a confirmation dialog when users attempted to close an in-progress lesson — lessons could not be left partially completed and had to be either finished or cancelled. At least, the app communicated this constraint to users and gave them the option to return to the lesson to maintain progress.

![Duolingo mobile app: Confirmation dialog before leaving lesson](https://media.nngroup.com/media/editor/2019/08/28/duolingo-confirmationdialog.png)

*Duolingo: Clicking the* X *button would end the current lesson and forfeit any progress. To guard against mistakes, the app included a confirmation dialog.*

While confirmation dialogs are effective in disambiguating the meaning of the *X*icon, they add extra steps; moreover, users don’t know what the *X* does before they press it and, therefore, they may worry about the consequence of their action.

## 2. Use Explicit Labels

Rather than relying on confirmation dialogs to catch users before they unwittingly lose all their selections, you can **eliminate the ambiguous X icon in favor of explicit text-labeled buttons**. Text can reduce ambiguity and clearly communicate what action would occur: *cancel* versus *close*.

The filter screen of Yelp’s mobile app offered buttons labeled *Cancel* and *Reset* at the top of the screen and a single large *Apply* button at the bottom. Similarly, the filter view in the Etsy mobile app provided separate buttons labeled *Clear* and *Done*. (Note: Etsy used *Done* rather than *Apply* because the filters were applied as soon as they had been selected, [as is recommended for toggle switches](https://www.nngroup.com/articles/toggle-switch-guidelines/).)

![Screenshots of Yelp mobile app and Etsy mobile app filter screens](https://media.nngroup.com/media/editor/2019/08/28/yelp_etsy-nox-cleartextlabels.png)

*(Left) Yelp mobile app: Text labels for* Cancel *,*Reset*, and *Apply* were direct and clear, making it less likely that users would inadvertently close the view and lose their filter selections. (Right) Etsy mobile app: The text label *Clear* gave a clear way (pardon the pun) for users to cancel their selections. The *Done* link returned to the product-listings page, with the selections already applied.*

## 3. Favor Close & Save

If the *X* icon must be used rather than text (to save space or because you’re following your organization’s [style guide](https://www.nngroup.com/articles/front-end-style-guides/)), err on the side of caution and ** save any intermediate work ** that has been done. In addition, provide a separate *Cancel* button, to give users an [emergency exit out of the process](https://www.nngroup.com/videos/usability-heuristic-user-control-freedom/) and to disambiguate between the two possible meanings of the *X*(closing and cancelling).

For example, Gmail automatically saved a draft of a message composed in its [nonmodal window](https://www.nngroup.com/articles/modal-nonmodal-dialog/). This practice allowed users to collapse or close the window when desired, while still saving their progress. Hovering over the *X* icon in the top right corner of the message window displayed a tooltip confirming that the draft was going to be saved and closed. Cancelling was also still available (using the *Delete* trash can icon at the bottom of the message window — far from the *Save & close* option at the top to help prevent mistakes).

![Gmail site: Screenshot showing tooltip for X icon within compose nonmodal window](https://media.nngroup.com/media/editor/2019/08/28/gmail-composemessage-saveandclosetooltip.jpg)

*Gmail: Hover revealed that the* X *icon was for dismissing the window and not for deleting the draft, allowing users to* Save & close *the message window without losing work in progress.*

Saving by default can also be a **good solution for long processes or processes that tend to be run in the background,** such as timers. For instance, the Glow Baby mobile app allowed users to browse other areas of the app while a feeding or sleeping timer ran in the background. Because these timers can run for a long period of time (hopefully, a very long time for the sleeping timer!), this functionality let the user accomplish other tasks in the app, like recording a past diaper change or browsing through articles and forums. Tapping the *X* icon in the timer view simply dismissed the window without canceling the running timer.

![Glow Baby mobile app: 3 screenshots of nursing timer either getting auto saved or presenting a confirmation dialog](https://media.nngroup.com/media/editor/2019/08/28/glowbabyapp-xasdismissbutsave.png)

*Glow Baby: (Left) Tapping the* X *icon in a running-timer view dismissed the view without canceling the timer, and thus, allowed the user to continue using the app to log other types of events, participate in the community discussions, read articles, and so on. (Middle) The status for the running timer was displayed in a banner at the top of the screen. (Right) Hitting the* X *while the timer was paused brought up the* Discard *or* Cancel *buttons to detect the user’s intention.*

Note that saving intermediate work or maintaining an ongoing process before closing is proactive, but sometimes can be contrary to the user’s intention: If users intend to cancel their selections by clicking the *X* button, auto applying those selections could be confusing and frustrating. This is why it’s critical to also include a separate *Cancel* button, to give users an out rather than forcing them to only save and close the view.

## Conclusion

While the *X* icon is ambiguous and can often cause usability problems, it’s unlikely that it will disappear from all interfaces any time soon. Designers should be aware of the multiple meanings of the *X* icon and disambiguate between *close* and *cancel*, as well as provide safeguards such as confirmation dialogs or autosaving to avoid losing any users’ work.

**Remember, when in doubt, save , then out.**
