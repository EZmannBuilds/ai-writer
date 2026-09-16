# AI Writer Benchmark v0.2
## v0.3 vs v0.4 Craft Integration

## Goal

Test whether the new craft layer improves reader-facing fiction rather than merely increasing prompt complexity.

## Conditions

```text
A = AI Writer v0.3
B = AI Writer v0.4
```

Match:
- model;
- prompt;
- context;
- approximate length;
- source/canon material;
- sampling settings where controllable.

Blind labels and randomize order.

## Pairwise questions

1. Which scene is easier to visualize without feeling over-described?
2. Which uses showing/telling more effectively?
3. Which dialogue has stronger subtext?
4. Which characters sound more distinct?
5. Which has clearer POV control?
6. Which uses backstory/exposition more naturally?
7. Which scene openings get to the meaningful pressure faster?
8. Which scene endings stop at a stronger moment?
9. Which details feel more specific and less generic?
10. Which story trusts the reader more?
11. Which setup/payoff is more satisfying?
12. Which protagonist behavior feels more psychologically motivated?
13. Which has better pacing between scene and summary?
14. Which ending feels more earned without over-explaining?
15. Which would you rather continue reading?
16. Which is better overall?

Allow:
- A;
- B;
- tie.

## Diagnostic failure tags

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
setup_no_payoff:
payoff_no_setup:
theme_overexplained:
ending_too_neat:
ending_too_abrupt:
```

## Important

Do not use an automated judge as the sole authority for:
- beauty;
- voice;
- emotional impact;
- originality;
- humor;
- literary value.

Use human reader comparison.
