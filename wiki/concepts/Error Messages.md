---
type: concept
name: Error Messages
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Error Handling"
---

# Error Messages

## Definition

An error message is what a system says when something has gone wrong, and its job
is to help users recognize, diagnose and recover from the problem. Handling errors
effectively matters because it is one of the five quality components of usable
experiences, and it is covered by Nielsen's heuristic "Help Users Recognize,
Diagnose, and Recover from Errors" [[2023-05-15_error-message-guidelines]]. Poor
error-message design is common for a structural reason: teams focus on the ideal
user path rather than thoughtfully addressing the deviations from it
[[2023-05-15_error-message-guidelines]].

The stakes are asymmetric. Because of negativity bias, a single usability flaw
weighs more than many positive features, so error messages are critical
touchpoints: courteous and clear ones can mollify a frustrating situation, while
harsh or obscure ones turn a slight inconvenience into an antagonistic encounter
[[2016-10-23_negativity-bias-ux]]. An informative error message is also a
teachable moment: people will not invest time in reading about an app's features,
but they will make the effort to understand an error if it is explained clearly,
because they want to overcome it [[2019-02-17_top-10-application-design-mistakes]].
In a taxonomy of feedback mechanisms, validations are the error-message form tied
specifically to user input, distinct from indicators (passive contextual cues) and
notifications (system events) [[2024-01-17_indicators-validations-notifications]].

## Practice

### Three dimensions: visibility, communication, efficiency

The guidelines cluster into visibility (displaying errors prominently near their
source with accessible indicators), communication (plain language that describes
the problem and offers constructive solutions without blaming users) and
efficiency (preserving user input, reducing correction effort, preventing common
mistakes) [[2023-05-15_error-message-guidelines]]. The same three dimensions
structure a scoring rubric, with four criteria each
[[2023-06-18_error-messages-scoring-rubric]].

### Placement and visibility

Place the error indicator adjacent to the problem field: proximity reduces
cognitive load and helps users associate the message with the specific element
[[2023-05-15_error-message-guidelines]]. Keeping the message next to the field in
error minimises working-memory load, because users can see the message while
fixing the error instead of having to remember it
[[2019-02-03_errors-forms-design-guidelines]]. Do not use tooltips for error
reporting: they hide critical information behind hover or focus, making errors
hard to notice and costly to access [[2019-02-03_errors-forms-design-guidelines]].
Combine redundant indicators (color, text, icons, animation) and remember that
color alone is insufficient for users with color-vision deficiencies
[[2023-05-15_error-message-guidelines]], [[2019-02-03_errors-forms-design-guidelines]].
Match the mechanism to the need: passive notifications used for critical errors get
missed, and indicators should not carry critical feedback
[[2024-01-17_indicators-validations-notifications]].

### Wording

Write in human-readable, plain language matching users' mental models rather than
system implementation details; avoid jargon and technical error codes
[[2023-05-15_error-message-guidelines]]. Do not stop at stating the problem:
explain why the error occurred and how to fix it, since vague "something went
wrong" messages leave users stranded
[[2019-02-17_top-10-application-design-mistakes]], [[2023-05-15_error-message-guidelines]].
Take a positive tone and avoid blame-oriented phrasing like "invalid" or
"incorrect", focusing on what is needed rather than what the user did wrong; the
proper usage of a system lies with its creators, not its users, so the system must
adapt gracefully and not shift blame [[2023-05-15_error-message-guidelines]].
Messages should be explicit, human-readable, polite, precise and constructive
[[2019-02-03_errors-forms-design-guidelines]]. Courtesy is not decoration here: it
is what keeps a recoverable moment from becoming an antagonistic one
[[2016-10-23_negativity-bias-ux]]. In smart-device setup, the specific ask is that
the message explain what went wrong, why, and give concrete next steps, plus
built-in access to support, so users are not pushed into trial-and-error
troubleshooting or abandonment [[2025-09-12_smart-device-onboarding]].

### Timing: the inline-validation tension

Sources agree that errors must not fire while a user is still typing. Showing an
error on the first digit of a phone number, on the first letter of an email field,
or on form load before any interaction demonstrates no actual mistake and feels
like unwarranted scolding; wait until users move away from the field or attempt
submission before validating format [[2022-10-30_hostile-error-messages]]. One
source advises avoiding errors on exploratory interactions such as unfocused text
fields, while reserving inline, real-time errors for genuinely error-prone
situations [[2023-05-15_error-message-guidelines]].

