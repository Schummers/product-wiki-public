---
title: "Working Memory and External Memory"
date: "2018-04-29"
url: "https://www.nngroup.com/articles/working-memory-external-memory/"
author: "Raluca Budiu"
topics: [human-computer-interaction, psychology-and-ux, web-usability]
type: article
---

When people use websites or other user interfaces, a frequent cause of difficulty is that they forget information from a previous step even though it's needed at a later stage to complete their task. This is not because users are particularly forgetful. Nor is it because they don’t bother paying attention — though never make the mistake of assuming that figuring out how to use your site is the most important thing in the world. No, the reason people forget information in the middle of the task is that the user interface requires them to keep in their working memory more than what their brains can hold.

## In This Article:

- [What Is Working Memory?](#toc-what-is-working-memory-1)
- [Relationship to Short-Term Memory](#toc-relationship-to-short-term-memory-2)
- [Working Memory and User Experience](#toc-working-memory-and-user-experience-3)

## What Is Working Memory?

Suppose someone asked you to add the numbers 353 and 489 in your head. How would you do it? Some may try to mentally line up the numbers and then add the corresponding digits for units, tens, and hundreds, respectively. Others may transform one of the numbers into an “easy” number (such as 300 or 500) and then add it to the other number (for example, by adding 11 to the second number and subtracting 11 from the first to get 342+500).

Whatever the method, chances are that the task will be challenging. To solve it, we have to keep a lot of information around: not only the exact numbers to be added, but also the intermediate products of the addition. This task is difficult because it **taxes our working memory**.

> **Human working memory** can be conceptualized as a buffer or scratchpad in which the mind deposits information relevant to the current task.

The working-memory buffer has limited capacity — think of it as an egg carton with a small number of slots. If a task requires too much information to be kept in the working memory, we need to free up some of the occupied slots to make space for that information. What is removed from working memory can, in fact, still be needed to finish the task, and we may end up working harder to recover that data; as a result, we may take longer to do the task or make [mistakes](https://www.nngroup.com/articles/user-mistakes/). In our addition example, we may end up dumping out a carry or digit from one of the original numbers, and produce the wrong answer.

The concept of working memory was first illustrated in a famous series of experiments by the psychologists Alan Baddeley and Graham Hitch from University of Stirling, in Scotland. In these experiments, participants were given 1 to 6 digits to keep in their memory while doing a different task where they had to judge if a sentence matched the order of presentation of two letters. The more digits people had to store in their memory, the worse the performance in the second task was. The experiment suggested that part of the participants’ working memory was occupied with storing the digits, so they had fewer slots available for the second task. (This process is roughly similar to **thrashing** in computer science — a phenomenon where the processor doesn’t have enough internal memory available to store all the info for a task and ends up repeatedly dumping part of it on disk and loading other info from disk.)

*In Baddeley and Hitch’s experiments, people had to store some digits in their working memory and remember them after doing a second task. When the number of digits they had to remember was small (1–2), their performance in the second task did not suffer. But when they had to remember more digits, their performance did deteriorate, because they had less working memory available to them for that task.*

## Relationship to Short-Term Memory

Working memory and [short-term memory](https://www.nngroup.com/articles/short-term-memory-and-web-usability/) are related, and sometimes, even in psychology, they are used interchangeably. Technically, they are, however, quite different. The concept of working memory is task-oriented: it can be thought as an “interface” between different processes (e.g., perception, attention, memory), all subordinated to a bigger task.

In contrast, short-term memory simply represents the brain process that allows us to store information (e.g., words, sentences, concepts) for a short amount of time. Most famously, it is associated with [chunking](https://www.nngroup.com/articles/chunking/) and Miller’s magical number 7 — which represents the short-term memory’s approximate capacity, based on the observation that George Miller made back in 1958 that we can remember about 7 “chunks” of information for a brief amount of time.

## Working Memory and User Experience

In our field, a common concept that is well related to that of working memory is the concept of **cognitive load**. If a task incurs a high cognitive load, it usually means that it puts a high burden on the working memory. Tasks that tax our working memory are generally perceived as hard; so, to make the experience pleasant and usable, designers must make sure that the user’s working memory won’t be overloaded.

But how can we know the working-memory capacity of our users? Although the working memory has limited capacity, its exact size will vary from person to person. Education and IQ are usually positively correlated with working-memory capacity, while age affects it negatively. If we target a specialized audience (e.g., [experts](https://www.nngroup.com/articles/writing-domain-experts/)) we may be able to have a fairly good idea of the working-memory capacity of its members. But for a general audience, the working-memory size will be quite variable.

While working-memory capacity depends on the individual, it’s likely that many members of your project team enjoy a substantially bigger capacity than found among those in your target audience. For sure, many developers have large working memories, because of self-selection: programming is so complicated that people are more likely to be good at it if they can hold lots of stuff in their working memory while coding. As a result, your colleagues may think that a certain task flow is easy — because it doesn’t overtax their own working memory — but most actual users will have great difficulty because they run out of working memory while attempting the task. As always, [you’re not the user](https://www.nngroup.com/videos/false-consensus-effect/).

A good user experience is good for everyone, not only for those people who have a large working-memory span. So, a general good practice of design is to **limit the burden put on the users’ working memory**. In other words, make sure that users can easily access all the information they need for a task, without having to commit it to working memory.

### External Memory

It’s easy to say: “limit the working-memory burden”, but certain tasks are naturally more complex than others. How can we help users get around their working-memory limitations? In our original addition example, we cannot change the task; addition is what it is. But we can make it easier — by providing pen and paper, so people can write down the numbers and the intermediate products in the task without having to store them in the working memory. The paper acts as a physical scratchpad, a “fake” working memory.

> **External memory** refers to any tool or UI feature that allows users to explicitly save and access information needed during a task.

Same with web tasks. Supplement the working memory with a form of **external memory** — a virtual scratchpad where users can store all the info that they need without having to commit it to their internal memory.

An example of a task with high working-memory needs is [reading a difficult passage on mobile](https://www.nngroup.com/articles/mobile-content/). Our studies show that, to achieve the same level of comprehension on a small screen and on a large screen, users must spend more time on mobile — likely because of the higher working-memory demands. The screen serves as a natural external memory — if people forgot something, they could glance up and revisit the concept from a previous paragraph. But on a smaller screen the information from a previous paragraph is no longer visible (that is, the size of the external-memory scratchpad is smaller), so they have to spend time to recover it.

A typical example of web task involving a high working-memory burden is item comparison: the user has to weigh in the pros and cons of several alternatives and choose the best. Whether comparing hotels, shoes, or insurance plans, comparison involves remembering the available options and deciding which option combination is optimal. Tools such as [comparison tables](https://www.nngroup.com/articles/comparison-tables/) are a form of external memory — they allow users to select a set of items of interest and explicitly compare their pros and cons, lined up with each other, in an easy-to-see table.

Sometimes users create their own external-memory tool. For example, we may use a spreadsheet, a file, or a web note to keep track of interesting summer camps for our children, of places to see in a vacation, or of articles to read. When engaging in online shopping, many users will save candidates for a target item in a shopping cart, and then, at the end, decide which is the best. [Millennials](https://www.nngroup.com/articles/young-adults-ux/) engage in [page parking](https://www.nngroup.com/articles/multi-tab-page-parking/) — they open interesting items in different tabs, saved for a future inspection, without interrupting the task of selection. These are all behaviors that create some form of external memory and help users cope with the burdens associated with a task with high working-memory demands.

### Conclusion

Different tasks have different working-memory requirements. Designers must understand what kinds of information users will need to keep in their working memory as they attempt to reach their goals on a website, and provide UI features that act as external memory to help them offload that burden and perform the task faster.

Learn more about working memory and external memory in our courses on [psychology](https://www.nngroup.com/courses/human-mind/) and [human-computer interaction](https://www.nngroup.com/courses/hci/) for designers.

### Reference

Baddeley, A.D., & Hitch, G. (1974). [Working memory.](http://apps.fischlerschool.nova.edu/toolbox/instructionalproducts/edd8124/fall11/1974-Baddeley-and-Hitch.pdf) In G.H. Bower (Ed.), *The psychology of learning and motivation: Advances in research and theory* (Vol. 8, pp. 47–89). New York: Academic Press.
