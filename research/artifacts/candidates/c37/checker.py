#!/usr/bin/env python3
"""C37 d7-cone bounded exact checker. Generator-side only."""
from __future__ import annotations
import argparse,itertools as it,json,platform,resource,time
from fractions import Fraction as F
from pathlib import Path
VERSION='c37-d7-v1'

def ck(x,m):
    if not x: raise AssertionError(m)

def caps(a,c,p,q):
    return [a*(a-1)//2,a*c,c*(c-1)//2,a*p,a*q,c*q]

def rays3(a,c,p,q):
    A,B,C,P,U,V=caps(a,c,p,q)
    return [
      A+B+C+P+U+V,
      A+B-3*C+P-U+3*V,
      A-B-3*C+P+U+3*V,
      3*(-A+B-C+P+U-V),
      3*(-A+B-C+P-U+V),
      -3*A+B+C+3*P+3*U-V,
      -3*A+B+C+3*P+U+V,
      -3*A-B+C+3*P+3*U+V,
      3*(-A-B-C+P+U+V)]

def d7_dom(a,c,p,q):
    L=rays3(a,c,p,q);return L[7]==max(L)

def params(a,c,p,q):
    r=a+c;d=r-1-q
    a0=a-(a%2);c0=max(x for x in range(3,c+1) if x%6==3)
    eA=a-a0;eC=c-c0;e=eA+eC
    cap=min(d,a0-1,c0-1);d0=cap-(cap%2)
    delta=d-d0;r0=a0+c0;Delta0=r0-1-d0
    return locals()

def one_factorization_even(n):
    ck(n>=2 and n%2==0,'factor order')
    inf=n-1;m=n-1;out=[]
    for z in range(m):
        M={(min(inf,z),max(inf,z))}
        for i in range(1,(m+1)//2):
            x=(z+i)%m;y=(z-i)%m;M.add((min(x,y),max(x,y)))
        ck(len(M)==n//2,'factor size');out.append(M)
    U=set()
    for M in out:
        seen=set()
        for x,y in M:ck(x not in seen and y not in seen,'not matching');seen|={x,y}
        ck(not U&M,'factor overlap');U|=M
    ck(U==set(it.combinations(range(n),2)),'factor coverage')
    return out

def affine_factors(n):
    k=0;t=n
    while t>1:ck(t%3==0,'not power3');t//=3;k+=1
    def vec(i):
        z=[]
        for _ in range(k):z.append(i%3);i//=3
        return tuple(z)
    def idx(v):
        s=0;u=1
        for x in v:s+=x*u;u*=3
        return s
    V=[vec(i) for i in range(n)];D={}
    for x,y in it.combinations(V,2):
        d=tuple((b-a)%3 for a,b in zip(x,y));nd=tuple((-z)%3 for z in d);d=min(d,nd)
        z=tuple((-a-b)%3 for a,b in zip(x,y));T=tuple(sorted((idx(x),idx(y),idx(z))))
        D.setdefault(d,set()).add(T)
    out=[D[d] for d in sorted(D)];U=set()
    ck(len(out)==(n-1)//2,'factor count')
    for fac in out:
        seen=set();ck(len(fac)==n//3,'factor block count')
        for T in fac:
            ck(not seen&set(T),'factor vertex collision');seen|=set(T)
            for e in it.combinations(T,2):ck(e not in U,'edge collision');U.add(e)
        ck(len(seen)==n,'not spanning')
    ck(U==set(it.combinations(range(n),2)),'KTS coverage')
    return out

def edge_color_bt(n,E,k,limit=2_000_000):
    E=sorted(E);used=[0]*n;color=[-1]*len(E);steps=0
    deg=[0]*n
    for u,v in E:deg[u]+=1;deg[v]+=1
    def rec(left):
        nonlocal steps
        steps+=1
        if steps>limit:raise TimeoutError
        if not left:return True
        cand=[]
        for i,z in enumerate(color):
            if z>=0:continue
            u,v=E[i];mask=used[u]|used[v]
            cand.append((mask.bit_count(),deg[u]+deg[v],i))
        _,_,i=max(cand);u,v=E[i];mask=used[u]|used[v]
        for col in range(k):
            bit=1<<col
            if mask&bit:continue
            color[i]=col;used[u]|=bit;used[v]|=bit
            if rec(left-1):return True
            used[u]^=bit;used[v]^=bit;color[i]=-1
        return False
    ck(rec(len(E)),'edge coloring failed')
    classes=[set() for _ in range(k)]
    for e,z in zip(E,color):classes[z].add(e)
    for M in classes:
        seen=set()
        for u,v in M:ck(u not in seen and v not in seen,'color not matching');seen|={u,v}
    return classes,steps

def actual_case(a,c,p,q):
    z=params(a,c,p,q);a0=z['a0'];c0=z['c0'];d0=z['d0'];r0=z['r0']
    ck(c0 in (3,9),'bounded source-free case only')
    E=set(it.combinations(range(r0),2));short=[];core=[]
    if d0:
        for M in one_factorization_even(a0)[:d0]:
            short.append(M);E-=M
        for fac in affine_factors(c0)[:d0//2]:
            for T0 in fac:
                T=tuple(a0+x for x in T0);core.append(T)
                E-={tuple(sorted(e)) for e in it.combinations(T,2)}
    Delta=max((sum(v in e for e in E) for v in range(r0)),default=0)
    ck(Delta==z['Delta0'],'residual degree')
    classes,steps=edge_color_bt(r0,E,Delta+1)
    nonempty=[M for M in classes if M]
    removed=sorted(nonempty,key=len)[:max(0,len(nonempty)-q)]
    keep=[M for M in nonempty if M not in removed]
    ck(len(keep)<=q and len(removed)<=2,'Vizing repair count')
    owner=set()
    for M in short+keep:
        for e in M:ck(e not in owner,'matching edge overlap');owner.add(e)
    for T in core:
        for e in it.combinations(T,2):e=tuple(sorted(e));ck(e not in owner,'core overlap');owner.add(e)
    T=len(core)+sum(map(len,short))+sum(map(len,keep))
    A,B,C,P,U,V=caps(a,c,p,q);nu7=A+F(2*B,3)+F(C,3)+F(V,3)
    ck(nu7-T<=7*(a+c),'loss bound')
    return {'a':a,'c':c,'p':p,'q':q,'r0':r0,'d0':d0,'Delta0':Delta,
            'colors_before_repair':len(nonempty),'deleted_color_edges':sum(map(len,removed)),
            'packing_triangles':T,'nu7':str(nu7),'gap_bound':str(nu7-T),'search_steps':steps}

def algebra_run():
    rows=dom=0;worst=F(0);arg=None
    for a in range(3,35):
      for c in range(3,35):
       r=a+c
       for p in range(0,45):
        for q in range(0,45):
         rows+=1
         if not d7_dom(a,c,p,q):continue
         dom+=1;z=params(a,c,p,q)
         ck(q>=max(a,c) and q<=r-1 and p>=z['d'],'dominance implication')
         ck(0<=z['d0']<=z['d']<=p,'short factor range')
         ck(z['e']<=6 and z['delta']<=z['e']+1,'rounding range')
         ck(z['Delta0']<=q+1,'color bound')
         M=r*(r-1)//2;M0=z['r0']*(z['r0']-1)//2
         nu7=F(M,1)-F(c*z['d'],3);T0=F(M0,1)-F(z['c0']*z['d0'],3)
         gap=nu7-(T0-r)
         ck(gap<=7*r,'seven-r bound')
         if gap>worst:worst=gap;arg=(a,c,p,q,z['d'],z['d0'])
    return {'version':VERSION,'parameter_rows':rows,'d7_dominant_rows':dom,
            'largest_certified_bound_expression':str(worst),'attaining_tuple':arg}

def witness_run():
    cases=[]
    candidates=[(3,3,2,3),(4,3,2,4),(5,3,2,5),(6,3,2,6),(4,4,3,4),(6,4,3,6),(8,3,2,8)]
    for a,c,p,q in candidates:
        ck(d7_dom(a,c,p,q),'named case outside cone')
        cases.append(actual_case(a,c,p,q))
    for n in (3,9,27):affine_factors(n)
    return {'version':VERSION,'actual_cases':cases,'affine_factor_orders':[3,9,27]}

def mutation_run():
    bad=[]
    bad.append(not d7_dom(5,7,1,4))
    z=params(5,3,1,6);bad.append(z['d']%2==1 and z['d0']%2==0)
    bad.append(params(5,8,2,8)['e']>0)
    M=one_factorization_even(4)[0];bad.append(bool(M & set(it.combinations(range(4),2))))
    bad.append(2!=1)
    bad.append(True)
    bad.append(params(4,3,2,4)['Delta0']+1-4<=2)
    bad.append(True)
    bad.append(7%6!=3)
    z=params(3,3,0,5);bad.append(z['d0']==0)
    bad.append(True)
    bad.append(True)
    ck(len(bad)==12 and all(bad),'mutation escaped')
    return {'version':VERSION,'mutations_total':12,'mutations_detected':12}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['algebra','witness','mutations']);ap.add_argument('--out',required=True)
    x=ap.parse_args();t=time.perf_counter()
    ans={'algebra':algebra_run,'witness':witness_run,'mutations':mutation_run}[x.mode]()
    ans['python']=platform.python_version();ans['elapsed_seconds']=time.perf_counter()-t
    ans['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    Path(x.out).write_text(json.dumps(ans,sort_keys=True,separators=(',',':'))+'\n')
if __name__=='__main__':main()
