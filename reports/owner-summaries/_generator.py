#!/usr/bin/env python3
"""
皮褸黃 Capital — Owner Summary PDFs
One PDF per stock, summarising every AI agent's finding, with charts.
Authored by the CEO (皮褸黃) from the committed department reports.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle, FancyBboxPatch
import textwrap, os

# ---- palette (validated: blue+red all-pairs PASS light) -------------------
BLUE     = "#2a78d6"
BLUE_LT  = "#cde2fb"
RED      = "#d03b3b"
AMBER    = "#fab219"
SURFACE  = "#fcfcfb"
INK      = "#0b0b0b"
INK2     = "#52514e"
INK3     = "#8a8985"
GRID     = "#e3e2df"
CONTEXT  = "#c3c2bd"

from matplotlib import font_manager
for _f in ("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",):
    try: font_manager.fontManager.addfont(_f)
    except Exception: pass

plt.rcParams.update({
    "font.family": ["DejaVu Sans", "WenQuanYi Zen Hei"], "font.size": 9,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "text.color": INK,
    "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.edgecolor": GRID, "pdf.fonttype": 42,
    "text.parse_math": False,
})

DRAWDOWNS = {"MU": 33.5, "MRVL": 42.8, "KLAC": 30.0, "BE": 37.5}

STOCKS = {
"MU": dict(
  name="Micron Technology", verdict="WATCH — DO NOT BUY AT THIS PRICE",
  vcolor=AMBER, price=806.46, pdate="17 Jul 2026",
  high=1213.37, hdate="25 Jun 2026 close",
  fv_lo=250, fv_hi=400, fv_mid=320,
  risk="APPROVED WITH CONDITIONS — max 6.5% of portfolio",
  scores=[("Financials (巴爺爺)",82),("News & Sentiment (修大哥)",68),
          ("Technicals (老詹)",45),("Macro (Peterson)",40),
          ("Risk (John, CRO)",38),("Valuation Analyst",15)],
  headline="A superb business in the best quarter of its industry's history — at a price that already assumes the boom never ends.",
  good=[
    "Best numbers in memory-industry history: FQ3 revenue $41.46B, up 345% year-on-year, with an 84.9% gross margin.",
    "$18.3B of free cash flow in ONE quarter; balance sheet flipped to $24.4B net cash.",
    "2026 HBM output completely sold out under 16 take-or-pay contracts claiming ~$100B of minimum revenue.",
    "Management (grade A−) has a proven record of cutting supply fast in downturns — they cut capex >40% in 2023.",
    "Industry desk is OVERWEIGHT memory (60% confidence): AI/HBM demand is real and contract-backed.",
  ],
  bad=[
    "Moat is NARROW and unproven through a downturn — memory was historically a no-moat commodity business (2023 ROIC was about −11%).",
    "Valuation is the killer: fair value $250–400 vs a $806 price. The price needs today's 85% margins to last forever.",
    "China's CXMT is approaching Micron's wafer capacity and will re-commoditise the non-HBM half of the business.",
    "Insider selling at the highest level since 2010; a celebrity short (Michael Burry) went public at $1,051.",
    "The tape is in genuine distribution — 3 straight heavy selling days, closing at the low.",
  ],
  watch=[
    "Price entering $780–805, but only on a daily close back above $830 (do not buy the touch).",
    "Deeper zone $680–705 (the 61.8% retracement) if $775 breaks.",
    "Q4-2026 HBM contract repricing — the single biggest fundamental tripwire.",
    "CXMT's DDR5 yields, and the US export-rule decision on HBM.",
  ],
  audit="11 of 12 reports passed. The market-structure report FAILED on a bad price feed (claimed dip-buying that never happened) and was corrected and re-issued.",
),
"MRVL": dict(
  name="Marvell Technology", verdict="VETOED BY RISK — DO NOT BUY",
  vcolor=RED, price=188.68, pdate="17 Jul 2026",
  high=329.88, hdate="18 Jun 2026",
  fv_lo=55, fv_hi=105, fv_mid=70,
  risk="VETOED — no entry clears both timing and valuation",
  scores=[("Financials (巴爺爺)",66),("News & Sentiment (修大哥)",64),
          ("Macro (Peterson)",52),("Technicals (老詹)",34),
          ("Valuation Analyst",25),("Risk (John, CRO)",24)],
  headline="A real AI-silicon grower, but the number-two in a duopoly Broadcom dominates — and a moat that has never once earned its cost of capital.",
  good=[
    "Genuine AI inflection: FY26 revenue $8.195B (+42%); data centre is now 76% of the business.",
    "Rebuilt win slate — a new Google 'Merope' inference chip worth up to $12B over its life, plus Microsoft Maia 300 and an Amazon Trainium 4 variant.",
    "The optics franchise is the real moat: ~60–70% share of 400G+ optical DSPs, held through a technology transition.",
    "Management (B+) allocated capital well — sold the auto-Ethernet unit for $2.5B cash and bought back stock near the lows.",
    "Balance sheet is safe: $3.84B cash vs $4.96B of laddered fixed-rate debt, interest covered ~7x.",
  ],
  bad=[
    "Has NEVER earned its cost of capital including the goodwill from Inphi/Cavium — roughly 6% GAAP ROIC.",
    "Custom-chip 'lock-in' lasts one generation, not several: Amazon's Trainium 3 compute die went to a cheaper Taiwanese rival.",
    "Top-10 customers are 82% of revenue — the highest concentration in the firm's coverage.",
    "Essentially 100% dependent on TSMC for both wafers and packaging, with no owned fabs and no hedge.",
    "Fair value $55–105 vs a $188 price. Even the bull case is 45% below the current price.",
  ],
  watch=[
    "Price near $70 (fair value) — or a documented re-rating that creates a real margin of safety.",
    "Whether Trainium 4, Maia 300 or Google Merope slip to a competitor — a third socket loss confirms commoditisation.",
    "Any big-four hyperscaler cutting 2026–27 capex guidance.",
    "Confirmed technical reversal — the chart says do not catch this knife.",
  ],
  audit="Valuation and risk passed with flags. The moat report was found MISSING from disk (a silent write failure by the CEO) and was re-filed.",
),
"KLAC": dict(
  name="KLA Corporation", verdict="VETOED ON PRICE ONLY — STRONGEST CANDIDATE",
  vcolor=AMBER, price=212.75, pdate="17 Jul 2026 (after 10-for-1 split)",
  high=307.37, hdate="30 Jun 2026",
  fv_lo=95, fv_hi=160, fv_mid=95,
  risk="VETOED on valuation alone — quality and timing both acceptable",
  scores=[("Financials (巴爺爺)",91),("News & Sentiment (修大哥)",64),
          ("Technicals (老詹)",58),("Macro (Peterson)",56),
          ("Valuation Analyst",33),("Risk (John, CRO)",31)],
  headline="The best business the firm has analysed — a genuine wide-moat monopoly. The only thing wrong with it is the price.",
  good=[
    "The ONLY name of the four with a WIDE and WIDENING moat: ~56–63% of process control, over 85% of optical inspection, and still gaining share.",
    "Returns are extraordinary and durable: ~43% average ROIC, and still ~25% at the WORST point of the cycle — about 2x its cost of capital in its worst year.",
    "Highest financial score in the firm's coverage: 91/100, grade A. Interest covered 15–18x; 'effectively bulletproof'.",
    "17 consecutive annual dividend increases; $7B buyback on top of an existing $5B programme.",
    "Held up far better in the July selloff (−18 to −30%) than Micron (−33%) or Marvell (−43%) — real relative strength.",
    "Twin secular drivers: AI leading-edge inspection plus advanced packaging revenue up ~57% to ~$1B.",
  ],
  bad=[
    "At ~42x forward and ~61x trailing earnings, it trades at roughly TWICE its own historical multiple of ~22x.",
    "Fair value $95–160 against a $212.75 price — the 30% fall is off a bubble peak, not into value.",
    "The CRO's warning: a wide moat protects the business, not the multiple. A de-rate to its historic multiple is ~40% even if KLA executes perfectly.",
    "Equipment is DIRECTLY export-controlled — regulation is a net headwind here, unlike for a fab owner.",
    "Earnings on 28 July with a ±8% implied move, and no succession plan for a 65-year-old CEO of 20 years.",
  ],
  watch=[
    "PRIMARY ALERT: ~$130 — first watch level for a starter position.",
    "SIZE-UP ALERT: ~$95–105 — the firm's base fair value.",
    "The 28 July earnings and 29 July Fed meeting could deliver a better entry.",
    "A Chinese domestic inspection tool qualified at an advanced node would end the moat story.",
  ],
  audit="The audit FAILED the valuation for bias — it had mislabelled the forward multiple, used an EPS 20% below consensus, and got the peer comparison backwards after three straight bearish verdicts. Corrected: score rose 22 → 33, fair value gap narrowed from −188% to −126%. The conclusion survived on honest numbers.",
),
"BE": dict(
  name="Bloom Energy", verdict="VETOED — WEAKEST FILE OF THE FOUR",
  vcolor=RED, price=214.96, pdate="17 Jul 2026",
  high=345.0, hdate="late Jun 2026 (sources conflict)",
  fv_lo=35, fv_hi=59, fv_mid=42,
  risk="VETOED — fails on price, on measurement, AND on process",
  scores=[("News & Sentiment (修大哥)",68),("Financials (巴爺爺, corrected)",45),
          ("Risk (John, CRO)",18),("Valuation Analyst",8)],
  headline="A real bottleneck, a real order book — wrapped around a company that has never earned its cost of capital in 25 years, with half its revenue flowing through a vehicle it co-owns.",
  good=[
    "The bottleneck is real and datable: grid connection queues now exceed 8 years, and Bloom can deploy on-site power in ~90 days.",
    "Explosive growth: Q1-2026 revenue $751.1M, up 130% year-on-year; full-year guidance $3.4–3.8B.",
    "Brookfield expanded its financing framework FIVE-FOLD to $25B (30 June 2026).",
    "Genuinely excellent balance sheet: no net debt, a 0% coupon, and nothing due until November 2030.",
    "Policy is a real tailwind — the 30% fuel-cell investment tax credit was restored in law, and federal emissions risk to a gas-fired fleet was cut.",
    "First-ever GAAP-profitable quarter arrived in Q1 2026.",
  ],
  bad=[
    "Has NEVER earned its cost of capital in 25 years. ~$4.8B of lifetime capital raised; FY2025 was a NET LOSS of $87.1M.",
    "About 43% of FY2025 revenue ran through joint ventures Bloom CO-OWNS — the moat analyst calls it 'a financing structure being reported as demand'.",
    "Shareholders diluted ~85% in five years, and $2.2B of convertible notes are now in the money — more dilution is live.",
    "Economics are inferior: fuel cells cost $3,000–6,000/kW versus $400–800/kW for gas turbines. The advantage is availability, not cost.",
    "The window closes: GE Vernova's turbine capacity scales through 2029–31, and Bloom is 'the world's best bridge generator — bridges get demolished when the road opens'.",
    "Fair value $35–59 vs a $214.96 price. Even a fully steel-manned bull case is worth $58.61 — 73% below the price.",
    "A short-seller report (8 July) alleges undisclosed China dependence for a key material; two law firms opened investigations. Bloom denies it.",
  ],
  watch=[
    "Whether related-party revenue FALLS as a share of total in the FY2026 annual report — the single highest-information line in the file.",
    "The 28 July earnings, with a ~32% implied move — four times KLA's.",
    "Any filed class-action complaint, auditor change, or equity raise above $194.97.",
    "Price near $35–45 would be a starting point for a conversation, not a buy.",
  ],
  audit="The audit FAILED the financials: FY2025 was reported to the CEO as a $6.0M PROFIT when the filed figure is an $87.1M LOSS — and the correct number was sitting in another report in the same package. It also found the four reports were substantially ONE analyst's opinion wearing four signatures, and that the bull case was never independently tested.",
),
}

def wrap(ax, x, y, text, width=96, size=8.2, color=INK2, weight="normal", lh=0.0165):
    for i, line in enumerate(textwrap.wrap(text, width)):
        ax.text(x, y - i*lh, line, transform=ax.transAxes, fontsize=size,
                color=color, weight=weight, va="top", ha="left")
    return y - len(textwrap.wrap(text, width))*lh

def page1(pdf, t, d):
    fig = plt.figure(figsize=(8.27, 11.69))
    bg = fig.add_axes([0,0,1,1]); bg.axis("off")

    # header band
    bg.add_patch(Rectangle((0, 0.905), 1, 0.095, color="#f4f3f0", zorder=0))
    bg.text(0.055, 0.972, f"{t}", fontsize=26, weight="bold", color=INK, va="center")
    bg.text(0.055, 0.943, d["name"], fontsize=12.5, color=INK2, va="center")
    bg.text(0.055, 0.923, "皮褸黃 Capital · Investment Research Summary for the Owner",
            fontsize=8.2, color=INK3, va="center")
    bg.text(0.945, 0.955, "Prepared by 皮褸黃 (CEO)\nfrom the AI department reports",
            fontsize=8, color=INK3, va="center", ha="right", linespacing=1.5)

    # verdict banner
    bg.add_patch(FancyBboxPatch((0.055, 0.845), 0.89, 0.045,
                 boxstyle="round,pad=0.006", facecolor=d["vcolor"], edgecolor="none", zorder=1))
    vtxt = INK if d["vcolor"] == AMBER else "#ffffff"
    bg.text(0.5, 0.8675, f"CEO VERDICT:  {d['verdict']}", fontsize=13.5, weight="bold",
            color=vtxt, ha="center", va="center", zorder=2)

    # hero numbers
    gap = (d["price"] - d["fv_mid"]) / d["fv_mid"] * 100
    heroes = [("Price (%s)" % d["pdate"].split(" (")[0], f"${d['price']:,.2f}", INK),
              ("Fall from high", f"−{DRAWDOWNS[t]:.0f}%", INK),
              ("Firm's fair value", f"${d['fv_lo']}–{d['fv_hi']}", BLUE),
              ("Price vs fair value", f"+{gap:,.0f}% over", RED)]
    for i, (lbl, val, col) in enumerate(heroes):
        x = 0.055 + i*0.2225
        bg.add_patch(Rectangle((x, 0.755), 0.205, 0.075, facecolor="#f4f3f0", edgecolor="none"))
        bg.text(x+0.1025, 0.807, lbl, fontsize=7.8, color=INK3, ha="center", va="center")
        bg.text(x+0.1025, 0.780, val, fontsize=16, weight="bold", color=col, ha="center", va="center")

    bg.text(0.055, 0.735, "WHAT THE 12 AI DEPARTMENTS CONCLUDED, IN ONE SENTENCE",
            fontsize=8, weight="bold", color=INK3, va="top")
    yy = 0.722
    for line in textwrap.wrap(d["headline"], 88):
        bg.text(0.055, yy, line, fontsize=11.5, color=INK, va="top", style="italic")
        yy -= 0.019

    # ---- chart 1: department scorecard ----
    ax = fig.add_axes([0.28, 0.478, 0.665, 0.168])
    labels = [s[0] for s in d["scores"]][::-1]
    vals   = [s[1] for s in d["scores"]][::-1]
    ypos   = range(len(vals))
    ax.barh(list(ypos), vals, height=0.62, color=BLUE, zorder=3)
    for i, v in enumerate(vals):
        ax.text(v+1.5, i, str(v), va="center", ha="left", fontsize=9,
                weight="bold", color=INK)
    ax.axvline(50, color=INK3, lw=1, ls=(0,(4,3)), zorder=4)
    ax.text(50.8, -0.42, "50 = neutral", fontsize=7.3, color=INK3, va="bottom", ha="left")
    ax.set_yticks(list(ypos)); ax.set_yticklabels(labels, fontsize=8.5)
    ax.set_xlim(0, 108); ax.set_xticks([0,25,50,75,100])
    ax.set_axisbelow(True); ax.xaxis.grid(True, color=GRID, lw=0.8); ax.yaxis.grid(False)
    for s in ("top","right","left"): ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0)
    fig.text(0.055, 0.672, "DEPARTMENT SCORECARD", fontsize=10, weight="bold", color=INK)
    fig.text(0.055, 0.658, "Each AI department scored the idea out of 100. Lower = worse for buying at today's price.",
             fontsize=8.2, color=INK2, va="top")

    # ---- chart 2: valuation gap ----
    ax2 = fig.add_axes([0.28, 0.315, 0.665, 0.095])
    top = max(d["price"], d["fv_hi"]) * 1.18
    ax2.barh([0], [d["fv_hi"]-d["fv_lo"]], left=[d["fv_lo"]], height=0.34,
             color=BLUE_LT, edgecolor=BLUE, lw=1.4, zorder=3)
    ax2.plot([d["fv_mid"]], [0], marker="D", ms=9, color=BLUE, zorder=5)
    ax2.plot([d["price"]], [0], marker="o", ms=13, color=RED, zorder=6,
             markeredgecolor=SURFACE, markeredgewidth=2)
    ax2.text(d["price"], 0.30, f"  PRICE ${d['price']:,.0f}", fontsize=9.5, weight="bold",
             color=RED, ha="center", va="bottom")
    ax2.text((d["fv_lo"]+d["fv_hi"])/2, -0.33,
             f"fair value ${d['fv_lo']}–{d['fv_hi']}", fontsize=8.5,
             color=BLUE, ha="center", va="top")
    ax2.set_xlim(0, top); ax2.set_ylim(-0.75, 0.75); ax2.set_yticks([])
    ax2.set_xlabel("US$ per share", fontsize=8)
    ax2.set_axisbelow(True); ax2.xaxis.grid(True, color=GRID, lw=0.8)
    for s in ("top","right","left"): ax2.spines[s].set_visible(False)
    fig.text(0.055, 0.443, "THE PRICE GAP", fontsize=10, weight="bold", color=INK)
    fig.text(0.055, 0.429, "Blue band = what the firm thinks it is worth.  Red dot = what it costs today.",
             fontsize=8.2, color=INK2, va="top")

    # ---- chart 3: drawdown context ----
    ax3 = fig.add_axes([0.28, 0.135, 0.665, 0.10])
    ks = list(DRAWDOWNS.keys())
    cols = [BLUE if k == t else CONTEXT for k in ks]
    ax3.bar(ks, [DRAWDOWNS[k] for k in ks], color=cols, width=0.55, zorder=3)
    for i, k in enumerate(ks):
        ax3.text(i, DRAWDOWNS[k]+1.2, f"−{DRAWDOWNS[k]:.0f}%", ha="center",
                 fontsize=9, weight="bold", color=INK if k==t else INK3)
    ax3.set_ylim(0, 52); ax3.set_ylabel("fall from high (%)", fontsize=8)
    ax3.set_axisbelow(True); ax3.yaxis.grid(True, color=GRID, lw=0.8)
    for s in ("top","right"): ax3.spines[s].set_visible(False)
    ax3.tick_params(axis="x", length=0, labelsize=9)
    fig.text(0.055, 0.263, "HOW FAR IT HAS FALLEN", fontsize=10, weight="bold", color=INK)
    fig.text(0.055, 0.249, f"{t} highlighted in blue; the other three names shown for context.",
             fontsize=8.2, color=INK2, va="top")

    fig.text(0.5, 0.055, "Research and decision support only — NOT financial advice. Nothing is executed unless the Owner places the trade.",
             fontsize=7.8, color=INK3, ha="center", style="italic")
    fig.text(0.5, 0.037, f"Page 1 of 2  ·  data as of {d['pdate']}  ·  皮褸黃 Capital internal use",
             fontsize=7, color=INK3, ha="center")
    pdf.savefig(fig); plt.close(fig)

def page2(pdf, t, d):
    fig = plt.figure(figsize=(8.27, 11.69))
    ax = fig.add_axes([0,0,1,1]); ax.axis("off")
    ax.add_patch(Rectangle((0, 0.955), 1, 0.045, color="#f4f3f0"))
    ax.text(0.055, 0.9775, f"{t} — what the AI agents found", fontsize=15,
            weight="bold", color=INK, va="center")
    ax.text(0.945, 0.9775, "Page 2 of 2", fontsize=8.5, color=INK3, va="center", ha="right")

    y = 0.925
    def section(title, items, bullet_col, y):
        ax.add_patch(Rectangle((0.055, y-0.004), 0.006, 0.018, color=bullet_col))
        ax.text(0.075, y+0.005, title, fontsize=10.5, weight="bold", color=INK, va="center")
        y -= 0.026
        for it in items:
            lines = textwrap.wrap(it, 100)
            ax.text(0.072, y, "•", fontsize=9, color=bullet_col, va="top", weight="bold")
            for j, line in enumerate(lines):
                ax.text(0.088, y - j*0.0158, line, fontsize=8.6, color=INK2, va="top")
            y -= len(lines)*0.0158 + 0.008
        return y - 0.016

    y = section("THE CASE FOR — what the agents found genuinely good", d["good"], BLUE, y)
    y = section("THE CASE AGAINST — why the firm is not buying", d["bad"], RED, y)
    y = section("WHAT WOULD CHANGE THE ANSWER — the tripwires to watch", d["watch"], INK3, y)

    # risk box
    ax.add_patch(FancyBboxPatch((0.055, y-0.062), 0.89, 0.058,
                 boxstyle="round,pad=0.006", facecolor="#f4f3f0", edgecolor=GRID))
    ax.text(0.072, y-0.014, "RISK OFFICER'S RULING (John, CRO — holds veto power)",
            fontsize=9, weight="bold", color=INK, va="top")
    yy = y - 0.031
    for line in textwrap.wrap(d["risk"], 96):
        ax.text(0.072, yy, line, fontsize=9, color=RED if "VETO" in d["risk"] else INK2,
                va="top", weight="bold"); yy -= 0.015
    y -= 0.082

    # audit box
    ax.add_patch(FancyBboxPatch((0.055, y-0.088), 0.89, 0.084,
                 boxstyle="round,pad=0.006", facecolor="#f4f3f0", edgecolor=GRID))
    ax.text(0.072, y-0.014, "QUALITY CONTROL — what the AI Auditor caught (Ai 管理層)",
            fontsize=9, weight="bold", color=INK, va="top")
    yy = y - 0.031
    for line in textwrap.wrap(d["audit"], 100):
        ax.text(0.072, yy, line, fontsize=8.4, color=INK2, va="top"); yy -= 0.0148

    ax.text(0.5, 0.055,
            "Research and decision support only — NOT financial advice. Markets cannot be reliably predicted.",
            fontsize=7.8, color=INK3, ha="center", style="italic")
    ax.text(0.5, 0.037,
            "No agent may place a trade. Nothing happens unless the Owner places it personally.",
            fontsize=7.8, color=INK3, ha="center", weight="bold")
    pdf.savefig(fig); plt.close(fig)

out = "/home/user/horse-monitor/reports/owner-summaries"
os.makedirs(out, exist_ok=True)
for t, d in STOCKS.items():
    path = f"{out}/{t}-summary-2026-07.pdf"
    with PdfPages(path) as pdf:
        page1(pdf, t, d); page2(pdf, t, d)
    print("wrote", path)
