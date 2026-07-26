# Wildshot Adventures — Living Game Design Document

**Version:** Concept snapshot through CORE-34; CORE-35 active  
**Date:** 2026-07-26  
**Status:** Guided concept definition / early pre-production; CORE-17 through CORE-20 remain open and CORE-35 is active.

## 1. Executive summary

**Wildshot Adventures** is a top-down 2D open-world fantasy action RPG that combines the long-term progression, dense world, meaningful grind, and systems knowledge of a classic MMO with freely aimed projectile combat in a complete single-player adventure.

Players create an Archer, Warrior, or Mage; explore a content-rich fantasy world; gain levels and class skill points; hunt specific enemies for dungeon portals; master increasingly intense bosses and raid-scale encounters; and pursue both broadly obtainable tiered equipment and powerful situational unique items.

### Short pitch

> A single-player MMO-scale adventure where every fight is freely aimed: hunt monsters for dungeon portals, master brutal projectile bosses and raids, and grind toward powerful equipment in a dense fantasy world.

## 2. Player promise [L]

> Explore a vast fantasy world filled with battles and events as a permanently chosen Archer, Warrior, or Mage; master freely aimed projectile combat; gain levels and class skill points through quests, monsters, and other activities; and collect progressively stronger RPG equipment and class-specific weapons, including rare boss-dropped uniques whose powerful but situational projectile patterns create distinct ways to fight.

## 3. Core fantasy [L]

The player inhabits a clear **zero-to-hero** arc. A new character begins unknown, inexperienced, and poorly equipped. Through persistence, knowledge, levels, equipment, class development, quests, dungeons, and major victories, the character becomes powerful and increasingly recognized by the world.

The rise should be visible in two dimensions:

- **Mechanical growth:** higher levels, developed skills, stronger statistics, better weapons, and mastery of difficult encounters.
- **World recognition:** NPCs, factions, settlements, and the wider world increasingly acknowledge the character's achievements. The exact recognition systems remain unresolved.

## 4. Target player [L]

The primary audience is experienced RPG, MMO, action-RPG, and projectile-combat players who enjoy:

- deep systems and long-term mastery;
- substantial but purposeful repetition;
- equipment hunting and targetable rewards;
- learning zones, enemies, statistics, routes, and encounter rules;
- relaxed farming sessions as well as highly demanding endgame combat;
- dozens or potentially hundreds of hours of character development without live-service obligations.

**Design shorthand:** accessible beginning, uncompromised endgame.

The opening should teach clearly and increase difficulty progressively. New players are welcome, but their presence must not cap the complexity, intensity, or systems depth of advanced content.

## 5. Design pillars [L]

### 5.1 Freely aimed projectile combat is satisfying, readable, and expressive in its own right

From relaxed open-world grinding to demanding dungeons, bosses, and raids, movement, independent aiming, weapon attacks, positioning, dodging, enemy prioritization, and class skills should feel responsive and create meaningful decisions. Enemies, weapons, skills, and builds should provide varied ways to fight while preserving clear feedback and learnable threats.

Not every encounter must require every action, but active control, execution, and game knowledge should consistently improve the player's safety and efficiency. Combat must remain enjoyable even when no valuable item drops.

### 5.2 Meaningful progression continually expands who the player is, what they can do, and what they can pursue

The player grows from an unknown, inexperienced adventurer into a powerful, recognized hero through self-directed play. Progress should be tangible across character strength, combat possibilities, equipment and builds, knowledge, access, reputation, and the challenges the player can pursue and overcome—not merely through larger numbers.

Across the journey, progression should regularly unlock new worthwhile grinds and long-term pursuits. As the player becomes stronger, more knowledgeable, better equipped, and more accomplished, they become capable of reaching, surviving, and efficiently farming new enemies, regions, portal sources, dungeons, bosses, raids, rewards, equipment, and build opportunities. Progression should therefore create new reasons to play, rather than only making old content faster.

Different activities and playstyles may provide different routes forward. Earlier grinds may remain useful without preventing new ones from becoming increasingly ambitious and rewarding. Reaching endgame begins another substantial stage of progression through specialization, build refinement, targeted rewards, collection, mastery, and the game's hardest pursuits.

New pursuits do not all require literal level gates. They may become available because the player has gained sufficient power, found access, completed a prerequisite, learned where to hunt, or developed enough skill to handle them.

### 5.3 Exploration builds world knowledge, and world knowledge turns discovery into deliberate pursuits

The world should reward curiosity, attention, and accumulated experience. Through exploration and play, the player learns its regions, routes, enemies, dangers, prerequisites, portal sources, reward sources, and other meaningful relationships. This knowledge helps them choose concrete goals, prepare appropriately, and deliberately pursue new content, rewards, and grinds rather than depend on directionless wandering, forced waiting, or arbitrary luck just to begin an attempt.

Discovery should provide both immediate and future value. The player may find secrets, landmarks, encounters, useful routes, or dangerous content before they are ready to overcome it, creating reasons to return later. As the player's goals, strength, access, and knowledge develop, earlier regions may gain new relevance instead of simply becoming exhausted and forgotten.

Specific enemies dropping portals to associated dungeons remains an important expression of this pillar, but not its entire scope. Similar learnable and targetable relationships may connect the player to desired equipment, bosses, quests, regions, and other progression opportunities.

