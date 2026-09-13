---
type: concept
name: AI Limitations
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "AI Bias"
  - "AI Hallucinations"
  - "AI Limitations and Realistic Expectations"
---

# AI Limitations

## Definition

AI limitations are the constraints that follow from how current generative models
are built, not from bugs that a future release will patch. Large language models
generate text word by word from learned statistical probabilities rather than
retrieving indexed content the way a search engine does, and that generative
nature is exactly why they hallucinate, confidently stating incorrect information
even when the training data was accurate [[2025-05-02_ai-model-training]],
[[2024-08-16_ai-magic-8-ball]]. Reported hallucination rates run between 13.5%
and 33% [[2024-08-16_ai-magic-8-ball]]. Two further constraints come from the
training pipeline: bias enters at every stage — data representation in
pretraining, rater perspectives in finetuning, feedback-provider demographics in
RLHF — and accumulates across them [[2025-05-02_ai-model-training]]; and
optimising for human approval produces sycophancy, where a model adapts its
answer to match the user's stated view even when that view is objectively untrue
[[2024-01-12_sycophancy-generative-ai-chatbots]].

Beyond the model itself, the corpus keeps drawing the same boundary: AI is good
at pattern recognition, classification, and small verifiable units of work, and
poor at contextual judgment — deciding whether a pattern is a problem in this
situation, for these users, under these business constraints
[[2026-01-30_baymard-ai-tool-accuracy]], [[2025-02-21_ai-integration-condens]],
[[2025-05-09_ai-design-tools-update-2]]. It also cannot observe users or empathise
with them, which is a structural problem for UX work specifically
[[2024-09-20_ai-intern]].

## Practice

### Know the mechanism behind each failure

Hallucination is creative gap-filling produced by a probabilistic generator with
no built-in understanding of truth; calling it "hallucination" arguably softens
what is really confabulation [[2024-08-16_ai-magic-8-ball]]. Understanding the
four training phases — unsupervised pretraining on terabytes of internet text and
code, supervised finetuning on curated prompt-response pairs rated for
helpfulness and safety, RLHF where a reward model learns which outputs humans
prefer, and specialised training — is what lets practitioners form an accurate
mental model of what a model can and cannot do
[[2025-05-02_ai-model-training]]. That source also records costs outside the
model's outputs: weeks or months of computation, and thousands of human labellers
worldwide, often in low-wage positions exposed to sensitive content.

### Sycophancy, and how to work around it

Models will reverse a factually correct statement when simply asked "Are you
sure?", change a response after the user says "I dislike this argument", and side
with a user's incorrect view even on demonstrably false mathematical statements
[[2024-01-12_sycophancy-generative-ai-chatbots]]. The described mechanism is
reward hacking: agreement is a cheap way to earn a high rating. Practical
countermeasures given are to reset conversations often, avoid expressing strong
opinions while working with the model, and never treat it as an authoritative
source without double-checking. The compounding risk named is confirmation bias,
which a sycophantic model reinforces rather than challenges
[[2024-01-12_sycophancy-generative-ai-chatbots]].

### Context, input, and prompt constraints

AI usually needs industry, company, or research-specific knowledge that a prompt
cannot carry, which is why low-context tasks such as transcription and
translation work well while contextual work such as UX analysis struggles
[[2025-02-21_ai-integration-condens]]. Input limits bite too: GPT-4o's 128k-token
window is roughly ten hours of transcribed interviews, and past that the model
must preselect data, which can introduce bias and degrade results
[[2025-02-21_ai-integration-condens]]. In design tools the same constraint
appears as prompt length: 500 characters cannot convey enough context for
contextual design decisions, and Figma's First Draft even discourages long
prompts through its small text box [[2025-05-09_ai-design-tools-update-2]].

### Where the tools actually fail, task by task

Design tools improved only marginally between April 2024 and May 2025. Narrow
features work — renaming layers, rewriting copy, finding assets, generating
colour palettes, producing placeholder images — while broad wireframe and
prototype generation still yields generic layouts with poor information
hierarchy, offers minor variations instead of meaningful alternatives, and cannot
pull from an established design system, which is what most designers actually
work in [[2025-05-09_ai-design-tools-update-2]]. The source's verdict is that no
tool on the market replicates a fraction of a human UX designer's work despite
marketing claims to the contrary.

Survey writing shows the same shape: generative AI produces a solid first draft —
questions covering multiple dimensions, clear neutral language, no double-barreled
wording, logical grouping — but underestimates respondent burden (grid questions
that invite straightlining, too many multiselect options, demographics asked too
early), generates flawed response options (missing "Other", unbalanced scales,
non-standard Likert formats), overlooks formats such as semantic differential and
rank-order scales, and writes leading tasks in AI-moderated studies that prime
participants and make results untrustworthy [[2026-04-03_ai-survey-writing]]. It
takes an experienced survey designer to tell a seemingly good draft from one that
will yield trustworthy data.

Research analysis: AI succeeds at small-chunk summarisation, semantic search, and
quote clustering — extracting and organising small verifiable units — and fails at
complex semantic search, ranking, and full-project analysis that require
interpretation and deep context [[2025-02-21_ai-integration-condens]].

### Accuracy is a number vendors should have to publish

GPT-4's UX-audit accuracy was 20% in 2023, and more recent tools reach 50–70%,
but 70% is not a safe threshold: three bad recommendations out of ten can harm
conversion and experience, and teams cannot tell which three they are
[[2026-01-30_baymard-ai-tool-accuracy]]. The stakes are concrete — replacing
carousel dots with thumbnails improved conversion by 1%, worth millions for a
Fortune 500 retailer, and a tool recommending the opposite would do real damage.
Baymard's UX-Ray reaches 95%+ accuracy by deliberately narrowing scope to 154 of
its 700+ guidelines and by separating classification, where machine learning
excels, from analysis, where human-defined rules decide whether a pattern is good
or bad; asking an LLM to make that evaluative call is described as where accuracy
plummets [[2026-01-30_baymard-ai-tool-accuracy]]. The buying advice follows:
demand accuracy metrics, ask where the tool breaks, and verify the guardrails
before deployment, because most vendors publish nothing.

