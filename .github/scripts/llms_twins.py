"""Write llms.txt and a Markdown twin of every page into a built Jekyll site.

Runs after `jekyll build` (see .github/workflows/pages.yml). Standard library only.

  python3 .github/scripts/llms_twins.py _site --repo .        # address from _config.yml url (or --url)
  python3 .github/scripts/llms_twins.py --selftest

- Twin of /a/b/ is /a/b/index.html.md and of /a/b.html is /a/b.html.md (the llms.txt proposal).
- Each twin is the page's <main> as Markdown, headed by its canonical URL and the date its source last changed
  (git, when --repo is given). Navigation, the ribbon diagram and other decoration are left out.
- Component pages carry their full port tables from _data/components.json instead of the port lists.
- llms.txt lists every twin: the product pages first, then its components, then the rest under "Optional".
- The build fails if a twin would be empty or contains Hangul (the public site is English only).
"""
import html
import json
import os
import re
import subprocess
import sys
from html.parser import HTMLParser
from urllib.parse import urljoin

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
SKIP_TAGS = {"script", "style", "svg", "noscript", "template", "nav", "button", "form", "input", "select", "textarea",
             "picture", "img", "video", "audio", "iframe", "canvas", "map", "head"}
SKIP_CLASSES = {"side", "stages", "plate", "skip", "crumb", "rel-nav", "zoom", "a-menu", "nick"}
BLOCK = {"p", "div", "section", "article", "aside", "header", "footer", "main", "ul", "ol", "li", "dl", "dt", "dd",
         "h1", "h2", "h3", "h4", "h5", "h6", "pre", "blockquote", "table", "figure", "figcaption", "details", "summary", "hr"}
HANGUL = re.compile("[%s-%s%s-%s%s-%s]" % tuple(map(chr, (0xAC00, 0xD7A3, 0x1100, 0x11FF, 0x3130, 0x318F))))   # syllables, jamo, compatibility jamo
OPTIONAL_PAGES = ("/eula/", "/privacy/")

class Node:
    __slots__ = ("tag", "attrs", "kids", "parent")

    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.kids, self.parent = tag, dict(attrs), [], parent

    def cls(self):
        return set((self.attrs.get("class") or "").split())

class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", {}, None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.kids.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.kids.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.kids.append(data)

def parse(text):
    t = Tree()
    t.feed(text)
    t.close()
    return t.root

def find(node, pred):
    if isinstance(node, Node):
        if pred(node):
            return node
        for k in node.kids:
            r = find(k, pred)
            if r is not None:
                return r
    return None

def find_all(node, pred, out=None):
    out = [] if out is None else out
    if isinstance(node, Node):
        if pred(node):
            out.append(node)
        for k in node.kids:
            find_all(k, pred, out)
    return out

def text_of(node):
    if isinstance(node, str):
        return node
    if skipped(node):
        return ""
    return "".join(text_of(k) for k in node.kids)

def skipped(n):
    return (n.tag in SKIP_TAGS or n.attrs.get("aria-hidden") == "true" or "hidden" in n.attrs
            or bool(n.cls() & SKIP_CLASSES))

def squash(s):
    return re.sub(r"\s+", " ", s).strip()

