---
title: "What Parallax Lacks"
date: "2019-01-20"
url: "https://www.nngroup.com/articles/parallax-usability/"
author: "Katie Sherwin"
topics: [visual-design]
type: article
---

Several years ago, a colleague and I ventured out to test a new design trend that was winning web-design awards and earning praise on designer forums. That trend was parallax scrolling. We were not impressed. More importantly, neither were users (for reasons I’ll explain below). After a short couple of years, the parallax trend slowly faded away, likely because those early adopters saw the same results we did: harm to the user experience or lukewarm user reactions, at best. The outcomes didn’t justify the work that went into creating and maintaining elaborate parallax-scrolling effects, and so the trend dwindled in popularity. For a while.

Fast forward to today. Just when we thought the web was safe, parallax scrolling is making a comeback. Like a sequel to a movie, our testing today reveals a familiar cast and storyline: unimpressed users and a range of usability issues. In this sequel, however, parallax scrolling is more restrained than the original. If the earlier parallax implementations were a horror show of usability issues, the modern version is closer to a PG-13 family comedy: not particularly entertaining, but also not likely to send people screaming to close the tab.

> The **parallax animation** effect is created by two or more layers of an interface moving at different speeds or in different directions in order to produce an impression of depth.

(To understand why parallax design induces this illusion, try this experiment: hold up both of your hands in front of your face, with one hand as far away as you can stretch your arm, and the other hand halfway between the first hand and your eyes. Now move your head from left to right while holding your hands steady: it’ll look as if the two hands are moving relative to each other, particularly if you close one eye so that you get a 2D view.)

The animated GIF below shows an example of parallax scrolling on a restaurant’s website.