Essential knowledge should eventually be discoverable or recordable inside the game. Mystery, uncertain rewards, and unexpected opportunities should remain, and roaming without a fixed goal should still be worthwhile. "Targetable" means that once the player understands a pursuit, they can normally attempt it deliberately; it does not guarantee the desired reward, remove travel or preparation, or reduce the world to selecting destinations from a menu.

### 5.4 Mastering major challenges becomes a rewarding long-term pursuit

Dungeons, world bosses, raids, optional superbosses, and other concentrated encounters begin as dangerous but learnable challenges. As the player improves their knowledge, execution, build, and equipment, they become increasingly consistent and efficient to overcome. This creates satisfying repetition and long-term goals through character progression, stronger equipment, powerful situational unique items, completion goals, and greater mastery.

Mastery does not necessarily make difficult content trivial; the hardest encounters may remain demanding even after the player understands them.

## 6. Anti-pillars [L]

The game must not become:

1. **Passive or self-playing combat.** Appropriately leveled enemies cannot be handled effectively by holding fire and ignoring their behavior.
2. **MMO-style waiting used as content.** No daily/weekly lockouts, long forced respawns, rare-spawn camping, forced waiting, or empty travel used merely to extend playtime.
3. **Directionless or unnecessarily cluttered grind.** Desired dungeons and rewards need learnable, targetable sources. Fragments and currencies exist only when they add a real decision or benefit.
4. **Unreadable projectile combat.** Endgame may be relentlessly intense, but attacks, hazards, safe spaces, and deaths must remain visually legible and mechanically learnable.
5. **A single universally superior unique weapon.** Uniques can be exceptionally strong in their intended situations, but meaningful tradeoffs must preserve choice.

## 7. Character and class structure [L]

- Three classes: **Archer, Warrior, and Mage**.
- Class is selected at character creation and cannot be changed on that character.
- A profile/account supports at least three character slots, allowing one character of each class.
- Each class has a separate skill tree.
- Levels grant skill points and broader progression.
- Each class must remain capable of completing all content solo.
- Mandatory tank/healer/DPS party composition is excluded.

## 8. Combat direction [L/P]

Combat is top-down and freely aimed. Movement and aiming are independent. The player uses one equipped active ability alongside a weapon-defined primary projectile attack.

### Combat format [L]

Wildshot Adventures uses real-time, top-down, freely aimed projectile-action combat. Keyboard movement and mouse aiming are independent, and attacks follow the player's aim rather than a selected or locked target.

Combat occurs seamlessly in the current outdoor, interior, dungeon, or raid map. There is no separate battle screen, combat instance, turn transition, or required target-engagement state before the player can attack.

**Combat never requires a selected or locked target.** The player can aim, fire, and activate combat actions without an enemy being present or selected, including aiming or firing into empty space wherever the action permits. Acquiring a target is never a prerequisite for attacking, using skills, dealing damage to an enemy, or killing it. Any later focus-targeting feature must remain optional and subordinate to free aiming; its exact informational, controller-assistance, or other functions remain deferred to CORE-35.

There is no tab targeting, passive auto-combat, turn-based play, or tactical pause-and-command system. Controller support, if retained, may use a secondary twin-stick equivalent, but it cannot restrict the primary mouse-and-keyboard combat design.

Combat resolution is primarily spatial. An attack must physically connect with an enemy or other valid hitbox. A visibly successful hit is not rejected by hidden accuracy or evasion rolls. Blocking, immunity, invulnerability, and similar defenses remain possible when clearly communicated.

Projectile combat is the game's central combat language, but not every action must literally be a projectile. Clearly authored melee arcs, beams, ground effects, area attacks, and other class or enemy mechanics are allowed when they preserve direct control, free aiming where appropriate, and readable outcomes. The already-established weapon-defined primary attacks remain projectile-based.

Single-player combat can normally be paused, freezing the action completely. Pausing is not used to issue commands or perform combat actions.

Exact skill activation, ability-specific animation commitments, detailed hitbox and collision geometry, aim assistance, and optional focus-target behaviour remain unresolved for CORE-34 onward. Universal movement and defensive actions are resolved by CORE-33 below.

### Primary attack [L/P]

Tapping LMB performs one primary attack. Holding LMB attacks continuously at the equipped weapon's cadence, so repeated clicking is never required. A remappable autofire hotkey toggles the same held-attack state and has a clear HUD indicator. Autofire follows the player's current aim—even into empty space—and never selects, tracks, or aims at enemies automatically.

Ordinary primary attacks consume no mana, stamina, ammunition, durability, or reload resource. They are always available; mana is reserved for active abilities.

Movement, aiming, and attacking remain independent. Ordinary attacks do not unexpectedly root, slow, direction-lock, displace, or reduce aim responsiveness. Special weapons may use clearly communicated charge times, wind-ups, recoil, or movement trade-offs as deliberate exceptions that behave consistently every time.

Primary attacks use deterministic, authored patterns. There is no random accuracy bloom or unexplained projectile drift. Fixed spreads, fans, bursts, and other formations are allowed, but identical inputs under identical conditions produce identical shot placement.

The equipped weapon defines the complete primary-attack behaviour rather than only its damage. Projectile count, formation, range, speed, cadence, piercing, bouncing, returning, bursts, waves, orbiting behaviour, and other readable spatial properties may all contribute to weapon identity. Development should prototype this design space broadly before narrowing the final arsenal. Finished weapons must remain readable, learnable, useful, deterministic, and meaningfully distinct. Standard tiered weapons may preserve a familiar style while improving numerically; alternative and unique weapons may substantially change positioning, aiming, and combat rhythm.

