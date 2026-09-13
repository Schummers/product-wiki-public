---
type: concept
name: Large Language Model
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "LLM"
  - "LLM (Large Language Model)"
  - "LLM (Large Language Models)"
  - "LLMs"
  - "Large Language Model (LLM)"
  - "Large Language Models"
---

# Large Language Model

## Definition

A large language model is a probabilistic system that predicts word sequences:
generative AI makes word-by-word predictions in the context of a prompt, rather
than retrieving knowledge [[2024-09-13_how-ai-works]]. LLMs generate text by
predicting the most likely next word from patterns learned in training data, not
by accessing true knowledge [[2024-07-12_artificial-intelligence-glossary]]. The
mechanism rests on word embeddings (words represented as points in a
multidimensional space, so similar words sit near each other), neural networks
that adjust internal weights and biases during training, and the transformer
architecture introduced in 2017, whose parallel processing and self-attention
give speed and context awareness — each word "knows about" every other word in
the passage [[2024-09-13_how-ai-works]].

The French corpus treats the LLM primarily as an underlying technology rather
than a product: a base technology that does not necessarily require an open
conversational interface [[2024-08-13_341_Dust_🇫🇷,_mieux_que_ChatGPT_Analyse_design_de_l_outil_IA_des_product_people...]], a technology and not a usage, comparable to
a database, meant to solve a specific problem [[2025-09-30_397_Pourquoi_l_IA_n_a_pas_(encore)_révolutionné_l_UX]], and a capability
available to every company whose real strength appears only when a designer
finds new uses by connecting it to other tools [[2025-09-16_395_L_UX_Design_est_mort_L_impact_de_l_IA_&_du_business_sur_le_métier_de_designer]]. Connected to external
tools, memory or APIs, an LLM becomes an AI agent with autonomy to execute
concrete tasks, as opposed to a plain LLM that only generates text [[2025-07-08_385_Designer_un_agent_IA,_ça_veut_dire_quoi_!]].

## Practice

### Understand how the model is built

- Four training types shape what a model can do: pretraining (unsupervised
  learning over terabytes of internet text, code and books to learn which words
  follow which), finetuning (supervised learning on curated prompt-response
  pairs rated for helpfulness, clarity and safety), RLHF (humans rank outputs, a
  reward model learns to predict those preferences and guides the main model),
  and specialized training [[2025-05-02_ai-model-training]].
- Pretraining is explicitly not learning tasks or human meaning; it is
  statistical relationships between words [[2025-05-02_ai-model-training]].
- Bias enters at every stage: data representation in pretraining, rater
  perspectives in finetuning, feedback-provider demographics in RLHF, and it
  accumulates across stages [[2025-05-02_ai-model-training]].
- Hallucination is a direct consequence of the generative mechanism: because
  LLMs construct answers word by word instead of retrieving indexed content like
  a search engine, they can confidently state incorrect information
  [[2025-05-02_ai-model-training]], [[2024-07-12_artificial-intelligence-glossary]].
- The models remain partly unexplainable: the mathematics is understood, but
  what each dimension of a word embedding represents is not, which is why AI is
  called a black box [[2024-09-13_how-ai-works]].
- Training also carries environmental and labour costs — weeks or months of
  computation, and thousands of human labellers often in low-wage positions
  exposed to sensitive content [[2025-05-02_ai-model-training]].
- Prompting technique changes the quality of the response: chain-of-thought,
  zero-shot and few-shot prompting are named as strategies that matter
  [[2024-07-12_artificial-intelligence-glossary]].

### Natural language as an interface: what it buys and what it costs

- Natural language is intuitive and flexible: it relies on words the user
  already knows, and lets people express very specific needs or chain complex
  actions without mastering submenus or technical jargon [[2024-05-21_329_Interface_IA_langage_naturel,_la_solution_idéale]].
