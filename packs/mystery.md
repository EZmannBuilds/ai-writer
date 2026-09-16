---
pack:
  id: mystery
  name: Mystery / Investigation
  version: "1.0"
  stage: genre
  pipeline_position: After Draft Starter and Origin Forge, before Intent Lock. Its ledgers stay active through drafting.
  purpose: Build solvable, surprising mysteries from a fixed truth, a fair clue trail, and tracked knowledge for investigator, suspects, and reader.
  triggers: ["Start Mystery"]
  natural_language_triggers: ["whodunit", "murder mystery", "plan the clues", "who did it", "detective story", "build the investigation", "locked-room"]
  requires: ["core/information-architecture", "core/suspense-curiosity-surprise"]
  optional_dependencies: ["draft-starter", "core/continuity", "core/character-model"]
  conflicts_with: []
  stacks_with: ["draft-starter", "origin-forge", "tragic-anime-engine", "horror", "romance", "series-engine", "worldbuilding", "comic-panel-writer"]
  inputs: ["draft_brief", "character canon", "world rules"]
  produces: ["mystery_brief", "truth_model", "clue_ledger", "suspect_state", "hypothesis_log", "reveal_plan"]
  skip_when:
    - A crime or investigator appears but the story's engine is not an unanswered "what happened / who did it" question.
    - The user wants a thriller or procedural where the answer is known and the tension is pursuit (use the suspense core instead, or the inverted form below only if asked).
  state_keys: ["pack_state.mystery", "open_loops", "characters.<id>.mental_state", "timeline"]
  research_basis: research/packs/mystery.md
  behavior_tests: ["F16", "F32"]
---

# Mystery / Investigation

## Purpose

A mystery is a promise: *there is an answer, and you could have found it.* The pack keeps that promise by building the truth first, then deciding exactly which parts of it the reader and investigator can see, when, and in what disguise.

