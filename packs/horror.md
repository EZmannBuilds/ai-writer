---
pack:
  id: horror
  name: Horror / Dread
  version: "1.0"
  stage: genre
  pipeline_position: After Draft Starter and Origin Forge, before Intent Lock. Also runs inside FAST SCENE MODE for a horror scene.
  purpose: Build fear as a shaped curve — safety, anomaly, uncertainty, confirmation, escalation, consequence — around a threat that is both dangerous and wrong.
  triggers: ["Start Horror"]
  natural_language_triggers: ["make this scary", "horror story", "build dread", "haunted", "the monster", "creepier", "psychological horror", "cosmic horror", "body horror"]
  requires: ["core/reader-state", "core/scene-engine"]
  optional_dependencies: ["draft-starter", "core/suspense-curiosity-surprise", "core/information-architecture"]
  conflicts_with: []
  stacks_with: ["draft-starter", "origin-forge", "tragic-anime-engine", "mystery", "romance", "series-engine", "worldbuilding", "comic-panel-writer"]
  inputs: ["draft_brief", "scene request", "world rules", "content limits"]
  produces: ["horror_brief", "threat_model", "dread_curve", "rule_ledger", "horror_audit"]
  skip_when:
    - The request only wants a brief eerie description, not fear as the scene's engine.
    - The user wants a cozy or comic tone where fear is incidental.
  state_keys: ["pack_state.horror", "reader_state", "world", "open_loops"]
  research_basis: research/packs/horror.md
  behavior_tests: ["F23", "F31"]
---

# Horror / Dread

## Purpose

Horror is not maximum intensity. Enjoyment of fear peaks at a middle level and tracks the rise-and-release of tension, not the peak [@andersen-2020]. This pack shapes that curve: a world that feels safe, a wrongness that won't resolve, rules the characters can't quite learn, a threat that is dangerous *and* categorically off, and a cost that stays after the lights come back.

