---
type: concept
name: Survey Design
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Open-Ended Questions"
  - "Question Design"
  - "Survey Research"
---

# Survey Design

## Definition

Survey design is the craft of writing and structuring questions that elicit
genuine, analysable answers — and the discipline of knowing what a survey can and
cannot tell you. Its central constraint, stated bluntly by the sources, is that
surveys measure attitudes and perceptions, not behaviours: use them to learn what
users think and feel, not what they do, because self-reported answers are filtered
by the respondent before they reach the researcher, whereas observational methods
capture real-time behaviour that cannot easily be faked
[[2023-02-26_10-survey-challenges]]. A survey is also frequently misused precisely
because practitioners assume it is quick and easy
[[2023-11-24_surveys-design-cycle]], and it is very easy to write a bad survey
that gathers flawed data [[2023-02-26_10-survey-challenges]].

The sources treat a survey instrument as a design in its own right, subject to the
same iteration as a user interface: small details of wording change how
respondents interpret and answer, and a carelessly written question can ruin a
study [[2019-10-06_survey-questions-iterative-design]]. Under this concept the
corpus also collects the wider craft of question construction shared with
interviews and screeners — open-ended versus closed questions
[[2024-01-26_open-ended-questions]], leading questions
[[2017-12-17_leading-questions]], interview guides
[[2021-02-28_interview-guide]] and interview-question mistakes
[[2022-03-06_interview-questions-mistakes]] — while noting that the two contexts
are not interchangeable: questions that might be fit for a questionnaire are not
always appropriate for a user interview [[2022-03-06_interview-questions-mistakes]].

## Practice

### Choose the survey type from where you are in the design cycle

Survey selection should follow the research goal, and the design cycle's four
phases each call for different types. **Discover**: discovery surveys and
diary-study surveys to gather background information and longitudinal behaviour,
often qualitative. **Explore**: competitor surveys and statistical-persona surveys
to inform direction and quantify segments. **Test**: post-task and post-test
instruments (SEQ, SUS) to measure perceived usability of prototypes, whose
established benchmarks make results interpretable. **Listen**: NPS, CSAT and CES
to monitor sentiment and catch problems early — with the caveat that NPS alone
should never be the only usability metric — plus custom listening surveys deployed
at key moments through intercept popups to track metrics longitudinally. Surveys
are most commonly associated with the Listen phase, but with proper strategy they
can serve any phase [[2023-11-24_surveys-design-cycle]].

Qualitative, open-ended surveys have a specific role upstream: they help discover
what questions to ask and what the answer categories should be, which prevents the
mistake of going straight to closed-ended questions designed from conference-room
assumptions [[2016-09-25_qualitative-surveys]].

### Open-ended and closed questions

Open-ended questions let participants answer freely and are where unanticipated
findings come from — motivations you did not expect, behaviours and concerns you
knew nothing about. Closed questions are faster to answer and easier to quantify,
but they stop the conversation: an interview made only of closed questions stays
stilted and surface-level. The recommended sequence is the **funnel technique** —
open broad, then narrow with specific closed questions — so that the specifics do
not prime the general [[2024-01-26_open-ended-questions]].

Grammar carries the bias. Questions beginning with "did", "was" or "is" often
suggest an expected answer, while "how" and "what" stay neutral; "How do you
normally…?" produces richer answers than "Do you normally…?"
[[2024-01-26_open-ended-questions]]. In interviews specifically, review each
question and ask whether a broader, more open-ended version exists — converting
yes/no questions into narrative prompts such as "Tell me about…" invites stories
and unanticipated detail [[2021-02-28_interview-guide]]. Probing questions extend
the inquiry: "Tell me more about that", "Why do you think that?"
[[2024-01-26_open-ended-questions]], and each main question should come with
prepared follow-ups such as "Where were you when this happened?"
[[2021-02-28_interview-guide]].

### Avoid leading and malformed questions

A leading question includes or implies its desired answer, making it difficult or
socially awkward to disagree. It matters more than it looks: the facilitator is
perceived as an authority, participants are reluctant to contradict authority, and
respondents are prone to mimic the interviewer's words. Three versions of the same
follow-up illustrate the gradient — "I saw you were having difficulty" assumes the
observation, "Why did you have difficulty" still presupposes it, and "What was
easy or difficult" lets the participant define their own experience. The named
traps are rephrasing observations in the interviewer's own words, suggesting
answers through wording, naming specific interface elements (which primes
terminology), and assuming what the user felt. Beyond biased answers, leading
questions cost you the insight you were not expecting
[[2017-12-17_leading-questions]].

