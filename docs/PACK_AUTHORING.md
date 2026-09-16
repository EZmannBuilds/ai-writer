# Pack Authoring

How to add a pack to AI Writer without bloating the core, tangling dependencies, or teaching the system to treat its own guesses as canon.

Start from [templates/PACK_TEMPLATE.md](../templates/PACK_TEMPLATE.md). Run `python3 scripts/validate.py` before committing.

---

## Is this a pack?

A pack is the right shape when the capability is:

- **optional** — many stories never need it;
- **activatable** — you can say when it should turn on and when it shouldn't;
- **stateful or procedural** — it adds a procedure, a ledger, or a schema, not just advice.

It is **not** a pack when:

| Situation | Put it in |
|---|---|
| Every story needs it | A core module (and justify why it must always be available) |
| It refines an existing core mechanism | That core module |
| It's a checklist with no activation logic | A section of an existing module or pack |
| It's reference material for one pack | A companion file (`companion: {of: <pack>}`) |
| It's a style preset for one project | The user's project notes, not the skill |

**Before writing, search the core.** Most "new" ideas already exist as a mechanism: suspense threads, information items, relationship state, the setup/payoff ledger, reader state. A pack should *extend* these, not re-invent them. The Mystery pack's clue ledger is a specialization of [information items](../core/information-architecture.md#information-items); the Romance pack's perception model extends [relationship state](../core/relationships.md#relationship-state).

---

## The contract

Every pack file opens with YAML front matter. The router reads only this block to decide whether to load the pack, so it must be accurate.

```yaml
pack:
  id: mystery                    # kebab-case; must equal the filename
  name: Mystery / Investigation
  version: "1.0"
  stage: genre                   # front-door | identity | genre | scale | world | output
  pipeline_position: After Draft Starter and Origin Forge, before Intent Lock.
  purpose: One sentence.
  triggers: ["Start Mystery"]    # explicit phrases
  natural_language_triggers: []  # examples of ordinary phrasing that should also activate it
  requires: []                   # hard dependencies: pack ids or core/<module>
  optional_dependencies: []      # used when present
  conflicts_with: []             # must be reciprocal
  stacks_with: []                # packs known to combine cleanly
  inputs: []                     # state or briefs it reads
  produces: []                   # schemas it writes
  skip_when: []                  # conditions that veto natural-language activation
  state_keys: []                 # project-state paths it reads or writes
  research_basis: research/packs/mystery.md
  behavior_tests: [F16]          # fixture ids in tests/fixtures/
```

`scripts/validate.py` enforces every field, the stage vocabulary, id uniqueness, that dependencies exist, that conflicts are reciprocal, that the research file and fixtures exist, and that the pack appears in the [SKILL.md pack table](../SKILL.md#packs).

### Stages

| Stage | Runs | Examples |
|---|---|---|
| `front-door` | First; turns a seed into a brief | draft-starter |
| `identity` | Shapes who a character is before the story | origin-forge |
| `genre` | Adds genre mechanics; genre packs stack | tragic-anime-engine, mystery, horror, romance |
| `scale` | Plans beyond a single story | series-engine |
| `world` | Builds setting systems | worldbuilding |
| `output` | Changes the output register at drafting time | comic-panel-writer |

Planning stages run before [Intent Lock](../core/intent-lock.md). Output packs run at drafting time. See [router order](../runtime/router.md#45-pack-activation).

---

## Required body sections

Use these headings, in this order. A section may be short, but it must exist.

1. **Purpose** — what problem the pack solves, in a paragraph.
2. **Activation** — explicit and natural-language triggers; how the router should recognize a request that is *about* this, not one that only mentions it.
3. **Skip conditions** — when it must not run, even if a trigger word appears.
4. **Pipeline position** — where it sits and what runs before and after it.
5. **Inputs** — what it reads.
6. **Outputs** — what it produces.
7. **State** — used and produced; see [State](#state) below.
8. **Procedure** — the steps, in order.
9. **Guardrails** — hard lines.
10. **Failure modes** — how the pack goes wrong, and the fix for each.
11. **Schemas** — YAML blocks. They must parse.
12. **Examples** — at least one worked example with invented, generic material.
13. **Behavior tests** — which fixtures cover it, and what each checks.
14. **Research provenance** — link to its research file and summarize fidelity.
15. **Integration** — how it combines with other packs and which core modules it extends.

---

## State

- **Your schemas live under `pack_state.<pack-id>`.** Stored in `.ai-writer/packs/<pack-id>.yaml` when a workspace exists.
- **Core facts stay in core branches.** A pack that changes a character writes to `characters`; one that changes a relationship writes to `relationships`. Never keep a private copy of core data.
- **Mirror open questions.** If your pack tracks questions (clues, reveals, promises), mirror each open one as an `open_loops` item with `pack` and `ref` set, so continuity and endings can see it.
- **Carry provenance.** Any fact your pack produces gets a [provenance status](../runtime/canon-resolver.md#provenance-statuses). Anything the agent invents is `agent_proposal` or `delegated_decision`.
- **Sparse is fine.** Define optional fields as optional.

See [project state](../runtime/project-state.md#where-the-existing-schemas-live) for how the existing packs map.

---

## Avoid

**Duplicate functionality.** If a core module does 80% of what you need, extend it in your pack by reference ("record each clue as an information item, plus these fields"). Don't copy its schema with renamed fields.

**Permanent core bloat.** Packs don't edit core modules to add pack-specific rules. If a core module genuinely needs a new general mechanism, that change is a separate, justified core change.

**Dependency tangles.** Keep `requires` to core modules wherever you can. A pack that requires another pack can never run alone; prefer `optional_dependencies` and degrade gracefully. No cycles.

**Contradictory schemas.** Don't reuse a core field name with a different meaning. Check [project state](../runtime/project-state.md) before naming anything.

**Unnecessary questions.** Packs inherit the interview discipline: read state and files first; ask at most 3–5 questions, only consequential ones; accept "you decide" as delegation. A pack that needs a questionnaire needs redesigning.

**Treating proposals as canon.** Every pack output that invents something must label it. A brief should separate confirmed facts, delegated decisions, agent proposals, and open questions.

**Default-to-genre.** A pack must not make every story more like its genre. The Horror pack doesn't make a romance scary; the Tragic engine doesn't kill someone because it's loaded.

**Imitation.** Reference works supply transferable mechanisms. Never copy proprietary names, characters, plot sequences, or distinctive dialogue.

---

## Research provenance

Every pack has `research/packs/<pack-id>.md`. Each research-derived mechanism gets an entry:

```markdown
### `source-key`

- **Source:** Author, "Title," venue, year. URL.
- **Claim:** What the source actually says, paraphrased.
- **Derives:** What the pack takes from it.
- **Limitations:** Sample, scope, era, method.
- **Fidelity:** exact | approximate | conceptual | convention | design
```

Fidelity:

| Value | Meaning |
|---|---|
| `exact` | The pack does what the source does. |
| `approximate` | The source uses a tool the skill lacks (embeddings, classifiers, decoding changes, multiple models, external memory); the pack imitates it with structured prompting. Say which tool. |
| `conceptual` | The source informs the design as an idea only. |
| `convention` | A historical or genre convention, not evidence. |
| `design` | A design decision with no external source. |

Add every key to [research/source-index.md](../research/source-index.md). Cite keys inline as `[@key]`. Never claim `exact` for an approximation.

If a mechanism has no source, say so and mark it `design` or craft inference. Don't borrow authority from an unrelated citation.

---

## Tests

Add at least one fixture per mechanism the pack claims, in `tests/fixtures/` (see [tests/README](../tests/README.md)). Good pack tests check:

- activation on the right request, and non-activation on a look-alike request;
- skip conditions;
- the pack's central invariant (e.g., "every reveal has a prior clue");
- provenance on anything invented;
- one integration with another pack or core module.

---

## Checklist

- [ ] Front matter complete; `python3 scripts/validate.py` passes.
- [ ] Row added to the [SKILL.md pack table](../SKILL.md#packs).
- [ ] Trigger rows added to the [router's task classifier](../runtime/router.md#1-task-classifier).
- [ ] State lives under `pack_state.<id>`; core facts go to core branches.
- [ ] Research file with fidelity on every entry; keys in the source index.
- [ ] Fixtures written, including one non-activation case.
- [ ] CHANGELOG entry.
