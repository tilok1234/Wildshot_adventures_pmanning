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
**Reference inputs:** LANDED 2026-08-01 at talk start — TEN
designer-run deep researches (the five commissioned topics × TWO
engines: GPT 5.6 Sol Pro + Kimi Agent), vendored verbatim at
`notes/research/2026-08-01-stat-talk/`, assessed into Appendix A
below. Reference only, the design authority stays here.
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
**RULING (designer, 2026-08-01):** the SEVEN CONFIRMED — health /
mana / attack (damage) / attack speed (dexterity) / range / armor
(defense) / movement speed (speed) — the parentheticals are the
designer's display-name candidates, captured [P]; final HUD naming
is a UI decision later. BOTH regens IN, deliberately boring (the
designer's word: "boring health and mana regain"): health regen
slow and out-of-combat-weighted — potion-less recovery, never
combat sustain; mana regen a constant trickle — the ability
economy's heartbeat, ability items keep owning their costs.
Neither regen appears on gear at first — base-stat lane only, so
the gear sheet stays lean at seven. Register: CORE-40 amended.

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
**RULING (designer, 2026-08-01, "i agree"):** THE FORMULA IS
`taken = max(attack − armor, ceil(attack × 0.2))` — flat
subtraction, 20% minimum-damage floor, floor rounds up (attacker's
favor), ONE rounding step. 1 defense = 1 less damage, felt
exactly; no hit ever zeroes; no armor ever makes immune. Both
engines' research independently recommended this exact shape
(Appendix A.1; floors bracketed 10–25%, ours mid). RIDER RULED
WITH IT (the enemy-side half): enemies get stronger across zones
by hitting BIGGER and in MORE patterns — never by becoming damage
sponges (CORE-36 kin, now formula-bound); per-bracket obtainable
armor budgets stay ~0.4–0.6× the bracket's typical enemy hit so
defense stays a live choice — the block-4 tables + the block-9
calculator inherit this as a constraint, and the calculator flags
any bracket where obtainable armor ≥ 0.8× common attacks (the
floor-plateau onset). Register: CORE-40 second amendment.

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
**RULING (designer, 2026-08-01, "ye this sounds good but we got to
make sure we come up with a way to properly balance the different
patterns"):** RULED AS RECOMMENDED — the tier sets a DPS BUDGET;
frames split it (damage × attack speed lands on budget); frames sit
within ±10% of budget, paid by handling — extra range/comfort costs
DPS, short/awkward earns it; the PATTERN is the identity, numbers
only set the envelope. Free block-2 synergy noted: slow-heavy
punches through armor (fewer, bigger hits lose less to flat
subtraction), fast-light is smoother but armor-taxed — a real trade
with zero extra rules. **THE DESIGNER'S CONDITION, ruled in as the
mechanism:** patterns are balanced by MEASUREMENT — a deterministic
pattern × scenario matrix (single target / clump / line / moving
target reference situations, bot-run, realized-DPS not paper-DPS)
with the gate "each pattern BEST IN ≥1 scenario, best in NONE
everywhere" — the situational-side-grade promise (CORE-41) made
mechanical; lands in the block-9 calculator spec; the encounter
side's showcase rule (CORE-44: clumps→spread, lines→pierce,
distant→long shot) is the same promise's other half. Register:
CORE-41 amended.

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
**RULING (designer, 2026-08-01, "we will go for plannings
reccomendation this actually sounds perfect for the game"):** RULED
AS RECOMMENDED, all four parts — (1) **the WEAPON carries the big
step: +40% DPS budget per tier** (the tier fantasy is the weapon;
research consensus: few tiers must be chunky or they're invisible,
Appendix A.4); (2) **defense is ENEMY-ANCHORED, not free-floating:**
per-tier armor lands wherever it keeps obtainable armor ≈ 0.4–0.6×
the tier's zone's typical enemy hit (the block-2 rider); HP steps
+25–30%/tier — offense explosive, survivability steady, old zones
never instantly trivial; (3) **slot jobs:** weapon = all offense ·
armor = defense + HP (archetype trades live here) · ability item =
its active + minor stats · ring = NO raw budget, purely paired
situational trades (block 7's grammar); (4) **T5 = rare capstone
pieces in late Snow Country (~lvl 28+), boss/dungeon-anchored** —
not a fifth zone-tier; the ladder stays 4 zones = 4 tiers with a
chase on top (the open sl-0082 T5 question CLOSES). Exact per-slot
numbers generate + verify in the block-9 calculator; the table is
the TECH-16 validator's source (over-budget items refused
mechanically). Register: CORE-37 amended.

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
**RULING (designer, 2026-08-01, "yep its like if you read my mind
this is perfect"):** RULED AS RECOMMENDED — (1) **the split:
levels ≈ ⅓ of cap-30 power, gear ≈ ⅔; the level third is
SURVIVABILITY-WEIGHTED** (research kin: weapons ~×5 across the
campaign vs levels ~×3 carrying HP, Appendix A.4); (2) **per level:
class HP + class mana + 1 skill point — NO automatic damage.**
Damage is the weapon's job, full stop — the split stays honest and
deaths stay readable (dying → you need levels; slow fights → you
need a weapon). The block-1 boring regens ride the level lane
(baseline, never build choices — the "if every build takes it,
make it baseline" doctrine, Appendix A.3); (3) **class spreads =
identity inside the same budget:** sword tanky at the slow end
(most HP, base speed at the floor) · bow fast-fragile (top of the
narrow band, least HP) · staff mana-rich middle — the icon trio;
(4) **XP curve: FLAT PER ZONE, stepping at zone borders** on the
ruled brackets (readable: "this zone asks N/level, pays ~M/kill");
time-per-level is chosen first and XP back-solved — constants land
in the block-9 calculator, not the talk. Register: CORE-39
amended.

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
**RULING (designer, 2026-08-01, "we can do it as you reccomend,
but we might have to look at it later after we tried it some"):**
RULED AS RECOMMENDED, the cap NUMBER explicitly feel-gated [P/T] —
(1) class bases 100 (sword, the floor) / ~105 (staff) / ~110
(bow); (2) gear speed RARE and TINY, and speed NEVER converts to
damage; (3) **HARD CAP +15% over the slowest base (115), counting
everything combined, enforced IN THE MOVEMENT INTEGRATOR** —
never in item data ("spreadsheet caps leak", Appendix A.2);
applied after all modifiers; a quiet perk falls out: the slow
tanky class benefits most from speed gear, the fast class starts
near ceiling; (4) DodgeBot proofs at floor AND cap forever, plus
the three research-earned hardenings: proofs cover pattern
COMBINATIONS/alignments (jointly-inescapable overlaps are a
shipped failure elsewhere), chaser enemies stay slower than the
slowest base, and any future slow-effect re-triggers the proofs
at its new floor — NO slows in the slice. Both engines' looser
caps (135–150%) considered and REJECTED with cause (their own
evidence argues tight; Appendix A.2). **THE REVISIT IS DESIGNED
CHEAP:** the cap is one constant + a proof re-run — the
designer's "look at it later after we tried it some" is a
sanctioned one-line act after real play (Loop run / slice feel),
never a redesign. Register: CORE-40 third amendment.

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
**RULING (designer, 2026-08-01, "yeah this reccomendation is very
good"):** RULED AS RECOMMENDED — (1) **every armor/ring stat line
is a PAIRED TRADE from the sanctioned list (v1):** +damage/−defense
· +speed/−HP · +range/−attack speed · +HP/−speed · +defense/−damage
· +mana/−HP — one up, one down, budget-neutral vs the block-4
tables; NO un-paired uplifts exist — the block-9 validator REFUSES
any item that gets something for nothing (the TECH-16 hook made
real); (2) **armor archetypes are the three named trades:** light
(+speed/damage-lean, pays HP/defense) · heavy (+HP/defense, pays
speed) · balanced (small trades both ways) — learned once, read
forever; (3) **rings = the pure situational slot:** each ring is
exactly ONE sanctioned pair sharpened — a choice about the fight
you're walking into, never a ladder; no universal ring by
construction; (4) **ONE GRAMMAR EVERYWHERE:** tree nodes and future
uniques speak the same pair vocabulary (Appendix A.3's grammar
finding) — every tooltip in the game reads the same way. List
extensions are a deliberate act (add a pair = a register row).
Register: CORE-37 second amendment.

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
**RULING (designer, 2026-08-01, "yeah this is perfect . ye
swapping can be easy i think"):** RULED AS RECOMMENDED — (1)
**each unique breaks EXACTLY ONE rule**; zero = not a unique, two
= never (two-break items go mandatory — both engines' shared
doctrine, Appendix A.5); (2) **the whitelist is the closed
complement of the ladder blocks 3/4/7 built:** (a) pattern
replacement · (b) sanctioned exception behaviours
(pierce/bounce/arc/return) · (c) over-budget stat WITH a paired
real cost paid IN PLAY on the same axis as the benefit (never
acquisition-priced) · (d) rule-bending utility
(information/interaction, non-combat); (3) **the hard exclusions
hold even for uniques** — no crit/evasion/lifesteal/resists/dice,
surprise lives in behaviour; (4) **slice discipline: each rule
broken AT MOST ONCE game-wide** (~8–12 slice uniques per the
bill — every unique memorable, no rule quietly repealed); (5)
**chassis rule: a unique's ordinary stats run ~70–90% of its
tier's slot budget** — the break IS the premium; tiered gear
keeps the best pure numbers, uniques are options not upgrades
(the evergreen mechanism at any tier); (6) **souvenir touch:**
where possible a boss's unique re-performs that boss's own
signature mechanic. **SWAP RULING [P]:** gear swapping is EASY —
sharp narrow niches are sanctioned (swap-in-for-the-moment is
intended play); exact swap UX (mid-fight vs between-pulls) lands
at slice build. Register: CORE-41 second amendment.

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
**RULING (designer, 2026-08-01, "approved"):** THE CALCULATOR IS
APPROVED as specced — a small deterministic script in the game
repo, CI-run beside the battery, gates named: (1) TTK/TTD per
zone × class × expected gear inside declared target bands at the
intended level; (2) the armor liveness flag (obtainable armor ≥
0.8× common hits = plateau warning, block 2); (3) the pattern
fairness matrix (realized DPS per pattern × scenario — best
somewhere, best nowhere-everywhere, block 3); (4) the chunky-hits
assertion (ordinary enemies die in 3–5 hits at every band;
frequent numbers ≤3 digits); (5) the ITEM VALIDATOR (tier budgets
+ paired-trade grammar + unique one-break/chassis rules refused
mechanically — TECH-16 discharged). Data lives in a versioned file
in the game repo mirroring the docs/22 tables; the design
authority stays here. PAPER-FIRST scope: NO sim change rides this
— the stat frame enters the sim at slice build; the calculator
comes first so the numbers exist before the code does. Endgame
curves re-derive against real content later (scoped out, header
rule). **THE GAME PASTE is the talk's closing deliverable**
(routed sl-0095; verbatim in the session file).

---

**ALL NINE BLOCKS RULED 2026-08-01 — the loop-era stat frame is
COMPLETE.** One commit per block (see the session file for the
designer's words per ruling); register amendments on
CORE-37/39/40/41. The slice bill (sl-0082/0087) was the customer
throughout; the calculator paste is the hand-off to the game repo.

---

## Appendix A — Deep research (designer-run, reference only; assessed 2026-08-01)

**What landed:** TEN deep researches at talk start — the five
commissioned topics × two engines (GPT 5.6 Sol Pro = "GPT" below;
Kimi Agent = "Kimi"). Sources vendored verbatim at
`notes/research/2026-08-01-stat-talk/` (its README maps the files).
Each topic pair was read in full against the locked constraints.
**Research is REFERENCE — nothing in this appendix is a decision;
the design authority stays this repo, and every RULING slot above
stays the designer's.**

### A.0 Cross-cutting verdict (the headline)

- **The skeleton survives contact.** No research overturned any
  locked constraint or planning recommendation. The two strongest
  independent convergences are exactly our shapes: block 2's
  flat-subtraction-with-floor (both engines recommend it unprompted)
  and block 8's exactly-one-rule-break whitelist (both engines state
  it as THE doctrine — GPT nearly verbatim to our draft).
- **Where the engines disagree with us:** both movement-speed docs
  recommend looser caps (135–150% vs our 115%) — but their own
  evidence argues our way (A.2). The two pacing docs bracket our
  +35–40% tier-step lean from opposite sides, and the engine arguing
  CHUNKY is the one aligned with the ruled taste (A.4).
- **Bracket-shift warning for every quoted table:** both pacing
  researches assumed zone brackets 1–7 / 8–14 / 15–21 / 22–30. Ours
  are RULED 1–7 / 8–15 / 16–22 / 23–30 (even split, sl-0087). Every
  level-indexed number quoted from them shifts accordingly.
- **Contamination filtered:** neither engine knew our locks; survey
  material carries the expected crit/proc/RNG/dash vocabulary, all
  flagged per topic below. Notably both engines' ORIGINAL designs
  (vs their survey sections) are mostly clean of it.
- **Sourcing honesty:** GPT's citations are unresolvable engine
  tokens (claims plausible, unverifiable as delivered); Kimi cites
  real URLs but leans on community sources, with footnote gaps and
  dangling figure references. Where both engines independently agree
  on a number, trust rises sharply (they corroborate each other on
  nearly every shared case). One direct factual clash — RotMG's
  minimum-damage constant (GPT ~15%, Kimi 10%) — means we cite no
  reference-game constant as fact in the talk.

### A.1 Damage mitigation (feeds block 2)

Sources: `gpt-sol-pro/damage-mitigation.md` ·
`kimi-agent/damage-mitigation/Damage_Mitigation_Models_Survey.md`

**GPT says:** surveys four families with formulas — flat subtraction
w/ floor (RotMG, Vampire Survivors), direct % (Hades, multiplicative
stacking), rating curves (D3's `A/(A+50L)` — EHP grows LINEARLY
despite the "diminishing returns" look), partial absorption (Grim
Dawn 70%), hit-size-dependent (PoE's `A/(A+5·hit)`, rejected as
tooltip-opaque). **Recommends flat subtraction with a 25% floor:**
`taken = max(ceil(0.25·attack), attack − armor)`. Tuning frames:
armor bands stay below typical hit size; value armor by
prevented-DPS = hit-rate × armor; ≤70–75% total sustained
reduction; a failure-mode table (floor plateaus, one-shot cliffs,
single-rounding rule).

**Kimi says:** same families + the pipeline-ordering lesson
(flat-AFTER-percentage is the hybrid that works; D2's opposite order
makes flat rolls junk). **Recommends
`final = max(hit − armor, ceil(hit × 10%))`** — integer math,
floor rounds in the attacker's favor. Budget rule: obtainable armor
≈ **0.4–0.6× the bracket's typical enemy hit**. Doctrine: scale
enemy hit size/count across brackets, NOT enemy HP sponges.
Graduation path if numbers ever inflate: small-K hyperbola
`A/(A+15)`. Parks three deterministic "dials" (elite Pierce N,
one conditional %, one per-hit-cap relic).

**Convergence:** both independently recommend our exact block-2
shape; our 20% floor sits between their 10% and 25%. Same failure
triad named; both reject evasion-style and hit-size models; both:
round once, publish the direction, worked-example tooltips; same
fallback (small-K hyperbola, K 15–20) if hit ranges widen.

**Applies to Wildshot:** block-2 recommendation CONFIRMED twice
over; the floor argument brackets 20% as defensible middle ground
(GPT: higher shrinks plateau zones; Kimi: lower keeps the negation
fantasy). New adoptables for the talk: armor budget 0.4–0.6× typical
hit per bracket (feeds block 4 + the calculator); the calculator
flags any bracket where obtainable armor ≥ 0.8× common attacks
(plateau onset = attack × (1 − floor)); classify enemy attacks by
RATE not just size; tooltip carries one worked example + an "armor
still helps vs stronger hits" line. Enemy-side doctrine adoptable:
scale hit size/count across brackets, not HP. Park, don't adopt:
elite Pierce N (deterministic and legal, but enemy-side and out of
slice scope).

**Contradicts locks:** Kimi's conditional-% relic and per-hit-cap
relic = mitigation stages beyond armor, off the lean-seven sheet
(second-HP pools likewise — fine as enemy presentation only). GPT's
optional post-armor % buff layer = the same soft conflict. Neither
engine's core recommendation violates the hard exclusions or
determinism; both floors satisfy no-immunity-cliffs by construction.

**Trust:** the engines contradict each other on RotMG's floor
constant — don't cite it. GPT grades its own source confidence
(good); Kimi asserts specifics on dangling footnotes.

### A.2 Movement-speed itemization (feeds block 6)

Sources: `gpt-sol-pro/movement-speed.md` ·
`kimi-agent/movement-speed/Movement-Speed Itemization in
Pure-Movement Dodging Games.md`

**GPT says:** speed is contained by MECHANISM, not tuning: RotMG's
affine formula (nonzero intercept = a free soft cap — a 50% stat gap
compresses to ~24% real speed), Gungeon's encounter-local caps,
Nuclear Throne's structural scarcity (ONE +12.5% item in the game),
Touhou's no-speed-loot purity pole. Recommends class bases 105–115%
of slowest; items +5–15%; a hard clamp at 140% applied AFTER all
modifiers; formal dodgeability = reachability/safe-set proofs at the
floor, at SEQUENCE level (patterns A+B jointly, not separately);
perturbation suite (−5% speed, +10% hitbox, −100 ms telegraph);
telegraph budgets 250–300 ms simple / 500–700 ms arena-crossing.

**Kimi says:** "+speed is the single most dangerous stat to
itemize — simultaneously defense, mobility, and encounter-skip."
Deep RotMG anatomy: endgame consensus settles at ~110% of slowest
(micro-dodging beats speed); Potion of Speed = the game's
most-consumed item (speed-as-tax evidence); ADMITTED inescapable
beam-wall overlaps shipped (the ensemble failure). Cross-genre cap
table (D3 itemized cap +25%; "caps that live only in the item
spreadsheet will leak" — Nova Drift). Margin math:
`M(v) = T_w − (R+L) − d/v`, dM/dv = d/v² — sharply diminishing.
Recommends spread ≤1.12×, itemized ≤1.40×, hard-clamp computed
velocity IN THE MOVEMENT INTEGRATOR, freeze v_min as a design
constant forever, proofs over all phase ALIGNMENTS.

**Convergence:** narrow class spread (~10–15%) · gear speed small
and rare · ONE hard clamp in movement code applied last · travel
speed = separate out-of-combat axis · faster ≠ easier (overshoot
kills gap-threading) · per-pattern proofs are INSUFFICIENT —
sequences/alignments must be verified (both derive this
independently). They diverge on the cap number (140 / 135–150) and
on buff/dash layers we don't have.

**Applies to Wildshot:** our ~10% class spread is validated by both
bands. Our +15% cap is TIGHTER than either engine recommends — and
should STAY: their higher caps exist to preserve loot-feel under
buff/dash layers we don't have, and their own evidence (RotMG ~110%
consensus, D3's +25% itemized cap, dM/dv = d/v²) says speed above
the floor buys comfort, not access; a tighter cap = cheaper proofs
+ less pattern trivialization. Direct pickups for block 6 + the
DodgeBot spec: the margin receipt
`M(v_min) = T_w − (R+L) − d/v_min ≥ buffer` (R≈0.25 s human
reaction, L≤0.1 s latency, buffer 0.15–0.5 s) as a per-pattern
acceptance artifact; the telegraph budgets; the perturbation suite;
sequence/alignment proofs (RotMG's inescapable overlaps = the
shipped counterexample); the clamp lives in the movement
integrator; chaser enemies stay slower than the slowest base; build
base difficulty from speed-INsensitive pattern families (aimed
streams/spirals/zones), reserve gap-walls as deliberate checks;
NEVER let speed convert to damage. If slows ever enter the game the
floor proof re-runs at the new floor — a new proof lane, designer
decision, not slice scope.

**Contradicts locks:** GPT's dash budget (160–200% instantaneous)
and Touhou-style focus mode; Kimi's burst-mobility layer (~2×,
citing a dash-with-iframes approvingly) — all violate movement-only
dodging / no iframes. GPT's rational diminishing-returns curve
fails tooltip-computable (it concedes this). Both engines' sustained
buff layers sit outside the lean-seven sheet. Kimi's slow-debuff
designs break the floor proof unless re-proven (it says so itself).
Netcode/anti-cheat sections inapplicable (local deterministic sim).

**Trust:** GPT's citations unresolvable BUT its numbers match
Kimi's independently sourced ones almost exactly — good
corroboration. Kimi's own cap recommendation is undercut by its own
evidence and never reconciled. Both correctly discount Gungeon
(iframe dodge carries its defense — weak comparator for us).

### A.3 Behavioural skill trees (feeds blocks 5/7; tree design itself = slice-build territory)

Sources: `gpt-sol-pro/skill-trees.md` ·
`kimi-agent/skill-trees/Behaviour-First Skill Tree Design - Survey
and 30-Node Blueprint.md`

**GPT says:** behaviour-first = nodes change targeting / cadence /
resource flow / hit consequences / skill relationships — never
"+more damage" in flavors. Surveys PoE keystones (~3% of tree =
behaviour), Last Epoch (39–59%), Hades (~80%). Recommends 30 nodes
at 17 behaviour / 13 support; a finished build carries only 3–5
ACTIVE behaviour changes. Ships three complete 30-node example
trees — genuinely clean of crit/proc/RNG — plus a 12-axis behaviour
taxonomy, a per-node compatibility contract
(Replaces/Preserves/Suppresses/Triggers), and a 13-trap table.

**Kimi says:** build identity lives in **2–4 pivotal picks**; ratio
anchors : synergists : conditionals ≈ 20:55:25; the "verb test" (a
node is behaviour only if it changes what you press, when, where
you stand, what you target, or how resource flows — otherwise it's
"+% in a trench coat"). Wider 12-game survey (Balatro's ≤3-lines
rule; WoW-Cataclysm as the negative control). Blueprint: 5 anchors /
3 exclusive converter pairs / flow + trigger + resource layers / 2
capstones take-≤1; tiers gated by POINTS INVESTED, not geography;
4–8 feel-distinct builds per class. Strongest original idea:
classes differ GRAMMATICALLY — one resource-engine class, one
flow/geometry class, one conversion/trigger class. Rule worth
framing: "if every build takes it, make it baseline."

**Convergence:** identity = few picks (3–5 / 2–4) — the transferable
core; anchors orthogonal with real costs; no travel/path-tax nodes
in small trees; gate by investment, not geography; ~⅓ conditional
scaffolding; near-identical trap lists. The headline ratio clash
(57% vs ~20% behaviour) is mostly DEFINITIONAL — Kimi's middle
layers count as behaviour under GPT's test; quote neither number
without its definition.

**Applies to Wildshot:** the slice bill says SIMPLE trees and gear
is the build system — so we adopt the principles and REJECT both
node budgets. Scaled-down shape both engines' logic supports:
~12–18 nodes/class, 2–3 genuine behaviour anchors each (binary
exclusive pairs = the cheapest implementation), the rest small
conditional supports — still yields 3–4 recognizable variants per
class. Kimi's grammar-per-class maps straight onto our block-5
identity lean: sword = guard/hit-consequence grammar, bow =
projectile-geometry/cadence grammar, staff = resource-engine
grammar — identity without touching the power share. For block 5:
"if every build takes it, make it baseline" IS the argument for
levels carrying HP/mana while trees carry only choices —
structurally protects gear-primacy. For block 7: Kimi's six
grammars (conversion / flow / inversion the safest three) = a ready
vocabulary; GPT's compatibility contract = the determinism
constraint expressed as documentation discipline — adopt when nodes
get written at slice build. Both engines' "screenshot test" (a node
you can't SEE in play fails) is our behaviour-communicated law
restated. GPT's three trees are a legal idea-quarry for node
writing later (returning projectile + catch window, every-Nth-shot
line attack, visible fuses, barrier-catches-projectiles).

**Contradicts locks:** BOTH engines assume the tree IS the build
system — gear-primary says no; principles yes, counts no. Survey
material is saturated with crit/evasion/proc nodes (Resolute
Technique, Second Sight, chance-to-bleed, Snecko Eye) — none
importable (hard exclusions + no dice). Dash/blink/backflip nodes
violate movement-only dodging; any speed or range node must clear
CORE-33 — neither document knows that constraint exists. Their
point budgets (~20 points on 30 nodes) are theirs, not ours —
block-5 territory.

**Trust:** GPT self-flags its behaviour-share percentages as
estimates; its 17/13 ratio is asserted, not derived. Kimi's
20:55:25 is pattern-matched, not counted (its own Hades arithmetic
gives ~35%); real URLs but weak sources among them. Both unusually
honest about their own uncertainty.

### A.4 Gear-tier + XP pacing (feeds blocks 4/5/9)

Sources: `gpt-sol-pro/gear-xp-pacing.md` ·
`kimi-agent/gear-xp-pacing/ARPG_Gear-Tier_and_XP_Pacing_Guide.md`

**GPT says:** decompose loot into volume × tier composition. XP:
smooth geometric ~×1.12/level (~21,450 total to 30; ~11 h campaign;
6→35 min/level, resetting slightly downward at zone entries).
Tiers: logistic onset + exponential retirement with a zone-entry
shock; ship table Z1 95/5/0/0 → Z4 1/4/28/67 (current-tier plateau
58–67%; next-tier teaser 4–5% in a zone's final third). Cadence:
meaningful upgrade every 35–70 min by zone, 14–18 per campaign
("meaningful" = +8–12% damage or +6–10% survivability). Tier power:
+18%/tier base index; full-item gain **15–22%**.

**Kimi says:** XP flat-per-zone, STEPPED ~×2.2 at boundaries
(50–150 / 400 / 800 / 1,400 per level; ~22,000 total; ~9.4 h) —
"nobody successful uses a single clean curve"; tune
kills-per-level (~45 trash/level) and back-solve mob XP. Tiers: a
trapezoid per tier vs distance-from-home-zone — sealed → preview
3–8% → plateau ~55% (deliberately never >60%, D2's below-max bias)
→ legacy taper. Power: weapon damage **×1.7/tier**; player HP
100→700; **trash hits-to-kill invariant 3–5 at ALL 30 levels**
(back-solve enemy HP from intended fight length); all frequent
combat numbers ≤3 digits. Cadence: ~12 felt upgrades/campaign; the
zone boss is the TIER ANCHOR (first kill guarantees a current-tier
piece).

**Convergence:** one tier per zone, T1–T4 = zones 1–4 — both;
current-tier plateau capped ~55–67%, never 100% — both; next-tier
preview late in the prior zone — both; legacy taper, never a
cliff — both; zone-boss first-clear guarantees a current-tier
piece — both; fix cadence via COMPOSITION, never raw drop volume —
both; pick time-per-level first and back-solve XP — both. THE
genuine disagreement: tier step 15–22% (GPT) vs ×1.7 weapon
(Kimi) — 3× apart; Kimi's argument (few tiers ⇒ chunky or
invisible) is the one aligned with the ruled taste.

**Applies to Wildshot:** block 5 — Kimi's flat-per-zone stepped XP
family fits our zone-authored brackets best and is
tooltip-computable ("this zone asks 400/level, pays 9/kill"); GPT's
smooth ×1.12 is the named fallback. Level-vs-gear share — Kimi's
budget (weapons ~×5 over the campaign vs levels ~×3, levels
carrying HP) is the closest evidence for our ⅓-levels / ⅔-gear
lean. Block 4 — our +35–40% lean sits BETWEEN the engines and reads
as safe; Kimi's logic suggests deliberate asymmetry: the weapon
slot carries the big tier step, armor/accessories take half-steps
(RotMG's asymmetric tier spreads). T5's seam gets named: late Snow
Country (~L28+) as boss/dungeon-anchored capstone pieces — a
concrete option for the open T5 call. Cadence — ~12–18 felt
upgrades per campaign, ~1 per 1.5–2.5 levels, schedulable
DETERMINISTICALLY via quest/boss/dungeon beats (authored placement
replaces pity RNG; worst case bounded at ≤ one boss kill per zone).
Block 9 — adopt as calculator assertions: trash hits-to-kill 3–5 at
every band; boss TTD anchored to the biggest telegraphed hit vs the
visible HP bar; ≤3-digit frequent values; GPT's acceptance criteria
(median time-to-first-current-tier-item after zone entry, etc.)
convert cleanly into checks.

**Contradicts locks:** BOTH engines' zone brackets are
1–7/8–14/15–21/22–30 — ours are RULED 1–7/8–15/16–22/23–30; shift
every quoted level-indexed table. Both are RNG-itemization
end-to-end (droprates, pity timers, roll variance) — the MECHANISMS
don't survive our determinism; the TARGETS do (authored drops hit
the same cadence bands). GPT assumes a crafting economy, Kimi a
vendor/gambling economy — neither is in scope. GPT's 15–22% step
undershoots the ruled "chunky, felt steps" taste. Slot counts
(GPT 8, Kimi 6) are theirs — block 4 redoes per-slot math against
our actual loadout. Neither models a 3-class base-curve split.

**Trust:** GPT explicit that its tables are
reconstructions/engineering targets (good). Kimi has real URLs but
weak sources and arithmetic wobbles (its zone XP sums don't quite
reconcile — don't quote its cumulative totals unchecked; its
per-tier percentage math DOES check out). Strongest signal = the
independent convergences listed above.

### A.5 Evergreen boss uniques (feeds block 8)

Sources: `gpt-sol-pro/boss-uniques.md` ·
`kimi-agent/boss-uniques/boss-unique-item-design.md`

**GPT says:** a boss unique is a persistent OPTION, not a superior
item. Central pattern, near-verbatim to our draft: "break exactly
one normal equipment or combat rule, grant a conditional advantage,
and charge an explicit cost." Split budgets: the unique's chassis
runs at 70–92% of the slot budget — the break is the premium.
Envelope: 90–98% of regular gear in ordinary play, 105–115%
in-niche; ~60% broad adoption = the alarm threshold; nerf
coverage/cost before identity; fix the weak ladder before nerfing
the unique (RotMG Enforcer). Plus a 5-question tooltip contract and
a 12-item / 4-zone illustrative library, each item breaking exactly
one rule.

**Kimi says:** uniques sell VERBS, the ladder sells numbers; flat
capabilities are inflation-immune (RotMG's Oreo unchanged since
2010), fixed-stat premiums expire ("denomination error"). Twelve
"ladder laws" as a CLOSED menu of legal breaks — zero breaks =
trash, two = unpriceable → mandatory. Anatomy per item: chassis /
break / cost / echo — the "souvenir principle": the unique
re-performs its boss's own mechanic. Tuning identity **f × a ≈ k**
(niche frequency × in-niche advantage held roughly constant across
the roster). The cost must be paid IN PLAY, taxing the same axis as
the benefit (Enigma/Melding lessons); no content gating
(Gjallarhorn's LFG walls).

**Convergence:** exactly-one-rule-break as THE doctrine — both,
independently. Tiered gear stays the unconditional numeric
baseline — both. Visible, always-paid cost — both. The same
frequency × magnitude budget identity in different notation — both.
The ~60% adoption alarm — both. They even invented nearly the same
item twice (an information-lens unique). Diverge on the evergreen
mechanism (GPT: sublinear scaling curves; Kimi: flat capabilities /
percent-of-own-investment) and on roll pools (GPT endorses;
determinism forbids).

**Applies to Wildshot:** block-8 recommendation CONFIRMED twice,
once nearly verbatim. Upgrades worth bringing to the talk:
(1) enumerate the ladder's actual rules (they fall out of blocks
4 + 7) and make the whitelist the closed COMPLEMENT of them —
Kimi's twelve-law menu is the template; our four draft categories
map onto it cleanly. (2) Each law broken AT MOST ONCE game-wide in
the slice — cheap discipline that stops any rule being effectively
repealed; supports ~8–12 slice uniques, matching the bill (1–3
world bosses/zone + 4 dungeon bosses). (3) The chassis-fraction
rule — a unique pays ~8–30% of its slot budget for its break —
plugs directly into block-4 tables and is simpler than scaling
curves at a 30 cap. (4) The souvenir principle = free flavor +
tutorialization for our zone bosses. (5) f × a as a spreadsheet
check: narrow niche ⇒ big edge, broad niche ⇒ sliver. One designer
question surfaced for the talk: is mid-fight gear swapping
intended? Kimi argues cheap swapping is load-bearing for
situational uniques; if swapping is costly, niches must widen.

**Contradicts locks:** GPT's roll pools (compatibility randomness)
die to determinism — the underlying principle (many uniques serving
different builds) survives without rolls. GPT's survey vocabulary
(crit echoes, proc chains, internal cooldowns, accuracy/resist
costs) is hard-excluded; the structural advice (cap interaction
surfaces, no recursive triggers) survives deterministically.
Low-health-payoff designs skirt the sustain exclusion's intent —
designer vets case by case. Kimi's projectile-curving-aura example
needs vetting against readable movement-only dodging before any
import. Both frameworks assume live-ops retuning — for us those
become design-review checklists, not patch plans.

**Trust:** the mildest contamination of the five topics; the
engines corroborate each other on every shared case. Kimi's
f × a ≈ k is an asserted heuristic, not an empirical law (its
worked numbers are invented illustrations); GPT self-flags its
guardrail numbers as starting targets. Same citation caveats as
A.0.
