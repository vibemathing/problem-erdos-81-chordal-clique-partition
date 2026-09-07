# C18: signed-weight compression and the fractional chordal extremum

Candidate ID: `candidate:erdos81-a01-c18-fractional-compression`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `835590bb3ce8016b41e6b96b7d57f39b5083d754`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Frozen target and explicit relaxation

The admitted target concerns INTEGER edge-disjoint clique partitions. This candidate studies a different, weaker parameter on the same finite simple graphs. It proves the split-domination analogue for that relaxation, not for cp. Neither the target nor the root is closed.

Let lambda(G) be the minimum of sum_C x_C over all edges and triangles C of G, subject to x_C>=0 and sum_(C containing e) x_C=1 for EVERY edge e. Let cp_f(G) allow all complete subgraphs with at least one edge instead. Let p23(G) be the INTEGER edge-and-triangle partition minimum. Thus
    cp_f(G)<=lambda(G)<=p23(G),  cp(G)<=p23(G),
    cp_f(G)<=cp(G).
No comparison cp(G)<=lambda(G) is asserted.

Write B(n)=floor(n(n+1)/6). The main candidate is
    max_(G chordal, |V(G)|=n) lambda(G)
      =max_(G chordal, |V(G)|=n) cp_f(G)=B(n),             (1)
for n>=1. The maxima are attained by complete split graphs. This is a fractional extremum only.

Inputs: the C01 split benchmark, the C04 clique-suffix PEO argument, and finite linear-program duality in the exact form scoped in the accompanying source note. There is no mathematical program, LP execution, numerical optimization, proof assistant, or verifier receipt. The finite LP theorem is a declared mathematical dependency requiring its usual proof, not a newly admitted axiom.

## 2. LP form and dual attainment

Let A have rows indexed by edges and columns indexed by the permitted pieces, with A_(e,C)=1 when e is in C and zero otherwise. The primal is min 1^T x subject to Ax=1 and x>=0. It is feasible using all edges singly. Every variable is at most one, since its piece has an edge whose equality has nonnegative summands. Thus the feasible region is bounded and closed and the minimum is finite and attained.

Finite LP duality gives an attained dual optimum
    lambda(G)=max sum_e w_e
subject to REAL SIGNED weights satisfying
    w_e<=1 for every edge,
    sum_(e in T) w_e<=1 for every triangle T.             (2)
The dual is feasible at zero. Equality constraints, not covering inequalities, are why the weights have no nonnegativity restriction. With all cliques permitted the analogous dual has one inequality for every clique.

Weak duality here is immediate: for a feasible x,w, sum_e w_e=sum_C x_C sum_(e in C)w_e<=sum_C x_C. This identity uses equality on each edge. The conversion from bounding all such w to the primal optimum uses strong duality, whose finite, feasible, bounded hypotheses were just checked. The edgeless graph is handled separately with value zero.

## 3. A PEO may end in any specified clique

C04 Section 2 proves that a PEO of a chordal graph can end at any specified MAXIMAL clique C. Briefly, root a clique tree at C. A leaf bag other than C has a vertex occurring in no other maximal bag; it is simplicial and outside C. Delete it and repeat. Other components can be exhausted in the same way, including complete components. This preserves C until it is the remaining graph.

For an arbitrary nonempty clique S, extend S to a maximal clique C, choose that PEO, and order the final clique C with C minus S first and S last. Any order within a clique is a PEO. Consequently S itself is the exact suffix. No arbitrary swap of a PEO vertex into its tail is being assumed.

## 4. C18.1: maximum weighted-neighborhood compression

Take any feasible weights w from (2). Define
    M=max_(u,S) sum_(s in S) w_(us),                      (3)
where u is a vertex and S is any clique contained in N_G(u), including the empty clique. The maximum is over finitely many pairs.

