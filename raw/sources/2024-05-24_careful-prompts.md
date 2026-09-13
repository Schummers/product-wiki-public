---
title: "CARE: Structure for Crafting AI Prompts"
date: "2024-05-24"
url: "https://www.nngroup.com/articles/careful-prompts/"
author: "Kate Moran"
topics: [ai]
type: article
---

Text-based generative AI tools (like OpenAI’s ChatGPT, Anthropic’s Claude, and Google’s Gemini) can be extremely useful — but only when given the right instructions.

Use the acronym **CARE (context, ask, rules, and examples)** to remember what information to give AI tools to achieve your desired results. This article demonstrates how to use the CARE framework specifically for UX work.

## In This Article:

- [CARE: Context, Ask, Rules, Examples](#toc-care-context-ask-rules-examples-1)
- [Context: Describe the Situation](#toc-context-describe-the-situation-2)
- [Ask: Request Specific Action](#toc-ask-request-specific-action-3)
- [Rules: Provide Constraints](#toc-rules-provide-constraints-4)
- [Examples: Demonstrate What You Want](#toc-examples-demonstrate-what-you-want-5)
- [Iterate, Refine, and Combine Outputs](#toc-iterate-refine-and-combine-outputs-6)
- [Caveats for CARE](#toc-caveats-for-care-7)

## CARE: Context, Ask, Rules, Examples

To get better results from a generative AI chatbot, write your prompts CAREfully.

Include these four key components in your prompts:

- **C** ontext: Describe the situation
- **A** sk: Request specific action
- **R** ules: Provide constraints
- **E** xamples: Demonstrate what you want

While CARE is a helpful mnemonic for remembering the components, you don’t always have to write prompts in this exact order.

You also will not need such detailed prompts for every interaction with generative AI. General information-seeking tasks may not require giving the AI this much information. However, when looking for complex or specific outputs, provide more details to ensure you get results from AI that meet your expectations.

## Context: Describe the Situation

Establish the [framing](https://www.nngroup.com/articles/ai-prompt-structure/) for your prompt.

For example, imagine we’re using ChatGPT to help us write an error message for a login screen, following the CARE framework to help us write the prompt. To provide the AI chatbot with context, we might explain the situation using the following types of details.

Your job role or experience level | I’m a senior UX designer with 15 years of experience | Where you live | based in Canada | The product you work on | working on an ecommerce site | The type of company you work for | for a large international eyewear retailer that sells sunglasses and prescription eyeglasses. | The project you’re currently working on | I’m currently designing the login screen, where customers sign in to access their accounts. | User profiles, research findings, or deliverables | Our customers are fashion-conscious young adults who value quality, authenticity, and self-expression. | One or more screenshots | Review the attached screenshot to reference the screen I’m currently designing. | The task you’re working on | I’m working on an error message users will see if they attempt to log in with credentials (email and password) that don't match what is in our system.

Focus on what’s relevant for the task. If you were speaking to a new consultant or team member, how would you explain your situation before asking for advice or help?

Depending on the AI tool you’re using, you may not need to enter details about yourself each time you start a new conversation. For example, ChatGPT offers a [custom instructions](https://openai.com/index/custom-instructions-for-chatgpt/) feature where you can provide contextual information for the system to remember and consider for all future results.

Additionally, in early 2024, OpenAI introduced [persistent memory](https://openai.com/index/memory-and-new-controls-for-chatgpt/) in ChatGPT. With this feature enabled, ChatGPT will learn and remember context about you based on information you’ve shared in past prompts to use in future results (If this sounds creepy, you can turn it off).

## Ask: Request Specific Action

This is the [request](https://www.nngroup.com/articles/ai-prompt-structure/) you’re asking the AI chatbot to perform. Whether you phrase the ask as a question or command, it’s important to be specific.

For example, you may include the following details in your requests:

- **Its role:** Who do you want the system to act as?
- **The output you need:** What do you want it to produce?
- **The number of outputs:** How many variations or options do you want?
- **The steps:** What process do you want it to take or follow?
- **The format:** How do you want to receive the results?

Role | You’re a UX writer focusing on intuitive, straightforward, plain language. | Output, Number, and Steps | Follow these steps. Don’t skip any steps. | Generate 15 options for different login error messages. | Review the 15 options you provided. According to the criteria I’ve given, select the 5 best options. | Rank those options from best to worst, and explain your reasoning. | Format | Present the final 5 options in a table, with the error messages in the first column and your reasoning in the second column.

### Chain-of-Thought Prompting

The steps listed in the table above are an example of **chain-of-thought prompting**.

> **Chain-of-thought prompting** is a technique in which a task is broken down into a series of discrete ordered steps, which can help an AI model approach solving the problem more systematically.

## Rules: Provide Constraints

Generative AI will produce better results if you provide guardrails and constraints that help it understand what you want it to do or avoid.

For example, when asking AI to help us write error messages for our login screen, we can include guidelines for writing good [UX copy](https://www.nngroup.com/articles/ux-writing-study-guide/) for [error messages](https://www.nngroup.com/articles/error-message-guidelines/) we want the bot to follow. We can also include product or brand-specific rules, such as tone-of-voice guidelines, and design constraints to consider, such as the amount of space in which the copy should fit or a maximum character count.

Best Practices | Use plain language | Don’t be funny or clever | Don’t obscure the message’s meaning | Offer solutions and recommendations | Don’t blame the user | Avoid passive voice | Style Guide | Tone of voice words: | Approachable and conversational, but not too casual or sloppy | Limits | No more than 100 characters | No more than 2 sentences

## Examples: Demonstrate What You Want

Whether good or bad, providing examples of what you do (or don’t) want the generative AI chatbot to produce can help it better understand what you need.

For example, if you’re trying to improve an existing error message, include it in your prompt and describe what you don’t like about it or what needs improvement.

Good Example | Provide constructive suggestions for fixing the problem. For example, “Add $12 more for free shipping” works well as a message in the shopping cart because it very clearly specifies what users should do to achieve their goal. | Bad Example | Avoid error messages like this: “Oopsie, we couldn’t log you in.” It’s too casual in a frustrating situation. | Existing Ideas | Our developer suggested the error message, “Invalid credentials; please check your email and password." This sounds a bit too techy and formal.

### Few-Shot Prompting

Providing examples in AI prompts is similar to a popular prompting technique called **few-shot prompting.** While related, the two approaches aren’t exactly the same. Few-shot prompting emphasizes inputting exact input-output examples for the system to reference and respond similarly.

> **Few-shot prompting** involves providing a few examples of input-output pairs to help the model understand how it should process similar inputs.

For this example of writing error messages for a login screen, we don’t need to give the AI the input-output pairs -- only the output examples of what we do or don’t want.

In other cases, such as using AI to generate ideas for article titles, we could use few-shot prompting to provide examples, with summaries from several articles as inputs and accompanying title ideas as outputs.

### Example Prompt and Output

**You don’t have to include all the details in the CARE framework** for every prompt. Pick out the pieces and order your commands in a way that’s most relevant and helpful for you and the AI chatbot.

In our example using AI to write error messages for the login screen, we could combine the following elements to produce a CAREful prompt.

> *Background:*
> 
> 
> 
> *I’m a senior UX designer with 15 years of experience working on an ecommerce site for a large international eyewear retailer that sells sunglasses and prescription eyeglasses.*
> 
> 
> 
> *I’m designing the login screen, where customers will sign in to access their account details.*
> 
> 
> 
> *I’m currently working on an error message that will be shown to a user if they attempt to log in with credentials (email and password) that don't match what we have in our system.*
> 
> 
> 
> *Your role:*
> 
> 
> 
> *You’re a UX writer focusing on intuitive, straightforward, plain language.*
> 
> 
> 
> *Steps:*
> 
> 
> 
> *Follow these steps. Don’t skip any steps.*
> 
> 
> 
> 1. *Generate 15 options for different login error messages.*
> 2. *Review the 15 options you provided. According to the criteria I’ve given, select the 5 best options.*
> 3. *Rank those options from best to worst, and explain your reasoning.*
> 4. *Present the final 5 options in a table, with the error messages in the first column and your reasoning in the second column.*
> 
> 
> 
> *Guidelines:*
> 
> 
> 
> *Follow these guidelines when you generate and evaluate the error messages.*
> 
> 
> 
> - *Use plain language.*
> - *Don’t be funny or clever.*
> - *Don’t obscure the message’s meaning.*
> - *Offer solutions and recommendations.*
> - *Don’t blame the user.*
> - *Avoid passive voice.*
> - *Tone of voice words: Approachable and conversational, but not too casual or sloppy*
> - *No more than 100 characters*
> - *No more than 2 sentences*
> 
> 
> 
> *Examples:**Provide constructive suggestions for fixing the problem. For example, “Add $12 more for free shipping” works well as a message in the shopping cart because it very clearly specifies what users should do to achieve their goal.*
> 
> 
> 
> *Avoid error messages like this: “Oopsie, we couldn’t log you in.” It’s too casual in a frustrating situation.*
> 
> 
> 
> *Our developer suggested the error message, “Invalid credentials; please check your email and password." This sounds a bit too techy and formal.*
> 
> 
> 
> *Ask me for additional information you need to do this. If there’s nothing else you need, complete the steps.*

When I ran this CAREful prompt in ChatGPT (using GPT-4o, the latest model as of this article’s publication), here’s the final table it gave me. A pretty decent set of options!

Error Message | Reasoning | Please check your email and password and try again. | Simple, direct, and provides a clear next step. | The email or password doesn’t match our records. Try again. | Clear explanation and straightforward instruction to retry. | The email or password you entered is invalid. Please re-enter them. | A clear indication of the problem and a solution. | We couldn't log you in. Please check your email and password. | Polite, clear, and provides a next step. | Those credentials don’t match our records. Try again. | Clear and to the point, with an easy-to-follow action.

## Iterate, Refine, and Combine Outputs

I find it’s very rare that I can just accept genAI’s output exactly as it’s returned to me. (This is especially true with writing, but I’m picky about that.) Even with a very comprehensive, CAREful prompt, you’ll probably have some additional steps to complete once you get your output.

- **Check whether the AI chatbot followed instructions.** The more detailed your instructions are, the more likely the generative AI chatbot will forget or overlook one or more details. Ask the bot to try again without missing any details.
- **Add any missing instructions or details.** Even with a very detailed prompt, it’s easy to overlook important details or rules. Ask the AI to run the command again with additional instructions included.
- **Ask for more options.** Especially with ideation, try asking the AI chatbot for more options. Using our example, we could ask for 5 more error message suggestions.
- **Combine multiple options.** As you refine the AI outputs, pick out the ideas or language you want to use and modify or combine them with your own. In our example, if the error messages lack constructive and specific feedback for users, we could use our knowledge of UX best practices to add a hyperlink to the text for users to reset their password or contact them for help.

> *Try resetting your password, or contact us for help.*

## Caveats for CARE

**If this seems like it’s a lot of work, that’s because it is.** With current genAI tools and models, this amount of strategic context is often necessary to achieve good outputs. AI chatbots are praised for their time-saving abilities, but they can be a time suck too. It can take significant amounts of time to craft and iterate on CAREful prompts — sometimes more time than you’d have spent just doing a task the old-fashioned way.

For example, I’m an experienced writer. With all of the steps I’ve outlined above, I could have just written an error message myself with less time and effort. But that may not be the case for someone else with less experience in writing.

**Different people will find that genAI is more or less helpful with different tasks.** Like most skills, this is another thing you acquire with practice -- a better sense of when this level of in-depth prompting might save you or cost you time.

**GenAI tools are better and more useful for certain tasks than others.** Writing a CAREful prompt won’t matter if you’re asking ChatGPT to perform a task it just isn’t capable of doing (or doing well). For example, ChatGPT can’t (and shouldn’t) do your taxes for you, whether you prompt it CAREfully or not. Smaller, more focused tasks tend to yield better results.

**Keep practicing with CAREful prompts.** The more you experiment with generative AI, the more you’ll see how and where it’s useful in your UX work. You’ll also become more keenly aware of where AI tends to fail or get confused. This will help you learn when to use genAI, and how to craft your prompts accordingly.
