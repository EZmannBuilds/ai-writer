# Migration map: v0.5 → v0.6

v0.5 kept the whole system in one 93 KB `SKILL.md` with numbered sections. v0.6 splits it into a kernel, runtime specs, and focused core modules. References to old section numbers resolve here.

Every body line of the moved sections was carried over verbatim and checked by script; only headings and cross-references changed. The v0.5 tree is preserved at the `v0.5-baseline` git tag.

## Numbering defects fixed

v0.5's numbering had gaps and was out of order: §50 was followed by §55, §53–54 never existed, and §51–52 and §82–83 appeared after §81. v0.6 drops numbers entirely in favor of named anchors, which don't break when sections move.

## Section map

| v0.5 | Section | Now |
|---|---|---|
| §0 | Purpose | [SKILL.md#purpose](../SKILL.md#purpose) |
| §1 | Governing Principles | [SKILL.md#governing-principles](../SKILL.md#governing-principles) |
| §2 | Operating Modes | [runtime/router.md#3-mode-selection](../runtime/router.md#3-mode-selection) |
| §3 | Intent Lock | [core/intent-lock.md#the-intent-lock-schema](../core/intent-lock.md#the-intent-lock-schema) |
| §4 | Story Genome | [core/story-genome.md#the-story-genome-schema](../core/story-genome.md#the-story-genome-schema) |
| §5 | Divergent Creative Search | [core/creativity-search.md#divergent-creative-search](../core/creativity-search.md#divergent-creative-search) |
| §6 | Creative Utility Selection | [core/creativity-search.md#creative-utility-selection](../core/creativity-search.md#creative-utility-selection) |
| §7 | Associative Creativity Search | [core/creativity-search.md#associative-creativity-search](../core/creativity-search.md#associative-creativity-search) |
| §8 | Fine-Grained Novelty Profile | [core/creativity-search.md#fine-grained-novelty-profile](../core/creativity-search.md#fine-grained-novelty-profile) |
| §9 | Discourse Diversity Check | [core/creativity-search.md#discourse-diversity-check](../core/creativity-search.md#discourse-diversity-check) |
| §10 | Character Architecture | [core/character-model.md#character-architecture](../core/character-model.md#character-architecture) |
| §11 | Character Action Engine | [core/character-agency.md#character-action-engine](../core/character-agency.md#character-action-engine) |
| §12 | Goal Sequencing and Stagnation Detection | [core/character-agency.md#goal-sequencing-and-stagnation-detection](../core/character-agency.md#goal-sequencing-and-stagnation-detection) |
| §13 | Dynamic Hierarchical Outline | [core/outlining.md#dynamic-hierarchical-outline](../core/outlining.md#dynamic-hierarchical-outline) |
| §14 | Rough Outline | [core/outlining.md#rough-outline](../core/outlining.md#rough-outline) |
| §15 | Detailed Outline Expansion | [core/outlining.md#detailed-outline-expansion](../core/outlining.md#detailed-outline-expansion) |
| §16 | Structured Drafting Context | [core/memory.md#structured-drafting-context](../core/memory.md#structured-drafting-context) |
| §17 | Plan Refresh | [core/outlining.md#plan-refresh](../core/outlining.md#plan-refresh) |
| §18 | Memory Architecture | [core/memory.md#memory-architecture](../core/memory.md#memory-architecture) |
| §19 | Memory Retrieval | [core/memory.md#memory-retrieval](../core/memory.md#memory-retrieval) |
| §20 | Consistency Taxonomy | [core/continuity.md#consistency-taxonomy](../core/continuity.md#consistency-taxonomy) |
| §21 | Evidence-Based Continuity Checker | [core/continuity.md#evidence-based-continuity-checker](../core/continuity.md#evidence-based-continuity-checker) |
| §22 | Reader-State Model | [core/reader-state.md#reader-state-model](../core/reader-state.md#reader-state-model) |
| §23 | Affect Curve | [core/reader-state.md#affect-curve](../core/reader-state.md#affect-curve) |
| §24 | Turning-Point Planning | [core/outlining.md#turning-point-planning](../core/outlining.md#turning-point-planning) |
| §25 | Suspense Engine | [core/suspense-curiosity-surprise.md#suspense-engine](../core/suspense-curiosity-surprise.md#suspense-engine) |
| §26 | Adversarial Suspense Planning | [core/suspense-curiosity-surprise.md#adversarial-suspense-planning](../core/suspense-curiosity-surprise.md#adversarial-suspense-planning) |
| §27 | Knowledge Disparity | [core/suspense-curiosity-surprise.md#knowledge-disparity](../core/suspense-curiosity-surprise.md#knowledge-disparity) |
| §28 | Foreshadowing vs Warning | [core/information-architecture.md#foreshadowing-vs-warning](../core/information-architecture.md#foreshadowing-vs-warning) |
| §29 | Information Architecture | [core/information-architecture.md#information-architecture](../core/information-architecture.md#information-architecture) |
| §30 | Revelation Test | [core/information-architecture.md#revelation-test](../core/information-architecture.md#revelation-test) |
| §31 | Psychological Depth Scale | [core/critics.md#psychological-depth-scale](../core/critics.md#psychological-depth-scale) |
| §32 | Psychological Depth Critic Council | [core/critics.md#psychological-depth-critic-council](../core/critics.md#psychological-depth-critic-council) |
| §33 | StoryScope Anti-Default Audit | [core/critics.md#storyscope-anti-default-audit](../core/critics.md#storyscope-anti-default-audit) |
| §34 | Structural Rarity Pass | [core/creativity-search.md#structural-rarity-pass](../core/creativity-search.md#structural-rarity-pass) |
| §35 | Macro Creativity Critics | [core/critics.md#macro-creativity-critics](../core/critics.md#macro-creativity-critics) |
| §36 | Critic Leader | [core/critics.md#critic-leader](../core/critics.md#critic-leader) |
| §37 | Multi-Round Plan Refinement | [core/critics.md#multi-round-plan-refinement](../core/critics.md#multi-round-plan-refinement) |
| §38 | Micro Creativity Critics | [core/critics.md#micro-creativity-critics](../core/critics.md#micro-creativity-critics) |
| §39 | Scene Contract | [core/scene-engine.md#scene-contract](../core/scene-engine.md#scene-contract) |
| §40 | Dialogue Engine | [core/dialogue.md#dialogue-engine](../core/dialogue.md#dialogue-engine) |
| §41 | Prose Generation Rules | [core/prose.md#prose-generation-rules](../core/prose.md#prose-generation-rules) |
| §42 | Dynamic Character Development | [core/character-model.md#dynamic-character-development](../core/character-model.md#dynamic-character-development) |
| §43 | Relationship State | [core/relationships.md#relationship-state](../core/relationships.md#relationship-state) |
| §44 | Ending Search | [core/endings.md#ending-search](../core/endings.md#ending-search) |
| §45 | Long-Form Scene Loop | [core/outlining.md#long-form-scene-loop](../core/outlining.md#long-form-scene-loop) |
| §46 | Critic Scheduling | [core/critics.md#critic-scheduling](../core/critics.md#critic-scheduling) |
| §47 | Evaluation Profile | [core/critics.md#evaluation-profile](../core/critics.md#evaluation-profile) |
| §48 | Automatic Judge Warning | [core/critics.md#automatic-judge-warning](../core/critics.md#automatic-judge-warning) |
| §49 | Human-in-the-Loop Checkpoints | [runtime/router.md#when-to-ask-the-user](../runtime/router.md#when-to-ask-the-user) |
| §50 | Research-Grounded Generation vs Research-Driven Formula | [core/research-mode.md#research-grounded-generation-vs-research-driven-formula](../core/research-mode.md#research-grounded-generation-vs-research-driven-formula) |
| §51 | Research Basis | [research/source-index.md](../research/source-index.md) |
| §52 | Known Translation Limits | [research/translation-limits.md](../research/translation-limits.md) |
| §55 | Theory-of-Mind Character Model | [core/character-model.md#theory-of-mind-character-model](../core/character-model.md#theory-of-mind-character-model) |
| §56 | Perspective Filter | [core/character-model.md#perspective-filter](../core/character-model.md#perspective-filter) |
| §57 | Belief–Desire–Intention Loop | [core/character-model.md#beliefdesireintention-loop](../core/character-model.md#beliefdesireintention-loop) |
| §58 | Second-Order Social Reasoning | [core/character-model.md#second-order-social-reasoning](../core/character-model.md#second-order-social-reasoning) |
| §59 | Reader Situation Model | [core/reader-state.md#reader-situation-model](../core/reader-state.md#reader-situation-model) |
| §60 | Situation-Model Continuity | [core/continuity.md#situation-model-continuity](../core/continuity.md#situation-model-continuity) |
| §61 | Curiosity Engine | [core/suspense-curiosity-surprise.md#curiosity-engine](../core/suspense-curiosity-surprise.md#curiosity-engine) |
| §62 | Information-Gap Calibration | [core/suspense-curiosity-surprise.md#information-gap-calibration](../core/suspense-curiosity-surprise.md#information-gap-calibration) |
| §63 | Curiosity Update Loop | [core/suspense-curiosity-surprise.md#curiosity-update-loop](../core/suspense-curiosity-surprise.md#curiosity-update-loop) |
| §64 | Curiosity vs Suspense vs Surprise | [core/suspense-curiosity-surprise.md#curiosity-vs-suspense-vs-surprise](../core/suspense-curiosity-surprise.md#curiosity-vs-suspense-vs-surprise) |
| §65 | Narrative Surprise Engine | [core/suspense-curiosity-surprise.md#narrative-surprise-engine](../core/suspense-curiosity-surprise.md#narrative-surprise-engine) |
| §66 | Surprise Construction Procedure | [core/suspense-curiosity-surprise.md#surprise-construction-procedure](../core/suspense-curiosity-surprise.md#surprise-construction-procedure) |
| §67 | Surprise Red-Team | [core/suspense-curiosity-surprise.md#surprise-red-team](../core/suspense-curiosity-surprise.md#surprise-red-team) |
| §68 | Surprise Research Caution | [core/suspense-curiosity-surprise.md#surprise-research-caution](../core/suspense-curiosity-surprise.md#surprise-research-caution) |
| §69 | Narrative Transportation | [core/reader-state.md#narrative-transportation](../core/reader-state.md#narrative-transportation) |
| §70 | Transportation Prerequisites | [core/reader-state.md#transportation-prerequisites](../core/reader-state.md#transportation-prerequisites) |
| §71 | Transportation Audit | [core/reader-state.md#transportation-audit](../core/reader-state.md#transportation-audit) |
| §72 | Reader Effort Budget | [core/reader-state.md#reader-effort-budget](../core/reader-state.md#reader-effort-budget) |
| §73 | Event-Level Flow, Not Token Predictability | [core/reader-state.md#event-level-flow-not-token-predictability](../core/reader-state.md#event-level-flow-not-token-predictability) |
| §74 | Emergent Sandbox Mode | [core/character-agency.md#emergent-sandbox-mode](../core/character-agency.md#emergent-sandbox-mode) |
| §75 | Hybrid Top-Down / Bottom-Up Plotting | [core/character-agency.md#hybrid-top-down--bottom-up-plotting](../core/character-agency.md#hybrid-top-down--bottom-up-plotting) |
| §76 | Social-State Propagation | [core/relationships.md#social-state-propagation](../core/relationships.md#social-state-propagation) |
| §77 | Genre Module Status | [research/README.md#genre-coverage](../research/README.md#genre-coverage) |
| §78 | Benchmark Requirement | [research/benchmark.md](../research/benchmark.md) |
| §79 | Primary Human Evaluation Questions | [research/benchmark.md#human-pairwise-evaluation](../research/benchmark.md#human-pairwise-evaluation) |
| §80 | Automatic Evaluation Role | [research/benchmark.md#automated-checks](../research/benchmark.md#automated-checks) |
| §81 | v0.3 Runtime Summary | [SKILL.md#runtime](../SKILL.md#runtime) |
| §82 | Legacy v0.3 Quality Gate (retained) | [core/revision.md#quality-gate--architecture](../core/revision.md#quality-gate--architecture) |
| §83 | Legacy Compact Runtime Instruction | [SKILL.md#compact-runtime-instruction](../SKILL.md#compact-runtime-instruction) |
| §84 | v0.4 Craft Layer | [core/prose.md#the-page-level-craft-layer](../core/prose.md#the-page-level-craft-layer) |
| §85 | Show–Tell Decision Engine | [core/prose.md#showtell-decision-engine](../core/prose.md#showtell-decision-engine) |
| §86 | Scene Entry / Exit Control | [core/scene-engine.md#scene-entry--exit-control](../core/scene-engine.md#scene-entry--exit-control) |
| §87 | Scene Goal, Resistance, Change | [core/scene-engine.md#scene-goal-resistance-change](../core/scene-engine.md#scene-goal-resistance-change) |
| §88 | Exposition and Backstory: Need-to-Know Routing | [core/information-architecture.md#exposition-and-backstory-need-to-know-routing](../core/information-architecture.md#exposition-and-backstory-need-to-know-routing) |
| §89 | Specificity Without Inventory | [core/prose.md#specificity-without-inventory](../core/prose.md#specificity-without-inventory) |
| §90 | POV and Psychic Distance Engine | [core/pov.md#pov-and-psychic-distance-engine](../core/pov.md#pov-and-psychic-distance-engine) |
| §91 | Dialogue and Subtext Engine | [core/dialogue.md#dialogue-and-subtext-engine](../core/dialogue.md#dialogue-and-subtext-engine) |
| §92 | Setup / Payoff Ledger | [core/information-architecture.md#setup--payoff-ledger](../core/information-architecture.md#setup--payoff-ledger) |
| §93 | Stakes and Tension | [core/scene-engine.md#stakes-and-tension](../core/scene-engine.md#stakes-and-tension) |
| §94 | Description and Worldbuilding Through Use | [core/world-state.md#description-and-worldbuilding-through-use](../core/world-state.md#description-and-worldbuilding-through-use) |
| §95 | Pacing: Scene vs Summary | [core/scene-engine.md#pacing-scene-vs-summary](../core/scene-engine.md#pacing-scene-vs-summary) |
| §96 | Character Behavior Test | [core/character-agency.md#character-behavior-test](../core/character-agency.md#character-behavior-test) |
| §97 | Common Human / Novice Writer Mistake Audit | [core/revision.md#common-human--novice-writer-mistake-audit](../core/revision.md#common-human--novice-writer-mistake-audit) |
| §98 | Reader-Trust / Redundancy Audit | [core/prose.md#reader-trust--redundancy-audit](../core/prose.md#reader-trust--redundancy-audit) |
| §99 | Endings: Consequence Without Over-Explanation | [core/endings.md#endings-consequence-without-over-explanation](../core/endings.md#endings-consequence-without-over-explanation) |
| §100 | Storytelling Question Bank | [core/question-bank.md#the-question-bank](../core/question-bank.md#the-question-bank) |
| §101 | Craft Revision Passes | [core/revision.md#craft-revision-passes](../core/revision.md#craft-revision-passes) |
| §102 | v0.4 Quality Gate | [core/revision.md#quality-gate--page-craft](../core/revision.md#quality-gate--page-craft) |
| §103 | v0.4 Compact Runtime Instruction | [SKILL.md#compact-runtime-instruction](../SKILL.md#compact-runtime-instruction) |

Operating-mode subsections (FAST SCENE, SHORT STORY, LONG-FORM, CRITIC) moved to the [router's mode table](../runtime/router.md#3-mode-selection); RESEARCH-GROUNDED MODE became [core/research-mode.md](../core/research-mode.md). The pack pointer sections (DRAFT STARTER, ORIGIN FORGE, TRAGIC ANIME STORY ENGINE, COMIC PANEL WRITER) were replaced by the [pack table](../SKILL.md#packs) and each pack's front-matter contract.

## Craft cards

v0.5's `craft/` directory held nine one-page cards that condensed material also present in the core. Each card now lives inside the module it summarizes, so there is one copy to maintain.

| v0.5 card | Now |
|---|---|
| `craft/show-tell.md` | [core/prose.md#showtell-quick-card](../core/prose.md#showtell-quick-card) |
| `craft/scene-craft.md` | [core/scene-engine.md#scene-quick-card](../core/scene-engine.md#scene-quick-card) |
| `craft/dialogue-subtext.md` | [core/dialogue.md#dialogue-quick-card](../core/dialogue.md#dialogue-quick-card) |
| `craft/pov-psychic-distance.md` | [core/pov.md#pov-quick-card](../core/pov.md#pov-quick-card) |
| `craft/exposition-backstory.md` | [core/information-architecture.md#exposition-quick-card](../core/information-architecture.md#exposition-quick-card) |
| `craft/common-mistakes.md` | [core/revision.md#mistake-matrix](../core/revision.md#mistake-matrix) |
| `craft/question-bank.md` | [core/question-bank.md](../core/question-bank.md) (questions the core bank lacked were appended) |
| `craft/revision-passes.md` | [core/revision.md#craft-revision-passes](../core/revision.md#craft-revision-passes) (its Exposition pass was missing from the core list and is now Pass 7) |
| `craft/storyscope-anti-defaults.md` | [core/critics.md#storyscope-evidence-summary](../core/critics.md#storyscope-evidence-summary) |

## Other moves

| v0.5 | Now |
|---|---|
| `research/research-pass-4.md` | [research/passes/pass-4-page-craft.md](../research/passes/pass-4-page-craft.md) |
| `research/benchmark.md` (v0.3 vs v0.4) | [research/benchmark.md](../research/benchmark.md), rewritten as baseline vs current |
