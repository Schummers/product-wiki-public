---
title: "Understanding User Pathways in Analytics"
date: "2022-10-16"
url: "https://www.nngroup.com/articles/analytics-pathways/"
author: "Page Laubheimer"
topics: [analytics-and-metrics, customer-journeys]
type: article
---

Understanding [users’ journeys](http://www.nngroup.com/articles/journey-mapping-101/) is one of the key insights that UX practitioners seek: if we know how our users move through our websites and what steps they take to satisfy their goals, we can better support them. Analytics tools often promise to reveal user journeys and offer dedicated tools for displaying how users move through a website.

However, understanding the [user’s journey requires more data](https://www.nngroup.com/articles/research-journey-mapping/) than analytics alone can provide — analytics cannot tell us each user’s specific goals or expectations and certainly cannot provide us with the rich [qualitative](https://www.nngroup.com/articles/quant-vs-qual/) details like their thoughts and feelings that make journey mapping such a valuable exercise. But, while you wouldn’t make a whole meal from just garlic, garlic certainly is a valuable ingredient; so, too, is analytics a key ingredient in understanding common user journeys.

What type of information does analytics provide? Analytics can reveal the most common **pathways** between pages — in other words, it can show us where most people start in our product or app and the pages or screens (or even features) they interact with next. These pathways are usually visualized in a Sankey diagram.

Definition: A **Sankey diagram** is made up of **nodes** (usually corresponding to pages, screens, or use of a feature) connected through **links** that indicate how people move from one node to the next. The width of the link indicates the amount of traffic that moves between those nodes.

![A Sankey diagram from Amplitude showing several columns of user data connected with arrows showing the relative volume of traffic](https://media.nngroup.com/media/editor/2022/10/18/amplitude-sankey.png)

*A Sankey diagram from Amplitude shows the common user flows within an app. The overlapping pathways can make it challenging to interpret.*

While Sankey diagrams may look overwhelming, the basic concept is simple: they flow from left to right, showing a sequence of steps in columns, with each successive column representing the first, second, third (and so on) node viewed.

In each column, the nodes are ordered according to the traffic they get — with the highest one at the top. At the bottom of the column, the diagram indicates the number of dropoffs (users who exited the site or application). From each node, there are links connecting it to the next node that users viewed. The width of each link visualizes the number of users that traveled between those nodes, so that you can quickly identify common pathways.

## In This Article:

- [Limitations of Analytics-Based Pathways](#toc-limitations-of-analytics-based-pathways-1)
- [Tips for Interpreting Analytics-Based Pathways](#toc-tips-for-interpreting-analytics-based-pathways-2)
- [Summary](#toc-summary-3)

## Limitations of Analytics-Based Pathways

One important point is that these user-flow diagrams aggregate (often dissimilar) traffic data. While many analytics platforms will allow you to dive into specific users’ sessions to some degree, the tools are built to present large-scale data. They **show trends rather than individual-user’s movement** through the site. That is, they reveal the most common first steps, second steps, and so on. They compile users who may have had different intentions, goals, and information needs. Therefore, they do not represent real *user**journeys.*

Since analytics cannot [directly observe what’s going on in users’ heads](https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/), we have **no reliable way to segment this traffic by what the user was interested in.** Two people with the exact same behavior may have had wildly different experiences. For example, on a search-results page two people may exit the site without clicking on any of the result links; one may have left out of frustration with the irrelevant results, the other may have got an answer to their question without clicking any links (an example of [good abandonment](https://www.nngroup.com/articles/good-abandonment/)). These two wildly different experiences will look identical in path reports, because we don’t know what each user was trying to achieve.

## Tips for Interpreting Analytics-Based Pathways

Because Sankey diagrams can be challenging to interpret, here are a few suggestions for how to analyze them effectively.

### Filter the Flow Data

Because flow diagrams display a large amount of data, it can be overwhelming to make sense of what is happening. A key recommendation is to filter this data down into meaningful chunks to make the interpretation process easier.

If you were to watch all the traffic in a city moving at the same time, it’d very hard to see patterns unless you focused in on a single stream of traffic and paid attention to the details. How many people entered the highway via a specific ramp during rush hour? Where did they come from before merging onto the highway? If we follow them for a bit, where do they exit the highway? Was there a big traffic jam when a bunch of entering traffic met up with a bunch of traffic trying to leave in the same few exits? A transportation engineer will take that traffic data to investigate how to solve congestion problems. In user experience, while we don’t manage traffic jams very often, we are trying to get people to their destination with the lowest amount of effort (in terms of [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/), [working memory load](https://www.nngroup.com/videos/working-memory-external-memory/), and [interaction cost](https://www.nngroup.com/videos/interaction-cost/)), so knowing those common connections is still absolutely vital.

Since there are so many journeys all superimposed in these diagrams, you can’t typically review *all* of them. So, instead, focus on key pages or screens as your starting point for analysis. Make liberal use of the feature that allows you to hide everything except traffic flowing through a specific page. This feature allows you to highlight one node and see where users came from when they arrived at that node and then where they went afterwards.

![A sankey diagram that has been filtered to show only data through a specific node](https://media.nngroup.com/media/editor/2022/10/18/mixpanel-path-report.png)

*By isolating or highlighting just the traffic flowing through a specific node as seen in this example from Mixpanel, it is easier to see the where the traffic to this node originated and the distribution of next steps. Without isolating that node’s traffic, the number of overlapping pathways makes analyzing this data more challenging.  ( Image source )*

It’s also worth taking the time to filter this data by user [segments](https://www.nngroup.com/articles/analytics-persona-segment/). Are the common pathways different on mobile vs desktop? How about for users that have completed key goals, such as conversions, purchases, or even important feature usage? What do the pathways look like for users that interacted with your search as compared to those that didn’t, for example?

### Review Key Touchpoints

**Review the first nodes that users encounter.** While a lot of traffic will start on the homepage, many of your users’ first impressions are on internal pages. Take a look at those popular internal pages — do they clearly indicate the purpose of the site and do they feature understandable [orientation, navigation, and wayfinding](https://www.nngroup.com/articles/navigation-you-are-here/) options to other key areas? Do these pages surface up links to key offerings, content, and features? Is the [dropoff rate](https://www.nngroup.com/videos/bounces-vs-exits-analytics/) from any of these landing pages higher than from others? That’s an indication that there may be issues with the content of that page.

Examine each of the common non-homepage starting pages individually and where users went next. You can use this information to make hypotheses about what information needs users had; just be aware that this exercise will often have relatively obvious insights — most users will follow prominent links on the page.

**Investigate which nodes are encountered at users’ second step.** Look for patterns such as a high dropoff rate after the second interaction. Such data could be the only sign you get of problems such as the lack of [deep linking](https://www.nngroup.com/articles/deep-linking-is-good-linking/) after a login page. For example, a user of a meal-kit delivery service might get a weekly email reminder to choose their recipes. They click that link and are asked to log into their account before proceeding. After logging in, they are unceremoniously redirected back to the homepage with no obvious way to get to the promised customized content from the email. The user sighs with frustration and proceeds to close the browser tab, rather than hunt around for the page offered up in the email.

**Compare related links to actual next paths.** Looking at the list of next steps can also identify places where algorithmically generated [related-content links](https://www.nngroup.com/articles/related-content-pageviews/) or [personalized](https://www.nngroup.com/videos/personalization-customization/) information [aren’t really relevant](https://www.nngroup.com/articles/recommendation-guidelines/) to users. To do this, however, you’ll need to compare the related links on each of those nonhomepage starting pages to the pages where users *actually* went next. If there’s a big difference, ask yourself why.

**Review hub pages.** Hub pages **** are nodes with a lot of traffic coming into and out of them; they are typically routing pages that function like a form of navigation. Look for [pogo sticking](https://www.nngroup.com/articles/pogo-sticking/): places where users come back to the same hub page over and over. This pattern can indicate a frustrating experience while the user is trying to locate a known item, but it can also be a sign of high engagement and enjoyable exploration. Consider using the path report to identify pogo-sticking locations and do some qualitative user testing to find out why it’s occurring.

### Start from the End of the Flow

Another technique for investigating pathways is to begin your analysis by looking at the **end** of the flow, not at the beginning. (However, not all analytics tools may have this capability.) Start from a key goal you have for users — such as signing up for a service, purchasing something, filling out a lead-generation form, or interacting with a feature meant for power users. Then move backwards to see how users made their way to that goal. This approach can reveal how [discoverable](https://www.nngroup.com/videos/findability-vs-discoverability/) advanced features are and how [persuasive](https://www.nngroup.com/articles/interface-copy-decision-making/) conversion-supportive content is.

This analysis technique can also help you to do a postmortem on less desirable outcomes. What are the last few features users typically interact with before deleting their account? Perhaps those interactions can help identify signs of dissatisfaction with the site or product, so that later on you can look more closely into the needs of those users who exhibit those signs (e.g., through [intercept recruiting](https://www.nngroup.com/articles/live-intercept-remote-test/)) and try to address them.

## Summary

User-path reports are an exploratory tool for understanding common ways that users move through a site. While helpful in understanding aspects of users’ journeys, they are not a replacement for qualitative research that seeks to understand the thoughts, feelings, and expectations of users as they use a product.

To learn more about the role that user-path reports have in UX work, take our full-day seminar [Analytics & User Experience](https://www.nngroup.com/courses/analytics-and-user-experience/).
