---
title: Antlion troubleshooting
description: Known symptoms in Antlion for Rhino and Grasshopper — what causes them and how to fix them.
---

# Troubleshooting

How to report a problem so that it gets fixed.

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
**No account or sign-in is required.**

<p><a class="a-btn" href="https://tally.so/r/MepAQM">Report a problem</a></p>

<div class="a-routes">
<section>
<h3>From Grasshopper</h3>
<p>Antlion 1.0.2 or later: right-click the <strong translate="no">License</strong> component →
<strong translate="no">Report a problem</strong>.</p>
<p>The form opens with your Antlion, Rhino and Windows or macOS versions attached, plus the document's units,
the last six characters of your license key and the most recent error message, which can contain file paths —
see the <a href="/privacy/">privacy policy</a>.</p>
</section>
<section>
<h3>If the plugin does not load</h3>
<p>Use the button above. In Rhino, run <code translate="no">SystemInfo</code>, right-click the text in the window
that opens → <strong translate="no">Copy All</strong>, and paste it into the form.</p>
</section>
<section>
<h3>Subscription, payment or invoice?</h3>
<p>Those go to <strong>Polar</strong>, the merchant of record, not the report form — use the customer portal
(the link in your purchase email, or right-click <strong translate="no">License</strong> →
<strong translate="no">Manage subscription</strong>).</p>
</section>
</div>

### Two things that make a report fixable

New to Grasshopper? These are the two steps people most often miss. Either one usually lets us find the cause
without asking you anything further.

<div class="a-two">
<section>
<h4>1 — Attach the definition, with its geometry internalised</h4>
<p>A definition only <em>references</em> the curves and surfaces in your Rhino document, so sent as-is it opens empty on our side.</p>
<ol>
<li>Select the input parameters holding your Rhino geometry (or the components you used).</li>
<li>Right-click → <strong translate="no">Internalise data</strong>. The wire to Rhino disappears; the geometry is now stored inside the definition.</li>
<li><strong translate="no">File → Save Document As…</strong>, and attach that copy.</li>
</ol>
<p>The copy holds only the geometry you internalised, not your Rhino document — <strong>we do not ask for your model
file.</strong> Screenshots are fine for anything visual.</p>
</section>
<section>
<h4>2 — Or paste the debug output instead</h4>
<p>Most Antlion components have a <strong><code translate="no">Debug</code></strong> output, and it is often faster than sending files.</p>
<ol>
<li>Double-click empty canvas, type <code translate="no">panel</code>, press Enter.</li>
<li>Drag a wire from the component's <strong><code translate="no">Debug</code></strong> output into that panel.</li>
<li>Right-click the panel → <strong translate="no">Copy Data Only</strong>, and paste it into the report form.</li>
</ol>
<p>An orange or red bubble on the component? Right-click it → <strong translate="no">Runtime warnings</strong>
(or <strong translate="no">Runtime errors</strong>) and click the message to copy it too.</p>
</section>
</div>

Every fix ships in a release and is listed in the [changelog](../changelog/index.md). Leave an email in the
form to hear when yours is fixed, and a display name if you would like the credit in the release notes.
