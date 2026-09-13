---
title: "The Mobile Checkout Experience"
date: "2018-12-02"
url: "https://www.nngroup.com/articles/mobile-checkout-ux/"
author: "Anna Kaley"
topics: [e-commerce, mobile-and-tablet-design]
type: article
---

In ecommerce design, the checkout path is one of the most highly scrutinized parts of the user journey. And rightfully so: it directly influences brand perception, propensity for return visits, and an organization’s ability to drive revenue online. With more and more users [shopping on smartphones](https://www.nngroup.com/articles/m-commerce-terrible-ux/), it’s imperative to design a mobile checkout flow that not only follows the best practices for ecommerce user experience, but is also optimized for the capabilities and constraints of mobile devices.

In this article, we’ll use findings from our recent research for the fourth edition of the [Ecommerce User Experience report series](https://www.nngroup.com/reports/ecommerce-user-experience/) to outline and discuss some of the most important design guidelines for an optimal mobile-checkout experience.

## In This Article:

- [Mobile Shopping Cart and Checkout Options](#toc-mobile-shopping-cart-and-checkout-options-1)
- [Order Summary and Pickup Options](#toc-order-summary-and-pickup-options-2)
- [Form Fields and Input Interactions](#toc-form-fields-and-input-interactions-3)
- [Easy Payment on Mobile](#toc-easy-payment-on-mobile-4)
- [Conclusion](#toc-conclusion-5)

## Mobile Shopping Cart and Checkout Options

Often, the checkout process begins with revisiting the [shopping cart](https://www.nngroup.com/articles/shopping-cart/) and editing it to contain only the items that will be purchased in the current session. The following guidelines ensure that the early stages of the mobile checkout are pain-free for users:

- **Provide quick access to the mobile shopping cart.** Tapping on the shopping cart indicates a desire to move forward, so get users to the cart as quickly as possible. Avoid performance-related delays and remove any unnecessary obstacles that may get in users’ way when trying to access the cart.

*This JCrew.com design represents a good example of easy access to the shopping cart.  When an item was added to cart, a badge on top of the cart icon gave users immediate feedback . Tapping on the cart icon took users to the shopping-cart page, without any extra clicks, popups, or added steps in their way.*

![PSSW forces users to tap an button to get to their cart](https://media.nngroup.com/media/editor/2018/10/19/pssw.jpg)

*On PSSW, tapping the cart icon revealed a mobile mini-cart. Users then had to tap* View Cart *or* Checkout *to access their full shopping cart and order details. This extra tap is unnecessary; when users tap the shopping cart icon, take them directly to their cart.*

- **Make it easy for users to update the contents of their shopping cart.** People often change their minds about purchasing a product or accidentally add an item to the shopping cart twice. Allow users to easily change the contents of their shopping cart.

- **Give users a clear Remove button next to each item in their cart.** Don’t force them to change quantities to zero in order to delete a product from their shopping cart.

While shopping on HP’s site, one study participant became frustrated when she couldn’t figure out how to remove an unwanted printer cartridge from her cart (she was supposed to set the quantity to zero). As a result, she purchased the printer cartridges from [Amazon](https://www.nngroup.com/articles/ecommerce-compete-amazon/) instead.

![HP forces users to change quantity to zero to remove items](https://media.nngroup.com/media/editor/2018/10/19/hp_final.png)

*HP did not include a clear* Remove *button next to each item in the cart and required users to change the quantity to zero to remove items from the cart. This design was unintuitive and caused frustration.*

- **Don’t use an Update button for committing changes to the shopping cart.** Some sites force users to tap an *Update* button for any change to their shopping cart to become effective. Thus, someone who wants to change the quantity of an item in the cart will have to indicate the new quantity and then press *Update* to commit the change.

This design is suboptimal for two reasons: (1) users must perform two actions (change the quantity, then tap the *Update* button) to change the item; (2) people often fail to tap the *Update* button — either because they forget or because they don’t realize they are supposed to do so.

![Things Remembered requires users to select update to edit quantity.](https://media.nngroup.com/media/editor/2018/10/19/thingsremembered.png)

*ThingsRemembered.com: Users had to tap the stepper and then the* Update *link to change the quantity of an item. This design is suboptimal.*

- **Support the continuity of the shopping experience across multiple devices.** As brands continue to develop across [channels](https://www.nngroup.com/videos/omnichannel-ux/), users’ expectations for easy access, flexibility, and consistency while shopping continue to rise. And, because users tend to bounce back and forth between channels while shopping, it’s important to give them reliable access to their carts, on desktop, mobile web, and in mobile apps.

Users of Apple devices can benefit from a feature called **handoff**, which allows them to (1) use a website in Safari on their iPhone and (2) then, when they move to their iPad or Mac computer, open up the same page in Safari on that device (or vice versa).

![Apple Handoff makes it easy to checkout across devices](https://media.nngroup.com/media/editor/2018/10/19/handoffexample-copy.png)

*Handoff allows Apple users to move between iPhone, iPad, and Mac devices. This feature supports a seamless shopping experience, allowing the same session to be continued across different devices. In this case, the user started shopping on a MacBook Pro computer but moved to the iPhone to checkout.*

An application can also hand off the user’s session to a different device. Thus, someone checking out using an application on an iPhone could seamlessly continue the process on the iPad, **provided that the developers of the app have taken advantage the handoff feature.** Unfortunately, many apps (Amazon being one notable example) do not use handoff — to the detriment of their users.

To support seamless cross-device transitions for users outside the Apple ecosystem or those who are not familiar with handoff, **make sure that their session can be resumed on a different device once they are logged in**. However, that is not enough: users have to be aware of this feature when they first create an account. To help users remember earlier shopping sessions on different devices, consider including labels that indicate when items were added to the cart and on which device or channel they were added.

![CrateandBarrel lets users access their cart across devices](https://media.nngroup.com/media/editor/2018/10/19/cratebarrel.png)

*CrateandBarrel.com displayed a message on the empty–shopping-cart page to let users know that they could access their shopping cart from all devices by signing in.*

- **Make guest checkout prominent and easy to find.** Even people who have an account forget passwords; in many cases, it will be easier for them to check out as guests than to recover their password on their mobile device. Make guest checkout the most salient of your checkout options by placing it above the fold and above the options to sign in or create an account.

![Pottery Barn makes it easy to checkout as a guest](https://media.nngroup.com/media/editor/2018/10/19/potterybarn.png)

*Pottery Barn did a good job of placing the guest checkout prominently in the viewport so the user doesn’t have to waste time looking around to find it. The guest checkout was prioritized over authenticated checkout and made it easy for on-the-go mobile shoppers to get through the checkout process quickly.*

## Order Summary and Pickup Options

Shoppers do not appreciate inaccuracies or unclear prices and grow frustrated when costs unexpectedly increase during the checkout process. Often when this happens, users will abandon their carts and seek out the items elsewhere to avoid excess fees, particularly when it comes to shipping and delivery charges. Two important details ensure that users can see and understand the information in the order summary on mobile:

- **Make the order summary easy to find in mobile layouts.** While the [details we display in the order summary](https://www.nngroup.com/articles/ecommerce-taxes-fees/), (including subtotal, taxes, fees, discounts, and shipping charges) are important for any checkout flow, we must pay extra attention to the placement of the order summary for mobile checkout. Due to limited screen space, these extra fees may appear low on the page and may be ignored by users. To avoid unpleasant surprises later in the flow, show the order summary prominently at the top of the checkout pages. Don’t make shoppers scroll to the bottom of the page to find this information.

![Adidas' order summary is too far down on the page](https://media.nngroup.com/media/editor/2018/10/19/adidas3.png)

*Adidas.com: The order summary was too low on the page to be easily viewed. Users had to scroll to the very bottom of the* Review & Pay *page, right above the mobile footer, to see their final order summary information. The information was also collapsed in an accordion, which made it difficult to see the price composition; instead, it should have been placed higher on the page and expanded to show each line item contributing to the order’s total.*

![Jet.com makes it easy to see your order summary](https://media.nngroup.com/media/editor/2018/10/19/jetcheckout.png)

*On Jet.com’s* Review & Pay *page, the order summary is placed prominently above the page fold. Users can clearly see each line item before placing their order, without having to scroll down.*

- **Use the user’s current location to determine sales tax, delivery costs, and any pickup options available.** Shipping costs and tax usually depend on the shipping address associated with the order, which is typically entered late in the checkout flow. Whenever possible, retailers should use their customers’ current location to estimate the delivery fees and the tax before the users have entered their shipping addresses. The current location can also serve to locate the closest physical locations where users could pick up their orders, if desired. Always ask the user for their permission to use their current location and allow them to easily change or update their location.

![Target uses the users' current location](https://media.nngroup.com/media/editor/2018/10/19/target.png)

*Target’s mobile checkout flow used location detection to offer store-pickup options as well as to estimate taxes in the order summary.*

## Form Fields and Input Interactions

[Filling in forms on mobile](https://www.nngroup.com/articles/mobile-input-checklist/) can be time-consuming and error-prone. Reducing the total number of form fields and automatically filling in fields for the user (based on the knowledge that the system has about that particular user) can dramatically ease the checkout process. Here are a few guidelines for checkout forms:

- **For each field, present the correct keyboard.** Use a numeric pad for numeric data such as credit-card numbers or phone numbers. For email-address fields, use a keyboard optimized for entering email addresses, which prominently features email-specific characters like “@” and “.”. Keyboards should also include up and down arrows to facilitate quick transitions to the next (or previous) form field.

![Nike uses the correct mobile keyboards](https://media.nngroup.com/media/editor/2018/10/19/nike2.png)

*Nike.com showed the correct keyboards for email (left) and phone-number (right) fields.*

- **Calculate fields automatically based on users’ prior inputs.** Fields such as credit-card type, address, city, or state can be automatically calculated based on other data entered by the user (the credit-card number and, respectively, the ZIP code). Instead of asking users to type this information explicitly, do the work for them. Our research showed that asking for a user’s ZIP code and then populating the city and state, while still allowing the user to correct the occasional error, worked well.

![Crutchfield uses mobile autofill in their forms.](https://media.nngroup.com/media/editor/2018/10/19/crutchfield2.png)

*Crutchfield made it easy for users to enter their address. The site prompted users to first enter their ZIP code (left) and used this information to complete the city and state in editable form fields (right). Users could change these fields in case their city name differed from what appeared in the database.*

- **Browser autofill and saved data should work on form fields such as name, address, email address, phone number, password, and credit card.** Usability-testing participants appreciated that they could use browser autofill while checking out on Tiffany’s mobile site. The form worked flawlessly with Safari’s *AutoFill Contact* feature, which delighted a user who was not looking forward to typing out her contact info. She said, “It autopopulates. Thank you, Apple. Apple autopopulated my information.” This remark sums up most users’ feelings about autofill: a poor autofill experience is blamed on the website, whereas a properly working experience is attributed to the phone manufacturer. Ensure that your site is coded to work properly with browser autofill functionality.

- **Use an open form field, not a selection list when asking users to enter their state and credit card expiration date.** Long [dropdown](https://www.nngroup.com/articles/drop-down-menus/) lists are especially difficult for mobile users, particularly those on iOS. The iOS picker control (which is used for implementing dropdowns) occupies half the screen and displays only a few items at a time. If the list is long, users have to scroll many times before getting to values at the end of the list. In our studies, users frequently struggled with selecting the correct item from these lists, making lots of errors that required repeated attempts. While it usually makes sense to reduce the amount of typing that users must do on mobile, a dropdown for a long list is the wrong solution. It’s faster for users to type the two letters that stand for their state and the 4 digits of credit-card expiration dates.

![Staples forces users to scroll through a long list of state abbreviations.](https://media.nngroup.com/media/editor/2018/10/19/staples.png)

*Users on Staples.com had to scroll through a long dropdown list to select the two letters that represent their state. It is much faster for users to type in the letters than to scroll down to select a state from the dropdown.*

![TM Lewin lets users type in their credit card expiration date and security code.](https://media.nngroup.com/media/editor/2018/10/19/tmlewin.png)

*TM Lewin correctly used a text-input field for the credit-card expiration date, rather than a cumbersome dropdown menu. It also switched the keyboard to the number pad on mobile, to make entering this information easy.*

## Easy Payment on Mobile

Entering credit-card details is labor-intensive, annoying, and, especially on mobile, error-prone; moreover, users on the go may not always have their credit card handy. Many of our study participants took advantage of easy-payment options such as PayPal or Apple Pay. Not only did these services save users from the trouble of typing in their credit-card information, but they were also perceived as more secure and trustworthy than providing their credit-card number directly to the site.

- **Offer mobile-friendly payment options, but don’t overwhelm users with too many options.** Recognizable third-party checkout options such as Paypal or Apple Pay can be helpful, but too many options can cause [choice overload](https://www.nngroup.com/videos/choice-overload-harms-users/). For each payment option offered, make the distinction between each one clear. The most common checkout process should be the most prominent on the page, or listed first among the other options. It’s also important to signal to users that they will be taken away from the site temporarily to enter their payment-service details before being brought back at the end. Use verbiage such as Checkout with Paypal, together with the standard branded buttons for those services. To minimize the information entered by the user, offer these options at the very beginning of the checkout flow; however, make sure you repeat them also on the payment page for those users who may have missed them in the beginning.

![Vineyard Vines offers mobile friendly payment methods](https://media.nngroup.com/media/editor/2018/10/19/vineyardvines2.png)

*Vineyard Vines offered many mobile-friendly payment options in the shopping cart (left) and again displays PayPal on the payment page for those who may have missed it in the cart (right).*

- **Allow users to take photos of their credit cards to populate information.** Several people in our study used the *AutoFill Credit Card* feature that’s offered in Safari, instead of typing in their credit-card information. This option enables users to take a photo of the credit card; the details are scanned and the information is then added to the website’s credit-card field.

While checking out on Tiffany’s mobile website, one user complained when she noticed that the site didn’t offer a PayPal or Apple Pay option. “I’m like, ‘ugggggh’ why is there not a PayPal or Apple Pay associated with this?” Then, she noticed that the site supported the built-in, *AutoFill Credit Card* option and, though she still had to get her credit card out of her wallet, her frustration decreased after she was able to scan her credit card to input the details.

![Tiffanys.com lets users take a photo of their credit card to pay.](https://media.nngroup.com/media/editor/2018/10/19/tiffanys2.png)

*Tiffanys.com: The* AutoFill Credit Card *feature within Safari (left) allowed users to take photos of their credit card to populate their payment information (right).*

## Conclusion

What distinguishes the best mobile checkout experiences from standard ones is the extra attention to detail. Mobile-focused, user-centered UI elements can help move your users through the experience with speed and ease. Though often overlooked and easily forgotten, these seemingly small design details in your mobile checkout will create an experience that delights your users.

For more on how to design an optimal ecommerce shopping cart, checkout and registration process, explore our report, [Vol. 04: Shopping Carts, Checkout and Registration](https://www.nngroup.com/reports/ecommerce-ux-shopping-carts-checkout-registration/), part of the recently updated fourth edition of our [Ecommerce User Experience report series.](https://www.nngroup.com/reports/ecommerce-user-experience/)
