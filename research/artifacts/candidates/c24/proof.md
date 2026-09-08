# C24: exact replay, linear-gap subclasses, and a simplicial-step obstruction

Candidate ID: `candidate:erdos81-a01-c24-replay-linear-gap`
Repository: `vibemathing/problem-erdos-81-chordal-clique-partition`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Transport obligation: `obligation:erdos81-split-extremal-reduction`
Base: `09c2b6f3e277eb20fc34d0add65ee8d027c5bb37`
Primary owner: math-proof. Verdict: candidate_only. Best verified result: none.

## 1. Frozen statements and actual progress

All graphs are finite and simple, including isolated vertices. A clique partition partitions E(G), not V(G), into nonempty, pairwise edge-disjoint clique edge sets; vertices may be reused. The empty edge set has cost zero. Write cp for arbitrary-clique partition cost, p23 for edge/triangle partition cost, lambda for its fractional equality-constrained version, nu for maximum edge-disjoint triangle packing, and nu_star for maximum fractional triangle packing with edge capacities one. Put delta=nu_star-nu, B(n)=floor(n(n+1)/6).

The three different statements are:
A. For every eta>0 there is N_eta such that every chordal G of order n>=N_eta has cp(G)<=(1/6+eta)n^2.
B. There exist universal C,n0 such that every chordal G of order n>=n0 has cp(G)<=n^2/6+Cn (the frozen root).
C. Every chordal G has a same-order split H with cp(H)>=cp(G) (the transport obligation).
A does not close B or C. The sufficient strengthening delta(G)=O(n) for chordal graphs would imply B, not necessarily C.

C24 actually replays both different C23 checker sources through order seven, supplies a constructive O(n) gap under an explicit near-complete-split hypothesis, and disproves a uniform constant loss for an ARBITRARY simplicial-vertex step. It does not prove or disprove the global strengthening, B, or C. Neither the local execution nor this generator-authored proof is a trusted verifier receipt.

## 2. Re-derivation of the asymptotic interface

A partition with k triangles has m-3k single edges and cost m-2k. Conversely any edge-disjoint triangle packing extends by the unused single edges. Thus p23=m-2nu and cp<=p23. For fractional triangle weights z, the singleton weight must and can equal x_e=1-sum_(T containing e)z_T. Nonnegativity is exactly the packing capacity condition, and the cost is m-2sum_T z_T. Hence lambda=m-2nu_star and p23=lambda+2delta. These are identities on all simple graphs.

The finite equality LP min 1^T x, Ax=1, x>=0 is feasible using singleton edges and compact, since every variable belongs to an edge equality and is at most one. Giving each of h triangles weight 1/[2(h+1)] and supplying residual singleton weights gives a strictly positive feasible point. Finite LP strong duality and attainment, source S1, therefore yield lambda=max sum_e w_e, with signed real w_e<=1 and sum_(e in T)w_e<=1 for every triangle T. Equality, not a covering inequality, explains the signs. Every optimum also has w_e>=-1: clipping a smaller coordinate to -1 preserves all constraints (the other two triangle weights are at most one) and strictly improves the objective. The affine substitution q_e=(1-w_e)/2 gives the fractional triangle-cover dual; no integer integrality is inferred.

Here is the structural dependency, without assuming C22's conclusion. In a connected noncomplete chordal graph, an inclusion-minimal separator S of nonadjacent a,b is a clique. Otherwise two nonadjacent members of S have shortest paths between them through the a-component and the b-component of G-S. Minimality supplies their neighbors in both components. Those shortest paths form an induced cycle of length at least four, a contradiction. Strong induction on order now gives two nonadjacent simplicial vertices in a noncomplete chordal graph: use the smaller induced graphs consisting of S and each of these components; their simplicial pair cannot both lie in the clique S. Disconnected graphs use two components; complete graphs and order one are the base cases. Consequently, while vertices outside any fixed clique Q remain, there is a simplicial vertex outside Q. Delete it. Induced chordality and the retained clique are invariants, and the number outside Q strictly decreases. This proves a PEO ending in exactly Q, including nonmaximal Q and disconnected graphs.

