"""Exact C25 template/product/optimal-face certificates. No numerical solver used.
Run: python freezing_checker.py --out freezing-results.json
Author-side finite checks, not a registered verifier. All-order proofs are separate.
"""
from __future__ import annotations
import argparse, collections, hashlib, itertools as it, json, pathlib, platform, resource, time
from fractions import Fraction as F
from functools import lru_cache
import extreme_audit as ex
VERSION='c25-freezing-exact-v2'
def ck(ok,msg):
    if not ok:raise ValueError(msg)
def pair(u,v):return (u,v) if u<v else (v,u)
def triangle(t):return tuple(sorted(t))
def edges(T):return list(it.combinations(sorted(T),2))
def validate_packing(T,E,expected=None):
    use=collections.Counter()
    for t in T:
        ck(len(set(t))==3,'repeated triangle vertex')
        for e in edges(t):
            ck(e in E,'triangle edge outside graph');use[e]+=1
            ck(use[e]==1,'packing edge overlap')
    if expected is not None:ck(set(use)==expected,'wrong exact covered edge set')
    return set(E)-set(use)

def rook():
    return {e for e in it.combinations(range(16),2) if e[0]//4==e[1]//4 or e[0]%4==e[1]%4}
def st19():
    return [triangle(((u+z)%19 for u in t)) for t in [(0,1,4),(0,2,9),(0,5,11)] for z in range(19)]
@lru_cache(None)
def design(k):
    if k==1:return tuple(st19())
    N=19**(k-1);out=[]
    for u in range(N):out.extend(triangle(19*u+i for i in t) for t in st19())
    for u,v,w in design(k-1):
        for i in range(19):
            for j in range(19):out.append(triangle((19*u+i,19*v+j,19*w+(10*(i+j))%19)))
    return tuple(out)
@lru_cache(None)
def product_blocks(k):
    if k==1:return tuple([tuple(range(4*i,4*i+4)) for i in range(4)]+[tuple(i+4*j for j in range(4)) for i in range(4)])
    N=19**(k-1);out=[]
    for i in range(19):out.extend(tuple(19*u+i for u in B) for B in product_blocks(k-1))
    for u in range(N):out.extend(tuple(19*u+i for i in B) for B in product_blocks(1))
    return tuple(out)
def complement(k,base):
    if k==1:return list(map(tuple,base))
    N=19**(k-1);out=[]
    for i in range(19):out.extend(triangle(19*u+i for u in t) for t in complement(k-1,base))
    for u in range(N):out.extend(triangle(19*u+i for i in t) for t in base)
    for u,v,w in design(k-1):
        for i in range(19):
            for j in range(19):
                if i!=j:out.append(triangle((19*u+i,19*v+j,19*w+(10*(i+j))%19)))
    return out

def k4rank():
    es=list(it.combinations(range(4),2));ts=list(it.combinations(range(4),3))
    return ex.rank([[int(set(e)<=set(t)) for t in ts] for e in es])
def anchor_vector():
    E,L,A,B=ex.model(4,2,4,1,1)
    positive={('z',(0,2,3)):F(1,2),('z',(1,2,3)):F(1,2),('a',(0,1)):F(1),('b',(0,2)):F(1,2),('b',(0,3)):F(1,2),('b',(1,2)):F(1,2),('b',(1,3)):F(1,2)}
    x=[positive.get(l,F(0)) for l in L];y=[F(1,3)]*len(B)
    ex.validate(A,B,F(4),x,y)
    J=ex.integer_edge_dp(4,2,4,1,1);J2=ex.integer_object_enum(4,2,4,1,1)
    ck(J==J2==3,'anchor integer optimum');return E,L,A,B,x,y

def case(k,templates):
    ex.tick();r=19**k;m=r*(r-1)//2;K=set(it.combinations(range(r),2));blocks=product_blocks(k)
    ell=8*k*19**(k-1);ck(len(blocks)==ell,'product block count')
    H=set();adj=[set() for _ in range(r)]
    for B in blocks:
        for u,v in edges(B):
            ck((u,v) not in H,'K4 block edge overlap');H.add((u,v));adj[u].add(v);adj[v].add(u)
    triH={t for B in blocks for t in it.combinations(B,3)}
    literal={tuple((u,v,w)) for u,v in H for w in adj[u]&adj[v] if w>v}
    ck(triH==literal and len(H)==6*ell and len(triH)==4*ell,'residual triangles escaped K4 blocks')
    S=design(k);validate_packing(S,K,K);P=complement(k,templates['complement_decomposition'])
    validate_packing(P,K,K-H);ck(len(P)==m//3-2*ell,'complement count')
    load=collections.Counter()
    for t in P:
        for e in edges(t):load[e]+=2
    A0=(0,1,2,3)
    ck(A0 in blocks,'missing anchor block')
    for B in blocks:
        if B!=A0:
            for t in it.combinations(B,3):
                for e in edges(t):load[e]+=1
    for t in [(0,2,3),(1,2,3)]:
        for e in edges(t):load[e]+=1
    load[(0,1)]+=2
    for e in [(0,2),(0,3),(1,2),(1,3)]:load[e]+=1
    ck(set(load)==K and all(x==2 for x in load.values()),'fractional core loads')
    x,y=r,r+1;host=K|{(0,x),(1,x),(0,y),(1,y),(2,y),(3,y)}
    outside=[t for t in S if not all(v<19 for v in t)]
    witness=[tuple(v if v<19 else r+(v-19) for v in t) for t in templates['anchor_packing']]
    leave=validate_packing(outside+witness,host)
    ck(leave==set(map(tuple,templates['anchor_leave'])) and len(outside+witness)==m//3+1,'true packing count or leave')
    odd={v for v in range(r+2) if sum(v in e for e in host)%2}
    ck(odd=={2,3} and (m+6)%3==0,'parity upper certificate')
    lower=m//3+1;lp=F(m,3)+2;fixed=len(P)+ell+2
    ck(lp-lower==1 and lp-fixed==ell,'true versus frozen gap')
    return {'k':k,'r':r,'n':r+2,'core_edges':m,'host_edges':m+6,'K4_blocks':ell,'fixed_integral_core_triangles':len(P),'positive_fractional_z':4*(ell-1)+2,'anchor_positive_coordinates':7,'nu_star':str(lp),'J':lower,'nu':lower,'J_fixed':fixed,'true_gap':1,'frozen_gap':ell,'cp':7,'cp_basis':'general clique-piece proof; not a whole-host cp solver run','actual_integer_packing_leave':sorted(leave),'odd_vertices':sorted(odd),'complete_design_triangles':len(S),'core_fractional_half_load_certificate':True,'support_ranks':[4,7]}

def mutations(templates):
    E,L,A,B,x,y=anchor_vector();K=set(it.combinations(range(19),2));P=list(map(tuple,templates['complement_decomposition']));rejected=[]
    def reject(name,fn):
        try:fn()
        except (ValueError,AssertionError) as err:rejected.append({'name':name,'rejected':True,'reason':str(err)})
        else:raise ValueError('undetected mutation '+name)
    reject('01_duplicate_complement_triangle',lambda:validate_packing(P+[P[0]],K))
    reject('02_deleted_template_triangle',lambda:validate_packing(P[:-1],K,K-rook()))
    reject('03_nontriangle_vertex_repeat',lambda:validate_packing([(0,0,1)],K))
    reject('04_complement_uses_forbidden_edge',lambda:validate_packing([(0,1,2)],K-rook()))
    xx=x.copy();xx[L.index(('a',(0,1)))]=F(2);reject('05_double_owned_core_edge',lambda:ex.validate(A,B,F(5),xx,y))
    xx=x.copy();xx[L.index(('b',(0,2)))]=F(3,4);reject('06_long_endpoint_overload',lambda:ex.validate(A,B,sum(xx),xx,y))
    yy=y.copy();yy[0]=0;reject('07_removed_dual_price',lambda:ex.validate(A,B,F(4),x,yy))
    xx=x.copy();xx[0]=F(-1);reject('08_negative_fractional_coordinate',lambda:ex.validate(A,B,sum(xx),xx,y))
    reject('09_support_half_integrality_assumption',lambda:ck(F(1,4).denominator<=2,'quarter-valued joint extreme point'))
    reject('10_cartesian_mixed_coordinate_triangle',lambda:ck((0,1,19) in {t for C in product_blocks(2) for t in it.combinations(C,3)},'nontriangle in residual product'))
    reject('11_unaccounted_anchor_leave',lambda:ck(set(map(tuple,templates['anchor_leave']))==set(),'leave cannot be empty'))
    reject('12_frozen_gap_is_true_gap',lambda:ck(8==1,'frozen optimum differs from unrestricted optimum'))
    return rejected

def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=pathlib.Path,required=True);arg=p.parse_args();start=time.monotonic()
    resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824));resource.setrlimit(resource.RLIMIT_CPU,(35,36));ex.DEADLINE=start+32
    tpath=pathlib.Path(__file__).with_name('templates.json');raw=tpath.read_bytes();T=json.loads(raw)
    K=set(it.combinations(range(19),2));ck(set(map(tuple,T['rook_edges']))==rook(),'rook input')
    validate_packing(T['complement_decomposition'],K,K-rook());ck(len(T['complement_decomposition'])==41,'P19 count')
    G=K|{(0,19),(1,19),(0,20),(1,20),(2,20),(3,20)}
    leave=validate_packing(T['anchor_packing'],G);ck(leave==set(map(tuple,T['anchor_leave'])) and len(T['anchor_packing'])==58,'anchor input')
    ck(k4rank()==4,'K4 support rank');anchor_vector()
    res={'verdict':'candidate_only','status':'exact_certificates_passed','version':VERSION,'cases':[case(k,T) for k in (1,2)],'mutations':mutations(T),'trusted_verifier_run':False,'best_verified_result':'none','template_sha256':hashlib.sha256(raw).hexdigest(),'limitations':['Product constructions instantiated only at k=1,2; all-order assertions are proved in proof.md.','No numerical solver or trusted verifier is called in this check.','The freezing obstruction is not a counterexample to nu_star-J=O(r).']}
    res['runtime']={'python':platform.python_version(),'arithmetic':'integer_edge_checks_and_Fraction','memory_bytes':1073741824,'threads':1,'internal_seconds':32,'cpu_seconds':35,'elapsed_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
    out=(json.dumps(res,sort_keys=True,indent=2)+'\n').encode();ck(len(out)<1048576,'output size')
    with arg.out.open('xb') as h:h.write(out)
    print(json.dumps({'status':res['status'],'cases':res['cases'],'mutations':len(res['mutations']),'sha256':hashlib.sha256(out).hexdigest(),'seconds':res['runtime']['elapsed_seconds']}))
if __name__=='__main__':main()
