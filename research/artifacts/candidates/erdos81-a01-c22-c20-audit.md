# C22: adversarial re-derivation of C20's uniform asymptotic bound

Candidate ID: `candidate:erdos81-a01-c22-c20-audit`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Transport target: `obligation:erdos81-split-extremal-reduction`
Protected base: `4f2601d4b99669a46106a00c7262daf99691e69e`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Frozen audit scope and status

All graphs are finite and simple; isolated vertices are allowed. A clique piece has at least two vertices. Pieces may share vertices but their edge sets must be disjoint and have union E(G). An edgeless graph has partition number zero. A chordal graph has no induced cycle of length at least four.

The bounded target audited here is the explicitly WEAKER statement:
    for every eta>0 there is N_eta such that, for every n>=N_eta
    and every n-vertex chordal G, cp(G)<=(1/6+eta)*n^2.       (A)
Its negation would require a fixed eta>0 with arbitrarily large counterexamples. Neither an n-dependent eta nor a finite small-graph mismatch to another parameter is such a counterexample.

We also audit the necessary low-core conditions for sequences with
    n_j -> infinity, cp(G_j)>=(1/6-delta_j)*n_j^2,
    delta_j>=0, delta_j -> 0.                              (B)

This is a new proof-drafted, source-backed audit candidate, not a trust-separated verifier receipt. The current principal remains the candidate generator. No mathematical program, graph enumeration, LP solver, Lean, SMT or proof-assistant execution occurred. The tests in Section 10 are explicit hand-derived finite certificates, not exhaustive computation.

The argument below re-derives all graph-specific steps. Its external theorem inputs are finite LP strong duality with attainment (S1) and the fixed-triangle packing approximation (S2), identified in the source note. Their use is source-backed; their proofs are not formalized here. No new axiom or canonical obligation is admitted. The frozen linear-error root and exact same-order split domination remain open. There is no priority or best-published-bound claim.

## 2. Definitions and dependency audit

Write m=|E(G)| and B(n)=floor(n(n+1)/6).
- cp(G): minimum number of pieces in an exact edge partition into arbitrary cliques.
- p23(G): the same integer minimum when pieces are restricted to edges and triangles.
- lambda(G): minimum sum of nonnegative weights on edges and triangles, with total weight EXACTLY one on each graph edge.
- nu(G): maximum number of pairwise edge-disjoint triangles.
- nu_star(G): maximum sum of nonnegative triangle weights whose total on each edge is AT MOST one.

The inequality directions matter. A p23 partition is an allowed cp partition, so
    cp(G)<=p23(G).                                         (1)
There is no asserted ordering between cp and lambda.

The historical dependency paths, all fresh-read at the protected base unless stated otherwise, are:
- `research/artifacts/candidates/erdos81-a01-c20-asymptotic-rounding.md`: audited target, external packing interface, dense-branch implication and windmill.
- `research/artifacts/candidates/erdos81-a01-c18-fractional-compression.md`: packing identities, signed dual, compression and fractional split values.
- `research/artifacts/candidates/erdos81-a01-c19-dual-rigidity.md`: only its Section 2 slack identity and Section 6 dense bound are needed here. The last-bad-vertex lemma, exact extremizer classification and sharp unit gap are NOT inputs.
- C18's historical dependencies are `research/artifacts/candidates/erdos81-a01-c04-deficit-one.md` for the clique-suffix ordering and `research/artifacts/candidates/erdos81-a01-c01-core-obstructions.md` for the split benchmark. Section 4 below replaces the structural dependency by a proof from the chordal definition. Section 7 gives the lower benchmark directly; no unexamined C01 matching construction is needed for (A).
- C18/C20 source notes are `research/artifacts/source-notes/erdos81-a01-c18-lp-faithfulness.md` and `research/artifacts/source-notes/erdos81-a01-c20-packing-faithfulness.md`. Fresh source comparison is in `research/artifacts/source-notes/erdos81-a01-c22-primary-source-audit.md`.

