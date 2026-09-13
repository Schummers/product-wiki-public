---
type: concept
name: Minimum Viable Product
created: 2026-07-31
updated: 2026-09-11
status: developed
aliases:
  - "MVP"
  - "MVP (Minimum Viable Product)"
  - "Minimum Viable Solution"
---

# Minimum Viable Product

## Definition

A minimum viable product is the first, deliberately minimal version of a product, shipped quickly so that real users can react to it before anything more is built. The Parlons Design corpus describes it from the maker's side: launch a first version with minimal features to test user interest as early as possible ([[2025-03-04_367_Le_meilleur_outil_de_benchmark_gratuit_1000+_screenshots]]), aim simple, solve one very defined problem without seeking perfection, and deploy fast so that feedback drives the next iterations ([[2025-06-10_381_Créer_sa_1ère_app_iPhone_-_Guide_complet_débutant]]). The justification is the same in both episodes: the only real feedback comes from people confronted with the product in their real life.

The venture-studio books use the MVP as a step in an institutional funnel rather than as a solo maker's first release. In *Venture Studios Demystified*, building early MVPs is one of the defining functions of a studio, alongside developing ideas internally, testing them, recruiting founding teams and providing capital ([[2022-02-08_venture-studios-demystified_02-part-1-venture-studio-basics]]); it is the third step of a three-step process, after brainstorming and customer validation, where early prototypes are built and tested before a company is launched ([[2022-02-08_venture-studios-demystified_06-process]]). Midealab, in *Startup Studio Playbook*, goes further and rejects the "merely viable" framing: its build phase develops a "minimum loveable product", a product that works, tested against actual users to reach fit before growth ([[2019-02-17_startup-studio-playbook_09-building-startups-from-megatrends]]). So a designer's MVP is a cheap probe of interest; a studio's MVP is a gated artefact whose purpose is to decide whether a venture exists at all.