For any optimum w in a nonempty chordal G, maximize M=sum_(a in S)w_ua over a vertex u and a clique S in N(u), allowing the empty set. The finite maximum is positive, since M=0 would force all edge weights nonpositive, whereas lambda>=m/3>0. Choose ANY maximizing pair and put r=|S|>=1,t=n-r>=1. A PEO ending in S counts each noncore edge once; every forward row has sum at most M. Thus lambda(G)<=w(E(S))+tM. Copying the weights w_ua to t mutually nonadjacent vertices joined to S gives a feasible signed dual on J(r,t)=K_r join I_t, so lambda(G)<=lambda(J(r,t)). This is a dual comparison, not cp-monotone edge completion.

For t>=r-1, give each mixed triangle weight 1/t and each crossing singleton weight 1-(r-1)/t. Edge loads are one and the cost is rt-binom(r,2). Crossing +1/core -1 is a matching dual. For 1<=t<r-1, r>=3: mixed triangles have weight 1/(r-1), core triangles [1-t/(r-1)]/(r-2). Again every edge load is one; the cost is [rt+binom(r,2)]/3, matched by w=1/3. Both formulas agree at t=r-1. The r=1 case is a star. Compression never has t=0; separately K_r has lambda=0 for r=0,1, lambda=1 for r=2, and binom(r,2)/3 for r>=3, using triangle weights 1/(r-2).

With t=n-r, g_n(r)=rt-binom(r,2)=(n+1/2)^2/6-(3/2)(r-(2n+1)/6)^2. Its integer values are <=B(n), because the fractional part of n(n+1)/6 is 0 or 1/3 and the extra term is only 1/24. The other split branch is at most n(n-1)/6<=B(n). Edgeless n=0,1 and the single edge n=2 are separate direct cases. Thus lambda(G)<=B(n) for every chordal G.

Source S2 states, for fixed K3 and each fixed epsilon>0, that there is N(epsilon) such that EVERY n-vertex graph with n>N has delta<epsilon*n^2. Its initial exclusion of isolated vertices is harmless: pair isolates by new edges, and attach an unpaired isolate by a pendant edge to a nonisolated vertex. This keeps n and the triangle list unchanged. Edgeless graphs have gap zero. The theorem counts original graph vertices, not auxiliary hypergraph vertices.

Let a(n)=max_(|V(F)|=n)delta(F), a finite maximum. S2 gives a(n)/n^2->0, uniformly over F. Thus cp(G)<=B(n)+2a(n)<=n^2/6+n/6+2a(n). Given eta>0, fix epsilon=eta/4, then require n>N(eta/4) and n>=1/(3eta). These two fixed-threshold conditions absorb both 2a(n) and n/6 into eta*n^2. No epsilon=1/n substitution occurs. This proves A relative to source-backed S1/S2, not B.

## 3. Simultaneous low-core audit

For any optimal w, any maximizing (u,S), and any PEO ending in S, let c_v denote a forward row. Define p_a=1-w_ua, P=r-M, h_ab=1-w_ua-w_ub-w_ab, R=sum h_ab, D=sum_(v outside S)(M-c_v), and theta=t-r+1. The edge, triangle, and maximum constraints give all these elementary slacks nonnegative. Summing core weights counts each p_a exactly r-1 times, so

    lambda=g_n(r)-theta*P-R-D,
    D=tM-lambda+w(E(S)).

The second identity makes total D independent of the compatible PEO. Removing negative entries from a forward-neighbor clique shows that its absolute negative weight is at most M-c_v.

Put s=B(n)-lambda>=0 and rho=(n+1/2)^2/6-B(n), equal to 1/24 or 3/8. Only when theta>=0 may we drop nonnegative terms in

    (3/2)(r-(2n+1)/6)^2+theta*P+R+D=s+rho.

This gives |r-(2n+1)/6|<=sqrt(2s/3+1/4) and theta*P+R+D<=s. In the dense branch t<r-1, the split formula instead gives s>=(n-1)/3+t(t-1)/6. Hence t<=1+sqrt(6s). Using the ACTUAL clique S once and all other edges singly gives cp<=rt+binom(t,2)+1<=n(1+sqrt(6s))+1. No residual chordality is used.

