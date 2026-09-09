# C28: arbitrary short subsets, an exact face test, and two-block repacking

Candidate: candidate:erdos81-a01-c28-arbitrary-subset
Repository: vibemathing/problem-erdos-81-chordal-clique-partition
Problem: problem:erdos-81-chordal-clique-partition
Attempt: attempt:web-20260906-erdos81-a01
Route: route:split-extremal-reduction-v1
Graph: graph:erdos81-initial-v1
Transport obligation: obligation:erdos81-split-extremal-reduction
Base: 426dc1dd3ce9c3e785e9ca49689cbde643557566
Owner: math-proof. Verdict: candidate_only. best_verified_result: none.

## 1. Scope, definitions, and result boundary

The core is a complete graph on a set V of size r, with actual short subset A of size a and complement C of size c=r-a. There are p independent short leaves adjacent to A, and q independent long leaves adjacent to ALL V. Counts are nonnegative. L=nu_star is fractional edge-disjoint triangle packing. The joint coordinates are z_T on actual core triples, alpha_e on AA edges, and beta_e on all core edges. A core edge has ONE constraint alpha_e+beta_e+sum_(T contains e)z_T<=1. The endpoint constraints are deg(alpha)<=p at A and deg(beta)<=q at V. Q restricts only z to integers; J restricts all coordinates to integers; nu additionally realizes allocations by individual leaf matchings. Thus nu<=J<=Q<=L. Q is NOT an integer triangle packing of the host, and not the optimum obtained by fixing an old core support.

The user's target r=3^k is retained; several lemmas also hold at other orders, but no nonuniform-price or general two-prefix conclusion is drawn. Arbitrary actual A causes no isomorphism difficulty: any bijection taking A to [a] preserves the host and each of these optimization values. It need not preserve affine lines. Restricting to the original affine-line system would be an additional, unjustified constraint.

This candidate does NOT close the whole arbitrary-subset one-third face. It gives (i) an exact source-free scalar test of this face when a,c>=3, and (ii) a fully specified two-block repacking with O(r) capacity deficit in the high-long-budget region q>=max(a,c). The all-order availability of the auxiliary resolutions in (ii) uses the classical Kirkman triple-system existence input K. A source-free version holds whenever the explicitly specified cyclic schedules supply the requested numbers of factors. The remaining region is stated in Section 7. The earlier frontend generation failure is NOT a mathematical failed route.

## 2. Full one-third face and an exact scalar criterion

Every joint column contains exactly three unit entries. For r>=3 and active endpoint rows the all-one-third dual gives U=(binom(r,2)+ap+rq)/3. Its OPTIMALITY, not merely feasibility, defines the face L=U. On that face any feasible x has

  3(L-value(x)) = sum_e unused_core_capacity(e)
                 + sum_A unused_short_budget(u)
                 + sum_V unused_long_budget(u).                 (1)

All capacities refer to original labeled edges/vertices. Fractions 1/4 or 1/12 in an input optimum are allowed; no argument below assumes half-integrality or retains its support. At inactive small prefixes use zero short count, as in the capped domain; r<=2 is treated directly.

Here is an exact face test for a,c>=3. Set d=r-1-q and s=d-p. The face exists if and only if p<=a-1, s>=0, and the interval [ell,u] is nonempty, where

  ell=max(0, a(c-q)/2, c(a-q)/2),
  u=min(ac/2, a*s/2, c*d/2, (a*s+c*d)/6).                (2)

Proof. Average a saturated feasible solution over all permutations within A,C and within each leaf class. Write t3,t2,t1,t0 for TOTAL core weights of types AAA,AAC,ACC,CCC. Saturation of core incidences and endpoint rows gives

  3t3+2t2+t1=a*s/2,   t2+2t1+3t0=c*d/2.

Put w=t1+t2. Nonnegative beta on AA,CC and AC is respectively equivalent to

  w>=a(c-q)/2, w>=c(a-q)/2, w<=ac/2.

For fixed w, the remaining triangle nonnegativity is precisely

  max(0,2w-c*d/2)<=t2<=min(w,a*s/2-w).

Such t2 exists exactly when w<=a*s/2, w<=c*d/2 and 3w<=(a*s+c*d)/2. These are (2). Necessity of p<=a-1 and s>=0 also follows at a vertex in A. Conversely choose any w in (2), then t2 in the displayed interval, t1=w-t2, t3=(a*s/2-w-t2)/3, t0=(c*d/2-2w+t2)/3. Set alpha total ap/2 and beta totals

  betaAA=[a(a-1)-a*d+2w]/2,
  betaCC=[c(c-1)-c*d+2w]/2,
  betaAC=ac-2w.