![Animated GIF of parallax animation on a restaurant website](https://media.nngroup.com/media/editor/2018/09/28/parallax_example.gif)

*RestaurantLeDuc.com: In this example of parallax scrolling, the fish and the white menu boxes move at different speed than the scrolling background, creating the impression of being layered on the screen.*

In this article, we’ll discuss why parallax is a popular trend, why it can be problematic, and how it can still sometimes be used to enhance user experience.

## In This Article:

- [Why Designers Use Parallax](#toc-why-designers-use-parallax-1)
- [4 Problems with Parallax](#toc-4-problems-with-parallax-2)
- [Make It Work: Use Restraint and Put Users in Control](#toc-make-it-work-use-restraint-and-put-users-in-control-3)
- [Conclusion](#toc-conclusion-4)

## Why Designers Use Parallax

If you ever played early video games, you may remember the parallax effect. Game designers moved objects in the foreground and background separately, to add depth to the game universe and make players feel immersed in it. The same desire to offer an “immersive” experience on the web often motivates the use of parallax effects by website designers, who assume that such effects make for a creative, unique branding statement and a memorable design.

Another reason for using parallax is to call attention to certain page elements. The velocity of motion is a **preattentive trait**: an object that moves at different speed than everything else in a scene stands out like a cheetah sprinting through open grasslands; people will notice it without making any explicit effort to search for it.

Unfortunately, **parallax effects come with some costs**. Designers need to know what their risks and benefits are.

## 4 Problems with Parallax

For sites considering adopting (or readopting) this trend, let’s look at some of the top UX issues with the parallax scrolling effect.

1. **Parallax-presented content can be difficult to control.** While parallax is supposed to draw attention to the animated elements, often these elements end up being ignored. Most users in our testing don’t wait for parallax effects to load: they scroll quickly, scanning for keywords of interest. Because this effect takes time, goal-oriented users looking for specific information may miss important content presented using parallax. 

**Pages can take longer to load** when parallax animations are used. On the Apple site, some users scrolled and saw almost nothing on the screen, because the parallax effects hadn’t animated yet. Blank screens are not what designers intended, nor are they what users came to see.

![Slow-loading parallax effects resulted in three near-blank screens on an iPhone](https://media.nngroup.com/media/editor/2018/09/28/applecom_mob_parallax-blankscrolls.png)

*Apple.com: A study participant encountered screens of blank space, because the parallax-animated text and images hadn’t loaded as quickly as he had scrolled down. The user had to keep scrolling to get the content to appear, then he scrolled back up to the start of each section so that he could read the text and look at the images.*

But too fast parallax can be a problem, too: when the animation is tied to users’ scrolling speed, people may not get a chance to read animated text if they scroll too fast. One user scrolling on the *New York* Times mobile site noticed a panel of text scroll up and past the graph she was reading. She commented, “Oh, that happened so quickly I didn’t even get to read it.” The effect delayed her ability to interpret the graph and feel in control of the experience.

![A block of parallax-animated text scrolled quickly off the screen](https://media.nngroup.com/media/editor/2018/09/29/nytimescom_parallax_quickscroll.gif)

*NYTimes app for iPhone: A fast-scrolling user caused parallax-animated text to scroll so quickly over and then off the user’s screen that she didn’t have time to read it.*
2. **Too much movement, especially of text, can be dizzying.** Using parallax to animate many different page elements and blocks of text [makes reading hard](https://www.nngroup.com/articles/scroll-animations/) and can even cause people to feel sick. If this sounds exaggerated, remember that in 2013, Apple released an update to [iOS 7](https://www.nngroup.com/articles/ios-7/) that allowed users to *Reduce Motion*, because the parallax animations for task switching caused many people to feel symptoms of vertigo, nausea, and dizziness. Having learned from that mistake, let’s hope future parallax [doesn’t cause harm](https://www.nngroup.com/articles/distracted-driving-ux/).
3. **Parallax effects might be missed entirely.** By now, users have learned that many advertisers use motion to attract attention. Some people purposefully ignore movement on a page because of the association with unwanted advertisements. On mobile, subtle parallax effects are easily missed because the user’s hand can block animations that appear underneath. Overlooking the parallax effects may not be harmful to the experience (as long as the content doesn’t go away), but designers should consider whether these effects are worth the effort to build and maintain.
4. **Parallax is just not that impressive to users .** The people most likely to appreciate parallax effects? Other designers or developers. When you know what goes in to building something complex like long-scrolling parallax pages, you can appreciate the work. But, to put it bluntly, average users could care less. Today, users’ reaction is the same as five years ago: indifference. They aren’t “wowed.” User-testing participants don’t stop to comment on how cool the effects are; they don’t scroll up and down for fun, to watch the effects bring the page to life. They don’t pause to watch each effect smoothly transition into the main content area. Instead, the vast majority of **people are focused on content**, and so the animation effects are an afterthought, if they’re noticed at all. The question to designers, then, becomes: is parallax the best way to impress users or make a brand statement?

(A note about doing user research on the impact of parallax or other animations: if you prompt users to talk about the animation on scroll, you might hear comments that praise the interaction design. Use caution before celebrating such comments: sometimes users say one thing, but their behavior shows a completely different reality. As soon as you’ve directed users’ attention to a feature, you’ve biased their interpretation of that feature. For example, at the very end of two testing sessions in which one participant struggled to control the parallax-animated text blocks and the other did not notice them, we asked people about any movement they saw on the page. That was when they gave praise, with comments like “Oh that’s so cool” or “That’s so cute how it appears as you go down the page.” But we shouldn’t forget what really happened when they were trying to find an answer or read an article: they struggled or ignored the parallax.)

## Make It Work: Use Restraint and Put Users in Control

As I said at the beginning of this article, the latest iteration of parallax is subtler than five years ago. This is a good thing. Remember that parallax is a form of animation, and, [for most animations, less is more](https://www.nngroup.com/articles/animation-usability/).

**No task, no problem.** Parallax is safest in environments where users are browsing for leisure, without a specific goal or task in mind. In those cases, parallax can be used to support a narrative or to contribute to a brand’s identity. If you’re not sure whether your use case fits this category, you can always refer to [the 3 Bs Test](https://www.nngroup.com/videos/3-bs-design-trends/) to see if parallax is a good choice for your business and your users.

**If users have a task, put content first.** The ultimate test of parallax usability is whether users can easily and quickly complete their task. To start, here are some suggestions:

- [Provide in-page navigation links](https://www.nngroup.com/articles/in-page-links/) on long scrolling parallax pages, so that scrolling isn’t the only way to navigate down the page. Use noticeable navigation UI, not just small vertical dots, which are likely to be missed (and have poor [information scent](https://www.nngroup.com/articles/information-scent/)).
- Save parallax effects for background or peripheral images, so that they are easy to ignore and don’t detract from the content.
- Once users have scrolled down the page and triggered all the parallax effects on the way down, leave those objects in their final positions, instead of reanimating each object on scroll up or scroll down. In a goal-oriented context, once users begin to go up and down a page, it’s because they’re looking for information. Forcing people to rewatch parallax effects delays their access to that information and can quickly become tedious and irritating. It’s like listening to the same joke again and again. Show restraint here, and your users will benefit.

In the following example, parallax scrolling animations are used to circle key descriptions of an iPad. The animations are subtle, but they call attention to key features about the device. They also remain in place — the keywords remain circled — as users scroll up or down the page. (Note that this is the same page that suffered slow page-load times caused by the larger parallax effects of iPad images sliding into view. The smaller subtler effects are not likely to cause such delays).

![Parallax animations circle and underline keywords as a user scrolls](https://media.nngroup.com/media/editor/2018/09/28/parallax_ipad.gif)

*On the iPad product page, users didn’t notice the subtle parallax animations, for example underlining or circling callout text. But the effects did not interfere with users’ ability to read the page. The markup-style animation also reinforced some of the page content, by showcasing the possibilities of using the Apple pencil with the tablet.*

## Conclusion

Trends may come and go, but human behavior remains largely unchanged. The risks of parallax effects remain the same as years ago, because people are still focused on their goals and they are impatient with slow-loading sites. Fortunately, we can learn from past mistakes. If your team is considering parallax, make sure that it won’t intrude on users, slow them down, or take away their ability to quickly and easily find what they came for.

### Reference:

Healey, C.G., *Perception in visualization* Department of Computer Science, North Carolina State University, available at: [https://www.csc2.ncsu.edu/faculty/healey/PP/](https://www.csc2.ncsu.edu/faculty/healey/PP/)
