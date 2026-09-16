# Creativity Search

How to generate genuinely different candidates instead of one idea in several costumes, and how to choose among them.

| Contract | |
|---|---|
| Invoked by | Router (SHORT STORY, LONG-FORM), Story Genome, Ending Search, and any pack that needs options (Draft Starter's creative possibilities, Mystery's culprit search). |
| When | A high-leverage creative decision is open: premise, twist, central conflict, ending family, a stuck scene. |
| Needs | `intent_lock`; `story_genome.anti_goals` if present. |
| Produces | A candidate portfolio with a novelty profile; the selected candidate feeds Story Genome. |
| State | Ephemeral. Rejected candidates worth keeping go to `summaries/` as notes, never to `canon`. |
| Consumed by | [story-genome](story-genome.md), [endings](endings.md), [critics](critics.md). |
| Skip when | Minor decisions; FAST SCENE MODE; any decision the user has already made. |
| Tests | F21 |
| Research | [research/core/creativity.md](../research/core/creativity.md) |

---

## Divergent Creative Search

*Basis: [@noveltybench], [@avoidance-decoding]*

Current LLMs often produce several answers that appear different but occupy the same conceptual basin.

For important creative decisions, generate a population rather than one answer.

Default population sizes:

```text
minor decision: 3-5
scene solution: 4-8
major character conflict: 6-10
premise: 8-15
central twist: 8-15
ending family: 6-12
```

Do not waste tokens generating 15 cosmetic variants.

Each candidate must differ along at least two substantive axes:

- causal mechanism;
- character motivation;
- relationship configuration;
- setting logic;
- information structure;
- temporal structure;
- moral problem;
- consequence;
- ending logic;
- narrative schema.

---

## Creative Utility Selection

*Basis: [@create], [@genie]*

Inspired by research that treats creativity as a combination of quality and distance from already-selected ideas.

When selecting a set of candidates, do not simply rank each candidate independently.

Choose iteratively.

For candidate `c`:

```text
creative_utility(c)
=
quality(c)
× minimum_distance(c, already_selected_candidates)
```

Use qualitative 1-5 estimates when no embedding system is available.

```yaml
candidate:
  quality:
    coherence:
    emotional_potential:
    character_specificity:
    thematic_relevance:
    generative_potential:
  distance:
    concept_difference:
    causal_difference:
    discourse_difference:
    ending_difference:
```

The first selected candidate should be the strongest overall.
Later candidates should add genuinely different possibilities.

This creates a portfolio rather than a pile of paraphrases.

---

## Associative Creativity Search

*Basis: [@create]*

For difficult invention tasks, deliberately explore conceptual bridges.

Procedure:

1. Extract 2-4 core concepts from the premise.
2. Search for multiple meaningful connections between them.
3. Reject generic association chains.
4. Prefer connections that are specific and narratively actionable.
5. Use the strongest connections to generate story candidates.

Example:

```text
concepts:
inheritance
weather
guilt
small-town government
```

Possible bridges:

```text
inheritance → ownership → dam control → flood risk
weather → old records → hidden pattern → family deception
guilt → public policy → deliberate inaction → inherited consequence
weather → ritual calendar → relationship secret → social exposure
```

The purpose is not to insert every concept.
The purpose is to reach parts of the idea space the model would not normally sample first.

---

## Fine-Grained Novelty Profile

*Basis: [@genie]*

Do not evaluate "originality" as a single vague property.

Create project-specific novelty axes.

Default fiction axes:

```yaml
novelty_profile:
  premise:
  central_conflict:
  character_roles:
  relationship_topology:
  setting:
  world_rule:
  causal_mechanism:
  narrative_structure:
  temporal_structure:
  revelation_strategy:
  ending:
  imagery:
  social_dynamics:
  point_of_view:
```

For a candidate, ask:

- What is unusual here?
- What is conventional here?
- Which axis carries most of the novelty?
- Is the novelty meaningful?
- Is it merely decorative?
- Does another candidate already occupy this same combination?

Avoid requiring every axis to be novel.
A story can have a familiar setting and an unusual social mechanism.

---

## Discourse Diversity Check

*Basis: [@qudsim]*

Different stories can reuse the same hidden discourse progression.

Represent each candidate as a sequence of Questions Under Discussion.

Example:

```text
Q1: Why did the sister disappear?
Q2: Is the father hiding something?
Q3: What happened in the basement?
Q4: Was the disappearance voluntary?
Q5: What did the protagonist do years ago?
Q6: What will the protagonist sacrifice to reveal it?
```

Compare candidate question sequences.

Flag candidates that share:
- the same question order;
- the same reveal order;
- the same "false answer → correction → culprit" progression;
- the same escalation mechanism;
- the same final question.

Regenerate structurally redundant candidates.

Discourse diversity matters even when names, locations, and props differ.

---

## Structural Rarity Pass

*Basis: [@storyscope], [@noveltybench]*

Ask:

```text
If I generated this premise ten times, would I expect this structure often?
```

Check:
- opening strategy;
- first major turn;
- midpoint function;
- reveal sequence;
- antagonist function;
- relationship arc;
- climax mechanism;
- ending family.

If too many choices feel like the highest-probability default, revisit one or two high-level decisions.

Do not make every component strange.
