"""R07 C23 finite exact audit; candidate-side replay, never an admission gate.
Python >=3.11, standard library only. No network, shell commands or ledger writes.
Usage: python exact_checker.py --max-order 7 --seconds 1200 --out <directory>
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import itertools as it
import json
import math
import pathlib
import platform
import time
from fractions import Fraction as Q
from functools import lru_cache

VERSION = 'c23-exact-v1'
DEADLINE = float('inf')
MAX_PIVOTS = 10000
MAX_STATES = 1000000

class Reject(ValueError):
    pass

def require(ok, message):
    if not ok:
        raise Reject(message)

def tick():
    if time.monotonic() > DEADLINE:
        raise TimeoutError('bounded audit deadline')

def pairs(n):
    return list(it.combinations(range(n), 2))

def edge_list(n, code):
    return [e for i, e in enumerate(pairs(n)) if (code >> i) & 1]

def encode(n, edges):
    lookup = {e: i for i, e in enumerate(pairs(n))}
    unique = {tuple(sorted(e)) for e in edges}
    require(all(e in lookup for e in unique), 'invalid simple edge')
    return sum(1 << lookup[e] for e in unique)

def adjacency(n, code):
    a = [0] * n
    for u, v in edge_list(n, code):
        a[u] |= 1 << v
        a[v] |= 1 << u
    return a

def vertices(s):
    return [i for i in range(s.bit_length()) if (s >> i) & 1]

def is_clique(a, s):
    return all((s ^ (1 << v)) & ~a[v] == 0 for v in vertices(s))

def canonical(n, code):
    """Exact isomorphism key: all permutations within sorted degree classes."""
    tick()
    a = adjacency(n, code)
    degrees = sorted(set(x.bit_count() for x in a))
    groups = [[v for v in range(n) if a[v].bit_count() == d] for d in degrees]
    best = None
    ps = pairs(n)
    for parts in it.product(*(it.permutations(g) for g in groups)):
        p = tuple(it.chain.from_iterable(parts))
        value = sum(1 << j for j, (u, v) in enumerate(ps) if (a[p[u]] >> p[v]) & 1)
        if best is None or value < best:
            best = value
    return 0 if best is None else best

def extend(n, old_code, nb):
    return encode(n, edge_list(n-1, old_code) + [(v, n-1) for v in vertices(nb)])

def generate_level(n, previous, simplicial_only=False):
    result = set()
    for code in sorted(previous):
        a = adjacency(n-1, code)
        for nb in range(1 << (n-1)):
            if not simplicial_only or is_clique(a, nb):
                result.add(canonical(n, extend(n, code, nb)))
    return result

def no_holes(n, code):
    """Definition-based test, not the simplicial-elimination test."""
    a = adjacency(n, code)
    for s in range(1 << n):
        vs = vertices(s)
        if len(vs) < 4 or any((a[v] & s).bit_count() != 2 for v in vs):
            continue
        reached, todo = 0, 1 << vs[0]
        while todo:
            reached |= todo
            todo = s & ~reached & __neighbors(a, reached)
        if reached == s:
            return False
    return True

def __neighbors(a, s):
    nb = 0
    for v in vertices(s):
        nb |= a[v]
    return nb

def suffix_peo(n, code, tail=0):
    a = adjacency(n, code)
    require(is_clique(a, tail), 'tail is not a clique')
    remaining, order = (1 << n)-1, []
    while remaining & ~tail:
        good = [v for v in vertices(remaining & ~tail) if is_clique(a, a[v] & remaining)]
        if not good:
            return None
        v = good[0]
        order.append(v)
        remaining ^= 1 << v
    return order + vertices(tail)

def clique_data(n, code):
    edges = edge_list(n, code)
    a = adjacency(n, code)
    vs = [s for s in range(1 << n) if s.bit_count() >= 2 and is_clique(a, s)]
    masks = [sum(1 << j for j, (u, v) in enumerate(edges) if s & (1 << u) and s & (1 << v)) for s in vs]
    tris = [mask for s, mask in zip(vs, masks) if s.bit_count() == 3]
    return edges, vs, masks, tris

def solve_linear(A, b):
    n = len(b)
    B = [[Q(x) for x in row] + [Q(rhs)] for row, rhs in zip(A, b)]
    for j in range(n):
        i = next((i for i in range(j, n) if B[i][j]), None)
        require(i is not None, 'singular basis')
        B[j], B[i] = B[i], B[j]
        pivot = B[j][j]
        B[j] = [x / pivot for x in B[j]]
        for i in range(n):
            if i != j and B[i][j]:
                k = B[i][j]
                B[i] = [x-k*y for x, y in zip(B[i], B[j])]
    return [B[i][-1] for i in range(n)]

def packing_lp(m, triangles):
    """Max packing by a rational tableau with the slack basis (Bland rule)."""
    h = len(triangles)
    rows = [[Q((T >> e) & 1) for T in triangles] + [Q(e == j) for j in range(m)] + [Q(1)] for e in range(m)]
    rows.append([Q(-1)]*h + [Q(0)]*(m+1))
    basis = list(range(h, h+m))
    for _ in range(MAX_PIVOTS):
        tick()
        entering = next((j for j in range(h+m) if rows[-1][j] < 0), None)
        if entering is None:
            z = [Q(0)] * h
            for i, j in enumerate(basis):
                if j < h:
                    z[j] = rows[i][-1]
            q = rows[-1][h:h+m]
            value = rows[-1][-1]
            require(all(x >= 0 for x in z+q), 'negative packing primal/dual')
            require(all(sum(z[j] for j,T in enumerate(triangles) if (T >> e)&1) <= 1 for e in range(m)), 'packing overload')
            require(all(sum(q[e] for e in vertices(T)) >= 1 for T in triangles), 'packing dual underload')
            require(sum(z) == sum(q) == value, 'packing duality gap')
            return value, z, q
        possible = [i for i in range(m) if rows[i][entering] > 0]
        require(bool(possible), 'unexpected unbounded packing LP')
        leaving = min(possible, key=lambda i: (rows[i][-1]/rows[i][entering], basis[i]))
        p = rows[leaving][entering]
        rows[leaving] = [x/p for x in rows[leaving]]
        for i in range(m+1):
            if i != leaving and rows[i][entering]:
                p = rows[i][entering]
                rows[i] = [x-p*y for x,y in zip(rows[i], rows[leaving])]
        basis[leaving] = entering
    raise TimeoutError('packing pivot cap')

def equality_lp(m, triangles):
    """Min exact partition by revised simplex; no packing identity is used."""
    if not m:
        return Q(0), [], []
    cols = [[Q(e == j) for e in range(m)] for j in range(m)]
    cols += [[Q((T >> e)&1) for e in range(m)] for T in triangles]
    basis = list(range(m))
    for _ in range(MAX_PIVOTS):
        tick()
        B = [[cols[j][i] for j in basis] for i in range(m)]
        xB = solve_linear(B, [1]*m)
        w = solve_linear(list(map(list, zip(*B))), [1]*m)
        entering = next((j for j,c in enumerate(cols) if j not in basis and 1-sum(a*b for a,b in zip(w,c)) < 0), None)
        if entering is None:
            x = [Q(0)] * len(cols)
            for i,j in enumerate(basis):
                x[j] = xB[i]
            validate_fractional(m, triangles, x, w)
            return sum(x), x, w
        d = solve_linear(B, cols[entering])
        possible = [i for i in range(m) if d[i] > 0]
        require(bool(possible), 'unexpected unbounded equality LP')
        leaving = min(possible, key=lambda i: (xB[i]/d[i], basis[i]))
        basis[leaving] = entering
    raise TimeoutError('equality pivot cap')

def validate_fractional(m, triangles, x, w):
    require(len(x) == m+len(triangles) and len(w) == m, 'fractional dimensions')
    require(all(a >= 0 for a in x), 'negative fractional piece')
    require(all(a <= 1 for a in w), 'dual edge bound')
    for e in range(m):
        require(x[e]+sum(x[m+j] for j,T in enumerate(triangles) if (T >> e)&1) == 1, 'edge equality')
    require(all(sum(w[e] for e in vertices(T)) <= 1 for T in triangles), 'dual triangle bound')
    require(sum(x) == sum(w), 'fractional duality gap')
    require(all(a >= -1 for a in w), 'optimal signed dual below clipping bound')

def validate_partition(full, allowed, parts):
    used = 0
    for p in parts:
        require(p in allowed and p != 0, 'invalid clique piece')
        require(not used & p, 'overlapping pieces')
        used |= p
    require(used == full, 'partition missing edges')

def integer_partition(m, masks):
    allowed = set(masks)
    full = (1 << m)-1
    @lru_cache(None)
    def rec(left):
        tick()
        if not left:
            return ()
        if left in allowed:
            return (left,)
        require(rec.cache_info().currsize < MAX_STATES, 'partition state cap')
        edge = left & -left
        options = sorted((p for p in masks if p & edge and p & left == p), key=lambda p: (-p.bit_count(),p))
        lower = math.ceil(left.bit_count()/max(p.bit_count() for p in masks))
        best = None
        for p in options:
            answer = (p,) + rec(left ^ p)
            if best is None or len(answer) < len(best):
                best = answer
            if len(best) == lower:
                break
        require(best is not None, 'no exact partition')
        return best
    parts = rec(full)
    validate_partition(full, allowed, parts)
    return len(parts), parts

def integer_packing(tris):
    """Maximum independent set of the triangle conflict graph, not edge DP."""
    conflicts = [sum(1 << j for j,U in enumerate(tris) if U & T) for T in tris]
    @lru_cache(None)
    def rec(active):
        tick()
        if not active:
            return ()
        require(rec.cache_info().currsize < MAX_STATES, 'packing state cap')
        i = max(vertices(active), key=lambda i: ((conflicts[i] & active).bit_count(),-i))
        no = rec(active & ~(1 << i))
        yes = (i,) + rec(active & ~conflicts[i])
        return yes if len(yes) > len(no) else no
    ids = rec((1 << len(tris))-1)
    used = 0
    for i in ids:
        require(not used & tris[i], 'packing conflict')
        used |= tris[i]
    return len(ids), ids

def all_maximizers(n, code, w):
    a = adjacency(n, code)
    E = {e:j for j,e in enumerate(edge_list(n,code))}
    values = []
    for u in range(n):
        for s in range(1 << n):
            if s & ~a[u] == 0 and is_clique(a, s):
                value = sum((w[E[tuple(sorted((u,v)))]] for v in vertices(s)), Q(0))
                values.append((value,u,s))
    M = max((v for v,_,_ in values), default=Q(0))
    return M, [(u,s) for v,u,s in values if v == M]

def check_slack(n, code, lam, cp, w, u, s, M):
    E = edge_list(n, code)
    pos = {e:j for j,e in enumerate(E)}
    actual_M, maxima = all_maximizers(n, code, w)
    require(M == actual_M and (u,s) in maxima, 'not a global maximizer')
    order = suffix_peo(n, code, s)
    require(order is not None, 'suffix PEO missing')
    r, t = s.bit_count(), n-s.bit_count()
    theta = t-r+1
    P = r-M
    core = [j for j,(a,b) in enumerate(E) if s & (1 << a) and s & (1 << b)]
    R = sum((1-w[pos[tuple(sorted((u,a)))]]-w[pos[tuple(sorted((u,b)))]]-w[pos[(a,b)]] for j,(a,b) in enumerate(E) if j in core), Q(0))
    D = t*M-(lam-sum(w[j] for j in core))
    Bn, g = n*(n+1)//6, r*t-r*(r-1)//2
    slack = Bn-lam
    require(min(P,R,D) >= 0, 'negative slack')
    require(lam == g-theta*P-R-D, 'slack identity')
    rho = Q((2*n+1)**2,24)-Bn
    require(Q(3,2)*(r-Q(2*n+1,6))**2+theta*P+R+D == slack+rho, 'square identity')
    ranks = {v:i for i,v in enumerate(order)}
    ds = []
    for v in order[:t]:
        row = [j for j,(a,b) in enumerate(E) if v in (a,b) and ranks[b if a==v else a] > ranks[v]]
        deficit = M-sum(w[j] for j in row)
        require(deficit >= 0, 'row exceeds M')
        require(-sum(w[j] for j in row if w[j] < 0) <= deficit, 'negative row load')
        ds.append(deficit)
    require(sum(ds) == D, 'PEO aggregate differs')
    if theta >= 0:
        require(theta*P+R+D <= slack, 'low-core slack bound')
        require(Q(3,2)*(r-Q(2*n+1,6))**2 <= slack+rho, 'low-core square bound')
    else:
        require(lam <= Q(math.comb(n,2)-math.comb(t,2),3), 'dense compression')
        require(slack >= Q(n-1,3)+Q(t*(t-1),6), 'dense slack')
        require(cp <= r*t+math.comb(t,2)+1, 'dense integer partition')
    return [r,t,theta,str(P),str(R),str(D)]

def audit_graph(n, code, chordal=None, keep=False):
    E, cv, masks, tris = clique_data(n, code)
    m = len(E)
    ch = no_holes(n, code)
    require(ch == (suffix_peo(n,code) is not None), 'chordality recognizers disagree')
    if chordal is not None:
        require(ch == chordal, 'fixture chordality')
    ns, z, q = packing_lp(m, tris)
    lam, x, w = equality_lp(m, tris)
    nu, packed = integer_packing(tris)
    cp, cpp = integer_partition(m, masks)
    p23, p23p = integer_partition(m, [1 << e for e in range(m)] + tris)
    require(cp <= p23 == m-2*nu, 'integer identity')
    require(lam == m-2*ns, 'fractional identity')
    require(p23 == lam+2*(ns-nu), 'rounding identity')
    checked = 0
    if ch:
        require(lam <= n*(n+1)//6, 'chordal fractional bound')
        for s in range(1 << n):
            if is_clique(adjacency(n,code),s):
                require(suffix_peo(n,code,s) is not None, 'arbitrary clique suffix')
        if m:
            duals = {tuple(w),tuple(1-2*qq for qq in q),tuple((ww+1-2*qq)/2 for ww,qq in zip(w,q))}
            for dual in duals:
                validate_fractional(m, tris, x, dual)
                M, mx = all_maximizers(n,code,dual)
                for u,s in mx:
                    check_slack(n,code,lam,cp,dual,u,s,M)
                    checked += 1
    data = dict(n=n, code=code, chordal=ch, m=m, nu=nu, nu_star=str(ns), lambda_value=str(lam), p23=p23, cp=cp, maximizer_checks=checked)
    if keep:
        data.update(edges=E, clique_vertex_masks=cv, triangle_edge_masks=tris, packing_triangle_ids=packed, packing_weights=list(map(str,z)), packing_dual=list(map(str,q)), partition_weights=list(map(str,x)), signed_dual=list(map(str,w)), cp_pieces=cpp, p23_pieces=p23p)
    return data

def split_graph(r,t):
    return r+t, encode(r+t, list(it.combinations(range(r),2))+[(a,b) for a in range(r) for b in range(r,r+t)])

def regression_and_mutations():
    fixtures = {'C4':(4,encode(4,[(0,1),(1,2),(2,3),(0,3)])), 'K4':(4,63), 'diamond':(4,encode(4,[(0,1),(0,2),(1,2),(0,3),(1,3)])), 'J32':split_graph(3,2), 'P6square':(6,encode(6,[(i,j) for i,j in pairs(6) if j-i<=2])), 'windmill2':(7,encode(7,list(it.combinations([0,1,2,3],2))+list(it.combinations([0,4,5,6],2))))}
    for n in range(0,8):
        fixtures['K'+str(n)] = (n,(1 << (n*(n-1)//2))-1)
        fixtures['tree'+str(n)] = (n,encode(n,[(i,i+1) for i in range(n-1)]))
    for r in range(1,7):
        for t in sorted({max(0,r-2),r-1,r}):
            if r+t <= 7:
                fixtures[f'J{r}_{t}'] = split_graph(r,t)
    results = {name:audit_graph(*g, keep=True) for name,g in fixtures.items()}
    expected_controls = {
        'C4': (4,0,0,4,4,4), 'K3': (3,1,1,1,1,1),
        'K4': (6,1,2,2,4,1), 'diamond': (5,1,1,3,3,3),
        'J32': (9,2,3,3,5,4), 'P6square': (9,2,2,5,5,5),
        'windmill2': (12,2,4,4,8,2),
    }
    for name, expected in expected_controls.items():
        d = results[name]
        actual = (d['m'],d['nu'],Q(d['nu_star']),Q(d['lambda_value']),d['p23'],d['cp'])
        require(actual == expected, 'explicit control mismatch: '+name)
    for n in range(8):
        d = results['tree'+str(n)]
        require(d['m'] == max(0,n-1) and d['nu'] == 0 and Q(d['nu_star']) == 0
                and d['cp'] == d['p23'] == Q(d['lambda_value']) == d['m'],
                'tree control')
        d = results['K'+str(n)]
        if n >= 3:
            require(Q(d['lambda_value']) == Q(n*(n-1),6) and d['cp'] == 1,
                    'complete graph fractional control')
    for name,g in fixtures.items():
        if not name.startswith('J') or '_' not in name:
            continue
        r,t = map(int,name[1:].split('_'))
        expected = Q(0 if r<2 else 1) if t==0 and r<3 else (Q(math.comb(r,2),3) if t==0 else Q(r*t-math.comb(r,2)) if t>=r-1 else Q(r*t+math.comb(r,2),3))
        require(Q(results[name]['lambda_value']) == expected, 'split branch formula')
    k3 = results['K3']; diamond=results['diamond']; j32=results['J32']
    mutation = []
    def must_reject(name, fn):
        try:
            fn()
        except Reject as exc:
            mutation.append({'name':name,'rejected':True,'reason':str(exc)})
        else:
            raise Reject('undetected mutation: '+name)
    def vf(d,x=None,w=None):
        validate_fractional(d['m'],d['triangle_edge_masks'],list(map(Q,d['partition_weights'])) if x is None else x,list(map(Q,d['signed_dual'])) if w is None else w)
    must_reject('01_cp_equals_lambda',lambda:require(j32['cp']==Q(j32['lambda_value']),'cp/fractional confusion'))
    must_reject('02_wrong_integer_factor',lambda:require(k3['p23']==k3['m']-3*k3['nu'],'wrong packing factor'))
    must_reject('03_cover_as_partition',lambda:validate_partition(31,set(clique_data(4,fixtures['diamond'][1])[2]),diamond['triangle_edge_masks']))
    must_reject('04_missing_edge',lambda:validate_partition(7,{1,2,4,7},[1,2]))
    must_reject('05_nonclique_piece',lambda:validate_partition(15,set(clique_data(*fixtures['C4'])[2]),[3,12]))
    x=list(map(Q,k3['partition_weights'])); x[-1]=-1
    must_reject('06_negative_fractional_piece',lambda:vf(k3,x=x))
    x=list(map(Q,k3['partition_weights'])); x[-1]=2
    must_reject('07_fractional_overload',lambda:vf(k3,x=x))
    must_reject('08_missing_triangle_dual_constraint',lambda:vf(k3,w=[Q(1)]*3))
    w=[Q(0)]*j32['m']
    must_reject('09_feasible_but_nonoptimal_dual',lambda:vf(j32,w=w))
    must_reject('10_omit_chordality',lambda:require(Q(results['C4']['lambda_value'])<=4*5//6,'C4 outside-domain control'))
    must_reject('11_drop_low_core_sign_guard',lambda:require(Q(3,2)*(3-Q(9,6))**2<=Q(1)+Q(3,8),'dense K4 square control'))
    d=results['P6square']; dw=list(map(Q,d['signed_dual'])); M,mx=all_maximizers(d['n'],d['code'],dw)
    must_reject('12_nonmaximizing_pair',lambda:check_slack(d['n'],d['code'],Q(d['lambda_value']),d['cp'],dw,0,0,M))
    must_reject('13_nonclique_suffix',lambda:suffix_peo(3,encode(3,[(0,1),(1,2)]),5))
    must_reject('14_p23_equals_cp',lambda:require(results['K4']['p23']==results['K4']['cp'],'unrestricted piece confusion'))
    require(len(mutation)>=8,'insufficient mutations')
    return results, mutation

def run(max_order):
    levels={0:{0}}; chordals={0:{0}}
    rows=[]; counters=[]; corpus=[]
    cert_stream=hashlib.sha256()
    for n in range(max_order+1):
        tick()
        if n:
            levels[n]=generate_level(n,levels[n-1])
            chordals[n]=generate_level(n,chordals[n-1],True)
        selected={code for code in levels[n] if no_holes(n,code)}
        require(selected==chordals[n], 'two complete chordal generation methods disagree')
        for code in sorted(levels[n]):
            require(no_holes(n,code)==(suffix_peo(n,code) is not None),'recognizers disagree')
            corpus.append([n,code])
        for code in sorted(selected):
            row=audit_graph(n,code,True,True)
            cert_stream.update((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode())
            rows.append({key:row[key] for key in ('n','code','m','nu','nu_star','lambda_value','p23','cp','maximizer_checks')})
        counters.append(dict(n=n,all_graphs=len(levels[n]),chordal_graphs=len(selected)))
    controls,mutations=regression_and_mutations()
    return dict(verdict='candidate_only',status='finite_generator_selfcheck_pass',checker_version=VERSION,python_version=platform.python_version(),max_complete_order=max_order,counts=counters,all_graphs_checked=sum(c['all_graphs'] for c in counters),chordal_lp_cases=len(rows),all_maximizers_of_sampled_optimal_duals_checked=sum(r['maximizer_checks'] for r in rows),optimal_dual_scope='Two exact solver optima and their midpoint; not exhaustive over the continuous optimal face.',certificate_stream_sha256=cert_stream.hexdigest(),mutations=mutations,control_count=len(controls),trusted_verifier_run=False,best_verified_result='none'),rows,controls,corpus

def write_bounded(path,data):
    require(len(data)<=1048576,'output file exceeds 1 MiB')
    with path.open('xb') as handle:
        handle.write(data)

def main():
    global DEADLINE
    p=argparse.ArgumentParser()
    p.add_argument('--max-order',type=int,default=7)
    p.add_argument('--seconds',type=int,default=1200)
    p.add_argument('--out',type=pathlib.Path,required=True)
    args=p.parse_args()
    require(0<=args.max_order<=7 and 1<=args.seconds<=1800,'budget limits')
    DEADLINE=time.monotonic()+args.seconds
    try:
        import resource
        resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824))
        resource.setrlimit(resource.RLIMIT_CPU,(args.seconds+2,args.seconds+3))
    except ImportError:
        raise Reject('POSIX resource enforcement required for replay')
    require(not args.out.exists() or not any(args.out.iterdir()), 'output directory must be fresh')
    args.out.mkdir(parents=True,exist_ok=True)
    summary,rows,controls,corpus=run(args.max_order)
    summary['checker_sha256']=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    summary['budgets']={'wall_seconds':args.seconds,'memory_bytes':1073741824,'threads':1,'max_pivots_per_lp':MAX_PIVOTS,'max_states_per_integer_dp':MAX_STATES,'max_file_bytes':1048576}
    outputs={}
    sio=io.StringIO(); writer=csv.DictWriter(sio,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    outputs['finite-table.csv']=sio.getvalue().encode()
    outputs['controls.json']=(json.dumps(controls,sort_keys=True,separators=(',',':'))+'\n').encode()
    outputs['corpus.json']=(json.dumps(corpus,separators=(',',':'))+'\n').encode()
    summary['outputs']={name:{'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)} for name,data in outputs.items()}
    for name,data in outputs.items():
        write_bounded(args.out/name,data)
    data=(json.dumps(summary,sort_keys=True,indent=2)+'\n').encode()
    write_bounded(args.out/'summary.json',data)
    print(json.dumps(summary,sort_keys=True))
    return 0

if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (Reject,TimeoutError) as exc:
        print(json.dumps({'verdict':'candidate_only','status':'NONTERMINAL_CHECKPOINT','error':str(exc)}))
        raise SystemExit(2)
