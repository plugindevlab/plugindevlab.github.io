---
title: Privacy policy
description: What personal data plugin.dev.lab processes, why, where it goes, and your rights.
effective: "2026-10-27"
---

# Privacy policy

<p class="legal-meta">Plugin Dev Lab ("we", "us") — operating as <strong>plugin.dev.lab</strong><br>
Contact: <strong>founder@plugindevlab.com</strong><br>
Published at: {{ page.url | absolute_url }}<br>
Version 1.6 — effective {{ page.effective }}</p>

<nav class="legal-toc" aria-label="Contents" markdown="0"><p class="label">Contents</p><ul>
<li><a href="#1-who-we-are-and-the-short-version">1. Who we are, and the short version</a></li>
<li><a href="#2-what-we-process-and-why">2. What we process, and why</a></li>
<li><a href="#3-optional-google-sheets-connection">3. Optional Google Sheets connection</a></li>
<li><a href="#4-legal-basis-and-purpose">4. Legal basis and purpose</a></li>
<li><a href="#5-processors-and-international-transfer">5. Processors and international transfer</a></li>
<li><a href="#6-retention">6. Retention</a></li>
<li><a href="#7-your-rights">7. Your rights</a></li>
<li><a href="#8-security">8. Security</a></li>
<li><a href="#9-children">9. Children</a></li>
<li><a href="#10-data-protection-officer-and-changes-to-this-policy">10. Data Protection Officer, and changes to this Policy</a></li>
</ul></nav>

This English text is the only authoritative version of this Policy.

---

## 1. Who we are, and the short version

We are **plugin.dev.lab**, publishing Grasshopper plug-ins for Rhino, of which
**Antlion** is the first. We operate **no servers of our own**. Everything described below is
handled by the third-party services we have listed, and our own access to your data is limited
to looking at those services' dashboards.

**We do not run analytics or telemetry, and your design data never leaves your machine.**
See section 2.4.

## 2. What we process, and why

### 2.1 Licence activation

When you register a licence key inside Grasshopper, the plug-in sends the following to **Polar**,
our merchant of record, so that a licence seat can be identified and released:

- **your computer name, your operating-system user name, and the date of registration**,
  combined into a single activation label
- your licence key, our organisation identifier, and an activation identifier

The label exists so that **you** can tell your own devices apart in the Polar customer portal and
release the right one. We do not use it for any other purpose. This transmission happens
automatically as part of registration and **cannot be switched off**; if you do not wish it to
happen, do not register a licence key.

### 2.2 Problem reports

If you report a problem through our form, we receive what you choose to submit: a description,
optional contact e-mail, and any file you attach. When you open the form from inside the
plug-in (the **Report a problem** menu), it also fills in technical details for you: the plug-in
version and build, your Rhino and operating-system versions, the unit system of the open document, the
last six characters of your licence key, and the most recent error message — which can include
file paths on your computer. The form is hosted by **Tally**. Giving an e-mail address is
optional — without it we simply cannot reply to you.

### 2.3 Student verification

If you apply for the student price, we receive your **name, school e-mail address and school
name** through a form hosted by **Tally**. If you have already subscribed or started a free trial,
you may also give us **the e-mail address you used at checkout**, so that we can find that
subscription and apply the discount to it; when we do, we let that address know. The answers are
recorded in a Google spreadsheet that we control; we e-mail a verification code to that school
address from our address, delivered through **Resend**, and once you enter it we apply a student
discount. The other e-mails about your student discount are delivered the same way.
Student status is re-verified every six months, so we keep your school address, the subscription
the discount is applied to, and the status of your discount while the discount is active. We
confirm student status only through a school e-mail address.

### 2.4 What we never receive

**Your models, seating layouts, geometry, and analysis results are never transmitted anywhere.**
The plug-in contains no analytics, no usage tracking, and no crash reporting. Outside the
licensing functions described above, the only component that makes a network connection at all is
`Google Workbook` — and that connection is between **you and Google**, not between you and us
(section 3).

### 2.5 E-mail you send us

If you write to us, we receive your e-mail address, your message and anything you attach. Mail
sent to our address is forwarded by **Cloudflare** to the Google (Gmail) mailbox in which we read
it, and our replies are delivered through **Resend**. We use this correspondence only to answer
you.

## 3. Optional Google Sheets connection

The `Google Workbook` component can read and write a Google spreadsheet on your behalf. If you
choose to use it:

- you sign in with **your own** Google account, and the authorisation is between you and Google;
- we request the **narrowest available scope** (`drive.file`) — access is limited to files the
  component creates or that you explicitly pick, and we deliberately do not request the broader
  spreadsheets permission;