Dependency chain of this candidate:
    definitions -> identities (2)-(4)
    chordal separator induction -> clique-suffix ordering
    S1 + signed compression + explicit split certificates -> lambda<=B
    S2 + isolate bridge + identities -> (A)
    (A)'s uniform packing error + exact slack + dense finite bound -> (B)'s conditions.
There is no appeal to CI, a merge, integer split domination, or chordality of an edge-deleted residual.

## 3. Exact packing identities and signed duality

If an integer edge/triangle partition uses k triangles, exactly m-3k edges remain as singleton pieces. Its cost is m-2k. Conversely any edge-disjoint triangle packing extends by those singleton edges. Taking extrema yields
    p23(G)=m-2*nu(G).                                     (2)

For a fractional triangle packing z, put
    x_e=1-sum_(T containing e) z_T.
The packing capacities say exactly x_e>=0. This gives a fractional edge/triangle partition. Conversely every such partition has these singleton weights. Its total cost is
    sum_T z_T + sum_e x_e = m-2*sum_T z_T.
Thus, in both directions,
    lambda(G)=m-2*nu_star(G),
    p23(G)=lambda(G)+2*(nu_star(G)-nu(G)).                 (3)
These statements require no chordality. Edgeless graphs satisfy them with all values zero.

All extrema exist: the integer feasible sets are finite, and the fractional packing polytope has every coordinate in [0,1]. For the partition LP, let A be the edge-versus-piece incidence matrix. Its form is
    min 1^T x, Ax=1, x>=0.
Singleton edges make it feasible. Each coordinate is at most one because every piece contains an edge, so the feasible set is compact. It even has a strictly positive feasible vector: if there are h triangles, assign each triangle 1/(2(h+1)) and assign each edge its positive unused capacity. The matrix contains the identity columns of the singleton edges.

Applying S1 with the explicitly checked finite, feasible and bounded hypotheses gives an attained signed dual:
    lambda(G)=max W, W=sum_e w_e,
    w_e<=1 for every edge,
    sum_(e in T) w_e<=1 for every triangle T.              (4)
The variables w_e are real and may be negative: primal edge constraints are equalities, not covering inequalities. Under the source convention the sign substitution is w=-v.

For later use, weak duality can be checked without S1:
    sum_e w_e=sum_C x_C*sum_(e in C)w_e<=sum_C x_C.
If m>0, summing the primal edge equalities gives m<=3*sum_C x_C, so lambda>=m/3>0.

## 4. A self-contained clique-suffix ordering lemma

Call a vertex simplicial when its neighbors form a clique. We prove by strong induction on graph order that every nonempty chordal graph is complete or has two nonadjacent simplicial vertices. A complete graph has simplicial vertices; order one is the base case.

For a disconnected graph, apply the induction hypothesis inside two distinct components to obtain a simplicial vertex in each. They are globally simplicial and nonadjacent. Each component is smaller and induced, hence chordal.

For a connected noncomplete graph choose nonadjacent vertices a,b and an inclusion-minimal separator S whose deletion separates them. Such a separator exists, since deleting all other vertices separates a,b. Let A and B be their components in G-S. Minimality implies every s in S has a neighbor in each of A and B. Indeed, in G-(S minus {s}) a path from a to b exists; it must go through s, and its segments before and after s enter the original components A and B.

The separator S is a clique. Otherwise take nonadjacent s,t in S. A shortest s-t path with internal vertices in A exists, as does one with internal vertices in B. Both have length at least two and are induced by shortestness. Their union is a cycle. There are no edges between A and B, no edge st, and no chords within either shortest path. Hence it is an induced cycle of length at least four, contradicting chordality.

The induced graph on A union S is smaller. If it is complete, any vertex in A is simplicial. Otherwise induction gives two nonadjacent simplicial vertices, not both in the clique S; choose one in A. Its neighbors in the full graph lie in A union S, so it is globally simplicial. Do the same in B. The two chosen vertices are nonadjacent. This proves the induction step and the assertion for every finite order.

