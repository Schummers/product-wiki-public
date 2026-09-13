---
title: "Breadcrumbs: 11 Design Guidelines for Desktop and Mobile"
date: "2018-12-23"
url: "https://www.nngroup.com/articles/breadcrumbs/"
author: "Page Laubheimer"
topics: [information-architecture, navigation, visual-design]
type: article
---

Breadcrumbs are an important navigational element that supports **wayfinding** — making users aware of their current location within the hierarchical structure of a website. Breadcrumbs are a list of links representing the current page and its “ancestors” (parent page, grandparent page, and so on), typically going all the way back to the site homepage. NN/g has been recommending breadcrumbs since [1995](https://www.nngroup.com/articles/breadcrumb-navigation-useful/), as they provide many benefits to users at almost no cost to the UI.

Breadcrumbs are represented as a trail of links at the top of the page, usually just below the global navigation; the home page (or root node of the hierarchy) is the first link and the links are usually separated by the symbols “>” or “/”. We recommend the “>” character, though there is no functional difference, and either is acceptable.

![REI breadcrumb trail showing the hierarchy of the site](https://media.nngroup.com/media/editor/2018/11/16/rei-breadcrumb-trail.png)

*REI.com: A breadcrumb trail (1) is displayed in its typical location at the top of the page, just below the global navigation bar. The trail shows the location of the current page within the hierarchy of the site. Each item in the breadcrumb trail is a link to an ancestor page; the “>” character separates the breadcrumbs. In this example, the home page and current page are omitted from the breadcrumb trail, which is not recommended.*

If users reach a deep page after traveling from the homepage through all the ancestor pages of that page, they will have a fairly clear understanding of where they are in the site’s information hierarchy. But when they skip some of these levels (for example, because they arrived to the site by clicking on an external link such as a search-engine result), breadcrumbs orient them and help them find their way to other, possibly more relevant, pages.

A deep page typically shows content on a relatively narrow, specific topic, but the breadcrumb trail can lead users to more-general content in the current page’s parent and grandparent nodes.

## In This Article:

- [Guidelines for Using Breadcrumbs on Desktop](#toc-guidelines-for-using-breadcrumbs-on-desktop-1)
- [Guidelines for Using Breadcrumbs on Mobile](#toc-guidelines-for-using-breadcrumbs-on-mobile-2)
- [Summary](#toc-summary-3)

## Guidelines for Using Breadcrumbs on Desktop

1. **Breadcrumbs should not replace the global navigation bar or the local navigation within a section.**

Breadcrumbs are intended to *supplement* other navigational components, such as a global navigation bar that stretches across the top of every page or a local navigation bar that is often found on the left hand side. Breadcrumbs augment but do not replace those main forms of navigation.

![Unusual breadcrumb that includes a drop down menu](https://media.nngroup.com/media/editor/2018/11/16/south-dakota-breadcrumbs-combined.png)

*Travelsouthdakota.com displays a breadcrumb trail that also serves as section navigation. Instead of a traditional breadcrumb trail (which would be: Home /Explore /Itineraries / Cultural Immersion), the breadcrumb trail includes a tier-1 item (Explore) and the parent page (Itineraries). The link to the parent page is a dropdown menu , with the current page’s siblings (bottom image). A better design would  have a separate UI for the local navigation, to enable users to travel to lateral pages in the current section of the site.*

1. **Breadcrumbs should display the current location in the site’s hierarchical structure, not the session history.**

Breadcrumbs are not intended to show the history of pages traversed during a session on the site (*a la* a browser’s native *Back* button); they are intended to show the hierarchical structure of the site. We’ve noted this for many years, but it still bears repeating; attempting to show a list of the pages a user has accessed, in order, will quickly become long and confusing, with a lot of repetition, and won’t provide any benefit for users who arrive on a deep page directly from an external link, which is one of the key uses of breadcrumbs.

1. **For polyhierarchical sites, breadcrumbs should show a single pathway in the site’s polyhierarchy.**

Breadcrumbs pose an inherent tension with [polyhierarchical](https://www.nngroup.com/articles/polyhierarchy/) sites (in which a page has more than one parent). In such situations, we do not recommend showing two or more breadcrumb trails reflecting the different paths in the polyhierarchy, because they will confuse users and take a lot of space at the top of the page.

If a page has multiple different parents, identify a canonical path to it in the site hierarchy and show that path in the breadcrumb trail. Don’t attempt to personalize the breadcrumb trail so that it will reflect each user’s individual path within the site hierarchy, because you will end up sending mixed signals to search engines. And you will still need to designate one path in the hierarchy as the primary trail for those visitors coming from an external link.

1. **Include the current page as the last item in the breadcrumb trail.**
2. **In the breadcrumb trail, the breadcrumb corresponding to the current page should not be a link.**

You should never have a link that does nothing. The last breadcrumb (denoting the current page) should not be a link. To avoid confusing users, visually differentiate between the current page and the preceding linked breadcrumb items, preferably using underlined or blue text.

![Breadcrumb with no visual differentiation between linked and unlinked items](https://media.nngroup.com/media/editor/2018/11/16/british-red-cross-breadcrumb.png)

*On the British Red Cross site, there is no visual differentiation between the breadcrumbs that are links and the* Volunteer in emergencies *item, which is (correctly) not a link.*

1. **Breadcrumbs should include only site pages, not logical categories in your IA.**

Each node in the breadcrumb trail should be a link to an ancestor page (with the important exception of the link corresponding to the current page, as noted above). If some of the subcategory labels in the global navigation don’t have a separate page dedicated to them do not include these subcategories in the breadcrumb trail.

The ability to “click-and-go” is a crucial part of users’ understanding of breadcrumbs, so all items (except the current page) should represent a place the user can go to.

![Breadcrumb that doesn't include logical categories from the navigation that aren't distinct pages of their own](https://media.nngroup.com/media/editor/2018/11/16/new-egg-breadcrumbs-combined.png)

*Newegg.com: The global-navigation megamenu (top) has subcategories that don’t have a page of their own — for example,* Commercial Networking **(*** 1) . On the Wired Networking page (bottom), the breadcrumb trail (2) does not include *Commercial Networking*, because that subcategory does not have an associated page.*

1. **Breadcrumbs aren’t necessary (or useful) for sites with flat hierarchies that are only 1 or 2 levels deep, or sites that are linear in structure.**

For sites with flat hierarchies with only 1 or 2 levels of categories, a breadcrumb isn’t needed as a wayfinding device. In this case, consider clearly indicating the top-level section or the category that the page lives within.

![Website with a flat hierarchy that doesn't need breadcrumbs](https://media.nngroup.com/media/editor/2018/11/16/mit-flat-hierarchy.png)

*MIT’s main website has a flat hierarchy, with only 1 page in each section. While it features a breadcrumb at the top of the page, this breadcrumb isn’t necessary. In the main navigation, the location of the page is highlighted.*

![Linear navigation site with no need for a breadcrumb](https://media.nngroup.com/media/editor/2018/11/16/npr-color-story.png)

*NPR features a minisite about the history of color, which is designed as a linear experience, where users will encounter each page in order. This site’s structure is nonhierarchical, and so there is no need (or value) in including a breadcrumb trail.*

1. **Breadcrumb trails should start with a link to the homepage**.

Much like our [guidelines](https://www.nngroup.com/articles/homepage-links/) for global navigation, links to the homepage (labeled *Home*) are still necessary. However, note that duplicating the *Home* link in both the global navigation and the breadcrumb trail is *not* recommended — one or the other is fine.

![Breadcrumb including a home link in both the navigation and breadcrumb](https://media.nngroup.com/media/editor/2018/11/16/oregon-breadcrumb.png)

*The Oregon state government website includes a breadcrumb trail, but omits a link to the homepage. However, in this case this is acceptable, as the site also includes a Home link in the global navigation — duplicating that homepage link is not necessary, but it does need to be shown in one of the two places.*

## Guidelines for Using Breadcrumbs on Mobile

Unfortunately, on mobile, the cost of using breadcrumbs can quickly overwhelm the benefits.

1. **Don’t use breadcrumbs that wrap to multiple lines.**

On mobile sites, breadcrumbs can quickly wrap to multiple lines, and eat up valuable space on an already crowded mobile display. A multiline breadcrumb trail does not illustrate the structure of the chain well (particularly when some items take up their own line, and others may have two or more links in a single row)

![Breadcrumb on a mobile site that is so large it pushes the page title below the fold](https://media.nngroup.com/media/editor/2018/11/16/rei-mobile-breadcrumb.png)

*REI.com’s mobile site uses so much real estate for the breadcrumb trail that it pushes the name of the product below the fold , even on a large mobile device (in this case, an iPhone X).*

1. **Don’t use breadcrumbs that are too small or too crowded together.**

Some sites attempt to get breadcrumbs take less screen space by making the links smaller or closer together. Unfortunately, this solution doesn’t work on touchscreens: [tap targets need to be at least 1 cm X 1 cm](https://www.nngroup.com/articles/touch-target-size/).

1. **Consider shortening the breadcrumb trail to include only the last level(s).**

On some pages, a single breadcrumb pointing up a level may be all that is necessary to support the main user goals. For example, on an ecommerce site, if a user lands on a product-detail page (via a Google search, for example), she may wish to see other product options in that same category to comparison shop, so a breadcrumb linking up to the parent level in the hierarchy can support this common task. This solution avoids a long, crowded breadcrumb trail that eats up precious mobile real estate.

Note that this advice conflicts with guideline #8, and should only be done on mobile. On desktop — where there’s more room — always show the full trail.

![Mobile breadcrumb compared with a desktop breadcrumb, where the mobile shows only the last tier in the hierarchy](https://media.nngroup.com/media/editor/2018/11/16/best-buy-breadcrumb-combined.png)

*Bestbuy.com: The mobile site (top) showed a truncated breadcrumb trail (1) , allowing access up to the immediate parent category. The desktop site (bottom) presented the full breadcrumb trail (2) . This compromise on mobile supports some wayfinding, but avoids taking up precious real estate.*

## Summary

Breadcrumbs are a secondary form of navigation that assists users in getting to content nearby in the hierarchical structure. They are especially useful when users arrive to the site through an external link and don’t start with the homepage. Ensure that all items in the breadcrumb trail are links and that each individual node gets more specific as you progress down into the site. On mobile, breadcrumbs can take up too much space or can be hard to tap; consider shortening the breadcrumb trail if your users’ tasks allow it.
