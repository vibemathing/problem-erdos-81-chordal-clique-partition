# C23: C22 admission audit, whole optimal-face guards, and exact replay request

Candidate ID: `candidate:erdos81-a01-c23-admission-audit`
Repository: `vibemathing/problem-erdos-81-chordal-clique-partition`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Transport obligation: `obligation:erdos81-split-extremal-reduction`
Base: `168492ce3df8528240507deee4cbc961317c8b72`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Exact scope, dependencies, and acceptance boundary

The audited mathematical statement is:
For every real eta>0 there exists an integer N_eta such that for every n>=N_eta and every finite simple chordal graph G with n vertices, cp(G)<=(1/6+eta)n^2.

A second audited implication concerns any sequence n_j tending to infinity with cp(G_j)>=(1/6-delta_j)n_j^2, where delta_j>=0 tends to zero. It asserts the simultaneous-in-choice dual necessary conditions in Section 6. It does not assert an O(n) remainder or exact same-order split domination.

All graphs allow isolated vertices. A clique piece has a nonempty edge set. Different pieces may share vertices, but every edge belongs to exactly one piece. All five parameters on an edgeless graph are zero. Chordal means no induced cycle of length at least four. Put m=|E(G)| and B(n)=floor(n(n+1)/6).

Historical inputs freshly read at the base are C18 (fractional compression), C19 (dual slack), C20 (asymptotic rounding), C21 (fractional variants), C22 (previous audit), and their primary-source notes. Their conclusions are NOT premises in the proof below. Graph-specific steps are re-derived. The only imported theorem inputs are:
S1: finite LP strong duality and attainment, with the strict-feasibility hypotheses verified below.
S2: the fixed-triangle specialization of Yuster's graph-packing theorem with its uniform quantifiers.
The source note and bounded source capture give original-body locators. These inputs are source-backed, not formal verification receipts. C19's last-bad-vertex or extremizer-classification claims are not needed.

The mathematical dependency chain is: definitions -> exact packing identities; chordal separator induction -> prescribed-clique-suffix ordering; S1 -> optimal signed dual; compression + explicit split certificates -> fractional bound; S2 + isolate bridge + exact identities -> uniform asymptotic bound; fractional bound + source error + signed slack + dense integer partition -> simultaneous necessary conditions.

The acting principal is still the generator. This document is a written adversarial audit candidate, not trust-separated verification. The exact checker is newly authored and syntax-parsed only. No mathematical algorithm or finite enumeration was executed in this Web lane, whose current profile has command_execution=false. The admission request is pending; the root and transport obligation stay open.

## 2. Exact integer and fractional interfaces

Define p23 as the minimum exact edge partition cost using only edges and triangles. Every such partition is a permissible arbitrary-clique partition, hence cp<=p23. Define nu as maximum cardinality of an edge-disjoint triangle packing. A p23 partition with k triangles leaves exactly m-3k single edges and costs m-2k. Conversely any such packing extends by every unused edge. Therefore
    p23=m-2nu.                                                    (1)

Let nu_star maximize the sum of nonnegative triangle weights z_T with load at most one on every edge. Let lambda minimize the sum of nonnegative weights on edges and triangles with edge load exactly one. The mutually inverse transformations are
    x_T=z_T, x_e=1-sum_(T containing e)z_T.
Their costs satisfy sum_T x_T+sum_e x_e=m-2sum_T z_T. Consequently
    lambda=m-2nu_star,
    cp<=p23=lambda+2(nu_star-nu).                                 (2)
No chordality is needed for these identities. Neither cp=lambda nor cp=p23 is inferred.

For nonempty graphs the equality LP is min 1^T x subject to Ax=1, x>=0, where A is the edge-versus-piece incidence matrix. Single-edge columns form an identity matrix and give feasibility. Every variable is at most one; hence a minimum exists on a compact polytope. If h triangles exist, assigning each triangle alpha=1/[2(h+1)] and giving every edge its remaining load makes every coordinate positive. S1 therefore applies with a finite optimum, and gives an attained dual
    lambda=max W, W=sum_e w_e,
    w_e<=1, sum_(e in T)w_e<=1 for each triangle T.                (3)
