# C29: exact low-budget core values and a mixed-type seed lifting theorem

Candidate: candidate:erdos81-a01-c29-mixed-core-lift
Repository: vibemathing/problem-erdos-81-chordal-clique-partition
Problem: problem:erdos-81-chordal-clique-partition
Attempt: attempt:web-20260906-erdos81-a01
Route: route:split-extremal-reduction-v1
Graph: graph:erdos81-initial-v1
Transport obligation: obligation:erdos81-split-extremal-reduction
Base: efda0a82d20357a02cfccbd16a343c4c57b2da5d
Owner: math-proof. Verdict: candidate_only. best_verified_result: none.

## 1. Exact boundary

The core is K_r on V. Its actual short set A has size a; C=V\A has size c. There are p independent short leaves adjacent to A and q independent long leaves adjacent to all V, and no other leaf edges. The original graph has r+p+q vertices. In particular the requested nine-CORE instance has ELEVEN graph vertices.

Write L=nu_star. Its joint model has z_T on actual core triples, alpha_e on AA edges and beta_e on all core edges. Each core edge e has one constraint alpha_e+beta_e+sum_{T contains e}z_T<=1. The tagged degree bounds are deg_alpha<=p at A and deg_beta<=q at V. Q requires only z integer; J requires all coordinates integer; nu additionally assigns the two edge graphs to actual leaf matchings. Thus nu<=J<=Q<=L. Neither Q nor J is a frozen-support optimum J_fix. L_D restricts allowable core triples to a newly specified family D; it does not fix their weights to one.

On the full one-third optimal-dual face, L=(M+ap+rq)/3 with M=C(r,2), and for every feasible point of value v,

    3(L-v)=S_core+S_short+S_long.                         (I)

Every column has three unit entries, so (I) is exact counting. The full dual prices, including all active tagged rows, equal 1/3; mere feasibility of those prices does not prove their optimality. A saturated primal below proves membership whenever it is claimed.

This candidate completely determines L,Q,J,nu,cp on (r,a,c,p,q)=(9,4,5,1,1), proves an all-order exact Q formula for p=q=1 on r=3^k, k>=2, and proves a mixed-seed lifting lemma. A finite 27-core seed yields a NEW family with arbitrary growing extra budgets, a=4r/9 not an affine-subspace size, and q<max(a,c). The whole low-long-budget face, other short proportions/budgets, the general two-level problem, exact split domination and the ProblemContract remain OPEN. No trusted closure or verifier receipt is asserted.

## 2. A general parity lower bound for actual capacity loss

Let P be any integer core packing of a Q-feasible point. Let F=K_r-E(P), and let d_v be the INTEGER degree of v in F. Since every selected core triangle removes two incident edges,

    d_v = r-1 (mod 2).

Set B_v=p+q for v in A and B_v=q for v in C. Let u_v be the total incident alpha/beta mass at v. Then 0<=u_v<=min(d_v,B_v). Allocate half of every unused core-edge capacity to each endpoint. Together with its unused endpoint budgets, vertex v is charged

    s_v=(d_v-u_v)/2+(B_v-u_v)
       =d_v/2+B_v-3u_v/2.

These charges sum EXACTLY to S=S_core+S_endpoint. If d_v<=B_v, then s_v>=B_v-d_v. If d_v>=B_v, then s_v>=(d_v-B_v)/2. Consequently s_v>=1/2 whenever B_v has parity different from r-1, and s_v>=0 otherwise. On the uniform face,

    L-Q >= o/6,
    o=|{v: B_v not congruent to r-1 modulo 2}|.          (P)

This is a bound for arbitrary core reselection. It does not count support distance or freeze an LP extreme point. Fractional alpha/beta of any denominators are allowed. Zero tagged budgets and coinciding short/long neighborhoods cause no change in the counting argument. Small inactive rows must have their actual zero budgets rather than be assigned nonexistent resources.

## 3. The nine-core instance is solved exactly

Let A={0,1,2,3}, C={4,5,6,7,8}, short leaf X=9 and long leaf Y=10. The two maximal cliques are A union {X}, and V union {Y}. There are 49 edges.

