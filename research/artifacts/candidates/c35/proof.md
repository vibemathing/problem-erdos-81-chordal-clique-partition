# C35: quadratic-margin absorption on the full one-third two-neighborhood face

Candidate: `candidate:erdos81-a01-c35-face-margin`  
Repository: `vibemathing/problem-erdos-81-chordal-clique-partition`  
Problem: `problem:erdos-81-chordal-clique-partition`  
Attempt: `attempt:web-20260906-erdos81-a01`  
Route: `route:split-extremal-reduction-v1`  
Graph: `graph:erdos81-initial-v1`  
Transport obligation: `obligation:erdos81-split-extremal-reduction`  
Fresh base: `3af18d3b9a5890783fd70c651c38d54bf291353e`  
Verdict: `candidate_only`. `best_verified_result=none`. `root_closed=false`.

## 1. Scope and the route correction

Let `G=G(r,A;p,q)` be the two-neighborhood split host.  Its core is
`K_r`; `A` is an actual subset of the core of size `a`; there are `p`
independent short leaves adjacent exactly to `A` and `q` independent
long leaves adjacent to the whole core.  Put

\[
 s=p+q,\qquad n=r+s,\qquad
 M=\binom r2,\qquad m=|E(G)|=M+ap+rq.
\]

All vertices, including isolated short leaves when `a=0`, count in `n`.
A clique partition is exact and edge-disjoint.

Write `nu,nu_star` for integer and fractional edge-disjoint triangle
packing, `p23` for exact partition into edges and triangles, and
`lambda` for its fractional exact-partition relaxation.  The identities

\[
 p_{23}=m-2\nu,\qquad
 \lambda=m-2\nu^*,\qquad
 p_{23}=\lambda+2(\nu^*-\nu),                    \tag{1}
\]

and `cp<=p23` are the C22 identities, rechecked here algebraically.

The **full one-third face** means

\[
 \nu^*(G)=m/3,
 \quad\text{equivalently}\quad
 \lambda(G)=m/3.                                \tag{2}
\]

It is an optimality statement, not merely feasibility of the all-one-third
dual.  C28 gives a scalar membership test in its stated nondegenerate
domain, and C29--C33 provide explicit saturated points in several
subdomains.

C32--C34 pursue the stronger statement `nu_star-nu=O(r)` by explicit
actual packings.  This candidate proves that the unresolved one-buffer
part of the full one-third face does **not** need that stronger statement
in order to satisfy the original `n^2/6+O(n)` inequality.  A quadratic
margin in the number of leaves absorbs the uniform `o(n^2)` packing
error.  The stronger linear packing-gap problem remains open.

## 2. Uniform packing input

Define

\[
 \gamma(n)=\max\{\nu^*(H)-\nu(H): |V(H)|=n\}.
\]

C22 derives, from the fixed-`K_3` Haxell--Rödl/Yuster input with the
isolated-vertex bridge,

\[
 \gamma(n)=o(n^2)                                      \tag{3}
\]

uniformly over all finite simple `n`-vertex graphs.  The quantifiers used
below are exactly

\[
 \forall\epsilon>0\ \exists N_\epsilon\
 \forall n>N_\epsilon\ \forall H,\qquad
 \nu^*(H)-\nu(H)<\epsilon n^2.                         \tag{4}
\]

No choice `epsilon=1/n` is made.  This is a source-backed dependency, not
a trusted verifier receipt.

## 3. Sparse-leaf direct partition

The core `K_r` is one clique.  Cover every leaf--core edge by a singleton
edge clique.  This gives

\[
 cp(G)\le 1+ap+rq\le 1+rs.                             \tag{5}
\]

Let

\[
 \tau=2-\sqrt3.
\]

If `s<=tau r`, then

\[
 6rs\le(r+s)^2                                        \tag{6}
\]

because, for `t=s/r`, the inequality is
`t^2-4t+1>=0` on `0<=t<=2-sqrt3`.  Therefore

\[
 cp(G)\le n^2/6+1.                                    \tag{7}
\]

This step does not assume the one-third face, chordality beyond the
displayed split structure, or any triangle packing.

## 4. Exact quadratic margin on the one-third face

Since `a<=r`,

\[
 m=M+ap+rq\le M+rs.
\]

The difference from the target quadratic term is the exact identity

