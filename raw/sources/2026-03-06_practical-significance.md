---
title: "Statistical Significance Isn’t the Same as Practical Significance"
date: "2026-03-06"
url: "https://www.nngroup.com/articles/practical-significance/"
author: "Rachel Banawa"
topics: [research-methods]
type: article
---

When you run a quantitative usability study or analyze a survey, it’s tempting to get excited when a result is statistically significant. But before you celebrate, pause: statistical significance doesn’t automatically mean the result matters in practice.

In UX research, what’s statistically significant might not be meaningful to users, product teams, or business outcomes.

## In This Article:

- [What Is Statistical Significance?](#toc-what-is-statistical-significance-1)
- [Statistical Significance May Not Matter](#toc-statistical-significance-may-not-matter-2)
- [What Is Practical Significance?](#toc-what-is-practical-significance-3)
- [The Role of Sample Size](#toc-the-role-of-sample-size-4)
- [How to Evaluate Practical Significance](#toc-how-to-evaluate-practical-significance-5)
- [Combining Both Perspectives](#toc-combining-both-perspectives-6)

## What Is Statistical Significance?

Statistical significance answers the question: **Is this result likely due to chance?**

> **Statistical significance** means that a result is unlikely to have occurred by chance. More specifically, the probability of that result being due to chance (also known as the p-value) is less than a preset threshold (usually 0.05).

When you run a statistical-significance test — say, comparing [conversion rates](https://www.nngroup.com/articles/conversion-rates/) between two webpages — you’re testing whether the difference you see could have appeared randomly. If the test returns a p-value that is less than .05, that means that the result is statistically significant, suggesting that the difference is unlikely to be random.

In other words, if you ran the same experiment many times under similar conditions, you could reliably expect to still see a similar result.

That’s all statistical significance means. It says nothing about how large, valuable, or noticeable the effect is to users or the business.

## Statistical Significance May Not Matter

Here’s an example. Let’s say you run an [A/B test](https://www.nngroup.com/articles/ab-testing/) comparing the completion rates between two checkout flows.

- Design A: 85.0% completion rate
- Design B: 85.2% completion rate

You run a statistical test to see if the difference between the two completion rates is statistically significant, and you get a p-value of 0.03.

Because that p-value is less than 0.05, that difference in the completion rates is statistically significant. This means that if we were to hypothetically run this same study again, we can expect to get a similar result. **That reliability is valuable because it tells us the pattern we’re seeing is real.** We’re not just seeing it out of pure luck.

![Two boxes. First one says: Design A Completion Rate 85%. Second one says: Design B Completion Rate 85.2%. Below it says: P-Value = .03 Statistically Significant.](https://media.nngroup.com/media/editor/2026/02/16/practical-significance-image.png)

*With a p-value of 0.03, the small difference between the two checkout designs is statistically significant, meaning the pattern is unlikely to be due to random chance.*

However, **reliability and impact are not the same thing.** In this example, the completion rate for design B is higher than design A by just 0.2%. We also need to ask whether the effect is big enough to matter.

Statistical significance doesn’t tell us whether that difference is noticeable to users, meaningful for the experience, or influential for the business. That’s why we need to also look at practical significance — to decide whether a statistically reliable result is worth acting on in the real world.

## What Is Practical Significance?

[Practical significance](https://www.nngroup.com/videos/practical-vs-statistical-significance/) asks a different, more applied question: **Is this result big enough to matter in real life?**

> **Practical significance** is when the size of an observed difference is large enough to meaningfully impact real-world decisions, user experience, or other outcomes.

Even if a result is statistically significant, the effect might be too small to justify a design change — meaning, it doesn’t have practical significance.

Let’s say you test two checkout designs and find that design B reduces average time on task from 55 seconds to 54 seconds.

With a large enough sample, that 1 second difference might be statistically significant, but does it meaningfully improve user experience or business metrics in the real world? Probably not, especially if the improvement demands extra engineering work, risks introducing new bugs, or adds unnecessary friction to the design for a barely noticeable speed boost.

Conversely, an effect that is not statistically significant may be large enough to trigger concern. For example, if a small-sample [quantitative usability test](https://www.nngroup.com/articles/usability-testing-101/) shows a 80% drop in task completion after a layout change, it might be a good idea to do further investigation or testing, even if that result did not reach statistical significance.

Importantly, this also means that not everything that matters in UX can — or should — be reduced to a p-value. Many impactful UX insights come from qualitative studies: watching users struggle, listening to their reasoning, or noticing patterns in behavior that don’t require large samples or statistical tests to be compelling. Statistical significance is useful, but it’s only one piece of the evidence puzzle.

## The Role of Sample Size

### 1. Large Sample Sizes Can Make Small Differences Look “Significant”

When you’re working with a large quantitative dataset — for example, analytics data from thousands or even millions of sessions — **even tiny differences can show up as statistically significant.**

For instance, imagine your product team tweaks a form field and errors drop by 0.03%. With a massive sample size, that microscopic change might produce a p-value below 0.001, signaling statistical significance.

But would anyone notice that difference of 0.03% in real-world use? In this particular case, probably not. Practically speaking, a decrease of 0.03% is so small that the experience is effectively the same.

**The ability to detect a statistically significant result improves as sample size grows**, even if the impact is trivial. **Practical significance, on the other hand, is about the actual size and impact of that effect** — not whether statistical formulas say it’s unlikely to be due to chance.

Both concepts are important in UX research, but they serve different purposes. Large datasets make it especially easy to misinterpret “statistically significant” as “important.” So, whenever a result is statistically significant, it’s critical to also ask: Is this difference meaningful enough that it would affect users?

### 2. Small Sample Sizes Can Hide Meaningful Patterns

Sometimes due to time or budget constraints, we can manage to gather only a small sample size, such as less than 15 participants. **With samples this small, it’s extremely difficult (and sometimes impossible) to achieve statistical significance.** The math simply isn’t on our side. This is because small samples are more vulnerable to noise, outliers, and idiosyncratic behavior from a few participants.

However, there are some cases where a small-sample quantitative study can still point to practical significance. For UX teams with limited time and budget, this is an important consideration.

This tends to happen when the pattern is unusually large and consistent. For example, imagine you’re testing two new dashboard layouts with 12 people. If 10 out of the 12 people fail to complete a task on dashboard A, while only 1 out of 12 people fail on dashboard B, that difference may not be “statistically significant,” but it’s difficult to dismiss from a practical standpoint. The magnitude of the gap suggests that dashboard A is not adequately supporting users.

This is where practical significance helps us fill in the gaps, especially if we’re able to couple quantitative results with qualitative evidence. It encourages us to look at the magnitude and meaning **** of what we’re observing. If users are consistently confused, stuck, or making the same mistake, that’s meaningful evidence worth paying attention to.

## How to Evaluate Practical Significance

When evaluating practical significance, it’s key to remember that **practical significance is context dependent.** A small numerical difference can matter a lot, or not at all, depending on scale. For example, imagine a design change increases revenue by $2 per conversion. If your average conversion is worth $1,000, that $2 increase could become substantial when multiplied across thousands or millions of conversions each year. But if each conversion is already worth $1,000,000, that same $2 increase is likely negligible.

Here are 3 ways UX teams can evaluate practical significance.

### 1. User Perception

Ask: **Would real users actually notice this change?**

Even if a result is statistically significant, it may not meaningfully affect the experience. Consider:

- Would users feel the interface is faster or smoother?
- Would this reduce frustration, hesitation, or confusion?
- Would the change meaningfully alter behavior in the product?

For instance, imagine a redesign that technically makes a page load 8 milliseconds faster. Statistically, that difference might show up as “significant”, but no human is going to consciously perceive an 8-millisecond improvement in this context. To users, the page will feel exactly the same. If the effect is too small for people to perceive, it may not be worth prioritizing.

### 2. Business Value

Ask: **Does this difference matter to the organization?**

A result can be practically significant if it affects important business outcomes. Consider:

- Does it save time, money, or support resources at scale?
- Does it reduce errors or abandonment in a high-stakes workflow?
- Does it improve key metrics (such as conversion, retention, task success) enough to justify implementation?

Small improvements can compound in high-volume contexts, while larger improvements may be irrelevant if they don’t support strategic goals.

For example, imagine a change that reduces checkout errors by just 0.5%. On its own, that might sound small. But if your product processes 2 million checkouts per year, that’s 10,000 fewer failed transactions. If each failed checkout costs the business $15 in lost revenue or support time, that small improvement translates to $150,000 per year.

In this case, the effect might feel subtle to individual users, but at scale it has clear, practical value for the business and it is worth prioritizing.

### 3. Effect Size

Effect size is a statistical calculation that tells you how big or meaningful a difference actually is. If user impact and business value are obvious, you may not need a formal effect-size calculation. Effect sizes become most valuable when results are ambiguous, tradeoffs are costly, or when you need a defensible, quantitative way to communicate magnitude to stakeholders.

There are different ways to calculate effect size depending on your data type. While a discussion of these techniques is beyond the scope of this article, methods include [Cohen's d, risk ratios, odds ratios, or correlation coefficients](https://en.wikipedia.org/wiki/Effect_size).

## Combining Both Perspectives

The best UX researchers look at **both** statistical and practical significance:

- Statistical significance ensures your findings aren’t random.
- Practical significance ensures your findings are worth acting on.

Together, they balance confidence with impact, ultimately grounding design choices in data that truly matter.

### Conclusion

In UX research, statistical significance and practical significance answer different but equally important questions. Statistical significance indicates whether a result is likely real, while practical significance helps us decide whether it’s worth acting on. Focusing on only one can lead to wasting resources on trivial changes or overlooking meaningful usability problems. By pairing p-values with practical significance, UX teams can make confident, balanced decisions and prioritize changes that are not just statistically reliable, but genuinely improve the user experience and drive business value.
