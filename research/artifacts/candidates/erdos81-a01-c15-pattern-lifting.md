# C15: pattern-sensitive lifts, residual reuse, and robust same-order domination certificates

Candidate ID: `candidate:erdos81-a01-c15-pattern-lifting`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `9e6e123bfbbfd6d8de01ee335906fcba1cc07eb1`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Scope and reuse

All graphs are finite and simple; cp is an exact edge partition into nonempty cliques. This cycle constructs partitions on the four-block family that obstructs C14's scalar upper certificates, and on specified perturbations and nonsplit chordal extensions. It does not claim that every chordal graph has the required block structure.

C01 supplies the explicit partition of J(q,q) with q(q+1)/2 pieces and the attained same-order split benchmark B(n)=floor(n(n+1)/6). C14 supplies the four-block test family. C09 is relevant prior work on modular K4 allocation, but its prime/sum/product construction and its single common-neighborhood family are not reused as a hidden hypothesis. The construction here works for EVERY positive q and multiple distinct neighborhoods. The elementary lifts below are proved directly; no external design-existence theorem, mathematical code, enumeration or proof assistant is invoked.

## 2. C15.1: explicit lifts with reserved within-group edges

Suppose three disjoint q-sets X,Y,Z have every intergroup edge. Label each by residues modulo q. The q^2 triangles
    {X_u,Y_v,Z_(u+v)}, u,v in Z_q,                        (1)
partition all three intergroup links. Any X-Y pair fixes u,v; any X-Z or Y-Z pair fixes the remaining variable by subtraction. No edge within a group is used. This remains valid when each group has arbitrary internal edges, which are reserved.

For four equal p-sets B_0,...,B_3 with p odd, the p^2 cliques
    {B_0[u], B_1[v], B_2[u+v], B_3[u+2v]}, u,v in Z_p,   (2)
partition all six intergroup links, using one vertex from each group. Here B_i[z] is the vertex with label z in group B_i; labels are reduced modulo p. To check uniqueness, the six pairs of coordinates recover (u,v) by:
    (u,v);
    (u,w): v=w-u;
    (u,z): v=(z-u)/2;
    (v,w): u=w-v;
    (v,z): u=z-2v;
    (w,z): v=z-w, u=2w-z.
Division by two is valid for odd p; primality is unnecessary.

For four q-sets of ANY size q, let p=q when q is odd and p=q+1 otherwise. Construct (2) on padded p-sets and restrict every clique to the q chosen vertices in each group. Discard pieces with fewer than two vertices. Restricting vertices of a clique preserves completeness; each desired intergroup edge remains in exactly one piece. Thus at most p^2 pieces suffice. This is vertex restriction of an explicit construction, not arbitrary edge deletion.

More generally, if a quotient's intergroup edges are partitioned into triangle, K4 and single-edge motifs, lift each motif separately by these rules. Distinct motifs spend distinct intergroup links. Within-group edges are then partitioned separately. The supplied motif partition, not the word quotient alone, certifies edge-disjointness.

## 3. C15.2: the four-block family and its resource schedule

Fix q>=1. Let Q=A_0 union A_1 union A_2 union A_3 be a 4q-clique, with each A_i of size q. Let I=I_0 union I_1 union I_2 union I_3 consist of four q-sets. Initially I is edgeless, and every vertex of I_i is adjacent precisely to Q minus A_i. Call this split graph H_q; n=8q.

Instead of using four mixed quotient triangles, use these THREE:
    T_1=(I_1,A_0,A_2),
    T_2=(I_2,A_0,A_3),
    T_3=(I_3,A_0,A_1).                                   (3)
Their core links form the star at A_0. Their crossing links are distinct. Lift them by (1), at cost 3q^2.

Now the six links among I_0,A_1,A_2,A_3 are all untouched and present. They form a K4 motif. Lift it using (2) and the padding rule, at cost at most p^2. This is why reserving the core triangle A_1A_2A_3 is useful; consuming one more of those links in an earlier triangle would obstruct this step.

After these two stages, the only crossing links remaining are
    I_1-A_3, I_2-A_1, I_3-A_2.                           (4)
All inter-A_i links have been used: the three star links in (3), and the three other links in the K4 motif. No edge inside any A_i has been spent.

The exact residual is therefore the disjoint edge union of
    J(A_3,I_1), J(A_1,I_2), J(A_2,I_3), and K_(A_0).
Each J has parameters (q,q), so C01 gives q(q+1)/2 pieces, using its own internal A_i edges. The last core costs epsilon_q, where epsilon_q=0 for q=1 and epsilon_q=1 for q>=2. No residual piece overlaps an edge used in the first two stages. Hence
    cp(H_q)<=3q^2+p^2+3q(q+1)/2+epsilon_q.                (5)

For odd q this is (11q^2+3q)/2+epsilon_q. For even q it is (11q^2+7q)/2+1+epsilon_q. In particular, uniformly for q>=1,
    cp(H_q)<=U(q):=(11q^2+7q+4)/2
                  =(11/128)n^2+(7/16)n+2.               (6)
U(q) is an integer, since q^2 and q have the same parity. The unpadded q=1 construction has three triangles, one K4, and three residual edges: seven pieces.

