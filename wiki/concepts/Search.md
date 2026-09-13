---
type: concept
name: Search
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Recherche Sémantique"
  - "Search Engine Results Pages"
  - "Search Suggestions"
  - "Search User Experience"
  - "Semantic Search"
  - "Site Search"
---

# Search

## Definition

Search covers both the built-in search of a site, intranet, or application — its interface, its algorithm, and the content and metadata behind it — and the search-engine results pages that shape what users expect from any search box they encounter. It is a critical path to task completion: users turn to search when navigation fails, and they typically arrive with a query already formulated, using search to bypass navigation and reach a known item as fast as possible [[2022-08-21_enriched-site-search-suggestions]]. Its quality is consequently a driver of conversion and satisfaction, yet it remains one of the most persistent web design weaknesses: search that fails to match user queries or indexes only part of the site wastes users' time and can push them onto inaccurate information [[2016-10-30_top-10-enduring]].

Two forces run through the sources. First, expectations are set elsewhere: users' mental models of how search works are shaped by Google, or by the dominant engine in their country, so a site's own search features should cater to those expectations [[2020-04-26_key-serp-features]] — employees testing intranets expected Google-like search and were repeatedly disappointed [[2022-05-22_intranet-search]]. Second, in the more recent French-language corpus, search is being redefined by embeddings: semantic search that understands the meaning and the whole word-universe of a query rather than matching keywords [[2025-07-01_384_Top_7_patterns_UX_pour_intégrer_l_IA_dans_vos_interfaces]], letting a designer find reference screens by typing a user story or a job to be done [[2025-09-09_394_Top_5_outils_IA_Product_Design_&_UXUI_-_Septembre_2025]].

## Practice

### Precision, recall, and the retrieval layer

Two metrics evaluate search: precision, the share of returned results that are relevant, and recall, the share of all relevant results actually retrieved [[2016-03-13_internal-website-search]]. Web-wide search prioritizes precision because only the top results matter; internal search must balance both, because a missing item leads users to conclude the site does not carry it. The techniques offered trade one against the other, which is why the distinction matters [[2016-03-13_internal-website-search]]. Seven techniques for improving a built-in engine [[2016-03-13_internal-website-search]]:

- Manually curate results for common queries, reviewing search logs and integrating promoted results into the algorithmic list — avoid a separate "best bets" panel, which users ignore like advertising.
- Offer curated search suggestions built on content metadata rather than raw search logs, with matching terms highlighted.
- Map synonyms and jargon variants, since users often do not know the industry's terminology.
- Use stemming so that "reducing" matches "reduction", while accepting that it can lower precision.
- Handle misspellings gracefully with "Did you mean" and by auto-retrieving corrected results, making the correction obvious.
- Support homophones.
- Exclude stop words.

Search quality is not only an algorithm problem. Intranet search is only as good as the content behind it: coherent page titles, meta descriptions, and tags are foundational, and without clear naming conventions and processes the results become meaningless [[2022-05-22_intranet-search]]. Recency is part of relevance — users check publication dates, recent content should rank higher, and outdated content should be retired through auditing [[2022-05-22_intranet-search]]. The same content-side point appears in the list of enduring mistakes: review search logs regularly and tag content properly [[2016-10-30_top-10-enduring]].

### The search interface

Expose search prominently with a persistent search box, in the upper right, rather than a magnifying-glass icon alone — this primes users to search and follows web convention [[2022-05-22_intranet-search]]. Unify search rather than splitting it: index all content, people, and tools in a single search instead of offering separate boxes per content type [[2022-05-22_intranet-search]]. Placeholder text should say what can be searched without looking pre-filled, persist until typing begins, and return if the user deletes their text [[2022-05-22_intranet-search]]. Results should be clean and scannable, separated into distinct sections for content, people, and tools, with dates, metadata labels, and icons so relevance can be judged quickly [[2022-05-22_intranet-search]].

Filtering is adjacent and often mishandled: a one-size-fits-all set of criteria fails different user needs, so offer both include and exclude options and tailor facets to the content type [[2016-10-30_top-10-enduring]].

### Search suggestions

Suggestions are recommended queries appearing in a dropdown as the user types, updating with each letter [[2018-05-20_site-search-suggestions]]. They have become an expected feature — users comment when they are missing — and they lower interaction cost, prevent typos, and inform users of the range of products a site offers; conversely, if a product name does not appear after the first few characters, some users conclude the site does not carry it and leave without even running the search [[2018-05-20_site-search-suggestions]]. Guidance [[2018-05-20_site-search-suggestions]]:

- Every suggested query must return good, relevant results. Suggestions leading to zero or irrelevant results are worse than no suggestions at all.
- Use different text styling for the characters the user typed and those the system suggested, so people understand why a suggestion appeared and can scan the options.
- On a scoped site, visually distinguish the scope of each suggestion (category, department) so the search area is clear.
- Rich suggestions — links to category pages, product pages, articles — work best on sites with visually diverse products.
- On small screens, simplify rich suggestions down to text only.

The two suggestion sources agree that suggestions are expected but disagree in emphasis on how far to enrich them, and both report low take-up. Suggested queries were selected in only 23% of the instances where they were offered [[2018-05-20_site-search-suggestions]]. Enriched suggestions fare far worse: used 7 times out of 60 instances encountered [[2022-08-21_enriched-site-search-suggestions]]. Four reasons are given for that gap [[2022-08-21_enriched-site-search-suggestions]]: users in search mode are goal-focused and not looking to explore, so query-irrelevant suggestions feel like distractions; image-based enriched results often load too slowly to be useful, appearing after the query has already been submitted; banner blindness means users fixate on the search box and overlook graphical content, missing even exact product matches; and unlabeled enriched suggestions get read as ads or upsell attempts rather than results. The recommendations that follow are to keep simple text autosuggestions, which users heavily use even when enriched ones are present, and to avoid shifting content types and inconsistent placement inside the enriched container, giving each content type a dedicated space [[2022-08-21_enriched-site-search-suggestions]].

