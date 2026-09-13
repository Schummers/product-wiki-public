---
title: "Complex Application Design: A 5-Layer Framework"
date: "2020-08-09"
url: "https://www.nngroup.com/articles/complex-application-design-framework/"
author: "Kate Kaplan"
topics: [applications, ux-design-process]
type: article
---

In preparation for our new course [Designing Complex Apps for Specialized Domains](https://www.nngroup.com/courses/complex-apps-specialized-domains/), we’ve conducted a series of research studies to understand and define the nature of complex applications, including:

- [Eyetracking](https://www.nngroup.com/articles/eyetracking-setup/) sessions to monitor users’ gaze and fixation patterns on components within complex applications
- Interviews with UX designers and researchers working on complex applications to understand the challenges and coping strategies of complex-app practitioners
- Remote observation sessions with users of complex applications to observe interaction behaviors and workflows

During these studies, we observed various factors — either inherent to the apps themselves or concerning users’ goals and environments — that contribute to an application’s categorization as complex.

## In This Article:

- [What Is a Complex Application?](#toc-what-is-a-complex-application-1)
- [A Framework: 5 Layers of Complexity](#toc-a-framework-5-layers-of-complexity-2)
- [1. Integrative Complexity](#toc-1-integrative-complexity-3)
- [2. Information Complexity](#toc-2-information-complexity-4)
- [3. Intention Complexity](#toc-3-intention-complexity-5)
- [4. Environmental Complexity](#toc-4-environmental-complexity-6)
- [5. Institutional Complexity](#toc-5-institutional-complexity-7)
- [Application of This Framework for UX Designers and Researchers](#toc-application-of-this-framework-for-ux-designers-and-researchers-8)
- [References](#toc-references-9)

## What Is a Complex Application?

We define a **complex application** as any application supporting broad, unstructured goals or nonlinear workflows.

In addition, complex apps frequently:

- Support highly trained users with specialized knowledge
- Help users navigate and manage large underlying data sets and enable advanced sensemaking or data analysis
- Support problem solving or end goals with unknown or variable underlying tasks
- Require handoff or collaboration among multiple roles, tools, or platforms
- Mitigate the risks of executing high-impact (or high-value) tasks, where high loss (e.g., revenue or even lives) is at stake

Complex apps are often specific to a specialized domain. A **specialized domain** is a field of work that requires specialized knowledge or training (i.e., expertise). Usually, work in a specialized domain requires advanced, recursive decision making and information analysis.

By comparison, **generalist applications for everyday domains** enable nonspecialized users to complete largely discrete, linear tasks organized around well-structured goals.

For example, a list-making application to create a grocery-shopping list is an example of a generalist application for an everyday domain. A geographic information system (GIS) used by scientists to analyze and predict rising sea levels is a complex application for a specialized domain.

![complex apps vs generalist apss](https://media.nngroup.com/media/editor/2020/07/14/complex-apps-vs-everday-apps.png)

*Complex applications support specialized users in carrying out broad, unstructured goals in nonlinear workflows. Generalist apps enable broad user groups to complete discrete tasks related to well-structured goals.*

## A Framework: 5 Layers of Complexity

Complexity in and of itself is difficult to define. There are many sources of complexity that contribute to the complicated nature of both designing and using complex applications.

Here we present a framework composed of 5 layers of complexity, beginning with complexity related to the core of an application itself (e.g., technology platforms and data), moving to complexity concerning the variable goals and environments of the people using the applications, and ending with the more nebulous complexity of institutionalized ways of working within organizational or domain-specific cultures.

We label these areas, respectively, as complexities of:

- Integration
- Information
- Intention
- Environment
- Institution

![5 layers of complexity for designing complex applications](https://media.nngroup.com/media/editor/2020/07/15/designing_complex_apps_5_layers_of_complexity.png)

*People who use and design complex apps navigate multiple layers of complexity, including complexities of integration, information, intention, environment, and institution.*

## 1. Integrative Complexity

**Integrative complexity** refers to the complexity of underlying technology, such as the interconnection of multiple and variable (often legacy) back-end systems or databases that support an application.

As one UX design manager in the cloud-computing industry described:

*The complexity…comes from what I'll delicately put as "legacy IT requirements." There's a lot of technical debt…We have a lot of data that is in disparate resources, and at some point, you can't make 10 calls to 10 separate data sources. You need to collate that data, clean it up, and put it in a better place. The cleanliness and the consolidation of the data is probably the most challenging thing…because you can imagine if a record set began being captured 15 or 20 years ago, it's in a very different place than a record set that we capture today, right? It's in an old legacy system, old legacy database. It's not structured; it's not containerized.*

In addition to the pain felt on the practitioner’s end in attempting to clean and consolidate unstructured data, integrative complexity often manifests in poor UX for end users — namely, slow, manual processes such as tedious data transfer and data entry for users who must reference different systems or platforms in order to make comparisons or inquiries.

A design lead in the insurance industry described observing this particular frustration during a field study with underwriters attempting to use an application to provide quotes to clients and its ripple effect on the company’s overall customer experience:

*So, we were asking them [underwriters running inquiries on the application for clients] during the shadowing, "Do you know why the client is waiting three minutes? Sometimes they were saying, "Oh. Yeah, it's because we have a batch we need to run every time the client is asking this, this, or that." Or, "Oh, we need to go in another system to look for the info”…So there was plenty of manual manipulation happening. Sometimes [the] client will really kind of [say], "Okay I'm waiting on the line. What are you doing?"*

Integrative complexity often results from the integration and layering of several disparate legacy architectures and platforms, in an effort to combine several formerly distinct products or capabilities into one product or piece together an interface to represent a single point of access to various subsystems.

A lead UX designer in the industrial-automation industry described such a case:

*This application that I'm working on is a combination of four or five pieces of software…We have all of these little pieces that do so many things. We want to create one piece of software that our customers can buy that does it all.*

Such attempts can quickly overwhelm practitioners and end users and result in complicated architectures where it feels impossible to change the system in order to improve user workflow.

## 2. Information Complexity

**Information complexity** refers to the data volume inherent in many complex applications and the interaction behaviors (e.g., exploring, filtering, zooming and modeling) required to navigate and analyze such data sets. (This layer is somewhat related to integrative complexity, as huge data sets may be dispersed among unlinked subsystems.)

Within complex applications, interface decisions must be made regarding how to both allow input to call upon a certain set of items within the data set and to display and enable user interaction with the surfaced data. When the presented data is not organized or sorted in a way that supports the workflow of the domain expert, clutter and confusion ensue.

For example, a service designer in healthcare informatics described the experience within a clinical knowledge-delivery tool that required medical practitioners to sift through high quantities of information:

*So, they [the medical practitioners] need to know how long after your last dose of that anticoagulant can you do the surgery, or should you do the surgery? So, they come here and then look at…the thromboembolic risk of the procedure and then...the procedure-specific bleeding risk…So this information helps them make that decision…But, it was a vomit of mainframe. It was an upstate-like page. I mean, it had so much information on it…And it was like, "How is anyone supposed to find anything here?"*

In addition to navigating high volumes of data, the workflows of expert or specialized users often involve building and analyzing complex data models and what-if scenarios. Ingesting, aggregating, analyzing, and exporting data from many different sources for these types of scenarios is a tedious process that creates periods of sustained waiting and interruption in user workflows.

One such occurrence is demonstrated by a coastal engineer describing the process for creating simulated computer models for sea-level rising in certain coastal regions:

*See, unfortunately, when you have gigabytes and gigabytes of data, they can take hours [to run]. Like this…it might take half a day to just do the zonal statistics on that. Yeah, just click the zonal statistics and then you'll walk away for half a day. That's how it is. So…that's why I have…70 computers and you just start processes in different ones and let them run for a while.*

When analyzing such large data sets, there’s obviously much at stake in terms of the amount of user time invested, as just described. Additionally, there is a high propensity for data inaccuracies or analysis errors. When analysis results are unexpected, even expert users often find themselves unable to quickly pinpoint sources of errors in the data.

A healthcare analyst performing a cost-effectiveness analyses on clinical-trial treatments demonstrated this challenge when she was stumped by an error in her analysis. She described the process she takes to begin uncovering the sources of ]errors in her model:

*I would first look to make sure all the variables have the right inputs, and then if [it] still seems odd, they**[the application’s support team] offer 24-hour support, so you can basically just send them an email or call them and…they will look through it with you, because…it would be really hard to know if it was some sort of error, if it was something with the model.*

The effects of information complexity, such as sustained waiting periods and the propensity for unexpected analysis results, can create uncertainty and lack of confidence in complex-application usage.

## 3. Intention Complexity

**Intention complexity** refers to **** the complexity associated with supporting the unstructured goals and broad tasks that characterize the usage of complex apps.

Workflows for complex problem solving are often nonlinear and variable; there is not always a known, ideal set of subtasks (or “happy path”) that all users follow in order to accomplish a goal and that UX practitioners can easily design for and measure the success of. Further complicating matters, many enterprise applications are designed as “open-box” software that can be marketed to many industries and many types of domain experts. Because of these two facts, designers and researchers working on applications supporting complex work may not even fully understand the range of use cases or workflows that their application needs to support.

One UX designer working on an analytics and data-monitoring platform captured this challenge in an interview, describing the product:

*I still don't know how it works…the number of contexts it can operate within…We are not even aware how it's used, because it's an open-source solution. So, that means…you can do everything with it.*

This ambiguity and variance make it difficult to understand and design for realistic usage. The difficulty is further increased when designing applications for safety-critical domains steeped in heavy regulations.

A human-factors lead in the aerospace/defense industry described the struggle to provide flexibility for a broad range of objectives and circumstances, while still designing within standardized protocols for elements such as in-app checklists:

*There’s a method that [pilots] go through on following a checklist. Everything has been paper for so long…And if you make it electronic…how do you [design for] the flexibility to make sure it [enables users] to skip over [an item] because it's not applicable for what you're doing?*

Designing for this type of flexibility is critical for the success of users who may need to vary their processes, skip around, or change approaches mid workstream, depending on the situation at hand.

## 4. Environmental Complexity

**Environmental complexity** refers to the physical surroundings of complex-app users. These surroundings are often difficult to understand and design for without first hand, real-time field work.

As an example, one UX designer working on a bedside-healthcare application described the environmental complexity faced by medical practitioners using the application and the resulting challenge for practitioners designing the application:

*They**[the medical practitioners] have so many things flashing in front of their face at all times...in addition to having to care for the person who's right next to that computer…Making sure that it [the information on the application] is distilled down to exactly what somebody needs, exactly where they need it, is extremely important.*

Another practitioner in the aerospace/defense industry working on an interface for aerial vehicles described a different yet equally complex environment for pilots:

*The complexity of it is there's so many aspects to it…if you're flying an aircraft, there's the actual aircraft itself, the interior environment, the exterior environment, then the situational awareness, then the health and status of the aircraft or whatever you're controlling.*

The competing environmental elements, interruptions, and distractions for complex-app users are almost impossible for UX practitioners or other domain outsiders to comprehend without onsite observation. Especially for practitioners with little domain experience, [field studies](https://www.nngroup.com/articles/field-studies/), such as [contextual inquiry](https://www.nngroup.com/videos/contextual-inquiry/), are critical early in the complex-app design process.

In addition to early field studies, in-situ user testing and evaluation are equally critical. The same usability-engineering lead designing military applications went on to describe the critical findings that testing with complex-app users outside of the lab can reveal:

*We do a lot of performance measurements. For example, the multitouch of a button, say, on a touch screen. There's problems when they [soldiers] have to put on protective gear. A responsive or conductive touch screen doesn't work because it doesn't have the stylus in there…The software may perform correctly in an ideal situation, but when we do our user studies, we'll do it outside [of the lab].”*

Simply put, practitioners must spend time in the work domain in order to understand the environmental factors bombarding complex-app users.

## 5. Institutional Complexity

Finally,**institutional complexity** refers to the cultural or microsocietal structures that exist within an organization, including norms, attitudes, roles, political tensions, sources of power, and institutionalized ways of doing things.

Practitioners of complex apps often defer to legacy approaches or institutionalized power sources because they feel they cannot fight them, even when they are suboptimal.

One lead user-experience researcher in the industrial-automation industry expressed frustration with working in such a “legacy” environment, where innovation was limited:

*But for the most part, they [the company] are an enterprise because they've been around forever and then they've made a million products. Then they turn into these old legacy products that they have to keep working because people rely on them and then they're old, bad code. Then you have a whole bunch of people who have worked here forever that do things this way because it's been done this way in the past and it's successful. So, there's no doing new things.*

The resistance to evolving legacy design approaches is just one way that institutional complexity creates hurdles for practitioners. Likewise, we see the effect of institutional culture and the influence of internal political structures on how designers and researchers are perceived and valued by other roles. Especially in areas of work with high domain exclusivity (meaning specialized domain knowledge unavailable to outsiders), practitioners often find themselves fighting for credibility among teams that include work-domain experts.

A senior UX interaction designer in the energy industry described her experience working with work-domain experts who have little empathy for practitioners with limited domain knowledge:

*There's a lot of subject-matter experts on the team. And they've been in this space for 10-plus years…They sometimes forget [how long they’ve been around] — like, "Hey, you didn't just come here and know everything." You had to ramp up for years…And any sort of UX people that come in —…, it just takes a long time to get them to 1) understand the business, and 2) [understand]…these user goals and motivations, and how can we enhance [the] experience?*

Another senior UX designer in healthcare-electronics manufacturing echoed this point and suggested using grassroots efforts to create partnerships with already respected staff to mitigate the challenge:

*What I do is usually I find somebody who can…help me out...Maybe they have more say in that area [of expertise] and then I just partner with them and they help me…bring my idea forward. Because I'm new. It seems like [company name redacted] has a culture of "if…you haven't been here [for a long time], you don't know what you're talking about."*

Institutional complexity is difficult to alter; however, UX practitioners should observe the influence of such factors over both the methods and assumptions employed during the design process for complex apps and the end user’s interaction with the application to build comprehensive awareness of the design hurdles they are likely to encounter.

## Application of This Framework for UX Designers and Researchers

UX practitioners often tout the importance of the user’s context (as they should). However, defining and using “context” as an all-inclusive, generic, umbrella-like concept is insufficient when it comes to designing complex apps for specialized domains. (Barbara Mirel first wrote about the inadequacy of this approach in her 2004 book, *Interaction Design for Complex Problem Solving: Developing Useful and Usable Software*.)

Rather than either being overwhelmed by complexity or simplifying your lens of context when it comes to complex-application design and usage, use the layers of complexity presented in this article as a framework for breaking down sources of complexity relevant to your work and “seeing the forest for the trees.”

In fact, during our recent Virtual UX Conference, attendees of our course on complex apps used the framework as a tool for making the complexity that surrounds their products more manageable by using a shared vocabulary and model for noting and discussing it, as shown below.

![Screenshot of a group activity where attendees discussed types of complexity present in their application design process](https://media.nngroup.com/media/editor/2020/07/09/complex-apps-complexity-activity-screenshot.png)

*A screenshot of a shared Google Sheets document from a recent virtual seminar, where attendees used the layers-of-complexity framework to note and discuss the sources of complexity surrounding their applications.*

We encourage you to use this framework, too, as part of an exercise in domain modeling, as a field-study observation tool, or simply as a method for discussing the complex nature of your work with colleagues.

To learn more about processes and approaches for designing complex applications for specialized domains, come to [our full-day seminar, Design Complex Apps for Specialized Domains](https://www.nngroup.com/courses/complex-apps-specialized-domains/).

## References

Mirel, B. (2004). *Interaction Design for Complex Problem Solving: Developing Useful and Usable Software*. San Francisco, CA: Morgan Kaufmann.
