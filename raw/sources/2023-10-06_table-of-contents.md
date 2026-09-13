---
title: "Table of Contents: The Ultimate Design Guide"
date: "2023-10-06"
url: "https://www.nngroup.com/articles/table-of-contents/"
author: "Huei-Hsin Wang, Maddie Brown"
topics: [design-patterns, interaction-design]
type: article
---

The table of contents has been a standard feature in book publication for centuries, helping readers locate specific chapters by providing an exact page number for each section. With the advent of the digital age, traditional printed tables of contents were adapted to digital formats. Today, they are widely used on websites, in ebooks, and in other digital interfaces to organize information and enable easy navigation.

## In This Article:

- [Definition](#toc-definition-1)
- [Benefits](#toc-benefits-2)
- [Considerations for Table-of-Contents Design](#toc-considerations-for-table-of-contents-design-3)
- [Placement Considerations](#toc-placement-considerations-4)
- [Styling Considerations](#toc-styling-considerations-5)
- [Best Practices for Tables of Contents](#toc-best-practices-for-tables-of-contents-6)
- [Conclusion](#toc-conclusion-7)

## Definition

> Definition:****A **table of contents** is an ordered list of clickable headings corresponding to the content sections on the page. It allows users to navigate directly to any of the sections on the same page.

This article provides comprehensive guidance on effective table-of-contents design by discussing its benefits, different placement and styling considerations, best practices, and common table-of-contents patterns.

![An illustration of different table of contents design combinations](https://media.nngroup.com/media/editor/2023/10/09/updated-article-visual_1.png)

*In this image, you can find the common table-of-contents designs resulting from combining the different choices discussed in this article.*

## Benefits

The benefits of using a table of contents on the page include:

- Scannable overview of the page
- [Direct access](http://www.nngroup.com/articles/direct-vs-sequential-access/) to specific sections
- Increased discoverability of bottom content
- Ability to share specific page sections
- Increased discoverability on the search-engine-results page

### Scannable Overview of the Page

A table of contents allows users to understand what the page has to offer without delving into details. It helps them form a [mental model](https://www.nngroup.com/articles/mental-models/) of the page and quickly determine whether the page content [satisfies their information needs](https://www.nngroup.com/articles/information-foraging/).

### Direct Access to Specific Sections

Each heading in a table of contents is [linked to a part of the page](https://www.nngroup.com/articles/in-page-links/), allowing users to jump to sections of interest without having to scroll through irrelevant content.

### Increased Discoverability of Bottom Content

Decades of research consistently indicate that [people dedicate more attention to the top of the page](https://www.nngroup.com/articles/scrolling-and-attention/). Thus, content at the bottom of a long page often suffers from low engagement. A table of contents increases the discoverability of the content that is low on the page.

### Ability to Share Specific Page Sections

Each section included in the table of contents has a unique [fragmented identifier](https://www.w3.org/DesignIssues/Fragment.html) in its URL, allowing users to precisely share specific sections of the page.

![A URL with fragmented identifier](https://media.nngroup.com/media/editor/2023/09/16/asset-2.png)

*Browser address bar: The fragmented identifier in the URL allows for sharing of a specific location.*

### Increased Discoverability on the Search-Engine-Results Page

The search algorithm can detect the section headings and display them as [site links](https://developers.google.com/search/docs/appearance/sitelinks), and a table of contents may increase the likelihood of this happening. Because users can get an overview of the page content **before accessing the page**, the clickthrough rate might increase as a result.

![An example of a search result that displays site links](https://media.nngroup.com/media/editor/2023/09/16/2-search-engine.jpg)

*Google search-results page: A regular search result (top) displays only a meta description of the page. The bottom search result displays additional site links generated based on the table of contents on the page.*

## Considerations for Table-of-Contents Design

When deciding what design to use for your table of contents, there are two kinds of considerations:

- **Placement considerations**

  - In rail or in the main body of the text
  - At the top of the page or lower in the body
  - Sticky or nonsticky
- **Styling considerations**

  - Vertical vs. horizontal vs. multicolumn layout

![A illustration of the decision tree with all the design considerations](https://media.nngroup.com/media/editor/2024/02/27/top-desktop.png)

*This decision tree summarizes all these considerations. A detailed discussion follows.*

![A illustration of the decision tree with all the design considerations](https://media.nngroup.com/media/editor/2023/09/16/top-mobile-copy.png)

*This decision tree summarizes all these considerations. A detailed discussion follows.*

## Placement Considerations

### Rail vs. Body

There are 3 placement options for tables of contents:

![A illustration of 3 placement options for a table of contents](https://media.nngroup.com/media/editor/2024/02/27/artboard-2-copy-4.png)

*A table of contents can be placed in the main body, in the left rail, or in the right rail.*

✅ Main Body | ✅ Left Rail | ⚠️ Right Rail | Very common approach | Adapts well to all screen sizes (responsive) | Very common approach | Works only for layouts with 2+ columns (large screens) | Less common | Susceptible to | right-rail blindness | Works only for layouts with 2+ columns

#### Main Body

One of the most common locations to place a table of contents is within the main body of the page. Frequently, this placement is utilized when the left or right rail is otherwise occupied, such as by [local navigation](https://www.nngroup.com/articles/local-navigation/), or not available (for example, on mobile or 1-column layouts).

![A screenshot of a content page with a table of contents placed in the content body when the left rail is taken](https://media.nngroup.com/media/editor/2023/09/18/32-simplilearn.jpg)

*Simplilearn: The table of contents on this page is in the body of the content, as the left rail contains local navigation.*

In addition to the obvious visibility benefits of placing the table of contents directly above or within the article itself, this placement approach is also the easiest to implement on mobile.

![A mobile screenshot that shows a content page with no left or right rail](https://media.nngroup.com/media/editor/2023/09/16/3-atrium-mobile.jpg)

*Atrium Health: Due to the limited screen size, mobile pages typically lack left or right rails.*

A factor that is necessary to consider with main-body placement is whether the table of contents should be placed at the very top of the page, or further down within the body of the text ([see below](#At the Top of the Page vs. In the Body of the Text)).

#### Left Rail

Another common approach is to place the table of contents within a rail on the left side of the page.

![An screenshot of a content page with a table of contents in the left rail](https://media.nngroup.com/media/editor/2023/09/16/4-investopedia.jpg)

*Investopedia: This page visually separates the table of contents from the rest of the article by placing it within the left rail.*

This approach provides a visual separation between the main content of the page and the navigational table of contents and allows readers quicker access to the article text.

The left rail placement does lead to some complications when it comes to mobile implementation, as mobile design typically does not allow for a left rail at all. Some common mobile implementations of left-rail table of contents placement include:

✅ **Move the table of contents to the main body**

The simplest solution is to move the table of contents to the main body of the article. One danger of this strategy is that even a short, 1-paragraph introduction to the page can push the table of contents below the [fold](https://www.nngroup.com/articles/page-fold-manifesto/).

![A short screen recording of a table of contents placed in the content body that takes some scrolls to reach](https://media.nngroup.com/media/editor/2023/09/16/5.gif)

*Google: The user must scroll down the page in order to discover the table of contents.*

✅ **Convert table-of-contents headings into accordions**

This solution uses accordions instead of links to create a table of content, by collapsing each section into an [accordion](https://www.nngroup.com/articles/accordions-on-desktop/).

![A screenshot of a table of contents converted to accordions on mobile](https://media.nngroup.com/media/editor/2023/09/16/6-american-red-cross.jpg)

*American Red Cross: All the body sections are collapsed behind their headings in an accordion layout.*

⚠️ **Convert to a sticky, collapsible table of contents**

Some designers choose to collapse the table of contents and make it sticky to the top of the page. In some implementations, this table of contents only appears after scrolling down to a certain point on the page.

However, visibility is often a concern. In testing, many users failed to notice the sticky table of contents in these implementations.

![A mobile screen recording of table of contents sticked to the top when scrolling down](https://media.nngroup.com/media/editor/2023/09/16/scrolling.gif)

*Investopedia: A collapsed table of contents appears after the user has scrolled partway down the page.*

#### Right Rail

While tables of contents placed in a left rail or main body are most common, right-rail tables of contents are still relatively frequent. Like main-body tables of contents, this approach is particularly appealing when the left rail is occupied by local navigation.

![A screenshot of a content page with its table of contents placed in the right rail](https://media.nngroup.com/media/editor/2023/09/16/8-google-search-central.jpg)

*Google Search Central: The left rail is already occupied by local navigation, so the table of contents is placed in the right rail instead.*

Like left-rail designs, right-rail tables of contents will not translate well to smaller screens or 1-column layouts.

The primary concern with right-rail tables of contents is visibility. Web users have trained themselves to ignore content that resembles advertising in any way, which includes any content placed in a right rail.

A simple, nongraphical design can prevent right-rail blindness.

![A screenshot of a right-rail table of contents with minimal graphical styling](https://media.nngroup.com/media/editor/2023/09/18/33-skin-cancer-foundation.jpg)

*Skincancer.org: This page attempts to alleviate the effects of right rail blindness with a simple, non-graphical design to the table of contents.*

Additionally, avoid confusion with local navigation or related-content links by including a clear, relevant header, such as *Table of Contents* or *On This Page*.

### Sticky vs. Nonsticky

Another consideration when designing a table of contents is whether it should be fixed ([sticky](https://www.nngroup.com/articles/sticky-headers/)) to the top of the page.

#### Sticky Tables of Contents

A sticky table of contents will not be lost after the user scrolls down the page. When the table of contents is in a left or right rail, making it sticky is easy, as the table of contents can remain in the same format (typically, a vertical stack of links).

To increase the usability and benefit of a sticky table of contents, consider highlighting the current section in the table of contents to show users where they are in the article as they scroll down.

![A screen recording of an article page with a sticky table of contents placed in the right rail](https://media.nngroup.com/media/editor/2023/09/16/9-time.gif)

*TIME: The various sections of the sticky table of contents are bolded as the user reaches them while scrolling.*

Benefits of highlighting the current section include:

- Users get feedback on scrolling [progress](https://www.nngroup.com/articles/progress-indicators/) and learn where they are on the page.
- [Animation attracts attention](https://www.nngroup.com/articles/animation-usability/), increasing the discoverability of the table of contents. Additionally, [subtle animation](https://www.nngroup.com/articles/animation-purpose-ux/) can create delightful [microinteractions](https://www.nngroup.com/articles/microinteractions/).

#### Nonsticky Tables of Contents

When dealing with a table of contents placed in the main body of the article, consider a nonsticky implementation. Sticky tables of contents in the main body can lead to a number of complications as they may compete with the site’s global navigation.

While most main nonsticky main-body tables of contents are stacked vertically, designers of sticky main body tables of contents tend to opt instead for a horizontal display of links. When this horizontal bar of links is stuck to the top of the page, it isn’t hard to understand why so many users confuse them with global navigation.

![A screen recording of an information page with non-stickly global navigation and sticky table of contents](https://media.nngroup.com/media/editor/2023/09/16/10-nhtsa.gif)

*National Highway Traffic Safety Administration: The global navigation is not sticky, but the table of contents is sticky. As a result, as the user scrolls down, the user will see only the table of contents.*

![A screen recording showing the global navigation and table of contents sticking to the top when scrolling down, stacked on top of each other](https://media.nngroup.com/media/editor/2023/09/16/11-accenture.gif)

Accenture: *Both the global navigation and the table of contents are sticky, leading to a stacked effect and resembling a common design pattern for global and local navigation*.

In both of the examples displayed above, the user is likely to confuse the table of contents for either a global or local navigation. As a result, we recommend a **nonsticky implementation of a table of contents when placed within the main body**.

If the table of contents is… | …then the table of contents should be… | In a left or right rail | …sticky. | In the main body | …nonsticky.

### At the Top of the Page vs. In the Body of the Text

Tables of contents are almost always found near the top of the page. Typically, they sit below the heading but above the main body of the article. This placement is the safe choice. However, sometimes tables of contents are embedded within the body of the article itself, sometimes following a brief introduction. This implementation comes with risks, which we outline in the sections below.

#### At the Top of the Page

Most often, tables of contents are located just below the heading or a short content brief, with some visual separation differentiating it from the body of the text.

![A screenshot of an information page with a table of contents right below the page brief](https://media.nngroup.com/media/editor/2023/09/16/12-massgov.jpg)

*mass.gov: The table of contents on this page is underneath the page summary, highlighted with a green bar and title.*

This is a time-tested pattern that brings with it some advantages.

- The table of contents will typically sit above the fold, allowing users to easily [scan](https://www.nngroup.com/articles/why-web-users-scan-instead-reading/) the contents of the page.
- The table of contents is less likely to be confused with other page elements, such as body text, local navigation, or other types of links.

#### In the Body of the Text

A table of contents placed further down the page within the page body is less discoverable, as it may require scrolling to get to it. As a result, it is less likely to function as an effective page overview. Additionally, when blended into the text body, the anchor links of the table of contents can easily be mistaken for links leading to other pages.

![A screenshot of an information page with a non-labeled table of contents in the main body](https://media.nngroup.com/media/editor/2023/09/16/13-irs.jpg)

*IRS: The table of contents is not labeled as such, and the styling of the table-of-contents links is identical to that of the related topics, publications, leaving ample opportunities for user confusion.*

There are a few strategies designers can employ to avoid this potential link confusion:

1. Ensure that the table of contents **heading is visually salient**(e.g., leveraging bolding and capitalization) to prevent the links from mixing with the body of the text. 

![A screenshot of an article page that has a table of contents with a bolded and capitalized heading](https://media.nngroup.com/media/editor/2023/09/16/14-national-cancer-institute.jpg)

*National Cancer Institute: This page uses the bold and capitalized heading ON THIS PAGE to introduce the table of contents.*
2. Use **icons as signifiers** to let users know what to expect. 

![A screenshot of an article page shows a down-arrow next to each heading in a table of contents](https://media.nngroup.com/media/editor/2023/09/16/15-betterhealth.jpg)

*BetterHealth: The down arrows inform the user that the links will take them further down the page, rather than to a new page.*
3. Use **visual boundaries** around the table of contents in order to separate it from the rest of the text. This approach can easily be taken too far and trigger [banner blindness](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/), as users may assume that the table of contents is an ad. 

![A screenshot of an article page that separates the table of contents from other body content with a divider line](https://media.nngroup.com/media/editor/2023/09/16/16-everymom.jpg)

*The Everymom: In this example, boundaries are employed, and the table-of-contents links are styled differently from the rest of the article. As a result, users may mistake the table of contents for an ad.*

## Styling Considerations

### Vertical Layout vs. Horizontal Layout vs. Multicolumn Layout

Depending on the makeup of the table of contents and the various links it contains, there are various potential layouts for how to style the table of contents itself.

![A illustration of possible layout options for a table of contents](https://media.nngroup.com/media/editor/2023/09/16/visual-layout.png)

A table of contents can be laid out in a vertical, horizontal, or multicolumn layout.

#### Vertical Layout

The most common layout for tables of contents is a single-column vertical format. This format is most advantageous when you have few topics with longer headings.

Advantages: | The sequence of the list items is clearly conveyed | Bullet points can be used to improve scannability | Easily scaled across different pages, as the design is not restricted by heading length | Disadvantages: | Requires more vertical space, and can push content below the fold

![A screenshot of a table of contents in a vertical one-column layout](https://media.nngroup.com/media/editor/2023/09/18/121-national-cancer-institute.jpg)

*The National Cancer Institute: The table of contents on this page uses a vertical stack of links to style its relatively long section headings.*

#### Horizontal Layout

Tables of contents can also be formatted in a horizontal layout, to save vertical space. This is best saved for instances with fewer topics and shorter headings.

Advantages: | Takes up less vertical screen space | Disadvantages: | Harder to scan | Less easily identified as a table of contents | Harder to discern the sequence of items

![S screenshot of an article page with a horizontal table of contents placed below the article title](https://media.nngroup.com/media/editor/2023/09/16/17-healthline.jpg)

*Healthline: This example features short section headings, appropriate for a horizontal table-of-contents layout.*

#### Multicolumn Layout

This is a less common design pattern that, nonetheless, offers the best of both worlds: efficient use of screen space and scannability. This approach is best suited for instances with many listed topics.

Advantages: | Takes up less vertical screen space | Bullet points can be used to improve scannability | Disadvantages: | Because it is less common, it may not be immediately recognized as a table of contents

![A screenshot of an about-us page that has a multi-column table of contents](https://media.nngroup.com/media/editor/2023/09/16/18-atrium.jpg)

*AtriumHealth: This page has a relatively long list of headings, and thus opts for a two-column layout.*

### Visualizing In-page Links

Our research has indicated that [web users demonstrate increased familiarity with in-page links](https://www.nngroup.com/articles/in-page-links-content-navigation). Nevertheless, it remains critical to provide sufficient signifiers of clickability in order to maximize the affordance of the links. In other words, all the [standard best practices for link visualization](https://www.nngroup.com/articles/guidelines-for-visualizing-links/) apply here. For example, table-of-contents links should be colored and underlined, as in the below example from the National Institute on Aging.

![An article page that stylize the links in a table of contents pages to be blue and underlined](https://media.nngroup.com/media/editor/2023/09/16/19-national-institue-on-aging.jpg)

*National Institute on Aging: This example opts for a traditional styling of blue, underlined links for its table of contents.*

On the other hand, if links lack sufficient signifiers, they are likely to be overlooked.

![A screenshot of a table of contents with links in black and no underlines](https://media.nngroup.com/media/editor/2023/09/16/20-wirecutter.jpg)

*The New York Times’ Wirecutter: The links are not colored, and the underline of the links only appears upon hovering over the link. In testing, users failed to interact with this table of contents.*

Additionally, misuse of signifiers can cause other forms of confusion, as in the example below.

![A screenshot of an article page with table of contents styled in chip shapes](https://media.nngroup.com/media/editor/2023/09/16/18-webmd.jpg)

*WebMD: Presumably in an attempt to visually distinguish table-of-contents links from other in-page links, WebMD chose to style the former as chips. This pattern is, however, commonly used for filters or tags. (Additionally, the long headings in the horizontal layout are difficult to scan.)*

### Smooth-Scrolling Effects

A final styling question to consider is how to facilitate the movement of the page from one section to another after the user clicks on a table-of-contents link. Traditionally, the page would instantly jump the user down the page, providing instant access to the desired content. An alternative approach employs smooth scrolling from one point on the page to another, which can create a seamless experience by [showing continuity in transition](https://www.nngroup.com/articles/guidelines-for-multimedia-on-the-web/). This design also eliminates any possible confusion that the user may have been taken to a new page.

![A screen recording of the page smoothly scrolling down when a heading is clicked](https://media.nngroup.com/media/editor/2023/09/16/22.gif)

*American Red Cross: When clicking a heading in this table of contents, the page employs smooth scrolling to reach the desired spot on the page.*

## Best Practices for Tables of Contents

Below are some best practices to follow when designing a table of contents:

- Use a clear label for the table of contents.
- Avoid discrepancies in link labels.
- Make headings scannable.
- Do not include external links in the table of contents.
- Do not skip content headings (even if they are above the fold).
- Include back-to-top links.
- Ensure consistency across all the tables of contents.

### Use a Clear Label for the Table of Contents

As in-page links often share a similar visual style with links that direct users to external pages, it becomes essential to distinguish the table-of-contents section from other links present on the page. Appropriately labeling the section helps clarify how the links will function. It can also provide context for screen-reader users and users who are exposed to a limited amount of content (e.g., screen magnifier users and users on a small screen)

*Table of Content*, *Contents*, *On**This**Page*, and *In**This**Article* are informative and predictable labels for a table of contents. *Tell**Me**More*, on the other hand, has poor [information scent](https://www.nngroup.com/articles/information-scent/), and the links in the section can be mistaken for links to related content.

![A screenshot of a table of contents that uses "Tell me more..." as a heading](https://media.nngroup.com/media/editor/2023/09/16/23-robinhood.jpg)

*Robinhood: The heading* Tell me more…*can be mistaken for related links to other pages.*

### Avoid Discrepancies in Link Labels

Just like any other links existing on the web, the links listed under the table of contents are [promises to keep](https://www.nngroup.com/articles/link-promise/). They should match the section headings they are leading to, to reassure users that they have arrived at the right section on the page. Discrepancies in wording force users to analyze and compare two highly similar headings, adding unnecessary [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/).

![A screenshot showing a mismatch in wording between the label in the table of contents and the section heading, with one saying "Prepare Before" and the other "Before an Incident""](https://media.nngroup.com/media/editor/2023/09/16/24-readygpv.jpg)

*ready.gov: The link labels in the table of contents (e.g. Prepare Before) don’t exactly match the corresponding section headings (e.g.  Before an Incident). Users might be unsure that they got to the right section.*

### Make Headings Scannable

The headings in the table of contents should be succinct and easy to scan, allowing users to quickly grasp the essence of the page. A long list of lengthy headings can create a daunting wall of text. Going through a long list of distinct links is like reading a huge paragraph, with each sentence conveying a separate message.

![A screenshot showing a table of contents with long-sentence headings](https://media.nngroup.com/media/editor/2023/09/16/25-usnrc.jpg)

*U.S. NRC: The table of contents in this FAQ page displays long, hard-to-scan headings.*

![A screenshot showing the table of contents sorted by themes that are easier to scan](https://media.nngroup.com/media/editor/2023/09/16/26-usnrc.jpg)

*U.S. NRC: Another FAQ page on the same site categorizes questions and labels each category with a short heading, making the table of contents much easier to scan.* Do Not Include External Links in the Table of Contents

### Do Not Include External Links in the Table of Contents

Users expect the links in the table of contents to behave consistently. Mixing external and in-page links in the list will break users’ mental models and cause confusion.

![A screen recording showing the table of contents mix in-page links with links to new pages](https://media.nngroup.com/media/editor/2023/09/16/27-uspto.gif)

*United States Patent and Trademark Office: One of the links in the table of contents is formatted the same as the others but leads to another page.*

### Do Not Skip Content Headings (even if they are above the fold)

A table of contents acts as a comprehensive overview of the page. Leaving out sections or only displaying the sections below the fold can lead to an incomplete understanding of the page content and cause confusion.

![A screenshot showing the table of contents skips the section above the fold, only displaying sections below](https://media.nngroup.com/media/editor/2023/09/16/28-usda.jpg)

*USDA.gov: This page skips sections that are displayed above the fold and shows only topics that are further down the page. This design can give a wrong sense of the page offerings.*

### Include Back-to-Top Links

When including a table of contents on a long page, consider whether users will access other sections of the page and how they will navigate after finishing the section. Will they keep reading? Or will they want to jump to a different section? Consider providing a [back-to-top link](https://www.nngroup.com/articles/back-to-top/) to help users return to the top, especially when you have a long page with a nonsticky table of contents.

![A screenshot showing a long content page incorporate back-to-top link at the end of each content section](https://media.nngroup.com/media/editor/2023/09/16/29-wage-and-hour-division.jpg)

*Wage and Labor Division: Adding a back-to-top link minimizes scrolling on a long page and allows users to jump to other sections after finishing a section.*

### Ensure Consistency Across All the Tables of Contents

The style and format of the table of contents should be consistent across the website to match users’ expectations. A website without [internal consistency](https://www.nngroup.com/articles/consistency-and-standards/) forces users to relearn the pattern on each new page, distracting them from accomplishing their intended goals.

![A screenshot showing 4 different styles of a table of contents appearing on the same website](https://media.nngroup.com/media/editor/2023/09/16/265-us-food-and-drug-administration.jpg)

*U.S Food and Drug Administration: The style and format of the tables of contents vary from page to page on this website — at least 4 different styles are presented across a few sibling pages.*

## Conclusion

A table of contents provides a helpful page overview and facilitates in-page navigation for content pages. A thoughtful implementation should take into consideration different placement and styling options. By carefully weighing the benefits and tradeoffs of each option, you can create table of contents designs that maximize usability and impact.
