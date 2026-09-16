# Research: Character Cognition

Sources behind the theory-of-mind parts of [core/character-model.md](../../core/character-model.md) and the knowledge boundaries in [dialogue](../../core/dialogue.md). Citations re-verified 2026-09-16.

## Entries

### `think-twice`

- **Source:** Wilf, Lee, Liang & Morency, "Think Twice: Perspective-Taking Improves Large Language Models' Theory-of-Mind Capabilities," ACL 2024. https://aclanthology.org/2024.acl-long.451/
- **Type:** empirical
- **Status:** verified
- **Claim:** SimToM, a two-stage prompt — first filter context to what a character knows, then answer about that character's mental state — improves theory-of-mind benchmark performance without training.
- **Derives:** The two-stage Perspective Filter; separating world truth, observation, interpretation, belief, and intention.
- **Limitations:** Evaluated on ToM question-answering benchmarks, not fiction generation.
- **Fidelity:** exact — it is a prompting procedure, reproduced as one. Its effect on fiction quality is not measured.

### `beyond-words`

- **Source:** Jafari, Hua, Xue & Salim, "Beyond Words: Integrating Theory of Mind into Conversational Agents for Human-Like Belief, Desire, and Intention Alignment," Findings of ACL 2025. https://aclanthology.org/2025.findings-acl.287/
- **Type:** empirical
- **Status:** verified
- **Claim:** Probes find belief, desire, and intention representations inside LLaMA-3 models; steering them improves aligned responses in negotiation dialogue.
- **Derives:** The belief–desire–intention loop and second-order social reasoning as explicit state.
- **Limitations:** Uses linear probes and activation steering, which a skill cannot do.
- **Fidelity:** conceptual — the BDI representation is written out as text, not probed or steered.
