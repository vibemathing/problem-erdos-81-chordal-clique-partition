# C27: one-third dual rigidity and affine-flag global repacking

Candidate: candidate:erdos81-a01-c27-uniform-face
Repository: vibemathing/problem-erdos-81-chordal-clique-partition
Problem: problem:erdos-81-chordal-clique-partition
Attempt: attempt:web-20260906-erdos81-a01
Route: route:split-extremal-reduction-v1
Graph: graph:erdos81-initial-v1
Transport obligation: obligation:erdos81-split-extremal-reduction
Base: 0588b8372b85a65f1838e5ca4fcb009a03ffd12e
Owner: math-proof. Verdict: candidate_only. best_verified_result: none.

## 1. Exact scope and what is still open

G(r,a,b,p,q) has a complete core [r]={0,...,r-1}, p independent leaves on [a], and q independent leaves on [b], with no other leaf edges. Counts are nonnegative integers, 0<=a<=b<=r. We use the capped domain from C24: a class on d<=1 has count zero; otherwise its count is at most d-1 for even d and d for odd d. Zero counts and equal prefixes are retained as tagged budgets when useful. All packing is edge-disjoint.

L is the full fractional triangle-packing optimum. The edge-specific joint model has a core-triangle coordinate z_T, a short coordinate alpha_e for e in K_a, and a long coordinate beta_e for e in K_b. Its constraints are

  alpha_e+beta_e+sum_(T containing e)z_T <= 1,
  deg_alpha(u)<=p (u in [a]), deg_beta(u)<=q (u in [b]),
  all coordinates nonnegative.

Its fractional value is L: aggregate actual leaf triangles, or distribute each type's aggregate edge weight equally among that type's leaves for the converse. At count zero the corresponding variables vanish, with no division. J restricts all coordinates to integers. Q restricts only core coordinates to integers. Thus J<=Q<=L. A feasible Q witness need not be an actual integer packing of the original graph.

The current target is L-Q<=K*r on the WHOLE face admitting an optimal full dual whose positive prices are all 1/3. This paper does not prove or disprove that whole-face assertion. It proves it on an explicit, all-order affine-flag subclass, including arbitrary allowed repetitions, high loads, zero/equal levels, both budget parities, and a bounded vertex-deletion extension. The unrestricted two-prefix theorem, nonuniform duals, many levels, exact split domination, and ProblemContract root stay open.

No prior integral core support is kept fixed. The construction below recomputes all objects from the current parameters and may replace quadratically many old integral triangles at zero objective cost. It does not charge support changes.

## 2. The exact meaning of the one-third face

Write the joint LP as max 1^T x, A x<=B, x>=0. EVERY column has exactly three entries equal to one: either three core rows, or one core row and two distinct tagged endpoint rows. Let y>=0 be a feasible dual with positive entries all 1/3. Each column costs at most one; feasibility requires cost at least one. Therefore all three incident rows have price 1/3. For r>=3 every core row occurs in a core-triangle column, and every endpoint row of a prefix of size at least two occurs in a leaf column. Other endpoint budgets are zero in the capped domain.

Consequently, for r>=3, the condition that SUCH A DUAL IS OPTIMAL is precisely

  L = ( C(r,2)+a*p+b*q )/3.                              (U)

The all-one-third vector is always feasible; its feasibility alone is NOT (U). In this face every optimal primal saturates all rows with a positive budget. For any feasible joint point x,

  L-sum_j x_j = ( S_core(x)+S_endpoint(x) )/3,           (I)

where S_core is the sum of all unused core-edge capacities and S_endpoint the sum of all unused tagged endpoint budgets. There are no reduced-cost terms, since every column has cost exactly one. This formula counts actual capacities, not the number of objects changed.

For r<3, inactive core rows can exist and the preceding rigidity argument is not asserted. Directly L-Q<=C(r,2)<=1; these are bounded exceptional orders. Inactive zero-budget rows contribute nothing. This separates the phrase 'all positive prices' from an unwarranted assertion about irrelevant rows.

On this face, when a>0, saturation implies

  p<=max(a-1,0),  p+q<=max(b-1,0).                       (N)

Indeed all alpha edges at a fixed short-prefix vertex lie in [a], and all alpha/beta edges there lie in [b], whose shared edge capacities sum to at most b-1. If a=0 then p=0 and q<=max(b-1,0) follows instead from a long-prefix vertex. Conditions (N) alone are not claimed sufficient at arbitrary r,a,b.

The earlier C25 quarter example (5,2,4,1,1) has L=5 but the one-third upper bound 16/3, so it is OUTSIDE this face. In contrast, twelfth-point.json supplies a new full-face extreme point at (7,3,7,1,1): all 31 rows saturate, L=31/3, and its 28 positive columns have rank 28. Its nonzero denominators include 4 and 12. Thus even this face is not assumed half-integral. Its Q optimum is not claimed by that point certificate.

## 3. An all-order theorem on affine-compatible prefix sizes