Six recurring mistakes when drafting questions: starting with closed questions
that belong in a screener; asking about *typical* behaviour rather than specific
recent examples, since perceptions of typicality diverge from actual behaviour;
asking hypothetical questions, since people predict their own future behaviour
badly while answering confidently; leading with "because", which should be
replaced by neutral prompts like "What made you decide…?"; compound questions that
ask several things at once and exceed working memory, which should be split with
follow-ups; and ambiguous, over-broad questions that invite misinterpretation
[[2022-03-06_interview-questions-mistakes]].

### Question wording is tested, not reasoned

An iterative case study over four rounds shows that changes intended to clarify
can introduce bias instead. Adding an explanatory sentence defining "significant
action or decision" narrowed respondents toward change-related answers, excluding
other significant decisions; a preceding multiselect question listing activities
(with "Researched a topic" last) primed subsequent open-ended answers toward
research; and adding reassurance — "If you can recall several such instances,
please describe the one that was the most important to you" — reduced overthinking.
Context drifts too: "finding online information" was unusual and specific in 1998
and mundane by 2019, changing how the same question is read. People interpret
subtle cues and behave as they assume researchers want, even subconsciously
[[2019-10-06_survey-questions-iterative-design]].

### Pilot testing

Every source that touches this agrees the instrument must be piloted with real
target-audience members rather than colleagues, using think-aloud protocols
[[2016-09-25_qualitative-surveys]],
[[2019-10-06_survey-questions-iterative-design]]. They differ on scale: one
recommends at least four rounds with **one** participant per round, testing on
paper first and then in the survey platform, checking that the output format is
actually analysable [[2016-09-25_qualitative-surveys]]; the other recommends
**5–10 participants per iteration** [[2019-10-06_survey-questions-iterative-design]].
For interview guides, piloting with one or two participants is enough to reveal
which questions need rewording, whether timing is realistic, and whether the order
works [[2021-02-28_interview-guide]]. AI-drafted surveys are held to the same bar:
pilot testing with real participants is what separates a draft that looks good
from one that yields trustworthy data [[2026-04-03_ai-survey-writing]].

### Length, order and structure

Length is the primary driver of completion, and every extra question reduces
response rate and decreases validity; twenty questions is too many unless
participants are highly motivated, one-question surveys get the highest
participation, and two short surveys to two subsamples beat one long survey
[[2016-09-25_qualitative-surveys]]. Feedback surveys should likewise be short and
task-specific [[2023-03-26_user-feedback]]. Conditional logic keeps each
respondent's path short and prevents them hitting questions they cannot answer,
which would otherwise bias results [[2016-09-25_qualitative-surveys]]. Mark
"(Required)" or "(Optional)" after each question — red asterisks and top-level
instructions do not work well [[2016-09-25_qualitative-surveys]].

Order effects are real and the sources give partly different remedies. One
prescribes randomizing the order of sections, questions and answer options, so
that first-position options do not attract disproportionate attention and
respondents who quit partway do not skew the data — while also front-loading the
important questions [[2016-09-25_qualitative-surveys]]. Another treats order as
something to sequence deliberately: build rapport first, put sensitive and
demographic questions at the end rather than the beginning
[[2024-08-09_sensitive-questions]]. For interviews, order should follow a natural
narrative, warmups first and reflective questions later
[[2021-02-28_interview-guide]]. What all agree on is that sequence changes
answers, through priming, recency and anchoring
[[2019-10-06_survey-questions-iterative-design]],
[[2023-02-26_10-survey-challenges]].

### Sensitive and demographic questions

A sensitive question is one respondents might find embarrassing or invasive.
Discomfort costs data: income questions are ten times more likely to be left blank
than other demographic questions, and respondents may abandon the survey or answer
unreliably. The guidelines are to emphasize confidentiality, provide context, offer
ranges rather than exact values (income brackets, age ranges, frequency options),
place sensitive items late, use indirect techniques such as the item-count method,
and load the question with normalizing context for potentially shameful behaviours.
Demographic wording must be inclusive and avoid assumptions about age, gender, race
and income [[2024-08-09_sensitive-questions]]. The same instruments —
confidentiality assurances, indirect questioning and ranges instead of exact
numbers — are recommended against social-desirability bias
[[2023-02-26_10-survey-challenges]].

### Response biases to design against

Ten named distortions: recall bias (mitigate by distributing the survey as soon as
possible after the experience), recency bias, social-desirability bias, prestige
bias, acquiescence bias, order effects, mood bias, central-tendency bias, demand
characteristics, and random-response bias. Two structural limits compound them:
respondents filter and self-censor before sharing, and the researcher cannot probe
— surveys yield ratings and selections with no chance to ask why
[[2023-02-26_10-survey-challenges]].

### Asking at the right moment, through the right channel

