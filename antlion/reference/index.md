---
layout: default
title: "Antlion Component Reference"
generated: true
---

# Antlion Component Reference

Every Grasshopper component in the Antlion plugin — descriptions, inputs and outputs —
split by ribbon panel and section so it reads well on any screen.

> The port pages (01–06) are generated straight from the plugin source: the text is the
> plugin's own tooltip text, so the wiki and the plugin can never disagree.
> This index and the tutorials are written by hand.

---

## Ribbon layout — where things are

Everything lives under the **`Antlion` tab**, in four panels. Panels are divided into
**sections**, and the section order is the working order.

### Panel `Bowl` — the bowl pipeline

- **Section 1 · Plan & Setup** → [01-plan.md](01-plan.md)
  `Field` · `Startline Rect` · `Startline Capsule` · `Startline Oval` · `Custom Startline` · `Axis` · `Custom Axis`
  Place the field, draw the line where the front row starts, set the axes the sections sit on.
  - **The four start lines form a continuum of shapes**: grow the corner radius and a
    rectangle becomes a capsule, then an oval — `Rect` (four straight sides, treated
    corners) → `Capsule` (two straight sides, semicircular ends) → `Oval` (no straight
    sides) → `Custom Startline` (any curve you draw, open curves allowed).

- **Section 2 · Section** → [02-section.md](02-section.md)
  `Section` · `Auto Section` · `Section Plus` · `Table Section`
  Build the stair section and attach extras such as railings and wheelchair platforms.
  **There are three ways to make a section** — `Section` reads a line you drew,
  `Auto Section` solves riser heights from a target C-value, `Table Section` builds it
  from workbook numbers. Downstream components cannot tell which way it came.

- **Section 3 · 2D Plan Layout** → [03-plan2d.md](03-plan2d.md)
  `Stand 2D` · `Vomitory` · `Seat` · `Custom Seat` · `Cut` · `Opening Cut`
  Unroll the section onto the plan, place vomitories and seats, cut the bowl to shape.
  **Most design decisions happen here.**

- **Section 4 · 3D Solids** → [04-body3d.md](04-body3d.md)
  `Stand 3D` · `Vom 3D` · `Assemble Bowl` · `Stand 3D Plus` · `Rail 3D` · `Seat 3D`
  Build what 2D decided as real solids.

### Panel `Bowl Analysis` — checking → [05-analysis-util.md](05-analysis-util.md)

`Section analysis` (C-value sightline check on one section) · `C-value Seat` (per-seat
C-value map) · `C-value Tread` (per-tread-band C-value map) · `C-value Section Check`
(per-axis sections onto sheets) · `C-value Map` (per-tier plan sheets) · `Seat Map`
(seat zones and numbering) · `View Axis` (axis number tags) · `View Limit` (viewing
distance limits) · `Seat View` (what a given seat actually sees).

- **`Section analysis` and the maps do not replace each other.** Use `Section analysis`
  to examine one section rigorously (it draws dimensions and sightlines as evidence);
  use the maps to see where the whole bowl breaks down.
- **`C-value Tread` and `C-value Seat` differ in resolution** — Tread uses one
  representative section per axis span, Seat computes one value per seat. Both are
  valid; which to use is a design judgement. They diverge most on curved segments.
- **`Section Check` creates no values** — it only draws what `Tread` computed, so the
  `C digest:` line in both components' `debug` output must match to the letter.

### Panel `Table` — spreadsheet round-trip → [06-table.md](06-table.md)

`Google Workbook` · `Excel Workbook` (connect/create) · `Table In` (read) ·
`Table Out` (write back). Values live in a spreadsheet instead of Rhino.
**Communication happens only when you press Run.**

### Panel `Util` — tools → [05-analysis-util.md](05-analysis-util.md)

`License` (license registration) · `Input Panel` (gather inputs in one panel) ·
`C-value Legend` · `Sheet Setup` (shared drawing-sheet format) · `Slider Merge` ·
`Toggle Merge` (bundle per-tier inputs) · `Data Gate` · `Gate Switch` (hold values).

