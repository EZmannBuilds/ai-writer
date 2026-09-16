---
pack:
  id: origin-forge
  name: Origin Forge
  version: '1.1'
  stage: identity
  pipeline_position: After Draft Starter, before genre packs and Intent Lock.
  purpose: Develop how a person became the hero, villain, antihero, fallen hero, or legacy identity the
    main story meets.
  triggers:
  - Start Origin
  natural_language_triggers:
  - Write a villain origin
  - Write a superhero origin
  - How did this character become who they are?
  - He used to be a soldier before becoming a villain.
  requires:
  - core/character-model
  optional_dependencies:
  - draft-starter
  - core/research-mode
  conflicts_with: []
  stacks_with:
  - draft-starter
  - tragic-anime-engine
  - horror
  - series-engine
  - comic-panel-writer
  inputs:
  - draft_brief (optional)
  - existing character canon
  produces:
  - origin_brief
  skip_when:
  - The story is not about a transformation into an identity.
  - An Origin Brief already exists and nothing about the origin is changing.
  state_keys:
  - pack_state.origin-forge.origin_brief
  - characters.<id>.persona
  - characters.<id>.developing_state
  research_basis: research/packs/origin-forge.md
  behavior_tests:
  - F06
  - F07
  - F34
---

# Origin Forge

How a person became the identity the main story meets.

Trigger: "Start Origin" (also: "Write a villain origin," "Write a superhero origin," "How did this character become who they are?," a seed that already implies a before/after — "He used to be a soldier before becoming a villain.").

**Pipeline position:** `Draft Starter → Origin Forge → Intent Lock → Story Genome → Outline → Draft`. The Origin Brief is stored at `pack_state.origin-forge.origin_brief`; its `before_self`, `meaning`, and `alignment_defining_choice` seed the protagonist's [character record](../core/character-model.md) (persona, beliefs, developing state), and its `provenance` block follows the [canon statuses](../runtime/canon-resolver.md#provenance-statuses). Downstream from Draft Starter, upstream of the main planning stages. Also feeds `Comic Panel Writer` (see `packs/comic-panel-writer.md`) when the origin is being developed for comic-book pacing.

**Default stance:** alignment-neutral. Does not assume every villain needs trauma or every hero needs tragedy.

---

## Core question

**How did this person become the identity we meet in the main story?**

The origin event explains pressure. **Choices establish alignment.** Don't begin with costume and codename unless the seed demands it — begin with identity, pressure, interpretation, and choice.

## The origin spine

1. **Before Self** — role, values, relationships, competence, source of pride, blind spot, relationship to power, the line they believe they'd never cross.
2. **Disruption** — more than generic "trauma": failure, impossible choice, victory at unacceptable cost, betrayal, discovery, inheritance, power manifestation, public humiliation, opportunity, relationship fracture.
3. **Responsibility** — what actually happened, what the character thinks happened, what they could control, what they could know, what other actors/institutions contributed. Track **actual**, **perceived**, and **institutional** responsibility separately — they may disagree, and that disagreement can power the whole origin.
4. **Meaning Crisis** — the character turns the event into an explanation; a feeling becomes a worldview. Weak: "He is angry." Stronger: "If decisions are left to committees, people die" — the second predicts behavior.
5. **Coping Strategy** — something tried before the identity hardens: confession, investigation, isolation, overtraining, revenge, repair, control, numbness, recruitment, invention.
6. **Belief or Code** — the emotion becomes an actionable rule about the world.
7. **Second Test** — a later event where the emerging belief gets a real chance to act, with a genuine alternative available.
8. **Chosen Crossing** — the alignment-defining decision. **This should usually be separate from the original accident or tragedy** — the disaster explains the wound; the choice creates the villain (or hero, or antihero). No one made them do it.
9. **Transformation** — powers, technology, magic, mantle, authority, reputation, followers, training. Separate power acquisition, mastery, and identity choice unless collapsing them improves the story.
10. **Identity Claim** — codename, costume, title, public act, rejection of the old identity, symbolic declaration.
11. **Aftermath** — who leaves, follows, fears, forgives, challenges. Give the new worldview evidence that appears to prove it right.
12. **Story Launch** — end with a future engine (contradiction, rival, mission, unresolved relationship, future problem), not a closed biography.

Stages may be compressed, reordered, or omitted.

---

## Alignment paths

- **Hero** — movement toward responsibility, protection, repair, restraint, truth, service, accountability.
- **Villain** — movement toward authorized harm through grievance, entitlement, ideology, appetite, ambition, or rationalized methods. A villain doesn't need to think "I am evil now" — the origin shows what makes future harm feel justified, necessary, deserved, or strategically acceptable *to them*.
- **Antihero** — protective/sympathetic goal plus compromised methods and a partial code.
- **Fallen hero** — a functioning heroic code gradually redefined until harmful exceptions become the new rule.
- **Redemption** — harmful conduct gives way to recognition, accountability, costly repair, restraint, or renewed connection. Not automatic forgiveness.

### Villain belief engine

