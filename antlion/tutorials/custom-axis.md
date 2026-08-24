---
layout: default
title: "Custom Axis — placing sections on curves you draw"
generated: true
---

# Custom Axis — placing sections on curves you draw

`Antlion ▸ Bowl ▸ Section 1` · ID `AXIS-003` · ports: [reference](../reference/01-plan.md#custom-axis)

Where `Axis` places axes automatically by rule (spacing, count), **`Custom Axis` makes
your own curves the axes.** Use it to bring axis lines straight in from a CAD drawing,
or to put sections exactly where you want them. The output is the same axis-system
object `Axis` produces — **downstream components cannot tell the difference.**

A few of its rules are invisible on screen. This page states all of them.

---

## 1. Minimal wiring

1. `Start Line` — **wire the output of any Startline component (recommended).**
   You can feed a bare curve into `Start Line Curve` instead, but the object carries
   the numbering reference frame (the field's long axis) and the bowl centre; with a
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
intended behaviour, not a bug.

- **Want axes on one stand only? Trim the curve on that side.** The component never
  guesses which crossing you "really meant" — a direct crossing is read as explicit intent.
- Curves crossing more than once raise the white note `AC04`:
  `N curves cross the start line more than once - one axis per crossing`.

## 3. Rule ② — axes are numbered along the start line, not by input order

**List order is irrelevant.** Axis points are sorted by their position along the start
line perimeter, and numbered in that order.

- **Index 0 is the axis nearest the field's long-axis +X direction** — the same rule as
  the `Axis` component, so the two components share one numbering system. If the field
  is rotated, the white note `AC13` tells you so.
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
  `AC12`: `N/M axis_curves skipped (does not point at the start line=N)`.
- An extension takes **only the nearest crossing** (the one using the least extension).
  This is deliberately different from direct crossings (§2): an extended line would
  also pierce the far side of the bowl, and taking every extended crossing would create
  ghost axes. **Direct crossing = explicit intent; extension = inference.** If you want
  a through-axis, actually draw the curve through.
- The fact that extension was used at all shows as the white note `AC11`:
  `extended N/M curves to meet the start line (no direct crossing)`.
- **A closed axis curve that doesn't touch the start line** cannot be extended, so it
  is treated as foreign and skipped (`AC12`).

## 5. Rule ④ — a large AC06 gap means "that's not an axis, that's debris"

When the extension distance exceeds 1 mm, the orange warning `AC06` appears:

```
N/M axis_curves stop short of the start line - extended along their own
direction to meet it (max gap 32.5mm, axes [3, 7])
```

- **Gap of a few mm–cm** — the axis line was drawn slightly short. Common and harmless;
  just know the axis point sits at the extended intersection, not at the curve's end.
- **Gap of tens of metres** — that is not an axis you drew short. It is **a distant
  stray curve that happened to point at the start line.** The warning names the axis
  numbers (`axes [...]`); check those axis points and remove the stray from the input.
- The extension limit is the size of the start line itself (its bounding-box diagonal) —
  anything inside the model can reach. It has nothing to do with `Guide Length`.

## 6. Section direction — follows your curve's tangent, faces outward

Each axis plane faces along **the curve's tangent at the crossing point**, projected to
the XY plane — then auto-flipped to face away from the bowl centre, so the direction
you drew the curve in doesn't matter.

- Cross the start line at an angle and the section stands at that angle — the reference
  is **your curve**, not a radial direction.
- If the tangent at the crossing is vertical (no XY component), the component falls
  back to the radial direction and notes it as `AC08`.

## 7. Base Line — where the stand is actually built

The `Base Line` output is the **faceted polyline connecting the axis points.** The
stand is built on this polyline, not on the original smooth start line — the same
principle as the `Axis` component.

- Sparse axes make a visibly faceted bowl. To smooth a curved stretch, add more axis
  lines there.
- Check spacing and shape directly on the canvas via `Axis Lines` (previews) and `Base Line`.

## 8. Warning codes at a glance

Balloon colours: **red** = nothing is produced / **orange** = some input was dropped
from the result / **white** = information.

- `AC01` (red) — no start line. Wire `Start Line` or `Start Line Curve`.
- `AC02` (red) — no axis curves.
- `AC10` (red) — every curve was skipped; zero axes (with a tally of reasons).
- `AC12` (orange) — some curves skipped. Reasons: `null` (empty entries) ·
  `does not point at the start line` (§4) · `degenerate direction`.
- `AC06` (orange) — extension beyond 1 mm; reports the max gap and the axis numbers (§5).
- `AC09` (orange) — two axis points within 1 mm. Both are kept; check the numbering.
- `AC04` (white) — one curve, several crossings, one axis each (§2).
- `AC08` (white) — vertical tangent, radial fallback (§6).
- `AC11` (white) — no direct crossing, matched by extension (§4).
- `AC13` (white) — numbering follows the rotated field long axis (§3).

## 9. Quick answers

- **Twice as many axes as curves** → through-curves make one axis per crossing (§2).
  Trim the curve if you want one side only.
- **Numbers don't match the order I fed them in** → they never will; numbering is
  perimeter order (§3). Check with `View Axis`.
- **One of my curves is missing from the result** → read `AC12`: it doesn't point at
  the start line even when extended (§4).
- **There's an axis in a weird place** → read `AC06`'s max gap and axis numbers. A huge
  gap means a stray curve got in (§5).
- **Changing `Guide Length` does nothing** → correct; it is display only (§1).
- **The section faces a strange direction** → direction is your curve's tangent at the
  crossing (§6). Redraw the curve at the angle you want.
