# C32: multiplicity-independent affine direction packets

Candidate: `candidate:erdos81-a01-c32-direction-packets`  
Repository: `vibemathing/problem-erdos-81-chordal-clique-partition`  
Problem: `problem:erdos-81-chordal-clique-partition`  
Attempt: `attempt:web-20260906-erdos81-a01`  
Route: `route:split-extremal-reduction-v1`  
Graph: `graph:erdos81-initial-v1`  
Transport obligation: `obligation:erdos81-split-extremal-reduction`  
Fresh base: `de0a67b00e14e200ab32da0a3b30d387be13dfb6`  
Verdict: `candidate_only`. `best_verified_result=none`.

## 1. Frozen definitions and claim boundary

Let \(G(r,A;p,q)\) have a complete core \(V\) of order \(r\), an actual
short set \(A\subseteq V\) of size \(a\), \(p\) independent short leaves
adjacent exactly to \(A\), and \(q\) independent long leaves adjacent to
all of \(V\). There are no leaf--leaf edges.

An **actual host packing** is a set of edge-disjoint triangles of this
graph. For each individual leaf, its core resource edges must therefore
form a matching. This candidate never replaces that condition by an
aggregate degree condition.

Write
\[
 M=\binom r2,\qquad
 U=\frac{M+ap+rq}{3}.
\]
The all-\(1/3\) row prices always give the fractional upper bound
\(\nu^*(G)\le U\). For an actual packing \(\mathcal P\), define its exact
capacity defect
\[
 S(\mathcal P)=M+ap+rq-3|\mathcal P|.
\]
Thus
\[
 U-|\mathcal P|=\frac{S(\mathcal P)}3,\qquad
 \nu^*(G)-\nu(G)\le \frac{S(\mathcal P)}3.              \tag{1}
\]
If a separate saturated primal proves \(\nu^*(G)=U\), then (1) measures
the packing's exact loss from that fractional face. No claim that the
displayed packing is maximum is made unless separately proved.

The main new result is an actual-packing theorem for arbitrarily large
leaf multiplicities on periodic short-set cardinalities, with a defect
constant independent of the multiplicities. It also gives arbitrary
short cardinalities with one explicit residual term. The first
nontrivial cases \(p=3,q=2\) and \(p=q=3\) are completely handled on
their full one-third face. The unrestricted one-third face, exact split
domination, and the ProblemContract root remain open.

## 2. Affine edge ownership

Let \(r=3^k\), \(k\ge2\), and label \(V\) by \(\mathbb F_3^k\).
For distinct \(x,y\), put
\[
 T(x,y)=\{x,y,-x-y\}.
\]
The third point is distinct from \(x,y\), and the unordered pair
\(\{x,y\}\) determines \(T(x,y)\) uniquely. Hence the affine lines
partition \(E(K_r)\).

A direction is a one-dimensional subspace. For a fixed direction, its
affine lines partition \(V\) into \(r/3\) triples; their edge sets form
a spanning 2-regular graph which is a disjoint union of triangles.
Distinct directions have disjoint edge sets. There are
\((r-1)/2\) directions.

If \(W\le V\) has order \(m=3^s\), every line with direction in \(W\)
lies wholly in one \(W\)-coset. This elementary fact is the boundary
invariant: a short packet supported on complete \(W\)-cosets never cuts
one of its own resource lines.

## 3. One multiplicity packet

Let \(X\) be an affine space of odd order \(n=3^s\). For a nonnegative
leaf multiplicity \(h\), define a resource graph as follows.

* \(h=0\): take the empty graph.
* \(h\) odd: take the union of \((h-1)/2\) direction classes. It is
  \((h-1)\)-regular.
* \(h>0\) even: take the union of \(h/2\) direction classes. It is
  \(h\)-regular.

The required number of directions exists when
\[
 \lfloor h/2\rfloor\le (n-1)/2.                         \tag{2}
\]

### 3.1 Odd multiplicity

The graph has maximum degree \(h-1\). Vizing's theorem gives a proper
edge coloring with at most \(h\) colors. Assign the colors to the
\(h\) actual leaves. Every color class is an actual matching.

