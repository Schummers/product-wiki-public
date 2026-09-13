---
title: "10 Usability Heuristics Applied to Virtual Reality"
date: "2021-07-11"
url: "https://www.nngroup.com/articles/usability-heuristics-virtual-reality/"
author: "Alita Kendrick"
topics: [heuristic-evaluation]
type: article
---

Occasionally, attendees in our seminar, [Emerging Patterns in Interface Design](https://www.nngroup.com/courses/emerging-patterns-interface-design/) will ask **about the best practices for designing virtual-reality applications**. My answer always leads to Jakob Nielsen’s [10 usability heuristics for interface design](https://www.nngroup.com/articles/ten-usability-heuristics/). From websites and mobile apps to [video games](https://www.nngroup.com/articles/usability-heuristics-applied-video-games/) and yes, even virtual reality, these heuristics maintain relevance.

In what follows, we look at each of the 10 usability heuristics applied to virtual reality. Specifically, these examples are from the Oculus Quest headset.

*Note: these screenshots are from a 3D virtual environment, so you will notice curves and shadows unsuited for a 2D environment like this webpage.*

## In This Article:

- [1. Visibility of System Status](#toc-1-visibility-of-system-status-1)
- [2. Match Between System and the Real World](#toc-2-match-between-system-and-the-real-world-2)
- [3. User Control and Freedom](#toc-3-user-control-and-freedom-3)
- [4. Consistency and Standards](#toc-4-consistency-and-standards-4)
- [5. Error Prevention](#toc-5-error-prevention-5)
- [6. Recognition Rather than Recall](#toc-6-recognition-rather-than-recall-6)
- [7. Flexibility and Efficiency of Use](#toc-7-flexibility-and-efficiency-of-use-7)
- [8. Aesthetic and Minimalist design](#toc-8-aesthetic-and-minimalist-design-8)
- [9. Help Users Recognize, Diagnose, and Recover from Errors](#toc-9-help-users-recognize-diagnose-and-recover-from-errors-9)
- [10. Help and Documentation](#toc-10-help-and-documentation-10)
- [Conclusion](#toc-conclusion-11)

## 1. Visibility of System Status

*The design should always keep users informed about what is going on, through appropriate feedback within a reasonable amount of time.*

**Systems that clearly communicate their current state foster trust and predictability**.

In the main navigation for Oculus Quest, known as the universal menu, battery life for both the headset and controllers displayed in the bottom left. Battery life is presented as four circles (communicating approximate quarters), but users can hover over one of the three icons (left controller, headset, right controller) to see precise battery percentages. This information communicates the current state of the system hardware and may influence player’s behavior.

![The universal menu in Oculus displays battery life.](https://media.nngroup.com/media/editor/2021/06/18/universal-menu.png)

*The universal menu in Oculus communicated battery status for the headset and two controllers.*

Similarly, in *Bogo*, a game where players interact with a virtual pet, a heart icon shows how much brushing still needs to be done in order to progress to the next phase of the adventure. Once the heart is full, the user can move on (or keep brushing if they wish to do so).

![A virtual pet with a status icon](https://media.nngroup.com/media/editor/2021/06/18/bogo.png)

*In* Bogo *on Oculus Quest, the status of a virtual brushing interaction was displayed.*

## 2. Match Between System and the Real World

[The design should speak the users' language. Use words, phrases, and concepts familiar to the user, rather than internal jargon. Follow real-world conventions, making information appear in a natural and logical order.](https://www.nngroup.com/articles/match-system-real-world/)

Many people have little to no experience with virtual reality and thus rely on past (physical and digital) experiences to drive their behaviors and expectations in the virtual realm. **Building on existing**[mental models](https://www.nngroup.com/articles/mental-models/)**helps users (correctly) predict interactions in a VR system.** In fact, since *virtual* reality often has a close relationship with *actual* reality, it ought to be easier to apply this heuristic for VR designers than it sometimes might be for traditional 2D-GUI designers.

*Immersed*, a digital work environment, allows users to work with others in familiar settings like coffee shops and conference rooms. In these spaces, users can share screens and brainstorm ideas on a whiteboard (like in the real world). The whiteboard element can be locked or unlocked with a [state-switch](https://www.nngroup.com/articles/state-switch-buttons/) icon at the top. (While this is not how you interact with a physical whiteboard, at least the padlock icon embodies a strong physical metaphor.)

![A virtual conference room and whiteboard](https://media.nngroup.com/media/editor/2021/06/18/immersed.png)

*Immersed used real-world counterparts, like conference rooms, whiteboards, and locks, to meet users’ expectations and existing mental models.*

## 3. User Control and Freedom

*Users often perform actions by mistake. They need a clearly marked "emergency exit" to leave the unwanted action without having to go through an extended process.*

Getting stuck in a virtual environment can be frustrating. Providing a way out, through buttons like *Back* or *Exit*, supports users’ sense of freedom and can get them out of an unpleasant experience.

For example, in Beat Saber, a music-based video game, avatars can be customized or randomly generated (via an unlabeled die button). Even when users accidentally click the die button, the *Cancel* button allows them to abandon the customization screen and keep the previous avatar. Users can also click the *Back* button next to the die, which reverts the avatar back to the previous version.

![Game avatar with customization options](https://media.nngroup.com/media/editor/2021/06/18/beat-saber.png)

*Beat Saber offered a* Cancel ***** button to users on the avatar-customization page. If multiple customizations were made within one session, users could select the *Back* button to revert to the previous avatar.*

In contrast, in the ESPN application, when prompted to sign in with a TV provider like Comcast or Hulu, users are unable to go back to the provider-selection screen. For instance, a user who selects Hulu cannot change their mind and navigate back to the selection screen (unless they exit the application and restart the process). It’s likely that users won’t know their login credentials at the time of this interaction, especially since referencing physical notes or a digital password manager is no easy feat while wearing a headset. A *Back* button would allow users to revisit the selection screen and browse offerings or even select a different provider (in case they made a mistake). Without a *Back* button, users may be forced to exit the app. (Unfortunately, Oculus blacks out this type of content during screen recording, so we are not able to provide a screenshot for this interaction.)

## 4. Consistency and Standards

*Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow platform and industry conventions.*

[Jakob’s law of user experience](https://www.nngroup.com/videos/jakobs-law-internet-user-experience/) says that users spend most of their time on websites other than yours. Since many of these follow design standards and users are familiar with them, **interfaces that go against these standards are prone to increasing user’s cognitive load**.

[Toggle switches](https://www.nngroup.com/articles/toggle-switch-guidelines/) are digital on–off switches that are present throughout the web. They’re also common in virtual environments where users can choose between two mutually exclusive options (like notifications on or off). In *Gravity Sketch*, a 3D drawing tool, what should be a toggle switch is visualized as a [slider](https://www.nngroup.com/articles/gui-slider-controls/), which is confusing and unnecessarily increases the [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/). In *Settings*, to turn the grid on or off, users must click and drag a knob. This interaction requires more effort than a switch and it fails to meet user’s expectations. Despite this poor design, at least Gravity Sketch is internally consistent and uses a similar visual design for all its toggles.

![System settings with slider bars](https://media.nngroup.com/media/editor/2021/06/18/gravity.png)

*Gravity Sketch did not comply with the conventional design standard for an on–off switch, though it used the same slider design for on­–off switches throughout the app.***

![Oculus settings with toggle switches](https://media.nngroup.com/media/editor/2021/06/18/oculus.png)

*In contrast to Gravity Sketch, Oculus followed the design standard for toggle switches.*

## 5. Error Prevention

*Good error messages are important, but the best designs carefully prevent problems from occurring in the first place. Either eliminate error-prone conditions, or check for them and present users with a confirmation option before they commit to the action.*

Interface [slips](https://www.nngroup.com/articles/slips/) and [mistakes](https://www.nngroup.com/articles/user-mistakes/) happen all the time. **Aim to design proactive systems that can anticipate and prevent errors.**

A guardian is a game-play boundary defined by the user. In Oculus, when a player approaches the predefined guardian, a grid appears on screen, to warn them. Many games recommend a minimum guardian size to ensure a reliable and consistent experience. When users play *Vader Immortal* with a guardian smaller than the recommended gameplay size, they are shown a warning. This information can prevent errors by 1) subtly encouraging users to move to a space where they can have a larger boundary and 2) stressing caution while playing the game to avoid physical harm.

![Game warning that reads "Your guardian is currently set to a size that is smaller than the recommended play size of 6.5 x 6.5 feet."](https://media.nngroup.com/media/editor/2021/06/18/vader.png)

*Vader Immortal prevented errors and accidents by warning players who set a guardian that was smaller than the recommended size.*

Similarly, in *National Geographic Explore VR*, before users leave an uncompleted activity, they are prompted with a confirmation message. This message warns users that their current activity progress with be lost if they choose to leave at this point.

![Confirmation message that asks 'are you sure?'](https://media.nngroup.com/media/editor/2021/06/18/natgeo.png)

*National Geographic VR showed a confirmation message to protect users from accidentally leaving the activity and losing progress. (It would be even better if, in addition, the progress was automatically saved.)*

## 6. Recognition Rather than Recall

*Minimize the user's memory load by making elements, actions, and options visible. The user should not have to remember information from one part of the interface to another. Information required to use the design (e.g. field labels or menu items) should be visible or easily retrievable when needed.*

Humans’ [short-term memory](https://www.nngroup.com/articles/short-term-memory-and-web-usability/) has a limited capacity and virtual experiences are often complex enough (especially for new users). **Don’t overburden VR users by asking them to remember additional information**.

Unlabeled [icons](https://www.nngroup.com/articles/icon-usability/) with [tooltips](https://www.nngroup.com/articles/tooltip-guidelines/) are a frequent culprit of memory strain in VR interfaces. Throughout Oculus, there were many instances of unlabeled icons. To see what the icons mean, users could hover to reveal a tooltip with the icon description. This design forces users to either memorize the meaning of the icons or put in additional effort to uncover the label.

![7 icons without labels](https://media.nngroup.com/media/editor/2021/06/20/unlabeled.png)

*Oculus’ use of unlabeled icons with tooltips weighed on users’ short-term memory.*

In contrast, National Geographic Explore VR promotes recognition over recall when users engage in activities like taking photos. Instead of asking users to recall which of their controller buttons to use in order to take a photo, the controls (with labels) are shown on screen.

![Scenery with overlaid camera frame and oculus controller button labels](https://media.nngroup.com/media/editor/2021/06/20/natgeo2.png)

National Geographic Explore VR *reminded users what controller buttons to use to take a picture whenever the camera feature was used.*

## 7. Flexibility and Efficiency of Use

*Shortcuts — hidden from novice users — may speed up the interaction for the expert user such that the design can cater to both inexperienced and experienced users. Allow users to tailor frequent actions.*

**Virtual environments, like traditional interfaces, must cater to novice and experienced users.** Good defaults are important to keeping everyone happy, but shortcuts and customizations may be needed to keep experienced users engaged.

For instance, *Beat Saber* players can modify their game experience to make it more challenging and enjoyable. This feature makes the gameplay flexible and customizable. Once the modifications are set, they persist for future game sessions, so users don’t need to define them again.

![Gameplay modification settings](https://media.nngroup.com/media/editor/2021/06/20/beat-saber2.png)

*Beat Saber’s game modifications offered an opportunity for players to create a flexible game-play experience, tailored to fit their needs.*

*Firefox Reality*, a browser designed for virtual reality, allowed users to tailor their browser window size to fit their preferences.

![web browser window with screen size modification overlay](https://media.nngroup.com/media/editor/2021/06/20/firefox.png)

*Firefox Reality offered users the flexibility to tailor their browser window size.*

## 8. Aesthetic and Minimalist design

*Dialogues should not contain information which is irrelevant or rarely needed. Every extra unit of information in a dialogue competes with the relevant units of information and diminishes their relative visibility.*

Virtual interfaces can offer a great deal of complexity, which makes it even more important to [prioritize the essentials](https://www.nngroup.com/articles/signal-noise-ratio/). For example, *YouTube* did a great job providing elements relevant to user’s primary goals — like viewing VR-friendly videos (360-degree) and search.

![Video listings with filter options](https://media.nngroup.com/media/editor/2021/06/20/youtube.png)

*YouTube’s minimalist homepage was tailored to user’s primary actions.*

On the other hand, *Pokerstars VR* is often messy and distracting. During gameplay, when users open the menu to select game-relevant actions (like placing a bet or viewing settings) they are met with a cluttered, difficult-to-scan interface.

![Poker game with crowded settings menu](https://media.nngroup.com/media/editor/2021/06/20/poker.png)

*Pokerstars VR had a cluttered and overly complex in-game menu that overlapped with an already busy game background.*

## 9. Help Users Recognize, Diagnose, and Recover from Errors

*Error messages should be expressed in plain language (no error codes), precisely indicate the problem, and constructively suggest a solution.*

Clear communication and helpful suggestions are key to effective error messages. Unfortunately, *Firefox Reality* fails to provide constructive error messages when users have trouble using voice commands. Despite several attempts with a variety of queries, the voice capability never understood a word, even though the system provided visual feedback that it captured audio. The system failure was made worse by the unhelpful suggestion to ‘please try again.’ It’s unclear whether it’s a local system issue, a Firefox Reality issue, or something else. This error message helps users recognize a problem but does little to help them diagnose and recover from it.

![Popup message that reads "Sorry! I could not understand. Please try again."](https://media.nngroup.com/media/editor/2021/06/20/firefox2.png)

*Firefox Reality’s error message lacked diagnostic or actionable help.*

*Pokerstars VR* offers a training where users could familiarize themselves with some of the primary game interactions, one of which was a complex gesture, likely unfamiliar to most users. If users struggle multiple times with the interaction, they are directed to another (nongestural) method to accomplish the same result. This workflow helps users recognize and recover from the error but doesn’t do much to diagnose the problem or make people understand how the gesture should be performed.

![Poker game with written instructions](https://media.nngroup.com/media/editor/2021/06/20/poker2.png)

*Pokerstars VR helped users recover from a tricky gesture by providing an alternate method. However, the system did not explain why the gesture failed.*

## 10. Help and Documentation

*It’s best if the system doesn’t need any additional explanation. However, it may be necessary to provide documentation to help users understand how to complete their tasks.*

Virtual-reality experiences often contain a high volume of interactions, some of which are complicated or unfamiliar to users. Instances like these require thoughtful documentation that enables users to solve their problem and get back on track.

*Immersed* offers users accessible help and documentation. In fact, users have a variety of channels for support, including video tutorials, [frequently asked questions](https://www.nngroup.com/articles/faq-ux-deconstructed/), help documentation, and live support. The documentation pages (available in a web browser) were well organized and easy to scan, applying good information hierarchy and action-oriented phrases.

![Help page with clear headings and steps](https://media.nngroup.com/media/editor/2021/06/20/immersed2.png)

*The help pages for Immersed were easy to access, organized, and scannable.*

## Conclusion

The user experience of virtual-reality applications can stunt its growth potential. Whether you think VR is overvalued or the future of technology, remember that VR has maintained its allure over a decade of hype. There is consumer interest and engineering capability, but this platform has a lot of room to grow in user experience. Despite being a different type of interface, **standard usability heuristics still apply**.
