---
type: source
name: "Split Buttons: Definition"
created: 2026-07-30
published: 2019-05-12
source_type: article
status: processed
url: https://www.nngroup.com/articles/split-buttons/
author: Page Laubheimer
raw: raw/sources/2019-05-12_split-buttons.md
concepts:
  - Interaction Design
  - UI Patterns
  - Cognitive Load
  - Discoverability
  - Usability
---

# Split Buttons: Definition

## Summary

A split button combines a default action with a menu of related alternatives. The label portion executes the default action instantly; the arrow portion opens a dropdown menu with other options. Split buttons reduce visual complexity by grouping related commands and lowering interaction cost for the most common action, but they create discoverability problems because users may not notice the arrow or the menu inside. Split buttons are appropriate for repeat-use applications where one option is clearly most frequent, but not for website navigation or touch interfaces.

## Key Takeaways

- **Split button: default action plus menu** — Clicking the label performs one-click access to the most-used action; clicking the arrow opens related options, lowering interaction cost for the default while grouping similar commands.

- **Visual separation is essential** — The arrow must be clearly separated from the label with a dividing line or color contrast, and always visible rather than appearing only on hover, so users recognize the split button pattern.

- **Discoverability is the tradeoff** — Users, especially those learning an application, may not notice the secondary menu; if users miss the menu options, the split button defeats its purpose.

- **Text labels improve recognition and target size** — Icons alone are insufficient; include text labels for both the default action and menu items to improve learnability, discoverability, and increase the clickable area.

- **Not for touch or navigation** — Split buttons are risky on touchscreens due to small arrow targets; they should not be used for navigation (use a standard dropdown menu instead) since navigation involves going to new pages, not selecting actions.

- **Persistent split buttons complicate learning** — While persistent buttons (where the last-selected option becomes the new default) help power users, they confuse new users by breaking spatial consistency and requiring attention to what the default is.

## Quotes

> "A split button is a button with two components: a label and an arrow; clicking on the label selects a default action, and clicking on the arrow opens up a list of other possible actions."

> "the arrow that signals the menu aspect of the button must be clearly separated from the label of the button."

> "Split buttons are most useful in repeat-use desktop applications with a large number of commands that need to be consolidated."

## Concepts

- [[Interaction Design]] — Split buttons reduce cognitive load by grouping commands but require careful design to ensure the secondary menu is discoverable.

- [[UI Patterns]] — Split buttons are a hybrid of buttons and menus; they work well for desktop applications with frequent repeat use but are problematic on touch and for navigation.

- [[Cognitive Load]] — Grouping related commands reduces complexity, but hidden menu options may increase cognitive load if users don't discover them.

- [[Discoverability]] — Small arrow targets and hidden menus have low discoverability, especially for new users who may not recognize the split button pattern.

- [[Usability]] — Fitts's Law applies to split-button arrows; small targets require more precision and time, making split buttons unsuitable for touchscreen interfaces.
