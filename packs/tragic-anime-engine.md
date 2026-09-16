---
pack:
  id: tragic-anime-engine
  name: Tragic Anime Story Engine
  version: '1.1'
  stage: genre
  pipeline_position: After Draft Starter and Origin Forge (when present), before Intent Lock.
  purpose: Make suffering, death, sacrifice, revelation, and defeat change the story, in dark action and
    tragic fantasy.
  triggers:
  - Start Tragic Story
  - Dark Anime Mode
  natural_language_triggers:
  - Build a tragic arc
  - Make this more emotionally devastating
  - Give this Attack on Titan / JJK structural energy
  - Build a consequential character death
  - Build the reveal chain
  - Pressure-test this cast
  requires:
  - core/information-architecture
  - core/character-model
  optional_dependencies:
  - draft-starter
  - origin-forge
  - series-engine
  conflicts_with: []
  stacks_with:
  - draft-starter
  - origin-forge
  - mystery
  - horror
  - romance
  - series-engine
  - worldbuilding
  - comic-panel-writer
  inputs:
  - draft_brief
  - origin_brief
  - character canon
  - user content boundaries
  produces:
  - tragic_story_brief
  - hope_reserve
  - consequence_ledger
  - reveal_ledger
  - death_impact_card
  - power_cost_card
  - ensemble_pressure
  skip_when:
  - The user wants a light, comic, or gentle story.
  - The user has ruled out lethal or irreversible consequences and the story has no other tragic engine.
  - Darkness is only incidental to a scene request.
  state_keys:
  - pack_state.tragic-anime-engine
  - open_loops
  - characters.<id>.developing_state
  - relationships
  research_basis: research/packs/tragic-anime-engine.md
  behavior_tests:
  - F08
  - F09
  - F10
  - F11
  - F29
---

# Tragic Anime Story Engine

Dark action and tragic fantasy, built from transferable craft, not imitation.

Primary reference pillars: **Attack on Titan** (escalating world mystery, ensemble military pressure, perspective reversal, humanized enemies, cycles of fear/oppression, recontextualizing revelations) and **Jujutsu Kaisen** (characters developing under cruel conditions, death as thematic lens, individualized dialogue, consequential combat, supernatural rules that pressure values). Secondary lenses (Madoka, Devilman Crybaby, Edgerunners, 86, To Your Eternity, Fate/Zero, Made in Abyss, Violet Evergarden, Chainsaw Man): see `packs/tragic-anime-lenses.md`.

> [!important] Design rule: borrow reasoning, not identity
> This pack extracts transferable narrative principles from official publisher/creator material — it does not copy prose, dialogue, plots, character designs, terminology, or the exact creative voice of any reference work. Never: copy character archetypes one-for-one, reuse proprietary terminology, recreate signature scenes, copy plot sequences, imitate exact dialogue cadence, or reproduce an author's distinctive prose voice.

**Triggers:** "Start Tragic Story," "Dark Anime Mode," "Build a tragic arc," "Make this more emotionally devastating," "Give this Attack on Titan / JJK structural energy," "Build a consequential character death," "Build the reveal chain," "Pressure-test this cast."

**Pipeline:** `Draft Starter → Origin Forge (when relevant) → Tragic Anime Story Engine → Intent Lock → Story Genome → Arc/Reveal/Consequence Planning → Comic Panel Writer or prose drafting`

**State:** all ledgers live under `pack_state.tragic-anime-engine`. Open reveals are mirrored into `open_loops`; power costs and death residue update the affected [character records](../core/character-model.md); relationship changes go to [relationships](../core/relationships.md). The reveal ledger extends [information architecture](../core/information-architecture.md) — it does not replace it.

**Core promise:** not a "kill characters" button. Its purpose is to make suffering, death, sacrifice, revelation, and defeat **change the story**. Do not confuse darkness with depth.

---

## I. The Core Tragedy Equation

`VALUED THING + PRESSURE + CHOICE + COST + RESIDUE = TRAGEDY`

- **Valued Thing** — friendship, family, freedom, home, ordinary life, reputation, future, moral code, identity, team, dream, promise.
- **Pressure** — war, cursed power, institution, impossible deadline, enemy doctrine, scarcity, inherited conflict, body cost, prophecy, public fear, misinformation.
- **Choice** — tragedy strengthens when consequence follows a *meaningful* choice, not random punishment.
- **Cost** — what becomes unavailable because of the choice.
- **Residue** — guilt, duty, inherited weapon, political consequence, unfinished promise, changed combat strategy, new fear, ideological hardening, relationship fracture, social myth, trauma, moral debt. **If there is no residue, the tragedy may only be spectacle.**

