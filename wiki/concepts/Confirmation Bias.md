---
type: concept
name: Confirmation Bias
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "Biais de confirmation"
  - "Biais de validation"
---

# Confirmation Bias

## Definition

Confirmation bias is the tendency to interpret new information in ways that
conform to beliefs already held: contradictory evidence is discarded even when
it is factual, confirming evidence is sought out, and ambiguous evidence is read
in favour of the existing belief [[2022-03-13_confirmation-bias-ux]]. It is not a defect of careless people but
an ordinary feature of human reasoning, and it strengthens with investment: the
more time and emotion someone has put into a design or into an assumption about
users, the more likely they are to read research findings as validation [[2022-03-13_confirmation-bias-ux]].

In UX it shows up in two directions at once. On the practitioner side it takes
the form of the false-consensus effect, the assumption that other people share
our beliefs and will behave as we would, generalised from the handful of
examples we have available (ourselves, our colleagues) [[2017-10-22_false-consensus]]; researchers are no
more immune than designers, and prior knowledge or heuristics can blind a team
to what actual users experience [[2017-10-22_false-consensus]] [[2022-03-13_confirmation-bias-ux]]. On the participant side, expectations
that a study or an interface has primed shape what people then perceive and
report: when primed expectations are confirmed the experience feels smooth and
intuitive, when they are violated users judge the same unchanged interface as
poorly usable [[2016-01-24_priming]]. The French corpus names the same trap "biais de validation"
and treats it as the first risk to control when testing interest in a feature
[[2024-06-04_331_Tester_un_concept_de_fonctionnalité,_3_méthodes_d_UX_&_Market_research]] or when running discovery interviews [[2025-04-01_371_L_interview_longue_en_phase_de_Discovery_-_Guide_UXR]].

## Practice

### Investigate rather than validate

The recurring instruction across the sources is to change the purpose of the
study. Approach research with an open mindset that tests hypotheses instead of
confirming them, and start with research rather than validation [[2022-03-13_confirmation-bias-ux]]. Avoid
using research to confirm existing assumptions; investigate actual behaviour,
especially where even slight doubt exists about a design choice [[2017-10-22_false-consensus]]. In
discovery, define the objective of the interview clearly beforehand (adjusting a
roadmap, finding opportunities): an unprepared long interview yields superficial
data and slides into confirmation bias [[2025-04-01_371_L_interview_longue_en_phase_de_Discovery_-_Guide_UXR]]. The trap named there is precisely
steering the interview or the questions to validate pre-existing beliefs [[2025-04-01_371_L_interview_longue_en_phase_de_Discovery_-_Guide_UXR]].

### Ask non-biasing questions

Leading survey questions prime participants and bias the study toward confirming
the researcher's hypothesis rather than surfacing real issues [[2022-03-13_confirmation-bias-ux]]. Task wording
carries the same risk: when a usability task uses terms already present in the
interface, participants are primed to hunt for those exact words, which can
produce a false conclusion that information is easy to find [[2016-01-24_priming]]. In interviews,
closed questions that invite a yes or no should be banned in favour of open
questions that let the participant develop their thinking and reveal unexpected
material [[2025-04-01_371_L_interview_longue_en_phase_de_Discovery_-_Guide_UXR]]. Two further interview techniques serve the same end: not filling
silences, so the participant keeps digging, and reformulating what they said, so
they correct imprecision and point at the real irritants [[2025-04-01_371_L_interview_longue_en_phase_de_Discovery_-_Guide_UXR]].

### Watch the moderator, not only the protocol

Facilitator behaviour primes participants too. Excessive friendliness,
verbosity, choice of terminology, demonstrations and physical redirects all
nudge participants into particular behaviours and reduce the reliability of the
test [[2016-01-24_priming]].

### Prefer behaviour and empirical signals over stated intentions

Ask users what they actually do to solve their problems rather than what they
would like: current behaviour expresses real needs far more reliably than
projections [[2025-04-01_371_L_interview_longue_en_phase_de_Discovery_-_Guide_UXR]]. The same reasoning drives the feature-testing methods in [[2024-06-04_331_Tester_un_concept_de_fonctionnalité,_3_méthodes_d_UX_&_Market_research]],
where the stated risk is that users say in an abstract survey that they would
use a feature, distorting any read on real interest. The three methods are
ranked by how close they sit to a real usage context, and therefore by how much
bias they carry: a fake door (a button or link in the live product toward a
feature that does not exist yet, measuring clicks and notification requests)
gives very reliable data for little development effort; a fake landing page
sells the value proposition before building it, at the cost of design effort and
targeted recruitment; feature cards (a visual plus a short description, used in
qualitative tests such as card sorting) are the simplest to set up but carry the
highest bias because they are furthest from real use [[2024-06-04_331_Tester_un_concept_de_fonctionnalité,_3_méthodes_d_UX_&_Market_research]]. Obtaining early
empirical data is listed as a prevention strategy in its own right [[2022-03-13_confirmation-bias-ux]].

### Triangulate, and bring in fresh eyes

Multiple data sources give credibility and make findings harder to twist into a
hypothesis than a single source does [[2022-03-13_confirmation-bias-ux]]. Colleagues who were not involved in
the work can spot confirmation bias that invested team members miss [[2022-03-13_confirmation-bias-ux]]. And
the only way to defeat the false-consensus effect is to test with real target
users, not with colleagues or with people like yourself: assumptions without
user data are almost always wrong [[2017-10-22_false-consensus]].

### Use priming deliberately where it is legitimate

Priming is not only a hazard to be suppressed. [[2016-01-24_priming]] argues for using it to
advantage, biasing people into expectations and behaviours that match both the
site's goals and their needs, while noting the cost of getting it wrong: images
and page content set expectations, aesthetic treatment produces unconscious
inferences about the business, and a prominent coupon-code field primes users to
abandon checkout and go hunting for a code they never intended to use.

## Sources (5)

- [[2016-01-24_priming]] — when user expectations primed by design are confirmed, the experience feels smooth and intuitive; when primed expectations are violated, users perceive poor usability despite the interface being unchanged.
- [[2017-10-22_false-consensus]] — describes the tendency to assume others think like us, a specific instantiation of confirmation bias in UX.
- [[2022-03-13_confirmation-bias-ux]] — how existing beliefs lead people and researchers to ignore contradictory evidence and selectively interpret information.
- [[2024-06-04_331_Tester_un_concept_de_fonctionnalité,_3_méthodes_d_UX_&_Market_research]]
- [[2025-04-01_371_L_interview_longue_en_phase_de_Discovery_-_Guide_UXR]]
