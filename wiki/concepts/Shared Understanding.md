---
type: concept
name: Shared Understanding
created: 2026-09-11
updated: 2026-09-11
status: developed
aliases:
  - "Information Radiator"
---

# Shared Understanding

## Definition

Shared understanding is the state in which the people who will build a product, the people who understand the problem it solves, and the stakeholders around them all hold the same picture of what is being made, for whom, and why. Jeff Patton makes it the explicit goal of working with stories: the point of a story is not a better-written card but a group that has talked its way to a common picture ([[2014-09-05_user-story-mapping_05-read-this-first]]). He frames the failure mode through the telephone game and the NASA Mars Climate Orbiter crash: a shared document is not shared understanding, because different readers imagine different things from the same words. Kent Beck's original insight behind user stories was the same one, and it is why stories replaced document-driven specification with conversation ([[2014-09-05_user-story-mapping_11-6-the-real-story-about-stories]]).

It is built rather than written: through conversation with thinking externalized into words and pictures, sticky notes, sketches and maps, so that people can see where they differ and correct each other. It is also perishable and non-transferable. Patton is explicit that the shared picture lives in the heads of the people who were in the conversation, not on paper, which is why handing the details off to someone else to build does not work ([[2014-09-05_user-story-mapping_14-9-the-card-is-just-the-beginning]]). Anna Dahlström describes the same effect at organisational scale: collaborating on storyboards and experience maps is what breaks down silos and gets different parts of the business to a common view ([[2019-12-17_storytelling-in-design_09-chapter-8-storyboarding-for-product-design]]).

## Practice

### Talk, and externalise the talking

- Write cards or sticky notes as the team tells stories, what Patton calls **talk and doc**: it stops ideas vaporising, lets people refer back and reorganise, and pointing at a card helps everyone recall the conversation ([[2014-09-05_user-story-mapping_06-1-the-big-picture]]).
- Rich story conversations use words *and* pictures, whiteboard sketches, workflow diagrams, personas, marked-up models ([[2014-09-05_user-story-mapping_11-6-the-real-story-about-stories]]).
- Photograph the whiteboards and flipcharts as you go, Patton's **vacation photos**, and share them; the visual record becomes the team's shared memory of what was decided ([[2014-09-05_user-story-mapping_12-7-telling-better-stories]]).
- Do not attempt this with a tracking tool. Patton, crediting Alistair Cockburn's *Agile Software Development: The Cooperative Game* for the term, contrasts an **information radiator**, big visible information on a wall that radiates into the room, with information that lives only in a tool and goes stale like frost at the back of a freezer. Physical tools are for real-time sense-making; digital tools are for tracking progress and storing decisions once the conversation is done ([[2014-09-05_user-story-mapping_13-8-its-not-all-on-the-card]]).

### What to talk about

- Work a checklist rather than a template: who (be specific about user types, customers, other stakeholders), what (user tasks, but also services and edge cases), why (the layered "why stick"), context (where, when, who else is present), what goes wrong, assumptions and open questions, better solutions, how, and how long ([[2014-09-05_user-story-mapping_12-7-telling-better-stories]]).
- Patton warns against **template zombies**, a term he takes from Tom DeMarco et al., *Adrenaline Junkies and Template Zombies*: forcing ideas into "as a... I want... so that..." reverts to document-driven thinking and kills the conversation. The template is a snowplow, useful for learning, not best practice for all terrain ([[2014-09-05_user-story-mapping_12-7-telling-better-stories]]).
- Ron Jeffries et al.'s **3 Cs** locate it precisely: the card is a minimal written prompt, the *conversation* is where shared understanding happens, and confirmation is agreeing on acceptance criteria ([[2014-09-05_user-story-mapping_11-6-the-real-story-about-stories]]).
- Be respectful of the expertise in the room: do not tell a technical specialist how to do her work, or tell someone who knows the users that he does not understand ([[2014-09-05_user-story-mapping_12-7-telling-better-stories]]).

### Build it by mapping and modelling together

- A story map built together surfaces gaps in thinking, reveals where people disagree, and builds collective ownership ([[2014-09-05_user-story-mapping_06-1-the-big-picture]]). In the morning-routine exercise the disagreement is trivial on its face, brushing teeth before or after breakfast, and the point is that laying the map out forces the group to separate what actually matters from what is merely preference ([[2014-09-05_user-story-mapping_10-5-you-already-know-how]]).
- Discovery's primary output is this shared mental model, not a list of stories. Patton's models, personas, journey maps, story maps, UI sketches, architectural sketches, exist to support different kinds of conversation, and personas in particular should be built collaboratively on flipchart paper rather than locked in a document nobody reads ([[2014-09-05_user-story-mapping_19-14-using-discovery-to-build-shared-understanding]]). Describing an idea in words alone leads developers to imagine something other than what was intended; words and pictures together prevent it.
- Storyboards and experience maps do the same work across the business. Dahlström recommends experience maps as living documents, printed large and visible, and cites the Rail Europe Experience Map by Chris Risdon and Adaptive Path as a catalyst that got people talking and aligned the company on touchpoints ([[2019-12-17_storytelling-in-design_09-chapter-8-storyboarding-for-product-design]]).
- Map how people work today, not how you imagine they should ([[2014-09-05_user-story-mapping_10-5-you-already-know-how]]).

