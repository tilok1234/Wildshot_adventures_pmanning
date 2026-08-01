# Damage Mitigation in Top-Down Action RPGs and Bullet-Hell Hybrids

## Executive Summary

Armor systems in action RPGs generally fall into four families: **flat subtraction**, **direct percentage reduction**, **rating-to-percentage conversion**, and **hybrid or hit-size-dependent formulas**. Each solves a different design problem.

Flat subtraction is the most readable at small numbers. In *Realm of the Mad God*, each Defense point subtracts approximately one point from an incoming hit, subject to a 15% minimum-damage floor; in *Vampire Survivors*, Armor subtracts one damage per point but cannot reduce a hit below one. These systems make an upgrade such as “+3 Armor” immediately understandable, but they strongly favor protection against many small projectiles and become proportionally weak against large attacks. The damage floors in both games are safeguards against complete immunity to weak enemies. *Realm of the Mad God*’s exact current calculation is not clearly documented by its present developer, so its formula should be treated as well-established legacy/community documentation rather than a current official specification. citeturn10view9turn4search0turn4search3

Direct percentage reduction, exemplified by Hades’s 30% Sturdy effect, is consistent across attack sizes: a 30% reduction is equally valuable against a 10-damage projectile and a 100-damage slam. Hades combines multiple reductions multiplicatively rather than additively, preventing ordinary stacking from reaching effortless 100% immunity. Percentage reduction is easy to explain when it is already displayed as a percentage, but less satisfying when equipment contains small integer “Armor” ratings that must be converted through an invisible curve. citeturn11search2turn11search5

Rating systems such as *Diablo III* convert Armor into damage reduction through a rational function. Its documented armor equation is

\[
R_{\text{armor}}=\frac{A}{A+50L},
\]

where \(A\) is Armor and \(L\) is attacker level. This gives smooth diminishing displayed returns, supports enormous item-stat ranges, and makes percentage immunity unreachable through Armor alone. It is poorly matched to a deliberately small-number system unless the denominator is also made small and the tooltip performs the conversion for the player. The level term also means that the same visible Armor number does not always represent the same protection. citeturn10view5turn5search6

Hybrid systems can solve specific balance problems but are harder to communicate. *Grim Dawn* lets armor cover up to the armor value while absorbing only a fraction—70% by default—of the covered portion. *Path of Exile* has used a hit-size-dependent rational formula in which armor becomes less efficient against larger individual hits; its official 3.16-era form made 50% mitigation require armor equal to five times the incoming physical hit. Grinding Gear Games explicitly changed the formula because low-to-medium armor investment was insufficient, illustrating the central risk of a formula whose result depends on both armor and hit size. citeturn10view4turn9view2

For the proposed game—a deterministic, no-crit, no-evasion system with double-digit values—the strongest default is:

\[
\boxed{T=\max\left(\left\lceil0.25D\right\rceil,\;D-A\right)}
\]

where \(D\) is raw hit damage, \(A\) is Armor, and \(T\) is final damage. This is **flat subtraction with a 25% minimum-damage floor**. It preserves the statement “1 Armor prevents 1 damage,” prevents immunity to low-level projectiles, and makes every equipment number meaningful without requiring players to understand a curve.

A strong alternative, particularly if attacks span a much wider size range, is:

\[
\boxed{T=\left\lceil D\frac{20}{20+A}\right\rceil}
\]

equivalent to \(R=A/(20+A)\). Here, 10 Armor means 33% reduction, 20 means 50%, 40 means 67%, and 60 means 75%. This is less mentally transparent than flat subtraction, but it treats small and large hits consistently and has a useful mathematical property: every 20 Armor adds one base-health-bar’s worth of effective health.

Because target platform, long-term level scaling, healing availability, and intended combat pacing are unspecified, the recommended constants should be treated as prototype baselines. Flat subtraction is preferable if ordinary raw hits remain approximately 8–60 and projectile frequency is deliberately controlled. The rational rating model is safer if late-game hits may become several times larger than early-game hits or if the game must support long progression without replacing every armor number.

## Scope, Terminology, and Evidence Quality

This report distinguishes **raw hit damage** \(D\), **Armor or Defense rating** \(A\), **fractional damage reduction** \(R\), and **final damage taken** \(T\). Unless otherwise stated, formulas describe one hit before health loss, barriers, invulnerability, or post-hit healing.

“Defense” is not consistent terminology across games. Most importantly, *Diablo II*’s ordinary Defense stat does **not** reduce damage. It modifies the attacker’s chance to hit according to an Attack Rating, Defense, and level formula, with the result bounded between 5% and 95%. Its actual physical damage mitigation comes from separate “Damage Reduced by X” and “Damage Reduced by X%” modifiers. Because the proposed system has no evasion or miss chance, *Diablo II* Defense itself is not an appropriate model; its separate flat and percentage damage-reduction modifiers remain relevant. citeturn2search0turn10view7

The simplified *Diablo II* physical mitigation relationship can be represented as:

\[
T\approx \max(0,D-F)(1-P),
\]

where \(F\) is integer physical damage reduction and \(P\) is percentage physical damage reduction. The full game has additional ordering interactions—including shields, skills, resistances, and debuffs—so this expression should be understood as a model of the flat-plus-percent portion, not a complete combat pipeline. Percentage physical reduction is capped at 50% under ordinary conditions, while integer reduction is applied as a fixed amount and is consequently much weaker against very large hits. citeturn10view7turn2search19

