# C17: partial-resource partitions with an unbounded number of neighborhood classes

Candidate ID: `candidate:erdos81-a01-c17-growing-classes`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `5a2bb851a71c0261976e97ad09ccaa2ada77114a`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Scope and inputs

All graphs are finite and simple. cp counts an exact edge partition into complete subgraphs with nonempty edge sets. Write B(n)=floor(n(n+1)/6). C01 constructs an n-vertex split graph attaining B(n); this is an attained comparison value, not a universal upper bound on split graphs.

This cycle proves a restricted domination statement for a family with an ARBITRARY number b of distinct neighborhoods, rather than a fixed quotient. Its constants do not depend on b. It does not assert that an arbitrary chordal graph has this structure, nor close either admitted obligation.

Inputs are C01's matching partition of J(q,q), C15's three-group cyclic lift, and C16's requirement to preserve actual residual edges. The formulas needed from those constructions are restated here. No mathematical code, enumerator, optimizer, solver or proof assistant was executed. Text hashing is not mathematical verification. No novelty claim is made.

## 2. Family and exact resource accounting

Fix integers b>=2 and q>=1. The core Q is a clique partitioned into q-sets A_i, one for each of b labels. There are also disjoint q-sets I_i, disjoint from Q. Initially the only crossing links are I_i-A_j for i!=j, each complete. Put I=union I_i and n=2bq.

The split version H_(b,q) has no edges within I. More generally put any graph F on I, with a supplied p_F-piece partition. The special graph G_(b,q) takes each I_i to be a clique and has no edges between different I_i.

A partial partition spends its ACTUAL edge set U. Later pieces must partition E(G) minus U. No whole group or whole link is marked spent merely because one of its edges was used. In particular, all the first-stage triangles below take one vertex in each of three groups and spend no within-group edge. Replacing several pieces by one clique is allowed only when their union of edge sets is exactly that clique, including its within-group edges.

For three q-groups X,Y,Z, the triangles
    {X_u,Y_v,Z_(u+v)}, (u,v) in Z_q^2,
partition all three intergroup links: each pair determines the third coordinate uniquely by subtraction. Equivalently we may use
    {I_i[v], A_j[u], A_k[v-u]}.
This costs q^2 and needs no primality or parity condition on q.

## 3. Odd b: all crossing links are assigned without padding

Suppose b is odd and label the groups by Z_b. Color each unordered pair {j,k}, j!=k, of core labels by its midpoint i=(j+k)/2. Two is invertible modulo b. The midpoint differs from both endpoints. For a fixed i the pairs {j,2i-j} form a matching covering every label other than i.

For each core-label pair {j,k} of color i, use the cyclic triangles on I_i,A_j,A_k. Each core intergroup link appears once. For a fixed leaf group I_i the matching visits each permitted core group exactly once, so each crossing link also appears once. Different leaf colors have disjoint crossing links. The prefix costs binom(b,2)*q^2 and uses no internal group edges.

Let epsilon_q=0 for q=1 and epsilon_q=1 for q>=2. The remaining graph consists of the b internal core cliques and F, with disjoint edge sets. Hence
    cp(H_(b,q) plus F) <= P_b(q)+p_F,
    P_b(q)=binom(b,2)*q^2+b*epsilon_q.                    (1)

For G_(b,q), p_F=b*epsilon_q, giving
    cp(G_(b,q))<=binom(b,2)*q^2+2b*epsilon_q.             (2)

## 4. Even b: one dummy label and an exact residual

Suppose b is even. Work in Z_(b+1), use its nonzero labels for the b actual groups, and leave label zero dummy. For a pair of distinct nonzero core labels {j,k}, use the same midpoint color when j+k!=0. There is a corresponding actual I_i, and i is neither endpoint. Omit the b/2 core pairs {j,-j}, whose color would be zero.

For a fixed nonzero i, the matching of all labels except i has the pair {0,2i}. Removing the dummy label leaves the actual core label 2i uncovered. Thus the ONLY remaining crossing link of I_i is I_i-A_(2i). Multiplication by two permutes the nonzero labels. The remaining core intergroup links are exactly the b/2 disjoint label pairs {j,-j}. The prefix has
    [binom(b,2)-b/2]*q^2=b(b-2)*q^2/2
triangles.

For each unordered pair {j,-j}, the residual on its two core groups and their two leaf groups has links
    A_j-A_(-j), A_j-I_(j/2), A_(-j)-I_(-j/2),
and all still-unspent within-group edges. These components are vertex-disjoint, before adding arbitrary edges of F.

First retain F separately. On A_j union I_(j/2), partition the internal A_j clique and its crossing link using C01's J(q,q) construction, at cost q(q+1)/2. This construction does not use any I-internal edge: color K_q into at most q matchings, attach each matching to a distinct I vertex by triangles, and use the remaining crossing edges singly. Do the same for the other pair of groups. Use q^2 single edges for A_j-A_(-j). Consequently
    cp(H_(b,q) plus F)<=P_b(q)+p_F,
    P_b(q)=b^2*q^2/2+bq/2.                              (3)
All the crossing-edge pieces in this version have size at most three.

Alternatively, for G_(b,q), use the two complete residual graphs
    A_j union I_(j/2), A_(-j) union I_(-j/2)
as two pieces, and partition A_j-A_(-j) into q^2 edges. The internal edges of all four groups are used exactly here, not in the prefix. Thus
    cp(G_(b,q))<=binom(b,2)*q^2+b.                       (4)

This distinction is essential: (3) is the small-piece construction used for edit robustness; (4) is the better unedited partition with large pieces.

## 5. Unbounded-class chordal domination with uniform constants

