---
title: "It’s Time We Addressed Time-Zone Selectors"
date: "2022-12-11"
url: "https://www.nngroup.com/articles/time-zone-selectors/"
author: "Kelley Gordon, Maria Rosala"
topics: [applications]
type: article
---

Time-zone selectors allow users to change the local time on a UI. They are commonly found in scheduling features, in the user-settings section of an application or website, and on websites that support live, virtual events — like our own. This article discusses findings from our research about how best to design a time-zone selector.

![A time-zone selector is open and the timezone for Berlin, Germany (GMT+2:00) is selected. The dropdown contains a search field and displays more timezones listed alphabetically by city.](https://media.nngroup.com/media/editor/2022/11/11/timezone-selector-virtual-events.png)

*Since we run live, virtual trainings, we implemented a time-zone selector to allow users to view the scheduled time of a course in a time zone of their choice. To understand how we should design our time-zone selector, we conducted several rounds of quantitative and qualitative research.*

Before jumping into the topic, it’s important to clarify some important terminology:

- A **time zone** refers to a **geographic region that shares the same time**. A time zone can be represented by a place (e.g., Berlin time) or as a collection of places that share the same time (e.g., Central European Time).
- An **offset** refers to the **difference in time from Universal Coordinated Time** (UTC). ([Universal Coordinated Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) is the main world standard for indicating time.) A geographical region can have different offsets at different times of the year if it observes daylight savings. For example, New York has an offset of UTC-04:00 in the summer and UTC-5:00 in the winter. An offset can be shared by more than one geographical region. For example, New York, Detroit, Washington DC, Miami, Toronto, and Havana all share the same offset.

## In This Article:

- [The Challenges of Designing Time-Zone Selectors](#toc-the-challenges-of-designing-time-zone-selectors-1)
- [Our Research](#toc-our-research-2)
- [Key Findings](#toc-key-findings-3)
- [Conclusion](#toc-conclusion-4)

## The Challenges of Designing Time-Zone Selectors

Usually, time zones are presented in a list such as a [dropdown menu](https://www.nngroup.com/articles/drop-down-menus/). Such a list could technically be sorted in several different ways:

- by offset
- by geographical region, such as continent
- alphabetically by country or city

Designing time-zone selectors can be tricky because:

- **Time zones can change**. A time zone can change its offset if it abides by daylight savings. This means that offsets in time-zone selectors need to be updated in real time when a time zone moves from standard time to daylight-savings time, and vice versa.
- There are many time zones to choose from, which means **dropdowns can be long and hard to scan**.
- There are lots of ways in which people think about their time zone (offset, city, or time-zone abbreviations like PST) so **choosing what to display in a time-zone selector can be challenging**.
- There is no universal way of organizing time zones.

Understandably, this is not a fun task for users. Participants in our recent research openly shared:

> “This is something that I hate doing in [sic] most websites.”
> 
> 
> 
> “​​I hate time zones. I hate having to select the time zone. I don't know why they always go wrong, especially when it comes to scheduling for me.”
> 
> 
> 
> “I'm terrible with time zones, like really bad.”

When reviewing some popular time-zone selectors, we found many different design approaches.

![The image shows an open timezone selector dropdown with the timezones Pacific Time, Mountain Time, Central Time, Eastern Time, and Alaska time displayed under a heading US/Canada. Next to each timezone is the current time.](https://media.nngroup.com/media/editor/2022/11/11/calendly-timezone-selector.png)

*Calendly displays time zones by region or continent. This approach results in fewer entries in the list (since multiple cities and countries share the same offset). North American time zones appear first on the list (Calendly is an American company) and, instead of the offset, the current time is displayed. A search feature allows users to search by items appearing in the list.*

![An open timezone selector dropdown displays timezones ordered by GMT. There is no search field, and at the top of the list 5 common time zones are shown.](https://media.nngroup.com/media/editor/2022/11/11/google-timezone-selector.png)

*Google Calendar’s time-zone selector is ordered by offset. Google displays departure from Greenwich Mean Time (GMT), which is technically a time zone, not a time standard. However, offset from GMT is identical to the UTC offset. The most frequently chosen time zones appear at the top of the list.*

![A preferences panel shows an open dropdown field under the label, Time Zone. The time zones in the dropdown are organized by UTC. The time zones are also clustered by cities that share the same offset. The selected time zone reads: UTC+1 Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna](https://media.nngroup.com/media/editor/2022/11/11/slack-timezone-selector.png)

*Slack’s time-zone selector is organized by offset. To reduce the length of the list, some of the time zones that share the same offset are grouped.*

## Our Research

To understand the best method of ordering and presenting time-zone selectors, we conducted:

- **2 rounds of remote, moderated usability tests with 13 participants** from 8 countries (UK, US, France, Belgium, Denmark, Germany, Australia, and UAE)
- **1 remote, unmoderated study with 83 participants** from 4 countries (US, Australia, UK, and Germany).

We wanted to learn:

- What users expect when interacting with a time-zone selector
- Which way of expressing time zones is more familiar (e.g., offset, time-zone name, city)
- What people’s strategies are when using a search field within a time-zone selector
- Whether grouping helps users to find their time zone in a dropdown

### Participants

We used UserInterviews.com to recruit participants for both studies. For our remote, unmoderated study, we recruited 83 people (42 men and 41 women, median age 37) from 4 countries: Australia (21 participants), the United States (22 participants), Germany (20 participants), and the United Kingdom (20 participants). We recruited from these 4 countries to control for and study any differences in behavior and familiarity with time zones across different geographical regions.

### Moderated Study Procedure

We ran 2 rounds of moderated tests using think-aloud protocol.

- In our first round, participants interacted with a prototyped version of our website created in Figma and were asked to find the scheduled time of a course in their time zone. Each participant interacted with two different versions of the time-zone selector. The aim of this study was to understand how best to implement a time-zone selector on the page and what participants expected from the feature.
- In our second round of moderated tests, we gave participants a link to a page with only a time-zone selector. These time-zone selectors were coded and fully functional (unlike the Figma prototype in the past round). Participants were asked to find their time zone. Each participant in this round experienced a grouped condition (in which time zones in the dropdown were grouped by continent) and an ungrouped condition (in which time zones were ordered by offset with no grouping). The order of the time-zone selectors was counterbalanced across participants.

### Unmoderated Study Procedure

Participants were invited to complete a 10-minute remote, unmoderated study in one sitting and were asked *not* to reference their phone or another browser tab during the study. The study was hosted on UserZoom.com.

The study began with a short questionnaire that included some questions about the participant’s location and time zone. Participants were also asked to rate their familiarity with certain time zones. Following the questionnaire, participants were given two tasks. In each task they had to find their time zone. One task displayed a search field and the other a dropdown. The order of the tasks was randomized.

To understand the effect of grouping time zones by continent, we randomly assigned participants to one of two conditions: grouped (in which time zones in the dropdown were grouped by continent) and ungrouped (in which time zones were ordered by offset with no grouping). We recorded participants’ time on task as the dependent variable.

As participants completed the tasks, their screen and audio were recorded, allowing us to identify any participants who cheated (by referring to another browser tab), experienced technical issues or disruptions, didn’t attempt the task, or had issues with the remote-testing software. These data points were removed or corrected.

## Key Findings

### Most Participants Know Their Time Zone

Participants were asked to write their current time zone in a text field. We analyzed and checked the responses and found that **most participants (73%) knew their own time zone**, sharing time zones such as *Pacific Time* or *European Central Time*. A small proportion (18%) shared the offset (e.g., *UTC -3*) rather than — or in addition to — a time zone. Interestingly, 3 of the 83 participants did not know their time zone or guessed their time zone incorrectly.

![A bar chart shows the types of entries given by participants when asked for their time zone. The sample size was 83. The bars, in order of high to low, read: Time zone, 61; Offset, 15; City, 6; Time, 4; Did not know / incorrect, 3.](https://media.nngroup.com/media/editor/2022/11/11/chart-type-of-entry.png)

*When asked about their current time zone, 61 participants (73%) offered the correct time zone (such as European Central Time). Less popular answers given were the offset (e.g., UTC+1) and cities (such as Berlin).*

### GMT Slightly More Familiar than UTC

We wanted to know whether participants knew their offset. In our initial review of time-zone selectors, we found that some designers chose to use [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time) (GMT) over UTC, so we wanted to explore whether one was more recognizable than the other. (Although GMT is a time zone, it is often used as a time standard since GMT’s offset is equal to UTC+0.)

We asked all our participants to identify the offset for their location in UTC and in GMT. The order of each question was randomized. 1 participant cheated by looking up their offset and so was excluded. Only a third of our 82 participants (34%) knew their time-zone offset in UTC, whereas over half of our participants knew their time in GMT (55%). This difference was statistically significant (p<.001). Given that GMT originated in the UK and the UK’s time zone *is* GMT for half of the year, we analyzed this difference by country. We found that the difference was statistically significant (p<.01) only for UK participants. In other words, **displaying offsets in GMT, rather than UTC, helped only the UK-based participants****and did not benefit people from the other 3 countries**.

![A chart shows the proportion of correct offset selections across countries. The chart contains two series: UTC and GMT. The countries displayed in the chart are Australia, Germany, the United Kingdom, and the United States. The chart shows that the proportion of correct offset selections was higher for all countries when offsets were displayed as GMT rather than UTC; however, the difference in correct offset selections was only significant for the United Kingdom as shown by errors bars which represent the 95% confidence interval.](https://media.nngroup.com/media/editor/2022/11/11/offset-selections-by-country.png)

*The chart shows the proportion of correct selections when participants from all four countries were shown offsets in GMT versus UTC. Error bars show the 95% confidence interval. While all groups had more correct selections in GMT than UTC, only the difference in the UK group was statistically significant.*

We also asked participants to rate the familiarity of GMT and UTC. **Participants rated GMT as more familiar than UTC**. The average familiarity rating for GMT was 3.6 (where 1 was *not at all familiar*, and 5 was *very familiar*), whereas the average familiarity rating for UTC was 2.3. This difference was statistically significant (p<.001). Even when removing UK participants, the average familiarity rating for GMT (3.2) was higher than UTC (2.3). This difference was statistically significant (p<.01). This means, while displaying offsets in GMT doesn’t necessarily help non-UK audiences locate their offset more accurately, seeing offsets expressed as GMT may seem more familiar to users.

Despite GMT being rated as more familiar, almost half of our participants did not know their offset, which means **communicating the offset alone is not enough**. Many participants commented that they didn’t know much about offsets:

> “I never pay attention to these.”
> 
> 
> 
> “I'm not sure, honestly never had to think of UCT (sic) or GMT as time zones or the meaning of the letter initials themselves”
> 
> 
> 
> “I know it’s Chicago/Central, but that’s all I know”

As participants interacted with the dropdown organized by offset, they struggled to find their time zone in the list and many participants from all countries in our studies **expected the list to be ordered alphabetically**.

> “I found it strange that it was grouped by kind of like location rather than alphabetical order.” Australian participant in our unmoderated testing
> 
> 
> 
> “I would have thought it would have been in alphabetical order as opposed to it didn't seem to be in any order. Actually, it was in order of UTC (....) I would expect [London to be under] L (…) halfway through the lot.” UK participant in our unmoderated testing
> 
> 
> 
> “It was difficult because they are not how I expected it to be because it wasn't sorted alphabetically, which is normally the case, but it was sorted based on the time zone.” German participant in our unmoderated testing
> 
> 
> 
> “I've used a lot of these dropdowns before. Like I think it's on Google calendar and I have to scroll down the whole list to find a city because most of the time, I don't really know the GMT time for each city. I don't even know. I think for Paris it may be plus one, but I'm not, never even that sure.” French participant in our moderated testing
> 
> 
> 
> *“* I think I prefer that [being organized alphabetically] because that's a more familiar grouping to me than the time zones (....) ‘Cause I don't know the times on offhand and the other one assumes that I would know that. And it's just like more mental gymnastics to stop and pause looking for it when it's sorted by time zone versus by alphabet.” US participant in moderated testing
> 
> 
> 
> “So, it comes up with the time zone first and then the location. Okay, so this is where I have to do some more thinking in my head, in my opinion, just because I need to work out, which time zone I’m in, which usually isn't very hard because UK, London time is zero usually, but we've just put our clocks forward, which means we're plus one, but I have to go through this thinking process in my head.” UK participant in moderated testing

Based on our findings, we recommend you **avoid organizing time zones by offset**. If you do organize by offset, list the offset first to help users quickly understand how the list is ordered. When we presented participants with time zones ordered by offset but had the offset trailing the time zone, participants did not understand how the list was ordered. One participant from the UK could not understand the ordering and felt she had to look through every entry.

> “So, this one is it's not even alphabetical. What is it? Yes, it's alphabetical until you get to… No, it's just a mishmash; slightly alphabetical but not properly. You've got to look at every single entry, which is scattered all over the world…”

### Users Often Want to Search

When we gave participants the task to use a dropdown to find their time zone, we deactivated the search field so that participants had to scroll. Nearly all our participants tried to search the dropdown and either expressed dissatisfaction when this was not possible or wished they could search.

> “It would be really cool if I can just search for it, you know?” Participant from UAE in our moderated session

Since time-zone lists are long, users find it more efficient to perform a search for the time zone (if they know it).

> “I think having the search bar at the top is very helpful. I think that’s just going to be **something I would use first** before scrolling through this window to find, you know, where I am in America.” US participant in one of our moderated sessions.

Several participants mentioned that they do a lot of tasks that require them to use time-zone selectors on their phones and search helps a lot with these tasks.

If possible, **provide a search field within the dropdown**. Most users will use this functionality to locate their time zone, rather than scrolling through the dropdown. Make sure that the search field is visible so that the functionality is discoverable — for example, by showing the search field as an "option” at the top of the dropdown field when that field is selected.

![Two timezone selector fields are shown side-by-side. The first timezone selector dropdown contains a visible search field. In the second timezone selector dropdown, the dropdown field itself becomes the search field.](https://media.nngroup.com/media/editor/2022/11/11/timezone-selector-search.jpg)

*A separate search field within the dropdown (left) helps users discover the search feature. In contrast, enabling search within the dropdown field (as shown right) makes it less discoverable.*

![Two timezone selector fields are shown side-by-side. The first timezone selector dropdown contains a visible search field. In the second timezone selector dropdown, the dropdown field itself becomes the search field.](https://media.nngroup.com/media/editor/2022/11/11/timezone-selector-search-mobile.jpg)

*A separate search field within the dropdown (top) helps users discover the search feature. In contrast, enabling search within the dropdown field (bottom) makes it less discoverable.*

In addition to these specific recommendations for implementing search within the dropdown field, many [search best practices](https://www.nngroup.com/videos/designing-search/) apply, such as displaying [search suggestions](https://www.nngroup.com/articles/site-search-suggestions/) or **filtering the dropdown in real time** as the user types.

![Timezone selector shows a search field where the user has begun to type San J. Two suggested results are shown: San Jose, Costa Rica, and San Juan, Peurto Rico.](https://media.nngroup.com/media/editor/2022/11/11/timezone-selector-search-typeahead.jpg)

*Providing search suggestions or real time results can support users in finding their time zone quickly. It can also help users understand what kind of queries will be accepted.*

### A City Was the Most Common Search Query

In the search task, we provided a search field with the dropdown deactivated (so participants couldn’t inspect the list or scroll through it) and asked participants to find their time zone. We analyzed the type of query that was first executed by participants. **The most-common first query was a city**.

![A bar chart shows participants' First Seach type. In order of high to low, the bars read: City, 33; Time zone, 18; Offset, 9; Country, 9; State, 4; Other, 2.](https://media.nngroup.com/media/editor/2022/11/11/chart-first-search.png)

*The most common first search query made by 75 participants was a city (44% of first search terms), followed by a time zone, such as Pacific Time (24% of search terms).*

Despite cities being the most popular search term, they may not always be the most successful search strategy. The 33 participants who used a city as a search strategy made on average 2.5 search attempts. This was because sometimes a city was not in the list of time zones, and so users had to execute a different, often broader, search query to find their time zone.

Not all your users will live in a central city or know the right city for their time zone, so it’s a good idea to **allow users to also search by country (and state if possible).**

> “So, I knew that by typing in ‘Brisbane’, I’d probably find it given I live in the capital city. I think if I didn’t live in Brisbane, I’d just go ‘Australia’ and then navigate through that way.” Australian participant in moderated testing

**Showing the country and offset (alongside the city)****can provide extra confirmation** that the selected time zone is the correct one.

> “Maybe there would be a need for the country because I know Adelaide because I’ve lived in Australia for 10 years, but I think most people wouldn’t really know. So maybe [...] it would be nice to have the confirmation: ‘[Adelaide], Australia’; ‘Lisbon, Portugal’.” French participant in moderated testing

Given that many people know their time zone (like Pacific Time) and some use it as a search strategy, **you can also provide common time zones** as discrete options or alongside cities, such as *New York (Eastern Time).* However *,***don’t use the time zone and offset alone**(e.g., Pacific Time, *GMT-8*). While most participants in our study knew their own time zone, users might not know the time zone (or offset) of another location.

### Time-Zone Lists: To Group or Not to Group?

In our remote unmoderated test, we compared two offset orders: one **grouped by continent and one with no grouping**. In the grouped condition, the time zones were ordered by continent first (with continents listed in alphabetical order), then, within each continent, they were ordered by offset. In the ungrouped condition, the time zones were ordered by offset. The search functionality was removed so that participants had to scroll to find their time zone. An equal number of participants from each country were randomized to either the grouped or ungrouped condition.

*Half of our participants were randomly assigned to either the ungrouped condition (left) or the grouped condition (right). Both dropdowns were ordered by offset and functioned identically.**Half of our participants were randomly assigned to either the ungrouped condition (top) or the grouped condition (bottom). Both dropdowns were ordered by offset and functioned identically.*

We asked participants to find their time zone from the dropdown and we recorded how long it took them. The median completion time for the 37 participants successful in the grouped condition was 39 seconds, and the median completion time for the 40 participants successful in the ungrouped condition was 47 seconds. This difference was not statistically significant. Since each participant’s time zone would appear in a different place in the list, we compared the relative speed to select a correct time zone by dividing the time on task by the participant’s time zone’s position in the dropdown. The relative median time for the grouped condition was 0.29 seconds and the relative median time for the ungrouped condition was 0.52 seconds. This difference was statistically significant (p<.001). This means that **when time zones were ordered by offset**, **grouping helped participants to find their time zone more quickly**. Since participants struggled to locate their time zone when time zones were ordered by offset, the presence of grouping may have helped participants locate the right area of the dropdown quicker.

Many participants commented that they **liked seeing the time zones grouped by continent**. For example, an Australian participant commented:

> “I do like how it’s sorted by region. That makes it a lot easier than if it was just all the cities in the world put on the list. So, it is good that it’s broken down by region…”

A participant from the UK who had dyslexia mentioned that she found the grouped dropdown easier to scan because of the added spacing.

Some participants from Europe and the US expressed dissatisfaction with the grouping; this was because our grouped dropdown had continents and regions ordered alphabetically, which resulted in participants from Europe and the US needing to scroll past continents like Africa, Asia, and Australasia first. Some participants commented that they would like to see their continent first or higher up the list. We did not test placing the most popular continents first. Had we done so, it’s possible that these participants may have found their time zone earlier in the dropdown.

If you do pursue grouping time zones, consider who your main audience is. **Place continents or regions that most of your customers are in at the top of the list**, like in Google’s or Calendly’s time-zone selectors.

One limitation of our analysis is that we did not test grouping in alphabetically ordered time-zone selectors, and so we don’t know whether grouping helps participants locate their time zone faster in such cases.

### Participants Expect the Dropdown to Locate Their Time Zone

Many participants wished they could see their time zone highlighted in the dropdown as they first interacted with it. “I wish this was smart enough to find my geolocation or at least guess,”**a Danish participant in our moderated testing said.

To do this, either present the location as a default in the dropdown field and allow users to change it or have the dropdown automatically scrolled to the point of the user’s location and show the location shaded in the list.

![Two versions of a timezone selector dropdown show Los Angeles, California preselected. In version 1, Los Angeles appears at the top of the list and separate from the rest of the timezone list. In version 2, Los Angeles is highlighted in the list of timezones, and the dropdown is prescrolled to time zones that begin with the letter, L.](https://media.nngroup.com/media/editor/2022/11/11/timezone-selector-default-location.jpg)

*Where possible, display the user’s location at the top of the list, such as shown on the left. Alternatively, open the time zone selector at the user’s location (as shown right).*

![Two versions of a timezone selector dropdown show Los Angeles, California preselected. In version 1, Los Angeles appears at the top of the list and separate from the rest of the timezone list. In version 2, Los Angeles is highlighted in the list of timezones, and the dropdown is prescrolled to time zones that begin with the letter, L.](https://media.nngroup.com/media/editor/2022/11/11/timezone-selector-default-location-mobile.jpg)

*Where possible, display the user’s location at the top of the list (as shown top). Alternatively, open the time zone selector at the user’s location (as shown bottom).*

## Conclusion

There are many ways to design a time-zone selector. Here’s a summary of our research findings:

1. Most users don’t know their offset and struggle to find their time zone when time zones are ordered by offset.
2. The most typical search strategy is by city, followed by a regional time zone (like Pacific Time).
3. GMT is a more familiar time standard than UTC (even though UTC is the correct time standard). However, using GMT doesn’t help participants find their correct offset (except for a UK-based audience).
4. Grouping time zones by continent helped participants find their time zone faster when time zones were ordered by offset.

Given our research, we recommend the following when designing time-zone selectors:

1. Where possible, identify the user’s time zone based on their location and allow them to change it if they need to.
2. Provide a way for users to search a time-zone selector. Make search easily discoverable by displaying a search field when the dropdown field is active.
3. Organize time zones alphabetically by city and make sure to display the country (and state if relevant) as well as the offset.
4. Where possible, allow users to be able to search by larger time zones (such as Pacific Time).
5. When grouping time zones by region or continent, consider displaying common regions at the top of the list.
6. Consider using GMT instead of UTC offsets if designing for UK audiences.
