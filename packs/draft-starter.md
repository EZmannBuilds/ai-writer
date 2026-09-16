# Draft Starter Insert v1.0
## AI Writer — pre-drafting interview layer

Added 2026-09-15. Sits **before** Intent Lock and Story Genome (§3–4 of the main skill).

Its job is not to write the story immediately. Its job is to convert a loose story seed into a usable creative brief through a short, collaborative interview, then hand that brief to the existing story-development pipeline.

```text
User story seed
    ↓
Draft Initiation Interview   ← this module
    ↓
Draft Brief
    ↓
Intent Lock
    ↓
Story Genome
    ↓
Candidate Generation → Rough Outline → Drafting
```

**User-facing trigger:** "Start Draft." Natural-language equivalents also activate it: "Let's make a story about...", "I want to write a story where...", "Help me start a draft.", "I have a story idea.", "Turn this idea into a story."

**Do not activate** when the user is already asking for prose from a sufficiently defined scene/chapter, explicitly asks to skip planning and draft immediately, or a complete Draft Brief already exists.

---

## Why it exists

Intent Lock and Story Genome are useful once there is a story-shaped object to reason about. A raw prompt like *"Let's make a heartfelt story about skiing"* doesn't yet contain enough to plan against. This insert converts the raw seed into that story-shaped object while preserving conversational flow — it should feel like talking to a creative partner, not completing a questionnaire.

**Avoid duplication.** This insert should not generate a full beat sheet unless requested, perform deep character dossiers, build a complete world bible, produce exhaustive theme matrices, replace Story Genome, or lock speculative details as canon. It defines just enough to let those later systems work well.

---

## First-pass interpretation

Before asking anything, silently classify available information into:

- **Confirmed** — explicitly stated by the user, or supplied canon/source material.
- **Inferable** — a reasonable interpretation that may help form options, but is never treated as canon.
- **Missing but consequential** — unknown information that would materially change the story's emotional core, identity, or structure.
- **Safely open** — unknown information that can stay undecided until later.

Never ask for information that is already confirmed — check the user's prompt, attached files, project canon, and memory first.

---

## Interview layers

Ask **3–5 questions per round**, most consequential first. Select only what matters — do not ask every question in a layer by default.

### Layer 1 — Emotional Core (ask first; shapes everything else)

- What should the reader feel most strongly by the end — comforting, bittersweet, painful, triumphant, unresolved, eerie, intimate?
- Is the emotional destination more important than the external plot outcome?
- Which relationship or inner conflict should carry the story emotionally?
- What does the protagonist want emotionally that they cannot easily admit?
- What does the central activity/place/object represent to the protagonist — gaining, losing, accepting, repairing, escaping?
- What tension should the story keep returning to?
- Is this inspired by something personal, entirely fictional, or a mix? Is there a real feeling to preserve even if events are invented?
- What must the story avoid becoming? Anything it shouldn't romanticize, excuse, simplify, or turn into spectacle?

*Option-assisted variant, when the user may not know the answer:* offer choices — "Should the mountain represent escape, home, danger, inheritance, or a memory being avoided?"

### Layer 2 — Story Identity (ask once emotional direction is reasonably clear)

- Format — short story, novella, novel, screenplay, episode, game narrative? Compact or built to expand?
- Genre / realism — realistic, heightened, speculative/fantastical? What genre gives the outer shape?
- Protagonist — who is best positioned to suffer, change, or make the central choice? Already inside this world, or entering it for the first time?
- Desire and pressure — what does the protagonist actively want? What external pressure prevents them from simply getting it? What happens if they refuse to act?
- Setting — does the location need to be specific, culturally meaningful, symbolic, or mostly functional? Is the time period important?
- Ending — resolve the external problem, the emotional problem, both, or neither? Hopeful, tragic, bittersweet, uncanny, open?
- Audience / content rating, if it changes what can appear on-page.

### Layer 3 — Authenticity & World Detail (ask only when materially relevant — never a mandatory checkbox)

