---
title: Antlion changelog
description: What changed in each Antlion release — fixes, additions, and which reports they came from.
---

# Changelog

This is the record of what a subscription buys: every release, what it fixed, and which
of those came from a user report.

New releases reach you through the Rhino package manager —
[how updates arrive](../getting-started/index.md#install).

## 1.0.0 — 2026-10-05

The first public release. It covers the seating bowl, from the field outline to the sightline
drawings.

**Build the bowl**

- Field presets, with the focal point every sightline aims at. Rectangle, capsule and oval
  start lines, or your own curve.
- Section axes laid out along the start line, or taken from your own axis curves.
- Sections three ways — drawn as tread lines, solved from a target C-value, or read from a
  workbook — with front railings and wheelchair platforms.
- Vomitories that run flat, step down or ramp down to the concourse.
- Seats and aisles laid out automatically, or from your own seat, aisle and wheelchair-space
  curves.
- Cuts and openings by axis number or by curve, chained one after another.
- 3D solids for the stands, vomitories, railings, chairs and seated spectators.

**Check the sightlines**

- C-value per seat and per tread band across the whole bowl, colored by a legend you set.
- Section checks with sightlines and dimensions, one sheet per axis.
- C-value maps and seat maps on drawing sheets — zones, seat counts, wheelchair spaces and
  seat addresses.
- A view from any seat, in the Perspective viewport.

**Tables**

- Step heights, tread depths, tier settings and the C-value target read from a Google Sheets
  or Excel workbook, with the results written back.

**Also**

- Millimeter and inch documents.
- The Util panel works without a license.
- Rhino 8 for Windows, running on .NET Core.
