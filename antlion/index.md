---
title: Antlion
description: Stadium bowl design workflow for Rhino 8 and Grasshopper — sections, stands, vomitories, seats and continuous C-value checking.
---

<p class="label">Rhino 8 · Grasshopper</p>

# Design the bowl as one chain you can keep editing.

Antlion builds a stadium seating bowl from the start line out — sections, stands,
vomitories, seats, cuts — and keeps every step editable. Sightline quality is checked
continuously as you go, not after the fact.

<section class="split">
<div class="split-text" markdown="1">
## One chain, not a black box

From the field outward, each component's outputs match the next one's inputs in order.
Change the start line and the whole bowl follows — the seats, the cuts, the solids, the
sightline maps.

Three different ways to build a section — drawn by hand, solved from a target C-value, or
driven from a spreadsheet — all produce the same object. **Everything downstream cannot
tell which way it came.**

[See the workflow](workflow/index.md)
</div>
<figure class="fig">
<div class="fig-wait">Image to come</div>
<figcaption>The bowl chain in Grasshopper, from field to railings.</figcaption>
</figure>
</section>

<section class="split flip">
<div class="split-text" markdown="1">
## Sightlines checked as you design

C-value is computed per seat and per tread band across the whole bowl, so you see where
the design breaks down rather than checking one section and hoping.

Section checks draw their evidence — dimensions and sightlines on the real cut — so a
number you report is a number you can defend in a meeting.

[Analysis components](reference/05-analysis-util.md)
</div>
<figure class="fig">
<div class="fig-wait">Image to come</div>
<figcaption>Per-seat C-value map across tiers.</figcaption>
</figure>
</section>

<section class="split">
<div class="split-text" markdown="1">
## Drawings and spreadsheets, both directions

Results go straight onto drawing sheets, and the numbers round-trip through Google Sheets
or Excel — read your inputs from a workbook, write the results back.

Works in millimetre and inch documents.

[Table components](reference/06-table.md)
</div>
<figure class="fig">
<div class="fig-wait">Image to come</div>
<figcaption>Section sheets and the workbook they came from.</figcaption>
</figure>
</section>

## Learn it

- [**Getting started**](getting-started/index.md) — install, licence, and the first
  definition that produces a bowl.
- [**Workflow**](workflow/index.md) — the whole chain as a map. Start here if you are
  wondering what order to use things in.
- [**Component reference**](reference/index.md) — every component, every port. Generated
  from the plugin source, so it cannot disagree with the plugin you are running.
- [**Tutorials**](tutorials/index.md) — the parts where the rules are not visible on screen.
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

