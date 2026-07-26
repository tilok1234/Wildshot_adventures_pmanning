# Wildshot Adventures — Systems Map and Dependencies

**Purpose:** Show which systems own which decisions and in what order they should be resolved.

**Current design coverage:** Part I complete — CORE-01 through CORE-55 all answered (2026-07-26); CORE-14 remains prototype-gated. Detailed 2026-07-26 decisions live in the Decision Register and GDD; this map's matrix reflects them.

## 1. Critical dependency chain

```text
Player promise, audience, constraints
              ↓
Movement + aiming + primary projectile combat
              ↓
Enemy attacks + telegraphs + combat readability
              ↓
Class resources + skills + weapon patterns
              ↓
Levels + stats + equipment scaling
              ↓
Loot sources + portal access + dungeon rewards
              ↓
World structure + quests + hubs + travel
              ↓
Bosses + raids + endgame progression
              ↓
Supporting systems, content production, polish
```

A later system should not be used to hide a failure in an earlier one. Loot must not disguise weak combat; a large world must not disguise weak encounter design.

## 2. Responsibility matrix

| System | Owns | Must not own |
|---|---|---|
| Class | Base statistics and growth, exclusive weapon/ability-item/gear families, the behaviour-changing passive skill tree | Granting active abilities through the tree; routine replacement of the weapon's pattern |
| Weapon | Primary attack damage, attack speed, range, projectile pattern, preferred positioning | The entire class identity |
| Ability item | The single equipped active ability and its behaviour; role choice (mobility/defense/burst/utility) | Being required by any encounter; existing outside its class's pool |
| Primary-attack input | Tap once, hold at weapon cadence, or toggle the same held-fire state; always follow current free aim | Target selection, automatic tracking, passive combat, or a separate attack resource |
| Armor and ring | RPG statistics with give-and-take archetypes and situational tradeoffs | Automatic universal best-in-slot progression; a single universally correct ring |
| Level | Class base-stat growth (incl. HP/mana), skill points, access pacing via instance and equipment level gates | Making execution irrelevant; scaling any content |
| Player knowledge | Efficient routes, loot/portal sources, stats, encounter understanding | Essential facts available only through external wikis |
| Tiered loot | Reliable vertical progression | Authored unique playstyles |
| Unique loot | Situational build identity and aspirational chase | Universally superior power in every situation |
| Open world | Exploration, relaxed grinding, quests, portal hunting, discovery | Constant maximum-intensity combat |
| Dungeon | Concentrated combat, boss access, targetable rewards | Waiting or schedule-based access |
| Boss | Pattern mastery, milestone victory, authored loot source | Unreadable damage or arbitrary failure |
| Raid | Long-form endgame mastery and gearing journey | Mandatory multiplayer |
| Quest | Direction, teaching, landmark deterministic rewards, faction standing, story beats; the gapped main quest | Empty quotas as the main content model; daily/repeatable structure |
| Faction | Reputation pursuits levelled through distinct verbs (quest sets, enemy hunts); vendor/QoL/cosmetic unlocks; world recognition | Mandatory core-progression rewards |
| World topology | Large outdoor zone maps, physical connections, separate interiors, coherent geography | A menu of disconnected levels |
| Procedural variation | Refresh repeatable details inside authored spaces | Moving essential destinations, erasing world knowledge, or replacing authored identity |
| Auto-travel | Paid teleportation to selected unlocked destinations from safe outdoor situations | Universal destination coverage, free recall, emergency escape, or simulated ambush travel |
| Fishing / foraging | Optional leveled collection grinds and world-enrichment discoveries | Mandatory combat power, daily chores, or a broad profession economy |
| Limited crafting | Deterministic exchange for known non-combat rewards | Combat equipment, combat statistics, buffs, consumables, random output, or a leveled profession |
| Pet | One small optional cosmetic collection follower | Any combat or statistic benefit; attacking, drawing aggro, tanking, casting, or becoming an AI party member |
| Controller | Optional comfort and portability | Restricting mouse/keyboard combat scope |
| Co-op | Optional shared adventure | Defining solo balance or gating content |
| Session goal / attempt | Player-chosen objective, attempt completion, pause/abandon boundaries, run telemetry | Guaranteeing a permanent upgrade on a fixed timer |

