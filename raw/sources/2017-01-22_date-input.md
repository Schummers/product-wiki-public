---
title: "Date-Input Form Fields: UX Design Guidelines"
date: "2017-01-22"
url: "https://www.nngroup.com/articles/date-input/"
author: "Angie Li"
topics: [applications, design-patterns]
type: article
---

Formatting a date-entry field may seem like a minor detail; however, even small interactions can draw a process to a standstill if implemented improperly. Poorly designed date input leads to distressed or annoyed users — risking the abandonment of the form altogether. Even worse, if the user specifies the wrong date, the entire transaction could be a disaster -- think, for example, how you'd feel if you showed up at the theater excited for a new show, only to discover that you bought tickets for a different day.

Considerations for users on mobile devices and for global audiences must be taken into account to improve this small, but fundamental input. This article discusses common input patterns, error handling, and international input for date fields.

## In This Article:

- [Date-Input Patterns](#toc-date-input-patterns-1)
- [Date-Input Design Guidelines](#toc-date-input-design-guidelines-2)
- [Conclusion](#toc-conclusion-3)

## Date-Input Patterns

Calendar pickers are control elements that display a full calendar month at one time. They typically show the days of the week across the top and match the metaphor of desk or wall calendars.

*Example of calendar picker on mobile shown on Google Calendar app*

Calendar pickers should be used for **events close to the present time** — within less than a year. However, they can be frustrating for users who choose dates far in advance because they require too much navigation to get to the desired input; for these users, it would be faster to simply type the year.

Calendar pickers are especially useful for selecting a date range. In those situations, they often display two months side by side.

![Examples/Revision%20Examples/Expedia%20Return%20-%20Highlight.png](https://media.nngroup.com/media/editor/2016/11/28/02-expedia.png)

*Expedia used a soft blue highlight to show the date range for the selected departure and return dates. The departure and return dates are colored differently in the calendar.*

- **Scrolling date pickers on mobile devices** are common, yet they can be annoying if the picker contains many dates. In those situations, scrolling in a small space is slow and unproductive; it’s better to allow users to type the date directly. In the Todoist app, users can enter the deadline for each task using an endless scrolling list. This is not an issue if the deadline occurs on that Friday or Saturday, as shown below, however, if the deadline is even a few weeks away it is easier for the user to type the date instead (a functionality that the app also provides). 

![Examples/Revision%20Examples/Todoist.PNG](https://media.nngroup.com/media/editor/2016/11/28/03-todoist.PNG)

*The iPhone Todoist app allowed users to scroll as well as type for date input. (Note the benefit of denoting the current date as “today:” it removes any uncertainty in case the user doesn’t remember today’s date.)*
- **Split date fields with drop-downs for month, day, and year** require a lot of unnecessary steps. This method increases [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) by adding additional clicks and scrolling. We advise against using this pattern. *DeviantArt provided drop-downs for each section of the date field.*
- **Typing the date** is the most basic option for date input, yet in many cases it is the most efficient one, especially when the date is further away in the past (e.g., birthdate) or future. We recommend that you allow users to type the date even if other input methods are available.

## Date-Input Design Guidelines

- **For a limited number of date options, provide a list of the applicable dates.** In some cases, users will have only few date choices. For example, Google Express, an online shopping service, makes it possible for customers to order groceries online and schedule a delivery time. Rather than offering blank date fields or a calendar picker of limitless options, Google Express provides a short list of date options. Any dates that are unavailable have been grayed out and disabled. (Alternatively, unavailable dates may not even be included in the list.) 

![../../../Downloads/express-date.PNG](https://media.nngroup.com/media/editor/2016/11/28/05-google-express.PNG)

*Google Express provided a drop-down with delivery options. The selection that is not available has been disabled and grayed out.*

In general, we don't recommend this method when there are more than 10 dates available however, as it can become tedious for people to scan and scroll through the list of dates.
- **Do not require users to enter special characters to format dates.**

Whatever format users chose for entering the date (dashes, spaces, slashes, dots between the month, day, and year components), their input should be recognized. Moreover, leftmost zeros should not affect the date. In the Priceline example below, the date 9-3-17 is rejected and 09/08/17 is accepted, although no format requirements were visible before submitting the form.

![../../../Documents/Priceline%20-%20Different%20Formats%20-%20Error%20](https://media.nngroup.com/media/editor/2016/11/28/06-priceline.png)

*Priceline rejected the date 9-3-17 without even providing suggestions on how to properly format it. Instead, it should have accepted it and parsed it for the user.*
- **Report errors appropriately.** If a user enters a date that is obviously a mistake, such as 11/81/17, do not make any assumptions. Give the user feedback and provide suggestions on how to resolve the error.
- **Remove illogical date options.** Prevent users from selecting illogical dates. Obviously, what’s reasonable will depend from case to case: for example, dates older than 130 years will be unlikely for birthdates, but quite acceptable for document dates. Users should be prevented from entering a return date that takes place before the departure date or that is in the past. Make the choices clear by disabling and graying out options that are not available or are illogical pairs.

- **Preserve users’ work.** If the same date information is required in a separate part of the form or later during a task, then don’t make users enter that date twice.
- **Keep date ranges consistent.** Avoid shifting date ranges for departure and return pairs. For example, if November—December is shown for departure, do not shift and show December—January for the return date range. The change may go unnoticed and [cause users to slip](https://www.nngroup.com/articles/slips/) by clicking where the intended date used to be. *Southwest Airlines shifted the return date range based on the**departure-date**selection. After selecting the departure date 8-16-16 from the July–August date range, the return date range changed to show August–September.*
- **If your site caters to international users, your date format should be clear and understandable.**

Date-entry fields are culture dependent, and can cause major problems for those users who are accustomed to a different format. “10/11/2016” could mean 11th of October 2016 to an American, but November 10th to someone from Europe. Follow these rules of thumb when designing date input for a global audience:

  - **Add labels and separate the fields** to make it clear which fields are for the month, day, and year. 

![../Google%20Drive/Articles/Date%20Input%20Format/Examples/dateandtime.PNG](https://media.nngroup.com/media/editor/2016/11/28/09-countdown-timer.png)

*This countdown timer separated the date components and labeled them clearly.*
  - **Spell out the name of the month** to distinguish it from the day. 

![../Google%20Drive/Articles/Date%20Input%20Format/Examples/tepwireless.png](https://media.nngroup.com/media/editor/2016/11/28/10-tep-wireless.png)

*The Tep Wireless site, where users can rent portable WiFi devices, spelled out the name of the month to serve its global audience.*

![eurostar-en.png](https://media.nngroup.com/media/editor/2016/11/28/11-eurostar.png)

*The Eurostar website, shown in English (US), supported several languages but did not say what date format it expected.  Here, the departure date could be read as July 2 or February 7.*
  - **Utilize calendar pickers with clearly spelled out names for months.**

Some frameworks, such as Bootstrap, provide calendar pickers to support unambiguous date selection.

![bootstrap calendar picker.png](https://media.nngroup.com/media/editor/2016/11/28/12-bootstrap.png)

*The Bootstrap calendar picker spelled out the name of the month, making it clear which date to select.*

![ctrip-english.png](https://media.nngroup.com/media/editor/2016/11/28/13-ctrip.png)

*The calendar picker on the English version of Ctrip did not spell the name of the month. Users had to infer that the month comes before the day.*

## Conclusion

Date-input patterns are not created equal. Implement design patterns that are appropriate for your context. When designing date-entry fields support text input and consider whether or not you have an international audience. Avoid designs that are ambiguous because they can cause people to become frustrated and annoyed with your site. Follow these guidelines to prevent form abandonment and catastrophic errors.
