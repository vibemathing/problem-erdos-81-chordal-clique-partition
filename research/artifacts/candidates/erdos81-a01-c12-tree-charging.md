# C12: tree charging, balanced interfaces, and collective split peeling

Candidate ID: `candidate:erdos81-a01-c12-tree-charging`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `68b035635f8da7d126d59b85a6c9d5e1931f465e`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Scope and notation

Graphs are finite and simple; cp partitions edges exactly once. The unrestricted target and root remain open. No mathematical code, enumeration, ILP or proof assistant was executed.

Candidate inputs: C01's exact complete-split calculation; C06's clique-tree counting; C08's path-power partitions; C10's universal-vertex restriction; C11's design-based bound
    cp(J(a,s)) <= (a^2+2as)/6+4a for a>=s.
The last bound has the explicitly declared Doyen-Wilson theorem dependency in C11's primary-source note. Transport does not verify any of these inputs.

Put B_C(n)=n^2/6+Cn and x_+=max(x,0). Allowed axioms: finite-graph-basic, finite-combinatorics, real-arithmetic.

## 2. C12.1: compatible edge layers of a rooted clique tree

Root a maximal-clique tree at a maximum clique Q of size r>=1. Join component trees through empty separators when necessary. Process bags in any order in which parents precede children. For a nonroot bag let
    S_i=C_i intersect parent(C_i), s_i=|S_i|,
    A_i=C_i minus S_i, a_i=|A_i|,
    N_i=number of vertices introduced before bag i.

The running-intersection property shows A_i consists exactly of the vertices first introduced at C_i, and its earlier neighbors are precisely S_i. Indeed, if a new vertex were adjacent to an earlier vertex not in S_i, a bag containing the edge and the path to that earlier vertex's first bag would force that vertex into the parent separator. Thus the new edges form exactly J(a_i,s_i), reserving the edges of S_i. Together with E(Q), these layers partition E(G).

Every absent pair is counted exactly when its later endpoint is introduced. Both endpoints cannot be new in the same bag, because that bag is a clique. Therefore
    Z := binom(n,2)-m = sum_i a_i(N_i-s_i).                 (1)
This is an identity for nonedges, not an inclusion-exclusion estimate.

Let Phi(a,s)=(a^2+2as)/6. Telescoping the introduced vertex counts gives
    sum_i Phi(a_i,s_i)=(n^2-r^2)/6-Z/3.                    (2)

## 3. C12.2: a general-deficit potential with an explicit minority penalty

Fix C>=4 and define
    P_C = sum_i a_i[(2/3)(s_i-a_i)+1/2-C]_+.               (3)
Then the following candidate upper bound holds:
    cp(G) <= n^2/6+Cn+1-r^2/6-Cr-Z/3+P_C.                 (4)

If a_i>=s_i, C11 bounds its layer by Phi+C a_i and its penalty is zero. If s_i>a_i, C01 gives the exact layer count
    cp(J(a_i,s_i))=a_i s_i-binom(a_i,2)
      =Phi(a_i,s_i)+a_i[(2/3)(s_i-a_i)+1/2].
In both cases the count is at most Phi+C a_i plus its summand in (3). Use Q once (an upper bound also when r=1), sum these edge-disjoint layer partitions, and use (2) and sum_i a_i=n-r. This proves (4).

A useful equivalent form retaining the original deficit
    delta=(r-1)n-binom(r,2)-m
is
    cp(G) <= [r(n-r)-delta]/3+(C-1/6)(n-r)+1+P_C.          (5)

In particular, any rooted clique-tree certificate satisfying
    P_C <= Z/3+r^2/6+Cr-1                                 (6)
gives cp(G)<=B_C(n). The deficit and the penalty are distinct. Small delta does not force small P_C, and no such implication is assumed.

## 4. C12.3: an infinite class with an explicit root constant

Suppose G admits a rooted maximal-clique tree for which
    s_i-a_i<=L for every nonroot bag,
where L>=0 is a fixed constant independent of G. Let
    C_L=max(4,1/2+2L/3).
Then P_(C_L)=0, so (4) gives
    cp(G)<=n^2/6+C_L n for every n>=1.                     (7)

This does not bound n or r. It applies whenever the private part of each bag is at least its separator size minus a fixed L; in particular, L=0 permits arbitrary-sized bags with private part at least separator size. For L<=5 one may take C_L=4.

Another sufficient class is given by
    D=sum_i a_i(s_i-a_i)_+ <= K n
for a fixed K>=0. Since P_4<=2D/3, formula (4) gives
    cp(G)<=n^2/6+(4+2K/3)n.                               (8)

These are complete written bounds for the explicitly restricted classes, not an assertion that every chordal graph belongs to either class. Empty graphs are handled separately with cp=0.

