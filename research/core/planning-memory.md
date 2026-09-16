# Research: Planning, Memory, and Agents

Sources behind [outlining](../../core/outlining.md), [memory](../../core/memory.md), [continuity](../../core/continuity.md), [character-agency](../../core/character-agency.md), and the [Story Genome](../../core/story-genome.md). Citations re-verified 2026-09-16.

**Translation note.** These systems use external memory stores, knowledge graphs, trained controllers, and multiple LLM agents. AI Writer approximates them with structured state ([project state](../../runtime/project-state.md), the optional [workspace](../../runtime/workspace.md)) and with separated reasoning passes in one model.

## Entries

### `doc`

- **Source:** Yang, Klein, Peng & Tian, "DOC: Improving Long Story Coherence With Detailed Outline Control," ACL 2023. https://arxiv.org/abs/2212.10077
- **Type:** empirical
- **Status:** verified
- **Claim:** A detailed hierarchical outliner moves creative work into planning; a controller keeps passages faithful to the outline. Human raters preferred it over the prior system on coherence, relevance, and interest.
- **Derives:** Recursive outline expansion, candidate child events, explicit setting/character association per node, and a compact drafting packet that includes the next node.
- **Limitations:** The controller is a FUDGE-style decoding modification with a trained relevance discriminator.
- **Fidelity:** approximate — outline structure is implemented; the controller becomes a prompt instruction.

### `dome`

- **Source:** Wang et al., "Generating Long-form Story Using Dynamic Hierarchical Outlining with Memory-Enhancement," NAACL 2025. https://aclanthology.org/2025.naacl-long.63/
- **Type:** empirical
- **Status:** verified; title corrected (v0.5 cited it by its method name, DOME).
- **Claim:** Merging planning and writing through a dynamic outline, plus a temporal knowledge-graph memory of generated content, reduces contradictions in long stories.
- **Derives:** Rough outline plus just-in-time detailed outline; alternate plan/write; a temporal event graph; targeted retrieval.
- **Limitations:** Uses an actual knowledge graph and retrieval system.
- **Fidelity:** approximate — `timeline` event facts and selective retrieval replace the graph store.

### `lost-in-stories`

- **Source:** Li et al., "Lost in Stories: Consistency Bugs in Long Story Generation by LLMs," Findings of ACL 2026. https://aclanthology.org/2026.findings-acl.410/
- **Type:** empirical
- **Status:** verified
- **Claim:** A benchmark and a 5-category, 19-subtype error taxonomy for long stories, plus an evidence-grounded automatic checker. Errors cluster in factual and temporal details and mid-narrative.
- **Derives:** The consistency taxonomy; the requirement that a continuity finding cite evidence from both sides; extra vigilance mid-story.
- **Limitations:** The checker is an automated LLM pipeline over a benchmark.
- **Fidelity:** approximate — the taxonomy is used as-is; checking is a structured pass, not the benchmark tool.

### `personas-to-plot`

- **Source:** Aluru et al., "From Personas to Plot: Character-Grounded Multi-Agent Story Generation for Long-Form Narratives," arXiv 2607.00918, 2026 (preprint). https://arxiv.org/abs/2607.00918
- **Type:** empirical
- **Status:** verified; preprint. v0.5 also referred to "MAGNET" as if it were a separate paper — MAGNET is the system proposed in this paper.
- **Claim:** Persona-grounded character agents propose actions against a shared world state and evolving goals, with critic and narrator stages; reported large hallucination reductions at 100 pages versus single-model baselines.
- **Derives:** Character action proposals, the action critic, narrator selection, goal sequencing, and stagnation monitoring.
- **Limitations:** Multiple LLM agents with an external shared world state.
- **Fidelity:** approximate — one model simulates separated roles in distinct passes, each given only perspective-filtered context.

### `bookworld`

- **Source:** Ran et al., "BOOKWORLD: From Novels to Interactive Agent Societies for Story Creation," ACL 2025. https://aclanthology.org/2025.acl-long.773/
- **Type:** empirical
- **Status:** verified; title and venue corrected (v0.5 used the arXiv title and no venue).
- **Claim:** Characters, relationships, and world rules extracted from novels are simulated as multi-agent societies to generate new stories.
- **Derives:** Optional emergent sandbox mode; social-state propagation.
- **Limitations:** Multi-agent simulation built from source novels.
- **Fidelity:** conceptual — used conservatively, as an optional technique.

### `storybox`

- **Source:** Chen, Pan & Li, "StoryBox: Collaborative Multi-Agent Simulation for Hybrid Bottom-Up Long-Form Story Generation Using Large Language Models," AAAI-26 (arXiv 2510.11618, 2025). https://ojs.aaai.org/index.php/AAAI/article/view/40288
- **Type:** empirical
- **Status:** verified; full title and venue added.
- **Claim:** Agents interact in a sandbox; the emergent events seed long stories that stay coherent past 10,000 words.
- **Derives:** Hybrid top-down/bottom-up plotting — plan the destination, simulate the local.
- **Limitations:** Requires a simulation environment and multiple agents.
- **Fidelity:** conceptual

### `human-level-narratives`

- **Source:** Tian et al., "Are Large Language Models Capable of Generating Human-Level Narratives?," EMNLP 2024. https://aclanthology.org/2024.emnlp-main.978/
- **Type:** empirical
- **Status:** verified
- **Claim:** LLM stories were uniformly positive and low in tension compared with human stories across arcs, turning points, arousal, and valence; making discourse features explicit improved generation substantially.
- **Derives:** Turning-point planning, the affect curve, the reader-state model, and the warning against positivity drift.
- **Limitations:** Corpus analysis with expert and automatic annotation.
- **Fidelity:** conceptual — the dimensions are used as planning labels, not measured.
