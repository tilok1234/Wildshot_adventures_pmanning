# Wildshot Adventures — Pre-production Roadmap

**Status:** Recommended sequence. Dates remain unset — the CORE-55 gates, not dates, are the discipline mechanism — but the pre-registered effort model below (added 2026-07-27) gives velocity measurement a falsifiable baseline against the CORE-20 capacity constraints.

## Stage 0 — Finish plan-blocking core questions ✅ COMPLETE (2026-07-26)

All of Part I (CORE-01 through CORE-55) is answered. The former blockers resolved as:

- first journey: ~40–80 focused hours to level cap + main quest (CORE-17 [P/T]);
- endgame: open-ended collectathon, no endgame-only systems (CORE-18);
- tone: colorful heroic fantasy with bite, clean-leaning E10+/T (CORE-19 [P]);
- production: solo AI-orchestrated developer, Godot [P], 40 h/week planning floor / ≈72 ceiling alongside a day job (CORE-20 as amended by PROD-01, 2026-07-27 — the floor is a self-correcting claim under test), no deadline (gates are the discipline), custom tileset + sprite + world generation pipeline.

**Gate: PASSED.** The project has an honest scope envelope.

## Stage 1 — Define loops and world structure on paper

CORE-21 through CORE-30 now define:

- the ten-second, ten-minute, one-hour, and long-term loop hierarchy;
- supporting activities and their exclusions;
- a layered multi-map world with authored foundations and controlled variation;
- mostly soft outdoor gating and purposeful contained gates;
- stable authored difficulty with no player scaling;
- selective paid teleportation that preserves special manual routes.

**Gate passed at the core-design level:** The game can be described at moment, activity, hour, world, access, difficulty, and travel scales without contradictions. Detailed implementation remains deferred.

## Stage 2 — Solo combat laboratory

**Build plan: `12-PHASE_A_LAB_BUILD_PLAN.md` (approved 2026-07-27)** — architecture bundle, v0 tuning hypotheses, milestones M0–M8 + M-FX with the pre-vacation/vacation split and slip ladder. The plan implements everything below; this stage description remains the design-level statement.

CORE-31 through CORE-36 and CORE-44/50/51/53 fully specify this stage. Implement:

- independent movement and free aiming with no selected-target requirement;
- tap-to-fire, hold-to-fire, and a visible remappable autofire toggle;
- resource-free ordinary primary attacks;
- deterministic weapon-defined patterns;
- predictable movement while firing;
- clear terrain collision and line-of-fire behavior;
- readable impact, immunity, blocked-hit, and kill feedback;
- NO universal defensive action beyond walking — dodging tested as pure movement (CORE-33);
- one equipped-ability test slot with swappable test abilities (CORE-34);
- three weapon frames, several enemy behaviors from the role grammar, and one elite.

Do not add progression rewards until the no-reward combat test passes.

**Pre-lab asset task (added 2026-07-27, showcase-packet review; rescoped same night —
Sprite Forge supersedes Actor Forge v2.3):** the Sprite Forge full pack ships 20 projectile
and 15 effect sheets (incl. telegraph rings/cones/beams, charge-up, muzzle, impact), so the
combat-effects task becomes **curate + gap-fill**: assign player-vs-hostile projectile
families, apply the shared hostile signature as a rendering treatment across all hostile
shots, and author hazard arm-progress indicators — spec'd against the eight readability laws
(CORE-51). Every other Phase A asset class ships: arena tilesets (including dungeon-room,
cave, and corrupt-zone scenes) and a 231-actor manifest-driven pack (28-row rig, 64 px
cells, deterministic cfg regeneration; placeholder-fidelity by design, polished swaps later
under the frozen contract), delivered in-repo at game repo `assets/`.

**Phase A build window — pre-registered (2026-07-27):** ~6 free weeks from ≈ early October
2026 (designer vacation; stated capacity up to 16 h/day — ≈670 h theoretical ceiling, 4×
Phase A's pessimistic bound). Plan targets **two full Gate 1 cycles** inside the block: lab
built in weeks 1–2; build in outside testers' hands by ~week 3 (the itch/devlog channel from
the pre-vacation weeks supplies testers); iterate on feedback; Gate 1 attempted before the
block ends; if it passes early, Phase B starts inside the block. The planning constraint is
tester turnaround, not designer hours. Pre-vacation weeks (evenings/weekends): the effects
pack, audio-pipeline design, Godot project + TileForge import proven via the §4 acceptance
test, itch/devlog stood up. **Fresh-hands guard:** dodgeability and feel verdicts are
verified in a rested session or by a bot pass — patterns tuned at hour 14 of a 16-hour day
are tuned to exhausted reflexes, which violates the lowest-speed honesty rule in spirit.

