# C30: exact p=1, q=2 values by two-direction global core reselection

Candidate: candidate:erdos81-a01-c30-one-two-exact
Repository: vibemathing/problem-erdos-81-chordal-clique-partition
Problem: problem:erdos-81-chordal-clique-partition
Attempt: attempt:web-20260906-erdos81-a01
Route: route:split-extremal-reduction-v1
Graph: graph:erdos81-initial-v1
Transport obligation: obligation:erdos81-split-extremal-reduction
Protected base: c1f2486638441e48b345efce7a7159815491e7fa
Primary owner: math-proof. Verdict: candidate_only. best_verified_result: none.

## 1. Frozen statement and evidence ceiling

Let k>=2, r=3^k, V be a set of r core vertices, and A any ACTUAL subset of size 2<=a<=r. Add one independent short leaf adjacent exactly to A, and two independent long leaves adjacent to all V. There are no edges between leaves. The host has r+3 vertices, not r. Set c=r-a, M=binom(r,2), b=a mod 3 in {0,1,2}, and t=floor(a/3).

The full fractional edge-disjoint triangle-packing value is L=nu_star. Its joint variables are z_T for each actual core triangle, alpha_e on AA edges and beta_e on every core edge, with

  alpha_e+beta_e+sum_(T contains e) z_T <= 1,
  deg_alpha(v)<=1 (v in A), deg_beta(v)<=2 (v in V),
  all variables nonnegative.

Aggregation of the leaf triangles gives this model. Conversely put alpha_e on the unique short leaf and beta_e/2 on each of the two long leaves; every spoke then has capacity at most one. Q requires only the core variables z_T to be integers. J requires all variables to be integers, and nu additionally requires the actual individual leaf matchings. These parameters are NOT identified. L_D is a different relaxation restricting allowed core triangles to D without setting their weights to one; J_fix imposes a frozen old support. Neither restriction is used here.

THEOREM CANDIDATE. Every above instance is on the full all-one-third optimal-dual face, and

  L=(M+a+2r)/3,
  Q=M/3+2r/3+t/2,
  L-Q=(a+b)/6.                                           (T)

The constructed Q witness has

  S_core=(a-b)/2, S_short=b, S_long=0,
  S_total=(a+b)/2 <= (r+2)/2.                             (S)

Thus the ENTIRE requested fixed-budget slice is handled, not only a finite range, an affine subspace, a seed ratio, or a high-long-budget strip. This is a proof-drafted candidate, not a trusted verifier/admission receipt. The whole uniform face with unrestricted growing p,q, the general two-level theorem, exact split domination and the ProblemContract root remain OPEN.

## 2. A fully explicit saturated fractional certificate

All full-dual row prices equal 1/3. Every joint column has exactly three unit entries, so this is feasible and has value (M+a+2r)/3. We now prove equality rather than infer it from dual feasibility.

Use alpha_e=1/(a-1) on AA. Denote by z_3,z_2,z_1,z_0 the PER-TRIANGLE weights for AAA,AAC,ACC,CCC, and by beta_2,beta_1,beta_0 the PER-EDGE beta weights for AA,AC,CC. Omitted types have no variables; their displayed absent weights mean zero.

Case c=0:

  z_3=(r-4)/((r-1)(r-2)), beta_2=2/(r-1).

Case c=2 (then a>=7):

  z_3=(a^2-6a+10)/(a(a-1)(a-2)),
  z_2=(a-3)/(a(a-1)), z_1=1/a, z_0=0,
  beta_2=2(a-2)/(a(a-1)), beta_1=2/a, beta_0=0.

Case 2<=a<=c (so c>=5):

  z_3=1/(a-1) if a>=3, and zero if a=2,
  z_2=0, z_1=(c-2)/(c(c-1)),
  z_0=(c^2-ac-3c+4a)/(c(c-1)(c-2)),
  beta_2=0, beta_1=2/c, beta_0=2(c-a)/(c(c-1)).

