---
title: "Challenges for Screen-Reader Users on Mobile"
date: "2023-04-30"
url: "https://www.nngroup.com/articles/screen-reader-users-on-mobile/"
author: "Tanner Kohler"
topics: [accessibility, mobile-and-tablet-design, writing-web]
type: article
---

Accessibility is a topic that makes some people feel excited and others feel anxious. Those who feel excited and passionate about accessibility tend to be individuals with exposure to users with disabilities. While this exposure does not take away the challenge of making things accessible, it *can* foster a strong sense of [empathy](https://www.nngroup.com/articles/sympathy-vs-empathy-ux/) for these users and an urgency to make things better. [Getting buy-in](https://www.nngroup.com/videos/convincing-companies-ux-accessibility/) for accessibility and [integrating accessibility efforts](https://www.nngroup.com/1-hour-talks/making-accessibility-happen/) into your existing processes can reduce anxiety around this topic. This article intends to help our audience understand how users who are blind and partially blind experience websites and apps on a mobile device when they are using a screen reader.

## In This Article:

- [Room for Improvement in Accessibility](#toc-room-for-improvement-in-accessibility-1)
- [1. Screen Readers Present All Information Sequentially](#toc-1-screen-readers-present-all-information-sequentially-2)
- [2. Screen Readers Make It Difficult to Scan](#toc-2-screen-readers-make-it-difficult-to-scan-3)
- [3. Poor Labels Are Confusing and Unhelpful (as Always)](#toc-3-poor-labels-are-confusing-and-unhelpful-as-always-4)
- [4. Accessibility Menus: Not Considered Helpful](#toc-4-accessibility-menus-not-considered-helpful-5)
- [Methodology](#toc-methodology-6)
- [Conclusion](#toc-conclusion-7)

## Room for Improvement in Accessibility

While great strides have been made in the last decade to improve the accessibility of websites and apps on mobile devices, there is much yet to be done. In one research session, we invited a participant who was fully blind and extremely skilled at using a screen reader, to choose an app he loved because it was easy to use. His response was instructive and set the theme for the entire study:

> *“That’s a hard statement because I don’t love any app .”*

He explained that there are apps he finds *useful*, but all apps are challenging to use with a screen reader and take a long time to figure out. Each design presents a whole new set of challenges for screen-reader users. Even apps from enormous companies such as Apple, Walmart, Target, and Amazon — which have entire teams dedicated to accessibility — presented challenges for some of our most-experienced participants.

## 1. Screen Readers Present All Information Sequentially

One completely blind participant made the following comment while reflecting on what it is like to use a screen reader:

> *“The only way I can find [what I want] is by swiping [...] until [the screen reader] reads it to me, which is very different from a sighted person who just sees what they want and goes there. [...] Everything for me with [the screen reader] is very linear. ”*

To understand the significance of this insight, one must attempt to navigate a completely new app or website using a screen reader — without looking. Screen readers read out one piece of information at a time and then wait for the user to swipe before reading what comes next. Swiping moves the screen reader's focus to the next or previous page element in the sequence dictated by the code.

Imagine covering your phone screen with a black piece of paper that has a small hole cut out, only revealing one tiny part of the screen at a time. Then imagine that, as you swipe, the hole jumps between page elements from left to right, top to bottom (or in any other custom pattern the code dictates) to sequentially reveal what is on the page.

*Swiping while using a screen reader announces one page element at a time. Someone using a screen reader is unaware of everything ahead and must remember everything they have already encountered.*

Although screen-reader users can tap or drag their finger around the screen to directly access anything there, doing so is generally useless because they are essentially just fumbling around in the dark with little or no idea of what they will find — especially in new environments. Even if a user did happen to tap on something useful, they would have no way of knowing how that page element was related to other parts of the design and would be unlikely to find it again. Thus, users who spend significant time relying on screen readers tend to methodically swipe forward and backward to navigate websites and apps, so they can develop a useful [mental model](https://www.nngroup.com/articles/mental-models/) of the environment. Those participants in our study who continuously tapped around “in the dark” rather than swiping forward and backward with the screen reader were often lost and confused.

Interacting with a screen reader is an extreme example of [sequential access](https://www.nngroup.com/articles/direct-vs-sequential-access/)**,** which is when users must interact with content one piece at a time, in a specific order. The user cannot jump around; they must move forward and backward through the sequence to access what they want. To access the last element in the sequence, they must pass through all the ones preceding it. [Carousels](https://www.nngroup.com/articles/mobile-carousels/), [decks of cards](https://www.nngroup.com/articles/cards-component/), and some [videos](https://www.nngroup.com/articles/video-usability/) are examples of design elements that require sequential access. The opposite of sequential access is **direct access,** which gives users the [autonomy](https://www.nngroup.com/articles/increase-user-autonomy/) to interact with information in any order they desire because they can see and access all of it at once.

### Implications for Design

What are the implications of this reality for designers and developers? **The screen-reader sequence must be crafted intentionally.** Designers and developers should try “removing the mouse” on desktop or turning on the screen reader for mobile to test the sequential navigation of their designs.

*The participant was trying to begin a new chat in Snapchat. After tapping on the contact with whom he wanted to chat, the screen reader's focus did not immediately jump to the overlay, and he assumed that nothing had happened.*

![Tapping on an expandable menu does not move the screen reader focus to the top of the overlay that appears.](https://media.nngroup.com/media/editor/2023/04/19/snapchat.jpg)

*Bad-design example: When the user taps on the + icon to open a menu in Snapchat, the menu opens as an overlay, but the screen reader's focus remains on the + button. Even if the user swipes left or right, the focus does not move to the newly opened menu.*

![The screen reader focus should jump to the top of a new overlay that results from a user tapping on a page element.](https://media.nngroup.com/media/editor/2023/04/19/snapchat-2.jpg)

*Suggested improvement: It would be better if the screen reader's focus immediately jumped to the beginning of the newly opened menu. The user will expect to interact with the newly opened menu as a result of their action.*

![The screen reader focus correctly jumps to the top of the overlay after a user triggers it to appear with a tap.](https://media.nngroup.com/media/editor/2023/04/19/target.jpg)

*Good-design example: When the user selects the* Filter *button in the Target app, a* Filter *overlay is displayed, and the screen-reader focus is taken directly to the top of the overlay.*

Screen-reader users are confused when, as they are swiping along, they hear something that seems unrelated to what they have heard so far. It is equally confusing when a user takes an action (e.g., tapping a button), yet the screen reader's focus remains in the same place as if nothing has happened. This is one reason why screen-reader users rely on in-page or on-site [search](https://www.nngroup.com/articles/search-not-enough/) whenever they can: it helps them jump straight to what they are looking for. Browsing through menus, page content, and filter options is incredibly tedious.

Users who are not confident using a screen reader or who still have some vision are more likely to tap around “in the dark” to search for something relevant. Tapping around rather than swiping sequentially circumvents the sequence of the screen-reader progression but might not result in something useful.

For those users who do have partial vision (as for sighted users), use a strong visual hierarchy, with good grouping and sizing of the most important elements, so they can see these elements and interact with them.

*A study participant with low vision attempted to tap on page elements rather than swipe through them sequentially. His task was to find a toy lion on the Playmobil website. (Notice how he makes no use of the accessibility menu in the bottom-right corner of the screen).*

## 2. Screen Readers Make It Difficult to Scan

One of the most common behaviors we have seen on the web for decades is [scanning](https://www.nngroup.com/articles/how-users-read-on-the-web/)**.** Users scan to efficiently decide if a page holds anything relevant to their current task. Users who are blind or have low vision obviously cannot visually scan through content to determine whether a page has something relevant for them. However, screen-reader users have developed their own version of this efficiency trick.

Screen-reader users scan content by having the screen reader jump between major page elements (such as headings or links) rather than reading out every single word on a page. This approach allows them to explore content at a high level before getting lost in the little details. Think of them as travelers who explore a new country by flying from major city to major city rather than driving through every little town along the way.

This behavior is not unlike what sighted users do in [our eyetracking studies](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/). The major difference is that screen readers can identify a heading as a heading only if it has been coded that way, whereas sighted users can identify important information based on the [visual hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/) of the page. **Headings must be marked as such in the code**(e.g., contained within a heading tag such as H1 or H2 in HTML)**** for a screen reader to recognize them. It is not enough to use large, bolded fonts that look like headings.

![IOS and Android both provide ways for screen reader users to switch between page elements they can jump between.](https://media.nngroup.com/media/editor/2023/04/19/rotor.jpg)

*Using the rotor on iPhone (left) or changing the reading controls on Android (right) allows users to jump between page elements as they swipe on the screen. Users use custom gestures to indicate which page elements the screen reader should jump between.*

Multiple study participants relied on jumping between headings on long pages — such as detailed [product pages](https://www.nngroup.com/articles/ecommerce-product-pages/) or [search engine result pages](https://www.nngroup.com/articles/anatomy-search-results-page/) (SERPs) — to find helpful information. Wading through all the copy on the page to find something informative requires too much time and energy for users.

![Long pages are easier to jump through with a screen reader when major headings are coded properly.](https://media.nngroup.com/media/editor/2023/04/19/amazoncom-garden-rake14-tines-heavy-duty-bow-copy.jpg)

*Screen-reader users greatly rely on the ability to jump between headings on pages with a lot of content.*

One challenge presented by this rule is when there is only one heading on a page. When a book begins with “Chapter One,” it [primes](https://www.nngroup.com/articles/priming/) the reader to assume that there will be more chapters ahead. Similarly, one heading on a page primes screen-reader users to think that there will be multiple such headings; therefore, they may try to jump between them to scan through the content.

Consider the following two pages. Both have only one major heading. In the case on the left, the heading was coded as a heading. Discovering the heading caused one study participant to switch his screen reader into *Headings* mode and try to jump down to locate the other headings before getting into the details of the page. He was surprised to realize that there was a single heading on that page. In the screenshot on the right, the highlighted phrase was not coded as a heading, thus, preventing the user from wasting time looking for other headings.

![Pages with only one heading might not need the heading to be coded as such for screen readers.](https://media.nngroup.com/media/editor/2023/04/19/headspace-headers.jpg)

*Left: The highlighted text was coded as a* heading *and prompted the user to switch his screen reader into* headings *mode. Right: The highlighted text was not coded as a* heading *, so the user did not try to read the other headings on the page.*

Using semantic HTML elements doesn't just afford efficient navigation, it also sends signals about what is important and interactive on the page. While a button might be stylized to look like a button to sighted users, screen-reader users will have no idea they could click on it if it is not coded properly as a button (i.e., <button type="button">Click Me!</button>). Screen-reader users constantly listen for words such as "heading," "button," or "link" that come from HTML tags because these words help them figure out how to interact with a design. When page elements have been coded properly, it is NOT necessary to include words such as "button" or "link" in the actual labels themselves.

## 3. Poor Labels Are Confusing and Unhelpful (as Always)

Properly coding page elements is important, but it’s not enough. Even if a screen-reader user can jump between links on a page, it will not be useful to get multiple [Learn more links](https://www.nngroup.com/articles/learn-more-links/), all in a row. We have always recommended that headings, navigation-menu items, and links be [as informative as possible](https://www.nngroup.com/articles/better-link-labels/), to increase their [information scent](https://www.nngroup.com/articles/information-scent/). Links and other page elements should be frontloaded with keywords so users can quickly decide whether clicking on them will be helpful for their goal. However, this study confirmed that informative labels are *even more* important for screen-reader users than for sighted users for two reasons:

- **Screen-reader users have little or no visual context for a link.** A sighted user might use the context in which a link is placed (e.g., imagery, visual hierarchy, or placement on a page) to determine if it will be useful. However, none of this information is available to screen-reader users. They must make most decisions based on the link label.
- **Many screen-reader users swipe through page elements very quickly** without listening to the entire label. If the first few words of the label don’t seem relevant, they’ll swipe and quickly move on.

One user in our study could not find the search box in Apple’s App Store because the page element was labeled *Games, Apps, Stories, and More. Search field. Double-tap to edit. (* The label also happened to be positioned inside the field — [a practice we recommend against](https://www.nngroup.com/articles/form-design-placeholders/).) The user listened to the first few words multiple times, as he swiped up and down the page, but he never realized that this label corresponded to the search box because the first few words were not related to search and he did not listen to the whole label. He eventually gave up, without realizing that the search was right under his nose.

![The placeholder text in the search bar is not frontloaded with keywords related to search.](https://media.nngroup.com/media/editor/2023/04/19/img_0983.jpeg)

*Apple’s App Store: One screen-reader user did not recognize the search box because its label was not front-loaded with words related to search.*

## 4. Accessibility Menus: Not Considered Helpful

Some websites rely on accessibility menus provided by third-party companies to improve the accessibility of their designs — particularly to meet ADA requirements and WCAG accessibility standards. These accessibility menus are available on every page of a website and provide options meant to assist users with all kinds of needs, including blindness and low vision. One major selling point of these accessibility menus is the ease with which developers can add a widget in the code to allow users to adapt how the design is displayed. Some common options found in these menus include:

- An available screen reader
- Alterations to visual contrast
- Customizable text sizes, spacing, and alignment
- Motion reduction (such as pausing animations)

![Example of Userway accessibility menu](https://media.nngroup.com/media/editor/2023/04/19/userway-2.jpg)

*The UserWay accessibility menu on the Coca-Cola website*

![Example of AccessiBe accessibility menu](https://media.nngroup.com/media/editor/2023/04/19/accesibe-2.jpg)

*The accessiBe usability menu on the Six Flags website*

We wondered how practically useful and recognizable these accessibility menus are to real users who are blind or have low vision. To answer this question, we had participants in our study perform tasks on mobile websites with these accessibility menus. The short answer is that **our screen-reader users did not find them useful.**

When we brought screen-reader users to websites with these accessibility menus, we waited to see whether they would discover them by themselves. Although participants did come across these menus as they completed tasks,**not one user opened the menus of their own accord.** The accessibility menus were almost completely ignored by both study participants who were fully blind and by those who were partially blind.

### Screen-Reader Users’ Impressions of Accessibility Menus

When participants did not open the accessibility menus on their own, we prompted them to open the menus and see whether there was anything that seemed useful inside. After briefly exploring one accessibility menu, a participant commented, *“the first thought that comes to mind is what a waste of time and money […] when anyone using a phone that needs a screen reader is already gonna have one built in.”*

#### Redundant

Screen-reader users generally become very accustomed to their screen reader (usually, one mobile, it is the one provided by the operating system). To use an accessibility-menu screen reader, users must turn off the operating system screen reader they have been using up to that point. (As one participant put it, you should run two screen readers at once only “if you want a headache.”) There is no reason for them to abandon a system they are already efficient with, in order [to learn a new one that](https://www.nngroup.com/articles/power-law-learning/) may be less good than what they already have and that will be available only on a subset of sites.

#### Restrictive

The built-in operating-system screen reader offers more user [control and freedom](https://www.nngroup.com/articles/user-control-and-freedom/) than any of the accessibility-menu ones. For example, in the accessibility-menu screen reader, to adjust the speaking rate, users must navigate around to find the menu again, open it, and choose one among a few speeds. The operating-system screen reader allows users to adjust the speaking rate very finely with custom gestures, at any time.

While third-party accessibility menus might provide helpful adaptations for some sighted users and may protect companies from being sued, our test led us to believe that they do not significantly improve the accessibility for users of screen readers. As one blind user put it, *“I hate [accessibility menus] because […] I think they make companies feel like they don't need to actually work on making something accessible […] it is not a substitute for actual accessibility testing and, to me, it feels like just a Band-Aid that can almost make it worse sometimes.”* If a company wants to make a design accessible, there is no substitute for [testing it with real users that have disabilities](https://www.nngroup.com/videos/convincing-companies-ux-accessibility/). Most accessibility issues are structural and cannot be fixed by a simple plugin.

## Methodology

We conducted a series of in-person research sessions with participants who relied on screen readers to use mobile devices because they were blind and partially blind. The participants used their screen readers to complete all the activities and tasks throughout the sessions. We employed a mix of [usability testing](https://www.nngroup.com/articles/usability-testing-101/), [contextual inquiry](https://www.nngroup.com/articles/contextual-inquiry/), and [user interviews](https://www.nngroup.com/videos/3-types-user-interviews/). The sessions were conducted in participants’ homes or personal offices. We extend our gratitude to each individual who participated in this research and allowed us to visit them.

Our study investigated two main questions:

1. Which characteristics of mobile designs make them **particularly easy** or **particularly difficult** to use?
2. How do users who are blind or have low vision learn to navigate **completely new digital environments** on their smartphones?

The following sections address 4 major findings that emerged in this study.

## Conclusion

Improving the accessibility and usability of a digital product for screen-reader users takes work; there is no quick and easy fix. Recognizing how the experience of using a screen reader differs from the way sighted users experience a website or application can help designers anticipate the difficulties that screen-reader users may encounter.
