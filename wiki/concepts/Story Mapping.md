---
type: concept
name: Story Mapping
created: 2026-09-11
updated: 2026-09-11
status: developed
aliases:
  - "Story Map"
  - "Story Maps"
  - "User Story Mapping"
---

# Story Mapping

## Definition

Story mapping is a technique for arranging user stories in two dimensions on a shared surface (index cards, sticky notes, or paper) so that a team can see a whole product at once instead of a flat list of features. Left to right, the map follows the **narrative flow**: the order in which you would tell the story of what a person does. Top to bottom, it holds **detail and priority**: the alternatives, variations and edge cases under each step, and, once the map is sliced, what is needed for a given outcome versus what can wait ([[2014-09-05_user-story-mapping_06-1-the-big-picture]], [[2014-09-05_user-story-mapping_10-5-you-already-know-how]]). Jeff Patton summarises the whole practice in the preface as telling a product's story with others, writing each big step the users take on sticky notes in a left-to-right flow, then going back to talk about the details of each step and placing those vertically underneath ([[2014-09-05_user-story-mapping_04-preface]]).

The problem it answers is the one Martin Fowler names in his foreword: splitting requirements into small stories gives real visibility into progress, but the pieces can end up "a jumble of pieces that don't fit into a coherent whole," or the essence of what is needed can be lost in the details ([[2014-09-05_user-story-mapping_01-foreword-by-martin-fowler]]). Alan Cooper makes the same point from the design side: building one feature at a time is a perfectly good construction strategy and a ruinous design method, yielding what he calls a Frankenstein monster of a program; he frames story mapping as the Rosetta Stone that keeps the designer's narrative structure intact while still letting the work be deconstructed for implementation ([[2014-09-05_user-story-mapping_02-foreword-by-alan-cooper]]). Patton's own framing across the book is less about documentation and more about conversation: stories get their name from how they should be used, not from what should be written, and the map is what makes the conversation collective and visible ([[2014-09-05_user-story-mapping_06-1-the-big-picture]]).

## Practice

### The two axes

- **Narrative flow, left to right.** Tasks are placed in the order they happen, with a hidden "and then" connecting each sticky; reading across the map tells the story of the journey ([[2014-09-05_user-story-mapping_10-5-you-already-know-how]]).
- **Detail and alternatives, top to bottom.** Once the main flow is laid out, ask the what-about questions: what happens when things go wrong, what if the user is in a hurry, what the ideal version looks like. Those tasks go vertically below the main narrative ([[2014-09-05_user-story-mapping_10-5-you-already-know-how]]).
- Patton warns against collapsing the two: stop and let the team finish the big story before diving into details, since the spatial relationships are what communicate meaning without words ([[2014-09-05_user-story-mapping_06-1-the-big-picture]]).

### User tasks, goal level, and the backbone

- The atomic unit is a **user task**: a short verb phrase describing something a person does to reach a goal, such as "Hit snooze" or "Take a shower". Patton calls tasks the basic building blocks of a story map ([[2014-09-05_user-story-mapping_10-5-you-already-know-how]]).
- **Goal level**, a concept Patton attributes to Alistair Cockburn, sorts tasks by scale: summary-level (many smaller tasks roll up into it), functional or "sea-level" (a natural stopping point), and subtask-level (done as part of a larger task). Use it to aggregate small tasks or decompose large ones ([[2014-09-05_user-story-mapping_10-5-you-already-know-how]]).
- **Activities** are clusters of tasks sharing a common goal, such as "Get ready" or "Make breakfast". Grouped along the top, the activities form the **backbone** of the map and are themselves read left to right as a high-level story ([[2014-09-05_user-story-mapping_10-5-you-already-know-how]]).
- The size of what a single card represents is unknowable until the team talks about it: a couple of hours, days, weeks or a month of development ([[2014-09-05_user-story-mapping_06-1-the-big-picture]]). See [[User Story]] and [[Customer Journey]].

### Slicing the map into releases