Remaining case a>c>=1, c!=2 (then a>=5):

  z_3=(a-c)(a-4)/(a(a-1)(a-2)),
  z_2=(a-2)/(a(a-1)), z_1=0,
  z_0=1/(c-2) if c>=3 and zero if c=1,
  beta_2=2(a-c)/(a(a-1)), beta_1=2/a, beta_0=0.

There is no zero denominator in its stated case. Nonnegativity in the third case follows from c^2-ac-3c+4a = a+(c-a)(c-3)>=0. In the second case the only less immediate numerator is a^2-6a+10=(a-3)^2+1>0. The other numerators are visibly nonnegative under the explicit size bounds.

For each existing edge or endpoint type, the following identities hold by substitution:

  1/(a-1)+beta_2+(a-2)z_3+c z_2=1,
  beta_1+(a-1)z_2+(c-1)z_1=1                  (c>0),
  beta_0+a z_1+(c-2)z_0=1                    (c>=2),
  (a-1)/(a-1)=1,
  (a-1)beta_2+c beta_1=2,
  a beta_1+(c-1)beta_0=2                      (c>0).

They give saturation on EVERY actual edge and tagged endpoint, not just total resources. This proves L and the face assertion. This is an explicit specialization/lift of the C28 type framework, including its small-complement boundaries; it is not obtained by averaging computed examples. In particular all 2<=a<=r are allowed for k>=2.

For any feasible joint point of value v, exact counting now gives

  3(L-v)=S_core+S_short+S_long.                          (I)

No reduced-cost term appears because every column has full-dual cost exactly one.

## 3. A new global support construction with a bounded remainder

Temporarily label V by F_3^k with least-significant-coordinate integer labels. For u!=v the triple {u,v,-u-v} has three distinct points; its uniqueness from a pair shows that the affine lines partition all core edges. This is a direct construction, with no external design-existence theorem.

Let D0 be the parallel class in the first coordinate direction, and D1 the parallel class in the second coordinate direction. They are disjoint families of triples with disjoint EDGE sets, although vertices are shared. Each class partitions the r vertices into r/3 triples. The two directions exist because k>=2.

Choose ANY t triples of D1 and mark all 3t vertices short. Mark b further vertices from the unchosen part. This is always possible: if b>0 then t<r/3, leaving at least one triple. Map this abstract short set bijectively to the actual A, and its complement bijectively to V\A. Every subsequent triangle and edge is transported by this same bijection. The actual set A is not required to be an affine subset in the old coordinates.

Recompute the entire core packing P as all affine lines EXCEPT every line of D0 and the selected t lines of D1. Put beta=1 on each edge in D0. Put alpha=1/2 on each edge of the selected D1 triples. All other leaf coordinates are zero.

Each core edge belongs to exactly one original line. The removed families have different directions. Hence none of beta, alpha and P competes for the same core edge. Every vertex has beta degree two. Each of the 3t good short vertices has alpha degree one; the b remainder short vertices have alpha degree zero. The nonshort vertices have no alpha edges. All constraints are thus checked individually.

Only the selected short triples have unused core capacity: 1/2 on each of their 3t edges. Split each unused-edge capacity equally between its endpoints; each good short vertex receives charge 1/2. Charge the one missing short budget at each of the b remainder vertices to that vertex. Long budget has no deficit. There are no separator charges, old-cut-line charges, or support-distance charges. This proves (S).

There are M/3-r/3-t selected core triangles, beta mass r and alpha mass 3t/2. The value is exactly M/3+2r/3+t/2. This proves the lower bound for Q in (T).

The construction needs only enumeration of O(r^2) lines/edges plus a finite bijection; the field pair formula is uniform in k. Termination follows from finite pair/class enumeration, not induction on finite test outputs. It starts independently of any old optimum and does not restrict which old integral triangles may be reopened.

