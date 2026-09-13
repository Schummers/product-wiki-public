---
title: "Prompt Controls in GenAI Chatbots: 4 Main Uses and Best Practices"
date: "2024-08-02"
url: "https://www.nngroup.com/articles/prompt-controls-genai/"
author: "Feifei Liu"
topics: [ai, design-patterns]
type: article
---

## In This Article:

- [Adding UI Controls to Prompting](#toc-adding-ui-controls-to-prompting-1)
- [Main Uses of Prompt Controls in GenAI UIs](#toc-main-uses-of-prompt-controls-in-genai-uis-2)
- [Best Practices for Prompt Controls in GenAI Chatbots](#toc-best-practices-for-prompt-controls-in-genai-chatbots-3)
- [Conclusion](#toc-conclusion-4)

## Adding UI Controls to Prompting

Generative AI (genAI) chatbots, such as ChatGPT and Perplexity, rely heavily on [text prompts](https://www.nngroup.com/articles/careful-prompts/) from their users. As these interfaces continue to evolve, AI chatbot designers have started to **introduce additional UI controls** in addition to the simple prompt field and thus create [hybrid UIs](https://www.nngroup.com/articles/ai-paradigm/) for genAI chatbots.

> Definition: **Prompt controls** are UI components that surround the input field in an AI-chatbot interface. Their role is to expedite and supplement text input.

Prompt controls can be displayed in different formats, such as buttons, tooltips, toggles, cards, and menus.

Prompt controls help users expedite prompting, clarify ambiguity, and get inspiration. They also facilitate followups. Ultimately, they help [overcome the articulation barrier](https://www.nngroup.com/articles/ai-articulation-barrier/) and, thus, lead to more-useful bot responses, benefiting both existing and [new users](https://www.nngroup.com/articles/new-AI-users-onboarding/).

## Main Uses of Prompt Controls in GenAI UIs

According to our research of prominent text-based genAI chatbots in the US and China, there are four ways in which prompt controls are used in these interfaces:

- Increasing the discoverability of AI-chatbot features
- Educating users and offering inspiration
- Setting constraints for conversations
- Facilitating followups

### Increasing Discoverability of Chatbot Features

Unlike pure text-based UIs, prompt controls allow users to discover the different bot capabilities and, as a result, have lower [interaction costs](https://www.nngroup.com/articles/interaction-cost-definition/): people don’t have to ask the bot whether it can do a certain task ([“can you” prompts](https://www.nngroup.com/articles/ai-prompt-structure/) are common among new users).

For instance, in [our diary study of an early version of ChatGPT](https://www.nngroup.com/articles/generative-ai-diary/) (that couldn’t access the internet or accept uploaded files), one participant wanted the bot to summarize an online report. After several prompt exchanges, he finally understood that he would have to copy and paste the 100-page report. He deemed this approach extremely painful and stopped using the bot for document summarization.

With the current ChatGPT, users can upload **** diverse types of files to supplement their text requests or choose files from online storage services like Google Drive. Still, people need to ask the bot about the types of files it accepts. In contrast, Baidu's Ernie bot indicates the supported file formats in a tooltip as users hovered over the upload icon.

*ChatGPT supported multiple file types as input, including documents, spreadsheets, data files, and images, from both local devices and cloud storage. Still, users had to ask the system about the supported file types.**As users hovered over the Upload icon, Baidu's Ernie showed a tooltip indicating the supported file types and the corresponding file-size limitations.*

### Educating and Offering Inspiration

Our research found that [new users had a difficult time understanding what a genAI bot can do and how it can be used](https://www.nngroup.com/articles/new-AI-users-onboarding/). Visible prompt controls can offer a glimpse into what kinds of tasks genAI can be used for. (Don’t forget that, worldwide, many online users are still new to GenAI. For instance, a [Reuters survey found that 19% of US participants and 30% of UK participants have never heard of any of most popular GenAI tools, including ChatGPT, Google Gemini, or Microsoft Copilot](https://reutersinstitute.politics.ox.ac.uk/what-does-public-six-countries-think-generative-ai-news).)

For example, the Chinese AI chatbot SparkDesk shows a list of plugins next to the prompt. One of them, *Smart PPT Generation,* generates PowerPoint files; this feature would have been a lot harder to discover without the prompt controls.

*The Chinese genAI chatbot SparkDesk listed its plugins, such as* Smart PPT Generation *, above the text fields. These prompt controls helped users understand what they could ask the tool to do and what types of output files they could expect.*

A common pattern that is starting to emerge in genAI bots is the inclusion of one or more **conversation starters.** These are task examples that aim to teach users what the bot can do.

*The* New in Claude *component educated users about the tool’s capabilities by offering a set of s conversation starters. Users could click on these to start a conversation.*

Some Chinese GenAI tools, like ChatGLM, provided a comprehensive library of prompts called *Inspiration Center* in the side panel. About 10 prompts were listed in the panel, allowing users to directly use them or edit the example prompt by clicking the *edit* icon. High-level tags like *Writing, Developers,* and *Parents* at the top of the panel allowed people to browse more prompt examples in that category *.*

*ChatGLM provided a prompt-library side panel. Users could click on the tags at the top of the panel to get prompt examples relevant to them; they could then directly use the examples or modify them as needed.*

### Setting Constraints for Conversations

Prompt controls are also used to set constraints to conversations with chatbots. For example, they can specify the scope that users want the bot to focus on or a specific output format.

For instance, the *Focus* feature in Perplexity allowed users to scope a specific domain to focus on, narrowing down the conversation from the beginning , like a [scoped search experience](https://www.nngroup.com/articles/scoped-search/) would narrow down search.

*Perplexity.ai provided a* Focus *feature, which allowed users to narrow down the search domain to* Reddit *,*YouTube*, and *Academic*.*

The Chinese GenAI chatbot Baidu’s Ernie bot allowed users to **designate output specifications** when they were working with certain plugins. For instance, after turning on the plugin *TreeMind*, users could create diagrams such as a fishbone diagram and directly edit the output as needed.

*Baidu’s Ernie bot allowed users to designate output specifications, such as various types of charts, after turning on the* Treemap *plugin*

### Facilitating Followups

In a diary study with genAI users, we found that [half of all conversations contained a followup action](https://www.nngroup.com/articles/generative-ai-diary/), and 77% of the conversations included more than 1 exchange. Followups and multi-prompt exchanges were especially likely when people [explored](http://nngroup.com/articles/AI-conversation-types) a new topic — in these cases, they would use subsequent interactions to acquire more in-depth knowledge on that topic.

Thus, another main function that prompt controls serve is to facilitate the back-and-forth followup process. ChatGPT’s UI **featured a nice set of followup actions** that users could take upon receiving an answer:

- Edit the previous prompt
- Have the bot read the answer aloud
- Copy the answer
- Regenerate the answer
- Provide feedback
- Change the AI model that processes the query

*ChatGPT offered a variety of followup actions at the bottom of each response it provided. They allowed users to change their prompt quickly. (Unfortunately, these icons were unlabeled, and they were not all standard. This common design mistake often hinders discoverability for new users.)*

Sometimes, people also refer to previous responses and ask the bot to modify a specific part, especially when working on text generation and editing tasks ([a behavior known as apple-picking](https://www.nngroup.com/articles/accordion-editing-apple-picking/)). Some chatbots (like the Chinese genAI chatbot ChatGLM) provide an inline quotation feature that decreases the amount of user effort for this interaction. Users need only to highlight and quote, instead of highlighting, copying and pasting in the input field.

*ChatGLM, a Chinese chatbot, allowed users to quote a snippet from a previous answer by clicking a* Quote *button as they highlighted some text (top). After clicking the button, the quoted text appeared above the input field, and the placeholder text prompted users for followup questions (bottom).*

Google Gemini went one step further and integrated commonly used simple followup requests such as *Shorter, Longer,* and *More casual* into a modification button. These requests can be helpful for text-generation tasks.

*Google Gemini provided some quick one-click followup requests like* Shorter *in the* Modify response *feature.*

Some chatbots provide relevant followup question suggestions as users start a conversation. These followup questions serve two functions:

- Save user from manually typing relevant in-depth questions
- Provide inspiration for other questions

For instance, when asked about foldable smartphones, Perplexity provided three related questions and options to *Search Videos* and *Generate Images,* since foldable smartphones could be demonstrated more effectively via video.

*Perplexity: Followup questions and suggestions for a conversation facilitated an in-depth conversation and broadened the search scope (video search and image generation).*

## Best Practices for Prompt Controls in GenAI Chatbots

Based on the top usability issues we observed in both US and Chinese genAI chatbots, we offer 4 tips for prompt controls.

### #1: Use Standard Icons and Labels or Tooltips

We’ve argued that [icons need labels](https://www.nngroup.com/articles/icon-usability/) for a long time because there are few universally recognized icons. In the context of GenAI tools, pairing icons with descriptive labels is even more important **because users tend to have little domain knowledge and have not yet formed**[mental models](https://www.nngroup.com/articles/mental-models/)**for how these bots work and what they can do.** In this case, using unconventional icons without accompanying text labels can cause even more confusion.

ChatGLM, a Chinese GenAI chatbot, included straightforward, standard icons for favorites, thumbs-up, thumbs-down, copy, or share at the bottom of each reply. All participants in our study readily understood these icons.

*✅ The Chinese generative Ai chatbot ChatGLM included straightforward icons at the bottom of each reply (top); a tooltip appeared as users hovered over each icon (bottom).*

If apps use novel icons to represent new, unfamiliar features, people might not be able to guess what the associated buttons may do and ignore the feature.

For instance, the Baidu’s Ernie mobile app used a magic wand icon beside the input field, to represent a set of prompt examples. None of our study participants understood what that icon meant; one user commented:

> “*I initially thought [is that] it would show me images, like emojis.”*

*❌  Baidu’s Ernie mobile app: The magic-wand icon puzzled all study participants. They either overlooked it or misguessed what it would do. In fact, it provided some prompt examples.*

A previous version of Bing Chat used a broom icon for starting a new conversation. This icon was not easy to understand. Luckily, a more recent version fixed this issue by using a more relevant icon (a conversation icon with a plus sign at the bottom right) together with the label *New topic* upon hovering.

*❌  Top: In a previous version of Bing Chat, the broom icon at the left of the input field was used for starting a new conversation. This icon had no label and was hard to understand. ✅  Bottom: A more recent version of Bing Copilot AI used an easier-to-understand icon (a speech bubble with a plus sign at the bottom right) to illustrate the feature, and its label* New topic *will appear as users hovered over the button.*

### #2: Clearly Name Features

Another common issue we observed was the use of vague, branded names for prompt controls. When labels accompanying icons fail to precisely describe their functionality, they don’t add context effectively. Baidu’s Ernie bot had a plugin named *Think Carefully.* One participant asked,

> “‘*Think Carefully’. So, think carefully about what?”*

Another plugin’s label was ambiguous. The Chinese name of the plugin was "一 *键流影"*, which was intended to mean *One-click to transfer videos*. However, one character in this label, *流*, has multiple meanings in Chinese, such as *stream*, *flow*, *circulate*, and *fluid*. A few study participants were uncertain about the plugin's function. Renaming it *Text to Video* (文字转视频) could remove the ambiguity.

*Ernie: Vague plugin labels such as* Think Carefully *confused participants in our usability study.*

### #3: Group Prompt Controls Based on Their Functionality

Users can feel overwhelmed when presented with lots of new features at once. We can guide them through a new interface by grouping elements that are related (thus, applying [the Gestalt principle of proximity](https://www.nngroup.com/articles/gestalt-proximity/)). Some genAI tools in our study failed to properly group prompt controls, increasing the learning cost and the chance that users would overlook those components.

For instance, a previous version of Baidu’s Ernie bot included a plugin hub, where users could choose to enable specific functionalities of the bot, such as creating a video based on text. However, the list of plugins was overwhelmingly long (10–15 items), and the functions they served varied a lot, including:

- Providing context: *File Upload* and *Image Upload*
- Setting scope: *Baidu Lawyer* and *Business Info Lookup*
- Specifying output formats **:*** TreeMind*(exporting data charts), text-to-image, and text-to-video

In addition, these distinct functions were hidden in the same *Plugin* button and named with branded labels, which further lowered their discoverability. In our study, when asked to create a video using the Ernie bot, none of the participants found the hidden text-to-video feature within the plugin hub. Even after the researcher pointed them to the right place, it took them quite a bit to understand what each plugin was for.

**Grouping plugins with similar functionality under clearly labeled categories can help users understand their purpose more quickly and smoothly.**

*❌ Ernie: The plugin hub contained a variety of plugins, with no hierarchical organization. This lack of structure made it hard for participants to find specific plugins or discover what kinds of plugins were available. (A more recent version of Ernie improved by placing* File Upload *and* Image Upload *features right above the input field and retired the plugin hub.)*

In contrast, Perplexity separated 2 features, *Focus* and *Attach*, instead of putting them in one contextual menu, since they served different purposes: the former was to set the scope of the conversation, while the latter allowed users to provide more background information. Still, since they both served to ask for user input on context, they were placed next to each other and far away from the *Send* icon or the toggle to switch to *Pro*.

*✅ UI components serving different purposes,* Focus *and* Attach *, were separated on the Perplexity’s interface with concise labeling.*

### #4: Follow Interaction-Design Conventions

The last but not least-common mistake made by genAI tools is failing to follow [existing design conventions](https://www.nngroup.com/articles/consistency-and-standards/). **Unconventional design patterns, even when deployed with good intentions, can cause confusion, increasing the perceived complexity of tools**. This is because users’ mental models tend to have strong inertia and are based on their prior experience with thousands ofother products. As [Jakob’s law of Internet user experience](https://www.nngroup.com/videos/jakobs-law-internet-ux/) says, users spend most of their time with much more time on other products than yours, so it’s always safer to obey current design conventions unless you have strong reasons to do so again.

In our study, we encountered many cases where violating design conventions caused confusion, both intentionally and unintentionally.

For instance, ChatGLM’s mobile app hijacked the normal gesture of long-pressing a previous entry to show the *Copy* tooltip. Whenever a user performed that gesture, the app would copy and paste the full prompt text. However, this greatly confused study participants and added extra burden for those who wanted to copy only a slice of a previous entry — they had no choice but to copy the full content and delete undesired parts.

*❌ The ChatGLM mobile app hijacked the conventional tooltip when users long-pressed a previous message sent to the bot. This nonstandard behavior confused a user who was trying to copy and modify a previous prompt.*

In contrast, ChatGPT’s mobile app also repurposed the long press, but in a more thoughtful way that did not completely override the standard functionality. When a user long-pressed part of a previous prompt, it provided a contextual menu with multiple options, including copying the full message or selecting a text snippet.

*✅ The ChatGPT mobile app: When the user long-pressed a previous prompt, a contextual menu displayed the standard* Select Text *option along with other useful options (such as copying the entire prompt or editing it).*

Sometimes, design conventions are unintentionally violated on new products due to limited time. Though it might be important for the product and market teams to launch novel features as soon as possible, usability shouldn’t be sacrificed in the process.

For instance, in our study, the Ernie bot would tell users that it couldn’t process documents larger than 10MB only after users uploaded a file exceeding the size limit. Moreover, the error message was displayed in a small [nonmodal popup](https://www.nngroup.com/articles/modal-nonmodal-dialog/) at the top of the screen, far from the *Upload* button (at the bottom right of the screen). One study participant tried to upload the same file multiple times and was confused as to why nothing happened — he totally overlooked the error message, also because the popup was automatically dismissed upon any click or scroll.

*❌ Baidu’s Ernie bot: The error message regarding oversized files was shown in a small, nonmodal overlay at the top of the screen (bottom), very far from the users’ focus of attention as they had just used the Upload button at the bottom of the screen (top).*

## Conclusion

Prompt controls in genAI chatbots increase the usability by decreasing the interaction cost, as commonly used commands can be executed with a click instead of typing.

Designers for prompt-based genAI tools should look for opportunities to better integrate prompt controls **into the conversational interface**, with **the goal of minimizing manual input, increasing feature discoverability, and allowing users to easily set scope and other constraints for their conversations, as well as get inspiration, and easily follow up with additional prompts**.
