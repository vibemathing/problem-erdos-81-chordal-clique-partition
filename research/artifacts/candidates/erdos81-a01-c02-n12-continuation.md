# Erdős 81: candidate domination through twelve vertices

Candidate ID: `candidate:erdos81-a01-c02-n12-continuation`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base used for this draft: `38ea689d964191e0ce5d72c40410ec7800770b53`
Verdict: `candidate_only`
Status: natural-language continuation draft awaiting full packet binding and external verification. No enumeration, solver, proof assistant, or local Harness run is claimed. No novelty claim.

## Frozen scope and prerequisites

All graphs are finite and simple. The quantity cp counts a partition of the edges into complete subgraphs with pairwise disjoint nonempty edge sets; vertices of different pieces may coincide. Split means a clique together with a set of pairwise nonadjacent vertices. The unrestricted target and the original asymptotic question remain open.

This draft proposes two restricted conclusions: every chordal graph of order at most twelve has a same-order split graph with cp at least as large; the same statement holds at every order for clique number at most four. These are not exhaustive computational results.

Reuse: `research/artifacts/candidates/erdos81-a01-c01-core-obstructions.md` at base `38ea689d964191e0ce5d72c40410ec7800770b53` constructs a split graph of each order n with cp equal to B(n)=floor(n(n+1)/6), and handles clique number at most three. That benchmark is only an attained value, not an upper bound for all split graphs. The accompanying C01 source note supplies the chordal perfect-elimination-ordering and clique-tree characterization. Allowed axioms remain finite-graph-basic, finite-combinatorics, and real-arithmetic.

A perfect elimination ordering can be chosen to end in any prescribed maximum clique C. One justification is to root a clique tree at C and eliminate a vertex belonging exclusively to a leaf clique other than C; such a vertex is simplicial. Repeat, handling disconnected components first when necessary. The running-intersection property ensures that a vertex in a leaf clique but not its neighbor belongs to no other maximal clique. This is the only structural theorem reuse beyond C01.

## 1. Degree deficit and an elementary packing bound

Let r=omega(G), k=r-1, t=n-r, and fix a maximum clique C. Choose a perfect elimination ordering ending in C. For the t outside vertices let d_i be their numbers of later neighbors. Then d_i<=k, and

    m=binom(r,2)+sum_i d_i=binom(r,2)+kt-Delta,
    Delta=sum_i(k-d_i)>=0.

The integer Delta is independent of the chosen maximum clique. Using C once and every other edge singly gives

    cp(G)<=kt+1-Delta.                                    (1)

If there is a triangle with at least two vertices outside C, its edges are disjoint from E(C), and

    cp(G)<=kt-1-Delta.                                    (2)

There is no assertion that the remaining graph is chordal after these pieces are selected: all remaining edges are used singly.

If G is not split, G-C contains an edge. In the absence of any triangle with at least two outside vertices, the earlier endpoint u of any outside edge has d_u=1. Otherwise its later-neighbor clique supplies such a triangle. Consequently Delta>=k-1 in that case. For r>=4, (1) and (2) therefore imply

    cp(G)<=kt-1.                                         (3)

An outside K4 saves five pieces relative to its six edges taken singly. Two edge-disjoint triangles save four; three edge-disjoint triangles save six. All these savings can be combined with the use of C when the selected pieces contain at most one vertex of C.

## 2. Two outside edges in the zero-deficit case

Assume Delta=0, G is not split, and r>=5. Every outside vertex has d_i=k. There is a maximum clique C for which G-C has at least two edges.

Proof. Start with any maximum clique. Zero outside edges would make G split. Suppose the only outside edge is uv, oriented with u earlier than v. Then v has k core neighbors and u has k-1 core neighbors, the latter contained in the former. Thus, for distinct a,b in C,

    N_C(v)=C-{a},  N_C(u)=C-{a,b}.

Every other outside vertex z is isolated in G-C and has N_C(z)=C-{c_z}. If every c_z=a, then (C-{a}) union {v} is a split core: its complement consists of a,u and the other outside vertices, with no edges. Otherwise choose z with c_z!=a and use the maximum clique (C-{c_z}) union {z}. Its complement contains the two edges uv and vc_z. This proves the claim, including the case with no other outside vertex by the vacuous first alternative.

Every edge of a zero-deficit graph lies in an r-clique: take the earlier endpoint in the chosen ordering, or use C for a core edge. If G-C has an outside K4, take it. Otherwise any r-clique containing an outside edge has at most three outside vertices, so that edge has at least r-3>=2 common neighbors in C. Select any two distinct outside edges. If they meet, choose different common core neighbors; if disjoint, any choices work. The resulting two triangles are edge-disjoint and avoid core edges. Hence

    Delta=0, r>=5, G nonsplit  =>  cp(G)<=kt-3.            (4)

## 3. Three outside edges in the zero-deficit case

Assume additionally t>=5. Some maximum clique C has at least three outside edges.

