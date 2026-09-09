# C34 — corrected partial-fiber arithmetic and two growing-multiplicity domains

Candidate: `candidate:erdos81-a01-c34-growing-multiplicity`

Status: `candidate_only`; `best_verified_result=none`.

## 1. Frozen model and claim boundary

The host has a complete core `V` of odd order `r`, an actual short set `A` of size `a`, `p` independent short leaves adjacent exactly to `A`, and `q` independent long leaves adjacent to all of `V`.  All packings are edge-disjoint triangle packings.

The coupled relaxation uses core variables `z_T`, aggregate short resources `alpha_e` on `E(K_A)`, and aggregate long resources `beta_e` on `E(K_V)`, with one shared capacity per core edge and endpoint budgets `deg_alpha<=p`, `deg_beta<=q`.  `L=nu_star` is its fractional optimum.  `Q` requires only the core variables integral; `J` also requires aggregate leaf resources integral; `nu` additionally requires the aggregate resource graphs to split into the actual leaf matchings.  `Q`, `J`, `nu`, `L_D`, and `J_fix` are not identified.

On the full all-one-third face,

```
L=[C(r,2)+ap+rq]/3,
3(L-value)=S_core+S_short+S_long.                         (1.1)
```

This manuscript does not prove the whole face, the general two-level theorem, exact split domination, or the ProblemContract root.  It proves two new growing-multiplicity subdomains, repairs a C33 arithmetic error, and isolates the remaining wedge.

## 2. Erratum for the C33 mechanical partial component

Let one component contain two full fibers `U,V` of order `m` and a partial fiber `W` of size `b`, where `m` is an odd power of three and `0<b<m`.  Put

```
D=floor(p/2),
mu=ceil(bD/m),
delta=m*mu-bD, 0<=delta<m.
```

The C33 construction selects `bD` transversal triangles and `D-mu` internal triangle factors in each full fiber.  Every selected transversal triangle contributes all three of its core edges to the aggregate short resource graph.  Hence the correct resource-edge count is

```
E=3bD+2m(D-mu),                                          (2.1)
```

not `bD+2m(D-mu)`.  The number of component vertices is `N=2m+b`; therefore the unused short endpoint budget before edge-color repair is

```
pN-2E,                                                   (2.2)
```

not `pN-4bD`.

The selected mechanical starts have floor/ceiling-balanced loads in both full fibers, so the aggregate maximum degree is at most `p-1` for odd `p` and at most `p` for even `p`.

If `p=2D+1`, Vizing's theorem gives a coloring with at most `p` colors and no deletion.  Substitution in (2.1)-(2.2) gives

```
kappa=2m+b+4delta<7m.                                   (2.3)
```

If `p=2D>0`, Vizing gives at most `p+1` colors.  Delete a smallest color class, of size at most `E/(p+1)`.  Every deleted aggregate edge loses one objective unit and creates three units of total capacity defect.  Thus

```
kappa=pN-2E+3E/(p+1)
     =4delta+3[D(2m+b)-2delta]/(2D+1)
     <17m/2.                                              (2.4)
```

For `p=0`, take `kappa=0`.  These corrected formulas preserve a uniform `O(m)` partial packet.  They supersede only the displayed C33 resource count and endpoint-defect arithmetic; no target counterexample is produced.

A diagnostic is `(m,b,p)=(9,1,8)`: the actual resource graph has `E=66`, endpoint defect `20`, and corrected packet `kappa=42`.

## 3. Product edge ownership and translation slots

Let `r=mR`, where `m` and `R` are powers of three.  Label vertices `(X,i)` with `X in F_3^s`, `i in Z_m`.  Decompose the quotient `K_R` into affine triples.  For an oriented quotient triple `(X,Y,Z)`, insert

```
((X,i),(Y,j),(Z,i+j mod m)),  i,j in Z_m.                (3.1)
```

Every pair between two of the three fibers determines the third coordinate uniquely, so (3.1) decomposes the three complete bipartite fiber pairs.  Internal affine lines decompose each fiber.  Thus every core edge has exactly one owner.

Fix a quotient direction and a translation slot `tau=j-i`.  As `i` varies, the triples

```
((X,i),(Y,i+tau),(Z,2i+tau))                             (3.2)
```

form a triangle factor on the three fibers because multiplication by two is a permutation of `Z_m`.  Across the parallel quotient triples of that direction, the same slot is a triangle factor on all `r` vertices.  Distinct direction-slot pairs are edge-disjoint.

Reserve one quotient direction for the short partial gadget.  The remaining quotient directions provide

```
m(R-3)/2                                                 (3.3)
```

