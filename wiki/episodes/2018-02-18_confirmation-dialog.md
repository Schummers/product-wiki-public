---
type: source
name: "Confirmation Dialogs Can Prevent User Errors — If Not Overused"
created: 2026-07-30
published: 2018-02-18
source_type: article
status: processed
url: https://www.nngroup.com/articles/confirmation-dialog/
author: Jakob Nielsen
raw: raw/sources/2018-02-18_confirmation-dialog.md
concepts:
  - "Error Prevention"
  - "User Interface"
  - "Interaction Design"
---

# Confirmation Dialogs Can Prevent User Errors — If Not Overused

## Summary

Confirmation dialogs provide users a second chance to review their actions before committing to potentially dangerous or irreversible operations. However, overuse of confirmation dialogs leads to automation where users click yes without thinking, defeating their purpose. Effective confirmation dialogs must be specific about consequences, avoid being used for routine actions, and respect user intent rather than interrupt frequently with generic warnings.

## Key Takeaways

- **Core purpose** — confirmation dialogs should allow users a genuine second chance to verify their work before proceeding with serious consequences, but effectiveness requires users actually pay attention to the dialog.
- **Specificity requirement** — dialogs must restate the user's request with identifying details (like filenames or quantities) so users can recognize if they made a mistake; generic questions like "Are you sure?" fail because users will automatically click yes.
- **Severity-based triggering** — use confirmation dialogs only for serious consequences like destroying work or large financial transactions, not routine actions, to prevent habituation where users stop paying attention.
- **Response design** — provide action-specific button labels like "Delete file" and "Keep file" instead of generic "Yes" and "No" buttons, and avoid default yes answers for dangerous operations.
- **Special techniques** — for extremely dangerous operations, require nonstandard user actions like typing a confirmation word (as MailChimp does) to prevent automated behavior, but reserve this for rare situations.

## Quotes

> When users are asked Are you sure you want to do this? without further details, the only sensible reaction is "of course I want to do the thing I just told you to do," and hit Yes without further thinking.

> If you warn people too much, they stop paying attention. If I said this a few more times, you would stop reading.

> Do try your best to offer undo — a key component of another usability heuristic, user control and freedom — in order to reduce anxiety and allow users to recover from major problems.

## Concepts

- [[Error Prevention]] — using confirmation dialogs strategically to catch serious user errors before they cause irreversible harm.
- [[User Interface]] — designing dialogs with specificity, appropriate severity thresholds, and action-specific language to support user intent.
- [[Interaction Design]] — balancing the need to prevent errors against user annoyance by applying confirmation selectively and providing undo alternatives.
