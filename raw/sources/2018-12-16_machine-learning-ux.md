---
title: "Can Users Understand Recommendations and Personalization Driven by Machine Learning?"
date: "2018-12-16"
url: "https://www.nngroup.com/articles/machine-learning-ux/"
author: "Raluca Budiu"
topics: [ai, human-computer-interaction]
type: article
---

In this article, we examine some of the challenges that users encounter when interacting with machine-learning algorithms on Facebook, Instagram, Google News, Netflix, and Uber Driver. Our discussion is based on a week-long [diary study](https://www.nngroup.com/articles/diary-studies/) in which 14 existing users of these systems video-logged their interactions with them.

## In This Article:

- [Machine Learning for Recommendations and Personalization](#toc-machine-learning-for-recommendations-and-personalization-1)
- [The Black-Box Model](#toc-the-black-box-model-2)
- [Unclear Inputs](#toc-unclear-inputs-3)
- [Lack of Control of the Output](#toc-lack-of-control-of-the-output-4)
- [Recommendations](#toc-recommendations-5)

## Machine Learning for Recommendations and Personalization

We live in a world flooded by information. It’s harder and harder for us to keep track of it or to manually curate it for others; luckily, modern data science can sort through the vast amounts of information and surface those items that are relevant to us.

**Machine-learning algorithms** rely on user knowledge and patterns observed in the data to make inferences and suggestions about what we may like or be interested in. With machine-learning technologies becoming more and more accessible to developers, there’s a push for companies to take advantage of these algorithms to improve their products and their users’ experience.

Typical uses of such artificial-intelligence (AI) technologies for UX purposes include:

- Recommendations (e.g., a list of movies to watch or products to purchase)
- Choice of what advertisements or content (e.g., news headlines) to display
- Deals and special offers, [personalized](https://www.nngroup.com/articles/recommendation-expectations/) to appeal to the current user
- Personalized shortcuts with one-click access to whatever a user will likely want to do next

Unfortunately, these algorithms are usually not transparent to the end users. People are not sure which of their actions are taken into account by these algorithms, and their outputs are not always easy to make sense of. Suggestions and recommendations may be right on spot or apparently random and nonsensical. Often, these algorithms sort their output according to invisible criteria or group it into ad-hoc categories that are not mutually exclusive. While these decisions make sense from an algorithmic viewpoint, they are often too obscure for the lay user and go against traditional ways of structuring content.

## The Black-Box Model

To interact successfully with any system, users must create a [mental model](https://www.nngroup.com/articles/mental-models/) of the system. Most people are not computer scientists and have no idea of how software is implemented, but they can form decent mental models based on prior knowledge about software artifacts, interfaces, or even the world at large. In many situations, they treat the system as a black box and determine how they can change the output of the system by playing with the possible inputs.

Machine-learning algorithms are one such type of black-box systems for users. They know that the algorithm uses as input some of their actions and can see what the output is. To successfully interact with the algorithm, users must form a mental model of how it works and figure out how the output can be changed to match their need. There are two big hurdles in creating this model:

1. **Unclear inputs**: It’s not clear which of the users’ actions are taken into account to produce the output.
2. **Lack of control on the output**: Even when people know which of their actions are considered as inputs by the algorithm, it is not clear whether those inputs were effective in producing a desired output.

![The black box is the machine-learning algorithm with several potential inputs and an output.; inputs include tap, like,watch, save. User wonders "Which of my actions counts" and "How do I change the output"?](https://media.nngroup.com/media/editor/2018/11/13/visual5.png)

*The black-box model*

We discuss each of these reasons separately.

## Unclear Inputs

The lack of clarity in the input makes the problem of creating an accurate mental model of the black box quite difficult. There are several reasons for which the input status can be unclear:

- **The algorithm is not transparent** — it does not explicitly tell people which of their actions matter.
- **The user is not aware of the universe of possible inputs**, for example, because they are not limited to actions inside a system or a platform, but come from other behavior data (e.g., visiting third-party sites).
- **There is a delay between input and output**: a certain action may not immediately influence the output that the user sees within the same session.

Among the machine-learning systems we looked at, Netflix did the best job in helping users understand which of their actions were taken into account by the recommender system. Netflix’s homepage (as well as the main-category landing pages) are usually one long set of lists; many of these lists have labels that explain how they were created — *Because you watched The Curious Creations of Christine McConnell, Because you added 22 July to your list,* and so on.

![Two Netflix lists: "Because you watched The Curious Creations of Christine McConnell" and "Because you added 22 July to your list"](https://media.nngroup.com/media/editor/2018/11/13/netflix-because.png)

*Netflix explains some of the inputs used by its recommender system.*

People were very appreciative of these types of suggestions, not only because they could feel in control but also because they gave them valuable information about the content being displayed.

Yet, even Netflix wasn’t totally successful in creating a good understanding of how the user’s actions are taken into account to create recommendations — also because these actions were not immediately reflected in the output of the algorithm. For example, one participant was puzzled that her *Top**picks* seemed unaffected by the stand-up comedy shows that she had watched the last time she used Netflix. She said:

> “Top picks *changed — I guess based on what I watched, but this has nothing to do with what I watched, there's not a lot of comedy.”*

Another person wondered why *Top picks* overlapped so much with her Netflix watchlist:

> “Top picks — I don't know how they get them, I'm sure there's some algorithm or something, but I wish it was a little bit better because a lot of it is stuff that I watched years ago, or stuff that I have had on my list or stuff that I am just absolutely not interested in, so I'm like, hmm I wonder why they're recommending these things.”

A Facebook user took the time to hide an ad on her newsfeed only to see the same ad repeated down the page.

Facebook and Instagram users had a harder time understanding which of their actions really mattered for the content that was displayed on their newsfeed. They assumed that the posts in their newsfeed that they engaged with (through the *Like* button and its relatives) are taken into account by the algorithm in order to decide what content is displayed to them. But some of the theories regarding possible inputs were clearly farfetched (sometimes [technology myths](https://www.nngroup.com/articles/technology-myths/)) and reflected the lack of transparency in the algorithm. For example, one user noted:

> *“This is interesting and creepy — yesterday I was talking about craving pho, which I normally don't eat, and now I see this [ad for a] pho burrito; I wonder if they just record your conversations."*

Upon seeing an ad for Hawaiian Airlines, a participant said, half joking and half serious, *“Maybe they know I need a vacation."* And yet another one: “*Ever since I got pregnant, I get ads about pregnancy, baby stuff, and life insurance.”*

Thus, lack of transparency in the input makes users suspicious — they assume that almost every one of their actions (whether online or in the real world) is taken into account by the algorithm and they end up believing that the systems are more “creepy” and intrusive than they are in reality. Such a perception is facilitated by the rising concerns about privacy and an awareness of the vast amounts of data that companies like Google and Facebook are in control of.

Google News users were generally pleased with the successful personalization that the app did for them, but they were also not sure what types of data it was based on. A participant said:

> *“This [the Google News app] seems to be catered to me and my interests […] — the fact that there’s three articles related to cars, which […] is the kind of topic I am interested in. It would be interesting to know how the* For you *page is generated. […] It’s got my local stories, so it obviously knows my location, that’s pretty handy.”*

While Uber does not make recommendations per se, it reputedly uses machine learning to predict demand and create incentives for drivers in the form of price surges, promotions, and gamification (for example, Uber drivers can take advantage of ‘quests’ that give them an extra gain when they drive a certain number of rides within a designated timeframe). The Uber algorithm is not based on driver actions per se; instead, its inputs are likely mostly external data such as historical traffic patterns. Yet, even in this case, a clear understanding of the input had some say in whether drivers were persuaded by some of the promotions or not. For example, one driver was notified that he needed to drive 15 minutes to pick up a passenger located at 2.3 miles away and that a premium was possible. He said:

> *“This is an irritating new feature. I think that in the past you used to get only 5 minutes rides [to pick up passengers], but this one says 15 minutes distance and premium is possible. I had that before and it didn’t happen. I am guessing it’s just a way to entice drivers to go a long distance without getting a fare.[…] I don’t like that possible premium.”*

Not understanding why the premium was offered and what it was based on made the driver suspicious about Uber’s intentions.

## Lack of Control of the Output

In all the systems we looked at, the output depended not only on the users’ actions but also on external events such as other people’s postings, news stories, new movie releases, or traffic. This wide variety of data made it even more difficult to understand how the algorithm could be controlled and to isolate the effects of the user’s own actions from those of third-party actions.

When a set of relevant items has been determined based on some automated prediction, often the order in which those items is displayed and whether they are displayed at all are dictated by a **relevancy metric**: items with a high relevancy are displayed first, followed by less relevant items. If relevancy is below a certain threshold, the item may not be shown at all. (Netflix displayed this relevancy metric explicitly in the form of a match score. The metric itself was of no direct interest to users — people in our study completely ignored this score).

While one could argue that a good relevancy metric should not place important items low on the list, the truth is that these systems gather only fragmentary information about the users, who are complex individuals whose needs depend not only on past habits but also on context and even mood. (For example, one participant said *“I wish there’s a way to hide all the sad posts on Facebook.”* And some posters may be of high interest, but very infrequent, so the system may not be able to accumulate enough data about their relevancy.) So it is very possible that even good relevancy metrics would fail to predict relevancy correctly — at least occasionally.

### Issues Due to Imperfect Relevancy Metrics

There are a few issues that arise due to imperfect relevancy metrics:

#### Items of Interest Are Left Out

In information-retrieval terms, this amounts to **low recall.**

Leaving out a high-relevancy item can be costly for users. On sites like Facebook and Instagram, missing a post by one of your closest friends can cause annoyance and deteriorate the experience. The fact that newsfeeds on these sites contained only a subset of the new posts was a major nuisance for our participants. One participant said, “*I need to fight with the algorithm to get the accounts that I want to see to show up.*” People attempted to steer the algorithm according to their (often incorrect or fragmented) mental model of how the system worked. Some engaged (through the *Like* button) with all the posts from those pages they were interested in, with the hope to convince the algorithm to not miss those posts again. The meaning of *Like* thus went beyond its original literal and social connotations (liking something used to indicate appreciation of the content or of the poster) and started to become construed as a way to assert some control over the algorithm.

Even those who thought they could manipulate the algorithm often were suspicious of their effectiveness. They kept visiting directly the newsfeeds of those people or organizations they were interested in to make sure they did not miss content.

Leaving out a high-relevancy item is not always as costly. For example, on Netflix or Spotify, there are thousands of items that are potentially of high interest to users; leaving one out is unlikely to cause people to complain

#### Unpredictable Ordering of Items

Missing an item that is important to a user can happen not only because the algorithm did not include it in the list of results, but also because it did not include it high enough on the list. Ultimately, this concern is related to the **attention economy**: if people have a finite quantity of attention that they can deploy to news or social media, then items that are important to them may be missed simply because they were placed too low on the output list.

With some of the recommender systems that we saw, **the ordering of the recommendations had no meaning** for the user: people did not understand why a certain post on their Facebook feed was shown before another one, nor did they know why a movie was shown before another one in a Netflix carousel.

A common complaint on Facebook, Instagram, and Google News was that **the order of stories was not chronological**. Because of that, it was not easy to predict whether you’ve seen everything from a person or you may have missed some posts. Similarly, with news, participants were worried that interesting-to-them stories of less importance (such as a car-related article) may come first in a long list and may make them miss recent general-interest news items.

In the case of Netflix, the ad-hoc categories in which the recommendations were structured (e.g., *Because you watched…, Top* picks) obscured natural categories that people have already formed of the domain. For example, with video content, a common concern is time (e.g., users may know they only have 1 hour to watch) or the type of show. Yet, in the Netflix-created categories, TV shows are mixed with full-length movies and presented in no recognizable order without [differentiating markers](https://www.nngroup.com/articles/visual-indicators-differentiators/), and people have no easy way of filtering them out.

#### Low-Interest Recommendations

In information-retrieval terms, this amounts to **low precision.**

**Bad suggestions are costly for the users’ attention**— they must *inspect* them, *identify* them as irrelevant, and *skip* past them. However, the cost of a bad suggestion is not always the same across different types of systems. With Netflix’s list-of-carousels layout, a bad suggestion can be relatively easier to ignore — an uninteresting movie does not take up too much space on the page and people can move around it easily

![Netflix homepage](https://media.nngroup.com/media/editor/2018/11/13/netflix-2.png)

*Netflix: A bad recommendation takes relatively little space in the list layout; people can easily ignore it.*

On systems like Spotify or StichFix (a clothing-shipping service), users cannot ignore a bad suggestion — they cannot simply sit and listen to a song they don’t like or wear a pair of pants that is not their style. Facebook is somewhere in between: an irrelevant post or ad takes space on the page and requires people to scroll past it.

![A Patagonia ad on Facebook](https://media.nngroup.com/media/editor/2018/11/13/facebook-patagonia.png)

*An irrelevant ad on Facebook may take up the whole viewport and requires more effort to ignore than a bad movie suggestion on Netflix.*

**The cost of ignoring a bad suggestion will dictate how likely people are to directly provide feedback on the item**. For example, on Spotify, they will engage with the system and rate the bad item not only in order to tune the algorithm, but also to save themselves from sitting through a song they don’t like.On Facebook, we did notice users engaging occasionally with the *Hide ad* button, but because it was hidden under a menu, some perceived that it was not worth doing it. Instead of down-rating poor recommendations, people focused on *Like-* ing good suggestions.

![Facebook more button associated to an ad](https://media.nngroup.com/media/editor/2018/11/13/facebook-ghide-ad.png)

*Facebook: Few users took advantage of the* Hide *ad option that was hidden under the* More *button.*

**The more real estate (or time to process) taken by a piece of recommended content, the more prominent a feedback button should be.** If recommended content can be easily ignored, the method for providing feedback can be secondary.

### Personalization Should Not Increase User Effort

We saw above that, in the user experience, the most successful recommendation algorithms were those that were able to convey users a reasonable mental model of the inputs they used. In particular, our study participants loved Netflix’s *Because you (watched/added to list/ etc.)…* suggestion lists.

However, a problem with such approaches is that the same item may end up being recommended multiple times. For example, a movie that is included in a *Because you watched* … list can also appear in *My List* or in *Top picks*. **People have to spend extra effort when they encounter these duplicate items** because, at a minimum, they have to recognize that they have seen them before and move over. One user commented:

> “*Why have various lists and keep duplicates? I hate these duplicate lists. I go over it and see the same things I have seen before and it annoys me, ‘cause I feel it’s such a waste of time…”*

*Netflix: The same movie (“What happened Miss Simone?”) appeared both under* Suggestions For You *and under the* Jazz & Easy Listening *lists.*

But duplication of effort is not restricted to repeated items only. Netflix admits going beyond content personalization and creating an individualized (and even session-specific) [homepage layout](https://medium.com/netflix-techblog/learning-a-personalized-homepage-aa8ec670359a) and [personalized cover art](https://medium.com/netflix-techblog/artwork-personalization-c589f074ad76) for videos.

Both these types of personalization can increase [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/).

### Session-Specific Thumbnails, Descriptions, and Headings

Personalizing how a piece of content is presented to a specific user can go a long way in capturing attention. Our study participants were presented with a plethora of content, and they scanned through it quickly, glancing at the thumbnails and reading 1–2 words of text here and there. A Facebook user said, ““*I don't normally even read what people wrote; I just skim through it,”* while a Netflix user commented that *“I look for stuff that is different and interesting, and the cover art calls my attention.”*

On Netflix, not only will two different users see different thumbnails for the same movie (e.g., “Empire Games”), but the same user may see different thumbnails for the same movie in two different sessions.

*Netflix: The same user saw different thumbnails for the movie Chappaquiddick in different sessions.*

In theory, this practice may increase the chance of the person liking the movie and watching it — since different aspects of the movie will be emphasized in different sessions, one of them may capture the user’s attention. Unfortunately, this inconsistency also makes the movie less memorable and wastes user time: people may end up visiting the movie-detail page and checking the description multiple times, only to discover that they are still not interested or that they have already added that movie to their watch list.

### Session-Specific Layouts

Netflix also personalizes the layout of the homepage according to user, session, and device. Thus, *Continue watching* may appear very close to the top of the page for one user in one session, or could be lower on the page in the next session. This practice is an example of an adaptive interface and limits [learning](https://www.nngroup.com/articles/power-law-learning/) of the page layout. Thus, users who prefer to start their browsing with checking the new additions may need to actively look for the *Recently added* list and will not benefit from having located that list in previous sessions. Because Netflix is such a browse-heavy interface, changing the order of the different lists of suggestions did not have a significant impact on our user pool; however, in general, this practice has been shown to significantly downgrade the user experience.

## Recommendations

We looked at a fairly limited number of systems that are heavily dependent on machine-learning algorithms to present content to users. Here are some of the lessons learned:

- **Strive to create an accurate mental model of the algorithm**. Be transparent about which of people’s actions can contribute to the output of the algorithm.
- Give people **easy controls over the output** of the machine-learning algorithm. Allow them to sort or reorganize the output in ways familiar or natural to them. The higher the cost of a bad recommendation, the easier it should be to give feedback to the system.
- Don’t **duplicate content** if it fits into multiple categories.
- **Personalize to individual users** and then stick with that personalized design; be cautious about personalizing at the session level and changing the UI under the user from one visit to the next.
- Pick **visual attributes** that are likely to engage users, since they are very important when people have to consume large amounts of content.
- **Frontload descriptions** and headlines to support the scan of large amounts of data.

Following these 6 UX guidelines will increase the likelihood that AI moves beyond a fancy technology to actively supporting users and increasing their satisfaction with the quality of their experience