If M=0, each individual edge weight is nonpositive by choosing S a singleton, so sum_e w_e<=0 and the desired upper bound is trivial. Suppose M>0 and fix an attaining pair u,S. Set r=|S|>=1 and t=n-r>=1. Choose a PEO ending at S. For every vertex v outside S let c_v be the sum of weights on edges from v to its later neighbors. That neighbor set is a clique in N_G(v), so c_v<=M by (3), even for signed weights. Counting every edge at its earlier endpoint gives
    W:=sum_e w_e
       =w(E(S))+sum_(v outside S)c_v
       <=w(E(S))+tM.                                   (4)

On H=J(r,t), the join of the core clique S and t pairwise nonadjacent new vertices, keep the original weights within S. Give every new vertex x the crossing weights w'_(xs)=w_(us). Any edge or triangle in H maps to an edge or triangle in the original clique S union {u}; core triangles are unchanged. Hence w' satisfies (2) on H. Its total weight is exactly the right side of (4). Weak duality on H yields
    W<=lambda(J(r,t)).                                  (5)

Apply this to an optimal w for G. Nonempty G has lambda(G)>=|E(G)|/3>0, so M>0. Thus every nonempty chordal G has a same-order complete split H with lambda(H)>=lambda(G). The selected S is defined by WEIGHT, not by the maximum unweighted clique size. No modification of G or preservation of its cp has been claimed.

The same copying argument works with every clique inequality imposed, and gives cp_f(G)<=cp_f(H) for a possibly different weight-selected H. Alternatively, the universal upper bound for cp_f follows from cp_f<=lambda below.

## 5. C18.2: exact complete-split fractional values for lambda

For integers r,t>=1,
    lambda(J(r,t)) =
      rt-binom(r,2),                 if t>=r-1;
      [rt+binom(r,2)]/3,             if 1<=t<r-1.         (6)

For the first case, give every mixed triangle xab weight 1/t. Every core edge belongs to t such triangles and is covered once. Every crossing edge belongs to r-1 of them. Give that edge additional singleton weight 1-(r-1)/t, which is nonnegative. Use no other pieces. The objective is rt-binom(r,2). Conversely assign crossing edges weight +1 and core edges weight -1. Every edge weight is at most one; a mixed triangle has total one and a core triangle has total -3. This feasible dual matches the objective. For r=1 there are no triangles and the formula just counts the t edges.

For the second case r>=3. Give every mixed triangle weight 1/(r-1), so every crossing edge is covered once and every core edge gets weight t/(r-1). Add each core triangle with weight
    [1-t/(r-1)]/(r-2).
This is nonnegative and covers the remaining weight of every core edge. Only triangles are used, so the objective is the edge count divided by three. The all-edge dual weights 1/3 match this value. The boundary t=r-1 agrees in the two formulas.

These are finite rational certificates, not solver outputs. Formula (6) is for lambda; it is not asserted as the all-clique fractional or integer optimum when t<r-1.

## 6. C18.3: optimization and attained bound B(n)

In the first branch of (6), with t=n-r, put
    g_n(r)=rn-3r^2/2+r/2.
Completing the square gives
    g_n(r)<= (n+1/2)^2/6 = n(n+1)/6+1/24.                (7)
The value g_n(r) is an integer. The fractional part of n(n+1)/6 is either zero or 1/3, as checking n modulo three shows. Therefore (7) implies g_n(r)<=B(n).

In the second branch lambda(J(r,t)) is at most binom(n,2)/3=n(n-1)/6<=B(n) for n>=2. Indeed, the difference between n(n+1)/6 and n(n-1)/6 is n/3, at least 2/3, while taking the floor loses at most 1/3. The n=1 edgeless case is direct. Combining (5)-(7) and dual attainment proves lambda(G)<=B(n) for every chordal G.

