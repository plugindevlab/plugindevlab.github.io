---
layout: default
title: "Custom Axis — placing sections on curves you draw"
generated: true
---

# Custom Axis — placing sections on curves you draw

`Antlion ▸ Bowl ▸ Section 1` · ID `AXIS-003` · ports: [reference](../components/custom-axis/index.html)

Where `Axis` places axes automatically by rule (spacing, count), **`Custom Axis` makes
your own curves the axes.** Use it to bring axis lines straight in from a CAD drawing,
or to put sections exactly where you want them. The output is the same axis-system
object `Axis` produces — **downstream components cannot tell the difference.**

A few of its rules are invisible on screen. This page states all of them.

---

## 1. Minimal wiring

1. `Start Line` — **wire the output of any Startline component (recommended).**
   You can feed a bare curve into `Start Line Curve` instead, but the object carries
   the numbering reference frame (the field's long axis) and the bowl center; with a
   bare curve the component falls back to a centroid estimate.
2. `Axis Curves` — the curves you drew across the start line, collected in a `Curve`
   container. **The order you collect them in does not matter** — numbering is by
   perimeter order anyway (§3).
3. `Guide Length` — **only the length of the preview line** drawn at each axis. It has
   no effect on the result: not on the count, not on the numbering, not on direction.

Wire the `Axis` output into any Section component and a section stands at every axis.

## 2. Rule ① — every crossing becomes an axis (one curve, N axes)

**Every direct intersection with the start line is an axis.** A curve that crosses the
start line twice makes two axes.

CAD axis lines usually run **through** the whole bowl. They naturally cross a closed
start line twice — so **one set of axis lines puts axes on both stands.** That is the
intended behavior, not a bug.

- **Want axes on one stand only? Trim the curve on that side.** The component never
  guesses which crossing you "really meant" — a direct crossing is read as explicit intent.
- Curves crossing more than once are noted as `AC04` in the `Debug` output — no balloon,
  since this is the intended behavior (§8).

## 3. Rule ② — axes are numbered along the start line, not by input order

**List order is irrelevant.** Axis points are sorted by their position along the start
line perimeter, and numbered in that order.

- **Index 0 is the axis nearest the field's long-axis +X direction** — the same rule as
  the `Axis` component, so the two components share one numbering system. If the field
  is rotated, `AC13` in the `Debug` output says so.
- **Numbers run counterclockwise** whichever way the start line was drawn — a clockwise
  start line is reversed first, and `AC19` in the `Debug` output says so.
- Why: you can't reliably control the collection order of referenced curves, and with
  order-based numbering **one stray curve shifts every number after it.** Perimeter
  order stays stable as curves are added or removed.
- `Cut` / `Opening Cut` from/to use **these numbers, counted from 0**. The fastest
  check before cutting is to wire up `View Axis` and read the tags — they start at `A0`.

## 4. Rule ③ — short axis lines are matched by tangent extension

Axis lines that stop short of the start line still work — but **the test is direction,
not distance.** The curve is extended straight along its own tangent; if that extension
**points at the start line**, the intersection becomes the axis.

- A curve sitting right next to the start line but **not pointing at it** does not
  become an axis. It is not dropped silently — it is counted in the orange warning
  `AC12`: `N/M axis curves skipped (does not point at the start line=N)`.
- **Except axis lines lying beyond the ends of an open start line** — those get only the
  white note `AC20`. When several stands share one set of axis lines and one stand's
  start line is shorter, the top view already shows why they were left out. Extend the
  start line if you wanted that stand wider.
- **An axis line that crosses the start line in plan but sits at a different height (Z)**
  stays in the orange `AC12`, with the reason
  `crosses the start line only in plan - drawn at a different height` — the test is a 3D crossing.
- An extension takes **only the nearest crossing** (the one using the least extension).
  This is deliberately different from direct crossings (§2): an extended line would
  also pierce the far side of the bowl, and taking every extended crossing would create
  ghost axes. **Direct crossing = explicit intent; extension = inference.** If you want
  a through-axis, actually draw the curve through.
- The fact that extension was used at all is noted as `AC11` in the `Debug` output. A gap
  over 1 mm also raises the orange `AC06` balloon (§5).
- **A closed axis curve that doesn't touch the start line** cannot be extended, so it
  is treated as foreign and skipped (`AC12`).

## 5. Rule ④ — a large AC06 gap means "that's not an axis, that's debris"

When the extension distance exceeds 1 mm, the orange warning `AC06` appears:

```
N/M axis curves stop short of the start line - extended along their own
direction to meet it (max gap 32.5 mm, axes [3, 7]).
```

- **Gap of a few mm–cm** — the axis line was drawn slightly short. Common and harmless;
  just know the axis point sits at the extended intersection, not at the curve's end.
- **Gap of tens of meters** — that is not an axis you drew short. It is **a distant
  stray curve that happened to point at the start line.** The warning names the axis
  numbers (`axes [...]`); check those axis points and remove the stray from the input.
- The extension limit is the size of the start line itself (its bounding-box diagonal) —
  anything inside the model can reach. It has nothing to do with `Guide Length`.

## 6. Section direction — follows your curve's tangent, faces outward

Each axis plane faces along **the curve's tangent at the crossing point**, projected to
the XY plane — then auto-flipped to face away from the bowl center, so the direction
you drew the curve in doesn't matter.

- Cross the start line at an angle and the section stands at that angle — the reference
  is **your curve**, not a radial direction. Three exceptions:
  - **Where the start line bends**, an axis is turned to the bend's miter — the only
    direction that keeps your tread depth on both sides of the bend. The white balloon
    `AC16` names those axes and the largest turn. Axis points and numbering do not change,
    but the far end of a long stand moves sideways; draw the axis curves more evenly
    through the bend to be followed more closely.
  - **An axis curve lying almost along the start line** (over 60° from its normal) is set
    to the start-line normal instead — orange balloon `AC17`. Redraw it closer to square.
  - **When outward cannot be worked out**, the drawn direction is kept — `AC18`: a white
    balloon if the curve runs sideways past the field center, orange if no field is wired
    at all (wire Field Info into the start line).
- If the tangent at the crossing is vertical (no XY component), the component falls
  back to the radial direction and notes it as `AC08` in the `Debug` output.

## 7. Base Line — where the stand is actually built

The `Base Line` output is the **faceted polyline connecting the axis points.** The
stand is built on this polyline, not on the original smooth start line — the same
principle as the `Axis` component.

- Sparse axes make a visibly faceted bowl. To smooth a curved stretch, add more axis
  lines there.
- Check spacing and shape directly on the canvas via `Axis Lines` (previews) and `Base Line`.

## 8. Warning codes at a glance

Balloon colors: **red** = nothing is produced / **orange** = some input was dropped
from the result / **white** = it works, but check this. Codes that only report what
happened raise **no balloon** — they appear as codes in the component's `Debug` output
(`info[...]`).

**Balloons**

- `AC01` (red) — no start line. Wire `Start Line` or `Start Line Curve`.
- `AC02` (red) — no axis curves.
- `AC10` (red) — every curve was skipped; zero axes (with a tally of reasons).
- `AC14` (red) — fewer than 2 distinct axis points; a base line needs at least 2.
- `AC15` (red) — fewer than 3 distinct axis points on a closed start line.
- `AC12` (orange) — some curves skipped. Reasons: `null` (empty entries) ·
  `does not point at the start line` (§4) · `crosses the start line only in plan` (height differs, §4) · `degenerate direction` · `zero-length curve`.
- `AC06` (orange) — extension beyond 1 mm; reports the max gap and the axis numbers (§5).
- `AC09` (orange) — two axis points within 1 mm. Both are kept; check the numbering.
- `AC17` (orange) — an axis curve lies almost along the start line; the start-line normal is used (§6).
- `AC18` (white, or orange with no field wired) — outward could not be worked out; the drawn direction is kept (§6).
- `AC16` (white) — axes at a bend of the start line were turned to the bend's miter (§6).
- `AC20` (white) — axis lines beyond the ends of an open start line were left out (§4). Fine if the stand is meant to be shorter.

**`Debug` output only**

- `AC04` — one curve, several crossings, one axis each (§2).
- `AC08` — vertical tangent, radial fallback (§6).
- `AC11` — no direct crossing, matched by extension (§4).
- `AC13` — numbering follows the rotated field long axis (§3).
- `AC19` — the start line was drawn clockwise and was reversed (§3).

## 9. Quick answers

- **Twice as many axes as curves** → through-curves make one axis per crossing (§2).
  Trim the curve if you want one side only.
- **Numbers don't match the order I fed them in** → they never will; numbering is
  perimeter order (§3). Check with `View Axis`.
- **One of my curves is missing from the result** → read `AC12` (orange) or `AC20` (white):
  it doesn't point at the start line even when extended, sits at a different height, or
  lies beyond the start line's ends (§4).
- **There's an axis in a weird place** → read `AC06`'s max gap and axis numbers. A huge
  gap means a stray curve got in (§5).
- **Changing `Guide Length` does nothing** → correct; it is display only (§1).
- **The section faces a strange direction** → direction is your curve's tangent at the
  crossing (§6). Redraw the curve at the angle you want. If a white `AC16` or orange
  `AC17`/`AC18` balloon is up, it names the axes that were turned or kept, and why.
