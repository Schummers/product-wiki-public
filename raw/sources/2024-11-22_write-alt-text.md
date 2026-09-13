---
title: "Alt Text: What to Write"
date: "2024-11-22"
url: "https://www.nngroup.com/articles/write-alt-text/"
author: "Emma Cionca, Tanner Kohler"
topics: [accessibility, writing-web]
type: article
---

Alt text, or alternative text, is a brief description added to images on a website, enabling screen readers to convey visual content to individuals with visual impairments. Well-crafted alt text is essential for ensuring web accessibility and usability. The best alt text takes into consideration the context of the image along with its purpose.

## In This Article:

- [Writing Good Alt Text (When It’s Needed)](#toc-writing-good-alt-text-when-its-needed-1)
- [3 Steps for Deciding What Your Alt Text Should Include](#toc-3-steps-for-deciding-what-your-alt-text-should-include-2)
- [Alt-Text Decision Tree](#toc-alt-text-decision-tree-3)
- [Decorative Images Don’t Need Alt Text](#toc-decorative-images-dont-need-alt-text-4)
- [Functional Images](#toc-functional-images-5)
- [Informative Images](#toc-informative-images-6)
- [AI Cannot Yet Write Alt Text on Its Own](#toc-ai-cannot-yet-write-alt-text-on-its-own-7)
- [Conclusion](#toc-conclusion-8)
- [Additional Resources](#toc-additional-resources-9)

## Writing Good Alt Text (When It’s Needed)

**If an image is essential for a task or for understanding page content, it needs alt text.** The following recommendations apply to every instance of alt text — regardless of the type of image it describes.

- **Keep it short.** Alt text shouldn’t be much longer than around 150 characters. Users can’t pause and resume the screen reader in the middle of alt text without going back to the beginning. People also can’t hold very much information in their [working memory](https://www.nngroup.com/articles/working-memory-external-memory/). Users will skip alt text if it doesn’t immediately seem like it will help them with their task.
- **Do not include words like ‘image’ or ‘photo’ at the beginning.** Screen readers already identify images as images when they encounter them because they are contained within the <img> HTML tag. Identifying an image as a certain type (e.g., infographic, chart, illustration) is appropriate if it will help the user understand the other alt text.
- **End alt text with a period,** even if it isn’t a full sentence. The period ensures that the screen reader pauses after reading the alt text.
- [Frontload](https://www.nngroup.com/articles/first-2-words-a-signal-for-scanning/)**alt text with the most important words,** to help users make a quick and informed decision about whether it’s worth listening to the rest of the alt text before moving on.
- **Always include an alt attribute**(alt=””), even if it will be empty. Otherwise, screen readers might announce the image file name.
- **Avoid technical jargon and abbreviations** unless users are certain to understand them.
- **Never reuse alt text** for the same image without reanalyzing the context in which the image is placed.
- **Mention identity only if it’s relevant.** If the race, ethnicity, gender, religion, or cultural identifiers of the people pictured aren’t part of the reason the image was included, don’t mention them.
- **Include alt text in**[each language that your page supports](https://www.nngroup.com/articles/international-b2b/)**.** Use a translation key to simplify your process.

## 3 Steps for Deciding What Your Alt Text Should Include

### Consider the Context

Read the page copy surrounding the image to understand its purpose. Look for any references to the image or explanations of the image — especially if image captions are present. (Struggling to understand context is one reason AI does not write good alt text on its own.)

**The context of an image and the author’s intention for including it determine what the alt text should say**, which is why the best alt text is created with input from those who write the content and choose the images. Alt text for the same image changes from context to context because different things will be relevant about the same image in different places.

The following example shows how the alt text for the same image changes based on its context.

![Screenshot of UT Austin homepage with UT logo in top-left corner.](https://media.nngroup.com/media/editor/2024/11/22/ut-austin-homepage.png)

*UT Austin homepage: The UT Austin logo in the top left corner links back to the homepage. The alt text should describe this function.***HTML:** alt="UT Austin home."

![Screenshot of UT Austin Brand Guidelines Page with large UT logo centered on page with explanation of logo below.](https://media.nngroup.com/media/editor/2024/11/22/ut-austin-brand-guidelines-page.png)

*UT Austin brand guidelines page: The same logo image is the focus of the page. The alt text should describe its components.***HTML:** alt= "The UT Austin logo featuring a shield adjacent to the word ‘Texas’ with the phrase ‘The University of Texas at Austin’ underneath."

### Identify the Intention

Write the basic idea(s) that the image conveys in the context of the surrounding page copy. Try answering the question “Why did the author include this image?”

### Trim the Text

Focus the alt text on the unique value that the image adds to the page. Reduce the alt text to state only that unique message to [avoid redundancy with other page copy](https://www.nngroup.com/articles/alt-text-usability/). (AI can be helpful for simplifying your writing at this stage.)

## Alt-Text Decision Tree

![Decorative images shouldn't have alt text. Functional images should communicate the action they afford. Informative images with long alt text should use a long description or alter the page copy.](https://media.nngroup.com/media/editor/2024/11/19/alt-text-link-tree-1-1.png)

## Decorative Images Don’t Need Alt Text

**An image is**[decorative](https://www.nngroup.com/videos/decorative-images/)**if users can complete all tasks and understand all information on the page without it.** Decorative images create a specific look and feel for sighted users but don’t convey information relevant for any tasks. Because of this, they’re superfluous and don’t merit screen-reader users’ time or attention, so the alt-text attribute should be empty so that the screen reader skips right over them.

The [W3C states](https://www.w3.org/WAI/tutorials/images/informative/) that: *“whether to treat an image as informative or decorative is a judgment that authors make, based on the reason for including the image on the page.”*

Decorative images often include:

- **Stock photos** used to enhance visual appeal
- **Hero** images
- **Icons** used for visual appeal
- **Ornamental** borders

Decorative images can also include page elements that use an image file, such as:

- **Headers**
- **Spacers** or dividers
- **Background** patterns
- Color or gradient **overlays**
- **Animations** or hover effects

![Screenshot of webpage featuring Sesame Street character, Elmo, alongside a description of his physical characteristics and personality.](https://media.nngroup.com/media/editor/2024/11/22/sesame-street.png)

*Sesame Street: This image of Elmo on a page introducing the characters of Sesame Street is lovely for sighted users, but its alt text (*“Elmo waves at us”*) is unnecessary. The image is decorative because it adds no additional information about Elmo that is not already described in the paragraph. Engaging with this image and determining whether it is relevant is a waste of screen-reader users’ time and attention.***HTML:** alt=""

![Screenshot of a ticket purchasing webpage featuring hero image of live concert performance in the background.](https://media.nngroup.com/media/editor/2024/11/22/rolling-loud.png)

*Rolling Loud: This hero image of a live performance homepage is decorative . The image is intended to create a certain aesthetic, not communicate information relevant to user tasks on this page. This image should have an empty alt attribute.***HTML:** alt=""

![Screenshot of webpage featuring an image of a white, antique-inspired frame surrounding invitation text.](https://media.nngroup.com/media/editor/2024/11/22/stanley.png)

*Stanley: This ornamental border around the page copy is decorative . Stanley is announcing a new line of beverage containers in collaboration with LoveShackFancy, a women's lifestyle brand. The purpose of this image is to be aesthetically coordinated with LoveShackFancy’s style, not convey task-related information on the page.***HTML:** alt=""

## Functional Images

Functional images enable users to take actions within an interface. Alt text for functional images should not describe the image; instead, it should [describe what will happen](https://www.nngroup.com/articles/information-scent/)**when the image is clicked or tapped**.

However, if an image is accompanied by words or a label that enables the same action when clicked, the image is considered redundant and does not merit alt text.

Functional images include:

- Linked images
- Images as buttons
- Icons
- QR codes
- Media controls
- Navigation elements
- Image maps

### Linked Images

![Screenshot of photography website featuring several images that link to different categories of images.](https://media.nngroup.com/media/editor/2024/11/22/rising-oak-galleries.png)

*Rising Oak Images: The image of a family on the Browse Galleries page is functional because it is linked to a gallery of family photos. Screen-readers automatically announce links when they come across them, therefore alt text is required to identify where the link will lead.***HTML:** alt= "Families."

### Buttons

![Screenshot of mobile application for booking a flu shot featuring a button labeled, 'Book your flu shot today' with an embedded image.](https://media.nngroup.com/media/editor/2024/11/22/cvs.png)

*CVS: This image and the text below both lead to the flu-shot booking page when clicked. The text is coded as a button, which the screen reader announces as “Book your flu shot today. Button.” The image correctly has no alt text because it is redundant and decorative.***HTML:** alt= ""

### Icons

![Screenshot of CA.gov homepage with house icon in top left corner and gear icon labeled 'settings' in top right corner.](https://media.nngroup.com/media/editor/2024/11/22/cagov.png)

*CA.gov: The house icon in the top left corner is a functional image that links to the homepage.***HTML:** alt=”California.gov home.”*The gear icon in the top right corner links to the Settings page. Because it is accompanied by the label Settings, this icon is redundant and does not require alt text.***HTML:** alt=""

![Screenshot of a Google Document toolbar highlighting the printer icon.](https://media.nngroup.com/media/editor/2024/11/22/google-docs.png)

*Google Docs: The print icon is a functional image because it initiates the printing process. Thus, its alt text should indicate the action it affords.***HTML:** alt= "Print."*(Note that Google includes the keyboard command [⌘P] in the alt text to help users learn that there is a more efficient way to take the same action.)*

## Informative Images

Informative images add task-related information beyond the contents of the surrounding page copy. If they visualize information that is already communicated elsewhere in writing, these images are considered redundant and will benefit from [a deeper analysis into whether they actually require alt text](https://www.nngroup.com/articles/alt-text-usability/).

For example, a graph showing a full data set accompanying a written analysis of that data is informative. Informative images don't serve a functional purpose. Alt text for informative images should highlight the unique value they contribute to the page and avoid redundantly restating things already communicated elsewhere. Alt text for informative images tends to be the most difficult to write.

Informative images can be simple or complex, depending on how easy it is to textually describe the information conveyed by the image.

### Simple Informative Images

An informative image is considered **simple when its main message can be summarized in one sentence** that fits within about 150 characters.

Simple informative images often include:

- Photographs
- Illustrations
- Simple graphs
- Graphic-based logos
- Animations
- Simple graphics
- Paintings
- Sketches
- Simple renderings
- Pictograms
- Silhouettes

While some images, such as graphs and charts, seem complicated at first glance, their main point is often simple.

For example, a line graph might contain hundreds of data points, yet its main message might be the simple correlation between the two variables, which can be succinctly described in one sentence.

![Screenshot of a webpage explaining a sample nutrition facts label, highlighting the four sections of the label.](https://media.nngroup.com/media/editor/2024/11/22/nutrition-facts.png)

*FDA: This graphic is a simple informative image : it communicates that a nutrition label has four sections and explains what those sections are. While there is a lot of information in the image, most of it is irrelevant to the purpose of this particular image and is explored in detail later on. One sentence of alt text as a summary would likely suffice in this case (with the option of including more detail in a hidden table as part of a long description).***HTML:** alt= "Nutrition labels have four sections: serving information, calories, nutrients, and percentage of daily values, for which 5% or less is low, 20% or more is high."

![Screenshot of an article about 'soft' interview rooms featuring an image that shows the room in more detail than the body of the article describes.](https://media.nngroup.com/media/editor/2024/11/22/news-article.png)

*Live 5 News WCSC: This photo is a simple informative image — its main purpose is to illustrate what a ‘soft room’ is like. The image is highly relevant to the page content, so the alt text should emphasize the sentiment of security and comfort within the room conveyed by the photo. Notice how the emotions communicated by the image are not communicated in the page copy.***HTML:** alt= "A small, inviting room with warm lighting, several cushioned chairs arranged to facilitate discussion, blankets, and calming photos on the walls."

**Simple informative images may include text.** If the text is short enough to fit with about 150 characters and is an important part of the image's message, include the exact words in the alt text. Otherwise, including the exact text isn’t necessary.

![Screenshot of a product page for a royal blue t-shirt with the phrase 'Golden State Warriors.'](https://media.nngroup.com/media/editor/2024/11/22/warriors_small.png)

*Warriors Shop: This product image is a simple informative one. The phrase Golden State Warriors, shown in this image, is not mentioned anywhere in the product details or description. The alt text describing this image should include the words on the t-shirt.***HTML:** alt= "Royal blue t-shirt with bold yellow text saying, ‘Golden State Warriors’."

### Complex Informative Images

An informative image is **complex** when:

- Its message cannot be summarized in 150 characters, and
- A structured description could convey its meaning better.

This is often the case for intricate visuals that communicate more than one point.

Complex informative images often include:

- Charts
- Graphs
- Figures
- Diagrams
- Maps
- Infographics
- Tables
- Flowcharts
- Blueprints
- X-rays
- Heatmaps
- Schematics
- Histograms
- Mind maps
- Collages
- Timelines
- Pie charts
- Venn diagrams
- Gantt charts
- Nutrition labels
- Screenshots (which turn page copy into an image)

Make complex informative images more accessible **by altering the page copy surrounding the image.** Editing the page copy to communicate the image’s message often makes the visual itself redundant. In many cases, this could be as simple as including a list or table within the HTML of the page.

If the page’s body copy cannot be altered, consider adding a caption right above or below the image. Richer page copy can also benefit users with low vision, learning disabilities, or lack of subject-matter expertise, but must be balanced with [brevity](https://www.nngroup.com/articles/rewriting-content-brevity/).

![Screenshot of webpage featuring a graphic of six fire safety tips.](https://media.nngroup.com/media/editor/2024/11/22/fire-safety.png)

*USA Fire Protection: The graphic on this page illustrates six fire-safety tips. It is a complex informative image because including all the tips in alt text would certainly exceed 150 characters. The simplest method for making this image more accessible is to present the information from the graphic as a list or table in the page copy. This method would make the image redundant and remove the need for alt text altogether.***HTML:** alt=""

**For unalterable page content, provide expanded alt text in a long description.** Long descriptions house more detailed information than is reasonable to stuff into traditional alt text. They can include longer paragraphs of text, lists, or tables.

A long description is text that is present in the HTML but invisible to people who do not use a screen reader. It can live on the same page as the image, ideally next to it, or on a separate page, linked to from an invisible link next to the image. If the description is located on a separate page, it can be made visible or invisible, depending on the HTML and the preferences of the designer.

![Screenshot of webpage featuring a graphic comparing data for 5 different rockets.](https://media.nngroup.com/media/editor/2024/11/22/first-engine-stage.png)

*Everyday Astronaut: This diagram compares engine cycle data points for several rocket models. Since this image requires alt text, the entire dataset can be included in a long description as a table that provides all relevant information and makes it easier for screen-reader users to navigate through it.***HTML:** alt= ”Engine cycle data for the Atlas V, Delta IV Heavy, Vulcan, Falcon 9, and Falcon Heavy.”

The following table is the HMTL version of the prior image that would live in the long description. | Atlas V | Delta IV Heavy | Vulcan | Falcon 9 | Falcon Heavy | Engine | 1 x RD-180 | 3 x RS-68A | 2 x BE-4 | 9 x Merlin 10 | 27 x Merlin 10 | Cycle Type | OX Rich Closed Cycle | Open Cycle | OX Rich Closed Cycle | Open Cycle | Open Cycle | Propellant | KeroLOX | HydroLOX | MethaLOX | KeroLOX | KeroLOX

However, linking to long descriptions in other locations increases the [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) of accessing the alt text compared to presenting the analysis in the body text for all users.

## AI Cannot Yet Write Alt Text on Its Own

At the time of writing, Artificial Intelligence (AI) tools still struggle to reliably write good alt text that communicates the intention behind images and accommodates their context.

**Use AI to refine alt text rather than relying on AI to write it** from scratch — particularly when using [LLM chatbots like ChatGPT](https://www.nngroup.com/articles/artificial-intelligence-glossary/). One critical step in writing useful alt text is to **identify the intention** behind including the image.

AI cannot read the mind of the author; it can only describe what it “sees.” When given strict parameters and adequate context, it might generate something decent for **redundant** or **simple informative** images. But it will struggle to produce accurate alt text for **functional** images because it may have difficulty interacting with interfaces and might not have a real understanding of what each interface element does.

When it comes to alt text for **complex informative** images, AI tends to write too much.

We hope that future accessibility software will leverage AI to efficiently aid in laborious accessibility work, but we are not there yet. Even AI-infused [accessibility widgets are not yet up to the task](https://www.nngroup.com/videos/accessibility-widget/) and can cause more harm than good.

Wrangling AI to write alt text is often more time-consuming than doing it yourself. However, if you are set on using an AI chatbot to help, **the results should be reviewed by those who understand the intentions behind images**. Your prompts should include the following parameters (which can also be used to evaluate the bot’s output):

- A character limit (~150) (However, remember that concise writing is not the same as useful alt text.)
- Context for the image (whether in writing or a screenshot that shows the image in the context of the larger page)
- A reminder to describe the message of the image, not describe what it looks like
- A focus on what the image uniquely contributes to the page to avoid redundancy

We tested AI’s alt text writing ability by inputting a screenshot from an Everyday Astronaut webpage alongside a prompt.

![Screenshot of webpage with a diagram comparing the dimensions of 5 rocket models, surrounded by page copy summarizing the diagram.](https://media.nngroup.com/media/editor/2024/11/22/ai-example-version-b.png)

*AI prompt example:*"Write alt text for the infographic on this page comparing the dimensions of 5 rockets. Keep the alt text to ~150 characters and describe the main message the image communicates rather than describing the information it displays. Avoid redundancy with information already communicated by the surrounding page copy."

We provided several popular LLM chatbots with the above information and the results were largely lackluster. Important details were often omitted for the sake of concision, and the chatbots misidentified key aspects of the image. While the AI-generated alt text was usable after some editing, it took more time and effort to hold its hand than to write it ourselves.

## Conclusion

Always make sure the alt text in your HTML code functions properly by testing prior to publishing. There are many testing tools available online, like this [browser extension](https://wave.webaim.org/extension/) from the Institute for Disability Research, Policy & Practice at Utah State University, which allows you to test for accessibility issues directly in your browser. Ideally, [a person with low or no vision will test your](https://www.nngroup.com/articles/mobile-accessibility-research/)[site](https://www.nngroup.com/articles/mobile-accessibility-research/) prior to publishing, and report on the issues that they come up with.

As with anything, writing good alt text takes practice. Always evaluate your alt text before implementing it and remember that your main driver should be meeting the user’s goal. Don’t recreate visual experiences — help your users efficiently obtain necessary information.

## Additional Resources

There are many fantastic resources available to help create good alt text. Two of our favorites include:

**W3C Web-Accessibility Initiative (WAI)**

- [Images Tutorial](https://www.w3.org/WAI/tutorials/images/)
- [Alt-Text Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/)

**WebAIM: Web Accessibility In Mind**

- [Alternative Text Guide](http://webaim.org/techniques/alttext/)
