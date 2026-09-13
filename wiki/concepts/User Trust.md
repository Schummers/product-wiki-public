---
type: concept
name: User Trust
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Trust"
  - "Trust Building"
  - "Trust and Credibility"
  - "Trust and Verification"
  - "User Trust and AI"
---

# User Trust

## Definition

User trust, across these sources, is the confidence and willingness of a person
to engage with a product or company, and it is earned incrementally rather than
assumed. The organising model is a hierarchy: like Maslow's pyramid, a user-site
relationship climbs five levels of commitment — baseline relevance and
credibility, interest and preference, willingness to give personal information,
willingness to give sensitive or financial information, and willingness to
commit to an ongoing relationship — where each level requires the ones beneath
it to be satisfied first. Skepticism is the default state; users start "in the
sand below the pyramid" and the site must actively induce the climb
[[2016-03-06_commitment-levels]].

The mechanisms that build trust are consistent across the corpus: design quality
that signals competence, upfront disclosure of costs and policies, comprehensive
and current content, and visible connection to third-party validation
[[2016-05-08_trustworthy-design]]. The mechanisms that destroy it are equally
consistent: hiding information, forcing commitment before delivering value, and
deceptive patterns that steer users against their own interests
[[2023-12-01_deceptive-patterns]] [[2024-10-04_sneaking]]. With AI systems the
concept shifts from earning trust to calibrating it — the problem becomes users
trusting outputs they have not verified, and the design goal becomes accurate
expectations rather than maximum confidence [[2023-09-24_generative-ai-diary]]
[[2026-01-09_humanizing-ai]].

## Practice

### Match demands to the level of trust already earned

Keep the site's requests and the user's trust needs in equilibrium: do not ask
for email, phone number or payment before establishing that the site is
relevant, credible and preferable to alternatives. Login walls are the canonical
violation, skipping levels 1 and 2 and causing abandonment before trust can
build. Use low-friction signals early instead — descriptive taglines, social
proof, representative images, free browsing — and let exploration build
confidence and a sense of control [[2016-03-06_commitment-levels]]. The same
guideline recurs in three other contexts: gated content and prominent signup
forms degrade trust even when value is technically provided
[[2016-05-08_trustworthy-design]]; B2B sites should answer basic questions on
How It Works pages, FAQs and forums before requiring sales contact, because
giving value first makes users comfortable reciprocating
[[2019-09-01_b2b-trust-from-b2c]]; and calculator or quiz tools should allow
anonymous use with results shown immediately, since users of these tools are
exploring, not committing [[2024-04-19_recommendations-calculator]].

### Credibility signals

Four factors identified in 1999 were found to still hold, and to hold across
Western and Asian cultures: design quality, upfront disclosure, comprehensive
and current content, and connection to the rest of the web. Concretely — 
well-organized navigation with meaningful unambiguous labels, appropriate colour
schemes (which set expectations of budget, corporate or luxury), adequate white
space, and no typos or broken links. Gaps in representation are themselves a
signal: missing content about certain offerings or customer segments suggests
the company undervalues them. Because people have learned to trust review sites
and social media more than company-sponsored content, linking out to external
reviews beats in-house testimonials [[2016-05-08_trustworthy-design]].

Research with Chinese online shoppers, where counterfeit prevalence raises the
stakes, adds market-specific signals on top of the generic ones: users actively
search for the "official website"; local presence (physical stores, local
distributors, visible regional expertise) makes an organization feel tangible
and accountable in a way a pure online presence cannot; detailed before-and-after
photos, testimonials with direct contact information and client logos carry
weight; and online chat is preferred over phone, with evasive answers from
representatives damaging credibility. A halo effect operates in reverse: a
single poorly produced element, such as a low-quality video, can undermine an
otherwise well-designed site [[2017-09-03_credibility-china]].

### Removing uncertainty in high-stakes purchases

