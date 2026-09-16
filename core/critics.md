# Critics

Specialized critics, a leader who may reject them, and the rules that stop criticism from sanding a strange story into a generic one.

| Contract | |
|---|---|
| Invoked by | Router in CRITIC MODE, and on the schedule below in SHORT STORY and LONG-FORM modes. |
| When | Plan level (macro critics) before drafting; prose level (micro critics) after; per the critic schedule. |
| Needs | The plan or draft; `intent_lock`; `story_genome`. |
| Produces | Labeled `finding` records; a leader decision. |
| State | Ephemeral; accepted plan changes update `story_genome` / `outline`. |
| Consumed by | [revision](revision.md), [outlining](outlining.md). |
| Skip when | Don't run every critic after every paragraph. FAST SCENE MODE runs one targeted critic at most. |
| Tests | F19, F30 |
| Research | [research/core/critique-evaluation.md](../research/core/critique-evaluation.md) |

---

## Automatic Judge Warning

*Basis: [@limits-auto-eval]*

Automated judges are not the reader.

Potential failure loop:

```text
AI writes unusual story
→ AI critic dislikes ambiguity
→ revision explains ambiguity
→ critic asks for clearer theme
→ revision states theme
→ critic asks for cleaner resolution
→ revision resolves relationships
→ final story becomes generic
```

Prevent this by requiring critics to label findings:

```yaml
finding:
  type: defect|risk|preference|intentional_choice|uncertain
  severity:
  evidence:
  why_it_matters:
  revision_options: []
  preserve_if_intentional:
```

The Editor may reject a critique.

---

## Critic Scheduling

Do not run every critic after every paragraph.

Suggested cadence:

### Every scene
- character/action check;
- local continuity;
- scene purpose.

### Every chapter
- engagement;
- dialogue/prose where needed;
- open loops;
- character/relationship state.

### Every major movement
- StoryScope audit;
- originality/discourse audit;
- psychological-depth profile;
- suspense/affect curve;
- macro continuity.

### Before ending
- ending critic;
- open-loop audit;
- revelation setup audit;
- thematic over-explanation audit.

---

## Psychological Depth Scale

*Basis: [@psych-depth]*

Evaluate stories using five distinct reader-centered dimensions.

### Emotion Provocation

Can the story produce meaningful emotional response?

Do not maximize emotion words.
Over-saturation may numb the reader.

### Empathy

Can the reader cognitively or emotionally inhabit the character's experience?

Empathy does not require likability.

### Engagement

Does the story sustain attention through:
- pacing;
- narrative flow;
- curiosity;
- suspense;
- investment?

### Authenticity

Do behavior, dialogue, relationships, and emotional consequences feel genuinely lived rather than mechanically written?

### Narrative Complexity

Does the story give the reader enough structure to mentally reconstruct, reinterpret, or puzzle through?

Complexity may come from:
- nonlinear narration;
- multiple perspectives;
- delayed causal understanding;
- conflicting accounts;
- recontextualization;
- layered character motives.

Narrative complexity is not syntactic complexity.

---

## Psychological Depth Critic Council

*Basis: [@psych-depth]*

Use separate personas when evaluating these dimensions.

```text
AUTHENTICITY CRITIC
Believability of people, dialogue, social behavior, emotional consequence.

EMPATHY CRITIC
Whether the text enables identification, perspective-taking, or emotional connection.

ENGAGEMENT CRITIC
Whether attention is maintained through pacing, suspense, curiosity, and flow.

EMOTION CRITIC
Whether emotional effects are earned, varied, and likely to land.

NARRATIVE COMPLEXITY CRITIC
Whether structure, character development, and recontextualization create productive cognitive depth.
```

Do not average them into one number without preserving the individual profile.

---

## StoryScope Anti-Default Audit

*Basis: [@storyscope]*

AI fiction exhibits recurring structural tendencies.

Audit for these patterns:

### Thematic Over-Determination

- theme stated too explicitly;
- narrator explains the lesson;
- moral/philosophical issue foregrounded too neatly;
- dialogue becomes thematic debate;
- subplots all reinforce one central theme too perfectly.

### Embodied/Sensory Overperformance