pairwise edge-disjoint global translation-slot factors for the long class.  Internal short directions, distinguished-direction transversal triples, external long slots, and retained core triangles occupy disjoint core-edge classes.

## 4. External-long theorem: both multiplicities may grow linearly

Assume

```
r=mR,  m,R powers of three, R>=9,
a=hm+b, 2<=h<=R-1, 0<b<m,
floor(p/2)<=(m-1)/2,
floor(q/2)<=m(R-3)/2.                                    (4.1)
```

Use `h-2` ordinary full short fibers, one corrected partial component on two full fibers plus the `b` partial vertices, and the external translation slots for the long packet.  Every component is converted to actual leaf matchings before the pieces are united.

For a union of `D=floor(t/2)` triangle factors on `n` vertices, define the standard conversion packet

```
sigma_n(t)=0                         if t=0,
           n                         if t is odd,
           3tn/[2(t+1)]              if t>0 is even.       (4.2)
```

For odd `t`, the aggregate degree is `t-1`, so `t` colors suffice and only endpoint budget `n` is unused.  For even `t`, Vizing gives `t+1` colors and deleting a smallest class costs at most `tn/[2(t+1)]` resource edges, hence the last expression.  In all positive cases `sigma_n(t)<3n/2`.

Combining (2.3)-(2.4), (3.3), and (4.2), the actual host-packing defect is

```
S <= (h-2)sigma_m(p)+kappa(m,b,p)+sigma_r(q)
  < 3r+4m
  <=31r/9.                                                (4.3)
```

The second inequality uses `h<=R-1`; the last uses `R>=9`.  Consequently

```
nu_star-nu <31r/27.                                      (4.4)
```

This is already a genuine growing model: for example

```
(r,m,R,h,b,p,q)=(729,81,9,4,40,80,400)
```

satisfies (4.1).  The two multiplicities are linear in the core order.  The construction may replace quadratically many old core triangles; support distance is not charged.

For arbitrary `p`, let `m` be the least power of three at least `p+1`.  Whenever `9m<=r`, `2m<=a<=r-1`, and the long-slot inequality in (4.1) holds, the theorem applies after writing `a=hm+b`; the periodic case `b=0` is the C32 construction.

## 5. Arbitrary sets and no-buffer cases at low total load

The preceding theorem still needs two whole short fibers.  The next theorem has no fiber or one-third-face hypothesis.

### 5.1 Source-backed decomposition input

We use the following current-preprint theorem of Delcourt and Postle.

> Every sufficiently large `K_3`-divisible graph `H` on `n` vertices with `delta(H)>=3n/4` has a triangle decomposition.

The source is *A Proof of Nash-Williams' Conjecture*, arXiv:2606.11178: Conjecture 1.1 states the quantified assertion and Theorem 1.8 states that it is true.  This is a source-backed input, not a trusted verifier receipt.

### 5.2 Dense-residual theorem

There is `r_0` such that for every odd `r>=r_0`, every actual short set `A`, and

```
0<=p<=max(a-1,0),
q>=0,
p+q<=r/4-6,                                               (5.1)
```

the host has an actual edge-disjoint triangle packing whose leave has at most

```
5r/4+1                                                    (5.2)
```

edges.  Therefore

```
nu_star-nu<=5r/12+1/3.                                   (5.3)
```

**Allocate actual leaves first.**  Factor `K_a` by the round-robin construction.  Give `p` distinct perfect or near-perfect classes to the actual short leaves.  At most `p` short spokes remain uncovered.  Sequentially remove `q` near-perfect matchings from the remaining core for the actual long leaves.  Before the `j`-th long matching the minimum degree is at least

```
r-1-p-(j-1)>=r-p-q>=3r/4+6.                              (5.4)
```

An odd-order graph with minimum degree at least `(r-1)/2` has a near-perfect matching: if a maximum matching left at least three vertices unmatched, two unmatched vertices would have degree sum at most twice the matching size, at most `r-3`, contradicting the degree condition.  Thus all `q` choices exist and leave exactly `q` long spokes uncovered.

Let `F` be the unused core.  Then

```
delta(F)>=r-1-p-q>=3r/4+5.                               (5.5)
```

Let `O` be its even-cardinality set of odd-degree vertices.  Pair `O`.  For each pair `x,y`, choose a common neighbor `z` not previously used internally and insert the path `x-z-y`.  There are at least

```
2delta(F)-r>=r/2+10                                      (5.6)
```

common neighbors.  Fewer than `r/2` internal vertices have been used, and at most four further candidates are excluded by path edges already incident with `x` or `y`.  Hence the choice is possible.  The union `T` has odd set `O`, `|T|<=r-1`, and `Delta(T)<=3`; consequently `F-T` is even.

