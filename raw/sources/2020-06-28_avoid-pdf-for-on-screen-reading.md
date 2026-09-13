---
title: "Avoid PDF for On-Screen Reading"
date: "2020-06-28"
url: "https://www.nngroup.com/articles/avoid-pdf-for-on-screen-reading/"
author: "Anna Kaley, Jakob Nielsen"
topics: [web-usability]
type: article
---

No matter how tempting it is, you should never use a PDF to display content that users need to read online. After [20 years of watching](https://www.nngroup.com/articles/avoid-pdf-onscreen-reading-original/) users perform similar tasks on a variety of sites that use either PDFs or regular web pages, one thing remains certain: PDFs degrade the user experience.

## In This Article:

- [Problems with PDFs](#toc-problems-with-pdfs-1)
- [Why PDFs Are Still Prevalent](#toc-why-pdfs-are-still-prevalent-2)
- [Guidelines for Using PDFs](#toc-guidelines-for-using-pdfs-3)
- [Updates in 2020: PDFs Still Causing Trouble](#toc-updates-in-2020-pdfs-still-causing-trouble-4)

## Problems with PDFs

PDFs are meant for distributing documents that users will print. They’re optimized for paper sizes, not browser windows or modern device viewports. We often see users get **lost in PDFs** because the print-oriented view provides only a small glimpse of the content. Users can’t [scan and scroll](https://www.nngroup.com/articles/how-users-read-on-the-web/) around in a PDF like on a web page. Content is split up across sheets of paper, which is fine for printed documents, but causes severe usability problems online.

PDFs also use lots of heavy, dense text and elaborate graphics which increase their file size and, subsequently, the time they take to download. They **lack navigation** and other interface elements that help users maintain context and move through digital content with speed and ease. The inability to navigate takes a toll on users as finding information becomes challenging and time consuming. Clickable tables of contents are often introduced in PDFs as pseudo navigation, but users still slow down and have trouble finding what they need. The use of *Command* or *Control* + F to find something within a PDF is not familiar to all users. Some users will take advantage of these shortcuts, but others won’t.

PDFs’ usefulness as a vehicle for print is also diminishing due to environmental concerns. Many organizations and individuals now place a heightened emphasis on [sustainability](https://www.nngroup.com/articles/corporate-social-responsibility/), and, therefore, think twice before printing off a lengthy document that could and should otherwise be formatted and structured for online consumption.

## Why PDFs Are Still Prevalent

PDFs are still commonly used because people incorrectly assume that posting a PDF online is faster and easier than creating a webpage, so that’s all that ever gets done. However, you still have to plan, write, and design the content you’ll put in the PDF. Why not spend that time on an accessible HTML page, that’s [properly written, and formatted for the web](https://www.nngroup.com/topic/writing-web/)? For example, when we asked an intranet-team lead about her team’s [content-management processes](https://www.nngroup.com/articles/intranet-content-management/), she said,

> “Someone usually hands us a PDF and says, ‘Here, put this online.’ We have a style guide and try to help our peers understand that we need to pick the layout for the content before it goes on the intranet. They want it to be pretty, but we want it to be useful. We have tried to enforce standards, but people always say they need it quickly and expect us to post the PDF.”

In reality, it takes more time to manage updates and handle versioning control with PDFs than with webpages. To make a simple change, you have to find the original document, make the change, ensure it’s accessible, save it as a new PDF, repost it to the web, and ensure that any existing links point to the new version. In contrast, with a web page, you simply open the CMS, find the page, make the change using a WYSIWYG editor, save it, and publish it. If you’re using a component-based design, [design system](https://www.nngroup.com/videos/design-systems/), or a set of predetermined templates, you don’t have to spend much time figuring out how the web page will look and the link will stay intact after the change is made.

In some cases, PDFs are preferred because they give less-savvy content creators a sense of ownership, control, and protection over the message and layout. They may feel that moving the content from a PDF to a webpage will relinquish some of that control; or, maybe, they don’t think they can post the content effectively in a webpage. They could also refuse to acknowledge how bad PDF is for usability, assuming it’s good enough the way it is. In another example, when we asked a content manager what instigates changes to the intranet, she said,

> “Normally we get a Word document or an Excel spreadsheet. Sometimes it’s a PDF. For anything that I link to on the intranet, I will convert it to a PDF”

There are legitimate cases when policies must exist in PDF format on a [company website](https://www.nngroup.com/articles/about-us-information-on-websites/) or intranet (e.g. legal reasons), but this doesn’t mean PDF is the only format in which the content should exist. PDFs are commonly passed around corporate communications and legal teams anyway, so it’s no wonder they often make their way onto intranets and corporate websites. During a field study, we observed a content manager trying to make sure that the PDFs were up to date; she crafted an email to a colleague which said,

> “Hello! I have the attached PDF documents available for our intranet site. Is the information still valid? Or do you have anything else we can share?”

Technical or resource limitations also lead to an organization’s use of PDFs over web pages. Team members may only be partly responsible for content creation or management in addition to their full-time role, so formatting the content for the web becomes a lower priority. Or, content owners may only be comfortable using simple, familiar tools like word-processing software and presentation slides that make exporting to PDFs much easier than learning how to use a new tool or content-management system. Organizations also often also lack proper content strategy and processes that would otherwise protect their digital experiences from the wrath of haphazardly posted PDFs. On that topic, one content manager said,

> “This is a hobby. We have a coordinator who usually posts content, but she is out, and I like changing activities. So, since I can do it, I just do it.”

## Guidelines for Using PDFs

If you must include a PDF in your experience, follow these guidelines to make it as usable as possible and to lend a smooth transition from a digital to a paper-based experience. Again, a PDF should never be used to display digital content that users will read online. It’s only suitable for print.

**1. Gather evidence to understand whether users need and expect to print out a PDF.** Which documents fall in this category? Well, you need to conduct research such as [field studies](https://www.nngroup.com/articles/field-studies-done-right-fast-and-observational/), [usability testing](https://www.nngroup.com/articles/usability-testing-101/), and [contextual inquir](https://www.nngroup.com/videos/contextual-inquiry/)[ies](http://www.nngroup.com/videos/contextual-inquiry/) to find out. It could be appropriate to provide a PDF version of a large document such as a report or manual, or something as simple as a single-page cafeteria menu or sprint calendar for your [scrum team](https://www.nngroup.com/articles/ux-scrum/). It will all depend on your users’ context and reading preference, relative to the content and task. If you find users don’t want to print out a document, explore a better *digital* format in which to serve the message.

**2. Make the PDF accessible when you’re creating it.** PDF is not inherently accessible. There’s additional work that needs to be done to ensure it is inclusive; you can’t just export it and assume it’s good to go. The text must be searchable, fonts must allow characters to be extracted to text, and form fields must be labeled as interactive and include error messages with proper timing. Users should be able to access bookmarks using the keyboard, and security settings on the PDF must not interfere with screen-reader capabilities. Structural tags on headlines, paragraphs, tables, and other elements need to be set to define reading order, and *ALT* text must be included on all images. Color should not be used to convey meaning and there must also be proper [contrast between foreground and background.](https://www.nngroup.com/articles/low-contrast/)

**3. Create an HTML gateway page that gives users the information they need, without forcing them to read a PDF in a browser.**[Gateway pages](https://www.nngroup.com/articles/gateway-pages-prevent-pdf-shock/) are HTML web pages that summarize the core messages that are otherwise found in a PDF. They provide sufficient detail right on the landing page so that users don’t have to read the PDF in a browser window to get the information they need. They can still get the key takeaways in a familiar digital format, with the option to download the full PDF. The best gateway pages have content that’s formatted and structured according to the best practices for web writing. They clearly label the link to download the PDF as such, include the page count and the file size in close proximity to the link. This information will help users decide whether the PDF is worth downloading.

If technical limitations are holding you back from creating HTML gateway pages for your PDFs, collaborate with experts on web-publishing principles to create a template for an HTML gateway page. Leveraging better methods and skillsets to convert legacy PDFs to web pages will pay dividends in time saved and preservation of the user experience in the long run. With tremendous advancements in web-content management and the ease with which people can publish online content today, there’s no reason why we should still see so many PDFs. You don’t need sophisticated coding skills to create a web page and reliance on developers to post content is much less than it was 20 years ago.

![The American Cancer Society uses HTML gateway pages to house their PDF reports.](https://media.nngroup.com/media/editor/2020/05/16/americancancersocietygatewaypage.jpg)

*The American Cancer Society used HTML gateway pages to house their reports. Users can review content directly on the page or have multiple options for downloading the full PDF.*

**4. Consider whether the PDF should open in a**[new window](https://www.nngroup.com/articles/open-new-windows-for-pdfs/)**or tab, the same window or tab, or should directly download.** This is another guideline that requires observational research, since the right answer may be different depending on the audience and on the task. For situations where the PDF will be used as a reference while completing some other flow (e.g., when the PDF has instructions for a process), it’s helpful to have it open in a new tab or a new window, so users can easily switch attention between the main flow and the reference. However, if the PDF is likely to be used by itself, then having it in a different tab can burden users by increasing browser clutter (too many tabs). And, on mobile, multiple tabs are often confusing and hard to manage.

For example, in our recent intranet research, many employees had several browser tabs open at a time to complete their work. When they encountered a PDF (or several) that opened in yet another new tab, they often wanted to stop and pause between tasks to clean up their tabs. This housekeeping behavior indicated that users felt the interface became cluttered or unmanageable. In certain PDF contexts, it might make sense to keep users in the same window or tab, so they can click the *Back* button to return to the previous page. However, after finishing with a PDF, we often see users close the browser window instead of clicking the *Back* button, so they lose their navigation history.

Directly downloading a PDF may be the best option to protect users from the agony of reading a PDF in a browser window, but we’ve also observed users who were bothered by having to first download the PDF and then reopen the file in another platform. In any case, these are all real problems you must consider before including a PDF in the user experience. Research with your own audience is the only way to understand the best course of action to take.

**5. Link to the gateway page, not the PDF.** Never let your search engines index the PDF file if you have a corresponding gateway page. Instead, ensure that your HTML gateway page is indexed by both internal site search and external search engines. We often see PDFs rank higher than HTML pages in internal search results (possibly because big files are likely to contain lots of background information and multiple occurrences of keywords). Usability suffers when users are abruptly dumped into a PDF file, especially if it's one that merely mentions the information they need in passing on page 47. Including an icon to indicate a PDF on search results pages doesn’t really help either. Though it may initially set expectations about what the user will encounter, it doesn’t ease the tension they feel once they arrive in the PDF.

![PDF icons that sit next to search result listings.](https://media.nngroup.com/media/editor/2020/05/16/searchresultpdficon.jpg)

*Including an icon on a search results listing may inform the user they’re about to open a PDF, but it doesn’t make the experience of interacting with a PDF in a browser window any better.*

**6. Don’t be too quick to convert your documents to the latest PDF version.** As with any software, many [users are slow to upgrade](https://www.nngroup.com/articles/the-increasing-conservatism-of-web-users/)when updates become available. There are still many people and organizations who use older PDF readers, so save your documents in an earlier PDF version to help users avoid issues when opening the document.

**7. Strive for the smallest PDF file size without sacrificing quality.** Make sure the file size of your PDF isn’t so large that it will take forever to download. Or, even worse, crash the users’ browsers or cause them to use an excessive amount of cellular data. Reduce the size by making sure only the most necessary information is included and that image sizes are reduced to balance size with quality of display.

**8. Format the PDF to fit different sizes of paper**. Some countries use 8.5x11, while others use A4. Make sure your document will fit both. Avoid using multiple columns of text and small font sizes. Multicolumn text is harder to read and scan when printed out and small font sizes cause readers to strain their eyes, regardless of the medium. Remember the use case: someone is going to print out this document because, for her context and task, using paper is easier than using a device.

![Wiski Cat's PDF is nicely formatted for mobile viewing.](https://media.nngroup.com/media/editor/2020/05/16/mobile-wiski.png)

*Wiskicat.com offered users the choice of watching a 10-minute assembly video or downloading a 20-page PDF instruction book to assemble their product (left). Because the PDF used a large font and images (right), reading it on mobile is not completely impossible, even though suboptimal.*

![Wiski Cat's PDF is formatted nicely for print or browser-viewing.](https://media.nngroup.com/media/editor/2020/05/16/wiskidesktoppdf.jpg)

*It’s still not pleasant to read this PDF in a browser window, but it’s much better than many of the other PDFs we’ve seen posted online. Users printing this out to assemble a product would find it easy to read and follow due to the plain language, large font, and simple imagery used.*

**9. Remove or archive previous versions of the PDF and update links from the old version to the new.** PDFs have a way of perpetuating stale content, and HTML pages always seem more recent and fresher to users. In our usability research on corporate websites and intranets, when participants encountered old PDFs, they lost trust and questioned the legitimacy of the corresponding information. In some cases, people spent additional time looking for a more recent version of the PDF to check the accuracy of the information. Audit your content and remove old or previous versions of PDFs. When versions are updated, check to make sure links point to the new version, not the old one. If for some reason an old PDF still needs to live on your site, clearly and legibly state what the most recent version is and where users can find it. Do this on the very first page and throughout the PDF. In addition to the date of the last update, include contact information where users can get help.

**10. Offer multiple formats, not just a PDF.** Give users a choice in how they consume your content; don’t just limit them to a PDF. Consider if users will appreciate also having an audio version to listen to, a version that’s specifically formatted for an ereader, or another format altogether that communicates the message while supporting the user’s task and context. Advances in technology have afforded improvements to ereaders, tablets, and mobile reading apps. These options have made reading on digital devices comfortable and convenient, whereas, in years past, this wasn’t always the case and printing was required. While PDFs can be read by most ereaders, offering *only* a PDF can make your experience seem inconsiderate and outdated.

![ACM offers multiple formats for their newsletter.](https://media.nngroup.com/media/editor/2020/05/16/acmformatsfornewsletter.png)

*The Association for Computing Machinery offered users the option to view their content as either an HTML page, a PDF, or with an ereader.*

## Updates in 2020: PDFs Still Causing Trouble

Recent studies for the fourth edition of our [intranet-guidelines report](https://www.nngroup.com/reports/topic/intranets/) and the third edition of our [corporate-website report](https://www.nngroup.com/reports/about-us-presenting-company-information/) once again found severe usability problems when users were dumped directly into PDF files for online reading. On intranets, employee handbooks, forms, and policies need to be broken down into focused web pages instead of being thrown online as a single blob in PDF format. On corporate websites, even though it’s good to be able to download and print out annual reports, financial information for online reading must be provided in simple formats that are easy to navigate.

In certain cases, including a downloadable PDF might be warranted. However, more often than not, people won’t need to print out the PDF, and the decision to house content in a PDF is based much less on critical thinking and user-centered evidence and more on the false pretenses of PDFs being faster to create and easier to control than web pages. In any case, PDF should never be used for on-screen reading. Don’t force your users to suffer and slog through PDFs!
