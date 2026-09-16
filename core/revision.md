# Revision

Revise macro before micro. Ordered passes, the common-mistake audit, and the quality gate.

| Contract | |
|---|---|
| Invoked by | Router for revision requests; after drafting in SHORT STORY and LONG-FORM modes; the quality gate before returning substantial fiction. |
| When | After a draft exists. |
| Needs | The draft; findings from [critics](critics.md) and [continuity](continuity.md); `intent_lock`. |
| Produces | Revised draft; a pass log naming what changed and why. |
| State | Ephemeral. Canon-affecting changes go through the [canon resolver](../runtime/canon-resolver.md). |
| Consumed by | The user; [memory](memory.md) for state re-extraction if events changed. |
| Skip when | Line-edit passes when a macro problem is still open. CRITIC MODE analyzes without revising unless asked. |
| Tests | F30 |
| Research | [research/core/page-craft.md](../research/core/page-craft.md) |

---

## Craft Revision Passes

Do not revise everything at once, and do not line-edit a structurally broken story.

```text
STORY PHYSICS
→ SCENE NECESSITY
→ ENTRY / EXIT
→ SHOW / TELL
→ POV / PSYCHIC DISTANCE
→ DIALOGUE / SUBTEXT
→ EXPOSITION
→ SPECIFICITY / IMAGE
→ SETUP / PAYOFF
→ RHYTHM / PACING
→ READER TRUST
→ LINE EDIT
```

Use passes:

### Pass 1 — Story physics
Check:
- causality;
- agency;
- motivation;
- chronology;
- world rules.

### Pass 2 — Scene necessity
For each scene:
- goal;
- resistance;
- change;
- carry-forward pressure.

Cut/merge/compress weak scenes before polishing sentences.

### Pass 3 — Entry / Exit
Run:
- enter-late test;
- leave-early test;
- orientation check.

### Pass 4 — Show / Tell
Mark:
- emotionally consequential dramatization;
- summary;
- exposition;
- repeated explanation.

Rebalance.

### Pass 5 — POV / Psychic Distance
Check:
- knowledge boundaries;
- head-hopping;
- accidental distance shifts;
- character-filtered detail.

### Pass 6 — Dialogue / Subtext
Check:
- hidden sentence;
- tactics;
- exposition;
- voice difference;
- read aloud.

