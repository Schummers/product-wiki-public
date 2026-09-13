"""Stage 2: deterministic concept-page generation (structure, not prose).

For every canonical concept with >=2 sources post-merge, or with an existing
page: (re)write the page with proper frontmatter (aliases folded in from the
merge maps) and a `## Sources` section built from the records' `## Concepts`
bullets. Definition/Practice stay empty on stubs — the writing pass (strong
model) fills them for well-sourced concepts.

Existing pages whose *name* became an alias are deleted; their aliases fold
into the target. Existing aliases in kept pages are preserved.
"""

import os, re, sys, yaml, collections

sys.path.insert(0, "stage2")
from merge_map import MERGES as _M1
from singleton_map import SINGLETON_MERGES as _M2

MERGES = {**_M1, **_M2}
for _k in list(MERGES):
    _v, _seen = MERGES[_k], set()
    while _v in MERGES and MERGES[_v] != _v and _v not in _seen:
        _seen.add(_v); _v = MERGES[_v]
    MERGES[_k] = _v

EP, CO = "wiki/episodes", "wiki/concepts"
TODAY = "2026-07-31"
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)

# 1. Collect, per canonical concept: sources (basename, published, contribution)
per = collections.defaultdict(list)
for f in sorted(os.listdir(EP)):
    if not f.endswith(".md"): continue
    t = open(f"{EP}/{f}").read()
    m = FM_RE.match(t)
    if not m: continue
    try: meta = yaml.safe_load(m.group(1)) or {}
    except Exception: continue
    body = t[m.end():]
    contrib = {}
    sec = re.search(r"## Concepts\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    if sec:
        for line in sec.group(1).splitlines():
            lm = re.match(r"- \[\[(.*?)\]\]\s*[—–-]*\s*(.*)", line.strip())
            if lm: contrib.setdefault(lm.group(1).strip(), lm.group(2).strip())
    base = f[:-3]
    pub = str(meta.get("published", ""))
    for c in (meta.get("concepts") or []):
        c = str(c).strip()
        per[c].append((pub, base, contrib.get(c, "")))

# 2. Existing pages: aliases to preserve; pages to fold (name is now an alias)
existing_aliases, fold = {}, []
for f in sorted(os.listdir(CO)):
    if not f.endswith(".md"): continue
    name = f[:-3]
    t = open(f"{CO}/{f}").read()
    m = FM_RE.match(t)
    al = []
    if m:
        try: al = [str(a) for a in ((yaml.safe_load(m.group(1)) or {}).get("aliases") or [])]
        except Exception: pass
    if name in MERGES:
        fold.append((name, MERGES[name], al))
    else:
        existing_aliases[name] = al

# aliases per canonical: merge-map keys used in corpus + folded pages' names/aliases
alias_map = collections.defaultdict(set)
corpus_names = set()
for c, lst in per.items(): corpus_names.add(c)
for k, v in MERGES.items():
    alias_map[v].add(k)
for name, target, al in fold:
    alias_map[target].add(name)
    alias_map[target].update(al)

# 3. Decide the page set: >=2 sources, or an existing kept page
pages = {c for c, lst in per.items() if len(lst) >= 2} | set(existing_aliases)

written = folded = 0
for name, target, _ in fold:
    os.remove(f"{CO}/{name}.md"); folded += 1

for c in sorted(pages):
    lst = sorted(per.get(c, []))
    n = len(lst)
    aliases = sorted((alias_map.get(c, set()) | set(existing_aliases.get(c, []))) - {c})
    fm = ["---", "type: concept", f"name: {c}" if ":" not in c else f'name: "{c}"',
          f"created: {TODAY}", f"updated: {TODAY}", "status: stub"]
    if aliases:
        fm.append("aliases:")
        fm += [f'  - "{a}"' for a in aliases]
    fm.append("---")
    src = [f"- [[{b}]]" + (f" — {t}" if t else "") for _, b, t in lst]
    body = [f"# {c}", "", "## Definition", "",
            "_Stub — to be written by the concept stage._", "",
            f"## Sources ({n})", ""] + src + [""]
    open(f"{CO}/{c}.md", "w").write("\n".join(fm) + "\n\n" + "\n".join(body))
    written += 1

print(f"pages ecrites: {written}, pages fondues (alias): {folded}")
print(f"concepts sans page (1 source, non absorbes): {len([c for c in per if c not in pages])}")