All selected affine triangles are completely occupied by resource
edges, so there is no core defect. Every vertex has aggregate leaf
degree \(h-1\), hence exactly one unused endpoint row. The exact local
defect is
\[
 \sigma_n(h)=n\qquad(h\text{ odd}).                     \tag{3}
\]

This includes \(h=1\): the resource graph is empty and all \(n\)
endpoint rows are the defect.

### 3.2 Even multiplicity

Vizing gives a proper \((h+1)\)-edge coloring. Delete a smallest color
class \(R\), and assign the remaining \(h\) colors to the actual leaves.
Since each color class is a matching,
\[
 |R|\le \frac{|E(H)|}{h+1}
      =\frac{hn}{2(h+1)}.                               \tag{4}
\]

A selected affine line is a triangle. A proper color occurs on at most
one of its edges. Therefore deletion of \(R\) leaves exactly one unused
core edge for each deleted resource edge; the other two edges of that
line remain resource edges. The two endpoints of each deleted edge
each miss one leaf incidence. Consequently
\[
 S_{\rm core}=|R|,\qquad S_{\rm endpoint}=2|R|,\qquad
 \sigma_n(h)=3|R|
 \le\frac{3hn}{2(h+1)}<\frac32n.                        \tag{5}
\]

Misra--Gries gives a finite constructive \(\Delta+1\) coloring
algorithm, so (3)--(5) describe an explicit terminating procedure once
the directions are listed. This theorem is used only for finite simple
graphs.

## 4. Two-class direction-packet theorem

### Theorem 4.1

Let \(r=3^k\), let \(m=3^s\le r\), and write
\[
 a=hm+b,\qquad 0\le b<m.
\]
Assume
\[
 \left\lfloor\frac p2\right\rfloor\le\frac{m-1}{2},
 \qquad
 \left\lfloor\frac p2\right\rfloor+
 \left\lfloor\frac q2\right\rfloor\le\frac{r-1}{2}.     \tag{6}
\]
Then every actual short set \(A\) of cardinality \(a\) admits an actual
host packing with
\[
 S\le h\,\sigma_m(p)+pb+\sigma_r(q),                    \tag{7}
\]
where \(\sigma\) is given by (3)--(5), and \(\sigma_n(0)=0\).

In particular, when \(b=0\),
\[
 S<\frac32a+\frac32r\le3r,\qquad
 \nu^*-\nu<r.                                           \tag{8}
\]
If the two positive multiplicities are odd, then
\[
 S=a+r\le2r,\qquad \nu^*-\nu\le\frac{2r}{3}.            \tag{9}
\]

### Proof

