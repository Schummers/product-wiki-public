---
title: "Tree Testing:  Fast, Iterative Evaluation of Menu Labels and Categories"
date: "2023-08-06"
url: "https://www.nngroup.com/articles/tree-testing/"
author: "Page Laubheimer"
topics: [information-architecture, navigation, research-methods]
type: article
---

Developing an effective [navigation hierarchy](https://www.nngroup.com/articles/navigation-you-are-here/) is a challenge. Even when following [best practices for understandable information architecture](https://www.nngroup.com/articles/ia-study-guide/), you cannot be sure that your categorization and labeling choices will make sense to your users. As we often say at NN/g, [if you’re not checking, you’re guessing](https://www.nngroup.com/videos/checking-guessing-ux-slogan/); you need to test your information architecture to be sure that your users will be able to find key resources and features.

This article discusses tree testing, a research method used to assess the [findability](https://www.nngroup.com/videos/findability-vs-discoverability/) of resources after you have created your proposed navigation hierarchy.

## In This Article:

- [What Is Tree Testing?](#toc-what-is-tree-testing-1)
- [The Tree-Testing Process](#toc-the-tree-testing-process-2)
- [Tree-Testing Tasks](#toc-tree-testing-tasks-3)
- [Qualitative vs. Quantitative Tree Testing](#toc-qualitative-vs-quantitative-tree-testing-4)
- [Tree Testing vs. Card Sorting: Different Purposes](#toc-tree-testing-vs-card-sorting-different-purposes-5)
- [When to Use Tree Testing](#toc-when-to-use-tree-testing-6)
- [Benefits of Tree Testing](#toc-benefits-of-tree-testing-7)
- [Limitations of Tree Testing](#toc-limitations-of-tree-testing-8)
- [Conclusion](#toc-conclusion-9)

## What Is Tree Testing?

Much like [usability testing](https://www.nngroup.com/articles/usability-testing-101/), tree testing is a task-based research method where you ask participants to look for key resources.

> **Tree test:** An evaluation of a hierarchical category structure, or tree, by having users find the locations in the tree where specific resources or features can be found.

![Graphic of a mouse pointer in a tree test](https://media.nngroup.com/media/editor/2023/08/15/treetesting_overview.jpg)

To conduct a tree test, you don’t need to create any prototypes, design layouts, or visuals, nor do you have to write any content. You need to prepare only two things:

- the **tree**, or hierarchical menu, which will be displayed as a series of [accordions](https://www.nngroup.com/articles/accordion-icons/) that represent the site’s navigation categories, without any visual design or content
- the **tasks***,* or instructions that tell study participants what they should look for in the tree

As the participant clicks on categories, they expand to reveal subcategories. The participant clicks through the tree until they have found the location that they believe contains the information specified in the task.

![Participant view of a tree test](https://media.nngroup.com/media/editor/2023/07/27/userzoom-tree-test-participant-view.png)

*The participant’s view of a tree test in UserZoom: at the top is the task, and below is the tree for a government website that the participant interacts with during the test. The highlighted item represents one participant’s solution to the given task and the expanded menus (* Home > Citizen > Popular Online Services > MVD Online Services *) correspond to the sequence of parent categories clicked by the participant.*

## The Tree-Testing Process

### 

### Define the Tree

Your tree should be a list of all the categories and subcategories in your [global navigation](https://www.nngroup.com/articles/navigation-you-are-here/) (and, potentially, in your [utility navigation](https://www.nngroup.com/articles/utility-navigation/), as well). Go beyond creating just the top-level navigation categories — define your tree down to the lowest level of subcategories that will contain the resources you will ask study participants to find.

### Select a Tool

You could conduct a tree test using a paper prototype (or any clickable prototyping tool), but a service designed specifically for tree testing will vastly expedite the data analysis and is well worth it. [Userzoom](https://userzoom.com/) and [Treejack](https://www.optimalworkshop.com/treejack) are both good options for conducting tree testing.

### Input the Tree into the Tool

Prepare your tree in a spreadsheet, where you can easily visualize and edit it, then copy and paste the entire hierarchy into your tree-testing tool. The spreadsheet should be formatted with your homepage in the top cell of Column A, then lower levels listed out in columns from left to right. Make sure to list only one category on each row, so that your levels will be correctly parsed when you import the hierarchy.

![A tree represented in a multicolumn screenshot](https://media.nngroup.com/media/editor/2023/07/27/tree-in-screenshot.png)

*This spreadsheet illustrates the tree, or menu hierarchy, for the New Mexico state- government website. Each category appears on a separate row, and subcategories are placed in columns to the right of the parent category which contains them.*

Once you have pasted your hierarchy into the testing tool, the categories are parsed and used to automatically create a clickable menu hierarchy in which each category can be expanded to show the corresponding subcategories.

![The same tree as the previous spreadsheet image, but parsed by the testing system into a series of nested accordions](https://media.nngroup.com/media/editor/2023/07/27/tree-accordions.png)

*A tree testing tool such as Treejack, pictured above, will automatically parse your spreadsheet hierarchy into a clickable menu with categories and subcategories.*

## Tree-Testing Tasks

The tasks you ask users to complete are just as important as the tree itself. Here are some typical task types:

- **Resource-finding tasks to key business goals,** where users must locate **** important products or services) or important information that may not have a dedicated page in the navigation
- **Sleight-of-hand tasks,** where users must find a resource that isn’t all that important or commonly needed, but that helps assess the [information scent](https://www.nngroup.com/articles/information-scent/) of a parent category. For example, on an [intranet tree-test](https://www.nngroup.com/articles/fixing-bad-intranet-navigation/) project, I asked participants to find information on their company’s charitable-donation match program –– not because this was a common resource, but because I wanted to assess potential category names for the HR department (*People, HR, Policies and Procedures,* etc.).
- **Potential problem areas**, such as new categories proposed by stakeholders or participants in a card sort, or even categories where there was a lot of disagreement between participants in a card-sorting study
- **Label or location comparisons:** alternate labels or locations for the same category
- **Warmup task:** an easy task at the beginning meant to warm up your participants to the test procedure and which can be used in unmoderated tests to quickly screen out cheaters. If participants get this task wrong, they probably were not paying attention.

For each task you write, you should also define the correct answer(s), corresponding to where the information is located within the tree. This information will allow the testing tool to automatically calculate success rates for each task.

![Tree test accordions with correct answer identified](https://media.nngroup.com/media/editor/2023/07/27/userzoom-success.png)

*This screen from the Userzoom tree-testing system is used to indicate which category is the correct answer for a particular task.*

### Avoiding Common Task-Phrasing Mistakes

Each task should test a category label by asking the user to find something contained within that category. As with usability-testing tasks, tree-testing [task instructions should avoid using terms that give away the answers](https://www.nngroup.com/articles/task-scenarios-usability-testing/). Preventing [priming](https://www.nngroup.com/articles/priming/) can sometimes be accomplished by describing a scenario and motivation. However, keep in mind that users may not read the instructions carefully and may easily miss important details if they are buried in a lengthy story.

Here are a few different possible phrasings for evaluating the *Starting a Business* category on the New Mexico state-government tree (depicted above):

Tree-Test Task Formulation | Find information about starting a business. | Gives away the answer by using the exact label term, | Starting a Business | You are moving to Santa Fe next year, and once you arrive you would like to supplement your income by opening a side business providing lawn-care services. Find out what regulations you will need to follow. | Long and packed with extraneous words that might sidetrack the participants | You are considering opening a lawn-care service. See if there are any resources on this site that can help you begin the process. | Avoids both mistakes above

### Multiple Trees

Sometimes a tree test may involve several trees rather than just one. For example, **if you are considering different labels (i.e., word choices) for the same category**, you may want to test two different trees to compare how the terms perform.

There’s **no need to test multiple trees if you just want to compare different locations for a label** — such as whether *tomatoes* should be placed under *Fruits* or *Vegetables.* Instead of testing two different trees for each location, you can test a single tree and compare how many users clicked *Fruits* vs. how many clicked *Vegetables*. (You’ll also be able to tell which category they tried first if they clicked on both.)

If you test multiple trees, **use a****between-subjects study design**, in which each participant sees a single tree version in a session. Otherwise, the experience with the first tree may affect users’ behavior when interacting with the second tree.

Some tree-testing tools allow you to randomly assign participants to different versions of the tree, in a manner similar to an [A/B test](https://www.nngroup.com/articles/putting-ab-testing-in-its-place/) on a live website, whereas others require that you manually assign participants to entirely different studies (and manually compare the data).

## Qualitative vs. Quantitative Tree Testing

Tree testing can be used both as a qualitative and a quantitative research method, depending on whether you are interested in a [formative or summative evaluation](https://www.nngroup.com/articles/formative-vs-summative-evaluations/).

### Qualitative Tree Testing

Tree testing can be used to **rapidly test and iterate on ideas for information architecture at the beginning of a project**, as it doesn’t require designing layouts, content, or interactions. Much like usability testing, qualitative tree testing [requires only a few participants to gather insights](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) for how to improve the navigation schema. It is often done as a moderated study, to benefit from the ability to have a trained facilitator probe when participants do interesting things. However, qualitative tree testing is [not appropriate for gathering statistics](https://www.nngroup.com/articles/metrics-qualitative/) (such as success rate or time on task).

### Quantitative Tree Testing

**Tree testing can be used****to benchmark a navigation structure** and compare it against other options (such as competitors, other ideas, or future redesigns). Quantitative tree testing requires a larger sample size. Like most quantitative study designs, it usually doesn’t produce deep insights into *why* users think or behave in specific ways but does allow for precise measurement of how long it takes users to find a resource, what proportion of users were successful, and so on. This information is very useful when you are comparing several options for a navigation schema: it’s quite common for product teams to have many different ideas on how to structure their IA, and tree testing can uncover the best option.

We recommend beginning a quantitative tree test with a small qualitative study for two reasons:

- To [pilot your study design](https://www.nngroup.com/videos/pilot-testing/) and ensure that your tasks are understandable and do not bias participants.
- To obtain insights about *why* users chose the answers they did, which category labels are confusing, and ideas for how to address these issues

## Tree Testing vs. Card Sorting: Different Purposes

![Tree testing vs card sorting graphic image.](https://media.nngroup.com/media/editor/2023/08/15/treetesting_treevcard.jpg)

Card sorting and tree testing are two key research methods that are specific to information architecture. Many newcomers to information architecture often misunderstand the purpose of card sorting, and use it inappropriately, instead of a tree test.

In **card-sorting**, users are given a list of representative content items to group and label as they see fit. In **tree testing**, users must find a specific item in a category tree.

The two methods are [used for different purposes](https://www.nngroup.com/videos/problem-solution-space/). **Card sorting is a generative method** used **for discovering possible groupings for your categories** or content. It captures users’ mental models of what belongs together and why, and what to call these groups but is not a particularly good method for evaluating a navigation hierarchy. **Tree testing, on the other hand, is a method solely used for evaluating a potential navigation hierarchy**; you must create the full category structure and name everything before you can test it, but it can reveal whether users are able to find key resources within your proposed structure.

Card sorting does not usually produce the exact categorization scheme you should follow. For example, participants in a card sort often create a generic category to hold a few items which don’t seem to fit anywhere else; this is understandable, but if you were to include an “other stuff” category in your menu, the same users would avoid it like the plague. (Website visitors are [notoriously reluctant to click on vague labels](https://www.nngroup.com/articles/category-names-suck/) because they quite rightly suspect they’ll have to do a lot of work to sift through the content.)

## When to Use Tree Testing

Tree testing can fit quite well in a few different stages of the product-development process.

- **At the beginning of a redesign project**. Tree testing at this stage allows you to [benchmark](https://www.nngroup.com/articles/benchmarking-ux/) the current IA’s performance and discover potential problem areas and confusing aspects to improve. (You can get many similar insights from a traditional qualitative usability test; that type of study will also give your team insights about visual design, layout, interaction design, and content. The advantage of doing tree testing is that it will help you benchmark improvements to the IA for the purpose of [demonstrating ROI](https://www.nngroup.com/videos/calculating-roi-design-projects/)).
- **After a card-sort study**. As card sorting often has [ambiguous results](https://www.nngroup.com/videos/ia-dendrogram/) (i.e., it gives you ideas, but not a single clear “correct” IA structure), you should always test the hierarchy that emerged from a card-sorting study.
- **Before generating content or layouts.** One key benefit of tree testing is that it allows you to test multiple IA options without any design, coding, or content development. As a result, a tree test enables the team to get the IA right without creating needless churn and revisions of the rest of the product’s design.

One common information-architecture research recipe is to:

1. Begin a redesign project with a usability test on the existing website or product. The test can include some findability tasks (as described below), focused on identifying confusing areas of the current navigation hierarchy.
2. Use a card-sorting study to generate options for redesigning the IA.
3. Do a tree test to assess one or more potential hierarchies and decide which should be the backbone of the redesign project. The tree test allows the information architect to efficiently identify problems, develop options, and refine the navigation hierarchy before any content writing, design, or coding has begun.

## Benefits of Tree Testing

Tree testing is useful because it:

- Evaluates a hierarchy according to how it performs in a real-world scenario, using tasks similar to those in a usability test
- Can be conducted well in advance of designing page layouts or navigation menus
- Tells you if users were able to find the “correct” answer, any other categories users selected, how long it took them, and even whether users bounced around trying a few categories before making a choice or went *directly* to their selection (a measure called **directness**, which can give you context about the clarity or ambiguity of your category labels, also functions as a proxy for how confident users are in a particular path)
- Provides a way to check whether [polyhierarchical](https://www.nngroup.com/articles/polyhierarchy/) options are necessary (e.g. if you categorized *socks* in both *footwear* and *accessories*, did any participants look for socks in the *accessories* category? If not, perhaps you don’t need to have socks in both places.)

## Limitations of Tree Testing

### Lack of Context in Unmoderated Studies

Tree testing (especially its quantitative version) is often executed as a remote, [unmoderated](https://www.nngroup.com/articles/remote-usability-tests/) study. After [recruiting representative users](https://www.nngroup.com/articles/recruiting-test-participants-for-usability-studies/), you send them a link to the study, and the testing tool walks them through the process of completing the tasks using their own computer. The testing tool is much better than a human would be at keeping track of exactly which categories users click on.

However, this format **does not capture the full context of user behavior** (such as comments made while performing the task) and **you can’t ask personalized followup questions**.

To minimize the effects of the format, **conduct at least a few moderated****pilot sessions** before collecting the bulk of your data. In these moderated sessions you can ensure the task wording is understandable and get a chance to pick up on nuances that might otherwise be hard to spot.

For example, in the pilot of a recent quantitative tree testing study, we noticed that many users avoided a certain category because the label was so broad that they feared the content would be overwhelming. This trend wasn’t noticeable in the quantitative results due to the task-order randomization, but it was evident as you sat through each session and saw task after task where users ignored an obvious choice. That insight alone made the pilot test a day well spent.

You can also partially compensate for the inability to ask followup questions in unmoderated tree tests by **including a short survey after the tree test**. Rather than asking users to recall any labels they found confusing, provide them with a list of labels and ask them to check which were difficult to understand. This question can be followed up with an [open-ended question](https://www.nngroup.com/articles/open-ended-questions/) inviting users to share any further comments and feedback, to elicit unexpected assumptions or misunderstandings that may not be apparent from the click history.

### Correct Answers Can Be Only a Leaf, Not a Branch

Tree-testing software typically comes with the limitation that **users can choose only bottom-level items in the tree as their answer** for a task; in other words, these systems assume that the categories that have child elements don’t have pages of their own. This draws from the directory metaphor on computers–- in my Mac’s Finder, I can have folders that contain files, but the folder itself isn’t a file, it’s just an empty box to put files in.

This is not always the case for actual websites, where a category in a navigation hierarchy may have a landing page of its own and still have child pages below it. For example, on the NN/g site, we have a navigation category called *Consulting*. That category *Consulting* isn’t just a folder – it’s a page, but it *also* acts as a folder with multiple child pages below (such as *Benchmarking, IA & Navigation Analysis,* and *Usability Testing)*.

![NNG page with child page](https://media.nngroup.com/media/editor/2023/07/27/nng-consulting.png)

*On NNgroup.com, the* Consulting *category in the navigation has its own category page as well as multiple “child” pages in the tree. However, tree-testing software wouldn’t allow us to mark this* Consulting *page as a correct answer to a task about where to find a list of our consulting services, since it’s technically a branch, not a leaf in the tree hierarchy.*

Unfortunately, tree-testing software cannot account for that sort of real-world design. You cannot mark a category (which is a *branch* on the tree) as the correct answer, only the lowest level (a *leaf* at the deepest level of its branch).

![Tree testing software that doesn't allow a branch to be selected as an answer](https://media.nngroup.com/media/editor/2023/07/27/leaf-not-branch.png)

*UserZoom’s tree testing software does not allow one to mark a category (such as* Consulting *in this screenshot) as an answer. Only the items at the bottom of the hierarchy (such as* Usability Testing *in this screenshot) can be answers. This may not always match the real world, where intermediate nodes may have landing pages.*

## Conclusion

Tree testing focuses exclusively on evaluating the findability of key resources in your category structure and whether the text labels are understandable to users. This is both its great strength and a significant weakness. Since the menu that users interact with is completely devoid of visual styling and content, the experience is different than interacting with the full design. For example, a design with [mega menus](https://www.nngroup.com/articles/mega-menus-work-well/) provides a quite different browsing experience than the one tested in a tree test, since it simultaneously displays the contents of several subcategories.

However, even these inherent limitations can often be overcome or minimized with careful data analysis — for example, by focusing on whether the user selects the correct top-level category, rather than on success rates for sites with mega menus.

Overall, these limitations are a small price to pay for the benefit of quickly being able to iterate and evaluate major structural changes to an information hierarchy early in the design process. You can create a completely new tree to test just by editing your spreadsheet — with absolutely no design or coding required.
