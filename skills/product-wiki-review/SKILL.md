---
name: product-wiki-review
description: |
  Review a design against the product-wiki corpus and report attributed findings, then re-review after fixes. Use when the owner shares a screen, flow, wireframe, prototype, spec or live page and asks to critique it, challenge it, audit it, run a heuristic evaluation, check accessibility, or find what is wrong with it. Also use for the second pass once he has changed something in response.
---

# Review against the product wiki

Runs a design review out of `~/AI OS/compound-learning/product-wiki`, where every rule traces to a
Nielsen Norman Group study or a Parlons Design transcript. The point is an
**attributed** critique: the reader can follow any finding back to the source and
argue with it.

Findings come from the corpus. When something looks wrong and no source in the
corpus supports it, say so and mark it as your own observation, clearly
separated from the sourced findings.

## 1. Frame the artifact

Establish before reading anything: what it is (screen, flow, spec, live URL),
the platform, who uses it, and what stage it is at. A wireframe and a
pre-launch build earn different findings.

Ask only what you cannot see. When the artifact is a URL, open it and look.

**Done when** you can name the artifact, the platform, and the user in one
sentence each.

## 2. Route

Read `wiki/themes/_router.md` and pick the themes this artifact actually
touches. Six themes carry a **playbook**, a distilled list of checkable rules,
and those are the review surface:

- Usability Heuristics and Evaluation
- Page Composition and Hierarchy
- Interaction and Interface Patterns
- Accessibility and Inclusion
- Mobile and Multi-Device
- Structure, Navigation and Findability

Read `wiki/playbooks/<Theme>.md` for each theme in scope. When a theme in scope
has no playbook, open its concept pages through the theme page instead and work
from their `### ` sub-sections.

**Done when** every theme in scope has been read from its playbook, or from its
concept pages where no playbook exists.

## 3. Apply every rule

Walk the rules one at a time and give each an explicit verdict:

| Verdict | Meaning |
|---|---|
| `holds` | the design satisfies it |
| `breached` | it does not, and this is a finding |
| `n/a` | the rule does not apply here, with the reason |

Exhaustiveness is the whole discipline. A review that reports four problems and
silently drops thirty rules tells the reader nothing about the thirty.

**Done when** every rule in every playbook read carries one of the three
verdicts, `n/a` included.

## 4. Report

Findings first, ordered by severity: what breaks a task, then what costs
effort, then what costs polish. Each finding carries:

- what is breached, in one sentence
- where, precisely, in the artifact
- the source: `[[Concept]]` and the `[[record]]` behind it
- what to change instead, phrased as the target rather than the ban

Then the `n/a` rules in a compact list, so the coverage is visible. Then any
unsourced observation of your own, under its own heading.

Where the sources disagree on a point, give both positions and let the owner
decide. Resolving a disagreement the corpus holds open is a fabrication.

**Done when** every breached rule has a location, a source and a target state,
and the `n/a` list is present.

## 5. Second pass

When the reader comes back with a revision, re-review: check the previously
breached rules first, then re-run the rules his change could have affected, and
report regressions as first-class findings. Say which findings are now closed.

**Done when** every previously breached rule has a fresh verdict and any
regression is reported.
