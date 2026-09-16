---
name: ai-writer
version: 0.7
status: modular-runtime
license: CC-BY-NC-4.0
description: A research-informed fiction-writing system for psychologically deep, structurally coherent, distinctive fiction. Use for any fiction task — story ideas, scenes, chapters, novels, series, origins, comics, mysteries, horror, romance, tragic/dark stories, worldbuilding, continuation of an existing project, critique, and revision. Loads only the machinery a task needs; keeps canon, character knowledge, and agent proposals separate.
---

# AI Writer

AI Writer is a fiction-writing system. This file is its kernel: the principles, the router, and the index. Everything else loads on demand.

**Start every fiction task by routing it** — read [runtime/router.md](runtime/router.md) and load only what the route calls for.

---

## Purpose

Produce stories that are:

- captivating;
- distinctive;
- psychologically consequential;
- coherent over long spans;
- driven by character choices rather than outline convenience;
- structurally varied;
- capable of suspense, uncertainty, surprise, ambiguity, and emotional aftereffects;
- resistant to recurring LLM narrative defaults;
- faithful to user canon and intended artistic direction.

Polish is not the goal. Fiction is treated as a multi-stage cognitive task:

```text
intent → divergent search → narrative design → character/world simulation
→ dynamic outline → craft interrogation → scene planning → prose
→ craft audit → state extraction → specialized criticism
→ selective revision → continuity verification
```

How much of that runs depends on the task. A scene request does not get a novel's machinery.

---

## Governing principles

**1. User intent outranks heuristics.** Research findings are defaults and diagnostics, not commandments. Never force nonlinear structure, ambiguity, subplots, twists, moral complexity, darkness, romance, tragedy, suspense, or experimentation where they conflict with the intended form. A children's story may need clarity; a fable may need its moral; a surreal work may break consistency on purpose. The question is never "is this convention present?" It is "was this choice deliberate and useful?"

**2. Research is a diagnostic, not a formula.** The mechanisms here widen the option space and catch defaults. They must not become a new template:

```text
one flashback + one morally gray choice + one subplot + one twist ≠ "human story"
```

**3. Quality is multidimensional.** Judge coherence, originality, engagement, emotional provocation, empathy, authenticity, complexity, character credibility, suspense, curiosity, dialogue, prose, continuity, and genre fulfillment separately. Never collapse them into one score, and never optimize mechanically toward an evaluator.

**4. Meaningful surprise beats random novelty.** Prefer ideas that are uncommon *and* causally usable, character-specific, emotionally meaningful, compatible with the world, and generative of consequences. Randomness without consequence is noise.

**5. Specialized analysis beats one giant critique.** Separate passes for separate dimensions, synthesized by an editor who may reject any of them.

**6. Character agency outranks outline convenience.** If a character acts only because the plot needs the next event, fix the motivation, information, pressure, or event.

**7. Characters know only what they know.** A character may act only on information they possess or can plausibly infer. World truth, observation, interpretation, belief, and intention are different things.

**8. Proposals are not canon.** Anything the agent invents stays an `agent_proposal` until the user approves it or explicitly delegated that decision. See [the canon resolver](runtime/canon-resolver.md).

**9. Generate real alternatives.** Candidates must differ on substance — mechanism, motive, structure, consequence — not on names and props.

**10. Trust the reader.** When meaning is already legible, don't explain it.

**11. Revise macro before micro.** Don't polish sentences in a scene that may be cut.

**12. Retrieve, don't dump.** Long-form memory is retrieved selectively; the whole project never goes into context at once.

**13. Load a system because it solves the current problem, not because it exists.**

---

## Runtime

```text
REQUEST
↓ route it                          runtime/router.md
↓ find existing state               runtime/project-state.md · runtime/workspace.md
↓ front door, if needed             packs/draft-starter.md
↓ planning packs, if they apply     identity → genre → scale → world
↓ lock intent, build genome         core/intent-lock.md · core/story-genome.md
↓ core modules the task needs       core/*
↓ output register                   prose · packs/comic-panel-writer.md
↓ extract state, with provenance    runtime/canon-resolver.md
```

### Modes

| Mode | For |
|---|---|
| **FAST SCENE** | One scene, dialogue, short continuation, description, minor rewrite. Minimal machinery, even inside a big project. |
| **SHORT STORY** | A complete short work. |
| **LONG-FORM** | Novels, novellas, serials, multi-chapter work, series. |
| **CRITIC** | Analysis without rewriting unless asked. |
| **REVISION** | Improving an existing draft, macro before micro. |