The quality of formula documentation varies by game:

| Game | Documentation status used here | Confidence and caveat |
|---|---|---|
| *Grim Dawn* | Official combat guide | High confidence; the guide gives numeric armor examples and default absorption. citeturn10view4 |
| *Path of Exile* | Official developer manifesto and historical official mechanics post | High confidence for the cited versions. The game has changed formulas over time, so the 3.16-era equation is presented as a documented design case, not guaranteed to describe every current mode or sequel. citeturn9view2turn9view3 |
| *Diablo III* | Widely accepted formula documentation and Blizzard community references | High confidence in the established equation; the accessible sources are not a current in-client specification. citeturn10view5turn5search6 |
| *Hades* | Authoritative community documentation, supported by official patch notes for the underlying effects | High confidence in the listed effects; Supergiant’s patch notes mention Sturdy changes but do not provide a complete mathematical combat manual. citeturn11search2turn3search4 |
| *Vampire Survivors* | Established community wiki documentation | Good practical confidence, but no complete official developer formula reference was found. citeturn4search0turn4search5 |
| *Realm of the Mad God* | Legacy wiki/community documentation and preservation of older official material | Formula is well established, but an unambiguous current official formula page was not found. Exact rounding and edge-case order should therefore be treated as implementation-dependent. citeturn10view9 |
| *Diablo II* | Official Arreat Summit material for Defense and authoritative community references for damage-reduction ordering | High confidence in the distinction between avoidance-oriented Defense and separate flat/percentage mitigation. citeturn2search0turn10view7 |

For small-number analysis, “small” means ordinary raw hits are generally in the **8–60 damage** range and armor values fit in one or two digits for most of the game. This is not how every cited game is numerically scaled; the formulas are being examined independently of their original magnitude.

Rounding matters disproportionately in such a range. A theoretical result of 6.1 and one of 6.9 both becoming 7 creates visible plateaus, while rounding down can accidentally make weak attacks harmless. The recommended implementations therefore perform calculations at full precision and apply **one final ceiling operation** to damage taken. This preserves the promise that a nonzero successful hit normally deals at least one visible point and avoids order-dependent intermediate rounding.

## Flat Subtraction Models

The general flat-subtraction model is:

\[
T=\max(M,D-A),
\]

where \(M\) is a minimum-damage floor. The floor may be an integer such as one damage, a fraction of the original hit, or zero if complete negation is permitted.

### Realm of the Mad God

The commonly documented *Realm of the Mad God* model is:

\[
T=\max(0.15D,\;D-\mathrm{DEF}),
\]

subject to the game’s integer handling. Each Defense point removes one damage until the result reaches approximately 15% of the attack’s original damage. A 100-damage attack against 100 Defense therefore still deals approximately 15 damage rather than zero. The currently accessible explanation is community-hosted legacy documentation associated with material preserved from the old RealmEye and WildShadow-era knowledge base, rather than a current official Deca formula page. citeturn10view9

At double-digit values, the mechanic is exceptionally legible. Before rounding:

| Raw damage | Defense | Subtraction result | 15% floor | Damage taken |
|---:|---:|---:|---:|---:|
| 12 | 3 | 9 | 1.8 | 9 |
| 12 | 10 | 2 | 1.8 | 2 |
| 12 | 15 | –3 | 1.8 | Approximately 2 after suitable rounding |
| 24 | 6 | 18 | 3.6 | 18 |
| 24 | 20 | 4 | 3.6 | 4 |
| 40 | 34 | 6 | 6 | 6 |

Its likely design value is visible directly in play: a player can compare projectile damage with Defense and predict the result without calculating percentages. No public designer statement establishing that rationale was found, so this is an inference from the mechanic rather than a claimed developer explanation. The proportional floor also ensures that every attack retains some identity; a nominally dangerous projectile cannot be turned into a universal one-damage ping merely by exceeding its damage with Defense. citeturn10view9

The main balance consequence is that Armor’s value is proportional to **hit count**, not merely total raw damage. Against ten 8-damage bullets, 3 Defense can prevent up to 30 total damage. Against one 80-damage hit, it prevents only 3. That asymmetry can be desirable in a bullet-hell game—Armor becomes the defense against chip damage while movement remains the answer to telegraphed heavy attacks—but it must be intentional.

### Vampire Survivors

The documented *Vampire Survivors* relationship is effectively:

\[
T=\max(1,D-A).
\]

Armor reduces incoming damage by one per point, but a successful damaging contact cannot be reduced below one. The Armor passive grants one point per level, and the persistent Armor power-up likewise provides fixed integer mitigation, making the stat’s meaning unusually direct. citeturn4search0turn4search3turn4search5

For a 12-damage contact:

| Armor | Damage taken |
|---:|---:|
| 0 | 12 |
| 1 | 11 |
| 3 | 9 |
| 5 | 7 |
| 10 | 2 |
| 15 | 1 |

This approach is highly readable because no attack-specific percentage needs to be shown. It is also naturally useful in a game where the player is repeatedly contacted by crowds and where many damage events can occur over a short period. The one-damage floor is critical: without it, enough Armor would allow the player to ignore entire classes of enemies. citeturn4search0turn4search4

The weakness is that the difference between 10 and 11 Armor may become literally irrelevant against an enemy already hitting the one-damage floor. A player can equip a visibly larger number and receive no benefit in the current encounter. This is not merely an abstract issue; every minimum-damage flat system necessarily develops floor plateaus once \(A\ge D-M\).

