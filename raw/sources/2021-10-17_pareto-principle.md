---
title: "Prioritize Quantitative Data with the Pareto Principle"
date: "2021-10-17"
url: "https://www.nngroup.com/articles/pareto-principle/"
author: "Evan Sunwall"
topics: [analytics-and-metrics]
type: article
---

Imagine this: after dozens of meetings with your company's legal, marketing, and engineering departments, you finally have access to an analytics tool. Congratulations! There is a rush of excitement as the UX team dreams of conducting [A/B testing](https://www.nngroup.com/videos/ab-testing-101/) on design improvements or (finally) convincing skeptical stakeholders with [quantitative user data](https://www.nngroup.com/articles/quantitative-studies-how-many-users/').

A few months pass and that initial excitement turns into dismay — there are so many pages, reports, and metrics to consider. The **scope and robustness of analytics tools** can mire any design team with **information overload** and **analysis paralysis**. What can UX professionals do when confronted with so much quantitative data? Consider using the Pareto Principle.

## In This Article:

- [What Is the Pareto Principle?](#toc-what-is-the-pareto-principle-1)
- [How to Create a Pareto Chart](#toc-how-to-create-a-pareto-chart-2)
- [Applying the Pareto Principle in UX](#toc-applying-the-pareto-principle-in-ux-3)
- [Reduce Scope and Increase Impact](#toc-reduce-scope-and-increase-impact-4)
- [The Dangers of Focusing on ONLY 20%](#toc-the-dangers-of-focusing-on-only-20-5)
- [Conclusion](#toc-conclusion-6)
- [References](#toc-references-7)

## What Is the Pareto Principle?

**Definition:** The Pareto principle (also described as the "80/20 Rule") states that 80% of the results come from 20% of the causes.

In the 19th century, the Italian economist and engineer Vilfredo Pareto noticed that 80% of the peas from his garden came from just 20% of the peapods. When he began studying land ownership and wealth inequality, he again noticed that 80% of Italy's land was owned by only 20% of its people. In the 20th century, management consultant Joseph Juran rediscovered Pareto's work and popularized it as the Pareto principle to prioritize investing valuable effort on the "vital few" instead of the "trivial many."

A surprisingly wide range of contexts have demonstrated this 80/20 imbalance:

- 20% of websites capture 80% of web traffic.
- 20% of customers generate 80% of a company's revenue.
- 20% of academic papers make up 80% of all citations.
- 20% of software bugs contribute to 80% of computer crashes.
- 20% of possible openings are used in 80% of chess games.

The Pareto principle is a statistical power law describing a particular [Pareto distribution](https://en.wikipedia.org/wiki/Pareto_principle), a distribution closely related to [Zipf curves](https://www.nngroup.com/articles/zipf-curves-and-website-popularity/). In basic terms, a [power law](https://www.nngroup.com/articles/power-law-learning/) describes a mathematical relationship between 2 variables: one variable is proportional to the other variable raised to a certain power. Examples include y = x2, y = 5x3, or y = 2.5 x-5. A small increase in x leads to a substantial change in y.

The **Pareto principle doesn't predict when** this phenomenon happens, nor does it explain why it happens. Also, **there's no guarantee your data will neatly follow an 80/20 distribution**. For instance, 5% of your web pages may be responsible for 67% of all pageviews and, in many social media, [1% of users account for 90% of postings](https://www.nngroup.com/articles/participation-inequality/). What's important is the magnitude of the imbalance between the 2 values and not their exact numbers. Think of the Pareto principle as a helpful observation that **inputs and outputs are often not evenly distributed**. A large group may contain only a few meaningful contributors to the desired outcome.

## How to Create a Pareto Chart

A Pareto chart is a data visualization illustrating which categories (e.g., different pages) are the most significant contributors to a given metric (e.g., number of page views).

![Example of a Pareto chart](https://media.nngroup.com/media/editor/2021/10/06/pareto-chart.jpg)

*In this Pareto chart example, the X-axis displays the website’s pages (ordered in decreasing order of page views). The left Y-axis is used for the bars, which represent the number of page views for each page. The right Y-axis is used for the line, which represents the cumulative contribution of each page to the total percentage of page views. In other words, the point on the line that corresponds to page E is the percentage of page views (out of the total number of page views) received by page E and by all the preceding pages (K and B). The last point on the line should always be 100%. Based on this chart, although this website has multiple pages, researching and implementing UX improvements for pages K, B, E, and A should influence about 80% of the website's total page views and, thus, have the highest return on investment.*

A Pareto chart contains two different plots in the same visual:

1. A bar plot that graphs the metric by category (in our example, the page views per page)
2. A line plot that graphs the cumulative percentage of the metric by category (in our example, the percentage of the page views due to the current page and to all the pages with larger pageview counts)

Creating your own Pareto chart requires making a simple table of categorical values, their numerical values for the metric of interest, and few calculated values. Before you begin, always start with a goal and a hypothesis that you want to investigate. Check if the required data exists, is exportable from the system storing it, and is free of redundancies or errors. You may find that a lot of cleanup and compiling of the data is necessary before creating the table below.

![A spreadsheet of 4 column containing data: Page (column A), Page Views (column B), Percent of Total (column C), Cumulative Percent of Total (column D)](https://media.nngroup.com/media/editor/2021/10/06/spreadsheet.jpg)

*The spreadsheet used to generate the Pareto chart above.*

Here are the steps for creating a Pareto chart:

1. **Choose a****descriptive****category** such as web pages, features, user segments.
2. **Choose a****numerical****metric** to compare across your categories, such as cost, page views, number of clicks.
3. Start with a blank spreadsheet.
4. In column A, **list all category values**. For example, if your category is pages, list all pages.
5. In column B, next to each category, **list the value of the metric****for that category.** For example, for each page, list the corresponding number of page views next to it.
6. Sum column B at the bottom of the table to get the **total counts** for all the members of the category. In our example, the sum would represent the total number of page views received by all pages.
7. **Sort the table** by the metric column from **highest to lowest**.
8. For column C, **calculate the percentage** that each category contributes to the total counts. To do that, take the value in column 2, divide it by the total-counts sum from step 6, and multiply by 100. This column should add up to 100%.
9. For column D, calculate the cumulative percentage for each category by **adding that item’s percentage with the percentages of all items above it** in the table.
10. On the same graph, create a bar chart corresponding to column A and B and a line chart for columns A and D. (You can also create two separate charts — one for the bar plot and another one for the line plot — or just the line plot based on columns A and D; even though technically the result will not be a Pareto chart, the information conveyed will be the same.)

Pareto charts are useful prioritization aids as they help you easily identify the biggest contributors to a metric. Microsoft Excel supports creating Pareto charts, but you can also create them in other data-visualization or spreadsheet applications.

## Applying the Pareto Principle in UX

Here are two situations where the Pareto Principle can help UX professionals set priorities from their data.

**Example 1:** An app's customer-satisfaction rating is sagging due to accumulated technical and [UX debt](https://www.nngroup.com/articles/ux-debt/).

**Goal**: Improve the UX of the app by fixing the most significant UI issues.

**X-axis category:** Product features

**Y-axis measure:** Number of negative user-feedback submissions

**Pareto analysis**: Just 3 features are responsible for 86% of feedback submissions.

**Key insight**: Improving these 3 features should disproportionately impact the feedback submission.

**Action**: [Persuade stakeholders](https://www.nngroup.com/1-hour-talks/presenting-stakeholders/) to invest effort in these 3 features, despite other features having more obvious and easier to implement fixes.

**Example 2**:**** Fewer users have signed up for a free product trial since a website redesign.

**Goal**: Improve the free-trial rate (a [micro-conversion goal](https://www.nngroup.com/articles/micro-conversions/)), which contributes to customer acquisition (a [macro-conversion goal](https://www.nngroup.com/videos/macro-microconversions-metrics-analytics/)).

**X-axis category:** Web pages visited by users who signed up for the trial

**Y-axis measure:** Number of unique page views

**Pareto Analysis**: 77% of this user segment visited a page describing your product's features and pricing.

**Key Insight**: Reducing the [exit rate](https://www.nngroup.com/videos/bounces-vs-exits-analytics/) of the pricing page should disproportionately improve the trial rate.

**Action**:**** Prioritize a qualitative-research project to [triangulate](https://www.nngroup.com/articles/triangulation-better-research-results-using-multiple-ux-methods/) the underlying issues with this pricing-plan page, even though other pages have higher exit rates.

## Reduce Scope and Increase Impact

UX teams generally have scarce resources, insufficient time, and a need to demonstrate business value to the organization. In environments with [low UX maturity](https://www.nngroup.com/articles/ux-maturity-model/), just gaining access to analytics can require spending valuable political capital. By leveraging the Pareto principle's scaling effect, a UX team can quickly realize many benefits, such as:

- Filter through the volume of analytics data
- Persuade stakeholders on the potential [return on investment of a UX project](https://www.nngroup.com/videos/calculating-roi-design-projects/)
- Reduce research and implementation scope
- Achieve impactful results efficiently

## The Dangers of Focusing on ONLY 20%

It can be **tempting to misuse** the Pareto Principle and **ignore 80% of your user experience**. Even Joseph Juran recognized this problem and revised his original description of the Pareto Principle from "the vital few and the trivial many" to "the vital few and the useful many." Investing exclusively on the 20% for too long can lead to **stagnation** and **overoptimization of a few metrics** to the detriment of others. It can also reinforce stakeholder beliefs that just a few metrics should drive product vision and design work. Avoid this trap of all-or-nothing thinking. Reserve some bandwidth for studying other parts of your user experience, which may have a significant aggregated impact on different metrics or provide needed utility for users.

If we take the Pareto Principle literally, then there is still 20% of total UX value to be derived from the 80% less-used or less-important elements of your design. We don’t want to leave that 20% on the table; we simply want to prioritize the higher-potential gains.

## Conclusion

Although analytics tools capture vast amounts of behavioral data from your website or app, not all parts of the user experience contribute equally to the bottom line. Leverage the Pareto principle by first confirming your organization's goals, the metrics that measure them, and the [user data aligned to those goals](https://www.nngroup.com/articles/ux-goals-analytics/). Then focus UX research and design efforts on those areas contributing significantly to those business metrics. Even **minor improvements to these vital areas** can generate **disproportionately powerful results**.

Learn more by taking our full-day course [Analytics and User Experience](https://www.nngroup.com/courses/analytics-and-user-experience/).

## References

1. Juran. 2019. Pareto principle (80/20 rule) & pareto analysis guide. (March 2019). Retrieved September 13, 2021 from [https://www.juran.com/blog/a-guide-to-the-pareto-principle-80-20-rule-pareto-analysis/](https://www.juran.com/blog/a-guide-to-the-pareto-principle-80-20-rule-pareto-analysis/%C2%A0)

2. Lada Adamic and Bernardo A. Huberman. 2000. The nature of markets in the World Wide Web. *SSRN Electronic Journal*(2000). DOI: [https://dx.doi.org/10.2139/ssrn.166108](https://dx.doi.org/10.2139/ssrn.166108)

3. M.EJ Newman. 2005. Power laws, pareto distributions and Zipf's law. *Contemporary Physics* 46, 5 (2005), 323–351. DOI: [https://dx.doi.org/10.1080/00107510500052444](https://dx.doi.org/10.1080/00107510500052444%C2%A0)

4. Richard Koch. 2017. *The 80/20 principle: The secret of achieving more with less*, London: Nicholas Brealey Publishing.
