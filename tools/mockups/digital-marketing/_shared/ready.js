// Marks the page ready for the screenshot once the window has loaded (images settled) and web fonts are ready.
window.addEventListener('load', function () {
  const done = function () { document.body.dataset.ready = '1'; };
  (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(done, done);
});