## 4. A sharp global upper certificate: parity AND divisibility by three

Consider ANY Q-feasible core packing P, not necessarily affine, and let F=K_r-E(P), e=|E(F)|. Its degrees d_v are even because r is odd and each core triangle removes two incident edges. Also e=M-3|P| is divisible by three, since r=3^k makes M divisible by three.

Let B_v=3 at short vertices and B_v=2 at other vertices, and let u_v be the total incident alpha+beta mass. Then u_v<=min(d_v,B_v). Assign half of each unused core capacity to each endpoint, then add its unused endpoint budgets. The charge at v is

  s_v=d_v/2+B_v-3u_v/2.

Its sum is EXACTLY S_core+S_endpoint. Its minimum for a fixed degree is

  psi_B(d)=d/2+B-3 min(d,B)/2.

For an even d and B=3, define preferred degree D=4 and baseline b_v=1/2. For B=2 define D=2 and b_v=0. Directly separating d<=B and d>=B, including d=0, proves both

  psi_B(d)>=b_v+(D-d)/4,
  psi_B(d)>=b_v+(d-D)/2.                              (E)

For example a short vertex of degree two costs at least one, while degree four costs at least one half; lowering degree by two does NOT save all of the parity charge. This is the additional modulus-sensitive step beyond C29's parity-only inequality.

The preferred edge count is E0=(4a+2c)/2=r+a. Summing (E) yields

  S >= a/2 + max((E0-e)/2, e-E0).                      (G)

Write delta=e-E0. The condition e=0 mod 3 gives delta=-a mod 3. Minimizing max(-delta/2,delta) over all such INTEGERS gives exactly

  0 if b=0 (delta=0),
  1/2 if b=1 (delta=-1),
  1 if b=2 (delta=-2 or +1).

Thus every Q point has S>=(a+b)/2. By (I), every Q point has value at most L-(a+b)/6. Section 3 attains it, proving the exact optimum (T). The integer relaxation here only enlarges the set of residual degree data; no claim that all degree sequences are graphical is needed for the lower bound.

This certificate permits arbitrary rational leaf weights and arbitrary core reselection. It is not a half-integral matching argument, an LP-result extrapolation or a support-freezing bound.

## 5. Complete nine-core structures and quadratic support replacement

The case k=2 has 12 original vertices (nine core and three leaves). The eight actual cardinalities have the following exact values:

  a:       2     3      4      5     6      7      8      9
  L:     56/3   19    58/3   59/3   20    61/3   62/3    21
  Q:      18   37/2   37/2   37/2   19     19     19    39/2
  S:       2    3/2    5/2    7/2    3      4      5     9/2

construct-results.json supplies all eight core-triangle lists, alpha/beta weights and actual short sets. They are full witnesses. Quotient and residual-support LPs have matching finite primal/dual data in lp-results.json. Global optimality is from Section 4, not an exhaustive nine-core Q search. No value of J, nu or cp is claimed here.

To demonstrate the absence of any reopening limit, order D1 with the line (0,3,6) LAST. If b>0 choose the b remainder vertices from this last, unselected line. The shear

  pi(v0,v1,v2,...)= (v0,v1+v0^2,v2,...), arithmetic mod 3,

preserves every D1 line setwise, and fixes the last line pointwise. It therefore preserves the abstract short set for EVERY a. Conjugate it by the actual relabeling to obtain an automorphism of the specified host. Apply it to the new Q point to obtain an old point of the SAME value and slack.

An affine line with nonzero first direction coordinate maps to a non-affine triple: its second-coordinate sum becomes 2. There are r/3 such directions. One is D0, which is not in P; the others all remain in P because D1 has zero first direction coordinate. Therefore EXACTLY

  (r/3-1)*(r/3)=r(r-3)/9

