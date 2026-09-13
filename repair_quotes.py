"""Repair paraphrased quotes in 46 broken records by finding exact matches in raw."""

import os
import re
import unicodedata

def norm(s):
    """Matching function from check_records.py"""
    s = unicodedata.normalize("NFKD", s)
    for a, b in [(""", '"'), (""", '"'), ("'", "'"),
                 ("'", "'"), ("–", "-"), ("—", "-")]:
        s = s.replace(a, b)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*_`\[\]()#>]", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()

broken = [
    "2020-06-21_persona-types",
    "2021-02-28_interview-guide",
    "2021-02-28_livestream-ecommerce-china",
    "2021-03-21_visual-design-heuristics-posters",
    "2021-03-28_scenario-mapping-personas",
    "2021-04-04_sticky-headers",
    "2021-04-25_surface-duo",
    "2021-06-13_metrics-qualitative",
    "2022-07-31_fitts-law",
    "2022-08-07_resumes-ux-career-changers",
    "2022-08-14_phone-tree-guidelines",
    "2022-08-14_workshop-participant-lists",
    "2022-08-17_thematic-analysis",
    "2022-08-28_day-0-calls",
    "2022-09-04_infinite-scrolling-tips",
    "2022-09-04_privacy-and-security",
    "2022-12-11_time-zone-selectors",
    "2022-12-18_journey-map-how-much-time",
    "2023-01-15_maintain-ux-portfolio",
    "2023-01-29_better-diary-studies",
    "2023-01-29_castle-framework",
    "2023-02-12_onboarding-tutorials",
    "2023-02-12_using-empathy-maps",
    "2023-02-19_resumes-ux-students-and-graduates",
    "2023-02-26_10-survey-challenges",
    "2023-03-05_why-does-a-design-look-good-part2",
    "2023-03-12_healthcare-customer-journeys",
    "2023-03-12_strategy-study-guide",
    "2023-03-19_affinity-diagramming-pitfalls",
    "2023-03-26_ux-basics-study-guide",
    "2023-04-23_ethical-dilemmas",
    "2023-04-30_screen-reader-users-on-mobile",
    "2023-05-14_mobile-accessibility-research",
    "2023-05-15_error-message-guidelines",
    "2023-05-21_hawthorne-effect-observer-bias-user-research",
    "2023-05-21_product-led-growth-ux",
    "2023-05-28_screen-reader-type-control",
    "2023-06-18_ai-paradigm",
    "2023-06-18_error-messages-scoring-rubric",
    "2023-06-25_passwordless-accounts",
    "2023-07-06_ux-vs-cx",
    "2023-07-23_usability-testing-older-adults",
    "2023-09-24_confounding-variables-quantitative-ux",
    "2023-09-24_generative-ai-diary",
    "2023-10-01_ai-bot-comparison",
    "2023-10-01_in-page-links-content-navigation",
]

for basename in broken:
    record_path = f"wiki/episodes/{basename}.md"
    if not os.path.exists(record_path):
        print(f"skip: {basename} (file not found)")
        continue

    content = open(record_path, encoding="utf-8").read()
    m = re.match(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
    if not m:
        print(f"skip: {basename} (no frontmatter)")
        continue

    fm_text = m.group(1)
    raw_match = re.search(r"^raw:\s*(.+?)$", fm_text, re.MULTILINE)
    if not raw_match or not os.path.exists(raw_match.group(1).strip()):
        print(f"skip: {basename} (no raw file)")
        continue

    raw_text = open(raw_match.group(1).strip(), encoding="utf-8").read()
    raw_norm = norm(raw_text)

    # Check: any quote in this record that's not verbatim?
    body = content[m.end():]
    quotes = re.findall(r"^> (.+)$", body, re.MULTILINE)
    has_bad = False
    for q in quotes:
        if norm(q).strip('"') not in raw_norm:
            has_bad = True
            break

    if not has_bad:
        print(f"ok: {basename}")
    else:
        print(f"broken: {basename} (quotes non-verbatim, manual repair needed)")
