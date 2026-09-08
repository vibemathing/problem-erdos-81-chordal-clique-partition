"""C25 exact joint-LP and leaf-face audit. Candidate-side, not trusted verification.
Run: python extreme_audit.py --seconds 38 --out extreme-results.json
Standard-library Fraction arithmetic; all reported ranges are generated literally.
"""
from __future__ import annotations
import argparse, hashlib, itertools as it, json, math, pathlib, platform, resource, time
from fractions import Fraction as F
from functools import lru_cache
VERSION='c25-exact-v2'
DEADLINE=float('inf')
def tick():
    if time.monotonic()>DEADLINE: raise TimeoutError('bounded exact audit deadline')
def check(ok,msg):
    if not ok: raise ValueError(msg)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def solve(A,b):
    n=len(b); B=[list(map(F,row))+[F(v)] for row,v in zip(A,b)]
    for j in range(n):
        tick(); i=next((i for i in range(j,n) if B[i][j]),None)
        check(i is not None,'singular basis');B[j],B[i]=B[i],B[j]
        v=B[j][j];B[j]=[x/v for x in B[j]]
        for i in range(n):
            if i!=j and B[i][j]:
                v=B[i][j];B[i]=[x-v*y for x,y in zip(B[i],B[j])]
    return [B[i][-1] for i in range(n)]
def rank(A):
    if not A:return 0
    B=[list(map(F,row)) for row in A];k=0
    for j in range(len(B[0])):
        i=next((i for i in range(k,len(B)) if B[i][j]),None)
        if i is None:continue
        B[k],B[i]=B[i],B[k];v=B[k][j];B[k]=[x/v for x in B[k]]
        for i in range(len(B)):
            if i!=k and B[i][j]:
                v=B[i][j];B[i]=[x-v*y for x,y in zip(B[i],B[k])]
        k+=1
        if k==len(B):break
    return k

def lp_tableau(A,b):
    m=len(b);h=len(A[0]) if m else 0
    if not h:return F(0),[],[F(0)]*m
    tab=[[F(v) for v in row]+[F(i==j) for j in range(m)]+[F(b[i])] for i,row in enumerate(A)]
    tab.append([-F(1)]*h+[F(0)]*(m+1));basis=list(range(h,h+m))
    for _ in range(10000):
        tick(); ent=next((j for j in range(h+m) if tab[-1][j]<0),None)
        if ent is None:
            x=[F(0)]*h
            for i,j in enumerate(basis):
                if j<h:x[j]=tab[i][-1]
            return sum(x),x,tab[-1][h:h+m]
        poss=[i for i in range(m) if tab[i][ent]>0];check(poss,'unbounded tableau')
        leave=min(poss,key=lambda i:(tab[i][-1]/tab[i][ent],basis[i]));v=tab[leave][ent]
        tab[leave]=[x/v for x in tab[leave]]
        for i in range(m+1):
            if i!=leave and tab[i][ent]:
                v=tab[i][ent];tab[i]=[x-v*y for x,y in zip(tab[i],tab[leave])]
        basis[leave]=ent
    raise TimeoutError('tableau pivot cap')

def lp_revised(A,b):
    m=len(b);h=len(A[0]) if m else 0
    if not h:return F(0),[],[F(0)]*m
    cols=[list(map(F,c)) for c in zip(*A)]+[[F(i==j) for i in range(m)] for j in range(m)]
    cost=[F(1)]*h+[F(0)]*m;basis=list(range(h,h+m))
    for _ in range(10000):
        tick(); B=[[cols[j][i] for j in basis] for i in range(m)]
        xb=solve(B,b);check(min(xb,default=0)>=0,'infeasible revised basis')
        y=solve(list(map(list,zip(*B))),[cost[j] for j in basis])
        ent=next((j for j in range(h+m) if j not in basis and cost[j]-dot(y,cols[j])>0),None)
        if ent is None:
            x=[F(0)]*h
            for i,j in enumerate(basis):
                if j<h:x[j]=xb[i]
            return sum(x),x,y
        d=solve(B,cols[ent]);poss=[i for i in range(m) if d[i]>0];check(poss,'unbounded revised')
        leave=min(poss,key=lambda i:(xb[i]/d[i],basis[i]));basis[leave]=ent
    raise TimeoutError('revised pivot cap')