class Md:
    """Renders a node tree to Markdown. `base` makes links absolute; `ports` replaces a page's port lists."""

    def __init__(self, base, page_url, ports=None):
        self.base, self.page_url, self.ports, self.port_lists = base.rstrip("/"), page_url, ports, 0

    def href(self, h):
        if not h or h.startswith(("mailto:", "tel:", "javascript:")):
            return h
        return urljoin(self.base + self.page_url, h)

    def inline(self, n):
        if isinstance(n, str):
            return re.sub(r"\s+", " ", n)
        if skipped(n):
            return ""
        t = n.tag
        inner = "".join(self.inline(k) for k in n.kids)
        if t == "br":
            return "  \n"
        if t == "a":
            label = squash(inner)
            h = self.href(n.attrs.get("href", ""))
            return f"[{label}]({h})" if label and h else label
        if t in ("strong", "b"):
            s = squash(inner)
            return f"**{s}**" if s else ""
        if t in ("em", "i"):
            s = squash(inner)
            return f"*{s}*" if s else ""
        if t == "code":
            s = squash(text_of(n))
            return f"`{s}`" if s else ""
        if t in BLOCK:
            return " " + inner + " "
        return inner

    def para(self, nodes):
        return squash("".join(self.inline(k) for k in nodes)).replace(" \n", "\n")

    def blocks(self, n, depth=0):
        """List of Markdown blocks for a node's children."""
        out, run = [], []

        def flush():
            s = self.para(run)
            if s:
                out.append(s)
            run.clear()
        for k in n.kids:
            if isinstance(k, str) or (k.tag not in BLOCK and not skipped(k)):
                run.append(k)
                continue
            flush()
            if skipped(k):
                continue
            out.extend(self.block(k, depth))
        flush()
        return out

    def block(self, n, depth):
        t = n.tag
        if t in ("h1", "h2", "h3", "h4", "h5", "h6"):
            s = self.para(n.kids)
            return [("#" * int(t[1])) + " " + s] if s else []
        if t == "p" and "tags" in n.cls():
            tags = [squash(text_of(k)) for k in n.kids if isinstance(k, Node)]
            return [" · ".join(x for x in tags if x)] if tags else []
        if t == "p" or t == "figcaption" or t == "dt" or t == "dd":
            s = self.para(n.kids)
            return [s] if s else []
        if t == "div" and "chain" in n.cls():
            return self.chain(n)
        if t in ("ul", "ol"):
            if self.ports is not None and "ports" in n.cls():
                return self.port_table(n)
            return [self.listing(n, depth)]
        if t == "pre":
            return ["```\n" + text_of(n).strip("\n") + "\n```"]
        if t == "blockquote":
            return ["\n".join("> " + ln if ln else ">" for ln in "\n\n".join(self.blocks(n, depth)).splitlines())]
        if t == "table":
            return [self.table(n)]
        if t == "hr":
            return ["---"]
        if t == "dl":
            rows = []
            for d in find_all(n, lambda x: x.tag == "dt"):
                dd = d.parent.kids[d.parent.kids.index(d) + 1:] if d.parent else []
                val = next((self.para(x.kids) for x in dd if isinstance(x, Node) and x.tag == "dd"), "")
                rows.append(f"- **{self.para(d.kids)}**: {val}")
            return ["\n".join(rows)] if rows else []
        if t == "details":
            summ = next((k for k in n.kids if isinstance(k, Node) and k.tag == "summary"), None)
            head = self.para(summ.kids) if summ else ""
            rest = Node("div", {}, None)
            rest.kids = [k for k in n.kids if k is not summ]
            return ([f"### {head}"] if head else []) + self.blocks(rest, depth)
        if t == "summary":
            s = self.para(n.kids)
            return [f"**{s}**"] if s else []
        return self.blocks(n, depth)

    def chain(self, n):
        """Component page 'In the chain' box: a heading, then 'Label: link (ID), ...' per direction."""
        out, label, links = [], None, []

        def flush():
            if label is not None:
                out.append(f"{label}: " + (", ".join(links) if links else "-"))
        for k in n.kids:
            if not isinstance(k, Node) or skipped(k):
                continue
            if k.tag in ("h2", "h3", "h4"):
                out.append("#" * int(k.tag[1]) + " " + self.para(k.kids))
            elif k.tag == "p":
                flush()
                label, links = self.para(k.kids), []
            elif k.tag == "a":
                ids = [squash(text_of(x)) for x in k.kids if isinstance(x, Node) and x.tag == "em"]
                name = squash("".join(x for x in k.kids if isinstance(x, str)))
                links.append(f"[{name}]({self.href(k.attrs.get('href', ''))})" + (f" ({ids[0]})" if ids else ""))
        flush()
        return out

    def listing(self, n, depth):
        lines, i = [], 0
        for li in n.kids:
            if not isinstance(li, Node) or li.tag != "li" or skipped(li):
                continue
            i += 1
            mark = f"{i}." if n.tag == "ol" else "-"
            parts = self.blocks(li, depth + 1)
            if not parts:
                continue
            pad = "  " * (depth + 1)
            body = parts[0] + "".join("\n\n" + "\n".join(pad + ln if ln else "" for ln in p.splitlines()) for p in parts[1:])
            lines.append("  " * depth + f"{mark} " + body.replace("\n", "\n" + "  " * depth + "  ").replace("\n" + "  " * depth + "  " + "\n", "\n\n"))
        return "\n".join(lines)

    def table(self, n):
        rows = []
        for tr in find_all(n, lambda x: x.tag == "tr"):
            cells = [squash(self.para(c.kids)).replace("|", "\\|") for c in tr.kids if isinstance(c, Node) and c.tag in ("th", "td")]
            if cells:
                rows.append(cells)
        if not rows:
            return ""
        w = max(len(r) for r in rows)
        rows = [r + [""] * (w - len(r)) for r in rows]
        out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * w]
        out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
        return "\n".join(out)

    def port_table(self, n):
        """Replaces a port list with the full table from components.json. Which side = the heading just above it
        (a component with no inputs has only the Outputs list)."""
        head_above = ""
        if n.parent is not None:
            for k in reversed(n.parent.kids[: n.parent.kids.index(n)]):
                if isinstance(k, Node) and k.tag in ("h2", "h3"):
                    head_above = squash(text_of(k)).lower()
                    break
        side = "outputs" if "output" in head_above else "inputs" if "input" in head_above else \
            ("inputs" if self.port_lists == 0 else "outputs")
        self.port_lists += 1
        ports = self.ports.get(side) or []
        if not ports:
            return ["None."]
        esc = lambda s: squash(str(s)).replace("|", "\\|")
        nick = lambda p: p.get("nick") or p.get("name")          # the page shows the name when the nickname is the same
        if side == "inputs":
            head = ["Name", "Nickname", "Type", "Access", "Default", "Description"]
            body = [[p.get("name"), nick(p), p.get("ghType"), p.get("access"),
                     p.get("default") if p.get("default") not in (None, "") else "-", p.get("desc")] for p in ports]
        else:
            head = ["Name", "Nickname", "Type", "Access", "Description"]
            body = [[p.get("name"), nick(p), p.get("ghType"), p.get("access"), p.get("desc")] for p in ports]
        out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
        out += ["| " + " | ".join(esc(c if c is not None else "") for c in r) + " |" for r in body]
        return ["\n".join(out)]

