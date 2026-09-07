# C21: recovered fractional proof variants and integer-gap certificates

Candidate ID: `candidate:erdos81-a01-c21-chat-transport-addendum`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Transport base: `2f7b0122c5df4169822195bb2dac9690fc471e8e`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Provenance, deduplication, and verification boundary

This is transport of arguments already present in Issue #1 comments 5560952646 and 5560997451, both created on 2026-09-06 and successfully read back during the 2026-09-07 reconciliation. It is not a new research cycle. Only the distinct proof variants, formulas, and witnesses are retained here; no full conversation or private reasoning transcript is stored.

The fractional complete-split domination theorem, extremum B(n)=floor(n(n+1)/6), edge-and-triangle fractional formulas, and packing-to-partition identities are already in `research/artifacts/candidates/erdos81-a01-c18-fractional-compression.md`. Those results are referenced rather than republished as new claims. C18's actual-neighborhood maximization differs from the capacity maximization written below. C19's dual-rigidity result does not replace the all-clique fractional formula or the integer-gap witnesses here.

Notation: cp is the integer exact edge-clique partition number; fcp allows nonnegative weights on all cliques with nonempty edge sets, with total weight exactly one at every edge. The parameter p3star allows only edges and triangles in that fractional partition. In C18, these are cp_f and lambda respectively. Every graph is finite and simple. fcp<=cp and fcp<=p3star, but p3star need not be at most unrestricted integer cp.

Finite LP strong duality and the clique-suffix perfect elimination ordering are declared inputs as in C18/C04. The original allowed axioms remain finite-graph-basic, finite-combinatorics, and real-arithmetic. The incidence-matrix argument below additionally requires audit of its elementary real linear-algebra interpretation under that contract; transport does not admit any new axiom.

All displayed statements and proofs remain unverified natural-language candidates. No LP, graph enumeration, numerical experiment, Lean, SMT, or mathematical proof-audit program was executed or replayed in this reconciliation. Byte hashing and transport CI are not mathematical verification. No novelty or current-best claim is made.

## 2. Recovered attachment-capacity proof variant

For the all-clique fractional primal, finite LP duality gives
    fcp(G)=max sum_e y_e,
    y(E(K))<=1 for each clique K with an edge,
where edge weights y_e may have either sign. Single-edge primal pieces ensure feasibility and a finite optimum. Edgeless graphs are separate trivial cases.

Fix an optimal y. For each nonempty clique S, of size s, define
    a_y(S)=max sum_(u in S) z_u
subject to
    sum_(u in A) z_u+y(E(A))<=1
for every nonempty subset A of S. The vector zero is feasible; singletons imply z_u<=1. On the part with nonnegative objective, z_u>=-(s-1). Thus the optimum is attained on a compact set. Let a=max_S a_y(S), choose a maximizing S and vector z. Singleton cliques give a>=1.

A PEO can end in S: first end it in a maximal clique containing S, using C04, then reorder that last clique so S is last. For each earlier pivot v with nonempty later-neighbor clique T, the vector (y_vu) over T satisfies the capacity constraints, because every {v} union A is a clique. Its later-edge sum is therefore at most a. An empty later neighborhood contributes zero. Counting edges at their earlier endpoints gives
    fcp(G)<=y(E(S))+(n-s)*a.

Construct J(s,n-s)=K_s joined to n-s pairwise nonadjacent vertices. Retain y on the core and put z_u on the edge from each outside vertex to core vertex u. Core-only constraints are inherited; every mixed-clique constraint is a capacity constraint. This feasible dual has value y(E(S))+(n-s)*a, proving the same-order fractional domination claim already recorded by C18 through a different proof.

For p3star the dual has only
    y_e<=1 and y_ab+y_ac+y_bc<=1 for every triangle.
Use the capacity constraints
    z_u<=1 and z_u+z_v+y_uv<=1.
The same compactness, PEO, and repeated-leaf argument applies. This recovers the alternate proof in comment 5560997451. The formulas for p3star(J(r,t)), its extremum B(n), and the exact rounding interface remain at C18; they are not new results of this addendum.

## 3. Recovered dense-core fractional upper certificate

Comment 5560952646 also used this all-clique certificate. For s>=2 and 1<=t<=s-1, give each mixed triangle of J(s,t) weight 1/(s-1) and give its whole core clique weight 1-t/(s-1). Each crossing edge has total weight one; each core edge has mixed load t/(s-1) and receives the remaining load from the core piece. Its cost is
    st/2+1-t/(s-1)<=n^2/8+1, n=s+t.

The original comparison used n>=6 and
    n^2/8+1<=n(n+1)/6-1<=B(n),
