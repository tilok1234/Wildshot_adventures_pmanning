# Wildshot Adventures — Pre-production Roadmap

**Status:** Recommended sequence. It does not assign dates or assume team capacity that has not been discussed.

## Stage 0 — Finish plan-blocking core questions ✅ COMPLETE (2026-07-26)

All of Part I (CORE-01 through CORE-55) is answered. The former blockers resolved as:

- first journey: ~40–80 focused hours to level cap + main quest (CORE-17 [P/T]);
- endgame: open-ended collectathon, no endgame-only systems (CORE-18);
- tone: colorful heroic fantasy with bite, clean-leaning E10+/T (CORE-19 [P]);
- production: solo AI-orchestrated developer, Godot [P], 10–40 h/week planned to the low end, no deadline (gates are the discipline), custom tileset + sprite-generation pipeline (CORE-20).

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

**Gate (CORE-53/55 Gate 1):** Fresh outside testers — never solely the builder — voluntarily re-engage for 20+ minutes with zero rewards; every death is explainable; every pattern is dodgeable at the lowest intended movement speed; controls, collision, and feedback feel dependable; the frames change how testers fight. Repeated failure means pivot or stop.

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

The purposes of quests (CORE-46), factions (CORE-39/46), hubs and recognition (CORE-47) are decided; implement the slice's share of them. Implement only enough fishing, foraging, limited non-combat crafting, collection presentation, pets (cosmetic-only), and authored settlement change to test their locked supporting roles. Build one dense region with several overlapping goals — the slice zone doubles as the quest-density test.

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

**Gate (CORE-55 Gate 2):** Voluntary post-completion boss farming; dry streaks read as dedication with the attempt counter; the level gap reads as invitation; explainable-death rate stays high at density; builds feel distinct; and slice production velocity extrapolates to a viable full-game plan under the CORE-20 constraints. Failure means scope cuts in the planned order.

## Stage 10 — Production planning

Only after the slice succeeds:

- lock content volume and team plan;
- build content-authoring tools;
- establish performance budgets;
- schedule classes, regions, quests, dungeons, bosses, raids, and polish;
- decide Early Access/demo strategy;
- revisit co-op commitment and platform expansion.

## Scope rules throughout

- Do not build the large world before one small expedition loop works repeatedly.
- Do not build all three classes before one class proves the architecture.
- Do not add item volume before a few items create real choices.
- Do not use progression rewards to hide weak combat.
- Do not let controller, co-op, or newcomer considerations reduce the intended mouse/keyboard endgame ceiling.
