---
title: "Scrolljacking 101"
date: "2023-08-06"
url: "https://www.nngroup.com/articles/scrolljacking-101/"
author: "Sara Paul"
topics: [design-patterns, interaction-design]
type: article
---

Scrolling is a basic interaction that enables users to see pixels that span beyond the length of a screen height. Scrolljacking is a relatively recent design trend that involves changing the normal pace or direction of scrolling on a website. In our usability testing, we observed that websites with scrolljacking exhibit significant threats to user control and freedom, discoverability, attention, efficiency, and task success.

## In This Article:

- [What Is Scrolljacking?](#toc-what-is-scrolljacking-1)
- [Why Is Scrolljacking Used?](#toc-why-is-scrolljacking-used-2)
- [Research Study: Findings](#toc-research-study-findings-3)
- [Scrolljacking Best Practices](#toc-scrolljacking-best-practices-4)
- [Conclusion](#toc-conclusion-5)

## What Is Scrolljacking?

[Consistency and following established interaction conventions](https://www.nngroup.com/articles/consistency-and-standards/) improve website usability. When it comes to scrolling, users have strong [mental models](https://www.nngroup.com/articles/mental-models/): they expect to scroll vertically, at a consistent rate that is related to how they are physically interacting with their input device.

In most computer operating systems, the default scroll speed can be manually adjusted to be more sensitive or less sensitive, but it is always consistent. Users expect a consistent scroll rate across all the applications on their devices.

When a website alters the default scroll functionality, it “hijacks” the user’s control over their device and can generate disorientation.

> Definition: **Scrolljacking** (or **scroll hijacking**) is a design pattern that changes the speed and, sometimes, the direction of scrolling on a web page.

*Apple.com: The scroll rate changes as the user moves down the page. At several points, scrolling does not advance the page but, instead, causes additional text and animations to appear (as evidenced by the scrollbar on the right, which continues to move down even though the page position remains the same). To go back to the top of the page, the user must scroll through the animations again.*

## Why Is Scrolljacking Used?

There are a few common reasons why designers use scrolljacking.

### Break Down Information

Scrolljacking is used to break down complex or information-dense topics and visuals into digestible chunks. For example, in the above example of the Apple Watch Ultra, the scrolljack enables a granular, step-by-step visual breakdown of eight physical features on the watch. As a result, minute technical details can be highlighted one at a time, to avoid overwhelming the user with too much information at once.

### Guide Storytelling

The second reason designers use this pattern is to guide [storytelling](https://www.nngroup.com/articles/persuasive-storytelling/?lm=persuasive-storytelling-adapt-vocabulary&pt=youtubevideo). For example, on the BBC website, the scrolljack serves the functional purpose of adding supporting information through [progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/).

*BBC.co.uk: Scrolling down reveals a “before the blast” image; scrolling further then triggers a gradual horizontal overlay showing the “after the blast” photo and related information.*

BBC’s use of scrolljacking was very successful in our testing because it helped participants comprehend the information and visualize the disaster. However, a couple of users incorrectly assumed the final image was the end of the page ([illusion of completeness](https://www.nngroup.com/articles/illusion-of-completeness/)), because scrolling a couple more times didn’t show anything new.

### Communicate Brand Personality

Designers are brand reinforcers who translate the brand into user-experience interactions. Then, customers interpret the brand based on the sum of their experiences with the brand over time.

For example, Therabody’s [brand vision](https://www.nngroup.com/articles/ux-brand-terms-defined/) is “everybody deserves to feel better and live life on their own terms.” The use of a trendy pattern like scrolljacking on its website is likely intended to bolster one of the company’s brand attributes (innovation).

*Therabody.com: The use of scrolljacking on this product page is likely meant to bolster its innovation brand attribute and to highlight images of people using the product.*

However, [usability is the foundation for delight](https://www.nngroup.com/articles/theory-user-delight/), and a seemingly aesthetic scrolljack with no real function can negatively impact the customers’ brand perception if it is disorienting. On the Therabody website, a study participant who tried to scroll down on a scrolljacking page was surprised and disoriented that nothing happened upon scrolling.

## Research Study: Findings

Several years have now passed [since scrolljacking was first introduced to the web](https://www.nngroup.com/articles/scroll-animations/); today it is a somewhat common pattern. We wanted to know whether users have become familiar with this pattern and whether it still causes any usability issues.

To better understand this pattern, we conducted a usability-testing study in which we tested websites from multiple industries. All used some form of scrolljacking.

Below are our findings and recommendations.

### Scrolljacking Caused Disorientation

There is a delicate balance between lessening users’ [cognitive load](https://www.nngroup.com/videos/cognitive-load/) through [progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/) and minimizing disorientation caused by the scrolljack animations. The majority of our study participants were at least mildly disoriented by scrolljacking. We observed this sense of disorientation across multiple similar sites, where participants did not hesitate to click away from the page or refresh it.

This disorientation was severely exacerbated when scrolljacks were excessively lengthy, interfering with normal scrolling for most of the page’s length. When this was the case, users sometimes interpreted the scrolljack as a bug.

For example, in our study, an entire page on Crypto.com used scrolljacking. All participants who visited it were disoriented. One participant had to go back through the page because he “got lost” and did not comprehend the story told on the scrolljacking page. He referred to going back as “a hassle.”

*Crypto.com: A study participant scrolls through a page that uses scrolljacking and becomes disoriented because of its excessive length.*

Some participants who became disoriented on Crypto.com rapidly scrolled back up and then back down to read the content multiple times so they could remind themselves of where they were. Others thought their normal method of scrolling (e.g., mouse) broke and reverted to clicking or dragging their browser scrollbar to scroll. Many also tried to refresh or even leave the page as a final attempt to regain lost control.

In contrast, when the scrolljack was short (like on the BBC News site), users were able to maintain a sense of orientation because it wasn’t too long before they hit a section of the page that resumed normal scrolling.

### Scrolljacking Worked Best When It Had Functional Value

Scrolljacks were best tolerated when they were used to progressively disclose relevant information. For example, on the BBC News website most study participants tolerated the scrolljack well and even benefited from it, because it added contextual information. However, it still disoriented some participants, causing them to hesitate and double check their place on the page.

### Faster Scrolling Rates Worked Better

When the number of scroll interactions required to see something change on the screen was small, scrolljacking caused less disorientation. In other words, when users could quickly see the result of one or two scroll interactions, whether it be a single swipe on a mobile device, a multifinger swipe on a laptop, or turning the mouse wheel on desktop, they were more likely to engage with the site.

However, some sites with faster scroll rates required **too much scrolling precision:** the user needed to scroll down to the exact right screen coordinate to see a particular piece of information appear; the information would disappear as soon as the user scrolled the slightest bit further.

Therefore, designers have to pick **the right scroll rate so that it’s not too slow, nor too fast**. A too-fast scroll rate means users are prone to miss things, but a too-slow scroll rate means they could experience scroll fatigue. Run [usability tests](https://www.nngroup.com/articles/usability-testing-101/) to identify the scrolling rate that is just right for a particular page.

### Task-Oriented Users Were Highly Annoyed by Scrolljacking

Task-oriented users did not have nearly as much patience for scrolljacking as users who were just exploring the site.

One task-oriented participant was asked to evaluate Reachdesk’s offerings as a solution for their role in sales. The website changed the user’s scroll rate and direction. He said, “That was a full swipe, and it moved nowhere. . . if I were looking at this as a prospect, I would get severely agitated and just move on.” The use of scrolljacking frustrated him and distracted from important content contained on the page.

*Reachdesk.com: In this clip from our usability study, the use of scrolljacking distracts the task-oriented participant from the page information.*

On the UT Austin website, a prospective college student was asked to find information that she might use to evaluate whether she would consider applying to the school. She began to search for information about how to transfer credits but ran into a scrolljack and felt that the scrolljack “wasted” her time. This sentiment was echoed by other prospective students in the study, too.

On the other hand, users who did not have a specific goal were willing to keep trying even if their scroll interaction was seemingly not moving them anywhere.

However, we know from past research that most users are goal-oriented, and, if the path to success is not frictionless, they will be likely to leave.

### Altered Scrolling Rate and Direction + Changing Text = Worst Usability

Pages that altered the rate and duration of scrolling while also requiring the user to read text exhibited the most severe usability issues. That was because users had to balance the reading of animated text with the scrolling interaction necessary to keep moving through the content at a reasonable rate.

This is what we observed in the ReachDesk example above: all participants who encountered this scrolljack quickly became very frustrated. In contrast, on the Therabody website, user frustration was minimal even though the pace and direction of scroll changed, too. The experience was better because people didn’t have to read any text while experiencing the horizontal scrolljack. Even so, one participant who used the Therabody website could not figure out how to navigate back up the page and tried to swipe horizontally, not realizing that he needed to use a “swipe down” motion to get back up to the top.

This is likely because content that unfolds horizontally is similar to a [carousel](https://www.nngroup.com/articles/designing-effective-carousels/), where the horizontal swipe is appropriate. There is a risk that people will not know how to get back to the top of the page if the page uses horizontal scrolljacking.

### Scrolljacking Is Worse on Mobile

The smaller mobile screen translates to scrolljacks that are longer in duration and have the chance to be even more disorienting. Further, due to poorer connection speeds, pages sometimes take longer to load on a mobile device, so a couple of participants had to wait for a long time for the text and visuals to display properly. When sites did not carry scrolljacking over from desktop to mobile, users had a much better experience.

### Sticky Navigation Serves as an Escape Hatch

Scrolljacking was more disorienting on websites where the navigation did not remain visible as the user scrolled. When participants ran into a confusing scrolljack, they clicked on the [sticky navigation](https://www.nngroup.com/articles/mobile-navigation-patterns/) to exit it. However, that was possible only when the site had a sticky navigation. Additionally, many sticky navigation menus were collapsed on mobile and thus harder to find — another reason why recovery from a scrolljack gone wrong was more difficult for users on mobile.

## Scrolljacking Best Practices

Our research findings tell us that scrolljacking leads to more user pain than benefits. If, however, your stakeholders still insist on using this pattern, minimize its negative impact on usability by adhering to the following guidelines.

### The Scrolljack Should Progressively Disclose Valuable Information

A scrolljack is beneficial when it gradually adds supporting information to lessen cognitive load and support storytelling. When it does not serve this function, it is not worth it: it requires more work for the user with no benefit.

Ensure that scrolljacking is used only for showcasing critical pieces of information. For example, on the Apple website, scrolljacking is used to break down the features of the Apple Watch Ultra and to map them to the physical device. To determine whether the scrolljack has a functional purpose in your design, ask the following questions:

- What purpose does scrolljacking serve? 

  - Does it add relevant context?
  - Does it break down a complex concept?
  - Does it communicate something about your brand?
- To justify implementation costs, do we have research to support that this functional purpose is valuable to users?
- What meaning is lost when the scrolljack is removed?

### Test Your Scroll Rate to Minimize Scroll-Interaction Costs

Users want to move through information as efficiently as possible, and they will invest only a limited amount of effort before leaving. The more attention users must dedicate to moving through a page, the [fewer cognitive resources they have for processing the information](https://www.nngroup.com/articles/attention-economy/) on the page.

Thus, there is a chance that, if scrolljacking is too fast or too slow, users will never discover the information in the scrolljack or below it. To minimize disorientation and frustration resulting from scrolljacking, require users to work as little as possible for the information they want by optimizing the scroll rate.

### Include Nonscrolljack Sections on the Page

If users land on a page that is entirely scrolljacked, it lacks familiarity to a large degree. Users are used to pages that scroll in the normal fashion. By balancing an unfamiliar scrolljack with the familiar scroll pattern, you reduce the negative impact of the scrolljack and create a greater sense of user control and freedom.

### Avoid Changing the Scroll Direction

When the user is performing the gesture used for vertical scrolling, but the page starts scrolling horizontally, there is a high chance that they will get disoriented and not understand what is happening. They may stop scrolling and miss the other information on the page, or they may leave the page altogether.

### Limit the Amount of Text In Scrolljacks

Numerous participants in our research struggled to comprehend text contained in a scrolljack. When relatively small chunks of text appear and then disappear from the screen, users may need to hold information in their [working memory](https://www.nngroup.com/articles/working-memory-external-memory/) in order to fully comprehend what the page is aiming to convey. Therefore, we advise against including important content inside of a scrolljack section to maximize comprehension and efficiency and minimize [cognitive load](https://www.nngroup.com/videos/cognitive-load/).

### Avoid Scrolljacking on Mobile

Most usability issues observed on desktop were exacerbated on mobile. On mobile devices, users face unique constraints such as touch-only input and a smaller screen. Scrolljacks that work reasonably on desktop may not translate well to mobile and you may need to come up with a mobile-specific implementation. Assess whether the benefits of scrolljacking are worth the additional implementation costs: in most cases, they are not.

### Use Scrolljacking Only Below the Fold

[Web users spend 80% of their time looking at information above the page fold](https://www.nngroup.com/articles/scrolling-and-attention-original-research/). A scrolljack above the fold is much more likely to cause frustration simply because it will be more discoverable. Therefore, if you are going to use scrolljacking, use it below [the fold](https://www.nngroup.com/videos/fold-manifesto/) to highlight key calls to action already present above the fold.

## Conclusion

Scrolljacking is a design pattern that can do more harm than good if not executed in a manner that maximizes user control and efficiency. Even then, it is risky. Our user research showed that scrolljacking is likely to cause disorientation and frustration.
