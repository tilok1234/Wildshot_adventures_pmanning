# Wildshot Adventures — Handoff for a New Chat, Account, or Work Session

**Handoff date:** 2026-07-26 (evening — supersedes all earlier handoffs); amended 2026-07-27 with maintenance commits (see notes/sessions/2026-07-27.md)  
**Project stage:** Guided concept definition / early pre-production  
**Interview position:** **Part I is COMPLETE — CORE-01 through CORE-55 are all answered.** CORE-14 remains provisional/prototype-gated (co-op depends on the Phase E network test).

## The single most important instruction

**This git repository is the source of truth.** Do not rely on chat memory, ZIP uploads, or summaries. Read `notes/INTERVIEW_STATE.md` first — it always holds the live position and the note-taking protocol. After every approved decision: update the questionnaire, decision register, GDD, and interview state, then **commit and push before moving on**. One approved answer = one commit. This protocol exists because notes were repeatedly lost before the repo existed; do not regress to "I'll write it up later."

If the new session cannot access the repository directly, ask the designer to grant repo access or provide a fresh clone/ZIP of the repo — but treat any ZIP as a transfer convenience, never the working source of truth, and get changes back into git as soon as possible.

## Read first, in this order

1. `notes/INTERVIEW_STATE.md` — live position, protocol, and per-question decision summaries from 2026-07-26.
2. `docs/08-DECISION_REGISTER.md` — the fastest complete picture of what is decided.
3. `docs/01-GAME_DESIGN_DOCUMENT.md` — the readable integrated design.
4. `docs/10-LIVING_DESIGN_QUESTIONNAIRE.md` — authoritative per-question record, when exact wording matters.
5. `docs/07-PROTOTYPE_SPEC.md` — the Phase A combat lab (the next build milestone) and vertical-slice scope.
6. `notes/sessions/` — dated working notes, including the full 2026-07-26 session log.

## What was decided on 2026-07-26 (one-screen version)

**Combat core:** Dodging is purely movement-based — no universal dash/roll/block/i-frames (CORE-33). Each character has exactly ONE active ability, granted by an equipped ability item from a class-exclusive pool; the skill tree grants no actives and its nodes must change behaviour, not just numbers (CORE-34). Focus targeting is cut entirely (CORE-35). Intensity climbs via density/speed/pattern complexity, never HP sponging, and the ladder repeats inside every zone at its authored band (CORE-36). Eight readability laws govern all art and encounters (CORE-51). Packs combine 1–2 role-grammar pressures, pulling is a learnable skill, and compositions showcase weapon frames (CORE-44).

**Character & items:** Class = base stats + tree + exclusive weapon/ability/gear families; four-slot loadout (weapon / ability item / armor / ring); armor uses give-and-take archetypes; no universally-correct ring allowed (CORE-37). Lean stat set: HP, mana, damage, attack speed, range, armor, movement speed (+regen candidates); crit/life-steal/resistances/accuracy/evasion intentionally excluded; uniques may break rules (CORE-40). Equipment IS the build system; tiers stay familiar-but-stronger; frames are side-grades; tier steps are chunky; item behaviour is readable before farming (CORE-41).

**Progression:** Levels grant class base stats (incl. HP/mana) + skill points; equipment has level requirements; the tree is points-spent-deep; a hard cap marks the endgame transition; provisional faction-reputation system (CORE-39). First journey targets ~40–80 focused hours to cap + main quest (CORE-17). Endgame is an open-ended collectathon, no endgame-only systems, alts modest (CORE-18).

**Loot & death:** No pity ever; dry streaks mitigated by reward breadth (cosmetic/collection boss drops) and cheap attempt cadence; dupes sell for meaningful gold, never power; no guarantees beyond quest uniques; faction vendors sell catch-up gear (CORE-42 + refinements). Grind targets: dungeon 10–20 min, portal 5–20 min, mastered loop 2–3×/hr, unique expected in ~20–40 attempts, p95 unlucky ≤ 2–3× expected [all T]; attempts tracked and displayed; every hunt advances ≥2 tracks (CORE-49). Death: nearest-city respawn + percent-of-gold fee (never cheaper than teleporting); dungeon death ends the instance, portal spent; raids give paid respawns at wing start with full boss resets and wing progress never lost; optional per-character hardcore permadeath mode (CORE-43). Raids use wings with player-controlled persistence, no time lockouts; deterministic skip baseline (refinement batch).

