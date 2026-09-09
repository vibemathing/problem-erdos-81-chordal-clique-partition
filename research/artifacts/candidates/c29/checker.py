"""C29 exact witnesses; generator-side checks, not a trusted verifier.
Usage: python checker.py --mode nine|oneone|lift|mutations --out NEW.json
Only mode nine imports the immutable C25 rational LP module from this repository.
"""
from __future__ import annotations
import argparse, collections, hashlib, importlib.util, itertools as it, json
import pathlib, platform, resource, time
from fractions import Fraction as F
from functools import lru_cache
VERSION='c29-mixed-repacking-v5'
DEP='bcee9e8a3d427059c5a10b9e3ce893ec1ae674f58feec3b10333e18ad8984c49'
ROOT=pathlib.Path(__file__).resolve().parent
DEADLINE=float('inf')
P9=[(0,2,6),(0,3,7),(0,4,8),(1,3,8),(1,4,6),(1,5,7),(2,4,7),(2,5,8),(3,5,6)]
A9={2:{0,1},3:{6,7,8},4:{0,1,2,3},5:{0,1,6,7,8},6:set(range(6)),7:{0,1,2,3,6,7,8},8:set(range(8)),9:set(range(9))}
def ck(ok,msg):
    if not ok:raise ValueError(msg)
def tick():
    if time.monotonic()>DEADLINE:raise TimeoutError('bounded exact checker deadline')
def edge(u,v):return tuple(sorted((u,v)))
def edges(t):return tuple(it.combinations(sorted(t),2))
def cycle(vs):return {edge(vs[i],vs[(i+1)%len(vs)]) for i in range(len(vs))}
def point(P=(),alpha=None,beta=None):
    return {'z':{tuple(sorted(t)):F(1) for t in P},'a':dict(alpha or {}),'b':dict(beta or {})}
def audit(r,A,p,q,x,integral=True):
    tick();A=set(A);ck(A<=set(range(r)),'short set out of core')
    ck(p>=0 and q>=0,'negative budget')
    load=collections.defaultdict(F); da=collections.defaultdict(F);db=collections.defaultdict(F)
    for t,w in x['z'].items():
        ck(len(t)==3 and len(set(t))==3 and all(0<=u<r for u in t),'invalid triangle')
        ck(w>=0 and (not integral or w.denominator==1),'nonintegral core')
        for e in edges(t):load[e]+=w
    for kind,d in [('a',da),('b',db)]:
        for e,w in x[kind].items():
            ck(len(e)==2 and e[0]<e[1] and 0<=e[0]<e[1]<r and w>=0,'invalid leaf edge')
            ck(kind!='a' or set(e)<=A,'short edge outside short set')
            load[e]+=w
            for u in e:d[u]+=w
    ck(all(0<=w<=1 for w in load.values()),'core edge overload')
    ck(all(da[u]<=p for u in A) and all(db[u]<=q for u in range(r)),'endpoint overload')
    M=r*(r-1)//2; Z=sum(x['z'].values(),F());U=sum(x['a'].values(),F())+sum(x['b'].values(),F())
    S0=F(M)-3*Z-U;SX=F(len(A)*p)-2*sum(x['a'].values(),F());SY=F(r*q)-2*sum(x['b'].values(),F())
    L=F(M+len(A)*p+r*q,3)
    ck(min(S0,SX,SY)>=0 and 3*(L-Z-U)==S0+SX+SY,'slack identity')
    mismatch=sum((r-1-(p+q if u in A else q))%2 for u in range(r))
    if integral:ck(S0+SX+SY>=F(mismatch,2),'parity capacity lower bound')
    return {'value':str(Z+U),'uniform_bound':str(L),'core_triangles_mass':str(Z),'leaf_mass':str(U),'S_core':str(S0),'S_short':str(SX),'S_long':str(SY),'S_total':str(S0+SX+SY),'parity_mismatches':mismatch}
def serial_point(x):
    return {k:[[list(e),str(w)] for e,w in sorted(x[k].items()) if w] for k in ('z','a','b')}
