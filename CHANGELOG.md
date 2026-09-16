# CHANGELOG

## v0.7 — Mystery, Horror, Romance, Series, and Worldbuilding

Added, each with a front-matter contract, research file, and fixtures:

- `packs/mystery.md` — truth model first; clue ledger with first-read and true meanings; suspects whose suspicious behavior comes from real secrets; hypothesis log for investigator and reader; false solutions; eight fairness tests; classic, inverted, whydunit, and open forms. Historical rules (Knox, Van Dine) are treated as conventions, and their prejudiced rules are excluded.
- `packs/horror.md` — threat model (dangerous *and* categorically wrong); safety baseline; visibility ladder; dread curve with required recovery beats; rule ledger separating actual rules from believed ones; mode profiles (supernatural, psychological, cosmic, body, human); anti-default audit that flags clichés instead of banning them. Guidance on isolation, disbelief, and aftermath is labeled craft inference.
- `packs/romance.md` — per-partner relationship perception; love as independent dimensions; commitment causes; threat responses; disclosure ladders; barriers; conflict beats; unrequited love from both sides; power-aware consent; queer-romance defaults check; an ending contract that separates genre romance from romantic storylines that may correctly end.
- `packs/series-engine.md` — promise stack, thread ledger with partial payoffs, seven-axis escalation with a bigger-villain check, arc and faction tracks, carry-forward check, convergence plan. Design module.
- `packs/worldbuilding.md` — condition → incentive → institution → norm → personal consequence chains, pressure maps, and scene hooks; no encyclopedia output. Design module.
- New research passes for mystery, horror, and romance, with every URL fetched and partial reads marked. Contested evidence (spoiler studies) is recorded rather than built on.

## v0.6 — Modular runtime

v0.6 turns the single-file skill into a small kernel with modular systems. No proven craft content was dropped; every moved line was checked by script. The v0.5 tree is tagged `v0.5-baseline`.

Architecture:

- `SKILL.md` is a ~13 KB kernel (was 93 KB): purpose, 13 governing principles, runtime flow, modes, pack and module index, guardrails, compact runtime instruction.
- `core/` — 22 focused modules (largest ~13 KB), each opening with a contract table: invoked by, when, needs, produces, state, consumed by, skip when, tests, research. `core/research-mode.md` is new: verification triage (load, exposure, harm) and four fact labels.
- `runtime/router.md` — task classifier (17 task types), precedence, state lookup, mode selection, pack activation and order, per-mode module selection, output register, state extraction, authority levels, when to ask the user.
- `runtime/project-state.md` — one sparse model unifying Draft Brief, Intent Lock, Story Genome, characters, relationships, world, timeline, outline, open loops, reader state, setups/payoffs, pack state, continuity, research, and summaries.
- `runtime/workspace.md` + `templates/workspace/` — optional persistent `.ai-writer/` folder with initialization, selective retrieval, append-and-supersede updates, snapshots, and recovery. Legacy mode needs no migration.
- `runtime/canon-resolver.md` — eleven provenance statuses, a nine-line precedence hierarchy, intentional-contradiction checks (unreliable narration, beliefs, alternate continuity, misdirection, retcons), conflict resolution with both sides quoted, and promotion rules. Proposals become canon only through the user.

Packs:

- Every pack has a YAML contract (triggers, natural-language triggers, requires, optional dependencies, conflicts, stacks, inputs, produces, skip conditions, state keys, research basis, behavior tests).
- Draft Starter gains the `interview_state` schema from its original pack, never previously integrated.
- `docs/PACK_AUTHORING.md` and `templates/PACK_TEMPLATE.md`.
- All legacy triggers still route: Start Draft, Start Origin, Start Tragic Story, Dark Anime Mode, Comic Mode.

Cleanup:

- Numbered section references replaced with named anchors; old subsection numbers removed from headings; numbering defects (gaps, out-of-order sections) documented in `docs/MIGRATION.md`, which maps every v0.5 section.
- `craft/` removed. Each card now lives inside the module it condensed. The Exposition revision pass, missing from the core list, is now Pass 7; unique card questions were merged into the question bank.
- Outdated v0.3/v0.4 framing rewritten where it described the current system.

Research:

- `research/` rebuilt: `README.md`, generated `source-index.md` (121 keys), `translation-limits.md`, `core/` and `packs/` entry files, each entry recording source, claim, derivation, limitations, and fidelity (exact, approximate, conceptual, convention, design).
- All 24 inherited core citations re-verified. Corrected: DOME's and NoveltyBench's published titles, BookWorld's and StoryBox's titles and venues. MAGNET is the system inside *From Personas to Plot*, not a separate paper. Preprints are labeled.
- The original pack research notes for Origin Forge, the Tragic engine, and Comic Panel Writer — never copied into the skill before — are now in `research/packs/` (not re-verified).
- Inline `[@key]` citations added to every research-derived core section.
- `research/benchmark.md` rewritten: baseline vs AI Writer under matched conditions, ten task types, human pairwise evaluation as primary, bounded automated checks, and an anti-homogenization rule. No run has been recorded yet.

Tests and CI:

- `tests/fixtures/` — 34 behavioral fixtures with expected route, behavior, failure modes, and pass criteria; `tests/README.md` defines an executor/grader protocol.
- `tests/workflow-traces.md` — seven end-to-end traces. Tracing found and fixed: pack `requires` not loading in modes that don't list them; active packs not restored on continuation; no hook for pack drafting checks; no place for pack constraints in Intent Lock; no storage for per-installment series contracts; skip conditions contradicting explicit triggers; a missing `story_request` task type.
- `scripts/validate.py` — links and anchors, duplicate anchors, code-span paths, stale references, YAML blocks, SKILL front matter, pack contracts (fields, stages, ids, dependencies, reciprocal conflicts, table sync, legacy triggers), core contracts, fixtures (including trigger/route consistency), research entries and citations, uncited research claims, templates, and index freshness.
- `scripts/build_source_index.py` generates the source index from entries.
- `.github/workflows/validate.yml` runs both on every push and pull request.

License:

- `LICENSE.md` plain-language section rewritten: explicitly explanatory; legal code authoritative; describes sharing and adapting accurately; separates the skill's material from fiction written with it without contradicting the license; flags that commercial-use questions go to the author. CC BY-NC 4.0 unchanged.

## v0.5 — Audit and merge into one directory

No craft content changed in this release. This is a structural pass, so that an agent opening the skill cold can tell what is here and when to load it.

Audited:
- `SKILL.md` and `AI_Writer_Skill_v0.4.md` were **byte-identical** (91,132 bytes each, md5 `12a83f808f66ee7812654f3b00d2e4c5`) — 182KB of a 292KB skill was one file stored twice, and every edit had to be made in both places by hand.
- The nine craft modules were tested against `SKILL.md` for redundancy and are **not** duplicates; they are condensed quick-reference cards covering the same ground as §84–§103 at much shorter length. Kept.
- 24 flat files carried three different naming conventions.

Removed:
- `AI_Writer_Skill_v0.4.md` — the duplicate. `SKILL.md` is the single copy; it carries the skill frontmatter and so must live at the root.
- `manifest.json` — Claude Code reads `SKILL.md` frontmatter, not a manifest. Its only content was a file list that would go stale and mislead agents reading it.

Restructured into three directories, all files kebab-cased:
- `packs/` — draft-starter, origin-forge, tragic-anime-engine, tragic-anime-lenses, comic-panel-writer
- `craft/` — show-tell, scene-craft, dialogue-subtext, pov-psychic-distance, exposition-backstory, common-mistakes, question-bank, revision-passes, storyscope-anti-defaults
- `research/` — research-pass-4, source-index, benchmark

Added:
- `SKILL.md` §0.0, a directory map at the top of the file: what lives where, each pack's trigger and load order, and the full pipeline. This is the first thing an agent reads after the frontmatter.
- A rewritten `README.md` as the human front door — install command, layout, pack trigger table, and the reasoning behind the license.

Changed:
- Every cross-reference inside `SKILL.md`, `packs/`, `craft/`, and `research/` now points at the new paths.
- Version bumped to 0.5; `license: CC-BY-NC-4.0` added to the frontmatter.

Entries below are kept verbatim as a record of past states, old filenames included.

## v0.4.3 — Tragic Anime Story Engine + license

Added:
- `TRAGIC_ANIME_STORY_ENGINE_INSERT.md` — dark-action/tragic-fantasy craft built from Attack on Titan and Jujutsu Kaisen as primary reference pillars (transferable reasoning only, never imitation). Core tragedy equation, cruel-conditions test, Hope Reserve, perspective reversal, reveal architecture, the Death Necessity Test, tragedy variety, power-under-pressure, escalation axes, ensemble pressure, ideological conflict, tragic foreshadowing, endgame convergence, and the full schema/ledger set.
- `TRAGIC_ANIME_SECONDARY_LENSES.md` — nine secondary reference lenses (Madoka, Devilman Crybaby, Edgerunners, 86, To Your Eternity, Fate/Zero, Made in Abyss, Violet Evergarden, Chainsaw Man), each reduced to transferable mechanisms.
- `LICENSE.md` — CC BY-NC 4.0. Free to use, share, and adapt; commercial resale is not permitted; attribution required.

Changed:
- SKILL.md and AI_Writer_Skill_v0.4.md each gained one more pointer section, beside Origin Forge (§3, before Intent Lock).
- manifest.json now records the license and the two new files.

## v0.4.2 — Origin Forge + Comic Panel Writer

Added:
- `ORIGIN_FORGE_INSERT.md` — how a person became the identity the main story meets. Flexible 12-stage spine (Before Self → ... → Story Launch), hero/villain/antihero/fallen-hero/redemption alignment paths, a dedicated military/moral-conflict module, a hard trauma/diagnosis guardrail, and the Origin Brief schema. Sits after Draft Starter, before Intent Lock.
- `COMIC_PANEL_WRITER_INSERT.md` — comic-book visual logic, six output modes (Comic Narrative default, through Full Script), panel/page/lettering/action frameworks, and production checks. Sits near §41 Prose Generation Rules, deliberately apart from the front-door planning inserts.
- Both packs bridge to each other: Origin Forge's transformation logic maps directly onto Comic Panel Writer's visual timing, stage for stage.

Changed:
- SKILL.md and AI_Writer_Skill_v0.4.md each gained two more short pointer sections: Origin Forge beside Draft Starter (§3), Comic Panel Writer beside the prose rules (§41).

## v0.4.1 — Draft Starter Insert

Added:
- `DRAFT_STARTER_INSERT.md` — a pre-drafting interview layer, sourced from `Draft_Starter_Insert_Pack_v1.0`, sitting before Intent Lock.
- "Start Draft" trigger (and natural-language equivalents) for turning a loose seed into a Draft Brief through a short collaborative interview.
- Three-layer question bank (Emotional Core, Story Identity, Authenticity & World Detail), selective by design — never a full questionnaire.
- Guided / Collaborative (default) / Autonomous creative-control modes.
- Draft Brief YAML schema, handed off to Intent Lock.
- Worked examples (loose seed, full delegation) and ten behavior checks.

Changed:
- SKILL.md and AI_Writer_Skill_v0.4.md both gained a short pointer section immediately before `# 3. Intent Lock` routing into this module.

## v0.4

Added:
- nuanced Show–Tell Decision Engine;
- show-then-tell for unfamiliar/speculative material;
- anti-body-language-cliché check;
- scene enter-late / leave-early test with exceptions;
- scene goal/resistance/change diagnostic;
- need-to-know exposition router;
- selective specificity;
- psychic-distance engine;
- dialogue hidden-sentence / tactic / subtext model;
- setup/payoff ledger;
- personal-stakes model;
- worldbuilding-through-use model;
- pacing via scene vs summary;
- character anti-puppet test;
- 25-item common writer mistake audit;
- reader-trust / redundancy audit;
- ending consequence vs over-explanation check;
- full storytelling question bank;
- ordered craft revision passes;
- v0.4 craft-specific benchmark.

Changed:
- main runtime pipeline now includes craft interrogation and craft audit;
- scene contract includes entry/exit, show/tell, exposition, psychic distance, setup/payoff;
- dialogue state includes hidden sentence, tactics, deflection, silence, voice;
- prose rules now distinguish dramatization from compression.

Retained:
- v0.3 character simulation;
- dynamic outlining;
- memory;
- suspense;
- curiosity;
- surprise;
- continuity;
- StoryScope anti-default analysis;
- specialized critics.
