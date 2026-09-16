---
pack:
  id: romance
  name: Romance / Attachment
  version: "1.0"
  stage: genre
  pipeline_position: After Draft Starter and Origin Forge, before Intent Lock. Its relationship model stays active through drafting.
  purpose: Model love stories as separate, moving dimensions — attraction, intimacy, trust, commitment, fear — held differently by each partner, with endings that fit the story rather than a default.
  triggers: ["Start Romance"]
  natural_language_triggers: ["love story", "slow burn", "they end up together", "enemies to lovers", "friends to lovers", "the breakup", "will they or won't they", "romantic subplot"]
  requires: ["core/relationships", "core/dialogue"]
  optional_dependencies: ["draft-starter", "core/character-model"]
  conflicts_with: []
  stacks_with: ["draft-starter", "origin-forge", "tragic-anime-engine", "mystery", "horror", "series-engine", "worldbuilding", "comic-panel-writer"]
  inputs: ["draft_brief", "character canon", "relationship records", "genre contract from intent_lock"]
  produces: ["romance_brief", "relationship_perception", "love_dimensions", "disclosure_ladder", "barrier_ledger", "conflict_beats"]
  skip_when:
    - Two characters share a scene but the relationship isn't romantic or its romantic dimension isn't in play.
    - The user wants intimacy or friendship explicitly without romance (the core relationship model is enough).
  state_keys: ["relationships.<a>--<b>", "pack_state.romance", "characters.<id>.mental_state", "open_loops"]
  research_basis: research/packs/romance.md
  behavior_tests: ["F24", "F25", "F33"]
---

# Romance / Attachment

## Purpose

"Chemistry" is not one number. Attraction, closeness, and commitment move independently [@sternberg-1986], [@sorokowski-2021]; people can be committed and unhappy, or happy and uncommitted [@rusbult-1983]; and two partners can hold different pictures of the same relationship [@murray-1996]. This pack gives each relationship those separate dials, tracks them from **each partner's side**, and builds the story from the gaps.

