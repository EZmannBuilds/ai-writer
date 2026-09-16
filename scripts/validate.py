#!/usr/bin/env python3
"""Repository validation for AI Writer.

Checks structure, not literary quality. Run from anywhere:

    python3 scripts/validate.py

Exit code 0 = clean, 1 = errors. Warnings never fail the run.
Requires PyYAML.
"""
import os
import re
import sys
from collections import Counter, defaultdict

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Files that describe past states on purpose. Old names and section numbers are allowed there.
HISTORICAL = {"CHANGELOG.md", "docs/MIGRATION.md", "docs/AUDIT-v0.5.md"}
HISTORICAL_DIRS = ("research/passes/",)

PACK_STAGES = {"front-door", "identity", "genre", "scale", "world", "output"}
PACK_REQUIRED = {
    "id": str, "name": str, "version": str, "stage": str, "pipeline_position": str,
    "purpose": str, "triggers": list, "natural_language_triggers": list,
    "requires": list, "optional_dependencies": list, "conflicts_with": list,
    "stacks_with": list, "inputs": list, "produces": list, "skip_when": list,
    "state_keys": list, "research_basis": str, "behavior_tests": list,
}
LEGACY_TRIGGERS = ["Start Draft", "Start Origin", "Start Tragic Story", "Dark Anime Mode", "Comic Mode"]
CONTRACT_ROWS = ["Invoked by", "When", "Needs", "Produces", "State", "Consumed by", "Skip when", "Tests", "Research"]
FIXTURE_KEYS = ["id", "title", "covers", "input", "expected", "failure", "pass_criteria"]
RESEARCH_FIELDS = ["Source", "Claim", "Derives", "Limitations", "Fidelity"]
STALE = [
    (re.compile(r"AI_Writer_Skill"), "removed duplicate core file"),
    (re.compile(r"manifest\.json"), "removed manifest"),
    (re.compile(r"[A-Z_]+_INSERT\.md|SOURCE_INDEX\.md|SHOW_TELL_ENGINE"), "v0.4 flat filename"),
    (re.compile(r"(?<![\w/])craft/[\w-]+\.md"), "removed craft/ directory"),
    (re.compile(r"research-pass-4\.md"), "moved to research/passes/"),
    (re.compile(r"§\s?\d"), "numbered section reference (use a named anchor)"),
    (re.compile(r"^#{1,6} \d+\.\d+ ", re.M), "v0.5 subsection number left in a heading"),
]

errors, warnings = [], []


def err(path, msg):
    errors.append("%s: %s" % (path, msg))


def warn(path, msg):
    warnings.append("%s: %s" % (path, msg))


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def md_files():
    out = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if not d.startswith(".") or d == ".github"]
        for f in fns:
            if f.endswith(".md"):
                out.append(rel(os.path.join(dp, f)))
    return sorted(out)


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as fh:
        return fh.read()


def strip_fences(text):
    """Return text with fenced code blocks blanked (line count preserved)."""
    out, fence = [], False
    for ln in text.split("\n"):
        if ln.startswith("```"):
            fence = not fence
            out.append("")
            continue
        out.append("" if fence else ln)
    return "\n".join(out)


def split_front_matter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    return text[4:end], text[end + 5:]


def slugify(heading):
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    h = h.replace("`", "").replace("*", "").strip().lower()
    h = re.sub(r"[^\w\- ]", "", h, flags=re.UNICODE)
    return h.replace(" ", "-")


_anchor_cache = {}


def anchors(path):
    if path in _anchor_cache:
        return _anchor_cache[path]
    _, body = split_front_matter(read(path))
    seen, result, dup = Counter(), set(), []
    for ln in strip_fences(body).split("\n"):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*#*$", ln)
        if not m:
            continue
        base = slugify(m.group(2))
        slug = base if seen[base] == 0 else "%s-%d" % (base, seen[base])
        if seen[base] and len(m.group(1)) <= 2:
            dup.append(m.group(2))
        seen[base] += 1
        result.add(slug)
    _anchor_cache[path] = (result, dup)
    return result, dup


def is_historical(p):
    return p in HISTORICAL or p.startswith(HISTORICAL_DIRS)


# --------------------------------------------------------------------------- checks

def check_skill_front_matter():
    fm, _ = split_front_matter(read("SKILL.md"))
    if fm is None:
        return err("SKILL.md", "missing front matter")
    try:
        data = yaml.safe_load(fm)
    except yaml.YAMLError as e:
        return err("SKILL.md", "front matter is not valid YAML: %s" % e)
    for k in ("name", "description", "version", "license"):
        if not data.get(k):
            err("SKILL.md", "front matter missing '%s'" % k)
    if data.get("name") != "ai-writer":
        err("SKILL.md", "front matter name must be 'ai-writer'")
    if len(str(data.get("description", ""))) > 1024:
        err("SKILL.md", "description exceeds 1024 characters")


