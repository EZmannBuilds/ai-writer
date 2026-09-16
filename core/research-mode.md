# Research Mode

Research-grounded fiction without research-driven fiction. This module decides **which details actually need verifying**, labels every fact-shaped claim by how it was established, and keeps research from dictating artistic choices.

| Contract | |
|---|---|
| Invoked by | Router when the request touches a real domain (see triggers below), or when a pack flags `research_needs` (Draft Starter, Origin Forge's authenticity branch). |
| When | Before outlining or drafting material whose credibility depends on real-world accuracy; again before returning the draft. |
| Needs | The request; `intent_lock.format` and realism level; any `research_needs` from pack briefs. |
| Produces | A research plan (which details, what depth), `research` entries with fact labels, and a fact-label pass on the draft. |
| State | `research` — `.ai-writer/research/<topic>.yaml`. |
| Consumed by | [world-state](world-state.md), [prose](prose.md), [information-architecture](information-architecture.md) (need-to-know routing for what reaches the page). |
| Skip when | The detail doesn't bear weight: nobody in the story or audience would act on it, and a plausible invention does no harm. Pure secondary-world fantasy with no real-world analogue claimed. |
| Tests | F20 |
| Research | [research/README](../research/README.md#how-research-is-used) |

---

## Triggers

The router considers research mode when a story includes any of:

- military procedure, rank, equipment, or chain of command;
- medicine, injury, illness, pharmacology, or mental health;
- law, courts, policing, or incarceration;
- a historical setting or real historical event;
- a real culture, religion, language, or community;
- science or technology presented as real;
- a technical profession (surgery, aviation, diving, finance, engineering...);
- a real place.

A trigger means *consider*. It does not mean *research everything*.

---

## Verification triage

For each fact-shaped detail, ask three questions:

```text
1. LOAD — does the plot, a character decision, or a reader's trust depend on it?
2. EXPOSURE — will readers with real knowledge notice if it's wrong?
3. HARM — could getting it wrong mislead someone about something real
   (medical, legal, safety), or misrepresent a real community?
```

| Load / exposure / harm | Action |
|---|---|
| Any **harm** | Verify, or fictionalize visibly. Never present unverified safety, medical, or legal procedure as fact. |
| High load **or** high exposure | Verify before drafting. |
| Low on all three | Plausible invention is fine. Label it. |
| Deliberately altered | Fictionalize on purpose and label it. |

Do not research details that don't matter. A story set in Chicago does not need the bus schedule unless someone misses the bus.

---

## Fact labels

Every research-sensitive claim gets exactly one label while planning. Labels live in state and planning notes, never in the prose.

```yaml
research_item:
  topic:
  claim:
  label: verified | plausible_invention | deliberate_fictionalization | unverified
  source:              # required when label is verified
  confidence:          # high | medium | low
  story_use:           # which scene/decision depends on it
  depth_needed:        # background | credible | expert
  notes:
```

- **verified** — checked against a source this session or a source already recorded in `research`. Cite it.
- **plausible_invention** — invented, consistent with how the real thing works as far as is known, low-stakes. Not presented as documented fact outside the fiction.
- **deliberate_fictionalization** — changed on purpose (a fictional city beside a real one, an invented military unit, altered history). Record what was changed and why.
- **unverified** — believed but not checked. Must be verified or relabeled before it bears plot weight.

When web access is unavailable, say so. Everything that would have been `verified` becomes `unverified`, and the user hears which details need checking.

---

## Depth

```text
background — enough that nothing is wrong on the page
credible   — an informed reader nods along
expert     — a practitioner would recognize their world
```

Take depth from `intent_lock` or the Draft Brief's realism level. Default to **credible** for load-bearing details and **background** for everything else.

---

## Research-grounded generation vs research-driven formula

Research answers factual questions. It does not make artistic decisions.

- Record constraints; do not let them decide what the story is about.
- A real procedure can be compressed, skipped, or broken by a character. The story needs to know the procedure exists and what breaking it costs.
- Research reaches the page only in the quantity the story can metabolize. See [the research-flex mistake](revision.md#common-human--novice-writer-mistake-audit) and [need-to-know routing](information-architecture.md#exposition-and-backstory-need-to-know-routing).
- A deliberately fictionalized world (a fictional city, an alternate agency) is not an error to correct. Check its provenance in [the canon resolver](../runtime/canon-resolver.md) before "fixing" it.

---

## Procedure

```text
1. List research-sensitive details from the request and pack briefs.
2. Triage each (load / exposure / harm).
3. Verify what must be verified; cite sources.
4. Label everything else.
5. Record items in `research`.
6. Draft.
7. Fact-label pass: scan the draft for fact-shaped claims without a label.
8. Tell the user which details are unverified or deliberately fictionalized, if any bear weight.
```
