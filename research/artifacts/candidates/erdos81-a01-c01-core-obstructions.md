# Erdős 81: complete-split benchmark, local obstructions, and clique number at most three

Candidate ID: `candidate:erdos81-a01-c01-core-obstructions`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `fff9c7ba9cba18ecfbadd1b70b61edf67b073947`
Verdict: `candidate_only`
Method: natural-language proof draft and explicit finite witnesses. No enumeration, solver, or proof assistant was run. No novelty claim.

## 1. Frozen statements and scope

All graphs are finite and simple. A chordal graph has no induced cycle of length at least four. A split graph admits a vertex partition C union I with C a clique and I a set of pairwise nonadjacent vertices. The quantity cp(G) is the minimum number of complete subgraphs with nonempty, pairwise disjoint edge sets whose union is E(G); cp of an edgeless graph is zero. Vertices of partition members may overlap. A cover, denoted cc, may repeat edges and is not a partition.

The admitted target asks whether, for every integer n and every n-vertex chordal G, some n-vertex split H has cp(H) >= cp(G). The results below prove this only for clique number at most three and exhibit counterexamples only to two stronger local rules. The original bound n^2/6+O(n) and the unrestricted reduction both remain open in this candidate.

Allowed axioms are finite-graph-basic, finite-combinatorics, and real-arithmetic. The only external structural theorem used is the perfect-elimination-ordering characterization of chordal graphs; see source note S3, Section 2. We do not transfer a biclique-partition theorem to cp.

## 2. Atomic claim C01.1: a signed edge-weight lower bound for split graphs

Let H have split partition C union I, |C|=k, and a crossing-edge count a=e(C,I). Assign weight +1 to a crossing edge and -1 to an edge inside C. Every clique with an edge has weight at most one. Indeed, a core-only clique on s vertices has weight -binom(s,2). A clique with one vertex of I and s>=1 core vertices has weight s-binom(s,2), which is at most one. A clique cannot contain two vertices of I.

Summing these weights over any edge partition gives
    cp(H) >= a - binom(k,2).
Negative weights are permitted because this is an exact partition, and every edge is counted exactly once. This argument would not establish the same lower bound for an overlapping cover.

## 3. Atomic claim C01.2: an exactly attained complete-split benchmark

Let J(k,t) be the join of a k-clique and t pairwise nonadjacent vertices. For k>=1 and t>=k,
    cp(J(k,t)) = kt - binom(k,2).

The preceding lower bound supplies one direction. For the other, partition E(K_k) into at most k matchings and assign distinct matching classes to distinct vertices of I. For each edge uv in the class assigned to x, use the triangle xuv. Use every remaining crossing edge as a two-vertex clique. Within a class its edges are a matching, so no crossing edge repeats; different classes use different vertices of I. All core edges occur exactly once. There are binom(k,2) triangles and kt-2*binom(k,2) remaining edges, giving the claimed count.

Here is an explicit matching decomposition, so no unreported edge-coloring algorithm is needed. For odd k>=3, use vertices Z_k and color uv by (u+v)/2 modulo k. Division by two is valid since k is odd; each color is a matching. For even k>=2, use vertices {infinity} union Z_(k-1). Color c has the edge {infinity,c} and pairs {c+j,c-j}, 1<=j<=(k-2)/2. These are k-1 matchings: every pair of finite vertices has a unique midpoint in the odd cyclic group. For k=1 the core has no edges.

Define B(n)=floor(n(n+1)/6). For every n>=1 there is an n-vertex split graph with cp equal to B(n). For n=1 take an isolated vertex. Otherwise take
    k=floor((n+1)/3), t=n-k.
Then t>=k and the preceding formula applies. Writing n=3q, 3q+1, or 3q+2 gives respectively
    (3q^2+q)/2, (3q^2+3q)/2, (3q^2+5q+2)/2,
which equals B(n). These are integer expressions in their respective cases.

This proves an attained lower benchmark for the maximum over all split graphs, not an upper bound for all split graphs. A chordal graph with cp>B(n) alone would not disprove the admitted target.

