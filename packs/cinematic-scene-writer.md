---
pack:
  id: cinematic-scene-writer
  name: Film and Music Video Scene Writer
  version: "1.0"
  stage: output
  pipeline_position: At drafting after scene design; before continuity and revision checks.
  purpose: Turn story beats into performable film scenes or timed music-video scenes, with meaning notes separate from screen action.
  triggers: ["Screenplay Mode", "Music Video Script"]
  natural_language_triggers: ["write a movie scene", "rewrite the music video script", "full cinematic scenes with meanings and times"]
  requires: [core/scene-engine, core/information-architecture, core/continuity]
  optional_dependencies: [core/dialogue, core/reader-state, core/research-mode]
  conflicts_with: []
  stacks_with: [mystery, horror, romance, series-engine]
  inputs: [user intent, source material, scene contracts, audio identity and timing when supplied]
  produces: [screen scenes, music cue map when relevant, optional separate intention notes]
  skip_when: [software script requests, movie reviews without a writing request, prose scenes merely described as cinematic]
  state_keys: [pack_state.cinematic-scene-writer]
  research_basis: research/packs/cinematic-scene-writer.md
  behavior_tests: [F36, F37, F38, F39, F40, F41]
---

# Film and Music Video Scene Writer

## Purpose

Translate narrative design into action that can be staged, photographed or animated. Distinguish a beat outline, treatment, screenplay, director's script and shot list. A request for full scenes receives the scenes, not an expanded checklist of intended events. Music-video timing is a second constraint alongside drama; neither page count nor cut count establishes running time.

## Activation

Use for writing or revising movie scenes, screenplays, narrative music-video scripts, timed visual treatments, or a director's script with cinematic action and meaning notes. Choose `screenplay` for conventional film pages, `music_video_script` for a fixed-track script, and `cinematic_treatment` for scene prose with directing notes. These are output registers, not new genres.

## Skip conditions

Skip for code scripts, video-player implementation, reviews that request no writing, or literary prose that happens to be cinematic. Do not turn a request for one scene into a production bible. Do not assume a band-performance segment, dialogue, lyric illustration or narrative plot is mandatory in every music video. [@caston-music-video-forms]

## Pipeline position

Read intent, canon and scene contracts first. Draft in the selected screen register. Review cause and consequence, audience information, timing, and only then language. A separate shot list or animatic follows only when requested. Genre packs may shape the story; this pack shapes its delivery.

## Inputs

- Existing draft and the user's specific dissatisfaction, including any rejected structure.
- Source authority, characters, world rules, ending constraints and proposals.
- Film format and intended viewer experience; infer reversible presentation choices.
- For fixed music: exact master/version, duration, supplied lyrics, section map, cue evidence and any offset uncertainty. Missing measurement does not authorize invented exact cues.

## Outputs

The requested scenes come first. For a multi-page timed script, give navigable scene pages with start/end/duration, scene headings, complete present-tense action, and entry/turn/exit. Add direction and meanings when requested, clearly separated from what is shown. Supply a compact timing map and source/assumption note. A machine-readable cue sheet is useful when it supports validation; it is not a substitute for the screenplay.

## State

- **Uses:** scene contracts, timeline, characters, information items and setups/payoffs in core state.
- **Produces:** `pack_state.cinematic-scene-writer` holds format, timing evidence, scene ranges, visual motifs and presentation decisions only. Do not duplicate character canon here.
- **Open loops mirrored:** unresolved identity, chronology or story mechanics go to `open_loops` with `pack` and `ref` when a workspace exists. Otherwise retain them in the project's normal draft notes. Do not create a workspace unasked.
- Every invented story event remains `agent_proposal` unless approved or delegated.

## Procedure

1. **Choose the document contract.** A treatment describes the viewing experience; a screenplay dramatizes it; a director's script may add essential framing; a shot list divides it for production. For annotated pages, say that page count is a reading format, not a duration estimate. Conventional screenplay formatting is useful for conventional screenplay requests, not a reason to suppress requested annotations. [@academy-screen-format]
2. **Find each scene's necessity.** What must become different, what disappears if the scene is removed, and who needs to be present? Use the core scene engine for desire/resistance/change. Consider an alternate entry before committing. A musical section may contain multiple scenes; one dramatic scene may span sections. [@august-scene-process]
3. **Rehearse the event mentally, then write it.** Know where the bodies and important objects begin, who looks where, how the attempt meets resistance, and what makes someone adapt. Write concrete behavior in present tense. Use short paragraphs for successive visible developments. “She realizes he lied” needs perceivable evidence and a response; “we see” is not intrinsically wrong. A silent film still needs performance, not explanatory captions pasted onto a plot summary.
4. **Allocate music time by dramatic workload.** Inventory cue evidence as measured, MIDI/arrangement-derived, listened, source-note claim, or proposed. Allocate an interval to the action and check that the physical work fits. Name strong musical anchors separately from movable internal beats. Do not invent lyrics or call a MIDI note audibly prominent without evidence. [@screen-time-ledger]
5. **Make the music-image relationship deliberate.** Choose when movement follows pulse, when a reveal meets a structural change, and when an image holds across beats. Energy can change through blocking, scale, motion within frame, density, or editing. Faster cutting alone may conceal rather than dramatize a change. Stage escalation around the track when useful; continuous choreography can also be highly active. [@usberghi-sanctuary] [@schroder-pille]
6. **Control what the audience can infer.** Extend core information items into visible setups and returns. Track who can recognize an object or gesture and why. Repetition should retain or change a specific relationship, not just provide decorative motifs. A visual match across eras does not establish literal simultaneity. Meanings are possible readings or authorial intentions, not facts every viewer must accept. [@screen-time-ledger]
7. **Protect the song's emotional subject.** Develop the artist's requested interpretation rather than importing a reference video's story. Symbolic or associative scenes can complement narrative scenes. A recurring image can organize a film without literal lyric illustration. [@adin-mcnally-rocket-man] [@frost-prelude]
8. **Separate layers on the page.** Put playable action first; put “Intended meaning,” camera/staging and timing notes below or on a facing page. Do not make silent characters communicate an essay. Do not put interpretive notes in spoken dialogue or on-screen text unless intended.
9. **Revise and verify.** Read only the action: does the film still make sense? Read only scene exits/entries: does momentum carry? Verify spatial continuity, character knowledge, reveal timing, physical duration, and full master coverage. If rendering a PDF, inspect actual pages. Discuss later thumbnail/animatic testing as a next stage, not proof that written timing is already performed. [@adin-mcnally-rocket-man] [@schroder-pille]

