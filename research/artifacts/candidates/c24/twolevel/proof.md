# C24 two-prefix joint rounding: exact reductions and a linear-cost leaf lift

Candidate ID: candidate:erdos81-a01-c24-twolevel-joint
Repository: vibemathing/problem-erdos-81-chordal-clique-partition
Problem: problem:erdos-81-chordal-clique-partition
Attempt: attempt:web-20260906-erdos81-a01
Route: route:split-extremal-reduction-v1
Graph: graph:erdos81-initial-v1
Transport obligation: obligation:erdos81-split-extremal-reduction
Protected base: 09c2b6f3e277eb20fc34d0add65ee8d027c5bb37
Primary owner: math-proof. Verdict: candidate_only.

## 1. Scope and the remaining gap

Let G(r,a,b,p,q) have a complete core [r], p independent vertices with neighborhood [a], and q further independent vertices with neighborhood [b]. There are no other edges. The main domain is 0<a<b<=r and p,q>=1; zero multiplicities and empty/equal neighborhoods are explicitly handled below. All packing is EDGE-disjoint. Write nu for integral triangle packing and nu_star for the capacity-one fractional packing. The desired statement is an absolute C with nu_star-nu<=C(r+p+q).

This manuscript does NOT prove that entire statement or give a counterexample to it. It closes a constituent lifting step with an explicit linear cost, gives exact multiplicity and fractional-model reductions, and excludes a stronger exact lifting shortcut. The unrestricted chordal root cp<=n^2/6+Cn and exact split domination remain open. C22/C23's uniform o(n^2) proof candidate is different from all these statements. No trusted verifier, EvidenceLink or closure receipt is produced here.

The main new all-order inequality uses the edge-specific integer relaxation J defined in Section 4:

    0 <= J(G)-nu(G) <= floor(a/2)+floor(b/2) <= r.        (1)

Its fractional relaxation is EXACTLY nu_star(G). Thus the unresolved loss is nu_star-J, not the conversion of an integral core allocation into individual leaf matchings. For two prefix levels, a bound nu_star-J<=K*r would give the requested result with C=K+1. This is an explicit open lemma, not an assumed premise.

## 2. Exact truncation of repeated neighborhoods

Define f(d)=0 for d<=1, f(d)=d-1 for positive even d, and f(d)=d for odd d>=3. Replacing the multiplicity of any independent class with clique neighborhood D, |D|=d, by min(m,f(d)) preserves BOTH nu and nu_star. It need not preserve cp.

For integer packing, retain the union F of the core edges used by that leaf class. F is simple because core-edge capacity is one. Color K_d with f(d) matching colors, restrict those colors to F, and assign each retained edge to the retained leaf of its color. Its two spokes do not repeat within a color. The set of core edges consumed is unchanged, so every other triangle, including those assigned to the other leaf type, remains compatible. The objective is unchanged.

For clarity the matching factorization is explicit. For even d, label K_d by infinity and the odd cyclic group Z_(d-1). Color z consists of infinity-z and {z+i,z-i}, 1<=i<=(d-2)/2. Finite pairs have a unique midpoint. For odd d, perform this factorization on K_(d+1) and delete the extra point, giving d near-perfect matching classes. Degrees zero and one yield no triangles.

For a fractional packing, let alpha_e be the sum of the mixed weights of this class using core edge e. Then 0<=alpha_e<=1. When m>f(d)>0, give each retained leaf weight alpha_e/f(d) on its e-triangle. Each spoke load is at most (d-1)/f(d)<=1. Core-edge loads and total weight are exactly preserved. Conversely every packing of the reduced induced graph remains a packing of the original graph. This proves the two equalities in both directions.

Apply the operation sequentially to the two types. After deleting triangle-inactive leaves, their counts obey p<=f(a)<=a and q<=f(b)<=b, so the reduced order is at most 3r. There is no hidden multiplicity-dependent constant. If a=b, combine the identical classes before truncating. Distinct leaves sharing a neighborhood still have distinct spokes; duplicate descriptions of one maximal clique do not create additional vertices or edge capacity. Empty neighborhoods, singleton neighborhoods and zero counts require no division.

## 3. An exact nine-row fractional model, and its limitation

Partition the vertices into A=[a], B=[b] minus A, C=[r] minus [b], X (short leaves), and Y (long leaves). Their sizes are a,b-a,r-b,p,q. The possible edge types are AA,AB,AC,BB,BC,CC,AX,AY,BY. The possible triangle types are

    AAA,AAB,AAC,ABB,ABC,ACC,BBB,BBC,BCC,CCC,AAX,AAY,ABY,BBY.