def check_links(files):
    link_re = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
    for p in files:
        text = strip_fences(split_front_matter(read(p))[1])
        text = re.sub(r"`[^`\n]*`", "", text)
        for m in link_re.finditer(text):
            target = m.group(1)
            if re.match(r"^[a-z]+:", target):
                continue
            path_part, _, frag = target.partition("#")
            if path_part:
                dest = os.path.normpath(os.path.join(os.path.dirname(p), path_part)).replace(os.sep, "/")
            else:
                dest = p
            full = os.path.join(ROOT, dest)
            if not os.path.exists(full):
                err(p, "broken link -> %s" % target)
                continue
            if frag and dest.endswith(".md"):
                if frag not in anchors(dest)[0]:
                    err(p, "missing anchor -> %s" % target)


def check_duplicate_anchors(files):
    for p in files:
        for h in anchors(p)[1]:
            err(p, "duplicate H1/H2 heading anchor: %s" % h)


def check_code_paths(files):
    path_re = re.compile(r"`((?:core|packs|runtime|research|docs|templates|tests|scripts)/[\w./-]+)`")
    for p in files:
        if is_historical(p):
            continue
        for m in path_re.finditer(read(p)):
            target = m.group(1).rstrip("/")
            if "*" in target or "<" in target:
                continue
            full = os.path.join(ROOT, target)
            if not (os.path.exists(full) or os.path.exists(full + ".md")):  # core/<id> names a module
                err(p, "path in code span does not exist: %s" % target)


def check_stale(files):
    for p in files:
        if is_historical(p):
            continue
        text = read(p)
        for pat, why in STALE:
            for m in pat.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                err(p, "line %d: stale reference '%s' (%s)" % (line, m.group(0), why))


def check_yaml_blocks(files):
    block_re = re.compile(r"^```ya?ml[^\n]*\n(.*?)^```", re.M | re.S)
    for p in files:
        for m in block_re.finditer(read(p)):
            try:
                yaml.safe_load(m.group(1))
            except yaml.YAMLError as e:
                line = read(p).count("\n", 0, m.start()) + 1
                err(p, "yaml block at line %d does not parse: %s" % (line, str(e).split("\n")[0]))


def load_packs():
    packs, companions = {}, {}
    pack_dir = os.path.join(ROOT, "packs")
    for f in sorted(os.listdir(pack_dir)):
        if not f.endswith(".md"):
            continue
        p = "packs/" + f
        fm, _ = split_front_matter(read(p))
        if fm is None:
            err(p, "pack file has no front matter")
            continue
        try:
            data = yaml.safe_load(fm) or {}
        except yaml.YAMLError as e:
            err(p, "front matter is not valid YAML: %s" % e)
            continue
        if "pack" in data:
            packs[p] = data["pack"]
        elif "companion" in data:
            companions[p] = data["companion"]
        else:
            err(p, "front matter needs a 'pack:' or 'companion:' block")
    return packs, companions


def core_ids():
    return {f[:-3] for f in os.listdir(os.path.join(ROOT, "core")) if f.endswith(".md")}


def fixture_ids():
    d = os.path.join(ROOT, "tests", "fixtures")
    if not os.path.isdir(d):
        return set()
    return {f.split("-")[0] for f in os.listdir(d) if f.endswith(".yaml")}


