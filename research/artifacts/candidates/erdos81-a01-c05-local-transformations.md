# Erdős 81 C05: two local transformation failures and an exact split model

Candidate ID: `candidate:erdos81-a01-c05-local-transformations`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `d292a22052a0622aaa8af163b6f6742d9766b6a1`
Verdict: `candidate_only`.
Method: explicit finite graphs, written optimality arguments and a finite variational identity. No mathematical code, enumeration, solver or proof assistant was run. No minimality or novelty claim.

## 1. Frozen scope

All graphs are finite and simple. cp means an exact edge partition into complete subgraphs; different pieces may share vertices but never edges. The admitted target is existential: some same-order split H must dominate each chordal G. A failure of a specified transformation is not a counterexample to that target. The root and the unrestricted target remain open.

This cycle excludes two more proposed local rules, in addition to the completion and residual-chordality failures in C01. The main admitted route is not declared unsuccessful. Source attribution is in `research/artifacts/source-notes/erdos81-a01-c05-transformation-sources.md`. Allowed axioms remain finite-graph-basic, finite-combinatorics, and real-arithmetic.

## 2. C05.1: adjacent edge migration can lower cp in both orientations

Let the vertex set be {u,v,s,t,a,b}. Let G have the six edges of the core clique {u,v,s,t} and the four extra edges
    ua, as, vb, bt.
There are no other edges. Let H be obtained by deleting ua and adding va. Both graphs have six vertices, ten edges and clique number four. Both are split with the same core and the two nonadjacent vertices a,b, hence chordal.

This is the Kelmans move with beneficiary v and co-beneficiary u: the only neighbor of u that is neither v nor a neighbor of v is a. The operation agrees with the primary definition identified in source K1; no cp monotonicity theorem is imported from that source.

The exact values are
    cp(G)=5,  cp(H)=4.

For G, the core K4 and the four extra singleton edges give five pieces. Any partition using that K4 has at least five pieces, since the edges at a and b cannot then be put in triangles without repeating a core edge. If the K4 is not used, every piece has at most three vertices. The only triangles not wholly inside the core are uas and vbt. At most one core triangle can be used, because any two core triangles share an edge. If both noncore triangles are used, their core edges us and vt are disjoint and the remaining core is a four-cycle, so no core triangle is available. Thus at most two triangles can occur in a partition without K4, and such a partition has at least 10-2*2=6 pieces. This proves cp(G)=5.

For H, the four pieces
    {v,a,s}, {v,b,t}, {u,s,t}, {u,v}
form an exact partition, with the last piece a K2. A partition without K4 contains at most three triangles, hence at least 10-2*3=4 pieces. A partition using K4 needs at least five. Therefore cp(H)=4.

The reverse orientation applied to the original G deletes vb and adds ub. Its result is isomorphic to H by swapping u and v, so it too has cp=4. Choosing the orientation of this particular edge does not restore nondecreasing cp.

To restrict the input to nonsplit chordal graphs, take disjoint unions with one additional K2. The resulting eight-vertex graphs are chordal and nonsplit: selecting one edge from each component induces 2K2. cp is additive across components, since a clique with an edge cannot span components. The same move then lowers cp from six to five. This variant is not claimed connected or minimal.

## 3. C05.2: PEO color folding lowers cp on a connected nonsplit input

Let G=P6 squared, with vertex set {1,2,3,4,5,6} and exact edge list
    12, 13, 23, 24, 34, 35, 45, 46, 56.
The ordering 6,5,4,3,2,1 is a PEO: each vertex's later neighbors are a clique. Thus G is chordal. Vertices {1,2,5,6} induce 2K2, so G is not split.

Its four triangles are exactly
    123, 234, 345, 456.
Successive triangles in this list share an edge. Any three of the four include a successive pair, and no K4 exists, so at most two triangles occur in an edge partition. Using 123 and 345 together with edges 24,46,56 gives five pieces. Hence cp(G)=9-2*2=5.

Take the terminal maximum clique Q={1,2,3} as color representatives. Reverse-PEO greedy coloring assigns
    color(1)=1, color(2)=2, color(3)=3,
    color(4)=1, color(5)=2, color(6)=3.
A proposed folding keeps Q, makes {4,5,6} pairwise nonadjacent, and replaces each outside vertex's later neighbors by their Q color representatives. It gives H with core 123 and neighborhoods
    N_H(4)={2,3}, N_H(5)={1,3}, N_H(6)={1,2}.
This explicitly defined graph is the 3-sun. It is split and has the same six vertices, nine edges and clique number three as G.

The triangles 234,135,126 partition all nine edges of H. No clique has more than three edges, so cp(H)>=9/3=3, and cp(H)=3. Thus this PEO folding lowers cp from five to three, despite preserving order, edge count, clique number and chordality.

This does not contradict the admitted target. For example, the six-vertex complete split graph J(2,4) from C01 has cp=7 and dominates G.

## 4. C05.3: an exact finite model for a fixed split core

Let H be any split graph with fixed partition C union I, with C a clique and I pairwise nonadjacent. For each x in I, choose a set partition P_x of N_H(x) into nonempty blocks. If N_H(x) is empty, P_x is the empty family. Require the core-edge sets E(K_S), over every block S of every P_x, to be pairwise disjoint.

Let L be the graph on C with edge set
    E(K_C) minus the union of E(K_S) over these blocks.
Then the following identity holds:
    cp(H) = min_(admissible families (P_x)) [sum_(x in I) |P_x| + cp(L)].

Proof. In any edge partition of H, each clique meeting I has exactly one I vertex x. Its other vertices form a block S. Each edge xy with y in N_H(x) occurs exactly once, so the blocks for x partition its neighborhood. No core edge can occur twice, giving the stated disjointness condition. The cliques not meeting I partition precisely L. This proves that every partition has size at least the minimum expression.

Conversely, from any admissible family use the cliques {x} union S and an optimal edge partition of L. Every crossing edge occurs once; every spent core edge occurs once; the remaining core edges are exactly L. Thus the assembled family is an edge partition with the displayed size. There are finitely many families, and the all-singleton choice is feasible, so the minimum exists.

The residual graph L need not be chordal. In C05.1, using both noncore triangles of G spends opposite core edges us,vt, leaving C4; doing the analogous operation in H spends adjacent core edges vs,vt and leaves a core triangle plus one edge. Neighborhood degrees or clique counts alone therefore do not capture the partition cost.

## 5. Method-failure proposals and next obligation

Proposed excluded local rules, with evidence entirely in this artifact:
- Adjacent Kelmans moves are cp-nondecreasing, or one of the two orientations is always cp-nondecreasing: contradicted by C05.1.
- Folding all later neighbors onto the color representatives of a terminal PEO clique produces a same-order split dominator: contradicted by C05.2.

These proposals concern local methods only. They do not retire `route:split-extremal-reduction-v1`; no canonical failed-route record is written, and neither witness satisfies the negation of the admitted target.

For a future bounded exact search, C05.3 supplies a precise finite model. Such a search would still need a valid lower certificate for cp(G) and an upper certificate for every split graph of the same order before producing a target counterexample. No search has been executed here.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: C04 for the restricted positive result, this artifact for explicit local obstructions.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
Next action: continue the deficit-based proof, not either excluded local monotonicity rule; freeze the order-twelve classification and investigate a uniform clique-number-six bound.
