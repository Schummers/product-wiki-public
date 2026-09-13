---
title: "Mobile Websites: Mobile-Dedicated, Responsive, Adaptive, or Desktop Site?"
date: "2016-02-14"
url: "https://www.nngroup.com/articles/mobile-vs-responsive/"
author: "Raluca Budiu"
topics: [mobile-and-tablet-design]
type: article
---

On the web, not all websites are created equal. On a mobile device, users can encounter one of the following types of sites:

- **Mobile**-**dedicated****sites** are designed for mobile phones.
- **Web apps** are a special type of mobile-dedicated site that looks and feels like an app.
- **Responsive-design sites** are sites designed for a multitude of devices with different screen sizes; they automatically adjust the layout of their content to the available screen size.
- **Full** (or **desktop)****sites** are designed for the desktop and are not mobile optimized.

## In This Article:

- [Mobile-Dedicated Sites](#toc-mobile-dedicated-sites-1)
- [Web Apps](#toc-web-apps-2)
- [Responsive Design](#toc-responsive-design-3)
- [Adaptive Design](#toc-adaptive-design-4)
- [Full Sites on Mobile?](#toc-full-sites-on-mobile-5)
- [Conclusion](#toc-conclusion-6)

## Mobile-Dedicated Sites

Mobile-dedicated sites are sites designed specifically for mobile phones. They often live under a separate URL (e.g., m.site.com) and are completely distinct from the full site. They contain features or content that have been deemed appropriate for mobile; frequently, these are just a subset of what is available on the desktop. They are often contrasted with responsive sites, which typically contain the same content and functionality for mobile and desktop, but rearrange these features on mobile.

## Web Apps

**Web apps** are not real applications; they are really **websites** that may *look and feel* like native applications, but are not *implemented* as such. (Our article on different types of apps details the [distinctions between web apps and native or hybrid apps](https://www.nngroup.com/articles/mobile-native-apps/).)

## Responsive Design

[Responsive design](https://www.nngroup.com/articles/responsive-web-design-definition/) is a development technique that detects the client type and dynamically adjusts the layout of a site according to the size of the screen on which it is displayed. Thus, the same content may be displayed in a three-column format on a desktop, two-column format on a tablet, and one-column format on a smartphone.

*Transport for London (tfl.gov.uk) is a responsive site. On the desktop the content was formatted across 3 columns.**The tablet (left) and mobile (right) versions of tfl.gov.uk showed the desktop content in two columns and one column respectively.*

One of the complaints against mobile-dedicated sites is that they often exclude content and functionality that may prove relevant at least to some users occasionally. Responsive design tackles that objection by striving for content and feature parity across different versions of a site.

In practice responsive design is often a continuum: many responsive sites are not “fully” responsive and do not have a 100% feature or content parity; instead, they do remove functionality that is rarely needed on mobile.

*Authenticjobs.com’s responsive site: the desktop version included the ability to post a new job opening, which was missing from the mobile version.**Authenticjobs.com’s mobile version: although the site was responsive, the mobile version did not include all the features available on the desktop.*

### Mobile-Dedicated vs. Responsive Sites

Here are some of the relative advantages and disadvantages of these two approaches.

- **Responsive sites can support a variety of devices and screen sizes with a single implementation.** Dedicated sites are device specific: companies must build separate sites for mobile and for desktop. In contrast, the same responsive site can work well on a range of devices and screen sizes, from smartphones to tablets to desktops.
- **Responsive sites offer content and feature parity (at least to some extent).** Unlike for mobile-dedicated sites, at least in theory, the same content and functionality is available on all versions of a responsive site. (We saw that in practice, some responsive sites do leave out content and functionality on mobile, but to a lesser extent than mobile-dedicated sites.) No more need to decide which features are important on mobile and which should be left out. Though you still need to prioritize features and decide on their placement on smaller screens.
- **Responsive sites used to be easier to find with a search engine.** Mobile sites have a different URL than desktop sites, and originally they did not always inherit a high search rank from their sister desktop site. As a result, mobile sites may have appeared lower on search-engine page results. And even if desktop sites detected mobile clients and redirected the users to the corresponding mobile site, the redirect could take extra time and impair the mobile user experience (plus, it could also affect SEO). Since a single URL corresponds to all versions of a responsive site, responsive sites did not have to worry about SEO or redirects. Nowadays, however, modern search engines have learned to deal with mobile-dedicated sites, and they do send users to the mobile version of the site if one is available.
- **Responsive sites save content and feature maintenance.** A single site and a single content repository are easier to maintain than several separate sites. However, any interface change must be tested across all devices.
- **Responsive sites tend to be more expensive to develop.** Our clients report that the process of building an entire responsive site from scratch can be more costly than just creating a separate mobile site. Also, the development skills required tend to be more advanced for responsive sites.
- **Responsive sites tend to be slower.** Although there are techniques for improving the performance of responsive sites, because the same content is delivered to all types of devices, loading a responsive page can take longer than loading a mobile-dedicated page.
- **Responsive sites work less well for complex tasks and content.** Complex tasks are hard to accommodate on all devices equally well. Complex spreadsheets, comparison tables, and visualizations are often difficult to rescale well on small mobile screens. Mobile-dedicated sites may often decide to leave out such content, especially since users tend to avoid doing complicated tasks on smartphones.
- **Responsive sites do not integrate well with existing third party services.** If you’re building a site that relies on a separate independent backend service (e.g., booking engine on a hotel site), it’s often hard to integrate the interface for that service into a responsive site.

A final downside to responsive sites is that some companies may think that this implementation technique frees them from considering the usability of both their mobile design and their desktop design. Just because an implementation allows the same code to rewrap and display on many different screen sizes doesn’t mean that the resulting user interfaces will be decent, let alone optimized for use with any given device category.

## Adaptive Design

**Adaptive design** is a version of responsive design in which the server detects the capabilities of a client device and only sends content and features that can be appropriately displayed on that device. More powerful devices receive more complex content that is enriched with CSS and JavaScript features accommodated by those devices. Less powerful devices on poor network connections are sent nimble, light versions of the page — stripped down to core functionality. This technique is sometimes called **progressive enhancement.**

The main advantage of adaptive design is that it solves the problem of [slow response times](https://www.nngroup.com/articles/website-response-times/) that often plagues responsive design.

## Full Sites on Mobile?

Users sometimes say that they’d rather go to a desktop site than to a mobile site. That’s mostly due to their prior experience with mobile-optimized content: In an attempt to make the content more digestible, some mobile-dedicated sites include only a tiny subset of the full-site offerings on their mobile site. And sometimes people may be so used to the full site that they can use this prior knowledge to figure out their way around on a small screen.

Finally, users occasionally declare that the mobile site is dumbed down: it’s too simple and impoverished. One of our participants was trying to make a reservation on a hotel’s mobile site. The first thing she said when she saw the site was that it was very barebones, and she expected a flashier website from that company (which happened to be a big casino hotel in Las Vegas). However, she was able to finish the reservation quickly. In the end, she came to appreciate the simplicity of the site and was pleasantly surprised at how easy it was for her to complete the task.

The bottom line is: [You should not listen to what users say](http://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/), but rather look at what they do. When people *use* mobile-optimized sites on their mobile devices, they typically are more efficient and more successful. But when you ask them whether they *prefer* mobile sites, they might tell you otherwise.

#### A Note on Phablets

In our studies involving phablets, that is phones with screens larger than 5.3 in, the larger screen did enable participants to read better, and also allowed some of them to use desktop site more often and slightly more successfully on mobile. Whereas some of our phablet participants consistently preferred desktop sites, the usability of these sites on the (still small) screen is far from good, and people struggled with small targets as well as with the tiny font.

Overall, while on large-size tablets (iPad like), [full sites work decently](https://www.nngroup.com/articles/ipad-usability-first-findings/) and a small number of minor adjustments can make them quite usable, on phablets they remain very much a strain. For this reason, we don’t recommend that you send your phablet users to your desktop site.

## Conclusion

Mobile-dedicated, responsive, or adaptive are all possible ways to implement mobile user experiences. (Delivering the desktop site on mobile is a possibility, too, but not one that we recommend.) Each of them has advantages and disadvantages, and [they even influence each other](https://www.nngroup.com/articles/mobile-usability-update/). For users there is no distinction among them. Normal people do not recognize responsive or adaptive sites as being different than mobile sites, and they don’t treat them differently. (The only way you can tell as an end user that a site is implemented in responsive design is by resizing the window in which it is displayed on the desktop, to check if the content reflows. And that’s not something users would do unless they’re participating in our seminar on [Scaling User Interfaces](https://www.nngroup.com/courses/scaling-responsive-design/).)

Although their implementations may be poles apart, responsive, adaptive, or mobile-dedicated sites need to follow the same [mobile-usability principles](https://www.nngroup.com/articles/mobile-ux/) and guidelines in order to be usable.
