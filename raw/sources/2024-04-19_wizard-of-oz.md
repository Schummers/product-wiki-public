---
title: "The Wizard of Oz Method in UX"
date: "2024-04-19"
url: "https://www.nngroup.com/articles/wizard-of-oz/"
author: "Maria Rosala, Sara Paul"
topics: [prototyping, user-testing]
type: article
---

The Wizard of Oz method helps teams test designs that are powered by complex technologies at a low cost. Instead of building out the technology, designers can simulate the responses the technology might provide by having a person “play” the system's role.

## In This Article:

- [What Is the Wizard of Oz Method?](#toc-what-is-the-wizard-of-oz-method-1)
- [When to Use the Wizard of Oz Method](#toc-when-to-use-the-wizard-of-oz-method-2)
- [Benefits of Using the Wizard of Oz Method](#toc-benefits-of-using-the-wizard-of-oz-method-3)
- [How to Set up a Wizard of Oz Study](#toc-how-to-set-up-a-wizard-of-oz-study-4)
- [Do You Need to Reveal the Wizard?](#toc-do-you-need-to-reveal-the-wizard-5)
- [Origins of the Method](#toc-origins-of-the-method-6)
- [Conclusion](#toc-conclusion-7)

## What Is the Wizard of Oz Method?

> The **Wizard of Oz** method **** is a moderated research method in which a user interacts with an interface that appears to be autonomous but is (fully or partially) controlled by a human.

The Wizard of Oz method takes its name from the children’s novel “The Wonderful Wizard of Oz” by Frank Baum. In this novel, the main protagonist, Dorothy, and her companions meet a giant head that appears to be a powerful wizard, only to learn that it’s just an ordinary man pulling levers behind a curtain.

The Wizard of Oz method is used in [moderated usability tests](https://www.nngroup.com/articles/remote-usability-testing-costs/). Like in a traditional moderated usability test, a Wizard of Oz study involves a facilitator and a target user. In addition, you need someone to be “the wizard.” This person will select or create responses from the interface.

The Wizard of Oz method is similar to [testing paper prototypes](https://www.nngroup.com/videos/paper-prototyping-tutorial/) (where you might have someone play the role of the computer). However, in the Wizard of Oz method, the design can be digital, and the person generating the system response is not visible to the user.

![A usability test session showing a user with a facilitator in one room and a wizard who is controlling the prototype in a separate room.](https://media.nngroup.com/media/editor/2024/04/15/wiz-of-oz_illustration_smaller_size.jpg)

*A usability-test session using the Wizard of Oz method involves an additional person, “the wizard,” who provides some or all of the system’s responses behind the scenes.*

## When to Use the Wizard of Oz Method

The Wizard of Oz method is useful when testing new interfaces powered by complex technologies that are difficult to test meaningfully with a prototype containing static content. Such interfaces include:

- Conversational UIs, like chatbots
- Interfaces that use learning algorithms to provide recommended content
- Interfaces that look up real-time information and present the results to the user

For example, the authors have used the Wizard of Oz method in the following research projects:

- **A project to improve the support chatbot on a technology retailer’s website.** A Wizard of Oz study helped the team explore how to provide helpful personalized recommendations appropriate for the device the user used to make a support request. A designer updated a Figma prototype during the session based on the responses that study participants gave in an introductory interview.
- **A project to design a new voice assistant.** The Wizard of Oz method was used to help the team understand how users would interact with a new [voice assistant.](https://www.nngroup.com/articles/audio-signifiers-voice-interaction/) A Bluetooth speaker was placed inside a physical cardboard mockup. The user would talk to the mockup, and the voice assistant’s responses were generated through a text-to-voice application channeled through the Bluetooth speaker.
- **A project to build a government form that searched various government databases in real time** and presented users the information that was stored about them. A Wizard of Oz study helped the team learn how users perceived the retrieval of their information and how this information should be communicated. The researchers gathered the participant’s information through an initial interview in the session, and the wizard updated a live, coded prototype with what the user might see if a real database search were to be performed.

## Benefits of Using the Wizard of Oz Method

The Wizard-of-Oz method lowers investment risk into complex, costly technologies (such as generative AI): it provides early insights into their desirability, utility, and usability before companies spend money building them.

The Wizard of Oz method is often used when developing [MVPs (Minimum Viable Products)](https://www.nngroup.com/articles/agile-glossary/#MVP). One of the most famous examples of an MVP that used the Wizard of Oz method comes from Zappos, the first online shoe retailer. Before investing money in warehouses, inventory, and service automation, founder Nick Swinmurn tested the company’s value proposition by fulfilling orders himself. When orders were placed on his website, Swinmurn would go to a local shoe store, buy the shoes, and mail them to the customer.

## How to Set up a Wizard of Oz Study

There are several moving parts to running a successful Wizard of Oz study. Follow these 5 steps to get your study off the ground.

### Step 1: Create the Prototype

You will need a prototype of the new design for the user to interact with. Depending on what you’re testing, this might be:

- A prototype in some design software (like Figma)
- A coded prototype
- An existing technology as a proxy for the new functionality (e.g., an existing messaging platform to simulate a new chatbot)

If you’ll be using design software (like Figma or ProtoPie), think about how the wizard can quickly make updates to the prototype. For example, you could create components for any elements in your prototype that need to be updated in the session. This removes the need for the wizard to hunt for specific areas of the design to update.

(If you’re using Figma, the [multi-edit variant feature](https://www.youtube.com/watch?v=5tucsH2lUSQ) allows you to update instances of the same UI element across a component set.)

*When using Figma's multi-edit variant feature, the same element can be updated simultaneously across component variations when the wizard makes a change to one of them.*

### Step 2: Decide What Responses the Wizard Will Provide

- Closed method: The wizard can choose from a set list of responses
- Open method: The wizard will create new responses in the session.
- Hybrid method: The wizard can choose from a short list or craft new responses as needed.

*A wizard can either choose system responses from a set list, create new responses in the moment, or do both during a session.*

The closed method suits situations where there are only a few possible responses the system could give.

The open method is better suited to interfaces that provide fluid user interactions (like conversational UIs); for these types of interfaces, it may be difficult to predict and provide preset responses.

The hybrid method offers the most flexibility; some responses are predetermined, but if one doesn’t fit, a new response can be created.

#### Pros and Cons of Each Response Method

Closed | ✅ | The wizard does not need to create a response on the spot. | ✅ | Responses are | easy to analyze since there’s less across tests. | ⚠️ | Choosing a response can take time if there are many. | ⚠️ | There might not be responses that fit the situation. | Hybrid | ✅ | The wizard can select a response or create a new one. | ⚠️ | It can be challenging to decide whether to use an existing response or create a new one. | Open | ✅ | The wizard doesn’t need to search through existing responses. | ✅ | The wizard can keep the test running if the user says or does something unexpected. | ⚠️ | Crafting new responses could be effortful and take time. | ⚠️ | If there is a lot of variation in responses across tests, it can be hard to evaluate the interface’s performance.

**Involve engineers in planning what the system responses should be.** Engineers can identify what responses are feasible, given their knowledge of the technology’s capabilities and constraints.

### Step 3: Create a Study Protocol

A study protocol is a detailed outline of the study goals and how the study should be conducted. The study protocol will help the wizard and the facilitator to understand how to act in the session.

In addition to all the usual elements found in a [test plan](https://www.nngroup.com/articles/pm-research-plan/) (like the tasks you would give the user), the study protocol for a Wizard of Oz study should include:

- **An overview of the roles,** including who will facilitate the session and who will be the wizard
- The **questions** that the facilitator will ask the user at the beginning of the session and that could inform the wizard’s responses during the session (if relevant)
- The **elements of the design** that will be controlled by the wizard and how they will be controlled (e.g., decision trees, step-by-step instructions, or screenshots for the wizard to consult or follow)
- The **responses** the wizard could choose from, if opting for the closed or hybrid method (.e.g., *Loading… please wait* when the wizard needs more time or *Under construction* if the user interacts with the system in an unexpected way)
- Any **guidelines** for how the wizard should respond if they improvise new system responses during the session (e.g., tone-of-voice recommendations if the wizard is pretending to be a chatbot)

### Step 4: Choose and Prepare the Wizard

The wizard should be familiar with the:

- **Product concept and design:** The wizard should understand what the product is intended to do and how it would work. Ideally, they’ll also be aware of any technological constraints, so they can avoid providing system responses that are not feasible.
- **Responses they should give:** If you are conducting a closed or hybrid test, the wizard may have helped create the responses.
- **Prototyping software or code** if the wizard will need to update elements in a prototype.

In many cases, a designer or developer may need to play the wizard. Spend some time preparing the wizard before the study so the sessions run smoothly. This might involve running through the study protocol with the wizard, giving the wizard practice on responding or updating the prototype, and even inviting the wizard to participate in a pilot test (see step 5).

### Step 5: Pilot the Study

Since there are many moving parts, [piloting your study](https://www.nngroup.com/articles/pilot-testing/) ensures everything works as intended and that the wizard can quickly provide responses. You can pilot the test with a friend, colleague, or a real user. Piloting gives your wizard some practice before the real sessions and avoids wasting precious time in the session resolving unexpected technical issues.

As part of your pilot, you may realize that new responses are needed that you hadn’t anticipated. Such insights allow you to refine your protocol before the study begins.

## Do You Need to Reveal the Wizard?

The presence of the wizard is not usually revealed to the participant to ensure that realistic behavior is collected during the session. However, sometimes participants guess that a person is providing a response, especially if the design is low fidelity or the participant has a lot of technological knowledge. In this case, the method becomes closer to a roleplay.

Don’t worry if participants guess or ask if the responses are human-generated. Remind them to behave as they would if they were interacting with a real system.

In user-research sessions that involve [deception](https://www.nngroup.com/articles/ethical-dilemmas/), a debrief at the end of the session is needed to ensure that participants learn accurate information about the study and can decide whether they want to withdraw.

Unless it could harm the participant to be unaware of this information, you don’t have to disclose that a human produced the system response.

## Origins of the Method

The Wizard of Oz method was first documented and used in 1973 by Don Norman and Allen Munro to test an automated airport computer-terminal travel assistant. The name for this method was coined in 1983 by researcher Jeff Kelley, in his dissertation on natural-language interfaces at Johns Hopkins University. These foundational studies explored user interactions with natural-language interfaces when this technology was early in its development.

## Conclusion

A Wizard of Oz study offers early insights into complex and highly interactive interfaces that might be costly to experiment with and build. Not all usability studies need to use the Wizard of Oz method. Consider your research goals and what you need to learn. In many cases, a prototype with static content will be more than sufficient.

If you need to learn how users react or engage with systems that provide personalized, real-time recommendations or utilize natural-language models, then the Wizard of Oz method can provide insights into how to design these systems most effectively. When running a Wizard of Oz study, preparation and planning are key. Make a plan, involve engineers, and pilot your study for the best results.
