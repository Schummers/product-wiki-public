---
type: concept
name: Doherty Threshold
created: 2026-09-10
updated: 2026-09-10
status: stub
---

# Doherty Threshold

## Definition

The Doherty threshold sets 400 ms as the response time below which a system and
its user interact without either waiting on the other, and productivity soars
([[2024-01-23_laws-of-ux_12-10-doherty-threshold]]). Above it, responsiveness
starts costing attention: delays beyond one second are enough for users to
think about other things and lose focus on the task at hand.

The record grounds the number in flow. Speed is what makes flow possible, the
mental state of complete immersion in which users are absorbed by their task,
free from inner criticism, and up to five times more productive
([[Cognitive Psychology]]). A system that keeps answering inside the threshold
removes the friction that would otherwise break that state, which is why the
threshold is treated as a design constraint and not merely an engineering
metric.

## Practice

### When you cannot be fast, be perceived as fast

[[2024-01-23_laws-of-ux_12-10-doherty-threshold]] treats perceived performance
as the practical lever whenever processing genuinely takes longer than 400 ms.
Skeleton screens, progress bars, blur-up image loading and optimistic UI
patterns all make a system appear faster than it is and reduce the perception
of waiting.

### Keep feedback running during the wait

Animation and visual feedback during loading keep users focused and reassure
them that their action is being processed ([[Feedback Design]]). The record
notes research showing that progress bars make wait times feel more tolerable
regardless of how accurate the progress they display actually is.

### Treat page weight as the performance problem

The load-time side of the threshold is getting harder, not easier: the average
desktop page weighed 2,286 KB in 2023 against 634 KB in 2010–2011, which makes
[[Web Performance]] increasingly critical to meeting the threshold at all.

### Sometimes add the delay back

The record's counterpoint to its own rule: purposefully adding a delay to a
process can increase its perceived value and instil a sense of trust, even when
the process itself takes much less time. It gives sensitive operations such as
privacy scans as the case, where users need confidence that the action was
thorough. [[User Friction]] therefore runs both ways here, negative when delays
and waits eat productivity, strategic when an intentional delay buys trust.

## Sources (1)

- [[2024-01-23_laws-of-ux_12-10-doherty-threshold]] — establishes 400 ms as the critical response-time threshold that maintains productivity and prevents user frustration.