Now let Q be any specified clique in a chordal graph. While a vertex outside Q remains, there is a simplicial vertex outside Q: if the current graph is complete choose any outside vertex; otherwise two nonadjacent simplicial vertices cannot both belong to Q. Delete an outside simplicial vertex and repeat. The invariant is that the current graph is induced and chordal and Q remains a clique. The nonnegative integer number of vertices outside Q decreases by one each step. At termination only Q remains, and its vertices can be ordered arbitrarily.

The resulting ordering is a perfect elimination ordering (PEO), meaning the later neighbors of each vertex form a clique, and it ends in precisely Q. This handles disconnected graphs and arbitrary, not necessarily maximal, cliques. It uses vertex deletion, not the unsafe assertion that arbitrary edge deletion preserves chordality.

## 5. Signed-neighborhood compression

Let G be a nonempty chordal graph and choose an optimal dual w in (4). Define
    M=max_(u,S) sum_(a in S)w_(ua),                       (5)
where u is a vertex and S is any clique contained in its neighborhood, including the empty set. The maximum is over finitely many choices and is attained. It is nonnegative. If M=0, choosing S as a singleton shows every edge weight is nonpositive, so W<=0, contradicting lambda>0. Thus M>0.

Fix an attaining pair u,S. Put r=|S|>=1, t=n-r>=1. The quantity r is the size of a WEIGHT-SELECTED clique, not omega(G). Choose a PEO ending in S by Section 4. For every vertex v outside S, write c_v for the sum of weights on its edges to later neighbors. Those later neighbors form a clique, so c_v<=M by (5). Each edge outside E(S) is counted exactly once, at its earlier endpoint:
    W=w(E(S))+sum_(v outside S)c_v<=w(E(S))+tM.           (6)

Form J(r,t), with core S and t mutually nonadjacent vertices each joined to all of S. Keep core weights w_ab, and give every crossing edge to a the weight w_ua. Every mixed triangle maps to the original triangle uab; core triangles are unchanged. The copied weights satisfy (4) on J(r,t). Their total is w(E(S))+tM. Weak duality there gives
    lambda(G)<=lambda(J(r,t)).                            (7)
This bounds a dual objective. It is not a graph transformation claimed monotone for integer cp.

## 6. Complete-split fractional certificates and optimization

For r,t>=1 the following are exact values:
    lambda(J(r,t))=rt-binom(r,2),              t>=r-1;
    lambda(J(r,t))=[rt+binom(r,2)]/3,          1<=t<r-1.   (8)

In the first branch assign every mixed triangle weight 1/t. Each core edge gets total one; each crossing edge gets (r-1)/t. Add crossing singleton weight 1-(r-1)/t, which is nonnegative. The cost is rt-binom(r,2). The dual assigning crossing weights +1 and core weights -1 matches: mixed triangle weight is one and core triangle weight is -3. When r=1 there are no triangles and this is just the t edges of a star.

In the second branch r>=3. Assign mixed triangles weight 1/(r-1). Each crossing edge gets one and each core edge gets t/(r-1). Assign every core triangle weight [1-t/(r-1)]/(r-2). This is nonnegative, and each core edge occurs in r-2 such triangles. Therefore all edge loads are exactly one. Only triangles are used, so the cost is the edge count divided by three. The constant dual w_e=1/3 matches. The two expressions agree at t=r-1.

For the first branch, with t=n-r, put
    g_n(r)=rn-3r^2/2+r/2
          =(n+1/2)^2/6-(3/2)*(r-(2n+1)/6)^2.            (9)
The quantity g_n(r) is an integer. Also
    (n+1/2)^2/6=n(n+1)/6+1/24.
The fractional part of n(n+1)/6 is either zero or 1/3, according as n modulo three is not one or is one. Thus the right side is less than B(n)+1. It follows that g_n(r)<=B(n).

