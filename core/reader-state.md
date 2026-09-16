# Reader State

What the reader is feeling, tracking, and able to picture — as a changing state, never a constant maximum.

| Contract | |
|---|---|
| Invoked by | Router in SHORT STORY and LONG-FORM modes; genre packs (Horror's dread curve, Mystery's reader hypotheses) write into it. |
| When | Planning an arc; after major chapters (transportation audit); when complexity climbs. |
| Needs | `outline`; `story_genome.reader_contract`. |
| Produces | `reader_state` curve, affect plan, transportation and effort audits. |
| State | `reader_state` — `.ai-writer/project.yaml`. |
| Consumed by | [suspense-curiosity-surprise](suspense-curiosity-surprise.md), [critics](critics.md), [horror](../packs/horror.md), [mystery](../packs/mystery.md). |
| Skip when | FAST SCENE MODE (use the scene contract's `reader_question` instead). |
| Tests | F23 |
| Research | [research/core/reader-psychology.md](../research/core/reader-psychology.md) |

---

## Reader-State Model

*Basis: [@human-level-narratives]*

Captivation is a changing state, not a constant maximum.

Track:

```yaml
reader_state:
  curiosity:
  suspense:
  emotional_intensity:
  uncertainty:
  empathy:
  attachment:
  information_debt:
  narrative_momentum:
  cognitive_load:
```

Use descriptive labels or rough 0-100 planning estimates.

Do not pin everything high.

A useful pattern may be:

```text
curiosity rises
→ answer
→ quiet intimacy
→ new implication
→ dread
→ false relief
→ social pressure
→ revelation
→ recontextualization
→ aftermath
```

Variation is the point.

---

## Affect Curve

*Basis: [@human-level-narratives]*

Track at least:

```text
valence: negative ↔ positive
arousal: calm ↔ intense
control: powerless ↔ powerful
```

Avoid automatic positivity drift.

After hardship, a character does not need to:
- learn a lesson;
- forgive;
- become hopeful;
- articulate growth.

Emotional trajectories may end:
- conflicted;
- numb;
- energized;
- angry;
- accepting;
- obsessed;
- uncertain;
- unchanged.

---

## Reader Situation Model

*Basis: [@event-indexing]*

Readers build an internal model of story events.

Track each important event across:

```yaml
event_index:
  time:
  space:
  active_entities: []
  causality:
  intentionality:
```

Optional additions:

```yaml
  emotional_state:
  object_state:
  social_state:
```

The core five dimensions are:

- time;
- space;
- protagonist/entity;
- causality;
- intentionality/goal.

When a new event sharply changes several dimensions at once, the reader must rebuild part
of the mental model.

Use this deliberately.

---

## Narrative Transportation

*Basis: [@green-brock-2000], [@van-laer-2014]*

A captivating story should make it easy for the reader to mentally enter and remain in the
story world.

Narrative transportation involves:

- cognitive involvement;
- emotional involvement;
- mental imagery;
- attention focused on the narrative world.

Use transportation as a reader-state lens, not a prose-style command.

---

## Transportation Prerequisites

*Basis: [@green-brock-2000], [@van-laer-2014]*

Check:

```yaml
transportation:
  situation_model_clarity:
  character_connection:
  active_goal_or_question:
  emotional_access:
  concrete_world_cues:
  causal_legibility:
  attentional_friction:
```

High transportation does not require maximal description.

A few well-selected concrete cues can be more immersive than a paragraph cataloguing
every surface.

Major transportation breakers include:

- accidental POV omniscience;
- contradictory geography;
- unexplained causal jumps;
- character behavior that ignores established motivation;
- exposition inserted at moments of high action;
- excessive clarification;
- arbitrary tonal changes.

---

## Transportation Audit

Ask after major chapters:

```text
Can the reader currently picture where the important action is occurring?
Do they know whose experience they are following?
Do they understand the active desire/problem?
Is there enough causal connection to predict possibilities?
Is the prose asking them to remember too many low-value facts?
Did the chapter interrupt an emotionally active moment with unnecessary explanation?
```

Do not turn the audit into "add more imagery."

---

## Reader Effort Budget

Readers can enjoy complexity while still needing footholds.

Track:

```yaml
reader_effort:
  active_characters:
  active_mysteries:
  timeline_layers:
  viewpoint_switches:
  unexplained_terms:
  unresolved_causal_links:
  simultaneous_goals:
```

Complexity is not inherently bad.

When several dimensions become demanding simultaneously, provide an anchor:

- familiar location;
- stable viewpoint;
- concrete immediate goal;
- repeated object;
- relationship;
- clear causal consequence.

This allows structural complexity without fog.

---

## Event-Level Flow, Not Token Predictability

*Basis: [@fiction-flows]*

Do not optimize story flow using simple sentence-level predictability alone.

Recent replication work on narrative sequentiality found that apparent effects can change
substantially under alternative measurement choices.

Treat flow as an event-level phenomenon involving:

- expectation;
- memory;
- causal continuity;
- goal continuity;
- rhythm;
- event segmentation.

Use token/sentence predictability metrics only as optional diagnostics.
