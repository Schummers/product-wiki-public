---
title: "The Impact of Interaction Design on Brand Perception"
date: "2016-07-17"
url: "https://www.nngroup.com/articles/interaction-branding/"
author: "Kate Moran"
topics: [branding, interaction-design]
type: article
---

Branding can be critically important when consumers decide whether to interact with organizations — make a purchase, use a service, apply for employment, or even sign up for a newsletter. While the perception of a brand cannot be strictly controlled, it can certainly be *influenced.*

**Almost every aspect of a digital interface can influence the portrayal of an organization’s brand identity** or ‘personality,’ including:

- Visual design: how the UI looks
- Content design: how the UI sounds
- Interaction design: how the UI feels

Of these three, visual design often receives the most attention from digital-product teams interested in conveying the right brand attributes. That’s not necessarily due to a lack of appreciation for the other two facets. It’s just often easier to speculate how a specific color scheme or logo design might impact branding than to understand the influence something invisible like an interaction pattern.

Manipulating interaction design with an eye towards brand impact can be particularly challenging. At the center of this challenge is some uncertainty about what the relationships are between specific types of interaction design and branding. For example, what kind of an interaction makes a brand feel ‘sophisticated’? What kind of interaction makes it ‘professional’? Research can help answer some of these questions, by measuring the effects that interaction design decisions have on users’ perceptions of brand attributes.

## In This Article:

