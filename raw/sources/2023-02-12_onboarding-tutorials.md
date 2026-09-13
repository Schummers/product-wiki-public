---
title: "Onboarding Tutorials vs. Contextual Help"
date: "2023-02-12"
url: "https://www.nngroup.com/articles/onboarding-tutorials/"
author: "Page Laubheimer"
topics: [applications, interaction-design]
type: article
---

## In This Article:

- [Examples of Tutorials in Apps](#toc-examples-of-tutorials-in-apps-1)
- [Tutorials: Disruptive, Often Skipped, and Easily Forgotten](#toc-tutorials-disruptive-often-skipped-and-easily-forgotten-2)
- [Why Tutorials (and Push Revelations) Don’t Work](#toc-why-tutorials-and-push-revelations-dont-work-3)
- [What Works: Pull Revelations](#toc-what-works-pull-revelations-4)
- [Guidelines for Implementing Pull Revelations](#toc-guidelines-for-implementing-pull-revelations-5)

## Examples of Tutorials in Apps

I recently purchased a bike that has an unusual feature –- instead of the classic chain drive system, it features a carbon-fiber belt that, doesn’t require messy grease, is nearly silent, and won’t rust in the rain. But, because it’s a fairly novel system for a bike, I had no idea how to properly set it up. Luckily, there was an app to help with that task, and it centers around a fairly unique interaction: you pluck the carbon-fiber belt on the bike as if it were a guitar string, and the app measures the sound’s frequency with the microphone in your mobile device to tell you whether the belt is properly tensioned. Neat!

When I first launched the app, it ushered me into a long tutorial on how to set up the new belt. The multistep tutorial was nice and clear, except for one big thing –- once I finished it, I couldn’t remember how to do the procedure on the setup screen, and, even worse, I couldn’t figure out how to launch the tutorial again. Eventually, I realized that there was a list of instructions available in the *Help* menu, but that still required me to memorize the steps, go back to the main part of the app, and complete the process with all that information in my [working memory](https://www.nngroup.com/videos/short-term-memory-ui-design/).

*Gates Carbon Drive app: After the tutorial finished, it dropped the user into the app without any further guidance. The user had to remember the steps and actions presented in the tutorial to set up the belt.*

Consider another recent experience. I was trying to dispute a fraudulent credit-card charge in my bank’s mobile app. I was, as you might imagine, a bit stressed. As I logged into the app, hoping to get things resolved quickly, I was bombarded with this walkthrough:

![Chase bank shows a deck of cards of new features when the user logs ins](https://media.nngroup.com/media/editor/2023/01/05/chase-1.png)

*Chase bank’s mobile app showed a*[deck-of-cards](https://www.nngroup.com/articles/two-basic-hypertext-presentation-models/)*meant**to promote new features when the user logged in. Not only did this walkthrough interrupt the user from their task, but it did not communicate what the specific improvements were or how to use them.*

Now, I’m happy for the Chase UX team that it’s made improvements. However, I was not filled with a sense of excitement and wonder when I encountered this tutorial. Nor was I motivated to go and explore these changes; I had a task to complete, and it was fairly pressing. This tutorial added to my stress during a moment when I relied on my bank to provide ease and stability. In that context, the happy and excited [tone of the messaging](https://www.nngroup.com/videos/establishing-tone-voice/) came across as rather tone-deaf –– it also [slowed me down](https://www.nngroup.com/articles/slow-ui/), which is something that we don’t often want to do to our users.

Or, consider another variation of this common experience. Imagine you’re on a tight deadline to finish a project at work. You log in to the productivity application you use everyday and are bombarded by a list of changes in a *What’s New* release-notes [modal](https://www.nngroup.com/articles/modal-nonmodal-dialog/). You dismiss it without bothering to read it, trying to get to your work. You then realize that many of the tools and features you rely on have been moved around, but you can’t find that list of changes anywhere to guide you

## Tutorials: Disruptive, Often Skipped, and Easily Forgotten

Good [help and documentation](https://www.nngroup.com/articles/help-and-documentation/) are critical, especially with fairly complex or nonstandard interactions. And, in fact, this is one of the [10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/).

But not all help is created equal. Intrusive tutorials and lists of changes that are shown when an app is launched or at random points during the user’s session are a type of **push revelation.** Push revelations reveal new information out of context, without any specific indication that the user would benefit from the information *at that moment*. A good user experience depends heavily on context –- presenting information and options to users at the right moment, when they are ready for it, not when it’s convenient for the system. Push revelations are well-named: they are typically *pushy*, devoid of context, and intrusive.

These sorts of tutorials tend to get used in two ways: for [new user onboarding](https://www.nngroup.com/articles/mobile-app-onboarding/) and to make existing users aware of new features or changes. Both struggle with similar problems: they interrupt users who are attempting to do something else at that moment, they don’t tend to be memorable, and they also [don’t result in better task performance](https://www.nngroup.com/articles/mobile-tutorials/). So, in essence, they slow users down, get in the way, and don’t achieve their very reason for being.

Now, this isn’t to say that walkthrough-style tutorials are never appropriate (our own research indicated that they were useful for [onboarding new users to a novel interaction paradigm like AR](https://www.nngroup.com/articles/ar-walkthroughs/)), but they are dramatically overused. Moreover, we find that users frequently skip them.

![ArcGIS onboarding tutorial in a modal in the middle of the screen](https://media.nngroup.com/media/editor/2023/01/05/arcgiis.png)

*ArcGIS included a detailed interactive onboarding tutorial that was better than many other tutorials or walkthroughs. Unlike many other walkthroughs, this one required users to perform the task, rather than simply showing them how to do it. Furthermore, this tutorial wasn’t activated automatically the first time the user logged in but rather was made available in the sidebar. This design made it possible for users to revisit the tutorial later, when they inevitably forgot much of the information.*

Tutorials *seem* like they should be effective for helping users learn: they’re directly telling users how to use the software! And yet, in our studies, they frequently don’t perform well with real users. So, what goes wrong? Is the whole idea of a tutorial bad, or is the execution that’s flawed? Are there ways to make them work better?

First, let’s break down what’s wrong.

## Why Tutorials (and Push Revelations) Don’t Work

These are the main design mistakes that tutorials (and, more generally, push revelations) make:

1. **Users want to start using the product right away.** They don’t want to spend time studying how to use your app.. This is known as the **paradox of the active user**(a paradox because the prep work would benefit them in the long run). The interruption posed by a tutorial is unwanted, so users skip it.
2. The guidance that tutorials provide, while potentially helpful, is **hard to remember when the user needs it**. The tutorial shows information **out of context,** and users would have to memorize it to use it when applicable. Unfortunately, our[memory is](https://www.nngroup.com/articles/working-memory-external-memory/) quite limited. Tutorials could increase the likelihood that users retain the information by forcing them to *practice* using the feature. However, that can be annoying for those users who turned to the product to complete a different task.
3. Dismissing the tutorial or the push revelation requires user effort. For example, push revelations (even if not full-blown tutorials) are often designed to be visually salient and noticeable, which unfortunately also makes them more likely to be distracting or annoying.

## What Works: Pull Revelations

It turns out that we can solve these issues by [presenting help content contextually](https://www.nngroup.com/articles/mobile-instructional-overlay/). **Pull******revelations** are help content triggered by some signal that the user would benefit from that information at that moment. Pull revelations can come in a variety of formats ranging from hover tooltips or [coach marks](https://www.nngroup.com/articles/mobile-app-onboarding/) to more expansive patterns like step-by-step task-flow wizards.

![Figma shows a contextual help indicator for text layout, only once the user has opened the appropriate text layout tool](https://media.nngroup.com/media/editor/2023/01/05/figma-contextual.png)

*Figma uses a pull revelation to note a change to its default text rendering: the tip is shown only when the user is involved in an activity related to the tip (e.g., they have added a new text box).*

## Guidelines for Implementing Pull Revelations

Pull revelations require that the app knows the what the user is trying to do and thus, they can be trickier to implement than push revelations. Determining the user’s goal is relatively straightforward in some situations — for example, if the user hovers over a new toolbar icon, it’s appropriate to show them a tooltip or an instructional overlay.

However, for more complex work, things can go wrong. The famous Clippy, the Microsoft Office assistant, was a failed attempt to develop AI-driven pull revelations; the failure was due to the intrusive and didactic nature of the revelations, the annoying animated, hard-to-ignore character sitting in the user’s peripheral vision, and the relatively unsophisticated, often wrong pattern matching used to figure out what the user was attempting to do.

Some guidelines for appropriately using contextual help include:

1. **Make it easy to dismiss (and recall) the help content**. Being able to get rid of a (momentarily) unhelpful overlay is absolutely critical, but so is the ability to find this information again later, when it is actually useful.

![Evernote has a "What's new" menu that is always available](https://media.nngroup.com/media/editor/2023/01/05/evernote.png)

*Evernote shows a list of new features in the sidebar that can easily be dismissed. However, the* What’s New *list at the bottom left remains in place in case the user wishes to access it again.*

1. **Use**[progressive disclosure](https://www.nngroup.com/videos/progressive-disclosure/)**in the help content.** Make the existence of the contextual help visible, but do not overwhelm the user with detail until they ask for it.

![Photoshop shows a hover-based tooltip with an animation showing the effect of the tool](https://media.nngroup.com/media/editor/2023/01/05/photoshop.png)

*Photoshop: A pull revelation is used to help users expand their command vocabulary. The tooltip appears when a user hovers over a toolbar icon and features a simple animation demonstrating the effect of the tool — useful for new users who need to quickly develop an understanding of the various features. The tip also uses progressive disclosure (* Learn how *) to engage those users who want more information on how to use the tool, but not overwhelm all users with unnecessary detail.*

1. **No memorization!** For multistep workflows, make sure that the help content doesn’t require the user to keep lots of information in their working memory — show help content alongside each step to [minimize cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/).
2. **Skip the obvious stuff.** If your app follows [design conventions,](https://www.nngroup.com/articles/consistency-and-standards/) you probably don’t need to give users lots of detail on what the gear icon means (it usually means *Settings*). Save the contextual help for more complex functionality or processes.
3. **Understand the user’s journey to that feature.** Take the time to really consider when the user is most likely to interact with the feature in question. This is the most important guideline, but also the most complex. This requires [user research](https://www.nngroup.com/articles/field-studies/) and [task analysis](https://www.nngroup.com/articles/task-analysis/) to figure out how users actually interact with your product and what sorts of signals indicate that a user is in need of help.
