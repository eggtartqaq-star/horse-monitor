# -*- coding: utf-8 -*-
"""
General one-page Owner brief → HTML, in the same house style as the front page (scripts/owner_pdf.py).
usage: python3 scripts/owner_pdf_generic.py <brief.txt> <out.html>
Then:  node scripts/owner_pdf_render.js <out.html> <out.pdf> <out.png>   (exits 1 if it does not fit one A4 page)

The brief file has one printed line per row: "TAG<TAB>text". Tags:
  B1 / B2 / B3   start a block with a red / slate / dark-grey banner. Text "title | right line | right line 2".
  LEAD           bold line under a banner.
  BOX            open a red-edged box; text = its label (e.g. 「CRO 嘅全部條件」). Close with ENDBOX.
  N              numbered line (dot colour follows the block: red in B1, slate otherwise).
  T              plain line.   S  bold line.   G  grey smaller line.   C  dark-red bold line.
  TILE           "label | big number" (consecutive TILE rows sit side by side; a third cell may be a G-style note "| note").
  AMBER          line with an amber bar on the left.
  PANEL / ENDPANEL  grey panel; PANEL text = small bold label.
  FOOT           footer (small, centred).
Every line is escaped; <<command>> becomes a grey code box (fmt() from owner_pdf.py).
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from owner_pdf import CSS, fmt  # noqa: E402

EXTRA = """
.b3x { background: #424242; }
.tline { margin: 0.4mm 0; } .gline { color: #555; font-size: 11pt; line-height: 13.5pt; margin: 0.4mm 0; }
.cline { color: #B71C1C; font-weight: bold; margin: 0.6mm 0; } .sline { font-weight: bold; margin: 0.6mm 0; }
.sline, .cline { -webkit-text-stroke: 0.45px currentColor; }   /* the CJK font has no bold face */
body { font-size: 14pt; line-height: 17.5pt; }                    /* one-page briefs are short: larger type */
.redbox { margin-top: 3.5mm; }                                     /* keep the box label clear of the banner */
.redbox .tline, .redbox .gline { margin-left: 7mm; }              /* lines under a numbered item are its sub-lines */
.block { margin-bottom: 4mm; }
.tiles .tile.note { flex: 1 1 auto; }
.panel { margin-bottom: 1.2mm; }
"""
TAGS = {"B1", "B2", "B3", "LEAD", "BOX", "ENDBOX", "N", "T", "S", "G", "C", "TILE", "AMBER", "PANEL", "ENDPANEL",
        "FOOT"}


def load(path):
    rows = []
    for n, row in enumerate(open(path, encoding="utf-8"), 1):
        row = row.rstrip("\n")
        if not row.strip() or row.startswith("#"):
            continue
        tag, _, text = row.partition("\t")
        if tag not in TAGS:
            print(f"line {n}: unknown tag {tag!r}")
            sys.exit(1)
        rows.append((tag, text.strip()))
    return rows


def build(rows):
    h = [f"<!doctype html><html><head><meta charset='utf-8'><title>Owner brief</title>"
         f"<style>{CSS}{EXTRA}</style></head><body><div class='page'>"]
    in_block = in_box = in_panel = False
    dot, num, tiles, foot = "red", 0, [], ""

    def flush_tiles():
        nonlocal tiles
        if tiles:
            cells = []
            for lab, big, note in tiles:
                cells.append(f"<div class='tile'><div class='tl'>{fmt(lab)}</div><div class='tn'>{fmt(big)}</div></div>")
                if note:
                    cells.append(f"<div class='tile note'>{fmt(note)}</div>")
            h.append(f"<div class='tiles'>{''.join(cells)}</div>")
            tiles = []

    for tag, text in rows:
        if tag != "TILE":
            flush_tiles()
        if tag in ("B1", "B2", "B3"):
            if in_panel:
                h.append("</div>"); in_panel = False
            if in_box:
                h.append("</div>"); in_box = False
            if in_block:
                h.append("</div>")
            parts = [p.strip() for p in text.split("|")]
            cls = {"B1": "b1", "B2": "b2", "B3": "b3"}[tag]
            left = "l1" if tag == "B1" else "l2"
            right = "<br>".join(fmt(p) for p in parts[1:])
            rcls = "r" if tag == "B1" else ("r2" if tag == "B2" else "r3")
            h.append(f"<div class='block'><div class='banner {cls}'><div class='{left}'>{fmt(parts[0])}</div>"
                     f"<div class='{rcls}'>{right}</div></div>")
            in_block, dot, num = True, ("red" if tag == "B1" else "slate"), 0
        elif tag == "LEAD":
            h.append(f"<div class='lead'>{fmt(text)}</div>")
        elif tag == "BOX":
            h.append(f"<div class='redbox'><div class='label'>{fmt(text)}</div>"); in_box = True
        elif tag == "ENDBOX":
            h.append("</div>"); in_box = False
        elif tag == "PANEL":
            h.append(f"<div class='panel'><div class='pl'>{fmt(text)}</div>"); in_panel = True
        elif tag == "ENDPANEL":
            h.append("</div>"); in_panel = False
        elif tag == "N":
            num += 1
            h.append(f"<div class='item'><div class='num'><span class='dot {dot}'>{num}</span></div><div>{fmt(text)}</div></div>")
        elif tag == "T":
            h.append(f"<div class='tline'>{fmt(text)}</div>")
        elif tag == "S":
            h.append(f"<div class='sline'>{fmt(text)}</div>")
        elif tag == "G":
            h.append(f"<div class='gline'>{fmt(text)}</div>")
        elif tag == "C":
            h.append(f"<div class='cline'>{fmt(text)}</div>")
        elif tag == "AMBER":
            h.append(f"<div class='amber'>{fmt(text)}</div>")
        elif tag == "TILE":
            parts = [p.strip() for p in text.split("|")] + ["", ""]
            tiles.append((parts[0], parts[1], parts[2]))
        elif tag == "FOOT":
            foot = text
    flush_tiles()
    for flag in (in_panel, in_box, in_block):
        if flag:
            h.append("</div>")
    h.append(f"<div class='footer'>{fmt(foot)}</div></div></body></html>")
    return "\n".join(h)


if __name__ == "__main__":
    rows = load(sys.argv[1])
    open(sys.argv[2], "w", encoding="utf-8").write(build(rows))
    print("rows", len(rows), "->", sys.argv[2])
