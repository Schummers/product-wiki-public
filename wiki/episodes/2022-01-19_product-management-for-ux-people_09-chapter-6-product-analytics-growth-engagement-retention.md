---
type: source
name: "Product Management for UX People: CHAPTER 6: Product Analytics: Growth, Engagement, Retention"
created: 2026-09-11
published: 2022-01-19
source_type: book
status: processed
url: https://rosenfeldmedia.com/books/product-management-for-ux-people/
author: Christian Crumlish
raw: raw/sources/2022-01-19_product-management-for-ux-people_09-chapter-6-product-analytics-growth-engagement-retention.md
book: "Product Management for UX People"
chapter: "CHAPTER 6: Product Analytics: Growth, Engagement, Retention"
concepts:
  - Analytics
  - Funnel
  - Sustainable Growth
  - User Retention
  - Business Metrics
---

# Product Management for UX People: CHAPTER 6: Product Analytics: Growth, Engagement, Retention

## Summary

This chapter addresses data analysis, a core responsibility of product managers that often feels alien to designers. While many UX practitioners consume data intelligently, most avoid spending the majority of their time analyzing data. Crumlish argues that successful product managers may spend significant time "living in the data"—immersing themselves in daily metrics, dashboards, and exploratory analysis until they develop an intuitive feel for patterns and anomalies. The chapter covers three major areas: funnel optimization (understanding drop-off at each step in a user's process); growth metrics using the AARRR framework (Awareness, Acquisition, Activation, Retention, Referral, Revenue); and two critical cautions about data-driven work. Throughout, Crumlish emphasizes that data is a tool alongside qualitative research, neither inherently good nor evil, but dependent on how it is used.

## Key Takeaways

- **Living in the data** — Successful PMs develop a daily practice of immersing themselves in metrics, setting up alerts for anomalies, and actively interrogating data to find patterns and meaning, rather than passively consuming dashboards. Matt LeMay (co-founder, Sudden Compass) offers a complementary view: "living in your user's reality," remembering that data is a proxy for people and their experiences, not an end in itself.

- **Technical self-sufficiency** — PMs should learn SQL or use no-code tools like Airtable to query databases and manipulate data independently, rather than depending on engineers or analysts to pull specific datasets. This skill is essential because you cannot always wait for a specialist to answer your questions.

- **Instrumentation as a feature requirement** — Adding product analytics hooks to capture user and system events must become part of every feature spec and launch plan, never an afterthought. Once instrumentation becomes a convention, you can measure success for everything you ship from day one.

- **Funnel analysis reveals drop-off patterns** — Funnels show how many users complete each step in a multi-step process; as a rough rule of thumb, you are likely to lose 10% right off the top every time you add another step, though the chapter stresses the drop-off varies greatly and some steps are trivial enough that everyone who completes the previous one completes the next. Looking for anomalous drop-offs at particular steps, versus normal attrition, lets you prioritize where to investigate and improve. You can also monitor funnels over time to see whether experiments are improving conversion rates, and use cohort analysis to compare drop-off across time periods and user segments.

- **The AARRR framework organizes growth levers, and it is Dave McClure's** — Crumlish credits the piratical mnemonic to Dave McClure, an entrepreneur and investor "from the eBay mob", and notes it is a start-up-oriented framing. AARRR is Acquisition, Activation, Retention, Referral, Revenue; the chapter says some pronounce it AAARRR, adding one further A, Awareness, at the top of the hierarchy, and it walks all six in that order. Each can be instrumented as a funnel. On the DAU/WAU/MAU ratios the chapter is explicitly a rule of thumb: DAU/MAU tells you how many days of the month a typical user drops by, 40% is generally considered good and above 50% excellent, "but this will actually vary depending on industry norms". It also warns that counting anyone who shows up as active overstates the case and makes a vanity metric, so the useful definition requires a basket of qualifying events.

- **Quantitative data needs a qualitative reality check, per Lukas Bergstrom** — Lukas Bergstrom, an ex-Google product consultant, makes the point in the chapter that at least some quantitative data needs to be regularly reality-checked with qualitative research.

- **A growth-stage PM's own day closes the chapter** — The "A Day in the Life of a Growth-Stage PM" box is contributed by Janet Brunckhorst, director of product management at Aurora Solar, described in the raw as a growth-stage (series B) start-up. It is her day, not a generic one.

- **Two cautions about metrics** — Avoid "dark metrics" powered by manipulation or deception (e.g., making it hard to cancel a subscription); these harm people in service of short-term business goals. Also guard against proxy metrics becoming ends in themselves: a metric can improve without the underlying goal improving, requiring ongoing validation with qualitative research and other signals.

## Quotes

> I call it 'living in your user's reality.' It's important to remember that data is a proxy for other things—I've seen a lot of product managers spend forever on dashboards but never actually learn directly from their customers.

> At least I've found it helpful to think of the product metrics and qualitative deep dives as opposite poles that I need to always be moving between.

> You can then even compare your ratios of engaged users to active users to see where more lookie-loos can be converted to participants. Ultimately, the more engaged a person is with your product, the more likely you are to retain them in your user base.

## Concepts

- [[Analytics]] — systematic immersion in data and interactive interrogation of metrics to find patterns and drive product decisions.
- [[Funnel]] — a multi-step process through which users drop off at each stage; analyzing and optimizing funnel conversion is a core growth lever.
- [[Sustainable Growth]] — durable user growth built on strong retention, not just acquisition; growth metrics like DAU/MAU and retention cohorts track health.
- [[User Retention]] — the percentage of users who return after initial use, measured by cohorts over time; retention is the foundation of compounding growth.
- [[Business Metrics]] — quantitative signals tracked daily by PMs (North Star metrics, DAU, MAU, etc.) to monitor product health and guide prioritization.
