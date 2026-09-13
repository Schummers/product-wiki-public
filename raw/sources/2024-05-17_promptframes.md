---
title: "Promptframes: Evolving the Wireframe for the Age of AI"
date: "2024-05-17"
url: "https://www.nngroup.com/articles/promptframes/"
author: "Evan Sunwall"
topics: [ai, prototyping]
type: article
---

## In This Article:

- [The Need for Quality Placeholder Content](#toc-the-need-for-quality-placeholder-content-1)
- [Introducing Promptframes](#toc-introducing-promptframes-2)
- [Benefits of Using Promptframes](#toc-benefits-of-using-promptframes-3)
- [How to Use Promptframes in the Design Process](#toc-how-to-use-promptframes-in-the-design-process-4)
- [The Potential of Promptframes](#toc-the-potential-of-promptframes-5)
- [A Few Precautions to Consider](#toc-a-few-precautions-to-consider-6)
- [A Good Tactic for the 1-Person UX Team](#toc-a-good-tactic-for-the-1-person-ux-team-7)

## The Need for Quality Placeholder Content

Using placeholder text or images early in your design workflow can help you explore possibilities and cope with evolving requirements.

However, placeholder content (especially the notorious lorem ipsum) can be a barrier to gathering insightful feedback from users and stakeholders. I have personally experienced derailed [usability testing](https://www.nngroup.com/articles/usability-testing-101/) sessions because my placeholders provoked unintentional confusion and doubt in my participants. (And folks like Anna Kaley have previously highlighted the benefits of taking a [content-focused approach](https://www.nngroup.com/videos/content-frames/) in early design work.) In UX, remember that **the content inspires feedback**, **not the container**.

To enable a more efficient feedback loop, **I propose a new design deliverable: the promptframe**. Use promptframes to create realistic placeholder content faster using AI.

## Introducing Promptframes

Promptframes unite the classic UX wireframe with prompt writing for generative AI.

> A **promptframe** is a design deliverable that documents content goals and requirements for generative-AI prompts **** based on a wireframe’s layout and functionality.

Promptframes organize and document prompts locationally within an existing wireframe. UX designers can create promptframes early in the design process as they begin crafting interfaces to address requirements. Promptframes describe the goals, purpose, requirements, and other details of the content that goes within various design elements, so that AI can readily assist with content ideation and generation.

![Diagram illustrating the stages of UX design from sketch to prototype. The stages include Sketch, Wireframe, Promptframe, and Prototype, arranged along a project timeline. The Promptframe stage is annotated with AI prompt documentation notes.](https://media.nngroup.com/media/editor/2024/05/16/graphic_promptframes.jpg)

*Creating promptframes is a step in the design process that comes between wireframes and more-detailed prototypes. It involves crafting and documenting AI prompts to rapidly generate and refine meaningful content to populate different areas of the candidate design. It serves to create realistic prototypes that collaborators and users can evaluate.*

## Benefits of Using Promptframes

Wireframes can sometimes create problems for UX designers:

- **Reduced ideation**. When designers rush ahead to make prototypes with high visual and interactive fidelity, they may spend less time exploring content. Most ideas are poor, and it's usually through evaluating many ideas (or combining several mediocre) that good designs emerge.
- **Obscured requirements**. Allowing placeholders to linger within designs can hurt the UX designer in the long run. Unknown requirements or technical constraints that the UX designer discovers too late may result in infeasible or misaligned designs that cannot be easily corrected in due time.
- **Diminished feedback.** Designs with poor content fidelity are too abstract for users to understand. For example, a data-intensive app with nonsensical charts and tables will be incomprehensible to a data-analyst accustomed to evaluating realistic data. Users may ignore these areas or ask questions about them in testing, consuming precious session time on what you (mistakenly) felt were unimportant details.

Promptframes address these issues in several ways:

- **Efficient ideation**. One of the superpowers of generative AI is providing multiple variations of an idea with minimal effort. Promptframes integrate this idea engine into the UX design workflow.
- **Improved content fidelity**. Specific, focused AI prompts can result in helpful content that, while not necessarily ideal for release, may be good enough for user testing and gathering feedback.
- **Faster iteration**. Writing prompts may initially require some upfront effort, but that effort is repaid with the ease of incorporating insights from testing and feedback. Content can be pivoted and improved rapidly by sharing those details in subsequent prompts.
- **Better collaboration**. Visuals are a great help when collaborating, as they build [common ground](https://www.nngroup.com/articles/common-ground/) with your team. Yet squiggly lines and lorem ipsum are often too abstract for nondesigners. AI-generated content, as well as the prompts generating it, can stimulate dialog and feedback from colleagues and may surface obscure requirements earlier in the design process.
- **Greater focus on objectives**. Promptframes ask UX designers to go beyond interface components and describe business and user goals. If the UX designer struggles to explain these goals to a generative AI tool, it calls into question the content's purpose.

## How to Use Promptframes in the Design Process

Conduct your early-stage UX design process normally using [sketches and simple wireframes](https://www.nngroup.com/articles/draw-wireframe-even-if-you-cant-draw/). This work will serve as the foundation for your promptframes once it is digitized in your design tool.

To illustrate promptframes in the design process, we will use hypothetical examples based on a [page from Blue Apron's website](https://cook.blueapron.com/heroes/) describing a special promotional offer for people in community-service roles.

![Diagram outlining the initial steps in a project. Step 1 (Establish Context & Describe Users) includes elements like user profiles and context notes. Step 2 (Write & Document AI Prompts) shows objectives, desired outcomes, and examples. The steps are connected with an arrow indicating the progression.](https://media.nngroup.com/media/editor/2024/05/16/graphic_laying-groundwork.jpg)

### 1. Establish Context and Describe Users

Documenting and sharing context with the generative AI will improve its ability to assist with content creation. ChatGPT is particularly well suited for promptframes due to its support for various output types.

Consider including these important high-level details in your prompts.

Category | Details | Example | Role | The role(s) that the generative AI will play (e.g., content strategist, graphic designer, video producer, data analyst), and the type of content it must create | As an expert Content Strategist, you will generate engaging website copy… | Organization | The organization's mission and how it serves its customers and clients | You work for Blue Apron, a company aiming to make tasty home cooking accessible to everyone… | Objectives | The crossfunctional goals of the experience and what success looks like for the project (e.g., persuading visitors to sign up for a service, successfully scheduling a sales consultation, completing a workflow quickly and confidently) | In general, Blue Apron wants user experiences that increase meal kit subscription sign-up rates, improve customer retention and satisfaction, and streamline the meal selection and checkout process… | Tone of voice | The | tone of voice | that should be used in all generated copy to align with the brand (reuse any tone of voice documentation from marketing or design-system resources if they exist.) | Your copy should inspire confidence in the kitchen, emphasizing simplicity, nutrition, and culinary delight… | Definitions | A glossary of unique terms your organization uses, including its products and services or competitors' names | Mealkit: a collection of pre-measured ingredients with recipes shipped to the customer’s home… | Visual principles | Documented stylistic guidance for any visual assets (e.g., a design system like | Shopify Polaris design system | to describe desirable illustrations' color, shape, lines, and other aspects) | Visuals should use vibrant colors that reflect fresh and healthy ingredients… | Variations | The number of divergent variations for all AI output (you will usually want 3–5 variations) (Variations are a crucial advantage of using generative AI, regardless of the generated content, but some AI tools may generate only few, if any, variations to manage their operating costs.) | For each request, you must generate 2-3 divergent variations of outputs, whether textual, visual, or data-driven…

Generative AI also needs **user insights** to be effective. Share written content from high-quality [personas or archetypes](https://www.nngroup.com/articles/personas-archetypes/) that mention user needs, behaviors, goals, pain points, as well as motivations for the product, service, or feature being designed.

All this specificity will give you better results than just using off-the-shelf AI agents that proclaim to fulfill similar content-generation roles. Although this looks like a lot of effort to write or compile, you need to do this only once and can reuse them throughout this project or others.

![A text-based image discussing the meal preparation habits of community service workers, highlighting the need for quick and varied meals. Two highlighted quotes from participants emphasize the challenges of finding time to eat during long shifts and the importance of meal variety.](https://media.nngroup.com/media/editor/2024/05/28/graphic_report-slide-2-2.jpg)

*Upload presentation or report files containing insights from interviews to quickly provide additional user context. In this hypothetical example, community service workers were interviewed about their needs during mealtime. The AI tool can incorporate the text into its knowledge base to tailor its generated content.*

Remember to leverage AI-tool features that maintain this context. For example, ChatGPT offers a custom *-* GPT feature that conveniently persists these details. Other AI tools like Gemini or Claude currently don’t support easy reuse of context; for those tools, you will need to capture these details (perhaps in a text document) and feed them into your prompt before discussing project specifics.

*ChatGPT’s custom**GPT feature allows you to define and reuse context across many chats. Upload existing user deliverables, such as the Community Service Hero archetype file shown here, to provide the AI with helpful context for generating future content ideas.*

### 2. Write and Document Prompts

With the context and users established with our AI tool, the next step is to document prompts that will direct the AI in content creation. Start by writing down the purpose of the various areas and elements in your design that will contain content.

Always include these details in your prompts:

- **Objectives**: Why is this piece of content present in the design? How does it benefit the business and the users? [User stories](https://www.nngroup.com/articles/ux-user-stories/) and other requirements from a [product-manager colleague](https://www.nngroup.com/articles/product-manager-archetype/) can be an excellent reference here.
- **Desired outcomes**: What do you hope users will do or think because of this content?
- **Examples**: If available, include examples that could serve as inspiration when generating the content.

Here are **additional aspects** to consider for specific types of content:

#### Copy

- **Message**: What core message are you trying to convey in this copy? What facts and details must be included?
- **Container**: Where will the copy be seen (landing page, call-to-action button, error message, etc.)?
- **Constraints**: Are there word-count limits or other limitations required by the container?
- **Tone of voice (conditional)**: Should the default tone of voice be adjusted for this copy? For example, softening a typically humorous tone of voice for an error message likely to disappoint the user.

#### Images

- **Subject**: Who or what elements should be depicted in the image?
- **Actions**: Are any actions happening with the subjects in the image?
- **Background**: Is the background relevant, or should it be plain for easy removal?
- **Dimensions**: What size should the image be to fit the interface? For example, if real images will be coming from another system, then this would be an excellent opportunity to start asking colleagues about expected dimensions of those real images and documenting that constraint in the prompt.
- **Style**: How should the image be presented? What illustrative techniques are being used, or should it be a photo?

Some generative AI systems are capable of photorealistic content, but some vendors prohibit its creation as a precaution against abuse and misinformation. Don't waste time trying to work around these prohibitions if your current AI tool won't comply. You may need to use a different AI tool or settle for less than true-to-life images.

**A promptframe example:***Instead of empty boxes or lorem ipsum, promptframes contextually describe the objectives and requirements in planned content areas. These are used with an AI tool to create content to populate the wireframe. (Note that the promptframe does not replace the wireframe; rather, it is a separate deliverable that documents and supports the process of populating the wireframe with realistic content.)*

#### Data Visualizations

- **Type**: Describe the specific visualization desired, such as a bar chart, line chart, or table.
- **Data and outliers**: Provide a spreadsheet of data or request AI to create synthetic data to illustrate a desirable visualization. For example, instead of handcrafting data, just describe that a specific product line should trend downward over time on a line chart if a downward trend would support a task in future usability testing.
- **Columns and totals**: Where applicable, describe table-column labels, desired totals, and reasonable upper and lower values. Again, consider what might be helpful to represent in future usability-testing tasks.
- **Sorting**: For tables, describe any default sorting of the data.
- **Axes**: Describe the components of chart axes, such as minimum and maximum values, data type, and label formatting.
- **Style**: Provide a color palette for charting elements, if relevant.
- **Background**: Describe the background fill and any usage of reference lines.
- **Legend**: Describe the content and placement of a legend, if relevant and desired.
- **Labels**: Consider data labels for specific data points or the label of the overall chart.
- **Dimensions**: For charts, describe what size and image format should be used.

![Diagram showing the iterative process from prompt to prototype. It includes three steps: Step 3 (Run Prompts in AI Tools & Populate Prototypes), Step 4 (Refine Through Collaboration & Testing), and Step 5 (Revise Promptframes from Insights), with arrows indicating iteration between steps.](https://media.nngroup.com/media/editor/2024/05/16/graphic_prompt-to-prototype.jpg)

### 3. Run Prompts in AI Tool and Populate Your Designs with Content

Copy and paste the prompts into your AI tool. Then integrate the generated content in the wireframe to start evolving it into a prototype. To keep your work organized, document links to separate AI-tool chats in the promptframe, as you will likely revisit them in future revisions.

When performing this step:

- **Guard against perfectionism**. Don’t be tempted to create production-ready content. You can inadvertently waste a lot of time trying to refine the AI tool’s output to be “just right” for only marginal improvements.
- **Chunk your prompts**. AI tools have token limits for prompts and the AI tool’s input and resulting output. For ChatGPT, that limit currently translates to about 2,000-2,500 words. You still need detailed prompts to be successful, though, so break very long prompts into chunks and run them separately so the AI tool can still provide a detailed response.

*Leverage design tools’ existing documentation features or repurpose documentation plugins (such as Gist for Figma shown here) to capture prompts in late-stage designs without disrupting their layout.*

### 4. Refine Through Collaboration and Testing

As you conduct [design critiques](https://www.nngroup.com/articles/design-critiques/) with your collaborators, review the AI-generated content or the prompts that were used. Parts may be added, revised, or dropped — which is normal — but you should always be progressing towards greater content fidelity in all aspects of the design.

Think of the AI-generated content as a provocation for your colleagues — is this content aligned with our project and user's goals? Why or why not? Capture that feedback by revising the prompts. If there's considerable disagreement, consider splitting the design into 2 prototypes for testing.

*Although the copy is verbose, the icons rough, and the salmon overcooked, this AI-generated content could be valuable in discussions with colleagues and in user testing. The content can be rapidly pivoted based on feedback due to the well-documented prompts and chat threads in the promptframe.*

Remember, promptframing aims to quickly construct a [testable design with meaningful content](https://www.nngroup.com/videos/usability-testing-content/). Consider the tasks you want participants to perform with the proposed design and use them to influence your prompt writing and content-creation strategy.

### 5. Iterate Quickly

Following this process should buy you more time, and skilled UX professionals know to reinvest those time-dividends into iteration. Revise your prompts with your research insights and regenerate new content for future testing. Weaker parts should be scrapped or have their prompt revised before rerunning it in the generative AI tool.

![Illustration of a person working on a laptop with a speech bubble displaying the message "Replace AI image with new graphic using example client data, please!" and marked as "Resolved." A screen in the background shows a digital interface with icons and text related to enhancing cybersecurity.](https://media.nngroup.com/media/editor/2024/05/16/graphic_step6.jpg)

### 6. Craft Quality Content

Once you have finished iteration, give your successful prototype the "human white-glove treatment" and elevate it with more content, visual, or interactive fidelity. **Human effort will still be required to create the final design!** However, you should have received a higher volume of richer feedback covering more design ideas, resulting in an overall more effective design. You can even share your prompts with other human collaborators to give them additional context on the prototype.

*The actual page from the Blue Apron website*

## The Potential of Promptframes

UX-design tools are currently exploring generative AI. Some vendors make bold claims, but their practical utility to UX professionals is not so bold (see our [review of the current state of AI tools for UX design](https://www.nngroup.com/articles/ai-design-tools-not-ready/).) These tools may someday output robust experiences with basic prompting, but what's likely to happen currently is a mishmash of incoherent material derived from commonplace design patterns needing an excessive amount of rework to be useful. **Whether machine or human — garbage in is garbage out.**

Promptframes acknowledge that current generative-AI technology can be practical and helpful in the UX-design workflow. But they nudge us to chunk content challenges into well-documented pieces and don't excuse us from thinking and deciding what is needed and why from a user perspective. Instead, they accelerate our ability to check our assumptions with content that users can meaningfully evaluate and give us feedback on.

Perhaps future UX-design tools will offer better support for documenting prompt inputs and their associated generated outputs to help designers create and refine promptframes efficiently within their project's context. Passing a designer’s prompt via an API call to a generative AI platform is simply not enough.

## A Few Precautions to Consider

No single UX deliverable can do it all. There are a few precautions to consider specifically with promptframes.

### Not for Executive Consumption

Promptframes, like their wireframe cousins, are not suitable for reviews with executives. People cognitively distant from a project typically need high visual and content fidelity to understand design deliverables. At a minimum, promptframes can convey some forward progress (you've been hard at work making something for this project) but don't expect early-stage promptframes to be particularly helpful in a design review with stakeholders deciding the project's direction or future investment.

### Content Will Require Revision

Depending on the details provided in the prompts and the generative AI's robustness, the resulting AI-generated content will vary wildly in quality. Images may be inconsistently styled, and copy will undoubtedly need editing. Remember, the goal is not pixel-perfect, launch-ready content but to have **sensible content faster** so colleagues or testing participants might reasonably understand and share insightful feedback.

### Respect Organizational AI Policies

Some organizations regulate the use of generative AI tools to protect their data. Be aware of and adhere to these before using promptframes.

## A Good Tactic for the 1-Person UX Team

Many UX professionals are a [1-person UX team](https://www.nngroup.com/courses/one-person-ux-team/) or work in environments with low [UX maturity](https://www.nngroup.com/articles/ux-maturity-model/), with few resources or specialized collaborators. These folks benefit from augmenting their workflow to accommodate an AI content assistant, particularly if writing or graphic design are not strong skills.

However, what if you can collaborate with a content strategist or UX writer? That’s wonderful! Think of promptframes as a collaborative deliverable with these roles, which are (unfortunately) often included very late in the design process. Use the same general workflow described above to get their feedback and suggestions into the design early so their contributions can be tested along with yours.

### Conclusion

Promptframes combine our thinking of content containers with a greater emphasis on the content itself in a way that enables generative AI to accelerate our workflow for user testing and feedback. Lorem ipsum as a placeholder practice is as dead as Latin is as a spoken language. Leave Cicero to the philosophers and use promptframes to rapidly create content your users can understand.
