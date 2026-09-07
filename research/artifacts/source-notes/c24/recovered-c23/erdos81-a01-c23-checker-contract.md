# C23 exact checker: design and replay contract

Status: `pending/unverified` code candidate. The source was syntax-parsed only; it was not imported or run as a mathematical program. This note is a ToolPlan, not a receipt. The current Web profile prohibits command execution, and no general trusted computation trigger was exposed.

## Intended two implementations

A: maximize triangle packing using a full rational tableau, standard nonnegative slacks, and Bland entering/leaving choices. It returns triangle weights and a nonnegative edge-cover dual. Their capacity, coverage and equal objective are checked from the original triangle list.

B: minimize the exact edge-and-triangle partition directly by revised-simplex bases. Start from the singleton identity matrix, recompute primal basic coordinates and signed dual by exact Gauss-Jordan elimination, and pivot by reduced costs. It does not set lambda=m-2*nu_star. Its independent edge equalities, sign-free dual constraints and equal objective are checked. Both use standard-library Fraction arithmetic; they are different implementations, not different trust domains.

Integer cp/p23 are solved by a pivot-edge residual DP. Triangles for nu are optimized separately by maximum independent set in the triangle conflict graph. Thus the three equalities are tested across separately optimized quantities rather than assigned by definition.

## Finite corpus and completeness argument

For each order n, add a new simplicial vertex with every possible clique neighborhood to every representative of order n-1, then quotient by exact isomorphism. Canonicalization groups vertices by degree and exhausts all permutations within equal-degree blocks. Isomorphic graphs have the same degree classes and permutation minimum; equal minimum encodings are an explicit isomorphism witness. No probabilistic hash or graph-library isomorphism verdict is used.

Induction proves the generator complete: every nonempty chordal graph has a simplicial vertex; delete it, use the representative of its smaller graph, and extend using its actual neighborhood. Conversely adding a simplicial vertex to a chordal graph preserves chordality, because any induced cycle through it of length at least four has a chord between its two cycle neighbors.

A separate recognizer rejects any connected induced 2-regular subset of size at least four. This is exactly an induced cycle, not an invocation of the PEO theorem being tested. Through n=5, an additional loop enumerates all 2^(n(n-1)/2) labeled simple graphs and compares the literal-recognizer/canonicalized set with the constructive set. Every clique subset in each tested chordal graph is also tested as a forced PEO suffix.

The intended full range is all chordal isomorphism classes with 0<=n<=7, plus named negative controls. This range has NOT been executed. No graph-count total is pre-filled as an observed output. The output records the largest fully completed order; an incomplete current order cannot be promoted to that field.

## Regression controls and mutations

Named controls: all small complete graphs and trees; all J(r,t) with r+t<=7, including t=0 and t=r-1; C4; diamond; P6 squared; two K4 windmill blocks. The certificate output for named nontrivial fixtures includes all edges/cliques, fractional primal/dual weights and integer partitions/packings.

Two independent solver optima are tested: the direct signed dual from B and w=1-2q from A's edge-cover dual. Every maximizing clique-neighborhood pair for each returned optimum is checked. This does NOT enumerate the continuous optimal face, for which the written audit supplies uniform arguments.

Twelve injected errors are passed to validation predicates: overlapping cover used as a partition; missing edge; nonclique piece; negative triangle weight; packing overload; uncovered packing-dual triangle; signed-dual triangle violation; fractional cover in place of equality; missing factor two; cp confused with p23; omission of chordality; omission of theta>=0. Detection means the concrete violated predicate raises CheckError, not a dummy always-false test. No mutation has actually run in this Web turn.

## Termination and resource boundary

All mathematical searches are finite. Canonicalization enumerates finitely many permutations; graph generation and subset loops are finite; residual DP strictly decreases the edge mask; conflict search strictly decreases the active triangle set. Bland pivoting applies because both LPs start at a primal-feasible basis, use the least-index improving nonbasic variable and the smallest-index basic variable among minimum-ratio ties. Every pivot also has a declared cap. The general finiteness theorem is not replaced by the caps.

An authorized runner must use a fresh output path, a wall-clock limit at most 1800 seconds, one CPU thread, an external process/memory cap, max 250000 memoized states per integer subproblem, and at most 2000 pivots per LP. The planned internal deadline is 1500 seconds; a tighter external deadline leaves time for checkpoint transport. The default limit applies to each exact DP/LP; the per-process memory limit covers aggregate caches. A timeout is nonterminal, not a counterexample. An arithmetic/identity failure includes its exact graph and clique list.

Proposed invocation, from an authorized repository checkout:

    python research/artifacts/candidates/erdos81-a01-c23-exact-checker.py --max-n 7 --seconds 1500 --state-cap 250000 --pivot-cap 2000 --output c23-check-output.json

The runner must first pass the registered tool probe and compute-plan policy, enforce the external wall time, memory and CPU limits, then record actual Python/build version, checker digest, command, budgets, exit status, output hash, mutation results and largest complete order. No version/exit status/count may be copied from this plan as observed.

The program writes only its specified bounded output, never records, EvidenceLink, Results or Solution. A local self-check success remains a finite candidate observation. A trusted replay must use an eligible separately identified principal, with explicit capability/policy mapping; this source file is not automatically a trusted verifier adapter.

## Source/runtime scope

The code uses Python's standard library, no third-party mathematical API. Target runtime is CPython 3.12 or an explicitly reviewed compatible version >=3.10; actual interpreter identity is pending. File hashing and AST parsing done while preparing this candidate do not test the algorithms. No new admission is inferred from either implementation's authorship or a future test success.

### Checkpoints on failure

The declared output budget is 5 MiB. On timeout, preserve which stage was reached, the last fully completed order and the partial representative count. If timeout occurs during generation, no claim is made about a complete current-order representative list. On a CheckError, preserve the failing graph's exact encoding, edges and all cliques. File-system/runtime exceptions may prevent the script from creating output, so the external runner must separately capture its exit status and transport a bounded diagnostic rather than infer a mathematical result.
