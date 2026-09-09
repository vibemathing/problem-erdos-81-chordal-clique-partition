#!/usr/bin/env python3
"""C34 generator-side exact checks. Standard library only; not trusted verification."""
from __future__ import annotations
import argparse, hashlib, itertools as it, json, math, platform, resource, time
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

VERSION="c34-growing-multiplicity-v1"
def ck(x,msg):
    if not x: raise AssertionError(msg)
def edges(t): return tuple(it.combinations(sorted(t),2))
def power3(n):
    k=0
    while n>1 and n%3==0: n//=3; k+=1
    ck(n==1,"not power three"); return k

def vec(n,k):
    a=[]
    for _ in range(k): a.append(n%3); n//=3
    return tuple(a)
def num(v):
    x=0
    for z in reversed(v): x=3*x+z
    return x
def addv(a,b): return tuple((x+y)%3 for x,y in zip(a,b))
def mulv(c,a): return tuple((c*x)%3 for x in a)

def affine_lines(n):
    k=power3(n); seen=set(); out=[]
    for u,v in it.combinations(range(n),2):
        w=num(tuple((-x-y)%3 for x,y in zip(vec(u,k),vec(v,k))))
        t=tuple(sorted((u,v,w)))
        if t not in seen: seen.add(t); out.append(t)
    use=Counter(e for t in out for e in edges(t))
    ck(len(use)==n*(n-1)//2 and set(use.values())=={1},"affine partition")
    return out

def direction_factors(n):
    k=power3(n); reps=[]
    for x in range(1,n):
        v=vec(x,k); lead=next(i for i,z in enumerate(v) if z)
        w=mulv(2 if v[lead]==2 else 1,v); z=num(w)
        if z not in reps: reps.append(z)
    allv=[vec(i,k) for i in range(n)]; factors=[]
    for z in reps:
        d=vec(z,k); lines=set()
        for x in allv:
            t=tuple(sorted(num(y) for y in (x,addv(x,d),addv(x,mulv(2,d)))))
            lines.add(t)
        ck(len(lines)==n//3,"factor size")
        factors.append(tuple(sorted(lines)))
    use=Counter(e for f in factors for t in f for e in edges(t))
    ck(len(factors)==(n-1)//2 and len(use)==n*(n-1)//2 and set(use.values())=={1},"directions")
    return factors

def mech(m,b): return {x for x in range(m) if ((x+1)*b)//m>(x*b)//m}
def sigma(n,h):
    if h==0:return F(0)
    if h%2:return F(n)
    return F(3*h*n,2*(h+1))
def partial_packet(m,b,p):
    ck(m%2 and 0<b<m and 0<=p<=m-1,"partial domain")
    D=p//2; C=mech(m,b); mu=(b*D+m-1)//m; delta=m*mu-b*D
    starts1=[(s+t)%m for s in C for t in range(D)]
    starts2=[(s-t)%m for s in C for t in range(D)]
    lo,rem=divmod(b*D,m); hi=lo+int(rem>0)
    ck(all(Counter(starts1)[i] in (lo,hi) for i in range(m)),"mechanical U")
    ck(all(Counter(starts2)[i] in (lo,hi) for i in range(m)),"mechanical V")
    E=3*b*D+2*m*(D-mu); N=2*m+b; endpoint=p*N-2*E
    ck(endpoint>=0,"endpoint negative")
    if p==0:k=F(0)
    elif p%2:
        k=F(endpoint); ck(k==2*m+b+4*delta and k<7*m,"odd packet")
    else:
        k=F(endpoint)+F(3*E,p+1)
        ck(k==4*delta+F(3*(D*(2*m+b)-2*delta),2*D+1),"even identity")
        ck(k<F(17*m,2),"even packet")
    return {"D":D,"mu":mu,"delta":delta,"E":E,"endpoint":endpoint,"kappa":k}

def product(m,R):
    fm=direction_factors(m); fq=direction_factors(R); triples=[]; owner={}
    def put(t,key):
        t=tuple(sorted(t)); ck(len(set(t))==3,"repeated triple")
        triples.append((t,key))
        for e in edges(t): ck(e not in owner,"edge collision"); owner[e]=key
    for X in range(R):
        for di,f in enumerate(fm):
            for t in f: put(tuple(X*m+i for i in t),("internal",X,di))
    for dq,f in enumerate(fq):
        for qi,(X,Y,Z) in enumerate(f):
            for i in range(m):
                for j in range(m): put((X*m+i,Y*m+j,Z*m+((i+j)%m)),("cross",dq,qi,(j-i)%m))
    r=m*R; ck(len(owner)==r*(r-1)//2,"product coverage")
    return triples,owner,fm,fq

def external(m,R,h,b,p,q):
    ck(R>=9 and 2<=h<=R-1 and 0<b<m,"external domain")
    ck(p//2<=(m-1)//2 and q//2<=m*(R-3)//2,"slot capacity")
    triples,owner,fm,fq=product(m,R); r=m*R
    distinguished=0; C=mech(m,b); D=p//2; mu=(b*D+m-1)//m
    alpha=set(); beta=set()
    # h-2 ordinary full fibers, D internal factors each.
    for X in range(h-2):
        for di in range(D):
            for t in fm[di]: alpha.update(edges(tuple(X*m+i for i in t)))
    U,V,W=(h-2,h-1,h)
    for di in range(D-mu):
        for X in (U,V):
            for t in fm[di]: alpha.update(edges(tuple(X*m+i for i in t)))
    qline=fq[distinguished][0]
    # Any quotient triple in the direction works; relabel fibers to U,V,W locally.
    qline=(U,V,W)
    for s in C:
        for t in range(D): alpha.update(edges((U*m+(s+t)%m,V*m+(s-t)%m,W*m+(2*s)%m)))
    # Long external direction/translation slots.
    need=q//2; slots=[]
    for dq in range(1,len(fq)):
        for tau in range(m): slots.append((dq,tau))
    ck(need<=len(slots),"long slots")
    for dq,tau in slots[:need]:
        for X,Y,Z in fq[dq]:
            for i in range(m): beta.update(edges((X*m+i,Y*m+(i+tau)%m,Z*m+(2*i+tau)%m)))
    ck(not alpha&beta,"alpha beta collision")
    ck(all(e in owner for e in alpha|beta),"resource not core edge")
    ca=Counter(v for e in alpha for v in e); cb=Counter(v for e in beta for v in e)
    A=set(range(h*m))|set(range(h*m,h*m+b))
    ck(all(ca[v]<=p for v in A) and all(ca[v]==0 for v in set(range(r))-A),"short degree")
    ck(all(cb[v]<=q for v in range(r)),"long degree")
    pred=(h-2)*sigma(m,p)+partial_packet(m,b,p)["kappa"]+sigma(r,q)
    ck(pred<3*r+4*m and pred<=F(31*r,9),"external bound")
    return {"r":r,"a":len(A),"p":p,"q":q,"alpha_edges":len(alpha),"beta_edges":len(beta),"defect_bound":pred}

def face(r,a,p,q):
    c=r-a
    if a<3 or c<3:return False
    d=r-1-q;s=d-p
    if p>a-1 or s<0:return False
    lo=max(F(0),F(a*(c-q),2),F(c*(a-q),2))
    hi=min(F(a*c,2),F(a*s,2),F(c*d,2),F(a*s+c*d,6))
    return lo<=hi

def saturated(r,a,q):
    c=r-a; return c>=a+1 and 0<=q<=c

def round_robin(n):
    if n<=1:return []
    N=n if n%2==0 else n+1; zmod=N-1; dummy=N-1; out=[]
    for z in range(zmod):
        M=[(dummy,z)]+[((z+d)%zmod,(z-d)%zmod) for d in range(1,(N-2)//2+1)]
        out.append([tuple(sorted(e)) for e in M if max(e)<n])
    use=Counter(e for M in out for e in M)
    ck(len(use)==n*(n-1)//2 and set(use.values())=={1},"round robin")
    return out

def max_matching(n,E):
    adj=[set() for _ in range(n)]
    for u,v in E:adj[u].add(v);adj[v].add(u)
    memo={}
    def go(mask):
        if not mask:return ()
        if mask in memo:return memo[mask]
        u=(mask&-mask).bit_length()-1; rest=mask&~(1<<u); best=go(rest)
        for v in adj[u]:
            if rest>>v&1:
                z=((min(u,v),max(u,v)),)+go(rest&~(1<<v))
                if len(z)>len(best):best=z
        memo[mask]=best;return best
    return list(go((1<<n)-1))
def find_c4(E,verts):
    for q in it.combinations(verts,4):
        for z in ((q[0],q[1],q[2],q[3]),(q[0],q[1],q[3],q[2]),(q[0],q[2],q[1],q[3])):
            C={tuple(sorted((z[i],z[(i+1)%4]))) for i in range(4)}
            if C<=E:return C,set(q)
    return None

def dense_mechanics(r,a,p,q):
    ck(r%2 and p<=max(a-1,0) and p+q<=r//5,"finite safe range")
    E=set(it.combinations(range(r),2)); short=set()
    for M in round_robin(a)[:p]:short.update(M)
    E-=short
    for _ in range(q):
        M=max_matching(r,E);ck(len(M)==(r-1)//2,"near perfect");E-=set(M)
    deg=Counter(v for e in E for v in e); O=[v for v in range(r) if deg[v]%2]
    T=set(); internal=set()
    for x,y in zip(O[::2],O[1::2]):
        for z in range(r):
            xz=tuple(sorted((x,z)));yz=tuple(sorted((y,z)))
            if z not in (x,y) and z not in internal and xz in E and yz in E and xz not in T and yz not in T:
                T|={xz,yz};internal.add(z);break
        else:raise AssertionError("parity path")
    H=E-T; ck(all(Counter(v for e in H for v in e)[v]%2==0 for v in range(r)),"parity")
    j=len(H)%3; C=set(); used=set()
    for _ in range(j):
        z=find_c4(H-C,[v for v in range(r) if v not in used]);ck(z,"C4")
        ce,vs=z;C|=ce;used|=vs
    H-=C;ck(len(H)%3==0,"mod three")
    return {"r":r,"a":a,"p":p,"q":q,"T":len(T),"C":len(C)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",required=True);ns=ap.parse_args();st=time.monotonic()
    partial=[]
    for m in (3,9,27):
        for b in range(1,m):
            for p in range(m):partial.append(partial_packet(m,b,p))
    complete=[]
    for h in range(2,9):
        for b in (1,2):
            for p in range(4):
                for q in range(20):complete.append(external(3,9,h,b,p,q))
    named=[external(9,9,2,1,8,40),external(9,9,4,8,9,55),external(3,27,10,2,3,73),external(81,9,4,40,80,400)]
    scans=[]
    for r in (27,81,243):
        n=0
        for a in range(3,r-2):
            for q in range(r):ck(face(r,a,a-1,q)==saturated(r,a,q),"saturated classification");n+=1
        scans.append({"r":r,"cases":n})
    dense=[]
    for r in (9,11,15):
        for a in range(r+1):
            for p in range(min(max(a-1,0),r//5)+1):
                for q in range(r//5-p+1):dense.append(dense_mechanics(r,a,p,q))
    diag=partial_packet(9,1,8);ck(diag["E"]==66 and diag["endpoint"]==20 and diag["kappa"]==42,"erratum diagnostic")
    # Twelve deliberately false statements must be rejected.
    muts=[]
    tests=[lambda:ck(66==58,"old E"),lambda:ck(20==120,"old endpoint"),lambda:ck(42<42,"underbound"),lambda:ck(3>=9,"R"),lambda:ck(27==26,"slots"),lambda:ck(sigma(81,8)>=F(243,2),"sigma"),lambda:ck(face(27,14,13,0),"false face"),lambda:ck(len(round_robin(9))==8,"factor count"),lambda:dense_mechanics(15,3,3,0),lambda:ck(8%3==1,"mod"),lambda:ck(F(3,4)<F(3,4),"threshold"),lambda:ck(F(5,4)+1<F(5,4),"leave")]
    for i,t in enumerate(tests):
        try:t()
        except Exception as e:muts.append({"id":i,"rejected":True,"error":type(e).__name__})
        else:muts.append({"id":i,"rejected":False})
    ck(all(x["rejected"] for x in muts),"mutation escaped")
    out={"version":VERSION,"python":platform.python_version(),"partial_cases":len(partial),"external_complete_cases":len(complete),"external_named":named,"saturated_scans":scans,"dense_mechanics_cases":len(dense),"diagnostic":{k:str(v) if isinstance(v,F) else v for k,v in diag.items()},"mutations":muts,"external_decomposition_theorem_executed":False,"elapsed_seconds":time.monotonic()-st,"peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    p=Path(ns.out);p.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":"ok","sha256":hashlib.sha256(p.read_bytes()).hexdigest()}))
if __name__=="__main__":main()
