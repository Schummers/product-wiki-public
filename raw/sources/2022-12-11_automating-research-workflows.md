---
title: "Supercharge UX Research by Automating Workflows and Repetitive Tasks"
date: "2022-12-11"
url: "https://www.nngroup.com/articles/automating-research-workflows/"
author: "Kim Flaherty"
topics: []
type: article
---

[ResearchOps](https://www.nngroup.com/articles/research-ops-101/) and [DesignOps](https://www.nngroup.com/articles/design-ops-definitions/) have emerged as new subfields of UX focused on increasing the productivity and efficiency of research and, respectively, design processes. This article discusses ways to improve research operations with added efficiencies by finding ways to automate and streamline the repetitive tasks behind the work we do.

## In This Article:

- [Downsides of User Research](#toc-downsides-of-user-research-1)
- [UX Researchers Find Ways to Create Efficiencies](#toc-ux-researchers-find-ways-to-create-efficiencies-2)
- [Other Ways to Automate](#toc-other-ways-to-automate-3)
- [Conclusion](#toc-conclusion-4)
- [Call for Examples](#toc-call-for-examples-5)

## Downsides of User Research

Conducting user research is central to every UX practice. However, user research is time- and resource-intensive. [Agile product development](https://www.nngroup.com/articles/agile-user-experience-projects/) is fast-paced, and applying UX appropriately throughout the lifecycle requires many different types of user research, ranging [from discovery](https://www.nngroup.com/articles/discovery-phase/) and [ethnographic research](https://www.nngroup.com/videos/ethnography-ux/) to [usability testing](https://www.nngroup.com/articles/usability-testing-101/). Conducting good UX research incurs administrative overhead such as:

- Recruiting and scheduling
- Study and participant management
- Data preparation

## UX Researchers Find Ways to Create Efficiencies

Enterprising researchers have found ways to streamline workflows and automate the repetitive and administrative activities involved in conducting research studies. We’ve spoken with some of these researchers and we highlight several tips and tricks learned from them in hopes of inspiring you to find similar opportunities for automation within your workflows.

### Use Webhooks and Scripting to Automate Recruiting and Scheduling

You can automate one or more steps in the process of filling in time slots for your research study by creating scripts that email potential candidates with a request to fill in an online screener; other scripts can alert you whenever someone successfully satisfied your screening criteria or even automatically schedule the candidate to an available time slot.

Mika Brown and Bronwyn Larsen, both UX researchers at Zapier, a software product that helps users write webhooks to connect multiple web applications together through scripts and Application Programming Interface (API) calls, shared how they use their own product to automate research-participant recruitment and scheduling.

Researchers at Zapier use a temporary Google Sheet that contains contact information for potential study participants. (For [privacy reasons,](https://www.nngroup.com/articles/privacy-and-security/) once recruitment is completed, that spreadsheet is deleted.) A column in that spreadsheet indicates whether a given participant would be a good candidate for a particular study. When researchers are ready to begin recruiting, they kick off the process by typing a trigger word (e.g., “RECRUIT”) into another column in the spreadsheet. The Zapier app identifies the trigger and kicks off a series of automated activities, in the following order:

1. Zapier sends a personalized email to all participants indicated in the spreadsheet as candidates for a given study with an invitation to fill in a web-based screener form hosted by Typeform, a form-filling platform.
2. Typeform notifies the Zapier app whenever a new participant has qualified for the study.
3. Zapier emails the qualified participant with an invitation to schedule a study session using Calendly, a scheduling web-based tool.

By setting up these automations, researchers can schedule study sessions without running through the overhead of emailing, coordinating with potential participants, and keeping track of the recruitment progress.

The process isn’t foolproof, however. The researchers have learned to work in several smaller batches, rather than in one large batch. This approach gives them time to assess the mix of participants that have been scheduled against their recruitment profile and adjust accordingly.

### Automating Invites and Reminders to Participate

Another task that can be scripted is sending confirmation and reminder emails to all parties involved in a particular study session — from participants to observers.

At Zapier, when a recruited participant signs up for a study session through the Calendly app, the following research-preparation tasks are also triggered:

- A confirmation email is sent to participants.
- A Slack message announces the time of the session (customized to individuals’ time zones) on an internal research Slack channel. Readers can express their interest by responding with a checkmark emoji; Zapier then sends an invitation with the session details (e.g., meeting link) to interested respondents.
- Zapier sends a reminder email to the research participant exactly one day before the study session; the email also asks the participant to complete the [consent form](https://www.nngroup.com/articles/informed-consent/) for the study.
- After the consent form is received, another email is sent with instructions for how to join the session.

### Keeping Track of Diary-Study Entries

In diary studies, researchers often must monitor the entries received from each participant to figure out if someone is behind and to remind them to send a new entry. This task can also be automated.

For example, our colleague Feifei Liu recently ran a 2-week [diary study](https://www.nngroup.com/articles/diary-studies/) in which participants were asked to provide a minimum number of reports before several milestones during the study; to keep track of the number of reports provided by each participant, she created a Zapier script that updated a Google Sheet whenever the participant emailed her with a new report.

### Incentive Delivery

It is possible to automatically send incentives to those participants who finished a study.

For example, when Zapier study participants complete a Qualtrics survey, the team automatically sends them their incentive through BHN Rewards, an online platform for providing e-gift cards..

### Data Preparation

After data is collected in a study, there’s often a degree of data preparation and cleaning required to get it in a format ready for analysis. For example, the data from quantitative-study sessions or video diaries may be uploaded in a repository and transcribed.

For a recent [diary study](https://drive.google.com/drive/u/0/folders/12PbKYQMrg_EhraDqPDhJQTOaCTpGNX7B) that I have run, whenever participants completed a questionnaire, their data was automatically uploaded into Dovetail, a tool for qualitative-data analysis. This automatization not only provided me with a real-time understanding of the study progress and of the engagement of each participant, but it also allowed me to code and analyze early survey responses as soon as they were received, without wasting time doing any manual data preparation.

## Other Ways to Automate

The examples shared in this article made use of Zapier as an automation tool. Although Zapier is designed to make these types of automations easy, you do not need access to this specific tool to streamline your workflows. There are other ways to automate tasks.

### Write Your Own Webhooks

It’s possible to write your own webhooks that allow various web-based services to communicate with each other. Webhooks are HTTP-based callback functions that allow lightweight, event-driven communication between two APIs. Zapier simply helps noncoders to set up webhooks via its GUI interface.

For example, suppose you’d like to generate a unique folder on Google Drive for every participant recruited to a usability study, along with an empty note-taking template file within that folder for every planned observer for those sessions. If this were a common workflow or a testing procedure defined by your ResearchOps program, developing a custom set of webhooks to automate this time-consuming file setup for each study would be worth the investment. When a new test participant is added to a participant spreadsheet, the webhooks could process the folder setup for that participant. This situation would require custom webhooks that deliver API commands to Google Drive directing the application to generate folders and make copies of note-taking template files. The specifics of the file setup could also be provided in other cells of the spreadsheet.

Scripts can also be written in Google Sheets and Google Docs. For instance, when an item on a to-do list is marked complete, an email could be generated to the next person in the workflow to complete their part of the process.

### Create Automations for Your Local Machine

Webhooks are not useful for tasks that take place on your personal device. That said, you can always write a small program or script to consolidate multiple operations into a single task and thus automate repetitive or cumbersome activities.

Scripting, however, is not for everyone. (There is a reason, after all, why command-line interfaces are not popular today.) However, tools such as Apple’s Automator, let you automate many of the activities you typically do on your computer without knowledge of programming or scripting languages.

For example, to prepare attendee materials for the courses I teach at our [NN/g virtual UX conferences](https://www.nngroup.com/training/virtual/): I have created an Automator workflow that creates copies of a master workbook for all attendees in my class. This type of file prep would take me at least 30 minutes to complete manually.

You can also create scripts to set up the correct desktop setup for a given complex task — for example, to open and position all the applications that you may need for a usability test or for a complex Zoom training session. Or, between two consecutive user-testing sessions, you may have a script to save one participant’s data, close all windows, clear out any history or cookies, and prepare the product or prototype for the next participant.

## Conclusion

To identify opportunities in your own research processes, consider conducting a [task analysis](https://www.nngroup.com/articles/task-analysis/) and documenting your workflow. If you seek to create reusable automations for a team of researchers, put your research skills to work by conducting interviews with your coworkers and observing how they carry out research activities. Look for manual and repetitive activities such as the need to move data from one tool to another and the need to manually track and document the progress of a study. Keep track of these common workflows and administrative tasks that take up time and resources.

Prioritize automations that will have the biggest impact and consider creating a shared library of such automations that researchers can search, copy, and tweak for their own purposes.

For more in-depth information about Research Operations, look into our training course [Research Ops](https://www.nngroup.com/courses/researchops/).

## Call for Examples

Thank you to the researchers who shared their workflows and automations with me for this article. We would like to hear what other efficiencies and automation our audience has create, for both research and design. Please share with us how you, your team, or your organization automate parts of your design and research workflows. We intend to publish additional examples gathered through this effort.

[Share your automation example](https://link.nngroup.com/ux-automation)