- A **slice** is a horizontal line drawn across the map; everything that would not be needed to reach a particular goal moves below the line. Slicing reveals priorities and shows the different paths through the map ([[2014-09-05_user-story-mapping_10-5-you-already-know-how]]).
- At Globo.com, Brazil's largest media company, eight teams from three divisions (Sports, News, Entertainment) mapped an interdependent rebuild of a content management system. Facing deadlines that do not move (sports events, television premieres, elections), they realised the full map would take over a year. Patton pushed the question "What outcomes do we need for the upcoming Brazilian election?" and the teams sliced the map with blue painter's tape into staged releases, each with target outcomes, so each release delivered real benefit ([[2014-09-05_user-story-mapping_07-2-plan-to-build-less]]).
- Patton's rule in that chapter is to **prioritise outcomes, not features**: that is what breaks down large scope. He also insists there is always more to build than you have people, time, or money for ([[2014-09-05_user-story-mapping_07-2-plan-to-build-less]]). See [[Release Planning]] and [[Product Outcome]].
- The same chapter gives Patton's definitions of MVP: a bad one (the crappiest product), and two good ones, the smallest release that successfully achieves its desired outcomes and, per Eric Ries, the smallest experiment to test assumptions. Patton is explicit that defining MVP is a guessing game about customer behaviour, feasibility and what makes people happy ([[2014-09-05_user-story-mapping_07-2-plan-to-build-less]], [[Minimum Viable Product]]).

### Now map versus later map

- The same mechanics serve two different maps: a **now map** of how people work today, and a map of how they will work with the new software. Patton presents them as identical in mechanics and different in purpose ([[2014-09-05_user-story-mapping_10-5-you-already-know-how]]).
- In the rock-breaking chapter, Patton describes mapping as a practice that helps teams understand how people work today and then imagine how things will change with a new solution, used especially during **discovery** to explore the scope and shape of what to build ([[2014-09-05_user-story-mapping_16-11-rock-breaking]]).
- Building a now map means talking directly with the people who do the work and capturing the reality of how they actually do things, not how designers or developers imagine they should ([[2014-09-05_user-story-mapping_10-5-you-already-know-how]]).

### Mapping as a group activity

- **Talk and doc**: write cards or sticky notes to externalise your thinking as you tell stories. Patton's argument is that this stops ideas vaporising, lets people refer back and reorganise, and that pointing at a card helps everyone recall the conversation ([[2014-09-05_user-story-mapping_06-1-the-big-picture]]).
- Frame first: before telling stories about features, agree why you are building the product, who will use it, and which users matter most ([[2014-09-05_user-story-mapping_06-1-the-big-picture]]).
- Mapping together is what produces [[Shared Understanding]]: it surfaces gaps in thinking, exposes where people disagree (down to whether you brush your teeth before or after breakfast) and forces the group to separate what matters from what is just preference ([[2014-09-05_user-story-mapping_06-1-the-big-picture]], [[2014-09-05_user-story-mapping_10-5-you-already-know-how]]). "Mapping your story helps you find holes in your thinking" ([[2014-09-05_user-story-mapping_06-1-the-big-picture]]).
- Across several teams, the map is also a dependency view: at Globo.com it revealed work each team assumed another was handling and nobody was. Patton's formulation of the phenomenon is that scope doesn't creep, understanding grows ([[2014-09-05_user-story-mapping_07-2-plan-to-build-less]]).
- Fowler insists the practice is for everyone involved in development, not just analysts: programmers are a vital source of ideas because they know best what software can do, and stories should not be one-way communication from analyst to developer ([[2014-09-05_user-story-mapping_01-foreword-by-martin-fowler]]). Cooper adds that design and development are distinct disciplines with different skill sets, and that story mapping is what gives them a common language ([[2014-09-05_user-story-mapping_02-foreword-by-alan-cooper]]). See [[Team Collaboration]] and [[Workshop Facilitation]].

### Worked examples the sources carry

