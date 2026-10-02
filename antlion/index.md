---
title: Antlion
description: Grasshopper plugin for stadium seating bowls in Rhino 8 — sections, stands, vomitories and seats as one editable chain, with C-value sightlines checked as you design.
---

<p class="label">Grasshopper plugin · Rhino 8</p>

# Design the bowl. Don't just generate it.

Antlion is a Grasshopper plugin for stadium seating bowls. It builds the stand from the
start line out — sections, stands, vomitories, seats, cuts — keeps every step editable,
and checks C-value sightlines continuously as you design, not after the fact.

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

[Analysis components](components/index.html)
</div>
<figure class="fig">
<div class="fig-wait">Image to come</div>
<figcaption>Per-seat C-value map across tiers.</figcaption>
</figure>
</section>

<section class="split">
<div class="split-text" markdown="1">
## Bring your own curves

The presets are where you start, not where you have to stay. A field outline, the start
line, section axes, hand-drawn tread lines, cut and opening curves, seat blocks and aisles
can all come from your own Rhino or Grasshopper curves.

Antlion builds the bowl around them and checks the sightlines again, so you can change the
shape and see what it does to every seat.

[Components](components/index.html)
</div>
<figure class="fig">
<div class="fig-wait">Image to come</div>
<figcaption>A bowl rebuilt around a custom start line.</figcaption>
</figure>
</section>

<section class="split flip">
<div class="split-text" markdown="1">
## Drawings and spreadsheets, both directions

Results go straight onto drawing sheets. Step heights, tread depths, tier settings and the
C-value target can be read from a Google Sheets or Excel workbook and the results written
back to it — change the numbers, run, and the section follows.

Works in millimeter and inch documents.

[<span translate="no">Table</span> components](components/index.html)
</div>
<figure class="fig">
<div class="fig-wait">Image to come</div>
<figcaption>Section sheets and the workbook they came from.</figcaption>
</figure>
</section>

## Where Antlion is going

Antlion 1.0.0 covers the seating bowl. Later versions build outward from it — first the
structure and circulation around the bowl, then the facade and roof.

<figure class="roadmap">
<div class="rm">
<section class="rm-v is-now"><p class="rm-head"><span class="tag on" style="--tier:var(--tier-core)">1.0.0</span><span class="rm-when">First release</span></p>
<h3>Bowl</h3>
<ul><li>Sections, stands, vomitories, seats and cuts</li><li>C-value sightlines, per seat and per section</li><li>Drawing sheets and spreadsheet round trips</li></ul></section>
<div class="rm-link"><span class="rm-note">A few months of fixes first</span><span class="rm-arrow"></span></div>
<section class="rm-v"><p class="rm-head"><span class="tag on" style="--tier:var(--tier-structure)">2.0.0</span><span class="rm-when">Planned</span></p>
<h3>Structure and circulation</h3>
<ul><li>Concourses</li><li>Columns and raker beams</li><li>Stairs</li><li>Static crowd flow</li></ul></section>
<div class="rm-link"><span class="rm-arrow"></span></div>
<section class="rm-v"><p class="rm-head"><span class="tag on" style="--tier:var(--tier-roof)">3.0.0</span><span class="rm-when">Planned</span></p>
<h3>Facade and roof</h3>
<ul><li>Facade</li><li>Roof</li></ul></section>
</div>
</figure>

- **Fixes come first.** For the first few months after release, the work goes into fixing and
  refining 1.0.0. Development of 2.0.0 starts after that.
- **Versions may come with their own plans.** 2.0.0 and 3.0.0 may be offered as higher
  subscription plans, and the plans may be priced differently.
- **Nothing you have moves up.** A component in your plan stays in your plan — a new version
  never moves an existing component to a higher plan.
- **Components can move down.** Over time, components from a higher plan may be added to a
  lower one.

<p class="rm-fine">This is a plan, not a release schedule. What goes into each version, and when, may change.</p>

## Learn it

New to Antlion? Read these two, in this order.

1. [**Getting started**](getting-started/index.md) — what you need, installing from the
   package manager, and registering your license.
2. [**Workflow**](workflow/index.md) — the whole chain as a map. Start here if you are
   wondering what order to use things in.

When you need to look something up:

- [**Components**](components/index.html) — every component, every port, with a diagram of
  where each port sits on the capsule. Generated from the plugin source, so it cannot
  disagree with the plugin you are running.
- [**Ribbon map**](workflow/index.md#ribbon) — which panel and section each component lives
  in, for when you know the plugin and just want to find the thing.
- [**Tutorials**](tutorials/index.md) — the parts where the rules are not visible on screen.
- [**Troubleshooting**](troubleshooting/index.md) — known symptoms, causes, and fixes.
- [**Changelog**](changelog/index.md) — what changed in each release.

## Get Antlion

Antlion is distributed through **Food4Rhino** and the Rhino package manager. Pricing and
purchase are handled there.

*(Food4Rhino listing link — coming with release.)*

The plugin itself is free to download. Components in the <strong translate="no">Util</strong> panel work without a
license; the bowl, analysis and table components need one.

## Report a problem

Found a bug, or something that does not behave the way the reference says it should?

[**Report a problem →**](https://tally.so/r/MepAQM)

**No account or sign-in is required.** The form asks what you saw and how to reproduce it;
the plugin fills in version and environment details for you. Two steps — internalising the
geometry, or pasting the `debug` output — usually let us find the cause without asking you
anything further:
[how to write a report that gets fixed](troubleshooting/index.md#report-a-problem).

Subscription, payment and invoice questions are handled by **Polar**, the merchant of record
for this product — use the customer portal link in your purchase email rather than the
report form.

## Who builds Antlion

Antlion is built and maintained by **plugin.dev.lab**, which works on design automation for
Rhino and Grasshopper. Bugs are fixed and shipped continuously — the
[changelog](changelog/index.md) is the record of that, and it is the honest way to judge
whether a subscription is worth it.

