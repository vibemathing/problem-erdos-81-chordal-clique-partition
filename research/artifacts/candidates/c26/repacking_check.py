"""C26 exact finite checks. Generator-side, not a registered verifier.
Run from a repository checkout: python repacking_check.py --out NEW.json
The imported C25 source is immutable and SHA-256 checked before execution.
"""
from __future__ import annotations
import argparse, collections, hashlib, importlib.util, itertools as it
import json, pathlib, platform, resource, time
from fractions import Fraction as F
from functools import lru_cache
VERSION = 'c26-repacking-v1'
DEP_SHA = 'bcee9e8a3d427059c5a10b9e3ce893ec1ae674f58feec3b10333e18ad8984c49'

def ck(ok, message):
    if not ok: raise ValueError(message)
def edge(u,v): return tuple(sorted((u,v)))
def all_edges(n): return set(it.combinations(range(n),2))
def adjacency(n,E):
    ck(all(0<=u<v<n for u,v in E),'invalid simple edge')
    out=[set() for _ in range(n)]
    for u,v in E: out[u].add(v);out[v].add(u)
    return out

def hamilton(n,E):
    """Endpoint extension and Dirac rotation; never retains a frozen core packing."""
    adj=adjacency(n,E)
    ck(n>=3 and 2*min(map(len,adj))>=n,'Dirac premise')
    path=[0]
    while True:
        while True:
            unused=set(range(n))-set(path)
            right=adj[path[-1]]&unused
            left=adj[path[0]]&unused
            if right: path.append(min(right))
            elif left: path.insert(0,min(left))
            else: break
        k=len(path)
        j=next((i for i in range(k-1) if path[i+1] in adj[path[0]] and path[-1] in adj[path[i]]),None)
        ck(j is not None,'Dirac closing rotation missing')
        cyc=path[:j+1]+path[:j:-1]
        ck(len(set(cyc))==k and all(edge(cyc[i],cyc[(i+1)%k]) in E for i in range(k)),'invalid rotated cycle')
        if k==n:return cyc
        outside=set(range(n))-set(cyc)
        link=next(((i,min(adj[v]&outside)) for i,v in enumerate(cyc) if adj[v]&outside),None)
        ck(link is not None,'dense graph disconnected')
        j,w=link;path=[w]+cyc[j:]+cyc[:j]

def cycle_edges(cyc):
    ck(len(cyc)>=3 and len(set(cyc))==len(cyc),'not a simple cycle')
    return {edge(cyc[i],cyc[(i+1)%len(cyc)]) for i in range(len(cyc))}

def parity_join(cyc,odd):
    n=len(cyc);bits=[];last=0
    ck(len(odd)%2==0 and odd<=set(cyc),'odd-set parity')
    for v in cyc:
        last^=int(v in odd);bits.append(last)
    ck(last==0,'parity recurrence did not close')
    one={edge(cyc[i],cyc[(i+1)%n]) for i,b in enumerate(bits) if b}
    other=cycle_edges(cyc)-one
    chosen=min((one,other),key=lambda z:(len(z),sorted(z)))
    deg=collections.Counter(v for e in chosen for v in e)
    ck({v for v,d in deg.items() if d%2}==odd,'T-join boundary')
    ck(2*len(chosen)<=n,'parity join exceeds half-cycle')
    return chosen

def small_cycle(n,E,k):
    adj=adjacency(n,E);path=[0]
    # A greedy (k-2)-edge path, closed by a common neighbor.
    while len(path)<k-1:
        options=adj[path[-1]]-set(path)
        ck(options,'short path failed');path.append(min(options))
    closing=(adj[path[0]]&adj[path[-1]])-set(path)
    ck(closing,'common-neighbor cycle premise not met')
    return path+[min(closing)]

def validate_repair(n,E,removed):
    ck(removed<=E,'repair removes absent edge')
    rest=E-removed;deg=[0]*n
    for u,v in rest:deg[u]+=1;deg[v]+=1
    ck(all(d%2==0 for d in deg),'repaired odd degree')
    ck(len(rest)%3==0,'repaired edge count')
    ck(2*len(removed)<=n+10,'linear repair budget')
    used=collections.Counter(v for e in removed for v in e)
    ck(max(used.values(),default=0)<=4,'repair maximum degree')
    return rest

