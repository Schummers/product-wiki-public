---
type: concept
name: Data Visualization
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Dashboard Design"
---

# Data Visualization

## Definition

Data visualization in this corpus is the graphical representation of data
through charts, graphs, maps and tables, judged not by how attractive it looks
but by how quickly and accurately an audience can extract the intended meaning
[[2018-08-12_designing-effective-infographics]]. The recommended way to approach
it is the same user-centered process used for an interface: start from the goal
("what point are you trying to make, what do you want the audience to
understand, what action should they take?") and design backwards from there,
while keeping the data honest [[2022-01-30_choosing-chart-types]].

Two ideas do most of the explanatory work across the sources. The first is
perceptual: some visual attributes are processed preattentively — length,
two-dimensional position, colour — and these support fast, accurate reading,
while area and angle do not, which is why bar and line charts outperform pie,
donut and treemap forms [[2017-06-18_dashboards-preattentive]]
[[2019-09-29_treemaps]]. The second is editorial: charts and infographics should
maximise the data-ink ratio, removing anything that does not carry information
[[2022-02-06_clutter-charts]] [[2018-08-12_designing-effective-infographics]]
[[2023-07-23_imagery-in-visual-design]], and then use annotation to say
explicitly what the viewer should look at [[2022-02-13_contrast-charts]]. The
concept also covers non-chart formats: data tables, which win when the task is
precise lookup and comparison [[2022-04-03_data-tables]]
[[2017-09-17_mobile-tables]], and research artifacts such as journey maps and
eyetracking heatmaps [[2017-05-28_customer-journey-mapping-process]]
[[2019-08-18_eyetracking-setup]].

## Practice

### The 3 Cs for better charts

Nielsen Norman Group's framework is three articles, one per C.

**Context.** A single number is meaningless on its own: a 24% completion rate
means nothing until it is compared against a previous year, a competitor
product, a different user group, or another task. People interpret data by
comparison, so the chart's job is to supply the comparison
[[2022-01-30_choosing-chart-types]].

**Clutter-free.** Using Tufte's data-ink ratio, data ink is anything that cannot
be removed without changing the meaning; chartjunk is everything else.
Practical consequences: avoid Excel's default styles with their 3D effects,
gradients, shadows and textures, which distract and can create optical illusions
that distort perception; evaluate axes and grid lines case by case, since they
are essential when values must be read off them and redundant when data labels
already give exact numbers; prefer direct labelling on the series over a legend,
because legends force back-and-forth eye movement and direct labels are also
better for colourblind viewers; and once direct labels are in place, grid lines
often become chartjunk too [[2022-02-06_clutter-charts]].

**Contrast.** Start with everything in grayscale and add colour only to the
values or series that carry your point. Write active titles that state the
finding ("Participants struggled to find past bills") rather than describing the
data ("Success rates by task"), and use the same colour in the title as in the
highlighted value so the two connect. Add callouts for context — a redesign, a
sales spike, an external event — so the context survives if the chart is shared
beyond the presentation. The annotation layer is presented as the single most
important element, on the reasoning that making viewers hunt for the meaning
puts the burden in the wrong place. Two constraints: emphasising a finding is
not the same as manipulating a chart to mislead, and findings that contradict
expectations must not be dropped. Test the chart by showing it to members of the
intended audience and asking them to summarise what it says; if that fails,
return to the three Cs [[2022-02-13_contrast-charts]].

### Choosing a chart type

Guidance converges on a small set of forms:

- **Bar charts** are the most comprehensible for comparing values, because they
  encode quantity as length [[2022-01-30_choosing-chart-types]]
  [[2017-06-18_dashboards-preattentive]]. Use horizontal orientation when labels
  are long, so they need not be abbreviated or rotated, and group paired bars so
  the comparison you care about sits adjacent
  [[2022-01-30_choosing-chart-types]].
- **Line charts** for trends over time, with data-point markers to show when
  collection actually happened [[2022-01-30_choosing-chart-types]].
- **Avoid** stacked bar charts (among the hardest to understand), pie and donut
  charts, bubble charts and any form requiring viewers to judge angle, area or
  volume, unless they add unique value [[2022-01-30_choosing-chart-types]]. Pie
  charts are described as poor at most information-communication tasks apart
  from showing overwhelming disparity in shares
  [[2017-06-18_dashboards-preattentive]].
- **Never 3D.** Three-dimensional rendering distorts the visual features being
  compared [[2017-06-18_dashboards-preattentive]].
- **Colour and shape encode categories, not magnitude.** They are preattentive
  but carry no sense of quantity, so use them to group related items and
  reinforce relationships shown through position or proximity
  [[2017-06-18_dashboards-preattentive]].
- **Pareto charts** combine a bar plot of a metric by category with a cumulative
  percentage line, which makes an uneven distribution immediately visible and
  helps identify the vital few areas worth improving among the trivial many
  [[2021-10-17_pareto-principle]].

### Treemaps: a worked case of the perceptual limits

Treemaps display hierarchical data as nested rectangles whose size is
proportional to a value, with colour encoding a category or a second quantity.
They are good at showing the largest contributors within categories, but area is
not preattentively perceived, so precise comparison requires hovering and
tooltips, which limits their usefulness for decision tasks. They fail on flat
data (where they are equivalent to a pie chart) and on balanced trees where all
items are similar in size, and they overwhelm when there are many items. Design
rules: use varying intensity of a single colour for quantitative values, since
people have no inherent ordering for hues, and reserve multiple colours for
categories; avoid red/green pairings and use colourblind-safe palettes with
redundant signals such as text labels and hover detail; add distinct borders
around top-level categories and high-contrast labels. Sorted bar charts and
scatter plots often serve the same purpose better [[2019-09-29_treemaps]].

### Dashboards

Dashboards communicate critical information at a glance without demanding deep
analysis, and come in two forms: operational, prioritising speed for
time-sensitive decisions, and analytical, supporting thoughtful analysis. Both
need a single-screen, at-a-glance layout, and both should be built out of the
preattentive attributes above [[2017-06-18_dashboards-preattentive]]. Treemaps
can add visual variety to a dashboard but consume space and may need interaction
to be read, so density should follow user need [[2019-09-29_treemaps]].

### Tables

Tables are the right choice when the task is comparison or precise lookup rather
than pattern recognition: adjacent values compare without moving the eyes or
loading working memory, and tables are space-efficient at scale. Four user tasks
define the design — finding records matching criteria, comparing data, viewing
or editing a single row, and acting on records. Concretely: make the first
column a human-readable identifier rather than an auto-generated ID; order
columns by importance to the user and keep related columns adjacent; freeze
headers and the first column once the table exceeds the screen; make hiding and
reordering columns easy while clearly signalling what is hidden; use non-modal
side panels rather than modals for editing a record, so surrounding data stays
visible; and prefer batch actions with checkboxes over per-row action buttons
[[2022-04-03_data-tables]].

On small screens the same table needs additional work. Build a good desktop
table first — the exercise of cutting to meaningful attributes usually improves
it for everyone. Columns must be legible without zooming, which limits how many
fit (a wordy comparison table may only manage two, numeric data more). Stick
column headers so context survives vertical scrolling, and signal horizontal
scrolling with cut-off elements or arrows, which draw attention better than
dots. Give users control over what is shown through filters applied before
display, column toggles, and accordions [[2017-09-17_mobile-tables]].

### Infographics and imagery

An infographic is a multimedia graphic that presents complex information
understandably; unlike a bare data visualization it stands alone as a complete
piece of content, adding narrative, quotes, captions and illustration
[[2018-08-12_designing-effective-infographics]]. Guidance: maximise the data-ink
ratio and present data truthfully with appropriate scaling, indicating sources
and baseline states so readers are not misled; choose readable rather than
decorative fonts that scale; keep a limited palette with enough contrast for
colourblind users, and never use colour as the only distinction; keep
illustrations simple enough to support rather than compete with the message;
watch for distorted scales and unclear hierarchy; and decide between static and
interactive formats according to whether the goal is to make a point or to
enable exploration. Iterate with audience feedback rather than chasing
perfection [[2018-08-12_designing-effective-infographics]].

Placed among the four types of interface imagery (photographs, illustrations,
iconography, data visualizations), visualizations are classed as
information-carrying imagery and should be favoured over decorative stock
photos, which occupy space and are quickly overlooked. The same high data-ink
principle applies: no gratuitous shadows, grid lines or 3D effects
[[2023-07-23_imagery-in-visual-design]].

### Visualization as a research deliverable

Several sources treat the visual artifact as the output of a research process
rather than a chart in a report.

- **Journey maps.** The fifth and final phase of journey mapping is narrative
  visualization: a workshop evolves the draft map from primary research, and a
  polished visual is produced only if the map needs to be shared with
  stakeholders — moving from sticky notes to a stakeholder-facing deliverable
  [[2017-05-28_customer-journey-mapping-process]].
- **Eyetracking.** The method produces three visualization types serving
  different goals and requiring different sample sizes: gazeplots (individual
  fixations) and gaze replays (video of eye movement) give qualitative insight
  with 8–12 participants, while heatmaps aggregating fixation data need roughly
  39 participants to be meaningful [[2019-08-18_eyetracking-setup]].
- **Analytics triage.** The Pareto principle is used to cut through analytics
  overload, with the caveat not to focus exclusively on the top 20% — that risks
  stagnation and overoptimisation of narrow metrics, so bandwidth should be kept
  for the rest of the experience [[2021-10-17_pareto-principle]].

### Mock data for prototypes

Because participants scrutinise unfamiliar data for outliers and
inconsistencies, prototypes need realistic content or the session drifts from
testing the design to questioning the numbers. Generative AI can produce mock
tables and charts if given enough constraint: context (business size, industry,
geography, product type), the volume of the notional full dataset so the
displayed sample is proportionally plausible, and specifications for uniqueness,
fixed values, formatting, ranges and distributions. For charts, describe the
narrative the chart should show, eliminate clutter, emphasise outliers, set
dimensions and request SVG. Verification matters: require the model to show its
calculations and use coding tools for the maths, since hallucinated numbers can
pass a usability test while being wrong. Synthetic data warrants extra caution
in regulated industries [[2024-09-06_ai-data-prototype-testing]].

## Sources (15)

- [[2017-05-28_customer-journey-mapping-process]] — Final phase creates narrative visual communication of journey, moving from sticky-note prototypes to polished stakeholder-facing deliverables.
- [[2017-06-18_dashboards-preattentive]] — Guidance on distinguishing operational and analytical dashboards, and chart type selection based on preattentive processing; linear charts work better than circular or area-based charts for at-a-glance information delivery.
- [[2017-09-17_mobile-tables]] — presenting structured data accessibly on small screens demands clear hierarchy, scent, and user control over what information is displayed.
- [[2018-08-12_designing-effective-infographics]] — the graphical representation of data through charts, graphs, and maps; infographics often contain visualizations but add narrative context and illustrative elements.
- [[2019-08-18_eyetracking-setup]] — Eyetracking produces multiple visualization formats (gazeplots, replays, heatmaps) suitable for different analysis goals and audience sizes.
- [[2019-09-29_treemaps]] — Treemaps are effective for hierarchical data and add visual variety to dashboards but have cognitive limitations and consume space; visualization choice should match user tasks and cognitive processes, with density calibrated to user needs and may require interaction for meaningful interpretation.
- [[2021-10-17_pareto-principle]] — The Pareto chart technique combines bars and cumulative line plots to make imbalanced distributions immediately visible.
- [[2022-01-30_choosing-chart-types]] — Context is essential for meaningful data visualization; numbers require comparison against other numbers for audiences to interpret them correctly.
- [[2022-02-06_clutter-charts]] — Effective data visualization removes chartjunk (unnecessary visual elements) and maximizes data-ink ratio to communicate information efficiently and clearly.
- [[2022-02-13_contrast-charts]] — Adding contrast through color, titles, and callouts guides viewers' attention to key findings; annotation layers are the most important tool for making data communicative.
- [[2022-04-03_data-tables]] — choosing tables over other presentation formats when the primary tasks involve comparison and precise data lookup.
- [[2023-07-23_imagery-in-visual-design]] — Addresses the principle of high data-ink ratios to avoid decorative clutter in infographics.
- [[2024-09-06_ai-data-prototype-testing]] — focuses on creating realistic charts and tables for testing without the effort of manual data curation.
- [[2016-11-04_ux-research_14-chapter-13-making-sense-of-the-mess]] — the chapter covers visualizing data using spreadsheets, pivot tables, and charts, with principles such as using valuable scales (not distorting the range), choosing appropriate chart types (pie charts for parts of a whole, not growth over time), and avoiding embellishments that distract from the data.
- [[2016-11-04_ux-research_15-chapter-14-communicating-insights]] — the chapter catalogs visual artifacts for research: experience maps (for touchpoints over time), personas (for user behaviors and qualities), mind maps (for data point connections), user flows (for single-user actions), swim lanes (for multi-actor workflows), mental models (for user thought and action), severity scales (for issue prioritization), click maps (for user journey within a system), and change logs (for design iteration tracking).
