"""Judgement layer for wiki/themes/. Written by a strong model, never by hand
in the generated files (generate_themes.py overwrites those on every run).

THEME_WHEN[theme]  -> the routing pointer. Line 1 is the trigger list and is
                      what _router.md prints, so keep it under 160 chars and
                      make it stand alone. Later lines add nuance for anyone
                      already on the theme page.
CONCEPT_GLOSS[name] -> one line, what opening that concept page buys you.
                      Grounded in the page's own `### ` sub-headings. Never
                      restates the concept name.

Editing here then re-running generate_themes.py is the whole update loop.
"""

THEME_WHEN = {
    "Choosing and Running Research": (
        "Picking a research method, running a usability test, writing tasks, or deciding what "
        "evidence a question actually needs.\n\n"
        "The entry point for 'how do I find out'. Method selection lives here; rigour, "
        "recruitment and ethics live in [[Research Rigour and Ethics]]."
    ),
    "Research Rigour and Ethics": (
        "Sample size, recruiting, screeners, validity, bias, consent, or defending a study "
        "someone is challenging.\n\n"
        "The quality half of research. Open it once the method is chosen and the question is "
        "whether the study will hold up."
    ),
    "Structure, Navigation and Findability": (
        "Organising content, designing navigation or menus, naming things, or diagnosing why "
        "users cannot find what exists.\n\n"
        "Covers both the backstage structure and the visible navigation that exposes it, plus "
        "search and information scent. The place to start for any B2B or complex-app "
        "navigation question."
    ),
    "Page Composition and Hierarchy": (
        "Deciding what goes on a page, in what order, and what the eye should hit first.\n\n"
        "The layout-level theme: hierarchy, scanning, disclosure, grouping. Pair it with "
        "[[Content and Interface Writing]] for what the sections actually say and "
        "[[Visual Design Craft]] for how they look."
    ),
    "Interaction and Interface Patterns": (
        "Choosing a control, designing a form, a modal, an error, a notification, or any "
        "concrete interface component.\n\n"
        "Component-level guidance and the patterns behind it. For whether the component is "
        "usable at all, go to [[Usability Heuristics and Evaluation]]."
    ),
    "Usability Heuristics and Evaluation": (
        "Auditing an interface, running a heuristic evaluation or expert review, or scoring "
        "usability without users.\n\n"
        "The audit theme: Nielsen's ten heuristics, cognitive walkthroughs, PURE scoring, "
        "competitive expert review. This is what a design review runs against."
    ),
    "Visual Design Craft": (
        "Typography, colour, grids, spacing, imagery, or judging whether a visual style choice "
        "costs usability.\n\n"
        "The craft layer. Hierarchy and page-level composition sit in "
        "[[Page Composition and Hierarchy]]; system-level tokens in "
        "[[Design Systems and Consistency]]."
    ),
    "Content and Interface Writing": (
        "Writing labels, microcopy, error text, headings, email, or deciding how much content "
        "a page should carry.\n\n"
        "Words as an interface material: scanning, chunking, plain language, and the ethics of "
        "framing."
    ),
    "Accessibility and Inclusion": (
        "Contrast, keyboard operation, screen readers, alt text, touch targets, motion "
        "sensitivity, or designing across age and ability.\n\n"
        "Small theme, high stakes: accessibility is treated by the sources as infrastructure, "
        "not a finishing pass. Its sharp edges carry the specific component rules."
    ),
    "Mobile and Multi-Device": (
        "Designing for phone, tablet, watch, car screen, AR, or voice, and deciding what "
        "changes across screen sizes.\n\n"
        "Mobile is treated as its own medium rather than a narrow desktop. Responsive "
        "mechanics, touch, microsessions and cross-device continuity all live here."
    ),
    "Psychology, Cognitive Load and Behaviour": (
        "Explaining why users behave as they do, reducing mental effort, or looking up a named "
        "law of UX (Fitts, Hick, Miller, Jakob, Tesler).\n\n"
        "The 'why' underneath the guidance. Reach for it when you need the mechanism rather "
        "than the rule: attention, memory, mental models and bias, plus the ten psychological "
        "principles Laws of UX turns into design guidance."
    ),
    "Persuasion, Trust and Design Ethics": (
        "Driving a behaviour, asking for data or permissions, building credibility, or "
        "checking whether a pattern has crossed into manipulation.\n\n"
        "Holds the persuasion-versus-deception line explicitly, plus user control, "
        "customisation and privacy as trust mechanics."
    ),
    "Journeys, Service and Omnichannel": (
        "Designing across touchpoints, mapping a journey, blueprinting a service, or fixing "
        "handoffs between channels.\n\n"
        "Zooms out past the screen to the whole delivery, backstage included. Personas and "
        "e-commerce journeys attach here."
    ),
    "Design Systems and Consistency": (
        "Building or governing a design system, naming components, or arguing about "
        "consistency versus one-off design.\n\n"
        "Covers the system's contents, its semantics, and the organisational conditions that "
        "decide whether it gets adopted."
    ),
    "Design Process and Collaboration": (
        "Structuring how the work gets done: process phases, workshops, ideation, "
        "prototyping, critique, or fitting design into Agile.\n\n"
        "The 'how we work' theme. [[Story Mapping]] is here as a group activity and in "
        "[[Product Strategy and Framing]] as a planning artefact. Convincing people is a "
        "different problem, in [[Influence, Stakeholders and UX Maturity]]."
    ),
    "Influence, Stakeholders and UX Maturity": (
        "Getting buy-in, presenting to leadership, handling resistance, or raising a "
        "team's design maturity.\n\n"
        "The political and organisational theme: stakeholder alignment, storytelling with "
        "evidence, change management, and proving business impact."
    ),
    "Product Strategy and Framing": (
        "Framing the problem, choosing what to build, roadmapping, prioritising, testing an "
        "assumption, or what a product manager actually does.\n\n"
        "Sits upstream of design work. Discovery methods are shared with "
        "[[Choosing and Running Research]]. [[Product Management]] holds the role itself, "
        "what a PM does all day and what it is not; [[Assumption Testing]] holds the "
        "twelve ways to test a bet when an A/B test is not the tool. [[Story Mapping]] and "
        "[[Product Outcome]] joined the rank-1 list with Patton's User Story Mapping; the "
        "rest of the delivery vocabulary (user story, backlog, story slicing, release "
        "planning) sits in the sharp edges below."
    ),
    "Measurement, Metrics and Business Impact": (
        "Choosing metrics, setting a baseline, reading analytics, running an A/B test, or "
        "proving a design changed something.\n\n"
        "Consistent warning across the corpus: start from goals, not from what the tool "
        "happens to report. When an A/B test is impractical (a small named enterprise user "
        "base, a change too large to split), [[Assumption Testing]] carries the "
        "alternatives."
    ),
    "Adoption, Onboarding and Engagement": (
        "First-run experience, empty states, tutorials, activation, retention, or getting a "
        "feature actually used.\n\n"
        "The recurring position: a learnable interface beats a dedicated onboarding flow, and "
        "onboarding is worth testing for necessity first."
    ),
    "Designing With and For AI": (
        "Designing an AI feature or chatbot, using AI in the design process, prompting, or "
        "reasoning about what these systems get wrong.\n\n"
        "Two distinct branches deliberately kept together: AI as a design material, and AI as "
        "a tool in the workflow."
    ),
    "Career, Portfolio and Case Study": (
        "Building a portfolio, writing a case study, preparing or running a design exercise, "
        "thinking about career direction, or preparing a promotion or a performance review.\n\n"
        "The only theme about the practitioner rather than the product. It reads from three "
        "seats: the candidate preparing, the hiring manager designing the process, and the "
        "designer already in post trying to grow a level. Dashinsky 2023 added the growth-plan "
        "half; the ladder, competency and promotion pages themselves are single-work stubs "
        "listed under sharp edges. Crumlish 2022 added a fourth seat, the UX practitioner "
        "weighing a move into product: that fork lives in [[Product Management]] and in the "
        "career half of [[UX Career]]. No design review runs against it."
    ),
    "Venture Building and Studios": (
        "Building or joining a venture studio, validating ideas in batches, studio equity and "
        "economics, recruiting founders, raising for a studio, or founding a startup yourself.\n\n"
        "The one theme sourced from books rather than articles (Szigeti 2019, Kannan and "
        "Peterman 2022, Hexa 2026; docs/adr/0005). Two of the three books look at company "
        "building from the studio's seat, the third from the founder's, which is where the "
        "sharp edges on cofounders, first hires, design partners and go-to-market come from. "
        "It also carries the product concepts all three feed (PMF, MVP, strategy). No design "
        "review runs against it; the books disagree on numbers often enough that every page "
        "keeps both."
    ),
}