**World & content:** Quests = direction + teaching + landmark rewards; main quest 1→cap with deliberate level gaps; MMO-dense quest world; faction quest sets, different factions level through different verbs (CORE-46). Several major hubs (not per-zone); per-character stash only; escalating hub recognition (CORE-47). Crafting/gathering per CORE-25; NO automation, all active play (CORE-48). Variation bounds: authored *where*, pooled *what* — fixed arenas with boss pools, roaming rares on authored routes (refinement). Tone: colorful heroic fantasy with bite; clean-leaning E10+/T as a preference; no casino aesthetics on loot (CORE-19). Pets cosmetic-only. Steam Deck contingent, controller = relaxed-grinding worst case.

**Production (CORE-20):** Solo developer, expert at orchestrating AI; production is AI-orchestrated across code/art/content. Engine most likely **Godot** [P]. Abundant AI access; no contractor budget. **Full-time (PROD-01, 2026-07-27): 72 h/week scheduled, 40 h/week reliable planning floor** — plans divide by the floor. **No deadline** — the CORE-55 gates, not dates, are the discipline. The asset pipeline is **verified shipping** (showcase packet reviewed 2026-07-27): **TileForge** — four complete theme packages (forest/autumn/dusk/winter; 31,431 tiles × 80 families each) with Godot importers, a pixel-match acceptance test, and dungeon-room/cave/corrupt-zone interior scenes; **Actor Forge v2.3** — deterministic 32×32 four-facing 23-frame actor sheets, 12 actors × 4 themes, first quadruped landed, sprites still WIP. One gap, designer-committed as the pre-lab task: the **combat-effects vocabulary** (projectiles, telegraphs, hazard markers, hit/cast effects) authored against the eight laws. Generators must encode the readability laws; tools accelerate authoring without weakening the handcrafted-world rule.

**Slice & gates:** Vertical slice = Archer, ~cap 10, 4 frames × ~3 tiers, 4 ability items, 2 armor archetypes, one zone + hub, 8–10 enemy types, full portal→dungeon→boss→unique chain, main-quest slice with one level gap, 10–15 side quests, one faction set, ~3–5 h + repeatable farm, one authored secret (CORE-52). First milestone = Phase A no-reward combat lab, judged by outside testers, patterns dodgeable at lowest movement speed (CORE-53). Top five risks ranked with test/mitigation/cut (CORE-54). Two formal continuation gates recorded (CORE-55).

## Next steps (designer to choose)

1. ~~**Answer the numbers**~~ ✅ **ALL THREE CLOSED 2026-07-27:** PROD-01 (full-time; 40 h/week floor / 72 scheduled), PROD-03 (cash unconstrained; all asset classes self-produced), and the scope menu (Option 4 — full game stays the target; Gate 2 "viable" = ≤ 5 years remaining at the then-current floor). Gate 2 is fully evaluable when reached.
2. **Part II — combat and controls module questions** (they spec the Phase A lab in detail).
3. **Start building the Phase A combat laboratory in Godot** — the spec is ready; interview and lab can run in parallel, with lab findings feeding [T] answers. External-review note (2026-07-27): recommendation is lab before further Part II paper — pre-lab answers deepen lock-in against lab evidence.
4. Any remaining doc polish; the companion docs were refreshed 2026-07-26 and re-synced 2026-07-27.

## How to conduct the interview (unchanged method)

- Ask one focused question at a time and finish it before moving on.
- Let the designer answer naturally, then consolidate into clear design language; give an honest opinion when asked — the designer explicitly values honest pushback and often asks "what would you add?"
- Keep straightforward decisions concise; expand only when a decision has real consequences.
- Use existing answers before asking again; mark conclusions [L]/[P]/[T]/[U]/[CUT]/[LATER].
- Challenge material design or production risks honestly.
- Treat purposeful, targetable repetition as an intended strength.
- Commit after every approved answer (see protocol above).

## Communication preferences learned

The designer writes informally (typos are normal — ask when a typo is ambiguous rather than guessing; this mattered at CORE-34 where "lobe" changed the meaning). They value momentum, honest opinions, and being offered concrete recommendations to react to rather than open-ended questions. They frequently approve batches with a short "ye sounds good" and often invite additions — offer 1–3 well-chosen additions, never a flood.

## Recommended opening prompt for the new session

> Continue the guided design interview and development work for **Wildshot Adventures**. The git repository is the source of truth. Read `notes/INTERVIEW_STATE.md` first and follow its note-taking protocol (one approved answer = one commit). Part I of the questionnaire (CORE-01 through CORE-55) is complete as of 2026-07-26. Ask what I want to do next — Part II module questions or starting the Phase A combat lab in Godot — and keep the established method: one focused question at a time, honest opinions, concrete recommendations, commit everything.
