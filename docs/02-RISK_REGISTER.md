# Wildshot Adventures — Risk Register

**Snapshot:** 2026-07-26; integrated through CORE-55 (Part I complete).  
**Status:** Early pre-production. Ratings are qualitative until production constraints are known.

| Risk | Likelihood | Impact | Early warning | Mitigation / gate |
|---|---|---|---|---|
| Combat is not enjoyable without rewards | Medium | Critical | Testers stop engaging when loot/XP are removed | No-reward combat lab before world/content production |
| Projectile intensity becomes unreadable | High | Critical | Testers cannot identify damage sources or safe spaces | Visual hierarchy, hitbox debug, density budgets, readability playtests |
| Content scope becomes too large for the team | High | Critical | Regions/classes/items expand before core loop works | Resolve production constraints; vertical slice first; one class before three |
| Portal access, dungeon length, boss difficulty, and rarity stack into excessive friction | High | High | More time spent regaining access than learning/fighting | Treat all four as one friction budget; measure attempt cadence and percentile acquisition time |
| Heavy grind becomes directionless or unrewarding | Medium | High | Players cannot name the self-chosen goal, learning, completed attempts, or other value gained in a session | Targetable sources, clear goals, attempt visibility, tiered baseline rewards, and visible long-term pursuits |
| Unique weapons become mandatory best-in-slot | High | High | One item dominates every scenario and build | Situational tradeoffs, matchup testing, no universal pattern multipliers |
| Broad weapon-pattern experimentation becomes unreadable or unbalanceable | High | High | Prototype weapons differ through novelty but create unclear shots, proc explosions, or impossible comparison | Prototype broadly but ship narrowly; require deterministic patterns, readable identity, role/tradeoff tests, projectile/proc budgets, and duplicate-purpose cuts |
| Stats or gear trivialize execution | Medium | High | Players ignore boss mechanics after modest gearing | Keep pattern knowledge and positioning relevant in current-tier/endgame content |
| Player skill overwhelms RPG progression | Medium | High | Gear upgrades feel cosmetic; progression lacks payoff | Preserve visible power gains and access advantages without hidden miss rules |
| Knowledge progression turns into external-wiki dependence | High | Medium/High | Players cannot locate required sources in-game | Discovery journal, loot/portal records, clear quest clues, player notes/markers |
| Controlled procedural variation erases useful world knowledge | Medium/High | High | Essential routes, sources, or encounters move so often that learned targeting becomes unreliable | Keep geography and progression-critical content authored; constrain variation to declared pools inside authored spaces; test persistence and source reliability |
| Fixed authored difficulty makes early regions feel disposable | Medium | Medium/High | Players have no reason to revisit once ordinary enemies become easy | Preserve portal sources, quests, collections, fishing/foraging, secrets, rare spawns, events, and deliberate higher-level pockets without scaling ordinary enemies |
| Higher-difficulty dungeon versions blur the no-scaling rule | Medium | Medium/High | Players cannot tell whether content is a separate fixed version or secretly adapting to them | Give each version an explicit name, entry choice, fixed rules, reward table, and difficulty; keep the original version unchanged |
| Auto-travel erases route knowledge or becomes punitive friction | Medium/High | High | Every activity becomes a teleport menu, or fees/cast time force tedious walking | Curate destinations; preserve manual final routes; test prices and destination spacing; keep the three-to-five-second cast interruptible and charge only on success |
| Access requirements become an opaque stack of gates | Medium/High | High | Players reach an entrance with a portal/key but are denied for an undisclosed reason | Communicate all requirements before resource use; keep each requirement purposeful; never consume access resources on denied entry |
| Supporting activities dilute the combat game or become mandatory chores | Medium/High | High | Fishing, foraging, crafting, or pets become required for combat power or consume disproportionate production | Keep them optional and bounded; non-combat crafting only; primarily cosmetic/collection rewards; no daily structure; prototype two strong gathering systems before expanding |
| Three classes multiply content and balance workload | High | High | Every weapon, quest reward, and unique requires three variants | Prove one class deeply; define shared frameworks; selectively use class-filtered rewards |
| Optional co-op causes architecture, save, and QA expansion | High | Critical | Desyncs, save corruption, duplicated encounter logic | Early network gate; host authority; personal saves/loot; cut co-op if gate fails |
| Controller support pressures encounter simplification | Medium | High | Boss patterns are reduced to fit stick precision | Mouse/keyboard remains design authority; controller can be limited or dropped |
| Autofire is mistaken for auto-combat or creates unclear input state | Medium | Medium/High | Players forget it is active, think the game is choosing targets, or fire unintentionally | Make it a visible remappable held-fire toggle; never auto-select, track, or aim; test state feedback and pause/menu transitions |
| Terrain collision feels inconsistent with visible geometry | Medium/High | High | Shots snag on corners, pass through walls, or produce unexplained misses | Align collision with visible shapes; provide hitbox debug; test corners at multiple projectile sizes/speeds; reserve obstacle exceptions for clearly identified weapons |
| High-rate hit feedback becomes exhausting or hides threats | High | High | Damage numbers, flashes, shake, sound, or hit-stop obscure bullets and movement | Use layered feedback budgets; reduce/disable damage numbers; avoid routine screen shake, movement disruption, and global hit-stop; stress-test dense encounters |
| Long solo raids become exhausting rather than satisfying | Medium | High | Attrition or repetition dominates learning | Later test checkpoints, shortcuts, section lengths, recovery, and progression within raids |
| Failure penalties make players avoid experimentation | Medium | High | Players stop attempting bosses or trying builds | No character deletion; prototype recoverable, bounded penalties and fast retry loops |
| Equipment/item systems create inventory clutter | High | Medium | Sorting and conversion dominate sessions | Small currency/material vocabulary, personal loot rules, salvage/filter tools |
| Independent RNG is perceived as fake progress or dishonest odds | Medium/High | High | Players believe failures secretly build pity, or conclude attempts are meaningless without a drop | Communicate independent odds honestly; track sources and attempts; use mastery, baseline loot, and self-chosen goals without implying the next roll improved |
| Committed ordinary-dungeon instances conflict with real-life interruptions | Medium | High | Players abandon runs because they cannot safely pause, or misunderstand re-entry/reset rules | Reliable single-player pause; explicit abandon warning; clear fresh-instance behavior; later test reasonable dungeon lengths |
| Save integrity and character persistence fail | Low/Medium | Critical | Lost/corrupted progression, especially with co-op | Stable IDs, versioned saves, backups, migration tests, disconnect tests |
| Market identity becomes "RotMG clone" or "single-player MMO" without a clear hook | Medium | Medium/High | Testers describe only the references | Preserve distinct world, classes, quests, loot philosophy, and zero-to-hero structure |

