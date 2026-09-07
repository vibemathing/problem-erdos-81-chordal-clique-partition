# C10: a valid universal-core reduction and a quadratic-loss completion obstruction

Candidate ID: `candidate:erdos81-a01-c10-universal-core`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `20c46a1fafeca87341e771708ec4bcf960a94340`
Verdict: `candidate_only`.

## 1. Scope

This cycle proves a general-deficit structural bound and distinguishes deleting a genuine universal core from creating one by completing a vertex set. The latter operation can lose a quadratic amount of cp even when its retained set is a maximum independent set and no choice among such sets helps.

All graphs are finite and simple. cp partitions edges exactly once into nonempty cliques. The same-order existential split domination and the root remain open. Dependencies are C04's PEO with an arbitrary maximum clique last, C01's exact complete-split calculation, and the directly proved signed-weight identity in C09. No mathematical program, graph enumeration, solver, or proof assistant was executed. No novelty claim is made.

## 2. C10.1: a deficit bound on universal vertices

Let G be chordal, of order n and clique number r>=2. Set
    delta=(r-1)n-binom(r,2)-m.
Then G has at least
    max(0,2r-n-delta)                                     (1)
universal vertices, meaning vertices adjacent to every other vertex.

Choose a maximum clique Q and a PEO ending in Q. Build the original induced graph in reverse PEO order, starting with Q. Track U, the subset of Q adjacent to all vertices introduced so far; initially U=Q. At a new vertex v, let S be its neighbors already present. By the PEO, S is a clique of size d_v<=r-1. Put epsilon_v=(r-1)-d_v.

Every vertex in U is adjacent to all vertices already present. Hence S union U is a clique in the original graph, and
    |U-S|+d_v<=r.
Exactly the vertices U-S cease to be tracked universal vertices when v is added. At most 1+epsilon_v are lost. There are n-r introduced vertices outside Q, and
    sum_(v outside Q) epsilon_v=delta.
Thus at least r-(n-r)-delta vertices of Q survive and are universal in the full graph. This proves (1). The proof does not complete G or assume anything about an edge-deleted residual. It also works when G is disconnected: in that case a positive bound would itself force a contradiction, so the numeric lower bound must be zero.

Every universal vertex lies in every maximum clique, since otherwise it would enlarge that clique. Therefore the tracked final U is exactly the set of all universal vertices, not merely an unlabelled clique of the same size.

## 3. C10.2: deleting the universal core preserves deficit

Suppose G is not complete. Let U be its set of all universal vertices, u=|U|, and H=G-U. Then H has n'=n-u>=2 vertices, clique number r'=r-u>=1, is chordal, and has no universal vertex. Moreover
    G=K_u joined to H,
    delta(H)=delta(G),                                    (2)
using f_r(n)=(r-1)n-binom(r,2) also for r=1.

Indeed all U vertices can be appended to any clique of H, so its clique number is exactly r-u. The removed edges number
    u(n-u)+binom(u,2)=un-u(u+1)/2.
Directly,
    f_(r-u)(n-u)=f_r(n)-un+u(u+1)/2,
so subtracting the new edge count proves (2). If a vertex of H were universal in H, it would also be adjacent to all of U and hence universal in G, contrary to the choice of U.

For r'>=2, apply (1) to H to obtain
    2r'<=n'+delta.                                        (3)
If r'=1, H is edgeless on at least two vertices and (3) still holds. Thus at zero deficit the graph left after removing all universal vertices has clique number at most half its order. For general delta its excess above half its order is at most delta/2.

Complete G is a separate trivial case with cp(G)=1 when n>=2 (and cp=0 for n<=1). Formula (2) is not applied with a spurious clique number for the empty residual.

This is an exact structural reduction, but NOT a cp monotonicity theorem. One still needs to allocate the U-internal and U-H edges and account for the residual cp(H). C08 and C09 supply several restricted join constructions, not a proof for arbitrary H.

## 4. C10.3: sharpness at zero deficit

For 2<=r<=n, let G=P_n^(r-1), with vertices 1,...,n and edges ij when 0<|i-j|<=r-1. The increasing order is a PEO; maximal cliques are consecutive windows of r vertices. Its edge count is f_r(n), so delta=0.

Vertex i is universal exactly when
    n-r+1<=i<=r.
The number of universal vertices is therefore max(0,2r-n), attaining (1). This shows that the coefficient and additive terms in (1) cannot be strengthened uniformly at delta=0. It is not a root counterexample.

## 5. C10.4: maximum-independent-set completion can lose Theta(n^2)

