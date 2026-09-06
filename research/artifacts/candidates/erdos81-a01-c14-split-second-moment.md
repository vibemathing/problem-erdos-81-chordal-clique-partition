# C14: deletion-sensitive designs and a uniform upper bound for split graphs

Candidate ID: `candidate:erdos81-a01-c14-split-second-moment`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `024685ec89fbb07a314477a97c2d8177dd844574`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Frozen scope and main candidate

All graphs are finite and simple. The number cp partitions the edge set exactly once into nonempty complete subgraphs. Let H be a split graph with a partition Q union I, where Q is an r-clique and I has t pairwise nonadjacent vertices. Set n=r+t, d_x=|N(x) intersect Q|, e=sum_x d_x, and q=binom(r,2). The specified core need not be maximum.

The candidate conclusion, for EVERY split H and n>=1, is
    cp(H) <= kappa*n^2+4n,
    kappa = sqrt((51*sqrt(17)-107)/3072).                 (1)
Here 1/6 < 1/(4*sqrt(2)) < kappa < 3/16. No novelty or current-best literature claim is made. This is not the n^2/6+O(n) root bound and does not prove the admitted chordal-to-split domination statement. Even combining (1) with that still-open reduction would transfer kappa, not 1/6.

Inputs: C01's explicit matching decomposition, C08's finite matching-assignment proof, and C11's design-based construction of J(r,t) for r>=t. C11 depends on the Doyen-Wilson theorem as documented in its primary-source note. These are named proof dependencies, not verifier receipts. No graph enumeration, mathematical program, numerical optimizer or proof assistant was executed. All optimization below is written algebra.

## 2. C14.1: deleting crossing edges with the correct local cost

Assume r>=t>=1 and r>=2. C11 constructs a partition of the COMPLETE split graph J(r,t) with at most
    (r^2+2rt)/6+4r                                        (2)
pieces. Its mixed pieces contain one I vertex and either one or two Q vertices. For small r the alternative construction in C11 is a core clique plus crossing edges and has the same mixed-piece property. No edge between I vertices is ever used.

Uniformly relabel the r core vertices in this partition while leaving I fixed. Then delete exactly the crossing edges absent from H. A core-only piece is unchanged. A mixed edge stays or vanishes. A mixed triangle xuv has the following exact repair:
- two surviving crossing edges: retain the triangle;
- no surviving crossing edge: retain the core edge uv;
- exactly one surviving crossing edge: replace the resulting two-edge path by its two edges.
Only the last case increases the number of pieces, by one. This repair does NOT assume an arbitrary edge-deleted clique stays complete. Every original piece is separately partitioned after deletion, so edge-disjointness is preserved globally.

Let h_x count mixed triangles through x in the complete-split partition. Their core edges form a matching, because a repeated core endpoint would repeat a crossing edge through x. Therefore h_x<=r/2. For any fixed pair of distinct core positions, the probability that exactly one image belongs to N_H(x) is
    2*d_x*(r-d_x)/(r*(r-1)).
Linearity of the finite average, without any probabilistic independence assumption, bounds the expected increase by
    sum_x d_x*(r-d_x)/(r-1).
Some relabeling has at most this average increase. Consequently
    cp(H) <= (r^2+2rt)/6+4r
                         +sum_x d_x*(r-d_x)/(r-1).        (3)

The same proof for ANY graph G with clique Q and |V(G)-Q|=t<=r gives the right side of (3) plus cp(G-Q): the constructed pieces do not spend outside edges. The split specialization sets that additional cost to zero.

## 3. C14.2: degree variance and the three compatible alternatives

For r,t>0 put rho=e/(rt). Then
    sum_x d_x*(r-d_x)
      =r^2*t*rho*(1-rho)-sum_x (d_x-r*rho)^2.             (4)
Thus heterogeneous degrees improve (3); discarding variance is only a weakening for the uniform estimate below.

An intact core plus singleton crossing edges always gives
    cp(H)<=e+1.                                          (5)
When t>=r>=2, C08's matching assignment gives
    cp(H)<=e+q-(1/t)*sum_x d_x*(d_x-1)
          <=rt*rho+r^2*(1/2-rho^2)+r*(rho-1/2).           (6)
The second inequality follows from sum d_x^2>=e^2/t. Its finite matching assignment consumes each core matching class at most once; it is not an assumption of simultaneous optimization with (3) or (5).

Equations (3), (5), and (6) describe alternative partitions. Their bounds may be minimized, but their savings are not added.

## 4. C14.3: small-core optimization, r<=t

Let alpha=r/n<=1/2 and T=alpha*(1-alpha). Ignoring an additive allowance at most n from (5)-(6), their minimum is at most n^2 times
    F=min(T*rho, T*rho+alpha^2*(1/2-rho^2)).

