"""Replay one frozen two-prefix certificate. Generator-side, not a trusted gate."""
from fractions import Fraction as Q
import argparse, hashlib, importlib.util, itertools as it, json, pathlib, platform, resource, time
EXPECTED='6413676247c2dcc5533a86736e2762a0493d11c5e4c4d5dffd71bc6b2324fc80'
p=argparse.ArgumentParser();p.add_argument('--checker',type=pathlib.Path,required=True);p.add_argument('--out',type=pathlib.Path,required=True);args=p.parse_args()
b=args.checker.read_bytes()
if hashlib.sha256(b).hexdigest()!=EXPECTED:raise ValueError('checker digest mismatch')
if args.out.exists():raise ValueError('output must not exist')
resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824));resource.setrlimit(resource.RLIMIT_CPU,(20,22))
spec=importlib.util.spec_from_file_location('frozen',args.checker);c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
c.BUDGET=c.Budget(18,1000000,10000);start=time.monotonic()
r,a,b,p,q=6,4,6,2,1;n=r+p+q
es=c.pairs(r)+[(u,r+i)for i,d in enumerate([a]*p+[b]*q)for u in range(d)]
row,data=c.inspect_graph(n,c.encode(n,es),True)
c.require(tuple(row[k]for k in ('nu','nu_star','cp','lambda','p23'))==(8,'9',9,'11',13),'frozen values')
A=set(range(4));D={4,5,8};X={6,7};edges=set(es)
triples=[t for t in it.combinations(range(n),3)if all(e in edges for e in it.combinations(t,2))]
z=[]
for t in triples:
 s=set(t);z.append(Q(1,4)if len(s&A)==2 and len(s&X)==1 else Q(1,6)if len(s&A)==2 and len(s&D)==1 else Q(1,4)if len(s&A)==1 and len(s&D)==2 else Q(0))
y={e:Q(1)if set(e)<=A or set(e)<=D else Q(0)for e in es}
c.require(sum(z)==sum(y.values())==9,'named primal-dual sum')
for e in es:c.require(sum(w for t,w in zip(triples,z)if set(e)<=set(t))<=1,'named primal capacity')
for t in triples:c.require(sum(y[e]for e in it.combinations(t,2))>=1,'named dual capacity')
P=[tuple(map(int,t))for t in ('014','235','028','136','037','127','158','348')]
used=[e for t in P for e in it.combinations(t,2)]
c.require(len(used)==len(set(used))==24 and set(used)<=edges,'named integer packing')
HX={(0,1),(0,2),(1,2)};HY={(0,3),(1,4),(2,5)};coreP=[(0,4,5),(1,3,5),(2,3,4)]
ce=[e for t in coreP for e in it.combinations(t,2)]
c.require(not(HX&HY) and not(set(ce)&(HX|HY)) and len(ce)==len(set(ce)),'J ownership')
c.require(HX|HY|set(ce)==set(c.pairs(r)),'J covers core once')
c.require(max(sum(v in e for e in HX)for v in range(a))<=p,'short degree')
c.require(max(sum(v in e for e in HY)for v in range(b))<=q,'long degree')
report={'verdict':'candidate_only','status':'finite_named_replay_pass','trusted_verifier_run':False,'best_verified_result':'none','scope':'One normalized nine-vertex graph, not a new complete enumeration','python':platform.python_version(),'arithmetic':'fractions.Fraction','checker_sha256':EXPECTED,'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'row':row,'maximal_cliques':[[0,1,2,3,6],[0,1,2,3,7],[0,1,2,3,4,5,8]],'joint_integer_allocation':9,'named_packing':P,'exact_solver_certificate':c.certificate_payload(data),'elapsed_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'budgets':{'wall_seconds':18,'cpu_seconds':20,'memory_bytes':1073741824,'threads':1}}
raw=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode()
if len(raw)>1048576:raise ValueError('output bound')
args.out.write_bytes(raw)
print(json.dumps({k:report[k]for k in ('status','python','row','elapsed_seconds','max_rss_kib')}))
