# Nested-prefix candidate: a one-time linear normalization charge

Candidate ID: candidate:erdos81-a01-c24-nested-normalization
Repository: vibemathing/problem-erdos-81-chordal-clique-partition
Problem: problem:erdos-81-chordal-clique-partition
Attempt: attempt:web-20260906-erdos81-a01
Route: route:split-extremal-reduction-v1
Graph: graph:erdos81-initial-v1
Transport obligation: obligation:erdos81-split-extremal-reduction
Base: 09c2b6f3e277eb20fc34d0add65ee8d027c5bb37
Primary owner: math-proof. Verdict: candidate_only. best_verified_result: none.

## 1. Scope and status

Let G(r;d_1,...,d_t) have clique vertices 0,...,r-1 and independent vertices x_1,...,x_t, where N(x_i)={0,...,d_i-1} and 0<=d_1<=...<=d_t<=r. Put n=r+t. Empty and equal neighborhoods are allowed, and the chosen core need not be maximal. All edge sets are simple. Triangle packing uses edge-disjoint triangles; fractional weights are nonnegative with capacity at most one on each edge. Write delta=nu_star-nu. The current atomic goal is a universal delta(G)<=C*n for this entire class. THIS GOAL REMAINS OPEN IN THIS CANDIDATE.

The result below is an explicit linear-cost reduction, not an integer packing of the final residual. It removes a genuine source of repeated separator costs, but does not prove a linear gap for the normalized graph. Leaf cliques with internal edges are not included in this independent-leaf theorem. No extension to general clique-tree intervals is claimed.

Distinct statements remain distinct: C22's source-backed uniform n^2/6+o(n^2) proof draft; the present unproved linear-gap goal for nested split graphs; the root's universal chordal cp<=n^2/6+O(n); exact same-order split domination. None is silently substituted for another.

## 2. One-time fractional edge-capacity charge

Let H be a spanning subgraph of an arbitrary simple G and let F=E(G) minus E(H), D=|F|. Fix ANY feasible fractional triangle packing z of G, and fix a total order on F. Charge every triangle that meets F to its first edge in F. Every charged weight at e is part of its original edge load, so the total charge at e is at most one. The charge classes are disjoint. Removing those triangles loses at most D units of packing weight and leaves a feasible fractional packing of H.

Applying this to an optimum z gives nu_star(G)<=nu_star(H)+D. Every integer packing of H is valid in G, so nu(G)>=nu(H). Therefore

    delta(G)<=delta(H)+D.                                  (1)

This is a charge on the original optimal packing, not a sum of separate separator optimizations. Each deleted edge is paid at most once. No monotonicity of delta under arbitrary deletion is asserted. No assumption that deletion preserves chordality is needed for (1).

## 3. An explicit h-divisible normal form

For every integer h>=2 and every nested graph G of order n, there is a spanning nested subgraph H, allowing additional isolates, such that

    |E(G) minus E(H)|<=3(h-1)n.                            (2)

When r>0 its retained core has size r'=1+h*floor((r-1)/h). Every positive leaf depth is divisible by h, and the multiplicity of every positive depth is divisible by h. Vertices outside this template are isolated. When r=0, take the edgeless graph itself.

Construction and disjoint charges:

A. Retain the first r' core vertices and isolate the other at most h-1 core vertices. At most (h-1)n edges are deleted. Cap the leaf depths at r'; these spoke deletions were already charged in A.

B. Retain the first t'=h*floor(t/h) leaves in the sorted order; isolate the last fewer than h leaves. Charge their surviving spokes to B. There are at most (h-1)r' such edges, none counted in A.

C. Partition the retained leaves into consecutive groups of h. In a group whose smallest and largest capped depths are l and u, lower all depths to l. This costs at most (h-1)(u-l). The degree intervals of consecutive groups are ordered and have disjoint interiors. Thus sum_groups(u-l)<=r', even if there are arbitrarily many groups, and the ENTIRE equalization cost is at most (h-1)r'. Each lost spoke is charged to its own group interval; no prefix-clique edge is charged at every occurrence.

D. In each group lower l to h*floor(l/h). Each leaf loses at most h-1 further spokes, costing at most (h-1)t in total. These edges were present after C and therefore are disjoint from all earlier charges.

