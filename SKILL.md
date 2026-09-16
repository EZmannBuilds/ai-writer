---
name: ai-writer
version: 0.5
status: craft-integrated
license: CC-BY-NC-4.0
description: A research-informed fiction-writing skill for psychologically deep, structurally coherent, distinctive fiction, expanded with scene craft, show/tell control, psychic distance, dialogue subtext, exposition discipline, setup/payoff tracking, common-writer mistake audits, reader-trust checks, and specialized revision.
---

# AI Writer Skill v0.5

## 0.0 How this skill is laid out

**This file is the whole core system.** Everything else is loaded on demand, only when the work calls for it. Paths below are relative to this file.

```text
SKILL.md          ← you are here: the core system (§0–§103)
packs/            ← staged add-ons; load one when its trigger fires
craft/            ← one-page reference cards for page-level craft
research/         ← provenance, source claims, evaluation method
```

### `packs/` — pipeline add-ons

These run **in order**, in front of the core pipeline. Load a pack only when its trigger fires; skip any that don't apply.

| Stage | Pack | Load when |
|---|---|---|
| 1 | `packs/draft-starter.md` | A loose seed needs turning into a Draft Brief. Trigger: "Start Draft," or any undeveloped story idea. |
| 2 | `packs/origin-forge.md` | The story is about becoming a hero/villain/antihero identity. Trigger: "Start Origin." |
| 3 | `packs/tragic-anime-engine.md` | Dark action, tragic fantasy, lethal consequence, ideological conflict. Trigger: "Start Tragic Story." Companion: `packs/tragic-anime-lenses.md`. |
| — | `packs/comic-panel-writer.md` | Output should carry comic-book visual logic, or needs real page/panel scripting. Trigger: "Comic Mode." Not a planning stage — an output register, used at drafting time. |

Full pipeline when all are active:

```text
seed → Draft Starter → Origin Forge → Tragic Anime Engine
     → Intent Lock (§3) → Story Genome (§4) → outline → draft
     → Comic Panel Writer, if the output is visual
```

### `craft/` — page-level reference cards

Condensed, single-topic cards. The core system covers the same ground at length in §84–§103; reach for a card when you want the compressed checklist rather than the full treatment.

`show-tell.md` · `scene-craft.md` · `dialogue-subtext.md` · `pov-psychic-distance.md` · `exposition-backstory.md` · `common-mistakes.md` · `question-bank.md` · `revision-passes.md` · `storyscope-anti-defaults.md`

### `research/` — why the rules are the rules

`research-pass-4.md` (the craft-layer synthesis), `research/source-index.md` (every source and the specific claim it supports), `benchmark.md` (how to test whether this skill actually improves output).

**Reach for these when a rule seems wrong for the work at hand.** They exist so the reasoning can be argued with rather than obeyed blindly.

---

## 0. Purpose

This skill is designed for fiction generation, development, continuation, revision, and critique.

Its primary objective is not to make prose merely polished. It is to produce stories that are:

- captivating;
- distinctive;
- psychologically consequential;
- coherent over long spans;
- driven by character choices rather than outline convenience;
- structurally varied;
- capable of suspense, uncertainty, surprise, ambiguity, and emotional aftereffects;
- resistant to recurring LLM narrative defaults;
- faithful to user canon and intended artistic direction.

The skill treats fiction as a multi-stage cognitive task:

```text
intent
→ divergent search
→ narrative design
→ character/world simulation
→ dynamic outline
→ craft interrogation
→ scene planning
→ prose generation
→ craft audit
→ state extraction
→ specialized criticism
→ selective revision
→ continuity verification
```

Do not collapse this pipeline into a single "write a story" operation for substantial fiction unless the user explicitly requests a fast draft.

---

# 1. Governing Principles

## 1.1 User intent outranks research heuristics

Research findings are defaults and diagnostic tools, not commandments.

Never force:
- nonlinear structure;
- ambiguity;
- subplots;
- twists;
- moral complexity;
- suspense;
- literary experimentation;

when they conflict with the user's intended form.

A clean linear children's story may need clarity.
A fable may need an explicit moral.
A procedural mystery may need strict causality.
A surreal work may intentionally violate ordinary consistency.

The question is not "Is this convention present?"
The question is "Was this choice deliberate and useful?"

## 1.2 Story quality is multidimensional

Do not reduce quality to one score.

Evaluate separately:
- coherence;
- originality;
- engagement;
- emotional provocation;
- empathy;
- authenticity;
- narrative complexity;
- character credibility;
- suspense;
- curiosity;
- dialogue;
- prose;
- continuity;
- genre fulfillment.

## 1.3 Meaningful surprise beats random novelty

Unexpectedness alone is not creativity.

Prefer ideas that are:
- uncommon;
- causally usable;
- character-specific;
- emotionally meaningful;
- compatible with the world;
- capable of creating future consequences.

Randomness without consequence is noise.

## 1.4 Specialized analysis beats one giant critique

For substantial fiction, use separate analytical passes for separate dimensions.

Do not ask a single critic to simultaneously judge:
- plot;
- chronology;
- prose;
- psychology;
- originality;
- continuity;
- suspense;
- worldbuilding;
- dialogue.

Use focused passes and synthesize them through an editor.

---

# 2. Operating Modes

## FAST SCENE MODE

Use for:
- one scene;
- dialogue;
- short continuation;
- description;
- minor rewrite.

Pipeline:

```text
intent
→ scene question pass
→ scene contract
→ show/tell + POV-distance choices
→ character actions
→ draft
→ craft audit
→ targeted critic
→ output
```

## SHORT STORY MODE

Pipeline:

```text
intent
→ candidate population
→ candidate selection
→ Story Genome
→ arc/revelation/affect plan
→ draft
→ critic council
→ revision
→ continuity check
```

## LONG-FORM MODE

Use for:
- novels;
- novellas;
- serial fiction;
- multi-chapter stories;
- long screen narratives.

Pipeline:

```text
intent
→ Story Genome
→ candidate population
→ rough outline
→ character/world initialization
→ memory initialization
→ dynamic detailed outlining
→ scene loop
→ state extraction
→ critic loop
→ outline refresh
→ continuity audit
```

## CRITIC MODE

Analyze without rewriting unless requested.

## RESEARCH-GROUNDED MODE

When the story depends on factual research:
- retrieve sources;
- distinguish fact from invention;
- record constraints;
- do not let factual research dictate artistic decisions that are not factual requirements.

---

## DRAFT STARTER — pre-drafting interview layer (added 2026-09-15)

Sits before Intent Lock. Triggered by "Start Draft" or an equivalent loose seed ("Let's make a story about...", "I have a story idea," a character without a plot, a theme without a story). Converts the seed into a compact Draft Brief through a short collaborative interview (default: 3–5 questions per round, emotional core first, no more than two rounds), then hands the brief to Intent Lock below. Skip it entirely when the user is already asking for prose from a defined scene, explicitly wants to skip planning, or a Draft Brief already exists.

Full behavior contract, question banks, the Draft Brief schema, worked examples, and behavior checks: **`packs/draft-starter.md`**.

## ORIGIN FORGE — how a person became the identity the story meets (added 2026-09-15)

Sits after Draft Starter, still before Intent Lock, when the project is specifically about a transformation into a hero/villain/antihero/fallen-hero/legacy identity. Trigger: "Start Origin" (also: "Write a villain origin," a seed that already implies a before/after). Tracks a flexible spine — Before Self → Disruption → Responsibility → Meaning Crisis → Coping → Belief/Code → Second Test → Chosen Crossing → Transformation → Identity Claim → Aftermath → Story Launch — and separates actual/perceived/institutional responsibility for disastrous events. Includes a dedicated military/moral-conflict module. Hard guardrail: never use trauma or mental illness as a lazy causal explanation for villainy — write harmful behavior through concrete choices, incentives, and beliefs instead.

Full behavior contract, origin types, belief engines, the military module, question bank, the Origin Brief schema, and a worked example: **`packs/origin-forge.md`**. Downstream, when the origin needs comic-book pacing: `packs/comic-panel-writer.md` (§41, near the prose rules).

## TRAGIC ANIME STORY ENGINE — dark-action / tragic-fantasy craft (added 2026-09-15)

Sits after Origin Forge (when relevant), still before Intent Lock, for tragic battle fantasy, dark shonen/seinen-adjacent action, supernatural teams, military fantasy, apocalyptic stories, ideological rivalries, or any story where victories should create new losses. Triggers: "Start Tragic Story," "Dark Anime Mode," "Build a tragic arc," "Make this more emotionally devastating," "Build a consequential character death," "Build the reveal chain," "Pressure-test this cast." Core equation: `VALUED THING + PRESSURE + CHOICE + COST + RESIDUE = TRAGEDY`. **Not a kill-characters button** — the point is that loss changes the story, not that loss happens.

Full behavior contract (tragedy equation, cruel conditions, Hope Reserve, perspective reversal, reveal architecture, the Death Necessity Test, tragedy variety, power-under-pressure, escalation axes, ensemble pressure, ideological conflict, foreshadowing, endgame convergence), schemas, and behavior checks: **`packs/tragic-anime-engine.md`**. Nine secondary reference lenses (Madoka, Devilman Crybaby, Edgerunners, 86, To Your Eternity, Fate/Zero, Made in Abyss, Violet Evergarden, Chainsaw Man): **`packs/tragic-anime-lenses.md`**. Downstream: `packs/comic-panel-writer.md` for visual pacing of tragedy beats.

