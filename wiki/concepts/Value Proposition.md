---
type: concept
name: Value Proposition
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "User Value Proposition"
---

# Value Proposition

## Definition

A value proposition is a clear promise to users of the specific value they will
receive and the goal they will accomplish by using a product
([[2025-07-04_powered-by-ai-is-not-a-value-proposition]]). Its function is
directive as much as communicative: it tells a product team which features
belong to the user journey it serves and gives it grounds to say no to
nice-to-have features outside that journey.

The sources agree that the proposition is stated in terms of what the user
achieves, never in terms of how the product is built. "Accelerate your
research" or "never miss a bill" are propositions; "easier to use" and "powered
by AI" are not, because a technology is not a user benefit
([[2025-07-04_powered-by-ai-is-not-a-value-proposition]]).
[[2018-02-12_solving-design-exercises_09-step-1-understand-your-goal-why]] adds a
second face to it: a solution is argued with both a customer benefit and a
business benefit, and the two are presented together.

A third source asks what "value" itself means, and answers through named
practitioners rather than in the author's own voice. In
[[2022-01-19_product-management-for-ux-people_04-chapter-1-what-exactly-does-a-product-manager-do]],
Christian Crumlish reports Jay Zaveri, his chief product officer at CloudOn and
later head of a product incubator at Social Capital, defining value as
"something special that a person or customer experiences that never existed in
the same way for them in the past": useful, usable and desirable, and apparent
when something is technologically differentiated, abundantly available, and
changes human behavior. Alongside it Crumlish borrows a much shorter test from
B. Pagels-Minor, then a product lead at LinkedIn: "Something the user values and
repeatedly uses."

## Practice

### Establish the value before choosing the technology

[[2025-07-04_powered-by-ai-is-not-a-value-proposition]] puts the sequence
plainly: decide what users need to achieve first, then select the tools —
including AI — that best enable it. Starting from the technology tends to
produce features that address no real problem. The same order appears in
[[2024-11-08_ai-user-value]], which treats "technology for its own sake" as the
recurring failure mode, from Flash plugins to LinkedIn's AI-powered questions
and Instagram's AI chat placed in search. That article also holds the opposite
case open: AI can serve a genuine pain point, as with Adobe Lightroom's
object-removal tool, which puts a previously difficult and time-consuming task
within reach of an average user.

### "Powered by AI" fails as a proposition, for several distinct reasons

- It shifts the work onto the user. The framing makes users wholly responsible
  for identifying opportunities to integrate the tool into their workflows
  ([[2025-07-04_powered-by-ai-is-not-a-value-proposition]]).
- It can repel rather than attract. Users and designers are aware of LLM
  limitations, so advertising AI presence may reduce the likelihood of
  conversion unless the specific anxieties are addressed
  ([[2025-07-04_powered-by-ai-is-not-a-value-proposition]]).
- It destroys focus. When "it has AI" is the proposition, the only remaining
  guiding principle is making the experience as AI as possible, which tends to
  end in broad-scope chatbots with high adoption barriers
  ([[2025-07-04_powered-by-ai-is-not-a-value-proposition]]).
- It does not create value by itself. Adding AI does not magically create
  value; teams must name the concrete gain — better accuracy, faster synthesis,
  a new capability — before implementing
  ([[2025-10-21_designing-ai-study-guide]]).

Both [[2025-07-04_powered-by-ai-is-not-a-value-proposition]] and
[[2025-10-21_designing-ai-study-guide]] tie the proposition to scope: successful
products start by doing one thing well, and narrowly scoped AI features are
easier to understand and see better adoption than broadly scoped ones.

### Lead with the benefit, not the specification

[[2024-11-08_ai-user-value]] is explicit that technical jargon and feature
descriptions do not compel users while benefit-focused language does: open with
how the feature improves the user's life, and leave specifications such as
token context windows for later. It also notes the cost of getting this wrong
at launch — a single bad experience with an AI feature can stop a user trying
them again.

