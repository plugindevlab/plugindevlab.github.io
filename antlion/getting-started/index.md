---
title: Getting started with Antlion
description: What you need, how to install Antlion from the Rhino package manager, and how to register your licence key.
---

# Getting started

<section class="split">
<div class="split-text" markdown="1">
Setup is three things: install from the Rhino package manager, register a licence key once,
and open Grasshopper. None of it touches your Rhino model.

Once the **Antlion** tab is in the ribbon, [the workflow](../workflow/index.md) shows what
order to use things in — that page is where the first bowl gets built.
</div>
<figure class="fig">
<div class="fig-wait">Image to come</div>
<figcaption>A bowl built with Antlion — sections, stands, vomitories and seats from one chain.</figcaption>
</figure>
</section>

## What you need

- **Rhino 8 for Windows**, with Grasshopper. Antlion is Windows-only for now.
- **Rhino running on .NET Core** — the current default. If Rhino was switched to .NET
  Framework mode for some other plugin, Antlion does not load at all and the tab never
  appears. Run `SetDotNetRuntime` in Rhino to check it, switch back, and restart.
- **Millimetre or inch documents** — both work.
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

The Food4Rhino listing carries the product description and the purchase route — its download
button opens the same package manager entry rather than handing you a file.

*(Food4Rhino listing — coming with release.)*

## Register your licence

Downloading Antlion is free. The **Util** panel works without a licence; the **Bowl**,
**Bowl Analysis** and **Table** panels need one.

**1 — Take the key from your customer portal.** Purchases, billing and invoices are handled
by **Polar**, the merchant of record for this product, and your licence key lives in the
customer portal there. Do not wait for it to arrive by email — the portal always has it.
Enter the email address you bought with, type the code it sends you, and copy the key from
the purchases page.

*(Customer portal — coming with release.)*

**2 — Enter it once in Grasshopper.**

- Antlion tab → [**License**](../components/license/index.html)
- Paste the key into `Key`
- Set `Register` to **True**
- `Status` reports what happened

That unlocks **every definition on this computer** — it is not something you repeat per file.

**One computer at a time.** To move to another machine, release the old one in the customer
portal and register on the new one. If a computer has been released, `Status` says so and
tells you to flip `Register` again.

*(Video walkthrough — coming with release.)*

## Where to go next

- [**Workflow**](../workflow/index.md) — the whole chain as one diagram, and what order to
  use things in. Start here.
- [**Tutorials**](../tutorials/index.md) — the parts where the rules are not visible on screen.

## When something does not work

Start with [Troubleshooting](../troubleshooting/index.md). If your symptom is not there,
[report it](../troubleshooting/index.md#report-a-problem) — no account needed.
