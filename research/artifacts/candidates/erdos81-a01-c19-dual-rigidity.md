# C19: dual slack, exact fractional extremizers, and a sharp one-unit gap

Candidate ID: `candidate:erdos81-a01-c19-dual-rigidity`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `9c1cd6894f94c3204dddcceb683e637417977002`
Primary owner: math-proof. Verdict: candidate_only.

## 1. Scope and dependency

This cycle audits equality and small slack in C18's FRACTIONAL compression. It does not assert an integer extremal theorem for all chordal graphs. The admitted target and root remain open.

Use C18's notation: lambda is the equality-constrained fractional edge-and-triangle partition minimum; cp_f allows all clique sizes; cp and p23 are integer parameters. Put B(n)=floor(n(n+1)/6), and J(r,t)=K_r joined to t pairwise nonadjacent vertices.

Dependency: `research/artifacts/candidates/erdos81-a01-c18-fractional-compression.md`, including its explicitly scoped finite LP duality and clique-suffix PEO arguments. C01 supplies the matching partition of the complete-split benchmark. All are proof drafts requiring joint audit; transport is not evidence. Only finite graph arguments and real arithmetic are used below. No mathematical code, LP solver, enumeration or proof assistant was executed; no novelty claim.

Main candidate: for n>=5 and chordal G, either G is an extremal complete split graph listed in Section 4, or
    lambda(G)<=B(n)-1 and cp_f(G)<=B(n)-1.                (1)
The unit cannot be improved uniformly, by Section 5.

## 2. C19.1: an exact slack identity

Take feasible real signed dual weights w, so every edge has weight at most one and every triangle has total weight at most one. Choose a pair u,S attaining the positive maximum
    M=max_(v,C clique in N(v)) sum_(x in C)w_(vx).
Let r=|S|, t=n-r, and choose a PEO ending at S. For each v outside S, let c_v be its weighted later degree.

Define nonnegative quantities
    p_a=1-w_(ua),                 a in S;
    P=sum_(a in S)p_a=r-M;
    h_ab=-1+p_a+p_b-w_(ab),       {a,b} in E(S);
    R=sum_(ab in E(S))h_ab;
    a_v=M-c_v,                   v outside S;
    D=sum_(v outside S)a_v.
The h_ab are nonnegative by the triangle uab constraint. The a_v are nonnegative by maximality of M. Also p_a>=0 by edge constraints; in fact w_(ua)>=0 since removing a negative summand would improve the selected clique neighborhood.

Set theta=t-r+1 and g_n(r)=rt-binom(r,2). Summing first the core weights and then the PEO forward weights gives the EXACT identity
    W:=sum_e w_e = g_n(r)-theta*P-R-D.                    (2)
Indeed w(E(S))=-binom(r,2)+(r-1)P-R and the outside contribution is t(r-P)-D.

There is another useful bound on negative weights. Remove all negative-weight neighbors from the later-neighbor clique of a vertex v. The remaining subset is still a clique, and its weighted sum is at most M. Hence the sum of absolute negative weights in that row is at most a_v. Every edge outside E(S) occurs in exactly one such row, so
    sum_(e outside E(S), w_e<0) |w_e| <= D.               (3)
In particular, for any forward edge vz, w_(vz)>=-a_v.

For an optimal dual put s=B(n)-lambda(G)>=0. When theta>=0, (2) and C18's integer bound g_n(r)<=B(n) give
    B(n)-g_n(r)<=s,  theta*P+R+D<=s.                     (4)
If theta>0, then P<=s/theta. This is a bound on weighted slack, not an unproved edit-distance conclusion.

For completeness, with rho_n=(n+1/2)^2/6-B(n), completing the square gives
    (3/2)*(r-(2n+1)/6)^2+theta*P+R+D=s+rho_n,            (5)
where rho_n=1/24 for n congruent to 0 or 2 modulo 3, and rho_n=3/8 otherwise. Under theta>=0,
    |r-(2n+1)/6|<=sqrt(2s/3+1/4).
No nonnegative-slack conclusion is made from theta*P when theta<0.

## 3. C19.2: a last bad vertex costs at least one unit

Assume r>=2 and theta>=2. If G is not J(r,t) with core S, then
    g_n(r)-W>=1.                                       (6)

To prove this, call an outside vertex good if its later-neighbor set is EXACTLY S. If every outside vertex is good, all crossing edges are present and no outside edge exists, giving J(r,t). Otherwise choose the LAST bad vertex v in the PEO.

Every later outside vertex z is good. Thus the later outside vertices are pairwise nonadjacent and each is joined to all of S. Since the later-neighbor set of v is a clique, it contains at most one later outside vertex.

If it contains none, then v is missing some neighbor of S. The edge upper bounds give c_v<=r-1. Since c_v=r-P-a_v,
    P+a_v>=1.
Equation (2) gives g_n(r)-W=theta*P+R+D>=1.

Suppose instead it contains one later outside vertex z. Put k=|N(v) intersect S|. If k=0, then c_v=w_(vz)<=1, so P+a_v>=r-1>=1, and the same argument applies.

It remains that 1<=k<=r. Because z is good, its row is exactly S and
    sum_(a in S)(1-w_(za))=P+a_z.
Each summand is nonnegative, so w_(za)>=1-P-a_z for every a in S. For a in N(v) intersect S, the triangle vza implies
    w_(va)<=P+a_z-w_(vz).