def check_packs(packs, companions):
    ids = Counter()
    fixtures = fixture_ids()
    cores = core_ids()
    all_ids = {meta.get("id") for meta in packs.values() if isinstance(meta, dict)}
    for p, meta in packs.items():
        if not isinstance(meta, dict):
            err(p, "'pack' must be a mapping")
            continue
        for k, typ in PACK_REQUIRED.items():
            if k not in meta:
                err(p, "pack metadata missing '%s'" % k)
            elif not isinstance(meta[k], typ):
                err(p, "pack field '%s' should be %s" % (k, typ.__name__))
        for k in meta:
            if k not in PACK_REQUIRED:
                err(p, "unknown pack field '%s'" % k)
        pid = meta.get("id")
        ids[pid] += 1
        if pid and pid != os.path.basename(p)[:-3]:
            err(p, "pack id '%s' must match filename" % pid)
        if meta.get("stage") not in PACK_STAGES:
            err(p, "stage '%s' not in %s" % (meta.get("stage"), sorted(PACK_STAGES)))
        if not meta.get("triggers") and not meta.get("natural_language_triggers"):
            err(p, "pack declares no triggers")
        for field in ("requires", "optional_dependencies", "conflicts_with", "stacks_with"):
            for dep in meta.get(field) or []:
                if isinstance(dep, str) and dep.startswith("core/"):
                    if dep[5:] not in cores:
                        err(p, "%s references unknown core module '%s'" % (field, dep))
                elif dep not in all_ids:
                    err(p, "%s references unknown pack '%s'" % (field, dep))
                if dep == pid:
                    err(p, "%s references itself" % field)
        rb = meta.get("research_basis")
        if rb and not os.path.exists(os.path.join(ROOT, rb)):
            err(p, "research_basis file missing: %s" % rb)
        for t in meta.get("behavior_tests") or []:
            if t not in fixtures:
                err(p, "behavior_tests references unknown fixture '%s'" % t)
        if not meta.get("behavior_tests"):
            err(p, "pack has no behavior_tests")
    for pid, n in ids.items():
        if n > 1:
            err("packs/", "duplicate pack id '%s'" % pid)
    for p, meta in companions.items():
        if not isinstance(meta, dict) or meta.get("of") not in all_ids:
            err(p, "companion 'of' must name an existing pack")
    # conflicts must be symmetric
    by_id = {m.get("id"): m for m in packs.values() if isinstance(m, dict)}
    for pid, m in by_id.items():
        for other in m.get("conflicts_with") or []:
            if other in by_id and pid not in (by_id[other].get("conflicts_with") or []):
                err("packs/%s.md" % pid, "conflicts_with '%s' is not reciprocated" % other)
    # SKILL.md pack table must list exactly the packs
    skill = read("SKILL.md")
    table = set(re.findall(r"^\| \[([\w-]+)\]\(packs/[\w-]+\.md\)", skill, re.M))
    if table != all_ids:
        err("SKILL.md", "pack table %s does not match packs %s" % (sorted(table), sorted(all_ids)))
    # legacy triggers must still be declared
    declared = {t.lower() for m in by_id.values() for t in (m.get("triggers") or [])}
    for t in LEGACY_TRIGGERS:
        if t.lower() not in declared:
            err("packs/", "backward-compatible trigger '%s' is not declared by any pack" % t)
    return by_id


def check_core_contracts():
    fixtures = fixture_ids()
    for f in sorted(os.listdir(os.path.join(ROOT, "core"))):
        if not f.endswith(".md"):
            continue
        p = "core/" + f
        text = read(p)
        rows = dict(re.findall(r"^\| ([A-Z][\w ]+?) \| (.*) \|$", text, re.M))
        for r in CONTRACT_ROWS:
            if r not in rows:
                err(p, "module contract missing row '%s'" % r)
        for t in re.findall(r"\bF\d{2}\b", rows.get("Tests", "")):
            if t not in fixtures:
                err(p, "contract cites unknown fixture %s" % t)
        if len(text.encode()) > 20000:
            warn(p, "module is %d bytes; consider splitting" % len(text.encode()))


def check_fixtures(pack_ids):
    d = os.path.join(ROOT, "tests", "fixtures")
    if not os.path.isdir(d):
        return err("tests/fixtures", "missing")
    cores = core_ids()
    triggers = {}
    for p in [f for f in os.listdir(os.path.join(ROOT, "packs")) if f.endswith(".md")]:
        fm, _ = split_front_matter(read("packs/" + p))
        meta = (yaml.safe_load(fm) or {}).get("pack") if fm else None
        if meta:
            for t in meta.get("triggers") or []:
                triggers[t.lower()] = meta["id"]
    seen = Counter()
    for f in sorted(os.listdir(d)):
        if not f.endswith(".yaml"):
            continue
        p = "tests/fixtures/" + f
        try:
            data = yaml.safe_load(read(p))
        except yaml.YAMLError as e:
            err(p, "does not parse: %s" % e)
            continue
        for k in FIXTURE_KEYS:
            if k not in data:
                err(p, "fixture missing '%s'" % k)
        fid = data.get("id", "")
        seen[fid] += 1
        if not f.startswith(fid + "-"):
            err(p, "filename must start with id '%s-'" % fid)
        for c in data.get("covers") or []:
            kind, _, name = c.partition("/")
            if kind == "core" and name not in cores:
                err(p, "covers unknown core module '%s'" % c)
            elif kind == "packs" and name not in pack_ids:
                err(p, "covers unknown pack '%s'" % c)
            elif kind == "runtime" and not os.path.exists(os.path.join(ROOT, "runtime", name + ".md")):
                err(p, "covers unknown runtime spec '%s'" % c)
            elif kind not in ("core", "packs", "runtime"):
                err(p, "covers entry must be core/, packs/, or runtime/: '%s'" % c)
        route = (data.get("expected") or {}).get("route") or {}
        packs = route.get("packs")
        if packs is not None:
            for pk in packs:
                if pk not in pack_ids:
                    err(p, "expected route names unknown pack '%s'" % pk)
            text = str((data.get("input") or {}).get("request", "")).lower()
            for trig, pk in triggers.items():
                if trig in text and pk not in packs and not route.get("trigger_overridden"):
                    err(p, "request contains trigger '%s' but expected packs omit '%s'" % (trig, pk))
        if not data.get("pass_criteria"):
            err(p, "fixture has no pass_criteria")
    for fid, n in seen.items():
        if n > 1:
            err("tests/fixtures", "duplicate fixture id %s" % fid)