- Its reliability is limited because human language carries subjective, context-
  dependent nuances ("soon", "not too expensive"), which produce
  misinterpretation and variable answers [[2024-05-21_329_Interface_IA_langage_naturel,_la_solution_idéale]].
- Input time is much longer than a click, and the same sentence does not
  guarantee the same output twice, which makes it a poor fit for repetitive
  tasks [[2024-05-21_329_Interface_IA_langage_naturel,_la_solution_idéale]]. The lesson given is explicit: impressive does not mean
  optimal as an interface [[2024-05-21_329_Interface_IA_langage_naturel,_la_solution_idéale]].
- Systematically replacing interfaces with chatbots is criticised as unsuited to
  most situations, particularly producing or structuring information — using a
  chat to draft an email can be more tedious than writing it [[2025-09-30_397_Pourquoi_l_IA_n_a_pas_(encore)_révolutionné_l_UX]]. Open
  discussion is described as a trap, comparable to launching a team debate with
  nothing to frame it [[2024-08-13_341_Dust_🇫🇷,_mieux_que_ChatGPT_Analyse_design_de_l_outil_IA_des_product_people...]].
- The counter-examples given are integrations that target a specific friction
  without imposing a full chat interface: Jira proactively explaining acronyms,
  Granola mixing written and audio notes, Airtable generating formulas from a
  prompt [[2025-09-30_397_Pourquoi_l_IA_n_a_pas_(encore)_révolutionné_l_UX]].
- Design method that follows: start from "I have a problem, how do I solve it?"
  rather than "what can I do with AI?" [[2025-09-30_397_Pourquoi_l_IA_n_a_pas_(encore)_révolutionné_l_UX]].

### Specialising a model rather than using it raw

- Connecting a model to internal knowledge bases (Notion, Slack) to create
  specialised assistants produces far more relevant, contextual answers than a
  generic model [[2024-08-13_341_Dust_🇫🇷,_mieux_que_ChatGPT_Analyse_design_de_l_outil_IA_des_product_people...]].
- Accepting initial friction — taking time to pre-configure an assistant —
  removes the need to rewrite long prompts every time and lowers daily workload;
  an expert can configure a strong agent once and share it with the whole team,
  which levels out differences in AI skill [[2024-08-13_341_Dust_🇫🇷,_mieux_que_ChatGPT_Analyse_design_de_l_outil_IA_des_product_people...]].
- Invoking several specialised agents inside one conversation is presented as a
  way to speed up complex problem solving [[2024-08-13_341_Dust_🇫🇷,_mieux_que_ChatGPT_Analyse_design_de_l_outil_IA_des_product_people...]].
- An agent's power comes from function calling: triggering calls to third-party
  services, APIs and databases to perform real actions [[2025-07-08_385_Designer_un_agent_IA,_ça_veut_dire_quoi_!]].

### Prompting and delegating work

- Frame the model with explicit rules first: define what a good deliverable is
  (for instance the exact structure of a variable name, or the elements of a
  good definition) so the generated results are consistent [[2025-01-28_362_Générer_de_la_doc_avec_ChatGPT_-_Product_Support_Tech_documentation]].
- Use few-shot prompting: give full context plus a few hand-written examples
  showing exactly the format and quality expected, which sharply improves
  generation of the rest [[2025-01-28_362_Générer_de_la_doc_avec_ChatGPT_-_Product_Support_Tech_documentation]].
- Human review remains mandatory on every generated result, to fix missing
  context, adjust product-specific vocabulary, and sometimes discover that a bad
  description actually reveals a badly chosen variable name [[2025-01-28_362_Générer_de_la_doc_avec_ChatGPT_-_Product_Support_Tech_documentation]].
- Use the model for long, tedious, low-value tasks where human expertise adds
  little, and treat it as a tool rather than a machine that produces absolute
  answers [[2025-01-28_362_Générer_de_la_doc_avec_ChatGPT_-_Product_Support_Tech_documentation]].