The nuance sits with positive, in-progress feedback rather than errors. Inline
validation is recommended so errors appear as soon as users finish filling a
field, letting them fix mistakes immediately without hunting for the problem
field; and for complex fields with specific requirements, such as passwords,
real-time validation feedback while typing helps users meet the guidelines without
trial and error [[2019-02-03_errors-forms-design-guidelines]]. Read together, the
corpus supports real-time feedback as success or requirement indicators, and
delayed validation for error styling
[[2019-02-03_errors-forms-design-guidelines]], [[2022-10-30_hostile-error-messages]].

### Do not over-signal

Reserve red text, caution symbols and warning icons for actual, critical errors:
using error styling for routine status messages or noncritical information creates
false alarms and desensitises users [[2022-10-30_hostile-error-messages]]. Mark
required fields with a single simple indicator, an asterisk or the word
"required"; stacking asterisk plus icon plus red outline plus inline message
creates visual noise and reads as combative [[2022-10-30_hostile-error-messages]].
The summarising rule from that source: assist users, do not admonish them
[[2022-10-30_hostile-error-messages]].

### Recovery and efficiency

Preserve what the user already entered and reduce the effort required to correct
[[2023-05-15_error-message-guidelines]]. Provide a clear recovery path for every
real error; blaming without a solution is the most frustrating combination
[[2022-10-30_hostile-error-messages]]. When the same error is hit three or more
times in a single form-filling attempt, treat it as a signal of a deeper interface
problem, unclear messaging, a mismatch with users' needs or over-complex
requirements, and give extra help
[[2019-02-03_errors-forms-design-guidelines]]. For catastrophic failures with no
recovery path at all, novelty and humility may be the only way to salvage the
experience [[2023-05-15_error-message-guidelines]].

### Evaluating error messages

A rubric scores each of the twelve criteria from 1 (poor) to 4 (excellent) and
averages them into a letter grade: A for 3.3-4.0, B for 2.5-3.2, C for 1.6-2.4,
D for 1.5 or less. The grade scale is deliberately familiar, so executives and
teams can prioritise UX debt [[2023-06-18_error-messages-scoring-rubric]]. Having
several evaluators score independently before averaging reduces individual bias
and guards against groupthink [[2023-06-18_error-messages-scoring-rubric]]. The
worked examples show the failure modes cluster: Craigslist scores low mainly on
communication and efficiency, Google Flights struggles on visibility, J.Crew
scores well across all three [[2023-06-18_error-messages-scoring-rubric]].

### Beyond the message itself

Some of the work happens before any message appears. Meaningful default values
speed interaction, teach appropriate responses and guide novices toward safe
outcomes; consistency in terminology, control placement and rules prevents the
confusion that generates errors in the first place
[[2019-02-17_top-10-application-design-mistakes]]. Microcopy used strategically,
small bits of contextual copy that instruct or alleviate concerns, prevents
negative impressions from forming at critical moments
[[2016-10-23_negativity-bias-ux]]. And honest progress reporting belongs to the
same trust budget: misleading progress bars that fill without reflecting real
progress destroy confidence, so state what is happening and give realistic
timeframes [[2025-09-12_smart-device-onboarding]].

## Sources (8)

- [[2016-10-23_negativity-bias-ux]] — Error messages are critical touchpoints; courteous, helpful messages can recover a bad situation while harsh ones escalate user frustration.
- [[2019-02-03_errors-forms-design-guidelines]] — Comprehensive framework for designing error correction flows that help users fix mistakes efficiently through clear messaging and strategic error placement.
- [[2019-02-17_top-10-application-design-mistakes]] — Guidelines for writing actionable, human-readable error messages that explain problems clearly and provide constructive guidance for recovery.
- [[2022-10-30_hostile-error-messages]] — effective error messages appear only after actual mistakes and provide clear recovery paths; premature messages feel like scolding and frustrate users still completing form fields.
- [[2023-05-15_error-message-guidelines]] — Designing systems to recognize problems and guide users toward resolution without frustration, through clear messages and helpful recovery paths.
- [[2023-06-18_error-messages-scoring-rubric]] — the rubric provides a structured framework for evaluating one of the most critical but often-overlooked UI elements in user experience.
- [[2024-01-17_indicators-validations-notifications]] — validations are a type of error message tied to user input; they must clearly indicate the problem and suggest solutions.
- [[2025-09-12_smart-device-onboarding]] — Documents best practices for transparent error messages that explain what went wrong, why, suggest actionable next steps, and provide built-in support access without forcing users to abandon the flow.
