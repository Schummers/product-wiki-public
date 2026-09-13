---
title: "Alt Text: Not Always Needed"
date: "2024-11-15"
url: "https://www.nngroup.com/articles/alt-text-usability/"
author: "Emma Cionca, Tanner Kohler"
topics: [accessibility, writing-web]
type: article
---

Alt text (or alternative text) is metadata intended to help screen-reader users understand what an image is depicting. Most [guidance for writing alt text](https://www.nngroup.com/articles/write-alt-text/) describes how to make individual web-based images **accessible** and **understandable** for all users. This is more complicated than it sounds because users encounter alt text while trying to accomplish more complex tasks that generally involve interacting with many elements on the page. Images are just part of the picture.

## In This Article:

- [What Users Need from Alt Text](#toc-what-users-need-from-alt-text-1)
- [Quit Describing What Images Look Like](#toc-quit-describing-what-images-look-like-2)
- [Alt Text Is Not the Only Key to Webpage Accessibility](#toc-alt-text-is-not-the-only-key-to-webpage-accessibility-3)
- [Does an Image Require Alt Text?](#toc-does-an-image-require-alt-text-4)
- [What About Users with Low Vision?](#toc-what-about-users-with-low-vision-5)
- [Conclusion](#toc-conclusion-6)
- [Additional Resources](#toc-additional-resources-7)

## What Users Need from Alt Text

Assistive-technology users obviously want individual page elements to be accessible, but ****(just like anyone else)** what they want most is an **[easy path](https://www.nngroup.com/videos/make-it-easy-ux-slogan-8/)** to accomplish **[basic tasks](https://www.nngroup.com/videos/top-tasks-ux-design/)**.** Accessibility is a means to the end of whatever the user needs to accomplish.

Even if every image has “perfect” alt text, our job isn’t done until assistive-technology users can do what they came to do. That is [the argument we’ve been making for nearly 20 years](https://www.nngroup.com/articles/accessibility-is-not-enough/): the focus must be [usability](https://www.nngroup.com/articles/usability-101-introduction-to-usability/) — not just accessibility.

## Quit Describing What Images Look Like

When writing alt text, it’s easy to find yourself thinking:

*“This image is really helpful for me … how can I help someone who couldn’t see this image accurately imagine it?*

*I’ll describe it in the alt text so screen-reader users can imagine what they aren’t seeing.”*

**Screen-reader users navigate digital devices differently**— they do not rely on visual information, which means they are not interested in designers’ attempts to recreate visual experiences for them.

**Consider the accessibility and usability of the entire page — not just of individual images.** Eyetracking research shows that sighted users often [pay significant attention to images](https://www.nngroup.com/articles/photos-as-web-content/), especially when they are [related to their current task](https://www.nngroup.com/articles/eyetracking-tasks-efficient-scanning/). However, for screen-reader users, image alt text does not play the same role. They begin by figuring out the structure of the page and working through it sequentially.

For example, here’s how a screen-reader user might approach a [product page](https://www.nngroup.com/articles/ecommerce-product-pages/):

1. Jump between the page headers to get a sense of the page structure.
2. Explore the details of a specific section with the heading label *Product Description.*
3. Encounter an image and wonder “**What information that I might have missed elsewhere does this image communicate about the product?**”

Most of the time, screen-reader users don’t wonder what images look like. Instead, they want to know their purpose. (Exceptions to this rule might include websites presenting images, such as artwork, purely for visual enjoyment, or users who could previously see and have lost their sight).

When alt text is useless for completing common tasks, images bring confusion, not clarity.

![Screenshot of Target webpage advertising Halloween products featuring a decorative cartoon bat.](https://media.nngroup.com/media/editor/2024/11/22/targetbat-1.png)

*Target: The cartoon of a bat alongside the text advertising Halloween products is not useful for completing common tasks.*

## Alt Text Is Not the Only Key to Webpage Accessibility

**If screen-reader users can skip interacting with images, they will.** Adding alt text to every image does not automatically make webpage content easy to navigate and consume. **Quality page copy is often the key** to making web content easy to understand — alt text supplements page copy as needed. Alt text is **most valuable when it contributes task-related information that isn’t redundant with other page copy**(with a few exceptions). Restating information found elsewhere on the page and descriptions of decorative visuals can be a waste of screen-reader users’ time and attention.

## Does an Image Require Alt Text?

Images that visualize information that is already communicated elsewhere in writing are **redundant**. Redundant visuals are powerful for sighted users because [visual information is easy to understand and remember](https://www.nngroup.com/articles/picture-superiority-effect/).

However, alt text describing redundant images can be unnecessary for users who can’t see the image because every page element demands equal attention from screen-reader users to determine if it’s useful for their task. They can’t rely on [visual hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/) or other [Gestalt principles](https://www.nngroup.com/videos/the-gestalt-principles-intro/) to skim over what doesn't seem useful.

This means that **tools that promise to automatically generate alt text for all images are not making things easier for users** — they might be adding unnecessary [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) (not to mention how bad automatically generated alt text can be). To decide whether a redundant image needs alt text, answer the following three questions in order:

![Images that repeat page content, aren't referenced by page copy, and don't increase efficiency might not need alt text. (this one is included based on the efficiency it offers by summarizing many points that follow)](https://media.nngroup.com/media/editor/2024/12/19/alt-text-not-needed_poster.png)

### 1. Repetitive?

**Is the task-related information in the image also found elsewhere on the page?**

If not, then the image is not redundant and requires alt text. (Alternatively, you could modify the page copy or other elements to include the information contained in the image.)

If yes, then the image is likely redundant. To decide whether alt text is needed, proceed to question 2 (*Referential?)*.

![A screenshot of a tree being planted that visually depicts what the page copy surrounding it describes.](https://media.nngroup.com/media/editor/2024/11/22/planting-1.png)

*Repetitive (no alt text required) Growingagreenerworld.com: The caption for this image describes exactly what the image communicates. Therefore, any alt text for the image will be redundant and a waste of time for screen-reader users. In this case, the actual alt text was the same as the caption. Coming across the same information twice in a row feels even more confusing and unnecessary.***HTML:** alt=""

![A screenshot of a table-setting diagram that contains more information than what is described in the surrounding page copy.](https://media.nngroup.com/media/editor/2024/11/22/table-setting-1.png)

*Not repetitive (alt text required)**Emilypost.com: This image communicates both the typical elements of a table setting and their proper placement. Because none of this information is described elsewhere on the page, this image requires alt text — most likely a long description that lists each element and its correct placement in an ordered list. We would suggest something like the following alt text, with a full description below that is visually hidden.***HTML:** alt= "Typical elements of a table setting and their proper placement."*(See additional long description below)*

*The following is an example of what could be an invisible full description (i.e., long description) of the prior image:*

1. *Bread plate and butter knife, located in the top left corner.*
2. *Dessert fork, placed horizontally at the top center.*
3. *Dessert spoon, placed horizontally at the top center, below the dessert fork.*
4. *Water glass/goblet, located in the top right corner.*
5. *Wineglass, located in the top right corner, slightly below and to the right of the water glass/goblet.*
6. *Napkin, located in the bottom left.*
7. *Salad and appetizer fork, located in the bottom left to the right of the napkin.*
8. *Entree fork, located in the bottom left, to the right of the salad and appetizer fork.*
9. *Entree knife, located in the bottom right.*
10. *Salad and appetizer knife, located in the bottom left, to the left of the entree knife.*

### 2. Referential?

**Does the page copy directly reference the image?**

References may be signaled by phrases such as *“as you can see in this image”* or “*the image below.”*

If yes, the page does directly reference the image, then it’s important to provide alt text so screen-reader users can find the image and won’t feel they’ve missed something that sighted users can access.

If no, proceed to question 3 (*Efficient?*).

![A screenshot of two pages of a Harry Potter ebook containing text and an illustration of Albus Dumbledore.](https://media.nngroup.com/media/editor/2024/11/22/harry-potter.png)

**Image not referenced (no alt text required)***Kindle: This illustration shows the reader what the character Albus Dumbledore looks like. However, alt text for this image would be redundant for screen-reader users since the author describes Dumbledore’s appearance in great detail in the written text, and the image is not referenced in the page copy.***HTML:** alt=””

![A screenshot of a United States map color-coded to represent the four categories of climate zones referenced throughout the surrounding page copy.](https://media.nngroup.com/media/editor/2024/11/22/climate-map-1.png)

*Image referenced (alt text required) Energy.gov: The page copy surrounding the image references it in two places, saying:* “The map below shows the four broadest categories of climate zones…” *and “* See the map to find your climatic region.” *The easiest way to make this image accessible would be to include a table in the page copy summarizing the main information (see below). Unfortunately, the page makes no such effort.***HTML:** alt=””*(Note the essential addition of the following table to the page copy which communicates the same message)*

Climate Zone | States (Alphabetical Order) | Cool | AZ, CO, CT, ID, IL, IN, IO, KS, MA, ME, MI, MN, MO, MT, ND, NE, NH, NM, NV, NY, OH, OR, PA, RI, SD, UT, VT, WA, WI, WV, WY | Hot-Arid | AZ, CA, CO, NM, TX | Hot-Humid | AL, FL, GA, LA, MS, SC, TX | Temperate | AL, AR, CA, DE, GA, KY, MD, MS, NC, NJ, OK, OR, SC, TN, VA, WA

Alt text for images referenced in page copy is also relevant for sighted users who might be confused or frustrated if they can’t see an image because it isn’t loading properly (particularly when images are far removed from references). In general, consider minimizing references to images in page copy, so, users do not over rely on them to understand webpage copy.

### 3. Efficient?

**Could alt text help users more efficiently complete a task?**

For example, alt text for a product image may summarize the product details distributed throughout a long and complex page, thus helping users quickly review all relevant product information. This approach reduces the load on users’ [working memory](https://www.nngroup.com/articles/working-memory-external-memory/) — when information is scattered across a lengthy page, a concise summary in the alt text can remind users of key points mentioned earlier.

If alt text can make a task more efficient, then it should highlight the information that would best help users efficiently accomplish a common task.

If it doesn’t, then the image is truly redundant, and the alt attribute should be empty.

Alt text that makes users more efficient is often redundant. **Include redundant alt text for the sake of efficiency only if it will help with users’ most frequent tasks and use cases.** Do not forget that redundant alt text generally slows screen-reader users down.****

![A screenshot of page copy that summarizes all the information contained in an accompanying rocket data image.](https://media.nngroup.com/media/editor/2024/11/22/payload-1.png)

*No added efficiency (no alt text required) Everyday Astronaut: This diagram compares the payload volume of several rocket models. The page copy above the image concisely summarizes all the task-related information. Providing alt text wouldn’t help users understand more efficiently how the payload volumes compare.***HTML:** alt=””

![Screenshot of amazon product page for dumbbells accompanied by product details.](https://media.nngroup.com/media/editor/2024/11/22/amazon-1.png)

*Added efficiency (alt text recommended) Amazon: This product image of dumbbells is redundant because it is accompanied by a detailed product description that outlines all the details communicated by the image. However, because the product details are distributed throughout the page, a summary in the alt text of the image could help users efficiently determine whether this product meets their needs.***HTML:** alt= ”Pair of Amazon Basics neoprene coated navy blue 10-pound dumbbells.”

## What About Users with Low Vision?

Some argue that even redundant images should all have alt text because users with *some* vision will struggle to see the images. Low vision includes trouble with:

- Visual acuity (clarity)
- Light sensitivity (e.g., photophobia)
- Contrast sensitivity (e.g., cataracts or macular degeneration)
- Field of vision (e.g., central- or peripheral-vision loss)
- Color vision (color blindness)

However, learning to use a screen reader is difficult, and using it can be frustrating. Many users with low vision don’t use assistive technology and prefer not to use it if they can avoid it. It's also common that alt text displayed on the screen in place of an image that is struggling to load is small, and difficult to see. This means that whether these users are relying on a screen reader or not, alt text doesn't offer them much help. These users benefit more from meaningful, large-font image captions and informative page copy than from alt text.

**If alt text is written for redundant images, it should prioritize screen-reader users.**

## Conclusion

While alt text is a crucial tool for making the web more accessible, it’s essential to consider the broader context in which users engage with content. Alt text for redundant images is most helpful when the page text directly references the image or when it enables users to complete tasks more efficiently.

## Additional Resources

There are many fantastic resources available to help create good alt text. Two of our favorites include:

**W3C Web-Accessibility Initiative (WAI)**

- [Images Tutorial](https://www.w3.org/WAI/tutorials/images/)
- [Alt-Text Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/)

**WebAIM: Web Accessibility In Mind**

- [Alternative Text Guide](http://webaim.org/techniques/alttext/)