---

# 3. Intent Lock

Create a compact project contract before major generation.

```yaml
intent_lock:
  format:
  genre:
  subgenre:
  audience:
  content_rating:
  approximate_length:
  tone:
  pov:
  tense:
  canon_sources: []
  mandatory_elements: []
  forbidden_elements: []
  thematic_questions: []
  stylistic_constraints: []
  prose_distance: wide|medium|close|immersed|variable
  show_tell_preference: dramatized|balanced|compressed|voice-led
  dialogue_directness: direct|mixed|subtext-heavy
  exposition_tolerance: low|medium|high
  scene_pacing: compressed|balanced|lingering|variable
  experimental_level: low|medium|high
  ending_constraints:
  user_priorities: []
```

Do not repeatedly ask the user for details that can reasonably remain open.

Ask only when an unresolved choice would substantially change the work.

---

# 4. Story Genome

The Story Genome stores the identity of the story.

```yaml
story_genome:
  premise:
  dramatic_question:
  central_desire:
  central_pressure:
  central_unknown:
  central_contradiction:
  protagonist:
  major_relationships: []
  important_world_rules: []
  thematic_questions: []
  emotional_destination:
  reader_contract:
  ending_contract:
  motifs: []
  structural_permissions: []
  anti_goals: []
```

`anti_goals` are outcomes the writer should avoid, such as:

```yaml
anti_goals:
  - do not turn the conflict into a simple good-vs-evil morality play
  - do not resolve the romance through a last-minute misunderstanding
  - do not reveal the monster's complete origin
```

---

# 5. Divergent Creative Search

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

# 6. Creative Utility Selection

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

# 7. Associative Creativity Search

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

# 8. Fine-Grained Novelty Profile

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

# 9. Discourse Diversity Check

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

# 10. Character Architecture

Major characters are stateful narrative agents.

## 10.1 Stable Persona

```yaml
persona:
  name:
  role:
  physical_description:
  personality:
  values: []
  deep_desires: []
  fears: []
  history: []
  competencies: []
  abilities: []
  limitations: []
  relationships: {}
  worldview:
  moral_boundaries: []
  recurring_contradictions: []
  habitual_defenses: []
```

## 10.2 Developing State

```yaml
developing_state:
  current_goals: []
  beliefs: []
  false_beliefs: []
  relationship_states: {}
  unresolved_grudges: []
  loyalties: []
  secrets: []
  hopes: []
  psychological_trajectory:
```

## 10.3 Immediate Scene State

```yaml
scene_state:
  location:
  physical_condition:
  emotional_state:
  current_goal:
  current_fear:
  current_assumption:
  known_information: []
  unknown_information: []
  concealed_information: []
  perceived_options: []
```

---

# 11. Character Action Engine

Before an important scene is drafted, participating major characters propose actions.

For each character, provide only information that character should have:

- persona;
- relevant relationships;
- current story goal;
- immediate scene state;
- recent history;
- relevant world state.

Ask for a concrete intended action.

Then run an Action Critic.

```yaml
action_critic:
  relevant_to_scene:
  specific:
  consistent_with_character:
  plausible:
  consistent_with_knowledge:
  advances_or_complicates_goal:
  non_repetitive:
  consequence_potential:
```

Reject or regenerate actions that are:
- vague;
- implausible;
- out of character;
- based on knowledge the character does not possess;
- repetitive;
- purely designed to satisfy the outline.

After several character actions are accepted, the Narrator chooses which actions actually enter the scene.

Not every proposed action must occur.

This lets plot emerge from competing agency.

---

# 12. Goal Sequencing and Stagnation Detection

Long stories can stall around an unresolved goal.

Track the current story-level and local goals.

```yaml
goal:
  description:
  initiated_at:
  completion_conditions: []
  active_characters: []
  blockers: []
  progress:
  repetition_warning:
```

If several consecutive scenes:
- repeat the same attempt;
- produce no new information;
- do not change relationships;
- do not alter risk;
- do not reduce or expand available options;

the goal may be stalled.

Respond by:
- completing it;
- reframing it;
- replacing it;
- introducing a consequential new domain of conflict.

Do not use fixed step counts as universal rules.
Use stagnation evidence.

---

# 13. Dynamic Hierarchical Outline

Do not fully over-specify a novel before writing it.

Maintain two planning levels:

```text
ROUGH OUTLINE
  large movements and destination points

DYNAMIC DETAILED OUTLINE
  near-future chapters/scenes generated just before they are needed
```

Structure:

```text
Story
└── major movement
    └── sequence
        └── chapter
            └── scene
                └── beat
```

The rough outline preserves overall shape.
The detailed outline adapts to what the story has actually become.

---

# 14. Rough Outline

The rough outline should contain:

```yaml
rough_outline_node:
  function:
  characters:
  setting:
  major_change:
  conflict:
  revelation:
  emotional_direction:
  required_setup:
  future_dependency:
```

Do not require one universal act structure.

Possible organizing systems include:
- acts;
- movements;
- phases;
- investigations;
- seasons;
- locations;
- relationship stages;
- viewpoint cycles;
- missions;
- ritual stages.

Use the structure appropriate to the project.

---

# 15. Detailed Outline Expansion

Expand outline nodes recursively when more detail is needed.

For each parent node:

1. Generate 2-4 possible child-event sets.
2. Reject causal contradictions.
3. Reject redundancy.
4. Select the strongest set.
5. assign:
   - setting;
   - active characters;
   - information changes;
   - relationship changes;
   - relevant memory;
   - next-node transition.

Prefer breadth-first expansion when constructing an initial detailed region, then just-in-time expansion during drafting.

Do not pre-expand the entire novel unless needed.

---

# 16. Structured Drafting Context

When drafting a scene, do not dump the entire story into context blindly.

Retrieve a compact packet:

```yaml
draft_context:
  current_scene_contract:
  current_outline_node:
  next_outline_node:
  immediate_previous_scene:
  near_past_summary:
  far_past_relevant_facts:
  active_character_states:
  relationship_states:
  current_setting:
  relevant_world_rules:
  relevant_open_loops:
  continuity_warnings:
```

Including the next outline node can help transitions, but the writer must not prematurely execute future events.

---

# 17. Plan Refresh

After a meaningful scene or chapter:

Ask:

- Did any character choose an unexpected path?
- Did a relationship become more important?
- Did a revelation arrive earlier than planned?
- Did a planned twist become obvious?
- Did a secondary character become causally important?
- Did the world state change?
- Did the story discover a stronger thematic question?
- Is the planned ending still credible?

Update the detailed outline.

Update the rough outline only when the larger direction genuinely changes.

---

# 18. Memory Architecture

Long-form generation requires explicit memory.

Use two complementary layers.

## 18.1 Narrative State Store

```yaml
memory:
  canon_facts: []
  character_states: {}
  relationship_states: {}
  world_state: {}
  timeline: []
  open_loops: []
  motifs: []
  objects: {}
  injuries_and_conditions: {}
  promises_and_debts: []
  unresolved_information: []
```

## 18.2 Temporal Event Graph

Represent important changes as time-indexed statements.

```yaml
event_fact:
  subject:
  relation_or_action:
  object_or_value:
  time_index:
  source_scene:
```

Examples:

```text
(Lena, trusts, Marcus, chapter_2)
(Lena, distrusts, Marcus, chapter_7)
(key, located_at, basement_safe, scene_14)
(Marcus, knows, bridge_is_rigged, scene_21)
```

The graph does not replace prose memory.
It enables targeted retrieval and contradiction detection.

---

# 19. Memory Retrieval

Before planning or writing:

1. extract entities from the current query/scene;
2. retrieve relevant memory facts;
3. rank by semantic relevance and recency;
4. keep only the useful subset;
5. surface temporal changes when important.

Avoid flooding the writer with every stored fact.

For a scene involving Lena and Marcus, retrieve:
- their relationship history;
- current trust state;
- promises;
- recent conflict;
- knowledge asymmetries;
- relevant shared objects/events.

---

# 20. Consistency Taxonomy

Check long stories across five major categories.

## Timeline and Plot Logic

- absolute-time contradiction;
- duration contradiction;
- simultaneity contradiction;
- causeless effect;
- causal logic violation;
- abandoned plot element.

## Characterization

- memory contradiction;
- knowledge contradiction;
- skill fluctuation;
- forgotten ability.

## Worldbuilding

- core-rule violation;
- social-norm violation;
- geographical contradiction.

## Factual and Detail Consistency

- appearance mismatch;
- nomenclature confusion;
- quantitative mismatch.

## Narrative and Style

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

# 21. Evidence-Based Continuity Checker

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

# 22. Reader-State Model

Captivation is a changing state, not a constant maximum.

Track:

```yaml
reader_state:
  curiosity:
  suspense:
  emotional_intensity:
  uncertainty:
  empathy:
  attachment:
  information_debt:
  narrative_momentum:
  cognitive_load:
```

Use descriptive labels or rough 0-100 planning estimates.

Do not pin everything high.

A useful pattern may be:

```text
curiosity rises
→ answer
→ quiet intimacy
→ new implication
→ dread
→ false relief
→ social pressure
→ revelation
→ recontextualization
→ aftermath
```

Variation is the point.

---

# 23. Affect Curve

Track at least:

```text
valence: negative ↔ positive
arousal: calm ↔ intense
control: powerless ↔ powerful
```

Avoid automatic positivity drift.

After hardship, a character does not need to:
- learn a lesson;
- forgive;
- become hopeful;
- articulate growth.

Emotional trajectories may end:
- conflicted;
- numb;
- energized;
- angry;
- accepting;
- obsessed;
- uncertain;
- unchanged.

---

# 24. Turning-Point Planning

For longer stories, identify meso-level turns.

A turning point should alter at least one:

- goal;
- interpretation;
- relationship;
- available option;
- power balance;
- stakes;
- identity;
- location/domain;
- reader model of the story.

Do not confuse:
- "a dramatic event happened"
with
- "the narrative changed direction."

---

# 25. Suspense Engine

Suspense requires:

1. a target outcome the reader hopes for or fears;
2. emotional investment;
3. uncertainty;
4. a perceived solution space;
5. progressive reduction in the number or quality of successful paths.

Represent a suspense thread as:

```yaml
suspense_thread:
  desired_outcome:
  feared_outcome:
  protagonist_goal:
  reader_stakes:
  feasible_paths: []
  blocked_paths: []
  deadline_or_pressure:
  reader_knowledge:
  character_knowledge:
```

---

# 26. Adversarial Suspense Planning

For a suspense-bearing sequence:

### Step 1: Protagonist option search

Generate the most rational available actions.

### Step 2: Failure pressure

For each action, generate a credible condition that reduces or blocks its success.

### Step 3: Update option space

The next action must account for previous failures.

### Step 4: Decrease apparent success probability

Later actions may become:
- riskier;
- more costly;
- less certain;
- morally difficult;
- dependent on unreliable allies.

### Step 5: Resolution

Do not repeat failures forever.
Allow:
- success;
- partial success;
- costly success;
- failure;
- reframing of the goal.

The final result should follow the project's intended ending logic.

---

# 27. Knowledge Disparity

Track three knowledge sets:

```yaml
knowledge:
  reader_knows:
  protagonist_knows:
  other_character_knows:
```

Suspense can emerge when the reader knows a danger the protagonist does not.

Surprise can emerge when a character or narrator knows something the reader does not.

Mystery can emerge when neither knows enough.

Use these asymmetries deliberately.

---

# 28. Foreshadowing vs Warning

Before a planned failure or revelation, decide whether clues should:

- be invisible until retrospect;
- create unease;
- let the reader predict danger;
- misdirect;
- openly reveal danger while withholding the character's awareness.

Do not foreshadow every event in the same way.

---

# 29. Information Architecture

For important information:

```yaml
information_item:
  truth:
  who_knows: []
  who_believes_false_version: []
  reader_state:
  first_hint:
  reinforcement:
  partial_reveal:
  full_reveal:
  recontextualizes: []
  consequences: []
```

Operations:

- reveal;
- conceal;
- distort;
- misinterpret;
- contradict;
- confirm;
- recontextualize.

A revelation is stronger when it alters meaning, not only knowledge.

---

# 30. Revelation Test

Before accepting a twist:

- Was it prepared?
- Is retrospective evidence available?
- Does it affect decisions?
- Does it change relationships?
- Does it change the reader's model of earlier events?
- Does it create consequences?
- Is it specific to these characters?
- Would the story still function identically without it?

If yes to the last question, the twist may be decorative.

---

# 31. Psychological Depth Scale

Evaluate stories using five distinct reader-centered dimensions.

## Emotion Provocation

Can the story produce meaningful emotional response?

Do not maximize emotion words.
Over-saturation may numb the reader.

## Empathy

Can the reader cognitively or emotionally inhabit the character's experience?

Empathy does not require likability.

## Engagement

Does the story sustain attention through:
- pacing;
- narrative flow;
- curiosity;
- suspense;
- investment?

## Authenticity

Do behavior, dialogue, relationships, and emotional consequences feel genuinely lived rather than mechanically written?

## Narrative Complexity

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

# 32. Psychological Depth Critic Council

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

# 33. StoryScope Anti-Default Audit

AI fiction exhibits recurring structural tendencies.

Audit for these patterns:

## Thematic Over-Determination

- theme stated too explicitly;
- narrator explains the lesson;
- moral/philosophical issue foregrounded too neatly;
- dialogue becomes thematic debate;
- subplots all reinforce one central theme too perfectly.

## Embodied/Sensory Overperformance

- every emotion becomes chest tightening, breath catching, pulse racing;
- setting mirrors mood automatically;
- sensory density remains high everywhere;
- smell/touch/body metaphors are used reflexively.

## Structural Streamlining

- one clean causal chain;
- no meaningful subplots;
- protagonist choice resolves everything;
- resolution defaults to internal understanding;
- character introductions rely on external description;
- every location and spatial relation is over-grounded.

## Reduced Human-Like Range

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

# 34. Structural Rarity Pass

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

---

# 35. Macro Creativity Critics

Before drafting a long story, run three plan-level critics:

## Critic A: Original Theme / Plot / Setting

Search for:
- conventional central material;
- unexplored cultural/social frames;
- more specific settings;
- more consequential premise variations;
- authenticity.

## Critic B: Unusual Structure

Search for:
- alternative ordering;
- viewpoint architecture;
- framing devices;
- nonlinear organization;
- embedded narratives;
- asymmetric acts/movements;
- structure generated by character/world logic.

## Critic C: Ending

Search for:
- predictable closure;
- unnecessary reconciliation;
- endings that merely state the theme;
- endings that do not exploit prior setup;
- stronger consequence structures;
- alternative closure families.

Each critic proposes one to three high-impact changes.

---

# 36. Critic Leader

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

# 37. Multi-Round Plan Refinement

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

# 38. Micro Creativity Critics

At prose level, separate two kinds of expressive criticism.

## Image Critic

Checks:
- perceptual specificity;
- internal imagery;
- visual/auditory/tactile usefulness;
- concrete detail;
- whether sensory detail actually serves the scene.

Important:
StoryScope warns against reflexive sensory over-description.
The Image Critic must never equate "more sensory detail" with "better."

## Voice Critic

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

# 39. Scene Contract

```yaml
scene_contract:
  pov_character:
  location:
  time:
  current_story_goal:
  scene_goal:
  opposition:
  hidden_pressure:
  active_characters:
  reader_question:
  knowledge_asymmetry:
  information_change:
  relationship_change:
  emotional_turn:
  state_change:
  next_scene_pressure:

  # v0.4 craft layer
  scene_entry_pressure:
  scene_exit_turn:
  hidden_sentence:
  surface_topic:
  concrete_anchor_detail:
  psychic_distance_start:
  psychic_distance_target:
  show_moments: []
  tell_summary_moments: []
  exposition_needed_now: []
  exposition_deferred: []
  setup_items: []
  payoff_items: []
  silence_or_omission:
  continuity_risks: []
```

A scene should usually change at least one:
- knowledge;
- relationship;
- risk;
- power;
- desire;
- interpretation;
- available action;
- commitment.

---

# 40. Dialogue Engine

For significant dialogue:

```yaml
dialogue_state:
  speaker_goal:
  listener_goal:
  shared_topic:
  actual_conflict:
  speaker_hidden_intent:
  listener_hidden_intent:
  hidden_sentence_each_cannot_say:
  current_tactic:
  tactic_shift_trigger:
  information_asymmetry:
  status_difference:
  social_risk:
  relationship_history:
  likely_deflection:
  meaningful_silence:
  action_beat_function:
  exposition_risk:
  voice_difference:
```

Dialogue functions may include:

- negotiation;
- evasion;
- intimacy;
- dominance;
- testing;
- confession;
- bonding;
- performance;
- camouflage;
- threat;
- humor;
- worldbuilding;
- plot movement.

Do not make characters answer every question directly.

Do not make all dialogue equally witty.

---

# 41. Prose Generation Rules

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

See the v0.4 craft modules below.

---

## COMIC PANEL WRITER — comic-book visual logic (added 2026-09-15)

An alternate output register for §41's prose rules, not a replacement for them. Triggers: "Comic Mode," "Panel this," "Write as a comic," "Comic script." Default output is prose with comic-book visual logic (iconic beats, compressed transitions, heightened dialogue, issue-like scene endings) — full page/panel production scripting only when actually asked for.

Full behavior contract, panel/page/lettering frameworks, output-mode menu (Comic Narrative / Page Map / Panel Breakdown / Full Script / Lettering Audit / Visual Pacing Audit), schemas, and production checks: **`packs/comic-panel-writer.md`**. Bridges with `packs/origin-forge.md` (§3, near Intent Lock) when an origin is being developed for comic pacing.

---

# 42. Dynamic Character Development

After a character participates in a consequential scene, update their developing state.

Do not rewrite their stable persona casually.

Example:

```text
stable:
Marcus values loyalty.

developing:
Marcus now believes Lena may expose his brother.

immediate:
Marcus intends to lie during dinner.

result:
After Lena protects him unexpectedly, Marcus's suspicion decreases but shame increases.
```

Character development should be accumulated state, not trait replacement.

---

# 43. Relationship State

```yaml
relationship:
  trust:
  affection:
  dependence:
  fear:
  attraction:
  resentment:
  obligation:
  power_balance:
  current_misunderstanding:
  shared_secret:
  unspoken_need:
  recent_change:
```

Relationship trajectories must persist across scenes.

---

# 44. Ending Search

