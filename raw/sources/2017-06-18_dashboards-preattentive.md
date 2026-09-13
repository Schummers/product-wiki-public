---
title: "Dashboards: Making Charts and Graphs Easier to Understand"
date: "2017-06-18"
url: "https://www.nngroup.com/articles/dashboards-preattentive/"
author: "Page Laubheimer"
topics: [applications, psychology-and-ux, visual-design]
type: article
---

Data dashboards are a common tool used in web apps, intranets, and other business intelligence contexts to show regularly updated information that users must frequently monitor.

Definition: **Dashboards** are collections of data visualizations, presented in a single-page view that imparts at-a-glance information on which users can act quickly.

The term “dashboard” is a metaphor for a car dashboard, which provides essential information that the driver can absorb quickly, without having to think. Thus, dashboards are not intended as expansive views of complex data: Their goal is not to facilitate exploration; instead, they provide information that can be consumed fast, with a minimum of interaction or cognitive processing. Users can glance at the dashboard and immediately see answers to questions like, “Am I speeding?” and “Am I about to run out of gas?” (in the case of an actual car dashboard), or “Are sales up?” and “Is this week’s email newsletter driving as much traffic as recent newsletters?” (in the case of a data dashboard).

Dashboards are distinct from [portals](https://www.nngroup.com/articles/intranet-portals-personalization/), which provide a combination of resources, information, tools, or access to [web-based applications](https://www.nngroup.com/courses/application-ux/), and are a single-point gateway for a variety of tasks. Dashboards are focused on a single task: communicating critical information.

## In This Article:

- [Operational Dashboards vs. Analytical Dashboards](#toc-operational-dashboards-vs-analytical-dashboards-1)
- [Preattentive Processing and Quantitative Representation](#toc-preattentive-processing-and-quantitative-representation-2)
- [Linear vs. Area-Based Graphs](#toc-linear-vs-area-based-graphs-3)
- [Use Color, Shape, and Grouping to Show Categories](#toc-use-color-shape-and-grouping-to-show-categories-4)
- [Conclusion](#toc-conclusion-5)
- [References](#toc-references-6)

## Operational Dashboards vs. Analytical Dashboards

Data dashboards generally exist in two forms:

- **Operational dashboards** aim to impart critical information quickly to users as they are engaged in time-sensitive tasks.
- **Analytical dashboards** provide the user with at-a-glance information used for analysis and decision making, but don’t have the same level of time sensitivity as operational dashboards.

![ArcGIS operational dashboard](https://media.nngroup.com/media/editor/2017/06/06/arcgis.png)

*An operational dashboard in ArcGIS shows emergency-management services in an urban environment. This information empowers emergency-response dispatchers to see the status of incidents and response teams. The use of a bar chart to indicate the types of incidents helps dispatchers quickly keep track of which types of emergency services (police, fire, ambulance) are needed.*

Operational dashboards exist to provide information quickly to users that are making immediate decisions and carrying out time-sensitive tasks, such as monitoring server availability, patient vitals during surgery, customer-service calls, or flight traffic. Operational dashboards typically present data that is continuously updating and changing. While not all operational dashboards are used in high-consequence environments like hospitals and emergency management, they all do need to present data quickly to users to help identify unacceptable deviations in parameters or, visualize available resources.

Unlike operational dashboards, which are intended to support time-sensitive decision making and immediate action, analytical dashboards help users identify the need for further thought, investigation, research, or analysis. A sales dashboard (which is usually an instance of analytical dashboard) that is updated once a day won’t show information that requires an immediate emergency intervention from a sales manager, but it can keep the manager aware of fluctuating sales data that will later demand a thoughtful analysis.

Like operational dashboards, analytical dashboards also require an at-a-glance, single-screen view of the data that they monitor, and must quickly communicate important information to a user.

## Preattentive Processing and Quantitative Representation

In order to make it easiest for users to quickly understand the relationships between data, it’s useful to leverage the properties of human visual perception. There are a variety of visual attributes that people perceive very quickly, without fully engaging their attention, in a process known as [preattentive](https://www.nngroup.com/articles/visual-indicators-differentiators/)**processing**. For example, in a display containing many lines of the same size, the one line that is longer will “pop out,” without the user having to engage in a visual search to locate it. Beside length, other preattentive features include area, angle, 2D position, and color.

![../Articles/Data%20Dashboards/Preattentive.png](https://media.nngroup.com/media/editor/2017/06/06/preattentive_lines.png)

*Even without fully devoting one’s attention to the diagram, it is easy to quickly tell which line is the longest, due to efficient and accurate preattentive processing of length.*

Although all preattentive features stand out easily, not all of them are equal. With some, people simply perceive a difference without being able to exactly pinpoint the size of the difference: for example, although we can effortlessly notice a large rectangle in a display containing many small rectangles, we are not good at judging how much bigger the large rectangle is, compared with the others.

In contrast, we are quite adept at estimating how lengths compare, and we can also accurately estimate position in a 2D space. (See the classical 1985 paper referenced at the end of the article for more detail on this finding.) This fact makes these two preattentive attributes ideal for quantitative representation; charts and graphs taking advantage of these features will generally be easy to understand.

![Dashboard with a line chart on the left and a bar chart on the right](https://media.nngroup.com/media/editor/2017/06/06/thedesignwork.png)

*This dashboard example ( from TheDesignWork ) shows a line graph on the left and a bar chart on the right. Line charts leverage the fact that people process 2D position preattentively. In the example chart, it is very easy to see that there is a dip in the data that occurs on Wednesday. The bar chart on the right expresses a single quantitative variable using length, another preattentive feature that allows people to quickly and accurately notice any data points that stand out and understand the quantitative relationships between the data. Thus, it is easy to see right away that the bar for c is longer than all the others, and you can even tell that it’s almost twice as long as the second longest bar (for b).*

Another powerful preattentive attribute is color: a red dot will easily stand out in a conglomerate of blue dots. However, unlike length, people do not perceive different colors as being in a particular order, so color should not be used to communicate information about quantitative values or magnitude. (Additionally, up to 4.5% of the general population suffers from some form of color blindness; also notable is the fact that many more men suffer from colorblindness than women — around 8% vs. 0.5%; though exact numbers vary by ethnicity.)

## Linear vs. Area-Based Graphs

As we mentioned above, 2D position and length are the two preattentive attributes that can be naturally mapped onto quantity and support quick data comparisons and inferences. Thus, visualizations based on them will generally be effective and easy to understand.

Bar charts are a reliable means of representing quantitative data: we pre-attentively process the length of each bar efficiently, allowing for easy comparison of values (especially if they are ordered in an ascending or descending pattern). Graphs that use 2D position like scatter plots or line graphs capitalize on the preattentive 2D attribute.

![Scatterplot of 2-axis data](https://media.nngroup.com/media/editor/2017/06/06/scatterplot.png)

*Scatterplots are an effective visualization for showing relationships between the two variables plotted on the x and y axes. In this graph, because 2D position is a preattentive variable, you can notice right away which data points are highest and lowest along each axis, and can also notice potential correlations or other relationships between the data easily.*

### Circular and Area-Based Graphs Are Difficult to Interpret Quickly or Accurately

Circular graphs like pie charts, gauges, and radar charts do not convey well quantitative relationships between data, as they rely on area and angle to communicate quantitative information. Although area and angle are preattentive features, it’s harder for people to say how much bigger one area is than another.

![Microsoft dashboard with donut charts and treemaps](https://media.nngroup.com/media/editor/2017/06/06/mspowerbi.png)

*This Microsoft Power BI dashboard uses (1) donut charts and (2) tree maps to display data. Donut charts are similar to pie charts — they use area and angle to encode quantitative information — but are made even less effective by the whitespace in the middle, which makes each slice area smaller and thus complicates even more the already difficult task of determining a quantitative value for each option in the chart. The tree map also uses area for representing the relative sales amounts of the different cities — each rectangle’s area denotes its value — but unfortunately, area is a variable that people don’t interpret quickly or with accuracy, and thus a tree map (in this context) is not an effective way to represent quantitative data for rapid understanding.*

Because charts based on area are not terribly efficient as a means of comparing quantities, visualizations like pie charts and tree maps are generally not recommended for *quickly* communicating complex quantitative relationships among items in a data set. Pie charts (and their even less helpful cousin, donut charts) are notoriously poor at most information-communication tasks (other than simply showing overwhelming disparities in percentage shares, such as a single source of revenue that represents the vast majority of a company’s profits), and should be avoided most of the time.

Tree maps (which show a hierarchical data set as a series of nested rectangles of different sizes, where the size of each rectangle corresponds to a numeric value) can be useful at representing a complex data space in a compact overview, when there is opportunity for users to leisurely explore the data set and seek out additional detail. However, treemaps are not appropriate for simple, actionable dashboards.

Angle, too, communicates quantitative information poorly — gauges that mimic the analog gauges found in car dashboards simultaneously consume a lot of precious space on a dashboard and are also harder to interpret than linear graphs.

![Klipfolio dashboard with car-style gauges and alternative bullet charts](https://media.nngroup.com/media/editor/2017/06/06/klipfolio.png)

*This Klipfolio dashboard uses a radial gauge (1) to show the value of a particular metric within a range. However, circular visualizations require a lot of space to communicate little information, and rely on angle (which is relatively poor at communicating information in a pre-attentive fashion) as the main means of communicating the key data. Just below, this same dashboard uses the significantly better linear bullet charts (2) to communicate similar information (quantitative data along a range, with a target value identified). All of these charts fail to show the overall range of the scale, however.*

### 3D Graphics

Plotting a 2-variable chart in 3D is often done to (arguably) improve aesthetics, but will make the chart much more difficult to interpret quickly and accurately, as it distorts the shapes and alignment of the visual features showing data. While area-based graphs (such as pie charts and tree maps) are most susceptible to the distorting effects of 3D visualizations (as placing them in a 3D projection skews the quantitative meaning of the area), 3D bar charts are also more difficult to properly interpret than their 2D counterparts, as they can make it much harder to see which value the top of a bar represents, and how it aligns with the gridlines.

*Using a 3D representation of a chart distorts and skews the shapes that represent the data, thus making it harder to decipher the quantitative values (and relative relationships between specific data). In a 3D visualization, it becomes much tougher to determine which bar is shortest, even though length is a very efficient preattentive variable when presented in 2D. For example, determining the specific relationship between the 3rd and 4th quarters in the 3D chart above is much more difficult than in the 2D version of the same data.*

![3D pie chart](https://media.nngroup.com/media/editor/2017/06/06/3d-pie.png)

*In a 3D representation of a pie chart, area is distorted. In order to create a 3D perspective, the bottom of the chart is tilted “closer” to the viewer (and thus larger than it would be in a 2D representation), and the top of the chart is tilted “away” from the viewer (and thus smaller) to show perspective. Each square centimeter that is “futher away” from the viewer (1)  therefore represents more of the area (and thus percentage data) than an equivalent square centimeter in the “front” of the 3D space (2). In a pie chart (which uses area to show percentage), the visualization is therefore skewed and potentially misrepresenting the data. Considering that area-based visualizations are already poor at conveying quantitative relationships, this 3D representation makes the user’s job much more difficult.*

## Use Color, Shape, and Grouping to Show Categories

While color and shape are preattentive cues that do not easily communicate quantitative relationships, they can be used to convey categorical information — that is, which items in a visualization belong together. (According to the [Gestalt psychology principle](https://www.nngroup.com/articles/closeness-of-actions-and-objects-gui/) of similarity, items that have similar shape or color are usually perceived as related.) Moreover, spatial proximity can also indicate semantic grouping.

Due to the prevalence of people with impaired color vision, color properties such as hue or saturation are helpful as a secondary grouping cue, rather than as the main way of showing groups or categories. Shape or clear visual grouping are more reliable signals for relatedness, and using color properties can help reinforce those relationships. Color can add visual weight to relationships, but, in most cases, should only be used to reinforce information that is already communicated in a different way (such as using proximity or similar shapes), since [the combination of color and shape together make for a more noticeable signal than either alone](https://www.nngroup.com/articles/visual-indicators-differentiators/).

![Dundas call center dashboard](https://media.nngroup.com/media/editor/2017/06/06/dundas.png)

*This Dundas call-center dashboard uses shape and borders to indicate different categories of data (shape distinguishes calls from web chat, and borders separate out different call-center agents. While color intensity is used in the* Interaction Length *section of the dashboard to indicate overlapping events, this attribute conveys information of secondary importance.*

## Conclusion

Data dashboards are intended to quickly communicate important information without requiring large amounts of time or cognitive resources to interpret. As a result, encoding the most important information in linear charts and graphs enables users to perceive the critical relationships between data before they even fully pay attention to the visualization.

Learn more about data dashboards in our full-day [Application Design for Web and Desktop](https://www.nngroup.com/courses/application-ux/) seminar, and more about human cognition and its impacts on UX in our [Human Mind and Usability](https://www.nngroup.com/courses/human-mind/) seminar.

## References

William S. Cleveland and Robert McGill: “Graphical Perception and Graphical Methods for Analyzing Scientific Data,” *Science*, Vol. 229, No. 4716 (Aug. 30, 1985)

*Perceptual Edge*, “Tapping the Power of Visual Perception,” September 4, 2004 ([link](https://perceptualedge.com/articles/ie/visual_perception.pdf))
