# Research

Why AI Writer's rules are what they are, and how far each rule can be trusted.

```text
research/
  README.md              this file
  source-index.md        every source, one row per citation key (generated)
  translation-limits.md  where a text-only skill only approximates a research system
  benchmark.md           how to test whether the system actually improves fiction
  core/                  sources behind the core modules
  packs/                 sources behind each pack
  passes/                historical research syntheses, kept as written
```

---

## How research is used

**Research mechanisms are tools and diagnostics, not commandments.** A finding widens the option space or catches a default. It never overrides what the user wants, and it never becomes a template.

Every research-derived mechanism records five things:

| Field | Question |
|---|---|
| **Source** | Who said it, where, when? |
| **Claim** | What does the source actually say? |
| **Derives** | What does AI Writer take from it? |
| **Limitations** | Sample, scope, era, method — why might it not transfer? |
| **Fidelity** | Does the skill do what the source does, or only something like it? |

Entries also carry a **Type** (empirical, theoretical, historical-primary, genre-scholarship, craft-practice, design, …) and a **Status** (verified on a date, details corrected, recorded but not re-verified, or unverified).

Modules cite sources inline as `[@key]`, and each module's contract table links its research file. The validator fails on an unknown key and on any core or pack section that talks about research findings without citing one.

### Fidelity

| Fidelity | Meaning | Examples |
|---|---|---|
| `exact` | The skill performs the source's method. | Perspective filtering (a prompting method to begin with) |
| `approximate` | The source uses tools the skill lacks; the skill imitates the effect with structured prompting. | Avoidance decoding, novelty measurement, multi-agent generation |
| `conceptual` | The source informs the design as an idea. | Transportation, attachment, curiosity theory |
| `convention` | A craft or genre convention, not evidence. | Knox's rules, script formats, show-don't-tell advice |
| `design` | A decision with no external source. | Draft Starter's interview limits, the Series engine |

**Never claim `exact` for an approximation.** See [translation limits](translation-limits.md).

---

## Verification status (v0.6/v0.7 pass, 2026-09-16)

- **Core research papers (24 citations):** all re-verified. Five had details corrected: DOME's published title, NoveltyBench's renamed title, BookWorld's title and venue, StoryBox's title and venue, and MAGNET, which is the system in *From Personas to Plot*, not a separate paper. Four are preprints and are labeled as such.
- **Mystery, horror, romance:** new research passes; every URL was fetched, and partial reads (abstract only, press release only, secondary summary) are marked on the entry.
- **Origin Forge, Tragic engine, Comic Panel Writer:** sources come from each pack's original v1.0 research notes. They were brought into the repository for the first time in this pass but **not re-verified**.
- **Page-craft sources (v0.4):** carried forward, **not re-verified**.

Known disputes and gaps are recorded where they apply: contested spoiler research ([mystery](packs/mystery.md)); missing sources for isolation, disbelief, and aftermath ([horror](packs/horror.md)); heterosexual and WEIRD samples ([romance](packs/romance.md)); unverified King's *Danse Macabre* levels ([horror](packs/horror.md#king-1981)).

---

## Genre coverage

| Area | Status |
|---|---|
| Character psychology, suspense, curiosity, surprise, continuity, originality, long-form planning, transportation | Research-grounded core mechanisms |
| Mystery / investigation | Pack with a dedicated research pass |
| Horror / dread | Pack with a dedicated research pass; some guidance is craft inference |
| Romance / attachment | Pack with a dedicated research pass |
| Tragedy / dark action | Pack grounded in creator and publisher material |
| Origins | Pack grounded in moral-injury and moral-disengagement research |
| Comics | Pack grounded in publisher and practitioner conventions |
| Series, worldbuilding | Design modules; no dedicated research pass yet |
| Humor, erotic narrative, thriller, literary realism | No dedicated module. Use general writing knowledge and say so. |

When no module covers a genre, don't present general craft knowledge as research-derived.

---

## Adding research

1. Add an entry in the right `core/` or `packs/` file using the five fields plus Type and Status.
2. Run `python3 scripts/build_source_index.py`.
3. Cite it as `[@key]` where the mechanism is used.
4. Run `python3 scripts/validate.py`.

Don't invent sources, authors, years, findings, or URLs. When a source can't be verified, say so on the entry.
