# Erdős 81 C02: a maximum-clique outside-edge bound

Candidate ID: `candidate:erdos81-a01-c02-outside-edge`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `38ea689d964191e0ce5d72c40410ec7800770b53`
Verdict: `candidate_only`.
Method: natural-language derivation; no graph enumerator, solver, proof assistant, or mathematical command was run. No novelty claim.

## 1. Frozen target and proof dependencies

For every n-vertex finite simple chordal graph G, does there exist an n-vertex split graph H with cp(H)>=cp(G)? Here cp is a partition of the edge set into complete subgraphs with no edge repeated. The root n^2/6+O(n) bound and the unrestricted target remain open.

Use the perfect elimination ordering (PEO) characterization recorded in C01 source S3, Section 2, only as a structural theorem. The prior candidate `research/artifacts/candidates/erdos81-a01-c01-core-obstructions.md` supplies two reusable proof drafts: domination when omega<=3 and an attained split benchmark B(n)=floor(n(n+1)/6). Those drafts must be audited together with this one; a merged file is not mathematical Evidence.

All statements below use only finite-graph-basic, finite-combinatorics, and real-arithmetic, with the stated PEO theorem.

## 2. C02.1: edge-count envelope and an initial partition bound

For a chordal graph on x vertices with clique number at most r, define
    f_r(x) = sum_(j=0)^(x-1) min(r-1,j).
The PEO later-degree bounds give |E|<=f_r(x). Equivalently, f_r(x)=binom(x,2) for x<=r and f_r(x)=(r-1)x-binom(r,2) for x>=r.

If G has order n and actual clique number r>=2, choose a clique Q of size r. Use Q once and every edge outside E(Q) singly. This is a genuine edge partition regardless of the residual graph's chordality. Consequently
    cp(G) <= |E(G)|-binom(r,2)+1
          <= U(n,r):=(r-1)(n-r)+1.

If equality |E(G)|=f_r(n) holds, every later-degree cap in a PEO is attained. The last r vertices form K_r and, in reverse order, every other vertex is added adjacent to exactly an (r-1)-clique of earlier vertices. Thus G is an (r-1)-tree, in this precise constructive sense. This equality characterization is derived here from the PEO, not inferred by adding edges to G.

## 3. C02.2: the cost of a bridge

If G has a bridge and actual clique number r>=3, then
    |E(G)| <= f_r(n)-(r-2).

Remove the bridge and group the components into A and B so that Q is contained in A, B is nonempty, and the bridge was the only crossing edge. Such a grouping exists also when G was disconnected. Put a=|A|>=r and b=|B|>=1. The induced graphs remain chordal, hence
    |E(G)| <= f_r(a)+f_r(b)+1
             = f_r(n)-((r-1)b-f_r(b))+1.
For b>=1, the expression (r-1)b-f_r(b) is at least r-1: it starts at r-1, increases by r-b while b<r, and is constant at binom(r,2) for b>=r. This proves the estimate.

Using Q and singleton residual edges also gives the useful stronger bridge-specific inequality
    cp(G) <= U(n,r)-(r-2).

## 4. C02.3: the outside-edge improvement for nonsplit graphs

For every nonsplit chordal G of actual clique number r>=4,
    cp(G) <= W(n,r):=(r-1)(n-r)-1 = U(n,r)-2.

If G has a bridge, C02.2 proves this because r-2>=2. Suppose G has no bridge. Every edge then lies on a cycle, and a shortest cycle containing that edge has no chord: a chord would leave a shorter cycle containing the edge. Chordality therefore places every edge in a triangle.

Since G is not split, V(G)\Q is not a set of pairwise nonadjacent vertices. Choose an edge uv outside Q. It belongs to a triangle T. At least two vertices of T are outside Q, so E(T) is disjoint from E(Q). Partition using Q, T, and every remaining edge as a two-vertex clique. Its size is
    |E(G)|-binom(r,2)-1 <= U(n,r)-2.

This proof never assumes an edge-deleted residual is chordal. The two large pieces may share one vertex; that does not violate an edge partition. A nonsplit graph, not just a particular nonsplit partition, is required in the statement.

## 5. C02.4: domination for clique number at most four and all orders at most nine

For graphs already split, take H=G. For omega<=3 use C01. Suppose G is nonsplit and r=4. C02.3 gives cp(G)<=3n-13. For integer n,
    n(n+1)/6 - (3n-12) = (n-8)(n-9)/6 >= 0,
because no integer lies strictly between 8 and 9. Hence B(n)>=3n-12>3n-13. The complete-split witness from C01 dominates G. This proves the target for every chordal graph of clique number at most four.

For n<=9 and r>=5, a maximum clique leaving at most one vertex already makes the graph split. The remaining nonsplit parameter pairs are exhausted by this arithmetic table:

| n | r | W(n,r) | B(n) |
|---|---|---|---|
| 7 | 5 | 7 | 9 |
| 8 | 5 | 11 | 12 |
| 8 | 6 | 9 | 12 |
| 9 | 5 | 15 | 15 |
| 9 | 6 | 14 | 15 |
| 9 | 7 | 11 | 15 |

Thus every chordal graph on at most nine vertices has a same-order split dominator. This is an analytic finite-order proof draft, not a report of exhaustive graph enumeration.

## 6. C02.5: a sharp necessary-parameter filter for further attacks

Any counterexample to the unrestricted target must be nonsplit, have n>=10 and r>=5, and satisfy
    (r-1)(n-r)-1 > floor(n(n+1)/6).
This is necessary, not sufficient. Surviving this inequality does not constitute a counterexample.

At n=10 the only remaining clique numbers are r=5 and r=6; both have W=19 whereas B(10)=18. If an order-ten counterexample exists, its cp must be exactly 19, and the maximum cp over all order-ten split graphs must be exactly 18.

Moreover such a graph has no bridge: the bridge bound is at most 18 for r=5 and at most 17 for r=6. For a bridgeless graph, the actual edge-count version of C02.3 says cp<=m-binom(r,2)-1. Thus cp=19 forces m=30 for r=5 or m=35 for r=6, attaining f_r(10). By C02.1 it is respectively a 4-tree or a 5-tree. A valid target counterexample would still need both a lower certificate cp(G)=19 and an upper certificate for every order-ten split graph; neither is supplied here.

## 7. Attack pass and checkpoint

Checked in the written argument: disconnected graphs in the bridge cut, shortest cycles through a specified edge, overlapping vertices versus overlapping edges, n-r<=1, the integer-floor comparison, and equality versus inequality in the edge-count envelope. The bridge-free case is not extrapolated to graphs with bridges.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: this natural-language draft, subject to C01 dependencies.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
No canonical failed route is added. The local unsafe rules recorded in C01 remain excluded.
Next action: attack the dense 4-tree/5-tree cases using a maximum clique whose complement has multiple edges, and certify the edge-disjoint packing explicitly. The unrestricted split maximum is not assumed to equal B(n).