These are nonnegative and satisfy all six resource equations. Distribute each type total uniformly over its actual objects. Incidence double counting gives load one on each core edge, p on each short endpoint and q on each long endpoint. This supplies an explicit primal matched to the all-one-third dual. Small classes must omit nonexistent triangle types; the six-row type model still works, but (2) is not asserted there.

In particular q>=max(a,c), 0<=p<=a-1 and p+q<=r-1 allow w=t1=t2=0. Thus the high-long-budget region is on the face. Its fractional witness can be written directly: alpha=p/(a-1) on AA, core AAA weights s/((a-1)(a-2)), CCC weights d/((c-1)(c-2)), betaAA=(a-1-d)/(a-1), betaCC=(c-1-d)/(c-1), betaAC=1. Empty families are omitted; singleton/two-vertex exceptions require separate handling, not division by zero.

## 3. Repacking algorithm on two actual subsets

We give the construction and its bounds for a,c>=3, q>=max(a,c), p<=a-1, p+q<=r-1. Then 0<=s=d-p<=d<=min(a-1,c-1). The constant bound below remains valid if either block has size at most two: delete that small block from the construction and use the same formulas with no good vertices there. The face itself is assumed in such exceptional cases rather than inferred from (2).

Choose a0<=a and c0<=c to be the largest orders congruent to 3 modulo 6, using 0 when a block has size below 3. Let eA=a-a0, eC=c-c0, e=eA+eC; each e_i<=5. Pick good subsets A0,C0 of those sizes; the other e vertices are temporary construction exceptions, not deleted from the host. Obtain resolutions of K_a0 and K_c0 into triangle factors (input K). A triangle factor covers every vertex of its block once, using degree two there; distinct factors use disjoint edges.

Let hA be the largest nonnegative even integer <=min(s,a0-1), and hC the largest even integer <=min(d,c0-1). For a0=0 or c0=0 choose its degree zero. Take hA/2 factors within A0 and hC/2 within C0 as the NEW integer core packing P. No old triangle is preserved by assumption. Define p0=min(p,a0-1-hA) when A0 is nonempty, and zero otherwise. On every unused A0 edge put alpha=p0/(a0-1-hA), omitting division if its denominator is zero. Set beta to one minus alpha on those edges, one on all A0-C0 edges, and one on unused C0 edges. All edges touching an exceptional vertex are initially unused.

Core capacity is exact on K_(A0 union C0). Short degree is p0 at A0 and zero elsewhere. Long degrees before repair are

  bA=r-e-1-hA-p0,   bC=r-e-1-hC.                       (3)

They may exceed q slightly; the initial point is not yet declared feasible. The inequalities

  p-p0<=eA,
  hA+p0>=d-eA-1,  hC>=d-eC-1                         (4)

hold whenever the corresponding good block is nonempty. The first follows from hA<=s and d<=a-1. For the second, either p0=p, in which case rounding hA loses at most eA+1 relative to s, or hA+p0=a0-1>=d-eA. The third is the same even-rounding bound. Thus bA-q<=1-eC<=1 and bC-q<=1-eA<=1. Also bA,bC>=0 by their explicit edge construction.

Process vertices in a fixed order. Whenever its current beta degree exceeds q, subtract the excess, at most one, from its incident positive beta weights in edge order, splitting the last subtraction if needed. Since every subtraction reduces degrees at both endpoints, no already repaired vertex becomes overloaded. An incident edge is paid only for the mass actually subtracted, even if later processed again. Total subtracted mass R<=r: charge each subtraction to the vertex whose overfull row triggered it, whose total charge is at most one. All alpha and z values remain unchanged. At termination the joint point is Q-feasible.

This is a global replacement. Every cross edge between the two good blocks is assigned to beta ONCE; no old line is repaired or charged individually. A transversal old line is simply absent from the new support. Construction time is finite once the auxiliary factors are supplied, and the repair processes r rows and finitely many edges with rational operations.

## 4. A capacity charge, not a support-distance charge

At most e*r core capacity is left unused before beta repair. The total short deficit is

  eA*p + a0*(p-p0) <= eA*(p+a0) <= eA*r,              (5)

because p<=d<=c-1. Long deficit (possibly negative before repairing overloads) is at most e*q+(r-e)*e<=2e*r: on a good vertex q-bA=e+hA+p0-d<=e, and q-bC=e+hC-d<=e. Hence the algebraic total unused capacity before repair is at most (3e+eA)r. Every unit of beta subtraction increases total unused capacity by exactly THREE (one core row, two endpoint rows). With e<=10, eA<=5 and R<=r we get

  S_core+S_endpoint <=38r,
  0<=L-Q <=38r/3.                                    (6)