def repair(n,E):
    cyc=hamilton(n,E);deg=adjacency(n,E)
    odd={v for v in range(n) if len(deg[v])%2}
    par=parity_join(cyc,odd);rest=E-par
    mod=len(rest)%3
    cyc2=[] if mod==0 else small_cycle(n,rest,4 if mod==1 else 5)
    rem=par|(cycle_edges(cyc2) if cyc2 else set())
    out=validate_repair(n,E,rem)
    return out,{'hamilton_cycle':cyc,'odd_vertices':sorted(odd),'parity_edges':sorted(par),'modulus_cycle':cyc2,'removed_edges':len(rem),'remaining_edges':len(out),'minimum_degree':min(map(len,adjacency(n,out)))}

def core_masks_forward(r):
    E=list(it.combinations(range(r),2));ids={e:i for i,e in enumerate(E)}
    tris=[(sum(1<<ids[e] for e in it.combinations(t,2)),t) for t in it.combinations(range(r),3)]
    states={0:()}
    for mask,t in tris:
        for old,P in list(states.items()):
            if not old&mask:states.setdefault(old|mask,P+(t,))
    return states

def core_masks_reverse(r):
    E=list(it.combinations(range(r),2));ids={e:i for i,e in enumerate(E)}
    tris=[sum(1<<ids[e] for e in it.combinations(t,2)) for t in it.combinations(range(r),3)]
    @lru_cache(None)
    def yes(left):
        if not left:return True
        e=left&-left
        return any(t&e and left&t==t and yes(left^t) for t in tris)
    return {s for s in range(1<<len(E)) if s.bit_count()%3==0 and yes(s)}

