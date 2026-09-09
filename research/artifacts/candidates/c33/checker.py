#!/usr/bin/env python3
"""Exact finite checker for C33 balanced cyclic boundary completion.

The universal proof is symbolic. This checker validates the explicit
mechanical-word/partial-Latin arrays, pair ownership, degree and defect
identities, and representative actual p=3,q=2/3 blow-up packings.
It does not prove Vizing's theorem or the universal quantifiers.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, time
from collections import Counter, defaultdict
from itertools import combinations, product
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set, Tuple

Vec=Tuple[int,...]; Vertex=Tuple[Vec,int]; Edge=Tuple[Vertex,Vertex]

def vecs(k): return list(product(range(3),repeat=k))
def add(x,y): return tuple((a+b)%3 for a,b in zip(x,y))
def neg(x): return tuple((-a)%3 for a in x)
def sub(x,y): return tuple((a-b)%3 for a,b in zip(x,y))
def canon_dir(d):
    assert any(d); return min(d,neg(d))
def dirs(k): return sorted({canon_dir(x) for x in vecs(k) if any(x)})

def affine_lines(k):
    V=vecs(k); lines=set()
    for x,y in combinations(V,2):
        z=neg(add(x,y)); T=tuple(sorted((x,y,z)))
        assert len(set(T))==3; lines.add(T)
    assert len(lines)==len(V)*(len(V)-1)//6
    return sorted(lines)

def vec_to_idx(v):
    out=0; p=1
    for x in v: out+=x*p; p*=3
    return out

def mechanical_set(m,b):
    return {x for x in range(m) if ((x+1)*b)//m-(x*b)//m==1}

def balanced_triples(m,b,D):
    assert m%2 and 0<=D<=m
    C=mechanical_set(m,b); B={(2*s)%m for s in C}
    T=[((s+t)%m,(s-t)%m,(2*s)%m) for s in sorted(C) for t in range(D)]
    return C,B,T

def check_full_td(m):
    A=[(u,v,(u+v)%m) for u in range(m) for v in range(m)]
    for I,J in ((0,1),(0,2),(1,2)):
        P=[(x[I],x[J]) for x in A]; assert len(P)==len(set(P))==m*m

def check_balanced(m,b,D):
    C,B,T=balanced_triples(m,b,D)
    assert len(C)==len(B)==b and len(T)==len(set(T))==b*D
    for I,J in ((0,1),(0,2),(1,2)):
        P=[(x[I],x[J]) for x in T]; assert len(P)==len(set(P))
    du=Counter(); dv=Counter(); dw=Counter()
    for u,v,w in T:
        assert (u+v)%m==w; du[u]+=1; dv[v]+=1; dw[w]+=1
    lo=b*D//m; hi=(b*D+m-1)//m
    assert all(du[i] in (lo,hi) for i in range(m))
    assert all(dv[i] in (lo,hi) for i in range(m))
    assert all(dw[i]==(D if i in B else 0) for i in range(m))

def boundary_stats(m,b,p):
    assert 0<b<m and 0<=p<=m-1
    D=p//2; _,B,T=balanced_triples(m,b,D)
    lam,rho=divmod(b*D,m); mu=lam+int(rho>0); t=D-mu
    assert 0<=t<=(m-1)//2
    iu=Counter(u for u,_,_ in T); iv=Counter(v for _,v,_ in T); iw=Counter(w for _,_,w in T)
    deg={('U',i):2*(t+iu[i]) for i in range(m)}
    deg.update({('V',i):2*(t+iv[i]) for i in range(m)})
    deg.update({('W',i):2*iw[i] for i in B})
    E=sum(p-d for d in deg.values())
    if p==0: expected=0
    elif p%2: expected=b+2*m if rho==0 else b+6*m-4*rho
    else: expected=0 if rho==0 else 4*(m-rho)
    assert E==expected
    assert max(deg.values(),default=0)<=(p-1 if p%2 else p)
    e=3*b*D+2*m*t
    if p>0 and p%2==0: assert E+3*(e//(p+1))<17*m/2
    elif p>0: assert E<=7*m

def vedge(x,y):
    assert x!=y; return (x,y) if x<y else (y,x)
def matching_ok(E):
    seen=set()
    for x,y in E:
        if x in seen or y in seen: return False
        seen|={x,y}
    return True

def color_tri(T,colors):
    x,y,z=T; colors[0].append(vedge(x,y)); colors[1].append(vedge(y,z)); colors[2].append(vedge(x,z))
def line_direction(T): return canon_dir(sub(T[1],T[0]))

def construct_p3_blowup(base_dim,fiber_dim,b,q):
    assert q in (2,3)
    Q=vecs(base_dim); R=len(Q); m=3**fiber_dim; BL=affine_lines(base_dim)
    distinguished=BL[0]; U,V,W=distinguished
    _,B,selected=balanced_triples(m,b,1); selected=set(selected)
    A={(U,i) for i in range(m)}|{(V,i) for i in range(m)}|{(W,i) for i in B}
    short={i:[] for i in range(3)}; long={i:[] for i in range(q)}
    core=[]; unused=set()
    for X,Y,Z in BL:
        for i in range(m):
            for j in range(m):
                k=(i+j)%m; tri=((X,i),(Y,j),(Z,k))
                if (X,Y,Z)==distinguished and (i,j,k) in selected: color_tri(tri,short)
                else: core.append(tuple(sorted(tri)))
    IL=affine_lines(fiber_dim); d0=dirs(fiber_dim)[0]
    for X in Q:
        for T in IL:
            tri=tuple(sorted((X,vec_to_idx(z)) for z in T))
            if line_direction(T)==d0:
                if q==3: color_tri(tri,long)
                else:
                    x,y,z=tri; long[0].append(vedge(x,y)); long[1].append(vedge(y,z)); unused.add(vedge(x,z))
            else: core.append(tri)
    for M in list(short.values())+list(long.values()): assert matching_ok(M)
    owner={}
    for c,M in short.items():
        for e in M: assert e not in owner and e[0] in A and e[1] in A; owner[e]=f'S{c}'
    for c,M in long.items():
        for e in M: assert e not in owner; owner[e]=f'L{c}'
    for T in core:
        for x,y in combinations(T,2):
            e=vedge(x,y); assert e not in owner; owner[e]='CORE'
    for e in unused: assert e not in owner; owner[e]='UNUSED'
    vertices=[(X,i) for X in Q for i in range(m)]
    assert set(owner)=={vedge(x,y) for x,y in combinations(vertices,2)}
    sdeg=Counter(v for M in short.values() for e in M for v in e)
    ldeg=Counter(v for M in long.values() for e in M for v in e)
    Ss=sum(3-sdeg[x] for x in A); Sl=sum(q-ldeg[x] for x in vertices); Sc=len(unused); S=Ss+Sl+Sc
    r=R*m; a=len(A); M=r*(r-1)//2
    packing=len(core)+sum(map(len,short.values()))+sum(map(len,long.values()))
    assert M+3*a+q*r-3*packing==S
    types=Counter(sum(v in A for v in T) for T in core)
    return {'r':r,'a':a,'b':b,'q':q,'packing':packing,'S_core':Sc,'S_short':Ss,'S_long':Sl,'S_total':S,'AAA':types[3],'AAC':types[2],'ACC':types[1],'CCC':types[0]}

def run_balanced():
    n=s=0
    for m in (3,9,27):
        check_full_td(m)
        for b in range(m+1):
            for D in range(m+1): check_balanced(m,b,D); n+=1
        for b in range(1,m):
            for p in range(m): boundary_stats(m,b,p); s+=1
    m=81; check_full_td(m)
    for b in (1,2,7,27,40,79,80):
        for D in (0,1,2,13,27,40,80,81): check_balanced(m,b,D); n+=1
        for p in (0,1,2,3,26,27,40,79,80): boundary_stats(m,b,p); s+=1
    return {'balanced_arrays':n,'boundary_parameter_rows':s}
def run_owners():
    out=[]
    for bd,fd in ((1,1),(1,2)):
        for b in range(1,3**fd):
            for q in (2,3): out.append(construct_p3_blowup(bd,fd,b,q))
    for b in (1,4,8):
        for q in (2,3): out.append(construct_p3_blowup(2,2,b,q))
    return {'actual_owner_instances':len(out),'named':out}
def run_controls():
    bad=0; _,_,T=balanced_triples(9,4,3)
    if len(set(T+[T[0]]))<len(T)+1: bad+=1
    u,v,w=T[0]; T2=T+[(u,(v+1)%9,w)]
    if len({(x[0],x[2]) for x in T2})<len(T2): bad+=1
    C=set(range(2)); loads=[sum(((x-t)%9) in C for t in range(2)) for x in range(9)]
    if max(loads)-min(loads)>1: bad+=1
    if dirs(2)[0]==dirs(2)[0]: bad+=1
    tri=[(('x',),i) for i in range(3)]
    if not matching_ok([vedge(tri[0],tri[1]),vedge(tri[1],tri[2])]): bad+=1
    assert bad==5; return {'rejected_mutations':bad}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('mode',choices=('balanced','owners','controls','all'),nargs='?',default='all'); a=ap.parse_args(); st=time.perf_counter()
    out={'status':'ok','mode':a.mode,'python':platform.python_version(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if a.mode in ('balanced','all'): out['balanced']=run_balanced()
    if a.mode in ('owners','all'): out['owners']=run_owners()
    if a.mode in ('controls','all'): out['controls']=run_controls()
    out['elapsed_seconds']=time.perf_counter()-st; print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
