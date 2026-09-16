# Project State

One model for everything AI Writer knows about a project. Every schema elsewhere in the system — Draft Brief, Intent Lock, Story Genome, character and relationship state, memory, ledgers, pack briefs — is a view onto a branch of this tree.

**State is sparse.** A one-scene request may carry only a scene contract. A novel may fill most branches. Never populate a branch to satisfy the model. An empty branch means "not needed yet," not "missing."

**State is not the manuscript.** Prose stays in the user's files. State holds compact structured facts that point at those files.

---

## The model

```yaml
ai_writer_project:
  metadata:          # id, title, format, schema_version, created, updated, active_packs
  provenance:        # defaults and designated source-of-truth files
  intent_lock:       # core/intent-lock.md
  story_genome:      # core/story-genome.md
  canon:             # facts with provenance; see runtime/canon-resolver.md
  characters:        # id -> persona / developing_state / mental_state (core/character-model.md)
  relationships:     # "a--b" -> relationship record (core/relationships.md)
  world:             # rules, places, institutions, social state (core/world-state.md)
  timeline:          # temporal event facts (core/memory.md)
  outline:           # rough + detailed nodes, goals (core/outlining.md)
  open_loops:        # curiosity, suspense, reveal, and mystery threads
  reader_state:      # planned reader-state and affect curve (core/reader-state.md)
  setups_payoffs:    # the setup/payoff ledger (core/information-architecture.md)
  pack_state:        # pack id -> that pack's brief and ledgers
  continuity:        # open issues and resolutions (core/continuity.md)
  research:          # fact-labeled research items (core/research-mode.md)
  summaries:         # chapter/arc summaries for retrieval (core/memory.md)
```

### Where the existing schemas live

| Schema | Branch |
|---|---|
| `draft_brief` | `pack_state.draft-starter.draft_brief` |
| `origin_brief` | `pack_state.origin-forge.origin_brief` |
| `tragic_story_brief`, `hope_reserve`, `consequence_ledger`, `death_impact_card`, `power_cost_card`, `ensemble_pressure` | `pack_state.tragic-anime-engine.*` |
| `reveal_ledger` (tragic), `clue_ledger` (mystery) | `pack_state.<pack>.*`, with each open item mirrored as an `open_loops` entry |
| `comic_project`, `page` records | `pack_state.comic-panel-writer.*` |
| `intent_lock` | `intent_lock` |
| `story_genome` | `story_genome` |
| `persona`, `developing_state` | `characters.<id>.persona`, `characters.<id>.developing_state` |
| `mental_state`, `BDI` | `characters.<id>.mental_state` |
| `scene_state` | ephemeral; never persisted |
| `relationship`, `relationship_perception` | `relationships.<a>--<b>` |
| `social_state`, `sandbox.world_state` | `world.social`, `world.*` |
| `memory.canon_facts` | `canon.facts` |
| `memory.timeline`, `event_fact` | `timeline.events` |
| `memory.open_loops`, `curiosity_thread`, `suspense_thread`, `information_item` | `open_loops.items` |
| `memory.objects`, `memory.injuries_and_conditions` | `world.objects`, `characters.<id>.developing_state.conditions` |
| `memory.promises_and_debts` | `open_loops.items` (kind `promise`) |
| `setup_payoff` | `setups_payoffs.items` |
| `continuity_issue` | `continuity.issues` |
| `research_item` | `research.items` |
| `goal` | `outline.goals` |

**Series projects.** The top-level `intent_lock` and `story_genome` hold the series-wide contract. Each installment's own contract and genome live at `pack_state.series-engine.installments.<id>.intent_lock` and `.story_genome` (workspace: `.ai-writer/packs/series-engine/<id>.yaml`).

