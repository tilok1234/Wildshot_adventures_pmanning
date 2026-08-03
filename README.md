# Wildshot Adventures

Top-down 2D open-world fantasy action RPG: a single-player MMO-scale adventure
with freely aimed projectile combat. **Era: Slice v0.1 is BUILDING** — the world
is the test (four zones, cap 30, all three classes; `docs/23-SLICE_BUILD_PLAN.md`
governs); S0 + S1 engineering complete and the designer's Green days run deep:
starhook v2, the nine-seam systems pass, and the menu-system v2 pass (built on
the designer's own UI package, 2026-08-03) are all IN. Systems-complete
remainder: the gear seam → class trees v1 (+ foraging on three designer words).

**This repository is the DESIGN AUTHORITY of a seven-repo ecosystem** (planning ·
game · tileforge · worldforge · world_filler · sprite assembler · resonance
forge). Who owns what: [`docs/16-ECOSYSTEM_MAP.md`](docs/16-ECOSYSTEM_MAP.md).
Cross-repo events and pins: `tools/sync_log.json` + `tools/ecosystem.lock.json`.

## Where things stand

Read **[`docs/03-HANDOFF.md`](docs/03-HANDOFF.md)** first — its CURRENT section
(top of the file) is always the live board and names the fresh session's first
moves. The chronological day-by-day story lives in `notes/sessions/`.

## Layout

- `docs/` — the living design documentation set: GDD (01), decision register
  (08), stat-system authority (22), slice build plan (23), ecosystem map (16),
  and more. See [`docs/06-DOCS_README.md`](docs/06-DOCS_README.md) for the
  document map.
- `notes/sessions/` — dated per-session working notes (the chronological record).
- `notes/reference/` — designer-delivered artifacts preserved verbatim (e.g. the
  starhook prototype; its `INDEX.md` is starhook law).
- `tools/` — sync log, ecosystem lock, decision-deck register and viewers.

## Continuing in a new session (any device or account)

Tell the assistant:

> Resume the planning seat for Wildshot Adventures. Read
> `docs/03-HANDOFF.md`'s CURRENT section in this repo first and follow its
> first moves.

No attachments needed — everything required is in the repo.

**History:** the project began as a guided design interview (Part I, CORE-01
through CORE-55, complete 2026-07-26 — register: `docs/08`). The interview era
ended with the Gate-1 rewrite (2026-07-30, `docs/19`) and the world-is-the-test
ruling (sl-0098); `notes/INTERVIEW_STATE.md` is that era's record.
