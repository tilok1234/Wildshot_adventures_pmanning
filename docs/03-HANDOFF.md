# Wildshot Adventures — Handoff for a New Chat or Work Session

## Current state

The project is in guided concept definition / early pre-production.

- CORE-01 through CORE-16 and CORE-21 through CORE-32 are answered; CORE-14 remains provisional/test-gated.
- CORE-17 is open and must be framed as the **first character’s journey to endgame**, not a fixed campaign.
- CORE-18 retains open structural questions while respecting the locked CORE-24 endgame direction.
- CORE-19 and CORE-20 are unanswered.
- **CORE-33 — What are the player's universal movement and defensive actions?** is the current active question and has no accepted answer.

The designer chose to continue at CORE-33 while CORE-17 through CORE-20 remain open. Continue at CORE-33 unless the designer explicitly returns to an earlier question.

## Read first

1. `08-DECISION_REGISTER.md`
2. `01-GAME_DESIGN_DOCUMENT.md`
3. `04-OPEN_QUESTIONS.md`
4. `10-LIVING_DESIGN_QUESTIONNAIRE.md` when detail or exact wording is needed.
5. `11-HANDOFF_2026-07-21_HISTORICAL.md` only as the preserved provenance record for the July 21 integration.

## Source of truth

The living questionnaire is authoritative. Companion documents summarize it and must not silently convert provisional, deferred, or unknown items into locked decisions.

## Newly locked CORE-16 summary

Wildshot Adventures does not prescribe one correct or normal session duration. A worthwhile session is defined by meaningful pursuit of a self-chosen goal, not by a guaranteed permanent upgrade. Quest progress, discovery, learning, execution improvement, completed dungeon/boss attempts, and additional targeted loot rolls can all make a session successful.

Targeted loot attempts remain independent under this baseline. More attempts create more total opportunities to have received the desired item, but failures do not raise the next roll's chance, accumulate an escalating modifier, or bank pity.

Active single-player gameplay is pausable. An ordinary dungeon is one committed instance: pausing is allowed, but leaving or abandoning ends it, and the same partially cleared instance cannot be resumed later. Exact raid duration, wings, checkpoints, and continuation rules are deferred.

## Approved CORE-21 through CORE-32 summary

- **CORE-21:** Ordinary, level-appropriate open-world combat follows a flexible encounter or aggression → situation-dependent fighting → repeated exchanges when needed → defeat → clear kill feedback → loot or portal collection loop. Ten seconds is a representative moment-to-moment window, not a required encounter length. Boss-specific loops remain separate.
- **CORE-22:** Over roughly ten minutes, the player may follow one self-chosen activity or naturally combine active low-attention grinding, quests, exploration, targeted hunts, encounters, and dungeon play. Relevant progress is expected; completion, an upgrade, or an entire dungeon clear is not guaranteed.
- **CORE-23:** Over roughly one hour, the player may sustain one pursuit or mix shorter activities, adjusting equipment, skills, inventory, route, or target only when useful. The hour should normally produce meaningful chosen progress but may be only part of a longer grind. Failed targeted rolls remain independent completed attempts.
- **CORE-24:** The central long-term objective is the zero-to-hero rise from an unknown adventurer into a powerful, recognized, legendary endgame hero. Reaching endgame begins a substantial continuation of targeted farming, unique hunts, powerful and alternative builds, hardest-solo-content mastery, optional superbosses, collection, completion, and efficiency goals. A story ending may be a milestone, not the ultimate endpoint.
- **CORE-25:** Fishing and foraging are optional supporting systems with their own levels and collection grinds. Limited crafting deterministically exchanges explicit requirements for known non-combat rewards. Housing and player-managed settlements are not planned; authored settlement changes remain possible. One small non-attacking pet may provide a modest passive benefit. No wider profession roster is planned.
- **CORE-26:** The world is a coherent network of many large outdoor zone maps connected through physical roads, gates, passes, tunnels, and discoverable paths. Interiors use separate maps where appropriate. Menu-based disconnected level selection is not the world structure.
- **CORE-27:** Geography, routes, settlements, landmarks, secrets, major interiors, bosses, and progression-critical content are handcrafted. Controlled procedural variation may refresh repeatable details inside authored spaces without erasing world knowledge or targeted pursuits.
- **CORE-28:** Outdoor regions use mostly soft danger gating and are not level-locked. Dungeons, raids, and selected challenge instances use explicit minimum levels and may have other meaningful prerequisites. Requirements must be clear, proportionate, and checked before consumable access resources are spent.
- **CORE-29:** Regions, outdoor enemies, and world bosses have stable authored difficulty and never scale to the player. Selected instanced dungeons may later receive separate optional higher-difficulty versions with their own fixed rules and rewards.
- **CORE-30:** Repeated travel uses selective paid teleportation to unlocked cities, settlements, hubs, and suitable landmarks. It can begin from most safe outdoor locations, has a visible interruptible three-to-five-second cast, and charges currency only on success. Special routes and selected content remain manual. There is no separate free recall.
- **CORE-31:** Combat is real-time, top-down, seamless, spatial, and freely aimed. No selected or locked target is ever required to aim, attack, use skills, deal damage, or kill. Hidden accuracy/evasion rolls cannot reject a visible hit. Projectile action is central, but readable authored melee arcs, beams, ground effects, and area attacks remain possible.
- **CORE-32:** Tap LMB to fire once, hold to fire at weapon cadence, or use a remappable autofire toggle that follows current free aim without auto-targeting. Ordinary attacks cost no resource; movement, aim, and attacks remain predictable and independent. Weapon patterns are deterministic, weapon-defined, terrain-aware, varied, and supported by readable impact feedback.

