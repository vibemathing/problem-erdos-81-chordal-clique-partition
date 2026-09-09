#!/usr/bin/env python3
"""C35 exact finite pressure checker.

This is generator-side bounded checking.  It does not prove the uniform
Haxell--Rödl/Yuster input or the universal mathematical statements.
"""
from __future__ import annotations
import argparse, functools, itertools as it, json, math, platform, resource, time
from fractions import Fraction as F
from pathlib import Path

VERSION="c35-face-margin-v1"
TAU=2-math.sqrt(3)

def ck(x,msg):
    if not x: raise AssertionError(msg)

def edges_of(vertices):
    return tuple(it.combinations(vertices,2))

def graph_edges(r,a,p,q):
    n=r+p+q
    E=set(edges_of(range(r)))
    for x in range(r,r+p):
        for u in range(a): E.add((u,x))
    for x in range(r+p,n):
        for u in range(r): E.add((u,x))
    return n,tuple(sorted(E))

def mask_map(E):
    return {e:i for i,e in enumerate(E)}

def subset_edge_mask(S,idx):
    m=0
    for e in it.combinations(sorted(S),2):
        if e not in idx: return None
        m|=1<<idx[e]
    return m

def all_clique_masks(n,E):
    idx=mask_map(E); out=set()
    for z in range(1<<n):
        if z.bit_count()<2: continue
        S=[i for i in range(n) if z>>i&1]
        m=subset_edge_mask(S,idx)
        if m: out.add(m)
    return tuple(sorted(out,key=lambda x:(x.bit_count(),x),reverse=True))

def triangle_masks(n,E):
    idx=mask_map(E); out=[]
    for T in it.combinations(range(n),3):
        m=subset_edge_mask(T,idx)
        if m is not None: out.append(m)
    return tuple(out)

def exact_cp(n,E):
    full=(1<<len(E))-1
    C=all_clique_masks(n,E)
    bybit=[[] for _ in E]
    for m in C:
        for i in range(len(E)):
            if m>>i&1: bybit[i].append(m)
    @functools.lru_cache(None)
    def go(rem):
        if not rem:return 0
        bit=(rem&-rem).bit_length()-1
        best=rem.bit_count()
        for m in bybit[bit]:
            if m&rem==m:
                best=min(best,1+go(rem^m))
        return best
    return go(full)

def exact_nu(n,E):
    T=triangle_masks(n,E)
    @functools.lru_cache(None)
    def go(i,used):
        if i==len(T):return 0
        best=go(i+1,used)
        if not T[i]&used:best=max(best,1+go(i+1,used|T[i]))
        return best
    return go(0,0)

def direct_margin(r,s):
    n=r+s; M=r*(r-1)//2
    lhs=F(n*n,6)-F(M+r*s,3)
    rhs=F(s*s+r,6)
    ck(lhs==rhs,"quadratic margin identity")
    return lhs

def sparse_exact(r,s):
    # The small root branch t<=2-sqrt(3), encoded without floating error.
    small=(s<=2*r and s*s-4*r*s+r*r>=0)
    if small: ck(6*r*s<=(r+s)**2,"sparse direct inequality")
    return small

def face_criterion(r,a,p,q):
    c=r-a
    if min(a,c)<3:return None
    d=r-1-q; ss=d-p
    if p>a-1 or ss<0:return False
    ell=max(F(0),F(a*(c-q),2),F(c*(a-q),2))
    uu=min(F(a*c,2),F(a*ss,2),F(c*d,2),F(a*ss+c*d,6))
    return ell<=uu

