---
type: concept
name: Participant Recruitment
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Participant Incentives"
  - "Participant Screening"
  - "Research Participant Recruitment"
  - "Screening"
---

# Participant Recruitment

## Definition

Participant recruitment is the work of finding, screening, scheduling and
compensating the people a study runs with. The sources treat it as a validity
question rather than a logistics one: the right participants are actual users of
the product, or representative users who mimic the demographic and behavioural
characteristics of the target audience, and without them the findings are
invalid regardless of how well the sessions were run
[[2024-11-01_screening-participants]], [[2026-05-01_selection-criteria]]. A
study has external validity only when its participants and setup represent the
real-world situation the design is used in [[2026-05-01_selection-criteria]].

The recurring risk is **misrecruitment** — poor-fit candidates who lack the
necessary experience, professional testers who are over-experienced in research,
and bad actors who lie to qualify [[2026-05-01_selection-criteria]]. Its most
expensive form is the undetected one: when flawed data is folded into findings
and drives business decisions, the cost is invisible
[[2026-05-01_selection-criteria]]. Recruitment failure also feeds back into
analysis, where misrecruits (professional participants, coworkers) undermine the
appropriateness of a data point and limit how far an insight generalises
[[2025-04-11_usability-data-in-analysis]].

## Practice

### Define who you need, and who you do not

Selection criteria come in three types: **inclusion** (who is a good fit),
**exclusion** (who would introduce bias) and **diversity** (who ensures the
sample represents the real population rather than one skewed perspective)
[[2026-05-01_selection-criteria]]. Demographics alone are weak predictors of
behaviour; behavioural history and attitudes shape mental models and predict
engagement with the product far better
[[2026-05-01_selection-criteria]], and criteria should focus on the behavioural
and demographic characteristics most critical to the research questions rather
than chasing a perfect participant who matches everything, which produces an
overly restrictive screener [[2024-11-01_screening-participants]]. Avoid
criteria that eliminate good candidates for weak reasons, such as excluding
anyone who has participated in any research recently
[[2021-11-07_recruiting-screening-research-candidates]].

[[2016-11-04_ux-research_08-chapter-7-recruiting]] starts one step earlier, with
participant identification: begin from existing sources such as past
qualitative research, current analytics reports, or customer segments from
marketing, or write baseline user profiles, so recruitment criteria stay
aligned with the research goals and product strategy. On sample size it gives a
lighter default than a matrix approach: assuming participant availability is
not an issue, qualitative research typically targets three to five
participants per user profile, with the number shifting based on how important
that profile is to hear from and how hard it is to find matching people.

A **recruitment matrix** maps behavioural segments against diversity criteria to
prevent one user type dominating and to surface remaining gaps; it is a flexible
guide, not a rigid quota system [[2026-05-01_selection-criteria]]. Screening for
diversity means covering genders, ages, ethnicities, abilities and tech skill
levels, prioritising characteristics relevant to inclusive design such as low
digital skills or accessibility needs
[[2021-11-07_recruiting-screening-research-candidates]].

### Screeners

A screener is a set of questions, delivered verbally or as a written
questionnaire, establishing whether a prospective participant fits the project
[[2024-11-01_screening-participants]]; it identifies optimal candidates and
excludes poor fits [[2021-11-07_recruiting-screening-research-candidates]].
Screeners protect data quality by weeding out poor-quality respondents, save
time and money by stopping unsuitable people before the session, and reduce the
bias of volunteer panels that skew toward IT professionals and other web-savvy
individuals [[2024-11-01_screening-participants]].
[[2016-11-04_ux-research_08-chapter-7-recruiting]] adds a practical target for
length, 10-15 minutes, using multiple-choice questions that confirm
desirability or disqualify candidates, and pushes the demographic criteria
past age and income into behavioural demographics relevant to the product —
online shopping habits, how participants resolve issues, or where they use a
product.

Screening questions have two conflicting goals: elicit specific information
about the participant while concealing what the study is about, so respondents
cannot exaggerate their way into the incentive
[[2019-07-14_screening-questions-select-research-participants]]. The techniques
the sources give:

- **Open-ended questions** make the "right" answer hard to guess. Ask what
  activities someone does online rather than whether they play games; asking a
  self-declared gamer to describe favourite games and why quickly separates the
  hard-core player from someone who can barely name one. Effective for past
  experience, disqualifying occupations and genuine interest levels, but they
  cost time to answer and to analyse, which makes them impractical for
  unmoderated studies
  [[2019-07-14_screening-questions-select-research-participants]].
- **Distractors** are plausible but non-target answer options that hide the
  study's purpose while allowing instant evaluation, which is what makes
  multiple choice workable for unmoderated recruiting. They must look realistic
  and relevant (walk, ride a bike, rent a scooter, use rideshare) rather than
  absurd (hang gliding). A respondent selecting every answer is a sign of
  over-eagerness to qualify
  [[2019-07-14_screening-questions-select-research-participants]].
  Combining the two techniques — open-ended for occupation, distractors for
  behaviour — often works best
  [[2019-07-14_screening-questions-select-research-participants]], and the same
  advice appears as using open-ended or multiple-choice-with-distractor
  questions to avoid telegraphing intent
  [[2021-11-07_recruiting-screening-research-candidates]].
- **Foils** are deliberately false answer options or questions — a nonexistent
  cloud-storage service in a list — that reveal respondents clicking through
  without attention, guessing to qualify, or misrepresenting themselves; a
  selection flags reliability concerns [[2025-10-10_screener-foils]]. Foil
  *answer options* work better than whole foil questions because they blend into
  the real options without adding length. Three design principles: plausible
  (blends in, does not stand out as nonsense), relevant to the topic (a foil for
  streaming services should sound like a service brand), and used sparingly —
  one or two per screener, since more confuses genuine participants
  [[2025-10-10_screener-foils]]. Foils catch some misrecruits, not all: pair
  them with open-ended questions requiring specific knowledge, consistency
  checks across questions, and validation during the live session
  [[2025-10-10_screener-foils]].
- **Ask about past behaviour, not hypothetical future behaviour** — users are
  notoriously unreliable at predicting whether they would use a product that
  does not yet exist, whether through genuine misestimation, a wish to flatter
  the researcher, or an attempt to lie into a paid opportunity
  [[2024-11-01_screening-participants]].
- **Avoid yes/no questions**, which are easy to game; use multi-option questions
  or several questions that make the intent harder to guess
  [[2024-11-01_screening-participants]].
- **Order the questions deliberately** — place critical elimination criteria
  early so respondents' time is not wasted
  [[2021-11-07_recruiting-screening-research-candidates]]. The same rule governs
  demographics: screening demographics (those determining eligibility) go early,
  non-screening demographics at the end, so participants feel invested before
  meeting sensitive questions [[2022-11-27_demographics-in-ux]].
- **Pilot the screener** with a few people to catch typos, confusing wording and
  skip-logic problems before launch [[2024-11-01_screening-participants]].

Screeners reduce manual vetting but do not eliminate it: someone still has to
review the answers for quality, including borderline candidates who may in fact
be acceptable — a person owning both an Android and an iPhone might be screened
out while being perfectly qualified
[[2021-11-07_recruiting-screening-research-candidates]].

### Carrying recruitment data into the session

[[2016-11-04_ux-research_10-chapter-9-managing-people-during-research]] treats
the recruitment record as feeding directly into rapport rather than closing
once someone is booked: understanding what is already known about a
participant, building initial rapport during the warm-up, and adjusting
communication style to match their personality — mirroring their word
preferences and posture, as UX researcher Lis Hubert describes it — are
treated as essential to participant comfort and engagement.

### Demographic questions

Collect only demographics whose use you can justify, since unnecessary questions
lengthen surveys, raise sensitivity and lower response rates
[[2022-11-27_demographics-in-ux]]. Use broad response ranges (10-15 year age
bands rather than 45-50, unless developmental differences justify narrower
bands) and explain why specific information is needed; always include a "Prefer
not to say" option so people can skip a question without abandoning the study;
use inclusive and current language for gender, including nonbinary and
transgender options, and rethink "Other" so nobody is implied to be abnormal;
allow "select all that apply" for sensitive categories such as race and gender
[[2022-11-27_demographics-in-ux]].