Proof. Suppose instead that the maximum number of outside edges over all maximum cliques is two. Section 2 allows choosing C with exactly two. On t>=5 outside vertices, this two-edge graph has an isolated vertex z. It has k core neighbors, so write N_C(z)=C-{a}. Replacing a by z in the core changes the outside edge count from two to two+deg_{G-C}(a), where this degree denotes the number of neighbors of a among the original outside vertices. Maximality of the count forces a to be adjacent to none of them. Every isolated outside vertex therefore misses the same a.

The two outside edges form either a matching or a path of length two. In a perfect elimination ordering, an outside forest is oriented toward a unique root in each nontrivial component: each vertex has at most one later outside neighbor, and each tree has one sink. A root has core neighborhood C-{a}. A nonroot has core neighborhood C-{a,b} for some b; along an edge joining two nonroots these neighborhoods agree, by containment and equal size.

For two disjoint edges, choose one oriented edge u->v with v its component root. The clique D=(C-{a,b}) union {u,v} is maximum. Its complement contains ab, the other outside edge wx, and bx, where x is the other component root. These are three distinct edges, a contradiction.

For a path with its root at the middle vertex v, (C-{a}) union {v} is already a split core, a contradiction. If its root is an endpoint w, write the path u->v->w. The nonroots u,v have the same core neighborhood C-{a,b}. The maximum clique D=(C-{a,b}) union {u,v} has outside edges ab, bw, and bz for an original isolated outside vertex z. Again there are three. This proves the claim.

For r>=6, if an outside K4 exists it supplies a saving of five. If not, each outside edge has at least r-3>=3 common core neighbors. Choose three outside edges and successively assign common core neighbors, forbidding a previously assigned neighbor only when the two outside edges meet. At each step at most two choices are forbidden. The three resulting triangles are pairwise edge-disjoint. Thus

    Delta=0, r>=6, t>=5, G nonsplit => cp(G)<=kt-4.        (5)

The weaker saving of five in the K4 alternative is intentional.

## 4. One unit of deficit

Assume Delta=1, r>=6, t>=3, and G is not split. Some maximum clique has at least two outside edges.

Suppose a chosen core has exactly one outside edge u->v. There is a unique outside vertex q of later degree k-1; all others have later degree k.

If q=u, then N_C(v)=C-{a}, and N_C(u) is a subset thereof of size k-2. All other outside vertices have k core neighbors. If they all miss a, replacing a by v produces a split core. Otherwise an isolated outside vertex z misses c!=a, and the core C-{c}+{z} leaves both uv and vc outside.

If q=v, the core neighborhoods of u and v both have size k-1 and agree, say S=C-{a,b}. The maximum clique S union {u,v} leaves a,b and at least one other outside vertex z. Such z has k core neighbors, so it is adjacent to at least one of a,b. Together with ab this gives two outside edges.

If q is isolated outside C, write N_C(v)=C-{a} and N_C(u)=C-{a,b}. If no other outside vertex is adjacent to a, replacing a by v produces a split core. Otherwise some outside z is adjacent to a; the maximum clique (C-{a,b}) union {u,v} leaves ab and az outside.

These alternatives prove the assertion. Every edge now lies in a clique of size at least r-1>=5, because every outside later degree is at least k-1. If there is no outside K4, each outside edge has at least two common core neighbors. The two-triangle packing of Section 2 applies, giving

    Delta=1, r>=6, t>=3, G nonsplit => cp(G)<=kt-4.        (6)

The condition t>=3 is necessary for this argument; it is not silently removed.

## 5. Two units of deficit: the twelve-vertex central cases

Here (n,r) is either (12,6) or (12,7), so (k,t) is respectively (5,6) or (6,5), and kt=30. Assume Delta=2.

If a maximum clique C leaves at least two outside edges, use the following packing. Every outside later degree is at least k-2>=3. If the outside graph has a triangle, its earliest vertex and its later-neighbor clique extend that triangle to a K4 containing at most one core vertex. This saves five. If the outside graph is triangle-free, the earlier endpoint of an outside edge has at most one later outside neighbor and hence at least two later core neighbors common with the other endpoint. Two outside edges therefore give two edge-disjoint triangles. In either case (1) improves by at least four and gives cp(G)<=25.

It remains to treat the possibility that every maximum clique leaves exactly one outside edge. Choose C and write that edge u->v. At least one isolated outside vertex z has later degree k: there are t-2>=3 such isolated vertices and only two units of deficit. Write N_C(z)=C-{a}. Replacing a by z leaves the existing uv and every edge from a to the original outside vertices. The assumed maximum of one outside edge forces a to be adjacent to none of the outside vertices. All healthy isolated outside vertices therefore miss a.

Write d_u=k-delta_u and d_v=k-delta_v. The containment N_C(u) subset N_C(v) yields delta_v<=delta_u+1. If delta_v=0, replacing a by v is a split core, impossible. Since total deficit is two, delta_v>=1 leaves only delta_v=1 and delta_u in {0,1}.

If delta_u=0, then N_C(u)=N_C(v)=C-{a,b}. The maximum clique (C-{a,b}) union {u,v} leaves ab and bz, two outside edges, impossible.

