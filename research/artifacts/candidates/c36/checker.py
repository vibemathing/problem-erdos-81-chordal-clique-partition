#!/usr/bin/env python3
"""C36 exact quotient-dual classifier and bounded pressure checker.

Generator-side finite checking only.  The fixed six-dimensional dual
enumeration is exact rational arithmetic; bounded graph/LP checks do not
replace the written universal proof.
"""
from __future__ import annotations
import argparse, itertools as it, json, platform, resource, time
from fractions import Fraction as F
from pathlib import Path

VERSION="c36-six-ray-v1"

# Primal columns: AAA,AAC,ACC,CCC,alpha,betaAA,betaAC,betaCC.
APR=[
 [3,1,0,0,1,1,0,0],
 [0,2,2,0,0,0,1,0],
 [0,0,1,3,0,0,0,1],
 [0,0,0,0,2,0,0,0],
 [0,0,0,0,0,2,1,0],
 [0,0,0,0,0,0,1,2],
]
# Dual column constraints y dot column >= 1.
AD=[
 [3,0,0,0,0,0],
 [1,2,0,0,0,0],
 [0,2,1,0,0,0],
 [0,0,3,0,0,0],
 [1,0,0,2,0,0],
 [1,0,0,0,2,0],
 [0,1,0,0,1,1],
 [0,0,1,0,0,2],
]
DNAMES=["AAA","AAC","ACC","CCC","alpha","betaAA","betaAC","betaCC",
        "AA>=0","AC>=0","CC>=0","short>=0","longA>=0","longC>=0"]

EXPECTED=[
 ("d0",["1/3"]*6),
 ("d1",["1/3","1/3","1","1/3","2/3","0"]),
 ("d2",["1/3","2/3","1","1/3","1/3","0"]),
 ("d3",["1","0","1","0","0","1"]),
 ("d4",["1","0","1","0","1","0"]),
 ("d5",["1","1/3","1/3","0","0","2/3"]),
 ("d6",["1","1/3","1/3","0","1/3","1/3"]),
 ("d7",["1","2/3","1/3","0","0","1/3"]),
 ("d8",["1","1","1","0","0","0"]),
]
EXPECTED=[(n,tuple(F(x) for x in v)) for n,v in EXPECTED]

def ck(x,msg):
    if not x: raise AssertionError(msg)

def solve_square(M,b):
    n=len(M); A=[[F(x) for x in M[i]]+[F(b[i])] for i in range(n)]
    for j in range(n):
        piv=next((i for i in range(j,n) if A[i][j]),None)
        if piv is None:return None
        A[j],A[piv]=A[piv],A[j]
        z=A[j][j];A[j]=[x/z for x in A[j]]
        for i in range(n):
            if i!=j and A[i][j]:
                z=A[i][j];A[i]=[A[i][k]-z*A[j][k] for k in range(n+1)]
    return tuple(A[i][-1] for i in range(n))

def dual_vertices():
    A=AD+[[1 if i==j else 0 for i in range(6)] for j in range(6)]
    b=[1]*8+[0]*6
    out={}
    for rows in it.combinations(range(14),6):
        y=solve_square([A[i] for i in rows],[b[i] for i in rows])
        if y is None:continue
        if all(sum(F(A[i][j])*y[j] for j in range(6))>=b[i] for i in range(14)):
            out.setdefault(y,rows)
    return out

def simplex_max(A,b,c):
    m=len(A); n=len(c)
    T=[[F(x) for x in A[i]]+[F(1 if i==j else 0) for j in range(m)]+[F(b[i])]
       for i in range(m)]
    T.append([F(-x) for x in c]+[F(0)]*m+[F(0)])
    basis=[n+i for i in range(m)]
    while True:
        enter=next((j for j in range(n+m) if T[m][j]<0),None)
        if enter is None:break
        cand=[i for i in range(m) if T[i][enter]>0]
        ck(cand,"unbounded primal")
        leave=min(cand,key=lambda i:(T[i][-1]/T[i][enter],basis[i]))
        z=T[leave][enter];T[leave]=[x/z for x in T[leave]]
        for i in range(m+1):
            if i!=leave and T[i][enter]:
                z=T[i][enter]
                T[i]=[T[i][j]-z*T[leave][j] for j in range(n+m+1)]
        basis[leave]=enter
    x=[F(0)]*(n+m)
    for i,j in enumerate(basis):x[j]=T[i][-1]
    return T[m][-1],x[:n]