### SERP features and how they change behaviour

Three SERP features studied through eyetracking and usability testing between 2016 and 2019 — featured snippets that excerpt an answer, People Also Ask accordions of related questions, and knowledge panels about entities [[2020-04-26_key-serp-features]]. Their effects:

- They act as signposts, letting users verify quickly that results concern the entity they meant, especially with images or video thumbnails.
- They replace linear top-to-bottom scanning with a pinball pattern, users bouncing between features and organic results according to visual emphasis and expected benefit.
- Their appeal is low interaction cost against high expected benefit: an answer without an extra click, page load, or leaving the view.
- Users sometimes keep reading a knowledge panel after clicking a result, returning to the SERP while the next page loads.
- They make query reformulation easier by presenting expanded, natural-language interpretations, so users pick from computer-generated alternatives instead of inventing their own.
- Because Google conditions expectations, internal site search should incorporate similar SERP-feature designs [[2020-04-26_key-serp-features]].

The Google–Baidu comparison shows those patterns are produced by design, not by search itself. The pinball pattern was near-absent on Baidu — one search in more than sixty — where most participants scanned sequentially [[2020-05-31_google-baidu-serp-comparison]]. The cause is relevance: Google's knowledge panels answer the user's question, while Baidu's right rail carries ads and unrelated searches that users learn to ignore. Both engines promote their own properties, but Google's integration reads as organic and Baidu's as forced; when Baidu's promoted content is task-relevant, users do engage with it [[2020-05-31_google-baidu-serp-comparison]]. The lessons drawn: relevance beats prominence, task-relevant content attracts attention even when not prominently placed while irrelevant content is ignored in prominent positions; mental models form from repeated exposure, so an area that has consistently shown irrelevant content will be ignored even after it improves; and it is fine to promote content on a SERP as long as it serves the user's task [[2020-05-31_google-baidu-serp-comparison]].

### AI and semantic search

Semantic search is presented as one of seven UX patterns for embedding AI in interfaces, an alternative to the free-form chatbot whose limits are that it lacks intuitiveness and forces users to guess by trial and error what the tool can do [[2025-07-01_384_Top_7_patterns_UX_pour_intégrer_l_IA_dans_vos_interfaces]]. AI modernizes classic search by using embeddings to grasp a full semantic universe and can display generated summaries inside a feature users already know how to operate — the guiding question being the right interface for the right context, for AI and non-AI features alike [[2025-07-01_384_Top_7_patterns_UX_pour_intégrer_l_IA_dans_vos_interfaces]].

Two applications from the same corpus, both about design benchmarking. Pablo.club is a free community library of screenshots whose AI-powered semantic search lets a designer find screens by describing a precise use case rather than by keyword — an answer to the classic problem that traditional inspiration libraries return poor results on very specific queries [[2025-03-04_367_Le_meilleur_outil_de_benchmark_gratuit_1000+_screenshots]]. To get value from it, the advice is to write very detailed queries in the AI search bar and to explore the similar-screenshots section [[2025-03-04_367_Le_meilleur_outil_de_benchmark_gratuit_1000+_screenshots]]. The later tools round-up describes the same library, by then over 5000 screenshots, as searchable by typing a user story or a job to be done directly, and adds Perplexity as an AI-run search engine for benchmarks and complex technical subjects, synthesizing multiple sources into sourced, clear, concise answers — judged better than ChatGPT Search — and Figma's little-known "Find More Like" for retrieving similar screens from an image or frame across a workspace [[2025-09-09_394_Top_5_outils_IA_Product_Design_&_UXUI_-_Septembre_2025]]. That source keeps its own caveat: AI accelerates certain phases, but the bulk of research, conception, and reflection is not replaced, and a tool must answer a need — the presence of AI is not what makes it good [[2025-09-09_394_Top_5_outils_IA_Product_Design_&_UXUI_-_Septembre_2025]].

## Sources (10)

- [[2016-03-13_internal-website-search]] — design and implementation of built-in search interfaces and algorithms.
- [[2016-10-30_top-10-enduring]] — Site search remains a major weakness; search logs reveal what users actually seek and show where results fail to match queries or content isn't indexed.
- [[2018-05-20_site-search-suggestions]] — Search suggestions have become expected on well-designed e-commerce sites; effective implementation requires guidance on differentiating typed and suggested text, handling scoped searches, and choosing between rich suggestions and simple text, though user behavior shows suggestions are selected in only 23% of instances where offered.
- [[2020-04-26_key-serp-features]] — describes three key SERP components (featured snippets, People Also Ask, knowledge panels) and their roles in directing user attention and behavior.
- [[2020-05-31_google-baidu-serp-comparison]] — comparative analysis of Google and Baidu SERP layouts and their distinct eyetracking patterns.
- [[2022-05-22_intranet-search]] — A critical employee tool in intranets that must be fast, accurate, and integrated; requires careful design and ongoing maintenance to meet user expectations shaped by Google.
- [[2022-08-21_enriched-site-search-suggestions]] — Search is a critical path to task completion and essential for conversions; text autocomplete suggestions are heavily used and effective, but enriched graphical suggestions add little value and often create usability problems if not implemented carefully.
- [[2025-03-04_367_Le_meilleur_outil_de_benchmark_gratuit_1000+_screenshots]]
- [[2025-07-01_384_Top_7_patterns_UX_pour_intégrer_l_IA_dans_vos_interfaces]]
- [[2025-09-09_394_Top_5_outils_IA_Product_Design_&_UXUI_-_Septembre_2025]]
