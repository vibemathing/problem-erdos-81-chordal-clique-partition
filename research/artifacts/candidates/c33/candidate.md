# Candidate C33 — balanced partial-fiber completion

**Status:** `candidate_only`; `best_verified_result=none`; `root_closed=false`.  
**Fresh base:** `5f7049f2678bc0ea096fe6fef2a206c5e5c1f114`.

## Theorem-sized handoff

Let `r=3^k`, let `m=3^s` divide `r`, put `R=r/m`, and write

\[
 |A|=hm+b,\qquad 2\le h\le R-1,\qquad 0<b<m.
\]

If

\[
 \lfloor p/2\rfloor+\lfloor q/2\rfloor\le(m-1)/2,
\]

then every actual short set `A` admits an **actual edge-disjoint host
triangle packing** with

\[
 S=M+|A|p+rq-3|\mathcal P|
 \le(h-2)\sigma_m(p)+\kappa_{m,b}(p)+R\sigma_m(q)
 <13r/3.
\]

Hence `nu_star-nu < 13r/9`.  Every individual leaf resource is a
matching; every core edge has one owner; every retained core triangle
has one of the types AAA/AAC/ACC/CCC.

The new boundary gadget is explicit.  For `D=floor(p/2)`, define the
periodic mechanical word

\[
 \epsilon_x=\lfloor(x+1)b/m\rfloor-\lfloor xb/m\rfloor,
\quad C=\{x:\epsilon_x=1\},\quad B=2C.
\]

In the cyclic transversal design `u+v=w`, select

\[
 (s+t,s-t,2s),\qquad s\in C,\quad 0\le t<D.
\]

Every point of `B` has incidence `D`; every row and column has incidence
`floor(bD/m)` or `ceil(bD/m)`.  The selected triples have simple pair
projections, and the unselected cyclic triples complete all unused
cross pairs exactly.  Thus the partial-Latin completion blocker from
C32 is closed without an external embedding theorem.

For odd `p`, the boundary defect is at most `7m`.  For positive even
`p`, one Vizing repair gives boundary defect `<17m/2`.  Complete fibers
use the C32 packet, and disjoint internal directions carry the long
packet.

If `m` is the least power of three at least `p+q+1`, then

\[
 6(p+q+1)\le|A|\le r-1
\]

implies the same `<13r/3` defect for arbitrary actual `A`; the
multiplicities may therefore grow linearly with `r` on this explicit
domain.  Divisible cardinalities and `A=V` use C32.

## Remaining boundary

The only short-cardinality configuration not addressed by this
completion scheme has fewer than two complete fibers at every
power-of-three scale large enough for the combined direction demand.
The next route requires a one-buffer/no-buffer trade.  Repeating
per-layer boundary deletion, selecting near-factor colors first, or
reusing a translation slot remains excluded.
