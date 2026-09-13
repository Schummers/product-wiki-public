---
title: "Creating Design Specs for Development"
date: "2025-06-20"
url: "https://www.nngroup.com/articles/creating-design-specs-for-development/"
author: "Kelley Gordon"
topics: [agile, ux-design-process, ux-teams]
type: article
---

You work tirelessly on a new design project. It’s your masterpiece… until the dev team says it isn’t possible. Most designers have experienced this situation at some point in their careers. As frustrating as it may be, there are many ways to avoid this situation from happening. Clear design specs are a good place to start.

## In This Article:

- [What Are Design Specs?](#toc-what-are-design-specs-1)
- [The Components of a Design Spec](#toc-the-components-of-a-design-spec-2)
- [Examples of Specs](#toc-examples-of-specs-3)
- [Tips for Aligning with Developers](#toc-tips-for-aligning-with-developers-4)

## What Are Design Specs?

Design specifications are a way to align on and efficiently communicate designs to a software-development team.

> **Design specifications (specs)** are documents that provide all relevant information on the functionality, behavior, and appearance of a design, so that developers can implement the design into a real, functioning product.

Design specs allow the design and development teams to have productive conversations and align on user needs, design feasibility, and design and technical requirements.

Depending on the project needs, design specs can be focused on one design aspect. For example, for a visual-refresh project, the design spec may include only information about the appearance of the different design elements, rather than on their functionality.

For many teams, this documentation takes the form of a Figma (or other design tool) link with additional project and development details, organized in **a development issue** or ticket in a development tool, like GitHub or Linear. The development issue would include relevant contextual information, like the goal, use case or requirements the design solves for, so that developers can implement the design.

![Design specifications include a design file and a development issue.” Shown are labeled mockups of a GitHub issue and a Figma webpage design file.](https://media.nngroup.com/media/editor/2025/05/29/design-spec-visual.jpg)

*Design specifications include a design file and development issue that contains additional context.*

## The Components of a Design Spec

Remember, the spec has two big components: the design file (e.g., Figma) and the development issue.

### What Is Included in the Design File

The design file is what designers typically think of when they hear the phrase “design spec.” It specifies the design work that the design team produces, broken down into consumable pieces for the development team.

This portion of the spec should include information about:

- **Interaction flows:** Define what happens when users click or tap on interactive elements.
- **Visual design:** Define the [color palette,](https://www.nngroup.com/articles/color-enhance-design/)[typography](https://www.nngroup.com/articles/typography-terms-ux/) styles, and icons used in the design. Color palettes and typographic styles should be set up separately in the design file, with each style named appropriately, so developers and other designers can easily use them.
- **Layout:** Define the grid system used, as well as[various breakpoints.](https://www.nngroup.com/articles/breakpoints-in-responsive-design/)
- **Interaction elements:** Provide components for any [user-interface elements,](https://www.nngroup.com/articles/ui-elements-glossary/) like [buttons](https://www.nngroup.com/articles/button-states-communicate-interaction/) and input fields. Include any details about associated microinteractions, like animations or transitions.
- **Content:** Use real text and multimedia content in the design mockups, not placeholders, providing details needed for image sizes.
- **Specific accessibility needs:** Your designs should comply with accessibility standards; however, specific items (e.g., tabbing order on a page or [alt text](https://www.nngroup.com/articles/write-alt-text/)) may need to be called out explicitly.

### What Is Included in the Development Issue

A lot of development teams see the development issue as a “contract” between the dev and design teams. What is outlined in the issue is what the developer is on the hook for delivering.

Issues typically include a lot of context needed to understand the designs and the project: the goal of the design, what is in and out of the project’s scope, a description of the functional (e.g., system features) and nonfunctional (e.g., performance) requirements, any use cases the design touches on, and potential risks and mitigations. This information should be specific to the design that is getting implemented and should come from the product owner or tech lead.

A screenshot of the design may also be included in the development issue, to communicate what the dev and design team agreed on when the issue was written. The screenshot also allows development to quickly see what the issue is about. However, if screenshots are included, they should be consistent with the designs in the design file.

If the design gets updated, the design team will need to discuss the update and an implementation timeline with the development team. Depending on how big the update is, an additional development issue might be created. Any discrepancies between the screenshots in the development issue and the Figma file should be noted to prevent confusion about what needs to be implemented.

![Linear issue view showing objectives, scope, assumptions, success metrics, and a Figma design link under “Wireframes / Design References.”](https://media.nngroup.com/media/editor/2025/05/29/spec-example.jpg)

*A Linear issue contains context and design details, including a link to the Figma design file*.

Small specs are much easier to create and implement than one very large spec. **If a design spec is getting too large** and difficult to organize and maintain, it might be a sign that it **needs to be broken down** into smaller, more digestible pieces. Include the dev team in this decision, as the ease of implementation will be affected by how the design is further broken down.

### Specs Are Created in the Design Phase

In the end-to-end product-design process, design specs are created during the design phase, after substantial work has already been completed. **Before creating a spec, your team should:**

- Define the product's strategic context
- Conduct any necessary discovery research
- Create and prototype flows and interactions based on user needs
- Carry out usability testing on the designs you or your team has created
- Apply findings discovered through usability testing to designs

It takes a lot of time to create a spec and then implement the designs. You want to make sure the designs are worth the effort and they address the right user needs. That is why a lot of upfront work is needed before even getting to spec your design work.****

![Diagram of the product design process: Define, Discover, Design (Ideate, Prototype, Test, Spec), then Develop. “Spec” is highlighted.](https://media.nngroup.com/media/editor/2025/05/29/product-design-process.jpg)

*Design specs are created in the design phase of the end-to-end product design process.*

### Who Is Responsible for Writing Design Specs?

The design team (whether made up of one designer or several designers with specialized roles such as visual designer or content designer) is in charge of creating the design file in the spec, as well as annotating it with any details that may be important for the developers.

The development issue is usually created by the product owner or a member of the development team (even though that may vary depending on the team and its specific context).

## Examples of Specs

### Example 1: Small Mobile Design

In this spec, the design is perfectly sized and portioned for a developer to understand the full design and implement it in a timely manner. The design is about how navigation for a website works on a mobile device. Sufficient contextual information is provided directly in Linear, as opposed to the Figma file, providing organization for the development team. The context supplies information on design goals, user needs and use cases, as well as any preliminary research findings. You will also notice that the Figma file is linked, ensuring that developers always have access to the latest version of the design.

![Linear issue titled “Create new mobile navigation” includes goals, scope, research, design notes, and a Figma file link for developer reference.](https://media.nngroup.com/media/editor/2025/05/29/issue-example.jpg)

*The Linear issue contains a link to the Figma file, as well as additional context for the development team to use when coding.*

In the linked Figma file, the relationships among different screens are mapped out through annotations, allowing developers to easily understand how users might interact with them.

![Figma prototype showing mobile navigation flow, including interactions for tapping the hamburger menu and search icon on the NN/g homepage.](https://media.nngroup.com/media/editor/2025/05/29/example-1.jpg)

*The Figma file**shows what happens when a user taps the hamburger and search icons.*

### Example 2: Large Webpage Design

The Figma file of this spec includes details on layout, content, and visual design of an entire webpage. The design shows the webpage at various breakpoints, as well as color variations that the page will need to support.

Annotations are color-coded, allowing developers to easily scan and see what is important for their specific coding work. For example, back-end-specific annotations are red, so backend developers can quickly find pertinent information to their work. Figma comments are also used to asynchronously align on design feedback and questions.

![Figma file showing webpage spec with page structure, color variants, and readiness indicators for developers in green, yellow, and red.](https://media.nngroup.com/media/editor/2025/05/29/example-2.jpg)

*The Figma file for a webpage spec shows the page breakpoints and color variations. In the left side panel,  green, yellow, and red indicators let developers know whether those pages are ready for them.*

### Example 3: Component Spec

This button component spec from Google’s Material Design provides details about each button style, including different states and values for various attributes (e.g., the button’s height is 40dp), as well as references for both designers and developers.

![Material Design webpage showing specs for an elevated button, with labeled parts, button states, and navigation for other button types.](https://media.nngroup.com/media/editor/2025/05/29/google-material-example.jpg)

*Google’s Material Design button component spec is presented on a website, instead of just a Figma file.*

## Tips for Aligning with Developers

Designers and developers do not always agree on designs. Each brings a unique and needed perspective to create and develop useful experiences. Here are some tips to improve communication and working relationship with developers:

- **Include the development team in design conversations way before your design is “done.”** Ideally, the design spec documents previously agreed-upon information on behavior, functionality, and visual design.
- **Allow time for developers to leave comments in your design file.** This needs to happen before the design-review meeting with your developers. It will give them time to think about the design and its feasibility. In your design-review meeting, focus the conversation around any comments made in the design file, making the meeting much more productive and effective.
- **Be prepared to make tradeoffs.** There are times to push back on development and times where tradeoffs are needed. This is a natural part of working with a development team. Designers should ensure that critical user needs are being met and should not give in to everything the development team brings up, but, if a certain aspect of the design is going to take substantial development effort, and is not critical for your user, revisiting it may be worth it.
- **Make sure design updates are documented and communicated to developers.** You would be shocked how many times a lack of documentation has created confusion and frustration in design and development teams. Communicate design changes in your design specs as well as through other communication channels that your team may use.
