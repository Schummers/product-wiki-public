---
title: "Cookie Permissions 101"
date: "2023-11-10"
url: "https://www.nngroup.com/articles/cookie-permissions/"
author: "Samhita Tankala"
topics: [analytics-and-metrics, design-patterns]
type: article
---

With the increase in regulation around [data protection](https://www.nngroup.com/articles/privacy-and-security/), companies must give users more control over data privacy by providing options for cookie permissions. The question becomes how to effectively give users clear and simple choices without confusing or frustrating them. To answer this question, we conducted a study to observe how users interact with a variety of cookie-permission designs.

## In This Article:

- [What Are Cookies?](#toc-what-are-cookies-1)
- [Our Research](#toc-our-research-2)
- [Cookie-Permission: Common User Behaviors](#toc-cookie-permission-common-user-behaviors-3)
- [Design Guidelines for Cookie-Permission Requests](#toc-design-guidelines-for-cookie-permission-requests-4)
- [Conclusion](#toc-conclusion-5)
- [References](#toc-references-6)

## What Are Cookies?

Cookies are small data files that are sent and stored in an individual’s browser by a website. They record data about user preferences, browsing history, and other interactions. Cookies are often used to identify users over time. Here are some of the common reasons why companies use cookies:

- Create [personalized experiences](https://www.nngroup.com/articles/customization-personalization/) by tracking behaviors and preferences.
- Gather [analytics](https://www.nngroup.com/articles/analytics-user-experience/) metrics such as pages visited, time spent on each page, and how frequently users return.
- Save login credentials or shopping-cart items.
- Generate relevant marketing content and advertisements.
- Facilitate integrations with third-party services the websites might use.
- Track user behaviors across the web to create a profile based on demographics, behaviors, and interests.

### What Are Cookies Permissions?

Legislation such as GDPR, CCPA, and VCDPA grants users the right to control how data is collected about them by websites. As a result, websites must [obtain users’ consent](https://www.nngroup.com/articles/informed-consent/) before they store, retrieve, or use data stored on individual devices. Cookie permissions involve the process of obtaining that consent.

Cookie permissions are a requirement if your company has users in areas where cookie regulations apply. These laws give users the right to choose whether to allow cookies from different categories such as analytics, marketing, and third-party separately.

In addition, GDPR also demands that users actively opt into these cookies, rather than opt-out. What that means is that cookies other than *strictly necessary* ones cannot be used until the user actively selects them. If the user ignores the cookie-permission request, then that action counts as opting out and only strictly necessary cookies can be used.

*(You should always check with your company’s legal team to determine how to comply with the laws that govern your users.)*

### What Do Cookie Permissions Mean for Your Business?

Although cookies may provide benefits to users, there is a significant level of skepticism among many users regarding the data collected and how it is used. Many users feel uneasy about being tracked by websites through cookies, and the unclear options provided do not alleviate their concerns.

And can you blame them? Often cookie-permission designs don’t respect users’ choices. They can be confusing, difficult to use, or might rely on manipulative tactics to encourage users to opt in for cookies. These practices do not help build trust. Companies must find a balance between collecting data for personalized user experiences and upholding ethical practices. Merely having a cookie-permission box is insufficient.

### How Are Cookie Permissions Displayed?

Cookie permissions can be presented in two primary formats:

- **cookie-permission boxes**: large [overlays](https://www.nngroup.com/articles/overuse-of-overlays/) that appear in the center or bottom of a page.
- **banners:** horizontal-bar overlays typically placed at the top or bottom of a page and are presented in the form of a horizontal bar.

Some websites give users the ability to accept different types of cookies. Others may not provide users with options at all and, instead, inform users that the site uses cookies. Local laws will dictate how granular the cookie-permission request needs to be.

*Iamsterdam.com: A cookie-permission box provides users with three options:  allow all cookies, customize cookies, and deny**cookies.**Marks & Spencer: The cookie–permission banner doesn’t provide users options to opt in or opt out of various cookies. Instead, the (UK-based) company displays a link to its policy.*

## Our Research

To understand the user experience of cookie-permission UIs, we conducted a qualitative usability study on mobile and desktop. The study involved 10 participants from all over the world. We explored a range of cookie-permission designs from live websites. Some of these were powered cookie-permission vendors, which are third-party services that allow companies to customize templates that comply with different regulations like GDPR.

## Cookie-Permission: Common User Behaviors

We learned in our study that users’ willingness to share data and how they interact with cookie permission box options varied pretty drastically. These behaviors sometimes would vary depending on the situation. For example, some users said that they select the *Accept all* option**only when they are in a rush, but in other situations, they look through options in more detail. Here are common user types that we discovered during the study:

- **The denier** adjusts cookies every time because they want to share as little data as possible and ideally deny all cookie permissions.
- **The skeptic** is willing to share data **only** for sites that they are familiar with or that seem trustworthy.
- **The****tech-savvy** selects *Accept all* but clears cookies at a later time.
- **The impatient** selects *Accept all* because they want to get the cookie overlay off their screen.
- **The enthusiast** is open to sharing their data and wants to have personalized ads.

*Users divide into different categories depending on their willingness to accept cookie permissions.*

Understanding the range of how users interact with cookie permissions gives you an idea of whom your design might alienate. For example, only one *Accept**all* option might alienate users who are less willing to share their data.

## Design Guidelines for Cookie-Permission Requests

Our study participants found cookie-permission designs annoying regardless of how willing they were to share their data. The degree of annoyance varied depending on the size, placement, options presented, and other UI elements of the cookie-permission design.

The following guidelines are based on research insights that emerged from the study. There are five main design considerations in cookie-permission requests:

- Cookie-permission options
- [UI](https://www.nngroup.com/videos/ux-vs-ui/) design elements
- Scannability of cookie descriptions
- Placement of the cookie overlay
- Size of the cookie overlay

### Cookie-Permission Options

**1. Provide users with clearly marked, low-granularity**[options](https://www.nngroup.com/articles/explicit-differences/)**for cookie selection, including:****Accept all, Deny all/Select strictly necessary only, and Manage settings.**

Cookie-permission options give users autonomy over their data. Companies need to understand that not providing options for users who care about their data privacy can be just as risky as having users opt out of cookies. By not including options, sites lose their users’ trust. As a result, they may leave the site or clear cookies right after using it.

Website cookie permissions are becoming common, and users notice when options are not provided. During the study, a participant encountered a cookie-permission box with only an *Accept**all* option. He said:

*I am kind of used to opt out options. It doesn't seem to give the option to reject it or to tailor the cookies and the provisions to me, which […]  makes me feel a bit uneasy.*

*Raidboxes.com: The cookie permissions were not granular enough.*

By not including multiple options, you may alienate users who care about what happens to their data.

**2. Make cookie options immediately available rather than forcing users to click into extra pages for additional options.**

On the Harper’s Bazaar website, you can’t deny cookies until you select *Learn more.* The button *Learn more* has low [information scent](https://www.nngroup.com/articles/information-scent/) and doesn’t indicate whether there will be additional options available. Users might assume that *Accept all* is their only option and *Learn more* is just an explanation of the cookies used by the site.

*HarpersBazaar.com: Lower-granularity cookie-permission were hidden under the nondescript label* Learn more *.*

Users prefer that options like *Accept**all*, *Manage**settings,* and *Deny* or *Strictly**necessary**only* are immediately available rather than hidden on secondary pages. This design builds trust and shows that the site does not try to force them to *Accept all.* It also supports quick access to the site content.

Having cookie options immediately available is particularly helpful on mobile devices, where screen space is limited, and it saves users from having to scroll or click around extensively.

### UI Design Elements

**3. Do not use deceptive UI patterns that trick users into opting into cookies.**

Some companies use UI designs that trick users into accepting all cookies.

Here are some deceptive UI elements that you should avoid:

- [Toggle switches](https://www.nngroup.com/articles/toggle-switch-guidelines/) with an unclear label such as *Do**not**sell**my**information*, which force people to handle double negatives
- [High-contrast](https://www.nngroup.com/articles/text-over-images/)*Accept**all* buttons that aim to capture people’s attention
- An *X* or *Close* button, which can have an unclear meaning: *Accept all* or *Deny**all/Accept only strictly necessary*

Many users can see through these deceptive tactics. One user came across a high-contrast button and said:

> *It’s obviously very leading because the Accept is darkened out. Like it kind of leads you to just click on that one, which for me is fine, but for other people, it may not be.*

For these reasons, we recommend that you stay away from these problematic design patterns. If you decide to include a *Close* button in your cookie-permissions overlay, make sure that it amounts to *Accept only strictly necessary.*

*Skillshare: The toggle labeled* Do not sell my personal information *caused confusion for many users, who weren’t sure whether it should be on or off. (The site updated its design since our test.)*

### Scannability of Cookie Descriptions

**4. Use**[plain language](https://www.nngroup.com/articles/plain-language-experts/)**.**

Sometimes websites use cookie options that are vague or too similar with each other. Users should be able to quickly scan the different options and decide which one is right for them.

*Cricut provides two options, starting with the word Accept. There isn’t a clear distinction between the two options, and the use of the same word gives the impression that users don’t have a choice.*

*Fenwick & West clearly distinguishes the different options and supports quick decision making. The option I consent to cookies empowers users to have control over their data.*

**5. Use**[bullet points](https://www.nngroup.com/articles/presenting-bulleted-lists/)**to describe each cookie.**

There are users who go through cookie settings every time to decide which to allow. Many *Manage**Settings* pages provide long descriptions of each cookie. Bullet points with short descriptions make information scannable.****

*Wellcome.ac.uk provides brief bullet points to describe the different cookie types on its website.*

### Placement And Size

**6. Minimize the size of cookie overlays to avoid obscuring page content.**

Our study participants preferred small cookie-permission overlays that didn’t block access to the page content. Sites with big cookie overlays were viewed as intrusive and annoying. Some users wanted to know more about the site before deciding whether to accept cookies.

One study participant explained:

> *The simpler the better. I don’t want [the cookie-permissions overlay] to be intrusive. I don’t want it to cover my page. I definitely don’t want it to cover the page when I can’t even see what the page is, [I want] to decide before I have to accept.*

A different participant who was on a website with a large cookie banner at the bottom of the screen said, *I don’t like it when I can’t see [the website]. I don’t know that I want to accept their cookies before I know what the site is*.

However, this same participant was okay with the UK government’s large cookie-permission banner, which was placed at the top of the page. He said, *It’s big but it’s not actually covering up the rest of the site. It just kind of pushes the site down so I can still see what the site is and make a decision.*

*The UK government website uses a large cookie banner but places it at the top of the page. This placement gave one study participant the illusion that it was covering up less content.*

DHL took an alternate approach and used [a modal](https://www.nngroup.com/articles/modal-nonmodal-dialog/) cookie banner that allowed users to scroll the landing page but prevented them from clicking on anything before making a decision about cookies.

*DHL uses a modal cookie banner that enables users to scroll the landing page only. Once users make a decision about cookies, they are able to navigate to other parts of the site.*

Some companies place the cookie-permission overlay in the middle of the screen or make it large and salient because they want to ensure that users make an informed decision. Other companies, who use a third-party cookie service, may not have a say in the placement or size of the cookie overlay.

Whatever the reason, if your content overlay is big and intrusive, give users clear and multiple options immediately to allow them to decide which permissions they will grant and then move on to the site. A large cookie permission overlay is more frustrating when the cookie-permission options are unclear.

**7. Do not include multiple competing overlays that show up immediately when a user lands on your site.**

When multiple overlays (such as cookie permissions, [newsletter](https://www.nngroup.com/articles/email-newsletters-inbox-congestion/) signups, coupons, or chat features) compete for attention, [the experience quickly deteriorates](https://www.nngroup.com/articles/overlay-overload/).

*The**Ordinary.com: One study participant said it* feels like a lot *as three different popups ‘welcomed’ him on this page. Another person thought that the newsletter signup (right) was a cookie box and said that having it there was* cheeky.

Users are getting more accustomed to cookie-permission overlays and expect to see them despite finding them annoying. But when sites add several popups or other disruptive elements, they run the risk of annoying users or even turning them away. Consider alternative locations (e.g., footer for newsletter signups) or wait to show certain overlays until after the user has accepted cookies.

## Conclusion

Cookie-permission overlays shouldn’t be only a compliance requirement. They are an opportunity to build trust and foster a positive website experience for users. Ultimately, what we aim to do is respect users’ privacy while finding ways to enhance their experience on your website. These design guidelines will help you develop long-term relationships with your users and improve brand loyalty.

## References

Anon. 2019. Cookies, the GDPR, and the ePrivacy directive. (May 2019). Retrieved August 31, 2023 from [https://gdpr.eu/cookies/](https://gdpr.eu/cookies/)

Lorenzo Porcelli, Massimo Ficco, and Francesco Palmieri. 2023. Mitigating user exposure to dark patterns in cookie banners through Automated Consent. *Computational Science and Its Applications – ICCSA 2023 Workshops* 14105 (2023), 145–159. DOI:http://dx.doi.org/10.1007/978-3-031-37108-0_10
