---
type: source
name: "Using the Title Attribute to Help Users Predict Where They Are Going"
created: 2026-07-30
published: 2016-06-19
source_type: article
status: processed
url: https://www.nngroup.com/articles/title-attribute/
author: Jakob Nielsen
raw: raw/sources/2016-06-19_title-attribute.md
concepts:
  - "Navigation Design"
  - "Web Usability"
  - "Information Scent"
  - "Tooltip"
  - "Accessibility"
---

# Using the Title Attribute to Help Users Predict Where They Are Going

## Summary

One of the web's greatest problems is that users do not know where they are going when they follow links. The title attribute provides a solution by offering a tooltip that pops up when users hover over a link, giving them a preview of where the link will lead. This feature helps prevent users from going down the wrong path and reduces disorientation upon arrival. However, the title attribute should only be used for supplementary information when the link label and surrounding context are already clear. It should never be relied upon as the sole source of information about a link, especially on touchscreen devices where tooltips may not appear.

## Key Takeaways

- **Link titles as preview mechanism** — The title attribute can help users predict what will happen if they follow a link before clicking, reducing time wasted on incorrect paths.
- **Guidelines for effective titles** — Titles should be less than 60-80 characters and include the name of the destination site or subsite, added details about the kind of information to be found, or warnings about access requirements.
- **Don't overuse** — Link titles should not be added to all links; if the link name and surrounding context make it obvious where the link leads, a tooltip adds clutter and reduces usability.
- **Avoid device assumptions** — Different browsers display link titles differently, and most touchscreen browsers do not display them at all; link titles should enhance the experience for desktop users without being required for basic functionality.
- **Link text is primary** — The link label and surrounding text should be understandable even without the title attribute; the tooltip should be reserved for supplementary information that enhances but does not replace clear link text.

## Quotes

> Do not add link titles to all links: if it is obvious from the link name and its surrounding context where the link will lead, then a tooltip will increase clutter and ultimately reduce usability.

> Link titles do not eliminate the need for good information scent: the link label and its surrounding text should be understandable even if the link title is not displayed.

## Concepts

- [[Navigation Design]] — Title attributes support navigation by helping users understand where links lead and reducing disorientation.
- [[Web Usability]] — The title attribute is one tool for communicating link destinations, but should only be used when the link text itself is insufficient.
- [[Information Scent]] — Title attributes provide additional context about where a link leads, but cannot replace clear, descriptive link text.
- [[Tooltip]] — Tooltips display link titles and provide a familiar mechanism for users to preview link destinations on desktop devices.
- [[Accessibility]] — While title attributes can enhance usability for mouse users, they must not be required for understanding or accessing content, as screen readers and touchscreen users may not have access to them.
