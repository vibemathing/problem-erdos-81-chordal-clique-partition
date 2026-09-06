# C13: two-way pendant-region peeling and cancellation of missing-edge cost

Candidate ID: `candidate:erdos81-a01-c13-pendant-slack`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `ffad8b3e61a763b2cc479d62e79d9e7276d3487b`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Frozen scope

All graphs are finite and simple; cp is an exact edge partition into nonempty cliques. The unrestricted split-domination target and the root remain open. This cycle gives sufficient root-compatible reductions, not an assertion that every chordal graph admits them.

Use C08's explicit matching-allocation inequality and C12's principle of removing a borrowed core with its attachments. C08's input is the self-contained complete-graph matching decomposition in C01. The new reductions below do not require C11's design theorem. No mathematical code, enumeration, solver, or verifier was executed. Allowed axioms: finite-graph-basic, finite-combinatorics, real-arithmetic.

Let V(G)=S disjoint union I disjoint union Z. Assume S is an s-clique, t=|I|>=s>=1, N=|Z|, and there are no I-to-Z edges. The vertices of I need not be nonadjacent and need not have equal neighborhoods in S. Write
    b=e(S,Z), M=st-e(S,I), B=s+t.
Let p>=cp(G[I]) be a specified nonnegative upper bound, preferably accompanied by an explicit partition. Put B_C(x)=x^2/6+Cx.

## 2. C13.1: two legitimate partitions with different retained cores

The first construction leaves S in the remainder:
    cp(G)<=cp(G[S union Z])+p+st-M.                         (1)
Use the remainder's partition, a partition of G[I], and singleton crossing edges from S to I.

The second construction removes S with I:
    cp(G)<=cp(G[Z])+p+st-binom(s,2)+(2s/t-1)M+b.            (2)
Apply C08's missing-neighbor matching bound to the subgraph on S union I. Its triangles use two S vertices and one I vertex and no edge of G[I]. Thus a partition of G[I] can be added without conflict. Use all S-to-Z edges singly, and partition G[Z]. For s=1, (2) follows directly from (1)'s singleton construction on S union I, since its extra allowance is 2M/t>=0.

Neither construction changes G or declares I edgeless. Formula (2) may not share its savings with a partition of G[S union Z]; formula (1) and formula (2) are alternatives, not additive improvements.

## 3. C13.2: exact slack and the cancellation identity

Suppose the proper induced remainders satisfy
    cp(G[S union Z])<=B_C(N+s), cp(G[Z])<=B_C(N).
The two constructions prove the desired bound whenever at least one of these slacks is nonnegative:
    L_1 = t(2N+t-4s)/6 + Ct-p+M,
    L_2 = (t-2s)^2/6 + BN/3 + CB-s/2-p-b
                             +(1-2s/t)M.                 (3)

These formulas are obtained by subtracting (1) and (2), with the displayed remainder bounds, from B_C(N+B). They retain both the missing-cross-edge term and the actual b, not only its upper bound sN.

If s<=t<=2s and d=2s-t, the EXACT identity is
    (d/t)L_1+L_2
      =sN-b+s(3C-1/2-d/3)-(2s/t)p.                        (4)
In particular, both M and the quadratic d^2 terms cancel. The weights d/t and one are nonnegative, so a nonnegative right side guarantees at least one nonnegative slack. At d=0 the conclusion directly concerns L_2; no division by d is performed.

## 4. C13.3: a uniform near-balance peeling criterion

Fix real constants A,L>=0 independent of G and choose
    C>=C(A,L):=max(A, 2A/3+1/6+L/9).                      (5)
Suppose
    p<=At, and t>=max(s,2s-L).                             (6)
Under the two induced-remainder bounds in Section 3, cp(G)<=B_C(n).

For s<=t<=2s, d<=L and b<=sN. The right side of (4) is at least
    s[3C-1/2-d/3-2A]>=0
by (5). Thus one of the two partitions works.

For t>=2s, use L_2 alone. Its squared term, its M term, and BN/3-b >= (t-2s)N/3 are nonnegative. Its remaining linear term is at least
    C(s+t)-s/2-At=(C-1/2)s+(C-A)t.