For each integer q>=1, define G_q as a clique blow-up of P5. It has five disjoint sets A_1,...,A_5, each of size q. Each A_i is a clique; consecutive sets A_i,A_(i+1) are completely joined; there are no other edges.

The order is n=5q, the clique number is 2q, and a PEO is obtained by listing A_1, then A_2, and so on. A current vertex in A_i has later neighbors only in the remaining A_i and all of A_(i+1), a clique. Thus G_q is chordal. One vertex from each of A_1,A_2,A_4,A_5 induces 2K2, so G_q is not split.

Every independent set contains at most one vertex from each A_i and its chosen indices are pairwise nonconsecutive in P5. The maximum size is three, and the only three-index choice is {1,3,5}. Consequently EVERY maximum independent set I consists of one vertex from each odd-index set. All such choices are equivalent by permutations within the A_i.

Let H_q be formed by adding all missing edges on V(G_q)-I and retaining all other adjacencies. It is a same-order split graph with clique side V-I and independent side I. The three I vertices have respectively 2q-1, 3q-1, 2q-1 neighbors outside I. Using the clique side once and each crossing edge singly gives
    cp(H_q)<=7q-2.                                       (4)

For a lower bound on G_q, give all edges between consecutive sets weight +1, edges inside odd-index sets weight -1, and edges inside even-index sets weight -2. A clique meets at most two consecutive sets. If it contains u vertices in an odd set and v in the neighboring even set, its weight is
    uv-binom(u,2)-2binom(v,2)<=1,
by the exact integer identity in C09. Cliques wholly inside a single set have nonpositive weight. Summing over an edge partition therefore gives
    cp(G_q)>=4q^2-7binom(q,2)=(q^2+7q)/2.                (5)

Combining (4)-(5),
    cp(G_q)-cp(H_q)>=(q^2-7q+4)/2
                    =n^2/50-7n/10+2.                   (6)
For q>=7 this is positive, and it grows quadratically along all q. Therefore no universal linear bound can control the cp loss of this completion rule, even after optimizing over all maximum independent sets. Merely changing the rule from exact monotonicity to an O(n)-loss assertion does not repair it.

This is an obstruction to that transformation, not a counterexample to existence of some other split dominator or to the root.

## 6. C10.5: an explicit root-compatible upper certificate for the same family

To avoid mistaking (5) for excessive root growth, the following is a genuine partition of G_q. Use A_1 union A_2 once and A_3 union A_4 once; these two cliques are vertex-disjoint. Use the q^2 edges between A_2 and A_3 singly. The only edges left are all A_4-A_5 edges and the edges inside A_5. This residual is J(q,q) on A_4 union A_5, with clique side A_5 and pairwise nonadjacent side A_4 in the residual.

C01's matching construction gives cp(J(q,q))=q^2-binom(q,2), also for q=1. These pieces do not repeat any already used edge. Hence
    cp(G_q)<=2+q^2+q^2-binom(q,2)
            =(3q^2+q)/2+2
            =(3/50)n^2+n/10+2.                          (7)
In fact (7)<=n^2/6 for q>=1: the difference is (8/3)q^2-q/2-2, positive at q=1 and increasing thereafter. Thus the family itself satisfies the root bound comfortably; (6) measures only loss caused by the proposed completion.

Its deficit is delta=3q(q-1)/2. No inference of small deficit is made for this blow-up family.

## 7. Checkpoint and next exact obligation

Audited: empty S in the universal tracking proof; missing tracked vertices versus all missing Q vertices; universal vertices necessarily belonging to a maximum clique; the noncomplete residual having at least two vertices; r'=1; path powers when the universal interval is empty; all maximum independent sets of P5; q=1 and q=7; and the distinction between original and residual adjacency inside A_4.

The auxiliary failed-method proposal is the O(n)-loss maximum-independent-set completion assertion. The admitted route is still open. The exact universal-core deletion statement is retained as a valid replacement structural reduction, with its cp cost explicitly unresolved.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: (1)-(3), the exact transformation-loss certificates (4)-(7), and their dependencies.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
route_status: open.
No mathematical execution, exhaustive enumeration, or verifier receipt is reported.

Next exact obligation: for K_s joined to an arbitrary chordal H on t vertices, control the incremental partition cost without paying for H's edges twice. Investigate triangle decompositions of K_(s+t)-K_t when s>=t, keeping the congruence repairs O(n), and a separator-specific potential when s<t. The size of a true universal core is quantified above; it is never created by the disproved completion rule.
