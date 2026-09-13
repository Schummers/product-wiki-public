---
title: "The Power Law of Learning: Consistency vs. Innovation in User Interfaces"
date: "2016-10-30"
url: "https://www.nngroup.com/articles/power-law-learning/"
author: "Raluca Budiu"
topics: [psychology-and-ux]
type: article
---

In response to one of our recent articles on centered logos vs. left-aligned logos, one reader tweeted: “Every @NNgroup newsletter, summarized: Do things exactly the way every other website already does them, or your users will be confused.”

Although obviously a hyperbole (we publish articles on a wide variety of topics), the tweet does identify a big theme in many of our articles and one of the main principles of user experience: **consistency**. Consistency is one of the original [10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) and is a corollary of [Jakob’s law of Internet use](https://www.nngroup.com/videos/jakobs-law-internet-ux/). As disappointing as it may be for designers to have to follow the same beaten path, we preach consistency again and again for reasons deeply rooted in basic human behavior. In this article, we explain the most fundamental of these reasons: the power law of learning.

## In This Article:

- [Learning Studies and Learning Curves](#toc-learning-studies-and-learning-curves-1)
- [The Power Law of Learning](#toc-the-power-law-of-learning-2)
- [Analyzing a Learning Curve](#toc-analyzing-a-learning-curve-3)
- [Memory and the Power Law of Learning](#toc-memory-and-the-power-law-of-learning-4)
- [Consistency = Boring, Old Interfaces?](#toc-consistency-boring-old-interfaces-5)
- [References](#toc-references-6)

## Learning Studies and Learning Curves

The best way to measure how people learn a task or an interface is by running a **learning experiment**. In a learning experiment, people come into the lab and do the same task *multiple times*. Each time the person does the task, the experimenter records one or more quantitative metrics (usually, the time it takes to do that task and the number of errors). If the measures get better, people have learned from their previous experience, and the numbers show how much. The repetitions of the same tasks may or may not be separated by different activities, and sometimes participants are even sent home between two measurements, and asked to come back after a day, a week, or a month.

One of the first rigorous learning experiments was described by Hermann Ebbinghaus in 1885 in his book on human memory. Since then, many other learning experiments have been reported in the psychology, human-factors, and HCI literature. All these experiments show that “practice makes perfect:” when people do the same task over and over again, they get better and faster. The chart below shows the results from one such study by David Ahlstrom and colleagues, who were investigating [pie menus](https://www.nngroup.com/articles/expandable-menus/) and comparing them with other types of menus.

*Ahlstrom et al.’s study had participants interact with the same menu interface for 8 different practice blocks — in each block participants selected the same 6 items in the menu, and the obtained selection times were averaged to get the mean time for that block. The learning curve shows that the mean selection time decreases with practice.*

This type of graph that plots the results from a learning experiment is a learning curve. **A learning curve** describes how a specific quantitative measure of the same human behavior changes as a function of time. In the menu experiment, the measure of interest is the task time — the mean time to select an option inside the menu. But the measure can vary from one learning experiment to another: it can be any metric that you’d expect to change as a result of learning. For example, if we were interested in UX education, we may ask people with the same background to facilitate a user test once, and measure how many facilitation errors they make. We would give them feedback on those errors, and then we would ask them to come a second time to facilitate a user test. After a few such repetitions, we would plot the average number of errors made for each test. That graphic of errors over time would represent a learning curve.

## The Power Law of Learning

In the 1980s, Allen Newell, a famous Carnegie Mellon cognitive scientist, analyzed reaction times for a variety of tasks reported in learning experiments and he noted that the learning curves obtained in all these studies had a very similar shape: that of a so-called **power law**. Power laws have a nice mathematical property: when you plot them in log-log scale, you obtain a straight line.

*The learning curve in Ahlstrom’s menu experiment is described by a power law; when plotted in log–log scale, it is well approximated by a straight line.*

Definition: **The power law of learning** says that (1) the time it takes to perform a task decreases with the number of repetitions of that task; and (2) the decrease follows the shape of a power law.

Newell focused primarily on time as the quantitative measure of learning, but there is evidence that the power law holds for other measures as well.

## Analyzing a Learning Curve

Although learning curves can be described by power laws, they won’t be described by the *same* power law.

Let’s assume that we were interested in analyzing the learnability of three different interfaces A, B, and C for the same task (e.g., answering a customer query in a call center). For each design, we ask participants to complete the task in different, repeated trials and we measure the task time for every trial. Then we plot the average task time corresponding to each repetition and we obtain three learning curves like the ones in the figure below.

*Three learning curves for three different interfaces*

Notice that in the first trial participants take roughly the same amount of time with all designs. But by the second repetition, design A is much faster than designs B or C. By the 3rd repetition design A speeds up even more, and after the 4th repetition the reaction times reach a plateau: the curve flattens out and the users have learned the interface as much as possible. There are no more improvements to be expected, and extra repetitions will only decrease the reaction time insignificantly. We can say that, with design A, **learning is saturated after the 4 th repetition**(or that 4 is the saturation point for design A)**.**

The learning curve for design C also flattens, but the plateau is reached later, by approximately the 10th or 11th repetition. So design C requires more practice to stabilize the performance. In other words, it takes people more trials to learn how to use design C than design A.

Moreover, design A exhibits more improvement: the difference between the highest and the lowest points on the learning curve is approximately 20s (22 for repetition 1 and 2 for repetition 15), whereas for design C this difference is approximately 19s. So with design C participants don’t speed up as much as they do with design A.

Design B also reaches saturation later than design A (approximately by repetition 11), but the improvement is bigger. More importantly, the expected task time after the interface has been learned is lower for design B than for design A (1s vs. 2s). In other words, design B takes longer to learn than design A, but once it has been learned, people are faster at using it.

The choice between A and C is easy: A is better in every way, with an earlier saturation point, a greater speedup, and a superior task time once the interface has been learned. But the choice between A and B depends on whether in real life users will be exposed to enough repetitions to reach the saturation plateau. If, for instance, you expect people to use the interface every day as part of their work, then it makes sense to go with design B, because in the long run it will save more time. (During the first week of use, A will be better, but halfway through the second work week B becomes better, and then it stays better forever.) However, if your users will use the design occasionally, with large intervals of time between two different sessions, then design A will be better because it will help people learn the interface faster.

Let’s consider two enterprise software examples:

- The employee directory: assuming that most people use it once a day, we should prefer a user interface like design B for this type of application.
- Reclaiming value-added taxes for foreign travel in expense reporting: we should prefer a user interface like design A if most people go on, say, at most one business trip abroad each year.

The ratio between the improvement and the saturation point indicates the *slope of the learning curve*: if the curve drops a lot and fast, then it means that the interface is highly learnable. If the curve drops only a little, or it takes many trials to reach the saturation point, the interface is less learnable. So the term “steep learning curve” is actually a misnomer — in reality, steep learning curves are good. They mean that the improvement is substantial and that it happens fast.

## Memory and the Power Law of Learning

Romans used to say that “repetition is the mother of learning” — the more we rehearse a piece of information, the more likely we’ll be to remember it. Not only that, but we’ll also be faster at retrieving it from memory. When applied to human memory, the power law of learning says that the time it takes to retrieve a piece of information from memory depends on how much we’ve used that information in the past, and this dependence follows a power law. Thus, we are fluent with concepts and patterns that we use every day in our work, yet high-school math (such as the definition of logarithms) or other facts that we don’t often encounter are hard to remember, because we haven’t used them often enough.

*In an experiment reported by Peter Pirolli and John R. Anderson (1985), the time it took participants to recognize facts that they had studied decreased with the number of days they had practiced those facts. The curve follows a power law and reaches a saturation level approximately around day 12.*

Items that are practiced a lot acquire [a high activation in our memory](https://www.nngroup.com/articles/recognition-and-recall/) and are retrieved faster. Whenever we’re trying to solve a problem or recall a piece of information, the first things that come to mind are those items in our memory that have a raised activation. Let’s say you want to navigate to the homepage of a site. You may have encountered multiple solutions to this problem in the past — for example, clicking the logo or clicking a *Home* link. All these solutions will compete in a “race” in your memory and you will select the one that gets to the finish line first. But, based on the power law of learning, the one that wins the race is the one that’s been practiced most often. Of course, if the first winning solution doesn’t work, people will try the next best. But they will also start feeling annoyed and perceive the problem as harder, and the site as less usable.

The key implications of this research are as follows:

- The power law of learning is real: it’s been proven in countless experiments during a very long period (the 19th, 20th, and 21st centuries). It’s the way the human brain works, and no degree of wishful thinking or new gadgets will change this. Design for it.
- Learning is not a dichotomy (as a simplistic model might have assumed), where either you know something or you don’t. The more something is practiced, and the more recently it was practiced, the better it’s known.
- Just showing users a tutorial or help screen isn’t enough to make them learn something well.
- Doing something often is the way to strong learning.

## Consistency = Boring, Old Interfaces?

We’ve seen that every repetition helps users practice a concept or an action. So, by being consistent with other sites, you’re giving users one more repetition of a highly common UI element, and you’re also reaping the benefits of practice on all these other websites. Remember Jakob’s law: your users spend most of their time on other websites.

*Learning curves for two different interfaces: when the new interface is introduced, the old one is already at saturation level (repetition 1 for the new interface corresponds to repetition 5 for the old one). It’s going to take a lot more time and good will for the user to put up with the new suboptimal interface than to continue using the old one.*

As shown in the graph above, when you are creating a new design pattern that goes against an old, familiar one (e.g., logo on the [right](https://www.nngroup.com/articles/logo-placement-brand-recall/) of the page instead of on the left, [horizontal scrolling](https://www.nngroup.com/articles/horizontal-scrolling/) instead of vertical scrolling on desktop, [hamburger menu instead of a navigation bar](https://www.nngroup.com/articles/mobile-first-not-mobile-only/) on desktop), the learning curve for the new pattern will be in the steep, high part of the first repetitions, while the learning curve for the competing old alternative will have already reached saturation. It’s going to take more than a few repetitions for your new design to also reach saturation and perhaps prove better than the competing one. Unless your users are captive and you can force them to practice, chances are that they will give up and go elsewhere instead of putting up with a harder to use design: [users hate change](https://www.nngroup.com/articles/fresh-vs-familiar-aggressive-redesign/).

So that means there’s no hope for innovation, right? We are doomed to have the search box in the top right corner, the [logo on the left](https://www.nngroup.com/articles/centered-logos/), and the navigation in a bar?

Any type of innovation will incur a cost for users and for designers. For users, because it will be a new pattern that they must learn and that takes them on an untrodden, slow path. For designers, because they must provide extra scaffolds such as contextual [tips](https://www.nngroup.com/articles/mobile-instructional-overlay/) and [progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/) to help users navigate on the new path. The cost of implementing these tools can be significant. Think twice at what you are trying to achieve — is it worth departing from the well-beaten path? Does it make sense to innovate or will you be just as well served by a traditional design?

It also means that innovation is easier push when you have a captive audience or when the [perceived value](https://www.nngroup.com/articles/perceived-value/) of a [brand](https://www.nngroup.com/articles/brand-experience-ux/) is a lot bigger than the cost of using a new design pattern. That’s why traditionally, big companies with a large user base (think Apple and iOS or Google and Android, to a lesser extent) can afford to innovate — because people who are already using these platforms will have to put up with the new interface (especially if the company is pushing updates aggressively, like Apple does with iOS, or the innovation happens in an enterprise, where users don’t have a choice to go back to an older version of the interface).

It’s also easier to innovate if your users will experience the new interface very often, perhaps several times a day. That means that people will get faster to the saturation part of the learning curve because they will have quite a few opportunities to practice. (Yet, if the saturation point is too far in the future, people may actually never get there. [Windows 8](https://www.nngroup.com/articles/windows-8-disappointing-usability/) is a live proof of that: Microsoft ended up changing the design instead of waiting for users to reach the saturation plateau.)

Innovation can also happen if designers adopt it en masse and create a new standard. If all websites rebelled tomorrow and started placing the logo in the top right corner, then users would get the repetitions needed to reach saturation relatively fast, everywhere. Usually, this process takes time, but it did happen with design elements such as the swipe-to-delete gesture in iOS or the [hamburger menu on mobile](https://www.nngroup.com/articles/hamburger-menus/).

We can make a simple decision tree for whether to introduce a deviant user interface in cases where a conventional design is already well established:

1. Will the new design perform *much* better than the old, once users have “descended” the learning curve? If not, don’t even try.
2. Is it credible that users will be willing to try the new design again and again, until they have learned it well enough to realize those long-term benefits? If people are likely to give up (e.g., leave a website for a competing, familiar design), then don’t introduce the new design.
3. Can you speed up learning, either by exposing users to the new design more often or by making it easier to learn? If yes, you will increase the proportion of users who will be willing to embrace the new design.

So yes, consistency is the curse of innovation in design. If you’re convinced that, once your users will have learned the interface, they will save time over the status quo, then it can be worth trying. But remember that the path to innovation is circuitous and costly, and if your users won’t have many learning opportunities, they may never reach that optimal-performance plateau accessible only after learning has happened.

Learn more about human memory and the power law of learning in our seminar on [The Human Mind and Usability](https://www.nngroup.com/courses/human-mind/).

## References

David Ahlstrom, Andy Cockburn, Carl Gutwin, Pourang Irani (2010). Why It’s Quick to Be Square: Modelling New and Existing Hierarchical Menu Designs. CHI 2010.

Hermann Ebbinghaus, (1885). [Memory: A contribution to experimental psychology](http://psy.ed.asu.edu/~classics/Ebbinghaus/index.htm)*.* New York: Dover.

Allen Newell, Paul Rosenbloom (1980). [Mechanisms of skill acquisition and the law of practice](http://repository.cmu.edu/cgi/viewcontent.cgi?article=3420&context=compsci)*.* Technical Report. School of Computer Science, Carnegie Mellon University.

Peter Pirolli, John R. Anderson, J. R. (1985). [The role of practice in fact retrieval](http://act-r.psy.cmu.edu/wordpress/wp-content/uploads/2012/12/283pirolli-1985-practice.pdf). *Journal of Experimental Psychology: Learning, Memory, & Cognition*, 11, 136-153.
