# Information Architecture

Who knows what, when the reader learns it, and whether the information arrives because the scene needs it. Covers reveals, foreshadowing, exposition, and setup/payoff.

| Contract | |
|---|---|
| Invoked by | Router whenever information is withheld or released; Mystery's clue ledger and Tragic's reveal ledger extend it. |
| When | Planning a reveal; before any exposition or backstory; during the Setup/Payoff revision pass. |
| Needs | `canon`; `characters.*.mental_state`; `outline`. |
| Produces | `information_item` records; the setup/payoff ledger; exposition routing decisions. |
| State | `setups_payoffs` — `.ai-writer/setup-payoff.yaml`; reveal items under `open_loops`. |
| Consumed by | [prose](prose.md), [suspense-curiosity-surprise](suspense-curiosity-surprise.md), [mystery](../packs/mystery.md). |
| Skip when | Nothing is being concealed and no backstory is entering. |
| Tests | F16, F18 |
| Research | [research/core/reader-psychology.md](../research/core/reader-psychology.md), [research/core/page-craft.md](../research/core/page-craft.md) |

---

## Information items

For important information:

```yaml
information_item:
  truth:
  who_knows: []
  who_believes_false_version: []
  reader_state:
  first_hint:
  reinforcement:
  partial_reveal:
  full_reveal:
  recontextualizes: []
  consequences: []
```

Operations:

- reveal;
- conceal;
- distort;
- misinterpret;
- contradict;
- confirm;
- recontextualize.

A revelation is stronger when it alters meaning, not only knowledge.

---

## Revelation Test

Before accepting a twist:

- Was it prepared?
- Is retrospective evidence available?
- Does it affect decisions?
- Does it change relationships?
- Does it change the reader's model of earlier events?
- Does it create consequences?
- Is it specific to these characters?
- Would the story still function identically without it?

If yes to the last question, the twist may be decorative.

---

## Foreshadowing vs Warning

*Basis: [@suspense-planning]*

Before a planned failure or revelation, decide whether clues should:

- be invisible until retrospect;
- create unease;
- let the reader predict danger;
- misdirect;
- openly reveal danger while withholding the character's awareness.

Do not foreshadow every event in the same way.

---

## Exposition and Backstory: Need-to-Know Routing

*Basis: [@friedman-backstory], [@reedsy-exposition], [@wd-exposition-early]*

Backstory is not bad.
Exposition is not bad.
**Unmotivated information delivery** is the problem.

Use:

```text
CURRENT SCENE NEED
→ reader question
→ smallest useful answer
```

### Exposition questions

- Does the reader need this to understand the current action?
- Does the POV character have a reason to think about it now?
- Would withholding it create productive curiosity or only confusion?
- Can the information arrive through consequence rather than lecture?
- Can a strange fact be shown first and explained after?
- Does another character already know this, making the dialogue unnatural?
- Is the writer explaining because the scene itself failed to communicate?

### CIA / need-to-know principle

Treat world/background information as classified:
release it when it changes what the reader can understand, fear, predict, or interpret.

### Exposition forms

Choose among:
- concise narrator summary;
- contextual detail;
- action consequence;
- conflict-driven dialogue;
- document/artifact;
- flashback;
- memory;
- rumor;
- demonstration;
- later reveal.

Do not default to characters reciting shared history to each other.

---

## Setup / Payoff Ledger

*Basis: [@scriptmag-setup-payoff], [@friedman-setup-payoff]*

A setup is a promise.
A payoff is the later use, transformation, inversion, or consequence of that promise.

Track:

```yaml
setup_payoff:
  setup:
  first_appearance:
  apparent_function:
  true_function:
  camouflage:
  reader_attention_level:
  expected_payoff_window:
  payoff:
  payoff_type:
    - plot
    - emotional
    - relationship
    - thematic
    - comic
    - visual
    - reversal
  status: planted|developing|paid|intentionally_unpaid
```

### Good payoff

A strong payoff often feels:

```text
surprising now
+
obvious in retrospect
```

### Do not over-mechanize

Not every object must become a gun on the mantel.

Fiction needs:
- texture;
- accidents;
- unused possibilities;
- ordinary objects.

Track setups that create **reader expectation**, not every noun.

---

## Exposition quick card

### Principle

```text
INFORMATION
should enter
WHEN IT CHANGES THE PRESENT SCENE
```

### Need-to-know questions

- Does the reader need this now?
- Can the reader understand the current choice without it?
- Has the story created a question that this fact answers?
- Does the POV have a reason to think about it now?
- Could the information arrive as consequence?
- Do characters already know this?
- Is the paragraph here because the writer is proud of the research?

### Useful routes

- show first, explain after;
- conflict-driven dialogue;
- concise summary;
- object/document;
- memory;
- flashback;
- rumor;
- demonstration;
- delayed reveal.

### Worldbuilding rule

Worldbuilding is strongest when it has verbs.

Prefer:
- law being enforced;
- machine breaking;
- ritual being performed;
- taboo being violated;
- money being spent;
- status being lost;
- magic failing;
- custom causing conflict.

over encyclopedia paragraphs detached from action.
