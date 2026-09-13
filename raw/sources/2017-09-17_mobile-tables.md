---
title: "Mobile Tables: Comparisons and Other Data Tables"
date: "2017-09-17"
url: "https://www.nngroup.com/articles/mobile-tables/"
author: "Amy Schade"
topics: [e-commerce, mobile-and-tablet-design]
type: article
---

Displaying big data on a small screen is a daunting challenge. How do we make a large amount of data fit on a small screen? Other than limiting the number of rows or columns of data, what other options are available to display tables on small screens? What does a usable table look like on mobile?

(The general problem of having more data than fits on the screen is not specific to mobile: information-visualization researchers have struggled for years with the topic of showing data that has more columns (or rows) that can fit on the user’s screen — be it a large monitor, an array of monitors, or a small mobile display. However, **the smaller the screen, the more likely that we’ll get into trouble** with any given dataset and will need to design carefully to minimize usability problems.)

In our article on [comparison tables](https://www.nngroup.com/articles/comparison-tables/), we covered key elements in presenting data, such as the need for **consistency of content** and **presenting meaningful attributes** to users. Both are equally, if not even more important for mobile tables, due to the small amount of data visible at one time. You must **first create a usable table for a large screen** before translating it to a small one. The need to make a table work on a smaller screen may be a good reason, excuse, or impetus to reevaluate the content and attributes in your table, regardless of screen size, and to improve content for all users.

## In This Article:

- [Columns Large Enough to Be Legible](#toc-columns-large-enough-to-be-legible-1)
- [Rotating the Phone Is a Last Resort](#toc-rotating-the-phone-is-a-last-resort-2)
- [Stick Column Headers in Place](#toc-stick-column-headers-in-place-3)
- [Clearly Indicate if Horizontal Scrolling Is Needed](#toc-clearly-indicate-if-horizontal-scrolling-is-needed-4)
- [Stick the Left Column in Place](#toc-stick-the-left-column-in-place-5)
- [Let Users Select the Data to View](#toc-let-users-select-the-data-to-view-6)
- [Accordions for Groups of Data](#toc-accordions-for-groups-of-data-7)
- [Help Users Find What They Need](#toc-help-users-find-what-they-need-8)

## Columns Large Enough to Be Legible

The number of columns that fit on a mobile screen without scrolling will depend on the width of those columns. Items need to be **legible without requiring the user to zoom in**.

For complex or wordy entries, such as those in comparison tables, only 2 columns may fit legibly on a narrow mobile screen. For a number-heavy table, narrower columns may work, allowing more columns to be visible.

*The National Rugby League’s player statistics were numeric and allowed 11 columns to be displayed on the screen without horizontal scrolling. Note that this was accomplished by using only the logo of the opposing team in the first column and the abbreviation for the statistics in the column headings, which will be a problem for users unfamiliar with this shorthand. That said, only rugby fanatics are likely to be interested in such detailed player stats in the first place.*

## Rotating the Phone Is a Last Resort

Rotating the phone allows more columns of information to be visible at once. However, what you gain in column space, you lose in row space. In addition, it can be an annoyance to users if you dictate how they must hold their phone. Carefully consider if the payoff of gaining width balances the downside of **annoying the user and losing space for data rows**.

*To compare credit cards on Citi.com, users needed to follow the instruction,* Rotate your device to continue using the compare credit card feature *. Once the phone was rotated, most of the screen height was dedicated to large images of the credit card, which locked in place as the user scrolled, leaving only very little space for the comparison-table data. (This is a classic example of the need to reconsider the use of images in the mobile version of a website : while credit-card photos might be good column headers for desktop users, they should be suppressed or made smaller for mobile users, who may be better off with name-only column headers.)*

## Stick Column Headers in Place

For any table that fills more than a single vertical screen, sticky column headers help users know what they are looking at. Without sticky headers, it is easy to lose the context of what the table is displaying.

*Left: This comparison table from BestBuy.com did not lock either column or row headings in place, making it harder to understand the data in the table. Right: The screenshot shows the table scrolled, with no labels visible.*

## Clearly Indicate if Horizontal Scrolling Is Needed

When data doesn’t fit the width of a portrait-view mobile screen, users may need to scroll horizontally to see the full information. (While [horizontal scrolling](https://www.nngroup.com/articles/horizontal-scrolling/) in general is nasty for desktop and mobile users, it’s somewhat acceptable for large tables on mobile screens.)

However, for such scrolling to work, it must be **apparent that there is more data beyond the horizontal fold**. Like for [carousels](https://www.nngroup.com/articles/designing-effective-carousels/), arrows or cut-off elements convey this information best. [Dots are sometimes used](https://www.nngroup.com/articles/4-ios-rules-break/), but are typically harder for users to notice and understand than arrows or cut-off elements.

*On eBag’s site, the final product column was cut off, indicating that a horizontal scroll was available.**The Subaru site used dots and arrows above the data table to show users that more screens of content were available. Dots are often overlooked in such designs and are a bit confusing here because two dots are highlighted to show “the current location,” (i.e., that two columns are currently visible). Also, the arrows will be more effective if placed within the display of data, not at the top of the page.*

## Stick the Left Column in Place

If users must scroll horizontally to see all the data, the leftmost column, which is typically a column of row headers, should be locked in place, so users can **see the necessary labels** at all times.

*Fidelity locked investment names and column headers in place for users. The last column was slightly cut off to help users realize they could scroll to see more information.**Officeworks.com.au locked the first product in the comparison table in place, so users could compare other items against that first one. The idea here was that the first item in the comparison was the “primary” item (shown by the label* Primary Compare *) to serve as a reference in the comparison. Users could replace the selected primary item with a different one. Arrows within the body of the table indicated that users could scroll the data left and right.*

## Let Users Select the Data to View

If the data won’t fit on the screen, chances are that users won’t have the time or desire to see all of it. So the question becomes how to provide them the information that is relevant to their needs.

The answer to that question depends on the user task and the type of data, and often is more complex than a mobile interface would allow. (Learn more about information-visualization solutions in our [Application Design](https://www.nngroup.com/courses/application-ux/) course). Here are two strategies that limit the amount of data displayed on the screen and work in a variety of situations:

- Allowing the user to refine exactly which data set is needed *before seeing* data
- Giving users control of the view of data *as they are seeing* the data

The first approach works if users need to **see data, but don’t need to compare it**. They can narrow the choice of data down to the specific information they need before displaying. For instance, users may only want the features of a specific model of car, the nutrition information for a specific food item, or the statistics for a particular player, rather than comparing that information across multiple items.

*To see nutritional information for a smoothie from Jamba Juice, users first need to select the drink of interest and then are shown the data specific to that item. A toggle between* Small *,*Medium*, and *Large* allows users to select which option they are interested in, but does not aid comparison between the three. (For example, to find out the difference in calories between a medium and a small drink, the user would first have to commit the number “410” to memory, then switch to the table for the medium drink, and finally do the math subtracting the remembered number from the newly displayed number — engaging in lots of mental work that people are notoriously bad at.)*

The second solution is to provide users **control over the specific details they see**. For instance, some may be interested in the similarities or differences between two products; others may care only about certain attributes of your data — for example, they may need to compare the trunk capacity or safety features, but not the noise level of two vehicles. The ability to select what rows or columns are shown on the screen lets users focus on the subset of data that is of interest to them.

*Left: On Dell’s website, users could select the product specifications of most interest to them via a menu at the top of the page. All specifications were shown by default. Center: Users could select any product specification. Right: The resulting view showed only the user's selection.*

## Accordions for Groups of Data

If the table includes data that can be grouped into logical categories, use accordions to allow mobile users to:

- See an overview of the type of data that’s available in the table
- Have [direct access](https://www.nngroup.com/articles/direct-vs-sequential-access/) to information of interest

*On Samsung.com, comparison tables displayed all specifications, only similiarities or only differences among products, or the users’ own selection of criteria. The site used accordions to group related attributes, giving users control over what data to see at what time. The accordions also acted as an overview of content, letting users know what information was available about products.*

## Help Users Find What They Need

On small screens, users can only see a small portion of a large data table. Signposts such as locked headers orient users when they scroll through the data, and tools that narrow down content according to user-specified criteria allow them to view the data in a meaningful way.

Learn more in our day-long course on [designing for different screen sizes](https://www.nngroup.com/courses/scaling-responsive-design/).
