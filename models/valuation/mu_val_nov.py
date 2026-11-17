# MU valuation refresh 2026-11-17 -- 𢦀鳩仔. All inputs are stated assumptions (see report §3).
SH = 1.13          # bn shares (Webull mkt value / price, derived)
NETCASH = 38.0     # $bn own net cash = 68.3 reported - ~30.3 refundable cash deposits (derived)
TAX = 0.155        # FQ1 FY27 guide
# discount timing from 17 Nov 2026; FY ends ~early Sep
T = {'FY27':0.40,'FY28':1.30,'FY29':2.30,'FY30':3.30,'FY31':4.30}
T_TV = 4.80

SCEN = {
 # rev, GM, opex, D&A, capex per FY ($bn); normalised = FY31 values; g, RONIC for terminal
 'bear': dict(rev=[200,90,55,62,75], gm=[.80,.30,.12,.28,.35], opex=[7,9,10,10.5,11],
              da=[14,19,22,23,23], capex=[55,35,20,22,23], g=.035, ronic=.10),
 'base': dict(rev=[240,150,85,92,100], gm=[.85,.55,.36,.40,.42], opex=[7,9,10.5,11.5,12.5],
              da=[14,19,23,25,26], capex=[55,50,30,27,26], g=.04, ronic=.15),
 'bull': dict(rev=[275,230,160,155,160], gm=[.87,.75,.55,.49,.47], opex=[7.5,10,12,14,16],
              da=[14,20,25,28,30], capex=[55,60,45,35,30], g=.05, ronic=.20),
}
YRS = ['FY27','FY28','FY29','FY30','FY31']

def nopat(rev,gm,opex):
    ebit = rev*gm - opex
    return ebit*(1-TAX) if ebit>0 else ebit   # no tax shield on losses (conservative-neutral)

def value(s, r, gm_norm=None, rev_norm=None, verbose=False, netcash=NETCASH):
    sc = dict(s); sc['gm']=list(s['gm']); sc['rev']=list(s['rev'])
    if gm_norm is not None: sc['gm'][-1]=gm_norm
    if rev_norm is not None: sc['rev'][-1]=rev_norm
    pv=0; rows=[]
    for i,y in enumerate(YRS):
        n = nopat(sc['rev'][i],sc['gm'][i],sc['opex'][i])
        if i < 4:
            fcf = n + sc['da'][i] - sc['capex'][i]
        else:
            fcf = n*(1 - sc['g']/sc['ronic'])   # terminal-year FCF on value-driver basis
        pv += fcf/(1+r)**T[y]; rows.append((y,sc['rev'][i],sc['gm'][i],n,fcf))
    n_norm = nopat(sc['rev'][-1],sc['gm'][-1],sc['opex'][-1])
    tv = n_norm*(1+sc['g'])*(1-sc['g']/sc['ronic'])/(r-sc['g'])
    pvtv = tv/(1+r)**T_TV
    eq = pv+pvtv+netcash
    if verbose:
        for y,rv,g,n,f in rows: print(f"  {y}: rev ${rv}bn GM {g:.0%} NOPAT ${n:.1f}bn FCF ${f:.1f}bn")
        print(f"  normalised NOPAT ${n_norm:.1f}bn = EPS ${n_norm/SH:.1f}; PV explicit ${pv:.0f}bn; TV ${tv:.0f}bn PV(TV) ${pvtv:.0f}bn ({pvtv/(pv+pvtv):.0%} of EV); net cash ${netcash}bn")
        print(f"  equity ${eq:.0f}bn -> ${eq/SH:.0f}/share")
    return eq/SH, n_norm/SH, pv, pvtv

R=0.12
P = {'bear':.25,'base':.50,'bull':.25}
print("=== SCENARIOS @ r=12% ===")
V={}
for k in ['bear','base','bull']:
    print(k.upper()); V[k]=value(SCEN[k],R,verbose=True)