def exact_q(ex,r,a,b,p,q,states,solver):
    full=(1<<(r*(r-1)//2))-1;best=F(-1);cert=None
    for used,P in states.items():
        E,L,A,B=ex.model(r,a,b,p,q,full^used,False)
        v,x,y=solver(A,B);ex.validate(A,B,v,x,y)
        if len(P)+v>best:best=len(P)+v;cert=(P,x,y,used)
    return best,cert

def finite_lp_checks(ex):
    rows=[];counts=[];max_gap=F(0);quarter=None
    for r in range(5):
        states=core_masks_forward(r);ck(set(states)==core_masks_reverse(r),'core enumerators disagree')
        nrow=0
        for a in range(r+1):
            for b in range(a,r+1):
                for p in range(ex.capfn(a)+1):
                    for q in range(ex.capfn(b)+1):
                        ex.tick();E,L,A,B=ex.model(r,a,b,p,q)
                        f,x,y=ex.lp_tableau(A,B);ff,xx,yy=ex.lp_revised(A,B)
                        ex.validate(A,B,f,x,y);ex.validate(A,B,ff,xx,yy);ck(f==ff,'joint LP disagreement')
                        Q,c=exact_q(ex,r,a,b,p,q,states,ex.lp_tableau)
                        QQ,cc=exact_q(ex,r,a,b,p,q,states,ex.lp_revised);ck(Q==QQ,'mixed Q disagreement')
                        J=ex.integer_edge_dp(r,a,b,p,q);JJ=ex.integer_object_enum(r,a,b,p,q)
                        E,L,A,B=ex.model(r,a,b,p,q,None,False)
                        M,lx,ly=ex.lp_tableau(A,B);ex.validate(A,B,M,lx,ly)
                        groups,D=ex.charge_leaf_groups(E,L,A,B,lx)
                        U=sum(v for v in lx if v.denominator==1)
                        AX={e for (kind,e),v in zip(L,lx) if kind=='a' and v==1}
                        BY={e for (kind,e),v in zip(L,lx) if kind=='b' and v==1}
                        hh=min(min(p,max(a-1,0))+min(q,max(b-1,0)),max(b-1,0))
                        ck(not AX&BY and len(AX|BY)==U,'rounded shared ownership')
                        ck(max(map(len,adjacency(r,AX|BY)),default=0)<=hh,'rounded degree bound')
                        allowed=all_edges(r)-(AX|BY)
                        pp=max((P for used,P in states.items() if all(e in allowed for t in P for e in it.combinations(t,2))),key=len)
                        ll=len(E)-U-3*len(pp)
                        ck(U+len(pp)<=J,'rounded allocation not integral feasible')
                        cap=(F(len(E))+2*M)/3;rho=cap-f
                        ck(J==JJ and J<=Q<=f and Q-J<=a+b,'Q sandwich')
                        ck(rho>=0 and D==M-U and D<=a+b,'leaf charge bound')
                        ck(f-(U+len(pp))==(2*D+ll)/3-rho,'integral repacking loss identity')
                        P,rx,ry,used=c;mass=sum(rx);leave=F(len(E))-3*len(P)-mass
                        ck(f-Q==(2*(M-mass)+leave)/3-rho,'objective-loss identity')
                        rows.append([r,a,b,p,q,str(f),str(Q),J,str(M),str(rho),len(states)])
                        max_gap=max(max_gap,f-Q);nrow+=1
        counts.append({'r':r,'cases':nrow})
    # The old quarter-valued input is used only to check that Q recomputes core supports.
    r,a,b,p,q=5,2,4,1,1;states=core_masks_forward(r)
    ck(set(states)==core_masks_reverse(r),'named core enumeration')
    Q,c=exact_q(ex,r,a,b,p,q,states,ex.lp_tableau)
    QQ,cc=exact_q(ex,r,a,b,p,q,states,ex.lp_revised)
    E,L,A,B=ex.model(r,a,b,p,q);f,x,y=ex.lp_tableau(A,B);ex.validate(A,B,f,x,y)
    ck(Q==QQ and Q<=f,'quarter control')
    quarter={'parameters':[r,a,b,p,q],'nu_star':str(f),'Q':str(Q),'chosen_core_triangles':c[0],'old_extreme_point_frozen':False}
    return {'counts':counts,'rows':rows,'maximum_observed_nu_star_minus_Q':str(max_gap),'named_quarter_regression':quarter}

def matchings(vertices):
    if not vertices:yield set();return
    u,*rest=vertices
    yield from matchings(rest)
    for i,v in enumerate(rest):
        for M in matchings(rest[:i]+rest[i+1:]):yield M|{edge(u,v)}

def run_repairs():
    # Complete Hamilton input sweep: all labeled graphs through n=5 meeting Dirac's premise.
    total=0
    for n in range(3,6):
        es=list(it.combinations(range(n),2))
        for mask in range(1<<len(es)):
            E={e for i,e in enumerate(es) if mask>>i&1}
            if 2*min(map(len,adjacency(n,E)))<n:continue
            cyc=hamilton(n,E);ck(cycle_edges(cyc)<=E and len(cyc)==n,'Hamilton test');total+=1
    joins=0
    for n in range(3,10):
        for mask in range(1<<n):
            if mask.bit_count()%2:continue
            T={v for v in range(n) if mask>>v&1};parity_join(list(range(n)),T);joins+=1
    dense=[]
    for n in (200,220,241,400):
        h=2*(n//80)
        deleted={edge(u,(u+j)%n) for u in range(n) for j in range(1,h//2+1)}
        E=all_edges(n)-deleted;rest,cert=repair(n,E)
        ck(h<=n//20 and 100*cert['minimum_degree']>=91*n,'dense threshold')
        dense.append({'n':n,'deleted_maximum_degree':h,**cert,'triangle_decomposition_executed':False,'certificate_kind':'divisibility_and_density_only'})
    # Smaller completed residual triangle decompositions are checked separately by literal edge recursion.
    finite=[]
    for n in (7,8,9,10):
        E=all_edges(n);rest,cert=repair(n,E)
        es=sorted(rest);pos={e:i for i,e in enumerate(es)}
        ts=[(sum(1<<pos[e] for e in it.combinations(t,2)),t) for t in it.combinations(range(n),3) if all(e in rest for e in it.combinations(t,2))]
        @lru_cache(None)
        def cover(left):
            if not left:return ()
            e=left&-left
            for t,v in ts:
                if t&e and left&t==t:
                    ans=cover(left^t)
                    if ans is not None:return (v,)+ans
            return None
        P=cover((1<<len(es))-1)
        ck(P is not None,'small residual decomposition missing')
        ck(collections.Counter(e for t in P for e in it.combinations(t,2))==collections.Counter(rest),'small decomposition edges')
        finite.append({'n':n,'repair':cert,'core_triangles':P,'external_threshold_invoked':False})
    n=200;a=100
    AX={edge(i,(i+1)%a) for i in range(a)}
    BY={edge(i,(i+3)%n) for i in range(n)}
    ck(not AX&BY and len(AX)==a and len(BY)==n,'proper two-prefix allocation')
    M=F(a+n);gamma=(1-F(2,n-1))/F(n-2);eta=F(2,(a-1)*(a-2))
    ck(gamma>=eta>=0,'large primal nonnegativity')
    ck((n-2)*gamma-(a-2)*eta+F(2,a-1)+F(2,n-1)==1,'AA fractional load')
    ck((n-2)*gamma+F(2,n-1)==1,'other fractional load')
    f=(F(n*(n-1)//2)+2*M)/3
    Pcore=F(n*(n-1)*(n-2),6)*gamma-F(a*(a-1)*(a-2),6)*eta
    ck(Pcore+M==f,'large primal objective')
    rest,cert=repair(n,all_edges(n)-(AX|BY))
    proper={'r':n,'a':a,'b':n,'p':2,'q':2,'leaf_optimum':str(M),'nu_star':str(f),'core_triangle_base_weight':str(gamma),'AAA_weight_subtraction':str(eta),'repair':cert,'triangle_decomposition_executed':False,'threshold_order_N_not_numerically_known':True}
    return {'hamilton_complete_small_inputs':total,'all_even_parity_subsets_checked':joins,'large_repair_certificates':dense,'small_literal_decompositions':finite,'proper_two_prefix_fractional_certificate':proper}

def mutations():
    out=[]
    def reject(name,fn):
        try:fn()
        except (ValueError,AssertionError):out.append(name)
        else:raise ValueError('undetected mutation '+name)
    reject('01_duplicate_cycle_vertex',lambda:cycle_edges([0,1,2,1]))
    reject('02_cycle_too_short',lambda:cycle_edges([0,1]))
    reject('03_odd_parity_set',lambda:parity_join(list(range(7)),{0}))
    reject('04_parity_vertex_outside_cycle',lambda:parity_join(list(range(7)),{0,7}))
    reject('05_missing_Dirac_hypothesis',lambda:hamilton(4,{(0,1),(1,2),(2,3)}))
    reject('06_graph_loop',lambda:adjacency(4,{(0,0)}))
    reject('07_repair_nonedge',lambda:validate_repair(7,all_edges(7),{(0,7)}))
    reject('08_parity_not_repaired',lambda:validate_repair(7,all_edges(7),{(0,1)}))
    reject('09_wrong_modulus_cycle',lambda:validate_repair(7,all_edges(7),cycle_edges([0,1,2,3])))
    reject('10_spent_edge_twice',lambda:ck(F(3,4)+F(3,4)<=1,'shared capacity'))
    reject('11_wrong_leaf_objective_coefficient',lambda:ck((F(3)+2*F(1))/3==F(3)/3+F(1)/3,'coefficient 2/3'))
    reject('12_total_order_used_as_core_order',lambda:ck(190>=F(91,100)*(200+100),'density order mismatch'))
    return out

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=pathlib.Path,required=True);arg=parser.parse_args()
    start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824));resource.setrlimit(resource.RLIMIT_CPU,(42,43))
    dep=pathlib.Path(__file__).resolve().parent.parent/'c25'/'extreme_audit.py'
    ck(hashlib.sha256(dep.read_bytes()).hexdigest()==DEP_SHA,'C25 dependency hash')
    spec=importlib.util.spec_from_file_location('c25_exact',dep);ex=importlib.util.module_from_spec(spec);spec.loader.exec_module(ex);ex.DEADLINE=start+39
    exact=finite_lp_checks(ex);repairs=run_repairs();mut=mutations()
    res={'verdict':'candidate_only','status':'finite_checks_passed','version':VERSION,'trusted_verifier_run':False,'best_verified_result':'none','exact':exact,'repairs':repairs,'mutations':mut,'scope':['Q is exhaustively optimized only through capped core order four plus one named order-five case.','Large graph outputs verify divisibility repair and minimum degree, not a triangle decomposition.','The uniform high-degree decomposition theorem is a source-backed dependency, not executed by this check.','Full two-prefix nu_star-Q=O(r) is still open.']}
    res['runtime']={'python':platform.python_version(),'arithmetic':'Fraction_and_integer','threads':1,'memory_bytes':1073741824,'cpu_seconds':42,'internal_LP_seconds':39,'elapsed_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'dependency_sha256':DEP_SHA}
    raw=(json.dumps(res,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode();ck(len(raw)<1048576,'output size')
    with arg.out.open('xb') as h:h.write(raw)
    print(json.dumps({'status':res['status'],'parameter_cases':len(exact['rows']),'hamilton_inputs':repairs['hamilton_complete_small_inputs'],'mutations':len(mut),'seconds':res['runtime']['elapsed_seconds'],'output_sha256':hashlib.sha256(raw).hexdigest()}))
if __name__=='__main__':main()