## II. Cruel Conditions, Not Random Cruelty

Cruelty should pressure character beliefs. Before adding gore, death, torture, betrayal, massacre, body horror, or permanent injury, ask: which character value is being tested? Which relationship changes? What decision becomes harder? What future consequence is created? What theme gains pressure? **If the answer is "none," reconsider the event.** Darkness without consequence is noise.

*The deeper question isn't "how horrible can the story become," it's "who does this person become when the world removes easy choices" — use pressure to reveal duty, selfishness, loyalty, fear, tenderness, philosophy of death, relationship to responsibility.*

## III. Hope Reserve

A tragic story needs something worth losing. Maintain a Hope Reserve: ordinary pleasures, jokes, meals, plans, crushes, rivalries, rituals, dreams, domestic spaces, future promises, moments of competence, people who still believe in each other. **Do not remove every source of warmth** — the reader must periodically understand what survival is for.

```yaml
hope_reserve:
  - hope: null
    character_or_group: null
    concrete_future_image: null
    evidence_it_is_possible: null
    current_threat: null
    status: alive          # alive | altered | false | lost | achieved
    payoff_or_loss_point: null
```

## IV. Perspective Reversal

When the story is large enough, let the reader understand people previously treated as enemies, monsters, invaders, terrorists, traitors, institutions, rival factions. **A perspective shift is not an automatic moral pardon.** Ask: what did the protagonist believe about them? What do they believe about themselves? What material/history makes their worldview intelligible? What actions remain objectionable even after understanding them?

**Six-stage module, when a conflict starts with a simplified enemy image:**
1. **Enemy silhouette** — protagonists understand the threat mainly through consequence.
2. **Contradictory evidence** — introduce behavior that doesn't fit the stereotype.
3. **Named enemy** — individual enemies get names, relationships, private goals, disagreements.
4. **Historical context** — reveal how the conflict looks from their side.
5. **Protagonist reframed** — show the protagonist's actions from the enemy viewpoint.
6. **Collision** — return the perspectives to direct conflict.

**Guardrail: perspective is not absolution.** Increase understanding while preserving evidence about actual harm.

## V. Reveal Architecture

A major reveal should change at least two of: interpretation of prior scenes, identity, faction map, stakes, power rules, moral responsibility, history, future goal. Prefer `ANSWER → RECONTEXTUALIZATION → LARGER QUESTION` over `ANSWER → next unrelated mystery`.

**Mystery ladder** — build at several levels at once, don't reveal them all together: *Personal* (why did this person lie?) · *Tactical* (why did the enemy retreat? how does the power really work?) · *Institutional* (what is the organization hiding?) · *Historical* (which accepted story about the past is false?) · *Cosmological* (what are the monsters/powers/world actually?).

**Fairness test**, before the reveal: at least one clue exists, at least one plausible wrong interpretation exists, no requirement that the reader guess the exact answer. Goal: *"I didn't predict that, but now I can see it,"* not *"there was no way to know."*

**Answer debt** — track question, promised answer horizon, clue count, partial answers, final answer, consequence. Don't create mysteries faster than the story can metabolize them.

```yaml
reveal_ledger:
  - id: R1
    question: null
    first_raised: null
    clues: []
    first_read_meaning: null
    true_meaning: null
    reveal_point: null
    recontextualizes: []
    affected_characters: []
    affected_factions: []
    action_caused: null
    larger_question_created: null
    status: planned
```

**Reveal Chain Designer** — build a chain of 3–6 reveals; for each: question answered, clues planted, surface interpretation, true interpretation, character most affected, faction most affected, new question created, action caused by the reveal. *A reveal that causes no action may belong in lore rather than plot.*

## VI. Consequential Death

Death is one tragedy tool, not the only one. **Death Necessity Test** before killing a character:
- **Function** — what does this death accomplish that survival cannot accomplish as well?
- **Preparation** — what relationships, promises, ambitions, flaws, unfinished business make it matter?
- **Causality** — why now?
- **Residue** — who changes because of it?
- **Irreplaceability** — what specific capability, relationship, worldview, or future disappears?
- **Story mutation** — how is the narrative different ten chapters later?

