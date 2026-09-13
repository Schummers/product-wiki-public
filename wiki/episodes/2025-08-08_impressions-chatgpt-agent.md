---
type: source
name: "Initial Impressions of ChatGPT's Agent: Successful, Shaky, and Slow"
created: 2026-07-30
published: 2025-08-08
source_type: article
status: processed
url: "https://www.nngroup.com/articles/impressions-chatgpt-agent/"
author: "Evan Sunwall"
raw: raw/sources/2025-08-08_impressions-chatgpt-agent.md
concepts:
  - "Agentic AI"
  - "Human-in-the-Loop"
  - "AI User Experience"
  - "Decision Gates"
---

# Initial Impressions of ChatGPT's Agent: Successful, Shaky, and Slow

## Summary

The author documents their experience using OpenAI's newly released ChatGPT Agent mode to book a restaurant reservation, a real-world task typical of how agents might be deployed. While the agent ultimately succeeded in booking the reservation, the journey revealed significant limitations: the process was surprisingly slow (taking longer than human completion), the agent failed to ask clarifying questions upfront despite receiving a weak prompt, it struggled with web form controls, and it required human intervention for personal information. The article highlights the importance of human-in-the-loop design, discusses decision gates where agents request confirmation, and suggests that mainstream agentic AI still has considerable distance to travel before reliable everyday use.

## Key Takeaways

- **Speed is Not Yet Competitive** — Booking the reservation took ChatGPT 11 minutes compared to a human's 2 minutes, and the reservation window technically timed out (though the system processed it anyway), revealing that agents may not yet replace human efficiency for complex tasks.
- **Clarifying Questions are Critical** — Rather than asking about dining style, budget, food preferences, or the dietary restriction the user later mentioned, ChatGPT jumped directly into the task with limited context, missing the opportunity to gather information that would have improved results.
- **Web Form Navigation Remains Challenging** — The agent struggled with dropdown selectors, scrolling to find options, and occasionally mis-clicked, requiring multiple attempts for seemingly simple interactions like selecting a time slot.
- **Human-in-the-Loop is Essential** — The agent correctly identified when personal information needed to be entered and wisely kept the human in the loop, and it used decision gates to request confirmation before submitting the reservation.
- **Slow, Pivots Cost Time** — Dead ends like a restaurant that was over budget or unavailable would have incurred additional delays, and the combination of slowness with required human intervention significantly erodes the value proposition of agentic AI.

## Quotes

> While this tool represents a significant step towards mainstream AI-agent use, my simple evaluation revealed that agentic AI still has a long way to go.

> Remember that the computer should adapt to the needs of the human, and not the other way around.

> The halting process over a simple web form implies that more complex experiences would be more error-prone and slow.

## Concepts

- [[Agentic AI]] — The article evaluates agentic AI capabilities and limitations in a realistic everyday task scenario.
- [[Human-in-the-Loop]] — The article defines and praises the practice of keeping humans actively involved in decision-making rather than letting agents act autonomously.
- [[AI User Experience]] — Web form manipulation, clarifying questions, and decision timing all relate to fundamental usability challenges in agentic AI design.
- [[Decision Gates]] — The article identifies and discusses points where agentic AI requests human confirmation before taking significant actions.
