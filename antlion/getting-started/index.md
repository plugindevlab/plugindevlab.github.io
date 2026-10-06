---
title: Getting started with Antlion
description: What you need, how to install Antlion from the Rhino package manager, and how to register your license key.
shots:
  - src: /assets/img/antlion/getting-started/package-manager.png
    w: 786
    h: 538
    alt: "Rhino's package manager with Antlion found by search and the Install button."
    cap: "Antlion in the Rhino package manager."
  - src: /assets/img/antlion/getting-started/register.png
    w: 1500
    h: 1000
    alt: "The License component in Grasshopper with the key in a Panel, blacked out, and Toggles set to True on Register and Diagnose."
    cap: 'Registering in Grasshopper: the key in a <span translate="no">Panel</span>, a <span translate="no">Toggle</span> on <code translate="no">Register</code>. The key is blacked out; the panel on the right is the <code translate="no">Diagnose</code> connection test.'
  - src: /assets/img/antlion/getting-started/license-menu.png
    w: 550
    h: 367
    alt: "The License right-click menu with Manage subscription and Report a problem."
    cap: 'Right-click <span translate="no">License</span> for <span translate="no">Manage subscription</span> and <span translate="no">Report a problem</span>.'
---

# Getting started

<section class="split">
<div class="split-text" markdown="1">
Setup is three steps, and none of it touches your Rhino model.

1. **Install** from the Rhino package manager — the download button on Food4Rhino opens it
   at Antlion.
2. **Buy a license.** Checkout is run by Polar, and the email address you enter there is how
   you reach your key in the customer portal.
3. **Register** in Grasshopper — put the key in a <strong translate="no">Panel</strong> wired to
   <code translate="no">Key</code> on <span translate="no">License</span>, and set a
   <strong translate="no">Toggle</strong> on <code translate="no">Register</code> to True.

Right-click <span translate="no">License</span> to open your customer portal
(<strong translate="no">Manage subscription</strong>) or to report a problem
(<strong translate="no">Report a problem</strong>). Each step is spelled out below; after that,
[the workflow](../workflow/index.md) is where the first bowl gets built.
</div>
{% include carousel.html id="gs" items=page.shots label="Installing and registering Antlion" %}
</section>

## What you need

- **Rhino 8 for Windows**, with Grasshopper. Antlion is Windows-only for now.
- **Rhino running on .NET Core** — the current default. If Rhino was switched to .NET
  Framework mode for some other plugin, Antlion does not load at all and the tab never
  appears. Run `SetDotNetRuntime` in Rhino to check it, switch back, and restart.
- **Millimeter or inch documents** — both work.
- **An internet connection when you register.** After that Antlion checks in quietly in the
  background and rides out short network outages.

## Install

1. In Rhino, run `_PackageManager`.
2. Search for **Antlion** and install it.
3. Restart Rhino.
4. Open Grasshopper. There is now an **Antlion** tab in the ribbon —
   [what sits in each panel](../workflow/index.md#ribbon).

**No tab after restarting?** Rhino is almost certainly in .NET Framework mode. See
*What you need* above; that one setting accounts for most "the components are not there"
reports.

Antlion is distributed **through the package manager only.** We do not publish `.gha` or
`.yak` files for download anywhere, so a copy offered as a direct file download did not come
from us.

**Updates arrive the same way.** New releases of Antlion are published to the package manager.
At the bottom of the package manager window, keep **Automatically update packages when Rhino
starts** checked — it is on unless someone turned it off. Rhino then looks for newer packages
shortly after it starts, installs them and asks you to restart; the new version runs from that
restart. If you keep it off, run `_PackageManager`, select Antlion and click **Install** on the
newer version. The [changelog](../changelog/index.md) lists what changed in each release.

The Food4Rhino listing carries the product description and the purchase route — its download
button opens the same package manager entry rather than handing you a file.

{% if site.f4r_url and site.f4r_url != "" %}<strong><a href="{{ site.f4r_url }}">Antlion on Food4Rhino</a></strong>{% else %}*(Food4Rhino listing — coming with release.)*{% endif %}

## Register your license

Downloading Antlion is free. The <strong translate="no">Util</strong> panel works without a license; the <strong translate="no">Bowl</strong>,
<strong translate="no">Bowl Analysis</strong> and <strong translate="no">Table</strong> panels need one.

**1 — Take the key from your customer portal.** Purchases, billing and invoices are handled
by **Polar**, the merchant of record for this product, and your license key lives in the
customer portal there. Do not wait for it to arrive by email — the portal always has it.
Enter the email address you bought with, type the code it sends you, and copy the key from
the purchases page.

Customer portal: [polar.sh/plugindevlab/portal](https://polar.sh/plugindevlab/portal)

**2 — Enter it once in Grasshopper.**

- <span translate="no">Antlion</span> tab → [<strong translate="no">License</strong>](../components/license/index.html)
- Paste the key into <code translate="no">Key</code>
- Set <code translate="no">Register</code> to <strong translate="no">True</strong>
- <code translate="no">Status</code> reports what happened

That unlocks **every definition on this computer** — it is not something you repeat per file.

Registering sends your computer name, your Windows user name and the date to Polar, so that you
can tell your machines apart in the customer portal. Nothing from your models is sent — see the
[privacy policy](../../privacy/index.md).

**One computer at a time.** To move to another machine, release the old one in the customer
portal and register on the new one. If a computer has been released, <code translate="no">Status</code> says so and
tells you to flip <code translate="no">Register</code> again.

## Where to go next

- [**Workflow**](../workflow/index.md) — the whole chain as one diagram, and what order to
  use things in. Start here.
- [**Tutorials**](../tutorials/index.html) — video walkthroughs that build a stadium bowl step by
  step, with chapters you can jump to.

## When something does not work

Start with [Troubleshooting](../troubleshooting/index.md). If your symptom is not there,
[report it](../troubleshooting/index.md#report-a-problem) — no account needed.