If integer near-extremizers satisfy cp(G_j)>=(1/6-e_j)n_j^2 with e_j->0 and n_j->infinity, then s_j<=e_j*n_j^2+2a(n_j)+n_j/6=o(n_j^2). The dense upper bound divided by n_j^2 tends to zero, contradicting this lower bound. The bound depends only on the graph's n,s, so it excludes ALL dense maximizing choices of ALL optimal duals simultaneously. The low-core bounds then imply r/n->1/3,t/n->2/3,theta/n->1/3,P/n->0,(R+D)/n^2->0 uniformly in those choices. This is not an edit-distance theorem.

A scope warning: low-core WITHOUT near-extremality is not a genuinely easier uniform-gap class. Given a nonempty chordal F on k vertices, add k isolates. Every maximizing S is still inside F, so r<=k-1 and t=2k-r>=r-1. Delta is unchanged. An O(n) gap bound for all such low-core graphs would therefore give an O(k) bound for all chordal F. Isolated-vertex padding cannot be used to claim that the global gap problem has already been reduced to an easy class.

## 4. Constructive linear gap for complete split graphs and controlled edits

Let r,t>=1 with t>=r-1. Every triangle of J(r,t) uses a core edge, so nu_star<=binom(r,2). The mixed-triangle weights 1/t attain this bound.

For even r, explicitly factor K_r into r-1 perfect matchings: set N=r-1 odd and label the vertices by Z_N and infinity. The class z contains {infinity,z} and {z+i,z-i}, 1<=i<=(N-1)/2. Each class is a matching, and every finite pair has its unique midpoint z modulo N. For odd r, apply this construction to K_(r+1) and delete the dummy vertex, obtaining r near-perfect matchings of size (r-1)/2. Assign different classes to different outside vertices and replace a core edge ab in class x by triangle xab. A matching prevents repeated crossing edges within a class; distinct classes use distinct outside vertices and disjoint core edges.

If r is even, or t>=r, this uses every core edge and delta(J)=0. The only uncovered case is odd r with t=r-1: omit one near-perfect matching, giving

    0<=delta(J(r,t))<=gamma(r,t),
    gamma=(r-1)/2 in this boundary case, and gamma=0 otherwise.   (L1)

The upper estimate need not be exact at the odd boundary. The cases r=1 and empty matching classes are direct.

Suppose a same-order G differs from this J in d_minus deleted and d_plus added edges. Discard from the displayed integer packing at most one triangle for each deleted edge. The surviving packing is valid in G, losing at most d_minus triangles. Conversely, from any fractional packing of G, remove all triangles using an added edge. Their total weight is at most d_plus by summing the capacity-one constraints. What remains is a feasible fractional packing of J. Consequently

    delta(G)<=gamma(r,t)+d_minus+d_plus.                       (L2)

This constructive comparison holds for any simple G. It does not claim that arbitrary completion is cp-monotone. Let d=d_minus+d_plus. If G is also chordal, Section 2 yields

    cp(G)<=B(n)+2gamma+2d<=B(n)+(n-1)/2+2d.                   (L3)

The last inequality uses r<= (n+1)/2 in the low-core branch. Therefore, for every fixed K, the explicit class d<=K*n obeys the root-scale bound n^2/6+(2K+2/3)n. No argument here shows that C23's weighted near-extremizer conditions imply d=O(n).

The rounding losses also add under a precisely delimited gluing operation. Build G from pieces G_i by successively identifying exactly one vertex with the previous union, with no other cross edges. Every triangle and every clique with an edge stays inside one piece, so nu,nu_star,cp all add. If each piece satisfies (L2), then delta(G)<=sum gamma_i+sum d_i. Since n-1=sum(n_i-1) and gamma_i<=(n_i-1)/4,

    delta(G)<=(n-1)/4+sum_i d_i.                              (L4)

This gives a linear-gap class of possibly non-split chordal graphs when sum_i d_i=O(n). The edge ownership is invariant during gluing and the finite number of pieces is the termination bound. Gluing along separators with edges is NOT covered: their capacities are shared and cannot be independently spent.

## 5. An exact small obstruction to constant-per-simplicial-vertex induction

Let H have core {0,1,2,3,4,5}, all its 15 edges, and two additional vertices: 6 adjacent to 0,4 and 7 adjacent to 1,3. Let G add vertex 8 adjacent to every core vertex and to neither 6 nor 7. Vertex 8 is simplicial. Both graphs are split. Every clique with an edge is either a subset of the core (including 8 in G) or one of the pin edges/triangles. The machine certificate lists all of them.

