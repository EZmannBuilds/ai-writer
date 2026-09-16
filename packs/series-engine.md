---
pack:
  id: series-engine
  name: Series / Season Engine
  version: "1.0"
  stage: scale
  pipeline_position: After genre packs, before Intent Lock. Each installment then gets its own Intent Lock and Story Genome under the series plan.
  purpose: Plan stories larger than one book or arc — nested promises, long-horizon threads, escalation that isn't just a bigger villain, and finales that converge.
  triggers: ["Start Series"]
  natural_language_triggers: ["plan season 2", "book two", "the saga", "series arc", "multi-book", "next installment", "episode arc"]
  requires: ["core/outlining", "core/memory"]
  optional_dependencies: ["draft-starter", "tragic-anime-engine", "mystery", "romance"]
  conflicts_with: []
  stacks_with: ["draft-starter", "origin-forge", "tragic-anime-engine", "mystery", "horror", "romance", "worldbuilding", "comic-panel-writer"]
  inputs: ["prior installment summaries", "story_genome per installment", "open_loops", "character arcs"]
  produces: ["series_plan", "promise_stack", "thread_ledger", "escalation_plan", "arc_ledger", "faction_tracks", "motif_ledger", "convergence_plan"]
  skip_when:
    - A single standalone story, even a long one.
    - The user wants to plan only the current installment and has said so.
  state_keys: ["pack_state.series-engine", "open_loops", "characters.<id>.arc", "relationships", "summaries", "world"]
  research_basis: research/packs/series-engine.md
  behavior_tests: ["F26"]
---

# Series / Season Engine

## Purpose

A series has promises at several scales at once. Each installment must satisfy on its own and move the larger story. The common failure is structural: every new season invents a stronger villain, last season's consequences evaporate, and the finale introduces material that was never seeded.

This pack keeps a **promise stack**, a **thread ledger** for long-horizon questions, **escalation on more than one axis**, arc and relationship trajectories, and a **convergence plan** for the end.

It sits on top of [outlining](../core/outlining.md) (a series is the top of the hierarchy) and [memory](../core/memory.md) (installment summaries are how later seasons remember earlier ones).

## Activation

- **Explicit:** "Start Series".
- **Natural language:** planning book two, season two, a saga, a multi-installment arc.
- **Continuation:** when a workspace has `metadata.format: series`, the pack's ledgers load for installment planning (not for single scenes).

## Skip conditions

- A standalone work.
- A scene or chapter request inside a series — read the thread ledger if the scene touches a long thread; don't run the procedure.

## Pipeline position

```text
Draft Starter → (Origin Forge) → genre packs → Series Engine
→ per installment: Intent Lock → Story Genome → outline → drafting
→ after each installment: summarize → update ledgers → escalation review
```

## Inputs

Prior installment summaries, current genomes, open loops, character and relationship state, faction state.

## Outputs

`series_plan`, `promise_stack`, `thread_ledger`, `escalation_plan`, `arc_ledger`, `faction_tracks`, `motif_ledger`, `convergence_plan`.

## State

- **Produces:** `pack_state.series-engine.*`, including `installments.<id>.intent_lock` and `installments.<id>.story_genome` for each installment. The top-level project branches hold the series-wide contract.
- **Writes to core:** long threads become `open_loops` items with a `horizon` naming an installment; character arc progress goes to `characters.<id>.arc`; faction changes go to `world`.
- **Summaries are required.** At the end of each installment, write `summaries/<installment>.md` with its event ids. Later seasons retrieve summaries, not manuscripts.

## Procedure

```text
1. Read everything that exists: summaries, genomes, open loops, arcs.
2. Write or confirm the PROMISE STACK.
3. Build the THREAD LEDGER: every long question, its horizon, its clue/answer schedule.
4. Plan ESCALATION across axes; check the bigger-villain default.
5. Track ARCS: characters, relationships, factions.
6. Plan the installment: its promise, its antagonist or pressure, what it pays, what it opens.
7. Check CARRY-FORWARD: what the last installment changed that must still be true.
8. Plan CONVERGENCE for the final installment (early — seeds go in now).
9. After the installment: summarize, update ledgers, review escalation.
```

### Promise stack

```yaml
promise_stack:
  series:                     # what the whole work promises (question, feeling, change)
  installment:                # season/book promise
  arc:                        # arc promise within the installment
  unit:                       # episode/chapter promise
  scene:                      # scene promise (usually from the scene contract)
```

Each level must be satisfiable **on its own terms** and must **feed the level above**. An episode that only sets up the season fails its own promise; a season that pays nothing forward fails the series.

### Thread ledger

```yaml
thread_ledger:
  - id:
    question:
    scale:                    # series | installment | arc
    opened_in:
    horizon:                  # installment where it should pay off
    partial_answers: []       # {installment, answer, new_question}
    clues: []
    status:                   # open | developing | paid | intentionally_open | abandoned
    risk:                     # stalling | overgrown | forgotten | on_track
```

Rules:

- **Pay something every installment.** Each installment answers at least one long question in part and transforms it into a larger or sharper one (`ANSWER → RECONTEXTUALIZATION → LARGER QUESTION`).
- **Don't open faster than you pay.** Track open-thread count per installment; flag growth without payoff.
- **Abandon deliberately.** A dropped thread is marked `abandoned` with a reason, or `intentionally_open`.

### Escalation

Stronger enemies are one axis of seven. Alternate them.

| Axis | Direction |
|---|---|
| **Threat scale** | person → team → city → nation → world |
| **Truth** | rumor → secret → institutional truth → historical truth → cosmological truth |
| **Moral** | clear defense → compromised necessity → faction conflict → impossible choice |
| **Personal** | stranger → ally → family → self → identity |
| **Cost** | fatigue → injury → sacrifice → irreversible loss |
| **Agency** | reacting → choosing → leading → responsible for others |
| **Relationship** | new bond → tested bond → broken or transformed bond |

