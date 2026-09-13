---
title: "Use Good Prototype Specifications to Empower Team Collaboration"
date: "2022-06-05"
url: "https://www.nngroup.com/articles/prototype-specifications/"
author: "Feifei Liu, Leeloo Tang"
topics: [interaction-design, prototyping]
type: article
---

## In This Article:

- [Introduction](#toc-introduction-1)
- [Are Prototype Specifications a Must?](#toc-are-prototype-specifications-a-must-2)
- [Conclusion](#toc-conclusion-3)

## Introduction

After delivering prototypes or wireframes, UX designers often face clarification questions such as:

- "What happens when a user clicks or hovers over an element?"
- "Under what conditions does a page element shows as active or inactive?"
- "What should this hidden content look like?"
- "Is there a maximum width on this field?"

Fortunately, most designers probably have already figured out the answers to these questions during the design. But if different people on their team ask the same questions or if team members forget the response after a while, they will have to explain the same idea repeatedly — an inefficient and frustrating experience.

Delivering prototypes and wireframes **along with prototype specifications** is probably the most proactive and practical approach to address such issues.

**Prototype specifications**, also called *prototype redlines* or *prototype annotations*, are a few lines of text written next to a prototype and describing details that may be ambiguous in the design. Such details may include font size, line spacing, click effects, and active or inactive conditions of UI elements. They are often used to help developers, product managers, or clients to understand the prototypes during delivery.

Using prototype specifications has several benefits:

- **It removes uncertainty about how the design works and improves communication efficiency.** Accurate prototype specifications represent the designers’ ideas with clarity and integrity and result in fewer team meetings and less communication cost –– a vast improvement in efficiency, especially for remote teams.
- **Team members don’t have to remember the original design ideas.** For design projects that unfold over a long time, people may forget the original concept of the prototype or new team members may be added to the team. Well-documented prototype specifications are a record of the original idea and serve as a source of [external memory](https://www.nngroup.com/articles/working-memory-external-memory/) for the team.
- **Prototype specifications help to standardize the team’s designs.** Prototype specifications can serve as a reference for future designs involving the same type of UI element or page, thereby helping to standardize the team's design. They can be further adopted into a team’s [design system](https://www.nngroup.com/articles/design-systems-101/).

It should be noted that other design-related artefacts may also involve annotations. For example, during ideation, a designer or product manager may annotate the sketch with possible opportunities and other features that could be considered. But these kinds of annotations are beyond the scope of this article. Specifications discussed in this article are all explanatory text written for the prototype-delivery phase.

### Different Types of Prototype Specifications

Recently, we conducted an international study with UX professionals. One primary goal was to learn about their day-to-day work. Based on this study, we identified three common types of prototype specifications: **element specifications**, **functionality specifications**, and **content specifications**.

#### Element Specifications

Element specifications refer to the basic attributes of text, images, interactive components, and other elements. Examples include font type, element size, color, alignment, spacing, and so on. This type of specification focuses more on how the element looks. Although simple and basic, element specifications are indispensable in the development process. Many prototyping tools (including Figma, Axure, Zeplin, Avocode, etc.) can automatically generate such element specifications, saving designers a tremendous amount of work.

*Figma can display basic information about individual elements in a prototype. Clicking on a specific component will show its width, height, spacing, font, size, color in the right panel. Source: Figma tutorial: Handoff seamlessly to developers*

#### Functionality Specifications and Content Specifications

**Functionality specifications** explain the feature’s behavior: what happens if users press the button, what changes on the screen if users make a different selection, when would a certain button be enabled or disabled. In other words, this type of specifications focuses on how the interface and system should work, not just on how it should look. Commonly, developers or clients need explanations of functionality in designs, so functionality specifications might be the first specification type that comes to designers' minds when the term "prototype specification" or "prototype annotation" is mentioned.

For instance, a UX designer working on a data-visualization page might need to annotate how the view of a pie chart would change when users hover over it or click a part of it.

**Functionality specifications might include information such as:**

- **How interactive elements or animations work**. Especially when a component requires complicated interaction and was rarely used in previous designs, detailed specifications help developers understand what to do and how to implement the right behavior.
- **Constraints of UI elements**, like the maximum number of characters in an input field, and what would happen if the constraints were violated
- **Different states of UI components**. For instance, the *Add to Cart* button may become inactive when an item is out of stock.
- **The user flow for complex interactions.** This can be combined with showing different states of a UI component to tell the full story. For example, specifications can annotate different states of the profile page before and after a user logs in, together with the whole flow of the login process.

**Content specifications** are explanations related to text content that may have been left blank in the prototype. While functionality specifications are mainly meant for developers and clients, the content specifications are intended for copywriters and visual designers.

For example, a UX designer working on an ecommerce app might leave some room for promotional copy when designing specific pages for a holiday event.

**Content specifications might include information as follows:**

- **Messages**, like [contextual tips](https://www.nngroup.com/articles/help-and-documentation/) or [error messages,](https://www.nngroup.com/articles/error-message-guidelines/) to help users with specific tasks
- **Detailed content-specific copy** — for example, product details, article content
- **Promotional copy —** such as call for subscriptions or sales

Both functionality and content specifications explain the logic of interaction instead of the visual details. Rather than being bound to a fixed format, these specifications usually have greater flexibility. Some designers write specifications below each design, while others annotate details on specific elements, depending on the complexity of the interface and how well their design tool supports annotation.

A UX designer shared with us an Axure prototype with specifications. This was a food-delivery mobile app intended for Australia. Functionality specifications (*Shake the phone to the next page*) and content specifications (*Display the dish name, price, and the restaurant location)* were included next to each screen.

*An example of prototype specifications (and a part of prototype) was shown above. The designer wrote functionality and some content specifications next to each screen.*

### What Makes a Good Prototype Specification

While prototype specifications are great for efficiency, unclear prototype specifications can cause headaches. Teams will often need additional meetings to explain these unclear texts. A good prototype specification:

1. **Represents ideas clearly and concisely.** Since the purpose of prototype specifications is to facilitate efficient understanding, review, and implementation, such specifications need to be brief, or people won’t read them.
2. **Describes the prototype, rather than replacing it.** Prototype specifications are not meant to be placeholders for a part of a design that wasn’t fully developed. A text description of a design will be more difficult to understand than a wireframe. A UX designer in China who participated in our research mentioned, “Once I wrote the word *category* next to a prototype I made. I meant that there would be some categories here in the interface, but I didn't sketch them on the prototype. In the design-review meeting, the visual designer asked what I meant by *category* and said I should have drawn some sample labels on the prototype before annotating the text *category* next to it. Then it would have been easier to understand." This example illustrates that prototype specifications alone can be obscure. Only a good combination of prototype specifications and prototypes could enable others to understand your design better.
3. **Uses language that is consistent with the vocabulary used in the project.** Especially for functional and content specifications, if the designer's language contradicts the project copywriting, it will be easy for others to misunderstand the specification. For example, if a heart symbol is annotated to mean “like” in the specification, but everyone else in the project talks about the “favorites” functionality, developers may wonder whether it is a new feature.
4. **Conforms to the design standards.** If there are design manuals or a well-established design system, your prototype specifications must be consistent with these design standards.

## Are Prototype Specifications a Must?

Element specifications are essential to help developers deliver the visual outcomes shown on your prototypes, and, luckily, they are automatically generated for most design tools. On the other hand, functionality and content prototypes provide clear definitions and explanations for vague and complex prototypes, but they are not a must for every design project.

Commonly, you don’t have to include extra specifications in the following scenarios:

- The interfaces or user flow is simple, without many state or component changes.
- The scope of the project is small (for instance, adding a single page instead of redesigning a whole product) or unlikely to impact the UX of your product.
- The components of the interfaces are largely from the company’s existing design system, with detailed annotations on how each component looks and works.

In our study, one Chinese UX designer also commented that in his team didn't always deliver prototypes with specifications. They chose to include them only if the interactions of the product were so complex that it was difficult to express all the information through prototype wireframes alone of if team members lacked relevant work experience — for example, because they were new to the team.

So, the context of your project and team determines whether you should include specification in your project.

### Alternative Approaches

In addition to prototype specifications, there are other ways to clarify design intent:

- **Separate prototype-specification document.** For very complex interactions or domain-specific apps, a few lines of prototype specifications noted on the side are no longer sufficient. It is common for designers to use a separate prototype-specification document to explain the interaction details and context prompts and deliver the document alongside the prototype.

- **Face-to-face review.** Even if prototype specifications are perfectly written, designers cannot guarantee that others will read them carefully or interpret them correctly. Especially in a big team, a dedicated face-to-face meeting together with prototype specifications can be useful. Team members can go through the prototype and specifications before the meeting and bring questions to the meeting. This can increase the efficiency of design-review meetings. Still, a face-to-face meeting should not replace prototype specifications for complex projects or new designs with which the team has little experience — people’s memory is unreliable, and it can be hard to remember all the specification details over time.

## Conclusion

Prototype specifications can disambiguate a design, save time, and serve as external memory for the team. But not every design needs detailed prototype specifications. Designers should evaluate their projects and team, then decide whether to write prototype specifications to make their work more efficient.
