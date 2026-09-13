---
title: "Scroll Fading 101"
date: "2023-12-08"
url: "https://www.nngroup.com/articles/scroll-fading-101/"
author: "Sara Paul"
topics: [design-patterns, interaction-design]
type: article
---

## In This Article:

- [Introduction](#toc-introduction-1)
- [What Is Scroll Fading?](#toc-what-is-scroll-fading-2)
- [Scroll Fading vs. Scrolljacking](#toc-scroll-fading-vs-scrolljacking-3)
- [Why Is Scroll Fading Used?](#toc-why-is-scroll-fading-used-4)
- [Research Study: Findings](#toc-research-study-findings-5)
- [Scroll Fading Best Practices](#toc-scroll-fading-best-practices-6)
- [Conclusion](#toc-conclusion-7)

## Introduction

Scroll fade is a new design pattern. It refers to an animation that is triggered by scrolling: new elements or content fade in or out once the user scrolls down to a certain point on the page.

Movement (and thus animation) is processed [preattentively](https://www.nngroup.com/articles/animation-usability/): the eyes are automatically drawn to it. As a result, incorrectly deployed animations can be highly distracting.

Because we know [fast user experiences beat glamorous ones](https://www.nngroup.com/articles/website-response-times/), we conducted a [qualitative](https://www.nngroup.com/articles/quant-vs-qual/) usability-testing study, in which we tested websites from multiple industries that all use scroll fading. This article discusses our findings and recommendations.

## What Is Scroll Fading?

From our [series of eyetracking studies](https://www.nngroup.com/articles/how-people-read-online/) on how people read online, we know users scan. One tactic for making information more digestible and scannable is to display it in small chunks. Designers can introduce those chunks when users scroll to a particular point on the page.

Definition: **Scroll fading** is an animation in which certain page elements appear or change once the user scrolls down to a certain point on the page.

![On Apple.com, the scroll interaction triggers text to fade in. The text is animated, rather than being revealed by the natural scroll progression on the page.](https://media.nngroup.com/media/editor/2023/11/27/definitionvideo1117.gif)

*Apple.com: The scroll interaction triggers the following text to fade in: Unlimited Daily Cash Back. Notice how the text is animated (rather than being revealed by the natural scroll progression on the page).*

## Scroll Fading vs. Scrolljacking

Scroll fading and [scrolljacking](https://www.nngroup.com/articles/scrolljacking-101/) are two different design patterns that relate to scrolling. The key difference between them is that scroll fading simply triggers an animation when a user scrolls to a particular point on the page, without affecting how the user is able to scroll. In contrast, scrolljacking changes the user’s scroll rate and sometimes the direction of scrolling, overriding the set scroll speed of the operating system.

Scroll fading and scrolljacking can be used together. In the Reachdesk.com example below, the user’s scroll rate is changed (scrolljacking) and elements on the page fade in upon the user scrolling (scroll fading).

*Reachdesk.com: In this clip from our usability study, a participant navigates a page that exhibits scrolljacking and scroll fading. Once the user scrolled down to the Deliver moments that matter portion of the page, the rate and direction of the scrolling were hijacked and the page started moving horizontally, even though the user was still scrolling vertically. Items like the text Boost virtual attendance by 42% faded into view — an example of a scroll fade within a scrolljack.*

## Why Is Scroll Fading Used?

Designers use scroll fading for a few common reasons, outlined below.

### Guide Users Through Long Pages

Scrolling per se introduces motion to an interface, but the scroll is controlled by the user. Scroll fading introduces a secondary type of motion that is not directly controlled by the user: an element can appear ("fade in”), disappear (“fade out”), and reappear. This additional motion gives high salience to the element that fades in or out and, thus, draws attention to it.

Scroll fading can be used to highlight important calls to action. Additionally, it can guide the user through the information-dense page via progressive disclosure, thus making the information more digestible.

### Optimize Data Loading

Product designers might advocate for lazy loading —not loading parts of a page until they are visible to the user. This practice [conserves bandwidth](https://www.nngroup.com/articles/law-of-bandwidth/) and data and rightly prioritizes fast loading of the elements above the fold. (We know that content [above the fold](https://www.nngroup.com/videos/fold-manifesto/) should load nearly immediately because [users are willing to wait for only so long](https://www.nngroup.com/articles/response-times-3-important-limits/) before moving on). Therefore, website-development teams might load images or other data-intensive resources only when users scroll down far enough.

### Add Timely, Supporting Information

Designers often leverage scroll fading to show users relevant information at a specific time. Crypto.com in the example below fades in supplementary images of the application that the text in focus describes. Scroll fading worked well in our testing when it added supplementary visual information. However, for some users, large images did not load quickly enough, further illustrating the importance of data-loading optimization.

*Crypto.com: In this clip on the homepage of Crypto.com, scroll fading is used to illustrate the Crypto in-app experience. Two phone notifications appear as overlays when the user scrolls to the Get the most out of your assets, safely section of the screen.*

### Boost Brand Credibility

The third reason why designers leverage scroll fading is to communicate the brand's credibility and trustworthiness. For example, on the University of Texas Austin’s homepage, scrolling down triggers a number-counter animation and shows the user that the information on the site is updated in real time. Multiple users in our study had this perception.

*Utexas.edu: In this clip from our usability study, scroll fading drew the user’s attention to the numeric information and created the sense that it was up to date and increasing in real time.*

## Research Study: Findings

### Animate Just Once

**Element persistence** in scroll fading refers to an animation that occurs only the first time the user reached that page position. The element remains visible, and the scroll-fading animation does not repeat as the user moves up and down the page.

Element persistence reduces the amount of animation on the page and works better than repeated animations.

Task-oriented users were not negatively impacted by scroll fading when it was accompanied by element persistence. In contrast, lack of persistence was problematic, because the same users did not have the patience to find the exact scroll position that caused the desired information to reappear.

For example, many study participants struggled with the calculator on Crypto.com because the inputs and outputs of the calculator were not displayed in the same viewport. Each time users readjusted the inputs, they had to scroll down and wait for the fade-in scroll animation to show the outputs. The result was wasted time and annoyance.

One participant frustratedly said, *Maybe the website should immediately scroll me down . . . and show me this . . . because I have to scroll down and up*.

*Crypto.com: A study participant tried to view the result of selecting multiple inputs in this online calculator and struggled because the calculator outputs kept appearing and disappearing due to scroll fading.*

### Illusion of Completeness Decreased Content Discoverability

The [illusion of completeness](https://www.nngroup.com/articles/illusion-of-completeness/) happens when the user perceives visible content as complete, yet more content exists below the fold. Large hero graphics or videos, expansive white space between content elements, and interruptions in the content flow (e.g., ads) often cause the illusion of completeness.

**Our study found that scroll fading can also contribute to the illusion of completeness**, especially when combined with other patterns susceptible to creating it.

When information below the fold slowly faded in on a page that already seemed complete, many study participants assumed there was nothing else to be found on the page.

Multiple participants experienced this issue on the Crypto.com page, because the information at the bottom of the page faded in only after the user scrolled far down below the fold. Eventually, because our study participants did spend some time exploring the site, they did discover the information that was faded in, but it’s safe to assume that, in real life, most users would not discover it on their own.

*Crypto.com: This clip shows the moment a study participant discovered the rate-of-return information she desired. This information was below the calculator and appeared on a scroll fade, but only if the user scrolled far enough into the seemingly empty space. She had initially assumed this information was not there at all because it was not initially visible.*

### Comprehension of Scroll-Fading Text Depended on Effective Writing

Scroll fading of text can affect how easily people understand it. In general, scroll fading worked well with text that followed the [best practices for writing on the web](https://www.nngroup.com/articles/writing-style-for-print-vs-web/).

For example, one participant reading through the MagicLinks website moved quickly past the scroll-fading text and then scrolled back up to reread it, because he did not comprehend it. This is partly because the text faded in too slowly and partly because the writing could have been more effective.

*MagicLinks.com: A study participant moved through a series of text scroll fades, to ultimately have to reread the text.*

In contrast, the scroll-fading text on Apple Card website was easier to understand, because it was short, punchy, and information-packed. The snippets concisely communicated product value in the first few words and supported scanning. Additionally, the Apple Card page design gave considerable visual weight to the text, which contained the card’s key selling points.

*Apple.com: A study participant moved through several text and image scroll-fade animations that captured her attention yet didn’t overwhelm her.*

### Users Skipped Content Fading In Too Slowly

The speed with which text faded in also contributed to comprehension. If the scroll-fade speed was too slow, users scanning quickly often skipped it altogether, scrolling past it. [Prior research](https://www.nngroup.com/articles/animation-duration/) tells us that a scroll-fade animation that takes more than 500ms is perceived as too slow. When this duration was approached or exceeded, we observed several users scroll past an element before it finished fading in.

*Apple.com:  A study participant scrolled past the Privacy and Security content block before it has a chance to fully fade in.*

### Scrollfading Images Often Failed to Load, Which Hurt Brand

In our study, pages with several scroll-fading images often failed to load all the images, confirming the consequences of the data-loading risk described above.

On Cigna.com, even though the text scroll faded in, the images didn’t load and our study participants were left feeling that they missed something. One user said, *I don’t like this portion, because it has text but there’s no image beside it. I think an image would probably help enhance the text*. Another participant, who was able to load and view the images, mentioned that the experience of choosing insurance is stressful and the images made a positive difference in decreasing stress and shaping the brand personality.

*Cigna.com: Slow loading images deteriorated the experience of a study participant, who mentioned that she wished the page included some images, because healthcare is “difficult.”*

### Scrolljacking + Scrollfading = Worst Usability

When scrollfading occurred within a [scrolljacked](https://www.nngroup.com/articles/scrolljacking-101/) page section, several study participants became overwhelmed and frustrated. The distracting motion from the scroll-fade animation combined with the lack of control from the scrolljack caused cognitive overload. This occurs in the Reachdesk clip above, where a study participant encountered text and an image that scroll faded in and out and were also contained inside of a horizontal scrolljack, which rendered the content difficult to read, navigate, and understand.

## Scroll Fading Best Practices

Our research findings show that scroll fading introduces a mix of usability obstacles, but designers can avoid them and take advantage of its benefits by adhering to the following guidelines.

### Optimize Your Text-Fade-In Rate

Users are likely to skip over text if it fades in too slowly. As a result, they may not comprehend what the website offers and whether it addresses their needs. However, too fast fade-in rates can also cause them to not notice the animation. To find the perfect duration, experiment with rates between [100–400ms](https://www.nngroup.com/articles/animation-duration/). Adjust and test the rates in [usability testing](https://www.nngroup.com/articles/usability-testing-101/), to determine whether your animation is too fast to be noticed or gradual enough to lead people through the page.

### Fade In Content Only Once

Because many users naturally skip over most scroll-fading text on their first pass down a page, element persistence on scroll fading gives the user a better chance of seeing the content on their way back up to the top of the screen if they missed it or if they need to reread it for comprehension or comparison purposes. Our study [confirmed](https://www.nngroup.com/articles/scroll-animations/) the importance of persisting content to support user efficiency and decrease cognitive load.

### Fade In One Element Type at a Time

If text and images fade in at the same time, they risk pulling the users’ attention in too many directions and overwhelming them. In our study, the most successful examples of scroll fading animated only one element at a time — either the text or the images. On websites where both text and images faded in together, they competed for the user’s attention. Any motion into an interface must carefully be deployed and evaluated. In the Apple.com design, either text or images faded in but not both simultaneously. This practice effectively drew the user’s attention to one place at a time, and it was always the most important place. That page saw the best overall efficiency and comprehension in our study.

### Leverage the Gestalt Principles of Proximity and Closure to Encourage Scrolling

Removing excessive whitespace and thereby decreasing the proximity between one content section and the next that fades in makes it less likely that people will fall prey to the illusion of completeness.

Further, leverage the [principle of closure](https://www.nngroup.com/videos/closure-gestalt/) by making at least part of each subsequent content section visible (like on the Apple Card website), to encourage the user to scroll down to view the full content.

### Avoid Scroll Fading on Mobile

The usability issues observed on desktop were exacerbated on mobile due to the smaller screen lengths, which meant fewer pixels could be viewed at a time and scroll fatigue was increased. For example, on the mobile site of Crypto.com, users had to scroll even more than on desktop to use the website calculator. They had to wait for the calculator output to fade in each time they tested a new input. Furthermore, the illusion of completeness was more severe on mobile due to the whitespace between the calculator and the information below it.

### Keep Text Concise

Scroll fading was by and large most successful when the text contained in it was concise and communicated value. This natural alignment with best practices of writing for the web enabled the highest levels of efficiency and comprehension.

## Conclusion

Scroll fading can cause serious usability issues when used incorrectly. Used sparingly, at relatively fast speeds, it can draw user attention, improve brand perception, speed up page loading, and divide your content into smaller, digestible nuggets.
