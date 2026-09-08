# C25: a charged leaf-polytope rounding lemma and an optimal-extreme-point freezing obstruction

Candidate: candidate:erdos81-a01-c25-extreme-rounding
Repository: vibemathing/problem-erdos-81-chordal-clique-partition
Problem: problem:erdos-81-chordal-clique-partition
Attempt: attempt:web-20260906-erdos81-a01
Route: route:split-extremal-reduction-v1
Graph: graph:erdos81-initial-v1
Transport obligation: obligation:erdos81-split-extremal-reduction
Base revision: 4a13193cdbb4aa4578f793434b56d409a4a08812
Primary owner: math-proof. Verdict: candidate_only. best_verified_result: none.

## 1. Exact scope

Write [d]={0,...,d-1}, with [0] empty. Let G(r,a,b,p,q) have core K_r, p mutually nonadjacent short leaves on [a], and q mutually nonadjacent long leaves on [b], with no other leaf edges. Usually 0<a<b<=r; zero counts, empty and equal prefixes are permitted as explicit boundary inputs. All graphs are finite and simple. nu is edge-disjoint triangle packing, nu_star its fractional edge-capacity-one relaxation, and cp exact edge-disjoint clique partition number.

C24's edge-specific model maximizes sum z_T + sum alpha_e + sum beta_e subject to

  alpha_e + beta_e + sum_(T containing e) z_T <= 1  (each core edge),
  sum_(e incident to u) alpha_e <= p                (u in [a]),
  sum_(e incident to u) beta_e <= q                 (u in [b]),
  all variables nonnegative.

Alpha exists only on K_[a], beta only on K_[b], and z indexes actual core triangles. Its fractional value is exactly nu_star: aggregate mixed triangles for projection, and distribute each color's aggregate edge load uniformly among its leaves for lifting. Zero counts force zero incident variables, without division. Its integer optimum is J; capacity one makes each variable zero or one. J permits allocated graphs of degrees at most p and q without initially requiring their edge colorability. C24 proves 0<=J-nu<=floor(a/2)+floor(b/2).

The current target remains: an absolute K such that nu_star-J<=Kr for every capped two-prefix instance. This document does NOT prove or disprove that target. It proves a correct conditional rounding bound and gives a new all-order obstruction to a preprocessing rule: permanently fixing all z_T=1 of an arbitrary optimal extreme point, or permitting only O(r) of these triangles to be reopened, can lose superlinearly. The true target gap in the obstruction family is exactly ONE. This distinction is essential.

No earlier seven/nine-vertex examples, saturated-prefix or staircase subclass arguments are used as new results. The root cp<=n^2/6+Cn and the weaker uniform o(n^2) statement retain their different identities. No trusted verifier or closure receipt is asserted.

## 2. A leaf-only rounding lemma with an explicit injection

Fix a genuine integer core triangle packing P. Remaining core capacities c_e are zero or one. The leaf-only polytope is alpha_e+beta_e<=c_e with the two endpoint-budget systems above. Take an extreme optimum x of this finite bounded polytope. An edge group consists of its one or two allowed coordinates. A group is fractional if it has a nonintegral positive coordinate.

For each fractional group choose a nonzero tangent vector supported on that group, preserving its tight local capacity row and its zero coordinates. If its sum is below one, increasing one positive coordinate is such a two-sided infinitesimal direction. If its sum is one, it must have two positive coordinates, both strictly below one, and the direction is (1,-1). Capacity-zero groups cannot be fractional. These directions have pairwise disjoint supports.

Project the directions to the active endpoint-budget rows (at most a+b rows). Their images are linearly independent. Otherwise a nonzero linear combination gives a feasible perturbation in both signs: tight local and endpoint rows stay fixed, zero coordinates stay zero, and all strict inequalities and positive coordinates retain a margin for sufficiently small perturbations. This contradicts extremality. Therefore there are at most a+b fractional edge groups.

This is also an executable charging map, not merely a count. Form a bipartite graph from fractional groups to active tagged endpoint rows, joining a group to a row where its selected direction has nonzero coefficient. Every set of groups has at least as many neighbors, by linear independence of its projected columns. A matching covering the groups follows by the finite augmenting-path argument: if an unmatched group cannot reach an unmatched row, its alternating reachable sets violate that neighbor inequality. Repeated augmentation terminates after at most the number of groups. Each fractional group is thus injected into a distinct (short,u) or (long,u) row.

