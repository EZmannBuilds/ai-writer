# Router

The router decides **what to load and in what order** for a request. It runs silently at the start of every fiction task. Its output is a `route`: the task, the mode, the packs, the core modules, the output register, and the questions worth asking.

The router's goal is the correct machinery, not the maximum. A module or pack loads because it solves the current problem, not because it exists.

```yaml
route:
  task:            # see Task classifier
  stage:           # seed | planning | drafting | continuing | revising | critiquing
  mode:            # FAST_SCENE | SHORT_STORY | LONG_FORM | CRITIC | REVISION
  research:        # none | triage | required   (research mode is an overlay, not a mode)
  state_source:    # workspace | context | none
  packs: []        # pack ids, in pipeline order
  core: []         # core module ids to load now
  register:        # prose | comic_narrative | comic_page_map | comic_panel_breakdown | comic_full_script | plan | critique
  ask_user: []     # only genuinely consequential forks; usually empty
  authority:       # guided | collaborative | autonomous  (who may make creative decisions)
```

Show the route to the user only when they ask, or as a one-line note at the top of a planning response. Never pad a scene request with routing talk.

---

## Precedence

When signals disagree, the higher line wins.

```text
1. The user's explicit instruction in this conversation
   ("skip planning", "just write it", "don't make it tragic", "use Comic Mode")
2. An explicit trigger phrase ("Start Draft", "Start Origin", "Comic Mode", ...)
3. Existing project state (workspace or supplied canon)
4. Natural-language signals and genre cues
5. Router defaults
```

A pack's heuristics never outrank line 1. If the user says a romance must end apart, the Romance pack models a relationship that ends apart. If the user says "don't kill anyone," the Tragic engine finds other costs.

---

## Pipeline

```text
user request
↓
1. TASK CLASSIFIER        what is being asked?
↓
2. PROJECT-STATE LOOKUP   is there a workspace, supplied canon, or nothing?
↓
3. MODE SELECTION         how much machinery does this task warrant?
↓
4. FRONT DOOR             Draft Starter, only if the idea isn't story-shaped yet
↓
5. PLANNING PACKS         identity → genre → scale → world, only those that apply
↓
6. INTENT LOCK            write down the contract (skip if unchanged)
↓
7. STORY GENOME           story identity (SHORT_STORY / LONG_FORM)
↓
8. CORE MODULES           only those the current task needs (table below)
↓
9. OUTPUT REGISTER        prose, or Comic Panel Writer
↓
10. STATE EXTRACTION      update project state; propose, never silently canonize
```

Steps 4–7 run once per project, not once per request. On a continuation, the router reads their stored output instead of rerunning them.

---

## 1. Task classifier

