---
title: "Mobile Login Methods Help Chinese Users Avoid Password Roadblocks"
date: "2018-09-02"
url: "https://www.nngroup.com/articles/mobile-login-china/"
author: "Xinyi Chen, Yuxuan (Tammy) Zhou"
topics: [international-users, mobile-and-tablet-design]
type: article
---

People have been struggling to remember and keep track of their online passwords since the dawn of personal Internet use in the mid 1990s. Twenty years later, the problem has only gotten worse. We work, shop, and communicate primarily online and we have to deal with more accounts, and more passwords. Often, these passwords must be entered on small touchscreen keyboards, and typing them causes much grief and wasted effort. When passwords are required in the login process, users have to [recall them](https://www.nngroup.com/articles/passwords-memory/) or deal with the consequences. The burden of remembering passwords causes users to often choose easy, insecure passwords or engage in dubious password-tracking practices, like [writing down](https://www.nngroup.com/articles/security-and-human-factors/) the password or using the same password for all accounts. And when they are unable to retrieve a password, they must waste time resetting it. (Login has huge impact on employee productivity in enterprise computing, with [the best quarter of login designs saving an estimated $2.5 M per year in a 10,000-employee company compared with the worst quarter of login designs.](https://www.nngroup.com/articles/security-and-human-factors/))

In an independently funded, qualitative user research study, we investigated the role that digital technology plays in people’s everyday lives through several field studies as well as usability testing both in North America (US and Canada) and China.

Many of the United States participants complained about remembering passwords or actually encountered account-login problems due to forgotten passwords during the study. These problems ranged from being unable to gain access to an account; having to reset a password; and needing to switch to another device where the participants were already logged in. One American participant tried 7 different passwords for her Google account with no luck, and then finally gave up. “I have to remember so many different passwords for everything!”, she complained.

In contrast to our American participants, few Chinese participants had issues with their passwords.

A major contributing factor to this difference is the prevalence of mobile-login methods in China, which allow users to authenticate on a desktop site using their smartphone, without having to remember a password. A majority of our Chinese participants used mobile login during our testing sessions. And 2 of the 3 Chinese participants who struggled to remember their password on a desktop site were able to easily log into their accounts by using an alternative mobile-login method. So, the extent of the password-related issues was much smaller in China than in North America.

## In This Article:

- [Popular Mobile-Login Methods in China](#toc-popular-mobile-login-methods-in-china-1)
- [OTPs vs. QR Codes for Login](#toc-otps-vs-qr-codes-for-login-2)
- [Mobile Login in the US](#toc-mobile-login-in-the-us-3)
- [Two Roadblocks in the US: QR Scanners and Email Addresses](#toc-two-roadblocks-in-the-us-qr-scanners-and-email-addresses-4)
- [How Could Other Regions Move Towards Mobile Login?](#toc-how-could-other-regions-move-towards-mobile-login-5)
- [Conclusion](#toc-conclusion-6)

## Popular Mobile-Login Methods in China

### QR-Code Login

![JD QR code](https://media.nngroup.com/media/editor/2018/08/23/jd.jpg)

*The desktop login user interface of JD (a popular Chinese ecommerce platform) uses QR codes as the default method for unauthenticated users to scan in order to log in.*

Scanning QR codes is a popular login method in China. QR codes are two-dimensional barcodes and are often used in China to[bridge the physical and digital worlds](https://www.nngroup.com/articles/wechat-qr-shake/) of information. They are also used to facilitate authentication across devices.

![WeChat_Desktop](https://media.nngroup.com/media/editor/2018/08/23/2-wechat-desktop-login2.png)

*In order to log in to WeChat’s desktop application (left), the login window provides a QR code (right) for the user to scan with her WeChat mobile app. (In order for the login to work, the user must be logged in already on her WeChat mobile app, but almost all Chinese users are permanently logged into WeChat because it offers so many other useful features. )*

![WeChat_Desktop_scan](https://media.nngroup.com/media/editor/2018/08/23/3-wechat-desktop-scan-qr.png)

*The user can use the scanner in the WeChat mobile application on her phone to scan the QR code on the desktop screen (left), and then confirm the login (right) to the desktop application.*

There are two types of QR-code login:

1. **Corresponding mobile application:** If a user needs to log into an application or website using a device other than her mobile phone (for example, a tablet or a laptop), the system generates a unique QR code. She can then use the corresponding mobile application installed on her phone to scan the QR code. The site or application then recognizes the device (and account) used to scan the code, and the user is logged in without having to recall any passwords. Typically, the sites that use this approach (such as WeChat, Taobao, JD) have a large user population and users would likely already have their mobile application installed and use it regularly (thus being normally logged into their accounts on their smartphones).This approach works well for frequent mobile users who are likely to stay logged in on their mobile devices. It may not be appropriate for sites or services accessed primarily on a desktop device.
2. **Third-party login:** This approach works just like Facebook or Google login in the US. Users can log in to any website or application utilizing the QR scanner in the mobile app for a large third-party platform (such as WeChat or Weibo), as long as their account is linked to one of these platforms.

![58pic_login](https://media.nngroup.com/media/editor/2018/08/23/4-58pic-login.png)

*In order to log in to the 58Pic website on a PC, the login window prompts several options (left), which include using WeChat to log in. If the user chooses that option, the website provides a QR code which the user can scan using her WeChat mobile app (middle). After scanning the QR code, the WeChat mobile application asks the user to confirm the login to 58Pic using her WeChat profile (right).*

Third-party QR-code login is particularly appropriate for smaller sites or situations where users are unlikely to use the corresponding mobile app frequently. The downside of this approach is that it requires users to be willing to authenticate with a third-party service, and thus share their web activity with that service.

### One-Time Passwords (OTPs)

A one-time password is a short numerical code (for example, “211464”) that the website or application sends to a user when the user attempts to log in, usually via text message. In China (and in [India](https://www.nngroup.com/articles/mobile-behavior-india/)), this method is being widely used as a convenient alternative to logging in with passwords. As long as users have previously linked their phone numbers with their accounts, they can log in to the website with the verification code sent to the phone at any time, without entering a password or username.

![China Mobile](https://media.nngroup.com/media/editor/2018/08/23/5-china-mobile.png)

*The login screen for the China Mobile website (left) prompts for the user’s phone number to send the verification code. Once the user receives the text message containing the OTP (middle), she can enter it to complete the login process (right).*

For the OTP approach to work, users must be willing to link their accounts with their phone numbers. A downside of this method is that, when a phone gets stolen or is used by multiple people (common in developing countries), intruders could easily log into the accounts corresponding to that phone even when the phone is locked, as long as the text messages are shown on the phone’s home screen.

## OTPs vs. QR Codes for Login

The OTP method differs from the QR-code method in several ways.

- OTPs are more versatile than QR codes: the user does not need to have a mobile app for scanning the QR code.
- OTPs have a higher [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) than QR codes— they require users to type a code (or copy and paste it from the text-message app into the password field).
- OTPs and QR codes take advantage of different smartphone capabilities: text messages and camera. Because of that, OTPs can be used to log in into any channel (mobile, desktop, or tablet), but QR codes work only for logging in on devices different than the smartphone (because, for the QR-code method to work, the user needs to be logged in already in the mobile app that performs the QR-code scanning.)

Beyond those differences, the approaches are quite similar. With both methods, as long as the users have an established account and their mobile devices handy, they’ll be able to quickly access their accounts. Thus, both methods are true crosschannel solutions that require the implementation to be [seamless across devices](https://www.nngroup.com/articles/seamless-cross-channel/) — something that’s more likely to be true with an experience architecture that assumes ubiquitous mobile ownership.

Either way, these types of login systems move the spotlight from **what the user knows** (username + password) to **what the user has** (mobile device, native apps). This approach is especially convenient since many people today carry their mobile devices everywhere; its main benefit is that it alleviates the burden associated with memorizing passwords.

We’ll note that there’s a usability problem in either case: do you remember your password vs. do you know where your phone is? (And is the phone charged?) No security solution can have perfect usability, because there needs to be some barrier to getting in. However, in today’s world, reliance on having something is less burdensome than reliance on human memory, which is famously terrible.

## Mobile Login in the US

If mobile login methods can save users so much time and anguish, why haven’t these approaches already been adopted in the United States the way they are in China? OTPs are common in the United States; however, they are used mostly for added security as two-factor authentication rather than an alternative to password login. (eBay is one of the few sites that supports OTP for logging in.)

![Discover TwoFactor Authentication](https://media.nngroup.com/media/editor/2018/08/23/7-discover-2factor2.png)

*Discover.com: When the user logs into the online-banking page from an unknown device, the site asks to verify the user’s identity using a temporary identification code that could be communicated via a text message, a phone call, or by email.*

![Ebay login](https://media.nngroup.com/media/editor/2018/08/24/ebay2.png)

*ebay.com: eBay allowed the user to sign in with OTP by texting a temporary password to the phone number associated with the account.*

Besides two-factor authentication, there are other instances in which American companies are experimenting with alternative login methods.

For instance, Microsoft Authenticator allows users to authenticate to Microsoft services using their smartphones. Users must download and install the Microsoft Authenticator application on their phones. Then, when they need to log into a Microsoft site, they’re shown a two-digit number on the login screen; the login must be approved in the mobile app by selecting the correct number from a list of codes. In this case, choosing a code is even easier than entering an OTP. After the initial setup, users can approve the signin with their fingerprint or Face ID, without having to select a code. However, the substantial precondition for Microsoft Authenticator login is that users have the dedicated application installed on their phones.

![Microsoft Authenticator](https://media.nngroup.com/media/editor/2018/08/23/9-microsoftauthenticator-app-intro.jpg)

*Microsoft provides the option to use passwordless signin using its Microsoft Authenticator mobile application.*

![Microsoft Authenticator User Flow](https://media.nngroup.com/media/editor/2018/08/23/10-microsoftauthenticator-userflow1.png)

*To authenticate with the Microsoft Authenticator mobile application, users receive a code on the site they want to log in, and then select it from a list of possible codes in the app.*

![Microsoft Authenticator User Flow](https://media.nngroup.com/media/editor/2018/08/23/11-microsoftauthenticator-userflow2.png)

*After the initial setup, Microsoft Authenticator allows users to take advantage of Face ID or fingerprint authentication to authorize login on a different device.*

## Two Roadblocks in the US: QR Scanners and Email Addresses

There are two important reasons why mobile login methods aren’t as popular in the US as they are in China.

First, the **QR code method requires a handy QR-code scanner**. The embedded QR code scanner in WeChat (China’s most widely and heavily used application) means every Chinese user has this requirement already met. The scanner is already necessary for other important WeChat tasks (like adding a contact in person), so [most Chinese users are familiar with the process](https://www.nngroup.com/articles/wechat-qr-shake/).

Second, **the OTP method requires a mobile number** associated with your account. In the US, the email address is the primary identifier for users to create a new account, but in China, it is the mobile number. For this reason, it makes sense for Chinese users to verify their identity through text message with a verification code — the phone number is already linked to their accounts.

(Yes, it’s possible to send an OTP as an email, but opening an email is more tedious than reading a text message, as anyone who has reset a password already knows. Plus, texting does not require a data plan or a good Internet connection, while email does.)

## How Could Other Regions Move Towards Mobile Login?

The prevalence of mobile login in China helps Chinese users avoid the many login problems created by the need to memorize passwords. Is it possible to use the same methods in the US and the Western world?

Apple has moved towards supporting QR-code scanning: in iOS 11, you can use the camera app to automatically scan a QR code. However, this capability is still not known to most users, and it remains to be seen how it will be used for authentication (and whether Apple will provide any additional functionality to help in that direction). Facebook has followed the WeChat model and introduced QR codes as identifiers for Facebook Messenger users; these codes can be used to communicate directly with a business or a person. But their popularity is still fairly low. Until these big companies will find a way to make QR codes important to people so they will learn how to scan them quickly, it is unlikely that this method will become a viable solution to the problem of authentication.

As far as OTPs, Americans are arguably more concerned than Chinese about sharing their cell-phone numbers with third parties. While they may be willing to do so with companies that they trust (such as financial institutions or other big brands), it is unlikely that they will do it with random sites on the web. Telemarketing calls and spam may be one reason, but another one is that [the cell-phone number has already become similar to the social-security number in its power to identify people](https://www.nytimes.com/2016/11/13/business/cellphone-number-social-security-number-10-digit-key-code-to-private-life.html) and, as individuals may get more aware of its power, they will likely become even more reluctant to share it.

## Conclusion

Ten years ago, we described single signon as the [Loch Ness monster of the intranet world](https://www.nngroup.com/articles/enterprise-portals-are-popping/): People hear about it and even believe it exists, but they've yet to see it for real. China’s login solutions are not true single signon, because they still require users to authenticate with each individual site. However, they constitute a major leap forward in login usability, and maybe we can stretch the metaphor to characterize them as mountain gorillas in the mist: they definitely exist, and you can go see them. However, they aren’t usually spotted outside their native habitat.

In mobile-first societies such as China, a large majority of users have first accessed the Internet through their mobile phone. The mobile-phone primacy has had some important implications: the use of phone numbers (instead of emails) as identifiers and the importance of platforms like WeChat for communication, which pushed the use of QR code as a way to easily add contacts and form groups and subsequently made this technology pervasive and adopted in other areas of life — digital or not. In contrast, in desktop-first societies such as the US, the conventions that we inherited from the early days of the web (such as email-based identification) are difficult to circumvent, and we’re still waiting for the “killer app” with QR codes that will push them into the public attention and will finally allow us to take full advantage of their power.