Discard all fractional groups and retain coordinates equal to one. This only reduces nonnegative capacity use and preserves P. A discarded group has objective mass at most one, so the objective loss is at most a+b<=2r. Each lost unit is charged to its matched tagged endpoint. No separator cost and no per-leaf repetition occurs.

Let Q(G) be the maximum of |P| plus the fractional leaf-only value over all integer core packings P. Applying the lemma to an optimizing P gives

  0 <= Q(G)-J(G) <= a+b.                                  (L)

Only the preceding integrality of core capacities justifies the argument. With fractional z, a tight edge row can have a fractional remaining capacity; a locally fractional group then need not possess any nonzero local tangent. One must NOT apply (L)'s rank count to that different polytope.

Empty prefixes, zero counts and missing edge groups are simply omitted; equal prefixes can be retained as two tagged systems, so the stated bound does not require a false assertion that merging two separate degree budgets preserves J. Repeated descriptions of a maximal clique create no variables or capacity. Parity is not assumed. This proof supplies a replacement for unjustified matching half-integrality, but leaves nu_star-Q uncontrolled.

## 3. A diagnostic non-half-integral joint extreme point

For (r,a,b,p,q)=(5,2,4,1,1), the following positive coordinates form an optimum extreme point of value five:

  z014=1/2, z023=1/4, z024=1/2, z123=1/4,
  z134=1/2, z234=1/2,
  alpha01=1/2,
  beta02=1/4, beta03=3/4, beta12=3/4, beta13=1/4.

All other coordinates are zero. Unit dual prices on core edges 01,03,13,24 and on the long endpoint row 2 cover all columns and total five. The tight-row matrix on these eleven columns has rank eleven; the exact audit records both rational implementations and the rank. An integer allocation of value five exists. This is a diagnostic of the full coupled model, not a counterexample to a linear gap. No integral z coordinate is present here to remove. It cannot be treated as an ordinary half-integral matching extreme point.

## 4. Finite ingredients for a new freezing family

Let F have vertices 0,...,18. Vertices 0,...,15 are a 4 by 4 array; two are adjacent when they have the same row or column. Vertices 16,17,18 are isolated. F's nontrivial maximal cliques are its four rows and four columns, all K4; their edge sets are disjoint. Thus |E(F)|=48. Every triangle lies in one such block, and each K4 has integral packing one and fractional packing two (its four triangles of weight 1/2).

The file templates.json supplies exactly 41 triangles decomposing K19-F, and exactly 58 triangles packing the graph with core K19, short leaf 19 on {0,1}, and long leaf 20 on {0,1,2,3}. These are finite explicit certificates, not theorem-library or numerical-solver assumptions. The checker verifies their edge sets, collisions and leaves directly. The 58-triangle packing leaves exactly {2-17,3-12,12-17}.

We also need a fully explicit design of K19. Take all modulo-19 translates of the three triples

  (0,1,4), (0,2,9), (0,5,11).

Their unoriented differences respectively cover {1,3,4}, {2,7,9}, {5,6,8}; hence every distance 1,...,9 occurs once among the starters. Translation then covers every pair exactly once. This is a 57-triangle decomposition S_1 of K19.

For k>=1 set r=19^k and H_k=F Cartesian-power k. An H_k edge changes exactly one coordinate, along an F edge. Its coordinate-row/column blocks are edge-disjoint K4s, numbering

  ell_k=8k19^(k-1).

Every triangle of a Cartesian product must change the same coordinate on all its edges: changing distinct coordinates on two edges makes their opposite endpoints differ in two coordinates. Consequently every H_k triangle is confined to one of these blocks. H_k has 6ell_k edges, packing value ell_k and fractional value 2ell_k. H_k need not be chordal; the HOST graph below is split and therefore chordal.

## 5. Complement decomposition with unique edge ownership

We construct complete designs S_k of K_(19^k) and decompositions P_k of K_(19^k)-H_k together. Base S_1 is above and P_1 is the explicit 41-triangle list.

Write a new vertex as (u,i), where u is an old vertex and i in Z19. First copy S_1 in every fixed-u fiber. For every triple (u,v,w) of S_(k-1), ordered once, add all 19^2 triples

  ((u,i),(v,j),(w,10(i+j) mod 19)).                       (D)

Since 10 is the inverse of two modulo 19, any pair between two distinct fibers determines the third last-coordinate uniquely. Together with the within-fiber designs, this proves S_k is an exact triangle decomposition. No random choice or limiting argument is involved.