It does not replace the core. A clue is an [information item](../core/information-architecture.md#information-items) with extra fields; the case question is a [curiosity thread](../core/suspense-curiosity-surprise.md#curiosity-engine); the reveal must pass the [surprise red-team](../core/suspense-curiosity-surprise.md#surprise-red-team). This pack adds the ledgers and tests those general mechanisms don't have.

## Activation

- **Explicit:** "Start Mystery".
- **Natural language:** a request whose engine is an unanswered question about what happened or who did it — "whodunit", "plan the clues", "locked-room murder", "the detective figures out...".
- **Not activation:** a story that merely contains police, a crime, or a detective. A cop drama about a partnership is not a mystery unless the story turns on solving something.

## Skip conditions

- The story's tension is pursuit or survival, not solution.
- The user wants the answer revealed up front and no investigation (unless they ask for an inverted mystery; see below).
- A FAST_SCENE request that doesn't touch clues, suspects, or the solution — read the ledgers if they exist, but don't run the procedure.

## Pipeline position

```text
Draft Starter → (Origin Forge) → Mystery → Intent Lock → Story Genome
→ outline with clue and reveal placement → drafting with ledger checks
```

## Inputs

- Draft Brief, if any.
- Existing character and world canon.
- `intent_lock`: fair-play strictness, subgenre, audience.

## Outputs

- `mystery_brief`, `truth_model`, `clue_ledger`, `suspect_state` records, `hypothesis_log`, `reveal_plan`.
- `open_loops` entries for the case question and each unresolved clue.

## State

- **Uses:** `characters.*.mental_state` (who knows what), `timeline`, `world` rules, `canon`.
- **Produces:** everything under `pack_state.mystery`. Each clue and the case question are mirrored into `open_loops` with `pack: mystery`.
- **Writes to core:** suspects' secrets and lies go into their `mental_state` / `developing_state` so the [Perspective Filter](../core/character-model.md#perspective-filter) keeps them honest.
- **Provenance:** a culprit the agent picked is a `delegated_decision` (if delegated) or `agent_proposal`. Never write it as confirmed.

## Procedure

```text
1. Read canon and briefs. Don't re-ask known facts.
2. Choose the form (below). Default: classic.
3. Build the TRUTH MODEL: what actually happened, minute by minute.
4. Derive EVIDENCE: every trace the truth would leave.
5. Build SUSPECTS: motive, means, opportunity, secrets, lies.
6. Select CLUES from the evidence; give each a first-read and true meaning.
7. Design the FALSE SOLUTION(S) and the red herrings that support them.
8. Place clues and plan the HYPOTHESIS path for investigator and reader.
9. Plan the REVEAL and the FINAL RECONSTRUCTION; run the fairness tests.
10. Plan the POST-REVEAL CONSEQUENCE.
11. During drafting, check each chapter against the ledgers.
```

Ask at most 3–5 questions, and only if the answer changes the solution: form, fair-play strictness, whether the user wants to choose the culprit, content limits.

### Forms

| Form | The question | Reader knows | Source |
|---|---|---|---|
| **Classic (whodunit)** | Who did it, and how? | Less than the solution requires, until the reveal | [@knox-1929], [@van-dine-1928] |
| **Inverted (howcatchem)** | How will the investigator find out? | The culprit and method from the start | [@freeman-1912] |
| **Whydunit** | Why did they do it? | Who, often early | design |
| **Open / ambiguous** | Can it be known? | Deliberately incomplete | design; requires user intent |

In the inverted form, tension moves to the investigator's method and the culprit's small mistakes. The knowledge ledger flips: the reader is ahead of the investigator, and the pleasure is watching the gap close.

### 1. Truth model

Write the truth before any clue. A mystery built clue-first tends to produce a solution that fits the clues but not the world.

```yaml
truth_model:
  crime:                      # or central event
  culprit:                    # may be multiple, or none
  method:
  motive:
  timeline: []                # minute-level where it matters
  what_went_wrong_for_culprit: []   # the mistakes that make detection possible
  cover_up: []                # what the culprit did afterward
  world_rules_relied_on: []   # must already be established in the story
  prov: agent_proposal
```

**The solution may use only rules the story has already established.** In a speculative setting, magic or technology that solves the case must be on the page before the reveal. This is the modern, general form of the old "no supernatural solution / no unknown poison" rules [@knox-1929].

### 2. Suspects

```yaml
suspect_state:
  id:
  relationship_to_victim:
  known_facts: []             # what they know about the crime
  hidden_facts: []            # what they know and conceal
  lies: []                    # {lie, to_whom, why, when_exposed}
  motive:
  means:
  opportunity:
  alibi: {claim:, truth:, verifiable_by:}
  unrelated_secret:           # the real reason an innocent suspect acts guilty
  suspicion_arc: []           # when suspicion rises and falls
  prov:
```

**Red herrings come from real secrets.** An innocent suspect who lies does so for a reason of their own — an affair, a debt, an embarrassment — not because the plot needs a suspect [@calvin-2021]. Record the secret, and decide whether it's revealed on the page or stays in backstory.

When presenting suspects, give each one a full `suspect_state` record in the schema's shape — every field present, written as `none` or `unknown` when empty — so gaps are visible rather than hidden in prose.

Every suspect's knowledge must be consistent with the truth model. Run the [Perspective Filter](../core/character-model.md#perspective-filter) before any suspect speaks.

### 3. Clue ledger

```yaml
clue:
  id:
  truth:                      # the fact in the truth model this clue comes from
  source:                     # object, testimony, absence, behavior, record...
  placed_at:                  # chapter/scene
  observed_by: []             # which characters perceive it
  reader_sees:                # exactly what reaches the page
  prominence:                 # buried | noticed | emphasized
  camouflage:                 # how its meaning is hidden (never by omission)
  apparent_meaning:           # what an attentive first reader will think
  true_meaning:               # what it means once the truth is known
  hypothesis_changes: []      # which hypotheses it strengthens or weakens
  supports_false_solution:    # true | false
  payoff:                     # where the true meaning is used
  status: planned             # planned | placed | paid | intentionally_unpaid
```

**Accessibility and interpretation are different.** A fair clue is *on the page* before the reveal. Its meaning may be disguised by misdirection, emphasis, or ordinary context — never by withholding the clue itself [@knox-1929], [@tobin-2018].

**Two meanings.** A strong clue reads naturally on first pass and means something else afterward [@tobin-conversation-2018]. If `apparent_meaning` and `true_meaning` are identical, the clue is a signpost, not a clue — fine occasionally, fatal as a pattern.

**The author's knowledge distorts.** Because the writer knows the answer, clues look more obvious to them than they are. Test fairness with the reader model below, not by feel.

### 4. Hypotheses

Track what the investigator and the reader each probably believe, chapter by chapter.

```yaml
hypothesis_log:
  - at:                       # chapter/scene
    investigator:
      leading: 
      alternatives: []
      knows_but_reader_doesnt: []   # must be empty in strict fair play
    reader_model:
      misled_reader: []       # what a reader following the misdirection believes
      ideal_reader: []        # what a reader weighing every clue could infer
    suspect_list_size:        # narrow gradually
```

- **Narrow the field over time.** Curiosity grows as the gap gets smaller and the answer feels closer [@loewenstein-1994]. Shrink the plausible suspect list in steps.
- **Hide the investigator's knowledge honestly.** In strict fair play the investigator never acts on a fact the reader hasn't seen. If the investigator keeps an inference private, the *evidence* for it must still be on the page.
- **Choose the effect per section.** Suspense (outcome delayed), curiosity (outcome shown before causes), and surprise (unexpected event) come from event ordering; tag sections by which one they are working [@brewer-lichtenstein-1982].

### 5. False solution

At least one coherent wrong answer that the clues genuinely support. It should:

- explain most of the evidence;
- fail on one or two clues that the true solution explains;
- come from a character's real behavior or the investigator's reasonable error;
- collapse *because of a clue*, not because of a new fact introduced to break it.

### 6. Reveal and reconstruction

```yaml
reveal_plan:
  reveal_point:
  trigger:                    # the clue, test, or event that breaks it open
  key_insight:                # the single realization that reorganizes everything
  reconstruction:             # the explanation, in order
  clues_accounted_for: []     # every placed clue, with its true meaning
  herrings_accounted_for: []  # resolved on page, or left in backstory (say which)
  false_solution_refuted_by: []
  consequence:                # what changes for people after the answer
```

**Fairness tests** — run all before accepting the solution:

1. **Coverage.** Every fact the reconstruction depends on appears as a placed clue *before* the reveal.
2. **Misled reader.** Following the misdirection, the solution seems unlikely before the reveal.
3. **Ideal reader.** Weighing every clue, the solution becomes highly probable in hindsight [@wagner-fairplay-2025]. This is the [post-dictability](../core/suspense-curiosity-surprise.md#narrative-surprise-engine) test applied to the whole case.
4. **Easy afterward.** The reconstruction makes the reveal easy to explain; surprise comes from it being hard to explain *beforehand* [@foster-keane-2013].
5. **Culprit presence.** The culprit appears early and meaningfully.
6. **No rule invented at the reveal.**
7. **No coincidence or unexplained intuition solves it.** The investigator reasons to the answer [@detection-club-oath].
8. **Red-team.** Run the core [surprise red-team](../core/suspense-curiosity-surprise.md#surprise-red-team).

**One insight, not a pile.** A solution that turns on one realization lands harder than a slow accumulation of facts [@loewenstein-1994]. Build the reconstruction around a `key_insight`.

**Don't rest everything on the secret.** Readers who guess right should still be rewarded — by the investigation, the people, and what the truth costs. The evidence on whether knowing the ending spoils enjoyment is contested [@leavitt-christenfeld-2011], [@levine-raines-2025]; don't design as if the answer's secrecy were the only value.

### 7. After the reveal

Answers alone tend to disappoint [@loewenstein-1994]. The reveal must change something: a relationship, a reputation, the investigator's belief about themselves, a community's story about itself. Plan it with the core [ending questions](../core/endings.md#endings-consequence-without-over-explanation).

## Guardrails

- The solution uses only established rules.
- Every load-bearing fact is on the page before the reveal (unless the user chose an open form).
- The investigator's reasoning is on the page, not implied by genius.
- Suspects know only what the truth model allows.
- Historical rules are **conventions**, not laws. Knox's and Van Dine's lists include prejudiced rules (an ethnic-stereotype rule; a class-bound servant rule) that the pack does not apply [@knox-1929], [@van-dine-1928].
- A culprit chosen by the agent is labeled as a proposal or delegated decision.

## Failure modes

| Failure | Looks like | Fix |
|---|---|---|
| Rabbit from the hat | Reveal depends on a fact introduced at the reveal | Place the fact earlier as a clue with a disguised meaning |
| Signpost clues | Every clue means exactly what it seems | Give clues a first-read meaning that points elsewhere |
| Late culprit | The culprit enters in the last act | Introduce them early, doing something meaningful |
| Suspicious for no reason | Innocent suspects lie without motive | Give each an unrelated secret |
| Genius detective | Investigator knows things the reader never saw | Put the evidence on the page |
| Empty answer | Reveal names the culprit and stops | Plan consequence and a key insight |
| Clue flood | Too many clues, no narrowing | Cut to load-bearing clues; shrink the suspect list in steps |
| Rules broken at the end | Magic/tech appears to solve it | Establish the rule earlier, in an unrelated use |

## Schemas

```yaml
mystery_brief:
  version: "1.0"
  form: classic               # classic | inverted | whydunit | open
  fair_play: strict           # strict | loose | off
  case_question:
  investigator:
  victim:
  setting_constraints: []
  culprit_choice: agent       # user | agent | delegated
  truth_model_ref:
  clue_count_target:
  false_solutions: []
  reveal_point:
  consequence:
  provenance: {confirmed_facts: [], delegated_decisions: [], agent_proposals: [], unresolved_questions: []}
```

The `truth_model`, `suspect_state`, `clue`, `hypothesis_log`, and `reveal_plan` schemas appear in the procedure above.

## Examples

**Seed:** a lighthouse keeper is found dead inside the locked lamp room. *(Generic demo.)*

- **Truth:** the assistant keeper, Wren, killed him during the evening watch and left by the external gallery, re-entering through the service hatch before the storm peaked. The door was bolted from inside because the victim bolted it himself when he heard someone on the gallery.
- **Key insight:** the bolted door doesn't prove no one entered. It proves the victim was afraid of someone *outside*.
- **Clue, first-read vs true:** the lamp's clockwork was wound early. *Apparent:* the keeper was diligent. *True:* he wound it early because he planned to stay inside, locked in.
- **Clue:** salt crust on the inside of the service hatch hinge. *Apparent:* storm damage. *True:* the hatch was opened during the storm.
- **Herring from a secret:** the supply-boat captain lies about when he left — he was smuggling, not murdering.
- **False solution:** the captain, supported by his lie and his debt to the victim; refuted by the salt on the hatch, which only fits someone already on the island.
- **Consequence:** Wren's motive (the victim's plan to automate the light and end both their posts) forces the investigator to decide whether to report what the keeper was hiding about the automation contract.

## Behavior tests

| Fixture | Checks |
|---|---|
| [F16](../tests/fixtures/F16-mystery-reveal-has-prior-clues.yaml) | Every load-bearing fact is a prior clue; clues have two meanings; a false solution exists; the culprit appears early. |
| [F32](../tests/fixtures/F32-mystery-red-herrings-from-secrets.yaml) | Suspect records are complete; innocent suspects' suspicious behavior comes from real secrets; knowledge matches the truth model. |
| [F19](../tests/fixtures/F19-fast-scene-minimal-machinery.yaml) | A scene request in a mystery project doesn't drag the pack in when the scene doesn't touch the case. |

## Research provenance

[research/packs/mystery.md](../research/packs/mystery.md). In short: curiosity and gap narrowing are grounded in information-gap theory; fair play as surprise-before plus coherence-after has recent computational support (a preprint); the two-meaning clue and misdirection rest on cognitive-literary analysis; the historical rules are conventions. The spoiler evidence is contested and is not used as a design rule.

## Integration

- **Core:** clues are information items; the case question is a curiosity thread; the reveal uses the surprise engine; continuity reads the clue ledger so planted misdirection is not flagged as an error ([canon resolver](../runtime/canon-resolver.md#before-calling-something-a-contradiction)).
- **Horror:** the mystery's truth model can be the horror's threat model; keep the horror pack's rule uncertainty and the mystery's fairness in tension deliberately — decide in Intent Lock which wins.
- **Tragic engine:** the reveal ledger and the clue ledger can share items; the reveal should cause action, not just answer.
- **Romance:** a suspect or investigator relationship runs on the romance pack's perception model; a lie between lovers is both a clue and a relationship event.
- **Series:** a long-horizon mystery lives in the series pack's mystery ledger, with each installment answering a smaller question.
- **Comic Panel Writer:** protect clue visibility and reveal placement with page turns; a clue must be *drawn*, not only captioned.
