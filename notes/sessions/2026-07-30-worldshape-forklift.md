# Session record — 2026-07-30, the forklift world-shape session (phone, at work)

**Session type:** planning/design conversation (remote, designer on phone
during work dead-time; agent session rooted in planning).
**Also produced earlier same session:** the operator guide
(`notes/operator-guide/` — quick card, manual, queue snapshot, PDFs).
**Hours:** designer's call — ~1 h scattered across the shift, designer
inclined not to count it; agent recommendation on record: log 1.0 h
(a pillar-level design reconnection + 14 recorded directions is work;
undercounting distorts the PROD-01 floor measurement like overcounting
would). Final call is the designer's.

---

## 1. The big one: the world shape, reconnected (Tier 1, designer)

The designer opened with "we should rethink the game — zones more like
Erenshor" (persistent living world, level-banded zones). On checking the
interview record, **no rethink was needed**: CORE-16 onward already
records exactly this vision — the fractal zone rule (CORE-36 [L]),
open-world death as respawn-at-city + gold fee (CORE-43), MMO-dense
geographic quest world (CORE-46), living hub cities with staged
recognition (CORE-47), 40–80 h zero-to-hero into a collectathon
endgame (CORE-17/18), slice = one zone + hub (CORE-52).

**Ruling (Tier 1, designer):** the game is and always was the Part I
persistent world. The Loop milestone is not the game's shape — it is
the **first mile of that world**: the minute-to-minute atom (leave
safety, fight, loot, maybe die, want to go again) that must be fun
before zones multiply it. No CORE amendments required. The loop bar
re-aims accordingly: "is the first mile of MY world worth walking
daily," not "is this run game fun." L1's death design (carried-gold
cut + run-back) already implements CORE-43's open-world death rule.

**Sequencing consequence (flagged, not yet ruled):** world_filler's
territory/danger-band/spawn authoring is the zone-authoring engine for
this shape — its consumption timeline likely moves up (it was
post-Gate-1 by doc 17). sl-0041 (dusk overworld direction rehearsal,
docs/20 step 1) is exactly this machinery starting.

## 2. The W-set — world & aliveness directions (all Tier 1, designer-approved as a set)

Status tags proposed; [P] unless noted. Deck payload for ratification
taps: `tools/decision_deck_items_2026-07-30-worldshape.json`.

- **W-1. Population model [P]** — placed camps are the backbone
  (learnable geography; camps can guard bosses/sites); loose roamers
  drift through wilds for texture. Grammar explicitly non-exhaustive.
- **W-2. Early cosmetic rare [P]** — a low-zone rare carries a
  high-rate cosmetic drop, introducing the collection game early to
  lucky finders (slots into CORE-18 + the dry-streak-breadth rule).
- **W-3. Respawn model [P]** — repopulation pace varies by zone depth
  (lazy safe zones, fast deep zones) AND by player proximity — the
  world refills behind/around the player, never popping in their face.
- **W-4. Rares, both archetypes [P]** — spot-check "he's UP" rares and
  free-roaming hunt rares coexist; roamer routes may cross zone lines
  so surprise encounters (mid boss-circuit) are intended, not
  accidental.
- **W-5. Intertwined zones [P — PILLAR CANDIDATE]** — zones keep a
  general level progression but deliberately contain cross-band
  pockets: endgame areas inside starter zones (walk in, get one-shot,
  learn and remember), high-level dungeons inside low-level zones or
  cities. The world teases its own future everywhere. Designer: "we
  can score a lot here."
- **W-6. Roads = geography [P]** — no safety promise for now; roads
  exist because a world without them looks wrong. Revisit later.
- **W-7. Roaming NPCs [LATER]** — when they come: free-roaming, not
  road-bound; some common, some rare finds.
- **W-8. Town aliveness v1 [P]** — stationed NPCs (smith at forge,
  keeper at inn); presence over motion. No vendor mechanics yet —
  nothing currently requires them.
- **W-9. Scavenging-vendor idea [PARKED]** — designer couldn't
  reconstruct it in-session; no decision recorded.
