---
type: concept
name: Deceptive Patterns
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Dark Pattern"
  - "Dark Patterns"
---

# Deceptive Patterns

## Definition

A deceptive pattern is a design pattern that prompts users to take an action
benefiting the company by deceiving, misdirecting, shaming, or obstructing their
ability to make another, less profitable choice [[2023-12-01_deceptive-patterns]].
Originally coined "dark patterns" in 2010, these designs are prolific on the web
because they work: they raise conversions. Their cost is borne by users, in
financial loss, loss of privacy and loss of legal control, and they succeed
disproportionately with vulnerable users, such as time-poor users or those with
lower literacy and digital literacy [[2023-12-01_deceptive-patterns]]. They are
also measurably widespread: a 2019 study of 11,000 shopping websites identified
1,818 instances of dark patterns designed to make users perform unintended
actions against their interests, and popular sites were more likely to feature
them [[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]].

The category is broader than outright lying. It covers manipulation that exploits
attention and cognitive biases rather than false statements: tricking users into
agreeing to something they did not intend [[2024-10-04_sneaking]], structuring a
choice so the wording and layout push one answer [[2019-02-10_interface-copy-decision-making]],
or shaming someone for declining [[2017-04-30_shaming-users]]. Adjacent, milder
practices sit at the edge of the category: needy patterns, which pester users to
lift signup or page-view metrics, are described as less malicious than dark
patterns but similarly manipulative in intent [[2016-05-15_needy-design-patterns]].

## Practice

### The forms deception takes

One source organises deceptive patterns into five mechanisms: obstruction (making
the beneficial choice harder to reach), visual tricks (exploiting cognitive
limitations), nagging (pestering after a user declines), emotional manipulation
(shaming users into a choice), and sneaking (adding items without permission)
[[2023-12-01_deceptive-patterns]]. Sneaking is itself decomposed into three
practices: forced continuity, which highlights a free trial while burying the
ongoing payment terms in small print or delaying billing notifications; hidden
costs, which show a low initial price and reveal the real total only at checkout;
and sneak into basket, which adds items to the cart or prefills consent checkboxes
on the assumption that users will not notice [[2024-10-04_sneaking]].