The variables w_e are signed real numbers because primal edge constraints are equalities. In the source's convention the substitution is w=-v. Weak duality follows directly from
    sum_e w_e=sum_C x_C sum_(e in C)w_e<=sum_C x_C.
Also lambda>=m/3>0, by summing edge loads.

### New audit guard: the entire optimal face is compact
Every optimal w in (3) satisfies -1<=w_e<=1. If w_e<-1, raising just this coordinate to -1 preserves every triangle constraint: the other two coordinates are each at most one. It also preserves the edge constraint but strictly raises W, a contradiction. Thus this applies to EVERY optimum, not a convenient selected one. The optimal face is closed and lies in a compact box.

The affine transformation q_e=(1-w_e)/2 identifies (3) with the triangle-packing dual min sum_e q_e, q>=0, sum_(e in T)q_e>=1. Its objective is (m-W)/2. At every optimum q_e<=1 by the same clipping argument. This is an algebraic correspondence, not a replacement for exact certificate validation by the two different LP implementations.

## 3. A prescribed clique is a PEO suffix

We prove by strong induction on order that every nonempty chordal graph is complete or has two nonadjacent simplicial vertices. A vertex is simplicial if its neighborhood is a clique. The one-vertex case is complete. If the graph is disconnected, select a simplicial vertex from each of two smaller components using induction; they are globally simplicial and nonadjacent.

For the connected noncomplete case, choose nonadjacent a,b and an inclusion-minimal separating set S disjoint from them. Let A and B be their components after deleting S. Every s in S has neighbors in both A and B: otherwise S minus {s} would still separate a,b, as is also seen from a simple a-b path after restoring s. If nonadjacent s,t belonged to S, shortest s-t paths internally in A and internally in B would form an induced cycle of length at least four. Each path is chordless by shortestness, the interiors have no cross edges, and st is absent. Thus S is a clique.

The induced graphs on A union S and B union S are smaller and chordal. If either is complete, choose any vertex from its component. Otherwise two nonadjacent simplicial vertices supplied by induction cannot both lie in S, so choose one outside S. All neighbors of that vertex in the full graph lie in the same component union S, so it is globally simplicial. Choices in A and B are nonadjacent. This completes the induction for every order.

For an arbitrary retained clique Q, whenever vertices outside Q remain, a simplicial vertex outside Q exists: in a complete residual choose any outside vertex; otherwise the nonadjacent simplicial pair cannot both lie in Q. Delete that vertex. The residual remains induced and chordal and Q remains intact. The integer number of outside vertices strictly decreases, so the process terminates at Q. Ordering Q arbitrarily then gives a perfect elimination ordering (PEO) ending in exactly Q. This includes empty Q and disconnected graphs. No edge-deletion chordality claim is used.

## 4. Signed compression and complete-split certificates

Take a nonempty chordal G and ANY optimal w from (3). Maximize
    M=max_(u,S clique contained in N(u)) sum_(a in S)w_ua,
allowing the empty S. This is a maximum of finitely many real numbers. If M=0, singleton choices imply all edge weights are nonpositive, contradicting lambda>0. Thus any maximizing pair has r=|S|>=1 and t=n-r>=1, since u is outside S.

Choose any PEO ending in S. Every outside forward row c_v is the weight sum to a clique in N(v), so c_v<=M. Each noncore edge occurs exactly once in these rows. Therefore
    lambda=w(E(S))+sum_v c_v<=w(E(S))+tM.                         (4)
