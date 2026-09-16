# Memory

Long-form memory: a structured state store, a temporal event graph, and selective retrieval into a compact drafting packet.

| Contract | |
|---|---|
| Invoked by | Router in LONG-FORM MODE and in any continuation of an existing project. |
| When | Before planning or drafting a scene (retrieval); after drafting (extraction). |
| Needs | Project state (workspace or context); the current scene's entities. |
| Produces | `draft_context` packet; new `timeline` event facts. |
| State | `timeline`, `summaries` — `.ai-writer/timeline.yaml`, `.ai-writer/summaries/`. See [workspace](../runtime/workspace.md#retrieval). |
| Consumed by | [scene-engine](scene-engine.md), [continuity](continuity.md). |
| Skip when | One-off scenes with no prior project; FAST SCENE MODE unless continuing a project. |
| Tests | F12, F27 |
| Research | [research/core/planning-memory.md](../research/core/planning-memory.md) |

---

## Memory Architecture

*Basis: [@dome]*

Long-form generation requires explicit memory.

Use two complementary layers.

### Narrative State Store

```yaml
memory:
  canon_facts: []
  character_states: {}
  relationship_states: {}
  world_state: {}
  timeline: []
  open_loops: []
  motifs: []
  objects: {}
  injuries_and_conditions: {}
  promises_and_debts: []
  unresolved_information: []
```

### Temporal Event Graph

Represent important changes as time-indexed statements.

```yaml
event_fact:
  subject:
  relation_or_action:
  object_or_value:
  time_index:
  source_scene:
```

Examples:

```text
(Lena, trusts, Marcus, chapter_2)
(Lena, distrusts, Marcus, chapter_7)
(key, located_at, basement_safe, scene_14)
(Marcus, knows, bridge_is_rigged, scene_21)
```

The graph does not replace prose memory.
It enables targeted retrieval and contradiction detection.

---

## Memory Retrieval

*Basis: [@dome]*

Before planning or writing:

1. extract entities from the current query/scene;
2. retrieve relevant memory facts;
3. rank by semantic relevance and recency;
4. keep only the useful subset;
5. surface temporal changes when important.

Avoid flooding the writer with every stored fact.

For a scene involving Lena and Marcus, retrieve:
- their relationship history;
- current trust state;
- promises;
- recent conflict;
- knowledge asymmetries;
- relevant shared objects/events.

---

## Structured Drafting Context

*Basis: [@doc]*

When drafting a scene, do not dump the entire story into context blindly.

Retrieve a compact packet:

```yaml
draft_context:
  current_scene_contract:
  current_outline_node:
  next_outline_node:
  immediate_previous_scene:
  near_past_summary:
  far_past_relevant_facts:
  active_character_states:
  relationship_states:
  current_setting:
  relevant_world_rules:
  relevant_open_loops:
  continuity_warnings:
```

Including the next outline node can help transitions, but the writer must not prematurely execute future events.
