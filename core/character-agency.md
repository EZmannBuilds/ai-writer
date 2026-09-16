# Character Agency

Characters choose; the outline does not choose for them. Action proposals, the anti-puppet test, stagnation detection, and emergent simulation.

| Contract | |
|---|---|
| Invoked by | Router in LONG-FORM MODE (every important scene) and whenever a character must make a consequential choice. |
| When | Before drafting a scene with competing wants; when the story stalls; when a choice feels convenient. |
| Needs | Perspective-filtered state from [character-model](character-model.md); current outline node. |
| Produces | Accepted actions for the narrator; stagnation warnings; emergent events (sandbox). |
| State | Accepted actions become events in `timeline`; goal tracking lives in `outline.goals`. |
| Consumed by | [scene-engine](scene-engine.md), [outlining](outlining.md) (plan refresh). |
| Skip when | FAST SCENE MODE unless the user's scene hinges on a character decision; the user has dictated what the character does. |
| Tests | F12, F21 |
| Research | [research/core/planning-memory.md](../research/core/planning-memory.md) |

---

## Character Action Engine

*Basis: [@personas-to-plot]*

Before an important scene is drafted, participating major characters propose actions.

For each character, provide only information that character should have:

- persona;
- relevant relationships;
- current story goal;
- immediate scene state;
- recent history;
- relevant world state.

Ask for a concrete intended action.

Then run an Action Critic.

```yaml
action_critic:
  relevant_to_scene:
  specific:
  consistent_with_character:
  plausible:
  consistent_with_knowledge:
  advances_or_complicates_goal:
  non_repetitive:
  consequence_potential:
```

Reject or regenerate actions that are:
- vague;
- implausible;
- out of character;
- based on knowledge the character does not possess;
- repetitive;
- purely designed to satisfy the outline.

After several character actions are accepted, the Narrator chooses which actions actually enter the scene.

Not every proposed action must occur.

This lets plot emerge from competing agency.

---

## Character Behavior Test

Before major character action ask:

```yaml
character_choice:
  current_goal:
  current_belief:
  known_information:
  mistaken_information:
  fear:
  desire:
  relationship_pressure:
  social_pressure:
  available_options:
  option_rejected_and_why:
  chosen_action:
  immediate_cost:
  future_consequence:
```

### Anti-puppet rule

If the only reason a character acts is:
> "because the plot needs the next event"

revise motivation, information, pressure, or event.

### Contradiction rule

Characters may behave inconsistently when the inconsistency is psychologically legible.

A character can:
- love and resent;
- believe and doubt;
- want safety and sabotage it;
- know better and still choose badly.

Consistency means **stateful plausibility**, not mechanical predictability.

---

## Goal Sequencing and Stagnation Detection

*Basis: [@personas-to-plot]*

Long stories can stall around an unresolved goal.

Track the current story-level and local goals.

```yaml
goal:
  description:
  initiated_at:
  completion_conditions: []
  active_characters: []
  blockers: []
  progress:
  repetition_warning:
```

If several consecutive scenes:
- repeat the same attempt;
- produce no new information;
- do not change relationships;
- do not alter risk;
- do not reduce or expand available options;

the goal may be stalled.

Respond by:
- completing it;
- reframing it;
- replacing it;
- introducing a consequential new domain of conflict.

Do not use fixed step counts as universal rules.
Use stagnation evidence.

---

## Emergent Sandbox Mode

*Basis: [@storybox], [@bookworld]*

For ensemble, social, world-simulation, or highly character-driven fiction, optionally use a
hybrid bottom-up mode.

Initialize:

```yaml
sandbox:
  world_state:
  locations:
  institutions:
  resources:
  social_norms:
  active_characters:
  secrets:
  pressures:
```

Then simulate several short interaction rounds.

For each round:

```text
1. perspective-filter each character;
2. generate intention/action;
3. resolve compatible/conflicting actions;
4. update world state;
5. update beliefs and relationships;
6. log emergent events;
```

The Narrator then selects the events with the best narrative potential.

Do not transcribe the simulation literally.
Simulation generates material.
Narration shapes material.

---

## Hybrid Top-Down / Bottom-Up Plotting

*Basis: [@storybox]*

Use top-down planning for:

- thematic destination;
- major irreversible turns;
- ending contract;
- required mysteries;
- canon events.

Use bottom-up simulation for:

- interpersonal conflict;
- local consequences;
- secondary plots;
- alliance changes;
- rumors;
- unplanned complications;
- relationship development.

This reduces puppet-like characters without surrendering the entire story to simulation.
