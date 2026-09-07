# C16: explicit fixed-template lifts, scaling limits, and residual clique reuse

Candidate ID: `candidate:erdos81-a01-c16-fixed-template-cost`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `79757835b1bf974d870daa971db778fa807cdf91`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Scope

The root bound and unrestricted same-order split domination remain open. This cycle gives an explicit lifting theorem for a specified finite quotient, exposes the nonuniform constants and the danger of scaling a linear error, and improves the unedited nonsplit family in C15.

All graphs are finite and simple. cp counts exact edge-disjoint clique partitions. C15's explicit triangle/K4 lifts and its fixed resource schedule are the immediate inputs. C01 supplies cp(J(q,t)) for t>=q. All other arguments below are elementary finite constructions with modular inverses. No mathematical program, enumerator, numerical optimizer, solver or proof assistant was run; there is no novelty claim.

## 2. C16.1: a direct lift for any bounded clique size

For k>=2 put
    L_k=lcm(1,...,k-2) if k>=3, and L_2=1.
The convention lcm(1)=1 handles k=3. Choose a positive integer p congruent to 1 modulo L_k. For k groups of size p, label k-1 groups by slopes a=0,...,k-2 and the last group by infinity. For each (u,v) in Z_p^2, take the clique with labels
    u+a*v in slope group a, and v in the infinity group. (1)

Any pair of finite slopes a!=b determines v by their label difference divided by a-b, and then u. This division is legitimate: 1<=|a-b|<=k-2 divides L_k, while p is congruent to 1 modulo L_k, so gcd(p,a-b)=1. A finite-slope label together with the infinity label also uniquely determines (u,v). Hence the p^2 cliques partition every intergroup pair exactly once and consume no within-group pair. For p=1, the statement is simply the one clique on one point from each group, so no ring convention is needed.

For target group size q>=1, choose the least p>=q congruent to 1 modulo L_k. Then
    q<=p<=q+L_k-1.
Pad each group to p, use (1), restrict vertices back to the q chosen points, and discard edgeless pieces. The result costs at most
    (q+L_k-1)^2                                          (2)
pieces. A subset of a clique is a clique, and the unique ownership of each surviving edge is preserved. No assertion about arbitrary edge deletion is used.

For k=2 and k=3 no padding is necessary. For k=4, L_k=2 gives exactly C15's odd-modulus construction after permuting group coordinates. Primality and any general transversal-design existence theorem are unnecessary for this explicit bound.

## 3. C16.2: finite quotient lifting with all constants exposed

Let F be a specified graph on b>=1 vertices with an explicit edge partition into h cliques K_1,...,K_h of sizes k_j>=2. Replace vertex i by a q-set V_i. Between V_i and V_l put all q^2 edges exactly when il is an edge of F. Inside V_i allow a graph with a supplied p_i-piece partition. Write P=sum_i p_i and ell_j=L_(k_j)-1.

Lift each quotient clique separately by Section 2. Distinct quotient pieces have disjoint edges, so their lifted pieces spend disjoint intergroup links even if they share groups. Add the within-group partitions. This gives the explicit bound
    cp(G)<=h*q^2+2q*sum_j ell_j+sum_j ell_j^2+P.           (3)
For an edgeless F the sums and h are zero. Equation (3) itself does not need chordality.

If each V_i is either a clique or an edgeless graph, P<=b. With n=bq, the sufficient condition
    h<=b^2/6                                             (4)
therefore implies
    cp(G)<=n^2/6+C_F*n,
    C_F=[2sum_j ell_j+sum_j ell_j^2+b]/b.                 (5)
Indeed n>=b, so the constant sum ell_j^2+b is at most its value divided by b times n.

This is a uniform-in-q result for a FIXED partition of a FIXED quotient. The coefficient C_F depends on the quotient and its chosen partition. The displayed least-common-multiple cost supplies no graph-independent constant when motif sizes grow. Even if all motif sizes are bounded, h and b must be tracked in (3); the word O(n) does not remove that dependence.

## 4. C16.3: chordality is not preserved by every block replacement

If F is chordal and every V_i is a clique, expand a perfect elimination ordering of F one whole group at a time. The remaining neighbors of an eliminated vertex consist of its own remaining group and later adjacent groups. They form a clique, so the resulting graph is chordal. This is a conditional class statement, not a transformation of an arbitrary graph that is asserted monotone for cp.

