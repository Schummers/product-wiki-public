---
title: "Front-End Style-Guides: Definition, Requirements, Component Checklist"
date: "2016-03-27"
url: "https://www.nngroup.com/articles/front-end-style-guides/"
author: "Page Laubheimer"
topics: [agile, ux-design-process, visual-design]
type: article
---

## In This Article:

- [What Is a Front-End Style Guide?](#toc-what-is-a-front-end-style-guide-1)
- [The UX Benefits of a Front-End Style Guide](#toc-the-ux-benefits-of-a-front-end-style-guide-2)
- [Front-End Style Guides Are not Editorial or Branding Style Guides](#toc-front-end-style-guides-are-not-editorial-or-branding-style-guides-3)
- [Front-End Style Guides Include Responsive Design Patterns](#toc-front-end-style-guides-include-responsive-design-patterns-4)
- [Checklist of 8 Main Requirements for a Front-End Style Guide](#toc-checklist-of-8-main-requirements-for-a-front-end-style-guide-5)
- [25 Common UI Components Included in Front-End Style Guides](#toc-25-common-ui-components-included-in-front-end-style-guides-6)
- [Conclusion](#toc-conclusion-7)
- [References](#toc-references-8)

## What Is a Front-End Style Guide?

Front-end style guides have become an increasingly commonplace deliverable in UX practice. As described by Jeff Gothelf and Josh Seiden in their book *Lean UX,* they originated in [Agile or Lean environments](https://www.nngroup.com/courses/lean-ux-and-agile/).

> Definition: **Front-end style guides are a modular collection of all the elements in your product’s user interface**, together with code snippets for developers to copy and paste as needed to implement those elements **.** They include common UI components like buttons, form-input elements, navigation menus, modal overlays, and icons.

A front-end style guide is both a **deliverable** created by the UX team (in concert with the engineering team, typically) and a **tool** used by the entire team for maintaining consistent, nimble product design in a modular format.

Front-end style guides are distinct from design pattern libraries, which are a long-standing tool used by UX practitioners to define broad design ideas, rather than specific implementation details. Unfortunately, [some](http://ux.mailchimp.com/patterns/about)[proponents](http://alistapart.com/blog/post/getting-started-with-pattern-libraries) of front-end style guides refer to them as *pattern libraries*, which has caused some confusion in the UX community.

![Salesforce Lightning Design System Screenshot](https://media.nngroup.com/media/editor/2020/02/29/screen-shot-2016-03-14.png)

*Salesforce’s Lightning Design System shows a UI element,* Button Group Base *, along with an example of how to implement it, guidelines for how it should function, and when an alternative variant (such as* Button Group Disabled *) should be used. The example is a live element that is interactive and exhibits the same behaviors as in the final product.*

## The UX Benefits of a Front-End Style Guide

The purpose of a style guide is to collect all product-interface elements in a modular library. It benefits the UX team in two ways: (1) prototyping ideas and implementing new designs becomes more efficient, and (2) a consistent visual design can be easily enforced throughout the product. Designers and developers are just as lazy as everybody else. (That’s “lazy” in a positive sense, as in preserving effort and company resources.) Thus, if it’s less work to do the right thing and create a consistent user interface, they’re more likely to do it than to invent a new, inconsistent design or implementation.

When a mature front-end style guide exists, the UX team spends less time creating high-fidelity design mockups for every new idea. Instead, the main design-specification deliverable can be a quick sketch that unambiguously references which components get applied where in the design. Such a library of existing modules also allows for fast high-fidelity prototyping: the UX team can quickly assemble a realistic interactive prototype that could be used in usability tests or shared with stakeholders.

## Front-End Style Guides Are not Editorial or Branding Style Guides

You may already be familiar with two other types of style guides:

1. Editorial style guides specify writing style, grammar, punctuation, and other content-editing rules. Many websites and most publications do have such style guides and content teams are supposed to follow them.
2. Branding style guides usually specify brand-related rules such as acceptable logo usage, color palette, and typography.

Unlike editorial style guides, front-end style guides do not normally include writing-related guidelines. However, they often do have a high overlap with the branding style guides — in addition to rules and descriptions of the UI components, they include brand-related elements and guidelines.

![Adobe Corporate Branding Guidelines Screenshot](https://media.nngroup.com/media/editor/2020/02/29/screen-shot-2016-03-09adobe.png)

*Adobe’s “Corporate Brand Guidelines” is a branding style guide and not a front-end style guide. Front-end style guides often contain many of the elements found a branding guidelines document.*

The most important feature that separates front-end style guides from other types of style guides is that front-end style guides are rarely static, but are living collections of UI- elements’ descriptions and corresponding code snippets.

Most often, front-end style guides take the form of a web page or other interactive digital asset, rather than a PDF. You can typically interact with all the components in a front-end style guide, and many development teams choose to implement them so that any change made to components in a style guide will automatically update the product’s design as well. This isn’t a requirement for an effective style guide, but it can help to enforce its rigorous use.

## Front-End Style Guides Include Responsive Design Patterns

In [responsive designs](https://www.nngroup.com/articles/responsive-web-design-definition/), the front-end style guide should not only define the interface components, but also describe how their styling and usage will differ across different screen sizes. Here are some pieces of information that are useful:

- Layout grids indicating how various components should be used in various screen-size contexts
- Spacing around common elements when used on different screen sizes
- Guidelines for where in the interface specific components should be placed (These guidelines can help enforce consistency: for example, in a mobile app, the title bar and navigational elements will typically be present in most screens at the top, so defining that in the style guide can help to avoid one-off screen designs.)

![Google Material Design Screenshot](https://media.nngroup.com/media/editor/2020/02/29/screen-shot-2016-03-09.png)

*Google’s Material Design style guide includes representations of how to use the responsive grid system, and where various parts of the interface should be consistently placed.*

## Checklist of 8 Main Requirements for a Front-End Style Guide

When creating a style guide, make sure to include the following 8 key features:

1. Table of contents **** that splits components into easily-findable categories
2. Responsive layout or grid systems used to place common UI elements
3. Color palette of the product (in appropriate format, e.g. HEX for the Web, UIColor for an iOS app)
4. Typeface styles (e.g. *H1 Title*, *Body text*, *Photo caption text*), which should include typeface name and foundry, sizes, weights, leading/line height, tracking/kerning, and the appropriate contexts of use for that text style

Then, for each of the specific UI elements in your product include the following information:

1. Description of the appropriate context of use: When does it make sense to use one particular component versus a similar one?
2. Code snippets **,** often hidden in an [accordion](https://www.nngroup.com/articles/accordions-complex-content/) feature
3. Specs for implementation, including positioning and spacing information
4. Dos and don’ts for that element.

## 25 Common UI Components Included in Front-End Style Guides

Here’s a starter list of UI elements that typically get included in a style guide. While this not an exhaustive list of all UI elements that *can* be used in a front-end style guide, it covers many of the common components.

1. Buttons
2. Button groups
3. Breadcrumbs
4. Cards
5. Tables
6. Dialogs
7. Grid lists of content, media, or photos
8. Vertical lists
9. Navigational menus (and subnavigation)
10. Date and time pickers
11. Progress and loading indicators
12. Checkboxes
13. Radio buttons
14. Drop-down menus
15. Sliders
16. On-off switches
17. Numeric-input steppers/incrementers

1. Form fields (include variations with maximum character-count indicators, and indicators for when the field is required)
2. Tabs
3. Toolbars
4. Tooltips
5. Alert modals
6. Icons
7. Animations
8. Tokens, also known as chips (e.g. email-address field)

![Kayak Numeric Input Stepper](https://media.nngroup.com/media/editor/2020/02/29/photo-mar-10-11.png)

*Kayak’s iOS app features numeric-input steppers for the number of rooms and guests. If you feature this input component in your product, it should be included in the style guide.*

![Token from Material Design](https://media.nngroup.com/media/editor/2020/02/29/screen-shot-2016-03-10.png)

An example of a token (or chip) from [Google’s Material Design](http://www.google.com/design/spec/components/chips.html). Tokens are often used in email-address recipient fields, to show each recipient separately, and allow you to delete a recipient with one click. They are also used in advanced-search fields and metadata tags to distinguish between terms that include a space.

Start with this list and pick from it only the components that are present in your product (don’t add new elements to your product or designs simply to satisfy this list). If you have additional unique elements, include them in your style guide.

## Conclusion

Front-end style guides are becoming one of the most useful UX deliverables. They are especially important in Agile environments, where enabling more efficient design workflows is critical to keeping the fast pace of development. When developed rigorously, style guides promote consistent design practices and enforce developer adherence to specifications. A good front-end style guide should include responsive-design patterns and grids, code snippets for implementation, and strong guidelines for using each component.

Learn more about best practices for determining the appropriate component granularity, common pitfalls when creating (and using) style guides, and workflow options for creating a front-end style guide in our full-day [UX Deliverables Seminar](https://www.nngroup.com/courses/ux-deliverables/).

## References

Jeff Gothelf and Josh Seiden (2013): [Lean UX: Applying Lean Principles to Improve User Experience](http://www.amazon.com/dp/1449311652?tag=useitcomusablein), O’Reilly Media.
