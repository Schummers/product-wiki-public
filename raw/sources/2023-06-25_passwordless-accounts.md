---
title: "Passwordless Accounts: One-Time Passwords (OTPs) and Passkeys"
date: "2023-06-25"
url: "https://www.nngroup.com/articles/passwordless-accounts/"
author: "Raluca Budiu"
topics: [design-patterns, mobile-and-tablet-design]
type: article
---

Passwords are a major pain point in any user experience. Until recently, this pain point was considered unavoidable. But one-time passwords and passkeys save users from the hassle of having to create, store, retrieve, or remember a password. These new developments are particularly seamless on mobile, but they can improve the login user experience on desktop as well.

## In This Article:

- [The Problem with Passwords](#toc-the-problem-with-passwords-1)
- [Passwordless Accounts](#toc-passwordless-accounts-2)
- [Passkeys](#toc-passkeys-3)
- [Recommendations for Designing Passwordless Accounts](#toc-recommendations-for-designing-passwordless-accounts-4)

## The Problem with Passwords

**Passwords are annoying .** They are hard to [create](https://www.nngroup.com/articles/password-creation/), hard to type, and hard to [remember](https://www.nngroup.com/articles/passwords-memory/).

Many of us rely on our smartphones to save passwords, which certainly helps to reduce the pain of passwords. For example, in a recent survey that we carried out:

- 76% of the respondents said they save their passwords on their phones
- 17% use a third-party password manager
- 10% use both

*According to our survey, most users save their passwords on their phones. The bar chart shows the percentage of respondents who selected each option; error bars represent 95% confidence intervals.*

Even if you use a crutch such as a password manager (whether built into the phone or a third-party one), the interaction is clunkier when a password is involved.

For example, sometimes a password field is not recognized and the **user is not offered the choice to use a password-manager generated password**. Or, sometimes the password manager will not read the password requirements on the site and will create **a password that might not match what the site or app demands**.

*Unsplash for iPhone: Even though the focus was in the* Password *field, the phone did not recognize it and did not suggest a password.**The strong password created by the iPhone did not satisfy the site’s requirements.*

Additionally, if the user saves passwords on multiple devices, they may have **trouble remembering on which device they created the account**. For example, I always struggle to figure out whether the password is in iCloud on one of my Apple devices, in Edge or Chrome (which I use on my Windows computer), or in the 3rd party password-manager application that I also use.

There are **two important interaction flows** associated with passwords: [registration and login](https://www.nngroup.com/articles/checklist-registration-login/).

With **login**, we saw significant usability progress once biometric authentication became available. People who were willing to share their fingerprint and face data could skip the recall and entry of a password. As a result, biometric authentication saved users considerable time and effort.

But how about **registration**? Until recently, whenever users had to create a new account (unfortunately, this is way too often on modern sites and apps), they had to create a password that satisfied complicated requirements which varied depending on the site or application. Often, [these requirements would not be disclosed in advance](https://www.nngroup.com/videos/disclosing-password-constraints/), forcing people to guess what the password should look like. Then, when they failed to guess correctly, they had to navigate the obligatory [error message](https://www.nngroup.com/articles/error-message-guidelines/) that told them that the password does not satisfy all the constraints.

*MLB for iPhone did not disclose what requirements the password had to satisfy.*

However, a new, welcome trend that alleviates the registration problem is that of passwordless accounts.

## Passwordless Accounts

Definition: A **passwordless****account** is an account that does not have a password associated with it. The user can securely authenticate and log in, but there is no fixed password that they need to type to access their account.

There are two types of passwordless accounts: OTP-based and passkey-based accounts.

### OTP-Based Passwordless Accounts

**One**-**time****passwords** (**OTPs**) are codes that are sent to a phone number or email associated with an account. These codes serve as temporary passwords: the user can log into their account using the OTP for authentication. (When the code is sent through the email, it sometimes takes the form of what’s called a **magic link**.)

One-time passwords are useful because the user does not have to:

- **Retrieve the password** from their long-term memory or from an [external-memory](https://www.nngroup.com/articles/working-memory-external-memory/) source (like the browser or a password manager)
- **Type the password**

However, one-time passwords do incur some costs — namely, the user has to:

1. **Wait****for****the****OTP** to become available — that is, wait for it to be received on their device; this cost can be significant in areas with poor connectivity
2. **Access the OTP** and input it in the site or application that sent it

Note that the access cost can be minimal if the OTP is sent through a text message that appears as a suggestion on top of the keyboard (without the user having to leave the corresponding page). However, accessing the **OTP is more difficult when the link is sent through email.** This is because the user must switch applications and access that email in order to authenticate. Moreover, there is also the risk that the email will be filtered out as spam by the email client.

Until recently, OTPs were used mostly for login — account holders could choose to log in by inputting their passwords or through an OTP. But why couldn’t the user use OTPs at all times, without ever creating a password?

That is the idea behind OTP-based passwordless accounts. **With a passwordless account, the account holder always uses an OTP or a magic link to log in**. They don’t have to create a password: whenever they want to log in, they are sent an OTP or a magic link.

*Yummly for Android asked for several pieces of information at registration, but a password was not one of them (left). To log in to the account, the user had to click a magic link in the email (right).*

Even though OTPs can be great if the user has forgotten their password, as we emphasized above, they are not without costs. Users who store passwords on their phones or in their browsers may find it easier to have them automatically filled in by the browser. Thus, such users may prefer to define a password for the account and then have the browser automatically fill it in for them.

Therefore, even for those accounts which can be created without a password, we recommend that you **offer users the option to later attach a password to the account**. That way, they can log in even faster — at least on a subset of their devices. Users should not, however, be forced to create a password if they do not want to.

Additionally, **allow****users the choice to log in using biometric****authentication**. That can speed up the process even more for those people who are willing to do it. (Our survey shows that **83% of users use a biometric method of authentication at least occasionally**, with a 95% confidence interval between 73%–87%.)

*Kayak for iOS (left) and Waze for iOS (right) allowed users to add a password to their account. However, none enabled them to use biometric authentication to log into the accounts.*

### OTPs on Desktops

OTPs can be used on desktops or laptops, too. If the code is sent through a text message, it may be a little harder to copy it on the desktop, unless the user has set up texting on their computer (for example, using the Messages application on a Mac). But the user may be able to easily copy and paste an email code, as the screen is larger and task switching is generally easier on desktop.

For that reason, especially for responsive sites that are likely to work on both desktop and mobile, **consider offering the user the choice of how to receive the OTP — through email or text message**.

## Passkeys

Another welcome trend in the world of authentication is passkeys. Passkeys are different than OTPs, but they also create a passwordless user experience. They rely on the other advancement in login technology — biometric authentication.

A **passkey** is a password that is invisible to the user. When you’re trying to register on a site that supports passkeys, your device will create a password for you; that password will be stored encrypted on the device (or somewhere in the cloud). Next time when you will log into the site, your device will use biometric authentication (such as fingerprint or face ID) to identify you, and, if that authentication was successful, will send your encrypted passkey to the website. The website will then log you in.

*Kayak for iPhone: The experience of logging in using a passkey*

Passkeys are obviously more usable than regular passwords: **the user does not have to either remember, store, or type them**. They also have lower [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) than OTPs: users do not have to type them, copy or paste them, or even click on a link to select them.

Additionally, **they are more secure than regular passwords** because they are not stored by each website. Instead, they are stored encrypted on your device, so they are less susceptible to data breaches and hacks. Even if the data was stolen, the thieves would have to also have access to your biometric authentication to use them. Plus, they cannot be used for phishing because they only can be sent to the sites they are associated with.

The catch is that, **if you are going to use the site across several devices, it may not be possible to easily take advantage of them on all**. For example, if you’ve created your passkey on an iPhone and you’re trying to authenticate on an Android or Windows tablet, the website will have to show a QR code and you will need to scan it with your iPhone to enable authentication. (However, passkeys will work seamlessly across all Apple devices because they are synced in iCloud.)

*Kayak.com: Users using the Chrome browser to access Kayak.com can choose to authenticate using a passkey created with a phone (left), by scanning a QR code with that phone’s camera (right).**Once the user scans the QR code with their phone, they are prompted to log in using the passkey. If they agree they are automatically logged in on their desktop.*

So, the benefits of lower interaction cost exist only if the user is using the same device (or the same device ecosystem) to access the website. But still, most people have their phones nearby at all times. Scanning a QR code with the phone’s camera is easier than typing a password or copying and pasting a string.

## Recommendations for Designing Passwordless Accounts

To summarize, passwordless accounts can help reduce friction during login and registration. Follow these recommendations to ensure a smooth passwordless-account experience for your users.

- **Offer the options of (1) creating and using a password****and (2) biometric authentication** after users have created a passwordless account.**** Some users may prefer these to using an OTP or passkey, so it’s a good idea to provide the choice.
- **For OTPs, let users choose between email and text messages.** Remember that some users may have text messages delivered to their current device, while others will not.
- **For passkeys, support multiple devices by allowing users to scan a QR code.** This is especially helpful if they are using a device that doesn’t have their passkey stored on it.
