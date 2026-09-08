# C26 replay map

Verdict: candidate_only. No trusted verifier is invoked.

`proof.md` proves the exact objective-loss identity and a source-backed restricted theorem when the combined allocated leaf-degree bound h is at most r/20. The unrestricted two-prefix nu_star-Q=O(r) problem remains open. Do not read the title or CI as a root solution.

## Exact replay

From a repository checkout (preserve frozen outputs), run:

    python research/artifacts/candidates/c26/repacking_check.py --out NEW.json

The program verifies the SHA-256 of the imported C25 module before loading it. It uses Python >=3.11 standard-library Fraction arithmetic, one thread, a 1 GiB address-space cap, a 39-second LP deadline and a 42-second CPU limit. The published run used CPython 3.13.5 with an outer wall cap of 44 seconds. Runtime-dependent JSON fields need not repeat on another machine.

The original full final process output is 22,183 bytes with SHA-256
`315153ef1c73a16cebaa7b9819bc32eba000b93095e4a64220c8a62e3614ac12`.
It is stored losslessly as `repacking-report.json`, `repacking-table.csv`,
`repair-r200.json`, `repair-r220.json`, `repair-r241.json`, `repair-r400.json`,
and `proper-two-prefix.json`. Reconstruct it without executing mathematics:

    python research/artifacts/candidates/c26/reconstruct.py --out NEW-FROZEN.json

The reconstruction refuses an existing output and checks exact size/SHA-256 before writing.
The `exact.rows` columns are:

    r,a,b,p,q,nu_star,Q,J,leaf_only_M,rho,number_of_core_masks

The two Q optimizers enumerate actual core packings in different directions, solve residual rational LPs with different implementations, and agree on all 149 capped boundary-inclusive tuples through core order four. One order-five quarter-input regression is additional; it is not a complete range. The code also validates 37 small Hamilton inputs, all 508 even parity subsets of cycles of orders 3..9, complete decompositions of four small repaired cores, and twelve mutations.

Large repair witnesses at core orders 200,220,241,400 contain the full Hamilton cycle, parity-removal edges and modulus cycle. They are density/divisibility certificates ONLY. They do not contain a full triangle decomposition and do not establish that the external theorem's unknown order threshold has already been passed.

A proper two-prefix certificate at (r,a,b,p,q)=(200,100,200,2,2) has leaf-only optimum 300 and fractional packing value 20500/3. Give each short-leaf triangle weight 1/99 and each long-leaf triangle weight 1/199. Give every core triangle gamma=(1-2/199)/198 and subtract 2/(99*98) on AAA triangles. All weights are nonnegative and the code checks the edge-type loads and objective. Uniform graph-edge prices 1/3 are the matching packing dual. Its integer leaf allocation is an A-cycle and the step-three cycle on the whole core, with disjoint edge sets. Only the repaired residual's divisibility and density, not its integer decomposition, are executed on this larger example.

`source-audit.json` under source-notes/c26 identifies Dross Theorem 7, the fixed epsilon=1/100 specialization, exact hypothesis comparison, and absent PDF-byte/visual/trusted receipts. `process.json` records the actual final exit and output digest. `artifact-manifest.json` binds frozen file bytes. Both small rational programs remain generator-side checks, not separate trust domains.

## Open continuation

In the high-load region h>r/20, maximize the actual joint objective, not the amount of old support kept. The remaining unproved goal is a completely reselected allocation with 2(M-U)+L-3rho=O(r), or a counterexample to that global target. The dense-core argument is not applied when its premise fails. No many-level inference or Evidence/Result/Solution admission is made.