**Task, then ask.** Requesting feedback before users have done anything skews
results and is logically empty; asking after a real task, while the experience is
fresh, produces relevant feedback. Requests should be subtle, dismissible, and not
obstruct information the user needs, with an always-available on-demand option such
as a small feedback tab. Rather than defaulting to email — users are flooded with
feedback-request emails — request feedback through the channel where the
interaction happened (push notification, in-app message, SMS), and better still let
people choose the channel. Requests specific to the completed task ("Tell us about
your cancellation experience") outperform generic satisfaction questions, and a
cheerful tone misaligned with the user's emotional state (mid tax-filing, say)
reads as tone-deaf and erodes trust. Appreciate participants
[[2023-03-26_user-feedback]].

### GenAI as a drafting aid, not a designer

GenAI tools produce solid first drafts: questions covering multiple dimensions,
clear neutral language, avoidance of double-barrelled wording, logical grouping,
a sensible open/closed mix. Their documented weaknesses are underestimating
respondent burden (suggesting grid questions that encourage straightlining, too
many multiselect options, demographic questions placed too early), flawed response
options (missing "Other", unbalanced scales, custom Likert scales that depart from
standard formats), overlooked formats (semantic differential scales, rank-order
questions), and, in AI-moderated studies, tasks that prime participants
unrealistically. It takes an experienced survey designer to tell a seemingly good
draft from one that will actually yield trustworthy data
[[2026-04-03_ai-survey-writing]].

### Cleaning the data: bots

Survey bots — automated scripts or people using automation tools — are an
increasing risk, especially with open distribution channels or monetary
incentives, and many pass basic attention checks. Detection signals: completion
times far below the pilot-tested median, or suspiciously uniform (dozens of
responses at exactly five minutes); open-ended answers that are long and generic,
uniform in length, unusually polished without typos, or vague in an AI-like way
with no specifics about the respondent's own experience; duplicate IP and email
patterns. Open-ended questions are the most powerful detector, because a
believable free-text answer is much harder to fake than a random multiple-choice
selection. No single sign is conclusive — a fast completion may be a power user, a
duplicate IP may be a household — but two or three converging signals warrant
removal. Batches differ from one another and the signals decay as tools improve,
so patterns must be re-learned. Always document how many responses were flagged
and removed and on what grounds, so stakeholders read the sample size as
deliberate quality control [[2026-06-26_survey-bots]].

### Analysing and reporting

Code open-ended responses to find trends and visualize them to make findings
actionable — and stay realistic about what the numbers mean: qualitative survey
metrics are rarely representative of the whole target audience, they represent the
opinions of the respondents [[2016-09-25_qualitative-surveys]].

## Sources (13)

- [[2016-09-25_qualitative-surveys]] — Provides 28 concrete practices for creating valid, analyzable qualitative surveys including testing, structure, questions, and data analysis approaches.
- [[2017-12-17_leading-questions]] — The craft of creating questions that elicit genuine participant responses; requires understanding how wording, framing, and phrasing influence how people answer.
- [[2019-10-06_survey-questions-iterative-design]] — Survey questions are sensitive to wording, order, and priming; iterative pilot testing is essential to ensure neutral language and valid responses.
- [[2021-02-28_interview-guide]] — the article explains how to convert closed questions into open-ended prompts that encourage narrative responses and story-telling.
- [[2022-03-06_interview-questions-mistakes]] — Starting interviews with open-ended prompts allows participants to share stories and unexpected insights, while avoiding six common mistakes when crafting interview questions ensures reliable, actionable research data.
- [[2023-02-26_10-survey-challenges]] — effective surveys must account for recall limitations, social desirability, question ordering, and the fundamental constraint that surveys measure attitudes rather than behaviors.
- [[2023-03-26_user-feedback]] — feedback surveys should be short, task-specific, and delivered through channels matching user interaction channels to maximize response quality and quantity.
- [[2023-11-24_surveys-design-cycle]] — the article provides guidance on when and how to use surveys, emphasizing that survey selection should align with research goals at each design phase.
- [[2024-01-26_open-ended-questions]] — a primary research method for discovering unexpected insights and understanding participant mental models and concerns.
- [[2024-08-09_sensitive-questions]] — addresses how to structure surveys to maximize response rates and data quality when asking sensitive topics.
- [[2026-04-03_ai-survey-writing]] — Emphasizes best practices that GenAI often misses, and the importance of pilot testing with real participants.
- [[2026-06-26_survey-bots]] — depends on identifying and removing bot responses to maintain the validity of findings and conclusions drawn from collected data.
- [[2016-11-04_ux-research_04-chapter-3-quantitative-research-methods]] — surveys are covered as an evaluative and insight-driven method that allows active, proactive collection of data on customer expectations and service quality, with various tools available for implementation
