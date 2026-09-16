# Workflow Traces

Seven end-to-end workflows traced by hand through the router, packs, core modules, and project state. Each step names the rule that drives it. The traces were done against v0.7 on 2026-09-16; gaps they exposed were fixed in the same pass and are listed at the end.

Notation: **Reads** and **Writes** are [project-state](../runtime/project-state.md) branches. Without a workspace, "writes" means the state is kept in the conversation.

---

## 1. Loose seed → Draft Starter → core planning → prose

**Request:** "Let's make a heartfelt story about skiing." No files, no workspace.

```yaml
route: {task: loose_seed, stage: seed, mode: SHORT_STORY, state_source: none,
        packs: [draft-starter], authority: collaborative, register: prose}
```

| # | Step | Rule | Reads | Writes |
|---|---|---|---|---|
| 1 | Classify: premise without a story shape | [task classifier](../runtime/router.md#1-task-classifier) | — | — |
| 2 | No workspace, no canon | [state lookup](../runtime/router.md#2-project-state-lookup) | — | — |
| 3 | A complete short work → SHORT_STORY | [mode selection](../runtime/router.md#3-mode-selection) | — | — |
| 4 | Gate passes: seed stage, no brief, no skip request | [Draft Starter gate](../runtime/router.md#45-pack-activation) | — | — |
| 5 | Interpret the seed; offer directions; ask 3–5 emotional-core questions. **Turn ends.** | [Draft Starter](../packs/draft-starter.md#response-pattern--first-turn) | — | `pack_state.draft-starter.interview_state` (round 1) |
| 6 | User answers. Synthesize; second round only if a major ambiguity remains | [after answers](../packs/draft-starter.md#response-pattern--after-answers) | interview_state | `draft_brief` with confirmed / delegated / proposed / open lists |
| 7 | Lock intent from the brief | [Intent Lock](../core/intent-lock.md) | draft_brief | `intent_lock` |
| 8 | Premise-family candidates; select for quality × distance | [creativity search](../core/creativity-search.md) | intent_lock | — (candidates are ephemeral) |
| 9 | Build the genome from the chosen candidate | [Story Genome](../core/story-genome.md) | intent_lock, brief | `story_genome` (prov: agent_proposal unless delegated) |
| 10 | Arc, reveal, and affect plan | [outlining](../core/outlining.md), [reader-state](../core/reader-state.md) | genome | `outline`, `reader_state` |
| 11 | Scene contracts → draft with POV, dialogue, show/tell choices | [scene engine](../core/scene-engine.md), [pov](../core/pov.md), [prose](../core/prose.md) | outline, characters | — |
| 12 | Critic council; revision macro → micro; quality gates | [critics](../core/critics.md), [revision](../core/revision.md) | intent_lock, genome | — |
| 13 | Continuity check; extract state; report proposals awaiting approval | [continuity](../core/continuity.md), [state extraction](../runtime/router.md#10-state-extraction) | draft | `timeline`, `characters` (as proposals) |

**Checks:** no prose before the emotional core is known (F01); settings the agent proposed in step 5 never become confirmed in step 6 (F04).

---

## 2. Military villain → Draft Starter → Origin Forge → Intent Lock → Story Genome → scene

**Request:** "Start Draft: a decorated officer becomes a supervillain after a strike goes wrong. Start Origin. Then write the scene where she makes the choice."

```yaml
route: {task: [loose_seed, origin, scene_request], stage: seed, mode: SHORT_STORY,
        research: triage, packs: [draft-starter, origin-forge], authority: collaborative}
```

| # | Step | Rule | Reads | Writes |
|---|---|---|---|---|
| 1 | Two explicit triggers → both packs; order front-door → identity | [pack order](../runtime/router.md#45-pack-activation) | — | — |
| 2 | Military procedure appears → research overlay (triage) | [research triggers](../core/research-mode.md#triggers) | — | — |
| 3 | Draft Starter: emotional core and non-negotiables, 3–5 questions | [Draft Starter](../packs/draft-starter.md) | — | interview_state, then `draft_brief` |
| 4 | Origin Forge reads the brief; states the transformation question | [Start-Origin procedure](../packs/origin-forge.md#start-origin-procedure) | draft_brief | — |
| 5 | Military module: decision environment; split actual / perceived / institutional responsibility | [military module](../packs/origin-forge.md#module-military-and-moral-conflict-origins) | draft_brief | — |
| 6 | Second test with a real alternative; the chosen crossing is separate from the strike | [origin spine](../packs/origin-forge.md#the-origin-spine) | — | `origin_brief` |
| 7 | Trauma guardrail: harm comes from choices and beliefs, not diagnosis | [guardrail](../packs/origin-forge.md#trauma-and-diagnosis-guardrail) | — | — |
| 8 | Research triage: rank, chain of command, and strike authorization are high-exposure → verify or fictionalize visibly; base decor is invention | [triage](../core/research-mode.md#verification-triage) | origin_brief | `research.items` with labels |
| 9 | Origin Brief seeds the character record | [Origin Forge state](../packs/origin-forge.md) | origin_brief | `characters.<id>.persona`, `.developing_state` |
| 10 | Intent Lock and Story Genome | [Intent Lock](../core/intent-lock.md), [Genome](../core/story-genome.md) | briefs | `intent_lock`, `story_genome` |
| 11 | The crossing scene: perspective filter on her; action proposal and anti-puppet test; scene contract | [perspective filter](../core/character-model.md#perspective-filter), [character agency](../core/character-agency.md) | characters, research | — |
| 12 | Draft; page-craft gate; extract state | [prose](../core/prose.md), [revision](../core/revision.md) | — | `timeline` (proposal) |

**Checks:** F06 (the disruption is not the villain turn), F20 (procedure labeled, not asserted).

---

## 3. Tragic supernatural series → Draft Starter → Tragic engine → Series Engine → long-form state

**Request:** "Start Draft. I want a tragic supernatural series — three seasons, a squad that hunts spirits. Dark Anime Mode. Start Series."

```yaml
route: {task: [loose_seed, tragic_story, series], stage: seed, mode: LONG_FORM,
        packs: [draft-starter, tragic-anime-engine, series-engine]}
```

| # | Step | Rule | Reads | Writes |
|---|---|---|---|---|
| 1 | Order: front-door → genre → scale | [pack order](../runtime/router.md#45-pack-activation) | — | — |
| 2 | Draft Starter brief | [Draft Starter](../packs/draft-starter.md) | — | `draft_brief` |
| 3 | Tragic activation: Hope Reserve, primary pressure, tragedy engines present | [activation procedure](../packs/tragic-anime-engine.md#xv-activation-procedure) | draft_brief | `tragic_story_brief`, `hope_reserve` |
| 4 | Ensemble pressure map for the squad | [ensemble pressure](../packs/tragic-anime-engine.md#x-ensemble-pressure) | — | `ensemble_pressure`; persona seeds in `characters` |
| 5 | Series promise stack; thread ledger for the world's mystery | [promise stack](../packs/series-engine.md#promise-stack), [thread ledger](../packs/series-engine.md#thread-ledger) | tragic brief | `pack_state.series-engine`; `open_loops` with installment horizons |
| 6 | Escalation plan across seasons; bigger-villain check | [escalation](../packs/series-engine.md#escalation) | reveal ledger | `escalation_plan` |
| 7 | Convergence plan now, so seeds go into season 1 | [convergence](../packs/series-engine.md#convergence) | thread ledger | `convergence_plan` |
| 8 | Series-wide Intent Lock and Genome; season 1 gets its own under `installments.s1` | [series projects](../runtime/project-state.md#where-the-existing-schemas-live) | all briefs | `intent_lock`, `story_genome`, `installments.s1.*` |
| 9 | The project is large and multi-session → **offer** a workspace | [initializing](../runtime/workspace.md#initializing) | — | nothing until the user agrees |
| 10 | If yes: seed files with provenance; list proposals for review | [workspace](../runtime/workspace.md) | — | `.ai-writer/` files |
| 11 | Per chapter: long-form scene loop; Tragic residue check at the critic step | [scene loop](../core/outlining.md#long-form-scene-loop), [pack checks](../runtime/router.md#68-core-module-selection) | consequence ledger | `consequence_ledger`, `timeline` |
| 12 | End of season: summary; carry-forward check before season 2 | [carry-forward](../packs/series-engine.md#carry-forward-check) | summaries | `summaries/s1.md` |

**Checks:** F08 (no death by default), F26 (escalation beyond power), F27 (no workspace created unasked).

---

## 4. Murder mystery → Draft Starter → Mystery → clue/reveal state → drafting

**Request:** "Start Draft: a murder at a lighthouse. Start Mystery. You pick the culprit."

```yaml
route: {task: [loose_seed, mystery], stage: seed, mode: SHORT_STORY,
        packs: [draft-starter, mystery], authority: autonomous}
```

| # | Step | Rule | Reads | Writes |
|---|---|---|---|---|
| 1 | "You pick the culprit" → delegated authority for that decision | [authority](../runtime/router.md#authority) | — | — |
| 2 | Draft Starter: brief with few or no questions | [Draft Starter](../packs/draft-starter.md) | — | `draft_brief` |
| 3 | Form and fair-play strictness recorded as pack constraints | [Intent Lock](../core/intent-lock.md#the-intent-lock-schema) | — | `intent_lock.pack_constraints.mystery` |
| 4 | Truth model first; culprit is a `delegated_decision` | [truth model](../packs/mystery.md#1-truth-model), [promotion](../runtime/canon-resolver.md#promotion) | — | `truth_model` |
| 5 | Suspects with secrets; knowledge written to their mental states | [suspects](../packs/mystery.md#2-suspects) | truth_model | `suspect_state`; `characters.*.mental_state` |
| 6 | Clue ledger with first-read and true meanings; mirrored to open loops | [clue ledger](../packs/mystery.md#3-clue-ledger) | truth_model | `clue_ledger`; `open_loops` (kind clue) |
| 7 | False solution; hypothesis log | [false solution](../packs/mystery.md#5-false-solution), [hypotheses](../packs/mystery.md#4-hypotheses) | clues | `hypothesis_log` |
| 8 | Reveal plan; all eight fairness tests | [reveal](../packs/mystery.md#6-reveal-and-reconstruction) | all ledgers | `reveal_plan` |
| 9 | Genome and outline with clue placement | [Genome](../core/story-genome.md), [outlining](../core/outlining.md) | reveal_plan | `story_genome`, `outline` |
| 10 | Drafting: perspective filter on each suspect; ledger check at the critic step | [pack checks](../runtime/router.md#68-core-module-selection) | ledgers | clue `status: placed` |
| 11 | Continuity treats planted misdirection as intentional | [resolver](../runtime/canon-resolver.md#before-calling-something-a-contradiction) | clue_ledger | — |

**Checks:** F16 (every load-bearing fact is a prior clue), F32 (herrings from secrets).

---

## 5. Horror scene request → FAST SCENE → Horror → scene contract → prose

**Request:** "Write the scene where Dana, alone in her late mother's farmhouse, realizes the house has started setting the table for two."

```yaml
route: {task: [scene_request, horror], stage: drafting, mode: FAST_SCENE,
        packs: [horror], core: [scene-engine, pov, prose, reader-state, character-model]}
```

| # | Step | Rule | Reads | Writes |
|---|---|---|---|---|
| 1 | Defined scene → FAST_SCENE, even though it's horror | [mode rules](../runtime/router.md#3-mode-selection) | — | — |
| 2 | Fear is the scene's engine → Horror activates (not a trivial description) | [activation rule 4](../runtime/router.md#45-pack-activation) | — | — |
| 3 | No Draft Starter: drafting stage, defined scene | [gate](../runtime/router.md#45-pack-activation) | — | — |
| 4 | Horror requires reader-state → loaded despite the FAST_SCENE table | [activation rule 6](../runtime/router.md#45-pack-activation) | — | — |
| 5 | Light procedure: baseline, threat model with a reveal ceiling, visibility ladder | [horror procedure](../packs/horror.md#procedure) | — | ephemeral |
| 6 | Dread curve with recovery beats | [dread curve](../packs/horror.md#dread-curve) | — | ephemeral |
| 7 | Scene contract: POV Dana, desire, resistance, reader question | [scene contract](../core/scene-engine.md#scene-contract) | — | — |
| 8 | Draft | [prose](../core/prose.md) | — | — |
| 9 | Horror audit at the critic step (one targeted critic) | [horror audit](../packs/horror.md#horror-audit) | — | — |

No candidate search, genome, or macro critics run. **Checks:** F19, F23, F31.

---

## 6. Romance continuation from an existing project → load state → relationship state → Romance → draft

**Request:** "Continue chapter 9 — Noor and Ines's first night back in the same apartment." Workspace present.

```yaml
route: {task: continuation, stage: continuing, mode: LONG_FORM, state_source: workspace,
        packs: [romance], core: [memory, relationships, character-model, dialogue, scene-engine, pov, prose]}
```

| # | Step | Rule | Reads | Writes |
|---|---|---|---|---|
| 1 | `.ai-writer/` exists → read `project.yaml` first | [state lookup](../runtime/router.md#2-project-state-lookup) | `metadata`, `intent_lock` | — |
| 2 | `active_packs: [romance]` and the scene touches the relationship → Romance active | [activation rule 5](../runtime/router.md#45-pack-activation) | metadata | — |
| 3 | No Draft Starter, no re-asking: continuation | [gate](../runtime/router.md#45-pack-activation) | — | — |
| 4 | Retrieval: entities Noor, Ines, the apartment → their records, the pair's relationship, recent events, the ch8 summary | [retrieval](../runtime/workspace.md#retrieval) | `characters`, `relationships/ines--noor`, `timeline`, `summaries/ch8` | — |
| 5 | Ending contract from `intent_lock.pack_constraints.romance` | [ending contract](../packs/romance.md#ending-contract) | intent_lock | — |
| 6 | Perception gap and love dimensions shape the chapter's pressure | [perception](../packs/romance.md#perception), [dimensions](../packs/romance.md#love-dimensions) | relationship record | — |
| 7 | Detailed outline refresh for ch9; scene contracts | [plan refresh](../core/outlining.md#plan-refresh) | outline | `outline.detailed` |
| 8 | Dialogue with hidden sentences; perspective filter on both | [dialogue](../core/dialogue.md), [perspective filter](../core/character-model.md#perspective-filter) | mental states | — |
| 9 | Draft; Romance perception update at the critic step | [pack checks](../runtime/router.md#68-core-module-selection) | — | — |
| 10 | Update state with provenance; report proposals | [updating](../runtime/workspace.md#updating) | — | `relationships/ines--noor` (proposal), `timeline`, `project.yaml` updated |

**Checks:** F33, F14, F24.

---

## 7. Comic villain origin → Origin Forge → Comic Panel Writer → page/panel output

**Request:** "Start Origin for my villain Kestrel (notes attached). Then Comic Mode: a page breakdown of her chosen crossing."

```yaml
route: {task: [origin, comic_output], stage: planning, mode: SHORT_STORY, state_source: context,
        packs: [origin-forge, comic-panel-writer], register: comic_panel_breakdown}
```

| # | Step | Rule | Reads | Writes |
|---|---|---|---|---|
| 1 | Notes supply the premise → Draft Starter gate fails (not seed stage, premise exists) | [gate](../runtime/router.md#45-pack-activation) | supplied notes | — |
| 2 | Origin Forge from canon; questions only if consequential | [Start-Origin procedure](../packs/origin-forge.md#start-origin-procedure) | notes (`source_canon`) | `origin_brief` |
| 3 | Comic Panel Writer is an output register → after planning | [pack order](../runtime/router.md#45-pack-activation) | — | — |
| 4 | Comic Panel Writer requires scene-engine → loaded | [activation rule 6](../runtime/router.md#45-pack-activation) | — | — |
| 5 | Bridge: Second Test shows a visible alternative; Chosen Crossing gets visual weight | [Origin Forge bridge](../packs/comic-panel-writer.md#integration-with-origin-forge) | origin_brief | — |
| 6 | Panel Breakdown mode: page jobs, panel beats, page-turn notes | [output modes](../packs/comic-panel-writer.md#output-modes) | — | `comic_project`, `pages` |
| 7 | Production checks: drawable, one beat per panel, reveal protection | [production checks](../packs/comic-panel-writer.md#production-checks) | — | — |

**Checks:** F34, F17, F18.

---

## Gaps found by tracing, and fixes

| Gap | Found in | Fix |
|---|---|---|
| A pack could require a core module the mode table doesn't load (Horror needs reader-state in FAST_SCENE) | Trace 5 | Router activation rule 6: an active pack's `requires` load with it |
| Continuations didn't say which packs were active | Trace 6 | Router activation rule 5: `metadata.active_packs` restore on continuation |
| Nothing said when packs' drafting-time checks run | Traces 3, 4, 6 | Router "pack drafting checks" at the critic step; a note in the long-form scene loop |
| Intent Lock had nowhere to put pack constraints (fair play, ending contract) | Traces 4, 6 | `intent_lock.pack_constraints` |
| Series installments had nowhere to store their own contract and genome | Trace 3 | `pack_state.series-engine.installments.<id>` |
| Skip conditions contradicted explicit triggers (a complete premise would skip "Start Draft") | Fixture F05 while tracing 1 | Skip conditions veto only natural-language activation; the Draft Starter gate always honors "Start Draft" |
| Bedtime-story request had no task type | Fixture F21 | New task `story_request` |