| Task | Signals | Default stage |
|---|---|---|
| `loose_seed` | A premise, image, theme, or character without a story shape. "Let's make a story about...", "I have an idea", "Start Draft". | seed |
| `existing_story` | The user supplies a draft, outline, or canon and asks to develop it. | planning |
| `continuation` | "Continue", "next chapter", "pick up where we left off", or a workspace exists and the request extends it. | continuing |
| `scene_request` | A specific scene with enough definition to write: who, where, what's at stake. | drafting |
| `chapter_request` | A chapter or sequence of scenes in a known project. | drafting |
| `story_request` | A complete short piece defined well enough to write now ("a bedtime story about a hedgehog who learns to share"). | drafting |
| `origin` | How someone became a hero, villain, or other identity. "Start Origin", "villain origin". | seed or planning |
| `comic_output` | "Comic Mode", "panel this", "comic script", "page breakdown". | any |
| `tragic_story` | "Start Tragic Story", "Dark Anime Mode", lethal consequence, ideological war, "make this devastating". | seed or planning |
| `mystery` | A crime, puzzle, investigation, detective, "whodunit", "clues", "Start Mystery". | seed or planning |
| `horror` | Dread, fear, a monster, haunting, "make this scary", "Start Horror". | any |
| `romance` | A love story, relationship arc, "slow burn", "they end up together", "Start Romance". | any |
| `series` | Multiple books, seasons, episodes, or a saga. "Start Series", "season arc". | planning |
| `worldbuilding` | Invented societies, magic, institutions, "build the world", "Build World". | planning |
| `research_grounded` | Real domains — see [research-mode triggers](../core/research-mode.md#triggers). | overlay |
| `critique` | "What's wrong with this", "give me notes", "review this", "is this consistent". | critiquing |
| `revision` | "Revise", "tighten", "rewrite this scene", "fix the pacing". | revising |

A request can carry several tasks. "Write the first chapter of a horror mystery in comic form" is `chapter_request` + `horror` + `mystery` + `comic_output`.

**User intent beats classification.** A request that looks like a loose seed but says "just write it" is a drafting request with authority `autonomous`. Draft Starter does not run.

---

## 2. Project-state lookup

Before asking anything, find what is already known.

```text
.ai-writer/ exists in the project?      → state_source: workspace   (read project.yaml first)
canon, drafts, or notes supplied/open?   → state_source: context     (legacy mode)
neither                                  → state_source: none
```

- **workspace** — load only what the task needs. See [workspace retrieval](workspace.md#retrieval).
- **context** — legacy mode. Treat supplied files as source material. Everything works; nothing persists unless the user wants a workspace.
- **none** — a fresh start.

Known canon is never re-asked. Before any question reaches the user, check it against state, supplied files, and earlier answers in the conversation. Conflicting information goes to the [canon resolver](canon-resolver.md); the router does not settle conflicts by picking one side.

---

## 3. Mode selection

| Mode | Use for | Core pipeline |
|---|---|---|
| **FAST_SCENE** | One scene, a dialogue, a short continuation, a description, a minor rewrite. | scene contract → show/tell + POV choices → character actions → draft → page-craft check → one targeted critic |
| **SHORT_STORY** | A complete short work. | intent → candidates → selection → Story Genome → arc/revelation/affect plan → draft → critic council → revision → continuity check |
| **LONG_FORM** | Novels, novellas, serials, multi-chapter, series. | intent → Story Genome → candidates → rough outline → character/world init → memory init → dynamic outline → scene loop → state extraction → critic loop → outline refresh → continuity audit |
| **CRITIC** | Analysis. | Critics and continuity; no rewriting unless asked. |
| **REVISION** | Improving an existing draft. | Diagnose the failing layer → revision passes, macro before micro → quality gate. |

Research mode is an **overlay** that attaches to any of these.

**Mode rules**

- FAST_SCENE is the default for a well-defined scene, **even inside a large project**. It reads project state if present, but it does not run candidate search, Story Genome, or macro critics. A scene request does not trigger full-project machinery.
- Escalate from FAST_SCENE only when the scene cannot be written without a missing decision (then ask one question, or decide under delegated authority).
- Do not collapse SHORT_STORY or LONG_FORM into one "write a story" step unless the user asks for a fast draft.

---

## 4–5. Pack activation

Packs are listed in [SKILL.md](../SKILL.md#packs). Each pack's front matter is its contract: triggers, skip conditions, inputs, outputs, and what it stacks with. The router reads the front matter; it loads a pack's body only when activating it.

**Activation**

1. An explicit trigger phrase activates its pack unless a higher-precedence instruction forbids it.
2. A natural-language trigger activates a pack when the request is *about* that thing. A story that mentions a detective is not necessarily a mystery; a story whose engine is "who did it" is.
3. A pack's `skip_when` conditions veto **natural-language** activation (Precedence lines 3–5). An explicit trigger always activates its pack; the pack then decides how much of its procedure the request needs — Draft Starter with a complete premise skips straight to the brief. Only the user can override a skip.
4. Genre cues alone do not activate a pack in FAST_SCENE for trivial requests. A one-paragraph spooky description doesn't need the Horror pack's dread curve; a horror *scene* does.
5. **Continuations restore packs.** With a workspace, packs in `metadata.active_packs` are active for any request that touches their material. A scene that doesn't touch them reads their ledgers only if relevant.
6. **An active pack's `requires` load with it**, whatever the mode table below says. A horror scene in FAST_SCENE still loads `core/reader-state`, because the Horror pack requires it.

**Order**

```text
front-door   draft-starter
identity     origin-forge
genre        tragic-anime-engine · mystery · horror · romance   (any combination)
scale        series-engine
world        worldbuilding
─────────── Intent Lock → Story Genome ───────────
output       comic-panel-writer
```

Genre packs stack. When two genre packs disagree about an ending convention (Romance's default of an emotionally satisfying ending vs. Tragic's permanent cost), the conflict is settled in Intent Lock by the user's stated intent, not by pack order.

**Draft Starter gate.** "Start Draft" always runs it. Otherwise, run Draft Starter only when *all* of these hold:

- stage is `seed`;
- the user has not asked to skip planning or draft immediately;
- no Draft Brief (or equivalent defined premise) exists in state or context;
- authority is not `autonomous` — in autonomous mode Draft Starter runs silently to build the brief and asks nothing.

---

## 6–8. Core module selection

Load the smallest set that does the job. `●` = load; `○` = load if the request needs it; blank = don't.

| Module | FAST_SCENE | SHORT_STORY | LONG_FORM | CRITIC | REVISION |
|---|:-:|:-:|:-:|:-:|:-:|
| [intent-lock](../core/intent-lock.md) | ○ | ● | ● | ○ | ○ |
| [story-genome](../core/story-genome.md) |  | ● | ● | ○ | ○ |
| [creativity-search](../core/creativity-search.md) |  | ● | ● |  | ○ |
| [character-model](../core/character-model.md) | ○ | ● | ● | ○ | ○ |
| [character-agency](../core/character-agency.md) | ○ | ○ | ● |  | ○ |
| [relationships](../core/relationships.md) | ○ | ○ | ● | ○ | ○ |
| [world-state](../core/world-state.md) | ○ | ○ | ● | ○ |  |
| [memory](../core/memory.md) | ○ |  | ● | ○ |  |
| [continuity](../core/continuity.md) |  | ○ | ● | ● | ○ |
| [outlining](../core/outlining.md) |  | ● | ● |  |  |
| [scene-engine](../core/scene-engine.md) | ● | ● | ● | ○ | ● |
| [reader-state](../core/reader-state.md) |  | ● | ● | ○ | ○ |
| [suspense-curiosity-surprise](../core/suspense-curiosity-surprise.md) | ○ | ○ | ● | ○ | ○ |
| [information-architecture](../core/information-architecture.md) | ○ | ○ | ● | ○ | ○ |
| [dialogue](../core/dialogue.md) | ○ | ● | ● | ○ | ○ |
| [pov](../core/pov.md) | ● | ● | ● | ○ | ● |
| [prose](../core/prose.md) | ● | ● | ● |  | ● |
| [revision](../core/revision.md) | ○ | ● | ● |  | ● |
| [critics](../core/critics.md) | ○ | ● | ● | ● | ● |
| [endings](../core/endings.md) |  | ● | ● | ○ | ○ |
| [research-mode](../core/research-mode.md) | ○ | ○ | ○ | ○ | ○ |
| [question-bank](../core/question-bank.md) | ○ | ○ | ○ | ○ | ○ |

**Pack drafting checks.** When drafting with packs active, each pack's drafting-time checks run at the critic step: Mystery's ledger check, Horror's audit, Romance's perception update, Tragic's residue check, Comic Panel Writer's production checks.

**Conditional loads (○)**

- `memory` in FAST_SCENE: only when continuing an existing project.
- `character-model` in FAST_SCENE: only when a named character with history acts or infers; the Perspective Filter always applies to anyone who reasons.
- `character-agency` in FAST_SCENE: only when the scene turns on a character's decision.
- `dialogue`: when the scene has significant dialogue.
- `information-architecture`: when something is concealed, revealed, or explained.
- `suspense-curiosity-surprise`: when the scene or story carries a question, a threat, or a twist.
- `research-mode`: when the research overlay is on.
- `critics` in FAST_SCENE: one targeted critic at most.
- `revision` in FAST_SCENE: the page-craft gate subset only.

---

## 9. Output register

| Register | When |
|---|---|
| `prose` | Default. |
| `comic_narrative` | Comic Panel Writer active, no pages or panels requested. |
| `comic_page_map` / `comic_panel_breakdown` / `comic_full_script` | The user asked for pages, panels, or a script. |
| `plan` | Planning requests: briefs, outlines, ledgers. |
| `critique` | CRITIC mode. |

Comic Panel Writer never forces production scripting when the user wants only a comic-book style.

---

## 10. State extraction

After drafting or planning, extract what changed: events, character and relationship updates, new open loops, setups and payoffs, research items.

- **With a workspace:** write updates per [workspace update rules](workspace.md#updating). Anything the agent invented is recorded with provenance `agent_proposal` (or `delegated_decision` when the user delegated), never as `user_confirmed`.
- **Without a workspace:** keep the updates in context. Offer a workspace once a project has grown past a few chapters; do not create one unasked.

---

## Authority

| Authority | Set by | Behavior |
|---|---|---|
| `guided` | "Ask me before choosing", rigid canon. | Ask before major creative decisions. |
| `collaborative` | Default. | Ask only consequential forks; propose the rest. |
| `autonomous` | "You decide", "surprise me", "full creative freedom". | Decide, state major assumptions, keep going. Record decisions as `delegated_decision`. |

"You decide" is an answer, not a prompt for another question. Delegated authority covers the decisions it was given for. A later canon-level change still goes to the user (see [canon resolver](canon-resolver.md#what-needs-the-user)).

---

## When to ask the user

Offer a choice at meaningful creative forks, not constantly:

- premise family;
- protagonist interpretation;
- ending family;
- a major canon change;
- an extreme structural experiment;
- an irreversible relationship direction.

Ask only when the answer would substantially change the work and context cannot resolve it. Don't interrupt after every scene unless the user asked for that.

---

## Anti-patterns

- **Maximum machinery.** Loading every module for a paragraph of dialogue.
- **Pack by vocabulary.** Activating Mystery because a character is a police officer.
- **Re-running the front door.** Asking Draft Starter questions on a continuation.
- **Silent canonization.** Treating the router's own guesses as confirmed facts.
- **Heuristic override.** A pack's defaults beating the user's stated intent.

---

## Route examples

| Request | Route |
|---|---|
| "Let's make a heartfelt story about skiing." | `loose_seed` · seed · SHORT_STORY · packs `[draft-starter]` · asks 3–5 emotional-core questions |
| "Write the scene where Mara confronts her brother in the hospital parking lot — she knows he forged the will; he doesn't know she knows." | `scene_request` · drafting · FAST_SCENE · packs `[]` · core scene-engine, pov, prose, dialogue, character-model · asks nothing |
| "Start Origin: a decorated officer who becomes a villain. You decide the rest." | `origin` · seed · SHORT_STORY · authority autonomous · packs `[draft-starter, origin-forge]` · asks nothing |
| "Dark Anime Mode. Build a tragic arc for my team." | `tragic_story` · planning · LONG_FORM · packs `[tragic-anime-engine]` (+ draft-starter only if no premise exists) |
| "Continue chapter 12." (workspace present) | `continuation` · continuing · LONG_FORM · packs from `project.yaml` · core memory first |
| "Panel this page." | `comic_output` · drafting · FAST_SCENE · packs `[comic-panel-writer]` · register comic_panel_breakdown |

Full walk-throughs: [tests/workflow-traces.md](../tests/workflow-traces.md).
