---
title: "Proximity Principle in Visual Design"
date: "2020-08-02"
url: "https://www.nngroup.com/articles/gestalt-proximity/"
author: "Aurora Harley"
topics: [psychology-and-ux, visual-design]
type: article
---

Gestalt principles were discovered in the first half of the 20th century by Gestalt psychologists, who were trying to make sense of how people visually perceive the world — specifically, how people decide whether certain elements are part of the same group or not. These principles include proximity, similarity, and closure — which are all important in the visual design of digital interfaces. Later, more grouping principles (such as [common region](https://www.nngroup.com/articles/common-region/)) were added to the original Gestalt list.

UI design heavily relies on proximity and other grouping principles, as correctly interpreting which elements are related is critical to successfully interacting with the interface.

> **Principle of proximity:** Items close together are likely to be perceived as part of the same group — sharing similar functionality or traits.

## In This Article:

- [Place Related Elements near Each Other](#toc-place-related-elements-near-each-other-1)
- [Far-Away Elements Appear Unrelated, Are Easily Overlooked](#toc-far-away-elements-appear-unrelated-are-easily-overlooked-2)
- [Proximity May Shift in Responsive Designs](#toc-proximity-may-shift-in-responsive-designs-3)
- [Conclusion](#toc-conclusion-4)

## Place Related Elements near Each Other

Proximity is one of the most important grouping principles and can overpower competing visual cues such as similarity of color or shape. The practice of **placing related elements close together** and **separating unrelated elements** can be seen almost everywhere in UI design.

![Graphic showing a 5-by-3 grid of a mix of dots and triangles, with whitespace after the third column to create the perception of 2 separate groups.](https://media.nngroup.com/media/editor/2020/07/02/proximity-withdifferentshapes.png)

*Whitespace separates the shapes into two distinct grouping through the principle of proximity. Even when including differing shapes within each group, these two groupings are still clear.*

Using **varying amounts of whitespace to either unite or separate elements** is key to communicating meaningful groupings. For example, in the header area of the Wellington City Council website, the *Search* function is located on the same line as the main navigation of the site when viewed on a large screen. However, the extra whitespace between the main navigation and *Search* indicates that they belong to separate groups and thus have distinctive functionalities. This whitespace is critical for making the *Search* function stand out from the rest of the main menu.

![Screenshot of the Wellington City Council website as seen on a desktop web browser.](https://media.nngroup.com/media/editor/2020/07/02/proximity_whitespaceseparatingsearch-wellingtondesktop.png)

*Wellington City Council website, as seen on a desktop monitor: Extra whitespace to the left of the* Search *button separates it from the rest of the main navigation and identifies it as a different type of functionality, even though it shares the same font treatment with the main categories in the navigation menu.*

On smaller screens, however, maintaining this spacing is not possible. To avoid these areas from being perceived as a single group, the *Search* is shifted up, away from the main navigation altogether. (Yes, other aspects of this design could be further improved, such as grouping the *Search* label and the corresponding icon using either proximity or common region.)

![Screenshot of the Wellington City Council website as seen on a tablet.](https://media.nngroup.com/media/editor/2020/07/02/proximity_placementseparatingsearch-wellingtontablet.png)

*On tablet, there is not enough screen space available to maintain this separation, and so, to avoid having the* Search *appear to be part of the main navigation, it was shifted up, grouped with other utility-menu items.*

Leveraging proximity to create meaningful groups is reflected even when presenting basic text content: sentences are grouped together in paragraphs separated above and below by whitespace. Further, whitespace around well-designed headings signals which paragraphs they are associated with — the text from the corresponding section is usually placed closer to the heading than the text from the preceding section.

![Screenshot of text content (1 headline with a paragraph of text followed by a sub-heading and 2 short paragraphs), and a graphic showing this same layout where the text is covered with gray boxes.](https://media.nngroup.com/media/editor/2020/07/02/proximity_textparagraphgroupings.png)

*(Left) Proximity defines groups of related text (paragraphs and sections) and helps scanning. (Right) These groupings are discernible even without viewing the actual text.*

[Chunking](https://www.nngroup.com/articles/chunking/) applies to [form design](https://www.nngroup.com/articles/form-design-white-space/) as well: when related fields appear grouped together, the form seems easier to scan and less daunting to complete. For example, a single form with 12 fields may appear too taxing to fill out, while a 3-chunk form with 4 fields each seems simple in comparison. (The principle of proximity is applied in many ways in good form design. For instance, a minimal amount of spacing between a top-aligned label and its corresponding form field makes that relationship apparent compared to a larger margin before the next label-field pair.)

![2 graphics mocking up a form: 1 with a single large grouping of form fields, versus grouping the fields into 3 sections.](https://media.nngroup.com/media/editor/2020/07/02/form-whitespacegroupings.png)

*12 form fields in one large group (left) appear more daunting than the same number of fields broken out into three groupings (right). (Obviously assuming that the groups are meaningful — for example, shipping information in one group and billing information in another.)*

On the other hand, **grouping together unrelated elements may camouflage them** from users. For example, on the California EDD website, the *Add* button to list employer information required for a form is buried among the unrelated buttons to move to the *Next* step of the process, *Save as Draft*, and *Cancel*. When looking around the page, users may **only look at one item within a perceived grouping and use that to make a judgement about what the other items in that group must be**. (In contrast, *Previous* and *Next* are related, so grouping them would have increased usability.)

![Screenshot of step 3 within the CA EDD claim form.](https://media.nngroup.com/media/editor/2020/07/02/proximity_addbuttonhiddeninunrelatedgrouping_eddform.png)

*CA.gov: The* Add *button was placed in close proximity to unrelated buttons, far from the main area of the form, which made it difficult to find.*

## Far-Away Elements Appear Unrelated, Are Easily Overlooked

When users completely miss a link, button, or piece of information even though it’s right in front of them, proximity (or rather, the lack of it) is often to blame. Because elements separated by whitespace are perceived as being less related, [far-away items](https://www.nngroup.com/articles/closeness-of-actions-and-objects-gui/) can be easily overlooked by [task-focused users](https://www.nngroup.com/articles/eyetracking-tasks-efficient-scanning/) who expect all relevant information and interactive elements to be placed close together. This behavior is sometimes described as “[tunnel vision](https://www.nngroup.com/articles/tunnel-vision-and-selective-attention/):” users selectively attend to certain areas of the screen as they complete their task and miss things “in plain sight” because they are outside this focal area.

For instance, in our mobile-usability studies, participants often get frustrated when apps require them to create an account before gaining access to content. However, in many of these designs, the account creation can be skipped — this option is simply hard to find because it is placed in a top corner of the page, far from the main calls to action.

![Screenshot of the sign-in screen of the Kayak mobile app](https://media.nngroup.com/media/editor/2020/07/02/skipbuttonfarfromsigninoptions-kayakmobileapp.png)

*Kayak mobile app: The* Skip *link is presented in the top left corner of the screen, far away from the main content and the most prominent calls to action. This placement makes it easy to overlook and tricks users into thinking they must sign in.*

Similarly, the Hulu app on an Apple TV presents instructions for how to interact with the current screen’s content all the way in the lower-right corner of the screen, far from the relevant content. Moreover, the [text is obscured by the photo](https://www.nngroup.com/articles/text-over-images/) background for the selected show. This lack of proximity led my husband to believe there was no way to access the *Details* screen (where the other episodes in the season were listed) — luckily, he had me there to correct him!

![Photograph of the Hulu Apple TV app.](https://media.nngroup.com/media/editor/2020/07/02/huluappletv-instructionsinlowrightcorner.jpg)

*Hulu on Apple TV: Instructions to* Click and Hold: *(for)* Details *are presented in the lower right corner of the screen, far from the information about the next episode to watch. Especially on a large TV screen, this placement makes it hard to notice.*

## Proximity May Shift in Responsive Designs

Paying attention to the proximity of elements is particularly important when designing responsive layouts, as these **groupings may change as they adapt to varying screen sizes**. Scaling down to smaller devices can minimize the space between elements or can push elements farther apart, destroying grouping relationships.

For instance, on the Transport for London Driving page on desktop, links to information about the *Ultra Low Emission Zone* and the *Low Emission Zone* appear side by side, in two different columns. Presenting these two links in close proximity allows users to easily see and compare them to decide which they want to click on. However, on small screens, these links appear far apart because the two columns are stacked one above the other, rather than side by side. This unfortunate placement can cause mobile users to never discover the second type of emission zone.

![Screenshots of the Transport for London Driving page as seen on a desktop screen and a mobile device.](https://media.nngroup.com/media/editor/2020/07/02/proximity-drivinguk_desktopvsmobile.png)

*Transport for London: Information about two types of low-emission zones appear in close proximity on a large screen (left). On a mobile device (right), the sections corresponding to the two zones were far apart due to how columns were stacked in the responsive layout.*

## Conclusion

Placing related elements in close proximity and using whitespace to create meaningful groups is a foundational principle in visual design. Users are task-focused and may scan pages quite quickly, so making these groupings visually obvious increases usability by helping users quickly find and focus only on those UI elements that are most related to their current task.