To define P_k, take:
(i) copies of P_(k-1) at each common last-coordinate i;
(ii) copies of P_1 in each fixed-u fiber;
(iii) the triples (D) with i!=j.

The last-coordinate rule is idempotent: 10(i+i)=i. For i!=j its third coordinate is different from both. Hence (iii) uses exactly pairs differing in both the old and last coordinates. Types (i) and (ii) cover the complementary pairs differing only in old or only in last coordinates. These are disjoint exhaustive categories of K_r-H_k, proving exact ownership and the recurrence. In particular

  |P_k|=binom(r,2)/3-2ell_k.

The integer k decreases in the recursion; all finite lists terminate. Redundant bag descriptions have no effect. The checker instantiates the entire construction for k=1 and k=2; the paragraph above, not those two tests, proves all k.

## 6. An optimal EXTREME point with a bad integral part

Let G_k=G(r,2,4,1,1), r=19^k, using lexicographic core labels. Its three maximal cliques are [r], {0,1,x}, and {0,1,2,3,y}. Both multiplicities are positive and already capped. Let A={0,1,2,3}, an H_k block.

Set z_T=1 for every T in P_k. In each H_k block except A, put weight 1/2 on all four triangles. At A put

  z023=z123=1/2, alpha01=1,
  beta02=beta03=beta12=beta13=1/2,

with all other coordinates zero. Every core edge has total load one. Each of the two short and four long endpoint budgets has load one. With m=binom(r,2), the objective is

  L=m/3+2.                                               (E)

Uniform dual prices 1/3 on core-edge rows and on all six endpoint rows cover every column exactly once and have value m/3+2. Thus (E) is nu_star, with an explicit primal/dual certificate.

The displayed optimum is an extreme point, not a nonextreme uniform averaging artifact. In any convex decomposition, zero coordinates stay zero and every z=1 coordinate stays one by its capacity-one bound. Each ordinary K4 support has four columns uniquely determined by its six tight edge equations (rank four). The anchor has seven positive columns. Alpha01 is fixed by edge01; then beta02=beta03=1-z023 and beta12=beta13=1-z123. The tight long rows at 0 and 1 force z023=z123=1/2, hence all seven coordinates uniquely. Blocks may share vertices but not core edges, and no leaf variable exists outside A. Thus all positive coordinates are uniquely fixed. Local rank checks 4 and 7 are also supplied in the executable certificate.

Now require all original P_k triangles to remain selected. The remaining graph is H_k, even if arbitrary previously zero residual triangle variables may be activated. Each nonanchor block contributes at most one integer core triangle. The anchor joint optimum is three: alpha01, beta02 and z123 attain it. Four would require three leaf edges plus one core triangle, because 3Z+U<=6 and U<=3. This forces alpha01 and a beta perfect matching avoiding01; the three remaining edges are not a triangle. Hence four is impossible.

Writing J_fix for the optimum under this extra freezing constraint, we obtain the EXACT formula

  J_fix=|P_k|+ell_k+2=m/3-ell_k+2,
  nu_star-J_fix=ell_k=(8/19)r log_19(r).                  (F)

The odd/nonintegral blocks here overlap at vertices. There are superlinearly many blocks, so no injection charging each block once into only O(r) vertex or two-boundary slots can exist after this freezing. Edge-disjointness of local obstructions does not imply vertex-disjointness.

## 7. Actual J, nu and cp: this is NOT a target counterexample

For p=q=1, an integral leaf-allocation graph of degree at most one is already a matching. Therefore J=nu for G_k, with no coloring loss.

The host has m+6 edges. Only core vertices 2 and 3 have odd degrees; packing triangles cannot change degree parity. Since r=19^k is 1 modulo 6, m+6 is divisible by three. A nonempty packing leave therefore has at least three edges, giving nu<=m/3+1.

In S_k, replace the 57 triangles of the distinguished K19 fiber (old coordinate zero) by the finite 58-triangle anchor witness, relabeling leaves 19,20 as x,y. All other complete-design triangles remain. They consume no edges inside that fiber and no leaf spokes. This is an actual packing of size m/3+1, so

  J(G_k)=nu(G_k)=m/3+1,
  nu_star(G_k)-J(G_k)=1.                                 (G)

