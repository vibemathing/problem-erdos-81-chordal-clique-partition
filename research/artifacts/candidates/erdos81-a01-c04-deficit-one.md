# Erdős 81 C04: maximal-clique deficit and the single-deficit case

Candidate ID: `candidate:erdos81-a01-c04-deficit-one`
Problem: `problem:erdos-81-chordal-clique-partition`
Attempt: `attempt:web-20260906-erdos81-a01`
Route: `route:split-extremal-reduction-v1`
Graph: `graph:erdos81-initial-v1`
Target: `obligation:erdos81-split-extremal-reduction`
Base: `47a02cabf428a642322ff30330952f3cc874687f`
Verdict: `candidate_only`.
Method: natural-language proof draft; no mathematical program, enumeration, solver or proof assistant was run.

## 1. Scope and dependencies

The target remains: every n-vertex finite simple chordal G has a same-order split H with cp(H)>=cp(G), where cp counts an exact edge partition into complete subgraphs. The unrestricted target and root remain open.

Use the C01 complete-split benchmark B(n)=floor(n(n+1)/6), C02's PEO edge bound, and C03's two-outside-edge packing and order-eleven filter. Their candidate paths have the common prefix `research/artifacts/candidates/erdos81-a01-` and suffixes `c01-core-obstructions.md`, `c02-outside-edge.md`, `c03-clique-exchange.md`. These are explicit proof dependencies, not verification receipts.

Write r=omega(G), m=|E(G)|,
    f_r(n)=(r-1)n-binom(r,2),
    delta=f_r(n)-m,
    U(n,r)=(r-1)(n-r)+1.
The only external structural input is the chordal clique-tree/PEO characterization, scoped in C01 source S3, Section 2. Allowed axioms: finite-graph-basic, finite-combinatorics, real-arithmetic.

## 2. C04.1: a PEO can end in any specified maximal clique

Let C be a maximal clique of a chordal graph. There is a perfect elimination ordering whose final |C| vertices are exactly C.

For a connected noncomplete component containing C, root a clique tree at its bag C. A leaf bag L different from C has a vertex x in L but not in its parent: otherwise L would not be maximal. The running-intersection property implies x belongs to no other maximal-clique bag. Hence every neighbor of x is in L, so x is simplicial and lies outside C. If another component exists, the same leaf argument supplies a simplicial vertex there; for a complete component any vertex works. Remove a simplicial vertex outside C and repeat. Induced subgraphs remain chordal, and C remains maximal. Eventually only C remains, and any ordering of it finishes the PEO.

This argument also covers a disconnected G and a singleton maximal clique. No uniqueness of a clique tree is assumed.

## 3. C04.2: the deficit controls all maximal cliques

Every maximal clique C of a chordal graph with actual clique number r has
    |C| >= r-delta.

Let c=|C| and use C04.1. In a PEO, a vertex with j later vertices has at most min(r-1,j) later neighbors. For each j=c,c+1,...,r-1, the corresponding vertex is outside C and all of C is later. That vertex cannot be adjacent to all of C, because C is maximal. Thus its later degree is at most j-1, one below its cap j. There are r-c such vertices. All other cap deficits are nonnegative, and their total is delta. Therefore delta>=r-c, as required.

In particular, if r>=5 and delta=1, every maximal clique has size at least r-1>=4. This supplies exactly the premise required in C03.1, not a weaker claim that each edge merely belongs to some large clique.

## 4. C04.3: maximum-clique exchange when delta=1

Suppose G is nonsplit, chordal, r>=5, delta=1, and s=n-r>=4. Then some maximum clique Q has at least two edges in its complement.

Take any maximum clique Q. Its complement cannot be edgeless, as that would make G split. If there are already two edges, stop. Otherwise the complement is exactly an edge uv and a set I of s-2 vertices with no neighbors outside Q. Set A=N(u) intersect Q and D=N(v) intersect Q. Chordality makes A and D comparable: otherwise a in A minus D and b in D minus A induce the four-cycle a-u-v-b-a. Orient so A is contained in D.

Define nonnegative integers
    alpha=r-2-|A|,
    beta=r-1-|D|,
    epsilon_z=r-1-|N(z) intersect Q|  (z in I).
Their nonnegativity follows from maximum clique size r. Counting all edges, including the single uv edge, gives
    alpha+beta+sum_(z in I) epsilon_z=delta=1.

Case alpha=0. The set Q'=A union {u,v} is another r-clique. Write Q minus A={a,b}. Outside Q' is edge ab. At most one z in I can miss both a and b, since each such z costs epsilon_z>=1. Since |I|=s-2>=2, some z is adjacent to a or b. There are therefore at least two outside edges.

Case alpha=1. Then beta=0 and all epsilon_z=0. Write Q minus D={w}. The r-clique Q_v=D union {v} leaves outside exactly the possible edges wz for z in I; uv is no longer outside and u has no neighbor among {w} union I. If none of these edges exists, G is split, a contradiction. If two exist, stop. If exactly wz exists, choose y in I minus {z}, possible since |I|>=2. The vertex y misses w and has r-1 neighbors in Q, hence N(y) intersect Q=D. The r-clique Q_y=D union {y} leaves both uv and wz outside. These are distinct edges.

The two cases exhaust alpha, completing the exchange argument.

## 5. C04.4: a partition improvement and all orders at most eleven

Under C04.3's hypotheses, C04.2 and C03.1 give
    cp(G) <= m-binom(r,2)+1-4
          = U(n,r)-delta-4
          = U(n,r)-5.

C03 already supplies same-order split domination for all n<=10 and all omega<=5. Its order-eleven filter leaves only a possible nonsplit graph with
    n=11, r=6, m=39, delta=1, cp=23.
Here s=5, so the preceding estimate applies and gives cp(G)<=26-5=21. The complete-split benchmark B(11)=22 dominates it. Thus every chordal graph on at most eleven vertices has a same-order split dominator.

This is an analytic restricted proof draft, not a graph enumeration result, and not a universal upper bound on every split graph. A target counterexample, should one exist, must have n>=12 and r>=6, in addition to the C03 necessary inequality and the new delta=1 exclusions.

## 6. Attack pass and checkpoint

Audited cases: a maximal but nonmaximum ending clique; disconnected graphs in the PEO argument; r=c; the sum of all PEO deficits; alpha=0 versus alpha=1; the requirement s>=4; and a clique with edgeless complement already making the whole graph split. No conclusion relies on an edge-deleted residual being chordal.

best_verified_result: none.
best_verified_candidate: none.
best_available_candidate: this proof draft and its stated C01-C03 dependencies.
route_status: open.
open_obligations: `obligation:erdos81-split-extremal-reduction`; `obligation:erdos81-root`.
Canonical failed-route records remain unchanged.

Next action: preserve the exact edge-migration and PEO color-folding counterexamples as local-method failures, then examine delta=2 and a fixed-core partition formulation. The exchange claim above is NOT asserted for delta>=2; that extrapolation requires a new proof or a counterexample.
