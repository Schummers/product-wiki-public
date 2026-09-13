"""Stage 2 merge map: candidate concept name -> canonical concept name.

Hand-curated (strong model judgment, 2026-07-31). Applied by apply_merge.py.
Every key becomes an alias of its value. Names not in this map and not a
canonical target keep their own identity.
"""

MERGES = {
    # --- research umbrella ---
    "UX Research": "User Research",
    "User Research Methods": "Research Methods",
    "UX Research Methods": "Research Methods",
    "Research Methodology": "Research Methods",
    "Research Design": "Study Design",
    "User Testing": "Usability Testing",
    "Usability Evaluation": "Usability Testing",
    "User Testing Methods": "Usability Testing",
    "Moderation": "Usability Testing",
    "Moderation Techniques": "Usability Testing",
    "Qualitative Research Methods": "Qualitative Research",
    "Survey Research": "Survey Design",
    "Question Design": "Survey Design",
    "Open-Ended Questions": "Survey Design",
    "Interviewing": "User Interviews",
    "Interview Preparation": "User Interviews",
    "Stakeholder Interviews": "User Interviews",
    "Contextual Inquiry": "Field Studies",
    "Ethnographic Research": "Field Studies",
    "Observation Methods": "Field Studies",
    "Participant Screening": "Participant Recruitment",
    "Participant Incentives": "Participant Recruitment",
    "Screening": "Participant Recruitment",
    "Informed Consent": "Research Ethics",
    "Research Validity": "Research Validity",  # canonical
    "Statistical Validity": "Research Validity",
    "Measurement Error": "Research Validity",
    "Reliability and Repeatability": "Research Validity",
    "Research Rigor": "Research Validity",
    "Research Bias": "Bias in Research",
    "Remote Testing": "Remote Research",
    "Eyetracking": "Eye Tracking",
    "Eyetracking Research": "Eye Tracking",
    "Usability Inspection": "Heuristic Evaluation",
    "Expert Review": "Heuristic Evaluation",
    "Usability Metrics": "UX Metrics",
    "UX Measurement": "UX Metrics",
    "Measurement": "UX Metrics",
    "Measurement Strategy": "UX Metrics",
    "Analytics and Metrics": "Analytics",
    "Metrics and Analytics": "Analytics",
    "Data Analytics": "Analytics",
    "Research Synthesis": "Data Analysis",
    "Data Interpretation": "Data Analysis",
    "Data Collection": "Data Analysis",
    "Data Synthesis": "Data Analysis",
    "Research Communication": "Storytelling",
    "Design Communication": "Storytelling",
    "ResearchOps": "Research Operations",
    "AI Research": "AI in User Research",
    "AI in Research": "AI in User Research",

    # --- design process & collaboration ---
    "UX Design Process": "Design Process",
    "UX Process": "Design Process",
    "UX Workflow": "Design Process",
    "Iteration": "Iterative Design",
    "Parallel Design": "Iterative Design",
    "Collaboration": "Team Collaboration",
    "Cross-Functional Collaboration": "Team Collaboration",
    "Cross-functional Collaboration": "Team Collaboration",
    "Team Alignment": "Team Collaboration",
    "Team Dynamics": "Team Collaboration",
    "Design Collaboration": "Team Collaboration",
    "Collaborative Design": "Team Collaboration",
    "Communication": "Team Collaboration",
    "Communication Skills": "Team Collaboration",
    "Remote Collaboration": "Remote Work",
    "Stakeholder Alignment": "Stakeholder Engagement",
    "Stakeholder Management": "Stakeholder Engagement",
    "Stakeholder Communication": "Stakeholder Engagement",
    "Consensus Building": "Stakeholder Engagement",
    "Organizational Alignment": "Stakeholder Engagement",
    "Common Ground": "Stakeholder Engagement",
    "Facilitation": "Workshop Facilitation",
    "Facilitation Skills": "Workshop Facilitation",
    "Group Facilitation": "Workshop Facilitation",
    "Workshop Design": "Workshop Facilitation",
    "UX Workshops": "Workshop Facilitation",
    "Design Workshop": "Workshop Facilitation",
    "Group Dynamics": "Workshop Facilitation",
    "Meeting Management": "Workshop Facilitation",
    "Brainstorming": "Ideation",
    "Group Ideation": "Ideation",
    "Design Exploration": "Ideation",
    "Design Critique": "Design Critique",  # canonical
    "Design Documentation": "Documentation",
    "Product Documentation": "Documentation",
    "Design Deliverables": "Documentation",
    "Design Artifacts": "Documentation",
    "Design Testing": "Usability Testing",
    "Visual Design Testing": "Usability Testing",

    # --- AI cluster ---
    "AI Agents": "AI Agent",
    "Intelligent Assistants": "AI Agent",
    "Large Language Models": "Large Language Model",
    "Natural Language Processing": "Artificial Intelligence",
    "AI Capabilities": "Artificial Intelligence",
    "Machine Learning": "Artificial Intelligence",
    "AI Hallucinations": "AI Limitations",
    "AI Bias": "AI Limitations",
    "AI in Design Tools": "AI in Design",
    "AI Tools": "AI in Design",
    "AI and Design": "AI in Design",
    "AI in UX": "AI in Design",
    "AI Design Tools": "AI in Design",
    "AI Usability": "AI User Experience",
    "AI Feature Design": "AI Product Design",
    "AI Product Strategy": "AI Product Design",
    "Conversational Interfaces": "AI Chatbots",
    "Conversational Interface": "AI Chatbots",
    "Conversational UI": "AI Chatbots",
    "Conversational Agent": "AI Chatbots",
    "Prompt Design": "Prompt Engineering",
    "Prompt Structure": "Prompt Engineering",
    "Prompt Suggestions": "Prompt Engineering",
    "Content Generation": "Generative AI",
    "Human-AI Collaboration": "Human-AI Collaboration",  # canonical

    # --- psychology & behavior ---
    "Psychology and UX": "Cognitive Psychology",
    "User Psychology": "Cognitive Psychology",
    "Priming": "Cognitive Psychology",
    "Choice Architecture": "Behavioral Economics",
    "Loss Aversion": "Behavioral Economics",
    "Choice Overload": "Decision Making",
    "Decision-Making": "Decision Making",
    "Mental Models": "Mental Model",
    "User Mental Models": "Mental Model",
    "User Perception": "User Expectations",
    "User Preferences": "User Expectations",
    "Behavior Patterns": "User Behavior",
    "User Behavior Patterns": "User Behavior",
    "User Motivation": "User Behavior",
    "Persuasion": "Persuasive Design",
    "Behavioral Design": "Persuasive Design",
    "User Delight": "Emotional Design",
    "First Impressions": "Aesthetic-Usability Effect",
    "Aesthetic Evaluation": "Aesthetic-Usability Effect",

    # --- IA / navigation / search ---
    "Wayfinding": "Navigation Design",
    "Navigation": "Navigation Design",
    "Navigation Patterns": "Navigation Design",
    "Mobile Navigation": "Navigation Design",
    "Navigation Menu": "Menu Design",
    "Findability": "Information Architecture",
    "Metadata": "Information Architecture",
    "Content Organization": "Information Architecture",
    "Site Search": "Search",
    "Search Suggestions": "Search",
    "Search Engine Results Pages": "Search",
    "Semantic Search": "Search",
    "Search Behavior": "Information Seeking",
    "Information Foraging": "Information Scent",
    "Information Scannability": "Reading Behavior",

    # --- content & writing ---
    "Web Writing": "UX Writing",
    "UI Copy": "UX Writing",
    "Microcontent": "UX Writing",
    "Content Design": "Content Strategy",
    "Content Structure": "Content Strategy",
    "Readability": "Typography",
    "Legibility": "Typography",

    # --- visual design ---
    "Visual Attention": "Visual Hierarchy",
    "Design Aesthetics": "Visual Design",
    "Color and Contrast": "Visual Design",
    "Visual Design Trends": "Design Trends",
    "Glassmorphism": "Design Trends",
    "Neobrutalism": "Design Trends",
    "Skeuomorphism": "Design Trends",
    "Brand Perception": "Branding",
    "Brand Recall": "Branding",
    "Image Optimization": "Imagery",
    "Icon Usability": "Icon Design",
    "Animation": "Animation",  # canonical

    # --- UI patterns ---
    "Interaction Patterns": "Design Patterns",
    "Web Design Patterns": "Design Patterns",
    "UI Components": "Design System",
    "Component Libraries": "Design System",
    "Design Systems": "Design System",
    "UI Design": "User Interface",
    "Interface Design": "User Interface",
    "User Interface Design": "User Interface",
    "Form Elements": "Form Design",
    "Button States": "Button Design",
    "Modal Dialogs": "Modal Window",
    "Overlay Design": "Overlay",
    "Human-Computer Interaction": "Interaction Design",
    "Gesture-Based Interaction": "Mobile Design",
    "Mobile UX": "Mobile Design",
    "Mobile Usability": "Mobile Design",
    "Mobile App Design": "Mobile Design",
    "Mobile Applications": "Mobile Design",
    "Mobile Design Patterns": "Mobile Design",
    "Touchscreen Design": "Mobile Design",
    "Smartwatch Design": "Smart Devices",
    "System Feedback": "Feedback Design",
    "Visual Feedback": "Feedback Design",
    "System Status Visibility": "Feedback Design",
    "Notifications": "Notification Design",
    "Error Handling": "Error Messages",
    "Slip (Error)": "Error Prevention",
    "Learning Curves": "Learnability",
    "Signifiers": "Affordance",
    "Web Design": "Web Usability",
    "Link Design": "Web Usability",

    # --- journeys / service design ---
    "Customer Journeys": "Customer Journey",
    "User Journeys": "Customer Journey",
    "Journey-Centric Design": "Customer Journey",
    "Customer Journey Mapping": "Journey Mapping",
    "UX Mapping": "Journey Mapping",
    "Service Blueprint": "Service Blueprinting",
    "Omnichannel": "Omnichannel Experience",
    "Omnichannel Design": "Omnichannel Experience",
    "Cross-Channel Design": "Omnichannel Experience",
    "Cross-Channel Experience": "Omnichannel Experience",
    "Customer Experience": "Customer Experience",  # canonical
    "Customer Communication": "Customer Experience",
    "Customer Loyalty": "User Retention",
    "Churn": "User Retention",

    # --- strategy / business / org ---
    "Strategy": "UX Strategy",
    "Strategic Planning": "UX Strategy",
    "Strategic Thinking": "UX Strategy",
    "Strategic UX": "UX Strategy",
    "Business Value": "Business Impact",
    "Business Goals": "Business Impact",
    "Conversion Optimization": "Conversion",
    "Conversion Rate": "Conversion",
    "UX Roadmaps": "Roadmapping",
    "Feature Prioritization": "Prioritization",
    "Organizational Change": "Change Management",
    "Organizational Design": "Organizational Culture",
    "Organizational Structure": "Organizational Culture",
    "Organizational Process": "Organizational Culture",
    "Organizational Strategy": "Business Strategy",
    "Organizational Assessment": "UX Maturity",
    "Design Operations": "DesignOps",
    "Agile Methodology": "Agile Development",
    "Discovery Phase": "Product Discovery",
    "Discovery Process": "Product Discovery",
    "Problem Definition": "Problem Framing",
    "Problem-First Design": "Problem Framing",

    # --- careers ---
    "UX Careers": "UX Career",
    "Career Development": "UX Career",
    "UX Career Development": "UX Career",
    "UX Career Trends": "UX Career",
    "Career Transitions": "UX Career",
    "Career Resilience": "UX Career",
    "Job Search Strategy": "UX Career",
    "Professional Development": "UX Career",
    "Professional Networking": "UX Career",
    "Resume Writing": "UX Career",
    "Portfolio Design": "Portfolio",
    "Portfolio Management": "Portfolio",

    # --- users & audiences ---
    "Personas": "Persona",
    "User Segmentation": "Persona",
    "Children's UX": "Young Users",
    "Digital Natives": "Young Users",
    "Internationalization": "Localization",
    "International UX": "Localization",
    "Cultural Design": "Localization",
    "Assistive Technology": "Accessibility",
    "Accessibility in Design": "Accessibility",
    "User Onboarding": "Onboarding",
    "User Education": "Onboarding",
    "User Guidance": "Onboarding",
    "User Trust": "User Trust",  # canonical
    "Trust": "User Trust",
    "Trust Building": "User Trust",
    "Trust and Credibility": "User Trust",
    "Trust and Verification": "User Trust",
    "User Needs": "User Research",
    "User Goals": "User Research",

    # --- domains ---
    "E-commerce": "E-Commerce",
    "E-commerce Design": "E-Commerce",
    "E-commerce UX": "E-Commerce",
    "E-Commerce UX": "E-Commerce",
    "Payment Systems": "E-Commerce",
    "Comparison Tables": "E-Commerce",
    "Email Communication": "Email Design",
    "Intranets": "Intranet Design",
    "Dashboard Design": "Data Visualization",
    "Dark Patterns": "Deceptive Patterns",
    "Dark Pattern": "Deceptive Patterns",
    "Data Protection": "Privacy",
    "GDPR": "Privacy",
    "Password Management": "Authentication",
    "Perceived Performance": "Web Performance",
    "Augmented Reality Design": "Augmented Reality",
    "UX Design": "User Experience",
    "Low-Fidelity Prototypes": "Prototyping",
    "Mixed-Methods Research": "Mixed-Methods Research",  # canonical
    "Task Complexity": "Task Design",
    "In-App Feedback": "User Feedback",
    "Pain Points": "User Research",
    "Vibe Design": "Vibe Coding",
    "Interviewer Metrics": "User Interviews",
}