Choose a coordinate subspace \(W\) of order \(m\). In an abstract
labeling, let \(A'\) consist of \(h\) whole \(W\)-cosets and \(b\)
vertices of one further coset. Transport the final construction by any
bijection sending \(A'\) to the given actual \(A\).

Choose the short directions inside \(W\), and choose the long
directions disjoint from them. Condition (6) guarantees availability.
On each whole short coset use the packet of Section 3, with one fixed
local coloring and, in the even case, one fixed deleted color. Reusing
the palette on disjoint cosets preserves the matching property. Use no
short resource edge in the partial coset; its \(b\) vertices contribute
exactly \(pb\) unused short endpoint rows.

Use the long packet on the whole core. Retain as core triangles every
affine line not assigned to a resource packet. For a short direction,
lines in a complete selected \(W\)-coset are resources; every other
line of that direction, including every line of the partial coset, is
retained as a core triangle. Long directions are disjoint from short
directions.

Thus every actual core edge has exactly one status:

1. one retained core triangle;
2. one short-leaf color;
3. one long-leaf color; or
4. one deleted-color unused slot.

No edge receives two owners. Each retained core triangle has exactly
one type AAA, AAC, ACC, or CCC according to its intersection with the
actual \(A\). Each leaf color is a genuine matching. Equations
(3)--(5) add over the edge-disjoint packets and give (7). This also
proves termination: enumerate finite directions and lines, run the
finite coloring algorithm, and transport a finite list. ∎

### 4.2 Periodic continuation

Adding one whole \(W\)-coset to the short set changes no old owner and
increases the defect by exactly one fixed local packet cost
\(\sigma_m(p)\). Therefore (7) is a genuine period-\(m\) continuation,
not a finite extrapolation:
\[
 S(a+m)-S(a)=\sigma_m(p).                               \tag{10}
\]
For even \(p\), the same local coloring and deleted color are repeated
on the new coset.

### 4.3 Arbitrary-cardinality growing range

Take the least power \(m=3^s\) satisfying \(m\ge p\) for odd \(p\), or
\(m\ge p+1\) for positive even \(p\). Then \(m<3(p+1)\). If
\[
 p(p+1)\le r,\qquad p+q\le r-1,                         \tag{11}
\]
then \(m\le r\), (6) holds, and \(pb<3p(p+1)\le3r\).
Consequently Theorem 4.1 gives, for **every** actual short cardinality,
\[
 S<6r,\qquad \nu^*-\nu<2r.                              \tag{12}
\]
This covers growing \(p\) through the square-root scale and arbitrary
allowed \(q\); the constant in (12) does not depend on either
multiplicity.

For the equal-prefix case \(A=V\), take \(m=r,b=0\). Under
\(p+q\le r-1\), (8) applies for all multiplicities, including those far
above the square-root scale.

The residual term \(pb\) is the remaining obstruction for arbitrary
high \(p\) and arbitrary nonperiodic \(a\). It is stated rather than
hidden.

## 5. The first nontrivial multiplicities on arbitrary short sets

### Theorem 5.1

Let \(r=3^k\), \(k\ge2\), and let \(A\) be any actual set of size
\(a\). Write \(a=3t+b\), \(b\in\{0,1,2\}\). For either
\[
 (p,q)=(3,2)\quad\text{or}\quad(p,q)=(3,3),
\]
there is an actual host packing with
\[
 S=a+r+2b\le2r+4.                                       \tag{13}
\]

### Explicit construction

Choose distinct affine directions \(D_S,D_L\). In the \(D_S\) parallel
class, declare \(t\) whole triples short and add \(b\) vertices of one
unselected triple; then transport this abstract short set to the
actual \(A\).

On every selected short triple, color its three edges with the three
short leaves. These three color classes are matchings because the
triples are vertex-disjoint. The selected \(3t\) vertices each have
short degree two and the \(b\) remainder vertices have short degree
zero, so
\[
 S_{\rm short}=3t+3b=a+2b.                              \tag{14}
\]

For \(q=3\), color all three edges of every \(D_L\)-triple with the
three long leaves. The core defect is zero and every core vertex has
long degree two, so the long endpoint defect is \(r\).

For \(q=2\), use a two-edge path in every \(D_L\)-triple and give its
two edges to the two long leaves. The unused third edge contributes
\(r/3\) core defect, and the two path endpoints contribute \(2r/3\)
long endpoint defect. Again the total long-side defect is \(r\).

Keep every other affine line as a core triangle. The two direction
classes are edge-disjoint, so all owners and all four triangle types
are compatible. Equations (13)--(14) follow.

The packing cardinality is
\[
 |\mathcal P|=
 \begin{cases}
 M/3+2t+r/3,&q=2,\\
 M/3+2t+2r/3,&q=3.
 \end{cases}                                            \tag{15}
\]

### 5.2 Full one-third face for \(a\ge4\)

For both \(q=2,3\), every parameter with \(4\le a\le r\) lies on the
full one-third face:
\[
 L=\nu^*=\frac{M+3a+qr}{3}.                             \tag{16}
\]

For \(c=r-a\ge3\), set \(d=r-1-q\), \(s=d-3\). Eliminating the symmetric
six-resource primal gives the exact interval
\[
 \max\!\left(0,\frac{a(c-q)}2,\frac{c(a-q)}2\right)
 \le
 \min\!\left(\frac{ac}2,\frac{as}2,\frac{cd}2,
             \frac{as+cd}{6}\right).                   \tag{17}
\]
If \(c\ge a\), choose \(w=a(c-q)/2\). The only final inequality, after
putting \(c=a+x\), is
\[
 a^2+a(q-5)+x(a-q-1)+x^2\ge0.
\]
It holds for \(a\ge4\), \(q=2,3\), \(x\ge0\). If \(a\ge c\), choose
\(w=c(a-q)/2\). The nontrivial differences reduce to
\[
 c^2-4c+x(2c-q-4)+x^2,
\]
\[
 c^2+c(q-5)+x(c-q-4)+x^2.
\]
For \(c\ge7\) they are immediate; the cases \(3\le c\le6\), under
\(2c+x=r\ge9\), are direct substitutions. Thus (17) is nonempty.

The complements \(c=0,1,2\) have explicit saturated primal points.
All variables below are per edge or per triangle.

* \(c=0\):
  \[
  \alpha=\frac3{r-1},\quad\beta=\frac q{r-1},\quad
  z_{AAA}=\frac{r-4-q}{(r-1)(r-2)}.
  \]
* \(c=1\), so \(r=a+1\):
  \[
  \alpha_{AA}=\frac3{a-1},\quad
  \beta_{AA}=\beta_{AC}=\frac q a,
  \]
  \[
  z_{AAC}=\frac{a-q}{a(a-1)},\quad
  z_{AAA}=\frac{a^2-a(q+5)+2q}{a(a-1)(a-2)}.
  \]
* \(c=2\):
  \[
  \alpha_{AA}=\frac3{a-1},\quad
  \beta_{AA}=\frac{q(a-2)}{a(a-1)},\quad
  \beta_{AC}=\frac qa,\quad\beta_{CC}=0,
  \]
  \[
  z_{ACC}=\frac1a,\quad
  z_{AAC}=\frac{a-q-1}{a(a-1)},
  \]
  \[
  z_{AAA}=
  \frac{a^2-a(q+6)+4q+2}{a(a-1)(a-2)}.
  \]
Every actual edge and tagged endpoint row saturates. Nonnegativity
holds at the stated boundary orders; for \(c=2,q=3\), the last numerator
is \((a-2)(a-7)\).

Combining (13) and (16) gives the actual-host result
\[
 0\le L-\nu\le\frac{a+r+2(a\bmod3)}3
             \le\frac{2r+4}{3}.                        \tag{18}
\]
The cases \(a=2,3\) are not inserted into this face: the necessary
short capacity \(p\le a-1\) already fails.

## 6. Translation slots for shared base edges

The primary construction uses disjoint directions, but the following
fallback permits different base objects to share a base edge.

Give every base vertex a fiber \(\mathbb Z_N\). For an oriented base
edge \(uv\), define
\[
 P_s(uv)=\{(u,i)(v,i+s):i\in\mathbb Z_N\},
 \qquad s\in\mathbb Z_N.
\]
The \(N\) sets \(P_s(uv)\) are pairwise edge-disjoint perfect matchings
and partition \(K_{N,N}\).

For a base triangle \(uvw\), slots \(s\) on \(uv\), \(t\) on \(vw\),
and \(s+t\) on \(uw\) lift to
\[
 \{((u,i),(v,i+s),(w,i+s+t)):i\in\mathbb Z_N\}.         \tag{19}
\]
Every edge in each of the three prescribed slots occurs exactly once.
Thus shared base edges are harmless **only** when their occurrences
receive distinct actual slots. If a base edge demands more than \(N\)
full slots, the fiber size \(N\) is insufficient: \(K_{N,N}\) has only
\(N\) edge-disjoint perfect-matching slots. This is the exact slot
congestion obstruction.

If one leaf color is a matching at base level, its lifted resource
edges remain a matching because no base vertex occurs twice in that
color.

## 7. Adversarial obstructions and route changes

### 7.1 Even regular packets must be repaired

Let \(h\) be even and let an \(h\)-regular resource graph have \(c\)
connected components, each of odd order. If deleting \(R\) makes it
\(h\)-edge-colorable, then
\[
 |R|\ge \frac{hc}{2}.                                   \tag{20}
\]
Indeed, in each odd component every matching color misses an odd,
hence at least one, number of vertices. Across the \(h\) colors the
number of missing color--vertex incidences is at least \(hc\), while it
equals
\[
 \sum_v(h-d_{H-R}(v))=2|R|.
\]
So the even-packet deletion in Section 3 is not a proof artifact.
For one direction, \(h=2\) and \(c=n/3\), (20) gives the exact
\(n/3\) deletion used in C31.

On the nine-point plane, frozen exact color certificates attain (20)
for \(h=2,4,6,8\), with
\[
 \rho_h=3,2,3,4.
\]
The checker verifies both the colorings and the lower certificate; the
discovery optimizer is not a proof input.

### 7.2 Selected near-factor colors have a quadratic middle regime

Consider a different route on an affine space of order \(m\): select
\(p\) color classes of the canonical near-one-factorization of \(K_m\)
as the actual leaf matchings, and let \(D\) be the \(e=m-p\) omitted
colors. An affine line with \(j\) omitted colors has \(3-j\) resource
edges. Keeping untouched affine lines as core triangles gives
\[
 S_{\rm endpoint}=p,
\]
\[
 S_{\rm core}=\frac{e(m-1)}2-3\tau(D),                  \tag{21}
\]
where \(\tau(D)\) is the number of affine lines contained in \(D\).
Since \(3\tau(D)\le\binom e2\),
\[
 S_{\rm core}\ge\frac{ep}{2}.                           \tag{22}
\]
Hence this selected-color route has quadratic defect whenever both
\(p\) and \(m-p\) are linear in \(m\). It is not a route to a
multiplicity-independent linear theorem. This is a strict route
obstruction, not a counterexample to the target host inequality.

The direction-packet construction changes route precisely here:
it selects entire triangle factors and only then edge-colors their
union, rather than selecting near-factor colors first.

## 8. Dependency DAG

```text
D0 frozen host definitions and capacity identity
 ├─ D1 affine lines partition every core edge
 │   ├─ D2 direction classes are disjoint triangle factors
 │   │   ├─ D3 Vizing/Misra–Gries Δ+1 coloring
 │   │   │   ├─ D4 odd/even local packet defect
 │   │   │   └─ D5 exact even-component lower obstruction
 │   │   └─ D6 W-coset boundary invariance
 │   │       └─ D7 two-class owner theorem and period continuation
 │   │           ├─ D8 arbitrary-cardinality square-root corollary
 │   │           └─ D9 p=3,q=2/3 explicit actual packing
 │   └─ D10 four core-triangle types have unique owners
 ├─ D11 six-resource face criterion and c=0,1,2 primal points
 │   └─ D12 full-face p=3,q=2/3 loss bound
 ├─ D13 translation-slot bijection
 │   └─ D14 exact base-edge congestion obstruction
 └─ D15 near-factor color accounting
     └─ D16 quadratic middle-regime failed-route signature
```

Every terminal claim traces to an explicit construction, a displayed
counting identity, or the named edge-coloring theorem. There is no
finite-to-universal extrapolation.

## 9. Pressure tests and evidence ceiling

The exact checker performs the following generator-side tests.

1. All \(240\) cardinality constructions for \(r=9,27,81\),
   \(q=2,3\), and every \(0\le a\le r\).
2. Every one of the \(764\) transported actual nine-core subsets with
   \(4\le a\le9\), for both \(q\).
3. All \(696\) recorded full-face parameter substitutions through
   \(r=243\), including \(c=0,1,2\).
4. Nine complete nine-point Vizing color certificates.
5. Exact even repair certificates \(\rho_2=3,\rho_4=2,\rho_6=3,\rho_8=4\).
6. All \(512\) omitted-color sets in the nine-point near-factor
   obstruction identity.
7. Translation-slot bijections for fiber sizes \(3,5,7\).
8. Negative tests for shared directions, reused slots, a nonmatching
   leaf color, and the excluded \(a=3\) face.

These checks validate the supplied finite objects and implementations.
They do not independently verify Vizing's theorem, the universal
quantifiers, the ProblemContract, or root closure. The candidate is
generator-authored and has no verifier receipt, EvidenceLink, Result,
or Solution admission.

Status: `NONTERMINAL_CHECKPOINT`; `candidate_only`;
`best_verified_result=none`; `root_closed=false`.
