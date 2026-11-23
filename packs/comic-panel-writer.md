---
pack:
  id: comic-panel-writer
  name: Comic Panel Writer
  version: '1.2'
  stage: output
  pipeline_position: Drafting time, in place of plain prose output. After all planning.
  purpose: Write with comic-book visual logic, and produce page maps, panel breakdowns, full scripts,
    and lettering or pacing audits on request.
  triggers:
  - Comic Mode
  natural_language_triggers:
  - Panel this
  - Write as a comic
  - Comic script
  - Page breakdown
  - Make this read like a comic
  requires:
  - core/scene-engine
  optional_dependencies:
  - origin-forge
  - tragic-anime-engine
  - core/dialogue
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
  - illustrated-audio-drama
  inputs:
  - scene contracts or outline
  - origin_brief (optional)
  - tragic ledgers (optional)
  produces:
  - comic_project
  - page records
  - comic narrative or script output
  skip_when:
  - The user wants ordinary prose.
  - Planning-only requests.
  state_keys:
  - pack_state.comic-panel-writer.comic_project
  - pack_state.comic-panel-writer.pages
  research_basis: research/packs/comic-panel-writer.md
  behavior_tests:
  - F17
  - F18
  - F34
---

# Comic Panel Writer

Comic-book visual logic, with or without production scripting. An alternate output register for [the prose rules](../core/prose.md), not a planning stage.

Triggers: "Comic Mode," "Panel this," "Write as a comic," "Comic script." Default output: **Comic Narrative**, unless the user explicitly asks for pages/panels. Works with or without an Origin Forge pass behind it — see the bridge section near the end.

**Core rule:** a comic script is not prose cut into boxes. It thinks in visible moments, reading order, page/screen units, lettering space, visual emphasis, reveal timing, and collaboration with the artist. There is no one universal comics-script format — this pack is research-informed, not a publisher-submission guarantee.

---

## Output modes

- **A. Comic Narrative** — prose-first, for origin stories, lore, pitches, scenes before page count is known. Visually legible prose, iconic images, compressed action, memorable motifs, controlled heightened dialogue, dramatic transitions, issue-like scene endings. No page numbers required.
- **B. Page Map** — page-by-page job/anchor/turn-hook, before panel detail exists. Example:
  ```text
  PAGE 1
  Job: Establish Vale as a respected officer.
  Anchor image: Vale kneeling beside a frightened civilian while giving orders.
  End beat: Radio reports the suspected weapons platform.
  ```
- **C. Panel Breakdown** — pages + panel beats + key dialogue + page-turn notes, without final production prose.
- **D. Full Script** — artist-facing page/panel descriptions, dialogue, captions, SFX, lettering notes.
- **E. Lettering Audit** — crowded balloons/panels, redundant dialogue, unclear speaker order, caption overuse, missing breathing room, concise alternatives.
- **F. Visual Pacing Audit** — pages doing too many jobs, flat rhythm, premature reveals, unearned splashes, unclear geography, missing silence, motif opportunities.

Don't force production scripting when the user only wants a comic-book *writing style* — stay in Comic Narrative unless pages/panels are actually wanted.

**Voiced motion comics** (panels revealed on 16:9 screen pages and timed to recorded audio) go to [Illustrated Audio Drama](illustrated-audio-drama.md). That pack owns the audio-first script, timing and the audio–picture split; this pack still supplies the drawable test, page jobs, reading order and lettering space. Use `format: motion_comic_16x9`.

---

## Drawable test

For every panel: **can an artist draw this as one readable visual state?**

Bad: *"Marcus enters the room, notices the body, remembers his father, crosses to the desk, opens the drawer, and finds the gun."* — several sequential actions plus an invisible thought. Split it, or choose the one decisive image.

## One primary beat per panel

A panel can have complex composition but should have one dominant narrative function: establish, orient, action, reaction, reveal, impact, silence, detail, bridge, atmosphere, parallel, payoff.

## Visible vs. invisible information

Panel descriptions carry visible action, setting, expression/body language, important props, spatial relationships, story-critical framing. Internal information belongs in dialogue, caption, visual metaphor, or established context — not panel description.

---

## Panel visual grammar

- **Panel as selected state.** A panel freezes/presents one visual state; split into multiple panels if the reader needs distinct before/after information.
- **Gutter as inference.** The reader connects panels — use the gap to omit routine movement, obvious consequences, travel, minor transitions, repetitive action.
- **Transition functions:** micro (tiny shift in expression/time/position), action (one stage of an action to another), subject (attention moves between subjects in one scene), scene (jump time/place), aspect (move among details of environment/mood), associative (connect images through theme/symbol/memory/contrast).
- **Visual hierarchy.** Every panel: what should the reader notice first? Every page: which moment owns the most visual weight? If every panel is equally loud, nothing is loud.
- **Panel record**, for each panel: function, subject, visible action/state, must-show information, optional framing, lettering load, transition out.
- **Reaction panels** carry story — use for moral choice, relationship shifts, reveals, horror, humiliation, grief, recognition.
- **Detail panels** — use when an object or gesture changes interpretation: safety off, medal bent, ring removed, hand over authorization, blood on a clean glove.

