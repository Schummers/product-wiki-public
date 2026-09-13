---
type: source
name: "Product Management for UX People: CHAPTER 7: Testing Hypotheses with Experiments"
created: 2026-09-11
published: 2022-01-19
source_type: book
status: processed
url: https://rosenfeldmedia.com/books/product-management-for-ux-people/
author: Christian Crumlish
raw: raw/sources/2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments.md
book: "Product Management for UX People"
chapter: "CHAPTER 7: Testing Hypotheses with Experiments"
concepts:
  - Assumption Testing
  - A-B Testing
  - Statistical Significance
  - Fake Door
  - Minimum Viable Product
---

# Product Management for UX People: CHAPTER 7: Testing Hypotheses with Experiments

## Summary

This chapter positions experimentation as a fundamental way of life in product management, not a specialized activity. Crumlish frames product work as a series of testable bets: the determination of what to build and for whom; prioritization decisions about which bugs to fix; and optimization of existing features. The core discipline is developing crisp, testable hypotheses about why data is behaving a certain way, then designing experiments to validate or disprove those hypotheses. The chapter covers A/B testing in detail (scheduling, statistical significance, impact measurement, learning, and stacking wins) but emphasizes that A/B tests are limited—they show what happens but not why—and that PMs should use a broader toolkit. A critical caveat: A/B testing often cannot be used in B2B and enterprise contexts where the user base is small and high-touch, and experiments can disrupt customer relationships. The chapter then catalogues thirteen named methods beyond the plain bucket test, starting with variations on A/B tests and running through Concierge, Wizard of Oz, Fake Doors, Pretotypes and Partial Rollouts.

## Key Takeaways

- **Hypotheses are testable ideas about cause and effect** — A hypothesis explains why something is the way it is; it is grounded in observation (often of anomalous data) and can be validated or disproven through experiments. Example: Heather Cornell at 7 Cups hypothesized that "new visitors don't know what a Listener is," leading to a button label test that improved performance.

- **Prioritize experiments by risk, not just impact** — Use a rubric that weighs potential reach, potential impact, engineering effort, and confidence in the hypothesis. Highest priority goes to the riskiest bets (de-risking), not just the easiest or most visible ones. Maintain a backlog of hypotheses and proposed experiments in a shared tracking tool (e.g., Airtable).

- **A/B tests require discipline and statistical rigor** — Crumlish gives the sample size as "a very broad rule of thumb": you tend to need at least 2,000 people in each bucket before you can trust a result, and he separately observes, of an A/A test, that you should not be surprised if the two groups stabilize at parity around 2,000 people each. Software such as Amplitude now reports significance and the likelihood the result is correct; decide your end condition before running the test to avoid cherry-picking; record both numerical impact and qualitative insight about what the result means for your next hypothesis. An A/A test (identical control and variant) helps you see when results stabilize at parity.

- **A/B tests have major blind spots** — They reveal what happened but not why. There is no way to know for sure whether externalities affected a test, or whether running it again at another time would give the same result. Overreliance on A/B testing can lead to "polishing a local maximum," optimizing one small area while missing much larger opportunities. Further validation through qualitative research is essential.

- **A/B testing often fails in B2B and enterprise contexts** — According to Clement Kao, enterprise customers cannot be shown different workflows because the user base is small, named customers in high-touch relationships, and training cohorts on different interfaces is disruptive. For these contexts, other testing methods are more practical.

- **Beyond A/B tests: thirteen named alternatives** — Variations on A/B tests (A/B/C and multivariate, which need still greater traffic), Concierge (human behind the scenes), Wizard of Oz (human disguised as automation), Pretotypes (Alberto Savoia's term for a low-fidelity version answering "should we build it"), Smokescreen (ad for a nonexistent product), Fake Door (phantom feature in UI), Broken Glass (deliberately difficult feature), Dogfooding (internal testing), Partial Rollouts (staged release), Beta Programs, Holdover (keeping the old version for a small group to watch performance over time, a method Ryan Rumsey of Second Wave Dive recommends because features often get used at first only because they are new), Sales Experiments (testing pitch language), and Process Experiments (varying team workflows).

- **Stack wins and learn from losses equally** — Once a test succeeds, lock it in and attempt follow-up tests to compound the improvement. A loss teaches you something about the hypothesis or the test itself; both matter for building your product intelligence arsenal over time.

## Quotes

> Generating hypotheses may sound like something you do in an ivory tower or laboratory, but it's just a fancy way of coming up with theories and ideas you can test out. Any design exploration you've ever done has been a way of testing hypotheses. User research scripts are based on hypotheses you want to explore. Don't let the science talk scare you. You've got this!

> In B2B, you can't actually A/B test because someone is trying to use your product to run their business. So if they have to train one cohort of users to use one workflow and another cohort to use a different workflow, you definitely cannot do that. Similarly, it's not helpful to recruit a random 'enterprise user' when you're trying to go after a specific set of customer accounts.

> The holdover is a nice way to look at performance over time. I think many teams assume an initial test result = same results over time. I've found many features were used initially because they were new, but then dropped back after 90 days.

## Concepts

- [[Assumption Testing]] — formulating testable hypotheses about product decisions (what to build, how to prioritize fixes, how to optimize features) and designing experiments to validate or disprove them.
- [[A-B Testing]] — a form of bucket testing in which users are split into two equal cohorts, one receiving a control experience and the other a variant, to measure statistical impact on a goal metric. Requires discipline around scheduling, statistical significance thresholds, and learning beyond the numerical result.
- [[Statistical Significance]] — the threshold of sample size and consistency at which you can trust A/B test results; as a very broad rule of thumb you tend to need at least 2,000 people per bucket, and an A/A test (identical control and variant) shows when results stabilize at parity, which Crumlish says may also happen around 2,000 per group.
- [[Fake Door]] — a phantom feature presented in the product interface to gauge user interest; when users attempt to use it, they are shown a promotion for the upcoming feature and sometimes a way to register interest. The chapter names the risk: you might frustrate your users.
- [[Minimum Viable Product]] — here appearing as "pretotype," Alberto Savoia's term (from his talk "Build the Right It") for a low-fidelity proof of concept or fast version of an idea that is just complete enough to generate real, data-driven validation of whether something "should be built," distinct from a prototype that proves "can we build it."