- the resulting token stays **on your computer** and is never transmitted to us. On Windows it
  is stored encrypted with Windows DPAPI; on macOS it is kept in memory only and never written
  to disk, so you sign in again each time you start Rhino;
- **we receive nothing** from this feature, including the contents of your spreadsheets.

You can revoke this access at any time in your Google account settings.

## 4. Legal basis and purpose

We process the data in section 2 to perform the contract you entered into when purchasing a
licence (delivering and enforcing that licence), to respond to support requests you initiate, and
to verify eligibility for a discount you applied for. We do not process personal data for
marketing, and we do not sell or otherwise transfer personal data to third parties for their own
purposes.

## 5. Processors and international transfer

We do not have our own storage. The following processors hold the data described above, and
they store it principally in the **United States**:

- **Polar Software, Inc.** — payment, subscription, and licence-key management (section 2.1).
  Polar acts as merchant of record and is the seller of record for your purchase; billing details
  are held by Polar under its own privacy policy, and we never see your full payment information.
- **Tally** — problem-report form and attachments (section 2.2), and the student-verification
  forms (section 2.3).
- **Google LLC** — the spreadsheet that records student verification (section 2.3), and the
  mailbox in which we read and answer your e-mail (section 2.5).
- **Cloudflare, Inc.** — forwarding of e-mail sent to our address (section 2.5).
- **Plus Five Five, Inc. (Resend)** — delivery of the e-mails we send, including verification
  codes and other student-discount e-mails (sections 2.3 and 2.5). Resend keeps a record of each
  e-mail it delivers for 30 days.

By using these services you accept that the data concerned is transferred to and stored in those
countries. Each processor publishes its own privacy policy governing that storage.

## 6. Retention

- **Activation labels** remain in Polar for as long as the activation exists; you can remove one at
  any time by releasing the device in the customer portal, or by asking us.
- **Customer and order records** (your name, e-mail address and purchase history) are kept by
  Polar as merchant of record under its own retention policy. We do not delete them separately,
  because they also document a sale for tax purposes.
- **Problem reports** are kept while the issue is open and for a reasonable period afterwards so
  that recurrences can be recognised. When we publish anything about an issue, we publish the
  technical facts only — **never your e-mail address or any identifying detail**.
- **Student-verification records** — your name, school e-mail address, school name, the checkout
  e-mail address if you gave one, and discount status — are kept while the student discount is
  active and deleted within 30 days after it ends, including the copies held by our form service.
  An application that is never completed is deleted within 30 days after its verification code
  expires or, if no code was sent, within 30 days after we reply to it. An application whose
  school domain we check by hand is kept until we decide, and if we cannot approve it, it is
  deleted within 30 days after we tell you so. If we end a student discount because it was used
  outside the student terms (for example, for commercial work), we keep the school e-mail address,
  the subscription the discount was applied to and the reason for 12 months after we end it, so
  that the same discount is not applied again, and then delete them. When we delete a form
  submission, our form service keeps it in its trash for up to 90 days before erasing it
  permanently.
- **E-mail correspondence** is kept in our mailbox for as long as we need it to deal with your
  request and any follow-up, and is deleted when you ask us to.

## 7. Your rights

You may ask us to confirm what we hold about you, to correct it, to delete it, or to stop
processing it, and you may withdraw a consent you have given. Write to
**founder@plugindevlab.com** and we will respond without undue delay. You also have the right to
lodge a complaint with the data protection authority in the country where you live.

You can exercise some of these rights directly and immediately: device activations can be
released by you in the customer portal, and the Google Sheets authorisation can be revoked by you
in your Google account.

## 8. Security

Access to each processor's dashboard is limited to accounts under our sole control. The Google
account that holds the student-verification records and sends our e-mails is protected by
two-factor authentication. Locally, the Google authorisation token is encrypted with
Windows DPAPI on Windows and is not written to disk at all on macOS. Because we operate no servers and hold no database of our own, there is no
separate store of customer data for us to lose.

## 9. Children

Our products are professional design tools and are not directed at children. We do not knowingly
collect personal data from children.

## 10. Data Protection Officer, and changes to this Policy

The person responsible for personal data protection can be reached at
**founder@plugindevlab.com** (Privacy Officer, plugin.dev.lab).

If we change this Policy we will publish the revised version at {{ page.url | absolute_url }} with a new version
number and effective date. Where a change materially affects what we process or who processes it,
we will say so on that page rather than change the text silently.