### Diablo II’s Integer Damage Reduction

*Diablo II* supports fixed “Damage Reduced by X” as a separate modifier from its Defense stat. This is also flat subtraction, but it coexists with percentage physical damage reduction and a complicated mitigation pipeline. Authoritative guides emphasize that integer reduction can be useful against frequent small physical hits but is low-value against sufficiently large attacks because it removes the same amount regardless of hit size. citeturn10view7turn2search19

That distinction produces a useful general rule:

\[
\text{Relative reduction from flat armor}=\frac{A}{D}
\]

until a floor or zero is reached. Six Armor prevents 50% of a 12-damage hit, 25% of a 24-damage hit, and only 15% of a 40-damage hit. If enemy damage rises faster than obtainable Armor, flat Armor becomes progressively less relevant at high tiers.

The reverse is equally dangerous. If Armor rises faster than ordinary damage, entire enemy families collapse to the minimum floor. Flat subtraction therefore requires much tighter coordination between enemy damage ranges, hit frequencies, and equipment progression than percentage mitigation.

## Percentage and Rating Models

A direct percentage system uses:

\[
T=D(1-R).
\]

If multiple reductions stack multiplicatively:

\[
T=D\prod_i(1-R_i),
\]

and the combined reduction is:

\[
R_{\text{combined}}=1-\prod_i(1-R_i).
\]

### Hades

Hades uses direct percentage modifiers rather than a general visible Armor rating. The Sturdy status provides 30% damage reduction, so its pre-rounding relationship is:

\[
T=0.70D.
\]

A 12-damage hit becomes 8.4 before rounding, 24 becomes 16.8, and 40 becomes 28. The percentage is equally meaningful against each hit size. citeturn11search2turn11search4

Multiple Hades reductions combine multiplicatively. A 10% reduction followed by a 30% reduction yields:

\[
T=D(0.90)(0.70)=0.63D,
\]

or 37% total reduction—not 40%. This prevents straightforward additive stacking from reaching or exceeding 100%, while still letting every additional source contribute. citeturn11search5

God Mode is another instructive percentage design. It begins with 20% damage reduction, increases by two percentage points after each death, and caps at 80%. Functionally, this is an adaptive difficulty-assistance system rather than an equipment-stat curve: the player can understand the displayed percentage, while the cap preserves some danger. citeturn11search1

Direct percentages are most readable when the item itself says “15% less damage.” They are less elegant if an item instead says “+4 Armor” and the player must infer that four Armor corresponds to, for example, 17% reduction. In a small-number system, direct percentages also cause frequent rounding plateaus:

| Raw hit | 10% less, rounded up | 20% less, rounded up | 30% less, rounded up |
|---:|---:|---:|---:|
| 8 | 8 | 7 | 6 |
| 12 | 11 | 10 | 9 |
| 16 | 15 | 13 | 12 |
| 24 | 22 | 20 | 17 |

On an 8-damage hit, 0% and 10% both display as 8 if final damage is rounded upward. The modifier is mathematically active but locally invisible. Tooltips should therefore show both the percentage and at least one evaluated example.

### Diablo III’s Armor Rating

*Diablo III* converts Armor into percentage reduction using:

\[
R_{\text{armor}}=\frac{A}{A+50L},
\]

which is equivalent to:

\[
T=D\frac{50L}{A+50L}.
\]

Elemental resistance uses the analogous formula:

\[
R_{\text{resist}}=\frac{R}{R+5L}.
\]

Armor and resistance reductions then multiply rather than add. At level 70, the published example of 10,000 Armor and 1,000 resistance gives approximately 74% reduction from each layer and approximately 94.5% combined reduction. citeturn10view5turn5search6

The armor curve has clear landmarks:

\[
A=25L \Rightarrow 33.3\%\text{ reduction}
\]

\[
A=50L \Rightarrow 50\%\text{ reduction}
\]

\[
A=100L \Rightarrow 66.7\%\text{ reduction}
\]

\[
A=150L \Rightarrow 75\%\text{ reduction}.
\]

The formula prevents Armor alone from mathematically reaching 100% reduction, and each additional point produces a smaller increase in the displayed percentage. It also normalizes mitigation by attacker level, allowing the game to use escalating Armor numbers while reducing the effectiveness of unchanged old equipment against higher-level enemies. That rationale is an inference from the equation and progression structure; the cited sources document the formula but do not provide a complete original designer rationale. citeturn10view5

For a small-number game, the same shape can be retained without the scale. Replacing \(50L\) with a constant \(K\) gives:

\[
R=\frac{A}{A+K}.
\]

This formula has an especially useful property:

\[
\text{Effective-health multiplier}
=\frac{1}{1-R}
=\frac{A+K}{K}
=1+\frac{A}{K}.
\]

Although the displayed reduction has “diminishing returns,” effective health grows **linearly** with Armor. With \(K=20\), every 20 Armor adds one additional base-health-bar’s worth of survivability:

| Armor | Reduction | Effective-health multiplier |
|---:|---:|---:|
| 0 | 0% | 1.0× |
| 5 | 20% | 1.25× |
| 10 | 33.3% | 1.5× |
| 20 | 50% | 2.0× |
| 40 | 66.7% | 3.0× |
| 60 | 75% | 4.0× |

This distinction matters when evaluating “diminishing returns.” The percentage number rises more slowly, but the survivability granted by equal chunks of Armor does not diminish under this exact curve.

