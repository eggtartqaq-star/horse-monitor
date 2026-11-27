// usage: node render.js in.html out.pdf out.png
const { chromium } = require('playwright');
(async () => {
  const [, , inp, pdf, png] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 1 });
  await p.goto('file://' + inp);
  await p.pdf({ path: pdf, format: 'A4', printBackground: true, margin: { top: '0', bottom: '0', left: '0', right: '0' } });
  await p.emulateMedia({ media: 'print' });
  await p.screenshot({ path: png, fullPage: true });
  const m = await p.evaluate(() => {
    const blocks = [...document.querySelectorAll('.block')];
    const last = blocks[blocks.length - 1].getBoundingClientRect().bottom;
    const foot = document.querySelector('.footer');
    return { scroll: document.documentElement.scrollHeight, lastBlockBottom: Math.round(last),
             footerTop: foot ? Math.round(foot.getBoundingClientRect().top) : null,
             footerBottom: foot ? Math.round(foot.getBoundingClientRect().bottom) : null };
  });
  console.log(JSON.stringify(m), '(one A4 page = 1123 px; need lastBlockBottom <= footerTop and footerBottom <= 1123)');
  if (!(m.lastBlockBottom <= m.footerTop && m.footerBottom <= 1123)) {
    console.error('OVERFLOW: content does not fit one A4 page');
    await b.close(); process.exit(1);
  }
  await b.close();
})();
