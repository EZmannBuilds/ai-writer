# Scene Engine

The scene contract, and the craft tests that decide where a scene starts, what it changes, and where it stops.

| Contract | |
|---|---|
| Invoked by | Router in every drafting mode, including FAST SCENE MODE. |
| When | Before drafting any scene; during revision (Scene necessity and Entry/Exit passes). |
| Needs | The request or outline node; relevant character and relationship state. |
| Produces | `scene_contract`; the scene diagnostic verdict. |
| State | Ephemeral for one-off scenes. In a project, the contract's `state_change` and `next_scene_pressure` feed `timeline` and `open_loops`. |
| Consumed by | [prose](prose.md), [dialogue](dialogue.md), [pov](pov.md), genre packs. |
| Skip when | Never skipped when drafting. Contract depth scales with mode: FAST SCENE MODE fills only the fields the scene uses. |
| Tests | F02, F19, F23 |
| Research | [research/core/page-craft.md](../research/core/page-craft.md) |

---

## Scene Contract

The contract is a working tool. For a scene request, fill it internally and return the scene; show the contract only when the user is planning or asks to see it.

```yaml
scene_contract:
  pov_character:
  location:
  time:
  current_story_goal:
  scene_goal:
  opposition:
  hidden_pressure:
  active_characters:
  reader_question:
  knowledge_asymmetry:
  information_change:
  relationship_change:
  emotional_turn:
  state_change:
  next_scene_pressure:

  # page-craft fields (see prose.md, pov.md, information-architecture.md)
  scene_entry_pressure:
  scene_exit_turn:
  hidden_sentence:
  surface_topic:
  concrete_anchor_detail:
  psychic_distance_start:
  psychic_distance_target:
  show_moments: []
  tell_summary_moments: []
  exposition_needed_now: []
  exposition_deferred: []
  setup_items: []
  payoff_items: []
  silence_or_omission:
  continuity_risks: []
```

A scene should usually change at least one:
- knowledge;
- relationship;
- risk;
- power;
- desire;
- interpretation;
- available action;
- commitment.

---

## Scene Goal, Resistance, Change

*Basis: [@reedsy-scene-anatomy]*

A functional scene usually contains:

```text
DESIRE
→ ATTEMPT
→ RESISTANCE
→ ADAPTATION / CHOICE
→ CHANGE
```

Conflict does not require shouting, violence, or an antagonist.

Resistance can be:
- another person's goal;
- social etiquette;
- shame;
- lack of information;
- time;
- weather;
- physical limitation;
- institutional rules;
- memory;
- self-deception;
- incompatible loyalties.

### Scene diagnostic

Ask:

```yaml
scene_diagnostic:
  what_does_pov_character_want_now:
  why_now:
  what_is_their_plan:
  what_resists:
  what_will_it_cost:
  what_tactic_changes:
  what_new_information_arrives:
  what_choice_becomes_possible_or_impossible:
  what_is_different_at_exit:
  what_pressure_carries_forward:
```

If the answer to "what changes?" is **nothing**, classify the scene:

```text
atmosphere / character texture by design
or
candidate for compression / removal
```

Do not keep a scene merely because its prose is attractive.

---

## Scene Entry / Exit Control

*Basis: [@reedsy-pacing]*

Use **enter late, leave early** as a test, not a commandment.

### Enter late

Before a scene starts, ask:

- What preparation can the reader infer?
- What is the first moment the character's desire meets pressure?
- Can five lines of arrival/setup disappear without confusion?
- Is the current opening only warming up?

Start as close to useful tension as the story allows.

### Leave early

After the scene's turn, ask:

- Has the decision/revelation/refusal already landed?
- Are the next paragraphs only explaining what the reader understood?
- Would a cut preserve more energy?

### Exceptions

Start earlier or linger longer when duration itself creates:
- dread;
- ritual;
- tenderness;
- awkwardness;
- exhaustion;
- comedy;
- realism;
- atmosphere;
- grief.

The problem is not slowness.

The problem is **unintentional dead time**.

### Ten-line cut test

In revision:
1. temporarily remove the first 5–10 lines;
2. see whether orientation survives;
3. temporarily remove the last 5–10 lines;
4. see whether the scene becomes more resonant.

Restore anything whose absence damages intended effect.

---

## Stakes and Tension

*Basis: [@wd-character-wants], [@reedsy-conflict], [@nybe-stakes]*

Stakes do not have to mean:
- death;
- apocalypse;
- prison;
- world destruction.

The useful question is:

> What becomes painful, impossible, humiliating, irreversible, or costly for THIS character?

Use:

```text
DESIRE
+ UNCERTAINTY
+ CONSEQUENCE
+ CONSTRAINT
=
TENSION
```

### Scene stakes questions

- What does the character stand to lose now?
- What might they gain?
- What will action cost even if it works?
- What unintended consequence can follow?
- Does the reader know more or less about the danger than the character?
- Can the character simply walk away? If yes, why don't they?
- What commitment has made retreat harder?

Quiet scenes can carry high tension through:
- embarrassment;
- social exposure;
- withheld apology;
- attraction;
- moral compromise;
- waiting.

---

## Pacing: Scene vs Summary

Pacing is not simply "fast" or "slow."

Control it through:

- dramatized time;
- summary compression;
- sentence length;
- paragraph size;
- dialogue density;
- information rate;
- question/reveal timing;
- action frequency;
- interiority;
- transition length.

### Slow down for:
- irreversible choices;
- revelation;
- intimacy;
- dread;
- sensory disorientation;
- first experiences.

### Speed up for:
- routine;
- travel;
- repeated attempts;
- unimportant aftermath;
- background chronology.

Do not dramatize every commute.
Do not summarize the scene the story has been waiting for.

---

## Scene quick card

A scene is not defined merely by being continuous in time and place.

A strong scene usually creates a **state transition**.

```text
before scene ≠ after scene
```

The change may involve:
- knowledge;
- relationship;
- power;
- risk;
- desire;
- commitment;
- interpretation;
- opportunity.

### Required internal questions

```yaml
scene:
  pov:
  want:
  why_now:
  plan:
  resistance:
  hidden_pressure:
  stakes:
  reader_question:
  hidden_sentence:
  entry_pressure:
  concrete_anchor:
  change:
  exit_turn:
  next_pressure:
```

### Entrance test

Delete arrival/preamble temporarily.

If the reader still understands:
- where they are;
- who is present;
- what matters;

start later.

### Exit test

Delete explanatory aftermath temporarily.

If the emotional/plot turn becomes stronger, leave earlier.

### Scene exception classes

A scene may intentionally prioritize:
- atmosphere;
- observation;
- ritual;
- comic delay;
- waiting;
- grief;
- tenderness;
- discomfort.

Such scenes still need a reason for their duration.

### Filler test

Ask:
> If this scene disappeared, what specific story state would be missing?

If the answer is "none," compress or cut unless the texture itself is intentionally part of the work.