- **Gary Levitt and Mad Mimi** — Patton helped Gary externalise his product vision out of a flat prioritised backlog into a spatial map, which revealed the true size and complexity of the product. The flat backlog is the counter-example throughout: prioritising a flat list of features can lead a team to build things that do not solve the real user problem, as happened in Gary's initial development ([[2014-09-05_user-story-mapping_06-1-the-big-picture]], [[Product Backlog]]).
- **The Learning Connexion**, an art college in New Zealand, used mapping to give a diverse team shared understanding of their business process and to prioritise what was truly vital ([[2014-09-05_user-story-mapping_06-1-the-big-picture]]).
- **FORUM Credit Union and SEP** — a sidebar in the "plan to build less" chapter describes mapping to build shared understanding around priorities, colour-coding sticky notes to distinguish differentiator, spoiler, cost reducer and table stakes features; the exercise revealed hundreds of thousands in savings before coding began ([[2014-09-05_user-story-mapping_07-2-plan-to-build-less]]).
- **Kent Beck** originated the story concept in Extreme Programming, with communication as a key value; Patton's stated reason for writing a whole book rather than a short guide is that in the decade and a half since, stories had become more popular and more misunderstood than ever ([[2014-09-05_user-story-mapping_01-foreword-by-martin-fowler]], [[2014-09-05_user-story-mapping_04-preface]]).

### A second, narrower use: surfacing assumptions

The eighth source uses the term for a different purpose than the book does. Teresa Torres presents story mapping as one of five methods for **identifying hidden assumptions**: map the steps each user or actor must take to get value from a given solution, then generate assumptions for each step, asking what must be true for that step to work and which desirability, feasibility and usability bets are being made. In her framing the map's value is that it forces the team to be specific and reveals dozens of hidden assumptions about what users will do, understand and want; the assumptions then go into an assumption map to find the riskiest ones ([[2021-05-18_continuous-discovery-habits_12-chapter-nine-identifying-hidden-assumptions]], [[Assumption Mapping]], [[Assumption Testing]]).

The two accounts do not contradict each other so much as aim at different things, and the corpus should not smooth them together. Patton's map is a planning and shared-understanding artifact for a whole product, with a backbone of activities, vertical detail and slices that become releases ([[2014-09-05_user-story-mapping_06-1-the-big-picture]], [[2014-09-05_user-story-mapping_07-2-plan-to-build-less]]). Torres's story map is per-idea and disposable, a way of interrogating one candidate solution before it is built; nothing in her chapter uses the backbone, the goal levels or release slicing ([[2021-05-18_continuous-discovery-habits_12-chapter-nine-identifying-hidden-assumptions]]). Patton's own discovery-side account, where mapping explores the scope and shape of what to build and digs into assumptions about who the customers are and how a solution would change their world, is the closest the two come to meeting ([[2014-09-05_user-story-mapping_16-11-rock-breaking]]).

## Sources (8)

- [[2014-09-05_user-story-mapping_01-foreword-by-martin-fowler]] — Fowler presents story mapping as the core technique for preserving the big picture and coherent user experience while working story-by-story in Agile.
- [[2014-09-05_user-story-mapping_02-foreword-by-alan-cooper]] — Cooper frames story mapping as the bridge that lets designers and developers collaborate, preserving narrative and design intent while enabling functional decomposition.
- [[2014-09-05_user-story-mapping_04-preface]] — Patton describes story mapping as a simple-to-execute practice that organizes stories into a left-to-right narrative with top-to-bottom details, making them more useful for Agile backlogs.
- [[2014-09-05_user-story-mapping_06-1-the-big-picture]] — The core technique: organizing user stories spatially on a surface (cards, sticky notes, or paper) to show sequence left to right and decomposition top to bottom, creating a visual representation of a user journey.
- [[2014-09-05_user-story-mapping_07-2-plan-to-build-less]] — Story mapping helps teams visualize their complete work and interdependencies, find planning holes, and make collective decisions about which outcomes to prioritize for staged releases.
- [[2014-09-05_user-story-mapping_10-5-you-already-know-how]] — The mechanics are introduced through the morning routine exercise: tasks arranged in narrative flow (left-to-right), depth added for alternatives and edge cases, and tasks grouped under activities to form a backbone.
- [[2014-09-05_user-story-mapping_16-11-rock-breaking]] — Patton describes story mapping as a practice that helps teams understand how people work today and then imagine how things will change with a new solution. It is used especially during discovery to explore the scope and shape of what to build.
- [[2021-05-18_continuous-discovery-habits_12-chapter-nine-identifying-hidden-assumptions]] — A technique for clarifying what an idea actually means by mapping the steps each user (or actor) must take to get value from the solution; story maps force teams to be specific and reveal dozens of hidden assumptions about what users will do, understand, and want.