On J(r,t)=K_r joined to t pairwise nonadjacent vertices, keep the core weights and copy w_ua as the crossing weight to a from each outside vertex. Each mixed triangle corresponds to uab in G and every core constraint is unchanged. This is a feasible signed dual on J, so weak duality gives
    lambda(G)<=lambda(J(r,t)).                                   (5)
Here r is weight-selected, not the maximum clique number of G.

For r,t>=1 the exact split values are
    lambda(J(r,t))=rt-binom(r,2)           when t>=r-1,
    lambda(J(r,t))=[rt+binom(r,2)]/3       when 1<=t<r-1.          (6)
In the first branch put weight 1/t on every mixed triangle. Core edges receive one; crossing edges receive (r-1)/t. Add crossing singleton weight 1-(r-1)/t. The objective is rt-binom(r,2). Crossing +1 and core -1 certify the same value by (3).
In the second branch r>=3: mixed triangles have weight 1/(r-1), core triangles [1-t/(r-1)]/(r-2). Their loads are exactly one on each edge. All pieces are triangles, giving m/3; dual w=1/3 matches. Both formulas agree at t=r-1.

Boundary audit: r=1,t>=1 is a star with no triangles and value t. r=2,t=1 agrees with K3. Compression never uses t=0. Separately, J(r,0)=K_r has value zero for r=0,1, one for r=2, and binom(r,2)/3 for r>=3, by giving every triangle weight 1/(r-2). Edgeless graphs, including n=0,1, are direct.

Let g_n(r)=r(n-r)-binom(r,2). Then
    g_n(r)=(n+1/2)^2/6-(3/2)(r-(2n+1)/6)^2.                    (7)
It is an integer. The fractional part of n(n+1)/6 is either zero or 1/3; hence (n+1/2)^2/6=n(n+1)/6+1/24<B(n)+1. Thus g_n(r)<=B(n). The second branch of (6) is at most n(n-1)/6, and
    B(n)-n(n-1)/6 >= (n-1)/3 >=0 for n>=1.
Equations (5)-(7), with the empty cases, prove
    lambda(G)<=B(n) for all finite simple chordal G.              (8)

## 5. Source quantifiers and uniform integer asymptotics

S2, with F fixed as {K3}, says: for every epsilon>0 there exists N(epsilon) such that for all n>N(epsilon) and all n-vertex graphs in its domain,
    nu_star(G)-nu(G)<epsilon*n^2.
The source's n counts original graph vertices, not auxiliary hypergraph vertices. Its graph convention excludes isolates. If G has an edge, pair its isolated vertices by new edges; if one isolate remains, attach it by a pendant edge to a nonisolated vertex. This preserves n and creates no triangles. The old triangle list and all relevant capacities are unchanged; both packing numbers are preserved. If G is edgeless the gap is zero. S2 therefore extends to all finite simple graphs; no chordality of the modified graph is needed.

Let a(n) be the maximum packing gap over all labeled n-vertex graphs, and a(0)=0. Finiteness of the graph set and compactness of each fractional polytope give a well-defined nonnegative maximum. The source's quantifier order gives a(n)/n^2 ->0, uniformly in the graph. Thus (2),(8) give
    cp(G)<=B(n)+2a(n)<=n^2/6+n/6+2a(n).                          (9)
Fix eta>0 and use epsilon=eta/4, independent of n. For n>N(eta/4) and n>=1/(3eta), both 2a(n)<eta*n^2/2 and n/6<=eta*n^2/2 hold. Enlarging to an integer threshold proves the statement in Section 1. This does not use epsilon=1/n, exchange limits, supply a quantitative cutoff, or upgrade the error to O(n).

## 6. All optimal duals and all maximizers: explicit uniform bounds

For ANY optimal w, ANY global maximizer (u,S), and ANY compatible PEO, define
    r=|S|, t=n-r, theta=t-r+1=n-2r+1;
    p_a=1-w_ua, P=sum_a p_a=r-M;
    h_ab=1-w_ua-w_ub-w_ab, R=sum_(ab in E(S))h_ab;
    a_v=M-c_v, D=sum_(v outside S)a_v.
