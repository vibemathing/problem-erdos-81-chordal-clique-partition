# C36: exact quotient dual and six effective rays

Candidate: `candidate:erdos81-a01-c36-six-ray-dual`  
Repository: `vibemathing/problem-erdos-81-chordal-clique-partition`  
Problem: `problem:erdos-81-chordal-clique-partition`  
Attempt: `attempt:web-20260906-erdos81-a01`  
Route: `route:split-extremal-reduction-v1`  
Graph: `graph:erdos81-initial-v1`  
Transport obligation: `obligation:erdos81-split-extremal-reduction`  
Fresh base: `193e0c9d758b004c219c157e402c9075657939ae`  
Verdict: `candidate_only`. `best_verified_result=none`. `root_closed=false`.

## 1. Frozen model

Let `G=G(r,A;p,q)` be the two-neighborhood split host.  Its core is
`K_r`; `A` is an actual subset of size `a`; put `C=V\A` and `c=r-a`.
There are `p` independent short leaves adjacent exactly to `A` and `q`
independent long leaves adjacent to all core vertices.

This manuscript assumes

\[
a\ge3,\qquad c\ge3.                                      \tag{1.1}
\]

The small-side boundary is disposed of in Section 7.  Zero
multiplicities are allowed.

Write

\[
 A_0=\binom a2,\quad B=ac,\quad C_0=\binom c2,\quad
 P=ap,\quad U=aq,\quad V=cq.                             \tag{1.2}
\]

Here `A_0,B,C_0` count core edges of types `AA,AC,CC`; `P,U,V`
count short endpoint, long-A endpoint, and long-C endpoint capacities.

Let `nu_star` be the fractional edge-disjoint triangle-packing optimum,
and put

\[
 \lambda=|E(G)|-2\nu^*(G).                               \tag{1.3}
\]

This is the fractional exact edge/triangle partition value from C22.
It is not `Q`, `L_D`, `J_fix`, `J`, or the integer packing number `nu`.

## 2. Exact eight-column quotient primal

Average a feasible fractional packing under all permutations within
`A`, within `C`, and within each leaf class.  Let

- `t3,t2,t1,t0` be the **total** weights of core triangles of types
  `AAA,AAC,ACC,CCC`;
- `alpha` be total short-leaf triangle weight;
- `beta2,beta1,beta0` be total long-leaf triangle weights whose core
  edge has type `AA,AC,CC`.

The averaged capacity inequalities are exactly

\[
\begin{array}{rcl}
3t_3+t_2+\alpha+\beta_2&\le&A_0,\\
2t_2+2t_1+\beta_1&\le&B,\\
t_1+3t_0+\beta_0&\le&C_0,\\
2\alpha&\le&P,\\
2\beta_2+\beta_1&\le&U,\\
\beta_1+2\beta_0&\le&V,
\end{array}                                               \tag{2.1}
\]
with all eight variables nonnegative, and the objective is their sum.

Conversely, every point satisfying (2.1) lifts to the original graph:
distribute each total uniformly over all actual objects of its type.
Every edge of one type then receives its type-total divided by the
number of such edges; every tagged endpoint receives its incidence
total divided by `a` or `c`.  The six inequalities are precisely the
resulting per-edge and per-endpoint inequalities.  Empty leaf classes
carry zero weight and require no division.

Therefore (2.1) is not a relaxation of the symmetric problem:

\[
 \nu^*(G)=\max\{\mathbf1^\mathsf T x:Mx\le
 (A_0,B,C_0,P,U,V),\ x\ge0\}.                            \tag{2.2}
\]

The hypothesis (1.1) is essential to this fixed list of eight object
types.  If a core part has fewer than three vertices, nonexistent
triangle columns must be removed rather than retained formally.

## 3. The fixed dual polyhedron

The dual variables are

\[
 y=(y_{AA},y_{AC},y_{CC},y_S,y_{LA},y_{LC})\ge0.
\]

The eight column constraints are

\[
\begin{array}{rclcrcl}
3y_{AA}&\ge&1,&&y_{AA}+2y_{AC}&\ge&1,\\
2y_{AC}+y_{CC}&\ge&1,&&3y_{CC}&\ge&1,\\
y_{AA}+2y_S&\ge&1,&&y_{AA}+2y_{LA}&\ge&1,\\
y_{AC}+y_{LA}+y_{LC}&\ge&1,&&y_{CC}+2y_{LC}&\ge&1.
\end{array}                                               \tag{3.1}
\]

An exact rational enumeration of all choices of six independent active
constraints among the eight rows of (3.1) and the six nonnegativity
rows gives exactly these nine vertices:

\[
\begin{array}{c|c}
d_0&(1/3,1/3,1/3,1/3,1/3,1/3)\\
d_1&(1/3,1/3,1,1/3,2/3,0)\\
d_2&(1/3,2/3,1,1/3,1/3,0)\\
d_3&(1,0,1,0,0,1)\\
d_4&(1,0,1,0,1,0)\\
d_5&(1,1/3,1/3,0,0,2/3)\\
d_6&(1,1/3,1/3,0,1/3,1/3)\\
d_7&(1,2/3,1/3,0,0,1/3)\\
d_8&(1,1,1,0,0,0).
\end{array}                                               \tag{3.2}
\]

The enumeration certificate is finite and independent of
`a,c,p,q`: every vertex has six recorded independent active rows, and
all `C(14,6)=3003` active-row choices are checked.  A linear objective
with nonnegative capacities has an optimum at one of these vertices by
finite LP duality.  Thus

\[
 \nu^*(G)=\min_{0\le i\le8} d_i\cdot
 (A_0,B,C_0,P,U,V).                                      \tag{3.3}
\]

The accompanying checker independently solves (2.1) by an exact
rational simplex on a bounded parameter box and obtains the same values.
The finite check is not the reason that (3.3) holds; the fixed
active-set exhaustion is the proof certificate.

## 4. Exact lambda rays

Substituting (3.2) into (1.3) gives nine affine forms:

\[
\begin{array}{rcl}
\ell_0&=&(A_0+B+C_0+P+U+V)/3,\\
\ell_1&=&(A_0+B-3C_0+P-U+3V)/3,\\
\ell_2&=&(A_0-B-3C_0+P+U+3V)/3,\\
\ell_3&=&-A_0+B-C_0+P+U-V,\\
\ell_4&=&-A_0+B-C_0+P-U+V,\\
\ell_5&=&(-3A_0+B+C_0+3P+3U-V)/3,\\
\ell_6&=&(-3A_0+B+C_0+3P+U+V)/3,\\
\ell_7&=&(-3A_0-B+C_0+3P+3U+V)/3,\\
\ell_8&=&-A_0-B-C_0+P+U+V.
\end{array}                                               \tag{4.1}
\]

Hence

\[
 \lambda(G)=\max_{0\le i\le8}\ell_i.                     \tag{4.2}
\]

Put `R_i=(3/2)(ell_i-ell_0)` for `i=1,...,8`.  Explicitly,

\[
\begin{array}{rcl}
R_1&=&V-U-2C_0,\\
R_2&=&V-B-2C_0,\\
R_3&=&P+U-2V-2A_0+B-2C_0,\\
R_4&=&P-2U+V-2A_0+B-2C_0,\\
R_5&=&P+U-V-2A_0,\\
R_6&=&P-2A_0,\\
R_7&=&P+U-2A_0-B,\\
R_8&=&P+U+V-2A_0-2B-2C_0.
\end{array}                                               \tag{4.3}
\]

Three vertices are redundant on the actual parameter cone.

First,

\[
 R_1-R_2=a(c-q).
\]
If `q>=c`, then `R_1<=R_2`; if `q<=c`, then
`R_1<=c(c-a)-c(c-1)=c(1-a)<=0`.

Second, if `R_2>0`, then `q>r-1`; consequently `R_7>0` and
`R_8=R_7+R_2>R_2`.  Otherwise `R_2<=0`.

Third,

\[
R_4-R_3=3q(c-a),\qquad R_4-R_8=3a(c-q).                 \tag{4.4}
\]
If `c<=a`, then `R_4<=R_3`.  Suppose `c>a`.  If `q>=c`,
then `R_4<=R_8`.  If `q<c`, use
\[
 R_4-R_6=c(a-c+1)+q(c-2a).                              \tag{4.5}
\]
When `c<=2a`, both terms on the right are nonpositive.  When `c>2a`,
the strict inequality `q<c` gives
\[
R_4-R_6<c(a-c+1)+c(c-2a)=c(1-a)<0.
\]

Therefore the exact formula collapses to **six effective rays**:

\[
 \boxed{\lambda(G)=
 \max\{\ell_0,\ell_3,\ell_5,\ell_6,\ell_7,\ell_8\}.}     \tag{4.6}
\]

## 5. Full-face criterion and exact excess

C35 defines the fractional face excess

\[
 \Delta_f(G)=\lambda(G)-|E(G)|/3.
\]

Since `ell_0=|E(G)|/3`, (4.6) gives

\[
 \boxed{\Delta_f(G)=\frac23
 \max\{0,R_3,R_5,R_6,R_7,R_8\}.}                        \tag{5.1}
\]

Thus the full one-third face is characterized, on (1.1), by only five
inequalities:

\[
 R_3\le0,\quad R_5\le0,\quad R_6\le0,\quad
 R_7\le0,\quad R_8\le0.                                 \tag{5.2}
\]

In the original parameters these are

\[
\begin{array}{rcl}
R_3&=&-a^2+ac+ap+aq+a-c^2-2cq+c,\\
R_5&=&-a^2+ap+aq+a-cq,\\
R_6&=&a(p-a+1),\\
R_7&=&a(p+q-r+1),\\
R_8&=&ap+rq-r(r-1).
\end{array}                                               \tag{5.3}
\]

