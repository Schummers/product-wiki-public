---
title: "Choosing Chart Types: Consider Context"
date: "2022-01-30"
url: "https://www.nngroup.com/articles/choosing-chart-types/"
author: "Kate Moran"
topics: [visual-design]
type: article
---

[Quantitative UX data](https://www.nngroup.com/articles/quantitative-user-research-methods/) can be incredibly powerful. It can help us make decisions, end arguments, or even prove the value of our work. However, I often find that many UX professionals struggle to present their data. In particular, they rarely put together compelling, easy-to-interpret charts.

You don’t have to have extensive [visual-design](https://www.nngroup.com/topic/visual-design/) skills to create good charts from your analytics data or other quantitative UX data. Simply apply the same user-centered–design approach that you would use when designing an interface.

Consider **one key question** before you begin designing your chart: **What is your goal?**

In other words, what point are you trying to make? What do you want your audience to understand when they look at your chart? What action do you want them to take?

Once you’ve answered that question, tailor your chart to fit that goal (while not misrepresenting or falsifying the data, of course).

### What This Article Does (and Does Not) Cover

This article focuses on explanatory data visualizations — communicating a finding to teammates, stakeholders, or clients. You will likely need to create different types of charts to explore your data during the analysis process.

Also, this article discusses charts, not [infographics](https://www.nngroup.com/articles/designing-effective-infographics/), which usually combine multiple visuals and data visualizations to tell a story. In addition, this article doesn’t [cover dashboard](https://www.nngroup.com/articles/dashboards-preattentive/) designs.

## In This Article:

- [The 3 Cs for Better Charts](#toc-the-3-cs-for-better-charts-1)
- [Context](#toc-context-2)
- [Choosing a Chart Type](#toc-choosing-a-chart-type-3)
- [Conclusion](#toc-conclusion-4)
- [Recommended Reading](#toc-recommended-reading-5)
- [Inspiration](#toc-inspiration-6)
- [References](#toc-references-7)

## The 3 Cs for Better Charts

The 3 Cs are an easy way to remember the most important aspects of any good chart:

- **C** ontext
- **C** lutter-free
- **C** ontrast

We explore each of these factors in **a three-part series.** This article discusses the importance of context in data visualization and how context can help you decide which type of chart to create.

## Context

Numbers are meaningless without context. If I told you that the completion rate for checking out in an ecommerce app was 24%, what would that mean? Nothing, unless I also told you that the completion rate had been 17% in the previous year. **People need to compare a number against another number in order to interpret it.**

In UX, we often compare data points collected at different **times.** For example, we could compare our completion rate for this year against our completion rate for the past 3 years. Or, we could look at completion time for an important task before and after a redesign.

Sometimes, instead of comparing two versions of the same product at different times, we **compare similar products, features, content, or user groups**. For example:

- A company’s product against a competitor’s product
- One company’s product against the rest of its family of products
- One feature against several other key features
- One webpage against other webpages using the same page template
- One very popular article against other articles on the same topic
- The performance of one task against other key tasks
- The performance of one group of users against another group

When comparing numerical data, it’s important to **be familiar with at least the basics of**[experimental design](https://www.nngroup.com/articles/internal-vs-external-validity/)**and statistics**— particularly confidence intervals and statistical significance. Our full-day course [How to Interpret UX Numbers](https://www.nngroup.com/courses/ux-statistics/) covers how these concepts apply to UX research.

## Choosing a Chart Type

There are many of different types of charts, but, for most UX purposes, we recommend the basics: bar charts, line charts, or scatter plots. Choose the chart that best suits your goal and the context you’re presenting.

### Bar Charts

For most of these common UX comparisons, the **bar chart** (sometimes called a column chart) works well. Researchers have found that bar charts are much easier for people to comprehend than other types of charts (like pie charts). This is because bar charts make it easy for people to quickly and accurately perceive the differences between values.

**Good:***A classic for a reason — simple bar charts are quickly processed and understood. This example shows the different conversion rates before and after a redesign, with the goal of communicating the redesign’s success.*

### Paired Bar Chart

A **paired bar chart** shows two data series side by side — for example, data about two different user groups, designs, or devices.

Let’s imagine we recently redesigned a website that sells home furniture. We have two primary user groups — people who buy furniture for their own homes (*Consumers*) and people who buy furniture for their clients (*Interior**Designers*). We collect the average order value (AOV) for each group before and after the redesign; essentially, this number shows how much money we make from the average purchase.

In this case, we have two variables (user group and time) with two levels each, resulting in four datapoints we want to compare:

- AOV for *Consumers***before** the redesign
- AOV for *Consumers***after** the redesign
- AOV for *Interior******Designers***before** the redesign
- AOV for *Interior******Designers***after** the redesign

This is a great opportunity for a paired bar chart, but we have to decide how to group the data. We can either group the bars by time (before vs. after) or by user group (*Consumers* vs. *Interior**Designers*).

Many people would opt to group them by time. (In one of my training courses, attendees often pick this grouping in a similar activity.) However, it’d be a mistake to group the bars by time in this case. To see why, take a look at the chart below.

**Bad:***In this example, the bars are grouped by time (* Before *vs.* After *). While that might feel logical, it makes it more difficult to see the point of the data — which is to show the impact of the redesign on each group (rather than the difference between the types of users).*

Think about our objective in this example — to show the differences before and after the redesign for each user group. **What comparison do you want people to make?** Put those things close together, so your viewers easily see them side by side and understand your main point. In the above chart, the easiest comparison is between consumers and interior designers: it’s very clear that the professionals buy more than the amateurs. But this isn’t the most important point.

**Good:***Grouping the bars by user type works better for this chart’s goal. We can flick our eyes between the* Before *and* After *bars for each group and quickly understand the difference.*

In a case like this one, we could simplify the chart even more by showing only the percent increase in order value for each user type. The result would be a simple bar chart with a single series. This approach does more of the work for the viewers — they don’t have to visually estimate those differences on their own.

*Consider whether you need a paired bar chart or if you can simply show the differences of interest, as in this example.*

A **horizontal bar chart** is a good option when you’re working with long labels — for example, feature names or task descriptions. The horizontal orientation allows you to display the labels without abbreviating or rotating them, as would be necessary with a vertical bar chart.

**Bad:***When visualizing UX data, we often deal with long labels (such as feature names or task descriptions). Placing labels in vertical or diagonal alignment makes them hard to read.***Good:***Horizontal bar charts are a good option when your items have long names. In this example, four short task descriptions are listed. These labels are more meaningful than shorter abbreviations (such as* Task 2 *or* Download *) and easier to read than vertical text labels. The goal for this example chart is to highlight that the task* Find bill from May 12 *has a much lower success rate than the other tasks in the study and needs to be investigated through a qualitative study.*

Another popular variation is the **stacked bar chart**. I often see this option used for [task-success levels](https://www.nngroup.com/articles/success-rate-the-simplest-usability-metric/). For example, such a chart could show, for each task, the breakdown of users who were successful on their own, successful with help from the facilitator, or failed the task.

In the previous horizontal bar chart example, we showed only the success rates for each task. Now, let’s include success with help and failures in a stacked bar chart.

*This stacked bar chart shows, for each task, the percentage of participants who were successful on their own, successful with help from the facilitator, or failed the task.*

The example above illustrates one of the key problems with the stacked bar chart. It’s easy to compare the *Success* bars shown in green, because all four bars are aligned on the x-axis at 0%. (Similarly, it’s reasonably easy to compare the *Fail* bars, which are all right-aligned.) However, it’s much harder to compare the *Success with Help* bars in yellow, because they don’t have the same starting point.

Also, notice that the stacked bar charts don’t allow you to show [confidence intervals](https://www.nngroup.com/articles/confidence-interval/) (or any other type of error bars) — which are important for making sound numerical comparisons.

Research shows that stacked bar charts are in fact very hard to understand — they are among the charts with the highest error rates. That is why we strongly recommend that you stay away from them. Simply use a series of 3 bar charts instead (or even 3 different charts if you want to emphasize, for instance, that one task benefits from facilitator intervention than others.)

### Line Charts

If you want to show a data trend over time, a **line chart** will work better than a bar chart. For line charts, use data-point markers to clarify where in the timeline you collected data.

*This line chart shows the trend of one company’s CSAT scores over a five-year period. Each data marker (blue dot) shows when the data was collected.*

### Scatterplot

Finally, a **scatterplot** can work in situations where you want to show the relationship between two variables. Scatterplots look like line charts, but the points are not connected with lines.

For example, to show that a few of the features in an app are used most frequently by the majority of users, we might show each feature as a dot plotted against the percentage of accounts that use each feature (x-axis) and the average amount of times the feature is used by each user in a month (y-axis).

*This scatterplot displays how much an app’s features (dots) are used by its users. The x-axis shows what percentage of user accounts have used the feature, while the y-axis shows the average amount of times each user has used the feature in the past 30 days. This chart might be used to argue for prioritizing these 3 most-popular features.*

### Chart Types to Avoid

Researchers have found that bar charts, line charts, and scatter plots are easiest to understand.

Other chart types require users to visually assess angle, area, or volume to understand the data. These tend to be much more challenging for people to process and include:

- Pie charts
- Bubble charts
- Mosaic charts
- Unit or waffle charts
- Sankey diagrams or dendrograms
- Stacked area charts

Just because they’re trickier to read, that doesn’t mean you can't ever use them. But before choosing one of these, go back to your goal: What are you trying to communicate? Is one of these more-complex visualizations adding value to your message? If your goal can be achieved with one of the basic charts, opt for them.

For example, many analytics and information-architecture testing tools use dendrograms to illustrate navigation flows. Those charts are good for indicating clusters of objects; the same information would be challenging to present with a bar or line chart. Also, typically those tools use dendrograms for exploring data and conducting analysis — not for presenting findings or recommendations to stakeholders.)

## Conclusion

Provide context for your data points by including relevant comparisons. Decide which type of chart to use based on the data type you’re working with and the comparison you’d like to present.

The **next article** in series explains [how to keep your charts clean and focused](https://www.nngroup.com/articles/clutter-charts/) by removing unnecessary elements.

## Recommended Reading

The following books and websites are good references on how to design great charts. These books provided inspiration for this article series.

**Better Data Visualizations: A Guide for Scholars, Researchers, and Wonks by Jonathan Schwabish**

Schwabish’s book provides concrete guidance on when to use each type of chart (from basic charts like bar charts to more obscure options like violin charts and treemaps). He provides detailed advice on how to design each type. Schwabish’s book is written in plain language and should be approachable for all experience levels.

**Storytelling with Data: A Data Visualization Guide for Business Professionals by Cole Nussbaumer Knaflic**

Nussbaumer Knaflic’s guide advocates for applying a design mindset to your data visualizations — starting from a clear understanding of your audience and your objective. The book goes beyond data visualization to consider the story you build around your data.

**The Visual Display of Quantitative Information******by Edward R. Tufte**

As a data visualization classic, Tufte’s book elevates this “boring” topic to an art form. Tufte assembles a diverse collection of data-visualization examples from a variety of fields, countries, and centuries. While this book may be less practical and applicable than the others listed here, I highly recommend it to anyone deeply interested in data visualization.

## Inspiration

For more inspiration, explore the websites of these organizations that excel (pun very much intended) at communicating quantitative data.

[Pew Research Center](https://www.pewresearch.org/)

Pew conducts large-scale surveys and publishes reports. Each of Pew’s charts focuses on clearly communicating a single finding from their enormous data sets.

[FiveThirtyEight](https://fivethirtyeight.com/)

Every article on politics, economics, or sports that FiveThirtyEight publishes contains at least one chart, and some of them are interactive.

[The Washington Post](https://www.washingtonpost.com/)

This American newspaper’s site often provides innovating interactive data visualizations focusing on current events.

[The Economist](https://www.economist.com/)

You don’t have to know much about economics to appreciate these brilliant charts. (Unfortunately, you do have to be a paying Economist subscriber.)

[Wired Magazine](https://www.wired.com/tag/charts/)

Wired publishes interesting charts on variety of technology-adjacent topics. If you happen to have a Wired or Apple News+ subscription, check out the *Chartgeist* column in the magazine, which features comedic charts (they’re funnier than they sound).

## References

Nussbaumer Knaflic, C., 2015. *Storytelling with Data: A Data Visualization Guide for Business Professionals,* Wiley.

Tufte, E., 1983. *The Visual Display of Quantitative Information,* Graphics Press.

Heer, J. and Bostock, M. and Ogievetsky V., 2010. A Tour Through the Visualization Zoo, *ACM.*

Schwabish J., 2021. *Better Data Visualizations: A Guide for Scholars, Researchers, and Wonks,* Columbia University Press.

Cleveland W. and McGill, R., 1984. Graphical Perception and Graphical Methods for Analyzing Scientific Data, Journal of the American Statistical Association.
