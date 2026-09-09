# C28 reproducible arbitrary-subset candidate

Status: NONTERMINAL_CHECKPOINT. verdict=candidate_only; best_verified_result=none.

The unrestricted one-third-face L-Q<=Kr theorem is OPEN. This packet contains an exact face-membership criterion for a,c>=3 and a new high-long-budget construction q>=max(a,c), valid for every actual short subset. Conditional on explicit triangle factors, total unused original core/endpoint capacity is at most 38r. Classical input K supplies such factors in general; its original proof was not audited. The source-free cyclic-factor subregion and all actual test schedules are explicitly described.

Read proof.md and source-notes/c28/source-audit.json before interpreting run success. The final core triangles need not be lines of the old affine coordinate system: Q permits any actual core triple. No old integral support is frozen. Every between-block edge is assigned once; objective loss is charged by capacity, not by number of changed triples.

## Replay

Run from a checkout containing the frozen dependencies, and choose NEW output paths:

```text
python research/artifacts/candidates/c28/subset_checker.py --mode construct --out NEW-construct.json
python research/artifacts/candidates/c28/subset_checker.py --mode types --out NEW-types.json
python research/artifacts/candidates/c28/subset_checker.py --mode named --out NEW-named.json
```

The program hashes c25/extreme_audit.py before importing its two rational LP implementations. Named mode also hashes c27/twelfth-point.json before reading it. These files already exist in main and are not duplicated here. Input dependency SHA-256 values are pinned in the program. All arithmetic affecting certificates is Fraction or integer; one thread, 1 GiB address-space cap, internal deadline 38 seconds and CPU budget 40 seconds. An external wrapper used wall limit 43 seconds in the recorded runs. Missing supplied factor schedules raise LookupError; the unexecuted general KTS existence claim is not fabricated as a run.

construct-results.json has literal labeled Q witnesses and repair traces; types-results.json contains the full 575-row table; named-results.json has the full joint certificates and the first precise low-budget uncovered input. Runtime timestamps/timings may vary on replay; compare mathematical fields and validate the frozen input/output bytes using artifact-manifest.json. All three final runs exited zero. One earlier combined LP probe timed out with unknown child exit; the run-record preserves that failure separately.

The first remaining atom is mixed AAC/ACC triangle realization in the interval test when q<max(a,c), including (r,a,p,q)=(9,4,1,1), L=49/3. Its exact fractional certificate is not a counterexample to the desired inequality. Q is not optimized there.

This is generator-side mathematics and computation, not a trusted source, semantic review, verifier or closure receipt. The n^2/6+o(n^2) asymptotic candidate, restricted O(r) packing gap, whole one-third face, unrestricted two-level target and ProblemContract root remain separate statements. No EvidenceLink, Result or Solution is self-signed.