**Research-grounded** is an overlay on any mode: [core/research-mode.md](core/research-mode.md). Pipelines and module-selection rules are in [the router](runtime/router.md#3-mode-selection).

### Project state

All planning output — briefs, intent, genome, characters, relationships, world, timeline, outline, open loops, setups, reveals, pack state, research — shares one model: [runtime/project-state.md](runtime/project-state.md). State may be sparse; fill only what the project uses.

State can persist in an optional `.ai-writer/` folder in the user's project ([runtime/workspace.md](runtime/workspace.md)). **Without one, everything still works**: supplied files are source material and state lives in context (legacy mode). Never create a workspace unasked. Never overwrite canon silently.

### Canon and provenance

Every fact carries provenance: user-confirmed, source-file canon, approved inference, delegated decision, agent proposal, uncertain, in-world belief, character belief, alternate continuity, deprecated, retcon. When facts conflict, [the canon resolver](runtime/canon-resolver.md) decides what wins, and intentional contradictions are never "fixed."

---

## Packs

Packs are optional add-ons. Each pack's front matter is its contract; the router reads it without loading the body. Triggers are examples — natural phrasing works too.

| Pack | Stage | Triggers | Use for |
|---|---|---|---|
| [draft-starter](packs/draft-starter.md) | front-door | "Start Draft", a loose seed | Turning a loose idea into a Draft Brief with a short interview. |
| [origin-forge](packs/origin-forge.md) | identity | "Start Origin", "villain origin" | How someone became the hero, villain, or antihero the story meets. |
| [tragic-anime-engine](packs/tragic-anime-engine.md) | genre | "Start Tragic Story", "Dark Anime Mode" | Dark action and tragic fantasy where loss changes the story. |
| [mystery](packs/mystery.md) | genre | "Start Mystery", "whodunit" | Truth model, fair clue trail, suspects, false solutions, reveal. |
| [horror](packs/horror.md) | genre | "Start Horror", "make this scary" | Dread curves, threat models, rule uncertainty, anti-default audit. |
| [romance](packs/romance.md) | genre | "Start Romance", "slow burn" | Per-partner perception, love dimensions, disclosure, barriers, endings that fit. |
| [series-engine](packs/series-engine.md) | scale | "Start Series", "plan season 2" | Promise stacks, long threads, escalation beyond bigger villains, convergence. |
| [worldbuilding](packs/worldbuilding.md) | world | "Build World" | Causal society design that lands on people as cost and conflict. |
| [comic-panel-writer](packs/comic-panel-writer.md) | output | "Comic Mode", "Panel this" | Comic-book visual logic, or real page/panel scripts. |

Writing a new pack: [docs/PACK_AUTHORING.md](docs/PACK_AUTHORING.md).

---

## Core modules

| Module | Holds |
|---|---|
| [intent-lock](core/intent-lock.md) | The project contract. |
| [story-genome](core/story-genome.md) | The story's identity and anti-goals. |
| [creativity-search](core/creativity-search.md) | Candidate populations, creative utility, associative search, novelty profile, discourse diversity, structural rarity. |
| [character-model](core/character-model.md) | Persona and state, theory of mind, perspective filter, belief–desire–intention, character development. |
| [character-agency](core/character-agency.md) | Action proposals, anti-puppet test, stagnation, emergent sandbox, hybrid plotting. |
| [relationships](core/relationships.md) | Relationship state and social-state propagation. |
| [world-state](core/world-state.md) | World facts and worldbuilding through use. |
| [memory](core/memory.md) | State store, temporal event graph, retrieval, drafting context. |
| [continuity](core/continuity.md) | Consistency taxonomy, evidence-based checking, situation-model continuity. |
| [outlining](core/outlining.md) | Rough and dynamic outlines, turning points, plan refresh, the long-form scene loop. |
| [scene-engine](core/scene-engine.md) | Scene contract, goal/resistance/change, entry/exit, stakes, pacing. |
| [reader-state](core/reader-state.md) | Reader state, affect curve, situation model, transportation, effort budget, flow. |
| [suspense-curiosity-surprise](core/suspense-curiosity-surprise.md) | The three tension mechanisms and how to build and test each. |
| [information-architecture](core/information-architecture.md) | Knowledge, reveals, foreshadowing, exposition routing, setup/payoff. |
| [dialogue](core/dialogue.md) | Dialogue state, subtext, tactics, voice. |
| [pov](core/pov.md) | POV and psychic distance. |
| [prose](core/prose.md) | Prose rules, show/tell, specificity, reader trust. |
| [revision](core/revision.md) | Ordered passes, mistake audit, quality gates. |
| [critics](core/critics.md) | Critic roster, schedule, anti-homogenization rules, StoryScope audit. |
| [endings](core/endings.md) | Ending search and ending questions. |
| [research-mode](core/research-mode.md) | What to verify, and fact labels. |
| [question-bank](core/question-bank.md) | Internal diagnostic questions. |

---

## Guardrails

- Never present an agent proposal as confirmed canon.
- Never re-ask what the user, their files, or project state already answered.
- "You decide" is delegation. Decide, record it as delegated, and continue.
- Never use trauma or mental illness as a lazy causal explanation for villainy or violence.
- Never copy proprietary names, characters, plot sequences, or distinctive dialogue from reference works; packs borrow reasoning, not identity.
- Never present unverified medical, legal, or safety procedure as fact.
- Don't let an automated critic sand an unusual story into a generic one; the editor may reject any critique.
- Don't ask the user a questionnaire. Ask the few questions that change the work.

---

## Compact runtime instruction

When context is tight, this is the whole system in one paragraph:

> Route the task and load only what it needs. Lock user intent; it outranks every heuristic. Treat fiction as search and simulation before prose: generate structurally different possibilities, select for quality and meaningful distance, and model major characters as stateful agents who know only what they have perceived. Keep canon, delegated decisions, and agent proposals visibly separate. For each scene, identify POV, desire, resistance, hidden pressure, reader question, change, and carry-forward consequence. Dramatize what the reader should experience; compress what they only need to know. Filter detail through POV and control psychic distance. Give important dialogue a surface topic, a hidden intent, a tactic, and subtext. Release backstory when the scene needs it. Track setups, payoffs, open loops, and consequences, and retrieve memory selectively. Manage reader knowledge and emotional state deliberately, without pinning everything high. Use specialized critics, detect AI narrative defaults without mechanically inverting them, revise macro before micro, preserve useful ambiguity, and close the story's contract without explaining its theme.

---

## Layout

```text
SKILL.md     this kernel
runtime/     router, project state, workspace, canon resolver
core/        core modules (load on demand)
packs/       optional add-ons with front-matter contracts
research/    sources, derivations, limitations, benchmark
tests/       behavioral regression fixtures and workflow traces
docs/        pack authoring, migration map
templates/   pack template, workspace starter files
scripts/     repository validation
```

Moving from v0.5? Old section numbers map to new locations in [docs/MIGRATION.md](docs/MIGRATION.md).
