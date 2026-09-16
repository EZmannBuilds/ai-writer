# Research: Creativity and Diversity

Sources behind [core/creativity-search.md](../../core/creativity-search.md) and the structural-rarity check. Citations re-verified 2026-09-16.

**Translation note.** Every system here uses tools a text-only skill doesn't have: embeddings, trained classifiers, large generated populations, or decoding changes. AI Writer approximates them with structured prompting. None of these mechanisms is implemented exactly.

## Entries

### `noveltybench`

- **Source:** Zhang et al., "NoveltyBench: Evaluating Language Models for Humanlike Diversity," COLM 2025. https://arxiv.org/abs/2504.05228
- **Type:** empirical
- **Status:** verified; title corrected (the v0.5 citation used the arXiv v1 title, "…Evaluating Creativity and Diversity in Language Models").
- **Claim:** Across 20 models, repeated generations for the same prompt were far less diverse than human responses; larger models were often less diverse than smaller ones. Diversity was measured by grouping generations into equivalence classes with a fine-tuned classifier.
- **Derives:** Mode collapse is real, so important decisions need a candidate *population*, and candidates must be checked for being the same idea in different words.
- **Limitations:** Uses a trained DeBERTa classifier and a reward model; a skill can only judge "same idea" qualitatively. General prompts, not fiction specifically.
- **Fidelity:** approximate — qualitative equivalence judgment replaces the trained classifier.

### `avoidance-decoding`

- **Source:** Park, Yang & Jung, "Avoidance Decoding for Diverse Multi-Branch Story Generation," EMNLP 2025. https://aclanthology.org/2025.emnlp-main.381/
- **Type:** empirical
- **Status:** verified
- **Claim:** Penalizing token logits for similarity to already-generated branches — concept-level early, narrative-level later — increased diversity (reported up to 2.6×) and reduced repetition.
- **Derives:** Check early candidates for concept-level overlap and later ones for narrative-level overlap; regenerate near-duplicates.
- **Limitations:** The method modifies decoding. A prompt-only skill cannot touch logits.
- **Fidelity:** approximate — candidate comparison, negative examples, and regeneration stand in for logit penalties. See [translation limits](../translation-limits.md).

### `create`

- **Source:** Wadhwa et al., "CREATE: Testing LLMs for Associative Creativity," arXiv 2603.09970, 2026 (preprint). https://arxiv.org/abs/2603.09970
- **Type:** empirical
- **Status:** verified; preprint.
- **Claim:** A benchmark where models generate many paths connecting two concepts; paths are scored on specificity and diversity, rewarding many strong, distinct connections.
- **Derives:** Associative search between a premise's core concepts; preferring specific, narratively usable bridges; valuing a portfolio of distinct options (quality × distance).
- **Limitations:** Uses a Wikidata knowledge graph, LLM judges, and embeddings for path distance. Not a fiction benchmark.
- **Fidelity:** conceptual — the skill borrows the quality-plus-distance idea and qualitative 1–5 estimates.

### `genie`

- **Source:** Namuduri et al., "GENIE: A Fine-Grained Measure for Novelty," arXiv 2606.12790, 2026 (preprint). https://arxiv.org/abs/2606.12790
- **Type:** empirical
- **Status:** verified; preprint.
- **Claim:** Novelty is scored per task-specific feature, relative to a large population of responses (~10k stories from 21 models), making originality explainable feature by feature.
- **Derives:** A project-specific novelty profile with named axes; asking which axis carries the novelty and whether it's meaningful.
- **Limitations:** Requires a large reference population, LLM question generation, and embeddings. The skill has no population to compare against.
- **Fidelity:** approximate — the skill reasons about "what would ten generations of this premise usually do" instead of measuring against a corpus.

### `qudsim`

- **Source:** Namuduri et al., "QUDsim: Quantifying Discourse Similarities in LLM-Generated Text," COLM 2025. https://arxiv.org/abs/2504.09373
- **Type:** empirical
- **Status:** verified
- **Claim:** Representing documents as sequences of Questions Under Discussion reveals that LLMs reuse discourse structures across samples more than humans do, even when content differs.
- **Derives:** The discourse diversity check: compare candidates' question sequences, not only their nouns.
- **Limitations:** Uses LLM-generated questions and answer-matching at scale.
- **Fidelity:** approximate — hand-written QUD sequences compared qualitatively.
