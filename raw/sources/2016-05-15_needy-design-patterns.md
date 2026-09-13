---
title: "Needy Design Patterns: Please-Don’t-Go Popups & Get-Back-to-Me Tabs"
date: "2016-05-15"
url: "https://www.nngroup.com/articles/needy-design-patterns/"
author: "Kate Moran, Kim Flaherty"
topics: [design-patterns, web-usability]
type: article
---

In UX design, “[dark patterns](http://darkpatterns.org/)” are deceptive strategies used by designers to trick users into doing potentially harmful things that support their organization’s goals. For example, sites that automatically add extra items into users’ shopping carts are using a dark pattern to increase their sales.

The two design patterns discussed in this article fall into a similar (if slightly less immoral) category, which we call “**needy patterns**.” These are design patterns aimed at grabbing users’ attention. They’re driven by goals like increasing email-newsletter signups or page views, but they slow users down or degrade their overall experience.

There are many patterns that could fall into this needy category. In this article we focus on two needy patterns that have recently become popular and that **interfere with browser-tab usage**.

There are two primary types of behavior involving the use of multiple browser tabs:

- **Parallel browsing**, where a user alternates between tasks, generally using one tab per task
- [Page parking](https://www.nngroup.com/articles/multi-tab-page-parking/), where a user opens multiple pages into different tabs in support of one large task (such as comparing items to buy, or researching a topic)

[Millennials in particular tend to rely on page parking](https://www.nngroup.com/articles/multi-tab-page-parking/) as an information-seeking strategy. The two needy patterns we discuss here hurt people who use multiple tabs, whether for parallel browsing or page parking. We’ve named these needy patterns:

- The please-don’t-go popup
- The get-back-to-me browser tab

## In This Article:

- [The Please-Don’t-Go Popup](#toc-the-please-dont-go-popup-1)
- [The Get-Back-to-Me Browser Tab](#toc-the-get-back-to-me-browser-tab-2)
- [Conclusion](#toc-conclusion-3)

## The Please -Don’t-Go Popup

This pattern is sometimes known as an “exit-intent popup,” an “exit popup,” or an “exit modal” (in an attempt to disassociate this pattern with the reviled word “popup," which is tainted by being the #1 [most-hated advertising technique](https://www.nngroup.com/articles/most-hated-advertising-techniques/)). These popups lurk unseen until the user starts to move the mouse towards the top of the page. Panicking that the user is about to bounce, the exit popup triggers a desperate, final attempt to keep the user’s interest. These popups often contain content such as, “Before you go…!” or “Don’t miss…!” Sometimes they offer discounts, advertise an email newsletter, or suggest related content.

![ExitPopup TNW News](https://media.nngroup.com/media/editor/2016/05/09/exitpopup-tnwnews.png)

*An exit popup from TNW News pushes the organization’s email newsletter.*

The exact functionality of each exit popup differs. Sometimes the popup will appear as soon as the user starts moving towards the top of the page; in other cases, it will show up after a specific amount of time (5 seconds, 10 seconds, etc.). Sometimes the popup is combined with animation — for example, creating a shaking effect. Sometimes it works alongside cookies, so a user who sees an exit popup and stays on the site won’t see it again.

![ExitPopup WP beginner](https://media.nngroup.com/media/editor/2016/05/09/exitpopup-wpbeginner.png)

*This exit popup on wpbeginner.com uses a shake animation, which has the effect of making a popup even more annoying.*

The goal is to catch users before they abandon the site, to show them something they may have missed, or to provide one final appeal to capture their attention. And, according to the logic of exit popups, who cares if this appeal doesn’t work and users are [annoyed](https://www.nngroup.com/articles/does-user-annoyance-matter/)? There’s nothing to lose, because they’re leaving anyway, right?

**Wrong.** When users engage in page parking, they systematically move between opened tabs, saving their place to return later. The code behind exit popups doesn’t know if a user is moving the mouse to:

- close the tab,
- temporarily move to another tab, or
- open a new tab.

The exit popup can’t tell the difference. Imagine that a user is engaging in page parking to help her research a topic. She starts with a Google query, and then opens up several results into new tabs rapidly. The user begins moving through each tab, closing some that are irrelevant, but saving some to return to them later. Then, in the middle of this process, an exit popup suddenly appears, pressuring her to check out some different content or sign up for an email newsletter. The user thinks, “Wow, calm down! I was going to come back in two minutes!”

![ExitPopup Lifehack](https://media.nngroup.com/media/editor/2016/05/09/exitpopup-lifehack.png)

*This exit popup on lifehack.org assumes users are leaving because they’re finished with the current piece of content, and makes a last-minute attempt to show related topics. Unfortunately, the popup is irritating if the user hasn’t finished reading the current piece of content.*

Except when it’s in their best interest (preventing someone from closing a file without saving it, for example), we never recommend intentionally interrupting or annoying users.

## The Get-Back-to-Me Browser Tab

This next pattern has nothing to do with what happens while you’re on the website, but instead it’s related to what happens when you’ve left. When a user navigates away from a website by visiting another browser tab, the site swaps the original page title with an attention-seeking message.

![TabTitleChangeChrome](https://media.nngroup.com/media/editor/2016/05/09/chrometabtitlechange2.png)

*In this example, the Chrome browser has 7 open tabs. The last three tabs have replaced the tab title with a needy message.*

![TabTitleChange1](https://media.nngroup.com/media/editor/2016/05/09/tabtitlechange1.png)

*Blog.invisionapp.com replaces the name of the blog post with a reminder to return to the tab. In this example, part of this reminder is cut off due the number of browser tabs open. (When users have many tabs open at once, page titles are often cut off.)*

The website’s primary goal is to cleverly hijack users’ attention and bring them back to the site. Maybe there were some good intentions driving this design decision: perhaps the site truly hopes to be helpful and remind users to view the content on that page. However, this reminder isn’t helpful at all; in fact, it is problematic for two major reasons:

- the loss of context caused by an unhelpful title, and
- the likelihood that whatever effectiveness the tactic once held will be eroded as more sites adopt it

**Loss of Context**

Without the true page title, people are left with no clues for the content of the tab. Users often keep frequently visited pages such as Facebook or news websites open throughout the day in order to revisit them and check for updates. Users who are shopping or conducting research may be parked on many pages at once, using browser tabs to collect and manage product options and information

[Page titles should begin with information-carrying words](https://www.nngroup.com/articles/microcontent-how-to-write-headlines-page-titles-and-subject-lines/) to give users context and help them differentiate among tabs. In addition, websites should utilize a well-designed favicon (the small 16x16 pixel icon used in tabs) to help users identify which tabs belong to which site.

In the previous example, Invisionapp would be better off keeping the title of the blog post on the tab at all times. For users conducting research on a particular topic, this tab may be one of many that they intend to read over time. The best reminder to return to the tab is the actual page title, which has meaning to the user and probably some appeal to them in the context of the current task (or the user wouldn’t have opened that page in the first place). With no context, it’s likely that users scanning their parked tabs will not recognize the unrelated title and dismiss the page altogether.

**Ineffective when Commonly Used**

Some designers might argue that this technique will delight users by catching their attention with something unique and unexpected. That delight (if it ever existed in the first place) will no doubt turn to frustration quickly if this pattern becomes widely used across the web. Page parking and parallel browsing will become quite difficult if your browser tabs resemble a bunch of journalists fighting for attention at a press conference.

![TabTitleChange2](https://media.nngroup.com/media/editor/2016/05/09/tabtitlechange2.png)

![TabTitleChange3](https://media.nngroup.com/media/editor/2016/05/09/tabtitlechange3.png)

*Too many other sites already replicate the problematic get-back-to-me pattern.*

When multiple browser tabs employ this technique, users have no indication of which tab contains what content. They will be forced to bounce in and out of each page to remember what the tab contains. And if these websites are really needy, these users may also be dealing with please-don’t-go popups slowing them down along the way.

![TabTitleChangeTwitter](https://media.nngroup.com/media/editor/2016/05/09/twitter-tabtitlechange.png)

*Twitter prepends the page title with a numeric indicator to let users know how much additional content has been added to their feed since it was last checked. This tab-title update effectively reminds the user to return without removing the context of the page.*

Think of your page tab as one of many nodes in a distinct and dynamic global navigation created by the user to meet their unique needs. Your page title serves as a label in this navigation and should provide the appropriate context and [information scent](https://www.nngroup.com/articles/information-scent/), so that users can assess the content of the page.

## Conclusion

Every website has a personality. The visual design, the interaction design, the copy, and tone of voice all contribute to how your users perceive your site and your brand. Needy patterns like the please-don’t-go popover and the get-back-to-me tab chip away at the presentation of a professional, confident website. They also damage users’ perceptions of credibility.

As a thought experiment, ask your brand manager whether “we’re desperate for attention” is one of the company’s stated brand values. If not, why signal such desperation to customers?

These kinds of tactics are often embraced and accepted based on better conversion [performance in A/B tests](https://www.nngroup.com/articles/putting-ab-testing-in-its-place/). However, there’s a big tradeoff that comes with being needy and annoying — the degradation of your relationship with your users.

Prioritizing conversions or short-term metrics leads designers to pressure people into doing things they don’t actually want to do and can easily cross the ethical boundaries towards dark patterns. It’s time to reassess priorities and long-term goals: you may be getting a few extra clicks now, but in the long run you’re losing your users’ trust and respect. **Nobody likes a needy website.**
