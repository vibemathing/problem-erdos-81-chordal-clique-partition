# C39: close C36 cone d5 by an equitable C-side owner construction

Candidate: `candidate:erdos81-a01-c39-d5-equitable`
Status: `candidate_only`; `best_verified_result=none`; `root_closed=false`.

## 1. Scope and exact fractional target

Use the C36 host `G(r,A;p,q)` with `a=|A|>=3`, `c=r-a>=3`. Assume the effective ray `ell5` is maximal; ties are allowed. Write
`A0=C(a,2), B=ac, C0=C(c,2), P=ap, U=aq, V=cq`.

C36 gives

    ell5=(-3A0+B+C0+3P+3U-V)/3.

If q=0 then ell5=ell6, so C38 applies. Hence suppose q>0.
Comparing ell5 with the other effective rays gives

    a>=c, q<=a, c+q>=a+1, R5=P+U-V-2A0>=0.      (1.1)

Put

    d0=max(0,a-1-p), h=a-q.

The last inequality says

    q(a-c)>=a d0, equivalently c q/a <= q-d0.    (1.2)

The first three give `0<=h<=c-1`.
Substituting lambda=ell5 in `nu_star=(|E|-lambda)/2` yields

    nu_star = A0 + (B+C0+2V)/3.                    (1.3)

Thus no betaCC resource is needed: the d5-tight columns are ACC, CCC,
alpha, betaAA and betaAC.

## 2. Good C subset and a regular complement

Choose `C' subset C` with

    c'=|C'| = largest integer <=c congruent to 3 mod 6.

Then `e=c-c'<=5`. Put

    h'=largest even integer <=min(h,c'-1),
    delta=h-h'.

Because `h<=c-1` and `c-c'<=5`,

    0<=delta<=5.                                      (2.1)

Set `t'=c'-1-h'`, which is even. A resolvable STS on C' has
`(c'-1)/2` triangle factors. Select `t'/2` of them as CCC core
triangles. Their edge set gives degree t' at every C' vertex. Let F be
the complement in K_C'. Then

    F is h'-regular, |E(F)|=c'h'/2.                    (2.2)

The STS/Kirkman existence input is source-backed exactly as in C28; it
is not re-certified here.

## 3. Equitable A-coloring of F and ACC ownership

Since c' is odd, the standard near-one-factorization of K_C' uses c'
matching colors. Restrict it to F and add empty colors so that exactly a
colors are available (`a>=c>=c'`). This is a proper a-edge-coloring of F.

We rebalance the color-class sizes without losing properness. If two
colors i,j differ in size by at least two, their union is a disjoint
union of alternating paths and even cycles. The size difference implies
there is an alternating path component containing one more i-edge than
j-edge. Swap i and j on that component. This keeps a proper coloring and
strictly decreases the sum of squares of color-class sizes. The finite
integer potential terminates. At termination all class sizes differ by
at most one.

Let m_x be the number of F edges of color x in A. For every colored
edge uv of F, take the core triangle xuv. Properness says edges of one
color form a matching, so no AC core edge is repeated. Every F edge is
used once. These are ACC triangles.

The unused AC graph betaAC on A,C' has degrees

    deg_betaAC(z)=a-h'=q+delta                         (z in C'),
    deg_betaAC(x)=c'-2m_x                              (x in A).       (3.1)

Equitability and |F|=c'h'/2 give

    m_x >= floor(c'h'/(2a)) >= c'h'/(2a)-1,

hence

    deg_betaAC(x) <= c'(q+delta)/a+2
                   <= c q/a + delta+2
                   <= q-d0+7.                         (3.2)

The second inequality uses c'<=c<=a; the last uses (1.2) and delta<=5.

## 4. AA ownership and one aggregate long-resource repair

Factor K_A by the standard round-robin construction: a-1 perfect
matching classes if a is even, and a near-perfect classes if a is odd.
Let

    d=max(0,d0-7).

