# 2026-08-02 — The Green-days batches session (nine routed seams)

Routing: the designer's Green-days paper batches #1 + #2, routed planning-side
as nine seams in dependency order (sl-0119, 0121, 0122, 0132 view family;
sl-0120 sim pass; sl-0116+0128, 0129, 0130, 0131 inventory family). Executed
in the game repo, each as its own sealed seam (build → gate → commit → push).
The planning sweep agent ran concurrently and swept each push into the
register/lock (its commits carry the deep per-seam record; this file is the
session narrative + lessons).

## Landed (all pushed to game main)

1. **sl-0119 — C sheet on screen** (`42d8260`). Root cause: zero-size
   PRESET_CENTER in _ready pins the panel's top-left at screen center (the
   camera holds the player there — hence "player-anchored") + fit_content
   unbounded growth. Fix: explicit center anchors from a computed size,
   ui-scale-aware, viewport-clamped, errands scroll [T]. RIDER: the
   onboarding screen carried the same latent bug (sibling grow-BOTH fix).
   Evidence at THREE scales (base / desktop screen-crop / ui-scale-2).
2. **sl-0121 — quest pull** (`e0dbe1f`). Overhead giver icons
   (quest.available / quest.turn_in — the obvious pack pair [T]);
   corner+full map markers (VISIT objective = amber diamond, turn-in =
   green ring, shape-first); HUD tracker top-right (short id-slug names,
   "DONE — return" cue, cap 5). C stays THE log; the bottom-left readout
   keeps the bare errand count [T]. HONEST GAPS reported: KILL/COLLECT
   quests carry no objective cell in data (planning data call if wanted);
   the capital zone-hub giver has no NPC body (slot == spawn cell, filtered
   by npc_view); the only minimap is dev-only (lint-pinned) — the designer
   plays dev so markers reach them; a tester-facing map stays the doc-13
   Part II designed round.
3. **sl-0122 — boss sprites** (`34c9035`). Grubb → boss:goblin-war-crown
   (importer run with BOTH ids — it rebuilds actors[] from argv);
   actor_sheet_map grew a view-side `scales` dict; Old Tusk 1.25 [T] —
   the ~1.3 ask taken to the nearest pixel-even step under the integer
   stretch (24→30 px exact). Sim/hurtbox untouched; control-boar +
   ranger in the evidence lineup.
4. **sl-0132 — NPC desync** (`a446a30`). Deterministic per-cell phase
   offsets (variant_hash fold — no RNG stream) + speed wobble 0.9–1.1 [T];
   probe grew a mechanical spread readout with a loud lockstep regression
   guard (32 sprites / 15 phases / 28 speeds).
5. **sl-0120 — firing rate ×1.25 exact** (`cdee9ea`). THE FINDING: the
   routed ~1.5× start is mathematically impossible under docs/22's own
   hits-to-kill band [3,5] vs the fast_light reference (6-hit kills at
   3.0/s; ceiling ~1.304×). Landed the largest EXACTLY-EVEN step ×1.25:
   cadences 100/30/50 → 80/24/40, rates 0.75/2.5/1.5 exact; damage
   re-derived via the calculator, all five gates PASS; TTK table delivered
   (sword 3.33→2.67 s, staff 2.50→2.00/2.67, bow held 2.00 s; TTD
   untouched). THE DESIGNER'S LEVER (if 1.25 still feels slow): raise
   trash_hp or widen the hits band — planning-side only. Feel flag stands.
6. **sl-0116 + sl-0128 — THE BAG** (`36a70b3`). SERIAL 23, WSR v3.
   Pick up INTO the bag (cap 20 [T]); equip is a DECISION via ONE recorded
   bag_op byte (replay-honest; bots never emit); replaced items return to
   the bag; armor/ring de-equip two-way; weapon replace-only [T]; the
   equipment pane in C with tooltip==drop_line test-pinned; mouse
   sanctioned with suppress-over-pane; death keeps the bag; legacy lane
   never bags (battery byte-identical by construction). Goldens + nine
   pinned-FAIL repros re-recorded v3 deliberately.
7. **sl-0129 — loot bags** (`29b1e14`). SERIAL 24.
   A kill's non-gold roll lands in ONE ground bag at the corpse (same
   rng_loot sequence — only the landing moved); gold stays its own
   walk-over drop; walk-over panel lists contents (no press); click a row
   to loot one; [B] loot-all [T — G was taken by the GIF key]; empty bag
   despawns; bag TTL = 2× drop TTL [T]; full player bag leaves leftovers;
   LOOT_PICKED per looted item (COLLECT quests count). CLASS-LANE WORLDS
   ONLY — legacy worlds keep per-item ground drops verbatim (the seam-6
   doctrine extended; battery honest).

8. **sl-0130 — the bank** (`4be7e75`). SERIAL 25. Walk-up panel at the
   PINNED stash-keeper station (112.5,182.5) — chosen clear of the
   quest-giver radius (the pack's giver.system.banker slot sits ON the
   spawn cell and would collide with the zone_hub giver; recorded [T
   station call: walk-up panel, the loot-panel language, rather than an
   F chest]). Deposit/withdraw are recorded ops legal only within radius
   1.2 sim-side; BANK_CAP 12 [T] distinct from the bag; capacities refuse
   loudly both ways (new BANK_FULL event); DEATH NEVER TOUCHES THE BANK
   (test-pinned); profile "bank" rows ride the by-id encoder.
   Grammar note: the one-decimal rate shows 0.75/s as "0.8/s" (display
   rounding, recorded).
9. **sl-0131 — vendors v1** (`912049f`). NO serial bump (stock is
   setup config; trades mutate gold+bag, already serialized). "vendors"
   balance_frame block (the starhook new-key precedent): sell 50% of
   value, buy 200% [T]; values weapon/armor by tier [10,16,26,40,64],
   rings by items-tier [12,20,32,50,80], ability 20, unique 100 [T all].
   Fixed CATALOG, infinite quantity v1 [T — "small FIXED stock" read as
   catalog]; stocks: general (T1 armor / haste ring / T2 weapon) +
   trader (T2 armor / reach ring). Stations: merchant (106.5,182.5) +
   trader (106.5,180.5) bodies pinned west of spawn (nearest-vendor
   resolution; cross-system separations ≥2.83). Buy refuses poor and
   full-bag with gold untouched (bag_add-first order — nothing
   half-happens). Fish-currency explicitly FUTURE, as routed.

## Lessons (recorded where they bit)

- **The desktop-capture honesty guard keeps earning its keep**: it caught
  its own naive mapping twice (the letterbox offset on 16:10 screens; a
  signature point sitting on an ANIMATING body) — both fixes live in the
  probes; every future probe copies the letterbox-aware two-point pattern.
- **SceneTree-script probes defer _ready to the first frame** — a
  post-add_child property feed lands BEFORE _ready and gets overwritten;
  feed after the first `await process_frame` (quest_pull probe lesson).
- **An sl-0129-class landing change breaks kill-produces-ground-drop test
  premises repo-wide** — loop_test §9 re-authored to source ground items
  explicitly; the legacy negative exposed the need for the lane-split
  landing (class worlds bag, legacy worlds keep loose drops verbatim).
- The planning sweep agent runs LIVE between game pushes — sync-log id
  collisions are real (gotcha 25 held: id verified at write time).
