# C24 addition: explicit additive rounding losses on a clique tree

Verdict: candidate_only. This document is a mathematical proof candidate, not a verifier receipt. The root and exact split-domination obligations stay open. No computation result is inferred from creating this file.

## 1. Exact statement

Let G be finite and simple and admit a clique-tree forest with bags B_i covering all graph edges and all triangles, and with the running-intersection property for every vertex. Root each tree. Put b_i=|B_i| and S_i=B_i intersect B_parent(i), with S_i empty at roots; write s_i=|S_i|. The candidate bound is

    nu_star(G)-nu(G) <= n/2 + (1/3) sum_i s_i^2 + (1/6) sum_i s_i
                     <= (n + sum_i s_i^2)/2.                (CT)

Here nu is maximum EDGE-disjoint triangle packing and nu_star is its nonnegative fractional relaxation with capacity one per graph edge. Isolated vertices and empty separators are allowed. In particular a class satisfying sum_i s_i^2 <= K*n for a fixed K has gap at most (K+1)*n/2. This is a genuine all-order linear bound on that restricted class, not a bound for arbitrary chordal graphs with no separator-budget hypothesis.

Combining (CT), the separately audited lambda<=B(n)=floor(n(n+1)/6), and cp<=p23=lambda+2(nu_star-nu), gives

    cp(G) <= n^2/6 + (K+7/6)*n

on this class. No weaker theorem is used to close the frozen unrestricted root.

## 2. A self-contained complete-graph packing with at most 3b/2 uncovered edges

For every odd integer q>=1 construct triples on Z_q x Z_3 as follows. Include the q vertical triples {(x,0),(x,1),(x,2)}. For every unordered pair x!=y and i in Z_3 include

    {(x,i),(y,i),((x+y)/2,i+1)}.

Division by two is in Z_q, where two is invertible. An equal-layer pair with distinct first coordinates determines its displayed triple uniquely. A pair in adjacent layers with distinct first coordinates determines the missing first coordinate y=2z-x uniquely; if the first coordinates agree, it belongs instead to the unique vertical triple. Each unordered pair of distinct vertices occurs once. Thus these triples decompose K_(3q), and the vertical triples form a parallel class. This explicitly proves the design property used here rather than importing a design-existence theorem.

For b congruent to 0,1,2,3 modulo six, take the least v>=b with v congruent to 3 modulo six and restrict this decomposition to b retained vertices. Here d=v-b is respectively 3,2,1,0. An uncovered retained edge has its unique third design point among the d deleted vertices. For each deleted point those retained pairs form a matching, so at most d*b/2 edges remain uncovered. In particular the leave has at most 3b/2 edges.

For b congruent to 4 modulo six, decompose K_(b-1) by the same construction and ignore the new vertex's b-1 incident edges.

For b congruent to 5 modulo six, put m=b-2=3q with q odd and start with its design. Add vertices x,y. For each vertical triple {a,b,c}, remove that triple and insert {x,a,b} and {y,a,c}. Different replacements have disjoint private triples and therefore disjoint crossing edges; their internal edges were used only by the removed vertical triple. The resulting packing has C(m,2)/3+q triangles. Exactly m+1=b-1 edges of K_b remain uncovered, including xy. This is again at most 3b/2.

Orders zero, one and two are handled directly by the empty packing. Thus for each bag of size b there is an explicit triangle packing whose leave L(b) satisfies L(b)<=3b/2. The construction asserts an upper bound on the leave, not the exact maximum packing number at every order.

## 3. Edge ownership and separator repair

For a graph edge e, the bags containing both endpoints form a nonempty connected subtree: it is the intersection of the two endpoint subtrees. It consequently has a unique highest bag. Hence the edge sets

    F_i=E(K_(B_i)) minus E(K_(S_i))

partition E(G). Each vertex similarly has a unique highest bag, giving

    sum_i b_i = n + sum_i s_i.

Choose the complete-bag packing from Section 2. Delete every packed triangle containing an edge of S_i. Since packed triangles are edge-disjoint, at most C(s_i,2) triangles are deleted. The survivors use only edges in F_i, so survivors from different bags cannot conflict, even when the bags share vertices and large separators.

If k_i triangles were deleted and the original bag leave was L_i, the number of uncovered edges in F_i is exactly

    L_i + 3*k_i - C(s_i,2)

