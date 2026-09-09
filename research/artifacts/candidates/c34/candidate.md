# C34 candidate summary: growing multiplicities in two complementary domains

Status: `candidate_only`; `best_verified_result=none`; `root_closed=false`.

## Frozen model

The host consists of a clique core `K_r`, an actual short set `A` of size `a`, `p` independent short leaves adjacent exactly to `A`, and `q` independent long leaves adjacent to the whole core. `L=nu_star` is the fractional edge-disjoint triangle-packing optimum. `Q` requires integral core triangles but permits aggregate fractional leaf resources. `J` also requires integral aggregate resources. `nu` additionally requires decomposition into the actual leaf matchings. `Q`, `J`, `nu`, `L_D`, and `J_fix` are distinct.

## Claim A: corrected mechanical partial component

For an odd power-of-three fiber order `m`, partial size `0<b<m`, and `D=floor(p/2)`, put

`mu=ceil(bD/m)` and `delta=m*mu-bD`.

The aggregate short resource graph has

`E=3bD+2m(D-mu)`

edges. The previous intermediate count omitting two edges from each transversal triangle is false. After one aggregate edge-coloring repair, the total partial-component capacity defect is `<7m` for odd `p`, `<17m/2` for positive even `p`, and zero for `p=0`. The diagnostic `(m,b,p)=(9,1,8)` has `E=66`, endpoint defect `20`, and total packet `42`.

## Claim B: external translation-slot growth theorem

Let `r=mR`, with `m,R` powers of three and `R>=9`. Write `a=hm+b`, where `2<=h<=R-1` and `0<b<m`. Assume

`floor(p/2)<=(m-1)/2` and `floor(q/2)<=m(R-3)/2`.

A fresh product decomposition uses one quotient direction for the short partial component and distinct direction-translation slots for the long resource graph. Every core edge has one owner. Converting each aggregate resource graph once to actual leaf matchings gives an actual host packing with capacity defect

`S<3r+4m<=31r/9`,

hence

`nu_star-nu<31r/27`.

Both multiplicities may be linear in `r`; for example `(r,m,R,h,b,p,q)=(729,81,9,4,40,80,400)` satisfies the hypotheses. Support distance is not charged.

## Claim C: arbitrary-set low-total-load theorem, source-backed

There is `r0` such that for every sufficiently large odd `r`, every actual short set `A`, `0<=p<=max(a-1,0)`, and

`p+q<=r/4-6`,

the host has an actual triangle packing with a leave of at most `5r/4+1` edges. Consequently

`nu_star-nu<=5r/12+1/3`.

The proof assigns round-robin short matchings and sequential near-perfect long matchings first, repairs parity by edge-disjoint two-edge paths, repairs edge-count modulo three by at most two vertex-disjoint four-cycles, and invokes the source-backed Delcourt--Postle theorem that every sufficiently large `K_3`-divisible graph of minimum degree at least `3n/4` has a triangle decomposition. This external theorem was not re-proved or executed by the checker.

## Claim D: multiplicity-independent leaf conversion

Existing C25 and C24 candidate lemmas give

`Q-J<=a+r` and `J-nu<=floor(a/2)+floor(r/2)`.

Thus every two-level instance satisfies the candidate bound

`Q-nu<=3r`.

The leaf-coloring correction is paid once for the short aggregate graph and once for the long aggregate graph, not once for each leaf. The remaining root difficulty is the global core-reselection gap `L-Q`.

## Claim E: saturated-short face classification

For odd `r`, `a,c>=3`, `c=r-a`, and `p=a-1`, the C28 interval criterion places the instance on the full all-one-third face exactly when

`c>=a+1` and `0<=q<=c`.

This isolates a remaining high-load wedge not covered by Claim C and only partially covered by Claim B.

## Scope and nonclaims

The full all-one-third face, arbitrary growing two-level multiplicities, multiple prefix levels, arbitrary clique trees, exact split domination, and the ProblemContract root remain open. The corrected C33 count is an auxiliary-formula erratum, not a counterexample to its linear route. Finite computations, CI, review, and merge are not mathematical verification or admission.
