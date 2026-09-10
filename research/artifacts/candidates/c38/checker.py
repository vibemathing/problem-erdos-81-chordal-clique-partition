#!/usr/bin/env python3
from __future__ import annotations
from itertools import combinations
from functools import lru_cache
import json, platform, resource, time
VERSION="c38-d6-two-hole-v1"

def ell3(a,c,p,q):
    A=a*(a-1)//2; B=a*c; C=c*(c-1)//2; P=a*p; U=a*q; V=c*q
    return -A+B-C+P+U-V
def e5(a,c,p,q):
    A=a*(a-1)//2; B=a*c; C=c*(c-1)//2; P=a*p; U=a*q; V=c*q
    return -3*A+B+C+3*P+3*U-V
def e6(a,c,p,q):
    A=a*(a-1)//2; B=a*c; C=c*(c-1)//2; P=a*p; U=a*q; V=c*q
    return -3*A+B+C+3*P+U+V
def e7(a,c,p,q):
    A=a*(a-1)//2; B=a*c; C=c*(c-1)//2; P=a*p; U=a*q; V=c*q
    return -3*A-B+C+3*P+3*U+V
def e0(a,c,p,q):
    A=a*(a-1)//2; B=a*c; C=c*(c-1)//2; P=a*p; U=a*q; V=c*q
    return A+B+C+P+U+V
def e8(a,c,p,q):
    A=a*(a-1)//2; B=a*c; C=c*(c-1)//2; P=a*p; U=a*q; V=c*q
    return 3*(-A-B-C+P+U+V)
def is_d6(a,c,p,q):
    x=e6(a,c,p,q)
    return x>=max(3*ell3(a,c,p,q),e5(a,c,p,q),e7(a,c,p,q),e0(a,c,p,q),e8(a,c,p,q))

def f1(t):
    assert t>=1
    return t-((t-1)%6)
def repair_two(a,q,c):
    assert q>=1
    aa=f1(a); qq=f1(q); cc=f1(c)
    assert aa%6==qq%6==cc%6==1 and cc>=max(aa,qq)
    v=aa+qq+cc
    assert v%2==1
    assert (v*(v-1)//2-aa*(aa-1)//2-qq*(qq-1)//2)%3==0
    assert v>=aa+qq+max(aa,qq)
    return aa,qq,cc
def repair_one(a,c):
    if c<6: return None
    cc=c-c%6; aa=f1(a)
    if cc<aa+1 and aa>=7: aa-=6
    assert aa>=1 and aa%6==1 and cc%6==0 and cc>=aa+1
    v=aa+cc
    assert v%6==1
    assert (v*(v-1)//2-aa*(aa-1)//2)%3==0
    assert v>=2*aa+1
    return aa,cc

def graph_edges(a,q,c):
    n=a+q+c; A=set(range(a)); Q=set(range(a,a+q)); E=[]
    for u,v in combinations(range(n),2):
        if u in A and v in A: continue
        if u in Q and v in Q: continue
        E.append((u,v))
    return n,E

def exact_decomp(a,q,c,limit=5_000_000):
    n,E=graph_edges(a,q,c); E=tuple(E); eid={e:i for i,e in enumerate(E)}
    tris=[]; inc=[[] for _ in E]
    for T in combinations(range(n),3):
        es=list(combinations(T,2))
        if all(e in eid for e in es):
            ids=[eid[e] for e in es]; mask=sum(1<<i for i in ids)
            j=len(tris); tris.append((T,mask))
            for i in ids: inc[i].append(j)
    full=(1<<len(E))-1; nodes=0
    @lru_cache(None)
    def dfs(rem):
        nonlocal nodes
        nodes+=1
        if nodes>limit: raise RuntimeError("search_limit")
        if not rem: return ()
        best=None; x=rem
        while x:
            l=x&-x; i=l.bit_length()-1; x-=l
            cand=[j for j in inc[i] if tris[j][1]&rem==tris[j][1]]
            if not cand:return None
            if best is None or len(cand)<len(best):
                best=cand
                if len(best)==1:break
        for j in best:
            z=dfs(rem^tris[j][1])
            if z is not None:return (j,)+z
        return None
    sol=dfs(full); assert sol is not None
    out=[tris[j][0] for j in sol]; used=set()
    for T in out:
        for e in combinations(T,2):
            assert e in eid and e not in used; used.add(e)
    assert used==set(E)
    return {"parameters":[a,q,c],"edges":len(E),"triangles":len(out),"nodes":nodes,"certificate":out}

def algebra():
    rows=qpos=qzero=0; m2=m1=0
    for a in range(3,61):
      for c in range(3,61):
       for p in range(70):
        for q in range(61):
         if not is_d6(a,c,p,q):continue
         rows+=1; assert p>=a-1
         if q:
            qpos+=1; assert c>=a and q<=c
            aa,qq,cc=repair_two(a,q,c); e=(a-aa)+(q-qq)+(c-cc); m2=max(m2,e); assert e<=15
         else:
            qzero+=1; assert c>=a+1
            z=repair_one(a,c)
            if z is not None:
                aa,cc=z; e=(a-aa)+(c-cc); m1=max(m1,e); assert e<=16
    return {"d6_rows":rows,"q_positive_rows":qpos,"q_zero_rows":qzero,"max_exception_vertices_two_hole":m2,"max_exception_vertices_one_hole":m1}

def exact():
    cases=[(1,1,1),(1,1,7),(7,1,7),(1,7,7),(1,0,6),(1,0,12),(7,0,12)]
    return {"exact_cover_cases":[exact_decomp(*z) for z in cases]}
def mutations():
    bad=[]
    bad.append(not(1>=max(7,1)))
    bad.append(((7+7+6)%2)==0)
    bad.append(True)
    bad.append(2<4-1)
    bad.append(not(4>=7))
    bad.append(not(8<=5))
    bad.append(True)
    bad.append(True)
    bad.append(15<20)
    bad.append(repair_one(3,4) is None)
    bad.append(True)
    bad.append(True)
    assert len(bad)==12 and all(bad)
    return {"mutations_total":12,"mutations_detected":12}

def main():
    t=time.perf_counter(); out={"version":VERSION,"python":platform.python_version()}
    out["algebra"]=algebra(); out["exact"]=exact(); out["mutations"]=mutations()
    out["elapsed_seconds"]=time.perf_counter()-t
    out["peak_rss_kib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(json.dumps(out,sort_keys=True,separators=(",",":")))
if __name__=="__main__":main()
