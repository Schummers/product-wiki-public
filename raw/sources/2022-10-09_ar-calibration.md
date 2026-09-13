---
title: "Augmented-Reality Calibration in Mobile Apps: 10 Guidelines"
date: "2022-10-09"
url: "https://www.nngroup.com/articles/ar-calibration/"
author: "Raluca Budiu, Sana Behnam"
topics: [interaction-design, mobile-and-tablet-design, web-usability]
type: article
---

Except for some [live try-on features for products such as makeup and glasses](https://www.nngroup.com/articles/augmented-reality-useful/), users often need to follow multiple steps to calibrate an augmented-reality feature in a mobile app before starting the experience.

What is calibration for [augmented reality](https://www.nngroup.com/articles/augmented-reality-ux/) (AR) and why is it needed? Remember, augmented reality combines real-world inputs with virtual objects in order to create a new scene. For that resulting scene to be meaningful, the AR software needs to consider the relative sizes, colors, and other features of virtual and real objects so that it can sensibly put them together. And that is done through calibration.

Definition: The **calibration process** in AR allows AR virtual elements to be accurately aligned and incorporated in the real-life environment.

Calibration is one of the critical parts of the AR experience, affecting users’ success and satisfaction with the experience. Unlike [onboarding](https://www.nngroup.com/articles/ar-walkthroughs/), which usually needs to be done just once, **calibration will usually need to be included for every session in which the user accesses the AR feature**.

This article presents 10 guidelines for calibration instructions and feedback in mobile applications using AR. These guidelines are based on a [usability-testing](https://www.nngroup.com/articles/usability-testing-101/) study in which 11 participants tested a variety of AR-related mobile apps.

## In This Article:

- [Calibration Patterns](#toc-calibration-patterns-1)
- [Guidelines for AR Calibration](#toc-guidelines-for-ar-calibration-2)
- [Conclusion](#toc-conclusion-3)

## Calibration Patterns

Depending on the app’s goals and functionality, AR calibration may involve one or more of the following user actions:

- **Scanning**: The user must scan a rough or textured surface such as a floor or wall (or a certain indicator in the environment such as edge between a wall and the ceiling).
- **Absolute positioning**: The user has to position the device in a certain location, such as leaning it to a wall or go to a specific landmark in a city.
- **Relative positioning:** The user must have the device in a fixed position on the ground or at waist level, then get to a certain distance from the camera/device and be fully or partially visible in the camera view. This is typical for AR fitness apps or games.
- **No calibration**: The AR feature can be used right away and requires only appropriate lighting. This is usually the case with live try-on apps (e.g., Ulta, Warby Parker) or AR filters (e.g., Instagram, TikTok).

Due to the complexity and variations in these patterns, many of our study participants struggled with the calibration process While it is often recommended to [minimize the number of instructions or tutorials in mobile apps](https://www.nngroup.com/articles/mobile-tutorials/), effective instructions and signifiers along with appropriate feedback can create a successful calibration experience.

![Instructions say "Slowly move your device from side to side to scan the floor" and "place your device against the wall"](https://media.nngroup.com/media/editor/2022/09/28/0-houzz-app-successful-instruction-2-images.png)

*Houzz app: One participant tried to view a painting in the AR mode. Even though he did not understand why he needed to scan the floor (left) or lean the device against the wall (right), he was able to achieve success due to the clear and detailed instructions.*

## Guidelines for AR Calibration

There are two big components of the calibration process: [instructions](https://www.nngroup.com/articles/mobile-instructional-overlay/) that tell users what they’re supposed to do to calibrate the AR feature and feedback that lets them know whether they are on the right track. In what follows, we address both these components.

### Instructions

1. **Provide low-granularity instructions, one at a time.**

Instructions should be broken down into small steps and presented one at a time. One of our participants struggled to figure out which of the three different instructions presented on the screen she was supposed to follow. She said: *“*Oh, gosh. It just had like three instructions. There's like a *Tap*, *Return to previous area to resume*, *Start over*. Now I'm just going to hit *Start over*. ‘Cause I don't really know what's going on. […] I didn't know […] what it wanted me to do.”

*ARvid app: A study participant didn’t know which of the 3 instructions displayed on this screen (* Tap *at the very top, in low contrast,* Return to the previous area to resume, *and* Start Over *) she was supposed to follow.*
2. **Instructions should be descriptive and unambiguous.**

Be specific enough to clarify misunderstandings and help users accomplish their goal. For example, moving the phone from side to side can be done at various speeds and across various trajectories.

The Civilization AR app instructed the user to *Scan a textured surface* to start the calibration process. The participant started scanning the chair's texture by moving the camera close to the chair's back part. But the app required a rough surface such as a carpet to initiate the calibrating process. She said *:*“All right. It wants texture. Here's texture. Okay. Now what? I don't know what these little dots are. Lots of little dots. Here's some texture for you. I don't know what you want me to do now […] Okay. It likes the chair. It's thinking. I don't know. I don't know what's going on right now. I have no idea.” In this case, not only were the instructions insufficient, but the feedback (through the dots) was also not understood by the participant (see our discussion of this signifier later in the article).

*Civilization AR**app: The participant followed the instruction by pointing the camera to the back of his chair. Unfortunately, the app needed a rough texture.  The participant had difficulty interpreting the feedback given by the apps (the low quantity of dots in the image was supposed to mean poor scanning, but she did not understand that) and was unsure as to whether the scanning was successful.*

If necessary, clarify text instructions by providing concrete examples or visuals.

*Mission to Mars app: Users were shown good and bad examples of lighting (left) and surfaces (right) they could use for calibration.*
3. **Give users enough time to read the instructions and execute them.**

The user should be given enough time to digest and respond to the information. Participants often didn’t have enough time to read the instructions, as they disappeared too fast.

*ARVid app: Not only was the instruction at the top shown in low-contrast text, but it disappeared too quickly from the screen and the study participant was not able to finish reading it.*
4. **Make the instructions visually salient by showing them close to the center of the screen, in a contrasting color, on a darker background.**

Some participants ignored the instructions because their attention was focused on task. Additionally, some instructions were hard to see or read because they blended in with the scene. Unlike in other applications, where the background is fixed, the background in an AR experience changes based on the user’s environment. Certain backgrounds may result in low visibility for instructions or other UI elements. Designers of AR experiences should keep these limitations in mind and test the experience in various environments and light conditions.

To ensure that the instructions are easy to notice and stand out across different backgrounds, consider enclosing them in a solid-colored box and displaying them in a color that contrasts with the box background.

*MauAR Berlin Wall app used a black, contrasting background for the narrative text (right). However, UI copy such as the label* Story *and the years (* 1961 *,*1971, 1981*) (left) would have also benefited from a black contrasting background.**Kinfolk app used relatively salient/bold colors that increased visibility. However, the text still needed a contrasting background to ensure its readability across a variety of environments*.
5. **Visuals used for instructions should augment (rather than contradict) text instructions.**

Visuals can help disambiguate text instructions and are effective for showing examples of gestures, textures, or other things that may be required for calibration. However, visual cues that prompt the user to take specific actions should be clear and precise because often users will follow visual instructions literally. For example, when prompted to scan a surface using the phone camera during the calibration process, users often follow the motion suggested by the visual cues.

*The Smartify: Museum and Art Guide app provided unclear animation and visual instructions for scanning and calibrating. The animation was meant to show users what they were supposed to do, but, in fact, one participant misinterpreted it as showing a rapid circular motion and proceeded to move her phone that way, with no success. In this case, both the speed and the direction of the demo animation were misleading.*

Additionally, misalignment between the visuals and the real experience can cause confusion. One participant using the Active Arcade app received visual instruction that displayed a person putting the device on a desk/table; however, the written instructions were asking the participant to put the device on the ground. In fact, the visual instruction was meant to be an animation showing the user pick up the device from the table and place it on the floor, but the animation was frozen during the session and the user saw only the first part. The app could have prevented this issue by timing the instruction text so that it was associated with the right frame of the animation.

*Active Arcade app: The visual showed the device set on the table at waist level, whereas the written instructions asked the user to put the device on the ground. The text instruction should have appeared when the user placed the device on the floor. These types of misalignments confused study participants.*
6. **Consider using audio instructions or tips if the device will need to be far away from the user.**

Users prefer receiving optional instructions in a brief, visual format rather than through lengthy text.

However, for certain apps, the user may not be able to perform the activity and read the instructions at the same time. For such apps, consider providing audio tips (of course, provided that the user allows them — you don’t want to unpleasantly surprise users!).

### Feedback

Feedback is essential for any good user experience. The first of [the ten usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) is [visibility of system status](https://www.nngroup.com/articles/visibility-system-status/): making sure that the user always knows what the state of the system is.

During calibration, keep users informed of the state of the system and to give them feedback about the actions that they are performing in order to calibrate the experience.

1. **Keep users informed of the state of the system.**

In many cases, as users were trying to calibrate the system, they had no idea of whether they were on the right track and the system was doing some complex computation or it was stuck because they had provided the wrong input.

For example, in the Civilization AR app, a participant struggled to figure out what the system was doing. He said: “[It says] *move your device slowly around to detect a surface. Okay. It likes the chair. It's thinking. I don't know. I don't know what's going on right now. I have no idea. What would be helpful here [is] to tell me what's happening.”*
2. **Use clear, standard signifiers to indicate the state of the system.**

The calibration process can be complex; hence, the UI elements and signifiers should be clear and easy to understand. Vague elements that do not provide any directions can add to users’ confusion.

Many applications used floating or scattered dots to indicate that the app is scanning the environment. Nonetheless, most participants were confused and unsure how to interpret these dots. A participant using the Target app commented, “There were, like, dots everywhere on the ground and I just sort of hit where it said ‘tap to position the sofa’ […] The dots were just confusing. I guess what was helpful is where it said ‘tap’ because I knew what to do. It gave me some direction, but just the dots… […] I thought it was, like, scanning my room and […] taking a photo of it or something, but they weren't helpful to me.”

Another participant had a similar experience with the Etsy app. The participant was trying to view a painting on the wall, but the dots showed up during the calibration process. She said: “So, I'm moving my camera at the wall. […] When I pointed it at the couch, [there were] yellow dots. I don't know why those yellow dots are there, but where I would put it [the painting] would be on the wall right here. And it's not doing anything. So that's frustrating. I probably actually by now would have just said, forget it. I'm not, I'm not gonna try to do this AR thing. So, I don't know. It's scanning everything in my room.”

*The yellow dots in the Target (left) and Etsy (right) apps  confused study participants.*

While these cues do show that the app is not frozen, they do not add any additional value and do not help the user in determining the next step or identifying potential issues.
3. **Load the AR object within the user’s field of view. If, for some reason, the object moves during the interaction, provide guidance to help users find it.**

Adding the virtual object to the real-world scene is often a step in the calibration process. But many participants struggled to find the AR object in the environment. For example, one participant using the ARLOOPA app attempted to place an animated character in the room; she believed that the character had disappeared when, in reality, it had moved behind her!

The AR object should be initially loaded in the user’s field of view, where it is fully visible. If, for some reason, the object needs to move, provide clear feedback to the user about the location of the virtual object or give them instructions of what they should expect. Only three applications (e.g., Civilization AR, Augmented Berlin, MauAR - Berlin Wall) used some visual clues to help the user find the AR object. For instance, the Augmented Berlin app prompted the user with an arrow to look behind him. The participant said: “I see the arrow that seems to be pointing behind me. I turn around, let’s see what it’s trying to show me.”

Depending on your application’s goal, you can use different strategies to guide the user to the AR object. For example, if your app uses AR to tell a story, a subtler cue (such as animation) that does not interrupt the flow of the experience might be preferrable to text or visual elements like an arrow. One participant said of the Augmented Berlin experience: “I guess if there was some sort of movement within this world, that I would then follow. Instead of telling me you know, hey this is a picture. Because this [approach] sort of feels like I'm just looking at the picture …. Now that, with the arrow, I’m not much in this place, but a picture of a place. So, if there was something walking, then I [might] feel like I’m interacting rather than being told ‘look behind you.’”

*MauAR —Berlin Wall (left) and Augmented Berlin (right) used arrows to direct the user to the AR object.**Civilization AR used a dotted line to direct the user to the virtual object. While it was good that the app pointed the user to the object of interest, the dotted line is a poor signifier, especially since many AR apps also use dots to indicate scanning.*
4. **Give users feedback about their actions so that they can recover from errors.**

Users should receive clear instruction on how to recover from an error and progress towards achieving their goals. If the user does seem to take any action for a certain amount of time, they should be notified about a potential issue and get guidance on how to resolve it.

One study participant using the Etsy application struggled to figure out what was wrong. She said, “Yeah. Directions. Like, if I'm scanning it at a blank wall and it's not working, I need to know why. Is it not bright enough? Maybe it needs more lighting — like tell me what's wrong. Otherwise, it's just frustrating. ‘Cause it said, ‘point it where you want it to be,’ which would be a blank space on my wall. So yeah. […] I don't want to stand there and scan the same place for five minutes or even one minute. I just want it to pop up on my walls.”

*The Target app provided unclear calibration instructions, with no suggestion towards the next steps.*

## Conclusion

Calibration is a complex and critical aspect of the mobile AR experience that often causes usability problems for users. While some issues are related to technological challenges and limitations, the calibration experience can be improved by clear, descriptive, timely, and unambiguous instructions that take into account users’ low familiarity with the AR technology. Additionally, prompt, explicit feedback and guidance will enable users to have a seamless and successful interaction with the AR feature.
