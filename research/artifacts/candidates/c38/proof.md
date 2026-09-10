# C38: close the C36 d6 cone by two-hole residual decomposition

Candidate: `candidate:erdos81-a01-c38-d6-two-hole`
Repository: `vibemathing/problem-erdos-81-chordal-clique-partition`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Transport obligation: `obligation:erdos81-split-extremal-reduction`
Verdict: `candidate_only`; `best_verified_result=none`; `root_closed=false`.

## 1. Frozen scope

Use the C36 two-neighborhood split host `G(r,A;p,q)`: the core is `K_r`,
`|A|=a`, `C=V\A`, `|C|=c`, there are `p` short leaves adjacent exactly
to A and `q` long leaves adjacent to the whole core. This candidate is
only for the nondegenerate C36 domain `a,c>=3` and assumes the C36 ray
`ell6` is maximal (ties allowed).

All packings are edge-disjoint triangle packings. Every resource edge
assigned to one leaf must be part of a matching for that leaf. `lambda`,
`nu_star`, `Q`, `J`, `nu`, `L_D` and `J_fix` retain their separate
definitions.

The claim is

    nu_star(G)-nu(G) <= 11 r,

and hence, using the C22 candidate identities,

    cp(G) <= lambda(G)+22r
          <= n^2/6+23n.

The constants are deliberately coarse. The proof has a source-backed
design input and is not trusted admission.

## 2. Algebra forced by d6 dominance

Write

    A0=C(a,2), B=ac, C0=C(c,2), P=ap, U=aq, V=cq.

C36 gives

    ell6=(-3A0+B+C0+3P+U+V)/3.

Comparing ell6 with the other effective rays gives:

1. `ell6>=ell0` implies `p>=a-1`.
2. `ell6>=ell5` gives `q(c-a)>=0`. Thus if `q>0`, `c>=a`.
3. `ell6>=ell7` gives `a(c-q)>=0`, hence `q<=c`.
4. If `q=0`, `ell6>=ell3` reduces to `c>=a+1`.

Substituting `lambda=ell6` in `nu_star=(|E|-lambda)/2` gives the exact
fractional target

    nu_star = A0 + (B+C0+U+V)/3.                    (2.1)

Thus the short AA resource contributes at most A0 units, and every
remaining positive unit belongs to the residual graph described next.
Extra short-leaf spokes above the threshold are not part of (2.1) and
are not charged as a packing loss.

The checker audits these implications on a broad finite parameter box;
the displayed algebra, not that audit, is the universal argument.

## 3. Short AA owner

We first assign core edges inside A to actual short leaves.

If `a` is even, the standard round-robin one-factorization of `K_a`
has `a-1` perfect matchings. Since `p>=a-1`, assign these factors to
distinct short leaves. Every AA core edge is used exactly once.

If `a` is odd and `p>=a`, use the `a` near-perfect matching classes of
the round-robin factorization of `K_a`.

