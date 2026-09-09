"""C27 finite certificate replay, not a trusted verifier or a general-face proof.
Run in a repository checkout: python uniform_face_checker.py --mode construct --out NEW.json
Modes: construct, lp. Python standard library; no external solver or network.
"""
from __future__ import annotations
import argparse, collections, hashlib, importlib.util, itertools as it
import json, pathlib, platform, resource, time
from fractions import Fraction as F
from functools import lru_cache
VERSION='c27-uniform-affine-v1'
DEP='bcee9e8a3d427059c5a10b9e3ce893ec1ae674f58feec3b10333e18ad8984c49'
DEADLINE=float('inf')
def ck(ok,msg):
    if not ok: raise ValueError(msg)
def tick():
    if time.monotonic()>DEADLINE: raise TimeoutError('explicit internal deadline')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def power3(n):
    if n<1:return False
    while n%3==0:n//=3
    return n==1
@lru_cache(None)
def digits(v,k): return tuple((v//(3**i))%3 for i in range(k))
def code(v): return sum(x*3**i for i,x in enumerate(v))
def add(u,v,k): return code(tuple((x+y)%3 for x,y in zip(digits(u,k),digits(v,k))))
def neg(u,k): return code(tuple(-x%3 for x in digits(u,k)))
def sub(u,v,k): return add(u,neg(v,k),k)
def direction(u,v,k):
    d=sub(v,u,k);return min(d,neg(d,k))
def dimension(r):
    ck(power3(r),'core not a power of three');k=0
    while 3**k<r:k+=1
    return k
@lru_cache(None)
def geometry(r):
    k=dimension(r);D=[];pairs=set()
    for u in range(r):
        tick()
        for v in range(u+1,r):
            w=neg(add(u,v,k),k)
            if v<w:
                t=(u,v,w);d=direction(u,v,k);D.append((d,t))
                for e in it.combinations(t,2):
                    ck(e not in pairs,'affine repeated pair');pairs.add(e)
    ck(len(pairs)==r*(r-1)//2,'affine missing pairs')
    dirs=tuple(sorted({d for d,t in D}))
    ck(len(dirs)==(r-1)//2,'direction count')
    return tuple(D),dirs

def parameters(r,a,b,p,q):
    ck(all(isinstance(x,int) for x in (r,a,b,p,q)),'integer parameters')
    ck(power3(r) and 0<=a<=b<=r,'core/prefix domain')
    ck((a==0 or power3(a)) and (b==0 or power3(b)),'prefix not a coordinate subspace size')
    ck(0<=p<=max(a-1,0) and q>=0 and p+q<=max(b-1,0),'necessary uniform-face degree budget')

def fill(directions,total,occupied=None):
    occupied=occupied or {};out={}
    for d in directions:
        use=min(total,2-occupied.get(d,0))
        if use:out[d]=use
        total-=use
    ck(total==0,'direction capacity exhausted');return out

def certificate(r,a,b,p,q,integral_core=False):
    parameters(r,a,b,p,q);D,ds=geometry(r)
    da=[d for d in ds if d<a];db=[d for d in ds if d<b]
    if integral_core and a==b and p+q:
        total=p+q;take=fill(db,total-total%2)
        ax=F(p,total);by=F(q,total)
        weights={('z',t):F(0 if all(v<b for v in t) and take.get(d,0) else 1) for d,t in D}
        for d,t in D:
            if all(v<b for v in t) and take.get(d,0):
                for e in it.combinations(t,2):
                    if p:weights[('a',e)]=ax
                    if q:weights[('b',e)]=by
        return weights
    pp=p-p%2 if integral_core else p;qq=q-q%2 if integral_core else q
    sx=fill(da,pp);sy=fill(db,qq,sx)
    weights={}
    for d,t in D:
        x=F(sx.get(d,0),2) if all(v<a for v in t) else F(0)
        y=F(sy.get(d,0),2) if all(v<b for v in t) else F(0)
        weights[('z',t)]=1-x-y
        for e in it.combinations(t,2):
            if x:weights[('a',e)]=x
            if y:weights[('b',e)]=y
    return weights

def verify(r,a,b,p,q,W,integer_core=False,saturated=False):
    core=collections.defaultdict(F);dx=[F(0)]*a;dy=[F(0)]*b;val=F(0)
    for (kind,obj),z in W.items():
        ck(z>=0,'negative coordinate');val+=z
        if kind=='z':
            ck(len(obj)==3 and len(set(obj))==3 and all(0<=v<r for v in obj),'bad core triangle')
            if integer_core:ck(z.denominator==1,'fractional core retained')
            for e in it.combinations(sorted(obj),2):core[e]+=z
        else:
            ck(kind in ('a','b'),'unknown object type');d=a if kind=='a' else b
            ck(len(obj)==2 and 0<=obj[0]<obj[1]<d,'leaf outside prefix')
            core[obj]+=z;deg=dx if kind=='a' else dy
            for v in obj:deg[v]+=z
    ck(all(z<=1 for z in core.values()),'shared core capacity exceeded')
    ck(all(z<=p for z in dx) and all(z<=q for z in dy),'endpoint budget exceeded')
    cs=F(r*(r-1)//2)-sum(core.values());es=sum(F(p)-z for z in dx)+sum(F(q)-z for z in dy)
    full=F(r*(r-1)//2+a*p+b*q,3)
    ck(full-val==(cs+es)/3,'one-third deficit identity')
    if saturated:ck(cs==es==0,'uniform primal not saturated')
    return {'value':str(val),'core_slack':str(cs),'endpoint_slack':str(es),'gap_to_full':str(full-val)}

def affine_case(pars):
    r,a,b,p,q=pars
    fractional=certificate(*pars);fp=verify(*pars,fractional,saturated=True)
    rounded=certificate(*pars,integral_core=True);rp=verify(*pars,rounded,integer_core=True)
    budget=b*((p+q)%2) if a==b else a*(p%2)+b*(q%2)
    ck(F(rp['core_slack'])==0 and F(rp['endpoint_slack'])==budget,'charged parity budget')
    ck(F(fp['value'])-F(rp['value'])==F(budget,3),'constructive loss')
    return {'parameters':pars,'L':fp['value'],'Q_witness':rp['value'],'charged_endpoint_budget':budget}

def support_trade(r):
    k=dimension(r);ck(k>=4 and k%2==0,'support-trade family domain')
    pars=(r,9,r,2,(r-1)//2);W=certificate(*pars,integral_core=True)
    verify(*pars,W,integer_core=True,saturated=True)
    def perm(u):
        v=list(digits(u,k));v[1]=(v[1]+v[0]*v[0])%3;return code(v)
    ck(len({perm(u) for u in range(r)})==r,'nonbijective shear')
    ck({perm(u) for u in range(9)}==set(range(9)),'shear moves prefix')
    changed={(kind,tuple(sorted(perm(u) for u in obj))):z for (kind,obj),z in W.items()}
    verify(*pars,changed,integer_core=True,saturated=True)
    old={t for (kind,t),z in changed.items() if kind=='z' and z==1}
    new={t for (kind,t),z in W.items() if kind=='z' and z==1}
    removed=len(old-new);lower=r*(r-9)//36
    ck(removed>=lower,'quadratic support lower bound')
    return {'parameters':pars,'old_integral_core_removed':removed,'proven_lower_bound':lower,'actual_objective_loss':'0'}

def construct_suite():
    rows=[]
    for r in (1,3,9,27):
        sizes=[0]+[3**i for i in range(dimension(r)+1)];count=0
        for a in sizes:
            for b in sizes:
                if a>b:continue
                for p in range(max(a-1,0)+1):
                    for q in range(max(b-1,0)-p+1):
                        tick();affine_case((r,a,b,p,q));count+=1
        rows.append({'r':r,'complete_affine_parameter_cases':count})
    named=[(81,9,81,2,40),(81,9,81,3,41),(81,9,27,5,17),(243,27,81,13,45),(243,27,243,25,217),(81,27,27,7,19),(27,0,27,0,7),(27,1,9,0,7)]
    extras=[affine_case(t) for t in named];trade=support_trade(81)
    pars=(9,3,9,1,3);W=certificate(*pars,integral_core=True);mut=[]
    def reject(name,fn):
        try:fn()
        except (ValueError,AssertionError):mut.append(name)
        else:raise ValueError('missed mutation '+name)
    bad=W.copy();bad[('z',(0,1,2))]=F(2);reject('core_double_spending',lambda:verify(*pars,bad,True))
    bad=W.copy();bad[('a',(0,8))]=F(1);reject('short_edge_outside_prefix',lambda:verify(*pars,bad,True))
    bad=W.copy();bad[('b',(0,1))]=F(4);reject('long_endpoint_overload',lambda:verify(*pars,bad,True))
    bad=W.copy();bad[('z',(0,0,1))]=F(1);reject('repeated_triangle_vertex',lambda:verify(*pars,bad,True))
    bad=W.copy();bad[('z',(0,1,2))]=F(-1);reject('negative_coordinate',lambda:verify(*pars,bad,True))
    bad=W.copy();bad[('z',(0,1,2))]=F(1,4);reject('quarter_core_not_integral',lambda:verify(*pars,bad,True))
    reject('nonaffine_prefix_silently_allowed',lambda:parameters(9,2,9,1,1))
    reject('excess_combined_degree',lambda:parameters(9,3,9,2,7))
    reject('positive_zero_prefix_budget',lambda:parameters(9,0,9,1,1))
    reject('bad_reservoir_direction_units',lambda:fill([1],3))
    reject('odd_budget_called_saturated',lambda:verify(*pars,W,True,True))
    reject('support_changes_counted_as_loss',lambda:ck(trade['old_integral_core_removed']==0,'positive changes at zero loss'))
    return {'complete_affine_ranges':rows,'named_cases':extras,'support_trade':trade,'mutations_detected':mut}

def load_dependency():
    path=pathlib.Path(__file__).resolve().parent.parent/'c25/extreme_audit.py'
    ck(sha(path)==DEP,'immutable C25 dependency SHA mismatch')
    spec=importlib.util.spec_from_file_location('c25_exact',path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);mod.DEADLINE=DEADLINE
    return mod

def core_masks(r,reverse=False):
    E=list(it.combinations(range(r),2));idx={e:i for i,e in enumerate(E)}
    ts=[sum(1<<idx[e] for e in it.combinations(t,2)) for t in it.combinations(range(r),3)]
    if not reverse:
        states={0}
        for t in ts:states.update(s|t for s in list(states) if not s&t)
        return states
    @lru_cache(None)
    def yes(s):
        if not s:return True
        first=s&-s;return any(t&first and t&s==t and yes(s^t) for t in ts)
    return {s for s in range(1<<len(E)) if s.bit_count()%3==0 and yes(s)}

def lp_suite():
    ex=load_dependency();counts=[];table=[]
    for r in range(5):
        states=core_masks(r);ck(states==core_masks(r,True),'two core-support enumerators')
        count=face=0
        for a in range(r+1):
            for b in range(a,r+1):
                for p in range(ex.capfn(a)+1):
                    for q in range(ex.capfn(b)+1):
                        tick();E,labels,A,B=ex.model(r,a,b,p,q);v,x,y=ex.lp_tableau(A,B);vv,xx,yy=ex.lp_revised(A,B)
                        ex.validate(A,B,v,x,y);ex.validate(A,B,vv,xx,yy);ck(v==vv,'LP implementations disagree');count+=1
                        cap=F(sum(B),3)
                        if v!=cap:continue
                        face+=1;Qs=[]
                        for solver in (ex.lp_tableau,ex.lp_revised):
                            best=F(0)
                            for used in states:
                                EE,LL,AA,BB=ex.model(r,a,b,p,q,((1<<len(E))-1)^used,False)
                                f,fx,fy=solver(AA,BB);ex.validate(AA,BB,f,fx,fy);best=max(best,F(used.bit_count(),3)+f)
                            Qs.append(best)
                        ck(Qs[0]==Qs[1] and Qs[0]<=v,'Q implementations disagree')
                        table.append([r,a,b,p,q,str(v),str(Qs[0])])
        counts.append({'r':r,'capped_tuples':count,'all_row_one_third_face':face})
    point=json.loads(pathlib.Path(__file__).with_name('twelfth-point.json').read_text());pars=point['params']
    E,labels,A,B=ex.model(*pars);positive={(z['kind'],tuple(z['vertices'])):F(z['weight']) for z in point['positive']};x=[positive.get(l,F(0)) for l in labels]
    v=F(point['value']);y=[F(1,3)]*len(B);ex.validate(A,B,v,x,y)
    ck(all(ex.dot(row,x)==rhs for row,rhs in zip(A,B)),'twelfth point not full face')
    v1,x1,y1=ex.lp_tableau(A,B);v2,x2,y2=ex.lp_revised(A,B)
    ex.validate(A,B,v1,x1,y1);ex.validate(A,B,v2,x2,y2);ck(v==v1==v2,'named point optimum')
    pos=[j for j,w in enumerate(x) if w];rk=ex.rank([[row[j] for j in pos] for row in A])
    ck(rk==len(pos),'twelfth point extremality')
    return {'complete_small_ranges':counts,'uniform_face_Q_table':table,'twelfth_point':{'parameters':pars,'L':str(v),'positive_columns':len(pos),'tight_column_rank':rk,'all_rows_saturated':True,'denominators':sorted({z.denominator for z in x if z}),'Q_not_computed':True},'old_quarter_case_scope':{'parameters':[5,2,4,1,1],'L':'5','one_third_bound':'16/3','in_uniform_face':False}}

def main():
    global DEADLINE
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['construct','lp'],required=True);ap.add_argument('--out',type=pathlib.Path,required=True);args=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824));resource.setrlimit(resource.RLIMIT_CPU,(42,43));start=time.monotonic();DEADLINE=start+39
    result=construct_suite() if args.mode=='construct' else lp_suite()
    result.update({'verdict':'candidate_only','status':'finite_checks_passed','mode':args.mode,'version':VERSION,'trusted_verifier_run':False,'best_verified_result':'none','limitations':['Only the affine-flag subclass is covered by the all-order constructive theorem.','Finite checks do not prove the arbitrary-size one-third face theorem.','The named twelfth point has no Q optimization in this run.']})
    result['runtime']={'python':platform.python_version(),'arithmetic':'fractions.Fraction and exact integer arithmetic','threads':1,'memory_limit_bytes':1073741824,'CPU_limit_seconds':42,'internal_wall_seconds':39,'elapsed_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_sha256':sha(pathlib.Path(__file__))}
    raw=(json.dumps(result,sort_keys=True,indent=2)+'\n').encode();ck(len(raw)<=1048576,'output size');args.out.open('xb').write(raw)
    print(json.dumps({'status':result['status'],'mode':args.mode,'sha256':hashlib.sha256(raw).hexdigest(),'elapsed_seconds':result['runtime']['elapsed_seconds']}))
if __name__=='__main__':main()
