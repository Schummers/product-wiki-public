---
title: "Scope in Generative AI Features"
date: "2025-02-28"
url: "https://www.nngroup.com/articles/scope-ai-features/"
author: "Kate Moran"
topics: [ai, interaction-design]
type: article
---

When designing an AI feature, its scope (how broad or narrow its capabilities are) influences its usability. Our research shows that narrower AI features are (typically) easier for new users to understand and adopt. This article compares broad AI systems like ChatGPT with narrow AI tools like Spotify’s playlist generator, exploring how scope impacts design.

## In This Article:

- [Defining AI Scope](#toc-defining-ai-scope-1)
- [Broad vs. Narrow: A Comparison Table](#toc-broad-vs-narrow-a-comparison-table-2)
- [Narrow Scope Allows for Guided AI and Better UX](#toc-narrow-scope-allows-for-guided-ai-and-better-ux-3)
- [Narrow Scope Is Less Likely to Be “AI for AI’s Sake”](#toc-narrow-scope-is-less-likely-to-be-ai-for-ais-sake-4)

## Defining AI Scope

Before beginning to design a UI for any user-facing AI-powered feature, teams should answer these 4 strategic questions:

- [What specific user problem](https://www.nngroup.com/articles/ai-user-value/) are we trying to solve?
- How would fixing this problem **contribute to****business goals?**
- [Is AI truly the best solution](https://www.nngroup.com/articles/how-ai-works/) for this problem?
- **How complete, clean, and structured is the data** we’ll feed into the AI?

If, after these considerations, an AI solution still seems the best course of action, the next aspect to consider is the feature’s scope. Scope is a useful way to categorize **interactive, user-facing AI features or products**— in other words, how broad or narrow the AI system’s capabilities are.

> **The scope** of an AI feature describes the breadth of its data inputs and functionality. The broader the scope, the more variety of inputs the system can accept and the wider the range of possible outputs the system can produce.

*Think of scope as a spectrum, stretching from very broad to very narrow. Any given AI product can sit anywhere on this spectrum.*

Scope can be defined for any type of system, AI or not, user-facing or running in the back end. However, this article focuses on interactive, user-facing AI features.

For an AI feature, its scope is determined by the:

- Kinds and size of **input** it accepts
- Types of **outputs** it produces
- **Tasks** it can handle
- **Subject** areas it covers

The scope of any given AI feature or product has significant implications for its design and usability.

### Broad-Scope AI Systems

Some systems, like ChatGPT or Claude, are very broad in scope. They can handle a **wide variety of tasks** and respond to open-ended user inputs **.** Some can **accept many types of input data,** including images, videos, or other file types. Some have access to the live internet, while others operate with static datasets. These broad-scope systems can also **produce a variety of outputs.**

AI-powered smart assistants and agentic AI tools have even broader scopes, by accessing data and interacting with multiple apps and websites. (Although, at the time of writing, agentic AI’s unreliable performance holds it back from widespread use.)

These systems do have some constraints — for example, they all impose limitations on the size of the input (tokens) they accept. Most also have “safety” constraints around what they can provide information on. (For example, ChatGPT isn’t supposed to tell you how to build a bomb.)

#### Examples: ChatGPT and Perplexity

ChatGPT and Perplexity are both very broad-scope AI systems. However, Perplexity is slightly narrower in scope, because (unlike ChatGPT) it is specifically designed for information seeking (it brands itself as an “answer engine”).

![The Scope Spectrum of AI Features is represented by a horizontal axis, stretching from Broad (left) to Narrow (right). ChatGPT is very broad, placed on the spectrum farthest to the left. Perplexity, which is a bit more narrow, is placed to its right.](https://media.nngroup.com/media/editor/2025/02/18/scope-spectrum-2.jpg)

Even this slight narrowing in scope has massive design implications. A more specific use case (even if it’s still very broad) allows for a more tailored interface design. Perplexity’s VP of design, Henry Modisett, said as much in our [podcast conversation](https://www.nngroup.com/articles/perplexity-henry-modisett/) last year:

> “Open AI is building a platform that’s going to have to work for all kinds of use cases that we’re not thinking about.”
> 
> 
> 
> *Henry Modisett, VP of Design at Perplexity AI*

Comparing the interfaces of ChatGPT and Perplexity, these differences are clearly visible.

- **ChatGPT** operates within a simple chat interface with a few icons (parameters). This generic interface reflects the huge variety of possible use cases.
- **Perplexity’s** interface has more UI elements and is more aligned with traditional search design. It offers the ability to ask followup questions but is not as conversational. Additionally, sources are a major focus in the design in a way they are not in ChatGPT (reflecting Perplexity’s narrower focus on information seeking.)

![When new users encounter ChatGPT, it offers dozens of suggested prompts to help people understand what it can be used for. These are extremely diverse, including "Create a charter to start a film club" and "Make a sandwich using ingredients from my kitchen."](https://media.nngroup.com/media/editor/2025/02/18/chatgpt-prompt-suggestions.png)

*ChatGPT can handle a huge range of tasks, which means new users will need to spend time exploring the tool to get a sense of where it’s valuable for them. This challenge is reflected in the number of prompt suggestions that OpenAI provides to new users.*

![Perplexity's mobile app, showing its response to the question, "How is hail formed during thunderstorms?" The UI is specifically designed to focus on question-answer interactions, unlike ChatGPT.](https://media.nngroup.com/media/editor/2025/02/18/perplexity-sources.jpeg)

*Perplexity’s UI is clearly focused on information seeking. Its primary elements are the question, sources, and answer; the chat box, while present, encourages asking followup questions rather than carrying long back-and-forth, ChatGPT-like conversations.*

### Narrow-Scope AI Features

On the opposite side of the spectrum, narrow-scope AI features serve a very specific purpose and generally support a single task or goal. They are not as versatile or powerful as broad-scope AI features, but their purpose is more immediately clear to users.

Let’s look at two narrow-scope features as examples: Spotify’s playlist creator and Photoshop’s generative fill.

![On the scope spectrum, Photoshop and Spotify's AI features are located far to the right, on the narrow side.](https://media.nngroup.com/media/editor/2025/02/18/scope-spectrum-3.jpg)

#### Example: Spotify

Spotify’s AI-powered playlist creator is an example of a moderately narrow AI tool. While it does have a chatbot interface for collecting input, it’s constrained to a single purpose — creating a playlist based on the user’s requests.

*Spotify’s AI playlist feature: Paid subscribers can generate a playlist based on a short music-related prompt. The playlist can then be modified, either by additional prompting or by directly editing the suggested songs. (Don’t judge my Millennial music taste, please and thank you.) While this more targeted scope makes the feature more approachable for new users, it isn' t perfect. For example, like many genAI tools, the playlist feature often ignores or misunderstands instructions. However, in this context, mistakes are minor inconveniences. The feature's value still outweighs those inconveniences, because it's easier to adjust an existing playlist than to create a new one from scratch.*

Within that scope, users still have plenty of freedom. They can request a specific artist, era, genre, or vibe. But, unlike ChatGPT and Perplexity, they can’t ask Spotify’s playlist generator to, say, write a sonnet about tacos.

![In a screenshot from Spotify's AI feature, a user tells the chat to "write me a sonnet about tacos." The system gracefully declines the request by saying, "I'm here to create playlists."](https://media.nngroup.com/media/editor/2025/02/18/spotify-tacos.jpg)

*Spotify’s narrow AI feature has constraints to prevent users from using the feature for unrelated tasks, like writing sonnets. This narrow focus allows the design team to tailor the experience for this specific task. It also helps the business avoid potential abuse or misuse of the system.*

Again, this narrower scope allows for a more tailored experience. For example, **the prompt suggestions are all specific** to this use case and therefore are more likely to be relevant to users. **Prompt writing is easier,** because the tool already "understands" its purpose and how to achieve it with minimal textual input from the users. People in our study wrote very short, search-style prompts. In some cases, participants only used one or two words.

**Because the feature's output**(the playlist) **is predictible** (a small set of songs),**it can be structured** in the interface. Before creating the playlist, users can sample, remove, or save suggested songs.

#### Example: Photoshop Generative Fill

With some narrow AI tools, like Photoshop’s generative-fill feature, text prompting may not be needed at all.

*Photoshop’s generative fill feature: Users can quickly remove or swap out elements from photos. The only needed context is a selection in the photo — any prompting is optional.*

## Broad vs. Narrow: A Comparison Table

Broad AI Systems | Narrow AI Features | Product Context | More likely to be stand-alone products or chat boxes | Task-specific features within apps or websites | Inputs and Prompts | May accept a wide variety of data and file typesLikely to use an open text field | More restrictions on the instructions or size and types of input | May not accept text or prompt input at all | Functionality | More flexible | More constrained | Interface | Can be very simple -- essentially a chat box | Richer in UI controls; may not be chat-based

## Narrow Scope Allows for Guided AI and Better UX

In our recent qualitative usability study, **narrow-scope AI features tended to perform better** than open-ended, broad-scope features. With narrower scopes, participants found it easier to:

- Understand the feature’s purpose
- Generate prompts (when needed)
- Iterate and customize outputs

In general (though not in every instance), participants also provided more-positive feedback about narrowly scoped features.

### Example: Planning a Trip with AI

TripAdvisor’s travel-itinerary planner is on the narrow side of the AI-scope spectrum. As a result, the feature’s UI is a prompt wizard that walks users through selecting a destination, interests, and travel dates. This guidance prevents users from having to formulate a free-text prompt and reduces [cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/) as well as the risk of errors (for example, incorrect dates).

*TripAdvisor’s AI trip planner walked users through constructing a prompt, asking for each important piece of information step-by-step. Users chose a travel location, type of trip, travel interests, and dates. They were then presented with an editable set of options for their itineraries.*

Several of our study participants reported using ChatGPT and other broad AI chats in their work and personal life. However, after they used TripAdvisor’s prompt wizard, two participants admitted that they had never thought to ask tools like ChatGPT for travel-planning help.

*After TripAdvisor’s narrow AI feature helped one participant understand that genAI could be used for travel planning, he tried out ChatGPT’s abilities. His previous experience with TripAdvisor influenced the details (date, partner) he included in his freeform prompt. “Wow,” he said. “I have never ever thought it could do this. Holy smokes.”*

A broad AI system’s **vast capabilities don’t matter if users don’t know they exist** or don’t know how to use them for that purpose.

In another session, a different participant, who hadn’t seen TripAdvisor’s narrow feature, started planning her trip with ChatGPT. Without that priming, she had to spend time deciding what details to provide in her prompt. “Let’s see,” she said thoughtfully before beginning her prompt. “With AI, it’s like talking to a kid. You have to list everything, so I have to think…”

In her initial prompt, she included the destination (Bali) and asked for advice on what time of year to visit. ChatGPT was easily able to help answer that question, which was not a functionality available in TripAdvisor’s AI feature (a benefit of ChatGPT’s broader scope).

While the participant appreciated that guidance, ChatGPT’s output was difficult to assess and customize. It responded with two hotel options, 4-stars or 5-stars. At least one of these options, St. Regis, was out of her budget — a detail she didn’t think to include in the prompt. The participant ignored the included source links, and instead searched for these on Google.

*Another participant used ChatGPT to plan a trip to Bali, without seeing TripAdvisor's narrow AI feature first. She had to pause and think of what information the system might need from her prompt to complete the task. When ChatGPT returned a few hotel options, she searched for them into a new tab..*

Compare that simple text output (necessary for such a broad system) to the structured response from TripAdvisor’s feature: because it’s designed for this exact purpose, the results were much easier for participants to explore. Each hotel option was presented next to a map of the travel location, showing its proximity to local sites of interest. When clicked, an overlay with more details about the hotel appeared in-context.

*In TripAdvisor’s AI trip planning tool, hotel suggestions were much easier to assess than ChatGPT’s results. Without leaving this screen, participants could explore hotel suggestions, see their locations relative to attractions, see each property’s amenities, and read reviews.*

While ChatGPT offered much more functionality than TripAdvisor, it required more effort from users — in both prompting (input) and working with the results (output).

### The Flexibility-Usability Tradeoff Applies

This shouldn’t surprise experienced UX professionals — it’s an example of the **flexibility-usability tradeoff**, which states that the more flexible a system is, the lower its usability will be. In other words, more features = more complexity = lower usability.

A broader scope of AI features is more challenging for users because it requires them to:

- Know, imagine, or learn the system’s wide range of capabilities
- Determine which of those capabilities fits their needs
- Cross the [articulation barrier](https://jakobnielsenphd.substack.com/p/prompt-driven-ai-ux-hurts-usability) — think about what they need and verbally express it (which can be challenging even for people with strong communication skills)

Note that **this doesn’t mean we should only design simple, low-functionality systems** (AI or otherwise). We just need to acknowledge that additional functionality may make those systems more challenging to use and ensure that the tradeoff is justified by our user and business needs. Additionally, **narrow-scope AI features are not immune to usability problems** — we observed plenty in our study. (We’ll be elaborating on that in future articles soon.)

Interestingly, in traditional designs, increasing functionality usually means increasing the amount of *stuff* that appears in an interface. In AI systems, the opposite is true — **a narrow scope offers the possibility of exposing more of the system’s functionality** through UI elements, thus making it more approachable to users.

## Narrow Scope Is Less Likely to Be “AI for AI’s Sake”

In addition, I think there’s a confounding variable at play here — the understanding of user needs. A narrow-scope AI feature that’s been crafted for a specific purpose is less likely to be a carelessly slapped-on AI feature. To have a narrow use case, someone is more likely to have spent time thinking about the users’ workflows and how AI could benefit them. In contrast, especially in peak AI hype, we’ve seen many broad AI chats crammed into interfaces without much thought about their actual purpose.

This point brings us back where we started and where all AI integration conversations need to start: at the user and business needs. Depending on your product, users, and business, the AI feature you decide to build could sit anywhere on the scope spectrum and be successful. The key to pulling that off will be making sure it’s appropriately scoped for your specific context.
