---
title: The Antlion workflow
description: The whole Antlion chain as one map, the standard component combinations that actually run, and where each component sits in the ribbon.
wide: true
full: true
---

{%- assign prod = site.data.products | where: "slug", "antlion" | first -%}
{%- assign pdata = site.data.components.products.antlion -%}
{%- assign g = pdata.graph -%}

<p class="label">Track 1 · Concept</p>

# What order to use things in

Most of the difficulty in a Grasshopper plugin is not *what exists* — it is *what comes
next*. This page has three answers to that, in order: the chain as a map, the combinations
people actually build, and where each component sits in the ribbon.

**The chain is not a single line.** Two strands run side by side — the plan and the section
— and they meet at the 2D layout. A few connections even run back up it.

{% include board.html %}

## Combinations that actually run

These are not made-up examples. Each one is a definition our test harness builds and solves
in Rhino, so if the plugin changes underneath them, they break there before they mislead you
here. Click any component to read what it does.

{% include combos.html %}

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

## Where things sit in the ribbon {#ribbon}

{% include ribbon-fig.html %}

{% include antlion-ribbon.html %}

## How the ports connect

A connection is allowed when the two ports carry the same type, when the input still has
room — an *item* input holds one wire, a *list* input holds several — and when it does not
loop back on itself. Those are the only three rules, and they are Grasshopper's own.

Types are the short port nicknames you see on the canvas. The plugin keeps them stable when
a component is renamed, which is exactly why a wire survives a rename. Every component page
carries its full port table and a diagram of where each port sits on the capsule.