def page_url(rel):
    """Built file path (posix) -> page URL."""
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel

def twin_rel(rel):
    return rel + ".md"

def meta(root, name):
    m = find(root, lambda n: n.tag == "meta" and (n.attrs.get("name") == name or n.attrs.get("property") == name))
    return squash(m.attrs.get("content", "")) if m else ""

def page_title(root):
    """<title> without the trailing ' · <site name>'."""
    t = squash(text_of(find(root, lambda n: n.tag == "title") or Node("x", {}, None)))
    site = meta(root, "og:site_name")
    return t[: -len(" · " + site)] if site and t.endswith(" · " + site) else t

def source_of(repo, rel):
    """Source file a built page came from (for its last-changed date)."""
    stem = rel[: -len(".html")]
    for cand in (stem + ".md", stem + ".html", stem + ".markdown"):
        if os.path.isfile(os.path.join(repo, cand)):
            return cand
    return None

def git_date(repo, path):
    try:
        r = subprocess.run(["git", "-C", repo, "log", "-1", "--format=%cs", "--", path], capture_output=True, text=True, timeout=30)
        return r.stdout.strip() or None
    except Exception:
        return None

def components(data_dir, product):
    f = os.path.join(data_dir, "components.json")
    if not os.path.isfile(f):
        return {}
    d = json.load(open(f, encoding="utf-8"))["products"].get(product, {}).get("components", [])
    return {c["id"]: c for c in d}

def convert(text, base, url, ports=None):
    root = parse(text)
    main = find(root, lambda n: n.tag == "main")
    if main is None:
        return None, root
    md = Md(base, url, ports)
    return "\n\n".join(b for b in md.blocks(main) if b.strip()), root