def check_research():
    index = read("research/source-index.md")
    keys = set(re.findall(r"^\| `([\w-]+)` \|", index, re.M))
    dup = [k for k, n in Counter(re.findall(r"^\| `([\w-]+)` \|", index, re.M)).items() if n > 1]
    for k in dup:
        err("research/source-index.md", "duplicate key %s" % k)
    entry_keys = defaultdict(list)
    for sub in ("core", "packs"):
        d = os.path.join(ROOT, "research", sub)
        if not os.path.isdir(d):
            err("research/" + sub, "missing")
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith(".md"):
                continue
            p = "research/%s/%s" % (sub, f)
            text = strip_fences(read(p))
            parts = re.split(r"^### `([\w-]+)`\s*$", text, flags=re.M)
            for i in range(1, len(parts), 2):
                key, body = parts[i], parts[i + 1].split("\n## ")[0]
                entry_keys[key].append(p)
                if key not in keys:
                    err(p, "entry `%s` is not in research/source-index.md" % key)
                for field in RESEARCH_FIELDS:
                    if not re.search(r"^- \*\*%s:\*\*" % field, body, re.M):
                        err(p, "entry `%s` missing '%s'" % (key, field))
                fid = re.search(r"^- \*\*Fidelity:\*\*\s*(\w+)", body, re.M)
                if fid and fid.group(1) not in ("exact", "approximate", "conceptual", "convention", "design"):
                    err(p, "entry `%s` fidelity must be exact|approximate|conceptual|convention|design" % key)
    # every citation must resolve
    for p in md_files():
        if is_historical(p):
            continue
        text = re.sub(r"`[^`\n]*`", "", strip_fences(read(p)))
        for k in re.findall(r"\[@([\w-]+)\]", text):
            if k not in keys:
                err(p, "citation [@%s] not in research/source-index.md" % k)
    for k in keys:
        if k not in entry_keys:
            warn("research/source-index.md", "key `%s` has no detailed entry" % k)


RESEARCH_CLAIM = re.compile(
    r"\bresearch (?:found|shows|suggests|on)\b|inspired by research|replication work|\bstudies (?:show|found)\b|\bthe study\b",
    re.I)


def check_uncited_claims():
    """A section that speaks of research findings must cite a source key."""
    for sub in ("core", "packs"):
        for f in sorted(os.listdir(os.path.join(ROOT, sub))):
            if not f.endswith(".md"):
                continue
            p = "%s/%s" % (sub, f)
            text = strip_fences(split_front_matter(read(p))[1])
            for section in re.split(r"^## ", text, flags=re.M)[1:]:
                title = section.split("\n", 1)[0]
                if RESEARCH_CLAIM.search(section) and not re.search(r"\[@[\w-]+\]", section):
                    err(p, "section '%s' cites research without a [@key]" % title)


def check_templates():
    base = os.path.join(ROOT, "templates", "workspace")
    for dp, _, fns in os.walk(base):
        for f in fns:
            if f.endswith(".yaml"):
                path = os.path.join(dp, f)
                try:
                    with open(path, encoding="utf-8") as fh:
                        yaml.safe_load(fh)
                except yaml.YAMLError as e:
                    err(rel(path), "template does not parse: %s" % str(e).split("\n")[0])


def main():
    files = md_files()
    check_skill_front_matter()
    check_links(files)
    check_duplicate_anchors(files)
    check_code_paths(files)
    check_stale(files)
    check_yaml_blocks(files)
    packs, companions = load_packs()
    by_id = check_packs(packs, companions)
    check_core_contracts()
    check_fixtures(set(by_id))
    check_research()
    check_uncited_claims()
    check_templates()
    import subprocess
    if subprocess.call([sys.executable, os.path.join(ROOT, "scripts", "build_source_index.py"), "--check"]):
        err("research/source-index.md", "stale; run scripts/build_source_index.py")
    for w in warnings:
        print("warning: " + w)
    for e in errors:
        print("error: " + e)
    print("\n%d markdown files, %d packs, %d errors, %d warnings"
          % (len(files), len(by_id), len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
