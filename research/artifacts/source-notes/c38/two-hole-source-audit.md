# C38 source comparison — d6 two-hole and one-hole residuals

Status: source-backed candidate only; no trusted source receipt.

## Bryant--Horsley two-hole theorem

Source: Darryn Bryant and Daniel Horsley, "Steiner triple systems with two disjoint subsystems", Journal of Combinatorial Designs 14(1), 14--24 (2006), DOI 10.1002/jcd.20071.

The public peer-reviewed bibliographic abstract states that a triangle decomposition of `K_v-K_u-K_w` for two vertex-disjoint holes exists iff: (i) `v,u,w` are odd; (ii) `C(v,2)-C(u,2)-C(w,2)` is divisible by three; (iii) `v>=u+w+max(u,w)`.

C38 maps `(u,w,v-u-w)=(a',q',c')`. Its residue repair makes `a',q',c'` all 1 modulo 6. Hence `v'=a'+q'+c'` is 3 modulo 6, the parity and mod-3 conditions hold, and d6 dominance yields `c'>=max(a',q')`, exactly the size condition.

A later paper by Y. Li, Y. Chang and T. Feng, "Triangle decompositions of lambda K_v-lambda K_w-lambda K_u" (Discrete Mathematics; arXiv:1910.03163), reproduces the lambda=1 Bryant--Horsley result as Theorem 1.2. It is used only as a statement cross-check.

## Doyen--Wilson one-hole theorem

The classical Doyen--Wilson theorem states that an STS(u) embeds in an STS(v), for distinct admissible orders, iff `v>=2u+1`. Equivalently, after removing the subsystem blocks, `K_v-K_u` has a triangle decomposition.

C38 repairs `a'=1 mod 6`, `c'=0 mod 6`, hence `v'=a'+c'=1 mod 6`, and ensures `c'>=a'+1`, equivalently `v'>=2a'+1`.

A readable published restatement was located in a later "A new proof of the Doyen-Wilson theorem"; its text explicitly gives the congruence and embedding conditions. The original 1973 paper bytes were not frozen.

## Trust and byte boundary

- Original publisher PDF bytes for Bryant--Horsley: not frozen.
- Original 1973 Doyen--Wilson paper bytes: not frozen.
- source byte SHA-256: null.
- Search-result snippets are not treated as proof.
- The general existence proofs are not reproduced or independently verified.
- Given the stated design blocks, all host ownership/lifting checks are internal to C38 `proof.md`.

This source note supports statement-faithfulness only at the candidate/source-backed level.