The disadvantages are cognitive rather than primarily mathematical. “10 Armor” does not intrinsically tell the player “33% less damage,” and a level-dependent denominator makes the same Armor number context-sensitive. A tooltip must calculate the result, and a small-number game gains little from including attacker level unless long progression genuinely requires it.

### Percentage Stacking and Effective-Health Inflation

Percentage mitigation becomes increasingly powerful near the top of the range:

| Reduction | Damage taken | Effective-health multiplier |
|---:|---:|---:|
| 20% | 80% | 1.25× |
| 40% | 60% | 1.67× |
| 60% | 40% | 2.5× |
| 75% | 25% | 4× |
| 80% | 20% | 5× |
| 90% | 10% | 10× |
| 95% | 5% | 20× |

This convexity is a major source of late-game tuning pressure. Increasing reduction from 20% to 30% raises effective health from 1.25× to 1.43×, an increase of about 14%. Increasing it from 80% to 90% doubles effective health from 5× to 10×. If players can approach very high reduction, enemy damage must either escalate sharply or fail to threaten optimized builds.

*Diablo III*’s example of two roughly 74% layers producing approximately 94.5% combined reduction illustrates how multiplicative layers can still create very high aggregate survivability even though they do not add directly. The answer is not necessarily additive stacking; it is tighter control of the number, magnitude, and applicability of independent layers. citeturn10view5

## Hybrid and Nonlinear Models

### Grim Dawn’s Partial Flat Absorption

*Grim Dawn* combines an armor amount with an armor-absorption coefficient. Its official guide describes a default 70% armor absorption. Armor can cover damage up to the relevant armor value, but only the absorption fraction of that covered amount is actually prevented. A compact expression for the armor stage is:

\[
T=D-\alpha\min(D,A),
\]

where \(\alpha\) is Armor Absorption and defaults to 0.70. citeturn10view4

The official examples include a 100-damage hit against 50 Armor at 70% absorption:

\[
T=100-0.70(50)=65,
\]

and a 100-damage hit against at least 100 effective Armor:

\[
T=100-0.70(100)=30.
\]

The guide also explains that raising absorption multiplicatively—for example by 20% from the 70% default—produces 84% absorption, leaving 16 damage when the armor fully covers a 100-damage hit. citeturn10view4

At small values, 6 Armor with 70% absorption behaves as follows before final rounding:

| Raw damage | Covered damage | Prevented | Damage taken |
|---:|---:|---:|---:|
| 4 | 4 | 2.8 | 1.2 |
| 8 | 6 | 4.2 | 3.8 |
| 12 | 6 | 4.2 | 7.8 |
| 24 | 6 | 4.2 | 19.8 |
| 40 | 6 | 4.2 | 35.8 |

This hybrid prevents ordinary Armor from creating complete immunity because even fully covered damage leaks through according to \(1-\alpha\). It also allows two independent progression axes: “how much of the hit Armor covers” and “how efficiently covered damage is absorbed.”

That flexibility comes at a substantial readability cost. “6 Armor, 70% absorption” means “prevent up to 4.2 damage,” which is much less direct than either “prevent 6” or “take 30% less.” If both values appear on equipment, players must multiply them. If absorption is mostly fixed, the game could instead display the effective value directly—for example, “Blocks up to 4 damage per hit”—and keep the underlying coefficient out of the main tooltip.

### Path of Exile’s Hit-Size-Dependent Armor

The officially described *Path of Exile* 3.16-era relationship can be represented as:

\[
R=\frac{A}{A+5D},
\]

or:

\[
T=D\frac{5D}{A+5D},
\]

for the physical hit and Armor interaction documented in that balance change. Grinding Gear Games stated that the previous behavior left Armor insufficient at low-to-medium investment and changed the formula so that 10,000 Armor against a 2,000-damage hit would mitigate 50% rather than approximately 33%. Under the changed relationship, 50% mitigation requires Armor equal to five times the incoming hit. citeturn9view2turn7search1

The same Armor value consequently produces different percentages against different hits. With 60 Armor:

| Raw hit | Reduction | Pre-rounding damage taken |
|---:|---:|---:|
| 12 | \(60/(60+60)=50\%\) | 6 |
| 24 | \(60/(60+120)=33.3\%\) | 16 |
| 40 | \(60/(60+200)=23.1\%\) | 30.8 |
| 60 | \(60/(60+300)=16.7\%\) | 50 |

This gives Armor a deliberate identity: it is effective against small and medium physical hits but does not automatically solve giant slams. It also avoids the extreme microhit dominance of pure subtraction because the reduction is proportional rather than a fixed number over much of the range.

The cost is severe tooltip ambiguity. There is no single correct text such as “60 Armor = 50% less physical damage” without naming an assumed hit size. Older official *Path of Exile* mechanics documentation explicitly noted that exact armor reduction was difficult to know because the result depended on how much physical damage the enemy dealt; the older documented formula used an even harsher coefficient of 12 rather than the later value of five. citeturn9view3

For a game whose central promise is “every number is visible,” this is a poor default unless the UI shows an evaluated reference such as:

> **Armor 60**  
> 50% less from a 12-damage hit  
> 33% less from a 24-damage hit  
> 23% less from a 40-damage hit

That tooltip is accurate, but it is no longer quick.

A useful mathematical interpretation is that against extremely large hits, the absolute amount prevented approaches a constant. For:

\[
R=\frac{A}{A+cD},
\]

damage prevented is:

\[
D_{\text{prevented}}=\frac{AD}{A+cD}.
\]

As \(D\) becomes very large:

\[
D_{\text{prevented}}\rightarrow \frac{A}{c}.
\]

Thus, with \(c=5\), 60 Armor asymptotically prevents only about 12 damage from a sufficiently huge hit. This explains both the model’s protection against trivial-hit immunity and its tendency to feel ineffective against one-shot threats.

### Piecewise and Soft-Cap Formulas

A piecewise curve can preserve simple behavior in the normal range while limiting extremes. One example is:

\[
T=
\begin{cases}
D-A, & A\le 0.5D\\[4pt]
0.5D-0.5(A-0.5D), & 0.5D<A<1.25D\\[4pt]
0.125D, & A\ge1.25D
\end{cases}
\]

This gives full-value subtraction initially, half-value Armor after the first threshold, and a 12.5% floor. It provides explicit soft caps but is difficult to explain without exposing the breakpoints. Players may experience an upgrade changing from “one point prevents one” to “two points prevent one” at an arbitrary boundary.

A smoother alternative is a capped exponential:

\[
R=R_{\max}\left(1-e^{-A/K}\right).
\]

This approaches a chosen cap gradually, but neither its mental arithmetic nor its marginal value is transparent. It is appropriate when simulation smoothness matters more than hand calculation, not when tooltips and visible integer reasoning are central.

A rational soft cap is simpler:

\[
R=R_{\max}\frac{A}{A+K}.
\]

With \(R_{\max}=0.75\), reduction approaches but never reaches 75%. Unlike the uncapped rational model, however, effective health no longer grows linearly with Armor, and late Armor eventually becomes genuinely weak. A player may reasonably ask why 20 additional points barely change the displayed result.

The most readable “soft cap” is therefore usually not a curved formula at all, but a **plain formula plus an explicit floor or cap**:

\[
T=\max(fD,D-A)
\]

or:

\[
R=\min\left(R_{\max},\frac{A}{A+K}\right).
\]

The player can see exactly which rule is active.

## Failure Modes Observed in Shipped Games

| Failure mode | Mechanism | Real-game evidence | Design implication |
|---|---|---|---|
| Armor becomes negligible against high-tier hits | Flat reduction stays constant while damage rises | *Diablo II* integer damage reduction is documented as weak against large physical hits; *Path of Exile*’s developers also found low-to-medium Armor investment insufficient and increased the formula’s effectiveness. citeturn10view7turn9view2 | Keep enemy hit growth close to Armor growth, or add a percentage component. |
| Weak attacks become irrelevant | Flat Armor reaches zero or minimum damage | *Vampire Survivors* uses a one-damage minimum, and *Realm of the Mad God* uses an approximately 15% floor, both preventing complete negation. citeturn4search0turn10view9 | Use an explicit floor and communicate it. |
| Armor disproportionately counters bullet density | Flat reduction is applied separately to every hit | This follows directly from the per-hit formulas used by *Vampire Survivors* and *Realm of the Mad God*. citeturn4search0turn10view9 | Tune Armor against hits per second, not just average damage per second. |
| High reduction causes effective-health explosion | Effective health is \(1/(1-R)\) | *Diablo III* documentation gives an example where two roughly 74% reductions combine to approximately 94.5%, leaving only about 5.5% damage. citeturn10view5 | Keep total sustained mitigation near 70–75% unless enemy damage is designed for extreme multipliers. |
| Additive stacking reaches immunity | Percentages are summed rather than multiplied | Hades instead multiplies reductions, with 10% and 30% producing 37% total rather than 40%. citeturn11search5 | Multiply independent percentage layers or apply a hard cap. |
| Low-value armor tiers feel pointless | Early rating gains are too small or rounding hides them | Blizzard later adjusted a *Diablo IV* armor formula specifically to provide more reduction at lower Armor amounts. citeturn5search14 | Ensure the first ordinary upgrade changes a representative hit by at least one visible damage. |
| One defensive stat crowds out others | Armor covers too many damage types or scales more efficiently | Blizzard stated that *Diablo IV* Armor was also reducing elemental damage and was outperforming elemental resistances, prompting a redesign that separated the roles. citeturn5search0 | Give Armor a clear damage domain or ensure competing defenses have distinct advantages. |
| Mitigation depends on unknown attack size | Hit-size-dependent formulas lack one stable tooltip percentage | Official *Path of Exile* documentation has acknowledged that exact reduction is difficult to determine because it depends on incoming hit size. citeturn9view3 | Avoid such formulas when predictability is a primary product goal, or show multiple reference hits. |
| Debuffs create sudden one-shot cliffs | Reduction can cross through zero into vulnerability | In *Diablo II*, Amplify Damage can turn substantial positive physical reduction into negative resistance; documented examples show a nominal 500-damage hit becoming 750 after the debuff in relevant conditions. citeturn10view7 | Clamp vulnerability separately and preview debuffed effective mitigation. |
| Rounding makes upgrades appear broken | Several neighboring percentage results round to the same integer | This is inherent when applying percentages to double-digit hits. | Show calculated examples and round only once, at the end. |
| Level-scaled ratings invalidate a visible number | Denominator grows with attacker level | *Diablo III*’s Armor equation includes \(50L\), so unchanged Armor gives less reduction against higher-level attackers. citeturn10view5 | Omit level from the curve unless the tooltip recalculates for the current area or enemy. |
| Minimum floors cause upgrade plateaus | Once the floor is reached, further Armor does nothing against that hit | The one-point floor in *Vampire Survivors* and proportional floor in *Realm of the Mad God* necessarily produce this outcome. citeturn4search0turn10view9 | Show “at minimum damage” in combat comparison tooltips and maintain a mix of attack sizes. |
| Layer order becomes obscure | Flat, percentage, shields, and resistance apply in different stages | *Diablo II* has distinct flat and percentage reductions with ordering interactions, while *Grim Dawn* documents armor and later absorption stages separately. citeturn10view7turn10view4 | Keep the player-facing pipeline to one primary Armor operation plus at most one multiplicative temporary layer. |

