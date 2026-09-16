# POV and Psychic Distance

Whose mind the reader stands in, and how close. Knowledge boundaries on the page start here.

| Contract | |
|---|---|
| Invoked by | Router for every prose draft. |
| When | Choosing a scene's POV; during the POV revision pass. |
| Needs | `intent_lock.pov`, `intent_lock.prose_distance`; the POV character's perspective-filtered state. |
| Produces | Scene POV and distance range (the scene contract's `psychic_distance_*` fields). |
| State | Ephemeral; project defaults live in `intent_lock`. |
| Consumed by | [prose](prose.md). |
| Skip when | Comic Full Script output (panels have no narrator), except for captions. |
| Tests | F12 |
| Research | [research/core/page-craft.md](../research/core/page-craft.md) |

---

## POV and Psychic Distance Engine

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

### Distance rules

- Choose a default range for the scene.
- Change distance intentionally.
- Avoid accidental head-hopping.
- Do not report information the POV character cannot know.
- Let description inherit the POV character's language and values.
- A close POV does not need constant "she saw / he noticed / she felt" filters unless the filtering itself matters.

### Zoom question

At any paragraph ask:

> Am I at the distance that gives this beat the strongest effect?

A death may need distance.
A tiny embarrassment may need extreme closeness.
Do not assume "closer" always means "better."

---

## POV quick card

POV controls:
- knowledge;
- interpretation;
- detail;
- language;
- reader proximity.

Psychic distance controls how close the narration sits to the character's consciousness.

### Working levels

```yaml
wide:
  context / geography / time compression

medium:
  observable scene + selective interiority

close:
  character-filtered perception / thought / desire

immersed:
  near-thought syntax / fragmented perception / crisis
```

### Checks

- Is the narrator revealing knowledge the POV cannot possess?
- Is another character's interior state being stated as fact?
- Does description sound like the author rather than the POV?
- Did the narrative zoom from wide to immersed without a transition?
- Does every observation begin with "she saw/he heard/she felt" even though the scene is already inside that character?
- Would another POV character describe the same room differently?

### Detail as characterization

The room is not neutral.

A mechanic, thief, child, soldier, grieving parent, architect, and jealous lover should notice different things.

Use that difference.