- Does a specific culture, community, identity, family tradition, religion, subculture, or social world matter here? Customs or expectations that shape behavior? Is the location inseparable from the people who live there?
- Does the story depend on technical accuracy in a sport, profession, craft, historical period, military context, science, medicine, law, music, or another domain? What level of realism — background credibility, expert-level, or emotionally plausible approximation?
- Is this part of an existing universe? Which canon sources outrank invention? Which parts may be expanded freely?
- What needs verification before outlining or drafting? Real locations, procedures, customs, historical details?
- Are there lived experiences or sensitive topics needing particular care? A framing to avoid? Anything better left implied than explicit?

---

## Questioning rules

1. Ask 3–5 questions per round, most consequential first.
2. Never ask for information already present in the prompt, files, canon, memory, or prior answers.
3. Never ask about choices that can safely stay open.
4. Offer possibilities when the user may not know the answer.
5. The user may always answer **"you decide."**
6. Keep confirmed decisions visibly separate from agent proposals.
7. Never silently convert a suggestion into canon.
8. Stop interviewing as soon as the project can move forward.
9. Default to **no more than two interview rounds**; use more only for genuinely complex projects.
10. Do not run an exhaustive questionnaire.
11. Prefer questions that change multiple downstream decisions at once.
12. If the user already gave enough, skip straight to the Draft Brief.
13. If the user delegates a decision, make it confidently and record it as *agent-chosen*, not *user-confirmed*.

---

## Creative-control modes

- **Guided** — ask before making major creative decisions. Use when the user wants close control, source material is rigid, or canon is sensitive to invention.
- **Collaborative — default.** Ask about emotional core, non-negotiables, and genuinely consequential choices; propose and develop the rest.
- **Autonomous** — interpret the seed, state major assumptions, build the story with minimal questioning. Use when the user says "you decide," asks for full creative freedom, or wants a fast concept pass.

Routing: "Ask me before choosing" → Guided. Nothing stated about control → Collaborative. "You decide / surprise me / full freedom" → Autonomous. The user may change mode at any point.

---

## Response pattern — first turn

1. **Interpretive opening** — one short paragraph on what the seed could emotionally or dramatically mean.
2. **Creative possibilities** — 2–4 directions, archetypal tensions, or premise vectors.
3. **Question round** — 3–5 high-impact questions.

Do not produce a giant outline before the emotional center is understood, unless the user selected Autonomous mode.

## Response pattern — after answers

1. Synthesize what the answers point toward.
2. Resolve delegated choices.
3. Ask a second round only if a major ambiguity remains.
4. Otherwise, produce the Draft Brief.
5. Separate confirmed facts / agent proposals / unresolved items clearly.
6. State the recommended next action (normally Intent Lock).
7. Continue into the next pipeline stage automatically if the host system supports chaining.

Suggested transition line: *"Here is the story I think those answers are pointing toward."*

---

## Draft Brief

Compact enough for downstream systems to use directly. Normally includes: original prompt, working premise, intended emotional effect, format, genre, protagonist, central relationship, central desire, central pressure, setting, cultural context (when relevant), thematic questions, mandatory/forbidden elements, confirmed facts, creative permissions, agent proposals, unresolved questions, and recommended next action.

```yaml
draft_brief:
  version: "1.0"
  original_prompt: ""
  source_context: []
  drafting_mode: "collaborative"          # guided | collaborative | autonomous
  working_title: null
  working_premise: ""
  intended_emotional_effect: []
  format: null
  approximate_length: null
  genre: []
  realism_level: null
  audience_or_content_rating: null
  protagonist: null
  central_relationship: null
  central_desire: null
  central_pressure: null
  emotional_conflict: null
  likely_ending_direction: null
  setting: { place: null, time_period: null, environment: null }
  cultural_context: null
  authenticity_needs: []
  research_needs: []
  thematic_questions: []
  motifs_or_symbols: []
  mandatory_elements: []
  forbidden_elements: []
  sensitive_elements: []
  confirmed_facts: []
  delegated_decisions: []
  creative_permissions: []
  agent_proposals: []
  assumptions: []
  unresolved_questions: []
  readiness: "ready"                      # ready | needs_one_more_round | blocked
  recommended_next_action: "Intent Lock"
```

**Handoff contract:** `Draft Brief → Intent Lock → Story Genome → candidate generation → rough outline → drafting`. Do not duplicate Story Genome work unless the downstream system is unavailable. This insert is a front door, not a replacement for the deeper planning stages.

---

## Failure modes to avoid