The first six axes come from the [Tragic engine's escalation model](tragic-anime-engine.md#ix-escalation), generalized; relationship is added here.

**Bigger-villain check.** If the plan for the next installment's antagonist can be summarized as "stronger than the last one," revise. Better season antagonists threaten something the last one couldn't:

- the protagonists' **beliefs** (an ideological rival who might be right);
- their **relationships** (someone inside the team, or a loved one on the other side);
- the **consequences** of the last victory (the power vacuum, the people it harmed);
- the **truth** they built on (the last season's win rested on a lie);
- their **identity** (what winning turned them into).

```yaml
escalation_plan:
  - installment:
    primary_axes: []          # at least two, not only threat_scale
    antagonist_or_pressure:
    what_it_threatens:        # beliefs | relationships | consequences | truth | identity | ...
    carries_forward: []       # consequences from earlier installments that still bite
    bigger_villain_check:     # pass | revise, with reason
```

### Arcs and trajectories

```yaml
arc_ledger:
  - character:
    series_arc:               # the long change (or refusal to change)
    installment_steps: []     # {installment, state_before, state_after, trigger}
    relationship_trajectories: []   # {with, direction, installment_steps}
    regression_allowed: true  # people backslide; plan it on purpose
```

```yaml
faction_tracks:
  - faction:
    installment_states: []    # {installment, power, goal, internal_split, relation_to_protagonists}
```

Arcs change unevenly. A character can regress in season 3 because of what season 2 cost. Record the cause.

### Motifs and callbacks

```yaml
motif_ledger:
  - motif:
    first_seen:
    appearances: []           # {installment, meaning_then}
    final_meaning:
```

A callback should mean something new each time it returns.

### Carry-forward check

Before planning the next installment, list what the last one changed — deaths, injuries, power costs, broken trust, political shifts, secrets now known — and confirm each is still true or was deliberately changed on the page. Consequences don't expire between seasons.

### Convergence

Plan the end early so its seeds can be planted.

```yaml
convergence_plan:
  central_question:           # the one question the finale answers
  debts_arriving: []          # thread ids, arcs, relationships, costs, motifs
  final_cost:                 # what the ending takes from the protagonist's original desire
  seeds: []                   # {installment, seed}
  forbidden: []               # e.g., new cosmology in the finale; a villain with no thematic tie
```

A finale should feel like many debts arriving at once. Avoid new cosmology late, a final villain with no thematic connection, undoing losses to soften the end, and ending the moment the climax does.

## Guardrails

- Each installment satisfies its own promise.
- Consequences persist across installments unless changed on the page.
- Escalation uses at least two axes per installment.
- Long threads get partial payoffs; nothing stays open by neglect.
- Agent-planned future events are proposals until approved; they don't become canon because they're in a plan.

## Failure modes

| Failure | Looks like | Fix |
|---|---|---|
| Power creep | Each season's villain is stronger | Threaten beliefs, relationships, consequences, truth, or identity |
| Reset season | Last season's costs vanish | Run the carry-forward check |
| Mystery box | Threads multiply, none pay | Partial answer each installment; cap open threads |
| Filler installment | Sets up the next one, pays nothing | Give it its own promise and payoff |
| Late cosmology | The finale explains everything with new material | Seed it seasons earlier |
| Frozen arcs | Characters end each season where they started | Log installment steps |

## Schemas

```yaml
series_plan:
  version: "1.0"
  format:                     # book_series | tv_seasons | web_serial | comic_run | saga
  installments_planned:
  promise_stack_ref:
  current_installment:
  central_question:
  provenance: {confirmed_facts: [], delegated_decisions: [], agent_proposals: [], unresolved_questions: []}
```

Other schemas appear in the procedure.

## Examples

*(Generic demo.)* Season 1 of an urban-fantasy show ends with the team defeating the Ash King.

- **Series promise:** can a city that runs on bargains with the dead ever be free?
- **Season 2 promise:** what does the city become without the king who enforced the bargains?
- **Escalation:** *consequences* (the bargains now go unenforced, and the dead start collecting on their own) and *moral* (the team must decide whether to become the enforcers).
- **Antagonist:** not a stronger king — a popular reform movement led by a former ally, arguing that the team is the new tyranny. It threatens the team's belief that they were the good side.
- **Carry-forward:** the captain's burned hand from the finale; the truce with the river court; the secret that the Ash King's crown is still missing.
- **Thread paid:** who crowned the Ash King (answered: the city council, a century ago) → larger question: what did the council get in return?

## Behavior tests

| Fixture | Checks |
|---|---|
| [F26](../tests/fixtures/F26-series-escalation-not-bigger-villain.yaml) | At least two non-power escalation axes; season-1 consequences carry forward; the antagonist's threat isn't raw power. |

## Research provenance

[research/packs/series-engine.md](../research/packs/series-engine.md). This pack is a **design** module: it generalizes the core's hierarchical outlining and memory research and the Tragic engine's escalation model to multi-installment scale. No series-specific empirical source was used.

## Integration

- **Core:** the promise stack sits above [rough outlines](../core/outlining.md#rough-outline); summaries feed [memory retrieval](../core/memory.md#memory-retrieval); long threads are `open_loops`.
- **Tragic engine:** its consequence ledger and endgame convergence are the per-installment and finale views of the same debts.
- **Mystery:** a series mystery is a thread ledger item whose clues span installments; each installment solves a smaller case.
- **Romance:** relationship trajectories live in the arc ledger.
- **Worldbuilding:** faction tracks read from and write to world systems.
