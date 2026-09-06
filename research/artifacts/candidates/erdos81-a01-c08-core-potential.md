# C08: core-edge allocation potentials aimed at the quadratic coefficient

Candidate ID: `candidate:erdos81-a01-c08-core-potential`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `2f3aafc2fa13b6df22c5d2353f840ef22ced5db5`
Verdict: `candidate_only`.

## 1. Root-facing claims and scope

For any fixed real A>=0, the following restricted root bounds are proved as natural-language candidates.

(I) If a chordal graph G has a maximum clique Q of size r<=n/2 and
    delta+e(G-Q)<=A n,
then
    cp(G)<=n^2/6+(2A+1)n.

(II) If a chordal graph G has a maximum clique Q of size r<=n/3 and
    cp(G-Q)<=A n,
then
    cp(G)<=n^2/6+(A+1)n.
In particular (II) applies with A=1 when G-Q is a disjoint union of cliques. It does not require e(G-Q)=O(n).

These are uniform statements on explicitly restricted infinite classes, not a universal solution of the root or of same-order split domination. The rest of the artifact supplies the quantitative potentials, proofs, and an obstruction to removing the restrictions by appealing only to small delta.

All graphs are finite and simple; cp means an exact edge partition into nonempty complete subgraphs. A split core is not assumed. The only reused constructions are the explicit matching decomposition of a complete graph in C01 and the PEO edge envelope in C02. C06 explains why a whole maximum clique cannot always be retained as one piece; C07 supplies the exact residual-state model. No mathematical computation, random experiment, enumerator, solver, or proof assistant was executed. The averaging below is a finite existence proof. No novelty assertion is made.

## 2. C08.1: finite matching-assignment bound for any clique core

Let Q be an r-clique, r>=2, in ANY graph G. Write R=V(G)-Q, t=|R|>=1,
    d_x=|N(x) intersect Q| for x in R,
    a=sum_x d_x=e(Q,R), h=e(G[R]), q=binom(r,2).
Partition E(K_Q) into c matchings, where c=r for odd r and c=r-1 for even r. C01 gives the explicit cyclic construction. Put D=max(c,t).

There exist edge-disjoint triangles, each using two Q vertices and one R vertex, in number at least
    (1/D) sum_(x in R) binom(d_x,2).                       (1)

For t>=c, choose uniformly an injection from the c matching classes to R. A class assigned to x supplies its edges with both endpoints in N(x) as triangles through x. For t<c, choose uniformly an injection from R into the matching classes and use the assigned class at each x. In either case classes and outside vertices are used at most once. Within a class the edges are a matching; hence no crossing edge repeats. Distinct classes use disjoint core edges. The triangles are therefore edge-disjoint, even when R has many internal edges.

For each fixed x, summing its usable edges over all c classes gives binom(d_x,2). The probability that a particular x-class pair is assigned is 1/D in either construction. The expected number of triangles is thus the right side of (1). Some injection attains at least that finite average. This does not assert a particular randomized run.

Partition G[R] optimally, use these triangles, and use all unused core and crossing edges singly. No triangle uses an edge of G[R]. Consequently
    cp(G)<=cp(G[R])+a+q-(2/D)sum_x binom(d_x,2).            (2)
Replacing cp(G[R]) by h yields a fully explicit bound. The right side need not be an integer; the integer triangle count may strengthen it.

A weaker expression depending only on a is
    cp(G)<=cp(G[R])+a+q-(a^2/t-a)/D,                      (3)
because sum_x d_x^2>=a^2/t. The second-moment bound (2), rather than (3), can retain useful neighborhood heterogeneity. The identity
    t sum_x d_x^2-a^2=sum_(x<y)(d_x-d_y)^2
proves the needed inequality without a numerical calculation.

## 3. C08.2: a linear missing-neighbor bound

Assume t>=r, and put M=rt-a. Then there is such a triangle packing of size at least
    q-rM/t.                                               (4)

Use the c matching classes, choose c vertices of R with the smallest missing-neighbor counts r-d_x, and assign the classes bijectively to them. The sum of these c counts is at most cM/t. For a fixed assigned vertex, deleting the matching edges that touch a missing neighbor removes at most one matching edge per missing neighbor. Thus across all classes at most cM/t core edges are lost; every retained core edge supplies a triangle. Since c<=r, (4) follows.

This proof does not assume M small. If the lower bound in (4) is negative it is simply uninformative; the resulting upper inequality remains valid. It also shows why only the number of missing neighbors, not the edge pattern inside R, matters for this particular packing.

Using the same assembly as in Section 2 gives
    cp(G)<=cp(G[R])+rt-q+(2r/t-1)M.                       (5)

## 4. C08.3: chordal deficit potentials and their root consequences

Now Q is a maximum clique in a chordal G, r=omega(G)>=2, t=n-r>=r. Let
    delta=(r-1)n-binom(r,2)-m.
The exact edge count m=q+a+h gives
    M=t+delta+h.                                          (6)

Substituting (6) into (5) yields the recursive core-allocation potential
    cp(G)<=g(n,r)+2r+(2r/t-1)(delta+h)+cp(G[R]),            (7)
where
    g(n,r)=(r-1)t-binom(r,2).

