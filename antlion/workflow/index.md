---
title: The Antlion workflow
description: The whole Antlion chain as one map — start line, section, 2D layout, 3D solids, analysis. What order to use things in.
---

<p class="label">Track 1 · Concept</p>

# What order to use things in

Most of the difficulty in a Grasshopper plugin is not *what exists* — it is *what comes
next*. This page is the whole chain in one view. Follow it left to right; branch off where
your design needs to.

If you already know the plugin and just want a component, go to the
[reference](../reference/index.md) instead — same pages, different door.

## The stages

<section class="split">
<div class="split-text" markdown="1">
### 1 · Plan & setup

Place the field, draw the line where the front row starts, and set the axes the sections
sit on. Four start-line shapes form a continuum — grow the corner radius and a rectangle
becomes a capsule, then an oval — with a custom curve as the escape hatch.

[Components](../reference/01-plan.md)
</div>
<figure class="fig"><div class="fig-wait">Image to come</div></figure>
</section>

<section class="split flip">
<div class="split-text" markdown="1">
### 2 · Section

Build the stair section and attach extras such as railings and wheelchair platforms.
**Three ways in** — read a line you drew, solve riser heights from a target C-value, or
build it from workbook numbers. Downstream components cannot tell which way it came.

[Components](../reference/02-section.md)
</div>
<figure class="fig"><div class="fig-wait">Image to come</div></figure>
</section>

<section class="split">
<div class="split-text" markdown="1">
### 3 · 2D plan layout

Unroll the section onto the plan, place vomitories and seats, and cut the bowl to shape.
**Most design decisions happen here** — this is where the bowl stops being a curve and
starts being a seating plan.

[Components](../reference/03-plan2d.md)
</div>
<figure class="fig"><div class="fig-wait">Image to come</div></figure>
</section>

<section class="split flip">
<div class="split-text" markdown="1">
### 4 · 3D solids

Build what 2D decided as real solids — tier stands, vomitory stairs, railings, seats.
The assembled result is what the analysis components read.

[Components](../reference/04-body3d.md)
</div>
<figure class="fig"><div class="fig-wait">Image to come</div></figure>
</section>

<section class="split">
<div class="split-text" markdown="1">
### 5 · Analysis

C-value per seat and per tread band, section checks with dimensions and sightlines drawn
as evidence, seat maps and numbering, and a view from any seat.

**Section analysis and the maps do not replace each other** — one examines a single section
rigorously, the others show where the whole bowl breaks down.

[Components](../reference/05-analysis-util.md)
</div>
<figure class="fig"><div class="fig-wait">Image to come</div></figure>
</section>

<section class="split flip">
<div class="split-text" markdown="1">
### 6 · Tables and sheets

Values can live in a spreadsheet instead of Rhino — read inputs from a workbook, write
results back. Google Sheets and Excel both work, and communication happens only when you
press Run.

[Components](../reference/06-table.md)
</div>
<figure class="fig"><div class="fig-wait">Image to come</div></figure>
</section>

## Wiring the chain

From the 2D layout on, each component's outputs match the next component's inputs
top-to-bottom, one to one — wire them straight down in order. The
[reference index](../reference/index.md) has the full chain diagram, including the
branches and which bundled ports carry the chain.
