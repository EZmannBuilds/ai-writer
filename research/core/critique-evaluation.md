# Research: Critique and Evaluation

Sources behind [core/critics.md](../../core/critics.md), the anti-default audit, and the [benchmark](../benchmark.md). Citations re-verified 2026-09-16.

## Entries

### `storyscope`

- **Source:** Russell, Rajendhran, Pham, Iyyer & Wieting, "StoryScope: Investigating idiosyncrasies in AI fiction," COLM 2026 (arXiv 2604.03136). https://arxiv.org/abs/2604.03136
- **Type:** empirical
- **Status:** verified
- **Claim:** 304 story-level features across 10 dimensions, extracted from 61,608 ~5,000-word stories, separate human from AI fiction without style signals. AI stories over-explain themes and favor tidy single-track plots; human stories show more moral ambiguity and temporal complexity and occupy a wider feature space.
- **Derives:** The anti-default audit (thematic over-determination, embodied overperformance, structural streamlining, reduced range) and the structural rarity pass.
- **Limitations:** Aggregate corpus differences, not a recipe. Uses LLM feature extraction, embeddings, and trained classifiers. Inverting the findings mechanically would create a new formula.
- **Fidelity:** approximate — the feature dimensions become a qualitative checklist; no classifier is run.

### `critics`

- **Source:** Bae & Kim, "Collective Critics for Creative Story Generation," EMNLP 2024. https://aclanthology.org/2024.emnlp-main.1046/
- **Type:** empirical
- **Status:** verified
- **Claim:** CritiCS runs persona-based critic groups and a leader over a plan stage and a text stage to raise creativity while keeping coherence.
- **Derives:** Macro critics (theme/plot/setting, structure, ending), micro critics (image, voice), the critic leader, and multi-round plan refinement.
- **Limitations:** Multiple LLM agents.
- **Fidelity:** approximate — one model plays separated critic roles in distinct passes.

### `psych-depth`

- **Source:** Harel-Canada et al., "Measuring Psychological Depth in Language Models," EMNLP 2024. https://aclanthology.org/2024.emnlp-main.953/
- **Type:** empirical
- **Status:** verified
- **Claim:** The Psychological Depth Scale (empathy, engagement, emotion provocation, authenticity, narrative complexity) is applied consistently by humans; persona-prompted LLM judges roughly track human ratings.
- **Derives:** The five-dimension scale and the persona-specific critic council; the rule not to average the profile into one number.
- **Limitations:** Judges roughly — not reliably — match humans; Reddit comparison corpus.
- **Fidelity:** approximate

### `limits-auto-eval`

- **Source:** Tutone, Franceschelli & Musolesi, "The Limits of Automatic Evaluation of Creativity in Large Language Models," arXiv 2608.23705, 2026 (preprint). https://arxiv.org/abs/2608.23705
- **Type:** empirical
- **Status:** verified; preprint.
- **Claim:** 115 human raters scored stories on 11 creativity dimensions; seven automatic metrics and an LLM judge aligned poorly with them.
- **Derives:** The automatic-judge warning, labeled findings, and human pairwise evaluation as the primary benchmark method.
- **Limitations:** Preprint; WritingPrompts stories.
- **Fidelity:** conceptual
