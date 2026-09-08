# C26: global core reselection with an objective-loss invariant

Candidate: candidate:erdos81-a01-c26-dense-core-repacking
Repository: vibemathing/problem-erdos-81-chordal-clique-partition
Problem: problem:erdos-81-chordal-clique-partition
Attempt: attempt:web-20260906-erdos81-a01
Route: route:split-extremal-reduction-v1
Graph: graph:erdos81-initial-v1
Transport obligation: obligation:erdos81-split-extremal-reduction
Base: b285b1755081c7b034a2e57eb4f21a29ce9cd39d
Primary owner: math-proof. Verdict: candidate_only. best_verified_result: none.

## 1. Statement identities and the new restricted theorem

Let G(r,a,b,p,q) have clique core [r], p independent short leaves adjacent to [a], and q independent long leaves adjacent to [b]; there are no other edges. Integers satisfy 0<=a<=b<=r and p,q>=0. All packing is EDGE-disjoint. The joint fractional variables are alpha_e on K_[a], beta_e on K_[b], and z_T on actual core triangles. Each core edge has the single constraint

  alpha_e+beta_e+sum_(T containing e) z_T <= 1,

and the tagged endpoint constraints are deg_alpha(u)<=p and deg_beta(u)<=q. Missing variables are zero. Its optimum f is exactly nu_star(G), by aggregation and uniform redistribution to the leaves. J is the all-integer optimum. Q restricts z to an integer core packing but leaves alpha,beta fractional. Thus J<=Q<=f. The full target f-Q<=K*r for all capped two-level instances is OPEN.

Define p0=min(p,max(a-1,0)), q0=min(q,max(b-1,0)), and

  h=min(p0+q0,max(b-1,0)).

These are degree bounds, not an assumption that leaf vertices disappear or that cp is unchanged. This candidate proves the following restricted theorem, relative to the precise source-backed decomposition theorem S1 below:

There is an absolute R such that for every r>=R and every such parameter tuple with h<=r/20,

  0 <= f-Q <= f-J <= 2(a+b)/3 + r/6 + 5/3.              (T)

One may take R=max(200,N_S1(1/100)). In particular an absolute K0 exists for which f-Q<=K0*r on this entire restricted class, including its small orders. This is NOT the unrestricted two-level theorem, not exact split domination, and not the ProblemContract cp<=n^2/6+Cn for every chordal graph. No trusted closure or verifier receipt is generated.

The useful difference from C25 is that every old z coordinate, including every z=1, may be discarded and reselected. There is no bound on how many old support objects change. Only the change in objective is charged. Core fractional quarters are permitted in the input and no matching half-integrality of the joint polytope is assumed.

## 2. A source-free exact objective-loss identity

Let m=C(r,2). Remove z from the joint model and retain every core edge at capacity one. Let M be the optimum of this leaf-only fractional LP. It is feasible, bounded and attained; a compact-polytope optimum may be chosen extreme. For any joint feasible solution with total core weight Z and leaf weight U,

  3Z+U<=m,  U<=M,
  Z+U<=U0 := (m+2M)/3.

Consequently rho=U0-f is nonnegative. This is an upper bound obtained from actual edge capacities, not total leaf spokes treated as independent resources.

Now choose ANY two disjoint integer leaf-allocation graphs A,B satisfying their original prefix and endpoint constraints, write U=|A|+|B|, and choose ANY triangle packing P in the actual residual F=K_r-(A union B). If L is the number of residual edges left uncovered by P, then m=U+3|P|+L and

  f-(|P|+U) = [2(M-U)+L]/3-rho.                        (I)

Every object on the right refers to the current allocation, not the old LP support. This is the global accounting invariant. In particular, many support changes with no lost objective cost nothing in (I).

The unrestricted sufficient charging criterion is to construct A,B,P with

  2(M-U)+L-3rho <= C*r.

One must not require or infer L=O(r) in every parameter region: the nonnegative LP slack rho can compensate for a large leave. No such global construction is proved here. Sections 3-5 prove it when h<=r/20, by bounding both positive charges separately.

## 3. Rounded leaf allocation without freezing core triangles

