---
title: The Antlion workflow
description: The four ribbon panels and what each is for, then the whole chain as one diagram.
wide: true
full: true
---

{%- assign prod = site.data.products | where: "slug", "antlion" | first -%}
{%- assign pdata = site.data.components.products.antlion -%}
{%- assign g = pdata.graph -%}

<p class="label">Track 1 · Concept</p>

# What order to use things in

Most of the difficulty in a Grasshopper plugin is not *what exists* — it is *what comes
next*. This page answers that twice: the four panels in the ribbon, then the whole chain
as a single diagram.

## Where things sit in the ribbon {#ribbon}

{% include ribbon-fig.html %}

**Bowl** builds geometry — start lines, sections, the 2D layout, the solids.
**Bowl Analysis** measures what Bowl built: sightlines, C-values, seat maps, and the guides
that make them legible. **Table** connects a workbook, so numbers live in Excel or Google
Sheets instead of in sliders. **Util** is everything that helps without being part of the
chain — a values panel, a legend, sheet setup, the licence.

**Inside a panel, the separators are the order of work.** Read a panel left to right,
section by section, and you are reading the sequence you would actually build in.

## The whole chain in one diagram

The chain is not a single line: two strands run side by side — the plan and the section —
and they meet at the 2D layout. Follow it left to right; every shape links to that
component's page.

{% include flowmap.html %}

**Arrows are order, not wiring.** Nearly all of them are a real connection you could make on
the canvas, but not every one is — the axis comes before the section even though nothing runs
between the two. **Dotted links mean "instead of", not "as well as":** a custom start line
replaces the built-in one; a table-driven section replaces the one you set by hand.

## The stages

{% for s in g.stages %}
{%- unless s.aside %}
<section class="split{% cycle '', ' flip' %}" id="{{ s.group }}" markdown="0">
<div class="split-text">
<p class="label">Stage {{ forloop.index }}</p>
<h3>{{ s.label }}</h3>
{{ site.data.stage_notes[s.group] | markdownify }}
<p class="comp-list">
{%- for c in g.components %}{% if c.group == s.group %}<a href="../components/{{ c.id }}/">{{ c.name }}</a> {% endif %}{% endfor %}
</p>
</div>
<figure class="fig"><div class="fig-wait">Image to come</div></figure>
</section>
{%- endunless %}
{% endfor %}

## Alongside the chain

{% for s in g.stages %}
{%- if s.aside %}
<section id="{{ s.group }}" markdown="0">
<h3>{{ s.label }}</h3>
{{ site.data.stage_notes[s.group] | markdownify }}
<p class="comp-list">
{%- for c in g.components %}{% if c.group == s.group %}<a href="../components/{{ c.id }}/">{{ c.name }}</a> {% endif %}{% endfor %}
</p>
</section>
{%- endif %}
{% endfor %}
