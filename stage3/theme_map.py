"""Curated thematic map: theme -> rank-1 `developed` concepts.

The stage-3 counterpart of stage2/merge_map.py. This is the one piece the
corpus cannot re-derive: co-occurrence clustering proposes, this map decides.
Edit here, then re-run generate_themes.py.

A concept may belong to several themes (multiple attachment is deliberate:
32 of 147). verify_wiki.py enforces the reverse constraint: every `developed`
concept belongs to at least one theme.

Rank 2 (stubs and single-source concepts) is NOT curated here. It is derived
from the records by generate_themes.py.

Names are English and ASCII-only, per docs/adr/0002 (English is the corpus
language) and docs/adr/0003 (theme names must not collide with concept names,
and precomposed accents broke wikilinks once already at stage 2).
"""

THEMES = {
    "Choosing and Running Research": [
        "Research Methods", "User Research", "Usability Testing", "Qualitative Research",
        "Quantitative Research", "User Interviews", "Survey Design", "Field Studies",
        "Remote Research", "Eye Tracking", "Card Sorting", "Task Design", "Benchmarking",
        "A-B Testing", "Product Discovery", "Active Listening",
    ],
    "Research Rigour and Ethics": [
        "Study Design", "Research Planning", "Participant Recruitment", "Sample Size",
        "Research Validity", "Bias in Research", "Confirmation Bias", "Research Ethics",
        "Research Operations", "Young Users", "Data Analysis", "AI in User Research",
        "Privacy",
    ],
    "Structure, Navigation and Findability": [
        "Information Architecture", "Navigation Design", "Information Scent", "Menu Design",
        "Search", "Information Seeking", "Discoverability", "Web Usability",
        "Intranet Design", "Complex Applications", "Card Sorting", "Content Strategy",
    ],
    "Page Composition and Hierarchy": [
        "Visual Hierarchy", "Information Design", "Eye Tracking", "Progressive Disclosure",
        "Gestalt Principles", "Aesthetic-Usability Effect", "Data Visualization",
        "Web Usability",
    ],
    "Interaction and Interface Patterns": [
        "Interaction Design", "Design Patterns", "User Interface", "Form Design",
        "Modal Window", "Feedback Design", "Error Prevention", "Error Messages",
        "Notification Design", "Affordance", "Animation", "Progressive Disclosure",
    ],
    "Usability Heuristics and Evaluation": [
        "Usability", "User Experience", "Usability Heuristics", "Heuristic Evaluation",
        "Learnability", "Design Principles", "Error Prevention",
        "Aesthetic-Usability Effect", "Benchmarking",
    ],
    "Visual Design Craft": [
        "Visual Design", "Typography", "Design Trends", "Flat Design", "Branding",
        "Emotional Design", "Gestalt Principles", "Design Principles", "Animation",
    ],
    "Content and Interface Writing": [
        "Content Strategy", "UX Writing", "Email Design", "Documentation",
        "Error Messages", "Localization",
    ],
    "Accessibility and Inclusion": [
        "Accessibility", "Localization", "Young Users", "User Expectations",
    ],
    "Mobile and Multi-Device": [
        "Mobile Design", "Responsive Design", "Smart Devices", "Augmented Reality",
        "Voice Interfaces", "Discoverability",
    ],
    # The ten pages from Laws of UX (2026-09-10) sit here at rank 1 although
    # they are `stub`: one book is one work, so the two-works rule of ADR 0005
    # keeps them out of `developed` for good, while each carries a written
    # Definition and Practice. Left at rank 2 they were truncated away by
    # MAX_RANK2 and reachable only from wiki/index.md. Rank 1 is curation, and
    # this is the curation call: a named law is exactly what someone opens this
    # theme to find. Deliberately all in this one theme, none in a
    # PLAYBOOK_THEMES entry, so no playbook goes stale on their account.
    "Psychology, Cognitive Load and Behaviour": [
        "Mental Model", "Cognitive Load", "Cognitive Psychology", "User Behavior",
        "Interaction Cost", "Cognitive Bias", "Decision Making", "Behavioral Economics",
        "User Expectations", "Empathy",
        "Jakob's Law", "Fitts's Law", "Miller's Law", "Hick's Law", "Postel's Law",
        "Peak-End Rule", "Von Restorff Effect", "Tesler's Law", "Doherty Threshold",
        "Human Factors Engineering",
    ],
    "Persuasion, Trust and Design Ethics": [
        "Persuasive Design", "User Trust", "Deceptive Patterns", "Privacy",
        "Behavioral Economics", "User Control", "Customization", "Personalization",
    ],
    "Journeys, Service and Omnichannel": [
        "Customer Journey", "Journey Mapping", "Service Design", "Service Blueprinting",
        "Omnichannel Experience", "Customer Experience", "Persona", "E-Commerce",
        "Context of Use",
        # Added 2026-09-11 with Storytelling in Design (Dahlström). User Flow is
        # the step-level view of the journey this theme routes to.
        "User Flow",
    ],
    "Design Systems and Consistency": [
        "Design System", "Design Consistency", "Design Principles", "Typography",
        "DesignOps", "Documentation",
    ],
    "Design Process and Collaboration": [
        "Design Process", "Team Collaboration", "Workshop Facilitation", "Ideation",
        "Design Thinking", "Prototyping", "Iterative Design", "Agile Development",
        "Remote Work", "Problem Framing", "Team Scaling", "Design Critique",
        # Added 2026-09-11: shipping conditions, leverage over hours, and
        # improving the process the team works in.
        "Productivity",
        # Added 2026-09-11 with User Story Mapping (Patton). Story Mapping is
        # a group activity before it is an artefact, and Product Trio is the
        # unit that runs it; both also sit under Product Strategy and Framing
        # where the framing question is what to build rather than how to work.
        "Story Mapping", "Product Trio",
        # Added 2026-09-11 with Storytelling in Design (Dahlström). Shared
        # Understanding is what the artefacts of this theme are for; Wireframing
        # sits beside Prototyping as the other low-fidelity way a team argues
        # about a design before building it.
        "Shared Understanding", "Wireframing",
    ],
    "Influence, Stakeholders and UX Maturity": [
        "Stakeholder Engagement", "Storytelling", "Change Management",
        "Organizational Culture", "UX Maturity", "DesignOps", "Business Impact",
        "User-Centered Design", "Decision Making", "Design Critique",
        "Design Presentation", "Design Leadership", "Active Listening",
        # Added 2026-09-11 with The Path to Senior Product Designer.
        "Design Advocacy",
    ],
    "Product Strategy and Framing": [
        "UX Strategy", "Product Strategy", "Product Discovery", "Product Design",
        "Problem Framing", "Roadmapping", "Prioritization", "Design",
        "Product-Market Fit", "Minimum Viable Product", "Business Strategy", "Innovation",
        "Value Proposition",
        # Added 2026-09-11: the page carries both altitudes, NN/g's
        # organisational UX strategy and the individual competency.
        "Design Strategy",
        # Added 2026-09-11 with Product Management for UX People (Crumlish).
        # Product Management is the discipline page the corpus lacked a home
        # for; Assumption Testing is the discovery-side counterpart to
        # A-B Testing, which sits in Measurement.
        "Product Management", "Assumption Testing",
        # Added 2026-09-11 with User Story Mapping (Patton). The book pushed
        # Story Mapping and Product Outcome past the developed threshold; both
        # answer "what do we build next and why", which is this theme.
        "Story Mapping", "Product Outcome",
    ],
    "Measurement, Metrics and Business Impact": [
        "UX Metrics", "Analytics", "Conversion", "Business Impact", "A-B Testing",
        "Benchmarking", "User Retention", "User Engagement",
        # Added 2026-09-11 with Product Management for UX People (Crumlish):
        # chapter 7 puts A/B tests and their twelve alternatives on one page.
        "Assumption Testing",
        # Added 2026-09-11 with User Story Mapping (Patton): the page now
        # carries both the outcome vocabulary and how to measure it.
        "Product Outcome",
    ],
    "Adoption, Onboarding and Engagement": [
        "Onboarding", "Learnability", "User Engagement", "User Retention", "Conversion",
        "User Feedback",
    ],
    "Designing With and For AI": [
        "Artificial Intelligence", "AI in Design", "Generative AI", "AI Product Design",
        "AI Chatbots", "Large Language Model", "AI Agent", "AI Limitations",
        "Prompt Engineering", "AI in User Research", "Voice Interfaces",
    ],
    "Career, Portfolio and Case Study": [
        "UX Career", "Portfolio", "Case Study", "Documentation",
        # Added 2026-09-10 with Solving Product Design Exercises (Dashinsky).
        "Design Hiring",
        # Added 2026-09-11 with The Path to Senior Product Designer (Dashinsky).
        # Performance Review is the checkpoint the career ladder is judged at;
        # Design Advocacy sits here for the personal-brand half and in
        # Influence for the champion-the-user half.
        "Performance Review", "Design Advocacy",
        # Added 2026-09-11 with Product Management for UX People (Crumlish):
        # the UX-to-product move is a career fork the page now documents, so
        # Product Management is rank 1 here as well as in Product Strategy.
        "Product Management",
    ],
    # Added 2026-09-03 with the two studio books (docs/adr/0005). The product
    # concepts the books also feed (PMF, MVP, strategy, innovation, scaling)
    # sit here AND in their discipline theme.
    "Venture Building and Studios": [
        "Venture Studio", "Studio Economics", "Equity Ownership", "Venture Capital",
        "Studio Fundraising", "Founder Recruitment", "Portfolio Strategy",
        "Idea Validation", "Studio Funnel", "Revenue Model", "Studio Team",
        "Product-Market Fit", "Minimum Viable Product", "Business Strategy",
        "Innovation", "Team Scaling", "Team Compensation",
    ],
}

# Themes whose rank-1 concepts are distilled into a playbook (docs/adr/0004).
# Only themes a design review actually runs against. The other 16 stay
# navigate-only.
PLAYBOOK_THEMES = [
    "Usability Heuristics and Evaluation",
    "Page Composition and Hierarchy",
    "Interaction and Interface Patterns",
    "Accessibility and Inclusion",
    "Mobile and Multi-Device",
    "Structure, Navigation and Findability",
]
