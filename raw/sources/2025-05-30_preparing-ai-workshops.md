---
title: "4 Tips for Preparing AI-Enhanced Workshops"
date: "2025-05-30"
url: "https://www.nngroup.com/articles/preparing-ai-workshops/"
author: "Tanner Kohler"
topics: [ai]
type: article
---

As the [research by Fabrizio Dell'Acqua and colleagues proved](https://www.nngroup.com/articles/ai-creative-teammate/), generative AI (genAI) can boost team ideation. However, incorporating AI in team ideation can be challenging, especially if different team members have different experience levels with genAI. This article discusses how you can prepare for a successful and productive AI-enhanced workshop. A subsequent article will talk about how to run such a workshop.

## In This Article:

- [1. Prepare an AI WarmUp Activity to Build Familiarity](#toc-1-prepare-an-ai-warmup-activity-to-build-familiarity-1)
- [2. Upload Files for Quick and Easy Context](#toc-2-upload-files-for-quick-and-easy-context-2)
- [3. Create a Custom AI for More Powerful Context and Constraints](#toc-3-create-a-custom-ai-for-more-powerful-context-and-constraints-3)
- [4. Provide Adaptable Sample Prompts](#toc-4-provide-adaptable-sample-prompts-4)

## 1. Prepare an AI WarmUp Activity to Build Familiarity

When prepping any workshop — AI-enhanced or not — I always use a [warmup activity or icebreaker](https://www.nngroup.com/videos/ux-workshop-icebreakers/) to get people’s minds and mouths moving. **Well-crafted warmups help groups become familiar with the session’s tools.** Whether this is a shared document, a digital whiteboard, or Sharpies and [sticky notes](https://www.nngroup.com/articles/post-it-in-ux/), getting the tools into people’s hands is meant to remove any hesitations or access obstacles that participants may have. When I teach courses on AI, I always invite people to open their LLMs early in the session. Doing so ensures that everyone has them ready to go. I’d encourage workshop participants to use the same LLM. That way, people can troubleshoot problems and spend less time getting distracted by differences in various tools.

Here are **some fun AI-based warmup examples** you can use regardless of the group size or AI tool:

- Tell the AI 3 things you know about someone else in the group, and have it generate a picture of them.
- Give the AI the names of everyone in the group and ask it to combine them into a team name.
- Have the team work together to send a short sequence of emojis to the AI and have it generate a story based on them.

Consider asking the AI for more ideas with a prompt like, *“* Suggest some fun icebreakers I could use for a team who will be using AI in a workshop that have people use the AI in some way." Add more details to the prompt to adapt it to your participants and their interests or to the focus of the workshop.

## 2. Upload Files for Quick and Easy Context

Part of good prompting is [providing adequate context](https://www.nngroup.com/articles/careful-prompts/). Sample prompts help with this, but it’s often much more effective to **prepare context-providing documents before the workshop.** Participants can then simply upload these documents into their LLMs to provide context for their prompts. Uploads could include things like:

- A description of the company and the goods or services it provides
- [Personas](https://www.nngroup.com/articles/personas-study-guide/) or other research artifacts describing data-derived information about users and their needs
- A timeline for an upcoming project
- A list of constraints or [requirements](https://www.nngroup.com/articles/ux-user-stories/) pertinent to the task at hand
- Clean and prepared qualitative or quantitative user data (such as survey responses or interview transcripts) *—* however, please avoid using the AI in the workshop to formally analyze this data, as it should serve only for context.

Providing contextual uploads will also allow people to start fresh conversations with the AI without losing the relevant context — they could simply reupload the same information.

**Keep file formats straightforward and use text-based documents**. LLMs are getting better at reading PDFs, spreadsheets, images, and other file types, but I always recommend testing any files you’ll use by uploading them yourself ahead of time and asking the LLM to prove that it can read them.

## 3. Create a Custom AI for More Powerful Context and Constraints

Let’s say you’re running lots of workshops around a certain topic. Or there are many contextual documents that are cumbersome to upload. Or there are very specific constraints or formats you want the AI to apply to its responses. In such situations, **I recommend creating a custom AI that already knows everything workshop participants will need .** Three prominent examples of custom AIs include [GPTs](https://chatgpt.com/gpts) within ChatGPT, [Gems](https://gemini.google/overview/gems/?hl=en) within Gemini, and [Projects](https://www.anthropic.com/news/projects) within Claude.

Examples of UX use cases for a custom AI might include:

- **Personas:** Create a separate custom AI to impersonate each persona. Provide it with as much real data as you have about that persona’s needs. While the AI’s responses will not always align with what real users will say, they’ll be just as reliable as asking team members to predict user behavior.
- **Constraints:** Teach the custom AI your team structure and typical work cadence. Also, give it any other major constraints you’re working within so that it automatically considers these when suggesting ideas.
- **Stylistic guidelines:** Give the custom AI documentation on style, tone, word choice,, and samples of good content that aligns with those guidelines. The LLM will provide outputs that automatically align with that direction, without further instruction from workshop participants. .

For example, I recently ran a workshop with the course instructors at NN/g to ideate about valuable future UX trainings. I created a custom “Course Creation“ GPT that I had trained to understand learning objectives, good assessment practices, the scope and style of our courses, and many other NN/g-specific details. I had all instructors in the workshop exclusively use this custom GPT. This approach saved significant time and energy by aligning the various outputs from different people.

## 4. Provide Adaptable Sample Prompts

You never want to completely control the prompts people use when working with AI. Writing and iterating prompts together leverage the group's expertise and creativity. However, some people might struggle getting started for a couple of different reasons:

- They aren’t comfortable using AI, or aren’t very good at writing prompts [(yet)](https://www.nngroup.com/articles/mindsets-fixed-vs-growth/).
- They don’t understand the problem space and aren’t sure what direction to take things (initially).
- They’re feeling lazy and don’t want to do a bunch of writing.
- They aren’t comfortable quickly writing out their thoughts for fluency or language reasons.

Your sample prompts are meant to be a starter kit, intended for adaptation and abandonment as people get going. However, they can serve as instructive demonstrations of useful prompting and steer people in a helpful direction for the workshop. Here are some basic examples following our [CAREful framework](https://www.nngroup.com/articles/careful-prompts/):

### Example 1: Writing Web Copy

> **Context:**
> 
> 
> 
> - *I’m a UX writer working on an enterprise productivity app.*
> - *We’re updating the homepage hero section to highlight our new collaborative whiteboard feature better.*
> 
> 
> 
> **Ask:***You’re a UX copywriter.*
> 
> 
> 
> 1. *Write three headline options for the hero banner.*
> 2. *Draft ten 12-word subheaders emphasizing seamless teamwork.*
> 3. *Suggest ten 4-word calls-to-action that drive signups.*
> 
> 
> 
> **Rules:**
> 
> 
> 
> - *Tone: clear, approachable, and action-oriented*
> - *Headlines ≤ 7 words; subheaders ≤ 12 words; CTA ≤ 4 words*
> - *Include “collaborate” or “together” at least once.*
> - *Avoid jargon and superlatives.*
> 
> 
> 
> **Examples:**
> 
> 
> 
> - *Good headline: “Collaborate in Real Time”*
> - *Bad headline: “Revolutionize Your Team’s Synergy”*

### Example 2: Reorganizing an Onboarding Workflow

> **Context:**
> 
> 
> 
> - *I’m a UX designer for a B2B analytics platform.*
> - *New users report that our 5-step onboarding is confusing, leading to dropoff.*
> 
> 
> 
> **Ask:**
> 
> 
> 
> 1. *You’re a UX strategist.*
> 2. *Propose ten revised sequences of the five onboarding steps.*
> 3. *Rename each step with a clear verb-led title. Group related subtasks under consolidated steps.*
> 
> 
> 
> **Rules:**
> 
> 
> 
> - *Only five primary steps*
> - *Titles ≤ 3 words, each starting with a verb*
> - *Ensure logical flow from account setup to first dashboard view.*
> - *Use plain, nontechnical language.*
> 
> 
> 
> **Examples:**
> 
> 
> 
> - *Good step title: “Connect Data”*
> - *Bad step title: “Configure Data Integrations”*

### Example 3: Suggesting Survey Questions (by a UX Researcher)

> **Context:**
> 
> 
> 
> - *I’m a UX researcher evaluating our new in-app chat feature.*
> - *We need both quantitative and qualitative insights.*
> 
> 
> 
> **Ask:**
> 
> 
> 
> 1. *You’re a survey-design specialist.*
> 2. *Propose 20 questions: 15 on a 5-point Likert scale, 5 open-ended.*
> 3. *Cover ease of use, satisfaction, and feature usefulness.*
> 
> 
> 
> **Rules:**
> 
> 
> 
> - *Avoid leading or double-barreled questions.*
> - *Likert scale: “Strongly disagree” to “Strongly agree”*
> - *Open-ended prompts begin with “What” or “How.”*
> - *Keep each under 20 words.*
> 
> 
> 
> **Examples:**
> 
> 
> 
> - *Good Likert item: “I found the chat feature easy to navigate.”*
> - *Bad open-ended: “Don’t you think the chat UI is confusing?”*

### Conclusion

Improving your workshops with AI starts by planning to use the tool from the get-go. Consider how you can leverage the [things AI is good at](https://www.nngroup.com/articles/ai-superpowers/), like ideation and communication, to improve participation and activities. And don’t forget to plan around the fact that your teammates all have different familiarity with using LLMs. When you begin with a solid plan for using AI in your workshops, its ability to enhance productivity and collaboration will come naturally.

In the next article in this series, we’ll continue leveraging AI’s strengths for ideation and efficiency by discussing facilitation techniques.

### Reference

Fabrizio Dell'Acqua, Charles Ayoubi, Hila Lifshitz-Assaf, Raffaella Sadun, Ethan Mollick, E., Lilach Mollick Yi Han, Jeff Goldman, Hari Nair, Stew Taub, Karim R. Lakhani, 2025. [The cybernetic teammate: A field experiment on generative AI reshaping teamwork and expertise](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5188231)**(March 28, 2025). Harvard Business School Strategy Unit Working Paper No. 25-043, Harvard Business School Technology & Operations Mgt. Unit Working Paper No. 25-043, Harvard Business Working Paper No. No. 25-043, The Wharton School Research Paper, Available at SSRN: [https://ssrn.com/abstract=5188231](https://ssrn.com/abstract=5188231) or [http://dx.doi.org/10.2139/ssrn.5188231](https://dx.doi.org/10.2139/ssrn.5188231)
