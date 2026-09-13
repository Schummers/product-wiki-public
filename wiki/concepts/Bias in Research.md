---
type: concept
name: Bias in Research
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Research Bias"
---

# Bias in Research

## Definition

Bias in research is the set of systematic errors in data collection or
interpretation that skew results away from what users actually think and do
[[2017-12-17_leading-questions]]. The sources treat it not as an occasional
accident but as the default state of any study that is not deliberately designed
against it: bias enters through who is recruited
[[2016-09-04_employees-user-test]], how they are screened
[[2019-07-14_screening-questions-select-research-participants]], how tasks are
worded [[2017-04-09_better-usability-tasks]], how follow-up questions are asked
[[2017-12-17_leading-questions]], and how the social setting of the session
shapes what participants are willing to say
[[2022-07-31_focus-groups-definition]].

A recurring mechanism links these: participants adapt to the researcher.
Employees adapt to their employer's interests
[[2016-09-04_employees-user-test]], screener respondents adapt to whatever they
guess will get them into the study
[[2019-07-14_screening-questions-select-research-participants]], interviewees
mimic the interviewer's words because the interviewer reads as an authority
[[2017-12-17_leading-questions]], and focus-group participants adapt to the
loudest person in the room [[2022-07-31_focus-groups-definition]]. The cost is
the same everywhere: findings that look like data but reflect the study's own
framing, and the loss of the unexpected insight the research existed to find
[[2017-12-17_leading-questions]].

## Practice

### Who you recruit decides what you can learn

Testing with employees saves time and money and introduces systematic bias that
compromises validity [[2016-09-04_employees-user-test]]. The named sources of
that bias are prior knowledge of company jargon, business goals and the project
itself; higher motivation to engage; different assumptions about feasibility and
resources; loyalty and internal relationships; and fear of disappointing the
team or insulting a designer's work. The effect is measurable: Yahoo! research
found employees rated their own company's site 2% higher than external users
did, while external users rated it 15% lower than competitors; employees also
spent less time on competitor sites and were more critical of them, and felt
obliged to complete tasks. Both preference and performance data were skewed.

The source's position is that thirty years of usability research show external
participants give more trustworthy and generalisable data, and that internal
recruitment is legitimate only in three cases: testing intranets, where
employees genuinely are the target audience; pilot tests to shake out
methodology flaws; and skunkworks demonstrations in organisations that do not
yet invest in UX — choosing, where possible, employees with minimal project
knowledge [[2016-09-04_employees-user-test]]. The warning attached is about
credibility rather than statistics: inconclusive employee results can acquire
false authority simply because they come from trusted colleagues, and acting on
them wastes resources without serving actual customers.

### Screening without telling participants what you want

[[2016-11-04_ux-research_08-chapter-7-recruiting]] names the failure mode
screening exists to prevent: without a screener, teams fall back on assuming
"everyone is a user" or recruiting whoever is convenient, and either habit
reintroduces the bias a screener is supposed to remove.

Screening questions carry two conflicting goals: eliciting specific information
about users while avoiding revealing the study's purpose, because respondents
who can guess the target profile will exaggerate their qualifications to get in
and collect the incentive
[[2019-07-14_screening-questions-select-research-participants]]. Two techniques
resolve the conflict:

- **Open-ended questions** — asking "What activities do you do online?" instead
  of "Do you play games?" makes the right answer hard to guess. They work well
  for assessing genuine interest and experience level and for catching
  disqualifying occupations; asking someone to describe favourite games and why
  quickly separates the hard-core gamer who reels off names and details from the
  person who can barely remember any. The costs are response time and the
  analysis of free text, which makes them impractical for unmoderated studies.
- **Distractor answer choices** — plausible alternatives alongside the target
  (walk, ride a bike, rent a scooter, use a rideshare) rather than an obvious
  target next to obviously wrong options such as hang gliding. Distractors
  disguise the purpose while allowing instant evaluation, which is what makes
  unmoderated recruiting possible. A respondent selecting every answer is a
  signal they are too eager to participate.

Combining the two — open-ended for occupations, distractors for behaviours —
often works best [[2019-07-14_screening-questions-select-research-participants]].

### Task wording as a source of bias

How a task is written directly determines the outcome of a study; bad
instructions bias participants and change what the study finds
[[2017-04-09_better-usability-tasks]]. The specific traps:

- **Interface language in the task** — repeating the exact words from the UI
  primes participants and turns the study into a test of reading comprehension
  rather than of navigation and labelling.
- **Telling users the steps** — revealing in advance that they must register or
  download removes the chance to observe surprise or annoyance.
- **Stale references** — dates and events must be current during testing, or the
  site and task feel unrealistic.
- **Tasks that require no effort** — a task should make users process
  information, not merely locate it, so that real cognitive activity is
  observed.
- **Elaborate scenarios** — brief context can clarify, but a long backstory adds
  complexity and signals that the task is unrealistic if that much justification
  is needed.
- **Internal vocabulary** — marketing phrases, business jargon, and corporate
  acronyms should be replaced with words users would actually use.
- **Emotional or offensive content** — avoid specific relationships, jokes,
  famous names, and sensitive topics such as politics, health, religion, or
  money; this is framed as a matter of participant well-being as well as
  validity.
- **Questions instead of imperatives** — "Find X", not "How would you find X",
  because the point is to observe what users do rather than what they say they
  would do.

