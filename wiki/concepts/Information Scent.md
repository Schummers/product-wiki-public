---
type: concept
name: Information Scent
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Information Foraging"
---

# Information Scent

## Definition

Information scent is the user's imperfect estimate of how relevant a source will
be to their current information need, formed from visible cues before they
commit any time to it — the link label, the text or image accompanying it, the
surrounding context, and any prior knowledge about the source
[[2020-02-02_information-scent]]. It sits inside information foraging theory,
developed at PARC by Peter Pirolli and Stuart Card, which models web navigation
on animal foraging: people try to maximise the rate of information gain over
time, weighing the value of a source against the cost of getting at it. Because
humans cannot estimate benefit and cost precisely, the theory rests on bounded
rationality — satisficing and imperfect heuristics rather than optimal choices
[[2019-11-10_information-foraging]]. This is why people neither scroll mindlessly
nor click every link: high scent signals that a page holds what they need, and
scent varies with the individual need.

The costs foragers weigh are of two kinds: the actual time and effort of
extracting information, and the opportunity cost of the documents they forgo,
which is why users extract gists rather than read deeply
[[2019-11-10_information-foraging]]. The same cost-benefit logic underlies
perceived value — the subjective worth a site has relative to a goal — where
the *perception* of interaction cost weighs as heavily as the real cost in
deciding whether to stay [[2016-04-17_perceived-value]]. Scent is not confined
to links: it is one of the four quality criteria for an icon, namely whether
users can predict what clicking it will do [[2016-02-07_icon-testing]], and its
absence explains why a QR code looks meaningless without accompanying
explanation [[2016-10-16_wechat-qr-shake]].

## Practice

### Write labels that carry the scent

Link labels should be succinct yet accurate descriptions of the destination;
obscure, vague or jargon-filled labels give poor scent and users miss valuable
content, so the language must be self-explanatory and user-centric
[[2020-02-02_information-scent]]. The four-Ss framework makes this operational:
Specific about what users will find (vague "Learn more" links force guessing and
reduce clicks), Sincere in setting expectations that are met immediately on
arrival, Substantial enough to stand alone since users scan and often read only
the links, and Succinct without sacrificing the other three — a link may be long
if it needs to be. First words matter most, so frontload the
information-carrying language [[2019-03-24_better-link-labels]]. In comparison
tables, unexplained jargon produces dense fixation clusters where users pause,
breaking their scanning rhythm; self-explanatory cells and clear terminology
keep it intact [[2020-12-13_lawn-mower-pattern]].

### Do not promise what the click does not deliver

A generic call to action can give strong scent for almost any customer activity
and thereby lead users down the wrong path: "Get Started" is read as an
invitation to learn more or explore, and instead drops people into a signup or
sales funnel before they have the foundational information to commit. Replacing
it with descriptive labels such as "Take our style quiz" or "Switch your cell
plan" sets accurate expectations. A link is a promise: setting the wrong one may
hit superficial conversion goals while losing customer trust
[[2017-08-20_get-started]]. Clickbait works the same way — misleading titles
generate clicks in the short term and erode trust and future click-through in
the long term [[2020-02-02_information-scent]].

### Context and prior knowledge feed the estimate

Summary text, images, and the surrounding page content add cues that help users
judge relevance, but context is often cut off on mobile, so specific labels
matter more than reliance on context. Familiarity with a brand or domain also
shapes how links are read; a brand that consistently delivers on its promises
earns slightly more room for the occasional misstep, though many mistakes
ultimately erode it. Social foraging extends scent outward: recommendations,
reviews and word of mouth are signals other users leave about a source's quality
[[2020-02-02_information-scent]].

Title attributes are a supplementary channel of the same kind. A tooltip can
help users predict where a link goes and reduce wasted paths — kept under about
60-80 characters, naming the destination site or subsite, the kind of information
to expect, or an access warning — but they should not be added to every link,
since obvious destinations plus tooltips only add clutter. Browsers render them
differently and most touchscreen browsers not at all, so the source is explicit:
link titles do not eliminate the need for good information scent, and the label
plus surrounding text must be understandable without them
[[2016-06-19_title-attribute]].

### Perceived value and first impressions

Users judge a site within seconds on visual appearance, and a negative reaction
lowers perceived value and triggers abandonment before any real interaction. A
cluttered page suggests an inability to distil information and triggers a halo
effect onto the whole organisation. Visual design should match the business's
value proposition — budget-looking for a budget airline, sophisticated for a
luxury brand — since misalignment confuses users and damages credibility. The
initial perception frames the whole visit: users who perceive low value complete
tasks half-heartedly and leave at the first exit. Expected utility rises when
the site conveys the right message and requires little effort to interact with
[[2016-04-17_perceived-value]].

### Navigation structures that expose scent