All clique-partition values can be specified too: cp(G_k)=7. The full core plus its six leaf spokes gives seven. Here is an elementary lower proof for every r>=6. Pieces through x partition its two neighbors, costing i=1 or2; pieces through y partition its four neighbors, costing j=1,...,4. If i=1 the pair01 is already consumed, so y blocks cannot contain both 0 and1. The residual core must be partitioned by further cliques.

If i+j>=6, at least one core piece is still required. If i+j=5, an AA edge has been removed and the residual is not a complete graph, requiring at least two pieces. If i+j=4, the residual contains a missing pair joined to two untouched core vertices outside A, an induced K4-e, which needs three pieces. If (i,j)=(2,1), A is edgeless in the residual; three A vertices and two untouched core vertices induce K2 join I3, whose clique-partition lower bound is five: give its six crossing edges price +1 and its core edge price -1. If (i,j)=(1,2), the two y blocks are either 3+1 with 0 and1 separated or two cross pairs. Directly listing these partitions shows a remaining induced P3 in A. Joining it to two untouched core vertices gives K5-e, which needs four pieces, so the total is at least 1+2+4=7. The case (1,1) is impossible. K4-e has cost three. For K5-e, a K4 piece leaves three spokes; without a K4, three pieces would have to be three triangles covering all nine edges, contrary to the odd degrees. Restricting a clique partition to an induced subgraph cannot increase its number of pieces. This proves the lower bounds used above and cp=7.

Thus the true two-prefix instance has gap ONE, while the frozen-face gap in (F) is superlinear. (F) excludes a preprocessing promise, NOT the requested uniform nu_star-J bound or the ProblemContract.

## 8. Even reopening only linearly many old triangles is insufficient

Suppose s original P_k triangles are allowed to be reopened and all others remain fixed. This frees exactly 3s additional core edges. From any integer solution on the enlarged free graph remove every allocated object using a newly free edge. Edge ownership is unique, so these removed objects inject into the 3s new edges, losing at most 3s objective units. The remaining free solution is feasible in H_k. The fixed part has meanwhile lost s units. Therefore the total optimum with such permission is at most

  J_fix+2s,
  nu_star-(best with s reopened) >= ell_k-2s.             (R)

Consequently s=O(r) cannot yield an O(r) deficit in this family. A successful global reoptimization may reopen Omega(r log r) old integral triangles; this can improve rather than lose objective. The obstruction does not prohibit selecting a better optimal extreme point, temporary algebraic subtraction, or a global exchange with many reopened triangles. It prohibits treating the old integral support as irrevocable, or giving it only a linear reopening budget.

## 9. Exact computation and proof dependencies

The two finite template lists were discovered by bounded floating-point MILP search, but only their exact edge-list checks are proof inputs. Their discovery status is not an optimality or mathematical admission argument. The proof uses finite LP extreme-point/duality facts with explicit feasible witnesses, elementary rank and augmenting-path reasoning, the displayed modulo-19 designs, parity, and exact edge counting. No external design theorem, screenshot, search summary or unverifiable source claim is needed.

freezing_checker.py checks all edges for k=1,2, both local support ranks, both integer packings, fractional loads, the dual bound and parity. extreme_audit.py compares two rational LP implementations and two separately organized integer optimizers on all capped boundary-inclusive instances with r<=4, and tests the injection on every residual core graph through r=4 and all prefix pairs at p=q=1. A five-core quarter-valued example is a named extra test, not a complete five-core range. Twelve new mutations are included in the construction checker. Actual process and code/output digests are supplied separately. Neither finite tests nor generator-authored proofs are trusted verifier receipts.

## 10. First open lemma

The original absolute-K inequality nu_star-J<=Kr remains open. The conditional bound (L) isolates a new equivalent sufficient target nu_star-Q=O(r), where the maximizing integral core packing may be completely reselected. A continuation must maintain actual core-edge ownership and endpoint budgets, but its potential cannot count every changed original integral triangle as an irrecoverable unit loss: (R) defeats that invariant. A concrete next atomic test is whether a core-reselection normal form can be chosen with at most O(r) residual fractional obstruction rank, allowing all old z=1 triangles to reopen; audit its exact objective change rather than its number of exchanges.

No multi-level theorem follows: even the positive leaf charging pays once per tagged class, totaling sum of prefix sizes for many classes unless a further invariant is proved. No root closure, EvidenceLink, Result or Solution is produced. Status: NONTERMINAL_CHECKPOINT.