It extends [relationship state](../core/relationships.md#relationship-state) — it doesn't replace it — and leans on [dialogue and subtext](../core/dialogue.md) for how love is spoken and not spoken.

**Relationship science describes real people.** Here it is a lens for believable characters, not a diagnosis. No character is "an anxious attacher." Characters have tendencies under pressure.

## Activation

- **Explicit:** "Start Romance".
- **Natural language:** the story is about two (or more) people falling in, staying in, or leaving love — "slow burn", "enemies to lovers", "the breakup", "will they or won't they".
- **Subplot:** a romantic storyline inside another genre activates the pack for that storyline only; the genre contract comes from the main story.
- **Not activation:** friendship, family, or rivalry with no romantic dimension in play.

## Skip conditions

- The relationship's romantic side isn't touched by the scene.
- The user wants intimacy without romance; use core relationships.

## Pipeline position

```text
Draft Starter → (Origin Forge) → Romance → Intent Lock (genre contract) → Story Genome
→ outline with relationship beats → drafting with perception checks
```

## Inputs

- Draft Brief; character canon; existing relationship records.
- `intent_lock.genre`: decides the **ending contract** (below).
- Content rating and consent boundaries.

## Outputs

`romance_brief`, per-pair `relationship_perception` and `love_dimensions`, `disclosure_ladder`, `barrier_ledger`, `conflict_beats`.

## State

- **Uses and writes** `relationships.<a>--<b>` — the pack adds `perception` and `love` blocks to the core record. It never keeps a separate copy.
- **Writes** each partner's beliefs about the other into their `mental_state` (`beliefs_about_others`, `beliefs_about_others_beliefs`).
- **Stores** the brief, ladders, and ledgers under `pack_state.romance`.
- **Mirrors** "will they / won't they" and unresolved declarations into `open_loops`.

## Procedure

```text
1. Read canon, relationship records, and the genre contract.
2. Set the ENDING CONTRACT.
3. For each romantic pair: PERCEPTION record and LOVE DIMENSIONS.
4. For each partner: THREAT RESPONSE and what restores safety.
5. BARRIERS: external and internal, and how each falls or holds.
6. DISCLOSURE LADDER: how closeness is built (or fails).
7. CONFLICT BEATS for the fights that matter.
8. Map the story beats (below); order and repeat as needed.
9. Draft; after consequential scenes, update perception and dimensions.
```

### Ending contract

| Contract | When | Requirement |
|---|---|---|
| **Romance (genre)** | `intent_lock.genre` is romance | A central love story and an emotionally satisfying, optimistic ending [@rwa-genre-definition]. Community shorthand: HEA or HFN. |
| **Romantic storyline** | Romance inside another genre | The storyline serves the main story. It may succeed, fail, or stay open. |
| **Literary / tragic** | The user wants the truth of the relationship over a genre promise | The ending follows from who these people are. Parting, loss, or ambiguity are valid. |

**Don't force marriage or reconciliation.** Even inside the genre, commitment can take the characters' own form — an anti-proposal, an unconventional arrangement, "happy for now" — and still satisfy [@kies-2024]. Outside the genre, a relationship that correctly doesn't work out is a success, not a violation.

Set the contract in Intent Lock. When another pack pulls against it (Tragic's permanent cost), the user's stated intent decides.

### Perception

```yaml
relationship_perception:
  character_a_thinks:
    status:                   # e.g., dating, exclusive, friends who kiss, over, nothing
    my_attraction:
    their_attraction:         # what A believes about B
    their_commitment:
    what_we_agreed:
    what_i_want_next:
  character_b_thinks: {}      # same shape
  actual_shared_agreement:    # what both have actually said; often less than either believes
  gap:                        # the mismatch, in one line
  gap_known_to: []            # who has noticed the mismatch
```

Two characters can disagree about what relationship they're in. The gap between their pictures is an engine, and each picture shapes what happens next [@murray-1996]. Never collapse the two into one status.

### Love dimensions

Track these **per partner, toward the other**, as rough planning labels or 0–100 estimates. They move independently.

```yaml
love_dimensions:
  a_toward_b:
    attraction:               # physical/romantic pull
    sexual_interest:          # only when relevant to the story and rating
    affection:
    intimacy:                 # felt closeness, being known
    trust:
    admiration:
    dependency:
    vulnerability:            # how exposed A lets themselves be
    fear:                     # of B, of loss, of being known
    resentment:
    commitment:
    status:                   # A's perceived standing relative to B
    boundaries: []
    expectations: []
  b_toward_a: {}
  pressure:
    external: []              # family, law, war, distance, class, secrets
    internal: []              # fear, shame, prior loss, incompatible goals
  incompatibility: []         # real differences that love doesn't erase
```

Flag informative combinations:

| Combination | Story state |
|---|---|
| High commitment, low satisfaction | Entrapment: history or lack of alternatives holds them [@rusbult-1983] |
| High attraction, low commitment | Temptation without a future |
| High intimacy, low attraction | Deep friendship; possibly intimacy without romance |
| High trust, low intimacy | Reliable but not known |
| Asymmetric attraction | Unrequited or uneven love |

**Commitment has causes.** It rises with satisfaction, with poorer alternatives, and with investment — time, disclosures, shared friends, shared memories [@rusbult-1983]. A rival raises alternatives; a shared history raises the cost of leaving. Use these to explain staying and leaving without melodrama.

### Threat response

Under relational threat, people tend to move in a direction: toward the partner (seeking, protesting, pursuing) or away (withdrawing, insisting on self-reliance) [@mikulincer-shaver-2003], [@hazan-shaver-1987].

```yaml
threat_response:
  character:
  tends_to:                   # pursue | withdraw | mixed
  triggers: []
  what_it_looks_like: []      # concrete behavior, not a label
  what_restores_safety: []
  care_capacity_under_threat: # frightened people give less care until safe again
```

Frightened characters are worse caregivers until they feel safe; once safe, play, desire, and generosity come back [@mikulincer-shaver-2003]. That gives you the shape of crisis and "safe harbor" scenes.

### Disclosure ladder

Closeness grows through steadily deeper, reciprocal disclosure [@aron-1997] — and **only when the disclosure is met with a response that feels understanding and caring** [@laurenceau-1998].

```yaml
disclosure_ladder:
  - rung:
    discloser:
    disclosure:
    risk:                     # low | medium | high
    response:                 # what the other does
    felt_as:                  # understood | dismissed | misheard | punished
    effect:                   # intimacy up | trust down | ...
    reciprocated:             # true/false
```

- A **slow burn** is a ladder: each rung riskier, each needing a response before the next.
- A confession that is misheard or dismissed **lowers** trust. That's a scene, not a stall.
- Pace escalation by vulnerability, not by how often they're in a room together.

### Barriers

```yaml
barrier_ledger:
  - barrier:
    kind:                     # external | internal
    highest_point:            # where it peaks
    falls_by:                 # choice, recognition, sacrifice, change in circumstance
    status:                   # active | falling | fallen | holds
```

Romance-genre structure commonly includes a defined society, a meeting, a barrier, attraction, a declaration, a point of ritual death (the "dark moment") at the barrier's height, a recognition, and a commitment [@regis-2003]. **These are beats, not a sequence.** They can be reordered, doubled, or combined. Link the dark moment to the barrier's peak and pair it with a recognition that makes the barrier fall — or, outside the genre, hold.

### Conflict beats

For fights that matter, track the few beats that show a relationship's health [@gottman-1998], [@gottman-levenson-1992]:

```yaml
conflict_beats:
  scene:
  start:                      # harsh | gentle
  surface_topic:
  real_topic:                 # see core/dialogue.md
  de_escalation_attempts: []  # {by, attempt, received_as}
  influence_accepted:         # who lets the other change their mind
  withdrawal_or_defensiveness: []
  after:                      # repair attempt, silence, escalation
```

These are signals, not a prophecy. **Don't assign them by gender** — the source studies used heterosexual couples, and their gendered findings don't transfer.

### Unrequited love

Write both sides [@baumeister-1993]:

- **The one who loves:** hope survives vague signals; they may believe the feeling was mutual or that they were led on.
- **The one who doesn't:** guilt, annoyance, and no script for saying no. Not a villain by default.
- Track `clarity_of_rejection`. Indirect refusals prolong hope.

### Consent and power

- Track power differences between partners: status, money, age, experience, authority, supernatural power.
- Where power is unequal, the more powerful character carries the work of checking in and reading signals; consent is shown as ongoing [@popova-2018].
- Dubious or non-consensual content is never a default. It appears only as an explicit, labeled choice within the content rating.

### Queer romance

Queer love stories are not pronoun swaps. Check for unexamined heterosexual defaults — marriage as the only ending, gendered roles in conflict, a single "acceptable" shape of commitment [@wood-allan-2016], [@kies-2024]. Let the characters' values define the ending.

### Supported shapes

Slow burn · established couple · breakup · reconciliation · unrequited · messy/triangle · queer romance · friends to lovers · rivals/enemies to lovers · intimacy without romance · polyamorous or non-exclusive arrangements · a relationship that correctly shouldn't work out.

For **enemies/rivals to lovers**, the antagonism must be real and its resolution earned by recognition, not erased by attraction. For **reconciliation**, the original incompatibility must be addressed, not forgotten.

## Guardrails

- Never collapse two partners' perceptions into one.
- Never force a romance toward marriage, reconciliation, or a happy ending outside the genre contract.
- Never let a love interest exist only to serve the protagonist; they have their own perception record and wants.
- Attachment research is a lens, never a diagnosis.
- Consent is modeled with power in view.
- The user's stated intent sets the ending.

## Failure modes

| Failure | Looks like | Fix |
|---|---|---|
| Chemistry slider | One "affection" value rising steadily | Track dimensions separately, per partner |
| Shared mind | Both partners always know where they stand | Add a perception gap and who has noticed it |
| Misunderstanding plot | A conflict one conversation would solve | Give the silence a cost or a reason (status, fear, shame) |
| Instant intimacy | Deep closeness with no disclosures | Build the ladder |
| Reset button | A breakup undone without addressing its cause | Name the incompatibility and what changed |
| Forced HEA | A literary romance bent toward reunion | Check the ending contract |
| Villain rejecter | The one who says no is cast as cruel | Write their side |

## Schemas

```yaml
romance_brief:
  version: "1.0"
  ending_contract:            # romance_genre | romantic_storyline | literary_or_tragic
  shape:                      # slow_burn | established | breakup | reconciliation | unrequited | ...
  pairs: []                   # relationship ids, e.g. ines--noor
  central_barrier:
  dark_moment:
  recognition:
  commitment_form:            # marriage | partnership | anti_proposal | open | none | parting
  heat_level:                 # within intent_lock.content_rating
  consent_notes: []
  provenance: {confirmed_facts: [], delegated_decisions: [], agent_proposals: [], unresolved_questions: []}
```

The `relationship_perception`, `love_dimensions`, `threat_response`, `disclosure_ladder`, `barrier_ledger`, and `conflict_beats` schemas appear above.

## Examples

**Perception gap.** *(Generic demo.)* Noor thinks she and Ines are dating. Ines thinks they're close friends who sometimes kiss.

```yaml
relationship_perception:
  character_a_thinks: {status: dating, their_commitment: rising, what_we_agreed: "we're together"}
  character_b_thinks: {status: close friends who kiss, their_commitment: casual, what_we_agreed: "nothing's official"}
  actual_shared_agreement: "They kiss. Neither has said a word about what it means."
  gap: Noor is building a future Ines doesn't know exists.
  gap_known_to: []
```

Scene plan: Noor mentions "our" trip in front of Ines's sister (surface topic: holiday dates). Ines deflects with a joke (tactic). The sister's glance makes the gap visible to the reader before either woman names it. The disclosure rung is Noor's: "I told my mother about you." Ines's response is felt as dismissive. Trust drops; the gap becomes known to both.

**A parting that's right.** Ana wants to stay in the town that raised her; Joel's work will always move. Both dimensions stay high to the end — attraction, intimacy, trust — while commitment can't take a shared form. The ending is a recognition, not a dark moment: they choose to part because they understand each other.

## Behavior tests

| Fixture | Checks |
|---|---|
| [F24](../tests/fixtures/F24-romance-perception-mismatch.yaml) | Separate perception records; the shared agreement differs from both; the scene turns on the gap. |
| [F25](../tests/fixtures/F25-romance-allowed-to-fail.yaml) | A literary parting is honored without being pushed toward reunion. |
| [F33](../tests/fixtures/F33-romance-continuation-loads-state.yaml) | A continuation reads relationship state first and keeps unresolved feeling unresolved. |
| [F14](../tests/fixtures/F14-relationship-updates.yaml) | Relationship records update after consequential scenes (core behavior the pack depends on). |

## Research provenance

[research/packs/romance.md](../research/packs/romance.md). In short: the dimensional model, commitment causes, disclosure-and-response intimacy, perception gaps, threat responses, conflict signals, and unrequited love come from relationship science (mostly WEIRD, often heterosexual samples; used as a conceptual lens). Story beats, genre contract, queer-romance and consent guidance come from genre scholarship and an industry definition.

## Integration

- **Core:** extends [relationships](../core/relationships.md); uses [dialogue](../core/dialogue.md) subtext for the hidden sentence; writes beliefs about partners into [character mental state](../core/character-model.md#theory-of-mind-character-model).
- **Tragic engine:** a love bond can be a Hope Reserve item; losing it is a tragedy form. The ending contract decides whether the romance survives.
- **Horror:** threat responses under terror — pursuit or withdrawal — shape scenes; frightened partners care less well until safe.
- **Mystery:** a lie between lovers is a clue and a relationship event; update both ledgers.
- **Series:** relationship trajectories span installments in the series pack's arc ledger.
- **Comic Panel Writer:** perception gaps read well in reaction panels and silence.
