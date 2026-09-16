# AI Narrative Default Guardrails
## StoryScope-informed, v0.4

StoryScope (Russell et al., 2026) found that discourse-level narrative features can distinguish
AI-generated from human-authored fiction even without style signals.

Important aggregate tendencies reported by the study:

AI fiction more often:
- over-explains theme;
- favors tidier single-track causal plots;
- uses fewer subplots;
- reaches cleaner protagonist-centered resolutions;
- uses more embodied/sensory emotional expression.

Human fiction in the dataset more often:
- permits morally mixed framing;
- uses more temporal discontinuity;
- leaves more structural mess/loose ends;
- occupies a wider narrative feature space.

## How v0.4 uses this

As diagnostics:

```text
Is the draft suspiciously clean?
Is the lesson stated?
Did every subplot converge?
Did the protagonist solve everything through one clear choice?
Is emotion constantly rendered through body sensations?
```

## How v0.4 does NOT use this

Do NOT force:
- nonlinear chronology;
- moral ambiguity;
- extra subplots;
- unresolved endings;
- reduced sensory detail.

Those would merely create a new formula.

The target is **deliberate range**, not "human-looking" camouflage.