In the second branch (8) is at most n(n-1)/6. For n>=2,
    B(n)-n(n-1)/6 >= (n-1)/3 >= 0,                       (10)
using B(n)>=n(n+1)/6-1/3. With (7) this proves
    lambda(G)<=B(n) for every n-vertex chordal G.          (11)
For edgeless graphs, including n=0 and n=1, the assertion is direct. A nonempty graph always had r,t>=1, so no t=0 denominator was used.

## 7. Original-source interface and uniform integer bound

Input S2 is the fixed K3 specialization of Yuster's Theorem 1.2, with its explicit quantifiers at the start of Section 3:
    for every epsilon>0 there exists N(epsilon) such that,
    for every n>N(epsilon) and every n-vertex simple graph
    in the source's domain, nu_star(G)-nu(G)<epsilon*n^2. (12)
The source initially excludes isolated vertices. Its n counts ORIGINAL graph vertices. This is not the order of its later auxiliary hypergraph. The source note gives exact page locators and the fixed-pattern comparison.

Here is the domain bridge. If G has an edge, pair its isolated vertices and add an edge within each pair; if one isolate remains, attach it by a pendant edge to a nonisolated vertex. This removes all isolates without changing n or creating any triangle. The triangle list and all its edge capacities are unchanged, so both nu and nu_star are unchanged. If G is edgeless its packing gap is already zero. Thus (12) extends to every finite simple graph. The new graph need not be chordal, since S2 does not require chordality.

Let
    a(n)=max_(G on vertex set {1,...,n}) (nu_star(G)-nu(G)).
There are finitely many labeled graphs, and their optima exist; a(n)>=0. The quantifiers in (12) give a(n)/n^2 -> 0. Consequently (1), (3) and (11) imply uniformly on chordal graphs
    cp(G)<=p23(G)<=B(n)+2a(n)
         <=n^2/6+n/6+2a(n).                              (13)
This supplies a single error function e(n)=n/6+2a(n) with e(n)/n^2 -> 0.

An explicit quantifier proof of (A) is useful. Fix eta>0 and set epsilon=eta/4, a constant. For
    n>N(eta/4) and n>=1/(3eta),
we have 2a(n)<eta*n^2/2 and n/6<=eta*n^2/2. Equation (13) gives cp(G)<=(1/6+eta)*n^2 for every chordal G of that order. Increase the integer threshold if necessary. No substitution epsilon=1/n occurs, and no numerical cutoff or linear remainder has been inferred.

The leading coefficient cannot be reduced using a universal smaller constant. For n>=2 set r0=floor((n+1)/3), t0=n-r0. Then t0>=r0. Directly evaluating g_n(r0) in the three residues gives B(n). The crossing +1/core -1 weights used above satisfy ALL clique inequalities: a clique with j core vertices and one outside vertex has total j-binom(j,2)<=1, and core-only cliques have nonpositive total. Summing these weights over an arbitrary integer clique partition proves cp(J(r0,t0))>=B(n). These split graphs are chordal by eliminating their outside vertices first. Hence both split and chordal integer extrema, divided by n^2, tend to 1/6 using (13). This does not prove equality of those two integer extrema at fixed n.

## 8. Exact low-core slack, including all signs

Keep an optimal lambda-dual w, an arbitrary maximizing pair u,S in (5), and an arbitrary PEO ending in S. Define
    p_a=1-w_(ua),                         a in S;
    P=sum_a p_a=r-M;
    h_ab=1-w_(ua)-w_(ub)-w_(ab)
        =-1+p_a+p_b-w_(ab),               ab in E(S);
    R=sum_ab h_ab;
    a_v=M-c_v,                           v outside S;
    D=sum_v a_v;
    theta=t-r+1=n-2r+1.                                  (14)
All p_a,h_ab,a_v, and therefore P,R,D, are nonnegative. The reasons are respectively the edge upper bounds, the triangle uab constraint, and the definition of M. Dropping a negative summand from S would improve (5), so w_ua>=0 as well; this extra property is not needed for the identity.

