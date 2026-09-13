---
type: concept
name: Onboarding
created: 2026-07-31
updated: 2026-07-31
status: developed
aliases:
  - "AI Onboarding and Guidance"
  - "Onboarding Patterns"
  - "Onboarding and Learning"
  - "Onboarding to AI"
  - "User Education"
  - "User Guidance"
  - "User Onboarding"
---

# Onboarding

## Definition

Onboarding is the process of getting users familiar with a new interface, using
dedicated flows and UI elements that are not part of the regular interface
([[2020-06-21_mobile-app-onboarding]]). It covers more than teaching
interaction: it also sets up the account, collects the data the product needs to
function, and introduces what the product can do. In complex systems it is
better read as a journey rather than a screen sequence — the work of moving a
user from initial unfamiliarity to proficiency and confidence, a path along
which people can stall as "legacy" users with rigid workarounds or progress to
genuine expertise ([[2025-06-27_complex-apps-users]]). In the French corpus the
same word is used for the welcome sequence whose job is less to explain how the
app works than to make its value felt quickly
([[2025-05-06_376_Designer_un_funnel_de_conversion_paywall_-_Gold_standard_2025]],
[[2026-06-09_417_Les_3_clés_de_l_adoption_produit_-_Hacks_Growth_Design]]).

The sources converge on a sceptical position: dedicated onboarding is a cost,
not a free addition, and the strongest recommendation across the corpus is to
avoid it where possible and spend the effort on making the interface itself
learnable ([[2020-06-21_mobile-app-onboarding]],
[[2020-03-08_mobile-tutorials]]). Where onboarding is genuinely needed —
unfamiliar technology, complex domains, first setup of a physical device — the
guidance shifts from upfront explanation to help delivered in context, one step
at a time, at the moment the user can act on it.

## Practice

### Prefer a learnable interface over a dedicated flow

- Avoid creating app onboarding whenever possible and spend the resources making
  the UI more usable, building on existing mental models
  ([[2020-06-21_mobile-app-onboarding]]).
- Tutorials take significant time and effort to design and develop; that effort
  is better spent making the UI easy to use and thus removing the need for a
  tutorial in the first place ([[2020-03-08_mobile-tutorials]]).
- Training and documentation supplement learning but cannot compensate for poor
  usability or unintuitive workflows ([[2025-06-27_complex-apps-users]]). Treating
  learner struggles as a training issue shifts responsibility from the design to
  the user and prevents genuine proficiency from developing.
- The fundamental principles of interaction design hold regardless of how novel
  the technology is ([[2024-03-29_new-ai-users-onboarding]]).

### Test whether onboarding is needed at all

- Add onboarding only if testing shows users struggle without it: test a
  no-onboarding version first, then validate that the onboarding actually solves
  the problem before committing to the design ([[2020-06-21_mobile-app-onboarding]]).
- A quantitative study of 70 users across 4 mobile apps found deck-of-cards
  tutorials gave no measurable benefit: 91% task success for users who read the
  tutorial versus 94% for those who skipped it, near-identical completion times
  (93.49 vs 85.17 seconds), and tutorial readers rated the tasks as *more*
  difficult than skippers ([[2020-03-08_mobile-tutorials]]). Many users skip
  tutorials anyway, and those who read them gain nothing tangible.
- Exploratory research confirms a feature's value and its optimal placement;
  evaluative usability testing surfaces discoverability problems before launch
  rather than after ([[2025-03-21_discoverability-ai-amazon]]).

### Push versus pull: contextual help beats upfront tutorials

The corpus draws a consistent line between two delivery modes.

- **Push revelations** reveal information out of context, with no signal that the
  user would benefit from it at that moment; **pull revelations** are triggered by
  a signal that the user needs the information now
  ([[2023-02-12_onboarding-tutorials]], [[2020-12-13_help-and-documentation]]).
- Unprompted tutorials at launch interrupt users who want to start using the
  product, so they skip them or forget what they read
  ([[2023-02-12_onboarding-tutorials]]). Presenting steps out of context forces
  memorisation and exceeds working-memory capacity.
