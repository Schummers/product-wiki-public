---
title: "Case Study: Iterative Design and Prototype Testing of the NN/g Homepage"
date: "2018-08-26"
url: "https://www.nngroup.com/articles/case-study-iterative-design-prototyping/"
author: "Kathryn Whitenton, Sarah Gibbons"
topics: [prototyping, ux-design-process]
type: article
---

Usability guidelines tend to be [stable over time](https://www.nngroup.com/articles/usability-guidelines-change/). But, in the 5 years since our last major redesign of the [NN/g homepage](http://www.nngroup.com), both our content and our audience’s expectations for visual design have evolved.

When we set out to redesign our own homepage, we used the same methods for strategy development, prototyping, and user testing that we teach at the [UX Conference](https://www.nngroup.com/ux-conference/). Because even though we’ve conducted [thousands of usability tests](https://www.nngroup.com/articles/nielsen-norman-group-20-years) on a wide variety of websites and applications, we still find that user research and iterative design are essential to achieving the best outcomes.

## In This Article:

- [Design Goals](#toc-design-goals-1)
- [Iterative Prototype Testing](#toc-iterative-prototype-testing-2)
- [From High-Fidelity Prototype to Specification](#toc-from-high-fidelity-prototype-to-specification-3)
- [Key Takeaways From Our Process](#toc-key-takeaways-from-our-process-4)
- [Incremental Implementation](#toc-incremental-implementation-5)

## Design Goals

Since we’ve conducted many rounds of usability testing of the website in the past, we started with a good grasp of our audience and its goals. But we did conduct [qualitative surveys](https://www.nngroup.com/articles/qualitative-surveys/) to assess customer reactions and expectations about both the website and about our overall brand.

This customer feedback, aligned with our internal strategic goals, led us to 3 main design objectives, each of them related to [outcomes, not just features](https://www.nngroup.com/articles/outcomes-vs-features/):

1. **Demonstrate credibility**: The best way to explain why we are a trusted authority is to not just talk about our dedication to research, but also show prominent examples of our ongoing work.
2. **Create an appealing, minimalist aesthetic**: Modernizing the visual design also enhances credibility, but only if visual details support usability rather than detracting from it. For example, large fonts are both appealing and usable; [small text overlaid on images](https://www.nngroup.com/articles/text-over-images/) looks trendy but impedes reading.
3. **Maintain access to primary offerings**: New content and visual details must not interfere with navigation pathways to services and information.

These design principles became both a guide in making [design tradeoffs](https://www.nngroup.com/courses/design-tradeoffs/) and a yardstick for measuring outcomes. For example, debates about how many different colors to use were ultimately resolved by revisiting the goal of creating a [minimalist aesthetic](https://www.nngroup.com/articles/characteristics-minimalism/). We knew the layout was working when people’s first reactions became positive comments about how much research we conduct (rather than comments on the visuals themselves.)

## Iterative Prototype Testing

We have long advocated [testing design prototypes](https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/) before writing code, and we followed our own advice. When it comes to prototyping, it is important to pick your tools with purpose — especially for teams like ours, where both our [developers](https://lightsonsoftware.com/) and our designers are geographically distributed. We avoided programs that were expertise-specific, which could limit or bottleneck collaboration. We chose to work in [Moqups](https://moqups.com) to wireframe and design, then used [Basecamp](https://basecamp.com/) to track tasks and to do lists. No tool is perfect, but these were a good fit for our team since they are low cost, easy to learn, automatically share changes to all users, and are accessible through a web browser.

We started with a low-fidelity, black–and–white wireframes for content planning, but shifted to [high-fidelity visual prototypes](https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/) before doing any testing, since [comparing visual designs](https://www.nngroup.com/articles/testing-visual-design/) to assess aesthetic appeal was a high priority. We created multiple visual versions to test, then successively narrowed the set. With each new version we added polish and fidelity.

![Examples of black and white and high fidelity prototypes](https://media.nngroup.com/media/editor/2018/08/24/iterative-prototype-progression.jpg)

*Our iterative design process evolved from black–and–white wireframes for content planning to multiple versions of high-fidelity visual mockups created with cloud-based prototyping tools.*

We [recruited both new visitors and repeat users](https://www.nngroup.com/reports/how-to-recruit-participants-usability-studies/) for 3 rounds of testing with interactive prototypes and the legacy design on a combination of both desktop and mobile devices.

We learned something new with each round. Feedback was categorized into four themes: copy, architecture, layout, and visual style. Depending on the feedback, we tweaked one or multiple aspects of the page. In some cases, we only needed to tweak a sentence or make something higher contrast; in other cases we redesigned a whole section to better achieve our design goals. Here are a few examples of what we learned from comparing multiple prototypes:

- Early homepage layouts compared a variety of introductory imagery, from no image to different styles of background images. We quickly realized that the background image added visual appeal, and from there compared various images to find the best one. (Pro tip: don’t put text on top of the subject’s face.)
- Early layouts used a grid of squares to present articles, videos, and training events. Users *said* they liked this grid — but when we added an alternative layout using a list format for articles, people unanimously gravitated towards the list version. ([Pay attention to what people do](https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/), which is often different than what they say.) Using distinct formats for different types of content helped people quickly understand the difference and focus on using the content rather than trying to make sense of the organization. (We also tested this list layout to determine whether the far-right column would trigger [banner blindness](https://www.nngroup.com/articles/banner-blindness-original-eyetracking/), and found that it did not.)

## From High-Fidelity Prototype to Specification

We began by [prioritizing our content](https://www.nngroup.com/courses/scaling-responsive-design/): we took a wireframe of the high-fidelity prototype and ranked the components based on importance. This became a guideline for our redesign (and served as a guideline for consistency across mobile and web).

![Content Prioritization example](https://media.nngroup.com/media/editor/2018/08/24/information-hierarchy.jpg)

*Using the high-fidelity prototype, we created a content hierarchy. We used this ranked list throughout our iterations to inform visual hierarchy and layout. (Desktop version on the left, mobile version on the right.)*

For the homepage, used the ranked components as a guide to sketch our first mobile wireframes. Starting relatively fresh for this redesign allowed us to build our layouts and visuals in a clean, sustainable manner. We created a 12-column grid (on both web and mobile) that we could use as a flexible base for a wide range of page layouts.

![Illustration of page grid](https://media.nngroup.com/media/editor/2018/08/24/grid.jpg)

*An early example of our grid system and its application to a mid-fidelity homepage wireframe.*

From here, we created three primary column variations and began to plug and play following the content hierarchy we specified from our old site. (This process is similar to the one taught in our course on [Web Page UX](https://www.nngroup.com/courses/web-page-design/).) Whereas most websites seem to ignore big-monitor users, one of our three layouts targeted this group. (In addition to the traditional laptop and mobile audiences.)

As new components were designed (for example, buttons, lines, type, hover styles, and tiles), they were added to a master component stylesheet. This process made creating specifications for developers efficient because there was no redundancy; we named each component on the page layouts, allowing development to reference the detailed spec in the master component stylesheet. If subsequent changes were made to one component in the stylesheet, these changes did not need to be reflected in new layouts.

Designing in this systematic way enabled easy collaboration with our developers, who built a corresponding [front-end style guide](https://www.nngroup.com/articles/front-end-style-guides/). The front-end style guide collected all product-interface elements in a modular library. It benefited us, as the UX team, in two ways: (1) prototyping ideas and implementing new designs was efficient, and (2) a consistent visual design was easily enforced throughout the product.

## Key Takeaways From Our Process

An iterative approach to prototyping and testing enabled us to:

- **Explore many design options without pressure to design the perfect layouts and visuals up front.** Because many rounds of testing are a key part of our progress, we expected our designs to continually evolve. This benefits us in two ways: (1) we didn’t waste time making the early version pixel perfect, and (2) the time to test and iterate was built into our project timeline from the beginning.
- **Make live improvements during usability testing to maximize user feedback**. Since we are a relatively lean team, this paradigm also offered us the opportunity to divide and conquer: as one person conducted usability test, the other dynamically shifted wireframes based on feedback. Improving wireframes during the test allowed us to get significantly more feedback in a short amount of time. If we changed a design, we quickly knew whether or not it worked. This process helped us focus our design time on the layouts that had the best feedback.

We are a small company, but we saw once again that a good user-centered design process doesn’t require huge budgets. Nor will many rounds of iterative design delay your project unacceptably. As long as you plan for it and use [discount usability](https://www.nngroup.com/articles/discount-usability-20-years/) methods, you can do a lot with a little, and improve the design every step of the way.

## Incremental Implementation

Rather than redesigning the entire site at once, we’ve opted for an [incremental approach](https://www.nngroup.com/articles/radical-incremental-redesign/), gradually updating different pages. To maintain a basic level of consistency in the meantime, we’ve implemented a few universal styles to the legacy site as well, such as the header and footer style, as well as fonts and link colors.

This incremental approach also gives us the flexibility to learn as we go. If something isn’t quite right, we can make adjustments rather than getting too far down the road, potentially tripling the re-do work. (And there are *always* tweaks needed after any launch: if you do enough user testing before launch, you can reduce the rework, not eliminate it.) We’re excited to share our new homepage with you, and look forward to extending these enhancements throughout our website in the coming months — stay tuned!
