# Research: Illustrated Audio Drama

Pack: [packs/illustrated-audio-drama.md](../../packs/illustrated-audio-drama.md).

Recorded 2026-11-23. The core of this pack is design: the owner's own production rulings for a voiced, illustrated YouTube series, a plan made with Codex that the owner approved, and a Claude–ChatGPT collaboration on the pack itself. Version 1.1 adds manga composition sources. They were gathered by the owner's lore session and re-read for this pack on 2026-11-23. Radio-drama and comics-lettering practice have not been checked yet.

## Entries

### `iad-owner-rulings`

- **Source:** Erik (skill owner), production rulings for an illustrated audio-drama series, 2026-11-20 to 2026-11-23, recorded in his project notes.
- **Type:** owner-ruling
- **Status:** Quoted from the owner's notes and messages; not independently tested.
- **Claim:** Episodes are about ten minutes, self-contained (parts may end on cliffhangers), voiced by a text-to-speech engine, and shown as a faster comic format with designed pages, lettering and a guided camera. The owner asked for "storytelling and cenematic shots from time to time. That means close shots, far shots and more", for art that "Isn't too basic", and for powers that "actually have some effect on the story", including on the audio and the visuals. A power's mechanism governs its counters: "She does not control sound per se. She controls the sense of sound in your brain. So air molecules don't actually vibrate. His hearing aids wouldn't stop it at all." After a rejected episode: "he shouldn't be telling her all of that information." Bracket delivery tags can be spoken by the engine, and acronyms are written as spaced letters. Darker scenes appear when the story calls for them, and each episode's look matches its lead. Later the same day, on one power system: "Chaos magic is awkard reality bending. By defult, it only has specific effects, but grows into random effects branching from their magic type". And on one episode: "She shouldn't be that creepy. And her powers going out of control shouldn't be a scene in this story either."
- **Derives:** The growth rule (new effects branch from the power's type), the per-episode intensity ceiling, the default beat map, the shot plan with reasons, the "too basic" warning, the removal and mechanism tests, the show-don't-confess rule, the engine-safe script rules and the per-episode look.
- **Limitations:** One series' rulings. The pack generalizes them as defaults that user intent may override.
- **Fidelity:** design

### `iad-codex-plan-2026-11-23`

- **Source:** "Powers that change the story, and a faster comic format," a plan drafted by Claude, critiqued by Codex and approved by the owner, 2026-11-23.
- **Type:** pack-design
- **Status:** Approved by the owner as a project plan; tested once as a one-minute board.
- **Claim:** A power succeeds only if removing its effects changes the plot. Each use should solve an immediate problem, create a worse one, show character or force a choice. Each powered character gets a signature (audible warning, sound transformation, comic-language transformation, trigger, cost, weakness, climax escalation), with owned devices nobody else uses. Effective comic-language devices include wrong-way bubble tails, the user's lettering inside a victim's bubble, repeated panels and cracking gutters.
- **Derives:** The power-signature card, the removal test and owned devices.
- **Limitations:** Built around one sound-based power; other power types were reasoned by analogy.
- **Fidelity:** design

### `iad-claude-codex-merge`

- **Source:** Claude's draft of this pack and ChatGPT's critique and counter-proposal (gpt-5.6-sol through the Codex CLI, read-only), merged by Claude and approved by the owner, 2026-11-23.
- **Type:** pack-design
- **Status:** Design review between two models; no reader testing.
- **Claim:** A screen-off radio play is the base and pictures must add rather than duplicate. A line-level "reason to hear it" test misses motivated briefings, so the confession test runs on the sequence. Fixed shot and layout counts would make episodes look alike, so they become revision warnings. Power mechanisms need range, onset, recovery, evidence and counterplay. Plot-critical spatial sound needs a mono-safe fallback. A multi-part ending settles its own question first.
- **Derives:** The audio/picture job split, the five-question confession scan, the warning-based shot and layout checks, the expanded mechanism schema, the accessibility fallbacks and the failure-mode rows.
- **Limitations:** Expert-style reasoning, not an empirical result. The warning thresholds are working numbers.
- **Fidelity:** design

### `iad-manga-mapping`

- **Source:** "Manga composition for our motion comics," a research note by the owner's lore session (Claude Code), 2026-11-23, made at the owner's request: "I don't want to use the actual manga style, but definitely the composition and storytelling would work."
- **Type:** pack-design
- **Status:** Project research note; its main sources were re-read for this pack (entries below). Its percentages were corrected against the source.
- **Claim:** Manga's framing, pacing and page-turn tools map onto audio-first 16:9 boards. One-character and detail panels become the default. Point-of-view panels serve perception. A look-around run stops time. Silent beats become written silence cues. Every page change works as a page turn, and each page has one focal panel.
- **Derives:** The composition subsection, the framing `content` and `subjective` fields, `page_role`, and the composition warnings.
- **Limitations:** A mapping from printed manga to screen pages, not a tested screen practice. Its suggested thirds split of close, medium and wide panels was kept only as a warning.
- **Fidelity:** design

### `cohn-2012-framing`

- **Source:** Neil Cohn, Amaro Taylor-Weiner and Suzanne Grossman, "Framing Attention in Japanese and American Comics: Cross-Cultural Differences in Attentional Structure," *Frontiers in Psychology* 3:349, 2012. https://pmc.ncbi.nlm.nih.gov/articles/PMC3449338
- **Type:** empirical
- **Status:** Article read 2026-11-23; the second half was read only in summary.
- **Claim:** Panels are coded by how much active content they frame: Macro (several active entities), Mono (one), Micro (less than one) and Amorphic (none, only environment). The article reports Cohn's earlier counts of about 60% Macro, 35% Mono and 5% Micro for American comics, against about 47%, 43% and 10% for manga. In its own sample of 30 books (10 manga, 10 mainstream American, 10 independent American), manga used Mono panels far more than other types. The Micro difference was not uniform across both American groups.
- **Derives:** The framing categories, and single-character panels as the default for manga-style composition.
- **Limitations:** English-translated shonen manga only; genre matching across cultures is imperfect. These are tendencies in print comics, not a target mix.
- **Fidelity:** approximate

### `cohn-2023-subjectivity`

- **Source:** Neil Cohn, Irmak Hacımusaoğlu and Bien Klomberg, "The framing of subjectivity: Point-of-view in a cross-cultural analysis of comics," *Journal of Graphic Novels and Comics* 14(3), 336–350, 2023. https://research.tilburguniversity.edu/en/publications/the-framing-of-subjectivity-point-of-view-in-a-cross-cultural-ana/
- **Type:** empirical
- **Status:** Abstract read 2026-11-23.
- **Claim:** Across more than 300 annotated comics from Asia, Europe and the US, more manga use subjective (point-of-view) panels, though high proportions also appear elsewhere. Subjective panels are proportionally more common in focal framings (close-ups and environment views) than in wide views of scenes.
- **Derives:** Subjective panels for perception, and the perceived-then-actual pairing for powers.
- **Limitations:** Abstract only; the pairing with powers is pack design.
- **Fidelity:** approximate

### `natsume-panels`

- **Source:** Natsume Fusanosuke, "The Functions of Panels (koma) in Manga," translated by Jon Holt and Teppei Fukuda, *Electronic Journal of Contemporary Japanese Studies* 21(2), 2021 (from Natsume's 1997 book). https://www.japanesestudies.org.uk/ejcjs/vol21/iss2/holt_fukuda.html
- **Type:** theoretical
- **Status:** Translation read 2026-11-23.
- **Claim:** Panels segment time and give the reader a sense of order. Contrast in panel size and shape compresses and releases tension. *Ma* names a space in time, and wordless sequences change reading speed. Words, pictures and frames are treated as three basic elements of expression.
- **Derives:** Silent beats as authored timing, and size contrast around a focal panel.
- **Limitations:** A critic's analysis of print reading; on screen, the locked audio sets the speed instead of the reader.
- **Fidelity:** conceptual

### `globalcomix-manga-paneling`

- **Source:** ArtCrumbs and the GlobalComix Team, "Creator Tips and Tricks #10: More tips for Paneling Manga," GlobalComix, 2022-03-08. https://globalcomix.com/news/details/260/creator-tips-and-tricks-10-more-tips-for-paneling-manga
- **Type:** craft-practice
- **Status:** Article read 2026-11-23.
- **Claim:** It names angled (*naname*) panels, used for speed and action, against straight square panels. *Ma-goma* are panels without spoken dialogue that create a quiet pause. *Misegoma* is one larger focal panel per page.
- **Derives:** Angled panels for tension and straight ones for calm, silent pause panels, and one focal panel per page.
- **Limitations:** A creator tips article, not scholarship. Page-turn terms (*hiki-goma*, *mekuri-goma*) and bleed panels are not defined there.
- **Fidelity:** convention

### `mccloud-transitions`

- **Source:** MediaSmarts, "Expression and storytelling in comics" (undated), summarizing Scott McCloud, *Understanding Comics*, 1993. https://mediasmarts.ca/digital-media-literacy/general-information/visual-media/comics/expression-and-storytelling-comics
- **Type:** craft-practice
- **Status:** Secondary summary read 2026-11-23; McCloud's book was not consulted directly.
- **Claim:** McCloud's six transitions include moment-to-moment and aspect-to-aspect, which slow time. Aspect-to-aspect shows different aspects of one place or moment, so the eye can wander. It is used more often in Japanese comics.
- **Derives:** The look-around run before a big beat.
- **Limitations:** A secondary summary of a classic but non-empirical book.
- **Fidelity:** convention
