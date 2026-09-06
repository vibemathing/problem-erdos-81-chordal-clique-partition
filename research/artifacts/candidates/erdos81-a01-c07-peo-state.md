# C07: deficit completion, perturbation cost, and exact PEO state

Candidate ID: `candidate:erdos81-a01-c07-peo-state`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `543fcc32f04426b01b1d8b8abf94b4ae7d193855`
Verdict: `candidate_only`.

## 1. Scope and inputs

All graphs are finite and simple. cp partitions edges exactly once into nonempty complete subgraphs; shared vertices are allowed. The unrestricted same-order split-domination target and the root n^2/6+O(n) bound remain open.

C04 supplies a written PEO ending in a chosen maximum clique. C05 supplies the exact split-core model. C06 supplies the deficit identity and the obstruction to always retaining an intact maximum clique. These are candidate dependencies, not verification receipts. The structural PEO characterization is scoped in C01 source S3. The proofs below are constructive finite arguments using finite-graph-basic, finite-combinatorics, and real-arithmetic. No mathematical program, graph enumeration, solver, or proof assistant was executed.

Write r=omega(G)>=2, k=r-1, n=|V(G)|, and
    delta=kn-binom(k+1,2)-|E(G)|.
A k-tree here starts with K_(k+1) and adds vertices one at a time adjacent to exactly an existing k-clique.

## 2. C07.1: exactly delta fill edges suffice

Every chordal G as above is a spanning subgraph of a k-tree T with exactly delta added edges. In particular, T has the same order and the same clique number as G.

Take a PEO ending in a fixed r-clique Q, and build T in reverse order, starting with Q. When adding v, its original later neighbors S are a clique of size d_v<=k. They remain a clique in the already constructed supergraph. Every clique in a k-tree lies in a maximal clique of size k+1: this follows by induction on the construction, since adding a vertex on a k-clique creates one new maximal (k+1)-clique and does not destroy any old maximal clique. Thus S can be extended to a k-clique in the current T. For S empty choose any k-clique. Add v adjacent to that k-clique.

This includes all original edges incident to later vertices and adds exactly k-d_v new ones. Each edge is considered only at its earlier original PEO endpoint. Since the terminal Q has all its edges,
    sum_(v outside Q)(k-d_v)=delta.
The construction therefore adds precisely delta edges. It works for disconnected G as well; the supergraph T need not preserve its components. No claim that this completion increases cp is made.

## 3. C07.2: a quantified edge-deletion perturbation bound

Let T be any graph with clique number at most r>=2, and let G=T-F for a set F of q edges. Then
    cp(G) <= cp(T)+(r-2)q.                                  (1)

Start with an optimal edge partition of T. Delete the edges of F in any fixed order. If the piece containing the next deleted edge uv is a K_s with s>=3, replace that piece after deleting uv by the clique on all its vertices except u and the s-2 singleton edges from u to its other neighbors. These s-1 pieces partition K_s-uv, increasing the number of pieces by s-2<=r-2. If s=2, just remove its one-edge piece; the count decreases by one. Other pieces are untouched. At every stage the pieces are still cliques and no edge is repeated, so the operation can be iterated.

More precisely, each deletion from a piece of size s contributes at most s-2, with a negative contribution when that piece is K2. Thus an application may use actual affected-piece sizes instead of the worst-case r-2. Formula (1) is a uniform one-sided comparison, not a Lipschitz assertion in the other direction.

Combining Sections 2 and 3 gives a constructive general-deficit reduction:
    cp(G) <= cp(T)+(r-2)delta,                              (2)
for some same-order zero-deficit chordal T.

Conditional consequence, with the missing hypothesis explicit: if a uniform bound cp(T)<=n^2/6+C_0 n were proved for ALL k-trees, with C_0 not depending on k, then every chordal graph with delta<=D would satisfy cp(G)<=n^2/6+(C_0+D)n. For delta=o(n), (2) would transfer the leading coefficient with an o(n^2) error, not necessarily the required O(n) error. For growing delta of order n or more, (2) alone is not enough. No bound for all k-trees is proved or assumed as a conclusion here.

## 4. C07.3: exact residual-edge PEO recurrence

Fix a PEO v_1,...,v_n of the ORIGINAL graph G. At step i write W_i={v_i,...,v_n}. A state F is a subset of E(G[W_i]) already used by pieces with an earlier pivot. Define the residual neighbor set
    R_i(F)={v_j : j>i and v_i v_j belongs to E(G) minus F}.