Every p_a occurs r-1 times when summing over core pairs. Thus
    w(E(S))=-binom(r,2)+(r-1)P-R,
    sum_v c_v=t(r-P)-D.
Adding gives the EXACT identity
    lambda(G)=W=g_n(r)-theta*P-R-D.                       (15)

The negative forward weights are also controlled. In one forward row, remove all neighbors whose edge weight is negative. The remaining subset is a clique; its weight sum is at most M. If L_v is the absolute sum of negative weights in that row, then
    L_v<=M-c_v=a_v.
Each noncore edge occurs in one forward row, so the absolute total of negative noncore weights is at most D. No assertion that all noncore weights are positive is required.

Put s=B(n)-lambda(G)>=0. In the LOW-CORE branch t>=r-1, theta>=0 and (15) yields
    B(n)-g_n(r)<=s,
    theta*P+R+D=s-[B(n)-g_n(r)]<=s.                      (16)
When theta>0 this includes P<=s/theta; in all low-core cases R+D<=s. Define
    rho_n=(n+1/2)^2/6-B(n),
which is 1/24 for n congruent to zero or two modulo three and 3/8 otherwise. Equations (9) and (15) give
    (3/2)*(r-(2n+1)/6)^2+theta*P+R+D=s+rho_n.            (17)
Hence, only in the low-core branch,
    |r-(2n+1)/6|<=sqrt(2s/3+1/4).                         (18)
P,R,D are nonnegative even in the dense branch, but theta*P need not be. It is invalid to drop that term when theta<0.

## 9. Dense-branch exclusion and arbitrary-choice quantifiers

In the DENSE branch t<r-1, equations (7)-(8) give
    lambda(G)<=[binom(n,2)-binom(t,2)]/3.
Together with (10), this implies
    s>=B(n)-n(n-1)/6+t(t-1)/6
     >=(n-1)/3+t(t-1)/6.                                (19)
In particular t(t-1)<=6s, so t<=1+sqrt(6s).

The actual set S is a clique in G. Use it once and use all other edges singly. In this branch r>=3, so that piece is nonempty. The resulting integer partition gives
    cp(G)<=m-binom(r,2)+1
         <=rt+binom(t,2)+1
         <=nt+1
         <=n*(1+sqrt(6s))+1.                             (20)
No property of the edge-deleted residual was used; its remaining edges were taken singly.

Now assume (B). From (3) and the uniform error a(n),
    lambda(G_j)>=cp(G_j)-2a(n_j).
With (11) and B(n)<=n^2/6+n/6, we get
    0<=s_j<=delta_j*n_j^2+2a(n_j)+n_j/6=o(n_j^2).         (21)

If dense compression choices existed for infinitely many indices, choose one at each such index. Equation (19) forces t_j=o(n_j), and (20) then forces cp(G_j)=o(n_j^2) on that subsequence. This contradicts (B), whose normalized lower bound tends to 1/6. Thus, eventually, EVERY optimal dual and EVERY maximizing weighted-neighborhood pair use the low-core branch. This argument does not require uniqueness or a consistent choice rule.

For any such choices, and any compatible PEO, (18), (21), and (16) imply
    r_j=n_j/3+o(n_j),
    t_j=2n_j/3+o(n_j),
    theta_j=n_j/3+o(n_j)>0 eventually,
    P_j<=s_j/theta_j=o(n_j),
    R_j+D_j<=s_j=o(n_j^2).                              (22)
These are necessary conditions on the chosen optimal lambda-dual and ordering. They are not conclusions about omega(G), edit distance to a split graph, sufficiency for being near-extremal, or extremizers of the all-clique fractional parameter.

## 10. Exact finite pressure tests

All entries below are hand-derived, with certificates provided next. They test the definitions and branch guards rather than replace the universal proof.

