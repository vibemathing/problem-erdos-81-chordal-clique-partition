# Candidate C32 — affine direction packets

**Status:** `candidate_only`; `best_verified_result=none`; `root_closed=false`.  
**Fresh base:** `de0a67b00e14e200ab32da0a3b30d387be13dfb6`.

Let \(G(r,A;p,q)\) be the two-neighborhood split host with core
\(K_r\), \(p\) short leaves on \(A\), and \(q\) long leaves on the whole
core. Put \(U=(\binom r2+|A|p+rq)/3\).

## Theorem-sized lemma

Let \(r=3^k\), let \(m=3^s\le r\), and write
\(|A|=hm+b\), \(0\le b<m\). Suppose
\[
 \lfloor p/2\rfloor\le(m-1)/2,\qquad
 \lfloor p/2\rfloor+\lfloor q/2\rfloor\le(r-1)/2.
\]
Then there is an **actual edge-disjoint host triangle packing** with
\[
 S:=3(U-|\mathcal P|)
 \le h\,\sigma_m(p)+pb+\sigma_r(q),
\]
where
\[
 \sigma_n(0)=0,\quad
 \sigma_n(t)=n\ (t\text{ odd}),\quad
 \sigma_n(t)\le\frac{3tn}{2(t+1)}\ (t>0\text{ even}).
\]

Construction: take unions of affine direction factors. For odd
multiplicity, Vizing colors the \((t-1)\)-regular union with \(t\)
actual leaf colors. For even multiplicity, color the \(t\)-regular
union with \(t+1\) colors, delete one smallest color class once, and
use the remaining \(t\) actual leaves. Each deleted edge contributes
exactly one core and two endpoint units. Distinct short and long
directions give a unique owner for every AAA/AAC/ACC/CCC core edge.

When \(b=0\), \(S<3r\), independently of \(p,q\). Adding one whole
\(m\)-coset increases \(S\) by the fixed amount \(\sigma_m(p)\), giving
a genuine period-\(m\) continuation. For arbitrary \(|A|\), if
\(p(p+1)\le r\) and \(p+q\le r-1\), the least admissible \(m\) gives
\(S<6r\).

## First nontrivial multiplicities

For every actual \(A\), \(a=|A|=3t+b\), and
\((p,q)=(3,2)\) or \((3,3)\), an explicit two-direction construction
has
\[
 S=a+r+2b.
\]
For \(4\le a\le r\), an explicit saturated primal proves
\[
 \nu^*=U=\frac{\binom r2+3a+qr}{3},
\]
hence
\[
 \nu^*-\nu\le\frac{a+r+2(a\bmod3)}3\le\frac{2r+4}{3}.
\]

## Strict route obstructions

* If \(t\) is even and a \(t\)-regular resource graph has \(c\)
  odd-order components, any deletion making it \(t\)-edge-colorable
  has size at least \(tc/2\).
* Selecting \(p\) near-factor colors first on an affine block of order
  \(m\) has core defect at least \(p(m-p)/2\); the middle regime is
  quadratic.
* A fiber of size \(N\) has only \(N\) translation slots per shared
  base edge. More than \(N\) full-slot requests are impossible.

The complete proof, finite certificates, exact checker, provenance,
and limitations are in this candidate package.