Since C>=A, the minimum for t>=2s occurs at t=2s, where it equals s(3C-2A-1/2)>=0. This proves the other regime.

Consequently, a vertex-minimal chordal counterexample to B_C for fixed C satisfying (5), should one exist, has no such clique-boundary pendant region with a certificate p<=At. Chordality is used only to keep both proper induced remainders in the class. The partition and slack identities hold for arbitrary graphs.

For a concrete choice compatible with C11-C12, C=4 permits A=1,L=28. Such a minimal counterexample cannot have a region I with cp(G[I])<=|I| and
    |I|>=max(|S|,2|S|-28).
An explicit partition of I into at most |I| pieces suffices; no algorithm for detecting all such regions is claimed.

## 5. C13.4: class consequences and composition

For L=0, the criterion no longer requires identical neighborhoods. An edgeless I with all its outside neighbors contained in S and t>=2s is permitted with A=0,C>=1/6. A disjoint union of cliques is permitted with A=1,C>=1. The latter class can have quadratically many internal edges, even though p<=t.

When Z is empty, both remainders are a clique and the empty graph, so their B_C bounds hold for C>=1/6. Formula (5) always has C>=1/6. Hence (5)-(6) give an unconditional all-order root bound on the explicitly stated class with a clique S and a linear-size partition of G-S; S need not be maximum.

The rule also composes with C11-C12 certificates: at a step with nonnegative L_1 remove I; at a step with nonnegative L_2 remove S union I. In reverse induction the chosen remainder has fewer vertices and the corresponding construction specifies disjoint edges. This requires the actual chosen remainder to have a valid certificate; there is no claim that all graphs reduce.

The path-power boundary in C12 is now covered. In P_(3k+1)^k, k>=2, take the central consecutive (k+1)-clique S. Its complement consists of two disjoint k-cliques, so t=2k, p<=2, and t=2s-2. There are no identical-neighborhood or clique-module assumptions. The conditions A=1,L=2,C=4 apply. This is a cross-layer partition route for a family on which the earlier reserved-layer certificate cost was quadratic above the root coefficient. Its still better explicit three-block partition from C08 remains available.

## 6. C13.5: a component-size separator criterion

A separate sufficient induction criterion is useful when I is the entire complement of a clique S. Let its component orders be t_1,...,t_j with sum t. Assume t>=2s. If each component satisfies the B_C bound, then p<=sum t_j^2/6+Ct by additivity of cp across components. Formula (2), now with Z empty, yields
    B_C(s+t)-[p+st-binom(s,2)+(2s/t-1)M]
      >=[(t-2s)^2-sum t_j^2]/6
                           +(C-1/2)s+(1-2s/t)M.           (7)

Thus if C>=1/2 and (t-2s)^2>=sum t_j^2, the smaller-component induction closes this step. This is a checkable separator condition, not a theorem asserting such a separator in every chordal graph. Using explicit component partitions instead of their quadratic induction bounds can be substantially stronger.

## 7. Limits and next exact task

The finite averages in C08 are existence arguments, not executed random experiments. All new formulas were checked algebraically in the written derivation: s=1, t=s, t=2s, d=0, M=0, M=st, b=0, b=sN, p=0, and empty Z. No optimality of the two chosen constructions is asserted.

Conditions (5)-(6) are sufficient, not necessary. If d=2s-t is proportional to n and no large M or sparse boundary compensates, (4) does not give a fixed universal C. When the pendant region itself needs a quadratic number of cliques, p<=At is unavailable. These remain mathematical gaps, not root counterexamples.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: this written slack identity and the named C08 input.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
No canonical failed-route record is appended.

Next exact task: improve the large-core side for arbitrary split neighborhoods using C11's triangle design before removing missing crossing edges. Account for triangles with exactly one surviving crossing edge, average over core relabelings, and compare the resulting second-moment bound with the intact-core and C08 bounds. The objective is a uniform asymptotic coefficient on ALL split graphs, without assuming the stronger domination reduction.