The exact values are

    H: (n,m,nu,nu_star,lambda,p23,cp)=(8,19,6,6,7,7,5),
    G: (n,m,nu,nu_star,lambda,p23,cp)=(9,25,7,25/3,25/3,11,5).

Thus delta(G)-delta(H)=4/3>1. This is the smallest example in the completely searched family of all subsets of the nine K_(3,3) pin edges, not a proved global minimum.

Here are proof certificates not dependent on solver trust. For H, the six edges 04,05,12,13,23,45 meet every triangle: the unselected core edges form K_(3,3) with sides {0,4,5} and {1,2,3}, and both pin triangles use a selected edge. Unit weights on these six edges give nu_star<=6. A six-triangle packing is in the finite certificate (or use both pin triangles and a parity decomposition of K_(2,2,2) on pairs {0,4},{1,3},{2,5}). Hence nu=nu_star=6.

For G, four core vertices have odd degree. Any triangle packing leaves at least two edges, so nu<=floor((25-2)/3)=7; the seven triangles 028,035,158,245,348,046,137 attain this (each string lists its three vertex labels). For a direct fractional certificate, use each pin triangle with weight one. In the remaining K7 minus the matching {04,13}, let A={0,1,3,4}, B={2,5,8}. Assign weight 1/3 to the triangle B; 1/6 to every triangle with one A and two B; and 1/3 to each valid triangle with two A and one B. The AA, AB, BB loads are respectively 3*(1/3), 2*(1/6)+2*(1/3), and 1/3+4*(1/6), all one. Thus all 25 edges are fractionally decomposed and nu_star=25/3.

For cp, the intact core plus four pin single edges gives five. A four-piece partition is impossible. With no pin triangle, four pin singles already leave the core uncovered. With one pin triangle, three pin pieces leave a noncomplete core for only one piece. With both pin triangles, the remaining core is K6 or K7 minus two disjoint edges. It cannot be partitioned into two cliques: two such edge-disjoint cliques intersect in at most one vertex and would make a disconnected graph or a graph with a cut vertex; this residual has neither. Hence cp=5 for both graphs.

## 6. No universal constant works: an explicit linear-sized jump

For h>=1 put m=3^h. There are m group labels, the vectors in F_3^h. For each label a take a pair a0,a1. Make all 2m core vertices mutually adjacent. Add m pins x_a adjacent only to a0,a1; call the graph H_m. Add v adjacent to all core vertices, but no pins, to get G_m. Both are split, and v is simplicial. Their orders are 3m and 3m+1, and edge counts are 2m^2+m and 2m^2+3m.

The affine lines {a,b,-a-b} form a Steiner triple system on the m labels: for two distinct points the third is distinct and unique. Lines parallel to the first coordinate form a partition into m/3 triples. No external design existence theorem is used.

First use all m pin triangles, consuming the m pair edges. For each affine line {a,b,c}, decompose the complete tripartite graph on the three pairs into four triangles (ai,bj,c(i xor j)), i,j in {0,1}. Pair uniqueness of the index lines makes these edge-disjoint and covers all other core edges. Thus H_m has a full triangle decomposition, with

    nu(H_m)=nu_star(H_m)=m(2m+1)/3.

To pack G_m, keep the pin triangles. Retain the four triangles for every line outside the selected parallel class. For a parallel triple {a,b,c}, put U=(a0,b0,c0), V=(b1,c1,a1). Replace its four triangles by the two triangles U,V and the three triangles (v,U_i,V_i). These five triangles use all six v-spokes in that block and all its cross-pair core edges except L={(a0,c1),(b0,a1),(c0,b1)}. Different parallel blocks use disjoint spokes; other affine lines use disjoint core-edge resources. The resulting packing leaves exactly m edges and has m(2m+2)/3 triangles.

All 2m core vertices of G_m have odd degree and every other vertex has even degree. Any triangle packing leaves a graph with the same degree parity, hence at least m unused edges. This proves the matching integer upper bound.

