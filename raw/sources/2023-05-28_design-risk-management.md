---
title: "Design Risks: How to Assess, Mitigate, and Manage Them"
date: "2023-05-28"
url: "https://www.nngroup.com/articles/design-risk-management/"
author: "Therese Fessenden"
topics: [strategy, ux-design-process]
type: article
---

It’s impossible to see into the future and anticipate every possible outcome of our design decisions. As a result, every major design decision comes with **risks**: risk that the design will be unfamiliar or hard to use or unpopular, risk that it will cost too much money, or risk that it will be abused or cause harm.

If a design is well-evaluated before it is implemented, these risks will be small and its benefits will outweigh them. If a design is not well-evaluated, these risks could go unchecked, causing long-term harm to the organization and its customers.

## In This Article:

- [Risk Management](#toc-risk-management-1)
- [6 Steps of Risk Management](#toc-6-steps-of-risk-management-2)
- [1: Establish Organizational Objectives](#toc-1-establish-organizational-objectives-3)
- [2: Identify Hazards](#toc-2-identify-hazards-4)
- [3: Assess Risk](#toc-3-assess-risk-5)
- [4. Develop Risk-Reduction Controls](#toc-4-develop-risk-reduction-controls-6)
- [5. Implement Controls (Or Make Risk Decisions)](#toc-5-implement-controls-or-make-risk-decisions-7)
- [6. Evaluate and Monitor Controls](#toc-6-evaluate-and-monitor-controls-8)
- [Not Every Risk Can Be Fully Mitigated](#toc-not-every-risk-can-be-fully-mitigated-9)

## Risk Management

To reduce harm and maximize the benefits of our designs, we need to incorporate **risk management** into our design decisions to **identify**, **assess**, **control**, and **evaluate** the risks in a systematic way.

> **Design risk:** The likelihood that an aspect of a new or existing design will negatively impact the business or its customers.

The magnitude of that risk can be written as:

> **Risk = Likelihood x Impact**

with the **likelihood** being the probability that a negative outcome (sometimes called a **hazard**) will be observed and the **impact** representing the severity of that outcome.

Organizations strive to mitigate risk to reduce harm, maximize profits, and improve the chance that customers will return. **Mitigation**, however, means reducing a risk, not necessarily eliminating it.

The process of **risk management** enables organizations to assess risks during the design process in order to better address them. It ultimately involves making sure that the assumed risks of our actions are outweighed by these actions’ expected benefits.

## 6 Steps of Risk Management

There are many published risk-management process frameworks, but most can be distilled down to the 6 steps described below:

1. **Establish organizational objectives**
2. **Identify hazards**
3. **Assess hazards**
4. **Develop risk-reduction controls**
5. **Implement controls**
6. **Evaluate and monitor controls**

To illustrate the risk-management process in a UX context, we will use the example of an ecommerce team working to improve the checkout process on its company’s website.

## 1: Establish Organizational Objectives

No organization or person ever intentionally takes on a risk unless there is a benefit. Put another way, a team cannot decide whether a risk is worth taking unless it is aligned on *why* the risk must be taken: that is, it understands the benefits of the associated action. So, it’s important that organizations establish and prioritize key success criteria for the organization and for the design before evaluating potential risks.

For our UX example, let’s imagine that our ecommerce team has a high-priority objective: to increase revenue per visitor. To increase revenue per visitor, a proposed design might include *1-click purchasing*, which allows for a transaction to happen with a single click.

## 2: Identify Hazards

Information about hazards (things which have the potential to cause harm) can be found through a number of different qualitative sources like **behavioral or attitudinal research,****cause-and-effect (“if [this], then [that]”) or flow diagrams, and audits (or data from other assessments).** These can shed light on common complaints, challenges, and concerns. **Analytics , support-ticket data, and case logs** may ****also****offer quantitative information about the frequency and outcomes of certain hazards.

As you can see, several of these data sources relate to *past* experiences or historical data about a product. If these are not available because your product does not exist yet, contextual knowledge obtained by qualitative research and [secondary (desk) research](https://www.nngroup.com/articles/secondary-research-in-ux/) (i.e., literature reviews) may give you a high-level idea of what risks to expect.

However, secondary research is not a substitute for observational research. Whenever possible, rely on observational research to assess hazards.

In our ecommerce example, at this step, the team needs to identify the hazards associated with *1-click purchasing*. The team may review any third-party sources that document possible issues with this solution. It may also conduct some [user research on competitor products](https://www.nngroup.com/articles/competitive-usability-evaluations/) who use this type of design. Here are some of the hazards that could emerge as a result of this research:

- *Users frequently make accidental purchases, ultimately raising support costs.*
- *Users become concerned about fraudulent transactions, which also raise support costs.*
- *People buy more, but smaller packages; these increase shipping costs and CO2 emissions due to inefficient order batching.*

## 3: Assess Risk

As we mentioned earlier, a risk is the combination of the **likelihood** (probability) that harm will happen and the **impact**(severity) of the consequence. Thus, to accurately assess risk, the knowledge around that risk must be more specific than a vague idea of negative outcomes. If we have information about the likelihood of a hazard and the severity of the consequences, we can then “plot” the risk associated to that hazard on a **risk-assessment matrix**, to evaluate how detrimental it is, and how crucial it is to mitigate it.

![A risk-assessment matrix, which features severity levels listed vertically: minimal, moderate, critical, and catastrophic. Probability, or expected frequency, is listed horizontally: unlikely, seldom, occasional, likely, and frequent. Within this 2-dimensional matrix, four risk levels are listed: low, medium, high, and very high.](https://media.nngroup.com/media/editor/2023/05/09/risk-assessment-16.jpg)

*This risk-assessment matrix is adapted from the US Army’s techniques publication (ATP 5-19). The values in the* Severity *column can be adapted to include actual severity, in the form of estimated revenue loss, costs incurred, or longevity of the effect (for example, a decrease in brand loyalty will have a long-term effect). The values in the* Probability *column can also be adapted to feature frequency values relevant to the organization, like the number or proportion of customers impacted, incidents per month/quarter/year, or maintenance days required per year. The value in each cell represents the risk associated with that combination of severity and probability (and is the product of the 2 values).*

Each team will define the risk-assessment matrix associated with their outcomes and then will “plot” each hazard on this matrix.

Consider the ecommerce example of *1-click purchasing* and the hazards we identified earlier:

Hazard | Risk Likelihood (Probability) | Risk Impact (Severity) | Increased number of accidental transactions | Likely | Moderate | Increased number of fraudulent transactions | Occasional | Critical | Increased shipping costs and CO2 emissions | Frequent | Moderate

We could then plot these onto a risk-assessment matrix to visualize the relative risk:

![Plotted on the risk-assessment matrix are three hazards: A) more accidental transactions (shown as medium risk); B) more fraudulent transactions (shown as high risk); and C) higher shipping costs and CO2 emissions (shown as high risk).](https://media.nngroup.com/media/editor/2023/05/09/risk-assessment-14.jpg)

*Plotting hazards by their severity and probability can give us an overall impression of the risk they pose to the organization. The three circles denoted by A, B, and C correspond to the 3 hazards identified in our 1*-click purchasing *example. The risks are medium to high. Depending on the organization’s risk tolerance, these risks might be too high, but mitigation measures (covered next) may reduce them.*

## 4. Develop Risk-Reduction Controls

Remember that the risk is **Likelihood** x **Severity.** Thus,**** the best way to mitigate risk is to either reduce its likelihood or limit its severity (or, ideally, both). While extremely high and high risks should be mitigated, low risks might not warrant special mitigation, especially if it means taking time away from other high-priority efforts.

Let’s go back to our ecommerce example. In our case, B (increased number of fraudulent transactions) and C (increased shipping costs) are high. The team may consider a few strategies to mitigate these risks:

Considering the hazards we’ve identified, we might mitigate risk as follows:

Hazard | Mitigation | New Risk Probability | New Risk Severity | Accidental transactions may result in more support inquiries and unhappy customers. | Immediately provide confirmation and cancellation options, but delay sending order info to fulfillment center by 12 hours. | Occasional | Negligible | Fraudulent transactions may put user data at risk and result in more support inquiries. | Require authentication within 12–24 hours as a condition of | 1-click ordering | Seldom | Critical | Inefficient order batching may increase shipping costs and produce more CO2 emissions. | Offer two forms of 1-click shipping: | Ship Now | and | Ship | with | Next | Batch | . | Likely | Moderate

![In this risk-assessment matrix, the risk level of hazard A, more accidental transactions, is reduced from medium to low. The risk levels of hazard B, more fraudulent transactions, and C, higher shipping costs, are both reduced from high to medium.](https://media.nngroup.com/media/editor/2023/05/09/risk-assessment-15.jpg)

*In the above example, the risk-mitigation measures proposed would deescalate the risk level for hazards B and C by decreasing their probability.  For hazard A, not only would the risk likelihood decrease, but the severity would also decrease, with self-service options alleviating the potential increase in customer-support costs.*

Reassessing risks after mitigation strategies are proposed can give an objective perspective of whether risks are truly mitigated or still too high to move forward with a decision. It also allows teams to propose more-involved or less-involved mitigation strategies, depending on their risk-tolerance levels, while the risks are still objectively evaluated the same way every time.

## 5. Implement Controls (Or Make Risk Decisions)

While your team may have developed strategies to reduce design risks to an acceptable level, that does not mean it should automatically implement them. Just because something is “low risk” does not mean it’s still worth pursuing. Risk mitigation may also interfere with the team’s original objectives.

With our earlier *1-click ordering example*, possible mitigation strategies might involve introducing friction, like one more click to confirm purchase (and thus, reduce the probability of accidental purchases), or slowing down backend processes to give users time to undo any accidental transactions without impacting customer-support costs. However, either of these strategies may also slow the speed of the transaction or shipping to the point it’s not much faster than the existing checkout process.

So, while the risk of accidental purchases may be lower, the benefit of a *mildly* faster transaction may still not outweigh the implementation cost and the remaining risk of an accidental purchase. Therefore, a more risk-**tolerant** team may opt to implement 1-click ordering without the mitigation, while a more risk-**averse** team may decide that the conversion-rate improvement is worth it only if it does **not** result in swamping the customer-support staff and may, therefore, choose to mitigate the risk (or forgo the initial design choice entirely). Still, even if a team is normally risk-tolerant, facing more risk than usual for other reasons (like an economic recession) may also impact that team’s *current* tolerance to risk.

More importantly, most teams aren’t, as my mother used to say, “made of money.” Risk-mitigation strategies come with their own implementation costs. Teams need to analyze the costs of these strategies and much like a team might prioritize designs by their user impact and feasibility, controls should be pursued by weighing their relative feasibility & overall *risk* impact.

Often, these controls come in the form of adjustments or specifications for both new and existing designs, but they may also be changes in workflows, processes, and business models. Regardless what types of controls you’re considering, some well-distributed (and more importantly, well-written) documentation will ensure that the controls are implemented consistently across the organization.

## 6. Evaluate and Monitor Controls

Finally, a risk-management strategy will only be as good as the team’s ability to update it with new and relevant data about those risks. As designs change over time, risk-mitigation strategies may become irrelevant or outdated. Thus, complacency and a false sense of security about previously identified risks can result in disastrous outcomes for users and organizations alike.

To avoid potential damage from insufficient risk mitigation or recurrent risks, teams should consider scheduling routine audits at specified intervals or milestones and regular retrospectives to evaluate whether risk-mitigation strategies are working, or need adjustment with new circumstances.

## Not Every Risk Can Be Fully Mitigated

Not only are some risks entirely out of our control, but some are also impossible to anticipate. “What-if”-ing every design decision to death (“What if an asteroid hits our server?”) is itself a risk to the organization — spending time deliberating about risks that are both unlikely and outside of our control is counterproductive. So, the best we might be able to do in cases of external, uncontrollable risk is to monitor frequently to ensure we are aware of new risks early and adapt our designs to be “resilient” to foreseeable risks.

Risk management is a critical skill that will only become more entwined with UX work as technology scales to impact more people at greater speeds in more places. As the old adage goes, accept the things we cannot change, have courage to change the things we can, and have the wisdom to know the difference.
