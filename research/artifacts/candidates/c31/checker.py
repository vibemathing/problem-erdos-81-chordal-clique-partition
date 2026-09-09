"""C31 exact construction checks for p=2,q=2 shared-boundary continuation.
Generator-side finite checks only; not trusted verification.
"""
from __future__ import annotations
import argparse, itertools as it, json, math, time, platform, resource
from pathlib import Path
from collections import Counter, defaultdict
from fractions import Fraction as F

VERSION="c31-p2q2-shared-boundary-v1"

def ck(x,msg):
    if not x: raise AssertionError(msg)

def edges(t):
    return [tuple(sorted(e)) for e in it.combinations(t,2)]

def power3(r):
    k=0; x=r
    while x>1 and x%3==0:
        x//=3; k+=1
    ck(x==1,"r not power of 3")
    return k

def third(u,v,k):
    w=0; place=1
    for _ in range(k):
        du=u%3; dv=v%3
        w += ((-du-dv)%3)*place
        u//=3; v//=3; place*=3
    return w

def design(r):
    k=power3(r); out=set()
    for u,v in it.combinations(range(r),2):
        w=third(u,v,k)
        ck(w!=u and w!=v,"third repeats")
        out.add(tuple(sorted((u,v,w))))
    cnt=Counter(e for T in out for e in edges(T))
    ck(len(cnt)==r*(r-1)//2 and set(cnt.values())=={1},"not STS edge partition")
    return sorted(out)

def classes(r):
    D0=[tuple(range(j,j+3)) for j in range(0,r,3)]
    D1=[(j+i,j+i+3,j+i+6) for j in range(0,r,9) for i in range(3)]
    return D0,D1

def relabel_for_A(r,A):
    A=sorted(A); a=len(A); t,b=divmod(a,3)
    D0,D1=classes(r)
    chosen=D1[:t]
    good=sorted({v for T in chosen for v in T})
    avail=sorted(set(range(r))-set(good))
    extra=avail[:b]
    abstract=good+extra
    rest=sorted(set(range(r))-set(abstract))
    ck(len(abstract)==a,"mark count")
    perm=dict(zip(abstract+rest,A+sorted(set(range(r))-set(A))))
    ck(len(set(perm.values()))==r,"not bijection")
    trT=lambda T:tuple(sorted(perm[v] for v in T))
    trE=lambda e:tuple(sorted(perm[v] for v in e))
    return D0,D1,chosen,b,perm,trT,trE

def aggregated_Q(r,A):
    A=set(A); a=len(A); ck(power3(r)>=2 and 3<=a<=r,"domain")
    D0,D1,chosen,b,perm,trT,trE=relabel_for_A(r,A)
    removed=set(D0)|set(chosen)
    P=[trT(T) for T in design(r) if T not in removed]
    alpha={trE(e):F(1) for T in chosen for e in edges(T)}
    beta={trE(e):F(1) for T in D0 for e in edges(T)}
    return P,alpha,beta,b,chosen,(D0,D1,perm)

def verify_joint(r,A,P,alpha,beta,p=2,q=2):
    A=set(A); load=defaultdict(F); da=[F(0)]*r; db=[F(0)]*r
    seen=set()
    for T in P:
        ck(T not in seen,"duplicate core triangle");seen.add(T)
        for e in edges(T): load[e]+=1
    for typ,H,deg in [('a',alpha,da),('b',beta,db)]:
        for e,w in H.items():
            ck(w>=0,"neg")
            if typ=='a': ck(set(e)<=A,"alpha outside A")
            load[e]+=w
            for v in e: deg[v]+=w
    ck(all(v<=1 for v in load.values()),"core overload")
    ck(all(da[v] <= (p if v in A else 0) for v in range(r)),"alpha degree")
    ck(all(db[v]<=q for v in range(r)),"beta degree")
    M=r*(r-1)//2
    sc=F(M)-sum(load.values())
    sa=F(len(A)*p)-sum(da)
    sb=F(r*q)-sum(db)
    val=F(len(P))+sum(alpha.values())+sum(beta.values())
    L=F(M+len(A)*p+r*q,3)
    ck(sc+sa+sb==3*(L-val),"slack identity")
    return dict(value=val,L=L,S_core=sc,S_short=sa,S_long=sb,S_total=sc+sa+sb)

def pathify_triangles(H, triples):
    H=dict(H); deleted=[]; colors=[set(),set()]
    for T in triples:
        a,b,c=sorted(T)
        de=tuple(sorted((a,c)))
        ck(H.get(de)==1,"expected full triangle")
        del H[de]; deleted.append(de)
        e0=tuple(sorted((a,b))); e1=tuple(sorted((b,c)))
        ck(H.get(e0)==1 and H.get(e1)==1,"kept edges absent")
        colors[0].add(e0); colors[1].add(e1)
    for C in colors:
        deg=Counter(v for e in C for v in e)
        ck(max(deg.values(),default=0)<=1,"not matching")
    ck(set(H)==colors[0]|colors[1],"path coloring incomplete")
    return H,deleted,colors

def actual_pack(r,A):
    P,alpha,beta,b,chosen,aux=aggregated_Q(r,A)
    D0,D1,perm=aux
    trT=lambda T:tuple(sorted(perm[v] for v in T))
    beta_tris=[trT(T) for T in D0]
    alpha_tris=[trT(T) for T in chosen]
    alpha2,delA,colA=pathify_triangles(alpha,alpha_tris)
    beta2,delB,colB=pathify_triangles(beta,beta_tris)
    ans=verify_joint(r,A,P,alpha2,beta2)
    t=len(chosen); a=len(A)
    ck(len(delA)==t and len(delB)==r//3,"delete counts")
    ck(ans["S_core"]==t+r//3,"core deleted edges")
    ck(ans["S_short"]==2*t+2*b,"short slack")
    ck(ans["S_long"]==2*r//3,"long slack")
    ck(ans["S_total"]==r+a+b,"total actual slack")
    return ans,dict(alpha_deleted=delA,beta_deleted=delB,
                    alpha_matchings=[sorted(x) for x in colA],
                    beta_matchings=[sorted(x) for x in colB],
                    core_triangles=P)

def q_formula_check(r,A):
    P,alpha,beta,b,chosen,_=aggregated_Q(r,A)
    ans=verify_joint(r,A,P,alpha,beta)
    ck(ans["S_core"]==0 and ans["S_long"]==0 and ans["S_short"]==2*b,"Q witness slack")
    return ans

def full_face_weights(r,a):
    c=r-a
    if c==0:
        alpha=F(2,r-1); beta=F(2,r-1); z3=F(r-5,(r-1)*(r-2))
        ck(alpha+beta+(r-2)*z3==1,"c0 edge")
        return {"case":"c0","alphaAA":str(alpha),"betaAA":str(beta),"zAAA":str(z3)}
    if c==1:
        alpha=F(2,a-1); b1=F(2,a); b2=F(2,a)
        z2=F(a-2,a*(a-1)); z3=F(a*a-6*a+4,a*(a-2)*(a-1))
        ck(alpha+b2+z2+(a-2)*z3==1,"c1 AA")
        ck(b1+(a-1)*z2==1,"c1 AC")
        ck((a-1)*alpha==2 and (a-1)*b2+b1==2 and a*b1==2,"c1 endpoints")
        ck(min(alpha,b1,b2,z2,z3)>=0,"c1 nonneg")
        return {"case":"c1","alphaAA":str(alpha),"betaAA":str(b2),"betaAC":str(b1),"zAAA":str(z3),"zAAC":str(z2)}
    if c==2:
        alpha=F(2,a-1); b=F(2,a+1)
        z1=F(a-1,a*(a+1)); z2=z1
        z3=F(a**3-6*a*a+3*a-2,a*(a-2)*(a-1)*(a+1))
        ck(alpha+b+2*z2+(a-2)*z3==1,"c2 AA")
        ck(b+(a-1)*z2+z1==1,"c2 AC")
        ck(b+a*z1==1,"c2 CC")
        ck((a-1)*alpha==2 and (a+1)*b==2,"c2 endpoint")
        ck(min(alpha,b,z1,z2,z3)>=0,"c2 nonneg")
        return {"case":"c2","alphaAA":str(alpha),"betaAll":str(b),"zAAA":str(z3),"zAAC":str(z2),"zACC":str(z1)}
    d=r-3; s=r-5
    ell=max(F(0),F(a*(c-2),2),F(c*(a-2),2))
    upper=min(F(a*c,2),F(a*s,2),F(c*d,2),F(a*s+c*d,6))
    ck(ell<=upper,"C28 interval fails")
    return {"case":"c>=3","ell":str(ell),"upper":str(upper)}

def controls():
    quarter={"params":[5,2,4,1,1],"L":"5","uniform":"16/3","inside":False}
    twelfth={"params":[7,3,7,1,1],"L":"31/3","uniform":"31/3","inside":True}
    for r in (9,27):
        D0,_=classes(r); ck(len(D0)==r//3,"factor count")
    return {"quarter":quarter,"twelfth":twelfth,
            "zero_short_class":"conversion lemma uses empty H and empty deletion set",
            "equal_prefix":"A=V is included for p=q=2; alpha/beta are tagged and edge-disjoint direction classes"}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("mode",choices=["construct","controls"]);ap.add_argument("--out",required=True)
    ns=ap.parse_args(); t0=time.monotonic()
    if ns.mode=="construct":
        rows=[]; nine=[]
        for r in (9,27,81):
            for a in range(3,r+1):
                A=set(range(a)); ff=full_face_weights(r,a)
                q=q_formula_check(r,A); act,w=actual_pack(r,A)
                ck(q["S_total"]<=4,"Q constant defect")
                ck(act["S_total"]<=2*r+2,"actual O(r)")
                rows.append({"r":r,"a":a,"Q_witness":{k:str(v) for k,v in q.items()},
                             "actual_witness":{k:str(v) for k,v in act.items()},"face":ff})
                if r==9: nine.append({"a":a,"Q":str(q["value"]),"L":str(q["L"]),"actual_pack_value":str(act["value"]),
                                      "Q_slack":str(q["S_total"]),"actual_slack":str(act["S_total"]),
                                      "alpha_deleted":w["alpha_deleted"],"beta_deleted":w["beta_deleted"],
                                      "alpha_matchings":w["alpha_matchings"],"beta_matchings":w["beta_matchings"],
                                      "core_triangles":w["core_triangles"]})
        subset_count=0
        for mask in range(1<<9):
            if mask.bit_count()<3: continue
            A={v for v in range(9) if mask>>v&1}
            q_formula_check(9,A); actual_pack(9,A); subset_count+=1
        out={"version":VERSION,"complete_cardinalities":{"9":7,"27":25,"81":79},
             "all_actual_r9_subsets_size_ge3":subset_count,"rows":rows,"nine":nine}
    else:
        out={"version":VERSION,**controls()}
    out["python"]=platform.python_version()
    out["elapsed_seconds"]=time.monotonic()-t0
    out["peak_rss_kib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    Path(ns.out).write_text(json.dumps(out,indent=2,sort_keys=True,default=str)+"\n")
if __name__=="__main__": main()
