---
pack:
  id: worldbuilding
  name: Society / Worldbuilding Engine
  version: "1.0"
  stage: world
  pipeline_position: Planning, before Intent Lock; also on demand during drafting when a scene needs a world system.
  purpose: Build worlds causally — conditions create incentives, incentives create institutions and norms, and those land on people as costs and conflicts the story can use.
  triggers: ["Build World"]
  natural_language_triggers: ["worldbuilding", "build the society", "how does the magic system work", "what's the economy like", "design the government", "invent the culture"]
  requires: ["core/world-state"]
  optional_dependencies: ["draft-starter", "core/research-mode", "core/relationships"]
  conflicts_with: []
  stacks_with: ["draft-starter", "origin-forge", "tragic-anime-engine", "mystery", "horror", "romance", "series-engine", "comic-panel-writer"]
  inputs: ["premise or world seed", "existing world canon", "story_genome (optional)"]
  produces: ["world_brief", "system_chains", "pressure_map", "world_hooks"]
  skip_when:
    - A contemporary realist setting with no invented systems (use research mode for real places).
    - The user asks for a single detail, not a system.
  state_keys: ["world", "pack_state.worldbuilding", "canon"]
  research_basis: research/packs/worldbuilding.md
  behavior_tests: ["F28"]
---

# Society / Worldbuilding Engine

## Purpose

A world is interesting when its parts cause each other. This pack builds only the systems the story will touch, as chains:

```text
CONDITION → INCENTIVE → INSTITUTION → SOCIAL NORM → PERSONAL CONSEQUENCE
```

— and then turns the last link into pressure, cost, and conflict the page can use. It is the systems-level partner of [world state](../core/world-state.md), whose rule still governs output: **worldbuilding reaches the page through use, conflict, expectation, cost, and consequence.**

It is not an encyclopedia generator and not a questionnaire.

## Activation

- **Explicit:** "Build World".
- **Natural language:** requests to design a society, a magic system's social effects, an economy, a government, a culture.
- **On demand:** during drafting, when a scene needs to know how a system works (who enforces the curfew; what a bribe costs).

## Skip conditions

- Real, contemporary settings: use [research mode](../core/research-mode.md).
- A single detail ("what's the capital called?"): answer it; don't run the engine.
- The story is intimate and the world is background: build only what the scenes touch.

## Pipeline position

```text
Draft Starter → (genre packs) → Worldbuilding → Intent Lock → Story Genome → drafting
drafting → (a scene needs a system) → Worldbuilding on demand → scene
```

## Inputs

