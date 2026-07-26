# Wildshot Adventures — Open Questions

**Current interview position:** **CORE-33 — universal movement and defensive actions** is active and has no accepted answer.  
**Open but currently bypassed by designer choice:** CORE-17 through CORE-20.

This file contains unanswered core questions and deferred decisions. It should prevent a new session from reopening matters that are already locked.

## Recently resolved

- **CORE-16 [L]:** The game does not prescribe a normal session duration. Self-chosen goal progress, learning, mastery, relevant attempts, and independent loot rolls can make a session worthwhile without a permanent upgrade. Single-player play is pausable. Leaving or abandoning an ordinary dungeon ends that instance; partial clears are not resumed later.
- **CORE-21 [L]:** Ordinary level-appropriate combat cycles through encounter or aggression, situation-dependent fighting, repeated exchanges when needed, defeat, clear kill feedback, and loot or portal collection. Ten seconds is representative, not a required fight length; boss-specific loops remain separate.
- **CORE-22 [L]:** A ten-minute window may contain one self-chosen activity or a natural mixture of active grinding, quests, exploration, targeted hunting, encounters, and dungeon play. Relevant progress is expected, but completion or an upgrade is not guaranteed.
- **CORE-23 [L]:** A one-hour window may sustain one pursuit or combine shorter activities, with preparation or retargeting only when useful. Meaningful progress is expected, but the hour may be part of a longer grind and independent failed loot rolls remain completed attempts.
- **CORE-24 [L]:** The long-term objective is a zero-to-hero rise into a powerful, recognized, legendary endgame character. Endgame is a major transition into substantial farming, build, mastery, superboss, collection, completion, and efficiency pursuits—not the end of the game.
- **CORE-25 [L/P]:** Fishing and foraging are optional leveled supporting systems with primarily cosmetic and collection-oriented rewards. Limited crafting gives deterministic known non-combat rewards. Housing and player-managed settlements are not planned; authored settlement changes remain possible. Small non-attacking pets are optional. No broad profession roster is planned.
- **CORE-26 [L/P]:** The world uses many large outdoor zone maps connected by physical routes, with separate interior maps where appropriate. It must feel like one coherent world rather than disconnected menu-selected levels.
- **CORE-27 [L/P]:** The world foundation and progression-critical content are handcrafted. Controlled procedural variation may refresh repeatable details inside authored spaces without erasing world knowledge, reliable targeting, or authored identity.
- **CORE-28 [L/P]:** Outdoor regions use soft danger gating and are not level-locked. Dungeons, raids, and selected instances use explicit minimum levels and may have meaningful additional prerequisites. Requirements must be clear, proportionate, and checked before access resources are consumed.
- **CORE-29 [L/P]:** Regions, outdoor enemies, and world bosses have fixed authored difficulty and never scale to the player. Selected instanced dungeons may later receive separate fixed higher-difficulty versions.
- **CORE-30 [L/P]:** Repeated travel uses selective paid teleportation to eligible unlocked destinations. It begins only from safe outdoor situations, has an interruptible three-to-five-second cast, charges only on success, and does not replace special manual routes. There is no free recall.
- **CORE-31 [L]:** Combat is real-time, top-down, seamless, spatial, and freely aimed. No selected target is required for any combat action or kill, and hidden accuracy/evasion rolls cannot invalidate a visible hit.
- **CORE-32 [L/P]:** Tap, hold, and toggle-autofire inputs all use current free aim. Ordinary primary attacks cost no resource, preserve predictable movement and aiming, use deterministic weapon-defined patterns, interact clearly with terrain, and provide readable hit feedback.

## Priority 1 — Scope and format blockers still open

1. **CORE-17:** What is the target length of the **first character’s journey to endgame**, what mechanical threshold counts as reaching endgame, and how should focused progression, optional content, and later endgame time be measured separately?
2. **CORE-18:** What replay or long-term endgame experience is intended?
3. **CORE-19:** What tone, age rating, violence, horror, language, humor, and content boundaries are intended?
4. **CORE-20:** What are the hard production constraints: team size, engine, skills, budget, weekly hours, timeframe, and asset limits?

## Priority 2 — Loops and world

CORE-21 through CORE-30 are answered at the core-design level. Their detailed implementation questions remain deferred below and in the Decision Register.

## Priority 3 — Combat and progression

- **CORE-31 [RESOLVED]:** exact combat format.
- **CORE-32 [RESOLVED]:** primary attack behavior and no-reward enjoyment.
- **CORE-33 [ACTIVE]:** universal movement/defense actions.
- CORE-34: active ability count and kit roles.
- CORE-35: focus-targeting purpose, if any.
- CORE-36: intensity curve.
- CORE-37: exact class/weapon/equipment responsibility boundary.
- CORE-38: class, weapon-frame, and build counts for slice/full game.
- CORE-39: purpose of levels.
- CORE-40: smallest readable stat set.
- CORE-41: how equipment changes play.
- CORE-42: deliberate acquisition path for important items, including whether any guarantees coexist with the independent-roll CORE-16 baseline.
- CORE-43: death and recovery.

## Priority 4 — Content systems

