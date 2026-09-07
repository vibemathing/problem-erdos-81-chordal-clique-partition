# C20: asymptotic integer rounding and the surviving near-extremal branch

Candidate ID: `candidate:erdos81-a01-c20-asymptotic-rounding`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `e00b467d7678c22cb07c66ad04ff9f1bfe29ada2`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Scope

This candidate combines C18's fractional extremum with a published packing theorem. It gives the WEAKER integer bound n^2/6+o(n^2), not the frozen n^2/6+O(n) root, and not exact same-order integer split domination. It also narrows any asymptotically integer-extremal sequence to C19's low-core branch.

Use C18's lambda, p23, nu, nu_star and B(n)=floor(n(n+1)/6). Their exact identities are
    lambda=m-2*nu_star, p23=m-2*nu, cp<=p23,
and C18's candidate proof gives lambda<=B(n) on chordal graphs. C19 supplies the two compression branches. These dependencies require joint verification.

## 2. C20.1: theorem reuse with its actual quantifiers

The external input is the fixed-triangle specialization of the Haxell-Rodl packing theorem, also proved by Yuster:
    for every epsilon>0 there is N(epsilon) such that
    nu_star(G)-nu(G)<epsilon*n^2 for every n>N(epsilon)
    and every n-vertex finite simple graph G.            (1)
Yuster's author-deposited version math/0305350v4, Theorems 1.1/1.2 and the opening of Section 3, provides this form; source details and limitations are in the accompanying note. Here triangles are edge-disjoint, and n is the number of ORIGINAL GRAPH VERTICES, not the number of edges in an auxiliary hypergraph. No minimum-degree or positive-density hypothesis is added.

The paper's initial convention excludes isolated vertices. Here is an explicit bridge. If G has a nonisolated vertex, pair up its isolated vertices and join each pair; if one remains, attach it by one pendant edge to a nonisolated vertex. These additions introduce no triangles and remove all isolates. If G is edgeless and n>=2, replace it for this purpose by any n-vertex tree. Both graphs then have zero triangle packing parameters. Thus (1) applies to all simple G with n>=2 without changing nu or nu_star. No chordality is required for this external bridge.

Define
    a(n)=max_(|V(G)|=n) (nu_star(G)-nu(G)).
The maximum exists over finitely many graph types and finite LP optima. Equation (1) says a(n)/n^2 tends to zero. It does not assert a(n)=O(n), or provide a usable numerical cutoff in this candidate.

## 3. C20.2: sharp leading coefficient for integer partitions

For every chordal G on n vertices, the exact C18 identities give
    cp(G)<=p23(G)
         =lambda(G)+2*(nu_star(G)-nu(G))
         <=B(n)+2*a(n).                                 (2)
Hence uniformly over chordal graphs
    cp(G)<=n^2/6+o(n^2).                                (3)
Explicitly: for every eta>0, for all sufficiently large n, every chordal G of order n has cp(G)<=(1/6+eta)*n^2. The n/6 term from B(n)<=n^2/6+n/6 is absorbed only after fixing eta and enlarging its cutoff.

Let F_ch(n) and F_sp(n) be the maxima of integer cp over chordal and split graphs of order n. C01's attained benchmark and the inclusion of split graphs in chordal graphs give
    B(n)<=F_sp(n)<=F_ch(n)<=B(n)+2*a(n).                 (4)
Both maxima divided by n^2 therefore tend to 1/6. Equivalently, C01's same-order complete split witness H_n obeys cp(G)<=cp(H_n)+o(n^2) uniformly for chordal G. This is approximate domination only. Equation (4) does not prove F_ch(n)=F_sp(n) at any unhandled order.

One cannot set eta=1/n in a theorem whose cutoff N depends on eta. A remainder such as n^(3/2) tends to zero after division by n^2 but not after division by n; this elementary example is a logical distinction, not a claimed graph witness. Neither the source's general tightness discussion nor (3) is a counterexample to the root.

## 4. C20.3: integer near-extremizers cannot use the dense compression branch

Let G_j be chordal, n_j tend to infinity, and suppose
    cp(G_j)/n_j^2 >= 1/6-o(1).
