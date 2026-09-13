"""Stage 0 scraper for the Nielsen Norman Group corpus (CLAUDE.md, "Pipeline").

Reads the sitemap, applies the topic filter (CONTEXT.md: published 2016+ and at
least one retained topic), and writes one raw file per retained article to
raw/sources/. Pure script, no LLM.

Resumable: an article whose output file exists is skipped, and every decision
is appended to nngroup_scrape_log.csv, so a crashed run restarts where it
stopped. Polite by design: one page fetch per article, 2s pause between
requests.

Usage:
    .venv/bin/python fetch_nngroup.py [--limit N] [--dry-run]
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import unicodedata
import urllib.request
from datetime import date

from bs4 import BeautifulSoup, NavigableString

SITEMAP_URL = "https://www.nngroup.com/sitemap.xml"
OUTPUT_DIR = "raw/sources"
LOG_FILE = "nngroup_scrape_log.csv"
MIN_PUBLISHED = "2016-01-01"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
PAUSE_SECONDS = 0.5

# Topic filter, decided 2026-07-30 (see docs/adr/ and CLAUDE.md). An article is
# retained when at least one of its topics is in INCLUDE. An article with no
# detectable topic is retained if its date passes — better a stray article in
# raw/ than a silent hole in the corpus.
INCLUDE = {
    # UX research & testing
    "research-methods", "user-testing", "personas", "customer-journeys",
    "analytics-and-metrics", "eyetracking", "heuristic-evaluation",
    # Interaction design & UI patterns
    "interaction-design", "design-patterns", "human-computer-interaction",
    "applications", "mobile-and-tablet-design", "visual-design", "prototyping",
    # Information architecture & navigation
    "information-architecture", "navigation", "search",
    # AI
    "ai",
    # Usability & psychology
    "web-usability", "accessibility", "psychology-and-ux", "behavior-patterns",
    "persuasive-design",
    # Process & ideation
    "ux-design-process", "ux-ideation",
    # Careers
    "careers-ux",
    # Email/newsletter design (explicitly retained)
    "email",
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def article_urls():
    xml = fetch(SITEMAP_URL)
    urls = re.findall(r"<loc>(https://www\.nngroup\.com/articles/[^<]+)</loc>", xml)
    seen, ordered = set(), []
    for u in urls:
        if u.rstrip("/") in seen:
            continue
        seen.add(u.rstrip("/"))
        ordered.append(u)
    return ordered


def json_ld(soup):
    for tag in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(tag.string or "")
        except (json.JSONDecodeError, TypeError):
            continue
        items = data if isinstance(data, list) else [data]
        for item in items:
            if isinstance(item, dict) and item.get("datePublished"):
                return item
    return {}


def to_markdown(node, depth=0):
    """Minimal HTML→Markdown for the article body. Keeps structure, drops
    layout. Good enough for raw material that a model will read."""
    parts = []
    for child in node.children:
        if isinstance(child, NavigableString):
            text = re.sub(r"\s+", " ", str(child))
            if text.strip():
                parts.append(text)
            continue
        tag = child.name
        if tag in ("script", "style", "nav", "aside", "form", "iframe"):
            continue
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            parts.append(f"\n\n{'#' * level} {child.get_text(' ', strip=True)}\n\n")
        elif tag == "p":
            parts.append("\n\n" + to_markdown(child, depth).strip() + "\n\n")
        elif tag in ("ul", "ol"):
            items = []
            for i, li in enumerate(child.find_all("li", recursive=False), 1):
                bullet = "-" if tag == "ul" else f"{i}."
                items.append(f"{'  ' * depth}{bullet} {to_markdown(li, depth + 1).strip()}")
            parts.append("\n\n" + "\n".join(items) + "\n\n")
        elif tag == "blockquote":
            inner = to_markdown(child, depth).strip().replace("\n", "\n> ")
            parts.append(f"\n\n> {inner}\n\n")
        elif tag == "a":
            text = child.get_text(" ", strip=True)
            href = child.get("href", "")
            if href.startswith("/"):
                href = "https://www.nngroup.com" + href
            parts.append(f"[{text}]({href})" if text else "")
        elif tag in ("strong", "b", "em", "i"):
            # Whitespace at the edge of an emphasis span belongs to the
            # sentence, not to the marker: stripping it glues words together
            # ("should be to**not fragment**").
            inner = re.sub(r"\s+", " ", child.get_text(" "))
            lead = " " if inner[:1].isspace() else ""
            trail = " " if inner[-1:].isspace() else ""
            inner = inner.strip()
            if not inner:
                continue
            mark = "**" if tag in ("strong", "b") else "*"
            parts.append(f"{lead}{mark}{inner}{mark}{trail}")
        elif tag == "img":
            alt = child.get("alt", "").strip()
            parts.append(f"\n\n![{alt}]({child.get('src', '')})\n\n" if alt else "")
        elif tag == "table":
            parts.append("\n\n" + child.get_text(" | ", strip=True) + "\n\n")
        else:
            parts.append(to_markdown(child, depth))
    return "".join(parts)


def slugify(url):
    slug = url.rstrip("/").rsplit("/", 1)[-1]
    slug = unicodedata.normalize("NFKD", slug).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9-]", "", slug.lower()) or "article"


def already_logged():
    done = set()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, newline="", encoding="utf-8") as f:
            for row in csv.reader(f):
                if row:
                    done.add(row[0])
    return done


def log(url, outcome, detail=""):
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([url, outcome, detail])


def process(url, dry_run):
    html = fetch(url)
    soup = BeautifulSoup(html, "html.parser")

    meta = json_ld(soup)
    published = (meta.get("datePublished") or "")[:10]
    if not published:
        log(url, "skip", "no-publish-date")
        return "skip"
    if published < MIN_PUBLISHED:
        log(url, "skip", f"too-old:{published}")
        return "skip"

    topics = sorted({
        m.group(1)
        for a in soup.find_all("a", href=True)
        if (m := re.match(r"^/topic/([a-z0-9-]+)/$", a["href"]))
    })
    if topics and not (set(topics) & INCLUDE):
        log(url, "skip", "topic:" + ",".join(topics))
        return "skip"

    title = (soup.find("h1") or soup.find("title")).get_text(" ", strip=True)
    author = meta.get("author", "")
    if isinstance(author, list):
        author = ", ".join(a.get("name", "") if isinstance(a, dict) else str(a)
                           for a in author)
    elif isinstance(author, dict):
        author = author.get("name", "")

    body_el = soup.find(class_="article-body") or soup.find("article")
    if body_el is None:
        log(url, "error", "no-article-body")
        return "error"
    body = re.sub(r"\n{3,}", "\n\n", to_markdown(body_el)).strip()
    if len(body) < 500:
        log(url, "error", f"body-too-short:{len(body)}")
        return "error"

    out_path = os.path.join(OUTPUT_DIR, f"{published}_{slugify(url)}.md")
    if dry_run:
        print(f"  would write {out_path} ({len(body)} chars, topics={topics})")
        log(url, "dry-run", out_path)
        return "fetched"

    quoted_title = title.replace('"', '\\"')
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(
            "---\n"
            f'title: "{quoted_title}"\n'
            f"date: \"{published}\"\n"
            f"url: \"{url}\"\n"
            f'author: "{author}"\n'
            f"topics: [{', '.join(topics)}]\n"
            "type: article\n"
            "---\n\n"
            + body + "\n"
        )
    log(url, "fetched", out_path)
    return "fetched"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not os.path.isdir(OUTPUT_DIR):
        sys.exit(f"Run me from the vault root: {OUTPUT_DIR} not found.")

    urls = article_urls()
    done = already_logged()
    todo = [u for u in urls if u not in done]
    print(f"sitemap: {len(urls)} articles, already handled: {len(urls) - len(todo)}, to do: {len(todo)}")
    if args.limit:
        todo = todo[: args.limit]

    tally = {}
    for i, url in enumerate(todo, 1):
        try:
            outcome = process(url, args.dry_run)
        except Exception as e:  # keep the run alive, log, move on
            log(url, "error", repr(e)[:200])
            outcome = "error"
        tally[outcome] = tally.get(outcome, 0) + 1
        if i % 25 == 0 or i == len(todo):
            print(f"[{i}/{len(todo)}] {tally}")
        time.sleep(PAUSE_SECONDS)

    print("done:", tally)


if __name__ == "__main__":
    main()
