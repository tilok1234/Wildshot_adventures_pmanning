# Wildshot Adventures — Proposed Prototype Specification

**Status:** Planning hypothesis, not a locked content promise. It translates current decisions into the cheapest useful tests.

## Prototype objective

Prove that freely aimed projectile combat is enjoyable without rewards and can support the intended progression, readability, boss-learning, and optional co-op architecture.

## Phase A — Solo combat laboratory

### Minimum content

- One greybox arena.
- One temporary player class shell.
- Independent movement and aiming.
- Tap-to-fire and hold-to-fire primary attack.
- One remappable autofire toggle with a clear HUD state.
- No selected-target requirement or automatic enemy tracking.
- No mana, stamina, ammunition, durability, or reload cost for ordinary primary attacks.
- No universal movement or defensive action beyond walking (CORE-33): dodging is tested as pure movement.
- One equipped-ability test slot with several swappable test abilities (CORE-34).
- Three deterministic weapon frames with meaningfully different positioning:
  - accurate long-range shot;
  - short-range spread;
  - piercing, returning, or otherwise spatially distinctive pattern.
- Solid terrain, corners, and obstacles for line-of-fire and collision testing.
- Five to six enemy behaviors.
- One elite encounter.
- Hitbox and projectile debug visualization.
- Clear impact, blocked-hit or immunity, kill, and damage-number feedback controls.
- No loot, experience, quests, or permanent progression in the first feel test.

### Questions to answer

- Is moving and firing enjoyable for at least 20 minutes without rewards?
- Does ordinary, level-appropriate combat naturally produce the CORE-21 sequence of encounter or aggression, situation-dependent fighting, repeated exchanges when needed, defeat, clear kill feedback, and collection?
- Can weaker enemies be defeated directly while more demanding ordinary encounters require additional movement, dodging, positioning, enemy prioritization, or skill use, without making every fight follow one rigid script?
- Can the player attack, use the prototype actions, deal damage, and kill without selecting or locking a target?
- Do tap, hold, and toggle-autofire inputs all follow the player's current free aim, including into empty space, without requiring repeated clicking or becoming automatic combat?
- Does firing preserve predictable movement speed, direction, and aim responsiveness?
- Do identical inputs produce identical projectile placement without random bloom or unexplained drift?
- Do the three weapon frames change where and how the player fights?
- Do terrain and corners create useful positioning decisions without visible shots snagging unpredictably?
- Do impacts, kills, immunities, and blocked damage read clearly without routine screen shake, global hit-stop, or feedback clutter?
- Can ordinary combat feel relaxed without becoming passive?
- Can an elite require active skill use without becoming unreadable?
- Does the player understand why damage occurred?
- Can intensity increase substantially while safe spaces and responses remain legible?

### Exit gate

Do not add large content or progression systems until testers voluntarily re-engage enemies, experiment with weapons, understand deaths, and report that movement, aiming, firing, autofire state, projectile placement, terrain collision, and hit feedback feel dependable.

The gate is judged by at least a few fresh outside testers, never solely by whoever built the lab (CORE-53). Every test pattern must additionally be verified dodgeable at the lowest intended movement speed, not a comfortable mid-tier loadout.

## Phase B — Enemy and readability grammar

Prototype reusable components:

- direct aimed shot;
- predictive shot;
- fan or cone;
- radial burst;
- delayed ground hazard;
- shield/guard role;
- healer or support priority;
- chaser or space-control role.

Test ordinary packs with one or two pressures and elite/boss patterns with higher complexity. Do not use projectile density alone as difficulty.

Enemy patterns may use appropriate authored variation, but player primary-attack tests must preserve the CORE-32 deterministic placement rule.

## Phase C — Build grammar

Add one prototype class with:

- one class resource;
- six to eight candidate skills;
- a limited equipped skill set;
- two or three plausible build directions;
- a small set of equipment effects that change decisions without replacing the weapon pattern.

The same encounters should feel different because positioning, timing, and priorities change—not only because damage numbers change.