For n>=2 take r=floor((n+1)/3), t=n-r. Then t>=r and C01 gives g_n(r)=B(n), by its three residue-class formulas. The preceding signed dual remains feasible for ALL clique inequalities: a clique with one outside vertex and s core vertices has weight s-binom(s,2)<=1; a core-only clique has nonpositive weight. The integer partition from C01 has B(n) pieces. Thus
    cp_f(J(r,t))=lambda(J(r,t))=cp(J(r,t))=B(n).
The isolated vertex handles n=1. This establishes (1) as a candidate proof.

## 7. C18.4: explicit integrality attacks

K4 has lambda=2: assign weight 1/2 to each of its four triangles. Each edge is covered once and the objective is two. The all-edge dual weights 1/3 match. Its integer edge-and-triangle optimum is four, because any two triangles in K4 share an edge, so at most one triangle can be used. Its full cp is one. Disjoint copies show that lambda=p23 is not valid even on chordal graphs and that an additive loss can accumulate.

There is also a gap for the ALL-clique parameter on a split graph. For J(3,2), the six mixed triangles with weight 1/2 give cp_f<=3; crossing +1/core -1 gives cp_f>=3. But cp=4. A K4 containing the core and one outside vertex plus three singleton edges at the other outside vertex gives four. If a partition uses a K4, those three remaining edges require three more pieces. If it uses no K4, a three-piece partition of the nine edges would need three triangles. Without the core triangle, each outside vertex can occur in at most one mixed triangle, since two would repeat one of its three crossing edges. With the core triangle, no mixed triangle can coexist. Three triangles are therefore impossible.

Neither example is a counterexample to the admitted target or root; both are guards against transferring fractional conclusions to cp.

## 8. The exact remaining rounding quantity

Let nu(G) be the maximum number of edge-disjoint triangles and nu_star(G) its fractional packing optimum, with nonnegative triangle weights and capacity at most one on every edge. From the edge equalities in Section 2, eliminate each singleton variable to obtain the exact identities
    lambda(G)=m-2*nu_star(G),
    p23(G)=m-2*nu(G).                                   (8)
Conversely every fractional packing extends to a fractional partition by adding the unused edge weights singly, proving the first identity in both directions. The integer identity follows by the same count.

For chordal G put s(G)=B(n)-lambda(G)>=0. Then
    p23(G)=B(n)+2*(nu_star(G)-nu(G))-s(G).                 (9)
An estimate 2*(nu_star-nu)-s<=C*n would imply the ROOT upper bound, via cp<=p23 and B(n)<=n^2/6+n/6. The stronger uniform bound nu_star-nu<=C*n would also suffice. Neither estimate is proved here. The root could be true even if a particular stronger rounding claim fails.

An O(n) conclusion would not by itself supply the exact same-order integer split domination target. An o(n^2) rounding conclusion would not supply the root's O(n) remainder. C07 shows that spent-edge residuals can be arbitrary even when the original graph is chordal, so chordal induction cannot simply be applied to those residuals.

## 9. Audit and continuation

Audited: signed versus nonnegative dual variables; existence and attainment of finite optima; the empty graph; empty S in (3); an arbitrary rather than maximal suffix; disconnected graphs; r=1; t=r-1; nonnegative rational coefficients in (6); integer floors; all-clique dual feasibility at the benchmark; and both integrality counterexamples.

Source locators and statement comparisons are in `research/artifacts/source-notes/erdos81-a01-c18-lp-faithfulness.md`. All derived graph statements are candidate-only; no current-best or novelty claim follows from the literature searches.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: the fractional compression and exact extremum (1), with the explicitly unproved rounding estimate (9).
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
failed_routes: canonical ledger unchanged; exact rounding and residual-chordality shortcuts are excluded, not the admitted route.

Next action: examine equality and near-equality in (4)-(7). Preserve each dual slack separately and test whether a near-extremal dual forces a structure whose integer rounding loss can be paid by s(G) plus a linear term. Exact equality classification is a bounded next candidate, not an assumption of this proof.