When the ending is not fixed, generate multiple ending families.

Examples:

- external victory / internal failure;
- internal resolution / external loss;
- costly victory;
- irreversible misunderstanding;
- revelation without reconciliation;
- ambiguous relationship;
- open causal mystery / emotional closure;
- tragic closure;
- circular return with changed meaning;
- temporal jump;
- deliberate anti-climax;
- transformation;
- refusal to transform.

Test:

- Is it caused by prior choices?
- Does it satisfy the story contract?
- Does it preserve consequences?
- Does it over-explain?
- Does it resolve relationships merely because the story is ending?
- Is it predictably bleak solely to appear mature?
- Could a prior scene be reinterpreted because of this ending?

---

# 45. Long-Form Scene Loop

```text
A. retrieve relevant memory
B. inspect current rough/detailed outline
C. generate/refresh scene contract
D. character agents propose actions
E. action critic accepts/rejects
F. narrator selects useful actions
G. draft scene
H. extract new state/events
I. update temporal event graph
J. run targeted critics
K. revise selectively
L. run continuity check
M. update detailed outline
N. continue
```

---

# 46. Critic Scheduling

Do not run every critic after every paragraph.

Suggested cadence:

## Every scene
- character/action check;
- local continuity;
- scene purpose.

## Every chapter
- engagement;
- dialogue/prose where needed;
- open loops;
- character/relationship state.

## Every major movement
- StoryScope audit;
- originality/discourse audit;
- psychological-depth profile;
- suspense/affect curve;
- macro continuity.

## Before ending
- ending critic;
- open-loop audit;
- revelation setup audit;
- thematic over-explanation audit.

---

# 47. Evaluation Profile

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

---

# 48. Automatic Judge Warning

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

# 49. Human-in-the-Loop Checkpoints

Offer user choice at meaningful creative forks, not constantly.

Good checkpoints:
- premise family;
- protagonist interpretation;
- ending family;
- major canon change;
- extreme structural experiment;
- irreversible relationship direction.

Do not interrupt after every scene unless requested.

---

# 50. Research-Grounded Generation vs Research-Driven Formula

The research in this skill provides mechanisms, not a universal aesthetic.

The writer must not become a machine that inserts:

```text
one flashback
+ one morally gray choice
+ one subplot
+ one recontextualizing twist
= "human story"
```

That would simply create a new template.

Use research to widen the option space and catch defaults.

---



---

# 55. Theory-of-Mind Character Model

A character must not reason from the author's omniscient context.

Maintain a separate mental-state model for every major character.

```yaml
mental_state:
  character:
  observed_facts: []
  believed_facts: []
  false_beliefs: []
  uncertain_beliefs: []
  desires: []
  intentions: []
  fears: []
  suspicions: []
  private_memories: []
  beliefs_about_others: {}
  beliefs_about_others_beliefs: {}
```

The last field is optional and should be used only when second-order social reasoning matters.

Examples:

```text
Lena knows the key is missing.
Lena believes Marcus took it.
Marcus knows Eli took it.
Marcus believes Lena suspects him.
Eli believes nobody noticed the key is gone.
```

Those are four different narrative facts.

Do not collapse them into:

```text
Everyone knows Eli took the key.
```

---

# 56. Perspective Filter

Before generating a major character's:

- action;
- dialogue;
- private thought;
- inference;
- plan;

filter the story context to information that character could actually possess.

Use a two-stage procedure:

```text
STAGE 1 — PERSPECTIVE FILTER
Which events, facts, conversations, objects, and behaviors has this character perceived
or learned about?

STAGE 2 — MENTAL-STATE INFERENCE
Given only that filtered context, what does the character believe, want, fear, intend,
suspect, or misunderstand?
```

This prevents accidental omniscience and improves Theory-of-Mind reasoning.

A character may infer something that is not objectively true.

Keep separate:

```text
world truth
character observation
character interpretation
character belief
character intention
```

---

# 57. Belief–Desire–Intention Loop

For socially complex scenes, model each major character as:

```yaml
BDI:
  belief:
  desire:
  intention:
```

Then update dynamically:

```text
observation
→ belief update
→ desire pressure
→ intention
→ action
→ social consequence
→ new observation
```

Do not force beliefs to update instantly when evidence appears.

Characters may:

- rationalize;
- deny;
- misinterpret;
- cling to prior beliefs;
- update partially;
- distrust the evidence;
- change intention without changing belief.

---

# 58. Second-Order Social Reasoning

Use when scenes depend on manipulation, romance, distrust, negotiation, embarrassment,
politics, deception, or rivalry.

Model statements such as:

```text
A thinks B is angry.
A thinks B believes A lied.
A wants B to think A is calm.
B knows A is pretending to be calm.
```

Do not recurse infinitely.

Default maximum:

```text
belief about another person's belief
```

Use deeper recursion only when it clearly matters.

---

# 59. Reader Situation Model

Readers build an internal model of story events.

Track each important event across:

```yaml
event_index:
  time:
  space:
  active_entities: []
  causality:
  intentionality:
```

Optional additions:

```yaml
  emotional_state:
  object_state:
  social_state:
```

The core five dimensions are:

- time;
- space;
- protagonist/entity;
- causality;
- intentionality/goal.

When a new event sharply changes several dimensions at once, the reader must rebuild part
of the mental model.

Use this deliberately.

---

# 60. Situation-Model Continuity

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

---

# 61. Curiosity Engine

Curiosity differs from suspense and surprise.

Curiosity is strongest when the reader recognizes a meaningful information gap.

Represent a curiosity thread as:

```yaml
curiosity_thread:
  question:
  why_reader_cares:
  known_information: []
  missing_information:
  competing_hypotheses: []
  perceived_solvability:
  gap_width:
  clue_schedule: []
  partial_answers: []
  payoff:
```

The reader must know that something is missing.

Examples:

```text
Why does the locked room smell like seawater?
Why has Marcus never entered his own basement?
Who keeps moving the family photographs?
Why does everyone remember the accident differently?
```

---

# 62. Information-Gap Calibration

Curiosity can fail in two opposite directions.

## Gap too small

The answer is obvious.

Result:
- low curiosity;
- reader predicts payoff early.

## Gap too large

The reader lacks enough structure to form hypotheses.

Result:
- confusion;
- indifference;
- random-feeling mystery.

Aim for a gap where the reader can:

- notice the missing information;
- understand why it matters;
- generate more than one plausible explanation;
- believe an answer is obtainable.

Novelty, ambiguity, incongruity, complexity, and uncertainty may trigger curiosity, but
comprehensibility must remain high enough for the reader to engage.

---

# 63. Curiosity Update Loop

For active curiosity threads:

```text
open question
→ clue
→ hypothesis formation
→ complication
→ partial answer
→ larger or transformed question
→ payoff
```

Do not preserve curiosity by simply withholding everything.

Progress is necessary.

A useful clue should alter at least one hypothesis.

---

# 64. Curiosity vs Suspense vs Surprise

Use the correct narrative tension mechanism.

```text
CURIOSITY
Reader recognizes missing information.
Primary question: "What happened / why is this true?"

SUSPENSE
Reader anticipates a consequential future outcome under uncertainty.
Primary question: "What will happen?"

SURPRISE
Reader encounters an outcome/revelation that violates expectation but becomes coherent
in retrospect.
Primary reaction: "I did not expect that, but now it makes sense."
```

These mechanisms can be chained:

```text
curiosity → suspense → surprise → recontextualized curiosity
```

Example:

```text
Curiosity: Why is the train arriving empty every night?
Suspense: Will Maya board it before the station closes?
Surprise: The train is returning objects from a future disaster, not passengers.
New curiosity: Why is Maya's own coat inside?
```

---

# 65. Narrative Surprise Engine

Evaluate significant twists and endings with six dimensions:

```yaml
surprise_profile:
  initiatoriness:
  immutability_violation:
  predictability:
  post_dictability:
  importance:
  valence:
```

Definitions:

## Initiatoriness

Does the reveal provide a causal antecedent that explains a previously unexplained event?

## Immutability Violation

Does the twist contradict a fundamental rule or assumed invariant of the story world?

Use cautiously. A twist can be surprising without breaking an invariant.

## Predictability

How easily could a typical attentive reader foresee the ending?

For many surprise-bearing stories, avoid both extremes:

```text
completely obvious
and
impossible to infer because required information never existed
```

## Post-Dictability

After the reveal, can the reader reconstruct why prior events occurred?

High post-dictability means the ending makes earlier material more coherent.

## Importance

Does the reveal materially affect the protagonist, conflict, relationships, or story meaning?

## Valence

Is the outcome positive or negative for the protagonist?

Do not use negative valence mechanically.
It is a descriptive dimension, not a mandate for bleakness.

---

# 66. Surprise Construction Procedure

For an intended twist:

```text
1. Identify the surprising event/revelation.
2. Identify the hidden initiating cause.
3. Seed evidence produced by that cause.
4. Hide or misinterpret the cause itself.
5. Maintain at least two plausible reader models.
6. Avoid making the intended resolution the dominant obvious answer.
7. Reveal the initiating cause.
8. Re-check every relevant prior event.
9. Remove contradictions created only to protect the twist.
10. Preserve consequences after the reveal.
```

Prefer:

```text
unexpected + retrospectively coherent
```

over:

```text
unexpected because the writer invented new information at the end.
```

---

# 67. Surprise Red-Team

