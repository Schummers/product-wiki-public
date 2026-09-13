---
type: concept
name: Research Methods
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Research Methodology"
  - "UX Research Methods"
  - "User Research Methods"
---

# Research Methods

## Definition

Research methods are the systematic approaches UX and product teams use to
gather and analyse data about users: what they say, what they do, and why. The
sources treat "method" less as a catalogue of techniques than as a matching
problem. The research question comes first, and the method follows from it
([[2019-06-09_why-user-interviews-fail]], [[2018-04-22_quantitative-user-research-methods]],
[[2024-02-23_should-you-run-a-survey]]). Two framing dimensions recur across the
corpus: attitudinal versus behavioural (what people say versus what they do) and
qualitative versus quantitative (why and how to fix versus how many and how
much), with a third dimension, context of use, ranging from natural to
decontextualised ([[2022-07-17_which-ux-research-methods]],
[[2022-08-21_guide-ux-research-methods]], [[2024-03-01_attitudinal-behavioral]]).
Methods also map onto phases of work — generative methods for strategy,
formative methods for design, summative methods for launch and assessment — or
onto the Discover / Explore / Test / Listen cycle
([[2017-02-12_ux-research-cheat-sheet]], [[2023-11-24_surveys-design-cycle]]).

No single method answers everything. Every method has structural limits:
qualitative work lacks statistical proof, quantitative work lacks context and
meaning, self-report is filtered by memory and social desirability, observation
is altered by the observer's presence
([[2021-02-21_triangulation-better-research-results-using-multiple-ux-methods]],
[[2023-02-26_10-survey-challenges]], [[2023-05-21_hawthorne-effect-observer-bias-user-research]]).
The sources therefore treat method choice, study design, participant selection,
moderation and analysis as one continuous chain in which validity can be lost at
any link — and repeatedly argue that combining methods is what makes findings
trustworthy. They also insist that research is a learning activity rather than a
validation ritual: a study framed to confirm a decision is worth less than no
study at all ([[2017-09-10_no-validate-in-ux]], [[2025-08-08_research-yes-or-no]],
[[2022-03-13_confirmation-bias-ux]]).

The field's toolkit did not appear all at once. Methods for measuring and
improving performance trace back to early-twentieth-century industrial
engineering — Frank Gilbreth's motion studies of bricklayers and factory
workers, and human factors engineering's turn toward everyday life, such as
the kitchen's Golden Triangle — and carried into digital work through GOMS
(Goals, Operators, Methods, Selection rules) and Keystroke-Level Modeling,
which apply the same systematic measurement to task performance and micro
interactions ([[2016-11-04_ux-research_02-chapter-1-the-history-of-research]]).

## Practice

### Choosing a method

- Start from the research question, then consider budget, timeline, expertise
  and minimum sample size ([[2018-04-22_quantitative-user-research-methods]],
  [[2022-07-17_which-ux-research-methods]]). Practitioners in practice pick from
  a narrow set they already know, and the frameworks exist to widen that set
  ([[2022-07-17_which-ux-research-methods]], [[2018-09-02_quant-research-practice]]).
- **The project triangle**: [[2016-11-04_ux-research_06-chapter-5-choosing-your-methods]]
  resolves method choice through the same questions as above plus location
  (qualitative work favours travelling to participants; global products may
  make that cost-prohibitive) and a time/budget/scope trade-off — identify
  which two constraints matter most and let the third vary. Site analytics
  can run "set-and-forget" at low retroactive cost, while a contextual
  inquiry needs 90-120 minutes of dedicated researcher time per session. The
  best combinations pair a qualitative and a quantitative measure aimed at
  the same root question rather than forcing one method to cover unrelated
  goals; when the questions are genuinely distinct, the chapter recommends
  separate research tracks instead. Its closing framing: "research is a
  muscle" that gets stronger with practice, so once the methods are
  understood, adapting them to a specific project is expected rather than a
  deviation.
- Behavioural evidence is generally more reliable than attitudinal evidence
  about actual use; attitudinal methods still matter for beliefs, sentiment and
  satisfaction ([[2022-07-17_which-ux-research-methods]],
  [[2024-03-01_attitudinal-behavioral]]). Mismatches between what users say and
  what they do are themselves findings ([[2024-03-01_attitudinal-behavioral]]).
- Interviews cannot answer behavioural questions such as preference or purchase
  intent; use observation or usability testing instead
  ([[2019-06-09_why-user-interviews-fail]]). Surveys are the only quantitative
  attitudinal method, which makes them ideal for "what percentage of users feel
  X" and unsuitable for everything else ([[2024-02-23_should-you-run-a-survey]]).
- If one activity only is affordable, [[2017-02-12_ux-research-cheat-sheet]]
  recommends qualitative think-aloud usability testing of the existing system as
  the highest-impact single method, and research at every stage as the ideal.
- Do secondary research before primary research: internal past studies, journey
  maps, support and search logs, plus external peer-reviewed literature and
  datasets. It is cheap, reveals what is already known, and sharpens the problem
  statement — but is not a substitute for primary work
  ([[2022-02-20_secondary-research-in-ux]]).