---

## Page and spread architecture

**Give every page a primary job** — introduce location, establish relationship, compress decision, reveal threat, stage argument, deliver impact, show aftermath, pivot timeline, end scene. A page may do several things, but one job should dominate.

**Spread awareness (print):** adjacent pages are perceived together. Audit what's visible before reading, whether a large image pulls the eye too early, whether a reveal is visible before its setup, whether two dominant images compete.

**Page-turn engine:** before the turn, leave an unanswered question or incomplete image; after the turn, reveal/reverse/expand/contradict/escalate/recontextualize. Don't use the trick on every single turn. Vertical scroll replaces physical page-turn logic with scroll distance, spacing, blank space, and delayed reveal — no odd/even parity assumed unless the numbering scheme is actually known.

**Splash logic:** earns space for scale, entrance, reveal, awe, emotional arrest, location spectacle, title imagery, transformation. Expensive real estate — don't spend it just because a moment is cool.

**Density variation**, useful patterns: dense argument → silent large panel; regular grid → broken impact panel; wide establishing panels → tight reactions; repeated micro-panels → sudden open space.

---

## Dialogue and lettering

- Dialogue must coexist with art. If it's heavy: simplify the image, split the beat, shorten the line, move exposition elsewhere, or use narration only if narration is genuinely the right tool.
- **Soft density warnings** (inspection thresholds, not laws): ~25 words in one balloon; ~50 total words in one panel; 4+ balloons in a small panel; a long speech over complex action. Tolerate less text when the image is visually complex.
- **Balloon rhythm:** one strong line beats three explanatory ones. Split balloons for thought/interruption/pause/vocal-rhythm changes, not to game a word count.
- **Reading order:** letter in the order the reader should encounter it; composition needs room for the first speaker's balloon to actually read first.
- **Captions**, used deliberately: location/time, internal monologue, spoken/off-panel, narrator/editorial voice. Not a default rescue for unclear art.
- **SFX** for impact, rhythm, environmental texture, transition, motif — don't label every noise.

---

## Action, silence, montage, time

- **Action goal first.** Before scripting punches: who wants what, what blocks them, what space matters, what changes if they fail. Action without objective is motion wallpaper.
- **Geography:** entrances/exits, vertical levels, hazards, distance, objective, important props, civilians/allies — re-establish after major disruption.
- **Beat chain:** anticipation → commitment → contact/impact → consequence → reaction. Don't automatically show all five.
- **Superpowers:** track readable setup, visual rule, limitation, counterplay, collateral effect, signature shape/behavior — the reader should understand enough to anticipate possibilities. A power can also change the comic language itself: bubble tails pointing the wrong way, the user's lettering inside a victim's balloon, repeated panels, cracking gutters. Give those devices to one character only, and use them only when the power acts. If removing the power's effects leaves the plot unchanged, the power is decorative.
- **Silence** carries grief, intimacy, awe, dread, aftermath, choice, recognition, hesitation. If every panel has dialogue, audit whether the art is being allowed to speak.
- **Montage** needs an organizing principle: repeated object, pose, calendar, headlines, costume evolution, training failures, locations, relationships, public reaction.
- **Time compression** via captions, repeated compositions, environmental change, costume/hair progression, weather, changing light, object wear — not only "THREE MONTHS LATER."
- **Parallel cutting**, especially useful for origins: public story vs. private truth; hero prep vs. villain prep; rescue vs. cover-up; two characters making opposite choices.

---

## Panel description house style

```text
PANEL X
Concise visual description.
Story-critical information.
Optional framing only when meaningful.
Lettering in intended reading order.
```

Optional labels: `MUST SHOW:` (plot/continuity-critical visual fact) · `SUGGESTED:` (composition/framing idea the artist may improve) · `DESIGN NOTE:` (recurring object/costume/interface information) · `LETTERING NOTE:` (special treatment or reading-order need). Don't micromanage every camera angle or pose.

## Full script format

```text
PAGE 1 (5 PANELS)

PANEL 1
Description...

CAPTION:
Text...

CHARACTER:
Dialogue...

SFX:
Sound...
```

Rules: start each page clearly; number every panel; include panel count in the page heading; keep descriptions concise but sufficient; list lettering in intended reading order; use MUST SHOW for continuity-critical details, SUGGESTED for optional framing; protect page-turn reveals; warn when lettering likely crowds the art; avoid invisible information in panel description; keep sequential actions out of one panel unless deliberately shown as montage or multiple exposure.

---

## Artist collaboration

The writer controls story, required information, dialogue, timing needs, continuity, reveal logic. The artist retains freedom over staging, acting, composition, and camera choice unless a specific choice is necessary to the story. Write enough to make the page producible — not enough to suffocate it.

---

## Integration with Origin Forge

