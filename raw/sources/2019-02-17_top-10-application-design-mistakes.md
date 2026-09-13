---
title: "Top 10 Application-Design Mistakes"
date: "2019-02-17"
url: "https://www.nngroup.com/articles/top-10-application-design-mistakes/"
author: "Jakob Nielsen, Page Laubheimer"
topics: [applications, interaction-design]
type: article
---

Designing complex applications is a challenging undertaking. Building applications that have both the depth to support complicated tasks *and* the intuitiveness to make it clear *how* to get that work done is a tremendous challenge. We spend a full day on this topic in our [Application Design for Web and Desktop](https://www.nngroup.com/courses/application-ux/) course, but we could easily spend a month to catalogue every type of problem we’ve encountered in our user-research studies.

Making general recommendations about common application-design problems is difficult, because so many of the problems we observe are domain-specific. This was true 11 years ago, when the [first version of this article](https://www.nngroup.com/articles/top-10-application-design-mistakes-2008/) was written, and remains so today.

Thus, **our first recommendation is to do user research****with your target audience**:

- Begin with task analysis and [field studies](https://www.nngroup.com/videos/contextual-inquiry/) to understand your users’ needs and workflows.
- [Prototype](https://www.nngroup.com/courses/wireframing-and-prototyping/) and [test](https://www.nngroup.com/courses/usability-testing/) low-fidelity ideas to rough out the essential structure of your app and its features, without committing many resources towards ideas that you will [revise or abandon](https://www.nngroup.com/articles/no-validate-in-ux/) as you learn from your users.
- [Design iteratively](https://www.nngroup.com/videos/observe-test-iterate-and-learn-don-norman/), and test each change with a [small number of users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/). The more iterations, the better your application will be.

Despite the domain-specific nature of most app usability problems, here are 10 common mistakes that we frequently see across industries. Five of these issues (#1, 2, 3, 4, and 6) were also included in the original article —which goes to show how [durable](https://www.nngroup.com/articles/durability-of-usability-guidelines/) usability guidelines are. All 10 of the original guidelines are still true, but 5 mistakes are (thankfully) less commonplace than they once were; they were replaced by another 5 problems (#5, 7, 8, 9, and 10).

Here is our current list of the top 10 application-design mistakes that are both egregious and commonplace. Let’s hope that when we write then next version of this article in another 11 years, most of these will be far less common.

## In This Article:

- [1. Poor Feedback](#toc-1-poor-feedback-1)
- [2. Inconsistency](#toc-2-inconsistency-2)
- [3. Bad Error Messages](#toc-3-bad-error-messages-3)
- [4. No Default Values](#toc-4-no-default-values-4)
- [5. Unlabeled icons](#toc-5-unlabeled-icons-5)
- [6. Hard-to-Acquire Targets](#toc-6-hard-to-acquire-targets-6)
- [7. Overuse of Modals](#toc-7-overuse-of-modals-7)
- [8. Meaningless Information](#toc-8-meaningless-information-8)
- [9. Junk-Drawer Menus](#toc-9-junk-drawer-menus-9)
- [10. Proximity of Destructive and Confirmation Actions](#toc-10-proximity-of-destructive-and-confirmation-actions-10)
- [Summary](#toc-summary-11)

## 1. Poor Feedback

One of the most basic guidelines for improving an application’s usability is to provide clear [feedback](https://www.nngroup.com/articles/indicators-validations-notifications/):

- Show users the system's current [state](https://www.nngroup.com/articles/visibility-system-status/).
- Tell users how their commands and actions have been interpreted.
- Tell users what's happening.

Apps that keep quiet leave users guessing. Often, they guess wrong.

Good feedback tells users a lot of things — for example, has the button they clicked been correctly interpreted by the system as a “click” and will the system now do something? What is currently selected or active?

One of the scenarios where feedback becomes important is when the application is put into an edit mode to modify existing information. It’s important that users have a clear understanding of what is currently editable, as applications will differ in the scope of the edit mode — for example, some applications will incorporate tables of data where a single cell or row is editable, others will make the entire table editable. Proper, clear feedback can convey to users the scope of the edit; good feedback can be implemented in a variety of ways, from using a different background to identify the current editable area to changing the buttons associated with editing to clearly show their function

![A table of data with a clear indication that a single row is editable](https://media.nngroup.com/media/editor/2019/01/17/edit-mode-feedback.png)

*In the edit mode, this application from Telerik.com adds a grey background to the table row that’s currently editable, changes the cells so that they look like form fields, and changes the* Edit *and* Delete *buttons to* Update *and* Cancel *,with a different layout and look. Changing the buttons’ location and color is an extra, important signal in this feedback, as it reduces the likelihood that users will click the wrong button after editing if they aren’t paying attention and relying on muscle memory.This level of feedback clearly indicates what is happening with the system and how it’s responding to user input.*

### 1.a. Out to Lunch Without a Progress Indicator

A variant on lack of feedback is when a system fails to notify users that it's taking a long time to complete an action. Users often think that the application is broken or they start clicking on other targets.

If you can't meet the recommended [response-time limits](http://www.useit.com/papers/responsetime.html), say so, and keep users informed about what's going on with a [progress indicator](https://www.nngroup.com/articles/progress-indicators/):

- If a command takes between **2 and 10 seconds**, show a wait animation such as a “spinner.”This type of progress indicator tells users to hold their horses and not click on anything else until the normal cursor returns.
- If a command takes more than **10 seconds**, put up an explicit **progress bar**, preferably as a percent-done indicator (unless you truly can't predict how much work is left until the operation is done).

## 2. Inconsistency

Remember the double-D rule: **differences are difficult**. When users have expectations for how something will behave or where they can access it, deviations from those expectations cause confusion, frustration, and increased [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/) as people attempt to puzzle out the problem. Human minds [crave consistency.](https://www.nngroup.com/articles/top-10-mistakes-web-design/)

There are a few types of inconsistency that are especially common in complex applications and cause even seasoned users to be utterly confused:

- Different words or commands for the same action
- Placing controls for the same feature in many different places
- Controls that seem similar to one another (from the *user’s* point of view) but are accessed in different places (e.g. one is accessed in a toolbar, another a menu, and a third deep in a *Preferences* dialog)
- Similar workflow patterns which require interacting with very different sections of the interface
- Inconsistent rules for legit input data: sometimes an entry is allowed, and at other times it’s marked as invalid, without any feedback as to why this is happening
- A feature is sometimes available, and sometimes not for mysterious reasons that are not made explicit
- UI elements or controls that move around, violating **spatial consistency**

An architect in our study who had many years of experience using AutoCAD struggled to understand when she could or couldn’t “dock” various floating panels to keep them pinned to one side of the screen. In the same session, she tried multiple times to get a floating panel to dock to the left side, to no avail. It turned out that, due to a hidden parameter setting, this particular panel could not be docked, but this constraint was not made explicit to the user. The hidden setting was intended to give power users the ability to customize the interface to an incredible degree, but, due to poor feedback, our study participant couldn’t figure out why docking sometimes worked and sometimes didn’t. This type of inconsistency is a major source of frustration even to experienced users.

![An AutoCAD window that couldn't be snapped to one side of the screen for mysterious reasons](https://media.nngroup.com/media/editor/2019/01/17/autocad.png)

*AutoCAD did not consistently allow our study participant to “dock” panels to one side of the screen. Even an experienced user could not determine why this feature worked on some panels and not others. (It turned out to be a hidden parameter turned off for this one panel.)*

## 3. Bad Error Messages

Error messages are a special form of feedback: they tell users that something has gone wrong. We've known the [guidelines for error messages](https://www.nngroup.com/articles/error-message-guidelines)for almost 30 years, and yet many applications still violate them.

The most common guideline violation is when an error message simply says something is wrong, without **explaining why and how** the user can fix the problem. Such messages leave users stranded.

This problem has worsened over the years, largely due to web apps: Users are shown a *Something went wrong. Try again.* error message, with no details about the cause of the error or how it can be repaired. At least the native desktop applications of yesteryear used to tell people (often in technical lingo that lay users had no hope to make sense of) what the issue was.

![A collection of vauge "something went wrong" error messages with no helpful detail](https://media.nngroup.com/media/editor/2019/01/17/something-went-wrong.png)

*A collection of vague* Something went wrong *error messages from Quicken (top left), Dropbox (top right), IBM Verse (bottom): None of these describe the nature of the problem, details on how to avoid the problem, and whether the user’s work was lost in the process.*

Informative error messages not only help users fix their current problems, but they can also serve as a **teachable moment**. Although people won't invest time in reading and learning about your app’s features, they will make the effort to understand an error situation if you explain it clearly, because they want to overcome the error.

## 4. No Default Values

[Defaults](https://www.nngroup.com/articles/the-power-of-defaults/) help users in many ways. Most importantly, defaults can:

- **speed up** the interaction by freeing users from having to specify a value if the default is acceptable
- **teach** by providing an example of the type of answer that is appropriate for the question
- **direct novice users** toward a safe or common outcome, by letting them accept the default if they don't know what else to do

Default values can save significant user effort in repetitive tasks, such as filling in the same form many times. Identifying key values for form fields can increase productivity and reduce frustration. Your analytics can help you understand if there is a most commonly chosen option for a specific field.

In particular, [dropdown menus](https://www.nngroup.com/articles/drop-down-menus/) benefit from a meaningful default. Many apps provide *Select one* (i.e. no value selected at all) as the default choice, forcing every user to interact with the dropdown and select a value. If you preselect one choice (ideally the most common), at least some users will not have to interact with that dropdown at all.

With numeric form fields, if users deviate very little from a common default (e.g., for *Quantity* fields), you can use a [stepper](https://www.nngroup.com/articles/input-steppers/) to allow them to adjust the number without typing (but still allow users to type a different value if desired). Steppers have two benefits: they reduce [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) and give a reasonable starting point for new users who are still learning the system.

![A wizard in the Mint finance app that pulls in a default value, and gives up and down stepper buttons to change the default.](https://media.nngroup.com/media/editor/2019/01/17/mint.png)

*Mint, the personal-finance app, has a feature to help users find credit cards that matched their needs. This wizard employed a good default by automatically importing the user’s average monthly credit-card spending and giving the user an easy method to modify this number, either by typing or by using the increment/decrement buttons.*

## 5. Unlabeled icons

It’s really [rare for icons](https://www.nngroup.com/articles/icon-usability/) to stand on their own, with most users able to understand them immediately. Even icons that might seem universal (such as the [hamburger menu](https://www.nngroup.com/articles/hamburger-menus/)) are not as familiar to users as most UX practitioners would expect. It gets much worse if your application has icons that are unique; the likelihood that users will understand what these unique icons mean is very low. Remember Jakob’s law: "[users spend most of their time on other websites](https://www.nngroup.com/videos/jakobs-law-internet-ux/).” This means that most icons, unless they have a text label next to them, will be difficult or impossible for users to understand.

Pairing icons with a text label has four benefits:

1. It increases the size of the target (which, according to [Fitts’ Law](https://asktog.com/atc/principles-of-interaction-design/#fittsLaw), reduces how long it takes for users to access the control).
2. It decreases the time to recognize the command: two memory cues (icon and text) are better than one.
3. Related to the previous, it can also facilitate learning of the interface (by establishing multiple associations with the same command).
4. It can help users visually differentiate between several commands placed next to one another.

![A selection of mysterious, unlabeled icons from several applications](https://media.nngroup.com/media/editor/2019/01/17/bad-icons.png)

*A selection of unlabeled icons from a variety of desktop applications in our recent studies: All of these are nonstandard icons that don’t clearly indicate their purpose. Can you guess what they stand for? Our study participants couldn’t.*

## 6. Hard-to-Acquire Targets

In human–computer interaction, anything that can be clicked (or tapped) on is called a *target*: all active UI elements are targets. For users to acquire a target, they must be able to (1) identify the target; (2) click on it reliably. Both of these aspects cause problems in modern app interfaces.

### 6a. Weak Signifiers

"Affordance" means what you can do to an object. For example, a checkbox affords turning on and off, and a slider affords moving up or down. *Signifiers* are the visual elements that help you to understand the affordances just by *looking* at the object, before you start using it (or feeling it, if it's a physical device rather than an on-screen UI element). These concepts are discussed in Don Norman's book *The Design of Everyday Things*.

Signifiers are especially important in UI design, because all screen pixels afford clicking — even though nothing usually happens if you click. There are so many visible things on a computer screen that users don't have time for a **mine-sweeping** game, clicking around hoping to find something actionable. (Exception: [young children](https://www.nngroup.com/articles/childrens-websites-usability-issues/)sometimes like to explore screens by clicking around.)

In modern applications, one of the worst offenders are [ultra flat](https://www.nngroup.com/articles/flat-design/) designs. Many [flat designs have weak signifiers](https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/) for targets: people cannot easily tell text from buttons because buttons lack traditional 3D clues.

Common **symptoms** of weak signifiers are:

- Users say, "What do I do here?"
- Users don't go near a feature that would help them.
- A profusion of screen text tries to overcome these two problems. (Even worse are verbose, multistage instructions that disappear after you perform the first of several actions.)

### 6b. Tiny Click Targets

An associated problem here is click targets that are so small that users miss and click outside the active area. Even if they originally perceived the associated signifier correctly, users often change their mind and start believing that something isn't actionable because they think they clicked it and nothing happened.

(Small click zones are a particular problem for [old users](https://www.nngroup.com/articles/usability-for-senior-citizens)and users with motor skill [disabilities](https://www.nngroup.com/articles/beyond-accessibility-treating-users-with-disabilities-as-people).)

## 7. Overuse of Modals

Many applications use [modal windows](https://www.nngroup.com/articles/modal-nonmodal-dialog/) to implement interactions with data — editing an existing item, adding a new item, deleting, or even reading additional details about an item. Modals appear on top of the current page and the background content is usually dimmed (under the assumption that dimming will reduce distractions and help users focus on the task at hand). Unfortunately, this design choice reduces context for users by covering up information that they may wish to refer to while filling out the form. (Note that, even if the covered-up window does not contain information needed for the editing, users often attempt to leverage the work they’ve done previously, by copying and pasting previous inputs, or even simply using other entries as templates for how to think about the current task.)

![A table application with a modal covering important information](https://media.nngroup.com/media/editor/2019/01/17/airtable-modal.png)

*In Airtable, editing a table row opens a modal that covers most of the information in the table and prevents users from referencing that information.*

## 8. Meaningless Information

Long strings of letters and digits, such as automatically generated IDs in a database are frequently used to uniquely identify an item in an application. These strings are completely meaningless to users, but they are often prominently displayed as the first column of a table, forcing people to scan past that first column to find the information that they care about. While these meaningless indices are important on the back end, they should not be the primary piece of information that users must refer to. Especially in high–information-density screens, provide some human-readable information as the main anchor point and push the IDs to a less prominent position.

Egregious uses of coded information often appear in medical applications, CRM systems (where users often have to select a code for each sales interaction with their customers), accounting software, and enterprise applications. In all these apps, information that is meaningful to humans is summarized by a short code, in an attempt to make it more compact. A short code may fit in a small area better than a whole sentence, but places a much higher cognitive load on users. They will need to translate the coded information to make sense of it, and our working memory is limited to begin with. Even highly trained professionals cannot remember every possible code, and it still takes them a lot of effort to do this mental translation.

![A table with encoded information](https://media.nngroup.com/media/editor/2019/01/17/encoded-table.png)

*This table has meaningless ID information as the first column; the* Net Code *and* Location Code *fields also include encoded information that is intended to represent complex information in a compact space. The* Location Name *is the only column that makes sense to humans; to decipher the others, people have to either rely on their memory or they have to refer to a list of code keys.*

## 9. Junk-Drawer Menus

If your application has hundreds or even thousands of features, you have to put controls for those features somewhere, and furthermore, you need to prioritize and organize them so users can easily find and quickly access the most important ones. One consequence of this constraint is often an overflow menu: the most commonly used actions are displayed in a toolbar, and a final item labeled *More actions*, or *Tools*, or worst of all *…* hosts everything else that did not fit.

These menu labels have low [information scent](https://www.nngroup.com/articles/information-scent/) and are nothing more than a junk drawer: a place to put all the stuff you can’t otherwise categorize, but don’t want to throw away. They often come about because the team has a list of required features but doesn’t know where to put them, or in legacy applications, it cannot remove old, seldom used features. The problem with an overflow menu is that, just like with the junk drawer in your house, no one else can know what you might have put in it. In other words, it limits both *discoverability* and *findability* of features, since most users won’t have any reason to go looking in those menus.

![A mysterious menu, labeled with an elipsis](https://media.nngroup.com/media/editor/2019/01/17/airtable-junk-drawer.png)

*Airtable: A junk-drawer menu labeled*… *has little information scent. Users will have a hard time predicting what’s inside that menu.*

![A junk drawer menu labeled only with the word "More"](https://media.nngroup.com/media/editor/2019/01/17/salesforce-junk-drawer.png)

*Salesforce: A junk-drawer menu labeled* More

## 10. Proximity of Destructive and Confirmation Actions

Placing actions such as *Save* next to actions that destroy work such as *Discard* is a commonplace design decision that causes much grief for users. While logically this placement often makes sense (for example, *Save* and *Delete* are related, in that they decide the fate of an item), it also makes it easy to click the wrong button or icon — especially when users are rushing, completing repetitive actions, or have motor difficulties. This type of unintentional substitution of one action for another is called a [slip](https://www.nngroup.com/articles/slips/)

![A wizard with the final step having a Cancel and Finish button right next to each other.](https://media.nngroup.com/media/editor/2019/01/17/veeam-redacted.png)

*Veeam,an enterprise backup software, features a multistep wizard to set up a new backup job. In our study, a user spent almost 20 minutes to go through this wizard, and almost clicked* Cancel *rather than* Finish *on the very last summary page, due to the two buttons’ proximity. Had this user clicked* Cancel *, 20 minutes’ worth of work would have been lost.*

![The Flag for Follow up button right next to the delete icon in an email app](https://media.nngroup.com/media/editor/2019/01/17/outlook.png)

*Microsoft Outlook places the* Flag for Follow-Up *button right next to the* Archive *and* Delete *icons. These icons serve opposite user intentions, yet they are small, placed closely, and easily mistaken by users in a hurry.*

## Summary

Applications are hugely domain-specific, so a usable, efficient, and pleasant application for one industry might be an unmitigated disaster in another. Creating a usable application requires researching with your users to identify their workflows, their needed features, and their mental models and expectations.

However, the 10 application mistakes outlined here represent common themes that we observe in studies across a range of industries, including creative, financial, enterprise, healthcare, engineering, and more.

For more guidelines on application design, take our full-day course on [Application Design for Web and Desktop](https://www.nngroup.com/courses/application-ux/).
