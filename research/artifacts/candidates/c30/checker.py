"""C30 exact p=1,q=2 slice. Generator-side finite checks, not trusted verification.
Run from a checkout: python research/artifacts/candidates/c30/checker.py MODE --out NEW.json
Only standard-library exact arithmetic is used. MODE is construct, lp, or controls.
"""
from __future__ import annotations
import argparse, collections, copy, hashlib, importlib.util, itertools as it
import json, math, pathlib, platform, resource, time
from fractions import Fraction as F
from functools import lru_cache
VERSION='c30-one-two-v1'
DEPSHA='bcee9e8a3d427059c5a10b9e3ce893ec1ae674f58feec3b10333e18ad8984c49'
TWELFTH='f25f6b06d50933b500e5c0433fd9b1af90e1228381201437b2341e49bd6687ef'
DEADLINE=float('inf')
def ck(x,msg):
    if not x:raise ValueError(msg)
def tick():
    if time.monotonic()>DEADLINE:raise TimeoutError('internal deadline')
def edges(t):return it.combinations(sorted(t),2)
def power3(r):
    k=0
    while r>1 and r%3==0:r//=3;k+=1
    ck(r==1,'core order is not a power of three');return k
def third(u,v,k):
    w=0;place=1
    for _ in range(k):
        w+=(-(u%3)-(v%3)%3)%3*place
        u//=3;v//=3;place*=3
    return w