The premise or world seed; existing world canon; the Story Genome if one exists (so the world serves the story's question).

## Outputs

`world_brief`, `system_chains`, `pressure_map`, `world_hooks`.

## State

- **Writes:** `world/<system>.yaml` records (rules, institutions, norms, places, social state), each with provenance.
- **Stores:** the brief and chains under `pack_state.worldbuilding`.
- **Canon:** invented systems are `agent_proposal` or `delegated_decision` until approved. In-world disagreements (competing histories, religions) are `in_world_belief` records, not contradictions — see [canon resolver](../runtime/canon-resolver.md#before-calling-something-a-contradiction).

## Procedure

```text
1. Read canon and the premise. Identify the 1–3 CORE CONDITIONS that make this world different.
2. Pick the SYSTEMS those conditions touch that the story will use (not all of them).
3. Build a CAUSAL CHAIN for each.
4. Cross-check chains against each other (a magic rule should affect the economy it touches).
5. Build the PRESSURE MAP: who benefits, who pays, who resists.
6. Turn consequences into WORLD HOOKS: scene-usable costs, conflicts, and expectations.
7. Mark what stays unknown to characters, and what stays contested in-world.
8. Ask at most 3–5 questions, only if a chain can't proceed without a choice.
```

### Systems

Use only the ones the story touches.

| Group | Systems |
|---|---|
| **Material** | geography, climate, resources, technology, magic, transportation, healthcare |
| **Power** | governance, law, military, policing, criminal systems |
| **Exchange** | economy, labor, debt, trade |
| **Meaning** | religion, culture, language, media, education, historical memory |
| **Belonging** | class, caste, race and ethnicity (when relevant), family structures, kinship, citizenship |

**Race, ethnicity, religion, and culture** — invented or real — are handled with care: avoid mapping real groups onto invented stereotypes; when a real culture is referenced, route through research mode.

### Causal chains

```yaml
system_chain:
  system:
  condition:                  # the material or metaphysical fact
  incentive:                  # what it makes people want or fear
  institution:                # what gets built to manage it
  social_norm:                # what everyone learns to expect
  personal_consequence:       # what it costs or gives a specific kind of person
  who_benefits: []
  who_pays: []
  who_resists: []
  contested_by: []            # in-world disagreements about it
  unknown_to_most:            # what ordinary characters don't know
  prov:
```

**Every chain ends in a person.** If a system never reaches a character's choices, it's background — keep it to a line.

**Chains must interlock.** A magic that heals changes healthcare, which changes labor, which changes family structure. Check each new chain against the others for contradictions and for consequences you haven't used.

### Pressure map

```yaml
pressure_map:
  - group:
    wants:
    fears:
    leverage:
    constrained_by: []
    in_conflict_with: []
```

Societies are not unanimous. Every major institution has true believers, reformers, opportunists, the exhausted, and the trapped.

### World hooks

Convert consequences into things scenes can use:

```yaml
world_hooks:
  - hook:                     # one line a scene can build on
    type:                     # cost | block | expectation | taboo | opportunity | misunderstanding | breakdown
    system:
    who_feels_it:
    scene_use:                # where it could enter the story
```

Useful hook types, from [world state](../core/world-state.md): what characters use, what blocks them, what costs money, status, or time, what is illegal or taboo, what breaks, what people misunderstand, what a character takes for granted, what a stranger notices.

### Output discipline

- **Build to need.** Expand a system when a scene uses it; leave the rest as a line.
- **Deliver as use.** When drafting, reveal systems by their effects on a scene, never as a paragraph of lore unless the lore itself is the conflict. Run the [worldbuilding audit](../core/world-state.md#description-and-worldbuilding-through-use).
- **Leave gaps.** Real societies have things no one fully understands. Mark them.

## Guardrails

- No encyclopedia output. No 200-question forms.
- Every system connects to a person's choices or it stays a line.
- Invented systems are proposals until approved.
- In-world disagreement is recorded as belief, not flattened into one "true" version.
- Real cultures and places go through research mode.

## Failure modes

| Failure | Looks like | Fix |
|---|---|---|
| Encyclopedia | Pages of categories unrelated to the premise | Build only chains the story touches |
| Rootless detail | Exotic customs with no cause | Trace to a condition and incentive |
| Unanimous society | Everyone believes the same thing | Add the pressure map's dissenters |
| Lore dump | Systems explained before they matter | Deliver through use |
| Frictionless magic | Power with no social consequence | Chain it through economy, law, or class |
| Isolated systems | A rule that never touches another | Cross-check chains |

## Schemas

```yaml
world_brief:
  version: "1.0"
  core_conditions: []
  systems_in_use: []
  tone:
  scale:                      # village | city | nation | world | cosmos
  real_world_analogues: []    # flagged for research mode
  unknowns: []
  contested: []
  provenance: {confirmed_facts: [], delegated_decisions: [], agent_proposals: [], unresolved_questions: []}
```

## Examples

**Seed:** a river city where debts are inherited by whoever holds the family boat. *(Generic demo.)*

```yaml
system_chain:
  system: economy / debt
  condition: Debt attaches to a family's boat, not to a person.
  incentive: Holding the boat means inheriting the debt; abandoning it means losing the family's trade.
  institution: The Mooring Registry records which boat carries which debts; registry clerks can be bribed to "lose" an entry.
  social_norm: Eldest children are pressured to take the boat; younger children leave the river. "Taking the tiller" is both honor and sentence.
  personal_consequence: A daughter who loves the river must choose between her mother's debts and a life on land.
  who_benefits: [creditors, registry clerks]
  who_pays: [eldest children, river families]
  who_resists: [boat-burners who sink family boats to void the debt]
  contested_by: [a temple that teaches debts pass to the soul, not the boat]
  unknown_to_most: The registry has never been audited.
```

Hooks: a boat-burning is a crime and a mercy (taboo); a clerk offers to lose a debt for a price (opportunity); a suitor asks which child will take the tiller (expectation); a sunk boat's debt transfers to the nearest kin under an old clause (breakdown).

## Behavior tests

| Fixture | Checks |
|---|---|
| [F28](../tests/fixtures/F28-worldbuilding-through-use.yaml) | A full chain to a personal consequence; scene-usable hooks; few questions; no encyclopedia. |
| [F22](../tests/fixtures/F22-intentional-contradiction-preserved.yaml) | Competing in-world beliefs are not flagged as errors (resolver behavior the pack relies on). |

## Research provenance

[research/packs/worldbuilding.md](../research/packs/worldbuilding.md). This is a **design** module. The chain is a causal-reasoning scaffold, not a model from social science; worldbuilding-through-use comes from the core craft research. No dedicated source was used for the chain itself.

## Integration

- **Core:** writes [world state](../core/world-state.md); uses [social-state propagation](../core/relationships.md#social-state-propagation) for rumor and reputation; routes real analogues through research mode.
- **Series:** faction tracks read from pressure maps.
- **Mystery:** institutions supply means, opportunity, and cover-ups; the registry clerk is a suspect.
- **Horror:** taboos and contamination rules come from the belief systems here.
- **Tragic engine:** ideological conflict uses the pressure map's `VALUE → FEAR → POLICY → HUMAN COST` view.
