---
type: concept
name: Research Ethics
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Informed Consent"
---

# Research Ethics

## Definition

Research ethics is the careful consideration of the rights, well-being and
dignity of the people involved in research activities, applying to how a study is
designed, how it is conducted, and what happens to the data afterwards
([[2019-12-29_user-research-ethics]]). The sources ground it in a small set of
principles — avoid harm, respect dignity, act with integrity, maintain
confidentiality ([[2016-05-29_team-members-user-test]]) — and in a duty of care
that outranks the study's own goals: when sensitive information is accidentally
captured, it must be removed even at the cost of evidence the team wanted
([[2023-04-23_ethical-dilemmas]]). Informed consent is the mechanism that carries
most of this weight, defined as a two-sided exchange in which the researcher
informs the participant of what participation involves and its consequences, and
the participant understands the terms and agrees voluntarily
([[2022-07-03_informed-consent]]).

The corpus stresses that this matters precisely because UX research is not
clinical research and therefore feels low-stakes: lean methods have put research
in the hands of practitioners without formal research training, who may cut
corners that harm participants ([[2019-12-29_user-research-ethics]]), and even
non-clinical sessions can cause temporary hardship or distress
([[2022-07-03_informed-consent]]). The same reasoning is extended beyond research
sessions to the product itself, where a permission request that does not explain
what access is being granted and why fails informed-consent principles and may
breach GDPR ([[2019-04-28_permission-requests]]).

## Practice

### Building ethical maturity into the organisation

[[2019-12-29_user-research-ethics]] treats ethics as an organisational capability
rather than an individual virtue, and lists what a mature setup contains: a code
of conduct, ethics training for every researcher at onboarding, written guidance
documents accessible to all, standardised consent forms, designated ethics
experts, and formal data policies. It offers a self-assessment checklist across
six dimensions to locate gaps. On sensitive topics it requires design review
before the research runs, special training, desk research on protection
strategies, and study design that mitigates distress. Its own framing of the bar
is modest — the basics require awareness of the issues and an agreement to do no
evil.

[[2022-09-04_privacy-and-security]] makes the same argument for privacy work,
recommending that these practices be folded into existing ResearchOps workflows
so privacy is managed at scale without adding burden to individual researchers.

### Informed consent

[[2022-07-03_informed-consent]] sets out the form's role: it documents the
exchange, guarantees every participant receives the same information, holds
researchers accountable, and lets participants protect their own welfare and
data. It notes the historical basis for the principle (the Nuremberg trials, the
Tuskegee syphilis study) and the review boards most institutions maintain. Two
practical points: some formats such as A/B tests and intercept studies may not
require a full consent form, though even intercept studies need a brief
information page covering data use, storage and deletion; and modular consent —
separate checkboxes for participating, audio recording, video recording and
publication — raises participation compared to all-or-nothing consent.

[[2019-12-29_user-research-ethics]] adds procedural detail: send consent forms
and information sheets in advance, explain the research in plain language, give
participants contact details for questions, and tell them participation is
voluntary. [[2023-04-23_ethical-dilemmas]] restates the principle as disclosure
of all aspects of the study so the person can decide, and identifies the tension
it creates with study validity.

[[2016-11-04_ux-research_07-chapter-6-logistics]] describes the paperwork that
carries consent in practice: nondisclosure agreements to prevent leaks,
recording waivers documenting permission to record sessions, and
permission-to-quote forms which the chapter calls not required but a courtesy,
so people understand how their words may be used. It also notes that some
people don't like to be recorded, and that the response is to show the
participant the recording devices are put away and proceed with the session.
It adds a compensation-side counterpart to the same accountability logic:
honorariums should be confirmed with a receipt, which documents that
participants actually received what they were promised and prevents later
disputes.

### Concealment, deception and debriefing

[[2023-04-23_ethical-dilemmas]] distinguishes the two and ranks them: deception,
which supplies false information, is riskier than concealment, which withholds;
both require debriefing afterwards; and it states that UX studies rarely need
either. [[2016-05-29_team-members-user-test]] applies the same standard to the
small lies teams are tempted to tell during sessions — do not lie about
observers, one-way mirrors, or recording. White lies look harmless but erode
trust; the better move is to acknowledge openly that usability testing feels
unnatural and be transparent about the setup.

UX consultant Kyle Soucy, in a practitioner interview in
[[2016-11-04_ux-research_12-chapter-11-facilitating-research]], extends the
same discipline to the facilitator's own reactions: conceal any judgment,
disgust, or surprise when a participant shares something sensitive or
shocking, and stay neutral and unbiased so the participant feels safe to
continue. The chapter adds that what counts as respect or offense varies by
culture, so this awareness has to extend across cultural context too.

