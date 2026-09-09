"""C28 finite exact checks. Candidate-side, not a trusted verification run.
Theorem input K is NOT executed. Every schedule actually used is checked exactly.
Run from repository: python subset_checker.py --mode construct|types|named --out NEW.json
"""
from __future__ import annotations
import argparse, collections, hashlib, importlib.util, itertools as it
import json, math, pathlib, platform, resource, time
from fractions import Fraction as F
from functools import lru_cache
VERSION='c28-subset-exact-v2'
DEP_SHA='bcee9e8a3d427059c5a10b9e3ce893ec1ae674f58feec3b10333e18ad8984c49'
DEADLINE=float('inf')
def tick():
    if time.monotonic()>DEADLINE:raise TimeoutError('finite audit deadline')
def ck(x,m):
    if not x:raise ValueError(m)
def edges(n):return list(it.combinations(range(n),2))
def ep(t):return list(it.combinations(sorted(t),2))
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def power3(n):
    while n>1 and n%3==0:n//=3
    return n==1

def field_add(x,y,k,sign=1):
    out=0;place=1
    for _ in range(k):
        out+=((x%3+sign*(y%3))%3)*place;place*=3;x//=3;y//=3
    return out
@lru_cache(None)
def affine_factors(v):
    ck(power3(v),'nonaffine order');k=0
    while 3**k<v:k+=1
    fac=[]
    for d in range(1,v):
        neg=field_add(0,d,k,-1)
        if d>neg:continue
        used=set();row=[]
        for x in range(v):
            if x not in used:
                T=tuple(sorted((x,field_add(x,d,k),field_add(x,neg,k))))
                row.append(T);used.update(T)
        fac.append(tuple(row))
    return tuple(fac)

@lru_cache(None)
def projective15():
    triples=sorted({tuple(sorted((u,v,u^v))) for u in range(1,16) for v in range(u+1,16)})
    masks=[sum(1<<(v-1) for v in T) for T in triples]
    classes=[]
    def visit(left,chosen):
        tick()
        if not left:
            classes.append(tuple(chosen));return
        u=left&-left
        for i,m in enumerate(masks):
            if m&u and m&left==m:visit(left^m,chosen+[i])
    visit((1<<15)-1,[])
    cms=[sum(1<<i for i in row) for row in classes]
    @lru_cache(None)
    def cover(left):
        tick()
        if not left:return ()
        bit=left&-left
        for j,m in enumerate(cms):
            if m&bit and m&left==m:
                rec=cover(left^m)
                if rec is not None:return (j,)+rec
        return None
    ans=cover((1<<35)-1);ck(ans is not None,'projective resolution not found')
    return tuple(tuple(tuple(v-1 for v in triples[i]) for i in classes[j]) for j in ans)

def validate_factors(v,rows):
    used=set()
    for row in rows:
        ck(sorted(x for T in row for x in T)==list(range(v)),'factor not a vertex partition')
        for T in row:
            ck(len(T)==3 and len(set(T))==3,'bad factor triple')
            for e in ep(T):
                ck(e not in used,'factor edge repeated');used.add(e)
    return used
@lru_cache(None)
def factors(v,count):
    ck(count>=0 and 2*count<=max(0,v-1),'invalid degree request')
    if count==0:return ()
    ck(v%6==3,'wrong good-block residue')
    if power3(v):rows=affine_factors(v)[:count]
    elif v==15:rows=projective15()[:count]
    else:
        m=v//3
        if count>m:raise LookupError('missing supplied resolution at this order')
        rows=tuple(tuple((j,m+(j+t)%m,2*m+(j+2*t)%m) for j in range(m)) for t in range(count))
    ck(len(rows)==count,'insufficient factors');validate_factors(v,rows);return rows

def good(n):return 0 if n<3 else n-(n-3)%6