def base_q(a):
    A=A9[a];x=point(P9); C6=cycle(range(6));C3=cycle([6,7,8])
    if a in (2,4,5,7):
        short4={0,1,2,3}<=A
        x['a'][(0,1)]=F(1)
        if short4:x['a'][(2,3)]=F(1)
        for e in [(1,2),(3,4),(0,5)]:x['b'][e]=F(1)
        for e in C3:
            x['b'][e]=F(1,2)
            if {6,7,8}<=A:x['a'][e]=F(1,2)
    elif a in (3,6,9):
        for e in C6|C3:
            x['b'][e]=F(1,2)
            if set(e)<=A:x['a'][e]=F(1,2)
    elif a==8:
        for e in C6:x['a'][e]=x['b'][e]=F(1,2)
        x['a'][(6,7)]=F(1);x['b'][(6,8)]=x['b'][(7,8)]=F(1,2)
    return x

def base_full(a):
    """Fractional decomposition of K_10 plus the short vertex; all host edges saturated."""
    A=A9[a];D=(set(range(9))-A)|{10};d=len(D)
    if d>=a+1:
        aa=F(1,a-1) if a>=3 else F(0);ab=F(0);ac=F(1,d-1);cc=(1-a*ac)/(d-2)
    elif d>=3 and a<=d+2:
        aa=F(0);ab=F(a-2,d*(a-1));ac=(1-(a-1)*ab)/(d-1);cc=(1-a*ac)/(d-2)
    elif d>=3:
        ab=F(1,a-1);ac=F(0);aa=F(a-2-d,(a-1)*(a-2));cc=F(1,d-2)
    elif d==2:
        ac=ab=F(1,a);aa=(F(a-2,a-1)-2*ab)/(a-2);cc=F(0)
    else:
        ab=F(1,a-1);aa=F(a-3,(a-1)*(a-2));ac=cc=F(0)
    ck(min(aa,ab,ac,cc)>=0,'negative type witness')
    x=point()
    for e in it.combinations(sorted(A),2):x['a'][e]=F(1,a-1)
    for t in it.combinations(list(range(9))+[10],3):
        j=sum(v in A for v in t);w=[cc,ac,ab,aa][j]
        if w:
            if 10 in t:x['b'][tuple(v for v in t if v!=10)]=w
            else:x['z'][t]=w
    report=audit(9,A,1,1,x,False);ck(report['S_total']=='0','base full witness not saturated')
    return x

@lru_cache(None)
def fadd(u,v,k):
    out=0;place=1
    for _ in range(k):out+=((u%3+v%3)%3)*place;u//=3;v//=3;place*=3
    return out
@lru_cache(None)
def fneg(u,k):
    out=0;place=1
    for _ in range(k):out+=((-u%3)%3)*place;u//=3;place*=3
    return out