- Discovery pays off: 83% of projects with a discovery phase report success
  versus 52% without, yet 58% of discoveries last two weeks or less
  ([[2020-05-17_discoveries-in-industry-revealed]]). The common excuses for
  skipping research (too slow, too expensive, users don't know what they want)
  are rebutted in [[2025-08-22_why-organizations-dont-do-user-research]], which
  locates the real barrier in incentives that reward shipping over value.
- When user behaviour shifts fast, the need for research rises rather than
  falls: research is risk reduction, and the pandemic-scale changes of 2020 —
  behavioural, psychological, regional, and in how user groups divide — could
  only be read through fresh study of one's own users. Qualitative interviews
  and surveys are what uncover the new behaviours, remote research is the safest
  and most practical format and reaches quality similar to in-person work when
  planned carefully in advance, and whether a change fades or becomes permanent
  can only be answered by continuing to research over months and years
  ([[2020-08-30_covid-changed-users]]).

### Generative and contextual methods

- **Interviews** are generative: they surface thoughts, beliefs, mental models
  and experiences ([[2019-06-09_why-user-interviews-fail]]). They are the
  dominant method in practice — 86% of journey-mapping teams use them for
  external research ([[2023-01-08_journey-mapping-how]]) — and among the most
  common discovery activities at 62%, with stakeholder interviews at 60%
  ([[2020-05-17_discoveries-in-industry-revealed]]).
- **Semistructured interviews need a guide**, not a script: start from research
  questions, broaden closed questions into "tell me about…" prompts, prepare
  probes, order questions to build rapport, and pilot with one or two
  participants ([[2021-02-28_interview-guide]]).
- **Field studies** observe users in their natural environment and expose
  workarounds, workflow mismatches, multiple information sources and
  environmental constraints that labs and surveys cannot show
  ([[2018-07-08_field-studies-intranet-redesign]], [[2024-01-12_field-studies]]).
  [[2024-01-12_field-studies]] distinguishes four types along an involvement
  scale: direct observation, contextual inquiry, customer-site visits, and
  ethnography; they are most valuable in discovery, with remote moderated or lab
  research as cost-effective substitutes when travel or ethics forbid them.
- **Contextual inquiry** combines observation with in-the-moment questioning on
  an apprenticeship model, grounded in four principles (context, partnership,
  interpretation, focus) and a four-part session (primer, transition, contextual
  interview, wrapup). It reveals habitual, invisible behaviour but is overkill
  for simple interfaces such as an ecommerce page ([[2020-12-06_contextual-inquiry]]).
- **Diary studies** collect self-reported data over days to months, remotely and
  asynchronously, which suits long-term experiences, habit change and
  cross-channel journeys ([[2024-03-29_diary-studies]]). Entries may be
  event-based, interval-based or signal-based; sample to saturation (roughly
  5–50); expect dropouts. The entry is the unit of data, and its template shape
  drives both data quality and participant effort: closed entries (rating
  scales, checkboxes) track adoption, frequency and satisfaction cheaply but
  cannot reach the *why*; open-ended entries surface unexpected insight at a
  higher cost to participant and analyst alike; multimedia entries capture
  visual context text cannot, at the price of technical complexity. Design
  against three constraints — participant effort, analysis effort, research
  goals — and when they conflict, participant effort wins, since high-effort
  entries produce skipped questions, rushed answers and dropout. Keep an entry
  to 5–10 minutes (beyond 15 the abandonment risk rises sharply), pair closed
  questions with short open follow-ups, and mark high-effort questions optional
  so irrelevant prompts can be skipped ([[2025-11-28_diary-study-entries]]);
  good studies balance the three types rather than maximising free text
  ([[2026-01-02_ux-quiz]]).
  Diary studies remain underused in journey mapping (12% external, 6% internal)
  despite fitting journeys that unfold over time ([[2023-01-08_journey-mapping-how]]).
- **Critical Incident Technique** asks participants to recall specific
  consequential events. Introduced by Flanagan in 1954, usable through
  interviews, focus groups or surveys, it surfaces rare and significant events
  across long time spans, but depends on fallible memory and skews toward
  extremes rather than typical use ([[2020-01-26_critical-incident-technique]]).
- **Qualitative surveys** with open-ended questions are a cheap way to discover
  which answer categories a later quantitative survey should offer, instead of
  writing closed questions from conference-room assumptions
  ([[2016-09-25_qualitative-surveys]]).

### Usability testing

- Core elements are the facilitator, the tasks and the participants; think-aloud
  is the standard protocol; the format axes are qualitative/quantitative,
  remote/in-person and moderated/unmoderated ([[2019-12-01_usability-testing-101]]).
  Costs span discount studies (three days, five users, a few hundred dollars in
  incentives) to elaborate multi-group international studies.
- **Moderated remote** testing is presented as the middle ground: near in-person
  quality with unmoderated-like cost, allowing follow-ups, task reordering,
  think-aloud coaching and hour-long sessions, with the team observing live
  ([[2020-04-12_moderated-remote-usability-test-why]]).
- **Unmoderated** testing scales to dozens or hundreds of participants within
  hours, but is poor for early prototypes and for tasks needing imagination or
  emotion; instructions must be exceptionally clear since nobody can clarify
  them, and piloting is essential ([[2019-10-27_unmoderated-usability-testing]]).
  Tooling is mature: eleven reviewed platforms all record screen and voice,
  auto-transcribe and offer panels, differing on pricing model and extras
  ([[2024-12-06_unmoderated-user-testing-tools]]).
- The sources disagree on how much unmoderated testing actually saves.
  [[2019-10-27_unmoderated-usability-testing]] and
  [[2020-04-12_moderated-remote-usability-test-why]] treat it as the quick, cheap
  option; [[2020-07-26_remote-usability-testing-costs]] measures only 20–40%
  savings for a five-participant study once overrecruiting for cheaters and the
  hidden analysis time of watching recordings are counted, and notes sessions cap
  out around 20 minutes versus 60 moderated.
- **Content-heavy sites** need moderated sessions (unmoderated participants rush
  and skip), a facilitator who has studied the domain, open-ended
  information-seeking tasks, tasks tailored per participant, and tolerance for
  long silent reading ([[2021-02-07_testing-content-websites]]).
- **Testing with minors** requires parental consent, segmentation by maturity
  rather than age alone, shorter sessions (60 minutes for 3–12, 90 for teens),
  more and more varied tasks, age-appropriate incentives, overrecruiting for
  no-shows, and a warm, praising facilitation style
  ([[2019-04-28_usability-testing-minors]]).
- **Scope the test realistically.** Sending users straight to the target page
  strips out navigation, which is itself part of feature usability — 36% of task
  failures in one embedded-calculator study happened during navigation. When
  pre-positioning is unavoidable, use neutrally-renamed bookmarks rather than
  long URLs or search ([[2016-03-06_feature-user-test]]).
- A 10-step moderation checklist runs from welcome to compensation: avoid the
  word "test", build rapport, take informed consent, set expectations that you
  will not help, ask broad follow-ups before specific ones, reserve the last five
  minutes for observers ([[2022-05-29_usability-checklist]]).
- Defending small qualitative samples to sceptics: explain the methodology
  before the study rather than after, have stakeholders observe sessions, recruit
  demonstrably representative participants, don't discount single-user findings,
  and corroborate with analytics, support tickets and published usability theory
  ([[2019-02-24_responding-skepticism-small-usability-tests]]).

### Inspection, comparison and simulation methods

- **Heuristic evaluation** inspects a design against established guidelines
  without users; three to five independent evaluators consolidating afterwards
  outperform a single one; Nielsen's 10 heuristics are the recommended starting
  point. A violation is not automatically a problem, and the method complements
  rather than replaces user research — useful to prepare a team for testing or
  stretch a thin budget ([[2023-06-25_how-to-conduct-a-heuristic-evaluation]]).
- **Competitive evaluations** run either as expert reviews or as usability tests
  where participants complete tasks on 2–3 competing products (2–4 competitors
  typically chosen). Alternate order and site pairs to avoid learnability
  effects; the aim is to improve your own design, not to crown a winner
  ([[2024-01-05_competitive-usability-evaluations]]).
- **Wizard of Oz** lets participants interact with an interface secretly driven
  by a human, so complex technology (conversational UI, recommendation engines,
  real-time lookup) can be tested before it is built. Wizard responses can be
  closed, open or hybrid; document the protocol and pilot it
  ([[2024-04-19_wizard-of-oz]]).
- **Card sorting** exposes mental models, and **tree testing** measures
  findability — used together in one B2B case they gave a 4/10 baseline rising
  to 7.4/10 after redesign ([[2021-01-31_quantifying-case-study]]). Card sorts
  are vulnerable to keyword matching, where participants group by shared words
  rather than meaning; counter it with synonyms, non-parallel phrasings, fuller
  descriptions, think-aloud and iterative regrouping
  ([[2024-06-14_card-sorting-terminology-matches]]).

### Quantitative methods and measurement

- Nine quantitative methods are catalogued in
  [[2018-04-22_quantitative-user-research-methods]]: quantitative usability
  testing, web analytics, A/B testing, card sorting, tree testing, surveys,
  clustering of qualitative data, desirability studies and eyetracking, spread
  across very different cost and difficulty levels. Quant work typically needs
  20–30 participants minimum for statistical significance, against five for
  qualitative discovery ([[2018-04-22_quantitative-user-research-methods]],
  [[2018-02-11_measuring-perceived-usability]]).
- **A/B versus multivariate testing**: A/B compares whole designs and suits
  radical redesigns; MVT tests combinations of element variants and measures
  their interactions, but the number of variations multiplies fast and demands
  much more traffic, so it fits incremental refinement of an already-validated
  design ([[2018-04-08_multivariate-testing]]).
- **Perceived usability** has standard instruments: SUS as a 10-question
  post-test score out of 100 (mean 68 across 500 studies; 80+ is the top decile),
  SEQ as a 7-point post-task question less exposed to the peak-end effect, and
  NASA-TLX for workload in high-consequence domains. Standard questionnaires beat
  custom ones because their validity and reliability are established, and they
  should sit alongside objective performance data
  ([[2018-02-11_measuring-perceived-usability]]).
- **Benchmarking** is a programme, not a one-off: choose 2–4 metrics against 5–10
  top tasks (HEART is cited as a frame), pick a methodology, pilot, take a
  baseline, redesign, allow users 2–5 weeks to adapt, re-measure, interpret
  statistically, and connect to business KPIs ([[2020-09-13_product-ux-benchmarks]]).
  Comparability depends on absolute consistency: document protocol, task wording,
  screener and metric definitions minutely, keep tasks stable, and archive raw
  data rather than summaries ([[2023-05-07_ux-benchmarking-repository]]).
- **Significance is two-dimensional.** A statistically significant difference can
  be practically trivial (a 0.03% change in a huge dataset), while a small sample
  with a large consistent pattern (10 of 12 failing versus 1 of 12) can be
  practically meaningful without p-values. Ask whether users would notice,
  whether it supports business outcomes, and what the effect size says
  ([[2026-03-06_practical-significance]]).
- **The Pareto principle** helps filter analytics overload toward the vital few
  areas worth deeper qualitative investigation, visualised with a Pareto chart —
  while warning against overoptimising the top 20% and ignoring the rest
  ([[2021-10-17_pareto-principle]]).
- In practice, 71% of surveyed UX professionals do quantitative research at least
  occasionally; analytics is the most common method (often collected without
  being used), recruiting large samples is the top obstacle at 37%, and only 24%
  judge success on both quantitative and qualitative data
  ([[2018-09-02_quant-research-practice]]).

### Surveys

- Surveys measure attitudes and perceptions, never behaviour; observational
  methods are required for what people actually do
  ([[2023-02-26_10-survey-challenges]], [[2024-02-23_should-you-run-a-survey]]).
- Three myths to discard: that surveys are easy, that a big sample rescues bad
  methodology, and that surveys are gentler on customers than interviews
  ([[2024-02-23_should-you-run-a-survey]]).
- Ten recurring biases are catalogued in [[2023-02-26_10-survey-challenges]] —
  recall, recency, social desirability, prestige, acquiescence, order effects,
  mood, central tendency, demand characteristics and random response — with
  mitigations: field the survey soon after the experience, assure anonymity, ask
  indirectly, offer ranges rather than exact numbers, and think about question
  order. Indirect questioning is also the main observer-bias defence in surveys
  ([[2023-05-21_hawthorne-effect-observer-bias-user-research]]).
- Craft rules from [[2016-09-25_qualitative-surveys]]: pilot at least four
  think-aloud rounds with real target users, keep it short (twenty questions is
  too many), label "(Required)"/"(Optional)" after each question rather than
  relying on asterisks, use conditional logic, randomise question and answer
  order, and front-load what matters.
- Survey type should follow the phase: discovery and diary-study surveys in
  Discover; competitor and statistical-persona surveys in Explore; SEQ and SUS in
  Test; NPS, CSAT, CES and intercept surveys in Listen — with the caveat that NPS
  alone is never an adequate usability metric ([[2023-11-24_surveys-design-cycle]]).

### Participants: recruiting, screening, sampling

- Participant selection is where validity is most often lost. Employees carry
  prior knowledge, higher motivation and fear of disappointing the team; Yahoo!
  data cited in [[2016-09-04_employees-user-test]] shows employees rated their own
  site 2% higher than outsiders did while outsiders rated competitors 15% higher.
  Employees are legitimate only for intranets, pilot tests, or as a skunkworks
  demonstration of UX value.
- Recruiting is an eight-step process: define eligibility on goals as well as
  demographics, build a screener that does not telegraph intent, choose among
  professional recruiters, automated platforms, internal panels, online forums
  and intercepts, review near-misses, and screen for diversity of gender, age,
  ethnicity, ability and digital skill ([[2021-11-07_recruiting-screening-research-candidates]]).
- Screeners protect data quality, save money and counteract volunteer panels
  skewed toward web-savvy professionals. Ask about past behaviour rather than
  hypothetical future behaviour, avoid gameable yes/no questions, and pilot the
  screener ([[2024-11-01_screening-participants]]).
- **Foils** — deliberately false but plausible answer options — catch inattentive
  or dishonest respondents. Foil answer options work better than whole foil
  questions; keep them plausible, topically relevant and rare (one or two per
  screener), and pair them with open-ended knowledge questions and consistency
  checks ([[2025-10-10_screener-foils]]).
- Define segments before recruiting, or an unfiltered pool silently collapses
  into one segment (nine commuters and one tourist); segment on behaviour,
  frequency of use and goals rather than demographics
  ([[2019-05-12_everyone-as-users]]).
- **Sampling**: convenience sampling is the justified default for qualitative and
  exploratory work, since the goal is finding problems rather than generalising;
  quotas do not make a convenience sample random. Probability sampling needs a
  complete population list and larger samples (40+ for quantitative usability
  testing, 100+ for surveys) and is reserved for high-stakes, population-level
  claims ([[2025-04-18_convenience-vs-probability-sampling]]).
- **Hard-to-reach participants**: for high-income users, warm referrals beat
  recruitment services, avoid asking about income directly, offer remote sessions
  and flexible evening/weekend scheduling, minimise presession paperwork, and
  raise incentives or offer charitable donations
  ([[2022-05-01_high-income-participants]]).
- When users join workshops (discovery, empathy, design, prioritisation,
  critique), recruit from previous research participants who are known to be
  articulate, brief them on the difference between needs and solutions, schedule
  critical discussion after they leave, and fall back on researchers or
  support/sales staff as proxies when real users are not feasible
  ([[2023-06-11_including-users-workshops]]).

### Moderation and facilitation

- Five facilitation mistakes to avoid in interviews: skimping on rapport,
  failing to probe, taking notes or multitasking during the session, letting
  observers into the room, and leading or priming. Record and transcribe rather
  than take live notes, keep a generic probe bank, cap the room at three people
  and keep the study purpose vague ([[2021-06-06_interview-facilitation-mistakes]]).
- **The funnel technique** — broad open questions and exploratory tasks first,
  narrowing to specifics afterwards — is presented as a foundational principle
  across interviews, usability tests and multimethod studies: prepare 5–8 broad
  main questions, give exploratory tasks before directed ones, and use stepped
  tasks to add specificity only when needed
  ([[2022-07-24_the-funnel-technique-in-qualitative-user-research]]).
- **Intentional silence** is a moderation tool: count to seven before speaking;
  the first four seconds feel awkward and the next three produce genuine
  thinking. Tolerance is cultural (English speakers ~4 seconds, Japanese 8.2)
  ([[2019-05-05_intentional-silence-ux]]).
- **Field sessions** fail in predictable ways: over-long sessions (keep under two
  hours), drifting into complaint collection, becoming group sessions, skewed
  host-guest dynamics in homes, and abstract "we usually…" descriptions — ask
  "how did you do this today?" instead
  ([[2022-10-09_why-field-study-sessions-go-wrong]]). Field research also demands
  close monitoring of recruiting against professional volunteers, careful
  observer management, immediate documentation and debriefs, and willingness to
  adapt the protocol as insights emerge ([[2023-02-19_tips-user-research-field]]).
- **Observers** need explicit rules: audio is recording, no talking or laughing,
  pass notes instead of speaking, write questions down for the facilitator, one
  observation per note with scenario letter and initials, and never answer,
  correct or converse with the participant ([[2016-10-30_observer-guidelines]]).

### Validity, bias and study design

- Validity has two faces: **internal** (the design does not push participants
  toward particular responses) and **external** (participants and setup represent
  reality), both distinct from reliability. Randomise and counterbalance task and
  condition order, control facilitator style, use representative rather than
  proxy participants, and replicate real conditions; when validity must be traded
  away, interpret results as best-case laboratory findings needing field
  retesting ([[2021-02-14_internal-vs-external-validity]]).
- **Confounding variables** — time of day, age, seasonality, prior product
  experience, protocol changes — can invalidate conclusions. Counterbalance
  within-subjects order, measure suspected confounds so they can be controlled
  statistically, or switch to qualitative exploration if control is impossible
  ([[2023-09-24_confounding-variables-quantitative-ux]]).
- **Observer bias / Hawthorne effect** touches every method: build rapport and a
  judgment-free atmosphere in field studies, use familiar realistic scenarios and
  state that the design is being tested rather than the user, question indirectly
  in surveys, and keep diary participants engaged by explaining why their entries
  matter ([[2023-05-21_hawthorne-effect-observer-bias-user-research]]).
- **Confirmation bias** grows with emotional investment in the design. Counter it
  with a research rather than validation mindset, early empirical data,
  nonleading questions, multiple data sources, and fresh eyes from uninvolved
  colleagues ([[2022-03-13_confirmation-bias-ux]]).
- **Language shapes the study.** [[2017-09-10_no-validate-in-ux]] argues against
  the word "validate", which primes participants to withhold criticism and teams
  to explain problems away; prefer "test", "examine", "study". Finding nothing
  wrong indicates a methodology problem, not a perfect design.
  [[2025-08-08_research-yes-or-no]] extends this to binary yes/no questions,
  which produce speculation rather than data and flatten even behavioural results
  into pass/fail.
- **Task writing depends on the methodology.** Quantitative tasks need one
  interpretation, one success criterion, enough specificity that all participants
  do the same thing, and dummy data for logins; qualitative tasks may be
  open-ended and may change mid-study when understanding improves. Both must be
  realistic, drawn from interviews, search logs, analytics and support calls,
  avoid priming with exact UI labels, stay emotionally neutral, and be pilot
  tested with one or two users ([[2018-01-21_test-tasks-quant-qualitative]]).

### Analysis and synthesis

- Distinguish data (raw observations, meaningless alone), findings (patterns
  without explanation) and insights (patterns tied to user needs and business
  opportunity, and therefore actionable); context is what converts findings into
  insights ([[2023-04-23_data-findings-insights-differences]]).
- A four-step analysis loop for qualitative usability data: collect relevant data
  points, assess each for accuracy, explain through synthesis, then check the
  explanation against the full dataset — cycling between the last two, because
  first explanations are biased toward memorable moments
  ([[2025-05-02_analyze-usability-data]]).
- Unanalysed interviews lose their insights to bias; record, transcribe and
  analyse as a team with highlighted transcripts and thematic clustering
  ([[2019-06-09_why-user-interviews-fail]]).
- **Note-taking formats** trade off: chronological digital logs when sequence,
  timing or remote observers matter; one-incident-per-sticky topical notes,
  colour-coded by participant, for fast post-session sorting; a whiteboard
  top-findings debrief after each session. Capture individually first, combine
  afterwards, to avoid groupthink; 4–10 observers is practical and each
  stakeholder should see at least two sessions ([[2017-04-30_group-notetaking]]).
- **Diverge then converge**: have team members analyse independently before
  discussing, with ground rules (quiet time, no "no" or "but", optional
  anonymity) to prevent dominant voices — applicable to research analysis,
  affinity diagramming and synthesis workshops ([[2024-05-30_diverge-converge]]).
- Contradictions between methods are information, not noise. Before dismissing
  either result, interrogate participant selection, tasks and exposure,
  logistics, and analysis; consider that perceived usability differs from
  objective usability and that people resist change regardless of benefit; and
  run learnability studies tracking both performance and satisfaction over time
  ([[2019-01-27_interpreting-research-findings]]).

### Combining methods

- **Triangulation** — using multiple sources or methods on the same question —
  compensates for each method's structural limits and raises credibility. Scale
  the investment to the stakes: a few hours checking existing data for a small
  reversible decision, robust mixed-method work for expensive, hard-to-reverse
  ones ([[2021-02-21_triangulation-better-research-results-using-multiple-ux-methods]]).
  It is also a bias control, since multiple sources are harder to twist toward a
  hypothesis ([[2022-03-13_confirmation-bias-ux]],
  [[2023-04-23_data-findings-insights-differences]]).
- Concrete pairings recurring in the corpus: quantitative usability testing or
  analytics with surveys for benchmarking ([[2020-09-13_product-ux-benchmarks]]);
  usability testing and card sorting with tree testing
  ([[2021-01-31_quantifying-case-study]]); qualitative interviews with
  large-scale surveys for personas ([[2020-06-21_persona-types]]); surveys with
  qualitative research for stakeholder-convincing evidence
  ([[2024-02-23_should-you-run-a-survey]]); quantitative patterns pointing to
  where qualitative depth is worth spending ([[2021-10-17_pareto-principle]]).
  A/B testing shows which variant wins but not why, so it cannot replace
  qualitative work ([[2025-08-22_why-organizations-dont-do-user-research]]).
- **Personas** come in three research grades: proto personas from existing team
  knowledge (fast, risky), qualitative personas from 5–30 interviews (the
  recommended sweet spot, but silent on population proportions), and statistical
  personas from 100+ respondents and clustering (population-level but expensive
  and often not substantially different). None should rest on demographics alone
  ([[2020-06-21_persona-types]]). Personas, alongside object-oriented UX,
  still figured among the foundational tools for structuring user understanding
  and design decisions in NN/g's most-watched videos of 2025
  ([[2025-12-19_top-videos-2025]]).
- **Journey mapping** is research-hungry. Maps must be built on truth rather than
  assumption ([[2016-07-31_customer-journey-mapping]]), combining internal data
  mining and stakeholder interviews with interviews, field studies, diary studies
  and competitive analysis, plus quantitative data for magnitude
  ([[2017-05-28_customer-journey-mapping-process]], [[2019-02-10_research-journey-mapping]]).
  Six to eight participants are enough to start
  ([[2017-05-28_customer-journey-mapping-process]]).
- **Alternating methods as understanding matures.** Research data goes stale,
  and a topic a team felt was "fully understood" may need revisiting from a
  different angle: if only qualitative methods were used before, adding
  quantitative ones gives a new point of view, and vice versa
  ([[2016-11-04_ux-research_16-chapter-15-getting-the-most-out-of-research]]).
  In his interview sidebar in that chapter, Ofer Deshe (CEO, Tobias & Tobias)
  makes a stronger claim for one side of that pair: deep understanding of
  customers' cognitive, emotional and behavioural characteristics cannot come
  from analytics and market research alone, and structured observations,
  ethnographic studies, and methods rooted in sociology and psychology are
  what he relies on personally to surface unmet needs
  ([[2016-11-04_ux-research_16-chapter-15-getting-the-most-out-of-research]]).
- The corpus disagrees on assumption-first mapping.
  [[2020-06-14_journey-mapping-approaches]] presents it as the faster, cheaper
  route when time or budget is short, recommending a hybrid (assumption map,
  then research validation, then future state), and
  [[2023-01-08_journey-mapping-how]] reports 62% of teams working that way. But
  [[2022-12-18_journey-map-how-much-time]] measured that hypothesis-first teams
  spend as much or more total time than research-first teams — external research
  and internal data collection already account for over half of the mean 73.8
  hours — so the expected saving does not appear in the data.

### Research operations and tooling

- **ResearchOps** is the orchestration of people, process and craft so research
  scales without proportional cost, across six interlocking areas: participants,
  governance, knowledge, tools, competency and advocacy. Standardised methods,
  scripts, templates and consent forms save planning time; governance covers
  GDPR-compliant consent and PII disposal; a shared insight repository prevents
  repeat studies ([[2020-08-16_research-ops-101]]).
- Ready-made templates exist for research plans, consent forms, interview guides,
  usability procedures, journey maps, empathy maps and cognitive walkthroughs
  ([[2024-09-13_free-ux-templates]]).
- Tools are not neutral. Research platforms often lack features needed for proper
  quantitative testing (task randomisation, multiple success URLs), push
  transcript-based analysis that misses silent behaviour and errors, and blur
  interviews with usability tests through templates — while their guides and
  certifications teach whatever practice their commercial incentives favour
  ([[2026-03-13_research-tool-problems]]).

### AI in research

- **As an assistant**: decompose a research plan into parts rather than asking
  for the whole thing, supply organisational and product context, generate 10+
  research questions and filter them offline, then ask which methods fit which
  questions and why — noting that generative AI over-suggests triangulation and
  behavioural methods where attitudinal ones would do
  ([[2024-04-05_plan-research-ai]]). For surveys, GenAI drafts multi-dimensional,
  neutrally worded, logically grouped questions well, but underestimates
  respondent burden, produces unbalanced scales and missing "Other" options,
  overlooks semantic differential and rank-order formats, and writes leading
  tasks for AI-moderated studies ([[2026-04-03_ai-survey-writing]]).
- **As an analyst**: four tested AI analysis tools could not process video, had no
  access to study goals or participant background, produced vague
  recommendations, failed to cite sessions or timestamps, and were unreliable in
  operation; their bias-free claims are unfounded
  ([[2023-07-02_ai-powered-tools-limitations]]).
- **As a participant**: [[2024-06-21_synthetic-users]] argues synthetic users
  cannot replace real ones — they are sycophantic, idealised, one-dimensional and
  produce unprioritised need lists — and should be confined to desk research and
  hypothesis generation. [[2025-08-15_ai-simulations-studies]] reports a more
  favourable picture from three academic studies: interview-based digital twins
  reach 80%+ accuracy on survey tasks and r=0.98 on population-level effect sizes
  with markedly lower demographic bias, while demographic-only synthetic users
  capture direction but underestimate magnitude and variability. Digital twins
  simulate specific individuals from rich personal data; synthetic users simulate
  segments from group-level descriptors ([[2026-01-02_ux-quiz]]).
- The open agenda: [[2025-06-20_genai-ux-research-agenda]] flags AI-supported
  secondary research, ideation, facilitation, extraction, analysis and
  visualisation as lower-risk applications, and automated heuristic review and
  synthetic participants as areas needing benchmarking against expert and human
  baselines — warning that cheaper research without validation produces expensive
  wrong decisions.

## Sources (98)

- [[2016-03-06_feature-user-test]] — controlling variables and scope in user research.
- [[2016-07-31_customer-journey-mapping]] — Journey mapping relies on qualitative research methods like field studies, contextual inquiry, and diary studies to ground maps in truth.
- [[2016-09-04_employees-user-test]] — Documents how participant selection directly impacts data validity and how systematic biases from employee testing compromise ability to represent actual user needs.
- [[2016-09-25_qualitative-surveys]] — Illustrates qualitative survey as a cost-effective method for generating rich feedback, discovering answer categories, and informing later quantitative surveys.
- [[2016-10-30_observer-guidelines]] — Structured, careful observation practices maintain the rigor and validity required for reliable usability research findings.
- [[2017-02-12_ux-research-cheat-sheet]] — it catalogs methods (field studies, interviews, surveys, testing, analytics) and recommends frequency of use.
- [[2017-04-30_group-notetaking]] — Presents chronological logs, topical notes, and whiteboard debriefing as complementary data-capture techniques with different strengths and tradeoffs.
- [[2017-05-28_customer-journey-mapping-process]] — Combines internal data mining, stakeholder interviews, and qualitative customer research (interviews, observation, diary studies) across phases.
- [[2017-09-10_no-validate-in-ux]] — the framing and language used in research studies subtly shape participant behavior and team interpretation of findings.
- [[2018-01-21_test-tasks-quant-qualitative]] — The systematic approach and methods used to gather and analyze data; choice of methodology affects every aspect of task design, from specificity to flexibility.
- [[2018-02-11_measuring-perceived-usability]] — distinguishing between post-test and post-task questionnaires and understanding when to apply each measurement instrument.
- [[2018-04-08_multivariate-testing]] — choosing appropriate testing methodologies based on whether the goal is radical redesign validation (A/B) or incremental optimization (MVT).
- [[2018-04-22_quantitative-user-research-methods]] — understanding the range of quantitative methodologies available and their appropriate applications in UX research.
- [[2018-07-08_field-studies-intranet-redesign]] — The article discusses field studies as an alternative to surveys and lab-based testing, highlighting advantages and limitations of different research methods for understanding user behavior and workflows.
- [[2018-09-02_quant-research-practice]] — the techniques and approaches UX professionals use to gather insights; practitioners employ diverse methods depending on questions asked, budgets, timelines, and expertise available.
- [[2019-01-27_interpreting-research-findings]] — Multiple methodologies (quantitative, qualitative, observational) provide different perspectives on product performance; contradictions between methods require investigation rather than dismissal.
- [[2019-02-10_research-journey-mapping]] — Qualitative techniques including interviews, field studies, diary studies, and competitive analysis combined for comprehensive customer journey understanding.
- [[2019-02-24_responding-skepticism-small-usability-tests]] — Techniques for conducting, reporting, and defending usability research findings including participant recruitment, direct observation, and data analysis.
- [[2019-04-28_usability-testing-minors]] — Qualitative methods must be adapted for young users: shorter sessions, simpler language, more varied tasks, and different think-aloud techniques.
- [[2019-05-05_intentional-silence-ux]] — Intentional silence is a powerful moderation technique that enhances data quality in interviews and usability testing.
- [[2019-05-12_everyone-as-users]] — Defining user segments before research ensures data collection includes diverse perspectives and avoids recruitment bias toward one segment.
- [[2019-06-09_why-user-interviews-fail]] — interviews must be matched to research questions; methods range from generative (interviews, focus groups) to evaluative (usability testing), each suited to different questions.
- [[2019-10-27_unmoderated-usability-testing]] — emphasizes the importance of clear study goals, careful tool selection, task design, pilot testing, and rigorous analysis procedures.
- [[2019-12-01_usability-testing-101]] — documents different usability testing approaches (qualitative/quantitative, remote/in-person, moderated/unmoderated) and when to apply each.
- [[2020-01-26_critical-incident-technique]] — Presents the Critical Incident Technique as a systematic research method with specific advantages and limitations for gathering qualitative data about user experiences.
- [[2020-04-12_moderated-remote-usability-test-why]] — explains the trade-offs between moderated (rich data, facilitator skill required) and unmoderated (quick, cheap, less detailed) remote research methodologies.
- [[2020-05-17_discoveries-in-industry-revealed]] — documents common discovery activities including user interviews (62%), stakeholder interviews (60%), competitive analysis (49%), and analytics review (49%).
- [[2020-06-14_journey-mapping-approaches]] — tradeoffs between assumption-first and research-first approaches to user understanding.
- [[2020-06-21_persona-types]] — how qualitative interviews and quantitative surveys can be combined or used independently to understand user needs.
- [[2020-07-26_remote-usability-testing-costs]] — cost-benefit analysis of moderated vs. unmoderated remote usability testing approaches.
- [[2020-08-16_research-ops-101]] — Standardizing research methods and supporting documentation (scripts, templates, consent forms) enables consistent application across teams and saves time in research planning.
- [[2020-08-30_covid-changed-users]] — Qualitative research (interviews and surveys) becomes invaluable for uncovering deep insights about new user behaviors. Remote research is safest and most practical, with careful advance planning ensuring quality similar to in-person studies.
- [[2020-09-13_product-ux-benchmarks]] — Combining quantitative usability testing or analytics (behavioral data) with surveys (self-reported data) provides holistic understanding of user experience and accounts for contextual factors affecting metrics.
- [[2020-12-06_contextual-inquiry]] — contextual inquiry as one of several qualitative methods for understanding user behavior and work processes, appropriate for complex systems and expert users.
- [[2021-01-31_quantifying-case-study]] — illustrates a synthesis of qualitative research (usability testing, card sorting) and quantitative research (tree testing) for robust design validation.
- [[2021-02-07_testing-content-websites]] — explains when to use moderated vs. unmoderated approaches and how to structure participant recruitment and task design for content studies.
- [[2021-02-14_internal-vs-external-validity]] — provides practical recommendations for ensuring internal and external validity in both qualitative and quantitative UX studies.
- [[2021-02-21_triangulation-better-research-results-using-multiple-ux-methods]] — demonstrates how combining qualitative and quantitative methods balances their respective limitations and improves research reliability.
- [[2021-02-28_interview-guide]] — the article situates interview guides within the discovery phase of product development and qualitative research methodology.
- [[2021-06-06_interview-facilitation-mistakes]] — Interviews must focus on unbiased questioning and data collection; distinguishes research interviews from journalistic or casual conversations.
- [[2021-10-17_pareto-principle]] — UX professionals can apply the principle to identify which aspects of user experience merit deeper qualitative research based on quantitative patterns.
- [[2021-11-07_recruiting-screening-research-candidates]] — Screening and recruiting are foundational activities affecting research quality and the validity of findings.
- [[2022-02-20_secondary-research-in-ux]] — Secondary research involves identifying reliable sources (peer-reviewed publications, public datasets, academic databases) and critically evaluating them for validity, methodology, and generalizability to your context.
- [[2022-03-13_confirmation-bias-ux]] — best practices for designing unbiased research studies, asking nonleading questions, and using multiple data sources to counteract researcher bias.
- [[2022-05-01_high-income-participants]] — adapting study logistics (scheduling, incentives, access methods) to accommodate participant needs.
- [[2022-05-29_usability-checklist]] — Usability testing is one method among many; successful execution depends on proper participant setup, clear instructions, and thoughtful questioning.
- [[2022-07-17_which-ux-research-methods]] — The three-dimensional framework helps UX professionals select appropriate methods based on research questions, product phase, and resource constraints.
- [[2022-07-24_the-funnel-technique-in-qualitative-user-research]] — The funnel technique is a foundational qualitative research principle applicable across interviews, usability tests, and multimethod studies.
- [[2022-08-21_guide-ux-research-methods]] — Twenty popular research methods map across dimensions of attitudinal versus behavioral and qualitative versus quantitative, helping researchers select appropriate methods for different objectives.
- [[2022-10-09_why-field-study-sessions-go-wrong]] — field study quality deteriorates with poor planning; researchers must clarify purpose upfront, set expectations around observation (not complaint-collecting), and maintain neutral, observing postures.
- [[2022-12-18_journey-map-how-much-time]] — External user research and internal data collection constitute over half the total journey-mapping investment, suggesting the importance of thorough research upfront.
- [[2023-01-08_journey-mapping-how]] — User interviews are heavily relied upon; diary studies, though underutilized, are well-suited to journey-mapping research given journeys occur over time and across channels.
- [[2023-02-19_tips-user-research-field]] — field research is most effective when combined with clear documentation practices, diverse participant recruitment, and protocol flexibility to accommodate emerging insights.
- [[2023-02-26_10-survey-challenges]] — surveys are best used to complement observational methods, with timing (post-task), wording (ranges vs. exact numbers), and question ordering all affecting data quality.
- [[2023-04-23_data-findings-insights-differences]] — Approaches like thematic analysis for qualitative data and statistics for quantitative data that help researchers move from raw data to meaningful patterns.
- [[2023-05-07_ux-benchmarking-repository]] — Approaches for conducting user research including benchmarking studies that require consistency and documentation to enable valid comparisons over time.
- [[2023-05-21_hawthorne-effect-observer-bias-user-research]] — Various approaches for conducting user research including field studies, usability tests, surveys, and diary studies, each with distinct observer-bias mitigation strategies.
- [[2023-06-11_including-users-workshops]] — recruiting, incentivizing, and structuring user participation in research activities follows evidence-based methods to minimize bias and maximize participant value.
- [[2023-06-25_how-to-conduct-a-heuristic-evaluation]] — heuristic evaluation is positioned as a complementary technique that can prepare teams for user testing or extend limited research budgets.
- [[2023-07-02_ai-powered-tools-limitations]] — proper research practices require understanding how AI tools' limitations affect data validity and analysis quality.
- [[2023-09-24_confounding-variables-quantitative-ux]] — Proper study design requires identifying and controlling for confounding variables to ensure conclusions are valid and reliable.
- [[2023-11-24_surveys-design-cycle]] — surveys are one of many UX research methods, each suited to different phases and research questions in the design process.
- [[2024-01-05_competitive-usability-evaluations]] — competitive testing is a research method where users complete tasks on competitors' products to gather comparative performance data.
- [[2024-01-12_field-studies]] — field studies are one of several research methods; understanding when to use field studies vs. remote/lab methods is key for research planning.
- [[2024-02-23_should-you-run-a-survey]] — part of a toolkit requiring careful matching of method to research question type.
- [[2024-03-01_attitudinal-behavioral]] — a toolkit requiring both attitudinal and behavioral approaches for comprehensive understanding.
- [[2024-03-29_diary-studies]] — establishes diary studies as a distinct longitudinal research method complementary to other qualitative and observational approaches.
- [[2024-04-05_plan-research-ai]] — addresses how to use AI to identify and justify appropriate methods for specific research questions.
- [[2024-04-19_wizard-of-oz]] — presents the Wizard of Oz method as a research technique for testing interactive systems.
- [[2024-05-30_diverge-converge]] — the technique supports various UX research activities like data analysis, affinity diagramming, and research synthesis by enabling researchers to work independently before converging on patterns.
- [[2024-06-14_card-sorting-terminology-matches]] — the article provides methodological guidance on preventing common research biases in card sorting, ensuring more valid findings about mental models.
- [[2024-06-21_synthetic-users]] — genuine UX research must include real users to capture behavioral complexity, priorities, and contextual factors that AI cannot model.
- [[2024-09-13_free-ux-templates]] — systematic approaches to gathering user data and insights, including interviews, usability testing, and field research.
- [[2024-11-01_screening-participants]] — Covers practical research methods including written and synchronous phone screeners, pilot testing, and various questioning techniques to ensure quality data collection.
- [[2024-12-06_unmoderated-user-testing-tools]] — Covers how unmoderated testing fits within the broader research methodology landscape alongside other methods like A/B testing, diary studies, card sorts, and tree tests.
- [[2025-04-18_convenience-vs-probability-sampling]] — compares and contrasts convenience versus probability sampling, their underlying mechanics, and implementation requirements.
- [[2025-05-02_analyze-usability-data]] — details 4-step framework and the iteration cycles within it, emphasizing that good analysis requires testing explanations for good fit.
- [[2025-06-20_genai-ux-research-agenda]] — techniques and practices for understanding user needs, behaviors, and evaluating design effectiveness.
- [[2025-08-08_research-yes-or-no]] — The article discusses how research method choice and framing impact the quality and actionability of insights.
- [[2025-08-15_ai-simulations-studies]] — The article synthesizes findings from three distinct methodological approaches to building and evaluating AI-simulated users.
- [[2025-08-22_why-organizations-dont-do-user-research]] — The article argues that various research methods are fast, inexpensive, and practical without sacrificing quality.
- [[2025-10-10_screener-foils]] — Provides practical guidance on designing foils that are plausible and relevant while remaining rare enough to test attention without confusing genuine participants.
- [[2025-11-28_diary-study-entries]] — what this article contributes to this concept
- [[2025-12-19_top-videos-2025]] — OOUX and personas remain foundational tools for structuring user understanding and design decisions.
- [[2026-01-02_ux-quiz]] — Diary studies, mixed-methods approaches, and research application workshops represent key methodologies for gathering and acting on user data.
- [[2026-03-06_practical-significance]] — Explains the distinction between statistical and practical significance and how researchers should weigh both in deciding whether to act on findings.
- [[2026-03-13_research-tool-problems]] — Highlights the importance of sound research design and how tool design choices either support or undermine research rigor.
- [[2026-04-03_ai-survey-writing]] — GenAI assists but does not replace the expertise needed to design surveys that actually measure what they intend to measure.
- [[2013-08-01_just-enough-research_01-foreword]] — Zeldman frames the book as teaching research techniques designed for speed and practicality in constrained environments, not theoretical purity.
- [[2013-08-01_just-enough-research_02-chapter-1-enough-is-enough]] — Hall distinguishes personal research (finding existing information), pure research (advancing a field through experimentation), and applied research (serving real-world goals with relaxed methods).
- [[2013-08-01_just-enough-research_03-chapter-2-the-basics]] — The chapter distinguishes generative (exploratory), descriptive (understanding), evaluative (testing), and causal (post-hoc explanation) research, and emphasizes matching method to the specific questions the project needs answered.
- [[2013-08-01_just-enough-research_04-chapter-3-the-process]] — the chapter presents the complete methodical cycle from problem definition through reporting, with emphasis on interviewing, usability testing, and literature review as core techniques.
- [[2013-08-01_just-enough-research_05-chapter-4-organizational-research]] — organizational research applies the same interview principles discussed in the previous chapter, but to stakeholders rather than end users; it surfaces business requirements and organizational constraints.
- [[2013-08-01_just-enough-research_06-chapter-5-user-research]] — the chapter covers ethnographic interviews, contextual inquiry (site visits), and explains why focus groups fail; it emphasizes participant observation in natural settings as central to understanding behavior.
- [[2013-08-01_just-enough-research_11-conclusion]] — the conclusion frames research as a toolbox of techniques (outlined throughout the book) to be selected based on goals and resources; emphasizes that the specific methods matter less than having a research habit and asking the right questions.
- [[2016-11-04_ux-research_02-chapter-1-the-history-of-research]] — Motion studies, GOMS, and KLM represent methods for measuring and improving efficiency and performance that evolved from manufacturing into human-computer interaction.
- [[2016-11-04_ux-research_06-chapter-5-choosing-your-methods]] — the chapter's primary focus, providing a systematic approach to selecting appropriate methods rather than seeking a one-size-fits-all approach, emphasizing that research methodology is a learnable skill
- [[2016-11-04_ux-research_16-chapter-15-getting-the-most-out-of-research]] — the main chapter frames qualitative and quantitative methods as complementary, encouraging teams to combine them for depth and breadth as they revisit topics over time. In his sidebar, Ofer Deshe adds that as a CEO he personally relies on structured observations, ethnographic studies, and methods rooted in sociology and psychology.
