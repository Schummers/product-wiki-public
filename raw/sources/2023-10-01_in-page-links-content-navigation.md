---
title: "In-Page Links for Content Navigation"
date: "2023-10-01"
url: "https://www.nngroup.com/articles/in-page-links-content-navigation/"
author: "Huei-Hsin Wang"
topics: [design-patterns, interaction-design, web-usability]
type: article
---

## In This Article:

- [What Are In-Page Links?](#toc-what-are-in-page-links-1)
- [Research Findings: User Perception of In-Page Links](#toc-research-findings-user-perception-of-in-page-links-2)
- [In-Page Links: Use or Pass?](#toc-in-page-links-use-or-pass-3)
- [The Alternatives: Accordions and Tabs](#toc-the-alternatives-accordions-and-tabs-4)
- [Conclusion](#toc-conclusion-5)

## What Are In-Page Links?

Navigating long-form content can be challenging, akin to climbing stairs in a tall building. Just like elevators can take you straight to the destination floors, in-page links help **** users navigate through page content with just one click.

> **In-page links**(also known as **jump links** or **anchor links**) are links that take users to a specific section on the same page.

In-page links can serve various purposes, such as a *Back to Top* link or a *Skip to Content* link for keyboard users, but one of their most common uses is in a table of contents. A table of contents, usually found at the top of information-rich pages, presents a structured list of the content topics on that page, allowing users to click and navigate directly to their desired sections. While there are alternative formats for tables of contents (e.g., [accordions](https://www.nngroup.com/articles/accordions-on-desktop/), [sticky navigation bars](https://www.nngroup.com/articles/sticky-headers/)), this article exclusively focuses on its implementation using in-page links.

To facilitate navigation within this article, the section below also presents a list of in-page links that can direct you to specific parts of the article.

## Research Findings: User Perception of In-Page Links

Despite their ability to facilitate content navigation, in-page links have historically raised usability concerns as they **break the mental model for a link.** Traditionally, on the web, links lead to external pages. Due to this reason, when in-page links initially made their appearance on the web, our recommendation was to avoid them.

However, with the increased prevalence of in-page links, we have seen a growing familiarity with this design pattern. A few years ago, we [reassessed the use of in-page links](https://www.nngroup.com/articles/in-page-links/) and provided guidelines for its implementation (which are still applicable today). In our most recent study on how people read long content pages, we observed participants naturally engage with the table-of-contents links; these behaviors demonstrate increased awareness and understanding of the interaction pattern. Many study participants **used, commented on, and appreciated the in-page links** in tables of contents. Below we highlight some key research findings.

### Are In-Page Links Still Confusing?

**Most of our study participants, regardless of age, were familiar with in-page links.** Only 2 out of 11 participants showed no engagement with in-page links when those were presented to them.

Despite the familiarity,**in-page links, when not formatted with intention, can still surprise users.** One participant, who adeptly used in-page links to navigate two other pages, expected that the in-page links on the Phone Arena page take her to another page. The confusion is likely due to how these links were styled on the Phone Arena page: they were right above the *Read More* section and looked exactly like regular links that lead to other pages. It is likely that the [proximity](https://www.nngroup.com/articles/gestalt-proximity/) and [similarity](https://www.nngroup.com/articles/gestalt-similarity/) of the two sections tricked her into thinking that the links from both sections serve the same purpose.

![Mobile screenshot of Phone Arena showing table of contents placed directly above the read more section](https://media.nngroup.com/media/editor/2023/09/07/phone-arena.png)

*Phone Arena: One participant was confused by the in-page links listed under the* Table of Contents,*thinking they would lead to another page.*

### How Do Users Recognize In-Page Links?

Like with any link, it’s important to **signify clickability** through [proper styling of the link](https://www.nngroup.com/articles/guidelines-for-visualizing-links/). Users should also be able to tell whether the link will keep them on the current page. This can sometimes be done through contextual cues, like in the case of the Healthline article, where the participant was able to infer that the links under the article title are in-page links because they were directly related to the article title. However, in most scenarios that will not be apparent. It’s, thus, a good idea to use a label such as *Table of Contents* or *On This Page* to help users identify in-page links.

*A study participant shared his thought process when he encountered in-page links on the article page of Healthline.com.*

### How Do Users Use In-Page Links?

As one study participant was exploring an article, he said about the table of contents: *I like that section heading up here. That kind of gives you the outline of the article so you can jump to a specific section rather than having to scroll through everything if you're only looking for a specific bit of information.*

This quote highlights two ways in which tables of contents with in-page links are useful:

- Allow users to skip to relevant sections
- Provide an outline of the page content

**Allow Users to Skip to Relevant Sections**

People [read little on web pages](https://www.nngroup.com/articles/how-users-read-on-the-web/). Several participants commented that in-page links helped them skip content that they were not interested in, allowing them to avoid scrolling through screenfuls of irrelevant information. Offering [direct access](https://www.nngroup.com/articles/direct-vs-sequential-access/) to specific sections on the page minimizes scrolling and helps users navigate more efficiently.

In our study, we [funneled tasks](https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/): we asked participants to first explore the page, and then we gave them more directed tasks. We observed that users tended to skip in-page links in their initial exploration and clicked on in-page navigation links **when they had a specific information need**. For instance, one participant did not use or comment on the table-of-content links when we asked him to explore a smartphone review. Later, when he had to compare camera features on two phones, he immediately navigated to the table of contents and clicked on the in-page links to jump to the right section. We observed this behavior recur on different participants across several websites.

**Provide an Outline of the Page Content**

When in-page links were presented at the top of the page, several study participants spent time examining the list before exploring the content. The upfront overview of the content allows users to form a [mental model](https://www.nngroup.com/articles/mental-models/) of the page and quickly [assess whether the page satisfies their information needs](https://www.nngroup.com/articles/information-scent/), giving them [a reason to continue to scroll](https://www.nngroup.com/articles/page-fold-manifesto/).

![A screenshot of table of contents on the Nerd Wallet website](https://media.nngroup.com/media/editor/2023/09/07/nerd-wallet.png)

*Nerd Wallet: One participant shared positive comments on the table of contents links on this page:* Well that gives me a quick [idea] of what I can expect further down the page. I see that they're links, so if I wanted to just jump to one of them I would. But I wanted to look at each one sequentially. But yeah, it tells me how far down the page I can expect to find what information, which is always nice. … Like a table of contents.

## In-Page Links: Use or Pass?

To maximize the value of in-page links, consider the following aspects before incorporating them into your design:

### Page Length

In-page links are most valuable for long-form content. For shorter pages with minimal information, users are unlikely to require in-page links for navigation. Including a table of contents with in-page links on such pages can add unnecessary length to the page and push content further away below the fold.

![A screenshot showing unnecessary use of table of contents on a short page](https://media.nngroup.com/media/editor/2023/09/07/pbgc.gif)

*Pension Benefit Guaranty Corporation (PBGC): This page has only a few brief sections, so a table of contents is unnecessary and increases the page length.*

### Content Shortening

While in-page links are valuable tools for facilitating page navigation, the content remains the core of the experience. When considering the use of in-page links for long-form content, assess whether the content can be condensed. Shorter, scannable content significantly enhances the overall reading experience. Eliminating unnecessary details helps reduce page length, potentially to a point where in-page tables of contents become unnecessary.

### One Page vs. Multiple Pages

While showing everything on one page and incorporating in-page links for navigation might seem appealing, this design choice comes with two significant disadvantages: excessively long pages and large load times. These disadvantages can be **problematic for mobile users** because of:

- limited screen size, which can lead to long pages demanding excessive scrolling
- poor page performance, due to variable connectivity or limited data plans

How you decide to lay out content should depend on the information **** on your page. Users are willing to scroll through a long page if all the presented information is highly relevant to their needs. However, if your page includes several distantly related topics, breaking it across multiple pages might be more practical.

![Screenshots of a very long page with rich content](https://media.nngroup.com/media/editor/2023/09/07/our-world-in-data_connected.png)

*Our World in Data: This very long page (as indicated by the scrollbar progress) presents rich research findings on the eradication of diseases. In-page links are used both in the top summary and in each section to facilitate content navigation. While displaying information in one scrollable long page creates a seamless reading experience, it can also increase loading time.*

### Logical Chunking

Using in-page links as a table of contents on the page requires breaking down the content into distinct chunks that can be summarized with a heading. [Chunking information improves scannability and comprehension](https://www.nngroup.com/articles/chunking/), but if the information is better presented in one cohesive body, in-page links are not useful.

![A screenshot of an interview article in a Q&A format](https://media.nngroup.com/media/editor/2023/09/07/au-review.png)

*The AU Review: This page contains an interview with multiple interviewees. The questions in the interview organically build off one another, making the page difficult to break into chunks. A table of contents with in-page links would not be useful in this case.*

## The Alternatives: Accordions and Tabs

Accordions and [tabs](https://www.nngroup.com/articles/tabs-used-right/) are alternative design patterns for implementing tables of contents on long content pages.

![A illustration of in-page links, accordions, and tabs](https://media.nngroup.com/media/editor/2023/09/08/article-visual.png)

*Accordions and tabs are alternatives to an in-page table of contents.*

These 3 interaction patterns share some similar characteristics:

- Serve as a table of contents that provides an overview of the content
- Facilitate direct access to content
- Manage content on the same page (as opposed to across multiple pages)
- Require logical chunking of information

The table below highlights their differences:

In-Page Links | Accordions | Tabs | Function | Navigation | Content structuring | Page length | Increased | Decreased | Is some content hidden by default? | No | Yes | Access to parallel content sections | Yes | No if only one accordion can remain open at a time | No | Main use case | Embedded into the body text as a table of contents | Formatting multiple short content sections | For formatting few longer content sections

Among the three,****accordions shine through in [mobile usage](https://www.nngroup.com/articles/mobile-accordions/)**.** In contrast to in-page links that push down content, accordions reduce page length by doubling as both section headings and content container controls.

Tabs suffer from low discoverability. In many cases, users tend to focus on the content in the default tab and ignore the information presented in the other tabs. Tabs also make it difficult to refer to information in two tabs at the same time. On mobile, the list of tabs may not entirely fit on the small screen, forcing designers to resort to imperfect solutions such as label truncation or hiding some of the tabs in a carousel.

When choosing among these design patterns, assess user goals and weigh the benefits and tradeoffs of each option. Two key questions to consider are:

- **How will the page be used?**
- **Does the selected pattern help users better accomplish their goals compared to the alternatives?**

One key point is that content structure and format should come **** before choosing a design pattern. By prioritizing content organization, you can make informed decisions that lead to better user experiences.

## Conclusion

Tables of contents based on in-page links are a valuable tool for navigating long-form content. Research indicates that users are increasingly familiar with this design pattern. When properly styled and labeled, in-page links provide a useful overview and a quick way to access specific page sections. The decision to implement in-page links should be based on thoughtful consideration of the content structure and user needs. If in doubt, conduct usability testing to assess if in-page links are suitable for your page.

Check out our full-day course [Web Page UX Design](https://www.nngroup.com/courses/web-page-design/)