@lru_cache(None)
def affine_lines(k):
    n=3**k;out=[]
    for u,v in it.combinations(range(n),2):
        w=fneg(fadd(u,v,k),k)
        if v<w:out.append((u,v,w))
    ck(len(out)==n*(n-1)//6,'affine line count')
    return tuple(out)
@lru_cache(None)
def line_factors(k):
    n=3**k;D=collections.defaultdict(list)
    for t in affine_lines(k):
        diff=fadd(t[1],fneg(t[0],k),k);direction=min(diff,fneg(diff,k))
        D[direction].append(t)
    ck(len(D)==(n-1)//2,'direction count')
    for factor in D.values():ck(sorted(v for t in factor for v in t)==list(range(n)),'not a parallel class')
    return tuple(tuple(D[d]) for d in sorted(D))

def oneone(k,a,full=False):
    r=3**k;ck(k>=2 and 2<=a<=r,'one-one domain')
    a0=next(t for t in range(2,10) if t<=a and 9-t<=r-a and (a-t)%3==0)
    A=set(A9[a0]);need=(a-a0)//3
    for j in range(9,r,3):
        if need:A.update(range(j,j+3));need-=1
    ck(not need and len(A)==a,'anchor color count')
    parallel={tuple(range(j,j+3)) for j in range(0,r,3)}
    P=[t for t in affine_lines(k) if t not in parallel and not all(v<9 for v in t)]
    x=point(P);base=base_full(a0) if full else base_q(a0)
    for kind in x:x[kind].update(base[kind])
    for j in range(9,r,3):
        t=(j,j+1,j+2)
        for e in edges(t):
            x['b'][e]=F(1,2)
            if j in A:x['a'][e]=F(1,2)
        if full and j not in A:x['z'][t]=F(1,2)
    return A,x

def permute_point(x,pi):
    return {kind:{tuple(sorted(pi[v] for v in e)):w for e,w in data.items()} for kind,data in x.items()}

def lift(h,xtra,ytra,full=False):
    seed=json.loads((ROOT/'seed27.json').read_text());m=3**h;r=27*m;a=12*m
    ck(xtra>=0 and ytra>=0 and xtra+ytra<=m-1,'extra-budget domain')
    pt=point();A=set(range(a))
    for u,v,w in seed['core_triangles']:
        for i in range(m):
            for j in range(m):
                z=fneg(fadd(i,j,h),h)
                pt['z'][(u*m+i,v*m+j,w*m+z)]=F(1)
    for kind,key in [('a','alpha_edges'),('b','beta_edges')]:
        for u,v in seed[key]:
            for i in range(m):
                for j in range(m):pt[kind][(u*m+i,v*m+j)]=F(1)
    for u in range(27):
        total=xtra+ytra if u<12 else ytra
        remaining=F(total,2)
        for factor in line_factors(h):
            take=min(F(1),remaining);remaining-=take
            for tt in factor:
                t=tuple(u*m+i for i in tt)
                if take<1 and (full or take==0):pt['z'][t]=1-take
                for e in edges(t):
                    if u<12:
                        if total:
                            if xtra and take:pt['a'][e]=take*F(xtra,total)
                            if ytra and take:pt['b'][e]=take*F(ytra,total)
                    elif take:pt['b'][e]=take
        ck(remaining==0,'insufficient directions')
    return r,A,2*m+xtra,2*m+ytra,pt

def load_exact():
    dep=ROOT.parent/'c25'/'extreme_audit.py';raw=dep.read_bytes()
    ck(hashlib.sha256(raw).hexdigest()==DEP,'changed rational dependency')
    spec=importlib.util.spec_from_file_location('c29_frozen_lp',dep);ex=importlib.util.module_from_spec(spec);spec.loader.exec_module(ex)
    ex.DEADLINE=DEADLINE;return ex

def nine_mode():
    ex=load_exact();E,labels,fullM,fullB=ex.model(9,4,9,1,1)
    # Exact symmetry quotient, verified separately by lifting the explicit full primal.
    columns=[(3,0,0,0,0,0),(1,2,0,0,0,0),(0,2,1,0,0,0),(0,0,3,0,0,0),(1,0,0,2,0,0),(1,0,0,0,2,0),(0,1,0,0,1,1),(0,0,1,0,0,2)]
    M=list(map(list,zip(*columns)));B=[6,20,10,4,4,5]
    reports=[]
    for fn in (ex.lp_tableau,ex.lp_revised):
        v,x,y=fn(M,B);ex.validate(M,B,v,x,y);ck(v==F(49,3),'full L')
        reports.append({'implementation':fn.__name__,'objective':str(v),'positive_columns':sum(bool(z) for z in x)})
    q=base_q(4);z=audit(9,A9[4],1,1,q);ck(z['value']=='31/2' and z['S_total']=='5/2','nine Q witness')
    used={e for t in P9 for e in edges(t)};free=sum(1<<i for i,e in enumerate(E) if e not in used)
    E,ll,m,b=ex.model(9,4,9,1,1,free,False)
    # Zero-capacity rows force their nonnegative incident columns to zero.
    cols=[j for j in range(len(ll)) if not any(row[j] and rhs==0 for row,rhs in zip(m,b))]
    live=[i for i,rhs in enumerate(b) if rhs>0]
    m=[[m[i][j] for j in cols] for i in live];b=[b[i] for i in live]
    leaf=[]
    for fn in (ex.lp_tableau,ex.lp_revised):
        v,x,y=fn(m,b);ex.validate(m,b,v,x,y);ck(v==F(13,2),'residual LP')
        leaf.append({'implementation':fn.__name__,'objective':str(v),'dual':[str(w) for w in y]})
    host=set(it.combinations(range(9),2))|{(u,9) for u in range(4)}|{(u,10) for u in range(9)}
    packing=P9+[(0,1,9),(2,3,9),(1,2,10),(3,4,10),(0,5,10),(6,7,10)]
    counts=collections.Counter(e for t in packing for e in edges(t));ck(max(counts.values())==1 and set(counts)<=host,'integer packing')
    leave=host-set(counts);odd={u for u in range(11) if sum(u in e for e in host)%2}
    ck(len(packing)==15 and len(leave)==4 and len(odd)==6 and len(host)%3==1,'integer parity certificate')
    part=[list(range(9))+[10]]+[[u,9] for u in range(4)]
    ck(collections.Counter(e for t in part for e in edges(t))==collections.Counter(host),'cp partition')
    full=base_full(4);audit(9,A9[4],1,1,full,False)
    # Named ranks are scope regressions, not new counterexamples or Q computations.
    tp=ROOT.parent/'c27'/'twelfth-point.json';ck(hashlib.sha256(tp.read_bytes()).hexdigest()=='f25f6b06d50933b500e5c0433fd9b1af90e1228381201437b2341e49bd6687ef','twelfth digest')
    data=json.loads(tp.read_text());ee,ll,mm,bb=ex.model(*data['params']);chosen={(z['kind'],tuple(z['vertices'])):F(z['weight']) for z in data['positive']}
    xx=[chosen.get(k,F()) for k in ll];ex.validate(mm,bb,F(31,3),xx,[F(1,3)]*len(bb))
    ee,ll,mm,bb=ex.model(5,2,4,1,1);v,xx,yy=ex.lp_tableau(mm,bb);ex.validate(mm,bb,v,xx,yy);ck(v==5<F(16,3),'quarter scope')
    return {'L':'49/3','Q':'31/2','J':15,'nu':15,'cp':5,'host_vertices':11,'core_order':9,'full_value_type_LPs':reports,'residual_LP':leaf,'Q_witness':serial_point(q),'full_primal':serial_point(full),'Q_upper_certificate':'General parity-capacity inequality gives L-Q >= 5/6, matching this witness. No global Q branch-and-bound is assumed.','integer_packing':packing,'integer_leave':sorted(leave),'odd_vertices':sorted(odd),'clique_partition':part,'maximal_cliques':[list(range(9))+[10],[0,1,2,3,9]],'cp_lower_certificate':'Restriction to the K10: without a full K10 block, all ten incidence rows have diagonal >=2 and pair inner product 1, so rank is 10; with it, four short edges need four separate blocks.','scope_regressions':{'quarter':'outside uniform face; no half-integrality assumed','twelfth':'rank28 inside uniform face; no new Q optimum computed'}}

def oneone_mode():
    rows=[]
    for k in (2,3,4):
        r=3**k
        for a in range(2,r+1):
            A,z=oneone(k,a);out=audit(r,A,1,1,z)
            AA,x=oneone(k,a,True);full=audit(r,AA,1,1,x,False);ck(full['S_total']=='0','oneone full')
            target=F(0) if a==r else F(2) if a==r-1 else F(r-a,2)
            ck(F(out['S_total'])==target,'oneone optimal slack formula')
            rows.append([r,a,out['value'],out['S_total']])
    for a in (2,4,5,7,100,200,241,242,243):
        A,z=oneone(5,a);out=audit(243,A,1,1,z)
        target=F(0) if a==243 else F(2) if a==242 else F(243-a,2)
        ck(F(out['S_total'])==target,'named larger oneone')
    # Every proper short subset on nine core vertices, by an explicit bijection.
    relabel=0
    for mask in range(1<<9):
        a=mask.bit_count()
        if a<2:continue
        target={u for u in range(9) if mask>>u&1};A,z=oneone(2,a)
        pi=dict(zip(sorted(A)+sorted(set(range(9))-A),sorted(target)+sorted(set(range(9))-target)))
        out=audit(9,target,1,1,permute_point(z,pi));relabel+=1
    return {'complete_cardinality_ranges':[{'r':3**k,'a_min':2,'a_max':3**k,'cases':3**k-1} for k in (2,3,4)],'rows':rows,'named_larger_cases':9,'actual_nine_subsets':relabel,'maximum_core_order':243,'generality_basis':'Proof and fixed nine-core seed, not finite extrapolation','boundary_c1':'The stronger capacity/count argument in proof.md, not parity alone, proves optimality.'}

def lift_mode():
    seed=json.loads((ROOT/'seed27.json').read_text());s=point(seed['core_triangles'],{tuple(e):F(1) for e in seed['alpha_edges']},{tuple(e):F(1) for e in seed['beta_edges']})
    out=audit(27,range(12),2,2,s);ck(out['S_total']=='0' and out['value']=='143','seed not saturated')
    hostpack=list(map(tuple,seed['core_triangles']))
    for vs in seed['alpha_cycles']:
        for i in range(len(vs)):hostpack.append(tuple(sorted((vs[i],vs[(i+1)%len(vs)],27+i%2))))
    for vs in seed['beta_cycles']:
        for i in range(len(vs)-(len(vs)%2)):hostpack.append(tuple(sorted((vs[i],vs[(i+1)%len(vs)],29+i%2))))
    host=set(it.combinations(range(27),2))|{(u,v) for u in range(12) for v in (27,28)}|{(u,v) for u in range(27) for v in (29,30)}
    hh=collections.Counter(e for t in hostpack for e in edges(t))
    ck(len(hostpack)==142 and max(hh.values())==1 and set(hh)<=host and len(host-set(hh))==3,'seed actual packing')
    odd={u for u in range(31) if sum(u in e for e in host)%2};ck(odd=={29,30} and len(host)%3==0,'seed nu upper parity')
    counts=collections.Counter(sum(u<12 for u in t) for t in s['z'])
    ps={tuple(sorted((1-u if u in (0,1) else u) for u in t)) for t in s['z']}
    change=len(set(s['z'])-ps);ck(change==20,'seed swap count')
    cases=[(0,0,0)]+[(1,x,y) for x in range(3) for y in range(3-x)]
    cases += [(2,x,y) for x,y in [(0,0),(0,8),(8,0),(1,1),(3,5),(4,4),(2,3),(7,1)]]
    rows=[]
    for h,x,y in cases:
        r,A,p,q,pt=lift(h,x,y);rep=audit(r,A,p,q,pt)
        rr,AA,pp,qq,full=lift(h,x,y,True);f=audit(rr,AA,pp,qq,full,False)
        expected=F(len(A)*((x+y)%2)+(r-len(A))*(y%2),2)
        ck(f['S_total']=='0' and F(rep['S_total'])==expected and expected<=F(r,2) and rep['S_short']==rep['S_long']=='0','lift saturation/slack')
        ck(q<max(len(A),r-len(A)) and p+q>F(r,20),'new low-budget outside dense region')
        if h==1 and x==y==0:
            m=3;pi={u:(1-u//m if u//m in (0,1) else u//m)*m+u%m for u in range(r)}
            swapped=permute_point(pt,pi);rep2=audit(r,A,p,q,swapped)
            changed=len(set(pt['z'])-set(swapped['z']))
            ck(rep2['value']==rep['value'] and changed==20*m*m,'global objective-preserving exchange')
        if h==1 and x==y==1:
            pi={u:(7*u+5)%r for u in range(r)};otherA={pi[u] for u in A}
            rr=audit(r,otherA,p,q,permute_point(pt,pi));ck(rr['value']==rep['value'],'actual-subset relabeling')
        rows.append({'r':r,'a':len(A),'p':p,'q':q,'extras':[x,y],**rep})
    return {'seed':out,'actual_seed_nu':142,'actual_seed_leave':sorted(host-set(hh)),'seed_core_types':{str(k):v for k,v in sorted(counts.items())},'cases':rows,'complete_extra_ranges':[{'fiber_order':1,'cases':1},{'fiber_order':3,'cases':6}],'named_fiber9_cases':8,'zero_loss_exchange':{'r':81,'old_core_triangles_changed':180,'objective_change':'0','general_change_formula':'20*m^2; m=3^h'},'large_general_statement':'r=27m,a=12m,p=2m+x,q=2m+y; x,y>=0,x+y<=m-1; m=3^h; exact L-Q=[a*((x+y)%2)+(r-a)*(y%2)]/6; S<=r/2.'}

def mutations_mode():
    rejected=[]
    def reject(name,fn):
        try:fn()
        except (AssertionError,ValueError) as e:rejected.append({'name':name,'reason':str(e)})
        else:raise ValueError('undetected mutation '+name)
    base=base_q(4)
    def copy():return {k:dict(d) for k,d in base.items()}
    x=copy();x['z'][P9[0]]=2;reject('01_duplicate_core_triangle',lambda:audit(9,A9[4],1,1,x))
    x=copy();x['a'][(4,5)]=1;reject('02_short_edge_outside_A',lambda:audit(9,A9[4],1,1,x))
    x=copy();x['b'][(6,7)]=F(3,2);reject('03_core_capacity_overload',lambda:audit(9,A9[4],1,1,x))
    x=copy();x['b'][(4,5)]=F(1);reject('04_long_endpoint_overload',lambda:audit(9,A9[4],1,1,x))
    x=copy();x['z'][P9[0]]=F(1,2);reject('05_fractional_core_in_Q',lambda:audit(9,A9[4],1,1,x))
    x=copy();x['a'][(0,1)]=-1;reject('06_negative_allocation',lambda:audit(9,A9[4],1,1,x))
    reject('07_zero_short_count_with_positive_alpha',lambda:audit(9,A9[4],0,1,base))
    reject('08_parity_floor_ignored',lambda:ck(F(49,3)-F(31,2)==0,'gap is 5/6, not zero'))
    reject('09_omitted_endpoint_slack',lambda:ck(audit(9,A9[8],1,1,base_q(8))['S_total']=='1','c=1 has core and endpoint loss'))
    reject('10_bad_fiber_budget',lambda:lift(1,2,2))
    reject('11_Q_is_actual_integer_packing',lambda:ck(F(31,2)==15,'Q differs from nu'))
    reject('12_arbitrary_twofactor_completion',lambda:ck(20<=2*9,'K9-(C4+C5) has 20 cross edges but only 9 triangles could cover them'))
    valid=[]
    for r,A,p,q in [(0,set(),0,0),(1,set(),0,0),(3,set(),0,0),(3,set(range(3)),0,0)]:
        z=point([(0,1,2)] if r==3 else []);valid.append([r,sorted(A),p,q,audit(r,A,p,q,z)['S_total']])
    for A in (set(),{0}):
        z=point(beta={e:F(1,2) for e in edges((0,1,2))});out=audit(3,A,0,1,z)
        full={kind:dict(v) for kind,v in z.items()};full['z'][(0,1,2)]=F(1,2)
        ck(audit(3,A,0,1,full,False)['S_total']=='0','zero-short full witness');valid.append([3,sorted(A),0,1,out['S_total']])
    for p,q in ((1,1),(0,2),(2,0)):
        z=point(alpha={e:F(p,2) for e in edges((0,1,2))},beta={e:F(q,2) for e in edges((0,1,2))})
        out=audit(3,set(range(3)),p,q,z);ck(out['S_total']=='0','equal-prefix witness');valid.append([3,[0,1,2],p,q,out['S_total']])
    return {'rejected_mutations':rejected,'count':len(rejected),'valid_boundary_controls':valid,'note':'Mutation 12 is an auxiliary residual obstruction, not a chordal-host gap counterexample.'}

def main():
    global DEADLINE
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['nine','oneone','lift','mutations'],required=True);ap.add_argument('--out',type=pathlib.Path,required=True);args=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824));resource.setrlimit(resource.RLIMIT_CPU,(39,40))
    start=time.monotonic();DEADLINE=start+36
    result=globals()[args.mode+'_mode']()
    out={'verdict':'candidate_only','best_verified_result':'none','trusted_verifier_run':False,'version':VERSION,'mode':args.mode,'status':'finite_exact_checks_passed','result':result,'runtime':{'python':platform.python_version(),'arithmetic':'fractions.Fraction and exact integer incidence','threads':1,'memory_limit_bytes':1073741824,'cpu_limit_seconds':39,'internal_wall_seconds':36,'elapsed_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'seed_sha256':hashlib.sha256((ROOT/'seed27.json').read_bytes()).hexdigest()}}
    raw=(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n').encode();ck(len(raw)<1048576,'output limit')
    with args.out.open('xb') as f:f.write(raw)
    print(json.dumps({'mode':args.mode,'status':out['status'],'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'elapsed':out['runtime']['elapsed_seconds']}))
if __name__=='__main__':main()
