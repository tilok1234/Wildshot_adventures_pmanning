# Decision Deck — game-dev decision & sign-off register

A single-file, offline app. Open `Decision Deck.html` in any browser. No install, no server.

## What it does
One queue of every call only you can make, dealt as cards sorted by blocking weight (what unblocks the most floats to the top). Six item types:

- **Ruling** — one-tap design decision. Card shows the options with your lean highlighted; tap one.
- **Feel verdict** — play it and judge. Tier `anytime` or `fresh` (fresh-eyes-only items stay hidden until you flip FRESH HANDS on).
- **Play evidence** — do once, logs prove it. Tap "mark done".
- **Acceptance row** — formal sign-off judged from captures/reports. Accept / Reject.
- **Go / no-go** — one DO IT tap authorizes an engineering batch.
- **Cadence** — recurring; "done" resets the cycle and it reappears when due.

Every item carries: repo, actionable **now / later** (later stays hidden until promoted), **what it unblocks**, and blocking weight 1–5.

## Views & controls
- **DECK** — one card at a time; decide, add an optional note, skip, or edit.
- **ALL ITEMS** — full list with type/repo/status filters, show-later toggle, edit/delete/reopen.
- **+ NEW ITEM** — full add/edit form; add repos with the `+` next to the repo select; attach any number of images (shown on the card, click to zoom) for visual reviews.
- **EXPORT / IMPORT** — JSON file, for backup or moving machines.
- **PASTE FROM AI** — paste a JSON array of items an AI generated; append or replace. "Copy the item schema" gives you a ready prompt to hand the AI.

## Data & storage
Everything autosaves to the browser's localStorage (per browser/device — export JSON to move it). Sample items are badged SAMPLE; remove them via CLEAR SAMPLE ITEMS in the list view.

## Item JSON schema (for AI intake / import)
```json
{
  "title": "required",
  "category": "ruling | feel | evidence | acceptance | gonogo | cadence",
  "repo": "string (new repos auto-added)",
  "actionable": "now | later",
  "weight": 3,
  "unblocks": "short label",
  "detail": "optional context",
  "options": ["A", "B"], "lean": "B",
  "tier": "anytime | fresh",
  "intervalDays": 7
}
```
`options`/`lean` are ruling-only, `tier` feel-only, `intervalDays` cadence-only. Import accepts a bare array or `{"items":[...],"repos":[...]}`.