For a fractional certificate, give each pin triangle weight one, each triangle vxy with x,y from distinct core pairs weight beta=1/[2(m-1)], and each core triangle using three distinct pairs weight alpha=(2m-3)/[4(m-1)(m-2)]. A v-spoke has load 2(m-1)beta=1, and a cross-pair core edge has load beta+2(m-2)alpha=1. Pair edges and pin spokes are covered by pin triangles. All weights are nonnegative since m>=3. Therefore

    nu(G_m)=m(2m+2)/3,
    nu_star(G_m)=m(2m+3)/3,
    delta(G_m)-delta(H_m)=m/3=(|V(G_m)|-1)/9.              (F1)

No absolute per-step constant can bound this jump, even on split graphs. Nevertheless (F1) is LINEAR in total order and is not a counterexample to the global O(n) gap strengthening.

For completeness, cp(H_m)=cp(G_m)=2m+1. The intact core and all 2m pin spokes attain this. In any partition, let k pin triangles be used; the pin pieces cost 2m-k, and the residual core is a complete graph minus k disjoint edges. Such a residual needs at least k+1 clique pieces (one if k=0). To see this for k>=1, form the vertex-piece incidence matrix. For each missing pair take the difference of its two rows. These k nonzero differences are mutually orthogonal, since all cross-pair adjacencies are present. If the row-space dimension were only k, the two nonzero, mutually orthogonal rows of one missing pair would both lie on its one-dimensional difference direction, a contradiction. Thus the number of pieces is at least k+1. The residual vertices are nonisolated for the orders here. This proves the stated cp values.

A second, previously constructed resource-pinning family is retained in rounding-result.json: group the complete core into q triples and pin EVERY cross-group edge by a degree-two vertex. With F=9*binom(q,2), the base has nu=nu_star=cp=F+q. Adding a simplicial universal-to-core vertex gives nu=cp=F+q and nu_star=F+2q. Charge every triangle using a cross-group core edge to its capacity; the remaining triangle problem is q K3 blocks before and q K4 blocks afterward. Pin triangles and the standard K4 half-weight certificate attain the bounds. For cp use weight +1 on pin spokes, -1 on cross-group core edges, and 1/3 (before) or 1/6 (after) on each within-block edge: a core clique meeting j groups has weight at most j-binom(j,2)<=1. This yields another exact obstruction, checked at q=1,2. It does not imply failure of every possible leaf-bag selection rule.

## 7. Execution, limits, and the first remaining lemma

Both immutable C23 programs were actually run using Python 3.13.5, standard-library Fraction arithmetic and bounded processes. Both cover all 532 chordal isomorphism classes at orders 0 through 7; the main version also independently generates all 1,253 graph classes and rejects its 14 mutations, while the recovery version rejects 12. The accompanying run record freezes exact commands, code/output hashes, resources and exit codes. Sampled solver optima do not enumerate a continuous optimal face; Section 3 supplies the all-choice argument instead.

Additional exact runs verify the 55 low-core split constructions of total order at most 14, all 26 symmetry orbits of the 512 selected-pin inputs, full certificates for the 9-vertex example, and the constructive affine cases m=3,9,27. These support only their finite stated ranges; the all-order proofs are the explicit arguments above.

The first unresolved strengthening is: find a universal K such that every chordal G satisfying the C23 INTEGER near-extremizer assumptions has delta(G)<=K|V(G)|, without imposing the additional d=O(n) edit hypothesis of (L2). The generic low-core condition alone is equivalent in difficulty up to constants to the all-chordal problem by isolate padding. A root-sufficient alternative is to bound 2delta-[B(n)-lambda] by K*n. Neither estimate is proved here.

The excluded subroute is a uniformly constant loss for EVERY simplicial-vertex deletion, not the admitted split-extremal route. A valid replacement must choose and amortize steps or track separator edge resources; it cannot infer a per-vertex bound from the small-order table. The next atomic test is an explicit separator-capacity potential whose loss bound telescopes and is checked against (F1) and the pinned-triple family. No claim that this potential exists is made.

Sources S1/S2 are source-backed inputs, with locators and exact captured-excerpt hashes; original PDF-byte capture and trust-separated verifier/admission remain separately marked. Main's old claims and truth ledgers are unchanged. Status: NONTERMINAL_CHECKPOINT; no root closure, EvidenceLink, Result, or Solution admission.