Origin Forge supplies the transformation logic (`packs/origin-forge.md`); this pack gives it visual timing.

- **Before Self** — one iconic competence image, one relationship beat, one value-in-action beat. Avoid biography montage unless needed.
- **Disruption** — enough geography and information to understand the decision, then the choice, then the consequence.
- **Meaning Crisis** — reactions, institutional response, motifs, selective captions, silence. Not a speech explaining the whole psychology.
- **Second Test** — a real alternative, structured visually. The reader should understand another path existed.
- **Chosen Crossing** — give the decision visual weight: large panel, silent beat before action, page-turn reveal, or a callback to the original event.
- **Transformation** — separate receiving power, mastering power, and choosing identity, unless collapsing them helps.
- **Identity Claim** — one image that could plausibly become a cover, poster, or recurring icon. Doesn't require an actual splash page.

---

## Schemas

```yaml
comic_project:
  version: "1.0"
  title: null
  format: null            # print_issue | graphic_novel | digital_paged | vertical_scroll | motion_comic_16x9 | unknown
  reading_direction: "left_to_right"
  target_page_count: null
  output_mode: "comic_narrative"
  visual_language: { tone: [], motifs: [], recurring_images: [], design_constraints: [] }
  pacing: { default_density: "medium", page_turn_strategy: "opportunistic", splash_policy: "earned" }
  lettering: { dialogue_density: "medium", balloon_word_warning: 25, panel_word_warning: 50 }
  collaboration: { artist_freedom: "high", mark_required_visuals: true }
  source_material: []
  canon_constraints: []
```

```yaml
page:
  page_number: null
  spread_position: null        # left | right | single | unknown
  page_job: null
  dominant_emotion: null
  visual_anchor: null
  target_panels: null
  word_load: null              # low | medium | high
  last_image_function: null
  page_turn_boundary_after: false
  hidden_reveal_next: null
panels:
  - number: null
    function: null
    description: null
    must_show: []
    suggested_framing: null
    continuity: []
    lettering: { items: [], estimated_word_count: 0 }
    transition_out: null
    crowding_warning: false
    drawable_warning: false
```

---

## Production checks

Regression fixtures: [F17](../tests/fixtures/F17-comic-panel-is-drawable.yaml), [F18](../tests/fixtures/F18-page-turn-reveal-protected.yaml), [F34](../tests/fixtures/F34-comic-villain-origin.yaml).

**Visual:** every panel drawable? one dominant beat per panel? invisible information moved to lettering/context? required props/characters visible?
**Reading order:** speakers ordered clearly? captions/dialogue/SFX in intended order?
**Page:** primary job present? one image given appropriate weight? final beat intentional?
**Reveal:** a surprise visible on the current spread before it should be? page-turn boundary actually known, or marked as opportunity rather than hard-coded parity?
**Lettering:** any balloon near/over 25 words, or panel near/over 50? does a visually complex panel need even less text? does dialogue repeat the art?
**Action:** geography established? objective clear? cause and consequence readable? every movement worth a panel?
**Rhythm:** too many same-size/same-function panels in a row? room for silence? splashes earned? density varying with story importance?
**Collaboration:** artist instructions story-critical, not over-directing? optional choices marked as suggestions?

---

## Worked example (generic demo, shared with Origin Forge's Major Vale seed — not project canon)

**PAGE 6** — Job: establish what Vale knows and how little time he has. Target 5 panels. Turn strategy: end on the decision, not the explosion.

```text
PANEL 1
Wide command room. Tactical map dominates. A civilian evacuation
corridor and a suspected hostile vehicle overlap.
MUST SHOW: Vale can see the civilian route.

PANEL 2
Close detail: a confidence indicator reading 71%.
ANALYST: Signal match is degrading.

PANEL 3
Vale looks to a live drone feed. Clouds and interference obscure the convoy.
VALE: Visual confirmation?
ANALYST: Negative.

PANEL 4
A subordinate points to the city icon beyond the corridor.
SUBORDINATE: If it clears the pass, we lose interception range.

PANEL 5
Vale's hand over authorization. No dialogue for a beat.
VALE: Authorize.

PAGE TURN.
```

**PAGE 7** — Job: consequence. Target 3 panels.

```text
PANEL 1
Large panel. The strike hits the convoy. Through the fireball, one
vehicle is visibly marked with the friendly reconnaissance identifier.
No dialogue.
SFX: KRAAAM

PANEL 2
Command room. Nobody moves.

PANEL 3
The analyst stares at new data.
ANALYST: Sir...
```

The sequence ends before the full casualty report — the reader understands uncertainty, civilian risk, catastrophic stakes, and Vale's personal authorization, and the page turn protects the consequence from being seen before the choice lands.

---

## Research provenance

Script-format, pacing, page-turn, and lettering guidance comes from publisher guides, a professional script archive, and practicing letterers and cartoonists. Word-count thresholds are warnings, not publisher rules. Details: [research/packs/comic-panel-writer.md](../research/packs/comic-panel-writer.md).
