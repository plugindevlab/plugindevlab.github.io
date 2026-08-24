---
title: plugin.dev.lab
description: Design-workflow plugins for Rhino and Grasshopper — automate the workflow, keep the design yours.
---

<p class="label">Rhino · Grasshopper</p>

# Automate the workflow, keep the design yours.

Design-workflow plugins for Rhino and Grasshopper. Each one takes a job that eats days of
an architect's time and makes it a chain you can keep editing — not a black box that hands
back a result you cannot argue with.

<div class="grid" markdown="0">
{%- for p in site.data.products %}
  <div class="card">
    <div class="fig-wait">Image to come</div>
    <h3>{% if p.status == "shipped" %}<a href="/{{ p.slug }}/">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}</h3>
    <p>{{ p.tagline }}</p>
    {%- if p.status == "shipped" %}
    <p><a href="/{{ p.slug }}/workflow/">Workflow</a> · <a href="/{{ p.slug }}/reference/">Reference</a> · <a href="/{{ p.slug }}/changelog/">Changelog</a></p>
    {%- else %}
    <p class="label">In development</p>
    {%- endif %}
  </div>
{%- endfor %}
</div>

## How these are built

Every plugin here is documented from its own source. The component reference is generated
from the plugin binary, so it cannot drift from the version you are running — if a port is
renamed, the page changes with it. Bugs are fixed and shipped continuously, and each
product's changelog is the record of that.

Reports do not require an account. Nothing on this site asks you to sign up.
