---
title: "7 Ways to Improve Your Website’s or Intranet’s Built-In Search Engine"
date: "2016-03-13"
url: "https://www.nngroup.com/articles/internal-website-search/"
author: "Page Laubheimer"
topics: [search]
type: article
---

Contemporary websites focus on optimization for external search engines like Google, Baidu, and Yandex. While search-engine optimization (SEO) is certainly important for bringing visitors to your website, the quality of the *built-in* search is often overlooked. Users do engage with the site search to find products, content, and other key assets; failing to provide a good search experience can lose [conversions](https://www.nngroup.com/articles/conversion-rates/), sales, and ultimately customers.

There are a few standard practices that can be used to strengthen your site search. Before discussing them, we define two key information-retrieval terms used for evaluating the performance of a search engine: precision and recall. These can help you better understand the implications and tradeoffs of the techniques below.

## In This Article:

- [Two Metrics for Search Performance: Precision and Recall](#toc-two-metrics-for-search-performance-precision-and-recall-1)
- [7 Techniques for Improving Site Search](#toc-7-techniques-for-improving-site-search-2)
- [Summary](#toc-summary-3)
- [References](#toc-references-4)

## Two Metrics for Search Performance: Precision and Recall

- **Precision** is the percentage of **retrieved search results that are relevant**.
- **Recall** is the **percentage of all relevant results** that the search system actually retrieves **.**

Imagine that on a recipes website, we have 1000 recipes, of which 300 are for Indian dishes. Assume that when we search for Indian dishes, we get 500 results on the search-results page. Of those 500 search results, only 100 of them are actually Indian dishes; the remainder 400 are actually nonIndian recipes that are not relevant to our search. That means the **precision** is 100/500 or 20%. The **recall** would be 100/300 or 33%, as the search engine only found 100 of the 300 Indian recipes available on the site, which means that 200 Indian recipes didn’t show up on our search-results page at all. A perfect search engine would give us only 300 results total, corresponding to the 300 Indian recipes available on the site, so it would have 300/300 or 100% precision and recall. However, in the real world, that rarely happens. Different techniques that we discuss below trade off precision for recall, or vice versa, so it’s important to understand the conceptual difference.

One of the great insights of the original Google team was that precision is more important than recall for most web searches: there’s so much information available on the Internet that nobody would even *want* to see all the relevant results. For web-wide search, it’s much more important to focus on high precision: to make sure that all the top 10 hits are as highly relevant as possible to the user’s current problem.

In contrast, for internal searches on a single website or intranet, recall can be quite important. For example, if you search an engineering company’s intranet for information about all suspension bridges the company has consulted on in the past, it would be unfortunate to miss one or two bridges and leave them out of the *References* section of a new bridge proposal. Or, on an ecommerce site, if a search misses a relevant product, the customer will assume that the site doesn’t carry it and go elsewhere to buy it.

## 7 Techniques for Improving Site Search

**1. Manually improve results for common queries**

Many typical commercial search engines that are available for integration with websites and intranets offer features for manually improving common search queries. In order to make better use of these features, you’ll want to routinely review search logs and evaluate the results returned by your site search to frequent user queries. When your relevance algorithm fails to return items that you consider highly relevant, you can manually indicate those items and surface them to the top of the search-results list for certain queries. However, be cautious about separating the manually promoted items into a “promoted” or “best bets” list when presenting the results, [as users often ignore these](https://www.nngroup.com/reports/intranet-searching/), like they ignore pay-per-click ads on web search engines. Instead, just integrate the manual hits with the search-engine–generated hits and present a single list to the users.

**2. Provide curated search suggestions**

Search-term suggestion (also called predictive search) refers to displaying suggested queries right below the search box while users are typing. However, an unedited list of common queries from the search logs will not be helpful. Remember, user queries may be misleading, inappropriate, or contain terms that have no results. Instead, suggest *curated* query terms that retrieve useful results. The suggestions can be based on your search logs or on your content’s descriptive metadata (more on this in our full-day [Information Architecture seminar](https://www.nngroup.com/courses/information-architecture/)). It is also critical that you highlight those suggested-query terms that match the input query, so users can easily identify the similarity (if, for example, the typed word appears in the middle of a suggested query).

![Ebay uses bolding to indicate search suggestions](https://media.nngroup.com/media/editor/2016/02/03/ebayseachsuggestions.png)

*Ebay uses bolding to indicate how the user’s typed query relates to the query suggestions.*

On ecommerce sites the predictive box should also show *product**results* with photos to help users evaluate products quickly. (For more information and additional guidelines for ecommerce search, see our report [Ecommerce User Experience: Search](https://www.nngroup.com/reports/ecommerce-ux-search-including-faceted-search/).)

For Intranets, one of the most impactful guidelines that has huge [ROI](https://www.nngroup.com/articles/return-on-investment-for-usability) is implementing [employee suggestions for search](https://www.nngroup.com/articles/suggested-employee-search/): queries that match to employee names show contact information, photos, and links to employee-specific pages as the user types. Presenting employee contact info as a “zero-click” result (where users don’t even have to click on a search result to find the information they seek) can save an enormous amount of employee time, and company money. (For more intranet-specific considerations, see our [Intranet Search Guidelines Report](https://www.nngroup.com/reports/intranet-searching/).)

**3. Recognize synonyms and alternative terms**

Users often don’t formulate perfect queries. Perhaps they don’t know the appropriate phrases or [industry jargon](https://www.nngroup.com/articles/specialized-words-specialized-audience/), or maybe they don’t know exactly what they’re looking for yet, and start with vague search terms.

![Best Buy's search doesn't allow for synonyms](https://media.nngroup.com/media/editor/2016/02/03/bestbuysynonyms.png)

*Searching BestBuy.com for “soundbar cable” brings up tons of soundbars, but no matches for the actual cable needed to plug a soundbar into a TV. BestBuy’s search engine only accommodates the technical name for that cable, “optical cable”, without assisting users who aren’t AV experts. This lack of flexibility can send users to competitors with a more accommodating site search.*

Your site search should accommodate realistic user synonyms and alternative terminology, especially if your content is jargon heavy, industry specific, or technical. Remember, your users likely don’t know the carefully crafted lingo that everyone in your office uses on a daily basis. Review your search logs and look for synonyms that you don’t currently have in your content. Then you can create synonym tables in your search engine where user search terms map to existing terminology that returns appropriate results.

**4. Accommodate variant word forms with stemming**

Here’s another common scenario: imagine that you searched for the term “marketing automation” on a website. If the writers had only used terms such as “automated marketing solutions”, your search wouldn’t have any results, even though lots of relevant articles on the site did match your information need (but did not match your exact query). You might assume that the website didn’t have any pertinent content and leave.

This issue could be avoided by using a process called stemming. Stemming **refers to removing endings (like suffixes) from words, and reducing them to their morphological ‘stem.’** For example, in English, the words *reduction*, *reduce*, and *reducing* would all be stemmed to *reduc*. If a search engine uses stemming, a search for *reduction* will also return results containing the word *reducing*.

Many commercial search products have a stemming feature available (such as the gold-standard [Porter stemmer](http://tartarus.org/martin/PorterStemmer/)). By default, this feature is often not enabled; turning it on is easy and thus a low-cost search improvement.

Although stemming will boost recall, it can also lower precision by returning results that are not relevant, but happen to include the stem of a query word. For example, a search for “university” may also return “universal” because the two words share the same stem. Decide whether stemming is right for your site by analyzing search logs and checking how many user search terms are variants of words used on your site.

**5.  Handle misspellings gracefully**

Typos and misspellings are extraordinarily common, which is why all big search engines offer a form of *Did you mean* spelling corrections. Although spelling suggestions are recognized as critical, many site-search systems don’t support them. Especially when your content includes a lot of complex jargon (such as on B2B websites), spelling suggestions are key to helping your users find what they need. Oftentimes query suggestions will assist users in adjusting spelling errors *while* they are typing the query. However, sometimes users will forge ahead with a misspelled query, and you’ll need to gracefully handle the problem on your search-results page by offering a *Did you mean* link.

If the original query doesn’t have any results, it’s a good practice to also go ahead and automatically retrieve the results for the alternative-spelling suggestion, without requiring the user to click the *Did you mean* link. Just be sure to make it clear that you retrieved results for a variation of the user’s spelling

![Google indicates when it has shown results for a spelling suggestion](https://media.nngroup.com/media/editor/2016/02/03/googlemispellings.png)

*Google indicates when it has chosen to retrieve an alternative spelling for a user’s query, and gives a clear option to force a search with the original spelling.*

**6.  Support homophones**

Sometimes users may type in a homophone instead of the word they actually mean. (Homophones are words that sound the same, but are spelled differently – such as “peace” and “piece”, or “Stuart” and “Stewart”.) For these situations, a useful tool is Soundex, which is an algorithm used to find similarly sounding words that are spelled differently. Soundex converts search terms (and words from indexed content) into their phonetic representations, and enables your site search to retrieve results that are spelled completely differently from the query words, but are pronounced in the same way. Soundex is widely available and can benefit searches for proper names, jargon terms, foreign words, and more. It’s even built into programming languages like PHP, and into MySQL databases, so it’s relatively easy for your development team to integrate it into the search engine.

Both spelling suggestions and the use of homophones improve the recall, but they can lower precision, by returning results that may not be relevant, but happen to sound like the query word.

**7. Ignore stop words**

The majority of words that fill out even the best written content on the web are **stop words.** Stop words include function words such as articles (“a”, “the”), prepositions (“of”, “for”), or conjunctions (“but”, “and”), but also other high-frequency words (“be”, “seem”) that appear in most documents and are unlikely to be distinctive for any one of them. These words can negatively affect search relevance.

The easiest way to manage this problem is to have your website’s search engine use a list of excluded **stop words**, ignored in users’ queries. If your search engine doesn’t do a lot of complex language modeling to determine relevance ranking, removing stop words from the users’ queries can have two benefits: (1) it can speed up the search performance, and (2) it can help to suppress irrelevant results that contain these common words. Many stop-word lists are available for most languages, but, before using one, do make sure that it does not include any terms that are uniquely important in your industry or on your website.

Ignoring stop words will boost precision, but lower recall, especially in edge cases like the famous example of “to be or not to be”, which is made *entirely of* stop words. However, if your search engine already does complex phrase matching and natural-language processing (much like Google does), do *not* exclude stop words, since those offer additional context that can improve the search results.

## Summary

While the major web search engines have grown ever more sophisticated, the built-in search on many websites has been neglected. Stemming, excluding stop words, showing curated query suggestions, and using homophones and spelling suggestions all modify the search query either to accommodate [user errors](https://www.nngroup.com/articles/slips/) or to address possible variations in word choice, and may improve the quality or the number of search results without requiring a major development investment.

## References

Dan Jurafsky, “Stanford Natural Language Processing: Word Normalization and Stemming” ([link](https://class.coursera.org/nlp/lecture))

W. Bruce Croft, Donald Metzler, Trevor Strohman, *Search Engines: Information Retrieval in Practice*, Addison-Wesley, 2010.
