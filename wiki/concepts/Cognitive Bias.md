---
type: concept
name: Cognitive Bias
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Cognitive Bias in Design"
  - "Complexity Bias"
  - "Memory Bias"
  - "Negativity Bias"
---

# Cognitive Bias

## Definition

Cognitive biases are systematic errors in thinking and judgement that shape how
people interpret information and make decisions
[[2017-12-19_decision-framing-cognitive-bias-ux-pros]]. In the sources they run
in two directions at once. On the user side, they explain why people make
seemingly illogical choices: prospect theory, proposed by Kahneman and Tversky
in 1979, describes how people choose between options and estimate their
likelihood in biased ways, through loss aversion, certainty bias and the
isolation effect [[2016-06-19_prospect-theory]]. On the practitioner side, the
same machinery distorts design and research: framing, narrative bias,
false consensus, confirmation bias, anchoring, functional fixedness and hindsight
bias all act on the team, not the user
[[2017-12-19_decision-framing-cognitive-bias-ux-pros]],
[[2017-02-19_narrative-biases]], [[2017-10-22_false-consensus]],
[[2022-03-13_confirmation-bias-ux]], [[2024-10-11_discovery-mindset]],
[[2017-07-30_functional-fixedness]], [[2022-05-01_ink-thinking]]. Two more sit
on the user side — memory bias and negativity bias, which together decide what an
experience is remembered as [[2024-01-23_laws-of-ux_08-6-peakend-rule]] — and one more on the practitioner's:
complexity bias, the pull toward complicated solutions [[2024-01-23_laws-of-ux_11-9-teslers-law]].

What unites the sources is that these biases are not defects of individuals but
features of how everyone thinks. Believing that others are like us is described
as deeply woven into human nature, not a moral failing
[[2017-10-22_false-consensus]], and knowing a bias exists does not stop it from
operating [[2017-02-19_narrative-biases]]. The practical consequence is that
biases are countered by process — testing, triangulation, reframing, recording
predictions — rather than by resolving to think more clearly.

## Practice

### Biases that shape user decisions

- **Loss aversion** — losses loom larger than gains; people overweight small
  probabilities to guard against loss and often prefer a smaller certain loss to
  a possible large one [[2016-06-19_prospect-theory]].
- **Certainty bias** — people overweigh certain outcomes and are risk-averse for
  gains, accepting a small guaranteed reward over a chance at a larger one
  [[2016-06-19_prospect-theory]].
- **Isolation effect** — when comparing alternatives, people disregard whatever
  the options share and focus only on differentiators, which makes their choices
  inconsistent depending on how the alternatives are presented
  [[2016-06-19_prospect-theory]].
- **Framing** — presenting information as a gain or as a loss significantly
  changes decisions; negatively framed messages prime people to think of losses
  [[2016-06-19_prospect-theory]].
- **Memory bias** — memories are rarely an accurate record of events. Intensely
  emotional moments are remembered more than less emotional ones, so an
  experience is recalled not as the sum of how it felt throughout but through its
  peak emotional moments and its end ([[Peak-End Rule]]) [[2024-01-23_laws-of-ux_08-6-peakend-rule]].
- **Negativity bias** — people register and dwell on negative events more readily
  than positive ones, which is why a single bad moment weighs so heavily on the
  memory of an otherwise working experience [[2024-01-23_laws-of-ux_08-6-peakend-rule]].
- **Asymmetry of experience** — users react far more strongly to moments of loss,
  frustration or confusion than to things working as expected; working correctly
  is treated as the norm, while small stumbling blocks are remembered much longer
  [[2016-06-19_prospect-theory]].

### Biases that distort the team's own judgement