- **W-10. Day/night & weather [LATER + guardrail, L-candidate]** —
  deferred. Standing guardrail whenever built: night must never be a
  visibility tax on grinding; weather must never be a performance tax.
  Atmosphere only ever ADDS — never degrades readability or framerate.
  (Designer pet peeve turned into law; kin to Readability Law 1.)
- **W-11. Night gameplay meaning [LATER]** — bolder-monsters-at-night
  considered eventually, contingent on W-10.
- **W-12. The aliveness test [P] (amended in-session)** — ordered:
  (1) enemies and camps read as ORGANIC, not generic — prerequisite:
  you must care to kill things before loot gets its chance;
  (2) loot worth reading — drops that cause stat-reading pauses;
  (3) audio pull — the never-mute bar. Designer's sentence: "when I
  want to play the game, that is when it feels alive."
  **Banked evidence:** the designer historically mutes game music and
  has not muted Resonance Forge's — the never-mute bar is already
  passed (Tier 1 taste verdict for RF, provisional as all feel).
- **W-13. Prop density vs movement freedom [P]** — from the designer's
  own map test: keep the visual density, CONVERT instead of delete —
  suitable props become walkable (walk-over "carpet" class per the
  moss precedent; walk-under canopy class per the awning precedent);
  solid reserved for things that should visibly read as blockers
  (CORE-32 needs solids to look solid; CORE-33 makes open-field
  freedom combat law). Ready-to-paste WF ask drafted (§3).
- **W-14. The purposefulness rule [P — PILLAR CANDIDATE]** —
  everything in the world exists for an in-world reason discoverable
  by looking at it; the named anti-pattern is "objectives placed
  throughout a world". Working test for any placement: **"what is
  this doing here?" should have an answer a villager could give.**
  Generalizes W-12's organic-camps prerequisite; makes W-5's pockets
  automatically purposeful; kin to CORE-46's "quests speak the game's
  own language" and the handcrafted-world rule. First exercise:
  judging world_filler's sl-0041 proposals.

## 3. Ready-to-paste WorldForge ask (W-13) — NOT yet logged as ask_opened

> Ask from the game/design side (designer-relayed): open-world prop
> density currently constrains movement more than intended. Do not
> thin props. Instead, classify wilderness props into three
> walkability classes and re-export: (1) walk-over "carpet" class for
> ground clutter (small rocks, tufts, debris, low bushes) — renders,
> never blocks, moss-carpet precedent; (2) walk-under canopy class for
> overhangs, tree-canopy precedent; (3) solid reserved for things that
> should visibly read as blockers (trunks, boulders, built walls).
> Designer taste rules edge cases. Expect flood/walkability changes —
> normal validation + delivery protocol applies.

**Sync-log note:** this record deliberately does NOT allocate a
sync-log id for the ask (this session ran on a side branch; allocating
sl-00xx here risks id collision with tonight's mainline sessions).
Whichever session pastes the ask into WorldForge logs `ask_opened`
with the next free id and may cite this file.

## 4. Board state discovered for the evening (verified by fetch)

- The morning phone WF session died without pushing — WorldForge tip
  is still the 13:32 handoff; nothing lost, nothing done.
- **sl-0035 OPEN:** b72 delivered (country roads as band lines),
  designer-approved for intake this morning, game-side intake
  unfinished — first move tonight.
- b72 road look: verdict pending, designer's eyes (WF-side).
- **sl-0041 OPEN:** world_filler directed-dusk-overworld rehearsal
  (docs/20 step 1), designer in the loop — where W-14's villager test
  gets exercised first.
- Designer is post-shift tonight: by the two-tier rule, no feel
  verdicts tonight; intakes, verdict-of-record on roads (taste
  ruling), direction sessions, render checks all fine.

## 5. Also this session (operator infrastructure)

Operator guide v1 (quick card + manual + perishable queue snapshot,
markdown + generated PDFs + build script) committed at
`notes/operator-guide/` on branch
`claude/operator-protocols-guidelines-ruyu4q`. Queue snapshot
refreshed end-of-day with the evening board. All derived,
non-authoritative, dated, regenerable (`python3 build_pdfs.py`).
