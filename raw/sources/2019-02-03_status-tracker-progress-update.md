---
title: "Status Trackers and Progress Updates: 16 Design Guidelines"
date: "2019-02-03"
url: "https://www.nngroup.com/articles/status-tracker-progress-update/"
author: "Maria Rosala"
topics: [e-commerce, email]
type: article
---

When users buy a product or apply for a service online, they don’t have control over the completion of that process — the delivery of the product or the service. (In this article, “delivery” refers to both physical shipment and virtual or online service delivery.) Lack of control can cause some anxiety, even more so when the product is expensive, sensitive or sentimental, or is needed urgently. Users also need to be informed of the progress of their application for a service — be it a new passport or a new mortgage.

Good [service design](https://www.nngroup.com/articles/service-design-101/) doesn’t just leave users in the lurch. Instead, status trackers and timely progress updates can reduce their anxiety, by [making the status of the delivery of that product or service visible](https://www.nngroup.com/articles/visibility-system-status/). Status trackers and progress updates are so prevalent now, that users expect them. For the organization, these features reduce [customer-service requests](https://www.nngroup.com/articles/customer-service-model/) (and thus save time and money), leading to a better [relationship with customers](https://www.nngroup.com/articles/loyalty-on-the-web/).

## In This Article:

- [Status Trackers Versus Progress Updates](#toc-status-trackers-versus-progress-updates-1)
- [Design Guidelines](#toc-design-guidelines-2)
- [Status Tracker Design Guidelines](#toc-status-tracker-design-guidelines-3)
- [Conclusion](#toc-conclusion-4)

## Status Trackers Versus Progress Updates

A **status tracker** is an online or app-based feature for tracking the progress of the delivery of a product or service. It usually consists of the latest status and prior updates, displayed in chronological order. If you’ve ever bought anything online or used a shipping company (like FedEx), you’ve probably seen a status tracker before.

*FedEx’s status tracker displays the delivery date and a progress-bar graphic. The previous updates are found under the* Travel History *section.*

**Progress updates** are notifications sent (via SMS, [email](https://www.nngroup.com/articles/state-transactional-email/), or social-media channels) by the company or service provider when the status of the delivery has changed — such as when an item has shipped or a decision on an application has been made.

*J.Crew sends users progress updates via SMS. It’s helpful that the update includes a link to the status tracker.**Gilt.com, an online retailer, emails customers delivery updates. The email contains an image of the product being delivered, which helps users recognize which of their purchases the update pertains to.*

![A user receives a message in WhatsApp from Deliveroo, which says "Your rider is Claudio. They've just picked up your order from Giraffe. They'll be with you soon."](https://media.nngroup.com/media/editor/2019/01/25/deliveroo-progress-update.jpg)

*Deliveroo, a fast-food–delivery company, uses WhatsApp to send users progress updates on the delivery of their takeout.*

Some differences between status trackers and progress updates are presented in the table below.

Status trackers | Progress updates | Purpose | Pull: Users can check progress at their own convenience. | Push: Users find out about changes in the state of the delivery process when they happen. | Content | Trackers contain specific details about the delivery process. | Depending on security, privacy, and user approval, the notification may contain the exact details of the update or generic text and a link to the status tracker for details. | Access | Users access a unique link or log into a secure site or app to view the status. | Users typically receive an update via SMS, email, or social channels such as Facebook Messenger or WhatsApp. | Longevity | Users can see past updates. | If users lose or cannot find their old messages, they may not be able to see past updates. | Contact details required? | No user contact details are required, but users often need a reference number or unique link to access the status tracker. | The organization needs to have collected users' contact details and obtained permission to send notifications. Moreover, details need to be correct for the user to receive the updates. | Recipient | Anyone who has the information needed to access the tracker (e.g., order number) can see the updates. | Only the email/phone number that was subscribed to notifications receives them.

It’s a good idea to **offer both a status tracker feature and progress updates**. Having only a status tracker may induce anxiety, as users end up obsessively checking the tracker to see if there has been a change since they last checked. However, only having notification updates could be problematic if users type their email address incorrectly or change their phone number and don’t receive the updates as a result.

Additionally, some users don’t like to be interrupted with notifications and prefer to check progress on their own terms. The status tracker acts as both a safety net and a place where users can add or change contact details and communication preferences.

## Design Guidelines

Poorly implemented status trackers and progress updates can create unhappy customers and increase calls to customer support. Following best practice guidelines and conducting early usability testing will ensure the features you develop meet user needs and [return on investment](https://www.nngroup.com/articles/return-on-investment-for-usability/).

## Status Tracker Design Guidelines

**1. Allow users to find tracking information from their customer account.**

If users have an account with your company, then ensure they can find tracking information from within their account. This makes it much easier for customers to track, as emails from the shipping company can be easily lost in an inbox.

Many companies decide to use their own site-embedded trackers instead of simply directing users to the tracker provided by the shipping companies (such as UPS or FedEx). There are some advantages to doing so, but also some serious downsides. The big advantage is that people can be kept on the site and the site will control the quality of the experience (which may vary depending on the carriers being used to deliver the service). The downside is that users may already be used with the trackers provided by the big shipping companies; plus, they may also be able to customize their delivery using those trackers (for example, by choosing a different delivery day or a nearby delivery address) — a feature that most companies will not be able to provide on their site. If you do offer an embedded tracker, **make sure that it does link to the shipping company’s tracker,** in case people want to modify their delivery.

Amazon uses a combination of different shipping suppliers to deliver products to its customers.

*Amazon offers users the ability to track their packages on its site. This feature saves users the effort to search their emails to find a link to the shipping company for tracking.*

**2.****The status tracker should prioritize information related to the latest update.**

Don’t clutter the status tracker with unnecessary information. Keep related links and information visually distinct, to aid users hunting for a mere update. Present the latest update prominently, so users can find it first.

![The most important information for the user, which reads: "We have finished processing your passport, and it has been mailed to you" is found in the 3rd paragraph of a section of text.](https://media.nngroup.com/media/editor/2019/01/25/travel-state-tracker.jpg)

*The U.S. Department of State provides a status tracker for customers who would like to check the status of a new passport. The status isn’t immediately obvious, as it is buried in a section of text.**UCAS.com manages student admissions to universities in the UK. UCAS’ status tracker consists of a vertical log of updates with the most recent at the top. Each item shows the date and time. The text is helpfully customized with the university and program.*

Users are used to seeing updates as an ordered list. You can make use of progress-bar graphics, which can be either horizontal or vertical. However, for many updates, vertical progress bars will support a better use of space and will also present better on mobile devices.

**3.****The status updates should use plain language that your users will understand.**

Sometimes status trackers are plugged onto a backend database without ensuring that the terminology used makes sense to users. Backend codes and internal jargon, such as “fulfilled” or “label created”, mean nothing to the user. Lack of clarity encourages users to contact the company. Each update should be written in [plain language](https://www.nngroup.com/articles/plain-language-experts/) and should be free from jargon.

*Some of the status updates in this tracker provided by Echo (another shipping company) have little meaning for users:* Processed Sort Facility, Pre-Advise Sent To Usps United Kingdom, Cert. of Posting Created.

**4.****Ensure information in the tracker is scannable.**

Where detailed tracking information is presented in a table format, ensure that the information is easily scannable. In the Echo tracker, the table columns are too narrow, causing the date and time to wrap. The result is that the information becomes difficult to scan. In the Royal Mail tracker (below), each update is visually distinct, with a dated header. There are only two columns and they have adequate spacing.

*The tracker provided by Royal Mail has visually distinct rows and two generously spaced columns, which makes scanning much easier than in the Echo status tracker.*

**5.****Allow users to change or add their contact information and to select frequency of updates.**

Where possible, allow users the option to add new contact details, change existing ones, and modify the frequency of notifications within the status tracker.

*USPS allow users to opt in to any of the 6 kinds of progress updates. Users can specify if they would like to receive them via SMS, email, or both.*

**6.****Tell users which information (e.g., reference number) they will need to access the status tracker.**

Ensure all your users have the information needed to use the status tracker from the start. Often, users will need to enter information such as an order or a reference number in order to get access to the tracker. Make sure that (1) people know that information will later be needed when you first provide it; (2) you tell users where to retrieve that information when they try to use the status tracker.

![Users who would like to track their passport application in the UK are asked for their reference number. Some hint text tells the user they can find this in their confirmation email.](https://media.nngroup.com/media/editor/2019/01/25/hmpo-tracker-login.png)

*Her Majesty’s Passport Office requires users tracking their new passport to authenticate themselves for security reasons. The user is told where to find the reference number.*

**7.****If users need to log in to track, ensure that error messages are specific and diagnostic.**

Vague error messages lead to confusion. For example, was the user’s record not found because it’s too early to track, or has the user made an error inputting a reference number? [Effective error messages](https://www.nngroup.com/articles/error-message-guidelines/) give users helpful information about possible reasons why they’ve encountered an error, which in turn, helps them understand whether they just need to wait or to try again.

Explore the possible error scenarios and spend time to design and test content to help your users [recover from errors](https://www.nngroup.com/articles/ten-usability-heuristics/).

**8.****Inform users about the status-tracker feature when they complete their application process.**

U.S. Citizenship and Immigration Services (USCIS) doesn’t inform their users that a status tracker for their work permit is available. Applicants receive a letter notifying them that their application has been received, but it mentions nothing about the status tracker on their website. Instead, the letter encourages users to call the help center if they have a query about the progress of their application. (Additionally, USCIS does not send any automatic updates, despite applicants providing contact details in their application.)

If users apply for a service or purchase a product online, send them a link to the status tracker in a confirmation email or when the product or service is ready to be tracked.

**9.****For processes that take a long time, provide regular updates, even if they are of low granularity.**

When offering a service that has a long processing time, and updates are few and far between, status trackers lose their value. This phenomenon is common in organizations that lack mechanisms to record certain events or are fearful about providing updates for PR or security reasons.

However, when there are long periods with no update, users start to think perhaps something went wrong, they lose trust in the status tracker, and begin to consider contacting the organization or company.

U.S. Citizenship and Immigration Service (USCIS) provide a status tracker for people applying for a green card or work permit. Following the creation of an account, applicants can log in to access the status tracker on USCIS’s website and see the status of their case. This feature is great to have, but there are no updates between documents being received to a decision being made, which can be several months.

*USCIS’ status tracker consists of a prominent status update in the center panel and previous updates below (to the left). There was a long period of no update between the 19th September and the 3rd December. Also, while the* Next Steps *panel is a useful concept, the content*— We will notify you if your document cannot be produced – *isn’t relevant anymore, as the card has already been produced and dispatched.*

Her Majesty’s Passport Office, on the other hand, includes frequent updates of lower granularity (such as *Joined the processing queue)*, which helps users feel that their application is in progress.

*Her Majesty’s Passport Office provides regular updates. The message* Joined the processing queue *helps users feel confident that their application made progress and that it won’t be long until their new passport will be on its way.*

Conduct user research to find out how much time users expect to pass between updates. When you have long periods with no possible updates (for example, an application is in a queue), consider using periodic messaging with helpful and relevant information about next steps. These may reassure users that progress is being made and their application or product is in hand.

**10. Show reliable and accurate updates.**

Some organizations have legacy systems that require some or all status updates to be entered manually by employees. This process often results in errors, and users may not be able to track status or may be shown inaccurate information.

In cases where employees must manually create and edit events in a backend system, a status tracker is less likely to meet user needs. It’s probably better to wait and deliver a status tracker when backend systems are suitably mature and it’s possible to automate events. In the meantime, consider other means of keeping users informed, such as providing regular, relevant, and reassuring email or SMS communications. This ensures users are not left in the dark between periods of no update. Throughout the user journey, ensure you set expectations for the wait time. Where possible, state exactly what the wait time will be.

For example, Monzo — a British digital-only, mobile bank — operated a waitlist for receiving a new debit card. The company sent emails to their users to reassure them that they’ll be notified as soon as a card was ready.

![The email sent by Monzo contains a colorful graphic and the text "Welcome to Monzo! Thank you for joining us! We need your support to build the bank of the future and we can't wait for you to get a card. We'll use the app to notify you as soon as we have one ready for you".](https://media.nngroup.com/media/editor/2019/01/25/monzo-email.png)

*An email sent by Monzo after registering an account and joining a wait list for a new card serves to keep users reassured that their new card order is being processed and excited to use the app.*

**11. Show previous updates, as well as the current update.**

Previous updates can be useful to users who need to make contact about a problematic order or who want to remind themselves how long certain steps took. Some status trackers — like the one shown previously from the U.S. Department of State — present only the latest update.

Shipping Force, who specialize in international home moves, provides a status tracker for their customers. Each dated notification — empty boxes have been sent to you, the driver has been assigned, the items are safely in the warehouse — shows progress and builds customer confidence that events are all happening as planned.

*Shipping Force’s status tracker utilizes a vertical progress graphic, showing all updates, dated, with the most recent at the top of the list. The list’s status label* In Progress *indicates there is still work to be done.*

Maintain all previous updates alongside dates. If space is limited, older updates can be made available behind clearly visible links or [progressive reveals](https://www.nngroup.com/articles/progressive-disclosure/).

**12. Have consistent updates in all channels .**

If users call the contact center, they should receive the same updates as seen in the status tracker. Status trackers lose their value if users find they can receive more-accurate updates by contacting the support center. This knowledge passes quickly by word of mouth and in online forums. Worse still, users lose [trust](https://www.nngroup.com/reports/ecommerce-ux-trust-and-credibility/) in your status tracker, especially if your employees tell them the status tracker is wrong.

Ensure that status updates in both the status tracker and customer-contact center systems have up-to-date and accurate records.

### Progress Updates

**13. Progress updates should provide a direct link to detailed tracking information.**

When sending progress updates, provide a link to where the user can see more detail. The link should be unique and take the user directly to their tracking information. Having to enter an order number before viewing the tracker is irritating and shouldn’t be necessary if users click a link from a progress update regarding their order or application.

*Club Monaco emails users that the order can be tracked (left), but when they click on the link in the email, they have to enter their order number and zip code to access the tracker (right). Users should have been taken directly to the tracker associated with that item.*

**14. Allow users to choose what types of progress updates they will receive (if any).**

When users make a purchase or apply for a service, give them choices as to how they’ll receive progress updates. Bear in mind that not all users want to receive progress updates — and some prefer email over SMS (and vice versa).

*The email progress update from UPS includes links to manage contact preferences.*

**15. Don’t overwhelm your users with updates.**

Progress updates can easily get out of hand if the company and the shipping company are both sending updates. Redundant messaging can be irritating for users. Instead, coordinate with any shipping suppliers to ensure you won’t send the user duplicate progress updates.

*Both Nordstrom and UPS sent email notifications when the same package was delivered.*

While frequent updates keep users informed, they could be annoying. Some users may only want a notification when the product is out for delivery. Carrying out user research with your users to understand what they need and expect can ensure that you find a good balance between too many and too few updates.

**16. Allow users to stop updates directly from the update.**

Users should be given the option to stop progress updates, like an [unsubscribe](https://www.nngroup.com/articles/unsubscribe-mistakes/) link. For email progress updates, the user should be provided with a link to change their contact preferences (which could be within the status tracker itself). For SMS, the user should be able to respond with the word *STOP.* These don’t need to be in every message, but they should be included periodically, so users can easily discover or be reminded of this option.

*AT&T provides SMS updates regarding a pending delivery of a new phone. The message tells users how they can stop receiving updates:* Text STOP to stop msgs.

## Conclusion

Status trackers and progress updates are necessary features when there’s any wait time for the user to receive a product or service. If designing a status tracker and sending status updates are both feasible, offer both to your users. Give users control over how they want to receive progress updates.

Run usability tests on your status trackers and progress updates to check that you are satisfying your users’ needs.

Learn more about designing services and messaging that support users in our report on [Transactional Email and Confirmation Messages](https://www.nngroup.com/reports/ecommerce-transactional-email-confirmation-message/).