The bounded exact checker verifies that (5.2) agrees with the C28
interval criterion on every tested nondegenerate parameter tuple.
Equation (5.2), however, follows directly from the fixed dual
classification and is not inferred from those tests.

## 6. Complementary object types

The tight columns at the four unresolved nonuniform vertices are:

\[
\begin{array}{c|l}
d_3& AAC,\ ACC,\ \alpha,\ \beta_{AA},\ \beta_{AC},\\
d_5& ACC,\ CCC,\ \alpha,\ \beta_{AA},\ \beta_{AC},\\
d_6& ACC,\ CCC,\ \alpha,\ \beta_{AC},\ \beta_{CC},\\
d_7& CCC,\ \alpha,\ \beta_{AA},\ \beta_{AC},\ \beta_{CC}.
\end{array}                                               \tag{6.1}
\]

These are permissible supports of an optimal fractional solution, not
immutable type totals and not actual leaf matchings.  Any integer
construction must still allocate every core edge once and split each
aggregate leaf graph among actual leaves.

The full ray `d_0` is root-safe by C35.  The all-leaf ray `d_8` is
root-safe by Section 8.  Therefore every remaining nondegenerate
two-neighborhood root obstruction must lie in one of the four mixed
cones in (6.1).

## 7. Small-side boundary is root-safe

If `a<=2`, decompose the edge set into the complete-split graph
`J(r,q)` and the `ap` short spokes as singleton cliques:

\[
 cp(G)\le cp(J(r,q))+ap.                                \tag{7.1}
\]

C35 gives the required quadratic-plus-linear bound for every
complete-split graph, while `ap<=2p<=2n`.

If `c<=2`, use the exact disjoint decomposition

\[
 E(G)=E(J(a,p+q))\ \dot\cup\ E(J(c,a+q)).                \tag{7.2}
\]

The first complete-split component has order at most `n`.  The second
has at most

\[
 \binom c2+c(a+q)\le2n+1
\]
edges, so singleton cliques contribute only a linear allowance.
Consequently the ProblemContract form holds on all small-side boundary
families, assuming the complete-split candidate already frozen in C35.
No fixed eight-column formula is asserted there.

## 8. The all-leaf ray is root-safe

Assume (1.1) and that `ell_8=lambda`.  Since

\[
 \ell_8-\ell_7=\frac23 R_2
              =\frac23\,c(q-r+1),
\]
we necessarily have

\[
 q\ge r-1.                                               \tag{8.1}
\]

Cover every short spoke by a singleton edge.  It remains to partition
the complete-split graph `J(r,q)`.

- If `r` is even, factor `K_r` into `r-1` perfect matchings and assign
  them to distinct long leaves.  Every factor edge lifts to a triangle.
  Remaining long leaves contribute singleton spokes.
- If `r` is odd and `q>=r`, use the `r` near-perfect matchings obtained
  from a one-factorization of `K_{r+1}`.  For each assigned long leaf,
  its unique unmatched spoke is a singleton.
- If `r` is odd and `q=r-1`, omit one near-perfect class.  Its
  `(r-1)/2` core edges and the `r-1` unmatched spokes are singleton
  cliques.

Every core edge and long spoke is used exactly once.  The number of
pieces is

\[
 rq-\binom r2
\]
except in the last odd boundary case, where it is larger by `r-1`.
Adding the `P=ap` short singleton edges gives

\[
 \boxed{cp(G)\le\ell_8+r-1=\lambda(G)+r-1.}              \tag{8.2}
\]

C22 gives `lambda<=floor(n(n+1)/6)` for every chordal graph, so (8.2)
has the required root form.  This is an actual clique partition, not a
statement about `Q`.

## 9. Finite audit and route change

The exact checker performs:

1. all `C(14,6)=3003` dual active-set choices and certifies the nine
   vertices (3.2);
2. an independent exact rational primal simplex on 10,816 parameter
   tuples;
3. the ray and redundancy identities on 129,600 tuples;
4. equality with the C28 face criterion on the same nondegenerate box;
5. actual round-robin partitions for all `r<=60` and
   `r-1<=q<=r+14`;
6. 86,240 small-side edge-count/decomposition rows;
7. twelve negative mutations.

The four final modes exit zero under the recorded bounds.  An earlier
oversized version of the classifier exceeded its 45-second parent
limit; no child exit was recovered, and that attempt is not counted as
success.

The next root-directed task is now finite in kind:

> for each of `d_3,d_5,d_6,d_7`, build an actual clique partition with
> at most `ell_i+O(n)` pieces throughout the cone where `ell_i` is
> maximal, or exhibit a source-valid family preventing that route.

The supports (6.1) suggest mixed complete-graph-with-holes designs, but
no such all-cone construction is claimed here.  General split
domination, arbitrary chordal graphs, and trusted closure remain open.