Each of p_a,h_ab,a_v is nonnegative by respectively edge constraints, triangle constraints, and the global maximum. Summing core pairs counts every p_a exactly r-1 times, giving
    w(E(S))=-binom(r,2)+(r-1)P-R.
Outside rows sum to t(r-P)-D. Therefore
    lambda=g_n(r)-theta*P-R-D.                                 (10)
The aggregate D=tM-lambda+w(E(S)) does not depend on the compatible PEO, though individual row deficits can. In any row, deleting negative summands leaves a clique whose total is <=M; consequently the absolute negative mass in that row is <=a_v.

Put s=B(n)-lambda>=0. If t>=r-1, all terms theta*P,R,D are nonnegative and
    theta*P+R+D<=s,
    (3/2)(r-(2n+1)/6)^2+theta*P+R+D=s+rho_n,                   (11)
where rho_n is 1/24 for n=0,2 modulo 3 and 3/8 otherwise. Set
    A(n,s)=sqrt(2s/3+1/4), L(n,s)=(n+2)/3-2A(n,s).
Simultaneously for every low-core choice,
    |r-(2n+1)/6|<=A(n,s), R+D<=s, theta>=L(n,s);
and if L(n,s)>0, P<=s/L(n,s). These bounds depend only on n,s, not a selected optimum or maximizer.

For a dense choice t<r-1, (5)-(6) instead imply
    s>=B(n)-n(n-1)/6+t(t-1)/6
     >=(n-1)/3+t(t-1)/6,
so t<=1+sqrt(6s). Since S is an actual clique (r>=3 here), use it once and every remaining edge singly:
    cp(G)<=m-binom(r,2)+1<=rt+binom(t,2)+1
         <=nt+1<=n(1+sqrt(6s))+1.                              (12)
No residual chordality assumption occurs. In particular, the graph-level condition
    cp(G)>n(1+sqrt(6s))+1                                      (13)
excludes EVERY dense maximizer of EVERY optimal signed dual at once.

For the near-extremizer sequence in Section 1, equations (2),(8),(9) imply
    0<=s_j<=delta_j*n_j^2+2a(n_j)+n_j/6=o(n_j^2).
The right side of (12), divided by n_j^2, tends to zero, whereas the assumed lower bound tends to 1/6. Thus (13) eventually holds. Every choice is then low-core, A(n_j,s_j)=o(n_j), L(n_j,s_j)=n_j/3+o(n_j)>0, and the simultaneous bounds give
    r_j=n_j/3+o(n_j), t_j=2n_j/3+o(n_j),
    theta_j=n_j/3+o(n_j), P_j=o(n_j), R_j+D_j=o(n_j^2).          (14)
Equivalently, the suprema of the normalized errors over ALL these choices tend to zero. Compactness of the optimal face is an additional audit guard, not a substitute for the pointwise bounds. The conclusion is not about omega(G), all-clique fractional optima, or graph edit distance, and is not sufficient for near-extremality.

## 7. Reproducible finite attack surface, not fabricated execution

The companion exact_checker.py implements two distinct rational LP algorithms: a packing tableau and a separately solved equality-partition revised simplex. Each returns primal and dual witnesses, all checked by exact Fraction arithmetic. Integer triangle packing uses a conflict-graph search; integer cp and p23 use an edge-cover recurrence. Thus the identities are compared across separately optimized quantities.

The planned complete corpus is all graphs through order 7 up to isomorphism. Construction A extends every smaller simple graph by every new-vertex neighborhood and takes an exact degree-class permutation canonical key. Construction B extends chordal graphs only by clique neighborhoods. Each unlabeled graph has a vertex-deleted representative in A's preceding level; each chordal graph has a simplicial vertex by Section 3, giving B's induction. Independent induced-hole recognition filters A and must match B exactly. A second simplicial recognizer and every possible clique suffix are checked. No external atlas or recalled graph count is assumed.