- Favour pull over push: make help accessible without forcing users into it,
  reserve push for essential information, and always allow easy dismissal
  ([[2020-12-13_help-and-documentation]]).
- For multistep workflows, show help alongside each step so nothing has to be
  held in working memory ([[2023-02-12_onboarding-tutorials]]).
- Progressive disclosure keeps help visible but not overwhelming by default, with
  the option to expand, which respects novices and experienced users at once
  ([[2023-02-12_onboarding-tutorials]]).
- Overlays and other windows layered on top of the task — onboarding, alerts,
  newsletters — train users to dismiss them reflexively without reading
  ([[2024-06-18_333_Design_contre-intuitif_Make_it_pop,_une_mauvaise_solution]]).
  The counter-intuitive fix is to make onboarding content look like ordinary
  content rather than making it louder; Notion's onboarding works because it
  presents itself as plain tasks to complete.
- The sources are not fully aligned on how far to push this. The heuristics
  article still treats tutorials and instructional overlays as legitimate
  proactive help for new users and for users meeting a redesigned interface,
  provided they are short and contextually relevant
  ([[2020-12-13_help-and-documentation]]), whereas the dedicated tutorial
  analyses recommend avoiding deck-of-cards tutorials outright
  ([[2020-03-08_mobile-tutorials]], [[2020-06-21_mobile-app-onboarding]],
  [[2023-02-12_onboarding-tutorials]]).

### What belongs in an onboarding flow, and what does not

Three common components, each with its own verdict
([[2020-06-21_mobile-app-onboarding]]):

- **Feature promotion** — belongs on the app-store page where users explore and
  compare, not at first launch; people rarely need to be sold on the features
  they downloaded the app for. Use contextual help inside the app when a feature
  becomes actionable.
- **Customisation** — gather the essential setup data the app needs to function
  (language, fitness level). Avoid asking users to pick colour schemes before
  they understand the interface; save visual customisation for settings.
- **Instructions** — keep them minimal and optional, limited to what is genuinely
  new or unfamiliar. Prefer overlays for contextual, timely guidance and
  interactive walkthroughs that teach novel workflows through practice.

### Do not force commitment before the user has context

- "Get Started" is an ambiguous call to action: users read it as a way to learn
  more, then find themselves in a signup flow, quiz, or sales funnel without the
  foundational information they needed ([[2017-08-20_get-started]]). Signup and
  orientation flows belong to users who have decided to commit.
- People arriving from marketing campaigns often lack the context to commit to a
  complex flow; the reciprocity principle means they give personal information
  and time more willingly after receiving value, not before
  ([[2017-08-20_get-started]]).
- Specific labels ("Take our style quiz", "Switch your cell plan") set accurate
  expectations where a generic label creates false information scent
  ([[2017-08-20_get-started]]).
- Requiring account creation before the paywall causes a sharp drop in
  conversion; delay the signup step as far as possible so it does not block the
  purchase path
  ([[2025-05-06_376_Designer_un_funnel_de_conversion_paywall_-_Gold_standard_2025]]).

### Onboarding as a value demonstration and conversion path

The Parlons Design corpus treats onboarding primarily as an adoption lever.

- Onboarding should not list features; it should make the product's promise felt
  immediately and end with a small success or gift that engages the user before
  the sale
  ([[2025-05-06_376_Designer_un_funnel_de_conversion_paywall_-_Gold_standard_2025]]).
- Most monetisation happens in the first hour of use, and often in the first
  moments; deferring paid offers by several days loses a large share of the
  potential audience. That episode is explicit that this "gold standard" funnel
  optimises selling efficiency, potentially at the expense of user-experience
  quality, and that no monetisation strategy compensates for a weak product
  ([[2025-05-06_376_Designer_un_funnel_de_conversion_paywall_-_Gold_standard_2025]]).
  This sits in tension with the reciprocity argument that users should receive
  value before being asked to commit ([[2017-08-20_get-started]]).
