# Relationships

Relationship state between two people, and social state across a group. Both persist across scenes.

| Contract | |
|---|---|
| Invoked by | Router whenever two or more characters with history share a scene; the Romance pack extends this module. |
| When | Before a scene with relational stakes; after any scene that changes trust, power, or affection. |
| Needs | `relationships.<a>--<b>`; `characters` mental states. |
| Produces | Updated relationship records; social-state updates (rumor, reputation). |
| State | `relationships` — `.ai-writer/relationships/<a>--<b>.yaml`; group state under `world.social`. |
| Consumed by | [dialogue](dialogue.md), [scene-engine](scene-engine.md), [romance](../packs/romance.md). |
| Skip when | Strangers meeting once; relationships the scene doesn't touch. |
| Tests | F14, F24 |
| Research | [research/core/planning-memory.md](../research/core/planning-memory.md); for romance, [research/packs/romance.md](../research/packs/romance.md) |

---

## Relationship State

```yaml
relationship:
  trust:
  affection:
  dependence:
  fear:
  attraction:
  resentment:
  obligation:
  power_balance:
  current_misunderstanding:
  shared_secret:
  unspoken_need:
  recent_change:
```

Relationship trajectories must persist across scenes.

---

## Social-State Propagation

For stories with communities, institutions, teams, families, courts, schools, workplaces,
politics, or factions, track social information separately.

```yaml
social_state:
  reputation:
  public_belief:
  private_belief:
  rumors: []
  alliances: []
  obligations: []
  taboos: []
  status:
  institutional_pressure:
```

Information may propagate imperfectly.

A rumor should not become universal truth in one scene unless the story establishes a
mechanism capable of spreading it that quickly.