An account of buying a sofa online shows confidence being built by eliminating
uncertainty at each decision point: break the complex choice into sequential
single-attribute steps (style, then fabric, then colour); explain domain jargon
with illustrations rather than text; caption every product image with the exact
configuration shown; offer free fabric swatches so tactile qualities can be
judged offline; show real customer photos in lived-in rooms for scale; list
granular, labelled dimensions; and keep communicating after the purchase. The
underlying instruction is to find out what people need to know before they are
comfortable buying, and prepare answers to those specific questions
[[2017-06-18_ux-design-ecommerce]].

B2B carries the same logic under different constraints — high switching costs
and purchases requiring multiple internal approvals. Show prices, or at least
starting prices and ranges: hiding them increases interaction cost, creates
sticker shock and gives the impression something is being concealed. Explain
what can and cannot be customized, present tiers in comparison tables with
consistent feature ordering, address switching costs directly with migration
assistance or fee coverage, and supply case studies, demos and free trials so
the buyer can defend the decision internally. Clear copy reads as honest;
convoluted writing is met with skepticism [[2019-09-01_b2b-trust-from-b2c]].

### Asking for data and permissions

Users run an explicit cost-benefit analysis when asked for personal data,
weighing privacy loss against perceived benefit — the creepiness–convenience
tradeoff. Vague promises of a "better experience" rarely convince; the benefit
has to be genuine and perceived. Uneasiness often wears off with exposure and
familiarity, tolerance varies by individual ("digital voyagers" versus "digital
pragmatists") and by culture, and transparency about what is collected and how
it is used is what helps the cautious group cross the threshold
[[2019-06-02_creepiness]].

For mobile permission requests specifically: give a reason (users were 12% more
likely to grant permission when given one, and 81% more likely when the reason
focused on user benefit rather than system need); time the request so it is
expected, triggered by the user's own action rather than fired at app launch;
frame it as an outcome ("scan travel documents quickly") not an access grant
("access to camera"), because users are highly skeptical of vague promises and
suspect them of covering nefarious schemes; add explanation screens on Android,
which has no purpose strings; and make it easy to reverse a refusal later
[[2019-04-28_permission-requests]].

### Deception as the fastest way to lose trust

Deceptive patterns prompt users into actions that benefit the company by
deceiving, misdirecting, shaming or obstructing. The recognised forms are
obstruction, visual tricks, nagging, emotional manipulation and sneaking. The
distinguishing test against legitimate persuasive design is threefold: is the
information factually accurate, does the design respect user autonomy, and is
the information easily accessible. Obvious patterns provoke anger in testing
while mild ones go undetected, especially among users with lower literacy, so a
cognitive walkthrough is recommended — asking systematically whether users might
spend more than intended, misinterpret a choice, miss an option, or feel rushed.
The practitioner's stated duty is to straddle business and user interests but to
call deceptive patterns out when proposed [[2023-12-01_deceptive-patterns]].

Sneaking is examined in detail as three practices — forced continuity, hidden
costs, and sneak into basket — each exploiting limited attention. These may
drive immediate growth in sales or subscriptions, but at the cost of long-term
loyalty and reputation once users discover the deception. The prescribed
counter-practice is noncommittal defaults, prices communicated upfront, and
regular subscription notifications; regulation such as GDPR is already turning
these from best practice into requirement [[2024-10-04_sneaking]].

### Trust in AI systems: calibration, not maximisation

The AI sources treat trust as something that can be too high as easily as too
low. A two-week diary study of 18 users across three chatbots found average
trustworthiness ratings of 6.00 on a 1–7 scale, yet only 22% of conversations
included any verification — trusting without verifying is called dangerous
precisely because these systems produce incorrect information that sounds
plausible. The recommendation is to lower the interaction cost of checking, by
supplying sources or citations [[2023-09-24_generative-ai-diary]]. A later study
observes a partly different behaviour: users distrust AI on specific data such
as pricing and deliberately ping-pong to traditional search to validate facts
for high-stakes or regulated domains, holding a mental model of AI as helpful
but fallible [[2026-02-27_ai-search-infoseeking]]. Read together, the two
suggest verification behaviour depends on stakes rather than being uniformly
absent, but the sources themselves report different levels of it.

Two further sources address how to earn the right amount of trust:

- **Don't buy it with personality.** Deliberately humanizing an LLM backfires.
  Users already anthropomorphize by default, so added personality is redundant;
  systems designed to be warm or empathetic show 10–30% higher error rates, and
  users who attribute emotional traits to an AI are *less* likely to accept its
  advice. Humanization also raises privacy risk, because users expect the
  confidentiality of a human conversation that the system cannot guarantee.
  Trust comes instead from accuracy, transparency and clear statements of
  limitation, with the system framed as a tool rather than a companion
  [[2026-01-09_humanizing-ai]].
- **Explain per role.** In enterprise settings trust is a prerequisite for
  adoption, and it is built through explainability calibrated to the job each
  role does: governance leads need global, system-level patterns, audit trails
  and compliance documentation; builders need local explanations tied to
  specific inputs and configuration changes; domain experts need plain language
  grounded in familiar policies, workflows and comparable past cases. All three
  are answering the same three questions — is this fair, does it reflect data I
  trust, can I defend it — and when users can question results, compare
  alternatives or test changes, they become active participants rather than
  passive recipients [[2026-07-03_crafting-ai-explanations]].

Algorithm transparency appears outside the AI context too: for calculator tools,
consider exposing how results are computed, and note that users trust such tools
for their perceived reliability and usefulness, not because AI is involved
[[2024-04-19_recommendations-calculator]].

## Sources (15)

- [[2016-03-06_commitment-levels]] — core framework for user-site relationships and persuasion.
- [[2016-05-08_trustworthy-design]] — Trust is built through upfront disclosure, comprehensive content, and visible connection to external validation; lacking any element damages user confidence.
- [[2017-06-18_ux-design-ecommerce]] — establishing confidence through transparency, completeness, anticipated questions, free samples, real-world photography, and post-purchase communication.
- [[2017-09-03_credibility-china]] — in markets with high counterfeit prevalence, organizations must actively demonstrate authenticity through professional production, local presence, and transparent communication.
- [[2019-04-28_permission-requests]] — Clear permission requests that respect user concerns build brand trust; dark patterns that obscure choices erode trust and may drive users to competitors.
- [[2019-06-02_creepiness]] — Transparent communication about data use and trustworthy brand reputation help users become comfortable with privacy-invasive features.
- [[2019-09-01_b2b-trust-from-b2c]] — B2B sites build trust through transparency (pricing, customization, policies), providing value upfront, and demonstrating they understand customer concerns and risks.
- [[2023-09-24_generative-ai-diary]] — Users tend to trust AI outputs without verification because checking answers has high interaction cost; this creates risk when bots generate plausible-sounding but incorrect information.
- [[2023-12-01_deceptive-patterns]] — deceptive patterns damage trust and user perception of companies; ethical designs that respect user autonomy build long-term relationships.
- [[2024-04-19_recommendations-calculator]] — discusses how design choices (transparency, no registration requirements, meaningful outputs) build user trust in calculator tools.
- [[2024-10-04_sneaking]] — the confidence and willingness of users to engage with a product or company, which is damaged by deceptive practices and built by transparency and ethical design.
- [[2026-01-09_humanizing-ai]] — Trust in AI grows from accuracy, transparency, and clear limitations—not from personality or emotional mirroring.
- [[2026-02-27_ai-search-infoseeking]] — Highlights the mental model that users hold about AI as helpful but fallible, leading them to verify critical facts through search.
- [[2026-07-03_crafting-ai-explanations]] — is built through calibrated, role-specific explanations that address fairness, data integrity, and accountability concerns before deployment.
- [[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]] — the chapter counts building credibility among the things friction can do when used appropriately, alongside preventing errors, enhancing security and promoting critical thought.
