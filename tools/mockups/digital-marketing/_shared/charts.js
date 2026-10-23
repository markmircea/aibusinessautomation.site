// Minimal SVG charts for the static dashboard mockups: lineChart, barChart, sparkline. No dependencies.
(function () {
  const NS = 'http://www.w3.org/2000/svg';
  const INK = { muted: '#898781', secondary: '#52514e', primary: '#0b0b0b', grid: '#e1e0d9', surface: '#fcfcfb' };
  function make(tag, attrs, parent) {
    const n = document.createElementNS(NS, tag);
    for (const k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }
  function label(parent, x, y, str, attrs) {
    const t = make('text', Object.assign({ x: x, y: y }, attrs || {}), parent);
    t.textContent = str;
    return t;
  }
  function svgFor(el, h) {
    const w = el.clientWidth, height = h || el.clientHeight;
    return { svg: make('svg', { width: w, height: height, viewBox: '0 0 ' + w + ' ' + height }, el), w: w, h: height };
  }

  // opts: { labels: [...], series: [{ name, color, values: [...] }], max, ticks: [...], format: v => string,
  //         labelEvery: n, area: bool (single series only) }
  window.lineChart = function (el, opts) {
    const c = svgFor(el), pad = { l: 48, r: 16, t: 10, b: 26 };
    const iw = c.w - pad.l - pad.r, ih = c.h - pad.t - pad.b, n = opts.labels.length;
    const x = (i) => pad.l + (iw * i) / (n - 1);
    const y = (v) => pad.t + ih - (ih * v) / opts.max;
    opts.ticks.forEach((v) => {
      make('line', { x1: pad.l, x2: c.w - pad.r, y1: y(v), y2: y(v), stroke: v === 0 ? '#c3c2b7' : INK.grid, 'stroke-width': 1 }, c.svg);
      label(c.svg, pad.l - 10, y(v) + 4, opts.format(v), { 'text-anchor': 'end', 'font-size': 11, fill: INK.muted, class: 'tabular' });
    });
    const every = opts.labelEvery || 1;
    opts.labels.forEach((lab, i) => {
      if (i % every === 0) label(c.svg, x(i), c.h - 6, lab, { 'text-anchor': 'middle', 'font-size': 11, fill: INK.muted });
    });
    opts.series.forEach((s) => {
      const pts = s.values.map((v, i) => x(i) + ',' + y(v)).join(' ');
      if (opts.area) make('polygon', { points: x(0) + ',' + y(0) + ' ' + pts + ' ' + x(n - 1) + ',' + y(0), fill: s.color, 'fill-opacity': 0.12 }, c.svg);
      make('polyline', { points: pts, fill: 'none', stroke: s.color, 'stroke-width': 2, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }, c.svg);
      const last = s.values[n - 1];
      make('circle', { cx: x(n - 1), cy: y(last), r: 4, fill: s.color, stroke: INK.surface, 'stroke-width': 2 }, c.svg);
    });
    return c.svg;
  };

  // Horizontal bars, value printed after each bar. opts: { rows: [{ label, value, color }], max, format, rowHeight, labelWidth }
  window.barChart = function (el, opts) {
    const rowH = opts.rowHeight || 36, labelW = opts.labelWidth || 112, valueW = 64, barH = 14;
    const c = svgFor(el, opts.rows.length * rowH), bw = c.w - labelW - valueW;
    opts.rows.forEach((r, i) => {
      const cy = i * rowH + rowH / 2, w = Math.max(6, (bw * r.value) / opts.max), top = cy - barH / 2;
      label(c.svg, 0, cy + 4, r.label, { 'font-size': 12, fill: INK.secondary });
      // square at the baseline, 4px rounded at the data end
      make('path', { d: 'M' + labelW + ' ' + top + 'h' + (w - 4) + 'a4 4 0 0 1 4 4v' + (barH - 8) + 'a4 4 0 0 1-4 4h-' + (w - 4) + 'z', fill: r.color }, c.svg);
      label(c.svg, labelW + w + 8, cy + 4, opts.format(r.value), { 'font-size': 12, 'font-weight': 600, fill: INK.primary, class: 'tabular' });
    });
    return c.svg;
  };

  // Tiny trend line for KPI tiles. The element's size sets the chart size.
  window.sparkline = function (el, values, color) {
    const c = svgFor(el), min = Math.min.apply(null, values), max = Math.max.apply(null, values);
    const x = (i) => 2 + ((c.w - 4) * i) / (values.length - 1);
    const y = (v) => c.h - 3 - ((c.h - 6) * (v - min)) / ((max - min) || 1);
    make('polyline', { points: values.map((v, i) => x(i) + ',' + y(v)).join(' '), fill: 'none', stroke: color, 'stroke-width': 2, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }, c.svg);
    return c.svg;
  };
})();
