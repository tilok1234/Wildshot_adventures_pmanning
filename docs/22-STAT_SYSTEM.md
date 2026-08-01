# Wildshot Adventures — Doc 22: The Stat System (loop-era frame)

**Doc:** 22-STAT_SYSTEM
**Status:** DRAFT SKELETON (staged 2026-08-01 pre-talk, sl-0082 queue).
The nine blocks below get ruled ONE AT A TIME in the designer session
("the talk"): short brief → planning's recommendation → the designer's
verdict → the RULING slot fills → one commit per block. Nothing in a
RULING slot is decided until the designer says it.
**Authority:** planning repo. The game consumes; it never amends.
**Customer:** Slice v0.1 (sl-0082) — 4 zones, levels 1–30
zone-bracketed, tiers bracket zones, 3 classes (bow/staff/sword per
the icon set's vocabulary).
**Reference inputs pending:** designer-run deep research A (mitigation
formula survey) + B (movement-speed itemization in dodge-centric
games) — attach as an appendix when they land; reference only, the
design authority stays here.
**Standing constraints inherited (not re-decidable here):** no
accuracy/evasion/crit/lifesteal/resist-matrices (docs/01 §9 [L]);
combat resolves through position and patterns; every number visible on
the tooltip (behaviour-communicated rule); equipment is the build
system; gear primary / levels supporting; movement-only dodging with
CORE-53 proofs at the slowest baseline; T1–T5 loot frame ratified
(deck 2026-08-01); readable small numbers preferred throughout.

---

## Block 1 — Confirm the sheet

**Question:** the locked lean seven (health, mana, damage, attack
speed, range, armor, movement speed) + are the two regen candidates
IN or OUT?
**Recorded:** docs/01 §9 [L/P]; regen explicitly [P] candidates.
**Planning recommendation:** confirm the seven; rule BOTH regens IN,
deliberately boring — health regen slow and out-of-combat-weighted
(keeps potion-less recovery without combat sustain), mana regen a
constant trickle (the ability economy needs a heartbeat; ability items
already own their costs).
**RULING:** ___

## Block 2 — THE damage formula

**Question:** one transparent mitigation model connecting damage and
armor.
**Recorded constraints:** no dice; tooltip-computable in your head;
small readable numbers; armor is a real stat on gear; no immunity
cliffs (visible hits always land and matter).
**Planning recommendation:** flat subtraction with a minimum-damage
floor — `taken = max(attack − armor, ceil(attack × 0.2))`. Readable
at double-digit numbers, armor feels every point, and the 20% floor
kills both failure modes at once (armor never zeroes a hit; big hits
never fully trivialize). Sanity-check against research A when it
lands.
**RULING:** ___

## Block 3 — DPS identity (damage × attack speed × range)

**Question:** how the three weapon-led stats trade inside a frame so
frames stay side-grades in-tier.
**Recorded:** weapon owns the primary pattern + damage/speed/range;
in-tier frames are situational side-grades [P]; chunky felt tier
steps [P].
**Planning recommendation:** tier sets a DPS BUDGET; the frame splits
it (slow-heavy / fast-light / long-reach each ±10% of budget, paid
for by handling). Pattern identity carries the real difference —
numbers only set the envelope.
**RULING:** ___

## Block 4 — Tier budgets (T1–T5, per slot)

**Question:** the per-slot stat budget table per tier + the step size.
**Recorded:** T1–T5 ratified; slice brackets tiers to zones (T1–T4 in
slice, T5 relationship open — the sl-0082 refinement queue);
"chunky, felt steps" [P]; TECH-16 wants unsafe-stat validation.
**Planning recommendation:** ~+35–40% budget per tier step (felt, not
dribble); slot weights — weapon carries offense, armor carries
defense+HP, ability item mostly its active + minor stats, ring purely
situational trades. Exact numbers land in the Block-9 calculator, the
table becomes the TECH-16 validation source.
**RULING:** ___

## Block 5 — Class base curves + the level share

**Question:** per-level gains per class, and how much total power is
levels vs gear at slice cap (30).
**Recorded:** levels grant class base stats (HP/mana chiefly) + skill
points; gear is the primary engine [L/P]; slice levels 1–30
zone-bracketed (lean 5/5/5/10).
**Planning recommendation:** levels ≈ one third of endgame power
(mostly survivability), gear ≈ two thirds; class spreads set identity
(sword tanky-slower, bow fast-fragile, staff mana-rich-mid) — the
same trio the icon emblems name.
**RULING:** ___

## Block 6 — MOVEMENT SPEED (the CORE-33-critical stat)

**Question:** sources, range, and the hard cap.
**Recorded:** premier handling stat, deliberately tuned sources +
caps [L/P]; every pattern provably dodgeable at the SLOWEST class's
base speed (CORE-33 + falsifier); the fit rule changed nothing here
(hurtbox untouched).
**Planning recommendation:** smallest stat range in the game — class
bases within ~10% of each other; gear +ms rare and small; HARD CAP at
+15% over the slowest base; DodgeBot proofs run at BOTH floor and
cap forever after. Research B sanity-checks the cap philosophy.
**RULING:** ___

## Block 7 — The tradeoff grammar (armor archetypes + rings)

**Question:** how "no strictly-better item in tier" becomes mechanics
instead of hope.
**Recorded:** armor = the statistical identity slot with real
give-and-take [P]; rings must never collapse into one correct choice
[L/P].
**Planning recommendation:** every armor/ring stat line is a PAIRED
TRADE from a sanctioned list (+damage/−armor, +speed/−HP,
+range/−speed…), budget-neutral by the Block-4 table; the validator
refuses un-paired uplifts. Archetypes are named trades (light/heavy/
balanced), not free-form.
**RULING:** ___

## Block 8 — The unique rule-break whitelist

**Question:** the bounded list of ways uniques may cheat.
**Recorded:** uniques deliberately break rules with authored,
clearly-communicated effects [P]; powerful but situational [L]; the
excluded stats stay excluded even for uniques? (to rule).
**Planning recommendation:** each unique breaks EXACTLY ONE rule from
a whitelist — pattern replacement, sanctioned exception behaviours
(pierce/bounce/arc), over-budget stat WITH a paired real cost, or a
rule-bending utility; the hard exclusions (crit/evasion/lifesteal/
resists) stay excluded even for uniques — surprise lives in
behaviour, never in dice.
**RULING:** ___

## Block 9 — The balance calculator (spec approval)

**Question:** approve the deterministic checker that makes all of the
above testable.
**Recorded:** bot-testing doctrine; CORE-49 percentile-sim kin;
TECH-14 anticipates DPS/TTK tooling.
**Planning recommendation:** a small deterministic script in the game
repo: inputs = Block 4/5 tables + per-zone enemy bands (the slice's
chapters); outputs = TTK and TTD per zone × class × expected-tier
state; gate = every zone's intended-level TTK/TTD inside declared
target bands, run in CI beside the battery. Balance becomes a check,
not a vibe.
**RULING:** ___

---

## Appendix A — Deep research (designer-run, reference only)

- Research A (mitigation formula survey): PENDING — attach summary.
- Research B (movement-speed itemization): PENDING — attach summary.