The most dangerous failure for a small-number bullet-hell is **microhit dominance**. Suppose two encounters both deal 60 raw damage per second:

\[
10\text{ hits}\times6=60
\]

and:

\[
2\text{ hits}\times30=60.
\]

With 4 flat Armor and no floor interference, the first encounter falls to 20 damage per second, while the second falls to 52. Armor prevents 40 damage in one case and only eight in the other. This may be excellent if Armor is intentionally the “crowd/contact defense,” but disastrous if the encounters were intended to remain equally threatening.

The most dangerous failure for percentage Armor is **late-game compression**. At 75% reduction, a 40-damage hit becomes 10. If the player gains enough mitigation to reach 80%, it becomes 8—only two fewer visible damage, but effective health rises from 4× to 5×, a 25% survivability increase. Small displayed differences can conceal large balance changes.

The most dangerous failure for hit-size-dependent Armor is the **one-shot cliff**. Players may feel durable against all ordinary projectiles and then receive very little percentage reduction from a boss slam. *Path of Exile*’s official formula changes and historical explanation show that this is a known practical tension rather than merely a theoretical objection. citeturn9view2turn9view3

## Comparative Design Matrix

| Model | Core formula | Representative games | Typical scale or characteristic parameters | Advantages | Small-number readability | Principal failure modes |
|---|---|---|---|---|---|---|
| Pure flat subtraction with floor | \(T=\max(M,D-A)\) | *Vampire Survivors*: \(M=1\); *Realm of the Mad God*: approximately \(M=0.15D\). citeturn4search0turn10view9 | Armor should be on the same order as ordinary hit damage. Live examples use an absolute one-damage floor or 15% proportional floor. | Exact, tangible value per point; no conversion; excellent for double-digit hits; naturally differentiates chip damage from heavy attacks. | Excellent. “+3 Armor” normally means three less damage. | Overpowered against many microhits; weak against huge hits; floor plateaus; requires tightly controlled damage ranges. |
| Direct percentage reduction | \(T=D(1-R)\) | Hades Sturdy: 30%; God Mode: 20–80%. citeturn11search2turn11search1 | Individual effects commonly remain in legible percentage bands; cited Hades examples range from 20% to an 80% assistance cap. | Same proportional value against every hit; simple if shown directly as a percentage; easy to cap. | Good for percentages, mediocre for rating numbers; rounding is noticeable below about 20 damage. | High-end effective-health explosion; additive-stack immunity; small upgrades can be invisible after rounding. |
| Rational Armor rating | \(R=A/(A+K)\) | *Diablo III*: \(K=50L\). citeturn10view5 | 50% at \(A=K\), 67% at \(2K\), 75% at \(3K\). *Diablo III* uses thousands of Armor at level 70 because \(K\) scales with level. | Smooth progression; no mathematical immunity; equal-sized Armor packages add equal effective health. | Good only if the tooltip displays converted reduction and example damage. | Rating number is not self-explanatory; level dependence can invalidate intuition; final integer rounding creates plateaus. |
| Partial flat absorption | \(T=D-\alpha\min(D,A)\) | *Grim Dawn*, with 70% default absorption. citeturn10view4 | Armor near the size of ordinary hits; \(\alpha=0.70\) by default in the cited implementation. | Avoids complete negation; supports separate capacity and efficiency progression; can distinguish armor quality. | Moderate to poor unless effective prevented damage is computed in the tooltip. | Two interacting stats; multiplication burden; low absorption can make nominal Armor values feel misleading. |
| Hit-size-dependent rating | \(R=A/(A+cD)\) | Officially documented 3.16-era *Path of Exile* form with \(c=5\). citeturn9view2 | 50% reduction at \(A=cD\); for the cited version, Armor must equal five times the hit. | Strong against ordinary hits without trivializing giant attacks; automatically resists immunity to weak physical hits. | Poor. A single Armor value has no single reduction percentage. | One-shot cliffs; opaque tooltips; players must know incoming hit sizes; low investment can feel worthless. |
| Flat then percentage layering | \(T=\max(0,D-F)(1-P)\), as a simplified sub-pipeline | *Diablo II* integer and percentage physical reduction. citeturn10view7turn2search19 | Percentage physical reduction ordinarily capped at 50%; integer reduction is independent of attack size. | Gives flat and percentage gear distinct niches; can support build specialization. | Moderate if order is explicitly shown. | Order sensitivity; combinatorial complexity; flat layer dominates microhits while percent layer dominates heavy hits. |
| Explicit piecewise soft cap | Full value below threshold, reduced value above it | General design alternative | Typical threshold near intended midgame Armor; second segment grants half or quarter value. | Precise control over breakpoints; protects the ordinary range while containing extremes. | Moderate if thresholds are displayed; poor if hidden. | Arbitrary-feeling breakpoints; upgrades change value unexpectedly; additional tooltip text. |
| Capped rational curve | \(R=R_{\max}A/(A+K)\) | General design alternative | \(R_{\max}\) often 70–80%; \(K\) controls midpoint relative to the cap. | Smooth, bounded, stable over long progression. | Poorer than uncapped rational because neither \(A=K\) nor another simple point means 50% total reduction unless explained. | Genuine late diminishing returns; high Armor upgrades can feel negligible. |