### Where to find participants

Five recruiting channels, each fitting different needs: professional recruiters
for specialised requirements, automated platforms for general audiences,
internal user panels for power users, online forums for niche interests, and
intercept studies for site visitors or task-specific users
[[2021-11-07_recruiting-screening-research-candidates]].
[[2016-11-04_ux-research_08-chapter-7-recruiting]] gives a parallel breakdown:
self-recruiting (DIY, slow, requiring a minimum two-week lead time), in-person
intercepts, online intercepts, cold calling, and outsourcing to third-party
firms or client-based recruiters. Remote-testing
platforms often carry "professional testers" who participate for income, so vet
screening answers for reasonableness and consider combining methods
[[2021-11-07_recruiting-screening-research-candidates]].

**Internal panels** let a team spin up small studies quickly and cut costs
relative to external recruiting services, but demand real upfront investment and
ongoing maintenance [[2023-05-07_research-participant-database]]. Practices:
choose tooling to match team maturity (a spreadsheet is simple but manual, CRM
software adds structure, specialised tools streamline the whole workflow at a
cost); collect only the data you need, since everything captured must be
maintained and stored; track engagement history — last contact, participation
dates, articulation level, number of studies — to avoid over-recruiting the same
people; work with legal and compliance on security, storage and GDPR, and
communicate the policy to opt-in participants; populate from existing customer
touchpoints such as support interactions, surveys, events and social media; and
audit regularly, removing stale contacts and making opt-out easy at every
contact [[2023-05-07_research-participant-database]].

Panels also fail in predictable ways [[2026-04-24_user-panels-fail]]. The
**static-database problem**: data that is never refreshed decays, so the panel
gradually stops saving time. **Panel-sampling bias**: loyal customers skew
feedback positively into an echo chamber that excludes new users and edge cases,
countered by tracking participation history and setting rotation practices — the
same warning appears as a panel skewed toward loyal customers and fans
[[2023-05-07_research-participant-database]]. **Business misalignment**: as the
company enters new markets or shifts segments, a panel without periodic
strategic review reflects yesterday's audience. Deterioration accumulates rather
than arriving at once, so watch declining response rates, repetitive insights
and difficulty finding qualified participants; governance matters more than the
existence of the panel, and panels should be treated as long-term systems rather
than recruiting shortcuts [[2026-04-24_user-panels-fail]].

### Employees as participants

Employees are cheap and convenient and systematically biased: they know the
company jargon, the business goals and the project, feel obliged to complete
tasks, and may fear disappointing the designers
[[2016-09-04_employees-user-test]]. Yahoo! research found employees rated their
own company's site 2% higher than external users did, while external users rated
it 15% lower than competitors — both preference and performance data were
skewed [[2016-09-04_employees-user-test]]. Legitimate uses are narrow: testing
intranets, where employees *are* the target audience; pilot tests to find
methodology flaws; and skunkworks demonstrations of UX value in organisations
that lack UX maturity, preferring employees with minimal project knowledge
[[2016-09-04_employees-user-test]]. Otherwise external recruitment is the only
reliable method, and acting on biased employee data risks spending time and
money without serving the actual audience — worse, inconclusive results can gain
false credibility because they come from trusted colleagues
[[2016-09-04_employees-user-test]].

### Overrecruiting against no-shows

Roughly one in nine recruited users fails to show up
[[2019-04-28_usability-testing-minors]], and every lost participant in a small
qualitative sample removes a substantial share of the potential insight
[[2020-10-04_recruit-backup-users-in-research]].
[[2016-11-04_ux-research_08-chapter-7-recruiting]] treats scheduling backup
participants as expected practice given how common no-shows are: a backup may
cover multiple sessions and is compensated similarly to the regular
participants. Overrecruiting is described as
buying optional insurance, and three models are given
[[2020-10-04_recruit-backup-users-in-research]]:

