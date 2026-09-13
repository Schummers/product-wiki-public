---
title: "13 QR-Code Usability Guidelines"
date: "2024-02-09"
url: "https://www.nngroup.com/articles/qr-code-guidelines/"
author: "Tanner Kohler"
topics: [mobile-and-tablet-design]
type: article
---

QR codes provide a [seamless](https://www.nngroup.com/articles/seamless-cross-channel/) transition from the physical world to digital spaces or across digital channels. QR codes have a lower [interaction cost](https://www.nngroup.com/articles/interaction-cost-definition/) than typing in a URL, but convenience does not guarantee that users will take action just because a QR code is presented to them.

## In This Article:

- [Uses For QR Codes](#toc-uses-for-qr-codes-1)
- [Guidelines for QR-Code Usability](#toc-guidelines-for-qr-code-usability-2)
- [The Dangers of QR Codes and How to Stay Safe](#toc-the-dangers-of-qr-codes-and-how-to-stay-safe-3)
- [Conclusion](#toc-conclusion-4)

## Uses For QR Codes

1. **Progressive disclosure.** QR codes can provide access to additional information that does not fit in limited spaces or is not relevant to all users. They can be like *Learn more links* for the physical world. For example, a small sign promoting a local initiative can’t fit much information on it, but more details can be accessed online by scanning a QR code in the corner of the sign. Very few users will take time to scan such codes because they lack interest or the interaction cost is too high, but the code allows the designer to design a simpler sign. The number of scans for this code can reveal meaningful insights about interest in the initiative.
2. **Transitions across different interaction channels.** Most often, these transitions are from the physical to the digital space. For example, a parking meter presents a QR code that allows users to download the application for making a payment. In other cases, QR codes can support seamless transitions across digital devices like smartphones, computers, and TVs. For example, [passkeys](https://www.nngroup.com/articles/passwordless-accounts/) and other forms of authentication. These codes are for convenience, not awareness, so the number of scans the code receives is far less meaningful than the usability of the workflow the code affords. Use [qualitative usability testing](https://www.nngroup.com/articles/qual-usability-testing-study-guide/) to evaluate how well these codes perform.
3. **Reducing print needs.** QR codes provide a way to move printed information to a digital space. This offers cleanliness, convenience, and benefits for the environment. For example, providing a QR code that links to a restaurant menu reduces the spread of germs and the need for printing menus while allowing as many people to access it as desired.

## Guidelines for QR-Code Usability

### 1. Tell Users What a QR Code Does and Where It Came From

Unlike [links with labels](https://www.nngroup.com/articles/better-link-labels/) or raw URLs that contain destination information **, QR codes have no**[information scent](https://www.nngroup.com/articles/information-scent/) by themselves. They tell users nothing about where they lead or what will happen when they are scanned. Designers must provide enough contextual information about the code to convince the user to scan it. Without contextual information, QR codes are not trustworthy or enticing.

![An unlabeled QR code on the bottom of a YETI mug](https://media.nngroup.com/media/editor/2024/02/02/img_3312-2.jpg)

❌*The QR code on the bottom of this Yeti mug does not indicate where it leads, making it both suspicious and unenticing.*

Additional contextual information might include a short URL indicating where the code leads, a label, or styling with company branding. However, a logo by itself is not sufficient contextual information.

Many users won’t be willing to read a paragraph to find out what a code does; instead, they will ignore it — especially if it provides only additional information. Information telling users what will happen if they scan the code should be as clear and visually prominent as the code itself.

![A paragraph of text with an unlabeled QR code next to it.](https://media.nngroup.com/media/editor/2024/02/02/img_2947-1.jpg)

❌ *Users must read the entire paragraph of text on the back of this National Geographic magazine to find out what the QR code does in the last sentence.*

![A street sign inviting pedestrians to donate money to a charity by scanning a QR code.](https://media.nngroup.com/media/editor/2024/02/02/img_3131.jpg)

✅ *This street sign makes it clear that scanning the QR code leads to a place where the user can donate locally to United Housing Connections.*

QR codes are not effective at promoting a website because users may not notice or remember the URL of the website associated with the code. If raising awareness of the website is important, show the URL next to the code. Displaying the URL alongside the code is also important if some users will want to visit the site on devices without cameras, such as laptops.

Other kinds of codes (like Apple’s **app-clip codes**) require the same level of contextual information, if not more. Users will be less familiar with new kinds of scannable codes than they are with traditional QR codes.

![A street sign with a traditional QR code and an Apple App Clip that allow zoo guests to pay for parking.](https://media.nngroup.com/media/editor/2024/02/02/img_2600-1.jpg)

✅ *All types of scannable codes require contextual information.*

### 2. Clarify Which Devices and Applications Can Scan Codes (When Necessary)

If QR codes must be scanned within a certain application or by a certain device, this information must also be presented alongside the code. For example, in China, QR codes on some restaurant tables must be scanned with a specific app — such as [WeChat](https://www.nngroup.com/articles/wechat-integrated-ux/) or Alipay — while others can be scanned with either. Clearly indicating which applications (or devices) can scan the code prevents confusion.

![A passkey QR code displayed on a desktop computer.](https://media.nngroup.com/media/editor/2024/02/02/passkey.png)

✅ *This contextual information around this passkey QR code makes it clear that it must be scanned by the device on which the user created the passkey.*

### 3. QR Codes Should Lead to Mobile-Friendly Pages

You can assume that users scanning a QR code will visit the associated site on a mobile device. QR codes should lead to [mobile-dedicated](https://www.nngroup.com/articles/mobile-vs-responsive/) or [responsive](https://www.nngroup.com/articles/responsive-web-design-definition/) sites.

![A hiring website accessed from a QR code that displays poorly on mobile.](https://media.nngroup.com/media/editor/2024/02/02/john.png)

❌ *The QR code for Papa Johns job applications linked to a website that rendered poorly on mobile.*

### 4. Deep-Link QR Codes Directly to Relevant Pages or Actions

Users expect a QR code to link to information directly related to the context of the code rather than to a generic homepage. It's annoying to scan a code that appears to offer a certain action or piece of information and end up on the website's homepage. This is like giving users a link with a high [information scent](https://www.nngroup.com/articles/information-scent/), but not taking them where the link [promises to go](https://www.nngroup.com/articles/link-promise/).

![A QR code in the tongue of a Nike shoe which leads to the homepage of the Nike website.](https://media.nngroup.com/media/editor/2024/02/02/nike-3.png)

❌ *The QR code on the tongue of this Nike shoe (left) leads to the generic homepage of the website (right) rather than to a page related to those specific shoes.*

**QR codes often afford an easy way to download mobile applications.** QR codes used for that purpose should provide direct access to Apple’s App Store or Google’s Play Store.

![A KFC flier with a QR code alongside the associated app download options for Apple and Android which display when the code is scanned.](https://media.nngroup.com/media/editor/2024/02/02/kfc-2.png)

✅ *The QR code for downloading the KFC app on the flier (top) takes users directly to the KFC app in Apple’s App Store (bottom left) or Google’s Play Store (bottom right), depending on the operating system of the device that scans it.*

If the QR code [deep-links](https://www.nngroup.com/articles/deep-linking-is-good-linking/) to something within the application, users who do not already have it downloaded should be immediately prompted to do so (or offered the equivalent information on a mobile-friendly page).

![If users scan the QR code on the Burger King flier, they are taken to deals in the app if it's downloaded or dropped on an unrelated page if it isn't.](https://media.nngroup.com/media/editor/2024/02/02/bk2.png)

❌ *The QR code on this Burger King flier (top) connects users with deals in the app, but only if they already have it downloaded (bottom left). If they don’t, it drops them on an unrelated page on the company’s website (bottom right).*

### 5. Use Direct Links Rather than QR Codes When Displaying and Accessing Information on the Same Mobile Device

Displaying a QR code on a mobile device is most valuable when it is intended to be presented by the user to someone else for scanning (such as to another user or to a scanner at a physical location).

Digital boarding passes or account connection codes within mobile applications are a great example of the types of QR codes that should be displayed on mobile devices. Neither of these codes are intended to be scanned by the users themselves.

![A Delta boarding pass code and a Venmo account sharing code.](https://media.nngroup.com/media/editor/2024/02/02/group-74.png)

✅ *A flight boarding pass code (left) is presented to scanning machines at the airport, and a Venmo account code (right) is presented to other users for scanning.*

However, if the information is intended to be accessed on the same mobile device displaying it, it will be more easily accessed through a direct link than through a QR code because **a user won’t be able to easily scan a QR code displayed on their own device.** (They may be able to take a screenshot of the QR code and then long-press it in the Photos app, but many users will not know that.)

![An IKEA email with a QR code and a bar code in a digital wallet.](https://media.nngroup.com/media/editor/2024/02/02/ikea.png)

❌ *The email from IKEA containing this QR code (left) suggested adding it to a digital wallet on a mobile device. However, the scannable code added to the digital wallet was not a QR code (right), implying that the QR code in the email was meant to be scanned by the user.*

In cases where direct links are blocked or prohibited, embedded QR codes can provide a workaround for accessing related content. For example, the popular Chinese superapp WeChat does not support links in messages. However, users commonly place QR codes in their posts so that others can access articles and images through a long press.

![A QR code in a WeChat message and the "Scan QR Code" option that becomes available after long-pressing the code.](https://media.nngroup.com/media/editor/2024/02/02/wechat.png)

*WeChat users can long-press QR codes presented within the application to visit the associated sites.*

However, **in most cases, a direct link is superior to a QR code on mobile devices**. This is why mobile-dedicated sites and mobile applications should **contain QR codes only if they are intended to be scanned by other devices** (watch out for codes ported over from sites designed primarily for desktop).

### 6. Do Not Invert QR-Code Colors

QR codes should be presented in [light mode](https://www.nngroup.com/articles/dark-mode-users-issues/) with a dark foreground and a light background. Most cameras on updated phones and tablets can scan QR codes with inverted colors, but not all scanning technology used in physical locations can do so. Dark colors absorb more light, creating clearer edges for scanning technologies to detect the code's unique pattern. This can be particularly important when codes are likely to be scanned in extreme lighting conditions, such as in dark rooms or direct sunlight.

### 7. Use QR Codes for Authentication Between Devices

Allowing devices to [collaborate](https://www.nngroup.com/articles/omnichannel-collaboration/) in ways that support each other is fundamental to good [omnichannel user experiences](https://www.nngroup.com/articles/customer-journeys-omnichannel/). QR codes provide a powerful way for users who are already signed into an account on a mobile device to easily authenticate on another device, such as a smart TV, a computer, or even another smartphone. While this form of authentication presents some risks, it is much more convenient than trying to recall and manually enter a password.

![A QR code displayed on a desktop computer that can be scanned with a mobile device to authenticate.](https://media.nngroup.com/media/editor/2024/02/02/screen-shot-2023-11-14-at-91816-pm.png)

✅ *WhatsApp users can sign in on the computer by scanning the QR code with a mobile device that is already logged into their account.*

![A smart TV displaying a QR code which enables users to authenticate with a mobile device.](https://media.nngroup.com/media/editor/2024/02/02/picture5.png)

✅ *Many smart TV applications allow users to scan a QR code to either automatically authenticate because they are already signed in on the mobile device or go directly to a website that will allow them to manually authenticate using a more convenient keyboard.*

### 8. Use QR Codes to Provide Additional Details Through Progressive Disclosure

QR codes provide an easy way to [hide additional details](https://www.nngroup.com/articles/progressive-disclosure/) that are not interesting to most people. They are particularly useful in physical products with a limited display area, such as in advertisements, signage, or product packaging. However, simply making information available does not make it interesting — only a small percentage of people will access information relegated to the digital realm.

![A QR code on a carton of cream that provides more details about the product on a mobile website when scanned.](https://media.nngroup.com/media/editor/2024/02/02/publix.png)

✅ *Many package labels use QR codes to provide more product details than can fit on the label. Most users will not be interested in these details, but those who are can easily access them.*

Avoid using generic [Learn more](https://www.nngroup.com/articles/learn-more-links/) labels for QR codes. Provide the richest contextual information you can about where the code leads.

### 9. Ensure that QR Codes Lead to Up-To-Date Information

Users who scan a QR code far in the future should still see relevant information. **Once a QR code is put out in the world (especially in physical print), it cannot be taken back**. Even if the code is relevant only for current, temporary information, such as a current ad campaign, some users might still scan it after the related information becomes irrelevant. Old codes should redirect to a relevant page that explains that the window has passed but provides easy access to current information related to the original purpose of the code.

![A flier for a past event that links to an out-dated informational webpage.](https://media.nngroup.com/media/editor/2024/02/02/italian.png)

❌ *The QR code on the flier from 2019 (left) was still linked to the same page for the 2019 event (right) when scanned in 2023.*

![A flier for a past event that links to an updated informational webpage.](https://media.nngroup.com/media/editor/2024/02/02/year.png)

✅ *The QR code on the flier from 2023 (left) is linked to an updated page for the same event in 2024 (right) when scanned after the 2023 event had passed.*

### 10. Use a Short, Memorable URL Rather than a QR Code if Users Have Less than 15 Seconds to Scan It

Users require more time than you might think to scan a QR code. They have to:

1. Notice the QR code
2. Consider where the code might lead
3. Decide to scan it
4. Retrieve their phone
5. Open the camera
6. Aim the camera
7. Focus the camera
8. Tap the link

Formal approaches to analyzing the time required for each step of this process (such as GOMS) provide varied estimates, but, as a rule of thumb, assume **users need at least 15 seconds to scan a QR code.** Many users will require even longer if they are undecided about whether it is worthwhile to scan the code, are not very dexterous, have trouble navigating mobile devices, or must dig a phone out of a pocket or purse.

QR codes are not well-suited to roadside billboards that are passed very quickly or in rotating [carousels](https://www.nngroup.com/articles/designing-effective-carousels/) (such as digital signage on large monitors) that show them only for a few seconds at a time. For quick-exposure scenarios, a short, meaningful, memorable URL will perform better because users can hold it in their [working memory](https://www.nngroup.com/articles/working-memory-external-memory/) while deciding to visit the site.

### 11. Do Not Rely Solely on QR Codes for Frequent Site Visits

QR codes cannot be remembered. Although users rarely memorize URLs, they are still more memorable than QR codes. Relying solely on QR codes for access to a site means that most users will not be able to revisit the site without the code. Many people will have trouble looking through their browsing history to access previously visited links — especially on mobile.

### 12. Place QR Codes Where Users Are Likely to Look

The Gestalt principle of [proximity](https://www.nngroup.com/articles/gestalt-proximity/) indicates that people assume things that are near each other are related. It’s tempting to put the QR code off to the side or down in the corner to place it out of the way, but moving it far from where people will look makes it less likely to be noticed and less associated with related content. Codes must be noticed to be scanned.

![A Walmart checkout kiosk with QR codes place right were shoppers must look to pay.](https://media.nngroup.com/media/editor/2024/02/02/img_3386-1.jpg)

✅ *The self-checkout kiosk at Walmart provides the QR code for digital payment on both the large monitor and the keypad — locations where users are likely to look when they are ready to pay (although the code is, unfortunately, not labeled on the keypad).*

### 13. Make Sure QR Codes Are Big Enough

Users must be close enough to QR codes to successfully scan them. While many phone cameras offer zooming capabilities, proximity is still essential. While the official minimum size for a QR code is 1 cm x 1 cm (0.4 inches x 0.4 inches), this size can be too small for reliable scanning. Aim for a minimum size of 2 cm x 2 cm (0.8 inches x 0.8 inches) for best results.

**The farther away you expect users to be while scanning the code, the bigger you should make the code.** As a rule of thumb, [for every 10 cm of distance to the code, add an extra 1 cm to the length and width of the code](https://www.fotor.com/blog/qr-code-minimum-size/).

For example, if you expect users to scan from 10 cm away, the code can be 1 cm x 1 cm; if users will likely scan from around 50 cm away, then the code should be at least 5 cm x 5 cm in size. It’s particularly important to make codes big when they will be scanned in dimly lit environments to increase visibility and scannability.

## The Dangers of QR Codes and How to Stay Safe

QR codes are convenient but still deserve caution. Individuals with malicious intent have abused QR codes in the following ways:

- **Phishing:** Codes might lead to an alternative malicious website that resembles what the users anticipated. For example, a code that seems to lead to a restaurant menu might lead to a fake website stealing information.
- **Malware:** QR codes can serve as gateways for malware, stealthily infiltrating a device with harmful software when scanned.
- **Payments:** QR codes can be manipulated to trigger unauthorized payments from mobile-payment apps. Scammers achieve this by linking the code to their own accounts, effectively siphoning funds from unsuspecting victims.
- **Tracking:** The information gleaned from QR code scans can be employed for targeted advertising or even more intrusive forms of surveillance.
- **Fake Codes:** Malicious QR codes can be strategically placed over legitimate ones in public places, such as restaurants, parking meters, or transportation hubs, opening the door to all manner of harmful actions.

**Tips for staying safe with QR codes:**

- Scan only trusted sources.
- Preview destinations before committing.
- Avoid suspicious or unexpected codes.
- Look for secure connections (HTTPS, padlock).
- Protect your device with antivirus and antimalware.
- Control automatic actions (like opening links).
- Report suspicious codes to authorities.

As designers, we will do everything we can to protect users. However, it’s also important to recognize that few users interacting with QR codes will actively consider these risks.

## Conclusion

While QR codes offer a convenient and seamless transition to mobile workflows, their effectiveness relies on thoughtful design that considers how they will be used. Add brief, clear, contextual information to each QR code. Ensure they lead to mobile-friendly destinations. Maintain awareness of potential security risks. Properly implementing these guidelines can enhance the user experience across a variety of channels.
