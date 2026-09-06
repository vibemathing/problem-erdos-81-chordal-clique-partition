# C09: modular mixed-clique packing and an exact quadratic-deficit family

Candidate ID: `candidate:erdos81-a01-c09-modular-packing`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `6ee7d293487b1fda18cedf8594b22e7b6f6ee3f7`
Verdict: `candidate_only`.

## 1. Scope and the precise auxiliary strategy under attack

This cycle treats an infinite family, not a finite-order exclusion. It supplies an exact edge clique partition number by a constructive partition and a matching signed edge-weight lower bound. It also shows why minimizing three restricted maximum-core strategies cannot by itself prove the root coefficient.

All graphs are finite and simple. cp is an exact edge partition into complete subgraphs; shared vertices are permitted. The graphs below are themselves split, so NONE is a counterexample to same-order split domination or to the root n^2/6+O(n) bound.

Inputs: C01's explicit matching decomposition of a complete graph and exact cp(J(k,t)) for t>=k; C05's fixed-core variational identity; C08's core matching potentials. These are candidate proof dependencies, not verification receipts. The present finite modular construction is proved directly. No mathematical program, enumeration, solver, random trial, or proof assistant was run. No novelty claim is made.

## 2. C09.1: family and an exact signed lower bound

Let G(a,b,t)=K_a joined to (K_b disjoint union I_t). In explicit terms, take disjoint sets A,B,I of sizes a,b,t; A union B is a clique; I is pairwise nonadjacent and each of its vertices is adjacent to all of A and to no vertex of B. Its order is n=a+b+t and
    m=binom(a,2)+binom(b,2)+ab+at.

It is split with core A union B. It is also chordal directly: list I first and then A union B to obtain a PEO. The frozen root concerns exact edge partitions, not this readily available clique cover.

Assign weights +1 to A-I and A-B edges, -1 to edges inside A, and -2 to edges inside B. Every clique has edge-weight sum at most one. A clique containing one I vertex and u A vertices has weight u-binom(u,2)<=1, and cannot meet B or contain a second I vertex. A clique containing no I vertices has u A and v B vertices, with weight
    uv-binom(u,2)-2binom(v,2)
      =1-(u-v)(u-v-1)/2-(v-1)(v-2)/2 <=1.
The last inequality holds for all nonnegative integers u,v because each product of two consecutive integers is nonnegative. In particular it covers cliques wholly in A or wholly in B.

Summing weights over any exact edge partition gives
    cp(G(a,b,t)) >= at+ab-binom(a,2)-2binom(b,2).           (1)
Negative weights are legitimate because each edge is counted exactly once; no overlapping-cover inference is used.

## 3. C09.2: modular packing attaining the bound

Let p>=3 be prime, and assume
    b=p-1, a>=2p, t>=a.                                   (2)
Under these assumptions equality holds in (1).

Label B by the nonzero residues modulo p. Reserve in A two disjoint sets
    U={u_z : z in Z_p}, V={v_z : z in Z_p}.
For each unordered pair of distinct labels i,j in B, take the K4
    {i,j,u_(i+j),v_(ij)},                                 (3)
where subscripts are calculated modulo p.

These binom(b,2) cliques are pairwise edge-disjoint. Each uses its unique B edge ij. At a fixed B vertex i, the maps j -> i+j and j -> ij are injective because i is nonzero modulo a prime; hence no B-U or B-V edge repeats. An A edge u_s v_z can repeat only if two unordered pairs have the same sum s and product z. If {i,j} and {k,l} have this property, then k is a root of
    X^2-sX+z=(X-i)(X-j).
Cancellation modulo p gives k=i or k=j, and equality of sums gives the other label. Thus the unordered pairs coincide. Edges internal to U or internal to V do not occur in (3), and U and V are disjoint even if the two residue values coincide.

All B edges and exactly binom(b,2) distinct A edges are now used. Decompose the complete graph on A into at most a matchings by C01, delete these used A edges from those matchings, and assign the resulting matching classes to distinct vertices of I. This is possible since t>=a. For every remaining A edge xy in a class assigned to z in I, take triangle {z,x,y}. Within a class the edges form a matching, and different classes use distinct I vertices, so crossing edges never repeat. These triangles share no edge with (3), which uses no I vertex.

Use every remaining edge as a K2. This partitions all edges exactly once. Relative to singleton edges it saves five for each of binom(b,2) K4s and two for each of binom(a,2)-binom(b,2) triangles. Its size is
    m-5binom(b,2)-2[binom(a,2)-binom(b,2)]
      =at+ab-binom(a,2)-2binom(b,2).
Together with (1), this proves the exact candidate formula
    cp(G(a,b,t))=at+ab-binom(a,2)-2binom(b,2)               (4)
for (2). It is a written optimality certificate, not the output of an ILP.

Since n=a+b+t, the same expression is
    an-(3/2)a^2-b^2+a/2+b <= n^2/6+n.
Indeed an-(3/2)a^2 = n^2/6-(3/2)(a-n/3)^2 and a/2+b<=n. Thus this infinite class satisfies a root-scale upper bound, despite permitting quadratic deficit.

## 4. C09.3: a scaling that defeats the three restricted maximum-core bounds

Specialize (2) to
    b=p-1, a=3b, t=4b.
Because b>=2, a>=2p. There are arbitrarily large such parameters, since primes are unbounded. Now
    n=8b, r=4b, m=20b^2-2b,
    delta=f_r(n)-m=4b(b-1),
    cp(G)=(19b^2+5b)/2.                                  (5)