Solve the leaf-only LP anew on the FULL core K_r. Use the exact rank-and-tagged-endpoint injection proved in C25, Section 2, now with the integer core packing empty. Its premise is valid here: all local edge capacities equal one.

For completeness the dependency is precise. At an extreme leaf optimum each fractional core-edge group has a local two-sided direction, either in one positive coordinate when its edge capacity is slack or in direction (1,-1) when two fractional coordinates sum to one. The projections onto active tagged endpoint rows are linearly independent. A finite augmenting-path matching injects groups into at most a+b such rows. Delete those groups. Each loses at most one unit of objective, and nonnegative capacities cannot increase. The surviving coordinates are zero or one and define disjoint A,B, with

  D:=M-U <= a+b.                                         (2)

This is a use of C25's conditional lemma after a DIFFERENT preprocessing step, not a claim that the old fractional residual capacities are integral. The graph H=A union B is simple. Every vertex has degree at most p0+q0, and every H edge is within [b], so

  Delta(H)<=h,  delta(F)>=r-1-h.                         (3)

This statement includes empty layers, equal prefixes and arbitrary repetitions. Equal prefixes may stay separately tagged: the proof never merges their degree systems or assumes such merging preserves J. Multiple descriptions of one maximal clique create no new edge. Parity does not enter the leaf rounding.

## 4. Linear divisibility repair, with explicit maps

We give an executable repair on every sufficiently dense residual F. In the region of (T), r>=200 and delta(F)>=19r/20-1.

### 4.1 A Hamilton cycle without importing a coloring theorem

A simple graph of order r>=3 and minimum degree at least r/2 has a Hamilton cycle. Here is the finite constructive argument used by the checker. Extend a simple path at either endpoint until neither endpoint can extend. All endpoint neighbors lie on the path v_1,...,v_k. The two index sets

  {i: v_1 v_(i+1) is an edge}, {i: v_i v_k is an edge}

are subsets of {1,...,k-1} and their sizes sum to at least r>k-1. A common index closes a cycle through all k vertices by traversing one path segment forward and the other backward. The graph is connected: two components would each have at least delta+1>r/2 vertices. If k<r, some outside vertex has a neighbor on the cycle; break the cycle there to form a longer path and continue. Each such step increases the number of path vertices, bounded by r. The checker implements the extension, closing rotation and cycle-breaking rule and verifies every produced edge.

### 4.2 Repair odd degrees on the Hamilton cycle

Let T be the even-cardinality set of odd-degree vertices of F. On a Hamilton cycle v_0,...,v_(r-1), select edge bits x_i by

  x_i xor x_(i-1) = 1_(v_i in T),

with indices modulo r. The even size of T makes this consistent. The two solutions are complementary subsets of the cycle; choose the smaller, called D0. Then the odd-degree set of D0 is exactly T, |D0|<=r/2, and Delta(D0)<=2. Therefore F0=F-D0 has all even degrees. Each removed cycle edge is charged to its starting vertex in the fixed cyclic orientation, an injection. The half-cycle choice improves the count to r/2.

### 4.3 Repair the edge count without changing parity

If |E(F0)| is 0 modulo three, put D1 empty. If it is 1 modulo three, choose a simple 4-cycle in F0; if it is 2, choose a simple 5-cycle. Delete its edges as D1. Such a cycle exists under our density: take a greedy simple path with L-1 vertices for L=4 or5 and close it with a common neighbor of its endpoints outside the path. The common-neighbor count is at least 2delta(F0)-r >= 9r/10-6, more than the at most three excluded path vertices for r>=200. This also justifies the deterministic greedy implementation.

Deleting a cycle changes every affected degree by two. D1 has at most five edges and is disjoint from D0. Thus R=F-(D0 union D1) is triangle-divisible, and

  Lrepair:=|D0|+|D1|<=r/2+5,
  delta(R)>=r-1-h-4>=19r/20-5>=91r/100.                 (4)

The cycle D1 is charged to at most five fixed residue-repair slots, not to a separator. No graph edge is removed or paid for twice.

## 5. Full core repacking and the theorem's quantifiers

