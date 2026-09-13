---
title: "5 Visual Treatments that Improve Accessibility"
date: "2022-10-30"
url: "https://www.nngroup.com/articles/visual-treatments-accessibility/"
author: "Kelley Gordon"
topics: [accessibility, visual-design, web-usability]
type: article
---

[According to the CDC, 61 million adults in the United States live with a disability.](https://www.cdc.gov/ncbddd/disabilityandhealth/infographic-disability-impacts-all.html#:~:text=61%20million%20adults%20in%20the,is%20highest%20in%20the%20South) Given the number of people who have a disability and the rise of Americans with Disabilities (ADA) website-related lawsuits over the past years, it is imperative that we design for these individuals. After all, accessible design drives better usability. Accessibility standards such as the [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/) are a good starting point for those aiming to improve the accessibility of their design. Additionally, platform-specific UI recommendations such as [Apple’s Human-Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility) and [Google’s Material Design](https://material.io/design/usability/accessibility.html#understanding-accessibility) also include accessibility guidelines for designers working within those ecosystems. This article presents 5 general guidelines that can be used to improve the accessibility of your visuals.

## In This Article:

- [1. Design for Color Contrast](#toc-1-design-for-color-contrast-1)
- [2. Provide Visual Cues in Addition to Color](#toc-2-provide-visual-cues-in-addition-to-color-2)
- [3. Identify Focus State](#toc-3-identify-focus-state-3)
- [4. Use Robust Alternative Text for Images](#toc-4-use-robust-alternative-text-for-images-4)
- [5. Test with Real Users](#toc-5-test-with-real-users-5)
- [Conclusion](#toc-conclusion-6)

## 1. Design for Color Contrast

People with vision impairments can have trouble reading text on low-contrast backgrounds. A **higher contrast ratio between text and its background** helps users with a low vision to read without contrast-enhancing assistive technology. This color contrast can also help users with normal vision to have a comfortable reading experience. According to the [WCAG](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html), the color-contrast ratio between text and its background should be at least 4.5:1. For text that is at least 18pt or 14pt bold, the ratio is a bit more generous at 3:1.

There are several tools to check color contrast. I like using [accessible-colors.com](https://accessible-colors.com/) because it provides decent alternative color suggestions if your contrast ratio is not compliant. To check for the color-contrast ratio, you will need to input the text size, the text weight, and the hexadecimal codes for text color and background color.

![Screenshot of website accessible-colors.com](https://media.nngroup.com/media/editor/2022/08/22/frame-27-1.jpg)

*To use a color-contrast tool, you will need the type size, weight, and color, as well as the text-background color.*

## 2. Provide Visual Cues in Addition to Color

Individuals who have color blindness or low visual acuity may not be able to distinguish between elements differentiated by color alone. It is thus important to **use additional cues (such as strokes, patterns)** to communicate important information.

*To signal an error, use a clear error message and a caution icon, in addition to color to make sure that people with vision impairments can see it.*

If you’re not sure if you need an additional design element in addition to color to get a point across, try the grayscale trick. Turn your design into grayscale and see if you can correctly understand the design.

*When you turn your design into grayscale, you can quickly see how color change alone is not enough to signal an error.*

## 3. Identify Focus State

Not only is it good usability practice to make interactive elements easily identifiable, but it is also beneficial for individuals who use the keyboard to navigate the web. A focus indicator, which is, by default, a blue outline around an element, helps people know which active element has the keyboard focus.

Focus states are easily customizable to fit your visual-design needs or brand standards. Links, form fields, widgets, buttons, and menu items should be focusable and their focus state should be clearly indicated.

I recommend using a **visually obvious stroke (e.g., a thick-weight line around the in-focus element)** to clearly identify a focus state for two reasons:

- This indicator is the default signal and many users expect it.
- Color change alone is not enough to distinguish between different states (see guideline #3 above), as it may not be perceived by some people with vision impairments.

*An easily identifiable thick border around the in-focus element helps individuals who use navigate the web using the keyboard.*

## 4. Use Robust Alternative Text for Images

Some users may use screen readers to interact and use a website. [Alternative text](https://www.nngroup.com/articles/write-alt-text/) (or **ALT text**) should be used to describe images and other graphic elements so that people who cannot see them can still get an idea of what is represented. A few guidelines to keep in mind when writing ALT text:

- Keep ALT text succinct.
- The **ALT text should not replicate the caption** of the image (since both will be read by the screen reader).
- ALT text should not be used for purely decorative images. If an image has no ALT text, the screen reader will jump over it, thus lessening the [working-memory](https://www.nngroup.com/articles/working-memory-external-memory/) load for users.

If you’re having trouble coming up with something valuable to include in your ALT text, reach out to a content designer.

*Use ALT text to succinctly describe the image.*

## 5. Test with Real Users

Make accessibility part of your research. Here are some tips to test your designs:

- **Get familiar with common assistive tools.** Understand how tools like screen readers, screen magnifiers, or Braille devices work and how to support them with your design.
- **Try it yourself.** Use the keyboard to navigate through your designs or turn on a screen reader. What did you miss or not account for? Is there anything confusing about the experience? Address these issues before testing your design with real users.
- **Test your design with real users.**[You need only 5 users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) to get valuable feedback. Fix the issues and test again as needed.
- **Consider recruiting users with a mix of accessibility needs —** for example, people with low vision and people with motor difficulty.

## Conclusion

How do your visuals hold up against these guidelines? If you haven’t designed with accessibility in mind, add it as a theme in your UX roadmap. Review your designs for accessibility and test them with real users with accessibility needs. It’s easier to design with accessibility in mind as you go, so there is less rework. Don’t sacrifice usability for aesthetics.
