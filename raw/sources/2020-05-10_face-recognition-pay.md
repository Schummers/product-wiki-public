---
title: "Making Cutting-Edge Technology Approachable: A Case Study of Facial-Recognition Payment in China"
date: "2020-05-10"
url: "https://www.nngroup.com/articles/face-recognition-pay/"
author: "Feifei Liu"
topics: [ai, design-patterns]
type: article
---

Recently, facial-recognition payment (FRP, or *Scan the face to pay*, 刷脸支付) has gained popularity in China as a new digital-payment method at physical stores.

Unlike the United States, China already has widespread mobile payment as a primary method of making purchases. In some places, cash isn’t accepted — only mobile payment. A Chinese shopper can leave home without her purse, as long as she has her phone.

This wallet-free reality is largely due to [QR-code scanning](https://www.nngroup.com/articles/wechat-qr-shake/): people scan the QR code of a shop and pay the amount of the order on their phones. Facial recognition takes this process a step further — you don’t even need your phone, just your face.

## In This Article:

- [How Facial-Recognition Payment Works](#toc-how-facial-recognition-payment-works-1)
- [Facial-Recognition Payment vs. Face ID](#toc-facial-recognition-payment-vs-face-id-2)
- [Methodology](#toc-methodology-3)
- [Convenience Is Not Enough](#toc-convenience-is-not-enough-4)
- [Poor Onboarding = No Trust](#toc-poor-onboarding-no-trust-5)
- [Better Onboarding Techniques to Increase Confidence](#toc-better-onboarding-techniques-to-increase-confidence-6)
- [Using Facial Recognition to Speed Up Interaction — Good or Bad?](#toc-using-facial-recognition-to-speed-up-interaction-good-or-bad-7)

## How Facial-Recognition Payment Works

Let’s look at the example of a bakery called WeiDuoMei. A specialized touchscreen device is placed at the checkout counter of the bakery. It’s similar in size to an iPad Mini. Produced by either Ali or Tencent (which are the two companies that monopolize the mobile-payment market in China), the device has access to the facial-information database of the parent company. So, if Tencent has your picture, you will be in its facial-information database, and the machine will be able to find you.

The cashier enters the amount of money for the order, which is then shown on the device screen. A user just needs 10 seconds and two taps to finish the payment:

1. The user taps *Pay with Face Recognition* on the screen of the device. The device scans the face and recognizes the user.
2. The user then taps *Confirm Payment* and is done.

![A user tapped Pay with Face Recognition and then Confirm Payment to pay](https://media.nngroup.com/media/editor/2020/05/04/frp_twosteps_withbackground.jpg)

*The specialized device supported facial recognition payment of Ali Pay in a bakery in Beijing. A returning user used facial-recognition payment to pay in 2 steps within 10 seconds.*

## Facial-Recognition Payment vs. Face ID

At first glance, facial recognition payment might seem very similar to the process of using Apple Pay on an iPhone: the newer iPhones (iPhone X and newer) use “Face ID” to check identity and approve payment. However, the key difference here is the reliance on a device. To use Apple Pay via Face ID, users must own a late-model iPhone, must have it with them, and have it at least partially charged. To use FRP in China, users only need to have a validated [WeChat](https://www.nngroup.com/articles/wechat-integrated-ux/) or Ali Pay account and an associated bank account, no matter what types of phones they have (or if they have a phone with them at all).

This technology enables a much larger audience to pay with their faces without worrying about the compatibility of their devices. While all new iPhone and Pixel models have face recognition, these devices are not that common in China. In fact, the most popular and middle-level smartphones in China don’t have facial-recognition authentication and still use fingerprint or passwords for authentication. Thus, FRP allows even users who own old-fashioned phones to pay with their faces.

A hardware vendor has an obvious interest in tying an important aspect of society (in this case, money) to a piece of equipment, but for users, it’s much better not to have to carry stuff around or to be locked into specific products.

Payment Methods | Device Requirements | Software Requirements | Time Cost | Apple Pay or Android Pay | A phone that supports facial recognition | Credit/debit card preset in Apple Pay | Within 15s | QR-code scanning | A smartphone with a camera | An Ali Pay/WeChat account and an associated bank account | 30s – 1min | Facial recognition | None (well, a face) | An Ali Pay/WeChat account and an associated bank account | 10 – 15s | (For frequent users, it could be less than 10 seconds)

Device Requirements | Software Requirements | Time Cost | Apple/Android Pay | A phone that supports facial recognition | Credit/debit card preset in Apple Pay | Within 15s | QR code | A smartphone with a camera | An Ali Pay/WeChat account and an associated bank account | 30s – 1min | FRP | None (well, a face) | An Ali Pay/WeChat account and an associated bank account | 10 – 15s | (For frequent users, it could be less than 10 seconds)

This new method has been adopted in many physical stores in China: clothing stores, grocery stores, vending machines, and checkpoints of subway stations. It seems cool and convenient, because it can reduce checkout time and the hassle of pulling out mobile phones. But, how do users view this new method of payment? How hard is it for new users to learn how the technology works? And do people really *want* to pay with their faces? We conducted a study to find out.

## Methodology

In Beijing, we conducted a study involving both interview and observation sessions. The study had 5 participants between the ages of 18 and 42; three were female and two were male. Two participants had used the facial-recognition payment technology before, but three were first-time users.

We interviewed each participant for 5–10 minutes before the session. We asked questions on payment habits for both online and offline shopping and FRP experiences (if any). We also asked them to draw and describe their [mental models](https://www.nngroup.com/articles/mental-models/) of the FRP technology and how it might work.

After the interview, they were invited to try FRP (associated with Ali Pay in this study) in one of two bakery chains that supported this new technology. During the whole shopping process, especially when paying, participants were encouraged to think aloud. After the observation session, we conducted another 10–15-minute interview. Participants spoke about the experiences, discussed the pros and cons of this new payment method, and revised their mental-model drawing if they wanted.

## Convenience Is Not Enough

All participants, but especially new users, praised the convenience of FRP. Even for first-time users, the method reduced the total payment time to around 15–20 seconds. One 35-year-old male, new to this process, couldn’t believe it happened so fast. When he finished the payment, he asked the cashier twice “So is it done?” After being repeatedly reassured that he had paid for his croissant, he left.

The below figure shows the process that a first-time user needs to go through in order to use the FRP technology. After the cashier enters the amount the customer needs to pay, the customer is prompted to stand before the specialized device. When the *Pay with Face Recognition* button on the screen is tapped, the customer’s face is captured and used to retrieve the associated Ali Pay account. Then, the user must enter the phone number listed in the Ali Pay account to validate identity. Once the identity is confirmed, the user taps *Confirm Payment*.

![It takes four steps for users to finish the payment with FRP: Start page, Face capture, Validation and confirmation, and Finish payment.](https://media.nngroup.com/media/editor/2020/05/01/frp-user-flow_nobackground.png)

*The user flows for first-time users and returning users of the FRP technology.*

![It takes four steps for users to finish the payment with FRP: Start page, Face capture, Validation and confirmation, and Finish payment.](https://media.nngroup.com/media/editor/2020/05/04/frp-user-flow_mobile.png)

*The user flows for first-time users and returning users of the FRP technology.*

Sounds convenient, right? But actually, **4 out of 5 participants we interviewed still preferred QR-code scanning**, even after they experienced this new, rapid way of paying. Why? Besides the fact that [users often hate change](https://www.nngroup.com/videos/users-hate-change/), the biggest problem was that the **onboarding experience** (or lack thereof) didn’t make them feel secure enough.

## Poor Onboarding = No Trust

Anything that relates to finances is generally regarding as private and requiring high security: people don’t want to risk their money. Although facial-recognition payments were fast, the onboarding experience for the first-time users was poor, and, as a result, they became suspicious, did not trust the technology, and said they did not want to return to it. Essentially, we witnessed a [halo effect](https://www.nngroup.com/articles/halo-effect/) — their first interaction was unsettling, so they viewed the entire technology negatively.

### Mistake #1: Ali Pay Didn’t Ask First-Time Users for Consent

Upon tapping the *Pay with Facial Recognition* button, a face-capture screen popped up immediately. Some participants were confused.

A 33-year-old female said, “It made me feel that the Ali Pay app allowed you to do this [FRP] without any consent. I first should authorize this FRP service.”

*Mistake #1: Ali Pay didn’t ask for users’ consent when they used FRP for the first time.*

Actually, Ali Pay did ask for consent, in a way. The company had updated its user agreement and notified users of the update on their next login.

None of our participants in our study even realized the existence of such a notification. This isn’t surprising — it’s a common joke that nobody reads privacy policies. **Adding a clause of legalese to the end of a long, formal document is not an acceptable way to notify users of a significant change.**

### Mistake #2: Ali Pay Didn’t Explain How The Face Was Recognized

When setting up Face ID on an iPhone, first-time users are asked to record their face as they move their head side-to-side, to capture different angles. This simple onboarding process makes sense to users — they know that the iPhone can recognize their faces, because they trained it to do so.

The Ali Pay FRP doesn’t have any such “training” step. Instead, it uses the government-ID data that users put in when they registered their Ali Pay account. (This identity information, similar to a driver’s license number, is required for most online-payment services in China. It also includes a photo of the user.)

However, most of our participants had registered their Ali Pay accounts a long time ago and didn’t remember that Ali Pay had their identity and photo. So, they developed **false mental models** for the technology. They believed that, when they used FRP for the first time,**it was a registration process, not a recognition process**. In other words, they thought that, when their picture was taken by the device, the software created a link on the spot between that face and the account indexed by the phone number.

*Mistake #2: Ali Pay didn’t tell users how the app recognized their faces. Participants incorrectly believed that when they used FRP for the first time and had their picture taken, the system learned how they looked like and associated that information with the account matching their phone number, so they were afraid that someone else could have used their phone number to register and steal their money.*

This is a potentially disastrous misunderstanding. The **implication** of this misunderstanding is that, if a user hasn’t yet used FRP, **anyone with that user’s phone number could go buy something and associate her own face with the account linked to that phone number.** (Again: That isn’t how the technology *actually* works, but that’s how participants *interpreted* the process. Belief overrules facts, to drive opinion.)

The participants asked questions like, “How does it know who I am? What if you used my phone number [to register]?” They were so worried about the account security that researchers had to debrief for a while after the study to explain that their accounts were not at risk. (This step should have been done by Ali Pay!)

### Mistake #3: Ali Pay Didn’t Allow Users to Choose the Account Used for Paying

After first-time users provided their phone numbers, they were asked to *Confirm Payment*. But Ali Pay users can add multiple cards to one account, so first-time users didn’t know which of their cards will be charged.

A 33-year-old participant was mad when he found out that the money was taken off via Ant Credit Pay, a product of Ali Pay that he didn’t like and did not want to use anymore.

He complained, “They forced me to use their product, and now I have to remember to pay them back later on!”

![For both first-time and returning users, they couldn't choose from other credit cards.](https://media.nngroup.com/media/editor/2020/05/01/mistake3-nobackground.png)

*Mistake #3: Users couldn’t choose from alternative cards or bank accounts.*

It’s likely that the Ali Pay designers intentionally didn’t want to let people choose an account — after all, the whole point of FRP is to have lightning-fast checkout. Fewer choices mean faster payment. We see similar design choices in American checkout products like Square and Clover — once a user inputs an email address for a receipt, it becomes associated with that credit card, and the user doesn’t have to enter it again.

However, users should be able to choose their own default payment method — at least when they use the technology for the first time. They should not be forced to use Ali Pay’s financial products. Since they can easily choose from a list of payment methods while paying by scanning QR codes, why can’t FRP also allow for it? Alternatively, people should at least be told what the default account is and how they could change it (if at all) **before they pay**.

### Mistake #4: Ali Pay Didn’t Ask for Confirmation Passwords

The mobile Ali Pay app requires users to enter a password in order to pay. People can disable the password if they want to, but by default they will have to enter it (in much the same way people in the US have to enter a password or have their face recognized before they use Apple Pay, for example). As a consequence, users were conditioned to enter a password when using Ali Pay. When Ali Pay FRP didn’t ask for the payment password, people were confused and suspicious.

One participant seemed astonished when he used FRP without a password. He said, “I have never disabled that feature [enter passwords to pay], and I enter passwords when I pay for something that is just 5 yuan (around 0.8 dollars). How can they do this?”

The absence of the password made him nervous. He added, “No passwords, no security!”

*Mistake #4: FRP didn’t ask for users’ consent to pay without entering a password.*

It’s likely that facial recognition is so reliable and secure that Ali Pay decided it didn’t need to add an extra layer of protection (and an extra step) with a password. However, while **Ali Pay may have faith in the security of the technology and a good understanding of how it works, new users do not**. They need to be convinced.

## Better Onboarding Techniques to Increase Confidence

Ali Pay FRP’s issues largely stem from **a failure to help users understand the new technology**(at least on a basic level) and adjust to it. This is a growing challenge for UX. We’re beginning to design interfaces and experiences around advanced new technologies (facial recognition, AI systems, VR, AR, autonomous vehicles, etc.). As we’ve seen in this example (and in many others, in domains such as [cloud computing](https://www.nngroup.com/articles/cloud-storage/), [intelligent assistants](https://www.nngroup.com/articles/mental-model-ai-assistants/), and [machine learning](https://www.nngroup.com/articles/machine-learning-ux/)), it’s all too easy **create false mental models and distrust**.

The key to avoiding these problems is a little extra handholding — **carefully introducing the technology in a simple way**, so that users can understand it and feel in control. While onboarding processes may [not be necessary for simple mobile app interactions](https://www.nngroup.com/articles/mobile-tutorials/), they’re needed for new technologies.

Designers in the early days of software faced a similar problem. Most people had no prior exposure to digital interfaces, so designers had to figure out how to make them approachable. One solution to this challenge was to use [direct manipulation](https://www.nngroup.com/articles/direct-manipulation/) and heavily [skeuomorphic](https://www.nngroup.com/articles/flat-design/) interfaces (for example, UI tabs that resembled physical tabs on file folders) to help users have a rough understanding of how things worked. Over time, as a larger proportion of the population gained experience and confidence, those hand-holding designs could be toned down, because users understood how the products worked.

Let’s explore how this particular cutting-edge technology, Ali Pay FRP, could be made more approachable.

### Fix #1: Ask for Consent

If you want to take a picture of someone you never met before, it’s polite to ask for permission first. It’s creepy if you don’t. The same is true for a digital product.

WeChat’s FRP did a better job of asking first-time users for consent. When a first-time user checked out in a supermarket using WeChat’s FRP, a popup window asked for approval before it began the payment process. Users could browse the detailed agreement if they wished to.

*WeChat Pay’s FRP asked users to authorize this new service when they used it for the first time. The popup window read,* Enable facial recognition payment of WeChat. Face is your unique feature. This payment method is safe and convenient. *A link to the full version of the agreement was also provided.*

While the additional step of consent may not be legally necessary and might slow down the first checkout by a few seconds, it would’ve been worth slowing down to increase users’ [sense of control](https://www.nngroup.com/videos/usability-heuristic-user-control-freedom/).

### Fix #2: Present Enough Information to Prevent Misunderstanding and Increase Confidence

When introducing a new technology, we must provide users with adequate information. That can be tricky — we have to give enough information to make them feel comfortable, but not so much information that you need a degree in computer science to understand it.

In this case, it would have been simple enough to tell people how Ali Pay recognized their faces. Designers don’t need to get into all of the details of how exactly the facial-recognition process works, but they should at least clearly state that Ali Pay uses the customer’s ID photo.

![Fix 2 - Add A Step](https://media.nngroup.com/media/editor/2020/05/01/technique2-addastep-nobackground.png)

![Fix 2 - Step 2](https://media.nngroup.com/media/editor/2020/05/01/technique2-step2-nobackground.png)

*Adding a step to tell users how the app got their facial information can help build correct mental models.*

Some users also raised privacy and security concerns. For example, two users wondered, “Where would it store my facial information? Who would have access to that? How long would my face be stored in this machine [for confirmation]?” They had no idea where to find the answer, either.

These questions could likely not be answered all at once during the first-time usage, and the local cashier may not be able to help. But these in-depth questions could be addressed on **other channels**.

One user tried to check her phone after she used the service. She said:

> “I am thinking it’s my first time using it [FRP]. There should be a notification [from the Ali Pay app] telling me that I used that for the first time, asking me to validate the information, or letting me learn more about it.”

*To help users understanding how the FRP technology works, Ali Pay could send push notifications to users who just used it for the first time. Users could learn details about how it works if they’d like to.*

The JD unmanned store in Beijing used a different approach to help users register their face for FRP. Outside the door of the store, users were prompted to scan a QR-code and use a [WeChat mini program](https://www.nngroup.com/articles/wechat-mini-programs/) to record their faces and choose payment methods.

People could, thus, take the time to learn what data the product was gathering and how. This is an elegant way of providing details without slowing the actual checkout process down. Users could also manage the FRP settings on the phone: they were allowed to choose from more payment options.

*FRP in JD unmanned stores invited users to go through the registration process on their smartphones. They learned that this payment method would record their faces and could choose their preferred payment method.*

### Fix #3: Allow Customization and Compromise When Challenging Existing Mental Models

For any new technology, if it challenges or violates users’ existing mental model, it’s better to allow some customization or compromise at first, to habituate people with it gradually.

In case of Ali Pay FRP, some users have the mental model “no passwords = no security.” Thus, allowing passwords as an extra layer of protection could be a compromise. Again, Ali Pay’s designers might know that isn’t necessary from a security perspective, but if it makes people more comfortable as they warm up to the new tech, what’s the harm?

One user suggested, “There should be an amount limit for this payment method, like a threshold that I can set.” She added that she would feel safer if she could pay a large amount with the combination of the face and password.

Actually, Ali Pay and WeChat Pay both used such a strategy when they were promoting QR-code payment and users thought it was not secure enough. While users could choose to enter the password every time when pay by QR code, they could also enable a feature called *Small Amounts No Passwords*. This service allowed users to pay without passwords when the order amount was below a user-set threshold (ranging between 200 and 5000 yuan). As they became more comfortable with QR-code scanning, more users enabled this feature, to increase efficiency.

### Fix #4: An Informative and Clear Layout

FRP’s payment confirmation page was not clear for both first-time users and frequent users.

For first-time users, the payment completion and the phone-number validation were done in the same step, with no payment-confirmation page at all.

For frequent users, though the device displayed their name, face, and account information, the key information — how much they were paying — was missing. So, both user groups in our study didn’t realize that tapping *Confirm Payment* was the final step of the process.

The confirmation page should provide adequate information in a clear way. As the key page of the flow, it should summarize the payment information, include facial and account information of the user, amount of the order, and the payment method. A better design is shown below (on the right).

![Fix 4](https://media.nngroup.com/media/editor/2020/05/04/technique4_v2.png)

*The current version (left) and a better design (right) of the confirmation page of the FRP: Adding the payment amount and payment method (or account) keeps users informed and confident.*

If there are similar or identical components of user flow for both new and current products, **align them to create an**[internal consistency](https://www.nngroup.com/videos/usability-heuristic-consistency-standards/). This approach can help users to feel in control of the interaction.

For example, a typical payment-confirmation page on Ali Pay contained three components: the amount of the money, memo, and payment method. If the FRP confirmation page also had these components and a similar visual design, it will be more likely that people recognize this page as the final step in the process.

*Ali Pay mobile app: The confirmation page for an online transfer includes the payment amount, item (memo), and payment method. Users are familiar with the layout and assume that the final step of any payment should involve these components.*

## Using Facial Recognition to Speed Up Interaction — Good or Bad?

Nowadays, many products with advanced technology aim to provide convenient services, which speed up the interaction and increase efficiency. In this case, Ali Pay used facial-recognition devices to speed up in-store payment.

However, users don’t necessarily appreciate this convenience, especially since it comes at the expense of those qualities of the interaction process that they believe to be critical. In our study, users’ security and privacy concerns outweighed FRP’s increased checkout efficiency. Since QR-code payment is widely used and perceived as fast, some people didn’t see why saving 15 extra seconds was worth feeling insecure about your money.

Offering an informative but not overwhelming onboarding experience for first-time users can reduce concerns and prevent false mental models. **“ Less is more ” isn’t always applicable:** you should not sacrifice onboarding for the sake of convenience **.** Once the majority of your population is familiar with the process, then you can think about streamlining it.

A longer but more informative first-time user experience can boost users’ confidence and invite them to try the new product again. Then that’s the time to show off your product’s advantages — in this case, the increased checkout efficiency.
