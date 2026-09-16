# Translation Limits

AI Writer is a set of instructions for one language model. Many of the systems it learns from are not. This page lists where the skill **approximates** a research system, what it does instead, and what that costs.

**Rule:** never claim exact reproduction when only an approximation is possible.

---

| Research system | What it actually uses | What AI Writer does instead | What is lost |
|---|---|---|---|
| Avoidance decoding [@avoidance-decoding] | Logit penalties during decoding | Candidate populations, explicit comparison, negative examples, regeneration | Token-level control; guaranteed diversity |
| Novelty measurement [@genie], [@noveltybench] | Large generated populations, embeddings, trained classifiers | Named novelty axes; "what would ten generations usually do?" reasoning | A real reference population; calibrated scores |
| Discourse similarity [@qudsim] | LLM question generation and answer matching at scale | Hand-written question sequences compared qualitatively | Scale and consistency |
| Associative search [@create] | Knowledge graphs, LLM judges, embedding distance | Concept extraction and bridge generation with qualitative quality × distance | Measured distance |
| Narrative defaults [@storyscope] | LLM feature extraction over 61k stories, trained classifiers | A qualitative anti-default checklist | Detection accuracy; corpus grounding |
| Outline control [@doc] | A decoding controller with a trained discriminator | Outline nodes in context and prompt instructions to follow them | Enforced faithfulness |
| Temporal memory [@dome] | A knowledge-graph store with retrieval | `timeline` event facts, summaries, selective retrieval ([workspace](../runtime/workspace.md)) | Automated retrieval quality |
| Multi-agent generation [@personas-to-plot], [@critics], [@bookworld], [@storybox] | Separate LLM agents, often with shared external state | One model playing separated roles in distinct passes, each given only the context that role should have | True independence between roles; a model may leak knowledge across roles |
| Consistency checking [@lost-in-stories] | An automated checker over a benchmark | A structured, category-guided pass that must cite both sides | Recall; automated coverage |
| Psychological depth judging [@psych-depth] | Persona-prompted LLM judges validated against humans | Persona critics as diagnostics | Validation; the paper's judges only roughly match humans |
| Mental-state representation [@beyond-words] | Linear probes and activation steering | Written belief–desire–intention state | Access to internal representations |
| Fear and enjoyment [@andersen-2020] | Heart-rate monitoring in a live attraction | A planned dread curve with recovery beats | Measurement; the finding is from a physical setting, not reading |

---

## What this means in practice

- **Separated roles leak.** When one model plays a character who shouldn't know something, the knowledge is still in context. The [Perspective Filter](../core/character-model.md#perspective-filter) reduces this; it can't eliminate it. The knowledge-boundary fixture ([F12](../tests/fixtures/F12-knowledge-boundary.yaml)) tests for it.
- **Diversity isn't guaranteed.** Asking for different candidates helps; it doesn't enforce distance. The creativity module requires candidates to differ on at least two substantive axes for that reason.
- **Qualitative scores are navigation aids.** No 1–5 estimate in this skill is a measurement.
- **Evaluation needs people.** Automated judges align poorly with human creativity ratings [@limits-auto-eval]. See the [benchmark](benchmark.md).
