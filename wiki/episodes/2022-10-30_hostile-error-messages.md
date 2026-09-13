---
type: source
name: "Hostile Patterns in Error Messages"
created: 2026-07-30
published: 2022-10-30
source_type: article
status: processed
url: https://www.nngroup.com/articles/hostile-error-messages/
author: Kate Kaplan
raw: raw/sources/2022-10-30_hostile-error-messages.md
concepts:
  - "Error Messages"
  - "Form Design"
  - "Visual Hierarchy"
  - "Usability Heuristics"
---

# Hostile Patterns in Error Messages

## Summary

While error prevention and recovery are established usability heuristics, some well-intentioned designs overreach by using overly aggressive patterns that frustrate rather than assist users. This article examines two common hostile error patterns: premature error messages displayed before users commit actual errors, and overuse of error-like visual treatments for non-error situations.

Premature error messages occur when systems display errors as users begin typing, before they've had a chance to complete a field or make a genuine mistake. Examples include phone-number fields showing errors on the first digit, email fields displaying "Invalid email address" as soon as a letter is typed, or forms showing required-field errors before user interaction. Error-like visual treatments (red text, caution symbols, warning icons) should be reserved for critical errors, not for routine status messages. Overuse of error styling for non-critical information creates false alarms and disrupts users' workflow unnecessarily. The article recommends waiting until users move away from a field before validating format, reserving error styling exclusively for actual errors, and using asterisks or the word "required" to mark required fields without aggressive visual treatments.

## Key Takeaways

- **Display errors only after users have truly made a mistake** — avoid showing errors while users are still typing; wait until they move to the next field or attempt submission.
- **Avoid errors on field focus or form load** — displaying errors when users click a field or before they interact demonstrates no actual mistake; this feels like scolding.
- **Reserve error styling for actual errors only** — red text, caution icons, and warning symbols should indicate critical failures, not routine status messages or noncritical information.
- **Use a single, simple required-field indicator** — an asterisk or the word "required" suffices; multiple redundant indicators (asterisk, icon, red outline, inline message) create visual noise and feel combative.
- **Provide clear recovery paths for actual errors** — when errors occur, explain what went wrong and how to fix it; errors that blame users without solutions are especially frustrating.

## Quotes

> "These aggressive strategies for error prevention and recovery are akin to standing over the shoulder of a user and shouting " YOU ARE DOING IT WRONG! " during a workflow."

> "Displaying error messages while the user types feels like an unwarranted scolding and can be irritating."

> "Bottom line: Let's assist users, not admonish them."

## Concepts

- [[Error Messages]] — effective error messages appear only after actual mistakes and provide clear recovery paths; premature messages feel like scolding and frustrate users still completing form fields.
- [[Form Design]] — required-field indicators should be subtle and consistent; excessive visual treatments (multiple asterisks, icons, colored outlines, inline messages) increase cognitive load without improving clarity.
- [[Visual Hierarchy]] — error-like styling should be reserved for critical system failures; overusing red, caution icons, and warnings on noncritical messages desensitizes users and creates false alarms.
- [[Usability Heuristics]] — Nielsen's heuristics #5 (error prevention) and #9 (error recovery) support users when applied thoughtfully; aggressive application violates heuristic #8 (aesthetic and minimalistic design).