## Guardrails

Preserve source writing and music. Keep uncertainty about canon, measurement and interpretation visible without repeating a warning on every page. Do not default to a rigid act formula, a fixed number of scenes, cuts on every beat, or mandatory conflict in a deliberately observational film. Do not confuse more adjectives, camera jargon or symbolism with a fully dramatized scene. When a user changes direction from animation to writing, complete the writing; do not restart production automatically.

## Failure modes

| Failure | Looks like | Fix |
|---|---|---|
| Outline disguised as scene | “They investigate and discover the truth” | Write the actual test, result and changed behavior. |
| Meaning replaces action | Paragraphs of theme with no visible event | Give the theme a choice, object or consequence; keep its interpretation separate. |
| Cut-count pacing | Dozens of tiny shots without new information | Budget complete attempts and reactions; vary density where it matters. |
| Hidden knowledge | A stranger recognizes an unseen historical gesture | Plant how the gesture survived and was learned, or remove the recognition. |
| False timing precision | Exact musical hits inferred from prose notes | Label proposed cues; measure the master and identify the evidence actually inspected. |
| Format dogma | Every music-video page forced into a one-minute estimate | Use explicit seconds; label annotated/director formats honestly. |

## Schemas

This extends, rather than replaces, `scene_contract` and core information items.

```yaml
pack_state:
  cinematic-scene-writer:
    register: music_video_script
    timing:
      master: user-supplied-track.wav
      duration_seconds: 120
      basis: measured
      offset_seconds: 0
      offset_status: proposed
    scenes:
      - id: S01
        scene_contract_ref: S01
        start_seconds: 0
        end_seconds: 20
        heading: EXT. FERRY LANDING - DAWN
        entry_image: A bicycle wheel spins above a missing plank.
        visible_turn: The rider abandons the bicycle to take the child's hand.
        exit_image: Two pairs of muddy shoes reach the ramp.
        music_relationship: Hold the choice across the phrase; cut when both feet land.
        cue_basis: proposed
        intended_meaning: Responsibility changes the rider's priority.
        meaning_status: authorial_intention
        provenance: agent_proposal
```

## Examples

**Outline:** A courier misses a ferry and learns to help someone.

**Scene:** EXT. FERRY LANDING - DAWN. The courier throws a bicycle onto the ramp. Its front wheel clears the gap. Behind her, a child has a suitcase caught between two boards. She puts one foot on the bicycle pedal. The ferryhand begins lifting the ramp. She takes the foot off, lets the bicycle fall against the rail, and pulls the suitcase free. The child reaches for her hand before either of them moves. They run together. The bicycle remains on the landing.

**Separate intention:** The changed priority is visible in the abandoned bicycle. Whether the audience calls this generosity or an impulsive mistake can remain open. For a timed version, allow the obstruction, choice and assisted run enough seconds; a requested 4-second slot would require simplifying the event or showing only its decisive beat.

## Behavior tests

| Fixture | Checks |
|---|---|
| F36 | Full scene output, performable turn and separated meanings. |
| F37 | Fixed master coverage, tail and cue uncertainty. |
| F38 | Software/nonfiction look-alikes do not activate. |
| F39 | Music intensity changes without compulsory beat cuts. |
| F40 | Recognition and visual matches respect knowledge and chronology. |
| F41 | Original film/performance format intent wins over pack defaults. |

## Research provenance

See [research/packs/cinematic-scene-writer.md](../research/packs/cinematic-scene-writer.md). Sources are professional craft accounts, a format guide, and historical research. The timing ledger, annotation design and tests are pack design, not empirically proven universal laws. No embedded reference videos were watched for this update; interviews and text sources were read.

## Integration

Extends [scene-engine](../core/scene-engine.md), [information-architecture](../core/information-architecture.md) and [continuity](../core/continuity.md). Mystery keeps a fair evidence trail; horror controls disclosure; romance supplies relationship behavior. Those packs do not impose their ending conventions over user intent. Comic pagination rules do not transfer to film runtime. Research limits remain in [research-mode](../core/research-mode.md).