## Top five risks (CORE-54, 2026-07-26)

Ranked from the full inventory above, each with test / mitigation / cut:

1. **Combat not fun without rewards** — Phase A lab gate / iterate feel first / pivot or stop if the lab fails repeatedly.
2. **Production feasibility unmeasured (CORE-20 open)** — answer CORE-20 + measure lab/slice velocity / one-class prove-then-multiply / planned scope-reduction order before touching the core loop.
3. **Friction stacking under no-pity RNG** — Phase D percentile simulation vs CORE-49 targets / friction budget + p95 guardrail + reward breadth / raise rates or shorten access, never add pity.
4. **Content multiplication (3 classes × exclusive items × dense quests)** — slice velocity extrapolation / shared frameworks, one class first / fewer frames and lower density before cutting classes.
5. **Endgame intensity outruns readability** — density stress-tests under the eight readability laws with outside testers / effect budgets + telegraph hierarchy + explainable-death review / cap density.

Named market runner-up: "RotMG clone / single-player MMO without a hook" perception — mitigated by the distinct pitch; tested by how outside slice testers describe the game unprompted. Tester source: the roadmap's tester and market pipeline (added 2026-07-27).

## Production feasibility status (updated 2026-07-26)

CORE-20 is now answered: solo developer, AI-orchestrated production, Godot [P], full-time capacity (PROD-01, 2026-07-27: 72 h/week scheduled, 40 h/week reliable planning floor), no deadline with the CORE-55 gates as the discipline mechanism, and a custom tileset + sprite-generation pipeline substantially de-risking art. Feasibility moves from **unmeasured** to **bounded**: the remaining unknown is real velocity, measured through the Phase A lab and the vertical slice per Gate 2.