\[
 \frac{n^2}{6}-\frac{M+rs}{3}
 =\frac{s^2+r}{6}.                                    \tag{8}
\]

Consequently, on the full one-third face,

\[
\begin{aligned}
 cp(G)
 &\le p_{23}(G)\\
 &=\frac m3+2(\nu^*-\nu)\\
 &\le \frac{n^2}{6}-\frac{s^2+r}{6}+2\gamma(n).
                                                               \tag{9}
\end{aligned}
\]

No floor term is lost: equation (9) compares directly with `n^2/6`.

Assume now `s>tau r`.  Then

\[
 \frac{s}{n}>\frac{\tau}{1+\tau}
             =\frac{3-\sqrt3}{6},
\quad
 \left(\frac{\tau}{1+\tau}\right)^2=\frac{\tau}{6}.
\]

Thus

\[
 \frac{s^2}{6}>\frac{\tau n^2}{36}.                    \tag{10}
\]

Fix once and for all

\[
 \epsilon=\tau/144.
\]

For every `n>N_epsilon`, (4), (9), and (10) give

\[
 cp(G)
 <\frac{n^2}{6}-\frac{\tau n^2}{36}
                  +\frac{\tau n^2}{72}
 <\frac{n^2}{6}.                                      \tag{11}
\]

Combining (7) and (11) proves the following class theorem.

### Theorem 4.1 — full-face root-strength bound

There is a universal integer `n_0` such that every full-one-third-face
two-neighborhood split host on `n>=n_0` vertices satisfies

\[
 \boxed{cp(G)\le n^2/6+1\le n^2/6+n.}                  \tag{12}
\]

Hence the frozen ProblemContract inequality holds on this whole class
with `C=1`, including every full-face parameter region left unresolved by C33/C34 exact packing constructions.
This does not determine `nu`, prove `nu_star-nu=O(r)`, or close the
ProblemContract for arbitrary chordal graphs.

## 5. Face-excess localization

For an arbitrary two-neighborhood split host define the nonnegative
face excess

\[
 \Delta_f(G)=\lambda(G)-m/3.                            \tag{13}
\]

Nonnegativity follows from `lambda=m-2nu_star` and `nu_star<=m/3`.
Repeating the preceding calculation without (2) gives the exact
screening inequality

\[
 \boxed{
 cp(G)\le
 \frac{n^2}{6}
 +\Delta_f(G)+2\gamma(n)-\frac{s^2+r}{6}.
 }                                                     \tag{14}
\]

Therefore:

1. if `s<=tau r`, the source-free direct partition (7) applies;
2. if `s>tau r` and a family has `Delta_f=o(n^2)` uniformly, then (14)
   and (3) eventually give `cp<n^2/6`;
3. any asymptotic two-neighborhood obstruction outside the direct region
   must have genuinely quadratic face excess.  More precisely, if
   `cp(G)>n^2/6+Cn`, then
   \[
   \Delta_f(G)>
   \frac{s^2+r}{6}-2\gamma(n)+Cn.                       \tag{15}
   \]

Thus further root-directed work should move from the already safe
one-third face to the high-excess, nonuniform-dual regime.  Equation
(15) is a necessary condition, not an existence assertion.

## 6. Complete-split pressure test

Let `J(x,y)=K_x join overline(K_y)`.  C22 gives

\[
 \lambda(J(x,y))=
 \begin{cases}
 (xy+\binom x2)/3,&y\le x-1,\\
 xy-\binom x2,&y\ge x-1.
 \end{cases}                                          \tag{16}
\]

The formulas agree at the boundary.  Hence its face excess is

\[
 \Delta_f(J(x,y))=
 \begin{cases}
 0,&y\le x-1,\\
 2x(y-x+1)/3,&y\ge x-1.
 \end{cases}                                          \tag{17}
\]

The high-leaf complete-split extremizers therefore lie exactly in the
quadratic-excess route isolated by (15); they are not falsely declared
safe by Theorem 4.1.

For completeness, the high branch has a direct integer construction.
If `x` is even, factor `K_x` into `x-1` perfect matchings.  If
`y>=x-1`, assign those matchings to distinct outside vertices and lift
each matching edge to a triangle.  If `x` is odd, factor `K_x` into `x`
near-perfect matchings; for `y>=x`, do the same and cover each unmatched
spoke by a singleton edge.  These constructions use
`xy-binomial(x,2)=lambda` pieces.  At the sole odd boundary `y=x-1`,
omit one near-perfect class; the same construction uses at most

