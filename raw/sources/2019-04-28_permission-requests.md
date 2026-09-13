---
title: "3 Design Considerations for Effective Mobile-App Permission Requests"
date: "2019-04-28"
url: "https://www.nngroup.com/articles/permission-requests/"
author: "Maria Rosala"
topics: [applications, mobile-and-tablet-design]
type: article
---

## In This Article:

- [What Are Permission Requests and Why Have Them?](#toc-what-are-permission-requests-and-why-have-them-1)
- [3 Design Considerations](#toc-3-design-considerations-2)
- [1. Permission-Request Copy](#toc-1-permission-request-copy-3)
- [2. The Timing of the Permission Request](#toc-2-the-timing-of-the-permission-request-4)
- [3. Decision Reversal for Permissions](#toc-3-decision-reversal-for-permissions-5)
- [Avoid Dark Patterns](#toc-avoid-dark-patterns-6)
- [Summary](#toc-summary-7)

## What Are Permission Requests and Why Have Them?

An app must request permission before accessing resources such as the camera, current location, or microphone, on the user’s mobile device. The app sends (via the operating system) a request in the form of a [modal dialog](https://www.nngroup.com/articles/modal-nonmodal-dialog/), asking the user to grant or decline access.

![An image of the permission requests from Google Translate on iOS and Android side-by-side. The permission request asks the user to allow Google Translate access the microphone to enable dictation.](https://media.nngroup.com/media/editor/2019/03/20/google_translate.png)

*Google Translate requires access to the microphone to use the dictation feature; iOS (left) and Android (right) permission requests differ slightly.*

There are slight differences in how these requests are presented across mobile operating systems. As you can see from the example above, in iOS the user is asked for access to the microphone, whereas in Android the user is asked for permission to record audio. Moreover, in iOS, the modal dialog contains what’s called a [purpose string](https://developer.apple.com/documentation/uikit/core_app/protecting_the_user_s_privacy/accessing_protected_resources), which describes why the app is requesting access. This type of information is not present in Android. **It’s up to Android designers to ensure that the rationale behind the request is introduced before the modal dialog appears**.

**Permission requests give users perceived and actual control** over their personal (and potentially sensitive) data. The decision to allow access can be a significant one, as the app often retains access to the resource until users uninstall the app or deliberately revoke the permission in their device’s permission settings. As a result, users need to trust that the app won’t ever maliciously access resources.

**App permission requests are still often poorly designed,** despite fairly extensive guidance from the iOS and Android development community. One reason could be that permission requests are often not considered to be part of UX design, because the UI component for the permission itself is dictated by the operating system. It may also be hard for UX designers and app developers to understand why permission requests are so important. After all, who wouldn’t want to give access to every resource so they may use all the excellent functionality?

However, **app permission requests contribute to the overall user experience and should follow the same usability principles as other features.** They should:

- be easy to use and [understand](https://www.nngroup.com/articles/plain-language-experts/)
- fit the user’s [mental model](https://www.nngroup.com/articles/mental-models/)
- promote genuine, informed choice
- stand up to scrutiny from regulators

When permission requests are designed well, they seem reasonable and nonintrusive; users barely think twice when dealing with them. On the other hand, **when permission requests are designed poorly, users often feel uncomfortable, confused, and irritated**. They may even consider uninstalling the app and looking to competitors, especially if the app’s brand isn’t strong and the functionality doesn’t provide great utility.

## 3 Design Considerations

3 design considerations greatly affect the quality of a permission request. These are:

1. Permission-request copy

2. Timing

3. Decision reversal

## 1. Permission-Request Copy

The best permission requests **communicate the rationale behind the request.** In one study of 15 mobile apps, Tan and his colleagues found that users were **12% more likely to grant a permission** request when they were given a reason for the request. This estimate came from randomly showing or removing the purpose string included with each request, as designed by its vendor, even when the explanation was fairly poor.

Of more interest, the researchers also tested a series of different reasons for requesting access to contacts in a party-planning app they had created. Here, the most compelling reason (*Let Party Planner use your contacts to autocomplete email addresses)* resulted in a whopping **81% lift** in granted requests compared to the least compelling reason (*Party Planner would like to access your address book to show you the cheapest attractions by your contacts’ location and other purposes*.). As we’ve said many times before, [UX copy drives decision making](https://www.nngroup.com/articles/interface-copy-decision-making/). It’s not at all surprising that the wording of a request came close to doubling the acceptance rate, because [words are one of the most important elements of the user experience](https://www.nngroup.com/courses/writing/).

When users read a permission request, they perform an implicit **cost­–benefit analysis.** They ask themselves how much benefit they will receive from granting this permission and how much they trust the app to allow it access. **Designers must write understandable copy**, especially when communicating the rationale for unexpected permission requests, so as not to alarm users and to help them understand why the app requires access to a resource on their device.

In order to assist users in making an informed choice:

- **write content that is free from**[technical jargon](https://www.nngroup.com/articles/plain-language-experts/)**and**[focus on user-oriented benefits, rather than system-oriented features](https://www.nngroup.com/articles/user-centric-language/)
- clearly **communicate to users**[what they’ll get in return](https://www.nngroup.com/articles/reciprocity-principle/)
- **don't request access to resources without providing any value to users**, as they may become suspicious of your app and [brand](https://www.nngroup.com/articles/brand-experience-ux/), and such data collection can be deemed excessive by regulators

![An image of an iOS permission request from Instagram that reads: "Instagram" would like to access your photos. This lets you share photos from your library and save photos to your camera roll.](https://media.nngroup.com/media/editor/2019/03/20/instagram_access_photos.png)

*Instagram clearly indicates the benefits of allowing the app to access the user’s photo library: the user can share photos with others and save photos edited within the app locally.*

![An image of an iOS permission request from United Airlines' mobile app. Permission reads: United would like to access your camera. Camera usage and photo for scanning various Travel documents and Payment options.](https://media.nngroup.com/media/editor/2019/03/20/united-access-camera.png)

*In the United Airlines iOS app, the purpose string reads more like placeholder text than informative description. It makes the app look clumsy and arouse suspicion. (The capitalization of the words* Travel *and* Payment *also seems random and reinforces the impression of unprofessionalism.) Moreover, the explanation doesn’t communicate to users the benefit of allowing access. For example, while scanning travel documents is a feature, an actual benefit could be that if users scan their passport, they won’t have to enter the details in manually.*

**Write requests that focus on user benefits.** Don’t just mention the features that depend on the permission; frame your requests in terms of what those features will do for your users. This information makes it easy for users to understand the request and to accept it.

Example:

**OK:***Skyscanner would like to access your location for flight-search personalization.*

**Better:***Skyscanner would like to access your location, so that you can quickly select departure airports near you.*

Example:

**OK:***Allow Snapchat access to your camera for taking photos.*

**Better:***Allow Snapchat access to your camera, so you can take snaps in the app to share with friends.*

Far too many Android apps neglect to provide explanations for the permission request and user benefits (while their iOS versions provide perfectly good explanations). **UX teams designing for Android should consider providing additional screens to communicate the purpose before the permission request appears**; otherwise, consent cannot be seen to be properly informed.

![A gif of a productivity app on Android. The screen in the app says "Never forget to call back. Any.do can remind you to call back. Never let an important call slip away. If the user selects the 'allow' button two Android permission requests appear asking for access to contacts and for the app to manage and make phone calls.](https://media.nngroup.com/media/editor/2019/03/20/anydo.gif)

*Any.do, an Android productivity app, provides an intro page upon launch, explaining the benefits of allowing access to the user’s contacts: get reminded to return phone calls. When users select* Allow *, the usual Android permission request is triggered. Without this initial screen, the permission request alone would be unexpected and potentially alarming for Android users, as users could wonder why a productivity app would require access to their contacts. However, it may not be appropriate to introduce the feature immediately after the app was launched for the first time, as I’ll discuss later.*

### Writing Suggestions:

- Write in the **active voice**.
- Use **plain language** that your users understand.
- Explain why the app requires access and convey the user benefits. Generally, a good content formula for permission requests goes like this: [app]*would like to access your* [resource] *so that you can* [benefit/task].
- **Avoid vague phrases** such as *to offer a better user experience* when explaining why the app requires access. (Users are highly skeptical of vague promises and often suspect that they cover nefarious schemes.)
- **For Android,** design additional screens for unexpected requests, so that the rationale and benefits can be communicated to users before the permission-request dialog appears. (And if you’re Google, redesign the permission API, to make it easy to include an explanation right when the request is made.)
- **Test your permission requests** with users to find out whether they understand the text.

## 2. The Timing of the Permission Request

The timing of permission requests is important, as it can result in users finding the request either normal or alarming.

There are two types of permission request: context-related and system-initiated. **Context-related permission requests are less likely to cause surprise**: users select an icon in the app (such as a camera or microphone symbol) or tap inside an address field (for location), and the system reacts with a permission request. The context of the users’ action and timeliness of the modal dialog help them to reason about the meaning of the request.

Conversely, **system-initiated requests**, which are programmed to request a permission at a specific time,**often require additional context**. An example of a system-initiated request is when the user opens an app for the first time and is greeted with a dialog asking for access to the current location. Because system-initiated requests can be programed to appear at any time, there’s more potential for them to occur at moments that are inopportune for the user.

![An image of a permission request from Google Maps in iOS. The permission message appears after the user has selected their destination and is about to start navigating. The permission request reads: Google Maps would like to access Apple Music, your music and video activity, and your media library.](https://media.nngroup.com/media/editor/2019/03/20/googlemaps.PNG)

*Google Maps for iOS: An unexpected system-initiated request to access the media library appears when the user is about to tap* Start *to navigate to a local hotel. The user is left wondering how Google Maps would use that permission (the answer is: to display the details of the currently playing song within the app). While this feature could enhance the user experience, it is brought up at the wrong time because users are likely to be task-focused, and possibly in a hurry when they start navigation. A better option would be to advertise new features when users open the app and then allow them to discover these new features when it is convenient.*

![A gif of a navigation app called Waze on Android. A microphone button is selected and a permission request appears reading: Allow Waze to record audio?](https://media.nngroup.com/media/editor/2019/03/20/waze_audio.gif)

*Waze for Android: When users press the red microphone button, the record-audio permission request appears. This is an example of a helpful and expected context-related permission request.*

![A gif showing 5 system-initiated requests from Viber on Android.](https://media.nngroup.com/media/editor/2019/03/20/ezgifcom-optimize.gif)

*When users install Viber (a messaging app) on an Android device, they are greeted with 5 system-initiated permission requests in a row, inducing a serious case of request fatigue. These are to access the user’s contacts, photos, camera, microphone, and location. While the user can guess why Viber might need access to contacts, other requests are less intuitive. The timing of some of these requests could be improved: for example, the permission to access the photo library and camera should be requested when users try to upload a picture from their phone or take a picture in the app, respectively.*

Interruptions at the start can be overwhelming and confusing. First impressions are formed when users install an app. Asking for all permissions (like Viber does on Android) is like [asking for a donation without telling people](https://www.nngroup.com/articles/donation-usability/) anything about the charity. A better modus operandi is to ask only for core permissions (essential for the core functionality of the app) upon the first launch and ask for further permissions only when they are needed to offer the user additional functionality.

### Suggestions for timing permission requests:

- Don’t show all permission requests at once. Avoid asking for all permissions upfront, when the app is first installed.
- Whenever possible, initiate a permission request when the user selects a feature that requires that permission. This approach gives the request important context and the user a feeling of control, plus it’s more likely for users to understand why the app needs it and agree to it.
- When users are completing a task in your app, don’t interrupt them with an unrelated system-initiated permission request, because [unsolicited modal dialogs irritate users](https://www.nngroup.com/articles/most-hated-advertising-techniques/) and are quickly dismissed.
- Provide value to the user before asking for noncritical permissions.

## 3. Decision Reversal for Permissions

Sometimes users initially deny access to a resource and later want to reverse their decision. For example, they may deny access to the phone contacts for a messaging app, but later realize that adding contacts manually is too arduous and may wish to reverse their initial decision.

Rather than reporting an error when users try to access a feature that relies on a denied permission, **clearly explain why that functionality can’t be used, and make it easy for them to grant access**. Sometimes users don’t make the mental connection between a permission and a functionality, so providing this messaging helps users to form the right mental model of the app’s workings.

Secondly, **provide a link to** where they can toggle the permission on, in order to make sure that users will not get lost in their permission settings.

![An image of a screen in the Venmo app in iOS when the app doesn't have permission to access the camera. The text reads: No camera access. To scan codes and take pictures for your profile, allow us to use your camera in Settings > Privacy > Camera. Open Settings.](https://media.nngroup.com/media/editor/2019/03/20/venmo.PNG)

*Venmo for iOS, a cash app for sending and receiving money from friends, shows this screen to users after they’ve declined the permission to access their camera. The text communicates the existing state of access and provides a link to the exact place in the device’s settings where the user can toggle the permission on from off. The only thing that could be improved here is making the* Open Settings *link look more like a link , as it could be easily mistaken for simply text.*

### Tips for designing for decision reversal:

- When users try to access functionality in the app that requires a permission they initially declined, clearly describe the reason the functionality is not available.
- Provide a link to the exact place in the device’s settings where they can reverse their decision.

## Avoid Dark Patterns

Since the implementation of the GDPR requiring unambiguous consent for EU citizens, some app developers have begun implementing [dark patterns](https://darkpatterns.org/) to nudge users to agree to their permission requests. In some cases, app developers try to couch a permission request as an informational dialogue (like in the WeChat example below). These requests can often pop up at times when the user is in the flow of a task. Sometimes designers make it deliberately difficult for users to deny the request. While these unscrupulous tactics may be successful in getting more users to accept permission requests, they are ethically and legally dubious. Moreover, they **erode trust** and **may impact**[user loyalty over time](https://www.nngroup.com/articles/communicating-trustworthiness/).

![A permission request shown in WeChat on iOS. The permission request reads: 'Find WeChat Friends. WeChat will upload your address book to its server to help you find out which mobile contacts are using WeChat. Your uploaded data is only used for matching contacts and won't be saved for other purposes'. The options for the user is to say 'OK' or 'Learn more'. 'OK' is labelled as 'Recommended'.](https://media.nngroup.com/media/editor/2019/03/20/wechat.PNG)

*This notification from WeChat uses a dark pattern to disguise a permission request as an informational dialogue. The* OK *button is labeled* Recommended *, and there’s no option to directly decline the request. If users want to deny access to contacts, they have to pay a greater interaction cost because they’ll need to select* Learn more *, where yet more dark patterns make it difficult to find out how to decline the request.*

**Avoid using dark patterns.** Give your users enough information to make their own choice. Respect their decision. Remember, you can always support users to reverse their decision later.

## Summary

App permission requests allow users to remain in control of their data. Users perform a cost–benefit analysis when deciding whether to accept a permission request. It’s important that designers think about how to communicate the benefits and when to make the request, so that users aren’t irritated or alarmed, and feel in control. Lastly, designers should avoid dark patterns, and instead present users with fair options and the ability to reverse their decision later.

For more on mobile notifications and related topics read our report [UX for Mobile Applications and Websites](https://www.nngroup.com/reports/mobile-website-and-application-usability/).

### References:

Tan, J., Nguyen, K., Theodorides, M., Negrón-Arroyo, H., Thompson, C., Egelman, S. and Wagner, D. (2014). [The effect of developer-specified explanations for permission requests on smartphone user behavior](https://doi.org/10.1145/2556288.2557400). In *Proceedings of the 32nd annual ACM conference on Human factors in computing systems - CHI ’14* (Toronto, Ontario, Canada, 2014), 91–100.

Android developer guidance: [https://material.io/design/platform-guidance/android-permissions.html](https://material.io/design/platform-guidance/android-permissions.html)

iOS developer guidance: [https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/requesting-permission/](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/requesting-permission/)
