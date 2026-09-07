# C06 source comparison and literature checkpoint

Verdict: candidate_only. Retrieval date: 2026-09-06. No source hit, repository merge, or webpage status is mathematical verification.

## Frozen definitions and structural reuse

The repository ProblemContract at a151526269cc0f2972243ce96e7d413dc0d4f5c8 asks for an exact edge partition, not a cover or a vertex partition. C06 uses the clique-tree characterization already scoped in C01 source S3, and the explicit matching construction in C01. The C06 family has a directly displayed PEO, so its chordality does not depend on a newly located theorem.

The existing S3 source is Bochuan Lyu and Illya V. Hicks, "Finding Biclique Partitions of Co-Chordal Graphs", arXiv:2203.02837v2, Section 2:
https://arxiv.org/html/2203.02837v2
Its journal version is Discrete Applied Mathematics 337 (2023), 278-287, DOI 10.1016/j.dam.2023.05.001. The publisher abstract was retrieved in this cycle. Its main parameter is biclique partition number of a co-chordal graph, not cp of a chordal graph. Only the structural theorem from the previously scoped Section 2 is reused. The arXiv HTML request in this cycle did not return a fresh readable full text.

## Original chordal source

P. Erdos, E. T. Ordman, Y. Zalcstein, "Clique Partitions of Chordal Graphs", Combinatorics, Probability and Computing 2(4) (1993), 409-415, DOI 10.1017/S0963548300000808.
https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/clique-partitions-of-chordal-graphs/CEA1F929F2A88B5A4C7C8E23DFD0DD29

The publisher abstract reports a quadratic lower example at n^2/6 and a general upper bound (1-c)n^2/4 for some c>0. December 1993 is the issue date; the 2008 online date is not a new mathematical result. The retrieved publisher summary of the 1997 reprint explicitly distinguishes coverage at least once from partition exactly once:
https://www.cambridge.org/core/books/abs/combinatorics-geometry-and-probability/clique-partitions-of-chordal-graphs/342329633D5A1341FC9A80CA211970EC
DOI 10.1017/CBO9780511662034.027, pp. 291-298. Its historical reference to the de Bruijn-Erdos proper partition lower bound does not give the desired chordal upper bound.

## Problem-page and split-paper lead

The search-indexed problem page and its LaTeX source retain the frozen question:
https://www.erdosproblems.com/81
https://www.erdosproblems.com/latex/81

They attribute a split-graph upper bound 3n^2/16+O(n) to G.-T. Chen, P. Erdos and E. T. Ordman, "Clique partitions of split graphs", Combinatorics, graph theory, algorithms and applications (Beijing, 1993), World Scientific (1994), pp. 21-30. The page's reported edit date is 2025-12-28; search results are not a guarantee of the latest literature status in September 2026.

Author-hosted primary-paper locator:
https://ordman.net/MathResearch/CEOClique_Parts.pdf
The full text was not obtained in this cycle. The numerical 3/16 statement is recorded as the problem page's attribution, not as a theorem whose primary proof was checked. It is not used in C06. No claim of the exact current-best coefficient is made.

No original theorem solving the frozen root was located in the retrieved material. Recent conditional-bound and explicit-constant leads were not upgraded into proof inputs without an accessible primary proof. Searches involving de Caen, Fisher-type bounds, and Erdos-Hanani do not by themselves supply an edge-partition upper bound; C06 invokes none of them.

## Relation to the new candidate

The clique-tree deficit identity and the G(k,t,d) construction are written derivations in C06, not claims attributed to these papers. The exact cp certificate matches a signed lower weighting with an explicit partition. No novelty or exhaustive literature-completeness assertion is made. The root and unrestricted split reduction stay open.