Thus delta_u=delta_v=1, all other outside vertices are healthy, and for distinct a,b,c in C,

    N_C(v)=C-{a,b},  N_C(u)=C-{a,b,c}.

Let K=C-{a}, a k-clique. The vertex a and the t-2 healthy outside vertices form s=t-1 pairwise nonadjacent vertices, each complete to K. The remaining vertices are v, adjacent to k-1 vertices of K, and u, adjacent to k-2 vertices of K and to v. No additional outside edges occur.

For k=5,t=6, the five universal vertices permit using all five matching classes of K5 in the triangle construction from C01. Ten triangles save twenty pieces relative to all edges singly. Here m=binom(6,2)+30-2=43, so cp(G)<=23.

For k=6,t=5, the four universal vertices permit using four of the five perfect matching classes of K6. These twelve triangles save twenty-four pieces. Here m=binom(7,2)+30-2=49, so cp(G)<=25.

This also handles the exceptional one-outside-edge shape, without assuming that completion preserves cp.

## 6. The no-triangle exceptional case at order twelve

For (n,r)=(12,6), suppose Delta=4 and a chosen maximum clique C has no triangle with at least two outside vertices. An outside edge has earlier endpoint u with d_u=1. This uses all four units of deficit; every other outside vertex has later degree five. Every outside edge must start at u, since any other starting vertex would create such a triangle. Thus the only outside edge is uv, u has no core neighbor, and v has core neighborhood C-{a}. The other four outside vertices each miss exactly one core vertex.

If they all miss a, replacing a by v makes the graph split. Otherwise choose z with core neighborhood C-{b}, b!=a. For C'=(C-{b}) union {z}, vertices b and v are outside and have a common core neighbor c in C-{a,b}. The triangle bvc avoids all edges of C'. Apply (2) at the unchanged deficit to get cp(G)<=30-1-4=25.

For Delta>=5, the elementary bound (1) already gives cp(G)<=26. For (n,r)=(12,7), absence of such a triangle forces Delta>=5 and (1) again gives at most 26.

## 7. Parameter audit and restricted conclusion

For nonsplit graphs with r<=3, C01 gives a same-order split comparison; its bound 2n-5 is at most B(n) for n>=4. Orders zero through three are handled directly. For r=4, (3) gives 3n-13, which is at most B(n): n(n+1)/6-(3n-13)=((n-8)(n-9)+6)/6>=1 for integer n. Thus the target holds for every graph with clique number at most four, at every order.

For n<=9 and r>=4, (3) suffices. Indeed kt=(r-1)(n-r)<=floor((n-1)^2/4); at n=6,7,8,9 the resulting upper bounds kt-1 are at most 5,8,11,15, whereas B(n) is 7,9,12,15. Smaller nonsplit graphs cannot have r>=4 and n<=5.

At n=10, B(n)=18. The only r>=5 not settled immediately by (3) are r=5,6, both with kt=20. Delta=0 is settled by (4). If Delta>=1 and a triangle avoids core edges, (2) gives at most 18. Without such a triangle, Delta>=k-1>=3, and (1) gives at most 18.

At n=11, B(n)=22. The only remaining clique numbers are r=5,6,7. For r=5,7, kt=24: use (4) when Delta=0, (2) when Delta>=1, and Delta>=k-1 in the no-triangle case. For r=6, kt=25: use (4) when Delta=0, (6) when Delta=1, and (2) when Delta>=2. The no-triangle case has Delta>=4, so (1) gives at most 22.

At n=12, B(n)=26. The only remaining clique numbers are r=5,6,7,8. For r=5,8, kt=28: (4) handles zero deficit, (2) handles positive deficit with a triangle, and Delta>=k-1 handles its absence. For r=6,7, kt=30: (5) handles zero deficit, (6) handles one unit, Section 5 handles two units, and (2) handles Delta>=3 when a triangle avoids core edges. Section 6 handles its absence.

Accordingly every nonsplit chordal graph of order at most twelve satisfies the candidate bound cp(G)<=B(n). Choose the complete split benchmark from C01. If G is already split, choose H=G; no upper bound for arbitrary split graphs has been assumed. This proves the stated restricted domination claim within this draft, not the unrestricted target.

## Attack pass, limitations, and continuation

The proof explicitly checks: matching versus incident outside edges; the shared-crossing-edge risk when constructing triangles; parity in the reused round-robin construction; the exceptional t=2 case excluded from Section 4; a maximum clique rather than merely an inclusion-maximal clique; zero deficit versus one or two missing forward incidences; and the distinction between cp>B(n) and an actual counterexample to domination over all split graphs.

All conclusions remain candidate-only pending verification of the arguments and of the source-to-statement correspondence. No mathematical execution or mathematical receipt is asserted. The target and root remain open. Proposed next bounded task: audit the degree-deficit case analysis and investigate order thirteen, where the central clique numbers r=6,7,8 require stronger packing or a bounded exact-search plan. No new obligation ID is admitted by this prose.