If rho<=1/sqrt(2), then F<=T*rho<=1/(4*sqrt(2)).
If rho>=1/sqrt(2), set K=rho+rho^2-1/2>0. Completing a square gives
    F<=alpha*rho-alpha^2*K
      =rho^2/(4K)-K*(alpha-rho/(2K))^2
      <=rho^2/(4K)<=1/(4*sqrt(2)).
For the last inequality, the equivalent expression factors as
    (sqrt(2)-1)*rho^2-rho+1/2
      =(sqrt(2)-1)*(rho-1/sqrt(2))*(rho-1-1/sqrt(2))<=0
on the stipulated interval. This uses no unconstrained numerical maximization. We obtain
    cp(H)<=n^2/(4*sqrt(2))+n                               (7)
for r<=t and r>=2.

## 5. C14.4: large-core optimization, r>=t

Assume r>=t>=1 and r>=2. Put alpha=r/n>=1/2,
    T=alpha*(1-alpha), A=(2alpha-alpha^2)/6.
Using (4) and 0<=rho<=1, the extra denominator correction in (3) is at most
    [rt/(r-1)]*rho*(1-rho)<=t/2.
Hence (3) and (5), each with additive allowance at most 4n, give
    cp(H)<=n^2*min(T*rho, A+T*rho*(1-rho))+4n.             (8)

For alpha>=4/5, the first term is at most T<=4/25.
For 1/2<=alpha<=4/5, put z=sqrt(A/T). Then 1/sqrt(2)<=z<=1. If rho<=z, the first term is at most Tz. If rho>=z, rho*(1-rho)<=z*(1-z), since
    z*(1-z)-rho*(1-rho)=(rho-z)*(rho+z-1)>=0.
The second term is then at most A+Tz*(1-z)=Tz. Thus the minimum in (8) is at most
    sqrt(A*T)=sqrt(alpha^2*(1-alpha)*(2-alpha)/6).          (9)

For completeness, the maximum in (9) is certified algebraically. Write
    a0=(9-sqrt(17))/8, g(x)=x^2*(1-x)*(2-x).
The identity 4a0^2-9a0+4=0 gives
    g(x)-g(a0)=(x-a0)^2
                *[x^2+(2a0-3)*x+3a0^2-6a0+2].           (10)
For x in [1/2,4/5] and a0 in [1/2,5/8], the bracket is negative:
    x*(x+2a0-3)<0,
    3a0^2-6a0+2=3*(a0-1)^2-1<=-1/4.
Therefore g(x)<=g(a0). Direct reduction using the quadratic relation gives
    g(a0)/6=(51*sqrt(17)-107)/3072=kappa^2.                (11)
The branch alpha>=4/5 is also covered, since 4/25<1/(4*sqrt(2))<kappa. Combining (7)-(11) proves (1). The omitted cases t=0, r=0, or r=1 have at most n singleton edges plus a core piece, and satisfy (1) directly. The empty graph has cp=0.

## 6. C14.5: a quadratic barrier for these scalar certificates, not for cp

For every positive integer q, set r=t=4q. Partition the core into four q-sets A_0,...,A_3, and I into four q-sets I_0,...,I_3. For x in I_i let N(x)=Q minus A_i. This is explicitly a split graph, and d_x=3r/4 for all x, so the variance term in (4) vanishes.

The three displayed partition bounds evaluate to:
    intact-core (5):              3r^2/4+1;
    matching (6), first bound:    11r^2/16+r/4;
    deletion-design (3):         r^2/2+4r+3r^3/[16(r-1)].
The linear missing-neighbor estimate of C08 gives 3r^2/4+r/2 and is no better here. The minimum of these displayed bounds has leading term
    (11/64)*n^2=(1/6+1/192)*n^2.
Thus these scalar bounds, even with degree variance retained, do not by themselves certify the desired 1/6 coefficient on every split graph.

This is NOT a lower bound for cp of the example. In particular it cannot be a counterexample to split domination, since the example already is split. It only identifies a limitation of the displayed upper certificates. Better pattern-sensitive assignments or larger pieces may do much better.

## 7. Audit and continuation

Audited: mixed-piece shape in every branch of C11; exact repair of a triangle with one crossing edge removed; pair marginals versus independence; r=2; r=t; rho=0,1; t=0; the signs of the variance term and both optimization branches; the algebraic maximum; and the distinction between a poor certificate and a graph lower bound.

Primary-source status and limitations are in `research/artifacts/source-notes/erdos81-a01-c14-design-deletion.md`. The upper coefficient (1) is a natural-language candidate with a declared design theorem input, not a claim about the best published constant.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: the written universal split bound and second-moment inequality, with C01/C08/C11 inputs.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
Canonical failed-route records are unchanged.

Next exact action: use the neighborhood pattern, rather than its first two degree moments, on the four-block family in Section 6. Lift edge-disjoint triangles of the eight-vertex quotient by an explicit cyclic construction; account separately for within-core-block edges. Seek a pattern-sensitive bound below n^2/6 for this certificate barrier before proposing a universal extension.