\[
 \lambda(J(x,x-1))+(x-1)                               \tag{18}
\]

pieces.  Small `x` is direct.  With `lambda<=B(x+y)`, this gives a
linear root allowance on the whole high branch.  The low branch is
covered by Theorem 4.1.  Thus complete-split graphs themselves do not
supply a counterexample to (12)'s extension; the remaining issue is
non-complete high-excess structure.

## 7. Two exact edge decompositions and additional root-safe regions

Two source-free decompositions help localize that structure.

First, the subgraph on the core and the `q` long leaves is `J(r,q)`.
The remaining `p a` short-leaf edges are disjoint singleton cliques, so

\[
 cp(G)\le cp(J(r,q))+ap.                               \tag{19}
\]

Second, split the edge set into

\[
 H_A=J(a,p+q)
\]

on core `A` and all leaves, and

\[
 H_C=J(r-a,a+q)
\]

on core `V\A`, with outside set `A` together with the `q` long leaves.
The two edge sets are disjoint and their union is exactly `E(G)`, so

\[
 cp(G)\le cp(J(a,p+q))+cp(J(r-a,a+q)).                 \tag{20}
\]

The complete-split discussion implies the existence of a universal
constant `C_*` and threshold such that every complete-split graph of
order `h` has at most `h^2/6+C_*h` pieces.  For components below the
threshold, the crude `binom(h,2)` bound enlarges `C_*` finitely.

Equation (19) gives a root-strength bound whenever `p=0` or

\[
 6a\le 2(r+q)+p,                                       \tag{21}
\]

because then

\[
 ap\le\frac{(r+p+q)^2-(r+q)^2}{6}.
\]

Equation (20) gives a root-strength bound whenever

\[
 (a+p+q)^2+(r+q)^2\le(r+p+q)^2,                        \tag{22}
\]

equivalently

\[
 a^2+2a(p+q)+q^2\le2pr.                                \tag{23}
\]

In (22), the two component orders sum to at most `2n`, so the linear
allowances remain `O(n)`.  These conditions are sufficient only; their
failure is not a counterexample.

## 8. Boundary and semantic audit

- `a=0`: short leaves may be isolated.  They still count in `n`;
  equations (5), (8), and (14) remain valid.
- `p=0` or `q=0`: no division by the absent multiplicity occurs.
- `A=V`: the equal-prefix graph is allowed; `m<=M+rs` remains exact.
- C25's quarter-valued point is outside the full face and is not covered
  by Theorem 4.1.
- C27's twelfth-denominator point is on the face; denominators of an
  optimum are irrelevant to the margin proof.
- C29--C33 retain their stronger finite/all-order actual-packing
  conclusions.  Theorem 4.1 neither identifies `Q,L_D,J_fix,J,nu` nor
  replaces their edge-ownership audits.
- The all-one-third dual being feasible does not imply (2).  A saturated
  primal or an exact criterion such as C28 is required.
- The empty-response frontend event is not a failed mathematical route.
- CI, this manuscript, and the finite checker are not trusted evidence.

## 9. Pressure tests and next obligation

The accompanying `checker.py` and frozen `results.json` perform:

1. exact integer verification of (6), (8), (14), (21), and (23);
2. explicit edge-ownership checks for decomposition (20);
3. round-robin complete-graph matching factorizations and all high-branch
   complete-split partitions through the bounded range;
4. exact `cp` and integer triangle-packing optimization for every
   two-neighborhood parameter representation with at most eight vertices;
5. C28 face-criterion enumeration on bounded nondegenerate parameters;
6. twelve negative mutations, including the wrong sign in (8), omission
   of the factor two in (1), use of all-one-third feasibility as
   optimality, and overlap of the two decomposition edge sets.

The finite runs test the implementation and small boundaries; they do
not prove (3) or any universal statement.

The first open root-directed lemma is now:

> characterize or dominate the two-neighborhood hosts with
> `s>tau r` and quadratic `Delta_f`, beyond the complete-split and
> sufficient regions (21), (23).

The stronger C33/C34 one-buffer statement `nu_star-nu=O(r)` remains open,
but it is no longer a prerequisite for the root inequality on the full
one-third face.  General split domination, arbitrary chordal graphs,
and trusted closure remain open.