- Progressive onboarding: do not expose the whole complexity of a solution up
  front. Demonstrate value immediately, simplify the adoption form, and split the
  path into small rewarding steps
  ([[2026-06-09_417_Les_3_clés_de_l_adoption_produit_-_Hacks_Growth_Design]]).
- Entry points into a new feature should read as contextual help, not intrusive
  advertising; relevance and timing beat raw visibility, and both click-through
  and bounce rate should be measured
  ([[2026-06-09_417_Les_3_clés_de_l_adoption_produit_-_Hacks_Growth_Design]]).
  Making a button visually louder than its neighbours tends to get it ignored
  rather than noticed
  ([[2024-06-18_333_Design_contre-intuitif_Make_it_pop,_une_mauvaise_solution]]).

### Use empty and default states as the teaching surface

- Empty states are common in complex applications during onboarding and initial
  use, and are natural moments for contextual help that appears only when the
  user interacts with the relevant element — pull revelations, more memorable
  than forced tutorials ([[2021-09-19_empty-state-interface-design]]).
- Go beyond describing what users *could* do: include buttons, links, or explicit
  instructions that show exactly *how*
  ([[2021-09-19_empty-state-interface-design]]). Communicate whether content is
  loading, processing, or genuinely absent, and never show a misleading "No
  records" message that disappears once loading finishes.
- The recommended empty-state structure: a relevant illustration or icon, a title
  explaining why the screen is empty, a short description of the value on offer,
  and one or two clear CTAs. Forgetting the CTA is the most frequent mistake, and
  generic titles ("there is nothing here") or database-flavoured technical
  descriptions should be avoided
  ([[2025-07-29_388_Empty_State_-_Guide_UX_design_pour_améliorer_l_onboarding]]).
- Advanced variants: creation templates, recommended content, or pre-filled
  default content to prime usage
  ([[2025-07-29_388_Empty_State_-_Guide_UX_design_pour_améliorer_l_onboarding]]);
  informative empty states, pre-filled states, templates, and dummy data help
  users project themselves into a new feature instead of facing a blank page
  ([[2026-06-09_417_Les_3_clés_de_l_adoption_produit_-_Hacks_Growth_Design]]).
- Empty-state design should be an established, consistent pattern across the
  organisation's applications, not an afterthought
  ([[2021-09-19_empty-state-interface-design]]).

### Onboarding to unfamiliar technology

When the technology itself is new to the user, the sources are markedly less
sceptical about explicit guidance.

- New technologies need "a little extra handholding": carefully introducing the
  technology in a simple way so users understand it and feel in control
  ([[2020-05-10_face-recognition-pay]]). Four onboarding failures in
  facial-recognition payment — no consent request, no explanation of how faces
  are recognised, no choice of payment account, no confirmation password —
  produced false mental models about security, and 4 of 5 participants preferred
  QR-code scanning despite the speed advantage. Convenience alone does not drive
  adoption.
- Users with no prior generative-AI experience cannot tell an image generator
  from a conversational chatbot, and tend to ask the chatbot about itself rather
  than consult documentation ([[2024-03-29_new-ai-users-onboarding]]). Brief,
  focused answers to "What does this do?" and "How does it work?" outperform long
  tutorials, and information placed too early in the journey is skipped because
  users do not yet see its relevance. Deliver detail at the right moment — voice
  tips when the user is about to use voice, not during setup.
- Tool names carry onboarding weight: a name should communicate function, and an
  unfamiliar name like "Rufus" means nothing to users
  ([[2024-03-29_new-ai-users-onboarding]], [[2025-03-21_discoverability-ai-amazon]]).
- Baseline familiarity with AI features is low, so research, standard design
  patterns, plain language, and contextual guidance are what let users discover
  and adopt them ([[2025-03-21_discoverability-ai-amazon]]). Nonstandard
  placement, ambiguous icons, and dense pages hide features users find valuable
  once shown. Mental models shift slowly but do shift — younger participants
  already looked for AI near the search bar — and standardisation across products
  accelerates that shift.