def check_point(r,A,p,q,P,al,be,claimed=None):
    E=set(edges(r));A=set(A);load=collections.Counter();da=collections.Counter();db=collections.Counter()
    for T in P:
        ck(len(T)==3 and len(set(T))==3,'bad core triangle')
        for e in ep(T):
            ck(e in E,'core triangle outside graph');load[e]+=1
    for kind,x in [('a',al),('b',be)]:
        for e,w in x.items():
            ck(e in E and w>=0,'bad allocated edge/weight')
            if kind=='a':ck(set(e)<=A,'short edge escaped actual subset')
            load[e]+=w
            for v in e:(da if kind=='a' else db)[v]+=w
    ck(all(w<=1 for w in load.values()),'core ownership conflict')
    ck(all(da[v]<=p for v in A),'short endpoint overloaded')
    ck(all(db[v]<=q for v in range(r)),'long endpoint overloaded')
    value=F(len(P))+sum(al.values())+sum(be.values())
    sc=sum(1-load[e] for e in E)
    sa=sum(p-da[v] for v in A);sb=sum(q-db[v] for v in range(r))
    upper=F(len(E)+len(A)*p+r*q,3)
    ck(sc+sa+sb==3*(upper-value),'one-third objective identity')
    if claimed is not None:ck(value==claimed,'claimed objective mismatch')
    return {'value':str(value),'uniform_upper':str(upper),'core_slack':str(sc),'short_slack':str(sa),'long_slack':str(sb),'total_slack':str(sc+sa+sb),'gap_to_uniform_upper':str(upper-value)}

