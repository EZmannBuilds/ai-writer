---
pack:
  id: your-pack-id
  name: Your Pack Name
  version: "0.1"
  stage: genre
  pipeline_position: After Draft Starter, before Intent Lock.
  purpose: One sentence describing the problem this pack solves.
  triggers: ["Start Your Thing"]
  natural_language_triggers: ["an example of ordinary phrasing"]
  requires: []
  optional_dependencies: []
  conflicts_with: []
  stacks_with: []
  inputs: []
  produces: []
  skip_when: []
  state_keys: ["pack_state.your-pack-id"]
  research_basis: research/packs/your-pack-id.md
  behavior_tests: []
---

<!--
Copy this file to packs/<id>.md. Keep every heading. See docs/PACK_AUTHORING.md.
This template is not a pack: scripts/validate.py only reads packs/.
-->

# Your Pack Name

## Purpose

What problem this solves, and why the core doesn't already solve it.

## Activation

- Explicit triggers.
- Natural-language cues — and how to tell a request *about* this from one that only mentions it.

## Skip conditions

- When this must not run, even if a trigger word appears.

## Pipeline position

```text
Draft Starter → [this pack] → Intent Lock → Story Genome → ...
```

## Inputs

## Outputs

## State

- **Uses:** core branches read.
- **Produces:** `pack_state.your-pack-id.*`; core branches written (with provenance).
- **Open loops mirrored:** which items.

## Procedure

1. Read state and supplied files first.
2. ...

## Guardrails

## Failure modes

| Failure | Looks like | Fix |
|---|---|---|
|  |  |  |

## Schemas

```yaml
your_schema:
  field:
```

## Examples

A worked example using invented, generic material.

## Behavior tests

| Fixture | Checks |
|---|---|
|  |  |

## Research provenance

See `research/packs/<id>.md`. Summarize fidelity: which mechanisms are evidence-based, approximate, conventions, or design decisions.

## Integration

- Core modules extended:
- Packs it combines with, and how:
