---
type: concept
name: Heuristic Evaluation
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Expert Review"
  - "Usability Inspection"
---

# Heuristic Evaluation

## Definition

A heuristic evaluation is a systematic usability-inspection method in which
evaluators assess a design against established guidelines — heuristics — to
identify problems without testing with users
[[2023-06-25_how-to-conduct-a-heuristic-evaluation]]. The heuristics themselves are
broad, research-backed rules of thumb for guiding design decisions and evaluating
usability; they apply to any interface regardless of the organization, and they
give teams a shared vocabulary for discussing issues, which distinguishes them from
design principles (value statements specific to a product), design patterns
(standardized reusable solutions) and team charters (agreements about how a team
works) [[2025-04-18_design-guidance]].

This page also gathers the family of inspection methods that share the same
premise — reviewer expertise instead of participants
[[2022-02-13_cognitive-walkthroughs]]. **Expert reviews** apply broader expertise
and past experience rather than referencing a fixed guideline set
[[2018-02-25_ux-expert-reviews]]; **cognitive walkthroughs** are task-based group
inspections focused specifically on learnability for new users
[[2022-02-13_cognitive-walkthroughs]], [[2022-04-10_cognitive-walkthrough-workshop]];
**PURE** turns expert judgment into a comparable numeric score
[[2017-04-16_pure-method]]; and **competitive evaluations** apply expert review
across several products at once [[2024-01-05_competitive-usability-evaluations]].
The whole family shares one economic argument — it finds likely issues without
having to test with participants, which stretches a limited research budget
[[2023-06-25_how-to-conduct-a-heuristic-evaluation]],
[[2022-04-10_cognitive-walkthrough-workshop]] — and one shared limitation: it never
replaces user research [[2023-06-25_how-to-conduct-a-heuristic-evaluation]].

## Practice

### Running a heuristic evaluation

Use three to five evaluators who assess the design **independently** before
consolidating findings; multiple independent evaluators find more issues than one,
bringing diverse perspectives and cancelling individual blind spots
[[2023-06-25_how-to-conduct-a-heuristic-evaluation]]. Start from Jakob Nielsen's ten
heuristics, widely adopted and grounded in human behaviour and psychology, and
supplement them with domain-specific heuristics where needed
[[2023-06-25_how-to-conduct-a-heuristic-evaluation]]. Narrow the scope — to
specific tasks, sections, user groups or device types — so evaluators are not
overwhelmed and findings stay detailed and actionable
[[2023-06-25_how-to-conduct-a-heuristic-evaluation]].

The single most important interpretive rule: a heuristic violation is not
automatically a problem. Whether it needs fixing depends on the context and the
available alternatives, and user research is what validates whether a violation
actually harms usability
[[2023-06-25_how-to-conduct-a-heuristic-evaluation]].

### Expert reviews

An expert review is conducted by a UX professional with deep knowledge of usability
principles and extensive research experience — and that research experience is a
prerequisite, not a bonus: designing in a vacuum without ever seeing the target
audience interact does not build the expertise needed to review interfaces
[[2018-02-25_ux-expert-reviews]]. The reviewer should be **external to the design
team**, for the same reason people cannot proofread their own writing: the mind
sees what it intended, not what is on the page
[[2018-02-25_ux-expert-reviews]].

A thorough review delivers a list of strengths as well as problems, severity
ratings, recommendations grounded in usability principles, and examples of best
practice addressing similar issues. Every issue must be explained by reference to
UX principles or research, never as bare opinion — that is what makes findings
actionable and avoids designer-versus-reviewer opinion wars. Reviews can happen at
any stage where a prototype exists, but are best placed before major redesigns and
run iteratively during the creative phase, while changes are still cheap
[[2018-02-25_ux-expert-reviews]].

### Cognitive walkthroughs