The final unused capacities are all nonnegative. A more precise executable certificate records their actual sums. Fractional beta mass can be charged by measure to a tagged vertex, not incorrectly counted as a number of whole edges. Exception-edge charges have at most ten vertex tags; short-deficit charges have at most five slots per original vertex; long-deficit and overload-repair charges similarly have absolute, not multiplicity-dependent, slot counts. None is a sum of squared separator sizes.

If both original block orders are themselves 3 modulo 6, no exceptions occur. Then p0=p. Put M=a*(s mod 2)+c*(d mod 2). Before repair the total algebraic slack is -M. Each repair subtraction reduces the sum of positive endpoint overloads by at least its mass, so R<=M; hence final S=3R-M<=2M<=2r and L-Q<=2r/3. This is an auxiliary arithmetic case, not a claim that both block orders can have that residue when r=3^k.

Let D=P be the final integer core support. It is allowed in the restricted reservoir LP, so L_D>=value(P,alpha,beta). Thus (6) also gives L-L_D<=38r/3. It does NOT identify Q with L_D or with J_fix, and no old support is frozen.

## 5. Auxiliary factors: unconditional construction given certificates; source-backed existence

Input K says that for every v=3 mod 6 there is a resolution of K_v into (v-1)/2 triangle factors (Kirkman triple-system existence). Its official SageMath 10.8 implementation specification and its RCW71 reference were read, with exact locators in source-audit.json. This is a source-backed mathematical input, not a kernel theorem or a trusted source attestation. The original 1971 paper and original source byte digest were not obtained; that limitation is explicit. The all-order high-load conclusion uses K, and the elementary proof in Sections 3-4 proves the conditional certificate theorem without it.

There is also a source-free schedule covering many arbitrary orders: for v=3m with odd m, divide a block into three m-sets and, for t=0,...,m-1, take the factor

  {(j,m+(j+t) mod m,2m+(j+2t) mod m): j=0,...,m-1}.

Each is a partition, and any pair from different parts determines its unique factor because 2 is invertible modulo odd m. These give m disjoint factors. Whenever hA/2<=a0/3 and hC/2<=c0/3, they implement (6) with no external design-existence input. Full affine resolutions on powers of three and a separately exact-checked resolution of the projective 15-point triples are additional finite implementations. Missing factor sizes are reported, not silently extrapolated.

An abstract all-order implementation using K can enumerate finite triangle-factor lists on v points until a complete resolution is found, with candidate-checkable edge/vertex identities. It terminates by K, but no practical runtime bound or unexecuted large resolution is asserted.

## 6. Boundary and implementation audits

Arbitrary A is used as an actual vertex list: both block schedules are transported by explicit bijections to A0,C0. No affine-subspace premise survives. Equal prefixes (a=r) and p=0 reduce to the previously proved full-prefix case: combine fractional budgets for Q and use the affine full-core construction, including parity loss. They are regression controls, not new discoveries. For q=0 with 0<a<r the high-load theorem does not apply; (2) or the full type LP still identifies face membership. For small inactive rows, direct arithmetic controls avoid an incorrect one-third identity.

The C25 quarter point is outside the one-third face, and the C27 twelfth-valued point is inside it. Their frozen certificates are checked only as scope regressions. Neither is a new counterexample, and no claim to optimize Q on the seven-core example is made. The construction ignores all old fractional denominators and reselects support from the parameters.

The exact checker compares the scalar criterion with a separately formulated six-row type LP; selected full edge-specific cases are compared with two rational implementations. It checks every actual edge of each constructed Q witness, all budgets, total slack, the bound and the objective identity. Parameter and subset coverage is reported literally. Finite checks are not the proof of (2), (6), or input K.

## 7. The first remaining lemma

The full task remains open outside this high-long-budget strip. For example r=9, a=4, c=5, p=q=1 satisfies (2): w=8,t2=0,t1=8,t3=4/3,t0=1/2 yields L=49/3, with full one-third dual. Here q<max(a,c), so the two-block construction cannot allocate ALL cross edges to beta: a C vertex has four cross edges but long budget only one. This is an explicit on-face uncovered input, not a failure of the user's inequality.

The next atomic construction must realize the cross-core triangle mass w in (2), jointly with the within-A alpha resource and the long beta degrees, to within O(r) lost capacity. Treating all old cut lines independently, fixing old z=1 variables, or allowing only linearly many support changes is not justified. There is no theorem for nonuniform dual prices or for several short levels in this candidate. The general one-third face, general two-level target, exact split domination and ProblemContract root remain open. No trusted closure exists. Status: NONTERMINAL_CHECKPOINT.