Let r=3^k, k>=0. Allow each of a,b to be zero or a power of three at most r, with a<=b. Interpret [3^i] as the coordinate subspace of F_3^k in which only the first i coordinates may be nonzero, using least-significant-coordinate integer labels. Suppose (N) holds and p,q>=0. Empty or singleton prefixes force their own count to zero.

THEOREM. These parameters satisfy (U). There is a fully explicit Q witness with every core edge used exactly once and

  S_endpoint = a*(p mod 2)+b*(q mod 2)                  (a<b),
  L-Q <= [a*(p mod 2)+b*(q mod 2)]/3 <= (a+b)/3.

If a=b=d, there is instead a witness with

  S_endpoint=d*((p+q) mod 2),
  L-Q<=d*((p+q) mod 2)/3.                               (A)

In particular, when p,q are even the proper two-level instance has L=J=Q. When equal prefixes have even total count we claim L=Q, not necessarily L=J. These statements do not claim L=nu, because individual leaf edge coloring is a different step.

Within the affine-compatible size class, (N) is both necessary and sufficient for (U); the necessity was established above and sufficiency is the construction below. This includes unsaturated two-prefix high-load families, not just the old saturated-prefix or dense-residual region.

### 3.1 One shared partition of all core edges

In V=F_3^k the unordered affine lines are triples {u,v,-u-v} with u!=v. The third point is distinct from both: equality with u would force v=u in characteristic three. Each unordered pair determines its unique third point. Hence the lines partition E(K_r).

A direction is a nonzero vector modulo multiplication by -1, represented canonically by the smaller of d and -d in the integer labels. There are (r-1)/2 directions. For any direction d, its affine lines partition V, so each vertex belongs to one line in that direction and has two incident edges of that direction. Directions within a coordinate subspace W give a partition of W into lines as well. A line of such a direction that meets W is contained in W; all its other cosets are disjoint from W.

Let D_a subset D_b be the direction sets of the short and long subspaces, of sizes max(a-1,0)/2 and max(b-1,0)/2. Empty sets have no directions. The construction uses this ONE core-edge partition; no separator occurrence creates additional capacity.

### 3.2 Explicit saturated fractional certificate

Choose rational direction masses x_d in [0,1] on D_a with sum x_d=p/2. Fill directions in their fixed order, up to one each, so at most one is half-full. Next choose y_d in [0,1] on D_b, with x_d+y_d<=1 on D_a and sum y_d=q/2. The remaining total capacity is (b-1-p)/2, at least q/2 by (N). Filling in order terminates; all masses are multiples of 1/2.

For each affine line T of direction d assign

  alpha_e=x_d for e in T if T subset [a], otherwise zero;
  beta_e=y_d for e in T if T subset [b], otherwise zero;
  z_T=1-x_d*1_(T subset [a])-y_d*1_(T subset [b]).

All other core-triangle coordinates are zero. A core edge belongs to exactly one such line, so its combined load is exactly one. At each short-prefix vertex the alpha degree is 2 sum x_d=p; at every long-prefix vertex the beta degree is q. No assumption on integer packing is made here. The objective is (U), which matches the full dual with all active prices 1/3. This proves its optimality and shows that the optional affine reservoir D has L_D=L for this subclass.

### 3.3 Entirely new integer core support and the charge

For a<b let p'=2 floor(p/2), q'=2 floor(q/2). Select p'/2 whole directions from D_a for short allocation. Select q'/2 different directions from D_b for long allocation. Their existence follows from p'/2+q'/2<=(b-1)/2. This selection is anew; it need not be a subset of the positive directions or triangles in any input optimum.

Use the rule in 3.2 with these direction masses zero or one. Every z is now zero or one, and alpha/beta also are zero or one. Core edges are all used once. Each short endpoint leaves budget p-p' in {0,1}, and each long endpoint leaves budget q-q' in {0,1}. Charge each unused unit to that very tagged vertex. This is an injection into at most a+b slots, with no repeated leaf or separator payment. Formula (I) proves (A). The final core support can replace any previous integral triangles.

For a=b=d, combine the fractional leaf variables into gamma of endpoint budget s=p+q. Use floor(s/2) whole directions and gamma=1 on their edges. Split each retained gamma into alpha=(p/s)gamma and beta=(q/s)gamma when s>0. Each vertex has combined missing endpoint budget s mod 2; charge it to one untagged vertex of [d]. If s=0 both variables vanish. The integer core remains unchanged by this split, establishing the Q claim without an integral splitting assumption for J.

These algorithms terminate after finite enumeration of directions, lines and edges. Quarter-valued or twelfth-valued input optima require no special case: no original positive coordinate is used as a rounding premise.

## 4. Quadratically many old integral triangles can change at zero cost

For r=3^(2h), h>=2, take (a,b,p,q)=(9,r,2,(r-1)/2). Both budgets are even, proper, and satisfy (N). The previous construction is an optimal all-integer JOINT point x with L=J=Q. Its load is of order r/2, outside the earlier h<=r/20 dense-residual condition for large r.

Write v=(v_0,v_1,...), and define the bijection

  pi(v)=(v_0, v_1+v_0^2, v_2,...),