Let `j=|E(F-T)| mod 3`.  Remove `j` vertex-disjoint four-cycles.  A graph with minimum degree greater than half its order contains a four-cycle because two vertices have at least two common neighbors; after deleting four vertices the inequality still holds here.  If their union is `C`, then `|C|=4j<=8` and `Delta(C)<=2`.  The graph

```
F'=F-T-C
```

has all degrees even, edge count divisible by three, and

```
delta(F')>=r-1-p-q-3-2>=3r/4.                           (5.7)
```

The source-backed theorem decomposes `F'` for sufficiently large `r`.  The host leave is contained in `T`, `C`, the missed short spokes, and the missed long spokes, so

```
leave <=(r-1)+8+p+q<=5r/4+1.                             (5.8)
```

This proves (5.2).  Since every fractional triangle packing is at most one third of the host edge count, (5.3) follows.

Together with the candidate identities `cp<=lambda+2(nu_star-nu)` and `lambda<=floor(n(n+1)/6)` for chordal graphs, this domain satisfies

```
cp(G)<=floor(n(n+1)/6)+5r/6+2/3.                         (5.9)
```

This is a class theorem, not the root.

## 6. Actual leaf matching conversion no longer scales with p or q

C25 proves for every two-level instance

```
0<=Q-J<=a+r,                                              (6.1)
```

by charging fractional aggregate edge groups to tagged endpoint rows.  C24 proves

```
0<=J-nu<=floor(a/2)+floor(r/2),                           (6.2)
```

by edge-coloring each aggregate resource graph and deleting at most one smallest color class per aggregate class.  Hence

```
Q-nu<=a+r+floor(a/2)+floor(r/2)<=3r.                     (6.3)
```

The cost is paid once for the short aggregate graph and once for the long aggregate graph, not once for each leaf.  Therefore, on the full one-third face, a uniform `L-Q=O(r)` theorem would already imply the required actual `nu_star-nu=O(r)`.  The remaining integrality problem is the global core reselection `L-Q`, not per-leaf coloring.

## 7. Exact saturated-short face classification

Assume `r` is odd, `a,c>=3`, `c=r-a`, and `p=a-1`.  Then the C28 interval criterion gives the full one-third face if and only if

```
c>=a+1 and 0<=q<=c.                                      (7.1)
```

Indeed `s=c-q`, so necessity gives `q<=c`.  If `c<a` and `q>0`, the lower term `c(a-q)/2` exceeds the upper term `a(c-q)/2`; if `q=0`, the last upper inequality forces `c>=2a`, again impossible.  Thus `c>=a+1`.

Conversely, if `c>=a+1` and `0<=q<=c`, the dominant lower endpoint is `a(c-q)/2`.  It is at most the first three upper endpoints directly.  The last upper inequality reduces to

```
c(c-a-1)+q(2a-c)>=0.                                    (7.2)
```

If `c<=2a`, its minimum over `q` is at `q=0` and is nonnegative.  If `c>2a`, its minimum is at `q=c` and equals `c(a-1)`.  This proves sufficiency.

This classification identifies a major residual wedge: `p=a-1`, `c>=a+1`, and `a-1+q>r/4-6`.  It is not covered by the dense-residual theorem, and the external-slot theorem covers only those parameters that admit its two-buffer fiber representation.

## 8. Pressure tests and nonclaims

1. `AAA/AAC/ACC/CCC` ownership is never imposed as immutable type totals.  Product triangles may change globally; only actual edge ownership matters.
2. Equal prefix `A=V` is handled only in the domains whose hypotheses permit it.  Zero multiplicity means an empty aggregate resource graph and zero repair cost.
3. The C25 quarter-valued point remains outside the full one-third face; the C27 twelfth-denominator point remains an on-face control.  Neither is rounded by denominator assumptions.
4. The checker verifies exact product ownership, slot disjointness, corrected packet formulas, finite dense-residual mechanics, and twelve negative mutations.  It does not execute or verify the Delcourt--Postle theorem and cannot replace the general proofs.
5. C33's erroneous intermediate count is a failed auxiliary formula, not a failed target route.  Its corrected packet remains linear.

## 9. Remaining obligations

Priority order:

1. prove `L-Q=O(r)` on the saturated-short wedge (7.1), or produce a genuine superlinear `L-Q` family;
2. extend the product-slot construction to one whole short fiber and to no whole short fiber without invoking the dense source theorem;
3. combine multiple short prefix levels with a single tagged-endpoint rank/charging invariant;
4. return from the two-level model to arbitrary clique trees;
5. close exact split domination or the ProblemContract root with trusted verification and statement-faithfulness.

`root_closed=false`.  No EvidenceLink, Result, or Solution is asserted.