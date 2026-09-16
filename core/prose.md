# Prose

Turning a scene contract into sentences: dramatize what the reader should experience, compress what the reader only needs to know.

| Contract | |
|---|---|
| Invoked by | Router for every prose draft. Comic Panel Writer is the alternate output register. |
| When | Drafting; during the Show/Tell, Specificity, and Reader Trust revision passes. |
| Needs | `scene_contract`; POV and distance; dialogue plan; `intent_lock` style fields. |
| Produces | Draft prose. |
| State | The manuscript stays in the user's own files. State extraction afterward goes through [memory](memory.md). |
| Consumed by | [revision](revision.md), [critics](critics.md), [memory](memory.md) (state extraction). |
| Skip when | Planning-only requests; Comic Page Map / Panel Breakdown / Full Script output. |
| Tests | F19, F21 |
| Research | [research/core/page-craft.md](../research/core/page-craft.md), [research/core/critique-evaluation.md](../research/core/critique-evaluation.md) |

---

## Prose generation rules

The prose writer should:

- obey POV knowledge boundaries;
- filter description through the POV character's priorities, history, fear, desire, and attention;
- control psychic distance deliberately rather than drifting accidentally;
- prioritize scene-specific language and concrete nouns/verbs over generic intensifiers;
- preserve subtext;
- vary paragraph density;
- vary sensory density;
- vary sentence rhythm according to scene function;
- allow direct emotion labels when they are the strongest, cleanest choice;
- show emotionally consequential moments through evidence, choice, action, dialogue, image, or contradiction;
- tell/summary-compress routine, connective, low-priority, or already-understood material;
- use show-then-tell when unfamiliar/speculative phenomena require both experience and explanation;
- avoid stock body-language substitutions for every emotion;
- avoid explaining an image immediately after presenting it;
- avoid restating the same feeling through narration + dialogue + internal thought + metaphor;
- avoid ending every scene with an aphorism;
- avoid universal polished eloquence;
- allow awkwardness when a character would be awkward;
- allow ordinary detail when it creates credibility or contrast;
- choose a few telling details rather than inventorying every visible object;
- preserve reader inference when the intended meaning is already legible;
- read significant dialogue aloud during revision when possible.

The rule is not "show, never tell."

The rule is:

> Dramatize what the reader should experience. Compress what the reader only needs to know.

