# C32: multiplicity-independent leaf conversion and two growing actual-packing domains

Candidate: `candidate:erdos81-a01-c32-growing-multiplicity`
Repository: `vibemathing/problem-erdos-81-chordal-clique-partition`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Transport obligation: `obligation:erdos81-split-extremal-reduction`
Status: `NONTERMINAL_CHECKPOINT`; verdict: `candidate_only`; `best_verified_result=none`.

## 1. Frozen model and claim boundary

Let `G=G(r,A;p,q)` be the split graph with core `V`, `|V|=r`, short set `A subset V`, `|A|=a`, `p` independent short leaves each adjacent exactly to `A`, and `q` independent long leaves each adjacent to all of `V`. There are no edges between leaves. All triangle packings are edge-disjoint.

Write `nu` and `nu_star` for the integer and fractional triangle-packing optima. The edge-specific joint relaxation uses core-triangle variables `z_T`, short aggregate variables `alpha_e` on `E(K_A)`, and long aggregate variables `beta_e` on `E(K_V)`, with one shared core-edge capacity and tagged endpoint budgets:

    alpha_e+beta_e+sum_(T contains e) z_T <= 1,
    deg_alpha(v)<=p  for v in A,
    deg_beta(v)<=q   for v in V.

Its fractional value is `L=nu_star`. Let `Q` require only the `z_T` to be integral, and let `J` require all three families integral. An actual host packing additionally splits the integral aggregate short and long graphs into `p` and `q` matchings. Thus

    nu <= J <= Q <= L.

`Q`, a reservoir optimum `L_D`, and an old-support optimum `J_fix` are different objects. Nothing below freezes an old extreme point or charges the number of support changes.

This candidate proves three things.

1. For every two-level instance, converting an optimizing `Q` point to actual leaves costs at most `3r`, independently of `p,q`; it is strictly smaller when `r` is odd.
2. For fixed `p=q=3` and `r=3^k`, there is an explicit all-order actual packing with linear leave; this is followed, not treated as the endpoint, by growing-multiplicity results.
3. For arbitrary growing `p,q` below the quarter-density barrier, there is an actual packing with `O(r)` leave. A second explicit saturated-seed family reaches total multiplicity about `7r/9`, far outside that dense-residual range.

The complete all-one-third face, arbitrary medium/high parameters, exact split domination and the ProblemContract root remain open.

## 2. The aggregate-to-actual bottleneck is uniformly linear

### 2.1 Leaf polytope rounding after the core is integral

Fix an integer core packing `P`. Its remaining capacities `c_e` are zero or one. In the leaf-only polytope, each core edge supports at most the pair `(alpha_e,beta_e)`, subject to `alpha_e+beta_e<=c_e` and the tagged endpoint budgets.

Take an extreme optimum. Call an edge group fractional if it has a nonintegral positive coordinate. Each fractional group has a nonzero two-sided local tangent: if its total is below one, perturb one positive coordinate; if its total is one, both positive coordinates are fractional and the direction `(1,-1)` preserves the tight local row. The local supports are disjoint.

Project these directions to the tight endpoint rows. They are linearly independent, because a dependence would give a nonzero perturbation preserving every tight row in both signs, contradicting extremality. There are at most `a+r` endpoint rows. Therefore there are at most `a+r` fractional groups.

Delete all fractional groups and keep the coordinates equal to one. Feasibility is preserved and the objective loss is at most `a+r`. Applying this to an optimizing integer core gives

    0 <= Q-J <= a+r.                                      (2.1)

This is the C25 rank argument restated in the present notation. It uses integral residual core capacities; it is not valid before the core variables are integral.

### 2.2 One edge-color repair per aggregate class