def run(site, base, repo, data):
    pages = []
    for d, _dirs, files in os.walk(site):
        for f in files:
            if f.endswith(".html"):
                rel = os.path.relpath(os.path.join(d, f), site).replace(os.sep, "/")
                if rel != "404.html":
                    pages.append(rel)
    pages.sort()
    comps_by_product = {}
    entries, bad = [], []
    for rel in pages:
        url = page_url(rel)
        m = re.match(r"^/([^/]+)/components/([^/]+)/$", url)
        ports = None
        if m:
            comps = comps_by_product.setdefault(m.group(1), components(data, m.group(1)))
            c = comps.get(m.group(2))
            if c:
                ports = {"inputs": c.get("inputs"), "outputs": c.get("outputs")}
        text = open(os.path.join(site, rel), encoding="utf-8").read()
        body, root = convert(text, base, url, ports)
        if not body:
            bad.append(f"{rel}: empty twin (no <main> content)")
            continue
        when = git_date(repo, source_of(repo, rel)) if repo and source_of(repo, rel) else None
        if repo and ports is not None:            # a component page is drawn from components.json as much as from its own file
            when = max(filter(None, [when, git_date(repo, "_data/components.json")]), default=None)
        head = [f"Source: {base}{url}"] + ([f"Updated: {when}"] if when else [])
        lines = body.split("\n", 1)
        if lines[0].startswith("# "):
            body = lines[0] + "\n\n" + "  \n".join(head) + ("\n\n" + lines[1].lstrip("\n") if len(lines) > 1 else "")
        else:
            body = "  \n".join(head) + "\n\n" + body
        if HANGUL.search(body):
            bad.append(f"{rel}: Hangul in the twin")
            continue
        with open(os.path.join(site, twin_rel(rel)), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(body.rstrip() + "\n")
        entries.append({"url": url, "twin": base + "/" + twin_rel(rel), "title": page_title(root), "desc": meta(root, "description"),
                        "product": url.split("/")[1] if url.count("/") > 1 else "", "component": bool(m)})
    return entries, bad

def config_value(data, key):
    """A top-level value from _config.yml next to _data (url, description)."""
    f = os.path.join(os.path.dirname(os.path.abspath(data)), "_config.yml")
    if not os.path.isfile(f):
        return ""
    m = re.search(r"^" + key + r":\s*(.+?)\s*$", open(f, encoding="utf-8").read(), re.M)
    return m.group(1).strip("\"'") if m else ""

def llms_txt(entries, site_title, site_desc, products, comp_order, default_desc=""):
    by_url = {e["url"]: e for e in entries}
    out = [f"# {site_title}", "", f"> {site_desc}", ""]
    out.append("Each link below is a Markdown copy of a page on this site. Drop the trailing index.html.md "
               "(or .md) from a link to reach the page itself.")
    used = {e["url"] for e in entries if any(k in e["url"] for k in OPTIONAL_PAGES)}   # legal pages go under Optional

    def item(e):
        used.add(e["url"])
        desc = e["desc"] if e["desc"] and e["desc"] not in (site_desc, default_desc) else ""   # a page with no description of its own inherits the site's
        return f"- [{e['title']}]({e['twin']})" + (f": {desc}" if desc else "")
    for p in products:
        slug, name = p["slug"], p["name"]
        home = by_url.get(f"/{slug}/")
        nav = [by_url[u] for u in p.get("nav", []) if u in by_url]
        skip = {f"/{slug}/", *p.get("nav", [])}
        rest = sorted((e for e in entries if e["product"] == slug and not e["component"] and e["url"] not in skip),
                      key=lambda e: e["url"])
        out += ["", f"## {name}", ""]
        out += [item(e) for e in [home] + nav + rest if e and e["url"] not in used]
        comps = [e for e in entries if e["product"] == slug and e["component"]]
        rank = {cid: i for i, cid in enumerate(comp_order.get(slug, []))}
        comps.sort(key=lambda e: (rank.get(e["url"].rstrip("/").split("/")[-1], len(rank)), e["url"]))
        if comps:
            out += ["", f"## {name} components", ""]
            out += [item(e) for e in comps if e["url"] not in used]
    others = [e for e in entries if e["url"] not in used or any(k in e["url"] for k in OPTIONAL_PAGES)]
    if others:
        out += ["", "## Optional", ""]
        out += [item(e) for e in sorted(others, key=lambda e: e["url"])]
    return "\n".join(out).rstrip() + "\n"

def site_info(site, data):
    """Title and description from the home page, products and their nav from the header of each product home."""
    home = parse(open(os.path.join(site, "index.html"), encoding="utf-8").read())
    title = meta(home, "og:site_name") or page_title(home) or "Site"
    desc = meta(home, "description")
    products, order = [], {}
    pj = os.path.join(data, "components.json")
    if os.path.isfile(pj):
        for slug, p in json.load(open(pj, encoding="utf-8"))["products"].items():
            order[slug] = [c["id"] for c in p.get("components", [])]
    for slug in sorted(order) or []:
        f = os.path.join(site, slug, "index.html")
        if not os.path.isfile(f):
            continue
        root = parse(open(f, encoding="utf-8").read())
        nav = find(root, lambda n: n.tag == "nav" and "a-nav" in n.cls())
        links = [a.attrs.get("href", "") for a in find_all(nav, lambda n: n.tag == "a")] if nav else []
        name = squash(text_of(find(root, lambda n: n.tag == "a" and "a-prod" in n.cls()) or Node("x", {}, None))) or slug
        products.append({"slug": slug, "name": name, "nav": [h for h in links if h.startswith(f"/{slug}/")]})
    return title, desc, products, order

def main(argv):
    if "--selftest" in argv:
        return selftest()
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    site = args[0]
    opt = lambda k, d=None: argv[argv.index(k) + 1] if k in argv else d
    repo = opt("--repo")
    data = opt("--data", os.path.join(repo or ".", "_data"))
    base = (opt("--url") or config_value(data, "url")).rstrip("/")
    if not base:
        print("FAIL: no site address - give --url or set url in _config.yml")
        return 2
    entries, bad = run(site, base, repo, data)
    if not entries:
        bad.append("no pages found - nothing to list")
    title, desc, products, order = site_info(site, data)
    txt = llms_txt(entries, title, desc, products, order, config_value(data, "description"))
    if HANGUL.search(txt):
        bad.append("llms.txt: Hangul")
    for b in bad:
        print("FAIL:", b)
    if bad:
        return 1
    with open(os.path.join(site, "llms.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(txt)
    print(f"llms.txt + {len(entries)} twins ({sum(e['component'] for e in entries)} component pages)")
    return 0

def selftest():
    page = """<html><head><title>T</title><meta name="description" content="D"></head><body>
<nav class="a-nav"><a href="/x/">X</a></nav><main><aside class="side"><p>skip me</p></aside>
<h1>Seat<span class="nick">SEAT-001</span></h1><p class="lede">Fills <b>rows</b> with <a href="../y/">seats</a>.</p>
<p class="tags"><span class="tag">core</span><span class="tag">Bowl ▸ Section 3</span></p>
<div class="chain"><h3>In the chain</h3><p class="dir">Comes after</p><a href="/antlion/components/vomitory/">Vomitory<em>VOMITORY-001</em></a><a href="/antlion/components/axis/">Axis<em>AXIS-002</em></a>
<p class="dir">Goes into</p></div>
<div class="plate"><p>diagram</p></div><h2>Inputs</h2><ul class="ports"><li>old list</li></ul>
<h2>Outputs</h2><ul class="ports"><li>old list</li></ul>
<details><summary>1.0.2 Fix</summary><ul><li>One</li><li>Two <code>a|b</code></li></ul></details>
<p><span aria-hidden="true">+</span>added: X</p><table><tr><th>A</th><th>B</th></tr><tr><td>1|2</td><td>3</td></tr></table>
<dl class="title-block"><div><dt>Version</dt><dd>1.1.0</dd></div></dl></main></body></html>"""
    ports = {"inputs": [{"name": "Seat Width", "nick": "Seat W", "ghType": "Number", "access": "item", "optional": False,
                         "default": "500 mm", "desc": "Width | of one seat"}], "outputs": []}
    md, _ = convert(page, "https://e.com", "/antlion/components/seat/", ports)
    cases = [
        ("side panel and diagram left out", "skip me" not in md and "diagram" not in md),
        ("heading kept, component ID left to the title block", md.startswith("# Seat\n")),
        ("relative link made absolute", "[seats](https://e.com/antlion/components/y/)" in md),
        ("bold kept", "**rows**" in md),
        ("input port list replaced by the table", "| Seat Width | Seat W | Number | item | 500 mm | Width \\| of one seat |" in md
         and "old list" not in md),
        ("chain box as one line per direction", "Comes after: [Vomitory](https://e.com/antlion/components/vomitory/) (VOMITORY-001), "
         "[Axis](https://e.com/antlion/components/axis/) (AXIS-002)" in md and "Goes into: -" in md),
        ("tags joined", "core · Bowl ▸ Section 3" in md),
        ("empty outputs say None", "## Outputs\n\nNone." in md),
        ("outputs-only page: its one list is the outputs", "| R1 | R1 | Boolean | item | Row 1 |" in convert(
            "<main><h2>Outputs</h2><ul class='ports'><li>x</li></ul></main>", "https://e.com", "/p/",
            {"inputs": [], "outputs": [{"name": "R1", "nick": "R1", "ghType": "Boolean", "access": "item", "desc": "Row 1"}]})[0]),
        ("details summary becomes a heading", "### 1.0.2 Fix" in md and "- One" in md),
        ("aria-hidden glyph dropped, words kept", "added: X" in md and "+added" not in md),
        ("table pipes escaped", "| 1\\|2 | 3 |" in md),
        ("definition list as bullets", "- **Version**: 1.1.0" in md),
        ("Hangul detector", bool(HANGUL.search(chr(0xAC00))) and not HANGUL.search("Seat")),
    ]
    bad = 0
    for name, ok in cases:
        bad += 0 if ok else 1
        print(("PASS" if ok else "FAIL"), name)
    if bad:
        print(md)
    print(f"\nselftest {len(cases) - bad}/{len(cases)}")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
