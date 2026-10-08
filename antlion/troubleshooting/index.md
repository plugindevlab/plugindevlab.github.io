---
title: Antlion troubleshooting
description: Known symptoms in Antlion for Rhino and Grasshopper — what causes them and how to fix them.
---

# Troubleshooting

{%- capture tlist -%}
{%- assign tpages = site.pages | sort: "title" -%}
{%- for p in tpages -%}
{%- if p.url != page.url and p.url contains page.url %}
- [{{ p.title | escape }}]({{ p.url | relative_url }})
{%- endif -%}
{%- endfor -%}
{%- endcapture -%}
{%- if tlist != "" %}

Search for your symptom. Each page says what you see, why it happens, and what to do about
it — including which version fixed it, if it was a bug.

If your problem is not here, the form to report it is at the bottom of this page, along with
the two steps that make a report fixable.

## Pages
{{ tlist }}
{% endif %}

## Report a problem

Found a bug, or something that does not behave the way the reference says it should?

[**Report a problem →**](https://tally.so/r/MepAQM)

**No account or sign-in is required.** The form asks what you saw and how to reproduce it.

**Easiest — from inside Grasshopper** (Antlion 1.0.2 or later): right-click the
<strong translate="no">License</strong> component → <strong translate="no">Report a problem</strong>. It opens this form
with your Antlion, Rhino and Windows versions already attached.
It also attaches the document's units, the last six characters of your license key and the most
recent error message, which can contain file paths — see the [privacy policy](../../privacy/index.md).

**If the plugin does not load**, use the link above and include your Rhino and Windows details: run
<code translate="no">SystemInfo</code> in Rhino, right-click the text in the window that opens →
<strong translate="no">Copy All</strong>, and paste it into the form.

### Two things that make a report fixable

New to Grasshopper? These are the two steps people most often miss. Either one on its own
usually lets us find the cause without asking you anything further.

**1 — Internalise the geometry before you save the file.**
A Grasshopper definition only *references* the curves and surfaces in your Rhino document.
Sent as-is, it opens empty on our side and there is nothing to look at.

- Select the components you used, or just the input parameters holding your Rhino geometry
- Right-click that input → <strong translate="no">Internalise data</strong>
- The wire to Rhino disappears and the geometry is now stored inside the definition
- <strong translate="no">File → Save Document As…</strong>, and attach that copy

The internalised file contains only the geometry you internalised — not your Rhino document.

**2 — Or paste the debug output instead.**
Most Antlion components have a **<code translate="no">Debug</code>** output, and it is often faster than sending files.

- Double-click empty canvas, type <code translate="no">panel</code>, press Enter
- Drag a wire from the component's **<code translate="no">Debug</code>** output into that panel
- Right-click the panel → <strong translate="no">Copy Data Only</strong>
- Paste it into the report form

If the component shows an orange or red bubble, copy that message too: right-click the
component → <strong translate="no">Runtime warnings</strong> (or <strong translate="no">Runtime errors</strong>)
and click the message — that puts it on the clipboard.

Attaching the Grasshopper definition that shows the problem is the single most useful thing
you can do — please **internalize the input geometry** first, so the definition reproduces
on its own without your Rhino model. Screenshots are fine for anything visual.
**We do not ask for your model file.**

Every fix ships in a release and is listed in the [changelog](../changelog/index.md). Leave an
email if you want to be told when yours is fixed, and a display name if you would like the
credit in the release notes.

Subscription, payment and invoice questions are handled by **Polar**, the merchant of record
for this product — use the customer portal (the link in your purchase email, or right-click
<strong translate="no">License</strong> → <strong translate="no">Manage subscription</strong>) rather than the report form.