## 3. Core reward architecture

```text
Normal enemy / elite / chest
        ├─ experience
        ├─ currency/materials (exact systems unresolved)
        ├─ tiered equipment appropriate to source
        └─ specific dungeon portal when associated

Dungeon / world boss / raid encounter
        ├─ stronger tiered equipment baseline
        ├─ progression rewards
        ├─ cosmetic and collection drops (dry-streak breadth, straight to the collection menu)
        └─ authored unique-item chance (duplicates sell for meaningful gold, never power)

Selected major quest [P]
        └─ guaranteed authored unique or other milestone reward
```

The exact number of reward layers is not yet locked. The principle is that a failed unique roll should not automatically make the entire activity worthless.

### CORE-16 session and attempt rules [L]

- Session value is measured against the player's self-chosen goal, not a prescribed duration or guaranteed upgrade timer.
- Learning, exploration, execution improvement, quest advancement, completed runs, and relevant loot attempts can all count as meaningful progress.
- Targeted loot rolls are independent under the current baseline. More attempts create more total opportunities, but failures do not improve the next roll or bank pity.
- Active single-player play is pausable.
- An ordinary dungeon is one committed instance: leaving or abandoning ends it, and the same partial clear is not resumed later.
- Raid commitment, wings, checkpoints, and continuation rules are deferred.

### CORE-21 through CORE-24 loop hierarchy [L]

- **Moment-to-moment:** Ordinary, level-appropriate open-world combat moves from encounter or enemy aggression into situation-dependent attacking, movement, positioning, dodging, enemy prioritization, and skill use; the exchange repeats as needed before defeat, clear kill feedback, and loot or portal collection. Ten seconds is representative, not a required fight length, and boss-specific loops remain separate.
- **Roughly ten minutes:** The player may pursue one self-chosen objective or roam into opportunities through active low-attention grinding, quests, exploration, targeted hunting, encounters, or dungeon play. Activities can mix naturally. Relevant progress is expected without guaranteeing completion, an upgrade, or a full dungeon clear.
- **Roughly one hour:** The player may sustain one pursuit or connect several shorter activities, adapting equipment, skills, inventory, route, or target when useful. Meaningful chosen progress is expected, but the hour may be only part of a longer grind; failed targeted rolls remain independent completed attempts.
- **Long term:** The chosen character rises from an unknown adventurer into a powerful, recognized, legendary endgame hero. Reaching endgame begins substantial targeted-farming, unique-hunting, build, mastery, optional-superboss, collection, completion, and efficiency pursuits. A story ending may be a milestone, but it does not replace endgame as a core continuation.

### CORE-25 supporting-system boundary [L/P]

- Fishing and foraging are the only currently planned non-combat activities with their own progression levels. Their main rewards are collections, cosmetics, and world-enrichment value.
- Limited crafting is a deterministic requirement-to-known-reward system for non-combat outcomes. It is not a profession level or equipment economy.
- Collections primarily use polished dedicated interfaces.
- Housing and player-managed settlement growth are not currently planned. Selected authored settlement changes may follow quests, victories, or events.
- One small optional pet may provide a modest passive benefit but never participates as a combat actor.
- New professions or supporting activities require a distinct purpose that the accepted systems cannot already serve.

### CORE-26 through CORE-30 world and travel boundary [L/P]