If the story returns to normal immediately, the death is underwritten.

**Character Death Designer** — don't activate automatically. Required fields: character, current desire, unfinished relationship, tactical function, thematic function, cause, preventability, last meaningful choice, immediate witness, public interpretation, private truth, inherited object/duty, three downstream consequences, chapter/arc where the absence is felt again. **Rescue alternative:** before finalizing a death, generate one version where the character survives with a severe consequence instead, and compare — if survival produces a richer story, don't kill them.

```yaml
death_impact_card:
  character: null
  current_desire: null
  future_they_expected: null
  unfinished_relationship: null
  narrative_function_before_death: null
  death: { cause: null, choice: null, preventability: null, witness: null, final_action: null }
  residue:
    emotional: []
    tactical: []
    ideological: []
    institutional: []
    inherited_objects_or_duties: []
    future_callback_points: []
  survival_alternative: { considered: false, version: null, why_death_is_stronger: null }
  necessity_status: null   # justified | revise | survival_stronger
```

**Aftermath Writer** — after major death, massacre, defeat, betrayal, or transformation, include an aftermath phase. Beats: casualty accounting, missing person confirmation, cleanup, funeral, political spin, argument about blame, equipment reassignment, changed sleeping arrangements, a survivor returning an object, media/public response, changed chain of command, someone using the dead character's technique, an empty seat/room/routine, mission continuing despite grief. **Purpose: not melodrama — proof the world noticed.**

## VII. Tragedy Variety

Do not solve every arc with death. Rotate: death, permanent injury, power loss, irreversible transformation, exile, moral compromise, betrayed trust, public disgrace, failed rescue, ruined home, victory with unacceptable cost, identity collapse, separation, memory loss, corrupted legacy, survivor burden, unwanted inheritance, becoming what one opposed, discovering the enemy was partly right, saving the world but losing the desired life. Rotate forms to prevent emotional numbness.

**Before proposing any death, lay out at least three non-death tragedy options** for the arc, drawn from this list, and say what each would cost the story and give it. A death may then be offered as one option among them, labeled a proposal, with the Death Necessity Test.

## VIII. Power Under Pressure

A dark battle system should generate story, not just fights. For each power, track: capability, limitation, cost, condition, counterplay, social meaning, emotional temptation, irreversible consequence. **Rule: power should solve one problem while exposing another** — stronger output damages the body; healing transfers harm; prediction destroys spontaneity; transformation erodes identity; summoning creates debt; forbidden technique exposes location; immortality preserves memory of every loss. Social and moral costs can be stronger than physical ones.

```yaml
power_cost_card:
  ability: null
  capability: null
  activation: null
  limitation: null
  costs: { immediate: [], delayed: [], biological: [], resource: [], social: [], relational: [], moral: [], identity: [] }
  counterplay: []
  information_revealed_to_enemy: []
  three_use_consequence: null
  escalation_form: null
```

## IX. Escalation

Don't escalate only via stronger enemies — alternate axes: **threat scale** (person → team → city → nation → civilization) · **truth scale** (rumor → secret → institutional truth → historical truth → cosmological truth) · **moral scale** (clear defense → compromised necessity → faction conflict → impossible choice) · **personal scale** (stranger → teammate → family → self → identity) · **cost scale** (fatigue → injury → sacrifice → irreversible consequence) · **agency scale** (reacting → choosing → commanding → becoming responsible for others).

## X. Ensemble Pressure

Every major character needs: desire, fear, capability, relationship, belief, vulnerability, current pressure, potential breaking point. **Don't treat supporting characters as queued corpses** — before killing someone, make sure they were living a story.

```yaml
ensemble_pressure:
  - character: null
    desire: null
    duty: null
    fear: null
    core_relationship: null
    belief: null
    capability: null
    vulnerability: null
    current_pressure: null
    breaking_point: null
    likely_response_to_loss: null
    arc_status: active
```

## XI. Dialogue

Dark stories still need human texture. Characters joke, grieve, rationalize, swear, avoid questions, and express affection *differently* — avoid one philosophical mouthpiece voicing everyone. After a catastrophe, different characters speak, shut down, work, clean, joke, get angry, obsess over logistics, or cling to routine. Let grief diversify voice.

## XII. Ideological Conflict