pw = sum(P[k]*V[k][0] for k in P)
print(f"PROB-WEIGHTED FV: ${pw:.0f}  (0.25*{V['bear'][0]:.0f} + 0.50*{V['base'][0]:.0f} + 0.25*{V['bull'][0]:.0f})")

print("\n=== Discount-rate sensitivity of PW FV ===")
for r in [0.10,0.11,0.12,0.13,0.14]:
    print(f" r={r:.0%}: bear {value(SCEN['bear'],r)[0]:.0f} base {value(SCEN['base'],r)[0]:.0f} bull {value(SCEN['bull'],r)[0]:.0f} PW {sum(P[k]*value(SCEN[k],r)[0] for k in P):.0f}")

print("\n=== BASE: normalised GM x discount rate ($/sh) ===")
for gm in [.35,.38,.42,.44,.47]:
    print(f" GM {gm:.0%}: " + "  ".join(f"{value(SCEN['base'],r,gm_norm=gm)[0]:.0f}" for r in [.10,.11,.12,.13,.14]))
print("\n=== BASE: normalised revenue x discount rate ($/sh) ===")
for rv in [75,85,100,120,140]:
    print(f" rev {rv}: " + "  ".join(f"{value(SCEN['base'],r,rev_norm=rv)[0]:.0f}" for r in [.10,.11,.12,.13,.14]))

# July-method comparable: r=11%, terminal FCF = NOPAT (no reinvestment)
print("\n=== Bridge items ===")
b=SCEN['base']
def val_julymethod(s,r):
    s2=dict(s); s2['ronic']=1e9
    return value(s2,r)[0]
print(f" base @12% value-driver TV: {value(b,.12)[0]:.0f}; @12% July TV method (no reinvestment): {val_julymethod(b,.12):.0f}; @11% July method: {val_julymethod(b,.11):.0f}; @11% value-driver: {value(b,.11)[0]:.0f}")

# Peak-not-yet variant: earnings peak in FY28 instead of FY27
late = dict(SCEN['base']); late['rev']=[255,260,150,100,100]; late['gm']=[.86,.80,.50,.42,.42]
late['opex']=[7,9.5,11,12,12.5]; late['da']=[14,20,24,26,26]; late['capex']=[55,60,35,27,26]
print("\n=== LATE-PEAK variant (peak FY28, then base normalisation) ===")
value(late,R,verbose=True)

# Reverse DCF at $700 and $719: required normalised NOPAT holding base harvest FY27-30
import math
def solve_norm(price, s, r):
    lo,hi=0,400
    for _ in range(100):
        mid=(lo+hi)/2
        s2=dict(s); s2['rev']=list(s['rev']); s2['gm']=list(s['gm']); s2['opex']=list(s['opex'])
        # set FY31 NOPAT = mid via revenue at fixed GM/opex
        s2['rev'][-1]=(mid/(1-TAX)+s2['opex'][-1])/s2['gm'][-1]
        v=value(s2,r)[0]
        if v<price: lo=mid
        else: hi=mid
    return mid
print("\n=== REVERSE DCF ===")
for price in [656.39,700,719.02]:
    for r in [.11,.12]:
        n=solve_norm(price,SCEN['base'],r)
        print(f" price ${price}: r={r:.0%} -> required normalised NOPAT ${n:.0f}bn = EPS ${n/SH:.0f} (vs base ${V['base'][1]:.1f})")
    nl=solve_norm(price,late,R)
    print(f"   with LATE-PEAK harvest @12%: required normalised NOPAT ${nl:.0f}bn = EPS ${nl/SH:.0f}")
for price in [1550,1561.91]:
    n=solve_norm(price,SCEN['base'],R); nl=solve_norm(price,late,R)
    print(f" consensus ${price}: base harvest -> norm EPS ${n/SH:.0f}; late-peak harvest -> ${nl/SH:.0f}")