Consequently, using (3),
    c_v=w_(vz)+sum_(a in N(v) intersect S)w_(va)
       <=k(P+a_z)-(k-1)w_(vz)
       <=k(P+a_z)+(k-1)a_v.
Substitute c_v=r-P-a_v and rearrange:
    r<=(k+1)P+k(a_v+a_z)
      <=(r+1)P+r(a_v+a_z).
Thus
    1<=(1+1/r)P+a_v+a_z<=theta*P+D<=g_n(r)-W.
The middle inequality uses r>=2, theta>=2, and that v,z are distinct outside vertices. This proves (6), without assuming individual noncore weights are nonnegative.

## 4. C19.3: classification and the fractional gap

Suppose n>=5 and lambda(G)>B(n)-1. It is positive, so C18 supplies an optimal dual and a positive maximum pair u,S.

If t<r-1, C18's second complete-split branch gives
    lambda(G)<=n(n-1)/6<=B(n)-(n-1)/3<B(n)-1.
Here B(n)>=n(n+1)/6-1/3; the strict inequality uses n>=5. This is impossible.

Otherwise theta>=0, and (2) gives
    B(n)-1<lambda(G)<=g_n(r)<=B(n).
The last two quantities g_n(r),B(n) are integers, so g_n(r)=B(n). The exact difference
    g_n(r+1)-g_n(r)=n-3r-1
classifies its integer maximizers:
    n=3q:       r=q;
    n=3q+1:     r=q or q+1;
    n=3q+2:     r=q+1.                                 (7)
For n>=5 all these r satisfy r>=2, t>=r and theta>=2.

If G were not J(r,t) with this core, (6) would give lambda(G)<=g_n(r)-1=B(n)-1, again impossible. Therefore G is one of the complete split graphs in (7). C01 and C18 provide
    cp(G)=cp_f(G)=lambda(G)=B(n)                          (8)
for each listed graph. This proves (1), including the assertion that there is no fractional value strictly between B(n)-1 and B(n).

It also classifies the full-clique fractional extremizers: cp_f(G)>B(n)-1 implies lambda(G)>B(n)-1 and hence (7)-(8). No conclusion that an INTEGER extremizer cp(G)=B(n) must have this structure follows.

The n>=5 hypothesis is necessary for the stated classification. On four vertices the path P4 has lambda=3=B(4), while it is not J(1,3) or J(2,2). Its maximizing weighted neighborhood can have r=1, precisely a case excluded in (6).

## 5. C19.4: the unit gap is sharp at every n>=5

Choose the smaller maximizing r=floor((n+1)/3) and t=n-r. Start with J(r,t) and delete one crossing edge xa. This graph remains split and hence chordal. The old signed dual, restricted to the remaining edges, is still feasible for ALL clique inequalities and has total B(n)-1.

Since t-1>=r for this choice and n>=5, assign the at most r matching colors of the core K_r to outside vertices OTHER than x, as in C01. Use those triangles and every remaining crossing edge singly. No triangle uses the deleted edge, and the count is
    (rt-1)-binom(r,2)=B(n)-1.
Thus cp_f=lambda=cp=B(n)-1.

This graph is not one of the extremizers in (7): x has degree r-1, whereas the minimum degree of any listed extremal J is at least the chosen smaller r. Hence the gap in (1) cannot be enlarged. The witness is not a counterexample to either admitted obligation.

## 6. Dense branch and limits of quantitative interpretation

When t<r-1, the precise C18 bound is
    lambda(G)<=[binom(n,2)-binom(t,2)]/3.
Therefore
    s>=B(n)-n(n-1)/6+t(t-1)/6.                           (9)
Near-maximal fractional value can still occur in this branch with an almost complete core, not with r close to n/3. For example lambda(K_n)=n(n-1)/6 for n>=3, while cp(K_n)=1. Its slack is only about n/3, despite its very different structure.

Thus (5) is a LOW-CORE-BRANCH statement, not a stability theorem for all near-maximal lambda. The dense branch must be handled separately, for example by using the large clique S as a single integer piece. From a clique of size n-t the elementary bound is
    cp(G)<=|E(G)|-binom(n-t,2)+1
          <=(n-t)t+binom(t,2)+1.                        (10)
No general bound of the required strength on the residual integer rounding term is inferred here.

## 7. Audit and continuation

Audited: the selected clique can omit negative summands; signs in theta; the exact core multiplicity r-1 in (2); charging all negative forward edges once; the definition of the LAST bad vertex; the at-most-one later outside neighbor forced by the PEO; k=0; both deficits a_v,a_z in the triangle estimate; n modulo three; n=5,6,7; P4 as a genuine small-order exception; and the missing-edge witness with t-1>=r.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: exact fractional extremizers and the sharp one-unit gap, conditional on joint audit of C18.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
failed_routes: canonical ledger unchanged. Do not apply the low-core slack estimate to the dense branch, or turn weighted slack into an edit bound without proof.

Next action: combine the two fractional branches with rigorous integer packing estimates. In particular, quantify the remaining excess 2(nu_star-nu)-s, and test rounding statements on clique sums as well as complete split graphs. A general o(n^2) packing theorem, if sourced and reused, would improve the asymptotic remainder only to o(n^2), not to O(n).
