# C22 primary-source and statement-faithfulness audit

Status: source-backed inputs to a candidate_only proof; no verifier receipt.
Read date: 2026-09-07.
Repository revision: 4f2601d4b99669a46106a00c7262daf99691e69e.

## S2: fixed-triangle packing

Raphael Yuster, Integer and fractional packing of families of graphs.
Author-deposited PDF: https://arxiv.org/pdf/math/0305350
Its visible text header identifies math/0305350v4 [math.CO], 27 July 2003.

Locators: page 1, Section 1, first paragraph and definitions; page 2, Theorems 1.1 and 1.2; page 3, Section 3, opening paragraph.
The comparison used in C22 is:
    F={K3}, fixed before epsilon;
    nu_F=nu, nu_F^*=nu_star;
    n=|V(G)|, not |E(G)| or auxiliary-hypergraph order;
    each edge has capacity one; copies are edge-disjoint, not vertex-disjoint;
    forall epsilon>0 exists N(F,epsilon) forall n>N forall G:
        nu_star(G)-nu(G)<epsilon*n^2.
There is no minimum-density hypothesis. The initial no-isolates convention is bridged explicitly in C22 without changing triangles or n. The source's auxiliary Lemma 2.3 is not substituted for this graph theorem. The original theorem body and quantifier paragraph, not a search abstract, were read. Only the stated theorem interface is imported; the entire external proof was not re-proved.

Original attribution: P. E. Haxell and V. Rodl, Integer and Fractional Packings in Dense Graphs, Combinatorica 21 (2001), 13-38:
https://link.springer.com/article/10.1007/s004930170003
The publisher metadata is available, but its parsed preview omits formulas and full text was not obtained. It is attribution, not our theorem-text evidence; Yuster's original paper supplies the usable theorem body.

## S1: finite LP strong duality and attainment

Stephen Boyd and Lieven Vandenberghe, Convex Optimization, Cambridge University Press, 2004; author-hosted text identifies seventh printing with corrections, 2009.
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf

Section 5.2.1, printed page 224 (PDF index 237), equations (5.17)-(5.20), gives min c^T x with Ax=b, x>=0 and dual max -b^T v with A^T v+c>=0. Setting w=-v gives C22's signed dual.
Section 5.2.3, printed pages 226-227 (PDF indices 239-240), gives strong duality under Slater's condition and dual attainment for finite optimum. C22 supplies a strictly positive primal feasible point and compactness. No integrality theorem is imported.

## Access limitations

The original PDF body text at the above locators was readable. Web screenshot attempts for Yuster pages 1-3 and the LP display/duality pages returned Internal Error. No successful visual inspection, PDF byte digest, whole-paper proof audit, or source-code execution is claimed. These limitations do not convert a typed original-body statement into an abstract-only citation; they remain declared reproducibility limitations. No source full text is copied into the repository.

## Frozen repository inputs and scope comparison

The following original candidate blobs were read in full at the revision above:
- C18 fractional compression: 74df7921365d605375b2acf9606c4ca52a30f0c3.
- C19 dual rigidity: c198ea5637cd019de7efaa643830e7121d78d351.
- C20 asymptotic rounding: 8373d9c6b7bd02b82080b0ed5ab9e37c9a1e496e.
- C18 LP-faithfulness note: 16be69dcc76597d05fda1e70ff62d7bef61dfeae.
- C20 packing-faithfulness note: cb343b8ebc96f5d66fa8bb88786fa999dcc10e29.

These are Git blob identities, not SHA-256. C22 re-derives the identities and compression, replaces the clique-tree input by separator induction, and uses only C19's slack/dense estimates. It does not rely on C19's unit-gap classification. Historical C01/C04 dependencies are named for traceability, not imported as verified results.

The new proof retains exact edge partition rather than cover; lambda uses equality-constrained fractional edges/triangles; nu_star uses capacity-constrained triangle packing. The result is a uniform o(n^2) upper remainder and dual necessary conditions for INTEGER near-extremizers. It neither supplies O(n), exact split domination, graph edit-distance stability, nor an executable efficient partition algorithm. Source-backed is not a mathematical admission level. The original candidates remain unchanged.