A full fractional certificate puts alpha_e=1/3 on AA; beta_e=1/5 on AC, beta_e=1/20 on CC, beta_e=0 on AA; core AAA triangles have weight 1/3, ACC triangles 1/5, CCC triangles 1/20 and AAC triangles zero. Every actual core edge and tagged endpoint row saturates. Its value is 49/3, equal to the full all-one-third dual. These are the C28 fractional totals, now used as a certificate, not as immutable integer type demands.

A NEW integer core packing is

    026, 037, 048, 138, 146, 157, 247, 258, 356.          (N)

Its exact residual core is the disjoint union of cycle (0,1,2,3,4,5) and triangle (6,7,8). Set alpha01=alpha23=1; beta12=beta34=beta05=1; beta67=beta68=beta78=1/2. All other leaf coordinates are zero. This Q point has value 9+2+9/2=31/2. All endpoint budgets saturate. The only unused core capacity is edge45 of mass one and half of each edge of 678, totaling 5/2.

There are five mismatched vertices in (P), namely C. Hence L-Q>=5/6, and this point attains equality:

    L=49/3, Q=31/2, L-Q=5/6.                            (NQ)

The core in (N) has three AAC and six ACC triangles, not the old fractional type proportions. The difference is allowed and charged through (I), rather than by preserving those type counts.

For the actual integer host packing, use (N), triangles 019,239 through X and 12Y,34Y,05Y,67Y through Y. These are 15 edge-disjoint triangles. The six odd-degree graph vertices are 4,5,6,7,8,Y. Any triangle packing has a leave with these odd vertices and hence at least three edges. Since the graph has 49 edges, its leave is 1 modulo 3 and therefore has at least four edges. Thus nu=15. Counts p=q=1 make every integer allocated leaf graph already a matching, so J=nu=15. This establishes

    (L,Q,J,nu)=(49/3,31/2,15,15).

The partition consisting of K_{10} on V union {Y}, plus the four edges from X, gives cp<=5. For the lower bound suppose fewer than five clique blocks suffice. Restrict their incidence vectors to the ten vertices of that K10. Every pair of distinct incidence rows has inner product one. If a row belongs to only one block, that block contains the whole K10; then none of its internal edges can be reused and the four X edges require four extra blocks. Otherwise all ten row norms squared d_i are at least two. The incidence Gram matrix is 11^T+diag(d_i-1), positive definite of rank ten, whereas a matrix with fewer than five columns has rank less than five. Contradiction. Hence cp=5. No floating optimum is needed for any of these bounds.

## 4. An exact all-order p=q=1 slice with arbitrary short cardinality

For r=3^k, k>=2 and 2<=a<=r, let c=r-a. Every such graph is on the uniform face, and

    L-Q = c/6                    if c>=2,
    L-Q = 2/3                    if c=1,
    L-Q = 0                      if c=0.               (U1)

The special c=1 value is not obtained by simply rounding the parity bound. All actual short subsets of a given size are handled by an explicit relabeling; affine alignment of the GIVEN subset is not assumed.

### 4.1 Fixed nine-core templates

Use the SAME core packing (N) and its residual C6+C3. In the abstract nine-set choose these short subsets:

 a0=2: {0,1}; a0=3: {6,7,8}; a0=4: {0,1,2,3};
 a0=5: {0,1,6,7,8}; a0=6: {0,1,2,3,4,5};
 a0=7: {0,1,2,3,6,7,8}; a0=8: {0,...,7}; a0=9: {0,...,8}.

For a0 in {2,4,5,7}, put alpha01=1, also alpha23=1 when 2,3 are short; put beta12=beta34=beta05=1. On 678 put beta=1/2, and also alpha=1/2 if all three are short. For a0=3,6,9 put beta=1/2 on every residual edge and alpha=1/2 on every residual edge with both endpoints short. For a0=8, put alpha=beta=1/2 on the six-cycle, alpha67=1 and beta68=beta78=1/2. Direct degree counting gives S=c0/2 for c0=9-a0>=2, S=2 for c0=1 and S=0 for c0=0. These are finite explicit templates, all checked by actual edge incidence.

