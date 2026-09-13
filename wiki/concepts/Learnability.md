---
type: concept
name: Learnability
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "AI Learnability"
  - "Learning Curves"
---

# Learnability

## Definition

Learnability is one of the quality components of usability: how easily users can
accomplish a task the first time they meet an interface, and how many repetitions
it takes them to become efficient at it [[2019-10-20_measure-learnability]]. It is
distinct from efficiency, which describes performance once learning is over. The
underlying regularity is the power law of learning: the time to perform a task
decreases with the number of repetitions, and the decrease follows the shape of a
power law, a pattern that holds across a very large body of human-factors
experiments [[2016-10-30_power-law-learning]].

Because learning is driven by repetition, learnability is not a property of a
screen in isolation but of the relationship between a design and the practice a
user has already accumulated — on other sites, on other products, and on the
product itself. Familiar patterns inherit that practice; novel or invisible ones
restart the curve [[2016-10-30_power-law-learning]] [[2021-01-10_consistency-and-standards]]
[[2017-12-03_iphone-x]]. Applied to AI systems, the same question becomes how
easily users can understand what the system can do at all, and how to address it
effectively [[2025-06-27_designing-use-case-prompt-suggestions]].

## Practice

### Three aspects to distinguish

[[2019-10-20_measure-learnability]] separates three things that "learnability"
can mean, each mattering for a different audience: first-use ease (decisive for
one-time tasks), the steepness of the curve (how fast users improve), and the
efficiency of the ultimate plateau (speed at full mastery).
[[2016-10-30_power-law-learning]] adds that saturation points vary by design:
design A may be learnable quickly, while design B only outperforms it after more
practice. Steep curves are good; shallow curves signal poor learnability.

There is a real trade-off here, and both articles name it. Systems optimized for
easy first use — wizards, for example — may plateau early and feel inefficient to
experienced users; the balance depends on the business value of the different
user groups [[2019-10-20_measure-learnability]].

### Measuring learnability

[[2019-10-20_measure-learnability]] gives the quantitative method: recruit 30-40
participants with little prior experience, measure time-on-task across multiple
trials until the plateau is reached, randomise task order to avoid bias, and run
statistical significance testing. Plot the curve to see whether users actually
reach saturation. Such studies pay off for complex systems used frequently; they
are not cost-effective for one-time tasks such as signing up or filing taxes,
where every user behaves as a novice anyway. The article also notes that even
without running a full study, thinking in these terms sharpens design trade-offs.

### Evaluating learnability without users

Cognitive walkthroughs evaluate learnability from a new user's perspective
without involving actual users, which makes them cheap and usable on early
conceptual prototypes [[2022-02-13_cognitive-walkthroughs]]
[[2022-04-10_cognitive-walkthrough-workshop]]. A cross-functional team walks each
step of a task flow and answers four prescribed questions: will users try to
achieve the right result, will they notice the correct action is available, will
they associate the action with the desired result, and will they see progress
after acting. The method comes from the CE+ model of how people learn interfaces
through exploration and problem solving, and was built for walk-up-and-use
interfaces such as kiosks and ATMs [[2022-02-13_cognitive-walkthroughs]].

Practical constraints from [[2022-04-10_cognitive-walkthrough-workshop]]: 2-6
evaluators of diverse roles, an explicitly defined action sequence prepared
before the session, a facilitator and a recorder, assume success when a step
fails so the analysis can continue, and roughly two full tasks per 90-minute
session. Both articles scope the method: it excels on complex, new or unfamiliar
workflows where users have no existing mental model, and is overkill for standard
web patterns everyone already knows [[2022-02-13_cognitive-walkthroughs]].
Paired with usability testing it gives broad coverage without a costly formal
study.

### Designing for learnability: reuse existing practice

Consistency is the cheapest source of learnability. By using standard patterns a
designer gives users one more repetition of an element they have already
practised on dozens of other sites [[2016-10-30_power-law-learning]].
[[2021-01-10_consistency-and-standards]] frames this as the fourth usability
heuristic and splits it in two: internal consistency (uniform patterns within a
product or product family) and external consistency (established web and platform
conventions). Jakob's Law underlies the second — people spend most of their time
on sites other than yours and arrive with those expectations. Consistency is
needed across several layers: visual (icons, imagery), page and button layout,
the format of user-entered data, and tone of voice. It does not happen by itself:
design reviews, consistency audits and design systems are what maintain it.
Breaking a convention adds cognitive load and should only be done when it is
necessary to the task or significantly improves efficiency.

### The cost of innovation and of invisibility

[[2016-10-30_power-law-learning]] sets three conditions for deviating from a
standard: the new design must perform substantially better once learned, users
must encounter it often enough to reach saturation, or the brand's perceived
value must justify the learning investment. Frequency is the deciding variable —
daily interaction, or an update imposed on a captive audience, builds practice
fast; occasional users may abandon the new design before ever benefiting.

[[2017-12-03_iphone-x]] applies exactly this reasoning to gesture navigation.
Gestures are invisible, so they are hard to remember and hard to remember to use;
gesture-heavy apps praised by the design community, such as Clear Todos and
Mailbox, never succeeded with general users. The iPhone X compounds the problem
with swipe ambiguity: the same swipe means different things depending on
location, length and direction. Two things rescue it — the visible home line
acting as a signifier for the critical gesture, which is what Windows 8 lacked,
and the sheer repetition of daily phone use. The article concludes that only
companies with strong brands can push this kind of innovation, since perceived
brand value compensates for the initial learning hurdle.

### Teaching capability, not just controls

For AI systems the learnability problem shifts from "which control does what" to
"what can this thing do". [[2025-06-27_designing-use-case-prompt-suggestions]]
recommends use-case prompt suggestions, calibrated to context: simple clickable
pills for broad systems and low-complexity tasks, richer examples (conversation
replays, video demonstrations) for specialised systems and high-complexity tasks.
For new users, curated pre-authentication suggestions act as lightweight
onboarding; for active users, context-aware suggestions surfaced when they face
ambiguity or lack domain knowledge give just-in-time guidance and reduce
cognitive load. Specific beats vague ("Easy family dinners" over "Recipe ideas"),
individualised beats one-size-fits-all, and placement near the input field
captures attention at the moment of engagement. Analytics can identify which
suggestions drive engagement, provided placement and order biases are controlled
for.

## Sources (7)

- [[2016-10-30_power-law-learning]] — Task performance improvements follow power laws that are consistent across human behavior; understanding learning curves helps predict interface learnability.
- [[2017-12-03_iphone-x]] — The ease with which users acquire proficiency with new interface patterns; invisible gestures are harder to learn than visible buttons, requiring either repeated practice or visual reminders.
- [[2019-10-20_measure-learnability]] — defines learnability as a usability component and provides a framework for measuring it through learning curves, demonstrating how to plot and interpret them to identify performance plateaus, measure saturation, and identify design tradeoffs.
- [[2021-01-10_consistency-and-standards]] — demonstrates how adherence to standards and consistency reduces the learning curve when users encounter new interfaces.
- [[2022-02-13_cognitive-walkthroughs]] — Cognitive walkthroughs specifically evaluate how learnable interfaces are for new users without prior knowledge; focuses on exploration and problem-solving capabilities rather than general usability.
- [[2022-04-10_cognitive-walkthrough-workshop]] — assessing how easily new users can understand and use a system.
- [[2025-06-27_designing-use-case-prompt-suggestions]] — how easily users can understand what an AI system can do and how to interact with it effectively to achieve their goals.