A cognitive walkthrough is a task-based inspection in which a cross-functional team
walks each step of a task flow and answers four prescribed questions: will users
try to achieve the right result; will they notice the correct action is available;
will they associate that action with the desired result; and will they see progress
toward their goal after acting
[[2022-02-13_cognitive-walkthroughs]],
[[2022-04-10_cognitive-walkthrough-workshop]]. The method comes from Clayton Lewis
and colleagues in 1990, built for walk-up-and-use interfaces such as kiosks and
ATMs where using the interface with no prior training is critical, and was later
streamlined by Cathleen Wharton and colleagues for any interface type; it rests on
the CE+ model of how people learn interfaces through exploration and problem
solving [[2022-02-13_cognitive-walkthroughs]].

Practical setup: 2–6 evaluators of diverse roles (product experts, UX
practitioners, engineers, domain experts), one facilitator driving and one recorder
documenting; define the action sequence explicitly before the session to keep the
group on track; remind everyone of the ground rules during the walkthrough; and
when a step fails, assume success and carry on so that all subsequent problems are
still found. Two full tasks fit in a 90-minute session with proper preparation
[[2022-04-10_cognitive-walkthrough-workshop]],
[[2022-02-13_cognitive-walkthroughs]].

Fit matters: walkthroughs excel on complex, new or unfamiliar workflows where users
have no existing mental model, and are overkill for standard web patterns everyone
already knows. They are best used early, on conceptual prototypes, to catch
fundamental learnability problems [[2022-02-13_cognitive-walkthroughs]].

### Turning expert judgment into a score: PURE

PURE (Pragmatic Usability Rating by Experts) has usability experts assign
quantitative ratings against a set of criteria and combine them into a final score
with a visual representation. Three experts rate each step silently on a 1–3 scale
reflecting cognitive load and task difficulty, then discuss and agree — the silent
pass followed by discussion is what produces reliable, valid results at a fraction
of benchmarking cost. Scores represent **friction**, the opposite of ease of use:
green (easy), yellow (moderate effort), red (difficult or failure-prone), and a
single red step colours the whole product, flagging a critical failure point. Target
interrater reliability is 0.667 or above, typically 0.8–0.9 after training;
disagreement is treated as a signal that evaluators hold different assumptions,
which must be surfaced and resolved [[2017-04-16_pure-method]].

Scope it to 3–20 fundamental tasks — those essential to the business or to core user
needs — rather than every possible path, and score the happy path, the optimal flow
for target users, so improvement effort concentrates on the best case before
alternatives. Because the same fundamental tasks and target audiences can be scored
across versions and across products, PURE enables direct competitive and iterative
comparison, and a simple numeric representation of ease of use tends to motivate
business stakeholders to set improvement goals [[2017-04-16_pure-method]].

### Competitive evaluation by expert review

Competitive evaluations assess whether a design is better or worse than competitors
and surface the relative strengths and weaknesses of each. They can be run as
expert reviews across multiple products or as usability tests with users completing
tasks on competing designs; the expert-review route is the cost-effective one, and
experienced reviewers identify trends, patterns, gaps in content or functionality,
and approaches worth borrowing. Focus on 2–4 competitors, chosen for similar
content and functionality, best overall experience, innovative design, strongest
competition, and whoever customers actually compare you against. Learn from
well-designed competitors, who may have solved the same problem through their own
iteration, as much as from poorly designed ones. When testing with users instead,
participants typically cover 2–3 sites, with alternating order and site pairs to
prevent learnability effects, and asking them to compare adds insight. The goal is
not to declare a winner but to improve your own design: you want to beat the
competition, not copy them [[2024-01-05_competitive-usability-evaluations]].

### Inspection and testing are complementary, not substitutes

