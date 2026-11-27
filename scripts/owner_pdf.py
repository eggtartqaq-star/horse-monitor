# -*- coding: utf-8 -*-
"""
Build the Owner's one-page front page (先睇我) as HTML from 翻譯官's line file, then render to PDF.
usage: python3 scripts/owner_pdf.py <lines.txt> <out.html>
The line file has one printed line per row: "L06<TAB>text". Layout follows
reports/owner-summaries/2026-11-27-start-here-v2-layout-en.md (排版師).
Rendering: node <render.js> out.html out.pdf out.png (Playwright, A4, print backgrounds).
"""
import html
import re
import sys

CMDS = ("pip install yfinance pandas numpy requests ta", "cd %USERPROFILE%\\Desktop\\v6.6", "python notify_v66.py --test")
BOLD_FILES = ("電腦檢查_v66.bat", "掃描_v66.bat", "schedule_v66.bat")


def load(path):
    L = {}
    for row in open(path, encoding="utf-8"):
        row = row.rstrip("\n")
        m = re.match(r"^(L\d\d)\t(.*)$", row)
        if m:
            L[m.group(1)] = (L.get(m.group(1), "") + ("\n" if m.group(1) in L else "") + m.group(2)).strip()
    return L


def fmt(t):
    """escape, then: commands -> grey boxes, double-click file names -> bold."""
    out = html.escape(t)
    for c in CMDS:
        out = out.replace(html.escape(c), f'<code>{html.escape(c)}</code>')
    for f in BOLD_FILES:
        out = out.replace(f, f"<b>{f}</b>")
    return out


def lead_bold(t):
    """bold the lead words before the first colon (L44-L46)."""
    m = re.match(r"^(.*?[::])(.*)$", t)
    return f"<b>{html.escape(m.group(1))}</b>{fmt(m.group(2))}" if m else fmt(t)


CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: "WenQuanYi Zen Hei", sans-serif; font-size: 13pt; line-height: 16pt; color: #111; }
.page { width: 210mm; height: 297mm; padding: 10mm 12mm; position: relative; }
.banner { display: flex; justify-content: space-between; align-items: center; color: #fff; border-radius: 2mm; padding: 2mm 4mm; margin-bottom: 2mm; }
.b1 { background: #C62828; min-height: 15mm; } .b2 { background: #37474F; } .b3 { background: #424242; }
.banner .l1 { font-size: 20pt; font-weight: bold; line-height: 22pt; }
.banner .r { text-align: right; font-weight: bold; font-size: 13pt; }
.banner .l2 { font-size: 15pt; font-weight: bold; } .banner .r2 { font-size: 11.5pt; text-align: right; }
.banner .r3 { font-size: 12pt; font-weight: bold; text-align: right; }
.block { margin-bottom: 3.5mm; }
.lead { font-weight: bold; margin: 0 0 2mm 0; }
.redbox { border: 1.5pt solid #C62828; background: #FDECEA; border-radius: 2mm; padding: 4mm 3mm 2.5mm 3mm; position: relative; }
.redbox .label { position: absolute; top: -3mm; left: 4mm; background: #fff; color: #C62828; font-weight: bold; font-size: 11pt; padding: 0 1.5mm; line-height: 13pt; }
.item { display: flex; margin: 0.8mm 0; } .num { flex: 0 0 7mm; }
.dot { display: inline-block; width: 5.2mm; height: 5.2mm; border-radius: 50%; color: #fff; font-size: 9.5pt; line-height: 5.2mm; text-align: center; font-weight: bold; }
.red { background: #C62828; } .slate { background: #37474F; }
.done { color: #555; font-size: 12pt; } .tick { color: #777; font-weight: bold; }
.div { border-top: 0.5pt solid #C62828; margin: 1.5mm 0; }
.conseq { color: #B71C1C; font-weight: bold; } .you { font-weight: bold; }
.tiles { display: flex; gap: 3mm; margin-top: 2.5mm; }
.tile { flex: 0 0 60mm; background: #F5F5F5; border-radius: 2mm; padding: 1.5mm 3mm; }
.tile .tl { font-size: 11pt; color: #555; line-height: 13pt; } .tile .tn { font-size: 18pt; font-weight: bold; line-height: 21pt; }
.tile.note { background: none; border-left: 1pt solid #999; border-radius: 0; color: #666; font-size: 11pt; line-height: 14pt; padding-top: 2.5mm; }
.sub { margin-left: 7mm; } .grey { color: #555; font-size: 12pt; } .gtick { color: #2E7D32; font-weight: bold; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 11pt; background: #EEEEEE; border: 0.5pt solid #BDBDBD; border-radius: 2mm; padding: 0.3mm 2.5mm; white-space: nowrap; }
.amber { border-left: 3pt solid #F9A825; padding-left: 4mm; margin-bottom: 1.5mm; }
.panel { background: #F5F5F5; border-radius: 2mm; padding: 2mm 3mm; margin-top: 1.5mm; }
.panel .pl { font-size: 11pt; font-weight: bold; color: #555; }
.ind { margin-left: 4mm; }
.footer { position: absolute; bottom: 4mm; left: 12mm; right: 12mm; text-align: center; color: #888; font-size: 8.5pt; line-height: 10pt; }
"""


def build(L):
    g = lambda k: L.get(k, "")
    items = [("1", "L06"), ("", "L07"), ("2", "L08"), ("3", "L09"), ("4", "L10"), ("5", "L11")]
    h = [f"<!doctype html><html><head><meta charset='utf-8'><title>先睇我</title><style>{CSS}</style></head><body><div class='page'>"]
    # Block 1
    h.append(f"<div class='block'><div class='banner b1'><div class='l1'>{fmt(g('L01'))}</div>"
             f"<div class='r'>{fmt(g('L02'))}<br>{fmt(g('L03'))}</div></div>")
    h.append(f"<div class='lead'>{fmt(g('L04'))}</div><div class='redbox'><div class='label'>{fmt(g('L05'))}</div>")
    for n, k in items:
        dot = f"<span class='dot red'>{n}</span>" if n else ""
        h.append(f"<div class='item'><div class='num'>{dot}</div><div>{fmt(g(k))}</div></div>")
    h.append(f"<div class='item done'><div class='num'><span class='tick'>✓</span></div><div>{fmt(g('L12'))}</div></div>")
    h.append(f"<div class='div'></div><div class='conseq'>{fmt(g('L13'))}</div><div class='you'>{fmt(g('L14'))}</div></div>")
    h.append(f"<div class='tiles'><div class='tile'><div class='tl'>{fmt(g('L15'))}</div><div class='tn'>{fmt(g('L16'))}</div></div>"
             f"<div class='tile'><div class='tl'>{fmt(g('L17'))}</div><div class='tn'>{fmt(g('L18'))}</div></div>"
             f"<div class='tile note'>{fmt(g('L19'))}<br>{fmt(g('L20'))}</div></div></div>")
    # Block 2
    h.append(f"<div class='block'><div class='banner b2'><div class='l2'>{fmt(g('L21'))}</div><div class='r2'>{fmt(g('L22'))}</div></div>")
    steps = [("1", "L23", [("L24", "")]), ("2", "L25", [("L26", "tick"), ("L27", "")]), ("3", "L28", [("L29", "")]),
             ("4", "L30", []), ("5", "L31", [])]
    for n, k, subs in steps:
        h.append(f"<div class='item'><div class='num'><span class='dot slate'>{n}</span></div><div>{fmt(g(k))}</div></div>")
        for sk, kind in subs:
            if kind == "tick":
                h.append(f"<div class='sub grey'><span class='gtick'>✓</span> {fmt(g(sk))}</div>")
            else:
                h.append(f"<div class='sub'>{fmt(g(sk))}</div>")
    h.append("</div>")
    # Block 3
    h.append(f"<div class='block'><div class='banner b3'><div class='l2'>{fmt(g('L32'))}</div><div class='r3'>{fmt(g('L33'))}</div></div>")
    h.append(f"<div class='amber'>{fmt(g('L34'))}<br>{fmt(g('L35'))}<br>{fmt(g('L36'))}</div>")
    h.append(f"<div>{fmt(g('L37'))}</div><div><b>{fmt(g('L38'))}</b></div>")
    h.append(f"<div class='panel'><div class='pl'>{fmt(g('L39'))}</div><div>{fmt(g('L40'))}<br>{fmt(g('L41'))}</div>"
             f"<div>{fmt(g('L42'))}</div><div>{fmt(g('L43'))}</div>"
             f"<div class='ind'>{lead_bold(g('L44'))}</div><div class='ind'>{lead_bold(g('L45'))}</div>"
             f"<div class='ind'>{lead_bold(g('L46'))}</div><div><b>{fmt(g('L47'))}</b></div></div></div>")
    h.append(f"<div class='footer'>{fmt(g('L48'))}</div></div></body></html>")
    return "\n".join(h)


if __name__ == "__main__":
    L = load(sys.argv[1])
    missing = [f"L{i:02d}" for i in range(1, 49) if f"L{i:02d}" not in L]
    if missing:
        print("missing lines:", missing)
    open(sys.argv[2], "w", encoding="utf-8").write(build(L))
    print("lines", len(L), "-> ", sys.argv[2])
