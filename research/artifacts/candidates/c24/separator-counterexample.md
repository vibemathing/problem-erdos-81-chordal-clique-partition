# C24: a separator-capacity counterexample and a valid additive repair bound

Verdict: candidate_only. Exact mathematical certificates follow; no trusted verifier or admission is claimed.

## A. A false local lemma

The claim that triangle-packing integrality gaps simply add under clique sums is false, even when each constituent has gap zero and the common separator consists of one edge.

Let G have vertices 1,...,8, all 21 pairs in {1,...,7}, and the two further edges 18 and 28. Its maximal cliques are exactly {1,...,7} and {1,2,8}. This is a chordal graph: vertex 8 is simplicial and its deletion leaves a complete graph. It is the clique sum of K7 and K3 along edge 12.

For K7, the seven triangles

    123,145,167,246,257,347,356

partition all edges. Thus nu(K7)=nu_star(K7)=7. The triangle K3 has both packing parameters one. Both constituent gaps are zero.

For G, the same seven core triangles form an integer packing. Since G has 23 edges, no integer packing has more than floor(23/3)=7 triangles. Hence nu(G)=7.

For its fractional certificate give triangle 128 weight one. Put R={3,4,5,6,7}. Give each triangle consisting of one of {1,2} and two vertices of R weight 1/4. Give each triangle entirely in R weight 1/6. Give all remaining triangles weight zero. These are all the positive-weight families; G has no triangle involving 8 except 128. Each edge from {1,2} to R occurs in four mixed triangles, so has load one. An edge within R receives 2*(1/4) from mixed triangles and 3*(1/6) from internal triangles, again load one. Edges 12,18,28 are covered by 128. The total fractional value is

    1 + 2*C(5,2)/4 + C(5,3)/6 = 23/3.

Summing edge capacities proves the matching upper bound. Consequently

    nu_star(G)=23/3, nu(G)=7, delta(G)=2/3,
    delta(K7)+delta(K3)=0.

The gap inequality delta(G)<=delta(K7)+delta(K3) has the explicit mismatch 2/3<=0.

The clique partition number of G is three: use K7, edge 18, and edge 28. It cannot be one because G is not complete. A two-clique exact edge partition would have pieces intersecting in at most one vertex; otherwise the common edge would repeat. If the pieces are disjoint the graph is disconnected; if they meet at one vertex that vertex is a cut vertex. But G is connected with no cut vertex: after removing 1 or 2, vertex 8 still attaches to the other, and all other deletions leave the core connected. Thus cp(G)=3.

All nonempty-edge cliques are the subsets of {1,...,7} of size at least two, together with 18,28,128; edge 12 is already in the first family. All triangles are the 35 core triples and 128. This description is exhaustive. The minimum order among all possible chordal clique-sum counterexamples is not asserted without a complete separator scan. Within the displayed family the graph is fully explicit.

## B. The repair inequality that is valid

Let a graph be formed as a tree of pieces G_i, where parent and child intersect in a clique S_i, with no edges between private parts, and vertex occurrences have running intersection. Every triangle lies in at least one piece. Assign the triangles of a fractional packing to containing pieces. The assigned packing in each piece is feasible, so nu_star(G)<=sum_i nu_star(G_i).

Select an integer packing in each piece. When adding a child, discard its packed triangles that meet an already used separator edge. At most C(|S_i|,2) triangles are discarded, because each separator edge belongs to at most one triangle in that packing. No other edge can conflict. Thus

    delta(G) <= sum_i delta(G_i) + sum_nonroot_i C(|S_i|,2).       (1)

An empty or one-vertex separator costs zero. This is an explicit additive bound on the rounding loss, rather than an unproved subadditivity rule. Section A shows that the extra term cannot always be omitted even at an edge separator.

## C. Near-complete-split pieces

For J(r,t)=K_r joined to an independent set of t vertices, t>=r-1, the signed/fractional certificate gives nu_star=C(r,2). A round-robin edge coloring of K_r lifts matching classes to mixed triangles. If r is even or t>=r, all core edges are used and the packing gap is zero. If r is odd and t=r-1, omitting one near-perfect matching loses at most (r-1)/2. Denote this bound gamma(r,t); always gamma<=(r+t-1)/4.

If G_i differs on the same vertex set from such J(r_i,t_i) by d_i edge additions and deletions, then delta(G_i)<=gamma(r_i,t_i)+d_i. To see this, at most one integer packed triangle is destroyed per deleted edge. From any fractional packing, removing the triangles that contain an added edge removes at most one unit of mass per added edge. The surviving fractional packing lies in the original J. Neither argument assumes that arbitrary edge deletion preserves chordality.

Substituting in (1), and using n=sum_i |V(G_i)|-sum_i |S_i|, proves a uniform O(n) gap for any such tree of pieces with sum_i d_i+sum_i |S_i|^2=O(n). All constants are independent of the number of pieces once that total budget is fixed. The general existence of such a budgeted decomposition for chordal near-extremizers is NOT proved here.

## D. Remaining target

These constructions do not contradict the global conjectural O(n) gap: both counterexamples to the local shortcuts have only linear or constant gaps. They also do not contradict C22's necessary low-core conditions, which concern integer near-extremizers, not this far-from-extremal graph. The root, universal gap theorem and trusted admission remain open. The next atomic obligation is to bound shared large-separator capacity costs in near-extremal chordal graphs without assuming a linear graph-edit budget.
