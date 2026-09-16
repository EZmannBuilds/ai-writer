# Intent Lock

The compact project contract. Everything downstream — genome, outline, critics — is measured against it. It is the place user intent is written down so heuristics cannot quietly override it.

| Contract | |
|---|---|
| Invoked by | Router, after any front-door pack (Draft Starter, Origin Forge, genre packs) and before Story Genome. |
| When | Before the first substantial generation in a project, or when the user changes format, tone, audience, or constraints. |
| Needs | The request; Draft Brief / pack briefs if present; any `canon` already in project state. |
| Produces | `intent_lock` |
| State | `intent_lock` — `.ai-writer/project.yaml` when a workspace exists, otherwise in context. |
| Consumed by | [story-genome](story-genome.md), [critics](critics.md) (the `user_intent_fit` check), every mode's pipeline. |
| Skip when | FAST SCENE MODE when the request already states POV, tone, and constraints; an `intent_lock` already exists and nothing has changed. |
| Tests | F02, F05, F21 |
| Research | Design principle, not a research import. See [research/README](../research/README.md). |

---

## The Intent Lock schema

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
