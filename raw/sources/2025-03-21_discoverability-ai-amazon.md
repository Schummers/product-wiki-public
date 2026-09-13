---
title: "Discoverability of AI Features: Learn from Amazon’s Mistakes"
date: "2025-03-21"
url: "https://www.nngroup.com/articles/discoverability-ai-amazon/"
author: "Feifei Liu, Kate Moran"
topics: [ai]
type: article
---

The first step to delivering a successful AI feature in your product is to make sure it’s valuable to your users and business. ([Most AI features fail at step 1.](https://www.nngroup.com/articles/ai-user-value/)) But even *valuable* AI features will still fail if users don’t see them.

## In This Article:

- [People Don’t Notice That AI Feature…](#toc-people-dont-notice-that-ai-feature-1)
- [Amazon.com Case Study](#toc-amazoncom-case-study-2)
- [“Rufus” Chat: Valuable but Invisible](#toc-rufus-chat-valuable-but-invisible-3)
- [AI in Search: A Mental-Model Mixup](#toc-ai-in-search-a-mental-model-mixup-4)
- [Product Q&A Chat](#toc-product-qa-chat-5)
- [Avoid the AI Discoverability Problem](#toc-avoid-the-ai-discoverability-problem-6)

## People Don’t Notice That AI Feature…

…Even if it’s right in front of them.

AI features (like all UI elements) are liable to be overlooked by users if they aren’t expected. And right now, as many sites and apps are adding their first AI features, their customers (even if fairly AI-savvy) don’t expect them.

### Many AI Features Lack Discoverability

A quick reminder:

> When a feature has good **findability,** users can easily find it if they look for it.

> When a feature has good **discoverability,** users notice, recognize, and understand it even when they were not previously aware of its existence.

In our qualitative usability testing, we found that the majority of AI features we tested lacked both [discoverability and findability.](https://www.nngroup.com/articles/navigation-ia-tests/) In other words, our participants mostly:

- **Didn’t expect or think to look for** AI features in apps or sites, even when they reported having used similar systems in the past
- **Didn’t notice, comment on, or use** AI features when they happened to encounter them (poor discoverability)
- **Couldn’t easily find** those features when we directed them to look for them as part of a [stepped-task](https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/) study methodology (poor findability)

This was unfortunate because, in several cases, participants [found the features useful](https://www.nngroup.com/articles/ai-user-value/) once researchers led them to these features. For example, one participant told us:

> *“Honestly I just didn’t even notice [the AI feature]. I’m wondering why it was here. It was definitely really helpful, but I totally missed it.”*

## Amazon.com Case Study

To explore the discoverability problem, let’s look at some of the AI features on Amazon’s website and mobile app. The site offered several AI features integrated at various places in its interface. They all were valuable to users, but unfortunately, haphazard design impeded their discoverability and usefulness.

In this article, we’ll analyze 3 of Amazon’s AI features:

- **A global site chat** named *Rufus*, accessed through the global navigation
- **AI-prompt suggestions** in the search bar
- A product-specific **AI-powered Q&A**

They were all intended to help people navigate the vast number of product options available on Amazon and make shopping decisions easier, thus ensuring that users will keep coming back and buy more.

At the time of writing, Amazon’s AI features appear to be available only to signed-in customers in some regions. (Required authentication is a smart business decision because it likely limits misuse or abuse of those features.)

## “Rufus” Chat: Valuable but Invisible

Amazon’s site-wide AI chat **offered a lot of user value,** especially since it had the useful context of what the shopper was currently (and had previously been) searching and browsing for. It acted as smart shopping assistant, following the user around from page to page and answering questions.

*Amazon desktop site: On larger devices, the site-wide AI chat could be accessed by clicking the* Rufus *button in the global navigation bar. Once initiated, the AI chat could provide information about product categories*(What’s the difference between silk and satin pillowcases *?) or suggest specific product options.*

Unfortunately, **none of our participants noticed it** until a researcher pointed it out. The global chat suffered from severe discoverability issues on both desktop and mobile.

On larger devices, the AI chat button was:

- **Located in a nonstandard location, in the upper left corner under the logo.** People expect to find a chat button in the lower right corner of the screen, where it is usually placed on most sites. (This is an example of how [external consistency](https://www.nngroup.com/articles/consistency-and-standards/) across experiences sets expectations and builds [mental models](https://www.nngroup.com/articles/mental-models/).)
- **Given a label that was unfamiliar to users:** Even the frequent Amazon shoppers in our study admitted they’d never noticed or thought to click this button. Why would they? Unless they’d previously encountered it, the name *Rufus* doesn’t mean anything to people.
- **Represented by a new version of the sparkles icon:** As they encounter [the sparkles icon](https://www.nngroup.com/articles/ai-sparkles-icon-problem/) in different products, people are starting to (vaguely) understand that it represents something related to AI. The meaning of the sparkles icon, is, however, nowhere from established, and Amazon’s design makes it worse by turning two of the sparkles into chat bubbles.

Additionally, the AI chat’s lack of discoverability was aggravated by Amazon’s busy design, which displays vast amounts of competing information, options, and promotions. Combined with the fact that users didn’t expect an AI chat on Amazon in the first place, these issues made the Rufus button invisible to our participants.

*Amazon mobile app on iOS: On smartphones, the hybrid chat/sparkles icon was more visible, since it was relatively larger in the small screen space. However, it was still ignored by users because the unlabeled and ambiguous icon did not communicate any meaning.*

Once people found and used the chat, it did have several more UX problems (for example, a tendency to get confused about what the user was shopping for or to give unnecessarily wordy and jargon-filled responses.) However, most participants liked Rufus and said they could see how it’d be helpful. A few also admitted that they would’ve never thought to use it without the facilitator pointing it out.

For example, after the facilitator directed her to Rufus, a study participant shopping for Birkenstock shoes was particularly impressed that the AI was aware of the product she had searched for and appreciated the relevant suggested followup questions and in-context information.

“This is dangerous,” she said, indicating that **it would make her likely to buy more**— surely Amazon’s exact intention.

However, she admitted that **she never would have noticed** or used the Rufus chat without the facilitator’s help.

> *“It was easy when you [the facilitator] showed it to me, I’ve just never heard of Rufus before, so I had no idea what that was. I probably would have just ignored it… Even looking at it [now], I don’t know what Rufus is until after having used it.”*

## AI in Search: A Mental-Model Mixup

In addition to the nonstandard *Rufus* button in the global navigation, Amazon.com also offered another unexpected and unnoticeable way to start conversations with its AI chatbot — through its [search suggestions](https://www.nngroup.com/articles/site-search-suggestions/).

As logged-in users typed keywords into the search, AI-**prompt suggestions** appeared below the search suggestions. Unlike the search suggestions (which are typically just a few words), the prompt suggestions were phrased as questions. The prompt suggestions also had a different icon next to them — instead of a magnifying glass, a small, outline version of the Rufus icon preceded each question. Clicking one of these prompts opened the Rufus chat, where Rufus would generate a response to the selected query.

*When users typed in the Amazon search bar, a few prompt recommendations sometimes appeared below the search suggestions and redirected users to the Rufus chat.*

The AI prompt suggestions went completely unnoticed without facilitator guidance.**None of our participants proactively clicked a prompt suggestion during the study**— not even those who reported using Amazon daily. Several factors contributed to its low discoverability.

First, there was **no visual indicator to suggest the search bar was any different** than it had always been. The placeholder text of the Amazon website’s search bar simply read *Search Amazon*, providing no indication that users could enter natural-language queries to initiate conversations. In contrast, the mobile app's placeholder text was changed to *Search or ask a question,* but this was a weak signifier, since people [rarely pay attention to placeholder text.](https://www.nngroup.com/articles/form-design-placeholders/)

Especially on larger devices,**the prompt suggestions blended in with regular search suggestions:** the same visual style was used for both and the icons preceding them were relatively similar. The prompt suggestions were also placed at the bottom of the recommendation list, far away from the search box, where participants’ attention was focused. And, because they were phrased as questions, they were not frontloaded with meaningful keywords and were less likely to be noticed during scanning.

*The prompt suggestions on Amazon.com were not easily distinguishable from regular search keyword suggestions.*

However, **the most significant challenge preventing users from adopting this feature was their existing**[mental models](https://www.nngroup.com/articles/mental-models/)**for search.** For decades, people have been trained to enter concise, keyword-based queries in search bars. Now, in the era of generative AI, they are suddenly being encouraged to type full sentences, directions, or questions in the same input field.

One participant said he wouldn’t consider using Amazon’s search bar to find information or shopping help, “**because that’s where you find products**.” After many years of being conditioned to use Amazon’s search only to find products, it’s tough for people to adjust.

The mental-model violations didn’t end here. In general, when users click or tap a search suggestion, they expect it to take them to a search-results page for that query. But when guided participants selected a prompt suggestion, the Rufus chat window opened instead. This violation of expectations created confusion and a feeling of lack of control for users.

#### Mental Models Can Change, But Slowly

Mental models are rigid but not unchangeable. As AI-powered search features become more prevalent, users may gradually expect AI chat or prompt suggestions to be integrated into search. We observed signs of this shift in our youngest participant, a 20-year-old woman, who instinctively looked near the search bar when prompted to find AI features in the Walmart app. She reasoned:

> *“I feel like if I am looking for AI. I feel like it should be like right near the search bar… I have heard of Meta AI before, and obviously never used it, but that's why I think I assumed in the Walmart app, where's the AI feature, and I thought it would be just like here, like Instagram.”*

As new design patterns emerge and become standardized [across many digital experiences](https://www.nngroup.com/videos/jakobs-law-internet-ux/), **user populations will slowly adapt.** But that takes time, and different populations will adapt at different rates.

## Product Q&A Chat

A slightly more [scoped](https://www.nngroup.com/articles/scope-ai-features/), limited version of Rufus appeared within individual product pages, integrated with what was previously a simple [scoped search](https://www.nngroup.com/articles/scoped-search/) for user-generated questions and answers about that product. That’s a common-sense place to integrate a feature that can help people navigate through dense product information and (sometimes) provide answers to users’ questions.

*In this example, the user asked the embedded AI search if the smart lock she was considering could be programmed to accept multiple entry codes.*

Unfortunately, Amazon product pages tend to be incredibly dense and chaotic. This is partially due to page design, but also to the millions of sellers who independently list their own products on the site. **These promotion-packed pages** do benefit from an AI Q&A, but unfortunately, their high information density made the feature hard to discover. Amazon’s AI Q&A was buried towards the bottom of the page, at the very end of the product description. Participants often scrolled quickly through that area in search of product reviews.

*Amazon product pages tend to be extremely long, colorful, and crowded. If users are aware of the embedded AI search, they may prefer to use it instead of scanning these long pages in search of specific information. Unfortunately, most of our participants scrolled right past this feature without noticing it.*

In contrast, a similar feature was very discoverable on TripAdvisor, which placed the page-specific AI assistant in a visually distinctive section.

*On TripAdvisor, the* Ask our AI assistant *section was visually separated from the main page, so it was easy to discover.*

## Avoid the AI Discoverability Problem

Mental models and behavior patterns will evolve over time as people keep encountering more of these AI features in the products they use. However, that will take time — probably more than you want to wait to see improvements in your engagement metrics.

Minimize the discoverability problem by applying the best practices you’d use when designing any other feature.

**Leverage standard design patterns** as much as possible. For example, put AI-chat buttons where people expect to find to chat —- floating in the lower right corner of the page. Use plain language. Don’t invent unnecessary labels, cute names, or inscrutable icons where something standard will be more noticeable.

And, critically: **conduct research!!!**

[Exploratory research](https://www.nngroup.com/articles/discovery-study-guide/) will ensure that the AI feature has a reason to exist. It will also help you understand where in the user’s workflow the feature should appear and what existing mental models you need to work with.

[Evaluative research](https://www.nngroup.com/articles/qual-usability-testing-study-guide/) will help you identify discoverability problems and adjust your strategy accordingly.
