---
type: source
name: "Executing UX Animations: Duration and Motion Characteristics"
created: 2026-07-30
published: 2020-02-09
source_type: article
status: processed
url: https://www.nngroup.com/articles/animation-duration/
author: Page Laubheimer
raw: raw/sources/2020-02-09_animation-duration.md
concepts:
  - "Animation"
  - "Motion Design"
  - "Accessibility"
  - "Microinteractions"
---

# Executing UX Animations: Duration and Motion Characteristics

## Summary

Animation execution quality directly impacts user experience, with timing and easing being critical details. Animation duration should generally fall between 100-500 milliseconds depending on complexity and distance traveled. Simple feedback animations work best at roughly 100ms, while substantial screen changes suit 200-300ms. At 500ms or longer, animations feel like delays. Easing—varying timing to make motion feel natural—is essential; ease-out is most common for entrance, ease-in for exit. Animations should respect users who enable "reduce motion" preferences. Accessibility is critical: animations with flashing, parallax, or scroll-jacking can trigger seizures or vestibular issues.

## Key Takeaways

- **Duration in 100-500ms range** — Most animations should fall between 100 and 500 milliseconds. Simple feedback like toggling should be about 100ms to feel immediate. Substantial screen changes suit 200-300ms. At 500ms animations become cumbersome and annoying.

- **Easing makes motion natural** — Linear motion appears unnatural. Easing varies timing to simulate physics: ease-out (fast start, slow end) works best for elements entering the screen, while ease-in works for exit. Ease-in-out is less responsive on entrance.

- **Recognize motion sensitivity** — Excessive animation, flashing, parallax, scroll-jacking, and carousel animations can cause vestibular disorders (dizziness, nausea, migraines) and trigger seizures in epileptic users. Respect browser "reduce motion" settings.

- **Entrance and exit differ** — Objects entering the screen typically need longer duration (300ms) than objects exiting (200-250ms). This asymmetry reflects natural perception and interaction patterns.

- **Specify clearly to developers** — Use animation timelines with all details (elements, triggers, transition types, durations in milliseconds, easing curves) rather than just video files. Different platforms require different easing specifications (cubic-Bezier for CSS, named curves for iOS/Android).

- **Details create quality** — Small timing details make enormous differences. Moving from 250ms to 300ms can feel very different. Getting animation details right requires careful attention and testing.

## Quotes

> The speed of an animation is hugely important for the usability — too fast, and it's hard to see or dizzying; too slow, and it becomes intrusive and feels like a delay to the user. In general, the duration of most animations should be in the range of 100–500 ms, depending on complexity and on how far the element is traveling.

> Simple feedback animations, such as showing a checkbox or toggle switch, should be roughly 100 ms (0.10 seconds) in total duration. This duration feels immediate to users and creates the illusion of physically manipulating the object.

> At 500ms, animations start to feel like a real drag for users — they become cumbersome and annoying. In most cases, a range of 100–400 ms is appropriate, with 400ms being a very slow animation, to be used only for big movements across large screens.

## Concepts

- [[Animation]] — Provides specific guidance on animation durations appropriate for different scenarios, from simple feedback to complex screen transitions.

- [[Motion Design]] — Shows how easing and movement characteristics affect how animation feels, emphasizing the importance of natural, physics-based motion.

- [[Accessibility]] — Highlights serious accessibility concerns with certain animation types and the importance of respecting user motion preferences.

- [[Microinteractions]] — Demonstrates how animation timing affects the perception and effectiveness of microinteraction feedback.