Expert reviews find different issues than usability testing, which is why combining
them produces the best overall design: a review catches minor inconsistencies and
best-practice violations that a small qualitative study would not surface —
inconsistent font usage, an off-brand colour, centre-aligned text where left-aligned
belongs — while testing reveals problems specific to the target audience
[[2018-02-25_ux-expert-reviews]]. Heuristic evaluation is explicitly limited by
evaluator bias and cannot replace user research; its value is finding obvious
problems early and building UX evaluation skills
[[2023-06-25_how-to-conduct-a-heuristic-evaluation]]. Cognitive walkthroughs paired
with usability testing likewise give comprehensive evaluation without costly formal
studies [[2022-02-13_cognitive-walkthroughs]]. And practice compounds: the more
evaluations you conduct, the less you rely on the explicit heuristics, developing
instincts that recognize usability problems quickly
[[2023-06-25_how-to-conduct-a-heuristic-evaluation]].

### The heuristics themselves

Heuristics are one layer in a hierarchy of design guidance: principles sit on top as
guiding philosophy, heuristics provide the research-backed assessment framework,
patterns supply concrete tactical solutions, and team charters govern how the team
works together [[2025-04-18_design-guidance]]. Individual heuristics are applied
directly in practice — error-message design is governed by "Help Users Recognize,
Diagnose, and Recover from Errors", with visibility (errors displayed near their
source, redundant indicators combining colour, text, icons and animation since
colour alone fails users with colour-vision deficiencies, and no premature errors on
exploratory interactions), communication (plain human-readable language, no jargon
or error codes, constructive suggested remedies, a positive tone that avoids
"invalid" or "incorrect"), and efficiency (preserve user input, reduce correction
effort, prevent common mistakes). Poor error handling is common precisely because
teams focus on the ideal path instead of the deviations
[[2023-05-15_error-message-guidelines]].

The corpus also records that the set is durable but not frozen: 90% of the
heuristics remain valid after 28 years, while specific guidelines can change as
human memory and technology evolve — a point made in an article that is itself an
April Fools' hoax, arguing satirically for recall over recognition and inviting
readers to notice where they stopped believing it. Recognition over recall remains
the correct guidance [[2022-04-01_recall-beats-recognition]].

## Sources (10)

- [[2017-04-16_pure-method]] — Uses structured expert panel evaluation with silent individual ratings followed by group discussion to produce reliable, validated scores.
- [[2018-02-25_ux-expert-reviews]] — systematically assessing designs against established usability heuristics and best practices to uncover violations, employing expert analysis as a complement to user testing for comprehensive evaluation of design quality.
- [[2022-02-13_cognitive-walkthroughs]] — Cognitive walkthroughs are one of several inspection methods (alongside heuristic evaluations and expert reviews) using reviewer expertise to identify problems without involving actual users.
- [[2022-04-01_recall-beats-recognition]] — the durability and occasional evolution of Nielsen's 10 usability heuristics over time.
- [[2022-04-10_cognitive-walkthrough-workshop]] — an expert-based evaluation method that identifies usability issues without requiring users.
- [[2023-05-15_error-message-guidelines]] — The foundational usability heuristics including Nielsen's principle to "Help Users Recognize, Diagnose, and Recover from Errors" that guide error-message design.
- [[2023-06-25_how-to-conduct-a-heuristic-evaluation]] — the article provides comprehensive guidance on applying this specific inspection method effectively at different project stages.
- [[2024-01-05_competitive-usability-evaluations]] — expert reviewers can conduct competitive reviews more cost-effectively than testing, identifying trends and opportunities across multiple competitors.
- [[2025-04-18_design-guidance]] — applies research-backed best practices as a framework for assessing interface usability independent of organization-specific principles.
- [[2013-08-01_just-enough-research_08-chapter-7-evaluative-research]] — The chapter introduces heuristic analysis based on Nielsen and Molich's 1990 framework: expert evaluators assess a design against ten usability principles (visibility, system-world match, control, consistency, error prevention, recognition, flexibility, aesthetics, error recovery, help). It is quick and cheap but may miss real-world problems and works best as a sanity check before usability testing.