Hit feedback combines clear projectile impacts, brief enemy flashes, responsive audio, and readable damage numbers that can be reduced or disabled. Kills, immunities, blocked damage, and any critical or heavy hits receive appropriately stronger feedback. Routine attacks do not cause constant screen shake, movement disruption, or global hit-stop; feedback must remain satisfying without obscuring dense encounters or interfering with precise dodging.

Ordinary projectiles require a clear line of fire and collide predictably with solid terrain. Collision should match visible geometry and avoid frustrating corner snagging. Clearly identified weapons may pierce, bounce from, curve around, or arc over obstacles as authored exceptions. Different patterns should reward different positioning and attack angles, with no universal hidden distance penalty applied to every weapon.

Primary attacks are intended to remain enjoyable without rewards through dependable control, continuous aiming and positioning decisions, learnable weapon behaviour, meaningful terrain and angle use, and responsive but readable impact feedback.

Exact weapon statistics, cadence ranges, individual patterns, exceptional mechanics, default autofire binding and HUD treatment, collision tuning, and feedback tuning remain unresolved for prototyping and later combat planning.

### Universal movement and defensive actions [L]

Dodging is purely movement-based, in the Realm of the Mad God tradition. The universal kit is movement plus free aim, and nothing else: no universal dash, roll, blink, sprint, block, parry, shield, or invulnerability-frame action exists. Survival comes from continuous positioning, spacing, routing, threat reading, and enemy prioritization at the character's movement speed.

This commitment carries binding consequences. Every attack pattern must be honestly avoidable through movement alone at its intended progression level—and, because all classes complete all content solo, at the baseline mobility of the least mobile class. Movement speed becomes a premier statistic and balance lever whose sources, growth, and caps must be tuned deliberately. Without a panic escape, the locked readability rules become even more load-bearing: deaths must always trace to visible, learnable mistakes, and death and recovery design must account for the absence of an escape action. Pause remains available but performs no combat action.

Class skill trees may still offer class-specific mobility or defensive abilities as class tools rather than universal actions [P]; no encounter may require a specific class's tool. Ability roles and counts are decided in CORE-34.

### Active ability and ability items [L/P]

Each character has exactly one active ability, granted by an equipped ability item rather than the skill tree. Each class has its own large pool of possible ability-equip items, so ability variety, build identity, and new playstyles come from the loot hunt: the weapon owns the primary pattern, the ability item owns the active, and armor owns supporting statistics. A new playstyle is a farming target, not a menu choice. Active abilities run on mana; the equipped item defines its own behaviour and cost.

The class skill tree grants no active abilities. It provides passives, resource behaviour, and class specialization under a binding condition: meaningful nodes must change behaviour rather than only numbers—modifying how equipped ability items work, altering resource behaviour, or specializing toward categories of ability items. The tree shapes *how* the equipped ability plays; the item decides *what* it is. A max-level capstone that supercharges the equipped ability item remains open design space [P].

No fixed role checklist is mandated: ability items may provide mobility, defense, burst, crowd control, utility, or other roles, and choosing role coverage is part of build choice and the hunt. Because the equipped item is the only active and no universal dodge exists, no encounter may require a specific ability item—or any ability at all—to be survivable. Movement must remain sufficient, and boss and encounter design carries this burden deliberately.

Exact per-class item pools, individual ability designs, mana costs, cooldown or charge models, acquisition sources, rarity structure, and the capstone concept remain unresolved.

### Experience curve [L]

- **Open world:** laid-back, satisfying, and productive; still requires awareness and active participation.
- **Dungeons and world bosses:** faster, more energetic, and more demanding.
- **Endgame bosses and raids:** may become relentlessly intense, provided patterns remain readable and learnable.

Appropriately leveled content should retain meaningful resistance. Progression should not erase player participation.

### Weapon ownership [L]

The equipped weapon owns the primary projectile pattern. The class skill tree improves the class's combat plan without routinely replacing or multiplying the weapon pattern.

Direct universal pattern nodes such as unrestricted extra projectiles, infinite piercing, or broad splitting are excluded from the baseline because they can multiply damage and on-hit systems uncontrollably.

## 9. Progression model [L/P]

Distinct progression layers should have distinct jobs:

| Layer | Primary responsibility |
|---|---|
| Character level | Broad advancement and skill-point acquisition |
| Class skill tree | Behaviour-changing passives, resource behavior, and class specialization (no active abilities) |
| Standard weapon | Primary attack damage and conventional projectile pattern |
| Unique weapon | Authored, powerful, situational projectile behavior |
| Ability item | The single equipped active ability and its behavior |
| Armor/equipment | Classic RPG statistics and supporting effects |
| Player knowledge | Understanding zones, stats, routes, portal sources, loot sources, and encounters |

Harder content generally provides statistically stronger equipment. The exact stat set, scaling curves, level cap, and gear tiers remain unanswered.

## 10. Loot model [L/P]

### Tiered equipment

Tiered weapons and equipment form the dependable vertical power ladder. They may drop from normal enemies, elites, chests, world bosses, dungeons, raids, and other appropriate sources. The maximum tier follows the source's difficulty and progression level.

