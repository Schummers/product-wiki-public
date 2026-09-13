---
title: "The 5 Qualities of Site-Specific AI Chatbots"
date: "2026-07-10"
url: "https://www.nngroup.com/articles/dimensions-of-ai-chatbots/"
author: "Georgia Kenderova, Tanner Kohler"
topics: [ai]
type: article
---

Designing a site-specific AI chatbot requires making key decisions even before user testing begins. The five chatbot qualities described in this article — handoff willingness, flexibility, proactivity, emotional responsiveness, and transparency — can guide those early design decisions and provide a framework for evaluating existing chatbots. (But don’t neglect real testing. Real users will help you [finetune the specific behaviors](https://www.nngroup.com/articles/ai-model-training/) that will best serve their needs.)

Getting these qualities wrong can be costly. People are still forming mental models of site-specific AI chatbots and figuring out whether to view them as human customer-support representatives or frontier-level LLMs. Many chatbots fall short of both types of expectations and quickly get abandoned by users.

## In This Article:

- [1. Handoff Willingness: Respect Users' Desire to Speak with Real People](#toc-1-handoff-willingness-respect-users-desire-to-speak-with-real-people-1)
- [2. Flexibility: Go Where the User Wants to Go (Within the Chatbot’s Defined Guardrails)](#toc-2-flexibility-go-where-the-user-wants-to-go-within-the-chatbots-defined-guardrails-2)
- [3. Proactivity: Anticipate Needs and Suggest Next Steps](#toc-3-proactivity-anticipate-needs-and-suggest-next-steps-3)
- [4. Emotional Responsiveness: Recognize and Acknowledge Human Emotions](#toc-4-emotional-responsiveness-recognize-and-acknowledge-human-emotions-4)
- [5. Transparency: Communicate Identity, Capability, and Rationale](#toc-5-transparency-communicate-identity-capability-and-rationale-5)
- [Conclusion](#toc-conclusion-6)

## 1. Handoff Willingness: Respect Users' Desire to Speak with Real People

AI chatbots should allow users to connect with human agents with minimal friction.

There is a strong business argument against escalating conversations to humans: preventing the involvement of human agents reduces the human hours needed to assist customers, thereby saving money.

However, **users do not yet view AI chatbots as equivalent to human agents.** As soon as they feel that the bot isn’t helping or that their circumstances are beyond its abilities (which is still common), they want to speak with a human.

This is not new. [It’s a repeat of the old phone tree dilemma](https://www.nngroup.com/articles/phone-tree-guidelines/): a system designed to save the business money becomes a barrier between users and getting the help they need.

One participant in [our study on site-specific AI chatbots](https://www.nngroup.com/articles/site-ai-chatbot/) explained:

> “I just get turned off by it because a lot of times you go through the AI or the chatbot and you ask the question and [...] **I feel like a hamster wheel kind of spinning around and around, and I'm not really getting anywhere**. Or they say, ‘I'm sorry, but we can't help you with that. Call this number.’ Well, that's what I want in the first place.”

![Wyze Smart Search chat. The user types "I wanna speak with an agent." The bot replies right away with two phone numbers to reach a human — one for the US, one for Canada — without asking any additional questions.](https://media.nngroup.com/media/editor/2026/06/16/desktop-1-6.png)

✅ *Wyze* Smart Search *chatbot was immediately ready to hand off the conversation to a human agent without any further explanation from the user.*

![Wilson Virtual Agent chat. The user tries to reach a human three different ways: "I want to speak with a representative," "How do I contact a human agent?," and "I think my question is a little bit complicated, so I'd like to speak with someone if I can." Each time, the bot deflects — asking the user to describe their issue first and promising to share contact information only afterward. No handoff is ever offered.](https://media.nngroup.com/media/editor/2026/06/16/image11.png)

❌ *Even after three attempts, Wilson’s* Virtual Agent *wouldn’t let the user connect with a human.*

**Never gatekeep when the user explicitly asks to be connected to a human.** If a customer asks for a human agent, the bot should immediately honor that request.

Beyond explicit requests, chatbots should offer to escalate when they can no longer answer effectively or when the user shows signs of frustration or extra effort (e.g., repeatedly rephrasing the same question).

Handoff is a balancing act: escalating too quickly to a human agent can undermine trust in the bot’s capabilities and increase labor costs. But refusing to escalate when the user asks directly or when the bot cannot help is far worse because it undermines the chatbot’s entire purpose and deters users from using it again.

## 2. Flexibility: Go Where the User Wants to Go (Within the Chatbot’s Defined Guardrails)

AI chatbots should adapt as users change their minds, commit errors, or meander among various topics. They should discuss topics on the user’s terms rather than forcing the user to adapt to their conventions.

![Three chatbot responses to the same question — "What should I wear for a day hike in cool weather?" — shown side by side for an outdoor-goods retailer. Bot A (Too narrow) only offers to look up products by name, refuses the styling question, then pushes a survey. Bot B (Appropriately scoped) explains a layering setup, offers to show matching products, and pulls up fleece mid-layers under $100 with images, prices, and Add-to-cart buttons. Bot C (Too broad) recommends competitor brands — Patagonia, Arc'teryx, REI — and quotes price ranges the retailer never authorized.](https://media.nngroup.com/media/editor/2026/06/26/user-asks-all-three-outdoor-good-bots-desktop.png)

*Three chatbot responses to the same question from a user at an outdoor-goods retailer: An overly rigid response (left) can make the bot seem oblivious to the user’s needs. An overly flexible one (right) can come across as a loose cannon — unpredictable and risky for the brand.*

Users universally appreciated flexibility. Those expecting a rigid chatbot were pleasantly surprised when it proved more flexible. And those very accustomed to products like ChatGPT sometimes felt site-specific bots seemed clumsy when they couldn’t follow the user’s lead. In either case, people appreciate flexibility.

There is, however, a strong cautionary argument for limiting the flexibility of a site-specific AI chatbot: do you really want your bot to stray from the topics it has been carefully trained on, risking its credibility and your brand perception? Do you want to pay increased computation costs if users figure out it’s a free version of more sophisticated LLMs they must pay for elsewhere?

![A horizontal spectrum labeled "Degree of flexibility," running from "Less flexible" on the left to "More flexible" on the right. Three boxes sit along it. Left: "Too narrow" — too rigid, misses adjacencies. Center, highlighted as the goal: "Appropriately scoped" — handles adjacencies, redirects out-of-scope requests. Right: "Too broad" — too permissive, answers off-domain.](https://media.nngroup.com/media/editor/2026/06/26/user-asks-all-three-outdoor-good-bots.png)

*Flexibility sits on a spectrum. A bot that's too narrow is rigid and misses questions adjacent to the user's goal; a bot that's too broad answers off-domain and drifts beyond what the company authorized. The target is the middle — appropriately scoped: flexible enough to handle adjacent questions, disciplined enough to redirect what's genuinely out of scope.*

### Handle Adjacent Questions, Not Just FAQs

Sometimes users ask chatbots questions related to the company’s product or service, but that don’t fit neatly into standard workflows or FAQs. For example, a user may ask a meal-kit-service bot about a possible substitution for a dietary restriction.

Such queries are adjacent to the bot’s domain: they are not standard product questions, but they are connected to the user’s goal (e.g., purchasing appropriate family meals). Bots that can handle these types of questions feel far more useful than ones that function as expanded FAQs.

To identify what counts as adjacent for your company, consider the [problems users are trying to solve](https://www.nngroup.com/articles/personas-jobs-be-done/) with your product or service. Then review past customer-support logs to see the kinds of questions customers have actually asked.

This doesn’t mean a bot should be able to answer everything. Some topics are just out of scope and unrelated to the company’s services. For example, a meal-kit-service bot offering advice on dietary restriction substitutions adds value; however, one that generates workout routines falls outside of its domain.

When a user asks something outside the bot’s scope, the bot shouldn’t simply stall; instead, it should acknowledge the request, its limitations, and redirect the user by explaining what it *can* help with.

![Two Home Depot Magic Apron chats side by side. Left: the user asks for general plant-care tips, and the bot gives watering and care advice for low-maintenance plants. Right: the user asks the price of apples, and the bot declines — explaining it can only help with products sold at Home Depot — and offers to help with home-improvement items instead.](https://media.nngroup.com/media/editor/2026/06/16/desktop-1_yXOyT2a.png)

✅ *Home Depot’s bot was appropriately scoped to answer questions that are adjacent to the company’s domain (left), but not ones that go outside of it (right).*

![Arc'teryx Virtual Assistant chat. The user says they're hiking in Norway and need good hiking pants; the bot replies that it only handles Arc'teryx product questions. After the user re-asks for hiking pants "from arc'teryx," the bot says it couldn't find the information, asks whether they want waterproof, insulated, or lightweight, then asks the user to take a two-question survey — without ever surfacing a product.](https://media.nngroup.com/media/editor/2026/06/16/desktop-1-1_Q133T7R.png)

*Arc’teryx is an outdoor-clothing and equipment store, but its chatbot did not recognize “hiking pants” as within its scope and, even after clarification, could not provide useful information (left). Worse, it immediately asked the user to fill out a survey (right).*

![Scouting America's Scoutly chat. Asked to help find current prices, the bot requests the user's city and state, then — for Seattle, WA — lists local grocery stores (Safeway, QFC, Fred Meyer, Whole Foods, Trader Joe's, PCC) and estimated prices for s'mores ingredients: graham crackers, marshmallows, and chocolate bars, with a tip to check store apps for deals.](https://media.nngroup.com/media/editor/2026/06/16/desktop-1-2_CGvCtTy.png)

*Scouting America’s* Scoutly *was able and willing to talk about topics that were outside of its immediate scope, ultimately providing the user with shopping advice and price estimates related to s’mores.*

### Handle Errors Actively

Flexibility extends to how the bot handles situations where communication breaks down. When encountering errors or when unable to process a user query, bots should try to clarify what the user means.

To handle errors, the bot could follow a progression of increasingly active strategies:

1. **Signal uncertainty rather than providing irrelevant responses.** The bot should be transparent when it isn’t confident about what the user is asking. Saying, *I’m not sure I understand correctly* is better than guessing wrong and providing an irrelevant answer.
2. **Diagnose what went wrong and communicate it clearly.** Not all misunderstandings are the same — a long, multipart query that overwhelmed the bot should be handled differently from a question that contains unfamiliar terminology. The bot should explain what *specifically* went wrong, and what it did and did not understand.
3. **Collaboratively work with the user to recover from misunderstandings.** The bot should invite the user to correct what it did not understand (for example, by asking *Did you mean X, Y, or Z?)*. Multiple-choice clarification questions alleviate the user from the burden of having to rephrase their question entirely.
4. **Defer to a human when repair attempts fail.** If the bot still cannot resolve the issue after multiple attempts, it should connect the user to a human agent.

![Scouting America's Scoutly chat. The user reports "the map is not displaying." The bot apologizes, lists possible causes (technical issue, connection problem, browser compatibility), suggests fixes like refreshing and checking the connection, and offers to search by zip code to find local troops instead.](https://media.nngroup.com/media/editor/2026/06/16/desktop-1-3.png)

✅ *Scouting America’s bot* Scoutly *, provided the user with troubleshooting steps and an alternative path to getting the information they requested.*​​​​​

![Scouting America's Scoutly chat, continued. The user says they still can't see the map. The bot apologizes again, repeats the troubleshooting steps, and offers alternative routes to the information — contacting the local Scouting America council, visiting the official website, or calling 1-800-SCOUTS — plus an offer to find contact details for the local Seattle council.](https://media.nngroup.com/media/editor/2026/06/16/desktop-1-4.png)

✅ *Once* Scoutly *recognized it couldn’t help, it suggested other ways to find the nearest scout troops, including an offer to find region-specific contact information.*

## 3. Proactivity: Anticipate Needs and Suggest Next Steps

AI chatbots should offer help and suggestions even when users don’t explicitly ask for them

Our research participants valued suggested follow-up questions or actions. The design challenge is deciding when and how the bot should take initiative.

We divide proactivity into two subcategories:

1. Clarification proactivity
2. Directional proactivity

### 1. Clarification Proactivity

Unlike error handling, clarification proactivity happens when nothing has gone wrong. The bot asks for more information so it can give a tailored response. This matters most when the user’s query is ambiguous or underspecified, because guessing may lead the bot in the wrong direction, solve the wrong problem, or provide a generic answer.

![Williams Sonoma's Olive chat. The user says "I want an espresso machine," and Olive asks three clarifying questions before recommending anything: manual, semi-automatic, or fully automatic; any specific features like a built-in grinder or milk frother; and budget range.](https://media.nngroup.com/media/editor/2026/06/16/image14.png)

✅ *Williams Sonoma’s bot* Olive *, asking followup clarification questions to an ambiguous prompt about an esspresso machine, in order to provide as relevant a response as possible.*

When bots ask clarifying questions, they imply that they will use the answers to tailor the response. If they can’t, the questions waste the user’s time. Bots should ask only questions that they can act on.

![Redfin Virtual Assistant chat. The user wants a condo in San Francisco's Castro District. The bot says it can't find "the Castro District" and asks for a street, landmark, or nearby neighborhood. The user clarifies the neighborhood is literally called "The Castro"; the bot acknowledges it and offers to show condos — but when the user gives their criteria (1 bedroom, no price range), the bot again says its search system doesn't recognize "The Castro" as a region.](https://media.nngroup.com/media/editor/2026/06/16/desktop-1-5.png)

*Redfin’s* Virtual Assistant *asked for details such as which city or neighborhood the user was interested in, but could not use them.*

### 2. Directional Proactivity

Bots should help users discover useful, relevant information they might not have thought of on their own.

#### Make Directional Guidance Easy to Notice

Suggested next steps should be easily scannable and self-contained (ideally presented as clickable buttons), rather than buried in lengthy explanations that require careful reading.

#### Keep Directional Guidance Focused

When a user is working toward a goal, the bot should not distract them with unrelated suggestions. Suggest possible follow-up questions or related topics only after a resolution has been achieved or the primary goal has been addressed.

In the example below, the user was trying to check whether a product was available at their local Williams Sonoma store. Instead of focusing on that task, the chatbot promoted other products. Its suggestion not only distracted from the user’s task but could also be perceived as upselling and ultimately erode trust.

![Williams Sonoma website with the Olive chatbot open over a shopping-cart page showing a Peter Rabbit Easter egg. The user asks whether the item is available for in-store pickup. Instead of focusing on that, Olive suggests related Easter decor and table-styling tips before asking which store to check, then — after the user gives a zip code — says it can't directly check store availability.](https://media.nngroup.com/media/editor/2026/06/16/image24.png)

❌ *The user was still trying to get information about a specific product when the bot suggested a followup actions related to other products.*

#### Provide Direct Links to Related Information

Chatbots should close the gap between information and action. Rather than simply naming a product or resource or telling people where to find it, they should link to it directly, including visuals and quick links (e.g., *Add to cart*, *Save to favorites,**Compare, Return policy*).

![Arc'teryx Virtual Assistant chat. The user asks for help finding a warm jacket for a hiking trip to Iceland. The bot recommends the Alpha Parka and Beta Insulated Jacket and describes their insulation and weather protection in a dense paragraph — but with no product images or links — then closes by asking the user to take a two-question survey.](https://media.nngroup.com/media/editor/2026/06/16/image4.png)

❌ *Arc’teryx’s chatbot provided product recommendations, but did not show pictures or links, so the user had to manually search to find the specific product it mentioned.*

![Lowe's Mylow chatbot on mobile. After asking about the user's needs, the bot displays a swipeable product card for a RELIABILT 1-in x 4-in x 12-ft unfinished board: $18.27, rated 4.5 stars from 79 reviews, with a product photo and two buttons — "Add to Cart" and "View Details."](https://media.nngroup.com/media/editor/2026/06/16/image27.png)

✅ *Lowe’s chatbot, Mylow, provided images and links to products, as well as an* Add to Cart *button, allowing users to easily browse and add items.*

## 4. Emotional Responsiveness: Recognize and Acknowledge Human Emotions

AI chatbots should recognize and acknowledge customers’ feelings in their language and tone.

To decide how to respond to users’ emotion, consider what your baseline is and what triggers might change this default behavior:

1. **Baseline:** What is the emotional weight your domain or industry typically carries? More sensitive domains (e.g., healthcare or crisis lines) should show more emotional acknowledgment by default; transactional domains (e.g., tax filing or government services) generally don’t need to.
2. **Triggers:** Are there predictable moments (either positive or negative) that call for emotional acknowledgment? For example, a user reports a problem the company caused (negative) or shares something emotionally significant (positive or negative). These moments should be reflected in your [customer-journey maps](https://www.nngroup.com/articles/journey-mapping-101/).

#### Acknowledge the Situation, but Don’t Pretend to Have Feelings

When acknowledging users’ emotions, a chatbot should not express feelings it cannot have; for example, saying *I’m sincerely sorry**about the delay* can come across as performative. The better approach is to **acknowledge the situation** — for example, *Two weeks is a long time to wait. Let me see what I can do to fix this*. It’s honest and moves the user toward a resolution.

Additionally, while it’s appropriate to describe the situation itself (for example, *That’s a stressful situation*), chatbots should not make claims about the user’s inner state (for example *, I understand your disappointment*).

![Lacoste "LET'S CHAT" window. The user writes "i have issues with my tennis shoes." The bot replies, "I am sincerely sorry to hear about the issue with your item. I understand your disappointment, and I am here to help," then asks for a description and photo of the defect — assigning the user an emotion (disappointment) they never stated.](https://media.nngroup.com/media/editor/2026/06/16/image3.png)

❌ *Lacoste’s chatbot was not only sincerely sorry but also assumed that the user was disappointed with the shoes — an emotion the user never expressed. This type of language can come across as both presumptuous and performative.*

![On chat. The user writes "I have issues with my running shoes." The bot responds, "We're here to help you get back on the road," then asks whether they want to start a warranty claim for a defect or return/exchange a recent purchase — acknowledging the situation without claiming to feel anything.](https://media.nngroup.com/media/editor/2026/06/16/image6.png)

✅ *On’s chatbot acknowledged the situation and the need to* get back on the road *, but did not express any feelings. Instead, it immediately moved to clarifying the desired next steps.*

#### Emotional Responsiveness Is No Substitute for Resolution

Even when appropriate, emotional responsiveness should not replace solving the problem quickly.**** No matter how much a bot acknowledges the customer’s emotion or “empathizes” with them, users will still become frustrated if it does not make progress. If the bot cannot resolve a query, the most empathetic response is to connect the customer with a human agent who can help (see *Handoff Willingness*).

![Ask Turo chat. The user explains their host cancelled last minute and they've waited 40 minutes for a car that isn't at the agreed location. The bot calls it a stressful situation and says it's sorry they're dealing with it, then explains the team can step in to arrange a replacement vehicle or a full refund, and asks whether the user wants that help.](https://media.nngroup.com/media/editor/2026/06/16/image26.png)

✅ *Turo’s chatbot recognized the stress-inducing situation and acknowledged its urgency, then quickly pivoted to providing a concrete solution (in this case, escalating to a human agent).*

## 5. Transparency: Communicate Identity, Capability, and Rationale

AI chatbots should make clear:

1. That they are an AI system (identity transparency)
2. Their capabilities and limitations (capability transparenc *y*)
3. The rationale behind their outputs (rationale transparency)
4. How they handle user data (privacy transparency)

#### Identity Transparency

It can be tempting to downplay that the chatbot is AI, but our research suggests that users prefer [upfront disclosure](https://www.nngroup.com/articles/trustworthy-design/). Identifying the bot as AI supports trust, which has long been a credibility best practice on the web, and is legally required in some regions, including the EU starting in August 2026. At a minimum, use a persistent indicator — such as an AI icon or an *AI agent* label — to make the bot’s identity clear.

#### Capability Transparency

Users still lack a clear [mental model](https://www.nngroup.com/articles/mental-models/) of what site-specific AI bots can and cannot do, so designers should shape those expectations by clearly defining the bot’s capabilities and limits.

##### Surface Capabilities when Most Relevant

You can outline the bot’s scope in its opening message, but don’t show an exhaustive list of everything it can do. Users may find that[overwhelming and forget it as the conversation moves forward.](https://www.nngroup.com/articles/onboarding-tutorials/) Instead, [surface capabilities contextually](https://www.nngroup.com/articles/help-and-documentation/), when they are most relevant. For example, if a Home Depot user has been looking at faucets and lands on a sink product page, the bot might ask *Want me to check whether the faucet you viewed fits this sink?* This reveals a capability exactly when it's most useful.

##### Be Honest About the Bot’s Limits

Compare *I can’t help with that*, which is vague, with *I don’t have access to your purchase history, but I can connect you to someone who does*. The second response explains the limitation and the next step. In one sentence, it shows handoff willingness, appropriately scoped flexibility, proactivity, and transparency.

![Williams Sonoma's Olive chat. The user asks whether a machine is available at their local store. Olive describes the De'Longhi Classic Espresso Machine and asks for a ZIP code as if it can check availability; after the user provides their ZIP code, the bot admits it can't actually check and tells the user to use the "Check Store Availability" feature on the product page themselves.](https://media.nngroup.com/media/editor/2026/06/16/image18.png)

❌ *Williams Sonoma’s bot could not provide product availability, yet it led the user on, asking them followup questions that made it seem like it can. Not only was it  misleading and dishonest about its capabilities, but it also wasted the user’s time.*

#### Rationale Transparency

Simple answers don’t usually need explanation. For example, if a user asks for a nearby store location, the chatbot doesn’t need to explain why it chose that location. Rationale transparency matters most when the bot makes a judgment call, such as recommending one product over another, or declining a request the user expected it to handle. Compare *I can’t process a return* to *This item is a final sale, so I can’t process a return. I can help you with an exchange instead.* The first leaves the user wondering why they can’t make a return; the latter explains the reason and offers an alternative.

![Home Depot's Magic Apron chat. The user says they're looking for an AC for a roughly 400-square-foot living room. The bot recommends a specific unit and explains why it fits: strong cooling capacity for the room size, good customer ratings, and features like a dehumidifier and remote control.](https://media.nngroup.com/media/editor/2026/06/16/image5.png)

✅ *Home Depot’s bot* Magic Apron *provided a concrete AC recommendation and describes the specific qualities that make it a good fit for this user.*

#### Privacy Transparency

Users don’t read privacy policies. If a chatbot explains its data practices only in a linked privacy policy, most users will miss it. Meaningful privacy transparency happens in the conversation itself, when the bot asks for potentially personal or sensitive information. For example, requesting the user’s phone number or address without explaining why it’s needed can feel intrusive, especially when the reason doesn’t clearly connect to the user’s task. Instead, explain the purpose in the request itself: *I need your email address to send a shipping confirmation.* Otherwise, users will be left wondering why their personal information is needed and how it’ll be used.

## Conclusion

Site-specific AI chatbots are still earning users’ trust, and every interaction with them either builds it or erodes it. Thoughtfully designed handoff willingness, flexibility, proactivity, emotional responsiveness, and transparency will help build the trust users require before they form hard-to-change opinions about your chatbot. Use these qualities to structure the conversation: Where does our bot currently stand on each dimension? Where should it be? What would it take to close the gap?
