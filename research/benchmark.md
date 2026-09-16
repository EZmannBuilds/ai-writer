# Benchmark

Does AI Writer produce better fiction than simply asking the same model? This benchmark is how to find out. It replaces the v0.2 benchmark (v0.3 vs v0.4), which compared two versions of the skill rather than the skill against a baseline; that version is preserved at the `v0.5-baseline` tag.

The [regression suite](../tests/README.md) checks that the system *behaves* as specified. This benchmark asks whether that behavior makes stories *better*. They answer different questions; passing one says nothing about the other.

---

## Conditions

```text
A = baseline      the same model, prompted directly with the task
B = AI Writer     the same model with this skill loaded
```

Hold constant:

- model and version;
- the task prompt (B gets the same words; the skill does the rest);
- supplied context and canon;
- approximate length (±15%);
- content constraints;
- sampling settings where controllable;
- number of turns. If B asks questions, a scripted "user" gives the same answers A would have been given up front.

Generate **at least 3 samples per condition per task** so diversity can be compared, not only quality.

---

## Task set

| # | Task | Prompt sketch | What it stresses |
|---|---|---|---|
| T1 | Short scene | Two siblings argue in a hospital parking lot about a forged will; 800 words. | Scene craft, subtext, knowledge boundaries |
| T2 | Dialogue | A job interview where the candidate knows the interviewer ruined her father. | Hidden sentences, tactics, voice distinction |
| T3 | Short story | A complete 3,000-word story from a one-line seed. | Structure, originality, ending |
| T4 | Mystery | A 5,000-word locked-room mystery with a fair solution. | Clues, false solution, reveal |
| T5 | Character-driven chapter | Chapter 6 of a supplied outline with character files. | Agency, state, relationship change |
| T6 | Long-form continuation | Continue chapter 12 from supplied chapters 1–11 summaries and state. | Continuity, memory, carry-forward |
| T7 | Tragic action | A battle chapter with a planned loss in a supplied ensemble. | Consequence, residue, grief diversity |
| T8 | Romance | The scene where two partners discover they disagree about what they are. | Perception gaps, disclosure, subtext |
| T9 | Horror | A 2,000-word horror story set in a familiar domestic space. | Dread curve, restraint, anti-defaults |
| T10 | Comic output | A 4-page panel breakdown of an origin's turning point. | Drawability, page turns, lettering load |

Keep tasks and inputs in a fixed file so runs are comparable across versions.

---

## Human pairwise evaluation

Human judgment is **primary** for:

- emotional impact;
- voice;
- beauty;
- originality;
- humor;
- overall literary value.

Procedure:

1. Pair one A and one B output for the same task and sample index.
2. Blind the labels and randomize order.
3. Give raters the task prompt, not the method.
4. Ask each question below; allow **A**, **B**, or **tie**.
5. Use several raters per pair; report agreement.
6. Include a few **A-vs-A** pairs as a sanity check: they should split near evenly.

**Questions**

1. Which would you rather keep reading?
2. Which has more believable character behavior?
3. Which is less predictable?
4. Which has a more meaningful surprise or turn (if any)?
5. Which creates stronger curiosity?
6. Which feels more emotionally authentic?
7. Which is more coherent?
8. Which feels more distinctive — less like something you've read many times?
9. Which has the more specific voice?
10. Which uses showing and summary more effectively?
11. Which trusts the reader more?
12. Which ending feels more earned?
13. *(T4)* Could you have solved it, looking back? Was it fair?
14. *(T9)* Which built more dread?
15. *(T8)* Which relationship felt more real?
16. *(T10)* Which could an artist draw more easily?
17. Which is better overall?

Report per-question preference with confidence intervals, per task. Don't collapse the profile into one number.

---

## Automated checks

Automated analysis **may assist** with:

| Check | How |
|---|---|
| Continuity | Category-guided contradiction search with evidence from both sides |
| Knowledge violations | Does any character act on information they couldn't have? |
| Repeated motifs | Count and locate recurring images and phrases |
| Structural duplication | Question-sequence comparison across samples ([discourse diversity](../core/creativity-search.md#discourse-diversity-check)) |
| Setup/payoff | Emphasized elements that never return; payoffs with no seed |
| Lexical repetition | Repeated phrases and tics within and across samples |
| Diversity | How different are the three samples within each condition? |
| Compliance | Length, POV, tense, content constraints |

Automated checks must **not** judge beauty, emotional impact, humor, originality, or overall value. Automatic creativity metrics and LLM judges align poorly with human ratings [@limits-auto-eval].

**Anti-homogenization rule.** Never feed automated scores back into generation as targets. An automated critic that prefers clarity will sand away deliberate ambiguity, and one that prefers resolution will close open endings. When a check flags an unusual choice, a human decides whether it was a defect or the point (see [critics](../core/critics.md#automatic-judge-warning)).

---

## Diagnostic tags

Raters may tag failures in either output:

```yaml
too_much_telling:
showing_overkill:
stock_body_language:
generic_detail:
inventory_description:
head_hopping:
psychic_distance_jolt:
exposition_dump:
expository_dialogue:
on_the_nose_dialogue:
same_voice:
scene_starts_early:
scene_lingers:
scene_no_change:
weak_stakes:
plot_puppet_behavior:
knowledge_violation:
setup_no_payoff:
payoff_no_setup:
unfair_reveal:
constant_intensity:
cliche_default:
relationship_flattened:
undrawable_panel:
theme_overexplained:
ending_too_neat:
ending_too_abrupt:
```

---

## Reporting

For each run record: date, model, skill version (git hash), task file version, sample counts, rater count, per-question results, tag counts, and notes on anything that broke the matched conditions.

**No benchmark run has been recorded yet.** Until one is, the skill's claim to improve fiction is a hypothesis supported by its sources and by passing behavior tests — not a measured result.
