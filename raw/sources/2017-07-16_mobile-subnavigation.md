---
title: "Mobile Subnavigation"
date: "2017-07-16"
url: "https://www.nngroup.com/articles/mobile-subnavigation/"
author: "Raluca Budiu"
topics: [mobile-and-tablet-design, navigation]
type: article
---

Many websites have fairly complex [information architectures](https://www.nngroup.com/articles/ia-vs-navigation/), with many levels of categories. While lower-level categories are often shown on desktop in [dropdown menus](https://www.nngroup.com/articles/drop-down-menus/) or [mega menus](https://www.nngroup.com/articles/mega-menus-work-well/), presenting these subcategories on mobile devices is not always straightforward.

*Cisco.com: The desktop site uses a horizontal navigation bar holding the primary categories. On mouse hover, each primary category expands as a megamenu with corresponding level-2 and level-3 subcategories. The mega menu is visually divided into three columns (* Products, Solutions, Services)*and also contains a list of tabs at the bottom (* Enterprise, Service Provider, Small and Medium Businesses *).*

How should these [expandable menus](https://www.nngroup.com/articles/expandable-menus/) be translated on mobile? **The small screen size cannot easily accommodate many subcategories**. While Cisco’s desktop site can display 30 or more subcategories in its mega menus fairly comfortably, without forcing users to scroll, those categories will not easily fit on a single mobile screen. Plus, some of the visual structure afforded by the two-dimensionality of the megamenu will not be easily apparent on mobile, simply because not all subcategories will be visible at the same time.

## In This Article:

- [Subnavigation: Design Goals](#toc-subnavigation-design-goals-1)
- [Types of Subnavigation on Mobile](#toc-types-of-subnavigation-on-mobile-2)
- [Sequential Menus](#toc-sequential-menus-3)
- [Section Menus](#toc-section-menus-4)
- [Category Landing Pages](#toc-category-landing-pages-5)
- [Conclusion](#toc-conclusion-6)
- [References](#toc-references-7)

## Subnavigation: Design Goals

Definition: **Subnavigation** refers to the navigation UI that helps users access lower-level categories in the site’s information architecture (IA).

When designing subnavigation, aim for the following design goals:

1. **Minimum interaction cost:** Users should be able to access an element of interest in the navigation with as little effort as possible. That means few taps, little scrolling, and zero page loads if possible.
2. **Typical-path support:** If, within a single session, users are likely to jump from a page in one section to another one in a completely different area of the site, subnavigation should make it easy. If, on the contrary, most visitors will “live” in a single section of the site (say, the sports section of a newspaper), then the subnavigation should focus on supporting that pattern.
3. **Discoverability:** Users should be able to find the subnavigation UI quickly, with no chance of confusing it with the main navigation.

## Types of Subnavigation on Mobile

There are four common ways to design subnavigation on mobile:

- Accordions (aka “submenus”) inside a main navigation menu, such as a [hamburger menu](https://www.nngroup.com/articles/hamburger-menus/)
- Sequential menus
- Section menus
- Category landing pages

### Accordions Inside a Main Menu

When the primary navigation is hidden inside a pull-down menu, a simple way to implement subnavigation is to use accordions for the primary categories, with each accordion expanding to expose its corresponding subcategories. This design feels like a “submenu” inside a larger menu.

*Tide.com uses accordions inside a main navigation menu to display subnavigation.*

Submenus work well when they contain just a few subcategories (typically less than 6), so that the navigation menu is not overly long at any time. When there are many subcategories inside a main category, submenus lengthen the main navigation menu too much and make the task of finding information inside it tedious.

*SBNation.com uses accordions to expand the main navigation categories. Unfortunately, the subcategories span more than 3 screenfuls and make it hard for people to find any one item of interest. (However, the fact that the menu contains team names ordered alphabetically compensates somewhat for this problem, since users don’t need to read all the labels and can scan for the desired team.)*

When the navigation menu is present on all pages of the site, this subnavigation design fares the best with respect to the goals set in the previous section:

- It has a low interaction cost, because users can access subcategories in the site’s IA anywhere on the site (if the menu is present on that page), without waiting for an extra page load.
- It supports all paths through the site, not only typical ones. Thus, it is well suited for situations where there is no dominant site-navigation pattern and allow users to easily jump through different branches of the site’s information hierarchy.
- Since it is part of the main navigation, there is little danger of people getting confused by having to choose between two navigation UIs. However, it is still important to make sure that primary categories look different than lower-level ones in the main menu (using indentation and perhaps color to distinguish between them).

*Seventhgeneration.com: The primary categories are shown in a different color than the lower-level categories.*

## Sequential Menus

**A sequential menu** is a menu which shows only the subcategories of the last selected category. The sequential menu starts by displaying the primary categories; once people select one of them, the list of primary categories is replaced by the subcategories of the selcted category. The popularity of sequential menus has increased significantly on mobile in the past few years, as they seem an easy solution to the problem of displaying many categories and subcategories on a small screen.

*HIV.gov: When selecting a primary category (* HIV Basics *) from the main menu, the corresponding subcategories are shown instead of the original content menu. The user can navigate up in the information hierarchy by tapping the button* Back *inside the menu.*

Research in [human–computer Interaction](https://www.nngroup.com/courses/hci/) is split on the effectiveness of sequential menus: some studies seem to indicate that people do just fine with them, at least for tasks that are not overly complex and that do not demand navigation in different areas of the same hierarchy. Users with low spatial ability (as measured by a spatial-ability test), however, seem to be less efficient with these menus than users with high spatial abilities. And unfortunately, on mobile devices, due to the increased probability of interruption, we are more likely to become disoriented and behave like users with poor spatial abilities.

Sequential menus cause users to accidentally make mistakes, especially on Android phones (or in a browser) — often people are tempted to use the phone’s physical *Back* button or the browser’s *Back* button, and accidentally end up closing the menu and navigating to a different page instead of moving back to the higher-level menu.

*Hiv.gov: Users who accidentally tap the Android phone’s physical* Back *button to go up in the menu are taken instead to the previous page that the user had visited in the browser. To get to the upper level of the menu hierarchy, they must use the* Back *button inside the menu. (As a separate point: we don't recommend showing menus directly over a busy image , as shown in the bottom screenshot.)*

Some sites purposefully use a different label instead of *Back* for navigating up in the information hierarchy. For example, on Macy’s site, a trail of breadcrumbs is shown in the menu to allow users to go up in the IA.

*Macys.com: This sequential menu displays a trail of breadcrumbs (* Menu-> Shop-> Women *) for the current menu view, so users have less of a chance to get confused or accidentally press the physical* Back *button when they want to navigate up in the parent hierarchy. (Note, however, that the breadcrumb trail does not look like one, and people could easily mistake it for the set of primary categories available on the site.)*

When sequential menus preserve state, people sometimes find themselves lost or do not realize that they can navigate in a different area of the hierarchy. For example, on Macy’s website, the menu will change to reflect the current page’s position in the IA. So a user who landed on the *Find a store* page will not see much content of interest when she opens the menu and may decide that the site is buggy or the menu is void of content.

*Macys.com: The sequential menu reflects the page the user is on. A user who has landed on the Find a store page will not find content of interest in the menu and may assume that the site is buggy or that the menu does not have anything helpful.**Mayoclinic.com: By default, the site displays the subcategories from one of its main categories (* Patient Care and Health Info *— left screenshot). In our testing, most participants were not able to find their way to the top categories (displayed on the right) and they assumed that the subcategories under* Patient Care and Health Info *were all that the site had to offer.*

When menus become overly deep, prompting users to make a sequence of selections, they amount to **nested-doll navigation** — a tedious pattern that involves repeatedly choosing categories and subcategories before reaching content. Many mobile users hate this pattern because it forces them to make multiple decisions, without seeing any useful information.

While sequential menus have only moderate interaction cost (at least when the navigation hierarchy has only 1–2 sublevels) and allow users to traverse the IA tree quite easily if they learn how to use it, they can disorient users — people may lose their understanding of where they are on the site and which categories belong to which IA level. Moreover, because the *Back* link in sequential menus can be confused with the browser's *Back* button, we generally do not recommend them for subnavigation.

## Section Menus

Section menus are separate menus (distinct from the main navigation menu) that appear on section homepages. For example, on BBC’s website, each of the main sections (e.g., *News*, *Sports* etc.) has a homepage with its own section menu. Essentially, it’s as if the section was a minisite with separate navigation.

*BBC.com: Each main-category landing page has a section menu for that category (* All Sport *for* Sport *,*Sections *for* News *).*

Section menus can accommodate a fairly large number of subcategories and are usually accessible on all pages within the corresponding section. While navigating within a section can be done easily through the section menu, this pattern does not support jumping from one subcategory of a section to another subcategory of a different section (e.g., from *Golf* under *Sport* to *Science* under *News*). Thus, it is well suited in cases when most users will spent their session in a single site section, but less appropriate if they usually navigate through multiple sections within the same visit. For those users, the interaction cost of navigating to that section’s homepage in order to get access to the section menu may be too high.

Occasionally, section menus may be confused with the main menu, and, if so, users will not use them for section navigation, thinking “I already expanded that, and I know it wasn’t relevant, so I am not bothering again.” That is why it is important to make sure that:

- The main menu and the section menu look distinct enough so people won’t confuse one with the other.
- You don’t reuse the same UI element used for main navigation as a section menu.

The BBC example above does well on both these criteria.

*Breastcancer.org: The same UI element (the* Menu *button) used for the main navigation menu on the homepage (left) is reused for the corresponding section menu on a deeper page (right). People don’t expect one button to do different things depending on where it is on the site, so they won’t realize they can click on the* Menu *button to reach subcategories of the current category.**Mayoclinic: The main menu and the section menu look distinct enough so people won’t have trouble confusing one for the other.*

## Category Landing Pages

When all else fails and you have too many subcategories to fit even in a section menu, the solution of choice is to create a landing page that serves as a [navigation hub](https://www.nngroup.com/articles/mobile-navigation-patterns/) for all the pages within that section. The landing page usually contains an enumeration of all the level-2 subcategories (and even some level 3 or 4 subcategories).

*Stanford.edu: Subnavigation is implemented through category landing pages. The* Admission *landing page contains more than 6 screenfuls of information and links to various subcategories.*

Category landing pages are even less flexible that section menus. While section menus allow users to jump across pages within the same section, category landing pages force them to pass through these pages each time the user wants to change the branch of the IA tree. That is why category landing pages are usually ok for situations where users typically visit a single area of the IA hierarchy within one session. Otherwise, the interaction cost for switching subcategories is too high, with each switch requiring a visit (and a page load) of the category landing page.

## Conclusion

Designing mobile subnavigation is often challenging due to the limited screen real estate. Here’s a simple decision algorithm to help you figure out which subnavigation pattern is best for you:

- If you have **less than 6** subcategories for all primary categories, then a submenu or accordion in the global navigation may be appropriate.
- If you have **between 6 and 15** subcategories for at least some of your primary categories, then consider a section menu.
- With **more than 15** subcategories per primary category, consider a category landing page.

Learn more about scaling navigation and subnavigation to different screen sizes in our classes on [mobile usability](https://www.nngroup.com/courses/usability-mobile-websites-apps/) and [UX for responsive design](https://www.nngroup.com/courses/scaling-responsive-design/).

## References

Harry Hochheiser, Ben Shneiderman.Performance Benefits of Simultaneous Over Sequential Menus as Task Complexity Increases *. International Journal of Human-Computer Interaction*, 2009.

Mari Carmen Puerta Melguizo, Uti Vidya, and Herre van Oostendorp. [Seeking information online: the influence of menu type, navigation path complexity and spatial ability on information gathering tasks](http://www.tandfonline.com/doi/abs/10.1080/0144929X.2011.602425). *Behaviour & Information Technology* ,2012