G_(b,q) is chordal. Eliminate the groups I_i one at a time, then Q. The remaining neighbors of an eliminated outside vertex are its own remaining group together with Q minus A_i, which is a clique. An induced cycle of length at least four would have an earliest vertex with adjacent cycle neighbors, a contradiction.

When q>=2, vertices taken two each from any two different I_i induce 2K2. A split graph cannot contain induced 2K2: its clique side would need to meet both edges, thereby creating an unwanted crossing edge. Thus this is a nonsplit chordal family, not only a calculation on already split inputs.

Every clique meets at most one I_i, so omega(G)=bq. Direct edge counting gives
    m=(3b^2-b)*q^2/2-bq,
    delta=[(bq-1)*(2bq)-binom(bq,2)]-m=bq(q-1)/2.        (5)
The large defect for growing q is not assumed small.

Equations (2) and (4) yield, simultaneously for ALL b>=2 and q>=1,
    cp(G_(b,q))<=n^2/8+n.                               (6)
The constant is independent of both parameters: binom(b,2)*q^2<=n^2/8 and 2b<=n.

More strongly, the displayed integral counts lie below B(n). For odd b the difference from n(n+1)/6 is
    b*((b+3)*q^2+2q-12*epsilon_q)/6>=0.                  (7)
For q=1 this is positive because epsilon_q=0; for q>=2 and b>=3 it is positive already at the minimum parameters. For even b the corresponding difference using (4) is
    b*((b+3)*q^2+2q-6)/6>=0,                            (8)
including b=2,q=1. Integrality gives cp(G_(b,q))<=B(2bq). C01's complete-split witness is therefore a same-order dominator for every graph of this family.

This removes the fixed-number-of-classes restriction for this PARTICULAR missing-own-group pattern. It does not remove the equal-size or neighborhood-pattern assumptions.

## 6. An additional coalescence saving for odd b

For odd b set s=(b-1)/2 and choose the disjoint core-label pairs
    {2h,2h+1}, h=0,...,s-1.
Their midpoint colors 2h+1/2 are distinct modulo b, since two is a unit. Hence these pairs use disjoint core groups and distinct leaf groups. In G_(b,q), all three internal groups of each chosen triple are cliques whose edges were reserved.

Replace that triple's q^2 cyclic triangles and its three internal clique pieces by one K_(3q). There is no shared edge with any other prefix piece. Distinct selected triples are vertex-disjoint. This yields the exact construction bound
    cp(G_(b,q)) <= [binom(b,2)-s]*q^2
                    +s+(2b-3s)*epsilon_q
                <= (b-1)^2*q^2/2+b+1.                  (9)
At q=1 the exact first expression, not a count of singleton internal pieces, is used. Equation (9) demonstrates additional savings from the partial-resource state; the unmerged bound (2) remains available when internal outside edges are absent.

## 7. Robust variant with arbitrary F and crossing edits

Start with the small-piece version (1) or (3). Keep the core complete and the graph F fixed, delete D of the original crossing edges and add A previously absent crossing edges. Then
    cp(G_edited)<=P_b(q)+p_F+D+A.                        (10)

To verify the repair, every crossing-affected piece is an edge or triangle. With one deleted edge a triangle leaves two edges and costs one extra piece. With two or three deletions it costs at most its original count plus the number deleted. Core-only cliques and F pieces are untouched. Repair each original piece separately and add the A new edges singly; none was previously present. This gives exact edge coverage, not an overlapping cover.

An exact sufficient benchmark criterion is
    p_F+D+A <= B(2bq)-P_b(q).                            (11)
For even b the right side equals floor(bq*(bq-1)/6).
For odd b it equals
    floor(b*((b+3)*q^2+2q-6*epsilon_q)/6).
All these quantities retain their dependence on the actual b,q, with no hidden template constant. The allowance is quadratic in many parameter ranges. Equation (11) implies the admitted domination statement for any CHORDAL edited input satisfying it. For arbitrary F or arbitrary edits, chordality must be checked separately.

The stronger large-piece constructions (4) and (9) do not inherit the cost D+A; (10) uses only the small-piece alternative.

## 8. Regression cases, scope audit, and checkpoint

For b=2 the prefix in Section 4 is empty, the residual consists of the two end cliques joined by a core bipartite link, and (4) gives q^2+2. At q=1 this is the three-edge path. Odd b=3 needs no dummy and has three group triangles. The formulas work for composite odd b and composite q; no field or design-existence theorem is invoked.

C16's star regression is retained: in J(q,3q), coloring internal K_q edges into matchings and attaching them to distinct outside vertices gives cp=3q^2-binom(q,2), whereas forbidding those internal resources wastes a quadratic number of pieces. Our resource rule allows that partition unchanged.

For b=4, C16's asymmetric three-triangle/K4 prefix and its five residual cliques remain a DIFFERENT valid certificate, often sharper than (4). Taking the better of the constructions is allowed; adding their incompatible savings is not. The present result generalizes the number of classes rather than claiming to optimize every fixed b.

Manual audit included endpoint exclusion of midpoint colors, all crossing-link multiplicities, the missing pair {0,2i}, the bijection i->2i, q=1 edgeless internal groups, b=2, residual vertex-disjointness, large-piece versus small-piece repairs, and the integer-floor comparisons. No claim of exhaustive testing or optimum cp is made.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: equations (1)-(11), natural-language proof draft with C01 input.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
failed_routes: canonical ledger unchanged; C16's two shortcut obstructions remain in force.

Next action: remove the equality between outside-class size and core-class size while retaining explicit resource capacities. A dummy LABEL in Section 4 is harmless because its exact residual was handled; padding real vertices and silently discarding the cost is not. Analyze unequal multiplicities and identify when core-edge budgets become the bottleneck.
