---
title: "Project Postmortems for UX Teams: Learning from Success and Failure"
date: "2026-02-27"
url: "https://www.nngroup.com/articles/ux-postmortems/"
author: "Laura Klein"
topics: [ux-design-process, ux-management]
type: article
---

The concept of postmortem is borrowed from engineering teams, who've been using postmortems for years to prevent catastrophic bugs. They’re one of the most underutilized tools in product development. When adapted thoughtfully for UX and product work, they create a systematic way to learn from both our successes and our failures, but most teams either skip them entirely or do them so poorly that they might as well not bother.

Let's fix that.

## In This Article:

- [What Postmortems Are (And Aren't)](#toc-what-postmortems-are-and-arent-1)
- [When to Hold Postmortems](#toc-when-to-hold-postmortems-2)
- [What Belongs in a Postmortem](#toc-what-belongs-in-a-postmortem-3)
- [The Anatomy of a Good Postmortem](#toc-the-anatomy-of-a-good-postmortem-4)
- [UX-Specific Considerations](#toc-ux-specific-considerations-5)
- [Making Postmortems Part of Your Culture](#toc-making-postmortems-part-of-your-culture-6)
- [The Goal: Systematic Improvement](#toc-the-goal-systematic-improvement-7)

## What Postmortems Are (And Aren't)

> A **postmortem** is a structured analysis of a completed project that examines what happened, why it happened, and what systemic changes are needed as a result.

The goal is straightforward: to understand the project thoroughly enough to replicate successes and prevent failures.

Notice I wrote, "completed project," not "failed project." This is the first misconception teams need to overcome. Yes, you should absolutely do a postmortem when your new onboarding flow tanks conversion rates, but you should also do one when your redesigned checkout process increases purchases by 40% instead of the 15% you predicted.

Success often teaches us more than failure, but only if we learn from it.

### How Postmortems Differ from Sprint Retrospectives

If you're doing some form of Agile, you're probably already conducting retrospectives. These happen every sprint and focus on your team’s process: What should we keep doing? What should we stop? What should we try next? They're forward-looking and process-oriented.

If you’re interested in doing effective UX retrospectives (and you should be!), here are some [tips](https://www.nngroup.com/articles/ux-retrospectives/) for how to do them. **Regular retros** can improve your team’s process significantly, but they don’t get rid of the need for **project postmortems.**

Postmortems have some similarities with retrospectives, and a lot of the advice about running them can be used for both events, but they’re different in key ways. Postmortems are backward-looking and outcome-oriented. They examine a specific project after it's complete (or after you have enough data to evaluate it) and ask whether that project succeeded, why or why not, and what we can learn from that outcome.

A sprint retrospective might surface that your team needs better stakeholder communication. A postmortem might reveal that your last product launch failed because you never validated the problem you were solving, and it will result in a new requirement that all future projects include problem validation before entering design.

Both are valuable. Neither replaces the other.

## When to Hold Postmortems

Timing matters more than most teams realize. Hold a postmortem too soon, and you're making decisions without data. Wait too long, and people forget crucial details or move to other teams.

**For projects with measurable outcomes** like experiments, launches, or feature releases, wait until you have enough data to evaluate success. If you're measuring retention over 30 days, don't hold your postmortem on day 2, but don't wait six months either. By then, the team has moved on and the details have faded.

**For projects without clean metrics** (like exploratory research, [design-systems](https://www.nngroup.com/articles/design-systems-101/) work, or process improvements) hold the postmortem within two weeks of completion, while everything is still fresh.

As a general rule: if people are saying "I don't really remember why we decided that," you've waited too long. But if people are saying “We don’t know whether this worked or not,” you’re too early.

## What Belongs in a Postmortem

Let's consider two scenarios, one "failure" and one "success," to understand what a good postmortem looks like.

### Scenario 1: The Failed Metrics Experiment

Your team hypothesized that adding social proof to your product signup page would increase conversion by 30%. You designed variations, ran the experiment properly, and conversion increased by 1%. Essentially, no change.

A postmortem here needs to examine two things: why the experiment failed *and* why you believed it would succeed.

The first question might reveal that your users are enterprise buyers who don't care about consumer social proof, or that the design implementation was too subtle, or that social proof matters, but 30% was wildly optimistic.

The second question — why you believed it would succeed — is often more illuminating. Did you skip user research because you were "pretty sure" about the solution? Did you base the estimate on a competitor's case study without considering how different its users are? Did stakeholder enthusiasm override data? Did a product manager oversell their pet project in order to get their idea shipped?

Understanding your reasoning process helps you fix it. Maybe the deliverable is a new requirement that all experiment hypotheses must be backed by user research. Maybe it's a calibration session for the team on realistic effect sizes. Maybe it's a decision to stop using competitor case studies as primary evidence.

### Scenario 2: The Super Successful Feature

Your team shipped a new dashboard feature that you hoped would improve user engagement. You estimated a 10% increase in daily active users. Instead, you saw 45%, the feature came in two weeks early, and users are requesting similar updates to other areas of the product.

Why did this go so well?

A good postmortem might uncover that the designer had worked in this domain before and deeply understood user workflows, or that you involved users unusually early and ran some initial experiments to validate the direction before shipping the final feature. It might show that you had a stable team with no turnover during the project or that the engineering lead pushed for a technical approach that made iteration faster.

Whatever the reasons, you want to identify them and systematically increase the chances of replicating them. Maybe you create a new practice of bringing in domain experts for complex features. Maybe you insist on validation experiments for strategic projects. Maybe you fight for team stability during important initiatives.

**Success isn't magic.** It has causes, and you can identify them.

## The Anatomy of a Good Postmortem

Here's what you need to make postmortems useful.

### 1. The Right People in the Room

At a minimum, include:

- **Core team members** who worked on the project
- **The product manager** or project owner
- **Key stakeholders** who were involved in decisions
- **Someone from a related team** who can offer outside perspective (*optional*)

Don't invite 30 people. You want enough perspectives to see the full picture but few enough that everyone can contribute meaningfully. Six to ten people is usually right.

### 2. Clear Success Criteria (Ideally Defined Beforehand)

If you didn't define what success looked like at the project's start, the postmortem becomes much harder. You end up arguing about whether a 5% increase was good or whether shipping two weeks late was acceptable.

**Define success metrics upfront** for future projects. For the current postmortem, spend time at the beginning aligning on what you were trying to achieve and how you're measuring it now.

### 3. Psychological Safety

This is critical, especially for projects that didn't go well. If people are afraid they'll be blamed, they won't share honestly, and you won't learn what actually happened.

Make it explicit: "We're here to understand what happened and improve our system, not to blame individuals." Consider having a facilitator who wasn't involved in the project run the session.

When mistakes come up, the question is always "what about our process allowed this mistake to happen?", not "why did this person mess up?" **People make mistakes; systems should catch them.**

### 4. Root-Cause Analysis

This is where you dig deep to understand why something happened. One useful technique, borrowed from my engineering days, is the five whys.

Here's how it works with a design example.

**Problem:** Users abandoned the new checkout flow at a high rate.

- **Why?** They got confused at the payment-information step.
- **Why?** The form wasn't clear about which fields were required.
- **Why?** Required field indicators weren't visible enough in the design.
- **Why?** The designer used the component library's default styling without customizing it.
- **Why?** The component-library documentation doesn't explain when to customize components for accessibility.

Now you have a real root cause: inadequate component-library documentation. The solution isn't "the designer needs to be more careful." It's "update component-library docs with accessibility guidelines and customization recommendations."

Or, it might be to update the components’ implementation so that it’s impossible to ship something that isn’t accessible. Sometimes the solution depends on what’s possible for your team to accomplish or to convince another team to improve.

You don't always need exactly five whys. Sometimes it's three, sometimes it's seven. Keep asking until you hit something systemic that you can change.

Other useful techniques include:

- Timeline reconstruction: mapping key decisions and their consequences
- Resource-allocation analysis: did we have the right people, time, and budget
- External-factor consideration: market changes, competitor moves, or organizational shifts that affected the outcome

### 5. Actionable Postmortem Deliverables

This is nonnegotiable. **Every postmortem must produce concrete changes** to your system.

Bad postmortem deliverables:

- "Communicate better with stakeholders."
- "Be more careful with research recruitment."
- "Don't let this happen again."
- “Be smarter.”

These are vague, unactionable, and unfollowable. They also rely on humans always doing the right thing in every circumstance, which, in my experience, is not going to happen.

Good postmortem deliverables:

- "Add a required stakeholder-review gate at the end of the research phase for all strategic projects."
- "Update the research-recruitment checklist to include a step for verifying participant qualifications before scheduling them"
- "Create a prelaunch checklist that includes reviewing analytics implementation with engineering."

Notice that good deliverables change the system. They create new processes, update documentation, modify checklists, or establish new requirements. They don't rely on people promising to "do better."

Focus on two types of changes:

- **Process changes**, like instituting checklists, adding new review steps, or fixing broken systems, can prevent bad things from happening
- **Culture changes**, like changing the team’s mindset or making certain behaviors feel more normal, shift how the team operates

Maybe you discover that your best work happens when designers pair with researchers early, so you make early pairing the default. Maybe you learn that having a dedicated project manager improves communication and adherence to timelines, so you fight for project-management support on future strategic work.

### 6. Someone Owns Each Postmortem Deliverable

Actionable deliverables are worthless if nobody implements them. Before the postmortem ends, assign an owner and a deadline to every action item.

Then follow up. This is the part most teams skip, which is unfortunate, because without it, your postmortem won’t change anything. Establish a recurring monthly reminder to check on action items and update your team on progress. If something isn't getting done, figure out why, and either reprioritize it or remove it.

### 7. Documentation and Archiving

Write down what you learned and store it somewhere the whole team can access — a shared drive, a wiki, a Confluence page, or whatever works for your organization.

Make it easy to find. Future team members should always see the postmortem from the checkout redesign when they're about to start a new checkout project.

Include:

- Project overview and goals
- Success metrics and actual outcomes
- Key findings from the root-cause analysis
- Deliverables and their owners
- Timeline (if relevant)

Don't write a novel. Two to three pages is usually enough.

## UX-Specific Considerations

While postmortems originated in engineering, UX and product work has its own challenges that deserve attention.

### Research Quality vs. Research Impact

Sometimes [great research gets ignored](https://www.nngroup.com/articles/research-recommendation-breakage/), or mediocre research drives major decisions. Your postmortem should **examine both the quality of the research and whether it actually influenced the outcome.** It should also acknowledge when research wasn’t done at all, and look at what the outcomes of the project were.

If you did rigorous generative research that no one acted on, that's worth analyzing. Why didn't it land? Was it a communication problem? A timing problem? Did stakeholders not understand the implications? Did you fail to connect research insights to business metrics? Regular postmortems can uncover patterns of project failures after neglecting research results.

### Stakeholder-Engagement Patterns

When and how you involve stakeholders dramatically affects project outcomes. Postmortems should examine this explicitly.

Did you involve leadership too late, after decisions were already made? Did you overinvolve them, turning every minor decision into a committee discussion? Did you bring them in at the wrong moments, asking for detailed feedback on execution when you needed strategic direction?

Identify the engagement pattern that worked (or didn't) and codify it for future projects.

### Design-Iteration Cycles

UX work requires iteration, but how much is right? Postmortems can help you calibrate.

Maybe you learn that you tested too early with throwaway sketches that confused users and wasted time. Maybe you tested too late and had to throw away high-fidelity work. Maybe you tested with the wrong users — early adopters when you needed mainstream users, or consumers when you were building for enterprise.

These insights help you optimize future iteration cycles.

### Distinguishing Correlation from Causation

Be careful about assuming that because X happened before Y, X caused Y. This is especially important in UX work, where many factors may influence outcomes simultaneously.

Your new design launched and retention improved. Great! But did the design cause the improvement, or did it launch at the same time as a marketing campaign, a competitor's price increase, and a seasonal upswing in your category?

Good postmortems separate signal from noise by looking for evidence beyond timing. If you ran an [A/B test](http://www.nngroup.com/articles/ab-testing/), then you have a head start because you already know whether the design change was effective and can focus on investigating why your hypothesis succeeded or failed, so you can improve future decision making. If you didn’t have an experiment, triangulate using existing qualitative data to rule out alternative explanations and to understand what likely drove the outcome.

## Making Postmortems Part of Your Culture

The first few postmortems will feel awkward. People won't know what to expect. They'll worry about blame. They'll wonder if this is a waste of time.

Push through it.

After you've done three or four, and people see action items getting implemented, and they watch the team genuinely improve, postmortems will start to feel valuable instead of painful.

Here's how to build the habit:

- **Start with successes.** Your first postmortem should examine a project that went well. This sets a positive tone and teaches people the format without the emotional weight of analyzing a failure.
- **Keep them blameless.** Every single time, reinforce that you're examining systems, not judging people. When someone blames themselves or others, redirect to process.
- **Follow through ruthlessly.** If you don't implement the deliverables, people will stop taking postmortems seriously. Implementation is where the value lives.
- **Share learnings broadly.** When a postmortem produces a valuable insight, share it with other teams. This multiplies the value and encourages participation.
- **Make them regular but not burdensome.** You don't need a postmortem for every tiny project. Focus on strategic projects, major launches, significant experiments, and anything that produces surprising results (good or bad).

## The Goal: Systematic Improvement

Here's what I learned doing postmortems as an engineer: when something bad happened, like a P0 bug taking down production, a security vulnerability, or a data-loss incident, we couldn't just fix the immediate problem. **We had to understand the root cause** well enough to prevent that category of problems from ever happening again.

The same principle applies to product development. When a project fails or succeeds beyond expectations, you have a rare opportunity to understand why and systematically improve how your team works.

Most teams don't take advantage of this opportunity. They ship, they move on, they repeat the same mistakes and fail to replicate their successes. They get better slowly, through gradual accumulation of experience, if they get better at all.

Postmortems let you get better quickly and deliberately. They transform random experience into systematic learning.

But only if you actually do them. And only if you follow through on what you learn.

So pick a recent project and try a postmortem. Get the team together, dig into what happened and why, and commit to changing something based on what you learn.

Then do it again next month.

You'll be surprised how much faster you improve when you're learning intentionally instead of accidentally.
