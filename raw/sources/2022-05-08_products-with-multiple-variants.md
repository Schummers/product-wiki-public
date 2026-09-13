---
title: "Design Guidelines for Selling Products with Multiple Variants"
date: "2022-05-08"
url: "https://www.nngroup.com/articles/products-with-multiple-variants/"
author: "Kim Flaherty"
topics: [e-commerce, web-usability]
type: article
---

In our most recent ecommerce-research study for the [5th edition of our report series on ecommerce user experience](https://www.nngroup.com/reports/ecommerce-user-experience/), we observed that users sometimes encounter difficulties when shopping for products that are offered in multiple variants (i.e., different sizes, colors, prints, materials).

The usability problems we identified came about when ecommerce sites incorrectly represented product variants as different products and vice versa — when they represented different products as product variants. This article discusses the difference.

## In This Article:

- [Product Variations vs. Different Products](#toc-product-variations-vs-different-products-1)
- [Multiple Listings for Multiple Products](#toc-multiple-listings-for-multiple-products-2)
- [Single Listing for Product Variants](#toc-single-listing-for-product-variants-3)
- [Variations for Single Products Should Be Easily Discoverable](#toc-variations-for-single-products-should-be-easily-discoverable-4)
- [Conclusion and Design Takeaways](#toc-conclusion-and-design-takeaways-5)

## Product Variations vs. Different Products

Let’s assume that we’re looking at two different items on an ecommerce site — A and B. If the only difference between these two items is **a single product attribute** (such as color, size, pattern, material), then those two items can be considered **variations of the same product**. If, however, the product descriptions for the two items are different, then the two items are **different products**.

Our main guideline, based on our ecommerce user research, can be summarized as follows:

**Different products should have different listings**; **product variations should be displayed under a single listing**(and variations should be presented as selectable attributes on the product detail page).

When this guideline is not followed, the following usability issues emerge:

- It becomes hard for users to compare items that, in spite of being essentially different products, are presented as variations of the same product on the same product page.
- If each product variation is shown on a different product page, there is a **** proliferation of product options, which makes browsing and selecting products tedious and risks that users may not discover the combination of attributes that meet their needs.

In this article we analyze examples of both problems encountered in usability testing and explore in detail the obstacles they create.

## Multiple Listings for Multiple Products

In our research, we encountered product pages with attribute-selection [dropdowns](https://www.nngroup.com/articles/drop-down-menus/) for fundamentally different products.

For example, Best Buy’s product-detail pages for televisions included a dropdown menu for the attribute *Series*. For context, each TV series corresponds to an entirely different model of television, with different technology and features available.

![BestBuy multiple product selector](https://media.nngroup.com/media/editor/2022/04/19/bestbuy1.jpg)

*Best Buy asked users to select a TV series on the product page.*

While shopping for a new television, one study participant became confused and overwhelmed by the *Series* selection. In fact, upon changing the *Series* field, the page information (including the product title) changed, but the participant did not immediately realize it because the featured image stayed the same.

The distinction between products and variations is important. Getting it wrong causes problems for users for two reasons.

**First, with just an attribute-selection dropdown, users won’t have enough information to make an informed selection when the attribute is so complex** that it changes the product description. Choosing a TV series is a complicated decision because there are many differences from one series to the next — these are entirely different products! People don’t have an intimate understanding of a brand’s product collection, so the *Series* options in the dropdown ­(e.g., *CX* vs *NanoCell**81*) mean nothing to most users. (This confusion is amplified by the [meaningless names](https://www.nngroup.com/articles/category-names-suck/), but that’s another story.)

![Best Buy What's the Difference](https://media.nngroup.com/media/editor/2022/04/19/bestbuymodal.jpg)

*Best Buy: Under the Series selection field, there was a link reading* What’s the difference? *(top) Clicking this link brought up a modal window with a high-level comparison and a link to a full comparison chart (bottom). Unfortunately, our study participant did not discover this link.*

For such an expensive product, making a selection would have required more detail than just the labels in the dropdown menu. The user noted:

“I would have to go elsewhere, like third-party sites and on the LG site, to find the differences between these different series; like, what is a BX versus what is a CX? I can see different price points, but then I have to establish is the price point good for the features it has or which ones have features within that price point that are relevant to me?”

(In fact, BestBuy did include information to help users differentiate between different LG TV series, but our participant did not discover it.)

**Second,** most shoppers visiting a product page **have already conducted a search and filtered the listings down to products that meet shopping criteria** such as size and budget. So, they are looking at the [product-detail page](https://www.nngroup.com/articles/ecommerce-product-pages/) for a reason. It’s confusing to introduce alternative products for selection without additional context, especially since these products may no longer satisfy the users’ needs. Users must carefully evaluate the details of each of the alternatives to determine if they still meet their criteria. For example, our shopper found himself looking at a much higher-priced model than he had intended to purchase and, at this point, it was difficult for him to re-find the TV he had originally been interested in.

It’s possible that the *Series* selector was included on TV product pages to ensure that shoppers discover other related TV models; however, this goal can be addressed in other ways ****— for example, by clearly highlighting related products on the page, like other retailers selling TVs did. Other models could also be discovered by browsing product listings. The potential increase in discoverability is not worth the usability challenges created by forcing users to select a complex attribute on the product-detail page.

![Costco TVs](https://media.nngroup.com/media/editor/2022/04/19/costco.jpg)

*Costco.com: The product page for a TV was dedicated to a single series (top). Other series and sizes were displayed in the* Similar Products *panel (bottom).*

**For these reasons, attribute selectors on product pages should be reserved for product variations,** which differ from each other only in that one attribute.

On the other hand, it’s also problematic when the opposite problem occurs — that is, when products with variations are split across different product pages.

## Single Listing for Product Variants

Product variants that are represented as separate product listings result in different but equally problematic usability issues for shoppers.

This was the case on Arhaus.com. One study participant who was shopping for stools on Arhaus visited the product page for the *Robin Wishbone Counter Stool*, but she was disappointed because the page made it appear that the frame only came in the color *Stone**Vintage*, which didn’t match her décor.

![Arhaus stool product page](https://media.nngroup.com/media/editor/2022/04/19/arhaus1.jpg)

*The product page on Arhaus.com gives the perception that the stool is available in only one frame color and height.*

The truth, however, was that the same stool was offered in various types of wood frames and heights. Rather than allowing shoppers to explore and select frame colors and heights on the product-detail page, the site had multiple product pages corresponding to different frame colors and heights for the same stool. Thus, because the stool came in 3 different frame colors and 2 different heights, these options were distributed across 6 different product pages.

To add insult to injury, the product page had a design flaw: the frame color, *Stone Vintage*, was not appropriately represented as the frame material on product pages — it was shown next to a label that read *Fabric*. Moreover, next to that label, only one color swatch was listed (*Stone Vintage*), when, in fact, there were different frame colors available, but they were offered on other product pages.

![Arhaus stools listing page](https://media.nngroup.com/media/editor/2022/04/19/arhaus2.jpg)

*Arhaus had separate product pages for different frame colors and sizes. On this listing page two variations are shown interspersed with completely different stool designs, making it hard for users to recognize the different versions of the same stool.*

It’s possible that Arhaus created separate product listings for all the stool variations to ensure that all these would be equally showcased. Unfortunately, in doing so, it introduced two serious usability challenges:

1. It made it difficult to discover all product variations.
2. It increased the effort involved in saving and inspecting all product variations.

We discuss each of these below.

### Users May Not Discover All Product Variations

Although we’d like to think that site visitors lovingly browse through all product listings with dedication and care, that’s not always the case. If the same product has a unique product page for each variation, **the result is the proliferation of product options that require inspection**. Users who are interested in just a single product now have to scroll past every variation of all other products — most of which they don’t care about. This number of options to inspect can easily become overwhelming and shoppers may get sidetracked or give up before they discover something they care about.

Luckily, our shopper who was interested in the Wishbone stool returned to the product-listing page, where she later encountered a similar stool in black. She said, “Oh, is this the same stool in black? It looks like it. [She confirmed it was] I like it better in black, but now I’m wondering what other colors it comes in!”

Later, she realized that the black stool she had selected was actually bar-height. It was labeled, *Robin**Wishbone***Barstool**, which was taller than the *Robin**Wishbone***Counter Stool** she had originally discovered in the *Stone Vintage* frame. This discovery added another wrinkle in her process, because, while she continued searching the listing page for other colors of the stool, she also had to pay close attention to the height of the stool in the product name to ensure she was selecting only the right ones. The different-height stools looked the same in the [product photos](https://www.nngroup.com/articles/product-photos-listing-pages/).

Fortunately, she did end up discovering the black Wishbone stool in the correct height by diligently inspecting all product listings in the stool category. Although she could have used the search feature to look up the product name, that process would have interrupted the browse phase she was already invested in.

### Increased Interaction Cost to Save and Inspect All Variations

Online shoppers often break the process out into two phases: (1) **a browse phase,** where ****they****browse for options and save possible candidates either in a separate tab ([page parking](https://www.nngroup.com/articles/multi-tab-page-parking/)) or [in their shopping cart](https://www.nngroup.com/articles/wishlist-or-cart/) and (2) a **selection phase,** where **** they inspect and compare the saved items to make final selections before checking out.

We already discussed the additional work involved in browsing through every variation of every product. There is, however, an additional cost to the user — present during the selection process.

Many shoppers don’t realize during the browse phase that they’ve selected the same product in multiple variants. Identifying duplicates during the browse phase relies on users’ [short-term memory](https://www.nngroup.com/articles/short-term-memory-and-web-usability/), as people must remember that they have seen a similar item before.

Even those who notice that the same product is displayed multiple times on the [listing page](https://www.nngroup.com/articles/ecommerce-homepages-listing-pages/) may not be ready to settle on one version during the browse phase and may end up with even more candidate products that must be resolved during the selection phase, by comparing multiple product pages carefully. This process can quickly get extremely complex and messy.

## Variations for Single Products Should Be Easily Discoverable

**A single product page should be available for each product and all its variations**. However, to ensure that users discover other product variations, the listing page must clearly communicate their existence. If the varying attributes are aesthetic – like color and pattern —, the page should clearly show corresponding swatches below the product’s entry on listing pages. Users are accustomed to this approach and, if swatches are salient, they will know that multiple options are available, with no need to generate different product listings for each product variation.

![Burton product swatches](https://media.nngroup.com/media/editor/2022/04/19/burton.jpg)

*Burton.com included colored swatches below children’s snow gear to indicate that the product was available in multiple styles.**Then, on the product page, shoppers could explore the color variations and make this simple selection before adding the item to their cart.*

Arhaus’s listing pages did include a color swatch below the image; next to it was a *+ MORE* link that led to additional frame colors. However, the test participant who was shopping for stools missed that detail.

![Arhaus +more link](https://media.nngroup.com/media/editor/2022/04/19/arhaus3.png)

*Arhaus.com: Our test participant missed the +* MORE *link that led to versions of the stool in other frame colors.*

The *+** MORE*links was missed for a few reasons:

- The standard approach for showing color options is to show a swatch for each available color rather than an [indicator](https://www.nngroup.com/articles/indicators-validations-notifications/) that more colors exist.
- The *+ MORE* link was small and low-contrast, and, therefore, hard to spot during normal scanning.

As the user scanned the page, she only discerned a single swatch, so she did not further inspect the area.

### How to Show Multiple Attribute Variations on Listing Pages

If a product has multiple attribute variations, which was the case with Arhaus’ stools (where the stool height and the frame color were both attributes that varied), representing them on a listing page may take more thought.

**Size** is often one of the variable attributes and, in most cases, size selections do not need to be represented on the listing page. This is the case when shopping for clothing. It’s assumed that you will be able to select the size on the product page, and there is no need for the listing page to indicate that various sizes exist.

Most other websites selling stools included **a size selector in the product page**. They also allowed users to filter the result set by stool height to narrow down products that came in their desired height.

**When a product has multiple variants aside from size** (for example, upholstery color and frame color as is often the case with stools), there are a few common options for ecommerce sites to indicate the existence of these variations on the listing page:

#### Combine the Two Options Together in a Single Selection

For example white/gunmetal vs. gray/natural. A combination could be represented either as a single-color swatch or as a two-color swatch. Users should be able to click on the swatches to change the product thumbnail and discover the different kinds of variations.

![crate and barrel product listings](https://media.nngroup.com/media/editor/2022/04/19/crateandbarrel.jpg)

*Crate and Barrel used a half-and-half swatch to represent the combination of a black frame and white seat for the armchair on the right.*

Alternatively, instead of color swatches, use small thumbnails of the item to indicate the possible variations — like IKEA did in the example below.

![ikea product listing](https://media.nngroup.com/media/editor/2022/04/19/ikea.png)

*IKEA used a small thumbnail of the object to indicate various frame-seat color combinations.*

This approach works well only if the combination of variations results in a manageable number of selections like 10 or fewer. If there are a dozen or more selections, the two attributes should remain separate selections.

#### Use Product Imagery to Represent the Variety in Attributes

Rather than showing one image for a product with multiple attributes, select an image that shows several products corresponding to different variations (e.g., different seat colors and frame colors).

![Grandin Road product images](https://media.nngroup.com/media/editor/2022/04/19/grandinroad.jpg)

*Grandin Road showed multiple stools in a single image to communicate the variety of options available.*

![Pottery Barn lamps](https://media.nngroup.com/media/editor/2022/04/19/potterybarn.jpg)

*Pottery Barn’s lamp thumbnails included several product variations.*

Most sites employ more than one of these options to help customers fully understand the variety of options available for a particular product.

### Sites With Small Product Catalogs May Be the Exception

Coclico, a small luxury shoe store in New York City, also created separate product listings for different-color shoes. However, unlike Aarhus, Coclico’s product catalog was quite small and each color was shown next to the other colors of the same shoe. For these reasons, the separate product listings were less problematic.

![coclico](https://media.nngroup.com/media/editor/2022/04/19/coclico.jpg)

*Because Coclico offered relatively few products and pictured each variation next to the others, separating products across listings was less problematic.*

Even if there is a strategic reason to separate variants across listings, **product pages should still allow users to select and explore the other variations of the same product**. Don’t make shoppers keep track of the other colors or backtrack to find them.

![Coclico product page](https://media.nngroup.com/media/editor/2022/04/19/coclico2.png)

*Unfortunately, Coclico’s product page did not show the other color options for a shoe. Even though small thumbnails of other colors were displayed as related products, users expect to be able to inspect and select other variants on the product page. Showing them as related products not only risks that users will ignore them but it also forces people to go to a different page to inspect the variant.*

It would have been better if Coclico had allowed users to select different colors on the product pages for each variation, much like Article.com did for beds that came in various sizes and colors.

![Article product page](https://media.nngroup.com/media/editor/2022/04/19/article.jpg)

*Article.com: The product page for a bed allowed users to select various colors and see images of the product in that color before purchasing.*

**It is more acceptable to break product variants across pages if the site’s product catalog is very limited**. However, on sites with medium-to-large product catalogs, discovering, locating, and managing the same product across listings increases task complexity and interaction cost.

## Conclusion and Design Takeaways

Breaking product variations into separate product listings may seem like a good idea, to ensure discoverability and give the impression of a large selection. However, in real-world shopping situations, this practice creates problems for users.

- For variable attributes that are simple, such as color, size, or pattern, use a single product listing with clear attribute-selection mechanisms.
- Product-listing pages should use high-contrast, salient variation indicators below products with multiple variations.
- Products with complex variations that fundamentally change the product description and features should be split into separate product listings to support research and comparison.
- Sites with a limited selection of products might consider separate listings for each variation; however, attribute selectors should still exist on product pages.