For this project’s stated priorities, the ordering is:

\[
\text{capped flat subtraction}
>
\text{small-scale rational rating}
>
\text{partial flat absorption}
>
\text{hit-size-dependent rating}.
\]

That order would change if the game had hundreds of levels, procedurally unbounded stat inflation, or highly variable attacker levels. Those conditions favor a rating curve. They have not been specified here.

## Recommended Models and Decision Framework

### Recommended Default: Capped Flat Subtraction

Use:

\[
\boxed{T=\max\left(\left\lceil0.25D\right\rceil,\;D-A\right)}
\]

with the following initial parameter envelope:

| Parameter | Prototype recommendation |
|---|---:|
| Ordinary enemy hit | 8–24 raw damage |
| Elite or telegraphed hit | 25–40 raw damage |
| Major boss hit | 40–60 raw damage |
| Early Armor | 0–5 |
| Midgame Armor | 6–12 |
| Late ordinary Armor | 13–20 |
| Exceptional temporary Armor | Up to approximately 30 |
| Minimum-damage floor | 25% of raw hit, rounded up |
| Final rounding | Ceiling after all continuous calculations |
| Permanent percentage layers | None, or at most one tightly capped secondary system |
| Temporary percentage effects | Multiply after Armor, not add to it |

The 25% floor is higher than *Realm of the Mad God*’s documented 15% floor and more proportional than *Vampire Survivors*’ one-damage minimum. The purpose is not to copy either game, but to preserve their readable one-for-one subtraction while reducing the size of immunity plateaus. Their floors demonstrate the same underlying safeguard in shipped games. citeturn10view9turn4search0

Worked results:

| Raw hit | 0 Armor | 3 Armor | 6 Armor | 10 Armor | 15 Armor | 20 Armor | 30 Armor |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 12 | 12 | 9 | 6 | 3 | 3 | 3 | 3 |
| 24 | 24 | 21 | 18 | 14 | 9 | 6 | 6 |
| 40 | 40 | 37 | 34 | 30 | 25 | 20 | 10 |

![Damage taken versus Armor under capped flat subtraction](sandbox:/mnt/data/capped_flat_damage_vs_armor.png)

This model makes equipment comparison unusually clear:

> **Iron Coat**  
> **+6 Armor**  
> Each hit deals 6 less damage.  
> A hit always deals at least 25% of its original damage.

A contextual comparison could read:

> **Equip Iron Coat**  
> Armor: 3 → 6  
> Typical 12-damage projectile: 9 → 6 damage  
> Heavy 40-damage attack: 37 → 34 damage

When the floor is already reached:

> **Armor 15**  
> A 12-damage projectile already deals its minimum: 3.  
> Additional Armor still protects against stronger hits.

That last line is important. Without it, a player may conclude that the stat is broken after observing no difference against a low-tier enemy.

The model’s central tuning metric should be **prevented damage per second**, not reduction percentage. For an attack pattern with hit rate \(h\):

\[
\text{maximum prevention per second}\approx hA
\]

before floor effects. A room firing eight projectiles per second makes each Armor point up to eight times as valuable as a boss attacking once per second. Encounter design should therefore classify attacks by frequency as well as damage:

| Attack family | Suggested raw damage | Expected Armor role |
|---|---:|---|
| Dense chip projectile | 8–12 | Armor is highly effective; movement errors remain survivable. |
| Standard aimed shot | 14–24 | Armor provides visible but incomplete protection. |
| Elite telegraph | 25–40 | Armor shaves damage but dodging remains the primary answer. |
| Boss slam or beam tick | 40–60 | Armor is helpful, not sufficient by itself. |
| Continuous hazards | Prefer slower discrete ticks | Avoid dozens of tiny ticks that make flat Armor either dominant or constantly floor-bound. |

A temporary “30% less damage” buff may be applied after Armor:

\[
T_{\text{buffed}}
=
\left\lceil
\max(0.25D,D-A)\times0.70
\right\rceil.
\]

The tooltip should state the order:

> Armor subtracts damage first. “Less Damage Taken” effects apply afterward.

Do not add many independent percentage layers. Hades and *Diablo III* show why multiplicative stacking is preferable to addition, but *Diablo III* also demonstrates that several multiplicative layers can still produce extremely high aggregate reduction. citeturn11search5turn10view5

### Recommended Alternative: Small-Scale Rational Armor

Use:

\[
\boxed{R=\frac{A}{A+20}}
\]

and:

\[
\boxed{T=\left\lceil D\frac{20}{A+20}\right\rceil}.
\]

Suggested parameters:

| Parameter | Prototype recommendation |
|---|---:|
| Curve constant \(K\) | 20 |
| Early Armor | 0–6 |
| Midgame Armor | 7–20 |
| Late Armor | 21–40 |
| Exceptional Armor | 41–60 |
| Content or displayed cap | Approximately 75%, reached at 60 Armor |
| Final rounding | Ceiling once, after all reductions |
| Level term | None |
| Other percentage reductions | Multiplicative, with total sustained reduction capped near 75% |