Assign d initial factor classes to betaAA. Assign as many subsequent
factor classes as possible, up to p, directly to distinct actual short
leaves (alpha). No AA edge is used twice.

The number of factor classes left unused is at most 7 when a is even and
at most 8 when a is odd. Therefore the number of unused AA edges is
strictly less than 4a<=4r.                              (4.1)

Let H_beta=betaAA union betaAC. Its maximum degree is at most q+7:
- if d0>=7, then at A, d+deg_betaAC <=(d0-7)+(q-d0+7)=q;
- if d0<7, then d=0 and deg_betaAC<=q+7;
- at C', (3.1) gives degree q+delta<=q+5.

By the finite Delta+1 fan edge-coloring theorem proved in C24,
H_beta has a proper edge coloring with at most q+8 colors. Keep the q
largest color classes and delete the rest. At most eight color classes
are deleted, each a matching of size at most r/2, so at most 4r beta
edges are lost. The retained q colors are assigned to the q actual long
leaves. Hence every long leaf receives a genuine matching; each retained
beta edge lifts to one actual long-leaf triangle.

This is one aggregate repair, not a q-fold or per-layer repair.

## 5. Exact good-C ledger and total loss

Before the beta-color deletion, the C'-side objects number

    c'h'/2 + c't'/6 + c'(q+delta),                       (5.1)

coming from ACC, CCC and betaAC. Since t'=c'-1-h' and
delta=a-q-h', subtracting the C'-restricted fractional target

    [a c' + C(c',2)+2q c']/3

from (5.1) gives exactly

    2 delta c'/3 >=0.                                   (5.2)

Thus the good-C construction has no deficit before actualizing beta;
the surplus in (5.2) merely reflects that the aggregate beta degrees may
exceed q before the final coloring deletion.

The fractional target lost by omitting the e<=5 exceptional C vertices is

    [a e + (C(c,2)-C(c',2)) + 2q e]/3 <=5r,             (5.3)

because q<=a and a+c=r. Add the unused-AA loss <4r from (4.1) and the
single beta-coloring loss <=4r. Hence

    nu_star-nu <13r.                                    (5.4)

C22 then gives

    cp <= lambda+2(nu_star-nu)
       <= n^2/6+n/6+26r
       < n^2/6+27n.                                     (5.5)

## 6. Complete owner audit

- Selected CCC factors and F partition E(K_C').
- Every F edge belongs to one ACC triangle; proper A-coloring ensures its
two AC edges are unique.
- betaAC is exactly the unused A-C' edge set.
- betaAA, alpha and unused classes partition the chosen AA factor classes;
no residual object uses an AA edge.
- H_beta is edge-colored once; retained colors are actual long-leaf
matchings. Deleted colors are simply unused.
- Edges incident to C\C' are never assigned by the construction and are
charged only through (5.3).
- Zero q is delegated to C38; equal prefix and small-side cases remain
outside the C36 nondegenerate quotient.
- No statement identifies Q, J, L_D, J_fix, nu or lambda.

## 7. Falsifier and source boundary

The generator-side checker audits 1,745,949 d5-dominant q>0 parameter
rows with 3<=a,c<=60, p<80, q<=60. It verifies delta<=5, the degree bound,
the seven/eight unused-AA-factor bounds, five explicit edge-owner
witnesses, and twelve semantic/mathematical mutations. The universal
argument is Sections 1--6, not finite extrapolation.

The only design existence input is the C28 source-backed resolvable STS
for order c' congruent 3 mod 6. The edge-coloring theorem is the finite
fan proof already frozen in C24. Neither dependency is a trusted receipt.

After C39, among C36's six effective rays, d0/full-face is C35, d8 is
C36, d7 is C37, d6 is C38, and d5 is this candidate. The remaining
nondegenerate cone is d3. General nested neighborhoods, split domination
and the ProblemContract root remain open.
