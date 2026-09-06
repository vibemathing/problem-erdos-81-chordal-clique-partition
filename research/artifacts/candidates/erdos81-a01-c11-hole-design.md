# C11: incomplete triple systems and a root-compatible interface increment

Candidate ID: `candidate:erdos81-a01-c11-hole-design`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `e70735bcaf64d1f1016c3bf4900ea5d8a1d91c4d`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Scope and dependency

All graphs are finite and simple. cp is an exact edge partition into nonempty complete subgraphs. The target and the asymptotic root remain open.

Let J(a,s)=K_a joined to s pairwise nonadjacent vertices. When it is an interface in a larger graph, the s vertices may have edges among themselves; NONE of those edges is included in J(a,s) or used by its partition.

This cycle reuses the Doyen-Wilson existence theorem as stated and proved in D. R. Stinson, "A new proof of the Doyen-Wilson theorem", J. Austral. Math. Soc. (Series A) 47 (1989), 32-42, especially the theorem on printed page 41. The primary PDF and the inequality >= were visually checked; details are in the accompanying source note. This is a declared external theorem dependency, not a kernel receipt or a new proof of that theorem. The subsequent graph conversion and congruence repair are proved below. Allowed axioms remain finite-graph-basic, finite-combinatorics, real-arithmetic. No mathematical program was executed.

## 2. C11.1: exact triangle decomposition with a hole

If positive integers v,w satisfy
    v,w congruent to 1 or 3 modulo 6, and v>=2w+1,
there is an STS(v) containing an STS(w) as a subsystem. Delete the subsystem's triples. Each remaining triple has at most one vertex in the w-point hole: a triple with two hole vertices would repeat a pair already covered inside the subsystem. The remaining triples therefore partition precisely
    E(K_v) minus E(K_w).
Their number is [v(v-1)-w(w-1)]/6.

This is an edge partition, not a cover, and spends no hole edge. The w=1 case simply uses a one-point subsystem with no internal pairs. The conversion depends on pair uniqueness, not on resolvability or an unmentioned design hypothesis.

## 3. C11.2: all congruences, with error proportional to the added core

For every a>=s>=0 with a>=1,
    cp(J(a,s)) <= Phi(a,s)+4a,
    Phi(a,s)=(a^2+2as)/6.                                  (1)

If s=0, one clique (or zero when a=1) suffices. Assume s>=1. Let w be the largest integer <=s congruent to 1 or 3 modulo 6. Put b=s-w, so 0<=b<=3. Let v be the smallest integer congruent to 1 or 3 modulo 6 with
    v>=max(a+w,2w+1),
and put d=v-(a+w).

Here 0<=d<=3. If a>w, then a+w>=2w+1 and the next allowed residue is at distance at most three. If a=w, then 2w+1 itself has an allowed residue and d=1.

Apply Section 2 to a core of size v-w=a+d and a hole of size w. Restrict the resulting triples to any a of the core vertices and all w hole vertices. Restricting a clique preserves completeness and cannot duplicate an edge; pieces with fewer than two surviving vertices are discarded. The other surviving pieces cover exactly J(a,w). Add the b omitted hole vertices and cover their ab edges to the core singly. Thus
    cp(J(a,s)) <= ab+[v(v-1)-w(w-1)]/6
      = Phi(a,s) - a/6 + (2/3)ab
        + d[2(a+w)-1+d]/6.
Using w<=a, b<=3 and d<=3 gives
    cp(J(a,s)) <= Phi(a,s)+(23/6)a+1.                       (2)
For a>=6 this is at most Phi(a,s)+4a.

For 1<=a<=5 use the core once and all as crossing edges singly, at cost at most as+1. Its excess over Phi is
    (2/3)as-a^2/6+1 <= a^2/2+1 <=4a.
This finishes every small and congruence case without an enumeration claim.

The construction augments and then deletes vertices; it never fills a missing edge inside the given graph. The s-hole edges remain reserved throughout. Formula (1) is a sufficient bound, not an exact formula in this regime.

