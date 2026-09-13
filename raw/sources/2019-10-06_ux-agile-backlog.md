---
title: "Incorporating UX Work into Your Agile Backlog"
date: "2019-10-06"
url: "https://www.nngroup.com/articles/ux-agile-backlog/"
author: "Rachel Krause"
topics: [agile, ux-design-process, ux-teams]
type: article
---

There is no definitive rulebook when it comes to Agile backlogs — every team may structure its backlog differently. At its core, this is a *good* thing: every team has its own way of working so a one-size-fits-all process isn’t practical. However, because of this flexibility and lack of official rules, UX is sometimes left out of the process.

**Definition:** A **backlog** is an ordered list of to-do items — including features, updates to existing features, bug fixes, [UX debt](https://www.nngroup.com/articles/ux-debt/), or other activities — that a team intends to deliver to complete a project.

## In This Article:

- [Backlogs in Agile](#toc-backlogs-in-agile-1)
- [Backlog Structure](#toc-backlog-structure-2)
- [Conclusion](#toc-conclusion-3)

## Backlogs in Agile

On most Agile teams, feature planning is documented in the form of [user stories](https://www.nngroup.com/articles/ux-user-stories/). Each user story is given acceptance criteria and an estimated effort necessary to complete them, and the list of stories is then prioritized based on the needs of the stakeholders, business, and development team.

Prioritization is an important task of any Agile team, as it determines what user stories will be completed in a given sprint. Depending on how much your stakeholders believe in the value of UX, user stories that represent UX work can be deprioritized in favor of development-focused user stories.

## Backlog Structure

Agile teams are often faced with a dilemma: should they use one backlog that includes UX work or use a dedicated UX backlog that is separate from development user stories?

Both methods — following one unified backlog or maintaining multiple backlogs — can be successful, depending on the nuances of how they are implemented. The key is to understand how your team works together and how much influence your stakeholders have on the backlog. Let’s look at some pros and cons of these different backlog models.

### Unified Backlog: Explicit UX and Development Items in the Same Backlog

A unified backlog stores all the work for the product, including development tasks, UX activities, and QA tasks.

Priority | Title | User Story | Story Points | Tag | 1 | Export data on dashboard | As a warehouse manager, I want to export data from my dashboard so I can run nightly reports. | 5 | Feature | 2 | Prototype: Filtering enhancements | As a warehouse manager, I want to filter my data. | 2 | UX | 3 | Reset password | As a user of the system, I want to enter a new password for my account. | 2 | Feature | 4 | New prospective client alerts | As an account manager, I want to know when potential new clients request information. | 3 | Feature

*An example of a sprint in a unified backlog**: items can be UX-related or development-related*

In this backlog example, the sprint is made up of 4 backlog items, each with its corresponding [story-point estimate](https://www.nngroup.com/articles/ux-user-stories/). The highlighted item, *Prototype: Filtering Enhancements*, is a UX-specific item that refers to building and testing a prototype.

![Jira backlog](https://media.nngroup.com/media/editor/2019/09/24/jira-backlog.png)

*Jira Software:  A backlog item can be labeled UX to help the team differentiate multiple types of work.*

With explicit UX-specific items included in the unified backlog, UX work is prioritized and estimated like anything else in the backlog. Differentiate UX backlog items from development items using tags, specific task names (e.g., prefixed by the string *UX*), or by using dedicated features (e.g., labels or categories) in your product-management software.

#### 

#### Pros

**This method makes UX work visible to the team and their stakeholders.** Everybody can look at the backlog and know what UX work needs to be done. Using tags in your product-management software will make UX items easy to filter.

**UX-related backlog items are often large, general tasks rather than small, specific ones**— a good thing for designers who are trying to envision an entire workflow or interaction, rather than just a small piece. User stories in an Agile backlog are typically specific and set up to be completed in a single sprint. However, we often have to think about UX work at a higher level to make sure we’re maintaining consistency throughout the application and that our designs accommodate the larger vision of the application. Using explicit UX-specific backlog items doesn’t limit the scope of the UX work.

#### 

#### Cons

**UX items can be deprioritized by stakeholders in favor of new features —** especially if they don’t see value in UX research. If you find that your stakeholders are consistently deprioritizing UX-related backlog items, you’ll want to try one of the other two backlog techniques explained later in this article.

**It can be harder to keep track of dependencies.** Certain UX-specific items may affect other backlog items, which means you’ll need to determine what needs to be completed first. If you use tags or categories in your product-management software, it may be easy to get away with this. However, pay extra attention to dependencies to avoid development working on a backlog item before you can do adequate UX work on it.

### Task-Based Unified Backlog: Role-Based Work Expressed as Tasks Within Backlog Items

The second method of organizing your backlog is to have items that each break down into a set of subtasks for different team competencies (e.g., UX tasks, development tasks).

Priority | Title | User Story | Story Points | Tag | 2 | Filtering enhancements | As a warehouse manager, I want to filter my data. | 2 | Enhancement | Task | Assigned To | Design filtering views | UX | Incorporate user feedback | UX | Implement filtering views | Development | Regression test | Quality Assurance

*An example of a unified backlog in which each item is split into multiple components assigned to different roles*

In this example, the backlog item *Filtering enhancements* breaks down into 4 subtasks — some for UX, some for development, and some for quality testing. When all these subtasks are completed, the backlog item is considered done.

In this method, UX tasks are added to any backlog item that requires**UX work. Examples of UX tasks include research, design, and usability testing.

#### 

#### Pros

**This method works best when design and development can be completed in a single sprint.** This is typically the case when teams are working with a well-understood domain and small or focused design problems. Since all members of the team are completing work at the same time, the team needs to ensure that UX work does not prevent the rest of the team from making progress.

**It’s easy to see a checklist of what needs to be done on each backlog item.** Each role on the team has associated tasks on backlog items; thus, dependencies across different types of work will be easier to identify than with a mixed-item unified backlog. Better tracking of what has yet to be completed will also be possible.

#### 

#### Cons

**Teams need to be skilled in estimating backlog items.** Since you’ll have multiple roles working on the same backlog item, estimation can get confusing. Some teams like to use Planning Poker or the Fibonacci sequence for development items, while using t-shirt sizes for UX work.

![Estimation with t-shirt sizes](https://media.nngroup.com/media/editor/2019/09/24/tshirt-estimation.png)

*When estimating in t-shirt sizes, items that are Small can be done quickly without much testing needed, while items that are Large will take more time and may be the only item completed in a sprint.*

**There is a chance that you’ll be carrying over backlog items from sprint to sprint, depending on the progress of tasks.** For example, if incorporating user feedback is a UX task that doesn’t happen until the end of a sprint, the corresponding development task may roll over into the next sprint, which would carry the entire backlog item over as well.

### Multiple Backlogs

The last backlog model is to maintain multiple backlogs, one for each competency — for example, a UX backlog and a main development backlog. Generally, I recommend this model only after you’ve tried the other two, as it takes a lot of discipline and communication to maintain multiple backlogs. This method is also ideal for [siloed UX teams or teams with multiple UX specialties](https://www.nngroup.com/articles/ux-team-models/).

UX Backlog | Prototype: Filtering enhancements | Usability test: Filtering enhancements | UI design: Filtering enhancements | Design sprint: New-client alerts | Design sprint: Dashboard export

*An example of a UX backlog in which only UX-related tasks are listed*

In this example, the product backlog and the UX backlog are independent. The UX backlog is made up of UX-related tasks that are created based on backlog items from the product backlog.

There will still be a primary product backlog with all of your new features, feedback, bugs, and so on. Your separate UX backlog will include all your different UX activities. It will be up to you and your product owner to make sure you’re working on the right things at the right time. Sometimes, UX may need to work on a task well before the rest of the team, in order to allow development to proceed with a sound solution. Coming back to the example above, if you see *New-client alerts* on the product backlog in sprint 3, you’ll want to make sure you complete the *Design Sprint: New-client alerts* well before development begins.

#### 

#### Pros

**UX is completely in charge of its own backlog.** The UX team is making decisions of what needs to get done and when, and it can plan for upcoming backlog items. Also, because UX works ahead of development, there will be less risk of holding up developers in a sprint.

**Separate UX backlogs can scale with multiple engineering teams and UX specialties.** If your organization has a large UX team with multiple specialties, each person can work on tasks that are relevant to her specialty. In addition, if your organization has multiple engineering teams working on the same product — iOS, Android, and web teams, for example — all of the UX tasks can live in one backlog to help maintain consistency across all teams.

#### 

#### Cons

**It is difficult to measure the overall team velocity.** Since UX works from a separate backlog, its velocity is not combined with that of the development team. (Some teams don’t consider UX as part of their team velocity, so this aspect may not be a con for you.)

**There is risk for working too far ahead.** When you’re planning ahead for the product backlog items, we recommend focusing most of your effort on the items that are in the current and next sprint. If your team is working further ahead on anything other than initial research, there is a large risk of losing work in the case that items are deprioritized.

## Conclusion

Your backlog structure may change from team to team and project to project. The great thing about backlogs is that you’re able and *required* to be flexible. Don’t be afraid to mix and match different methods until you find something that works for your team.
