---
title: "12 Design Recommendations for Calculator and Quiz Tools"
date: "2024-04-19"
url: "https://www.nngroup.com/articles/recommendations-calculator/"
author: "Tanner Kohler"
topics: [design-patterns, search]
type: article
---

Users like calculator and quiz tools because such tools offer an opportunity to get expert advice without having to speak to anyone or make long-term commitments. However, these tools quickly become frustrating and get abandoned when they aren’t easy to use.

The following guidelines help you increase the usability, trustworthiness, and usefulness of calculators, quizzes, estimators, converters, or of other similar types of tools. This article refers to all these tools as “calculators.”

## In This Article:

- [1. Optimize Calculator-Tool Pages for SEO](#toc-1-optimize-calculator-tool-pages-for-seo-1)
- [2. Embed Calculators Directly in Webpages](#toc-2-embed-calculators-directly-in-webpages-2)
- [3. Accommodate Variable Amounts of User Input](#toc-3-accommodate-variable-amounts-of-user-input-3)
- [4. Do Not Force Users to Register to Use a Tool](#toc-4-do-not-force-users-to-register-to-use-a-tool-4)
- [5. Provide Immediate Results on the Website](#toc-5-provide-immediate-results-on-the-website-5)
- [6. Facilitate Easy Input Adjustments and Restarts](#toc-6-facilitate-easy-input-adjustments-and-restarts-6)
- [7. Offer to Explain the Purpose of Inputs](#toc-7-offer-to-explain-the-purpose-of-inputs-7)
- [8. Help Users Understand Inputs](#toc-8-help-users-understand-inputs-8)
- [9. Contextualize Outputs in Meaningful Ways](#toc-9-contextualize-outputs-in-meaningful-ways-9)
- [10. Avoid Misleading Defaults](#toc-10-avoid-misleading-defaults-10)
- [11. Consider Exposing the Algorithm of the Tool](#toc-11-consider-exposing-the-algorithm-of-the-tool-11)
- [12. Do Not Assume AI Is Necessary](#toc-12-do-not-assume-ai-is-necessary-12)
- [Conclusion](#toc-conclusion-13)

## 1. Optimize Calculator-Tool Pages for SEO

[Incorporate keywords](https://www.nngroup.com/articles/web-writing-use-search-keywords/) such as "calculator," “quiz,” or “estimator” in the title of the page that hosts the tool. Users looking for guidance frequently start on a search engine and are willing to open a calculator tool directly from the search results, even if they are unfamiliar with the organization.

## 2. Embed Calculators Directly in Webpages

Users prefer tools that are readily accessible and embedded on relevant pages rather than in popups or on dedicated pages. However, the embedded tool should load quickly. Some users in our research skipped over the calculator they were looking for because they scrolled too quickly, and the tool had not yet loaded.

![A debt consolidation calculator embedded in a webpage which is directly accessible to the user.](https://media.nngroup.com/media/editor/2024/03/26/debt1.png)

✅ *NerdWallet: The debt-consolidation calculator was embedded within the relevant webpage rather than forcing users to go elsewhere to access it.*

## 3. Accommodate Variable Amounts of User Input

Users assume that the more information they enter, the more accurate the results will be (somewhat like in a [filter](https://www.nngroup.com/articles/filters-vs-facets/)). However, not all users will be prepared to enter the same amount of information in a calculator. Make only [essential inputs required](https://www.nngroup.com/articles/required-fields/).

[Dropdowns](https://www.nngroup.com/articles/drop-down-menus/) and [sliders](https://www.nngroup.com/articles/gui-slider-controls/) are sufficient when precision isn’t required, such as when indicating a general level of risk tolerance. Open-text fields are essential when users must enter unique, detailed information, such as their monthly budget. When in doubt, let users type things in rather than forcing them to use a slider.

![A dropdown with income ranges to enter the users' yearly income](https://media.nngroup.com/media/editor/2024/03/26/ramsey1.png)

✅ *Ramsey: For this insurance check-up calculator, users didn't need to enter the exact amount of their yearly income. Choosing an income bracket from a set of options captured a sufficient level of granularity. Notice the encouraging verbiage* Ballpark figures are fine!❌ *Ramsey: The same insurance calculator frustrated one research participant because it would not allow him to select multiple types of life insurance. He immediately discounted the value of the results because he now knew the calculator did not fully understand his situation.*

## 4. Do Not Force Users to Register to Use a Tool

Users commonly turn to calculator tools while exploring information and trying to understand a problem space. They will almost always choose to *continue as a guest* or otherwise use the tool anonymously when given the option. They don’t want to be bombarded with follow-up communications.

![A pop up that allows users to "Continue as guest" rather than having to register to see results.](https://media.nngroup.com/media/editor/2024/03/26/screenshot-2024-02-26-at-15431-pm-1.png)

✅ *The Ohio State University: All participants in our research who interacted with this cancer-risk calculator chose to* Continue as a guest *. They were interested in the results, but not in an ongoing relationship with the university.*

## 5. Provide Immediate Results on the Website

Users do not like signing up for an account or waiting for an email to see their results because, when they are using a calculator, they are just exploring, not committing. At the very least, present users with their results right on the web page, in addition to any forced registration. Users especially like it when the output is dynamically calculated as they input their information, so they can see how different inputs affect the outputs.

![A pop up that requires users to sign up to see their results.](https://media.nngroup.com/media/editor/2024/03/26/screenshot-2024-02-26-at-20044-pm-1.png)

❌ *Princeton Review: After answering 24 questions about himself, a study participant had to sign up to see his results. He was particularly frustrated because he did not know registration would be required before beginning the quiz.*

## 6. Facilitate Easy Input Adjustments and Restarts

Once users have seen outputs, they should be able to:

- Change individual inputs without having to reenter all the other inputs
- Easily erase all inputs and restart the whole process

Facilitating small tweaks to inputs without forcing complete restarts is most important when users have entered more than a handful of inputs. They don’t want to have to start all over in order to make a few adjustments. However, when the tool only accepts a few inputs, users are more likely to want to erase all inputs and start again.

![The end of a series of paint choices, followed by a "Start over" button](https://media.nngroup.com/media/editor/2024/03/26/clare-color-genius_-find-your-perfect-paint-color-quiz-copy-3-1.jpg)

⚠️ *Clare.com: This chatbot-like tool asked users a series of questions about a room they will be painting before suggesting some color options. While the tool did properly provide a* Start over *button at the end, changing any previous selections erased all subsequent inputs. The user must reenter everything that comes next, even if they did not want those fields changed.*

This flexibility supports iterative exploration and helps users understand the impact of different inputs on the outputs — particularly since users often begin by putting in rough, estimated information to gauge the value of the tool. Do not expect users to be wholeheartedly committed to outputs.

## 7. Offer to Explain the Purpose of Inputs

Users are happy to enter information when they understand how it impacts the value of the outputs. However, they hesitate when they feel the calculator is asking for either too much information (because it takes [too much effort](https://www.nngroup.com/articles/interaction-cost-definition/)) or too sensitive of personal information (because they worry about privacy). In both cases, provide a rationale for why the information is important for generating useful outputs to motivate users. This rationale can be visually deemphasized in the interface.

![A question about the user's phone accompanied by a reason for asking the question](https://media.nngroup.com/media/editor/2024/03/26/screenshot-2024-02-26-at-45732-pm.png)

✅ *Mint Mobile: The quiz offered a reason for why it needs to know whether the user has paid off their phone. This pattern is even more important for more laborious or personal questions.*

## 8. Help Users Understand Inputs

Offer clarifications and examples of inputs if they are likely to be unfamiliar to nonexperts. Such clarifications could include the required format, [what others commonly enter](https://www.nngroup.com/articles/social-proof-ux/), an [anchor](https://www.nngroup.com/articles/anchoring-principle/) to decide what’s reasonable, or an explanation of unfamiliar terms. (Do not recommend values when requesting factual information that the user cannot change — for example, the amount of savings a user has, as one investment calculator did).

Clarifications should be in line with the associated input fields, to help users refer to them as they input information. They should not be listed in an instruction block, below or off to the side of the calculator.

![A lot of detailed explanations of calculator inputs that are hard to scan and read.](https://media.nngroup.com/media/editor/2024/03/26/screenshot-2024-02-26-at-14722-pm.png)

❌ *American Heart Association: Users in our research were not familiar enough with the required inputs to confidently know what to enter. The massive wall of text with explanations to the side of the inputs was overwhelming.*

## 9. Contextualize Outputs in Meaningful Ways

Frame outputs in meaningful ways, offering interpretations or context to make information actionable. Users often turn to calculator tools because they are unfamiliar with the domain and cannot be expected to understand outputs immediately.

![A set of budget calculator outputs framed around needs, wants, and savings.](https://media.nngroup.com/media/editor/2024/03/26/piggy1.png)

*✅ Voya: One participant found it meaningful to see how her spending aligned with a simple framework for* Needs, Wants, *and* Savings *. She planned to revisit this calculator because she considered this framework useful.*

## 10. Avoid Misleading Defaults

Be cautious with default values that can influence user assumptions about what's reasonable. For example, one user was discouraged to see he could not afford a home while using a mortgage calculator, only to realize later that the default property-tax amount provided by the tool was more than four times the typical amount in their area.

![A mortgage calculator with a misleading default amount.](https://media.nngroup.com/media/editor/2024/03/26/mortgage1.png)

❌ *Google: Although users could change the US state for which they are estimating a mortgage with Google’s Mortgage Calculator, the estimated yearly property-tax amount did not automatically change. The inaccurate default property-tax amount overestimated monthly payments by hundreds of dollars per month if a user did not recognize that the default amount was inaccurate and changed it themselves.*

## 11. Consider Exposing the Algorithm of the Tool

This is not always essential, as many users automatically trust the calculator based on their trust in the provider. However, transparent explanations of how the tool calculates results can enhance user trust and comprehension. A clear understanding of the tool's mechanics can align user expectations with actual outcomes, fostering more effective use.

## 12. Do Not Assume AI Is Necessary

While [AI can add sophistication and power](https://www.nngroup.com/articles/ai-productivity-customer-support/), it isn’t always essential for generating useful outputs. Users’ trust in a tool's algorithms comes from their perceived reliability and usefulness, not necessarily from the use of AI.

## Conclusion

Developing a calculator tool can be difficult — especially in complex decision-making domains. However, complex domains are exactly where calculator tools are the most valuable because that is where decision makers struggle the most. Accept as much information as users will provide and iterate the design to generate more and more personalized outputs for differing circumstances.
