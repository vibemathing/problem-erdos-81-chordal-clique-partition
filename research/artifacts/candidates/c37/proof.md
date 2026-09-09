# C37: the d7 mixed cone has a lambda-plus-linear actual packing

Candidate: `candidate:erdos81-a01-c37-d7-cone`  
Repository: `vibemathing/problem-erdos-81-chordal-clique-partition`  
Problem: `problem:erdos-81-chordal-clique-partition`  
Attempt: `attempt:web-20260906-erdos81-a01`  
Route: `route:split-extremal-reduction-v1`  
Graph: `graph:erdos81-initial-v1`  
Transport obligation: `obligation:erdos81-split-extremal-reduction`  
Verdict: `candidate_only`. `best_verified_result=none`. `root_closed=false`.

## 1. Scope

Let `G=G(r,A;p,q)` be the two-neighborhood split host.  Its core is
`K_r`; `A` has size `a`; put `C=V\A`, `c=|C|`; there are `p` short
leaves adjacent to `A` and `q` long leaves adjacent to the full core.
Assume

\[
 a\ge3,\qquad c\ge3.                                      \tag{1.1}
\]

Write

\[
 A_0=\binom a2,\quad B=ac,\quad C_0=\binom c2,
 \quad P=ap,\quad U=aq,\quad V=cq.                       \tag{1.2}
\]

C36 proves that the fractional exact edge/triangle partition value is
one of six affine rays.  This candidate treats the cone where

\[
 \lambda=\ell_7=\frac{-3A_0-B+C_0+3P+3U+V}{3}.           \tag{1.3}
\]

Equivalently the corresponding fractional triangle-packing optimum is

\[
 \nu^*=A_0+\frac{2B}{3}+\frac{C_0}{3}+\frac V3.          \tag{1.4}
\]

No equality with `Q`, `L_D`, `J_fix`, `J`, or the integer packing number
`nu` is assumed.  The construction below is an actual edge-disjoint host
triangle packing; all unused graph edges are later singleton clique
blocks.

## 2. Consequences of d7 dominance

Compare `ell_7` with the other effective rays in C36.

- `ell_7>=ell_5` gives `c(q-a)>=0`, hence `q>=a`.
- `ell_7>=ell_6` gives `a(q-c)>=0`, hence `q>=c`.
- `ell_7>=ell_0` gives `p+q>=r-1`.
- `ell_7>=ell_8` gives `q<=r-1`.

Put

\[
 d=r-1-q.                                                \tag{2.1}
\]

Then

\[
 0\le d\le\min(a-1,c-1),\qquad p\ge d.                  \tag{2.2}
\]

These are exactly the inequalities used by the construction.  Ties
between rays cause no problem.

## 3. Good subsets and one shared residual graph

Choose an even `a'<=a` with

\[
 e_A=a-a'\le1.                                           \tag{3.1}
\]

Choose the largest `c'<=c` satisfying `c'=3 mod 6`; then

\[
 e_C=c-c'\le5.                                           \tag{3.2}
\]

Set

\[
 r'=a'+c',\qquad e=e_A+e_C\le6.                         \tag{3.3}
\]

Let `d'` be the largest even integer at most

\[
 \min(d,a'-1,c'-1).                                      \tag{3.4}
\]

The hypotheses (2.2) imply

\[
 0\le d'\le d\le p,
 \qquad d-d'\le e+1.                                    \tag{3.5}
\]

Indeed `a'-1>=d-e_A` and `c'-1>=d-e_C`; taking the minimum and then
rounding down to an even integer loses at most `e+1`.

Only the good core `A' union C'` is used in non-singleton blocks.
Exception vertices remain in the host and their incident edges are not
silently discarded; they are singleton clique blocks in the final
partition.

## 4. Three disjoint owners for good-core edges

### 4.1 Short-leaf matchings on A'

Because `a'` is even, the standard round-robin construction factors
`K_{a'}` into `a'-1` perfect matchings.  Select any `d'` factors and
assign each selected factor to a distinct short leaf.  Every factor edge
`uv` produces the triangle consisting of that leaf and `u,v`.

This contributes

\[
 \frac{a'd'}2                                             \tag{4.1}
\]

actual triangles and uses each selected `AA` core edge once.  The
assignment is legal because `p>=d'`.

### 4.2 Core triangle factors on C'

Since `c'=3 mod 6`, take a resolvable Steiner triple system on `C'` and
select `d'/2` of its triangle factors.  This contributes

\[
 \frac{c'd'}6                                             \tag{4.2}
\]

core triangles and removes degree `d'` at each vertex of `C'`.

The all-order existence of the resolution is the same source-backed
Kirkman input already isolated in C28.  Given the finite factor lists,
every subsequent step is elementary and explicit.  This candidate does
not upgrade that source to a trusted attestation.  For orders `3,9,27`
the accompanying checker uses the affine resolution directly.

### 4.3 One residual graph for all long leaves