CONCEPT_GLOSS = {
    # Research
    "Research Methods": "the master inventory: how to choose among methods, and what each one can and cannot answer",
    "User Research": "matching method to project phase, and making findings actually land in the organisation",
    "Usability Testing": "planning, task writing, moderation, and the bias failures that recur in every study",
    "Qualitative Research": "when to go qualitative, issue-finding versus saturation, and defending small samples",
    "Quantitative Research": "choosing a quantitative method, sizing it, and why significance is not importance",
    "Active Listening": "implicit and explicit listening with stakeholders, and reading a participant's comfort, tone and body language during a session",
    "User Interviews": "funnel-structured guides, question craft, story-based interviewing, and facilitating without contaminating the answer",
    "Survey Design": "question wording, response biases, piloting, and when in the cycle each survey type fits",
    "Field Studies": "contextual inquiry variants, what to observe, and the failure modes of live sessions",
    "Remote Research": "moderated versus unmoderated, compensating for the absent moderator, guarding data quality",
    "Eye Tracking": "what attention actually lands on, scanning patterns, and how stable those findings are",
    "Card Sorting": "study variants, reading the results, and pairing it with tree testing",
    "Task Design": "writing tasks that do not prime or lead, and the ten wording mistakes to avoid",
    "Benchmarking": "getting a baseline before the work starts, choosing metrics, and the cheaper PURE instrument",
    "A-B Testing": "where in a funnel to test, guardrail metrics, and what it cannot replace",
    "Story Mapping": "the two axes and the backbone, slicing a map into releases, the now map versus the later map, and running the mapping as a group rather than drawing it alone",
    # Added 2026-09-11 with Storytelling in Design (Dahlström).
    "User Flow": "pairing flows with journeys instead of choosing, designing the branches rather than the happy path alone, the content each step needs, and reading competitors' flows in context",
    "Product Outcome": "which outcome a team should be given, Torres's anti-patterns, the outcome as the root of discovery, and how to measure it after release",
    "Product Trio": "what the trio is for, assigning the outcome to it rather than to a person, working individually before merging, and where Torres and Patton describe different groupings",
    "Product Management": "what the role is and is not, the five archetypes it descends from, what a PM actually does all day, and whether a UX person should make the move",
    "Assumption Testing": "surfacing and prioritising assumptions, designing a test that moves behaviour, and the twelve alternatives when an A/B test is not the tool",
    "Product Discovery": "when discovery is warranted, timeboxing it versus a weekly habit, running it inside Agile, and mapping the opportunity space",
    "Study Design": "protecting internal and external validity, order effects, attrition, and observer effects",
    "Research Planning": "what a plan contains, piloting, session length, and planning for a protocol that will change",
    "Participant Recruitment": "screeners, where to find people, over-recruiting against no-shows, hard-to-reach groups",
    "Sample Size": "where 'five users' comes from and when it breaks, plus quantitative sizing and saturation",
    "Research Validity": "internal versus external validity, sampling, and saying so when validity is sacrificed",
    "Bias in Research": "how recruiting, screening, task wording and moderation each inject bias",
    "Confirmation Bias": "investigating rather than validating, and triangulating against your own expectations",
    "Research Ethics": "informed consent, deception and debriefing, vulnerable populations, data across the lifecycle",
    "Research Operations": "panels, repositories, governance, standardisation, and why the work gets underestimated",
    "Data Analysis": "assessing data before interpreting it, thematic coding, affinity diagramming, statistical care",
    "AI in User Research": "where AI helps, where it fails, and the open disagreements between sources",
    "Young Users": "physical and cognitive development, teenagers, and consent and assent with minors",
    "Privacy": "the creepiness-convenience tradeoff, controls users expect, and consent in research",

    # Structure and findability
    "Information Architecture": "structure versus navigation, labels, hierarchy depth, search, and findability failures",
    "Navigation Design": "menu patterns, visible versus hidden, wayfinding, back navigation, long pages, mobile",
    "Information Scent": "writing labels that carry scent, and not promising what the click will not deliver",
    "Menu Design": "choosing a menu shape, mega menus, dropdown hierarchy, labels and touch targets",
    "Search": "precision and recall, the search interface, suggestions, and how AI changes retrieval",
    "Information Seeking": "designing for task type, results-page scanning, and the vocabulary problem",
    "Discoverability": "signifiers for invisible interactions, modes, and testing whether people find things",
    "Web Usability": "convention as default and deviation as cost, layout, links, trust, speed, forms",
    "Intranet Design": "the persistent internal-tool mistakes, plus crisis IA and post-merger structure",
    "Complex Applications": "locating where complexity actually sits, studying the domain, three user types",
    "Content Strategy": "writing for scanning, length under mobile constraint, and organising and labelling content",

    # Composition and visual
    "Visual Hierarchy": "the core techniques, colour as a hierarchy tool, and why prominence must be earned",
    "Information Design": "signal-to-noise, deliberate encoding, redundant cues, grouping with containers",
    "Progressive Disclosure": "breaking long tasks into steps, layering depth, and signalling that more exists",
    "Gestalt Principles": "proximity, similarity, common region and closure, applied inside visual design",
    "Aesthetic-Usability Effect": "the instant judgement and what it decides, and countering it during research",
    "Data Visualization": "the 3 Cs, choosing a chart type, dashboards, tables, and the perceptual limits",
    "Visual Design": "principles, grids, type, colour, imagery, first impressions, and validating the result",
    "Typography": "choosing and pairing typefaces, building hierarchy, spacing, and reading context",
    "Design Trends": "skeuomorphism, brutalism, neobrutalism and glassmorphism, and where each costs usability",
    "Flat Design": "the evidence on weak signifiers, when fully flat is defensible, and risk reduction",
    "Branding": "brand as an experience system, defining one before there is a product, interaction qualities that carry it, and not looking like an ad",
    "Emotional Design": "building on usability rather than instead of it, surface versus deep delight, peaks and endings",
    "Design Principles": "writing product-specific principles, and the visual-design principles the corpus uses",

    # Interaction
    "Interaction Design": "the widest component theme: feedback, mappings, motor constraints, modes, gestures, ethics",
    "Design Patterns": "deciding whether a pattern applies to you, plus controls, menus, disclosure and icons",
    "User Interface": "making objects and actions visible, choosing controls, dialogs and modes, evaluating the result",
    "Form Design": "asking for less, layout and sequencing, labels, validation, buttons, multi-step flows",
    "Modal Window": "questioning the pattern first, legitimate cases, timing, and why cancel is not close",
    "Feedback Design": "confirming the action registered fast, choosing the mechanism, encoding status redundantly",
    "Error Prevention": "designing for the inattentive user, confirmation dialogs used sparingly, defence in depth",
    "Error Messages": "placement, wording, the inline-validation timing tension, and recovery",
    "Notification Design": "classifying before designing, timing, intensity and fatigue, permission and the ethical line",
    "Affordance": "the learning cost of invisible interactions, icons as signifiers, signalling current state",
    "Animation": "using motion for a purpose, timing, scroll-triggered motion, and motion sensitivity",
    "Usability": "usability as a precondition rather than a finishing layer, and prioritising the problems found",
    "User Experience": "usability before delight, accumulated friction, and diagnosing an existing experience",
    "Usability Heuristics": "Nielsen's ten, one sub-section each, and where they bend outside software",
    "Heuristic Evaluation": "running an evaluation, expert review, cognitive walkthrough, and PURE scoring",
    "Learnability": "the three aspects to distinguish, measuring it, and the cost of innovation and invisibility",

    # Accessibility, content, mobile
    "Accessibility": "contrast, keyboard and focus, screen readers, alt text, targets, motion, and testing",
    "Localization": "how far to localise, regional conventions, trust conventions, and context of use",
    "User Expectations": "how design primes expectations, why perception lags performance, and sticky failures",
    "UX Writing": "writing for scanning, subheadings, labels and commands, plain language, framing ethics",
    "Email Design": "layout, imagery without the flyer trap, what the tests found on animation and emoji",
    "Documentation": "knowing which document you are writing and for whom, and designing it for updating",
    "Mobile Design": "mobile as its own medium: layout, touch, input, microsessions, content, and beyond the phone",
    "Responsive Design": "breakpoints, why porting is not adapting, images, tables, navigation across sizes",
    "Smart Devices": "whether to build at all, watch interactions, companion-app control, notifications as the core",
    "Augmented Reality": "whether AR adds value, realism and trust, discoverability, calibration, testing",
    "Voice Interfaces": "discoverability without a screen, the cost of listening, and which tasks voice suits",

    # Psychology and persuasion
    "Mental Model": "conform to the model or change it, borrowing from the real world, surfacing models in research",
    "Cognitive Load": "external memory, interruptions, what to remove, and whether hiding reduces or displaces load",
    "Cognitive Psychology": "attention, working memory and chunking, automatic processing, perception-action mapping",
    "User Behavior": "scanning patterns, learned conventions, filtering and avoidance, named behaviour patterns",
    "Interaction Cost": "why counting clicks fails, how hiding raises cost, and cost across a whole journey",
    "Cognitive Bias": "biases that shape user decisions, biases that distort the team, and the limits of awareness",
    # Laws of UX (Yablonski, 2024), 2026-09-10
    "Jakob's Law": "starting from the convention, who sets the expectation, what breaking the pattern costs, turning it into team rules",
    "Fitts's Law": "size before proximity, spacing, screen edges as infinite targets, reach by device and hand, menu shape",
    "Miller's Law": "chunk rather than count, why the seven-item navigation rule is a myth, how to chunk visually",
    "Hick's Law": "cutting the choices shown at once, weighting options, the floor below which simplifying hurts",
    "Postel's Law": "accepting input in the forms people give it, adapting to device capability, planning for language and typography",
    "Peak-End Rule": "designing deliberate peaks, why the ending counts double, defusing negative peaks, locating them first",
    "Von Restorff Effect": "the levers of contrast, signalling change on purpose, restraint, and contrast that excludes",
    "Tesler's Law": "which side carries the irreducible complexity, complexity mistaken for competence, managing what must stay visible",
    "Doherty Threshold": "the 400 ms mark, being perceived as fast, feedback during the wait, page weight, and delay added back on purpose",
    "Human Factors Engineering": "observing people where the work happens, measuring the human limit then designing to it, the lineage into HCI and UX",
    "Decision Making": "how users choose among alternatives, anchoring team decisions, auditing your own reasoning",
    "Behavioral Economics": "the named biases, choice architecture in copy, and reducing sludge rather than adding nudges",
    "Empathy": "direct exposure over reports, and empathy maps: what they are, when and how to build them",
    "Persuasive Design": "the psychological levers, sequencing the ask to earned trust, and refusing deception",
    "User Trust": "credibility signals, removing uncertainty in high-stakes purchases, calibrating trust in AI",
    "Deceptive Patterns": "the forms deception takes, telling persuasion from deception, and designing the honest version",
    "User Control": "exits, undo, predictable dismissal, overriding system decisions, and where control has limits",
    "Customization": "customisation versus personalisation, making it get used, and granular control against fatigue",
    "Personalization": "whether to personalise at all, building the user model conservatively, presenting recommendations",

    # Journeys and service
    "Customer Journey": "designing the journey rather than the touchpoint, mapping scope, and finding what breaks",
    "Journey Mapping": "one actor one scenario, the five-phase process, and not skipping the insights zone",
    "Service Design": "blueprinting as the core method, workshops, silos, and the whole delivery including physical",
    "Service Blueprinting": "what it is for, the five-step process, scope, facilitation, and the root cause of failure",
    "Omnichannel Experience": "mapping the ecosystem first, consistency, seamlessness, orchestration, the org condition",
    "Customer Experience": "the three levels, journey mapping as shared view, and operationalising CX at scale",
    "Persona": "grounding them in research, segmenting by behaviour, and getting the organisation to use them",
    "E-Commerce": "listing pages, filtering, product information, cart and payment trust, post-order service",

    # System, process, org
    "Design System": "what it contains, semantics and naming, governance and adoption, and its cautions",
    "Design Consistency": "standard patterns as default, auditing by dimension, and encoding consistency in systems",
    "DesignOps": "the nine-activity menu, where to start, role versus mindset, measurement and maturity",
    "Design Process": "problem before solution, research woven through, prototyping and iteration, how rigid to be",
    "Team Collaboration": "workshops as default format, shared artifacts, critique, dissent, and remote collaboration",
    "Workshop Facilitation": "preparation, who is in the room, explain-execute-examine, dominance and groupthink",
    "Ideation": "framing before generating, diverge then converge, breaking fixation, remote ideation, and finding a startup idea in the first place",
    "Design Thinking": "the four moves, it as a team practice, and where the sources push back on the framework",
    "Prototyping": "starting from the hypothesis not the tool, choosing fidelity, Wizard of Oz, handoff",
    # Added 2026-09-11 with Storytelling in Design (Dahlström), the second
    # work that pushed these three past the developed threshold.
    "Shared Understanding": "why documents do not create it, what a team must talk about, mapping and modelling together, how many people and for how long, and the limit of the idea",
    "Wireframing": "no drawing skill needed, why messy is the point, paper before the tool, wireframes as the story of a page, and Penchenat's argument that the era is over",
    "Iterative Design": "the loop and how many turns it takes, iterating in parallel, keeping fidelity low",
    "Agile Development": "fitting UX into the backlog, scaling discovery instead of skipping it, quality debt",
    "Remote Work": "team norms, synchronous versus asynchronous, and why familiar tools beat powerful ones",
    "Problem Framing": "outcomes before outputs, writing the problem and user-need statements, framing new technology",
    "Stakeholder Engagement": "aligning before the work starts, designing the meeting itself, listening before responding, showing the reasoning rather than the conclusion, locking in agreement, handling authority",
    "Design Critique": "structuring the session, listening before responding, the receiving mindset, forming a response, keeping it on track, and closing the loop afterwards",
    "Storytelling": "what a UX story is made of, turning research data into narrative, and the grounding problem",
    "Change Management": "mindset before operations, governance, actionable deliverables, and quiet maturity regression",
    "Organizational Culture": "culture as a maturity factor, incentives, team structure, trust across disciplines",
    "UX Maturity": "the four factors, what each stage looks like, moving up, and spotting regression",
    "Business Impact": "outcomes over outputs, leadership's language, and measuring the cost of a degraded experience",
    "User-Centered Design": "personas and jobs-to-be-done, holding the balance with business, the organisational end state",

    # Strategy and measurement
    "UX Strategy": "vision goals plan, roadmaps as the strategic artifact, and deciding under risk",
    "Product Strategy": "differentiation over feature parity, product-led growth, and deciding whether to build at all",
    "Product Design": "owning the business not only the user, moving from intuition to evidence, career posture",
    "Design": "designing for messy reality, designing around goals, and turning research into decisions",
    "Roadmapping": "choosing scope, the six-step process, prioritisation methods, timing and communication",
    "Prioritization": "choosing a method that fits the team, running a matrix, scoring versus comparing opportunities, and deciding not to build",
    "UX Metrics": "starting from goals, metric families, giving raw numbers context, baselines, reporting",
    "Analytics": "goals over what is easy to count, vanity metrics, site-search logs, connecting to business impact",
    "Conversion": "forms, speed, mobile, paywalls, exit moments, and not optimising the wrong metric",
    "User Retention": "retention as the counterweight to conversion, NPS limits, and intervening at departure",
    "User Engagement": "frequency and recency over bounce rate, designing for return, the ethics of engagement",
    "Onboarding": "testing whether onboarding is needed at all, contextual help over upfront tutorials, empty states",
    "User Feedback": "when and how to ask, and what qualitative feedback is good for and where it stops",

    # AI
    "Artificial Intelligence": "the mechanism before the capability, designing AI experiences, adopting AI in a team",
    "AI in Design": "where AI earns its place in design work, where it fails, and what it changes for the designer",
    "Generative AI": "how it is trained and what that implies, failure modes, and where it adds product value",
    "AI Product Design": "starting from the user problem, scoping narrowly, designing for probabilistic output",
    "AI Chatbots": "deciding whether chat is right at all, five qualities to design for, known conversational limits",
    "Large Language Model": "how the model is built, natural language as interface, specialising rather than using raw",
    "AI Agent": "judging whether an agent is useful, the want-attempt gap, agents as users of your interface",
    "AI Limitations": "the mechanism behind each failure, sycophancy, and where the tools fail task by task",
    "Prompt Engineering": "structuring the prompt, how prompt shape determines conversation shape, context design",

    # Career
    "UX Career": "career stages, specialist versus generalist, transitioning in, job search, resilience",
    "Portfolio": "curating rather than accumulating, showing impact in numbers, confidentiality constraints",
    "Case Study": "what one contains, telling it as a story, connecting decisions to business, the interview exercise",
    # Solving Product Design Exercises (Dashinsky, 2018), 2026-09-10
    "Design Hiring": "the shape of the process, what each step is measuring, running it from the hiring manager's seat, and where the sources disagree on tailoring",
    # Added 2026-09-11 with The Path to Senior Product Designer (Dashinsky).
    "Design Advocacy": "advocating a decision, pushing back on a bad suggestion without refusing it, advocating externally, and advocating for your own work",
    "Performance Review": "assessing yourself against something other than yourself, keeping a plan between reviews, turning scattered feedback into signals, and archiving what you actually did",
    "Design Strategy": "vision, goals and plan, learning the business you design for, choosing what to work on and when to stop, and the strategic skills themselves",
    "Productivity": "leverage over hours, protecting the conditions to ship, fixing the process rather than only your own habits, tooling, and designing for users who switch tasks",
    "Design Presentation": "knowing who is in the room, designing the meeting itself, choosing the message, responding to feedback, and closing the loop afterwards",
    "Design Leadership": "leading the conversation rather than the decision, holding the line on changes without refusing them, and what the organisation owes design in return",
    "Context of Use": "mapping the when-and-where variables first, letting context pick the device, social context, and worked examples where it became the constraint",
    "Value Proposition": "settling the value before the technology, leading with the benefit rather than the specification, and stating customer and business value together",
    # Venture Building and Studios (2026-09-03)
    "Venture Studio": "what a studio does that other models do not, where ideas come from, the platform, founders and equity, and where the two books disagree",
    "Studio Economics": "front-loaded costs and late returns, how to build the model, unit costs, intermediate revenue, exits and the best-in-class case",
    "Equity Ownership": "why a studio takes founding equity, how much (the books differ), dilution, ownership floors, common versus preferred",
    "Studio Fundraising": "funding the operating company versus raising a fund, the credibility barrier, closed-ended or evergreen, revenue as a substitute for capital",
    "Venture Capital": "how the studio model differs from VC, VC as investor in the studio, keeping ventures fundable, borrowing the fund structure",
    "Portfolio Strategy": "the portfolio as risk-management unit, how many ventures at what cost, market focus (where the books diverge), governance and killing",
    "Founder Recruitment": "what a studio offers a founder, who it looks for, sourcing models, cash and equity compensation, bringing founders in early",
    "Idea Validation": "why validate before building, methods including Hexa's interviews-writing-wireframes sequence, running ideas in parallel, time and budget, deciding and killing",
    "Studio Funnel": "stage structures, filling the top, scoring and budgeting, conversion rates, throughput, modelling the funnel",
    "Revenue Model": "the cash-flow gap, billing back launched companies, corporate co-builds and consulting, agency revenue, spending less instead",
    "Studio Team": "which competencies to hold in-house, structuring the team across ventures, founding composition, attracting and retaining talent",
    "Product-Market Fit": "confronting the market early, tools and cold calls to estimate fit, fit as a studio gate, design partners and one focus metric as early signals, timing, keeping fit once shipped",
    "Minimum Viable Product": "aim small and ship, prototype before the MVP, the MVP as a funnel step, viable versus loveable, one percent of the vision shipped in weeks",
    "Business Strategy": "diagnosis, guiding line and action plan, vision statements linking strategy to UX, planning a studio like a factory, and whether execution beats the idea (the books disagree)",
    "Innovation": "three scales: deviating from an interface standard, innovating in at least one dimension of an idea, and innovation as a studio's engine with its limits",
    "Team Compensation": "salary and equity in the early team, the concrete numbers (ESOP size, vesting, salary grids), founder equity splits, and where the payroll money comes from",
    "Team Scaling": "scaling research through operations, a design system without more people, and a studio scaling authority without a management layer",
}
