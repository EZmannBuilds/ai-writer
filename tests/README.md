# Tests

AI Writer is a set of instructions, so its tests are **behavioral**: given a request and context, does an agent following the skill route correctly and respect the system's invariants? They do not judge literary taste. Whether the stories are *better* is the [benchmark's](../research/benchmark.md) question.

```text
tests/
  README.md              this file
  fixtures/F##-*.yaml    behavioral regression fixtures
  workflow-traces.md     step-by-step traces of seven end-to-end workflows
  results/               recorded runs
```

Structure is checked separately, by `python3 scripts/validate.py` (see [CI](#ci)).

---

## Fixture format

```yaml
id: F12
title: A character cannot use knowledge they do not possess
covers: [core/character-model, core/pov, runtime/router]   # what it exercises
input:
  request: "..."                 # the user's words, verbatim
  context:                       # what exists before the request
    state: none | context | workspace
    canon: "..."                 # optional summaries of supplied material
    workspace: {file: summary}   # optional
expected:
  route:                         # the router's decision (see runtime/router.md)
    task: scene_request
    mode: FAST_SCENE
    packs: []
  behavior: []                   # what a correct response does
failure: []                      # what a regression looks like
pass_criteria: []                # checkable statements; all must hold
```

`pass_criteria` are written so a grader can decide each one from the response alone.

---

## Invariants covered

| Invariant | Fixture |
|---|---|
| A loose seed activates Draft Starter | F01 |
| A detailed scene request skips Draft Starter | F02 |
| "You decide" is delegation, not another question | F03 |
| An agent proposal never silently becomes canon | F04 |
| Known canon is not re-asked | F05 |
| Origin Forge separates the disruption from the villain-defining choice | F06 |
| A non-traumatic hero origin is possible | F07 |
| The Tragic engine doesn't default to death | F08 |
| A death creates downstream residue | F09 |
| A survival alternative is considered | F10 |
| Power costs persist | F11 |
| Characters can't use knowledge they don't have | F12 |
| Characters keep distinct beliefs | F13 |
| Relationships update after consequential scenes | F14 |
| Continuity findings cite both sides | F15 |
| A mystery reveal has prior clues | F16 |
| A comic panel is drawable | F17 |
| A page-turn reveal isn't spoiled early | F18 |
| FAST SCENE MODE avoids full-project machinery | F19 |
| Research mode separates fact from invention | F20 |
| User intent overrides heuristics | F21 |
| Intentional contradictions aren't "fixed" | F22 |
| Horror has a dread curve with quiet | F23 |
| Romance tracks each partner's perception | F24 |
| A relationship may correctly end | F25 |
| Series escalation isn't just a bigger villain | F26 |
| No workspace → legacy mode | F27 |
| Worldbuilding enters through use | F28 |
| Legacy "Dark Anime Mode" still routes | F29 |
| Critics don't homogenize deliberate choices | F30 |
| The horror audit flags stock devices | F31 |
| Red herrings come from real secrets | F32 |
| A romance continuation loads state first | F33 |
| Comic villain origin: Origin Forge then Comic Panel Writer | F34 |
| Referenced-but-unsupplied canon isn't invented as approved | F35 |

---

## Running the behavioral suite

The suite is run by agents, in two separated roles, so the model that answers is not the model that grades.

**1. Execute.** For each fixture, an executor agent:

- loads the skill from `SKILL.md` and follows its routing;
- receives `input.request` as the user's message and `input.context` as the situation (supplied files are described, not attached);
- writes its full response, preceded by a fenced `route` block stating the route it chose;
- does **not** see `expected`, `failure`, or `pass_criteria`.

**2. Grade.** A grader agent receives the fixture's `expected`, `failure`, and `pass_criteria` plus the executor's response, and returns for each criterion `pass` or `fail` with a quoted piece of evidence. A fixture passes only if every criterion passes.

**3. Record.** Save the run to `tests/results/<date>.md`: skill version (git hash), model, per-fixture verdicts with evidence, and failures with notes.

Guidance:

- Run executors in independent contexts. A context that has seen other fixtures' criteria is contaminated.
- A route is judged on task, mode, and packs. `mode` may be a list, meaning any of those modes passes. `packs_optional` lists packs a response may load without failing. Core-module lists may reasonably differ at the edges.
- For a request carrying several tasks, a route whose task list includes the expected task passes.
- Treat a fixture failure as a signal to inspect, not an automatic defect: the fixture may be wrong. Fix whichever is wrong and note it in the results.
- Behavioral results vary between runs. Re-run failures before concluding.

---

## Static checks

`scripts/validate.py` also checks the fixtures themselves: every fixture parses, has the required keys, has an id matching its filename, covers modules and packs that exist, and — if its request contains an explicit trigger phrase — expects the pack that trigger belongs to.

---

## CI

`.github/workflows/validate.yml` runs on every push and pull request:

```bash
pip install pyyaml
python3 scripts/validate.py
python3 scripts/build_source_index.py --check
```

The behavioral suite is not run in CI; it needs a model. Run it before releases and after changes to the router, packs, or canon rules.
