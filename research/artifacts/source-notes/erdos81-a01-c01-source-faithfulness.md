# Source-faithfulness note: Erdős 81, cycle C01

Status: candidate_only. Retrieval date: 2026-09-06. This is bounded bibliographic and statement comparison data, not a proof receipt.

## S0. Frozen repository input
Repository: vibemathing/problem-erdos-81-chordal-clique-partition.
Revision: fff9c7ba9cba18ecfbadd1b70b61edf67b073947.
Paths: problem-library/records/canonical-problems.jsonl; research/records/obligation-graphs.jsonl.
The contract asks for an upper bound on an exact edge partition. The target is an existential same-order split domination statement, not monotonicity of every completion operation.

## S1. Original chordal paper
P. Erdos, E. T. Ordman, Y. Zalcstein, "Clique Partitions of Chordal Graphs", Combinatorics, Probability and Computing 2(4) (1993), 409-415. DOI: 10.1017/S0963548300000808.
Publisher locator:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CEA1F929F2A88B5A4C7C8E23DFD0DD29/S0963548300000808a.pdf/clique-partitions-of-chordal-graphs.pdf

The retrieved publisher response is abstract/metadata HTML, despite the PDF-shaped URL. Its abstract reports chordal examples that are also threshold and split, at quadratic scale n^2/6, and an upper bound (1-c)n^2/4 for some absolute c>0. The issue date is December 1993; the publisher's online date in 2008 is not the original paper date. This is prior art, not the desired n^2/6+O(n) upper bound. The exact best currently available numerical coefficient c has NOT been established by this retrieval.

## S2. Split-graph paper: incomplete full-text access
Guan-Tao Chen, Paul Erdos, Edward T. Ordman, "Clique partitions of split graphs", Combinatorics and Graph Theory '93, World Scientific (1994), pp. 21-30.
Author-hosted locator:
https://ordman.net/MathResearch/CEOClique_Parts.pdf
Author publication-list locator:
https://math.gsu.edu/gchen/research.html

Full-text requests to the first locator failed; author-hosted search-index excerpts and the publication list were available. A short indexed excerpt reads: "We cannot show that this many will suffice." The antecedent concerns n^2/6+O(n). Other indexed formulas lost their coefficients during extraction. We do not infer a numerical split-graph upper coefficient from the damaged excerpts. No PDF digest or full-paper reading is claimed. The indexed complete-split example is compatible with C01.2's self-contained reconstruction.

In particular, these retrievals do not supply a universal split upper bound n^2/6+O(n). The candidate records that root-implication gap; it does not infer the present literature status solely from a 1994 paper.

## S3. Structural theorem reuse, not parameter reuse
Bochuan Lyu and Illya V. Hicks, "Finding Biclique Partitions of Co-Chordal Graphs", arXiv:2203.02837v2, revised 2023-02-16.
https://arxiv.org/html/2203.02837v2
Section 2 states the chordal equivalences with a perfect elimination ordering and a clique tree, and defines split graphs. This is an exact reuse of the structural characterization only. Its main parameter bp counts complete bipartite pieces on co-chordal graphs; those partition bounds are not assertions about cp on chordal graphs. The author's deposited version uses the arXiv perpetual non-exclusive distribution license; this note stores no full text.

## S4. Recent nearby result: a different question
Bo Ning, "On the difference between clique partition and clique covering numbers of graphs", arXiv:2608.11536v1, submitted 2026-08-12.
https://arxiv.org/html/2608.11536v1
https://arxiv.org/pdf/2608.11536

The introduction defines cp and cc separately. Its Theorem 1.2 concerns max_(|V(G)|=n)(cp(G)-cc(G)) over all graphs, with deficit of order n^(4/3) from floor(n^2/4). It is not a solution of the frozen chordal upper-bound question. The introduction cites the 1993 chordal estimate above. The first PDF page was visually inspected; this is a scope comparison, not a correctness audit of the paper's proof.

## Retrieval limitations and next source obligation
The live ErdősProblems problem-81 endpoint did not return readable content in this research step. Its frozen statement remains the repository contract, not a guessed live edit. A secondary search result mentioned a 2026 explicit-constant refinement; no matching in-scope primary proof was retrieved, so it is not used as a theorem or as the current best bound. The Renyi collected-papers index inspected here ends at 1990 and did not expose the 1993/1994 papers.

No claimed source closes the split-extremal reduction, no claimed source upper-bounds every split graph by the attained benchmark B(n), and no exact current-best numerical coefficient is asserted. A later source-only cycle may resolve the missing primary texts without changing the frozen contract.