- [Finding the Links Between Interaction and Brand](#toc-finding-the-links-between-interaction-and-brand-1)
- [Applying These Findings to Your Designs](#toc-applying-these-findings-to-your-designs-2)

## Finding the Links Between Interaction and Brand

In [a study](http://dl.acm.org/citation.cfm?id=2858036&picked=formats) published at CHI 2016, UX consultant Peter Tolstrup Aagesen and interaction design researcher Clint Heyer selected a set of specific qualities of interactivity (that they called **interactivity attributes)**, and then measured their impacts on emotion, as well as on brand perception.

The interactivity attributes studied by Tolstrup and Heyer include:

- **Responsiveness:** How quickly an element responds to a user action
- **Direct or indirect manipulation:** Whether a user can manipulate an element directly by interacting with the element itself (for example, by clicking on it) or indirectly (for example, by using a tool like slider)
- **Precision**: How precise a user can be when interacting with the element (for example, being able to select specific parts of an element, or just the whole)
- **Pliability**: How easy or difficult it is for a user to effect a change on an element (for example, clicking twice to expand an element, or simply hovering over the element to expand it)
- **Continuous or discrete behavior**: How continuous or discrete (with stops or separate steps) the transitions between states are
- **Clear labels or no labels:** How well the system communicates available actions and the consequences of those actions (Tolstrup and Heyer call this attribute “Feedback”)
- **Expected or unexpected behavior:** Whether an element’s behavior conforms with a user’s expectations
- **Consistent or inconsistent behavior:** Whether an element’s behavior conforms with established patterns (either internal or external to the system)

For each interactivity attribute, Tolstrup and Heyer constructed simple interactive prototypes meant to embody the two extremes of that attribute. For example, they created one prototype for direct manipulation in which users could change the width of a circle by directly clicking on the circle itself and dragging. The opposite extreme, indirect manipulation, was expressed in a prototype in which users would change the width of a circle by clicking and dragging a slider.

*This still from Tolstrup and Heyer’s study demonstrates their prototypes for direct or indirect manipulation of objects. In this example, users were able to alter the circle by clicking and dragging on the circle itself (direct manipulation) or by clicking and dragging an external slider (indirect manipulation).*

For an example of how this difference could play out in real-world web design, let’s consider a vacation rental site like Airbnb.com. Say that we want to rent an apartment within a few blocks of Covent Garden in London.

A direct-manipulation interface would allow users to click directly on the desired spot on the map or drag a rectangle to specify the area they want. However, the site currently uses an indirect-manipulation interface for zooming, where the user has to click a plus or a minus button. Moving the map itself (without zoom) is done by direct manipulation, by “grabbing” the map with the mouse.

*Airbnb.com: In 2016, this site used direct manipulation for panning the viewport and indirect manipulation for zooming the magnification.*

Participants were asked to interact with each pair of prototypes, and then answer a series of 7-point rating-scale questions. Each question asked the participant to indicate which of the two extreme prototypes related most to a brand value or emotion. For example, for the direct/indirect manipulation example, one of the questions might ask, “Which of the two [prototypes] is more closely related to ‘surprise’?” The participant could select options 1–3, to indicate the direct manipulation prototype was more related to surprise. Or, the participant could select options 5–7 to indicate the indirect manipulation prototype was more related to surprise. If the participant selected the neutral option 4, they weren’t sure which prototype was more related to that emotion.

The rating scales asked about five brand attributes and six emotional attributes, listed below.

**Brand attributes:**

- Sincerity
- Excitement
- Competence
- Sophistication
- Ruggedness

**Emotional attributes:**

- Surprise
- Anger
- Anxiety
- Disgust
- Sadness
- Joy

Tolstrup and Heyer found many relationships between interactivity attributes and the brand and emotional attributes. For the full discussion on the relationships they found, see their paper, referenced at the end of this article. The findings related to labels, expected behavior, and consistency in particular support existing best practices and confirm widely-held assumptions, so we’ll address those briefly here.

*This brief video (2:02) demonstrates the behavior of three of the interactive prototypes used in the study: Labels, expectedness, and consistency.*

The prototype with [clear labels](https://www.nngroup.com/articles/category-names-suck/) suggested sincerity and competence, and triggered a feeling of joy. In contrast, the prototype without labeling was associated with surprise, but also anger — not an emotion we want to evoke in our users. These findings reinforce the importance of information scent ­— **clearly communicating what actions are available in the system**.

When the prototypes [functioned as users expected](https://www.nngroup.com/articles/the-need-for-web-design-standards/) or demonstrated **consistency**, people associated them with sincerity and competence. On the other hand, prototypes that did not behave consistently or conform to expectations were, again, associated with surprise and anger.**Know what your users expect in interactions, and avoid breaking consistency unnecessarily.**

## Applying These Findings to Your Designs

Tolstrup and Heyer’s study used extremely simplified tasks and prototypes. They also used a homogeneous and potentially unique sample as participants — their own personal and professional acquaintances, all 30 to 40 years old. For these reasons, you should expect some differences in how these various interactive qualities influence your users. That said, there are a few ways you can learn from this study and apply to your interaction design.

- **Take an inventory of your interaction-design attributes.** Narrow your focus to a specific task, feature, or workflow. How does this interactive feature match up with the interactivity attributes? How responsive are the elements to users’ actions? Are the labels and icons clear to users? Can users directly manipulate elements?
- **Consider how these interaction-design attributes might support or detract from your stated brand values.** If conveying a sense of professionalism and competence is critical for your brand, does an interactive feature with inconsistent behavior conflict with that goal?
- **Pay special attention to inconsistent or unexpected interactive elements.** When designed carefully, these have the potential to trigger feelings of pleasant surprise. However, they can also make users feel powerless. Proceed with caution. The best way to know for sure if you’re evoking pleasant surprise and not anger will be to test with your users.
- **Conduct a brand/emotion evaluation of your interaction.** Ask your users to use a specific interactive feature in your system. Then ask them to fill out rating scales indicating how much their experience matched up to your brand attributes or emotions of interest (Likert scales or semantic differential scales might work equally well for this). You might also consider asking the participants to choose from a [product-reaction word list](https://www.nngroup.com/articles/microsoft-desirability-toolkit/) to help you gauge the impact of your brand attributes. After one round of testing, modify your interaction design to be more consistent, clear, or responsive, and then retest.

This study is just a starting point — further research on this topic is needed to answer all our questions. But it is interesting in demonstrating a quantifiable relationship between specific interaction designs and users’ perceptions of overall brand personality traits.

In interactive systems such as websites, the way people interact with the user interface obviously has a strong impact on their feelings about the system. We know that [people prefer designs that are easy to use](https://www.nngroup.com/articles/satisfaction-vs-performance-metrics/). But as this research shows, the impact of interaction design goes deeper than simple preferences or user satisfaction. Interactivity influences customers’ perceptions of brand traits just like visuals and content do.

*Note: Tolstrup and Heyer use slightly different terminology to describe the interactivity attributes.*[A demonstration video of the interactive attributes](http://dl.acm.org/citation.cfm?doid=2858036.2858521)*used in Tolstrup and Heyer’s study is currently available from the ACM Digital Library under the tab ‘Source Materials’ (linked as “Supplemental Video”).*[The interactive prototypes](http://petertolstrup.com/attributes/)*themselves are available on Tolstrup’s website.*

# Reference

Aagesen, P. T., & Heyer, C. (2016). [Personality of Interaction](http://dl.acm.org/citation.cfm?doid=2858036.2858521). *Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems — CHI'16*.