---

## The standard chain — what plugs into what

```
Field ─> Startline* ─> Axis ─> Section ─> Stand 2D ─> Vomitory ─> Seat ─> Cut ─> Assemble Bowl ─> Stand 3D Plus ─> Rail 3D
  │                        (or Auto Section              │        │       │                          │
  │                         or Table Section)       Opening Cut  Vom 3D   ├─> C-value Seat            └─> Seat 3D
  │                              │                                        ├─> C-value Tread
  │                         Section Plus                                  └─> Seat Map ─> Seat View
  │                       (railings, wheelchair)
  └─> View Limit (reference)                     Section analysis (C-value check, branches off the section)
```

- **It flows in one line.** From `Stand 2D` on, each component's outputs match the next
  component's inputs top-to-bottom 1:1 — wire them straight down in order.
- **`Stand 3D`** branches off `Stand 2D` to build tier solids; `Stand 3D Plus` takes the
  result and carves the cuts.
- **`Vom 3D` is the exception** — feed its own returned `Seat Result` into
  `Stand 3D Plus` (feeding the original leaves the stairs buried inside the stand).
  Vom 3D's 3D result travels inside that `Seat Result`, so analysis components only
  need **one wire: Rail 3D's `Rail Result` (RLD)**.
- **Analysis components take one RLD wire** — `C-value Seat` / `C-value Tread` accept
  RLD on their `Build Result` port (RLD carries BRD inside). To exclude railings from
  the obstacle set, turn `Rail Check` off.

### Chain-carrier ports

Short upper-case port names carry **bundled chain data**. Don't inspect them — just
wire them through to the next component.

- `Stand Sections` SSD — tier sections / `Axis` — the axis system / `Stand 2D` — tread rings (the 2D bowl)
- `Vomitory` VD — vomitories / `Seat Result` SRD — **the whole 2D layout. The spine of the chain**
- `Stand Body` SBD — raw stand solids / `Build Result` BRD — the 3D bowl
- `Rail Result` RLD — railings (also carries BRD and vomitory 3D)
- `Sheet Data` SHD — drawing sheet format / `Seat Map Data` — seat zones, numbers, addresses

---

## Where diagnostics show up

- **Warnings = the component itself.** Balloon colour is severity — **red** = fatal,
  nothing is produced / **orange** = something is missing, part of the work was skipped /
  **white** = it works, but there is advice. Silence means all good.
- **`report`** — analysis components only: the human-readable result summary. This is
  the one to keep on a panel.
- **`debug`** — every component: a one-line diagnostic (build identity, counts, warning
  tallies, any exception at the end). Ignore it day-to-day; **copy this text into a bug
  report** when something goes wrong.

---

## How to read the port pages

```
3. `Focal Height`  ·  nick `Focal H` — `Number` `item` · default `1500 mm / 60 in` · optional
   - (the plugin's tooltip text, extracted from source)
```

- Leading number = **port order in Grasshopper** (0-based, top to bottom).
- `Number` = data type; `item` = one value, `list` = a list, `tree` = a data tree.
- `nick` = the short label shown on the canvas. Only listed when it differs from the name.
- `default` = the value used when nothing is wired. **`500 mm / 20 in` means a
  code-aware default that follows the document unit system** (an inch document gets
  20 in, not 19.7 in); a plain `500 mm` is a straight conversion.
- `optional` = safe to leave unwired. `dropdown` = wiring a Value List auto-fills the options.
- Inputs marked "one value per tier" broadcast a single value to all tiers; use
  `Slider Merge` / `Toggle Merge` for per-tier values.

---

## Tutorials — the rules you can't see on screen

- [Custom Axis — placing sections on your own curves](../tutorials/custom-axis.md) —
  one axis per crossing, perimeter-order numbering, tangent-extension matching, and
  what a large AC06 gap really means.