## Phase D — Progression and loot mini-loop

Add only enough structure to test:

- character levels and skill points;
- a minimal readable stat set;
- standard tiered weapons/equipment;
- one authored unique weapon with a situational pattern;
- one portal-dropping enemy;
- one short dungeon and boss;
- tiered baseline rewards plus a unique-item chase.

Test whether repeated runs remain productive when the unique does not drop. The player should be able to identify value in self-chosen goal progress, learning, execution improvement, completed attempts, and additional independent rolls without the prototype pretending that a failed roll improved the next one.

When activity scaffolding exists, test the locked loop hierarchy: a roughly ten-minute window may sustain one activity or mix several naturally, and a roughly one-hour window should normally create meaningful progress toward a chosen pursuit without requiring a guaranteed upgrade, finished dungeon, world change, or completed objective.

Also test the ordinary-dungeon commitment rule:

- pausing preserves the active single-player run;
- leaving or abandoning ends the instance;
- re-entry starts a fresh instance rather than resuming a partial clear;
- the reset is communicated clearly enough that it feels like a known commitment rather than lost progress.

## Phase E — Two-player network feasibility gate [T]

Run this early, after solo movement/combat is stable but before building the large world.

Required test:

1. Two players join one room.
2. Both move and aim independently.
3. Both fire synchronized projectiles.
4. One enemy targets and damages either player consistently.
5. Both players can damage the enemy without state disagreement.
6. Both receive personal loot.
7. One portal admits both players to one dungeon instance.
8. Disconnect/reconnect does not corrupt saves or world state.

### Pass condition

Co-op remains in provisional scope only when the prototype is stable, readable, testable, and does not force compromises to solo combat or project architecture.

### Fail condition

Cut or defer co-op. Continue the solo game without redesigning the foundation.

## Prototype instrumentation

Build early tools for:

- spawn/reset encounter;
- slow motion and invulnerability;
- collision/hitbox display;
- projectile count and density;
- primary-attack input state and autofire-state display;
- deterministic shot-placement capture or replay;
- terrain-collision and corner-snag logging;
- impact, immunity, blocked-hit, kill, and damage-number feedback toggles;
- damage, proc, and resource logs;
- runtime stat editing;
- forced drops;
- drop-rate and percentile-acquisition simulation;
- attempt counters that distinguish completed runs from loot success;
- session-goal and session-end playtest logging;
- ten-minute activity-mix and one-hour pursuit-progress logging;
- pause, abandon, and fresh-instance reset tests;
- save reset and world-state toggles;
- unattended AI bot harness (movement-only dodgeability proofs at lowest speed, soak/regression runs, percentile simulation) — mechanical verification only, never a substitute for human gate judgment (CORE-53).

## Vertical-slice scope (CORE-38, 2026-07-26)

[P] The vertical slice is built around one class — provisionally the **Archer** — with roughly three to five genuinely distinct weapon frames, three to four ability items covering different roles (at minimum mobility, defense, and burst), and two to three build directions through the skill tree. The slice must prove the locked combat pillar in practice: movement-only dodging, the single equipped active, weapon-owned patterns, honest boss design, and armor and ring tradeoffs. Three classes remain locked for the full game; per-class full-game content counts are explicitly deferred until CORE-20 resolves production constraints.

CORE-52 fills in the full content bill: one zone (outskirts to dangerous pocket) plus a hub; 8–10 enemy types with an elite and a roaming rare; one portal enemy, one 10–20 minute committed dungeon and boss; tiered and cosmetic drops plus one unique weapon; a main-quest slice with one level gap, 10–15 side quests, and one faction set with vendor; roughly 3–5 hours plus a repeatable boss farm; co-op, raids, hardcore, gathering, and mounts excluded. The slice ships with explicit gate questions (voluntary post-completion farming, dry-streak feel with the attempt counter, gap-as-invitation, explainable deaths) and one authored secret as the discovery-pillar test.