- In workshops, warmup activities such as AI-based icebreakers get the tool into
  participants' hands early and remove hesitation; pre-prepared context
  documents, custom AI instances, and adaptable sample prompts act as scaffolding
  for mixed skill levels, and having everyone use the same LLM keeps
  troubleshooting focused on prompting rather than tool differences
  ([[2025-05-30_preparing-ai-workshops]]).

### Prompt suggestions as lightweight onboarding

- Prompt suggestions are system-generated hints that address the blank-page
  problem when users first meet an open-text AI system, reducing cognitive load
  and interaction cost and encouraging exploration of capabilities users did not
  know existed ([[2025-04-25_prompt-suggestions]]). Three types: use-case
  suggestions (learnability and creativity), prompt autocomplete (efficiency),
  and followup questions (engagement) — the last currently the most relevant
  because they build on what the user has already asked.
- For new users in pre-authentication views, simple curated suggestions
  showcasing key capabilities work as lightweight onboarding and encourage
  account creation; for active users, context-aware suggestions delivered when
  they face ambiguity or lack domain knowledge give just-in-time guidance
  ([[2025-06-27_designing-use-case-prompt-suggestions]]).
- Complexity should match context: simple clickable pills for broad systems and
  low-complexity tasks, richer examples for specialised systems and complex
  tasks. Place suggestions near the input field, and prefer specific prompts
  ("Easy family dinners") over vague ones ("Recipe ideas")
  ([[2025-06-27_designing-use-case-prompt-suggestions]]).
- On specificity the two AI-onboarding sources point in different directions:
  general, broad prompts like "Generate text" are recommended as more inviting
  than niche examples that require the user to adapt them
  ([[2024-03-29_new-ai-users-onboarding]]), while the use-case suggestion article
  argues targeted, concrete suggestions let users assess relevance quickly and
  drive more engagement than generic ones
  ([[2025-06-27_designing-use-case-prompt-suggestions]]).

### Step-by-step setup flows and feedback

- Visual step-by-step wizards — one task at a time, supported by images,
  animations, and clear text — build confidence better than text-only
  instructions or several simultaneous tasks
  ([[2025-09-12_smart-device-onboarding]]).
- Because setup happens infrequently, users rarely remember the steps;
  reconnection after a power or WiFi outage deserves the same visual guidance,
  feedback cues, and progress reassurance as first-time setup
  ([[2025-09-12_smart-device-onboarding]]).
- Tell users what to expect physically (beeps, blinking lights) so they can judge
  whether the device is responding, keep progress indicators honest rather than
  filling a bar that does not reflect real progress, and make error messages
  specific and actionable instead of leaving users to trial and error
  ([[2025-09-12_smart-device-onboarding]]).
- AR calibration, which unlike onboarding recurs every session, follows the same
  shape: low-granularity instructions presented one at a time, descriptive and
  unambiguous wording rather than vague phrases like "scan a textured surface",
  text enclosed in solid high-contrast boxes so it stays readable against
  variable real-world backgrounds, and standard signifiers plus explicit feedback
  about system status and error recovery ([[2022-10-09_ar-calibration]]).
  Combining text, visual examples, and sometimes audio accommodates users holding
  a device at a distance or in contexts where reading is hard.

### Beyond the first session

- Users of complex applications fall into three profiles — the Legacy (long
  tenure, inefficient workarounds), the Legend (power user), and the Learner
  (domain expert new to the software) — and progression between them is fluid:
  learners become legends with proper support and discoverability, or become
  legacy users if abandoned ([[2025-06-27_complex-apps-users]]). Deliberate
  support for discoverability, learnability, safe exploration, and progressive
  feature introduction is what decides which.
