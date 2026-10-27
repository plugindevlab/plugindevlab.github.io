---
title: plugin.dev.lab
description: Design-workflow plugins for Rhino and Grasshopper — automate the workflow, keep the design yours.
layout: a
bare: true
---

<section class="a-house" aria-labelledby="house-h"><div class="a-wrap">
<h1 id="house-h">Automate the workflow, keep the design yours.</h1>
<p class="a-lead">Plugin Dev Lab makes design-workflow plugins for Rhino and Grasshopper.</p>
<h2 class="vh">Products</h2>
{%- for p in site.data.products %}
{%- assign rel = site.data.changelog[p.slug] | first %}
<article class="a-card" aria-labelledby="card-{{ p.slug }}">
{%- if p.card_pic %}
{% include pic.html key=p.card_pic dark=p.card_pic_dark alt=p.card_pic_alt sizes="(min-width: 1200px) 640px, (min-width: 761px) 55vw, 100vw" %}
{%- endif %}
<div class="a-card-body">
<h2 id="card-{{ p.slug }}" translate="no">{{ p.name }}</h2>
<p>{{ p.tagline }}</p>
{%- if p.status == "shipped" %}
<p class="a-facts">{{ rel.version }} · {{ rel.date }} · {{ p.runs_on }}</p>
<a class="a-btn" href="/{{ p.slug }}/">Open {{ p.name }}</a>
<p class="a-more"><a href="/{{ p.slug }}/components/">Components</a> · <a href="/{{ p.slug }}/changelog/">Changelog</a></p>
{%- else %}
<p class="a-facts">In development</p>
{%- endif %}
</div>
</article>
{%- endfor %}
<p class="a-house-note">Every plugin here is documented from its own source. Nothing on this site asks you to sign up.</p>
</div></section>
