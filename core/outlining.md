# Outlining

A rough outline that keeps the destination, and a detailed outline that is written just before it is needed and rewritten when the story changes.

| Contract | |
|---|---|
| Invoked by | Router in SHORT STORY and LONG-FORM modes; the Series pack for season-level planning. |
| When | After Story Genome; before each drafting region (expansion); after each consequential scene (refresh). |
| Needs | `story_genome`; pack briefs; `timeline`; accepted character actions. |
| Produces | `outline` (rough + detailed nodes), turning points, the long-form scene loop. |
| State | `outline` — `.ai-writer/outline.yaml`. |
| Consumed by | [scene-engine](scene-engine.md), [memory](memory.md), [series-engine](../packs/series-engine.md). |
| Skip when | FAST SCENE MODE; the user has supplied a fixed outline (then refresh only, never re-plan). |
| Tests | F19, F26 |
| Research | [research/core/planning-memory.md](../research/core/planning-memory.md) |

---

## Dynamic Hierarchical Outline

Do not fully over-specify a novel before writing it.

Maintain two planning levels:

```text
ROUGH OUTLINE
  large movements and destination points

DYNAMIC DETAILED OUTLINE
  near-future chapters/scenes generated just before they are needed
```

Structure:

```text
Story
└── major movement
    └── sequence
        └── chapter
            └── scene
                └── beat
```

The rough outline preserves overall shape.
The detailed outline adapts to what the story has actually become.

---

## Rough Outline

The rough outline should contain:

```yaml
rough_outline_node:
  function:
  characters:
  setting:
  major_change:
  conflict:
  revelation:
  emotional_direction:
  required_setup:
  future_dependency:
```

Do not require one universal act structure.

Possible organizing systems include:
- acts;
- movements;
- phases;
- investigations;
- seasons;
- locations;
- relationship stages;
- viewpoint cycles;
- missions;
- ritual stages.

Use the structure appropriate to the project.

---

## Detailed Outline Expansion

Expand outline nodes recursively when more detail is needed.

For each parent node:

1. Generate 2-4 possible child-event sets.
2. Reject causal contradictions.
3. Reject redundancy.
4. Select the strongest set.
5. assign:
   - setting;
   - active characters;
   - information changes;
   - relationship changes;
   - relevant memory;
   - next-node transition.

Prefer breadth-first expansion when constructing an initial detailed region, then just-in-time expansion during drafting.

Do not pre-expand the entire novel unless needed.

---

## Turning-Point Planning

For longer stories, identify meso-level turns.

A turning point should alter at least one:

- goal;
- interpretation;
- relationship;
- available option;
- power balance;
- stakes;
- identity;
- location/domain;
- reader model of the story.

Do not confuse:
- "a dramatic event happened"
with
- "the narrative changed direction."

---

## Plan Refresh

After a meaningful scene or chapter:

Ask:

- Did any character choose an unexpected path?
- Did a relationship become more important?
- Did a revelation arrive earlier than planned?
- Did a planned twist become obvious?
- Did a secondary character become causally important?
- Did the world state change?
- Did the story discover a stronger thematic question?
- Is the planned ending still credible?

Update the detailed outline.

Update the rough outline only when the larger direction genuinely changes.

---

## Long-Form Scene Loop

```text
A. retrieve relevant memory
B. inspect current rough/detailed outline
C. generate/refresh scene contract
D. character agents propose actions
E. action critic accepts/rejects
F. narrator selects useful actions
G. draft scene
H. extract new state/events
I. update temporal event graph
J. run targeted critics
K. revise selectively
L. run continuity check
M. update detailed outline
N. continue
```