Copy is a deception surface of its own. Scare tactics that emphasise potential
losses exploit loss aversion and push users toward "protective" options regardless
of their real value; artificial scarcity and time-limited offers force fast
decisions instead of careful evaluation; emotional framing dresses up a mundane
transaction (calling a processing fee a "generous" choice) and distorts the
decision context; and describing options differently from what users can actually
select creates trust and satisfaction problems
[[2019-02-10_interface-copy-decision-making]]. Manipulinks, also called
confirmshaming, are rejection links worded as undesirable self-descriptions ("No
thanks, I hate saving money") so that declining feels bad
[[2017-04-30_shaming-users]].

[[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]] situates these mechanisms inside a wider set of ways digital
products exploit psychological vulnerabilities: variable rewards, infinite
loops, social affirmation, algorithmic personalisation, default settings,
removed friction and reciprocity. Its grounding is B. F. Skinner's
operant conditioning, where variable, unpredictable reinforcement shapes
behaviour most powerfully — slot machines being the modern-day Skinner box, and
pull-to-refresh reproducing both the gesture and the variable reward [[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]]. Two of those levers overlap
directly with the patterns above. Defaults steer behaviour without explicit
consent: a 2011 study found Facebook's default privacy settings matched user
expectations only 37% of the time [[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]]. And removing friction is
not automatically a gain, since friction is also what preserves [[User Control]],
preventing errors and protecting privacy [[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]].

That source also insists the harm does not require bad intent. Facebook's like
button and infinite scroll, Snapchat filters and personalisation algorithms were
not created to cause harm, yet research links social media use to increases in
depression and loneliness in young adults and to a rise in suicide-related
outcomes among adolescents
[[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]].

### Where they concentrate

**Consent and privacy.** Cookie-permission designs are a documented cluster:
toggle switches with unclear labels, high-contrast accept buttons, and ambiguous
close buttons that trigger accept-all instead of deny all trick users into opting
in [[2023-11-10_cookie-permissions]]. Hiding deny or customize behind an extra
click, such as a "Learn more" button, reduces trust and makes users feel pushed
toward accepting everything; and two options both starting with "Accept" defeat
scanning [[2023-11-10_cookie-permissions]]. The same mechanics appear outside the
browser: an LG TV setup presents pre-checked data-collection agreements and
unclear opt-out mechanisms, leaving users feeling forced to accept invasive data
practices, with the device prioritising data collection over its core viewing
function [[2025-09-12_physical-discs-streaming-experience]].

**Subscriptions and checkout.** Real-world sneaking examples are documented at
Spotify, Ticketmaster, Airbnb, GoDaddy and LinkedIn, contrasted with more
transparent handling by Apple and United Airlines [[2024-10-04_sneaking]].

**Paywalls.** A dissection of top App Store monetisation funnels describes a
sequence of aggressive paywalls: a first discounted paywall at the end of
onboarding, and, on refusal, a second one appearing immediately with a heavy
time-limited promotion (-50% to -70%), often coupled with deceptive chance
mechanics such as rigged wheels of fortune offering a "second chance"
[[2025-05-06_376_Designer_un_funnel_de_conversion_paywall_-_Gold_standard_2025]].

**Attention grabs.** Exit popups fire when a user moves to close the tab, on the
assumption they are abandoning the site, and interrupt page-parking behaviour;
get-back-to-me tab titles replace the page title with an attention-seeking
message, destroying the context users rely on to identify their tabs
[[2016-05-15_needy-design-patterns]].

### Telling persuasion from deception

Persuasive design that uses social proof or scarcity is ethical when the
information presented is factually accurate and the exchange is fair; deception
begins when a design hides information or misleads about the choices available
[[2023-12-01_deceptive-patterns]]. Three tests are proposed: is the information
factually accurate, does the design respect user autonomy, and is the information
easily accessible [[2023-12-01_deceptive-patterns]]. A neutral presentation of
options does not exist, so the question is not whether copy influences the
decision but whether it supports an optimal decision or steers users toward one
they will later regret [[2019-02-10_interface-copy-decision-making]]. A blunter
heuristic: if it would be rude to say in person, it is rude in copy
[[2017-04-30_shaming-users]].

### Detecting them

Obvious deceptive patterns trigger visible anger in user testing, but mild ones
escape detection entirely, especially among users with lower education, so
designers cannot rely on testing alone and must scrutinise designs systematically
[[2023-12-01_deceptive-patterns]]. A cognitive walkthrough works for this,
structured around whether users might spend more than intended, misinterpret a
choice, miss an option, or feel rushed or manipulated
[[2023-12-01_deceptive-patterns]].

### The cost, and the disagreement about it

Most sources here converge on the same trade: the pattern wins in the short term
and loses in the long term. A/B tests showing higher micro conversions from
manipulinks may reflect dishonesty rather than cleverness (for instance, not
disclosing that an email signup follows), and the signup gain comes at the cost of
negative brand perception, lower NPS, reduced credibility and lost trust
[[2017-04-30_shaming-users]]. Sneaking drives immediate growth in sales and
subscriptions while sacrificing transparency and damaging loyalty
[[2024-10-04_sneaking]]. Manipulative choice architecture generates immediate
sales but damages long-term loyalty and reputation, and customer satisfaction
matters more than a few conversions [[2019-02-10_interface-copy-decision-making]].
Needy patterns signal organisational desperation and lack of confidence, and are
unlikely to produce lasting conversions [[2016-05-15_needy-design-patterns]].

The paywall analysis takes the opposite stance on the same trade-off, presenting
the aggressive funnel as the 2025 "gold standard" and stating explicitly that the
objective is an efficient sales journey, potentially at the expense of the quality
of the user experience
[[2025-05-06_376_Designer_un_funnel_de_conversion_paywall_-_Gold_standard_2025]].
It is a description of what converts best, not an endorsement of user benefit; the
same source notes that no monetisation strategy compensates for not having a good
product.

Regulation is tightening independently of the ethical argument: deceptive patterns
are increasingly illegal under data protection regulation
[[2023-12-01_deceptive-patterns]], GDPR prohibits prefilled checkboxes and
requires explicit consent [[2024-10-04_sneaking]], and cookie designs must comply
with GDPR, CCPA and VCDPA requirements that users actively opt into non-necessary
cookies [[2023-11-10_cookie-permissions]].

### Designing the honest alternative

Default choices should be noncommittal, leaving people free to make their own
decision [[2024-10-04_sneaking]]. Communicate prices upfront and send regular
subscription notifications, as Apple does [[2024-10-04_sneaking]]. Make accept,
deny and customize immediately available at the same level, use plain language in
cookie descriptions, keep the overlay small enough not to obscure the page, and
avoid stacking competing overlays (cookies, newsletter, chat) at once
[[2023-11-10_cookie-permissions]]. Describe choices truthfully, so that what the
copy promises matches what users can actually select
[[2019-02-10_interface-copy-decision-making]]. In modals, research shows users
prefer a direct, polite pattern (an X button, a plain "No thanks") over
condescending tone and clever rejection language [[2017-04-30_shaming-users]].
Interrupting or annoying users is only recommended when it is in their own
interest, such as preventing someone from closing a file without saving
[[2016-05-15_needy-design-patterns]]. [[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]] turns the same idea into
a positive instruction: embrace friction strategically, to prevent errors,
protect privacy and encourage critical thought, against the assumption that
frictionless always equals good experience.

For the practices that produce those alternatives, [[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]] asks
designers to slow down and be intentional: think beyond the idealised happy-path
use case, build diverse teams so blind spots get caught, and gather qualitative
research by listening to users, all in service of [[Ethical Design]] aligned
with user well-being rather than metrics such as daily active users or time on
site [[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]].

The designer's role is to straddle the needs of the employing business and the
interests of users: call out deceptive patterns when they are proposed or
implemented, and seek fairer ways for both sides to reach their goals
[[2023-12-01_deceptive-patterns]].

## Sources (9)

- [[2016-05-15_needy-design-patterns]] — Needy patterns fall into a similar (though less malicious) category as dark patterns; both use deceptive strategies to manipulate user behavior.
- [[2017-04-30_shaming-users]] — Categorizes manipulinks as deliberately deceptive interface design intended to frustrate users into unwanted actions.
- [[2019-02-10_interface-copy-decision-making]] — Specific deceptive design techniques including scare tactics emphasizing losses, artificial scarcity creation, emotional framing of choices, and mismatches between described and available options.
- [[2023-11-10_cookie-permissions]] — specific deceptive patterns in cookie designs (toggle switches, high-contrast buttons, unclear close buttons) trick users into sharing more data than intended.
- [[2023-12-01_deceptive-patterns]] — the article defines deceptive patterns, their forms (obstruction, visual tricks, nagging, emotional manipulation, sneaking), and legal implications.
- [[2024-10-04_sneaking]] — Interface designs and interactions deliberately crafted to mislead users into unintended actions through dark patterns like sneaking, forced continuity, and hidden costs; these deliberately exploit user behavior and cognitive biases to serve business interests at the expense of user interests.
- [[2025-05-06_376_Designer_un_funnel_de_conversion_paywall_-_Gold_standard_2025]]
- [[2025-09-12_physical-discs-streaming-experience]] — The LG TV example illustrates pre-checked data-collection agreements and unclear opt-out mechanisms that make users feel forced to accept invasive data practices.
- [[2024-01-23_laws-of-ux_14-12-with-power-comes-responsibility]] — identifies dark patterns as prevalent (1,818 instances across 11,000 shopping websites) techniques that make users perform unintended actions against their interests.