Using cp(G[R])<=h gives the explicit bound
    cp(G)<=g(n,r)+2r+(2r/t-1)delta+(2r/t)h.                (8)
It can be combined with, rather than substituted for, the intact-clique bound:
    cp(G)<=min{(r-1)t+1-delta,
               g(n,r)+2r+(2r/t-1)delta+(2r/t)h}.          (9)

The exact quadratic identity is
    g(n,r)=n^2/6-n/2+3/8
            -(3/2)(r-n/3-1/2)^2.                         (10)
For t>=r, 2r<=n, 2r/t<=2, and 2r/t-1<=1. Thus (8) gives
    cp(G)<=n^2/6+n/2+3/8+delta+2h
            -(3/2)(r-n/3-1/2)^2.                         (11)

If delta+h<=A n, drop the nonpositive square and use delta+2h<=2A n. Since n/2+3/8<=n for integers n>=1, this proves claim (I).

For r<=n/3, the coefficient 2r/t-1 in (7) is nonpositive, and delta+h>=0. Dropping that term and the square gives
    cp(G)<=n^2/6+n/2+3/8+cp(G[R]).
This proves claim (II). If G[R] is a disjoint union of cliques, use each component with an edge once, so cp(G[R])<=t<=n. Edgeless input graphs, omitted by r>=2, have cp=0 and satisfy both upper claims whenever their stated core conditions apply.

The extremal center of the new quadratic g is r=n/3+1/2, not the r approximately n/2 center of the crude (r-1)(n-r) expression. The negative square in (11) quantifies how much deficit or outside-edge cost can be absorbed away from that center. No hypothesis that delta or h is universally linear is made.

## 5. C08.4: a complementary disjoint-clique potential

For vertex-disjoint cliques Q_1,...,Q_p, each of size at least two, in ANY graph G,
    cp(G)<=m-sum_j binom(|Q_j|,2)+p.                      (12)
Use these cliques and all other edges singly. More generally only edge-disjointness is needed, but vertex-disjointness is a convenient checkable condition.

Bounds (2), (7), (9), and (12) may be minimized over available cores or clique families. They need not be realized by one common partition: each is a separate valid construction. A general root proof cannot add their savings unless the corresponding pieces are actually edge-disjoint.

## 6. C08.5: small deficit does not ensure sparse outside edges

For every k>=3, let G=P_(3k+1)^k have vertices 1,...,3k+1 and edges ij exactly when 0<|i-j|<=k. The increasing ordering is a PEO, every maximal clique is a consecutive window of k+1 vertices, and
    n=3k+1, r=k+1, m=kn-binom(k+1,2), delta=0.

For any maximum clique window Q, its complement is a prefix of size a and a suffix of size b, with a+b=2k. There are no edges between the prefix and suffix. Define
    f(s)=binom(s,2) for s<=k+1,
    f(s)=ks-binom(k+1,2) for s>=k+1.
Thus h=e(G-Q)=f(a)+f(b). Relabel the two sides so a<=k<=b. Direct subtraction gives
    h-k(k-1)=(k-a)(k-a+1)/2>=0.                           (13)
In particular every maximum clique has h>=k(k-1), although delta=0. No bound h<=C(delta+1)n with universal C can hold for all chordal graphs.

This family does NOT contradict the root. Take three disjoint consecutive cliques with sizes k+1, k+1, and k-1. Formula (12) gives
    cp(G)<=k^2+k+2=(1/9)n^2+O(n).                         (14)
All cliques in this construction are displayed; no graph search or exact optimum is claimed.

It also illustrates the value of the recursive version (7). For the central window Q, the residual is two K_k components, so cp(G-Q)=2 despite h=k(k-1). Here t=2k and 2r/t-1=1/k. Formula (7) yields
    cp(G)<=(3k^2+5k)/2+3=n^2/6+O(n).
This latter estimate is weaker than (14), but succeeds without pretending h is linear. Claim (II)'s exact r<=n/3 condition is not applied here, since r=k+1 exceeds n/3; the explicit 1/k coefficient is used instead.

## 7. Audit, unresolved mechanism, and checkpoint

Checked assumptions: t<c versus t>=c in the injection average; even r with c=r-1; zero neighborhood size; no consumption of G[R] edges by the triangles; t>=r only where (4)-(11) need it; the sign change at r=n/3; all maximum cliques of the path power; and not adding savings from incompatible constructions.

The root-facing gap is now quantitative. One needs a uniform core or clique-family selection mechanism making a bound such as (7) or (12) at most n^2/6+Cn. Outside-edge cardinality alone cannot do this by (13), while C06 rules out always choosing an intact maximum clique. A faithful refinement may recurse on G[R] and retain how much of each separator's edge set has been spent, as in C07. None of these selection or charging assertions is assumed.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: the explicit potentials and restricted infinite-class bounds above.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
No mathematical execution or verifier receipt exists. Canonical failed-route records remain unchanged.

Next exact action: test a clique-tree core-selection dichotomy using (7) with the actual residual partition cost, not h. Isolate a quantitative inequality which charges residual cp against the negative deficit term or against a disjoint-clique saving; attack it first on complete split graphs, path powers, and the C06 family.
