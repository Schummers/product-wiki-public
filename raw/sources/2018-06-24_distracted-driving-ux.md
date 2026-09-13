---
title: "Distracted Driving: UX’s Responsibility to Do No Harm"
date: "2018-06-24"
url: "https://www.nngroup.com/articles/distracted-driving-ux/"
author: "Page Laubheimer"
topics: [behavior-patterns, mobile-and-tablet-design, psychology-and-ux]
type: article
---

Very recently, my wife and I were in an Uber, stopped in traffic. As I marveled at the congestion on the Brooklyn-Queens Expressway on a Saturday afternoon, there was suddenly a huge bang, so loud it almost seemed unreal, and the car jolted forward violently. We had been rear-ended by another car going at least 30 MPH. Both my wife and the driver were okay.

Out of the rear window I saw smoke billowing from the car that hit us, its airbags deployed, and what looked suspiciously like a mobile-device cradle on the dashboard pointed at the driver.

I jumped out to check on the other car, and banged on the windows. To my amazement, the people inside were stunned, but okay.

After regrouping, the driver said that she hadn’t seen our car. At a dead stop in traffic with lights on, a car would be pretty hard to miss, unless the driver was distracted. I suspect that she was using her phone while driving, though, of course, I don’t know that for certain.

I also don’t know for certain whether the driver that rear-ended my taxi 5 days later, in a nearly identical accident, was using his phone, but when I looked out the back windshield I noticed the telltale sign of a mobile-device cradle on his dashboard (before he fled the scene of the accident). Luckily, this accident was much less severe than the first, and once again, everyone walked away.

