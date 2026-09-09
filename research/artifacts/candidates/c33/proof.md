# C33: balanced cyclic boundary completion

Candidate: `candidate:erdos81-a01-c33-balanced-boundary`  
Repository: `vibemathing/problem-erdos-81-chordal-clique-partition`  
Problem: `problem:erdos-81-chordal-clique-partition`  
Fresh base: `5f7049f2678bc0ea096fe6fef2a206c5e5c1f114`  
Verdict: `candidate_only`. `best_verified_result=none`.

## 1. Scope

Let `G(r,A;p,q)` be the two-neighborhood split host: the core is `K_r`; there are `p` independent short leaves adjacent exactly to the actual set `A`, and `q` independent long leaves adjacent to all core vertices. Every leaf color below is an actual matching, so the output is an actual edge-disjoint host triangle packing, not merely a `Q` or `J` point.

Put

\[
 M=\binom r2,\qquad U=\frac{M+|A|p+rq}{3}.
\]

For every actual packing `P` let

\[
 S(P)=M+|A|p+rq-3|P|.
\]

The all-one-third dual gives `nu_star <= U`, hence

\[
 0\le \nu^*-\nu\le U-|P|=S(P)/3.                 \tag{1}
\]

No full-face equality is needed for the theorem below.

## 2. Balanced cyclic partial-Latin lemma

### Lemma 2.1

Let `m` be odd, `0 <= b <= m`, and `0 <= D <= m`. There is a set `B subset Z_m`, `|B|=b`, and `bD` triples in three disjoint groups `U=V=W=Z_m` such that:

1. every selected triple has the form `(u,v,w)` with `u+v=w`;
2. every pair from two different groups occurs in at most one selected triple;
3. every `w in B` occurs exactly `D` times and every `w notin B` occurs zero times;
4. every point of `U` and `V` occurs either `floor(bD/m)` or `ceil(bD/m)` times;
5. the unselected triples of the cyclic Latin square `u+v=w` cover every unused cross-group pair exactly once.

### Construction and proof

For every integer `x` define

\[
 \epsilon_x=\left\lfloor\frac{(x+1)b}{m}\right\rfloor
             -\left\lfloor\frac{xb}{m}\right\rfloor .
\]

The word is `m`-periodic and has exactly `b` ones in a period. Put

\[
 C=\{x\bmod m:\epsilon_x=1\},\qquad B=2C.
\]

For `s in C` and `0 <= t < D`, select

\[
 T_{s,t}=(s+t,\ s-t,\ 2s).                         \tag{2}
\]

All arithmetic is modulo `m`. Since two is invertible, any two coordinates in (2) recover `s,t`; hence all pair projections are simple. The third coordinate `2s` occurs `D` times.

For any integer interval of length `D`,

\[
 \sum_{j=0}^{D-1}\epsilon_{x+j}
 =
 \left\lfloor\frac{(x+D)b}{m}\right\rfloor
 -\left\lfloor\frac{xb}{m}\right\rfloor
 \in\left\{\left\lfloor\frac{bD}{m}\right\rfloor,
            \left\lceil\frac{bD}{m}\right\rceil\right\}. \tag{3}
\]

The first-coordinate degree is the number of points of `C` in one cyclic interval of length `D`; the second-coordinate degree is the same count in a reversed interval. Thus (3) proves balance. Finally, (2) is a subset of the full cyclic transversal design, whose complement supplies the exact completion. No external Latin-square completion theorem is used.

## 3. One partial-fiber short packet

Now let `m=3^s` and `0<b<m`. Put

\[
 D=\lfloor p/2\rfloor,\quad
 N=bD,\quad
 \lambda=\lfloor N/m\rfloor,\quad
 \rho=N-\lambda m,
\]
\[
 \mu=\lambda+\mathbf 1_{\rho>0},\qquad
 t=D-\mu.                                             \tag{4}
\]

Assume `D <= (m-1)/2`. Apply Lemma 2.1 to two wholly short fibers `U,V` and to a short subset `B` of a third fiber `W`. Use every edge of every selected transversal triple as a short resource edge. Inside each of `U,V`, add `t` affine direction classes as resource triangles. The value `t` is nonnegative because `b<m`, and the directions exist by the displayed assumption.

A point of `B` has triangle incidence `D`. A point of `U` or `V` has incidence `D`, or—only when `rho>0`—`D-1`. Hence the resource graph has maximum degree `2D`.

For odd `p=2D+1`, Vizing colors it with at most `p` colors. The exact endpoint defect before coloring is

\[
 E_{\rm odd}=
 \begin{cases}
  b+2m,&\rho=0,\\
  b+6m-4\rho,&\rho>0.
 \end{cases}                                         \tag{5}
\]

No core edge is lost: selected triples are resources and every other transversal/internal triple is retained as a core triangle. Thus the partial-fiber defect is at most `7m`.

For positive even `p=2D`, Vizing gives `p+1` colors. Delete a smallest color class `R` and use the other `p` colors as the actual short leaves. Before deletion the endpoint defect is

\[
 E_{\rm even}=
 \begin{cases}
  0,&\rho=0,\\
  4(m-\rho),&\rho>0.
 \end{cases}                                         \tag{6}
\]

The resource graph has

\[
 e=3bD+2mt                                             \tag{7}
\]

