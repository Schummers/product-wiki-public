---
title: "Glassmorphism: Definition and Best Practices"
date: "2024-06-07"
url: "https://www.nngroup.com/articles/glassmorphism/"
author: "Megan Brown"
topics: [interaction-design, visual-design]
type: article
---

Glassmorphism is a [visual-design trend](https://www.nngroup.com/videos/3-bs-design-trends/) gaining popularity since 2020 and is prominent in Apple and Microsoft's design systems. Glassmorphic elements look like frosted glass. Thoughtful use of glassmorphism can help designers effectively establish visual hierarchy and depth. However, without a solid grasp of visual-design principles or if overused, glassmorphism can pose significant accessibility and usability challenges.

## In This Article:

- [What Is Glassmorphism?](#toc-what-is-glassmorphism-1)
- [Glassmorphism in Design Systems](#toc-glassmorphism-in-design-systems-2)
- [Characteristics of Glassmorphism](#toc-characteristics-of-glassmorphism-3)
- [Designing with Glassmorphism: Best Practices](#toc-designing-with-glassmorphism-best-practices-4)
- [Conclusion](#toc-conclusion-5)

## What Is Glassmorphism?

> **Glassmorphism** is a visual-design style that utilizes different levels of translucency to create depth and contrast between foreground and background elements, mimicking frosted glass.

Typically, glassmorphic UI elements stand out when placed in front of gradients or complex backgrounds to accentuate depth.

*Two examples of glassmorphism from Apple’s SwiftUI design system:  iPadOS application folders (left) and MacOS notifications (right). Background elements are still visible but not easily identifiable.*

## Glassmorphism in Design Systems

While “glassmorphism” is a commonly used term, [design systems](https://www.nngroup.com/articles/design-systems-101/) tend to label this style under the broader category of “material” since these elements replicate the look of physical material in a digital space. For instance, [Microsoft’s Fluent Design System](https://fluent2.microsoft.design/material) defines a material called “Acrylic,” which embodies the characteristics of glassmorphism.

*Microsoft’s Fluent Design System defines Acrylic — a glassmorphic material.*

These design systems aim to create depth against complex backgrounds in order to emphasize or contain specific parts of an interface. In virtual- or mixed-reality spaces, glassmorphic elements help maintain a 3D experience by providing texture to objects that might otherwise seem two-dimensional on a standard screen. For example, the Apple Vision Pro uses glassmorphic [SwiftUI materials](https://developer.apple.com/documentation/swiftui/material) in translucent UI overlays to effectively blur the virtual-reality environments behind them while keeping them perceptible.

![A semi-transparent interface in the Apple Vision Pro showing information about objects in orbit, including text about the Moon and satellites, with a 3D model of a satellite on the right side. The background includes a living room setting with a plant and picture frame visible behind the interface.](https://media.nngroup.com/media/editor/2024/05/31/apple-v-pro-screen.png)

*Glassmorphism is used in the Apple Vision Pro interface. (Image source: https://developer.apple.com/design/human-interface-guidelines/windows )*

## Characteristics of Glassmorphism

Two main characteristics create glassmorphism’s translucency: opacity and background blur. To achieve a glassmorphic effect, designers can vary the opacity and background blur of components to affect how much background information is visible and distinguishable. Designers can also opt to use strokes and gradients for more depth and contrast if the glassmorphic elements will be placed on both complex and simple backgrounds.

### Opacity

To achieve a glassmorphic look, you need to be able to see through the element you are designing. You can achieve this by adjusting the opacity of your component’s fill (the color, pattern, or gradient inside of an object).

**Opacity** defines how much you can see through an element. The more opaque an element is, the less you can see the contents behind it. The less opaque, the more you can see. For example, the glass windows in your home probably have 0% opacity, meaning you can see everything outside clearly.

![Three rectangles demonstrating opacity variations: 90% opacity on the left, 60% opacity in the middle, and 30% opacity on the right. Each rectangle shows more of the colorful background as the opacity decreases.](https://media.nngroup.com/media/editor/2024/05/31/glassmorphism-opacity.jpg)

*The lower the opacity an element has, the more clearly you can see background elements.*

### Background Blur

**Background blur** distorts objects behind the main component, giving background elements a fuzzy, out-of-focus appearance. Examples of background blur in the physical world are a walk-in shower with a frosted glass door or a conference room with privacy glass. You can still see objects on the other side, but they are blurred to a point where you might be unable to identify them.

Background blur provides this same effect for low-opacity digital elements. For instance, a white rectangle with 30% opacity and a 25-pixel blur will distort background elements but still have somewhat distinguishable edges. However, by adjusting the blur to 100 pixels, those same background elements become more out-of-focus and blend together.

![Three rectangles demonstrating background blur at 30% opacity: 0px blur on the left, 25px blur in the middle, and 100px blur on the right. The rectangles show progressively more blurred backgrounds, making the elements behind them less distinguishable as the blur increases.](https://media.nngroup.com/media/editor/2024/05/31/glassmorphism-blur.jpg)

*The more background blur applied to a glassmorphic component, the harder it is to distinguish the elements behind it.*

### Strokes and Gradients

In addition to opacity and background blur, **strokes (borders) and gradients** can emphasize depth of glassmorphic elements, especially when these elements are placed on simple or one-color backgrounds.

A gradient takes two or more colors, color shades, or color opacities and blends them together seamlessly. Gradients can be applied to both fills and strokes of an element. You can add a low-opacity or gradient stroke around a component to create an illusion of thickness. Gradients can also be applied to the fill of the component to mimic the reflection of light on actual glass.

![A grid comparing stroke and gradient applications on elements with simple and complex backgrounds. The columns show variations: solid fill only, low-opacity stroke with solid fill, gradient stroke with solid fill, and gradient stroke with gradient fill. The rows compare the effects on simple versus complex backgrounds.](https://media.nngroup.com/media/editor/2024/05/31/strokesgradients.jpg)

*Adding a simple low-opacity stroke to an element with a solid fill can create the illusion of thickness. To go even further, use both gradient strokes and gradient fills to create depth over single-color backgrounds.*

## Designing with Glassmorphism: Best Practices

When incorporating glass-like materials in your UI, it is essential to understand the accessibility constraints of translucent components. One of the most significant issues with glassmorphism stems from text readability problems, with text either being too light or too dark or backgrounds being too busy. Follow these three best practices when incorporating glass-like materials into your design system

### Meet Contrast Requirements

**Ensure that text and graphical elements meet contrast requirements.** Since glassmorphic components are translucent, textual elements can fall over multiple colors, which can affect readability. For instance, if you are designing a card component over a busy background, your text might only have enough contrast over certain areas and be challenging to read. If you are designing in Figma, I recommend checking out the plugin [Contrast](https://www.figma.com/community/plugin/748533339900865323/contrast?searchSessionId=lv6xctrp-pmuz1pua1tm) by Willowtree, which lets you quickly check the contrast ratios of text and other design elements.

*WillowTree’s Contrast plugin lets designers sample colors from gradient or complex backgrounds to check for contrast accessibility.*

### More Blur Is Better

**More background blur is better, especially with intricate backgrounds**(e.g., video, photography, animations). Many UI designs on Behance or Dribble try too hard to keep background elements distinguishable. However, overwhelming backgrounds can make it hard for users to focus on meaningful content and affect text readability.

❌ *The low translucency reduces text contrast and makes this prototype's background overly distracting. (Screen capture taken from**Catalog Glassmorphism )*

In instances where components can appear in various contexts, like an overlay on a website or contextual menu on a desktop application, the background blur must **account for the many possible backgrounds on which the item may appear.** For example, the contextual menu below uses Microsoft’s acrylic material that appears over a complex image.

![A contextual menu with a high-blur Acrylic material from Microsoft’s Fluent Design System overlaying a desktop background featuring blue abstract shapes. The menu emphasizes interacting with the menu options by blurring the background.](https://media.nngroup.com/media/editor/2024/05/31/materials_acrylic_hero_1880.png)

*A contextual menu using the high-blur Acrylic material from Microsoft’s Fluent Design System accounts for the many possible desktop backgrounds and puts emphasis on the task of interacting with the menu.*

On the other hand, if you have control of what appears behind a translucent component, opt for simple or single-color backgrounds.

### Let Users Adjust Transparency

If feasible, **give users the option to control contrast or transparency settings.** For example, Apple’s accessibility features allow users to reduce transparency or increase contrast, minimizing or removing the blur of glassmorphic components altogether. These options enable the interface to be adaptable for low-vision users.

*Increasing the contrast with Apple’s accessibility features replaces any glassmorphic component with a solid color.*

If your budget or time constraints do not allow this type of [customization](https://www.nngroup.com/articles/customization-personalization/), then make sure that any glassmorphic elements in your interface are [WCAG-compliant](https://www.w3.org/TR/WCAG22/).

## Conclusion

Overall, glassmorphism is best when utilized sparingly to create an illusion of depth. Consider using already established design systems, like Apple’s SwfitUI, to avoid any potential issues with creating glassmorphic materials from scratch. Otherwise, be mindful of how translucent components are affected by background elements while maintaining visual hierarchy and accessibility requirements.