Equation (2), together with a(n)=o(n^2), implies
    lambda(G_j)=n_j^2/6+o(n_j^2),
    s_j:=B(n_j)-lambda(G_j)=o(n_j^2).                    (5)
Choose an optimal dual and maximum weighted-neighborhood pair as in C18. Write its clique size as r_j and t_j=n_j-r_j.

Suppose t_j<r_j-1 for an infinite subsequence. C19's dense-branch estimate gives
    s_j>=B(n_j)-n_j(n_j-1)/6+t_j(t_j-1)/6.
The first difference is at least (n_j-1)/3. Consequently (5) forces t_j=o(n_j) on that subsequence. The actual clique of size r_j=n_j-t_j can be used as ONE integer piece, after which using all other edges singly gives
    cp(G_j)<=r_j*t_j+binom(t_j,2)+1=o(n_j^2).
This contradicts the starting lower bound. Thus every such sequence eventually uses only the low-core branch t_j>=r_j-1, for any chosen optimal compression pair.

In that branch C19's square-completion identity and (5) give
    r_j=n_j/3+o(n_j), theta_j=t_j-r_j+1=n_j/3+o(n_j),
    P_j=o(n_j), R_j+D_j=o(n_j^2).                        (6)
This is a quantitative statement about the selected dual and its PEO. It is NOT a proved edit-distance stability theorem for the graphs.

In particular any sequence witnessing a superlinear excess over n^2/6, if one exists, must survive (5)-(6); almost-complete-core fractional examples such as K_n cannot serve as such integer witnesses.

## 5. C20.4: a linear rounding calibration on chordal clique sums

For k>=1 take k copies of K4, identifying exactly one vertex from each into a common vertex c, with no other identifications or edges. Call the graph W_k. It is chordal: deleting c leaves separate triangles and an induced cycle cannot pass through different blocks without revisiting c. Its order and edge count are
    n=3k+1, m=6k.

Every triangle lies in a single block. A K4 contains at most one edge-disjoint triangle, whereas weights 1/2 on its four triangles are a fractional packing of size two; total edge capacity gives the matching upper bound 6/3=2. Hence
    nu(W_k)=k, nu_star(W_k)=2k,
    lambda(W_k)=2k, p23(W_k)=4k, cp(W_k)=k.               (7)
The cp statement follows by using each K4 once; no clique with an edge can span distinct blocks.

Therefore
    nu_star-nu=(n-1)/3, p23-lambda=2(n-1)/3.              (8)
Any universal additive triangle-packing gap bound C*n on chordal graphs must have C>=1/3 asymptotically. This is a lower calibration, not a matching upper theorem. Larger cliques can outperform the edge-and-triangle rounding route, as cp(W_k)=k shows.

The root-relevant quantity from C18 is 2*(nu_star-nu)-s, not the gap in isolation. For W_k, s=B(3k+1)-2k is quadratic while the gap is linear, so this family does not threaten the root.

## 6. Verification boundary and continuation

This is a natural-language reuse/derivation candidate. No packing algorithm, random process, LP solver, enumerator, proof assistant, or mathematical command was run. The external theorem is cited as an input, not re-proved or kernel-verified here. The paper's eight-page text was available; the reused statement and quantifier paragraph were read, while screenshot calls failed. No visual check or whole-proof audit is claimed.

Audited: isolated-vertex convention, original graph versus hypergraph order, fixed pattern versus growing family, exact packing-to-partition factor two, uniform versus pointwise little-o, the floor/linear term, the dense-subsequence contradiction, and block additivity in W_k.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: integer n^2/6+o(n^2) corollary and the necessary low-core structure of integer near-extremizers, subject to the stated dependencies.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
failed_routes: canonical ledger unchanged. An n-dependent epsilon substitution and use of auxiliary-hypergraph order are excluded shortcuts, not failures of the admitted route.

Next action: attack additive rounding in the low-core branch, keeping the full slack s rather than demanding an unnecessary exact fractional-to-integer transfer. Test leaf-bag rounding rules against arbitrary fractional separator capacities before using them inductively; local rounding with a fixed separator can be much worse than constant per eliminated vertex.
