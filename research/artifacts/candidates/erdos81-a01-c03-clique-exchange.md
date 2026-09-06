# Erdős 81 C03: maximum-clique exchange and two outside pieces

Candidate ID: `candidate:erdos81-a01-c03-clique-exchange`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `f27c03b536f3d41aff3c82b93822b4b187c51a39`
Verdict: `candidate_only`.
Method: natural-language proof draft. No mathematical command, exhaustive enumeration, solver, or proof assistant was run. No novelty assertion.

## 1. Frozen scope and dependencies

The target is the existential same-order split domination of every finite simple chordal graph, with cp the minimum size of an exact edge partition into complete subgraphs. This candidate establishes only restricted cases; the target and root remain open.

C01 (`research/artifacts/candidates/erdos81-a01-c01-core-obstructions.md`) supplies the attained split benchmark B(n)=floor(n(n+1)/6). C02 (`research/artifacts/candidates/erdos81-a01-c02-outside-edge.md`) supplies the PEO edge envelope
    f_r(n)=(r-1)n-binom(r,2),
    U(n,r)=(r-1)(n-r)+1,
the bridge bound cp<=U-(r-2), and the bridgeless nonsplit bound
    cp<=m-binom(r,2)-1.
Here r is the actual clique number, n>=r, m=|E(G)|, and delta=f_r(n)-m>=0.

Those are candidate dependencies to be audited, not mathematical conclusions inferred from their merges. The only external structural theorem is the chordal PEO characterization scoped in C01 source S3. Allowed axioms remain finite-graph-basic, finite-combinatorics, and real-arithmetic.

## 2. C03.1: two outside edges provide a saving of at least four

Let Q be an r-clique in a graph G, and suppose every maximal clique of G has at least four vertices. If the subgraph on R=V(G) minus Q has at least two edges, there is an edge partition using at most
    m-binom(r,2)+1-4
cliques.

If some clique has at least three vertices in R, extend it to a maximal clique and choose a four-vertex subclique with at least three in R. This is possible because the maximal clique has size at least four: take four R vertices when available, or three R vertices and a fourth vertex otherwise. Its edges are disjoint from E(Q), and using it saves five compared with singleton edges.

Otherwise every clique has at most two R vertices. For each edge of R, a containing clique of size at least four supplies at least two common neighbors in Q. Choose two distinct R edges and distinct Q vertices, one common neighbor for each edge. The resulting triangles share no edge: their R edges differ, and their Q vertices differ, even if the two R edges share an endpoint. Their edges are also disjoint from E(Q). Use Q, the two triangles, and the remaining edges singly, saving four.

## 3. C03.2: a dense nonsplit chordal graph has a suitable maximum clique

Suppose G is chordal, nonsplit, r>=5, and m=f_r(n). Then some maximum clique Q has at least two edges outside it.

C02's equality characterization expresses G as an (r-1)-tree: start with K_r and repeatedly add a vertex adjacent to an (r-1)-clique. It follows by induction that every edge is contained in an r-clique, every maximal clique has size r, and every vertex has degree at least r-1.

Take any maximum clique Q. Since G is nonsplit, its complement R contains an edge. If it has two, we are done. Otherwise R consists of one edge uv and s-2 vertices with no neighbors in R, where s=n-r>=2. Put A=N(u) intersect Q and D=N(v) intersect Q. Chordality forces A and D to be comparable by inclusion: vertices a in A minus D and b in D minus A would induce the four-cycle a-u-v-b-a. Relabel u,v so A is contained in D.

Since uv belongs to an r-clique and no other R vertex is adjacent to u or v, |A|=r-2. Also |D|<=r-1, and each of the other R vertices has at most r-1 neighbors in Q. Counting all edges and using m=f_r(n) forces |D|=r-1 and gives every other R vertex exactly r-1 neighbors in Q.

Write Q=A union {a,b} and D=A union {a}. The clique Q'=A union {u,v} has size r. Outside Q' there is edge ab. Every one of the old s-2 R isolates is adjacent to at least one of a,b, because it misses only one vertex of Q. Thus Q' has at least s-1 outside edges, and this is at least two if s>=3.

If s=2, the original graph is itself split: A union {a,v} is a clique and its complement {b,u} has no edge. This contradicts the assumption. Hence the case s=2 cannot obstruct the claim.

Together with C03.1 this yields, for these full-edge-count nonsplit graphs,
    cp(G)<=U(n,r)-4.

## 4. C03.3: the uniform nonsplit bound for r>=5

Every nonsplit chordal graph of actual clique number r>=5 satisfies
    cp(G)<=(r-1)(n-r)-2 = U(n,r)-3.

If G has a bridge, C02 gives cp<=U-(r-2)<=U-3. If G has no bridge and delta>=1, C02's actual-edge-count partition gives cp<=U-delta-2<=U-3. If delta=0, apply C03.2 and C03.1 to obtain the stronger U-4 bound. These cases are exhaustive.

## 5. C03.4: domination for omega<=5 and all orders through ten

Already split graphs satisfy the target by H=G. For omega<=4 use C02. For nonsplit r=5, C03.3 gives cp<=4n-22. For every integer n,
    n(n+1)/6-(4n-22)=(n-11)(n-12)/6>=0.
Since 4n-22 is an integer, B(n)>=4n-22. C01's same-order complete-split witness therefore dominates G. This covers every chordal graph with clique number at most five.

All orders through nine were handled in C02. For n=10 and nonsplit r>=6, the possible remaining values r=6,7,8 give C03.3 bounds 18,16,12 respectively, all at most B(10)=18. Values r>=9 leave at most one vertex outside a maximum clique and are split. Thus the target holds for all chordal graphs on at most ten vertices.

This proves a domination statement, not the assertion that every split graph has cp<=B(n). The latter is not supplied by any of these candidates.

## 6. C03.5: the remaining order-eleven filter

Any target counterexample must have n>=11, r>=6, and
    (r-1)(n-r)-2>B(n).
At n=11, only r=6 survives: the bound is 23 while B(11)=22. A counterexample at that order would need cp=23 and would force the maximum cp over all order-eleven split graphs to be 22.

Here U(11,6)=26 and f_6(11)=40. A bridge gives cp<=22. The full-edge-count case gives cp<=U-4=22. For a bridgeless graph with delta>=2, C02 gives cp<=U-delta-2<=22. Consequently the only parameter case left at n=11 is
    r=6, m=39, delta=1, no bridge, cp=23.
These are necessary conditions only; no graph with these properties and no split-class upper certificate is constructed.

## 7. Audit and checkpoint

The proof explicitly checks: the maximal-clique hypothesis (not merely an edge-extension hypothesis) and the four-vertex clique when it meets R in exactly three vertices; two triangles sharing a vertex but not an edge; the comparable-neighborhood four-cycle; the s=2 split exception; bridge versus positive-deficit versus zero-deficit cases; and integer-floor inequalities. No assertion depends on an edge-deleted residual remaining chordal.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: this draft with its C01/C02 dependencies.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
Canonical failed routes are unchanged.
Next action: quantify how delta bounds the smallest maximal-clique size, then attack the single-deficit order-eleven case. Separately preserve the newly found local edge-migration and PEO color-folding obstruction witnesses; neither is a counterexample to the admitted target.