`VALUE → FEAR → POLICY → HUMAN COST` (e.g. Value: Security. Fear: Another invasion. Policy: Permanent military control. Human Cost: Civilian autonomy disappears.) Stronger than "Faction A good / Faction B evil."

**Faction builder** — for each faction: historical wound, core value, central fear, public story, private contradiction, policy, beneficiary, victim, internal dissident, the line they claim they won't cross, the line they actually cross. **No large faction speaks with one voice** — hardliners, reformers, opportunists, exhausted moderates, true believers, people trapped by circumstance. Avoid "everyone is equally wrong" — track evidence, power, coercion, alternatives, scale of harm, intent, accountability instead; a faction can be understandable and still clearly doing something worse. A strong ideological rival threatens the protagonist's model of justice, freedom, strength, sacrifice, love, humanity, or responsibility — not just their body.

## XIII. Tragic Foreshadowing

Two readable states: **first-read meaning** (ordinary, mysterious, or emotionally specific) and **later meaning** (new information gives the same detail a second function). Hide inside casual dialogue, family history, a recurring image, a procedural rule, architecture, a joke, a dream, a weapon limitation, an unexplained reaction, a missing name, a ritual. Record both meanings in the reveal ledger.

## XIV. Endgame

A tragic ending should pay off the central thematic question, the protagonist's core desire, the world conflict, the major relationship, and accumulated consequences.

**Endgame convergence** — the final arc should feel like multiple story debts arriving at once: protagonist desire, main relationship, world mystery, faction conflict, power cost, original promise, accumulated dead/absent characters, central theme. Phrase one question the ending must answer (*"Is freedom possible if it requires domination?" "Does saving people justify controlling them?" "Can grief become responsibility instead of revenge?"*). Choose a final cost that attacks the protagonist's original desire — they save the city but can't go home; they stop the curse but lose the power that defined them; they win freedom but lose the person they wanted to share it with.

**Avoid:** new cosmology appearing too late, a final villain with no thematic connection, resurrecting losses only to soften the ending, explaining every ambiguity, ending immediately after the climax with no social aftermath.