| Model | How it works | Cost for 5 users | Risk |
|---|---|---|---|
| One floater per participant | Two people booked per slot; the floater is released and paid the full honorarium if the scheduled person arrives | $1,800 vs $900 | Lowest |
| One floater per two participants | The floater covers two sessions, paid double if they cover both | $1,640 vs $900 | Moderate |
| Extra sessions | Schedule more sessions than needed (5 + 2); cancel the surplus but pay the participants | $1,260 vs $900 | Highest, and slowest (1.5 days vs 1) |

Floaters are worth it when the schedule allows only a narrow window, when
external constraints (rented equipment, lab availability) impose time limits,
when background must be screened on site, or when observers need to see
particular sessions for buy-in [[2020-10-04_recruit-backup-users-in-research]].
Recruit them honestly with the same screening criteria as the main
participants, tell them what the role is, frame it as insurance against
cancellations, and dismiss them professionally without implying they did
something wrong; if both people show, the floater can be used to pick the
better-fit participant [[2020-10-04_recruit-backup-users-in-research]]. For
unmoderated remote research, one extra per three sessions is enough
[[2020-10-04_recruit-backup-users-in-research]].

### Catching problem participants after recruiting

Remote unmoderated studies attract problem participants more than moderated or
in-person work, and three types recur
[[2020-08-23_problem-participants-remote-unmoderated]]:

- **Outliers** behave differently because they *are* different, not because they
  cheat — different experience level, background or motivation.
- **Cheaters** want the payment and click randomly without attempting the tasks.
- **Professional participants** have seen too many studies and are too attuned
  to researchers' goals; terminology like "kerning", "mental model" or
  "hamburger" gives them away.

Detection depends on the study type: in qualitative work, watch the recordings
for those signals; in quantitative work, start from the metrics — frequency
distributions of task times and success rates, where low success combined with
very fast times strongly indicates cheating, and open-ended responses expose
nonsense keyboard-mashing
[[2020-08-23_problem-participants-remote-unmoderated]]. On removal: exclude
genuinely unrepresentative outliers completely, but an unfavourable reaction to
the design is not by itself a reason to drop someone; for cheaters, remove the
affected tasks or the whole session, and most remote testing tools replace
cheaters for free; professional participants who showed up and participated
should generally be kept, noted in the conclusions, and excluded from future
studies by screening out anyone who participated in the last 0-3 or 0-6 months
[[2020-08-23_problem-participants-remote-unmoderated]].

[[2016-11-04_ux-research_08-chapter-7-recruiting]] names a milder case than an
outright misrecruit: screeners sometimes fail and a "dud" arrives who does not
fit the profile. The session still produces data and may call for adjusting
tactics on the spot, rather than being discarded outright.

### Hard-to-reach populations

High-income participants are hard to contact, busy, and not motivated by typical
incentives; recruitment panels undersample them because the people who register
are looking for extra cash [[2022-05-01_high-income-participants]]. What worked:
word-of-mouth referrals, particularly when an existing contact makes the
introduction rather than the researcher cold-calling, since wealthy people are
wary of being asked for money; identifying participants by profession or
shopping behaviour rather than asking about income directly, which can offend;
remote sessions; flexible scheduling across weeks, evenings and weekends;
minimal presession demands, with no long surveys and consent forms signed during
the session; and either a higher payment or a donation to a cause they care
about [[2022-05-01_high-income-participants]].

### Minors

Recruiting minors adds a parent to every recruitment, raises the no-show rate
because either party can prevent attendance, and requires segmenting by maturity
and interest rather than age alone — the difference between a 7- and a
17-year-old is far more pronounced than between a 37- and a 47-year-old, a
6-year-old can use a trackpad where younger children only manage touchscreens,
and teenagers' interests shift by school grade
[[2019-04-28_usability-testing-minors]]. Recruit a few extra participants
accordingly [[2019-04-28_usability-testing-minors]].