- **Framing bias in research interpretation.** A frame is the context used to
  describe an idea, question or decision, and identical data can lead to opposite
  conclusions depending on it: practitioners shown a usability finding as a
  failure rate ("4 out of 20 users could not find search") were 31% more likely
  to support a redesign than those shown the same result as a success rate
  ("16 out of 20 found it") [[2017-12-19_decision-framing-cognitive-bias-ux-pros]].
  Frames also fail by being incomplete (considering only existing users, missing
  potential ones) or overly specific (asking "should we implement feature X"
  instead of weighing broader benefits)
  [[2017-12-19_decision-framing-cognitive-bias-ux-pros]].
- **Narrative bias.** People interpret information as part of a larger story
  whether or not the facts support it, and will invent explanatory stories on the
  flimsiest foundation. Two story elements do the damage: specific details and
  cause-effect explanations [[2017-02-19_narrative-biases]].
- **Base-rate neglect.** A vivid detail overrides the statistics: in a survey,
  41% of UX practitioners overestimated the probability that a New York Times
  reader holds a PhD [[2017-02-19_narrative-biases]].
- **Preference for causation over randomness.** Faced with ambiguous data — a
  high exit rate on a low-traffic page — people prefer a causal explanation such
  as poor design over random variation, even when the sample is far too small to
  support it, and then spend effort solving a problem that does not exist
  [[2017-02-19_narrative-biases]]. The "digital natives figure out any interface"
  story is the same bias applied to an audience: poor design harms users of all
  ages [[2017-02-19_narrative-biases]].
- **False-consensus effect.** People overestimate how many others share their
  choices, values and beliefs, and treat those who differ as rare or deviant.
  Availability bias reinforces it: we generalise from the handful of examples we
  have, ourselves and our colleagues [[2017-10-22_false-consensus]].
- **Confirmation bias.** People interpret new information so that it conforms to
  existing beliefs — discarding contradictory facts, seeking confirming evidence,
  and reading ambiguous evidence in their own favour. It grows with investment:
  the more time and emotion sunk into a design, the more research findings read
  as validation [[2022-03-13_confirmation-bias-ux]].
- **Anchoring.** Starting discovery with a preferred solution makes teams
  interpret research through that lens and test the solution instead of exploring
  the problem [[2024-10-11_discovery-mindset]].
- **Functional fixedness.** A bias driving people to use objects only in their
  traditional ways. It strengthens with practice and age — five-year-olds solved a
  candle-mounting puzzle faster than older children because they were not fixated
  on a box's containment function — so experience that ought to broaden
  perspective narrows it instead [[2017-07-30_functional-fixedness]].
- **Hindsight bias.** People overestimate their ability to have predicted an
  outcome once they know the result [[2022-05-01_ink-thinking]].
- **Complexity bias.** People favour complex solutions over simple ones because
  complexity is associated with intelligence and expertise. In a 1989 study by
  Farris and Revlin, participants preferred complicated hypotheses over the
  simple rule "list three numbers that go up"; the preference for overengineered
  solutions is read as a sign of not yet understanding the problem well enough
  [[2024-01-23_laws-of-ux_11-9-teslers-law]].

### Countermeasures

- **Test with real target users.** The only way out of false consensus is testing
  with actual target users, not colleagues or people like yourself; assumptions
  unbacked by user data are almost always wrong [[2017-10-22_false-consensus]].
- **Investigate, don't validate.** Approach a study with an open mindset testing
  hypotheses rather than confirming them, and get empirical data early
  [[2017-10-22_false-consensus]], [[2022-03-13_confirmation-bias-ux]].
- **Ask non-leading questions.** Leading survey questions prime participants and
  bias the study toward the researcher's hypothesis instead of surfacing real
  issues [[2022-03-13_confirmation-bias-ux]].
- **Triangulate and bring in fresh eyes.** Multiple data sources are harder to
  twist to fit a hypothesis than a single one, and uninvolved colleagues spot the
  bias that invested team members cannot [[2022-03-13_confirmation-bias-ux]].
- **Ground stories in research.** Memorable details in stories and personas must
  come from actual research, preferably several data sources; even a quick survey
  checks a basic assumption. Where a story is implicit, articulate and challenge
  it explicitly through formal problem definition
  [[2017-02-19_narrative-biases]].