- Reactive help remains necessary alongside proactive help: documentation and
  FAQs should be detailed and specific rather than high-level, scannable, chunked
  with highlighted keywords and lists, available as both text and video, grouped
  into categories, searchable, with top content highlighted
  ([[2020-12-13_help-and-documentation]]).

### Measuring it

- Track item creation, time to value, and the effect on overall retention; empty
  states are a basic quick win whose effectiveness should still be measured
  ([[2025-07-29_388_Empty_State_-_Guide_UX_design_pour_améliorer_l_onboarding]]).
- Measure entry points by click-through and bounce rate, and A/B test variants to
  find the best performer
  ([[2026-06-09_417_Les_3_clés_de_l_adoption_produit_-_Hacks_Growth_Design]]).
- Matched-group quantitative usability testing is what validated (and undermined)
  the assumed benefit of tutorials ([[2020-03-08_mobile-tutorials]]).

## Sources (19)

- [[2017-08-20_get-started]] — signup and orientation flows should be reserved for users who have decided to commit, not forced on new visitors before they understand what they're joining.
- [[2020-03-08_mobile-tutorials]] — reveals that formal deck-of-cards tutorials may not effectively onboard users to simple mobile apps and may even harm perceived usability.
- [[2020-05-10_face-recognition-pay]] — case study of how poor onboarding for facial-recognition payment creates security concerns; demonstrates that handholding during first use is essential for new technology adoption.
- [[2020-06-21_mobile-app-onboarding]] — Mobile onboarding comprises feature promotion, customization, and instructional components, each warranted at different times; teaching new interfaces benefits from learning through doing rather than tutorials, with evidence-based guidance on when each approach is most effective.
- [[2020-12-13_help-and-documentation]] — proactive help for new users at first launch or first encounter with a redesigned interface, including tutorials and instructional overlays that help users learn the system initially.
- [[2021-09-19_empty-state-interface-design]] — Empty states can serve as natural teaching moments that contextualize features and reduce reliance on external documentation or tutorials.
- [[2022-10-09_ar-calibration]] — effective calibration combines text, visual examples, and sometimes audio instructions to accommodate users holding devices at distances or in contexts where reading text is difficult.
- [[2023-02-12_onboarding-tutorials]] — onboarding tutorials are often misused as push revelations that interrupt users, but contextual help is more effective for teaching new interfaces.
- [[2024-03-29_new-ai-users-onboarding]] — Onboarding users to complex and unfamiliar technologies benefits from simplicity and contextual help over comprehensive tutorials, supported by effective communication approaches for teaching.
- [[2024-06-18_333_Design_contre-intuitif_Make_it_pop,_une_mauvaise_solution]]
- [[2025-03-21_discoverability-ai-amazon]] — Emphasizes that research, standard design patterns, plain language, and contextual guidance are essential to overcome low baseline familiarity and help users discover and adopt new AI features.
- [[2025-04-25_prompt-suggestions]] — emphasizes prompt suggestions' role in reducing friction for new users unfamiliar with AI capabilities and how to interact with them.
- [[2025-05-06_376_Designer_un_funnel_de_conversion_paywall_-_Gold_standard_2025]]
- [[2025-05-30_preparing-ai-workshops]] — providing initial exposure to AI tools and techniques that help participants become comfortable using them in group settings.
- [[2025-06-27_complex-apps-users]] — the process of helping new users progress from initial unfamiliarity to proficiency and confidence using complex systems.
- [[2025-06-27_designing-use-case-prompt-suggestions]] — Interface techniques and content, including contextually appropriate assistance, help new users understand system capabilities and progress from initial confusion to confident, effective system use and adoption.
- [[2025-07-29_388_Empty_State_-_Guide_UX_design_pour_améliorer_l_onboarding]]
- [[2025-09-12_smart-device-onboarding]] — Provides comprehensive guidance for smart-device onboarding through visual wizards, clear step-by-step flows, appropriate support options, and personalization prompts that make setup feel intuitive and complete.
- [[2026-06-09_417_Les_3_clés_de_l_adoption_produit_-_Hacks_Growth_Design]]
