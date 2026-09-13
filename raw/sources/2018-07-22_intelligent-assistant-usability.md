---
title: "Intelligent Assistants Have Poor Usability: A User Study of Alexa, Google Assistant, and Siri"
date: "2018-07-22"
url: "https://www.nngroup.com/articles/intelligent-assistant-usability/"
author: "Page Laubheimer, Raluca Budiu"
topics: [ai, web-usability]
type: article
---

The holy grail of usability is to build an interface that requires zero [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/): being able to fulfill users’ needs without having them do anything. While interface design is still far from reading people’s minds, intelligent assistants such as Alexa, Google Assistant, and Siri are one step in that direction.

## In This Article:

- [UI Characteristics](#toc-ui-characteristics-1)
- [User Research](#toc-user-research-2)
- [Results: Delivered Usability Grossly Inferior to Promised Usability](#toc-results-delivered-usability-grossly-inferior-to-promised-usability-3)
- [Why Do People Use Assistants](#toc-why-do-people-use-assistants-4)
- [Speaking with Assistants](#toc-speaking-with-assistants-5)
- [Presenting Answers](#toc-presenting-answers-6)
- [Skills and Actions](#toc-skills-and-actions-7)
- [Integration with Other Apps](#toc-integration-with-other-apps-8)
- [Conclusion](#toc-conclusion-9)

## UI Characteristics

The intelligent computer-based assistants combine 5 fundamental user-interface technologies:

1. **Voice input**: commands are spoken instead of issued through typing or clicking/tapping graphical items.
2. **Natural-language** understanding: users are not restricted to using a specific, computer-optimized vocabulary or syntax, but can structure their input in many ways, just as they would do in human conversation.
3. **Voice output**: instead of displaying information on a screen, the assistant reads it out loud.
4. **Intelligent interpretation**: the assistant utilizes additional information (such as context or past behaviors), besides the user’s literal input, to estimate what the user wants.
5. **Agency**: the assistant does actions that the user hasn’t requested, but which the computer undertakes on its own.

Both intelligent interpretation and agency require that assistants **actively learn** about the user and be able to modify their behavior in the service of the user.

Thus, when evaluating the user experience of intelligent assistants, we need to consider 6 issues: each of the 5 technologies, plus their **integration**.

The idea of integrating a bundle of UI technologies isn’t new. The same principle is behind the most popular style of graphical user interfaces (GUIs), called WIMP for “windows–icons–menus–pointing device”. You can have windows without a mouse (use *Alt*-*Tab*) or a mouse without icons (click on words), but the full set generates a nicely integrated GUI that has offered good usability for more than 30 years.

Not all assistants use all 5 UI technologies at all times: for example, if a screen is available, assistants may use visual output instead of voice output. However, the 5 technologies support and augment each other when they are smoothly integrated. For instance, voice commands, like the traditional command-based interaction style, have an inherent usability weakness compared to clicking (they rely on some amount of recall, whereas clicking and [direct manipulation](https://www.nngroup.com/articles/direct-manipulation/) involve [recognition](https://www.nngroup.com/articles/recognition-and-recall/)), but natural language may potentially make composing a command less arduous than clicking an icon.

Integrating the 5 UI techniques promises an interaction style with two advantages:

- It can short-circuit the physical interface and simply allow users to formulate their goal in natural language. Although speaking does involve an interaction cost, in theory this cost is smaller than learning a new UI, pressing buttons, and making selections.
- It can infer users’ goals and be proactive about them by offering appropriate suggestions based on contextual information or prior user behavior. This second aspect is in fact closer to “reading our minds.”

Contextual suggestions are still fairly limited with today’s assistants, although small steps are taken in that direction — Google Assistant parses email and adds flights or restaurant reservations to calendars; and both Siri and Google Assistant warn users of the time it takes to get to a frequent destination once they leave a location. When these contextual suggestions are appropriate, they seamlessly progress users towards their goals.

## User Research

To better understand what challenges these assistants pose today and where they help users, we ran two usability studies (one in New York City and one in the San Francisco Bay Area). A total of 17 participants — 5 in New York, 12 in California — who were frequent users of at least one of the major intelligent assistants (Alexa, Google Assistant, and Siri) were invited into the lab for individual sessions. Each session consisted of a combination of usability testing (in which participants completed facilitator-assigned tasks using Alexa, Google Assistant, or Siri) and an interview.

During the usability-testing portion of the study, we asked participants to use the assistants to complete a variety of tasks, ranging from simple (e.g., weather for the 4th of July weekend, pharmacy hours for a nearby Walgreens, when George Clooney was born) to more complicated (e.g., the year when Stanley Kubrick’s second to last movie was made, traffic to Moss Beach during the weekend).

This article summarizes our main findings. A [second article will discuss the social dimension](https://www.nngroup.com/articles/voice-assistant-attitudes/) of the interaction with intelligent assistants.

## Results: Delivered Usability Grossly Inferior to Promised Usability

Our user research found that current intelligent assistants fail on all 6 questions (5 technologies plus integration), resulting in an overall usability level that’s close to useless for even slightly complex interactions. For simple interactions, the devices do meet the bare minimum usability requirements. Even though it goes against the basic premise of human-centered design, users have to train themselves to understand when an intelligent assistant will be useful and when it’s better to avoid using it.

Our ideology has always been that computers should adapt to humans, not the other way around. The promise of AI is exactly one of high adaptability, but we didn’t see that that when observing actual use. In contrast, observing users struggle with the AI interfaces felt like a **return to the dark ages of the 1970s**: the need to memorize cryptic commands, oppressive modes, confusing content, inflexible interactions — basically an unpleasant user experience.

Let’s look at each of the 6 UI techniques and assess how well they met their promise to our users. While the answers to this question are sad, we can also ask whether the current weaknesses are inherent to the techniques and will remain, or whether they are caused by current technology limitations and will improve.

UI technique | Current usability | Future potential | Voice input | Good (except for nonnative speakers) | Soon to be great and also cope with accents | Most of the input is correctly transcribed, with the occasional exception of names. | Natural language | Bad | Can become much better, but hard to do | Multiclause sentences are not understood; equivalent query formulations produce different results. There is limited understanding of pronoun referents. | Voice output | Bad | Inherently limited usability, except for simple information | Except for a few tasks (e.g., navigation, weather), the assistants are not able to consistently produce a satisfactory vocal response to queries. | Intelligent interpretation | Bad | Can become much better, but extremely difficult to do | The assistants use simple contextual information such as current location, contact data, or past frequent locations, but rarely go beyond that. | Agency | Bad | Can become much better | There is only a very a limited use of external sources of information (such as calendar or email) to infer potential actions of interest to the user. | Integration | Terrible | Can become much better, but requires much grunt work | The assistants don’t work well with other available apps on the device and the interactions with various “skills” or “actions” don’t take advantage of all the UI technologies.

Are we being unreasonable? Isn’t it true that AI-based user interfaces have made huge progress in recent years? Yes, current AI products are better than many of the AI research systems of past decades. But the requirements for everyday use by average people are dramatically higher than the requirements for a graduate student demo. The demos we saw at academic conferences 20 years ago were impressive and held great promise for AI-based interactions. The current products are better, and yet don’t fulfill the promise.

The promise does remain, and people already get some use out of their intelligent assistants. But vast advances are required for this interaction style to support wider use with a high level of usability. An analogy is to the way mobile devices developed: when we [tested mobile usability in 2000](https://www.nngroup.com/articles/wap-mobile-phones-field-study-findings/), the results were abysmal. Yet, the promise of mobile information services was clear and many people already made heavy use of a particularly useful low-end service: person-to-person text messages. It took many more years of technology advances and tighter UI integration for the first decent smartphone to ship, leading to an acceptable, though still [low level of mobile usability by 2009](https://www.nngroup.com/articles/mobile-usability-first-findings/). Another decade of improvements, and [mobile user interfaces are now pretty good](https://www.nngroup.com/articles/state-mobile-ux/).

AI-based user interfaces may be slightly better than mobile usability was in 2000, but not by much. Will it take two decades to reach good AI usability? Some of the problems that need solving are so tough that this may even be an optimistic assessment. But just as with mobile, the benefits of AI-based UIs are big enough that even the halfway point (i.e., decent, but not good, usability) may be acceptable and could be within reach much sooner.

## Why Do People Use Assistants

Most of our users reported that they use intelligent assistants in two types of situations:

1. When their hands were busy — for example, during driving or cooking
2. When asking the question was faster than typing it and reading through the results

The second situation deserves a discussion. Most people had clear expectations about what the assistants could do, and often said that they would not use an assistant for complex information needs. They felt that a query with one clear answer had a good chance of being answered correctly by the assistant, and two participants explicitly mentioned 5W1H [(Who, What, Where, When, Why, How)]()questions. In contrast, more nuanced, research-like information needs were better addressed by a web search or some other interaction with screen-based device such as a phone or tablet.

However, some people felt that the assistants were capable of accomplishing even complicated tasks, provided that they were asked the right question. One user said “I can do everything I can do on my phone with Siri. […] Complex questions — I have to simplify to make them work.”

Most people however considered that thinking about the right question was not worth the effort. As one user put it, “Alexa is like an alien — I have to explain everything to it… It’s good only for simple queries. I have to tell her everything. I like to simply ask questions, not think [about how to formulate questions].”

One notable area where voice assistants saved interaction cost was dictation: long messages or search queries were easier to say than type, especially on mobile devices, where the [tiny keyboard is error-prone](https://www.nngroup.com/articles/mobile-ux/), slow, and frustrating. Participants were usually quick to note that dictation was imperfect and helpful when they could not type easily (for example, because they were walking, driving, cooking, or simply away from a device with a real keyboard), and that they avoided dictation if the text used unique terminology that could be mistranscribed. They also mentioned struggles with having the assistant insert the correct punctuation (either the assistant would stop listening if the user paused to denote a sentence end or the assistant simply would ignore punctuation altogether, requiring users to proofread and edit the text).

## Speaking with Assistants

When participants took the time to think about how to formulate the query and then delivered it to the assistant in a continuous flow, the assistant was usually able to parse the whole query. As a user put it, “You should think of your question before you ask it — because it’s hard to fix it while you’re saying it to [an assistant]. You’ve just got to think of it beforehand, because it’s not like a person where in a conversation with them [you can be vague].” Another said, “I almost feel like a robot when I’m asking questions, because I have to say it in such a clear and concise way, and I have to think of it so clearly. When I try to give a command or ask a specific question, you don’t use much inflection. It’s really just picking up words, it’s not picking up emotions in your voice.”

But many participants started speaking before formulating the query completely (as you would normally do with a human), and occasionally paused searching for the best word. Such pauses are natural in conversation, but assistants did not interpret them correctly and often rushed to respond. Of course, answers to such incomplete queries were incorrect most of the time, and the overall effect was unpleasant: participants complained that they were interrupted, that the assistant “talked over them”, or that the assistant was “rude.” Some even went as far as to explicitly scold the assistant for it (“Alexa, that’s rude!”).

When people needed to restate a query that wasn’t understood correctly, they often enunciated words in a highly exaggerated way (as if they were talking to a human with a hearing impairment).

The majority of the participants felt that complex, multiclause sentences (such as “What time should I leave for Moss Beach on Saturday if I want to avoid traffic?” or “Find the flight status of a flight from London to Vancouver that leaves at 4:55pm today”) were unlikely to be understood by the assistants. Some tried to decompose such sentences in multiple queries. For example, one participant who wanted to find out when Kubrick’s second-to-last movie was made asked for a list of movies by Kubrick, and then planned to ask questions about the second-to-last item in that list. Unfortunately, Siri was not helpful at all, because it simply provided a subset of Kubrick’s movies, with no apparent order.

### Nonnative English Speakers

Several people had foreign accents and felt that the assistant did not always get their utterances and had to repeat themselves often. These people were frustrated and considered that the assistants had to learn to deal with various languages and ways of speaking.

Besides the accent, there were three other factors that affected their success with assistants:

1. They were likely to pause even more in their utterances than native speakers. These pauses were often interpreted by the assistant as the end of the query.
2. They tended to correct themselves when they felt that they had mispronounced a word and ended up saying the same word twice. These repeated words seemed to confuse assistants — especially Alexa.
3. They sometimes used less common wordings. For example, one participant asked “Alexa, when did Great Britain’s soccer team play in the soccer championship.” Alexa was not able to find an answer for that question.

Luckily, accent comprehension is an area where computers have the potential to be [better than reality](https://www.nngroup.com/articles/better-than-reality-a-fundamental-internet-principle/): they can recognize non-standard pronunciations of words much better than a human can do. A computer doesn’t care how you pronounce a certain word — unless it’s trained to only recognize a specific sound, it can be made to understand that several different sounds all represent the same word. Thus, we expect that better accent recognition is only a matter of time. Coping with the other issues discussed in this section will be harder.

## Presenting Answers

### Assistant’s Language

Some of the participants complained that the assistant spoke too fast and that there was no way to make it repeat the answer. Especially when the answer was too long or complex, participants could not commit all the information to their [working memory](https://www.nngroup.com/articles/working-memory-external-memory/). For example, before offering a mortgage quote, the Alexa Lending Tree skill asked the user to confirm that all the details entered were correct by reciting the address and the mortgage terms, and then enumerating a set of commands for editing the information if needed. One user said: “It’s talking too fast at the very end — [it says] `if something is not correct [you have to] go to bla bla bla’; it’s just too hard to remember all the options.”

When the assistants misunderstood the question and offered an incorrect response, the experience was off-putting and annoying. People resented having to wait for a long answer that was completely irrelevant and struggled to insert an “Alexa, stop” in the conversation. One participant explained, “What I don’t like is that [Alexa] doesn’t shut up when I start talking to her. This is what a more human interaction should be. […] It would be ideal if it interacted to something less than `Alexa, stop’ — something like `ok’, or `enough’, or pretty much anything that I mutter […] It’s like talking to someone who just goes on and on, and you’re waiting to find a pause so you can somehow stop them.”

But even some of the correct assistant responses were too wordy. One user complained that, when she tried to add items to the grocery list, Alexa confirmed “<item> added to grocery list” after each one. It felt as too many words for such a repetitive task. Another user called Google Assistant “too chatty” when it provided extra information to a query about pharmacy opening hours. A participant rolled her eyes when Alexa read a long description for each recipe in a list of tiramisu recipes, including a mention of (some) fairly obvious and repetitive ingredients — like eggs.

### Voice vs. Screen Results

One of the major uses of intelligent assistants is hands-free usage in the car, in the kitchen, or in other similar situations. **Our users considered a vocal answer superior to on-screen answers in the vast majority of the cases.**(Exceptions included situations where the answer contained sensitive information — for instance, one woman resented having her doctor appointment read out loud, saying “I would rather have it say the word ‘event’”.)

Most smart speakers don’t have a screen, so they must convey answers in vocal format. This restriction made some participants prefer the speakers over their phone-based counterparts, where a mixed-modal interaction felt more tedious.

Phone-based assistants usually deferred to search results when they didn’t have a ready answer, forcing users to interact with the screen. People were disappointed when they had to use their eyes and fingers to browse through a list of results. They commented that “it didn’t give me the right answer. It gave me an article and links. It doesn’t tell me what I asked,” and “I kind of wish that it didn’t show me just some links… [At least it] should tell me something… And then, maybe `if you want more, check this or that.’”

When the right answer was read, “it felt like magic.” A participant asked Google Assistant “How many days should I spend in Prague?”, and the response came loud and clear: “According to Quora, you should ideally spend 3-4 days in Prague […].” The user said, “That’s what I was looking for in the others; it read the information out loud to me and it also showed the information.” These types of experiences were considered the most helpful by our participants, but they were rare in our study: even though this task was performed by several participants, only one used the “right” query formulation that produced a clear verbal answer; the other six who tried variants of the same question (“OK Google, what do you think would be a good amount of time to vacation in Prague”, “OK Google, how long should I vacation in Prague”, “Hey Siri, how many days is enough for visiting Prague,” “OK Google, what’s a good amount of time to stay in Prague,” “Siri, how many days should I go to Prague for?”, “Siri, if I go to Prague, how long should I go?”) got a set of links instead from both Siri and Google Assistant, except for the last query, which was offered the traffic around Prague.

With Siri, there was another reason for which links were disruptive: those who clicked on a link in the result list were taken to the browser or to a different app, and some did not know how to get back to the list to continue inspecting other results. One iPhone user clicked on a restaurant to see it on a map, and then tried to return to the other restaurants; she said, “Oh no, [the restaurants] disappeared… That’s one thing that bothers me, that I don’t know how to retrieve the Siri request, you know, once it says there’s something you might find interesting … like if I’m driving, if I really want to find who starred in this movie, I could say `add it to my to-do list to do later’ or I could say `look it up’, but I am not going to look at it until I get to my destination, and, by the time I’m there, it’s disappeared… So this list of restaurants is gone because I touched on Maps, so I’ll have to try it again.” (The list of restaurants could have been retrieved should the user have clicked on the [back-to-app iPhone button](https://www.nngroup.com/articles/ios-9-back-to-app-button/) in the top left corner of the screen, but that button was tiny and many users are not familiar with it. However, the more general point of being unable to retrieve the history of interactions is definitely a weakness of Siri compared with other intelligent assistants. Even Alexa allows users to see a history of their queries in the Alexa mobile app.)

Screen-based assistants that transcribed the user’s query caused issues when the transcription was not instantaneous. One participant thought that, because she did not see any of her spoken words on the screen, Siri hadn’t heard her, so she would repeat those first few words more than once. The resulting utterance was usually not properly understood by the assistant.

### Partial Answers

Sometimes Alexa openly recognized that it did not have an answer. When it did offer information that was still relevant, although not a direct response to the user’s query, participants were pleased. For example, one user asked about rent in Willow Glenn (a neighborhood in San Jose, California) and Alexa said that it did not know the answer, but offered instead the average rent in the San Francisco Bay Area. The user was pleased that the assistant had recognized Willow Glenn as part of the Bay Area and was okay with the answer. Another user asked “Alexa, how much is a one-bedroom apartment in Mountain View?” and, when the assistant answered “Sorry, I don’t know that one. For now I am able to look up phone numbers, hours, and addresses.”, the user commented “Thank you. That’s really helpful — like ‘Ok, I cannot do that, but I can do this’...”

When, instead of a vocal answer, Siri or Google Assistant provided a set of on-screen results, the first reaction was disappointment, as mentioned above. However, if the results on the screen were relevant to their query, people sometimes felt that the experience was acceptable or even good. (This perception may be specific to the laboratory setting, where participants’ hands were free and they could interact with their device.) Many felt that they knew how to search and pick out relevant results from the SERP better than an assistant (and especially better than Siri), so when the assistant returned just the search results, some said that they would have to redo the searches anyhow. A few people tried to formulate search queries out loud when talking to the assistant and bet on the idea that the first few results would be good enough. These people used the assistant (Google Assistant usually) as a vocal interface to a search engine.

### Trust in Results

People knew that intelligent assistants are imperfect. So, even when the assistant provided an answer, they sometimes doubted that the answer is right – not knowing if the query was correctly understood in its entirety, or the assistant only matched part of it. As one user put it, “I don't trust that Siri will give me an answer that is good for me.”

For example, when asked for a recipe, Alexa provided a “top recipe” with the option for more. But it gave no information about what “top” meant and how the recipes were selected and ordered. Were these highly rated recipes? Recipes published by a reputed blog or cooking website? People had to trust the selections and ordering that Alexa made for them, without any supporting evidence in the form of ratings or number of reviews. Especially with Alexa, where users could not see the results and just listened to a list, the issue of how the list was assembled was important to several users.

However, even phone-based assistants elicited trust issues, even though they could use the screen for supporting evidence. For example, in one of the tasks, users asked Siri to find restaurants along the way to Moss Beach. Siri did return a list of restaurants with corresponding Yelp ratings (seemingly having answered the query), but there was no map to show that the restaurants did indeed satisfy the criterion specified by the user. Accessing the map with all the restaurants was also tedious: one had to pick a restaurant and click on its map; that map showed all the restaurants selected by Siri.

*Siri did not show the list of restaurants on a map. To access the map, users had to select a restaurant and show it on a map. Once they did so, some users did not know how to recover the list of restaurants (which could be done by clicking the back-to-app button* Siri *in the top left corner of the screen).*

In contrast, Google Assistant did a much better job of addressing the same query: it did show all the restaurants suggested on a map, and users could see that (unfortunately) the results were concentrated at the Moss Beach end of the route instead of in between.

*Google Assistant showed the restaurants on the map.*

### Poor Support for Comparison and Shopping

In our study, tasks involving comparisons had especially poor usability, for several reasons:

1. Speech is an [inefficient output modality](https://www.nngroup.com/articles/voice-first/). It takes a [long time to listen](https://www.nngroup.com/articles/direct-vs-sequential-access/) to an assistant read out each possible alternative, and we watched users get visibly annoyed while listening to an assistant talk at length about an option. The assistant’s wordiness was especially frustrating when the participant quickly realized that she didn’t care about the current item, but she still had to listen to Alexa or Siri droning on about it. If two people are talking with each other, they can use tone, facial, or body-language cues to steer the conversation into a direction interesting to both. But voice assistants cannot understand when the user isn’t interested in an option and stop talking about it.
2. There was no way for users to easily go back and forth and compare options. They had to commit all the information about one alternative to their working memory in order to compare that item with subsequent ones.

For example, when offering different tiramisu recipes to a user, Alexa listed the name of the recipe, the time it takes to prepare it, and then said, “You can ask for more information, or, for more recipes, say ‘Next’.” If the user said, “Next”, it was difficult to go back and refer to a previous recipe. This interaction style assumed that the user was comfortable [satisficing](https://www.nngroup.com/articles/satisficing/) (i.e., choosing the first minimally acceptable option) rather than comparing pros and cons of different alternatives. For some simple tasks, with no consequences for picking a mediocre choice, satisficing may be a reasonable assumption, but in our study, even for picking a recipe for dinner, users wanted to do a fair degree of comparison.

Using multiple criteria for selection makes the task even harder. For example, when using Google Assistant to compare pizza places in New York City, users couldn’t efficiently compare how far away each one was, and then decide among the nearby options based on the number of stars they had in reviews — all of that information was presented for each restaurant individually, and users had to keep all those details in their working memory to compare different restaurants.

Lack of accompanying visual details for each choice mattered — especially for things such as online shopping, restaurants, or hotels. Users in our study routinely dismissed the idea of buying an item without being able to view images of it to assess it, and also to doublecheck that it was the correct item. There was too much room for error with ambiguous or similarly named products.

One participant even noted that asking Alexa for the current price of bitcoin was frustrating, as it couldn’t easily communicate change over time, a key factor for people trading rapidly fluctuating cryptocurrency.

## Skills and Actions

For systems like Alexa and Google Assistant, users can access special “apps” (called “skills” in Amazon’s ecosystem and “actions” in Google’s) devoted to specific tasks.

In theory skills and actions can enlarge the power of these systems, but in our study they proved pretty much useless. The majority of the Alexa users did not know what skills were; some had encountered them before, installed one or two, and then completely forgotten about their existence.

Alexa skills have two big discoverability problems:

- They require users to remember precisely the name of the skill. Although you can ask Alexa what skills are currently installed on your device, the enterprise is quite futile, because Alexa starts describing them one by one in no apparent order, and by the time you got to the third skill, you feel you’ve had enough.
- They require users to remember the magic words that invoke the skill. In theory, these are “play <skill>”, “talk to <skill>”, “ask <skill> <specific question>”, but, in practice, our participants had trouble making some of these phrases work: one word seemed okay with one skill, but not with the other. (We asked people to navigate to the skill page in the Alexa app and sometimes they tried the phrases listed there as examples, and even those did not seem to work.)

One person recounted how the main reason for which he bought an Echo device was to control his home entertainment system with a Harmony remote, but then struggled to remember the exact words that he had to use to invoke the Harmony skill and eventually gave up using it.

People were even less familiar with Google Assistant’s actions than with Alexa’s skills. One user asked for directions to Moss Beach, and then, after receiving them, continued with the query “how about this weekend” (meaning to get directions if he were to leave during the weekend). Google Assistant answered “Sure, for that you can talk to Solar Flair. Does that sound good?” The user said yes, and accidentally found himself in the Solar Flair action, which, after asking for a location, offered “Up to 10 in Moss Beach.” This sentence left the user completely confused. (It turns out that Solar Flair returns the UV Index for a location.) The user commented: “At this point, I feel uncomfortable about having a new app and not knowing exactly what it was.”

Your browser does not support the video tag.

*One user accidentally found himself in the Solar Flair action for Google Assistant, as he was trying to get directions for Moss Beach during the weekend. (In most browsers, hover over the video to display the video-player controls if they're not already visible.)*

While it seemed that an action (or skill) suggestion may be appropriate occasionally, that suggestion should be accompanied by some basic information about the app.

### Interacting with Skills

Even when people were finally able to access one of Alexa’s skills, interacting with them was not straightforward. Unlike Alexa itself, which accepted relatively free-form language, skills required a restricted set of responses. In many ways, they seemed very similar to traditional interactive voice-response systems that require users to make selections by saying a specific word or number. People did not understand the difference between the “restricted-language” mode and the “normal-language” mode, and many of the interactions with skills failed because they did not discover the right way to talk with the app. Most of the time, they simply ignored the instructions and formulated their answers and queries in free form. This behavior created difficulties and triggered repetitive responses from the skills.

For example, the Restaurant Explorer skill forced users to refer to the restaurants it suggested by saying “1”, “2” or “3” instead of allowing them to use the restaurant’s name. The Lonely Planet skill required users to say specific keywords such as “best time to go” and did not understand questions such as “What are the events in Sydney in July 2018?.” When users asked this or other nonscripted questions, the skill repeated a set of general facts about Sydney. One participant commented “It’s too much. It’s as if I am listening to an encyclopedia – it’s not interactive. [..] It just tells me the facts and it doesn’t care if I don’t want to listen.”

The Air Canada skill also provided users with limited functionality and wanted specific wording; when people asked “What is the status of a flight from San Francisco to Vancouver that leaves at four fifty five pm”, the skill pretty much ignored all the words except “four fifty five”, which it interpreted as the flight number.

Skills were also annoying because of the “introductory” portion, which played the combined role of a “splash” screen and tutorial. In such (lengthy) introductions, the skills welcomed the user and enumerated the list of word commands that were available to them. Unfortunately, these introductions were repeated often, and, like with all tutorials, people pretty much ignored them, eager to start their task with the skill.

The skills worked better when they asked users specific questions and allowed them to provide answers. But even there, there was a problem of setting the expectations: one user interacting with Lending Tree skill complained that the skill started asking questions without telling her (1) why it needed the answers, and (2) without giving it assurance that it will have the answer. A better response to her query about mortgage rates in zip code 94087 would have been a range of values, followed by the option to continue and answer some questions in order to get a precise rate.

Yet another issue caused by skills and actions was user disorientation: participants were not sure whether they were still interacting with a skill or they could resume normal interaction with Alexa. One participant tried to solve this issue by asking Alexa explicitly: “Alexa, are we still in [the skill] Woot?”, to figure out what she needed to do next. (This question is a sign of the UI having utterly failed the first usability heuristic — [visibility of system status](https://www.nngroup.com/articles/visibility-system-status/).)

## Integration with Other Apps

A common complaint with the assistants was that they did not integrate well in the virtual ecosystems in which users lived. iPhone users complained about lack of integration between Siri and a variety of apps they wanted to use — Spotify to play Music, Google Maps for directions, and so on. Many felt that Siri was optimized for Apple apps and devices, but did not speak with the apps and services they had.

Alexa users also complained about Amazon’s services taking precedence — many already had subscriptions to Spotify or to Apple Music and felt that it was wasteful to subscribe to Amazon Music as well in order to get to listen to the music they wanted on their Echo device. Aggressive promoting of the company’s own services forced users to learn to formulate queries so that they get around these restrictions: “When I say play music, it tells me that I don’t have Amazon Music so I have to be very clear and say `Play iHeart Radio.’”

## Conclusion

Today’s `intelligent’ assistants are still far from passing a Turing test — for most interactions, people will easily figure out that they are not speaking with a human. Although users project human-like qualities onto them, they have relatively low expectations for these assistants and reserve them for black-and-white, factual questions. Even though the main hurdle is probably better natural language and dialogue processing (an inherently hard problem), many smaller scale issues could be fixed with more thoughtful design.