def validate(A,b,v,x,y):
    check(all(t>=0 for t in x+y),'negative primal/dual')
    check(all(dot(row,x)<=rhs for row,rhs in zip(A,b)),'capacity violation')
    check(all(dot(y,col)>=1 for col in zip(*A)),'dual undercoverage')
    check(sum(x)==dot(y,b)==v,'primal dual mismatch')
    pos=[j for j,v in enumerate(x) if v];tight=[row for row,rhs in zip(A,b) if dot(row,x)==rhs]
    check(rank([[row[j] for j in pos] for row in tight])==len(pos),'not an extreme point')

def model(r,a,b,p,q,free=None,triangles=True):
    E=list(it.combinations(range(r),2));index={e:i for i,e in enumerate(E)};m=len(E)
    cap=[1 if free is None or (free>>i)&1 else 0 for i in range(m)]+[p]*a+[q]*b
    cols=[];labels=[]
    if triangles:
        for t in it.combinations(range(r),3):
            c=[0]*(m+a+b)
            for e in it.combinations(t,2):c[index[e]]=1
            cols.append(c);labels.append(('z',t))
    for kind,d in [('a',a),('b',b)]:
        for e in it.combinations(range(d),2):
            c=[0]*(m+a+b);c[index[e]]=1
            for u in e:c[m+(0 if kind=='a' else a)+u]=1
            cols.append(c);labels.append((kind,e))
    A=[list(c) for c in zip(*cols)] if cols else [[] for _ in cap]
    return E,labels,A,cap

def integer_edge_dp(r,a,b,p,q):
    E,labels,A,cap=model(r,a,b,p,q);m=len(E)
    tri=[sum(1<<E.index(e) for e in it.combinations(t,2)) for t in it.combinations(range(r),3)]
    @lru_cache(None)
    def rec(left,da,db):
        tick()
        if not left:return 0
        k=(left&-left).bit_length()-1;u,v=E[k];rest=left^(1<<k)
        best=rec(rest,da,db)
        for kind,d,budget in [('a',a,da),('b',b,db)]:
            if v<d and budget[u]>0 and budget[v]>0:
                z=list(budget);z[u]-=1;z[v]-=1
                val=1+rec(rest,tuple(z) if kind=='a' else da,tuple(z) if kind=='b' else db)
                best=max(best,val)
        for t in tri:
            if t&(1<<k) and (left&t)==t:best=max(best,1+rec(left^t,da,db))
        return best
    return rec((1<<m)-1,(p,)*a,(q,)*b)

def integer_object_enum(r,a,b,p,q):
    E,labels,A,cap=model(r,a,b,p,q);cols=list(zip(*A));best=0
    # Object order differs from edge DP: include/exclude actual triangle and color objects.
    @lru_cache(None)
    def go(j,resources):
        tick()
        if j==len(cols):return 0
        no=go(j+1,resources);col=cols[j]
        if all(c<=t for c,t in zip(col,resources)):
            no=max(no,1+go(j+1,tuple(t-c for c,t in zip(col,resources))))
        return no
    return go(0,tuple(cap))

def charge_leaf_groups(E,labels,A,cap,x):
    m=len(E);frac=[];directions=[]
    for e in E:
        ids=[j for j,(kind,ee) in enumerate(labels) if ee==e and kind!='z' and x[j]>0]
        if not any(x[j].denominator!=1 for j in ids):continue
        total=sum(x[j] for j in ids);v=[0]*len(labels)
        if total<1:v[ids[0]]=1
        else:
            check(total==1 and len(ids)==2,'bad fractional capacity-one group')
            v[ids[0]]=1;v[ids[1]]=-1
        frac.append(e);directions.append(v)
    active=[i for i in range(m,len(cap)) if dot(A[i],x)==cap[i]]
    images=[[dot(A[i],v) for v in directions] for i in active]
    check(rank(images)==len(frac),'endpoint direction dependence')
    owner={}
    def aug(j,seen):
        for k,row in enumerate(images):
            if row[j] and k not in seen:
                seen.add(k)
                if k not in owner or aug(owner[k],seen):owner[k]=j;return True
        return False
    for j in range(len(frac)):check(aug(j,set()),'charging matching failed')
    kept=[v if v.denominator==1 else F(0) for v in x]
    lost=sum(x)-sum(kept)
    check(lost<=len(frac)<=len(cap)-m,'charged loss bound')
    check(all(dot(row,kept)<=rhs for row,rhs in zip(A,cap)),'rounded leaf infeasible')
    return len(frac),lost