## 4. Atomic claim C01.3: reduction for chordal graphs with clique number at most three

For n>=4, every chordal G with omega(G)<=3 satisfies
    cp(G) <= 2n-5 = cp(J(2,n-2)).
The graph on the right is split and has the same order.

To prove the upper bound, take a perfect elimination ordering. Each vertex has at most two later neighbors, the penultimate vertex at most one, and the last vertex none. Thus m=|E(G)|<=2n-3. If G has a triangle, use that triangle and every other edge singly, obtaining at most m-2<=2n-5 cliques. If G is triangle-free, chordality implies it is a forest: a shortest cycle in any graph is induced, and here neither a triangle nor a longer induced cycle is allowed. Hence m<=n-1<=2n-5, and every edge singly suffices. Formula C01.2, or the direct argument below, gives cp(J(2,n-2))=2n-5.

In J(2,t), all triangles contain the single core edge. At most one triangle can occur in an edge partition, no clique is larger, and the graph has 2t+1 edges. One triangle plus all other edges therefore attains the minimum 2t-1 for t>=1.

For n=1,2,3, direct classification gives cp(G)<=n-1, attained by the star on n vertices (and the isolated vertex for n=1). The possible triangle on three vertices has cp=1. If order zero is included, the empty split graph handles it.

## 5. Atomic claim C01.4: adding a chordal-safe completion edge can decrease cp

Use vertices 1,2,3,4,5 and G=P5 with edges 12,23,34,45. This is a tree and cp(G)=4. Its induced subgraph on {1,2,4,5} is 2K2; a split graph cannot contain induced 2K2, since its clique side would need to meet both disjoint edges and would create a forbidden cross edge. Thus G is not split.

Add only edge 24 to obtain H. It is split with C={2,3,4}, I={1,5}, and is chordal: its only cycle is the central triangle. Its partition is {12}, {234}, {45}, so cp(H)<=3. The two pendant edges cannot be members of any larger clique, and the central triangle has edges, so cp(H)>=3.

Consequently n and chordality are preserved but cp drops from four to three. This excludes the rule that making a chosen core into a clique by chordal-safe edge additions never lowers cp. It does not exclude all possible split choices: the same-order star K_(1,4) has cp=4.

The smaller nonsplit chordal witness 2K2 on four vertices has cp=2 and is dominated by the four-vertex star with cp=3; it is not a counterexample to the target either.

## 6. Atomic claim C01.5: deleting a maximal clique's edges need not preserve chordality

Let G=J(2,3), with core a,b and other vertices x,y,z. All three maximal cliques are abx, aby, abz. Delete the three edges of the maximal clique abx, but keep all vertices. The residual graph is a-y-b-z-a plus isolated x, an induced four-cycle. Hence it is not chordal.

The three maximal triangles form a cover, not a partition, because they all share ab. In this example cc(G)=3: each of x,y,z requires a distinct covering clique, and the three triangles suffice. By C01.3's book calculation, cp(G)=5. This is an explicit guard against interpreting a maximal-clique cover as a partition or applying chordal induction to an edge-deleted residual.

## 7. Reuse, attack pass, and unresolved obligations

Source provenance and statement comparisons are in `research/artifacts/source-notes/erdos81-a01-c01-source-faithfulness.md`. The complete-split family is classical prior art; the calculation above is a self-contained reconstruction, not a novelty assertion.

Manual attacks included edgeless cases; n=1,2,3,4; odd/even core sizes in the matching decomposition; overlapping triangle edges in the book; and the existential quantifier in the P5 witness. No finite exhaustive test is claimed.

The unrestricted target and root remain open. The root also requires a universal upper bound for all split graphs if this reduction is used; merely proving the reduction and the attained lower benchmark does not supply that missing implication.

Next bounded step on the same admitted target: sharpen the chordal edge-count bound when omega=4, with explicit clique/triangle packing witnesses, and use B(n) to exclude small parameter pairs. Verification requests must separately audit the structural theorem reuse, the witness edge lists, partition disjointness, and statement scope.
