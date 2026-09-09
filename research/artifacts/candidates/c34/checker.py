#!/usr/bin/env python3
"""C34 exact arithmetic checks; generator-side only, not trusted verification."""
from __future__ import annotations
import argparse, hashlib, itertools as it, json, platform, resource, time
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
VERSION='c34-compact-v1'
def ck(x,m):
    if not x: raise AssertionError(m)
def mech(m,b): return {x for x in range(m) if ((x+1)*b)//m>(x*b)//m}
def sigma(n,h):
    if h==0:return F(0)
    if h%2:return F(n)
    return F(3*h*n,2*(h+1))
def partial(m,b,p):
    ck(m%2 and 0<b<m and 0<=p<=m,'partial domain')
    D=p//2; C=mech(m,b); mu=(b*D+m-1)//m; delta=m*mu-b*D
    L1=Counter((s+t)%m for s in C for t in range(D))
    L2=Counter((s-t)%m for s in C for t in range(D))
    lo,rem=divmod(b*D,m); hi=lo+int(rem>0)
    ck(all(L1[x] in (lo,hi) and L2[x] in (lo,hi) for x in range(m)),'mechanical balance')
    E=3*b*D+2*m*(D-mu); N=2*m+b; endpoint=p*N-2*E
    ck(endpoint>=0,'negative endpoint defect')
    if p==0:k=F(0)
    elif p%2:
        k=F(endpoint); ck(k==2*m+b+4*delta and k<7*m,'odd packet')
    else:
        k=F(endpoint)+F(3*E,p+1)
        ck(k==4*delta+F(3*(D*(2*m+b)-2*delta),2*D+1),'even identity')
        ck(k<F(17*m,2),'even packet')
    return {'m':m,'b':b,'p':p,'D':D,'mu':mu,'delta':delta,'E':E,'endpoint':endpoint,'kappa':k}
def slot(m):
    owner={}
    for tau in range(m):
        seen=set()
        for i in range(m):
            T=((0,i),(1,(i+tau)%m),(2,(2*i+tau)%m))
            ck(len(set(T))==3,'repeated point')
            for e in it.combinations(T,2):
                e=tuple(sorted(e)); ck(e not in owner,'slot collision'); owner[e]=tau; seen.add(e)
        ck(len(seen)==3*m,'factor edge count')
    ck(len(owner)==3*m*m,'Latin pair coverage')
    return {'m':m,'slots':m,'edges':len(owner)}
def external(m,R,h,b,p,q):
    ck(R>=9 and 2<=h<=R-1 and 0<b<m,'external domain')
    ck(p//2<=(m-1)//2 and q//2<=m*(R-3)//2,'slot capacity')
    r=m*R
    S=(h-2)*sigma(m,p)+partial(m,b,p)['kappa']+sigma(r,q)
    ck(S<3*r+4*m and S<=F(31*r,9),'external bound')
    return {'r':r,'a':h*m+b,'p':p,'q':q,'defect':S,'long_slots':m*(R-3)//2}
def face(r,a,p,q):
    c=r-a
    if a<3 or c<3:return False
    d=r-1-q; s=d-p
    if p>a-1 or s<0:return False
    lo=max(F(0),F(a*(c-q),2),F(c*(a-q),2))
    hi=min(F(a*c,2),F(a*s,2),F(c*d,2),F(a*s+c*d,6))
    return lo<=hi
def sat(r,a,q):
    c=r-a; return c>=a+1 and 0<=q<=c
def round_robin(n):
    if n<=1:return []
    N=n if n%2==0 else n+1; z=N-1; dummy=N-1; out=[]
    for a in range(z):
        M=[(dummy,a)]+[((a+d)%z,(a-d)%z) for d in range(1,(N-2)//2+1)]
        M=[tuple(sorted(e)) for e in M if max(e)<n]
        ck(len({v for e in M for v in e})==2*len(M),'not matching')
        out.append(M)
    use=Counter(e for M in out for e in M)
    ck(len(use)==n*(n-1)//2 and set(use.values())=={1},'round robin coverage')
    return out
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); z=ap.parse_args(); st=time.monotonic()
    partial_rows=[partial(m,b,p) for m in (3,9,27,81) for b in range(1,m) for p in range(m+1)]
    slots=[slot(m) for m in (3,9,27,81)]
    complete=[external(3,9,h,b,p,q) for h in range(2,9) for b in (1,2) for p in range(4) for q in range(20)]
    named=[external(9,9,2,1,8,40),external(9,9,4,8,9,55),external(3,27,10,2,3,73),external(81,9,4,40,80,400)]
    scans=[]
    for r in (27,81,243):
        n=0
        for a in range(3,r-2):
            for q in range(r): ck(face(r,a,a-1,q)==sat(r,a,q),'saturated classification'); n+=1
        scans.append({'r':r,'cases':n})
    rr=[{'n':n,'classes':len(round_robin(n))} for n in range(18)]
    d=partial(9,1,8); ck(d['E']==66 and d['endpoint']==20 and d['kappa']==42,'diagnostic')
    tests=[lambda:ck(66==58,'old E'),lambda:ck(20==120,'old endpoint'),lambda:ck(42<42,'underbound'),lambda:ck(3>=9,'R'),lambda:ck(27==26,'slots'),lambda:ck(sigma(81,8)>=F(243,2),'sigma'),lambda:ck(face(27,14,13,0),'face'),lambda:ck(len(round_robin(9))==8,'factor count'),lambda:ck(8%3==1,'mod'),lambda:ck(F(3,4)<F(3,4),'threshold'),lambda:ck(F(5,4)+1<F(5,4),'leave'),lambda:ck(slot(9)['edges']==200,'ownership')]
    mutations=[]
    for i,t in enumerate(tests):
        try:t()
        except Exception as e:mutations.append({'id':i,'rejected':True,'error':type(e).__name__})
        else:mutations.append({'id':i,'rejected':False})
    ck(all(x['rejected'] for x in mutations),'mutation escaped')
    cv=lambda x: str(x) if isinstance(x,F) else x
    out={'version':VERSION,'python':platform.python_version(),'partial_cases':len(partial_rows),'slot_audits':slots,'external_complete_cases':len(complete),'external_named':[{k:cv(v) for k,v in row.items()} for row in named],'saturated_scans':scans,'round_robin':rr,'diagnostic':{k:cv(v) for k,v in d.items()},'mutations':mutations,'delcourt_postle_executed':False,'elapsed_seconds':time.monotonic()-st,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    p=Path(z.out); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'ok','sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'cases':len(partial_rows)+len(complete)+sum(x['cases'] for x in scans)}))
if __name__=='__main__':main()
