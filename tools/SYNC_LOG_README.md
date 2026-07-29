# Sync Log — cross-repo record & viewer

Companion to the Decision Deck, for a different kind of information:
the deck holds **calls only you can make**; the sync log holds **facts
about things moving between repos** — pack deliveries and intakes, asks
one repo has of another, and problems found (drift, unpushed sources,
stale clones).

## Files

- `sync_log.json` — the record. Agents append entries the moment a
  cross-repo event happens (protocol: `docs/18-AGENT_SYNC_PROTOCOL.md`).
  Committed like the deck register. Never hand-edit past entries.
- `sync_log.html` — single-file offline viewer. Open in any browser, no
  install. Ships with a built-in snapshot; IMPORT `sync_log.json` to see
  the current log.
- `ecosystem.lock.json` — who currently consumes exactly what (the
  machine-readable successor to doc 16's version table). Updated only
  during pack intakes or mainline rulings.

## The app

Top board answers the three questions that matter at a glance, computed
from the entries (nothing hand-kept):

- **deliveries waiting for intake** — a pack was exported but no repo
  has taken it in yet
- **open problems** — sync failures found and not yet fixed
- **open asks** — one repo needs something from another

Below: the full timeline, filterable by repo and type, searchable. Tap
an entry to expand it. Open items have a MARK RESOLVED button — add a
one-line note, then EXPORT and commit the JSON (or tell the next agent
session you resolved it and it will sweep the export in).

PASTE FROM AI appends entries an agent hands you; COPY THE ENTRY SCHEMA
gives you the prompt to request them in the right shape.

## Status

DRAFT alongside doc 18 — using the log binds nobody; the protocol rules
(publish gates, default-branch rule, GitHub-release transport) wait for
your deck ruling (doc 18 §11).
