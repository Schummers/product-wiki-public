"""One-shot normalisation of the concept layer (SCHEMA.md + ADR 0002).

Three things at once, because they cannot be done independently:

1. Every legacy concept name maps to one canonical English name. Several legacy
   names collapse into a single canonical concept (`LLM`, `LLM (Large Language
   Model)`, `Large Language Model (LLM)` were three files for one idea).
2. Records are rewritten to point at canonical names, in frontmatter and in the
   `## Concepts` body section.
3. Concept pages are regenerated from the records. Safe because every legacy
   page was an empty stub: a heading, two "À compléter" placeholders and a list
   of episodes. The list is what gets rebuilt, from the records themselves.

Every page comes out `status: stub` — none of them has written content yet.
Promoting to `developed` is stage 2's job, once it actually writes the concept.

Idempotent: re-running maps canonical names to themselves and regenerates the
same pages.
"""

import os
import re
import shutil
import sys
from datetime import date

EPISODES_DIR = "wiki/episodes"
CONCEPTS_DIR = "wiki/concepts"

# legacy name -> (canonical English name, [extra aliases])
# The legacy name is added as an alias automatically when it differs.
MAPPING = {
    "8-point Grid": ("8-Point Grid", []),
    # "/" is a folder separator in Obsidian wikilinks, so the canonical
    # name avoids it and "A/B Testing" lives as an alias.
    "A-B Testing": ("A-B Testing", ["A/B Testing", "AB Testing"]),
    # Frontmatter variants with "/" where the legacy filenames used "-".
    "A/B Testing": ("A-B Testing", []),
    "Design Tokens / Modes": ("Design Token Modes", []),
    "Discovery / Delivery": ("Discovery and Delivery", []),
    "Focus / Deep Work": ("Deep Work", []),
    "Focus / Hover State": ("Hover State", []),
    "Interface Conversationnelle / Chatbot": ("Conversational Interface", []),
    "Website Builder / No-code": ("No-Code Website Builder", []),
    "Wireframing / Idéation sur papier": ("Wireframing", []),
    "API Figma": ("Figma API", []),
    "Accessibilité": ("Accessibility", []),
    "Accessibilité Web": ("Accessibility", ["Web Accessibility"]),
    "Accès progressif à l'information": ("Progressive Disclosure", []),
    "Action Control": ("Action Control", []),
    "Affinity Mapping": ("Affinity Mapping", []),
    "Agent Conversationnel": ("Conversational Agent", []),
    "Agent IA": ("AI Agent", []),
    "App Clips": ("App Clips", []),
    "App Intents": ("App Intents", []),
    "Apple Intelligence Entities": ("Apple Intelligence Entities", []),
    "Architecture modulaire": ("Modular Architecture", []),
    "Atomic Design": ("Atomic Design", []),
    "Audit UX": ("UX Audit", []),
    "Auto-layout": ("Auto Layout", []),
    "Auto-remplissage": ("Autofill", []),
    "Autocomplétion": ("Autocomplete", []),
    "Automatisation": ("Automation", []),
    "Automatisation de contenu": ("Content Automation", []),
    "Benchmark": ("Benchmarking", []),
    "Biais de confirmation": ("Confirmation Bias", []),
    "Biais de validation": ("Confirmation Bias", []),
    "Brag Document": ("Brag Document", []),
    "Brainstorming": ("Brainstorming", []),
    "Brainwriting": ("Brainwriting", []),
    "Business Impact": ("Business Impact", []),
    "Business Metrics": ("Business Metrics", []),
    "CSS Grid": ("CSS Grid", []),
    "Call to Action (CTA)": ("Call to Action", ["CTA"]),
    "Canvas": ("Canvas", []),
    "CarPlay": ("CarPlay", []),
    "Card Sorting (Tri de cartes)": ("Card Sorting", ["Tri de cartes"]),
    "Case Study": ("Case Study", []),
    "Change Management": ("Change Management", []),
    "Charge cognitive": ("Cognitive Load", []),
    "Checkbox": ("Checkbox", []),
    "Churn": ("Churn", ["Churn Rate"]),
    "Cold Calls": ("Cold Calls", []),
    "Cold Start": ("Cold Start", []),
    "Collaboration en temps réel": ("Real-Time Collaboration", []),
    "Component Properties": ("Component Properties", []),
    "Composants Sémantiques": ("Semantic Components", []),
    "Concept Map": ("Concept Map", []),
    "Console de développement": ("Developer Console", []),
    "Content Curation": ("Content Curation", []),
    "Content Generation": ("Content Generation", []),
    "Conversion": ("Conversion", ["Conversion Rate"]),
    "Crazy 8": ("Crazy Eights", ["Crazy 8s"]),
    "Croissance Soutenable": ("Sustainable Growth", []),
    "Cross-device Interaction": ("Cross-Device Interaction", []),
    "Curseur natif": ("Native Cursor", []),
    "Curseur sur mesure": ("Custom Cursor", []),
    "Cycle de vie des appareils": ("Device Lifecycle", []),
    "Dark Pattern": ("Dark Pattern", []),
    "Data Analytics": ("Data Analytics", []),
    "Data-driven Decision": ("Data-Driven Decision", []),
    "Deep Delight": ("Deep Delight", []),
    "Default Focus": ("Default Focus", []),
    "Design Guilds": ("Design Guilds", []),
    "Design Ops": ("DesignOps", []),
    "DesignOps": ("DesignOps", ["Design Ops"]),
    "Design System": ("Design System", []),
    "Design Tokens": ("Design Tokens", []),
    "Design Tokens - Modes": ("Design Token Modes", []),
    "Design to Code": ("Design to Code", []),
    "Discovery": ("Product Discovery", ["Discovery"]),
    "Discovery - Delivery": ("Discovery and Delivery", []),
    "Documentation": ("Product Documentation", ["Documentation"]),
    "Documentation Produit": ("Product Documentation", []),
    "Dot Scoring": ("Dot Voting", ["Dot Scoring"]),
    "Double Diamant": ("Double Diamond", []),
    "Double Diamond": ("Double Diamond", ["Double Diamant"]),
    "Process Double Diamant": ("Double Diamond", []),
    "Déclencheurs contextuels": ("Contextual Triggers", []),
    "Découvrabilité": ("Discoverability", []),
    "Déproductisation": ("Deproductization", []),
    "Développement": ("Software Development", []),
    "Easter Egg": ("Easter Egg", []),
    "Edge Case": ("Edge Case", []),
    "Edge Cases": ("Edge Case", ["Edge Cases"]),
    "Embeddings": ("Embeddings", []),
    "Emotional Design": ("Emotional Design", []),
    "Empty State": ("Empty State", []),
    "Event-Based Analytics": ("Event-Based Analytics", []),
    "Excel Test": ("Excel Test", []),
    "Eye Tracking": ("Eye Tracking", []),
    "Fake Door (Faux point d'entrée)": ("Fake Door", ["Faux point d'entrée"]),
    "Fake door": ("Fake Door", []),
    "Faux positifs": ("False Positives", []),
    "Feedback in-app": ("In-App Feedback", []),
    "In-App Feedback": ("In-App Feedback", ["Feedback in-app"]),
    "Feedback visuel et sonore": ("Visual and Audio Feedback", []),
    "Fenêtre Modale": ("Modal Window", []),
    "Fenêtre Non Modale": ("Non-Modal Window", []),
    "Few-Shot Prompting": ("Few-Shot Prompting", []),
    "Fiabilité et Répétabilité": ("Reliability and Repeatability", []),
    "Figma": ("Figma", []),
    "Figma Design": ("Figma Design", []),
    "Figma Make": ("Figma Make", []),
    "Figma Slots": ("Figma Slots", []),
    "Flatten (Aplatir)": ("Flatten", ["Aplatir"]),
    "Focus - Deep Work": ("Deep Work", []),
    "Focus - Hover State": ("Hover State", []),
    "Founding Product Designer": ("Founding Product Designer", []),
    "Framework EAS": ("EAS Framework", []),
    "Friction Utilisateur": ("User Friction", []),
    "Function Calling": ("Function Calling", []),
    "Funnel": ("Funnel", []),
    "GEO (Generative Engine Optimization)": ("Generative Engine Optimization", ["GEO"]),
    "Generative UI Assets": ("Generative UI Assets", []),
    "Golden Scenario": ("Golden Scenario", []),
    "Génération d'images": ("Image Generation", []),
    "Génération de code": ("Code Generation", []),
    "Heuristiques de Bastien & Scapin": ("Bastien and Scapin Heuristics", []),
    "Hidden Layers": ("Hidden Layers", []),
    "In-page tabs": ("In-Page Tabs", []),
    "Information Inline": ("Inline Information", []),
    "Intelligence Artificielle": ("Artificial Intelligence", ["IA", "AI"]),
    "Intelligence Artificielle en Design": ("AI in Design", []),
    "Intelligence Artificielle générative": ("Generative AI", []),
    "Intent Driven Design": ("Intent-Driven Design", []),
    "Interface Conversationnelle - Chatbot": ("Conversational Interface", ["Chatbot"]),
    "Interface en Langage Naturel": ("Natural Language Interface", []),
    "Interviewer Metrics": ("Interviewer Metrics", []),
    "Itération": ("Iteration", []),
    "Just-in-Time Design": ("Just-in-Time Design", []),
    "Kanban": ("Kanban", []),
    "Keyboard Type": ("Keyboard Type", []),
    "LLM": ("Large Language Model", ["LLM", "LLMs"]),
    "LLM (Large Language Model)": ("Large Language Model", []),
    "LLM (Large Language Models)": ("Large Language Model", []),
    "Large Language Model (LLM)": ("Large Language Model", []),
    "Local LLM": ("Local LLM", []),
    "Layer Management": ("Layer Management", []),
    "Liquid Glass": ("Liquid Glass", []),
    "Liquid Morphing": ("Liquid Morphing", []),
    "Live Activity": ("Live Activity", []),
    "Live concept voting": ("Live Concept Voting", []),
    "Lovable": ("Lovable", []),
    "Low Delight": ("Low Delight", []),
    "MCP (Model Context Protocol)": ("Model Context Protocol", ["MCP"]),
    "Model Context Protocol (MCP)": ("Model Context Protocol", []),
    "MVP": ("Minimum Viable Product", ["MVP"]),
    "MVP (Minimum Viable Product)": ("Minimum Viable Product", []),
    "Magic Button": ("Magic Button", []),
    "Make it pop": ("Make It Pop", []),
    "Memory Usage": ("Memory Usage", []),
    "Micro-prototypage": ("Micro-Prototyping", []),
    "Minimalisme": ("Minimalism", []),
    "Mobile Prototyping": ("Mobile Prototyping", []),
    "Motivational Segmentation": ("Motivational Segmentation", []),
    "Mémoire spatiale": ("Spatial Memory", []),
    "Native Scroll Edge Effect": ("Native Scroll Edge Effect", []),
    "Next.js": ("Next.js", []),
    "Notion": ("Notion", []),
    "Nœud (Node)": ("Node", ["Nœud"]),
    "Object Oriented UX": ("Object-Oriented UX", ["OOUX"]),
    "Onboarding": ("Onboarding", []),
    "Open Source": ("Open Source", []),
    "Opinionated Design": ("Opinionated Design", []),
    "Out of the box": ("Out of the Box", []),
    "Outils No-Code": ("No-Code Tools", []),
    "Overlay": ("Overlay", []),
    "PUE (Power Usage Effectiveness)": ("Power Usage Effectiveness", ["PUE"]),
    "Pass-through": ("Pass-Through", []),
    "Pattern Library": ("Pattern Library", []),
    "Paywall": ("Paywall", []),
    "Perceived Performance": ("Perceived Performance", []),
    "Performance Review": ("Performance Review", []),
    "Pixel Perfect": ("Pixel Perfect", []),
    "Placeholder": ("Placeholder", []),
    "Podcast Format": ("Podcast Format", []),
    "Point d'entrée": ("Entry Point", []),
    "Portfolio": ("Portfolio", []),
    "Post-it trashing": ("Post-It Trashing", []),
    "Priorisation quotidienne": ("Daily Prioritization", []),
    "Proactivité": ("Proactivity", []),
    "Probe testing": ("Probe Testing", []),
    "Product Builder": ("Product Builder", []),
    "Product Delight": ("Product Delight", []),
    "Product Design": ("Product Design", []),
    "Product Discovery": ("Product Discovery", []),
    "Product Market Fit": ("Product-Market Fit", []),
    "Product Market Fit (PMF)": ("Product-Market Fit", ["PMF"]),
    "Product Strategy": ("Product Strategy", []),
    "Productivité": ("Productivity", []),
    "Prompt Engineering": ("Prompt Engineering", []),
    "Proof of Concept (POC)": ("Proof of Concept", ["POC"]),
    "Proof of Thought": ("Proof of Thought", []),
    "Prototypage": ("Prototyping", []),
    "Prototypage IA": ("AI Prototyping", []),
    "Prototypage Rapide": ("Rapid Prototyping", []),
    "Prototype": ("Prototyping", ["Prototype"]),
    "Pré-prompt": ("Pre-Prompt", []),
    "RGPD": ("GDPR", ["RGPD"]),
    "Raccourcis Clavier": ("Keyboard Shortcuts", []),
    "Radio Button": ("Radio Button", []),
    "Recherche Spotlight": ("Spotlight Search", []),
    "Recherche Sémantique": ("Semantic Search", []),
    "Replit": ("Replit", []),
    "Return Key": ("Return Key", []),
    "Search Intent Analysis": ("Search Intent Analysis", []),
    "Session Recording": ("Session Recording", []),
    "Session-Based Analytics": ("Session-Based Analytics", []),
    "Sketching": ("Sketching", []),
    "Solution de contournement": ("Workaround", []),
    "Spatial Computing": ("Spatial Computing", []),
    "Storytelling": ("Storytelling", []),
    "Stratégie d'Entreprise": ("Business Strategy", []),
    "Supabase": ("Supabase", []),
    "Surface Delight": ("Surface Delight", []),
    "Svelte": ("Svelte", []),
    "SwiftUI": ("SwiftUI", []),
    "Tab bar": ("Tab Bar", []),
    "Tap Area": ("Tap Area", []),
    "Task Chunking": ("Task Chunking", []),
    "Taux de churn": ("Churn", ["Taux de churn"]),
    "Taux de conversion": ("Conversion", ["Taux de conversion"]),
    "Temps d'input": ("Input Time", []),
    "Test d'usabilité": ("Usability Testing", []),
    "User Testing": ("Usability Testing", ["User Testing"]),
    "Time Blocking": ("Time Blocking", []),
    "Time to value": ("Time to Value", []),
    "Toggle Switch": ("Toggle Switch", []),
    "Tokens Sémantiques": ("Semantic Tokens", []),
    "Toolbar": ("Toolbar", []),
    "Tracking Plan": ("Tracking Plan", []),
    "Trade-off": ("Trade-Off", []),
    "UX Design": ("UX Design", []),
    "UX Research": ("UX Research", ["User Research"]),
    "User Research": ("UX Research", []),
    "UX Writing": ("UX Writing", []),
    "User Experience (UX)": ("User Experience", ["UX"]),
    "User Flow": ("User Flow", []),
    "User Interface (UI)": ("User Interface", ["UI"]),
    "User Retention": ("User Retention", []),
    "User-Centric AI": ("User-Centric AI", []),
    "User-Centric Design": ("User-Centered Design", ["User-Centric Design"]),
    "Veille Design": ("Design Trend Watching", []),
    "Vibe Coding": ("Vibe Coding", []),
    "Vibe Design": ("Vibe Design", []),
    "Visual Search": ("Visual Search", []),
    "Website Builder - No-code": ("No-Code Website Builder", []),
    "Widgets": ("Widgets", []),
    "Winesurf": ("Windsurf", ["Winesurf"]),
    "Wireframing": ("Wireframing", []),
    "Wireframing - Idéation sur papier": ("Wireframing", ["Idéation sur papier"]),
    "Wow Moment": ("Wow Moment", []),
    "Xcode": ("Xcode", []),
    "Éco-conception": ("Sustainable Design", ["Éco-conception"]),
    "Évaluation Coût-Impact": ("Cost-Impact Evaluation", []),
}

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def canonical(name):
    if name in MAPPING:
        return MAPPING[name][0]
    # Already canonical (re-run), or a name the mapping never saw.
    return name