Packs keep their own schema shapes inside `pack_state.<pack-id>`. They do not redefine core branches. A pack that needs relationship data reads and writes `relationships`, not a private copy. See [pack authoring](../docs/PACK_AUTHORING.md#state).

---

## Provenance on records

Any record that states a fact can carry `prov`. Full form:

```yaml
prov:
  status: user_confirmed      # see the status list below
  source: "user, 2026-09-15"  # who or what established it
  since: 2026-09-15
  note:
```

Short form, when nothing else is needed:

```yaml
prov: agent_proposal
```

A record without `prov` inherits `provenance.default_status`, which is `agent_proposal` unless the user says otherwise. **Nothing is canon by default.**

**Statuses:** `user_confirmed`, `source_canon`, `approved_inference`, `delegated_decision`, `agent_proposal`, `uncertain`, `in_world_belief`, `character_belief`, `alternate_continuity`, `deprecated`, `retcon`. Their meanings and precedence are in [the canon resolver](canon-resolver.md#provenance-statuses).

```yaml
provenance:
  default_status: agent_proposal
  source_of_truth:            # files that outrank project state, in order
    - path: "Characters/Mara Quinn.md"
      scope: characters.mara-quinn
  continuities:               # optional; see canon resolver
    - id: main
      default: true
```

---

## Branch shapes

Only the fields a project uses need to exist.

```yaml
metadata:
  id: skiing-story
  title:
  format: short_story          # scene | short_story | novella | novel | series | comic | other
  schema_version: 1
  created: 2026-09-16
  updated: 2026-09-16
  active_packs: [draft-starter]
  mode: SHORT_STORY
```

```yaml
canon:
  facts:
    - id: f-001
      subject: port-calder
      fact: Port Calder sits on the north shore of the lake.
      prov: {status: user_confirmed, source: "user, 2026-09-15"}
      continuity: main
      visibility: world_truth    # world_truth | public_belief | secret | character_belief
      supersedes:
      superseded_by:
```

```yaml
characters:
  lena:
    persona: {}                # core/character-model.md#character-architecture
    developing_state: {}
    mental_state: {}           # per-character knowledge; drives the Perspective Filter
    arc: {}                    # optional; the Series pack stores arc progress here
    prov: user_confirmed
```

```yaml
relationships:
  lena--marcus:
    record: {}                 # core/relationships.md#relationship-state
    perception: {}             # packs/romance.md adds relationship_perception
    history: []                # event ids from timeline
```

```yaml
timeline:
  events:
    - id: e-014
      subject: marcus
      relation: knows
      object: bridge_is_rigged
      time: ch3.s21
      source: "Chapter 3.md"
      prov: user_confirmed
```

```yaml
open_loops:
  items:
    - id: q-003
      kind: curiosity          # curiosity | suspense | reveal | clue | promise | mystery
      question:
      opened_at:
      horizon:                 # when it should pay off
      status: open             # open | developing | paid | intentionally_open | abandoned
      pack: mystery            # set when a pack owns the item
      ref:                     # id inside pack_state
```

```yaml
continuity:
  issues: []                   # continuity_issue records
  resolutions: []              # {issue, decision, decided_by, date}
```

```yaml
summaries:
  - scope: ch3                 # scene | chapter | arc | season
    text:                      # a few sentences, written after the unit is final
    events: [e-012, e-013, e-014]
```

---

## Reading and writing state

- **Read narrowly.** Pull the branches the route needs. A scene between Lena and Marcus needs their records, their relationship, recent timeline events that involve them, and open loops they touch — not the whole project. See [retrieval](workspace.md#retrieval).
- **Write provenance honestly.** User statements are `user_confirmed`. Material from designated files is `source_canon`. The agent's inventions are `agent_proposal`, or `delegated_decision` when the user delegated that choice.
- **Promote only through the resolver.** A proposal becomes canon when the user approves it. The agent never flips a status on its own authority. See [promotion](canon-resolver.md#promotion).
- **Keep history.** Changed facts are superseded, not deleted.

---

## Without a workspace

In legacy mode the same model lives in the conversation. Build only the branches the task needs, keep provenance labels visible in planning output (for example, *confirmed / delegated / proposed / open*), and offer a workspace only when a project has grown enough to benefit from one.