def capfn(d):return 0 if d<=1 else d-1 if d%2==0 else d

def run():
    rows=[];counts=[]
    for r in range(5):
        count=0
        for a in range(r+1):
            for b in range(a,r+1):
                for p in range(capfn(a)+1):
                    for q in range(capfn(b)+1):
                        E,L,A,B=model(r,a,b,p,q)
                        v,x,y=lp_tableau(A,B);v2,x2,y2=lp_revised(A,B)
                        validate(A,B,v,x,y);validate(A,B,v2,x2,y2);check(v==v2,'two LP disagreement')
                        J=integer_edge_dp(r,a,b,p,q);J2=integer_object_enum(r,a,b,p,q)
                        check(J==J2 and J<=v,'two integer disagreement')
                        rows.append({'r':r,'a':a,'b':b,'p':p,'q':q,'nu_star':str(v),'J':J,'gap':str(v-J)});count+=1
        counts.append({'r':r,'cases':count})
    leafcases=0;groups=0;maxloss=F(0)
    for r in range(5):
        for free in range(1<<(r*(r-1)//2)):
            for a in range(r+1):
                for b in range(a,r+1):
                    E,L,A,B=model(r,a,b,1,1,free,False)
                    v,x,y=lp_tableau(A,B);validate(A,B,v,x,y)
                    n,lost=charge_leaf_groups(E,L,A,B,x);leafcases+=1;groups+=n;maxloss=max(maxloss,lost)
    E,L,A,B=model(5,2,4,1,1)
    chosen={('z',(0,1,4)):F(1,2),('z',(0,2,3)):F(1,4),('z',(0,2,4)):F(1,2),('z',(1,2,3)):F(1,4),('z',(1,3,4)):F(1,2),('z',(2,3,4)):F(1,2),('a',(0,1)):F(1,2),('b',(0,2)):F(1,4),('b',(0,3)):F(3,4),('b',(1,2)):F(3,4),('b',(1,3)):F(1,4)}
    x=[chosen.get(l,F(0)) for l in L];y=[F(0)]*len(B)
    for e in [(0,1),(0,3),(1,3),(2,4)]:y[E.index(e)]=1
    y[len(E)+2+2]=1;validate(A,B,F(5),x,y)
    v,u,vdual=lp_tableau(A,B);vv,uu,vvdual=lp_revised(A,B)
    check(v==vv==5 and integer_edge_dp(5,2,4,1,1)==5,'quarter example optimum')
    return {'verdict':'candidate_only','status':'finite_exact_checks_passed','version':VERSION,'complete_capped_core_range':counts,'parameter_rows':rows,'leaf_residual_cases':leafcases,'charged_fractional_groups':groups,'maximum_leaf_discarded_mass':str(maxloss),'named_quarter_example':{'r':5,'a':2,'b':4,'p':1,'q':1,'objective':5,'positive_columns':len(chosen),'tight_column_rank':11,'J':5,'primal':[{'kind':k,'vertices':t,'value':str(v)} for (k,t),v in chosen.items()],'dual':[str(v) for v in y]},'limitations':['No complete core range above four; core five is one named extra case.','Independent implementations share one generator trust domain.','The conditional leaf bound assumes integral residual core capacities.','No universal bound nu_star-J is proved by these finite tests.'],'trusted_verifier_run':False,'best_verified_result':'none'}

def main():
    global DEADLINE
    p=argparse.ArgumentParser();p.add_argument('--seconds',type=int,default=38);p.add_argument('--out',type=pathlib.Path,required=True);arg=p.parse_args()
    check(1<=arg.seconds<=120,'invalid time budget');start=time.monotonic();DEADLINE=start+arg.seconds
    resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824));resource.setrlimit(resource.RLIMIT_CPU,(arg.seconds+2,arg.seconds+3))
    result=run();result['runtime']={'python':platform.python_version(),'arithmetic':'fractions.Fraction','wall_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'memory_bytes':1073741824,'threads':1,'internal_seconds':arg.seconds,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
    raw=(json.dumps(result,sort_keys=True,indent=2)+'\n').encode();check(len(raw)<1048576,'output size limit')
    with arg.out.open('xb') as h:h.write(raw)
    print(json.dumps({'status':result['status'],'counts':result['complete_capped_core_range'],'leaf_cases':result['leaf_residual_cases'],'groups':result['charged_fractional_groups'],'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'seconds':result['runtime']['wall_seconds']}))
if __name__=='__main__':main()