Before accepting a twist, attack it.

Ask:

```text
Could a reader predict this immediately?
Does the reveal depend on facts introduced only during the reveal?
Does it contradict an established world rule?
Does it require a character to behave irrationally only to hide information?
Would a second reading reveal fair evidence?
Does the reveal explain earlier oddities?
Does it create a more interesting story after the reveal?
Is the twist just a familiar trope with different nouns?
```

Reject fake surprise.

---

# 68. Surprise Research Caution

Research on mystery endings found reader preference for surprise was associated with:

- stronger initiatory causal explanation;
- stronger post-dictability;
- lower predictability;
- more negative valence.

Do not convert this into:

```text
good twist = negative ending
```

The evaluated sample was restricted to mystery endings, and surprise is audience-dependent.

Use these as diagnostics, not universal optimization targets.

---

# 69. Narrative Transportation

A captivating story should make it easy for the reader to mentally enter and remain in the
story world.

Narrative transportation involves:

- cognitive involvement;
- emotional involvement;
- mental imagery;
- attention focused on the narrative world.

Use transportation as a reader-state lens, not a prose-style command.

---

# 70. Transportation Prerequisites

Check:

```yaml
transportation:
  situation_model_clarity:
  character_connection:
  active_goal_or_question:
  emotional_access:
  concrete_world_cues:
  causal_legibility:
  attentional_friction:
```

High transportation does not require maximal description.

A few well-selected concrete cues can be more immersive than a paragraph cataloguing
every surface.

Major transportation breakers include:

- accidental POV omniscience;
- contradictory geography;
- unexplained causal jumps;
- character behavior that ignores established motivation;
- exposition inserted at moments of high action;
- excessive clarification;
- arbitrary tonal changes.

---

# 71. Transportation Audit

Ask after major chapters:

```text
Can the reader currently picture where the important action is occurring?
Do they know whose experience they are following?
Do they understand the active desire/problem?
Is there enough causal connection to predict possibilities?
Is the prose asking them to remember too many low-value facts?
Did the chapter interrupt an emotionally active moment with unnecessary explanation?
```

Do not turn the audit into "add more imagery."

---

# 72. Reader Effort Budget

Readers can enjoy complexity while still needing footholds.

Track:

```yaml
reader_effort:
  active_characters:
  active_mysteries:
  timeline_layers:
  viewpoint_switches:
  unexplained_terms:
  unresolved_causal_links:
  simultaneous_goals:
```

Complexity is not inherently bad.

When several dimensions become demanding simultaneously, provide an anchor:

- familiar location;
- stable viewpoint;
- concrete immediate goal;
- repeated object;
- relationship;
- clear causal consequence.

This allows structural complexity without fog.

---

# 73. Event-Level Flow, Not Token Predictability

Do not optimize story flow using simple sentence-level predictability alone.

Recent replication work on narrative sequentiality found that apparent effects can change
substantially under alternative measurement choices.

Treat flow as an event-level phenomenon involving:

- expectation;
- memory;
- causal continuity;
- goal continuity;
- rhythm;
- event segmentation.

Use token/sentence predictability metrics only as optional diagnostics.

---

# 74. Emergent Sandbox Mode

For ensemble, social, world-simulation, or highly character-driven fiction, optionally use a
hybrid bottom-up mode.

Initialize:

```yaml
sandbox:
  world_state:
  locations:
  institutions:
  resources:
  social_norms:
  active_characters:
  secrets:
  pressures:
```

Then simulate several short interaction rounds.

For each round:

```text
1. perspective-filter each character;
2. generate intention/action;
3. resolve compatible/conflicting actions;
4. update world state;
5. update beliefs and relationships;
6. log emergent events;
```

The Narrator then selects the events with the best narrative potential.

Do not transcribe the simulation literally.
Simulation generates material.
Narration shapes material.

---

# 75. Hybrid Top-Down / Bottom-Up Plotting

Use top-down planning for:

- thematic destination;
- major irreversible turns;
- ending contract;
- required mysteries;
- canon events.

Use bottom-up simulation for:

- interpersonal conflict;
- local consequences;
- secondary plots;
- alliance changes;
- rumors;
- unplanned complications;
- relationship development.

This reduces puppet-like characters without surrendering the entire story to simulation.

---

# 76. Social-State Propagation

For stories with communities, institutions, teams, families, courts, schools, workplaces,
politics, or factions, track social information separately.

```yaml
social_state:
  reputation:
  public_belief:
  private_belief:
  rumors: []
  alliances: []
  obligations: []
  taboos: []
  status:
  institutional_pressure:
```

Information may propagate imperfectly.

A rumor should not become universal truth in one scene unless the story establishes a
mechanism capable of spreading it that quickly.

---

# 77. Genre Module Status

Do not pretend every genre has been equally researched.

v0.3 has strong general mechanisms for:

- character psychology;
- suspense;
- curiosity;
- surprise;
- continuity;
- originality;
- long-form planning;
- narrative transportation.

Genre-specific modules for:

- horror/dread;
- romance/attachment;
- humor;
- erotic narrative;
- tragedy;
- mystery clue design;

remain targets for deeper dedicated research.

Use ordinary genre expertise in the meantime, but label it as general writing knowledge rather
than a research-derived module.

---

# 78. Benchmark Requirement

Do not keep expanding this skill indefinitely without testing whether complexity produces
better stories.

Evaluate against a direct-prompt baseline under matched conditions.

Minimum experiment:

```text
same model
same prompt
same approximate length
same content constraints
baseline prompting vs AI Writer skill
blinded comparison
```

Test both:

```text
quality
and
diversity across repeated generations
```

---

# 79. Primary Human Evaluation Questions

Prefer pairwise judgments.

For each baseline/skill pair ask:

```text
Which story would you rather continue reading?
Which story has more believable character behavior?
Which story is less predictable?
Which story has a more satisfying or meaningful surprise?
Which story creates stronger curiosity?
Which story feels more emotionally authentic?
Which story is more coherent?
Which story feels more distinctive?
Which story is better overall?
```

Randomize presentation order.

Do not tell evaluators which output used the skill.

---

# 80. Automatic Evaluation Role

Automatic evaluation may assist with:

- continuity contradictions;
- StoryScope-style feature analysis;
- plot/discourse similarity;
- lexical repetition;
- character-state consistency;
- length/control compliance.

It must not serve as the sole authority for:

- beauty;
- emotional impact;
- humor;
- originality;
- overall literary value.

---

# 81. v0.3 Runtime Summary

For substantial fiction:

```text
LOCK INTENT
↓
GENERATE DIVERSE STRUCTURAL CANDIDATES
↓
CHECK NOVELTY + DISCOURSE DIFFERENCE
↓
BUILD STORY GENOME
↓
INITIALIZE CHARACTERS, BDI, RELATIONSHIPS, WORLD STATE
↓
PLAN ROUGH ARC
↓
DESIGN CURIOSITY / SUSPENSE / SURPRISE THREADS
↓
EXPAND NEAR-FUTURE OUTLINE
↓
PERSPECTIVE-FILTER CHARACTERS
↓
PROPOSE ACTIONS
↓
DRAFT SCENE
↓
UPDATE EVENT INDEX + MEMORY + BELIEFS
↓
RUN TARGETED CRITICS
↓
CHECK TRANSPORTATION + CONTINUITY
↓
REFRESH OUTLINE
↓
REPEAT
```

The objective is not maximal machinery.
The objective is better fiction.


# 51. Research Basis

## StoryScope: Investigating Idiosyncrasies in AI Fiction
Russell et al., COLM 2026.

Integrated:
- narrative rather than merely stylistic AI signatures;
- 10-dimension narrative analysis;
- anti-default audit;
- thematic over-determination;
- temporal complexity;
- subplot/moral ambiguity signals;
- dimension-specific analysis.

## Creating Suspenseful Stories: Iterative Planning with Large Language Models
Xie & Riedl, EACL 2024.

Integrated:
- target outcome;
- dire failure state;
- feasible solution space;
- iterative protagonist action generation;
- adversarial blockage of actions;
- decreasing path quality;
- reader/character knowledge disparities;
- pre-failure clue options.

## Measuring Psychological Depth in Language Models
Harel-Canada et al., EMNLP 2024.

Integrated:
- emotion provocation;
- empathy;
- engagement;
- authenticity;
- narrative complexity;
- persona-specific evaluation;
- caution against simply increasing emotional intensity.

## Collective Critics for Creative Story Generation
Bae & Kim, EMNLP 2024.

Integrated:
- separate macro and micro creativity stages;
- multiple critics;
- leader/editor selection;
- multi-round refinement;
- original theme/setting;
- unusual structure;
- ending criticism;
- Image and Voice criticism.

## DOC: Improving Long Story Coherence With Detailed Outline Control
Yang et al., ACL 2023.

Integrated:
- hierarchical detailed outline;
- recursive expansion;
- candidate events;
- explicit setting/character association;
- dynamic character descriptions;
- structured drafting context;
- next-outline-node context.

## DOME: Dynamic Hierarchical Outlining with Memory-Enhancement
Wang et al., NAACL 2025.

Integrated:
- rough outline + just-in-time detailed outline;
- alternating plan/write process;
- temporal memory graph;
- targeted retrieval;
- semantic filtering;
- temporal conflict analysis.

## Lost in Stories: Consistency Bugs in Long Story Generation by LLMs
Li et al., Findings of ACL 2026.

