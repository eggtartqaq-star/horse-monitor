# -*- coding: utf-8 -*-
"""
記錄簿驗證(離線,用 data/ 嘅 CSV):
  1. 逐日跑 daily_scan_v66(2025-03-03 → 2025-05-30)寫入臨時記錄簿
  2. 再跑一次 → 行數唔變(冪等)
  3. resolve 嘅結果 == lab.simulate 用同一批訊號(逐筆:代號/日期/出場原因/出場價)
  4. 2倉書 == AS_TRADED;fill 指令會標記違規
"""
import sys, os, shutil, io, contextlib, pandas as pd
V=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,V); os.chdir(V)
import daily_scan_v66 as D, ledger_v66 as L, lab, rules_v642 as R
from dataclasses import replace
import tempfile; T=tempfile.mkdtemp()
data=lab.load_csv('data', R.TICKERS+['SPY'])
days=[d for d in data['SPY'].index if pd.Timestamp('2025-03-03')<=d<=pd.Timestamp('2025-05-30')]
for d in days:
    with contextlib.redirect_stdout(io.StringIO()):
        D.scan('csv','data',str(d.date()),T,False,quiet=True)
FAIL=[]  # Tom 2026-11-24:以前只係 print,永遠 exit 0;而家任何一項唔啱就 exit 1
s=L.read(T,'signals.csv',L.SIGNAL_COLS); print('signals logged',len(s), s.path.value_counts().to_dict())
if len(s)==0: FAIL.append('no signals logged')
# idempotence
with contextlib.redirect_stdout(io.StringIO()):
    D.scan('csv','data',str(days[-1].date()),T,False,quiet=True)
n2=len(L.read(T,'signals.csv',L.SIGNAL_COLS)); print('after rerun',n2)
if n2!=len(s): FAIL.append('rerun changed row count')
# resolve
class A: source='csv'; data='data'; include_asof=False
# CRO C-3r:預設 resolve 唔計歷史重跑行(days_er=off)—— 呢個測試記錄簿全部係歷史重跑,所以應該得返 None
with contextlib.redirect_stdout(io.StringIO()):
    res0=L.cmd_resolve(A,T)
print('default resolve excludes as-of rows', res0 is None)
if res0 is not None: FAIL.append('resolve counted as-of rows')
A.include_asof=True     # 測試專用:明確要求計歷史重跑行,先可以同 lab 逐筆比較
with contextlib.redirect_stdout(io.StringIO()):
    res=L.cmd_resolve(A,T)
# reference: lab precompute with signals restricted to logged dates
sig,_=lab.precompute(data)
lo,hi=days[0],days[-1]
for tk,df in sig.items():
    df['sig']=[e if lo<=d<=hi else {'route':'SKIP'} for d,e in zip(df.index,df['sig'])]
for path,cfg in (('bt',lab.AS_TRADED),('scan',lab.SCANNER)):
    ref,_,_=lab.simulate(sig, replace(lab.PER_TRADE,e2_breakout_gate=cfg.e2_breakout_gate,e1_strong_only=cfg.e1_strong_only), start=lo)
    ref=ref.copy(); ref['reason']=ref['reason'].replace({'數據結束':'持倉中'})
    got=res[(res.path==path)&(res['mode']=='per_trade')]
    k=lambda t:sorted(zip(t.ticker,pd.to_datetime(t.sig_date).dt.strftime('%Y-%m-%d'),pd.to_datetime(t.exit_date).dt.strftime('%Y-%m-%d'),t.reason,t['exit'].astype(float).round(4)))
    a,b=k(ref),k(got)
    print(path,'ref',len(a),'resolve',len(b),'IDENTICAL' if a==b else 'DIFF')
    if a!=b or not a: FAIL.append(f'resolve per_trade {path}')
    if a!=b:
        print(' only ref',[x for x in a if x not in b][:5]); print(' only res',[x for x in b if x not in a][:5])
# book_2slot vs AS_TRADED (bt path only, signals restricted)
ref,_,_=lab.simulate(sig, lab.AS_TRADED, start=lo)
ref=ref.copy(); ref['reason']=ref['reason'].replace({'數據結束':'持倉中'})
got=res[(res.path=='bt')&(res['mode']=='book_2slot')]
print('book bt ref',len(ref),'resolve',len(got),'IDENTICAL' if k(ref)==k(got) else 'DIFF')
if k(ref)!=k(got) or not len(ref): FAIL.append('book_2slot')
# fills + review with synthetic breaches
import types
def F(**kw):
    base=dict(date=None,fees=0.0,reason=None,target=None); base.update(kw); a=types.SimpleNamespace(**base)
    with contextlib.redirect_stdout(io.StringIO()) as o: L.cmd_fill(a,T)
    return o.getvalue()
print(F(action='open',ticker='WMT',price=90.0,shares=1,stop=86.0,engine='E2',date='2025-05-20').strip())
print(F(action='open',ticker='COST',price=900.0,shares=1,stop=890.0,engine='E1',date='2025-05-21').strip())
print(F(action='close',ticker='COST',price=850.0,date='2025-05-28').strip())
out=None
with contextlib.redirect_stdout(io.StringIO()) as o: out=L.review(T, today='2025-06-02')
print('breaches',out['breaches']); print('notes',out['notes'])
if not any('COST' in b and '超上限' in b for b in out['breaches']): FAIL.append('S2 over-cap fill not flagged')
print('LEDGER CHECK', 'PASS' if not FAIL else f'FAIL {FAIL}')
shutil.rmtree(T, ignore_errors=True)   # CRO N-17:唔好留低臨時資料夾
sys.exit(1 if FAIL else 0)
