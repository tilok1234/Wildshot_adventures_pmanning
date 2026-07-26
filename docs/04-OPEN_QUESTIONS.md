# Wildshot Adventures — Open Questions

**Snapshot:** 2026-07-26 — **Part I complete: CORE-01 through CORE-55 all answered.**  
**Purpose:** List what remains genuinely open, so a new session neither reopens settled matters nor silently treats open ones as decided.

## Interview position

- All 55 Part I core questions are answered (see `08-DECISION_REGISTER.md` for status per question; `notes/INTERVIEW_STATE.md` for the live position).
- CORE-14 (optional two-player co-op) remains provisional and prototype-gated on the Phase E network test.
- The interview proceeds to Part II modules (combat and controls first), alongside building the Phase A combat laboratory.

## Test-gated decisions awaiting prototypes [T]

- **Phase A lab gate:** no-reward combat enjoyment, dependable feel, explainable deaths, lowest-speed dodgeability, outside-tester judgment (CORE-53/55 Gate 1).
- **CORE-33 movement-only dodging falsifier (added 2026-07-27):** honest lowest-speed dodgeability at intended intensity, and endgame density achievable as relentless-but-fair within walking-only constraints; failure reopens CORE-33 (fallback order: class mobility tools as soft-universal, one limited universal option, lower intensity ceiling).
- **No-pity baseline falsifier (CORE-16/42, added 2026-07-27):** Phase D dry-streak feel test at simulated p95 unluck — if the pursuit reads as disrespectful despite reward breadth and attempt visibility, the mitigation menu reopens (bounded bad-luck protection stays distinct from escalating odds).
- **Committed-instance falsifier (CORE-16, added 2026-07-27):** Phase D interruption/abandon tests — the rule must read as a known commitment rather than lost progress.
- **Grind cadence targets (CORE-49):** dungeon 10–20 min; portal at known source 5–20 min; mastered loop 2–3×/hour; felt upgrade most leveling hours; unique expected in ~20–40 attempts; p95 unlucky ≤ ~2–3× expected — all validated by the Phase D percentile simulation.
- **Slice gate questions (CORE-52/55 Gate 2):** voluntary post-completion farming; dry-streak feel with attempt counter; level-gap-as-invitation; explainable-death rate at density; build distinction; production-velocity extrapolation.
- **Raid skip mechanics:** deterministic baseline (mastery shortcuts vs trophy tokens) to prototype; escalating within-wing respawn fee.
- **Main-quest level-gap sizes** and quest-density feel (slice zone is the density test).
- **Portal drop rates** (~20–30% normal / 50–100% world boss remain test targets).
- **Co-op (CORE-14):** the Phase E two-player greybox gate.

## Deferred implementation details by area

### Combat and player kit
- Exact skill activation, ability-specific animation commitments, hitbox/collision geometry, aim assistance details.
- Weapon statistics, cadence ranges, final individual attack patterns, exceptional weapon mechanics.
- Per-class ability-item pools, individual ability designs, mana costs, cooldown/charge models.
- Default autofire binding and HUD treatment; collision and hit-feedback tuning.
- Enemy-specific and boss-specific encounter loops; per-region role rosters; pack composition tables; aggro ranges.
- The capstone-empowers-equipped-item concept [P design space].

### Stats, levels, and equipment
- Exact stat values, per-level growth curves, caps (especially movement speed), the regeneration-stat decision, equipment formulas.
- Level cap value; equipment level-requirement thresholds; tree size and point totals.
- Tier counts and step sizes; per-frame balance; per-slot stat budgets; whether rings are class-bound or shared.
- Class base-stat spreads; respec rules; item preview/interface implementation.

### Loot and economy
- Exact drop rates; gold values; shop inventories and pricing; class filtering; upgrade retention.
- Cosmetic dupe-milestone design [LATER]; currency/material vocabulary beyond gold.

### Death, saves, and hardcore
- Exact death-fee percentages and minimum fee; escalating raid-fee curves; respawn presentation.
- Save architecture; hardcore anti-save-scum handling; dungeon reset/save boundaries; portal persistence and expiration.

### World, travel, and content
- Zone sizes and count; route placement; secret connections; regional difficulty bands.
- Procedural content pools, placement rules, reset schedules; boss-pool assignments.
- Auto-travel destinations, unlock requirements, prices, cost scaling; mount and shortcut mechanics; remote turn-in/storage (undecided by CORE-30).
- Higher-difficulty dungeon-version names, eligibility, mechanics, rewards.
- Hub count and placement; service rosters; stash size/interface; the possible narrative capital [U].
- Milestone-dungeon selection; raid duration, wing lengths, section boundaries, checkpoint implementation.

### Quests, factions, and narrative
- Faction identities and count; per-faction leveling verbs; faction-set designs; reward tables.
- Quest density numbers; individual quest designs; main-quest structure details.
- Narrative specifics: story, characters, world lore, the possible story conclusion (tone/boundaries ARE decided — CORE-19).
- Exact authored settlement changes; recognition beats and NPC behaviour tiers.

### Supporting systems
- Fishing/foraging mechanics, curves, locations, rarity, rewards; crafting recipes, requirements, sources, interfaces, eligible reward types.
- Collection-menu categories, metadata, previews, completion presentation.
- Pet acquisition, collection structure, presentation (cosmetic-only is decided).

### Accessibility, readability, and audio-visual
- Exact option lists, defaults, slider ranges; colorblind palettes and the hostile shape language; visual language, effect budgets, audio design; readability review process implementation.

### Production
- Post-launch content cadence; Early Access/demo strategy; Steam Deck viability outcome; controller final scope; measured velocity (the great remaining unknown — resolved only by building).

## Settled — do not reopen casually

Everything in `08-DECISION_REGISTER.md` rows CORE-01 through CORE-55, including (highlights): three permanent classes with exclusive item families; weapon-owned patterns; movement-only dodging with no universal defensive action (Phase A/B falsifier recorded 2026-07-27); one equipped-item active ability with a behaviour-changing passive tree; focus targeting cut; four-slot loadout and the lean stat set with its exclusion list; no pity (Phase D feel-test falsifier recorded 2026-07-27), dupes-to-gold, no guarantees beyond quest uniques; committed dungeon instances where death ends the run (Phase D falsifier recorded 2026-07-27); raid wings with player-controlled persistence and full boss resets; optional hardcore mode; the fractal intensity ladder and honest-HP rule; the eight readability laws; the pack role grammar; quests speaking the game's language with a gapped main quest and faction sets; several hubs with per-character stash; no automation; no global difficulty setting; no M+K aim assist; colorful-heroic-with-bite tone and clean-leaning rating; solo AI-orchestrated production in Godot [P] with no deadline; the Archer slice; the top-five risk ranking; and both continuation gates.
