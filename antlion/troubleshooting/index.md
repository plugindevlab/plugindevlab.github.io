---
title: Antlion troubleshooting
description: Known symptoms in Antlion for Rhino and Grasshopper — what causes them and how to fix them.
---

# Troubleshooting

Search for your symptom. Each page says what you see, why it happens, and what to do about
it — including which version fixed it, if it was a bug.

If your problem is not here, [report it](#report-a-problem) — the form and the two steps that
make a report fixable are further down this page.

## Pages

*No pages yet — this section fills up as reports come in after release.*

## Report a problem

Found a bug, or something that does not behave the way the reference says it should?

[**Report a problem →**](https://tally.so/r/MepAQM)

**No account or sign-in is required.** The form asks what you saw and how to reproduce it;
the plugin fills in version and environment details for you.

### Two things that make a report fixable

New to Grasshopper? These are the two steps people most often miss. Either one on its own
usually lets us find the cause without asking you anything further.

**1 — Internalise the geometry before you save the file.**
A Grasshopper definition only *references* the curves and surfaces in your Rhino document.
Sent as-is, it opens empty on our side and there is nothing to look at.

- Select the components you used, or just the input parameters holding your Rhino geometry
- Right-click that input → **Internalise data**
- The wire to Rhino disappears and the geometry is now stored inside the definition
- **File → Save As**, and attach that copy

The internalised file contains only the geometry you internalised — not your Rhino document.

**2 — Or paste the debug output instead.**
Every Antlion component has a **`debug`** output, and it is often faster than sending files.

- Double-click empty canvas, type `panel`, press Enter
- Drag a wire from the component's **`debug`** output into that panel
- Right-click the panel → **Copy Data Only**
- Paste it into the report form

If the component shows an orange or red bubble, hover it and copy that message too.

Attaching the Grasshopper definition that shows the problem is the single most useful thing
you can do — please **internalize the input geometry** first, so the definition reproduces
on its own without your Rhino model. Screenshots are fine for anything visual.
**We do not ask for your model file.**

Every fix ships in a release and is listed in the [changelog](../changelog/index.md). Leave an
email if you want to be told when yours is fixed, and a display name if you would like the
credit in the release notes.

Subscription, payment and invoice questions are handled by **Polar**, the merchant of record
for this product — use the customer portal link in your purchase email rather than the
report form.