Omit an edge or triangle type when its vertex class sizes make it impossible. Let x_T be the TOTAL weight of triangles of type T. For an edge type e, let B_e be its number of actual edges, and let A_eT be the number (0,1,2 or 3) of e-type edges in a T-type triangle. Consider

    L = max sum_T x_T,  A x <= B,  x>=0.                 (2)

Projection of a graph fractional packing is feasible. Conversely, distribute x_T uniformly over all actual triangles of type T. The permutation group of each class is transitive on each edge type. Double-counting incidences shows that every e-edge then has load (sum_T A_eT*x_T)/B_e<=1. This proves L=nu_star, including empty classes. No symmetry of an integer optimum is assumed.

Let I be (2) with integer x_T. Then nu<=I<=nu_star and

    0 <= nu_star-I < 9.                                 (3)

Indeed, take an extreme optimum. Its positive columns are linearly independent: otherwise a sufficiently small signed perturbation supported there would preserve A*x and nonnegativity in both directions. There are at most nine rows, hence at most nine positive coordinates. Floor those coordinates. All coefficients are nonnegative, so the integer vector remains feasible and loses less than nine. Finite boundedness and attainment are direct, since every triangle has an incident edge of finite capacity.

Equation (3) does not say I can be realized as a packing. Even the following additional necessary integral constraints do not suffice: for each class V_i,

    sum_T multiplicity_i(T)*x_T <= |V_i|*floor(deg(V_i)/2). (4)

They are obtained by summing the integer number of incident packed triangles over actual vertices. They are NOT valid constraints for unrestricted fractional packing, where the floor must not be inserted. Section 6 supplies a failure of exact realization after the multiplicities have already been capped.

## 4. Preserve actual core edges, not just totals

For each core triangle T choose z_T; for each e in K_[a] choose alpha_e; for each e in K_[b] choose beta_e. Missing variables are zero. The edge-specific LP is

    maximize sum_T z_T + sum_e alpha_e + sum_e beta_e,
    alpha_e+beta_e+sum_(T containing e)z_T <= 1     (every core edge),
    sum_(e incident with u)alpha_e <= p            (u in [a]),
    sum_(e incident with u)beta_e <= q             (u in [b]),
    all variables nonnegative.                              (5)

This too has value exactly nu_star. Aggregating the original mixed triangles proves one direction. For the converse, divide alpha_e uniformly among the p short leaves, and beta_e among the q long leaves. The two displayed degree bounds are precisely the individual spoke bounds after division. If a count is zero, its incident nonnegative variables must be zero, and no division is made.

Define J by requiring every variable in (5) to be integer. The core capacity makes every variable zero or one. An integral feasible point consists of an actual edge-disjoint core triangle family P, a short-edge graph H_X and a long-edge graph H_Y. Their edge sets are mutually disjoint and

    H_X subset K_[a], Delta(H_X)<=p,
    H_Y subset K_[b], Delta(H_Y)<=q.                        (6)

It does NOT yet require p- or q-edge-colorability. Every actual packing projects to such a point, so nu<=J<=nu_star. In contrast to the false aggregate lifting claim, this object keeps the exact core edge identities and all chosen core triangles.

### Constructive leaf lift and charging map

Color H_X with Delta(H_X)+1 colors by the fan algorithm below. If at most p colors occur, keep them all. Otherwise Delta(H_X)=p and at most p+1 colors occur. Delete a least populated color class. That class is a matching and has at most floor(a/2) edges. Assign each remaining color to a distinct short leaf, and turn every edge in it into the corresponding mixed triangle. Do the same for H_Y, losing at most floor(b/2) edges. Preserve P unchanged.

Within a leaf, matching colors ensure that spokes are disjoint. Between leaf classes and P, (6) ensures core-edge disjointness. Each lost objective unit is a deleted matching edge. Charge it to its smaller endpoint, tagged X or Y. This is an injection within each tagged class, with at most one discarded matching per TYPE, not per leaf or separator. This proves (1).

Other unused edges of (5) have not been silently charged away: the difference between the fractional objective and the best integral (5) is exactly the still-open nu_star-J. The construction bounds the subsequent conversion loss and nothing more.

### Fan algorithm and proof, without a black-box coloring assumption