Bosses may drop tiered equipment as baseline rewards in addition to unique-item chances.

### Cosmetic and collection drops [P]

Bosses and other named encounters may additionally drop cosmetic and collection items, so repeated attempts stay productive during unlucky streaks. Reward breadth—not pity—is the dry-streak mitigation: unique-item rolls remain independent under the CORE-16 baseline, while cosmetics, collection entries, and baseline tiered rewards give most runs something permanent. Cosmetic drops are recorded directly in the collection interface rather than occupying inventory space.

### Unique equipment

Unique items come from named, authored high-value sources:

- world bosses;
- dungeon encounters and bosses;
- raid encounters and bosses;
- potentially selected major quests [P].

Generic normal enemies do not randomly drop unique items.

Unique weapons should be powerful but situational. Examples of valid tradeoffs include range, precision requirements, fire rate, optimal distance, crowd versus single-target performance, and difficult returning or converging patterns.

Selected quest uniques, if retained, should generally be authored guaranteed rewards rather than another random roll. Exact drop rates, pity systems, duplicate handling, class filtering, and upgrade retention remain unresolved.

## 11. Portal, dungeon, boss, and raid loop [L/P]

Specific open-world enemies are associated with specific dungeons and directly drop their portals. Portal fragments are not the baseline system.

Current target concept, subject to testing:

- associated normal enemies: roughly **20–30%** portal chance;
- associated world bosses: roughly **50–100%** portal chance.

The important principle is not the exact percentage. Relevant enemies must exist in sensible concentrations and be reliably farmable by a player who knows where to hunt.

### Intended loop

1. Learn which enemy is associated with a desired dungeon.
2. Travel to an appropriate region and hunt that enemy deliberately.
3. Earn a dungeon portal through active open-world play.
4. Enter faster, harder, concentrated combat.
5. Learn and eventually master the boss.
6. Receive tiered progression and pursue its unique reward.
7. Return more powerful and more knowledgeable.

### Boss lifecycle [L]

1. Discovery and access.
2. Several learning attempts.
3. First reliable victories.
4. Efficient farming through mastery and power.
5. Long-term unique-item pursuit.

Boss-access difficulty, encounter difficulty, unique usefulness, and reward rarity must be balanced together. Exact retry rules, portal persistence, dungeon length, checkpoints, and death costs remain unanswered.

### Raids [L/P]

Raid-scale content means long, extremely difficult solo endgame dungeons requiring sustained execution, preparation, build strength, and accumulated game knowledge. It does not imply mandatory multiplayer.

Raids are structured in separate wings or sections [P], in the spirit of classic multi-wing raid dungeons. A wing is the unit of commitment—roughly one committed, dungeon-scale sitting—while the raid is the larger campaign around its wings. Where appropriate, wings may be attempted in more than one order, supporting targeted re-runs of a desired wing once the raid is mastered.

Raid progress persists across sessions and days until the raid is completed or the player chooses to reset it [P]. Persistence is player-controlled, never time-controlled: no daily or weekly lockouts, no scheduled resets, and resetting for a fresh farming run is free and immediate.

Skip and shortcut mechanics are test-gated [T]. The baseline must be deterministic—mastery-earned permanent shortcuts unlocked by defeating a wing or section boss, or reliably dropped "trophy" skip tokens from bosses already conquered—so that mastery, not luck, buys speed. Rare skip items may exist only as an optional luxury on top of that deterministic baseline, never as the sole path. Within-wing checkpoints for the longest wings are worth testing, but must not erode the committed-attempt value of a wing.

Exact raid duration, wing length, section boundaries, checkpoint implementation, skip-mechanic details, and rewards remain unresolved.

## 12. Gameplay loops, session structure, RNG pursuit, and committed attempts [L]

### 12.1 Ten-second ordinary-combat loop

An ordinary, level-appropriate open-world fight follows this flexible sequence:

> Encounter an enemy or group → initiate combat, or respond if an aggressive enemy attacks first → fight by attacking and using movement, positioning, dodging, enemy prioritization, and skills whenever the situation calls for them → repeat this combat exchange until the encounter is resolved → defeat the enemies → receive clear kill feedback and collect any loot or portal drops.

Ten seconds is only a representative window for repeated moment-to-moment play, not a required encounter duration. Some weaker enemies may be defeated directly; more demanding encounters may repeat the exchange many times and require more active use of movement, dodging, positioning, enemy prioritization, and skills. Boss-specific loops are outside this definition.

### 12.2 Ten-minute activity loop

Over roughly ten minutes, the player may pursue a specific self-chosen objective or roam and let opportunities emerge. The window may contain quest collection or advancement, relaxed but actively controlled enemy grinding, exploration, a targeted reward or portal hunt, an encounter, dungeon progress, or a natural mixture.

Travel, combat, discoveries, quests, and rewards should connect naturally. An unexpected quest, enemy, portal, item, landmark, or discovery may support the current objective or lead to another one. The player should normally make relevant progress through XP, loot, quest advancement, discovery, knowledge, access, practice, improved efficiency, or additional reward attempts, but ten minutes does not guarantee completion, an upgrade, or an entire dungeon clear.

### 12.3 One-hour progression loop

Over roughly one hour, the player may sustain one self-chosen pursuit or combine several shorter activities. The whole period could be spent grinding particular enemies for XP, equipment, portals, or another target; advancing quests; exploring a region; completing dungeon or boss attempts; or moving among these as opportunities arise.