| Graph | m | nu | nu_star | lambda | p23 | cp |
|---|---:|---:|---:|---:|---:|---:|
| Edgeless graph | 0 | 0 | 0 | 0 | 0 | 0 |
| Forest with m edges | m | 0 | 0 | m | m | m |
| K3 | 3 | 1 | 1 | 1 | 1 | 1 |
| K4 | 6 | 1 | 2 | 2 | 4 | 1 |
| K4 minus edge 34 | 5 | 1 | 1 | 3 | 3 | 3 |
| J(3,2) | 9 | 2 | 3 | 3 | 5 | 4 |
| Square of path P6 | 9 | 2 | 2 | 5 | 5 | 5 |
| k copies of K4 meeting in one vertex | 6k | k | 2k | 2k | 4k | k |

A forest has no triangle and its only nonempty-edge cliques are its edges. A tree is chordal because it has no cycle. Adding isolates changes no row in the table. For K3 use its single triangle with weight one.

For K4, all six pairs are edges; all four triples are triangles; the full vertex set is its one four-clique. Any two distinct triangles share an edge. Thus nu=1; putting weight 1/2 on each triangle gives nu_star=2, with upper bound m/3=2. An integer triangle plus the three unused edges gives p23=4, whereas the full K4 gives cp=1.

For the diamond K4-34, the edges are 12,13,23,14,24 and the triangles are exactly 123,124. They share 12, so both packing optima equal one. The partition {123,14,24} costs three, and there is no larger clique. A clique COVER of size two exists using both triangles, but it repeats edge 12 and is not a partition. This is a definition guard, not a counterexample to (A).

For J(3,2), use core 123 and outside vertices 4,5. The edges are 12,13,23,14,24,34,15,25,35. The triangles are exactly 123,124,134,234,125,135,235; the only four-cliques are 1234 and 1235. All other nonempty-edge cliques have just been listed. The packing {124,135} has size two. No larger packing exists: using 123 excludes every mixed triangle; otherwise each outside vertex occurs in at most one packed triangle, since two core pairs in a three-set meet. Assign weight 1/2 to each of the six mixed triangles to obtain nu_star=3; m/3 is a matching upper bound. The partition {1234,15,25,35} gives cp<=4. Any partition with a four-clique needs its three remaining star edges separately; without a four-clique a three-piece partition would require three triangles, already excluded. Thus cp=4, lambda=3 and p23=5. In particular neither cp<=lambda nor cp=lambda+2*(nu_star-nu) holds universally.

For P6 squared, use vertices 1,...,6 and join pairs at distance one or two in the path. The edges are 12,13,23,24,34,35,45,46,56. Its triangles are exactly 123,234,345,456; there is no four-clique. The ordering 1,...,6 is a PEO. Vertices {1,2,5,6} induce 2K2, impossible in a split graph: a clique side must meet both disjoint edges and would introduce an extra edge. Thus this is a non-split chordal test. The packing {123,456} has size two. Any fractional packing satisfies z123+z234<=1 from edge 23 and z345+z456<=1 from edge 45, so nu_star<=2. Those two triangles and singleton edges 24,34,35 give the five-piece optimum.

There is an explicit signed-slack test on this same non-split graph. Give edges 23 and 45 weight -1 and all other edges weight +1. Every triangle has weight one and W=5=lambda. Every vertex has at most two vertices in a clique inside its neighborhood, so M<=2; the pair u=1,S={2,3} attains M=2. The PEO 6,5,4,1,2,3 ends at S. Its outside forward sums are respectively 2,0,2,2. Hence
    r=2, t=4, theta=3, P=0, R=0, D=2,
    g_6(2)=7, s=B(6)-lambda=2.
Equations (15)-(17) give 5=7-2 and 2+1/24=2+rho_6 exactly, including a negative forward edge.

For the K4 windmill, each block consists of the common vertex c and its own private triple. Every nonempty-edge clique is a subset of one of these four-sets; triangles and edges cannot span two blocks. The graph is chordal, since a simple cycle cannot move between blocks without revisiting c. Integer and fractional edge packings, and clique partitions, add over blocks; the K4 certificate therefore gives the table. For k>=2 two private edges in different blocks induce 2K2, so the example is non-split. The gap nu_star-nu=(n-1)/3 is linear while cp=(n-1)/3 is small.

