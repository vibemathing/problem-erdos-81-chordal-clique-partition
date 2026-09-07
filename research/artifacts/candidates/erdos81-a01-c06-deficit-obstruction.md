# C06: exact deficit accounting and an asymptotic obstruction to intact-core partitions

Candidate ID: `candidate:erdos81-a01-c06-deficit-obstruction`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `a151526269cc0f2972243ce96e7d413dc0d4f5c8`
Verdict: `candidate_only`.

## 1. Scope, inputs, and conventions

All graphs are finite and simple. A clique partition partitions edges exactly once; different pieces may share vertices. Empty edge sets contribute no pieces. Write cp(G) for the minimum number of pieces, r=omega(G), and
    f_r(n)=(r-1)n-binom(r,2),  delta=f_r(n)-|E(G)|.
The root is the universal n^2/6+O(n) upper bound. The admitted reduction asks for a same-order split dominator. Neither is concluded here.

C01 supplies the written complete-split calculation for J(k,t)=K_k joined to a set of t pairwise nonadjacent vertices: for t>=k, cp(J(k,t))=kt-binom(k,2), and B(n)=floor(n(n+1)/6) is attained by some split graph. We reuse that construction, not a universal split upper bound. C04 supplies the motivation for testing maximum-clique exchange beyond delta=1. Its conclusion is not assumed for delta>=2.

The clique-tree characterization of chordal graphs is the structural input scoped in C01 source S3. All other arguments here are explicit counting, constructions, and elementary inequalities. No mathematical enumerator, solver, or proof assistant was executed. The edge weights below are a written certificate, not an ILP run or verifier receipt. No novelty assertion is made.

## 2. C06.1: an exact clique-tree deficit identity

Choose a clique tree of G, rooted at a maximum clique Q_0 of size r. For disconnected G, take a clique tree of each component and join the trees using empty separators. For every nonroot maximal-clique bag C_i, put
    S_i=C_i intersect parent(C_i),
    a_i=|C_i minus S_i|,  h_i=r-|C_i|.
Distinct maximal bags give a_i>=1 and h_i>=0.

The running-intersection property gives
    n=r+sum_i a_i,
    m=binom(r,2)+sum_i [binom(|C_i|,2)-binom(|S_i|,2)].
To verify this accounting, bags containing a fixed vertex form a connected subtree. Their number minus the number of parent edges with that vertex in the separator is one. The same holds for a graph edge: bags containing both endpoints are a nonempty connected subtree. Summing these identities counts vertices and edges exactly once.

Substitution yields the exact formula
    delta=sum_i [a_i h_i+binom(a_i,2)].                       (1)
Indeed |S_i|=r-h_i-a_i, and the edge contribution of bag i is
    a_i(r-1)-a_i h_i-binom(a_i,2).

Zero cost occurs exactly for (a_i,h_i)=(1,0). Every positive-cost bag costs at least one; hence at most delta bags have positive cost. Their total number of newly introduced vertices is at most 2 delta: for a>=2, binom(a,2)>=a/2, and for a=1 positive cost is at least one. Also h_i<=delta, recovering |C_i|>=r-delta.

This controls deficit contributions, not the number or arrangement of zero-cost bags. An arbitrarily long tree of zero-cost bags is possible.

## 3. C06.2: exhaustive positive-cost types at delta=2 and delta=3

For a>=1 and h>=0, the possible positive costs up to three are:
    cost 1: (a,h)=(1,1) or (2,0);
    cost 2: (a,h)=(1,2);
    cost 3: (a,h)=(1,3), (2,1), or (3,0).

Thus delta=2 consists of one cost-two bag or two cost-one bags, with all other bags of type (1,0). Delta=3 consists of one cost-three bag, one cost-two and one cost-one bag, or three cost-one bags, again with any number of zero-cost bags.

This is a complete classification of the positive summands in (1), not of clique-tree isomorphism types or separator placements. Those placements must still be tracked in partition arguments.

## 4. C06.3: a uniform family obstructing maximum-clique exposure

Fix integers
    d>=2,  k>=d+2,  t>=k.
Take a k-clique K, a set I of t pairwise nonadjacent vertices joined to every vertex of K, and two further vertices u,v. Choose a d-element subset B of K and b in B. Add exactly these edges incident to u or v:
    uv;
    vx for x in K minus {b};
    ux for x in K minus B.
There are no edges from {u,v} to I. Call the resulting graph G(k,t,d).

An explicit perfect elimination ordering is u,v, then all vertices of I, then K. The later neighborhood of u is (K minus B) union {v}, that of v is K minus {b}, and that of each I vertex is K. All are cliques. A graph with such an ordering is chordal: the earliest vertex of an induced cycle of length at least four would have two nonadjacent later neighbors on the cycle. The graph is connected.

Its numerical parameters are
    n=k+t+2,
    m=binom(k,2)+k(t+2)-d,
    r=k+1,
    delta=d.                                                (2)
The maximum cliques are EXACTLY K union {x}, for x in I. A clique containing v but not u has at most k vertices; one containing both u and v has at most k-d+2<=k vertices; an I vertex cannot occur with u or v. These observations prove both the maximum-clique list and r=k+1.

For every maximum clique Q=K union {x}, the graph induced outside Q has exactly one edge, uv. No choice or exchange of maximum clique can expose two outside edges. Nevertheless G is nonsplit: for any x in I, {u,v,b,x} induces 2K2. A split graph cannot contain induced 2K2, since its clique side would have to meet both disjoint edges and hence create another edge.