These are upper partitions, not an exact optimum assertion. C14's scalar bound with leading coefficient 11/64 is thus very far from a lower bound on this family's actual cp.

## 4. C15.3: internal outside edges cost only their actual partition

Keep Q and the crossing pattern, but now allow ANY graph F on I. All pieces in (3), the K4 motif, and the three J residuals contain at most one I vertex, so they spend no edge of F. A specified partition of F with p_F pieces can be added without conflict. Consequently
    cp(G)<=U(q)+p_F.                                     (7)
No chordality of F or G is needed for this partition inequality. A linear p_F contributes only a linear term; it must be supplied rather than assumed for an arbitrary residual graph.

## 5. C15.4: explicit repair under many crossing-edge edits

Keep the core Q complete and keep F fixed. Relative to the crossing pattern in Section 3, delete D original crossing edges and add A formerly absent crossing edges. Then
    cp(G_edited)<=U(q)+p_F+2D+A.                          (8)

For the proof, use the partition from (5). Every piece touched by a crossing deletion has at most four vertices. Untouched pieces and the partition of F stay unchanged. A triangle with one edge deleted has a two-edge partition; all its other deletion cases cost no more. A K4 with one edge deleted is partitioned by one triangle and two edges, costing three, an increase of two. A K4 with j>=2 deleted edges has at most 6-j remaining edges, so singletons cost at most 6-j<=1+2j. The same inequality holds for pieces of size two or three. Thus deletions increase the piece count by at most 2D. Add the A new edges singly; none was covered before. This proves (8).

This is not a general Lipschitz claim for arbitrary optimal clique partitions: the only potentially large piece here is the clique on A_0, and crossing edits never touch its internal edges. In the split specialization F is empty, arbitrary crossing edits preserve the split property.

Combining (8) with C01 gives an exact same-order benchmark criterion:
    p_F+2D+A <= floor((31q^2-13q-12)/6)
      implies cp(G_edited)<=B(8q).                        (9)
Indeed the right side equals B(8q)-U(q). For any chordal input satisfying (9), the complete-split benchmark graph from C01 is a same-order dominator. Criterion (9) permits quadratically many edits, not just O(n), for large q. It is sufficient and need not be sharp.

## 6. C15.5: a nonsplit chordal infinite family with quadratic deficit

In the unedited graph, take each I_i to be a clique and put no edges between distinct I_i. For q>=2 the resulting graph G_q is nonsplit: two vertices of I_0 and two of I_1 induce 2K2. A split graph cannot contain induced 2K2, since its clique side must meet both disjoint edges and would introduce a crossing edge between them.

G_q is chordal. Eliminate I_0, then I_1, then I_2, then I_3, then Q. Each eliminated outside vertex has a clique as its remaining neighborhood: its own remaining I_i together with Q minus A_i. An induced cycle of length at least four would have an earliest vertex whose two cycle neighbors are adjacent, giving a chord; hence the ordering certifies chordality directly.

Here p_F=4 for q>=2. From (7),
    cp(G_q)<=U(q)+4<=B(8q), q>=2.                         (10)
To check the last inequality, (31q^2-13q-12)/6 is at least four at q=2 and increases for integer q>=2: its successive increment is (62q+18)/6>0. Thus (9) applies. At q=1, F is edgeless and Section 3 already gives seven pieces.

The graph has n=8q, maximum clique size r=4q, and
    m=22q^2-4q,
    delta=[(r-1)n-binom(r,2)]-m=2q(q-1).                  (11)
A clique meets at most one I_i, and its size there is at most q+3q, proving r=4q. Equation (11) follows by counting the core, four internal I_i cliques, and twelve crossing links separately.

This is a directly constructed nonsplit class satisfying the admitted domination target, not only a root-coefficient comparison on already split graphs. The class still has strong block restrictions; no claim is made that every chordal graph can be transformed into it without lowering cp. Some weaker bounds for this class may also follow from earlier candidates; the present resource schedule gives the stronger explicit coefficient (6).

## 7. Dependencies, attack pass, and next obligation

Reuse relation: C01's J(q,q) partition and same-order B(n) witness are exact inputs; C14's barrier family is the exact test object; C09 is prior modular-allocation context only. The new cyclic lift and every residual edge set are specified above. There is no dependence on a field of prime order or an unproved general transversal-design existence assertion.

Audited cases: q=1; q=2 and padding to three; division by two over any odd modulus; all six coordinate-pair inverses; vertex restriction versus edge deletion; the six residual crossing/core links; isolation of the internal F partition; K4 deletion with one versus several missing edges; and the precise sufficient range in (9). No optimality, finite enumeration or executed certificate checking is asserted.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: explicit partitions (5)-(10), with C01 input.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
Canonical failed routes remain unchanged; C14's scalar-certificate limitation is retained, not mistaken for a failed root route.

Next exact task: generalize the motif lift to a bounded clique size using an odd modulus on which every required slope difference is a unit. Derive an explicit O(n) padding cost for a FIXED quotient, then test what fails when the quotient size or its largest clique grows. A fixed-template lifting result must not be promoted to a uniform all-chordal reduction.
