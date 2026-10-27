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

Setup is three steps, and none of it touches your Rhino model.

<ol class="a-steps">
<li id="install"><div><h2>Install</h2>
<ol class="a-do">
<li>In Rhino, run <code>_PackageManager</code> — the download button on Food4Rhino opens it at Antlion.</li>
<li>Search for <strong>Antlion</strong> and install it.</li>
<li>Restart Rhino.</li>
<li>Open Grasshopper. There is now an <strong>Antlion</strong> tab in the ribbon — <a href="/antlion/workflow/#ribbon">what sits in each panel</a>.</li>
</ol>
<p><strong>No tab after restarting?</strong> Rhino is almost certainly in .NET Framework mode — see <a href="#what-you-need">What you need</a>.</p>
<p>Antlion comes <strong>through the package manager only</strong>. We do not publish <code>.gha</code> or <code>.yak</code> files for download, so a direct file download did not come from us.</p>
<details class="a-more-d"><summary>Updates</summary>
<p>New releases arrive through the package manager. At the bottom of its window, keep <strong>Automatically update packages when Rhino starts</strong> checked — it is on unless someone turned it off. Rhino then installs newer packages shortly after it starts and asks you to restart; the new version runs from that restart.</p>
<p>If you keep it off, run <code>_PackageManager</code>, select Antlion and click <strong>Install</strong> on the newer version. The <a href="/antlion/changelog/">changelog</a> lists what changed in each release.</p>
<p><strong>Files from another version.</strong> A file saved with an older Antlion opens in a newer one with its wires and values in place; when a release removes an input or changes a default value, the changelog says what happens to older files. The other way round is not guaranteed. A file saved with a newer Antlion may use inputs your version does not have — they are left out when you open it, and from 1.1.0 the component says so. Update Antlion before saving such a file, because saving it with the older version removes those inputs for good. When several people work on the same files, keep everyone on the same version.</p>
</details>
</div>
{%- assign s = page.shots[0] %}
<figure><img src="{{ s.src }}" width="{{ s.w }}" height="{{ s.h }}" alt="{{ s.alt }}" fetchpriority="high"><figcaption>{{ s.cap }}</figcaption></figure></li>
<li class="no-fig"><div><h2>Buy a license</h2>
<p>Downloading is free. The <strong translate="no">Util</strong> panel works without a license; the <strong translate="no">Bowl</strong>, <strong translate="no">Bowl Analysis</strong> and <strong translate="no">Table</strong> panels need one.</p>
<p>{% if site.f4r_url and site.f4r_url != "" %}Buy from the <a href="{{ site.f4r_url }}">Antlion listing on Food4Rhino</a>.{% else %}<em>(Food4Rhino listing — coming with release.)</em>{% endif %} Purchases, billing and invoices are handled by Polar, the merchant of record, and the email address you enter at checkout is how you reach your key.</p>
</div></li>
<li id="register-your-license"><div><h2>Register</h2>
<ol class="a-do">
<li>Open your customer portal at <a href="https://polar.sh/plugindevlab/portal">polar.sh/plugindevlab/portal</a>, enter the email address you bought with and the code it sends you, and copy the key from the purchases page. Do not wait for it by email — the portal always has it.</li>
<li>In Grasshopper, <span translate="no">Antlion</span> tab → <a href="/antlion/components/license/"><strong translate="no">License</strong></a>: put the key in a <strong translate="no">Panel</strong> wired to <code translate="no">Key</code>.</li>
<li>Set a <strong translate="no">Toggle</strong> on <code translate="no">Register</code> to <strong translate="no">True</strong>. <code translate="no">Status</code> reports what happened.</li>
</ol>
<p>That unlocks <strong>every definition on this computer</strong> — you do not repeat it per file.</p>
<p>Registering sends your computer name, your user name on that computer and the date to Polar, so that you can tell your machines apart in the customer portal. Nothing from your models is sent — see the <a href="/privacy/">privacy policy</a>.</p>
<details class="a-more-d"><summary>Moving to another computer, and the License menu</summary>
<p><strong>One computer at a time.</strong> To move to another machine, release the old one in the customer portal and register on the new one. If a computer has been released, <code translate="no">Status</code> says so and tells you to flip <code translate="no">Register</code> again.</p>
<p>Right-click <span translate="no">License</span> to open your customer portal (<strong translate="no">Manage subscription</strong>) or to report a problem (<strong translate="no">Report a problem</strong>).</p>
{%- assign s = page.shots[2] %}
<figure class="a-natural"><img src="{{ s.src }}" width="{{ s.w }}" height="{{ s.h }}" alt="{{ s.alt }}" loading="lazy" decoding="async"><figcaption>{{ s.cap }}</figcaption></figure>
</details>
</div>
{%- assign s = page.shots[1] %}
<figure><img src="{{ s.src }}" width="{{ s.w }}" height="{{ s.h }}" alt="{{ s.alt }}" loading="lazy" decoding="async"><figcaption>{{ s.cap }}</figcaption></figure></li>
</ol>

## What you need

- **Rhino 8** for Windows or Mac, with Grasshopper. The Mac version is a beta - see [Mac (beta)](#mac-beta) below.
- **Rhino running on .NET Core** — the current default. If Rhino was switched to .NET
  Framework mode for some other plugin, Antlion does not load at all and the tab never
  appears. Run `SetDotNetRuntime` in Rhino to check it, switch back, and restart.
- **Millimeter or inch documents** — both work.
- **An internet connection when you register.** After that Antlion checks in quietly in the
  background and rides out short network outages.

### Mac (beta)

Antlion runs on Rhino 8 for Mac from 1.1.0. It is the same plugin, with a few differences:

- **Help cards** open in a standard Mac window instead of the floating card on the canvas. Move it by its title bar and resize it from its edges.
- **Excel Workbook** - close the workbook in Excel before you press Run. Writing into a workbook that is open in Excel works on Windows only.
- **Google Workbook** - you sign in to Google again each time you start Rhino.

Something not working on Mac? Right-click the **License** component and choose **Report a problem** - it attaches your Rhino and macOS versions.

## Where to go next

- [**Workflow**](../workflow/index.md) — the whole chain as one diagram, and what order to
  use things in. Start here.
- [**Tutorials**](../tutorials/index.html) — video walkthroughs that build a stadium bowl step by
  step, with chapters you can jump to.

## When something does not work

Start with [Troubleshooting](../troubleshooting/index.md). If your symptom is not there,
[report it](../troubleshooting/index.md#report-a-problem) — no account needed.