It works through the core. The dread curve is a specialization of the [affect curve](../core/reader-state.md#affect-curve); the unknown is a [curiosity thread](../core/suspense-curiosity-surprise.md#curiosity-engine); the threat's approach is a [suspense thread](../core/suspense-curiosity-surprise.md#suspense-engine).

## Activation

- **Explicit:** "Start Horror".
- **Natural language:** fear is the point — "make this scary", "build dread", "a haunting", "the thing in the house".
- **FAST SCENE:** a horror *scene* activates the pack with a light procedure: baseline, threat visibility, curve, audit.
- **Not activation:** a thriller with a killer where the question is pursuit, not dread; a fantasy with monsters that are simply enemies.

## Skip conditions

- A one-paragraph spooky description.
- Comic or cozy tones where the user wants fear light.
- The user says the story isn't horror, whatever its content.

## Pipeline position

```text
Draft Starter → (Origin Forge) → Horror → Intent Lock → Story Genome → outline with dread curve → drafting → horror audit
FAST SCENE: scene request → Horror (light) → scene contract → prose → horror audit
```

## Inputs

- Draft Brief or scene request.
- World rules and canon.
- `intent_lock`: audience, content rating, mode preferences, limits on gore.

## Outputs

`horror_brief`, `threat_model`, `dread_curve`, `rule_ledger`, `horror_audit`.

## State

- **Uses:** `reader_state`, `world`, character `mental_state` (who has seen what).
- **Produces:** `pack_state.horror.*`. Open questions about the threat mirror into `open_loops`. Rules the characters learn update their `mental_state`, not the world's actual rules.
- **Two rule sets.** The *actual* rules of the threat and the *believed* rules are separate records. Characters act on belief.

## Procedure

```text
1. Read canon and briefs.
2. Pick the mode(s) and the audience's plausibility frame.
3. Build the THREAT MODEL: what it is, what makes it wrong, what it wants, its actual rules.
4. Establish the SAFETY BASELINE the story will violate.
5. Plan VISIBILITY: what is seen, when, and how much.
6. Plan the DREAD CURVE across the scene/story, with recovery beats.
7. Plan RULE UNCERTAINTY: what the characters believe, and how that belief fails.
8. Plan PRESSURES: isolation, disbelief, contamination, taboo, helplessness vs counterplay.
9. Draft.
10. AFTERMATH: what stays.
11. Run the HORROR AUDIT.
```

### Modes

Modes combine; choose the dominant one.

| Mode | Fear source | Success test |
|---|---|---|
| **Supernatural** | Agents or forces outside natural law | The rules feel real and partly unknowable |
| **Psychological / uncanny** | The familiar made wrong; unreliable perception | The ordinary never quite recovers [@freud-1919] |
| **Cosmic** | Scale; the unknown; human insignificance | Atmosphere and the sense of contact with something vast [@lovecraft-1927] |
| **Body** | Violation of anatomy and biology: fusion, mutation, transformation | The body's integrity is the stake [@cruz-2012] |
| **Human** | People: cults, killers, institutions, neighbors | Plausibility; the horror of what people choose |

**Match the frame to the audience.** Readers who find the supernatural plausible prefer supernatural threats; others prefer natural ones [@clasen-2020]. If the audience is unknown, ask once or pick and state it.

### Threat model

```yaml
threat_model:
  what_it_is:                 # the truth; may never be fully revealed
  wrongness:                  # which category it violates
  wrongness_type:             # fusion | fission | formless | incomplete | near_human | impossible_behavior | human_choice
  danger:                     # what it can do to people
  wants:                      # or "nothing comprehensible"
  actual_rules: []            # what really governs it
  limits: []                  # what it cannot do (horror needs limits to have rules)
  tells: []                   # the signs of its presence
  counterplay: []             # what might work, at what cost
  reveal_ceiling:             # the most that will ever be explained
  prov:
```

**Dangerous and wrong.** A threat that is only dangerous is a thriller antagonist. Horror needs a threat that also violates a category — alive and dead, person and thing, one and many, familiar and not [@carroll-1990]. Name which one.

**Near-human is worse than inhuman.** Something almost human unsettles more than something clearly alien, and movement sharpens it [@mori-1970]. Show near-human wrongness through *behavior and motion*, not static description.

### Safety baseline

Before anything goes wrong, the reader must believe in a normal: routines, a home, a relationship, a rule of everyday life. The uncanny needs a familiar thing to corrupt [@freud-1919]. Record it:

```yaml
safety_baseline:
  normal:
  what_feels_safe:
  why_the_character_trusts_it:
  first_violation:
```

### Visibility

```text
absent → implied → glimpsed → partial → confirmed → fully shown
```

- **Terror before horror.** Anticipation and obscurity widen attention; confirmation contracts it [@radcliffe-1826]. Default to the slow side of the ladder; use full visibility sparingly and late.
- **Obscure, not confused.** Hints must be specific enough to feed imagination. Vagueness that the reader can't picture is not dread.
- **Revealing reduces the uncanny.** Once the rules are openly fantastical, the uncanny drains away [@freud-1919]. Keep the reader unsure which rules apply for as long as the story can bear it.

### Dread curve

The default shape:

```text
safe
→ anomaly
→ uncertainty
→ confirmation
→ temporary explanation
→ rule violation
→ escalation
→ helplessness or counterplay
→ consequence
```

```yaml
dread_curve:
  - beat:
    phase:                    # one of the phases above, or "recovery"
    intensity:                # 0-100 planning estimate
    uncertainty:              # what / when / whether / which-rules
    visibility:               # absent … fully shown
    recovery_after:           # true/false
    note:
```

Rules for the curve:

- **Recovery beats are required.** After a spike, drop. Enjoyment tracks moderate fear and the swing between tension and release, not constant peak [@andersen-2020].
- **Uncertainty is its own dial.** Unpredictable *timing* of threat drives anxiety even when nothing happens [@grupe-nitschke-2013]. Vary *when*, not only *how much*.
- **The temporary explanation matters.** A plausible mundane explanation lets the reader relax — so its failure lands.
- **Quiet is structural.** A still room, an ordinary conversation, a meal: these are where dread accumulates. Don't cut them for pace.
- **Shocks need a frame.** A sudden scare depends on the build before it and the release after. Distinguish the false alarm (build, no payoff) from the unwarned shock (no build); budget both [@acosta-sears-2025]. In prose, the jolt is a change in rhythm, syntax, or paragraph shape.

### Rule uncertainty

```yaml
rule_ledger:
  - rule:                     # e.g., "it can't cross salt"
    actual: true              # true | false | partial
    believed_by: []
    evidence_seen: []
    fails_at:                 # scene where the belief breaks, if it does
    cost_of_failure:
```

Characters try to learn when they're safe. Horror sharpens when that learning fails — a rule that held twice breaks the third time [@grupe-nitschke-2013]. A broken rule must be consistent with `actual_rules`; the characters were wrong, not the world.

### Pressures

Use the ones the story needs; don't stack all of them.

| Pressure | Craft note | Basis |
|---|---|---|
| **Isolation** | Remove help physically, socially, or informationally. Earn it: the reason for being alone should be believable. | craft inference |
| **Social disbelief** | No one believes the witness. Give the disbelievers good reasons. | craft inference |
| **Contamination** | The threat spreads: to objects, bodies, homes, family. | [@carroll-1990] (impurity) |
| **Taboo** | A line the culture holds; crossing it has meaning beyond danger. | design |
| **Helplessness vs counterplay** | Readers use horror partly to rehearse coping [@scrivner-2021]. Let characters try things — including failing. | [@scrivner-2021], [@clasen-2020] |

Isolation, disbelief, and aftermath guidance is **craft inference**. The research pass found no dedicated source for them; treat them as design choices, not findings.

### Aftermath

Fear can persist after the story ends, and relief at resolution is only one of horror's payoffs [@martin-2019]. Unresolved or partly resolved endings are legitimate. Plan what stays:

- a changed routine, a room no one uses, a habit of checking;
- a relationship altered by what someone saw or didn't believe;
- a belief about the world that can't be un-learned;
- the threat's status: gone, dormant, spread, or unknowable.

## Guardrails

- **No stupidity for plot.** Characters make choices that follow from their knowledge and pressures. If someone goes into the basement alone, give them a reason that would move a sensible person.
- **Gore has a job.** Graphic content serves the mode (body horror, consequence) and stays within `intent_lock.content_rating`.
- **Don't explain the monster early.** The reveal ceiling is set in the threat model; lore dumps come after, if ever.
- **Real-world harm.** Mental illness is not a monster. Real communities, religions, and places used for horror go through [research mode](../core/research-mode.md).
- **Don't horror-ify other genres.** The pack runs only when fear is the engine.

## Failure modes

| Failure | Looks like | Fix |
|---|---|---|
| Constant peak | Every paragraph maximum dread | Add recovery beats; vary uncertainty, not only intensity |
| Early lore dump | The monster's history explained in act one | Move explanation past the reveal ceiling or cut it |
| Threat without wrongness | A strong enemy, nothing uncanny | Name the category it violates |
| Stupid protagonist | Danger reached through implausible choices | Supply motive, pressure, or missing knowledge |
| Arbitrary rules | The threat does whatever the scene needs | Write `actual_rules`; break beliefs, not rules |
| No baseline | Wrong from the first line | Establish a trusted normal first |
| Clean ending by reflex | Everything resolved and safe | Plan aftermath; decide what stays |

## Horror audit

Run after drafting. **Flag defaults; don't ban them.** A stock device can work when it's transformed, specific, or earned.

```yaml
horror_audit:
  baseline_present:
  curve_has_recovery:
  uncertainty_varied:
  visibility_ladder_respected:
  threat_wrongness_named:
  rules_consistent:
  choices_motivated:
  aftermath_present:
  anti_defaults: []           # {device, where, why_it_reads_as_default, alternative}
```

**Anti-defaults** — flag these when they appear by reflex [@waggoner-2020]:

- **The creepy smile** as the go-to expression of wrongness.
- **Constant whispers** — especially repeated lines like "play with me."
- **Endless flickering lights** and failing electronics.
- **Unexplained gore** with no mode or consequence.
- **Characters behaving stupidly** to reach danger: splitting up, investigating the noise alone, tripping while fleeing.
- **The lore dump** explaining the monster too early.
- **Overused shells** without a fresh angle: the stock vampire, witch, ghost child, clown, zombie, "it was the narrator all along."

For each, offer a story-specific alternative or name the condition under which the device works (for example, lights that fail *in a pattern the character has learned to read*).

## Schemas

```yaml
horror_brief:
  version: "1.0"
  modes: []                   # supernatural | psychological | cosmic | body | human
  dominant_mode:
  audience_frame:             # supernatural_plausible | naturalistic | unknown
  content_rating:
  gore_policy:                # none | implied | on_page_with_purpose
  safety_baseline_ref:
  threat_model_ref:
  reveal_ceiling:
  ending_state:               # threat gone | dormant | spread | unknowable
  provenance: {confirmed_facts: [], delegated_decisions: [], agent_proposals: [], unresolved_questions: []}
```

The `threat_model`, `safety_baseline`, `dread_curve`, `rule_ledger`, and `horror_audit` schemas appear above.

## Examples

**Scene request:** Dana, alone in her late mother's farmhouse, realizes the house has started setting the table for two. *(Generic demo.)*

| Beat | Phase | Intensity | Note |
|---|---|---|---|
| Dana eats cereal standing up, leaves one bowl in the sink | safe | 10 | Baseline: grief routine, the house as her mother's |
| Morning: two bowls on the table, spoons laid the way her mother laid them | anomaly | 35 | Visibility: implied |
| She assumes she did it half-asleep; puts one away | temporary explanation | 20 | Recovery |
| She sets up a phone camera. Next morning, two bowls; the recording shows the kitchen empty, then two bowls, with no cut | confirmation | 60 | Uncertainty shifts from *whether* to *what* |
| She calls her brother. He's kind, and certain she's not sleeping | social disbelief | 30 | Recovery, with isolation added |
| Night. She sets one place deliberately. At 3 a.m., the scrape of a second chair | rule violation / escalation | 80 | Near-human behavior: the chair pulled out the exact distance her mother liked |
| She doesn't go down. She lies awake until the scraping stops | helplessness | 55 | A motivated choice; no basement run |
| Morning: two bowls. One has been eaten from | consequence | 70 | Ending state: unknowable; nothing explained |

Audit: baseline present; recovery after each spike; no lights, whispers, or smiles; no lore; Dana's choices motivated.

## Behavior tests

| Fixture | Checks |
|---|---|
| [F23](../tests/fixtures/F23-horror-dread-curve-has-quiet.yaml) | Baseline, anomaly, and escalation; a recovery beat; no lore dump; no reflexive clichés. |
| [F31](../tests/fixtures/F31-horror-anti-default-audit.yaml) | The audit flags stock devices and offers alternatives instead of bans. |

## Research provenance

[research/packs/horror.md](../research/packs/horror.md). In short: the dread curve rests on a field study of fear and enjoyment and on anxiety research about uncertainty (analogies from haunted attractions and clinical research to prose — approximate); terror/horror and the uncanny are historical and theoretical positions; the category-violation model is philosophical theory; isolation, disbelief, and aftermath rules are craft inference.

## Integration

- **Core:** the dread curve extends the [affect curve](../core/reader-state.md#affect-curve); the unknown is a curiosity thread; the approach is a suspense thread; the reveal ceiling uses [information architecture](../core/information-architecture.md#information-items).
- **Mystery:** the threat model can be the truth model. Decide in Intent Lock whether fairness (Mystery) or rule uncertainty (Horror) wins at the end.
- **Tragic engine:** body cost and irreversible transformation feed the power-cost and consequence ledgers.
- **Romance:** attachment under threat — frightened characters give less care until they feel safe (see the Romance pack's threat response).
- **Comic Panel Writer:** visibility maps to panel framing; page turns carry confirmations; silent panels carry recovery beats.