For completeness their uniform-face membership also has explicit fractional certificates. Regard the host as K10 on the nine-core plus Y, and the extra short vertex X. Write d=10-a0. Put weight 1/(a0-1) on every XAA triangle. In the K10, let u,v,w,t be the weights per AAA,AAD,ADD,DDD triangle, where D consists of the nonshort core vertices and Y. Choose:

* If d>=a0+1: u=1/(a0-1) for a0>=3 (zero for a0=2), v=0, w=1/(d-1), t=(1-a0*w)/(d-2).
* If d>=3 and a0<=d+2: u=0, v=(a0-2)/(d(a0-1)), w=(1-(a0-1)v)/(d-1), t=(1-a0*w)/(d-2).
* If d>=3 and a0>d+2: v=1/(a0-1), w=0, u=(a0-2-d)/((a0-1)(a0-2)), t=1/(d-2).
* If d=2: v=w=1/a0, u=((a0-2)/(a0-1)-2v)/(a0-2), t=0.
* If d=1: v=1/(a0-1), u=(a0-3)/((a0-1)(a0-2)), w=t=0.

All displayed denominators are nonzero in their cases and weights nonnegative. The three edge equations are (a0-2)u+d*v=(a0-2)/(a0-1), (a0-1)v+(d-1)w=1 and a0*w+(d-2)t=1 whenever that edge type exists. Thus every host edge saturates, providing the full dual equality. This is a finite seed proof, not an empirical assertion about larger orders.

### 4.2 Global reselection from the nine-core patch

Label the core by F_3^k. The triples {u,v,-u-v} partition every core edge. Choose the first coordinate direction; its parallel class consists of r/3 disjoint triples. A coordinate plane W of order nine contains exactly three of them and twelve affine lines total.

Choose a0 in {2,...,9} with a0<=a, 9-a0<=c and a-a0 divisible by three. Such a choice exists for all r>=9 and 2<=a<=r: for residue zero use 3,6 or9 as needed; for residue one use4 or7; for residue two use2,5 or8. Mark the nine-plane according to the corresponding short template. Mark (a-a0)/3 outside parallel triples wholly short and the rest wholly nonshort. Map these abstract short/nonshort vertices bijectively to the actual A,C.

Start anew from all affine core lines; remove the chosen parallel class and every other line wholly inside W. Insert (N) on W. The result is an integer core packing of exactly (M-r)/3 triangles. On each outside all-short triple put alpha=beta=1/2 on its three edges; on each outside nonshort triple put beta=1/2 only. On W use the template above. It follows by disjoint pair ownership that the total slack is c/2, 2 or0 as asserted. Core edges crossing W or these parallel triples are handled by the retained affine lines and are NOT paid for separately.

A saturated full fractional witness instead uses the saturated template on W and additionally puts core weight 1/2 on each outside nonshort parallel triple. Thus L=(M+a+r)/3 for the full host. Parity bound (P) proves optimality in (U1) when c>=2 and also handles c=0.

For c=1, put h=(M-r)/3, an integer. For any Q point with k core triangles and leaf mass U, U<=r-1/2 and 3k+U<=M. If k<=h-1 its value is at most h+r-3/2; if k>=h+1 it is at most h+r-2. If k=h, its residual graph has r edges and even degrees. The unique nonshort vertex either has positive even degree, forcing at least one unit of unused core capacity because its beta degree is at most one, or is isolated, in which case all leaf allocations lie on r-1 vertices with combined budget two and U<=r-1. Either way the value is at most h+r-1=L-2/3. The template attains this. This proves the exceptional value exactly.

This constant-budget slice sharpens the already known asymptotic restricted bounds; it is not presented as solving arbitrary growing p,q.

## 5. A zero-defect mixed seed with growing-budget consequences

seed27.json explicitly lists 104 core triangles, 12 alpha edges and 27 beta edges for

    (r0,a0,c0,p0,q0)=(27,12,15,2,2).

Every core edge occurs exactly once across the three lists, every short endpoint has alpha degree two, and every core endpoint has beta degree two. Therefore the joint point is integral and saturates every row. Its value 143 equals

    (C(27,2)+12*2+27*2)/3=143.