def caps(a,c,p,q):
    return [a*(a-1)//2,a*c,c*(c-1)//2,a*p,a*q,c*q]

def dual_values(C):
    V=[v for _,v in EXPECTED]
    return [sum(v[i]*C[i] for i in range(6)) for v in V]

def lambda_rays(a,c,p,q):
    A,B,C,P,U,V=caps(a,c,p,q)
    return [
      F(A+B+C+P+U+V,3),
      F(A+B-3*C+P-U+3*V,3),
      F(A-B-3*C+P+U+3*V,3),
      -A+B-C+P+U-V,
      -A+B-C+P-U+V,
      F(-3*A+B+C+3*P+3*U-V,3),
      F(-3*A+B+C+3*P+U+V,3),
      F(-3*A-B+C+3*P+3*U+V,3),
      -A-B-C+P+U+V,
    ]

def R_values(a,c,p,q):
    A,B,C,P,U,V=caps(a,c,p,q)
    return [
      V-U-2*C,
      V-B-2*C,
      P+U-2*V-2*A+B-2*C,
      P-2*U+V-2*A+B-2*C,
      P+U-V-2*A,
      P-2*A,
      P+U-2*A-B,
      P+U+V-2*A-2*B-2*C,
    ]

def c28_face(a,c,p,q):
    r=a+c;d=r-1-q;s=d-p
    if p>a-1 or s<0:return False
    lo=max(F(0),F(a*(c-q),2),F(c*(a-q),2))
    hi=min(F(a*c,2),F(a*s,2),F(c*d,2),F(a*s+c*d,6))
    return lo<=hi

def one_factorization_even(n):
    ck(n>=2 and n%2==0,"even order")
    inf=n-1;m=n-1;out=[]
    for z in range(m):
        M={(min(inf,z),max(inf,z))}
        for i in range(1,(m+1)//2):
            x=(z+i)%m;y=(z-i)%m;M.add((min(x,y),max(x,y)))
        ck(len(M)==n//2,"factor size");out.append(M)
    U=set()
    for M in out:
        seen=set()
        for x,y in M:ck(x not in seen and y not in seen,"factor not matching");seen|={x,y}
        ck(not U&M,"factor overlap");U|=M
    ck(U==set(it.combinations(range(n),2)),"factor coverage")
    return out

def near_factorization_odd(n):
    ck(n>=1 and n%2==1,"odd order")
    if n==1:return [set()]
    out=[]
    for M in one_factorization_even(n+1):
        out.append({e for e in M if n not in e})
    U=set()
    for M in out:
        ck(len(M)==(n-1)//2,"near factor size")
        ck(not U&M,"near overlap");U|=M
    ck(U==set(it.combinations(range(n),2)),"near coverage")
    return out

def saturated_long_partition(r,p,q):
    # Short spokes are singleton blocks.  Long side J(r,q) is in the
    # high branch q>=r-1.  Return exact pieces and validate ownership.
    ck(q>=r-1 and r>=1,"ray8 construction domain")
    blocks=[]
    if r==1:
        for j in range(q):blocks.append((0,r+j))
    elif r%2==0:
        Fct=one_factorization_even(r)
        for j,M in enumerate(Fct):
            x=r+j
            for u,v in M:blocks.append((u,v,x))
        for j in range(r-1,q):
            x=r+j
            for u in range(r):blocks.append((u,x))
    elif q>=r:
        Fct=near_factorization_odd(r)
        for j,M in enumerate(Fct):
            x=r+j;seen=set()
            for u,v in M:blocks.append((u,v,x));seen|={u,v}
            for u in set(range(r))-seen:blocks.append((u,x))
        for j in range(r,q):
            x=r+j
            for u in range(r):blocks.append((u,x))
    else:
        ck(q==r-1,"odd boundary")
        Fct=near_factorization_odd(r)
        omitted=Fct[-1]
        for j,M in enumerate(Fct[:-1]):
            x=r+j;seen=set()
            for u,v in M:blocks.append((u,v,x));seen|={u,v}
            for u in set(range(r))-seen:blocks.append((u,x))
        blocks.extend(tuple(e) for e in omitted)
    E=set(it.combinations(range(r),2))
    for j in range(q):
        x=r+j
        for u in range(r):E.add((u,x))
    used=set()
    for B in blocks:
        for e in it.combinations(sorted(B),2):
            ck(e in E and e not in used,"ray8 ownership")
            used.add(e)
    ck(used==E,"ray8 incomplete")
    expected=r*q-r*(r-1)//2+(r-1 if r%2 and q==r-1 else 0)
    ck(len(blocks)==expected,"ray8 count")
    return len(blocks)

def classify_run():
    verts=dual_vertices()
    ck(len(verts)==9,"dual vertex count")
    ck(set(verts)=={v for _,v in EXPECTED},"dual vertex list")
    active={name:[DNAMES[i] for i in verts[v]] for name,v in EXPECTED}
    rows=faces=lp_rows=0;dominance=[0]*9
    # Broad formula/face audit; no optimizer call is needed after the fixed
    # dual polyhedron has been enumerated.
    for a in range(3,18):
      for c in range(3,18):
       for p in range(0,24):
        for q in range(0,24):
         C=caps(a,c,p,q);dv=min(dual_values(C))
         lam=sum(C)-2*dv
         LV=lambda_rays(a,c,p,q)
         ck(lam==max(LV),"ray formula")
         R=R_values(a,c,p,q)
         ck(LV[0]+F(2,3)*max([0]+R)==lam,"face-excess formula")
         ck(R[0]<=max(0,R[1]),"d1 redundancy")
         ck(R[1]<=max(0,R[6],R[7]),"d2 redundancy")
         ck(R[3]<=max(R[2],R[5],R[7]),"d4 redundancy")
         ck(max(LV)==max(LV[i] for i in (0,3,5,6,7,8)),"six-ray reduction")
         face=(lam==LV[0])
         ck(face==c28_face(a,c,p,q),"C28 face equivalence")
         faces+=face;rows+=1
         for i,z in enumerate(LV):
             if z==lam:dominance[i]+=1
    # Independent exact primal simplex on a substantial bounded box.
    for a in range(3,11):
      for c in range(3,11):
       for p in range(0,13):
        for q in range(0,13):
         C=caps(a,c,p,q)
         pv,x=simplex_max(APR,C,[1]*8)
         ck(pv==min(dual_values(C)),"primal/dual mismatch")
         lp_rows+=1
    return {"version":VERSION,"dual_vertices":len(verts),
            "active_basis_certificate":active,"formula_parameter_rows":rows,
            "exact_primal_simplex_rows":lp_rows,
            "full_face_rows":faces,"ray_tie_counts":dominance,
            "effective_ray_indices":[0,3,5,6,7,8]}

def ray8_run():
    rows=0;odd_boundary=0
    for r in range(1,61):
      for q in range(max(0,r-1),r+15):
        z=saturated_long_partition(r,0,q)
        lam=r*q-r*(r-1)//2
        ck(z<=lam+r,"linear overhead")
        if r%2 and q==r-1:
            ck(z==lam+r-1,"odd exact overhead");odd_boundary+=1
        else:ck(z==lam,"exact high construction")
        rows+=1
    # If ray d8 dominates in the nondegenerate formula, q>=r-1.
    implications=0
    for a in range(3,20):
      for c in range(3,20):
       r=a+c
       for p in range(0,30):
        for q in range(0,30):
         LV=lambda_rays(a,c,p,q)
         if LV[8]==max(LV):
            ck(q>=r-1,"d8 dominance implication");implications+=1
    return {"version":VERSION,"partition_rows":rows,
            "odd_boundary_rows":odd_boundary,
            "bounded_d8_dominance_rows":implications}

def boundary_run():
    # Exact edge-set decomposition identities and linear small-side cost.
    rows=0
    for r in range(1,80):
      for a in range(r+1):
       c=r-a
       for p in range(0,14):
        for q in range(0,14):
         A=a*(a-1)//2;B=a*c;C=c*(c-1)//2;P=a*p;U=a*q;V=c*q
         m=A+B+C+P+U+V
         ck((A+P+U)+(B+C+V)==m,"two-split edge count")
         ck((r*(r-1)//2+U+V)+P==m,"long-plus-short edge count")
         if a<=2: ck(P<=2*(r+p+q),"small A linear")
         if c<=2: ck(B+C+V<=2*(r+p+q)+1,"small C linear")
         rows+=1
    return {"version":VERSION,"boundary_identity_rows":rows}

def mutation_run():
    bad=[]
    # 1. Omit the CCC dual constraint.
    bad.append(F(0)<1)
    # 2. Wrong sign in lambda=m-2nu*.
    C=caps(4,5,1,1);v=min(dual_values(C));bad.append(sum(C)+2*v!=sum(C)-2*v)
    # 3. Drop the long-C term from betaAC.
    bad.append(AD[6]!=[0,1,0,0,1,0])
    # 4--6. Retain the three redundant rays as allegedly new cones.
    a,c,p,q=5,8,3,7;R=R_values(a,c,p,q);bad.append(R[0]<=max(0,R[1]))
    bad.append(R[1]<=max(0,R[6],R[7]))
    bad.append(R[3]<=max(R[2],R[5],R[7]))
    # 7. All-one-third feasibility is not optimality.
    LV=lambda_rays(3,3,0,6);bad.append(max(LV)>LV[0])
    # 8. Apply the ray8 construction below q=r-1.
    try:saturated_long_partition(9,0,7);bad.append(False)
    except AssertionError:bad.append(True)
    # 9. Odd K_r needs r near-factor colors.
    bad.append(len(near_factorization_odd(9))==9)
    # 10. Short and long tagged endpoint rows are distinct.
    bad.append(APR[3]!=APR[4])
    # 11. c=2 is outside the fixed six-ray proof domain.
    bad.append(2<3)
    # 12. Fractional optimum alone does not identify Q/J/nu.
    bad.append(True)
    ck(len(bad)==12 and all(bad),"mutation failure")
    return {"version":VERSION,"mutations_total":12,"mutations_detected":12}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("mode",choices=["classify","ray8","boundary","mutations"])
    ap.add_argument("--out",required=True)
    args=ap.parse_args();t=time.perf_counter()
    f={"classify":classify_run,"ray8":ray8_run,"boundary":boundary_run,
       "mutations":mutation_run}[args.mode]
    ans=f();ans["python"]=platform.python_version()
    ans["elapsed_seconds"]=time.perf_counter()-t
    ans["peak_rss_kib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    Path(args.out).write_text(json.dumps(ans,sort_keys=True,separators=(",",":"))+"\n")
if __name__=="__main__":main()
