"""Apply the stage 2 merge map to every record.

- Rewrites frontmatter `concepts:` lists (merge + dedupe, order kept).
- Retargets `[[wikilinks]]` in bodies (all records, French legacy included:
  link structure is not content).
- Singleton absorption: a candidate not in the map is matched
  case-insensitively and singular/plural against the canonical set; on match
  it is merged too.

Usage: python3 stage2/apply_merge.py [--write] [--only SUBSTR]

--only restricts the pass to records whose basename contains SUBSTR (a book
slug) and layers merge_map.BOOK_MERGES over MERGES for that pass. The
singleton absorption then still counts citations over the whole corpus.
"""

import os, re, sys, yaml, collections
sys.path.insert(0, "stage2")
from merge_map import MERGES as _M1, BOOK_MERGES as _MB
from singleton_map import SINGLETON_MERGES as _M2
ONLY = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else ""
MERGES = {**_M1, **_M2, **(_MB if ONLY else {})}
# chain resolution: alias of alias collapses to the final target
for _k in list(MERGES):
    _v, _seen = MERGES[_k], set()
    while _v in MERGES and MERGES[_v] != _v and _v not in _seen:
        _seen.add(_v); _v = MERGES[_v]
    MERGES[_k] = _v

EP = "wiki/episodes"
WRITE = "--write" in sys.argv

# Canonical set = every merge target + every candidate that stays itself.
def load_candidates():
    c = collections.Counter()
    for f in os.listdir(EP):
        if not f.endswith(".md"): continue
        t = open(f"{EP}/{f}").read()
        m = re.match(r"\A---\n(.*?)\n---\n", t, re.DOTALL)
        if not m: continue
        try: meta = yaml.safe_load(m.group(1)) or {}
        except Exception: continue
        for x in (meta.get("concepts") or []): c[str(x).strip()] += 1
    return c

cand = load_candidates()
# Singletons are NOT canonical: they must earn identity via >=2 citations,
# an existing page, or absorption into a canonical name.
canonical = set(MERGES.values()) | {k for k, v in cand.items()
                                    if k not in MERGES and v >= 2}
# existing concept pages count as canonical names too
for f in os.listdir("wiki/concepts"):
    if f.endswith(".md"): canonical.add(f[:-3])

# case/plural lookup for singleton absorption
def keyize(s):
    k = s.strip().lower()
    if k.endswith("ies"): k = k[:-3] + "y"
    elif k.endswith("s") and not k.endswith("ss"): k = k[:-1]
    return k

canon_by_key = {}
for c_ in sorted(canonical):
    canon_by_key.setdefault(keyize(c_), c_)

def resolve(name):
    name = name.strip()
    if name in MERGES: return MERGES[name]
    if name in canonical: return name
    hit = canon_by_key.get(keyize(name))
    return hit if hit else name


BULLET_RE = re.compile(r"^- \[\[(.+?)\]\](.*)$")


def merge_concept_bullets(body):
    """Join `## Concepts` bullets that now name the same concept.

    A merge can send two candidates of one record onto one canonical name.
    The frontmatter list dedupes, the bullets do not: the record ends up with
    the same `[[Name]]` twice, which is what had to be repaired by hand across
    133 records on 2026-09-09. First occurrence keeps its position; the later
    explanations are appended to it, separated by "; ".
    """
    i = body.find("\n## Concepts")
    if i < 0:
        return body
    # The section stops at the next heading. Without this bound the scan ran
    # to end of file, so a bullet in a later section would be folded into a
    # concept bullet and its own section left empty: silent data loss in a
    # --write path. No record has a section after `## Concepts` today, which
    # is the only reason it never fired.
    j = body.find("\n## ", i + 1)
    if j < 0:
        j = len(body)
    head, section, rest_of_body = body[:i], body[i:j], body[j:]
    out, index = [], {}
    for line in section.split("\n"):
        m = BULLET_RE.match(line)
        if not m:
            out.append(line)
            continue
        name, tail_of_line = m.group(1).strip(), m.group(2)
        if name in index:
            tail = (tail_of_line.split("—", 1)[-1].strip() if "—" in tail_of_line
                    else tail_of_line.strip())
            if tail:
                prev = out[index[name]].rstrip()
                # One trailing period, never an ellipsis: rstrip(".") ate all
                # of them and turned "first..." into "first".
                if prev.endswith(".") and not prev.endswith(".."):
                    prev = prev[:-1]
                # A first bullet with no explanation yet takes the template's
                # separator rather than a bare "; " glued to the wikilink.
                sep = " — " if prev == f"- [[{name}]]" else "; "
                # Case is left alone: lowercasing the first word corrupts a
                # proper noun ("Greever explores...").
                out[index[name]] = f"{prev}{sep}{tail}"
            continue
        index[name] = len(out)
        out.append(f"- [[{name}]]{tail_of_line}")
    return head + "\n".join(out) + rest_of_body


