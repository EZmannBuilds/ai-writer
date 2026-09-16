# Continuity

Finding contradictions with evidence from both sides, and knowing when a contradiction is intentional.

| Contract | |
|---|---|
| Invoked by | Router after drafting in LONG-FORM MODE; CRITIC MODE; any time the user asks "is this consistent?". |
| When | After each scene (local), each chapter, and each movement (macro). |
| Needs | The draft; `timeline`; `canon` with provenance; `characters`. |
| Produces | `continuity_issue` records, each citing both conflicting sources. |
| State | `continuity.issues` — `.ai-writer/project.yaml`; resolved conflicts go through the [canon resolver](../runtime/canon-resolver.md). |
| Consumed by | [revision](revision.md), [canon-resolver](../runtime/canon-resolver.md). |
| Skip when | Never "fix" a contradiction marked intentional in provenance (unreliable narrator, in-world belief, alternate continuity). |
| Tests | F15, F22 |
| Research | [research/core/planning-memory.md](../research/core/planning-memory.md), [research/core/reader-psychology.md](../research/core/reader-psychology.md) |

---

## Consistency Taxonomy

*Basis: [@lost-in-stories]*

Check long stories across five major categories.

### Timeline and Plot Logic

- absolute-time contradiction;
- duration contradiction;
- simultaneity contradiction;
- causeless effect;
- causal logic violation;
- abandoned plot element.

### Characterization

- memory contradiction;
- knowledge contradiction;
- skill fluctuation;
- forgotten ability.

### Worldbuilding

- core-rule violation;
- social-norm violation;
- geographical contradiction.

### Factual and Detail Consistency

- appearance mismatch;
- nomenclature confusion;
- quantitative mismatch.

### Narrative and Style

- perspective confusion;
- tone inconsistency;
- style shift.

Intentional exceptions must be marked:
- unreliable narration;
- deception;
- altered memory;
- mystery;
- approved retcon;
- deliberate stylistic rupture.

---

## Evidence-Based Continuity Checker

*Basis: [@lost-in-stories]*

Do not merely ask "Is this consistent?"

Use four stages:

```text
1. category-guided extraction
2. contradiction pairing
3. evidence chain
4. structured report
```

For each suspected contradiction:

```yaml
continuity_issue:
  category:
  claim_a:
  source_a:
  claim_b:
  source_b:
  contradiction_reason:
  confidence:
  intentional_possible:
  proposed_repairs: []
```

The checker must point to both sides of the conflict.

---

## Situation-Model Continuity

*Basis: [@event-indexing]*

For scene transitions, ask:

```text
What remained continuous?
What changed in time?
What changed in space?
Which character/entity became active?
What causal chain continues?
Which goal or intention continues?
```

A high-discontinuity transition can be useful for:

- shock;
- ellipsis;
- chapter breaks;
- disorientation;
- nonlinear structure.

But repeated unmarked discontinuity may produce confusion instead of intrigue.

Do not "fix" intentional discontinuity.
Signal enough for the reader to reconstruct the new situation.