@lru_cache(None)
def design(r):
    k=power3(r);out=set()
    for u,v in it.combinations(range(r),2):
        w=third(u,v,k);ck(w!=u and w!=v,'affine third repeats')
        out.add(tuple(sorted((u,v,w))))
    used=collections.Counter(e for t in out for e in edges(t))
    ck(len(used)==r*(r-1)//2 and set(used.values())<={1},'affine edge partition')
    return tuple(sorted(out))
def joint(r,A,p,q,P,alpha,beta,integral=True,saturated=False):
    ck(0<=p and 0<=q and set(A)<=set(range(r)),'bad graph/budget')
    load=collections.defaultdict(F);da=[F(0)]*r;db=[F(0)]*r;val=F(0)
    seen=set()
    for t,w in P:
        t=tuple(t);w=F(w)
        ck(len(t)==3 and len(set(t))==3 and tuple(sorted(t))==t and set(t)<=set(range(r)),'bad triangle')
        ck(t not in seen,'duplicate triangle');seen.add(t)
        ck(w>=0 and (not integral or w.denominator==1),'core nonintegral/negative')
        val+=w
        for e in edges(t):load[e]+=w
    for typ,weights,deg in [('a',alpha,da),('b',beta,db)]:
        for e,w in weights.items():
            e=tuple(e);w=F(w)
            ck(len(e)==2 and 0<=e[0]<e[1]<r,'bad edge')
            ck(typ!='a' or set(e)<=set(A),'short edge outside actual subset')
            ck(w>=0,'negative leaf weight');load[e]+=w;val+=w
            for u in e:deg[u]+=w
    ck(all(w<=1 for w in load.values()),'shared core overload')
    ck(all(da[u]<=(p if u in A else 0) for u in range(r)),'short endpoint overload')
    ck(all(v<=q for v in db),'long endpoint overload')
    sc=F(r*(r-1)//2)-sum(load.values());sa=F(len(A)*p)-sum(da);sb=F(r*q)-sum(db)
    upper=F(r*(r-1)//2+len(A)*p+r*q,3)
    ck(sc+sa+sb==3*(upper-val),'capacity identity')
    if saturated:ck(sc==sa==sb==0,'not a saturated full primal')
    return {'value':val,'core_slack':sc,'short_slack':sa,'long_slack':sb,'total_slack':sc+sa+sb}
def construct(r,A):
    k=power3(r);A=tuple(sorted(A));a=len(A)
    ck(k>=2 and 2<=a<=r and len(set(A))==a,'slice domain')
    D0=[tuple(range(j,j+3)) for j in range(0,r,3)]
    D1=[(j+i,j+i+3,j+i+6) for j in range(0,r,9) for i in range(3)]
    anchor=(0,3,6);D1=sorted(t for t in D1 if t!=anchor)+[anchor]
    t,b=divmod(a,3);chosen=D1[:t]
    good={v for z in chosen for v in z}
    bad=set(anchor[:b]) if b else set();ck(not good&bad,'boundary marked twice')
    abstract=good|bad;rest=set(range(r))-abstract
    perm=dict(zip(sorted(abstract)+sorted(rest),list(A)+sorted(set(range(r))-set(A))))
    ck(set(perm)==set(range(r)) and set(perm.values())==set(range(r)),'nonbijection')
    tr=lambda z:tuple(sorted(perm[v] for v in z))
    P=[(tr(z),F(1)) for z in design(r) if z not in set(D0)|set(chosen)]
    alpha={tr(e):F(1,2) for z in chosen for e in edges(z)}
    beta={tr(e):F(1) for z in D0 for e in edges(z)}
    ans=joint(r,set(A),1,2,P,alpha,beta)
    ck(ans['core_slack']==F(a-b,2) and ans['short_slack']==b and ans['long_slack']==0,'explicit charges')
    ck(ans['value']==F(r*(r-1)//2,3)+F(2*r,3)+F(t,2),'Q formula')
    return P,alpha,beta,ans,perm

def face_weights(r,a):
    c=r-a;ck(r>=9 and 2<=a<=r,'face certificate domain')
    z={0:F(0),1:F(0),2:F(0),3:F(0)};beta={0:F(0),1:F(0),2:F(0)}
    al=F(1,a-1)
    if c==0:
        z[3]=F(r-4,(r-1)*(r-2));beta[2]=F(2,r-1)
    elif c==2:
        z[3]=F(a*a-6*a+10,a*(a-1)*(a-2))
        z[2]=F(a-3,a*(a-1));z[1]=F(1,a)
        beta[2]=F(2*(a-2),a*(a-1));beta[1]=F(2,a)
    elif a<=c:
        z[3]=F(1,a-1) if a>=3 else F(0)
        z[1]=F(c-2,c*(c-1))
        z[0]=F(c*c-a*c-3*c+4*a,c*(c-1)*(c-2))
        beta[1]=F(2,c);beta[0]=F(2*(c-a),c*(c-1))
    else:
        z[3]=F((a-c)*(a-4),a*(a-1)*(a-2))
        z[2]=F(a-2,a*(a-1));z[0]=F(1,c-2) if c>=3 else F(0)
        beta[2]=F(2*(a-c),a*(a-1));beta[1]=F(2,a)
    ck(all(v>=0 for v in [al,*z.values(),*beta.values()]),'negative face weight')
    # Independent incidence equations, omitting nonexistent edge types.
    ck(al+beta[2]+max(a-2,0)*z[3]+c*z[2]==1,'AA face row')
    if c:
        ck(beta[1]+(a-1)*z[2]+(c-1)*z[1]==1,'AC face row')
        ck(a*beta[1]+(c-1)*beta[0]==2,'long C face row')
    if c>=2:ck(beta[0]+a*z[1]+(c-2)*z[0]==1,'CC face row')
    ck((a-1)*al==1 and (a-1)*beta[2]+c*beta[1]==2,'A endpoint face row')
    return z,al,beta

def full_face(r,A):
    A=set(A);z,al,be=face_weights(r,len(A))
    P=[(t,z[len(set(t)&A)]) for t in it.combinations(range(r),3) if z[len(set(t)&A)]]
    alpha={e:al for e in it.combinations(sorted(A),2)}
    beta={e:be[len(set(e)&A)] for e in it.combinations(range(r),2) if be[len(set(e)&A)]}
    return P,alpha,beta,joint(r,A,1,2,P,alpha,beta,False,True)

def local_min(d,B):return F(d,2)+B-F(3*min(d,B),2)
def degree_dp(r,a):
    # Integer relaxation: all possible EVEN residual degrees, sum divisible by six.
    dp={0:F(0)}
    for B in [3]*a+[2]*(r-a):
        nd={}
        for rem,val in dp.items():
            for d in range(0,r,2):
                x=(rem+d)%6;v=val+local_min(d,B)
                if x not in nd or v<nd[x]:nd[x]=v
        dp=nd
    return dp[0]

def load_dep():
    f=pathlib.Path(__file__).resolve().parents[1]/'c25/extreme_audit.py'
    ck(hashlib.sha256(f.read_bytes()).hexdigest()==DEPSHA,'dependency digest')
    spec=importlib.util.spec_from_file_location('c25_exact',f);ex=importlib.util.module_from_spec(spec);spec.loader.exec_module(ex)
    ex.DEADLINE=DEADLINE;return ex

def quotient(r,a):
    c=r-a;caps=[a*(a-1)//2,a*c,c*(c-1)//2,a,2*a,2*c]
    specs=[('AAA',a>=3,[3,0,0,0,0,0]),('AAC',a>=2 and c>=1,[1,2,0,0,0,0]),
    ('ACC',a>=1 and c>=2,[0,2,1,0,0,0]),('CCC',c>=3,[0,0,3,0,0,0]),
    ('alphaAA',a>=2,[1,0,0,2,0,0]),('betaAA',a>=2,[1,0,0,0,2,0]),
    ('betaAC',a>=1 and c>=1,[0,1,0,0,1,1]),('betaCC',c>=2,[0,0,1,0,0,2])]
    labels=[n for n,on,col in specs if on];cols=[col for n,on,col in specs if on]
    mat=[list(v) for v in zip(*cols)] if cols else [[] for _ in caps]
    return labels,mat,caps

def residual_lp(ex,r,A,P):
    A=set(A);used={e for t,w in P for e in edges(t)}
    es=[e for e in it.combinations(range(r),2) if e not in used];ids={e:i for i,e in enumerate(es)}
    short=sorted(A);sid={u:i for i,u in enumerate(short)};cap=[1]*len(es)+[1]*len(A)+[2]*r;cols=[];labels=[]
    for kind in ('a','b'):
        for e in es:
            if kind=='a' and not set(e)<=A:continue
            col=[0]*len(cap);col[ids[e]]=1
            for u in e:col[len(es)+(sid[u] if kind=='a' else len(A)+u)]=1
            cols.append(col);labels.append((kind,e))
    mat=list(map(list,zip(*cols))) if cols else [[] for _ in cap]
    val,x,y=ex.lp_tableau(mat,cap);vv,xx,yy=ex.lp_revised(mat,cap)
    ex.validate(mat,cap,val,x,y);ex.validate(mat,cap,vv,xx,yy);ck(val==vv,'residual LPs disagree')
    return {'leaf_value':val,'core_value':len(P),'total':len(P)+val,'positive':[{'kind':k,'edge':e,'weight':v} for (k,e),v in zip(labels,x) if v],'dual':y,'scope':'fixed newly constructed support only; global Q bound is the written parity-residue proof'}

def serialize_witness(r,A,P,al,be,ans):
    return {'r':r,'A':sorted(A),'p':1,'q':2,'core_triangles':[t for t,w in P],
    'alpha':[[*e,v] for e,v in sorted(al.items())],'beta':[[*e,v] for e,v in sorted(be.items())],**ans}

def construct_run():
    rows=[];counts=[];nine=[]
    for r in (9,27,81):
        for a in range(2,r+1):
            tick();P,al,be,ans,perm=construct(r,range(a));face_weights(r,a)
            ck(degree_dp(r,a)==ans['total_slack'],'integer residue relaxation')
            rows.append([r,a,str(ans['value']),str(ans['total_slack'])])
            if r==9:
                f=full_face(r,range(a));nine.append({**serialize_witness(r,range(a),P,al,be,ans),'L':f[3]['value'],'type_counts':dict(collections.Counter(len(set(t)&set(range(a))) for t,w in P))})
        counts.append({'r':r,'complete_cardinalities':r-1})
    subsets=0
    for mask in range(512):
        if mask.bit_count()<2:continue
        A=[u for u in range(9) if mask>>u&1];construct(9,A);full_face(9,A);subsets+=1
    larger=[]
    for a in (2,3,4,5,121,122,241,242,243):
        tick();P,al,be,ans,perm=construct(243,range(a));face_weights(243,a)
        larger.append({'r':243,'a':a,**ans})
    # Conjugate the nonlinear shear through the relabeling; the marked set is invariant.
    changes=[]
    for r,a in ((9,4),(27,13),(81,40),(243,121)):
        P,al,be,ans,perm=construct(r,range(a));inv={v:u for u,v in perm.items()}
        def shear(u):
            v=inv[u];v0=v%3;v1=(v//3)%3;z=v-v1*3+((v1+v0*v0)%3)*3;return perm[z]
        ck({shear(v) for v in range(a)}==set(range(a)),'shear changes short neighborhood')
        tr=lambda t:tuple(sorted(shear(v) for v in t))
        old=[(tr(t),w) for t,w in P];aa={tr(e):v for e,v in al.items()};bb={tr(e):v for e,v in be.items()}
        oldans=joint(r,set(range(a)),1,2,old,aa,bb);ck(oldans==ans,'support exchange value loss')
        changed=len({t for t,w in old}-{t for t,w in P})
        ck(changed==r*(r-3)//9,'quadratic support formula')
        changes.append({'r':r,'a':a,'removed_old_core_triangles':changed,'objective_loss':0})
    return {'complete_cardinality_ranges':counts,'parameter_rows':rows,'nine_core_certificates':nine,'complete_actual_nine_subsets':subsets,'named_larger':larger,'global_reselection':changes,'complete_k_above_4':False}

def lp_run():
    ex=load_dep();rows=[];res=[]
    for r in (9,27,81):
        for a in range(2,r+1):
            tick();lab,mat,caps=quotient(r,a)
            v,x,y=ex.lp_tableau(mat,caps);vv,xx,yy=ex.lp_revised(mat,caps)
            ex.validate(mat,caps,v,x,y);ex.validate(mat,caps,vv,xx,yy)
            ck(v==vv==F(r*(r-1)//2+a+2*r,3),'full face LP equality')
            face_weights(r,a);rows.append([r,a,str(v)])
            if r==9:
                P,al,be,ans,perm=construct(r,range(a));t=residual_lp(ex,r,range(a),P)
                ck(t['total']==ans['value'],'residual support optimum')
                res.append({'a':a,**t})
    controls=[]
    for a in (2,3):
        lab,mat,caps=quotient(3,a);v,x,y=ex.lp_tableau(mat,caps);ex.validate(mat,caps,v,x,y)
        ck(v<F(3+a+6,3),'r=3 false face');controls.append({'r':3,'a':a,'L':v,'uniform_upper':F(3+a+6,3),'on_face':False})
    # Previously frozen denominators are only scope controls, not new Q results.
    path=pathlib.Path(__file__).resolve().parents[1]/'c27/twelfth-point.json';raw=path.read_bytes()
    ck(hashlib.sha256(raw).hexdigest()==TWELFTH,'twelfth digest');data=json.loads(raw)
    E,labels,mat,caps=ex.model(*data['params']);pos={(o['kind'],tuple(o['vertices'])):F(o['weight']) for o in data['positive']}
    ex.validate(mat,caps,F(31,3),[pos.get(l,F(0)) for l in labels],[F(1,3)]*len(caps))
    E,labels,mat,caps=ex.model(5,2,4,1,1);v,x,y=ex.lp_tableau(mat,caps);ex.validate(mat,caps,v,x,y)
    ck(v==5 and v<F(sum(caps),3),'quarter scope mismatch')
    return {'complete_quotient_ranges':{'r':[9,27,81],'a':'2..r','cases':len(rows)},'rows':rows,'nine_residual_LP_pairs':res,'k_one_no_face':controls,'denominator_controls':{'quarter':'L=5 < 16/3; outside face','twelfth':'frozen 31-row full-face rank-28 point verified; Q not optimized'},'global_Q_optimizer_run':False}

def controls_run():
    tests=[]
    for d in range(0,50,2):
        for B in (2,3):
            s=local_min(d,B);dv=4 if B==3 else 2;base=F(1,2) if B==3 else F(0)
            ck(s>=base+F(dv-d,4) and s>=base+F(d-dv,2),'local supporting lines')
    # Accepted boundary fixtures without claiming a q=0 extension theorem.
    boundary=[]
    for r,A,p,q,mode in [(1,[],0,0,'empty'),(3,[],0,2,'beta'),(9,[],0,2,'beta'),(9,[0],0,2,'beta'),(9,list(range(9)),0,0,'core'),(9,[],0,0,'core'),(9,[0,3,6],1,0,'short'),(9,[],0,1,'half'),(9,list(range(9)),1,2,'main')]:
        ds=design(r);P=[(t,F(1)) for t in ds];al={};be={}
        if mode in ('beta','half'):
            D0={tuple(range(j,j+3)) for j in range(0,r,3)}
            P=[(t,F(1)) for t in ds if t not in D0];be={e:F(q,2) for t in D0 for e in edges(t)}
        elif mode=='short':
            T=(0,3,6);P=[(t,F(1)) for t in ds if t!=T];al={e:F(1,2) for e in edges(T)}
        elif mode=='main':P,al,be,ans,perm=construct(r,A)
        ans=joint(r,set(A),p,q,P,al,be);boundary.append({'r':r,'a':len(A),'p':p,'q':q,**ans})
    P,al,be,ans,perm=construct(9,range(4));used={e for t,w in P for e in edges(t)}
    def reject(name,f):
        try:f()
        except (ValueError,AssertionError):tests.append(name);return
        raise AssertionError('mutation accepted: '+name)
    reject('duplicate_core',lambda:joint(9,set(range(4)),1,2,P+P[:1],al,be))
    reject('repeated_vertex',lambda:joint(9,set(range(4)),1,2,[((0,0,1),F(1))],{},{}))
    reject('fractional_core_in_Q',lambda:joint(9,set(range(4)),1,2,[(P[0][0],F(1,2))],{},{}))
    reject('negative_alpha',lambda:joint(9,set(range(4)),1,2,P,{(0,1):F(-1,2)},be))
    reject('short_edge_outside_A',lambda:joint(9,set(range(4)),1,2,[],{(0,8):F(1,2)},{}))
    reject('short_endpoint_overload',lambda:joint(9,set(range(4)),1,2,[],{(0,1):F(3,4),(0,2):F(3,4)},{}))
    reject('long_endpoint_overload',lambda:joint(9,set(range(4)),1,2,[],{},dict.fromkeys([(0,1),(0,2),(0,3)],F(1))))
    bb=dict(be);bb[min(used)]=F(1,2)
    reject('core_beta_shared_conflict',lambda:joint(9,set(range(4)),1,2,P,al,bb))
    fp,fa,fb,fs=full_face(9,range(4));fb=dict(fb);key=next(iter(fb));fb[key]/=2
    reject('false_saturation',lambda:joint(9,set(range(4)),1,2,fp,fa,fb,False,True))
    reject('face_small_core',lambda:face_weights(3,2))
    reject('wrong_remainder_Q',lambda:ck(ans['value']==F(36+4+18,3)-F(4,6),'omitted residue correction'))
    reject('non_power_three',lambda:design(8))
    ck(len(tests)==12,'mutation count')
    return {'rejected_mutations':tests,'accepted_boundary_controls':boundary,'local_degree_rows':50,'global_residual_graph_enumeration':False}

def main():
    global DEADLINE
    pa=argparse.ArgumentParser();pa.add_argument('mode',choices=['construct','lp','controls']);pa.add_argument('--out',type=pathlib.Path,required=True);pa.add_argument('--seconds',type=int,default=38);args=pa.parse_args()
    ck(1<=args.seconds<=40,'time budget');start=time.monotonic();DEADLINE=start+args.seconds
    resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824));resource.setrlimit(resource.RLIMIT_CPU,(args.seconds+2,args.seconds+3))
    result={'verdict':'candidate_only','best_verified_result':'none','version':VERSION,'mode':args.mode,'data':{'construct':construct_run,'lp':lp_run,'controls':controls_run}[args.mode]()}
    result['runtime']={'python':platform.python_version(),'arithmetic':'fractions.Fraction and integers','threads':1,'memory_limit_bytes':1073741824,'internal_seconds':args.seconds,'internal_elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
    raw=(json.dumps(result,sort_keys=True,separators=(',',':'),default=lambda v:str(v) if isinstance(v,F) else list(v))+'\n').encode();ck(len(raw)<=1048576,'output cap')
    with args.out.open('xb') as f:f.write(raw)
    print(json.dumps({'mode':args.mode,'status':'finite_checks_passed','bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'elapsed':result['runtime']['internal_elapsed_seconds']}))
if __name__=='__main__':main()
