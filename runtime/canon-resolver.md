# Canon Resolver

Decides what is true in a project when sources disagree, and keeps the difference between *canon*, *proposal*, and *belief* visible.

It runs whenever:

- two facts conflict ([continuity](../core/continuity.md) found an issue, or the user said something that contradicts state);
- the agent is about to write state;
- a proposal might be promoted to canon;
- a revision would change an established fact.

---

## Provenance statuses

| Status | Meaning | Is it canon? |
|---|---|---|
| `user_confirmed` | The user stated or approved it. | Yes |
| `source_canon` | It comes from a file the user designated as source of truth, or from supplied canon material. | Yes |
| `approved_inference` | The agent inferred it and the user approved the inference. | Yes |
| `delegated_decision` | The user delegated the choice ("you decide") and the agent made it. | Yes, provisionally — the user can overturn it without a retcon |
| `agent_proposal` | The agent suggested or invented it. Nobody approved it. | **No** |
| `uncertain` | Unclear or unverified. | No |
| `in_world_belief` | Something people in the world believe (a myth, a rumor, an official story). | True *as a belief*; says nothing about world truth |
| `character_belief` | Something a specific character believes. | True *as that character's belief* |
| `alternate_continuity` | True in a named alternate timeline, draft branch, or adaptation. | Only inside that continuity |
| `deprecated` | Once canon, now withdrawn. Kept for history. | No |
| `retcon` | An approved change that replaces earlier canon. | Yes; it supersedes what it names |

`in_world_belief` and `character_belief` are not weaker canon. They are a different kind of fact: "Most of Port Calder believes the city has always existed" can be firmly canon while the city's actual origin is something else.

---

## Precedence

When two facts about the same thing conflict **in the same continuity**, the higher line wins:

```text
1. The user's explicit correction in the current conversation
2. Designated source-of-truth files (provenance.source_of_truth, in listed order)
3. Approved retcons (they name what they replace)
4. Approved project state: user_confirmed, approved_inference
5. Earlier user decisions recorded in the conversation or history
6. Published or accepted manuscript text
7. Delegated decisions
8. Agent-authored material the user accepted without comment in a draft
9. Unapproved proposals, inferences, and uncertain facts
```

Notes:

- **Line 1 is absolute** for the fact it corrects. It is recorded as `user_confirmed` and supersedes the old fact.
- **Line 2 vs line 1.** If a correction contradicts a source-of-truth file, apply the correction and tell the user the file now disagrees. Don't edit their file unless they ask.
- **Line 6 vs line 4.** A manuscript fact that contradicts approved state is flagged, not auto-resolved. The manuscript may be wrong, or the state may be stale. Ask.
- **Line 8** exists because a user reading a draft and moving on is weak approval, not no approval. It still loses to anything the user stated.
- **Line 9 never beats anything.** A proposal cannot overwrite canon, however plausible.
- **Recency breaks ties only within a line.** The later of two `user_confirmed` facts wins; a later `agent_proposal` never beats an earlier `user_confirmed` one.

---

## Before calling something a contradiction

Many apparent contradictions are intentional. Check these before flagging:

| Situation | How to tell | Action |
|---|---|---|
| **Unreliable narrator** | The claim comes through a narrator marked unreliable in `intent_lock` or `story_genome`. | Not a defect. Track world truth separately. |
| **False character belief** | The claim is in dialogue, thought, or close POV, and conflicts with world truth. | Record as `character_belief`. Not a defect. |
| **In-world disagreement** | Cultures, factions, or historians disagree. | Record each version as `in_world_belief` with its holder. Don't pick one. |
| **Alternate continuity** | The facts belong to different named continuities. | Not a conflict. Keep both. |
| **Intentionally unresolved** | Marked `intentionally_open` in `open_loops`, or the user said the question stays open. | Leave it open. |
| **Mystery misdirection** | A planted false lead in the clue ledger. | Not a defect. |
| **Approved retcon** | A `retcon` record names the old fact. | Old fact is `deprecated`; no conflict. |
| **Deliberate stylistic rupture** | Marked in `intent_lock.stylistic_constraints`. | Not a defect. |

**Never "fix" an intentional contradiction.** When provenance is missing and you can't tell, report both sides and ask.

---

## Resolving a real conflict

```yaml
canon_conflict:
  subject:
  fact_a: {text:, source:, prov:, continuity:}
  fact_b: {text:, source:, prov:, continuity:}
  intentional_check: []       # which of the situations above were ruled out, and why
  precedence_result:          # a | b | undecided
  rule_applied:               # the precedence line
  action:                     # apply | ask_user | record_both | leave_open
  user_question:              # only when action is ask_user
```

1. Quote **both** sides with their sources. Never describe a conflict from one side.
2. Rule out the intentional situations.
3. Apply precedence.
4. If precedence decides it and the losing fact isn't something the user stated, apply it and note what changed.
5. If the losing fact was ever `user_confirmed`, or precedence is undecided, **ask**. Offer the options; don't adjudicate silently.
6. Record the resolution in `continuity.resolutions`. Supersede the losing fact; don't delete it.

---

## Promotion

A fact changes status only this way:

| From | To | Requires |
|---|---|---|
| `agent_proposal` | `approved_inference` or `user_confirmed` | The user approves it: explicitly, or by building on it in their own words ("yes, and then Mara..."). |
| `agent_proposal` | `delegated_decision` | It falls inside a decision the user delegated. |
| `delegated_decision` | `user_confirmed` | The user endorses it. |
| `uncertain` | `source_canon` / `user_confirmed` | A source or the user confirms it. |
| canon | `deprecated` | A `retcon` or a user correction supersedes it. |

The agent never promotes its own proposals. Silence after a planning message is not approval.

**Delegation has edges.** "You decide the setting" delegates the setting, not the ending. Delegated decisions stay overturnable: if the user later rejects one, it becomes `deprecated` without ceremony.

---

## What needs the user

Ask before:

- changing or superseding any `user_confirmed` or `source_canon` fact;
- resolving a conflict where precedence is undecided;
- promoting a proposal that would constrain future stories in a large way (a death, an origin, a world rule, the ending) — even under broad delegation, flag it clearly;
- writing into a source-of-truth file.

Don't ask about:

- facts the user already stated (read them);
- proposals clearly marked as proposals;
- choices inside an active delegation.

---

## Alternate continuities and retcons

```yaml
provenance:
  continuities:
    - id: main
      default: true
    - id: legends
      description: Pre-2026 material kept for reference
      relation: historical        # historical | alternate | adaptation | draft_branch
```

- Facts default to the `default: true` continuity.
- Queries run against one continuity at a time. Cross-continuity differences are never flagged as contradictions.
- A **retcon** is a canon record with `prov.status: retcon` and `supersedes: [fact ids]`. It needs user approval. The superseded facts become `deprecated` and stay in state.

---

## In planning output

When a plan mixes kinds of fact, label them so the user can see which is which:

```text
Confirmed:  Port Calder sits on the north shore.
Delegated:  The city council meets in the old mill.
Proposed:   The mayor knows the city's real origin.   ← not canon until you approve it
Open:       Who actually founded the city.
```
