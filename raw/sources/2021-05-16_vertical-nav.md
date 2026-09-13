---
title: "Left-Side Vertical Navigation on Desktop: Scalable, Responsive, and Easy to Scan"
date: "2021-05-16"
url: "https://www.nngroup.com/articles/vertical-nav/"
author: "Page Laubheimer"
topics: [information-architecture, navigation, visual-design]
type: article
---

Every time I talk about [broad hierarchies](https://www.nngroup.com/articles/flat-vs-deep-hierarchy/) in our UX Conference course on [information architecture](https://www.nngroup.com/courses/information-architecture/), two questions come up:

1. Is it okay to have more than 7-9 top-tier categories in the global navigation? (Spoiler alert: [it is okay](https://www.nngroup.com/videos/number-items-navigation-menu/), you just need to plan appropriately for it.)
2. If we go with a large number of top-tier categories, they don’t fit in the horizontal navigation bar. Where should they go?

Many teams will try to shoehorn a broad navigation hierarchy into a horizontal navigation bar on desktop sites. To make the list of categories fit into the limited horizontal space, they will use excessively **small font** sizes, **crowd** items close to one another, or come up with unnaturally **short category labels**. Worst of all is changing the IA so that there are only as many main categories as will fit in the available space. When we limit a broad information space into a small number of categories, we will end up with top-tier items that are too generic and will make it difficult for users to find what they need. Moreover, users will have to work more (clicking around and scanning various lower-tier categories) to find the relevant category.

![B2B website navigation that presents a large number of subcategories under a single Services top level category](https://media.nngroup.com/media/editor/2021/05/11/accenture.png)

*Accenture hid a broad information space under a single* Services *category in order to artificially limit the number of top-level categories. Findability of specific consulting areas was reduced and interaction cost was increased (because people had to open various top-level categories, scan them, and decide they were not right).*

However, there is another type of main-navigation UI that, on desktop, can accommodate as many top-tier items as needed — **vertical, left-side navigation**.

![Restaurant website with a left-side vertical navigation](https://media.nngroup.com/media/editor/2021/05/11/arbor-restaurant.png)

*Arbor Restaurant’s website easily accommodated 13 global navigation categories using a vertical-navigation pattern. This navigation UI allowed for main categories that are specific and with high information scent and saves the users the interaction cost of first selecting a generic top-level category before seeing specific options.*

## In This Article:

- [Benefits of Vertical Navigation](#toc-benefits-of-vertical-navigation-1)
- [Vertical Navigation Requires More Space](#toc-vertical-navigation-requires-more-space-2)
- [Guidelines for Usable Vertical Navigation](#toc-guidelines-for-usable-vertical-navigation-3)
- [Summary](#toc-summary-4)

## Benefits of Vertical Navigation

Most benefits of this navigation UI derive from its ability to accommodate many top-tier categories.

1. **Specific categories increase findability and decrease interaction cost.**

Using vertical navigation removes the visual design constraints that limit the number of categories, allowing the team to create an IA that naturally fits the information space, and expose specific, high-[information scent](https://www.nngroup.com/videos/information-scent/) categories to users without requiring them to dig into the second tier of the hierarchy

1. **Vertical navigation offers room for growth.**

Vertical navigation is an excellent choice for sites where the navigation is likely to grow in the future — large organizations that may continually evolve their offerings or content, in areas such as B2B, enterprise, government, higher education, and healthcare. Adding additional categories to the vertical navigation doesn’t require a major process of redesigning the navigation UI; the only major decision is how the new items should be blended into the existing category structure.

1. **Vertical navigation supports more efficient scanning than horizontal navigation.**

We know from eyetracking studies that attention leans left on websites: [users look at the left half of the screen 80% of the time](https://www.nngroup.com/videos/attention-leans-left-websites/). The real estate on the left side of the screen is valuable, and placing your navigation there makes it likely to be noticed and scanned by your users.

Additionally, research in psycholinguistics shows that visual search in a list is more efficient if the list is vertical than if it is horizontal — people are able to find an item of interest with fewer eye fixations, simply because much more information can be derived from a single fixation. (Remember that the eye is able to perceive information not only from the exact location where it fixates but also from a relatively small area around it. As a result, even when we do read every single word in a sentence, we need to fixate only on a few of them.)

![Website navigation with left-side vertical navigation that is center aligned](https://media.nngroup.com/media/editor/2021/05/11/sunglass-hut-old.png)

*A previous design for Sunglass Hut used a left-side vertical navigation, but center-aligned the text of each navigation element, creating a jagged edge that undermined the visual scanning benefit of a vertical list of items.*

![A website's navigation with a horizontal bar, featuring the logo in the middle of the navigation](https://media.nngroup.com/media/editor/2021/05/11/solstice-sunglasses.png)

*Solstice sunglasses placed navigation options in a horizontal navigation bar, making it marginally more effortful to scan across the list. This design’s effectiveness was also compromised by center-placing the logo .*

Note that a common misconception is that horizontal-navigation designs support the [F-shaped](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/) reading pattern. However, the F-shaped pattern is encountered when users read a piece of unstructured text, which is definitely not applicable for the navigation, header, or other page chrome.

1. **Users are familiar with vertical navigation**. Despite being less common on contemporary websites, vertical navigation is frequently encountered in desktop applications (both native apps and webapps).

![A dual screenshot of the navigation panels for both Slack and Gmail](https://media.nngroup.com/media/editor/2021/05/11/slack-and-gmail.png)

*Slack and Gmail are examples of widely used web applications that use vertical left-side navigation.*

In addition, many websites use **vertical local navigation** (i.e., showing the current page’s “sibling” pages, that are part of the same category in the site hierarchy).

![A website with left-side navigation for pages within the parent category](https://media.nngroup.com/media/editor/2021/05/11/logitech.png)

*Logitech used left-side vertical navigation for the local navigation options to various pages within a specific product’s section, a very common approach on the web.*

1. **Vertical navigation translates naturally to mobile.** Translating a horizontal menu bar to a [mobile-friendly design](https://www.nngroup.com/articles/mobile-navigation-patterns/) may require some tweaking, as the menu bar is usually transformed into a vertical navigation (often shown under a hamburger menu). In contrast, using a vertical navigation for desktop and mobile allows the team to apply the same visual-design choices with relatively minimal adaptation. Borders, type, spacing, order of the categories, and UI for second-tier categories can be shared across devices.

![The same navigation for a website's desktop and mobile versions remains the same as it is a vertical navigation pattern](https://media.nngroup.com/media/editor/2021/05/11/heywood-golf-responsive.png)

*heywoodgolf’s vertical navigation easily adapted from desktop to mobile sites, with few design changes necessary to make the design look, work, and feel appropriate for the platform.*

**That being said, don’t be tempted to hide your desktop navigation under a vertical (hamburger or other) menu**. Visible navigation is the gold standard for both mobile and desktop. While some mobile websites may be forced to hide most or all of the navigation under a [hamburger menu](https://www.nngroup.com/articles/support-mobile-navigation/) due to the limited screen space, there is a huge [discoverability](https://www.nngroup.com/videos/hamburger-menus/)benefit from using a visible navigation. When navigation is hidden, people simply forget to check it. Moreover, on desktop a hamburger menu has a such a small footprint relatively to the rest of the page, that its chances of being ignored are even bigger than on mobile.

## Vertical Navigation Requires More Space

The main drawback to using vertical navigation compared to horizontal navigation is that it takes up more space and, as a result, there is less room available for content. Vertical navigation usually results in pages with a lower [content-to-chrome](https://www.nngroup.com/articles/content-chrome-ratio/) ratio than horizontal navigation.

![Comparison of an old and new version of a website.  The older version has a vertical navigation (which takes more space) and the new version, which has horizontal navigation (which takes less space)](https://media.nngroup.com/media/editor/2021/05/11/nua-bikes-content-to-chrome.png)

*Nua Bikes old and new designs. (Left) a Previous design of Nua Bikes used a vertical, left-side navigation which had an approximate 5:1 content-to-chrome ratio. (Right) a redesign of the site moved to a horizontal navigation bar with a 12:1 content-to-chrome ratio on the same screen size. While the new design exposes far fewer top-level categories in the visible navigation, it does take up much less content space.*

At small window sizes (like those encountered on smaller displays or tablets), this tradeoff may be challenging to accommodate. If you are working with a responsive design, you may need to decide what the right navigation UI should be for various breakpoints (i.e., window sizes) and at what display size a vertical navigation will lead to a decent content-to-chrome ratio. Bear in mind, however, that as you approach the large window-size end of the spectrum, vertical navigation will most likely no longer affect the content-to- chrome ratio (as often the viewport area will be filled with blank space on right and left when the display is really big).

![A website with left-side navigation on a very large display with extra empty space to the left and right](https://media.nngroup.com/media/editor/2021/05/11/watson.png)

*IBM’s Watson Studio: On a very large display, the impact of vertical navigation on the content-to-chrome ratio is negligible, as the site adds whitespace (or in this case, empty dark background space) to the left and right.*

A very long vertical menu may have some items below the page fold. We know, from much research, that users pay more attention to information above the fold than to that below the fold. They might not even scroll at all if what they see above the fold looks useless for their current goal. (Remember that users are [very quick to leave web pages](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/) they deem useless.) On the other hand, vertical navigation is a sufficiently well-established design pattern that most users will know to scroll if they don’t see the full menu—assuming that the information that’s visible above the fold convinces them that the site might be useful.

## Guidelines for Usable Vertical Navigation

1. **Place vertical navigation on the left and use a noticeable design.**

As noted earlier, visual attention leans to the left side of the screen. That, coupled with the fact that we often see [right-rail blindness](https://www.nngroup.com/articles/fight-right-rail-blindness/) (where users avoid looking at the right column of the page if it looks like it could contain ads) means that navigation on the right side of the page is less likely to be noticed. (As always with left-vs-right guidelines, this advice applies to languages that read left to right. If your language reads right to left, the opposite advice applies.)

Furthermore, make sure that the navigation is visually salient. Different text or background colors and borders can make it stand out from the other page elements.

![Vertical navigation with a high-contrast dark background against a light page content area.](https://media.nngroup.com/media/editor/2021/05/11/audi-design-system.png)

*Audi’s design system used high contrast and a dark background to ensure that the left-side navigation was noticeable and that the links were readable.*

1. **Don’t duplicate the menu both vertically and horizontally.**

A recent odd trend consists of using two redundant UIs for the global navigation: a horizontal menu bar and a hamburger menu with the same categories. It almost feels like the design team wasn’t sure which UI should be used, so it included both. This duplication (like most duplication of UI elements) is [unnecessary and potentially confusing](https://www.nngroup.com/articles/reduce-redundancydecrease-duplicated-design-decisions/).

![Website with both a hamburger menu and duplicate horizontal navigation](https://media.nngroup.com/media/editor/2021/05/11/bdo.png)

*BDO Advisory used two redundant global-navigation UIs: a horizontal bar and a hamburger menu on the right side of the screen. These two menus contain the exact same items, but the hamburger menu also includes the items from the site’s*[utility navigation](https://www.nngroup.com/articles/utility-navigation/)**(Locations, Events, News, *and so forth). This duplication is unnecessary and confusing.*

1. **Don’t hide the navigation behind icons.**

Since vertical navigation takes up more space than horizontal navigation, designers often attempt to minimize its corresponding area. This is certainly an understandable objective, but some means of achieving it end up creating additional problems. One emerging trend has been to use icons instead of text labels for categories. While text labels are available for every navigation item, the user can see them only when clicking, tapping, or hovering on the navigation bar.

We have recommended for years to add [labels to icons](https://www.nngroup.com/videos/icon-text-labels/). Not only does text reduce ambiguity, but it also [increases the target size](https://www.nngroup.com/videos/fittss-law/). Yet, we still see sites that assume their users will instantly understand their icons for navigation categories. I often say that in navigation, a word is worth a thousand pictures.

Hiding the navigation text labels means that users will be most likely to simply ignore the navigation (as often happens with a hamburger menu). Those users who *do* interact with it must carry either the additional interaction cost of hovering or clicking to see the text labels or the additional [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/) of attempting to decode what the icons mean.

The strategy of minimizing the navigation to a series of icons (where the default is *showing* the text label, and hiding it is optional) may be a realistic compromise for applications used every day, where the user may well [learn](https://www.nngroup.com/videos/learnability-efficiency-ui-design/) what the categories represent. However, on a website that sees only occasional use by each individual user, this is not a recommended strategy.

*NOAA’s desktop site showed icons for the global navigation categories by default, requiring the user to click on an icon to see the text labels for the categories. This design also increased the interaction cost of using the navigation, since the user must click twice to move to that page: once to open the menu and a second time to follow the link.*

1. **In long menus, place less-important ones at the bottom.**

Due to the usability problems caused by the page fold (discussed above), a very long vertical menu risks having items that are not visible without scrolling. Unfortunately, since different users have differently sized monitors, you can’t know where the page fold will hit your menu for any individual user. For long menus, prioritize the items so that the ones that are likely to be invisible without scrolling are among the less important features.

## Summary

Vertical navigation can be a reasonable choice on the desktop, particularly for sites that have a broad range of content, are rapidly growing, or simply want to surface specific categories for users. Vertical navigation is also easy to adapt for mobile. To keep vertical navigation helpful, don’t hide it under a hamburger menu, use left-aligned, keyword-frontloaded labels (not just icons) for categories, and weigh whether its benefits justify the space taken away from the content area.