Delete the selected `A'` matching edges and selected `C'` triangle-factor
edges from the complete graph on `A' union C'`.  The result `H` is
regular of degree

\[
 \Delta'=r'-1-d'
        =q+(d-d')-e
        \le q+1.                                         \tag{4.3}
\]

By the finite fan recoloring theorem proved in C24's two-level candidate, `H` has a proper edge coloring with at
most `Delta'+1<=q+2` colors.  If more than `q` colors occur, delete the
smallest one or two color classes.  Each class is a matching of size at
most `r'/2`, so the number `D` of deleted residual edges satisfies

\[
 D\le r'.                                                \tag{4.4}
\]

Assign each remaining color class to a distinct long leaf.  Every
colored core edge gives one long-leaf triangle.  Hence all three owners

1. short-leaf matching edges in `A'`,
2. core triangles in `C'`,
3. long-leaf matching edges in `H-D`,

are pairwise edge-disjoint, and every individual leaf receives a genuine
matching.  The same residual edge is never paid once per leaf; the
single edge coloring is performed after all selected short/core factors
have been removed.

## 5. Exact count and linear loss

Before the at-most-two-color deletion, the construction has formal
triangle count

\[
 T_0=\frac{a'd'}2+\frac{c'd'}6
     +\frac{r'(r'-1-d')}2
     =\binom{r'}2-\frac{c'd'}3.                          \tag{5.1}
\]

The actual packing has

\[
 T\ge T_0-r'.                                            \tag{5.2}
\]

Using `q=r-1-d`, equation (1.4) simplifies exactly to

\[
 \nu^*=\binom r2-\frac{cd}{3}.                           \tag{5.3}
\]

Since `c'd'<=cd`,

\[
 \nu^*-T_0
 =\left[\binom r2-\binom{r'}2\right]
   -\frac{cd-c'd'}3
 \le\binom r2-\binom{r'}2
 \le er\le6r.                                           \tag{5.4}
\]

Together with (5.2),

\[
 \boxed{\nu^*(G)-\nu(G)\le7r.}                          \tag{5.5}
\]

The bound remains valid if the intermediate `T_0` happens to exceed the
fractional optimum: only the final actual packing `T` is used.

Fill every unused graph edge by a singleton two-vertex clique.  By the
identity `p23=lambda+2(nu_star-nu)` and `cp<=p23`,

\[
 cp(G)\le\lambda(G)+14r.                                 \tag{5.6}
\]

C22 gives `lambda<=floor(n(n+1)/6)` for chordal graphs.  Therefore every
host in the `d7` cone satisfies

\[
 \boxed{cp(G)\le n^2/6+(14+1/6)n.}                       \tag{5.7}
\]

A coarser integer statement `cp<=n^2/6+15n` is immediate.  This is a
root-strength bound on one quotient cone, not a proof of the full
ProblemContract.

## 6. Boundary and semantic checks

- If `d=0`, take `d'=0`; no short factor or core factor is selected.
  The residual complete graph uses at most `q+2` colors and the same
  deletion bound applies.
- `p=0` can occur in this cone only with `d=0`; there is no division by a
  zero leaf multiplicity.
- Equal short/full prefixes correspond to `c=0` and lie outside (1.1);
  C36 handles the small-side boundary separately.
- Extra short and long leaves not assigned a matching remain vertices;
  their spokes are singleton cliques.
- The construction uses only the object types tight at `d7`: `CCC`
  core triangles, short `alpha`, and long `betaAA,betaAC,betaCC`.
  No `AAA,AAC,ACC` core triangle is inserted.
- Core edges have one owner.  Core triangles, short matching edges, long
  matching edges, and singleton residual edges are disjoint.
- The quarter-valued C25 point and twelfth-valued C27 point are different
  parameter regimes.  No denominator or half-integrality premise is
  used.
- `Q`, `L_D`, `J_fix`, `J`, `nu`, and `lambda` remain distinct.
- The C24 finite fan proof and C28's source-backed Kirkman input are mathematical dependencies; CI and bounded replay are
  not evidence for them.

## 7. Pressure tests and next cone

The checker verifies two million bounded parameter rows, including all
`d7` dominance implications, the parity/divisibility rounding of
`a',c',d'`, the degree bound `Delta'<=q+1`, and the exact count (5.1).
It constructs actual edge-colored witnesses in seven small cases,
checks affine triangle-factor resolutions at orders `3,9,27`, and
rejects twelve mutations.  This finite work tests implementation only.

After C36 and this candidate, the nondegenerate two-neighborhood model
has only three unresolved effective rays: `d3,d5,d6`.  The next route is
`d6`, whose dominance forces `p>=a-1`, `c>=a`, and `q<=c`.  Its tight
support is `ACC,CCC,alpha,betaAC,betaCC`; the unresolved object is a
single compatible completion of the `A x long x C` Latin rectangle and
the remaining `C`-edge factors.  No result for that cone is claimed here.
