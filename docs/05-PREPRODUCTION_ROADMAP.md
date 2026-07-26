# Wildshot Adventures — Pre-production Roadmap

**Status:** Recommended sequence. It does not assign dates or assume team capacity that has not been discussed.

## Stage 0 — Finish plan-blocking core questions

CORE-16 is resolved: the game does not prescribe a normal session duration, and session value is not dependent on receiving a permanent upgrade. The remaining plan-blocking questions are CORE-17 through CORE-20:

- first character's journey to endgame: target length and exact endgame threshold;
- replay/endgame intent;
- tone, rating, and content boundaries;
- hard production constraints: team, engine, budget, time, skills, and target window.

The designer has completed CORE-21 through CORE-32 and chosen to continue at CORE-33 while CORE-17 through CORE-20 remain open.

**Gate:** The project has an honest scope envelope.

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

CORE-31 and CORE-32 establish the combat format and primary-attack baseline. Resolve CORE-33 onward as needed while implementing:

- independent movement and free aiming with no selected-target requirement;
- tap-to-fire, hold-to-fire, and a visible remappable autofire toggle;
- resource-free ordinary primary attacks;
- deterministic weapon-defined patterns;
- predictable movement while firing;
- clear terrain collision and line-of-fire behavior;
- readable impact, immunity, blocked-hit, and kill feedback;
- one universal defensive or movement action;
- three weapon frames, several enemy behaviors, and one elite.

Do not add progression rewards until the no-reward combat test passes.

**Gate:** Combat remains enjoyable and understandable without loot, feels dependable while moving and aiming, and never relies on hidden targeting, accuracy, or movement behavior.

## Stage 3 — Enemy, projectile, and readability grammar

Establish telegraph language, hostile/friendly visual hierarchy, projectile rules, safe-space readability, encounter roles, and intensity scaling.

**Gate:** Deaths are understandable and endgame intensity appears feasible rather than visually chaotic.

## Stage 4 — Class, skill, and weapon grammar

Prototype one class deeply before building all three. Define the boundary between class, skill tree, weapon, and equipment. Test several build directions.

**Gate:** Builds change decisions and positioning, not only sheet damage.

## Stage 5 — Optional co-op technical gate

Run the two-player greybox test before large world production. Keep solo design authoritative.

**Gate:** Co-op is either retained provisionally with evidence or cleanly deferred/cut.

## Stage 6 — Levels, stats, equipment, and loot

Define the smallest readable stat set, scaling rules, equipment tiers, unique-item rules, source targeting, duplicate behavior, and protection against multiplicative projectile/proc explosions.

**Gate:** Progression feels tangible without making execution irrelevant or creating one mandatory build.

## Stage 7 — Portal-to-dungeon vertical mini-loop

Build one portal source, one field route, one short dungeon, one boss, tiered baseline loot, and one unique chase.

Test the complete friction budget: travel + enemy availability + portal chance + dungeon commitment/reset boundary + dungeon length + boss learning + drop rarity.

**Gate:** A failed unique roll can still leave a self-directed session feeling productive; repeated attempts feel earned rather than obstructed; the player understands that rolls are independent; pausing protects an active run while abandoning clearly resets the ordinary-dungeon instance.

## Stage 8 — World, quests, hub, and recognition

Define the detailed purposes of quests, factions, hubs, world recognition, and return visits. Implement only enough fishing, foraging, limited non-combat crafting, collection presentation, pets, and authored settlement change to test their locked supporting roles without allowing them to become mandatory combat progression or a parallel profession economy. Build one dense region with several overlapping goals.

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

Exact content counts are deferred to CORE-52.

**Gate:** Measurable player evidence justifies scaling to full production.

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