old integral core triangles disappear when replacing the sheared point by the constructed point. Lines with zero first direction coordinate map to the same direction classes; the selected D1 triples are unchanged, so none creates another removed-support contribution. This proves quadratic support change at zero OBJECTIVE CHANGE. The common optimal defect may be positive; zero change is not a claim of zero total defect. Every edge/budget remains valid under the automorphism.

## 6. Boundary and source-faithfulness checks

The theorem is uniform over arbitrary actual A, all size residues and parities, and includes A=V. When A=V the two neighborhoods are equal, but their tagged budgets remain 1 and 2. Formula (T) gives L-Q=r/6; no unjustified integral splitting or leaf-coloring inference is made.

At r=3 and a>=2, full-face saturation would require combined leaf degree three at a vertex with only two core edges. Hence no p=1,q=2 instance lies on this face. Direct small LP controls show L=3 below the uniform upper values 11/3 and 4. For r=1 there is no allowed a>=2. Empty or singleton short sets with a positive short budget are outside the frozen slice; boundary controls use the correct zero multiplicity. Separate zero-count fixtures are capacity checks, not an asserted q=0 or arbitrary-budget theorem.

The C25 (5,2,4,1,1) quarter-valued point is outside the full one-third face; the C27 (7,3,7,1,1) twelfth-valued rank-28 point is on it. These different-parameter frozen inputs are scope controls only. The present construction takes no coordinates of either point as a premise; no denominator-based restriction is imposed. Their Q values are not inferred by C30.

Let D be the newly constructed P regarded only as a set of permitted triples. Its relaxation admits the Q witness, so L-L_D <= (a+b)/6. This is not an assertion L_D=Q or a frozen-face value J_fix. The original LP and every proof upper bound still permit ALL actual core triangles.

No external Kirkman, dense decomposition, regularity, asymptotic rounding or design-existence theorem is used. The finite-field edge partition is proved in Section 3. Official design documentation was consulted only for conventional parallel-class terminology; its existence results are not dependencies. C25's frozen exact arithmetic code is a computation dependency, not a proof input. C28 and C29 provide the prior definitions/targets, whose relevant counting identities have been rederived above.

## 7. Actual execution and remaining obligations

Three bounded modes of checker.py validate the claimed exact objects. construct covers all cardinalities at r=9,27,81, all 502 actual nine-core subsets of size at least two, nine named r=243 cases and four support replacements. lp uses two separately implemented rational solvers on all 114 six-row quotient parameters and on each of the eight newly selected nine-core residual-support problems. Direct full edge certificates check the rational formulas separately from the quotient. controls tests twelve rejected mutations, nine positive zero/equal/empty fixtures and the local degree inequalities. All final modes genuinely exit zero; exact resources, versions, output digests and scope are in source-notes/c30/run-record.json. Different implementations still share the generator trust domain.

The degree dynamic program enumerates even residual-degree choices only; it is an integer RELAXATION, not enumeration of all graphs or triangle supports. The full nine-core Q optimum is proved by (G) and the explicit witness, not by a numerical or exhaustive Q optimizer. No large MILP, Lean or trusted verifier run occurred.

Dependency chain: full primal/dual formulas -> face and capacity identity; affine two-direction partition and relabeling -> feasible witness/explicit charge; arbitrary residual parity and modulo-three count -> matching global bound. The shear proof is a separate verification of objective-preserving large support changes. No finite table is used as an induction hypothesis.

This fixed p=1,q=2 atom has a complete natural-language proof candidate. It does not give a constant uniform in growing budgets p,q, nor solve the whole low-long-budget face. The first OPEN general lemma remains a shared-core schedule with O(r) unused capacity for arbitrary feasible low-budget C28 interval parameters. Multiple short-direction demands cannot be paid anew at every vertex/direction; the one reserved short direction used here does not furnish that uniform bound. Both admitted stronger obligations remain open. No EvidenceLink, Result or Solution is self-signed. Overall status: NONTERMINAL_CHECKPOINT.