Equipment, skills, inventory, route, or target may be adjusted when useful, but no fixed preparation ritual is required every hour. The player should normally make meaningful progress toward something chosen, while recognizing that an hour may complete one pursuit, connect several activities, or form only part of a much longer grind. It does not guarantee a permanent upgrade, completed dungeon, world change, or finished objective. Failed targeted rolls remain independent but still count as completed attempts in the wider pursuit.

### 12.4 Main long-term objective

The central long-term objective is to develop a chosen character from an unknown, inexperienced adventurer into a powerful, recognized, legendary endgame hero through levels, class development, equipment, exploration, quests, targeted grinding, increasingly difficult zones, dungeons, bosses, and raid-scale encounters.

Reaching endgame is a major transition rather than the end of the journey. Substantial endgame play continues through targeted farming, desired unique-item hunts, powerful and alternative builds, mastery of the hardest solo content, optional superbosses, collection, completion goals, and increasingly efficient play. A future story conclusion or final threat may provide direction and an important milestone, but it is not the game's ultimate endpoint. Endgame is core content, not optional cleanup after the "real game."

### 12.5 Session duration and attempt meaning

Wildshot Adventures does not prescribe one correct or normal session duration. A session is successful when the player can actively pursue a self-chosen goal that matters to them. A permanent upgrade is welcome but is not required for the session to be worthwhile.

Brief and extended sessions may both support useful play:

- quest completion or advancement;
- exploration and discovery;
- learning routes, enemies, mechanics, dungeons, or bosses;
- improving execution, knowledge, or clear efficiency;
- completing dungeon or boss attempts;
- making additional targeted loot rolls;
- receiving tiered gear, uniques, or other permanent progression when rolls succeed.

Repeated targeted attempts are meaningful across the broader pursuit, but the rolls remain independent. Additional kills or clears create more total opportunities to have succeeded; a failed attempt does not raise the probability of the next roll, accumulate an escalating modifier, or bank pity under the CORE-16 baseline.

Active single-player gameplay is pausable. An ordinary dungeon is normally one committed gameplay instance: pausing while remaining in the run is allowed, but leaving or abandoning ends that instance. The player cannot later resume the same partially cleared dungeon, and ordinary dungeons are not permanently completed room by room across separate entries.

## 13. World direction [L/P]

The world should be dense and worth inhabiting for a long time. Regions need multiple reasons to visit and revisit, such as:

- quests and lore;
- enemy and equipment targets;
- dungeon portal sources;
- named enemies and world bosses;
- secrets and landmarks;
- dangerous content seen before the player is ready;
- routes and efficiencies learned over time;
- later objectives that recontextualize earlier regions.

Heavy repetition is acceptable and desirable when it is deliberate, targetable, cumulative, and creates a pull toward the next frontier.

### World structure and travel foundation [L/P]

Wildshot Adventures uses a layered multi-map world consisting of many large, distinct outdoor zone maps rather than one technically seamless map. Each zone is a substantial, freely explorable space belonging to the same coherent world.

The player travels between neighbouring outdoor zones by physically finding and crossing their connecting roads, gates, mountain passes, tunnels, paths, or other entrances. Some connections are huge, obvious roads forming the world's main travel network, while others may be smaller, concealed, unusual, or discovered through exploration. Learning these routes and entrances is part of learning the world.

Houses, shops, caves, ruins, dungeons, raids, and similar locations may use separate interior maps. Larger locations can contain multiple connected maps or deeper floors, and leaving normally returns the player to the entrance used.

Map transitions and loading screens are acceptable, but travelling should feel like movement through an interconnected physical world rather than selection of disconnected levels from an overworld screen or menu.

As the player progresses, they can unlock a convenient auto-travel system for selected previously discovered destinations. Auto-travel supplements physical exploration rather than replacing it: the player must initially discover the world, and unknown locations, hidden connections, and undiscovered routes cannot simply be selected through auto-travel.

Exact zone sizes, route placement, secret connections, and broader progression requirements remain unresolved. Detailed auto-travel rules are established below.

### Repeated travel and selective auto-travel [L/P]

Wildshot Adventures compresses repeated travel through a selective auto-travel system that functions as teleportation. It complements physical exploration without replacing the need to learn the world.

Auto-travel is available only to selected unlocked destinations, such as cities, settlements, major hubs, and appropriate landmarks. Discovering a location does not automatically make it an auto-travel destination. Many caves, wilderness locations, secrets, and selected dungeons deliberately have no direct access. The player teleports to the nearest suitable destination and manually follows the roads, concealed paths, or special entrances they have learned.

Eligible destinations may have different permanent unlock requirements, including discovering and activating the location, paying an initial cost, completing a quest, repairing a route, or meeting another appropriate condition.

Auto-travel may begin from most safe outdoor locations. It cannot begin during combat, near immediate danger, or inside houses, caves, dungeons, raids, and other contained maps.

Teleportation has a visible three-to-five-second cast time. Moving, taking damage, or entering combat cancels the cast, preventing auto-travel from becoming an emergency escape.

Each successful teleport costs currency. Currency is charged only when the teleport completes; a canceled or interrupted cast costs nothing. The fee should make teleportation a modest decision without forcing unnecessary walking.

Once the cast completes, the player travels directly to a fixed safe arrival point. The route is not simulated, and no ambushes or travel interruptions occur during the teleport.

