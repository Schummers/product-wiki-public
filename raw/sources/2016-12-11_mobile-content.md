---
title: "Reading Content on Mobile Devices"
date: "2016-12-11"
url: "https://www.nngroup.com/articles/mobile-content/"
author: "Kate Moran"
topics: [content-strategy, mobile-and-tablet-design, writing-web]
type: article
---

In 2010, researchers at the University of Alberta found that [reading comprehension was impaired when content was presented on a mobile-size screen](https://nngroup.com/articles/mobile-content-is-twice-as-difficult-2011) versus a larger computer screen. A simple explanation for this result was that, with a small screen, users saw less of the text at any given time, so they had to rely more on their memory to access contextual information needed during reading. In other words, the smaller screen resulted in a higher working-memory load. People could not sustain that higher load, so their comprehension suffered.

In our research, conducted six years later, we found a surprisingly different result. We asked 276 participants to read a variety of articles on various topics on either a mobile phone or a personal computer. Some of the articles were easy and some were difficult. After each article, we asked participants to answer a few questions to measure their level of comprehension of the content. We found **no practical differences** in the comprehension scores of the participants, whether they were reading on a mobile device or a computer.

Despite this finding, **we still recommend**[prioritizing brevity](https://www.nngroup.com/articles/condense-mobile-content/) and reducing unnecessary content when writing for mobile.

## In This Article:

- [Methodology and Analysis](#toc-methodology-and-analysis-1)
- [Comprehension Scores: Slightly Higher on Mobile](#toc-comprehension-scores-slightly-higher-on-mobile-2)
- [Very Difficult Content May Cause Lower Comprehension on Mobile](#toc-very-difficult-content-may-cause-lower-comprehension-on-mobile-3)
- [Reading Speeds: Readers Slow Down for Difficult Articles on Mobile](#toc-reading-speeds-readers-slow-down-for-difficult-articles-on-mobile-4)
- [Speed-Accuracy Tradeoff on Mobile](#toc-speed-accuracy-tradeoff-on-mobile-5)
- [Key Takeaways](#toc-key-takeaways-6)
- [Recommendations for Mobile Content](#toc-recommendations-for-mobile-content-7)
- [Reference](#toc-reference-8)

## Methodology and Analysis

We began our study with the expectation that our findings would support the original 2010 conclusions. Our two hypotheses were:

1. Reading comprehension is lower when articles are read on mobile phones vs computers.
2. Articles that are difficult to read impact mobile comprehension more than desktop comprehension.

Our participants were a broad sample of general web users. In all phases of the study, participants were asked to read a variety of articles on different topics and levels of difficulty.

The difficulty of the articles (“easy” or “hard”) was determined by the length of the article (word count) and the difficulty of the language used (according to the [Flesch-Kincaid reading-level](https://www.nngroup.com/articles/legibility-readability-comprehension/) formula). All of the articles were presented as HTML pages created from the same simple design template.

The difference between the easy and difficult articles is summarized in the following table (averaged across the articles used in the last two rounds of our research):

Easy articles | Hard articles | Average length | 404 words | 988 words | Average reading level | 8th grade | 12th grade

By way of comparison, the article you’re reading right now has 2,072 words and is written at the 13th grade [readability level](https://www.nngroup.com/articles/legibility-readability-comprehension/).

Participants read half of the articles on a computer and half of the articles on a phone, alternating between the computer and the phone (we randomized the device used for each person’s first article). After reading each article, they answered multiple choice questions to assess how well they had comprehended and retained the information they had just read.

We began our study with a small [pilot test](https://www.nngroup.com/articles/pilot-testing/) (something we highly recommend for all UX research studies). When our results contradicted the previous research by suggesting that there was no difference between comprehension for mobile and computers, we had to consider the possibility that our methodology was faulty, and so we proceeded through a series of studies with different stimuli and test conditions. In the end, our research combined four [measurement studies](https://www.nngroup.com/courses/measuring-ux/):

- 10-participant online pilot
- 30-participant online study
- 40-participant in-person study
- 206-participant online study

For the pilot, we used content pulled from live websites; for the other studies, we used articles that we wrote ourselves to have more control over the content. Half the articles in our studies were easy and half were hard, and each participant saw both hard and easy passages on each device. (In other words, both article difficulty and presentation device were [within-subjects](https://www.nngroup.com/articles/between-within-subjects/) independent variables. In our final analysis, the type of study — online or in-person — was the third between-subjects independent variable.)

For all studies, we used comprehension scores as the main dependent variable. These scores are percentages from 0 to 100% that took into account correct responses, but also penalized incorrect responses (see the attached materials for a precise definition). For the in-person studies we also measured article reading times. Note that our comprehension metric was different than that used by Singh and colleagues in their original study (they used a [cloze test](https://www.nngroup.com/articles/cloze-test-reading-comprehension/)).

In each phase of the study, we tweaked our methodology or stimuli, but found the same surprising result — no perceptible difference in reading comprehension between the devices. To supplement the quantitative testing, we also ran a set of focus groups with the participants in our in-person study, asking them to discuss how they read web content and how they perceive reading on mobile devices vs. reading on computers.

(If you’d like to replicate our research — or conduct new reading research, maybe with additional devices — you can download our final stimuli and associated comprehension quiz questions from the link at the bottom of this article.)

To maximize the statistical power of our study, we performed a mixed ANOVA on the comprehension scores from all four phases of the study, controlling for the different articles and study procedures used. This analysis included **1,629 cases** where a user read an article and completed the comprehension quiz for that article.

For the in-person data, we also ran a repeated-measure ANOVA on the reading speed (defined as the time taken to read one word).

## Comprehension Scores: Slightly Higher on Mobile

We found that, on average, comprehension scores were slightly *higher* when users read the articles on mobile devices. Although **the effect of device was statistically significant (at p = 0.0006), the difference in comprehension scores was not practically significant**: comprehension on mobile was about **3 percentage points higher than on a computer**, with a 95% confidence interval of 1% to 5%.

Unsurprisingly, comprehension scores were lower for difficult articles compared with easy ones (this main effect of difficulty was significant at p=0.0001).

![Reading comprehension scores by article difficulty and device](https://media.nngroup.com/media/editor/2016/12/13/comprehension-scores-2.png)

*Average comprehension scores for easy and hard articles, by device*

## Very Difficult Content May Cause Lower Comprehension on Mobile

Our data analysis of comprehension scores also found a marginally significant interaction (p=.10) between content difficulty (easy vs. hard articles) and reading device (mobile vs. computer), indicating that the (already very small) comprehension-score advantage for mobile is reduced when reading difficult articles.

More research is needed to know if this effect is real, but if it is, and if it continues to be true for progressively more difficult content (beyond the difficulty levels included in our study), then it may be the case that **very difficult content is harder to read on a phone than on a computer**.

## Reading Speeds: Readers Slow Down for Difficult Articles on Mobile

For the in-person data, we also captured the time each user spent reading each article. Because articles varied in length, instead of analyzing the overall reading time, we looked at the reading speed, defined as the article reading time divided by the article length (in words).

Our repeated-measures ANOVA yielded a significant interaction of device and difficulty (p =0.01). **Easy passages were read about as fast on both devices, but hard passages actually took longer on mobile versus computer.**(On average, participants spent about 30 milliseconds more on each word when reading on mobile than on a computer.)

![Reading speeds](https://media.nngroup.com/media/editor/2016/12/13/reading-speed-2.png)

*Average reading speeds for easy and hard articles, by device*

## Speed-Accuracy Tradeoff on Mobile

Why did we get no comprehension-score difference between the devices? Does this result contradict our theory that text presented on a small screen incurs a higher cognitive load than text presented on a larger screen?

We can find the answer by considering the reading-speed difference in mobile vs. computer. Remember, when participants were reading easy articles, their reading speeds were about the same on mobile as on a computer. However, when the participants read *difficult* articles (long word counts, challenging topics and language), their reading speeds slowed down.

In other words, **they could not sustain the higher working-memory load**, and, to achieve the same level of comprehension, they had to either:

1. read more carefully and try to remember potentially relevant information, or
2. go back and re-read certain passages.

In psychology, this phenomenon is referred to as a **speed–accuracy tradeoff**— users had to slow down to achieve the same level of comprehension for difficult articles on a phone as they did on a computer.

This suggests that, while reading comprehension may be comparable on a phone and a computer for easy articles, **reading on mobile becomes more difficult as the complexity of the content increases**. (The marginally significant interaction on comprehension scores points in that direction, too.)

The speed-accuracy tradeoff also offers a potential explanation for why we obtained very different results than Singh and his colleagues: their study used *very* difficult content (privacy policies) as stimuli. It’s possible that, at that level of complexity, participants simply ended up sacrificing some of their comprehension to maintain a decent completion speed in the experiment. With extremely complex content, we may still see substantial decreases in comprehension scores on mobile. But then, we’d never recommend that any web content be as complex as privacy policies tend to be.

There are other several possible reasons that may have contributed to the difference in the results:

- **The prior study used a different comprehension metric** (cloze test) than we did. It’s possible that our test tapped into different cognitive processes.
- **Text presentation on mobile devices has significantly improved** since Singh et al.’s study. Smartphones screens are bigger, and their resolutions are crisper: a typical phone screen today (iPhone 7) has 6.5 times more pixels than a typical phone screen at the time of the original research (iPhone 3).
- **Some participants reported frequently reading articles on their phones**, and feeling comfortable doing so. They commented that thumb scrolling felt easier than acquiring the scrollbar and dragging it — which some users still do, not being accustomed to a scroll wheel on a mouse.
- **Some participants reported that they liked the lack of “distractions” on the mobile device**. For sequential reading, like articles, mobile may have the advantage here. Though the smaller window limits the amount of information that can be viewed at once, it also can filter out competing information.

## Key Takeaways

For linear content like articles, especially easy-to-read content, comprehension on mobile appears to be on-par with larger devices.

Does this result mean that mobile devices are now just as easy to use as desktops or laptops? Unfortunately, no.

First, we know that, in general, **task performance on mobile devices is still lower** than desktops or laptops. We measured reading comprehension in this study, but most web tasks involve much more than reading. **Articles are linear content**— they don’t reflect all web content or online tasks. Most online activities involve some degree of navigation and interaction. Ecommerce and other web tasks require substantial navigation and [comparisons between multiple pieces of content](https://www.nngroup.com/articles/the-3cs-of-critical-web-use-collect-compare-choose/).

Second, even if the comprehension scores were comparable on mobile devices and computers, we saw that mobile readers paid a price in reading speeds: when the articles were more difficult, they were slower to achieve the same level of comprehension as on the computer. Thus, **for difficult passages, mobile readers had to work harder than computer readers.** Comprehension scores are just one aspect of task performance; reading speed is another one, and to get a full picture, they must be considered together.

## Recommendations for Mobile Content

We’ve long [advocated brevity in mobile content](https://www.nngroup.com/articles/defer-secondary-content-for-mobile/), and **that rule still stands**. Short, easy passages were faster to read, regardless of the device. That said, **the strict requirement for ultra-short content in mobile may be relaxed** somewhat if the content:

- Is appropriately written for general web audience (no challenging topics or language)
- Serves an entertainment, time-killing, or informative purpose

However, certain sites do offer extremely challenging content, including many organizations within the financial, medical, and scientific sectors; certain government agencies; and B2B sites that target IT or engineering customers. If you’re one of these sites, we highly recommend that you **run your own usability studies of any high-complexity material** you want your readers to access on mobile devices.

Even though mobile reading comprehension for easy articles seems to be comparable with computer comprehension, it doesn’t mean we can ignore the still present [limitations of mobile](https://www.nngroup.com/articles/mobile-ux/).

Most writing on the web is *not* in a linear format—it requires some degree of interactive or comparative effort, which adds to the reader’s [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/). As demonstrated by the speed-accuracy tradeoff, readers will probably need to exert more effort to comprehend difficult subjects on mobile. Many mobile activities are also performed on-the-go, which means environmental conditions will often fragment user attention and focus.

For the majority of mobile content scenarios, **the need for brevity and prioritization is still critical.**

## Reference

R.I. Singh, M. Sumeeth, and J. Miller: "Evaluating the Readability of Privacy Policies in Mobile Environments," International Journal of Mobile Human Computer Interaction, vol. 3, no. 1 (January–March 2011), pp. 55–78.
