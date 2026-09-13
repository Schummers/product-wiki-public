---
title: "Adding an Item to a Shopping Cart: Provide Clear, Persistent Feedback"
date: "2018-06-17"
url: "https://www.nngroup.com/articles/cart-feedback/"
author: "Page Laubheimer"
topics: [e-commerce, interaction-design]
type: article
---

On ecommerce sites, the first step of purchasing a product is adding it to the shopping cart. Clear [feedback](https://www.nngroup.com/articles/indicators-validations-notifications/) that this step was completed successfully gives users a sense of control and allows them to confidently continue shopping or proceed with their checkout. (It also complies with two of the [10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) — [visibility of system status](https://www.nngroup.com/articles/visibility-system-status/) and error prevention, as it reassures people that they have not [slipped](https://www.nngroup.com/articles/slips/) and added the wrong item.)

However, our usability testing of ecommerce sites shows that many sites do a poor job of confirming when a product has been added to a cart. Specifically, these two issues often arise:

- It is not clear whether the site processed the add-to-cart action.
- If the action was processed, there is no indication of whether the *correct* product (including specific options such as size, color, or quantity) was added to the cart.

When these problems are encountered, users often feel compelled to double check and make sure that the add-to-cart action was completed successfully. This behavior suggests that they have had poor prior experiences with adding products to carts.

This is a relatively old usability problem for ecommerce websites — we reported on it in in a previous round of ecommerce user research, and we warned publicly about this design flaw as one of the top-3 [bad new ecommerce design trends in 2014](https://www.nngroup.com/articles/e-commerce-usability/). I guess we warned in vain, because the same problem has become *worse* now, as proven by the new round of ecommerce testing that we have just completed.

## In This Article:

- [Badges on the Cart Icon](#toc-badges-on-the-cart-icon-1)
- [Confirmation for Adding an Item to Cart](#toc-confirmation-for-adding-an-item-to-cart-2)
- [Changes to the Add to Cart Button](#toc-changes-to-the-add-to-cart-button-3)
- [Conclusion](#toc-conclusion-4)

## Badges on the Cart Icon

A noticeable badge superimposed on the cart icon clearly indicates the number of items in the cart and can indirectly assure users that a product has been successfully added to cart. The badge will stand out clearly if its color contrasts with the cart icon.

If possible, include the cart subtotal near the icon as well. The subtotal helps in several ways:

- Users can infer to some degree if a major mistake (such as adding more than one of an item) was made.
- A change in the subtotal can attract the eye (especially if accompanied by motion or animation).
- The size of the cart is increased and represents a larger target for mouse or [fingers](https://www.nngroup.com/reports/mobile-website-and-application-usability/), leveraging [Fitts’ Law](http://www.asktog.com/columns/022DesignedToGiveFitts.html).

![Buddiboxes's mobile site shows the running subtotal in the cart icon](https://media.nngroup.com/media/editor/2018/02/16/buddhiboxes.png)

*The mobile site of Buddhiboxes.com showed a cart icon, the number of items in the cart, and the running subtotal, proving that displaying all these details is possible even on a small screen. Users were provided with useful, easily recognizable information; the larger shopping-cart target area was easy to tap without accidentally hitting other UI elements.*

## Confirmation for Adding an Item to Cart

However, just changing the cart icon to reflect the number of items in the cart isn’t enough. In addition to this numeric badge on the cart icon, use a secondary, more noticeable indicator to confirm that a product has been added to cart. Typical examples include a [subtly animated](https://www.nngroup.com/articles/animation-usability/) popover or a separate page showing which product has been added to the cart. Include an image of the product and a list of corresponding options in these confirmations. However, don’t overuse animation: small amounts of movement can draw attention, but lots of movement are both distracting and annoying.

Stay away from disappearing [overlays](https://www.nngroup.com/articles/overuse-of-overlays/) that quickly fade from view. The transient nature of these popovers prevents users from easily reviewing *what specifically* ended up in the cart — were the size and the color right? Viewing the feedback popover becomes a race against time and can create stress, as well as uncertainty about how to access this information again.

In our new round of usability testing, a participant shopping on Burberry.com added a coat to her cart, noticed the overlay showing that the product had been added to her cart, and began moving her mouse over to the overlay to doublecheck that the item was the size she wanted. However, before she could read the overlay, it disappeared. “Where did my bag go? I guess it’s really sensitive to the movement of my mouse.”

![Burberry transient overlay for add to cart](https://media.nngroup.com/media/editor/2018/02/16/burberrypopover.png)

*The overlay on Burberry.com showed that an item has been added to the shopping bag, but disappeared quickly. Participants in our study attempted to review the feedback to make sure they had added the right item to their bag, but could not do so because of the transient overlay.*

Here are the **recommended** ways to show feedback in the cart:

- An overlay or popover that **doesn’t obstruct** key information on the product page, and does not disappear on its own, or
- A banner that appears on the product page at the top of the page, or
- An new interstitial page that shows a *Product X has been added to the cart* message, with *View cart,**Checkout,* and *Continue**shopping* buttons

![Saks Fifth Avenue non modal overlay showing feedback that an item was added to cart](https://media.nngroup.com/media/editor/2018/02/16/sakspersistentpopover.png)

*Saks Fifth Avenue showed a nonmodal overlay that didn’t disappear on its own after the user added a product to the cart. While the overlay obscured some of the page content (which we don’t recommend), it still kept the main product information visible. In addition, the nonmodal nature of the overlay allows users to select links outside the overlay without dismissing it. Finally, the overlay  didn’t look like the type of newsletter-signup popups that users in our study would often dismiss without reading .*

![Boden shows a banner indicating items have been added to cart, but also includes cross-sell promotions](https://media.nngroup.com/media/editor/2018/02/16/bodenbanner.png)

*BodenUSA displayed a banner above the product to indicate that it had been added to the cart. This banner appropriately showed a product image, the options selected, and a clear link to the checkout process. However, it also included upsell promotions (* We saw these and thought of you *), which can have two downsides: (1) users could assume that the promotions are items in their cart and wonder why they were different from the actual products that they had added to cart , and (2) they could also cause banner blindness and get ignored.*

![Macy's iOS app shows a new interstitial page to confirm an item has been added to cart](https://media.nngroup.com/media/editor/2018/02/16/macysinterstitial.png)

*The Macy’s iOS app took users to a new interstitial page to show that an item had been added to the cart. This pattern is useful when users are likely to order only a few items during a session; otherwise, it can be disruptive for the users’ flow.*

Which of these variations is appropriate for your design depends on the shopping behaviors of your users. In most cases, an overlay or a banner showing that something has been successfully added to one’s cart is most useful, especially on sites where users tend to purchase or compare several items. However, on sites with a limited number of options (such as a custom-furniture store), or with users who purchase only 1–2 items in a session (for example, repeat users such as Amazon Prime shoppers who do not bother to consolidate multiple items in a single order), an interstitial page can [keep users focused on the checkout process](https://www.nngroup.com/articles/shopping-cart/), and thus expedite it.

Whichever pattern you choose for your site, show:

- A nicely sized [product image](https://www.nngroup.com/articles/shopping-cart/) that correctly reflects the color or other options selected by the user
- The name of the product
- The price of the item
- The quantity added
- Additional text listing any options selected (size, color, etc.)

## Changes to the Add to Cart Button

In our usability studies, many participants accidentally added the same item to their cart multiple times, and, then were surprised during checkout when they noticed the replication. There are many reasons why people may add an item to the cart several times:

- They may forget that they have already put the product into their cart, either because of a distraction or because their purchase was split across a longer period of time (e.g., several hours or even days).
- When engaging in comparison shopping across different similar items, people may save candidate products in their shopping cart (a form of external memory).
- As they reach the same item in multiple ways (e.g., from a [search-results page](https://www.nngroup.com/reports/ecommerce-ux-search-including-faceted-search/) and from a *Related**Products* list on a product page), they may add it to their cart each time, without realizing that they have saved it before.
- The site may provide poor feedback that the item was added to cart, and the user may press the *Add to cart* button multiple times.

How can designers remind users that an item was already added to cart? Here are some options:

- **Add a message** indicating that the item is already in the cart. This message should be visually salient and placed next to the *Add to Cart* button. Additionally, the button’s label should be changed to *Add Another* (or similar). While not every user will notice these changes, some will.
- **Gray out** the *Add to cart* button or change it to *View Cart, In Cart,* or to a checkmark to indicate that the item is in the cart. **We don’t recommend this option**, because it prevents people from adding more of the same item to the cart. To avoid that problem, many sites that adopt this solution make the label change transient and revert the button back to the standard *Add to Cart* after a few seconds. This means that some users may miss the label change and will still add the item to cart multiple times.

![Rose and Rex changed the Add to Cart button to a checkbox temporarily](https://media.nngroup.com/media/editor/2018/02/16/roseandrexcheckbox.png)

*Rose & Rex changed the* Add to Cart *button to a checkbox after an item was added to the cart;  a few seconds later, this label reverted back to a standard* Add to Cart,*which did not provide any indication that the item was already in the cart.*

![Freshdirect shows a small, easy-to-miss indicator that an item was already in the cart](https://media.nngroup.com/media/editor/2018/02/16/freshdirectalreadyincart.png)

*Freshdirect.com showed a small message below the* Add to Cart *button to indicate that there were already two of this item in the cart. While potentially helpful, such a message is easy to miss.*

## Conclusion

Give users appropriate feedback when they add an item to their cart, including all of the following:

- A badge on the cart icon
- A persistent overlay or new interstitial page showing that the item was successfully added to cart (along with details about the product)
- A changed *Add to Cart* button to showcase that the item is already in the cart (but with the ability to add more of that same item to the cart)

Learn more about making purchases easier with [800+ UX guidelines in the new edition of our Ecommerce report](https://www.nngroup.com/reports/ecommerce-user-experience/) series.