The craft sections below — show/tell, specificity, reader trust — are the working detail behind these rules. POV and psychic distance live in [pov](pov.md); dialogue in [dialogue](dialogue.md); exposition in [information-architecture](information-architecture.md#exposition-and-backstory-need-to-know-routing).

**Alternate output register.** When the output should carry comic-book visual logic or real page/panel scripting, [Comic Panel Writer](../packs/comic-panel-writer.md) takes over the page. It is an alternate register for these rules, not a replacement: its default Comic Narrative mode is still prose.

---

## The page-level craft layer

The architecture modules — character simulation, reader state, suspense, novelty, continuity, anti-default structure — decide *what* happens. This layer decides how it lands on the page.

It asks:

```text
Is this the right scene?
→ Is the scene entering at the right pressure point?
→ Who wants what right now?
→ What changes?
→ What should be shown?
→ What should be told/summary-compressed?
→ What is the POV character actually capable of noticing?
→ What is being said vs. meant?
→ What information is needed now?
→ What setup/payoff is active?
→ Where should the scene cut?
```

These are diagnostics, not laws.

A slow scene can be excellent.
A direct emotional statement can be excellent.
A long description can be excellent.
A scene without overt conflict can be excellent.

The question remains:

> Was the choice deliberate, and what effect does it produce?

---

## Show–Tell Decision Engine

*Basis: [@friedman-show-tell], [@kole-show-tell], [@storyscope]*

"Show, don't tell" is useful only when it is treated as a **control dial**, not a ban on summary.

### Prefer showing when the reader should EXPERIENCE:

- a consequential choice;
- a relationship shift;
- a revelation;
- a first encounter;
- an irreversible action;
- a contradiction between words and behavior;
- a moment whose emotional interpretation should belong partly to the reader;
- a setting detail that reveals character;
- the exact behavior that makes a claim believable.

### Prefer telling / summary when the reader only needs to KNOW:

- routine actions;
- connective travel;
- repeated behavior already established;
- low-priority time passage;
- unimportant logistics;
- background that would be tedious as full scene;
- information whose dramatization would steal emphasis from the real scene.

### Show, then tell

Useful in speculative, technical, historical, or unfamiliar settings:

```text
reader experiences strange thing
→ curiosity forms
→ concise explanation answers only what is now necessary
```

This is usually stronger than explaining the rule before the reader has a reason to care.

### Telling can carry voice

"Tell" does not mean "write neutrally."

Summary can reveal:
- attitude;
- irony;
- prejudice;
- compression;
- cultural assumptions;
- retrospective judgment.

### Avoid body-language pantomime

Do not translate every emotion into:
- clenched jaw;
- racing heart;
- hitched breath;
- tightened chest;
- stomach drop;
- fists;
- tears.

Those can be valid details.
They become weak when they are interchangeable emotional emojis.

Prefer:
- character-specific behavior;
- choice;
- speech error;
- fixation;
- avoidance;
- object interaction;
- altered plan;
- unusual attention.

Sometimes the strongest line is simply:
> She was afraid.

Direct naming is allowed when it has more force than another generic physiological cue.

### Do not tell after a successful show

If action/dialogue/image already makes the meaning legible, resist immediately explaining it.

Use the **echo audit**:

```text
Did narration label what action just demonstrated?
Did internal thought repeat what dialogue just admitted?
Did metaphor restate the emotion a third time?
```

If yes, delete or transform at least one layer unless repetition is intentionally rhetorical.

---

## Specificity Without Inventory

*Basis: [@reedsy-novice-mistakes], [@lott-novice-mistakes]*

Common weak description is generic:

```text
nice house
beautiful woman
scary basement
old car
angry man
```

Another weak form is exhaustive:

```text
hair
eyes
shirt
shoes
wall
desk
lamp
rug
window
```

Prefer **selective specificity**.

### Detail selection rule

Choose details that do at least one:

- reveal POV;
- reveal status/class/history;
- create a usable image;
- affect action;
- foreshadow;
- create contrast;
- carry motif;
- establish atmosphere;
- become relevant later.

### POV detail test

Ask:

> Would this character, in this emotional state, notice this detail before the others?

If no, either remove it or move to a more appropriate narrator distance.

---

## Reader-Trust / Redundancy Audit

*Basis: [@ebsco-teaching-cw]*

Strong prose often leaves a small amount of work for the reader.

Check for **meaning duplication**.

Common pattern:

```text
action shows emotion
+
dialogue states emotion
+
internal thought explains emotion
+
narrator summarizes emotion
```

Choose the strongest layer(s).

### Trust test

Ask:

- Can the reader infer this?
- Is ambiguity productive?
- Is the explanation necessary for plot comprehension or only reassurance?
- Does deleting the explanatory sentence make the passage stronger?

Do not confuse reader trust with obscurity.

Necessary facts should be clear.
Interpretation can remain open.

---

## Show–tell quick card

"Show, don't tell" is a **priority system**.

It is not:
> never state anything directly.

### Decision tree

#### 1. Is this moment emotionally, relationally, or causally important?
If YES, lean toward dramatization.

#### 2. Is the point mainly to move through time or logistics?
If YES, lean toward summary/telling.

#### 3. Is the setting/world unfamiliar enough that inference will fail?
Use **show → question → tell only what answers the live question**.

#### 4. Has the draft already shown the meaning?
Do not immediately explain it again.

---

### Ways to show

Not just body language.

Use:
- choices;
- mistakes;
- contradictions;
- object interaction;
- dialogue;
- silence;
- altered plans;
- attention/fixation;
- what a character refuses to see;
- what they notice first;
- consequence.

### Ways to tell well

Use:
- narrator voice;
- compressed time;
- retrospective judgment;
- social context;
- concise backstory;
- repeated routine;
- transitions.

Telling can be stylish, biased, funny, bitter, intimate, or unreliable.

---

### Emotion checklist

Before writing "he clenched his jaw":

Ask:
- What would THIS person do?
- What would they try to hide?
- What task would suddenly become difficult?
- What would they notice?
- What decision changes?
- What sentence can they not say?

If no specific behavior is stronger than a direct label, use the direct label.

---

### Redundancy test

Weak:

```text
show
→ explain
→ repeat in dialogue
→ repeat in thought
```

Better:

```text
choose the strongest channel
→ let the reader finish the inference
```

---

### Scene/summary balance

Use scene for:
- firsts;
- lasts;
- irreversible turns;
- confrontations;
- revelations;
- important failures;
- intimacy;
- danger;
- decisions.

Use summary for:
- repeated attempts;
- travel;
- routines;
- low-priority aftermath;
- periods where change is gradual.

Break these defaults whenever the artistic effect requires it.
