---
title: "The Anchoring Principle"
date: "2018-12-09"
url: "https://www.nngroup.com/articles/anchoring-principle/"
author: "Therese Fessenden"
topics: [persuasive-design, psychology-and-ux]
type: article
---

My husband and I were car shopping and found a used BMW that looked pristine and had only 10,000 miles on it. The price was shockingly low, only $2,000. We had to have it. Driving home, we smiled from ear to ear about our shiny used car, unknowing it would fall apart within 18 months. We had focused so much on the price and vehicle make, that we did not consider the possible issues (such as rusted parts in old, unused cars). This is anchoring bias at work.

**Definition:** Anchoring (or focalism) bias refers to the tendency to rely on a single piece of information or aspect of an event (the “anchor”) to inform decision making.

## In This Article:

- [Judgment Heuristics](#toc-judgment-heuristics-1)
- [Past Studies about Anchoring](#toc-past-studies-about-anchoring-2)
- [How Anchoring Can Improve the User Experience](#toc-how-anchoring-can-improve-the-user-experience-3)
- [Conclusion](#toc-conclusion-4)

## Judgment Heuristics

Anchoring is a judgment heuristic. Anchoring and other judgment heuristics, such as [framing](https://www.nngroup.com/articles/prospect-theory/) and [priming](https://www.nngroup.com/articles/priming/), are helpful in expediting everyday decisions, particularly in the absence of information, resources, or time. They [tend to be automatic](https://www.nngroup.com/articles/first-impressions-human-automaticity/) for most people and can sometimes lead to erroneous estimates or judgment calls.

There are some people who benefit greatly from anchoring; for example, domain experts with deep experience directly related to the decision or judgment at hand. Because they are so familiar with the situation, their early responses are likely to be correct.

## Past Studies about Anchoring

Researchers have conducted many studies about anchoring. For fun, let’s pretend we’re subjects in the most notorious study.

Take **ONLY FIVE SECONDS** to calculate the following mathematical expression (no calculators!). Then write down your answer.

**1x2x3x4x5x6x7x8**

Did you write a number between 100 and 900? Most people do.

In 1974, the psychologists Amos Tversky and Daniel Kahneman asked each of their study participants to calculate one of two different mathematical expressions:

**1x2x3x4x5x6x7x8**

or

**8x7x6x5x4x3x2x1**

Because participants were given only 5 seconds to solve the problem, they estimated the answer as opposed to actually performing the multiplication.**The solution to both problems is the same number: 40,320.** But people made very different estimates for each mathematical expression. For the group which was presented with the 1x2x3x4x5x6x7x8 problem, the median estimate was **512** — meaning that half the participants came up with a number smaller than 512. For the group presented with 8x7x6x5x4x3x2x1, the median estimate was **2,250**, or **more than 4 times bigger**. Not a negligible difference — created by simply presenting the stimulus in reverse order.

![Median estimates for the two forms of mathematical expressions presented during the Tversky and Kahneman study.](https://media.nngroup.com/media/editor/2018/09/17/anchoringeq3.png)

*Amos Tversky and Daniel Kahneman’s research on judgment heuristics revealed large discrepancies in estimates when people were shown different versions of the same mathematical product.*

Why such a big difference in estimates? The answer is that the leading “anchor” numbers of each of the problems (1x2=2 vs. 8x7=56) swayed estimates significantly. Small numbers at the beginning signaled a small result, and large ones coaxed a large estimate.

In a similar study done by Dan Ariely and colleagues at MIT, participants were asked whether they would purchase various goods (such as wireless keyboards, bottles of wine, and textbooks) for the dollar figure equal to their last two digits of their social security number (SSN). After accepting or rejecting that price, they had to state the maximum price they would actually be willing to pay for the item. People whose SSNs ended in low digits chose a lower price threshold than people with high-ending SSNs. In other words, participants were primed to use the last two digits of their SSN as an anchor for the price of the good, although the SSN was obviously unrelated to the value of the good.

Table 1. Dan Ariely et al. Study Results: Bids on a Wireless Keyboard, by SSN | Last two digits of | Social Security Number | Average Bid | 00-19 | $16.09 | 20-39 | $26.82 | 40-59 | $29.27 | 60-79 | $34.55 | 80-99 | $55.64

*Average bids for a wireless keyboard varied depending on the first hypothetical price (equal with the last two digits of their SSN) that people had been asked to consider: those whose SSN ended in low numbers tended to make lower bids than people whose SSN ended in high numbers.*

Both studies illustrate people’s tendency to overly rely on initial information to anchor future estimates, even if those anchors have little relevance to the actual decision being made.

## How Anchoring Can Improve the User Experience

Anchoring can set novice users up for success and establish clear expectations about how a process or experience might go. Consider the following applications in your next redesign.

### Good Defaults and Suggested Values

Not only do [well-chosen numerical default values](https://www.nngroup.com/articles/the-power-of-defaults/) minimize the interaction cost of typing, but they can also serve as anchors for the expected variation of the corresponding [numerical parameters](https://www.nngroup.com/articles/sliders-knobs/). They can help users figure out what a big value is and what a small value is. For example, for people who have never used an image-editing program, a default gamma value of 2.2 creates an understanding of the normal, most used value, and allows users to adjust that value in the direction that they want, according to the effect they seek.

If you are new to shopping for a house, a good mortgage calculator can form expectations by providing defaults that best represent the user population. For example, Bankrate.com’s mortgage calculator shows default values that are close to the typical value most users will enter. These defaults help users gauge what’s expected and what might be off the norm.

![Bankrate.com screenshot of mortgage calculator showing helpful default values](https://media.nngroup.com/media/editor/2018/09/17/bankrate.png)

*Bankrate.com’s mortgage calculator takes advantage of the anchoring principle when it sets customary default values for the calculator fields. These values set expectations with users as they shop for a new home.*

A suggested donation value can also prod users in the right direction on nonprofit websites, by providing an anchor for deciding how much they should give. This default takes the decision burden off users: depending on their situation and level of interest in the cause, they can donate less or more than the recommended value. For example, in one A/B test reported by Behave.org, Oxfam tested two different variations of a donation call-to-action: one with suggested values of monthly donation and ‎£4 and another with just a Donate now button. The first condition yielded 23% more form completions than the second condition.

![Screenshot of Behave.org A/B test of the Oxfam mobile site donation CTA](https://media.nngroup.com/media/editor/2018/09/17/oxfam.png)

*In an A/B test of the Oxfam mobile site, a suggested donation rate and value resulted in an increase in form completions. (Screenshots from Behave.org)*

The winning design decreased users’ cognitive load and interaction cost in two ways:

- People did not have to navigate to a new page and wait for that page to load.
- They did not have to think about the donation specifics because they were already provided in the defaults; they could simply adjust those levels up or down, depending on their circumstances.

### Set Accurate Expectations at the Beginning of a Workflow or Process

Anchoring can also establish expectations at the beginning of an experience. With [complex forms or applications](https://www.nngroup.com/articles/forms-vs-applications/), it is helpful to provide a sense of how long the process might take, upfront, to allow users to determine whether they have the time and resources to complete it right then. However this time estimate also serves as an anchor: if the process will end up being longer, users will feel cheated and disappointed (and vice versa). It’s important to strive for accurate (or slightly conservative) estimates to avoid disappointment.

### Show Original Prices Along with the Discounted Price

Consider how you present discounts. Showing the original price with the discounted price means that original price can anchor the user’s [perception of that item’s value](https://www.nngroup.com/articles/perceived-value/). For example, users might estimate a high value for the excursions offered by Reykjavik Excursions because the original prices are displayed with the discounted ones.

![Reykjavik Excursions website screenshot of discounted prices shown alongside regular prices](https://media.nngroup.com/media/editor/2018/09/17/re-savings.png)

*Reykjavik Excursions highlighted sales price while still displaying original prices (12,900 ISK, 8,500 ISK, and 21,900 ISK, respectively­) in strikeout text format, which can help to anchor estimates of true value to a higher value than if that original price was not presented.*

## Conclusion

In the absence of other information, people rely heavily on anchoring in order to shape the decisions they make when using a product or service. Good anchors help users set their expectation for what’s normal or exceptional, lower the cognitive cost of decision making, and can even increase the perceived value of a product.

**References**

Amos Tversky and Daniel Kahneman: “Judgment under uncertainty: heuristics and biases,” *Science* (Sep. 27, 1974)

Dan Ariely, George Loewenstein, and Drazen Prelec: “Coherent arbitrariness: stable demand curves without stable preferences,” *The Quarterly Journal of Economics*, Volume 118 (February 1, 2003)
