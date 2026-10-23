/* Architecture-diagram renderer (plain JS, no libraries).
 *
 * A case-study page only supplies data:
 *   renderDiagram(document.getElementById('frame'), { eyebrow, title, columns, edges, note });
 * See diagram.css for the look. Everything is built inside #frame; connectors are drawn
 * after layout and again once the webfont has settled, then body[data-ready] is set to "1".
 */
(function () {
  'use strict';

  var SVG_NS = 'http://www.w3.org/2000/svg';
  var STROKE = '#5B6CFF';
  var STROKE_DASHED = '#6B7490';

  // Icon path bodies from the Lucide set (ISC licence): 24x24 viewBox, stroke only.
  var ICONS = {
    bot: '<path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>',
    globe: '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    server: '<rect width="20" height="8" x="2" y="2" rx="2" ry="2"/><rect width="20" height="8" x="2" y="14" rx="2" ry="2"/><line x1="6" x2="6.01" y1="6" y2="6"/><line x1="6" x2="6.01" y1="18" y2="18"/>',
    database: '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/>',
    cpu: '<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/>',
    monitor: '<rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/>',
    smartphone: '<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>',
    plug: '<path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 8V2"/><path d="M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8Z"/>',
    workflow: '<rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/>',
    lock: '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    image: '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>',
    film: '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 3v18"/><path d="M3 7.5h4"/><path d="M3 12h18"/><path d="M3 16.5h4"/><path d="M17 3v18"/><path d="M17 7.5h4"/><path d="M17 16.5h4"/>',
    box: '<path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    gamepad: '<line x1="6" x2="10" y1="11" y2="11"/><line x1="8" x2="8" y1="9" y2="13"/><line x1="15" x2="15.01" y1="12" y2="12"/><line x1="18" x2="18.01" y1="10" y2="10"/><path d="M17.32 5H6.68a4 4 0 0 0-3.978 3.59c-.006.052-.01.101-.017.152C2.604 9.416 2 14.456 2 16a3 3 0 0 0 3 3c1 0 1.5-.5 2-1l1.414-1.414A2 2 0 0 1 9.828 16h4.344a2 2 0 0 1 1.414.586L17 18c.5.5 1 1 2 1a3 3 0 0 0 3-3c0-1.545-.604-6.584-.685-7.258-.007-.05-.011-.1-.017-.151A4 4 0 0 0 17.32 5z"/>',
    languages: '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>',
    shield: '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
    chart: '<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
    zap: '<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>'
  };

  function div(className, text) {
    var el = document.createElement('div');
    el.className = className;
    if (text !== undefined && text !== null) el.textContent = text;
    return el;
  }

  function svgNode(tag, attrs) {
    var el = document.createElementNS(SVG_NS, tag);
    for (var key in attrs) {
      if (Object.prototype.hasOwnProperty.call(attrs, key)) el.setAttribute(key, attrs[key]);
    }
    return el;
  }

  function icon(name) {
    if (!Object.prototype.hasOwnProperty.call(ICONS, name)) {
      console.warn('renderDiagram: unknown icon "' + name + '"');
      return null;
    }
    var el = svgNode('svg', {
      'class': 'dg-icon',
      viewBox: '0 0 24 24',
      fill: 'none',
      stroke: 'currentColor',
      'stroke-width': '2',
      'stroke-linecap': 'round',
      'stroke-linejoin': 'round',
      'aria-hidden': 'true'
    });
    el.innerHTML = ICONS[name];
    return el;
  }

  function round(v) {
    return Math.round(v * 10) / 10;
  }

  function buildNode(node) {
    var card = div('dg-node' + (node.accent ? ' accent' : ''));

    var head = div('dg-node-head');
    if (node.icon) {
      var glyph = icon(node.icon);
      if (glyph) head.appendChild(glyph);
    }
    head.appendChild(div('dg-node-title', node.title === undefined || node.title === null ? '' : node.title));
    card.appendChild(head);

    if (node.text) card.appendChild(div('dg-node-text', node.text));

    if (node.chips && node.chips.length) {
      var chips = div('dg-chips');
      node.chips.forEach(function (chip) {
        chips.appendChild(div('dg-chip', chip));
      });
      card.appendChild(chips);
    }

    return card;
  }

  function boxOf(el, frameRect) {
    var r = el.getBoundingClientRect();
    return {
      left: r.left - frameRect.left,
      top: r.top - frameRect.top,
      right: r.right - frameRect.left,
      bottom: r.bottom - frameRect.top,
      cx: (r.left + r.right) / 2 - frameRect.left,
      cy: (r.top + r.bottom) / 2 - frameRect.top
    };
  }

  function renderDiagram(frameEl, data) {
    data = data || {};
    frameEl.textContent = '';

    var hasHeader = !!(data.eyebrow || data.title);
    if (hasHeader) {
      var header = div('dg-header');
      if (data.eyebrow) header.appendChild(div('dg-eyebrow', data.eyebrow));
      if (data.title) header.appendChild(div('dg-title', data.title));
      frameEl.appendChild(header);
    }

    var columnsEl = div('dg-columns');
    if (!hasHeader) columnsEl.classList.add('dg-no-header');
    if (!data.note) columnsEl.classList.add('dg-no-note');

    var nodes = {}; // node id -> { el, column }
    (data.columns || []).forEach(function (col, colIndex) {
      var colEl = div('dg-column' + (col.label ? ' dg-grouped' : ''));
      // Grow from a zero basis so the widths follow the given ratios, not each column's text length.
      colEl.style.flex = (typeof col.width === 'number' ? col.width : 1) + ' 1 0';
      if (col.label) colEl.appendChild(div('dg-column-label', col.label));

      (col.nodes || []).forEach(function (node) {
        var card = buildNode(node);
        colEl.appendChild(card);
        if (node.id) {
          if (nodes[node.id]) console.warn('renderDiagram: duplicate node id "' + node.id + '"');
          nodes[node.id] = { el: card, column: colIndex };
        }
      });

      columnsEl.appendChild(colEl);
    });
    frameEl.appendChild(columnsEl);

    // One SVG for every connector: above the group boxes, below the cards.
    var svg = svgNode('svg', { 'class': 'dg-edges' });
    var defs = svgNode('defs', {});
    svg.appendChild(defs);
    frameEl.appendChild(svg);

    if (data.note) frameEl.appendChild(div('dg-note', data.note));

    var markers = {};
    function markerId(color) {
      if (!markers[color]) {
        var id = 'dg-arrow-' + color.replace(/[^a-zA-Z0-9]/g, '');
        var marker = svgNode('marker', {
          'id': id,
          viewBox: '0 0 8 8',
          refX: '8',
          refY: '4',
          'markerWidth': '8',
          'markerHeight': '8',
          'markerUnits': 'userSpaceOnUse',
          'orient': 'auto-start-reverse'
        });
        marker.appendChild(svgNode('path', { d: 'M0 0 L8 4 L0 8 Z', fill: color }));
        defs.appendChild(marker);
        markers[color] = id;
      }
      return markers[color];
    }

    var labelEls = [];

    function drawEdges() {
      var frameRect = frameEl.getBoundingClientRect();

      while (svg.childNodes.length > 1) svg.removeChild(svg.lastChild);
      labelEls.forEach(function (el) {
        if (el.parentNode) el.parentNode.removeChild(el);
      });
      labelEls.length = 0;

      (data.edges || []).forEach(function (edge) {
        var from = nodes[edge.from];
        var to = nodes[edge.to];
        if (!from || !to) {
          console.warn('renderDiagram: edge "' + edge.from + '" -> "' + edge.to + '" references an unknown node id');
          return;
        }

        var a = boxOf(from.el, frameRect);
        var b = boxOf(to.el, frameRect);
        var x1, y1, x2, y2, dx, d, mx, my;

        if (from.column < to.column) {
          // Target column to the right: right-middle -> left-middle.
          x1 = a.right; y1 = a.cy;
          x2 = b.left; y2 = b.cy;
          dx = Math.max(30, (x2 - x1) / 2);
          d = 'M ' + round(x1) + ' ' + round(y1) +
            ' C ' + round(x1 + dx) + ' ' + round(y1) +
            ', ' + round(x2 - dx) + ' ' + round(y2) +
            ', ' + round(x2) + ' ' + round(y2);
          // B(0.5) = (P0 + 3P1 + 3P2 + P3) / 8
          mx = (x1 + 3 * (x1 + dx) + 3 * (x2 - dx) + x2) / 8;
          my = (y1 + 3 * y1 + 3 * y2 + y2) / 8;
        } else if (from.column > to.column) {
          // Target column to the left: mirrored.
          x1 = a.left; y1 = a.cy;
          x2 = b.right; y2 = b.cy;
          dx = Math.max(30, (x1 - x2) / 2);
          d = 'M ' + round(x1) + ' ' + round(y1) +
            ' C ' + round(x1 - dx) + ' ' + round(y1) +
            ', ' + round(x2 + dx) + ' ' + round(y2) +
            ', ' + round(x2) + ' ' + round(y2);
          mx = (x1 + 3 * (x1 - dx) + 3 * (x2 + dx) + x2) / 8;
          my = (y1 + 3 * y1 + 3 * y2 + y2) / 8;
        } else {
          // Same column: straight vertical line between the facing edges.
          if (b.cy >= a.cy) {
            x1 = a.cx; y1 = a.bottom;
            x2 = b.cx; y2 = b.top;
          } else {
            x1 = a.cx; y1 = a.top;
            x2 = b.cx; y2 = b.bottom;
          }
          d = 'M ' + round(x1) + ' ' + round(y1) + ' L ' + round(x2) + ' ' + round(y2);
          mx = (x1 + x2) / 2;
          my = (y1 + y2) / 2;
        }

        var color = edge.dashed ? STROKE_DASHED : STROKE;
        var path = svgNode('path', {
          'd': d,
          'fill': 'none',
          'stroke': color,
          'stroke-width': '1.75',
          'stroke-opacity': '0.75',
          'marker-end': 'url(#' + markerId(color) + ')'
        });
        if (edge.dashed) path.setAttribute('stroke-dasharray', '5 5');
        if (edge.both) path.setAttribute('marker-start', 'url(#' + markerId(color) + ')');
        svg.appendChild(path);

        if (edge.label) {
          var label = div('dg-edge-label', edge.label);
          label.style.left = round(mx) + 'px';
          label.style.top = round(my) + 'px';
          frameEl.appendChild(label);
          labelEls.push(label);
        }
      });
    }

    function markReady() {
      document.body.dataset.ready = '1';
    }

    drawEdges();

    if (document.fonts && document.fonts.ready && document.fonts.ready.then) {
      document.fonts.ready.then(function () {
        drawEdges();
        markReady();
      });
    } else {
      markReady();
    }
  }

  window.renderDiagram = renderDiagram;
})();
