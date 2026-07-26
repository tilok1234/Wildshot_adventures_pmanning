# Wildshot Adventures — Project Handoff

**Handoff date:** 2026-07-21  
**Project stage:** Guided concept definition / early pre-production  
**Baseline documentation:** `01-Wildshot_Adventures_Project_Documentation_2026-07-20.zip`  
**Current active question:** **CORE-21 — What is the ten-second gameplay loop?**

## Current questionnaire state

| Range | State |
|---|---|
| CORE-01 through CORE-15 | Answered in the July 20 project documentation. CORE-14 remains provisional and test-gated. |
| CORE-16 | Completed and locked. The canonical answer is recorded below. |
| CORE-17 | Opened but not completed. Use **first character’s journey to endgame**, not **campaign**. No numerical duration is locked in the current project record. |
| CORE-18 through CORE-20 | Unanswered. |
| CORE-21 | Current active topic. No answer has been accepted. |
| CORE-22 onward | Unanswered. |

The designer chose to continue at CORE-21 while CORE-17 through CORE-20 remain open. Continue at CORE-21 unless the designer chooses to return to one of those earlier questions.

## Source hierarchy

Use the project documentation as follows:

1. `source/Wildshot_Adventures_Living_Design_Questionnaire.md` — authoritative detailed record through the July 20 checkpoint.
2. This handoff — authoritative continuation for CORE-16, the current CORE-17 framing, and the active questionnaire position.
3. `DECISION_REGISTER.md` — concise decision status through CORE-15.
4. `GAME_DESIGN_DOCUMENT.md` — readable design overview through CORE-15.
5. `OPEN_QUESTIONS.md` — unresolved-question list from the July 20 checkpoint.
6. Other planning documents — working interpretations, dependencies, risks, and prototype guidance.

The July 20 files still show CORE-16 as blank because they predate the discussion recorded here.

---

# Newly completed decision

## CORE-16 — Desired normal session length **[L]**

Wildshot Adventures should not prescribe one correct or normal session duration. A satisfying session is defined mainly by whether the player can actively pursue a self-chosen goal they genuinely care about, rather than by whether the game guarantees a permanent upgrade within a fixed amount of time.

A session may feel worthwhile through:

- completing or advancing quests;
- exploring and discovering useful information;
- learning routes, enemies, mechanics, dungeons, or bosses;
- improving execution, knowledge, or clear efficiency;
- completing dungeon or boss attempts;
- performing additional targeted loot rolls;
- receiving equipment, uniques, or other permanent progression when the rolls succeed.

### RNG pursuit and the meaning of progress

The game is intentionally heavily RNG-based. Repeated independent attempts are meaningful progress in the broader pursuit even when the desired item does not drop.

More boss kills or dungeon clears create more total opportunities to succeed across the full set of attempts. Ten attempts therefore give a better overall chance of having received the item than one attempt. However:

- failed attempts do not increase the next attempt’s drop chance;
- no escalating drop-rate modifier is accumulated;
- no pity value is banked;
- the next roll retains its normal independent probability.

A player may reasonably finish a session feeling that progress was made after two unsuccessful boss kills. The item is not mechanically closer and the next roll is not improved, but the player completed two relevant attempts and did what the pursuit requires: continued crushing the numbers.

### Session-length implications

Brief and extended sessions should both be worthwhile:

- A brief session may contain quest progress, discovery, practice, a dungeon run, or a small number of targeted attempts.
- A longer session may contain sustained exploration, extensive dungeon or boss farming, greater mastery, and many more loot opportunities.
- Receiving no unique item or permanent upgrade does not inherently make a session unsuccessful.
- CORE-16 does not lock numerical session-duration ranges.

### Pausing, leaving, and dungeon commitment

Active single-player gameplay should be pausable so real-life interruptions do not destroy an active run.

An ordinary dungeon should normally be completed as one committed gameplay attempt:

- pausing while remaining in the active run is allowed;
- leaving or abandoning the dungeon ends that instance;
- the player cannot return later to the same partially cleared dungeon state;
- the dungeon is not permanently completed room by room across separate entries.

This preserves the value of preparation, investment, consistency, dungeon knowledge, and improving clear efficiency. As the player masters a dungeon, faster and more reliable clears allow more complete attempts—and therefore more independent reward opportunities—within the same available playtime.

### Raid details deferred

Exact raid duration, maximum uninterrupted commitment, wing structure, section boundaries, checkpoints, and continuation rules are deferred until raids are designed properly.

