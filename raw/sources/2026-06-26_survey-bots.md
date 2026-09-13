---
title: "Kick the Bots Out of Your Survey Data"
date: "2026-06-26"
url: "https://www.nngroup.com/articles/survey-bots/"
author: "Rachel Banawa"
topics: [research-methods]
type: article
---

If you distribute surveys through open channels like social media, online communities, or public links, there’s a good chance some of your responses aren’t coming from real participants. Instead, they may be coming from survey bots, which have become an increasingly common problem for researchers.

If bot responses remain in your final dataset, they can distort your findings and lead you toward the wrong conclusions because they simply don’t reflect the needs and opinions of real people. For that reason, bot screening should be a standard part of survey-data cleaning. However, survey-bot responses can sometimes be difficult to spot because they can look perfectly normal to an untrained eye.

## In This Article:

- [What Are Survey Bots?](#toc-what-are-survey-bots-1)
- [Common Signs of Bot Responses](#toc-common-signs-of-bot-responses-2)
- [Key Considerations when Evaluating Bot Responses](#toc-key-considerations-when-evaluating-bot-responses-3)
- [Always Document Your Decisions](#toc-always-document-your-decisions-4)

## What Are Survey Bots?

> **Survey bots** are automated programs, or people using automation tools, that fill out surveys with fraudulent responses.

Bots range in sophistication from crude scripts that select random answers to AI-assisted tools that generate plausible open-ended text and adapt to question logic. Many can pass basic quality checks like **attention-check questions**, which ask respondents to select a specific answer to confirm they’re paying attention and aren’t an automated program (e.g., “Please select ‘Strongly Agree’ for this question”).

**The risk of encountering bot responses increases when monetary incentives are involved.** Even modest incentives — such as a $5 gift card or a raffle entry — can attract bots designed to complete surveys solely for compensation. However, any survey distributed through an open channel — regardless of the incentive — can still be exposed to survey bots.

## Common Signs of Bot Responses

Screening for bots involves looking for patterns across the entire dataset that suggest a response may not have come from a real participant. Different types of survey questions and metadata can reveal different clues that a response may not be genuine.

While there are several common signs of bot activity, **a single suspicious detail does not automatically mean a response is fraudulent.** Instead, use the following signs to identify responses that deserve closer review.

### Completion Times

Timing data is one of the fastest ways to surface suspicious responses. Most survey platforms automatically record the total completion time. Look for extremely fast or very uniform completion times.

#### Extremely Fast Completions

A survey that takes a human 8–10 minutes should not be completed in 30 seconds. Anything far below your pilot-tested median is suspicious.

#### Uniform Completion Times

If hundreds of responses come in at almost exactly 5 minutes (give or take a few seconds), that clustering is not how humans behave. Real participants vary widely — some skim, some read carefully, some get interrupted. A tight cluster of near-identical completion times suggests a script is submitting responses automatically at a set pace.

![Spreadsheet data showing submission times as 5:37 or 5:42.](https://media.nngroup.com/media/editor/2026/06/03/bot-responses-image_OJoAEag.png)

*Dozens of responses came in consecutively and had a completion time of almost exactly 5 minutes (give or take a few seconds), suggesting bot activity.*

### Open-Ended Responses

Although surveys are primarily a quantitative method, it’s common to include at least one open-ended question, even if it’s simply “Do you have any additional thoughts or comments to share?”. **These questions are among your most powerful bot-detection tools** because it's much harder for a bot to produce a believable free-text answer than to select a random multiple-choice option.

When reviewing open-ended responses, look for:

- **Very long, generic answers:** A bot that is asked, "Why did you choose this rating for the customer experience?" might return three cliché paragraphs about the importance of customer experience without ever actually mentioning anything specific.
- **Uniform response length:** If a large batch of open-ended responses are all roughly the same length — say, all exactly one sentence, or all hovering around 40 words — that's not natural. Real respondents vary widely in how much they write. Consistent length across many responses suggests a bot using a template or a text-generation tool with a fixed output setting.
- **Unusually polished writing:** Real survey responses are often messy. They may include typos, sentence fragments, informal punctuation, or shorthand, especially when participants are responding on mobile devices. A large set of responses that are all grammatically perfect and polished should raise suspicion.
- **Distinctive AI tone.** AI-written responses tend to be fluent and well-organized but remarkably vague. They can sound articulate without ever saying anything specific to the respondent's actual experience. Look out for responses that could apply to almost any product or situation, rather than the specific one your survey is asking about.

### IP Addresses

Most survey platforms automatically capture IP addresses. **Multiple responses from the same IP within a short window** may indicate a single bot operator repeatedly submitting responses. However, note that shared networks (such as university campuses, corporate offices, or household Wi-Fi) can also produce legitimate duplicates.

### Email Addresses

If your survey collects email addresses (such as for incentive distribution or interview followup), these can reveal bot patterns. Look for:

- **Duplicate email addresses:** While it's possible that a real participant accidentally submitted their response more than once, duplicate emails can also be an indication of bot behavior, particularly when they appear alongside other suspicious signals
- **Strings of odd addresses in a row.** Random letter-number combinations (h7fq2w@gmail.com, x9klm3p@gmail.com) arriving back-to-back indicate disposable email generators being used by bot operators.

### Randomized Question Order

If your survey randomizes question order, bots often struggle to keep up with the context. Look for responses where the answer to one question clearly belongs to a different question. For example, a respondent asked about “the most recent app you used” might give an answer that's clearly about “your favorite feature” instead, because the bot pulled from a set of pre-written answers and matched it to the wrong question. This kind of mismatch is easiest to spot in open-ended responses within randomized blocks.

## Key Considerations when Evaluating Bot Responses

The signs discussed above can help you flag suspicious responses, but they shouldn’t be treated as a mechanical checklist to go through. Deciding which responses to remove from your final dataset requires careful judgment of overall patterns.

Keep the following in mind:

- **No single sign is conclusive.** A fast completion time might be a power user. A duplicate IP might be two people on the same household network. A grammatically perfect open-ended response might be from someone who writes carefully. Evaluate each response against multiple indicators before removing it.
- **A response doesn’t need to have every sign to be a bot.** Two or three converging signals — for instance, fast completion and duplicate IP addresses — are typically sufficient to flag a bot response for removal.
- **Bot responses tend to arrive in batches, not one at a time.** When you find one suspicious response, scan the surrounding responses (such as responses submitted within a similar time window). If bot responses are present in your survey, you’ll often find a cluster of suspicious responses sharing similar patterns.
- **Different bot batches may look different**. Do not assume that all bot responses will follow the same pattern. One batch may contain responses completed in exactly five minutes, each with a one-sentence open-ended answer. Another batch may include 30-second completions with long, generic AI-generated paragraphs.
- **Bots are improving quickly**. Bot behavior is changing as generative AI and automation tools become more accessible. The signs that worked six months ago may not catch bots that show up today, and today's signals might miss next quarter’s bots. Stay alert for new patterns.

## Always Document Your Decisions

Once you decide which bot responses to remove, always document your decisions. Keep a record of how many responses were flagged, how many were removed, and which signs led to each decision. This documentation protects the integrity of your analysis. It also helps stakeholders understand that your final sample size reflects a deliberate quality-control process.

### Conclusion

Survey bots are a common risk in online survey research, especially when recruitment happens through open channels or incentives are offered. If left in the dataset, bot responses can distort patterns in the data and lead teams to misinterpret what real users think or feel. Before analyzing survey results, researchers should inspect the data for suspicious patterns, document their bot screening decisions, and remove responses that show strong evidence of bot activity. This process helps ensure that the final dataset reflects the experiences, attitudes, and behaviors of real participants.