- every emotion becomes chest tightening, breath catching, pulse racing;
- setting mirrors mood automatically;
- sensory density remains high everywhere;
- smell/touch/body metaphors are used reflexively.

### Structural Streamlining

- one clean causal chain;
- no meaningful subplots;
- protagonist choice resolves everything;
- resolution defaults to internal understanding;
- character introductions rely on external description;
- every location and spatial relation is over-grounded.

### Reduced Human-Like Range

Inspect whether the story could benefit from:
- moral ambivalence;
- temporally displaced information;
- flashback/flash-forward;
- recontextualization;
- parallel subplots;
- greater location variety;
- more dialogue;
- explicit real-world/intertextual reference where appropriate;
- unresolved social tension.

Never insert these merely to pass the audit.

---

## StoryScope evidence summary

*Basis: [@storyscope]*

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

### How AI Writer uses this

As diagnostics:

```text
Is the draft suspiciously clean?
Is the lesson stated?
Did every subplot converge?
Did the protagonist solve everything through one clear choice?
Is emotion constantly rendered through body sensations?
```

### How AI Writer does NOT use this

Do NOT force:
- nonlinear chronology;
- moral ambiguity;
- extra subplots;
- unresolved endings;
- reduced sensory detail.

Those would merely create a new formula.

The target is **deliberate range**, not "human-looking" camouflage.

---

## Macro Creativity Critics

*Basis: [@critics]*

Before drafting a long story, run three plan-level critics:

### Critic A: Original Theme / Plot / Setting

Search for:
- conventional central material;
- unexplored cultural/social frames;
- more specific settings;
- more consequential premise variations;
- authenticity.

### Critic B: Unusual Structure

Search for:
- alternative ordering;
- viewpoint architecture;
- framing devices;
- nonlinear organization;
- embedded narratives;
- asymmetric acts/movements;
- structure generated by character/world logic.

### Critic C: Ending

Search for:
- predictable closure;
- unnecessary reconciliation;
- endings that merely state the theme;
- endings that do not exploit prior setup;
- stronger consequence structures;
- alternative closure families.

Each critic proposes one to three high-impact changes.

---

## Critic Leader

*Basis: [@critics]*

A leader/editor receives competing critic proposals.

The leader must evaluate:

```yaml
proposal:
  originality:
  coherence:
  interestingness:
  character_credibility:
  user_intent_fit:
  future_consequence:
  genericity_risk:
```

Select the strongest proposal or reject all.

Criticism is optional advice, not an order.

The leader protects:
- coherence;
- character identity;
- canon;
- user intent;
- useful ambiguity.

---

## Multi-Round Plan Refinement

*Basis: [@critics]*

For high-stakes projects:

```text
initial plan
→ critics
→ leader selection
→ revised plan A
→ critics
→ leader selection
→ revised plan B
→ evaluator compares all plan versions
→ final plan
```

Do not assume the final round is automatically best.

Preserve earlier candidates and compare them.

---

## Micro Creativity Critics

*Basis: [@critics], [@storyscope]*

At prose level, separate two kinds of expressive criticism.

### Image Critic

Checks:
- perceptual specificity;
- internal imagery;
- visual/auditory/tactile usefulness;
- concrete detail;
- whether sensory detail actually serves the scene.

Important:
StoryScope warns against reflexive sensory over-description.
The Image Critic must never equate "more sensory detail" with "better."

### Voice Critic

Checks:
- vocabulary specificity;
- rhythm;
- sentence structure;
- colloquial/informal speech when appropriate;
- character-specific language;
- authenticity.

The leader decides which kind of revision suits the sentence.

A dialogue line may need voice, not another description of someone's heartbeat.

---

## Evaluation Profile

*Basis: [@limits-auto-eval], [@psych-depth]*

```yaml
evaluation_profile:
  coherence:
  originality:
  discourse_diversity:
  character_credibility:
  agency:
  authenticity:
  empathy:
  engagement:
  emotion_provocation:
  narrative_complexity:
  suspense:
  curiosity:
  dialogue:
  prose:
  continuity:
  genre_fulfillment:
```

Use ratings only as navigation aids.

Do not optimize mechanically toward maximal numbers.
