---
title: "8 Design Guidelines for Complex Applications"
date: "2020-11-08"
url: "https://www.nngroup.com/articles/complex-application-design/"
author: "Kate Kaplan"
topics: [applications, design-patterns, interaction-design]
type: article
---

## In This Article:

- [What Is a Complex Application?](#toc-what-is-a-complex-application-1)
- [1. Promote Learning By Doing](#toc-1-promote-learning-by-doing-2)
- [2. Help Users Adopt More Efficient Methods](#toc-2-help-users-adopt-more-efficient-methods-3)
- [3. Provide Flexible and Fluid Pathways](#toc-3-provide-flexible-and-fluid-pathways-4)
- [4. Help Users Track Actions and Thought Processes](#toc-4-help-users-track-actions-and-thought-processes-5)
- [5. Coordinate Transition Among Multiple Tools and Workspaces](#toc-5-coordinate-transition-among-multiple-tools-and-workspaces-6)
- [6. Reduce Clutter Without Reducing Capability](#toc-6-reduce-clutter-without-reducing-capability-7)
- [7. Ease Transition Between Primary and Secondary Information](#toc-7-ease-transition-between-primary-and-secondary-information-8)
- [8. Make Important Information Visually Salient](#toc-8-make-important-information-visually-salient-9)
- [Conclusion](#toc-conclusion-10)

## What Is a Complex Application?

We’ve previously [defined a complex application](https://www.nngroup.com/articles/complex-application-design-framework/) as any application supporting the broad, unstructured goals or nonlinear workflows of highly trained users in specialized domains. Complex apps certainly vary in the type of workflows and end users they support — from research scientists to military professionals to financial analysts, for example — but they often share similar qualities. For example, complex apps frequently:

- Support highly trained users with specialized knowledge
- Help users navigate and manage large underlying data sets and enable advanced sensemaking or data analysis
- Support problem solving or end goals with unknown or variable underlying tasks
- Require handoff or collaboration among multiple roles, tools, or platforms
- Mitigate the risks of executing high-impact (or high-value) tasks, where high loss (e.g., revenue or even lives) is at stake

Despite the great variance, many of the same challenges exists across all complex applications, both for practitioners creating these complex applications and the end users relying on them for their work.

This article outlines 8 guidelines for complex-application design, given the shared challenges that designers and researchers face while working on these applications.

## 1. Promote Learning By Doing

Research shows that, when introduced to an application or system, users prefer to start using it immediately, undeterred by its level of complexity. Users are more motivated to begin their tasks than spend time consuming tutorials, documentation, or other types of help or setup content. (This phenomena is known as the [paradox of the active user](https://www.nngroup.com/articles/paradox-of-the-active-user/).) While it would be risky and inappropriate to rely solely on trial-and-error learning for applications in mission- or safety-critical domains, some degree of learning by doing will always be required, because it’s not possible to cover all uses of a system in a training course or manual.

Support users’ preference to begin exploring the interface immediately by allowing them to learn the interface through trial and error, without that experimentation resulting in loss of work or irreparable damages.

For example, limit users’ ability to carry out a long sequence of actions without seeing the results of those actions. Real-time dashboard construction, where a dashboard-element preview updates in real time as it is constructed, supports this principle. Users do not have to wait until the end of their task to see if the result of their actions matches their intent.

![screenshot of dashboard widget editing dialogue box, with filters on the left, and live preview of dashboard element on the right](https://media.nngroup.com/media/editor/2020/10/23/1_learning-by-doing-dashboard-editing.jpg)

*In this Salesforce dashboard editing module, the dashboard element is previewed and updated in real time on the right as the user sets parameters and filters for the data on the left.*

## 2. Help Users Adopt More Efficient Methods

For the most part, even users of complex applications tend to plateau at mediocre performance. In other words, the majority of users do not transition to true expert usage with the systems they use when left to their own devices. Many users will [satisfice](https://www.nngroup.com/articles/satisficing/), meaning that they will keep using satisfactory (often inefficient) ways of accomplishing tasks, rather than invest time in seeking out optimal solutions for their workflows. This behavior adds up to an incredible chasm in productivity over time, as users spend years or even decades using the same system day-in and day-out in inefficient ways.

Help users transition to more efficient methods and break their ingrained behavioral patterns by finding unobtrusive ways to communicate faster, more efficient methods for their tasks.

For example, instead of relying solely on lengthy tutorials or manuals (even well-written ones), embed in-context learning cues for [accelerators](https://www.nngroup.com/articles/ui-accelerators/) or additional functions throughout the application. In-context learning cues are those presented to the users only in context of the task at hand. [Tooltips](https://www.nngroup.com/articles/tooltip-guidelines/) that suggest a faster method for accomplishing a task as the user hovers over a toolbar menu item support this principle.

![screenshot of a desktop application displaying a tooltip that reads: Add Data. Add new data to the map's active data frame. Tip: You can also drag data into the map from the Catalog window.](https://media.nngroup.com/media/editor/2020/10/23/2_efficient-methods-tooltip.jpeg)

*ArcMap, a geospatial processing program, provides in-context help, alerting users of an alternative, faster method to add data to the map (here, drag-and-drop) as they hover over a toolbar menu item.*

## 3. Provide Flexible and Fluid Pathways

Users of complex applications often carry out broad, unstructured goals in nonlinear workflows. For these workflows, users may not know their exact end goal, but rather need to analyze data to look for answers. Even if a well formulated end goal does exist, users often do not follow a known, sequential set of subtasks to reach it. Yet, out of necessity, the system has to have some sort of structure: a physical interface with which users interact and some type of linear process that they complete over time.

Allow users flexibility in their task sequence by avoiding rigid, linear workflows that force users through a set of actions from start to finish with no escape hatches or flexibility in sequence.

For example, provide methods that allow for skipping ahead, looping back to an earlier step, and moving fluidly from any step to any other. For example, a flexible, interactive sequence map within a [wizard](https://www.nngroup.com/articles/wizards/) allows users to return to previous steps without losing their progress.

![screenshot of a desktop application featuring a sequence map with 8 clickable targets (Event, Settings, Setup, Clean, Control, Evaluate, Finalize, Results)](https://media.nngroup.com/media/editor/2020/10/23/3_fluid-pathways-sequence-map.jpeg)

*Mastercard Test & Learn, a self-service analytics application, uses wizards to guide users through complex tasks, but provides flexibility with an interactive sequence map that allows users to move back and forth through the sequence steps at their discretion.*

## 4. Help Users Track Actions and Thought Processes

Complex-app users often face long waits and frequent interruptions to their work. Complex data analyses can run for hours, if not days, for example, and the high [environmental complexity](https://www.nngroup.com/articles/complex-application-design-framework/) surrounding most complex-app users can translate to unexpected and jarring interruptions in their work. Even without unplanned interruptions, the complexity and variability in subtasks executed to achieve a goal requires users to hold a lot of information in [working memory](https://www.nngroup.com/articles/working-memory-external-memory/) during tasks, which can be easily lost as they pivot directions.

Offload working-memory burden and help users resume tasks after interruptions or breaks in workflow by enabling users to keep a record of their actions and thought processes during their work.

Allowing users to add and store open-ended notes about particular data sets, charts, or other elements is one way to support this principle. For example, during complex data modeling or analysis, user-entered comments can remind users at later points in time why they created a model and what question they were attempting to answer when they did so.

![2 screenshots of the same web application. one shows a feature to add a comment during data analysis. the second screenshot shows a user accessing a previously-created comment within a data model.](https://media.nngroup.com/media/editor/2020/10/23/4_track-thoughts-enabling-comments.jpeg)

*TreeAge, a decision-modeling software, allows users to enter open-ended comments during data analysis and modeling (top) that can be accessed at later points in time (bottom).*

## 5. Coordinate Transition Among Multiple Tools and Workspaces

Complex-app users typically work across multiple tools and multiple workspaces. Even if users rely mostly on one specialized application for the majority of their work, they frequently switch applications for a number of reasons; for example, to gather data from online databases, find and reference articles or other external documentation, or make their own notes and commentary in other applications when the primary software does not support that action. Even within the primary application, users may transition between different environments or workspaces due to software addons or other optional packages that enable various specialized functions within the application.

Reduce the burden of tool switching by supporting the transition from one environment to another, both inside and outside the primary application.

One way to reduce the burden of tool switching is by simply accepting this ecosystem and designing connection points between the primary application and frequently used third-party tools. For example, complex work often requires collaboration and reporting. Built-in functions for exporting data sets to Excel or images to PowerPoint enable users to save precious time otherwise spent converting data or screenshotting images as they attempt to compile reports and presentations.

![screenshot of an dashboard with several icons in the top right of each dashboard element. One icon displays a tooltip on hover that says: Copy visual as image.](https://media.nngroup.com/media/editor/2020/10/23/5-ease-transition-export-as-image.jpg)

*Microsoft Power BI, a business analytics application, provides a function to copy visuals as images, enabling users to quickly capture and insert data visualizations into external applications.*

## 6. Reduce Clutter Without Reducing Capability

Complex apps are often designed to accommodate a broad range of uses. The same analytics-monitoring software used by an environmental agency to measure and track honey-bee production might also be used by an automotive company to monitor machine failure, for example. This diversity of usage scenarios makes complex applications very powerful on the one hand, but often very cluttered, on the other. Additionally, complex applications must often support both novice and expert users at the same time, and expert users may need advanced features that infrequent or novice users rarely access.

Help users manage the choice, feature and function overload prevalent within complex applications by minimizing the appearance of clutter within the interface without reducing the capability of the application.

[Staged disclosure](https://www.nngroup.com/articles/progressive-disclosure/), where options are shown to the user only when they are relevant to the task at hand or the item in focus, is one way to reduce clutter. For example, displaying advanced parameters or settings only after a related field is checked in a complex [form](https://www.nngroup.com/articles/forms-vs-applications/) or wizard is an example of staged disclosure relevant to complex applications.

![2 screenshots of a form in a web application. The top screenshot has a checkbox for the setting "mark this setting as private." In the second screenshot, the checkbox is checked, and a sub-setting is now displayed for who to "give permissions to."](https://media.nngroup.com/media/editor/2020/10/23/6-staged-disclosure.jpeg)

*This complex setup dialogue uses staged disclosure to reduce clutter. In this case, the* Give permissions to *setting (bottom) is only displayed after the* Mark this setting as private *option (top) is selected.*

## 7. Ease Transition Between Primary and Secondary Information

Even when clutter is effectively reduced within an interface, not all elements and information can (or should) be displayed at once. Some information must be deferred to secondary levels; however, that secondary information is often necessary to contextualize and make decisions about information on the primary level.

Ease the transition between primary and secondary information and help users contextualize primary information by allowing users to access and view supplemental information without leaving the primary screen or environment.

Dashboards often support this principle, for example, by allowing users to view more precise quantitative data in a tooltip when the user hovers over a specific point in a chart or graph.

![screenshot of a dashboard within a web application. the mouse icon hovers over a line graph, and a tooltip is displayed showing more precise data for the point in the chart.](https://media.nngroup.com/media/editor/2020/10/23/7-ease-transition-dashboard-hover-tooltip.jpeg)

*In this dashboard, hovering over a data visualization reveals more precise detail about a particular point without requiring users to navigate away from the primary screen.*

## 8. Make Important Information Visually Salient

Many of the tasks performed by complex-app users require a high degree of visual search. To name a few examples: Users may have to locate and distinguish relevant data across tabular views in huge tables. System alerts must draw attention to relevant parts of the interface so that users can notice and rectify underlying conditions in a timely manner. Simply viewing and attempting to comprehend data visualizations on a dashboard has a significant visual-search component, as well. The sheer amount of competing information and elements within complex application can hinder these tasks.

Help users find and act upon important information by making critical elements visually salient, (i.e., making them stand out from surrounding elements). It’s worth noting that making important information stand out does not always mean adding emphasis to that information (e.g., a bright color or a heavier font weight). Removing nonessential elements can be equally or even more effective at making important information visually salient.

For example, removing superfluous graphics or visual elements that serve no purpose can make the data left behind stand out. A dashboard module that eliminates nondistinctive, unintelligible illustrations from data elements supports this principle by lessening the burden of visual search for the user attempting to locate data across the dashboard.

![screenshots of 2 different sets of dashboards. Dashboard elements on the left display clear, large numbers without imagery or icons. Dashboard elements in the right set display numbers next to various money-related icons (a piggy bank, a computer with a money icon on the screen, and a stack of cash)](https://media.nngroup.com/media/editor/2020/10/23/8-reduce-clutter-dashboard-icons.jpeg)

*Dashboard elements accompanied by superfluous graphics make visual search more difficult (left). Dashboard elements without unnecessary icons make the numerical data more visually salient (right).*

## Conclusion

Complex applications are diverse, supporting a board range of user types and workflows; however, similar challenges exist across such complex applications, regardless of domain. Optimize complex applications by following these 8 design guidelines:

1. Promote learning by doing.
2. Help users adopt more efficient methods to do their tasks.
3. Provide flexible and fluid pathways through workflows.
4. Help users track actions and thought processes.
5. Coordinate transition among multiple tools and workspaces.
6. Reduce clutter without reducing capability.
7. Ease transition between primary and secondary information.
8. Make important information visually salient.
