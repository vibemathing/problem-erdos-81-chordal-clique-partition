"""Independent-library cross-checks for C32 finite certificates.
Uses tuple vectors, NetworkX matching predicates, and SciPy LP for small type models.
Not a trusted verifier and not used by the all-order proofs.
"""
from __future__ import annotations
import hashlib, itertools as it, json, pathlib, platform, sys, time
from fractions import Fraction as F
import networkx as nx
import numpy as np
from scipy.optimize import linprog

BASE_P=[(0,3,4),(1,6,8),(2,4,7),(3,5,6),(5,7,8)]
BASE_A=[(0,1),(0,2),(1,2)]
BASE_B=[(0,5),(0,6),(0,7),(0,8),(1,3),(1,4),(1,5),(1,7),(2,3),(2,5),(2,6),(2,8),(3,7),(3,8),(4,5),(4,6),(4,8),(6,7)]

def pairs(t):return {tuple(sorted(e)) for e in it.combinations(t,2)}
def vectors(k):return list(it.product(range(3),repeat=k))
def negsum(u,v):return tuple((-x-y)%3 for x,y in zip(u,v))
def lines(k):
    V=vectors(k);out=set()
    for u,v in it.combinations(V,2):out.add(tuple(sorted((u,v,negsum(u,v)))))
    return out

def affine_check(k):
    V=vectors(k);L=lines(k);cnt={}
    for t in L:
        for e in it.combinations(t,2):cnt[frozenset(e)]=cnt.get(frozenset(e),0)+1
    assert len(cnt)==len(V)*(len(V)-1)//2 and set(cnt.values())=={1}
    return len(V),len(L)

def base_check():
    E={};
    for t in BASE_P:
        for e in pairs(t):E[e]=E.get(e,0)+1
    for e in BASE_A+BASE_B:E[e]=E.get(e,0)+1
    assert len(E)==36 and set(E.values())=={1}
    GA=nx.Graph();GA.add_nodes_from(range(3));GA.add_edges_from(BASE_A)
    GB=nx.Graph();GB.add_nodes_from(range(9));GB.add_edges_from(BASE_B)
    assert dict(GA.degree())=={0:2,1:2,2:2}
    assert set(dict(GB.degree()).values())=={4}
    return {'core_edges':len(E),'alpha_degrees':dict(GA.degree()),'beta_degree_set':sorted(set(dict(GB.degree()).values()))}

def type_lp(r,a,p,q):
    c=r-a
    rows=[];rhs=[]
    if a>=2:rows.append([a-2,c,0,0,1,1,0,0]);rhs.append(1)
    if a and c:rows.append([0,a-1,c-1,0,0,0,1,0]);rhs.append(1)
    if c>=2:rows.append([0,0,a,c-2,0,0,0,1]);rhs.append(1)
    if a:
        rows.append([0,0,0,0,a-1,0,0,0]);rhs.append(p)
        rows.append([0,0,0,0,0,a-1,c,0]);rhs.append(q)
    if c:rows.append([0,0,0,0,0,0,a,c-1]);rhs.append(q)
    res=linprog(np.zeros(8),A_eq=np.array(rows,float),b_eq=np.array(rhs,float),bounds=[(0,None)]*8,method='highs')
    return res.success

def main(out):
    start=time.monotonic();aff=[affine_check(k) for k in (2,3)]
    base=base_check()
    face3=[]
    for r in (9,27):
        for a in range(r+1):face3.append({'r':r,'a':a,'p3q3_type_saturated':type_lp(r,a,3,3)})
    assert not nx.algorithms.matching.is_matching(nx.Graph(BASE_A),set(BASE_A))
    result={
      'status':'independent_generator_crosscheck_passed','verdict':'candidate_only','trusted_verifier_run':False,
      'python':platform.python_version(),'networkx':nx.__version__,'numpy':np.__version__,
      'scipy':__import__('scipy').__version__,'tuple_affine_orders':aff,'base_seed':base,
      'p3q3_type_feasibility':face3,
      'scope':['Tuple-vector affine implementation is independent of checker.py integer encoding.','SciPy floating LP only checks small symmetric feasibility and is not a proof input.','No all-order dense decomposition theorem is executed.'],
      'wall_seconds':time.monotonic()-start,
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    }
    raw=(json.dumps(result,sort_keys=True,indent=2)+'\n').encode();pathlib.Path(out).write_bytes(raw)
    print(json.dumps({'status':result['status'],'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'seconds':result['wall_seconds']}))
if __name__=='__main__':main(sys.argv[1])