# apply
auto_absorbed = {}
collapsed = []
changed_files = 0
post = collections.Counter()
for f in sorted(os.listdir(EP)):
    if not f.endswith(".md"): continue
    if ONLY and ONLY not in f: continue
    path = f"{EP}/{f}"
    t = open(path).read()
    m = re.match(r"\A---\n(.*?)\n---\n", t, re.DOTALL)
    if not m: continue
    try: meta = yaml.safe_load(m.group(1)) or {}
    except Exception: continue
    old = [str(x).strip() for x in (meta.get("concepts") or [])]
    if not old:
        continue
    new, seen = [], set()
    for o in old:
        r = resolve(o)
        if r != o and o not in MERGES and o not in canonical:
            auto_absorbed[o] = r
        if r in seen:
            # Two candidates of the same record collapse onto one name. The
            # frontmatter dedupes below, but the `## Concepts` bullets would
            # stay duplicated (133 records had to be repaired by hand on
            # 2026-09-09). merge_concept_bullets() joins them; it is reported
            # here so the decision is visible before --write.
            collapsed.append((f, o, r))
            continue
        seen.add(r); new.append(r)
    for n in new: post[n] += 1
    if new == old:
        continue
    changed_files += 1
    if WRITE:
        # rewrite frontmatter concepts block
        fm = m.group(1)
        block = "concepts:\n" + "\n".join(f'  - "{n}"' for n in new)
        fm2 = re.sub(r"concepts:\n(?:  - .*\n?)*", block + "\n", fm)
        body = t[m.end():]
        # retarget wikilinks
        def sub_link(mm):
            return f"[[{resolve(mm.group(1).strip())}]]"
        body = re.sub(r"\[\[(.*?)\]\]", sub_link, body)
        body = merge_concept_bullets(body)
        open(path, "w").write(f"---\n{fm2.rstrip()}\n---\n{body}")

print(f"records touches: {changed_files}")
print(f"singletons auto-absorbes: {len(auto_absorbed)}")
if collapsed:
    print(f"bullets ## Concepts fusionnes: {len(collapsed)} "
          "(deux candidats du meme record vers un seul nom)")
    for f_, o_, r_ in collapsed[:20]:
        print(f"  {f_}: {o_} -> {r_}")
for k, v in sorted(auto_absorbed.items())[:20]: print(f"  {k} -> {v}")
print(f"\nconcepts post-fusion: {len(post)}")
print(f"  >=5 sources: {sum(1 for v in post.values() if v>=5)}")
print(f"  2-4 sources: {sum(1 for v in post.values() if 2<=v<5)}")
print(f"  1 source:    {sum(1 for v in post.values() if v==1)}")
print("\ntop 15:")
for k, v in post.most_common(15): print(f"  {v:4d}  {k}")
if WRITE and not ONLY:
    with open("stage2/post_merge_counts.txt", "w") as f:
        for k, v in sorted(post.items(), key=lambda kv: (-kv[1], kv[0])):
            f.write(f"{v}\t{k}\n")
