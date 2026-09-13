---
type: source
name: "Marking Required Fields in Forms"
created: 2026-07-30
published: 2019-06-16
source_type: article
status: processed
url: https://www.nngroup.com/articles/required-fields/
author: Raluca Budiu
raw: raw/sources/2019-06-16_required-fields.md
concepts:
  - Form Design
  - Required Fields
  - Cognitive Load
---

# Marking Required Fields in Forms

## Summary

Marking required fields in forms is essential for reducing user cognitive load and interaction cost. Many designers attempt to avoid marking required fields by showing a single instruction at the form top (e.g., "All fields required") or marking only optional fields, but users do not read these instructions reliably and may forget them. Users must then scan the form or make assumptions, slowing their interaction. Best practice is to mark all required fields explicitly (typically with an asterisk or the word "required"), optionally mark optional fields as well, and ensure visual distinction through color or positioning. For login forms, marking is optional because users expect both fields to be required, but registration forms should always mark required fields unless the form is explicitly limited to username and password.

## Key Takeaways

- **Mark All Required Fields** — users do not reliably read top-of-form instructions and increased cognitive load; explicit marking on each field removes ambiguity and reduces interaction cost.
- **Visual Distinction Matters** — use an asterisk or the word "required" in a contrasting color (red is expected on the web) and sufficient contrast to be accessible; place it at the beginning of the label to aid scanning.
- **Mark Optional Fields Too** — while not mandatory, marking optional fields lightens cognitive load by eliminating the need for users to infer optionality from unmarked neighbors.
- **Login Forms Are Special** — users expect both fields to be required; marking is optional but does no harm and may aid accessibility.
- **Registration Forms Require Marking** — registration forms vary by site, so marking required fields (including username and password) is essential to guide users accurately.

## Quotes

> It's well known that users don't read instructions, and they are particularly less likely to read instructions at the top of a form. Form fields seem self-sufficient — after all, each field has a specific instruction — its label, why would you need to read anything else to fill it in?

> If the word optional is next to the field descriptor, that task becomes a tad easier. Not specifying that a field is optional is not a deal breaker, but doing so is a nice perk.

> In HTML 5, it is possible to add markup to the form field to instruct screen readers to say the word "required" whenever they encounter an asterisk next to the field label.

## Concepts

- [[Form Design]] — required field marking is a critical usability feature for forms, influencing error rates, completion rates, and user trust.
- [[Required Fields]] — explicit marking of required fields (via asterisk or word label) with visual distinction and sufficient contrast reduces user errors and abandoned forms.
- [[Cognitive Load]] — reducing the need for users to remember whether fields are required or scan for optional-field markers minimizes working-memory burden during form completion.
