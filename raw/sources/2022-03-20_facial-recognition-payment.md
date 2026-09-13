---
title: "Revisiting Facial-Recognition Payment: Old Problems Still Lingering"
date: "2022-03-20"
url: "https://www.nngroup.com/articles/facial-recognition-payment/"
author: "Leeloo Tang"
topics: [design-patterns, international-users]
type: article
---

China is a world leader in adopting innovative payment methods. Most Chinese today use their mobile phones to make payments and many people don’t carry a physical wallet. Mobile-payment apps like Alibaba’s Alipay and Tencent’s WeChat Pay have vastly outpaced cash and credit cards as the dominant forms of payment. Now facial-recognition payment (FRP, 刷脸支付) is gaining traction in China as well.

To use FRP, users must first register their face and upload bank-card information to a mobile app. Then, they can complete payments by simply glancing at cameras positioned at the checkout in stores.

FRP has become a popular payment method, used mostly in convenience stores, vending machines, and supermarkets. According to [iiMedia Research' s estimates](https://www.iimedia.cn/c400/66866.html), more than 495 million Chinese used facial-recognition payment in 2021 — that’s roughly one third of China’s population. Interestingly, Chinese people refer to facial recognition as "swipe the face," just like swiping a physical card.

We conducted [a study on facial recognition payment in Beijing in 2019](https://www.nngroup.com/articles/face-recognition-pay/), when the technology was relatively new. In that study, we found that, while the technology could offer convenience for paying, it provided poor onboarding experiences to new users. Since our last study, the COVID-19 pandemic swept the globe and masks became required in public buildings in China. We wanted to know whether this payment method had improved since our last study (now that the technology is more established) and whether the pandemic had altered people’s attitudes towards it.

Overall, our findings on FRP can be summarized as follows:

- Users prefer the speed and convenience of FRP but are concerned about its security.
- Users are more likely to accept a system if they understand how it works.
- Inconsistent interactions can make users feel insecure.
- Fast interactions can sometimes seem suspicious.
- Habituation to similar systems can affect how users perceive usability issues.

## In This Article:

- [Methodology](#toc-methodology-1)
- [How FRP Works](#toc-how-frp-works-2)
- [Users Are Still Suspicious About FRP](#toc-users-are-still-suspicious-about-frp-3)
- [What’s Different from 2019？](#toc-whats-different-from-2019-4)
- [Takeaways](#toc-takeaways-5)

## Methodology

Our study was conducted in Beijing and involved 6 participants between the ages of 22 and 48. Three participants had used facial-recognition payments before and FRP made up about 10–15% of their overall mobile transactions. The other three were new to FRP.

We first interviewed each participant for 5–10 minutes to find out about their payment habits and FRP experiences. We also asked them to draw and describe their [mental models](https://www.nngroup.com/articles/mental-models/) of the FRP technology and how they thought it works.

After the interviews, participants were invited to use FRP at two stores: Burger King (a fast-food restaurant with FRP-enabled self-ordering machines) and Tous Les Jours (a bakery with FRP machines available at the checkout counter). The FRP machines used in these two stores were powered by Alipay. Participants were encouraged to think aloud throughout the shopping process and especially during the payment part. Another 15-minute interview was conducted at the end of the observation period. Participants described their experiences, discussed the pros and cons of FRP, talked about how they thought masks affected FRP, and modified their mental-model maps as needed.

## How FRP Works

*At a Burger King in Beijing, the ordering machine placed at the entrance of the store allowed the user to select what they wanted to order and pay either by scanning a QR code or by facial recognition. A study participant who selected FRP was able to pay in less than 10 seconds.*

For both new and existing users, FRP consisted of 3 main steps:

1. **Initiation**: Click the *Pay**with**facial**recognition* button at checkout to start the payment.
2. **Validation**: The user had to face the camera and remain still. Some users were also required to enter their full cellphone number or its last four digits to complete a secondary validation.
3. **Payment****Confirmation:** The interface displayed a button that was labeled either *Confirm**payment* or *Authorize**and**confirm**payment*(for new users). After the user clicked this button, the whole process of facial recognition payment was completed. In general, the whole FRP process took about 10–30 seconds, depending on whether the user had to enter cellphone information for secondary validation.

FRP machines also supported payment by QR code. To use this additional method, users had to choose a *QR-Code Payment* option and then scan the payment QR code with the corresponding mobile-payment app (for example, AliPay if the machine supported AliPay) on their cellphones.

*The three steps of FRP, plus the final screen showing that the payment was processed.*

## Users Are Still Suspicious About FRP

Even though FRP has been around for a while in China, some new users were still unsure about how secure this form of payment was. Some said that they would prefer to use it for small payments to avoid more substantial losses.

Part of this lack of trust was due to the fact that people did not have a clear understanding of how the technology worked and how likely it was to correctly recognize someone. Almost all the mental models drawn by our participants assumed that the FRP machine compares the shots taken by the camera with previously uploaded face photos. Thus,these models implied that recognition cannot be successful if the face was obscured. Yet, in reality, face recognition is based on feature recognition, which works well even if the face is partially obscured.

For example, both Alipay and WeChat's FRP machines were able to recognize users' faces while wearing masks. But in our study, all new users and one existing user ignored the mask-friendly tagline and removed masks before facial recognition. When they were informed of that feature, they became worried and even suspicious. One of our participants said: “If it can recognize my face even when I'm wearing a mask, what exactly does it rely on? It's really kind of creepy.”

It’s unfortunate that improved recognition that overcomes face masks induces additional suspicion, but this is understandable as long as users have weak or erroneous [mental models](https://www.nngroup.com/articles/mental-models/) that don’t allow them to adequately assess such technology advances.

*An Alipay's FRP machine was placed close to the cashier in a grocery store. The Chinese text read: You can use facial-recognition payment while wearing a mask .*

To make new users comfortable with FRP, companies could provide some more (not overly technical) **details about facial recognition, how secure it is, and explain that the technology can recognize people wearing masks.**

In advertisements like Alipay's *You can use Facial Recognition Payment while wearing masks*, a brief explanation like *We can recognize you perfectly even when you wear a mask* could be accompanied by a QR code linking to a detailed explanation. This information might help alleviate the concerns of users who still have doubts.

### Validation Felt Unsecure

When using FRP, some users were prompted to enter cellphone information after their face was recognized: *Please enter your eleven-digit Alipay cellphone number* or *Please enter the last four digits of your Alipay cellphone number*. According to Alipay’s explanation on its website, whether this secondary authentication method was needed after facial recognition depended on two factors: and the reliability of the facial-recognition result and user’s previous use of a particular FRP location. If the face captured was obscured or blurred or if it was the user's first visit to an FRP-enabled store, there was a high probability that a secondary verification would be required.

*During the validation part, users needed to face the camera and remain still. Some users were also required to enter all or part of the cellphone number.*

### Cellphone Numbers Considered Unsafe for Secondary Authentication

In our study, all three participants who were asked for cellphone numbers raised concerns about the security of this approach. A participant said, "If someone looks like me and knows my cell number, will they be able to pay with my account?"

Users believed that their faces lacked “uniqueness" compared to other biometric features. They assumed that the phone number was needed as a secondary method of authentication in those cases when face recognition failed and felt that a more secure password was needed, since, obviously, cellphone numbers are known by many others (friends, colleagues, bank tellers, couriers, etc.).

In raising concerns about the security of the phone number, two participants suggested that they would prefer to complete the verification by accepting a real-time verification code on their phone, but this approach would interrupt the overall experience of FRP and significantly increase the time of paying.

To balance the ease of use and perceived security of FRP, one alternative option is **to ask users to set a dedicated FRP password**. For instance, after using FRP for the first time, users might choose to set up a FRP password in their mobile apps that could be used to authenticate them during subsequent FRP use.

### Inconsistent Use of Secondary Validation

We found that even experienced participants failed to understand the logic behind the secondary authentication but expected the process to be the same every time and became suspicious when it wasn’t. One user mentioned in a pretest interview that he often used FRP with a friend at vending machines in subway stations; he noted that his friend never had to enter his phone number, while he had to every time.

But in our field study, he was not asked to enter a phone number, , which made him feel worried. Because he had been always asked for secondary authentication in the past, this step was part of his mental model of FRP. The absence of this step made him question whether the payment had been completed: “It's true that it's fast, but isn't it too fast?”

In UX it is critical to [maintain consistency](https://www.nngroup.com/articles/consistency-and-standards/) as much as possible. Whenever interaction consistency is violated due to security requirements, companies should provide an explanation help users understand the reasons for the inconsistency. Otherwise, people will inevitably make up their own stories to explain why things work differently from time to time, giving rise to UI superstitions when the explanations are derived from misleading or incomplete mental models.

For example, if users have to go through secondary validation, an explanation could be displayed telling them that they need to go through this step because it is their first time at the store or because their face is partially obstructed.

### No Payment Information on Confirmation Page

Once users were authenticated, during the last step of FRP they had to confirm their payment by tapping a button on the FRP machine’s screen.

*In the payment-confirmation step, users had to tap a confirmation button labeled slightly differently for new and existing users.*

The confirmation page did not show any information about the payment. Some participants complained about not being sure how much they were paying — even though the clerk may have read out the price, it could be easily missed due to mask coverings and background noises (And users were not able to get a receipt even after an FRP was completed unless they asked for human service at checkout). They also did not know which bank card or account would be charged. One participant wanted to use his Alipay balance for FRP, but the payment process did not allow for changing accounts. He said that he would be willing to continue using FRP only if he could use his balance.

Like the confirmation interface for online payments, **the FRP confirmation page should present clear payment information**, including the exact amount and the account used for payment. Telling people how much they will be paying is a clearcut case of usability heuristic #1: [visibility of system status](https://www.nngroup.com/articles/visibility-system-status/).

### No Maximum Payment Amount

People new to FRP were pleasantly surprised by the speed and convenience of this payment method, but they were also worried about the security of the method and about exposing their accounts to fraud. All the new users in our study wanted to know how much money could be drawn from their accounts with FRP. One participant even said that she would look for this information in her FRP mobile app or by contacting Alipay’s customer service.

According to Alipay's official website, the maximum amount that could be paid with FRP was 1,000 yuan (about USD $150), but this information was not available during the payment process, nor could it be easily discovered in the app. **This limit should be displayed on the payment-confirmation screen for first-time users**. Moreover, being able to set the maximum payment amount inside the FRP app could increase users’ trust in this payment method.

## What’s Different from 2019？

### Interaction and UI Have Not Changed Much

Most of the issues that we identified in 2019 still hold true: the FRP interface still did not display the payment amount, the maximum payment limit, or the account the money came from. The only improvement over 2019 was that new users were shown an an *Authorize and Confirm Payment* button on the payment-confirmation, which indicated that they were giving consent to this service.

Issues | 2019 Study | Current Study | FRP didn’t ask first-time users for consent. | Yes | Fixed | Not showing the amount of paying before payment confirmation | Yes | Yes | Not showing the maximum payment amount for FRP | Yes | Yes | Users couldn’t choose from alternative cards. | Yes | Yes

When presented with user-research findings about usability problems in new designs or new technologies, UX-sceptics often react by saying that “surely users will figure this out soon enough.” And yes, users sometimes do learn how a new technology works, if it’s designed to help them construct a valid mental model. Unfortunately, as our new study has shown, it is also possible that old problems remain years later. Such problem persistence is more likely when the technology is mysterious (from users’ perspective) and isn’t designed to facilitate mental-model formation.

### Facial Registration Widely Spread in China

In recent years, facial-recognition technology has become very common in China due to both technological developments and COVID-19.

For example, nowadays many residential buildings are equipped with face-recognition devices at entrances. After registering their faces for one time, residents can enter the building freely without a physical key or fob. In our study, several participants mentioned these devices. Moreover, the devices used in these scenarios are much less accurate in terms of face-recognition results and may not be successful if people wear hats, masks, or have bangs covering the face.

This inconsistency between high-powered and low-powered face recognition systems might well have contributed to the usability problems we observed with the higher-tech FRP systems. Unfortunately, in the real world, we can’t avoid the infrastructure problem of older systems still being in place, at the same time as newer systems are being rolled out. The usability burden falls on the designers of the new technology to recognize that users’ mental models will initially be based on their experience with the installed base and to design hints and other interaction elements to set uses straight.

*A person entering a residential area in China through face recognition had to take her mask off to be recognized.*

Additionally, people in China must have a green “health code” to travel without restrictions. But in Beijing, the only way to get a health code is to register with facial authentication in the government’s health applet on WeChat. This means that everyone in Beijing has experience with face recognition, at least on their phone. Moreover, a variety of other real-life interactions such as hotel and hospital checkin, campus entry and exit, and social-security payment inquiries also involve face recognition.

Thus, despite the continued usability issues of this authentication method, **Chinese people today are more open to use it** than in 2019 due to their experiences with facial recognition in a variety of contexts.

## Takeaways

**Users agree that facial-recognition payment is fast and convenient**; it only takes about 10 seconds to pay with your face and, unlike for QR-code payments or other types of payments such as Apple Pay and Google Pay, you don’t need to fumble with your phone in order to complete it. This aspect makes it particularly convenient when shoppers’ hands are full with purchases or simply when someone has left their phone at home.

Yet, **users’ biggest concern for FRP is security**: they worry that an error in the face-recognition technology will lead to unauthorized charges.

The following lessons that we learned from this study apply to any new products that aim to change users’ existing habits — especially those related to highly sensitive areas like payments and finances:

- **Understand the gap between engineers’, designers’, and users' mental models.** Engineers and designers, due to their extensive product experience, [have different mental models than users](https://www.nngroup.com/articles/false-consensus/). And a wrong mental model affects the user's trust in the product or technology.
- **Keep users informed of how the system works.** While faced with the unknown, people's first reaction is always to worry and fear. So, make it simple for your users to understand how the technology works.
- **Maintain interaction consistency.** People will build their own mental models of how the product works based on previous experiences with it. If the interaction flow varies and users are not informed of the reasons for the discrepancies, they may lose trust or even abandon that product.
- **Give users control and keep the process transparent.** Sometimes it’s okay to add extra steps to make people feel in control in highly sensitive interactions such as purchases. In the case of FRP, lack of control over the payment source and no information about the payment amount confused and worried users.

Interestingly, the increased adoption of FRP in China is a good example of the [creepiness-convenience tradeoff](https://www.nngroup.com/articles/creepiness/): the pervasiveness of face-recognition technologies in China as well as the convenience of this payment method has made people willing to use it, in spite of serious doubts regarding its security.
