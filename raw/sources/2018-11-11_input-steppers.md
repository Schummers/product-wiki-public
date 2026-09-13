---
title: "Design Guidelines for Input Steppers"
date: "2018-11-11"
url: "https://www.nngroup.com/articles/input-steppers/"
author: "Yuxuan (Tammy) Zhou"
topics: [interaction-design]
type: article
---

## In This Article:

- [Definition: The Input Stepper](#toc-definition-the-input-stepper-1)
- [Benefits of Input Steppers](#toc-benefits-of-input-steppers-2)
- [Drawbacks of Input Steppers](#toc-drawbacks-of-input-steppers-3)
- [Stepper-Design Guidelines](#toc-stepper-design-guidelines-4)
- [When to Use Input Steppers](#toc-when-to-use-input-steppers-5)

## Definition: The Input Stepper

Designing for data input can be tricky. Limited screen space on a mobile device or high [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) can make it difficult for users to type information. There are many input options, but not all methods are suited for every task.

A common input control is the input stepper, a user-interface element for inputting numeric information.

![Input Steppers](https://media.nngroup.com/media/editor/2018/09/18/1_steppers.png)

*Example of steppers: horizontal (left) and vertical (right)*

> **Input stepper:** A two-segment UI control used to incrementally increase or decrease a numeric value.

Most input steppers are visual elements of a graphical user interface (i.e., they’re GUI controls), voice and gestural interfaces can also have steppers. For example, saying “volume up” or “volume down” to a voice-controlled TV set will modify the volume by a set quantity. And in a 3D gestural interface, waving your hand up might increase the value of a selected variable. The key defining attribute of all these steppers is that they are *relative* controls — the user’s action changes the value of the specified variable by a certain fixed amount. (Contrast this type of control to an absolute one such an text-entry field; with absolute controls, the user specifies the new desired value with no reference to the previous value.) In this article we focus on the design of GUI input steppers.

Though input steppers are a handy tool for entering numbers in some cases, they’re not an ideal choice in every scenario. In this article, we discuss the pros and cons of this UI control, and how to use steppers correctly.

## Benefits of Input Steppers

### No Keyboard

Steppers can get around device limitations. For example, using a keyboard on a smartphone is error-prone, and some computer systems (such as transit terminals or museum kiosks) do not have keyboards. In these cases, input steppers are an appropriate design choice for supporting small adjustments of [default values](https://www.nngroup.com/articles/the-power-of-defaults/). (As in many other areas of interaction design, selecting good defaults based on task analysis or other user research will be crucial for the usability of these systems.)

![Kayak Input Steppers](https://media.nngroup.com/media/editor/2018/09/18/2_kayak.png)

*Kayak used input steppers to allow users to change the number of travelers in on its search form.*

### Intuitive to Use

Input steppers have clear, explicit [signifiers](https://www.jnd.org/dn.mss/signifiers_not_affordances.html): the plus segment is usually positioned to the right of (or above) the value and the minus segment is placed to the left (or below); these placements map naturally onto conceptual metaphors such as “progress is from left to right” or “more is up and less is down.” (These metaphors depend, however, on culture; for example, in cultures with right-to-left languages, the progress metaphor reverses. The position of the stepper segments should reflect cultural norm — like in the iOS example below.) Directional buttons and symbolic labels communicate function without the need for additional instructions.

![IOS input stepper](https://media.nngroup.com/media/editor/2018/09/18/3_ios_language.jpg)

*In iOS, changing the system language to a right-to-left one such as Arabic (left) reverses the stepper-segment placement (decrement on the right and increment on the left) in contrast to the English version (right).*

### Low Interaction Cost

For adjusting small values, steppers require fewer interactions than other input methods. For example, to increase the number of guests from 1 to 2 in a form, the user only needs one tap on the plus button. This action requires less effort than selecting the input field, tapping the digit “2” on the keypad, and hitting Enter or dismissing the keyboard.

![Steppers vs others](https://media.nngroup.com/media/editor/2018/09/18/4_steppers_vs_others.jpg)

*These 3 mobile screenshots show 3 different approaches to numerical input. American Airlines (left) used a dropdown for selecting the number of passengers. This control required several gestures (select the field, scroll and select the number, then hit Done). Treadmill Run Tracker (center) used a text field for inputting distance; the user had to select the field, type the desired number, then hit the Save button or tap a different field. In contrast, the interaction cost for changing the number of passengers from 1 to 2 in Delta Airlines’ mobile app (right) consisted of a single tap. (However, the interaction cost of the stepper would be much higher if the user wanted to increase the number from 1 to 10; this increased cost for large deviations from default is a major disadvantage of using steppers.)*

### Relative Controls when Users Don’t Know Exact Values

Since steppers are relative controls, they can free users from considering the exact value of the variable they’re modifying. People only need to think about whether they want the value to go up or down, relative to its current state. For example, when specifying the desired text size in a web browser, people who are not graphic designers will be hard pressed to decide on the exact number that will optimize the [legibility](https://www.nngroup.com/articles/legibility-readability-comprehension/) of a web page.

However, they definitely know if the current text feels too small or (rarely) too large, so it’s easy to use a stepper-like operation like CTRL-plus or CTRL-minus to make the text one step bigger or smaller (provided, of course, that they are familiar with these browser commands).

## Drawbacks of Input Steppers

### Difficult to Acquire

[Fitts’ Law](https://www.asktog.com/columns/022DesignedToGiveFitts.html) calculates the time it takes for people to reach a target. Whether using a mouse or a finger, bigger buttons are faster to reach than smaller buttons. But many input steppers feature stacked button positions or small button sizes.

In the example below, the up and down arrows are so tiny and close to each other that users need to slow down and plan their movement carefully in order to avoid misclicking on the opposite direction.

![Sketch input stepper](https://media.nngroup.com/media/editor/2018/09/18/5_sketch.png)

*Sketch, a creative-design editor, used tiny vertical stepper buttons for adjusting the size of a component on the screen.*

### Not for Large Adjustments to Default Value

Too much clicking and tapping can be irritating. Steppers are not suitable for a large number adjustments. For example, when users need to change a value from 1 to 50, an input stepper is not a wise choice. Thus, steppers make sense for numerical parameters with a clear default that most users are likely to select. If frequent, large deviations from that default are expected, a different input method will be more appropriate.

## Stepper-Design Guidelines

Based on the above considerations, here are some general recommendations for designing input steppers:

- **Use steppers for numerical fields with a clear most frequently selected value**. Steppers work well for fields that have one commonly entered value and most other input values deviate only slightly from that. If there is a lot of variability in the range of values that users normally enter for a field (e.g., for age or date of birth), a stepper is not appropriate.
- **Set the most frequently selected value as a stepper default**. This guideline is a direct implication of the first. For example, 1 is usually the default number of passenger for booking tickets or the default quantity for adding an item to cart, whereas 2 may be the default number of diners in a restaurant reservation.
- **Avoid steppers for continuous quantities**. By design, stepper fields can only take discrete values — that is, multiples of the step increment. (You cannot specify 1.5 items for a quantity stepper.) Sometimes, it makes sense to transform continuous variables into discrete ones (for example, we usually treat age as a discrete variable, counted in years). However, in many situations, transforming a continuous variable (such as prices or distances) into a discrete one with the wrong step can be irritating or inappropriate for the user task.

For instance, when looking to buy a house, an increment of $100K for the price field will be too restrictive, since some users may want to enter a value that is not a multiple of $100K, and rounding it up or down may not produce the same results.It’s best to allow users to type such continuous values instead of forcing them to use a fixed-increment stepper.

- **Show clearly what field is controlled by the stepper**. Clearly indicate the form content that the stepper applies to. For example, if a stepper control is used for changing time and date, the part of time or date being adjusted should clearly highlighted, so that users are aware of exactly what are they changing.

![Ns.nl input stepper](https://media.nngroup.com/media/editor/2018/09/18/6_nsnl.png)

*Ns.nl, the Dutch railway operator, used steppers to for time and date input. The exact section being changed was highlighted by a dark-blue underline.*

- **Use large buttons for both desktop and mobile**. Target areas should be big enough to support the input modality. For example, for touchscreens, we’ve long recommended a [minimum target size of 1 cm by 1 cm](https://www.nngroup.com/articles/touch-target-size/). And even though a mouse allows for more precision than a fingertip, don’t make buttons too small for desktop screens either.

![gpa input stepper](https://media.nngroup.com/media/editor/2018/09/18/7_gpa.png)

*In the left example from Handshake, a career-planning site, the adjustment buttons are small and difficult to acquire, even with a mouse. The example on the right shows how this UI could be redesigned and improved. The two buttons are placed farther apart and allow for easier selection.*

Horizontal steppers are usually better than vertical ones, which tend to be crowded. If you decide for a vertical placement, space the increment and decrement controls to make sure that you avoid slips due to accidental hits.

We recommend horizontal placement for steppers on mobile devices, considering the inherent precision challenges of using a fingertip.

![vertical horizontal input steppers](https://media.nngroup.com/media/editor/2018/09/18/8_vertical_vs_horizontal.jpg)

*StackExchange (left) used vertical steppers (highlighted in red). The Airbnb mobile application (right) used horizontal steppers for adjusting the number of guests for a reservation. Horizontal placement with separated buttons creates enough space between inputs to help users avoid accidental touches. On the other hand, the up/down metaphor is more appropriate for the Stack Exchange stepper (which indicates how many people gave a “thumbs up” or “thumbs down” vote to the post).*

- **Use +/- or arrow up/down as the button visualizations**. For horizontal steppers, plus and minus signs usually work best as labels for the step segments. For vertical steppers (with segments above and below the value), you can also use arrow-up and arrow-down buttons, often visualized as chevrons.

Arrow left/right buttons are a possibility for horizontal steppers, but are rarely recommended because they have less of a direct connotation with the concept of making something larger or smaller.

- **Add additional input methods**. In addition to a well-designed stepper, you might want to add alternative input methods to give users control and flexibility, especially when the input value is complicated or unpredictable. Here are a few additional input methods to combine with steppers in order to make the input more efficient: 

  - A text-field stepper is a UI component that enables quick entry of a number using a text field along with stepper buttons on the sides for adjustment. Users can choose to either directly enter the precise value or use the stepper to adjust the default value, if it’s close to the desired value and changing it requires only a few taps. This would be appropriate for our restaurant-reservation example with a default table size of 2 diners: the stepper could be easily used to specify single diners or a family of 4, whereas text input would be better for a group of 10.
  - Allow long press or click on the buttons for faster continuous increment or decrement.
  - (For desktop) allow users to use keyboard arrows for increment or decrement: up and down, left and right should match the button layout on the screen.

We usually don’t recommend having lots of different interaction techniques to achieve the same goal, because the need to learn and choose between multiple methods adds its own overhead to the UI. However, in the case of steppers, the alternate input methods are not visually prominent and people who just want to make a small adjustment to the default value won’t be slowed down by considering the alternatives.

- **Clarify the step value and the stepper range**. Designers should make the step and the unit explicit (e.g., dollars, cents, percentage). Also, if the input value has a maximum or minimum limit, be sure to indicate it. It is usually best to have a stepper change the current value by a step of one unit per button-press, but there can be cases where other step values are more appropriate, if indicated by a task analysis. (For example, in the above screenshot of specifying a student’s GPA, the appropriate step value is one tenth of a full grade point.)

![Expedia input steppers](https://media.nngroup.com/media/editor/2018/09/18/9_expedia.png)

Expedia used a grayed-out plus segment to signal when that the value had reached its limits.

## When to Use Input Steppers

Use Input Steppers When | Do Not Use Input Steppers When | The numeric field has a most commonly selected value and most users will not deviate insignificantly from it (e.g., number of passengers). | The numeric field can take a wide range of values (e.g., age), with no one value being entered significantly more often than others. | The numeric field needs to be adjusted by a small, discrete amount or precision is not important (e.g., number of bedrooms). | The numeric field is continuous and the exact value is important. | There is enough room for generous spacing of the stepper segments. | Limited design space for button layout would make the stepper segments small or cramped.

Implement input steppers for those fields that have a clear, preferred value that users will adjust only slightly. Stepper segments should be big enough to prevent user mistakes.
