---
title: "Multivariate vs. A/B Testing: Incremental vs. Radical Changes"
date: "2018-04-08"
url: "https://www.nngroup.com/articles/multivariate-testing/"
author: "Aurora Harley"
topics: [analytics-and-metrics, research-methods]
type: article
---

In the world of design-optimization methods, A/B testing gets all the attention. Multivariate testing is its less understood alternative, often deemed too time-consuming to be worth the wait. While this method has its limitations, they are counterbalanced by its benefits, which cannot be easily achieved using A/B testing alone.

## In This Article:

- [Multivariate Testing (MVT)](#toc-multivariate-testing-mvt-1)
- [Difference Between Multivariate Testing and A/B Testing](#toc-difference-between-multivariate-testing-and-ab-testing-2)
- [MVT Measures Interactions Between Elements](#toc-mvt-measures-interactions-between-elements-3)
- [Limitations of MVT](#toc-limitations-of-mvt-4)
- [Use MVT to Refine a Design, Not Completely Change It](#toc-use-mvt-to-refine-a-design-not-completely-change-it-5)

## Multivariate Testing (MVT)

Let’s assume you wanted to optimize the design of a live product-detail page in order to maximize [conversions](https://www.nngroup.com/articles/conversion-rates/) for adding the item to the user’s cart. You are considering several possible changes:

- Using a video of a product instead of an image
- Changing the label of the main call-to-action button from *Buy Now* to *Add to Cart*

A **multivariate test can help you decide which combination of these design choices** would optimize conversions.

Let’s first clarify some terminology:

- **Variable:** A UI element (such as an image or headline) with multiple possible design versions

In our ecommerce example, the variables are the visual representation of the product and the label of the call-to-action button.
- **Variant:** Each design version of a variable

The product image and the product video represent the two variants for the visual-representation variable; the *Add to Cart* and the *Buy Now* labels are the variants of the call-to-action.
- **Variation:** The resulting design containing a variant of each variable, to be compared with other variations

In our example, there would be 4 design variations, corresponding to all the possible combinations of the variables’ variants: image × *Add to Cart*, image × *Buy Now,* video × *Add to Cart,* video × *Buy Now*.

> Definition: A multivariate test (MVT) is a design-optimization method in which **multiple variants of specified variables** are tested in a user interface, with the goal of maximizing conversions (either major conversions like completing an order, or [micro conversions](https://www.nngroup.com/articles/micro-conversions/) like interacting with a feature on a page). This method determines which combination of the variants results in the highest performing design (in terms of the conversion goal specified).

![Diagram showing UI with 2 variants for 2 variables identified.](https://media.nngroup.com/media/editor/2018/03/16/mvt.png)

*In a multivariate test, 2 or more design elements (the variables) are tested. Each of these variables could have multiple variants. For example, in the above page we could test 2 variables: visual representation for a product (with 2 variants: an image or a video) and label for the main call-to-action (with 2 variants:* Buy Now *or* Add to Cart *).*

## Difference Between Multivariate Testing and A/B Testing

Multivariate testing is often regarded as a type of[A/B testing](https://www.nngroup.com/articles/putting-ab-testing-in-its-place/), although its setup and strengths are somewhat different. Here are the similarities and differences between them:

- Both methods test design variations against each other by dividing live site (or application) traffic across variations.
- Both measure which design alternative (i.e., variation) leads to the highest rate of conversions for specified goals.
- In an A/B test, the variations being tested could be completely different from each other, and not the result of manipulating a small set of variables. For instance, you could have two pages with completely different layouts, different copy, different navigation, different visual design, and so on. The result of the A/B test will indicate that one variation performs better than the other, but you will not know whether it’s because your copy is better, your visual design is better, or your layout is better (or the combination).

In contrast, if you use MVT, you will usually be able to assign credit to one particular variant or combination of variants. Thus, you may, for example, find out that a product video makes a much bigger difference in your conversions than changing the button label, which can give you further strategy and design insights (for instance, it may tell you that it’s worthwhile to invest in producing good product videos).

## MVT Measures Interactions Between Elements

Let’s come back to our original ecommerce example. You may wonder whether two sequential A/B tests would produce the same result as an MVT. Specifically, let’s pretend that you’d first run an A/B test to compare the video vs. the image — assume that the video wins. Next, on the winning variation (i.e., video), you’d do another A/B test between the two possible button labels, and the *Buy Now* label proved better. Wouldn’t this result be equivalent with the MVT test?

The answer is: not necessarily. It may be the case that the optimal combination is image × *Buy Now*, but you won’t have tested that version.

The main advantage of running a multivariate test rather than an A/B test is the **ability to determine how various elements on a page interact** with one another. Only by testing each combination of various variants can you not only figure out that visual A performs better than visual B, and that button C performs better than button D, but you can also **discover the best combination** of these overall.

## Limitations of MVT

The variations generated from every combination of the variants multiply like rabbits. Even our fairly simple ecommerce example has 4 design variations to compare, corresponding to all the possible combinations between the 2 variables. Adding 1 more variant for the call-to-action variable (e.g., *Purchase*) would create 2 more variations — generated by combining this variant with the other 2 variants of the visual-representation variable. (In general, the number of variations will be obtained by multiplying number of variants for each variable; so if you had 2 variables, one with 2 and the other with 3 variants, you’ll get 2×3=6 variations.)

![Diagram showing 4 combinations of the variants](https://media.nngroup.com/media/editor/2018/03/16/4variations.png)

*Two variables that have each 2 variants leads to 4 design variations in a multivariate experiment, to represent all the possible combinations of these variants.*

The large number of variations that need to be tested in a multivariate test leads to this method’s greatest limitation: much **more traffic is typically required to run a multivariate test** compared to an A/B test, in order to reach statistical significance. This is because each variation added to the comparison causes the live traffic to be divided into smaller pieces, and thus it also can take a long time to gather enough data points for each design alternative. (However, keep in mind that the time needed to run the test is dependent not only on the overall traffic, but also on the expected change in conversion rate for the experiment goal, because bigger improvements are easier to measure than tiny differences.) In general, splitting the live traffic among more variations leads to longer-running experiments.

Another limitation of MVT is that **all combinations of the variants must make sense** together. For example, when testing variants of an image and of a headline on a page, don’t write headlines that refer to details of an image variant (such as “Great Spa Vacations” vs. “Great Beach Vacations” with corresponding photos), because each headline will accompany each image in a variation for the test. That type of experiment would be better set up as an A/B test, so the combinations could be more controlled.

## Use MVT to Refine a Design, Not Completely Change It

Multivariate testing is a great way to **make incremental improvements to a design**, rather than dramatic redesigns. Because it requires that you identify certain elements of interest on a page to test multiple variants of that variable, you cannot easily compare radical changes across variations.

![Diagram showing A/B test for radical page redesigns compared to MVT for incremental improvements.](https://media.nngroup.com/media/editor/2018/03/16/whentousewhich.png)

*For major redesigns, run an A/B test between the original and the proposed new version to find which is better. Then, refine various elements of the winning design using multivariate tests. Always keep iterating!*

If your goal is to move towards a substantial redesign (such as major layout redesign), an A/B test to compare this new design against the current one is more appropriate than an MVT. **Once the higher-performing design is discovered, use multivariate tests to further refine specific elements** in the winning layout.
