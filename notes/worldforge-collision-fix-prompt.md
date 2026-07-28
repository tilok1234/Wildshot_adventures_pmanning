# WorldForge agent prompt — porous structure collision fix (2026-07-28)

Handed to a designer-run agent in the WorldForge repo ~10:40. Recorded
here per cross-tool coordination discipline (doc 15; game ledger #15
holds the evidence). The consuming game repo committed the diagnostic
that must acquit the fix: `tools/diag_walkability_grid.py`.

---

Task: fix porous structure collision in WorldForge's game-pack export.

Orient in `C:\Users\headc\Documents\WorldForge` first (README/
conventions), find the game-pack exporter (produces manifest.json,
walkability.json, world.json, minimap.png, resolved/resolved-map.tmj,
validation-report.json). Deterministic export, repo conventions, no
touching the game repo.

Bug (verified consumer-side in the shipped dusk pack): buildings emit
POROUS collision — solid wall chunks with single-cell walkable slots
between segments (window/door columns) plus walkable lanes/pockets
behind and inside facades. Sample rows (one visually continuous
building each): `SS..P..SS.SS.SS` / `SSS.SSS.SS.SS` / `SSS.SS.S.SS`
(world rows 130/134/136, x≈234-247). The 0.7-tile player circle fits
every 1-wide slot: players slide inside building visuals, render on
top, snag on micro-geometry.

Fix intent: stamp each structure placement's FULL footprint
non-walkable (collision outline == art outline), doors included
(Phase A has no interiors). Do NOT stamp `props-overhang` cells
(awnings/eaves stay walkable; the game occludes players under them).
Implement where placements know their templates/footprints.

Format coupling to regenerate: floodCount = fresh flood fill from
spawnCell (spawn stays walkable + on the main region; streets stay
connected — an outsized flood drop = orphaned region, investigate);
manifest hashes; green validation-report; deterministic re-export.

Acceptance: (1) no walkable cell carries a structures tile or sits
enclosed in one placement's outline; (2) floodCount matches recompute;
(3) validation green + hashes consistent; (4) consumer spot-check from
the game repo: `python tools/diag_walkability_grid.py` over region
208-248 x 126-148 against the NEW pack shows closed solid blocks —
no `.` inside `S` runs. Optional separate commit: move roof-ridge/
chimney rows to `props-overhang` (the game renders overhang above
actors).

Hand-back: stage the revised `small-cold-coastal-pack-dusk` in this
repo's normal output location; report what changed, where stamping
lives now, new floodCount vs old 33845, and the diag before/after.
