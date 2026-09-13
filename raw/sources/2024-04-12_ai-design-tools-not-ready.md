---
title: "AI UX-Design Tools Are Not Ready for Primetime: Status Update"
date: "2024-04-12"
url: "https://www.nngroup.com/articles/ai-design-tools-not-ready/"
author: "Caleb Sponheim, Megan Brown"
topics: [ai]
type: article
---

*For an updated article on the state of AI design tools, see AI Design Tools Are Marginally Better: Status Update .*

AI tools won’t be replacing UX designers any time soon. Currently available LLM-based tools are not shortcutting steps in the design process just yet.

## In This Article:

- [Our Study](#toc-our-study-1)
- [Designers Use AI, Just Not for Design](#toc-designers-use-ai-just-not-for-design-2)
- [Existing AI Tools for UX Design Are Lacking](#toc-existing-ai-tools-for-ux-design-are-lacking-3)
- [Examples of AI Tools for UX Design](#toc-examples-of-ai-tools-for-ux-design-4)
- [Advice for UX Designers Using AI](#toc-advice-for-ux-designers-using-ai-5)

## Our Study

There’s so much marketing hype around AI that it’s hard to know what tools and strategies can help UX *right now.*

To find specific, useful ways in which practitioners integrate AI into their work, we conducted in-depth interviews in early 2024 with UX practitioners (researchers, designers, and managers).

We asked our participants to describe and show us how they currently use AI in their work. We focused on the uses of generative AI and of other tools branded as AI for the study. Our study participants were early adopters, were big proponents of AI, and had been using a variety of AI tools in their work for a while.

**Among the practitioners we spoke with, UX designers were most limited in their use of AI in their work.** While many AI-based design products exist, we did not identify any design-specific AI tools in active use by UX designers — or any that our participants would recommend to others.

## Designers Use AI, Just Not for Design

UX designers actively engaged with text-based AI tools such as ChatGPT for brainstorming and ideation tasks, but **we found zero design-specific AI tools in serious use by the professional UX designers we spoke with**.

AI tools are capable of filling skill gaps, allowing practitioners to continue their work without needing to engage with a specialized team member or stakeholder. For example, a UX designer may turn to a text-based AI tool to generate UX copy for a prototype instead of reaching out to a copywriter and waiting for a response.

AI tools are also helpful as a brainstorming partner, providing suggestions for feature names, research approaches, or anything else that doesn’t require absolute precision or trust. We found that UX designers turn to AI for many nondesign tasks: writing emails, structuring communication, organizing and breaking down difficult tasks into manageable pieces.

## Existing AI Tools for UX Design Are Lacking

We combined our findings from interviews with UX designers with our own evaluations of current AI-based UX-design tools. Our evaluation agreed with the impressions of the UX practitioners we interviewed: existing AI tools that are advertised for design are lacking, and the vast majority are not ready to be used in design workflows.

The UX designers we spoke with said they **were not actively using design-specific AI tools** (such as Figma Plugins). Our expert review of popular plugins and AI tools (examples included below) also found that they didn’t add much value to the design process.

Issues around these new tools often became magnified when deployed across medium-to-large scale organizations. One participant was particularly disappointed by the lack of customer support and guidance for use when he attempted to set up his agency in Midjourney. He also worried about ethical and legal risk if his team used AI-generated content in designs, due to potential copyright issues.

“There are folks over the past few decades have generated content that these tools are piggybacking on. Is it right to use that without attribution without licensing and royalty fees? We're thinking about the ethical use of it.”

Right now, AI tools, especially in the context of UX design, **are a solution in search of a problem.** There are many problems and points of friction that cause UX designers to be inefficient and unproductive in their work, but working to develop solutions to those problems wouldn’t necessarily lead you to AI.

AI developers hope to insert AI into the design process, applying it to existing design challenges and inefficiencies. But, for a tool to be useful enough to integrate into a workflow consistently, the interaction with that tool must be consistent.

Unfortunately, AI-based tools are not deterministic at this point. For example, a single ChatGPT 4 prompt for an example of front-end design featuring Google’s Material Design components resulted in three drastically different designs. While this variety in output is valuable for ideation, it isn’t so helpful for the end-to-end, replicable AI-powered design solutions that some products promise.

![three separate screenshots showing basic HTML implementations of material design. all three designs are different.](https://media.nngroup.com/media/editor/2024/04/12/material_design_screenshots.png)

*Screenshots from three html files generated by ChatGPT 4, from the same prompt, repeated three times*

It remains to be seen whether AI’s opaque and unreliable nature is an inherent characteristic of the technology or could be overcome with future products. Current AI chatbots based on large language models are probabilistic, relying on a statistical dice roll to determine the sequence of words that make up the response to a prompt.

The current state of AI tools, text-based or otherwise, presents an inconsistent, unreliable, and low-value attempt to solve existing design problems. As prompt engineering, community knowledge, and implementation of AI tools progresses, **we may see an improvement in the control and precision** that these tools allow, potentially crossing the threshold in reliability and trustworthiness for professional workflows.

## Examples of AI Tools for UX Design

In our assessment of various AI-based tools for design, we found that most produced basic results that don't add much value to the design process in their current states.

Below we discuss three such tools. These were frequently mentioned by our study participants or in design communities.

### Wireframe Designer: A Figma Plugin

**AI-based wireframing tools** often generated generic layouts that weren’t helpful or creative even with very specific prompts.

The free version of the Figma plugin [Wireframe Designer](https://www.figma.com/community/plugin/1228969298040149016/wireframe-designer) by Chenmu Wu generates low-fidelity wireframes when the design needs and context are met. To test the limits of this tool, we generated screens using a variety of prompts varying in length and detail.

We noted that, even when ample contextual information was provided about design needs and target users, the plugin generated generic, seemingly templatized outputs.

Even when we tried a variety of prompts corresponding to different contexts and business needs, the generated outputs were fairly similar, with the main difference being the placeholder text pulled from the prompt. The Wireframe Designer plugin also didn’t offer a straightforward method for generating several variations from a single prompt, making it harder to get a variety of ideas.

![Two low fidelity wireframes generated by the Wireframe Designer plugin. The left wireframe was generated for the prompt "Prompt 1: A sneaker retailer selling shoes to sneaker enthusiasts." The right wireframe was generated for the prompt "A homepage for a make-up e-commerce website selling the latests make-up brands and trends"](https://media.nngroup.com/media/editor/2024/04/11/wireframer-variations.jpg)

*Low-fidelity screens generated for different prompts using the Wireframe Designer Figma plugin*

### Uizard: An AI-Assisted Design Tool

[Uizard](https://uizard.io/) is an [AI-assisted design tool](https://www.nngroup.com/articles/generative-ui/) that integrates AI wireframing, image generation, theme generation, and UI-copy assistance.

Unlike the Wireframe Designer plugin, Uizard requires text prompts to be 300 characters or less. While still basic in its output, Uizard’s screen generator offered more variety and options in comparison to the Wireframe Designer Figma plugin.

When using Uizard’s *Autodesigner*, the generated screens aligned better with our prompts than those created by the Wireframe Designer. However, the AI-based outputs still varied significantly in quality. Even though Uizard seemed more promising as an AI-assisted prototyping-and-design application, its interface was clunkier than that of more-popular design tools like Figma.

*Based on a single prompt, UIzard’s screen generator created 5 low-fidelity options to choose from, with the option to regenerate results.*

### UX Pilot: AI-Driven Toolkit

[UX Pilot](https://uxpilot.ai/a) is a subscription-based, AI-driven toolkit designed to help designers create color schemes, wireframes, and questions for user and stakeholder interviews, as well as plan and analyze workshops.

WHile this toolkit shows some promise for aiding in UX research, it is less helpful for design-specific tasks. For instance, its *Color & Gradient AI* Figma plugin generated color schemes that didn’t work well together for interface design.

*Out of the three color palettes generated with UX Pilot's Figma plugin, the top palette is the most usable as a starting point, but the other two results require significant adjustments.*

This plugin was good for ideating color schemes quickly, but it did require that the designer understand some color theory when narrowing down color choices.

## Advice for UX Designers Using AI

While our study did not yield specific tool recommendations for designers, it did generate plenty of good advice for UX designers trying to navigate emerging AI tools.

**Familiarize yourself with the potential benefits of AI for ideation, brainstorming, and copywriting tasks.** Artificial-intelligence tools are currently most effective with text-related tasks and, with effective prompts, can serve as beneficial partners in ideation and brainstorming exercises. UX writing and copywriting are also strong opportunities for AI to streamline work.

**Lean on existing methods for design tasks.** Current AI offerings cannot meaningfully enhance those visual and design-heavy workflows. Currently, the work necessary to get a high-quality result from an AI design tool is too time-consuming to justify its use. Stick to tried and true methods for visual design, wireframing, and prototyping.

**Do not use AI to generate user data, user-research findings, or user personas.** Using AI to generate artificial research data is unethical, deceitful, and potentially harmful to a final product and your professional reputation.

**Don’t panic about missing the boat on AI.** Developers and companies are still figuring out whether AI can meaningfully improve the experience of being a UX designer, and there aren’t any “killer apps” right now. Take time to play and tinker with AI tools to stay current, but don’t expect them to return much value at the moment.
