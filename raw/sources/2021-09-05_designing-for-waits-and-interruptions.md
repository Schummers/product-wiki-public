---
title: "Designing for Long Waits and Interruptions: Mitigating Breaks in Workflow in Complex Application Design"
date: "2021-09-05"
url: "https://www.nngroup.com/articles/designing-for-waits-and-interruptions/"
author: "Kate Kaplan"
topics: [applications, design-patterns]
type: article
---

Users of [complex applications](https://www.nngroup.com/articles/complex-application-design-framework/) are frequently interrupted during their workflows, starting a task only to have to wait an extended period of time before completing it. These long waits occur for a variety of reasons — for example, the system may need a substantial amount of time to process a request (e.g., run a model, query a database) or the user may need additional information from external sources before proceeding and be forced to wait while information is gathered and before the task can be resumed.

Regardless of circumstance, adhering to the following 5 guidelines can mitigate the frustration that [complex-app users](https://www.nngroup.com/videos/myths-about-complex-app-users/) experience during long waits or interruptions in their workflows:

1. Clearly indicate progress completed and time or steps remaining
2. Contextualize success-dialog messages with additional details
3. Enable user-generated notes and comments within the system
4. Provide access to historical content
5. Allow lengthy processes to run in the background

The rest of this article provides additional details and examples for each of these guidelines.

## In This Article:

- [1. Clearly Indicate Progress Completed and Time or Steps Remaining](#toc-1-clearly-indicate-progress-completed-and-time-or-steps-remaining-1)
- [2. Contextualize Success-Dialog Messages with Additional Details](#toc-2-contextualize-success-dialog-messages-with-additional-details-2)
- [3. Enable User-Generated Notes and Comments Within the System](#toc-3-enable-user-generated-notes-and-comments-within-the-system-3)
- [4. Provide Access to Historical Content](#toc-4-provide-access-to-historical-content-4)
- [5. Allow Lengthy Processes to Run in the Background](#toc-5-allow-lengthy-processes-to-run-in-the-background-5)
- [Conclusion](#toc-conclusion-6)

## 1. Clearly Indicate Progress Completed and Time or Steps Remaining

Users of complex applications often analyze large data sets, run complex models, or query robust information sources — all processes that take a substantial amount of system-processing time. During these relatively long waits, [visibility of system status](https://www.nngroup.com/articles/visibility-system-status/) is particularly important, meaning that the user should be provided with feedback about what is happening within a reasonable amount of time.

Because it’s common for processing times in complex applications to be relatively long (at least compared to everyday online activities such as adding an item to a shopping cart), complex-app users benefit from a detailed information about what is happening during system processing and where they stand relative to the end of the process. [Progress indicators](https://www.nngroup.com/articles/progress-indicators/) that provide details such as time elapsed (or steps completed) and time or steps remaining make long waits more tolerable and increase user confidence.

For example, the geographic-information–system (GIS) application below provides details about the percentage of completed work and the current step (*Rasterizing polygon features…*) during long periods of system processing *.* This information helps users understand whether the process is proceeding as they expected, how much longer the process will take, and whether they should wait for the process to complete or begin another task during this time.

*The progress indicator includes an explicit percent-done animation and communicates the current step (“Rasterizing polygon features…”).*

When these details are not provided, even frequent, long-term users become confused and frustrated. For example, during one recent contextual-inquiry session, an urban planner attempting to analyze demographic data revealed the uncertainty that lack of progress details can create. As he waited for data to be processed, he described the “progress indicator” the system provided:

*Let's see what happens…I know it's doing something as long as it has this thing down here. If this little globe is spinning, it's still doing something. If I see that globe stops spinning, or it doesn't show up, then I know my software probably crashed.*

*Within this application, the only indication that the system is processing a request is the tiny spinning globe at the bottom of the window (red box). This approach does not help users understand what the system is doing or how much longer the process will take (not to mention the low discoverability of this indicator).*

While looped animations such as this one can help users understand that the system is doing *something*, it’s been long-established that [they are not appropriate for waits exceeding 10 seconds](https://www.nngroup.com/articles/response-times-3-important-limits/), a common scenario within complex applications. That’s because a busy-state loop animation doesn’t tell users whether it’s worth waiting out the process or they should invest in another task or action during the wait.

**To clearly indicate progress to users of complex applications:**

- Communicate percentage of work done or time remaining for any wait that exceeds 10 seconds.
- When reasonably accurate percent-done or time-remaining estimates cannot be provided, indicate relative progress by providing a list of completed and remaining steps.
- When appropriate, indicate current step. (But do not overburden users with overly detailed information about system actions.)
- Ensure the progress indicator is highly salient and discoverable.

## 2. Contextualize Success-Dialog Messages with Additional Details

During long waits, complex-app users are likely to step away from their work to complete different activities or initiate other tasks within the system; these activities will increase their overall [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/). For example, one coastal engineer in a recent study described initiating scores of analyses across 70 computers in a typical day:

*Unfortunately, when you have gigabytes and gigabytes of data, they can take hours [to run]…It might take half a day to just do the zonal statistics on [this project]. [I’ll] just click* zonal statistics *and then…walk away for half a day…That's why I have like…70 computers, and I just start processes in different ones and let them run for a while.*

To alleviate returning users’ working-memory load and help them recover context, upon completion of a process, provide details that summarize what happened while users were away.

Success [dialogs](https://www.nngroup.com/articles/modal-nonmodal-dialog/) (system messages that alert the user that a process has been successfully completed) can supply useful contextual information such as time elapsed, a timestamp of when the processes was completed, and links to any relevant information related to the completed process (e.g., new records created, related documentation for errors, logs). Using this information, users can learn typical processing times, make better informed decisions about whether they should invest in other tasks during similar processes in the future, and increase confidence that the process executed as expected.

*This success dialog includes useful details about the process: the start and end times and the total duration.*

Success dialogs are also an appropriate place to provide details about the results of the executed process — new records that were created, data matches or validations that took place, errors that occurred, or steps that were skipped.

*In addition to alerting users that the process is complete, this success dialog provides useful details in the form of number of matching records.*

Better yet, success dialogs can provide direct links to any relevant content associated with details when appropriate.

**To contextualize success messages for users of complex applications:**

- Provide start time, stop time, and total time elapsed for long processes.
- Provide information about what occurred during the process (e.g., new records that were created or steps that were skipped).
- When appropriate, link to relevant documentation or other content mentioned in the success dialog.

Make use of [modals](https://www.nngroup.com/articles/modal-nonmodal-dialog/) for success dialogs occurring after longs waits (i.e., do not allow them to disappear without explicit user interaction).

## 3. Enable User-Generated Notes and Comments Within the System

Users returning to a particular workflow after an interruption may not remember exactly what information they were looking for, which steps they completed, or why they took a particular sequence of actions. An often overlooked strategy for helping complex-app users remember their previous goals and actions is supplementing working memory with some source of [external memory](https://www.nngroup.com/articles/working-memory-external-memory/), where users can save and access information needed during their workflow within the system.

One relatively straightforward way to support the creation of an external-memory source it to allow user-generated notes or comments within the application. Using this functionality, users can track their thought processes during complex work.

For example, the decision-modeling software below allows users to create and attach comments to different distribution options as they experiment with running various analyses on their data. These comments can then be viewed in context of the workflow when analyzing the model, helping users recall what they were looking for or why they took these actions.

*In this decision-modeling software, users can create and attach comments to various distribution options, creating a source of external memory.*

When users do not have the ability to leave open-ended comments in their workflows, they face undue burden to understand and remember the purpose of objects within complex models or projects. For example, one engineer in a recent study session complained about the lack of ability to add a note to his work:

*There are no comments or anything…so you have to open every single item to know, this one is to retrieve data, this one is to [do something else]…And you always constantly have to do that… I should be able to add a note…to say this is here because the VP of sales needs it, or because this means ‘x.’*

Without the ability to add open-ended notes, users typically resort to creating and maintaining various external documents — such as a series of spreadsheets — to log their actions and thought processes. These external documents become a burden to manage and reference during complex workflows.

**To help users of complex applications track their thought processes:**

- Allow users to leave notes and comments within the system to explain their actions, additions, or queries.
- Allow comments to be open-ended.
- Show previously created comments in context of workflow.
- Do not force users to go outside of the application to track their thought processes and create sources of external memory.

## 4. Provide Access to Historical Content

Efficiency is critical for users of complex applications. Even seemingly small interactions, such as requiring users to click into a couple of extra screens in order to access a list or table before selecting and loading a project, compiles into wasted time and effort for frequent users who switch between projects or files several times a day or even hour.

To support quick task reentrance after breaks in workflow, provide historical content, such as a list of recently viewed files or pages, as soon as possible after the user logs into the application. These lists remind users where they left off and provide some quick entry points back into their workflow. For example, Azure DevOps provides a list of recently accessed content under the heading *Continue where you left off* when the user logs into the program.

*Azure Devops: Users can immediately jump to recently accessed content using the list under the heading Continue where you left off.*

When providing a list of recent, favorited, or common items, label the content properly so that users understand what it is, as is done in the example above. In contrast, many applications pin items to a homepage or overview screen without explicitly labeling them as *Recent Content* or *Continue where you left off*, making it unclear whether they **** are *frequently* or *recently* accessed content. Furthermore, it is unclear whether users can customize these items (e.g., pin or unpin items from the area).

Especially for workflows with high information complexity — such as with files that take a long time to load or that may have obscure, hard to remember, system-generated names — it can be useful to also provide a preview for historical content. For example, the application below provides thumbnail images of recent files alongside the recent file names. As the mechanical engineer using the program described, “File preview is nice here, because it takes a long time for these files to load. [There is] lots of lost time if you open the wrong file.”

*In this application, thumbnail preview images accompany file names in the Recent Documents dialog, helping users quickly find and access the intended files.*

**To help users quickly reenter previously initiated tasks:**

- Provide a list of recently accessed pages or items.
- Explicitly label this list of items so users understand that it is recent content.
- Make this list accessible as quickly as possible. Do not require users to go to a separate overview screen of pages, items, or projects in order to view the list.
- When relevant, enhance historical content with previews (e.g., when files are ambiguously named or take a long time to load).

## 5. Allow Lengthy Processes to Run in the Background

Frequently, users will prefer to perform another task, view additional information, or reference other content within the application while a process is running. Don’t trap users into a long wait during these processes by forcing them to be idle while the system works. Allow users the option to run lengthy processes in the background, so that they can continue their work within the application during the time the process is running.

*This progress indicator includes an option to run the process in the background, allowing the users the freedom to initiate or resume other tasks within the application during the wait.*

It’s worth nothing that, because processes that run in the background are not highly visible to users, the success dialogs that display at the completion of these processes should be highly salient and discoverable. Modal success dialogs, which must explicitly be dismissed by users, are appropriate because users are likely not paying attention to or thinking about these processes as they continue their work.

## Conclusion

Long waits are often inevitable during complex workflows, but there are several strategies for helping users cope with the duration of these waits and supporting task reentrance at the end of them:

1. Clearly indicate progress completed and time or steps remaining
2. Contextualize success-dialog messages with additional details
3. Enable user-generated notes and comments within the system
4. Provide access to historical content
5. Allow lengthy processes to run in the background

These guidelines and more are discussed in our full-day course, [Designing Complex Applications for Specialized Domains](https://www.nngroup.com/courses/complex-apps-specialized-domains/).
