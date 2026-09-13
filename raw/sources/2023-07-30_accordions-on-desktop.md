---
title: "Accordions on Desktop: When and How to Use"
date: "2023-07-30"
url: "https://www.nngroup.com/articles/accordions-on-desktop/"
author: "Huei-Hsin Wang"
topics: [design-patterns, interaction-design]
type: article
---

Swimming through a sea of content and trying to find what we are looking for can feel tiresome, particularly when faced with lengthy, information-rich web pages. An accordion is a design pattern that can help mitigate the challenge.

## In This Article:

- [What is an Accordion?](#toc-what-is-an-accordion-1)
- [Benefits of Accordions](#toc-benefits-of-accordions-2)
- [Usability Issues Caused by Accordions](#toc-usability-issues-caused-by-accordions-3)
- [When to Use & When to Avoid Accordions](#toc-when-to-use-when-to-avoid-accordions-4)
- [Consideration When Implementing Accordions](#toc-consideration-when-implementing-accordions-5)
- [Conclusion](#toc-conclusion-6)

## What is an Accordion?

> An **accordion** is a header that can be clicked to reveal or hide content associated with it.

An accordion is typically made up of three elements:

- **Heading**: A descriptive title that conveys the gist of the information contained within the accordion
- **Icon**: A graphic symbol that signifies the state of the accordion and whether it will expand or collapse
- **Panel**: The secondary content that is hidden when the accordion is closed

![Illustration of accordions each containing a heading, an icon, a panel](https://media.nngroup.com/media/editor/2023/07/11/accordion-anatomy.png)

*Anatomy of an accordion: An accordion is made up of 3 key components—heading, icon, and panel. These elements work together to provide users with control and flexibility in accessing information while maintaining a minimalistic and organized interface.*

Accordions are a type of [progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/). The heading provides a concise overview of the topic. The panel is hidden by default, offering supplementary details to those who are interested. An accordion thus empowers people to choose what to read and what to skip. It supports [user control and freedom](https://www.nngroup.com/articles/user-control-and-freedom/), the third of the [10 usability heuristics for user-interface design](https://www.nngroup.com/articles/ten-usability-heuristics/).

## Benefits of Accordions

Accordions are versatile. They share similarities with [anchor links](https://www.nngroup.com/articles/in-page-links/), helping users navigate through page content. They also can be used to organize information in a logical manner and implement as a [mini-IA of a page](https://www.nngroup.com/articles/mini-ia-structuring-information/). The following are key advantages of accordions.

### Reducing Clutter

Disclosing rich information all at once can make a page cluttered and overwhelming. Accordions display information one section at a time and hide information that is not relevant to the user. They simplify the page, lowering users’ [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/) and allowing them to concentrate on the information immediately at hand.

![A screenshot of TurboTax Tax Calculator which uses accordions to display different sections required to finish the form](https://media.nngroup.com/media/editor/2023/07/11/turbotax.png)

*TurboTax Tax Calculator: The different sections in the form are represented by accordions. Once the user has completed a section, the accordion for the next one automatically expands. Users can focus on answering the questions in the current section, without being distracted or overwhelmed by the fields in other sections.*

### Minimizing Scrolling

Users are used to scrolling, but [they scroll for a purpose](https://www.nngroup.com/articles/page-fold-manifesto/). Collapsing information in accordions not only shortens the page but also ensures that essential content remains visible. Accordions reduce the effort required to navigate through long pages and allow a broader range of topics within the content to remain accessible without the need for scrolling.

![A product detail page uses accordions to display product information](https://media.nngroup.com/media/editor/2023/07/11/logitech.png)

*Logitech: Accordions are utilized on this page to present product information. By collapsing information under the accordions, all relevant topics remain visible above the fold. This design allows users to access information from each topic conveniently, without the need to scroll down the page.*

### Conveying an Overview of the Page

Just like how animals forage for food, [users navigate on the web to satisfy an information need](https://www.nngroup.com/articles/information-foraging/). As soon as they land on a page, they start to look for [cues that assure them they are on the right track to finding what they need](https://www.nngroup.com/articles/information-scent/). An effective webpage should promptly communicate what users can expect to find on the page and eliminate any unnecessary guesswork as it won’t take long until they decide to seek their answers elsewhere. This is where accordions can play a vital role—acting as a concise table of contents, providing users with an overview of available content without delving into details. Accordions help users form a [mental model](https://www.nngroup.com/articles/mental-models/) of the page, empowering them to navigate with confidence and efficiency.

![A course offering page uses accordions to display course topics in the syllabus](https://media.nngroup.com/media/editor/2023/07/11/codecademy-course-syllabus.png)

*codecademy: This course detail page uses accordions to present key topics in the course syllabus, allowing users to get a high-level overview of the course content without delving into details.*

### Improving Scannability

Research shows that [people tend to scan web pages rather than read them word by word](https://www.nngroup.com/articles/how-users-read-on-the-web/). Therefore, web pages should accommodate this behavior by making the content easily scannable. One effective strategy is to [organize information in chunks](https://www.nngroup.com/articles/chunking/). Accordions shine in this regard as they break down lengthy content into digestible sections. Accordion headings support scanning by highlighting the main points of each chunk. This streamlined presentation enables users to process information faster and better.

![A U.S. Citizenship and Immigration Services page uses accordions to display steps in consular processing](https://media.nngroup.com/media/editor/2023/07/11/uscis.png)

*USCIS: This page summarizes each step of the consular processing in a concise heading and presents them in sequential order. This logical organization allows users to scan through the list and digest the information more efficiently.*

### Direct Access to Content

Accordions allow users to quickly access the piece of information relevant to them without having to scroll through all the preceding content. [Direct access](https://www.nngroup.com/articles/direct-vs-sequential-access/) is particularly beneficial for users who are searching for specific information or are interested in only one small portion of the information on your page.

![A Google search result page displays relevant information in accordions](https://media.nngroup.com/media/editor/2023/07/11/google.png)

*Google: The* People also ask *section on the search result page uses accordions to present a list of commonly asked questions. Users can go directly to the question of interest without having to read through all the preceding questions.*

## Usability Issues Caused by Accordions

Despite accordions’ ability to effectively organize information and simplify long, complex pages, their use on desktop is not always recommended. Here are some of their drawbacks.

### Fragmented Access to Information

Using accordions on a content page can hinder users’ ability to access information from different content blocks. When a user needs to access information from most or all accordions, it can become tedious to have to expand each of them. Excessive clicking interrupts people’s interaction with the page. Forcing users to interact with each panel individually to access the information can lead to a loss of context when important details are scattered across different panels. Users may have difficulty connecting related information from different sections on the page.

This problem can further escalate when an accordion automatically closes when another is opened, **restricting users’ ability to combine information from multiple accordions at the same time**. If you expect users to need information from several accordions at once, it is better to display all the content at once (even if it results in a longer page).

*Administration for Community Living: On this page, the accordion collapses automatically when the user opens another accordion, hindering users’ ability to compare the information from both accordions at the same time.*

### Increased Interaction Cost

Each step involved in expanding the accordion—scrolling the page, scanning the headings, deciding which one to expand, targeting the click, and waiting for the content to appear—incurs a certain [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/). These individual substeps may seem minor, but they accumulate and can become burdensome for users.

### Compromised Discoverability

Utilizing accordions to hide secondary content simplifies the page, but it also compromises the discoverability of the collapsed content. Valuable content that is hidden under an accordion may be missed altogether. Furthermore, when the heading fails to provide a descriptive and enticing preview, users are less likely to expand the accordion and might miss out on the entire section hidden beneath. This diminished discoverability undermines the effectiveness of the information contained within the accordions.

![A government information page displays mask mandate in the accordion](https://media.nngroup.com/media/editor/2023/07/11/usda.jpg)

*USDA: The accordion labeled* Mask **Guidance* contains important information about face mask requirements. Collapsed and hidden by default, this information can be overlooked. In this case, given the brevity of the content within the accordion, displaying the information directly on the page without using an accordion would be more effective.*

### Accessibility Considerations

Plain text is inherently accessible without additional measures. In contrast, designers must make sure that accordions are accessible for [keyboard](https://www.nngroup.com/articles/keyboard-accessibility/) and [screen-reader users](https://www.nngroup.com/articles/screen-reader-type-control/). To achieve this, the accordion heading should function as a button, allowing keyboard users to interact with the element. Screen readers should also announce the state change when the accordion is opened or collapsed. In addition, **when the accordion is collapsed,****ensure the content inside the panel is both visually hidden and programmatically unreachable to all users**. Simply making the content invisible without restricting access can lead to an inconsistent user experience and confuse sighted keyboard users as they won’t be able to see what they are interacting with.

### Difficulty with Printing

Accordions are often not optimized for printing. In the absence of an *Expand All* button or of a special implementation to optimize printing, users are required to expand each accordion individually before printing. This can be cumbersome, especially on lengthy pages with numerous accordions and extensive content.

Additionally, auto-collapse accordions that permit only one accordion to be open at a time make it impossible for users to access and print all the content on the page at once. When incorporating accordions, it is crucial to ensure that the page is properly configured to facilitate printing. Consider including an *Expand All* button or expanding accordions automatically at print preview.

## When to Use & When to Avoid Accordions

Deciding whether to incorporate accordions into your design requires careful consideration of the tradeoffs and benefits involved. Start by considering:

- **Your audience's needs**: What are the common and critical use cases? Do accordions help users find answers to their questions more efficiently?
- **The specific content you are presenting**: Does the content structure lend itself well to accordion-style presentation? Are there alternative navigation tools or design patterns?

Based on these considerations, the following recommendations can guide your decision.

### When to Use

- **When users need only a few pieces of information on the page**, they will likely skip most of the content. Hiding most of the content on the page helps users spend their time more efficiently by focusing on the few topics that matter.
- **When****the main task is a logical, step-by-step process**, accordions can guide users through the process by presenting information relevant to the current step and hiding irrelevant details that can distract or overwhelm users. This approach is commonly used to simplify multistep flows, making the experience more manageable for users.

![An ecommerce check-out page displays each check-out step in an accordion](https://media.nngroup.com/media/editor/2023/07/11/sephora.png)

*Sephora:**The checkout page leverages accordions to guide users through each step of the checkout process. Each subsequent accordion expands only when all the required information from the previous step has been provided, ensuring that users don’t miss any required entries. (Unfortunately, the accordions lack a proper signifier — there is no icon indicating that they expand in place.)*

- **When the information in each section is independent and users are unlikely to need simultaneous access to multiple sections,** accordions can help them quickly access only the section of interest.**** FAQ pages and product-detail sections are good candidates for accordions.

![A FAQ page displays frequently asked questions in accordions](https://media.nngroup.com/media/editor/2023/07/11/delta.png)

*Delta: The FAQ page utilizes accordions to present common questions. Each question is featured in the heading, and the corresponding answer is contained within the collapsed panel. This design allows users to easily navigate through the list of questions and expand only the ones they are interested in.*

- **When the content is long and the window size is small,** which is especially relevant [on mobile devices](https://www.nngroup.com/articles/mobile-accordions/),**** using accordions helps prioritize content display and reduce the page length.

### When to Avoid

- **When your audience requires the majority or all the content on the page to find answers to their questions**, show all the content at once. In this case, easy access to essential information matters more than reduced page length.

![A university information page displays application requirements in accordions](https://media.nngroup.com/media/editor/2023/07/11/university-requirements.png)

*Northeastern University: Visitors to this page are likely to expand all the accordions to view all the application requirements. In such cases, it is more advantageous to present all the content at once, thereby saving users from unnecessary clicking and the potential risk of overlooking essential information.*

- **When there is little content on the page,** accordions will make the page look mostly empty. Avoid using accordions to conceal information, as the absence of content can cause the illusion that there is no valuable information on the page and prompt users to abandon the page.

![A government information page collapses content in accordions, only displaying a heading on the page](https://media.nngroup.com/media/editor/2023/07/11/minnesota-department-of-revenue_stacked.png)

*Minnesota Department of Revenue: With accordions, there is a lack of visible content on this page (top). Displaying all the content at once (bottom) is better because users can see most of what the page has to offer. The use of accordions is not necessary in this case because, even when the content is all visible, the page is quite short—there is not a lot of information to be displayed.*

- **When the content has a deep hierarchy****with multiple sublevels**, it can be too complex to be displayed in a flat-hierarchy format like accordions. Users may feel confused and lose track of where they are within the accordion structure. In such cases, consider alternatives such as tabs or vertical [local navigation](https://www.nngroup.com/articles/navigation-you-are-here/) to better accommodate the hierarchical nature of the content.

![A university degree audit page uses accordions to display hierarchical information](https://media.nngroup.com/media/editor/2023/07/11/degree-audit.png)

*University of Cincinnati* Degree Audit page *uses nested accordions to display course requirements and current academic progress. With multiple levels of information displayed under accordions, users may struggle to maintain a clear sense of their location within the accordion structure.*

- **When the content is scattered and difficult to summarize**, it becomes a challenge to chunk the content and come up with representative headings that effectively convey the essence of the information. As a result, failure to capture the precise gist can lead to confusion and may not effectively convey the essence of the information hidden within the panels.

![A page displays show recommendation list, each item contains name, ranking, rating, thumbnail, critics consensus, cast and director information](https://media.nngroup.com/media/editor/2023/07/11/rottentomatoes-recommendation.jpg)

*Rotten Tomatoes: This page offers recommendations for a wide range of shows, each accompanied by a brief sentence explaining the reasons for the recommendation. It would be difficult to present this information with accordions as summarizing the content with concise headings will likely leave out crucial context and diminish the ability to entice users.*

- **When users are likely to immerse in a continued flow of reading,** using accordions could disrupt the experience by fragmenting the information and hindering users' ability to comprehend the full context. This is why news articles or narratives often avoid accordions, even when dealing with longer pages—a seamless reading experience and uninterrupted narrative flow are prioritized in such cases.

![A long article page split into 3 screenshots does not use accordions to display content](https://media.nngroup.com/media/editor/2023/07/11/vox.png)

*Vox: Despite the length of the content on this page, it is preferable to present all the information on a single scrollable page compared to using accordions that mandate excessive clicking. Embracing a scrollable page design allows users to navigate through the content seamlessly, without the need for constant interactions.*

## Consideration When Implementing Accordions

If you choose to incorporate accordions into your design, keep the following guidelines in mind:

- **Ensure that the heading accurately reflects the content within the panel**. A clear, descriptive heading is key to enticing users’ interest in exploring the detailed content inside the accordion. [The labels of accordions](https://www.nngroup.com/articles/better-link-labels/) can greatly impact the findability, discoverability, and accessibility of your content.
- **The visual design of the accordion should clearly indicate that it can be expanded.** One of the biggest pitfalls of accordions is the lack of a clear signifier to tell users that they can expand them. Useful content is left unknown, unseen, and unconsumed. To prevent this, provide appropriate icons ([the caret and the plus work best according to our research](https://www.nngroup.com/articles/accordion-icons/)) that clearly communicate the clickability of the accordion headings. In addition, ensure that both the heading and icon are clickable and they both expand or collapse the accordion.
- **Allow users to open or collapse multiple sections at a time.** Users should have full control over the access of the content on the page. Consider including an *Expand All* and *Collapse All* button to facilitate faster navigation and allow users to customize their viewing experience.
- **Avoid hiding any crucial information within the collapsed panels.** Essential information should be presented outside of accordions to ensure it is readily available and not easily overlooked. By doing so, you prevent critical content from being buried and ignored.

## Conclusion

Accordions are a valuable tool for organizing and simplifying complex web pages. When implementing accordions on desktop, consider potential drawbacks and make informed decisions based on your audience's needs and the nature of the content being presented. By weighing the tradeoffs and aligning with content requirements, you can use accordions effectively to enhance user experience and facilitate efficient navigation.
