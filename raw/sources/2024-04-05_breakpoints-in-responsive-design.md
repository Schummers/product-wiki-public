---
title: "Breakpoints in Responsive Design"
date: "2024-04-05"
url: "https://www.nngroup.com/articles/breakpoints-in-responsive-design/"
author: "Kelley Gordon"
topics: [web-usability]
type: article
---

## In This Article:

- [Grids, Layouts, and Responsive Design](#toc-grids-layouts-and-responsive-design-1)
- [What Are Breakpoints?](#toc-what-are-breakpoints-2)
- [Four Common Breakpoints](#toc-four-common-breakpoints-3)
- [Examples of Breakpoints in Use](#toc-examples-of-breakpoints-in-use-4)
- [Tips for Designing with Breakpoints](#toc-tips-for-designing-with-breakpoints-5)

## Grids, Layouts, and Responsive Design

Both grids and layouts are essential components of [responsive web design](https://www.nngroup.com/articles/responsive-web-design-definition/). In responsive design, the design adapts and reacts to device characteristics and screen sizes.

[Grids](https://www.nngroup.com/articles/using-grids-in-interface-designs/) provide an organized way to efficiently create layouts in web and mobile designs. A grid is made up of columns, gutters, and margins that provide a structure for the layout of elements on a page.

**A layout** refers to how the different content and UI elements that make up a page are positioned on a screen. Layouts allow designers to utilize the space available on a screen or device to make the design and content most meaningful for users.

Grids are the structure that layouts are designed on. In addition to grids, breakpoints are fundamental in creating responsive designs.

## What Are Breakpoints?

Breakpoints are the building blocks of responsive design. They allow designers to adjust the layout to fit the needs of various screen sizes and devices.

A **breakpoint** defines a screen size where the design should adjust to a different layout.

Technically, a breakpoint is a specific screen size. When a window size hits that specific value, (for example, when because the user resized their browser window), the layout will change.

In practice, however, designers tend to use the word “breakpoint” to refer to the screen-size range (minimum and maximum width) for which a specific layout will be shown, because that is what they have to specify in media queries. For example, a desktop breakpoint might range from 1200px to 1400px — meaning that the desktop layout will be shown on any screen with the width in that range.

*As the ritual.com website is resized, it goes through 2 different breakpoints. As a result, the layout changes from a 4-column to a 2-column layout.*

The more breakpoints you have, the more your design will be able to adapt to granular screen-size variations properly and gracefully. However, having many layouts corresponding to a plethora of screen sizes may not work in practical situations, where design resources are limited. In practice, designers usually accommodate only 2–3 breakpoints.

## Four Common Breakpoints

Typically, designers will consider designing for 4 basic breakpoints. We use T-shirt sizing (small, medium, large) as there is no specific standard for each size. As mentioned previously, each breakpoint usually contains a minimum and maximum width that is customizable to fit the design’s layout needs. (A starting point for determining the exact values for these breakpoints would be to analyze the range of devices that your audience uses when accessing your site and then establish the breakpoints so you optimally accommodate the more common display sizes.)

- **Extra-small:** This range is intended for mobile and generally is up to 500px (if you include the device when in landscape orientation). A 4-column grid is commonly used at this breakpoint size.
- **Small:** This range accounts for tablet devices and ranges from 500 px to 1200 px. An 8-column grid is commonly used at this tablet size.
- **Medium:** This range is meant for laptop devices and typically ranges from 1200 px to 1400px. A 12-column grid is generally used at this size.
- **Large:** This range considers the large external monitor size and is 1400px and larger. The 12-column grid is generally continued at this size.

![Common breakpoints in responsive design](https://media.nngroup.com/media/editor/2024/03/19/breakpoints1.png)

*The basic breakpoint sizes to consider when designing is extra small, small, medium, and large.*

### Layout Changes

The following layout changes commonly occur when shifting between breakpoint sizes:

- **Different navigation:** For example, the left navigation may collapse under a hamburger icon when transitioning from a medium to small or extra-small breakpoint.
- **Collapsing columns:** A right column, if present, may collapse into the main content area or become available elsewhere.
- **Different amounts of visible content:** Layout columns may increase or decrease, resulting in more or fewer elements (cards, files, products, etc.) in a given row.

## Examples of Breakpoints in Use

### Example 1: Web to Mobile

Warby Parker is an eyewear brand. Its responsive website used a column grid to create an attractive visual experience.

At the medium screen size, 3 consistently sized columns made up the grid structure, and elements were aligned to and within these columns. On mobile (small screen size), Warby Parker’s 3-column grid reflowed into a one-column grid structure.

![Warby Parker website example](https://media.nngroup.com/media/editor/2024/03/19/breakpoint-examples-51.jpg)

*At the breakpoint for the small screen size, Warby Parker’s three-column grid (top) was reflowed into a one-column grid structure (bottom).*

### Example 2: Desktop to Laptop

On IBM’s website, the left navigation was visible by default in the layout corresponding to the large screen sizes, but at medium screen sizes, it was collapsed under a hamburger icon in the top bar.

![IBM Design Language website example](https://media.nngroup.com/media/editor/2024/03/19/breakpoint-examples-49.jpg)

*At large screen sizes, IBM’s left navigation was visible by default (top). At the medium size, the left navigation collapsed under a hamburger menu (bottom).*

### Example 3: Desktop to Tablet

Our third example is from Airbnb, a travel-booking site. At the large screen size, both a list of properties and a map with their locations were displayed on the screen. At the small size (corresponding to tablet devices), the list became the default display and the map was hidden behind a button.

![Airbnb website example](https://media.nngroup.com/media/editor/2024/03/19/breakpoint-examples-50.jpg)

*Airbnb’s displays both a list and a map of available properties on large-screen devices (top). At small-screen sizes, the map collapsed under a button (bottom).*

## Tips for Designing with Breakpoints

Breakpoints are fundamental to responsive design and to creating usable layouts and experiences.

### Define Your Breakpoints

If you don’t already have breakpoints determined, take some time to set them up. Think about the common ranges discussed above and refine them as needed. **Decide on a sensible naming convention** (like T-shirt sizing) that can adapt if you need to change your breakpoints. For example, if you discover that most of your mobile users now use larger smartphones, you may need to adjust your breakpoints for mobile to accommodate these larger display sizes.

Involve your development team in defining your breakpoints, because that team will set up the website's breakpoints.

**If you’re working with an existing website,** the breakpoints will most likely be established. In this case, take time to understand the different breakpoints so you can design layouts appropriately.

### Design with Breakpoints in Mind

Once you have your breakpoints defined,**** think through how the design (including content) will flow and rearrange at these different sizes. Ask yourself:

- Is there something that your users **need to know at a particular size?**
- Are those crucial pieces of information easily available in the layout, at that size **?**
- Is there **anything that needs to change** from the standard flow of content and layout?

For example, at the extra-small size (mobile), space is limited. Collapsing a left navigation under a hamburger icon will allow the user to focus on important content.

Or, if at large screen sizes, your main call to action was in the rightmost column, will this still be accessible on mobile, if your columns are stacked? Creating an exception from regular column stacking to make the call to action more discoverable (for example by making some preceding content collapsible under accordions) may be needed. These kinds of questions will help you decide how the layout will change from breakpoint to breakpoint. Once you created and tested your design, communicate to developers how the design will change based on the established breakpoints.