Separate raid wings or sections are possible future design space. Naxxramas and Karazhan were mentioned only as broad structural examples; no wing-based raid format is currently committed.

---

# CORE-17 clarification

## CORE-17 — First character’s journey to endgame **[Open]**

The questionnaire currently calls this the length of a first **campaign**, but that term gives the wrong impression for Wildshot Adventures because it suggests a fixed, predetermined route through authored story content.

The initial progression should instead be framed as the player’s **first-character journey to endgame** or **initial zero-to-hero journey**.

The player may advance through different combinations of:

- quests;
- ordinary enemy grinding;
- exploration;
- equipment hunting;
- dungeons;
- bosses;
- other progression activities established later.

The project already establishes a long-form, knowledge-driven zero-to-hero experience. Reaching endgame is the broad transition being discussed, not necessarily completion of a linear quest path or the end of character progression.

Still unresolved:

- the numerical target for a first journey to endgame;
- the exact mechanical threshold that counts as reaching endgame;
- how focused progression, optional content, and later endgame time should be measured separately.

The current project documentation contains no locked numerical answer for CORE-17.

---

# Essential project direction

Wildshot Adventures is a single-player-first, top-down 2D open-world fantasy action RPG combining:

- freely aimed projectile combat, movement under pressure, portal hunting, dungeons, bosses, tiered equipment, and authored unique-item pursuit inspired primarily by **Realm of the Mad God**;
- a long-form, knowledge-driven, zero-to-hero single-player MMO journey inspired primarily by **Erenshor**.

The player creates a permanent **Archer, Warrior, or Mage**, with at least three character slots available. Each class has its own skill tree. The equipped weapon owns the primary projectile pattern; class skills support the class plan without routinely replacing or universally multiplying the weapon pattern.

The four design pillars are:

1. Satisfying freely aimed projectile combat, even without valuable drops.
2. A visible zero-to-hero journey.
3. Open-world knowledge and targeted hunting that earn access to concentrated challenges.
4. Boss mastery that develops into a rewarding unique-item chase.

Ordinary open-world play should feel laid-back, satisfying, and productive. Dungeons and world bosses become faster and more demanding. Endgame bosses and raid-scale encounters may become relentless, but attacks, hazards, safe spaces, and causes of death must remain readable and learnable.

Specific associated enemies directly drop portals to specific dungeons. Fragment crafting is not the baseline. Current provisional test targets are approximately 20–30% portal chance from associated normal enemies and 50–100% from associated world bosses; practical targetable farming matters more than the exact percentages.

Tiered equipment can drop broadly and forms the dependable vertical progression ladder. Authored unique equipment comes from named world bosses, dungeons, raids, and potentially selected major quests. Generic normal enemies do not randomly drop uniques. Uniques should be powerful and situational rather than universally superior.

All classes and all content must remain solo-completable. Optional two-player online co-op remains provisional and depends on an early host-authoritative networking prototype. Mouse and keyboard defines the full combat and endgame ceiling. Controller support is secondary and may be reduced or removed rather than weakening combat or encounter design.

The business model is a premium one-time Steam purchase with no subscription, battle pass, pay-to-win purchases, recurring-payment structure, or live-service retention pressure.

---

# Continuing the guided interview

Use the established project-document method:

- Ask one focused question at a time and finish it before moving on.
- Let the designer answer naturally, then consolidate the intent into clear design language.
- Keep straightforward decisions concise and preserve momentum.
- Expand when a decision creates a meaningful design, balance, technical, or production consequence.
- Use existing answers before asking for a decision again.
- Mark conclusions as locked, provisional, test-gated, unknown, cut, or deferred.
- Update the living questionnaire and companion documents in sensible batches.
- Treat purposeful, targetable repetition as an intended strength rather than assuming grind should be removed.

## Next question

**CORE-21 — What is the ten-second gameplay loop?**

The source questionnaire defines this as the actions, decisions, feedback, and immediate result that repeatedly occupy the player over roughly ten seconds.

No CORE-21 answer has been accepted. Continue the question fresh and let the designer describe how ordinary, level-appropriate moment-to-moment play should flow.

## Recommended opening prompt

> Continue the guided design interview for **Wildshot Adventures** using the attached project documentation and this handoff. CORE-16 is locked as recorded here. CORE-17 through CORE-20 remain open, but the current active topic is **CORE-21 — the ten-second gameplay loop**, which has no accepted answer yet. Ask one focused question at a time, preserve the established design direction, keep straightforward conclusions concise, and challenge material design or production risks honestly.
