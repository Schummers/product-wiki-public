---
type: concept
name: Privacy
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Data Privacy"
  - "Data Protection"
  - "GDPR"
  - "Privacy Design"
  - "Privacy and AI Systems"
  - "Privacy and Security"
  - "RGPD"
  - "Trust and Privacy"
  - "User Privacy"
---

# Privacy

## Definition

Privacy in this corpus covers two distinct obligations that share a principle.
The first is privacy toward users of a product: how much personal data a system
collects, what it visibly does with it, and how much say people have in that.
Users are not passive here — they run an explicit cost-benefit analysis, weighing
the loss of privacy against the perceived benefit and adopting or refusing on
that basis, which is the creepiness–convenience tradeoff
[[2019-06-02_creepiness]]. The second is privacy toward research participants:
protecting the rights, well-being, and dignity of the people who take part in
studies, before, during, and after data collection
[[2019-12-29_user-research-ethics]], [[2022-09-04_privacy-and-security]].

The shared principle is that privacy is a right of the person whose data it is,
not a compliance checkbox. Cookie-permission overlays should not be treated as
only a legal requirement but as an opportunity to build trust
[[2023-11-10_cookie-permissions]]; the data collected in a study is valuable to
researchers but more important to participants
[[2022-09-04_privacy-and-security]]. Also recurring: perception matters as much
as fact. Users form privacy judgments from what they see displayed, so an
interface can create the impression of a leak without any leak occurring
[[2026-05-08_designing-ai-agents]].

## Practice

### The creepiness–convenience tradeoff

Privacy concerns are outweighed only when the product offers genuine perceived
utility; vague promises of a "better experience" do not convince cautious users
[[2019-06-02_creepiness]]. Initial unease often wears off with exposure,
familiarity, and seeing others use the technology, until people cross their
personal acceptance threshold. That threshold varies: some users are indifferent
to the risk, some firmly opposed, and others come round gradually as value is
demonstrated; the source names digital voyagers, comfortable trading data for
convenience, and digital pragmatists, wary of fraud and privacy. Culture shifts
it too, with collectivist cultures such as China showing lower creepiness
thresholds than individualist ones such as the US and Canada. The design lever
is transparency: explaining what is collected and how it will be used is what
addresses pragmatists' concerns, and revealing benefits progressively is more
persuasive than an upfront appeal [[2019-06-02_creepiness]].

### Tracking that users already accept, and its edges

In the recommendation study, participants were well aware that sites track their
behaviour and were largely accepting of it as a normal cost of the internet and a
fair trade for relevant suggestions, while keeping some reservations about how far
the tracking goes [[2018-09-30_recommendation-expectations]]. They also had
expectations about how the data should be used: explicit actions such as purchases
and saved items should weigh more than passive browsing, since clicking something
does not necessarily signal genuine interest. Note the tension with advertising,
where the same behavioural data pushed further reads as creepy and intrusive — the
tolerance is conditional, not general [[2019-06-02_creepiness]].

Voice assistants sit at the harder end: privacy and trust concerns are named as
major barriers to wider adoption, specifically always-on recording, audio being
transmitted to the cloud, the consequences of a misunderstanding, unauthorized
contact, and smart-home reliability [[2018-08-05_voice-assistant-attitudes]]. The
observed behavioural response is restriction — users confine assistants to home or
to being alone, avoiding public settings, and stick to simple predictable tasks.

### Giving users the controls

Cookie permissions are the concrete case. Regulation (GDPR, CCPA, VCDPA) requires
that users actively opt in to non-necessary cookies, and the design question is
how to offer clear, simple choices without confusing or frustrating people
[[2023-11-10_cookie-permissions]]. Accept, deny, and customize should all be
immediately available rather than hidden behind a "Learn more" step, which makes
users feel pushed; descriptions should use plain, distinguishable language rather
than two options both beginning with "Accept"; deceptive patterns — ambiguous
toggle labels, a high-contrast accept button, a close button that silently accepts
everything — trick users into sharing more than they intended; and the overlay
should stay small and not compete with newsletter or chat overlays. User types
differ, from deniers who configure carefully to impatient users who accept all
just to clear the box [[2023-11-10_cookie-permissions]].

On shared devices, the control users reach for is app-level locking. In India,
where phone sharing among family and friends is culturally normal and children
rarely own their own device, app lockers restrict access to sensitive apps behind
a PIN or pattern, guarding against inadvertent notification exposure, misuse, and
access to financial information, and serving as parental control
[[2016-11-27_app-lockers]]. The social dimension is part of the design: stealth
mode hides the locker's own icon so that borrowers do not read the protection as
distrust, and some users drop the device-level password entirely and rely on the
locker so that lending the phone stays frictionless. The costs are real too — a
password on every access, a separate ecosystem with its own rules, an app that can
be hard to find because it hides itself, and generally poor usability. The same
source notes American users share the underlying worries, accidental disclosure
and misuse, under the same pressure not to seem secretive
[[2016-11-27_app-lockers]].

### Privacy perception in AI agents

When Qwen's agent displayed a user's full home address before an item had even
been selected, participants reacted as though their address had leaked
[[2026-05-08_designing-ai-agents]]. The guidance drawn from it is to surface only
the minimum data required at each step and to explain how that data is used, since
users do not reliably understand how an agent accesses their information. The same
study ties this to autonomy: users want efficiency without losing control, and
withheld information — pricing, fees, minimum order values, baggage allowances —
causes abandonment, while agents that keep users informed retain long-term trust
[[2026-05-08_designing-ai-agents]]. It also records a structural point: platforms
that already own delivery, payments, and behavioural data can build agents that
anticipate requests in ways unbundled competitors cannot, which is a privacy
consideration as much as a competitive one.

