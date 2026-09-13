---
title: "ChatGPT, Bard, or Bing Chat? Differences Among 3 Generative-AI Bots"
date: "2023-10-01"
url: "https://www.nngroup.com/articles/ai-bot-comparison/"
author: "Amy Zhang, Emma Cionca, Feifei Liu, Raluca Budiu"
topics: [ai]
type: article
---

One of the benefits of the generative-AI bots is that [they shortcut the task of information foraging](https://www.nngroup.com/articles/generative-ai-diary/). They aggregate pertinent information from multiple sources for users — saving them the effort of inspecting different web pages, extracting relevant information, and then combining it into a coherent answer.

In a diary study conducted with three bots, we found that people rated the conversations with these bots as highly helpful and trustworthy. However, there were some differences in the ratings for the three bots, due to their different capacities and interfaces.

## In This Article:

- [Our Research](#toc-our-research-1)
- [The Three Bot Interfaces](#toc-the-three-bot-interfaces-2)
- [Helpfulness and Trustworthiness Ratings](#toc-helpfulness-and-trustworthiness-ratings-3)
- [Why Was Bing Chat Rated Lower?](#toc-why-was-bing-chat-rated-lower-4)
- [User Experience: Essential for the Design of Successful AI](#toc-user-experience-essential-for-the-design-of-successful-ai-5)
- [Best Practices and Design Recommendations for Generative-AI Chatbots](#toc-best-practices-and-design-recommendations-for-generative-ai-chatbots-6)

## Our Research

We ran a diary study with 18 participants: 8 used the newest version of ChatGPT (4.0), 5 used Bard, and 5 used Bing Chat. The participants had various levels of experience with the chatbots: some had used them before, some had used one bot but tested another in the study, and others had heard about them but had not used them.

Participants logged all their conversations with the bots over a period of approximately 2 weeks. At the end of the diary study, 14 participants were invited for in-depth interviews. The study was conducted in May and June 2023.

## The Three Bot Interfaces

The three bots we studied had different user interfaces and capabilities.

### ChatGPT

ChatGPT did not have access to the Internet and provided primarily textual information as output. It automatically saved conversation history, allowing users to revisit previous interactions with the bot. At the time of the study, none of the other bots provided this capability in a consistent manner. (Bing Chat’s history was available only to some users.)

**ChatGPT:***The interface available at the time of the diary study included buttons for regenerating responses, a quick binary-rating system (thumbs up or down), conversation history, and settings.*

### Bard and Bing Chat

Unlike ChatGPT, Bard and Bing Chat were able to return multimedia in their responses, which included links and images. In addition, Bing Chat was capable of embedding videos directly in its responses.

Bing Chat also provided sources for some of its answers and suggested additional followup questions to the users. At the time of the study, it was also the only bot that had image-generation capabilities.

**Bard:***The interface was fairly similar to ChatGPT's. However, Bard did not allow access to the complete text of the past conversations.***Bard:***Some Bard answers included images and links. The links were placed at the top right of the images in a tag format and usually pointed to product or site recommendations mentioned in the answer.***Bing Chat:***Bing Chat’s interface elements at the time of the study included references (in-text, as links, and also as footnotes, listed in the* Learn more section *), suggested followup queries, and a conversation history that was available to only some of its users.*​​**Bing Chat:***Bing Chat’s responses could contain images and videos, as well as ads.*

Functionality and UI Features of the 3 Generative-AI Bots | Bard | Bing Chat | ChatGPT | Text generation | Yes | Yes | Yes | Image generation | No | Yes | No | Output format | Images, Links, Text | Images, links, text, videos | Text | Access to Internet | Yes | Yes | No | References | No | In-text footnotes/links & | Learn more | links | No | Suggested followup questions | No | Yes | No | Chat history | No (at the time of study) | Limited users | Yes | Ads | No | Yes | No

## Helpfulness and Trustworthiness Ratings

Bing Chat’s helpfulness rating was significantly lower than those of Bard (p <0.001) and ChatGPT (p = 0.006). Bard was also rated as more helpful than ChatGPT (p=0.03; however, with a Bonferroni correction, this difference is only marginally significant). The bots also had some differences in trustworthiness ratings: Bard and ChatGPT were perceived as more trustworthy than Bing Chat (p<0.002). There was no difference in the trustworthiness perception between Bard and ChatGPT.

*Bing Chat had significantly lower helpfulness and trustworthiness scores than Bard and ChatGPT.*

## Why Was Bing Chat Rated Lower?

It is surprising that Bing Chat was rated lower than ChatGPT and Bard, especially since Bing Chat and ChatGPT both use Open AI’s GPT.

We believe there are two big reasons for Bing’s poorer ratings:

- **Poor information foraging:** Broad answers that did not always perform information aggregation or performed it only at the surface level
- **User-interface issues:** A UI, with potentially useful but poorly executed elements that did not support users well enough and sometimes distracted them from the task at hand

### Poor Information Foraging

Information foraging is the behavior that users engage in whenever they need to satisfy an information need on the web. It involves:

- finding potential sources of information (often with the help of a search engine)
- evaluating them and picking the most promising ones
- aggregating the information from those sources and making sense of it

That last step, aggregation of information, is present in many (but not all) user tasks. In simple tasks such as finding an address or specific website, that step may be absent. But in many other tasks, from shopping online to researching a new technology or device, information aggregation is essential.

For example, when shopping, we often see people save multiple candidate products (sometimes [in different browser tabs](https://www.nngroup.com/articles/multi-tab-page-parking/)) and then review all of these to decide which are best for their needs. Or, in research tasks, users often go to multiple sites, extract information from each (often by copying and pasting it into a file or some other form of [external memory](https://www.nngroup.com/articles/working-memory-external-memory/)), then revisit and combine all the gathered information in order to make a decision or reach a conclusion.

One of the major advantages of AI bots over traditional search engines is that they can do the entire task of [information foraging](https://www.nngroup.com/articles/information-foraging/) (including the aggregation of information) for the user. Much of Bing Chat’s lower rating scores are explained by the fact that **it does not always perform information aggregation,** or only performs it **at the surface level**.

Several users complained that, instead of providing solid answers to their questions, Bing Chat sent them to webpages where they could look up the answers for themselves. Thus, it was still the user's job to combine the different pieces of information — which is exactly what search engines require. Participants felt that **Bing Chat’s response was no better than what a search engine would provide**.

For instance, one participant looking for chainsaw recommendations complained that Bing Chat’s response contained no detail:

> *I feel like it took some prodding. When I said I wanted to buy a chainsaw, its first response was ‘here are four chainsaws from consumer reports’ with no additional information. I feel like it could have tried to gather more information , like price or features I was looking for.*

*One participant complained about the too little detail provided by Bing Chat in response to the* prompt I want to buy a chainsaw.

Another study participant asked Bing Chat for *the best way to cook a steak*. He had hoped that the bot would aggregate the best methods and give him pros and cons of each one. Instead, it provided a bland list of four methods, with no additional information. He had to navigate to a *Learn more* link provided by the answer. That page answered his question perfectly. The participant rated the helpfulness of this answer as 4 (out of 7) and commented:

> *I understand that is a subjective question, but it responded with four answers without giving the pros and cons to them. It also did not explain how to do anything […] It just included links to different websites to go read. One of the links was what I was expecting the answer to be. Four best ways to cook a steak with how to do it and the pros and cons. It was a good Bing search result, but not great chat experience .*

*One participant was unsatisfied with the information provided by Bing Chat in response to the question* what **is the best way to cook a steak*(top). He had to navigate to one of the links it recommended, the Spruce Eats, to find four methods to cook a steak and their pros and cons (bottom).*

In contrast, when asked a similar “the best way to do…” question, Bard did a better job of aggregating relevant information.

For example, when a participant asked the best ways to tread water, Bard provided her with several methods and included images showing the movements. It concluded with tips for treading water effectively. She was highly satisfied with the improvement in efficiency provided by Bard:

It gave me sufficient information with all the tips I needed. It gave me a quick answer to simple question **without digging through internet for the best information**.

*Bard provided a detailed answer to the question* the best ways to tread water *, with detailed instructions and illustrations on each technique. (The screenshot was taken from the extension MyChatGPT, which study participants used to share the conversations with us; the interface might look different from the actual Bard interface.)*

When other general issues (such as **inaccurate links and broad answers without considering the context**) are intertwined with poor information aggregation, people became extremely frustrated with the bot, as illustrated by the following quote from one of our participants:

> *Here's the answer to your question, but you're gonna have to go over here to get the specifics of what you want. And [Bing Chat] doesn’t put it all in front of you. It sends you someplace else to get the answer. It's […]  like if you ask a librarian […] ‘What is the book Seven Wonders of the World about?’ And she says, ‘Okay, go, go down the second aisle, look up on the top left shelf, you, you're gonna see the book, […] as well as the other works from that author.*

People tried to come up with theories about what may cause the bot to perform poorly. One person decided that Bing was not good at finding current or local information but was okay with more general queries. Another participant **described Bing Chat as unpredictable**. He was especially frustrated when he found Bing Chat performed even worse than a search engine on some occasions. He commented:

> *Bing Chat is, I’d say, hit or miss because I can never really predict what I'm going to get […] There were some chats that I thought it did a very good job and it […] even got me to ask questions that originally […] I wasn't going to ask. […] But then there were others where it really didn't. And the funny thing was I couldn't predict.*

### User-Interface Issues

Bing Chat had the richest user interface: it had a lot of features (e.g., references, suggested followup queries) that were not present in the other bots’ interfaces. We believe that, ironically, that fact contributed to its lower ratings.

Whereas, in theory, many of these elements could be useful additions, they were **often imperfectly executed and, instead of helping the user, they****got in the way**. This result emphasizes the importance of user experience in the design of AI bots.

Across all bots, people interacted with some of the other UI elements available (other than the chat) in 33.64% of conversations (95% confidence interval: 29.32% to 38.28%). ChatGPT and Bard had relatively sparse interfaces compared with Bing Chat, so it is not surprising that those few additional features were not used much (24.74% for ChatGPT and 31.86% for Bard; **These were both significantly lower than Bing Chat’s percentage, which was 50%**(p <0.004). Many of the interactions with ChatGPT’s or Bard’s UI involved the thumbs-up or thumbs-down buttons, which gave feedback for a conversation.

*Bing Chat’s UI was used significantly more than the UI of the other chatbots.*

In what follows, we discuss the issues that participants encountered with Bing-specific interface elements.

#### References

At the time of the study, Bing Chat was the only bot that provided sources for the different pieces of information in its answers. Sources were linked in the text and also listed in the *Learn more* section below the answer.

References are an extremely valuable feature for AI chatbots. They help users understand where the synthesized information originated from, which is necessary to determine how much it should be trusted. However, in Bing’s case,**the presence of sources sometimes contributed to the lower ratings; If the sources did not seem relevant or specific enough,** they reflected poorly on the judgment of the answer.

For instance, one participant was annoyed that the first source that Bing Chat provided to the question *what should I know about having a baby* was from a Canadian source. He said:

> *I did not like that the advice in first answer was to consult the Public Health Agency of Canada. I live in the United States so I would want to hear advice from a US agency or site as there could be differences in healthcare or services or policies.*

*A US participant did not like that the first source listed by Bing Chat was Canadian, since healthcare standards or policies may differ across countries.*

Another person who wanted to learn about the Chichijima incident and George H.W. Bush was annoyed that the sources were not specific enough:

> *Although I found the links provided for followup, I can't give it a higher rating because it led me to sites that were more about the War, not the incident [Chichijima Incident] in itself.*

Sources can be less important for users when the question is simple and has a clear, unique answer. One user noted that she was more interested in sources and links for broad, research-like questions, where she did not know the knowledge space well (for example, learning about clouds with her kids) but she was less likely to consult them for specific questions that had a clear answer (e.g., the address of a business or the author of a book).

Our finding does not mean that designers should remove sources from their AI interfaces — they’re necessary for users to verify answers and find more information. It only means that sources (like all other UI elements) need to be well tested and designed, so that they are **displayed in a way that is easily accessible** and people can find them when needed.

#### In-Answer Links

Aside from references, Bing Chat’s answers (as well as Bard’s) could also include links to other websites, in response to queries that asked for such links (for example, product or site recommendations).

*Aside from references, Bing Chat’s answers could include links (marked in purple) that named products or websites which were part of the answer. Any of these kinds of links could be included in the* Learn More *section.*

In 36.84% of the Bing Chat conversations, participants clicked on a provided link, compared to only 14.68% for Bard. This difference was statistically significant (p<0.0001).

Both **Bing Chat and Bard occasionally provided incorrect links** that were either no longer current or did not contain the information they claimed to contain. (For Bing, incorrect or broken links also caused some of the dissatisfaction with references that was discussed above.)

One participant was looking for things to do on a Friday night in Nashville. Bing Chat failed to provide any results first, only listing a few websites with no information about any of them. She rephrased the questions several times and asked for free events instead. The bot finally provided her with a few free event names and links to various sites. When she followed the links, she discovered that the events were, in fact, not free. At that point, she gave up chatting with the bot.

*One participant was looking for events in Nashville on a Friday night. The bot failed to provide any helpful information other than a few links at first (left). When the participant asked for free events, the bot listed a few with links without any brief introduction to them (right). Furthermore, the first link directed her to a Viator* Nashville Top Tours & Activities *page containing only paid events.*

Similarly, a Bard participant looking for perfume suggestions discovered that *all the stores that it said you could find the perfumes at did not exist or were closed.*

There were many such examples for both Bing Chat and Bard.**However, by the sheer fact that Bing participants tended to click on links more, they were more likely to encounter issues.

#### Suggested Followup Queries

Bing Chat also offered users suggestions for followup questions. Generally, users found these helpful because they bridged the [articulation barrier](https://www.nngroup.com/articles/ai-articulation-barrier/) and helped them speed up the process of satisfying their information need. These questions were especially useful when they helped the user understand the structure of the information space: **what they didn’t know they should know**. As one user put it:

> *[Bing Chat] provided follow up questions that […were] either […] word for word what I was going to ask next […] or, even better, […] a question that I hadn't thought of but really wanted to know.*

For example, one user who was expecting his first child asked what to do to support his wife during labor. Bing Chat helped him discover several things he was unaware of or he hadn’t thought of:

> *I asked what to do to support your wife during labor. I was picturing or thinking of the actual delivery, and this answer seemed to focus on when she goes into labor at home and what to do. I hadn't really thought about that, so that was very helpful. I liked the provided followup question ‘What to bring to the hospital?’ That was more along the lines of what I was originally thinking, and it provided a good list. It then gave two follow up questions that I liked. ‘What should I pack for the baby’ and ‘What is a birth plan?’ I chose what is a birth plan, because I had absolutely no idea. The next response provided two questions I was interested in. Pain-management options and postpartum options. I thought this thread was very informative and gave great options for continuing the conversation and discovery.*

A particularly helpful type of followup question is the one which requests an answer to be made shorter or longer. This supports the [accordion-editing behavior](https://www.nngroup.com/articles/accordion-editing-apple-picking/), especially for creation tasks, in which the bot must come up with a text or a list of items.

> *In one instance though, where […] it said like make it shorter, I was like, ‘oh that's actually a helpful button to have’ […]. And, also, kind of prompted [by ] my response ‘I have to make it shorter’ was ‘oh could you just make that kind of something in between’ and it was able to do that in that instance. So that was helpful.*

*A particularly helpful followup question involves shortening an already provided answer.*

Followup questions were generally well received, but unfortunately they had a few major issues. Respondents reported that they were sometimes:

- Too basic
- Too similar with the original question
- Not persistent

**Too basic.** Sometimes suggested followup questions picked up on terms in the users’ question but not on their real information need. For example, they would suggest asking for the definition of a word or for something that was only tangential to the topic of the conversation.

When a study participant used Bing Chat to help her refine the resume, she commented that she didn’t need a followup question for a definition of a medical term in her resume. This happened to other participants, as well:

> *But sometimes it would just be like, basically what is the definition of this word? And that, I don't know, I feel like is a waste of a followup question for me. […] You could Google that on your phone. I dunno, I didn't need the definition ones.*

> *I did use some of the [suggested followup] questions at the bottom, which were, a lot of times […] something silly […] like, could you tell me about the pyramids or something? And, I'm like, that's not relevant to this conversation but thank you.*

**Too similar with the original questions.** Such questions did not broaden the scope of the conversation and yielded almost identical answers. For example, the participant looking for events in Nashville tried one of Bing Chat’s followup questions (*What are some popular free events in Nashville*). This question was very similar to her previous prompt *Are there any free event happening in Nashville this weekend* and gave her links to the same sources.

**Not persistent**. The followup questions changed after each new response and the user was not able to return to them and select a suggested question from a previous list.

Sometimes the bot offered really good questions, but people could only select one. If they wanted to come back to another question that they had seen before, that was no longer available. The user would have to remember and type the whole followup question.

For example, one participant who was trying to figure out why his cat was coughing up hair balls recalled:

> *It did a good job providing follow up questions and I clicked on the first one provided. After the response to that question it provided to good follow up questions, "What kind of diet should I feed my cat?" and "How often should I groom my cat?". I clicked on the first one, and after I read the answer, I went back to click on the second and it was not there anymore. I asked the question myself anyway, but maybe those provided possible questions should stay in case someone wants to go back and get that answered as well.*

*One participant liked two suggested followup queries provided by Bing Chat, but the second question disappeared after he selected the first. He tried to scroll back to refind the second question. Unable to find it anywhere, he ended up typing the question on his own (this video is played at 1.5x speed).*

Multimedia Components

Unlike ChatGPT, whose answers were text-only, **89.56% of the Bing conversations and 46.01% of the Bard conversations included multimedia elements**, such as

- Videos
- Pictures
- Contextual information panels (e.g., news articles, map, products)

This difference was statistically significant at p <0.0001). The **multimedia elements were generally perceived positively**. For instance, the videos often supplemented the text answer and were particularly useful when the queries requested instructions about a particular process (e.g., how to serve at volleyball),

*When short videos were present to help visualize instructions about a specific process, people generally found them helpful.*

However, multimedia components presented in different formats can sometimes cause the following issues:

- Aggravate the fear of losing the context
- Prevent users from quickly getting to the main point (especially true for media content, such as long videos)
- Don’t translate well on mobile devices

##### Lose the Context

Losing the chat is a fear that many people have when chatting on any website — whether the chatbot is powered by generative AI or not. A participant summarized this feeling for us:

> *I don’t know if you feel the same way: it’s one of the most annoying things when you click on something and it opens a new page for you and it’s like, I don’t wanna lose where I am, but I also don’t want to be directed to like 30 other places when I’m trying to accomplish something.*

While rich external links invite users to perform more followup actions on Bing Chat (70% for Bing vs. 51% for Bard and 43% for ChatGPT, p <0.002 for both comparisons), they can **increase the fear of losing the chat**, especially when users don’t know which links would direct them to a different site or will open in an overlay.

One participant was reluctant to play the videos within the answers provided by Bing Chat at the very beginning, because she didn’t know how the video would be displayed and whether she would lose her conversation. She was relieved when she discovered that the video player was contained within the chat:

> *[The video interface] was almost too simple. I worried about navigating away from the chat would be like, okay, if I go back it's gonna have lost its place and where it was talking to me and especially with the video feature. So I, I did enjoy that it was like kind of self-contained [video player] within the chat.*

##### Fail to Support Scanning

Videos require users to process information [sequentially](https://www.nngroup.com/articles/direct-vs-sequential-access/), which prevents them from scanning the main content quickly as they would with text or imageries. Thus, while it’s nice that Bing Chat would provide a list of videos below the answers, it could be hard for users to decide which ones are the most helpful to their questions solely based on the names of the videos. (The **list of videos is another example of failed information aggregation** — instead of summarizing and pointing out to a single video, the user must go through each of them like they would on a search-engine results page.)

*Bing Chat sometimes displayed a video panel below its answer but failed to provide any information about these videos other than their names.**A Google search-results page includes video featured snippet, showing an excerpt of the video transcript to help users decide if that video is relevant.*

##### Don’t Translate Well on Mobile

Richer elements can challenge users more when presented on mobile because the screen space is limited. One participant described the mobile interface of Bing as **cluttered**, because there were too many things competing for her attention and too many buttons placed close to the input field (the *broom* button, the *voice input* button, the input field, and suggested followup queries). Sometimes, specific components would not load properly on mobile.

*A flight detail and price widget didn’t size proportionally to the mobile screen when a participant searched for the cheapest flight from Nashville to Flagstaff.*

Furthermore, the overall experience of using Bing Chat on mobile was more error-prone, as people could accidentally submit the query before they had finished typing. When this happened, the participant would have to resubmit the query.

*A Bing participant meant to copy and paste some text in the prompt box but accidentally submitted the query too soon and had to resubmit the query. In this case, Bing remembered the bigger conversation contexts, but in other situations it would assume a new conversation was started. (Note also that the broom button for a new conversation was very close to the input box and easy to touch by mistake.)*

Occasionally, the bot would assume that the participant had initiated a new conversation and it would lose context:

> *And there were quite a few instances […]**where I […]**accidentally sent something before I was […]**ready to have it sent and I wanted to provide more context.**A** nd,**then,** when I provided more context,**it was like, […]**'**oh you’re starting a new topic,’** and it doesn’t connect back to the previous message.*

### Ads

One other element that impaired the experience of Bing Chat participants was ads. Overall, 15.65% of its answers contained an ad. (None of the other chatbots included ads.)

Participants had a mixed attitude towards the ads. They were okay with them when they searched for a products or when the ads were highly relevant to their queries. They were annoyed when the ads were irrelevant, too prevalent, or too intrusive, even as they understood their purpose and acknowledged their legitimacy.

For instance, one participant used Bing Chat as a way to explore nursery lamp options he could buy for his wife. He was satisfied about the whole experience (including ads) because the chat helped him find and purchase a beautiful white floor lamp from Pottery Barn. Similarly, another participant researched the bullet-train ticket prices to get prepared for her upcoming Japan trips was okay with the promoted ticket-purchase links below the answer.

*Participants were fine with ads if they were highly relevant to their queries.*

While ads were okay when people were searching for specific information, they were generally perceived as **annoying in broader research-oriented activities**. This finding is consistent with our previous studies of [research-oriented information-seeking activities](https://www.nngroup.com/articles/information-seeking-expectations/).

One participant asked about life-insurance advice and received 2 ads from AARP (American Association of Retired Persons). He was annoyed by the ads, especially because he knew his age would not qualify him for AARP insurance. What’s worse, the bot failed to provide a helpful answer. He commented,

> *It didn't really provide any in depth help [with life insurance advice], and instead of providing alternative places to read, gave me ads for insurance companies.*

Another participant asked about the website Clutch (a site for finding agencies that specialize in a variety of website-related services), but the promoted ads were about clutch kits, which she didn’t like at all.

*An irrelevant ad panel about clutch kits was placed below the answer to the participant’s question about the website Clutch, a service for finding web-related agencies.*

During our study, the mostly misplaced and overwhelming number of ads displayed by Bing Chat generally left a negative impression over the participants. They commented,

> *Well, I, I mean, so I asked a question about […] vegan food or about coding; [it] doesn't mean I necessarily now want to be pummeled with opportunities to buy vegan food or coding courses, but that that is in fact the outcome of the Bing interface.*

> *I mean, it, it's, it disappointing […]  it's clear that they're presenting me with things that are in fact relevant to me and it's a prequalifier for their revenue model to send me to places where they've got people paying for ads […] It's quite […] a marketing operation; as a utility, as a resource [it is] kind of distasteful.*

## User Experience: Essential for the Design of Successful AI

Overall, Bing Chat had the poorest helpfulness and trustworthiness ratings compared with ChatGPT and Bard. There were two big reasons why: its poorer information aggregation and its faultier interface.

The poor information aggregation is something that AI researchers can and should fix. But the faultier interface regards us — UX professionals.

Bing had the most complex interface, with the most features, yet it got dinged for it. Does that mean that we are better off if the AI design includes no or very few UI elements (like that of ChatGPT)?

The answer is a resounding no. References, in-answer links, suggested followup questions, and multimedia components (like videos, images and other types of information panels) are all good, necessary features. They help users make sense of the answer received from the bot. They also help them act upon the information. As AI is becoming pervasive and people will use it to engage in more complex and varied tasks, these features will become indispensable.

What our finding means is that **these additional UI elements need to be well designed and tested with many different users and tasks.** so that they do not get in the way. The idea is good, but the execution needs to improve.

## Best Practices and Design Recommendations for Generative-AI Chatbots

Designers of generative AI bots can learn from Bing Chat’s experience and follow these best practices:

- While **references** for an answer are helpful, they should be relevant and should not distract the user too much from the gist of the answer. It should be easy to ignore them, yet also easily find them when needed.
- **In-answer links** need to be accurate, current, and match the answer provided by the bot. Otherwise, they may diminish credibility.
- **Suggested followup questions** bridge the articulation barrier: they help users formulate queries and explore the information space, but only if they are nontrivial and related to the current topic. Followup questions should not go away with a new answer.
- Users should be able to easily **recover the context of the conversation**, even if they visit new sites, watch videos, or submit a prompt too soon.
- Set users’ expectations about features and design components such as modes and video-playing formats.
- It's okay to include **contextually relevant ads in focused product-recommendation queries**, but do not use them in broad, research-based conversations.
