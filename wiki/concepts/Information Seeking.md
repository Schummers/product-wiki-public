---
type: concept
name: Information Seeking
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Information Seeking Behavior"
  - "Information-Seeking Behavior"
  - "Search Behavior"
---

# Information Seeking

## Definition

Information seeking is how people locate, evaluate and assemble the information
they need in order to decide or act. NN/g's replication of a 1997 Xerox PARC
study, based on 498 critical incidents and 471 search instances, splits it into
three behaviors: **Acquire** (finding a fact), **Compare/Choose** (evaluating
options) and **Understand** (learning about a topic)
[[2020-05-24_information-seeking-expectations]]. Over 22 years the mix shifted:
Understand grew from 24% to 40% of critical internet use while Compare/Choose
fell from 51% to 36%, critical use became predominantly mobile (42% on
smartphones), and 28% of respondents reported social interaction while deciding
[[2020-01-26_information-seeking-behavior-changes]]. Seeking is not always
deliberate: passive acquisition — accidental discovery while browsing, or being
notified — rose from 4% to 14% of the information behind significant decisions
[[2020-04-05_passive-information-acquisition]].

The behavior is shaped by the interfaces people use. As search-results pages
gained knowledge panels, snippets and interactive elements, scanning went from
linear to a nonlinear "pinball" path, and the first position's share of clicks
fell from 51% in 2006 to 28% [[2019-11-17_pinball-pattern-search-behavior]].
Users are satisficers rather than maximizers: they collect information until
confident enough, then stop [[2020-03-29_good-abandonment]]. Generative AI is now
part of the same picture, used alongside rather than instead of search
[[2025-08-15_ai-changing-search-behaviors]] [[2026-02-27_ai-search-infoseeking]],
and the underlying patterns hold across very different ecosystems
[[2026-05-01_information-seeking-china]].

## Practice

### Design for the task type, not for "search" in general

The three behaviors carry different expectations
[[2020-05-24_information-seeking-expectations]]:

- **Acquire** — users want speed, few clicks, a direct answer, plain language.
  Featured snippets and knowledge panels are especially valuable here. These
  incidents are also the least memorable (57% were reported within one week,
  against 33% for other types).
- **Compare/Choose** — users want comprehensive information from multiple
  perspectives, key information upfront, and comparison tools such as tables.
- **Understand** — users want organized, centralized content (bullets,
  subheadings, one page rather than several clicks) and ads only in expected
  locations.

Research tasks (Compare/Choose and Understand) get significantly more time on the
SERP before a click than Acquire tasks, and supporting them well matters
disproportionately because users form stronger impressions from
research-intensive experiences [[2020-05-24_information-seeking-expectations]].
Task type also changes scanning: simple fact-finding keeps attention on top
results, while complex research tasks push users lower, with 20% of selections
below the fold [[2019-11-17_pinball-pattern-search-behavior]]. Because Understand
activities now dominate, sites are advised to provide comprehensive educational
content rather than relying on appealing design
[[2020-01-26_information-seeking-behavior-changes]].

### Scanning patterns on results pages

Three patterns are documented. The **pinball pattern** — nonlinear bouncing
between results and SERP features, driven by visual weight — is the default on
complex SERPs; features received looks in 74% of cases, the 6th position gets
looks in 36% of cases, and users clicked past page one in only 2% of queries
[[2019-11-17_pinball-pattern-search-behavior]]. The **love-at-first-sight
pattern** — examining a single result and ignoring the rest — occurred in 20% of
377 search instances, up from 17% in 2006; it is enabled by trust in the search
engine's ranking (a cross-cultural "Google gullibility"), by SERP features that
make the top result easy to find, and by low motivation, time pressure, or a
navigational query [[2020-07-12_love-at-first-sight-pattern]]. **Sequential
linear scanning** still dominates where features are not relevant: on Baidu, the
pinball pattern appeared in 1 of 60+ searches
[[2020-05-31_google-baidu-serp-comparison]].

That comparison is the practical lesson: relevance, not prominence, drives
attention. Google's knowledge panels are looked at because they answer the
question; Baidu's right rail carries ads and unrelated searches, so users train
themselves into banner blindness. Promoting your own content on a results page is
fine as long as it serves the current task — and once users have learned to
ignore an area, winning them back requires consistently relevant content over
time [[2020-05-31_google-baidu-serp-comparison]]. Even unclicked, appearing in
results builds brand awareness and familiarity for future searches
[[2019-11-17_pinball-pattern-search-behavior]] [[2020-03-29_good-abandonment]].