**Ending types:** Tragic (loses the thing they tried to preserve) · Bittersweet (goal achieved at permanent personal cost) · Contaminated victory (external victory preserves a moral wound or unstable system) · Redemptive tragedy (protagonist dies/falls/loses but changes others' moral direction) · Surviving tragedy (protagonist lives and must carry what happened) · Hope-after-ruin (the system is broken, but something human remains possible). Don't make the ending dark only because the rest of the story was dark.

## XV. Activation Procedure

1. Read existing canon first (canon, Draft Brief, Origin Brief, character files, user constraints — don't re-ask known information).
2. Identify the story's Hope Reserve.
3. Identify the central tragic pressure.
4. Determine which tragedy engines are already present: war/system, cursed/supernatural cost, mystery/reveal, ensemble mortality, ideological conflict, body cost, repeating loss, institutional dehumanization, irreversible descent.
5. Select only useful reference lenses (expanding threat/enemy perspective, cruel conditions, hope/despair trap, institutional dehumanization, systemic doom, repeated attachment/loss, ideological zero-sum, irreversible descent, postwar aftermath) — don't imitate exact reference style.
6. Ask no more than 3–5 questions if major choices are missing. Prefer: What must remain worth fighting for? How lethal/irreversible should consequences be? Should the story reframe the enemy later? How much mystery should the world contain? What ending range is allowed?
7. Produce a Tragic Story Brief, a Hope Reserve, the first active Consequence Ledger, and a Reveal Ledger only if the story uses major mystery.
8. Continue to arc design, reveal design, death audit, or drafting.

## Tragic Arc Designer

For an arc: **arc promise** (what does the cast believe can be accomplished?) · **emotional promise** (what relationship/hope might improve?) · **hidden pressure** (what already makes success unstable?) · **midpoint truth** (what information changes the mission's meaning?) · **apparent victory** (what seems solved?) · **cost collection** (which earlier debt arrives?) · **irreversible change** (what can't return to pre-arc normal?) · **residue** (what becomes the next arc's starting condition?). A tragic arc should not end by restoring the board.

---

## Schemas

```yaml
tragic_story_brief:
  version: "1.0"
  premise: null
  genre: []
  format: null
  core:
    protagonist_desire: null
    central_relationship: null
    thematic_question: null
    hope_reserve: []
    primary_pressure: null
  tragedy_engines: []   # war_system | supernatural_cost | mystery_reveal | ensemble_mortality | ideology
                         # irreversible_descent | repeating_loss | institutional_dehumanization | body_cost
  world: { apparent_truth: null, hidden_truth: null, faction_conflicts: [] }
  power_system: { core_rule: null, major_cost: null, irreversible_costs: [] }
  major_characters: []
  reveal_chain: []
  irreversible_losses: []
  ending: { type: null, central_answer: null, final_cost: null, surviving_hope: null }
  guardrails: { forbidden_tropes: [], content_boundaries: [], do_not_copy_reference_elements: true }
  provenance: { confirmed_facts: [], agent_proposals: [], unresolved_questions: [] }
  recommended_next_action: null
```

```yaml
consequence_ledger:
  - event_id: null
    event: null
    immediate_costs: []
    delayed_debts: []
    relationship_changes: []
    belief_changes: []
    tactical_changes: []
    institutional_changes: []
    public_narrative: null
    private_truth: null
    next_arc_effect: null
    paid_off: false
```

---

## Integration with the other inserts

- **Draft Starter** establishes emotional core, premise, protagonist, central relationship, setting, creative permissions — then activate this pack if the user wants dark action, tragic fantasy, lethal consequences, ideological conflict, reveal-heavy worldbuilding, or emotionally brutal ensemble storytelling. **Don't make every story tragic merely because the pack exists.**
- **Origin Forge** explains how a person became this identity; this pack explains **what the ongoing story does to that identity under pressure.** Map Origin Forge's Before Self / Disruption / Meaning / Alignment-defining choice / Power cost / Contradiction into this pack's Hope Reserve, Character Pressure Map, Power Cost Card, ideological conflict, and future breaking point. **For villains: do not use tragedy to excuse them** — use it to explain pressure, then keep tracking choices and accountability.
- **Comic Panel Writer** takes this pack's outputs (what the tragedy means, which reveal lands, which relationship changes, what cost becomes irreversible) and determines page-turn placement, silent reaction panels, impact pages, reveal framing, aftermath rhythm, visual callbacks. Strong sequence: `hope beat → pressure → choice → event → silence → consequence`. A death splash with no later empty-seat panel, tactical gap, argument, funeral, or behavioral change can feel hollow.

---

## Behavior checks

Regression fixtures: [F08](../tests/fixtures/F08-tragic-engine-does-not-default-to-death.yaml), [F09](../tests/fixtures/F09-death-creates-downstream-residue.yaml), [F10](../tests/fixtures/F10-survival-alternative-considered.yaml), [F11](../tests/fixtures/F11-power-costs-persist.yaml), [F29](../tests/fixtures/F29-dark-anime-mode-legacy-trigger.yaml).

1. Darkness is not automatic — can recommend less death when another consequence is stronger.
2. Hope Reserve identifies concrete ordinary things worth preserving.
3. Death residue — a major death alters at least three future story elements.
4. Enemy perspective — humanization increases understanding without automatically erasing accountability.
5. Reveal quality — major reveals recontextualize earlier material and cause action.
6. Cruel-condition purpose — severe events test values/relationships, not just shock.
7. Escalation diversity — uses truth, moral cost, personal stakes, or agency, not only stronger enemies.
8. Ensemble life — supporting characters have desires/relationships beyond their death function.
9. Power consequence — stated costs recur later.
10. Grief diversity — characters react in distinct ways.
11. Tragedy variety — multiple loss types available, not death-only.
12. Reference independence — generated stories don't copy proprietary names, characters, plot sequences, or distinctive dialogue from reference works.

## Story audit checklist

What does the audience hope survives, and is that hope concrete? Are consequences cumulative? Does each major arc permanently alter the state? Are deaths causally grounded, and does every major death leave residue? Are there important non-death losses? Are power costs enforced? Does the cast hold different philosophies, and are factions internally diverse? Are antagonists understandable without forced sympathy? Are reveals foreshadowed, and do they change decisions? Does mystery debt get paid? Does escalation vary across axes? Is there room for humor, tenderness, routine, or beauty? Does aftermath receive page/time space? Does the endgame converge earlier story debts? Does the ending answer the story's central question?

---

## Research provenance

Reference-work claims come from official publisher and streaming descriptions and from creator/editor interviews, reduced to transferable mechanisms. Sources, what each supports, and limits: [research/packs/tragic-anime-engine.md](../research/packs/tragic-anime-engine.md).
