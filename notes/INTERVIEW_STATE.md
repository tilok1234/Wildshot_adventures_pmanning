# Interview State — ALWAYS CURRENT

> **This file is the single source of truth for where the guided design interview stands.**
> Any session (human or AI) continuing the interview MUST read this file first,
> and MUST update + commit it after every approved answer. If this file and chat
> memory disagree, this file wins.

**Last updated:** 2026-07-26 (refinement batch recorded — see below)

## Interview position

🎉 **PART I IS COMPLETE — CORE-01 through CORE-55 all answered (2026-07-26).**
CORE-14 remains provisional/prototype-gated.

Next steps (designer to choose, in any order):

1. **Part II — combat and controls module questions**, which directly feed the Phase A
   lab's design details (movement feel numbers, exact ability behaviours, enemy
   grammar specifics).
2. **Start building the Phase A combat laboratory in Godot** (CORE-53's milestone),
   using the existing tileset/sprite pipeline; interview and lab can proceed in
   parallel, with lab findings feeding back into [T] answers.
3. **Companion-doc refresh sweep**: 03-HANDOFF, 04-OPEN_QUESTIONS, 05-ROADMAP, and
   09-SYSTEMS_MAP still reflect the CORE-32 snapshot and should be reconciled with
   everything decided 2026-07-26 (the GDD, registers, and prototype spec are current).

Option 3 is recommended before long Part II sessions so every doc agrees.

## Question status table

| Range | State |
|---|---|
| CORE-01 through CORE-16 | Answered. CORE-14 remains provisional/test-gated. |
| CORE-17 | Open. Frame as **first character's journey to endgame**, not "campaign". No numerical duration locked. |
| CORE-18 | Open. Constrained by CORE-24's locked endgame direction. |
| CORE-19, CORE-20 | Open, unanswered. |
| **CORE-01 through CORE-55** | **ALL ANSWERED — Part I complete 2026-07-26.** |
| CORE-14 | Provisional/prototype-gated (co-op depends on the Phase E network gate). |

### CORE-19 — answered 2026-07-26 [P] — completed Part I

Tone: colorful heroic fantasy with bite (established visually by the existing tileset;
dungeon/dusk style masters carry the menace). Rating: clean-leaning E10+/T, guiding
preference not a hard lock ("keep it clean without letting it restrict us"); fantasy
violence, no gore. Boundaries: no sexual content; mild language at most; no real-world
religion/politics; horror atmosphere without shock imagery; loot RNG never presented
with casino aesthetics. Narrative specifics open.

### CORE-18 — answered 2026-07-26 [L/P]

Endgame = open-ended, collection-driven "never-ending-ish collectathon"; the growing
collection book is the horizon, not one authored pinnacle; content added over time
under the locked business model (expansions ok, live-service pressure never; complete
as purchased). Alts = supported but deliberately modest replay loop [P]. No
endgame-only systems [L].

### CORE-17 — answered 2026-07-26 [P/T]

Endgame threshold = level cap + main quest completion (roughly coincide by design).
First zero-to-hero journey targets ~40–80 focused hours; optional content extends
freely; substantial endgame beyond. Design target validated later; nothing gated at
runtime.

### CORE-20 — answered 2026-07-26 [L/P]

Solo developer; AI-orchestration expert with strong technical understanding and deep
genre knowledge; production AI-orchestrated across code/art/content. Engine most
likely Godot [P]. Abundant AI access removes tooling/asset cost; no contractor budget.
10–40 h/week, planning anchored to the low end. No deadline — CORE-55 gates are the
discipline mechanism. Custom broad tileset + generation system built; matched
enemy/player sprite generator near completion. Consequences: generators must encode
the readability laws; tools accelerate authoring without weakening the handcrafted-
world rule; velocity measured through lab and slice. Risk #2: unmeasured → bounded.

### CORE-55 — answered 2026-07-26 [L/P]

Two formal continuation gates. Gate 1 (lab→slice): Phase A exit gate + outside testers
+ lowest-speed dodgeability + explainable deaths + frames change how testers fight;
repeated failure = pivot or stop. Gate 2 (slice→production): voluntary post-completion
farming; dry-streak-as-dedication; gap-as-invitation; explainable-death rate at
density; build distinction; slice velocity extrapolates to a viable plan under CORE-20;
failure = planned-order scope cuts. Gate 2 unevaluable until CORE-20.

### CORE-54 — answered 2026-07-26 [L/P]

Top five risks with test/mitigation/cut (detail in Risk Register): no-reward fun (Phase
A gate); production feasibility unmeasured (CORE-20 + velocity); friction stacking
(percentile sim, never pity); content multiplication (one class first, cut density
before classes); endgame readability (stress-tests under the eight laws, cap density).
Market runner-up: clone-without-a-hook perception.

### CORE-53 — answered 2026-07-26 [L/P]

First playable milestone = prototype spec Phase A no-reward combat lab with its
standing exit gate. Additions: gate judged by fresh outside testers, never solely the
builder [P]; every test pattern verified dodgeable at lowest intended movement speed
[P]. Lab timeline awaits CORE-20.

### CORE-52 — answered 2026-07-26 [P]

Full slice bill: Archer, cap ~10, small behaviour-changing tree; 4 frames × ~3 tiers,
4 ability items, 2 armor archetypes, situational rings; one zone + hub; 8–10 enemy
types + elite + roaming rare; portal enemy → 10–20 min committed dungeon → boss;
tiered + cosmetic drops + one unique weapon; main-quest slice with one level gap,
10–15 side quests, one faction set + vendor; ~3–5 hrs + repeatable farm. Excludes
co-op/raids/hardcore/gathering/mounts. Additions: explicit gate questions (voluntary
post-completion farming; dry-streak feel; gap-as-invitation; explainable deaths) and
one authored secret (discovery-pillar test).

### CORE-51 — answered 2026-07-26 [L/P]

Eight readability laws: threat renders above beauty; player shots subordinate; hostile
vs friendly by shape/pattern first with one hostile family language; telegraph
prominence = danger; per-encounter effect budgets stress-tested at endgame density;
quiet arena floors; audio as eyes-closed second channel; death always explainable
(unexplainable deaths fail review).

### CORE-50 — answered 2026-07-26 [L/P]

Required-from-start baseline: full remapping; hold/toggle fire; effect-density/opacity
options; flash reduction; colorblind-safe projectile language (shape/pattern, never
color alone); optional visible-hitbox indicator; UI/text scaling; reducible damage
numbers; separate audio channels + audible key threats; pause wherever legal; no
photosensitivity-hostile defaults. No global difficulty setting [L] — higher-difficulty
dungeon versions are the hard mode; accessibility = readability + control, never enemy
tuning. No M+K aim assist; possible stick assist quarantined to controller.

### CORE-49 — answered 2026-07-26 [L/T]

Feel stays as locked. Target ranges as [T] hypotheses: dungeon runs ~10–20 min; portal
at known source ~5–20 min; mastered loop 2–3×/hr; felt upgrade most 1-hr leveling
sessions (endgame exempt); boss unique expected ~20–40 attempts. Percentile guardrail:
p95 unlucky time ≤ ~2–3× expected, tuned via rates/cadence never odds. Additions:
attempt counts tracked and displayed per pursuit [P]; grinds overlap — every hunt
advances ≥2 tracks, no run a pure loss [P]. Final numbers await Phase D simulation.

### CORE-48 — answered 2026-07-26 [L]

Confirms CORE-25 + adds automation stance: crafting deterministic non-combat only;
gathering = fishing/foraging exactly; NO automation of any kind — no idle production,
automated gathering, or offline progress. Everything through active play.

### CORE-47 — answered 2026-07-26 [L/P]

Several major hubs (fewer than one per zone) as full-service anchors: faction vendors,
crafting commissions, quest givers, auto-travel, stash. Possible narrative capital open
[U]. Stash strictly per-character — no sharing/muling; each character is its own
journey. Recognition staged in hubs [P]: NPC behaviour, improvements, settlement states
escalate with progression; selected quests may alter hub states.

### CORE-46 — answered 2026-07-26 [L/P]

Quests = packaged direction + world context: teach, route to sources/special places,
landmark rewards, faction standing, story beats; quest design speaks the game's own
language; no daily/repeatable structure. Main quest 1→cap directs progression
geographically with deliberate level-gap moments pushing players into side content;
gaps playtest-tuned [T] and must surface options. MMO-dense quest world [P], numbers
deferred to CORE-20, slice zone = density test. Faction XP woven in: some factions via
order-free themed quest sets (all/most ≈ max standing), others via other verbs (enemy
hunts) — each faction its own pursuit. Guards: faction rewards never mandatory; sets
finite; major quest rewards deterministic.

### CORE-45 — answered 2026-07-26 [L/P]

Tier roles: elites = pattern tests + portal/rare sources; dungeons = mastery chambers +
targetable loot; bosses = learn-master-farm centerpieces + unique chases; world bosses =
outdoor anchors + portal fountains; raids/superbosses = execution ceiling. Almost all
dungeons optional-but-best-rewarding [P]; small set of authored milestone dungeons tied
to major quest/story beats under CORE-28 gate rules. Milestone selection deferred.

### CORE-44 — answered 2026-07-26 [L/P]

Packs = combined pressures from the role grammar (aimed/predictive/fan/burst/ground
hazard/shield/healer/chaser); ordinary = 1–2 pressures, dangerous = 3+; density never
the difficulty. Priority targets make packs decisions. Terrain placement matters [P].
Additions: pulling/splitting as a learnable skill via readable engagement ranges [P];
pack compositions deliberately showcase different weapon frames [P]. Roles readable at
a glance.

### CORE-43 — answered 2026-07-26 [L/P]

No character/progression loss outside optional hardcore. Open world: respawn nearest
city + percent-of-gold fee (scales with wealth; never cheaper than teleporting — no
death-warp) [P/T]. Dungeons: death ends the committed instance, portal spent [L/P] —
balanced by re-obtainable portals for knowledgeable players. Raids: paid respawn at
wing start, wing progress never resets, bosses reset to full (gold buys attempts, not
progress), escalating within-visit fee [T]. Optional per-character hardcore permadeath
[P]: never warps baseline, anti-save-scum deferred, trophy candidate.

### CORE-42 — answered 2026-07-26 [L/P]

Acquisition = learn authored source, farm, roll independently; no pity. No tokens,
first-kill guarantees, or selectable rewards for uniques beyond guaranteed quest uniques
[L]. Dupes sell for meaningful gold, never convert to power/materials/odds [P];
cosmetic dupe milestones = optional [LATER]. Faction vendors may sell modest baseline
tiered gear as a leveling catch-up floor [P]; drops always outpace shops; shops never
sell uniques.

### CORE-41 — answered 2026-07-26 [L/P]

Equipment is the build system: loadout (weapon pattern × ability item × armor archetype
× ring) changes positioning, engagement, roles, and attemptable content — not just
numbers. Tiering rule: ordinary tiers preserve a familiar style while improving
numerically; behaviour swings come from frames, ability items, uniques. Additions
(assistant-proposed, designer-invited): side-grade rule (frames within a tier are
situational alternatives, not a ranking) [P]; chunky felt tier steps [P]; itemization
readability (behaviour communicated before farming) [P].

### CORE-40 — answered 2026-07-26 [L/P]

Lean baseline stat set: health, mana, damage, attack speed, range, armor/defense,
movement speed; HP/mana regen candidates [P]. Intentional exclusions [L]: accuracy/
evasion/dodge chance, crit chance, life-steal/on-hit sustain, resistance matrices —
combat resolves through position, not dice. Uniques may deliberately break these rules
with authored, communicated effects [P]. Values/growth/caps/regen decision deferred.

### CORE-39 — answered 2026-07-26 [L/P]

Levels grant class-specific base stats incl. HP and mana + skill points (leveling feels
good); gear stays the primary stat engine. Equipment has level requirements as an
anti-rush gate [P] alongside instance minimum levels. Skill tree: large, points-spent-
deep, not level-tier-gated [P]; capstone at tree bottom reached near cap. Hard cap ≈
endgame transition [P]. NEW: provisional faction-reputation system — vendor/similar
unlocks, faction XP ground from different enemies at varying difficulties; first concrete
world-recognition mechanism (GDD §3 pointer added). Details deferred.

### CORE-38 — answered 2026-07-26 [P]

Vertical slice: one class — provisionally the Archer — with ~3–5 distinct weapon frames,
~3–4 ability items (covering at least mobility/defense/burst), 2–3 build directions.
Proves the locked combat pillar (movement-only dodging, single active, weapon-owned
patterns, honest bosses, armor/ring tradeoffs). Full game: three classes locked;
per-class content counts explicitly deferred until CORE-20. Rationale: class-exclusive
item families multiply content — prove one class deeply first.

### CORE-37 — answered 2026-07-26 [L/P]

Ownership map confirmed. Class = eligibility + identity (base stats, tree, exclusive
weapon/ability-item families — gear-driven unique playstyle per class). Weapon = pattern
+ damage/attack speed/range. Ability item = the single active, may carry stats. Armor and
ring = classic RPG stats. Four-slot loadout [L/P]: weapon, ability, armor, ring; all
pieces may carry stats. Armor uses give-and-take archetypes (light/high-dmg vs
heavy/low-dmg etc.). Ring anti-degeneracy rule: no universally correct ring (no mandatory
HP ring). Uniques in any slot may carry behaviours beyond stats [P]. Deferred: stat set,
per-slot budgets, class stat spreads, ring class-binding.

### CORE-36 — answered 2026-07-26 [L/P]

Tiered intensity ladder confirmed: fodder → ordinary packs → dangerous packs/pockets →
elites → rare/named roamers → world bosses → dungeon enemies → dungeon bosses → raid
wings → optional superbosses. Escalation axis [L]: projectile density, speed, pattern
complexity, and composition — never HP sponging; health stays honest. Fractal rule [L]:
the open-world ladder repeats inside every zone at that zone's authored band (relaxed
outskirts through genuine danger in each zone); bands don't trivially overlap.

