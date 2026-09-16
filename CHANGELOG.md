# CHANGELOG

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