edges, so `|R| <= floor(e/(p+1))`. A proper color meets a resource triangle in at most one edge. Deleting one edge therefore creates exactly one unused core edge and two unused endpoint units. The total partial-fiber defect is

\[
 \kappa_{m,b}(p)
 \le E_{\rm even}+3\left\lfloor\frac e{p+1}\right\rfloor
 <\frac{17m}{2}.                                      \tag{8}
\]

For odd `p`, define `kappa` by (5); for `p=0`, put `kappa=0`.

All resource colors are genuine matchings. All remaining cross pairs are covered by the complement of the same cyclic Latin square, so there is no slot competition or repeated boundary charge.

## 4. Global two-class theorem

For `n=3^s` define the C32 packet bound

\[
 \sigma_n(0)=0,\qquad
 \sigma_n(h)=n\ (h\text{ odd}),\qquad
 \sigma_n(h)\le\frac{3hn}{2(h+1)}\ (h>0\text{ even}).  \tag{9}
\]

### Theorem 4.1

Let `r=3^k`, let `m=3^s` divide `r`, write `R=r/m`, and suppose

\[
 R\ge3,\qquad |A|=hm+b,\qquad
 2\le h\le R-1,\qquad 0<b<m,                           \tag{10}
\]
\[
 \left\lfloor\frac p2\right\rfloor+
 \left\lfloor\frac q2\right\rfloor
 \le\frac{m-1}{2}.                                    \tag{11}
\]

Then every actual set `A` of that cardinality admits an actual host triangle packing with

\[
 S\le
 (h-2)\sigma_m(p)+\kappa_{m,b}(p)+R\sigma_m(q)
 <\frac{13r}{3}.                                      \tag{12}
\]

Consequently

\[
 \nu^*-\nu<\frac{13r}{9}.                              \tag{13}
\]

### Construction

Use an affine Steiner system on `R` base points and replace every base point by an `m`-point fiber. Internal fiber pairs are decomposed by the affine Steiner system of order `m`. For each base triple, a Latin square of order `m` decomposes all pairs between its three fibers. This partitions every core edge: pairs in one fiber use its internal system; pairs in distinct fibers use the unique base triple containing their two base points.

Choose one base triple `(U,V,W)`. Declare `U,V` wholly short and put the balanced set `B` of Lemma 2.1 in `W`; declare `h-2` further fibers wholly short. Transport this abstract set by a bijection to the given actual `A`.

Reserve disjoint internal affine directions for the short and long packets; (11) guarantees availability.

* On the `h-2` ordinary short fibers use the C32 `p`-packet.
* On `U,V,W` use the partial-fiber packet of Section 3.
* In every one of the `R` fibers use the C32 `q`-packet for long leaves.
* On the distinguished base triple use the cyclic Latin square from Lemma 2.1; selected triples are short resources and all other transversal triples are core triangles.
* Every other base-triple transversal, and every unused internal affine line, is a core triangle.

The short components are vertex-disjoint, so their `p`-color palettes can be reused. The long components lie in separate fibers, so their `q`-color palettes can also be reused. Short and long direction sets are disjoint. Thus each individual leaf receives a matching.

Every actual core edge has exactly one owner: one retained core triangle, one short color, one long color, or one deleted-color unused slot. Each retained triangle has exactly one of the types AAA/AAC/ACC/CCC after transport.

The first inequality in (12) is the sum of the disjoint packet defects. Using `sigma_m < 3m/2`, `kappa < 17m/2`, `hm <= r-m`, and `m <= r/3` gives

\[
 S<
 \frac32(h-2)m+\frac{17}{2}m+\frac32r
 \le3r+4m\le\frac{13r}{3}.
\]

### Corollary 4.2

Let `m` be the least power of three with `m >= p+q+1`. If

\[
 6(p+q+1)\le |A|\le r-1,                               \tag{14}
\]

then either `m` divides `|A|`, in which case C32 gives `S<3r`, or Theorem 4.1 applies and gives `S<13r/3`. This removes the C32 square-root restriction: both multiplicities may grow linearly with `r` on the explicit domain (14).

If `p=0` or `q=0`, the corresponding packet is empty. If `A=V` or `m` divides `|A|`, use the C32 full-period construction. Cases with fewer than two full `m`-fibers remain outside Theorem 4.1.

## 5. Pressure tests and route boundary

The checker verifies:

1. Lemma 2.1 for `m=3,9,27`, every `b,D`, and named `m=81` rows;
2. all three pair projections, cyclic completion, and exact floor/ceiling degrees;
3. formulas (4)--(8) throughout the same finite domain;
4. explicit full edge ownership in blow-ups with `(R,m)=(3,3)`, `(3,9)`, and selected `(9,9)` cases;
5. all zero/equal/full-period boundaries;
6. mutations with a duplicated cell, a repeated pair slot, an unbalanced mechanical word, overlapping short/long directions, and a nonmatching leaf color.

Finite execution is generator-side and does not prove the universal statements. Vizing's theorem is inherited as the only external mathematical input from C32.

The remaining high-multiplicity domain is now narrower: `|A|` has fewer than two fibers at every power-of-three scale capable of hosting the combined `p,q` direction demand. The exact next route is a one-buffer or no-buffer boundary gadget, not another per-layer boundary deletion and not the quadratic near-factor-color route.

Status: `NONTERMINAL_CHECKPOINT`; `candidate_only`; `best_verified_result=none`; `root_closed=false`.