### CORE-35 — answered 2026-07-26 [CUT]

Focus targeting is cut entirely: no selection, lock-on, marking, focused-enemy state, or
hover focus on any input method; nothing is ever tied to a focused enemy. Enemy info
(names, health, boss casts) comes through general interface presentation (overhead bars,
boss presentation, bestiary — implementation deferred to interface/knowledge questions).
Controller aim assistance, if retained, must work without a focus system and stays
quarantined from M+K play and encounter design.

### CORE-34 — answered 2026-07-26 [L/P]

Exactly one active ability per character, granted by an equipped ability item; each class
has its own large pool of ability-equips, so ability variety and build identity come from
the loot hunt (weapon = primary pattern, ability item = active, armor = stats). Abilities
run on mana; the item defines behaviour and cost. The skill tree grants no actives — it is
passives/resource/specialization with a binding condition that meaningful nodes change
behaviour, not just numbers (including modifying equipped ability items). Max-level
capstone that supercharges the equipped item = open design space [P]. No mandated role
checklist. No encounter may require a specific ability item, or any ability, to be
survivable — movement stays sufficient (designer: "awesome boss fights where movement is
enough, just like RotMG").

### CORE-33 — answered 2026-07-26 [L/P]

Purely movement-based dodging, RotMG tradition. Universal kit = movement + free aim only;
no universal dash, roll, blink, sprint, block, parry, shield, or i-frame action. Binding
consequences recorded: honest dodgeability by movement alone (at the least mobile class's
baseline), movement speed as a premier tuned stat, readability/traceable deaths even more
load-bearing, death design must account for no escape action. Class-specific mobility or
defensive abilities may exist as class tools [P]; never required by encounters; roles and
counts belong to CORE-34.

### Refinement batch — 2026-07-26 (approved, recorded, committed)

Out-of-order refinements approved after a coherence review; integrated into the GDD,
Decision Register, and Living Questionnaire:

1. **Dry-streak mitigation [P]** (CORE-16): no pity ever; reward breadth instead —
   cosmetic/collection drops from bosses, recorded straight into the collection menu.
2. **Controller worst case [P]** (CORE-13/12): controller may end up as the relaxed
   grinding input only; endgame expects M+K; Steam Deck demoted to "where it survives".
3. **Variation bounds [P]** (CORE-27): authored *where*, pooled *what* — fixed arenas
   with 3–4 possible bosses; roaming rares patrol authored zone+route; pooled locations
   share key rewards or stay variety-only.
4. **Pets cosmetic-only [P]** (CORE-25): no combat/stat benefit of any kind, if included.
5. **Raid structure [P/T]** (CORE-16 raid scope): wings as the unit of commitment;
   player-controlled persistence, no time-based lockouts, free instant reset;
   deterministic skip baseline (mastery shortcuts or trophy tokens) [T]; rare skips
   only as luxury on top; within-wing checkpoints test-gated.

## Note-taking protocol (the fix for lost notes)

After **each** approved answer, in the same working session, before moving to the next question:

1. Record the approved decision with its status tag ([L]/[P]/[T]/[U]/[CUT]/[LATER]) in
   `docs/10-LIVING_DESIGN_QUESTIONNAIRE.md` (fill the question's answer slot).
2. Update `docs/08-DECISION_REGISTER.md` with the concise decision entry.
3. Integrate the decision into `docs/01-GAME_DESIGN_DOCUMENT.md` where it belongs.
4. Update the **Active question** and **status table** in this file to the next question.
5. Append a short entry to today's file in `notes/sessions/`.
6. `git commit` all of the above and push. **One approved answer = one commit.**

Never batch multiple answered questions into a deferred "I'll write it up later" step —
that is exactly how notes were lost before this repo existed.

## Working method (established, unchanged)

- Ask one focused question at a time and finish it before moving on.
- Consolidate the designer's natural answer into clear design language; get approval before recording.
- Keep straightforward decisions concise; expand when a decision has real design, balance, technical, or production consequences.
- Use existing answers before asking for a decision again.
- Challenge material design or production risks honestly.
- Treat purposeful, targetable repetition as an intended strength.

## Source hierarchy

1. `docs/10-LIVING_DESIGN_QUESTIONNAIRE.md` — authoritative detailed interview record.
2. `notes/INTERVIEW_STATE.md` (this file) — current position and continuation instructions.
3. `docs/08-DECISION_REGISTER.md` — concise decision status.
4. `docs/01-GAME_DESIGN_DOCUMENT.md` — readable integrated design overview.
5. `docs/04-OPEN_QUESTIONS.md` — unresolved questions and deferred details.
6. `docs/11-HANDOFF_2026-07-21_HISTORICAL.md` — historical provenance only; its CORE-21 marker is intentionally outdated.