and is therefore at most L_i+2*C(s_i,2). Negative algebraic lower estimates are not used; the displayed exact expression counts an actual nonnegative edge set. Summing over the disjoint F_i yields a global packing with leave at most

    (3/2) sum_i b_i + 2 sum_i C(s_i,2).

Every fractional triangle packing has value at most |E(G)|/3, by summing edge capacities. If a constructed integer packing leaves L edges, then nu_star(G)-nu(G)<=L/3. Applying this and the vertex count identity gives

    nu_star-nu <= (1/2) sum_i b_i + (2/3) sum_i C(s_i,2)
                = n/2 + (1/3) sum_i s_i^2 + (1/6) sum_i s_i.

The second inequality in (CT) follows from s_i<=s_i^2 for nonnegative integer s_i. This proof explicitly charges every local loss; it does not add incompatible bag optima while ignoring shared separator edges.

## 4. Chordal applicability and termination

A PEO supplies a clique-tree forest without an algorithmic existence gap: reconstruct the graph in reverse PEO order. When adding a vertex, its already present neighbors are a clique. By induction every clique in the present graph is contained in some current bag. Attach its new bag (the vertex together with those neighbors) to a bag containing the neighbor clique, or start a new tree if the neighbor clique is empty. Running intersection is preserved. Every new clique containing the added vertex is in the new bag. The number of unintroduced vertices decreases strictly. Redundant bags may be retained; (CT) applies to any resulting forest, with its actual separator budget.

The graph-specific lambda bound used to translate (CT) to cp is a separate proof dependency, not necessary for the gap bound itself. The existence of a clique tree by itself does not imply that its sum of squared separator sizes is linear. For example complete split graphs can have many bags with the same large core separator. Their separately proved matching construction is the appropriate certificate, not a false claim that this budget is automatically small.

## 5. Explicit failure of constant loss for an arbitrary simplicial deletion

The proposed rule delta(G)<=delta(G-v)+1, with delta=nu_star-nu and v simplicial, fails already on K8.

K7 has edges all pairs of {1,...,7}, unique maximal clique {1,...,7}, and the seven disjoint triangles

    123,145,167,246,257,347,356.

They cover all 21 edges. Thus nu=nu_star=7, delta=0, cp=1.

K8 has edges all pairs of {1,...,8}, unique maximal clique {1,...,8}, and the eight disjoint triangles

    345,678,147,258,156,237,138,246.

Their leave is exactly {12,36,48,57}. Every vertex of K8 has odd degree while packed triangles use even degree at each vertex. A leave must therefore have degree at least one at each of the eight vertices and at least four edges. It follows that nu<=8, matched by the displayed packing. Giving all 56 triangles weight 1/6 saturates each edge and gives nu_star=28/3; total capacity gives the matching upper bound. Therefore delta(K8)=4/3 and cp(K8)=1. Deleting any vertex gives K7, and that vertex is simplicial. The numerical mismatch is 4/3>1. No minimality over all smaller chordal graphs is asserted without the separate completed deletion-enumeration record.

There cannot be any universal constant for this arbitrary-deletion rule. For h>=1 the affine lines of F_3^h decompose K_(3^h), so its gap is zero. In K_(3^h+1), every degree is odd; hence every integer triangle packing leaves at least (3^h+1)/2 edges, whereas fractional weights 1/(3^h-1) on all triangles saturate every edge. Its gap is at least (3^h+1)/6 and diverges. This family negates constant *single-step* loss, not a global O(n) gap bound; its cp is always one. The exact integer optimum of every larger even member is not claimed by this lower argument.

## 6. Open obligation and audit limits

The first remaining rounding question is whether large repeated separators can be charged with a total O(n) debt rather than sum_i s_i^2, or bypassed by a compatible simultaneous core/leaf packing. Arbitrary constant-per-simplicial-step loss is invalid, as Section 5 proves. The separate low-complete-split edit-distance theorem covers only an actual linear edit budget, not every dual-low-core graph.

All constructions here are finite and explicit. A checker should enumerate the displayed triples, verify pair uniqueness, build F_i, and compare the exact leave after separator repair. Computational confirmation is finite support, not the universal proof. No trusted verifier, source attestation, EvidenceLink, Result or Solution is asserted. The unrestricted root remains open; checkpoint status is NONTERMINAL_CHECKPOINT.
