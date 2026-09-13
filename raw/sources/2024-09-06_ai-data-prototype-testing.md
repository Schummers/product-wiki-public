---
title: "Leverage AI for Mock Tables and Charts When Testing Prototypes"
date: "2024-09-06"
url: "https://www.nngroup.com/articles/ai-data-prototype-testing/"
author: "Evan Sunwall"
topics: [ai, prototyping]
type: article
---

Prototype testing is at the core user-centered design. But crafting realistic data for prototypes that you plan to test is time-consuming. Especially when the design itself is still evolving, you’re pressed for time, or you are a [one-person UX team](https://www.nngroup.com/training/course/4901/one-person-ux-team/). Don’t let the struggle of crunching numbers discourage you. Generative AI can help.

## In This Article:

- [Users Will Scrutinize Your Tables and Charts](#toc-users-will-scrutinize-your-tables-and-charts-1)
- [Be Cautious with Your Real Data](#toc-be-cautious-with-your-real-data-2)
- [Craft a Promptframe](#toc-craft-a-promptframe-3)
- [7 Tactics for Generating Mock Tables with AI](#toc-7-tactics-for-generating-mock-tables-with-ai-4)
- [7 Tactics for Generating Mock Charts with AI](#toc-7-tactics-for-generating-mock-charts-with-ai-5)
- [Importing Tables into Design Tools](#toc-importing-tables-into-design-tools-6)
- [Differences in AI Tools for Mock-Data Generation](#toc-differences-in-ai-tools-for-mock-data-generation-7)
- [Opportunities with Synthetic Data in Regulated Industries](#toc-opportunities-with-synthetic-data-in-regulated-industries-8)

## Users Will Scrutinize Your Tables and Charts

Research in data sensemaking by Laura Koesten and colleagues found that when participants were given unfamiliar data, they spent more time looking for outliers and inconsistencies than when they worked with familiar data. If you plan to test a prototype (especially if your [user personas](https://www.nngroup.com/articles/persona/) critique data frequently), **your study participants will scrutinize the prototype’s tables and charts, whether you want them to or not**.

This article will discuss practical tactics that any UX professional with access to a general-purpose generative AI tool can use to create higher-quality charts and tables efficiently. To illustrate these tactics, we use a hypothetical example of a sales and marketing-management app targeting ecommerce retailers.

## Be Cautious with Your Real Data

Some of the tactics I recommend involve sharing portions of actual data or examples. In any situation involving generative AI (genAI) and your organization’s data, always be informed and follow your organization’s policies and data-protection regulations.

We recommend that you never share sensitive or identifying data with genAI tools unless your company has verified and approved their use.

## Craft a Promptframe

Start by gathering the information needed to inform your mock-data generation. Create a [promptframe](https://www.nngroup.com/articles/promptframes/) to establish objectives and requirements for content areas. This hybrid form of prompt writing and wireframes will help you facilitate dialog with your collaborators and build prompts to use with an AI.

During this process, remember your testing goals and usability-testing tasks. What would you hope users will accomplish with the prototype during testing? Where are the contentious parts of the design that need clarification?

## 7 Tactics for Generating Mock Tables with AI

Consider these 7 tactics when crafting the prompt for generating tables.

### 1. Contextualize Tables to Your Audience

**Consider the contextual qualities that the AI should mimic** and reference from its training data. Your table will be less helpful if your AI is modeling data for a large enterprise when your app targets mall businesses. For example, business size, industry or market, geography, or time periods can all influence the table’s data.

In addition, ask yourself whether the AI should use real or just realistic names for data such as companies or products. Include these details in the prompt.

![The image compares two sales data scenarios for shoe companies, highlighted with red and blue annotations. Scenario 1 is a large U.S.-based shoe corporation with annual revenue of $1 billion. The table shows high volumes and low prices in dollars for real athletic shoes, such as Nike Air Force 1 and Adidas Stan Smith, with monthly units sold ranging from 72,500 to 15,800 and prices from $80 to $185. Scenario 2 is a small French boutique shoemaker with annual revenue of €450,000. This table shows low volumes and high prices in euros for bespoke, French-styled shoes like Le Parisien Oxford and Riviera Loafer, with monthly units sold between 4 and 9 and prices ranging from €280 to €750. Annotations emphasize the differences in volume, price, and product type between the two scenarios.](https://media.nngroup.com/media/editor/2024/08/26/contextualize-data.jpg)

*Claude 3.5 Sonnet was prompted to demonstrate two scenarios of how context affects the generated data. Scenario 1 was focused on data suitable for a large athletic-shoe corporation in the United States. It used real shoe names and large sales volumes. Scenario 2 was focused on data for a boutique shoemaker in France. It had tiny sales volumes, high prices in euros, and French-styled shoe types.*

### 2. Define Volume

**Determine how much data needs to be generated.** You may have room to display only a few dozen rows of a data table in your prototype, but the dataset may be much larger. Describe the size of the larger dataset, if known, so the AI can account for these additional records when calculating values. Mention that you require only a subset to be generated.

For example, a table may typically contain approximately 2,000 transactions totaling 7 million dollars of revenue. You only need 50 transactions to show in your prototype. The AI will account for 2,000 transactions when generating revenue values for those 50.

![A comparison of two scenarios for generating daily revenue data for an online shoe retailer, with differences highlighted by annotations. In Scenario 1, the prompt does not specify the number of products, leading to larger daily revenue figures for each shoe model, such as Running Pro X and Formal Elegance G. Scenario 2 defines the dataset size as 100 products, resulting in smaller daily revenue figures for the same shoe models. The annotations emphasize how the lack of a specified dataset size in Scenario 1 results in higher revenue numbers, while Scenario 2’s defined dataset size produces more moderate figures.](https://media.nngroup.com/media/editor/2024/08/26/define-volume.jpg)

*Claude 3.5 Sonnet was prompted to demonstrate two scenarios illustrating the impact of defining volume on generated data. In both scenarios, Claude was prompted to generate daily revenue for 10 shoe products, assuming $10 million in total annual revenue. Scenario 1’s prompt did not mention how many shoe products the company sold. Scenario 2’s prompt mentioned that the company sold 100 different shoe products. Scenario 2’s revenue numbers were much smaller compared to Scenario 1, since Claude factored in revenue from 90 other products.*

### 3. Apply Sorting

Ask yourself if **there is an ideal ordering for the data.** There is no need for you to sort your table manually in a spreadsheet; instruct the AI to sort the data by that value.

### 4. Provide Specifications for the Data

Add these specifications to your prompt for more authentic-looking data for your table.

- **Uniqueness**: Do all **the values need to be distinct, or can there be duplicates**? For example, a *Product**Name*, *Tracking Number*, or *Email Address* column would typically not contain duplicate values.
- **Fixed values**: Sometimes, **data has predefined values** that must be used. Enumerate those options in your prompt. For example, each row's *Status* column can be tagged only as *Open*, *In Progress*, or *Closed*.
- **Formatting**: Specify the format you need in your prompt, such as *DD MM YYYY* for dates or $XX.99 for prices. (A common pricing tactic is to have product prices end in .99, such as $19.99.)
- **Plausible ranges**: Determine a **realistic range to bound** values in the table. For example, average product ratings on ecommerce sites typically range from 1 to 5 stars, or human systolic blood pressure generally ranges from 90 to 140 mmHg.
- **Flexible and inflexible constraints**: If there is data where it does not matter what the generated values are, **make it clear to the AI that it can adjust those values** to comply with other constraints you’re placing on the table. But mention any specific values that your usability-testing task and prototype design depend on. For example, if a usability-testing task depends on the fact that product named *Roadrunner Sprinter* has the most customer complaints, then mention that as a requirement in your prompt.
- **Value distribution**: Sometimes, you want values to be over- or underrepresented in the table. For example, a table listing code defects that developers must fix may have few rows with an *In Progress* status. **Mention these useful distribution types in your prompt** to guide the AI in distributing values: 

  - **Normal distribution**: This is the classic bell curve. Most values center around the mean, with a minority at the extremes.
  - **Pareto distribution**: A few data points generate most of the impact, while most others generate little. For example, it’s common for only a few products to generate most of a company’s sales.
  - **Uniform distribution**: Values are spread evenly across a range of potential values.
  - **Custom distribution**: Mention precisely how you want the values distributed. For example, 20% of rows should use *Value A*, 60% should use *Value B*, 20% should be blank, and so on.

### 5. Provide a Chart and Generate Supporting Data

If you have a specific chart already designed but need the tests participant to also be able to inspect the table containing that chart’s data, **upload the chart along with your prompt**. Thanks to the multimodal capabilities of today’s AI tools, they can use this added context when generating table data.

![A bar chart titled “Product Performance - Total Sales,” showing the sales figures of various shoe models, with “Pegasus” having the lowest sales. Below the chart is a prompt for a data analyst role. The instructions ask the analyst to analyze the bar chart, identify the worst-performing product, and generate a realistic transaction dataset to match that product’s performance. The prompt includes detailed specifications for the data, such as transaction ID, product name, quantity sold, price, and total line item, along with tips for completing the task. An annotation highlights that the bar chart is directly attached to the prompt.](https://media.nngroup.com/media/editor/2024/08/26/provide-chart.jpg)

*Claude 3.5 Sonnet was provided with a bar-chart image and prompted to generate transaction data for the worst-performing product. The worst-performing product and the exact sale values were unspecified in both the bar chart and the prompt to test Claude’s multimodal capabilities. Claude correctly identified the worst-performing product, estimated a reasonable value from the bar chart, and generated the table.*

### 6. Contextualize Tables to Your Participants

Leverage AI’s abilities to quickly regenerate and revise data to create mock tables tailored to your users.Ask yourself: What do you know about your usability-testing participants? What kinds of data do they use in their domain, and how would that affect the test of your design? For example, a prototype focusing on shoe products could be pivoted into hats with minimal change.

Share your existing mock table with the AI and ask it to revise it with a description of the participant’s background and context. Then, reupload that table back into the prototype.

### 7. Require Explicit Calculations and Verification

Always **be cautious when dealing with numbers and generative AI**. Large language models’ math skills depend on help from additional tools. Sometimes, the AI will rely on patterns found in its training data, which may fail in more complex calculations. Worse, the AI will confidently hallucinate that it diligently followed your instructions when it did not. Therefore, use these approaches in your prompts to avoid errors:

- **Prompt for using coding tools**: Confirm that your AI can use coding tools (namely Python, which is well-suited for math) and require their use for all numerical calculations. You should also check the AI tool's interface to see if the AI indeed generated and executed code for numerical values (even if you don’t know Python).
- **Ask for explicit calculations**: Ask that the AI show its work when performing calculations. For example, the prompt may say "Sum the *Revenue* column and show your calculation process."
- **Require verification**: Instruct it to doublecheck each result according to your requirements before completing its task. For example, "Verify that the *Revenue* column totals exactly $487,455 before finishing your task.”

You may need to display totals in other parts of your prototype, so requesting them in your prompt makes you more efficient and the AI more accurate in its mock-data generation.

![A process of verifying an “Ecommerce Shoe Sales Data Generator” table against given guidelines. The table lists products, their prices, and quantities sold. Annotations indicate different verification steps: ensuring each product name is unique and realistic, checking that prices end in .99 and fall within the specified range ($59.99 to $299.99), and confirming quantity sold ranges from 0 to 687. The final annotation points out unreliable revenue calculations that overshoot the target by a significant margin, indicating the need for adjustments.](https://media.nngroup.com/media/editor/2024/08/26/verify-calculations.jpg)

*Claude 3.5 Sonnet was prompted to generate a mock table of athletic-shoe products with various requirements and a total revenue of approximately $487,455. Since Claude was prompted to show calculations and verify its work, it met most requirements but overshot the desired total revenue. Claude self-corrected and eventually provided a dataset that complied with the desired total revenue. That said, a more reliable method would have been for Claude to use Python to calculate the total accurately, but this version of Claude lacked that capability.*

## 7 Tactics for Generating Mock Charts with AI

### 1. Describe What to Show

Rather than fumbling with numbers for charts, **describe the story** instead. Part of what makes AI powerful is that you can use natural language to convey your intent.

For example, you could include in your prompt that overall revenue has been trending downward over the past year, but there was a spike in December due to seasonal holiday demand. The AI will generate a starting point for your narrative, and you can further refine it.

### 2. Eliminate the Clutter

The AI tool may render charts with gridlines, drop shadows, or legends that are [more clutter than](https://www.nngroup.com/articles/clutter-charts/)**insight**. By default, most AI tools will include some of these chart elements, so ask it in your prompt not to use them.

### 3. Emphasize Outliers

In many usability-testing tasks, charts can visualize outliers that require user analysis and attention. **In your prompt, call out these outliers.**

For example, in a bar chart depicting sales performance across sales representatives, you might specify that one person, *Sam H.,* has accomplished roughly only 20% of his sales quota, and only his bar should be shaded red. This instruction would be helpful if you were testing to see if the user notices *Sam H*.’s lagging performance and engages in a sales-coaching workflow.

### 4. Specify Dimensions

**Include the chart’s dimensions** in your prompt. (You may copy them from your promptframe, if using one.) Setting dimensions will save you significant time readjusting chart elements to fit them into the interface.

### 5. Request SVG format

Request that generated charts use **the scalable vector graphics (SVG) format**. Compared to image formats (JPEG or PNG), SVG preserves the editability of individual chart elements in design tools, which is important if you need to make small adjustments to the chart later.

![A dashboard interface with a bar chart titled “Top Products by Revenue” highlighting different products and their associated revenue. The products listed include “Air Zoom Pegasus,” “Ultra Boost 21,” “Superstar,” and others, with revenue amounts visualized by the length of green bars. Above the chart, key performance indicators (KPIs) are shown, including total revenue ($842,982), number of orders (7,246), and average order value ($116.20). A red annotation on the right points out that the text elements within the chart are editable, indicating the potential for customization or modification of the data labels and other text components.](https://media.nngroup.com/media/editor/2024/08/26/editable-elements.png)

*Generating charts in SVG format makes them easy to import and edit in design tools like Figma.*

### 6. Don’t Delegate Critical Thinking

Even though AI can rapidly construct and modify charts, Claude 3.5 Sonnet and ChatGPT 4o would dutifully create nonsense charts, even when prompted to act as a data-visualization expert. These tools have impressive capabilities, but **they need a discerning human prompter**.

You must train on [effective data-visualization techniques](https://www.nngroup.com/articles/choosing-chart-types/) if you frequently design chart content. Relying on AI to catch your mistakes is a mistake.

![A line chart titled “Product Performance Over Time,” plotting sales data for various shoe products, such as “RunnerPro X1,” “AirWalk 2000,” and “UrbanPace 5.” The sales figures fluctuate, creating a wavy trend line that may suggest a continuous relationship between these discrete categories. However, a blue annotation points out that the chart’s trend is misleading. A suggestion below the chart recommends using a bar chart instead, as bar charts are better suited for comparing discrete categories without implying a continuous trend, which would prevent the misinterpretation of the data.](https://media.nngroup.com/media/editor/2024/08/26/misleading-trend.jpg)

*ChatGPT4o and Claude 3.5 Sonnet were prompted to act as data-visualization experts and asked to critique this uploaded line chart. Both initially failed to recognize that the chart showed meaningless and misleading product trends. However, when prompted to identify the X-axis’s level of measurement and then asked to critique the chart again, Claude correctly recommended a bar chart because the X-axis used qualitative data.*

### 7. Provide Data and Request a Chart

This is the reverse of the tactic above. Provide the AI with a table and ask to plot it using several chart types. Requesting variants is an efficient way to ideate over charts (but use critical thinking, as mentioned above).

## Importing Tables into Design Tools

Now that you have sensible content, how do you get it into your design tool?

For charts, this is as easy as copying and pasting or importing the SVG file into the design tool. Tables are more challenging, however. Design tools have historically done a very poor job importing table data, but there are options.

For example, Figma has several community-made plugins that assist with importing data from spreadsheets. [Google Sheets Sync](https://www.figma.com/community/plugin/735770583268406934/google-sheets-sync) and [Table Builder](https://www.figma.com/community/plugin/1104128112873973808/table-builder?searchSessionId=ly7hf0o4-qjl1eil3rb8) are free plugins that import and synchronize spreadsheet data with Figma layers, helping you to populate a table efficiently.

*Figma has plugins like* Table Builder *that enable you to copy and paste AI-generated data into your prototype.*

However, there are issues with Figma’s third-party plugin model. These plugins can have usability issues and hidden costs, they may raise data-privacy concerns, or they may become abandoned and unsupported by their author.

More specialized and robust design tools, such as Axure, support importing spreadsheet files directly into prototype components. This feature can be a significant convenience for designers of data-intensive apps testing data-manipulation workflows.

*Axure allows importing data from a CSV-formatted file into a dedicated component that supports filtering, sorting, searching, pagination, and row manipulation as prototype interactions.*

Regardless of your design tool, **do not import thousands of rows with these methods and do not attempt to create a complete simulation of a developed design** (you’ll probably break your design tool). Import just enough data to enhance the prototype’s content fidelity and support the tested interactions. A fully developed data table may contain thousands of records, but you may need to display only 50 realistic-looking rows in your prototype to support a testing task.

## Differences in AI Tools for Mock-Data Generation

AI tools have differences in their training and available tools; they do not handle tasks in the same way or with the same proficiency.

While exploring mock-data capabilities for this article, **Claude 3.5 Sonnet was easier to use and more reliably effective at generating tables and charts than ChatGPT 4o**.

Claude 3.5 Sonnet | ChatGPT 4o | Tables | Data Quality | ✅ Generated data that more consistently followed requirements, such as enforcing unique values for a column, distributing values, or applying formatting | ❌ Would claim that the generated data followed requirements when it did not, despite prompts to verify its output before finishing | Numerical Accuracy | ❌ Generated Python code but could not run it to confirm numerical accuracy | ✅ Could run Python code to confirm numerical accuracy | File Output | ⚠️ Could not generate Excel or CSV files, but the data could be copied and pasted into a spreadsheet | ✅ Generated Excel or CSV files containing the data for download | Charts | Generation | ✅ Reliably created and modified charts when prompted (using the React-based Recharts library); applied best practices | ⚠️ Reliably generated and modified various charts when prompted (using the Python-based matplotlib library); sometimes included unhelpful defaults (e.g., axes’ labels formatted in scientific notation, such as .2e6 for 200,000) | Fonts | ✅ Could use web-safe and system font families | ❌ Had limited font family options and could not be prompted to use different ones | Ease of Import into Design Tool | ✅ Generated charts with text elements that were easy to copy, paste, and edit in a design tool (when prompted to use the SVG file format) | ❌ Rendered chart text as vectors and not actual text elements, so the chart’s text could not be edited in the design tool

Also, design tools such as Figma are experimenting with integrating AI-powered commands. These integrations are promising developments, as designers need more efficient workflows that prompt AI tools in their design context. But beware:

- A general-purpose AI tool may be more effective at generating tables and charts than an AI feature embedded in Figma or another design tool.
- It's unclear whether these AI-powered commands support revising a comprehensive dataset rather than independently filling separate elements with generated text or images.
- Prompting from within the design tool may not retain the rich context and chat history available in a general-purpose AI tool such as Claude or ChatGPT. As a result, designers may find revising content more challenging.

AI tools are rapidly evolving, so today’s winner could be tomorrow’s loser as new model versions are released. But if you’re struggling to get desired results from your preferred AI tool, try a different tool instead (if you can). Its results may surprise you.

## Opportunities with Synthetic Data in Regulated Industries

This article has focused on filling tables with mock data, which is artificially generated and inspired by real data. However, it lacks high statistical fidelity and is used in small quantities. For many UX professionals, mock data is the pragmatic choice for their fast, iterative prototyping.

Yet, synthetic data may be helpful for UX professionals who work in highly regulated industries such as healthcare or finance. Synthetic data is derived from samples of actual data. Specialized AI tools use these samples to artificially generate new data that mimics various properties of the original, such as statistical patterns. Undesirable aspects (originating from those actual data samples) may also be adjusted, like personally identifiable information or human biases. The result is much more realistic data and in much larger quantities.

If a lack of representative data in your prototypes is a recurring problem, build relationships with others in your organization with similar needs. For example, with more authentic data, a presales team could customize more-understandable product demos for prospective customers, and a quality-assurance team could have more realistic testing builds to help them catch more functional defects before release. Forging alliances with other departments with similar pain points can justify the cost and effort of implementing a synthetic-data AI tool.

### Conclusion

Data-intensive applications are challenging to design, prototype, and present realistically. Despite the effort required, your prototype’s content fidelity must be high to gain the most valuable insights from usability testing. Clever use of generative AI can help create and refine the data necessary to make these experiences sensible to your meticulous users. Crafting realistic data is a chore, but now we have help.

### References

Laura Koesten, Kathleen Gregory, Paul Groth, and Elena Simperl. 2021. Talking datasets – understanding data sensemaking behaviours.*International Journal of Human-Computer Studies* 146, 102562. DOI:http://dx.doi.org/10.1016/j.ijhcs.2020.102562
