---
type: source
name: "Modal & Nonmodal Dialogs: When (& When Not) to Use Them"
created: 2026-07-30
published: 2017-04-23
source_type: article
status: processed
url: https://www.nngroup.com/articles/modal-nonmodal-dialog/
author: Therese Fessenden
raw: raw/sources/2017-04-23_modal-nonmodal-dialog.md
concepts:
  - "Dialog Design"
  - "Design Patterns"
  - "User Interruption"
  - "Information Architecture"
---

# Modal & Nonmodal Dialogs: When (& When Not) to Use Them

## Summary

Modal dialogs force system mode changes that disable background content and require immediate user interaction, while nonmodal dialogs allow continued interaction with main content. Modal dialogs are appropriate for critical errors, irreversible actions, necessary information requests, and workflow fragmentation, but their drawbacks (interruption, context loss, increased cognitive load) make them inappropriate for nonessential information. The article provides seven guidelines for appropriate modal use and explains when nonmodal dialogs or other interface patterns are better choices.

## Key Takeaways

- **Modal dialogs interrupt workflow** — They force mode changes, interrupt task flow, impose cognitive load, create extra interaction goals (dismissing the dialog), and block background content, making them costly for users.
- **Use for critical errors only** — Modal dialogs suit error prevention when mistakes are irreversible (file overwrite, unsaved work loss) or when the error is easier to fix with user attention than within main content.
- **Use for required information** — Request critical information needed to continue user-initiated processes, such as login credentials when required to complete a task.
- **Fragment complex workflows appropriately** — Modals can break complex tasks into digestible steps (wizards), but multiple-step modals prolong interruption; dedicated pages often work better.
- **Streamline information requests** — Modals work when requested information significantly lessens user effort and follows workflow expectations; use progressive disclosure to ask one focused question at a time.
- **Avoid nonessential information** — Never use modals for marketing (newsletter signups), upsells, or information unrelated to user goals; these damage trust and decrease attention to future modals (boy-who-cried-wolf effect).
- **Never interrupt high-stakes processes** — Checkout flows particularly suffer from unnecessary modals that distract or make users feel pressured, potentially affecting purchase decisions.

## Quotes

> A dialog that appears on top of the main content and moves the system into a special mode requiring user interaction. This dialog disables the main content until the user explicitly interacts with the modal dialog.

> Modal dialogs were originally intended to alert users to an error or to some other system state that required immediate user action. In these cases, it was essential for users to be interrupted in order to fix the error.

> No one likes to be interrupted, but if you must, make sure it's worth the cost.

## Concepts

- [[Dialog Design]] — Distinguishes modal and nonmodal patterns, explaining when each is appropriate and the trade-offs of interrupting user workflows with modal interactions.
- [[Design Patterns]] — Discusses how modals function as system mode changes, affecting what commands work and what users can do; related to affordances and user mental models.
- [[User Interruption]] — Core concern showing how modals impose cognitive load, context loss, and workflow disruption costs that must justify their use for critical tasks only.
- [[Information Architecture]] — Shows how information priority and task criticality should determine whether dialogs are modal or nonmodal, and whether dialogs are appropriate at all.