**Bot-testing system [P] (2026-07-27):** AI-driven test bots for unattended mechanical
verification — movement-only lowest-speed dodgeability proofs (this IS the CORE-53
verification, mechanized), soak/regression runs, drop-rate percentile simulation (Phase D),
TTK sanity checks. **Guard:** bots never substitute for the human gates — Gate 1/2 judgments
(fun without rewards, explainable deaths, dry-streak feel) belong to fresh outside human
testers per CORE-53/55.

**Gate (CORE-53/55 Gate 1):** Fresh outside testers — never solely the builder — voluntarily re-engage for 20+ minutes with zero rewards; every death is explainable; every pattern is dodgeable at the lowest intended movement speed; controls, collision, and feedback feel dependable; the frames change how testers fight. Repeated failure means pivot or stop. Pre-registered consequence order (2026-07-27): repeated failure first unlocks CORE-33, then CORE-32 determinism details, then the frame roster — before any pivot/stop decision (see decision register).

## Stage 3 — Enemy, projectile, and readability grammar

Establish telegraph language, hostile/friendly visual hierarchy, projectile rules, safe-space readability, encounter roles, and intensity scaling.

**Gate:** Deaths are understandable and endgame intensity appears feasible rather than visually chaotic.

## Stage 4 — Class, skill, and weapon grammar

Prototype one class (Archer, provisional) deeply before building all three. The class/weapon/equipment boundary is decided (CORE-34/37/41: one item-granted active, behaviour-changing passive tree, four-slot loadout); implement and test 2–3 build directions against it.

**Gate:** Builds change decisions and positioning, not only sheet damage.

## Stage 5 — Optional co-op technical gate

Run the two-player greybox test before large world production. Keep solo design authoritative.

**Gate:** Co-op is either retained provisionally with evidence or cleanly deferred/cut.

## Stage 6 — Levels, stats, equipment, and loot

The stat set (CORE-40), tier philosophy (CORE-41), acquisition and duplicate rules (CORE-42), and grind-cadence targets (CORE-49) are decided; implement them, tune exact values and curves, and run the drop-rate/percentile simulation against the CORE-49 targets. Guard against multiplicative projectile/proc explosions.

**Gate:** Progression feels tangible without making execution irrelevant or creating one mandatory build.

## Stage 7 — Portal-to-dungeon vertical mini-loop

Build one portal source, one field route, one short dungeon, one boss, tiered baseline loot, and one unique chase.

Test the complete friction budget: travel + enemy availability + portal chance + dungeon commitment/reset boundary + dungeon length + boss learning + drop rarity.

**Gate:** A failed unique roll can still leave a self-directed session feeling productive; repeated attempts feel earned rather than obstructed; the player understands that rolls are independent; pausing protects an active run while abandoning clearly resets the ordinary-dungeon instance.

## Stage 8 — World, quests, hub, and recognition

The purposes of quests (CORE-46), factions (CORE-39/46), hubs and recognition (CORE-47) are decided; implement the slice's share of them. Implement only enough fishing, foraging, limited non-combat crafting, collection presentation, pets (cosmetic-only), and authored settlement change to test their locked supporting roles. *(2026-08-02: fishing is now STARHOOKING — land rifts, the starhook INDEX is law; water fishing (sl-0111) is parked; starhook v2 is already live in the slice.)* Build one dense region with several overlapping goals — the slice zone doubles as the quest-density test.

**Gate:** The world supplies meaningful reasons to explore and grind beyond isolated combat rooms.

## Stage 9 — Full vertical slice

The slice should demonstrate the full promise in miniature:

- beginning weak;
- discovering a region and objectives;
- gaining levels and equipment;
- hunting a known portal source;
- entering a dungeon;
- learning and defeating a boss;
- obtaining dependable progression and pursuing a situational unique;
- learning physical routes and unlocking one selective teleport destination or permanent shortcut;
- returning visibly stronger and more recognized.

The full content bill is decided in CORE-52 (Archer, ~cap 10, 4 frames × ~3 tiers, 4 ability items, one zone + hub, 8–10 enemy types, complete portal→dungeon→boss→unique chain, main-quest slice with one level gap, 10–15 side quests, one faction set, one authored secret, ~3–5 hours plus repeatable farm).

**Gate (CORE-55 Gate 2):** Voluntary post-completion boss farming; dry streaks read as dedication with the attempt counter; the level gap reads as invitation; explainable-death rate stays high at density; builds feel distinct; and slice production velocity extrapolates to a viable full-game plan under the CORE-20 constraints. Failure means scope cuts in the planned order. Pre-registered order (2026-07-27): slice-as-v1.0 → shrink the content bill (capacity-raise moot after PROD-01). "Viable" is defined (2026-07-27): the remaining full-game bill at measured slice velocity extrapolates to ≤ 5 years at the then-current PROD-01 floor (see the effort model below and the decision register).

## Stage 10 — Production planning

Only after the slice succeeds:

- lock content volume and team plan;
- build content-authoring tools;
- establish performance budgets;
- schedule classes, regions, quests, dungeons, bosses, raids, and polish;
- decide Early Access/demo strategy;
- revisit co-op commitment and platform expansion.

## Pre-registered effort model (added 2026-07-27) [T]

Recorded before any build hours exist so Phase A velocity measurement has a falsifiable baseline. Assumes strong AI leverage on code and asset generation and human-paced feel iteration, tuning, playtesting, and integration. Attack the inputs, then replace them with measured actuals.

| Stage | Optimistic | Pessimistic |
|---|---|---|
| Phase A — combat lab | 60 h | 150 h |
| Phase B — readability grammar | 40 h | 100 h |
| Phase C — build grammar | 40 h | 100 h |
| Phase D — progression/loot mini-loop | 80 h | 200 h |
| Phase E — co-op network gate | 40 h | 120 h |
| Stages 8–9 — slice content (zone, hub, quests, faction set, art, audio, UI, CORE-50 baseline, tuning, playtests) | 250 h | 500 h |
| Overhead — integration, bugfix tax, doc upkeep (~20%) | 100 h | 230 h |
| **Vertical slice total** | **~610 h** | **~1,400 h** |

At the PROD-01 planning floor (40 h/week ≈ 2,000 h/year): **roughly 4–8.5 months to Gate 2**; at the ≈72 h/week ceiling, roughly 2–5 months; if the floor self-corrects to ~20 h/week, roughly 8–17 months — every case inside the accepted horizon. (Pre-PROD-01 anchors, kept for the record: the assumed 10 h/week gave 1.2–2.7 years; 20 h/week gave 7–16 months.)

**Full-game extrapolation** (content scaling ~10–20× slice content for the 40–80-hour journey, plus two further classes with exclusive item families, raids/superbosses/endgame, supporting systems, and release work): roughly **4,500–9,000 hours** — about **2.25–4.5 years at the PROD-01 floor (40 h/week)**, 1.25–2.5 at the 72 h/week ceiling. (The pre-registration read 9–17 years because it assumed a 10 h/week side-project anchor; PROD-01's full-time correction — not any change to the hour estimates — is what moved the horizon.) Calibration: Stardew Valley consumed ≈16,000 solo hours pre-AI for a smaller content bill.

**Scope menu (designer decision pending — blocks honest Gate 2 evaluation):**

1. **Slice-as-v1.0:** ship the CORE-52 slice scope as a small premium game; the MMO-scale world becomes the expansion path that exists only if strangers pay for and replay the seed.
2. **Shrink the content bill:** shorter first journey, fewer/smaller zones, two classes, raids as post-launch expansion.
3. **Raise the reliable capacity floor** (changes the divisor, nothing else).
4. **Consciously accept the long horizon in writing** — legitimate for a no-deadline project, but Gate 2's "viable full-game plan" criterion then needs a stated definition of viable.

**DECIDED 2026-07-27 — Option 4 (designer-approved):** the full game as specced stays the target ("keep everything we planned"); the floor-case ~2.25–4.5-year horizon is consciously accepted in writing. **Gate 2 "viable" is now defined:** at measured slice velocity, the remaining full-game bill must extrapolate to **≤ 5 years at the then-current PROD-01 floor**; longer auto-triggers the pre-registered cut order (slice-as-v1.0 → shrink the content bill; the capacity-raise step is moot — PROD-01 already maxed capacity). Options 1–2 remain live as that failure cascade, not as the plan.

**Pending designer inputs:** none — PROD-01 ✅, PROD-03 ✅, and the scope-menu choice ✅ (Option 4) all answered 2026-07-27. Gate 2 is fully evaluable when reached.

## Tester and market pipeline (added 2026-07-27)

Gates 1 and 2 are judged by fresh outside testers; this is where they come from.

1. During Phase A, capture a 30–60-second GIF each week (the lab's debug tools make this nearly free).
2. Before the lab gate: stand up an itch.io page, one devlog thread, and a bare Discord; post progress GIFs to r/rotmg and one bullet-hell or indie-dev community — the RotMG community is the target audience for the combat hypothesis.
3. At gate-ready: publish the lab build unlisted on itch; recruit 5–8 testers — 2–3 strangers from those communities, 2–3 genre-familiar acquaintances; never solely the builder (CORE-53).
4. Standing rule: every gate playtest includes at least 3 strangers; log unprompted "what is this game?" descriptions (the CORE-54 market test, now with respondents).
5. A Steam page and wishlist push deliberately wait for slice-quality footage [LATER] — a weak page is its own risk; the itch/devlog channel is the pre-slice market thermometer.

## Scope rules throughout

- Do not build the large world before one small expedition loop works repeatedly.
- Do not build all three classes before one class proves the architecture.
- Do not add item volume before a few items create real choices.
- Do not use progression rewards to hide weak combat.
- Do not let controller, co-op, or newcomer considerations reduce the intended mouse/keyboard endgame ceiling.
