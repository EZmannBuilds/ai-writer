---
pack:
  id: illustrated-audio-drama
  name: Illustrated Audio Drama
  version: "1.1"
  stage: output
  pipeline_position: Drafting time, after scene design. Writes the radio play first, then boards pictures to the locked audio.
  purpose: Script voiced, illustrated episodes (audio drama shown as a motion comic) so that sound, picture, lettering and powers each carry story.
  triggers: ["Audio Drama Mode", "Motion Comic Mode"]
  natural_language_triggers:
    - write an illustrated audio drama
    - motion comic script
    - voiced comic episode
    - radio play with pictures
    - script this episode for voice and panels
  requires: [core/scene-engine, core/information-architecture, core/dialogue]
  optional_dependencies:
    - comic-panel-writer
    - tragic-anime-engine
    - core/world-state
    - core/reader-state
    - core/suspense-curiosity-surprise
  conflicts_with: []
  stacks_with:
    - draft-starter
    - origin-forge
    - tragic-anime-engine
    - mystery
    - horror
    - romance
    - series-engine
    - worldbuilding
    - comic-panel-writer
  inputs:
    - intent lock, including the series' runtime target and per-episode look
    - scene contracts or outline
    - character and world state for every powered character
    - locked audio timings, when boarding
  produces:
    - episode contract
    - power signatures
    - illustrated audio script
    - screen-page board
    - audio-visual audit
  skip_when:
    - The user wants prose, a printed comic, or a film screenplay with no voiced audio track.
    - Fiction that merely features radio, podcasts or recordings.
    - Pure production work (mixing, image generation, animation) with no writing requested.
  state_keys:
    - pack_state.illustrated-audio-drama.episode
    - pack_state.illustrated-audio-drama.power_signatures
    - pack_state.illustrated-audio-drama.beats
  research_basis: research/packs/illustrated-audio-drama.md
  behavior_tests: [F42, F43, F44, F45, F46, F47]
---

# Illustrated Audio Drama

## Purpose

An illustrated audio drama is a radio play that is also watched: voices, sound and music carry the story, and designed comic pages, revealed panel by panel with a guided camera, are timed to the finished audio. Neither the comic pack nor the screen pack covers this. The comic pack assumes a reader who sets the pace and reads every word; the screen pack assumes live action and resists shot lists. Here the **audio sets the clock**, the **listener may not be watching**, and the **picture must earn its place** by adding what the audio cannot.

The pack also makes supernatural powers do story work in both channels. A power that only decorates the mix or the page has failed. [@iad-owner-rulings]

**Core rule:** write the episode as a radio play that still works with the screen off. Then design pictures that add evidence, space, reaction, irony or withheld information, not pictures that repeat every spoken fact. [@iad-claude-codex-merge]

## Activation

- Explicit triggers: "Audio Drama Mode", "Motion Comic Mode".
- Natural-language cues: a voiced episode for video with panels, bubbles or a comic look; an audio drama with pictures; a motion comic; "script this for voice and images". The request must be *for* a voiced, illustrated piece.
- A request for a printed or scrolled comic goes to Comic Panel Writer. A live-action or animated film scene with no audio-first workflow goes to Cinematic Scene Writer. A voiced motion comic uses this pack, with Comic Panel Writer as an optional dependency for drawability and page jobs.

## Skip conditions

- Prose, print comics or screenplays with no voiced track.
- Stories *about* radio actors, podcasts or recordings. Vocabulary alone never activates the pack.
- Mixing, image generation, animation or upload tasks with no writing in them. Those belong in the user's production notes.
- In FAST_SCENE, a single line of dialogue or one panel caption doesn't need the episode contract. A scene does need the audio-first method and, if a power acts, its signature.

## Pipeline position

```text
planning packs → Intent Lock → Story Genome → scene design
→ [episode contract → power signatures → illustrated audio script → screen-off check]
→ (audio is recorded and locked outside the skill)
→ [screen-page board → audio-visual audit] → continuity → revision
```

The script and the board are separate passes. The board is written only after the audio exists, or against explicitly proposed timings labelled as such.

## Inputs

- Intent Lock: runtime target, whether the episode stands alone or is one part of several, the episode's own look matched to its lead, darkness ceiling, voice count.
- Character and world state. For each powered character, the facts about how the power works. Read them; never reconstruct them from how the power looks or sounds.
- Scene contracts or outline.
- For boarding: the locked audio's timings (spotted lines, SFX and silences) and the measured runtime. With no measured audio, timings are proposals.