In contrast, replacing BOTH vertices of the chordal graph K2 by edgeless q-sets gives K_(q,q). For q>=2, two vertices from each side induce a four-cycle. Thus uniform intergroup adjacency alone does not ensure chordality. In the split specialization, replacing clique-side vertices by cliques and the other side by edgeless sets does preserve splitness directly. The partition inequality (3) is valid even when its graph is not chordal; domain membership is a separate obligation.

## 5. C16.4: a linear quotient error can become a quadratic lifting error

Let F be the four-vertex star K_(1,3). Its exact clique partition number is three, because it is a tree, and
    cp(F)=3=B(4)=floor(4*5/6).
Replace its center by K_q and each leaf by an edgeless q-set. The resulting graph is exactly J(q,3q), a split graph on n=4q vertices.

A quotient-only partition uses the three K2 motifs. Their lifted intergroup subgraphs are complete bipartite graphs and contain no larger allowed piece when each piece takes at most one vertex from each group. They require exactly 3q^2 pieces, plus one internal center clique when q>=2. This specific certificate exceeds n^2/6 by a quadratic term:
    3q^2-(4q)^2/6=q^2/3.
It cannot be brought to the root coefficient by a fixed linear allowance.

The graph itself is not a counterexample. C01 gives the exact unrestricted value
    cp(J(q,3q))=3q^2-binom(q,2)=(5q^2+q)/2
               <=B(4q).                                (6)
The improvement spends internal center edges in triangles together with crossing edges; that option was excluded by quotient-only lifting.

More generally, an input estimate h<=b^2/6+C*b multiplied by q^2 produces the error C*b*q^2=C*n*q, not C*n. Thus a bound such as h<=B(b), with its additive linear-in-b term, does not by itself satisfy the sufficient hypothesis (4). The star is an exact obstruction to that proof rule, not to the root or the domination target.

## 6. C16.5: exploit the residual outside cliques in C15

Consider C15's unedited G_q: Q is the union of four q-cliques A_i, every pair of vertices in Q is adjacent, I is the disjoint union of four q-cliques I_i, and the crossing links I_i-A_j exist exactly for i!=j. For q>=2 this is nonsplit and chordal as explicitly certified in C15.

Keep the prefix in C15: the three mixed quotient triangles
    (I_1,A_0,A_2), (I_2,A_0,A_3), (I_3,A_0,A_1),
and the K4 motif (I_0,A_1,A_2,A_3). Its cost is at most 3q^2+p^2, with p=q for odd q and p=q+1 for even q.

All edges remaining after that exact prefix form FIVE disjoint complete graphs:
    A_3 union I_1; A_1 union I_2; A_2 union I_3;
    A_0; I_0.                                           (7)
The first three are K_(2q), and the last two are K_q. In particular, partitioning the I_i edges separately from their residual neighbors, as in C15's general p_F bound, wastes an available merge in this special case. Using (7) gives
    cp(G_q)<=3q^2+p^2+5
             <=4q^2+2q+6
              =n^2/16+n/4+6.                            (8)
At q=1 the two singleton groups have no edges, so the same construction actually costs seven pieces.

Equation (8) lies below the attained same-order split benchmark for EVERY q>=1:
    (8q)(8q+1)/6-(4q^2+2q+6)
       =2(10q+9)(q-1)/3>=0.
Since the upper count is integral, cp(G_q)<=B(8q). Thus the specific nonsplit family has an explicit same-order split dominator with a substantially stronger partition bound than the previous general certificate.

The improved construction (8) uses large mixed K_(2q) residual pieces. It MUST NOT automatically inherit C15's 2D+A crossing-edit allowance, whose proof required every touched mixed piece to have at most four vertices. The older robust bound and this stronger unedited bound are alternatives with different hypotheses.

## 7. Attack pass and exact next action

Audited: k=2,3,4; q=1; composite moduli; all slope differences being units; vertex restriction; shared groups versus shared links; P=0; fixed versus varying quotient constants; the induced C4 after edgeless substitution; the exact star certificate; and the five actual residual cliques in (7).

This cycle discards two prospective shortcuts: arbitrary edgeless cloning preserves chordality, and a quotient bound with an additive linear error automatically transfers to a root-scale blow-up bound. It does not discard the admitted route. Canonical failed-route records remain read-only and unchanged.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: explicit lift (3), its conditional fixed-template consequence, and residual improvement (8).
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.

Next action: formulate a partial-link template certificate that charges internal group edges only when consumed, and leaves the actual residual graph available for later clique merging. It must include the star and C15 family as exact regression cases. Seek a bound uniform when the number of neighborhood classes grows, rather than repeating fixed-template arguments with hidden quotient-dependent constants.