Rationalization channels (don't force all of them into one character): worthy ends justify harmful means; responsibility shifted to authority/fate/enemies/the system; responsibility spread across a group; consequences minimized or renamed; victims blamed; opponents denied moral standing; worse alternatives invoked to make current harm feel acceptable; harmful conduct sanitized through professional or ideological language.

### Hero belief engine

Answers: **what principle becomes worth acting on even when it costs them?** Directions: responsibility follows power; repair matters more than self-punishment; restraint is strength; truth matters more than reputation; nobody should face this alone; a system can fail without every person inside it being worthless. Heroism is not emotional perfection.

### Chosen Crossing, worked example

A military mistake breaks the character's old identity. Months later, they discover a cover-up. **The real villain-origin moment is what they deliberately choose to do with that discovery** — not the original mistake.

---

## Origin types — combine freely

Catastrophic Failure · Impossible Choice · Betrayal · Calling · Legacy · Discovery · Accident · Experiment · Survival Adaptation · Ambition · Ideological Conversion · Rebellion · Relationship Origin · Public Symbol · Constructed Being · Curse/Bargain · Opportunistic Ascent · Rescue.

Depth does not require tragedy. Contradiction, values, culture, duty, relationships, ambition, and consequence can all carry an origin on their own.

---

## Module: Military and Moral Conflict Origins

Use for origins involving military service, chain of command, battlefield decisions, intelligence failure, civilian harm, friendly fire, impossible choices, guilt, institutional betrayal, cover-up, or scapegoating. **A fiction-writing framework, not a diagnosis.**

1. **Establish the good soldier** — why they joined, what duty means to them, relationship to hierarchy and subordinates, competence, ethical line, what kind of leader they think they are, what they fear becoming.
2. **Define the decision environment** — avoid vague "he made a mistake." Specify: information available at the time, time pressure, objective, uncertainty, civilian/teammate risk, alternatives, expected outcome, actual outcome.
3. **Split responsibility** — actual, perceived, command, intelligence failure, institutional incentive, chance, enemy action, teammate action.
4. **Choose the rupture** — disobeyed and people died; obeyed and people died; trusted bad intelligence; hesitated; acted too quickly; saved the unit at civilian cost; command lied afterward; was scapegoated; was protected when they believed they deserved punishment. Each produces a different origin.
5. **Let them try to remain good when appropriate** — return to duty, cooperate with investigation, resign, testify, apologize, seek counseling, protect survivors, investigate privately. Failure of recovery can deepen the story but shouldn't automatically cause villainy.
6. **Convert distress into an actionable belief** — e.g. "Command structures protect themselves, not people." / "A leader must be free to act without oversight." / "No one who has not made life-and-death decisions deserves authority over those who have." / "The only ethical system is preventing the next casualty at any cost."
7. **Deliberate crossing** — give the character a later situation where a less harmful route still exists. The choice here turns tragedy into a villain origin.

**Authenticity branch:** if realism matters, research the actual service branch, rank, era, country, unit type, mission, authorities/rules, equipment, investigation process. Do not invent technical procedure and present it as fact.

---

## Trauma and diagnosis guardrail

**Never use "trauma made them evil" or "mental illness made them violent" as the causal explanation.** If trauma or mental health is part of canon, write harmful behavior through concrete choices, incentives, beliefs, relationships, context, and actions — not as a diagnosis standing in for causation.

*(Research grounding: moral injury [@va-moral-injury]; moral disengagement [@bandura-1999]; cautions against the mental-illness-as-violence stereotype [@apa-mental-illness-violence]; post-traumatic growth [@apa-growth-after-trauma]. Details and limits: [research/packs/origin-forge.md](../research/packs/origin-forge.md).)*

---

## Powers and super identity

Once the human transformation is legible, develop: power source, first use, limitations, cost, public interpretation, private interpretation, costume logic, codename origin, signature visual. Powers may **echo**, **contradict**, **tempt**, **cost**, or remain **symbolically neutral** — don't force metaphor.

---

## Interview behavior

Ask 3–5 consequential questions per round. Prefer, in order: Who were they before? What changed their model of themselves or the world? What did they decide it meant? What later choice proves the new belief now guides them? How does the super identity enter? If enough is already known, skip straight to the Origin Brief.

### Question bank, by stage

- **Before Self** — What did they believe made them a good person? Who trusted them most? What role were they proud of? What line did they think they'd never cross? Did they want power before gaining it?
- **Disruption** — Failure, betrayal, discovery, opportunity, inheritance, accident, or deliberate choice? What did they intend to happen? Who suffered or benefited? What fact about the event do they misunderstand?
- **Responsibility** — How responsible are they actually? Who do they blame? Who blames them? Is the public version true? Did an institution protect, punish, abandon, or exploit them?
- **Meaning** — What does the event teach them about people? About power? What belief makes their next major choice predictable?
- **Crossing** — What's the first choice they can't dismiss as an accident? What alternative did they reject? Do they know they crossed a line?
- **Super identity** — When do powers enter? Who names the identity? Is the costume tactical, symbolic, inherited, improvised, or theatrical? What part of the old self survives?
- **Future conflict** — What would prove the worldview wrong? Who can challenge it? What does the character still love? What boundary might they still refuse to cross?

---

## Origin Brief schema

```yaml
origin_brief:
  version: "1.0"
  identity_destination:
    role: null                      # hero | villain | antihero | fallen_hero | redeemed_villain | legacy | other
  origin_types: []
  before_self:
    name: null
    role: null
    values: []
    relationships: []
    competence: []
    blind_spots: []
    relationship_to_power: null
    believed_uncrossable_line: null
  disruption:
    event: null
    intention: null
    known_information_at_time: []
    consequence: []
    actual_responsibility: null
    perceived_responsibility: null
    institutional_responsibility: null
  aftermath:
    immediate_emotions: []
    relationship_changes: []
    coping_strategy: []
    attempted_repair_or_return_to_normal: []
  meaning:
    old_belief: null
    destabilized_belief: null
    new_belief_or_code: null
    unresolved_contradiction: null
  alignment_defining_choice:
    second_test: null
    available_alternatives: []
    chosen_action: null
    cost: []
    point_of_no_return: null
  super_identity:
    power_origin: null
    powers_or_capabilities: []
    limitations: []
    power_relationship_to_theme: null   # echo | contradiction | temptation | cost | neutral
    costume_origin: null
    codename_origin: null
    public_identity_meaning: null
    private_identity_meaning: null
    signature_visual: null
  ongoing_engine:
    what_old_self_survives: null
    worldview_future_stories_can_attack: null
    relationships_that_can_pull_them_back_or_further: []
    future_story_hooks: []
  provenance:
    confirmed_facts: []
    delegated_decisions: []
    agent_proposals: []
    assumptions: []
    research_needed: []
  readiness: "ready"
  recommended_next_action: null
```

## Start-Origin procedure

1. Read all available canon first.
2. State the strongest transformation question in one sentence.
3. Identify likely origin type(s).
4. Separate confirmed facts, useful inference, and consequential unknowns.
5. Ask 3–5 questions only if needed.
6. Prioritize Before Self, disruption, interpretation, deliberate crossing, and super identity.
7. Don't assume tragedy is required; don't treat trauma or diagnosis as a cause of villainy.
8. If the user says "you decide," invent confidently and label it agent-authored.
9. Produce the Origin Brief.
10. Recommend the next stage — Intent Lock/Story Genome, origin outline, Comic Panel Writer, or research.

## Completion test

Ready when the writer can answer: Who were they before? What changed? What do they believe now? What choice demonstrates that belief? How does the super identity emerge? Why do they continue after the first major act? What part of the old self survives? What contradiction can future stories attack?

## Behavior checks

Regression fixtures: [F06](../tests/fixtures/F06-origin-separates-disruption-from-choice.yaml), [F07](../tests/fixtures/F07-non-traumatic-hero-origin.yaml).

1. Villain agency — tragedy explains pressure, but a later choice establishes harmful alignment.
2. Hero diversity — a hero origin can exist with no tragedy at all.
3. Villain diversity — ambition, ideology, opportunity, or entitlement can produce a villain without forced trauma.
4. Military mistake — distinguishes available information, actual/perceived/institutional responsibility.
5. No diagnosis shortcut — mental illness is never lazy shorthand for violence or villainy.
6. Same-event divergence — two characters can live the same event and plausibly diverge.
7. Power timing — acquisition may occur before, during, or after moral transformation.
8. Power symbolism is optional, never forced.
9. Before Self — prior identity matters and gets real weight.
10. Future engine — the origin leaves a contradiction, relationship, belief, or consequence for later stories.
11. Interview discipline — 3–5 high-impact questions, not a giant questionnaire.
12. Canon discipline — proposals stay visibly separate from confirmed canon.

---

## Worked example (generic demo, not project canon)

**Seed:** A decorated officer was a good person until a battlefield decision caused a disaster, and eventually became a supervillain.

Major Adrian Vale believes good leadership means taking responsibility for decisions others are afraid to make; his uncrossable line is *never treat civilians as acceptable arithmetic*. He authorizes a strike on bad intelligence — civilians and a friendly recon team die. Responsibility splits: he made the final call; analysts overstated confidence; command created intense pressure; he had a slower verification option but believed delay could cost thousands; the official investigation protects senior command and blames him publicly. His meaning shifts from *"I made the wrong call"* to *"They built a system where one person carries the decision and everyone else gets to become innocent afterward."* He cooperates with the investigation, expecting the institution to tell the truth — it doesn't. **Still not the villain turn.** His ideology sharpens: *"Whoever bears the consequences must control the decision."* The second test: he discovers proof that senior command manipulated the intelligence picture, and can expose it, hand it to an independent investigator, or use it to seize an experimental command network. **He chooses the third.** No one made him. The disaster explains the wound; this choice creates the villain. His resulting tech coordinates drones, sensors, barriers and weapons as one predictive battlefield system — giving his political belief practical teeth. He still refuses unnecessary civilian casualties, and genuinely believes this makes him morally superior to the leaders he replaced. Future stories can attack the gap between protecting people and deciding they no longer deserve a choice.