Integrated:
- five consistency categories;
- 19 subtypes;
- evidence-grounded contradiction detection;
- category-specific checking.

## From Personas to Plot: Character-Grounded Multi-Agent Story Generation for Long-Form Narratives
Aluru et al., 2026.

Integrated:
- persona-grounded character agents;
- character-specific world-state retrieval;
- action proposals;
- action critic;
- narrator selection;
- story-goal sequencing;
- stagnation monitoring.

## GENIE: A Fine-Grained Measure for Novelty
Namuduri et al., 2026.

Integrated:
- task-specific novelty features;
- population-relative novelty;
- feature-level novelty profile;
- explainable originality analysis.

## QUDsim: Quantifying Discourse Similarities in LLM-Generated Text
Namuduri et al., COLM 2025.

Integrated:
- discourse structure abstraction;
- Questions Under Discussion;
- detection of structural repetition beneath surface differences.

## CREATE: Testing LLMs for Associative Creativity
Wadhwa et al., 2026.

Integrated:
- associative search;
- quality + distance thinking;
- candidate portfolios rather than one answer;
- specific and diverse conceptual bridges.

## NoveltyBench: Evaluating Creativity and Diversity in Language Models
Zhang et al., COLM 2025.

Integrated:
- recognition of mode collapse;
- diversity across repeated generations;
- candidate populations;
- in-context regeneration as a diversity tool.

## Avoidance Decoding for Diverse Multi-Branch Story Generation
Park et al., EMNLP 2025.

Integrated at prompt/workflow level:
- concept-level anti-similarity early;
- narrative-level anti-similarity later;
- branch diversity;
- rejection/regeneration of near-duplicate candidates.

Note:
The original paper modifies decoding logits. A prompt-only skill cannot reproduce that mechanism exactly.

## Are Large Language Models Capable of Generating Human-Level Narratives?
Tian et al., EMNLP 2024.

Integrated:
- story arcs;
- turning points;
- arousal/valence;
- tension;
- explicit discourse planning.

## The Limits of Automatic Evaluation of Creativity in Large Language Models
Tutone et al., 2026.

Integrated:
- automatic-judge caution;
- multidimensional evaluation;
- preservation of unpredictability;
- human judgment remains authoritative.

---



## Think Twice: Perspective-Taking Improves Large Language Models' Theory-of-Mind Capabilities
Wilf et al., ACL 2024.

Integrated:
- perspective-filtering before mental-state inference;
- separation between objective context and character-visible context;
- limited-knowledge character reasoning.

## Beyond Words: Integrating Theory of Mind into Conversational Agents for Human-Like Belief, Desire, and Intention Alignment
Jafari et al., Findings of ACL 2025.

Integrated:
- belief/desire/intention mental-state representation;
- pragmatic social reasoning;
- explicit mental-state alignment.

## The Construction of Situation Models in Narrative Comprehension: An Event-Indexing Model
Zwaan, Langston & Graesser, Psychological Science 1995.

Integrated:
- event representation over time, space, protagonist/entity, causality, and intentionality;
- situation-model continuity checks;
- reader reorientation after discontinuities.

## Narrative Transportation Research
Green & Brock tradition; van Laer et al.; Green & Appel; Thomas et al.

Integrated:
- cognitive, emotional, and imagery involvement as distinct from decorative prose;
- transportation prerequisites;
- reader effort and story-world continuity checks.

## A Theoretical Framework for Evaluating Narrative Surprise in Large Language Models
Bissell, Paulin & Piper, WNU 2025.

Integrated:
- initiatoriness;
- immutability violation;
- predictability;
- post-dictability;
- importance;
- valence;
- explicit distinction between surprise and curiosity;
- twist red-teaming.

## Curiosity / Information-Gap Literature
Berlyne tradition; Loewenstein information-gap theory; Shin & Kim review; recent curiosity reviews.

Integrated:
- recognizable information gaps;
- hypothesis formation;
- gap-width calibration;
- novelty/complexity/uncertainty balanced against comprehensibility.

## Fiction Flows: A Replication and Reinterpretation of Narrative Sequentiality
Piper, Hamilton, Zhou & Pianzola, ACL 2026.

Integrated:
- caution against treating sentence-level LM predictability as a stable measure of narrative flow;
- preference for event-level and situation-model analysis.

## BookWorld / StoryBox and related agent-society work
Ran et al., 2025; Chen, Pan & Li, 2025.

Integrated conservatively:
- optional emergent sandbox mode;
- social-state propagation;
- hybrid top-down/bottom-up story generation.


# 52. Known Translation Limits

Some research mechanisms cannot be implemented exactly in a portable text-only skill.

Examples:

### Avoidance Decoding
The research modifies model token logits directly.
This skill approximates it through:
- candidate generation;
- structural comparison;
- negative examples;
- regeneration;
- diversity-conditioned prompting.

### Embedding / classifier metrics
GENIE, QUDsim, StoryScope, and other systems may use embeddings, classifiers, or large evaluation corpora.
Without those tools, use structured qualitative approximations.

### Multi-model agent architectures
MAGNET and CritiCS may use distinct models/agents.
If only one model is available, simulate separated roles in independent calls/passes.

Do not claim exact reproduction when only an approximation is possible.

---

# 82. Legacy v0.3 Quality Gate (retained)

Before returning a substantial story/chapter, verify:

## Identity
Does this feel specific to this project?

## Agency
Did characters act according to their state and knowledge?

## Causality
Do consequences emerge from prior events?

## Structural diversity
Is the story using the highest-probability AI plot skeleton?

## Information
Is reader knowledge intentionally managed?

## Suspense
Where relevant, are successful paths becoming meaningfully constrained?

## Psychology
Does the story evoke empathy/authenticity without reducing psychology to introspection?

## Affect
Does emotional intensity vary?

## Revelation
Does important new information alter meaning or action?

## Continuity
Are chronology, knowledge, abilities, geography, facts, tone, and world rules consistent?

## Theme
Did the draft trust the reader enough?

## Ending
Did it close what should close and leave open what should remain open?

If multiple checks fail, revise the relevant layer, not merely the wording.

---

# 83. Legacy Compact Runtime Instruction (retained)

When context is limited, use this compressed rule:

> Treat fiction writing as a search-and-simulation problem before treating it as prose generation. Generate several structurally distinct possibilities, select for both quality and meaningful distance, model major characters as stateful agents with limited knowledge, maintain a dynamic hierarchical outline and explicit temporal memory, manage reader knowledge and emotional state deliberately, draft from scene contracts, and use specialized critics for psychology, originality, suspense, continuity, structure, and prose. Detect common AI narrative defaults without mechanically inverting them. Revise selectively, preserve useful ambiguity, and never optimize a story solely for an automated judge.
---

# 84. v0.4 Craft Layer

v0.3 concentrated heavily on:
- narrative architecture;
- character simulation;
- reader-state management;
- suspense;
- novelty;
- continuity;
- anti-default structure.

v0.4 adds a **page-level craft layer**.

The new layer asks:

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

# 85. Show–Tell Decision Engine

"Show, don't tell" is useful only when it is treated as a **control dial**, not a ban on summary.

## 85.1 Prefer showing when the reader should EXPERIENCE:

- a consequential choice;
- a relationship shift;
- a revelation;
- a first encounter;
- an irreversible action;
- a contradiction between words and behavior;
- a moment whose emotional interpretation should belong partly to the reader;
- a setting detail that reveals character;
- the exact behavior that makes a claim believable.

## 85.2 Prefer telling / summary when the reader only needs to KNOW:

- routine actions;
- connective travel;
- repeated behavior already established;
- low-priority time passage;
- unimportant logistics;
- background that would be tedious as full scene;
- information whose dramatization would steal emphasis from the real scene.

## 85.3 Show, then tell

Useful in speculative, technical, historical, or unfamiliar settings:

```text
reader experiences strange thing
→ curiosity forms
→ concise explanation answers only what is now necessary
```

This is usually stronger than explaining the rule before the reader has a reason to care.

## 85.4 Telling can carry voice

"Tell" does not mean "write neutrally."

Summary can reveal:
- attitude;
- irony;
- prejudice;
- compression;
- cultural assumptions;
- retrospective judgment.

## 85.5 Avoid body-language pantomime

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

## 85.6 Do not tell after a successful show

If action/dialogue/image already makes the meaning legible, resist immediately explaining it.

Use the **echo audit**:

```text
Did narration label what action just demonstrated?
Did internal thought repeat what dialogue just admitted?
Did metaphor restate the emotion a third time?
```

If yes, delete or transform at least one layer unless repetition is intentionally rhetorical.

---

# 86. Scene Entry / Exit Control

Use **enter late, leave early** as a test, not a commandment.

## Enter late

Before a scene starts, ask:

- What preparation can the reader infer?
- What is the first moment the character's desire meets pressure?
- Can five lines of arrival/setup disappear without confusion?
- Is the current opening only warming up?

Start as close to useful tension as the story allows.

## Leave early

After the scene's turn, ask:

- Has the decision/revelation/refusal already landed?
- Are the next paragraphs only explaining what the reader understood?
- Would a cut preserve more energy?

## Exceptions

Start earlier or linger longer when duration itself creates:
- dread;
- ritual;
- tenderness;
- awkwardness;
- exhaustion;
- comedy;
- realism;
- atmosphere;
- grief.

The problem is not slowness.

The problem is **unintentional dead time**.

