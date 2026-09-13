---
type: concept
name: AI in User Research
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "AI Research"
  - "AI in Research"
  - "AI in UX Research"
---

# AI in User Research

## Definition

AI in user research covers every use of AI tools across the research lifecycle:
planning studies, recruiting and screening participants, moderating or
simulating interviews, transcribing and coding data, analysing results, and
reporting them. The sources converge on a division of labour rather than a
verdict: AI is fast, broadly knowledgeable and strong at text-based and
administrative work, but it cannot observe behaviour, cannot exercise
situational judgement, and cannot feel or understand context
[[2024-09-20_ai-intern]], [[2024-09-27_research-with-ai]]. The recurring frame
is the intern: extremely knowledgeable, fast, eager to please, and in need of
heavy instruction, context and correction before anything it produces can be
trusted [[2024-09-20_ai-intern]].

Beyond the question of what AI can do lies the question of what is lost when it
does it. Research produces two outputs, findings and learning, and AI can only
deliver the first: the observing, wondering and interpreting a team does
together is an experience, not a deliverable [[2026-07-17_human-led-research-still-matters]].
The field also lacks rigorous evidence about where AI-driven methods are
accurate enough to substitute for human studies, which is why cost reduction
alone is not an argument for adoption [[2025-06-20_genai-ux-research-agenda]].

## Practice

### Where AI helps

- **Planning and documentation.** Generating research questions, building study
  templates, drafting consent forms and recruitment materials — the tedious
  administrative layer around a study [[2024-09-27_research-with-ai]]. Drafting
  discussion guides belongs here too [[2026-07-17_human-led-research-still-matters]].
- **Text-based analysis.** Transcription, summarisation, preliminary coding and
  initial clustering of qualitative data can all be accelerated, provided a
  human expert reviews and refines the output [[2024-09-27_research-with-ai]].
- **Support work around sessions.** Recruiting participants, transcribing and
  cleaning data are the tasks to hand off, precisely because they are not where
  learning happens [[2026-07-17_human-led-research-still-matters]].
- **Desk research in unfamiliar domains.** AI-generated profiles can synthesise
  academic literature, forums and product information into a digestible
  overview when entering a completely new domain [[2024-06-21_synthetic-users]].
- **Secondary research, ideation, writing, facilitation, data extraction and
  visualisation** are identified as lower-risk candidates for AI-assisted
  workflows [[2025-06-20_genai-ux-research-agenda]].
- **Structured, scalable interviewing.** AI moderators work for product
  feedback, recruitment screening and multilingual interviews — tasks where a
  script should be followed identically every time [[2026-01-30_ai-interviewers]].

### Where AI fails

- **It cannot observe.** AI cannot watch a usability test or register nonverbal
  interaction; it can only analyse what users say, never what they do
  [[2024-09-27_research-with-ai]], [[2024-09-20_ai-intern]].
- **It cannot read the room.** AI interviewers follow scripts rigidly, never
  adapting, skipping or reframing, and struggle to recognise when a question is
  sufficiently explored — the judgement human moderators exercise constantly
  [[2026-01-30_ai-interviewers]].
- **It is sycophantic.** AI chatbots tend toward agreement, making synthetic
  participants likely to approve of any concept [[2024-06-21_synthetic-users]];
  AI interviewers praised mundane answers as "fascinating" and "brilliant",
  which experienced participants found fake and disingenuous
  [[2026-01-30_ai-interviewers]].
- **It hallucinates.** AI can invent sources, regurgitate bad advice and produce
  false information, so nothing leaves the researcher's hands unverified
  [[2024-09-20_ai-intern]].
- **It oversimplifies and idealises.** Synthetic users miss the contextual
  reasons behind choices, produce one-dimensional responses, and report
  optimistically where real users honestly reported abandonment
  [[2024-06-21_synthetic-users]].
- **It changes participant behaviour.** In AI-moderated interviews participants
  held back sensitive information, doubting the system's accountability, and
  reported losing the sense of control they have with a human moderator
  [[2026-01-30_ai-interviewers]].

### How to work with AI

- **Treat it as an intern, not a mentor.** Provide detailed, step-by-step
  instructions and relevant organisational context rather than open-ended
  projects; supervise, correct, and expect to review everything
  [[2024-09-20_ai-intern]], [[2024-09-27_research-with-ai]].
- **Use it for drafts, not final products.** AI output is a starting point, not
  a substitute for human expertise and judgement [[2024-09-20_ai-intern]].
- **Never let it do the whole analysis.** AI is stochastic: it may attend to
  some parts of the data and disregard others, focusing on the wrong aspects
  [[2024-09-27_research-with-ai]].
- **Treat synthetic output as hypotheses.** If synthetic users are used at all,
  their output should shape the questions asked of real users, never inform
  final decisions [[2024-06-21_synthetic-users]].
- **Keep sense-making human.** Protect moderating, observing sessions live,
  debriefing together and interpretive work — passing analysis to AI creates an
  illusion of learning without retention, because information people generate
  themselves is retained better (the self-generation effect)
  [[2026-07-17_human-led-research-still-matters]].

### Testing AI products, and testing AI tools

Two distinct questions run through the sources. On the object side, the Wizard
of Oz method — where a hidden human supplies the responses of an apparently
autonomous interface — is singled out as particularly valuable for AI systems
and natural-language interfaces, lowering the investment risk of costly
generative-AI technologies by testing desirability, utility and usability before
they are built [[2024-04-19_wizard-of-oz]]. On the tooling side, AI features
embedded in research platforms generate leading tasks, too many interview
questions and flawed test plans that novice researchers cannot catch, so those
features need expert methodological input rather than trust
[[2026-03-13_research-tool-problems]].

### Open questions and disagreement

The sources are not evenly positioned. The research-agenda piece treats
synthetic users, digital twins and automated interface evaluation as promising
directions whose accuracy and bias remain open questions to be settled by
benchmarking against expert evaluation [[2025-06-20_genai-ux-research-agenda]],
while the synthetic-users test concludes from its own comparison against real
research that they cannot replace real user research at all
[[2024-06-21_synthetic-users]]. What both agree on is the trap: cheaper is not
better without validation, because poor results lead to incorrect design
decisions and high long-term costs [[2025-06-20_genai-ux-research-agenda]]. The
strongest form of the argument goes further — even if AI outputs became
indistinguishable from an expert's, outsourcing the work would still remove the
team's learning [[2026-07-17_human-led-research-still-matters]].

## Sources (8)

- [[2024-04-19_wizard-of-oz]] — highlights the method's particular value for testing AI systems and natural-language interfaces.
- [[2024-06-21_synthetic-users]] — artificial intelligence applied to research has limitations related to sycophancy, oversimplification, and inability to model actual behavior; requires careful interpretation.
- [[2024-09-20_ai-intern]] — the appropriate applications and limitations of AI tools for conducting, analyzing, and reporting user research.
- [[2024-09-27_research-with-ai]] — the capabilities and limitations of AI tools across research planning, conducting, analysis, and reporting phases.
- [[2025-06-20_genai-ux-research-agenda]] — applications of generative AI to support, augment, or replace traditional UX research workflows and data analysis.
- [[2026-01-30_ai-interviewers]] — AI interviews supplement but do not replace human moderation; they excel at structured tasks but lack judgment for discovery and complex contexts.
- [[2026-03-13_research-tool-problems]] — Warns that AI-powered research features need expert input to avoid automating flawed research practices at scale.
- [[2026-07-17_human-led-research-still-matters]] — should handle support work (recruiting, transcribing, data cleaning) to free teams for the work where learning lives: moderating, observing, debriefing, and interpreting.
