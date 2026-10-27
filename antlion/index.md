---
title: "Antlion — Stadium Seating and C-value Sightlines for Grasshopper"
description: Grasshopper plugin for stadium seating bowls in Rhino 8 — sections, stands, vomitories and seats as one editable chain, with C-value sightlines checked as you design.
layout: a
bare: true
---

{%- assign prod = site.data.products | where: "slug", "antlion" | first -%}
{%- assign rel = site.data.changelog.antlion | first -%}

<section class="a-hero" aria-labelledby="top-h"><div class="a-wrap a-hero-grid">
<h1 id="top-h">Design the bowl. Don't just generate it.</h1>
<p class="a-lead">Antlion is a Grasshopper plugin for stadium seating bowls in Rhino 8. Sections, stands, vomitories and seats stay one editable chain, and C-value sightlines are checked as you design.</p>
<figure class="a-hero-fig">
{% include pic.html key="assets/img/antlion/landing/hero-3d" alt="A three-tier soccer bowl in 3D, first as a white model, then with each seat colored by its C-value." sizes="(min-width: 1200px) 660px, (min-width: 861px) 56vw, 100vw" eager=true %}
<figcaption>A three-tier soccer bowl, each seat colored by its C-value.</figcaption>
</figure>
<aside class="a-spec" id="get-antlion" aria-label="Antlion at a glance">
<dl>
<dt>Version</dt><dd>{{ rel.version }}</dd>
<dt>Updated</dt><dd>{{ rel.date }}</dd>
<dt>Runs on</dt><dd>{{ prod.runs_on }}</dd>
<dt>Units</dt><dd>{{ prod.units }}</dd>
<dt>Install</dt><dd>Rhino Package Manager — free download</dd>
<dt>License</dt><dd>Util components work without one; the rest need a plan</dd>
</dl>
<a class="a-btn" href="{{ site.f4r_url }}">Get Antlion on Food4Rhino</a>
<p class="a-fine">Pricing and plans are on Food4Rhino. Checkout asks you to accept the <a href="/antlion/eula/">EULA</a>.</p>
</aside>
</div></section>

<section class="a-sec" aria-labelledby="how-h"><div class="a-wrap">
<div class="a-sec-head"><h2 id="how-h">How it works</h2><p>Each step feeds the next: change the start line and everything after it follows.</p></div>
<svg class="a-rake" viewBox="0 0 1000 56" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0 52 H200 V41 H400 V30 H600 V19 H800 V8 H1000"/><circle cx="6" cy="52" r="3.5"/><circle cx="206" cy="41" r="3.5"/><circle cx="406" cy="30" r="3.5"/><circle cx="606" cy="19" r="3.5"/><circle cx="806" cy="8" r="3.5"/></svg>
{%- assign steps = "Place the field, draw where the front row starts, set the section axes — or use your own curves.|Draw the stair profile, solve it from a target C-value, or read it from a workbook.|Unroll it onto the plan, place vomitories and seats, cut the bowl to shape.|Stands, vomitory stairs, railings and seats as solids.|C-value for every seat and tread band; section checks draw their evidence." | split: "|" -%}
{%- assign figs = "1-plan,2-section,3-seats,4-3d,5-analysis" | split: "," -%}
{%- assign alts = "The field with the start line and the section axes around it.|Three tiers of stepped sections with sightlines to the focal point.|The bowl in plan with every seat laid out and the vomitories cut in.|A close view of the stand solids as a white model: stepped treads, aisle stairs and vomitory openings.|The same view with every seat colored by its C-value." | split: "|" %}
<ol class="a-flow">
{%- for s in prod.flow.spine %}
{%- assign i = forloop.index0 %}
<li><span class="num">{{ forloop.index | prepend: "0" }}</span><h3>{{ s.label }}</h3><p>{{ steps[i] }}</p>
{%- capture k %}assets/img/antlion/how/{{ figs[i] }}{% endcapture %}{% capture kd %}{{ k }}-dark{% endcapture %}{% assign al = alts[i] %}
{% include pic.html key=k dark=kd alt=al sizes="(min-width: 961px) 220px, 300px" %}</li>
{%- endfor %}
</ol>
<p class="a-tail">Section and tier values can live in Excel or Google Sheets; results go back there. <a href="/antlion/workflow/">See the workflow</a></p>
</div></section>

<section class="a-sec" aria-labelledby="decide-h"><div class="a-wrap">
<div class="a-sec-head"><h2 id="decide-h">Before you decide</h2></div>
<div class="a-qa">
<article><h3>Is it maintained?</h3><p>The latest release, {{ rel.version }} ({{ rel.date }}): {{ rel.title }}.</p><p><a href="/antlion/changelog/">Read the changelog</a></p></article>
<article><h3>Will it run on my setup?</h3><p>Yes, if Rhino runs on .NET Core — the default.</p><p><a href="/antlion/getting-started/#what-you-need">What you need</a></p></article>
<article id="report-a-problem"><h3>What if something breaks?</h3><p>No account needed: in Grasshopper, right-click <strong translate="no">License</strong> → <strong translate="no">Report a problem</strong>, and your versions come attached. If Antlion won't load, use the <a href="https://tally.so/r/MepAQM">report form</a>. Billing questions go to Polar, the merchant of record.</p><p><a href="/antlion/troubleshooting/#report-a-problem">How to write a report that gets fixed</a></p></article>
<article><h3>Where is it going?</h3><p>Antlion covers the seating bowl today. Later versions add structure and circulation, then the facade and roof.</p><p><a href="/antlion/roadmap/">See the roadmap</a></p></article>
</div>
</div></section>

<section class="a-sec" aria-labelledby="go-h"><div class="a-wrap">
<div class="a-sec-head"><h2 id="go-h">Where to start</h2></div>
<ul class="a-go">
<li><a href="/antlion/getting-started/"><b>Getting started</b><span>Install and register.</span></a></li>
<li><a href="/antlion/components/"><b>Components</b><span>Every port, regenerated each release.</span></a></li>
<li><a href="/antlion/tutorials/"><b>Tutorials</b><span>Videos with chapters.</span></a></li>
</ul>
<p class="a-tail" id="who-h">Antlion is built and maintained by Plugin Dev Lab, which works on design automation for Rhino and Grasshopper.</p>
</div></section>