## Ten-line cut test

In revision:
1. temporarily remove the first 5–10 lines;
2. see whether orientation survives;
3. temporarily remove the last 5–10 lines;
4. see whether the scene becomes more resonant.

Restore anything whose absence damages intended effect.

---

# 87. Scene Goal, Resistance, Change

A functional scene usually contains:

```text
DESIRE
→ ATTEMPT
→ RESISTANCE
→ ADAPTATION / CHOICE
→ CHANGE
```

Conflict does not require shouting, violence, or an antagonist.

Resistance can be:
- another person's goal;
- social etiquette;
- shame;
- lack of information;
- time;
- weather;
- physical limitation;
- institutional rules;
- memory;
- self-deception;
- incompatible loyalties.

## Scene diagnostic

Ask:

```yaml
scene_diagnostic:
  what_does_pov_character_want_now:
  why_now:
  what_is_their_plan:
  what_resists:
  what_will_it_cost:
  what_tactic_changes:
  what_new_information_arrives:
  what_choice_becomes_possible_or_impossible:
  what_is_different_at_exit:
  what_pressure_carries_forward:
```

If the answer to "what changes?" is **nothing**, classify the scene:

```text
atmosphere / character texture by design
or
candidate for compression / removal
```

Do not keep a scene merely because its prose is attractive.

---

# 88. Exposition and Backstory: Need-to-Know Routing

Backstory is not bad.
Exposition is not bad.
**Unmotivated information delivery** is the problem.

Use:

```text
CURRENT SCENE NEED
→ reader question
→ smallest useful answer
```

## Exposition questions

- Does the reader need this to understand the current action?
- Does the POV character have a reason to think about it now?
- Would withholding it create productive curiosity or only confusion?
- Can the information arrive through consequence rather than lecture?
- Can a strange fact be shown first and explained after?
- Does another character already know this, making the dialogue unnatural?
- Is the writer explaining because the scene itself failed to communicate?

## CIA / need-to-know principle

Treat world/background information as classified:
release it when it changes what the reader can understand, fear, predict, or interpret.

## Exposition forms

Choose among:
- concise narrator summary;
- contextual detail;
- action consequence;
- conflict-driven dialogue;
- document/artifact;
- flashback;
- memory;
- rumor;
- demonstration;
- later reveal.

Do not default to characters reciting shared history to each other.

---

# 89. Specificity Without Inventory

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

## Detail selection rule

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

## POV detail test

Ask:

> Would this character, in this emotional state, notice this detail before the others?

If no, either remove it or move to a more appropriate narrator distance.

---

# 90. POV and Psychic Distance Engine

POV is not only who narrates.
It is **how close the reader is allowed to stand to a consciousness**.

Use four practical distances:

```yaml
psychic_distance:
  wide:
    use_for: context, time compression, geography, transitions
  medium:
    use_for: observable action with selective interior access
  close:
    use_for: scene-level interpretation, desire, fear, judgment
  immersed:
    use_for: near-thought texture, fragmented perception, crisis
```

## Distance rules

- Choose a default range for the scene.
- Change distance intentionally.
- Avoid accidental head-hopping.
- Do not report information the POV character cannot know.
- Let description inherit the POV character's language and values.
- A close POV does not need constant "she saw / he noticed / she felt" filters unless the filtering itself matters.

## Zoom question

At any paragraph ask:

> Am I at the distance that gives this beat the strongest effect?

A death may need distance.
A tiny embarrassment may need extreme closeness.
Do not assume "closer" always means "better."

---

# 91. Dialogue and Subtext Engine

Dialogue should not be a transcript of real speech, nor an author briefing disguised as conversation.

For important exchanges define:

```yaml
subtext:
  surface_topic:
  real_topic:
  speaker_request_or_attack:
  thing_speaker_cannot_say:
  thing_listener_cannot_say:
  current_tactic:
  social_cost_of_directness:
  status_difference:
  lie_or_avoidance:
  action_that_contradicts_words:
```

## Useful tactics

Characters may:
- deflect;
- answer a different question;
- joke;
- over-agree;
- attack a safer topic;
- change subject;
- withhold;
- bargain;
- threaten indirectly;
- perform politeness;
- go silent;
- physically do what they verbally deny.

## On-the-nose test

If both characters repeatedly state:
- exactly what they feel;
- exactly what they want;
- why they feel it;
- what the relationship means;

the dialogue may be functioning as commentary rather than human interaction.

Directness is still valid when:
- crisis removes social masks;
- character is unusually blunt;
- confession is the scene's event;
- the genre/tone benefits from explicitness.

## Read-aloud pass

Read significant dialogue aloud.

Listen for:
- impossible sentence length;
- repeated formal syntax;
- lack of contractions where character would use them;
- every speaker sharing the same rhythm;
- exposition nobody would naturally say;
- cleverness exceeding the character.

---

# 92. Setup / Payoff Ledger

A setup is a promise.
A payoff is the later use, transformation, inversion, or consequence of that promise.

Track:

```yaml
setup_payoff:
  setup:
  first_appearance:
  apparent_function:
  true_function:
  camouflage:
  reader_attention_level:
  expected_payoff_window:
  payoff:
  payoff_type:
    - plot
    - emotional
    - relationship
    - thematic
    - comic
    - visual
    - reversal
  status: planted|developing|paid|intentionally_unpaid
```

## Good payoff

A strong payoff often feels:

```text
surprising now
+
obvious in retrospect
```

## Do not over-mechanize

Not every object must become a gun on the mantel.

Fiction needs:
- texture;
- accidents;
- unused possibilities;
- ordinary objects.

Track setups that create **reader expectation**, not every noun.

---

# 93. Stakes and Tension

Stakes do not have to mean:
- death;
- apocalypse;
- prison;
- world destruction.

The useful question is:

> What becomes painful, impossible, humiliating, irreversible, or costly for THIS character?

Use:

```text
DESIRE
+ UNCERTAINTY
+ CONSEQUENCE
+ CONSTRAINT
=
TENSION
```

## Scene stakes questions

- What does the character stand to lose now?
- What might they gain?
- What will action cost even if it works?
- What unintended consequence can follow?
- Does the reader know more or less about the danger than the character?
- Can the character simply walk away? If yes, why don't they?
- What commitment has made retreat harder?

Quiet scenes can carry high tension through:
- embarrassment;
- social exposure;
- withheld apology;
- attraction;
- moral compromise;
- waiting.

---

# 94. Description and Worldbuilding Through Use

Do not pause the story to inventory a world.

Reveal worldbuilding through:
- what characters use;
- what blocks them;
- what costs money/status/time;
- what is illegal or taboo;
- what breaks;
- what people misunderstand;
- what a character takes for granted;
- what a stranger notices.

## Worldbuilding audit

For every paragraph of lore:

```text
Does this alter current action or interpretation?
```

If no:
- defer;
- compress;
- cut;
- or make the information itself the subject of conflict.

Research belongs on the page only in the quantity the story can metabolize.

---

# 95. Pacing: Scene vs Summary

Pacing is not simply "fast" or "slow."

Control it through:

- dramatized time;
- summary compression;
- sentence length;
- paragraph size;
- dialogue density;
- information rate;
- question/reveal timing;
- action frequency;
- interiority;
- transition length.

## Slow down for:
- irreversible choices;
- revelation;
- intimacy;
- dread;
- sensory disorientation;
- first experiences.

## Speed up for:
- routine;
- travel;
- repeated attempts;
- unimportant aftermath;
- background chronology.

Do not dramatize every commute.
Do not summarize the scene the story has been waiting for.

---

# 96. Character Behavior Test

Before major character action ask:

```yaml
character_choice:
  current_goal:
  current_belief:
  known_information:
  mistaken_information:
  fear:
  desire:
  relationship_pressure:
  social_pressure:
  available_options:
  option_rejected_and_why:
  chosen_action:
  immediate_cost:
  future_consequence:
```

## Anti-puppet rule

If the only reason a character acts is:
> "because the plot needs the next event"

revise motivation, information, pressure, or event.

## Contradiction rule

Characters may behave inconsistently when the inconsistency is psychologically legible.

A character can:
- love and resent;
- believe and doubt;
- want safety and sabotage it;
- know better and still choose badly.

Consistency means **stateful plausibility**, not mechanical predictability.

---

# 97. Common Human / Novice Writer Mistake Audit

These are recurring problems reported by editors, teachers, and writing coaches.
They are not universal laws and are not empirical prevalence estimates.

Audit for:

## 1. Writer-knows, reader-doesn't confusion
The author can picture the scene, but necessary orientation never reached the page.

Fix:
- clarify time/place/speaker/action;
- do not solve confusion with a paragraph of unrelated exposition.

## 2. Generic language
"Beautiful," "angry," "old," "strange," "nice."

Fix:
- replace with one useful specific.

## 3. Inventory description
Head-to-toe character description or room catalog.

Fix:
- select details with narrative/POV function.

## 4. Exposition too early
The novel explains history before the reader has a present-tense reason to care.

Fix:
- delay, dramatize, or show-then-tell.

## 5. Dialogue as information dump
Characters explain facts both already know.

Fix:
- give them conflicting objectives; release information under pressure.

## 6. On-the-nose dialogue
Characters say their subtext aloud repeatedly.

Fix:
- define the hidden sentence and write around it.

## 7. Dialogue in a vacuum
Pages of speech with no bodies, objects, setting, or action.

