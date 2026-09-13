---
title: "User Control and Freedom (Usability Heuristic #3)"
date: "2020-11-29"
url: "https://www.nngroup.com/articles/user-control-and-freedom/"
author: "Maria Rosala"
topics: [heuristic-evaluation]
type: article
---

Jakob Nielsen’s third [usability heuristic](https://www.nngroup.com/articles/ten-usability-heuristics/) for user interface design is [user control and freedom](https://www.nngroup.com/videos/usability-heuristic-user-control-freedom/). This principle states:

> *Users often choose system functions by mistake and will need a clearly marked “emergency exit” to leave the unwanted state without having to go through an extended dialogue. Support undo and redo.*

Part of a great user experience is nurturing users’ feeling of control over the user interface (UI) they happen to be using. **Users should be able to quickly correct mistakes or backtrack on choices made**. The ability to easily get out of trouble encourages exploration, which facilitates learning and discovery of features. It also increases overall use and sales (in the case of exploring a product space). Conversely, when the UI doesn’t support these actions, users feel trapped and typically report dissatisfaction.

There are several UI controls that typically allow people to **go back to the previous state of the system**:

- A *Back* link which returns users to a previous page or screen
- A *Cancel* link which allows the user to quit a task or multi-step process
- A *Close* link which allows users to close a new view
- An *Undo* option (and a corresponding redo option) to allow users to backtrack on a change to a UI element

## In This Article:

- [Always Allow Users to Go Back a Step](#toc-always-allow-users-to-go-back-a-step-1)
- [Meet Users’ Expectations When Using a Back Link](#toc-meet-users-expectations-when-using-a-back-link-2)
- [Make Exit Links Easily Discoverable](#toc-make-exit-links-easily-discoverable-3)
- [Allow Users to Easily Cancel an Action](#toc-allow-users-to-easily-cancel-an-action-4)
- [Support Undo](#toc-support-undo-5)
- [Ensure Undo Is Discoverable](#toc-ensure-undo-is-discoverable-6)
- [Conclusion](#toc-conclusion-7)

## Always Allow Users to Go Back a Step

Whenever users click a link to open a new page, screen or view, they should always be able to go back to where they came from. On the web, users rely on the browser’s *Back* button to navigate to the previous page in usability testing, we often see some users defaulting to the browser’s *Back* button when navigating a website, rather than using the website’s own navigation (such as breadcrumbs). This is one of the reasons why we recommend [not to open links in new tabs indiscriminately](https://www.nngroup.com/articles/new-browser-windows-and-tabs/) because some users don’t notice they are in a new tab and struggle to go back.

**Never stop users from leaving your site by disabling the browser Back button.** Some sites deliberately make their site sticky, preventing users from returning to the search engine. While users will stick around on your site for a few seconds longer if you use this tactic (because they can’t leave), you’ll quickly frustrate them — and good luck getting them to do business with you! This design choice is often the result of prioritizing [vanity metrics](https://www.nngroup.com/articles/vanity-metrics/) over tangible UX goals. Instead of trapping users by disabling the *Back* button, sites should offer users valuable content to make them want to stay.

Nonfunctioning browser *Back* buttons can also be found on some online forms, because moving backward could break the underlying logic. In some cases, users can use the browser *Back* button but instead of returning to the previous screen, they receive a timeout message and lose their work. Where possible, **build forms where users can use the browser's Back button**. If the design makes this impossible, warn users when they click the browser’s *Back* button and provide them with a chance to cancel this action. Designers should also explore creating a *Back* link or a clickable progress bar that help users move back through the form without losing work.

![Four screenshots from Delta's mobile app are displayed. The first screen shows several available flights for a search from Detroit to Honolulu. The second screen shows one flight has been selected. There is a back button at the top of the screen. When the back button is pressed, a overlay message is displayed (shown on screen 3) which asks the user if they want to continue booking or search for a new flight. Selecting search for a new flight takes the user back to the beginning where they have to enter their search criteria, rather than to the previous list of all available flights.](https://media.nngroup.com/media/editor/2020/11/20/delta_mobile_horizontal_resized.png)

*On Delta’s app, once a flight is selected, there’s no way for the user to move back to the list of the flights without having to begin the search all over again. In this case, the* Back *link doesn’t function as expected, because it doesn’t allow the user to move one-step backward. Instead, the* Back *link functions as a ‘cancel’ link. Slapping people like that makes them hesitant to explore potential flights and, thus, likely reduces sales.*

![Two screenshots from Delta's mobile app are displayed. On the first screen, the user has a selected a flight to view. When the back button is pressed, an overlay message is displayed (shown on screen 2) which asks the user if they want to continue booking this flight by staying on the page or whether they'd like to search for a new flight.](https://media.nngroup.com/media/editor/2020/11/11/delta_app_mobile_version.png)

*On Delta’s app, once a flight is selected, there’s no way for the user to move back to the list of the flights without having to begin the search all over again. In this case, the* Back *link doesn’t function as expected, because it doesn’t allow the user to move one-step backward. Instead, the* Back *link functions as a ‘cancel’ link. Slapping people like that makes them hesitant to explore potential flights and, thus, likely reduces sales.*

## Meet Users’ Expectations When Using a Back Link

When presented with an [overlay or lightbox](https://www.nngroup.com/articles/overuse-of-overlays/), users often get disoriented and think they are on a new page — especially where overlays take up the whole screen. Therefore, to return to the previous screen, users often use the browser’s *Back* button instead of tapping a *Close* link or *X* icon. This action has the effect of taking the user back two steps, rather than one, causing confusion and disorientation.

In a recent mobile usability-testing session, a participant used the browser’s *Back* button on a full-screen overlay and was taken out of the overlay *and* out of the page he intended to return to. The participant commented, “I don't expect to be taken out of that page (…) If I click Back, it brings me out of the page I was on. It doesn't bring me back to the page that I popped out from.”

When it’s possible that users mistake the overlay for a new screen — whether on desktop or mobile — **ensure the Back button has the same effect as a Close link**.

![A gif shows Asos.com, a clothing retailer. When a user selects a pair of shoes from the product listings page, and selects a link from within that page to view shipping information, a fullscreen overlay appears. Using the browser's back button (rather than the close icon) takes the user back to the product listings, rather than to the product overview page for the pair of shoes the user selected.](https://media.nngroup.com/media/editor/2020/11/20/asos_back.gif)

*On ASOS.com, when a user selects the* Free Shipping & Returns *link, a full-screen overlay appears. Tapping the browser’s Back button returns the user to the product listings, rather than the product-overview page.*

![Two screenshots from Wayfair.com are presented. A product overview page for an armchair is shown on screen 1. Underneath the product's title is the average rating (4.5) and a link to read the reviews. Clicking on the link opens up a drawer which fills the full screen. A back link appears at the top of the page to take the user back to the screen they were looking at before clicking the reviews link.](https://media.nngroup.com/media/editor/2020/11/20/wayfair_compressed.png)

*On Wayfair.com, clicking on the* Reviews *link opens a drawer which expands to take up the full screen. Both Back buttons (the site’s and browser’s) take users to the initial product overview page, which is what users expect. The user can also swipe from left to right to close the drawer.*

In mobile apps, users tend to transfer their knowledge of the *Back* button from their experience with the web and have the same expectation for it: that is a way to move back a step (from whichever direction the user came). Unfortunately, often designers mean it as a way of moving up in the application’s IA. As a result, users can easily get disoriented. In the example below, a user can swipe right to left to read another news story in BBC News’ app (the order corresponds to the way they’re listed vertically on the news listing page). However, users can’t use the *Back* button to return to a story they visited by swiping; using the *Back* button returns users one step up in the IA to the article-listings page, rather than to the previous article they visited.

![A gif of the BBC News app shows a user clicking on a story from the main page and then swiping from right to left to move through stories. When the user selects the back button in the app, they are returned to the main page where all stories were listed.](https://media.nngroup.com/media/editor/2020/11/20/bbc_app_compressed.gif)

*After users click on a news story on the BBC News app, they can swipe through other articles in the list. The Back button takes the user one step up in the IA (back to the listing page), rather than to the article the user previously visited.*

## Make Exit Links Easily Discoverable

Like in a physical space, **exits should be easy to find and well signposted** so that they will be discovered when needed.

Follow [design standards](https://www.nngroup.com/videos/usability-heuristic-consistency-standards/) when positioning *Close*, *Exit* or *Cancel* signs, so that users can easily find them where they typically expect them. For example, on a lightbox overlay, users typically expect an ‘X’ icon in the top right corner of the overlay.

![An image of an article on Harper's Bazaar's website. On top of the article appears a modal overlay. The close link appears outside of the modal overlay and is easily missed because it lacks contrast to the background, which is the article's image.](https://media.nngroup.com/media/editor/2020/11/20/harpers_bazaar_compressed.jpg)

*On Harper’s Bazaar’s website, a popup invites the user to consider a subscription. The* Close *link appears in the bottom left corner outside of the overlay. This unusual placement, together with the poor contrast to the background , makes it difficult to see.*

In addition to placing *Exit* signs in expected places, use [universal icons](https://www.nngroup.com/articles/icon-usability/) so users understand what the link does. [Accompany icons with text labels](https://www.nngroup.com/articles/icon-usability/) or substitute icons with plain text. For example, use *Back* instead of < and *Close* instead of *X*.

## Allow Users to Easily Cancel an Action

Whether a user is beginning a purchase, a transfer of money, or a large download, she should be able to cancel that task at any point. The *Cancel* option should be easy to find and quick to execute. Even though in multistep processes users could make use of *Back* links in the place of *Cancel*, it’s best to provide a *Cancel* link to avoid unnecessary clicks.

![A screenshot of a user beginning to compose a tweet on Twitter. The cancel link has been tapped which generates a dialogue asking the user whether they'd like to delete the draft or save it. Another cancel link appears to allow the user to undo the action.](https://media.nngroup.com/media/editor/2020/11/20/twitter_cancel_compressed.jpg)

*When users begin to compose a tweet, they can easily cancel the task by selecting* Cancel *at the top left of the screen. Upon doing so, Twitter presents the user with the option to delete the message or save a draft. This choice ensures users don’t accidentally lose work.*

On mobile, some designers try to save space by using the *X* icon, instead of *Cancel*. Unfortunately, sometimes [X can be mistaken for Close , rather than Cancel](https://www.nngroup.com/articles/cancel-vs-close/). In some interfaces, it’s important to distinguish the difference between the two to avoid user error. If *X* means *Close**and**cancel*, then use an explicit text label (*Cancel)* or provide the user with a warning dialogue to avoid losing users’ work.

![A screenshot from the Wealthfront app (a finance app) is shown. The user has begun a multi-step process to transfer money from an investment account to a current account. The user is provided the option to finalize the transfer, cancel the transfer through an 'X' icon and go back a step in the transfer process by clicking on a back arrow icon.](https://media.nngroup.com/media/editor/2020/11/20/wealthfront_compressed.jpg)

*When transferring money from an investment account in Wealthfront’s app, users follow several steps on sequential screens. At the top of the screen, users can either go back a step using the arrow or select* X *to cancel the transfer. However, it’s not completely clear whether pressing* X *will save the transfer arguments or cancel the transfer completely. In this case, it cancels the transfer entirely, so a* Cancel *label would have been better.*

## Support Undo

When a user makes a change to the status of a system, he should be able to easily undo that. Imagine accidentally deleting a whole paragraph of text and not being able to get it back!

*Undo* can be supported in many ways on an interface, not just through a simple *Undo* button. For example, if users add an item mistakenly to a shopping basket, they should be able to undo that change by removing the item.

![An image of the shopping basket from the CVS pharmacy website. Some allergy relief eye drops have been added to the basket. A remove link appears below the item to allow the user to remove the item from the basket.](https://media.nngroup.com/media/editor/2020/11/11/cvs_checkout.png)

*On an ecommerce site, like in the example above from CVS, a user can undo adding an item to the basket, by selecting* Remove *.*

![A screenshot of the iOS notification settings for the BBC News app. The user is given the option to toggle notifications and sounds on or off, and also select and deselect how notifications appear (for example, on a locked screen, in the notification center or in banners).](https://media.nngroup.com/media/editor/2020/11/20/ios_notification_settings_compressed.jpeg)

*When changing notification settings, a user can undo a change by using the toggles and checkboxes.*

![An interactive floorplan is shown from Mattamy's site. The user has made some changes to the floorplan by selecting additions from a panel that appears on the left of the page. On the right of the floorplan itself, several icons are shown with no labels. One icon is a backward facing arrow which has been highlighted in this image by the author.](https://media.nngroup.com/media/editor/2020/11/20/mattamy_floorplan_compressed.jpg)

*Mattamy, a home builder, provides interactive floor plans on its website, giving users a way to explore several possible structural changes. In order to undo edits, users uncheck structural changes from the left pane. Unfortunately, the* Reset *button (highlighted) can easily be mistaken for an undo button.*

**If users are likely to make many actions in short succession, support multiple Undo and Redo**. Undoing the last action is often not enough. For desktop users, it’s also a good idea to support [standard keyboard shortcuts for power users](https://www.nngroup.com/articles/flexibility-efficiency-heuristic/).

## Ensure Undo Is Discoverable

Remember the [shake-to-undo feature in iOS](https://www.nngroup.com/articles/ios-7/)? This feature is notoriously underused because it is so hard to discover.

For desktop designs, don’t assume your users will know that they can use a keyboard shortcut. It’s a good idea to give users a visible option to undo an action on the UI. This feature should be where users typically expect it. In WYSIWYG (What-You-See-Is-What-You-Get) applications like word processors and design software, *Undo* is usually in the toolbar or in the app’s menus. On web-based applications with no [chrome](https://www.nngroup.com/articles/browser-and-gui-chrome/), an *Undo* option is often contextual — it may appear in a transient snackbar or in a [contextual menu](https://www.nngroup.com/articles/contextual-menus/).

![An image of Microsoft Word's toolbar. The edit menu category has been opened and the Undo Typing menu item has been selected. Alongside the menu items prompts to the user appears to show them that it's possible to activate this command by using keyboard shortcuts.](https://media.nngroup.com/media/editor/2020/11/20/microsoft_word_toolbar_compressed.jpg)

*In Microsoft Word – like in many other WYSIWYG applications – users can find* Undo *and* Redo *options from within the* Edit *menu. Users are also shown keyboard shortcuts for those actions.*

If an *Undo* option is contextual, ensure it has good visibility in the UI. On Google Drive, when a user makes a change to a file, a snackbar appears in the bottom left corner of the window to confirm the change has been made and to provide an option to undo. Unfortunately, the message only appears for a few seconds. Users would need to know they want to undo and act quickly in order to make use of this feature. (It’s also possible to use keyboard shortcuts, but these are not listed in the UI.)

![An image of the content of a Google Drive folder. Two documents are contained in this folder and a notification appears below to tell the user that a document has been successfully renamed. In this notification is a link to undo the action.](https://media.nngroup.com/media/editor/2020/11/11/google_drive.png)

*In Google Drive, an* Undo *option is available only when the user has taken an action. It appears as a snackbar at the bottom of the screen after the action has been completed but disappears after a few seconds.*

## Conclusion

To ensure users have a sense of freedom and control using your product, they should be able to easily abandon a task, go back a step, and undo a change they’ve made to the system’s state. By thinking about carefully crafting clear exit points and *Undo* features, you can leave users feeling in control of the experience, rather than at the mercy of your design.