### Protecting the participant during the session

[[2016-05-29_team-members-user-test]] catalogues the ways well-meaning colleagues
create ethical problems, with a rule for each. Participants must always be free
to take a break or leave, and coercing someone to stay is unethical and probably
illegal — besides which a disengaged participant taints the findings. Pay the
full incentive even when a recruitment error produced a poor-fit participant,
since they gave their time and short-paying damages future recruitment. Do not
let managers observe their direct reports; anonymise findings and ensure no link
to performance reviews. Set observer etiquette in advance — testing is about
receiving feedback, not giving it, so observers stay silent until the end — and
cap in-room observers at three, broadcasting to another room if more want to
watch, with participants told about observers beforehand. When a user struggles,
reframe it as an interface failure rather than user incompetence, which also
stops name-calling within the team.

[[2016-11-04_ux-research_10-chapter-9-managing-people-during-research]] gives a
related tactic for workplace settings, where employees may worry the research
is a pretext for job cuts: frame the study's purpose explicitly (for example,
"I'm here to make your job easier by understanding how you approach your
work"), emphasise anonymity, and offer "off the record" moments so participants
do not fear job security or other negative consequences.

[[2023-04-23_ethical-dilemmas]] adds that sensitive-topic research needs
subject-matter-expert guidance, explicit informed participation, a clear
withdrawal option, and access to support resources.
[[2024-08-09_sensitive-questions]] covers the survey and screener equivalent: a
sensitive question is one respondents may find embarrassing or invasive, and it
costs data quality — income is ten times more likely to be left blank than other
demographic questions. Its guidance is to emphasise confidentiality, place
sensitive and demographic questions at the end after rapport has been built
rather than at the start, offer ranges (income brackets, age brackets, frequency
options) instead of exact values, and load questions with context that normalises
potentially shameful behaviour, or use indirect techniques such as the item-count
method. It insists demographic questions on age, gender, race and income be
worded inclusively, without assumptions, and includes a participant quote about
the recurring distress such forms cause trans respondents.

### Vulnerable populations, consent and assent

[[2022-07-03_informed-consent]] names those who may be unable to consent for
themselves — children, cognitively impaired adults, people with low literacy,
prisoners — and requires guardian consent in their place, plus extra precautions
and clear communication about potential impact. [[2023-04-23_ethical-dilemmas]]
adds people with dementia and those who might face discrimination, and requires
informed consent from legal representatives.
[[2019-12-29_user-research-ethics]] specifies guardian consent plus child assent
for children, and specialised consent forms for low literacy, cognitive
impairment and visual impairment.

[[2026-02-13_research-minors-consent]] develops this into a full procedure.
Minors, generally those under 18, cannot legally consent, so ethical research
needs both written parental or guardian consent and verbal assent from the child:
consent is legally binding permission from an informed, competent adult, assent
is affirmative agreement from someone who cannot legally consent but can indicate
willingness. Assent must be developmentally appropriate — never expect a child to
read an adult consent form; speak to them directly and respectfully, in plain
language matched to their age, explaining what you are doing, what they will do,
and that they can stop at any time, and look for clear verbal agreement rather
than a nod. The consent form must cover purpose, what the child will do, data
storage and protection, compensation, voluntariness, and researcher contact
details. Parental presence varies with age: 3–6 may benefit from a parent nearby,
positioned behind and silent; 7–12 are comfortable with a parent nearby or
outside the room; teens typically participate alone. Compensation should be fair
and age-appropriate — money to parents for their time and effort, small gift
cards for children of 9 and over, a choice from pre-approved toys for ages 3–8.
The source also argues the inclusion case: research with minors surfaces real
usage patterns and usability issues for non-readers, and makes products safer and
more age-appropriate.

### Data privacy across the research lifecycle

[[2022-09-04_privacy-and-security]] organises the work into six practices:
establish data-management guidelines before any study (covering consent forms,
storage, sharing, breach response and deletion, communicated to the whole team
and updated as laws change); build a data-collection plan aligned with
regulations such as GDPR; obtain informed consent; maintain anonymity through
analysis and reporting; share files securely with only the people who need them;
and delete data once it is no longer needed. It separates confidentiality (data
kept private but still linked to an identity) from anonymity (data unlinked), and
explains encryption as scrambling data so it is unreadable in transit. Concrete
rules: justify every piece of identifiable data before collecting it, since
unnecessary identifiers add breach risk without benefit; choose secure tools up
front to avoid fragmentation across platforms and avoid public cloud storage such
as Google Drive or Dropbox for sensitive data, using secure file transfer
instead; never put participant names in notes or file names; pause recording
while participants enter passwords or addresses, and blur or delete identifying
material from audio and video; and keep consistent naming conventions and storage
locations so data can actually be found when it is time to delete it. Deletion is
described as one of the best privacy protections and should happen automatically
at the end of a study.

