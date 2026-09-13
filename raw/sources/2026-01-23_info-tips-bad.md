---
title: "Why So Many Info Tips Are Bad (and How to Make Them Better)"
date: "2026-01-23"
url: "https://www.nngroup.com/articles/info-tips-bad/"
author: "Kate Kaplan"
topics: [applications, design-patterns, interaction-design]
type: article
---

Information tips — those helpful little messages triggered by tapping or hovering over a question mark (*?*) or info (* i*) icon — can help users make faster decisions and increase the understandability of UI elements. But in practice, they’re often overused, misapplied, or bloated with unnecessary content. When info tips hide essential instructions or bury users in redundant explanations, they create confusion rather than clarity.

## In This Article:

- [What Is an Info Tip?](#toc-what-is-an-info-tip-1)
- [Representing Info Tips in User Interfaces](#toc-representing-info-tips-in-user-interfaces-2)
- [The Problem with Info Tips](#toc-the-problem-with-info-tips-3)
- [Pitfalls of Bad Info Tips](#toc-pitfalls-of-bad-info-tips-4)
- [Pitfall #2: Hiding Critical, Task-Assistive Information](#toc-pitfall-2-hiding-critical-task-assistive-information-5)
- [Pitfall #3: Interrupting the Task Flow](#toc-pitfall-3-interrupting-the-task-flow-6)

## What Is an Info Tip?

> An **information (info) tip** is a brief, contextual message designed to offer supplemental information about a specific interface element or step in a workflow.

It’s typically activated by hovering over or clicking on a small icon — often a lowercase *i* or a question mark — and is attached to a specific element within the interface (e.g., a text field, icon, button, label).

![Hovering over a ? on a form reveals a popup that says "It is recommended that you select the sex that appears on the majority of other legal documents, such as a driver's license or Social Security card. The information entered is for benefit application purposes only and required by carriers in order to allow enrollment."](https://media.nngroup.com/media/editor/2026/01/22/infotip1.png)

*✅ An example of a useful info tip from the Ease Employment Benefits Portal: Clicking on the*?*icon reveals a concise explanation about why specific data is collected and how it’s used.*

Info tips can be revealed through two primary patterns:

- [Tooltips](https://www.nngroup.com/articles/tooltip-guidelines/), which appear on mouse- or keyboard-hover gestures within desktop sites
- **Popup tips,** which are similar to tooltips, but are triggered by clicking or tapping an element’s associated icon

Both types serve the same core purpose: providing extra context to those who need additional clarification or guidance without overwhelming the interface with text.

## Representing Info Tips in User Interfaces

### The i Icon: General Information

The encircled lowercase *i* icon is broadly understood to indicate optional, helpful information.

In our [icon-related research](https://www.nngroup.com/books/digital-icons-that-work/), participants interpreted the *i* icon primarily as representing an option for “more information” and expected it to reveal supplemental information such as:

- Definitions
- Additional details or brief explanations
- Promotional terms

This makes the *i* icon ** a good fit for general information or nice-to-know guidance**, but not urgent or error-related content. It is a solid choice for representing info tips that support user understanding without interrupting flow.

### The ? Icon: Help and Support

The encircled **question-mark icon (****?****)** is also used frequently to trigger info tips. In our research, it was more **strongly associated with help and support** than with general supplemental information.

People expected this icon to lead to:

- FAQs
- Customer-support contact information
- Help content or tutorials

However, when placed directly next to a specific interface element (such as the form field label in the example above) the *?* icon is also an effective trigger for contextual help about a specific element. The key is [proximity](https://www.nngroup.com/articles/gestalt-proximity/): When the icon is close to what it refers to, users interpret the help as local and relevant, rather than global or generic.

## The Problem with Info Tips

Unfortunately, info tips are often abused as band aids in the interface, used to:

- Cram in explanations that should’ve been designed into the UI
- Hide critical instructions in the name of a “clean” interface
- Offload poor labeling or [UX copywriting](https://www.nngroup.com/articles/microcontent-how-to-write-headlines-page-titles-and-subject-lines/) onto the user

**Info tips are not a catch-all solution for decluttering the interface** by sweeping essential content into a hidden layer. Nor should they be used to bury large amounts of information that disrupt users’ flow when revealed — what we call the “jump scare” scenario, where a user expects a quick tip but gets an entire modal or screen takeover instead.

**But info tips aren’t inherently bad.** When well-implemented, they offer concise, helpful, and contextual information that improves usability without cluttering the interface.

Well-crafted info tips can:

- Clarify jargon or technical terms
- Explain why specific data is requested
- Guide users to locate needed information
- Reassure users about data usage

However, a good rule of thumb is to assume that **most users will never see the info tip.** Those who do have extra motivation for seeking them out are confused, stuck, or need clarification or reassurance. That’s why info tips should deliver clear, in-the-moment guidance that directly supports the user's immediate task.

## Pitfalls of Bad Info Tips

Info-tip misuse generally falls into three categories:

1. **Wasting users’ time:** Displaying obvious, redundant, or irrelevant information
2. **Hiding critical information:** Burying essential guidance or constraints most users will need upfront
3. **Interrupting the task flow:** Using intrusive patterns such as modals or overlays that take users away from the task at hand

### Pitfall #1: Wasting Users’ Time

Every info-tip interaction — even just that one small click or hover — incurs a small but real [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/). Redundant or obvious tips waste users’ time and undermine trust.

**Don’t use info tips for:**

- Marketing fluff
- Restating visible content or instructions
- Reexplaining the obvious

Info-tip icons like the *i* or *?* signal to users that something might be unclear or needs elaboration. When they instead reveal generic marketing fluff, users can feel misled and frustrated.

![A table with an infotip that says "The quickest way for two people to meet" under the row "Schedule 1:1".](https://media.nngroup.com/media/editor/2026/01/22/infotips2.png)

*❌ Doodle.com: The info tip displays marketing information (* The quickest way for two people to meet)*to further sell the* Schedule 1:1s *feature.*

Info tips also waste time when they restate what’s already perfectly clear in the interface. These tips give the illusion that additional explanation exists, but deliver only repetition.

![Info tip for "City of Birth" field says "Enter your city of birth."](https://media.nngroup.com/media/editor/2026/01/22/infotip3.png)

❌ *State.gov: Clicking the* i *icon next to the* City of Birth *form field triggers the message:* Enter the city of your birth.*These tips simply repeat what's already on the screen, making users feel like there's more to learn when there isn’t.*

![On a page for selecting printer settings including preferred paper type like "satin" or "glossy" the infotip says "Choose your preferred paper type from the options below."](https://media.nngroup.com/media/editor/2026/01/22/infotips4.png)

*❌ In this example, a*? *icon next to* Paper Type *appears promising. Users might expect guidance on how to choose between options like* Satin *,*Gloss*, or *Uncoated*. Instead, it produces an obvious, unhelpful message:*Choose your preferred paper type from the options below.

## Pitfall #2: Hiding Critical, Task-Assistive Information

Info tips should not be used to bury essential instructions, constraints, or legal disclaimers. Doing so turns important guidance into a game of hide-and-seek and could even be a [deceptive pattern](https://www.nngroup.com/articles/deceptive-patterns/) in some cases.

**Avoid putting in info tips:**

- Constraints or rules
- Form-field limitations (e.g., character limits)
- Legal agreements or disclaimers
- Complex instructions or explanations

Complex instructions that help users make decisions should be visible, not hidden in a tip. People need to reference these explanations while completing tasks, not break their flow or current view to search for guidance.

![Pop up near a name on Find a Grave says "This record may be a match for someone in your tree. Decide how likely by reviewing the record information on this page.  Choose Yes if it aligns with what you know about the person to get more details and save the record.  Choose No if it's not for the person in your tree and the hint will be ignored.  Choose Maybe if you're undecided and the hint will be saved for evaluation later."](https://media.nngroup.com/media/editor/2026/01/22/infotips5.png)

*❌ U.S. Find a Grave Index: These complex explanations for proceeding with a simple task are too overwhelming for an info tip. If a task truly requires this much upfront guidance, the information should be integrated directly into the interface, where it’s always visible and easy to reference.*

Instead of hiding complex instructions in an info tip, it’s more effective to display key information at the primary level of the interface. When users must weigh multiple options or make nuanced choices, surfacing that guidance upfront enables quick comparison without disrupting task flow.

![3 selections for output types that clearly list them and explain them in the same view.](https://media.nngroup.com/media/editor/2026/01/22/infotips6.png)

✅ *Microsoft Test and Learn: The design provides clear, inline explanations for the various output types (* Result Grid *,*Trend Chart*, and *Category Impact*) without requiring multiple clicks or hovers to reveal. This approach helps users compare outputs and quickly make an informed decision without having to hunt down hidden descriptions.*

Additionally, any constraints, rules, or limitations for inputs should be displayed on the primary level.

![Infotip that says to not put special characters into the form.](https://media.nngroup.com/media/editor/2026/01/22/infotips7.png)

*❌ USPS.com: The form field hides character constraints within an info tip. This information should be displayed on the primary level. If the form fails due to unseen constraints, users are left frustrated and rework is required.*

## Pitfall #3: Interrupting the Task Flow

People expect clicking an information icon to reveal brief, helpful messages that they can reference in the context of their current workflow — not modal windows or full-page takeovers of walls of text.

**Don’t surprise users with:**

- Overly complex, verbose content
- Modals or overlays that block their task
- New pages that take them away from the workflow

When possible, ensure that info tips are displayed inline or adjacent to the relevant element. Obscuring the current step or view of the interface makes it harder for users to connect the guidance with the task at hand.

![Payment amount screen beside “Amount Options” help popup listing Other Amount, statement balance, current balance, last posted, minimum payment.](https://media.nngroup.com/media/editor/2026/01/22/infotips10.png)

*❌ CapitalOne mobile site: Clicking the* i *icon next to* About payment options *replaces the current view with several explanations of the different amount options. While the information is useful, the pattern disconnects users from the content they need to reference while comparing options.*

Modals and full-page overlays are jarring when used for info tips. Keeping the guidance adjacent to the element it supports allows users to maintain context and better understand the relevance of the information.

![Meals & Incidentals (M&IE) rates table for federal travel. Infotip on the option for "First & Last Day of Travel".](https://media.nngroup.com/media/editor/2026/01/22/infotips11.png)

*❌ GSA.gov (1 of 2): Users are likely to expect that clicking the* i *icon next* to First & Last Day of Travel *will reveal a brief definition of the term as defined in the travel policy.*

![Pop-up titled “First & Last Day of Travel” explaining federal employees receive 75% of the daily amount for the first and last calendar day of travel and darkening the rest of the screen.](https://media.nngroup.com/media/editor/2026/01/22/infotips12.png)

*❌ GSA.gov (2 of 2): Instead, clicking the icon triggers a darkened overlay that obscures the workflow and a surprising modal dialog at the top of the page.*

Even more disruptive is launching an entirely new page from what appears to be a simple info-tip icon. This approach not only obscures the context but also forces users to abandon their task.

![Sign in screen with an infotip next to "Sign-in Code."](https://media.nngroup.com/media/editor/2026/01/22/infotips13.png)

*❌ Nextdoor.com (1 of 2): The site displays a*?*icon next to the* Sign-in code *field label. Users are likely to expect that clicking the icon will display a brief description of what a signin code is or where to find it.*

![A new page that explains the sign-in code process. It has a lot of text like a full article.](https://media.nngroup.com/media/editor/2026/01/22/infotips14.png)

*❌ Nextdoor.com (2 of 2): Instead, clicking the*?*icon next to the* Sign-in code *field launches a new page containing a full explanation of two-step verification. The information about where to find the signin code is buried within the verbose content.*

### Conclusion: Use Info Tips Wisely

Info tips can enhance clarity when they offer just-in-time, supplemental guidance within the context of the current workflow.

**Do:**

- Use info tips for supplemental content
- Keep them short, contextual, and easy to dismiss
- Represent them with familiar icons (*i* or *?*)
- Assume users who activate them need quick, in-the-moment guidance

**Don’t:**

- Hide essential or frequently needed information
- Use info tips as a crutch for poor labeling or dense layouts
- Trigger popups or overlays that hijack the user’s focus or flow

When thoughtfully implemented, info tips reduce confusion and increase user confidence. But they should always serve the user’s goals, not the designer's desire to declutter at all costs.