There is no separate free recall ability. Cities and hubs are ordinary auto-travel destinations using the same unlock rules, currency cost, and interruptible cast.

Mounts, permanent shortcuts, and learned routes may make manual travel outside the teleport network faster. Their detailed mechanics remain unresolved.

Exact eligible destinations, individual unlock requirements, prices, and whether costs vary by distance or destination remain unresolved for later world and economy planning.

### World authorship and controlled variation [L/P]

The world is handcrafted at its foundation, with controlled procedural variation used inside authored spaces. Zone geography, roads, entrances, settlements, landmarks, caves, secrets, major interiors, bosses, progression-critical content, and the defining identity of major dungeons and raids are authored.

Procedural systems may vary enemy groups, roaming encounters, rare spawns, events, resource locations, fishing and foraging opportunities, and other repeatable details within those authored spaces. Selected dungeons may eventually use curated room or encounter variations, but major dungeons and raids must retain authored identity, controlled mechanics, and learnable structure.

Procedural variation exists to keep revisiting and grinding familiar regions interesting, not merely to inflate world size. Randomness must not erase useful world knowledge, make targeted pursuits unreliable, constantly relocate essential destinations, or replace distinctive authored content with interchangeable filler.

Variation follows authored bounds [P]: the *where* is authored and learnable, while the *what* varies within a known pool. A fixed, authored location may host a small authored pool of possible bosses or encounters—for example, one arena where any of three or four bosses may appear—so the place stays learnable while the fight varies. Roaming rare enemies are not placed randomly; they patrol authored restrictions such as a specific zone and a route within it, keeping them huntable through route knowledge. When a pooled location matters to a targeted pursuit, key rewards such as portals should be shared across the pool, or the location reserved for variety rather than sole-source targets; roaming rares remain bonus encounters rather than sole sources.

The exact procedural systems, content pools, placement rules, reset schedules, dungeon applications, and balance between persistence and variation remain unresolved for their dedicated questions and prototypes.

### World gating and access [L/P]

Wildshot Adventures uses mostly soft world gating, supported by selected meaningful hard gates.

Outdoor zones are not level-locked. Players may physically travel into dangerous regions early, explore cautiously, encounter powerful enemies, learn routes, discover portal sources and entrances, and see challenges they are not yet ready to overcome. Enemy danger is the main natural readiness barrier and should create visible future goals.

Outdoor openness does not make every contained location immediately accessible. Sealed ruins, inner areas, special routes, and similar spaces may use meaningful hard gates while their surrounding outdoor zones remain explorable.

Dungeons, raids, and selected challenge instances use explicit minimum-level entry requirements. Their surrounding outdoor zones remain accessible regardless of level, and an attempted early entry must clearly communicate the required level. Meeting the minimum level only permits an attempt; equipment, build quality, preparation, player skill, and knowledge still determine whether the player is ready to succeed.

Selected content may additionally require a dropped portal, key, completed quest, boss victory, world event, environmental protection, discovered route, or another meaningful prerequisite. Multiple requirements may coexist only when each serves a clear purpose. They must not be stacked merely to extend playtime, and the total effort needed to begin and repeat an attempt should remain proportionate to the content.

All requirements must be clear before an access resource is spent. A portal, key, or similar item is never consumed when entry is denied. Permanent progression gates normally remain solved once completed, while explicitly repeatable access items such as dungeon portals may still be required for each new attempt.

Hard gates should be understandable and purposeful. The world should provide multiple viable frontiers where appropriate rather than forcing every player through one rigid universal sequence. Exact minimum levels, the activities that use them, and the placement and implementation of other gates remain unresolved for later progression and content planning.

### Enemy and region difficulty [L/P]

Wildshot Adventures uses stable, authored difficulty. Nothing automatically scales to match the player's level, equipment, statistics, or progression.

Each outdoor region has an intended difficulty range while still allowing easier outskirts, tougher inner areas, dangerous pockets, elites, rare enemies, and world bosses with their own fixed strength. Entering a late region early should feel genuinely dangerous, while returning to an early region later should let the player feel substantially stronger and defeat its ordinary enemies efficiently.

World bosses, outdoor enemies, and regions do not scale. Stronger later-game enemies should be distinct creatures, recognizable variants, or deliberately placed encounters rather than secretly scaled copies of existing enemies. Earlier regions remain worthwhile through quests, dungeon-portal sources, collections, fishing, foraging, events, secrets, rare spawns, and other targeted pursuits rather than by raising every ordinary enemy to the player's level.

Selected instanced dungeons may later receive optional higher-difficulty versions. These are separately chosen versions with their own fixed enemy strength, mechanics, entry requirements, and rewards. They do not adapt dynamically to whoever enters, and the original dungeon version remains unchanged.

This boundary does not prevent the later addition of entirely new and stronger world bosses. Each individual world-boss encounter still retains its authored difficulty rather than following the player.

Exact regional difficulty ranges, higher-difficulty dungeon-version names, eligibility, unlock conditions, mechanics, entry requirements, and rewards remain unresolved for later dungeon and progression planning.

### Optional world-filling and reward activities [L/P]

The four established design pillars remain Wildshot Adventures' only pillars. Non-combat activities are optional supporting systems intended to enrich the open world, provide relaxed alternative grinds, and create additional collection goals without competing with the main combat game.