[[2019-12-29_user-research-ethics]] converges on the same points from its
checklist: data-protection and retention policies, prompt deletion of personal
data, secure storage with restricted access, and collection on encrypted,
password-protected devices.

[[2023-04-23_ethical-dilemmas]] raises a case the privacy practices cannot fully
solve: in a small participant pool, anonymity may be impossible, and the honest
response is to tell participants they could be identified rather than promise a
confidentiality that cannot be delivered.

### Consent beyond the research session

[[2019-04-28_permission-requests]] carries the informed-consent standard into
product design. Users perform a cost-benefit analysis on a permission request,
weighing the feature against privacy and trust concerns, and vague requests fail
informed consent and may violate GDPR. Its findings: giving a reason made users
12% more likely to grant permission, and framing that reason around user benefit
rather than system need increased grants by 81%; explain what the user gets
("scan travel documents quickly") rather than what is accessed ("access to
camera"), which reads as suspicious. Timing matters — a request triggered by the
user tapping a camera icon is expected, while one fired at app launch causes
surprise and needs extra explanation. On Android, where the dialog does not
support purpose strings, a context screen must precede the request for consent to
be informed. And permission decisions must be reversible: explain clearly why
functionality is unavailable and link directly to the settings.

## Sources (12)

- [[2016-05-29_team-members-user-test]] — The article applies core ethical principles (avoid harm, respect dignity, act with integrity, maintain confidentiality) to specific testing scenarios.
- [[2019-04-28_permission-requests]] — Users must understand what access they're granting and why; vague requests fail to meet informed consent principles and may violate GDPR.
- [[2019-12-29_user-research-ethics]] — Ethical user research requires a comprehensive framework across all study phases, emphasizing voluntary, informed participation with clear communication about study purposes and data use.
- [[2022-07-03_informed-consent]] — Informed consent is a core ethical principle ensuring researchers respect participant wellbeing and autonomy rather than exploiting their willingness to help.
- [[2022-09-04_privacy-and-security]] — Data privacy is fundamental to research ethics; researchers must respect participant involvement by protecting data, following informed consent principles, and informing participants about data collection, usage, and protection measures—ensuring participants understand how their data will be handled and approve such practices.
- [[2023-04-23_ethical-dilemmas]] — The principles and practices ensuring that user research protects participant autonomy, safety, and dignity through informed consent and safeguard measures, including ensuring participants understand what the study involves and receive disclosure of research goals and organization before agreeing to participate.
- [[2024-08-09_sensitive-questions]] — emphasizes participant dignity, informed consent, and protecting research participants from emotional harm.
- [[2026-02-13_research-minors-consent]] — Research with minors requires extra ethical care, legal compliance, and respect for both child autonomy and parental authority.
- [[2013-08-01_just-enough-research_03-chapter-2-the-basics]] — The chapter outlines informed consent, confidentiality, safety, honesty about study purpose, and the principle that the project itself must be ethical—good methodology does not justify harmful outcomes.
- [[2016-11-04_ux-research_07-chapter-6-logistics]] — the consent paperwork the chapter groups together: NDAs, permission to record, and permission to quote (the last one not required, offered as a courtesy so people understand how their words may be used); participants may refuse recording, and are asked to sign a receipt for their honorarium.
- [[2016-11-04_ux-research_10-chapter-9-managing-people-during-research]] — The chapter suggests a practical way to protect participant anonymity, allow "off the record" moments, and frame the research's purpose so participants do not fear job security or other negative consequences.
- [[2016-11-04_ux-research_12-chapter-11-facilitating-research]] — UX consultant Kyle Soucy, in the chapter's practitioner interview, describes concealing any judgment, disgust, or surprise when a participant shares something shocking — not raising her eyebrows, scrunching her brow or wrinkling her nose — because a UX researcher must remain neutral and unbiased; she also watches the participant's own body language and facial expressions and, the moment she senses unease, asks how they are doing and reminds them they can stop at any time. The chapter itself adds that what counts as respect or offense varies by culture, so this awareness needs to extend across cultural context too.
