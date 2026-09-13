---
title: "Stop Making Your Team Figure Out AI on Their Own"
date: "2025-10-31"
url: "https://www.nngroup.com/articles/ai-research-ops/"
author: "Laura Klein"
topics: [ai, ux-management]
type: article
---

If you work in research or design, chances are someone in leadership has asked you about AI lately. Maybe they've suggested you "explore" how ChatGPT could help with your work. Maybe they've mentioned that using AI tools will be part of your next performance review. Maybe they've forwarded you an article about how AI is revolutionizing UX research with a cheerful "Thoughts?"

Here's what's actually happening in most organizations: people are being told to use AI without being given any real guidance on how, why, or which problems it should solve. It's creating chaos, security risks, and collaboration problems.

## In This Article:

- [The Performance-Review Problem](#toc-the-performance-review-problem-1)
- [The Grimoire Problem](#toc-the-grimoire-problem-2)
- [The Context-Switching Tax](#toc-the-context-switching-tax-3)
- [The Context Issue](#toc-the-context-issue-4)
- [The Security Nightmare](#toc-the-security-nightmare-5)
- [The Collaboration Breakdown](#toc-the-collaboration-breakdown-6)
- [What Actually Works: The Ops Approach](#toc-what-actually-works-the-ops-approach-7)
- [Stop Asking Everyone to Be a Pioneer](#toc-stop-asking-everyone-to-be-a-pioneer-8)

## The Performance-Review Problem

Let's start with the most immediate issue: **teams are evaluated on their AI usage without clear definitions of what successful usage looks like**.

I recently spoke with a researcher who told me that, for her quarterly review, her manager asked her to document how she'd incorporated AI into her workflow. She'd used ChatGPT a few times to help organize interview notes but honestly wasn't sure if that counted or if she should be doing something more sophisticated. Her colleague on the same team was being praised for using AI extensively, but nobody could articulate what made his approach better or whether it was improving outcomes.

This is backwards. **We're measuring adoption before we've measured value.** It's like grading developers on how many new JavaScript frameworks they've tried without asking whether their code is actually better.

When you tell people they'll be evaluated on using a tool without giving them clear guidelines, you create performative usage. People start mentioning AI in their status updates and sprinkling ChatGPT screenshots into their documentation, not because it's making their work better, but because they need to prove they're keeping up. That's not innovation. That's theater.

## The Grimoire Problem

Meanwhile, the people who *are* using AI heavily have often developed elaborate systems that work for them but are completely opaque to everyone else. They've accumulated massive collections of multistep prompts that might as well be magic spells. They think that if they feed Claude exactly the right context in exactly the right order, they'll get useful research summaries. They've learned that GPT-4 is better for certain types of synthesis while Sonnet 4.5 is better for others. They've figured out workarounds for common failure modes.

I have started calling these collections of incantations “[grimoires](https://en.wikipedia.org/wiki/Grimoire)” because they remind me of witches’ spellbooks. The prompts and guidelines might work for the original practitioner, but they are frequently missing important information that would allow anybody else to use them.

This knowledge could be valuable to other members of the team, but it's trapped in individual practitioners' heads (or worse, in their personal note-taking apps). There's no good way to share it with the rest of the team. Posting a prompt in Slack gets it lost in the scroll. Creating a document just means that everybody ends up with their own private spellbook rather than anything shared and, more importantly, tested by more than one person. And even when people do share their approaches, it can be hard for others to understand the context and reasoning behind why something works.

**This is exactly the kind of knowledge-management problem that ops teams are supposed to solve.** We've developed systematic approaches to sharing design patterns, research methodologies, and testing strategies. But when it comes to AI, everyone is expected to figure it out themselves and, maybe, if they're feeling generous, share a tip or two with their immediate team.

## The Context-Switching Tax

Here's another pattern I'm seeing: experienced practitioners are using different AI tools for different parts of their workflow. They might use ChatGPT for brainstorming, Claude for analysis, Perplexity for research, and GitHub Copilot for any light coding work. Each tool has its strengths, and switching between them seems logical.

But here's the problem: every time you switch tools, you lose context. That interview you had Claude summarize? You now need to manually copy that summary into ChatGPT if you want to use it for ideation. The research questions you brainstormed in one tool need to be reentered into another tool when you're ready to draft your discussion guide. You're essentially working with a bunch of tools that can't talk to each other, and **you're the integration layer.**

This is exhausting and error-prone. More importantly, it means that each tool is working with a fraction of the relevant context. The AI helping you write your research plan doesn't know anything about the previous three research projects you conducted on similar topics. The one helping you analyze data doesn't have access to the strategic goals that shaped your research questions in the first place.

We wouldn't accept this fragmentation with our other tools. Imagine if your design system lived in three different places and you had to manually copy components between them. We'd recognize that as a workflow problem that needed solving.

## The Context Issue

Because general-purpose AI tools don't have shared organizational memory, everyone needs to manually provide context every time they use them. This leads to a few predictable problems.

First, people forget things. You might remember to tell the AI about your current project goals but forget to mention the recent user research that directly contradicts your initial assumptions. Or, you remember the research but forget about the technical constraints that will shape what's possible to build. The quality of what you get out is directly tied to the quality of what you put in, and humans are terrible at comprehensively remembering everything that's relevant.

Second, people don't always know what's relevant. A senior researcher might have the experience to know that historical customer-satisfaction scores are crucial context for interpreting new interview data. A junior researcher might not think to include that information. Without a systematic way of ensuring the right context gets provided, you get wildly variable results depending on who's doing the work.

Third, and most seriously, people make security mistakes. When everyone is responsible for figuring out what to upload and what not to upload, the wrong thing will inevitably be uploaded.

## The Security Nightmare

This is where things get genuinely scary. I've heard stories from multiple organizations where people have pasted customer data, including personally identifiable information, into public AI tools. Not because they're careless, but because nobody gave them clear guidelines about what was okay and what wasn't.

This could be somebody copying interview transcripts that include participant names, email addresses, and demographic information into ChatGPT because they want help identifying themes. Or it could be somebody pasting internal strategy documents into Claude because they want to draft a research plan that aligns with upcoming launches. It could be somebody uploading a spreadsheet with customer-usage data because they're trying to identify patterns.

In most cases, these people aren't doing anything that feels risky to them. They're just trying to do their jobs, and AI tools seem like a reasonable way to work faster. But they're **inadvertently creating massive compliance and privacy risks** because nobody has given them clear policies or, more importantly, tools that are designed to keep them safe.

This isn't a training problem you can solve by sending around a memo about not uploading personal identifying information. People are making dozens of micro decisions every day about what information to share with AI tools, and expecting each individual to perfectly navigate the security implications is unrealistic.

## The Collaboration Breakdown

Now imagine you're trying to collaborate on a design project with a colleague. You've been using one tool with a carefully crafted set of prompts to structure your wireframes. Your colleague prefers a different tool and has developed a completely different approach. You want to work together on creating an interactive prototype, but you can't easily share your AI-assisted work because it's tied to different tools and different methodologies.

This is like one designer insisting on Figma, another demanding Sketch, and a third preferring Adobe XD for the same project. Or, imagine if every researcher on your team used a different repository for storing their work, or a different framework for structuring their findings. It would be chaos.

But with AI tools, we're somehow treating this fragmentation as acceptable, or even as empowering individual choice. It's not. It's creating silos, making peer review harder, and preventing teams from building on each other's work effectively.

The tools we use shape how we work together. When everyone is using different AI tools in different ways, we lose the ability to have shared practices, shared quality standards, and shared learning. We can't build on each other's approaches because we can't even see what others are doing.

## What Actually Works: The Ops Approach

The solution to all of these problems is straightforward, even if it's not simple. You need to treat AI tools like any other significant tool or process change in your organization. Stop making everyone fend for themselves.

Here's what that looks like in practice.

### Start with Process Analysis

Before you do anything else, your [ops team](https://www.nngroup.com/articles/research-ops-101/), or whoever is in charge of deciding what gets used, needs to **understand your current workflows and identify where AI could provide real value.** This means actually analyzing how work gets done, not just assuming that "AI would probably help with research synthesis" or "AI could speed up design critiques."

What are the bottlenecks in your current process? Where are people spending time on repetitive work that could be systematized? Where are junior team members struggling because they don't have access to senior expertise? Where is important knowledge getting lost or siloed?

Only after you understand the actual problems should you start thinking about AI as a potential solution. And you might discover that some problems don't need AI at all — they need better documentation, clearer processes, or different role structures.

### Design Specific Interventions

Once you've identified real problems, **design targeted interventions** rather than just turning everyone loose with the LLM of their choice.

For example, let's say your organization relies heavily on democratizing research: you have product managers and designers conducting lightweight [interviews](https://www.nngroup.com/articles/user-interviews/) even if they're not trained researchers. This can be valuable for moving quickly, but the quality is often inconsistent. Some people are natural interviewers, but others ask [leading questions](https://www.nngroup.com/articles/leading-questions/) or fail to probe interesting responses.

An AI intervention here might be a coaching tool that helps nonresearchers prepare for and conduct better interviews, but it needs to be systematic. You'd want to create standardized prompts that walk people through preparing an interview guide, practice scenarios where they can try out their questions and get feedback, and maybe even a post-interview reflection process. You'd pilot this with a small group, refine it based on their feedback, and then roll it out with training and support.

The key here is that you're not just saying "use AI to get better at interviewing." You're creating a structured process with specific tools and clear guidance.

Maybe your team spends a lot of time writing standard research documents like [research plans](https://www.nngroup.com/articles/pm-research-plan/), [discussion guides](https://www.nngroup.com/articles/interview-guide/), or [screeners](https://www.nngroup.com/articles/screening-participants/). These might have established formats in your organization, but people still waste time staring at blank pages or trying to remember what sections to include.

An AI tool that helps scaffold these documents could save time and improve consistency, but only if it's designed to work with your specific formats and terminology. You'd want official prompts or bots that incorporate your organization's standards, not just generic "write me a research plan" requests.

### Invest in Integrated Tools

Rather than having everyone cobble together their own AI workflows, invest in tools that have integrated AI capabilities thoughtfully and train your team to use them well.

For research, tools like Marvin, Dovetail, and UserTesting have built AI features specifically designed for research workflows. These tools understand research context, maintain security boundaries, and integrate with how research actually gets done. They're not perfect, but they're much better than expecting researchers to manually copy transcripts into ChatGPT and then copy the results back into wherever they're storing their work.

**The key is treating these tools like any other significant technology adoption.** That means:

- Evaluating options based on your specific needs, not just what's trendy
- Piloting with a small team before a full rollout
- Creating training materials and best practices
- Designating power users who can help others
- Establishing clear workflows for how these tools fit into your existing processes

### Create Clear Security and Privacy Policies

You need explicit, practical policies about what people can and cannot do with AI tools. Not a 50-page legal document, **but clear guidelines that help people make decisions in the moment.**

For example:

- "Never paste customer data that includes names, email addresses, or other PII into public AI tools."
- "If you need to analyze customer data with AI, use [specific tool], which has appropriate security controls."
- "When in doubt about whether information is sensitive, check with [specific person/team]."

These policies need to be paired with tools and processes that make compliance easy. If you tell people not to use public AI tools but don't provide alternatives, they'll use the public tools anyway. If you require security approvals for everything but make the approval process take two months, people will find workarounds.

The best security policies are ones that make the secure option the easiest option.

### Build a Prompt Repository

Create a shared space where people can contribute, browse, and remix useful prompts. This could be a Notion page, a wiki, or an intranet. The platform matters less than the practice.

Make this repository an active, curated resource rather than a dumping ground. You want:

- Clear categorization so people can find prompts relevant to their work
- Context about when and why to use specific prompts
- Comments or discussion space where people can share results and variations
- Regular updates to remove outdated approaches and highlight what's working

Think of this repository as similar to a [design system](https://www.nngroup.com/articles/design-systems-101/) or a pattern library. You're not just collecting every possible variation. You're curating the approaches that have proven valuable and making them easy for others to adopt and adapt.

Some teams have found success with regular "prompt show and tell" sessions where people share interesting approaches they've developed. Such sessions help socialize the repository and encourage contribution. But remember, this is in addition to the centralized space. Live, or even recorded, sessions can’t replace written documentation, because it’s too easy for people to forget the details.

### Pilot Before You Scale

When you're considering a new AI tool or approach, pilot it with a small team first. Let them actually use it for real work, encounter real problems, and develop real recommendations.

This is how you'd approach adopting any significant new tool. If you were considering switching from Sketch to Figma, you wouldn't make the entire design team switch overnight. You'd have a few teams try it, work out the migration process, develop best practices, and identify gotchas. Then you'd use that learning to make the broader rollout smoother.

The same principle applies to AI tools. A pilot team can:

- Test whether the tool solves the problems you think it solves
- Identify unexpected issues or limitations
- Develop training materials and best practices based on real usage
- Build internal champions who can help with broader adoption
- Give you concrete data about whether the investment is worthwhile

### Treat AI-Tool Rollout Like Any Other Tool Rollout

This might be the most important point: AI tools should be subject to the same rigor as any other organizational change. That means:

- **Have clear goals:** What specific problems are you trying to solve? How will you know if it's working?
- **Conduct a proper evaluation:** What tools are you considering and why? What are the tradeoffs? What are the security implications?
- **Design a structured rollout:** Who's using it first? What training and support do they need? How will you gather feedback?
- **Plan your change management**: How are you communicating about the change? How are you addressing concerns? How are you supporting people through the transition?
- **Establish success metrics:** What does success look like? How are you measuring impact? When will you evaluate whether to continue, adjust, or stop?

There are well-established practices for organizational-change management because dropping new tools on people's desks doesn't work. The fact that AI feels futuristic and exciting doesn't change these fundamentals.

## Stop Asking Everyone to Be a Pioneer

The current approach to AI adoption in most organizations is essentially asking everyone to be a solo pioneer. Figure out the tools, develop the processes, navigate the security implications, learn the best practices, all on your own time, and all while your performance might be evaluated on how well you do it.

**This is not just inefficient; it's unfair.** It puts an unreasonable burden on individual contributors who are just trying to do their jobs. It creates massive variance in outcomes based more on individual initiative than on actual value. And it misses the opportunity to develop organizational capabilities rather than just individual skills.

Research and design teams are particularly vulnerable to this problem because we're often seen as "creative" roles where individual variation is expected and even celebrated. But our work is fundamentally collaborative. We build on shared methods, shared tools, and shared knowledge. When we fragment those foundations by making everyone develop their own AI approaches, we undermine the collaboration that makes our work effective.

The good news is that **we already know how to solve this.** We've developed mature practices for rolling out new tools, establishing shared processes, and supporting teams through change. Now we need to apply them to AI instead of treating it as somehow special or different.

So, if you're in an ops role, or if you're a leader trying to figure out how to handle AI in your organization, here's the core message: stop expecting everyone to figure this out on their own. Do the hard work of understanding your processes, designing thoughtful interventions, providing good tools, and supporting your team through adoption.

If you're an individual contributor who's been told to "explore AI" without much support, know that you're not behind, you're not doing it wrong, and the chaos you're experiencing isn't your fault. The problem isn't that you haven't found the right prompt or the right tool yet. The problem is that you're being asked to solve an organizational problem by yourself.

AI tools have some potential to improve research and design work. But that potential will be realized only if we treat them seriously — which means treating them like the significant organizational changes they are, not like individual experiments everyone should run on their own.