### SERP features and good abandonment

Featured snippets, People Also Ask and knowledge panels act as signposts that let
users verify they are looking at the right entity, help them reformulate by
offering computer-generated alternatives instead of forcing them to invent new
queries, and carry very low interaction cost since they require no extra click or
page load; users even return to a knowledge panel after clicking, while the next
page loads [[2020-04-26_key-serp-features]]. Because users' mental models of
search are formed by the dominant engine in their country, internal site search
should adopt similar feature designs [[2020-04-26_key-serp-features]].

The consequence is **good abandonment**: the information need is fully satisfied
by the results page itself, with no click and no reformulation
[[2020-03-29_good-abandonment]]. Desktop searches ended without a click about 35%
of the time (up 9 points since 2016), rising to 62% on mobile. The source is
explicit about the trade-off: efficiency for simple factual needs, against
accuracy risks when a snippet extracts text out of context, and the near
impossibility of assessing credibility when an answer has been reformatted and
excerpted by the engine — it raises this as an ethical question about whether
designers are eroding critical thinking. For content creators it recommends
answering common questions well, claiming and optimizing knowledge panels, and
studying voice-search queries, which tend to be how/what-is questions that
snippets favour [[2020-03-29_good-abandonment]]. The love-at-first-sight article
gives the same advice from the other side: understand the user's question
precisely and structure content (lists, tables, definitions) so it can be
featured [[2020-07-12_love-at-first-sight-pattern]].

### The vocabulary problem: keyword foraging

Before the real search there is often a search for the right words. **Keyword
foraging** is the preliminary query users run to discover terminology when they
know what something looks like but not what it is called, need a solution but not
the tool's name, have forgotten a term, or know it in another language. It is
common in specialized domains — fashion, home improvement, car parts, skin care —
and search tools fail when users cannot supply the right terms. Remedies:
faceted navigation that exposes domain vocabulary ("dual-fuel range" as a filter
teaches the term), accepting imperfect query formulations, plain language in
content, avoiding invented branded terminology (or pairing it with the plain
term), and mining site-search logs for the gap between what users type and the
correct word [[2021-03-28_keyword-foraging]].

### Passive acquisition

When information arrives unbidden, the design requirements change
[[2020-04-05_passive-information-acquisition]]. Passive discovery splits into
*explore* (stumbling on something while browsing) and *notified* (email, text,
push). Compared with active seeking, people are roughly twice as likely to
interact socially, with sharing dominant (21% vs 2%); the content scope is
narrower (product info, news/politics and people account for 81%); paid content
supplies 37% of critical passive acquisitions against 1% for active; and use is
mobile and single-device (only 10% multi-device, vs 22% for active). Practical
implications: supply the missing context around a discovered item (links to
related content, comparison tables, expanded information), make sourcing
transparent and free of clickbait since credibility is hard to judge in this
mode, let users personalise notifications to cut the reported volume overload,
and give content strong information scent so it can be discovered at all.

### AI as an information-seeking tool

Six conversation types were identified across 425 interactions with generative-AI
bots, each mapping to a different seeking strategy: **search query** (one simple
prompt, users transferring their search-engine mental model without giving enough
context), **funneling** (vague prompts refined over several turns toward a need
that is specific but poorly articulated), **exploring** (depth: learning
terminology and building on the bot's answers), **chiseling** (breadth: many
related questions that do not build on each other), **pinpointing** (heavy upfront
specification, short exchange) and **expanding** (a too-narrow query relaxed after
poor results). There is no optimal conversation length; length is part of the
nature of exploring and chiseling [[2023-11-10_ai-conversation-types]].

AI's concrete value is in shortcuts around tedious research: overcoming keyword
foraging, closing information gaps, evaluating sources, sifting, synthesising and
storing [[2025-08-15_ai-changing-search-behaviors]]. Because it accepts wordy
natural-language descriptions, it helps most in the simple foraging case where
the user knows the goal but not the term
[[2025-08-22_ai-information-seeking-keyword-foraging]]. Users turn to AI when the
goal is vague, when several constraints must hold at once (budget, timeline,
location), and when information must be aggregated from many sources
[[2026-02-27_ai-search-infoseeking]].