For a simple graph `H` with maximum degree at most `m`, define

    rho_m(H)=min{|R|: chi'(H-R)<=m}.

If `m=0`, then `H` is empty. For `m>=1`, Vizing's fan argument gives an edge-coloring with at most `m+1` colors. If only `m` colors occur, `rho_m(H)=0`. Otherwise delete a smallest color class. Since

    |E(H)| <= m|V(H)|/2,

that class has size less than `|V(H)|/2`. Hence

    rho_m(H) <= floor(|V(H)|/2).                          (2.2)

Each remaining color class is a matching and is assigned to one actual leaf. A deleted aggregate edge loses one triangle and no other edge ownership changes.

Apply (2.2) to the integer short and long graphs produced after (2.1). Their core-edge sets are disjoint by the unit core capacities. Thus

    0 <= J-nu <= floor(a/2)+floor(r/2).                   (2.3)

Combining (2.1)-(2.3),

    Q-nu <= a+r+floor(a/2)+floor(r/2) <= 3r.             (2.4)

and consequently

    nu_star-nu <= (nu_star-Q)+3r.                         (2.5)

This is the reusable shared-boundary invariant for the two-prefix model. The repair is paid once for each aggregate class, not once for each leaf and not once for each affine direction. It eliminates multiplicity dependence from the `Q -> actual host` conversion. The remaining general obstruction is entirely in `nu_star-Q`.

## 3. Fixed `p=q=3`: explicit actual packing for every `k`

Let `r=3^k`, `k>=2`, and identify the core with `F_3^k`. The affine lines `{u,v,-u-v}` partition all core edges. Choose two distinct direction classes `D0,D1`; each consists of `r/3` vertex-disjoint triples and uses exactly `r` core edges. Their edge sets are disjoint.

Write `a=3t+b`, `b in {0,1,2}`. Select `t` triples of `D1`, mark all their vertices short, and mark `b` further vertices. Map this abstract marked set bijectively to the actual `A` and transport every object by the same bijection.

Take as core triangles all affine lines except `D0` and the selected `D1` triples. Three-edge-color every triangle of `D0` and assign its three colors to the three actual long leaves. Three-edge-color every selected `D1` triangle and assign its colors to the three actual short leaves. Within each parallel class the triples are vertex-disjoint, so each color is a matching. Every used core edge has one owner, and the core triangle, short-resource and long-resource edge sets are pairwise disjoint.

All core edges are covered. Each long leaf misses one third of the core vertices, so the total long-spoke leave is `r`. Each selected short vertex misses one short spoke and each of the `b` remainder vertices misses all three short spokes, so the short-spoke leave is

    3t+3b = a+2b.

Therefore this actual packing leaves exactly

    ell_3 = r+a+2(a mod 3) <= 2r+4,                       (3.1)

and

    nu_star-nu <= ell_3/3 <= (2r+4)/3.                   (3.2)

No all-one-third-face assertion is needed for (3.2): the universal edge-capacity bound is `nu_star<=|E(G)|/3`. This closes the fixed `p=q=3` atom at candidate level and is not used as a finite extrapolation to growing budgets.

## 4. Arbitrary growing multiplicity below the quarter barrier

### Theorem 4.1

Fix `eta>0`. There is `R_eta` such that the following holds for every odd `r>=R_eta`, every `A subset V(K_r)`, and integers `p,q>=0` satisfying

    p <= f(a),
    p+q <= (1/4-eta)r,                                   (4.1)

where `f(a)=0` for `a<=1`, `f(a)=a-1` for positive even `a`, and `f(a)=a` for odd `a>=3`. Then `G(r,A;p,q)` has an actual triangle packing whose leave has at most

    r+8+p+q                                                (4.2)

edges. Consequently

    nu_star-nu <= [r+8+p+q]/3
                <= (5/12-eta/3)r+8/3.                    (4.3)

For the concrete fixed margin `eta=1/20`, this gives arbitrary linearly growing multiplicities `p+q<=r/5` and, for sufficiently large `r`,

    nu_star-nu <= 2r/5+8/3.                               (4.4)

The source-dependent threshold is uniform over all choices of `A,p,q` in (4.1).

### 4.1 Assign every short leaf an actual matching

The standard round-robin formulas decompose `K_a` into matching classes. If `a` is even, write its vertices as `Z_(a-1) union {infinity}` and use

    M_s={infinity,s} union {{s+i,s-i}:1<=i<=(a-2)/2}.

These `a-1` perfect matchings partition `E(K_a)`. If `a` is odd, use on `Z_a`

    M_s={{s+i,s-i}:1<=i<=(a-1)/2};

these `a` near-perfect matchings partition `E(K_a)` and `M_s` misses only `s`. Select any `p` classes and assign one to each short leaf. Their core edges are disjoint. The number of uncovered short spokes is zero when `a` is even and `p` when `a` is odd; in all cases it is at most `p`.

Let `H_A` be the union of these core edges. It has maximum degree at most `p`.

### 4.2 Assign the long leaves sequentially

We use the elementary lemma: an odd-order graph on `r` vertices with minimum degree at least `(r-1)/2` has a matching of size `(r-1)/2`. Indeed, if a maximum matching left at least three vertices unmatched, choose two unmatched vertices `u,v`. They are nonadjacent. On each matched edge, the total number of incidences from `u` and `v` is at most two, or an augmenting path of length three exists. Thus

    deg(u)+deg(v) <= 2|M| <= r-3,

contradicting the minimum degree.

After `j-1` long matchings have been chosen, the available core graph has minimum degree at least

    r-1-p-(j-1) >= r-p-q >= (3/4+eta)r.

It therefore has a near-perfect matching. Choose one and assign it to long leaf `j`. Repeating for `j=1,...,q` terminates and keeps all resource core edges disjoint. Every long leaf misses exactly one spoke, so the long-spoke leave is `q`.

Let `H` be the union of all short and long resource matchings and put

    F=K_r-H.

Then

    delta(F) >= r-1-p-q >= (3/4+eta)r-1.                 (4.5)

### 4.3 A linear parity and divisibility correction

Let `O` be the even-cardinality set of odd-degree vertices of `F` and pair its vertices arbitrarily. For each pair `x,y`, use the unused edge `xy` when available. Otherwise choose a two-edge path `x-z-y` in `F`, with all internal vertices `z` distinct and no previously used edge.

This greedy choice is possible for large `r`. By (4.5), any two vertices have at least

    2delta(F)-(r-2) >= (1/2+2eta)r

common neighbors. Before a pair is processed, fewer than `r/2` internal vertices have been used. Since each current endpoint can previously have served as an internal vertex at most once, at most four additional common neighbors are excluded by used incident edges. A choice remains once `2eta r>4`.

Let `T` be the union of these paths. Each vertex of `O` has odd degree in `T`; every other vertex has even degree. Moreover

    |E(T)|<=r,  Delta(T)<=3.                              (4.6)

Thus `F_1=F-T` has all degrees even.

Let `h=|E(F_1)| mod 3`. Remove `h` edge-disjoint 4-cycles from `F_1`. Such cycles exist greedily for large `r`: after (4.6), and again after one 4-cycle has been removed, the minimum degree remains greater than `r/2+2`, so any two vertices have two common neighbors. Removing a 4-cycle preserves degree parity and changes the edge count by one modulo three.

Let `C` be the union of the zero, one, or two cycles, and set

    F'=F-T-C.

Then `F'` is `K_3`-divisible,

    |E(T union C)|<=r+8,  Delta(T union C)<=7,             (4.7)

and

    delta(F') >= (3/4+eta)r-8.                            (4.8)

### 4.4 Exact core decomposition: the only external input

For sufficiently large `r`, (4.8) is at least `(3/4+eta/2)r`. Delcourt and Postle, arXiv:2606.11178v1, Corollary 1.5, state that for each fixed positive epsilon, every sufficiently large `K_3`-divisible graph of order `n` and minimum degree at least `(3/4+epsilon)n` has a triangle decomposition. Apply it with `epsilon=eta/2` and `n=r` to `F'`.

This is a source-backed input from a June 2026 preprint, not a trusted verifier receipt and not re-proved here. The source's `n` is exactly the order `r` of the residual core graph, not the order of the original split host. The quantifiers are used in the order `for fixed eta, choose the source threshold, then for every eligible graph`.

### 4.5 Assemble the actual host packing

Take the exact triangle decomposition of `F'`, the short-leaf triangles induced by the selected `K_a` matching classes, and the long-leaf triangles induced by the sequential near-perfect matchings. Core edges have exactly one owner. Within each actual leaf, the assigned core edges are a matching, so no spoke is repeated.

The uncovered edges are only `T union C`, at most `p` short spokes, and exactly `q` long spokes. This proves (4.2). Since every selected triangle covers three edges and `nu_star<=|E(G)|/3`, (4.3) follows.

For the finitely many odd orders below `R_eta`, the trivial bound `nu_star<=|E(G)|/3=O_eta(r)` absorbs them into a constant depending on the fixed `eta`. Hence Theorem 4.1 is a genuine uniform `O(r)` result over the stated growing domain, with a constant independent of `p,q,A`.

## 5. A source-free high-multiplicity power-of-three family

The previous theorem stops a fixed distance below total multiplicity `r/4`. A different construction reaches much larger multiplicities and remains on the full one-third face.

### 5.1 An exact nine-core saturated seed

Take base core `{0,...,8}`, short set `{0,1,2}`, and budgets `(p_0,q_0)=(2,4)`. Use core triangles

    034, 168, 247, 356, 578;

short aggregate edges

    01, 02, 12;

and long aggregate edges

    05,06,07,08, 13,14,15,17, 23,25,26,28,
    37,38, 45,46,48, 67.

The supplied finite certificate checks that every one of the 36 core edges occurs exactly once, every short vertex has short degree two, and every core vertex has long degree four. Thus this is an integral row-saturated joint seed of value

    [C(9,2)+3*2+9*4]/3 = 26.                              (5.1)

Its aggregate short triangle is not two-edge-colorable; (5.1) is a `Q=J` statement, not an assertion that the base host has `nu=26`.

### 5.2 Latin-fiber lifting and shared parity defect

Let `m=3^h`, `h>=0`, and take `x,y>=0` with `x+y<=m-1`. Replace every base vertex by a fiber indexed by `F_3^h`. A base core triangle `uvw` is replaced by all

    {(u,i),(v,j),(w,-i-j)}  (i,j in F_3^h).

Every pair between two of the three fibers has a unique owner. A base short or long resource edge is replaced by all edges between its two fibers, with the same aggregate owner. Within each fiber, affine direction factors supply the extra budgets `x,y`; when an odd half-factor is required, its leaf mass is retained and the complementary half core factor is rounded down. This is the C29 saturated-seed lifting argument, now with the fully listed nine-core seed above.

The lifted parameters are

    r=9m,  a=3m,  p=2m+x,  q=4m+y,                       (5.2)

so `r` remains a power of three and

    p+q<=7m-1=(7/9)r-1,
    q<=5m-1<6m=max(a,r-a).                               (5.3)

The full fractional witness saturates every core edge and endpoint row. Hence it lies on the all-one-third face. The integer-core `Q` witness has exact defect

    L-Q = [3m*((x+y) mod 2)+6m*(y mod 2)]/6 <= r/6.      (5.4)

Every between-fiber edge is owned once by its lifted base object; every within-fiber edge is owned by its unique affine line. The construction is a global replacement and can change quadratically many old support objects.

Combining (5.4) with the universal conversion and using `a=r/3`, note that `r=9m` and `a=3m` are odd, so

    Q-nu <= a+r+floor(a/2)+floor(r/2)=2r-1.

Hence the lifted family has an actual host packing with

    nu_star-nu <= 13r/6-1 < 13r/6.                       (5.5)

The constant is independent of the growing `x,y,p,q`. This family is outside the dense-residual range in Section 4 for many choices and outside the C28 high-long strip by (5.3). No external design-existence theorem is used: the finite seed and all fiber maps are explicit.

## 6. Consequence for clique partitions on the covered domains

For every graph with `m_G` edges,

    p_23(G)=m_G-2nu(G),
    lambda(G)=m_G-2nu_star(G),
    cp(G)<=p_23(G).

Thus

    cp(G)<=lambda(G)+2(nu_star-nu).                       (6.1)

C22 gives the candidate chordal bound `lambda(G)<=B(N)=floor(N(N+1)/6)` for a host of order `N`. Combining it with Theorem 4.1 gives, on that growing split subclass,

    cp(G) <= B(N)+2(N+8)/3
          <= N^2/6+5N/6+16/3.                            (6.2)

Therefore the ProblemContract form holds on this subclass with a universal linear allowance. Equation (6.2) depends on the still-candidate C22 proof and the source-backed 2026 decomposition theorem; it is not a closure of the root obligation.

## 7. Pressure tests and the remaining full-face region

1. **Edge ownership.** Short matchings, long matchings, corrected residual core, and all core triangles have disjoint core-edge sets. AAA/AAC/ACC/CCC are merely the four possible labels of core triangles in the final decomposition; no fractional type total is frozen.
2. **Actual leaves.** Sections 3 and 4 directly use matching color classes. Section 5 uses (2.1)-(2.3) and never identifies `Q` with an actual packing.
3. **Equal prefix and zero multiplicity.** `A=V` is allowed. If `p=0` or `q=0`, the corresponding aggregate graph and repair are empty. For `a<=1`, Theorem 4.1 requires `p=0`.
4. **Scale divisibility.** The dense route explicitly creates even residual degrees and an edge count divisible by three before invoking the source theorem. The fiber route requires exactly `m=3^h` and checks `x+y<=m-1` before choosing directions.
5. **Denominator controls.** The old quarter-valued point is outside the one-third face and the twelfth-valued point is inside it; neither denominator is used as a rounding premise.
6. **No layer-count charge.** For any aggregate graph of maximum degree `m`, (2.2) bounds its entire matching repair by half its vertex set, even if it is the union of arbitrarily many path, cycle, or affine factors. The old strategy of deleting once per factor is therefore unnecessary at the conversion stage.
7. **Route boundary.** The dense residual proof needs a fixed margin below total multiplicity `r/4`; at and above that range its minimum-degree certificate no longer meets the source threshold. This is a limitation of the route, not a counterexample to a linear gap.

An exact C28-criterion scan records a persistent uncovered stress family

    r=3^k,
    a=(r-1)/2,
    p=q=floor(2r/5),                                     (7.1)

for the tested powers `r=9,27,81,243,729`. These parameter tuples lie on the full one-third face, have `p+q` about `4r/5`, and satisfy `q<max(a,r-a)`. They are not covered by Theorem 4.1, the high-long theorem, or the fixed-budget constructions. The scan is only a parameter-faithfulness test, not a proof for all `k` and not a gap lower bound.

The next atomic route is to construct a zero- or linear-defect saturated seed for the balanced medium-residual profile in (7.1), or to prove a periodic mixed-core realization theorem that covers a neighborhood of that profile. The invariant must preserve one owner per actual core edge and may use the universal conversion (2.4); no future proof needs to pay a matching boundary separately for each leaf.

## 8. Nonclaims

No theorem here covers the complete all-one-third face, arbitrary numbers of distinct prefix levels, all split graphs, all chordal graphs, exact split domination, or the ProblemContract root. The Delcourt-Postle theorem is source-backed from a very recent preprint and has no registered source attestation in this repository. The finite checker, PR checks, review and merge are not mathematical Evidence. No EvidenceLink, Result or Solution is created.