**Foraging and fishing are optional supporting systems, not design pillars or major focuses.** They should make the vast open world feel richer, livelier, and more worth exploring while offering relaxed alternatives to combat.

- **Foraging** has its own progression level and a long-term collection grind centered on uncommon and rare flowers.
- **Fishing** has its own progression level and a corresponding rare-fish collection grind.
- Rewards from both systems should be primarily cosmetic and collection-oriented, so dedicated players can pursue them without making either system necessary for core progression.
- Regional flowers, fish, and suitable gathering locations should provide additional discoveries and reasons to explore or revisit parts of the world.
- Neither system should become a mandatory daily chore, a required combat-power grind, or a source of excessive material clutter.

**Crafting is a limited optional supporting system, not a broad profession or a parallel equipment economy.** Its intended structure is closer to buying or commissioning a known reward through an in-world crafting presentation: the player fulfills explicit costs or requirements and receives the selected, deterministic result.

- Crafting produces only non-combat rewards. It does not create, improve, or reroll combat equipment; grant combat statistics or power; or produce combat consumables or buffs.
- It may support high-dedication optional goals such as prestigious non-combat mounts, character or equipment skins, cosmetics, collection rewards, and other carefully selected non-combat reward types added later.
- Foraging and fishing may supply resources or fulfill requirements for crafting, allowing those optional gathering and collection grinds to lead toward known, deterministic rewards.
- The crafting fiction should make acquisition feel grounded in the world, while the underlying requirements remain understandable and targetable.
- It should avoid a sprawling material economy, recipe clutter, random-output crafting, mandatory upkeep, and routine crafting chores.
- The system should remain deliberately extensible within its non-combat boundary; the complete list of eligible non-combat reward types is not locked.

**Collectables should primarily be tracked, presented, and enjoyed through dedicated, polished interface menus rather than physical housing displays.** Fishing, foraging, trophies and major accomplishments, cosmetics and skins, mounts, and future collection categories should contribute to an organized long-term collection system with clear progress and satisfying completion feedback.

**Player housing is not currently planned.** It is not required for collection, storage, crafting, or progression and should not be added merely to provide somewhere to display rewards. This is not a permanent prohibition: housing may be reconsidered later only if a separate compelling purpose emerges.

**Player-managed settlement growth is not planned.** Settlements remain authored locations rather than player-built or managed systems. Selected settlements may undergo authored changes through quests, major victories, or world events. These changes support the world and narrative rather than forming a separate management activity.

**Pets are a purely cosmetic collection system, if included [P].** One small pet may follow the player as a companion and collection reward. Pets provide no combat or statistic benefit of any kind: they do not heal, regenerate, buff, attack, draw aggro, tank enemies, cast abilities, or function as AI party members. Dropping the earlier modest-passive-benefit concept keeps optional collection systems fully separated from combat power and removes an entire balance surface; pets are pure collection and appearance joy.

**Fishing and foraging are the only non-combat activities currently planned with their own progression levels.** Limited crafting is a deterministic reward system, not a leveled profession. No wider profession roster—such as mining, smithing, cooking, alchemy, or woodcutting—is currently planned. Another activity should be considered later only if it creates a genuinely distinct and valuable pursuit that fishing or foraging cannot already provide. The project prefers two strong non-combat activity systems over ten merely adequate ones.

Foraging and fishing interactions, progression curves, detailed collection-interface structure, locations, rarity structures, and reward sets remain unresolved. Crafting recipes, exact requirements, resource sources, interfaces, and eligible non-combat reward types also remain unresolved. Exact pet acquisition, collection structure, and presentation remain unresolved, as do the quests, victories, or world events that may produce authored settlement changes. These details belong to their dedicated later questions.

## 14. Knowledge as progression [L]

Endgame success should require more than reflexes or gear score. Players should gradually learn:

- useful stat relationships and build choices;
- enemy behavior and projectile patterns;
- portal associations and farming locations;
- item and boss sources;
- zone danger and route efficiency;
- dungeon structure and boss phases;
- preparation appropriate to specific content.

Essential knowledge should eventually be discoverable or recordable inside the game. Mystery is welcome; permanent external-wiki dependence for core progression is not.

## 15. Platform, input, and business model

### Platform [L]

- Lead platform: Windows PC through Steam.
- Steam Deck compatibility is desirable and supported where it survives the design, but it is contingent on the input rules below and may be reduced rather than weaken the game [P].
- Consoles may be considered later but do not drive initial scope.

### Input [L]

Mouse and keyboard defines the intended combat experience, precision ceiling, encounter complexity, and endgame scope.

Controller support is a secondary convenience for relaxed grinding, exploration, couch play, and possible Steam Deck use. It must adapt to the game; the game must not be weakened to support it. If controller support requires reducing projectile intensity, precision demands, skill design, or encounter scope, controller support should be reduced or dropped.

The intended worst case is explicitly acceptable: controller may end up suitable mainly for relaxed, extended grinding sessions while endgame content expects mouse and keyboard, and players should understand this split early. Open-world content remains designed for mouse and keyboard and merely happens to be playable on a controller; enemy and encounter design must never be adjusted toward stick precision.

### Business [L/P]

- Premium one-time purchase on Steam [L].
- No subscription, battle pass, pay-to-win purchases, recurring payments, or live-service retention pressure [L].
- A free itch.io release remains at the developer's discretion [P].
- Demo, Early Access, expansions, and account requirements are undecided.

