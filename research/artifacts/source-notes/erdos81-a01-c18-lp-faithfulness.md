# C18 source-faithfulness note: finite LP duality and the parameter boundary

Status: candidate_only. Retrieval: 2026-09-07. No novelty or current-best assertion.

## Primary LP input

Stephen Boyd and Lieven Vandenberghe, Convex Optimization, Cambridge University Press, 2004; retrieved author-hosted version identifies the seventh printing with corrections, 2009.
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf

Section 5.2.1, printed page 224 (PDF index 237), displays the standard-form primal min c^T x with Ax=b, x>=0 and the equivalent dual maximize -b^T v with A^T v+c>=0. Setting w=-v gives exactly the free-sign dual used in C18. Sections 5.2.3-5.2.4, printed pages 226-227, give LP strong duality and dual attainment under feasibility with finite optimum. C18 supplies both feasibility and boundedness directly. No integer integrality theorem is being imported.

Parsed text of those sections was read. Web screenshot requests for PDF indices 237 and 240 failed; no visual inspection, whole-book reading or PDF digest is claimed. Only this bounded statement comparison is retained.

A second MIT course-notes extract had inconsistent min/max and inequality signs in its parsed strong-duality display. Its screenshot requests also failed. It was not used to replace or modify the exact LP statement above; no determination about a printed typographical error is made.

## Structural input and reuse relation

C04, `research/artifacts/candidates/erdos81-a01-c04-deficit-one.md`, Section 2 at base 835590bb3ce8016b41e6b96b7d57f39b5083d754, supplies the clique-tree proof of a PEO ending at a specified maximal clique. C18 explicitly extends that argument to any clique by reordering the terminal complete graph. The clique-tree/PEO theorem input was scoped by C01 source S3. This is a proof dependency, not a verifier receipt.

C01 supplies the complete-split benchmark and an integer matching construction; C07 supplies the exact residual-state obstruction. Reusing their arguments does not import a mathematical status from merge or CI.

## Exact statement difference

The new parameter lambda is an equality-constrained fractional edge-and-triangle partition, not a clique cover, not a vertex partition, and not the integer cp in the frozen contract. Its signed dual compression controls all chordal graphs, while an additive integer rounding estimate remains unproved. The J(3,2) and K4 witnesses in C18 make the differences explicit.

Searches for chordal fractional clique partitions also returned distance-multigraph decompositions and vertex-disjoint triangle packing. Those objects do not match this LP and were not used as graph theorems. No search result establishes priority or resolves the remaining rounding obligation.
