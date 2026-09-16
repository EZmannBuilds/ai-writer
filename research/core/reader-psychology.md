# Research: Reader Psychology

Sources behind [reader-state](../../core/reader-state.md), [suspense-curiosity-surprise](../../core/suspense-curiosity-surprise.md), [information-architecture](../../core/information-architecture.md), and situation-model [continuity](../../core/continuity.md). Citations re-verified 2026-09-16 unless noted.

These mechanisms describe *readers*. The skill uses them to plan reader experience; it cannot measure it.

## Entries

### `suspense-planning`

- **Source:** Xie & Riedl, "Creating Suspenseful Stories: Iterative Planning with Large Language Models," EACL 2024. https://aclanthology.org/2024.eacl-long.147/
- **Type:** empirical
- **Status:** verified
- **Claim:** A zero-shot prompting planner grounded in suspense theory — a protagonist in a dire situation, iterative action planning with reasons each action might fail — produces suspenseful stories without training data. Human evaluation.
- **Derives:** Suspense threads, adversarial suspense planning, knowledge disparity, pre-failure clue options.
- **Limitations:** Short stories; one evaluation setup.
- **Fidelity:** exact — it is a prompting method, reproduced here as a procedure. Its reported results were not re-measured.

### `brewer-lichtenstein-1982`

- **Source:** Brewer & Lichtenstein, "Stories Are to Entertain: A Structural-Affect Theory of Stories," Technical Report 265, Center for the Study of Reading, University of Illinois, 1982 (journal version: *Journal of Pragmatics* 6, 1982). https://eric.ed.gov/?id=ED222854
- **Type:** theoretical
- **Status:** verified (abstract only)
- **Claim:** Surprise, suspense, and curiosity drive story enjoyment, and each comes from a particular ordering of events relative to their telling.
- **Derives:** The distinction between the three mechanisms and the idea that discourse order is a design lever.
- **Limitations:** Only the abstract was read; the specific ordering definitions come from secondary summaries. General, not genre-specific.
- **Fidelity:** conceptual

### `loewenstein-1994`

- **Source:** Loewenstein, "The Psychology of Curiosity: A Review and Reinterpretation," *Psychological Bulletin* 116(1), 75–98, 1994. https://doi.org/10.1037/0033-2909.116.1.75
- **Type:** theoretical
- **Status:** verified
- **Claim:** Curiosity is a deprivation felt when attention falls on a gap in knowledge relative to a reference point; it can increase as knowledge grows and the answer feels closer; insight problems produce more curiosity than incremental ones; satisfied curiosity tends to disappoint.
- **Derives:** Recognizable information gaps, gap-width calibration, narrowing the field over time, one-insight solutions, and planning a payoff beyond the bare answer.
- **Limitations:** A review of general curiosity research, not fiction reading.
- **Fidelity:** conceptual

### `narrative-surprise`

- **Source:** Bissell, Paulin & Piper, "A Theoretical Framework for Evaluating Narrative Surprise in Large Language Models," WNU 2025. https://aclanthology.org/2025.wnu-1.7/
- **Type:** empirical
- **Status:** verified
- **Claim:** Six criteria (initiatoriness, immutability violation, predictability, post-dictability, importance, valence) were applied to 120 human and LLM endings of 30 mystery stories; four correlated with reader preference, and human endings still ranked higher.
- **Derives:** The surprise profile, construction procedure, red-team, and the caution against turning "negative valence" into a rule.
- **Limitations:** Small corpus; mystery endings only; audience-dependent.
- **Fidelity:** conceptual — used as diagnostics, not scores.

### `event-indexing`

- **Source:** Zwaan, Langston & Graesser, "The Construction of Situation Models in Narrative Comprehension: An Event-Indexing Model," *Psychological Science* 6(5), 292–297, 1995. https://doi.org/10.1111/j.1467-9280.1995.tb00513.x
- **Type:** empirical
- **Status:** verified
- **Claim:** Readers index story events along time, space, protagonist, causality, and intentionality; shifts on these dimensions require model updating.
- **Derives:** The reader situation model and transition checks (what stayed continuous, what changed).
- **Limitations:** Lab experiments with verb-clustering tasks.
- **Fidelity:** conceptual

### `green-brock-2000`

- **Source:** Green & Brock, "The Role of Transportation in the Persuasiveness of Public Narratives," *Journal of Personality and Social Psychology* 79(5), 701–721, 2000. https://doi.org/10.1037/0022-3514.79.5.701
- **Type:** empirical
- **Status:** verified
- **Claim:** Develops a scale for transportation — absorption into a narrative through attention, imagery, and feeling — and shows greater transportation increases story-consistent beliefs.
- **Derives:** Transportation as a reader-state lens: cognitive, emotional, and imagery involvement; transportation breakers.
- **Limitations:** Focused on persuasion; self-report scale.
- **Fidelity:** conceptual

### `van-laer-2014`

- **Source:** van Laer, de Ruyter, Visconti & Wetzels, "The Extended Transportation-Imagery Model: A Meta-Analysis of the Antecedents and Consequences of Consumers' Narrative Transportation," *Journal of Consumer Research* 40(5), 797–817, 2014. https://doi.org/10.1086/673383
- **Type:** empirical
- **Status:** verified
- **Claim:** A meta-analysis of 76 articles modeling what increases narrative transportation and what it affects.
- **Derives:** Transportation prerequisites (identifiable characters, imaginable plot, verisimilitude).
- **Limitations:** Consumer-research framing; many studies use short or commercial narratives.
- **Fidelity:** conceptual

### `fiction-flows`

- **Source:** Piper, Hamilton, Zhou & Pianzola, "Fiction Flows: A Replication and Reinterpretation of Narrative Sequentiality," ACL 2026. https://aclanthology.org/2026.acl-long.1576/
- **Type:** empirical
- **Status:** verified (author first name corrected: Haiqi Zhou)
- **Claim:** A multi-model replication of an LM-based "sequentiality" measure found the earlier imagined-vs-recalled contrast weakens under other setups, while fiction keeps a robust sequentiality advantage over reality-bound genres.
- **Derives:** Treat flow as event-level (expectation, memory, causal and goal continuity), and don't optimize sentence-level predictability.
- **Limitations:** Measures are LM log-probabilities.
- **Fidelity:** conceptual — used as a caution.
