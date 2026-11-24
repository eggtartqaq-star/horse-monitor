#!/usr/bin/env python3
"""皮褸黃 Capital — MASTER Owner Report: all five names in one document."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib import font_manager
import textwrap, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _generator import STOCKS as DET

for _f in ("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",):
    try: font_manager.fontManager.addfont(_f)
    except Exception: pass

BLUE="#2a78d6"; BLUE_LT="#cde2fb"; RED="#d03b3b"; AMBER="#fab219"
SURFACE="#fcfcfb"; INK="#0b0b0b"; INK2="#52514e"; INK3="#8a8985"
GRID="#e3e2df"; CONTEXT="#c3c2bd"; PANEL="#f4f3f0"

plt.rcParams.update({
    "font.family":["DejaVu Sans","WenQuanYi Zen Hei"], "font.size":9,
    "figure.facecolor":SURFACE,"axes.facecolor":SURFACE,"savefig.facecolor":SURFACE,
    "text.color":INK,"axes.labelcolor":INK2,"xtick.color":INK2,"ytick.color":INK2,
    "axes.edgecolor":GRID,"pdf.fonttype":42,"text.parse_math":False})

# ticker: name, price, fv_lo, fv_hi, fv_mid, drawdown, verdict, vcolor,
#         quality, price_attr, risk, one_liner, keep_watching
S = [
 ("KLAC","KLA Corporation",212.75,95,160,95,30.8,"VETO ON PRICE — STRONGEST CANDIDATE",AMBER,88,38,31,
  "The best business we found: a genuine wide-moat monopoly in chip inspection, ~43% returns on capital even at the bottom of its cycle. Only the price is wrong.",
  "Watch $130, then $95-105."),
 ("MU","Micron Technology",806.46,250,400,320,33.5,"WATCH — DO NOT BUY HERE",AMBER,70,20,38,
  "Record-breaking numbers — $18.3B of free cash flow in one quarter, 2026 output sold out — but the price assumes the memory boom never ends.",
  "Watch $780-805 on a close above $830; deeper $680-705."),
 ("MRVL","Marvell Technology",188.68,55,105,70,42.8,"VETOED",RED,52,26,24,
  "A real AI-chip grower, but the number two in a duopoly Broadcom dominates, 82% of revenue in ten customers, and it has never earned its cost of capital.",
  "Watch ~$70. Needs a third socket NOT to be lost."),
 ("INTC","Intel Corporation",91.68,22,55,33,35.6,"VETO ON PRICE — BUSINESS IMPROVING",AMBER,45,14,28,
  "The only one of the five where the business is genuinely getting better — best quarter in 15 years, 18A shipping — but the stock is up 343% and sits above even our own bull case.",
  "Hard price gate: nothing at or above $45."),
 ("BE","Bloom Energy",214.96,35,59,42,38.8,"VETOED — WEAKEST FILE",RED,35,10,18,
  "A real power bottleneck and explosive growth, wrapped around a company that has never earned its cost of capital in 25 years, with ~43% of revenue flowing through a vehicle it co-owns.",
  "Watch related-party revenue falling as a share of total."),
]

def foot(fig, page, total):
    fig.text(0.5,0.048,"Research and decision support only — NOT financial advice. Markets cannot be reliably predicted.",
             fontsize=7.6,color=INK3,ha="center",style="italic")
    fig.text(0.5,0.032,"No agent may place a trade. Nothing happens unless the Owner places it personally.",
             fontsize=7.6,color=INK3,ha="center",weight="bold")
    fig.text(0.945,0.016,f"{page} / {total}",fontsize=7,color=INK3,ha="right")

# ───────────────────────── PAGE 1 — the whole picture ─────────────────────
def page_overview(pdf):
    fig=plt.figure(figsize=(8.27,11.69)); bg=fig.add_axes([0,0,1,1]); bg.axis("off")
    bg.add_patch(Rectangle((0,0.90),1,0.10,color=PANEL))
    bg.text(0.055,0.963,"皮褸黃 Capital",fontsize=23,weight="bold",color=INK,va="center")
    bg.text(0.055,0.933,"Five-Stock Research Review — every finding from the AI departments",
            fontsize=12.5,color=INK2,va="center")
    bg.text(0.055,0.913,"Prepared by 皮褸黃, Chief AI Executive · data as of 17–27 July 2026",
            fontsize=8.2,color=INK3,va="center")

    # headline finding
    bg.add_patch(FancyBboxPatch((0.055,0.812),0.89,0.072,boxstyle="round,pad=0.007",
                 facecolor=RED,edgecolor="none"))
    bg.text(0.5,0.868,"THE MOST IMPORTANT FINDING",fontsize=8.5,weight="bold",
            color="#ffffff",ha="center",va="center")
    for i,l in enumerate(["All five names are the same bet. Micron sells the memory, Marvell the silicon,",
                          "KLA the tools that build it, Intel the processors, Bloom the electricity that runs it —",
                          "all funded from one budget: hyperscaler AI spending. Owning several is not diversifying."]):
        bg.text(0.5,0.850-i*0.0145,l,fontsize=8.8,color="#ffffff",ha="center",va="center")

    # verdict table
    bg.text(0.055,0.792,"THE VERDICTS",fontsize=10,weight="bold",color=INK,va="top")
    hdr=["","Company","Price","Our value","Verdict"]
    xs=[0.058,0.135,0.315,0.415,0.545]
    bg.text(0.058,0.775,"STOCK",fontsize=7.5,color=INK3,weight="bold",va="top")
    for x,h in zip(xs[1:],hdr[1:]):
        bg.text(x,0.775,h.upper(),fontsize=7.5,color=INK3,weight="bold",va="top")
    y=0.760
    for t,nm,px,lo,hi,mid,dd,vd,vc,q,pa,rk,one,watch in S:
        bg.add_patch(Rectangle((0.055,y-0.019),0.89,0.024,
                     facecolor=PANEL if S.index((t,nm,px,lo,hi,mid,dd,vd,vc,q,pa,rk,one,watch))%2==0 else SURFACE,
                     edgecolor="none"))
        bg.text(0.058,y,t,fontsize=10,weight="bold",color=INK,va="center")
        bg.text(0.135,y,nm,fontsize=8.3,color=INK2,va="center")
        bg.text(0.315,y,f"${px:,.2f}",fontsize=8.3,color=INK,va="center")
        bg.text(0.415,y,f"${lo}–{hi}",fontsize=8.3,color=BLUE,va="center")
        bg.text(0.545,y,vd,fontsize=7.6,weight="bold",color=RED if vc==RED else "#8a6400",va="center")
        y-=0.024

    # ── chart 1: the two-axis quadrant (the firm's rebuilt scorecard) ──
    ax=fig.add_axes([0.335,0.395,0.475,0.215])
    ax.axhspan(50,100,xmin=0,xmax=0.5,color="#f7f7f4",zorder=0)
    ax.axvline(50,color=INK3,lw=1,ls=(0,(4,3)),zorder=1)
    ax.axhline(50,color=INK3,lw=1,ls=(0,(4,3)),zorder=1)
    for t,nm,px,lo,hi,mid,dd,vd,vc,q,pa,rk,one,watch in S:
        ax.scatter([pa],[q],s=190,color=BLUE,zorder=5,edgecolor=SURFACE,linewidth=2)
        ax.text(pa,q+5.5,t,fontsize=8.6,weight="bold",color=INK,ha="center",zorder=6)
    ax.set_xlim(0,100); ax.set_ylim(0,100)
    ax.set_xlabel("PRICE ATTRACTIVENESS  →  cheaper",fontsize=7.8,color=INK2)
    ax.set_ylabel("QUALITY  →",fontsize=8,color=INK2)
    ax.text(2,95,"good business,\nwrong price",fontsize=7.4,color=INK3,va="top")
    ax.text(97,95,"the rare buy",fontsize=7.4,color=INK3,va="top",ha="right")
    ax.text(2,6,"decline",fontsize=7.4,color=INK3,va="bottom")
    ax.text(97,6,"value-trap risk",fontsize=7.4,color=INK3,va="bottom",ha="right")
    ax.set_axisbelow(True); ax.grid(color=GRID,lw=0.7)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    fig.text(0.055,0.607,"QUALITY vs PRICE",fontsize=10,weight="bold",color=INK)
    fig.text(0.055,0.593,"The firm's rebuilt\nscorecard, after the\nAI Auditor found the\nold one blended these\ntwo things together.\n\nAll five sit on the\nLEFT: every one is\nexpensive on our\nnumbers. None is in\nthe buy corner.\nQuality varies widely\n\u2014 KLAC top, BE bottom.\n\nScores are the CEO's\ncomposites of the\ndepartment scores;\nsee the .md note.",
             fontsize=8,color=INK2,va="top",linespacing=1.55)

    # ── chart 2: how many times fair value ──
    ax2=fig.add_axes([0.335,0.215,0.475,0.115])
    tick=[x[0] for x in S]; mult=[x[2]/x[5] for x in S]
    ax2.bar(tick,mult,color=BLUE,width=0.5,zorder=3)
    ax2.set_xlim(-1.15,len(tick)-0.4)
    for i,m in enumerate(mult):
        ax2.text(i,m+0.12,f"{m:.1f}x",ha="center",fontsize=8.8,weight="bold",color=INK)
    ax2.axhline(1.0,color=RED,lw=1.6,zorder=4)
    ax2.text(-1.10,1.05,"fair\nvalue",fontsize=7.2,color=RED,ha="left",va="bottom",linespacing=1.2)
    ax2.set_ylim(0,6.0); ax2.set_ylabel("× our fair value",fontsize=8)
    ax2.set_axisbelow(True); ax2.yaxis.grid(True,color=GRID,lw=0.8)
    for s in ("top","right"): ax2.spines[s].set_visible(False)
    ax2.tick_params(axis="x",length=0,labelsize=9)
    fig.text(0.055,0.327,"WHAT YOU'D PAY",fontsize=10,weight="bold",color=INK)
    fig.text(0.055,0.313,"How many times our own\nestimate of value each\nstock costs today.\nThe red line is fair value.",
             fontsize=8,color=INK2,va="top",linespacing=1.55)

    # ── chart 3: drawdowns ──
    ax3=fig.add_axes([0.335,0.085,0.475,0.085])
    dds=[x[6] for x in S]
    ax3.bar(tick,dds,color=CONTEXT,width=0.5,zorder=3)
    for i,d in enumerate(dds):
        ax3.text(i,d+1.3,f"−{d:.0f}%",ha="center",fontsize=8.4,color=INK2)
    ax3.set_ylim(0,52); ax3.set_ylabel("fall from high",fontsize=8)
    ax3.set_axisbelow(True); ax3.yaxis.grid(True,color=GRID,lw=0.8)
    for s in ("top","right"): ax3.spines[s].set_visible(False)
    ax3.tick_params(axis="x",length=0,labelsize=9)
    fig.text(0.055,0.167,"ALREADY FALLEN",fontsize=10,weight="bold",color=INK)
    fig.text(0.055,0.153,"All five dropped hard in the\nJuly chip selloff — and all\nfive are still expensive on\nour numbers.",
             fontsize=8,color=INK2,va="top",linespacing=1.55)
    foot(fig,1,len(S)+2); pdf.savefig(fig); plt.close(fig)

# ───────────────────────── PER-STOCK PAGES ────────────────────────────────
def page_stock(pdf,rec,idx,total):
    t,nm,px,lo,hi,mid,dd,vd,vc,q,pa,rk,one,watch = rec
    fig=plt.figure(figsize=(8.27,11.69)); bg=fig.add_axes([0,0,1,1]); bg.axis("off")
    bg.add_patch(Rectangle((0,0.935),1,0.065,color=PANEL))
    bg.text(0.055,0.972,t,fontsize=22,weight="bold",color=INK,va="center")
    bg.text(0.055,0.948,nm,fontsize=11,color=INK2,va="center")
    bg.text(0.945,0.960,"皮褸黃 Capital · Owner Review",fontsize=8,color=INK3,ha="right",va="center")

    bg.add_patch(FancyBboxPatch((0.055,0.880),0.89,0.042,boxstyle="round,pad=0.006",
                 facecolor=vc,edgecolor="none"))
    bg.text(0.5,0.901,vd,fontsize=12.5,weight="bold",
            color=INK if vc==AMBER else "#ffffff",ha="center",va="center")

    for i,(lb,vl,cl) in enumerate([("Price today",f"${px:,.2f}",INK),
                                   ("Our fair value",f"${lo}–{hi}",BLUE),
                                   ("Times fair value",f"{px/mid:.1f}x",RED),
                                   ("Fall from high",f"−{dd:.0f}%",INK)]):
        x=0.055+i*0.2225
        bg.add_patch(Rectangle((x,0.795),0.205,0.070,facecolor=PANEL,edgecolor="none"))
        bg.text(x+0.1025,0.843,lb,fontsize=7.6,color=INK3,ha="center",va="center")
        bg.text(x+0.1025,0.818,vl,fontsize=15,weight="bold",color=cl,ha="center",va="center")

    yy=0.775
    for line in textwrap.wrap(one,90):
        bg.text(0.055,yy,line,fontsize=10.8,color=INK,va="top",style="italic"); yy-=0.0175

    # quality / price bars
    ax=fig.add_axes([0.30,0.640,0.615,0.075])
    ax.barh([1,0],[q,pa],height=0.5,color=[BLUE,BLUE],zorder=3)
    for i,v in zip([1,0],[q,pa]):
        ax.text(v+1.5,i,str(v),va="center",fontsize=9.5,weight="bold",color=INK)
    ax.axvline(50,color=INK3,lw=1,ls=(0,(4,3)),zorder=4)
    ax.set_yticks([1,0]); ax.set_yticklabels(["Business quality","Price attractiveness"],fontsize=8.7)
    ax.set_xlim(0,108); ax.set_xticks([0,25,50,75,100])
    ax.set_axisbelow(True); ax.xaxis.grid(True,color=GRID,lw=0.8)
    for s in ("top","right","left"): ax.spines[s].set_visible(False)
    ax.tick_params(axis="y",length=0)
    fig.text(0.055,0.716,"THE TWO SCORES",fontsize=9.5,weight="bold",color=INK)
    fig.text(0.055,0.702,"Judged separately, so a\ngood company at a bad\nprice is never recorded\nas a bad company.",
             fontsize=7.9,color=INK2,va="top",linespacing=1.5)

    # price gap
    ax2=fig.add_axes([0.30,0.520,0.615,0.075])
    top=max(px,hi)*1.20
    ax2.barh([0],[hi-lo],left=[lo],height=0.30,color=BLUE_LT,edgecolor=BLUE,lw=1.4,zorder=3)
    ax2.plot([mid],[0],marker="D",ms=8,color=BLUE,zorder=5)
    ax2.plot([px],[0],marker="o",ms=12,color=RED,zorder=6,markeredgecolor=SURFACE,markeredgewidth=2)
    ax2.text(px,0.28,f"  YOU PAY ${px:,.0f}",fontsize=9,weight="bold",color=RED,ha="center",va="bottom")
    ax2.text((lo+hi)/2,-0.30,f"worth ${lo}–{hi}",fontsize=8.2,color=BLUE,ha="center",va="top")
    ax2.set_xlim(0,top); ax2.set_ylim(-0.7,0.7); ax2.set_yticks([])
    ax2.set_xlabel("US$ per share",fontsize=8)
    ax2.set_axisbelow(True); ax2.xaxis.grid(True,color=GRID,lw=0.8)
    for s in ("top","right","left"): ax2.spines[s].set_visible(False)
    fig.text(0.055,0.596,"THE PRICE GAP",fontsize=9.5,weight="bold",color=INK)
    fig.text(0.055,0.582,"Blue = what it's worth.\nRed = what it costs.",
             fontsize=7.9,color=INK2,va="top",linespacing=1.5)

    # detail from the per-stock PDFs
    from _generator import STOCKS as DET
    d=DET[t]
    y=0.480
    def sect(title,items,col,y,maxn=4):
        bg.add_patch(Rectangle((0.055,y-0.004),0.006,0.017,color=col))
        bg.text(0.075,y+0.004,title,fontsize=10,weight="bold",color=INK,va="center")
        y-=0.024
        shown=items[:maxn]
        for it in shown:
            lines=textwrap.wrap(it,101)
            bg.text(0.072,y,"•",fontsize=9,color=col,va="top",weight="bold")
            for j,l in enumerate(lines):
                bg.text(0.088,y-j*0.0152,l,fontsize=8.3,color=INK2,va="top")
            y-=len(lines)*0.0152+0.0072
        if len(items)>len(shown):
            bg.text(0.088,y,f"+ {len(items)-len(shown)} further point(s) in the {t} single-stock PDF",
                    fontsize=7.6,color=INK3,va="top",style="italic")
            y-=0.016
        return y-0.014
    y=sect("WHAT'S GOOD",d["good"],BLUE,y)
    y=sect("WHAT'S WRONG",d["bad"],RED,y)

    y = max(y, 0.128)          # hard floor: never encroach on the compliance footer
    bg.add_patch(FancyBboxPatch((0.055,y-0.048),0.89,0.044,boxstyle="round,pad=0.006",
                 facecolor=PANEL,edgecolor=GRID))
    bg.text(0.072,y-0.014,"WHAT WOULD MAKE US LOOK AGAIN",fontsize=8.8,weight="bold",color=INK,va="top")
    bg.text(0.072,y-0.031,watch,fontsize=9,color=INK2,va="top",weight="bold")
    foot(fig,idx,total); pdf.savefig(fig); plt.close(fig)

# ───────────────────────── FINAL PAGE — what we learned ───────────────────
def page_lessons(pdf,total):
    fig=plt.figure(figsize=(8.27,11.69)); bg=fig.add_axes([0,0,1,1]); bg.axis("off")
    bg.add_patch(Rectangle((0,0.935),1,0.065,color=PANEL))
    bg.text(0.055,0.965,"What the firm learned about itself",fontsize=18,weight="bold",color=INK,va="center")
    bg.text(0.055,0.945,"The AI Auditor checks every department's work. Here is what it caught.",
            fontsize=9,color=INK2,va="center")

    y=0.905
    def blk(title,body,col,y):
        bg.add_patch(Rectangle((0.055,y-0.004),0.006,0.017,color=col))
        bg.text(0.075,y+0.004,title,fontsize=10.5,weight="bold",color=INK,va="center")
        y-=0.026
        for line in textwrap.wrap(body,104):
            bg.text(0.072,y,line,fontsize=8.6,color=INK2,va="top"); y-=0.0158
        return y-0.016

    y=blk("A BAD PRICE FEED WAS CAUGHT AND CORRECTED (Micron)",
      "One analyst reported buyers stepping in at $850 — from a data source that was simply wrong. The stock had "
      "actually closed at its low. The report was failed, corrected and re-issued, and that data provider is now "
      "banned firm-wide. Without the check, the trading desk would have had guidance built on an event that never happened.",BLUE,y)
    y=blk("A REPORT WENT MISSING AND I MIS-LABELLED THE RECORD (Marvell)",
      "The moat analysis failed to save because of a silent error, and I recorded it as filed anyway. Two later reports "
      "leaned on it without noticing. The auditor found the file did not exist. It has been re-written and the record corrected.",RED,y)
    y=blk("THE DESK TALKED ITSELF INTO A BEARISH VIEW (KLA)",
      "Three separate mistakes all pushed the same direction — a mislabelled valuation multiple, an earnings estimate 20% "
      "below consensus, and a backwards peer comparison — after three straight negative verdicts. The auditor called it "
      "narrative lock-in. The work was sent back and redone on honest numbers. The conclusion survived, but was far less extreme.",RED,y)
    y=blk("A FALSE PROFIT FIGURE PASSED FOUR ANALYSTS (Bloom Energy)",
      "The financial report showed a $6M profit for 2025. The filed figure was an $87M LOSS. The correct number was sitting "
      "in another report in the same package, on the same day, and nobody cross-checked it. The auditor also found the four "
      "reports were substantially one analyst's opinion wearing four signatures.",RED,y)
    y=blk("MY OWN SCORING SYSTEM WAS BROKEN (Intel)",
      "The scorecard I designed put about 60% of its weight on one thing — price versus value — so any fairly-priced stock "
      "was capped near 40 regardless of quality. It scored Intel 12, below two weaker businesses, on the same day an analyst "
      "called Intel the only one of the five that is genuinely improving. The scorecard now has two separate axes, which is "
      "the quadrant chart on page 1.",AMBER,y)

    # decisions
    bg.add_patch(FancyBboxPatch((0.055,y-0.182),0.89,0.178,boxstyle="round,pad=0.008",
                 facecolor="#fdf6e3",edgecolor=AMBER,linewidth=1.5))
    bg.text(0.072,y-0.016,"THREE DECISIONS ONLY YOU CAN MAKE",fontsize=11,weight="bold",color=INK,va="top")
    dec=[("1. How cheap is cheap enough?",
          "Five names, five rejections — and not one was stopped by a risk limit. Every one was stopped by the "
          "margin-of-safety rule I wrote and you never approved. If it demands more discount than this market offers, "
          "it will keep saying no forever. Your risk officer has escalated this himself."),
         ("2. Your targets break your own rule.",
          "The plan sets AI 30% + Technology 20% = 50%, but the risk file caps any single correlated bet at 40%. "
          "Either raise the cap, or redefine the sleeves so they aren't the same bet. Escalated five times."),
         ("3. The portfolio file is still empty.",
          "No holdings, no cash. Every percentage limit is a fraction of a number nobody knows.")]
    yy=y-0.040
    for h,b in dec:
        bg.text(0.072,yy,h,fontsize=9,weight="bold",color=INK,va="top"); yy-=0.0148
        for line in textwrap.wrap(b,100):
            bg.text(0.082,yy,line,fontsize=8.2,color=INK2,va="top"); yy-=0.0138
        yy-=0.006
    foot(fig,total,total); pdf.savefig(fig); plt.close(fig)

# consistency gate: master data must match the single-stock source of truth
for _r in S:
    _t,_px = _r[0], _r[2]
    assert abs(DET[_t]["price"]-_px) < 0.01, f"price mismatch for {_t}: {DET[_t]['price']} vs {_px}"
    _dd = (1-DET[_t]["price"]/DET[_t]["high"])*100
    assert abs(_dd-_r[6]) < 0.15, f"drawdown mismatch for {_t}: {_dd:.2f} vs {_r[6]}"

out="/home/user/horse-monitor/reports/owner-summaries/ALL-STOCKS-master-review-2026-07.pdf"
total=len(S)+2
with PdfPages(out) as pdf:
    page_overview(pdf)
    for i,rec in enumerate(S): page_stock(pdf,rec,i+2,total)
    page_lessons(pdf,total)
print("wrote",out)
