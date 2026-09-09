# C31: p=2, q=2 shared-boundary continuation

Candidate: `candidate:erdos81-a01-c31-two-short-shared-boundary`
Repository: `vibemathing/problem-erdos-81-chordal-clique-partition`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Transport obligation: `obligation:erdos81-split-extremal-reduction`
Verdict: `candidate_only`. `best_verified_result=none`.

## 1. Frozen scope

The core is `K_r`, where `r=3^k`, `k>=2`. An actual short set `A` has size `a`, with `3<=a<=r`. There are exactly two independent short leaves adjacent to A and exactly two independent long leaves adjacent to the whole core. Thus the host has `r+4` vertices.

`L=nu_star` is the fractional edge-disjoint triangle packing optimum. In the aggregated joint model, `z_T` are core-triangle variables, `alpha_e` is total use of `AA` core edge `e` by the two short leaves, and `beta_e` is total use of any core edge by the two long leaves. The constraints are

    alpha_e + beta_e + sum_(T contains e) z_T <= 1,
    deg_alpha(v) <= 2 for v in A,
    deg_beta(v) <= 2 for every core vertex.

`Q` additionally requires every core `z_T` integral but still permits fractional/aggregated leaf allocation. It is NOT an actual host triangle packing and is not `L_D` or `J_fix`.

This candidate proves a uniform O(r) actual-packing correction for this fixed two-short/two-long atom and records the exact one-time conversion invariant. It does not prove the growing-budget one-third face, the general two-level theorem, split domination, or the ProblemContract root.

## 2. One-third face membership

Every joint column uses exactly three capacity rows, so the all-one-third dual is feasible with value

    U = [ C(r,2) + 2a + 2r ] / 3.

We need primal equality, not mere dual feasibility.

For `c=r-a>=3`, C28's exact interval criterion applies with `p=q=2`, `d=r-3`, `s=r-5`:

    ell = max(0, a(c-2)/2, c(a-2)/2),
    u   = min(ac/2, as/2, cd/2, (as+cd)/6).

If `c>=a`, choose the first nonzero lower term. The inequalities `ell<=ac/2`, `ell<=as/2`, and `ell<=cd/2` reduce respectively to `c-2<=c`, `a>=3`, and `c(c-3)+2a>=0`. The last inequality is

    a^2-ac+c^2+a-3c >= 0,

which after `c=a+x` is `a^2+ax+x^2-2a-3x>=0` for `a>=3,x>=0`.
If `a>=c`, the analogous inequalities reduce to `c>=1`,
`a^2-5a+2c>=0`, and

    a^2-ac+c^2-5a+3c >= 0,

which after `a=c+x`, `c>=3`, is `c^2+cx+x^2-2c-5x>=0`.
The minimum checks occur at `c=3` and `x=0,1`; thereafter the quadratic is increasing. Hence the interval is nonempty.

The boundary complements are explicit.

* `c=0`: put `alpha=beta=2/(r-1)` on each core edge and core-triangle weight `(r-5)/((r-1)(r-2))`.
* `c=1`: on `AA` put `alpha=2/(a-1)`, and put `beta=2/a` on all core edges. Put every `AAC` triangle at `(a-2)/(a(a-1))` and every `AAA` triangle at `(a^2-6a+4)/(a(a-1)(a-2))`. Here `a>=8`.
* `c=2`: put `alpha=2/(a-1)` on `AA`, `beta=2/(a+1)` on every core edge, every `AAC` and `ACC` triangle at `(a-1)/(a(a+1))`, and every `AAA` triangle at `(a^3-6a^2+3a-2)/(a(a-1)(a-2)(a+1))`. Here `a>=7`.

Direct substitution gives unit load on every core edge, short degree two, and long degree two. All displayed weights are nonnegative in their stated ranges. Therefore every instance in this candidate is on the full one-third optimal face and

    L = [ C(r,2) + 2a + 2r ] / 3.                      (F)

For every feasible joint point of value `v`,

    3(L-v)=S_core+S_short+S_long.                       (I)

## 3. Aggregate two-direction Q witness: one shared boundary, not two leaf payments

Relabel the core by `F_3^k`. The affine triples `{u,v,-u-v}` partition all core edges. Let `D0` and `D1` be two distinct parallel classes. Each class has `r/3` vertex-disjoint triples and exactly `r` core edges; the two classes have disjoint edge sets.

Write

    a = 3t + b,  b in {0,1,2}.

Choose `t` triples from `D1`, mark their `3t` vertices short, and mark `b` additional vertices. Map this marked set bijectively to the actual A and transport all objects by the same bijection.

Select as integer core packing every affine line except all lines in `D0` and the selected `t` lines of `D1`.
Put

    beta_e = 1 on every edge of D0,
    alpha_e = 1 on every edge of the selected D1 triples.

Every core edge has exactly one owner: selected core triangle, alpha, or beta. Every core vertex has beta degree two. Every short vertex in a selected D1 triple has alpha degree two. Only the `b` remainder short vertices miss their alpha budget.

Thus this Q witness has

    S_core=0, S_long=0, S_short=2b,
    L-Q <= 2b/3 <= 4/3.                                 (Q)

