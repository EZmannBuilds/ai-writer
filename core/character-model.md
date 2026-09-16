# Character Model

Major characters as stateful minds with limited knowledge. This module defines what a character is, what they know, and how that changes.

| Contract | |
|---|---|
| Invoked by | Router whenever a named character acts, speaks, or decides; [character-agency](character-agency.md) before every action proposal. |
| When | Before drafting any scene with a major character; after a consequential scene (state update). |
| Needs | `characters.<id>` from project state; the scene's events so far. |
| Produces | Updated `characters.<id>.developing_state`, `scene_state`, and `mental_state`. |
| State | `characters` — `.ai-writer/characters/<id>.yaml`. |
| Consumed by | [character-agency](character-agency.md), [dialogue](dialogue.md), [pov](pov.md), [continuity](continuity.md). |
| Skip when | Unnamed or one-line characters. Use only the Perspective Filter for them if they must infer something. |
| Tests | F12, F13 |
| Research | [research/core/character-cognition.md](../research/core/character-cognition.md), [research/core/planning-memory.md](../research/core/planning-memory.md) |

---

## Character architecture

*Basis: [@personas-to-plot], [@doc]*

Major characters are stateful narrative agents.

### Stable Persona

```yaml
persona:
  name:
  role:
  physical_description:
  personality:
  values: []
  deep_desires: []
  fears: []
  history: []
  competencies: []
  abilities: []
  limitations: []
  relationships: {}
  worldview:
  moral_boundaries: []
  recurring_contradictions: []
  habitual_defenses: []
```

### Developing State

```yaml
developing_state:
  current_goals: []
  beliefs: []
  false_beliefs: []
  relationship_states: {}
  unresolved_grudges: []
  loyalties: []
  secrets: []
  hopes: []
  psychological_trajectory:
```

### Immediate Scene State

```yaml
scene_state:
  location:
  physical_condition:
  emotional_state:
  current_goal:
  current_fear:
  current_assumption:
  known_information: []
  unknown_information: []
  concealed_information: []
  perceived_options: []
```

---

## Theory-of-Mind Character Model

*Basis: [@think-twice], [@beyond-words]*

A character must not reason from the author's omniscient context.

Maintain a separate mental-state model for every major character.

```yaml
mental_state:
  character:
  observed_facts: []
  believed_facts: []
  false_beliefs: []
  uncertain_beliefs: []
  desires: []
  intentions: []
  fears: []
  suspicions: []
  private_memories: []
  beliefs_about_others: {}
  beliefs_about_others_beliefs: {}
```

The last field is optional and should be used only when second-order social reasoning matters.

Examples:

```text
Lena knows the key is missing.
Lena believes Marcus took it.
Marcus knows Eli took it.
Marcus believes Lena suspects him.
Eli believes nobody noticed the key is gone.
```

Those are four different narrative facts.

Do not collapse them into:

```text
Everyone knows Eli took the key.
```

---

## Perspective Filter

*Basis: [@think-twice]*

Before generating a major character's:

- action;
- dialogue;
- private thought;
- inference;
- plan;

filter the story context to information that character could actually possess.

Use a two-stage procedure:

```text
STAGE 1 — PERSPECTIVE FILTER
Which events, facts, conversations, objects, and behaviors has this character perceived
or learned about?

STAGE 2 — MENTAL-STATE INFERENCE
Given only that filtered context, what does the character believe, want, fear, intend,
suspect, or misunderstand?
```

This prevents accidental omniscience and improves Theory-of-Mind reasoning.

A character may infer something that is not objectively true.

Keep separate:

```text
world truth
character observation
character interpretation
character belief
character intention
```

---

## Belief–Desire–Intention Loop

*Basis: [@beyond-words]*

For socially complex scenes, model each major character as:

```yaml
BDI:
  belief:
  desire:
  intention:
```

Then update dynamically:

```text
observation
→ belief update
→ desire pressure
→ intention
→ action
→ social consequence
→ new observation
```

Do not force beliefs to update instantly when evidence appears.

Characters may:

- rationalize;
- deny;
- misinterpret;
- cling to prior beliefs;
- update partially;
- distrust the evidence;
- change intention without changing belief.

---

## Second-Order Social Reasoning

Use when scenes depend on manipulation, romance, distrust, negotiation, embarrassment,
politics, deception, or rivalry.

Model statements such as:

```text
A thinks B is angry.
A thinks B believes A lied.
A wants B to think A is calm.
B knows A is pretending to be calm.
```

Do not recurse infinitely.

Default maximum:

```text
belief about another person's belief
```

Use deeper recursion only when it clearly matters.

---

## Dynamic character development

*Basis: [@doc]*

After a character participates in a consequential scene, update their developing state.

Do not rewrite their stable persona casually.

Example:

```text
stable:
Marcus values loyalty.

developing:
Marcus now believes Lena may expose his brother.

immediate:
Marcus intends to lie during dinner.

result:
After Lena protects him unexpectedly, Marcus's suspicion decreases but shame increases.
```

Character development should be accumulated state, not trait replacement.