## How to conduct the interview

- Ask one focused question at a time and finish it before moving on.
- Let the designer answer naturally, then consolidate the intent into clear design language.
- Keep straightforward decisions concise and preserve momentum.
- Expand when a decision creates a meaningful design, balance, technical, or production consequence.
- Use existing answers before asking for a decision again.
- Mark conclusions as locked, provisional, test-gated, unknown, cut, or deferred.
- Update the living questionnaire and companion documents in sensible batches.
- Treat purposeful, targetable repetition as an intended strength rather than assuming grind should be removed.
- Do not let controller support, optional co-op, or beginner accessibility weaken the intended mouse/keyboard endgame scope.

## Recommended opening prompt

> Continue the guided design interview for **Wildshot Adventures** using the extracted project documentation as the source of truth. CORE-01 through CORE-16 and CORE-21 through CORE-32 are recorded in the living questionnaire; CORE-14 remains provisional/test-gated and CORE-17 through CORE-20 remain open. The current active topic is **CORE-33 — universal movement and defensive actions**, which has no accepted answer. Ask one focused question at a time, preserve the established design direction, keep straightforward conclusions concise, and challenge material design or production risks honestly.

## Essential design summary

Wildshot Adventures is a single-player-first, top-down 2D open-world fantasy action RPG combining RotMG-style freely aimed projectile combat and portal/dungeon/raid loot pursuit with Erenshor-style long-form, knowledge-driven, zero-to-hero MMO progression.

Three permanent classes—Archer, Warrior, Mage—use class-specific weapons whose projectile patterns define primary attacks. Tiered gear drops broadly and provides vertical progression; unique items come from named world bosses, dungeons, raids, and perhaps selected major quests, and should be powerful but situational.

Open-world play is laid-back and productive. Endgame bosses and raids may be relentlessly intense but must remain readable. Specific mobs directly drop specific dungeon portals; player knowledge and targeted hunting earn access. All content remains solo-completable. Optional online duo co-op is architecture-aware but not promised until a prototype passes.

The world consists of large handcrafted outdoor zone maps connected by physical routes, with controlled procedural variation inside authored spaces. Difficulty is stable rather than player-scaled. A selective paid teleport network compresses repeat journeys without reaching every cave, secret, wilderness destination, or dungeon route.

Fishing, foraging, limited non-combat crafting, collections, and small non-attacking pets are supporting systems rather than new pillars. Housing, player-managed settlements, broad professions, and combat-power crafting are not currently planned.

Combat requires no selected target. Tap, hold, or toggle autofire all use the player's current free aim. Primary attacks consume no resource, use deterministic weapon-defined patterns, preserve predictable movement, collide clearly with terrain, and prioritize readable feedback.

Mouse and keyboard defines the full game. Controller is secondary and can be reduced or cut rather than constrain content. The business model is a one-time Steam purchase.

## Communication preference learned during the interview

The designer values thoroughness but dislikes unnecessary administrative delay or overlong finalization of easy questions. Keep momentum. Expand only when the decision genuinely benefits from analysis.

When an answer is approved, update the current project-facing documents and verify the new text and interview marker in those exact files. Do not describe a separate copy or storage version as though a Project attachment itself has refreshed.
