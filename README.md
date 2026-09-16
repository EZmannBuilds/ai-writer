# AI Writer

A research-informed fiction-writing skill for Claude Code — built for psychologically deep, structurally coherent, distinctive fiction, and for *arguing with itself* rather than following rules blindly.

Licensed **CC BY-NC 4.0** — free to use, share, and adapt; not for resale. See [LICENSE.md](LICENSE.md).

---

## What it does

Most writing assistance collapses into the same defaults: competent, smooth, forgettable. This skill is built to resist that. It treats craft advice as **tools and tests**, not commandments.

"Show, don't tell" becomes:

> Dramatize what the reader should experience. Compress what the reader only needs to know.

The core system runs a full pipeline — intent lock, story genome, character simulation, dynamic outlining, scene contracts, craft interrogation, prose generation, craft audit, layered revision — plus specialized critics and anti-default analysis.

## Install

Clone into your Claude Code skills directory:

```bash
git clone https://github.com/EZmannBuilds/ai-writer.git ~/.claude/skills/ai-writer
```

Claude Code discovers it automatically. Invoke it with `/ai-writer`, or just describe fiction work and it will load.

## Layout

```text
SKILL.md          the core system — everything else is loaded on demand
packs/            staged add-ons; each has a trigger phrase
craft/            one-page reference cards for page-level craft
research/         provenance, source claims, evaluation method
```

### `packs/` — pipeline add-ons

Each pack runs in front of the core pipeline, in this order. Load one only when its trigger fires.

| Pack | Trigger | What it does |
|---|---|---|
| [draft-starter.md](packs/draft-starter.md) | "Start Draft," or any loose seed | A short collaborative interview that turns a premise into a Draft Brief before Intent Lock runs. Three question layers (Emotional Core, Story Identity, Authenticity & World Detail), selective by design. Guided / Collaborative / Autonomous control modes. |
| [origin-forge.md](packs/origin-forge.md) | "Start Origin" | How a person became the identity the main story meets. A flexible 12-stage spine (Before Self → Story Launch), alignment paths for hero/villain/antihero/fallen hero/redemption, a military & moral-conflict module, and a hard trauma guardrail. |
| [tragic-anime-engine.md](packs/tragic-anime-engine.md) | "Start Tragic Story" | Dark action and tragic fantasy: the tragedy equation, cruel-conditions test, Hope Reserve, perspective reversal, reveal architecture, the Death Necessity Test, escalation axes, ideological conflict. Companion: [tragic-anime-lenses.md](packs/tragic-anime-lenses.md), nine secondary reference lenses. |
| [comic-panel-writer.md](packs/comic-panel-writer.md) | "Comic Mode" | Comic-book visual logic and optional page/panel scripting. Six output modes from Comic Narrative through Full Script. Not a planning stage — an output register, used at drafting time. |

Full pipeline when all are active:

```text
seed → Draft Starter → Origin Forge → Tragic Anime Engine
     → Intent Lock → Story Genome → outline → draft
     → Comic Panel Writer, if the output is visual
```

Origin Forge and Comic Panel Writer bridge to each other: the transformation logic of one maps onto the visual timing of the other, stage for stage.

### `craft/` — reference cards

Condensed single-topic cards. `SKILL.md` covers the same ground at length; these are the compressed checklists.

[show-tell](craft/show-tell.md) · [scene-craft](craft/scene-craft.md) · [dialogue-subtext](craft/dialogue-subtext.md) · [pov-psychic-distance](craft/pov-psychic-distance.md) · [exposition-backstory](craft/exposition-backstory.md) · [common-mistakes](craft/common-mistakes.md) · [question-bank](craft/question-bank.md) · [revision-passes](craft/revision-passes.md) · [storyscope-anti-defaults](craft/storyscope-anti-defaults.md)

### `research/` — why the rules are the rules

[research-pass-4.md](research/research-pass-4.md) is the craft-layer synthesis. [source-index.md](research/source-index.md) maps every source to the specific claim it supports. [benchmark.md](research/benchmark.md) is how you test whether the skill actually improves output.

These exist so the reasoning can be argued with. If a rule seems wrong for the work at hand, go read why it's there and then decide.

## On the reference pillars

The tragic-story packs are built from Attack on Titan, Jujutsu Kaisen, and nine secondary lenses — reduced to **transferable mechanisms only**. Nothing in here reproduces those works, and the skill is explicit that imitation is a failure state.

## License

CC BY-NC 4.0. Use it, share it, fork it, publish your own version. Don't sell it. Credit the author.

Fiction you write *using* the skill is entirely yours — the license covers the instructions and frameworks, not your stories.

Copyright © 2026 Erik Mann.