For reference, a clique tree has root K union {x_0}, all other K union {x} adjacent to it, bag (K minus {b}) union {v} adjacent to the root, and bag (K minus B) union {u,v} adjacent to that bag. The last two bags have (a,h)=(1,1) and (1,d-1). Thus the failure at delta=2 uses two cost-one bags; at delta=3 it uses costs one and two.

This family contradicts the unqualified extrapolation of C04's exposure lemma to delta>=2. It is not a counterexample to the admitted split-domination target.

## 5. C06.4: exact cp, with matching primal and signed dual certificates

For the family in Section 4,
    cp(G(k,t,d))=k(t+2)-binom(k,2)-d-3.                      (3)

Lower certificate. Give weight +1 to edges from K to I union {u,v}, weight -1 to edges inside K, and weight -2 to uv. Every clique has total edge weight at most one. A core-only clique on s vertices has weight -binom(s,2). A clique with one outside vertex and s core vertices has weight s-binom(s,2)<=1. A clique with both u,v and s core vertices has weight
    2s-binom(s,2)-2 = 1-(s-2)(s-3)/2 <= 1
for every integer s>=0. No other pair of outside vertices can belong to a clique. Summing weights over an exact edge partition proves the lower bound (3). Negative edge weights are valid precisely because every edge occurs exactly once.

Upper certificate. Choose distinct p,q in K minus B; k>=d+2 guarantees their existence. Use the four-vertex clique {u,v,p,q}. Decompose E(K_k) into at most k matchings as in C01 and omit edge pq from its matching. Assign the matching classes to distinct vertices of I, possible because t>=k. For each remaining core edge ab in the class assigned to x, use triangle {x,a,b}. Use all remaining edges as K2 pieces.

Within each matching no crossing edge repeats; different classes use distinct I vertices. The four-vertex piece uses core edge pq and crossing edges at u,v, none of which occur in these triangles. The construction therefore is an exact partition. It has one K4 and binom(k,2)-1 triangles. Relative to all singleton edges their savings are five and twice binom(k,2)-1, respectively. Its number of pieces is
    m-5-2[binom(k,2)-1]
      =k(t+2)-binom(k,2)-d-3.
This equals the lower certificate. No search for optimality is needed.

The same-order split graph J(k,t+2) has cp=k(t+2)-binom(k,2), exceeding (3) by exactly d+3. Thus these examples have explicit split dominators.

## 6. C06.5: a quadratic obstruction to retaining an intact maximum-clique piece

Let cp_Q(G) denote the minimum size of an edge partition required to contain Q itself as one piece, where Q is any maximum clique of this family. Then
    cp_Q(G(k,t,d))=k(t+1)-d-1.                              (4)

After Q is used, any other piece has at most one vertex in Q. Outside Q there is only uv. Consequently the only possible remaining pieces larger than K2 are triangles uvz; at most one such triangle can be used. One exists because K minus B is nonempty. The remaining edge count is m-binom(k+1,2), so (4) follows by saving exactly two with that triangle:
    cp_Q=1+[m-binom(k+1,2)]-2.

The result is the same for every maximum clique Q. Combining (3) and (4),
    cp_Q(G)-cp(G)=binom(k,2)-k+2.                           (5)
Thus even an OPTIMAL residual partition after selecting an intact maximum clique can lose quadratically many pieces. Exposing more residual edges is not the essential missing resource.

For fixed d>=2 and every n>=3d+5, set
    k=floor((n+1)/3),  t=n-k-2.
Then k>=d+2 and t>=k. By C01's benchmark calculation,
    cp(G(k,t,d))=B(n)-d-3,
whereas
    cp_Q(G(k,t,d))=(2/9)n^2+O_d(n).
The actual optimum is (1/6)n^2+O_d(n). In particular delta=2 gives B(n)-5 and delta=3 gives B(n)-6 in an infinite nonsplit family.

Therefore a strategy that always includes some whole maximum clique as a partition piece cannot prove the root coefficient 1/6, even when delta is fixed at two. This rules out a strategy, not the root: the explicit partitions in Section 5 use core edges across many mixed pieces instead.

## 7. Verification scope, failed-method proposal, and next obligation

The precise local hypothesis to discard is: every nonsplit chordal graph with r>=5, n-r>=4, and delta=2 admits a maximum clique whose complement contains at least two edges. Parameters d=2, k>=4, t>=k in Section 4 violate it. The broader intact-maximum-clique strategy has the quantitative failure (5). Neither failure retires the admitted existential route, and no canonical failed-route record is written.

Attack pass: d=2 versus d=3; the smallest allowed k=d+2; t=k; all maximum cliques, not just a selected one; the induced 2K2; s=0,1,2,3 in the signed certificate; parity of the matching decomposition reused from C01; repeated vertices versus repeated edges; and the distinction between cp and cp_Q.

Required further checks: formal statement faithfulness, the clique-tree counting identity, the quantified family and maximum-clique list, and the equality of explicit partition count and signed lower bound. No verification receipt is supplied.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: this proof draft together with the stated C01 structural and matching inputs.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.

Next exact task: retain core-edge expenditure as a state variable, derive a general-delta completion/perturbation bound and an exact PEO residual recurrence, and test whether an amortized bound on that recurrence can reach n^2/6+O(n). A proof for the zero-deficit class and a uniform treatment of growing delta are still missing. Increasing the finite excluded order is not the objective.