def build(r,A,p,q,full=False):
    A=sorted(set(A));C=sorted(set(range(r))-set(A));a=len(A);c=len(C)
    ck(a>=1 and c>=1 and q>=max(a,c),'outside proper high-long region')
    ck(0<=p<=a-1 and p+q<=r-1,'invalid endpoint bounds')
    d=r-1-q;s=d-p;a0=good(a);c0=good(c)
    AA=A[:a0];CC=C[:c0];eA=a-a0;eC=c-c0;e=eA+eC
    hA=2*(min(s,a0-1)//2) if a0 else 0
    hC=2*(min(d,c0-1)//2) if c0 else 0
    p0=min(p,a0-1-hA) if a0 else 0
    P=[]
    for block,h in [(AA,hA),(CC,hC)]:
        for row in factors(len(block),h//2):
            P.extend(tuple(sorted(block[v] for v in T)) for T in row)
    used={e for T in P for e in ep(T)}
    ck(len(used)==3*len(P),'initial core packing conflict')
    al={};be={};den=a0-1-hA
    aa=set(AA);vv=sorted(AA+CC)
    for ed in it.combinations(vv,2):
        if ed in used:continue
        w=F(p0,den) if den>0 and set(ed)<=aa else F(0)
        if w:al[ed]=w
        if w<1:be[ed]=1-w
    deg=collections.Counter()
    for ed,w in be.items():
        for v in ed:deg[v]+=w
    ck(max((deg[v]-q for v in range(r)),default=0)<=1,'overload estimate')
    charges=collections.Counter();trace=[]
    for v in range(r):
        excess=max(F(0),deg[v]-q)
        if not excess:continue
        for ed in sorted(be):
            if v not in ed or not be[ed]:continue
            drop=min(excess,be[ed]);be[ed]-=drop;excess-=drop;charges[v]+=drop
            for u in ed:deg[u]-=drop
            trace.append([v,list(ed),str(drop)])
            if not excess:break
        ck(excess==0,'failed overload trimming')
    ck(all(t<=1 for t in charges.values()) and sum(charges.values())<=r,'repair charge')
    be={ed:w for ed,w in be.items() if w}
    vals=check_point(r,A,p,q,P,al,be)
    ck(F(vals['total_slack'])<=38*r,'linear capacity bound')
    out={'r':r,'a':a,'c':c,'p':p,'q':q,'good_sizes':[a0,c0],'exceptions':e,'core_degrees':[hA,hC],'retained_short_degree':p0,'repair_mass':str(sum(charges.values())),**vals}
    if full:out.update({'actual_short_subset':A,'core_triangles':P,'alpha':[[list(ed),str(w)] for ed,w in sorted(al.items())],'beta':[[list(ed),str(w)] for ed,w in sorted(be.items())],'repair_trace':trace,'maximal_cliques_schema':{'short':[A,'one distinct short leaf per clique'],'long':[list(range(r)),'one distinct long leaf per clique']}})
    return out

def interval(r,a,p,q):
    c=r-a;ck(a>=3 and c>=3,'scalar formula small-class restriction')
    d=r-1-q;s=d-p
    lo=max(F(0),F(a*(c-q),2),F(c*(a-q),2))
    hi=min(F(a*c,2),F(a*s,2),F(c*d,2),F(a*s+c*d,6))
    return p<=a-1 and s>=0 and lo<=hi,lo,hi

def type_model(r,a,p,q):
    c=r-a;caps=[a*(a-1)//2,a*c,c*(c-1)//2,a*p,a*q,c*q]
    objects=[('AAA',[3,0,0,0,0,0],a>=3),('AAC',[1,2,0,0,0,0],a>=2 and c>=1),('ACC',[0,2,1,0,0,0],a>=1 and c>=2),('CCC',[0,0,3,0,0,0],c>=3),('alpha',[1,0,0,2,0,0],a>=2),('betaAA',[1,0,0,0,2,0],a>=2),('betaAC',[0,1,0,0,1,1],a>=1 and c>=1),('betaCC',[0,0,1,0,0,2],c>=2)]
    labels=[name for name,col,on in objects if on];cols=[col for name,col,on in objects if on]
    return labels,[list(row) for row in zip(*cols)] if cols else [[] for _ in caps],caps

def load_dep():
    p=pathlib.Path(__file__).resolve().parents[1]/'c25'/'extreme_audit.py'
    ck(p.is_file() and sha(p)==DEP_SHA,'frozen C25 dependency mismatch')
    spec=importlib.util.spec_from_file_location('c28_prior_exact',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.DEADLINE=DEADLINE
    return m

def lp_mode(include_full=False):
    ex=load_dep();counts=[];rows=[];full_checks=[]
    for r in range(6,11):
        count=0
        for a in range(3,r-2):
            for p in range(a):
                for q in range(r):
                    tick();labels,M,B=type_model(r,a,p,q)
                    v,x,y=ex.lp_tableau(M,B);vv,xx,yy=ex.lp_revised(M,B)
                    ex.validate(M,B,v,x,y);ex.validate(M,B,vv,xx,yy);ck(v==vv,'rational LP disagreement')
                    yes,lo,hi=interval(r,a,p,q);upper=F(sum(B),3)
                    ck(yes==(v==upper),'scalar face criterion mismatch')
                    rows.append([r,a,p,q,int(yes),str(v)]);count+=1
        counts.append([r,count])
    if not include_full:
        return {'complete_scalar_ranges':counts,'rows':rows,'complete_full_edge_range':None,'Q_optimized':False}
    named=[(6,3,0,0),(6,3,2,0),(7,3,1,1),(8,3,1,1),(9,4,1,1),(9,5,4,0),(9,4,2,5)]
    for r,a,p,q in named:
        tick();E,l,M,B=ex.model(r,a,r,p,q)
        v,x,y=ex.lp_tableau(M,B);vv,xx,yy=ex.lp_revised(M,B)
        ex.validate(M,B,v,x,y);ex.validate(M,B,vv,xx,yy);ck(v==vv,'full LP mismatch')
        names,TM,TB=type_model(r,a,p,q);tv,_,_=ex.lp_tableau(TM,TB);ck(v==tv,'projection mismatch')
        full_checks.append({'parameters':[r,a,r,p,q],'L':str(v),'uniform_upper':str(F(sum(B),3)),'positive_primal':[{'kind':kind,'vertices':t,'weight':str(w)} for (kind,t),w in zip(l,x) if w],'dual':[str(w) for w in y]})
    return {'complete_scalar_ranges':counts,'rows':rows,'named_full_edge_checks':full_checks,'complete_full_edge_range':None,'Q_optimized':False}

def named_mode():
    ex=load_dep();out=[]
    for r,a,p,q in [(3,3,1,1),(3,0,0,1),(6,3,0,0),(6,3,2,0),(7,3,1,1)]:
        tick();E,l,M,B=ex.model(r,a,r,p,q)
        v,x,y=ex.lp_tableau(M,B);vv,xx,yy=ex.lp_revised(M,B)
        ex.validate(M,B,v,x,y);ex.validate(M,B,vv,xx,yy);ck(v==vv,'named full LP disagreement')
        names,TM,TB=type_model(r,a,p,q);tv,_,_=ex.lp_tableau(TM,TB);ck(v==tv,'type/full mismatch')
        out.append({'parameters':[r,a,r,p,q],'L':str(v),'uniform_upper':str(F(sum(B),3)),'positive_primal':[{'kind':kind,'vertices':t,'weight':str(w)} for (kind,t),w in zip(l,x) if w],'dual':[str(w) for w in y]})
    # Lift a separately solved type optimum to an exact full nonextreme certificate.
    r,a,p,q=9,4,1,1;c=r-a
    names,TM,TB=type_model(r,a,p,q);v,tx,ty=ex.lp_tableau(TM,TB);vv,_,_=ex.lp_revised(TM,TB);ck(v==vv,'lift LP mismatch')
    masses=dict(zip(names,tx)); E,l,M,B=ex.model(r,a,r,p,q);nobj=collections.Counter()
    def kind(label):
        k,vs=label
        if k=='z':return 'A'*sum(u<a for u in vs)+'C'*sum(u>=a for u in vs)
        if k=='a':return 'alpha'
        return 'beta'+'A'*sum(u<a for u in vs)+'C'*sum(u>=a for u in vs)
    for label in l:nobj[kind(label)]+=1
    x=[masses[kind(label)]/nobj[kind(label)] for label in l]
    y=[ty[0] if v<a else ty[1] if u<a else ty[2] for u,v in E]+[ty[3]]*a+[ty[4] if u<a else ty[5] for u in range(r)]
    ck(all(w>=0 for w in x+y),'negative lifted certificate')
    ck(all(ex.dot(row,x)<=b for row,b in zip(M,B)),'lifted primal overload')
    ck(all(ex.dot(y,col)>=1 for col in zip(*M)),'lifted dual undercoverage')
    ck(sum(x)==ex.dot(y,B)==v==F(49,3),'lifted value mismatch')
    # Revalidate frozen input points, not their Q optima. No old support is retained.
    scope=[]
    E,l,M,B=ex.model(5,2,4,1,1)
    old={('z',(0,1,4)):F(1,2),('z',(0,2,3)):F(1,4),('z',(0,2,4)):F(1,2),
         ('z',(1,2,3)):F(1,4),('z',(1,3,4)):F(1,2),('z',(2,3,4)):F(1,2),
         ('a',(0,1)):F(1,2),('b',(0,2)):F(1,4),('b',(0,3)):F(3,4),
         ('b',(1,2)):F(3,4),('b',(1,3)):F(1,4)}
    ox=[old.get(z,F(0)) for z in l];oy=[F(0)]*len(B)
    for e in [(0,1),(0,3),(1,3),(2,4)]:oy[E.index(e)]=1
    oy[len(E)+2+2]=1;ex.validate(M,B,F(5),ox,oy)
    scope.append({'parameters':[5,2,4,1,1],'value':'5','uniform_upper':'16/3','on_face':False,'rank':11})
    tpath=pathlib.Path(__file__).resolve().parents[1]/'c27'/'twelfth-point.json'
    tsha='f25f6b06d50933b500e5c0433fd9b1af90e1228381201437b2341e49bd6687ef'
    ck(tpath.is_file() and sha(tpath)==tsha,'frozen twelfth input mismatch')
    frozen=json.loads(tpath.read_text());E,l,M,B=ex.model(*frozen['params'])
    vals={(z['kind'],tuple(z['vertices'])):F(z['weight']) for z in frozen['positive']}
    fx=[vals.get(z,F(0)) for z in l];fy=[F(1,3)]*len(B)
    ex.validate(M,B,F(31,3),fx,fy)
    ck(all(ex.dot(row,fx)==rhs for row,rhs in zip(M,B)),'twelfth row not saturated')
    scope.append({'parameters':frozen['params'],'value':'31/3','uniform_upper':'31/3','on_face':True,
                  'rank':28,'source_sha256':tsha,'denominators':sorted({z.denominator for z in fx if z}),'Q_optimized':False})
    return {'frozen_scope_regressions':scope,'named_two_full_LP_cases':out,'lifted_open_case':{'parameters':[9,4,9,1,1],'L':str(v),'type_totals':{k:str(t) for k,t in masses.items()},'type_dual':[str(t) for t in ty],'full_primal_and_dual_checked':True,'Q_optimized':False},'complete_parameter_range':None}

def construct_mode():
    counts=[];max_ratio=F(0);digest=hashlib.sha256();total=0
    for r in (3,9,27):
        count=0
        for a in range(1,r):
            # Arbitrary actual labels, not an affine-prefix promise.
            perm=sorted(range(r),key=lambda i:((7*i+3)%r,i));A=perm[:a]
            for q in range(max(a,r-a),r):
                for p in range(min(a-1,r-1-q)+1):
                    tick();row=build(r,A,p,q)
                    max_ratio=max(max_ratio,F(row['total_slack'])/r)
                    digest.update((json.dumps(row,sort_keys=True)+'\n').encode());count+=1
        counts.append([r,count]);total+=count
    subset_count=0
    r=9
    for mask in range(1,(1<<r)-1):
        A=[u for u in range(r) if mask>>u&1];a=len(A)
        for q in range(max(a,r-a),r):
            for p in range(min(a-1,r-1-q)+1):
                tick();row=build(r,A,p,q);subset_count+=1
    large=[]
    for r,a,p,q in [(81,35,8,70),(81,40,8,70),(243,100,20,200)]:
        perm=sorted(range(r),key=lambda i:((17*i+11)%r,i));large.append(build(r,perm[:a],p,q))
    # Auxiliary non-power-of-three orders exercise genuine beta-overload shaving.
    repair_controls=[]
    for rr,aa,pp,qq in [(6,3,1,3),(18,9,1,9),(30,15,3,17)]:
        control=build(rr,list(range(aa)),pp,qq,True)
        ck(F(control['repair_mass'])>0,'repair control did not shave beta')
        ck(F(control['total_slack'])<=2*rr,'zero-exception sharper bound')
        repair_controls.append(control)
    witness=build(27,[i for i in range(27) if i%2==0],4,18,True)
    mutation=mutations(witness)
    return {'complete_cardinality_ranges':counts,'cardinality_representations':total,'all_nonempty_proper_subsets_order9':510,'subset_budget_cases_order9':subset_count,'deterministic_rows_sha256':digest.hexdigest(),'maximum_total_slack_over_r':str(max_ratio),'named_large_cases':large,'auxiliary_repair_controls':repair_controls,'explicit_witness':witness,'mutations':mutation,'KTS_existence_theorem_executed':False,'missing_schedule_cases_in_asserted_ranges':0}

def mutations(w):
    r=w['r'];A=w['actual_short_subset'];p=w['p'];q=w['q'];P=[tuple(t) for t in w['core_triangles']]
    al={tuple(e):F(x) for e,x in w['alpha']};be={tuple(e):F(x) for e,x in w['beta']};res=[]
    def reject(name,fn):
        try:fn()
        except (ValueError,AssertionError,LookupError):res.append(name)
        else:raise ValueError('undetected mutation '+name)
    reject('01_duplicate_core_triangle',lambda:check_point(r,A,p,q,P+[P[0]],al,be))
    bad=al.copy();bad[ep(P[0])[0]]=1
    reject('02_shared_core_capacity',lambda:check_point(r,A,p,q,P,bad,be))
    bad=al.copy();bad[next(iter(al))]=-1
    reject('03_negative_fraction',lambda:check_point(r,A,p,q,P,bad,be))
    outside=next(e for e in edges(r) if not set(e)<=set(A));bad=al.copy();bad[outside]=F(1,10)
    reject('04_short_subset_escape',lambda:check_point(r,A,p,q,[],bad,{}))
    reject('05_loop_triple',lambda:check_point(r,A,p,q,[(0,0,1)],{},{}))
    bad={e:F(1) for e in edges(r)}
    reject('06_long_budget_ignored',lambda:check_point(r,A,p,q,[],{},bad))
    reject('07_wrong_objective',lambda:check_point(r,A,p,q,P,al,be,F(w['value'])+1))
    rows=factors(9,1)
    reject('08_duplicate_factor',lambda:validate_factors(9,rows+rows))
    reject('09_invalid_factor_partition',lambda:validate_factors(9,[rows[0][:-1]]))
    reject('10_unsupported_resolution_not_success',lambda:factors(21,10))
    reject('11_face_necessary_conditions_suffice',lambda:ck(interval(9,5,4,0)[0],'off-face'))
    reject('12_scalar_small_class_domain',lambda:interval(9,2,1,1))
    return res

def main():
    global DEADLINE
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=['construct','types','named'],required=True);parser.add_argument('--out',type=pathlib.Path,required=True);args=parser.parse_args()
    start=time.monotonic();DEADLINE=start+38
    resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824));resource.setrlimit(resource.RLIMIT_CPU,(40,41))
    payload={'construct':construct_mode,'types':lp_mode,'named':named_mode}[args.mode]()
    out={'version':VERSION,'verdict':'candidate_only','best_verified_result':'none','trusted_verifier_run':False,'status':'finite_checks_passed','mode':args.mode,**payload,'runtime':{'python':platform.python_version(),'arithmetic':'Fraction/integer','threads':1,'memory_limit_bytes':1073741824,'wall_limit_seconds':38,'cpu_limit_seconds':40,'elapsed_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_sha256':sha(__file__)},'limitations':['The whole arbitrary-subset face is not proved.','Only claimed finite ranges are executed; input K is source-backed, not verified here.','No Q optimum is claimed on the named seven-core extreme point.','Both LP implementations share this generator trust domain.']}
    raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();ck(len(raw)<1048576,'output budget')
    with args.out.open('xb') as f:f.write(raw)
    print(json.dumps({'status':out['status'],'mode':args.mode,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'seconds':out['runtime']['elapsed_seconds']}))
if __name__=='__main__':main()
