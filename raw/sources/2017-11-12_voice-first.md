---
title: "Voice First: The Future of Interaction?"
date: "2017-11-12"
url: "https://www.nngroup.com/articles/voice-first/"
author: "Kathryn Whitenton"
topics: [ai, human-computer-interaction]
type: article
---

Voice and screen-based interaction are converging, from two directions:

- **Screen-first** devices like smartphones, tablets and televisions are being enhanced with the addition of voice control systems.
- **Voice-first** devices like smart speakers are being enhanced with screens, such as the Echo Show (no doubt soon to be followed by similar offerings from other brands).

We should not expect speech to completely replace written communication, despite common science-fiction portrayals. But it’s clear that standard human–machine communication is rapidly expanding to encompass both written and spoken interaction. Currently voice interaction is primarily within the realm of personal and home use. But as people become accustomed to it, they will come to expect it in business and commercial contexts as well. (For anyone who’s ever struggled with a conference-room projector or phone-system menu, imagine if you could just say ‘Show my screen’ or ‘Start the meeting.’)

Truly integrated voice-plus-screen systems can transform user experience for a huge range of tasks, by capitalizing on the strengths of each interaction style:

- Voice is an **efficient input modality**: it allows users to give commands to the system quickly, on their own terms. [Hands-free control](https://www.nngroup.com/articles/voice-interfaces-assessing-the-potential/) lets users multitask, and effective natural language processing bypasses the need for complex navigation menus, at least for familiar tasks and known commands.
- A screen is **an efficient output modality**: it allows systems to display a large amount of information at the same time and thus [reduce the burden on users’ memory](https://www.nngroup.com/articles/minimize-cognitive-load/). Visual scanning is faster than the [sequential information access](https://www.nngroup.com/articles/direct-vs-sequential-access/) enforced by voice output. It can also efficiently convey system status and bridge the [Gulf of Execution](https://www.nngroup.com/articles/audio-signifiers-voice-interaction/) by providing visual signifiers to suggest possible commands.

Logically, combining these into a single system sounds like an obvious win. But the design challenges of integrating two very different interaction modes have thus far prevented any single system from fully realizing the benefits of both voice and screen.

## In This Article:

- [Limitations of Screen-First Interaction](#toc-limitations-of-screen-first-interaction-1)
- [Voice-Only Interaction](#toc-voice-only-interaction-2)
- [Voice-First Interaction](#toc-voice-first-interaction-3)
- [Integrating Voice and Screen Output From the Ground Up](#toc-integrating-voice-and-screen-output-from-the-ground-up-4)
- [Is Voice-First a Long Term Solution?](#toc-is-voice-first-a-long-term-solution-5)

## Limitations of Screen-First Interaction

Until recently, most devices that combined screen and voice control were screen-first: smartphones with a voice-control system added to the preexisting graphical user interface in the form of a voice agent, like Siri or Google Assistant.

These screen-first systems exhibit impressive speech recognition and language processing, but the overall user experience remains severely fragmented due to the fundamental division between the voice agent and the touchscreen application functionality.

### Missing Functionality

Too often, the voice agent can initiate only the first step of a task, and any subsequent steps require the user to shift to a touch interaction style. For example, Siri will execute a web-search query or open the Apple News application in response to a voice command, but the user must then tap the screen to select a search result or access a news story. Google Assistant also requires screen input to move beyond the first step of many searches.

![Examples of voice search results from Siri and Google Assistant](https://media.nngroup.com/media/editor/2017/11/03/screen-first-voice-search-results-siri-and-google.png)

*Siri and Google Assistant both execute a voice command to search for a recipe, but then require users to touch the screen in order to select a result and complete the task.*

### Poor Use of Screen Space in ‘Voice Mode’

Even for those tasks with some support for multistep voice input, Siri uses a screen design that is completely different from the GUI version and often makes poor use of the available screen space. For example, Siri can read text messages and send replies. But when reading a text message aloud, the entire screen is dark and only the name of the message sender appears – not the actual contents of the message. Similarly, when replying, the screen does not display the text of the message you are responding to as it would in the GUI messaging application. This limitation unnecessarily restricts the information available to the user. In fact, the voice mode should be able to display even more of the message history, because there’s no need to display a keyboard.

![Examples of the screen display shown by Siri while messaging in voice mode](https://media.nngroup.com/media/editor/2017/11/03/siri-voice-mode-screen-display.png)

*While Siri reads a text message aloud (left), the message contents are not visible on the screen; while dictating a text message reply (right), you can’t see the message you are replying to.*

### Missing Affordances

Siri’s minimalist voice-agent screen also omits most of the visual affordances that have been carefully incorporated into the graphical user interface, like letting people know they have the ability to edit a text message before sending it. (Google Assistant has far more affordances, with suggested commands displayed immediately below each task outcome, and a feed which lets you revisit previous tasks.)

## Voice-Only Interaction

A radically different approach to voice interaction appeared with the introduction of smart speakers like Amazon’s Echo and Google Home. These devices offer no visual display at all, and everyday usage relies on audio for both input and output (with the exception of a few flashing lights). Due to big improvements in voice-recognition accuracy over moderate distances, smart speakers allow true hands-free operation, which in turn [increase flexibility and efficiency](https://www.nngroup.com/articles/voice-interaction-ux/) enough to make them desirable even to users who already own a voice-enabled smartphone.

But the lack of a screen is a huge limitation for these speakers. Only [auditory signals](https://www.nngroup.com/articles/audio-signifiers-voice-interaction/) can be used to cue users about possible commands, and reading output aloud becomes tedious for all but the simplest of tasks. Setting a timer with a voice command while cooking is great, but being forced to ask how much time is left is not. Getting the weather forecast becomes a memory test for the user, who must try to listen and absorb a series of facts for the whole week, instead of taking them in at-a-glance from a screen.

## Voice-First Interaction

The success of smart speakers combined with the frustrating limitations of voice-only output has now spawned a new product: the Echo Show, which adds a display screen to the basic Echo smart speaker. This screen significantly expands the functionality of the original Echo, making tasks like checking the weather and monitoring timers much easier. But compared to screen-first devices with a full GUI (such as Amazon’s own Fire 7 tablet, at a much lower price point), Echo Show is far less capable of performing basic functions that have long been available on smartphones and tablets. For example, it can’t (yet) even browse websites, show reviews, or display the contents of your Amazon shopping cart.

What Echo Show *does* offer is an fundamentally different interaction style which can be described as “voice-first,” and which relies almost exclusively on speech input, rather than relegating speech to a secondary, limited mode.

**Voice-first Interaction** refers to a system which primarily accepts user input via voice commands, and may augment audio output with a tightly integrated screen display.

Although technically a touchscreen, Echo Show only rarely provides buttons or menus. (A touch keyboard is grudgingly displayed to let you enter a wireless-network password, but then swiftly whisked away, never to be seen again.) Instead of encouraging users to tap or swipe, Echo Show often displays suggested verbal commands, such as *Try “Alexa, scroll right.”*

![Echo Show interface](https://media.nngroup.com/media/editor/2017/11/03/alexa-scroll-right.JPG)

*Whenever possible, Echo Show encourages users to stick to voice input instead of touching the screen, by suggesting verbal commands like* Try “Alexa, scroll right”*instead of typical touchscreen signifiers like buttons.*

## Integrating Voice and Screen Output From the Ground Up

Essentially, voice-first represents a new approach to the problem of integrating voice commands into an existing graphical user interface. First, the GUI is completely eliminated (as exemplified by the original voice-only Echo); then a screen is re-introduced and visual information is gradually incorporated as part of a holistic system.

Voice interaction between people and personal devices represents a new and fundamentally different type of communication — analogous to a foreign language for both users and designers. Just as foreign languages are most easily learned through immersion, the invention and adoption of voice interaction is likely to be greatly enhanced by an environment the focuses exclusively on this modality.

Some interesting examples of the innovation driven by the voice-first approach are already evident in Echo Show’s interface:

- **Sequential numbering of search results**, which was a convention common in the early days of web search, but long since abandoned as unnecessary in a visual list. On a voice-first device, the numbers serve the important function of providing unique and efficient verbal ‘handles’ which let users efficiently select items.

- **Randomly displayed suggested commands**, such as *Try “Alexa, play Al Green”* or *Try “Alexa, what’s your favorite word?”* This technique is similar to methods used by both Siri (*Things you can ask me)* and Google Assistant (*Explore),* but differs in that these tips are displayed not just in a dedicated educational area, but instead at the bottom of the home screen, various search-results screens, and the music-player screen. (This ambient education mechanism can definitely entice new users to spontaneously engage with the device. But the random contents means the tips are often uninteresting, and annoying to experienced users because they cannot be turned off.)
- **Immersive displays of rich, interactive content**, which are normal on traditional web and mobile GUIs but not on previous screen-first voice interfaces. For example, recipe results on Echo Show include detailed screens showing ingredients, directions, and a demonstration video — all accessible via voice commands.

![Echo Show provides an immersive, interactive rich screen display in response to voice commands](https://media.nngroup.com/media/editor/2017/11/03/echo-show-immersive-screen-detail.JPG)

*As a voice-first system, Echo Show does not simply provide a link to a recipe in a GUI application, but instead includes voice-navigable immersive screens with detailed ingredients, directions, and a demonstration video.*

## Is Voice-First a Long Term Solution?

The elimination of traditional GUI elements such as menus and buttons may be a necessary stepping stone for learning about voice-interaction interfaces. But just like the ‘mobile-first’ movement (which generated bad ideas, like [hiding global navigation](https://www.nngroup.com/articles/killing-global-navigation-one-trend-avoid/) even when using a big screen), the concept of voice-first is not a panacea.

Ultimately, deliberately handicapping the functionality of a screen in the name of ‘pure’ voice interaction unnecessarily limits the usefulness of the device and increases users’ cognitive load and frustration. A visual display is inherently a more efficient way to let people access a large amount of information than audio-only output.

For example, the voice-first approach means that despite its name, Echo Show it won’t actually ‘show’ you whatever you request: it’s impossible to see basic device information such as a menu of all installed applications, or ‘skills’ (as Amazon names them).

Alexa currently has a library of over 15,000 skills, many of which can only be accessed by speaking the name of the skill. Even if users only have a few dozen skills installed, how can they be [expected to remember](https://www.nngroup.com/articles/recognition-and-recall/) the exact name of every skill they’ve installed? Personalized suggestions and natural-language processing can reduce the need to consult an application menu — but unless voice agents become mind readers, they can’t possibly suggest everything users might be interested in at any given moment.

Voice-first design may significantly improve voice interaction, but in the long term, arbitrarily prohibiting visual menus for the sake of voice-first interaction would be like going into a fight with one hand tied behind your back. And with the looming complexity of holistic, intelligent voice and screen interfaces, UX designers need all the tools they can get.
