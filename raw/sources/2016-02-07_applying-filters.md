---
title: "User Intent Affects Filter Design"
date: "2016-02-07"
url: "https://www.nngroup.com/articles/applying-filters/"
author: "Katie Sherwin"
topics: [e-commerce, interaction-design]
type: article
---

## In This Article:

- [Introduction](#toc-introduction-1)
- [When to Apply the Filters](#toc-when-to-apply-the-filters-2)
- [Scrolling the New Results into View](#toc-scrolling-the-new-results-into-view-3)
- [Conclusion](#toc-conclusion-4)

## Introduction

Filters are among the top web innovations since, well, the Internet. These controls allow us to quickly find the needle in the haystack on information-rich sites, such as travel sites or ecommerce sites. Brands have built their reputations for their ability to narrow results efficiently. Filters eliminate items that do not satisfy specific criteria, and facets [turn search into navigation](https://www.nngroup.com/articles/search-navigation/) by suggesting categories and attributes users might want (but might not otherwise think of on their own). Filters and facets have become standard for refining large results sets.

However, while filters may look similar on many sites (e.g., they are typically placed on the left), their behaviors vary widely. In this article we focus on two dimensions of filter implementation:

1. **When to apply the filters.** Can the user adjust multiple filters before the results of the compound query are returned (**batch****filters**), or are the results returned after each filter value is specified (**interactive****filters**)? Or, can the results be computed and displayed quickly enough that this dimension is irrelevant?
2. **Whether the new results should be scrolled into view.** Once the query is submitted, does the page scroll back to the top to show the results or is the current position on the page preserved to allow users to continue specifying more filters without distraction?

Both these dimensions inform the **continuity of the user experience**. The overarching theme in selecting an implementation should be to **not fragment the user experience,** and let users smoothly progress towards their goals while maintaining a sense of UI stability and [user mastery](https://www.nngroup.com/articles/ideologies-of-web-design/).

## When to Apply the Filters

Continuing [our restaurant UX analogy](https://www.nngroup.com/articles/ux-learn-in-restaurants/), think about how you might order appetizers at a restaurant. Say you want to order three appetizers for the table, but as soon as you name the first one, the waiter snatches the menu out of your hands and walks back to the kitchen to get the chefs started on cooking that dish. Instead, a good waiter understands that you’re still in the process of ordering and knows to give you more time before taking away the menu. A good waiter **allows you time to****make a batch decision**, even if that might slightly delay the delivery of the first item ordered. (However, sometimes the waiter may take the appetizer order, and then give you more time to decide on the main course. A good waiter is flexible and adapts to the needs of the customers.)

Just like it would be disruptive for the waiter to immediately walk away every time you named an item from the menu, for users who intend to select more than one facet, it’s disruptive and tiresome to refresh the page every single time they make a selection, especially if the site is slow.

Choosing between a batch and an interactive filter implementation will depend on both **user intent** (does the user plan to specify multiple filtering criteria or just one) and **site speed** (how fast the results are presented to the user).

### User Intent

Intelligent filtering mechanisms **recognize when users are still thinking** and do not refresh the page until the user is done making selections. The big problem then is how can the system know if users are ready to see the updated results? How can a system be like a good waiter?

The first question to ask is whether users are in an exploratory mode or they have clear search parameters in mind. Users who do not have a clear search goal still need to [learn about the structure of the search space](https://www.nngroup.com/articles/search-not-enough/) and the possible options that are available to them. These users will benefit most from **interactive** filtering. They make one selection, and the system updates the results. After looking through the updated results, they get an idea for another filter, select it, and the system updates the results again, and so on.

Interactive filtering is usually associated with facets: as soon as users have selected a new possible facet, the results are displayed along with the set of new applicable facets (e.g., once the user has selected *Refrigerators*, new range-specific facets such as *Freezer volume* will be displayed). Often, facets also show the number of elements available under each filter, and thus help users avoid zero-search results.

Alternatively, users who already have multiple criteria in mind will benefit from **batch** filtering. For example, a customer shopping for a “little black dress” might go to a *Dresses* category and immediately look to the filters to refine by color, length, style, and size. For these shoppers, the experience will be smoothest if the system waits for them to finish making selections before it loads the new results set. The biggest disadvantage of batch filtering is that there is a risk that users will select a combination of criteria that leads to zero results. Delaying the presentation of results makes it difficult to give users continuous feedback about which filters are available or disabled and how many results there are for each filter. The advantage is however that it saves users extra wait time between queries, and that instead of waiting through multiple queries (one for each attribute) they can only wait for one.

For designers, it is **difficult to accurately predict users’ mindset while they are filtering**. Here are some rules of thumb to help you figure out the users’ goals:

- **Let users tell you when they’re done selecting filters.** This essentially means to err on the side of batch filtering and include an *Apply* button in your filter design. Users can click on that button once they’ve indicated all the filter values that they are interested in. This is the recommended approach on mobile devices, [even with the new tray design pattern](https://www.nngroup.com/articles/mobile-faceted-search/). However, this method implies that you’re failing your exploratory users, who may not be sure of what attributes they are interested in.
- **Detect activity around the filters.** Look for user movement via mouse hover or keyboard focus. If users are moving the mouse around the filters (or using the keyboard to tab between them), they may be on their way to make another selection. Conversely, if the mouse leaves the filter area and moves to main results, it’s a good sign that users are ready for the results. Note that even if there is some movement, this works best when a time limit is used as a fallback (see #3 in this list).
- **Update results based on the time since the last selection.** If a user hasn’t made another selection or moved the mouse after a certain amount of time (1–2 seconds), then display the new results. Of course, the system should still give immediate feedback (e.g. a [progress indicator](https://www.nngroup.com/articles/progress-indicators/)) to acknowledge that the first selection was received.

*Houseoffraser.co.uk: An example of effective batch filtering. The system allows users to keep making selections while users are active in the filter area. After a few moments of user inactivity, the system displays the results with all the filters applied.**(In most browsers, hover over the video to display the controls if they're not already visible.)*

### Site Speed

The other variable that influences the choice between interactive and batch filtering is **the speed of the site**: how fast you can produce the results. If you expect the queries to be instantaneous (and the new results to be [shown less than one second](https://www.nngroup.com/articles/response-times-3-important-limits/) after each filter has been specified) then interactive filtering will be less offensive even to users in search mode. If however your site is likely to be slow at least occasionally, then the batch filtering can save users some wait time. That is the main reason for which, on mobile devices, we recommend batch filtering — page loads are often slow on the go, and having to wait for four page loads for a complex query involving four filter values increases [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition) too much for the user.

### Continuous Feedback: A Warning

Interactive filtering has another disadvantage: continuous updates can be visually distracting, even if they are fast and don’t scroll the page. Any time items in a results list update, the flicker of an image swap will attract attention (though it probably will not be clear what exactly changed). Flickering in the peripheral vision is annoying and may also cause the user to waste time looking at the preliminary results. That said, visual cues are necessary so that users are aware that a change has occurred (i.e., to prevent [change blindness](https://www.nngroup.com/articles/change-blindness/)).

To balance the advantages of continuous feedback without distracting users’ peripheral vision, many effective faceted navigation systems dim the results set and show a progress indicator before displaying the new results. This way, the change that users detect is a single dimmed area (instead of individual items seemingly flashing on and off the screen).

![Results dim while updating](https://media.nngroup.com/media/editor/2016/02/03/dimmed-filter-results.png)

*Net-a-porter.com: The moment between when a facet is selected (in this case,* Black *) and the new results are displayed minimizes visual distractions; the entire results area dims and an animated spinner shows progress. Even with a fast system, designs should avoid visual changes that happen too quickly, becoming annoying and distracting.*

## Scrolling the New Results into View

Remember that our goal is to achieve a smooth user experience. What happens to the page view once users apply the filters is the second stage of this experience. This stage also depends on correctly recognizing user intent. Unfortunately, many sites fragment the experience during this part of the interaction.

For example, Houseoffraser.co.uk disappoints after the filters are applied: the page scrolls back to the top of the results. This will usually cause users who are still looking at the filters to lose their place on the page and become disoriented. But worst of all, it increases the chances of an accidental click on the wrong category if users are in the process of selecting a filter and the page scrolls at the same time.

*Houseoffraser.co.uk: Jumping the results page to top can cause users to accidentally select unintended facets. (In most browsers, hover over the video to display the controls if they're not already visible.)*

On the other hand, scrolling to the top of the page has some benefits as well. First, the best results will appear at the top of the list: if relevance or popularity declines dramatically with results lower down on the page, then users will see the best options sooner if they are taken to the top of the page. Second, after filtering, there may be too few results and the page might refresh to a blank screen next to the filters. In both these situations, it is better to send users to the top of the page so that they can see the changes.

![New results are not visible without scrolling up](https://media.nngroup.com/media/editor/2016/02/03/results-dont-scroll-into-view.jpg)

*Kayak.com: After adjusting the price filter to show flights up to $500, the page refreshes the results to the current page position. Unfortunately, no results are visible at this view, because only six matching flights were found. The empty screen can be interpreted as the system still working, or as zero results. It would be better to refresh the page to the top of the results list.*

Note that the main problem here is, again, failing to recognize the user intent — namely that the user is still engaged with the filters area. The same techniques that we describe in the first section of the article can be successfully applied to determine whether it’s safe to scroll up or you should wait a few more seconds until the users are done with interacting with the filters.

## Conclusion

By detecting users’ intent to select additional filters, sites can offer a smoother, more efficient filtering experience. Use interactive filters if your users are exploratory in their search. Use batch filtering when your users have clear refinement criteria, or you know that your site will be slow at least occasionally (e.g., on mobile devices).