## 5. C12.4: collectively peel a large common-neighborhood class

Let S be an s-clique, s>=1. Let I be t>=s pairwise nonadjacent vertices with N_G(x)=S for every x in I. Let Z_0=V(G) minus (S union I), N=|Z_0|, b=e(S,Z_0), and B=s+t. There are no I-to-Z_0 edges. The exact complete-split partition on S union I, the singleton S-to-Z_0 edges and a partition of G[Z_0] give
    cp(G)<=cp(G[Z_0])+st-binom(s,2)+b.                     (9)

The core S is processed collectively with I and is then removed. Its edges may be used in many mixed pieces; they are NOT simultaneously charged to a remaining parent clique.

If cp(G[Z_0])<=B_C(N), then comparison with B_C(N+B) gives the exact sufficient slack
    B_C(N+B) - [B_C(N)+st-binom(s,2)+b]
      =(t-2s)^2/6+BN/3+C B-s/2-b.                         (10)

In particular, if t>=2s and C>=1/6, this slack is nonnegative:
    b<=sN<=BN/3, and C B>=s/2.
Thus deleting S union I is a root-compatible induction step. The condition on the smaller graph is explicit, and chordality passes to that induced graph.

Consequently, for every fixed C>=4 a vertex-minimal chordal counterexample to B_C, should one exist, has fewer than 2s simplicial vertices with the same s-clique neighborhood, for each s>=1. Isolated vertices can always be deleted without cost.

## 6. C12.5: composable certificates, and a quantitative boundary

A valid certificate may repeatedly remove either:
A. a nonempty clique module of size a at least its outside-neighborhood size s, using C11;
B. S union I as in Section 5 with t>=2s;
and finish with an edgeless graph, a complete graph, or a graph satisfying (6).
All steps use the CURRENT induced graph. For one fixed C>=4, (4), C11 and (10) show by reverse induction that the original graph satisfies cp<=B_C(n). Vertices removed at distinct steps are disjoint, and each step's proof specifies its own disjoint edge sets. This composition does not add incompatible partition savings.

These rules are NOT complete even at delta=0. Take P_(3k+1)^k for k>=2: vertices 1,...,3k+1, with ij an edge iff 1<=|i-j|<=k. Here r=k+1 and delta=0. C06's identity forces every nonroot bag in every maximal-clique tree to have a_i=1 and s_i=k; there are 2k such bags.

If one requires every partition piece to stay in a single reserved-edge layer of Section 2, the exact optimum is
    cp_layer=1+2k^2,                                      (11)
since the root is a clique and each later layer is J(1,k), a k-edge star. For every fixed C, (11) exceeds
    B_C(3k+1)=(3/2)k^2+(1+3C)k+C+1/6
for all sufficiently large k. When k is large enough that the brackets in (3) are positive, the right side of (4) is exactly (11), so criterion (6) also fails for every root and clique tree.

Neither peeling primitive applies initially. Closed neighborhoods are the distinct intervals
    [max(1,i-k),min(3k+1,i+k)],
so there are no adjacent true twins and hence no clique module of size at least two. Every vertex has degree at least k>1, ruling out a one-vertex module with a>=s.
There are no false twins either. For nonadjacent i<j, j-i>=k+1. If i>1, i-1 is a neighbor of i but not of j. If i=1 and j<3k+1, j+1 is a neighbor of j but not of i. If i=1,j=3k+1, j-1 distinguishes their neighborhoods. Adjacent vertices cannot have equal open neighborhoods. Thus every common-neighborhood class has size one.

The graph nevertheless has cp<=k^2+k+2 by C08's explicit three-block partition, with leading coefficient 1/9 rather than the 2/9 in (11). This excludes completeness of the present certificate system, not the root or the valid sufficient bounds (4)-(10). It demonstrates that thin bags sometimes require pieces spending edges from different layers.

## 7. Audit and continuation

Checked: disconnected clique trees, parent-before-child order, no earlier neighbor outside the separator, exact nonedge accounting, the positive-part truncation, the C_L quantifier independent of n, b versus the upper bound sN, removal of the whole borrowed core, induced rather than edge-deleted remainders, and every twin case in the path-power boundary.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: the written potentials and peeling rules here with their named inputs.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
No enumeration extremizers, executed ILP certificates, verifier receipts or canonical failed-route writes are claimed.

Next exact lemma: for the remaining thin-bag clique trees, authorize and account for borrowing a separator's edges across a connected group of bags, with an explicit cost for the parent remainder. The path-power example requires such cross-layer grouping; separate annulus optima and counts of positive-deficit bags cannot suffice. A computational plan should track spent separator edges as in C07, not merely n,r,delta or bag sizes.
