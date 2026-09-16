# Workspace

An optional `.ai-writer/` folder inside the user's project that persists [project state](project-state.md) between sessions.

**Optional means optional.** Without it, AI Writer runs in legacy mode: supplied files are source material and state lives in the conversation. Existing projects never have to migrate.

---

## Layout

```text
.ai-writer/
  project.yaml         metadata, provenance, intent_lock, reader_state, continuity, pack list
  canon.yaml           canon facts with provenance
  story-genome.yaml    story_genome
  outline.yaml         rough and detailed outline, goals
  timeline.yaml        temporal event facts
  open-loops.yaml      curiosity / suspense / reveal / clue / promise threads
  setup-payoff.yaml    setup/payoff ledger
  characters/<id>.yaml
  relationships/<a>--<b>.yaml     (ids in alphabetical order)
  world/<topic>.yaml              rules, places, institutions, social state
  packs/<pack-id>.yaml            pack_state for that pack
  research/<topic>.yaml
  summaries/<scope>.md            short prose summaries for retrieval
  snapshots/<date>-<label>/       copies taken before risky changes
```

Starter files: [templates/workspace/](../templates/workspace/). Each file maps to one branch of the [project-state model](project-state.md#the-model). A branch the project doesn't use has no file.

### Design rules

- **Human-readable.** Plain YAML and Markdown with comments. A writer should be able to open and edit any file.
- **Compact.** Store facts, ids, and short summaries, never copies of the manuscript. Point at manuscript files by path.
- **The user's files stay primary.** Manuscripts, notes, and wikis the user already keeps are source material. The workspace indexes them; it doesn't replace them.
- **No silent canon writes.** Anything the agent writes carries provenance. Nothing becomes `user_confirmed` without the user.
- **Stable ids.** Kebab-case ids (`lena`, `lena--marcus`, `e-014`). Renaming a character changes `persona.name`, not the id.

---

## Initializing

Create a workspace only when the user asks, or after offering one and hearing yes. Offer when a project has several chapters, several sessions, or canon heavy enough that re-reading it every time is wasteful.

```text
1. Confirm the project root with the user.
2. Create .ai-writer/ and copy project.yaml and canon.yaml from templates/workspace/.
3. Fill metadata. Set provenance.default_status: agent_proposal.
4. Ask which existing files are source of truth. Record them in provenance.source_of_truth.
5. Seed state from what is already established:
     - facts from source-of-truth files → canon.yaml as source_canon
     - facts the user stated in conversation → user_confirmed
     - anything the agent inferred → agent_proposal, listed for review
6. Create other files only when their branch has content.
7. Show the user a summary: what was seeded, and which proposals need review.
```

Seeding never rewrites the user's files.

---

## Retrieval

Load what the current task needs, not the workspace.

```text
1. Always: project.yaml (small by design).
2. From the route: the branches its modules need.
3. From the request: extract entities (characters, places, objects, open questions).
4. Load their records: characters/<id>, relationships/<a>--<b>, world/<topic>.
5. Timeline: events involving those entities, most recent first, plus any event
   those entities' open loops reference.
6. Open loops and setups touching those entities or this chapter.
7. Summaries: the previous unit in full; older units by summary only.
8. Stop when the drafting packet is full (core/memory.md#structured-drafting-context).
```

Prefer summaries and current state over raw history. A character's `developing_state` already reflects past events; the timeline is there to answer *when* and *who knew*.

---

## Updating

After a planning or drafting step, extract changes (see [state extraction](router.md#10-state-extraction)) and write them:

- **Append, supersede, don't delete.** Changed facts get `superseded_by`; timeline events are never edited to say something different.
- **Tag provenance.** User statements → `user_confirmed`. Agent inventions → `agent_proposal` or `delegated_decision`.
- **Touch only affected files.** Update `project.yaml`'s `metadata.updated`.
- **Summarize finished units.** When a chapter is final, write `summaries/<chapter>.md` and list its event ids.
- **Report.** End with a short list of what changed in state and which proposals await approval. Don't bury canon changes in prose.

Conflicts found while updating go to the [canon resolver](canon-resolver.md). The update step never settles them on its own.

---

## Snapshots and recovery

**Snapshot before risky changes:** a retcon, a bulk import, a schema migration, or any change the user flags as major.

```text
.ai-writer/snapshots/2026-09-16-before-retcon/   ← copy of the affected files
```

If the project is a git repository, a commit is a better snapshot; say so and let the user decide.

**Recovery:**

| Problem | Response |
|---|---|
| A file won't parse | Stop writing to it. Show the error and the line. Offer to restore the latest snapshot or repair by hand. Never regenerate it from memory. |
| State contradicts the manuscript | Treat as a canon conflict. Report both sides. |
| State looks stale (manuscript changed outside a session) | Re-extract from the changed chapters, propose updates, and apply them after review. |
| Workspace missing or deleted | Fall back to legacy mode. Offer to rebuild from source files; rebuilt facts start as `source_canon` or `agent_proposal`, never `user_confirmed`. |
| Unknown `schema_version` | Read what you can; don't write. Tell the user. |

---

## Schema version

`metadata.schema_version: 1` is this layout. A future layout change must ship a migration note in [CHANGELOG](../CHANGELOG.md), and the agent must snapshot before migrating.
