# CHANGELOG

## v0.9.1 - 2026-11-23

Illustrated Audio Drama 1.1, approved by Erik:

- **Manga composition, not the manga look.**
  - Framing by how much a panel shows (several characters, one, a detail, or only the place), with one-character and detail panels as the default.
  - Point-of-view panels for perception.
  - Look-around runs that stop time.
  - Silent beats written as silence cues.
  - Every page change works as a page turn, with one focal panel per page.
  - New warnings for whole-scene framing, missing silent beats and pages that end flat.
- **Powers.** A growth rule: new effects branch from the power's type. A per-episode intensity ceiling, and a loss-of-control escalation is optional and can be saved for a later part.
- **Research.** Six new entries: two of Cohn's corpus studies, Natsume's essay on panels, a GlobalComix paneling article, a McCloud summary, and the lore session's mapping note. The note's manga percentages were corrected against the source. Source research was gathered by Erik's lore session.

## v0.9 - 2026-11-23

Added the optional **Illustrated Audio Drama** output pack for voiced episodes shown as motion comics, with router integration, a research file and six behavioral fixtures (F42–F47). Added on Erik's explicit request, designed with ChatGPT (gpt-5.6-sol through the Codex CLI, read-only): Claude drafted, ChatGPT critiqued and counter-proposed, Claude merged, and Erik approved.

- `packs/illustrated-audio-drama.md`. Contents:
  - an episode contract with a default ten-minute beat map, or the same beat jobs on a custom shape;
  - power signatures split into how the power works and how it shows, with the removal test and the mechanism test;
  - an audio-first script format that is safe for a voice engine;
  - a sequence-level show-don't-confess scan;
  - screen-page boards timed to locked audio, with a shot plan that gives a reason for each shot and expressive layout that answers story pressure;
  - lettering conventions by voice type;
  - a self-check whose shot-variety, "too basic" and crowding counts are warnings, not gates.
- The registers are `illustrated_audio_script`, `screen_page_board` and `audio_visual_audit`. The router gains the task type `audio_drama_output`.
- `packs/comic-panel-writer.md` 1.2: a `motion_comic_16x9` format, a pointer to the new pack for timing, and the superpower check now covers changes to the comic language.
- `runtime/project-state.md`: the new schemas are mapped. A power's mechanism is a `world` fact, and its signature points to it.
- **Unchanged:** Cinematic Scene Writer, the genre packs, and canon and workspace behavior.
- **What ChatGPT contributed:**
  - the sequence-level confession test, which catches motivated briefings;
  - the expanded mechanism schema, covering range, onset, recovery, evidence and counterplay;
  - mono and small-speaker fallbacks;
  - the job split between audio and picture, against "picture karaoke";
  - turning fixed shot and layout rules into warnings;
  - most of the failure rows and the fixture set.

## v0.8 - 2026-09-26 10:03 PM CDT

Added the optional Cinematic Scene Writer output pack for film and fixed-track music videos, seven consulted sources plus a labeled design entry, cue-evidence and scene-meaning separation, router integration, and six behavioral fixtures. Existing genres, canon and workspace behavior are unchanged. Added on Erik’s explicit request; research and prose authored by Codex.


## v0.7 — Mystery, Horror, Romance, Series, and Worldbuilding

Added, each with a front-matter contract, research file, and fixtures:

- `packs/mystery.md` — truth model first; clue ledger with first-read and true meanings; suspects whose suspicious behavior comes from real secrets; hypothesis log for investigator and reader; false solutions; eight fairness tests; classic, inverted, whydunit, and open forms. Historical rules (Knox, Van Dine) are treated as conventions, and their prejudiced rules are excluded.
- `packs/horror.md` — threat model (dangerous *and* categorically wrong); safety baseline; visibility ladder; dread curve with required recovery beats; rule ledger separating actual rules from believed ones; mode profiles (supernatural, psychological, cosmic, body, human); anti-default audit that flags clichés instead of banning them. Guidance on isolation, disbelief, and aftermath is labeled craft inference.
- `packs/romance.md` — per-partner relationship perception; love as independent dimensions; commitment causes; threat responses; disclosure ladders; barriers; conflict beats; unrequited love from both sides; power-aware consent; queer-romance defaults check; an ending contract that separates genre romance from romantic storylines that may correctly end.
- `packs/series-engine.md` — promise stack, thread ledger with partial payoffs, seven-axis escalation with a bigger-villain check, arc and faction tracks, carry-forward check, convergence plan. Design module.
- `packs/worldbuilding.md` — condition → incentive → institution → norm → personal consequence chains, pressure maps, and scene hooks; no encyclopedia output. Design module.
- New research passes for mystery, horror, and romance, with every URL fetched and partial reads marked. Contested evidence (spoiler studies) is recorded rather than built on.

### Behavioral run (2026-09-16)

`tests/results/2026-09-16.md`. Round 1 passed 27 of 34. Final grading passes 35 of 35 after these changes:

- **FAST SCENE MODE keeps planning internal.** Scene contracts and routes aren't shown unless asked.
- **The Tragic engine gives at least three non-death options** before proposing any death.
- **Research is a route overlay, not a task type.** Research items now carry a `kind` (real fact, plausible invention, deliberate fictionalization) plus, for real facts only, a verification `status`. The old single label list mixed the two.
- **The Draft Starter gate is rewritten.** Authority changes how it runs, not whether; a genre-trigger seed is still a seed.
- **Canon that is referenced but not supplied is never reconstructed as approved canon.** Covered by the new fixture F35.
- **The Mystery pack presents suspects as complete `suspect_state` records.**
- **Fixture fixes:** optional packs, any-of modes, a narrowed page-turn failure, a supplied truth model for F32, and gender-neutral wording in F06.

## v0.6 — Modular runtime

The pre-refactor state is recorded in `docs/AUDIT-v0.5.md`.

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

- `tests/fixtures/` — 35 behavioral fixtures with expected route, behavior, failure modes, and pass criteria; `tests/README.md` defines an executor/grader protocol.
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
