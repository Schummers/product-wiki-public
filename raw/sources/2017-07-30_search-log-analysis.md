---
title: "Search-Log Analysis: The Most Overlooked Opportunity in Web UX Research"
date: "2017-07-30"
url: "https://www.nngroup.com/articles/search-log-analysis/"
author: "Susan Farrell"
topics: [analytics-and-metrics, search]
type: article
---

## In This Article:

- [Introduction](#toc-introduction-1)
- [Search Engines and Search Logs](#toc-search-engines-and-search-logs-2)
- [Why You Want to Analyze Search-Log Data](#toc-why-you-want-to-analyze-search-log-data-3)
- [How to Make Search Logs Useful](#toc-how-to-make-search-logs-useful-4)
- [Insights You Can Gain from Search Logs](#toc-insights-you-can-gain-from-search-logs-5)
- [Acting on Your Findings](#toc-acting-on-your-findings-6)
- [Privacy Danger With IP Addresses and User Identifiers](#toc-privacy-danger-with-ip-addresses-and-user-identifiers-7)
- [Conclusion](#toc-conclusion-8)
- [More Information](#toc-more-information-9)

## Introduction

Analysis of site-search logs is one of the biggest missed opportunities in UX research. Much emphasis is placed on external search optimization (getting the visit) but less attention is paid to on site-search optimization (serving the visitor).

Web-wide search engines can provide some website-search statistics. That’s the outside view of your search traffic that shows which terms and websites drive traffic to your site. If you choose to add some scripts to your pages, these big engines and analytics services can also give you some information about traffic internal to your website. But it’s not detailed enough usually, and often you can’t view the data in the ways you might like to.

If you have a search engine on your website, however, you likely have your own search data, focused on your internal website traffic. Site-search log files contain a wealth of information about your website visitors and what they want from your organization.

## Search Engines and Search Logs

The search engines of most interest to the UX researcher are [site-search engines that focus on the pages and links in your own website](https://www.nngroup.com/articles/internal-website-search/), rather than those that index the whole web (Google, Bing, Baidu, etc.).

Search engines can produce a log (text file) containing a list of all the questions and terms that users type into the search tool. Logs also have useful information about each search query, such as the user’s IP address or other identifier and the time of the request, which means you can often look at a sequence of searches in one person’s session if you sort the list by user identifier and time. [An example of a log from Google Search Appliance](http://rosenfeldmedia.com/search-analytics/log-sample-google-appliance/).

## Why You Want to Analyze Search-Log Data

Search-log analysis can help stakeholders empathize with site visitors, because the data shows people struggling to find what they need. This information can help gain support for improving the website, because it usually illuminates problems that are frequently encountered and difficult to fix without doing significant work. Some problems are easy to fix, though, and the logs show these issues as well.

Search data can impact:

- Advertising strategy
- Content strategy
- Incoming traffic flows
- Information architecture (IA)
- Localization strategy
- Navigation design
- New target audiences
- Search-engine optimization (SEO)
- Usability of search-results pages
- Website vocabulary

Most search engines allow you to force good results (*best bets* for a given query) to the top, once you figure out which queries need that kind of help. They also allow you to make **synonym****relationships** between terms so that when someone searches for X they get Y. For example, this feature helps overcome misspellings or ties branded terms to generic terms. The various ways you can alter what your search engine does form **search**-**engine****tuning**.

## How to Make Search Logs Useful

Ask your sysadmin or IT department whether your organization keeps a search-engine log. If not, ask for logging to be turned on, so you can look through your log every 6 months or so for usability clues.

It’s a good idea to analyze search logs that span a few months, so that you can put weird events in context, such as keyword spikes that happen during an advertising campaign or when a news article is published.

Extract key information from log files before trying to analyze the data. If you are handy with a scripting language and command-line tools, you can pull interesting information from these files yourself. If not, ask for the kind of data listed below. Put these lists into different tabs of a spreadsheet so you can annotate them and highlight items of interest:

1. **Get a list with the top 1000 query terms over 3–6 months**. Sort these by frequency (how often that term occurs in the log).

Mark anything you don’t understand or that you wonder about. Mark anything you know the website does not offer. While analyzing the top 300 or so terms, look farther down the list for terms that are **synonyms** for each other or that naturally cluster together because of **similar****meaning or utility**.

If you see a lot of terms with similar meanings, copy the data to a new sheet and group terms by meaning or shared task. For example, you might find a group of related terms such as: *ATM locations, paychecks, bank, payday, payroll*, and *direct deposit*. That cluster could help you improve content grouping for those on the website, make crosslinks, create see-also–link lists, or help suggest **best bets** for search-results pages.

![Spreadsheet screenshot showing terms sorted by number of queries, and other columns for Recommendation, Owner, Status, and Preferred target URL](https://media.nngroup.com/media/editor/2017/06/23/2017_0231.png)

*Search log formats vary with the search engine. Here is an example of one way to work with extracted data from a log, using a spreadsheet. Many other data points could be included, such as rank on search results pages, your comments, and so on. Terms that are nearly the same and that likely return the same results, such as* holiday *and* holidays *, would be easy to find and count together if this data were sorted by term. It can also be very helpful to cluster terms by meaning, category, owner, and user identifier in other sheets.*

2. **Sort another copy of the log data by IP address or user identifier, then by timestamp**. Some systems use cookies or other unique identifiers to indicate particular browsers, instead of relying on IP addresses. Sorting the log data by user identifier and timestamp allows you to see who searched for more than one term. These user sessions can help you understand people’s word choices, illuminate natural clusters of terms, help you understand what people are looking for, and allow you to find out which search queries were effective or not (for example, repeated searches for related terms may indicate ineffective queries).

For example on a pet store website, you might see that, in 5 minutes, there were 4 queries coming from the same user identifier: *dog*, *canine*, *dog**toys*, *bones.* It would be reasonable to guess that this person wanted to find dog toys, and, more specifically, dog bones, and that the first three queries didn’t satisfy this need.

In order to test this hypothesis, you can redo the searches and look at the results pages. You could perhaps find out if this same user made a purchase or went to the shopping cart during the same few minutes, if you have access to that piece of analytics data.

Even if all you have is the search data, you can evaluate the quality of both the search term and the results for terms in the sequence, then decide whether it’s reasonable to improve those results so that people like this person could succeed with fewer searches. You can also look at the frequent search data to discover how many people looked for *bones* and other related things (*chew**toys*, *rawhide*, etc.), and you can find out whether dog bones exist on the website.

Doing research like this can lead to changing the website in various ways: **search tuning, information architecture, product descriptions, visible representative products, self-advertising promotions on search pages, and new products carried by the store**.

**Note**: IP numbers that are the same sometimes correspond to a server, rather than to a particular person’s device. Most analytics software uses “user sessions” (an amount of time, for example 15–20 minutes, that one IP address or user ID engages with the website) to try to map IP addresses to website visits when IP numbers are not unique. If you see thousands of visits from one IP address, it’s probably not an obsessed fan or a bot, but a group of many people sitting behind one IP address at a company, an ISP, or a proxy server. Similarly, groups of students, cybercafe visitors, airport kiosk users, and hotel customers often share the same browser and computer.

3. **Get the list of search terms with no results**. These queries often indicate both misspellings and wanted information that the search engine can’t find for some reason. Terms that were only used a few times are not of interest, but any terms with lots of searches may point to problems you can address.

**Consider the**[messaging on the no-results page](https://www.nngroup.com/articles/search-no-results-serp/). At a minimum, it should show the site navigation, the search tool with the query in it, plus these suggestions: Check your spelling and try different or fewer terms. If you see that people are searching for something you know the site doesn’t have, consider offering custom results for some terms that point to the resources people need. For example, if the search engine searches only the support website but people are obviously looking for content on the main site, point them in the right direction or pass the search through to the main site and give them what they need.

4. **Get the list of longest queries**. These search terms are often full-sentence searches that can help illuminate some of the one-word terms used in the top queries. Some questions will be irrelevant, but a few might be very interesting and helpful. If you have a lot of long queries, consider making your [search box](https://www.nngroup.com/articles/search-visible-and-simple/) longer to allow more characters to be in view at a time.

## Insights You Can Gain from Search Logs

Beyond the list of top terms (most-wanted information), you can find unexpected insights and new research questions from your search data mining. In particular, you may find out:

### 1. What people want but can't find

**Uses**: IA, search-engine tuning, creating best bets (results you force to the top of search results pages), [popular links lists](https://www.nngroup.com/articles/quicklinks-label-intranet/), and [FAQs](https://www.nngroup.com/articles/faqs-deliver-value/)

**Examples of findings**: On a health product ecommerce website, 11,750 people in one month searched for *heating pads*, but only 13 people bought one. You guess that both the search and the navigation must be useless for this product type. Your test search for that term returns hot compresses and kitchen hot pads. The store carries heating pads, but they are on a page called *Hot & Cold Therapy* found under *Home First Aid.*

**Possible actions**:

- Locate hot compresses near heating pads.
- Add synonyms to the search engine so that when someone searches for *heating pad* they get *hot therapy* products.
- Force *heating pads* up to the top result for that search (*best bet*).
- Add *heating pad* to product descriptions.
- Add a link on the homepage in the *Most Popular Products* section for *heating pads* that goes to *Home First Aid*.
- Some of these things are not possible to do right away, so you add a question and answer to the *Frequently Asked Questions* page with a link to *Home First Aid*.
- Suggest that the company carry more heating-pad brands and add a *heating pad* landing page.

### 2. What people want but does not exist

**Uses**: Content strategy

**Example of findings**: 27,840 people in 3 months searched for *organic chicken stock, chicken stock organic, organic chicken soup,* and *organic chicken.* The food and recipe website doesn’t have any articles or recipes about this topic, however.

**Possible actions**:

- Now that you know about this gap between what people want and what the website provides, prioritize creating some content for this topic.
- Consider whether some existing content could also apply to *organic**chicken*, and if so, showcase that when people search, for example with best bets or search suggestions (a list of searches that displays when someone types into the search box).
- If what people want is outside the scope of your website mission, use this evidence to drive a linking, advertising, or partnership strategy with content providers that do meet these visitor needs.

### 3. The difference between users' vocabulary and the website's vocabulary

**Uses**: [SEO](https://www.nngroup.com/articles/seo-and-usability/), search engine tuning, navigation, content improvement, and glossary terms

Vocabulary mismatch problems happen a lot on websites that use branded terms, acronyms and abbreviations, or cute labeling instead of generic terms. Some websites can benefit from adding synonyms for words in other languages, too.

**Example of findings**: People on a review website about popular chocolate products search frequently for *dark chocolate,* but the website focuses more on *noir chocolate* and *Cote D'or Noir De Noir*, which don’t show up in the *dark chocolate* search results.

**Possible actions**:

- Put the words *dark**chocolate* on all the appropriate pages. Add synonyms to the search engine to make *dark*=*noir*.
- Change navigation labels to include both *noir* and *dark,* (If you have branded terms in navigation, however, just [use the generic term](https://www.nngroup.com/articles/category-names-suck/).)
- Write content to educate visitors about types of and common terms for chocolate in key languages and how those types map to brands, with definitions, links, and descriptions that incorporate the appropriate words you found in the search logs.

### 4. Terms people misspell frequently and others with very poor results

**Uses**: Tune the search engine and bring up appropriate *best bets*(results you force to the top of search-results pages)

**Example of findings**: According to search logs, the most-frequent misspelling of the chief scientist’s name *(Tycho)* is *tyko*. When you do a test search for *Tycho*, you discover the top results are press releases instead of the scientist’s biography and work page.

**Possible actions**:

- Add search synonyms for all the misspellings of *Tycho*
- Add a best-bet result for her name and for *chief scientist* that showcases her biography page at the top of the search results.

### 5. The most-frequent term is no term

**Uses**: No term or blank term requires investigation

**Possible causes**: On some websites, searching with no term returns everything. People use that as a workaround for poor search or poor information architecture. On other websites, this finding may be a result of the search tool looking strange or acting in an unexpected ways, so people accidentally trigger searches while poking at the widget. If the “no term” is actually not blank but consists of many entries that look like this: ______________, try displaying the log in your browser, in Unicode view. These may be queries in non-ASCII character sets. Translate them in Google Translate to find out what’s going on.

### 6. Longest queries show evidence of customer distress or hacking attempts

**Uses**: Requires investigation and possible escalation

**Possible actions for customer distress**:

- Change products or services.
- Add relevant material to the FAQ.
- Change product documentation and add support material.
- Return custom search results or suggestions to call support when key terms are searched for.

**Hacking attempts**: If longest searches are giant blocks of characters or something that looks like code, commands, or nonsense, report it to your security team or sysadmin immediately. All forms should have limits to the number and kind of characters that they accept.

### 7. Many frequent terms are numbers

**Uses**: Content strategy, website features

**Possible causes**: Numerical searches are often for product identifiers. If you see lots of product numbers in the logs and your search engine doesn’t find those products when you do your test searches, it could be time to implement a product-number search capability.

If people are searching for phone numbers or partial phone numbers, they might need to find contact information such as names, departments, and addresses, so test those results to see if they seem helpful enough. If you see people searching with phone numbers on an intranet, it could be time to implement a [people search](https://www.nngroup.com/articles/employee-directory-search/).

## Acting on Your Findings

As discussed, it’s typical to need to tune the search engine for vocabulary and misspellings. You might also need to add some page redirects.

Run the top-100 queries and capture the first page of results. Note whether anything useful was found. If something good is on the page, but it’s not high on the page, consider what might be done to raise its rank. Use this data to make *best bets* for some queries and to hide noisy results that lead people to the wrong information.

For problems found that may lead to larger changes, such as new features, new content, different information architecture, or larger issues involving products, support, security, and so on, share your findings with other stakeholders. Understanding search insights can be a catalyst for improving many organization processes.

Keep track of questions and findings that should be researched further using other methods, then pitch those projects.

## Privacy Danger With IP Addresses and User Identifiers

IP addresses and other user identifiers are very sensitive in terms of user privacy, because they can (but don’t always) correspond to a particular person and machine. If your sysadmin won’t give you raw log data, this is why. Some countries have strict privacy laws that limit the use of unique identifiers for website tracking, so this data might not be available. Sequential searches are the only reason you would need unique identifiers for search-log analysis, so you can still do a lot of analysis without that information.

If you are entrusted with raw logs having personally identifiable information (PII), don’t lose control of this data, don’t email unencrypted logs containing PII, and never put logs in world-readable locations, not even inside companies. Remove PII before sharing log data with anyone else, and destroy logs after you have analyzed them.

## Conclusion

Search data has a wealth of vital information for UX research, website strategy, and marketing. Take the time to find yours and look at it. You may discover user behavior that surprises you and changes what the organization is doing. Search data can enhance your user research efforts by helping you ask very important questions and find big problems to fix.

## More Information

Our day-long course on [data analysis and analytics](https://www.nngroup.com/courses/topic/analytics-and-metrics/)

[Louis Rosenfeld, Search Analytics](https://www.amazon.com/Search-Analytics-Your-Louis-Rosenfeld-ebook/dp/B005EI86HC), [Rosenfeld Media, July 2011](http://rosenfeldmedia.com/books/search-analytics-for-your-site/). Digital ISBN: 1-933820-04-7

[SIGIR: Conferences on Information Retrieval](http://sigir.org/conferences/sponsored-conferences/)