### Research: consent and study design

Research ethics is defined as careful consideration of the rights, well-being, and
dignity of the people involved, applying to study design, conduct, and post-study
use of the data [[2019-12-29_user-research-ethics]]. Informed consent means
sending consent forms and information sheets in advance, explaining the research in
plain language, providing contact details for questions, and stating that
participation is voluntary. Special populations need specific handling: guardian
consent plus the child's own assent for minors, and adapted consent forms for low
literacy, cognitive impairment, and visual impairment. Sensitive topics require a
design review before the research runs, specific training, desk research on
protection strategies, and a design that mitigates distress
[[2019-12-29_user-research-ethics]].

Whether to use participants' real data in usability testing is a judgement call.
Do not require it by default: fake but realistic data usually suffices for
quantitative testing, and qualitative testing should be assessed case by case
[[2016-01-24_users-real-data]]. The argument for real data is that watching people
type their own information surfaces more varied interface problems than everyone
entering the same fake record, producing more robust qualitative findings. Where
it is used, confirm willingness during recruiting with a clear explanation of how
the data will be used and protected, especially for financial or health
information, and offer workarounds for hesitant participants, such as a gift card
instead of a personal credit card or a budget scenario instead of real finances
[[2016-01-24_users-real-data]].

For cold calls, the constraint is regulatory: customer data may only be used in
strict compliance with GDPR and the user's own communication preferences, and if
the call is to be recorded, explicit consent must be collected within the first
thirty seconds
[[2024-11-12_351_Les_cold_calls,_méthode_d_UX_Research_-_Guide_pratique]].

### Research: handling the data afterward

Distinguish confidentiality (data kept private but still linked to the
participant's identity) from anonymity (data unlinked from identity), and treat
encryption as the mechanism that makes data unreadable in transit and in sharing
[[2022-09-04_privacy-and-security]]. The six practices given span the lifecycle:
establish data-management guidelines before any study, covering consent forms,
storage, sharing, breach response, and deletion, and update them as laws change;
build a collection plan aligned with privacy regulation such as GDPR; obtain
informed consent; maintain anonymity through analysis and reporting; share files
securely with only the people who need them; and delete the data once it is no
longer needed [[2022-09-04_privacy-and-security]].

The operational details: justify every piece of identifiable data before
collecting it, since unnecessary identifiers add breach risk without benefit;
choose secure tools up front rather than fragmenting across platforms, and avoid
public cloud storage such as Google Drive or Dropbox for sensitive material in
favour of secure file transfer; never put participant names in notes or file
names; pause recording while participants enter passwords or addresses; blur or
delete identifying content from video and audio; and keep consistent naming
conventions and storage locations precisely so that data can be found and deleted
later, deletion being one of the strongest protections available and something
that should happen automatically at study close
[[2022-09-04_privacy-and-security]]. Remote studies raise the stakes, since
third-party tools and online platforms increase breach exposure and researchers
must assess tool security and retain control over storage and sharing. The stated
ambition is that applying all this should not add work, which is why it belongs in
ResearchOps workflows rather than in each researcher's head
[[2022-09-04_privacy-and-security]].

The usability-testing article adds the in-session and post-session gestures: blur
personal information in highlight videos and in report screenshots, clear browser
data in front of the participant after the session, and let participants take away
or shred any printed material containing their information
[[2016-01-24_users-real-data]].

### Making it institutional

Ethical maturity is described as organizational rather than individual: a code of
conduct, ethics training for every researcher at onboarding, written guidance
documents, standardized consent forms, designated ethics experts, and formal
data-protection and data-retention policies, with a self-assessment across six
dimensions to find the gaps [[2019-12-29_user-research-ethics]]. The article's own
framing of the difficulty is worth keeping: the basics are fairly easy and mostly
require awareness of the issues and an agreement to do no evil
[[2019-12-29_user-research-ethics]].

## Sources (10)

- [[2016-01-24_users-real-data]] — central to the guidance on consent, data protection, and post-session data handling.
- [[2016-11-27_app-lockers]] — App lockers address privacy concerns in shared-device contexts by enabling selective access control to sensitive apps and data.
- [[2018-08-05_voice-assistant-attitudes]] — major barriers to expanded assistant adoption, with users expressing concerns about data collection, security, and the reliability of delegated actions.
- [[2018-09-30_recommendation-expectations]] — users' acceptance of personal data tracking as a necessary cost for receiving relevant recommendations, though they maintain some concerns about the extent of tracking.
- [[2019-06-02_creepiness]] — Users perform explicit cost-benefit analyses when asked for personal data; technology must offer genuine value to overcome privacy concerns.
- [[2019-12-29_user-research-ethics]] — addresses storage, retention, and security practices for protecting participant data throughout research process.
- [[2022-09-04_privacy-and-security]] — Protecting participant data throughout research requires proactive practices before collection (justifying identifiable data, using secure tools, avoiding cloud storage for sensitive data), security during analysis (maintaining anonymity), and deletion afterward; privacy is a participant right and ethical obligation.
- [[2023-11-10_cookie-permissions]] — cookie permission designs are a critical way websites communicate respect for user privacy and data control.
- [[2024-11-12_351_Les_cold_calls,_méthode_d_UX_Research_-_Guide_pratique]]
- [[2026-05-08_designing-ai-agents]] — Users form privacy perceptions based on what they see displayed; agents must explain data access clearly and surface only minimum required information at each step to prevent false impressions of data leakage.