The core triangle type counts are (AAA,AAC,ACC,CCC)=(8,29,50,17): the seed handles substantial mixed-core traffic. No assertion that arbitrary rounded type totals are realizable is used. The finite lists were found with bounded floating MILP, but proof use consists solely of exact incidence identities in those lists and the displayed weak dual. The discovery solver's status is not a proof input.

Alpha is the cycle (0,9,4,2,5,7,8,6,1,11,3,10). Beta is the union of cycles (0,14,8,5,16,11,20,21) and (1,12,4,24,3,19,26,13,2,15,7,25,18,9,23,10,17,6,22). In particular Q=J=L=143 does NOT mean nu=143. Alternating colors on the alpha cycle, the even beta cycle, and the odd beta cycle after deleting its closing edge give an actual 142-triangle host packing. Only the two long leaves have odd degree, and the host has 429 edges, so a nonempty leave has at least three edges. Thus the actual host has nu=142. This is an additional scope check, not a target counterexample.

## 6. Saturated-seed lifting: an explicit general repacking lemma

Suppose a fixed finite base core K_R with short set A0 of size A admits a row-saturated joint point (P0,alpha0,beta0), where P0 is an INTEGER core packing and endpoint budgets p0,q0 are integers. No restriction to an old affine reservoir is imposed. Let m=3^h, h>=0, and take integers x,y>=0 with x+y<=m-1. Replace each base core vertex u by a fiber {(u,i):i in F_3^h}. The new short set is the union of the A short fibers; after construction an arbitrary bijection maps it to any given actual subset of size A*m. Set

    r=R*m, a=A*m, p=m*p0+x, q=m*q0+y.                  (B)

For an empty short set take p0=x=0. Equal short/full sets are allowed by the same tagged fractional split below. The construction respects the original capped domain whenever the base satisfies the corresponding endpoint inequalities.

### 6.1 Between-fiber pairs have exactly one owner

For each selected base triangle {u,v,w}, ordered once, insert all m^2 triples

    {(u,i),(v,j),(w,-i-j)}   (i,j in F_3^h).            (L)

Each pair between two of its fibers uniquely determines the third coordinate. Hence (L) partitions the three complete bipartite edge sets. If a base core edge instead has alpha0/beta0 mass, assign those same masses to EVERY pair between its two fibers. Its combined mass is one, because the base is saturated and P0 is integral. Base ownership guarantees that these assignments cannot conflict with any inserted triangle. At each fiber vertex the resulting tagged degrees are exactly m*p0 and m*q0 where applicable. This is global block repacking, not separate repairs of old cut affine lines.

### 6.2 Within-fiber saturation and optimal parity rounding

Affine lines partition K_m, and each direction is a triangle factor contributing degree two at each fiber vertex. In a short fiber let t=x+y; in a nonshort fiber let t=y. Choose floor(t/2) complete directions. If t is odd choose one additional direction with mass 1/2. These directions exist because t<=m-1.

Write gamma=1,1/2 or0 on the edges of the selected whole, selected half, or other direction lines. In a short fiber split gamma into alpha=(x/t)gamma, beta=(y/t)gamma when t>0; at t=0 both are zero. In a nonshort fiber put beta=gamma. For a full fractional witness assign core line weight 1-gamma. All within-fiber rows saturate and therefore (B) belongs to the full uniform face.

For the Q witness keep ALL leaf masses but round the core line weights DOWN: a half-selected line receives core weight zero rather than 1/2. Complete unselected lines have weight one. This does not increase any capacity. Endpoints stay saturated. In an odd-budget fiber only the half-selected factor has unused core capacity, namely 1/2 on each of its m edges, total m/2. Each endpoint sees exactly two such half-empty edges; assigning half an edge's unused capacity to each endpoint charges exactly 1/2 to that vertex. No other vertex is charged. Thus

    S_endpoint=0,
    S_core=[a*((x+y) mod2)+(r-a)*(y mod2)]/2.            (C)

There is no factor counting how many old support objects changed. Every edge's ownership follows from its base edge or its one within-fiber line. All steps are finite explicit loops; construction and validation need O(r^2) objects for a fixed seed.

