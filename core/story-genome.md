# Story Genome

The identity of the story: what it is about, what it promises, and what it must not become.

| Contract | |
|---|---|
| Invoked by | Router, directly after Intent Lock. |
| When | SHORT STORY and LONG-FORM modes; any time the premise, dramatic question, or ending contract changes. |
| Needs | `intent_lock`; Draft Brief and pack briefs if present; chosen candidate from [creativity-search](creativity-search.md). |
| Produces | `story_genome` |
| State | `story_genome` — `.ai-writer/story-genome.yaml`. |
| Consumed by | [outlining](outlining.md), [critics](critics.md), [endings](endings.md), [series-engine](../packs/series-engine.md). |
| Skip when | FAST SCENE MODE unless a genome already exists (then read it, don't rebuild it). |
| Tests | F02, F19 |
| Research | [research/core/planning-memory.md](../research/core/planning-memory.md) |

---

## The Story Genome schema

The Story Genome stores the identity of the story.

```yaml
story_genome:
  premise:
  dramatic_question:
  central_desire:
  central_pressure:
  central_unknown:
  central_contradiction:
  protagonist:
  major_relationships: []
  important_world_rules: []
  thematic_questions: []
  emotional_destination:
  reader_contract:
  ending_contract:
  motifs: []
  structural_permissions: []
  anti_goals: []
```

`anti_goals` are outcomes the writer should avoid, such as:

```yaml
anti_goals:
  - do not turn the conflict into a simple good-vs-evil morality play
  - do not resolve the romance through a last-minute misunderstanding
  - do not reveal the monster's complete origin
```
