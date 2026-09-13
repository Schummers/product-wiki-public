---
title: "Wireflows: A UX Deliverable for Workflows and Apps"
date: "2016-12-04"
url: "https://www.nngroup.com/articles/wireflows/"
author: "Page Laubheimer"
topics: [applications, interaction-design, visual-design]
type: article
---

## In This Article:

- [Introduction](#toc-introduction-1)
- [Wireflows as a Deliverable for Workflows](#toc-wireflows-as-a-deliverable-for-workflows-2)
- [Why We Need Something New: Flowcharts and Wireframes Don't Document Complex Apps Well](#toc-why-we-need-something-new-flowcharts-and-wireframes-dont-document-complex-apps-well-3)
- [Wireflows Document Interactions](#toc-wireflows-document-interactions-4)
- [Wireflows for Collaborative Ideation](#toc-wireflows-for-collaborative-ideation-5)
- [Conclusion](#toc-conclusion-6)

## Introduction

In the UX field, [wireframes](https://www.nngroup.com/courses/wireframing-and-prototyping/) are a common deliverable to show page-level layout ideas, whereas flowcharts are useful for documenting complex [workflows and user tasks](https://www.nngroup.com/articles/workflow-expectations/). However, despite the fact that both of these deliverables [remain in common use among UX professionals](https://www.nngroup.com/articles/common-ux-deliverables/), there are situations in which they are suboptimal tools for communicating design ideas, particularly when documenting mobile, [desktop, or web apps](https://www.nngroup.com/courses/application-ux/) that don't have many unique pages, but instead feature a few core pages which change content (or layout) dynamically based on user interaction. In the last few years, an alternative deliverable called **wireflow** has emerged as a solution to these issues, used to show designs in the context of common user tasks.

![Standard desktop wireframe](https://media.nngroup.com/media/editor/2017/05/11/standard-wireframe-desktop-8.png)

*A wireframe of a web page conveys layout ideas, content, and page-level design for websites and apps that have few, mostly static pages, but is not as useful in communicating heavily dynamic process flows.*

![Simple UX workflow flowchart](https://media.nngroup.com/media/editor/2017/05/11/simple_flowchart_for_nng_wireflows_article-8.png)

Flowcharts are used describe both back-end processes and user task flows (as seen in this example). However, for UX use, they lack the page context — an aspect which strongly impacts the user experience.

## Wireflows as a Deliverable for Workflows

**Definition: Wireflows are a design-specification format****that combines wireframe-style page layout designs****with a simplified flowchart-like way of representing interactions**.

![Mobile app wireflow](https://media.nngroup.com/media/editor/2017/05/11/reworked-littlehootz-8.png)

*This low-fidelity wireflow shows a simple user task. The use of screen designs, rather than abstract flowchart symbols, keeps focus on the product with which users will be interacting. While wireflows can be created in high fidelity for the purposes of communicating detailed design specifications, they are just as useful as lower-fidelity documents to discuss and communicate interaction design and user workflows.*

Wireflows emerged as a common practice among teams designing mobile apps, where each step in the flowchart is represented by a wireframe for a full mobile-screen design. Because of the relatively small size of mobile screens, actual page designs (i.e., wireframes) could easily replace abstract symbols in flowcharts. However, wireflows are not merely limited to documenting mobile apps and websites — they can also be used for desktop products, typically by showing a portion of a screen or webpage that changes based on user interactions. Many designs for [ecommerce shopping carts and checkout pages](https://www.nngroup.com/reports/ecommerce-ux-shopping-carts-checkout-registration/) are suited to be specified as wireflows.

## Why We Need Something New: Flowcharts and Wireframes Don't Document Complex Apps Well

Usually it’s bad to introduce a new specification format because many stakeholders won’t know how to interpret it. What’s old is usually familiar. However, we do like wireflows because (1) they are easily [learnable](https://www.nngroup.com/articles/power-law-learning/) by those who’ve seen wireframes and flowcharts before, and (2) wireflows have enough advantages to overcome the inertia that otherwise favors familiar formats.

Wireframes are a great way of showing layout, but they don't describe interaction well, and they are especially poor at documenting the layout of digital products that have a lot of dynamic content, such as mobile apps or [webapps](https://www.nngroup.com/courses/application-ux/). Wireframes are most useful when documenting websites (or other digital products) with many discrete, *relatively static* pages or screens, where clicking a link or button will typically [navigate to a completely different page](https://www.nngroup.com/articles/avoid-within-page-links/).

However, many modern webapps and mobile apps have few overall pages, but change the content and layout dynamically through [AJAX](https://www.nngroup.com/articles/good-ajax-an-example/)(or other technologies), based on interactions the user has with the product. They can range from ecommerce products in which selecting [facets or filters](https://www.nngroup.com/articles/filters-vs-facets/) changes the products shown on the page, to [complex creative or technical applications](https://www.nngroup.com/courses/application-ux/), where the overall layout and information present can vary drastically based on interactions with tools, modes, and other control parameters. In these cases, wireframes don't capture well the various layout possibilities or the rules for how content changes. In addition, typical wireframes don't document the important [feedback](https://www.nngroup.com/articles/direct-manipulation/)that the system presents to users after they interact with the page. (Feedback that communicates to users that their action has been recognized by the system is critical to a good user experience, and is the first of the [10 usability heuristics.](https://www.nngroup.com/articles/ten-usability-heuristics/))

Flowcharts, on the other hand are a tool for *exhaustively* documenting complex workflows and interactions with multiple steps or paths, but typically leave out the context of the interactions and its impact over users. Using flowcharts as the main deliverable to document (and ideate) the interaction design and steps involved in multistep user tasks can lose sight of the information that's shown contextually on the page and that influences the success of the interaction.

## Wireflows Document Interactions

The classic use-case for wireflows is to document the process of a user working through a common task on the product (e.g. “send a direct message to someone in your network” on a social media app). At each step in the workflow a simple wireframe or high fidelity screen mock-up shows the screen available to users.

An arrow is used to indicate the specific UI component where the user takes action (such as a tap on a button, click on a link, and so forth), and points to another wireframe image of what happens as a result of the interaction. The second "node" of that interaction need not be a separate page or screen; rather, it can show the same page with the result of that interaction, such as content that has changed, or feedback that the interface shows as a result of the interaction (e.g., a confirmation popup, a color change, or an error message). It's important that the arrows clearly indicate the clickable “hotspots” (or targets) that lead to the next step in the flow, in order to lessen ambiguity in the wireflow. Unambiguously indicating the triggering hotspot is particularly important for complex apps that have multiple actionable targets on a single page.

![Mobile app wireflow](https://media.nngroup.com/media/editor/2017/05/11/letter-8.png)

*This simple wireflow shows a sequence of several mobile-app wireframes for a typical user-task flow. In this example, each wireframe corresponds to the same app page, rather than representing different app pages. Each step clearly indicates the hotspots that connect to the next step in the task flow. In addition, the wireflow shows the use of visual feedback in the second step (where the clicked album changes background color to register the tap).*

Despite being most frequently used for mobile apps, wireflows are also useful for documenting complex workflows in desktop application and webapps. Since showing a full-screen desktop wireframe for each step in a process can waste a lot of space if most of the screen design stays unchanged at each step, showing only the portion of the screen that changes (such as a dialog box, modal, filters or facets) in each step can be sufficient to document relevant, changing parts of the interface, while still providing enough context.

![Desktop Wireflow](https://media.nngroup.com/media/editor/2017/05/11/desktopwireflowv2-8.png)

*A simplified high-fidelity desktop wireflow for a configurator webapp demonstrates that not all parts of the screen design must be represented in each step. Due to the larger size of desktop screen designs, showing the full page for each step is not necessary if the majority of the information visible does not change. Using a tactical approach to showing relevant screen designs, one can visualize only the elements that do change due to user input. (Screenshots from www.planar.com made into a wireflow by NN/g)*

While wireflows excel at showing task flows on apps and dynamic websites where the content or layout on each page changes based on user interactions, they can also be suitable for documenting task flows in traditional static websites. Be cautious, however, about using wireflows to document static *desktop* sites, as the size of each wireframe image can be large enough to lose the context of the process being documented.

## Wireflows for Collaborative Ideation

In addition to being a useful form of communication with project stakeholders and developers, wireflows also work well as a tool for collaboration between team members. Especially in [Agile environments](https://www.nngroup.com/topic/agile/), being able to collaborate and communicate well among a crossfunctional team is critical. [Design-workshop sessions](https://www.nngroup.com/articles/design-charrettes/) can build buy-in and shared understanding among a crossfunctional team; in these [parallel-design](https://www.nngroup.com/articles/parallel-design/) workshops, team members ideate and write down task flows, the group then discusses options, and the UX person sketches each step in a wireflow style to visualize potential options (and to document ideas that the team agrees on).

In a collaborative environment, wireflows need not be visually polished; these types of discussions are benefitted strongly by using sketching techniques with a whiteboard or paper and pencil to quickly document ideas and focus on the interactions.

![Deliverables Seminar Wireflow Photo](https://media.nngroup.com/media/editor/2017/05/11/deliverables-wireflow-seminar-photo.jpg)

*Several team members in the UX Deliverables seminar at an NN/g UX Conference use mobile-phone sticky notes, markers, and paper to collaborate on a wireflow in a design workshop. This process can easily work on a whiteboard, or simply using paper and pencil.*

## Conclusion

Wireflows are an emerging UX deliverable for documenting user workflows and complex interactions for mobile and webapps. They are well suited for representing dynamic changes on one or few pages inside an app, and work less well for capturing flows through a large number of relatively static pages linked together. Wireflows are also useful as a collaboration and ideation technique for teams to think through user workflows and tasks and to ideate screen designs at each step in the process.