# --- design hiring, 2026-09-10 ---
# In a product/design corpus "Hiring and Recruitment" is design hiring; the one
# NNg record citing it means the same thing as the Dashinsky chapters.
MERGES["Hiring and Recruitment"] = "Design Hiring"

# --- books, 2026-09-03 (docs/adr/0005) ---
# Applied ONLY to the book records (apply_merge.py --only <slug>), layered
# over MERGES with precedence. Three keys deliberately override a global
# rule: in a studio book "Portfolio Management" is the venture portfolio,
# not a UX portfolio; "Team Dynamics" is studio culture; "Organizational
# Structure" is the studio's legal structure, not its culture. The extra
# vocabulary keys ("Venture Builder", "Company Builder"...) are not cited by
# any record: they exist to become aliases, so the next book converges.
BOOK_MERGES = {
    "Startup Studio": "Venture Studio",
    "Venture Builder": "Venture Studio",
    "Company Builder": "Venture Studio",
    "Startup Factory": "Venture Studio",
    "Startup Studios": "Venture Studio",
    "Venture Studios": "Venture Studio",
    "Startup Success Repeatability": "Venture Studio",
    "Studio Fund": "Studio Fundraising",
    "Studio Financing": "Studio Fundraising",
    "Fund Type": "Studio Fundraising",
    "Product Validation": "Idea Validation",
    "Portfolio Management": "Portfolio Strategy",
    "Portfolio Companies": "Portfolio Strategy",
    "Cash Flow Modeling": "Studio Economics",
    "Financial Viability": "Studio Economics",
    "Studio Financial Model": "Studio Economics",
    "Founder Cash": "Team Compensation",
    "Founder Financing": "Team Compensation",
    "Founder Compensation": "Team Compensation",
    "Team Dynamics": "Studio Culture",
    "Organizational Values": "Studio Culture",
    "Ritual": "Studio Culture",
    "Talent Retention": "Studio Team",
    "Skill Matrix": "Studio Team",
    "Core Team": "Studio Team",
    "Agency Revenue Model": "Revenue Model",
    "Studio Revenue": "Revenue Model",
    "Secondary Sales": "Exit Strategy",
    "Exit Outcomes": "Exit Strategy",
    "Investor Mindset": "Venture Capital",
    "Leadership Development": "Studio Leadership",
    "Organizational Structure": "Studio Structure",
    "EIR": "Entrepreneur in Residence",
    "Go/No-Go Decision": "Stage Gate",
    "Stage Gates": "Stage Gate",
    "Corporate Venture Builder": "Corporate Venture Building",
    "Corporate Venture Studio": "Corporate Venture Building",
    # Continuous Discovery Habits (Torres, 2021), 2026-09-03
    "Continuous Discovery": "Product Discovery",
    "Customer Understanding": "Product Discovery",
    "Desired Outcome": "Product Outcome",
    "Measuring Impact": "Product Outcome",
    "Leading Indicators": "Product Outcome",
    "Iterative Process": "Iterative Design",
    "HiPPO": "Stakeholder Engagement",
    "Retrospectives": "Continuous Improvement",
    "Keystone Habit": "Continuous Interviewing",
    "Resources": "UX Career",
    "Learning Community": "UX Career",
    "Practice": "UX Career",
    # The 10x Method (Hexa, 2026), 2026-09-08
    # Chapter 1 trait "build resilience through purpose" is one of the ten
    # founder traits, not a concept of its own.
    "Resilience": "Founder Mindset",
    # Articulating Design Decisions (Tom Greever, 2020), 2026-09-10
    # "Trust Building" is already an alias of "User Trust", which means the
    # user's trust in an interface; here it is the stakeholder's trust in the
    # designer ("the bank account of trust"), so the book overrides it.
    "Trust Building": "Stakeholder Engagement",
    "Design Maturity": "UX Maturity",
    # Solving Product Design Exercises (Dashinsky, 2018), 2026-09-10
    # "Design Framework" is the book's own seven-step answer method, not a
    # generic design process: it belongs to the exercise, not to Design Process.
    "Design Framework": "Design Exercise",
    "Design Career Path": "UX Career",
    "Design Interview": "Design Hiring",
    "Personal Branding": "Portfolio",
    # "Problem Solving" was mapped to "Ideation" here on 2026-09-10 and the
    # entry then removed, which is NOT the same as never having mapped it.
    # apply_merge.py had already run: record 12 (Step 4: List ideas) cited both
    # names, so the merge dropped the redundant one and the record now cites
    # Ideation alone. Removing the key un-stamps the alias, not the rewrite.
    #
    # It was removed because 2016-07-31_design-thinking uses the same words for
    # defining the problem before solving it, while record 12 means exploring a
    # wider spectrum of solutions. One name, two senses: the alias made
    # verify_wiki demand a backlink the older record cannot earn.
    #
    # Consequence to know before replaying this book from fresh stage 1 records:
    # "Problem Solving" will come back as a candidate on record 12 and has to be
    # dropped by hand again. Do not re-add the key to make the run reproducible
    # (fold_records.py --write refuses it now, correctly).
    # Vocabulary keys, cited by no record: they exist as aliases so the next
    # source on design interviews converges instead of coining its own name.
    "Whiteboard Challenge": "Design Exercise",
    "Take-Home Exercise": "Design Exercise",
    "Design Challenge": "Design Exercise",
    # NOT "Product Sense": 2026-07-24_product-sense-definition (NN/g) defines it
    # as pattern-matching past outcomes and explicitly rejects the loose sense
    # this book's "product thinking" carries. Two names, two ideas, kept apart.
    # Laws of UX (Jon Yablonski, 2nd ed. 2024), 2026-09-10
    # Rule applied to this book's sidebars: a "PSYCHOLOGY CONCEPT" box whose
    # subject has no page of its own folds into Cognitive Psychology, unless it
    # is named as a bias, in which case it folds into Cognitive Bias.
    "Automatic Cognitive Processing": "Cognitive Psychology",
    "Selective Attention": "Cognitive Psychology",
    "Flow State": "Cognitive Psychology",
    "Memory Bias": "Cognitive Bias",
    "Complexity Bias": "Cognitive Bias",
    "Negativity Bias": "Cognitive Bias",
    # Each law absorbs the paraphrases its own chapter coined for it.
    # "Robustness Principle" is Postel's law's other name, stated in chapter 5.
    "Robustness Principle": "Postel's Law",
    "User Input Flexibility": "Postel's Law",
    "Design Resiliency": "Postel's Law",
    # Chapter 3 is explicit that Miller's real contribution was chunking, not
    # the number seven. NOT "Task Chunking", which in this corpus means
    # breaking a to-do list into steps (2024-10-01_348_TWL), a different idea.
    "Chunking": "Miller's Law",
    "Working Memory": "Miller's Law",
    "Paradox of Choice": "Hick's Law",
    # Chapter 2 is about distance and size of a target: the size half is the
    # existing Tap Area page, the distance half belongs to the law itself.
    "Touch Target Design": "Tap Area",
    "Interactive Element Spacing": "Tap Area",
    "User Interface Positioning": "Fitts's Law",
    "Contrast": "Visual Hierarchy",
    # Also cited by 2024-12-06_experience-design, which uses it in the same
    # sense (the philosophy behind UCD); that page gets the backlink by hand.
    "Human-Centered Design": "User-Centered Design",
    # Just Enough Research (Erika Hall, A Book Apart, 2013), 2026-09-10
    # The book argues for research rather than naming new methods, so most of
    # its candidates already had a page. These are the coinages.
    # "Research Benefits" (foreword + chapter 1) is the payoff argument, not a
    # method: it belongs to the umbrella page, whose Practice already covers
    # making findings land in an organisation.
    "Research Benefits": "User Research",
    # Chapter 1 defines "design research" against pure and applied research;
    # in this corpus that umbrella is User Research (alias "UX Research").
    "Design Research": "User Research",
    # Chapter 1's Segway argument is about the circumstances a product has to
    # fit into, which is exactly what Context of Use means here.
    "Context in Design": "Context of Use",
    # Chapter 6 presents SWOT inside competitive research, not as a strategy
    # tool of its own. "Competitive Analysis" was an orphan until this book.
    "SWOT Analysis": "Competitive Analysis",
    "Split Testing": "A-B Testing",
    "Brand Positioning": "Branding",
    # Chapter 4 ("workflow") and chapter 8 ("task analysis/workflow") mean the
    # same thing: breaking work into steps to see where a system fits. New
    # canonical name; the corpus mentions task analysis in four page bodies but
    # had no page for it. NOT "Task Design", which here means writing the tasks
    # of a usability test.
    "Workflow Analysis": "Task Analysis",
    # NOT "Organizational Structure": already an alias of Organizational
    # Culture in the corpus AND a BOOK_MERGES key pointing at Studio Structure
    # since the studio books. One name, two senses, and a dict has one value
    # per key. Chapter 4's record was hand-edited to cite Organizational
    # Culture directly, so no key is needed and the studio alias is untouched.
    # Replaying this book from fresh stage 1 records means redoing that edit.
    # --- UX Research (Nunnally and Farkas, 2016), 2026-09-10 ---
    # Chapter 12 means capturing observations while the session is still
    # running (spreadsheets, affinity walls, highlight reels), which is the
    # front half of what Data Analysis already covers ("Data Collection",
    # "Data Synthesis" are aliases of it). NOT "Tracking Plan", which in this
    # corpus is analytics instrumentation.
    "Data Tracking": "Data Analysis",
    # Vocabulary keys, cited by no record: they exist so the next research
    # book converges on the page this one creates.
    "Body Language": "Nonverbal Communication",
    "Microexpressions": "Nonverbal Communication",
    "Nonverbal Cues": "Nonverbal Communication",
    "Debrief": "Debrief Session",
    "Debriefing": "Debrief Session",
    "Debrief Sessions": "Debrief Session",
    # NOT "Fitts Law" (no possessive), which 2016-05-08_expandable-menus cites.
    # Registering it as an alias here would make fold_records refuse the write:
    # the older record is already processed, so it could not earn the backlink
    # verify_wiki.py would then demand. Same law, but its link stays dangling
    # until a global pass can retarget that record too.
    # --- The Path to Senior Product Designer (Dashinsky, 2023), 2026-09-11 ---
    # The candidate list handed to stage 1 held, so the tally came back with
    # no two names for one idea and nothing to redirect. What follows is
    # vocabulary only: keys cited by no record, registered so the next career
    # book converges on the pages this one creates.
    # NOT "Career Progression", which 2024-08-16_stages-of-ux-career-progression
    # already cites: that record is processed, so stamping the alias here would
    # make fold_records refuse the write over a backlink it cannot earn. It
    # stays an orphan until a global pass can retarget it.
    "Competency Matrix": "Design Competencies",
    "Competencies Matrix": "Design Competencies",
    "Design Competency": "Design Competencies",
    "Design Titles": "Career Ladder",
    "Design Levels": "Career Ladder",
    "Levelling": "Career Ladder",
    "Growth Plan": "Career Growth Plan",
    "Career Growth Canvas": "Career Growth Plan",
    "Getting Promoted": "Promotion",
    "Mentoring": "Mentorship",
    # NOT "Ownership" alone: too generic for a filename in this corpus.
    "Design Ownership": "Design Ownership",  # canonical
    # --- Product Management for UX People (Crumlish, 2022), 2026-09-11 ---
    # The candidate list handed to stage 1 held: 34 distinct names across
    # 14 records, 33 of them already pages. The only coinage was
    # "Estimation" (chapter 4), which there means how engineers size
    # sprint work and how a PM negotiates around it -- the Agile Development
    # page already covers that, and the same record cites it.
    "Estimation": "Agile Development",
    # Vocabulary only: keys cited by no record, registered so the next
    # product-management book converges instead of coining.
    "Effort Estimation": "Agile Development",
    "Story Points": "Agile Development",
    "Product Owner": "Agile Development",
    "Definition of Done": "Agile Development",
    # --- User Story Mapping (Jeff Patton with Peter Economy, 2014), 2026-09-11 ---
    # The candidate list held: 34 distinct names over 23 records, and the
    # seven coinages the book needed ("Story Mapping", "User Story",
    # "Shared Understanding", "Product Backlog", "Story Slicing",
    # "Validated Learning", "Release Planning") came back with no rival
    # spelling. Four singletons are redirected.
    # Chapter 16's "story workshop" is Patton's name for the last best
    # conversation before building: a facilitated session, which is what
    # Workshop Facilitation already covers, and chapter 16 cites it too.
    "Story Workshop": "Workshop Facilitation",
    "Story Workshops": "Workshop Facilitation",
    # Chapter 13's "opportunity" is the largest unbroken story, sized up
    # before discovery starts. NOT "Opportunity Solution Tree", which in this
    # corpus is Torres's specific artefact.
    "Opportunity": "Product Discovery",
    "Opportunity Canvas": "Product Discovery",
    "Opportunity Backlog": "Product Discovery",
    # Cagan's foreword contrasts teams with a compelling vision against
    # roadmap executors: that argument lives on Product Strategy here.
    "Product Vision": "Product Strategy",
    "Design and Development Collaboration": "Team Collaboration",
    # NOT "User Stories": 2022-05-15_two-tips-better-ux-storytelling already
    # cites it, and there it means a story told about users to win support,
    # not a unit of delivery. That record is processed, so stamping the alias
    # would make fold_records refuse the write over a backlink it cannot
    # earn. It stays an orphan until a global pass can retarget it.
    # Vocabulary only below: keys cited by no record, registered so the next
    # agile or delivery book converges on the pages this one creates.
    "Story Map": "Story Mapping",
    "User Story Mapping": "Story Mapping",
    "Story Maps": "Story Mapping",
    "Backlog": "Product Backlog",
    "Flat Backlog": "Product Backlog",
    "Backlog Refinement": "Product Backlog",
    # NOT "Backlog Management": 2019-10-06_ux-agile-backlog already cites it,
    # in the same sense, but that record is processed, so stamping the alias
    # here would make fold_records refuse the write over a backlink it cannot
    # earn. Promoting it to MERGES and re-running apply_merge globally would
    # also drag "User Stories" into "User Story" via the singleton map, a
    # sense drift this book does not want. It stays an orphan until a global
    # pass can retarget both.
    "Story Splitting": "Story Slicing",
    "Story Sizing": "Story Slicing",
    "Rock Breaking": "Story Slicing",
    "Acceptance Criteria": "User Story",
    "Three Cs": "User Story",
    "Release Roadmap": "Release Planning",
    "Release Slicing": "Release Planning",
    "Walking Skeleton": "Release Planning",
    "Minimum Viable Solution": "Minimum Viable Product",
    # --- Storytelling in Design (Dahlström, 2019), 2026-09-11 ---
    # Two candidates fold into pages the corpus already has. The rest are
    # new names this book earns, registered here with their vocabulary so the
    # next storytelling or content book converges instead of re-coining.
    # "Transmedia Storytelling" is one story spread across media: a form of
    # storytelling, not an omnichannel service, so it folds into Storytelling
    # rather than Omnichannel Experience.
    "Transmedia Storytelling": "Storytelling",
    "Interactive Storytelling": "Storytelling",
    # Dahlström's "product life cycle" is the arc the USER travels (awareness,
    # consideration, purchase, onboarding, loyalty), which is what Customer
    # Journey already carries with 32 sources. Not the product-management
    # sense (introduction/growth/maturity/decline); no record in the corpus
    # uses that sense, and a future one should coin "Product Lifecycle
    # Management" rather than reuse this key.
    "Product Life Cycle": "Customer Journey",
    "Experience Life Cycle": "Customer Journey",
    # New pages, with their vocabulary as aliases.
    "Dramaturgy": "Narrative Structure",
    "Three-Act Structure": "Narrative Structure",
    "Story Structure": "Narrative Structure",
    "Plot Point": "Narrative Structure",
    "Sequence Approach": "Narrative Structure",
    "Story Shape": "Experience Shape",
    "Shape of Stories": "Experience Shape",
    "Emotional Arc": "Experience Shape",
    "Through Line": "Red Thread",
    "Story Theme": "Red Thread",
    "Character Definition": "Character Development",
    "Character Arc": "Character Development",
    "Main Plot": "Subplot",
    "Subplots": "Subplot",
    "Choose Your Own Adventure": "Nonlinear Storytelling",
    "CYOA": "Nonlinear Storytelling",
    "Branching Narrative": "Nonlinear Storytelling",
    "Nonlinear Narrative": "Nonlinear Storytelling",
    "Scene Design": "Scene Structure",
    "Information Radiator": "Shared Understanding",
}