equivalent at the first step to n^2+4n-48>=0. At n=4,5 the quantity n^2/8+1 is already at most B(n). For n<=3 the possible clique, star, and edgeless cases are handled directly; when t=0 one core piece suffices if it has an edge. The sparse-core certificate and final B(n) conclusion are already C18. This section preserves only the distinct dense-core construction, not a claim that it is optimal.

## 4. Exact unrestricted fractional value of every complete split graph

For integers r,t>=1 let
    mu=1+(r-1)/t, k=floor(mu), theta=k+1-mu.
The recovered candidate formula is
    fcp(J(r,t))=rt*[theta/k+(1-theta)/(k+1)]
              =r*[2tk-(r-1)]/[k(k+1)].                 (1)

For each outside vertex, give each mixed clique with k core vertices weight theta/binom(r-1,k-1), and each with k+1 core vertices weight (1-theta)/binom(r-1,k). When k=r, theta=1 and the second family is omitted, so no division by a zero binomial is used. Each crossing edge has total weight theta+(1-theta)=1. For r>=2 the total load on a core edge is
    t*[theta*(k-1)+(1-theta)*k]/(r-1)=1.
For r=1 there are no core edges. Counting the pieces with their weights gives the first expression in (1).

For a matching dual certificate, set
    y_cross=2/(k+1), y_core=-2/[k(k+1)].
A mixed clique with j core vertices has weight
    j*(2k+1-j)/[k(k+1)]
     =1-(j-k)*(j-k-1)/[k(k+1)]<=1
for every integer j. Core-only cliques have nonpositive weight. The dual objective equals the second expression in (1), so the written primal and dual certificates agree. This is a symbolic certificate, not the output of an executed LP.

## 5. A nearly n-sized integer versus unrestricted-fractional gap

For r>=1, let J(r,2)=K_(r+2) with exactly one edge uv removed, and put n=r+2. The candidate integer value is
    cp(J(r,2))=r+1=n-1.                                (2)
One K_(r+1), together with the other outside vertex's r remaining edges, gives the upper bound.

For the lower argument from comment 5560997451, let M be the vertex-versus-piece incidence matrix of any exact clique partition, and d_w the number of pieces containing w. Every core vertex has d_w>=2, since its full neighborhood is not a clique. If d_u=1 or d_v=1, its sole piece contains the whole core; each of the other endpoint's r edges then needs a separate piece, giving at least r+1.

Otherwise every d_w>=2. Writing J for the all-ones matrix,
    MM^T=J+diag(d_w-1)-e_u e_v^T-e_v e_u^T.
On the (n-1)-dimensional subspace x_u=x_v its quadratic form is
    (sum_w x_w)^2
       +sum_(w in core)(d_w-1)*x_w^2
       +(d_u+d_v-4)*x_u^2.
All terms are nonnegative, and vanishing forces every core coordinate to be zero and then x_u=x_v=0. Thus M has rank at least n-1 and at least n-1 columns. This gives (2).

Specializing (1) yields
    fcp(J(r,2))=4r/(r+1) when r is odd,
    fcp(J(r,2))=4(r+1)/(r+2) when r is even.
Consequently (cp-fcp)/n tends to one. A uniform chordal inequality cp<=fcp+c*n+O(1) cannot have c<1. This is not a denial of a larger linear rounding allowance. These witnesses themselves are split, so they are not counterexamples to the admitted integer split-domination question or the root bound.

## 6. Recovered clique-sum calibration

The single-block values cp(J(3,2))=4 and fcp(J(3,2))=3 already appear in C18, with explicit partitions and lower arguments. Identify one core vertex across h disjoint copies of this block, with no other edges between blocks. Every cycle and every clique containing an edge remains inside one block. Thus the graph is chordal and both integer and fractional partition objectives add over blocks:
    n=4h+1, cp=4h, fcp=3h, cp-fcp=h=(n-1)/4.
This is the clique-sum extension in comment 5560952646, not a newly generated family. It rules out a uniformly constant unrestricted-fractional rounding error, not a linear error.

## 7. Scope and resume point after transport

The root and exact integer same-order domination remain open. C18 already states that p3star=m-2*nu3star and p3=m-2*nu3; a uniform linear bound on nu3star-nu3 would suffice for a root-scale integer bound. The separate condition cp-fcp=O(n) is also only a sufficient, unproved strengthening. Neither is silently assumed here.

The companion source/coverage note identifies which earlier material was already in main, which distinct arguments are now transported, and why previously unread write responses did not imply missing Issue comments. This round introduces no fresh mathematical claim beyond those comments.

best_verified_result: none.
best_verified_candidate: none.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
next_action: complete final transport reconciliation; only a later research step may audit these pending arguments or pursue rounding.