def aliases_for(canonical_name):
    found = []
    for legacy, (target, extras) in MAPPING.items():
        if target != canonical_name:
            continue
        if legacy != canonical_name and legacy not in found:
            found.append(legacy)
        for extra in extras:
            if extra != canonical_name and extra not in found:
                found.append(extra)
    return found


def yaml_quote(value):
    return '"' + value.replace('"', '\\"') + '"'


def rewrite_records():
    """Point every record at canonical concept names. Returns
    {canonical: [(record_basename, detail_text)]}."""
    usage = {}
    unknown = set()

    for filename in sorted(os.listdir(EPISODES_DIR)):
        if not filename.endswith(".md"):
            continue
        path = os.path.join(EPISODES_DIR, filename)
        with open(path, encoding="utf-8") as f:
            content = f.read()

        m = FM_RE.match(content)
        if not m:
            continue
        block, body = m.group(1), content[m.end():]
        basename = filename[:-3]

        # Frontmatter concepts list, in order, deduplicated after mapping.
        names, in_list = [], False
        out_lines = []
        for line in block.splitlines():
            if re.match(r"^concepts:\s*$", line):
                in_list = True
                out_lines.append(line)
                continue
            if in_list:
                item = re.match(r"^\s*-\s*(.+?)\s*$", line)
                if item:
                    legacy = item.group(1).strip().strip('"').strip("'")
                    legacy = re.sub(r"^\[\[|\]\]$", "", legacy).strip()
                    if legacy not in MAPPING and legacy not in {
                        c for c, _ in MAPPING.values()
                    }:
                        unknown.add(legacy)
                    target = canonical(legacy)
                    if target not in names:
                        names.append(target)
                    continue
                in_list = False
            out_lines.append(line)

        rebuilt = []
        for line in out_lines:
            rebuilt.append(line)
            if re.match(r"^concepts:\s*$", line):
                rebuilt.extend(f"  - {yaml_quote(n)}" for n in names)

        # Body wikilinks, longest legacy name first so a short name never
        # eats a longer one it is a prefix of.
        for legacy in sorted(MAPPING, key=len, reverse=True):
            body = body.replace(f"[[{legacy}]]", f"[[{canonical(legacy)}]]")

        with open(path, "w", encoding="utf-8") as f:
            f.write("---\n" + "\n".join(rebuilt) + "\n---\n" + body)

        # Per-source detail lines, for the concept pages' Sources list.
        details = {}
        for link, text in re.findall(
            r"^\*?\s*-?\s*\[\[(.+?)\]\]\s*[:—-]\s*(.+?)\s*$", body, re.MULTILINE
        ):
            details[canonical(link.strip())] = text.strip()

        for name in names:
            usage.setdefault(name, []).append((basename, details.get(name, "")))

    if unknown:
        print("Legacy concept names absent from MAPPING (left as-is):")
        for name in sorted(unknown):
            print(f"  - {name}")

    return usage