Since the base is saturated with integral P0, its combined leaf budget at each vertex is congruent to R-1 modulo two. Since m is odd, the mismatch count in (P) for (B) is exactly a*((x+y) mod2)+(r-a)*(y mod2). Therefore (C) ATTAINS the universal parity lower bound:

    L-Q=[a*((x+y) mod2)+(r-a)*(y mod2)]/6.               (E)

This proves a general lifting lemma conditional on a finite saturated seed. It does not prove that every parameter tuple has such a seed, or that arbitrary fractional seeds can be lifted with only linear loss. A seed with positive slack would multiply its cross-fiber slack by m^2.

### 6.3 The new low-long-budget family

Apply the lemma to seed27.json. For every m=3^h and every x,y>=0 with x+y<=m-1,

    r=27m, a=12m, c=15m, p=2m+x, q=2m+y,
    L=(C(r,2)+ap+rq)/3,
    L-Q=[12m*((x+y) mod2)+15m*(y mod2)]/6 <= r/6.       (F)

All sizes and both repetitions grow. The short size 12m is not a power of three, so this is not the C27 affine-subspace theorem. The combined load is at least 4m>r/20, and q<=3m-1<max(a,c), so neither the old dense-low-load nor the high-long strip supplies this result. The core order is a power of three and ANY actual short subset of cardinality 12m is handled by relabeling. The result is not asserted for other cardinality ratios.

The permutation exchanging base vertices 0 and1 preserves the short set and maps the seed to another row-saturated point. The two core supports differ in exactly twenty base triangles. Their lifts differ in exactly 20*m^2 cross-fiber triangles; the full within-fiber systems are invariant as sets. Both witnesses have the same value and the same capacity defect. At x=y=0 both are optimal with zero defect. Thus the rule can change Theta(r^2) old triangles at zero objective loss, without imposing any reopening limit.

## 7. Verification boundaries, negative tests and the remaining obligation

The all-order arguments in Sections 2,4,6 are proved symbolically using finite counting and the listed seeds. No Kirkman/Dross/regularity or detachment theorem is imported. Exploratory literature queries are not treated as proof inputs. Source dependence on C25 is computational only; its exact module is SHA-256 checked before use. The old quarter-valued example is checked as outside this face; the frozen twelfth-valued point is checked as on-face with rank28. Its Q optimum is not inferred. Fractional leaf weights of other denominators are permitted by the constructions.

The checker compares two exact rational implementations of the six-resource symmetry quotient for the nine-core L, and two exact residual leaf LPs after deleting columns forced zero by zero-capacity rows. An explicit full edge-specific primal plus full one-third dual separately certifies L. Q is globally optimal by the parity proof, not by claiming to exhaust all nine-core packings. The actual integer packing, its leave and the five clique blocks are checked by full graph incidence. The all-order p=q=1 construction and seed lift are checked over precisely recorded finite ranges; they are not extrapolated from these ranges.

An initial oversized combined full-edge revised-LP probe hit the tool timeout with no completed process/output record. Its child exit is unknown; the later reduced exact runs do not rewrite that failure. Twelve mutations include negative capacities, duplicate edge ownership, invalid short edges, fractional core variables in Q, omitted endpoint deficit and out-of-domain fiber budgets.

One auxiliary construction trap is explicit: K9-(C4 union C5) has 20 cross edges between the four- and five-vertex parts. A full decomposition would have nine triangles, each using at most two cross edges, so it cannot exist. We use the certified C6+C3 leave instead. This is a residual-design obstruction, not a counterexample within the chordal-host target class or a new root failure.

The remaining task is to implement EVERY low-budget uniform-face parameter, not just (U1) or (F). The interval in C28 controls fractional type totals; no theorem here realizes arbitrary such totals by an integral core. The next concrete obligation is a bounded-slack mixed seed/completion scheme whose scale and short-set ratio are not restricted to one finite seed family. It must control actual lost objective even when no row-saturated integral-core seed exists (the nine-core example already shows this can happen). A fractional base cannot simply be blown up because its error scales quadratically. Nonuniform duals, several short levels, exact split domination, the ProblemContract root and trusted admission all remain open.

Status: NONTERMINAL_CHECKPOINT; verdict=candidate_only; best_verified_result=none.