The limits are equally documented. Habits are sticky — participants default to
Google out of long familiarity, and only a compelling shortcut shifts them
[[2025-08-15_ai-changing-search-behaviors]]. Articulation is a deeper barrier
than vocabulary: users often cannot explain a problem they do not understand, and
the recommendation is that systems ask clarifying questions rather than expect
users to be prompt engineers, since "the product should adapt to the user"
[[2025-08-22_ai-information-seeking-keyword-foraging]]. Discoverability is a
barrier too: users do not know what AI can do, and in the Google AI Mode study 4
of 7 participants had never noticed the feature, confused it with Gemini and AI
Overviews, bypassed its onboarding, and were overwhelmed by wordy unformatted
answers and by scrolling through long conversations — with the persistent tab bar
reflecting the first query rather than the latest follow-up
[[2025-10-17_google-ai-mode]]. Users also still type keyword phrases into AI
rather than natural language [[2025-10-17_google-ai-mode]], and low-fluency users
treat chatbots like search engines and give up quickly
[[2026-05-01_information-seeking-china]].

### AI and search are complementary, not substitutes

The sources agree that AI has not replaced search. All participants in
[[2025-08-15_ai-changing-search-behaviors]] kept using traditional search
alongside AI, to fact-check and explore other angles, even while AI overviews at
the top of results satisfied needs without a click and reduced traffic to content
sites. [[2026-02-27_ai-search-infoseeking]] describes users ping-ponging between
the two: AI for exploratory, multi-constraint, synthesis-heavy work; search for
verification, pricing, high-stakes decisions and authoritative sources in
regulated domains such as medicine and academic research. The same complementarity
appears in China, where users left Baidu for genAI and social platforms out of
frustration with promotional clutter, then validate genAI answers on social apps
like Rednote and Douyin by seeing real peer outcomes — information seeking
distributed across tools, with genAI for synthesis and social platforms for
real-world validation [[2026-05-01_information-seeking-china]]. That study also
finds prompt-fluency, trust and cross-validation patterns mirroring Western
research, and notes that trust in a parent brand transfers to its new AI
products.

## Sources (15)

- [[2019-11-17_pinball-pattern-search-behavior]] — documents how SERP complexity changes user scanning patterns from sequential to nonlinear, with implications for visibility.
- [[2020-01-26_information-seeking-behavior-changes]] — Shows that search and information gathering behaviors have changed dramatically, with understanding and learning becoming primary purposes of internet use.
- [[2020-03-29_good-abandonment]] — describes the evolution from traditional click-through behavior to good abandonment where answers from SERP features satisfy information needs.
- [[2020-04-05_passive-information-acquisition]] — documents the growing role of passive, unintended discovery in critical decision-making and how it differs fundamentally from active information seeking.
- [[2020-04-26_key-serp-features]] — explains how SERP features influence different stages of information seeking, from modifying queries to providing quick answers that end tasks on the SERP.
- [[2020-05-24_information-seeking-expectations]] — taxonomy of three distinct online information-seeking behaviors (Acquire, Compare/Choose, Understand) based on critical incident and search analysis research, including analysis of search patterns and query formulation differences across task types; Research tasks involve more reformulation and character count than other types.
- [[2020-05-31_google-baidu-serp-comparison]] — documents how SERP design (relevant vs. irrelevant content, sidebar prominence, feature positioning) shapes user gaze patterns and interaction.
- [[2020-07-12_love-at-first-sight-pattern]] — Users sometimes fixate on a single search result and ignore alternatives through satisficing, a user strategy shaped by context.
- [[2021-03-28_keyword-foraging]] — the article defines and analyzes keyword foraging as a specific user behavior pattern in search.
- [[2023-11-10_ai-conversation-types]] — the six conversation types directly correspond to different strategies users employ to find information, from simple searches to exploratory learning.
- [[2025-08-15_ai-changing-search-behaviors]] — The article documents how AI is changing information-seeking behaviors and strategies, with shifts in user search habits from keyword-based traditional search to natural-language AI chat.
- [[2025-08-22_ai-information-seeking-keyword-foraging]] — The article focuses on how AI impacts the broader information-seeking process beyond simple keyword lookup.
- [[2025-10-17_google-ai-mode]] — Documents information-seeking behavior shifts with AI: users expect AI to aggregate information, eliminate keyword-foraging problems, but users still rely on traditional keyword phrases instead of natural language.
- [[2026-02-27_ai-search-infoseeking]] — The article documents how users choose between AI and search based on their information need, the clarity of their goal, and the stakes involved.
- [[2026-05-01_information-seeking-china]] — Information seeking is increasingly distributed across multiple tools and platforms; users assemble information strategically from genAI for synthesis and social platforms for real-world validation.
