---
title: "Google AI Mode: Powerful Search, Poor Usability"
date: "2025-10-17"
url: "https://www.nngroup.com/articles/google-ai-mode/"
author: "Josh Brown, Kate Moran"
topics: [ai]
type: article
---

## In This Article:

- [What Is Google AI Mode?](#toc-what-is-google-ai-mode-1)
- [Conversational Format: Followup Prompts](#toc-conversational-format-followup-prompts-2)
- [Benefits of AI Mode: Supercharged Search](#toc-benefits-of-ai-mode-supercharged-search-3)
- [Our Study](#toc-our-study-4)
- [Problems with Google AI Mode](#toc-problems-with-google-ai-mode-5)
- [Conclusion](#toc-conclusion-6)

## What Is Google AI Mode?

Google AI Mode is a new feature of the search engine that combines the breadth of a web search with the reasoning power of a large language model (LLM). It’s essentially an open-end AI chat (like Claude or ChatGPT) but tailored to information seeking.

Users can search the internet by asking questions, receive comprehensive answers, and follow up with clarifying questions or additional requests.

*Google AI Mode: In response to the user’s question (* who was Alphonse Mucha *), AI Mode conducted a multi-query web search and returned a synthesized answer, along with related multimedia assets (in this case, examples of Mucha’s work) and cited sources with links.*

Anyone who’s used Perplexity might see echoes of it in Google’s AI Mode. Since its launch in 2022, Perplexity has been using AI to challenge the traditional approach to web search.

![Perplexity search interface displaying multimedia assets and linked sources in a layout similar to Google AI Mode's design approach.](https://media.nngroup.com/media/editor/2025/10/15/perplexity-mucha.jpg)

*Perplexity: Google AI Mode’s design has similar elements to Perplexity’s design — particularly the  emphasis on multimedia assets and linked sources.*

## Conversational Format: Followup Prompts

Unlike Google’s traditional search pages, AI Mode uses a conversational format similar to that used by many AI chatbots. This structure enables users to ask followup questions after the system’s initial response. AI Mode actively encourages conversations by offering clickable [followup prompt suggestions](https://www.nngroup.com/articles/prompt-suggestions/) (another feature shared with Perplexity).

![Google AI Mode interface showing clickable followup prompt suggestions at the bottom of a search response, with an open text field for custom questions.](https://media.nngroup.com/media/editor/2025/10/17/ai-mode-followup-prompts-lavender.jpg)

*AI mode offers clickable followup prompt suggestions at the end of each response. Users can choose one of those, or type their own in the open text field.*

This is a feature that differentiates AI Mode from Gemini and other AI chatbots — those tools sometimes fail to offer followup suggestions, or offer them as in-text suggestions. Compared to the clickable options in AI Mode, in-text suggestions require [more work](https://www.nngroup.com/articles/interaction-cost-definition/) for users because they have to accept the suggestion by typing in the text field.

## Benefits of AI Mode: Supercharged Search

AI-powered search tools like Google AI Mode and Perplexity are essentially supercharging and automating the traditional search process.

### Traditional Search Process

1. The user identifies information need.
2. They write a query containing keywords.
3. The query is executed by the search engine.
4. They explore results, gathering relevant information.
5. They revise the query and repeat as needed.

### AI-Powered Search

1. The user communicates information need in as many words as needed.
2. LLM interprets the need based on user’s prompt.
3. LLM generates several sub-queries (which may include keywords the user didn’t know, effectively [eliminating the keyword foraging problem](https://www.nngroup.com/articles/ai-information-seeking-keyword-foraging/) of search).
4. The subqueries are executed through traditional search indexes.
5. LLM compiles and synthesizes many search results into a relevant answer for the user (thus performing [the information-foraging step](https://www.nngroup.com/articles/generative-ai-diary/) for the user).
6. In “deep research,” this process may be conducted iteratively to more deeply explore a domain or problem space.

For example, if a user searches *best Mexican food Oakland* in Google AI Mode, the system may submit many related queries, like *Top taquerias in Oakland* and *Great Oakland Mexican restaurants*. The LLM then synthesizes the results, summarizes them, and presents the answer back to the user.

*Essentially, Google AI Mode interprets the user's query or prompt, generates many related search queries, and executes them. Then, it synthesizes the information it finds to provide an answer to users.*

Essentially, the AI-powered search is quickly conducting a broad, comprehensive series of searches that would take users hours to complete if done manually. This approach uses two techniques to expand the information-seeking value of LLMs: query fan-out and retrieval-augmented generation (RAG)

> **Query fan-out** is an information-retrieval technique in which an information need is translated into multiple related subqueries, which are run concurrently, possibly across different data sources, before blending the results into a summarized answer.

> **Retrieval-augmented generation (RAG)** is a technique that enhances LLMs by having them retrieve and reference external information before generating responses, instead of relying on training data alone.

Compared to pure LLM chatbots using only their training data, this approach is considered more reliable from an information-seeking perspective. Despite this, Google AI Mode did return false information and [hallucinate](https://www.nngroup.com/articles/ai-hallucinations/) during our study.

### Google’s Big Advantage: Information Ecosystem

Google AI Mode tailors its response and UI based on the query. Google’s structured, indexed knowledge is vast, which makes AI Mode even more powerful. When the system sees relevance to the query, it can return data from:

- Google Maps: Locations and reviews
- Google Shopping: Carousels of available products with pricing
- Multimedia: Images and video, particularly from YouTube

![Google AI Mode hotel search results for New York showing integrated data from Google Maps, reviews, and pricing with expandable details panels.](https://media.nngroup.com/media/editor/2025/10/15/ai-mode-nyc-hotels.jpg)

*AI Mode integrates data across the Google ecosystem, like maps, reviews, and shopping. In this example, it returned nicely formatted hotel options in New York, including price, rating, star level, and a short description. When clicked, each option expanded into an interactive side panel with details, as well as price quotes for the specific dates of the user’s trip.*

## Our Study

In a recent study on information seeking, 7 participants were encouraged to use AI Mode — if they didn’t naturally — when conducting online research on their own tasks.

Overall, participants were pleased with Google AI Mode. They appreciated the sources provided, suggested followups to continue the conversation, and information from products like Maps and Shopping embedded in the responses. However, we found several large usability issues that hindered some users from fully utilizing it.

## Problems with Google AI Mode

### Poor Discoverability

Currently, users can access Google AI Mode:

- from the Google homepage before searching
- through a new tab on Google search-results pages
- at the bottom of expanded AI Overviews

![Google homepage search bar showing AI Mode button with sparkly magnifying glass icon next to voice search and image search options.](https://media.nngroup.com/media/editor/2025/10/15/google-blank-ai-mode-button.png)

*On the Google homepage, an* AI Mode *button appears within the search field, next to the icons for voice search and image search. It’s a good thing that Google included the* AI Mode *label, since a sparkly magnifying glass would hardly be meaningful on its own.*

![Google search results page showing AI Mode tab and access button at bottom of expanded AI Overview, demonstrating poor discoverability placement.](https://media.nngroup.com/media/editor/2025/10/17/google-ai-overivew-mucha-lavender.jpg)

*AI Mode can be accessed from a tab or the bottom of AI Overviews on Google search results pages. However, to see the button, users must expand the overview content and scan all the way to the bottom of the (often very long) response. Even when participants did expand the AI Overviews during our study, they rarely noticed this button.*

You might think these multiple access points would be enough for Google users to easily discover AI Mode… but you’d be wrong.

[Like many AI features built into existing products,](https://www.nngroup.com/articles/discoverability-ai-amazon/)**AI Mode has poor discoverability** — meaning that people are unlikely to notice it on their own. While AI Mode can be accessed from several places, it’s still easy to miss. In our study, **4 out of 7 participants had not noticed or used AI Mode** before we directed them to it.

We hypothesize that the familiarity of Google’s interface contributed to this problem. All our participants (like many users today) were extremely familiar and comfortable with Google search — they knew what they needed to perform a search (the search box) and that they could safely ignore whatever else Google put on their screen. Additionally, people tend to be extremely task-focused when looking for information. They just want to answer their question, find what they need, make decisions, and move on with their lives — they aren’t visiting Google just to look around and see what’s new.

Google is likely aware of this discoverability problem and experimenting with ways to fix it. Since our research sessions, Google has added a shimmery rainbow outline animation that appears around the AI Mode button, likely in the hopes of drawing user attention to it.

![Google AI Mode button with shimmery rainbow outline animation designed to attract user attention and improve discoverability.](https://media.nngroup.com/media/editor/2025/10/15/google-ai-mode-button-rainbow.gif)

*Google added a shimmery rainbow outline animation around its* AI Mode *button to attract attention.*

But we’re skeptical that the animation will make much of a difference. The larger problem seems to be the vague “AI Mode” name and the lack of differentiation from Google’s other AI products and features.

### Multiple, Poorly Differentiated AI Products

A big hurdle in the use of AI Mode was the lack of clear differentiation from the rest of Google’s AI features. When participants encountered Google’s AI Mode, **their initial reaction was often confusion.** One participant confidently told us that he’d used AI Mode in the past, but it later became clear that he was thinking of past experiences with a different Google AI product.

With the addition of AI Mode, Google now offers three different paths for retrieving information with the help of AI.

System | Type | Description | Gemini | Open-ended LLM chat | A general-purpose chat that can access and search the web when needed | Separate product from core Google Search | AI Mode | AI-powered search chat | A mode within Google Search that’s tailored specifically for information seeking | AI Overviews | AI-generated summaries | A feature that automatically appears at the top of some Google search-results pages

![Google Gemini pulling from Google Search to answer a question about houseplants.](https://media.nngroup.com/media/editor/2025/10/15/gemini-monstera.png)

*Gemini is a standalone product and general-purpose AI chatbot that, when needed, can access Google Search.*

![AI Mode is listed in the tabs as an additional feature (like Google Image Search) of Google Search.](https://media.nngroup.com/media/editor/2025/10/15/aimode-monstera.jpg)

*Google presents AI Mode as an additional search option, similar to image or video search.*

![A Google AI overview which appears under the query of a normal search.](https://media.nngroup.com/media/editor/2025/10/15/google-monstera.jpg)

*Traditional Google search-results pages may include AI overviews in response to some queries.*

When asked about AI Mode, **participants often conflated it with these other AI features.**

> “And this doesn't give me Gemini?”
> 
> 
> 
> "But isn't Gemini Google as well? They're not the same, though.”
> 
> 
> 
> “I've seen it, but I thought it was just how you search for a product or something. It gives you quick AI information. I thought it was just that.**** That's why I never clicked on it, because I just assumed it was the same information that you get when you quickly search for something on here.”

The distinction between these three AI offerings is not immediately clear to users, and there’s a fair amount of overlap in their functionality. All three use Gemini (the LLM) models and can execute web searches.

This confusion is unlikely to improve in the short term and may even be a bit intentional from Google’s perspective. In Google’s [announcement of AI Mode](https://blog.google/products/search/google-search-ai-mode-update/#deep-search), Elizabeth Reid (head of Search) indicated that features that perform well in AI Mode will be integrated into core Google Search. If anything, the distinction between these three offerings will likely become blurrier and more confusing to Google users.

### Missed Onboarding Microcopy

Even though the AI Mode’s welcome page contains useful information, our participants never saw it. The only way to view the page was to click the *AI Mode* button from the empty search box on Google’s homepage, and none of our participants accessed it in that way. Many Google users will also overlook the onboarding pages because modern browsers typically feature a default search feature that allows users to enter queries directly into the URL bar.

**Help and explanatory text is only useful if people see it.**

![Google AI Mode welcome page showing onboarding guidance and personalized prompt suggestions based on a user's recent activity and interests.](https://media.nngroup.com/media/editor/2025/10/17/ai-mode-blank-lavender.jpg)

*The AI Mode homepage offered guidance like* Ask detailed questions for better responses *and*[prompt suggestions](https://www.nngroup.com/articles/prompt-suggestions/)*, but our participants missed it because they bypassed this page. When users are logged into their Google accounts, the suggestions are tailored to their recent activity. (This screenshot was taken from Kate's account, and she does actually spend a lot of time in museums and reading about AI developments.)*

That’s a problem, because people are pretty ingrained in their longstanding information-seeking habits, and it will take them some time to adapt their queries to AI-based search.

For example, **participants in our study relied on traditional keyword phrases** like *shop refrigerator smart* instead of asking natural-language questions.

Or, at times, **participants did not realize they could ask followup questions** in the chat. One participant repeatedly used Google search to reenter AI Mode, while another used the back button, expecting to return to a previous response, only to leave AI Mode and lose the entire conversation.

### Wordy, Unformatted Responses

AI Mode suffers from a problem common across all LLMs: it provides [thorough but overly long responses](https://www.nngroup.com/articles/genai-write-for-the-web/), which discourage and overload users.

At best, **participants quickly skimmed or skipped to the bottom of the response for a summary**. But in other cases, the amount of text caused participants to abandon AI Mode entirely. One participant told us they would go back to manual, traditional searching.

> “So, at this point, to be honest, I get a little bit [lost]. Like this is just too much.”

![Google AI Mode response about hand-held steamers showing 5 paragraphs of dense, unformatted text that overwhelmed a participant.](https://media.nngroup.com/media/editor/2025/10/15/aimode-steamer.jpg)

*While using AI Mode to search for a hand-held steamer, one participant received a response that was 5 paragraphs long with very little formatting.*

Sometimes long responses can’t be avoided, but [simple formatting](https://www.nngroup.com/articles/formatting-long-form-content/) (bold text, subheadings, bulleted lists) make them easier to read. Additionally, [collapsible sections](https://www.nngroup.com/articles/accordions-on-desktop/) could allow users to control the amount of visible text and, thus, make browsing smoother.

### Lost in Long Conversations

AI Mode’s ability to support information seeking through a conversation that can build over time was often an advantage over traditional, one-query-at-a-time search. It allowed participants to explore complex information needs in more depth. But after a few exchanges, the conversation thread became quite long (exacerbated by the AI Mode’s tendency to give wordy responses). As a result, particularly on mobile, revisiting the results of a previous query **required a lot of scrolling.**

One participant spent several minutes chatting with AI Mode in her search for a refrigerator She noticed that one option offered by LG included access to a “ThinkQ App.” Unfamiliar with this oddly named app, she asked AI Mode about its purpose. Once she understood what it offered, she began scrolling back through her conversation, trying to find the LG fridge she had seen earlier. However, she struggled to locate it and eventually wondered if it would be easier to just ask AI Mode to provide the link again.

> “I don't know if it’s faster to just type it [again] or just look back up for it.”

*With no way to jump back, participants have to scroll and scan for previous responses.*

**Adding**[jump links](https://www.nngroup.com/articles/in-page-links-content-navigation/)**or a**[table of contents](https://www.nngroup.com/articles/table-of-contents/) pointing to various questions within a thread would save users a lot of effort and allow them to easily refer back to previous answers. This is critical on mobile devices, where moving back and forth within a conversation will require excessive scrolling.

### Mismatch with Users’ Mental Model

Another issue related to navigation was that **the tabs in the persistent top tab bar**(containing *AI Mode,**All, Shopping, Images*, etc.) **lead to search results relevant to the first query in the AI-Mode conversation,** instead of reflecting the most recent user question in the conversation.

![AI Mode is featured in the tabs of Google Search along with options like Images and Videos.](https://media.nngroup.com/media/editor/2025/10/17/google-ai-mode-hydrangea-lavender.jpg)

*AI Mode is presented as a tab, alongside Videos, Short videos, Images, Forums, Shopping, and Maps. These other tabs are actually scoped search tools, narrowing the user’s query to a specific kind of information or media. AI Mode violates that expected behavior, because it isn’t just another way to filter or format search results.*

For example, one participant started by researching *Mexican restaurants* in an area, but her conversation eventually evolved to *best hikes*. When she clicked on the *Images* tab in the top tab bar, she was shown pictures of restaurants, not hikes. This disconnect was jarring and broke her workflow.

> “That was kind of confusing to have all your restaurants. And then I switched over to hikes, but this up here [the *Images* tab] was back to restaurants. So, I had to go back.”

This is an example where users’ [mental model](https://www.nngroup.com/articles/mental-models/) clashes with designers’ conceptual model. Conceptually, the AI Mode page is a tab within the search-results page and a followup question asked within the AI Mode conversation is not a new query; the tabs are thus relevant to the current query — that is to the query entered in the search engine. To the user, however, any question, regardless of where they asked it, counts as a query.

### Hallucinations

Like all LLM-powered chats, AI Mode is not immune to [hallucinations.](https://www.nngroup.com/articles/ai-hallucinations/) It tries to mitigate this **by including references and sources to build user trust**. These were well received by participants but **did not solve the hallucination problem.** Like any LLM, its behavior seemed to be less reliable for niche topics, especially.

When a participant attempted to utilize Google AI Mode to look for scientific studies about a specific niche neuroscience topic, he was initially impressed by its ability to source relevant papers. But, upon closer inspection, it became clear that the paper and its author did not actually exist.

In this specific example, the expert user caught the error quickly. But this will not be the case for all users, particularly for those relying on the AI to summarize or compare information they are unfamiliar with.

## Conclusion

AI Mode is a powerful tool if you know how to find and use it — which is a big “if,” considering the range of usability problems we observed.

Google’s wide reach as a major search engine means many of its users are less familiar with new technologies such as AI. To help these users benefit from AI features, Google should offer a clearer value proposition and improved onboarding.

One participant, previously unaware of AI Mode, highlighted the importance of addressing these usability issues:

> “I'd have to play around with it a little bit more to not get lost or not but (...) I think I might try it, use this instead of just regular Google. I don't know. We'll see. Because I'm still like, set in my ways too.”

This hesitation also applies to users with more exposure to AI, as the conversational nature of AI Mode may conflict with their established mental model of a Google search.

However, once the usability issues of AI Mode are addressed, Google will be able to build on its existing dominance in the search space. The fact that people are “set in their ways” or have an existing mental model of Google search means they've already established a habit of using it. By demonstrating the value of AI mode, effectively onboarding users, and connecting AI Mode responses to the wider Google ecosystem (such as Shopping and YouTube) in the responses, AI mode will be well-positioned to compete with other AI chatbots and AI-based search engines as they become mainstream.