### Pass 7 — Exposition
Release only what current action needs.
Check each block of backstory or lore against [need-to-know routing](information-architecture.md#exposition-and-backstory-need-to-know-routing).

### Pass 8 — Specificity / Image
Replace generic claims with selective concrete evidence.
Remove inventory description and sensory clutter.

### Pass 9 — Setup / Payoff
Track active promises and missing seeds.

### Pass 10 — Rhythm / Pacing
Check:
- paragraph density;
- sentence rhythm;
- scene/summary balance;
- emotional intensity variation.

### Pass 11 — Reader Trust
Remove:
- theme explanation;
- emotional restatement;
- redundant interpretation.

### Pass 12 — Line Edit
Only now optimize:
- syntax;
- diction;
- modifiers;
- repetition;
- sound.

---

## Common Human / Novice Writer Mistake Audit

*Basis: [@reedsy-novice-mistakes], [@lott-novice-mistakes], [@ebsco-teaching-cw], [@wd-exposition-early], [@wd-pov]*

These are recurring problems reported by editors, teachers, and writing coaches.
They are not universal laws and are not empirical prevalence estimates.

Audit for:

### 1. Writer-knows, reader-doesn't confusion
The author can picture the scene, but necessary orientation never reached the page.

Fix:
- clarify time/place/speaker/action;
- do not solve confusion with a paragraph of unrelated exposition.

### 2. Generic language
"Beautiful," "angry," "old," "strange," "nice."

Fix:
- replace with one useful specific.

### 3. Inventory description
Head-to-toe character description or room catalog.

Fix:
- select details with narrative/POV function.

### 4. Exposition too early
The novel explains history before the reader has a present-tense reason to care.

Fix:
- delay, dramatize, or show-then-tell.

### 5. Dialogue as information dump
Characters explain facts both already know.

Fix:
- give them conflicting objectives; release information under pressure.

### 6. On-the-nose dialogue
Characters say their subtext aloud repeatedly.

Fix:
- define the hidden sentence and write around it.

### 7. Dialogue in a vacuum
Pages of speech with no bodies, objects, setting, or action.

Fix:
- anchor action beats selectively.

### 8. Everyone has the same voice
Same sentence length, vocabulary, wit, politeness, and metaphor system.

Fix:
- differentiate social history, education, rhythm, goals, and tactics.

### 9. Head-hopping
Interior access jumps minds without a deliberate POV system.

Fix:
- choose scene POV and psychic-distance boundaries.

### 10. Scene starts before it starts
Arrival, greetings, coffee, weather, setup.

Fix:
- test entering later.

### 11. Scene continues after it ends
Characters recap meaning after the turn.

Fix:
- test leaving earlier.

### 12. Nothing changes
A scene has atmosphere but no intentional function.

Fix:
- add change, classify as texture, compress, or cut.

### 13. Stakes are huge but impersonal
"The world will end," but the character has no specific emotional relationship to that outcome.

Fix:
- define what "the end of the world" means to their world.

### 14. Character acts for outline convenience
Motivation appears after the plot requires it.

Fix:
- rebuild desire/belief/pressure before action.

### 15. "Show don't tell" becomes cliché-body-language soup
Every feeling gets pulse, breath, jaw, stomach, chest.

Fix:
- choose character-specific evidence or use a direct label.

### 16. The writer explains after showing
Reader inference is immediately translated into a moral.

Fix:
- run echo audit.

### 17. Purple or modifier-heavy prose
Adjectives/adverbs decorate weak nouns/verbs.

Fix:
- test stronger noun/verb; keep modifiers that change meaning.

### 18. Research flex
Facts appear because the writer learned them, not because the story needs them.

Fix:
- need-to-know exposition.

### 19. Setup with no payoff
Attention is drawn to an object/question that disappears.

Fix:
- pay it, intentionally abandon it, or reduce emphasis.

### 20. Payoff with no setup
Solution/reveal arrives without enough prior possibility.

Fix:
- seed evidence or capability earlier.

### 21. Flat emotional intensity
Every paragraph is maximum dread, grief, wit, beauty, or violence.

Fix:
- create contrast and recovery.

### 22. Theme is explained
Narrator/character states what the story "means" after the events already demonstrated it.

Fix:
- trust image, action, consequence, and unresolved interpretation.

### 23. Ending is too neat
Every relationship heals, every question closes, protagonist fully understands themselves.

Fix:
- close the story's required contract, not every human contradiction.

### 24. Ending is too abrupt
Climax occurs and story cuts before the important consequence lands.

Fix:
- add the smallest necessary aftermath.

### 25. Revision becomes line-polish before story repair
Writer perfects sentences inside scenes that may later be cut.

Fix:
- revise macro → scene → paragraph → sentence.

---

## Mistake matrix

These are **recurring craft problems reported by editors, teachers, and writing coaches**, especially in first manuscripts.

They are not universal human behaviors and not prevalence statistics.

### Diagnostic matrix

| Problem | What it looks like | Repair |
|---|---|---|
| Reader disorientation | writer knows who/where/when; page doesn't | clarify the minimum orientation |
| Generic description | "beautiful," "scary," "old," "angry" | choose one specific piece of evidence |
| Inventory description | head-to-toe / room census | select details with function |
| Early info dump | history before present tension | defer or show-then-tell |
| Expository dialogue | characters brief each other on known facts | put info under genuine conflict/need |
| On-the-nose dialogue | people state exact feelings and motives | define hidden sentence + tactic |
| Dialogue vacuum | talking heads in white space | selective action/setting beats |
| Same voice | every character equally witty/eloquent | vary tactics, rhythm, vocabulary, caution |
| Head-hopping | interior facts jump between minds | lock POV + distance |
| Warm-up scenes | arrivals, greetings, commute before conflict | enter later |
| Lingering scenes | recap after turn | leave earlier |
| Static scene | no story state changes | add function/change or compress |
| Inflated stakes | apocalypse with no personal meaning | define character-specific loss |
| Puppet action | character moves because outline says so | repair belief/desire/pressure |
| Body-language clichés | heart/jaw/breath for every emotion | use character-specific behavior or direct label |
| Meaning redundancy | action + dialogue + thought + narrator repeat | keep strongest layer(s) |
| Modifier/purple overload | decoration obscures noun/verb | strengthen core words, cut redundant modifiers |
| Research flex | facts with no scene function | need-to-know filter |
| Missing payoff | emphasized element vanishes | pay, reduce emphasis, or mark intentional |
| Unseeded payoff | solution arrives from nowhere | plant possibility earlier |
| Flat intensity | everything is max emotion | add contrast/recovery |
| Overexplained theme | story states its own lesson | trust consequence/image/choice |
| Too-neat ending | all human contradiction resolves | close contract, leave life open |
| Too-abrupt ending | climax then immediate blackout | add minimal consequence |
| Micro-edit too early | polishing scenes that may be cut | revise macro → micro |

### Do not overcorrect

For every "mistake" ask:

> Is this accidental, or is the story using it deliberately?

Examples:
- a long arrival can build dread;
- a direct confession can be the point;
- a head-hop can be part of an omniscient voice;
- an info dump can work if voice is the entertainment;
- purple prose can belong to a baroque narrator.

Intent and effect outrank dogma.

---

## Quality gate — architecture

Run both gates before returning substantial fiction. This one checks the story's structure; the page-craft gate below checks its execution. FAST SCENE MODE runs only the page-craft gate's Scene, Show / Tell, POV, and Dialogue items.

Before returning a substantial story/chapter, verify:

### Identity
Does this feel specific to this project?

### Agency
Did characters act according to their state and knowledge?

### Causality
Do consequences emerge from prior events?

### Structural diversity
Is the story using the highest-probability AI plot skeleton?

### Information
Is reader knowledge intentionally managed?

### Suspense
Where relevant, are successful paths becoming meaningfully constrained?

### Psychology
Does the story evoke empathy/authenticity without reducing psychology to introspection?

### Affect
Does emotional intensity vary?

### Revelation
Does important new information alter meaning or action?

### Continuity
Are chronology, knowledge, abilities, geography, facts, tone, and world rules consistent?

### Theme
Did the draft trust the reader enough?

### Ending
Did it close what should close and leave open what should remain open?

If multiple checks fail, revise the relevant layer, not merely the wording.

---

## Quality gate — page craft

Before returning substantial fiction, ask:

### Story
- Does a character want something specific enough to generate behavior?
- Do choices create consequences?
- Are important surprises causally usable?

### Scene
- Does each major scene have a deliberate function?
- What changes?
- Does it enter and exit at useful points?

### Show / Tell
- Are important moments experienced rather than merely reported?
- Is summary used intelligently for compression?
- Did "showing" become generic body-language clutter?

### POV
- Is psychic distance deliberate?
- Are details filtered through the correct mind?
- Any accidental head-hopping?

### Dialogue
- Is there subtext where social/psychological pressure would create it?
- Are voices distinct?
- Is dialogue carrying unnatural exposition?

### Exposition
- Is information arriving because it matters now?
- Is backstory answering a question the reader actually has?

### Specificity
- Are details selective and useful?
- Any inventory description?

### Tension
- What does the character risk?
- What closes off options?
- Does quiet material still contain pressure?

### Setup / Payoff
- Are conspicuous promises paid, transformed, or intentionally left open?
- Are important payoffs sufficiently seeded?

### Theme
- Does the story trust the reader?
- Is the narrator explaining the moral after the events already did?

### Ending
- Did the climax produce visible consequence?
- Is there enough aftermath?
- Is there too much explanation?

### Prose
- Is the voice specific to this project?
- Is sentence rhythm varied by function?
- Did line polish hide a larger story problem?

When checks fail, revise the **relevant layer**, not merely wording.
