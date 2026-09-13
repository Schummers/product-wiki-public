---
title: "Designing Effective Contextual Menus: 10 Guidelines"
date: "2025-11-28"
url: "https://www.nngroup.com/articles/contextual-menus-guidelines/"
author: "Kate Kaplan"
topics: [applications, design-patterns, interaction-design]
type: article
---

When used well, contextual menus help reduce visual noise, streamline layouts, and support focused interaction. But when used inconsistently, or when mislabeled, misplaced, or overloaded, they introduce confusion and can slow users down.

## In This Article:

- [What Are Contextual Menus?](#toc-what-are-contextual-menus-1)
- [How Should Contextual Menus Be Represented in an Interface?](#toc-how-should-contextual-menus-be-represented-in-an-interface-2)
- [Tradeoffs of Contextual Menus](#toc-tradeoffs-of-contextual-menus-3)
- [Guidelines for Using Contextual Menus](#toc-guidelines-for-using-contextual-menus-4)

## What Are Contextual Menus?

> [Contextual menus](https://www.nngroup.com/articles/contextual-menus/)**** are sets of actions related to a specific UI element, an area of the interface, a piece of data in an application, or a view of the application. They are typically used to house secondary functions that people may need to occasionally use and, therefore, should be kept within reach.

![Meatball (three horizontal dots) menu with the options archive, report, and delete.](https://media.nngroup.com/media/editor/2025/11/25/chatgpt_contextual_menu.png)

*ChatGPT 4: The contextual menu for a chat is accessed by clicking on the meatball icon (⋯) and includes the actions* Archive, Report,*and* Delete *.*

These menus are contextual because their contents depend on what the user is interacting with. For example:

- A post’s contextual menu might include options like *Edit*, *Pin*, or *Delete*.
- A photo’s contextual menu might include *Share*, *Download*, or *Set as Background*.
- A calendar event’s contextual menu might include *Delete, Reschedule*, *Duplicate*, or *Invite*.

## How Should Contextual Menus Be Represented in an Interface?

Contextual menus can be revealed in multiple ways, depending on the device and interaction model. On desktop, they often appear through right-clicks or two-finger clicks on a trackpad. On touch interfaces, they may appear after a long press on a specific element. Increasingly, though, designers use small icons, most commonly the **kebab** (⋮) or **meatball** (⋯) icons, to visually indicate the presence of a contextual menu.

These icon-based triggers began as mobile-design patterns, but they’ve since become common across desktop applications as well, serving as a recognizable shorthand for “related actions” or “additional options.”

### Kebab and Meatball Icons are Recognizable

In research I conducted for the book [Digital Icons that Work](https://www.amazon.com/Digital-Icons-That-Work-Comprehensive/dp/B0DFBLZ728/), participants were shown interfaces containing various icons, including kebab and meatball icons, and asked to describe and predict their functions.

Overall, both kebab (⋮) and meatball (⋯) icons were **generally recognized to mean “more options” or “other actions,”** as long as the icon followed the guidelines listed in this article. This was true across both mobile and desktop applications.

As one user describing the functionality of the icon explained:

> “It usually means there’s some other set of functions or icons that are hidden temporarily that you can click on and get to.”

Both kebab and meatball icons are good choices for representing contextual menus within interfaces.

## Tradeoffs of Contextual Menus

Despite this general understanding,**users often had little idea what specific options were hidden behind the kebab and meatball icons** because they have low [information scent](https://www.nngroup.com/articles/information-scent/), even when recognizable.

In addition, **some contextual menus were missed entirely** when the corresponding icons were:

- Positioned too far from the content they affected
- Rendered too small
- Designed to be [low contrast](https://www.nngroup.com/articles/low-contrast/)

And so, while contextual menus offer flexibility, they also introduce real usability challenges:

- **Reduced**[findability](https://www.nngroup.com/videos/findability-vs-discoverability/)**:** Icons representing contextual menus may be missed entirely, especially if they’re small, faint, or far away from the task focus area.
- **Low information scent:** Users can’t easily predict what the menu contains, making it harder to decide whether to potentially waste time sorting through it.
- **Misinterpretation risk:** Poor placement or inconsistent use may lead users to confuse contextual-menu icons with other functions, such as [progress indicators](https://www.nngroup.com/articles/progress-indicators/) or carousel controls (such as in the example below).

![A listing for a home with a meatball (3 horizontal dots) menu. When clicked it reveals the options to share and hide.](https://media.nngroup.com/media/editor/2025/11/25/trulia-contextual-menu-closed-and-open.jpg)

*❌ Trulia application for iOS: In our study, some participants confused the meatball icon with a carousel and expected that clicking it would allow them to view additional images of the property. In fact, clicking the icon revealed two actions associated with the post:* Share *and* Hide *. (Note: These two actions could have been easily surfaced outside the menu, eliminating the need for the meatball icon altogether.)*

To use contextual menus effectively, designers must weigh their limitations against layout constraints, user expectations, and task prioritization.

## Guidelines for Using Contextual Menus

### 1. Use Contextual Menus for Secondary, Noncritical Actions

Contextual menus are not appropriate for actions users rely on frequently. They are best used for secondary or low-priority options that can be accessed when needed but that shouldn’t distract from the core task flow.

- **Do**: Use research-informed judgement. Hide actions that are not primary but that are used enough that they need to be accessible.
- **Don't:** Hide essential, high-frequency actions behind an extra tap or click.

**Why:** Users are less likely to find or use actions hidden in contextual menus, especially if they are expecting those actions to be visible by default. Burying key actions frustrates users who perform the task frequently.

![AT&T help chat menu with a red box that says "end chat."](https://media.nngroup.com/media/editor/2025/11/25/att_chat_contextual_menu.jpg)

*❌ AT&T.com: The contextual menu in the chat experience contains the function* End Chat *, which would be a critical and primary action for anyone completing a chat workflow. The* End Chat *functionality should be displayed on the primary level, ideally represented by an “x” in the top right corner, a widely utilized standard.*

### 2. Place Contextual Menus near the Content They Affect

Users rely on [spatial proximity](https://www.nngroup.com/articles/gestalt-proximity/) to interpret how an element is related to others on the page. The location of the contextual-menu icon should clearly indicate the object it relates to.

- **Do:** When the contextual menu applies to a specific element (in comparison to an entire screen or page), position its icon directly within or beside the object it controls or supports.
- **Don't:** Place it randomly or ambiguously in the interface or far away from its associated element.

**Why:** Proximity reinforces context and helps users predict what actions the menu will contain.

![Kabab (3 vertical dots) menu in the bottom corner of a form field with the options "add to trip," "request policy exception," and "repay transaction."](https://media.nngroup.com/media/editor/2025/11/25/ramp_contextual_menu_open_and_closed.png)

*❌ Ramp.com: It’s unclear what the tiny kebab icon in the bottom right corner relates to. Because it is far away from any specific element (and therefore does not seem associated with anything in particular), it’s very likely to go unnoticed. Since the revealed actions are related to the transaction itself, this icon should be positioned higher up on the page, next to other transaction-related actions.*

### 3. Ensure Contextual-Menu-Icon Visibility with Sufficient Size and Contrast

Too often, contextual-menu icons are visually subtle to the point of invisibility, especially in small mobile interfaces or dense information areas, such as [complex applications](https://www.nngroup.com/articles/complex-application-design/).

- **Do:** Make icons large enough, high-contrast, and visible without hover when possible. Follow [known, tried-and-true visual design standards and guidelines](https://www.nngroup.com/articles/visual-design-in-ux-study-guide/).
- **Don't:** Tuck them away in hover-only states or reduce their visual salience in an attempt to make the interface feel light and minimalistic.

**Why:** Overly subtle visual design decreases discoverability. Contextual menus are often missed when their representative icons lack visual prominence.

![Kabab (3 vertical dots) menu in the bottom corner of a form.](https://media.nngroup.com/media/editor/2025/11/25/ramp_contextual_menu_closed.png)

*❌ Ramp.com: You may recall this example from guideline #2: Place Contextual Menus Near the Content They Affect. The kebab icon in the bottom right is likely to be missed because it's small, low-contrast, and far from the element it supports.*

![Meatball (3 horizontal dots) in a box with other content..](https://media.nngroup.com/media/editor/2025/11/25/rippling-in-app-contextual-menu.png)

*✅ Rippling mobile application for iOS: The border around the meatball icon increases salience and provides useful clues about the icon’s tappability. The three black dots against the white background provide sufficient contrast.*

### 4. Use Contextual Menus to Group Related, Contextual Actions

Contextual menus should group together actions that logically belong to the same object, element, or general hierarchy. Mixing unrelated options leads to confusion.

- **Do:** Group logically related options (e.g., *Duplicate*, *Share*, *Delete* for a file). If possible, surface a few action-related icons within the space before the overflow icon to add context and increase information scent for what other kinds of actions may be contained within the menu.
- **Don't:** Group unrelated options or combine both global and element-specific actions within the same contextual menu.

**Why:** Groups of unrelated options reduce clarity, decrease [findability](https://www.nngroup.com/videos/findability-vs-discoverability/), hinder spatial memorability, and increase [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/).

![A kebab (3 vertical dots) menu in the corner of a message on the Slack app.](https://media.nngroup.com/media/editor/2025/11/25/slack-message-thread-contextual-menu.png)

*✅ Slack desktop application for MacOS: The user can reasonably assume the hidden menu items will be related to the initial displayed actions — here, actions that can be performed on the message within the thread. Thread-specific messages, such as starring or moving the entire conversation, should be (and are) located elsewhere.*

### 5. Maintain Consistent Representation and Behavior of Contextual Menus Across the Interface

Contextual-menu icons should have a consistent function, behavior, and appearance across the product. If you decide to use a meatball or kebab icon to represent contextual menus throughout the interface, use it consistently, and reserve it for contextual menus only.

- **Do:** Use the same icon to represent contextual menus consistently.
- **Don't:** Repurpose the icon for unrelated interactions (e.g., using it to expand hidden content in one area, launch a [popup](https://www.nngroup.com/articles/popups/) in another, and open a side panel in yet another).

**Why:**[Inconsistent usage](https://www.nngroup.com/articles/consistency-and-standards/) erodes the user’s [mental model](https://www.nngroup.com/articles/mental-models/) and trust in the interface, as well as decreases [learnability](https://www.nngroup.com/articles/power-law-learning/) and memorability.

![Kebab menu (3 vertical dots) on a Google result revealing a popup for My Ad Center with many options including like, block, and report.](https://media.nngroup.com/media/editor/2025/11/25/google_serp_contextual-menu_add_center.png)

*❌ Google.com (1 of 2): Users can never be quite sure what they’re in for when they click the kebab icon. Clicking the icon next to a sponsored ad reveals a modal pop up for* My Ad Center *. Useful actions, such as* Like *,*Block*, and *Report* are likely to never be discovered due to their hidden nature and the overwhelming content revealed in the surprising popup.*

![A kebab (3 vertical dots) on a Google result showing a menu with additional information about the source.](https://media.nngroup.com/media/editor/2025/11/25/google_serp_contextual-menu_right-panel.png)

*❌ Google.com (2 of 2): Clicking the kebab icon for a nonsponsored result reveals a different set of information, element, and position for the secondary content: a side panel with secondary actions and information about the source. Again, the useful actions such as* Share *and* Save *are unlikely to be discovered. The behavior of revealing a side panel is likely also to be surprising and jolting; users expect this icon to reveal a brief, manageable set of actions, not a full-blown explanation on how search works.*

### 6. Use Tooltips or Labels to Clarify Ambiguous Contextual-Menu Icons

Because the kebab and meatball icons lack inherent meaning, small cues can greatly increase usability.

- **Do:** Include helpful labels or [tooltips](https://www.nngroup.com/articles/tooltip-guidelines/) when possible. Be as specific as possible. For example, when the actions are element-specific, include descriptors such as *Post Actions* or *Message Options*. If possible, include these descriptions as [visible labels for the icons](https://www.nngroup.com/videos/icon-text-labels/); if not, enable descriptive tooltips on hover.
- **Don't:** Leave the icon up for interpretation with no label or hover-state description, rely on ambiguous labels such as *Options*, or worse, use literal labels like *Ellipses*,**which don’t provide any additional context.

**Why:** Overflow icons carry low information scent; text cues improve clarity.

![In the bottom corner of a large banner image are 3 horizontal dots.](https://media.nngroup.com/media/editor/2025/11/25/patagonia_meatball-icon-expands-image.png)

*❌ Patagonia.com: At one point, the site’s hero images could be expanded by clicking on a meatball icon. (Why? Who knows.) The icon’s hover-state description was Ellipses. Obviously, a better label would be Expand Image. But, of course, an even better approach would be to reserve the overflow icon for revealing contextual options or actions (see guideline #7: Use Contextual-Menu Icons for Showing Actions, Not Expanding Content).*

![A meatball (3 horizontal dot) menu reveals additional actions on Notion.](https://media.nngroup.com/media/editor/2025/11/25/notion-contextual-menu.png)

*✅ Notion desktop application for iOS: Hovering over the overflow menu icon in the top right corner reveals a descriptive label that greatly increases information scent:* Style, Export, and more…*This tooltip changes contextually throughout the application based on the contents of the contextual menu.*

### 7. Use Contextual-Menu Icons for Showing Actions, Not Expanding Content

Do not use meatball or kebab icons to reveal hidden text or expand images.

- **Do:** Reserve meatball and kebab menu icons for revealing additional actions and options. When partial text content (e.g., a partial review or product description) can be expanded to show more, use explicit labels such as *Read more* or *Expand.*
- **Don’t:** Use these icons to expand text or images.

**Why:** These icons signal actions, not content expansion. Using them to reveal content misleads users and reduces clarity.

![A review has 3 horizontal dots underneath indicating the ability to expand the review.](https://media.nngroup.com/media/editor/2025/11/25/etsy-meatball-icon-expands-content.png)

*❌ Etsy.com: A* Read More *label is better than a meatball icon for expanding content.*

![A review has a blue "more" link at the bottom.](https://media.nngroup.com/media/editor/2025/11/25/google_reviews_more_link-expands-content.png)

*✅ Google.com: The* More *action label provides better information scent than a meatball icon would for expanding the full-text version of the review. This is a good move, since not that long ago, Google reviews utilized the meatball icon for this action. Unfortunately, the kebab icon in the top right still reveals only one action, Report, breaking guideline #8: Avoid Using Contextual Menus for A Single (Or Very Few) Action(s).*

### 8. Avoid Using Contextual Menus for One (Or Very Few) Action(s)

If there are only one or two possible actions, don’t make users hunt for those actions behind an icon. That approach increases [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) unnecessarily.

- **Do:** Display single actions (or limited sets of actions) directly in the interface when possible.
- **Don’t:** Use contextual menus to hide one or two items that could easily be accommodated within the available space.

**Why:** By arbitrarily hiding one or two actions behind a kebab or meatball icon, you save no space, increase effort, and reduce discoverability. Especially when the action has a well-understood and standardized icon (e.g., an “x” or trashcan icon for deleting an item or a flag for reporting a post), hiding that functionality under an ambiguous icon does not save space.

![Clicking Weather.com's kebab (3 vertical dots) menu reveals the single option of "delete".](https://media.nngroup.com/media/editor/2025/11/25/weatherdotcom-meatball-icon.png)

*❌ Weather.com: Clicking on the kebab icon transforms it into a black button labeled* Delete *. This approach doesn’t save any space, as the* Delete *function, if initially visible, would take up about the same amount of screen real estate as the kebab icon.*

![In the corner of a pinterest pin is a red button that says "save."](https://media.nngroup.com/media/editor/2025/11/25/pinterest-contextual-post-actions.png)

*✅ Pinterest.com: Instead of hiding critical actions within a contextual menu, Pinterest surfaces critical actions, here the* Save *(top right button) and* Share *(bottom right icon) actions when a user hovers over a pin.*

### 9. Avoid Hamburger Icons for Triggering Contextual Menus

The [hamburger icon (☰) is a widely recognized symbol](https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/) for global or main navigation, while the kebab and meatball icons (⋮ or ⋯) are recognized as representing contextual actions tied to specific elements or groups of related actions. Misusing one for the other can create confusion and dilute both patterns’ clarity.

- **Do:** Use the hamburger icon exclusively for accessing main site or app navigation. Use kebab or meatball icons to surface secondary, item-specific actions.
- **Don’t:** Use the hamburger icon near content to reveal contextual actions. Likewise, don’t use kebab or meatball icons to house global actions like account settings or site-wide preferences.

**Why:** These icons have distinct and well-established meanings. Swapping their roles breaks users’ [mental models](https://www.nngroup.com/articles/mental-models/), leading to hesitation and missed functionality.

![A chat with three horizontal lines indicating a menu in the bottom left corner.](https://media.nngroup.com/media/editor/2025/11/25/banana-republic-chat-hamburger-menu.png)

*❌ Bananarepublic.com: The site’s chat window features a hamburger menu containing one contextual action:* Save Transcript *. The hamburger menu icon should be reserved for housing global navigation or main site items. This example also violates guideline #8: Avoid Using Contextual Menus for A Single (Or Very Few) Action(s).*

### 10. Make Contextual Menus Keyboard and Screen Reader Accessible

Contextual menus must be usable by everyone. Users who do not use a mouse to click or fingers to tap need a way to access and interpret these menus efficiently.

- **Do**: Ensure contextual menus can be opened and navigated using keyboard shortcuts (e.g., tab, enter, arrow keys), and that their contents are fully readable and actionable via screen readers.

- **Don't**: Design menus that are accessible only by clicking or tapping. Avoid custom interactions that break standard accessibility behaviors.

**Why**: Prioritizing accessibility helps all users, not just those with disabilities. It improves efficiency for power users and ensures your interface complies with inclusive design standards.

### Conclusion

Contextual menus can streamline interfaces, reduce cognitive clutter, and support focused interaction when used appropriately. But because their discoverability and clarity are limited, they demand careful use. Balance minimalism with usability, reserving contextual menus for true secondary actions, placing them clearly and consistently, and using recognizable triggers.