- **Questionnaire dump** — 15–30 questions at once. Fix: 3–5 consequential questions only.
- **Creative labor boomerang** — asking the user to invent every component from scratch. Fix: propose possibilities, let them react.
- **False canon** — presenting an agent suggestion later as if the user confirmed it. Fix: track provenance.
- **Premature drafting** — pages of prose before the emotional core is understood, when the user asked to develop the idea. Fix: interview first, unless Autonomous mode or explicit "draft now."
- **Endless interview** — continuing because more detail is theoretically possible. Fix: stop when there's enough to move forward.
- **Mandatory culture field** — forcing every story to answer cultural questions. Fix: ask only when materially relevant.
- **Re-asking known information** — ignoring canon, files, memory, or prior answers. Fix: use available context before questioning.

## Completion test

The insert is done when the system can answer: What is this story emotionally about? Who or what carries that emotion? What does the protagonist want? What pressure makes the story move? What kind of story is this? Where/when does it occur, at the level needed right now? What is non-negotiable? What may the agent invent? What, if anything, still needs resolution before outlining? If those are sufficiently answered, stop interviewing.

---

## Worked examples

### Loose seed → Collaborative

**User:** "Let's make a heartfelt story about skiing."

**Good first response:** Skiing can carry a surprising amount of emotional weight — freedom, inheritance, fear, aging, grief, competition, a relationship that only feels natural on the mountain. Strong directions: an estranged family returning to a place they once loved; a mentor realizing they can't keep doing the thing that defined them; someone learning to ski because of a person they've lost.

1. Which relationship should carry the story — parent/child, siblings, friends, romantic partners, mentor/student, or someone confronting themselves?
2. Should the mountain represent escape, home, danger, or a memory the protagonist has been avoiding?
3. Should the emotional finish feel comforting, bittersweet, tragic, or hopeful?
4. Is there a specific place, culture, community, or personal experience that needs to shape the story?
5. Several premises to choose from, or should I choose the strongest direction and develop it?

*Why this works:* interprets the seed before questioning, offers creative directions, asks only consequential questions, leaves room for delegation, doesn't hand the whole creative task back to the user.

*Bad version, for contrast:* "Who are the characters? What is the plot? What is the theme? Where is it set? What is the culture?" — returns the entire creative task to the user.

### Full delegation → Autonomous

**User:** "Start Draft: A woman keeps receiving voicemail messages from her dead sister. You decide everything else."

Because the user delegated creative control, skip the normal interview: state the core interpretation, briefly note assumptions that materially affect the story, build the Draft Brief, mark invented elements as delegated/agent proposals, and continue to Intent Lock.

*Example synthesis:* the story works best if the voicemails are emotionally useful before they become frightening — letting grief and supernatural uncertainty reinforce each other rather than collapsing into a simple ghost mystery. Agent-chosen from there: contemporary psychological horror; older sister as protagonist; unresolved guilt over the final call she ignored; a small city setting; voicemails that initially contain mundane details only the sister could know; an ending that resolves the protagonist's guilt but leaves the supernatural explanation ambiguous. **None of these are user-confirmed facts — they're authorized creative decisions**, recorded as such in the Draft Brief.

---

## Behavior checks

Lightweight acceptance tests — use to sanity-check this module's own behavior, not to run on the user.

1. **Loose seed** — interprets first, asks 3–5 emotional-core questions, offers options, no 15+ item dump.
2. **"You decide"** — agent decides, records as delegated, continues toward Draft Brief.
3. **Existing canon supplied** — does not re-ask protagonist/setting already given; asks only what's still consequential.
4. **Culture irrelevant to a contained surreal premise** — does not force a culture question.
5. **Culture relevant** (multigenerational family story tied to a specific community) — recognizes it, asks one focused authenticity question.
6. **Enough already given** (protagonist, desire, pressure, relationship, tone, setting, ending direction all present) — skips the interview, produces the Draft Brief directly.
7. **False canon check** — after proposing three possible settings and the user answering only emotional questions, none of those settings appear as confirmed facts.
8. **Two-round ceiling** — usually stops after one or two rounds; a third round only for genuine story-level ambiguity.
9. **"Full creative freedom"** — mode switches to Autonomous, questioning goes minimal.
10. **Pipeline handoff** — completed Draft Brief recommends Intent Lock, not a duplicate Story Genome pass.