def regenerate_concepts(usage, today):
    if os.path.isdir(CONCEPTS_DIR):
        shutil.rmtree(CONCEPTS_DIR)
    os.makedirs(CONCEPTS_DIR)

    for name in sorted(usage):
        lines = [
            "---",
            "type: concept",
            f"name: {yaml_quote(name)}",
            f"created: {today}",
            f"updated: {today}",
            "status: stub",
            "aliases:",
        ]
        for alias in aliases_for(name):
            lines.append(f"  - {yaml_quote(alias)}")
        lines += [
            "---",
            "",
            f"# {name}",
            "",
            "## Definition",
            "",
            "*Not written yet.*",
            "",
            "## Practice",
            "",
            "*Not written yet.*",
            "",
            "## Sources",
            "",
        ]
        for basename, detail in usage[name]:
            suffix = f" — {detail}" if detail else ""
            lines.append(f"- [[{basename}]]{suffix}")
        lines.append("")

        safe = name.replace("/", "-").replace(":", "-")
        with open(
            os.path.join(CONCEPTS_DIR, f"{safe}.md"), "w", encoding="utf-8"
        ) as f:
            f.write("\n".join(lines))


def main():
    if not os.path.isdir(EPISODES_DIR):
        sys.exit(f"Run me from the vault root: {EPISODES_DIR} not found.")
    today = date.today().isoformat()

    usage = rewrite_records()
    regenerate_concepts(usage, today)

    print(f"records rewritten: {len(os.listdir(EPISODES_DIR))}")
    print(f"concepts: {len(usage)} (was 253 legacy files)")


if __name__ == "__main__":
    main()