- **Reframe as a bias check.** Restate the decision from the reverse
  perspective — failure versus success, percentages versus actual numbers
  affected — to detect when framing is doing the deciding. Resist snap judgements,
  gather context, and recognise when you simply lack enough information
  [[2017-12-19_decision-framing-cognitive-bias-ux-pros]].
- **Reframe goals around problems and icebox solutions.** Set a problem-focused
  discovery goal rather than a solution-focused one, surface and prioritise what
  the team is assuming versus what it knows, and freeze solution ideas in writing
  until research is complete so they neither anchor the work nor get lost
  [[2024-10-11_discovery-mindset]].
- **Abstract the problem and go far afield.** Strip surface detail and
  domain-specific language to break functional fixedness; the abstracted problem
  reveals structurally related but distant fields to borrow from. Delay judgement
  during ideation — diverge first, converge later — and expose yourself to other
  people's perspectives [[2017-07-30_functional-fixedness]].
- **Design against the negative peak.** Because negativity bias makes bad moments
  dominate the memory of an experience, prevent negative peaks outright with
  proactive guidance — real-time password validation, as Mailchimp does — and
  humanise the friction that cannot be removed by carrying brand personality
  through it [[2024-01-23_laws-of-ux_08-6-peakend-rule]].
- **Keep a written record of predictions.** Ink thinking counters hindsight bias:
  record a decision and what you expect in two or three sentences, then record the
  actual outcome and advice to yourself once it is known. A small thin ruled
  journal and a scheduled 5–10 minutes weekly are the recommended setup;
  participants who journalled answered 23% more math puzzles correctly than those
  who simply practised more [[2022-05-01_ink-thinking]].

### The limits of awareness

Knowing about narrative bias does not immunise anyone against it — the sources
are explicit that you cannot stop yourself or your team from believing stories,
only ensure the stories you tell are true [[2017-02-19_narrative-biases]]. The
same holds for false consensus, framed as a natural human tendency rather than an
error to be willed away [[2017-10-22_false-consensus]]. Rich, real-world
situations carry more context than a survey question but the biases stay just as
powerful and become harder to detect [[2017-02-19_narrative-biases]].

## Sources (10)

- [[2016-06-19_prospect-theory]] — Prospect theory describes systematic deviations from rational decision-making, including loss aversion and certainty bias that influence how users evaluate options.
- [[2017-02-19_narrative-biases]] — narrative bias, base-rate neglect, and the fan effect are cognitive biases that misguide UX decisions.
- [[2017-07-30_functional-fixedness]] — functional fixedness as a cognitive bias that increases with expertise and experience, limiting innovation and problem-solving flexibility.
- [[2017-10-22_false-consensus]] — provides psychological explanation for why the false-consensus effect occurs and how it relates to other biases like availability bias.
- [[2017-12-19_decision-framing-cognitive-bias-ux-pros]] — Systematic errors in thinking and judgment that influence how people interpret information and make decisions; framing bias is one example where context affects conclusions despite identical underlying facts.
- [[2022-03-13_confirmation-bias-ux]] — understanding this systematic error in thinking and its influence on design decisions and research interpretation.
- [[2022-05-01_ink-thinking]] — counteracting hindsight bias and overconfidence by maintaining records of predictions.
- [[2024-10-11_discovery-mindset]] — systematic patterns in how teams and individuals think that can distort discovery and design decisions, including anchoring and confirmation bias.
- [[2024-01-23_laws-of-ux_08-6-peakend-rule]] — A cognitive bias impairing memory recall; people remember intense emotional events more vividly, directly driving peak-end evaluation; The human tendency to register and dwell on negative events more readily; must be mitigated through preventive guidance or reframing.
- [[2024-01-23_laws-of-ux_11-9-teslers-law]] — The human tendency to favor complex solutions over simple ones, often because complexity is associated with expertise. Leads designers to overlook simpler solutions without sufficient problem understanding.