## 16. Optional two-player co-op [P/T]

The game is designed and balanced as a complete single-player experience. Its technical architecture should preserve a credible path to optional two-player online co-op, but co-op is not promised until an early networked prototype succeeds.

Rules already established:

- Every class, quest, dungeon, boss, raid, unique item, and progression path remains available solo.
- Co-op is a way for two friends to share the existing adventure, not the foundation of encounter design.
- Four-player and mandatory group content are outside the current direction.
- Solo balance remains the baseline.
- Local/shared-screen co-op is a separate feature and is not implied.

Technical direction under test:

- avoid global assumptions that exactly one player exists;
- separate input from player simulation;
- use stable IDs and serializable state;
- host-authoritative enemies, projectiles, damage, loot, portals, dungeons, and world state;
- personal character saves and personal loot;
- early test of movement, aiming, projectiles, enemy authority, portal entry, dungeon instancing, disconnect/reconnect, and save safety.

Co-op should be cut if it materially harms combat quality, save reliability, project scope, or the solo game.

## 17. Primary references [L]

### Realm of the Mad God

Primary reference for independently aimed projectile combat, movement under pressure, portal hunting, dungeons, bosses, raids, tiered equipment, and authored unique-item pursuit.

Not inherited: permadeath as the normal rule, multiplayer dependence, zerging, trading-driven balance, live-service pressure, uncontrolled visual clutter, excessive wiki dependence, or excessive rebuilding after failure.

### Erenshor

Primary reference for the long-form single-player MMO journey: beginning with almost nothing, dense maps with many goals, heavy but worthwhile repetition, meaningful return visits, equipment hunting, knowledge-driven progression, and end content that requires broad system understanding.

Not inherited: SimPlayers as a core system, tab-target combat, mandatory party composition, waiting for named enemies, obscurity without an in-game learning path, statistics replacing execution, or unnecessary inventory clutter.

## 18. Major unresolved areas

The project has not yet locked:

- the numerical length and exact threshold of the first character’s journey to endgame;
- the detailed replay and endgame structure beyond the locked long-term objective;
- exact raid duration, wing lengths, section boundaries, checkpoint implementation, and skip-mechanic details (wing structure, player-controlled persistence, and the deterministic skip baseline are provisionally decided);
- tone, rating, and content boundaries;
- team, engine, budget, schedule, and production constraints;
- exact world-gate placement, regional difficulty ranges, higher-difficulty dungeon-version implementation, auto-travel destinations, unlock requirements, prices, cost scaling, manual-travel aids, and exact procedural-variation implementation;
- enemy-specific and boss-specific encounter loops; skill activation, ability-specific animation commitments, detailed hitbox and collision geometry, aim assistance, optional focus-target behaviour, exact weapon statistics and cadence ranges, final individual attack patterns, exceptional weapon mechanics, default autofire binding and HUD treatment, hit-feedback tuning, individual ability-item designs, and per-class ability-item pools;
- stat set, level curve, and equipment formulas;
- death, saves, dungeon failure, and recovery;
- quests, factions, hubs, and the exact authored changes that quests, victories, or world events may produce in settlements;
- detailed foraging and fishing interactions, progression, collections, locations, rarity structures, and rewards;
- exact pet acquisition, progression, passive benefits, balance, collection, and presentation;
- accessibility and readability implementation;
- vertical-slice scope and measurable continuation gates.

No planning document should silently treat these as decided.

## Appendix A. CORE interview integration index

The numbered sections in this GDD are document chapters, not CORE question numbers. For example, **“18. Major unresolved areas” is chapter 18; it does not mean the design interview stops at CORE-18.**

Current interview state:

- **CORE-01 through CORE-16:** recorded.
- **CORE-17 through CORE-20:** still open. CORE-18 has later constraints established by CORE-24, but its exact replay/endgame structure remains unresolved.
- **CORE-21 through CORE-34:** approved and integrated into this GDD.
- **CORE-35:** active and unanswered.

| CORE | Status | Where the approved decision is integrated |
|---|---|---|
| CORE-21 | [L] | Section 12.1 — ten-second ordinary-combat loop |
| CORE-22 | [L] | Section 12.2 — ten-minute activity loop |
| CORE-23 | [L] | Section 12.3 — one-hour progression loop |
| CORE-24 | [L] | Sections 5.2 and 12.4 — long-term objective and substantial endgame |
| CORE-25 | [L/P] | Section 13 — optional world-filling and reward activities |
| CORE-26 | [L/P] | Section 13 — world structure and travel foundation |
| CORE-27 | [L/P] | Section 13 — world authorship and controlled variation |
| CORE-28 | [L/P] | Section 13 — world gating and access |
| CORE-29 | [L/P] | Section 13 — enemy and region difficulty |
| CORE-30 | [L/P] | Section 13 — repeated travel and selective auto-travel |
| CORE-31 | [L] | Section 8 — combat format |
| CORE-32 | [L/P] | Section 8 — primary attack |
| CORE-33 | [L/P] | Section 8 — universal movement and defensive actions |
| CORE-34 | [L/P] | Sections 8 and 9 — active ability, ability items, and skill-tree boundary |

The Decision Register and Living Design Questionnaire retain the full per-question records. This GDD integrates approved decisions by design topic instead of duplicating the entire interview transcript.