*User Story Mapping* gives a third framing again, closer to the podcast's
maker posture than to the studios' funnel but built on outcomes rather than
features. Patton defines MVP three ways: a bad definition ("the crappiest
product you could possibly release"), and two good ones — the smallest release
that achieves desired outcomes, and, crediting Eric Ries, the smallest
experiment that tests an assumption. He is explicit that defining "minimum"
and "viable" both require guessing about customer behaviour and what makes
people happy, and that this uncertainty cannot be removed
([[2014-09-05_user-story-mapping_07-2-plan-to-build-less]]). Patton then
reframes the acronym as "minimum viable product experiment" (MVPe): the
smallest thing that can be built to learn something, deliberately less than
viable at first, iterating toward viability rather than starting there
([[2014-09-05_user-story-mapping_08-3-plan-to-learn-faster]]). Elsewhere he
drops the word "product" from the definition altogether: an MVP is the
smallest possible experiment needed to validate a core assumption, and it can
be a design comic or a paper prototype rather than working software
([[2014-09-05_user-story-mapping_20-15-using-discovery-for-validated-learning]]).

*The 10x Method* gives the sizing rule the other sources leave implicit: a properly scoped MVP delivers 1 percent of the founder's ultimate long-term vision while capturing 80 percent of its core value, and it ships in weeks rather than months ([[2026-03-05_10x-method_04-building-your-mvp]]). It also draws a line the podcast does not: the artefact must be a functional product, not a polished prototype, because a prototype invites opinions while a working product triggers real behaviour. So the vision comes first, the MVP is explicitly only its first step, and the discipline is ruthless prioritisation down to the one fundamental problem that delivers immediate value.

## Practice

### Aim small and ship (podcast)

- **One defined problem, no perfection.** For a first project, [[2025-06-10_381_Créer_sa_1ère_app_iPhone_-_Guide_complet_débutant]] insists on aiming simple and solving a very narrow problem. The goal of the first project is to go from zero to an application actually put into production; building a small app is already a lot, and much is learned along the way. Deploying a first version quickly is what allows collecting user feedback and iterating effectively afterwards.
- **Minimal features to test interest.** [[2025-03-04_367_Le_meilleur_outil_de_benchmark_gratuit_1000+_screenshots]] describes the same posture for Pablo.club, a community benchmark library: launch the first version with minimalist features to test user interest as fast as possible, and ask users to share feedback to make the product evolve.

### Prototype before the MVP (podcast)

The Pablo.club story ([[2025-03-04_367_Le_meilleur_outil_de_benchmark_gratuit_1000+_screenshots]]) shows an MVP arriving after several iterations rather than as the first artefact. The project started in summer 2024 as a manual prototype on Notion, which ran into the difficulty of getting users to contribute. Integrating AI to automatically describe screens, combined with AI-driven semantic search, is what unblocked the concept and led to an MVP built with Svelte and PocketBase. The lesson the episode draws is that the concept had to be unlocked before the MVP was worth building. See [[Prototyping]] and [[Benchmarking]].

### Why the designer should build one (podcast)

[[2025-06-10_381_Créer_sa_1ère_app_iPhone_-_Guide_complet_débutant]] frames building and shipping a small app as a way for a product designer to acquire a global view of a product's lifecycle, from design to marketing, to dialogue more easily with technical teams, and possibly to earn complementary income. AI assistants are recommended as allies if used to understand the logic rather than to copy-paste.

### The MVP as a funnel step (books)

- **Studio definition.** Studios found startups by developing ideas internally, testing them, building early MVPs, assembling founding teams and providing initial capital; they act as co-founders, not advisors ([[2022-02-08_venture-studios-demystified_02-part-1-venture-studio-basics]]). See [[Venture Studio]].
- **Third of three steps.** The standard studio process is (1) brainstorming and early idea development, (2) customer validation through user research and marketing testing (click-through rates, customer letters of intent), and (3) building and testing early prototypes to validate the concept before full company launch ([[2022-02-08_venture-studios-demystified_06-process]]). The MVP therefore comes after demand has been tested with marketing signals, not before. See [[Idea Validation]].
- **Fail fast, preserve runway.** The process rests on design thinking: rapidly prototype, test, and fail fast, because a studio must fund ideas for years before a single exit. Many ideas are killed in the earliest research stages and advanced ideas are scrutinised against short evaluation windows ([[2022-02-08_venture-studios-demystified_06-process]]). Stage gates exist precisely to stop unsuccessful ideas consuming resources ([[2022-02-08_venture-studios-demystified_02-part-1-venture-studio-basics]]). See [[Stage Gate]] and [[Studio Funnel]].
- **Funnel numbers.** It takes 30 to 107 top-level ideas to launch one company, and 73 percent of studios aim to launch at most 4 companies a year; time to Seed runs 6 to 18 months ([[2022-02-08_venture-studios-demystified_06-process]]). The MVP is one of the artefacts that gets an idea through this funnel.

### Viable versus loveable (books)

Midealab's build phase ([[2019-02-17_startup-studio-playbook_09-building-startups-from-megatrends]]) develops a "minimum loveable product", a product that works, rather than an MVP in the strict sense. It is tested with real market validation to understand how customers adopt it and where the venture can best enter the market, while the studio also clarifies the business model and assembles a dedicated core team. Seed funding is secured before the growth phase so the team focuses on execution rather than fundraising. See [[Product-Market Fit]].

### One percent of the vision, shipped in weeks (books)

[[2026-03-05_10x-method_04-building-your-mvp]] is the most operational of the
sources on how to scope and run an MVP.

- **Scope by ratio.** The MVP is 1 percent of the long-term vision and 80
  percent of its core value. Defining the long-term vision comes first, then the
  one fundamental problem that delivers immediate value; the separation is what
  stops founders overbuilding while still shipping something users measurably
  value.
- **Weeks, not months.** Speed is treated as a competitive advantage in itself:
  the sooner the product is in users' hands, the sooner the core hypothesis is
  tested, and real usage teaches more than months of internal discussion or
  polished prototypes. Shipping fast also signals execution ability to the team
  and to investors.
- **Low-fidelity wireframes.** Start with deliberately ugly wireframes to
  iterate rapidly, simplify the MVP, save time on high-fidelity design, and let
  teams collaborate without premature attachment to aesthetics: when a design
  looks finished, stakeholders hesitate to challenge it. See [[Prototyping]].
- **Design partners rather than beta testers.** Move from internal assumptions
  to real-world validation through partners who actively co-build the product.
  Struggling to find partners willing to invest their time is itself a signal
  that the pain point is not strong enough. See [[Design Partner]].
- **Rituals to keep it moving.** Weekly product committees of 30 to 60 minutes
  review shipped work, refine priorities and clear blockers; quarterly milestone
  planning of one to two hours keeps day-to-day execution from derailing the
  long-term vision. See [[Operating Rituals]].
- **One focus metric after launch.** Pick a single north star among customer
  retention rate, MRR growth, or active users, rather than measuring everything;
  at this stage conviction and qualitative user feedback matter more than
  dashboards.

### Outcomes, not features, define minimum (books)

Patton illustrates the outcome-first definition through Globo.com, Brazil's
largest media company, where eight teams from three divisions used story
mapping to plan a shared content-management rebuild against unmovable
deadlines. Once the full map showed the work would take over a year, Patton
had the teams ask "what outcomes do we need for the upcoming Brazilian
election?" and slice the map into staged releases targeting specific outcomes
rather than every feature. His framing: "scope doesn't creep; understanding
grows" — what looks like discovered scope is teams learning, together, work
nobody had actually claimed
([[2014-09-05_user-story-mapping_07-2-plan-to-build-less]]). A sidebar on
FORUM Credit Union, run with SEP, shows the same outcome discipline used to
sort features by differentiator, spoiler, cost-reducer and table-stakes value
with color-coded sticky notes, before any code was written
([[2014-09-05_user-story-mapping_07-2-plan-to-build-less]]).

Patton's Liquidnet example, a product owner named Eric, makes the same point
at the scale of a single feature rather than a company-wide rebuild. Eric
frames the opportunity with leadership, validates with customers and users
that the problem is real, sketches prototypes in tools like Axure without
building software, then releases increasingly complete versions to a small
group of development partners while measuring actual usage rather than stated
preference — because people may say they like something and never use it. The
real outcome he is chasing is not a prototype or an MVP but customers who
choose to use the product every day, so each release functions as an
experiment with an explicit thing to learn, deliberately built less than
viable at first and grown toward viability as development partners begin
recommending it to others
([[2014-09-05_user-story-mapping_08-3-plan-to-learn-faster]]).

Folding MVP into Lean Startup's build-measure-learn loop, Patton offers a
20 / 20 / 60 split — about 20 percent of what we build succeeds, another 20
percent genuinely does harm, and the rest is neither — and is explicit that
this is his own estimate from his failures and what he observes, "not rooted
in any formal scientific research or studies." The published figures he cites
alongside it are the Standish Group's, that 64 to 75 percent of features are
rarely or never used. Either way, in his reading, guessing and hoping does not
work and assumptions must be validated. The corrective is a short cycle: name the
riskiest assumption, build the smallest possible test (often not code at all),
measure by observing customers, and rethink from the result; failing fast is
good news because it happens before a large investment
([[2014-09-05_user-story-mapping_20-15-using-discovery-for-validated-learning]]).

### Where the sources diverge

- **How minimal.** The podcast's advice is to strip to one problem and ship, accepting imperfection ([[2025-06-10_381_Créer_sa_1ère_app_iPhone_-_Guide_complet_débutant]], [[2025-03-04_367_Le_meilleur_outil_de_benchmark_gratuit_1000+_screenshots]]). Midealab explicitly wants more than viable: a loveable product that works ([[2019-02-17_startup-studio-playbook_09-building-startups-from-megatrends]]). *Venture Studios Demystified* speaks of "early MVPs" and "early prototypes" without taking a position on polish. *The 10x Method* sets an explicit ratio instead of a feeling, 1 percent of the vision for 80 percent of the value, and insists the result be functional rather than polished ([[2026-03-05_10x-method_04-building-your-mvp]]). Patton goes further than any of these and drops "product" from the definition itself: the smallest thing that answers a question does not have to be functional software at all — a design comic or a paper prototype qualifies ([[2014-09-05_user-story-mapping_20-15-using-discovery-for-validated-learning]]).
- **What precedes it.** In the podcast, the MVP follows the maker's own prototypes and is the first thing real users see. In the studio process, the MVP follows a customer-validation step run on marketing signals and letters of intent, so demand is already partly established before anything is built ([[2022-02-08_venture-studios-demystified_06-process]]). In *The 10x Method*, what precedes the MVP is neither a prototype nor a marketing test but a written long-term vision, against which the MVP is scoped ([[2026-03-05_10x-method_04-building-your-mvp]]). Patton puts opportunity framing and problem validation with real customers first, then sketched prototypes, and treats even the first release to development partners as deliberately less than viable ([[2014-09-05_user-story-mapping_08-3-plan-to-learn-faster]]).
- **Who it serves.** For the podcast, the MVP serves the designer's learning and the product's first feedback loop. For the studios, it serves a portfolio decision: whether to launch a company and commit capital. For Patton, it serves neither a solo maker's curiosity nor a portfolio gate, but a specific outcome the team named in advance — Globo.com's election deadline, or the one assumption Eric at Liquidnet needs validated ([[2014-09-05_user-story-mapping_07-2-plan-to-build-less]]).
- **Prototype or product.** The podcast reaches its MVP through prototypes, including a manual Notion one ([[2025-03-04_367_Le_meilleur_outil_de_benchmark_gratuit_1000+_screenshots]]), and *Venture Studios Demystified* builds and tests "early prototypes" as its third step ([[2022-02-08_venture-studios-demystified_06-process]]). *The 10x Method* keeps low-fidelity wireframes for internal iteration but argues that what reaches users must be a working product, since a prototype invites opinions where a functional product triggers real behaviour ([[2026-03-05_10x-method_04-building-your-mvp]]). Patton sits closest to the podcast here, and furthest from *The 10x Method*: his "minimum viable product experiment" can be pure prototype, and staying below viable on purpose is the point, not a compromise ([[2014-09-05_user-story-mapping_08-3-plan-to-learn-faster]]).

## Sources (10)

- [[2025-03-04_367_Le_meilleur_outil_de_benchmark_gratuit_1000+_screenshots]]
- [[2025-06-10_381_Créer_sa_1ère_app_iPhone_-_Guide_complet_débutant]]
- [[2019-02-17_startup-studio-playbook_09-building-startups-from-megatrends]] — Midealab's build phase develops a "minimum loveable product" (rather than merely viable), focusing on product-market fit before growth; the MVP is tested with real market validation to understand how customers adopt it and where the venture can best enter; sufficient runway and seed funding are secured before growth phase to enable focus on execution rather than fundraising.
- [[2022-02-08_venture-studios-demystified_02-part-1-venture-studio-basics]] — Studios build early MVPs as part of their internal development process to test and validate venture concepts.
- [[2022-02-08_venture-studios-demystified_06-process]] — The third step involves building and testing early prototypes to further validate product concepts before full company launch.
- [[2026-03-05_10x-method_04-building-your-mvp]] — A properly scoped MVP delivers 1% of the founder's ultimate vision while capturing 80% of core value, shipping in weeks to gather real-world feedback. Success depends on ruthless prioritization: define your long-term vision first, then identify the one fundamental problem that delivers immediate value, creating a functional product (not a polished prototype) that users can truly engage with.
- [[2022-01-19_product-management-for-ux-people_10-chapter-7-testing-hypotheses-with-experiments]] — here appearing as "pretotype," Alberto Savoia's term (from his talk "Build the Right It") for a low-fidelity proof of concept or fast version of an idea that is just complete enough to generate real, data-driven validation of whether something "should be built," distinct from a prototype that proves "can we build it."
- [[2014-09-05_user-story-mapping_07-2-plan-to-build-less]] — Patton defines MVP as the smallest product release that achieves desired outcomes, while also acknowledging Eric Ries's definition (the smallest experiment to test assumptions); Patton emphasizes that defining MVP requires guessing and involves inherent uncertainty.
- [[2014-09-05_user-story-mapping_08-3-plan-to-learn-faster]] — Reframed as "minimum viable product experiment" (MVPe): the smallest thing that can be built to learn something; Eric builds less than viable to start and iterates toward viability.
- [[2014-09-05_user-story-mapping_20-15-using-discovery-for-validated-learning]] — Patton reframes MVP not as a reduced-scope product but as the smallest possible experiment (design comic, paper prototype, or coded minimum) needed to validate a core assumption, allowing teams to learn quickly before building the full vision.
