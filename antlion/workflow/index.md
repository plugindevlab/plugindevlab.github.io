---
title: The Antlion workflow
description: Where every component sits in the ribbon, and the whole chain as one diagram — what order to use things in.
wide: true
full: true
---

{%- assign prod = site.data.products | where: "slug", "antlion" | first -%}
{%- assign pdata = site.data.components.products.antlion -%}
{%- assign g = pdata.graph -%}

<p class="label">Track 1 · Concept</p>

# What order to use things in

Most of the difficulty in a Grasshopper plugin is not *what exists* — it is *what comes
next*. This page answers that twice: first where every component sits in the ribbon, then
the whole chain as a single diagram.

## Where things sit in the ribbon {#ribbon}

{% include ribbon-fig.html %}

The tab holds four panels, and the panels are not four categories of thing — they are four
kinds of work. **Bowl** builds geometry, and it is by far the largest because everything
downstream hangs off it. **Bowl Analysis** measures what Bowl built: sightlines, C-values,
seat maps, and the guides that make them legible. **Table** connects a workbook, so the
numbers you would otherwise retype live in Excel or Google Sheets and come back in.
**Util** is everything that helps without being part of the chain — a values panel, a
legend, sheet setup, the licence.

**Inside a panel, the separators are the order of work, not a grouping of similar things.**
Read a panel left to right, section by section, and you are reading the sequence you would
actually build in. In Bowl that means the start line first, then the section through the
stand, then the plan layout, then the 3D bodies. In Bowl Analysis it is the 2D check, then
the 3D checks, then the drawings, then the on-screen guides. Nothing about that order is
decoration: a component in a later section usually cannot run until something from an
earlier one has produced its result.

That ordering is worth one warning, because it was broken until recently. Grasshopper sorts
a panel by exposure first and then by name, so the only way to control the order inside a
section is the name itself. Antlion carries an invisible sort prefix to do that, and on
Rhino 8 the prefix it used was discarded by the runtime — every section quietly fell back to
alphabetical. It is fixed, so what you see above is the intended order, but if you have an
older build the panels will read alphabetically instead.

{% include antlion-ribbon.html %}

## The whole chain in one diagram

Everything below is one picture on purpose. The chain is not a single line: two strands run
side by side — the plan and the section — and they meet at the 2D layout. Follow it left to
right; every shape is a link to that component's page.

{% include flowmap.html %}

**Arrows are order, not wiring.** Most of them are a real connection you could make on the
canvas, but a few say *do this first* where no wire exists — the axis before the section,
the bowl before you put a guide on it. The component pages carry the ports; this diagram
carries the sequence.

**Dotted links mean "instead of", not "as well as".** A custom start line replaces the built-in
one; a table-driven section replaces the section you set by hand. Wire one or the other.

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

## How the ports connect

A connection is allowed when the two ports carry the same type, when the input still has
room — an *item* input holds one wire, a *list* input holds several — and when it does not
loop back on itself. Those are the only three rules, and they are Grasshopper's own.

Types are the short port nicknames you see on the canvas. The plugin keeps them stable when
a component is renamed, which is exactly why a wire survives a rename. Every component page
carries its full port table and a diagram of where each port sits on the capsule.