I do know this for certain: distracted driving claimed [3,450 lives in 2016](https://www.nhtsa.gov/risky-driving/distracted-driving) alone, and in 2015 [391,000 people were injured](https://www.cdc.gov/motorvehiclesafety/distracted_driving/index.html) in crashes involving distracted driving — which is often due to mobile-device use. The National Highway Traffic Safety Administration estimates that roughly [660,000 drivers](https://www.nhtsa.gov/staticfiles/numbers/SafetyInNumbers_Nletter101_811742.pdf) every day are using a mobile device while driving. We can wring our hands, denounce all the irresponsible people doing so, and wish that they would just stop this dangerous behavior, but that’s unlikely to solve the problem. I was lucky to walk away from not one, but two incidents in one week. Many are not so lucky.

Traffic laws won’t save us. Partly because drivers flout the law. But more so because laws about modern technology are often misguided: for example, many recent traffic laws forbid use of handheld phones but allow hands-free phone calls even though they are incredibly dangerous. (Accidents stem from the [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/) of conversing with a remote person, not from having a telephone in one hand.) Yet drivers — quite reasonably — feel that complying with the law will make them safe. Thus, rules against handheld phone calls likely increase accidents if the law tempts drivers to have more hands-free calls or use features such as Siri Eyes-Free.

People should absolutely not use their phones while driving. They also should not drive drunk, burn plastic, or litter. But they do these and other things that harm themselves and others. They use their phones while driving. With this reality in mind, it is becoming clear to me that, if we don’t *consider* the unfortunate but realistic scenario of people using our mobile products while driving, we are not [responsible UX professionals](https://theblog.adobe.com/social-responsibility-ux-designers-comes-teens-tech-addiction/).

## In This Article:

- [We Can’t Design Specifically for Drivers, Can We?](#toc-we-cant-design-specifically-for-drivers-can-we-1)
- [Voice Input Is Not a Panacea but Can Help if Designed Right](#toc-voice-input-is-not-a-panacea-but-can-help-if-designed-right-2)
- [Strong Signifiers and Low Cognitive Load](#toc-strong-signifiers-and-low-cognitive-load-3)
- [Good Defaults and Interaction Cost](#toc-good-defaults-and-interaction-cost-4)
- [Glanceable Typography](#toc-glanceable-typography-5)
- [Smartphone Addiction, Gamification, and Mental-Reward Systems](#toc-smartphone-addiction-gamification-and-mental-reward-systems-6)
- [The UX Hippocratic Oath](#toc-the-ux-hippocratic-oath-7)

## We Can’t Design Specifically for Drivers, Can We?

I anticipate some of the questions and concerns about the previous statement. Your immediate reaction to reading that might be:

- “While our users may indeed be using mobile devices while driving, we can’t responsibly design for that use case!”
- “Wouldn’t that be encouraging that behavior?”
- “Wouldn’t that take away from our focus of designing for our intended use cases?”
- “Wouldn’t that expose us to legal liability?”
- “You wouldn’t specifically design a car to be able to be more easily driven when intoxicated, right? Why should we design our apps to be easier to use when driving?”

To which I respond: no, you shouldn’t design *specifically* to facilitate the use of your mobile app or website while driving. However, you can —and should — make design choices (based on known UX guidelines) that reduce, even if not completely eliminate, the dangers of people using their devices while driving. I’m not suggesting that UX is solely responsible for the problem (or its solution), but we should consider the principle of harm reduction when creating a design that has a reasonable likelihood of being used by drivers.

No matter how good the UI is, if people use it while they’re driving, it’s dangerous. In theory, we can discourage people from using our products in situations where they can serve as dangerous distractions, but it is difficult to do it without penalizing legitimate uses. For example, many cars’ built-in navigation systems won’t allow people to enter a destination while the car is moving, even if it’s the passenger doing the entry. This restriction is extraordinarily frustrating, and the wordy error message is still a distraction if the driver attempts to use the system while driving.

## Voice Input Is Not a Panacea but Can Help if Designed Right

Often, the reaction to concerns like this is that [voice-recognition systems](https://www.nngroup.com/articles/voice-first/) and conversational agents will solve this problem — if not today, then in the near future. However, as [we’ve been studying systems](https://www.nngroup.com/articles/voice-interaction-ux/) such as Siri, Alexa, Cortana, and Google Assistant for some time, these systems still pose major problems for users:

- Voice agents (especially Siri) frequently require the user to [look at the screen](https://www.nngroup.com/articles/voice-first/) and interact with visual elements such as buttons.
- These systems still pose significant [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/), because they require the user to [recall, rather than recognize](https://www.nngroup.com/articles/recognition-and-recall/), acceptable commands.
- Users have to expend mental resources to formulate their verbal queries before speaking. They must think about how to phrase the query so that the voice-recognition system will understand it.
- Voice-based systems often do a poor job at understanding a query that is a followup to a previous answer.
- These voice-recognition systems often don’t work (or don’t work well) with third-party apps and features people want to access while driving.
- Verbally listing options is not an [efficient output modality](https://www.nngroup.com/articles/voice-first/), compared to the [nonsequential visual access](https://www.nngroup.com/articles/direct-vs-sequential-access/) that a screen-based list affords. Users therefore have to listen to a voice assistant droning on and on to hear their options, which is yet another form of distraction.

While voice interaction does hold some major promise for reducing the need to look at the screen, it is not the sole solution to this problem. If your app does integrate voice recognition, there are several strategies to make it less disruptive for users (and, as a benefit, these also help accessibility for [screen reader](https://www.nngroup.com/articles/touchscreen-screen-readers/) users as well): be brief and [cut excessive wordiness](https://www.nngroup.com/articles/content-strategy-long-vs-short/) (especially for lists of items), use clear [auditory signifiers](https://www.nngroup.com/articles/audio-signifiers-voice-interaction/) and [progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/) to give options and detail only when needed.

## Strong Signifiers and Low Cognitive Load

Bad design overloads users’ [working memory](https://www.nngroup.com/articles/working-memory-external-memory/), increases their [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/), and raises their stress level. If our users are safely sitting at their desks or on their couches, the [cognitive strain](https://www.nngroup.com/articles/navigation-cognitive-strain/) that results from lack of usability may seem just a minor inconvenience, but if they’re driving at 55 miles per hour, a design that requires an extra 5 seconds to decipher means they could have traveled [the length of a football field](https://www.cdc.gov/motorvehiclesafety/distracted_driving/index.html) with their eyes off the road.

In our recent [eyetracking study](https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/) of flat designs, we found that weak [signifiers](https://www.jnd.org/dn.mss/signifiers_not_affordances.html) led to [click uncertainty](https://www.nngroup.com/articles/flat-design-best-practices/) (and, critically, increased time on task). In other words, commonly used flat-design patterns make people spend precious mental resources to consider whether, for example, a [ghost button](https://www.nngroup.com/articles/characteristics-minimalism/) really *is* a button or just a rectangle.

Even flat design patterns that may seem obvious to the design team are confusing to people that are distracted or stressed. Right after the first accident, after we ensured that everyone was okay and called 911 to report the accident, my Uber driver (who was faultless and shaken up by the experience) tried to end the ride in the Uber app so that he could report the accident. The app design featured a full-width, flat button at the bottom of the screen; to end the ride, the driver had to swipe (not tap) along the length of the button. (Presumably, the app designers chose a gesture that was harder to perform accidentally, to avoid unwanted ride cancelations.) But unfortunately there was no signifier to tell users what gesture they had to use. I watched as the driver tried over and over again to use this weakly signified UI component (while admittedly in a stressed state) and had to force myself not to ask him to [think out loud](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/)!

We may think that following basic principles of good design — such as using strong signifiers for active UI elements, clear, descriptive labels for buttons and icons, or following conventions and giving users all the tools they need to complete the task — is a nice-to-have add-on, but in fact, in dangerous or stressful situations, it is mission critical. And with phones becoming ubiquitous, we should all design for dangerous circumstances.

## Good Defaults and Interaction Cost

An important interaction principle that can help reduce distraction is to develop [good defaults](https://www.nngroup.com/articles/the-power-of-defaults/) for top tasks, and to vary the defaults based on the user’s context. Good defaults, when appropriately employed, reduce the [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/), and can significantly speed up the [microinteractions](https://www.nngroup.com/courses/usability-mobile-websites-apps/) that often occur when driving. If a person is attempting to locate a restaurant in a mapping application like Google Maps while not moving, a good default would be to find the closest match in any direction; if, however, the person already has turn-by-turn navigation turned on and is driving on the highway, the appropriate good default would be to search for a restaurant along the route.

## Glanceable Typography

Another method to improve designs for distracted users involves adopting font sizes that support glanceable reading. In a [recent study](https://www.nngroup.com/articles/glanceable-fonts/) by MIT’s Agelab on glanceable typography, larger, wider, and capitalized text outperformed smaller, narrow, and lowercase text. While all-caps text can negatively affect the legibility of long passages, for small, glanceable items (such as button labels), all-caps, large, and wide text makes it possible for users to read words quickly.

## Smartphone Addiction, Gamification, and Mental-Reward Systems

[Smartphone addiction](https://www.npr.org/sections/alltechconsidered/2017/03/13/519977607/irresistible-by-design-its-no-accident-you-cant-stop-looking-at-the-screen) is starting to be recognized as a problem with real consequences, even by some of the [companies](https://www.facebook.com/zuck/posts/10104413015393571)[responsible](https://www.theverge.com/2018/5/8/17327302/android-p-update-new-features-changes-video-google-io-2018) for designing devices and apps. Consider Apple’s embarrassing incident when three of its employees [walked right into the glass walls](http://time.com/5162419/apple-new-headquarters-glass/) at the new Cupertino campus while, you guessed it, they were using their phones. The blame should go to the building designers for not signaling glass walls appropriately, but also to app designers for making mobile apps and websites addictive. It’s not simply a byproduct of the inherent usefulness of mobile devices; for many teams, there is often a mandate to design mobile products that [encourage habitual behaviors](https://www.nirandfar.com/hooked).

Many small companies, especially startups, prioritize increasing user engagement in their apps; in doing so, they ignore the human costs of [excessive gamification,](https://www.nngroup.com/articles/difficult-design-best/) constant [notifications](https://www.nngroup.com/articles/indicators-validations-notifications/), and [delight](https://www.nngroup.com/articles/theory-user-delight/)[ful](http://www.nngroup.com/articles/theory-user-delight/)rewards for every interaction.

It’s very possible to use techniques that leverage human psychology in a moderate, ethical way (as we advocate for in our [Persuasive Web Design](https://www.nngroup.com/courses/credibility-and-persuasive-web-design/) and [The Human Mind and Usability](https://www.nngroup.com/courses/human-mind/) seminars) to help nudge users toward mutually beneficial behaviors, but if we focus solely on how to light up users’ dopamine receptors every time they fire up our apps, we’ve gone astray. You can [design for how people think](https://www.nngroup.com/videos/design-how-people-think/) without manipulating them to devote every spare minute to your app.

## The UX Hippocratic Oath

I firmly believe that UX is a professional discipline. That means we have professional responsibilities to uphold. If we truly are human-centered designers, we should embrace [Don Norman’s original concept](https://www.nngroup.com/videos/don-norman-term-ux/) of user experience as the *totality* of factors that influence what happens when users interact with our designs. We must consider the person on the other side of the screen, what her actual context of use is (even if it’s not what we intended), and the possible implications of our design choices on our users’ lives — *beyond* momentary delight or annoyance.

It is a hard problem, and there are many obstacles in place to prevent the UX community from making meaningful improvements in this area. I don’t have all the answers, and I’m fully aware that I’m not the first to speak up. I’m writing this article as a call-to-arms for our community to consider how each one of us can do better, even in a small way. I’m consistently amazed and humbled by the smart, driven, and empathetic UX people that come to our [UX Conferences](https://www.nngroup.com/ux-conference/), and I have no doubt that all of that talent, turned to this problem, can make a difference.

As a first step, I urge you to consider your own design priorities and choices in the same way that responsible physicians do when they take the Hippocratic Oath, saying “**first, do no harm.”** So, I ask the UX community at large: what is an equivalent code of ethics for our discipline? Rather than list the obstacles in our way, how can you change your own UX process and design decisions so that you make a difference? Can you commit to asking your team about the implications of distracted driving during your next internal design review? Can you give users 5 seconds to complete one of your top tasks in a usability-testing session?

When we’re doing our day-to-day design work, we rarely consider our users’ real context. We often assume that people who use our product will be focused on it, with no distractions. But that’s simply not how people interact with digital products. Whether it’s a case of using a mobile app while watching TV, walking along a busy city street while reading email, being interrupted by a Slack message while doing complex work on a desktop computer, or trying to figure out a faster route while driving, our users are constantly distracted. Shouldn’t we be considering these distractions if we’re truly doing context-sensitive, human-centered design?
