---
title: "Using the Title Attribute to Help Users Predict Where They Are Going"
date: "2016-06-19"
url: "https://www.nngroup.com/articles/title-attribute/"
author: "Jakob Nielsen"
topics: [navigation]
type: article
---

One of the greatest problems on the web is that **users don't know where they are going** when they follow links. Web browsers have the ability to pop up a short explanation of a link *before* the user selects it. Such explanations can give users a **preview of where the link will lead** and improve their navigation:

- **bad links are less likely to be followed**; users will waste less time going down the garden path
- increasing users' understanding of good links helps them interpret the destination page upon arrival and **reduce****disorientation**

The link explanation is called a link title and most browsers display it in a **tooltip**. It is very easy to encode — for example, the HTML code for adding a title to the link in the following paragraph is [<a href="https://www.nngroup.com/articles/information-scent/" title="Alertbox: Information Foraging — Why Google Makes People Leave Your Site Faster">](). If you rest your cursor on the “information scent” link below, the title will pop up after about a second. Having an informative tooltip appear when the mouse hovers on a link gives users an indication of the type of information they can expect to get from following the link. Although it’s not a good practice to rely *only* on the title attribute to convey [information scent](https://www.nngroup.com/articles/information-scent/), you can take advantage of it to provide additional detail about that link. The title attribute can be applied to other HTML elements (such as images and form fields) beside links.

## In This Article:

- [Guidelines for Link Titles](#toc-guidelines-for-link-titles-1)
- [Touchscreen Devices and the Title Attribute](#toc-touchscreen-devices-and-the-title-attribute-2)

## Guidelines for Link Titles

- The goal of the link title is to **help users predict** what will happen if they follow a link.
- Appropriate information to include in a link title can be: 

  - **name of the site** the link will lead to (if different from the current site)
  - **name of the subsite** the link will lead to (if staying within the current site but moving to a different part of the site)
  - added details about the **kind of information to be found on the destination page** and how it relates to the link name and to the context of the current page
  - warnings about possible problems at the other end of the link (for example, "Subscription required" when linking to *The Wall St. Journal*)
- Link titles should be less than 80 characters, and should only **rarely go above 60 characters**. Shorter link titles are better; however super-tooltips are useful for displaying more text in the context of a large overview screen.
- **Do not add link titles to all links**: if it is *obvious* from the link name and its surrounding context where the link will lead, then a tooltip will increase clutter and ultimately reduce usability. (Even if users may not actually purposefully hover on the link, the tooltip may be displayed while the user moves the mouse.) A link title is superfluous if it simply repeats the same text that is already shown in the link label displayed on the page.
- Do not assume that the link title will look the same for all users. Indeed, screen readers will not display the text, but may read the text aloud. Different browsers will **display link titles in different ways**, as shown in the figure. And most touchscreen browsers will not display the link title at all.

*Example of a Tooltip on Edge on Microsoft Windows 10**Example of a Tooltip on Safari on Mac OS X*

Finally and most important, link titles do not eliminate the need for good information scent: **the link label and its surrounding text should be understandable** even if the link title is not displayed. Users should not have to point to a link to understand what it means: the tooltip should be reserved for *supplementary* information. Moreover, the link text should be properly *formatted* to ensure good scannability.

## Touchscreen Devices and the Title Attribute

Some [people recommend against link titles](http://www.w3.org/TR/html/dom.html#the-title-attribute) because hovering is not supported by touchscreen browsers and by keyboard-only browsers. Although a special gesture such as the [3D Touch](https://www.nngroup.com/articles/3d-touch/) could be used to display the tooltip, most touchscreen browsers do not support this feature. However, this is no reason to deny the usability benefits of link titles to those users who do use a mouse. As long as the link title is treated as an [enhancement](https://www.nngroup.com/articles/enhancement/) for mouse users and is not required for using the site, you can help some users without hurting others. Since a browser that does not display link titles will simply ignore them and will not change in any way the layout of the page, we recommend that you use this feature as a way to fully take advantage of the desktop capabilities and to optimize for this device.

*(An earlier version of this article was originally published January 11, 1998. The article was last updated and revised on June 19, 2016.)*
