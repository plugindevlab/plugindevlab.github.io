---
title: The Antlion workflow
description: The whole Antlion chain as one map — plan, section, 2D layout, 3D solids, analysis. What order to use things in.
wide: true
---

{%- assign prod = site.data.products | where: "slug", "antlion" | first -%}
{%- assign wf = site.data.workflow.antlion -%}

<p class="label">Track 1 · Concept</p>

# What order to use things in

Most of the difficulty in a Grasshopper plugin is not *what exists* — it is *what comes
next*. This is the whole chain in one view. Follow it left to right, and branch where your
design needs to.

If you already know the plugin and just want a component, go to the
[reference](../reference/index.md) instead — same pages, a different door.

<div class="map-wrap" markdown="0">
<svg class="map" viewBox="0 0 1000 290" role="img" aria-label="The Antlion workflow, five stages left to right with two side groups">
  {%- assign step = 208 -%}
  {%- for s in prod.flow.spine -%}
  {%- assign g = wf[s.group] -%}
  {%- assign x = forloop.index0 | times: step -%}
  {%- unless forloop.last %}
  <path class="map-arrow" d="M{{ x | plus: 172 }} 79 H{{ x | plus: 202 }}" marker-end="url(#mk)"/>
  {%- endunless %}
  <a href="#{{ s.group }}">
    <title>{{ s.label }} — {{ g.count }} components</title>
    <rect class="map-node" x="{{ x }}" y="40" width="168" height="78" rx="2"/>
    <text class="map-n" x="{{ x | plus: 16 }}" y="66">{{ forloop.index }}</text>
    <text class="map-t" x="{{ x | plus: 16 }}" y="90">{{ s.label }}</text>
    <text class="map-c" x="{{ x | plus: 16 }}" y="107">{{ g.count }} components</text>
  </a>
  {%- endfor -%}

  {%- for a in prod.flow.aside -%}
  {%- assign g = wf[a.group] -%}
  {%- assign ax = a.col | times: step -%}
  {%- if a.into != "" %}
  <path class="map-arrow map-dash" d="M{{ ax | plus: 84 }} 200 V128" marker-end="url(#mk)"/>
  {%- endif %}
  <a href="#{{ a.group }}">
    <title>{{ a.label }} — {{ g.count }} components</title>
    <rect class="map-node map-aside" x="{{ ax }}" y="200" width="168" height="62" rx="2"/>
    <text class="map-t" x="{{ ax | plus: 16 }}" y="228">{{ a.label }}</text>
    <text class="map-c" x="{{ ax | plus: 16 }}" y="246">{{ g.count }} components</text>
  </a>
  {%- endfor %}

  <defs>
    <marker id="mk" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L8 4 L0 8 z" class="map-head"/>
    </marker>
  </defs>
</svg>
</div>

Each box is a stage. Click one to see what is in it, then click a component to read what it
does and what to wire into it.

## The stages

{% for s in prod.flow.spine %}
{%- assign g = wf[s.group] %}
<section class="split{% cycle '', ' flip' %}" id="{{ s.group }}" markdown="0">
<div class="split-text">
<p class="label">Stage {{ forloop.index }} · {{ g.path }}</p>
<h3>{{ s.label }}</h3>
{{ site.data.stage_notes[s.group] | markdownify }}
<p class="comp-list">
{%- for c in g.components %}<a href="../reference/{{ c.page }}.html#{{ c.anchor }}">{{ c.name }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}
</p>
<p><a href="../reference/{{ g.page }}.html">All {{ g.count }} in the reference</a></p>
</div>
<figure class="fig"><div class="fig-wait">Image to come</div></figure>
</section>
{% endfor %}

## Alongside the chain

{% for a in prod.flow.aside %}
{%- assign g = wf[a.group] %}
<section id="{{ a.group }}" markdown="0">
<p class="label">{{ g.path }}</p>
<h3>{{ a.label }}</h3>
{{ site.data.stage_notes[a.group] | markdownify }}
<p class="comp-list">
{%- for c in g.components %}<a href="../reference/{{ c.page }}.html#{{ c.anchor }}">{{ c.name }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}
</p>
</section>
{% endfor %}

## Wiring the chain

From the 2D layout on, each component's outputs match the next component's inputs
top-to-bottom, one to one — wire them straight down in order. The
[reference index](../reference/index.md) carries the full chain diagram, including the
branches and which bundled ports carry the chain between stages.