S1 is Dross, arXiv:1503.08191v3 (21 July 2015), Theorem 7, printed page 3. It states that for each FIXED epsilon>0 there is N(epsilon) so every triangle-divisible graph of order s>=N(epsilon), minimum degree at least (9/10+epsilon)s, has a triangle decomposition. Triangle-divisible means all degrees even and edge count divisible by three. The theorem depends on the fractional-to-exact transfer of Barber--Kuhn--Lo--Osthus, explicitly named in Dross Theorem 6. It is an exact integer decomposition theorem, not an o(s^2)-leave theorem.

Fix epsilon=1/100 ONCE. Apply S1 to the repaired core graph R, whose order is r, not the original r+p+q. All simplicity, parity, edge-count, order and minimum-degree hypotheses were verified in (4). Residual chordality is neither used nor asserted. A triangle decomposition P of R has

  |P|=(m-U-Lrepair)/3.

Together with A,B it is a genuine integer joint allocation, so J>=|P|+U and Q>=J. Substituting (2) and (4) into (I) and discarding only the NONNEGATIVE rho proves (T).

For a literal finite algorithm after repair, enumerate core triangle partitions of R by selecting the least uncovered edge and branching over its possible third vertex. Each recursion removes three edges. The finite tree terminates, and S1 guarantees a successful branch when its hypotheses hold. No practical runtime bound or execution of this enumeration on the large tested cores is claimed. The proof imports S1; the checker checks density/divisibility on those cores, not S1 itself.

For all small orders, every triangle of the host contains at least one core edge, whence f<=m. Let R0=max(200,N(1/100)). For r<R0, f-Q<=r(r-1)/2<=(R0-1)r/2. For r>=R0, (T) is at most 2r. Thus K0=max(2,(R0-1)/2) is a single finite constant valid on the stated restricted class for every r; r=0 is direct. No numerical value for the source threshold N is asserted and epsilon is never set to 1/r.

## 6. What is and is not executed

repacking_check.py imports the frozen C25 exact module only after verifying its SHA-256. It computes the NEW mixed integer/fractional value Q in two ways: forward enumeration of compatible core-triangle masks with a rational tableau residual LP, and reverse exact-decomposability enumeration with a separately implemented revised-basis residual LP. It compares these with two joint LPs and two integer J searches on every boundary-inclusive capped tuple through core order four. The old quarter-valued input is a single extra regression; its original support is not frozen.

The checker independently validates Hamilton rotations on every small input in its recorded range, the parity recurrence on every even vertex subset through order nine, small completed residual decompositions, larger divisibility/density witnesses, and twelve error injections. Its process record states actual time, versions, arithmetic, memory, exit code and output digests. Finite checks do not prove (T), S1, an all-order full two-level bound, or trusted admission. Source byte/visual acquisition limitations are explicit in the source note.

## 7. First remaining lemma

For the full capped parameter space, h may be a positive fraction of r larger than 1/20. Maximizing the leaf allocation can then leave a core too sparse for S1. Do not infer any failure of f-Q<=Kr from that. Nor is it legitimate to add edges to R, spend another type's capacities, or freeze the old z=1 triangles to invoke S1.

The exact remaining construction problem is to choose disjoint A,B and a completely reselected core packing P so that the net charge in (I), namely 2(M-U)+L-3rho, is O(r), allowing arbitrarily many support changes. In the unresolved high-load region a bound on L alone can be too strong; it must be compared with the exact LP slack rho. A concrete next atomic test is to partition the residual into a bounded number of dense blocks while allocating each between-block edge once, and prove that the boundary leave is paid by 3rho plus O(r), rather than by a sum of squared separators. That compensation inequality has NOT been proved.

For many prefix types, the C25 leaf injection has one tagged endpoint family per type and can cost the sum of their prefix sizes. The present argument neither reduces that sum to O(r) nor establishes a many-level invariant.

Status: NONTERMINAL_CHECKPOINT. The unrestricted two-level, nested, exact split-domination and ProblemContract claims remain open. All results here are candidate_only with source-backed S1, not a trust-separated verifier attestation.