- For interface generation, write prompts like specifications: detail the user
  journey step by step, as you would brief a developer — bad specs given to a
  very good developer still produce a bad result [[2025-08-26_392_Artifact_le_meilleur_outil_de_micro-prototypage_IA_pour_designers_&_PMs]]. Referencing the
  design of well-known companies (Apple, Notion, Uber) avoids a crude visual
  rendering, and the advice is to prompt in English and avoid long iteration
  chains inside a single conversation [[2025-08-26_392_Artifact_le_meilleur_outil_de_micro-prototypage_IA_pour_designers_&_PMs]].
- For UX writing specifically, two methods: ask the model to explain a given
  wording in context to test its clarity, and ask for 10 to 30 alternatives to
  remix manually. The model is useful as a detached, probabilistic outside
  tester of whether internal jargon has deformed a term, but it cannot guess
  which of two wordings will perform better — that depends on company and user
  context and requires real testing [[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]].

### Consequences for designers

- Designing for agents means designing a system of building blocks and commands
  rather than static interfaces; the agent then assembles its response
  dynamically from that toolkit [[2025-07-08_385_Designer_un_agent_IA,_ça_veut_dire_quoi_!]]. Research shifts toward defining the
  agent's personality and managing its autonomy — when and how to give the user
  feedback about the agent's actions [[2025-07-08_385_Designer_un_agent_IA,_ça_veut_dire_quoi_!]].
- Designers are urged to experiment directly: no-code automation platforms like
  N8N or Make to demystify function calling [[2025-07-08_385_Designer_un_agent_IA,_ça_veut_dire_quoi_!]], model playgrounds to see
  what the technology can actually do [[2025-09-30_397_Pourquoi_l_IA_n_a_pas_(encore)_révolutionné_l_UX]], and hands-on work with AI APIs
  and LLMs rather than staying abstract and distant from the technical layer
  [[2025-09-16_395_L_UX_Design_est_mort_L_impact_de_l_IA_&_du_business_sur_le_métier_de_designer]].
- The stated risk of not doing so: without knowing what an LLM can do, you
  cannot design a feature that uses it to answer a real problem, and you will
  reproduce existing patterns instead of innovating [[2025-09-30_397_Pourquoi_l_IA_n_a_pas_(encore)_révolutionné_l_UX]].
- Because AI now easily produces average output, the bar rises and expert human
  judgement becomes more important, not less [[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]].

## Sources (11)

- [[2024-05-21_329_Interface_IA_langage_naturel,_la_solution_idéale]]
- [[2024-07-12_artificial-intelligence-glossary]] — explains the architecture and behavior of LLMs including how they generate text and why they produce hallucinations.
- [[2024-08-13_341_Dust_🇫🇷,_mieux_que_ChatGPT_Analyse_design_de_l_outil_IA_des_product_people...]]
- [[2024-09-13_how-ai-works]] — probabilistic systems trained on vast text corpora that predict word sequences and generate coherent responses based on statistical patterns in language.
- [[2025-01-14_360_UX_Writing_&_ChatGPT_2_méthodes_simples_et_efficaces]]
- [[2025-01-28_362_Générer_de_la_doc_avec_ChatGPT_-_Product_Support_Tech_documentation]]
- [[2025-05-02_ai-model-training]] — details training stages for LLMs, bias sources at each stage, and capability limitations resulting from training approach.
- [[2025-07-08_385_Designer_un_agent_IA,_ça_veut_dire_quoi_!]]
- [[2025-08-26_392_Artifact_le_meilleur_outil_de_micro-prototypage_IA_pour_designers_&_PMs]]
- [[2025-09-16_395_L_UX_Design_est_mort_L_impact_de_l_IA_&_du_business_sur_le_métier_de_designer]]
- [[2025-09-30_397_Pourquoi_l_IA_n_a_pas_(encore)_révolutionné_l_UX]]
