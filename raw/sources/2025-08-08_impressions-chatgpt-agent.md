---
title: "Initial Impressions of ChatGPT’s Agent: Successful, Shaky, and Slow"
date: "2025-08-08"
url: "https://www.nngroup.com/articles/impressions-chatgpt-agent/"
author: "Evan Sunwall"
topics: [ai]
type: article
---

OpenAI recently released its agent mode for ChatGPT. Agent mode enables ChatGPT to navigate and manipulate websites designed for human use. This article documents my first impressions of this new interaction paradigm.

While this tool represents a significant step towards mainstream AI-agent use, my simple evaluation revealed that agentic AI still has a long way to go.

*Note:* On August 7 2025, OpenAI released GPT-5, the successor to the company’s collection of previous models. OpenAI’s Agent Mode was not updated alongside GPT-5, as they are separately developed AI models.

## In This Article:

- [The Task: Book a Business Lunch](#toc-the-task-book-a-business-lunch-1)
- [Step 1: Search for Restaurants](#toc-step-1-search-for-restaurants-2)
- [Step 2: Access the Restaurant Website](#toc-step-2-access-the-restaurant-website-3)
- [Step 3: Clarify the Guest Count](#toc-step-3-clarify-the-guest-count-4)
- [Step 4: Book the Reservation](#toc-step-4-book-the-reservation-5)
- [Step 5: Enter Details with Human Intervention](#toc-step-5-enter-details-with-human-intervention-6)
- [Step 6: Submit Reservation](#toc-step-6-submit-reservation-7)
- [Step 7: Confirm Reservation](#toc-step-7-confirm-reservation-8)
- [Overall: It Worked, But Beware the Caveats](#toc-overall-it-worked-but-beware-the-caveats-9)

## The Task: Book a Business Lunch

*Watch a recording of this interaction (about 5 minutes). This is a ChatGPT replay of this agent interaction; it's sped up and does not depict the actual duration I experienced.*

I chose the everyday task of booking a restaurant reservation. This was my starting prompt to ChatGPT:

> Find a restaurant suitable for a business lunch near 3100 Travis St, Houston, TX 77006 for next friday at noon.

Is this a [high-quality prompt](https://www.nngroup.com/articles/careful-prompts/)? No.

I kept it terse and deliberately omitted relevant details to simulate real-life use of everyday people who don’t fancy themselves as “prompt engineers.” (Writing highly detailed prompts poses a high [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) on users. In some of our recent studies of the prompting strategies of consumers, we’ve noticed that even experienced genAI **users rarely include sufficient context and criteria** in their first prompt.)

Remember that **the computer should adapt to the needs of the human, and not the other way around.** I wanted to evaluate what this agent could perform with minimal handholding from a rushed and distracted user.

This realistic-yet-weak prompt should have encouraged ChatGPT to request additional details before beginning. For example:

- **What does “suitable” mean here?** Are you going to talk with a prospective job applicant and want a quiet venue? Are you trying to impress a client's executive staff with something fancy?
- **What’s the budget for the meal?** Is this a casual lunch with a peer, or an expensive celebration?
- **How will people be arriving?** What’s more important: ample parking or access to mass transit?
- **What type of food?** Do attendees have preferred cuisines or dietary restrictions?
- **How many attendees?** Is this a 1-on-1 meeting, or will you need to rent out a private room in the restaurant?

**Instead of asking any of these clarifying questions, ChatGPT jumped immediately into the task with limited context.** It focused on the necessary geographic proximity and operating hours but didn’t ask followups on relevant topics that would have significantly influenced its subsequent searches and suggestions. This behavior struck me as unusual, since ChatGPT’s “deep research” mode always asks clarifying questions before investing 8–15 minutes researching and writing a report.

## Step 1: Search for Restaurants

ChatGPT spent 6 minutes conducting research on various restaurants by performing 10 web searches utilizing 96 sources — far more than any human could reasonably use to find a lunch spot for a business meeting. (Though, arguably, a human might not need to consult 96 different sources to make a well-informed decision.)

ChatGPT’s search used mostly sensible sources for the task: Yelp, OpenTable, Instagram, and various restaurant-focused sites, and it took screenshots to document the process. ChatGPT did mention encountering some difficulties using these sites, such as dynamic features, anchor links that interfered with scrolling, and even the dreaded popup-upon-arrival.

![A pop-up message appears over the homepage of the ŌPORTO Fooding House & Wine website. The pop-up announces happy hour hours—“3:00–6:30 Happy Hour Monday–Friday”—and includes a link labeled “DA GAMA CANTEEN,” referencing the restaurant’s sister location. In the background, the site’s homepage features overhead photos of food and drinks, such as seafood dishes, charcuterie, and a glass of red wine. The navigation menu behind the pop-up includes links for menus, reservations, events, and online ordering.](https://media.nngroup.com/media/editor/2025/07/30/chatgptagentpopup.jpg)

*ChatGPT had to locate and trigger the ‘Close’ button on a disruptive popup before using a website. It probably experienced 100% less annoyance in this task than a human might.*

Excerpts of ChatGPT’s documented “thinking” during this process:

> The open table [sic] might be inaccessible due to dynamic features or cross-late issues. I'll use the computer tool to open it and bypass these limitations.

> It seems that scrolling has not progressed as expected, likely due to an anchor.

> A pop-up about Oporto is showing, and I need to close it by clicking the 'x'. I'll use the multi-action function to click the cross and close the pop-up window.

ChatGPT eventually suggested 3 restaurants that are viable candidates for a business lunch, based on my expertise as a Houston local. It created a table containing the following information:

- Cuisine category
- Atmosphere
- Location (with distance from prompted address)
- Business hours
- Justification

There are a few glaring omissions in this list, though: What’s on the menu and how much will it cost?

It would be hard to choose a restaurant based on this information alone, and navigating directly to the restaurant’s website was a little difficult. Sometimes the embedded sourcing pills would link to the mentioned website, but, if the source was a screenshot, it would instead display an image preview that, when clicked, included a link to the website. I found this inconsistent behavior unintuitive.

![This image shows a side-by-side comparison of three Houston restaurants, highlighting why each is a suitable choice for a business lunch. The top listing, Brennan’s of Houston, is marked as the recommended choice due to its elegant, white-tablecloth setting and top-tier Creole/Cajun cuisine. Its hours (Mon–Fri, 11 a.m.–2 p.m.) are emphasized, along with a notable 25-cent martini lunch special. Two alternatives are listed below: Josephine’s Gulf Coast Tradition, offering casual Gulf Coast seafood in a polished setting, and Oporto Fooding House & Wine, a stylish option with Portuguese-inspired small plates. Each listing includes cuisine, atmosphere, location, hours, and why it suits business dining.](https://media.nngroup.com/media/editor/2025/07/30/chatgptagentscreenshotsourcing.jpg)

*ChatGPT took screenshots of each website’s operating hours and included them in its results. It didn’t have much to say about the restaurant menu or prices, however.*

These screenshots are an effective sourcing technique (an important tactic for trust building with users, which we discuss in our course [Designing AI Experiences](https://www.nngroup.com/courses/designing-ai-experiences/)), but more direct access to the websites would have been helpful.

## Step 2: Access the Restaurant Website

I responded to this table with a choice and direction:

> Let’s book a table at Brennan’s.

After I prompted with the desired restaurant, ChatGPT **spent a surprising 55 seconds attempting to access the restaurant’s website.** It appears it was redirected to a Google Maps page, but it resolved this issue on its own.

![a ChatGPT interface where the user has prompted, “Let’s book a reservation at Brennan’s.” The assistant responds by explaining two steps. First, it notes a technical issue: the Brennan’s website redirected to Google Maps instead of loading the correct page, so it plans to retry using HTTPS to reach the hours and location page. Second, it states the need to confirm the number of attendees for the business lunch, assuming a default of two people but indicating it will ask the user to specify. The assistant also mentions it will collect contact information once the guest count is confirmed.](https://media.nngroup.com/media/editor/2025/07/30/chatgptagentgooglemaps.jpg)

*It’s unclear why ChatGPT was sent to a Google Maps page — perhaps it may have interacted with a Google Maps link found on the restaurant website’s* About *page. It was also unclear why these interactions required nearly a minute to complete.*

## Step 3: Clarify the Guest Count

ChatGPT then determined that clarifying the guest count was important before proceeding.

I replied with 2 guests but then decided to add a twist: I mentioned that 1 had a shellfish allergy. (Remember, typical users won’t behave methodically and logically! In these agentic interactions, they’ll likely share information whenever it occurs or is asked of them. And they still might not answer with total clarity. I didn’t tell ChatGPT *who* had the shellfish allergy, and it didn’t ask.)

## Step 4: Book the Reservation

With the restaurant selected, guest count confirmed, and website open, ChatGPT was ready to book the reservation. This step was the most surprising step for several reasons.

![A ChatGPT interface where the assistant is helping navigate a reservation form for Brennan’s of Houston. The screenshot highlights the reservation page displaying the restaurant’s name and dress code, which requests business casual attire and discourages athletic wear or shorts. In the center of the page is a time selection menu showing available reservation times starting at 10:15 a.m. A note from the assistant appears as a caption, stating that it needs to scroll slightly to reach the desired 12:00 p.m. time slot and will do so carefully to ensure it selects the correct midday option.](https://media.nngroup.com/media/editor/2025/07/30/chatgptagentscrolling.jpg)

First, it took an unusually long time. ChatGPT needed 11 minutes to navigate the restaurant’s web forms, whereas it took me about 2 minutes to perform the same workflow at a casual pace. (Not exactly the magical time saver that AI agents are often purported to be.)

**ChatGPT took so long to complete the process that the 10-minute window to hold a****table reservation technically timed out**. Fortunately, the website processed the reservation anyway, but if the restaurant had been receiving lots of reservations, it could have been rejected and the process would have needed to pivot.

Second, ChatGPT had **some difficulty manipulating the dropdown time selector**. It had trouble scrolling the list to make 12:00 PM visible within the viewport, and then mis-clicked 12:15. To ChatGPT’s credit, it noticed the mistake and clicked 12:00 PM instead, but the agent might experience some challenges, or at least slowdown, with some selector-control implementations.

Third, when the search results returned possible reservations, 12:00 PM was unavailable. **ChatGPT then decided to select a 12:15 timeslot instead** and warn me about the change. It even correctly noted alternatives at 11:45 AM and 12:30 PM, too, but if noon had been a firm requirement, then this process would have, again, had to make a big, slow detour.

![A restaurant reservation interface for Brennan’s of Houston, with available time slots for Friday, August 1. The screen presents multiple options, including 11:45 a.m., 12:15 p.m., and 12:30 p.m., with variations for lunch, bar seating, and outdoor seating. A cursor is hovering over one of the 12:15 p.m. lunch options, suggesting a selection is being made.](https://media.nngroup.com/media/editor/2025/07/30/chatgptagentreservationselection.jpg)

Finally, and **most impressively, ChatGPT accounted for the shellfish allergy successfully.** It identified dietary restrictions as the appropriate option in the booking form and selected the appropriate choice. I didn’t intentionally specify which guest had the allergy, so it defaulted to me.

ChatGPT handled the ambiguity and was able to select from an unconventionally styled [array of toggle-switch controls](https://www.nngroup.com/articles/toggle-switch-guidelines/). The [modal window](https://www.nngroup.com/articles/modal-nonmodal-dialog/) containing these controls also used unconventional positioning of the *Cancel* and *Save* buttons (at the top of the window’s frame instead of the bottom). Could this mean that agents might be less affected by unintuitive designs than humans? Could there be designs that stymie agents but remain usable for humans? The similarities and differences will be intriguing to explore in the future.

![a ChatGPT interface where the assistant is helping book a restaurant reservation. A screenshot at the top displays a reservation form with a list of dietary restrictions for both the user and their guests. “Shellfish” has been selected as a restriction. Below the image, the assistant explains it chose the nearest available time slot—Friday, August 1 at 12:15 PM—because noon was unavailable. It notes the shellfish allergy, and outlines that the user must now enter their contact details and agree to the venue’s policy.](https://media.nngroup.com/media/editor/2025/07/30/chatgptagentdietaryrestrictions.jpg)

*Interestingly, ChatGPT also included an optional note mentioning that one of the party members had a shellfish allergy, which certainly never hurts to reiterate when your dining companion’s well-being is at stake.*

## Step 5: Enter Details with Human Intervention

Next, ChatGPT correctly identified that I needed to complete the remaining portion of the web form since it involved personal information that I had not previously provided. In agentic AI, this referred to keeping the “human in the loop.”

> **Human-in-the-loop** is an agentic AI design strategy that aims to keep humans actively involved in decision making, instead of letting the agent make choices and act autonomously.

The “takeover” process was straightforward, but the web-browser window was seemingly low-resolution. I couldn’t find a way to resize it, but I was able to enter the necessary details.

![A reservation summary screen for Brennan’s of Houston on the SevenRooms booking platform that is being controlled by the user and not the agent. The reservation is set for Friday, August 1 at 12:15 p.m. for 2 guests. A shellfish allergy is noted under dietary restrictions, and a matching comment appears under “Reservation Notes.” Below, two required checkboxes confirm agreement with the venue’s policies—such as the business casual dress code—and the option to receive reservation updates via text.](https://media.nngroup.com/media/editor/2025/07/30/chatgptagentusercontrol.jpg)

*I entered my personal information in ChatGPT’s cramped browser window before the agent submitted the reservation.*

## Step 6: Submit Reservation

Once I handed back control to ChatGPT, it took a minute to review the completed form and then ask me *Shall I go ahead and submit [the reservation] now?*

![A nearly completed online reservation form for Brennan’s of Houston, scheduled for Friday, August 1 at 12:15 p.m. for 2 guests. The form includes personal information fields at the top—first and last name, email, phone number, birthday, and postal code—with some fields filled out. ChatGPT is requesting permission from the user to submit the reservation.](https://media.nngroup.com/media/editor/2025/07/30/chatgptagentdecisiongate.jpg)

*ChatGPT requested final approval before submitting the reservation on my behalf.*

Once again, ChatGPT was effectively keeping the human in the loop at a decision gate.

> **Decision gates** are points where an agentic AI requests confirmation from a human before taking significant actions with potential adverse consequences.

## Step 7: Confirm Reservation

Once permission was given, ChatGPT took another 2 minutes to submit the form and confirm the reservation.

ChatGPT recognized that the reservation window had technically expired, which may have slowed its processing, but the restaurant website was seemingly quick and responsive otherwise, so the delay was probably with ChatGPT.

## Overall: It Worked, But Beware the Caveats

With the reservation confirmation in my inbox (that sadly will have to be cancelled even though it’s a nice restaurant), ChatGPT’s agent mode was successful. Despite being given a weak user prompt, ChatGPT performed some research, found a suitable restaurant, prepared the reservation, and successfully submitted and confirmed it.

**But the process was very slow,** and it’s important to notice the shaky ground it rests on. Some early probing by ChatGPT could have revealed critical information, such as a food allergy, that might have altered the entire trajectory of the chat.

While it surfaced some useful information, it hewed too heavily on the initial prompt and not enough on the practical details that a restaurant patron would need to know to make an informed dining decision. **Pivots and dead ends,** like a restaurant that is over budget, serves incompatible food, or is unavailable, would have incurred even more delays.

**The halting process over a simple web form implies that more complex experiences would be more error-prone and slow.** Plus, any agent handling payment or personal information must keep the user in the loop. While this practice mitigates serious errors, it also **erodes the agent’s value proposition,** and there’s no guarantee that the agent will correctly identify these situations to begin with.

![A completed reservation for two guests at Brennan’s of Houston. The confirmation page shows a message stating, “We look forward to welcoming you,” with details sent to the user’s email. It lists the name of the user, the restaurant name, the reservation date (Friday, August 1), time (12:15 PM), and party size (2 guests).](https://media.nngroup.com/media/editor/2025/07/30/chatgptagentcompletion.jpg)

### Conclusion

Although just a single anecdotal experience, this author sees ChatGPT’s agent mode as an impressive milestone. But to handle the rigors of everyday use, this agent mode will need to be more inquisitive, much faster, and demonstrate reliability over the long term. Still, we’re entering a new era of computing where machines are becoming fellow users alongside humans.
