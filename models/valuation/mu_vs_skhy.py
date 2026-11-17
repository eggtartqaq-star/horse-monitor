from math import log, sqrt, exp, erf
Phi=lambda x:0.5*(1+erf(x/sqrt(2)))
P=697.83
PW,BASE,BEAR,BULL,LATE=351,314,168,606,424
print("MU MoS at $697.83 and $719.02:")
for lab,fv in [('PW',PW),('base',BASE),('bear',BEAR),('bull',BULL),('late-peak base',LATE),('PW late-peak replaces base',405)]:
    print(f"  {lab} ${fv}: {(fv-697.83)/fv:+.0%} / {(fv-719.02)/fv:+.0%}")
print("Entry levels: PW", [round(PW*x) for x in (1,.75,.6)], " base", [round(BASE*x) for x in (1,.75,.6)], " range low/high 300/425:",[round(300*.6),round(425*.6)])
# expected annual return (assumption: price converges to FV in N yrs, FV compounds at r)
def irr(fv,p,r,N): return (1+r)*(fv/p)**(1/N)-1
print("MU expected annual return from $700 (r=12%):")
for lab,fv in [('PW',PW),('bear',BEAR),('base',BASE),('bull',BULL)]:
    print(f"  {lab}: " + "  ".join(f"N={N}:{irr(fv,700,.12,N):+.1%}" for N in (1,3,5)))
print("SKHY ADS $121.03 (ke 11%):")
for lab,fv in [('PW blended',102.40),('parity@1330',107000/1330),('premium-incl ×1.40',112),('(c)×1.40',150.7)]:
    print(f"  {lab} ${fv:.2f}: MoS {(fv-121.03)/fv:+.1%}; N=3 IRR {irr(fv,121.03,.11,3):+.1%}")
# implied ordinary from ADS at measured premium band
for prem in (1.43,1.47,1.52):
    print(f"  implied ordinary at premium {prem-1:.0%}, FX 1330: ₩{121.03*1330*10/prem:,.0f}")
for o in (1059000,1125700,1175000,1212000):
    print(f"  ordinary ₩{o:,}: vs FV ₩1,070,000 MoS {(1.07e6-o)/1.07e6:+.1%}; N=3 IRR {irr(1.07e6,o,.11,3):+.1%}")
# Webull SKHY P/E check
eps_ads=13.67
print(f"SKHY Webull EPS 13.67/ADS -> ordinary EPS ₩{eps_ads*10*1330:,.0f}; x700M = ₩{eps_ads*10*1330*700e6/1e12:.0f}tn; 3-quarter on-disk NI sum 1Q-3Q26 = ₩{40.35+93.92+39.78:.2f}tn")
print(f"  parity-equivalent P/E = 8.85/1.43..1.52 = {8.85/1.52:.1f}-{8.85/1.43:.1f}x")
# normalised multiples
sk_nopat_usd = 65*0.75/1.33   # ₩tn -> $bn
mu_nopat=24.9
print(f"SK hynix mid-cycle NOPAT ${sk_nopat_usd:.1f}bn; MU base ${mu_nopat}bn")
for o in (1059000,1125700,1175000,1212000):
    mc=o*700e6/1330/1e9
    print(f"  SK ordinary ₩{o:,}: mkt cap ${mc:.0f}bn -> {mc/sk_nopat_usd:.1f}x mid-cycle NOPAT; ADS-implied (×1.43-1.52) {mc*1.43/sk_nopat_usd:.1f}-{mc*1.52/sk_nopat_usd:.1f}x")
mumc=697.83*1.13
print(f"  MU mkt cap ${mumc:.0f}bn -> {mumc/mu_nopat:.1f}x base normalised NOPAT; P/E on base norm EPS {697.83/22.1:.1f}x; on FY27 cons 176.5 {697.83/176.5:.2f}x; on 178.93 {697.83/178.93:.2f}x; on my base FY27 EPS {166.5/1.13:.0f} -> {697.83/(166.5/1.13):.2f}x")
# MU normalisation ratio consistency with SK hynix (24% of peak-year)
cy26_ebit = (23.86*.744-1.4)+33.7+(54.23*.87-1.6)+(61.5*.8625-1.7)
fy26_ebit = (13.64*.56-1.3)+(23.86*.744-1.4)+33.7+(54.23*.87-1.6)
print(f"MU CY26-equiv EBIT ~${cy26_ebit:.0f}bn (derived) -> 24% = ${cy26_ebit*.24:.0f}bn EBIT -> EPS ${cy26_ebit*.24*.845/1.13:.1f}; FY26 EBIT ~${fy26_ebit:.0f}bn -> 24% EPS ${fy26_ebit*.24*.845/1.13:.1f}; base norm NOPAT/CY26 NOPAT = {24.9/(cy26_ebit*.845):.0%}")
print(f"SK hynix: 65/268.8 = {65/268.8:.0%}")
# peak multiple view
for m in (3,4,5,6,9):
    print(f"  FY27 cons $176.5 x {m} = ${176.5*m:.0f}")
# touch probabilities, zero expected price change (log drift -s^2/2)
def touch(S,B,s,T):
    mu=-0.5*s*s; b=log(B/S)
    return Phi((b-mu*T)/(s*sqrt(T)))+exp(2*mu*b/(s*s))*Phi((b+mu*T)/(s*sqrt(T)))
print("MU touch probabilities from $697.83 (zero expected change):")
for B in (600,351,263,211):
    print(f"  ${B}: " + "  ".join(f"{T*12:.0f}m@{int(s*100)}%:{touch(697.83,B,s,T):.0%}" for T in (0.25,0.5) for s in (0.72,1.03)))
