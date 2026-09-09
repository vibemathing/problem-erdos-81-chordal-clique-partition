"""Finite parity-boundary checks of deleting at most two affine core vertices."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,resource,time,platform
import uniform_face_checker as c
ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);arg=ap.parse_args()
start=time.monotonic();c.DEADLINE=start+36
resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824));resource.setrlimit(resource.RLIMIT_CPU,(39,40))
ex=c.load_dependency();cases=[]
for removed in ({8},{7,8},{2}):
    pars=(9,3,9,1,1);W=c.certificate(*pars,integral_core=True)
    kept=[v for v in range(9) if v not in removed];idx={v:i for i,v in enumerate(kept)}
    new=(len(kept),sum(v<3 for v in kept),len(kept),1,1)
    restricted={(kind,tuple(idx[v] for v in obj)):w for (kind,obj),w in W.items() if not(set(obj)&removed)}
    stats=c.verify(*new,restricted,integer_core=True)
    charge={};loss=F(0)
    for (kind,obj),w in W.items():
        if not(set(obj)&removed) or not w:continue
        candidate_edges=list(__import__('itertools').combinations(obj,2)) if kind=='z' else [obj]
        e=min(e for e in candidate_edges if set(e)&removed)
        charge[e]=charge.get(e,F(0))+w;loss+=w
    c.ck(all(w<=1 for w in charge.values()) and loss<=len(removed)*8,'deleted-edge charging')
    E,L,A,B=ex.model(*new);v,x,y=ex.lp_tableau(A,B);ex.validate(A,B,v,x,y)
    uniform=(v==F(sum(B),3))
    if uniform:ex.validate(A,B,v,x,[F(1,3)]*len(B))
    upper=F(3+9,3)+len(removed)*8
    c.ck(v-F(stats['value'])<=upper<=8*new[0],'padding corollary')
    cases.append({'parameters':new,'deleted_core_vertices':sorted(removed),'uniform_face':uniform,'L':str(v),'Q_witness':stats['value'],'actual_witness_deficit':str(v-F(stats['value'])),'discarded_object_mass':str(loss),'edge_charge_upper_bound':len(removed)*8})
out={'verdict':'candidate_only','status':'finite_checks_passed','cases':cases,'Q_optimized':False,'trusted_verifier_run':False,'runtime':{'python':platform.python_version(),'arithmetic':'fractions.Fraction','threads':1,'memory_limit_bytes':1073741824,'CPU_limit_seconds':39,'internal_wall_seconds':36,'elapsed_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
p=arg.out;raw=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode();p.open('xb').write(raw);print(json.dumps(out))
