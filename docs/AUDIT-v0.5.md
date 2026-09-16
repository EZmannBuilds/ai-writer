# Baseline audit: v0.5

The state of the repository before the v0.6 refactor, recorded 2026-09-16 at commit `d5d6d69` (tagged `v0.5-baseline`). Kept as a historical record; old filenames and section numbers are intentional here.

---

## Files

| File | Bytes | Role |
|---|---:|---|
| `SKILL.md` | 93,549 | Entire core system, §0–§103, plus four pack pointer sections |
| `packs/tragic-anime-engine.md` | 21,825 | Pack |
| `packs/origin-forge.md` | 16,465 | Pack |
| `packs/draft-starter.md` | 15,254 | Pack |
| `packs/comic-panel-writer.md` | 14,261 | Pack |
| `packs/tragic-anime-lenses.md` | 4,267 | Companion reference |
| `research/source-index.md` | 6,620 | v0.4 craft sources only |
| `research/research-pass-4.md` | 5,969 | v0.4 craft synthesis |
| `research/benchmark.md` | 1,858 | v0.3 vs v0.4 comparison |
| `craft/*.md` (9 files) | 1,010–2,933 each | Condensed quick cards |
| `README.md`, `CHANGELOG.md`, `LICENSE.md` | — | Docs |

Total: 207,658 bytes. `SKILL.md` was 45% of the skill and loaded on every request.

## Section map of `SKILL.md`

287 headings. Top-level sections in file order:

```text
0.0 layout · 0 Purpose · 1 Governing Principles (1.1–1.4) · 2 Operating Modes
  (FAST SCENE, SHORT STORY, LONG-FORM, CRITIC, RESEARCH-GROUNDED, + 3 pack pointers)
3–50 in order
55–81 in order                  ← §51–54 missing here
51 Research Basis               ← out of order
52 Known Translation Limits     ← out of order
82 Legacy v0.3 Quality Gate     ← after 52
83 Legacy Compact Runtime
84–103 v0.4 craft layer
```

**Numbering defects:** §50 is followed by §55; §53 and §54 never existed; §51–52 appear after §81; §82–83 appear after §52. Subsections carried their own numbers (10.1–10.3, 18.1–18.2, 85.1–85.6).

## Cross-references

- Numbered: `§3`, `§3–4`, `§41`, `§84–§103`, in `SKILL.md` and in `packs/draft-starter.md`, `packs/origin-forge.md`.
- File: `SKILL.md` → every pack and `research/source-index.md`; packs → each other (Origin Forge ↔ Comic Panel Writer; Tragic → both and lenses); `research-pass-4.md` → `source-index.md`; README and CHANGELOG → every file.
- Every numbered reference would break when sections moved.

## Duplicated concepts

| Concept | Locations |
|---|---|
| Show/tell | §85, §41, `craft/show-tell.md` |
| Scene craft | §39, §86, §87, `craft/scene-craft.md` |
| Dialogue/subtext | §40, §91, `craft/dialogue-subtext.md` |
| POV/psychic distance | §90, §56 (different sense), `craft/pov-psychic-distance.md` |
| Exposition | §88, §94, `craft/exposition-backstory.md` |
| Mistakes | §97, `craft/common-mistakes.md` |
| Question bank | §100, `craft/question-bank.md` |
| Revision passes | §101 (11 passes), `craft/revision-passes.md` (12 — adds Exposition) |
| StoryScope | §33, §51, `craft/storyscope-anti-defaults.md` |
| Quality gates | §82 (v0.3), §102 (v0.4) |
| Compact runtime | §81, §83, §103 |
| Relationship state | §43, §76 (social), Tragic ensemble map |
| Reveal/information ledgers | §29, §92, Tragic reveal ledger |
| Genre status | §77 said horror, romance, tragedy, and mystery were unresearched — stale once the Tragic pack shipped |

## Load classification

**Always loaded (kernel):** purpose, governing principles, mode summary, routing, provenance rule, pack and module index, guardrails, compact runtime.

**On demand:** everything else — character simulation, memory, outlining, reader state, suspense/curiosity/surprise, information architecture, dialogue, POV, prose, revision, critics, endings, question bank, research basis, benchmark.

## Pack behavior at baseline

| Pack | Trigger | Position | Produces | Asks | Notable rules | Gaps |
|---|---|---|---|---|---|---|
| Draft Starter | "Start Draft", loose seed | Before Intent Lock | Draft Brief (with confirmed / delegated / proposal / unresolved lists) | 3–5 per round, ≤ 2 rounds | "You decide" → delegation; never silently canonize | `interview_state` schema from the original pack never integrated; no research notes |
| Origin Forge | "Start Origin" | After Draft Starter | Origin Brief with provenance | 3–5 | Disruption ≠ chosen crossing; split responsibility; trauma/diagnosis guardrail; military module | Research notes from the original pack not in the repo |
| Tragic Anime Engine | "Start Tragic Story", "Dark Anime Mode", + 6 phrases | After Origin Forge | Tragic brief, Hope Reserve, consequence/reveal ledgers, death/power/ensemble cards | ≤ 3–5 | Not a kill button; Death Necessity Test; survival alternative; no imitation | Research notes not in the repo; ledgers not tied to shared state |
| Comic Panel Writer | "Comic Mode", + 3 phrases | Near prose rules | comic_project, page records, six output modes | — | Drawable test; one beat per panel; page-turn protection | Research notes not in the repo |

No pack declared machine-readable metadata; activation lived only in prose.

## Other findings

- No routing logic beyond mode descriptions; nothing prevented loading all 103 sections for a one-line request.
- No shared project-state model; each schema stood alone.
- Provenance existed only inside Draft Starter and Origin Forge briefs.
- Research citations in §51 were never verified; five later proved to have title or venue errors.
- The benchmark compared v0.3 with v0.4, not the skill with a baseline.
- No tests and no validation.
- `LICENSE.md` described "professional" use as permitted without qualification, which the NonCommercial term doesn't guarantee, and used a gendered pronoun for the author.
