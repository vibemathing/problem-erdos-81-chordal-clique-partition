"""Finite nested-prefix experiments. Candidate-side computation, not admission.
Uses the supplied immutable C23 exact-rational backend, explicitly digest-bound.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, itertools as it, json, pathlib
import platform, resource, time
from fractions import Fraction as Q
VERSION='nested-normalization-1'
def require(x,message):
    if not x: raise ValueError(message)
def stable(x): return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def digest(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def edge_set(r,ds):
    return set(it.combinations(range(r),2)) | {(a,r+i) for i,d in enumerate(ds) for a in range(d)}
def normalize(r,ds,h):
    require(h>=2 and ds==sorted(ds) and all(0<=d<=r for d in ds),'input domain')
    n=r+len(ds); es=edge_set(r,ds)
    if r==0: return set(), {'core':[], 'leftover':[], 'equalize':[], 'residue':[]}
    rp=1+h*((r-1)//h); t0=h*(len(ds)//h)
    core=sorted(e for e in es if any(rp<=v<r for v in e)); left=es-set(core)
    rem=sorted(e for e in left if e[1]>=r+t0); left-=set(rem)
    ds0=[min(d,rp) for d in ds]; target=[0]*len(ds); eq=[]; res=[]
    for i in range(0,t0,h):
        lo=ds0[i]; low=h*(lo//h)
        for j in range(i,i+h):
            eq.extend((a,r+j) for a in range(lo,ds0[j])); res.extend((a,r+j) for a in range(low,lo)); target[j]=low
    left-=set(eq)|set(res); cats=dict(core=core,leftover=rem,equalize=eq,residue=res)
    deleted=set().union(*(set(v) for v in cats.values()))
    require(sum(len(v) for v in cats.values())==len(deleted),'overlapping deletion classes')
    require(left==es-deleted,'deleted edge union')
    require(left==set(it.combinations(range(rp),2))|{(a,r+i) for i,d in enumerate(target) for a in range(d)},'normal form adjacency')
    require(len(core)<=(h-1)*n and len(rem)<=(h-1)*rp,'vertex isolation budget')
    require(len(eq)<=(h-1)*rp and len(res)<=(h-1)*len(ds),'telescoping budget')
    require(len(deleted)<=3*(h-1)*n,'total normalization budget')
    require(rp%h==1 and all(d%h==0 for d in target),'normal form residues')
    require(all(target.count(d)%h==0 for d in set(target) if d),'twin multiplicities')
    if h==2:
        require(all(sum(v in e for e in left)%2==0 for v in range(n)),'Eulerian normal form')
    return left,cats

def charge(E,tri,z,deleted):
    lost={i for i,e in enumerate(E) if e in deleted}; charged={i:Q(0) for i in lost}; mass=Q(0)
    for mask,w in zip(tri,z):
        hit=[i for i in lost if (mask>>i)&1]
        if hit: charged[min(hit)]+=w;mass+=w
    require(all(v<=1 for v in charged.values()),'fractional edge overcharge')
    require(mass==sum(charged.values()) and mass<=len(deleted),'one-time charge total')
    return mass

def prefix_dual(r,ds,k):
    prices={e:(Q(1) if e[1]<k else Q(1,3)) for e in it.combinations(range(r),2)}
    for i,d in enumerate(ds):
        special=2*max(0,d-k)<=d
        prices.update({(a,r+i):Q(0) if special and a<k else Q(2,3) if special else Q(1,3) for a in range(d)})
    value=Q(r*(r-1)//2+2*(k*(k-1)//2)+sum(min(d,2*max(0,d-k)) for d in ds),3)
    require(sum(prices.values())==value,'dual objective')
    return value,prices

def main():
    p=argparse.ArgumentParser();p.add_argument('--backend',type=pathlib.Path,required=True);p.add_argument('--backend-sha256',required=True)
    p.add_argument('--max-n',type=int,default=8);p.add_argument('--seconds',type=int,default=38);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args()
    require(0<=a.max_n<=9 and 1<=a.seconds<=120,'resource domain');require(digest(a.backend)==a.backend_sha256,'backend digest')
    resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824));resource.setrlimit(resource.RLIMIT_CPU,(a.seconds+2,a.seconds+3))
    start=time.monotonic();s=importlib.util.spec_from_file_location('checker',a.backend);c=importlib.util.module_from_spec(s);s.loader.exec_module(c);c.BUDGET=c.Budget(a.seconds,1000000,10000)
    a.out.mkdir(parents=True,exist_ok=False); rows=[];levels=[];cache={};certs={};cur=None;error=None;mut=None
    def inspect(n,es):
        code=c.encode(n,sorted(es));key=(n,code)
        if key not in cache: cache[key]=c.inspect_graph(n,code,True)
        return cache[key]
    try:
        mut=c.mutations()
        for n in range(a.max_n+1):
            number=0
            for r in range(n+1):
                for ds_tuple in it.combinations_with_replacement(range(r+1),n-r):
                    ds=list(ds_tuple);cur=(n,r,ds);es=edge_set(r,ds);row,data=inspect(n,es);E,adj,pcs,tri,x,w,z,y,cpw,pw,nuw=data
                    ub=[]
                    for k in range(r+1):
                        value,prices=prefix_dual(r,ds,k)
                        require(all(sum(prices[E[j]] for j in range(len(E)) if (T>>j)&1)>=1 for T in tri),'prefix cover triangle')
                        require(value>=Q(row['nu_star']),'prefix cover upper bound');ub.append(value)
                    norm=[]
                    for h in (2,6):
                        left,cats=normalize(r,ds,h);deleted=es-left;mass=charge(E,tri,z,deleted);hr,_=inspect(n,left)
                        require(Q(row['nu_star'])<=Q(hr['nu_star'])+mass,'fractional transfer')
                        require(row['nu']>=hr['nu'],'packing subgraph inclusion')
                        require(Q(row['nu_star'])-row['nu']<=Q(hr['nu_star'])-hr['nu']+len(deleted),'gap transfer')
                        norm.append({'h':h,'deleted':len(deleted),'fractional_mass_removed':str(mass)})
                    row=dict(row,r=r,ds=ds,gap=str(Q(row['nu_star'])-row['nu']),prefix_upper=str(min(ub)),normalizations=norm);rows.append(row);number+=1
                    # Proposed false shortcut: Eulerian plus integral fractional optimum => no gap.
                    even=all(sum(v in e for e in es)%2==0 for v in range(n))
                    if even and Q(row['nu_star']).denominator==1 and Q(row['nu_star'])>row['nu']:
                        key=f'{n}:{r}:{ds}'
                        certs[key]={'row':row,'maximal_cliques':[list(c.vertices(s)) for s,_ in pcs if not any(s!=q and s&q==s for q,_ in pcs)],'certificate':c.certificate_payload(data)}
            require(number==2**n,'complete representation count')
            levels.append({'n':n,'parameter_cases':number});(a.out/'progress.json').write_bytes(stable(levels))
    except Exception as e:error=type(e).__name__+': '+str(e)
    status='complete' if error is None else 'partial';exit_code=0 if error is None else 2
    payloads={'table.jsonl':b''.join(stable(row) for row in rows),'counterexamples.json':stable(certs)}
    for name,b in payloads.items():require(len(b)<=1048576,'file size');(a.out/name).write_bytes(b)
    usage=resource.getrusage(resource.RUSAGE_SELF)
    summary={'verdict':'candidate_only','status':status,'version':VERSION,'python':platform.python_version(),'backend_sha256':a.backend_sha256,'source_sha256':digest(__file__),'target_max_n':a.max_n,'largest_completed_n':levels[-1]['n'] if levels else None,'levels':levels,'parameter_cases':len(rows),'distinct_labelled_LP_cases':len(cache),'mutations_rejected':mut,'error':error,'first_unfinished_parameter':cur if error else None,'counterexample_count':len(certs),'scope':'all sorted prefix sequences for every specified core size; descriptions are not distinct graph isomorphism classes; two exact rational LPs and separate integer optimizers; sampled optimal duals only','run':{'elapsed_seconds':time.monotonic()-start,'cpu_seconds':usage.ru_utime+usage.ru_stime,'maxrss_kib':usage.ru_maxrss,'wall_budget_seconds':a.seconds,'memory_bytes':1073741824,'threads':1,'exit_code':exit_code},'outputs':{name:{'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)} for name,b in payloads.items()}}
    (a.out/'summary.json').write_bytes(stable(summary));print(json.dumps({k:summary[k] for k in ('status','largest_completed_n','parameter_cases','error','counterexample_count','run')}));return exit_code
if __name__=='__main__':raise SystemExit(main())