### How many people, and for how long

- Patton names as an anti-pattern the belief that everyone must be in every conversation: effective discussion and decision making runs best with two to five people, "dinner conversation sized", with small groups deciding and continued conversation spreading the result ([[2014-09-05_user-story-mapping_14-9-the-card-is-just-the-beginning]]). Mat Cropper's account of a 25-person UK government team points the same way: splitting a whole-team planning "car crash" into a four-person grooming group and short write-ups with a developer pair made the large sessions easy ([[2014-09-05_user-story-mapping_12-7-telling-better-stories]]).
- That said, every role has a legitimate and different conversation about the same story, product manager, analyst, tester, UX designer, project manager, each caring about market hypotheses, business rules, failure modes, usability, dependencies, schedule. Teams must deliberately design multiple conversation channels rather than one meeting ([[2014-09-05_user-story-mapping_13-8-its-not-all-on-the-card]]).
- Shared understanding is not a milestone that closes. Maintain it through the build by continued storytelling and presence: someone who was in the discovery conversation retells the story to whoever needs it next, and the listener asks questions and marks up pictures to build her own vacation photos ([[2014-09-05_user-story-mapping_14-9-the-card-is-just-the-beginning]]).

### Why it pays off

- Estimation. Patton's position is that the best estimates come from developers who really understand what they are estimating, including who the user is and why it matters, and that this beats any estimation method applied to unclear requirements ([[2014-09-05_user-story-mapping_09-4-plan-to-finish-on-time]]).
- Scope. Prioritisation flows from specific business goals to specific users and their goals and only then to features; good discovery discards more ideas than it keeps ([[2014-09-05_user-story-mapping_19-14-using-discovery-to-build-shared-understanding]]).
- Buy-in. Collaborating on storyboards is what gets different parts of the business to incorporate both user insight and business requirements into the same product ([[2019-12-17_storytelling-in-design_09-chapter-8-storyboarding-for-product-design]]).

### Its limit

A team agreeing with itself is not evidence. The team's shared picture routinely differs from users' reality, so it must be tested against real users; user testing reveals the mismatch quickly and supplies both the motivation and the direction for improvement ([[2014-09-05_user-story-mapping_14-9-the-card-is-just-the-beginning]]).

## Sources (10)

- [[2014-09-05_user-story-mapping_05-read-this-first]] — Patton establishes shared understanding as the true goal of stories and story conversations, achieved through collaborative dialogue and externalized thinking, not through written documents or specifications.
- [[2014-09-05_user-story-mapping_06-1-the-big-picture]] — The entire chapter emphasizes that the primary value of story mapping is building shared understanding among team members, customers, and stakeholders about what the product does and why.
- [[2014-09-05_user-story-mapping_09-4-plan-to-finish-on-time]] — The foundation of accurate estimation; developers and the whole team must understand who the user is, what they're trying to accomplish, and why it matters.
- [[2014-09-05_user-story-mapping_10-5-you-already-know-how]] — Built by mapping together with real people; seeing the map laid out reveals disagreements (e.g., whether to brush teeth before or after breakfast) and forces the group to agree on what matters and what's just preference.
- [[2014-09-05_user-story-mapping_11-6-the-real-story-about-stories]] — Built through conversation and discussion, not documents; when multiple people talk together about a story using words and pictures, they correct misunderstandings and arrive at alignment.
- [[2014-09-05_user-story-mapping_12-7-telling-better-stories]] — Built by talking through a checklist of considerations (who, what, why, context, failure modes, assumptions, solutions); teams that record these discussions on whiteboards and photograph them create shared memory.
- [[2014-09-05_user-story-mapping_13-8-its-not-all-on-the-card]] — Building shared understanding is the critical first goal when presenting a story; it requires conversations and externalizing ideas on walls or in shared spaces, and it fails when information is locked into email or tools.
- [[2014-09-05_user-story-mapping_14-9-the-card-is-just-the-beginning]] — Patton emphasizes that shared understanding must be maintained throughout the build process through continued storytelling and presence, not handed off as documentation, and that everyone's shared picture must be tested against user reality.
- [[2014-09-05_user-story-mapping_19-14-using-discovery-to-build-shared-understanding]] — The entire chapter returns to this core theme: discovery's primary output is not a list of stories but a shared mental model that product, design, engineering, and stakeholders all agree on; this is built through collaborative creation of models (maps, sketches, personas).
- [[2019-12-17_storytelling-in-design_09-chapter-8-storyboarding-for-product-design]] — By collaborating on storyboards and experience maps, teams break down organizational silos and build buy-in; Dahlström stresses that different parts of the business must come together to create products that truly incorporate user insight and business requirements.