The resulting graph has exactly the asserted adjacency. Equal groups may merge, but their multiplicities remain multiples of h. Summing costs gives at most (h-1)(n+2r'+t)<=3(h-1)n, proving (2). Isolated vertices are retained, so n is unchanged. Each operation removes edges; each group is processed once, and the finite number of groups decreases to zero. The retained nonisolated core and all leaf neighborhoods remain nested throughout.

Combining (1)-(2) gives

    delta(G)<=delta(H)+3(h-1)n.                            (3)

For h=2, H has an odd core and even depths occurring in pairs. Every leaf has even degree; each core vertex has even core degree plus an even number of leaf neighbors. Thus H is Eulerian and the overhead in (3) is at most 3n.

For h=6, the overhead is at most 15n. A uniform K*n gap bound for these six-divisible normal forms would imply the requested nested-class bound with C=K+15. Conversely, a bound for the full nested class includes its normal forms. This is an equivalent reduction up to a constant change, NOT a solution of the normalized rounding problem. In particular, divisibility alone is not being asserted to make the triangle-packing LP integral.

Empty/full neighborhoods, ties and small r are explicit: zero depths remain isolated; initially full depths are capped and rounded just like other depths; equal depths give zero C-charge; for 1<=r<h+1 the retained core is one vertex and subsequent depth rounding leaves no triangle. Repeated maximal-clique bags are not counted at all; the construction uses vertices and their neighborhood list, not a bag occurrence count.

## 4. A seven-vertex obstruction to an exact parity shortcut

The proposed shortcut "Eulerian nested graph and integral nu_star imply nu=nu_star" is false. Take core K5 on {0,1,2,3,4}, and leaves 5,6 each adjacent only to {0,1}. Its maximal cliques are exactly {0,1,2,3,4}, {0,1,5}, {0,1,6}. All other cliques with edges are their subsets; the machine certificate lists them. It has n=7, m=14, all degrees even, and

    nu=3, nu_star=4, delta=1, cp=5, p23=8, lambda=6.      (4)

Integer packing: 015, 023, 124. Four triangles would leave exactly two edges. A triangle packing removes even degree at every vertex, so the leftover graph must have even degrees. A simple graph with exactly two edges cannot have all degrees even. Thus at most three triangles are possible.

Fractional packing: weight 1/2 on 015 and 016; weight 1/2 on each of 023,024,034,123,124,134; zero on other triangles. The edge 01 has load one, each of the other nine core edges has load one, and every pin spoke has load 1/2. The total is four. A matching dual sets price one on 01, price 1/3 on the other nine core edges, and zero on the pin spokes. Every triangle has price at least one; the total price is four. These are explicit rational primal/dual certificates.

The K5 and the four pin spokes partition the edges into five cliques. No partition with at most four pieces exists. If neither pin triangle is used, the four pin spokes require four distinct singleton pieces and the core still needs a piece. If a pin triangle is used, the other cannot be used because they share 01; three pin-containing pieces are needed, while the remaining noncomplete core needs at least two clique pieces. This proves cp=5.

Complete enumeration of every nested representation through order seven found the first failures of this shortcut at order seven: two representations of this same type, r=5,d=(2,2) and r=4,d=(2,2,4). This is an order-minimum claim within the enumerated nested domain, not among arbitrary chordal graphs. It is not the old eight-vertex clique-sum example, and is not a superlinear-gap or root counterexample. A correction must allow nonzero normalized rounding loss.

## 5. A family of exact prefix-capacity upper certificates

For 0<=k<=r, set packing-dual prices one on core edges inside [k], and 1/3 on other core edges. At a leaf of depth d, choose the cheaper of: all spokes priced 1/3; or prefix-[k] spokes priced zero and remaining spokes priced 2/3. Its cost is min(d,2(d-k)_+)/3. Every core triangle has price at least one. A mixed triangle with both endpoints in [k] has its core edge priced one; a mixed triangle with an endpoint outside [k] has core price 1/3 and spoke price at least 2/3 in the second option. The first option also works for every mixed triangle. Therefore

    nu_star(G)<=U_k(G)
      =[binom(r,2)+2binom(k,2)+sum_i min(d_i,2(d_i-k)_+)]/3. (5)

These bounds charge core capacity once. The case k=0 is simply an upper certificate, not necessarily tight on triangle-free edges. We do NOT assert that min_k U_k, or a further minimum with a cut bound, equals the optimum. An observed finite equality would not prove such a dual classification.

## 6. Exact computation and first remaining obligation

The accompanying check.py was actually executed with the immutable supplied C23 backend. That backend solves the fractional packing by rational tableau simplex and lambda directly by a different rational revised-basis equality simplex, rather than assigning lambda=m-2nu_star. Integer triangle packing and edge partitions use separate exact search recurrences. All twelve authored backend mutations were actually rejected.

A complete run checked all 255 prefix parameter descriptions at orders 0 through 7 (2^n descriptions at each order, not 255 distinct isomorphism classes), all h=2,6 normalizations, capacity-charge inequalities, the certificates (5), and the C23 identities. A later bounded run completed 500 descriptions: all 255 through order seven and 245 of 256 at order eight, stopping during (n,r,d)=(8,6,(5,6)) because its wall budget expired. It therefore does not establish a complete order-eight range. Run records bind versions, actual exit codes, resource budgets and source/output hashes. These generator executions are not trusted verifier receipts and do not exhaust continuous optimal dual faces.

First open lemma: given an exact fractional packing of an arbitrary six-divisible normal form in Section 3, construct an integer packing with loss at most K*n for a universal K, while assigning each retained core edge globally once. Neither (3) nor (5) supplies that construction. The false zero-loss parity shortcut in Section 4 is excluded; the main nested O(n) goal is not declared false. The next atomic action is to formulate and attack a laminar palette/core-edge allocation rule on these normal forms, with a nonzero global rounding allowance, before extending anything to clique-tree intervals.

Historical C24 proof and separator candidates are unchanged. The o(n^2) theorem remains source-backed/proof-drafted. No admission, root closure, independent-verifier identity, or Result is asserted. Status: NONTERMINAL_CHECKPOINT.
