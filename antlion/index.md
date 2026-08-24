---
title: Antlion
description: Stadium bowl design workflow for Rhino 8 and Grasshopper — sections, stands, vomitories, seats and continuous C-value checking.
---

# Antlion

**Stadium bowl design workflow for Rhino 8 / Grasshopper.**

Antlion builds the seating bowl as one connected chain — start line, section, stands,
vomitories, seats, cuts — and keeps every step editable. Sightline quality (C-value) is
checked continuously, per seat or per tread, and results go straight to drawing sheets
and spreadsheets.

- **Bowl pipeline** — field, start lines, axes, sections (drawn, auto-solved from a target
  C-value, or driven by a workbook), 2D layout, 3D solids, railings.
- **Analysis** — C-value maps per seat and per tread, section checks with dimensions and
  sightlines, seat maps and numbering, view previews from any seat.
- **Tables & sheets** — Google Sheets / Excel round-trip, drawing sheet layouts.

Runs on Rhino 8 with Grasshopper. Works in millimeter and inch documents. All components
live under the **Antlion** tab. See [getting started](getting-started/index.md) for the
full requirements and the first-run steps.

## Documentation

- [**Getting started**](getting-started/index.md) — install, license, and the first
  definition that produces a bowl.
- [**Component reference**](reference/index.md) — every component, every port. Generated
  from the plugin source, so it can never disagree with the plugin you are running.
- [**Tutorials**](tutorials/index.md) — task-shaped guides for the parts where the rules
  are not visible on screen.
- [**Troubleshooting**](troubleshooting/index.md) — known symptoms, causes, and fixes.
- [**Changelog**](changelog/index.md) — what changed in each release.

## Get Antlion

Antlion is distributed through **Food4Rhino** and the Rhino package manager. Pricing and
purchase are handled there.

*(Food4Rhino listing link — coming with release.)*

The plugin itself is free to download. Components in the **Util** panel work without a
licence; the bowl, analysis and table components need one.

## Report a problem

Found a bug, or something that does not behave the way the reference says it should?

*(Report form link — coming with release.)*

**No account or sign-in is required.** The form asks what you saw and how to reproduce it;
the plugin fills in version and environment details for you.

Attaching the Grasshopper definition that shows the problem is the single most useful thing
you can do — please **internalize the input geometry** first, so the definition reproduces
on its own without your Rhino model. Screenshots are fine for anything visual.
**We do not ask for your model file.**

Every fix ships in a release and is listed in the [changelog](changelog/index.md). Leave an
email if you want to be told when yours is fixed, and a display name if you would like the
credit in the release notes.

Subscription, payment and invoice questions are handled by **Polar**, the merchant of record
for this product — use the customer portal link in your purchase email rather than the
report form.

## Who builds Antlion

Antlion is built and maintained by **plugin.dev.lab**, which works on design automation for
Rhino and Grasshopper. Bugs are fixed and shipped continuously — the
[changelog](changelog/index.md) is the record of that, and it is the honest way to judge
whether a subscription is worth it.