The unique maximum clique is Q=A union B: any other maximal clique is A union {x} for x in I and has size 3b+1<4b. Consequently a choice among maximum cliques cannot alter the following conclusions.

Restricted strategy 1: require Q itself to be a partition piece. After all Q edges are used, the remaining graph consists of the 12b^2 A-I edges and no triangle. Its exact constrained cost is
    12b^2+1.                                             (6)

Restricted strategy 2: use only mixed triangles with two Q vertices and one I vertex, then put EVERY unused edge in a K2. Such a triangle necessarily uses an A edge. Thus at most binom(3b,2) triangles are possible. C01's matching construction through I attains that number, since t>=a. The exact minimum cost among these restricted partitions is therefore
    m-2binom(3b,2)=11b^2+b.                               (7)
C08's matching-average upper expression for the maximum Q also equals (7): every outside vertex has d_Q=3b and the averaging denominator is 4b. This does not say that an adaptive multi-stage procedure is limited to (7).

Restricted strategy 3: choose arbitrary vertex-disjoint cliques, then use singleton edges elsewhere, as in C08's disjoint-clique potential. Such chosen cliques collectively cover at most binom(4b,2) edges inside Q and at most a=3b A-I edges. For the latter assertion, each A vertex appears in at most one chosen clique, and each clique contains at most one I vertex. Thus the saving relative to singletons is at most binom(4b,2)+3b, even before subtracting the number of chosen pieces. EVERY bound produced by this strategy is at least
    m-binom(4b,2)-3b=12b^2-3b.                            (8)

It follows from (6)-(8) that the minimum of these three strategies is still bounded below by
    (11/64)n^2-O(n).
The coefficient 11/64 exceeds 1/6 by 1/192. No uniform linear error can eliminate this quadratic obstruction. This disproves asymptotic sufficiency of exactly these three restricted strategies, not the root or the admitted split reduction. The graph is split throughout.

## 5. C09.4: three successively richer constructions on the same graphs

The obstruction disappears by changing what information or pieces the procedure retains.

(A) Use the NONMAXIMUM core A. Assign all A edges to mixed triangles through I, and treat the remaining B clique as one piece. This gives
    cp(G)<=a(b+t)-binom(a,2)+1
          =(21b^2+3b)/2+1.
Its leading coefficient is 21/128<1/6. The point is that A is a useful universal core even though no maximum-clique choice has this size.

(B) Recycle the residual core instead of making all its unused edges singletons. First partition the A-I edges using matching triangles, spending all A edges, with total prefix cost at-binom(a,2). The residual on A union B is J(b,a): B is its clique side and A is pairwise nonadjacent in the residual. C01 gives its exact cp=ab-binom(b,2), because a>=b. Thus
    cp(G)<=at-binom(a,2)+ab-binom(b,2)=10b^2+2b.
This is a legal two-stage edge partition, not an assertion that every intermediate residual is chordal. Its leading coefficient is 5/32.

(C) The modular K4 construction (3) and its matching signed lower bound attain the optimum (5), with leading coefficient 19/128. The K4 pieces allocate one B edge, one A edge, and four crossing edges simultaneously. They are precisely the extra resource omitted by strategies (6) and (7).

These constructions can be compared as upper bounds but their savings cannot be added unless a single edge-disjoint assembly is explicitly supplied. Only construction (C) is asserted optimal under (2).

## 6. C09.5: universal cores with clique-union residuals

One useful infinite class can be stated without maximum-clique language. Suppose G=K_s joined to R, where s>=2, t=|R|>=s, and R is a disjoint union of cliques. If R has p components with at least one edge, then
    cp(G)<=st-binom(s,2)+p.                               (9)
Assign all core matching classes to distinct R vertices, which are all adjacent to the core. Triangles from these classes use no R-internal edge and are edge-disjoint. Partition each nontrivial R component once and leave remaining crossing edges as K2s. This proves (9).

Writing n=s+t, the quadratic part satisfies
    s(n-s)-binom(s,2)
      =n^2/6+n/6+1/24-(3/2)(s-n/3-1/6)^2.
Since p<=n, (9) in particular implies cp(G)<=n^2/6+2n. These graphs are chordal by eliminating each R component before the universal core. The condition of a universal core and clique-union residual is a genuine restriction, not a structural theorem about all chordal graphs.

## 7. Audit, failed-method proposal, and next obligation

Audit cases: p=3, b=2, a=2p, t=a; repeated sum but different product; a common endpoint i in two B edges; the nonzero-label requirement; disjointness of U and V; matching restriction after K4 expenditure; wholly A or wholly B cliques in the lower certificate; uniqueness of Q in the scaling; exact versus restricted cp; and vertex-disjoint versus merely edge-disjoint clique families.

The auxiliary method to discard is the assertion that choosing a maximum clique and minimizing only its intact-piece cost, its one-stage mixed-triangle-plus-singleton cost, and the vertex-disjoint-clique-plus-singleton potentials always reaches n^2/6+O(n). Section 4 contradicts that assertion. Neither all core-allocation methods nor the admitted existential route is discarded. The canonical failed-route ledger is not edited.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: formula (4), its explicit upper/lower certificates, and the restricted-class root bounds.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
No mathematical execution or verifier receipt exists.

Next exact obligation: introduce separator-edge budgets allowing nonmaximum cores and several passes, and quantify when mixed K4 or larger pieces can replace the loss in the triangle-only potential. Do not assume that choosing a maximum independent set and completing its complement has only O(n) cp loss; a clique blow-up of P5 gives a quadratic-loss test for that prospective replacement route.
