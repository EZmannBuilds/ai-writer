# Suspense, Curiosity, and Surprise

Three different tension mechanisms. Use the right one; chain them deliberately.

| Contract | |
|---|---|
| Invoked by | Router when a story carries a question, a threat, or a twist; the Mystery, Horror, and Tragic packs build on it. |
| When | Planning an arc or sequence; before accepting any twist. |
| Needs | `reader_state`; `information` items from [information-architecture](information-architecture.md); character knowledge. |
| Produces | `suspense_thread`, `curiosity_thread`, `surprise_profile` records; twist red-team verdicts. |
| State | `open_loops` — `.ai-writer/open-loops.yaml`. |
| Consumed by | [information-architecture](information-architecture.md), [outlining](outlining.md), [mystery](../packs/mystery.md). |
| Skip when | Quiet literary pieces where the user wants no plot tension — don't invent a twist. |
| Tests | F16, F21 |
| Research | [research/core/reader-psychology.md](../research/core/reader-psychology.md) |

---

## Curiosity vs Suspense vs Surprise

Use the correct narrative tension mechanism.

```text
CURIOSITY
Reader recognizes missing information.
Primary question: "What happened / why is this true?"

SUSPENSE
Reader anticipates a consequential future outcome under uncertainty.
Primary question: "What will happen?"

SURPRISE
Reader encounters an outcome/revelation that violates expectation but becomes coherent
in retrospect.
Primary reaction: "I did not expect that, but now it makes sense."
```

These mechanisms can be chained:

```text
curiosity → suspense → surprise → recontextualized curiosity
```

Example:

```text
Curiosity: Why is the train arriving empty every night?
Suspense: Will Maya board it before the station closes?
Surprise: The train is returning objects from a future disaster, not passengers.
New curiosity: Why is Maya's own coat inside?
```

---

## Suspense Engine

Suspense requires:

1. a target outcome the reader hopes for or fears;
2. emotional investment;
3. uncertainty;
4. a perceived solution space;
5. progressive reduction in the number or quality of successful paths.

Represent a suspense thread as:

```yaml
suspense_thread:
  desired_outcome:
  feared_outcome:
  protagonist_goal:
  reader_stakes:
  feasible_paths: []
  blocked_paths: []
  deadline_or_pressure:
  reader_knowledge:
  character_knowledge:
```

---

## Adversarial Suspense Planning

For a suspense-bearing sequence:

#### Step 1: Protagonist option search

Generate the most rational available actions.

#### Step 2: Failure pressure

For each action, generate a credible condition that reduces or blocks its success.

#### Step 3: Update option space

The next action must account for previous failures.

#### Step 4: Decrease apparent success probability

Later actions may become:
- riskier;
- more costly;
- less certain;
- morally difficult;
- dependent on unreliable allies.

#### Step 5: Resolution

Do not repeat failures forever.
Allow:
- success;
- partial success;
- costly success;
- failure;
- reframing of the goal.

The final result should follow the project's intended ending logic.

---

## Knowledge Disparity

Track three knowledge sets:

```yaml
knowledge:
  reader_knows:
  protagonist_knows:
  other_character_knows:
```

Suspense can emerge when the reader knows a danger the protagonist does not.

Surprise can emerge when a character or narrator knows something the reader does not.

Mystery can emerge when neither knows enough.

Use these asymmetries deliberately.

---

## Curiosity Engine

Curiosity differs from suspense and surprise.

Curiosity is strongest when the reader recognizes a meaningful information gap.

Represent a curiosity thread as:

```yaml
curiosity_thread:
  question:
  why_reader_cares:
  known_information: []
  missing_information:
  competing_hypotheses: []
  perceived_solvability:
  gap_width:
  clue_schedule: []
  partial_answers: []
  payoff:
```

The reader must know that something is missing.

Examples:

```text
Why does the locked room smell like seawater?
Why has Marcus never entered his own basement?
Who keeps moving the family photographs?
Why does everyone remember the accident differently?
```

---

## Information-Gap Calibration

Curiosity can fail in two opposite directions.

### Gap too small

The answer is obvious.

Result:
- low curiosity;
- reader predicts payoff early.

### Gap too large

The reader lacks enough structure to form hypotheses.

Result:
- confusion;
- indifference;
- random-feeling mystery.

Aim for a gap where the reader can:

- notice the missing information;
- understand why it matters;
- generate more than one plausible explanation;
- believe an answer is obtainable.

Novelty, ambiguity, incongruity, complexity, and uncertainty may trigger curiosity, but
comprehensibility must remain high enough for the reader to engage.

---

## Curiosity Update Loop

For active curiosity threads:

```text
open question
→ clue
→ hypothesis formation
→ complication
→ partial answer
→ larger or transformed question
→ payoff
```

Do not preserve curiosity by simply withholding everything.

Progress is necessary.

A useful clue should alter at least one hypothesis.

---

## Narrative Surprise Engine

Evaluate significant twists and endings with six dimensions:

```yaml
surprise_profile:
  initiatoriness:
  immutability_violation:
  predictability:
  post_dictability:
  importance:
  valence:
```

Definitions:

### Initiatoriness

Does the reveal provide a causal antecedent that explains a previously unexplained event?

### Immutability Violation

Does the twist contradict a fundamental rule or assumed invariant of the story world?

Use cautiously. A twist can be surprising without breaking an invariant.

### Predictability

How easily could a typical attentive reader foresee the ending?

For many surprise-bearing stories, avoid both extremes:

```text
completely obvious
and
impossible to infer because required information never existed
```

### Post-Dictability

After the reveal, can the reader reconstruct why prior events occurred?

High post-dictability means the ending makes earlier material more coherent.

### Importance

Does the reveal materially affect the protagonist, conflict, relationships, or story meaning?

### Valence

Is the outcome positive or negative for the protagonist?

Do not use negative valence mechanically.
It is a descriptive dimension, not a mandate for bleakness.

---

## Surprise Construction Procedure

For an intended twist:

```text
1. Identify the surprising event/revelation.
2. Identify the hidden initiating cause.
3. Seed evidence produced by that cause.
4. Hide or misinterpret the cause itself.
5. Maintain at least two plausible reader models.
6. Avoid making the intended resolution the dominant obvious answer.
7. Reveal the initiating cause.
8. Re-check every relevant prior event.
9. Remove contradictions created only to protect the twist.
10. Preserve consequences after the reveal.
```

Prefer:

```text
unexpected + retrospectively coherent
```

over:

```text
unexpected because the writer invented new information at the end.
```

---

## Surprise Red-Team

Before accepting a twist, attack it.

Ask:

```text
Could a reader predict this immediately?
Does the reveal depend on facts introduced only during the reveal?
Does it contradict an established world rule?
Does it require a character to behave irrationally only to hide information?
Would a second reading reveal fair evidence?
Does the reveal explain earlier oddities?
Does it create a more interesting story after the reveal?
Is the twist just a familiar trope with different nouns?
```

Reject fake surprise.

---

## Surprise Research Caution

Research on mystery endings found reader preference for surprise was associated with:

- stronger initiatory causal explanation;
- stronger post-dictability;
- lower predictability;
- more negative valence.

Do not convert this into:

```text
good twist = negative ending
```

The evaluated sample was restricted to mystery endings, and surprise is audience-dependent.

Use these as diagnostics, not universal optimization targets.
