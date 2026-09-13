---
title: "Vibe Architects: Agentic Vibe Coders"
date: "2026-06-19"
url: "https://www.nngroup.com/articles/vibe-architects/"
author: "Kate Moran, Sarah Gibbons"
topics: [ai]
type: article
---

Generative AI lets people's technical capability outpace their technical knowledge in ways that no previous technology has. We've seen this in vibe coding for some time.

Now, however, vibe coding is expanding into something broader, messier, and more impactful. This shift is tied to the rise of agentic AI and Claude Cowork, a flexible agentic system targeted at general information workers rather than engineers.

In our recent study, we learned how people manage to architect systems and transform workflows for themselves and their teams — without knowing much about exactly how they’re doing it. We call these people “vibe architects.”

## In This Article:

- [Meet the Vibe Architects](#toc-meet-the-vibe-architects-1)
- [How Vibe Architects Build](#toc-how-vibe-architects-build-2)
- [How Vibe Architects Learn](#toc-how-vibe-architects-learn-3)
- [What Vibe Architects Learn](#toc-what-vibe-architects-learn-4)
- [Conclusion](#toc-conclusion-5)

## Meet the Vibe Architects

The primary goal of our study was to **understand how people who are not professional developers use agentic AI.** The study was inspired by Claude Cowork's explicit focus on noncoders. We wanted to know how well Cowork serves that population.

For the study, we'd hoped to recruit people who were not developers, didn't work in our field (digital design, product, or UX), and used open-ended agentic tools like Claude Cowork or Claude Code. We managed to find 7 nontechnical people but struggled to find people outside of our industry (which may hint at how rare these people are).

Our participants included:

- An operations specialist building automation pipelines and deploying web apps for her team
- A product designer at a financial institution building personal software tools on evenings and weekends
- A marketing-startup founder running a headless orchestration system with proactive suggestions and multiagent coordination
- A head of product who put his entire team on a Claude-based “operating system” that replaced meetings, shared information, and facilitated decision making

All these individuals were building complex agentic systems using Claude (alongside other AI tools) for a wide array of personal and professional purposes — without having a technical background.

> **Vibe architects** build complex, proactive agentic systems using AI tools, sometimes with little technical knowledge or understanding of how these systems work.

Some of the systems that our participants created had traditional interfaces (e.g., vibe-coded dashboards or websites), but others lived purely in [Markdown](https://en.wikipedia.org/wiki/Markdown) text files or in the LLM’s chat. One participant showed us a dashboard he’d built, then mentioned he didn’t really look at it — he worked primarily in his code environment and the chat. The traditional UI was an afterthought.

These people were applying vibe coding to design how information flows across systems, how AI agents coordinate, and how work gets done — sometimes for entire teams.

As vibe architects build increasingly complex systems, they aren't learning about the technical functionality under the hood. Instead, they *are* developing something more amorphous — **a semi-instinctual set of behaviors, preferences, and tendencies,** shaped **** by hours spent experimenting, watching YouTube videos, and reading blogs.

**These instincts aren't always accurate or useful.** They reflect hazy [mental models](https://www.nngroup.com/articles/mental-models/) that sometimes produce real results and sometimes lead nowhere.

One participant, for example, developed a habit of resetting her Claude Cowork chats by importing the entire conversation into the prompt of a fresh conversation. She assumed that this practice saved tokens. While longer conversations do use more tokens, so does including the context in a long prompt.

Thus, while vibe architects can improve their and their teams’ workflows, the resulting systems aren’t always the most efficient or reliable. And, predictably, they report maintenance headaches: **The systems decay.** Connections expire, context drifts, and single sources of truth fall out of sync, so keeping everything running becomes a recurring tax on the architect’s time.

The participant who had moved his team’s primary communication into Claude said that his system would hold up “for a few weeks, and then the decay hits and we have to […] set up the process [again].”

Another participant described the same problem as **drift**: “As I develop my own stuff, [it] can start to drift, and managing that is […] harder.”

## How Vibe Architects Build

The latest-frontier models are extremely good at interpreting ambiguous prompts. So much so that many of our participants reported that **they don’t prompt engineer at all — they deliver stream-of-consciousness instructions** to their AI systems, often using dictation apps like Wispr Flow.

There is still some “engineering” happening, however. It’s less about choosing words in the prompt, and more about selecting tools, techniques, and approaches to get what they want. That process often involves asking Claude itself for help.

For example, one participant reported that he would always ask Claude, “What would make this world-class?” He said Claude often would respond with improvement suggestions, and he’d almost always accept them.

This was a common theme across our sample — **our participants often delegated the decision making, as well as the execution, to Claude.** They exercised minimal oversight on what Claude was up to.

During one session, a participant screenshared her Visual Studio Code window, where she primarily interacted with Claude Code. During the session, Claude was working on building something for her team and kept asking for permission to take various action. While speaking with us, she repeatedly clicked *Accept* without reading the requests. When we asked whether this was how she usually handled permission approvals, and she said yes.

> “Yes, because I don't want to give it *dangerously accept permissions* [level of access]. Most of the time I will just click ‘yes’ for things that [it] asks me, even if I don't understand what it means, because it only has […] the context of this folder. So, I don't really need to worry about it accessing other things.”

(*Dangerously accept permissions* was the label that Claude’s designers chose to prevent people from allowing the LLM to make unrestricted choices. Apparently, it was quite an effective label.)

Another participant told us he’s developed carpal tunnel from repeatedly accepting permission requests.

(As an aside, Anthropic released *Auto mode* in Claude Code shortly after we’d wrapped up our last session. This new option autoapproves requests that are not destructive or risky, selectively requiring permission only for certain actions. We hope our participants will discover this new feature, to save their poor finger tendons.)

## How Vibe Architects Learn

Our participants reported that they developed their vibe-architecting skills in **two primary ways: spending a great deal of time experimenting and learning from a community**.

### Time Spent Experimenting

Everyone in our sample invested a massive amount of time to get a “feel” for tools like Claude Cowork and Code. One participant reported spending 8 hours per day, 6–7 days per week inside AI chats. Another estimated spending 4–5 hours per day across Claude, Codex, and other tools. A third experimented with these tools on his home computer on evenings and weekends because his employer restricted AI use at work.

This time investment doesn't level off, either. These tools keep changing as AI labs ship model improvements and product updates, and other vibe architects share their ideas, so the vibe architects often must engage in continuous reevaluation. One participant used an agent to assess the evolving AI-tool landscape every 3–4 months, tracking what's changed and what new capabilities have emerged. Another scanned GitHub leaderboards weekly for new agents he could slot to his workflows. A third tested new tools daily.

The advanced users in our sample weren't exhausted by the constant change — they're excited by it. But that willingness to absorb continuous churn functions as a filter: it selects for a particular kind of person — one willing and able to invest this much time and energy into learning about AI tools.

### Learning from Other Vibe Architects

Across all seven participants, **the AI-coding products themselves consistently failed as a source of learning**, regardless of how technically sophisticated the participant was. This makes sense: LLMs are inherently opaque and uneven, and **users don’t see their limitations until they run into them.** Even when you are working with products from a single AI lab, like Anthropic’s, different models can behave differently and vary in how well they handle specific tasks.

System structures also matter: for example, orchestration agents managing subagents may perform better or worse, depending on what you’re building. Token usage, too, can be more or less efficient depending on how the system is set up. This **variability is one reason all our participants relied so much on experimentation.** While they could get advice and direction from Claude itself, none of participants reported using Claude as their primary way of learning and getting started.

Although Cowork was intended to help nontechnical folks get started with agentic AI, most of our participants didn’t truly understand its relationship to Code (even those that sometimes used both.)

> "I don't really understand what Cowork is for. I don't know."
> 
> 
> 
> "There's no onboarding. And even if you ask Claude itself, there's no real clear direction on when to use Cowork versus Chat."

One participant who used Cowork heavily couldn't figure out where he was inside Cowork's *Scheduled**Tasks* interface:

> "I don't even know where I am right now. I'm in Cowork within a scheduled run project on a particular date in a chat format. Where is that?"

Instead of learning within the product, all of our participants mentioned **learning how to use and build these systems from other people.**

In a few cases, these people were friends, partners, or coworkers. More often, though, our participants learned from online communities such as Twitter, Reddit, YouTube, and Slack groups. They followed other practitioners who had invested even more deeply in AI and shared back with the community what worked and what didn’t.

One participant described his primary learning channel:

> "Twitter, for sure. Twitter and Reddit. A big name will tweet something out and then in the replies will be 5 or 6 different, like, alternative suggestions."

He ran one of the most technically complex systems in our sample — 8+ tools, n8n automation, a team of named AI agents — and his primary source of knowledge was social media.

## What Vibe Architects Learn

You might expect that after hundreds or thousands of hours with these tools, advanced users eventually "get it" — that the system becomes legible and the vibes resolve into understanding. Our study shows the opposite.

**Opacity persists** at the deepest end of the practice spectrum.

One participant told us that one of his agents had attempted to make a $200 purchase the night before. When asked how he prevented these kinds of incidents, he went hunting through his files, unsure of what was governing the system. He found a file called *boundaries.md*, which contained security and privacy guidelines. He opened it and seemed surprised by what was in it. He hadn’t written it himself; Claude had created and maintained this governance architecture largely on its own, and his role was to authorize it after the fact.

The vibes compound — they just don't crystallize into the kind of clear, articulable knowledge we typically associate with expertise. What accumulates is intuition: a thicker sense of the shape of the technology, a feel for where it fails, and a growing **instinct for how to poke it to get what you want.** Our participants struggled to name how they know what they know. One said:

> "I know enough about AI to realize that I really don't know anything about it… I understand how to use it, I wouldn't be able to rebuild [this system] — is probably how I would best describe that."

Learning something new can feel like looking through a foggy window that gradually clears. Agentic AI is different: it is more like navigating in patchy fog, where some areas briefly come into view while others remain obscured. You gain a better sense of the terrain, but never a full, stable picture. And just as the fog starts to lift in one place, the landscape shifts as AI labs release new models and product updates that rearrange the interface overnight.

This opacity also carries a sense of guilt: **Nearly every participant in our study assumed that someone else must be doing this more cleanly**, more professionally, more correctly than they were.

One participant named it directly:

> "I'm not actually […] nervous or embarrassed about it, but there's definitely an emotion of like, ‘oh, I'm going to be not criticized, but […] I'm embarrassed at how poorly I'm using this tool.’"

**Going with the vibe is not a shortcut to the "real" way of using these tools –- it is the practice.** At least in this user population, there is no non-vibes version of working with these tools.

It’s likely (or at least we hope) that enterprises building agentic systems into their workflows and products are doing so in a more formal, reliable, and rigorously evaluated way, especially since those systems are more likely to be built by developers who understand code and AI engineering in ways our study participants may not.

But even if that’s true, the **real value of these hacked-together agentic systems is in how customized they are.** Vibe architects know their systems are messy, yet they’re uniquely tailored to them and their context, and can be finetuned as their creators’ needs change.

It may be a house of cards, but it’s still a useful one.

## Conclusion

This is how tacit knowledge has always spread — through observation, shared practice, and time spent doing the work.

What's unusual is that it’s happening with **a technology that's supposed to be intuitive enough to not need this kind of apprenticeship**. The promise of conversational systems has been that *anyone* can use them simply through conversation. At least right now, that doesn’t seem to be the case.

While we don’t have data on the people who didn’t participate in our study, we can make reasonable assumptions based on how hard the sample was to recruit and what those people had in common. They were almost all in our industry (tech), which means they’re likely more aware of AI concepts and capabilities than the broader population. Some of them had tech-savvy friends or colleagues who encouraged and helped them get started. And they all had substantial time and motivation to vibe until their intuitive sense allowed them to piece together something useful, if fragile.

The bet that nondevelopers are the next major market for agentic AI has stopped being a quiet hypothesis and started shipping as product strategy. Days after our final session, OpenAI repositioned Codex out of the developer’s IDE, launching six job-specific plugins for roles like sales, creative production, and public-equity investing, with corporate finance, marketing strategy, and strategy consulting named as next in line. Knowledge workers are already about a fifth of Codex’s 5 million weekly users, and they’re growing more than three times as fast as developers ([according to OpenAI](https://openai.com/index/codex-for-knowledge-work/)). Anthropic built Cowork on the same wager.

But our study suggests capability alone won’t win that market. **These tools are already extraordinarily powerful; what they still lack is a usable entry point**

The vibe architects we met found their way in through years of immersion, the right online communities, and an intuition no documentation can hand you. Until the labs make that path shorter — until competence stops requiring an apprenticeship — poor usability will limit the reach of these tools, and the people who benefit will keep being the ones who were already close enough to figure it out on their own.
