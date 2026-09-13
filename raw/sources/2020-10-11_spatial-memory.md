---
title: "Spatial Memory: Why It Matters for UX Design"
date: "2020-10-11"
url: "https://www.nngroup.com/articles/spatial-memory/"
author: "Page Laubheimer"
topics: [navigation, psychology-and-ux]
type: article
---

The ability to recall the location of things is an important aspect of [human memory](https://www.nngroup.com/articles/working-memory-external-memory/). In graphical user interfaces (GUIs), this capability is absolutely essential, as it allows users to quickly locate controls without undergoing laborious visual search each time. [Searching an interface visually](https://www.nngroup.com/articles/how-users-read-on-the-web/) for specific objects is inherently a slow and effortful process, and reducing the need for it is a huge boon to user efficiency.

For example, I recently moved and things in my new kitchen aren’t in the same places as before. The other night, I was looking for my garlic press and I couldn’t remember exactly where I had put it when I unpacked. I had to visually search every drawer in order to find it. Finding the press took a while and demanded much of my mental energy. While a good organizational system (like a good [information architecture](https://www.nngroup.com/courses/information-architecture/)) helps quite a bit, there is still a lot of scouring through drawers that needs to happen. But, with practice, I’ll eventually remember where the garlic press lives, so long as it doesn’t move from drawer to drawer!

**Definition: Spatial memory** is the ability to learn the location of objects of interest by interacting with them repeatedly. In GUIs, spatial memory allows users to develop a level of [automaticity](https://www.nngroup.com/articles/first-impressions-human-automaticity/)when accessing frequently used features or data.

For users to be able to develop spatial memory, two things are necessary:

- Stable UIs where things don’t move around (much)
- Repeated practice accessing the objects

Research in both cognitive science and human–computer interaction (such as that carried out by Jason Alexander and his colleagues in 2009 Amy Shelton and her colleagues in 2001) reveals that users develop spatial memory in *reference* to **boundaries** and **landmarks**.

For example, imagine you’re searching a paper map for a town, and you find it somewhere in the lower right part of the map. You put the map down for a while and when you pick it up again, your spatial memory of the town is in relationship to the boundary of the map. So, you’ll start by looking in the lower-right portion first.

![A person holding a paper map of Paris](https://media.nngroup.com/media/editor/2020/09/23/david-tapia-san-martin-vwgo4tgoaoo-unsplash.jpg)

*Spatial memory on a map is created in reference to boundaries, such as the the edges of this paper map or the boundaries created by the river Seine that runs through the middle of Paris (which functions both as a landmark and a boundary in this example). (Photo by David Tapia San Martin on Unsplash )*

The UX takeaway from this example is two-fold. First, clearly defined areas of controls with obvious [visual boundaries](https://www.nngroup.com/articles/common-region/) (such as toolbars) are key for users to build spatial memory. Second, when the viewport size changes (e.g., because the browser windows is resized), objects should be as positionally stable relative to the outside borders as possible. In other words, scaling the interface, rather than reflowing it, is a good strategy for supporting users’ spatial memory and should be used if you have evidence that your audience changes the window size frequently. Reflowing the whole layout (as is common with masonry-based layouts of card UIs, for example) causes a major disruption in users’ ability to relocate objects.

(But reflowing may be just fine if your users tend to not use your site or app often or if they always work with a single viewport size.)

![Two images of the MacOS Finder's Applications folder: on the left a version of the folder that is wide, and on the left, a resized view of the same folder shrunk in horizontal size)](https://media.nngroup.com/media/editor/2020/09/23/spatial-instability.png)

*The MacOS Finder reflows the* Applications *folder when the browser window is resized, pushing icons down to other rows so that there’s no horizontal scrolling. Because spatial positioning is not preserved, it becomes difficult to relocate a particular icon.*

![Two images of the MacOS Finder's documents folder: on the left a version of the folder that is wide, and on the left, a resized view of the same folder shrunk in horizontal size)](https://media.nngroup.com/media/editor/2020/09/23/spatial-stability.png)

*However, not all folders in the MacOS Finder are reflowed. In this example, the spatial positioning is preserved when the window is resized, and the user needs to scroll horizontally in order to access the items outside the current viewport. Another approach would be to shrink all the icons so that they preserve relative position to each other. That approach, of course, would have visibility and legibility limits and downsides.*

Besides boundaries, users also use landmarks to remember where objects are. Landmarks are prominent objects that stand out and are thus easy to locate — such as the Eiffel Tower in Paris or the London Eye in London. People orient themselves relative to these easily findable objects.

In a user interface users might remember that an object is, say, close to the search bar or to the hero carousel on the homepage. While this aspect of spatial memory is largely out of designers’ control, it is important to understand how users visually process the UI.

Note that spatial memory is used not only for remembering where objects are on a screen or in real life but also for navigating to these objects in both a 2D and 3D environment. The latter task involves the ability to find these objects even though they may not be in view at the moment. For example, spatial memory is involved when you’re in a new city and find your way back to the hotel (without using a mobile app). In that situation, you might rely on landmarks and boundaries to plan your route and create intermediate goals. You may recall the subway station that was closest to the hotel and create a goal to navigate to it. Once you’re there, you may use the tall building that was next to the hotel to orient yourself and find your way. This is different than looking in your refrigerator and remembering that you keep the vegetables in the bottom right crisper.

An article by Harry Hocheiser and his colleagues shows that there is a relationship between people’s abilities to navigate and build spatial memory in physical environments and their success with various user interfaces for site navigation such as sequential menus. This result makes sense, as both real-world navigational abilities, and sequential menus that only show one part of the hierarchy at a time require remembering how to access things that aren’t currently visible.

## In This Article:

- [Spatial Memory Is Inexact](#toc-spatial-memory-is-inexact-1)
- [Helping Users Build Spatial Memory](#toc-helping-users-build-spatial-memory-2)
- [Summary](#toc-summary-3)
- [References](#toc-references-4)

## Spatial Memory Is Inexact

Except for the most-accessed objects, spatial memory tends to be fuzzy: users don’t remember the exact location of an object, but rather an approximation. Spatial-memory ability varies from user to user, as studies have shown that users with [higher spatial abilities](https://www.nngroup.com/articles/mobile-subnavigation/) more accurately recall the specific location of items, but even in these cases, the spatial memory tends to be “neighborhood-level”, rather than “street-address–level.” Eventually, with **enough rehearsal and repetition**, users will develop an accurate spatial memory of the few, **most**-commonly accessed items.

![An intentionally blurry image of the AutoCAD ribbon UI](https://media.nngroup.com/media/editor/2020/09/23/fuzzy-spatial-memory-2.png)

*Spatial memory is inexact: recall of the location of controls is relatively inaccurate. This intentionally blurred image of the AutoCad ribbon UI is meant to approximate the “fuzzy” nature of spatial memory, with users recalling the “neighborhood” where controls are located, but not the specific “street address”.*

## Helping Users Build Spatial Memory

The following guidelines come with a caveat: all need to be [balanced against other UX considerations](https://www.nngroup.com/articles/efficiency-vs-expectations/) to determine the best overall design choices for your users in their specific circumstances and tasks. As with any UX design, there are [tradeoffs](https://www.nngroup.com/courses/design-tradeoffs/)between [learnability, efficiency](https://www.nngroup.com/videos/learnability-efficiency-ui-design/), and even overall user satisfaction).

These guidelines support *spatial memory* and are tailored for users who work with an interface repeatedly. In such scenarios, relocating key features and content quickly is important. The calculus might change for consumer-facing websites that users may visit only occasionally.

### Avoid Adaptive Interfaces

Adaptive interfaces rearrange the UI elements in response to expected user needs. There have been a wide variety of experimental adaptive interfaces over the years, but most have not worked well because they break users’ ability to build spatial memory.

A type of adaptive UIs that doesn’t break spatial memory is an interface with a special area for frequently or recently used items. The most common example is the frequency-based dropdown: the top most used items are often placed at the top of the [dropdown](https://www.nngroup.com/articles/drop-down-menus/). (If you use this approach, duplicate the items both in their normal place and in the *Frequently**Used* area.)

![The MS Word fonts dropdown, featuring an area for recently used fonts](https://media.nngroup.com/media/editor/2020/09/23/frequency-recency-dropdown.png)

*MS Office’s font dropdown has a* Recently Used Fonts *section at the top. Fonts that show up in the recent section are duplicated in their normal position in the dropdown.*

### Increase Salience with Text Labels and Thumbnails

As spatial memory is rather imprecise, relying only on it to find items in the UI won’t be very efficient. Since most users remember the coarse neighborhood of an object, they have to perform a visual search in that neighborhood to find the specific object. To speed up that process, designers need to supply other supplementary visual or textual cues. This means, for example, [pairing up icons with text labels](https://www.nngroup.com/videos/icon-text-labels/) or including page thumbnails in a document to help users find specific pages. [Visually salient features](https://www.nngroup.com/articles/visual-indicators-differentiators/), such as color highlighting or badges, can differentiate objects in dense lists, but use caution to prevent unnecessary visual clutter (which can slow down visual search).

### Use Broad, Shallow Hierarchies

Designing for spatial memory often means making the entire information space visible at the same time, so users are repeatedly exposed to all the items and their locations. However, this approach, besides being unrealistic when screen real estate is limited, inherently slows down visual search —[the more options](https://www.nngroup.com/articles/chunking/) that users must consider, the more time they will spend. The typical balance point of this tradeoff is to use a hierarchical organization of content or controls — as in dropdown navigation menus, ribbons, or accordions.

Unfortunately, hierarchies cause two inefficiencies for relocating items of interest: (1) they typically involve slow mechanical interactions such as dropdown menus and (2) they hide a significant part of the information space, and thus, according to [HCI studies](https://doi.org/10.1145/2207676.2207713) such as that by Joey Scarr and his colleagues negatively impact spatial memory. Thus, for quickly retrieving items that you’ve already encountered, a [broad, shallow hierarchy](https://www.nngroup.com/articles/flat-vs-deep-hierarchy/) is more efficient than a narrow, deep structure as it is both faster for spatially recalling the locations of key links and also reduces interaction cost. That’s not to say that [broad and shallow hierarchies are inherently superior](https://www.nngroup.com/videos/number-items-navigation-menu/) in all cases, but, for building spatial memory, breath is better than depth.

### Display Information-Space Overviews

Large amounts of data rarely fit on a screen and force the user to scroll. This type of information display, where data is divided across several pages or screenfuls, hinders build spatial memory of the information space.

Consider adding visualization techniques such as minimaps (common in video games and IDEs for software developers), thumbnail views of large documents, or even focus+context displays to help users build a spatial sense of the information space. These visualizations also help when users need to go back and forth through lots of information, by creating short-term spatial-memory landmarks within a large document, for example.

![An IDE code editor with a small minimap showing an tiny overview of the entire information space scaled down](https://media.nngroup.com/media/editor/2020/09/23/atom-minimap.png)

*Atom.io: The minimap on the right side shows the whole information space, along with a green highlight marking the portion the user is currently viewing.*

When using techniques such as the document overview, an [animation](https://www.nngroup.com/articles/animation-usability/) zooming into the detail pages (or back out to the overview) can build a spatial awareness of the overall information space. In fact, a study by B. Bederson and A. Boltman showed that this technique improves spatial comprehension for users.

![Apple's Preview PDF viewer showing a series of thumbnails for all the pages in a document](https://media.nngroup.com/media/editor/2020/09/23/mac-preview-overview.png)

*Apple’s Preview application on MacOS offers a spatially stable overview of a large document, that shows a zoom-in or zoom-out animation when transitioning to a specific page.*

### Create Landmarks for Users

Especially in data-rich, [high-complexity applications](https://www.nngroup.com/courses/complex-apps-specialized-domains/), users often need to comb through large volumes of data and then review several options. To support revisitation, you can create artificial landmarks called **visit wear** (or sometimes readwear)— small marks (e.g., colored dots, color changes) on either the content itself or in overview areas such as the scrollbar or the list of page thumbnails. These marks are like dog-eared pages in a book. Much like marking [visited links](https://www.nngroup.com/articles/change-the-color-of-visited-links/) on websites, visit wear helps users located already accessed content.

## Summary

Spatial memory is important for building task efficiency for repeat users. Spatial memory is bolstered through repeated use of spatially stable interfaces and can reduce the amount of cognitive effort needed to find key features or content. However, as spatial memory tends to be imprecise, assist users by including other salient visual cues and artificial landmarks, overviews of the whole information space, and by using broad, shallow hierarchies for information.

As a separate point, from a user perspective, because spatial memory (and implicitly task performance) improves when you can see more items at a time, it’s worth getting the largest monitor you can afford if you want to maximize productivity.

## References

Jason Alexander, Andy Cockburn, Stephen Fitchett, Carl Gutwin, and Saul Greenberg. “Revisiting read wear: analysis, design, and evaluation of a footprints scrollbar”. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, CHI ’09

Benjamin B. Bederson and Angela Boltman. “Does animation help users build mental maps of spatial information?”*, Information Visualization, 1999*. (Info Vis ’99) Proceedings. 1999 IEEE Symposium

Brian D. Ehret. “Learning where to look: location learning in graphical user interfaces.” In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, CHI ’02

Carl Gutwin and Andy Cockburn. “Improving list revisitation with listmaps.” In P *roceedings of the working conference on Advanced visual interfaces, AVI ’06*

Harry Hochheiser, Ben Shneiderman.Performance “Benefits of Simultaneous Over Sequential Menus as Task Complexity Increases.” *International Journal of Human-Computer Interaction*, 2009.

Joey Scarr, Andy Cockburn, and Carl Gutwin. “Supporting and Exploiting Spatial Memory in User Interfaces,” *Foundations and Trends in Human-Computer Interaction,* 2012**

Joey Scarr, Andy Cockburn, Carl Gutwin, and Andrea Bunt. “Improving command selection with commandmaps.” In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, CHI ’12*

Amy L Shelton, Timothy P McNamara. “Systems of spatial reference in human memory.” *Cognitive Psychology*, 2001.
