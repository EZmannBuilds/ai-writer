# Dialogue

Dialogue as action under pressure: surface topic, real topic, tactics, and the sentence nobody can say.

| Contract | |
|---|---|
| Invoked by | Router for any scene with significant dialogue; the Romance pack and Comic Panel Writer consume it. |
| When | Before drafting important exchanges; during the Dialogue/Subtext revision pass. |
| Needs | Speakers' mental states; relationship state; scene contract's `hidden_sentence`. |
| Produces | `dialogue_state` / `subtext` records for the exchange. |
| State | Ephemeral. Consequences land in `relationships`. |
| Consumed by | [prose](prose.md), [comic-panel-writer](../packs/comic-panel-writer.md) (lettering). |
| Skip when | Incidental lines; confession or crisis scenes where directness is the event (still check voice). |
| Tests | F13 |
| Research | [research/core/page-craft.md](../research/core/page-craft.md), [research/core/character-cognition.md](../research/core/character-cognition.md) |

---

## Dialogue Engine

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

## Dialogue and Subtext Engine

*Basis: [@reedsy-dialogue], [@masterclass-dialogue], [@nybe-dialogue], [@scriptmag-subtext]*

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

### Useful tactics

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

### On-the-nose test

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

### Read-aloud pass

Read significant dialogue aloud.

Listen for:
- impossible sentence length;
- repeated formal syntax;
- lack of contractions where character would use them;
- every speaker sharing the same rhythm;
- exposition nobody would naturally say;
- cleverness exceeding the character.

---

## Dialogue quick card

Dialogue is not information with quotation marks.

### The hidden sentence

For emotionally important dialogue identify:

```text
the sentence the character most wants to say
but cannot / will not / does not understand enough to say
```

Then write the conversation under its pressure.

### Reasons for subtext

A character may avoid directness because of:
- shame;
- status;
- love;
- fear;
- etiquette;
- manipulation;
- denial;
- professional risk;
- pride;
- uncertainty.

### Tactics

Characters can:
- deflect;
- ask instead of answer;
- attack a smaller issue;
- joke;
- bargain;
- over-agree;
- perform politeness;
- withdraw;
- change subject;
- use an object/task as cover;
- lie;
- remain silent.

### Exposition trap

Flag dialogue that sounds like:

```text
"as you know..."
"since we both..."
"remember when..."
```

when the real reason is to brief the reader.

Information can enter dialogue if one person:
- does not know it;
- disputes it;
- needs it;
- lies about it;
- weaponizes it;
- misunderstands it.

### Voice distinction

Do not give each character a gimmick.

Differentiate through:
- sentence length;
- vocabulary;
- directness;
- social caution;
- humor;
- metaphors;
- what they avoid;
- what they assume;
- tactics under pressure.

### Read-aloud pass

If a line feels unnatural aloud, investigate:
- overlong syntax;
- too much explanation;
- formal wording;
- repeated names;
- lack of contractions;
- cleverness beyond character.