Only `a` odd and `p=a-1` leaves a defect. Omit one near-perfect factor;
exactly `(a-1)/2` AA edges are then unused. In all cases the actual
short-leaf triangles form matchings at each leaf and

    h_A := A0 - (# packed short AA edges) <= (a-1)/2 < r/2.  (3.1)

No residual design below uses an AA edge, so this owner class is
edge-disjoint from every later class.

## 4. q>0: the residual is a complete graph with two holes

Let Y be the set of q long leaves. On the vertex set `A union C union Y`
consider

    H = K_(a+c+q) - K_a - K_q.                       (4.1)

Its edges are exactly:

- AC core edges;
- CC core edges;
- A--Y long spokes;
- C--Y long spokes.

A triangle of H can only have one of the forms

    ACC, CCC, A-C-Y, C-C-Y.                           (4.2)

The last two are actual long-leaf triangles. Therefore an exact triangle
decomposition of H is automatically a valid host packing using only the
d6-tight object types. In particular, for a fixed y in Y, the core
edges paired with y form a matching: two triangles through y cannot
reuse a y-spoke in an edge decomposition.

### 4.1 Residue repair

For positive integer `t`, put

    f(t) = largest positive integer <=t congruent to 1 mod 6.

Choose arbitrary actual subsets

    A' subset A, |A'|=a'=f(a),
    Y' subset Y, |Y'|=q'=f(q),
    C' subset C, |C'|=c'=f(c).

At most five vertices are deleted from each class, hence at most 15 in
total. Since d6 gives `c>=max(a,q)` and f is monotone,

    c' >= max(a',q').                                  (4.3)

Put `v'=a'+q'+c'`. Then a',q',c' are 1 mod 6, so v' is 3 mod 6.
Consequently v',a',q' are odd and

    C(v',2)-C(a',2)-C(q',2) = 0 mod 3.                 (4.4)

Moreover (4.3) is exactly

    v' >= a'+q'+max(a',q').                            (4.5)

The Bryant--Horsley two-disjoint-holes theorem therefore gives a triangle
decomposition of

    H' = K_v' - K_a' - K_q'.                           (4.6)

Every block in (4.6) is one of the four types (4.2), so its edge-owner and
leaf-matching semantics are exact.

### 4.2 Loss ledger

Let `E_res=B+C0+U+V=|E(H)|`. The fractional residual contribution in
(2.1) is `E_res/3`; the construction gets `|E(H')|/3`.

There are at most 15 exceptional vertices. Since `q<=c<=r`,

    |V(H)|=r+q<=2r.

Deleting one vertex removes at most `2r-1` residual edges, so

    (E_res-|E(H')|)/3 < 10r.                           (4.7)

Together with (3.1),

    nu_star-nu < 10r+r/2 < 11r.                        (4.8)

This loss is paid once at the union boundary. It is not a per-layer,
per-slot, or support-change payment.

## 5. q=0: the one-hole residual

Now

    H=K_r-K_a,

and d6 dominance forces `c>=a+1`.

If `c<6`, then `r<=9`; leaving all residual edges unpacked costs less
than `C(9,2)/3=12`, already below the final `11r` allowance.

Assume `c>=6`. Let

    c' = largest multiple of 6 not exceeding c,
    a0 = f(a).

If `c'>=a0+1`, take `a'=a0`. Otherwise take `a'=a0-6` when `a0>=7`;
when `a0=1` no adjustment is needed. Because `c>=a+1`, the only possible
failure of `c'>=a0+1` has `c'=a0-1`, so after the adjustment

    c'>=a'+1.

We have

    a' = 1 mod 6, c'=0 mod 6, v'=a'+c'=1 mod 6,
    v' >= 2a'+1.

Thus the Doyen--Wilson theorem supplies a Steiner triple system of order
v' containing one of order a'. Removing the subsystem blocks is exactly
a triangle decomposition of `K_v'-K_a'`.

The residue adjustment deletes at most 11 A vertices and five C vertices.
Hence the residual fractional loss is less than `16r/3`; with (3.1) it is
less than `6r`, and therefore also below the uniform `11r` bound.

## 6. Edge ownership and lifting audit

The owner classes are disjoint:

1. short-leaf triangles own AA core edges from the chosen matching
   factorization;
2. residual design triangles own no AA edge;
3. every residual edge belongs to exactly one design block;
4. every long-leaf block contains exactly one long leaf and two distinct
   core vertices; edge-disjointness makes each long leaf's core resource
   set a matching;
5. exception-incident core edges and leaf spokes are simply unused by this
   triangle packing and may later be singleton clique pieces in p23.

AAA/AAC do not occur in the residual design because AA is a hole.
The retained core types are ACC and CCC; the mixed leaf types are
betaAC and betaCC. No edge can be both a core triangle edge and a leaf
resource edge.

Zero multiplicity is treated separately above (`q=0`). The equal-prefix
case `A=V` is outside `c>=3` and is not pulled into the C36 quotient.
No denominator or half-integrality assumption is used. The old quarter
and twelfth extreme-point controls remain outside this construction's
logic.

## 7. Source boundary

The two-hole input is Darryn Bryant and Daniel Horsley, *Steiner triple
systems with two disjoint subsystems*, Journal of Combinatorial Designs
14(1), 14--24 (2006), DOI 10.1002/jcd.20071. Its published abstract
states the exact necessary-and-sufficient conditions used in (4.3)--(4.6).

The one-hole input is the classical Doyen--Wilson embedding theorem:
for admissible Steiner orders u<v, an STS(u) embeds in an STS(v) iff
v>=2u+1. Here both repaired orders are 1 mod 6.

The source comparison is recorded separately. Original publisher PDF
bytes were not frozen, and neither theorem is kernel-checked or independently
attested in this packet. Thus C38 is source-backed candidate mathematics.

## 8. Falsifier and finite replay

The generator-side exact checker:

- checks every d6-dominant tuple with `3<=a,c<=60`, `0<=p<70`,
  `0<=q<=60`: 3,356,402 rows;
- verifies the residue repairs and theorem hypotheses in every such row;
- constructs exact-cover decompositions for seven small repaired residuals,
  including two-hole and one-hole cases;
- rejects twelve deliberately invalid boundary/ownership mutations.

The small exact covers are independent finite falsifiers for the residue
logic. They do not prove Bryant--Horsley, Doyen--Wilson, or the universal
d6 theorem.

## 9. Root boundary and continuation

This candidate closes only the C36 d6 cone, subject to the stated
source-backed design inputs. C35 closes the full one-third face candidate,
C36 closes d8, and C37 closes d7. The remaining nondegenerate quotient
cones after C38 are d3 and d5.

The next root action is to attack d5 and d3 by their exact tight object
sets, seeking an actual ell_i+O(n) clique partition or a genuine
primal-dual obstruction. No statement here proves general split
domination, arbitrary nested neighborhoods, or the ProblemContract root.
