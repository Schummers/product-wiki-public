---
title: "The Principle of Common Region: Containers Create Groupings"
date: "2020-07-12"
url: "https://www.nngroup.com/articles/common-region/"
author: "Aurora Harley"
topics: [psychology-and-ux, visual-design]
type: article
---

**Gestalt principles guide how people visually perceive the world** — including digital interfaces. Specifically, these principles explain how people decide whether several individual elements are part of the same group and, thus, are related in some way. This knowledge helps them understand and interact with the world in general, and also applies to controls and content on screens.

The original set of Gestalt principles was discovered in the first half of the twentieth century and includes proximity, similarity, and closure. Later research at the end of the twentieth century added a few more grouping principles to the list discovered initially by the Gestalt psychologists. Among these, perhaps the most relevant for UX is that of common region.

*Definition*: The **principle of common region** says that items within a boundary are **perceived as a group** and assumed to **share some common characteristic or functionality**.

![Graphic showing a 5-by-3 grid of dots, with the middle row of 3 dots contained in a colored box.](https://media.nngroup.com/media/editor/2020/06/10/commonregion-dotexamplesv2.png)

*The boundary around the three middle circles in this graphic makes them appear related and as part of the same group.*

In the above graphic, the boundary around the three middle circles causes them to appear as one group and separates them from the other, less-related surrounding circles. In a user interface, using a **border or background color to create a container for related items** helps users quickly and effectively understand the UI’s structure and which elements are connected.

For example, in the traditional *Print* dialog below, borders are used to organize the many detailed options into three groups: where to print (*Select Printer*), what to print (*Page Range*), and how many to print (*Number of copies*). The grouping makes it clear that the numeral “1” in the lower left is a page number, whereas the same character in the lower right specifies the number of copies to be printed.

![Screenshot of print dialog box on Microsoft Windows](https://media.nngroup.com/media/editor/2020/06/10/print-dialog-box.png)

*The print dialog box on Microsoft Windows, containing 3 groupings indicated by borders.*

## In This Article:

- [Construct a Clear Structure](#toc-construct-a-clear-structure-1)
- [Containers Communicate Relationships](#toc-containers-communicate-relationships-2)
- [Common Region Overpowers Other Groupings](#toc-common-region-overpowers-other-groupings-3)
- [Caution: Overuse Creates Clutter](#toc-caution-overuse-creates-clutter-4)
- [Conclusion](#toc-conclusion-5)

## Construct a Clear Structure

When users land on a webpage or open an app, they make [fast, automatic judgements](https://www.nngroup.com/articles/first-impressions-human-automaticity/) about where to look to complete their task. Designs that have distinct, organized sections make it easy to recognize the basic structure of the interface and to determine what areas of the UI to interact with.

Designating the header, footer, left navigation panel, or other areas of a UI using a background color is often used to create common regions that visually separate [chrome](https://www.nngroup.com/articles/browser-and-gui-chrome/) from content. For instance, in the Slack app, the dark background color groups together all the UI controls. Within that dark background, lines further create other common subregions, that communicate the grouping of the various controls (search and navigation at top, workspaces in the far left, and channels within a workspace).

![Screenshot of the Slack for Mac app](https://media.nngroup.com/media/editor/2020/06/10/commonregion_chromevscontent-slackapp.png)

*Slack app: Menu areas use a common background color to separate chrome from content.*

Websites with fixed or “sticky” headers can especially benefit from using a distinguishing background color or clear border, to effectively separate the header from the page content scrolling below. Additionally, a single unifying background color for [large footers](https://www.nngroup.com/articles/footers/) serves to effectively signal that all the links in this area belong to one group.

![Screenshot of Synchrony website showing both the fixed header area with a blue background and the footer area with a dark gray background, compared to the white main content area](https://media.nngroup.com/media/editor/2020/06/10/commonregions-headerandfooter-synchronybackwebsite.png)

*Synchrony Bank: The header and footer areas are each contained within a colored common region to distinguish them from the main content of the page.*

## Containers Communicate Relationships

People rely on visible boundaries in the page body to understand what information or UI elements are related. For instance, on article webpages, an image is often grouped together with its caption within a boundary to ensure that their relationship is clear, and to separate them from the rest of the article content. Once you begin looking for these visible groupings, you’ll see examples of boundaries to establish relationships everywhere.

For example, tabs and accordions often leverage a common region to communicate grouping. Displaying the tab or accordion label within the same boundary as its associated content visually connects the two areas and establishes their relationship. This visual trick can apply to countless situations: strategically placing items on a shared background makes them more likely to be perceived as related.

![Screenshots of 2 UI designs using common regions to communicate groupings](https://media.nngroup.com/media/editor/2020/06/10/commonregionswithinui-athleta_backcountry.png)

*(Left) Athleta mobile app: When open, subcategories within an accordion menu appear in the same container as the associated top-level heading. This design clearly communicates grouping and hierarchy inside the navigation. (Right) Backcountry.com: The article type (e.g.,* Guide, Story *) is clearly grouped with the title below by the white background, which creates a common region using a shared background color.*

## Common Region Overpowers Other Groupings

Creating a clear boundary is a **strong visual cue that can overpower other grouping principles** such as proximity or similarity. Thus, it is a powerful tool to use when needing to contain several different types of UI elements, or when adjusting the amount of whitespace between objects isn’t possible.

![Graphic showing 2 rows of 4 dots, where the middle 2 dots appear closer together than the outer dots. In the bottom row, borders are added to group the first 2 dots in a common region, as well as the second 2 dots.](https://media.nngroup.com/media/editor/2020/06/10/graphic_commonregionvsproximity.gif)

*In the top row, proximity causes the middle two circles to appear grouped together. In the bottom row, adding boundaries changes the perception of grouping, separating the two middle circles regardless of their proximity.*

In UI design, establishing a common region for related elements helps people quickly and accurately understand groupings. For example, in an older version of the Food Network tablet app, there were large gaps between elements associated with the same recipe. The extra space beneath each recipe name likely was intended to accommodate multiple lines of text in the recipe title, but the result was that it was difficult to tell which byline and rating were related to which recipe — the one above or below the rating? A simple solution to this problem is simply enclosing all the related content within a border — namely, a [card layout](https://www.nngroup.com/articles/cards-component/), like the one used in a subsequent version of the app.

![2 screenshots of the Food Network tablet iOS app: 1 from a previous version that suffered from proximity issues, and 1 from a later version that fixed the issue by using a card layout to group related information.](https://media.nngroup.com/media/editor/2020/06/10/proximityissuesfixedusingcardlayout.png)

*Food Network tablet app: An older version of the app’s grid layout (left) suffered from proximity issues — allowing room for long titles to wrap to multiple lines created excess whitespace under most titles and made it difficult to tell which byline and ratings went with which recipe. A later version (right) corrected this problem by using the card-layout style to create a common region for each recipe’s image, title, and details.*

Showing a common region can also aid perceiving multiple groupings at a time. For example, in a comparison table it’s important to distinguish both the column (for each product or service) and the row (for each characteristic). “Zebra” stripes, where alternating rows have a colored background, are a common method of uniting horizontal elements while whitespace or another border distinguishes each column.

![Graphic showing 3 columnsof shaped: 3 squares, 3 circles, and 3 triangles. The middle row containing a square, circle, and triangle are grouped within a colored container.](https://media.nngroup.com/media/editor/2020/06/10/commonregion-dualgroupings.png)

*The colored common region groups the middle row of items together, while proximity and similarity (the type of shape) create the three separate columns.*

## Caution: Overuse Creates Clutter

When possible, using whitespace alone to create clear groupings reduces the visual complexity of a design. Borders are often added in an abundance of caution, to ensure that groupings are clear; however, this approach can result in busy, cluttered designs and in many situations it’s enough to rely on proximity for grouping.

For instance, in the mobile version of Backcountry.com, each filter set in the filter menu is enclosed in a box. While not terrible, these borders aren’t necessary — proximity is enough to signal grouping.

![2 screenshots of a filter menu on a mobile website, showing what the UI looks like with and without borders segmenting each filter group.](https://media.nngroup.com/media/editor/2020/06/10/commonregionnotnecessaryforgroupings.png)

*The filter menu on the Backcountry.com mobile website displays each filter category within a bordered box (left). However, these groupings are still clear after removing the borders (right), so they could be omitted to save visual processing and allow room for more content.*

Apart from being unnecessary visual elements, segmenting a page into distinct sections can create [false floors](https://www.nngroup.com/articles/illusion-of-completeness/), and may prevent users from scrolling down the page because they think they’ve hit the end. This issue is especially common when borders extend the full width of the screen. Why keep scrolling if you’ve reached the end of what you were reading?

![Screenshot of Better Homes and Garden homepage, showing several sections of content with full-width colored backgrounds breaking up the page.](https://media.nngroup.com/media/editor/2020/06/10/commonregions-toomanysectionscausefalsefloors-bhg-cropped.jpg)

*Full-width content blocks with distinct borders and contrasting background colors can prevent users from continuing to scroll down a page because the new color creates a stopping point.*

Before adding more borders and backgrounds to a design, consider: are they necessary to understand the grouping? Can I communicate this grouping by simply adding or removing whitespace? Do I need to signal that these elements are related to each other, but not related to other, nearby elements? Were users confused during usability testing when the boundaries were not present?

## Conclusion

The principle of common regions is everywhere in UI design and serves to visually unite related UI components. Grouping elements in a container is a strong visual cue that can be used when whitespace alone doesn’t suffice. However, too many borders and colored boxes that exist purely for decoration add clutter to the interface.

Learn more about visual perception and other psychology principles affecting designs in our training course [The Human Mind and Usability](https://www.nngroup.com/courses/human-mind/).

### Reference

Palmer, S.E. (1992). Common region: A new principle of perceptual grouping. *Cognitive Psychology*, 24(3), 436–447. [https://doi.org/10.1016/0010-0285(92)90014-S](https://psycnet.apa.org/doi/10.1016/0010-0285(92)90014-S)