Nothing is frozen from an old optimum, and the support may be globally reselected.

The aggregate alpha and beta graphs are unions of triangles. Consequently (Q) is generally NOT an actual host packing with two individual short and two individual long leaves: a triangle has edge-chromatic number three.

## 4. Shared-boundary continuation lemma

Let an aggregated joint point have integral core packing P and, for one leaf class of multiplicity m, an integral aggregate resource graph H on the core. Suppose R is a set of resource edges such that `H-R` has a proper edge-coloring with at most m colors.

Then deleting R from the aggregate allocation and assigning each remaining color class to one actual leaf produces valid host triangles. Every deleted resource edge had objective contribution one and occupied exactly three capacity rows: its core edge and the two corresponding spoke budgets. Hence deletion of R increases total unused capacity by exactly `3|R|` and decreases the packing objective by exactly `|R|`.

For several leaf classes with pairwise core-edge-disjoint aggregate graphs, choose the deletion sets on the AGGREGATE graphs first. The total conversion loss is

    sum_i |R_i|,

not a sum repeated separately for each individual leaf. This is the iteration invariant.

Define

    rho_m(H)=min{|R| : chi'(H-R)<=m}.

A future growing-layer argument will be sufficient if it constructs aggregate leaf graphs with total `sum rho_{m_i}(H_i)=O(r)` independent of the number of individual leaves. This candidate proves that condition only for the present `m=2` triangle factors; it does not prove the required growing-budget bound.

## 5. Apply the continuation once to both two-leaf classes

For a disjoint union of triangles, `rho_2` equals the number of components: every triangle needs at least one edge removed to become 2-edge-colorable, and deleting one edge turns it into a two-edge path.

Apply this independently to the aggregate graphs in Section 3:

    |R_beta|  = r/3,
    |R_alpha| = t.

In every triangle delete one fixed edge. The two retained edges form a path and receive opposite colors. Across components, the same two colors give two matchings. Therefore the beta graph is assigned to the two actual long leaves and the alpha graph to the two actual short leaves.

The resulting actual integer host triangle packing has

    S_core  = r/3 + t,
    S_short = 2t + 2b,
    S_long  = 2r/3,

so

    S_total = r + a + b <= 2r+2.                        (H)

Equivalently, the explicit packing has value

    L - (r+a+b)/3,

and therefore

    nu_star - nu <= (r+a+b)/3 <= (2r+2)/3.              (A)

This is a genuine host packing statement: the two short resource color classes and the two long resource color classes are actual matchings.

The two leaves of one class SHARE the one deletion set for their aggregate graph. We do not delete one boundary separately for each leaf.

## 6. Nine-core structured base instances

For `r=9`, all `a=3,...,9` are included. The checker freezes the complete core-triangle list, both aggregate resource lists, the deleted edges, and the four actual matching color classes.

The aggregate Q witness has total slack `0,2,4` according to `a mod 3`. The matching-converted host witness has total slack `r+a+(a mod 3)`. These are explicit witnesses, not claims that the displayed host packing is maximum.

The same construction is checked for every actual nine-core subset of size at least three, not merely prefixes. Relabeling is a graph isomorphism; it does not preserve old affine coordinates and is not required to.

## 7. Boundary audit

* Equal prefix `A=V` is included. Alpha uses selected D1 lines; beta uses D0. Their core edge sets are disjoint. The conversion deletes one edge from each resource triangle and yields four actual matching classes.
* Zero multiplicity is a property of the continuation lemma: if a leaf class is absent, take `H=R=empty`; it contributes no budget or loss. This does not assert that a different zero-budget parameter tuple lies on the present one-third face.
* The old C25 `(5,2,4,1,1)` quarter-valued point remains outside the one-third face. The C27 `(7,3,7,1,1)` twelfth-denominator point remains on it. Neither is a parameter instance of this theorem, and no Q value is imported from either.
* Core-leaf shared capacity is checked edge by edge. Alpha, beta and selected core triangles never overlap on a core edge.
* `Q`, `L_D`, `J_fix`, `J`, and `nu` remain distinct. Section 5 gives one actual nu witness, not equality between them.

## 8. Relation to the balanced one-depth lemma and next invariant

The merged C24 balanced-one-depth candidate allocates complete-graph matching classes to distinct outside vertices and proves objective loss by one-use internal-edge charging. Its edge ownership is explicit: the two triangle families use disjoint resource edge classes. Its odd-boundary allowance comes from one omitted near-perfect matching, with no hidden scale divisibility assumption.

The present continuation has the complementary role: an aggregated layer may be cheap for Q but fail individual-leaf realizability because of odd cycles. The quantity `rho_m(H)` isolates exactly that boundary. For p=q=2, the aggregate triangles become paths after one deletion per component and the two colors are the actual leaves.

The next multi-demand invariant must construct ALL aggregate short demand layers together and prove

    aggregate Q capacity defect + 3*sum rho_{m_i}(H_i) = O(r),

with a constant independent of the number of short leaves. Paying a fresh `Theta(r)` deletion set for every new layer would give `O(pr)` and is not an acceptable iteration. No such growing-layer invariant is proved here.

Status: NONTERMINAL_CHECKPOINT; candidate_only; best_verified_result=none.