- The world is a coherent network of many large outdoor zone maps connected through physical routes. Interiors use separate maps when appropriate.
- Geography, routes, settlements, landmarks, secrets, major interiors, bosses, and progression-critical content are handcrafted.
- Controlled procedural variation may refresh enemy groups, events, rare spawns, resources, fishing, foraging, and other repeatable details without making targetable pursuits unreliable.
- Outdoor zones rely on soft danger gating rather than level locks. Dungeons, raids, and selected instances use explicit minimum levels and may have other clear, meaningful prerequisites.
- Regions, outdoor enemies, and world bosses retain fixed authored difficulty. Only selected instanced dungeons may later receive separate fixed higher-difficulty versions.
- Selected discovered destinations support paid teleportation from safe outdoor situations after an interruptible three-to-five-second cast. Many special destinations and final routes remain manual, and there is no separate free recall.

### CORE-31 through CORE-32 combat baseline [L/P]

- Combat is real-time, top-down, seamless in the current map, freely aimed, and resolved through visible spatial contact.
- No selected or locked target is required to attack, use skills, deal damage, or kill. Hidden accuracy/evasion rolls cannot reject a visible hit.
- Tap LMB fires once; holding fires at weapon cadence; a remappable toggle reproduces held fire with a clear HUD state. All modes follow current aim and may fire into empty space.
- Ordinary primary attacks use no mana, stamina, ammunition, durability, or reload resource.
- Movement, aiming, and ordinary firing remain independent and predictable. Explicit special-weapon tradeoffs are authored exceptions.
- Player primary-attack patterns are deterministic and weapon-defined. Terrain collision, line of fire, angles, range, and readable impact feedback support weapon identity and no-reward enjoyment.

## 4. Portal system interaction map

```text
World knowledge
   ↓ identifies
Specific portal-dropping enemy
   ↓ hunted in
Known region / route
   ↓ may drop
Specific dungeon portal
   ↓ enters
Committed ordinary-dungeon instance
   ↓ pausable while active; abandon/leave ends the instance
Dungeon encounter sequence
   ↓ culminates in
Boss mastery + tiered loot + unique chase
   ↓ improves
Character power and access to later frontiers
```

Balance these together:

- enemy availability and concentration;
- travel time;
- portal chance;
- portal persistence and party rules;
- dungeon length;
- death/retry cost;
- pause, abandonment, and reset boundaries;
- boss difficulty;
- unique usefulness and rarity.

## 5. Progression relationships

Character power should be a product of several dimensions:

```text
Effective power = character level
                + class development
                + equipment statistics
                + weapon pattern suitability
                + player execution
                + player knowledge
```

This is conceptual, not a numerical formula. The design goal is that no single term completely replaces the others in relevant endgame content.

## 6. Solo/co-op architecture boundary [P/T]

The solo game is authoritative from a design perspective. Technical systems should avoid assuming exactly one player so that a two-player test remains possible.

Potential host-authoritative ownership:

- enemies and AI;
- projectiles and hit validation;
- damage and status effects;
- portals and dungeon instances;
- world and quest state;
- item drops.

Potential personal ownership:

- character save;
- class, level, skills, equipment, inventory;
- personal loot;
- player settings.

These rules are not release commitments until the network prototype passes.

## 7. Decisions that block downstream work

Resolved on 2026-07-26: production constraints and engine [P] (CORE-20); the player kit — movement-only dodging, one item-granted active, focus targeting cut (CORE-33–35); the readability laws and pack grammar at the rule level (CORE-44/51); the stat set and scaling philosophy (CORE-40); the death/retry baseline (CORE-43); quest/hub/faction purpose (CORE-46/47); vertical-slice scope and both measurable gates (CORE-52/55); raid wing structure and persistence (CORE-16 revision).

Still blocking before or during full production:

1. Measured production velocity (only the lab and slice can provide it — Gate 2).
2. Save architecture, exact death fees, and hardcore save handling.
3. Exact zone sizes, content-density numbers, procedural content pools, access-gate placement, travel prices/unlocks, and higher-difficulty dungeon-version implementation.
4. Numeric combat tuning: weapon stats, ability designs, growth curves, caps, drop rates against the CORE-49 targets.
5. Raid wing lengths, checkpoint implementation, and skip-mechanic prototypes.
6. Narrative specifics within the decided tone boundaries.