Key milestones are easy to memorize:

| Armor | Reduction |
|---:|---:|
| 5 | 20% |
| 10 | 33% |
| 20 | 50% |
| 40 | 67% |
| 60 | 75% |

Worked results:

| Raw hit | 0 Armor | 3 Armor | 6 Armor | 10 Armor | 15 Armor | 20 Armor | 30 Armor | 40 Armor | 60 Armor |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 12 | 12 | 11 | 10 | 8 | 7 | 6 | 5 | 4 | 3 |
| 24 | 24 | 21 | 19 | 16 | 14 | 12 | 10 | 8 | 6 |
| 40 | 40 | 35 | 31 | 27 | 23 | 20 | 16 | 14 | 10 |

![Damage taken versus Armor under a rational rating curve](sandbox:/mnt/data/rational_rating_damage_vs_armor.png)

Recommended tooltip:

> **Armor 10**  
> Take **33% less damage from hits**.  
> 12 damage becomes 8.  
> 24 damage becomes 16.  
> 40 damage becomes 27.

Comparison tooltip:

> **+3 Armor**  
> Armor: 10 → 13  
> Damage reduction: 33% → 39%  
> Typical 24-damage hit: 16 → 15

The additional example is necessary because “+3 Armor” has no invariant per-hit interpretation. Depending on current Armor and final rounding, it may change some hits but not others.

This alternative should be preferred when:

| Condition | Why rational Armor is safer |
|---|---|
| Late-game attacks may be five or more times stronger than early attacks | Flat Armor would either become obsolete late or overpowered early. |
| Projectile sizes vary greatly within the same encounter | Proportional mitigation keeps Armor relevant to every hit size. |
| Enemy hit frequency is difficult to normalize | Percentage reduction does not multiply its value by the number of hits in the same extreme way as fixed subtraction. |
| The game has substantial healing or life regeneration | A stable proportional reduction is easier to model against sustained recovery. |
| Equipment progression must continue for a long campaign | The curve accepts additional Armor without reaching mathematical immunity. |

Do not copy *Diablo III*’s level-scaled denominator for this project unless attacker level is a major, clearly surfaced mechanic. A constant \(K=20\) lets players retain an intuition for the stat throughout the game. *Diablo III*’s \(50L\) denominator serves a long-scaling loot system but makes Armor context-dependent. citeturn10view5

### Why the Path of Exile-Style Formula Is Not Recommended

A hit-size-dependent formula would preserve a distinction between chip damage and boss attacks, but flat subtraction already does that while remaining much easier to explain. The *Path of Exile* approach requires the player to know \(D\) before converting \(A\) into a percentage, and official documentation has acknowledged the resulting uncertainty. It also received a significant effectiveness revision because low-to-medium investment was underperforming. citeturn9view2turn9view3

It remains useful when the explicit design requirement is:

> Armor should be excellent against many ordinary physical hits but intentionally poor against giant physical hits, and players are expected to use another defense against slams.

That is a valid action-RPG niche. It conflicts with the stated goal of maximum predictability.

### Why the Grim Dawn-Style Formula Is a Secondary Option

The partial-absorption model is mechanically robust and can be simplified to:

\[
T=D-0.75\min(D,A).
\]

With a fixed 75% absorption coefficient, the system avoids total negation while giving Armor an approximately flat identity. However, if absorption never changes, the displayed Armor number is misleading: 8 Armor really prevents at most 6 damage. The game should either rename it “Armor Capacity” or display the effective value.

If absorption can change, the player now tracks two defensive numbers and their product. That is appropriate for a deep loot game like *Grim Dawn*, whose official combat guide exposes multiple defensive stages, but unnecessarily complex for a solo-developed system centered on readable tooltips. citeturn10view4

### Decision Flow

```mermaid
flowchart TD
    A[Are ordinary incoming hits mostly 8–60<br/>and individually readable?]
    A -- Yes --> B[Is “1 Armor = 1 less damage”<br/>a core player promise?]
    B -- Yes --> C[Capped flat subtraction<br/>T = max(25% of D, D − A)]
    B -- No --> D[Must Armor be equally relevant<br/>against small and large hits?]
    D -- Yes --> E[Rational rating<br/>R = A / (A + 20)]
    D -- No --> F[Partial-flat hybrid<br/>T = D − α · min(D, A)]
    A -- No --> G[Does the game have wide level scaling<br/>or large stat inflation?]
    G -- Yes --> H[Rating curve with a controlled K<br/>and evaluated tooltip examples]
    G -- No --> E
    C --> I[Apply temporary percentage effects<br/>multiplicatively after Armor]
    E --> I
    F --> I
    H --> I
    I --> J[Keep sustained total reduction<br/>near or below 70–75%]
    J --> K[Round only final damage<br/>and show representative hit previews]
```

The decisive question is not whether flat or percentage mitigation is universally superior. It is whether **hit frequency and hit size are intended to be separate defensive axes**.

Capped flat subtraction says:

> Armor is especially good against repeated small mistakes, but large telegraphed attacks remain dangerous.

Rational Armor says:

> Armor grants approximately the same proportional survivability against every ordinary hit.

For a bullet-hell hybrid with no evasion roll, no critical-hit variance, visible double-digit numbers, and a strong commitment to understandable tooltips, the first statement is usually the more distinctive and readable design. The second is the safer systems-engineering choice if future level scaling, enemy damage inflation, or combat pacing cannot yet be tightly bounded.