Use Delta+1 colors for a finite simple H. Start with no colored edges. At an uncolored edge u v_1 select a color alpha missing at u. Build distinct neighbors v_1,...,v_k: choose a missing color c_i at v_i; if c_i is missing at u, stop; otherwise follow the unique u-edge of color c_i, unless its other endpoint is already in the list. Then u v_(i+1) has color c_i. No transition color is alpha. The list grows strictly until it stops.

Put beta=c_k. If beta is missing at u, shift colors left along the fan and color its last spoke beta. Otherwise u v_j has color beta for some j>=2, so beta is missing at v_(j-1). Follow the maximal alpha/beta alternating path from u and interchange its two colors. The path starts with beta, so beta is now missing at u. If its other endpoint is not v_(j-1), that vertex was not on the path (beta was missing there); rotate only the prefix through v_(j-1) and color its last spoke beta. If the endpoint is v_(j-1), alpha is now missing there, while v_k is outside the path and still misses beta. The full fan is still valid after u v_j changes to alpha; rotate the full fan and finish at v_k.

All other fan transition colors are different from alpha and beta, so their required missing-color relations survive the interchange. At each rotation a color moves to a vertex where it is missing; the colors at u are only permuted. Thus every step preserves proper coloring and increases the number of colored edges by one. The finite edge count is a strict termination bound. This proves the Delta+1 coloring fact and supplies the implemented exchange rule. No efficient asymptotic running-time claim is required; the provided implementation checks properness after every insertion.

## 5. The previously known bad allocations as regression controls only

The old seven-vertex allocation and the within-halves J(2s,s-1) assignment are not new counterexamples here. They are tested only to reject forbidden total-only reasoning. For the latter, take two packed triangles x u_1 u_2 and x v_1 v_2, with the u's and v's in opposite core halves. With distinct u_3 and v_3 and free cross edges, replace them by

    x u_1 v_1, x u_2 v_2, u_1 u_2 v_3, v_1 v_2 u_3.

This is a verified 2-to-4 improvement. Its resources are the two freed internal edges, the old x-spokes and formerly unused cross edges; there is no repeated edge. The implementation also exhaustively searches strict improvements removing at most two triangles. Cardinality increases and is bounded by |E|/3, so termination is clear. Neither the fact that these controls improve nor the bounded tests prove a global approximation bound for a locally optimal packing. The invariant needed for arbitrary r remains the integral feasibility of (5) together with a controlled fractional deficit.

## 6. A normalized two-level exact-lift obstruction, with full certificates

Take (r,a,b,p,q)=(6,4,6,2,1). The core is 0,...,5, short leaves are 6,7, and the long leaf is 8. These multiplicities already satisfy p<=f(4)=3 and q<=f(6)=5. Equivalently the graph has a K7 on {0,1,2,3,4,5,8} and two leaves joined to A={0,1,2,3}. Its maximal cliques are exactly

    {0,1,2,3,6}, {0,1,2,3,7}, {0,1,2,3,4,5,8}.

Let D={4,5,8}. Exact values are

    n=9, m=29, nu=8, nu_star=9, lambda=11, p23=13, cp=9. (7)

Every vertex has even degree. Nine packed triangles would leave exactly two edges, but a nonempty even-degree simple graph cannot have only two edges. Hence nu<=8. The eight triangles

    014,235,028,136,037,127,158,348

are pairwise edge-disjoint and attain eight.

For a uniform fractional certificate, give each triangle with two A vertices and one short leaf weight 1/4; each triangle with two A and one D weight 1/6; each triangle with one A and two D weight 1/4; all others zero. AA loads are 2/4+3/6=1, AD loads are 3/6+2/4=1, DD loads are 4/4=1, and short spokes have load 3/4. The total is 3+3+3=9. Prices one on AA and DD, zero elsewhere, cover every triangle and have total nine. This supplies matching primal/dual certificates.

The abstract counts AAB=2, AAX=4, ABB=1, ABY=2 (here B={4,5} and Y={8}) have total nine and satisfy every edge-type capacity and (4). They cannot be realized, by the leave parity argument above. This is the first such normalized failure with a>=2 in the complete increasing-order parameter audit through order nine, not a global minimum over arbitrary graphs or over a different model.

There is also an explicit integral point of the stronger, edge-specific model (5), with value nine:

    H_X={01,02,12}, H_Y={03,14,25},
    P={045,135,234}.