Left-side vertical navigation accommodates as many top-tier categories as
needed, which lets a site show specific, high-scent categories instead of
forcing generic groupings that users must open before finding out what is
inside. It also suits how people scan — attention leans left, with users looking
at the left half of the screen 80% of the time, and vertical lists yield more
information per eye fixation than horizontal menus. The cost is a lower
content-to-chrome ratio. Guidelines: place it left with high contrast, do not
duplicate the same menu horizontally and vertically, keep visible text labels
rather than icon-only designs, do not hide navigation behind a desktop hamburger,
and put important items above the fold — "in navigation, a word is worth a
thousand pictures" [[2021-05-16_vertical-nav]].

Comparison tables carry scent through their own structure. Users first appraise
column and row labels, then sweep in the lawn-mower pattern; very long tables
make them lose track of which product is in which column and force repeated
returns to the top. Fixed headers, narrower navigation, self-explanatory cells,
grouped yes/no features, minimal repetition and no placeholder content preserve
the pattern [[2020-12-13_lawn-mower-pattern]].

### Signal that there is more to find

Weak carousel cues give insufficient scent about what further content awaits, so
users never realise more options exist. Content peeking off the screen edge,
headlines naming the carousel frames, salient arrow controls and slide counts
communicate continuation; the same logic applies vertically, where full-screen
hero content, full-width horizontal rules, expansive white space and interrupting
ads can all read as the end of the page — in one study six of eight users did not
scroll past a hero video [[2016-01-17_illusion-of-completeness]]. A vague,
prominent call to action produces the same effect by acting as a magnet that
stops users scrolling to the information below
[[2017-08-20_get-started]].

### Icons and unfamiliar interaction cues

Icon quality has four criteria — findability, recognition, information scent,
attractiveness — and testing should be matched to the criterion and the project
phase. Out-of-context tests, showing an icon in isolation and asking what it
represents and what users expect to happen, suit early conceptualisation for
recognition and scent; time-to-locate tests on the full interface measure
findability with first-click accuracy; A/B tests on live sites measure scent
through interaction rates and probing behaviour (clicking then immediately
leaving); 1-7 rating scales and comparative selection cover attractiveness.
Watch the wording of tasks, since it can prime interpretations
[[2016-02-07_icon-testing]]. The same problem appears in physical-to-digital
bridges: QR codes have no information scent and need explanatory context or
artistic customisation to be meaningful [[2016-10-16_wechat-qr-shake]].

### Design so that foraging needs no workarounds

Users develop behavioural enrichments (page parking, F-pattern scanning) and
interaction enrichments (filters, keywords) to cut between-patch and within-patch
costs. Well-designed pages make these unnecessary: scanning-friendly formatting,
bolded keywords and descriptive headlines maximise the information gained per
unit of time, and optimisation should focus on the top tasks the page serves
[[2019-11-10_information-foraging]].

### Generative AI compresses the foraging loop

A two-week diary study of 18 users across ChatGPT, Google Bard and Bing Chat
(425 logged conversations, 75% information-seeking) found that chatbots collapse
the traditional find-evaluate-aggregate sequence into a single coherent answer,
sharply reducing interaction cost. Bots scored 5.77 for helpfulness and 6.00 for
trustworthiness on a 1-7 scale, yet only 22% of conversations included any
verification. Users were disappointed by broad, generic answers — expectations
for AI exceeded those for search engines because crafting a prompt costs more
effort — and by bots forgetting earlier context. Because verification itself
carries a high interaction cost, tools should make it cheap by supplying sources
or citations [[2023-09-24_generative-ai-diary]].

## Sources (12)

- [[2016-01-17_illusion-of-completeness]] — mentioned in context of carousel design; weak carousel cues provide insufficient information scent about what additional content awaits, so users do not realize more options or content exist to explore.
- [[2016-02-07_icon-testing]] — a key criterion for icon usability; users must infer what clicking the icon will do.
- [[2016-04-17_perceived-value]] — The article applies information-foraging theory, explaining how users assess perceived value against perceived interaction cost to decide whether to stay on a site.
- [[2016-06-19_title-attribute]] — Title attributes provide additional context about where a link leads, but cannot replace clear, descriptive link text.
- [[2016-10-16_wechat-qr-shake]] — Identifies lack of information scent (QR codes look meaningless without explanation) as a usability limitation requiring additional context or artistic customization.
- [[2017-08-20_get-started]] — users judge whether a link or button will lead them toward their goal based on the visual and textual cues present; misleading labels create false information scent.
- [[2019-03-24_better-link-labels]] — Link labels must communicate what content lies beyond so users can anticipate whether to click.
- [[2019-11-10_information-foraging]] — presents the foundational theory of how users navigate web content to satisfy information needs based on cost-benefit analysis, judging page relevance through visible cues and signals before committing time to exploration.
- [[2020-02-02_information-scent]] — Applies foraging theory to web navigation, showing how users estimate value and predict relevance to make navigation decisions.
- [[2020-12-13_lawn-mower-pattern]] — highlights how unclear labels and jargon interrupt users' ability to efficiently scan and process table information.
- [[2021-05-16_vertical-nav]] — Vertical navigation exposes specific categories with high information scent without requiring users to first select generic parent categories.
- [[2023-09-24_generative-ai-diary]] — Generative AI drastically reduces the effort required to find, evaluate, and aggregate information by automating the entire aggregation process.