## 4. C11.3: clique-module peeling with no double counting

Let A be a nonempty clique of a vertices in G. Suppose all vertices of A have the same outside neighborhood S of size s, and a>=s. Put H=G-A and N=|V(H)|. No restriction on edges of H[S] is needed. The edges not in H form exactly the interface J(a,s). Hence
    cp(G) <= cp(H)+Phi(a,s)+4a.                             (3)

The partitions in (3) share at most vertices: the first uses only H edges, while the second uses only edges incident to A. This is why the hole condition matters.

Fix C>=4 and set B_C(x)=x^2/6+Cx, including x=0. If cp(H)<=B_C(N), then
    cp(G) <= B_C(N+a)-a(N-s)/3+(4-C)a
           <= B_C(N+a).                                   (4)
H is chordal whenever G is chordal, since it is induced.

Consequently, a vertex-minimal chordal counterexample to cp(G)<=B_C(n), should one exist for a fixed C>=4, has no nonempty clique module whose size is at least its outside-neighborhood size. This is a minimal-counterexample reduction, not a proof that such counterexamples do not exist.

In particular, for a leaf of a maximal-clique tree, its private set A and separator S satisfy these module hypotheses. A minimal counterexample cannot have |A|>=|S|. The statement includes a complete component with an empty separator. It does not assume the remaining edge-deleted graph is chordal.

## 5. C11.4: genuine universal-core reduction for the root potential

If G=K_u joined to H with u>=|V(H)|=t, then
    cp(G) <= cp(H)+[(u+t)^2-t^2]/6+4u.                     (5)
This uses a hole on ALL t vertices of H, even if H is not complete. It is not the operation of declaring H edgeless in G.

Thus for fixed C>=4, a vertex-minimal chordal counterexample to B_C has fewer than n/2 universal vertices. Combining this with C10's candidate lower bound
    u >= max(0,2r-n-delta)
gives the necessary condition
    4r < 3n+2delta.                                        (6)
The C10 bound and (6) concern genuine universal vertices, not a core made universal by adding edges.

Formula (5) is conditional on a bound for the smaller H when used in induction. It does not replace cp(H) by t^2/6 without that hypothesis. In particular, it does not settle general zero-deficit graphs or low-core joins.

## 6. C11.5: the small-core barrier is quadratic, not a residue error

One cannot extend (1) to every a,s with an error O(a). If s=2a, C01's explicit matching and signed-weight argument gives
    cp(J(a,2a))=2a^2-binom(a,2)=(3a^2+a)/2.
Subtracting Phi(a,2a)=5a^2/6 leaves
    (2/3)a^2+a/2,
which exceeds every fixed multiple of a.

This does not contradict the root: J(a,2a) has n=3a and cp=n^2/6+n/6. The edgeless hole has much smaller cp than its quadratic induction allowance. A successful low-core potential must retain that slack or use some hole edges in mixed cliques.

Triangle-only decomposition also has a direct capacity restriction. Each mixed triangle covers two crossing edges and spends one core edge. Covering all as crossing edges this way requires as/2<=binom(a,2), or s<=a-1. The O(a) repair in Section 3 permits the boundary a=s, not an arbitrary imbalance.

## 7. Audit and next obligation

Audited: the >= threshold in the primary source versus damaged text extraction; w=1; all residue gaps; a=w; d=0; deletion of padded vertices; pieces shrinking to K2; a<=5; s=0; reserved hole edges; and the distinction between an induction reduction and root closure.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: this written derivation with the declared design theorem and C10 input.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.

Next exact task: amortize these interface costs over a clique tree, keeping both the nonedge slack and the cost of minority private sets. Derive the exact penalty rather than summing incompatible savings from C08 and C09. Separately, the Doyen-Wilson theorem dependency needs the verification capabilities required by the admission policy before any root use is admitted. No ledger, EvidenceLink or Result is written.
