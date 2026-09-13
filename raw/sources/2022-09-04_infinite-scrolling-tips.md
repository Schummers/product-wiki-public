---
title: "Infinite Scrolling: When to Use It, When to Avoid It"
date: "2022-09-04"
url: "https://www.nngroup.com/articles/infinite-scrolling-tips/"
author: "Tim Neusesser"
topics: [design-patterns]
type: article
---

**Infinite scrolling** is a [listing-page](https://www.nngroup.com/articles/ecommerce-homepages-listing-pages/) design approach which loads content continuously as the user scrolls down. It eliminates the need for [pagination](https://www.nngroup.com/articles/item-list-view-all/) — breaking content up into multiple pages.

![A picture of the Adidas listing page, highlighting the pagination at the bottom of the page.](https://media.nngroup.com/media/editor/2022/08/15/adidas_pagination.png)

*Adidas.com: For its listing pages, Adidas uses pagination to display its selection of products to its users.**Nike.com: In comparison to its competitor Adidas, Nike is using infinite scroll to display its products on its listing pages.*

Since its invention in 2006, infinite scrolling experienced a steep growth in popularity. Today, it is mostly used on websites and apps with a flat structure, where content streams constantly and is equally relevant to the user — for example, social-media sites (e.g., TikTok, Instagram, Twitter) but also news or ecommerce websites (e.g., Apple News, Nike.com). **What are the benefits and limitations of infinite scrolling?**

Since its invention, some variations to classic infinite scrolling (as described above) have been developed. One variant requires the user to explicitly press a *Load More* or *See More* button to see more content added to the bottom of a page. Another variant breaks down the infinite scroll into pages that serve as valuable landmarks for orientation and enable users to quickly navigate the content, as they can jump from one page to the next one.

## In This Article:

- [Benefits of Classic Infinite Scrolling](#toc-benefits-of-classic-infinite-scrolling-1)
- [Usability Issues Caused by Infinite Scrolling](#toc-usability-issues-caused-by-infinite-scrolling-2)
- [A Compromise: Infinite Scrolling with a Load More Button](#toc-a-compromise-infinite-scrolling-with-a-load-more-button-3)
- [A New Alternative: Infinite Scrolling with Integrated Pagination](#toc-a-new-alternative-infinite-scrolling-with-integrated-pagination-4)
- [Is Infinite Scrolling Right for Your Design?](#toc-is-infinite-scrolling-right-for-your-design-5)
- [References](#toc-references-6)

## Benefits of Classic Infinite Scrolling

1. **Reducing interruptions.** Arguably, the biggest advantage of infinite scrolling over pagination is that it reduces interruptions for the user. A study published in the Information Systems Journal found that even short interruptions (such as clicking a *Next* button to go to another page for more content) can trigger users on a social ecommerce platform to change their task. While the effect of interruptions may vary depending on the type of user activity (e.g., it may be less drastic if users search for a specific item or piece of information), minimizing interruptions is important for social-media, entertainment, and news sites because it **helps to create a seamless experience and encourages users to stay engaged.**
2. **Lowering interaction cost**. If the page loads new items continuously and quickly, without users having to press a button and wait for a new page to load, the interaction cost is diminished. Moreover, if the users want to navigate back to items that they have seen already, they do not have to press the *Back* button and wait for a previous page to load — they can simply scroll up.
3. **Well-suited for mobile devices.** The increased popularity of infinite scroll was related to the steep rise of mobile devices. Because mobile viewports are small, users are already engaging in extensive scrolling ([if they have something to scroll for](https://www.nngroup.com/videos/scrolling-information-foraging/)), keeping their finger close to the screen and ready to swipe down.

## Usability Issues Caused by Infinite Scrolling

Despite the benefits discussed above, infinite scrolling does have several drawbacks, which can impair the user experience:

- Difficulty refinding content
- Illusion of completeness
- Inability to access the end of the page
- Accessibility problems
- Increased page load
- Poor SEO performance

### Difficulty Refinding Content

Infinite scrolling results in a lack of landmarks to help users orient themselves. With pagination, users may remember the page that an item was on and that an item was close to the top of the page or towards the middle, but **in an infinite list of items, it is hard to remember the location of any specific item and return to it.**

This is especially disruptive for the user experience when websites **do not save the user’s spot in the list during**[pogo sticking](https://www.nngroup.com/articles/pogo-sticking/). Frequently, users will click on an item in the infinite list or feed to go to its detail page and, when they come back, using the *Back* button, they will find themselves at the top of the list, having to scroll down through screenfuls and screenfuls of already seen content. In contrast, with pagination, users are returned to a single page of content. Even if they’re taken back to the top of the page, that reduced set of items is more manageable than on a page with infinite scrolling.

*bmwusa.com*:*The position within the product list was not saved when the user selected an item and then returned to the product list via the* Back *button. Instead, the* Back *button took the user to the top of the page and gave them the cumbersome task of finding their old position within the product list.*

### Illusion of Completeness

On some pages that use infinite scrolling without a *Load More* button, there can be an [illusion of completeness](https://www.nngroup.com/articles/illusion-of-completeness/) : the user may assume that the end of the content stream has been reached as new content loads in the background, below the fold. Usually, this problem arises **when there is no indication that additional content is loading** as users reach the end of their preloaded content.

![Screenshot of the Miami FC website, showing the illusion of completeness effect where users falsely assume that they reached the end of the page](https://media.nngroup.com/media/editor/2022/08/15/screenshot_illusion-of-completeness_miamifccom.png)

*Miamifc.com:**The big whitespace at the bottom of the page, in combination with an ad, created an illusion of completeness. Users could think that they reached the end of the page, while in fact there was more content loading below the fold*.

### Inability to Access the Footer

**Infinite scrolling (without a Load More button) can make it impossible to access the footer of a website**. The constant stream of content prevents users from reaching useful information usually hosted in the footer (e.g., contact information, return policies).

*Nike.com: The constant stream of new items didn’t allow the user to access the footer section.*

### Accessibility Problems

Infinite scrolling can cause additional problems for users with [accessibility needs](https://www.nngroup.com/articles/inclusive-design/). For keyboard-only users, infinite scrolling complicates navigating the web, due to the vast amount of content that can be placed on one page because such users have to “tab” through content link by link and therefore face a lengthy task if they want to navigate to the end of an infinite scroll. On the other hand, screen-reader users will only see the first “chunk” of the list, without being able to trigger the loading of new content.

However, in recent years there have been positive developments in supporting infinite scrolling for users with accessibility needs. For example, the [ARIA “feed](https://udn.realityripple.com/docs/Web/Accessibility/ARIA/Roles/Feed_Role)” role, introduced by the [World Wide Web Consortium (W3C)](https://www.w3.org/WAI/), allows screen readers to scroll through a feed of infinitely scrolling content. This role also enables keyboard users to move past the infinite feed to the first focusable element following it.

### Increased Page Load

Sites with infinite scrolling often tend to take longer to load due to the infinite flood of new content. If sites try to do the right thing and keep track of users’ location on the page as users engage in pogo sticking (see above), then there could be a ton of content to be loaded whenever the user returns to a list.

**The slow speed tends to be a problem for mobile users**(due to the variable connectivity) **or to any user in an area with low bandwidth or on limited data plans.**

Some companies, like Facebook, attempt to overcome these page-load issues by launching “lite” versions of their products (e.g., Facebook lite and Instagram lite) that require less data to function. While this is a great approach to make products available to a wider range of users, it might not be feasible for smaller companies to develop an additional lite version of their product.

### Poor SEO Performance

Last but not least,**infinite scrolling can negatively impact the SEO performance of your website.** This is because search engine crawlers cannot always access all the content that is hidden below the first section of your page and page speed (an important SEO factor) can be slowed down by infinite scrolling.

## A Compromise: Infinite Scrolling with a Load More Button

To avoid some of the drawbacks of infinite scrolling without returning to traditional pagination, many sites and apps implement a variation on the infinite-scrolling approach — **infinite scrolling with a Load More button**. *Load More* buttons have gained popularity recently, particularly in mobile sites and apps. This approach is not only used on ecommerce websites, but also on Google’s mobile search-result pages.

![A screenshot of Asos' website, showing their infinite scrolling with a load more button approach](https://media.nngroup.com/media/editor/2022/08/15/load-more-button_asoscom.png)

*Asos.com: A Load More button gave users the option to load additional items. This approach is beneficial for users in low bandwidth areas and gives all users easy access to the footer of the page. The indication of how many products were already viewed, as well as the total number of products help users to navigate the page and is a great example of how to enhance the user experience.*

**Adding a Load More button reduces some of the usability issues created by classic infinite scrolling.** The main issues that a *Load More* button can resolve or decrease are:

- **Access to the footer.** The *Load More* button stops the constant flow of new content and thereby enables users to access the footer section of a website.
- **Illusion of completeness.** A *Load More* button placed prominently at the bottom of a page is a clear indication that there is more content to discover, and that the user did not yet see all the content.
- **Low bandwidth and limited data plans.***Load More* buttons offer a way to load less content upfront. That helps users with low bandwidth or limited data plans. This approach is especially helpful when users have control over the amount of content that is loaded each time.

One disadvantage of *Load More* buttons, compared to classic infinite scrolling, is that interaction cost increases — users have to click the *Load More* button to load more content. Even the small interruption of clicking *Load More* might make users consume less content and cause them to switch tasks.

## A New Alternative: Infinite Scrolling with Integrated Pagination

A new variant of classic infinite scrolling is infinite scrolling with integrated pagination. With this variant, as the user reaches the end of the first loaded content segment, a set of page indicators is displayed and then a new chunk of content is automatically loaded.

*Google.com*: *The mobile* Shopping *page used infinite scrolling with integrated pagination. The page numbers act as landmarks that can improve refindability and navigation.*

This approach **has the potential to reduce some of the usability issues created by classic infinite scrolling —** in particular:

- **Refinding content.** The page indicators are valuable landmarks that can help users navigate the page and refind content more easily, as they might remember which page a certain item was on.
- **Improved navigation.** Users can utilize the integrated pagination to jump back and forth in between pages and thereby efficiently skip irrelevant content.

Even though integrated pagination might solve some of the usability issues caused by infinite scrolling, it can’t solve all of them. In particular, the inability to access the end of the page and an increased page load remain problems that make this design decision not feasible for websites that place relevant information in the footer section or websites that need to avoid long load times.

Moreover, this design pattern is so new that we don’t have user-testing data. Even though integrated pagination has the potential to improve classic infinite scrolling, it **could be that, at least for a while, it confuses more than helps users because of its low familiarity.**

## Is Infinite Scrolling Right for Your Design?

Because of the usability issues that infinite scrolling can cause, we do not recommend it when users will want to use the listing page’s content to:

- Find something specific (e.g., looking for a specific article or item)
- Compare items in a long list (e.g., choose between several products that might be very far apart in the list)
- Inspect only a few items at the top of the list (e.g., pick the best search results)

Infinite scrolling is also not a good fit if you have a large user group from areas with low bandwidth or if your website is visited frequently by users with accessibility needs.

**There is no solution (infinite scroll, pagination, Load More , or integrated pagination) that is overall superior and the perfect fit for every website.** It always depends on the specific circumstances of your website and the goals that your users want to accomplish. To assess what is the best solution for your website consider the advantages and limitations of each of the four options. You should ask yourself questions like:

- Who are your users?
- What are your users’ goals when they visit your site?
- Which devices do your users primarily use to access your website?
- Are there other limiting factors (e.g., a large user group with low bandwidth or many users with accessibility needs)?

Infinite scrolling typically **works best for situations where users will want to scroll through homogeneous items with no particular task or goal in mind**— for example, entertainment, news, or social media.

To explore new design trends and decide whether they’re right for your designs, check out our full-day course [Emerging Patterns in Web Design.](https://www.nngroup.com/courses/emerging-patterns-web-design/)

## References

Kim, J. et al. 2016. Pagination versus Scrolling in Mobile Web Search. *Proceedings of the 25th ACM International on Conference on Information and Knowledge Management.*(2016).

Sharma, S. and Murano, P. 2020. *A usability evaluation of Web user interface scrolling types. First Monday.* 25, 3 (2020).

Zhang, Y. et al. 2019. *How do interruptions affect user contributions on social commerce? Information Systems Journal.* 30, 3 (2019), 535-565.