Minors cannot legally give informed consent: you need written consent from a
parent or guardian **and** verbal assent from the child, both
[[2026-02-13_research-minors-consent]]. Assent must be developmentally
appropriate — plain language matched to age, the child understanding what is
being asked and feeling free to decline or stop at any time, with a clear verbal
agreement rather than a nod; never expect a child to read an adult-style consent
form [[2026-02-13_research-minors-consent]]. The consent form covers purpose,
what the child will do, data storage and protection, compensation, the voluntary
nature of participation, and researcher contact details
[[2026-02-13_research-minors-consent]]. Parental presence varies by age: 3-6 may
benefit from a parent positioned behind them and silent, 7-12 are comfortable
with a parent nearby or outside the room, teens are typically fine alone
[[2026-02-13_research-minors-consent]].

On compensation the two sources agree in direction and differ in detail. One
recommends age-appropriate incentives — gift cards, small toys or stickers
appeal more to young children than cash, and parents may control monetary
incentives, so offer tangible items too [[2019-04-28_usability-testing-minors]].
The other splits it explicitly: parents receive the monetary compensation for
their time and effort, children aged 9+ receive small gift cards, and children
aged 3-8 choose from pre-approved toys [[2026-02-13_research-minors-consent]].

### Recruiting for longitudinal studies

Diary studies suffer from forgetfulness, dwindling interest, fatigue and
dropout, and recruitment is the first defence
[[2023-01-29_better-diary-studies]]. State the time commitment clearly in the
recruitment material and use screener questions to confirm participants
understand and accept the effort, including open-ended questions that gauge both
commitment and comfort with writing [[2023-01-29_better-diary-studies]].
Onboarding — a pre-study brief walking through the tool, the procedure, what a
helpful entry looks like, the incentive structure and the conditions for
withdrawal — builds rapport and prevents dropout from technical confusion
[[2023-01-29_better-diary-studies]]. Keep entries under 15 minutes, maintain
contact with reminders and thanks without overwhelming people, and expect
dropouts when sizing the recruit [[2023-01-29_better-diary-studies]].

Incentives here compensate **effort**, not time, since compensation is tied to
the quantity and quality of submissions rather than to hours in a session
[[2026-06-19_diary-study-incentives]]. Three structures, each with a distinct
side effect [[2026-06-19_diary-study-incentives]]:

- **Payment for a minimum number of entries** — simplest to administer, but
  participants submit exactly the minimum and may cluster submissions at the
  start or end rather than spreading them; best for shorter studies.
- **Pay per entry** — motivates more submissions and rewards those with more to
  share; best for effortful entries such as video or photos; risks low-effort or
  fabricated submissions without controls.
- **Tiered pay per entry** — different rates for different entry types, useful
  when certain events matter more, but needs more explanation and tracking.

Bonus payments can reward consistency, completeness or responsiveness
[[2026-06-19_diary-study-incentives]], [[2023-01-29_better-diary-studies]].
Payment cadence matters as much as amount: a lump sum at the end suits short
studies, while weekly or biweekly intervals encourage ongoing engagement in
longer ones, at the cost of administrative work
[[2026-06-19_diary-study-incentives]]; the same argument appears as splitting
the total into milestone instalments (for example after three days of logging)
to keep motivation up [[2023-01-29_better-diary-studies]]. There is no single
best structure — the right one is whichever meets the study's priorities and
yields the data needed — and it must be communicated clearly so participants are
not confused or disappointed [[2026-06-19_diary-study-incentives]]. One source
notes the opposite risk: some participants conclude the reward is not worth the
work and drop out [[2023-01-29_better-diary-studies]].

## Sources (22)