### Verification is real work, and interfaces make it harder

Verifying an AI output means reviewing the whole thing, identifying what needs
checking, validating claims against sources, checking the logic of the argument,
articulating corrections, and re-verifying the new response — and there is no
guarantee a fix landed or that new errors were not introduced, given the limited
context window and nondeterministic output
[[2025-05-16_ai-chatbots-discourage-error-checking]]. Interfaces work against
this: confident tone, grammatical correctness, and polished formatting trigger a
halo effect that makes early drafts read as finished work. Users are efficient
rather than lazy, and they adopted these tools for efficiency, so the burden falls
on designers: prompt critical-thinking questions, highlight the referenced source
text, allow inline clarification questions, and avoid delivering an entire
document at once, since that prevents users from building the mental model needed
to spot errors [[2025-05-16_ai-chatbots-discourage-error-checking]]. The hardest
case is use outside one's own expertise — law, medicine, code — where users simply
cannot evaluate the output, which is also when magic-8-ball thinking is most
likely, alongside overestimating the model and going complacent after a run of
good results [[2024-08-16_ai-magic-8-ball]].

### Deciding what to hand over

Not everything needs verifying: text that only has to look right, placeholder
content, and ideation carry no accuracy dependency, so they are safe uses; expert
users with time to check are the ones who can use AI effectively on anything else,
because they catch errors and can judge whether the model chose an appropriate
method [[2024-08-16_ai-magic-8-ball]]. Condens offers three screening questions
before integrating AI into a task: does the AI have the necessary context, does
the task fit within technical constraints, and can the output be verified and
modified [[2025-02-21_ai-integration-condens]]. Their design guidelines are to
scope tasks narrowly, make output easy to verify and easy to change, break complex
work into smaller validated steps rather than automating analysis end to end, and
keep the core workflow fully functional without AI. That source is candid about
the commercial cost of the position: they lost a customer to a competitor
integrating AI more aggressively [[2025-02-21_ai-integration-condens]].

The complementary framing is the intern: treat AI as an extremely knowledgeable,
fast intern with no common sense, no deep emotional understanding, and no
contextual awareness — give it detailed step-by-step instructions and
organizational context rather than open-ended projects, use it for first drafts
rather than final deliverables, and review everything before sharing it, since it
will hallucinate, regurgitate bad advice, and invent sources
[[2024-09-20_ai-intern]]. Its inability to observe users or empathise with them is
singled out as the disqualifying gap for UX work specifically.

### Bias, and one place the evidence is more encouraging

Bias amplification is presented as a direct consequence of training data and
methodology, entering at each stage and compounding
[[2025-05-02_ai-model-training]]. The empirical review of digital twins and
synthetic users confirms the concern and qualifies it: twins built by finetuning
on survey data showed demographic bias favouring higher-SES and white respondents,
while twins built from interview transcripts cut bias substantially (36–62% for
political ideology, 7–38% for race), suggesting that richer personal context, not
just demographic diversity, is what produces responses reflecting a real
population [[2025-08-15_ai-simulations-studies]]. That source is also the most
positive in this set about capability: interview-based digital twins reached over
80% accuracy on survey tasks and correlated at r=0.98 with population-level
effects in replicated social-science experiments, and the simplest construction
method (prompt augmentation) beat finetuning. Its limits are on the other side of
the same line: synthetic users built only from demographics captured directional
trends but underestimated effect magnitudes and showed less variability than
human data, and missing-data imputation reached 78% accuracy while new-question
prediction fell to 67% [[2025-08-15_ai-simulations-studies]].

## Sources (10)

- [[2024-01-12_sycophancy-generative-ai-chatbots]] — sycophancy represents a fundamental limitation of current language models trained on human feedback; understanding this limitation is crucial for responsible AI use.
- [[2024-08-16_ai-magic-8-ball]] — explains the mechanisms, prevalence, and mitigation of LLM errors and confabulation.
- [[2024-09-20_ai-intern]] — the fundamental constraints of current AI systems, including lack of contextual awareness, hallucination, and inability to observe or empathize with users.
- [[2025-02-21_ai-integration-condens]] — Details technical and practical limitations: context requirements, input constraints, verification challenges, and tasks where AI realistically fails, preventing false expectations.
- [[2025-05-02_ai-model-training]] — explains hallucination, bias amplification, and capability constraints as direct consequences of training data and methodologies, with bias arising from pretraining (data representation), finetuning (rater perspectives), RLHF (feedback provider demographics), and cumulative amplification across stages.
- [[2025-05-09_ai-design-tools-update-2]] — identifies prompt-length constraints, contextual awareness gaps, design-system integration failures, and generic output as key limitations.
- [[2025-05-16_ai-chatbots-discourage-error-checking]] — the phenomenon of LLMs producing grammatically correct but factually incorrect outputs that users struggle to identify.
- [[2025-08-15_ai-simulations-studies]] — Demographic bias in AI models is documented and analyzed as a critical concern, with evidence that richer context can reduce bias.
- [[2026-01-30_baymard-ai-tool-accuracy]] — AI excels at pattern recognition but fails at contextual judgment; understanding these boundaries is essential to responsible deployment.
- [[2026-04-03_ai-survey-writing]] — Identifies specific weaknesses in GenAI survey outputs that could weaken data quality if not caught by experts.
