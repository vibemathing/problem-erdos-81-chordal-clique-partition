# C14 source and statement comparison: deletion-sensitive split partitions

Verdict: candidate_only. Retrieval date: 2026-09-06.
Repository input revision: 024685ec89fbb07a314477a97c2d8177dd844574.

## Primary theorem and exact reuse boundary

D. R. Stinson, "A new proof of the Doyen-Wilson theorem", J. Austral. Math. Soc. (Series A) 47 (1989), 32-42; DOI 10.1017/S1446788700031177.
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EE5D4035844A6D45B857385D25E0B981/S1446788700031177a.pdf/a-new-proof-of-the-doyen-wilson-theorem.pdf

The primary PDF's parsed text was obtained during this continuation. Its definition of an incomplete pairwise balanced design reserves all pairs inside the hole, and covers every other pair exactly once. The C11 source note records an earlier successful visual inspection of the theorem on printed page 41, including the >= threshold; this continuation's screenshot request failed with Cache miss. No new visual confirmation or full-proof audit is claimed, and damaged parsed inequality glyphs are not used to change C11's frozen theorem statement.

C14 reuses the graph construction in C11, Sections 2-3: a complete split graph with core size r>=t has a partition costing at most (r^2+2rt)/6+4r. Crucially, every mixed piece is a triangle or an edge. The theorem alone is not attributed as a statement about cp of arbitrary split graphs.

## Candidate derivations and scope differences

C08's matching-allocation argument and C01's explicit cyclic matching decomposition are internal proof-draft inputs. C14 derives the additional cost of deleting absent crossing edges by inspecting the surviving edges of EACH piece. A mixed triangle with one missing crossing edge becomes a path and costs two pieces, not one. This is the new graph conversion that must be audited separately.

The finite core-label average retains sum_x d_x(r-d_x), hence the variance of neighborhood sizes. The uniform radical coefficient in C14 and its scalar optimization are derived in the candidate, not quoted from the design paper. They are weaker than the desired 1/6 leading coefficient, and apply to all split graphs rather than all chordal graphs.

A second primary bibliographic target remains Guan-Tao Chen, Paul Erdos, Edward T. Ordman, "Clique partitions of split graphs", Combinatorics and Graph Theory '93 (1994), pp. 21-30, author locator https://ordman.net/MathResearch/CEOClique_Parts.pdf . The full-text request did not yield readable text in this continuation; the author academic-page request also timed out. Thus no exact comparison with that paper's best coefficient, and no present-day priority or novelty claim, is made. Nearby biclique or overlapping-cover results are not substituted.

## Verification boundary

These source comparisons do not close the target or root. C14 has the declared C11 design dependency plus its own deletion, averaging, and algebraic obligations. No mathematical solver, enumeration or proof-assistant run occurred. Local hashing processes candidate UTF-8 bytes for transport only. Source text and passing candidate CI do not supply mathematical Evidence.