with arithmetic modulo three. It preserves the short subspace [9] and the whole core, hence is an automorphism of this two-prefix host. Apply pi to x to obtain another optimal integral point x_old. Both are extreme points of the joint polytope: a feasible 0/1 point is extreme since each coordinate lies in [0,1].

Any affine line whose direction has nonzero first coordinate is mapped to a triple whose coordinate sum has second entry 2, not zero. Its image is not an affine line. There are r/3 such directions. At most q/2+1 directions need be excluded for the long allocation and the short allocation. Therefore at least (r-9)/12 whole directions survive in the new core packing. Each has r/3 lines. Replacing x_old by x consequently removes at least

  r(r-9)/36

old integral core triangles, while the actual objective loss and total slack are ZERO. This is an allowed objective-preserving global repacking, not a claim that every good solution must change that many objects. It explicitly permits more than Omega(r log r) support changes. The k=4 (r=81) replay records 375 removed old triangles, exceeding the proved lower bound 162, at zero loss.

## 5. Even core/prefix boundaries by a bounded deletion extension

Here is an explicit limited extension, not a claim that every size is close to a power of three. Suppose a uniform-face instance G is obtained from an affine-compatible host G' as in Section 3 by deleting d<=2 core vertices and retaining the leaf vertices. Relabel the retained core in order; prefixes remain prefixes. Write R for the larger core order and r=R-d>=1.

Restrict the constructed Q witness of G': remove every core triangle meeting a deleted vertex and every allocated leaf-core edge meeting one. Remaining core variables are integral; all capacities and budgets can only decrease. Charge each removed object (or fractional object mass) to its first incident deleted-vertex core edge. The total weight charged to any such edge is at most its original core load one. Hence the loss is at most d(R-1). Weak monotonicity L(G)<=L(G') follows by extending any fractional packing by zero.

Consequently, using the bound (a'+b')/3<=2R/3 in the larger host,

  L(G)-Q(G)<=2R/3+d(R-1)<=8r.

This proves an absolute-constant bound on this additional uniform-face subclass, including some even core/prefix orders. It does NOT cover arbitrary nonaffine sizes or assert a result for nonuniform prices. If a retained class exceeds its degree cap, the irrelevant excess budget may be capped at d_prefix-1 for L and Q; this is not a cp identity.

The three frozen finite deletion tests include (8,3,8,1,1), (8,2,8,1,1), and the new twelfth-point parameter (7,3,7,1,1). Their one-third face membership is checked by explicit rational primal/dual equality. Witnesses need not optimize Q; that distinction is recorded.

## 6. Audit and dependencies

The new all-order construction uses only finite vector arithmetic over {0,1,2}, unique edge ownership, weak LP duality, and the displayed charging identities. It imports no external design-existence, decomposition, half-integrality or regularity theorem. The C25 immutable module is a computational dependency only; the universal proof does not depend on its finite outputs.

The C26/value-reservoir recovery package was verified byte-for-byte against all 14 entries of its supplied manifest. Its proof digest is 911052d91753a994ca754ce057ac0a1fd666bc119a23140f50a0558f7afd300a. That local recovery material is not silently identified with the separately merged dense-core C26. The optional-reservoir concept is a prior comparison, while Section 3 explicitly supplies an objective-correct reservoir for its stated subclass. The earlier frozen-core and bad-reservoir families are not repeated as new results.

The checker validates every edge and endpoint load, the tagged charge, and the field shear. It uses two rational LP implementations and two core-edge-mask enumerators to compute Q on the stated finite small face range. The named nonaffine extreme point is rank-checked and compared with both LPs, but its Q optimum is not computed. Different implementations still share the generator trust domain. Finite successful execution, hashes, CI and merge do not close a mathematical obligation.

The side dependency chain is: scope and matrix columns -> face rigidity and identity -> affine line partition -> nested direction allocation -> parity charge -> restricted bound. The support-change example and deletion extension have their separate elementary arguments. Nonapplicable methods: no probabilistic inference, no asymptotic extrapolation, no hidden induction on the finite test table. The construction is uniform in k; exhaustive finite loops test implementations, not its universal quantifiers.

## 7. First remaining gap

For arbitrary capped r,a,b in the uniform-price face, no aligned affine line system has been constructed, nor has a replacement schedule with O(r) unused capacity been proved. Most such sizes are not covered by Section 3 or the two-vertex extension. The twelve-denominator point confirms that half-integrality cannot supply that missing step.

The exact next lemma is an arbitrary-size shared-core decomposition/schedule whose capacity defect (not support distance) is bounded by K*r, allowing the core triangles to be completely reselected. An affine flag supplies such a schedule on the subclass above; it is not evidence that every feasible parameter tuple has one. A next atomic extension is one arbitrary prefix size inside an affine core with full long prefix, retaining the single-use core-edge partition while controlling the defects where that prefix cuts affine lines. Counting all cut lines independently would reintroduce a potentially quadratic charge, so that bound must not be assumed.

The whole one-third face, nonuniform prices, many levels, exact split domination and ProblemContract root remain open. Status: NONTERMINAL_CHECKPOINT; verdict=candidate_only; best_verified_result=none. No trusted verification or admission is self-signed.