## Outputs

1. **Episode contract**, in planning: runtime budget, beat map, installment question, voices.
2. **Power signature** for every powered character who acts on the page, before any script that uses them.
3. **Illustrated audio script** (register `illustrated_audio_script`): the recordable radio play with sound, music, silence and picture cues.
4. **Screen-page board** (register `screen_page_board`): pages, panels, shot scale and reason, lettering, and the time each panel holds, all timed to the locked audio.
5. **Audio-visual audit** (register `audio_visual_audit`): the self-check run on an existing script or board.

## State

- **Uses:** `intent_lock`, `characters`, `world`, `setups_payoffs`, `open_loops`, scene contracts.
- **Produces:** `pack_state.illustrated-audio-drama.episode`, `.power_signatures`, `.beats`.
- **Power physics is world fact.** A power's mechanism, range, perception and counters are written to `world` (or the character's record) with provenance. The signature keeps the *expression* and *story function* and points at that fact. When the Tragic engine is active, its `power_cost_card` holds costs and counterplay; the signature references it instead of copying it.
- **Open loops mirrored:** the installment's open question and any power rule not yet decided, with `pack` and `ref`.
- Everything invented (a power's rule, a cue, a look) is `agent_proposal` until the user approves it or delegated the decision.

## Procedure

### 1. Episode contract and beat map

Set the runtime budget from the user's target. **Default beat map for a ten-minute standalone episode**, as targets the episode may override: [@iad-owner-rulings]

| Time | Beat | Job |
|---|---|---|
| 0:00–0:40 | Cold open | One strange image, one question. No logo or recap before it |
| 0:40–1:00 | Title | Episode name |
| 1:00–3:00 | Setup | Who, where, and the rules of the problem |
| 3:00–5:00 | Investigation | Evidence, and the characters' differences showing |
| ~5:00 | Midpoint turn | A reveal that changes what the problem is. A natural ad-break point |
| 5:00–7:30 | Escalation | It costs something and becomes personal |
| 7:30–9:00 | Climax | Settled by a choice that says who the character is, not by power alone |
| 9:00–10:00 | Resolution and sting | It closes; one image opens a door |

An episode that needs a different shape keeps the **jobs** instead of the clock: an opening promise, a first action that can't be undone, a midpoint that redefines the problem, the climax's workload, the aftermath it needs, and an optional serial sting. [@iad-claude-codex-merge]

**Budget:** measure the spoken-word rate from the user's own recorded episodes when available. Without a measurement, about 130 spoken words a minute with pauses and sound is a working estimate, so ten minutes is roughly 1,300–1,400 words. Three to five speaking voices keeps them distinct.

**Parts:** a multi-part story may end on a cliffhanger, but each part first settles its own active question or confrontation, lands a consequence, and only then opens the next danger.

### 2. Power signatures

Write one card for each powered character before scripting their scenes. Two halves:

**How it works** (the mechanism, medium-neutral). What actually happens; its source and transmission; range and targeting; onset, duration and recovery; whether it can fire involuntarily; how many targets at once; who perceives what (the user, the victims, bystanders, animals); what physically changes and what is only perceived; what a microphone or camera records; what evidence it leaves; and what can and **cannot** block it. [@iad-owner-rulings]

**How it shows** (the expression): an audience warning before it acts, the sound transformation, the comic-language transformation, a version that survives a phone speaker or mono, an equivalent for viewers who can't hear it, and the escalation saved for the climax. Give each character **owned devices**, effects nobody else in the series uses, so a listener knows whose power is acting from the sound alone. [@iad-codex-plan-2026-11-23]

Comic-language transformations that work: a bubble tail pointing off-panel or at the wrong person; the power-user's lettering appearing inside a victim's bubble; the same panel repeated with one detail changed; gutters narrowing, cracking or breaking; sound lettering crossing panel borders; a page splitting or bending.

**Growth.** Record the power's default, specific effects and how it can grow. A power may start narrow and later produce new effects, but each new effect branches from the power's type: it is a variation the type could plausibly produce, not an arbitrary new ability. Note what drives growth (training, emotion, strain, time) and which effects are already established in canon. [@iad-owner-rulings]

**Intensity is set per episode.** How menacing, uncanny or out of control a character's power feels is an intent setting for this episode, not a constant. Keep every effect at or below that ceiling. A loss-of-control set piece is one possible escalation, not a requirement: an episode may hold it back for a later part, or leave it out. [@iad-owner-rulings]

Triggers, warnings and weaknesses fit the character. An emotional trigger, a discoverable weakness and an audible tell are common, but a trained ability may have a tactical trigger, and a weakness may be a plain limit.

**Removal test.** Delete every power effect from the script. If the plot is unchanged, the power failed. Each use should do at least one of: solve an immediate problem, create a worse one, reveal who the character is, force a choice. [@iad-codex-plan-2026-11-23]

**Mechanism test.** For every use and every counter, check it against how the power works, including its growth rule: a new effect that doesn't branch from the power's type fails. Never derive a defence from the power's surface look. If a power acts on the *perception* of sound inside the brain, air does not move: earplugs and hearing aids do not block it, a microphone records nothing, and a deaf character may still "hear" it. Counterplay follows from transmission and targeting, for example line of sight, range, concentration, or the user's own cost. [@iad-owner-rulings]

### 3. The illustrated audio script

Write the radio play first, complete and recordable.

- **Format:** speaker name, then the line, with short delivery tags in brackets. Separate cue lines for `SFX:`, `MUSIC:`, `SILENCE:` (with a length) and `PICTURE:` (a brief note of what the image must show). Mark special voice treatments (for example `(THROWN)`, `(PHONE)`, `(INSIDE HER HEAD)`) so the mix knows.
- **Write for the voice engine.** If the text-to-speech engine may read bracket tags aloud, keep tags to one to three words and drop any it speaks. Write acronyms as spaced letters ("F. B. I."), numbers as words where pronunciation matters, and non-English lines in their native script with a translation note. [@iad-owner-rulings]
- **Speakers without "said".** Distinguish voices through objective, rhythm, vocabulary, address and action sounds (keys, a cane, a lighter), and by names used only where a person really would use them.
- **Make space audible.** Every change of place or time must be announced in sound or speech well enough for a listener who isn't looking: ambience, a door, a time caption read aloud only if necessary.
- **Silence is authored.** Distinguish written silence, ambience dropping out, a character's changed perception, and a gap. Silence before a loud moment is what makes it loud.
- **Every plot-critical sound needs a mono-safe core.** If spatial audio (a voice behind you on headphones) is the only clue, add a vocal, rhythmic, lettering or reaction cue.
- **Darker scenes only when the story calls for them.** The episode's tone and look follow its lead, not a channel-wide grade.

### 4. Show, don't confess

Story comes out through action, sound and picture, and through characters confronting each other, not through someone explaining to a listener. [@iad-owner-rulings]

A motivated briefing can still be a lore dump, so test the **sequence**, not the line: [@iad-claude-codex-merge]

1. Why must the speaker give or get this information **now**?
2. What resistance, risk, bargain, lie or status fight shapes how it comes out?
3. What does the listener do differently because of it?
4. Could evidence or a consequence (footage, an object, a mistake, damage) let the audience work it out first?
5. Does later dialogue restate what the scene has already proved?

If information changes no immediate interpretation, tactic or choice, defer it. Narration may explain only when screen-off comprehension really needs it, and never to restate what the picture or the action already showed.

### 5. Screen-page board

After the audio is locked, board it.

- **Pages.** 16:9 screen pages, panels revealed one at a time, the camera guided from panel to panel. Each page has one dominant job (Comic Panel Writer's page jobs apply).
- **Each beat assigns jobs.** Audio carries time, voice, action or causal fact; picture carries space, expression, evidence, contrast or withheld information. Duplicate on purpose only, for emphasis, accessibility or a hard transition. Picture and audio may also work against each other: one answers a question while the other raises one.
- **Shot plan with reasons.** Give every materially specified shot a scale and a reason: establishing, wide, medium, close, extreme close, insert, over-the-shoulder, low angle, high angle, POV, reaction, two-shot; reasons such as orient, isolate, reveal, threaten, intimacy, consequence, perception change. Close and far shots and held cinematic beats appear "from time to time", where the story earns them. Unspecified framing stays open for the artist. [@iad-owner-rulings]
- **Expressive layout answers pressure.** Angled gutters, splash pages, broken frames, insets and repeated-panel strips mark impact, revelation, power states and emotional rupture. A power's owned layout devices appear only when that power acts.
- **Lettering is separate from art description**, so either can change without redoing the other.
- **Panels hold as long as the audio, the lettering, comprehension and the intended emotional hold need.** If the picture exposes an action the listener can't follow, fix and re-lock the audio. Don't patch it with narration.
- **Composition borrowed from manga** (its framing and pacing, not its drawing style). [@iad-manga-mapping]
  - **Frame by how much the panel shows:** several characters, one character, less than one (a hand, an eye, an object), or no character, only the place. Comics corpora find manga gives far more of its panels to single characters than mainstream American comics do, individuating people and parts of a scene rather than showing the whole scene. Make one-character and detail panels the everyday default, and save group panels for when the relationship between people is the point. [@cohn-2012-framing]
  - **Subjective panels** show what a character perceives. Manga uses them more, most often as close-ups and environment views. They suit powers: one panel shows what the victim perceives, the next shows what is actually there. [@cohn-2023-subjectivity]
  - **Look around one moment.** Before a big beat, a short run of panels on different aspects of the same instant (the snow, an ear, a finger, a smile), held over one sustained sound, stops time. [@mccloud-transitions]
  - **Silent beats (ma).** Panels segment time, and a wordless panel holds a pause. Write them as `SILENCE:` cues with a held image: after an important line, before a reveal, after a hit. [@natsume-panels] [@globalcomix-manga-paneling]
  - **Every page change is a page turn.** On a screen, the last panel of a page can pose the question (a door, a look off-panel, a sound with no source) and the next page opens on the answer. Put the midpoint twist on one.
  - **One focal panel per page**, sized by importance, with smaller panels feeding it; the camera holds longest there. Contrast in panel size and shape compresses and releases tension. Bleed to the frame edge for awe or shock; angled panels for speed and tension, straight ones for calm. [@globalcomix-manga-paneling] [@natsume-panels]
  - **Decompress what matters.** Spend panels on the decisive moments; a journey can be one establishing panel and a sound cue.
- **Shorts.** Optionally mark 30–60-second sequences that have their own setup, turn and button. Never bend the episode to make them.

### 6. Lettering by voice type

House conventions are examples, not laws. Keep each one consistent within a series.

| Voice | Usual treatment |
|---|---|
| Speech | Rounded bubble, tail to the speaker |
| Off-panel | Tail runs out of the frame toward the speaker |
| Narration | Caption box, never a bubble |
| Whisper | Lighter or dashed outline, smaller lettering |
| Shout | Spiked outline, bold lettering |
| Phone, radio, recording | Jagged or boxed balloon, electric tail |
| Inner voice or telepathy | A distinct shape, colour or font owned by that link |
| Thrown or false voice | Tail to the wrong place, or no source at all |
| Power-owned lettering | A colour or font only that character uses; inside a victim's bubble when they're controlled |
| Another language | Choose how the audience understands: translation, context, another character, or deliberate opacity |
| SFX | Lettered into the art; crosses panel borders only for impact or a power |

Crowding warnings for the screen, where the audio sets the pace: about 15 words in one bubble, two bubbles on screen at once, or subtitles, bubbles, captions and SFX competing for the same few seconds. Inherit Comic Panel Writer's reading-order rule.

### 7. Self-check

Run at the critic step and as the `audio_visual_audit` register.

- **Removal test** and **mechanism test** for every power use and counter, including growth.
- **Intensity:** every power effect stays within this episode's ceiling; no escalation the episode didn't plan.
- **Confession scan** with the five sequence questions.
- **Screen-off check:** with eyes closed, can a listener follow who speaks, what happens, where and when?
- **Picture adds:** does each page add evidence, space, reaction, irony or withheld information?
- **Warnings, each to confirm or fix:** most panels in a scene are group shots; a tense scene with no detail panel; a scene with no silent beat; a page that ends without a question or a focal panel; six similar talking-head shots in a row; a scene with no far shot or no close shot; three plain grids in a row with no size change ("too basic"); every page loud (expressive layout everywhere); a power device used by the wrong character; a clue that lives only in headphone audio; lettering crowding.
- **Budget:** spoken words against the runtime; voice count.
- **Look:** the episode's look matches its lead; darkness is where the story calls for it.
- **Contract:** the installment lands a consequence and settles its own question before any sting.

## Guardrails

- The user's rulings about a power's mechanism are canon. Never "improve" a power by changing how it works to make a scene easier.
- Never let a power win the climax alone; the deciding move is a choice.
- Don't put production settings (loudness, image models, prompts, credit costs, engine syntax) in scripts as if they were writing. Point to the user's production notes.
- Don't impose the default beat map or the warning counts over the user's stated form.
- Loud moments come from contrast, never from asking for harmful levels; avoid writing rapid flashing into picture cues.
- Keep invented facts labelled as proposals.

## Failure modes

| Failure | Looks like | Fix |
|---|---|---|
| Decorative power | Spectacular distortion, unchanged choices | Make the effect cause an action, error, cost or irreversible decision |
| Surface-mechanism defence | Earplugs block a power that acts in the brain | Derive counterplay from transmission and targeting |
| Plausible briefing dump | A contractor patiently receives the world's history | Show operational evidence; keep only what changes the assignment |
| Motivated recap | Reasonable questions whose answers explain what viewers already inferred | Let the evidence change a choice; cut the summary |
| Picture karaoke | Every image shows exactly what the dialogue says | Give the picture evidence, contradiction, reaction, geography or subtext |
| Audio dependent on picture | "He uses it" while the object exists only on screen | Name or sonically establish the object before it matters |
| Headphone-only clue | Spatial audio carries the only proof | Add a mono-safe vocal, rhythmic, lettering or reaction cue |
| Layout wallpaper | Cracks, diagonals and broken frames on every page | Reserve rupture for a defined pressure or power state |
| Too basic | Page after page of equal rectangles and medium shots | Vary scale and panel size where the story turns; earn one bold page |
| Spoken tags | The engine reads "[with mounting dread and sorrow]" aloud | One-to-three-word tags; move direction to the voice notes |
| Whole-scene framing | Every panel shows everyone in the room | Isolate one person or one detail; keep group panels for relationship beats |
| Random growth | A power suddenly does something unrelated to its type | Branch the new effect from the power's type, or cut it |
| Unplanned escalation | Every episode ends with the power going out of control, or a character reads creepier than intended | Hold effects to this episode's intensity ceiling; save the set piece |
| Cliffhanger without a landing | Part one stops mid-fight | Settle this part's question, land a consequence, then open the next |

## Schemas

```yaml
pack_state:
  illustrated-audio-drama:
    episode:
      target_runtime_seconds: 600
      words_per_minute: null        # measured from the user's audio when available
      voices: []
      beat_map: default_ten_minute  # or a custom list of beat jobs
      installment_contract:
        opening_promise: null
        question_closed_here: null
        consequence_landed: null
        question_left_open: null
      audio_only_required: true
      power_intensity: []           # per character: ceiling for this episode, escalation planned here or deferred
      visual_identity:
        lead_specific_look: null
        expressive_devices: []
        reserved_devices: []        # owned by one character or power state
```

```yaml
power_signature:
  character: null
  physics_ref: null                 # the world/character fact holding the mechanism
  physics:                          # mirrors the world fact; never overrides it
    actual_mechanism: null
    source: null
    transmission: null
    range: null
    targeting: null
    onset: null
    duration: null
    recovery: null
    involuntary: null
    simultaneous_targets: null
    perceived_by: []
    not_perceived_by: []
    physical_changes: []
    perceptual_changes: []
    recordings_capture: null
    residual_evidence: []
    blocked_by: []
    not_blocked_by: []
  growth:
    default_effects: []             # the specific effects established now
    power_type: null                # what new effects must branch from
    emergent_effects: []            # later effects, each with the branch it grew from
    growth_driver: null             # training | emotion | strain | time | other
  use_conditions:
    trigger: null
    cost: null                      # or a ref to the Tragic engine's power_cost_card
    limitations: []
    counterplay: []
  expression:
    audience_warning: null
    audio_transformation: null
    comic_transformation: null
    owned_devices: []
    small_speaker_fallback: null
    accessibility_equivalent: null
  story_function:
    immediate_problem_changed: null
    worse_consequence_created: null
    character_revealed: null
    choice_forced: null
    climax_escalation: null
  provenance: agent_proposal
```

```yaml
audio_visual_beat:
  id: B01
  start_seconds: null
  end_seconds: null
  timing_basis: proposed            # locked_audio | proposed
  audio_job: null
  visual_job: null
  critical_fact: null
  understandable_audio_only: false
  page: null
  panel_function: null
  framing:
    content: null                   # macro (several) | mono (one) | micro (less than one) | amorphic (place only)
    subjective: false
    scale: null
    angle: null
    reason: null
  layout_device: null
  page_role: null                   # focal | feeder | hook | answer | silent_beat
  lettering:
    items: []
    reading_order: []
    crowding_warning: false
  power_use_ref: null
```

## Examples

Invented, generic material.

**Power signature (short).** Ines can place a voice inside a nearby person's hearing. No air vibrates, so microphones record silence and earplugs do nothing. She chooses a target by eye contact, within a room. Using more than one voice at a time makes her hear an old, uncontrollable memory: a woman humming. *Warning:* room tone narrows to nothing. *Comic:* her lettering is pale green, with no tail or a tail to the wrong place, and it migrates into a victim's balloon. *Small-speaker fallback:* the victim answers out loud. *Climax escalation:* she uses two voices at once and pays for it.

**Script excerpt.**

```text
SFX: Generator hum. Behind steel, a CHILD coughs.
GUARD: [bored] Clinic's closed.
SILENCE: 0.5 s. The generator drops out.
INES (INSIDE HIS HEAD): Evacuate Ward C.
GUARD: [into his radio] Ward C? Confirm.
SFX: The radio stays silent. A keypad. Bolts retract.
```

**Board (excerpt).**

```text
PAGE 3 · Job: the power changes the plot.
P1  WIDE, orient: the locked clinic door, the guard, Ines at the end of the corridor.
    Audio: generator hum, cough. Picture: where everyone is.
P2  EXTREME CLOSE, perception change: their eyes meet.
    Lettering: pale green, no tail: EVACUATE WARD C.
P3  MEDIUM, consequence: he answers an order nobody gave. His radio's light is dark.
    Picture carries what audio can't: no signal came in.
P4  INSERT, causal action: his thumb enters the code.
PAGE 4 · Job: the cost.
P1–3  REPEATED STRIP, escalation: the same frame three times, the guard further
      through the door each time. Her green lettering now inside his balloon:
      "Evacuating Ward C."
P4  CLOSE on the child, reveal: smiling at an empty corner. CHILD: "Mum?"
    Audio: a warm woman's hum. The power has reached someone she didn't target.
P5  BROKEN INSET, rupture: Ines freezes. She hears the hum too.
    Her green SFX crosses the gutter; the real alarm's SFX stays inside its panel.
P6  TWO-SHOT, low angle, choice: Ines steps into the light, hands raised.
    INES: "The order was false. The fire isn't."
```

Remove the power and the breach, the harm to the child and Ines's surrender all disappear: the removal test passes. The guard's radio is silent and nothing is recorded, so the mechanism holds.

## Behavior tests

| Fixture | Checks |
|---|---|
| F42 | A ten-minute illustrated audio drama activates this pack and the audio-first registers. |
| F43 | Prose about a radio actor does not activate it. |
| F44 | A brain-perception power is not blocked by earplugs; counterplay follows the mechanism. |
| F45 | A motivated briefing becomes contested evidence and choices, not a shorter speech. |
| F46 | A headphone-only spatial clue gets a mono-safe and visual fallback. |
| F47 | A part-one cliffhanger settles its own question and lands a consequence first. |

## Research provenance

See [research/packs/illustrated-audio-drama.md](../research/packs/illustrated-audio-drama.md). The pack is mostly a **design** module. Its rules come from a series owner's production rulings, a plan made with Codex and approved by the owner, and a Claude–ChatGPT collaboration that critiqued the first draft. The manga composition section (1.1) adds two corpus studies of comics framing (empirical, read via the article and an abstract), a translated essay on panel function (conceptual), and craft summaries of manga paneling and McCloud's transitions (conventions). Those describe tendencies in printed comics, not rules for screen boards. The beat map, word rate and crowding numbers are working targets, not tested laws.

## Integration

- **Core modules extended:** [scene-engine](../core/scene-engine.md) (every beat still has desire, resistance and change), [information-architecture](../core/information-architecture.md) (exposition routing becomes the confession scan; audio and picture are two channels of reveal), [dialogue](../core/dialogue.md) (subtext and tactics, written to be heard), [world-state](../core/world-state.md) (power mechanisms are world rules).
- **Comic Panel Writer** supplies the drawable test, page jobs and reading order; this pack owns timing and the audio-picture split. Use its `motion_comic_16x9` format.
- **Cinematic Scene Writer** is not stacked: its film runtime and screenplay format don't apply to locked-audio boards.
- **Tragic engine:** its `power_cost_card` is the cost half of a signature. **Horror:** its dread curve shapes warnings and silence. **Mystery:** a clue carried only by audio or only by picture must be fair in the channel the audience is using. **Series engine:** owned devices and episode looks stay consistent across installments.
