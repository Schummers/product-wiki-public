---
title: "Natural Mappings and Stimulus-Response Compatibility in User Interface Design"
date: "2018-10-14"
url: "https://www.nngroup.com/articles/natural-mappings/"
author: "Katie Sherwin"
topics: [human-computer-interaction]
type: article
---

Have you ever played a video game in which the controls were reversed? In other words, right meant left and left meant right? If you did, you probably know that it’s not easy. It is an example of stimulus–response incompatibility.

Back in the 1950s, the psychologists Paul Fitts (well known in human–computer interaction for the [law that bears his name](https://www.asktog.com/columns/022DesignedToGiveFitts.html)) and Charles Seeger ran a series of experiments which demonstrated this concept. They asked people to respond to a stimulus that appeared on their left or right side by pressing two buttons:

1. In one condition, the stimuli and the responses were on the same side: people had to use their left hand to press a button on their left when the stimulus appeared on the left (and their right hand when the stimulus was shown on the right).
2. In another condition, the stimuli and the responses were on opposite sides: participants had to use their right hand to press a button on the right when the stimulus appeared on the left, and vice versa.

Fitts found that participants were faster in the first condition, which presented a stimulus–response compatibility.

Definition: **Stimulus–response compatibility** is the degree to which the physical arrangement of the stimuli matches the location of the expected responses.

Stimulus–response compatibility is highly relevant for design. When an object or an interface violates it, its usability decreases significantly.

Consider these two stoves. Which knob controls which burner? Does one stove make you feel more confident in your guess?

![Four burner stove with unnatural mapping compared to five-burner stove with natural mappings to control knobs](https://media.nngroup.com/media/editor/2018/07/20/stovetop_natural-unnatural_mappings.jpg)

*On the left, a typical stovetop arranges burners in a two–by–two grid and the controlling knobs aligned in a single row across the bottom. This design makes it difficult for users to guess which knob controls each burner (no stimulus–response compatibility). On the right, the arrangement of the controls mimics the arrangement of the five burners, and therefore has a higher stimulus–response compatibility.*

Consider this picture I took not long ago of a ticket machine at a train station. After paying with a credit card, the machine asked for my ZIP code as a security measure. But, to my confusion, the yellow numbered buttons were not touchable. Dumbfounded, I repeatedly tapped the yellow on-screen numbers, thinking that maybe the screen was frozen or had a slow response time. Then, I noticed the column of metal buttons on either side of the screen. Each column was numbered 1-6. To my surprise (and horror), pressing the button marked ‘1’ on the right column, caused a ‘6’ to appear in the zip code field. Pressing the metal button for 2 caused a ‘7’ to appear on the screen. I couldn’t believe it. It felt physically and cognitively unnatural to press one number to get a different number to appear. My slow reaction time to press each button was a direct result of stimulus–response incompatibility.

![Train ticket kiosk with poor stimulus-response compatibility](https://media.nngroup.com/media/editor/2018/07/20/njtransit_stimulus-response.jpg)

*An example of low stimulus–response compatibility is this train-ticket machine, in which users had to press a button labeled with a number that did not necessarily match the actual desired number (e.g., pressing the metal button labeled 1 to get 6 to appear on screen).*

## In This Article:

- [Natural Mappings](#toc-natural-mappings-1)
- [Conclusion](#toc-conclusion-2)
- [References:](#toc-references-3)

## Natural Mappings

The concept of stimulus–response compatibility can be extended beyond its spatial dimension. This is exactly what Don Norman does in his book “[The Design of Everyday Things](https://www.nngroup.com/books/the-design-of-everyday-things/)”.

Definition: **Natural mapping** refers to a design in which the system’s controls represent or correspond to the desired outcome. When controls map to the actions that will result, systems are faster to learn and easier to remember.

Natural mappings bridge the [gulf of execution](https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/), helping users to understand how a system can be used and what actions are required to accomplish their goal. Designers can create natural mappings in several ways, including the three common patterns below:

1. **Spatial similarity.** This pattern is pretty much the same as the stimulus–response compatibility. By arranging controls in a spatial layout that mimics the design layout, users can understand the system faster. For example, consider the screenshot below, taken from the *Display Settings* menu on a Mac. When multiple monitors are connected, the *Display Arrangement* screen allows users to rearrange the on-screen versions of the monitors to match the actual positions of the physical monitors. For users working on extended screens, this similarity of layout helps them quickly drag files from one monitor to the other, because the layout maps closely to how the monitors are arranged on the desk. 

![Screenshot of desktop monitor arrangement and photo of actual monitor arrangement](https://media.nngroup.com/media/editor/2018/07/20/naturalmapping_monitor-arrangement.png)

*Arranging on-screen monitors (left) to mimic the arrangement of the physical monitors (right) is an example of natural mappings, which helps users move efficiently between monitors while working.*
2. **Conceptual or metaphorical similarity.** Some designs take advantage of a commonly accepted metaphor and use that as the basis for design decisions. When done well, these metaphorical mappings can serve to make the system’s functions more transparent. Consider the brightness control in the iOS Control Center. Swiping up within the control increases the screen brightness, and swiping down on the control makes the screen darker. This arrangement works because of the strong cultural metaphor “up is more,” which conceptually maps the “higher [brightness]” to the higher level. Moreover, the brightness control fills with a white background color, which also conceptually maps to the level of brightness (imagine if the fill were reversed; —that is, if a black fill indicated greater screen brightness. It wouldn’t feel natural.). Or consider color, which can have associations with specific actions — for example, in the Western world, “green is go” and “red is stop.” Designers can take advantage of such metaphors to create natural mappings. Be aware that the effectiveness of mapping is largely dependent on cultural and social conventions. 

![iOS control center](https://media.nngroup.com/media/editor/2018/07/20/iphone_brightness_control.png)

*The brightness control in the iOS Control Center uses natural mapping by arranging the control so that swiping up raises the screen brightness (up is more) and swiping down darkens the screen (down is less).*
3. **Behavioral similarity.** Users often have expectations about what will happen when they perform an action, and these expectations are often governed by their goals. Behavioral similarity is another form of system feedback in which the interface responds in a way that resembles the action that users perform. For example, when users are interested in consulting their watch, they will often move and tilt their hands to see the watch better. This behavior was capitalized by the smartwatch designers in the “raise to wake” gesture. For a user to “wake up” the device, all that’s required is that she turn her wrist to look at the watch face. The device detects the movement and interprets the user’s intention to interact. The behavior is so natural that users don’t have to recall a special function in order to get the device’s screen to turn on: the wake-up command has become a [noncommand user interface](https://www.nngroup.com/articles/noncommand/). Note that despite [gestures becoming more common](https://www.nngroup.com/articles/iphone-x/) in devices and applications, they still present [burdens and challenges to users](https://www.jnd.org/dn.mss/opportunities_and_ch.html). Many gestures are unnatural; they don’t relate to the actions users attempt to complete, and therefore they are harder to discover, remember, and execute. One exception is the rotate gesture on a trackpad, which is similar to how a person might rotate a photo in real life. But gestures that require complex interactions, such as two, three, or four-finger taps or swipes, are too difficult for average users to learn and recall correctly. When creating a gesture, designers must consider natural mappings if they want to have any hope of the gesture being adopted. 

![Screenshots of multi-touch gesture illustrations](https://media.nngroup.com/media/editor/2018/07/20/gestures_natural-unnatural.png)

*The rotate gesture on a trackpad (left) has a natural mapping to how a person might rotate an object in real life. However, many gestures, such as the four-finger swipe and three-finger tap, aren’t clearly associated to the action being carried out, and therefore they are challenging for users to learn and execute (Image source: support.apple.com/en-us/ht204895 ).*

## Conclusion

For a system to be easy to learn, people need to quickly understand how it works, what actions are possible, and how to accomplish their goals. Designs that have a high stimulus–response compatibility and take advantage of natural mappings can help users act faster and with more confidence.

## References:

Fitts, P. M., & Seeger, C. M. (1953). "S-R compatibility: spatial characteristics of stimulus and response codes." *Journal of Experimental Psychology*, 46(3), 199-210.

Lakoff, G. & Johnson, M. (2003). *Metaphors we live by*. Chicago: University of Chicago Press.

Norman, D. (2013). *The design of everyday things*. New York, New York: Basic Books.