- [[2016-09-04_employees-user-test]] — Provides clear guidance on when internal recruitment is appropriate (intranets, pilots, skunkworks demonstrations) versus when external recruitment is essential for valid findings.
- [[2019-04-28_usability-testing-minors]] — Recruiting minors involves parents; no-show rates are higher; segmentation by maturity rather than age alone produces more relevant findings.
- [[2019-07-14_screening-questions-select-research-participants]] — effective recruitment uses open-ended questions for authenticity and distractor answer choices for covert evaluation; combined approaches prevent bias and ensure participant-audience alignment.
- [[2020-08-23_problem-participants-remote-unmoderated]] — Proper screening involves watching qualitative recordings and analyzing quantitative metrics to identify participants whose behavior or performance is not representative of the target user population.
- [[2020-10-04_recruit-backup-users-in-research]] — Strategic overrecruiting using floaters or extra sessions protects research schedules against no-shows and cancellations, ensuring adequate data collection while balancing costs.
- [[2021-11-07_recruiting-screening-research-candidates]] — Screeners are questionnaires that gather information to identify optimal candidates and exclude poor fits for studies.
- [[2022-05-01_high-income-participants]] — strategies for recruiting wealthy individuals who have different constraints and motivations than general populations.
- [[2022-11-27_demographics-in-ux]] — screening questions (those determining eligibility) should appear early to avoid wasting participants' time; non-screening demographics belong at survey end.
- [[2023-01-29_better-diary-studies]] — Recruiting well-matched participants with clear commitment expectations and realistic time estimates is the foundation for successful diary study completion, with incentive timing and structure directly influencing engagement; interval payments and tiered or per-entry compensation models outperform single end-of-study payments for longer studies.
- [[2023-05-07_research-participant-database]] — Strategies for finding and enrolling research participants, including internal panels that reduce costs compared to external recruiting services.
- [[2024-11-01_screening-participants]] — Discusses how screeners are the best way to recruit the right participants for research studies and ensure representative sampling of the target audience.
- [[2025-04-11_usability-data-in-analysis]] — highlights how misrecruitment (professional participants, coworkers) or unrepresentative sampling undermines appropriateness and limits insight generalizability.
- [[2025-10-10_screener-foils]] — Addresses the full recruitment toolkit: foils are one safeguard; combine with open-ended questions, consistency checks, and live-session validation for comprehensive misrecruit prevention.
- [[2026-02-13_research-minors-consent]] — Recruiting minors involves navigating legal, developmental, and emotional considerations; transparency and fairness are essential.
- [[2026-04-24_user-panels-fail]] — Panel-based recruitment accelerates studies and reduces costs but requires active ownership and regular maintenance to prevent deterioration and ensure continued effectiveness.
- [[2026-05-01_selection-criteria]] — Rigorous screening prevents misrecruitment by focusing on behavioral and attitudinal criteria that predict meaningful participation; screening quality determines whether gathered data reflects real user experience.
- [[2026-06-19_diary-study-incentives]] — Incentive structure shapes participation behavior; cash incentives are most flexible; timing and amount both influence engagement and data quality.
- [[2013-08-01_just-enough-research_04-chapter-3-the-process]] — the chapter emphasizes that good recruiting is central to research quality; a screener survey with behavioral and skill-based questions identifies better-matched participants than demographics alone.
- [[2013-08-01_just-enough-research_06-chapter-5-user-research]] — the chapter calls recruiting and screening the most time-consuming and least informative aspect of user research, and warns that one bad recruit can tank an entire focus group session, whereas in one-on-one interviews that recruit at least does not taint the pool.
- [[2013-08-01_just-enough-research_08-chapter-7-evaluative-research]] — Effective recruitment requires that participants share key goals with target users, so they can immerse themselves in test scenarios. Maintain an ongoing database of potential participants. Participants are single-use (bringing them back risks tainting from prior experience), so a good supply is essential. Recruiting for usability testing is substantively the same as recruiting for ethnographic interviews.
- [[2016-11-04_ux-research_08-chapter-7-recruiting]] — identifying, screening, and scheduling research participants through methods ranging from DIY to outsourced recruiting.
- [[2016-11-04_ux-research_10-chapter-9-managing-people-during-research]] — In the chapter's practitioner sidebar, Lis Hubert describes reminding herself of the recruitment data for the person she is about to talk to, then, during the warm-up, noting their communication style, word preferences and posture and mirroring those characteristics back to them, which she says almost always gets even a guarded participant engaged within two or three minutes.
