---
title: "Polyhierarchies Improve Findability for Ambiguous IA Categories"
date: "2018-05-13"
url: "https://www.nngroup.com/articles/polyhierarchy/"
author: "Page Laubheimer"
topics: [information-architecture, navigation]
type: article
---

## In This Article:

- [Introduction](#toc-introduction-1)
- [Definition](#toc-definition-2)
- [Restrained Use of Polyhierarchies Supports Multiple Mental Models](#toc-restrained-use-of-polyhierarchies-supports-multiple-mental-models-3)
- [Wayfinding and Polyhierarchies Can Conflict](#toc-wayfinding-and-polyhierarchies-can-conflict-4)
- [Conclusion](#toc-conclusion-5)

## Introduction

Creating a perfect [information architecture](https://www.nngroup.com/courses/information-architecture/) (IA) for a website is tough, especially when it comes to balancing precision and clarity. Ideally, you want to create categories that accurately describe your content and products, are extensible when you add new topics or products, and match your users’ [mental models](https://www.nngroup.com/articles/card-sorting-definition/)(which often vary from one person to another).

The most common IA hierarchy is structured as a tree, in which each node (except for the one corresponding to the homepage) has a single parent. (Note that while we’re talking about the [invisible IA structures underlying a website](https://www.nngroup.com/articles/ia-vs-navigation/), these are usually reflected in the navigation UI as well). This type of hierarchy often poses a problem, however: some things don’t fit cleanly in just one category, but they naturally have multiple parents, depending on one’s point of view. Here is where polyhierarchies come in.

![Site map of a website, including polyheirarchies](https://media.nngroup.com/media/editor/2018/04/27/site-map.png)

*This diagram depicts a website’s underlying IA. The IA is structured as a tree: each node (except for the homepage) has a parent, and some nodes have child nodes. The green item at the top is the root of the tree; its children are the 1st-tier categories (blue). Each of those blue nodes has multiple (gray) 2nd-tier child nodes. Note that two of the 3rd-tier items (in orange) are polyhierarchical, as they have more than one parent node.*

## Definition

**Definition**: A polyhierarchy refers to a graph structure in which at least some *child* nodes have more than one *parent* nodes.

A polyhierarchical IA is a structure where an item exists in more than one place ­— that is, it can be reached following several category paths. A classic example of an object in a polyhierarchy is the piano within the hierarchy of musical instruments: a piano could be considered a keyboard instrument, a percussion instrument, or a string instrument (pressing a key on a piano forces a tiny hammer to hit a string). So, if you were creating a hierarchy of all musical instruments, where does the piano fit? Since it can comfortably fit in several categories, a solution is to place it in all of these *parent* categories (*keyboard*, *percussion*, and *strings*).

Polyhierarchies pose a big difficulty for physical objects: if you only have one copy of a book (or only one piano), it can only be in one place. To avoid polychierarchies, many complicated ways of classifying items emerged; they involve carefully structured taxonomies and judicious use of crossreferencing (such as the Library of Congress’s classification system, for example).

However, if we tried to avoid a polyhierarchy when deciding where to put the piano, we’d have to create mutually exclusive categories which could appropriately handle instruments like this. These artificial categories can easily increase the complexity of taxonomies and make them inaccessible to lay people. One example of such a complicated taxonomy is the [Hornbostel-Sachs](https://en.wikipedia.org/wiki/Hornbostel%E2%80%93Sachs) musical-instrument classification, in which instruments are classified by how they produce the air vibrations that make the sound. (The piano is considered a chordophone in this system.) While that might work from a technical perspective, it’s not helpful for regular people whose mental models don’t include things like chordophones, idiophones, membranophones, and so on. These categories are so obscure that most users would skip right over them, rather than trying to figure out what they mean.

Clearly, polyhierarchies have their uses. Luckily, the digital world easily [affords](http://www.jnd.org/dn.mss/affordances_and.html)polyhierarchies, as long as we use them thoughtfully.

## Restrained Use of Polyhierarchies Supports Multiple Mental Models

Polyhierarchies are useful on [ecommerce sites](https://www.nngroup.com/reports/ecommerce-ux-homepages-and-category-pages/), where having the same product category appear in multiple places supports several different mental models. For example, on Target.com, the products were organized in an extensive polyhierarchy. The product subcategory *Nintendo Switch* could be found both in the *Video Games* and *Electronics* top-level categories. This decision reflects the fact that different users assume that either *Video Games* or *Electronics* are the natural “home” for the Nintendo Switch and its games and accessories; if the site didn’t include both of these two parents for *Nintendo Switch*, it would likely lose customers who chose the “wrong” category and couldn’t find what they were looking for. (Users frequently assume that, if a product is not present in the place where it “ought” to be, the site doesn’t carry that product.)

![Wireflow of Target.com's polyhierarchical placement of Nintendo Switch](https://media.nngroup.com/media/editor/2018/04/27/target-navigation.png)

*Target used a product-category polyhierarchy to make items findable; for example,* Nintendo Switch *was listed under both* Video Games *and* Electronics *top-level categories.*

However, Target notably avoids putting the *Switch* in every possible parent category (e.g., *Toys)* that could conceivably include it. This aspect of designing polyhierarchies is important because exhaustively crossreferencing every single place where a particular item could sit would swell each menu with tons of items, and add significant[cognitive strain](https://www.nngroup.com/articles/navigation-cognitive-strain/) for users. Navigation menus are meant to help people find the content they seek and discover unexpected but relevant items; they should not be tortuously long lists. For huge, complex sites with tremendous overlap in categories, a better solution is to use [facets](https://www.nngroup.com/articles/filters-vs-facets/) to provide robust search aids.

So, how do you determine if an item should have multiple parents? The answer involves understanding users’ mental models for your information space. There are multiple ways to collect this data. One solution is to conduct **closed**[card sorting](https://www.nngroup.com/videos/card-sorting-organize-product-offerings/?lm=bias-card-sorting&pt=youtubevideo) (where users have to sort cards into existing categories) or [tree testing](https://www.nngroup.com/articles/tree-testing/). If in that study you discover that different users tend to place that item in two different categories, then you can add it to both those categories. Another solution is to test the item’s findability during moderated [usability tests](https://www.nngroup.com/courses/usability-testing/); if you find that some users reasonably expect another parent category for that item, then you can use that data as a basis for your decision.

## Wayfinding and Polyhierarchies Can Conflict

A big drawbacks for polyhierarchies is that they conflict with navigational [wayfinding](https://www.nngroup.com/articles/navigation-you-are-here/) elements, particularly [breadcrumbs](https://www.nngroup.com/articles/breadcrumb-navigation-useful/). Breadcrumbs exist to show users where they are, and how the current page fits in the site hierarchy.

We’ve known for many years that breadcrumbs should show the location of the current page in the site’s IA, not the user’s browsing history. What does that mean for nodes with multiple parents? Because sites cannot succinctly represent polyhierarchies (as well as for SEO and content-governance reasons), a “canonical’ path to a page will be shown in the breadcrumbs. However, this canonical path can potentially conflict with the path that the user took to access that particular page.

Unfortunately, this is a tradeoff that needs to be made. The alternative involves giving up breadcrumbs altogether. This solution can work for shallow hierarchies with fewer than 3 levels, but it can lead to disorientation and navigation difficulties for deeper hierarchies.

![Target.com's use of breadcrumbs showing the primary location of the page](https://media.nngroup.com/media/editor/2018/04/27/target-breadcrumbs.png)

*Target showed breadcrumbs that described the primary location of* Nintendo Switch *in the polyhierarchy, even though this page was located both in* Home > Video Games > Nintendo Switch *, and* Home > Electronics > Video Games > Nintendo Switch *.*

## Conclusion

Polyhierarchies are IA structures in which a single item fits in more than one parent categories. They primarily exist to accommodate multiple mental models that different users have for the natural “home” of a page. While digital tools make polyhierarchies possible, they should be used with restraint: too many parents for any given node increase cognitive load and make navigation difficult.

Learn more in our full-day [Information Architecture](https://www.nngroup.com/courses/information-architecture/) seminar.

**References**

Morville, P., Rosenfeld, L., and Arango, J. (2015). *Information Architecture, 4th Edition*. Sebastopol, CA: O’Reilly Media

Kalbach, J. (2007). *Designing Web Navigation: Optimizing the User Experience*. Sebastopol, CA: O’Reilly Media
