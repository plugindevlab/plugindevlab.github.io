(function () {
  "use strict";

  var root = document.querySelector("[data-trainer]");
  var raw = document.getElementById("trainer-graph");
  if (!root || !raw) { return; }

  var G;
  try { G = JSON.parse(raw.textContent); } catch (e) { return; }
  if (!G || !G.components || !G.components.length || !G.map) { return; }

  var board = root.querySelector(".tr-board");
  var map = root.querySelector(".tr-map");
  var bar = root.querySelector(".tr-bar");
  var say = root.querySelector(".tr-say");
  if (!board || !map) { return; }

  var BY_ID = {}, BY_GROUP = {};
  G.components.forEach(function (c) {
    BY_ID[c.id] = c;
    (BY_GROUP[c.group] = BY_GROUP[c.group] || []).push(c);
  });
  var BOX = {};
  G.map.nodes.forEach(function (n) { BOX[n.group] = n; });
  var STAGE = {};
  G.stages.forEach(function (s) { STAGE[s.group] = s; });

  function wireable(c) {
    return c["in"].filter(function (p) {
      var t = G.types[p.t];
      return t && t.producers && t.producers.length;
    });
  }
  function makers(type) {
    var t = G.types[type];
    return ((t && t.producers) || []).map(function (id) {
      return BY_ID[id] ? BY_ID[id].name : id;
    });
  }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (ch) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch];
    });
  }

  var nodes = [];  var wires = [];  var seq = 0;
  var armed = null;
  var dragWire = null;
  var afterDrag = false;
  var moving = null;

  root.classList.add("tr-live");
  var fallback = root.querySelector(".tr-fallback");
  if (fallback) { fallback.remove(); }

  var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("class", "tr-wires");
  board.appendChild(svg);

  var ghost = document.createElementNS("http://www.w3.org/2000/svg", "path");
  ghost.setAttribute("class", "tr-ghost");
  svg.appendChild(ghost);

  var pop = document.createElement("div");
  pop.className = "tr-pop";
  pop.hidden = true;
  board.appendChild(pop);

  var panel = document.createElement("div");
  panel.className = "tr-panel";
  panel.hidden = true;
  root.appendChild(panel);

  var MAP_H = G.map.h;
  var GAP = 26;
  map.addEventListener("click", function (ev) {
    var a = ev.target.closest ? ev.target.closest("a[data-stage]") : null;
    if (!a) { return; }
    ev.preventDefault();
    openStage(a.getAttribute("data-stage"));
  });

  function openStage(group) {
    var box = BOX[group], list = BY_GROUP[group] || [];
    if (!box || !list.length) { return; }
    pop.innerHTML = '<div class="tr-pop-h"><b>' + esc(STAGE[group] ? STAGE[group].label : group)
      + "</b><span>" + list.length + " components</span>"
      + '<button type="button" class="tr-close" aria-label="Close">×</button></div>'
      + '<div class="tr-chips">' + list.map(function (c) {
        return '<a href="' + esc(root.getAttribute("data-comp-base") + c.id) + '/" data-comp="'
          + esc(c.id) + '"><b>' + esc(c.name) + "</b>"
          + (c.cid ? "<code>" + esc(c.cid) + "</code>" : "") + "</a>";
      }).join("") + "</div>"
      + '<p class="tr-pop-n">Click one to put it on the board. Its ports appear on the node.</p>';
    pop.style.left = Math.min(box.x, Math.max(0, G.map.w - 300)) + "px";
    pop.style.top = (box.y + box.h + 8) + "px";
    pop.hidden = false;
    tell(list.length + " components in " + (STAGE[group] ? STAGE[group].label : group) + ".");
  }
  pop.addEventListener("click", function (ev) {
    if (ev.target.closest(".tr-close")) { pop.hidden = true; return; }
    var a = ev.target.closest ? ev.target.closest("a[data-comp]") : null;
    if (!a) { return; }
    ev.preventDefault();
    place(a.getAttribute("data-comp"));
  });

  var NODE_W = 236, ROW_H = 34;

  function freeSpot(c) {
    var feeders = nodes.filter(function (n) {
      return BY_ID[n.id].out.some(function (o) {
        return c["in"].some(function (i) { return i.t === o.t; });
      });
    });
    var x, y;
    if (feeders.length) {
      var f = feeders[feeders.length - 1];
      x = f.x + NODE_W + 44;
      y = f.y;
    } else {
      var box = BOX[c.group];
      x = box ? box.x : 10;
      y = MAP_H + GAP;
    }
    var guard = 0;
    while (guard++ < 60 && nodes.some(function (n) {
      return Math.abs(n.x - x) < NODE_W - 20 && Math.abs(n.y - y) < n.h + 12;
    })) {
      y += 40;
    }
    return { x: x, y: Math.max(y, MAP_H + GAP) };
  }

  function place(id) {
    var c = BY_ID[id];
    if (!c) { return; }
    var spot = freeSpot(c);
    var rows = Math.max(c["in"].length, c.out.length);
    var n = {
      uid: "n" + (++seq), id: id, group: c.group,
      x: spot.x, y: spot.y, h: 44 + rows * ROW_H + 10,
      pins: { "in": [], out: [] }
    };
    nodes.push(n);
    drawNode(n);
    pop.hidden = true;
    tell(c.name + " is on the board. Wire it from the ports on its left.");
    redraw();
  }

  function pinRow(n, side, p, i) {
    var row = document.createElement("button");
    row.type = "button";
    row.className = "tr-pin tr-" + side;
    row.setAttribute("data-side", side);
    row.setAttribute("data-i", String(i));
    var t = G.types[p.t];
    if (side === "in" && !(t && t.producers.length)) { row.classList.add("tr-ext"); }
    row.innerHTML = "<i></i><b>" + esc(p.t) + "</b><em>" + esc(p.n) + "</em>";
    row.title = p.n + " — " + p.t + " · " + p.a + (p.opt ? " · optional" : "");
    n.pins[side][i] = row;
    return row;
  }

  function drawNode(n) {
    var c = BY_ID[n.id];
    var el = document.createElement("div");
    el.className = "tr-node";
    el.style.left = n.x + "px";
    el.style.top = n.y + "px";
    if (c.tier) { el.style.setProperty("--tier", "var(--tier-" + c.tier + ")"); }

    var head = document.createElement("div");
    head.className = "tr-head";
    head.innerHTML = "<b>" + esc(c.name) + "</b>" + (c.cid ? "<code>" + esc(c.cid) + "</code>" : "");
    var kill = document.createElement("button");
    kill.type = "button";
    kill.className = "tr-kill";
    kill.setAttribute("aria-label", "Remove " + c.name);
    kill.textContent = "×";
    head.appendChild(kill);
    el.appendChild(head);

    var body = document.createElement("div");
    body.className = "tr-ports";
    var lhs = document.createElement("div");
    var rhs = document.createElement("div");
    c["in"].forEach(function (p, i) { lhs.appendChild(pinRow(n, "in", p, i)); });
    c.out.forEach(function (p, i) { rhs.appendChild(pinRow(n, "out", p, i)); });
    body.appendChild(lhs);
    body.appendChild(rhs);
    el.appendChild(body);

    board.appendChild(el);
    n.el = el;
    n.h = el.offsetHeight || n.h;

    kill.addEventListener("click", function (ev) { ev.stopPropagation(); remove(n); });
    head.addEventListener("click", function (ev) {
      if (ev.target === kill) { return; }
      openPanel(n);
    });
    head.addEventListener("pointerdown", function (ev) { startMove(n, ev); });
    el.addEventListener("pointerdown", function (ev) {
      var pin = ev.target.closest ? ev.target.closest(".tr-pin") : null;
      if (pin) { startWire(n, pin, ev); }
    });
    el.addEventListener("click", function (ev) {
      var pin = ev.target.closest ? ev.target.closest(".tr-pin") : null;
      if (!pin) { return; }
      ev.preventDefault();
      if (afterDrag) { afterDrag = false; return; }
      tapPin(n, pin);
    });
  }

  function remove(n) {
    wires.filter(function (w) { return w.a.node === n || w.b.node === n; }).forEach(dropWire);
    nodes.splice(nodes.indexOf(n), 1);
    if (n.el) { n.el.remove(); }
    closePanel();
    disarm();
    redraw();
  }

  function reaches(a, b) {
    if (a === b) { return true; }
    var seen = {}, stack = [a];
    while (stack.length) {
      var cur = stack.pop();
      if (cur === b) { return true; }
      if (seen[cur.uid]) { continue; }
      seen[cur.uid] = 1;
      wires.forEach(function (w) { if (w.a.node === cur) { stack.push(w.b.node); } });
    }
    return false;
  }

  function wireInto(node, i) {
    for (var k = 0; k < wires.length; k++) {
      if (wires[k].b.node === node && wires[k].b.i === i) { return wires[k]; }
    }
    return null;
  }

  function refuse(outNode, oi, inNode, ii) {
    var op = BY_ID[outNode.id].out[oi];
    var ip = BY_ID[inNode.id]["in"][ii];
    if (op.t !== ip.t) {
      var mk = makers(ip.t);
      return ip.n + " takes " + ip.t + ". You offered " + op.t + " from "
        + BY_ID[outNode.id].name + "."
        + (mk.length ? " " + ip.t + " comes from " + mk.join(", ") + "." : "");
    }
    if (ip.a === "item" && wireInto(inNode, ii)) {
      return ip.n + " is an item input, so it takes one wire. Remove the one on it first.";
    }
    if (reaches(inNode, outNode)) {
      return "That would loop back into itself. Grasshopper does not allow a cycle.";
    }
    return null;
  }

  function connect(outNode, oi, inNode, ii) {
    var bad = refuse(outNode, oi, inNode, ii);
    if (bad) { tell(bad, true); return false; }
    var path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path.setAttribute("class", "tr-wire");
    svg.appendChild(path);
    var w = { uid: "w" + (++seq), a: { node: outNode, i: oi }, b: { node: inNode, i: ii }, path: path };
    wires.push(w);
    path.addEventListener("click", function () {
      dropWire(w);
      tell("Wire removed.");
      redraw();
    });
    tell(BY_ID[outNode.id].name + " → " + BY_ID[inNode.id].name + " ("
      + BY_ID[inNode.id]["in"][ii].t + ").");
    redraw();
    return true;
  }

  function dropWire(w) {
    if (w.path) { w.path.remove(); }
    var k = wires.indexOf(w);
    if (k >= 0) { wires.splice(k, 1); }
  }

  function disarm() {
    if (armed && armed.node.pins.out[armed.i]) {
      armed.node.pins.out[armed.i].classList.remove("tr-armed");
    }
    armed = null;
    ghost.removeAttribute("d");
  }

  function tapPin(n, pin) {
    var side = pin.getAttribute("data-side");
    var i = Number(pin.getAttribute("data-i"));
    if (side === "out") {
      if (armed && armed.node === n && armed.i === i) { disarm(); tell("Let go."); return; }
      disarm();
      armed = { node: n, i: i };
      pin.classList.add("tr-armed");
      tell("Holding " + BY_ID[n.id].out[i].t + " from " + BY_ID[n.id].name
        + ". Now click an input that takes it.");
      return;
    }
    if (armed) {
      if (connect(armed.node, armed.i, n, i)) { disarm(); }
      return;
    }
    var p = BY_ID[n.id]["in"][i];
    var has = wireInto(n, i);
    var mk = makers(p.t);
    if (!mk.length) {
      tell(p.n + " takes " + p.t + ", which comes from outside the plugin. "
        + (G.external[p.t] || "Leave it unwired here."));
    } else if (has) {
      tell(p.n + " already has " + BY_ID[has.a.node.id].name + " on it. Click the wire to remove it.");
    } else {
      tell(p.n + " takes " + p.t + ". " + p.t + " comes from " + mk.join(", ") + ".");
    }
  }

  function startWire(n, pin, ev) {
    if (pin.getAttribute("data-side") !== "out") { return; }
    ev.preventDefault();
    dragWire = { node: n, i: Number(pin.getAttribute("data-i")), moved: false };
  }

  function boardPoint(ev) {
    var r = board.getBoundingClientRect();
    return { x: ev.clientX - r.left + board.scrollLeft, y: ev.clientY - r.top + board.scrollTop };
  }

  board.addEventListener("pointermove", function (ev) {
    if (moving) { onMove(ev); return; }
    if (!dragWire) { return; }
    dragWire.moved = true;
    ghost.setAttribute("d", curve(pinPoint(dragWire.node, "out", dragWire.i), boardPoint(ev)));
  });

  board.addEventListener("pointerup", function (ev) {
    if (moving) { endMove(); return; }
    if (!dragWire) { return; }
    var d = dragWire;
    dragWire = null;
    ghost.removeAttribute("d");
    if (!d.moved) { return; }
    afterDrag = true;
    var el = document.elementFromPoint(ev.clientX, ev.clientY);
    var pin = el && el.closest ? el.closest(".tr-pin") : null;
    if (!pin || pin.getAttribute("data-side") !== "in") { tell("Drop it on an input port."); return; }
    var host = null;
    nodes.forEach(function (n) { if (n.el && n.el.contains(pin)) { host = n; } });
    if (host) { connect(d.node, d.i, host, Number(pin.getAttribute("data-i"))); }
  });

  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape") { disarm(); closePanel(); pop.hidden = true; }
  });

  function startMove(n, ev) {
    if (ev.target.closest && ev.target.closest(".tr-kill")) { return; }
    var p = boardPoint(ev);
    moving = { node: n, dx: p.x - n.x, dy: p.y - n.y };
    n.el.classList.add("tr-moving");
  }
  function onMove(ev) {
    var p = boardPoint(ev), n = moving.node;
    n.x = Math.max(0, p.x - moving.dx);
    n.y = Math.max(0, p.y - moving.dy);
    n.el.style.left = n.x + "px";
    n.el.style.top = n.y + "px";
    redrawWires();
  }
  function endMove() {
    if (moving) { moving.node.el.classList.remove("tr-moving"); }
    moving = null;
    grow();
  }

  function pinPoint(n, side, i) {
    var pin = n.pins[side][i];
    if (!pin) { return { x: n.x, y: n.y }; }
    var pr = pin.getBoundingClientRect(), br = board.getBoundingClientRect();
    return {
      x: (side === "out" ? pr.right : pr.left) - br.left + board.scrollLeft,
      y: pr.top + pr.height / 2 - br.top + board.scrollTop
    };
  }

  function curve(a, b) {
    var dx = Math.max(30, Math.abs(b.x - a.x) * 0.45);
    return "M" + a.x + " " + a.y + " C" + (a.x + dx) + " " + a.y
      + " " + (b.x - dx) + " " + b.y + " " + b.x + " " + b.y;
  }

  function redrawWires() {
    wires.forEach(function (w) {
      w.path.setAttribute("d", curve(pinPoint(w.a.node, "out", w.a.i),
        pinPoint(w.b.node, "in", w.b.i)));
    });
  }

  function grow() {
    var w = G.map.w, h = MAP_H + GAP;
    nodes.forEach(function (n) {
      w = Math.max(w, n.x + NODE_W + 10);
      h = Math.max(h, n.y + (n.el ? n.el.offsetHeight : n.h) + 20);
    });
    board.style.minHeight = h + "px";
    svg.style.width = w + "px";
    svg.style.height = h + "px";
  }

  function reachedSet() {
    var got = {};
    nodes.forEach(function (n) { if (!wireable(BY_ID[n.id]).length) { got[n.uid] = 1; } });
    var changed = true;
    while (changed) {
      changed = false;
      nodes.forEach(function (n) {
        if (got[n.uid]) { return; }
        for (var k = 0; k < wires.length; k++) {
          if (wires[k].b.node === n && got[wires[k].a.node.uid]) {
            got[n.uid] = 1; changed = true; return;
          }
        }
      });
    }
    return got;
  }

  function redraw() {
    grow();
    redrawWires();
    root.classList.toggle("tr-building", nodes.length > 0);
    var got = reachedSet();
    nodes.forEach(function (n) { n.el.classList.toggle("tr-floating", !got[n.uid]); });

    var spine = G.stages.filter(function (s) { return !s.aside; });
    var done = 0, html = "";
    spine.forEach(function (s, i) {
      var here = nodes.filter(function (n) { return n.group === s.group && got[n.uid]; });
      if (here.length) { done++; }
      html += '<div class="' + (here.length ? "here" : "") + '" style="--st:var(--s'
        + (i + 1) + ')">' + (i + 1) + "<b>" + esc(s.label) + "</b></div>";
    });
    var floating = nodes.length - Object.keys(got).length;
    var parts = [];
    if (!nodes.length) {
      parts.push("Open a stage on the map and put something down.");
    } else {
      parts.push("Reached " + done + " of " + spine.length + " stages.");
      if (floating > 0) {
        parts.push(floating === 1
          ? "One component is floating — nothing upstream reaches it."
          : floating + " components are floating — nothing upstream reaches them.");
      }
    }
    if (done === spine.length && spine.length) { parts.push("That is the bowl workflow, end to end."); }
    if (bar) {
      bar.innerHTML = '<div class="stages">' + html + '</div><p class="tr-score">'
        + esc(parts.join(" ")) + "</p>";
    }
  }

  function openPanel(n) {
    var c = BY_ID[n.id];
    var rows = function (list, label) {
      if (!list.length) { return ""; }
      return "<h4>" + label + "</h4><ul>" + list.map(function (p) {
        return "<li><b>" + esc(p.n) + "</b><code>" + esc(p.t) + "</code><em>"
          + esc(p.a) + (p.opt ? " · optional" : "") + "</em></li>";
      }).join("") + "</ul>";
    };
    panel.innerHTML = '<button type="button" class="tr-close" aria-label="Close">×</button>'
      + "<h3>" + esc(c.name) + (c.cid ? "<code>" + esc(c.cid) + "</code>" : "") + "</h3>"
      + (c.summary ? "<p>" + esc(c.summary) + "</p>" : "")
      + rows(c["in"], "Chain inputs") + rows(c.out, "Chain outputs")
      + '<a class="tr-more" href="' + esc(root.getAttribute("data-comp-base") + c.id)
      + '/">Full description</a>';
    panel.hidden = false;
    panel.querySelector(".tr-close").addEventListener("click", closePanel);
  }
  function closePanel() { panel.hidden = true; }

  function tell(msg, bad) {
    if (!say) { return; }
    say.textContent = msg;
    say.classList.toggle("bad", !!bad);
  }

  var reset = document.querySelector("[data-trainer-reset]");
  if (reset) {
    reset.hidden = false;
    reset.addEventListener("click", function () {
      wires.slice().forEach(dropWire);
      nodes.slice().forEach(function (n) { if (n.el) { n.el.remove(); } });
      nodes = [];
      disarm();
      closePanel();
      pop.hidden = true;
      redraw();
      tell("Board cleared. The map is back to just the stages.");
    });
  }

  window.addEventListener("resize", function () { grow(); redrawWires(); });

  redraw();
  tell("Click a stage on the map to see what is in it.");
}());
