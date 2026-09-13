---
title: "Prompt Structure in Conversations with Generative AI"
date: "2023-11-24"
url: "https://www.nngroup.com/articles/ai-prompt-structure/"
author: "Amy Zhang, Emma Cionca, Feifei Liu, Raluca Budiu"
topics: [ai]
type: article
---

Our study of AI-chatbot interactions shows that most AI prompts contain one or more of several key components. These components help articulate the users’ information need. Prompts that lack certain components can result in long, inefficient conversations, with many query refinements.

Designers can support users by providing AI-interface elements that make it easy to include the different prompt components.

## In This Article:

- [Our Research](#toc-our-research-1)
- [Prompt Structure](#toc-prompt-structure-2)
- [Special Types of Prompts](#toc-special-types-of-prompts-3)
- [AI Prompt = the Visible Part of the User’s Information Need](#toc-ai-prompt-the-visible-part-of-the-users-information-need-4)
- [Tips for Users of Generative AI](#toc-tips-for-users-of-generative-ai-5)
- [Recommendations for Designing the UX of Generative AI](#toc-recommendations-for-designing-the-ux-of-generative-ai-6)

## Our Research

In May and June 2023, we conducted a 2-week diary study involving 18 participants who used ChatGPT 4.0, Bard, and Bing Chat. Participants logged 425 conversations and rated each for helpfulness and trustworthiness. At the end of the study, we conducted in-depth interviews with 14 participants.

The findings of this study are reported in several articles:

- [Information foraging with generative AI](https://www.nngroup.com/articles/generative-ai-diary/): how AI bots change the process of finding information
- [Differences in helpfulness and trustworthiness among ChatGPT, Bing Chat, and Bard](https://www.nngroup.com/articles/ai-bot-comparison/)
- [Analysis of AI-conversation structures](https://www.nngroup.com/articles/AI-conversation-types/)
- Prompt structure for AI conversations (this article)

## Prompt Structure

A **prompt** is a discrete input from the user that initiates or guides the chatbot’s response. A **conversation** with an AI chatbot can have one or more prompts.

We identified four components that were often (but not always) part of the AI prompts used in our study:

- Request
- References to either previous bot answers or to external sources
- Format
- Framing

*Analysis of an AI prompt created by a diary-study participant (Names of dogs were modified for privacy.)*

Not all these components were present in every prompt or in every type of conversation.

### Request

The request is the most straightforward part of the prompt — **the core of the information need that the user wants to address**.

In our study, the request was present in most (but not all) prompts, and many prompts contained only this component. The prompts that did not include a request were usually simple filler prompts such as *Thank you* or prompts that provided additional clarification to an initial request.

The language of the request component typically took the form of a question, implicit request, command, or incomplete sentence.

Different Language Formats for the Prompt Request | Question | “should dogs eat kibble?” | “What are some ways to work from home with young children around?” | Implicit requests | (signaled by phrases like | I want | or | I need | ) | “I am looking for a new videogame to play” | “I need a dinner meal plan for 7 days on a budget” | Commands | (introduced by phrases like | Provide, Tell me, Give me | ) | “Give me some ideas around real estate” | “recommend restaurants in South Elgin, Illinois to go for lunch” | Incomplete sentences | “Best strength exercises” | “Tips for doing a successful surprise proposal”

Some of the conversations we observed contained request-only prompts — the prompt consisted of a request without any additional context. Some request-only prompts (e.g.,*best strength exercises*) resembled a search-engine query.

A common request-only prompt in our study involved asking the bot to provide the best of something — for instance, *the cheapest airport, the best way to get from Tokyo to Hakone to see Mount Fuji, the best cures for migraine, the easiest way to add lentils to your diet.*

These best-of prompts were often inefficient (because they lacked sufficient details) and resulted in funneling conversations. As explained in our article on AI-conversation types, funneling conversations start with vague, underspecified prompts and require a lot of back-and-forth between the user and the bot., as the user is using subsequent prompts to articulate some of their requirements.

### References: Internal or External

There are two kinds of references that may appear in AI prompts:

- **Conversation-internal references** (or quotes) to a previous answer provided by the bot, usually within the same conversation
- **Conversation-external references** to documents or third-party sources, usually copied or pasted by the user as part of their prompt

#### Internal Reference: Quote from Previous Answer

This prompt component references **something the bot said within the same conversation.**

It was common for our study participants to have to mention a part of a previous answer (a behavior called apple-picking). Especially when the referent was a piece of text, the user had to type it again or copy and paste it to remove ambiguity. Sometimes, the user would refer to the structure of the bot’s answer to indicate their interest (e.g., *Change the last word in the last paragraph*). These kinds of references could be used independently (like in the example above *— last word in the last paragraph*) or in conjunction with an actual quote.

*The user quoted from the answer by both referring to a part of the answer,* the second example,*and including a direct quote,* To first apply, *in his prompt*.

Especially on mobile, it was difficult for the user to refer to specific aspects of an earlier bot response. Sometimes, instead of copying the text, the user inadvertently hit the *Enter* button and submitted the query too soon.

*When a study participant requested Bing Chat to edit a CV entry on a mobile device, she used two references to that entry: the words* first line *and the quote* conducting research. *Despite her efforts, the bot did understand her instructions correctly until after she had tried three different prompts. (Video at 1.5x speed)*

[Direct manipulation](https://www.nngroup.com/articles/direct-manipulation/) would vastly improve users’ interactions with bots. Designers can support internal references by allowing users **to select part of an answer and add it to the next query**. For example, the user could right-click on a selected part of the answer and add it to the next query, as suggested in our article on [apple-picking](https://www.nngroup.com/articles/accordion-editing-apple-picking/).

#### External Reference: Source Text

When asking the bot to work on a piece of text (for example, in text-generation or coding activities), users often must copy and paste it from elsewhere. When coding, users occasionally also paste error messages to seek debugging assistance.

*A participant copied and pasted text from her resume to have it rewritten by the AI bot.*

Not all references involve copying and pasting the source text. Instead, a user may simply reference an external source by name, without pasting its text in the prompt, because they assume that the AI bot is already familiar with it. For instance, in the following prompt *,* the user assumed that the lyrics of a popular song did not need to be provided:

> *Please do a comical play on the lyrics of Holy by Justin Bieber but center the song on Mr. Smith, my dog [...]*

Occasionally, users include an external source as an example of the type of output they want from the bot.

For instance, when instructing Bing Chat to revise sections of a resume, one study participant used the prompt:

> *Review job summary. Match in tone to this: [a previous section of her resume].*

#### Tips for Designing Generative-AI Interfaces

Consider how you can **support easy referencing** to parts of the bot’s previous responses, as well as to external sources.

- **Allow users to select parts of the conversation** (from bot-generated answers or images) and **include them in their further prompts**. While copying and pasting is a familiar, relatively straightforward operation, it can still be cumbersome on mobile or when long documents are involved.
- Allow users to easily **upload a document** and select a piece of text from it or ask for help with specific fragments. At the time of the study, none of the bots had this functionality. However, ChatGPT-4 and other bots, such as Claude, now allow users to upload a document as part of their prompts.

*Claude allows users to upload various file formats, making it easier to refer to external documents.*

### Format

When specifying the format in a prompt, **users provide specific attributes they want from the bots’ output.** These attributes often included:

- Length (e.g., *one paragraph, 1500 words*)
- Language (e.g., *middle-school English, Python*)
- How the information should be presented (e.g., *bulleted list, table, visual*)
- Tone of voice (e.g., *professional, casual, fun*)

Here are some examples of format specifications from our diary study:

> *Act as an Artificial Intelligence expert and tell me what is necessary to connect Bing to Bard to Anthropic to ChatGPT and give a response in one window .*

> *Translate the following informal note for my house cleaner. Use standard informal Spanish (Mexico) .*

> *can you give a visualization of the convolutional connections and recurrent connections*

> *Please write me an email thanking a group for attending a meeting including a question/answer section. This email should be professional and not too long .*

Understandably, only a few study participants included such specifications in their prompts, as these were often unnecessary for information-seeking conversations. (The exception was when the user wanted a concise, easy-to-read explanation.) Format specifications were more common in task-based conversations, whose output was supposed to be used by the participant for a specific goal (e.g., to include it in a resume or a presentation).

#### Tips for Designing Generative-AI Interfaces

Include a **UI feature that allows users to select among different possible output formats**, as well as change the format of an answer already received.

For example, for certain text creation queries, Bing Chat offered a *make-it-shorter* suggested followup prompt. Additionally, the current version of Bard allows users to modify the length, complexity, and tone of voice of an answer.

*The current Bard interface allows users to apply a format modifier to the answer they received from the bot. It would be good if these format options would also be available at prompt-creation time, before the bot provides an answer.*

**Format-specification options should be provided at prompt level or conversation level rather than as a global setting** that applies to all conversations.**** That is because people use AI bots in a variety of contexts and for a wide range of tasks, and their formatting needs will vary according to the task.

For example, the current version of ChatGPT has a global setting that allows users to enter format specifications for all ChatGPT’s answers. Such a setting is unlikely to be helpful because [many people use AI bots for both work and personal purposes](https://www.nngroup.com/articles/ai-roles-ux/), and they will likely need different kinds of formats for these settings.

*A global ChatGPT setting called* Custom Instructions *allows users to specify context (top field) and also format preferences (bottom field). However, users’ contexts and formatting needs are likely to depend on their current task.*

### Framing

The **prompt****framing involves a description of the problem that the user wants to solve or of their context**. Framing is intended to provide the bot with all the necessary information to generate a satisfactory response. It thus reduces the need for query reformulations.

Certain types of well-defined information needs cannot be satisfactorily addressed without enough framing. However, providing contextual details takes a lot of user effort.

In our study, some conversations started with a prompt that had detailed framing. Some examples include:

> *I am wanting to start a laundry service in my area. The service would be wash, dry and fold. I would provide pickup and delivery as well. Can you give me some name suggestions?*

> *I am going to Japan for the first time in November for 7-10 days. I will be staying in Toyko and will not be renting a car. What are the top 10 things that I should see.*

Framing often included an **explanation of the user’s goal**, to ensure that the AI’s response would include the right angle. For example:

> *I trying to decide which car to purchase . My three choices are a 2023 Kia Telluride, a 2023 Kia Carnival, and a 2023 Jeep Grand Cherokee L. Please compare the 3 in the following categories; safety, cost, and online reviews.*

Some framing prompts followed [the roleplaying model](https://www.nngroup.com/articles/anthropomorphism/), popularized in news and social media. Word phrases used to introduce such prompts included *Be a*, *Imagine you are, Pretend you are, Act as a.* The intent behind these phrases was to **reduce ambiguity by setting upfront the domain of the query.**

> *Imagine you are my coach , I am a 130 lb woman and want to get my first pull up. Design a daily program of a few exercises (preferably body weight) that can be done to guarantee that I can get my first pull up in two months.*

> *Be a travel guide . Create me a 4 day itinerary in Chicago including activities and restaurant recommendations with estimated costs*

> *Act as an Artificial Intelligence expert and tell me what is necessary to connect Bing to Bard ta Anthropic to ChatGPT and give a response in one window.*

Sometimes, however, the participants misused roleplaying prompts and assumed that *be X* or similar phrases were magic words that were likely to lead to a good answer. In fact, **inviting the bot to play a specific role was not always necessary (or sufficient) to frame their query.**

For example, the framing for the following prompt contained a roleplaying component, but that component did not provide any benefit:

> **Imagine you are a business intelligence analyst or a technology strategist,***what are the technical skills that I would need to know?*

A similarly detailed answer was provided by the shorter prompt, without framing:

> *What are the technical skills needed for business-intelligence analysts?*

**Framing a prompt is a time-consuming task for users.** It requires them to think of all the information that the bot might need and then type it out. Some users may find it difficult to explicitly state all the constraints of their query. As a result, many conversations with well-defined information goals start without proper framing.

Note, however, that **not all prompts need framing**. When the information need is broad and is centered on learning, framing may not be necessary. It can be okay to start with an unframed question and then use the bot’s answer to determine the best direction that the conversation should take.

#### Tips for Designing Generative-AI Interfaces

- When prompts lack framing and are too vague to get a detailed response **, the bot should ask questions to understand the user’s context** and help them consider all relevant aspects related to their query. (Such questions are integrated into the design of Perplexity AI’s Copilot feature.)
- Provide suggested followup prompts that **add framing to the user’s original prompt**.
- Give **examples** of what good framing for a particular question may look like.
- Minimize the effort of framing by allowing users to **reuse framing from past conversations.** The GPT feature of ChatGPT also allows users to create customized agents (or GPTs) that always consider a task-specific set of instructions as part of prompt framing.

*Perplexity AI’s Copilot feature attempts to gather neccessary framing details after the user submits their prompt but before producing output. In this case, Copilot requested the occasion when the user asked for help finding a gift for a friend.**ChatGPT allows certain specialized instructions to be part of the framing for all conversations with a GPT agent.*

## Special Types of Prompts

Most of the prompts we encountered in our study had a combination of the components described above. There were, however, a few notable exceptions, discussed below.

### Can You Prompt : Uncertainty about Bot’s Capability

Sometimes users were not sure whether their information need fell within the bot’s realm, so they would start a conversation by **asking the bot whether it could help with a particular task**. This strategy saved users’ time because they didn’t need to bother with entering a complex query if the bot wasn’t able to help.

For example, one user who wanted to analyze some documents started his conversation with:

> *Are you able to access the 2022 Local Control and Accountability Plan (LCAP) for the Visalia Unified School District?*

Once he learned that ChatGPT was not able to do that, he asked further questions to determine how he could get the bot to access those documents, only to eventually give up.

Another participant wasn’t sure whether ChatGPT could help with the creation of a business plan, so he started the conversation by asking *Can you help me create a business plan?* ChatGPT responded with a detailed structure of a business plan. While this information was accurate, it did require the user to read through a long response that wasn’t specific to his situation.

A better experience would involve the bot prompting the user with query refinements to help them articulate their question, as it did when a different participant asked for help generating a recipe.

*When asked for help generating a recipe, the bot requested further details to clarify the user’s needs before proceeding.*

*Can you* prompts are often asked by individuals who are new to AI or who are attempting a task with the bot for the first time. As users become more experienced with AI bots, such questions are likely to become rarer.

Note that sometimes people use *Can you* language to ask the bot to do something rather than inquiring about its ability. That is usually a query that provides more context than the very basic *Can you do this* query, like in the example below, where a user who wanted their resume rewritten referenced the text that needed to be edited:

> *Can you rewrite this? Hard-driving business leader offering skills…*

#### Tip for Designers of Generative AI

**Distinguish between the two****intents behind Can you language**:

- Well-specified prompts that include *Can you* language are directive: the bot is supposed to do the task.
- Underspecified, general prompts that include *Can you* language**need a brief answer; the bot should ask additional questions to help the user narrow down their query.

### Give Me More Prompts: Low Effort, Low Reward

Sometimes participants were unsatisfied with the bot’s answer and **asked for more options**. These kinds of queries usually occurred in conversations where the user had provided a broad, underspecified prompt with little or no framing, usually requesting a list of items (e.g., recommendations). If the items included in the bot’s list failed to elicit the user’s interest, the participant would ask for more options, without attempting to add framing to their prompt.

*When the gifts suggested by the bot were not to her taste, the participant asked for more options, without trying to explain what she was looking for.*

With *Give me more* prompts, **the user effort is minimal at the prompt level, but not at the conversation level** — it is likely that they will need to follow up with further prompts or query refinements that include more detail for their question.

*Give me more* conversations are least likely to result in success and users may, in fact, be better off by just using a search engine. As one participant put it:

> *I felt like I wanted more once again like more unique or more creative meals but it kinda kept giving me stuff that I already knew, and then I had to keep asking, like, ‘give me more’, ‘give me more.’ And, so, if I’m already having to ask it to give me more ideas, I feel like I might as well just go into Google and be able to scroll and click on the links that I think are gonna be answering my question how I want it to be.*

#### Tip for Designers of Generative AI

Bots should attempt to make *Give me more* prompts more specific by **asking framing questions and suggesting followup prompts** that help users define their query.

### Filler Prompts : Anthropomorphic Language

Filler utterances, which include polite phrases like *Thank you, Have a good night, Cute,* or *That was helpfu* l, have **no real communicative function,** but they do have a social function in human-to-human conversations. Such utterances reassure the conversation partner that their message was received and appreciated.

Our participants used fillers fairly often — [a sign that they were projecting anthropomorphic qualities](https://www.nngroup.com/articles/anthropomorphism/) to the bots.

*A participant asking about ways to decrease stress replied with the filler* Great. I will check out CBT.*This filler had no communicative function, but ChatGPT used the occasion to provide more information about cognitive behavioral therapy.*

Some users complained when the bots did not recognize some of the subtler fillers (other than *Thank you*, *That was great,* and similar) and, instead, treated them as regular prompts, providing an answer to them. Even though people could choose to ignore a response that they did not need, the response still required their attention.

*Bard did not recognize the filler* That looks really good *and assumed it was asked to provide an image for the spaghetti salad recipe in its previous answer.**A participant ended his exchange with ChatGPT by saying* Many would agree with you, *which the bot took to mean that he needed further convincing.*

#### Tip for Designers of Generative AI

Tools need to **distinguish fillers from information requests** to prevent users from feeling flooded with unwanted information.

## AI Prompt = the Visible Part of the User’s Information Need

The user’s information need is like an iceberg. The visible tip of this iceberg is the direct prompt, while the submerged layers are the critical mass that gives the prompt its true shape and direction. The more of these submerged layers is revealed in the prompt, the more effective the AI can be in meeting the user’s information need.

Including all the different components (request, references, format, and framing) in a prompt can help users get the most precise response. But sometimes this is difficult, due to several reasons:

- The user effort involved in uncovering and precisely describing some of these components is too large.
- The user lacks the [vocabulary or knowledge necessary to articulate some components](https://www.nngroup.com/articles/ai-articulation-barrier/) precisely (e.g., they may not know how to describe a desired tone of voice or a particular visual style).
- Some people do not want to share certain pieces of information due to privacy or data-confidentiality concerns.
- Many current AI interfaces lack sufficient support for uploading large amounts of contextual information into the prompts.

## Tips for Users of Generative AI

If you are getting started with generative AI and you want help with a specific task, **think of your information need as an iceberg:** the more you uncover of that need in your prompts, the higher the chance that the bot will provide something useful.

Prompts like *Best of* or *Give me more* are very inefficient — if you find yourself using them, it’s a sign that you may be better off with a search engine.

Requests, references, and many format specifications are relatively straightforward for most people (even though some of us may forget about the format when we first ask our questions). However, determining the right framing for a prompt can be tricky. First, uncovering all the contextual information takes effort — you have to think about it, articulate it, and finally type it. (That’s why it helps to have [a library of prompts if you’re likely to do the same task several times](https://www.nngroup.com/articles/ai-ux-getting-started/)). Second, providing too many unnecessary details can occasionally sidetrack the bot.

The current focus on prompt engineering and the popularity of roleplay framing in the media leads some users to assume that framing is just asking the bot to play a specific role. In fact, **a rich context specification is often essential but does not necessarily mean roleplay.**

If the framing for a question is too hard to figure out, **enroll the bot’s help** — prompt it to ask you questions about additional information that may be necessary for it to provide a specific answer.

However, **not all prompts need elaborate framing**. If your goal is less well-defined and you’re looking to learn about a new domain or get started in an area, you can safely begin with a general request and then use the bot’s response to determine the direction that the conversation should take.

## Recommendations for Designing the UX of Generative AI

The structure of the generative-AI prompts and conversations teaches us about what designers can do to improve the overall experience of generative AI and allow users to efficiently address their information needs.

In particular, designers should:

- Help users add **framing to their prompt** by proactively asking relevant questions and providing suggested followups that better define the problem instead of launching into a general-purpose response.
- Add UI elements that **allow users to select among certain possible formats** (e.g., list, table, visual) for the bot response. Allow them to also add additional attributes such as the number of words or the length of the response.
- Allow users to **easily reference back** previous answers by right-clicking selected answer fragments.
- Support the **upload of documents** and allow users to ask questions regarding particular parts of the document.
- Be sensitive to filler prompts and *Can you* prompts to determine what kind of response they require and whether they are meant to finish a conversation or, respectively, understand the bot’s capabilities.