For all complete graphs K_n with n>=3, assigning every triangle weight 1/(n-2) covers each edge once, so lambda=binom(n,2)/3 and nu_star=binom(n,2)/3; constant dual 1/3 certifies lambda. Yet cp=1. We do not assume a formula for the integer triangle-packing optimum at arbitrary n; p23=m-2nu remains exact. The cases n=1,2 are respectively edgeless and a single edge, with no division by n-2.

Two additional negative controls delimit the universal lemmas. If chordality is dropped, C4 has only its four edges as nonempty-edge cliques, no triangles, and lambda=cp=4>B(4)=3. It is outside the domain of (11). If the low-core sign guard is dropped, take K4 with dual weights 1/3 and S any three vertices, u the fourth. Then r=3,t=1,theta=-1,P=2,R=D=0,W=2,g_4(3)=0,s=1. Identity (15) holds, but (18) would compare squared quantities 9/4 and 11/12 and is false. This is not a failure of (18) under its stated hypothesis.

No tested on-domain identity or C20 implication was contradicted. That finite observation is separate from the proof in Sections 3-9.

## 11. Audit closure, caveats and reproducibility

The five requested checks have explicit proof components:
1. cp<=p23, both packing identities and lambda<=B: Sections 3-6.
2. Original fixed-K3, graph-order, uniform-epsilon and isolated-vertex comparison: Section 7 and the source note.
3. Uniform little-o with a fixed eta and epsilon=eta/4: Section 7.
4. Every sign and parameter in the dense/low-core implication, including all choices: Sections 8-9.
5. Forests, complete graphs, windmills and a non-split chordal graph: Section 10.

Reproduction without a mathematical program consists of checking the displayed partitions and capacity sums; the separator induction; the edge ownership in the PEO sum; the rational loads in (8); the integer floor in (9)-(10); and the finite inequalities (15)-(21). Inspect S1 and S2 at the locators in the source note. The theorem-existence steps use LP duality and S2; no implementability, practical runtime, numerical cutoff, or executed construction algorithm is claimed.

Reasoning-discipline audit:
- Definitions, domains, quantifier order, weaker scope and negation: explicit in Sections 1-3.
- Dependency graph: acyclic chain in Section 2, with source-backed inputs named.
- Witnesses and exact coverage: primal/dual certificates in Sections 3, 6, 7, 10.
- Induction: Section 4 uses all smaller orders and proves the step; finite tests are not its substitute.
- Invariants and termination: induced chordality and retained clique; strictly decreasing outside-vertex count.
- Extremal existence: finite neighborhood choices and finite graph sets; compact fractional polytopes.
- Symmetry: uniform weights justified by actual edge multiplicities, not an assumed integer symmetric optimum.
- Probability: no probabilistic computation; S2 is imported only as an existence theorem with fixed parameters.
- Scale and signs: graph vertex count, isolates, n=0,1,2, r=1, t=r-1, theta=0, negative dual weights and subsequences checked.
- Verification boundary: proof-drafted/source-backed only; separate trusted review and any formal validation remain pending.

Remaining caveats: S2 gives o(n^2), not O(n). Equation (22) concerns integer near-extremizers and lambda-duals, not arbitrary fractionally near-extremal graphs. It gives necessary, not sufficient, conditions and no graph edit-distance estimate. An O(n) rounding theorem would be additional research. The exact split-domination obligation is stronger than the approximate comparison proved here.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: this expanded proof of (A) and (22), with explicit source-backed dependencies.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
failed_routes: canonical ledger unchanged; the outside-domain and parameter-confusion controls are not failures of the admitted route.
next_action: submit this frozen audit and source comparison for trust-separated mathematical/semantic review; any subsequent linear-rounding work must retain the slack s and its branch conditions.