Consider all set partitions pi of R_i(F) into nonempty blocks B such that E(K_B) is disjoint from F. These are precisely the permissible pieces {v_i} union B with pivot v_i. The original later neighborhood is a clique, so there is no extra original-adjacency condition. The empty neighbor set has the single empty partition. The all-singleton partition is always permissible.

Set
    F_next=(F restricted to W_(i+1)) union union_(B in pi) E(K_B).
Let V_(n+1)(empty)=0 and define backwards
    V_i(F)=min_pi (|pi|+V_(i+1)(F_next)).                   (3)
Then
    cp(G)=V_1(empty).                                     (4)

For a direct proof, every edge-partition clique has a unique earliest vertex in the fixed ordering. Group its pieces by this pivot. At step i, the pieces at v_i partition exactly the unspent edges incident to v_i, so their other vertices form an admissible pi. Edges they consume wholly among later vertices are exactly the added state edges in (3). Conversely, assembling the pieces prescribed by a trajectory of (3) covers each original edge once, at or before its earlier endpoint, and never repeats one. This gives both inequalities in (4). The same reasoning proves V_i(F)=cp(G[W_i]-F) for every such state F.

The residual graph need NOT be chordal. Chordality is used only for the original PEO and its original later-neighborhood cliques. This is a finite exponential recurrence, not a report that a dynamic program was run. A root proof would require an amortized upper potential on reachable states, not merely this exact encoding.

## 5. C07.4: arbitrary residual graphs occur even at zero deficit

Let L be ANY simple graph on a set Q of s>=2 vertices. Let H=J(s,s), with core Q and s pairwise nonadjacent vertices I universally adjacent to Q. This fixed original graph has
    n=2s, r=s+1, delta=0.
Take the PEO consisting of I first and Q last.

Let F=E(K_Q) minus E(L). Partition E(K_Q) into at most s matchings by C01's explicit odd/even matching construction, restrict these matchings to F, and pad with empty matchings to get M_1,...,M_s. Assign M_j to a distinct x_j in I. At pivot x_j, take triangle x_j ab for each ab in M_j and singleton edge x_j a for each unmatched a in Q.

These are admissible PEO choices: edges within each M_j are a matching; all M_j are mutually edge-disjoint. They spend exactly F on Q. After all s pivots have been processed, the residual is precisely L. The number of prefix pieces is
    sum_j(s-|M_j|)=s^2-|F|.                               (5)

This proves universality of reachable residuals even for an original complete split graph of zero deficit. It does not claim that every such prefix is part of an optimal partition.

A concrete state-compression obstruction uses the SAME original H=J(4,4):
- F_1={12,34} leaves C4 on the four core vertices, with cp=4.
- F_2={12,13} leaves triangle 234 and pendant edge 14, with cp=2.
Both states are reachable after four pivots, have the same original n,r,delta, the same prefix cost 14, two spent core edges, four remaining vertices, and four remaining edges. But their exact cost-to-go differs. Hence these scalar counts do not determine V_i(F).

This excludes exact count-only state identification and excludes any assumption that original zero deficit guarantees chordal residuals. It does NOT exclude every upper potential based partly on counts: such a potential may keep extra state or pay carefully justified slack.

## 6. Audit, root implications, and checkpoint

The completion is checked at empty S, d_v=k, n=r, disconnected input, and k=1. The perturbation distinguishes a K2 piece from larger pieces and maintains the partition invariant after each deletion. The recurrence permits nonchordal residuals and unused final vertices, and identifies cliques by their earliest vertex rather than by maximality. The universality example verifies total prefix cost and exact residual cp without enumeration.

A sufficient potential for (3) would assign Phi_i(F) so that for each reachable state SOME admissible pi obeys
    |pi|+Phi_(i+1)(F_next)<=Phi_i(F),
with Phi_(n+1)(empty)=0 and Phi_1(empty)<=n^2/6+Cn.
No such uniform Phi is supplied. Sections 2-3 isolate a zero-deficit proof obligation and quantify, rather than hide, the growing-deficit loss. Section 5 specifies what a faithful state representation must not forget.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: this written construction and its explicit C01/C04-C06 inputs.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
Canonical failed-route records are unchanged.

Next exact action: derive a core-edge matching potential in terms of n,r,delta and h=e(G-Q), without requiring Q to remain an intact piece; combine it with a disjoint-clique packing potential and exhibit boundary families where either term alone is insufficient. The objective is a uniform leading coefficient, not a larger finite excluded order.