The short graph has maximum degree two and needs three matching colors. The fan construction drops just one of its edges and realizes eight triangles. Since J<=nu_star=9, this proves J=9 and J-nu=1 in this graph. The linear lifting allowance cannot in general be replaced by zero.

For completeness, cp=9 has both a construction and a finite combinatorial lower proof. Use the K7 once and all eight short spokes singly. In any other partition, the pieces through each short leaf partition its four A-neighbors into blocks. Blocks of the two partitions intersect in at most one vertex, since AA edges cannot be spent twice. Let their total number of blocks be k. Then k>=4. If no AA edge is spent, k=8 and the core needs one further piece. If k>=5 and an AA edge is spent, the residual core contains an induced K5 minus one edge, using that missing pair and the three D vertices. That graph needs at least four clique pieces: a K4 leaves three spokes; without K4, a three-piece partition would be a triangle decomposition of its nine edges, contradicting its odd degrees. Thus the original cost is at least 5+4=9. Finally k=4 forces two different 2+2 partitions of A. Their consumed edges form a 4-cycle. In the residual core, give AD edges weight +1, DD edges -1, and the two remaining AA edges -2. A clique has at most two A vertices; checking k_A=0,1,2 and k_D=0,1,2,3 gives total weight at most one. The objective is 12-3-4=5, proving that this residual requires at least five pieces. The total is at least 4+5=9.

This is an obstruction to exact lifting, not a superlinear gap family, and not a root counterexample.

## 7. Actual finite execution and scope

All published computational claims below were actually executed with CPython 3.13.5 and Fraction arithmetic. The frozen prior recovery checker provides a packing tableau and a separate equality-partition revised simplex, a triangle-conflict integer search, and a residual-edge partition optimizer. New code provides the exact orbit LP/ILP, a separately formulated edge-specific revised-basis LP, core-mask matching DP, fan coloring, and exchange checks.

Complete two-prefix positive-multiplicity representations of total orders 4,...,9 were checked: respectively 1,5,15,35,70,126, for 252 total. Two formulations agree on fractional values; integer routines compute nu and cp; the orbit inequalities and cap comparisons were checked. The order-nine run initially stopped after 108 complete parameter rows at its internal deadline. Two later, disjoint indexed runs checked rows 108..116 and 117..125. The combined report validates exact parameter identities and no gaps/duplicates before calling order nine complete. The first outer timeout's exit code was not read back; no successful exit is invented for it.

All capped parameter tuples with core orders 2,3,4,5 were also checked independently, with counts 2,14,42,108 (166 total), using the orbit tableau, edge-specific revised-basis LP and exact core-mask DP. The cap theorem, not extrapolation from small samples, relates these finite tuples to arbitrary repetition at those fixed core orders.

The fan algorithm was tested on all 1,100 labeled simple graphs of order at most five. The discarded matching charges were checked. Twenty-seven explicit within-halves improvements and twelve new error injections passed. The normalized nine-vertex certificate was separately replayed, as were empty/equal-neighborhood, zero-count and small-order controls. None of this is a general proof by enumeration or an exhaustive search over the continuous optimal dual face.

The run record, exact parameter tables, source hashes, certificates and executable sources are provided together. They are generator self-checks, not an admitted verifier or EvidenceLink. Historical partial archive files elsewhere in the C24 branch are not used as proof or execution inputs for these results.

## 8. First open lemma and continuation invariant

The next mathematical obligation is to prove, or disprove, an absolute K such that the fractional optimum of (5) exceeds its integral optimum J by at most K*r, after the exact multiplicity caps. The fan proof already pays at most r for the subsequent conversion. The nine-row model is an exact fractional compression and its integer numerical gap is less than nine, but its realizability defect is not controlled; Section 6 prohibits declaring it zero.

A valid continuation must keep the exact three-way ownership of each core edge: short, long, a specified core triangle, or unused; its endpoint degree budgets; and a bound on the loss from the original fractional objective. It may recolor a type's edges without changing that ownership. The owner map cannot be replaced by separate leaf totals or independent separator budgets. For more levels, deleting one matching per level would cost sum d_i/2; a uniform linear induction would need an additional nonrepeated charging invariant. Such a multi-level bound has NOT been established here.

Status: NONTERMINAL_CHECKPOINT. The two-level theorem, general nested theorem, and ProblemContract root remain open. No stability assertion is inferred from failure of an exact lifting shortcut. best_verified_result=none.