The organising principle is to start from the user's end goal rather than the
task's end goal or the feature under test: ask why someone would use that
section at all [[2017-04-09_better-usability-tasks]].

### Leading questions in moderation and interviews

A leading question includes or implies the desired answer, making it difficult
or socially awkward to disagree [[2017-12-17_leading-questions]]. The source
grades three versions of the same follow-up: "I saw you were having difficulty"
assumes what was observed and is not neutral; "Why did you have difficulty"
still implies difficulty occurred; "What was easy or difficult" lets the
participant define their own experience.

Why this matters more in a test than in ordinary conversation: the interviewer
is perceived as an authority, and many participants are reluctant to contradict
someone in a position of power, so a leading question adds social pressure to
confirm. Participants also simply mimic the interviewer's words. The traps
listed are rephrasing an observation in the interviewer's own words, which can
misrepresent the experience; suggesting an answer through wording; naming
specific UI elements, which primes terminology; and assuming what emotion the
user felt. Open-ended questions that elicit explanations rather than yes/no
answers are the stated requirement, and the cost of not using them is losing the
surprising insight that would have revealed a problem the researcher did not
anticipate [[2017-12-17_leading-questions]].

### Four pitfalls in question design, and when to break them deliberately

[[2016-11-04_ux-research_03-chapter-2-good-research-starts-with-good-questions]]
names four pitfalls that undermine a question, extending the leading-question
problem into a fuller taxonomy: leading questions that inadvertently suggest
an answer to participants who want to be helpful, shallow yes/no questions
that give an easy out, personal bias that lets the researcher's own beliefs
slip into the wording, and unconscious bias reflecting social norms and
expectations the researcher may not even be aware of holding. It adds a
nuance the corpus's other treatment of leading questions does not allow for:
once a researcher has practiced enough to control the effect, three of those
pitfalls can be used deliberately — a leading question to build trust or
validate a comment already made, a shallow question to ease a participant
into comfort before probing further, and personal bias voiced as devil's
advocacy to spark deeper discussion. Throughout, the rule given is to relate
every question back to the research goals: if a question does not produce
information that helps answer them, it should be cut from the guide.

### Group settings and self-report

Focus groups — a qualitative, attitudinal method, typically 6–9 participants in
a facilitated 1–2 hour discussion — concentrate several biases at once
[[2022-07-31_focus-groups-definition]]. On the individual side: memory is
fallible, negativity bias pulls discussion toward bad experiences, the peak-end
rule overweights memorable moments, priming makes participants overemphasise
whatever someone else raised, and social desirability shapes what gets said. On
the group side: dominant personalities skew participation, groupthink suppresses
disagreement, and under-facilitation reduces the session to the views of the
most vocal — "a great way to pay 9 people for the opinions of three".

The methodological consequence is scope. Focus groups cannot produce behavioural
or usability data, because people do not always do what they say they will;
observational methods such as usability tests or field studies are required for
that. They do not predict future behaviour and should be treated as a starting
point for further research rather than a validation step. Where they work is
early discovery: gauging familiarity or interest in a concept, understanding
mental models and vocabulary before design, and cocreation workshops. Mitigation
is largely facilitation: recruit representative participants including diverse
seniority levels, use structured warmups, offer both written and verbal
participation so quieter people contribute, use open-ended questions with the
funnel technique, and combine the method with others
[[2022-07-31_focus-groups-definition]].

## Sources (9)

- [[2016-09-04_employees-user-test]] — Identifies multiple sources of systematic bias (prior knowledge, motivation, fear, loyalty, internal relationships) that cause employee data to diverge from actual customer behavior.
- [[2017-04-09_better-usability-tasks]] — Explains how poor task construction (priming with interface language, revealing steps, emotional content) can bias participants and invalidate findings.
- [[2017-12-17_leading-questions]] — Systematic errors in data collection or interpretation that skew results; leading questions are a major source of bias, causing participants to confirm interviewer assumptions rather than express genuine experience.
- [[2019-07-14_screening-questions-select-research-participants]] — respondents may exaggerate qualifications if study purpose is obvious; carefully designed screening questions reduce response bias and ensure authentic participant profiles, improving research validity.
- [[2022-07-31_focus-groups-definition]] — Focus groups are vulnerable to negativity bias, peak-end rule, priming, and group dynamics; participants are also prone to memory fallibility and social desirability bias.
- [[2013-08-01_just-enough-research_03-chapter-2-the-basics]] — Hall catalogs design bias, sampling bias, interviewer bias, sponsor bias, social desirability bias, and the Hawthorne effect, arguing that acknowledging bias allows appropriate weighting of results without claiming impossible objectivity.
- [[2013-08-01_just-enough-research_06-chapter-5-user-research]] — the chapter argues that assumptions about users (age, gender, ethnicity, sexuality, abilities) can embed discrimination into products; user research replaces assumptions with actual insight about diverse individuals.
- [[2016-11-04_ux-research_03-chapter-2-good-research-starts-with-good-questions]] — The chapter lists four factors that can lead to misinformed or poor research results, two of them biases: leading questions that point participants toward predetermined answers, shallow yes/no questions that avoid depth, personal bias that introduces the researcher's own beliefs, and unconscious bias from social norms, personal history, past experiences or expectations, which the chapter calls the hardest to catch.
- [[2016-11-04_ux-research_08-chapter-7-recruiting]] — avoiding bias in recruitment by using appropriate screeners rather than assuming "everyone is a user" or recruiting convenient contacts.