For each chordal graph the checker compares exact optima and the fractional bound. It checks all global maximizing pairs of two produced optimal duals and their midpoint. This finite set of duals does NOT exhaust the continuous optimal face; Section 6, not sampling, addresses the universal-choice quantifier.

Explicit expected controls are:
|graph|m|nu|nu_star|lambda|p23|cp|
|---|---:|---:|---:|---:|---:|---:|
|forest|m|0|0|m|m|m|
|K3|3|1|1|1|1|1|
|K4|6|1|2|2|4|1|
|diamond|5|1|1|3|3|3|
|J(3,2)|9|2|3|3|5|4|
|P6 squared|9|2|2|5|5|5|
|two K4 blocks sharing one vertex|12|2|4|4|8|2|

Their exact clique/packing certificates are in C22 Section 10 and can also be independently reconstructed from the checker edge lists. K4's four triangles of weight 1/2 give fractional packing 2, while any two triangles intersect in an edge. The diamond has exactly two triangles sharing an edge. J(3,2)'s two outside vertices each occur in at most one packed mixed triangle; all six mixed triangles of weight 1/2 give fractional optimum 3. P6 squared has triangles 123,234,345,456; constraints on edges 23 and 45 bound the fractional total by 2, attained by 123 and 456. Block additivity gives the windmill. These hand certificates are not executed enumeration results.

Fourteen authored injections cover cp/lambda confusion, a wrong packing factor, overlapping cover, missing edges, nonclique pieces, negative weights, overload, missing dual constraints, nonoptimal dual, omitted chordality, omitted theta sign, nonglobal maximizer, nonclique suffix, and cp/p23 confusion. Each must be rejected during replay. C4 is an explicit out-of-domain negative control, not a counterexample to (8).

Actual execution status: only Python AST syntax parsing was performed. Complete tested range: none. Executed mathematical tests: zero. Executed mutation tests: zero. Any future replay must report the actual maximum fully completed order, exact counts, input/output/code digests and toolchain fingerprint; a timeout cannot be reported as a passed order-7 check. The code itself remains pending correctness review.

## 8. Admission request and checkpoint

Fresh current registry facts: the Candidate ledger is empty; the admitted graph has only the O(n) root and exact split-domination statement; the weak asymptotic statement has no admitted obligation of its own. The registered Lean adapter requires an imported Candidate, actual Lean source and an exact toolchain allowlist match; the registry has no such allowlist. The sole GitHub workflow performs structural transport checks with contents:read. There is no applicable remotely invokable source/proof admission gate for this natural-language candidate. The generator must not substitute an unrelated fixture run.

The accompanying admission-request.json requests appropriately scoped trusted import, a separate asymptotic statement binding, bounded exact replay, source capture and cross-domain semantic/mathematical review. Missing source PDF byte digests, reviewer fingerprints and real run attestations are explicit nulls, not invented data. No EvidenceLink, ledger, Result or Solution is written by this candidate.

No internal contradiction was identified in the written proof relative to S1/S2. This is not independent admission. Because that primary acceptance is still pending, the secondary linear integrality-gap strengthening is NOT started.

Reasoning audit: definitions and negation are explicit; finite extrema and strict feasibility are checked; separator proof is strong induction with smaller graphs; vertex deletion preserves induced chordality and decreases an integer; exact edge loads justify symmetric certificates; floor and dense/low-core signs are separated; no random computation or finite-to-universal inference occurs. Existence from S1/S2 is mathematical, not an implemented efficient construction.

Status: NONTERMINAL_CHECKPOINT.
best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: candidate:erdos81-a01-c23-admission-audit.
Next action: fulfill the frozen admission request and replay the exact checker in an authorized, trust-separated runtime, then inspect all failures before any linear-rounding work.