- CORE-44: ordinary enemy-group tactics.
- CORE-45: role of dungeons, elites, bosses, and raids.
- CORE-46: purpose of quests.
- CORE-47: hub, faction, settlement, and recognition purpose.
- CORE-48: crafting, gathering, and automation purpose.
- CORE-49: acceptable grind times and reward cadence.
- CORE-50: accessibility and comfort requirements.
- CORE-51: visual/audio readability rules.

## Priority 5 — Production gates

- CORE-52: exact vertical-slice content.
- CORE-53: first playable milestone.
- CORE-54: five largest risks after constraints are known.
- CORE-55: measurable continuation gates.

## Deferred details already identified

### Portals, ordinary dungeons, and raids

Locked by CORE-16:

- active single-player play is pausable;
- leaving or abandoning an ordinary dungeon ends that instance;
- the same partially cleared ordinary dungeon is not resumed later.

Still open:

- exact portal drop rates and whether they vary by enemy/region;
- portal persistence, ownership, and expiration;
- death and retry rules;
- dungeon reset timing and save boundaries;
- whether first discovery changes future access;
- party entry and portal consumption if co-op survives;
- exact raid duration and maximum uninterrupted commitment;
- raid wings/sections, checkpoints, continuation, and re-entry rules.

### Loot

- exact tier structure and stat ranges;
- unique drop rates;
- whether deterministic guarantees, tokens, or other fallback systems exist outside the independent-roll pursuit described by CORE-16;
- duplicate behavior;
- class-relevant drop filtering;
- unique upgrade/retention across later tiers;
- whether selected major quests award uniques.

### Classes and skills

- class resources;
- skill counts and loadout structure;
- skill-tree size and respec rules;
- weapon families per class;
- which effects are allowed to influence projectile patterns indirectly.

### World, access, difficulty, and travel

- exact outdoor-zone sizes, route placement, and secret-connection requirements;
- exact procedural systems, content pools, placement rules, reset schedules, and selected dungeon applications;
- exact minimum levels and which activities use them;
- placement and implementation of keys, quests, boss victories, events, environmental protection, discovered routes, and other gates;
- exact regional difficulty ranges;
- higher-difficulty dungeon-version names, eligibility, unlock conditions, mechanics, entry requirements, and rewards;
- exact auto-travel destinations, individual unlock requirements, prices, and whether costs vary by distance or destination;
- mount, permanent-shortcut, and other manual-travel mechanics;
- remote quest turn-in and remote storage access, which CORE-30 did not decide.

### Supporting activities and collections

- fishing and foraging interactions, progression curves, regional placement, rarity structures, collections, and rewards;
- limited-crafting recipes, exact requirements, resource sources, interfaces, and eligible non-combat reward types;
- collection-menu categories, metadata, previews, and completion presentation;
- pet acquisition, progression, passive benefits, balance, collection, and presentation;
- exact quests, victories, or world events that produce authored settlement changes.

### Combat

- universal movement and defensive actions;
- active ability count, activation, kit roles, and ability-specific animation commitments;
- detailed player, enemy, projectile, and terrain hitbox/collision geometry;
- aim assistance and the optional focus-target feature's exact purpose;
- exact weapon statistics, cadence ranges, final primary-attack patterns, and exceptional mechanics;
- default autofire binding and HUD treatment;
- hit-feedback and collision tuning;
- enemy-specific and boss-specific encounter loops.

### Co-op

- whether the early prototype passes;
- host/guest quest and world progression;
- personal loot specifics;
- scaling and enemy-targeting rules;
- revival and death;
- pause behavior in co-op;
- disconnect/rejoin and save ownership.

### Controls

- controller viability target;
- aim assistance and dead-zone rules;
- Steam Deck performance/UI target;
- whether controller remains in release scope after testing.
- default autofire hotkey and final HUD indicator treatment.

## Questions that are already answered and should not be reopened casually

- three permanent classes and at least three character slots;
- weapon-owned primary projectile patterns;
- targeted direct portal drops rather than fragment crafting;
- tiered gear versus situational unique loot;
- solo-completable content and no mandatory roles;
- mouse/keyboard as design authority;
- premium Steam purchase;
- no prescribed normal session duration or requirement that every session grant a permanent upgrade;
- independent targeted loot rolls under the CORE-16 baseline;
- pausable single-player play and committed ordinary-dungeon instances;
- RotMG and Erenshor as primary references;
- accessible beginning without compromising endgame.
- the flexible ten-second ordinary-combat loop and its non-prescriptive duration;
- self-directed ten-minute and one-hour loops without guaranteed completion or upgrades;
- the zero-to-hero long-term objective and endgame as a core continuation rather than post-story cleanup.
- optional fishing and foraging, limited non-combat crafting, interface-led collections, small non-attacking pets, no current housing, no player-managed settlements, and no broad profession roster;
- the layered multi-map world, handcrafted foundation, and controlled procedural variation;
- mostly soft outdoor gating with clear, purposeful contained gates and minimum-level instance requirements;
- fixed authored outdoor/world-boss difficulty with no player scaling and only separate optional higher-difficulty dungeon versions;
- selective paid teleport travel with an interruptible three-to-five-second cast and no free recall;
- real-time seamless free-aim combat that never requires a selected target;
- tap, hold, and toggle-autofire primary attack input; no ordinary attack resource cost; deterministic weapon-defined patterns; predictable movement; terrain collision; and readable hit feedback.