Fix:
- anchor action beats selectively.

## 8. Everyone has the same voice
Same sentence length, vocabulary, wit, politeness, and metaphor system.

Fix:
- differentiate social history, education, rhythm, goals, and tactics.

## 9. Head-hopping
Interior access jumps minds without a deliberate POV system.

Fix:
- choose scene POV and psychic-distance boundaries.

## 10. Scene starts before it starts
Arrival, greetings, coffee, weather, setup.

Fix:
- test entering later.

## 11. Scene continues after it ends
Characters recap meaning after the turn.

Fix:
- test leaving earlier.

## 12. Nothing changes
A scene has atmosphere but no intentional function.

Fix:
- add change, classify as texture, compress, or cut.

## 13. Stakes are huge but impersonal
"The world will end," but the character has no specific emotional relationship to that outcome.

Fix:
- define what "the end of the world" means to their world.

## 14. Character acts for outline convenience
Motivation appears after the plot requires it.

Fix:
- rebuild desire/belief/pressure before action.

## 15. "Show don't tell" becomes cliché-body-language soup
Every feeling gets pulse, breath, jaw, stomach, chest.

Fix:
- choose character-specific evidence or use a direct label.

## 16. The writer explains after showing
Reader inference is immediately translated into a moral.

Fix:
- run echo audit.

## 17. Purple or modifier-heavy prose
Adjectives/adverbs decorate weak nouns/verbs.

Fix:
- test stronger noun/verb; keep modifiers that change meaning.

## 18. Research flex
Facts appear because the writer learned them, not because the story needs them.

Fix:
- need-to-know exposition.

## 19. Setup with no payoff
Attention is drawn to an object/question that disappears.

Fix:
- pay it, intentionally abandon it, or reduce emphasis.

## 20. Payoff with no setup
Solution/reveal arrives without enough prior possibility.

Fix:
- seed evidence or capability earlier.

## 21. Flat emotional intensity
Every paragraph is maximum dread, grief, wit, beauty, or violence.

Fix:
- create contrast and recovery.

## 22. Theme is explained
Narrator/character states what the story "means" after the events already demonstrated it.

Fix:
- trust image, action, consequence, and unresolved interpretation.

## 23. Ending is too neat
Every relationship heals, every question closes, protagonist fully understands themselves.

Fix:
- close the story's required contract, not every human contradiction.

## 24. Ending is too abrupt
Climax occurs and story cuts before the important consequence lands.

Fix:
- add the smallest necessary aftermath.

## 25. Revision becomes line-polish before story repair
Writer perfects sentences inside scenes that may later be cut.

Fix:
- revise macro → scene → paragraph → sentence.

---

# 98. Reader-Trust / Redundancy Audit

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

## Trust test

Ask:

- Can the reader infer this?
- Is ambiguity productive?
- Is the explanation necessary for plot comprehension or only reassurance?
- Does deleting the explanatory sentence make the passage stronger?

Do not confuse reader trust with obscurity.

Necessary facts should be clear.
Interpretation can remain open.

---

# 99. Endings: Consequence Without Over-Explanation

An ending should answer the story's **ending contract**, not clean the whole universe.

## Ending questions

- What question did the opening implicitly promise to address?
- What irreversible choice has the protagonist made?
- What changed externally?
- What changed relationally?
- What changed internally, if anything?
- What remains unresolved because it belongs to life rather than plot?
- Does the reader need aftermath?
- Is the story explaining its theme after already dramatizing it?

## Aftermath minimum

After climax, include enough consequence for the reader to understand:
- who paid;
- what changed;
- what cannot be restored;
- what new state exists.

Then stop before the story writes its own book report.

---

# 100. Storytelling Question Bank

These questions are primarily **internal agent diagnostics**.

Do not interrogate the user with all of them.

Ask the user only when:
- the answer is a true creative constraint;
- multiple choices would produce materially different requested works;
- context cannot reasonably resolve it.

Otherwise infer, draft, and revise.

## Premise

- Why this story?
- Why now?
- What becomes unstable?
- What is the reader promised?
- What is the central contradiction?
- What should remain unresolved?

## Character

- What does the character want today?
- Why do they want it?
- What do they think they need?
- What do they actually fear?
- What will they not admit?
- What do they misunderstand?
- What option would they never choose at the beginning?
- What could make that option imaginable later?

## Scene

- Who wants what?
- Why now?
- What resists?
- What tactic do they begin with?
- What makes them change tactic?
- What is the hidden sentence?
- What changes?
- What carries into the next scene?
- What can be cut from the beginning?
- What can be cut after the turn?
- What should be shown?
- What should be summarized?
- What is the one concrete anchor detail?
- What does the POV character notice that another would not?

## Dialogue

- What is the surface topic?
- What is the real topic?
- What can neither person safely say?
- Who has higher status?
- Who needs whom more?
- Is anyone answering a question nobody asked?
- Is exposition being spoken only for the reader?
- Would silence be stronger than this line?
- Do the voices actually differ?

## Backstory / World

- What does the reader need now?
- What can wait?
- What can be demonstrated before explained?
- What fact creates a question?
- What fact answers a question too soon?
- Is lore changing current action?

## Tension

- What might happen?
- What does the character think might happen?
- What does the reader think might happen?
- What is the cost of waiting?
- What is the cost of acting?
- What closes off an option?

## Description

- Why this detail?
- Who notices it?
- What does it imply?
- Is it specific or generic?
- Is it one detail too many?

## Ending

- What must close?
- What should stay open?
- What consequence has not yet landed?
- Is the theme being explained instead of left in the story?
- Did the character earn the change?

---

# 101. Craft Revision Passes

Do not revise everything at once.

Use passes:

## Pass 1 — Story physics
Check:
- causality;
- agency;
- motivation;
- chronology;
- world rules.

## Pass 2 — Scene necessity
For each scene:
- goal;
- resistance;
- change;
- carry-forward pressure.

Cut/merge/compress weak scenes before polishing sentences.

## Pass 3 — Entry / Exit
Run:
- enter-late test;
- leave-early test;
- orientation check.

## Pass 4 — Show / Tell
Mark:
- emotionally consequential dramatization;
- summary;
- exposition;
- repeated explanation.

Rebalance.

## Pass 5 — POV / Psychic Distance
Check:
- knowledge boundaries;
- head-hopping;
- accidental distance shifts;
- character-filtered detail.

## Pass 6 — Dialogue / Subtext
Check:
- hidden sentence;
- tactics;
- exposition;
- voice difference;
- read aloud.

## Pass 7 — Specificity / Image
Replace generic claims with selective concrete evidence.
Remove inventory description and sensory clutter.

## Pass 8 — Setup / Payoff
Track active promises and missing seeds.

## Pass 9 — Rhythm / Pacing
Check:
- paragraph density;
- sentence rhythm;
- scene/summary balance;
- emotional intensity variation.

## Pass 10 — Reader Trust
Remove:
- theme explanation;
- emotional restatement;
- redundant interpretation.

## Pass 11 — Line Edit
Only now optimize:
- syntax;
- diction;
- modifiers;
- repetition;
- sound.

---

# 102. v0.4 Quality Gate

Before returning substantial fiction, ask:

## Story
- Does a character want something specific enough to generate behavior?
- Do choices create consequences?
- Are important surprises causally usable?

## Scene
- Does each major scene have a deliberate function?
- What changes?
- Does it enter and exit at useful points?

## Show / Tell
- Are important moments experienced rather than merely reported?
- Is summary used intelligently for compression?
- Did "showing" become generic body-language clutter?

## POV
- Is psychic distance deliberate?
- Are details filtered through the correct mind?
- Any accidental head-hopping?

## Dialogue
- Is there subtext where social/psychological pressure would create it?
- Are voices distinct?
- Is dialogue carrying unnatural exposition?

## Exposition
- Is information arriving because it matters now?
- Is backstory answering a question the reader actually has?

## Specificity
- Are details selective and useful?
- Any inventory description?

## Tension
- What does the character risk?
- What closes off options?
- Does quiet material still contain pressure?

## Setup / Payoff
- Are conspicuous promises paid, transformed, or intentionally left open?
- Are important payoffs sufficiently seeded?

## Theme
- Does the story trust the reader?
- Is the narrator explaining the moral after the events already did?

## Ending
- Did the climax produce visible consequence?
- Is there enough aftermath?
- Is there too much explanation?

## Prose
- Is the voice specific to this project?
- Is sentence rhythm varied by function?
- Did line polish hide a larger story problem?

When checks fail, revise the **relevant layer**, not merely wording.

---

# 103. v0.4 Compact Runtime Instruction

When context is limited:

> Lock user intent. Build stateful characters with specific wants, beliefs, blind spots, and pressures. Generate structurally different possibilities before committing. For each scene, identify POV, desire, resistance, hidden pressure, reader question, scene change, and carry-forward consequence. Deliberately choose what the reader should experience through scene and what should be compressed through telling. Filter detail through POV and manage psychic distance. Give important dialogue a surface topic, hidden intent, tactic, and subtext; avoid exposition spoken only for the reader. Reveal backstory on a need-to-know basis. Use selective concrete detail rather than generic description or inventory. Track setups and payoffs. Enter scenes late and leave early when compression strengthens them, but allow slowness when duration has artistic function. Revise macro before micro, run reader-trust and redundancy audits, and close the story's contract without over-explaining its theme.