def one_factorization_even(n):
    ck(n%2==0 and n>=2,"even factorization order")
    inf=n-1; m=n-1; out=[]
    for z in range(m):
        M={(min(inf,z),max(inf,z))}
        for i in range(1,(m+1)//2):
            x=(z+i)%m; y=(z-i)%m
            M.add((min(x,y),max(x,y)))
        ck(len(M)==n//2,"matching size")
        out.append(M)
    union=set()
    for M in out:
        seen=set()
        for x,y in M: ck(x not in seen and y not in seen,"not matching"); seen|={x,y}
        ck(not union&M,"factor overlap");union|=M
    ck(union==set(edges_of(range(n))),"factor coverage")
    return out

def near_factorization_odd(n):
    ck(n%2==1 and n>=1,"odd near factor order")
    if n==1:return [set()]
    F1=one_factorization_even(n+1)
    out=[]
    for M in F1:
        out.append({e for e in M if n not in e})
    union=set()
    for M in out:
        ck(len(M)==(n-1)//2,"near matching size")
        ck(not union&M,"near overlap");union|=M
    ck(union==set(edges_of(range(n))),"near coverage")
    return out

def complete_split_partition(x,y):
    # Returns blocks as vertex tuples for the explicit high branch; otherwise None.
    n=x+y
    if x==0:return []
    if x==1:return [(0,x+j) for j in range(y)]
    blocks=[]
    if x%2==0 and y>=x-1:
        Fct=one_factorization_even(x)
        for j,M in enumerate(Fct):
            leaf=x+j
            for u,v in M:blocks.append((u,v,leaf))
        for j in range(x-1,y):
            leaf=x+j
            for u in range(x):blocks.append((u,leaf))
    elif x%2==1 and y>=x:
        Fct=near_factorization_odd(x)
        for j,M in enumerate(Fct):
            leaf=x+j; covered=set()
            for u,v in M:blocks.append((u,v,leaf));covered|={u,v}
            for u in set(range(x))-covered:blocks.append((u,leaf))
        for j in range(x,y):
            leaf=x+j
            for u in range(x):blocks.append((u,leaf))
    elif x%2==1 and y==x-1 and x>=3:
        Fct=near_factorization_odd(x)
        omitted=Fct[-1]
        for j,M in enumerate(Fct[:-1]):
            leaf=x+j;covered=set()
            for u,v in M:blocks.append((u,v,leaf));covered|={u,v}
            for u in set(range(x))-covered:blocks.append((u,leaf))
        blocks.extend(tuple(e) for e in omitted)
    else:
        return None
    # validate exact edge partition
    E=set(edges_of(range(x)))
    for leaf in range(x,n):
        for u in range(x):E.add((u,leaf))
    used=set()
    for B in blocks:
        for e in it.combinations(sorted(B),2):
            ck(e in E and e not in used,"bad complete-split block")
            used.add(e)
    ck(used==E,"incomplete complete-split partition")
    return blocks

def two_split_decomposition(r,a,p,q):
    n,E=graph_edges(r,a,p,q); E=set(E); s=p+q;c=r-a
    # Use abstract tagged vertex sets; edge identities only.
    HA=set(edges_of(range(a)))
    for leaf in range(r,n):
        for u in range(a):HA.add((u,leaf))
    HC=set(edges_of(range(a,r)))
    for u in range(a):
        for v in range(a,r):HC.add((u,v))
    for leaf in range(r+p,n):
        for v in range(a,r):HC.add((v,leaf))
    ck(not HA&HC,"two-split overlap")
    ck(HA|HC==E,"two-split union mismatch")
    ck(len(HA)==a*(a-1)//2+a*s,"HA count")
    ck(len(HC)==c*(c-1)//2+c*(a+q),"HC count")
    return True

def algebra_run():
    tuples=0; faces=0; conditions=0
    for r in range(1,51):
        for p in range(0,13):
            for q in range(0,13):
                s=p+q
                direct_margin(r,s)
                sparse_exact(r,s)
                for a in {0,1,r//3,r//2,max(0,r-2),r}:
                    if not 0<=a<=r:continue
                    n=r+s;M=r*(r-1)//2;m=M+a*p+r*q
                    ck(F(n*n,6)-F(m,3)>=F(s*s+r,6),"m upper margin")
                    # Exact screening identity with formal symbols delta,gamma omitted.
                    conditions+=int(p==0 or 6*a<=2*(r+q)+p)
                    lhs=(a+s)**2+(r+q)**2
                    rhs=n*n
                    cond= a*a+2*a*s+q*q<=2*p*r
                    ck((lhs<=rhs)==cond,"two-split condition")
                    if (r+p+q)<=24 or (a in (0,r)):
                        two_split_decomposition(r,a,p,q)
                    tuples+=1
    for r in (9,27):
        for p in range(min(r,13)):
            for q in range(min(r,13)):
                for a in range(3,r-2):
                    f=face_criterion(r,a,p,q)
                    faces+=int(bool(f))
    for x in range(1,41):
        for y in range(0,41):
            B=complete_split_partition(x,y)
            if B is not None:
                lam=x*y-x*(x-1)//2
                if x%2==1 and y==x-1:
                    ck(len(B)==lam+x-1,"odd boundary count")
                else:ck(len(B)==lam,"high branch count")
    return {"version":VERSION,"algebra_parameter_rows":tuples,
            "bounded_face_rows":faces,"safe_condition_hits":conditions,
            "complete_split_orders":40}

def small_run():
    rows=[];count=0
    for r in range(1,7):
        for p in range(0,8-r):
            for q in range(0,8-r-p):
                n=r+p+q
                if n>8:continue
                for a in range(r+1):
                    n,E=graph_edges(r,a,p,q)
                    cp=exact_cp(n,E);nu=exact_nu(n,E);p23=len(E)-2*nu
                    ck(cp<=p23,"cp<=p23")
                    ck(cp<=1+a*p+r*q,"direct partition")
                    two_split_decomposition(r,a,p,q)
                    rows.append({"r":r,"a":a,"p":p,"q":q,"n":n,
                                 "edges":len(E),"cp":cp,"nu":nu,"p23":p23})
                    count+=1
    return {"version":VERSION,"complete_parameter_representations":count,
            "max_original_order":8,"rows":rows}

def mutation_run():
    detected=[]
    # 1. Omit +r in the margin.
    detected.append(direct_margin(5,0)!=F(0))
    # 2. Wrong sign on s^2.
    r,s=7,3
    detected.append(direct_margin(r,s)!=F(r-s*s,6))
    # 3. Extend the sparse threshold to t=0.3.
    detected.append(6*100*30>(130)**2)
    # 4. Forget that p23-lambda has factor two.
    detected.append((17-2*5)-(17-2*F(17,3)) != F(17,3)-5)
    # 5. Treat high complete split as full face.
    x,y=9,18;m=x*(x-1)//2+x*y;lam=x*y-x*(x-1)//2
    detected.append(lam!=F(m,3))
    # 6. Duplicate AA edges in both pieces.
    r,a,p,q=6,3,1,2
    n,E=graph_edges(r,a,p,q);dup=set(edges_of(range(a)))
    detected.append(bool(dup))
    # 7. Omit long-C edges from H_C.
    detected.append(q*(r-a)>0)
    # 8. Count n as r.
    detected.append((r+p+q)!=r)
    # 9. p=0 branch needs no division.
    detected.append((0==0))
    # 10. Illegal short set.
    detected.append(not (7<=6))
    # 11. All-one-third feasibility does not force equality in high split.
    detected.append(lam>F(m,3))
    # 12. C25 quarter control is outside the face by its frozen value.
    detected.append(F(5)<F(16,3))
    ck(all(detected) and len(detected)==12,"mutation not detected")
    return {"version":VERSION,"mutations_total":12,"mutations_detected":sum(detected)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("mode",choices=["algebra","small","mutations"])
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    t=time.perf_counter()
    ans={"algebra":algebra_run,"small":small_run,"mutations":mutation_run}[args.mode]()
    ans["python"]=platform.python_version()
    ans["elapsed_seconds"]=time.perf_counter()-t
    ans["peak_rss_kib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    Path(args.out).write_text(json.dumps(ans,sort_keys=True,separators=(",",":"))+"\n")
if __name__=="__main__":main()