### Check the proposition against why users are actually there

[[2026-03-20_site-ai-chatbot]] provides the evidence of misalignment. In a study
of 9 users across 8 site chatbots, participants often failed to notice the
feature, arrived sceptical from past poor chatbot experiences, and could not
articulate what it offered beyond the tools already on the page. Some chatbots
proposed capabilities such as recipes or DIY help that did not match the reason
people came to the site, which was to buy products; others were simply slower
and more effortful than the search, filters and navigation users had already
mastered. Where the chatbots did add value was context-specific: product-level
questions, clarification of complex information, and personalised multivariate
questions. The article's diagnosis is that the chatbots were added without
understanding which user problems they solve, and that vague messaging leaves
users unwilling to experiment to find out.

### The metrics are not the value (book)

Zaveri's warning, as
[[2022-01-19_product-management-for-ux-people_04-chapter-1-what-exactly-does-a-product-manager-do]]
records it, is aimed at the habit of reading value off a dashboard: "No true
value is created by just financial and growth metrics." It sits under Crumlish's
own definition of the product manager's job, which is responsibility for value
through the coordination and delivery of customer experiences, so that the
experience is valuable enough to be "hired" by the user and developed as a
sustainable concern, ideally in service of a broader vision. Sustaining that,
Crumlish adds, means finding repeatable cycles of inputs and outcomes, with the
people and money inputs at least steady, and taking for the organisation "a fair
share of the value created for the customer" — a position sitting beside, not
against, the business-benefit framing below. See [[Business Metrics]] and
[[Product Management]].

### State customer value and business value together

[[2018-02-12_solving-design-exercises_09-step-1-understand-your-goal-why]] treats
the proposition as the opening of a design presentation: why the product or
feature matters, what problem it solves, how it benefits customers, and what
business opportunity it creates. Both of the chapter's worked openings state the
two faces in one breath: the NYC MetroCard redesign pairs societal impact (less
pollution, better access to education and employment, healthier citizens) with
money saved for the city's economy, and the LinkedIn freelancer marketplace
pairs increased value to customers with another revenue stream for the company.
Two supporting moves are recommended: when improving an
existing product, start from the company's vision and mission and explain how
the improvement supports them; and describe the status quo and its problems
before proposing the solution, which makes the opportunity more compelling. The
same chapter advises pointing at existing assets the solution leverages — the
LinkedIn marketplace example rests on the company already having both
freelancers and businesses.

## Sources (6)

- [[2024-11-08_ai-user-value]] — Discusses how AI features must provide genuine value to users by solving real problems, not by being flashy or technological trendy.
- [[2025-07-04_powered-by-ai-is-not-a-value-proposition]] — a clear promise to users of the specific value they will receive and the user goal they will accomplish by using a product.
- [[2025-10-21_designing-ai-study-guide]] — Challenges "Powered By AI" marketing; requires teams to articulate concrete value before implementing (improved accuracy, faster synthesis, new capabilities that solve actual pain points).
- [[2026-03-20_site-ai-chatbot]] — Emphasizes the importance of aligning chatbot capabilities with actual user problems on the site.
- [[2018-02-12_solving-design-exercises_09-step-1-understand-your-goal-why]] — the chapter frames the opening of a presentation as a customer benefit and a business opportunity stated together: the MetroCard example pairs societal impact (less pollution, better access to education and employment) with money saved for the city, the LinkedIn example pairs increased value to customers with another revenue stream for the company
- [[2022-01-19_product-management-for-ux-people_04-chapter-1-what-exactly-does-a-product-manager-do]] — Jay Zaveri's definition of value is quoted at length (special, previously non-existent for that person, useful, usable and desirable, technologically differentiated, abundantly available, behavior-changing) along with his warning that financial and growth metrics are necessary but not sufficient, and B. Pagels-Minor's shorter test, "Something the user values and repeatedly uses."
