# Balanced one-depth nested graphs: shared capacity allocated once

Candidate ID: candidate:erdos81-a01-c24-balanced-one-depth
Repository: vibemathing/problem-erdos-81-chordal-clique-partition
Problem: problem:erdos-81-chordal-clique-partition
Attempt: attempt:web-20260906-erdos81-a01
Route: route:split-extremal-reduction-v1
Graph: graph:erdos81-initial-v1
Transport obligation: obligation:erdos81-split-extremal-reduction
Base: 09c2b6f3e277eb20fc34d0add65ee8d027c5bb37
Verdict: candidate_only. best_verified_result: none.

## The exact restricted theorem

Let A,B,L be disjoint with sizes d,q,t. The core A union B is complete, L is independent, and every vertex of L is adjacent exactly to A. All sizes are nonnegative. Suppose

    t>=d-1 and d>=q-1.                                      (1)

Write n=d+q+t, nu for maximum edge-disjoint triangle packing and nu_star for its fractional capacity-one relaxation. For s,u with u>=s-1 define epsilon(s,u)=(s-1)/2 if s is odd and u=s-1, and zero otherwise. Then

    nu_star=binom(d,2)+binom(q,2),
    0<=nu_star-nu<=epsilon(d,t)+epsilon(q,d)<=n/2.           (2)

This is a restricted all-order theorem candidate. It does NOT prove a bound for arbitrary chains of prefix depths, arbitrary one-depth parameters outside (1), leaf blocks with internal edges, or the general chordal root. It does not assume that the missing join has O(n) edges. For example d=q=t=k satisfies (1) with k^2 absent B-to-L edges, and both epsilon terms are zero.

## Upper bound starting from an arbitrary fractional packing

Let F be the union of the edges internal to A and internal to B. Every triangle of the graph contains an edge in F: a triangle meeting L uses two A vertices, and a core triangle has two vertices in the same one of the two parts A,B. Order F and charge each triangle's fractional weight to the first internal edge it contains. Each edge receives weight at most its original load, hence at most one. Thus any exact fractional packing z satisfies

    sum_T z_T<=|F|=binom(d,2)+binom(q,2).                  (3)

Equivalently, prices one on F and zero elsewhere form a feasible packing dual. There is one shared core budget; no separator occurrence is charged separately.

A matching fractional certificate assigns weight 1/t to every triangle with one L vertex and two A vertices, and weight 1/d to every triangle with one A vertex and two B vertices. Empty triangle families are omitted before division. The AA and BB edge loads are exactly one. The A-to-L loads are (d-1)/t<=1; the A-to-B loads are (q-1)/d<=1. These families use disjoint edge classes, and their total weights are binom(d,2) and binom(q,2). This proves equality in (3).

## Integer allocation without repeated core-edge spending

For even s, factor K_s into s-1 perfect matchings explicitly. Label its vertices by an odd cyclic group Z_(s-1) and infinity. Matching z has edge infinity-z and pairs {z+i,z-i}, 1<=i<=(s-2)/2. Every finite pair has a unique midpoint modulo s-1, so the classes partition all edges. For odd s, factor K_(s+1), then delete its dummy vertex; the s classes are near-perfect matchings, each of size (s-1)/2. The cases s=0,1 have no edges and are handled directly.

Assign distinct matching classes of K_d to distinct vertices of L. Lift each assigned AA edge ab to the triangle xab. Within a class there is no repeated spoke, and classes have disjoint AA edges. Under t>=d-1 this uses exactly binom(d,2)-epsilon(d,t) AA edges.

Separately assign distinct matching classes of K_q to distinct vertices of A. Lift each assigned BB edge bc to triangle abc. Under d>=q-1 this uses exactly binom(q,2)-epsilon(q,d) BB edges. The second family uses only BB and AB edges; the first uses only AA and AL edges. They are therefore edge-disjoint, even though their vertices are shared. Combining them proves the lower integer bound in (2).

## Every unused edge class and its charge

Unused AA edges are precisely one omitted near-perfect matching in the odd boundary case, or none. Their number is epsilon(d,t). Unused BB edges are similarly charged to their own omitted matching, with total epsilon(q,d). Each such resource edge is charged once.

There can be quadratically many unused AL or AB edges. They are NOT silently called a linear leftover. They cannot improve the packing objective without consuming an AA or BB edge, by (3). The entire fractional optimum has already been bounded by that one internal-edge budget, and the integer construction spends all but the two explicitly bounded matching classes. This is why (2) is an additive objective bound despite possibly many leftover spokes.

Repeated equal neighborhoods create distinct outside vertices, to which distinct colors may be assigned; no multiplicity of a maximal-clique representation is paid. If q=0, a leaf has the full core neighborhood and the second family is empty. If d=0, (1) forces q<=1 and the graph is edgeless. If t=0, (1) forces d<=1; the same formulas cover all resulting graphs, with zero-size families omitted. Core vertices and isolates are never removed. The two finite matching-class lists give termination of the construction.

The seven-vertex graph with d=2,q=3,t=2 has nu_star=4 and nu=3, so the nonzero odd-boundary allowance is genuinely needed. Its full maximal cliques, optimal fractional primal/dual and integer partition certificates are in nested/proof.md; it is not a superlinear or root counterexample.

## Scope and continuation

The constructive checker exhausts bounded parameter triples by explicit rational edge loads and disjoint triangle sets. This does not replace the all-order midpoint/coloring proof above. This manuscript is generator-authored, not a trusted verifier receipt. The general chain-of-prefixes linear-gap goal remains open: three or more effective core layers permit transversal core triangles that avoid a proposed union of only within-layer resource edges. A further allocation theorem is required; neither (3) nor the earlier linear-cost normalization establishes it.

Status: NONTERMINAL_CHECKPOINT. No extension to general clique-tree intervals or closure of either admitted obligation is claimed.
