---
title: "The Methodological Problems Hiding in Your Research Tools"
date: "2026-03-13"
url: "https://www.nngroup.com/articles/research-tool-problems/"
author: "Maria Rosala"
topics: [research-methods]
type: article
---

Many user-research platforms have been around for over a decade; some close to two decades. And yet, one thing is apparent to most experienced researchers: many of these tools were not built by expert researchers or with sufficient input from them. At Nielsen Norman Group, we’ve lamented this for years.

For most of the history of UX research tools, the worst thing a poorly designed platform could do was slow you down or send you looking for a workaround. That's changed. **We're now in an era where research tools don't just host your study — they plan it, moderate it, and analyze it for you.** If those tools lack a solid foundation in research methodology, the risk is greater than simple inconvenience — it's flawed research presented with confidence on a large scale.

## In This Article:

- [A Quick History of UX Research Tools](#toc-a-quick-history-of-ux-research-tools-1)
- [Methodological Faux Pas in Research Tools](#toc-methodological-faux-pas-in-research-tools-2)
- [UX Research Tools Have Changed the Research Profession](#toc-ux-research-tools-have-changed-the-research-profession-3)
- [In the Age of AI, the Stakes of Poorly Designed Research Tools Are Higher](#toc-in-the-age-of-ai-the-stakes-of-poorly-designed-research-tools-are-higher-4)
- [Takeaways](#toc-takeaways-5)
- [Summary](#toc-summary-6)

## A Quick History of UX Research Tools

Before diving in, it helps to understand the landscape of tools we're talking about and where AI fits into it.

If you've been in this field long enough, you'll remember when there was no dedicated UX research software at all. Analysis happened in spreadsheets, notes were taken on physical sticky notes, and remote research was cobbled together with tools like Skype and GoToMeeting — software that was buggy, limited, and certainly not designed for research. None of it was browser-based; participants and researchers alike had to download and install software just to get started. Seeing both a participant's screen and their face at the same time was also a luxury. In-person, lab-based research was the norm.

![A digital voice recorder](https://media.nngroup.com/media/editor/2026/03/03/digital-voice-recorder.jpg)

*A digital voice recorder: a research tool I used at the beginning of my career.*

### Mid-2000s: The Rise of Unmoderated-Research Platforms

As an alternative to expensive lab-based research, research platforms (such as UserTesting, Userlytics, and UserZoom) emerged in the mid-2000s and introduced a new form of usability research: [unmoderated testing](https://www.nngroup.com/articles/unmoderated-usability-testing/). Participants could complete tasks on their own, in their own environment, and without a moderator present.

![A screenshot from an unmoderated test on mobile in User Testing. The opening task instruction is visible as a popover on the screen. The user has nngroup.com loaded on their mobile device.](https://media.nngroup.com/media/editor/2026/03/04/user-testing-test.png)

*An example of an unmoderated test in UserTesting*

Some of these platforms expanded their repertoire of study formats to include [card sorting](https://www.nngroup.com/articles/card-sorting-definition/), [tree testing](https://www.nngroup.com/articles/tree-testing/), [surveys](https://www.nngroup.com/articles/should-you-run-a-survey/), and even [moderated research](https://www.nngroup.com/articles/moderated-remote-usability-test-why/).

### Mid-2010s: The Emergence of Analysis and Repository Tools

The mid-2010s brought a second wave: analysis and [repository](https://www.nngroup.com/articles/research-repositories/) tools. Researchers had long struggled with the messiness of qualitative analysis. Insights were often buried and lost in spreadsheets, hand-written notes, transcripts, or video recordings. Qualitative-analysis software existed, but it was desktop-based, clunky, and not designed for collaborative teams. A new generation of SaaS tools — Dovetail, Aurelius, EnjoyHQ — changed that. They offered AI transcription, video uploads, collaborative tagging, and cloud-based storage.

![Screenshot of Dovetail an analysis tool. A transcript and video is visible. To the right are tags that have been applied to the transcript.](https://media.nngroup.com/media/editor/2026/03/04/dovetail-tagging.jpg)

*An example of a transcript generated from a recording that has been tagged*

Towards the end of the decade, "full-stack" research platforms (like Great Question) began to emerge, giving researchers more capabilities, such as [internal panel](https://www.nngroup.com/articles/user-panels-101/) features, scheduling tools, and the ability to observe moderated research.

### 2020s: The Advent of AI-Powered Research Tools

Then came ChatGPT, and with it, a mushrooming of new research tools, many of which promise to revolutionize research by standing in for human researchers. These tools:

- **Simulate users**, providing you with interview transcripts or survey responses from AI-generated people (i.e., [synthetic users](https://www.nngroup.com/articles/synthetic-users/))
- **Use AI to moderate research** (such as [AI interviewers](https://www.nngroup.com/articles/ai-interviewers/) and usability-test moderators)
- **Have “AI agents” that can help you plan research**, analyze research data, or report research findings

Many of these tools are in their infancy and are quickly improving their capabilities and performance. **While there are valid use cases for AI in research , we don’t recommend replacing all traditional research methods and approaches with AI agents, tools, or features.**

In addition to new competitors entering the market, existing research tools are updating their feature sets to include AI where possible. We’ll likely see some of the more successful AI tools be absorbed or acquired by larger UX-research tools.

## Methodological Faux Pas in Research Tools

Companies that develop UX research tools face the same problems as other organizations, such as being driven by product- and engineering priorities and a lack of a research culture. Moreover, many founders come from business, marketing, and product backgrounds, rather than UX research. Despite the enormous value these tools have brought to the field, **many have made significant methodological mistakes over the years**— some subtle, some glaring. We could cite many examples of methodological faux pas, but three are enough to make the point.

### Quantitative Features Missing the Basics

Many research tools don't offer the essential features required for the research methods they advertise. Even UserTesting.com, which has been around for nearly 20 years and has acquired many competitors along the way, still lacks key features needed for proper quantitative usability testing. The platform offers two options for remote, unmoderated tests: *think-out-loud* tests for qualitative usability testing and *interaction**tests*, supposedly designed for quantitative testing. But the interaction test is missing features that are fundamental to the method:

- **Single success URL**: While it does offer a success URL, it allows you to add only one. This is a problem because participants can often complete a task or find the right information on multiple pages on a site. Limiting success to a single URL risks incorrectly marking successful completions as failures.
- **Lack of task-randomization support**: Task randomization is essential for controlling order effects in quantitative studies — a basic requirement, not an advanced one.

![When creating an unmoderated test in user testing, there are two options: "Think-out-loud test" to "gather rich verbal feedback" and "Interaction test" to "record user interactions at scale without verbal feedback"](https://media.nngroup.com/media/editor/2026/03/04/user-testing-unmoderated-test-options.png)

*UserTesting offers two types of unmoderated usability tests: think-out-loud tests and interaction test. Sadly, the interaction test doesn't have the right features to support quantitative usability testing.*

UserTesting isn't alone in this. We found it genuinely difficult to identify tools with the right features for quantitative usability testing and usability benchmarking. (If you’re looking for one, we recommend [UX Tweak](https://www.uxtweak.com/), which has the necessary features.)

![UX Tweak's Interface has options to add as many success URLs as needed and options to randomize all tasks or all tasks apart from the first and last ones.](https://media.nngroup.com/media/editor/2026/03/04/ux-tweak-quant-features.png)

*UX Tweak offers the necessary features for quantitative usability testing: randomization and multiple success URLs.*

### Analysis Tools that Miss Behavior

Dovetail was an early leader in the UX-research-analysis space, and it was a genuine improvement on clunky, unintuitive academic software like NVivo. But it lacked the ability to tag video content directly – researchers could tag only text, such as transcripts or imported notes. In usability research, where critical moments often occur without accompanying verbal commentary, this is a serious limitation. As a result, researchers must devise workarounds, tagging transcript text that roughly corresponds to important video moments. This is tricky if the participant is silent or their words don’t match their actions. And if a video has no transcript at all, it cannot be clipped or tagged at all.

In contrast, Marvin does support adding notes and tags directly to the video, even if the participant is silent during that moment. (This is a common participant behavior, by the way. Participants are often not narrating their behavior while they do interesting things. That’s a major reason why AI research-analysis tools that claim to analyze usability testing from transcripts alone are selling you snake oil.)

![A screenshot of a video in Marvin. A user is adding a timestamped note to the recording.](https://media.nngroup.com/media/editor/2026/03/04/marvin-adding-notes.jpg)

*Marvin provides the option to add time-stamped notes and tags directly to the video, a much-needed feature for usability research that is not available in Dovetail.*

The inability to add time-stamped notes or tags directly to video in Dovetail points to a fundamental misunderstanding of how usability research is analyzed.

### Tools that Blur Evaluative and Exploratory Research

Perhaps the most consequential faux pas has been the blurring of research methods. **A persistent and damaging confusion in the field is mixing up user interviews and usability tests — two distinct methods with fundamentally different goals.** Interviews are used to understand people's experiences and perspectives. Usability tests evaluate the performance of a design. Conflating the two leads to research that does neither well.

Several tools have made this confusion worse. Many refer to usability tests as "interviews" in their interface.

![Marvin has a repository of templates. There are templates for feedback interviews and usability test. The text at the top of the page reads "Create new guides for different kinds of interviews which need different scripts."](https://media.nngroup.com/media/editor/2026/03/04/marvin-discussionguide-templates.png)

*Marvin refers to all research plans as discussion guides. The design seems to imply a usability test is a type of interview, which it isn’t.*

Even the recruiting giant [User Interviews](https://www.userinterviews.com/) has contributed to this confusion through its name alone. For years, attendees would sign up for our [User Interviews training course](https://www.nngroup.com/courses/user-interviews/), expecting to learn how to facilitate a usability test. (They still do, sometimes.)

The consequences are real. This conflation has led to the mistaken belief that UX research is just "talking to customers," resulting in research that blends the two methods in unproductive ways — for example, asking participants to review and react to a design instead of interacting with it.

One thing is clear: **many builders of UX research tools don’t understand research best practices for the methods supported by their software**.

## UX Research Tools Have Changed the Research Profession

**UX research tools have done more than host studies — they've shaped how entire generations have learned to conduct research.** Some platforms offer certifications or discounted educational licenses, making them the first exposure many students have to the field. It's perfectly rational to assume that a tool designed for research reflects how research should be done. That assumption is often wrong.

**The problem is compounded by the guidance these platforms provide.** With large marketing budgets and a commercial interest in making research look accessible, many tools produce blogs, field guides, and templates written by content marketers instead of researchers. There's an obvious commercial incentive to depict research as simple and accessible.

That commercial logic has also driven a shift in these tools’ target audience. Many platforms now market themselves not to researchers, but to broader product and business teams. This is part of a broader trend known as the [democratization of research](https://www.nngroup.com/articles/democratize-user-research/). For example, Dovetail’s marketing messaging has recently shifted away from research, and more towards “customer insights” (a growing job title).

![The homepage for Dovetail reads, "Dovetail turns your customer feedback into agents, dashboards, and reports that drive your roadmap, revenue, and results."](https://media.nngroup.com/media/editor/2026/03/04/dovetail-homepage.jpg)

*Dovetail is now marketing its product as a platform for making sense of customer feedback, with a heavy emphasis on automation and AI.*

Enterprise packages allow thousands of employees to access insights, interrogate data, and even conduct their own research. The result is a growing population of users who may not recognize when a tool does not support good research — and who are unprepared to challenge its shortcomings.

## In the Age of AI, the Stakes of Poorly Designed Research Tools Are Higher

Today, research tools not only host your research, but also plan, moderate, and analyze research studies for you. Setting up a research study in a research platform used to require careful preparation and thought, but now anyone using AI-powered research tools can launch a study with just a few prompts and clicks.

The problem is that these new AI-based research tools are engineered by people who, in many cases, don't have sufficient understanding of research best practices. And the stakes are so much higher.

For example, TheySaid, a research platform that uses AI to help design and conduct studies, asks for your research goals when setting up a new study for you. In the example below, I’ve shared a research goal we had for testing the Nielsen Norman Group website. We wanted to learn whether people understand what we offer and how easily they can find a course on a particular topic, whether it’s a live online course or a self-paced one.

![TheySaid Platform asks for goals for a project. The following goals have been added: "How well can potential customers understand what we offer?" "How easily can they find a course on a particular topic, whether it's a live online course or a self-paced one?"](https://media.nngroup.com/media/editor/2026/03/04/theysaid-research-goals.jpg)

*TheySaid is a research platform that uses AI to help you design and conduct studies.*

TheySaid generated a draft plan that I could amend. Unfortunately, the task [primes](https://www.nngroup.com/articles/priming/) participants to behave unrealistically.

> **Leading task created by TheySaid:**
> 
> 
> 
> *Imagine you are interested in improving your skills in 'Information Architecture'. Try to find a course on this specific topic. Pay close attention to whether the available courses are live online or self-paced*.

*TheySaid uses AI to generate tasks and questions for an AI-moderated usability test. Unfortunately, what it produces is often of poor quality.*

The task included the instruction to pay attention to the course format and used the exact terminology from the NNGroup.com site. This wording makes users aware of the two course types and primes them to consider both in their search. Without this instruction, users may not have thought of looking for both formats. This instruction thus encourages unrealistic behavior and undermines the study goal.

This is not an issue unique to this platform. We’ve witnessed many poor tasks and interview questions generated by AI across these tools. Userology, another tool that offers AI-moderated usability tests, also has an AI-assisted study planner. It also produced leading tasks and far too many interview questions that would bore a participant to tears.

Here’s an example of a task Userology created for us.

> **Leading task created by Userology**:
> 
> 
> 
> *Imagine you have a $40k+ budget to improve your team's UX maturity. Navigate to 'Consulting'. 1) Identify the difference between 'In-House' and 'Intensives'. 2) Compare the maturity assessment tiers. 3) Before booking, find information about the specific people/team to assess credibility. 4) Find how to inquire.*

This task tells users exactly where to go and what steps to take — exactly the opposite of what usability test tasks should do! The results of tests like this would be unhelpful and untrustworthy.

*Userology has a built-in assistant who creates a usability-test plan for you. However, the interview questions and tasks it generates are leading (as shown above). Also, the resulting test plan is referred to as an Interview plan.*

While I could easily catch these mistakes and rectify them, it becomes harder to do when they are baked into the AI assistants’ behavior or in elements of the study design that can’t be customized — like instructions that encourage unmoderated-testing [participants to be overly verbal or opinionated](https://www.nngroup.com/articles/problem-participants-remote-unmoderated/).

**Additionally, even though I was able to catch these mistakes, many novices and nonresearchers won’t.** The results will be flawed research plans, usability-testing tasks that prime participants, interview guides with leading questions, and AI facilitators who don't know how to moderate a usability test well.

## Takeaways

If you're a **research-tool creator**: consult expert UX researchers and involve them in the design of your tools — not as an afterthought, but as a core part of your process.

If you're a **junior UX professional**, don't assume that the way a tool has been designed reflects best study-design practices. Seek out independent learning resources rather than relying solely on the guidance platforms provide.

If you're a **ResearchOps professional** procuring new tooling, ask vendors about their AI features: how they’re designed, what they’re trained on, and how much control researchers have over their behavior. Don't rely on vendor demos alone — these tend to showcase simple studies that rarely expose how tools perform in more complex or nuanced research scenarios. Pilot tools with trained researchers using real studies before wider rollout and set up guardrails to prevent teams without research expertise from producing flawed work without realizing it.

## Summary

UX research tools have reshaped how the field works — sometimes for the better, sometimes not. Research is a craft that requires expertise, and that expertise needs to be at the heart of how these tools are designed. As AI plays a larger role in the research process, the stakes are too high to leave tool design to people who don't fully understand the methods they support. The good news is that this is a solvable problem if the right people are involved. The tools shaping research need to be shaped by researchers.
